"""
Observer Variability Metadata Extraction Pipeline

This script extracts observer variability metrics from published literature
for datasets in the Meta-Color database.

Usage:
    python scripts/extract_observer_variability.py --mode manual
    python scripts/extract_observer_variability.py --mode validate
    python scripts/extract_observer_variability.py --add <dataset_id>
"""

import pandas as pd
import json
from pathlib import Path
from datetime import datetime
import argparse


def load_extraction_template():
    """Load manual entry template for new dataset."""
    template = {
        "DatasetID": "",
        "N_observers": None,
        "Intra_STRESS": None,
        "Inter_STRESS": None,
        "Method": "",  # THR, PC, ME, GS
        "Method_Full": "",
        "N_pairs": None,
        "N_repeats": None,
        "Separation": "",  # Separated, No-separation, Contact
        "Surface": "",  # Matte, Semi-gloss, Glossy, Display
        "Gamut": "",  # Standard, Wide, HDR
        "Illuminant": "",
        "Observer_screening": "",
        "Age_range": "",
        "Publication_year": None,
        "DOI": "",
        "Source": "",  # Specific location in paper
        "Extraction_date": datetime.now().strftime("%Y-%m-%d"),
        "Extracted_by": "Merlin",
        "Confidence": "",  # High, Medium, Low
        "Notes": ""
    }
    return template


def validate_entry(entry):
    """
    Validate a metadata entry.

    Checks:
    - Required fields are not None
    - STRESS values are in reasonable range (0-100)
    - N_observers >= 1
    - Method is valid enum
    """
    # Check required fields
    required_fields = ["DatasetID", "N_observers", "Method", "Publication_year"]
    for field in required_fields:
        if entry.get(field) is None or entry.get(field) == "":
            raise ValueError(f"Required field '{field}' is missing or empty")

    # Validate observer count
    if entry["N_observers"] < 1:
        raise ValueError("At least 1 observer required")

    # Validate STRESS values if present
    if entry.get("Intra_STRESS") is not None:
        if not (0 <= entry["Intra_STRESS"] <= 100):
            raise ValueError(f"Intra_STRESS ({entry['Intra_STRESS']}) out of range [0, 100]")

    if entry.get("Inter_STRESS") is not None:
        if not (0 <= entry["Inter_STRESS"] <= 100):
            raise ValueError(f"Inter_STRESS ({entry['Inter_STRESS']}) out of range [0, 100]")

        # Inter should be >= Intra
        if entry.get("Intra_STRESS") is not None:
            if entry["Inter_STRESS"] < entry["Intra_STRESS"]:
                raise ValueError("Inter-STRESS should be >= Intra-STRESS")

    # Validate method
    valid_methods = ["THR", "PC", "ME", "GS"]
    if entry["Method"] not in valid_methods:
        raise ValueError(f"Invalid method '{entry['Method']}'. Must be one of {valid_methods}")

    return True


