"""
Plot WCG outliers on the sUCS a-b plane.

This script implements the sUCS conversion locally since the colour-science
library version 0.4.7+ (which includes XYZ_to_sUCS) requires Python 3.10+.
The implementation follows Li & Luo (2024) as documented in the colour-science
source code.

This version plots BOTH reference and sample colors for each pair,
connected by dashed lines for outlier pairs.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import colour

# Set path to include src
repo_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo_root))

from src.loader import DataLoader

# ============================================================================
# sUCS Implementation (from colour-science 0.4.7 source)
# ============================================================================

MATRIX_SUCS_XYZ_TO_LMS = np.array([
    [0.4002, 0.7075, -0.0807],
    [-0.2280, 1.1500, 0.0612],
    [0.0000, 0.0000, 0.9184],
])

MATRIX_SUCS_LMS_P_TO_IAB = np.array([
    [200.0 / 3.05, 100.0 / 3.05, 5.0 / 3.05],
    [430.0, -470.0, 40.0],
    [49.0, 49.0, -98.0],
])


def spow(a, p):
    """Signed power function."""
    a = np.asarray(a)
    return np.sign(a) * np.abs(a) ** p


def XYZ_to_sUCS(XYZ):
    """
    Convert from CIE XYZ tristimulus values to sUCS colourspace.
    
    Parameters
    ----------
    XYZ : array_like
        CIE XYZ tristimulus values, adapted to D65 and in domain [0, 1]
        (where white Y is 1.0).
    
    Returns
    -------
    ndarray
        sUCS Iab colourspace array.
    """
    XYZ = np.asarray(XYZ)
    
    # XYZ to LMS
    LMS = np.dot(XYZ, MATRIX_SUCS_XYZ_TO_LMS.T)
    
    # Apply signed power (p=0.43)
    LMS_p = spow(LMS, 0.43)
    
    # LMS_p to Iab
    Iab = np.dot(LMS_p, MATRIX_SUCS_LMS_P_TO_IAB.T)
    
    return Iab


def convert_xyz_to_sucs_d65(xyz, xyz_w, d65_xyz):
    """Convert XYZ to sUCS with chromatic adaptation to D65."""
    if np.any(xyz_w == 0):
        return np.array([np.nan, np.nan, np.nan])
    
    # Scale so whitepoint Y=1
    scale = 1.0 / xyz_w[1]
    xyz_scaled = xyz * scale
    xyz_w_scaled = xyz_w * scale
    
    # Chromatic adaptation: source whitepoint -> D65
    xyz_d65 = colour.adaptation.chromatic_adaptation_VonKries(
        xyz_scaled, xyz_w_scaled, d65_xyz, transform="CAT02"
    )
    
    # Convert to sUCS
    return XYZ_to_sUCS(xyz_d65)


def plot_sucs_plane():
    output_path = repo_root / "results/classic_audit_sucs/wcg_outliers_sucs_plane.png"
    
    # Load Data
    dl = DataLoader(mat_file=str(repo_root / "dataset_comprehensive.mat"), 
                    metadata_file=str(repo_root / "data/metadata_registry.json"))
    wcg = dl.get_dataset('WCG')
    
    # Load Outlier Info
    audit_df = pd.read_csv(repo_root / "results/classic_audit_sucs/full_audit_data.csv")
    wcg_audit = audit_df[audit_df['DatasetID'] == 'WCG'].reset_index(drop=True)
    
    if len(wcg.color_pairs) != len(wcg_audit):
        print(f"Count mismatch: Raw {len(wcg.color_pairs)} vs Audit {len(wcg_audit)}")
        return

    # Get D65 whitepoint for chromatic adaptation
    illuminant_xy = colour.CCS_ILLUMINANTS["CIE 1964 10 Degree Standard Observer"]["D65"]
    d65_xyz = colour.xy_to_XYZ(illuminant_xy)  # shape (3,), Y=1
    
    ref_iab_list = []
    sam_iab_list = []
    
    print("Computing sUCS coordinates for both reference and sample colors...")
    for i, pair in enumerate(wcg.color_pairs):
        xyz_ref = pair.xyz_1  # Reference
        xyz_sam = pair.xyz_2  # Sample
        xyz_w = pair.xyz_w    # Whitepoint
        
        ref_iab = convert_xyz_to_sucs_d65(xyz_ref, xyz_w, d65_xyz)
        sam_iab = convert_xyz_to_sucs_d65(xyz_sam, xyz_w, d65_xyz)
        
        ref_iab_list.append(ref_iab)
        sam_iab_list.append(sam_iab)

    ref_iab = np.array(ref_iab_list)
    sam_iab = np.array(sam_iab_list)
    
    # Outlier mask
    outliers = wcg_audit['Is_Outlier'].astype(bool).values
    
    # Valid mask (no NaN)
    valid = ~np.isnan(ref_iab[:, 0]) & ~np.isnan(sam_iab[:, 0])
    
    # sUCS a, b are indices 1 and 2
    ref_a, ref_b = ref_iab[:, 1], ref_iab[:, 2]
    sam_a, sam_b = sam_iab[:, 1], sam_iab[:, 2]
    
    # Plotting
    fig, ax = plt.subplots(figsize=(12, 12))
    
    print("Plotting...")
    
    # First, draw dashed lines for outliers (draw lines first so points are on top)
    outlier_indices = np.where(valid & outliers)[0]
    for idx in outlier_indices:
        ax.plot([ref_a[idx], sam_a[idx]], [ref_b[idx], sam_b[idx]], 
                'r--', linewidth=0.8, alpha=0.6, zorder=1)
    
    # Normal pairs: plot both points without connecting lines
    normal_mask = valid & ~outliers
    ax.scatter(ref_a[normal_mask], ref_b[normal_mask], 
               c='gray', alpha=0.4, s=20, marker='o', edgecolors='none', 
               label='Normal (Reference)', zorder=2)
    ax.scatter(sam_a[normal_mask], sam_b[normal_mask], 
               c='lightblue', alpha=0.4, s=20, marker='o', edgecolors='none', 
               label='Normal (Sample)', zorder=2)
    
    # Outlier pairs: plot both points with triangles
    outlier_mask = valid & outliers
    ax.scatter(ref_a[outlier_mask], ref_b[outlier_mask], 
               c='red', s=50, marker='^', edgecolors='darkred', linewidth=0.5,
               label='Outlier (Reference)', zorder=3)
    ax.scatter(sam_a[outlier_mask], sam_b[outlier_mask], 
               c='orange', s=50, marker='v', edgecolors='darkorange', linewidth=0.5,
               label='Outlier (Sample)', zorder=3)
    
    ax.set_xlabel('sUCS $a$', fontsize=12)
    ax.set_ylabel('sUCS $b$', fontsize=12)
    ax.set_title('WCG Dataset: Color Pairs on sUCS $a$-$b$ Plane\n(Outlier pairs connected by dashed lines)', fontsize=14)
    ax.set_aspect('equal')
    ax.legend(fontsize=9, loc='upper right')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.axhline(0, color='black', linewidth=0.5, alpha=0.3)
    ax.axvline(0, color='black', linewidth=0.5, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    print(f"Saved plot to {output_path}")
    print(f"Total pairs: {np.sum(valid)}, Outliers: {np.sum(outlier_mask)}, Normal: {np.sum(normal_mask)}")


if __name__ == "__main__":
    plot_sucs_plane()
