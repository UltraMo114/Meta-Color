"""
Inspect XYZ data structure in detail
"""
import scipy.io as sio
import numpy as np

# Load the .mat file
mat_file = 'dataset_comprehensive.mat'
mat_data = sio.loadmat(mat_file)

dataset = mat_data['dataset_comprehensive']

# Get BFD-P dataset (row 1) for detailed inspection
bfd_p = dataset[1]
dataset_name = str(bfd_p[1][0]) if bfd_p[1].size > 0 else "Unknown"
xyz_data = bfd_p[2]

print(f"Dataset: {dataset_name}")
print(f"XYZ data shape: {xyz_data.shape}")
print(f"Number of color pairs: {xyz_data.shape[0]}")
print(f"Number of columns: {xyz_data.shape[1]}")

print("\nFirst 5 rows of XYZ data:")
print(xyz_data[:5])

print("\nColumn statistics:")
for i in range(xyz_data.shape[1]):
    col = xyz_data[:, i]
    print(f"  Column {i}: min={col.min():.4f}, max={col.max():.4f}, mean={col.mean():.4f}")

# Check if columns might be: X_ref, Y_ref, Z_ref, X_sample, Y_sample, Z_sample, dE_visual, ...
print("\nGuessing column meanings:")
print("  Likely structure: [X_ref, Y_ref, Z_ref, X_sample, Y_sample, Z_sample, visual_diff, ...]")