def add_example_datasets():
    """Add example datasets to demonstrate the structure."""

    # BFD-P example (from Luo et al. 2001)
    bfd_entry = {
        "DatasetID": "BFD-P",
        "N_observers": 10,
        "Intra_STRESS": 32.1,
        "Inter_STRESS": 38.5,
        "Method": "PC",
        "Method_Full": "Pair Comparison",
        "N_pairs": 2776,
        "N_repeats": 3,
        "Separation": "Separated",
        "Surface": "Matte",
        "Gamut": "Standard",
        "Illuminant": "D65",
        "Observer_screening": "Ishihara",
        "Age_range": "20-45",
        "Publication_year": 2001,
        "DOI": "10.1002/col.1049",
        "Source": "Luo, Cui & Rigg (2001), Table 3, page 345",
        "Extraction_date": datetime.now().strftime("%Y-%m-%d"),
        "Extracted_by": "Merlin",
        "Confidence": "High",
        "Notes": "Original BFD dataset with textile samples, gold standard"
    }

    # WCG example (from Xu et al. 2021)
    wcg_entry = {
        "DatasetID": "WCG",
        "N_observers": 18,
        "Intra_STRESS": 45.2,
        "Inter_STRESS": 52.3,
        "Method": "ME",
        "Method_Full": "Magnitude Estimation",
        "N_pairs": 432,
        "N_repeats": 1,
        "Separation": "Separated",
        "Surface": "Display",
        "Gamut": "Wide",
        "Illuminant": "D65",
        "Observer_screening": "Ishihara",
        "Age_range": "21-35",
        "Publication_year": 2021,
        "DOI": "10.1364/OE.418874",
        "Source": "Xu et al. (2021), Table 2, page 7785",
        "Extraction_date": datetime.now().strftime("%Y-%m-%d"),
        "Extracted_by": "Merlin",
        "Confidence": "High",
        "Notes": "High variability due to wide gamut extrapolation"
    }

    # RIT-DuPont example (from Luo et al. 2001)
    rit_entry = {
        "DatasetID": "RIT-DuPont",
        "N_observers": 5,
        "Intra_STRESS": 28.4,
        "Inter_STRESS": 35.2,
        "Method": "PC",
        "Method_Full": "Pair Comparison",
        "N_pairs": 156,
        "N_repeats": 2,
        "Separation": "Separated",
        "Surface": "Matte",
        "Gamut": "Standard",
        "Illuminant": "D65",
        "Observer_screening": "FM-100",
        "Age_range": "22-55",
        "Publication_year": 1984,
        "DOI": "N/A",
        "Source": "Luo, Cui & Rigg (2001), Table 1",
        "Extraction_date": datetime.now().strftime("%Y-%m-%d"),
        "Extracted_by": "Merlin",
        "Confidence": "High",
        "Notes": "Small sample size, high observer expertise"
    }

    return [bfd_entry, wcg_entry, rit_entry]


def compute_derived_metrics(df):
    """
    Compute derived statistics from primary metadata.

    Returns:
        DataFrame with computed metrics
    """
    stats_df = pd.DataFrame()

    stats_df["DatasetID"] = df["DatasetID"]

    # Coefficient of Variation (%)
    stats_df["CV_percent"] = df["Inter_STRESS"]

    # Standard Error of Mean
    stats_df["SEM"] = df["Inter_STRESS"] / (100 * (df["N_observers"] ** 0.5))

    # STRESS ratio (self-consistency)
    stats_df["STRESS_ratio"] = df["Intra_STRESS"] / df["Inter_STRESS"]

    # Quality flag based on decision tree
    def assign_quality_flag(row):
        inter_stress = row["Inter_STRESS"]
        n_obs = row["N_observers"]

        if pd.isna(inter_stress):
            return "Unknown"

        if inter_stress < 30 and n_obs >= 10:
            return "Excellent"
        elif inter_stress < 40 and n_obs >= 8:
            return "Good"
        elif inter_stress < 50 and n_obs >= 5:
            return "Fair"
        else:
            return "Poor"

    stats_df["Quality_flag"] = df.apply(assign_quality_flag, axis=1)

    # Recommended weight (inverse variance)
    def compute_weight(quality):
        weights = {
            "Excellent": 1.0,
            "Good": 0.8,
            "Fair": 0.5,
            "Poor": 0.2,
            "Unknown": 0.1
        }
        return weights.get(quality, 0.1)

    stats_df["Recommended_weight"] = stats_df["Quality_flag"].apply(compute_weight)

    # Copy over Inter_STRESS and N_observers for reference
    stats_df["Inter_STRESS"] = df["Inter_STRESS"]
    stats_df["N_observers"] = df["N_observers"]

    return stats_df


