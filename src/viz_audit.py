"""
Ronnier-style visualization helpers for the Classic Statistical Audit.

Figures:
  - fig1_bias.png: dV vs dE scatter with y=x reference.
  - fig2_outlier_ranking.png: per-dataset outlier rate bar chart.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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

