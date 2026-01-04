"""
Sigma exceedance analysis for the Classic Audit.

Purpose:
  Quantify how many samples fall above / below the ±kσ reference lines used
  in `fig_ronnier_ratio_trend.png`, i.e. computed from global Ratio statistics.

Inputs (default):
  - results/classic_audit/full_audit_data.csv

Outputs (default):
  - results/classic_audit/sigma_exceedance_summary.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def _compute_global_ratio_stats(df: pd.DataFrame) -> tuple[float, float]:
    ratio = df["Ratio"].to_numpy(dtype=float)
    finite = np.isfinite(ratio)

    if "Is_Outlier" in df.columns:
        good = finite & (~df["Is_Outlier"].to_numpy(dtype=bool))
    else:
        good = finite

    if np.sum(good) < 2:
        good = finite

    mean = float(np.mean(ratio[good])) if np.any(good) else float("nan")
    std = float(np.std(ratio[good], ddof=1)) if np.sum(good) > 1 else 0.0
    return mean, std


def _summarize_block(ratio: np.ndarray, mask: np.ndarray, mean: float, std: float, sigma: float) -> dict[str, float]:
    upper = mean + sigma * std
    lower = mean - sigma * std

    n = int(np.sum(mask))
    if n == 0:
        return {
            "N": 0,
            "N_above": 0,
            "Pct_above": float("nan"),
            "N_below": 0,
            "Pct_below": float("nan"),
            "N_outside": 0,
            "Pct_outside": float("nan"),
        }

    above = int(np.sum(mask & (ratio > upper)))
    below = int(np.sum(mask & (ratio < lower)))
    outside = above + below

    return {
        "N": n,
        "N_above": above,
        "Pct_above": 100.0 * above / n,
        "N_below": below,
        "Pct_below": 100.0 * below / n,
        "N_outside": outside,
        "Pct_outside": 100.0 * outside / n,
    }


def run_sigma_exceedance(audit_csv: Path, out_dir: Path, sigma: float) -> Path:
    df = pd.read_csv(audit_csv)
    required = {"DatasetID", "Ratio"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns in audit CSV: {sorted(missing)}")

    ratio = df["Ratio"].to_numpy(dtype=float)
    finite = np.isfinite(ratio)

    mean, std = _compute_global_ratio_stats(df)

    rows: list[dict[str, float | str]] = []

    global_summary = _summarize_block(ratio, finite, mean, std, sigma)
    rows.append(
        {
            "DatasetID": "ALL",
            "Sigma": float(sigma),
            "Mean_Ratio": mean,
            "Std_Ratio": std,
            **global_summary,
        }
    )

    for dataset_id, idx in df.groupby("DatasetID").groups.items():
        mask = np.zeros(len(df), dtype=bool)
        mask[np.fromiter(idx, dtype=int)] = True
        mask &= finite

        summary = _summarize_block(ratio, mask, mean, std, sigma)
        rows.append(
            {
                "DatasetID": str(dataset_id),
                "Sigma": float(sigma),
                "Mean_Ratio": mean,
                "Std_Ratio": std,
                **summary,
            }
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "sigma_exceedance_summary.csv"
    out_df = pd.DataFrame(rows)

    # Sort datasets (keep ALL first) by descending percent-above for quick inspection.
    out_df_rest = out_df[out_df["DatasetID"] != "ALL"].sort_values("Pct_above", ascending=False)
    out_df_all = out_df[out_df["DatasetID"] == "ALL"]
    out_df = pd.concat([out_df_all, out_df_rest], ignore_index=True)

    out_df.to_csv(out_path, index=False)
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Sigma exceedance analysis for Classic Audit ratios.")
    parser.add_argument(
        "--audit-csv",
        type=Path,
        default=Path("results/classic_audit/full_audit_data.csv"),
        help="Path to classic audit CSV.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("results/classic_audit"),
        help="Output directory.",
    )
    parser.add_argument(
        "--sigma",
        type=float,
        default=1.0,
        help="Sigma multiplier (e.g., 1.0 for ±1σ).",
    )
    args = parser.parse_args()

    out_path = run_sigma_exceedance(args.audit_csv, args.out_dir, args.sigma)
    print(f"Wrote: {out_path}")

    # Print a one-line global summary for convenience.
    out_df = pd.read_csv(out_path)
    all_row = out_df[out_df["DatasetID"] == "ALL"].iloc[0]
    print(
        f"ALL | sigma={all_row['Sigma']:.3g} | N={int(all_row['N'])} | "
        f">+{all_row['Sigma']:.3g}σ: {int(all_row['N_above'])} ({all_row['Pct_above']:.2f}%) | "
        f"<-{all_row['Sigma']:.3g}σ: {int(all_row['N_below'])} ({all_row['Pct_below']:.2f}%)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
