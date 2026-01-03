"""
Compute CIEDE2000 (DE00) STRESS on dataset_comprehensive.mat and export
per-pair DE00 values for MATLAB comparison.

Outputs:
  - results/de00_python.csv
  - prints per-dataset and overall STRESS for:
      * de00_py_current: matches current src/models.py behavior
      * de00_py_wp: uses per-pair whitepoint XYZw for XYZ->Lab conversion
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import csv
import numpy as np
import colour

from src.loader import DataLoader
from src.metrics import calculate_stress


_EPSILON = 216 / 24389  # (6/29)^3
_KAPPA = 24389 / 27


def _xyz_to_lab_with_whitepoint(xyz: np.ndarray, xyz_w: np.ndarray) -> np.ndarray:
    """
    Convert XYZ to Lab using an explicit reference whitepoint XYZw (both in same scale).
    Supports vectorized inputs of shape (N, 3).
    """
    xyz = np.asarray(xyz, dtype=float)
    xyz_w = np.asarray(xyz_w, dtype=float)

    if xyz.shape != xyz_w.shape or xyz.shape[1] != 3:
        raise ValueError("xyz and xyz_w must both have shape (N, 3)")

    # Ratios X/Xn, Y/Yn, Z/Zn
    t = xyz / xyz_w

    f = np.where(t > _EPSILON, np.cbrt(t), (_KAPPA * t + 16.0) / 116.0)

    fx, fy, fz = f[:, 0], f[:, 1], f[:, 2]
    L = 116.0 * fy - 16.0
    a = 500.0 * (fx - fy)
    b = 200.0 * (fy - fz)
    return np.stack([L, a, b], axis=1)


def main() -> int:
    loader = DataLoader()
    datasets = loader.load()

    out_path = Path("results/de00_python.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    overall = {
        "dv": [],
        "de00_current": [],
        "de00_wp": [],
    }

    # Current src/models.py behavior: constant illuminant xy (D65 10-degree) and no XYZ scaling.
    illuminant_xy = colour.CCS_ILLUMINANTS["CIE 1964 10 Degree Standard Observer"]["D65"]

    print("=" * 80)
    print("DE00 STRESS on dataset_comprehensive.mat")
    print("=" * 80)

    for ds in datasets:
        raw = np.asarray(ds.raw_data, dtype=float)
        xyzw = raw[:, 0:3]
        xyz1 = raw[:, 3:6]
        xyz2 = raw[:, 6:9]
        dv = raw[:, 9].astype(float)

        # Vectorized "current" computation.
        lab1_current = colour.XYZ_to_Lab(xyz1, illuminant=illuminant_xy)
        lab2_current = colour.XYZ_to_Lab(xyz2, illuminant=illuminant_xy)
        de00_current = colour.difference.delta_E_CIE2000(lab1_current, lab2_current, textiles=False)

        # Whitepoint-aware conversion using per-pair XYZw.
        lab1_wp = _xyz_to_lab_with_whitepoint(xyz1, xyzw)
        lab2_wp = _xyz_to_lab_with_whitepoint(xyz2, xyzw)
        de00_wp = colour.difference.delta_E_CIE2000(lab1_wp, lab2_wp, textiles=False)

        stress_current = calculate_stress(de00_current, dv, use_scaling=True)
        stress_wp = calculate_stress(de00_wp, dv, use_scaling=True)

        print(f"{ds.name:>18s} | n={len(dv):5d} | STRESS current={stress_current:7.3f} | STRESS wp={stress_wp:7.3f}")

        overall["dv"].append(dv)
        overall["de00_current"].append(de00_current)
        overall["de00_wp"].append(de00_wp)

        # Export per pair for MATLAB comparison.
        for i in range(raw.shape[0]):
            rows.append([
                ds.name,
                i + 1,  # 1-based index for MATLAB friendliness
                *xyzw[i].tolist(),
                *xyz1[i].tolist(),
                *xyz2[i].tolist(),
                float(dv[i]),
                float(de00_current[i]),
                float(de00_wp[i]),
            ])

    dv_all = np.concatenate(overall["dv"])
    de00_current_all = np.concatenate(overall["de00_current"])
    de00_wp_all = np.concatenate(overall["de00_wp"])

    print("-" * 80)
    print(
        f"{'ALL':>18s} | n={len(dv_all):5d} | "
        f"STRESS current={calculate_stress(de00_current_all, dv_all, use_scaling=True):7.3f} | "
        f"STRESS wp={calculate_stress(de00_wp_all, dv_all, use_scaling=True):7.3f}"
    )

    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "dataset_id",
            "pair_index",
            "xyzw_X", "xyzw_Y", "xyzw_Z",
            "xyz1_X", "xyz1_Y", "xyz1_Z",
            "xyz2_X", "xyz2_Y", "xyz2_Z",
            "dV",
            "de00_py_current",
            "de00_py_wp",
        ])
        writer.writerows(rows)

    print("-" * 80)
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

