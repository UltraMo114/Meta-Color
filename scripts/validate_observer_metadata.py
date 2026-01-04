"""
Observer Metadata Validation Script

Performs comprehensive quality assurance checks on the observer variability
metadata database.

Usage:
    python scripts/validate_observer_metadata.py
    python scripts/validate_observer_metadata.py --detailed
"""

import pandas as pd
import numpy as np
from pathlib import Path
import argparse
from datetime import datetime


class ObserverMetadataValidator:
    def __init__(self, metadata_path):
        """Initialize validator with metadata file."""
        self.metadata_path = Path(metadata_path)
        self.df = None
        self.errors = []
        self.warnings = []
        self.passed = []

    def load_data(self):
        """Load metadata CSV."""
        if not self.metadata_path.exists():
            raise FileNotFoundError(f"Metadata file not found: {self.metadata_path}")

        self.df = pd.read_csv(self.metadata_path)
        print(f"Loaded {len(self.df)} datasets from {self.metadata_path}")

    def check_completeness(self):
        """Check that required fields are filled."""
        print("\n" + "="*60)
        print("1. COMPLETENESS CHECK")
        print("="*60)

        required_fields = ["DatasetID", "N_observers", "Method", "Publication_year"]

        for field in required_fields:
            missing = self.df[field].isna().sum()
            if missing > 0:
                self.errors.append(f"Field '{field}' has {missing} missing values")
                print(f"❌ {field}: {missing} missing values")
            else:
                self.passed.append(f"Field '{field}' is complete")
                print(f"✓ {field}: Complete")

        # Check optional but important fields
        optional_important = ["Inter_STRESS", "Intra_STRESS", "DOI"]
        for field in optional_important:
            missing = self.df[field].isna().sum()
            if missing > 0:
                self.warnings.append(f"Field '{field}' has {missing} missing values")
                print(f"⚠️  {field}: {missing} missing (optional)")
            else:
                print(f"✓ {field}: Complete")

    def check_consistency(self):
        """Check logical consistency of values."""
        print("\n" + "="*60)
        print("2. CONSISTENCY CHECK")
        print("="*60)

        # Inter-STRESS >= Intra-STRESS
        inconsistent = self.df[
            (self.df["Inter_STRESS"].notna()) &
            (self.df["Intra_STRESS"].notna()) &
            (self.df["Inter_STRESS"] < self.df["Intra_STRESS"])
        ]

        if len(inconsistent) > 0:
            for idx, row in inconsistent.iterrows():
                self.errors.append(
                    f"{row['DatasetID']}: Inter_STRESS ({row['Inter_STRESS']}) < "
                    f"Intra_STRESS ({row['Intra_STRESS']})"
                )
                print(f"❌ {row['DatasetID']}: Inter < Intra (invalid)")
        else:
            self.passed.append("All datasets have Inter_STRESS >= Intra_STRESS")
            print("✓ Inter-STRESS >= Intra-STRESS for all datasets")

        # N_observers should be reasonable
        low_n = self.df[self.df["N_observers"] < 5]
        if len(low_n) > 0:
            for idx, row in low_n.iterrows():
                self.warnings.append(
                    f"{row['DatasetID']}: Low observer count (N={row['N_observers']})"
                )
                print(f"⚠️  {row['DatasetID']}: Low N_observers ({row['N_observers']})")
        else:
            print("✓ All datasets have N_observers >= 5")

    def check_ranges(self):
        """Check that values are in reasonable ranges."""
        print("\n" + "="*60)
        print("3. RANGE CHECK")
        print("="*60)

        # STRESS values should be 0-100
        for stress_col in ["Intra_STRESS", "Inter_STRESS"]:
            out_of_range = self.df[
                (self.df[stress_col].notna()) &
                ((self.df[stress_col] < 0) | (self.df[stress_col] > 100))
            ]

            if len(out_of_range) > 0:
                for idx, row in out_of_range.iterrows():
                    self.errors.append(
                        f"{row['DatasetID']}: {stress_col} = {row[stress_col]} "
                        f"(out of range [0, 100])"
                    )
                    print(f"❌ {row['DatasetID']}: {stress_col} out of range")
            else:
                print(f"✓ All {stress_col} values in valid range [0, 100]")

        # Flag high variability datasets
        high_stress = self.df[
            (self.df["Inter_STRESS"].notna()) &
            (self.df["Inter_STRESS"] > 50)
        ]

        if len(high_stress) > 0:
            for idx, row in high_stress.iterrows():
                self.warnings.append(
                    f"{row['DatasetID']}: Very high Inter_STRESS ({row['Inter_STRESS']})"
                )
                print(f"⚠️  {row['DatasetID']}: Very high Inter_STRESS ({row['Inter_STRESS']})")

    def check_method_validity(self):
        """Check that experimental methods are valid."""
        print("\n" + "="*60)
        print("4. METHOD VALIDITY CHECK")
        print("="*60)

        valid_methods = ["THR", "PC", "ME", "GS"]
        invalid = self.df[~self.df["Method"].isin(valid_methods)]

        if len(invalid) > 0:
            for idx, row in invalid.iterrows():
                self.errors.append(
                    f"{row['DatasetID']}: Invalid method '{row['Method']}'"
                )
                print(f"❌ {row['DatasetID']}: Invalid method '{row['Method']}'")
        else:
            self.passed.append("All methods are valid")
            print("✓ All methods are valid")

        # Show distribution
        print("\nMethod distribution:")
        for method in valid_methods:
            count = (self.df["Method"] == method).sum()
            print(f"  {method}: {count} datasets")

    def check_cross_dataset_consistency(self):
        """Check that similar datasets have similar values."""
        print("\n" + "="*60)
        print("5. CROSS-DATASET CONSISTENCY")
        print("="*60)

        # Group by method and check variability
        for method in ["THR", "PC", "ME", "GS"]:
            subset = self.df[
                (self.df["Method"] == method) &
                (self.df["Inter_STRESS"].notna())
            ]

            if len(subset) > 0:
                mean_stress = subset["Inter_STRESS"].mean()
                std_stress = subset["Inter_STRESS"].std()
                print(f"\n{method} datasets (N={len(subset)}):")
                print(f"  Mean Inter_STRESS: {mean_stress:.1f} ± {std_stress:.1f}")

                # Flag outliers (>2 SD from mean)
                if len(subset) >= 3:  # Need at least 3 for meaningful statistics
                    outliers = subset[
                        np.abs(subset["Inter_STRESS"] - mean_stress) > 2 * std_stress
                    ]
                    if len(outliers) > 0:
                        for idx, row in outliers.iterrows():
                            self.warnings.append(
                                f"{row['DatasetID']}: Inter_STRESS ({row['Inter_STRESS']}) "
                                f"is an outlier for method {method}"
                            )
                            print(f"  ⚠️  {row['DatasetID']}: Outlier (STRESS={row['Inter_STRESS']})")

    def check_documentation(self):
        """Check that datasets are properly documented."""
        print("\n" + "="*60)
        print("6. DOCUMENTATION CHECK")
        print("="*60)

        # Check for DOI or source
        no_source = self.df[
            (self.df["DOI"].isna() | (self.df["DOI"] == "N/A")) &
            (self.df["Source"].isna() | (self.df["Source"] == ""))
        ]

        if len(no_source) > 0:
            for idx, row in no_source.iterrows():
                self.warnings.append(
                    f"{row['DatasetID']}: No DOI or source information"
                )
                print(f"⚠️  {row['DatasetID']}: Missing DOI and source")
        else:
            print("✓ All datasets have source documentation")

        # Check confidence ratings
        if "Confidence" in self.df.columns:
            low_confidence = self.df[self.df["Confidence"] == "Low"]
            if len(low_confidence) > 0:
                print(f"\n⚠️  {len(low_confidence)} datasets marked as Low confidence:")
                for idx, row in low_confidence.iterrows():
                    print(f"  - {row['DatasetID']}")

    def generate_report(self, detailed=False):
        """Generate validation report."""
        print("\n" + "="*60)
        print("VALIDATION SUMMARY")
        print("="*60)

        print(f"\n✅ Passed: {len(self.passed)} checks")
        print(f"⚠️  Warnings: {len(self.warnings)}")
        print(f"❌ Errors: {len(self.errors)}")

        if len(self.warnings) > 0:
            print("\nWarnings:")
            for w in self.warnings[:10]:  # Show first 10
                print(f"  - {w}")
            if len(self.warnings) > 10:
                print(f"  ... and {len(self.warnings) - 10} more")

        if len(self.errors) > 0:
            print("\nErrors:")
            for e in self.errors:
                print(f"  - {e}")

        # Overall statistics
        print("\n" + "="*60)
        print("DATASET STATISTICS")
        print("="*60)

        total = len(self.df)
        with_inter = self.df["Inter_STRESS"].notna().sum()
        with_intra = self.df["Intra_STRESS"].notna().sum()

        print(f"Total datasets: {total}")
        print(f"Datasets with Inter_STRESS: {with_inter} ({100*with_inter/total:.1f}%)")
        print(f"Datasets with Intra_STRESS: {with_intra} ({100*with_intra/total:.1f}%)")

        if with_inter > 0:
            print(f"\nInter-observer STRESS statistics:")
            print(f"  Min: {self.df['Inter_STRESS'].min():.1f}")
            print(f"  Median: {self.df['Inter_STRESS'].median():.1f}")
            print(f"  Mean: {self.df['Inter_STRESS'].mean():.1f}")
            print(f"  Max: {self.df['Inter_STRESS'].max():.1f}")

        # Quality distribution
        if detailed:
            self._print_detailed_report()

        return len(self.errors) == 0

    def _print_detailed_report(self):
        """Print detailed dataset-by-dataset report."""
        print("\n" + "="*60)
        print("DETAILED DATASET REPORT")
        print("="*60)

        for idx, row in self.df.iterrows():
            print(f"\n{row['DatasetID']}:")
            print(f"  N_observers: {row['N_observers']}")
            print(f"  Intra_STRESS: {row.get('Intra_STRESS', 'N/A')}")
            print(f"  Inter_STRESS: {row.get('Inter_STRESS', 'N/A')}")
            print(f"  Method: {row['Method']}")
            print(f"  Source: {row.get('Source', 'N/A')}")


