"""
Observer Variability Visualization Script

Generates diagnostic figures for observer variability analysis.

Figures:
1. Observer variability by dataset (bar chart)
2. Variability by experimental method (box plot)
3. STRESS ratio analysis (scatter plot)

Usage:
    python scripts/visualize_observer_variability.py
    python scripts/visualize_observer_variability.py --output-dir results/observer_analysis
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import argparse


def plot_observer_variability(df, output_path):
    """
    Bar chart showing Intra/Inter STRESS for each dataset.

    X-axis: Dataset (sorted by Inter_STRESS)
    Y-axis: STRESS (0-60)
    Bars: Blue (Intra), Red (Inter)
    """
    # Filter datasets with STRESS data
    df_plot = df[df["Inter_STRESS"].notna()].copy()

    if len(df_plot) == 0:
        print("⚠️  No datasets with Inter_STRESS data to plot")
        return

    # Sort by Inter_STRESS
    df_plot = df_plot.sort_values('Inter_STRESS')

    fig, ax = plt.subplots(figsize=(14, 6))

    x = np.arange(len(df_plot))
    width = 0.35

    # Plot bars
    intra_vals = df_plot['Intra_STRESS'].fillna(0)
    inter_vals = df_plot['Inter_STRESS']

    bars1 = ax.bar(x - width/2, intra_vals, width,
                   label='Intra-observer', color='steelblue', alpha=0.8)
    bars2 = ax.bar(x + width/2, inter_vals, width,
                   label='Inter-observer', color='coral', alpha=0.8)

    # Reference lines
    ax.axhline(y=30, color='green', linestyle='--', linewidth=1.5,
               label='Good threshold (30)', alpha=0.7)
    ax.axhline(y=50, color='red', linestyle='--', linewidth=1.5,
               label='High variability (50)', alpha=0.7)

    # Formatting
    ax.set_xlabel('Dataset', fontsize=12, fontweight='bold')
    ax.set_ylabel('STRESS (units)', fontsize=12, fontweight='bold')
    ax.set_title('Observer Variability by Dataset', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(df_plot['DatasetID'], rotation=45, ha='right', fontsize=10)
    ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
    ax.grid(axis='y', alpha=0.3, linestyle=':')
    ax.set_ylim(0, max(65, df_plot['Inter_STRESS'].max() * 1.1))

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"✅ Saved: {output_path}")


def plot_method_comparison(df, output_path):
    """
    Box plot showing STRESS distribution by psychophysical method.

    X-axis: Method (THR, PC, ME, GS)
    Y-axis: Inter-observer STRESS
    """
    # Filter datasets with method and STRESS data
    df_plot = df[(df["Method"].notna()) & (df["Inter_STRESS"].notna())].copy()

    if len(df_plot) == 0:
        print("⚠️  No datasets with Method and Inter_STRESS data to plot")
        return

    fig, ax = plt.subplots(figsize=(10, 6))

    methods = ['THR', 'PC', 'ME', 'GS']
    method_labels = {
        'THR': 'Threshold',
        'PC': 'Pair Comparison',
        'ME': 'Magnitude Estimation',
        'GS': 'Gray Scale'
    }

    # Prepare data for each method
    data = []
    labels = []
    for method in methods:
        method_data = df_plot[df_plot['Method'] == method]['Inter_STRESS'].values
        if len(method_data) > 0:
            data.append(method_data)
            labels.append(f"{method}\n(N={len(method_data)})")
        else:
            data.append([])
            labels.append(f"{method}\n(N=0)")

    # Create box plot
    bp = ax.boxplot(data, labels=labels, patch_artist=True,
                    notch=True, showmeans=True,
                    meanprops=dict(marker='D', markerfacecolor='red',
                                  markersize=6, markeredgecolor='darkred'))

    # Color the boxes
    colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightcoral']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    # Formatting
    ax.set_xlabel('Psychophysical Method', fontsize=12, fontweight='bold')
    ax.set_ylabel('Inter-observer STRESS', fontsize=12, fontweight='bold')
    ax.set_title('Observer Variability by Experimental Method', fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3, linestyle=':')

    # Add reference line
    ax.axhline(y=30, color='green', linestyle='--', linewidth=1.5,
               label='Good threshold', alpha=0.7)

    ax.legend(loc='upper right')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"✅ Saved: {output_path}")


def plot_stress_ratio(df, output_path):
    """
    Scatter plot: Intra vs. Inter STRESS

    Diagonal line = perfect self-consistency
    Points below line = well-trained observers
    Points above line = problematic (intra > inter, impossible)
    """
    # Filter datasets with both Intra and Inter STRESS
    df_plot = df[(df["Intra_STRESS"].notna()) & (df["Inter_STRESS"].notna())].copy()

    if len(df_plot) == 0:
        print("⚠️  No datasets with both Intra and Inter STRESS data to plot")
        return

    fig, ax = plt.subplots(figsize=(9, 9))

    # Scatter plot
    scatter = ax.scatter(df_plot['Intra_STRESS'], df_plot['Inter_STRESS'],
                        s=df_plot['N_observers'] * 10,  # Size proportional to N_observers
                        c=df_plot['N_observers'],
                        cmap='viridis',
                        alpha=0.6,
                        edgecolors='black',
                        linewidth=1)

    # Diagonal line (perfect consistency)
    max_val = max(df_plot['Intra_STRESS'].max(), df_plot['Inter_STRESS'].max())
    min_val = min(df_plot['Intra_STRESS'].min(), df_plot['Inter_STRESS'].min())
    ax.plot([0, max_val * 1.1], [0, max_val * 1.1], 'k--',
            label='Perfect consistency\n(Intra = Inter)', linewidth=2, alpha=0.7)

    # Add typical range
    ax.axhline(y=30, color='green', linestyle=':', alpha=0.5, label='Good Inter-STRESS')
    ax.axvline(x=30, color='green', linestyle=':', alpha=0.5)

    # Label datasets (especially outliers)
    for _, row in df_plot.iterrows():
        if (row['Inter_STRESS'] > 45 or row['Intra_STRESS'] > 40 or
            row['N_observers'] >= 15):
            ax.annotate(row['DatasetID'],
                       (row['Intra_STRESS'], row['Inter_STRESS']),
                       xytext=(5, 5), textcoords='offset points',
                       fontsize=9, alpha=0.8,
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow',
                                alpha=0.3, edgecolor='none'))

    # Formatting
    ax.set_xlabel('Intra-observer STRESS (self-consistency)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Inter-observer STRESS (agreement)', fontsize=12, fontweight='bold')
    ax.set_title('Observer Consistency Analysis\n(Size = Number of Observers)',
                fontsize=14, fontweight='bold')
    ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
    ax.grid(True, alpha=0.3, linestyle=':')

    # Set equal aspect ratio
    ax.set_xlim(0, max_val * 1.1)
    ax.set_ylim(0, max_val * 1.1)
    ax.set_aspect('equal')

    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Number of Observers', fontsize=11, fontweight='bold')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"✅ Saved: {output_path}")


def plot_quality_summary(df, output_path):
    """
    Additional plot: Quality flag distribution
    """
    # Compute quality flags
    def assign_quality_flag(row):
        inter_stress = row.get("Inter_STRESS")
        n_obs = row.get("N_observers", 0)

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

    df['Quality_flag'] = df.apply(assign_quality_flag, axis=1)

    # Count quality flags
    quality_counts = df['Quality_flag'].value_counts()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Pie chart
    colors = {
        'Excellent': '#2ecc71',
        'Good': '#3498db',
        'Fair': '#f39c12',
        'Poor': '#e74c3c',
        'Unknown': '#95a5a6'
    }
    plot_colors = [colors.get(label, '#95a5a6') for label in quality_counts.index]

    ax1.pie(quality_counts.values, labels=quality_counts.index,
           autopct='%1.1f%%', colors=plot_colors, startangle=90,
           textprops={'fontsize': 12, 'fontweight': 'bold'})
    ax1.set_title('Dataset Quality Distribution', fontsize=14, fontweight='bold')

    # Bar chart by method and quality
    if 'Method' in df.columns:
        quality_by_method = pd.crosstab(df['Method'], df['Quality_flag'])
        quality_by_method.plot(kind='bar', stacked=True, ax=ax2,
                              color=[colors.get(q, '#95a5a6')
                                    for q in quality_by_method.columns],
                              alpha=0.8)
        ax2.set_xlabel('Method', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Number of Datasets', fontsize=12, fontweight='bold')
        ax2.set_title('Quality Distribution by Method', fontsize=14, fontweight='bold')
        ax2.legend(title='Quality', bbox_to_anchor=(1.05, 1), loc='upper left')
        ax2.set_xticklabels(ax2.get_xticklabels(), rotation=0)
        ax2.grid(axis='y', alpha=0.3, linestyle=':')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"✅ Saved: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Visualize observer variability")
    parser.add_argument("--input", type=str,
                       default="data/observer_metadata/dataset_observer_metadata.csv",
                       help="Path to metadata CSV file")
    parser.add_argument("--output-dir", type=str,
                       default="results/observer_analysis",
                       help="Output directory for figures")

    args = parser.parse_args()

    # Load data
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ Error: Metadata file not found at {input_path}")
        print("   Run extract_observer_variability.py first to create the metadata file")
        return 1

    df = pd.read_csv(input_path)
    print(f"Loaded {len(df)} datasets from {input_path}")

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate figures
    print("\nGenerating visualizations...")

    plot_observer_variability(
        df,
        output_dir / "fig_observer_variability.png"
    )

    plot_method_comparison(
        df,
        output_dir / "fig_method_comparison.png"
    )

    plot_stress_ratio(
        df,
        output_dir / "fig_stress_ratio.png"
    )

    plot_quality_summary(
        df,
        output_dir / "fig_quality_summary.png"
    )

    print("\n✅ All visualizations generated successfully!")
    print(f"   Output directory: {output_dir}")

    return 0


if __name__ == "__main__":
    exit(main())
