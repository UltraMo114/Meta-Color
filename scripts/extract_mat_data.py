"""
Extract actual data from dataset_comprehensive.mat
"""
import scipy.io as sio
import numpy as np

# Load the .mat file
mat_file = 'dataset_comprehensive.mat'
mat_data = sio.loadmat(mat_file)

dataset = mat_data['dataset_comprehensive']

# First row is headers
headers = [str(field[0][0]) if field.size > 0 else '' for field in dataset[0]]
print("Column headers:")
for i, h in enumerate(headers):
    print(f"  {i}: {h}")

print("\n" + "="*80)
print("Sample datasets (rows 1-5):")
print("="*80)

# Look at actual data (skip header row)
for row_idx in range(1, min(6, dataset.shape[0])):
    row = dataset[row_idx]
    print(f"\nDataset {row_idx}:")

    for col_idx, (header, field) in enumerate(zip(headers, row)):
        if isinstance(field, np.ndarray):
            if field.size == 0:
                value = "Empty"
            elif field.dtype == object:
                # Handle nested arrays
                if field.shape == (1, 1):
                    value = str(field[0, 0])
                else:
                    value = f"Array{field.shape}"
            elif field.dtype.kind in ['U', 'S']:  # Unicode or string
                value = str(field[0]) if field.size > 0 else "Empty"
            elif field.size == 1:
                value = str(field.flat[0])
            else:
                value = f"Array{field.shape}"
        else:
            value = str(field)

        print(f"  {header}: {value}")