def main():
    parser = argparse.ArgumentParser(description="Validate observer metadata")
    parser.add_argument("--detailed", action="store_true",
                       help="Show detailed dataset-by-dataset report")
    parser.add_argument("--file", type=str,
                       default="data/observer_metadata/dataset_observer_metadata.csv",
                       help="Path to metadata CSV file")

    args = parser.parse_args()

    # Create validator
    validator = ObserverMetadataValidator(args.file)

    try:
        validator.load_data()

        # Run all checks
        validator.check_completeness()
        validator.check_consistency()
        validator.check_ranges()
        validator.check_method_validity()
        validator.check_cross_dataset_consistency()
        validator.check_documentation()

        # Generate report
        success = validator.generate_report(detailed=args.detailed)

        # Save validation report
        report_path = Path("results/observer_analysis/validation_report.txt")
        report_path.parent.mkdir(parents=True, exist_ok=True)

        with open(report_path, 'w') as f:
            f.write(f"Validation Report\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"="*60 + "\n\n")
            f.write(f"Total datasets: {len(validator.df)}\n")
            f.write(f"Passed checks: {len(validator.passed)}\n")
            f.write(f"Warnings: {len(validator.warnings)}\n")
            f.write(f"Errors: {len(validator.errors)}\n\n")

            if validator.warnings:
                f.write("Warnings:\n")
                for w in validator.warnings:
                    f.write(f"  - {w}\n")

            if validator.errors:
                f.write("\nErrors:\n")
                for e in validator.errors:
                    f.write(f"  - {e}\n")

        print(f"\n✅ Validation report saved to {report_path}")

        return 0 if success else 1

    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
