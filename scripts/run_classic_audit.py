"""
Classic Statistical Audit for color difference datasets (Ronnier-style).

Pipeline:
  1) Load datasets from a MATLAB .mat file.
  2) Compute CIEDE2000 dE, dE/dV ratios, and global outliers.
  3) Export full per-pair audit table and generate two figures.

Outputs (default):
  - results/classic_audit/full_audit_data.csv
  - results/classic_audit/fig1_bias.png
  - results/classic_audit/fig2_outlier_ranking.png
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from scipy.io import loadmat


def _ensure_repo_imports() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(repo_root))


def _default_mat_path() -> Path:
    candidates = [
        Path("data/dataset_comprehensive.mat"),
        Path("dataset_comprehensive.mat"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def load_data(filepath: str | Path) -> dict[str, dict[str, np.ndarray]]:
    """
    Load datasets from a MATLAB .mat file.

    Supports two layouts:
      1) Repo layout: a single variable named 'dataset_comprehensive' which is a
         (N, 9) MATLAB cell-array. Each row is a dataset, with the data matrix
         in field 2 (Nx10 float array).
      2) Generic layout: each non-__ key is a dataset struct with fields
         'Ref_XYZ', 'Sam_XYZ', and 'DV' (optionally 'XYZw').
    """
    mat = loadmat(str(filepath))
    datasets: dict[str, dict[str, np.ndarray]] = {}

    for key, value in mat.items():
        if key.startswith("__"):
            continue

        if key == "dataset_comprehensive":
            cell = value
            if not isinstance(cell, np.ndarray) or cell.dtype != object or cell.ndim != 2:
                raise ValueError("Unexpected 'dataset_comprehensive' format; expected 2D object array.")

            for row_idx in range(1, cell.shape[0]):  # skip header row
                row = cell[row_idx]
                dataset_id = (
                    str(row[1][0])
                    if isinstance(row[1], np.ndarray) and row[1].size > 0
                    else f"Dataset_{row_idx}"
                )
                xyz_data = np.asarray(row[2], dtype=float)
                if xyz_data.ndim != 2 or xyz_data.shape[1] < 10:
                    raise ValueError(f"{dataset_id}: expected Nx10 float array in field 2.")

                datasets[dataset_id] = {
                    "XYZw": xyz_data[:, 0:3],
                    "Ref_XYZ": xyz_data[:, 3:6],
                    "Sam_XYZ": xyz_data[:, 6:9],
                    "DV": xyz_data[:, 9].astype(float),
                }
            continue

        extracted = _extract_dataset_struct(value)
        if extracted is not None:
            datasets[key] = extracted

    if not datasets:
        raise ValueError("No datasets found in .mat file (no usable keys).")

    return datasets


def _extract_dataset_struct(value: Any) -> dict[str, np.ndarray] | None:
    if not isinstance(value, np.ndarray) or value.dtype.names is None:
        return None

    field_names = set(value.dtype.names)
    required = {"Ref_XYZ", "Sam_XYZ", "DV"}
    if not required.issubset(field_names):
        return None

    ref_xyz = np.asarray(value["Ref_XYZ"][0, 0], dtype=float)
    sam_xyz = np.asarray(value["Sam_XYZ"][0, 0], dtype=float)
    dv = np.asarray(value["DV"][0, 0], dtype=float).reshape(-1)

    out: dict[str, np.ndarray] = {
        "Ref_XYZ": ref_xyz,
        "Sam_XYZ": sam_xyz,
        "DV": dv,
    }
    if "XYZw" in field_names:
        out["XYZw"] = np.asarray(value["XYZw"][0, 0], dtype=float)
    return out


def run_classic_audit(
    datasets: dict[str, dict[str, np.ndarray]],
    difference: str = "CIEDE2000",
    adaptation_transform: str = "CAT02",
) -> pd.DataFrame:
    _ensure_repo_imports()
    from src.models import CIEDE2000, SUCS, xyz_to_lab_user_whitepoint

    frames: list[pd.DataFrame] = []

    diff_key = difference.strip().lower()
    if diff_key in {"ciede2000", "de00", "de_00"}:
        mode = "ciede2000"
        model = CIEDE2000(kL=1.0, kC=1.0, kH=1.0)
    elif diff_key in {"sucs", "sucs"}:
        mode = "sucs"
        model = SUCS(adaptation_transform=adaptation_transform)
    else:
        raise ValueError(f"Unknown difference '{difference}'. Use 'CIEDE2000' or 'sUCS'.")

    for dataset_id, ds in datasets.items():
        ref_xyz = np.asarray(ds["Ref_XYZ"], dtype=float)
        sam_xyz = np.asarray(ds["Sam_XYZ"], dtype=float)
        dv = np.asarray(ds["DV"], dtype=float).reshape(-1)

        if ref_xyz.ndim != 2 or ref_xyz.shape[1] != 3:
            raise ValueError(f"{dataset_id}: Ref_XYZ must be Nx3, got {ref_xyz.shape}.")
        if sam_xyz.shape != ref_xyz.shape:
            raise ValueError(f"{dataset_id}: Sam_XYZ must match Ref_XYZ shape, got {sam_xyz.shape}.")
        if dv.shape[0] != ref_xyz.shape[0]:
            raise ValueError(f"{dataset_id}: DV must be length N, got {dv.shape} for N={ref_xyz.shape[0]}.")

        if "XYZw" in ds:
            xyz_w = np.asarray(ds["XYZw"], dtype=float)
            if xyz_w.shape != ref_xyz.shape:
                raise ValueError(f"{dataset_id}: XYZw must be Nx3, got {xyz_w.shape}.")

            max_xyz = float(max(np.max(ref_xyz), np.max(sam_xyz), np.max(xyz_w)))
            scale = 0.01 if max_xyz > 1.5 else 1.0
            ref_xyz = ref_xyz * scale
            sam_xyz = sam_xyz * scale
            xyz_w = xyz_w * scale
            ref_lab = xyz_to_lab_user_whitepoint(ref_xyz, xyz_w)
            sam_lab = xyz_to_lab_user_whitepoint(sam_xyz, xyz_w)
        else:
            import colour

            max_xyz = float(max(np.max(ref_xyz), np.max(sam_xyz)))
            scale = 0.01 if max_xyz > 1.5 else 1.0
            ref_xyz = ref_xyz * scale
            sam_xyz = sam_xyz * scale

            ref_lab = colour.XYZ_to_Lab(ref_xyz)
            sam_lab = colour.XYZ_to_Lab(sam_xyz)

        if mode == "ciede2000":
            dE = np.asarray(model.predict(ref_lab, sam_lab, input_type="Lab"), dtype=float).reshape(-1)
        else:
            if "XYZw" not in ds:
                raise ValueError(f"{dataset_id}: sUCS requires per-pair whitepoint XYZw.")
            dE = np.asarray(
                model.predict(ref_xyz, sam_xyz, input_type="XYZ", whitepoint=xyz_w),
                dtype=float,
            ).reshape(-1)

        # Dataset-wise scaling factor F (least squares) to align visual scale to computed scale.
        # Uses the same closed-form as in STRESS (but applied per dataset):
        #   dv ≈ F * dE  =>  F = Σ(dE·dv) / Σ(dE²)
        denom = float(np.sum(dE ** 2))
        if denom <= 0.0:
            F = np.nan
            dv_scaled = np.full_like(dv, np.nan, dtype=float)
        else:
            F = float(np.sum(dE * dv) / denom)
            dv_scaled = dv / F if F != 0.0 else np.full_like(dv, np.nan, dtype=float)

        ratio = np.where(dv_scaled == 0, np.nan, dE / dv_scaled)

        frames.append(
            pd.DataFrame(
                {
                    "DatasetID": dataset_id,
                    "Ref_L": ref_lab[:, 0],
                    "Ref_a": ref_lab[:, 1],
                    "Ref_b": ref_lab[:, 2],
                    "Sam_L": sam_lab[:, 0],
                    "Sam_a": sam_lab[:, 1],
                    "Sam_b": sam_lab[:, 2],
                    "dV": dv,
                    "dV_scaled": dv_scaled,
                    "dE": dE,
                    "Ratio": ratio,
                    "F": F,
                }
            )
        )

    df = pd.concat(frames, ignore_index=True)

    global_mean = float(df["Ratio"].mean())
    global_std = float(df["Ratio"].std())

    if np.isnan(global_std) or global_std == 0.0:
        df["Is_Outlier"] = False
    else:
        df["Is_Outlier"] = (df["Ratio"] - global_mean).abs() > 2.0 * global_std

    return df


def main() -> int:
    parser = argparse.ArgumentParser(description="Classic Statistical Audit (Ronnier analysis).")
    parser.add_argument("--mat-file", type=Path, default=_default_mat_path())
    parser.add_argument("--out-dir", type=Path, default=Path("results/classic_audit"))
    parser.add_argument(
        "--difference",
        type=str,
        default="CIEDE2000",
        help="Computed difference method: 'CIEDE2000' (DE00) or 'sUCS'.",
    )
    parser.add_argument(
        "--adaptation-transform",
        type=str,
        default="CAT02",
        help="Von Kries chromatic adaptation transform for sUCS (e.g., CAT02, Bradford).",
    )
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)

    datasets = load_data(args.mat_file)
    df = run_classic_audit(datasets, difference=args.difference, adaptation_transform=args.adaptation_transform)

    out_csv = args.out_dir / "full_audit_data.csv"
    df.to_csv(out_csv, index=False)
    print(f"Wrote: {out_csv}")

    from src.viz_audit import (
        plot_1sigma_counts,
        plot_1sigma_rate_ranking,
        plot_global_bias,
        plot_outlier_counts,
        plot_outlier_ranking,
        plot_ratio_ranking,
        plot_ratio_vs_magnitude,
    )

    plot_global_bias(df, out_dir=args.out_dir)
    plot_ratio_vs_magnitude(df, out_dir=args.out_dir)
    plot_outlier_ranking(df, out_dir=args.out_dir)
    plot_outlier_counts(df, out_dir=args.out_dir)
    plot_1sigma_counts(df, out_dir=args.out_dir)
    plot_ratio_ranking(df, out_dir=args.out_dir)
    plot_1sigma_rate_ranking(df, out_dir=args.out_dir)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
