"""
Ronnier-style visualization helpers for the Classic Statistical Audit.

Figures:
  - fig1_bias.png: dV vs dE scatter with y=x reference.
  - fig2_outlier_ranking.png: per-dataset outlier rate bar chart.
  - fig3_outlier_counts.png: per-dataset outlier count bar chart.
  - fig5_ratio_ranking.png: per-dataset mean ratio ranking.
  - fig6_1sigma_rate_ranking.png: per-dataset +1σ exceedance rate.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


_STYLE = {
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
}


def plot_global_bias(df: pd.DataFrame, out_dir: str | Path = Path("results/classic_audit")) -> Path:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "fig1_bias.png"

    x = df["dV"].to_numpy(dtype=float)
    y = df["dE"].to_numpy(dtype=float)

    finite = np.isfinite(x) & np.isfinite(y)
    if not np.any(finite):
        raise ValueError("No finite dV/dE values to plot.")

    max_val = float(np.max(np.maximum(x[finite], y[finite])))
    max_val = max(max_val, 1e-12)

    with plt.rc_context(_STYLE):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.scatter(x, y, color="#1f77b4", alpha=0.3, s=10)
        ax.plot([0.0, max_val], [0.0, max_val], "k--", linewidth=1)
        ax.set_xlabel("Visual Difference (ΔV)")
        ax.set_ylabel("Computed Difference (ΔE)")
        ax.grid(True, alpha=0.3, linestyle="--")
        fig.tight_layout()
        fig.savefig(out_path, dpi=300)
        plt.close(fig)

    return out_path


def plot_outlier_rates(df: pd.DataFrame, out_dir: str | Path = Path("results/classic_audit")) -> Path:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "fig2_outlier_ranking.png"

    if "Is_Outlier" not in df.columns:
        raise ValueError("DataFrame must include 'Is_Outlier' column.")

    rates = (df.groupby("DatasetID")["Is_Outlier"].mean() * 100.0).sort_values(ascending=False)

    labels = rates.index.tolist()
    values = rates.to_numpy(dtype=float)
    colors = ["red" if v > 10.0 else "gray" for v in values]

    height = max(4.0, 0.25 * len(labels) + 1.0)
    with plt.rc_context(_STYLE):
        fig, ax = plt.subplots(figsize=(8, height))
        y_pos = np.arange(len(labels))
        ax.barh(y_pos, values, color=colors)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels)
        ax.set_xlim(0, 100)
        ax.invert_yaxis()
        ax.set_xlabel("Outlier Rate (%)")
        ax.grid(True, axis="x", alpha=0.3, linestyle="--")
        fig.tight_layout()
        fig.savefig(out_path, dpi=300)
        plt.close(fig)

    return out_path


def plot_outlier_ranking(df: pd.DataFrame, out_dir: str | Path = Path("results/classic_audit")) -> Path:
    """Alias for backward/forward compatibility with prompt naming."""
    return plot_outlier_rates(df, out_dir=out_dir)


def plot_outlier_counts(df: pd.DataFrame, out_dir: str | Path = Path("results/classic_audit")) -> Path:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "fig3_outlier_counts.png"

    if "Is_Outlier" not in df.columns:
        raise ValueError("DataFrame must include 'Is_Outlier' column.")

    grouped = df.groupby("DatasetID")["Is_Outlier"]
    counts = grouped.sum().astype(int)
    totals = grouped.size().astype(int)
    rates = (counts / totals) * 100.0

    counts = counts.sort_values(ascending=False)
    labels = counts.index.tolist()
    values = counts.to_numpy(dtype=float)

    colors = ["red" if float(rates.loc[label]) > 10.0 else "gray" for label in labels]

    height = max(4.0, 0.25 * len(labels) + 1.0)
    with plt.rc_context(_STYLE):
        fig, ax = plt.subplots(figsize=(8, height))
        y_pos = np.arange(len(labels))
        ax.barh(y_pos, values, color=colors)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels)
        ax.invert_yaxis()
        ax.set_xlabel("Outlier Count (N)")
        ax.grid(True, axis="x", alpha=0.3, linestyle="--")
        fig.tight_layout()
        fig.savefig(out_path, dpi=300)
        plt.close(fig)

    return out_path


def plot_ratio_vs_magnitude(df: pd.DataFrame, out_dir: str | Path = Path("results/classic_audit")) -> Path:
    """
    Ronnier-style plot: Ratio vs computed magnitude (dE).

    - X-axis: dE (computed CIEDE2000)
    - Y-axis: Ratio (scaled dE/dV)
    - Scatter: all points, light gray
    - Reference lines: mean (red), ±1 std (blue dashed), ±2 std (green dotted)
      computed on non-outlier finite ratios.
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "fig_ronnier_ratio_trend.png"

    x = df["dE"].to_numpy(dtype=float)
    y = df["Ratio"].to_numpy(dtype=float)

    finite = np.isfinite(x) & np.isfinite(y)
    if not np.any(finite):
        raise ValueError("No finite dE/Ratio values to plot.")

    if "Is_Outlier" in df.columns:
        good = finite & (~df["Is_Outlier"].to_numpy(dtype=bool))
    else:
        good = finite

    if np.any(good):
        mean_ratio = float(np.mean(y[good]))
        std_ratio = float(np.std(y[good], ddof=1)) if np.sum(good) > 1 else 0.0
    else:
        mean_ratio = float(np.mean(y[finite]))
        std_ratio = float(np.std(y[finite], ddof=1)) if np.sum(finite) > 1 else 0.0

    max_de = float(np.max(x[finite]))
    max_de = max(max_de, 1e-12)

    upper1 = mean_ratio + std_ratio
    lower1 = mean_ratio - std_ratio
    upper2 = mean_ratio + 2.0 * std_ratio
    lower2 = mean_ratio - 2.0 * std_ratio

    n_total = int(np.sum(finite))
    above_1s = int(np.sum(finite & (y > upper1)))
    below_1s = int(np.sum(finite & (y < lower1)))
    above_2s = int(np.sum(finite & (y > upper2)))
    below_2s = int(np.sum(finite & (y < lower2)))
    outlier_rate = float(np.mean(df["Is_Outlier"].to_numpy(dtype=bool)[finite]) * 100.0) if "Is_Outlier" in df.columns else float("nan")

    with plt.rc_context(_STYLE):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.hexbin(
            x[finite],
            y[finite],
            gridsize=120,
            extent=(0.0, max_de, 0.0, 3.0),
            cmap="Greys",
            mincnt=1,
            linewidths=0,
            norm=LogNorm(),
        )

        ax.axhline(mean_ratio, color="red", linestyle="-", linewidth=1)
        ax.axhline(upper1, color="blue", linestyle="--", linewidth=1)
        ax.axhline(lower1, color="blue", linestyle="--", linewidth=1)
        ax.axhline(upper2, color="green", linestyle=":", linewidth=1)
        ax.axhline(lower2, color="green", linestyle=":", linewidth=1)

        ax.set_xlim(0.0, max_de)
        ax.set_ylim(0.0, 3.0)
        ax.set_xlabel("Computed Difference (ΔE)")
        ax.set_ylabel("Ratio (ΔE / scaled ΔV)")
        ax.grid(True, alpha=0.3, linestyle="--")

        summary = (
            f"N={n_total}\n"
            f"Mean={mean_ratio:.3f}, σ={std_ratio:.3f}\n"
            f"> +1σ: {100.0 * above_1s / n_total:.1f}%   < -1σ: {100.0 * below_1s / n_total:.1f}%\n"
            f"> +2σ: {100.0 * above_2s / n_total:.1f}%   < -2σ: {100.0 * below_2s / n_total:.1f}%\n"
            f"Is_Outlier: {outlier_rate:.2f}%"
        )
        ax.text(
            0.99,
            0.99,
            summary,
            transform=ax.transAxes,
            ha="right",
            va="top",
            fontsize=8,
            bbox={"facecolor": "white", "alpha": 0.75, "edgecolor": "none"},
        )
        fig.tight_layout()
        fig.savefig(out_path, dpi=300)
        plt.close(fig)

    return out_path


