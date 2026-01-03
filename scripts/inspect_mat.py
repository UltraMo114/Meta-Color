"""
Inspect the structure of dataset_comprehensive.mat
"""
import scipy.io as sio
import numpy as np

# Load the .mat file
mat_file = 'dataset_comprehensive.mat'
mat_data = sio.loadmat(mat_file)

print("Keys in .mat file:")
for key in mat_data.keys():
    if not key.startswith('__'):
        print(f"\n{key}:")
        data = mat_data[key]
        print(f"  Type: {type(data)}")
        print(f"  Shape: {data.shape if hasattr(data, 'shape') else 'N/A'}")
        if hasattr(data, 'dtype'):
            print(f"  Dtype: {data.dtype}")

        # Show first few elements if it's small
        if hasattr(data, 'shape') and len(data.shape) <= 2:
            if data.shape[0] <= 10:
                print(f"  Data preview:")
                print(f"    {data}")
