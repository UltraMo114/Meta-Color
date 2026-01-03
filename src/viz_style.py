"""
Publication-quality plotting standards for Meta-Color Framework

This module provides standardized matplotlib styling for all visualizations,
ensuring consistency and publication quality across all plots.
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import numpy as np
from typing import Optional, Tuple


# Publication style constants
PUBLICATION_STYLE = {
    # Font settings
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,

    # Figure settings
    'figure.figsize': (6, 4),
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,

    # Line settings
    'lines.linewidth': 1.5,
    'lines.markersize': 6,

    # Axes settings
    'axes.linewidth': 1.0,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,

    # Tick settings
    'xtick.major.width': 1.0,
    'ytick.major.width': 1.0,
    'xtick.direction': 'out',
    'ytick.direction': 'out',

    # Legend settings
    'legend.frameon': False,
    'legend.loc': 'best',

    # Color cycle (colorblind-friendly palette)
    'axes.prop_cycle': mpl.cycler(color=[
        '#0173B2',  # Blue
        '#DE8F05',  # Orange
        '#029E73',  # Green
        '#CC78BC',  # Purple
        '#CA9161',  # Brown
        '#949494',  # Gray
        '#EFE441',  # Yellow
        '#56B4E9',  # Light blue
    ])
}


def set_publication_style():
    """Apply publication-quality style to matplotlib"""
    plt.style.use('seaborn-v0_8-whitegrid')
    mpl.rcParams.update(PUBLICATION_STYLE)


def create_figure(figsize: Optional[Tuple[float, float]] = None,
                  nrows: int = 1,
                  ncols: int = 1,
                  **kwargs) -> Tuple:
    """
    Create a publication-quality figure

    Parameters
    ----------
    figsize : Optional[Tuple[float, float]]
        Figure size in inches (width, height). If None, uses default.
    nrows : int
        Number of subplot rows (default: 1)
    ncols : int
        Number of subplot columns (default: 1)
    **kwargs
        Additional arguments passed to plt.subplots()

    Returns
    -------
    Tuple
        (fig, ax) or (fig, axes) if nrows*ncols > 1

    Examples
    --------
    >>> fig, ax = create_figure()
    >>> ax.plot(x, y)
    >>> save_figure(fig, 'output.png')
    """
    if figsize is None:
        figsize = PUBLICATION_STYLE['figure.figsize']

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize, **kwargs)

    return fig, axes


def save_figure(fig,
                filename: str,
                dpi: Optional[int] = None,
                formats: Optional[list] = None):
    """
    Save figure in publication quality

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to save
    filename : str
        Output filename (without extension)
    dpi : Optional[int]
        Resolution in dots per inch (default: 300)
    formats : Optional[list]
        List of formats to save ['png', 'pdf', 'svg'] (default: ['png'])

    Examples
    --------
    >>> fig, ax = create_figure()
    >>> ax.plot(x, y)
    >>> save_figure(fig, 'results/figure1', formats=['png', 'pdf'])
    """
    if dpi is None:
        dpi = PUBLICATION_STYLE['savefig.dpi']

    if formats is None:
        formats = ['png']

    for fmt in formats:
        output_file = f"{filename}.{fmt}"
        fig.savefig(output_file, dpi=dpi, bbox_inches='tight', format=fmt)
        print(f"Saved: {output_file}")


def plot_forest(data: dict,
                xlabel: str = "Effect Size",
                title: str = "Forest Plot",
                save_path: Optional[str] = None) -> Tuple:
    """
    Create a forest plot for meta-analysis

    Parameters
    ----------
    data : dict
        Dictionary with keys as dataset names and values as tuples (mean, ci_low, ci_high)
    xlabel : str
        X-axis label
    title : str
        Plot title
    save_path : Optional[str]
        If provided, save figure to this path

    Returns
    -------
    Tuple
        (fig, ax)

    Examples
    --------
    >>> data = {
    ...     'Study 1': (1.2, 0.8, 1.6),
    ...     'Study 2': (1.5, 1.1, 1.9),
    ... }
    >>> fig, ax = plot_forest(data, xlabel='dE/dV Ratio')
    """
    set_publication_style()

    # Extract data
    studies = list(data.keys())
    means = [data[s][0] for s in studies]
    ci_lows = [data[s][1] for s in studies]
    ci_highs = [data[s][2] for s in studies]

    # Calculate error bars
    errors_low = [m - l for m, l in zip(means, ci_lows)]
    errors_high = [h - m for m, h in zip(ci_highs, means)]

    # Create figure
    fig, ax = create_figure(figsize=(8, len(studies) * 0.4 + 1))

    # Plot error bars
    y_positions = np.arange(len(studies))
    ax.errorbar(means, y_positions,
                xerr=[errors_low, errors_high],
                fmt='o',
                markersize=8,
                capsize=5,
                capthick=2,
                color='#0173B2',
                ecolor='#0173B2',
                alpha=0.7)

    # Add vertical line at x=1 (or 0 for some metrics)
    ax.axvline(x=1.0, color='gray', linestyle='--', linewidth=1, alpha=0.5)

    # Formatting
    ax.set_yticks(y_positions)
    ax.set_yticklabels(studies)
    ax.set_xlabel(xlabel)
    ax.set_title(title, fontweight='bold')
    ax.invert_yaxis()  # Put first study at top

    # Add grid
    ax.grid(axis='x', alpha=0.3, linestyle=':')

    plt.tight_layout()

    if save_path:
        save_figure(fig, save_path)

    return fig, ax


def plot_scatter_with_diagonal(predicted: np.ndarray,
                                observed: np.ndarray,
                                xlabel: str = "Visual Difference (ΔV)",
                                ylabel: str = "Predicted Difference (ΔE)",
                                title: str = "Predicted vs. Observed",
                                save_path: Optional[str] = None,
                                show_stats: bool = True) -> Tuple:
    """
    Create scatter plot with 1:1 diagonal line

    Parameters
    ----------
    predicted : np.ndarray
        Predicted values (ΔE)
    observed : np.ndarray
        Observed values (ΔV)
    xlabel : str
        X-axis label
    ylabel : str
        Y-axis label
    title : str
        Plot title
    save_path : Optional[str]
        If provided, save figure to this path
    show_stats : bool
        If True, display statistics on plot

    Returns
    -------
    Tuple
        (fig, ax)
    """
    set_publication_style()

    fig, ax = create_figure(figsize=(6, 6))

    # Scatter plot
    ax.scatter(observed, predicted, alpha=0.5, s=30, color='#0173B2', edgecolors='none')

    # Diagonal line (1:1)
    lims = [
        np.min([ax.get_xlim(), ax.get_ylim()]),
        np.max([ax.get_xlim(), ax.get_ylim()]),
    ]
    ax.plot(lims, lims, 'k--', alpha=0.5, linewidth=1.5, label='Perfect fit')

    # Best fit line (optional)
    from scipy import stats
    slope, intercept, r_value, p_value, std_err = stats.linregress(observed, predicted)
    fit_line = slope * observed + intercept
    ax.plot(observed, fit_line, 'r-', alpha=0.7, linewidth=1.5, label=f'Linear fit (r={r_value:.3f})')

    # Statistics
    if show_stats:
        from src.metrics import calculate_stress, calculate_rmse
        stress = calculate_stress(predicted, observed)
        rmse = calculate_rmse(predicted, observed)

        stats_text = f"STRESS = {stress:.2f}\nRMSE = {rmse:.2f}\nR² = {r_value**2:.3f}"
        ax.text(0.05, 0.95, stats_text,
                transform=ax.transAxes,
                verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # Formatting
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title, fontweight='bold')
    ax.legend()
    ax.set_aspect('equal')

    plt.tight_layout()

    if save_path:
        save_figure(fig, save_path)

    return fig, ax


def plot_ratio_distribution(ratios: np.ndarray,
                            title: str = "dE/dV Ratio Distribution",
                            save_path: Optional[str] = None) -> Tuple:
    """
    Plot histogram of dE/dV ratios

    Parameters
    ----------
    ratios : np.ndarray
        Array of dE/dV ratios
    title : str
        Plot title
    save_path : Optional[str]
        If provided, save figure to this path

    Returns
    -------
    Tuple
        (fig, ax)
    """
    set_publication_style()

    fig, ax = create_figure(figsize=(7, 4))

    # Histogram
    ax.hist(ratios, bins=30, color='#0173B2', alpha=0.7, edgecolor='black')

    # Add vertical line at mean
    mean_ratio = np.mean(ratios)
    ax.axvline(mean_ratio, color='red', linestyle='--', linewidth=2,
               label=f'Mean = {mean_ratio:.2f}')

    # Add vertical line at 1.0 (perfect prediction)
    ax.axvline(1.0, color='gray', linestyle=':', linewidth=2,
               label='Perfect (1.0)')

    # Formatting
    ax.set_xlabel('dE/dV Ratio')
    ax.set_ylabel('Frequency')
    ax.set_title(title, fontweight='bold')
    ax.legend()

    plt.tight_layout()

    if save_path:
        save_figure(fig, save_path)

    return fig, ax


# Initialize publication style on import
set_publication_style()