def plot_1sigma_counts(df: pd.DataFrame, out_dir: str | Path = Path("results/classic_audit")) -> Path:
    """
    Count-based view of 1σ exceedance, analogous to fig3_outlier_counts.

    Definition:
      A sample is counted if Ratio > (Global Mean + 1σ), where global stats are
      computed the same way as in `plot_ratio_vs_magnitude` (exclude outliers if present).
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "fig4_1sigma_counts.png"

    ratio = df["Ratio"].to_numpy(dtype=float)
    finite = np.isfinite(ratio)

    if "Is_Outlier" in df.columns:
        good = finite & (~df["Is_Outlier"].to_numpy(dtype=bool))
    else:
        good = finite

    if np.sum(good) < 2:
        good = finite

    mean_ratio = float(np.mean(ratio[good])) if np.any(good) else float("nan")
    std_ratio = float(np.std(ratio[good], ddof=1)) if np.sum(good) > 1 else 0.0
    upper = mean_ratio + std_ratio

    grouped = df.groupby("DatasetID")["Ratio"]

    def _count_valid(s: pd.Series) -> int:
        arr = s.to_numpy(dtype=float)
        return int(np.sum(np.isfinite(arr)))

    def _count_above(s: pd.Series) -> int:
        arr = s.to_numpy(dtype=float)
        return int(np.sum(np.isfinite(arr) & (arr > upper)))

    counts = grouped.apply(_count_above)
    totals_valid = grouped.apply(_count_valid)

    with np.errstate(invalid="ignore", divide="ignore"):
        rates = (counts / totals_valid) * 100.0

    counts = counts.sort_values(ascending=False)
    labels = counts.index.tolist()
    values = counts.to_numpy(dtype=float)
    def _color_for(label: str) -> str:
        rate = float(rates.loc[label])
        if np.isnan(rate):
            return "gray"
        return "red" if rate > 10.0 else "gray"

    colors = [_color_for(label) for label in labels]

    height = max(4.0, 0.25 * len(labels) + 1.0)
    with plt.rc_context(_STYLE):
        fig, ax = plt.subplots(figsize=(8, height))
        y_pos = np.arange(len(labels))
        ax.barh(y_pos, values, color=colors)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels)
        ax.invert_yaxis()
        ax.set_xlabel("Count Above +1σ (N)")
        ax.grid(True, axis="x", alpha=0.3, linestyle="--")
        fig.tight_layout()
        fig.savefig(out_path, dpi=300)
        plt.close(fig)

    return out_path


def plot_ratio_ranking(df: pd.DataFrame, out_dir: str | Path = Path("results/classic_audit")) -> Path:
    """
    Rank datasets by their mean Ratio (ΔE / scaled ΔV).

    The mean is computed on finite Ratio values, excluding global outliers
    (Is_Outlier) if the column exists.
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "fig5_ratio_ranking.png"
    out_csv = out_dir / "ratio_ranking_summary.csv"

    if "Ratio" not in df.columns:
        raise ValueError("DataFrame must include 'Ratio' column.")

    ratio = df["Ratio"].to_numpy(dtype=float)
    finite = np.isfinite(ratio)
    mask = finite
    if "Is_Outlier" in df.columns:
        mask &= ~df["Is_Outlier"].to_numpy(dtype=bool)

    df_valid = df.loc[mask, ["DatasetID", "Ratio"]].copy()
    if df_valid.empty:
        raise ValueError("No valid Ratio values available for ranking.")

    stats = (
        df_valid.groupby("DatasetID")["Ratio"]
        .agg(N="size", Mean_Ratio="mean", Std_Ratio=lambda s: float(np.std(s.to_numpy(dtype=float), ddof=1)) if len(s) > 1 else 0.0)
        .sort_values("Mean_Ratio", ascending=False)
    )
    stats.to_csv(out_csv)

    labels = stats.index.tolist()
    values = stats["Mean_Ratio"].to_numpy(dtype=float)

    colors = ["red" if v > 1.0 else "gray" for v in values]

    height = max(4.0, 0.25 * len(labels) + 1.0)
    x_max = max(1.5, float(np.nanmax(values)) * 1.1)

    with plt.rc_context(_STYLE):
        fig, ax = plt.subplots(figsize=(8, height))
        y_pos = np.arange(len(labels))
        ax.barh(y_pos, values, color=colors)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels)
        ax.invert_yaxis()
        ax.axvline(1.0, color="black", linestyle="--", linewidth=1)
        ax.set_xlim(0.0, x_max)
        ax.set_xlabel("Mean Ratio (ΔE / scaled ΔV)")
        ax.grid(True, axis="x", alpha=0.3, linestyle="--")

        pad = 0.01 * x_max
        for i, v in enumerate(values):
            ax.text(v + pad, i, f"{v:.2f}", va="center", ha="left", fontsize=8)

        fig.tight_layout()
        fig.savefig(out_path, dpi=300)
        plt.close(fig)

    return out_path