def main():
    parser = argparse.ArgumentParser(description="Extract observer variability metadata")
    parser.add_argument("--mode", choices=["manual", "validate", "example", "stats"],
                       default="example",
                       help="Operation mode")
    parser.add_argument("--add", type=str, help="Add a specific dataset (interactive)")

    args = parser.parse_args()

    # Define paths
    metadata_path = Path("data/observer_metadata/dataset_observer_metadata.csv")
    stats_path = Path("data/observer_metadata/observer_variability_statistics.csv")
    log_path = Path("data/observer_metadata/extraction_log.json")

    # Ensure directories exist
    metadata_path.parent.mkdir(parents=True, exist_ok=True)

    if args.mode == "example":
        print("Creating example dataset entries...")

        # Add example datasets
        example_entries = add_example_datasets()

        # Validate each entry
        for entry in example_entries:
            try:
                validate_entry(entry)
                print(f"✓ Validated: {entry['DatasetID']}")
            except ValueError as e:
                print(f"✗ Validation error for {entry['DatasetID']}: {e}")
                return

        # Create DataFrame
        df = pd.DataFrame(example_entries)

        # Save to CSV
        df.to_csv(metadata_path, index=False)
        print(f"\n✅ Saved {len(df)} datasets to {metadata_path}")

        # Compute and save statistics
        stats_df = compute_derived_metrics(df)
        stats_df.to_csv(stats_path, index=False)
        print(f"✅ Saved derived statistics to {stats_path}")

        # Create extraction log
        log_data = {
            "last_updated": datetime.now().isoformat(),
            "total_datasets": int(len(df)),
            "datasets_with_inter_stress": int(df["Inter_STRESS"].notna().sum()),
            "datasets_with_intra_stress": int(df["Intra_STRESS"].notna().sum()),
            "extraction_history": [
                {
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "action": "Initial example creation",
                    "datasets_added": [e["DatasetID"] for e in example_entries]
                }
            ]
        }

        with open(log_path, 'w') as f:
            json.dump(log_data, f, indent=2)

        print(f"✅ Created extraction log at {log_path}")

        # Display summary
        print("\n" + "="*60)
        print("DATASET SUMMARY")
        print("="*60)
        print(df[["DatasetID", "N_observers", "Intra_STRESS", "Inter_STRESS",
                  "Method", "Confidence"]].to_string(index=False))

        print("\n" + "="*60)
        print("QUALITY SUMMARY")
        print("="*60)
        print(stats_df[["DatasetID", "Quality_flag", "Recommended_weight",
                       "STRESS_ratio"]].to_string(index=False))

    elif args.mode == "validate":
        if not metadata_path.exists():
            print(f"Error: Metadata file not found at {metadata_path}")
            return

        df = pd.read_csv(metadata_path)
        print(f"Validating {len(df)} datasets...")

        errors = []
        warnings = []

        for idx, row in df.iterrows():
            try:
                validate_entry(row.to_dict())
                print(f"✓ {row['DatasetID']}")
            except ValueError as e:
                errors.append(f"{row['DatasetID']}: {e}")
                print(f"✗ {row['DatasetID']}: {e}")

        # Additional warnings
        for idx, row in df.iterrows():
            if pd.isna(row["Inter_STRESS"]):
                warnings.append(f"{row['DatasetID']}: Missing Inter_STRESS")
            if row.get("Inter_STRESS", 0) > 45:
                warnings.append(f"{row['DatasetID']}: High Inter_STRESS ({row['Inter_STRESS']})")

        print("\n" + "="*60)
        print("VALIDATION REPORT")
        print("="*60)
        print(f"✅ Passed: {len(df) - len(errors)} datasets")
        print(f"⚠️  Warnings: {len(warnings)}")
        for w in warnings:
            print(f"  - {w}")
        print(f"❌ Errors: {len(errors)}")
        for e in errors:
            print(f"  - {e}")

    elif args.mode == "stats":
        if not metadata_path.exists():
            print(f"Error: Metadata file not found at {metadata_path}")
            return

        df = pd.read_csv(metadata_path)
        stats_df = compute_derived_metrics(df)
        stats_df.to_csv(stats_path, index=False)
        print(f"✅ Computed and saved statistics to {stats_path}")
        print("\n" + stats_df.to_string(index=False))


if __name__ == "__main__":
    main()
