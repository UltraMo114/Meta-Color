"""
Demo: Ratio Analysis and Forest Plots

This script demonstrates Module 1 functionality:
1. Load datasets
2. Calculate model predictions
3. Compute dE/dV ratios
4. Generate forest plots
"""

import numpy as np
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.loader import DataLoader
from src.models import CIELAB, CIEDE2000, CAM16UCS
from src.metrics import calculate_de_dv_ratio, calculate_stress, evaluate_model_performance
from src.viz_style import plot_forest, plot_scatter_with_diagonal, plot_ratio_distribution


def analyze_single_dataset(dataset, model):
    """Analyze a single dataset with a color difference model"""

    print(f"\nAnalyzing dataset: {dataset.name}")
    print(f"  Number of pairs: {dataset.n_pairs}")

    # Calculate predictions for all color pairs
    predicted = []
    observed = []

    for pair in dataset.color_pairs:
        # Calculate color difference between XYZ1 and XYZ2
        dE = model.predict(
            pair.xyz_1,
            pair.xyz_2,
            input_type='XYZ',
            whitepoint=pair.xyz_w
        )
        predicted.append(dE)
        observed.append(pair.visual_difference)

    predicted = np.array(predicted)
    observed = np.array(observed)

    # Calculate metrics
    metrics = evaluate_model_performance(predicted, observed)

    print(f"  Results for {model.name}:")
    print(f"    STRESS: {metrics['stress']:.2f}")
    print(f"    Mean dE/dV Ratio: {metrics['mean_ratio']:.3f} ± {metrics['std_ratio']:.3f}")
    print(f"    Pearson r: {metrics['pearson_r']:.3f}")

    return predicted, observed, metrics


def generate_forest_plot_data(loader, model_name='CIEDE2000'):
    """Generate data for forest plot across all datasets"""

    print(f"\n{'='*80}")
    print(f"Generating Forest Plot Data for {model_name}")
    print(f"{'='*80}")

    model = CIEDE2000() if model_name == 'CIEDE2000' else CIELAB()

    datasets = loader.get_all_datasets()

    forest_data = {}

    for dataset in datasets[:5]:  # Limit to first 5 datasets for demo
        predicted, observed, metrics = analyze_single_dataset(dataset, model)

        # Calculate ratio and confidence interval
        mean_ratio = metrics['mean_ratio']
        std_ratio = metrics['std_ratio']

        # Simple 95% CI: mean ± 1.96 * std
        ci_low = mean_ratio - 1.96 * std_ratio
        ci_high = mean_ratio + 1.96 * std_ratio

        forest_data[dataset.name] = (mean_ratio, ci_low, ci_high)

    return forest_data


def main():
    """Main demonstration function"""

    print("\n" + "="*80)
    print("Meta-Color Framework - Module 1 Demonstration")
    print("Ratio Analysis and Forest Plots")
    print("="*80)

    # Load data
    print("\nLoading datasets...")
    loader = DataLoader()
    datasets = loader.load()

    print(f"\nLoaded {len(datasets)} datasets")

    # Analyze first dataset in detail
    print("\n" + "="*80)
    print("Detailed Analysis of First Dataset")
    print("="*80)

    first_dataset = datasets[0]

    # Test multiple models
    models = [
        CIELAB(),
        CIEDE2000(),
    ]

    results = {}

    for model in models:
        predicted, observed, metrics = analyze_single_dataset(first_dataset, model)
        results[model.name] = {
            'predicted': predicted,
            'observed': observed,
            'metrics': metrics
        }

        # Create scatter plot
        try:
            from src.viz_style import plot_scatter_with_diagonal
            fig, ax = plot_scatter_with_diagonal(
                predicted, observed,
                xlabel="Visual Difference (ΔV)",
                ylabel=f"{model.name} Prediction (ΔE)",
                title=f"{model.name} vs Visual - {first_dataset.name}",
                save_path=f"results/figures/scatter_{first_dataset.name}_{model.name}"
            )
            print(f"  Saved scatter plot for {model.name}")
        except Exception as e:
            print(f"  Could not create scatter plot: {e}")

    # Generate forest plot data
    forest_data = generate_forest_plot_data(loader, model_name='CIEDE2000')

    print("\n" + "="*80)
    print("Forest Plot Data (dE/dV Ratios with 95% CI)")
    print("="*80)

    for dataset_name, (mean, low, high) in forest_data.items():
        print(f"{dataset_name:20s}: {mean:.3f} [{low:.3f}, {high:.3f}]")

    # Create forest plot
    try:
        from src.viz_style import plot_forest
        fig, ax = plot_forest(
            forest_data,
            xlabel="dE/dV Ratio",
            title="CIEDE2000 Performance Across Datasets",
            save_path="results/figures/forest_plot_ciede2000"
        )
        print("\nSaved forest plot")
    except Exception as e:
        print(f"\nCould not create forest plot: {e}")

    print("\n" + "="*80)
    print("Analysis Complete!")
    print("="*80)


if __name__ == '__main__':
    main()