def plot_1sigma_rate_ranking(df: pd.DataFrame, out_dir: str | Path = Path("results/classic_audit")) -> Path:
    """
    Rank datasets by their +1σ exceedance rate on Ratio.

    Definition:
      A sample counts as "1σ outlier" if Ratio > (Global Mean + 1σ), where global
      stats are computed the same way as in `plot_ratio_vs_magnitude` (exclude
      Is_Outlier rows if present).
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "fig6_1sigma_rate_ranking.png"

    if "DatasetID" not in df.columns or "Ratio" not in df.columns:
        raise ValueError("DataFrame must include 'DatasetID' and 'Ratio' columns.")

    ratio = df["Ratio"].to_numpy(dtype=float)
    finite = np.isfinite(ratio)

    if "Is_Outlier" in df.columns:
        good = finite & (~df["Is_Outlier"].to_numpy(dtype=bool))
    else:
        good = finite

    if np.sum(good) < 2:
        good = finite

    mean_ratio = float(np.mean(ratio[good])) if np.any(good) else float("nan")
    std_ratio = float(np.std(ratio[good], ddof=1)) if np.sum(good) > 1 else 0.0
    upper = mean_ratio + std_ratio

    grouped = df.groupby("DatasetID")["Ratio"]

    def _count_valid(s: pd.Series) -> int:
        arr = s.to_numpy(dtype=float)
        return int(np.sum(np.isfinite(arr)))

    def _count_above(s: pd.Series) -> int:
        arr = s.to_numpy(dtype=float)
        return int(np.sum(np.isfinite(arr) & (arr > upper)))

    n_valid = grouped.apply(_count_valid)
    n_above = grouped.apply(_count_above)

    with np.errstate(invalid="ignore", divide="ignore"):
        rates = (n_above / n_valid) * 100.0

    rates = rates.sort_values(ascending=False)
    labels = rates.index.tolist()
    values = rates.to_numpy(dtype=float)

    def _color(v: float) -> str:
        if np.isnan(v):
            return "gray"
        return "red" if v > 10.0 else "gray"

    colors = [_color(v) for v in values]

    height = max(4.0, 0.25 * len(labels) + 1.0)
    with plt.rc_context(_STYLE):
        fig, ax = plt.subplots(figsize=(8, height))
        y_pos = np.arange(len(labels))
        ax.barh(y_pos, values, color=colors)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels)
        ax.set_xlim(0, 100)
        ax.invert_yaxis()
        ax.set_xlabel("Rate Above +1σ (%)")
        ax.grid(True, axis="x", alpha=0.3, linestyle="--")
        fig.tight_layout()
        fig.savefig(out_path, dpi=300)
        plt.close(fig)

    return out_path
