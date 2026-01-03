"""
Detailed inspection of dataset_comprehensive.mat structure
"""
import scipy.io as sio
import numpy as np

# Load the .mat file
mat_file = 'dataset_comprehensive.mat'
mat_data = sio.loadmat(mat_file)

dataset = mat_data['dataset_comprehensive']
print(f"Dataset shape: {dataset.shape}")
print(f"Number of datasets: {dataset.shape[0]}")
print(f"Number of fields per dataset: {dataset.shape[1]}")

print("\n" + "="*80)
print("Inspecting structure of first dataset:")
print("="*80)

# Look at first dataset
first_dataset = dataset[0]
for i, field in enumerate(first_dataset):
    print(f"\nField {i}:")
    print(f"  Type: {type(field)}")

    if isinstance(field, np.ndarray):
        print(f"  Shape: {field.shape}")
        print(f"  Dtype: {field.dtype}")

        # Show sample data
        if field.size > 0:
            if field.dtype == object or field.dtype.kind == 'U':
                # String data
                print(f"  Content: {field}")
            elif field.size <= 10:
                print(f"  Content: {field}")
            else:
                print(f"  Content (first few): {field.flat[:5]}")

print("\n" + "="*80)
print("Dataset IDs/Names:")
print("="*80)

# Try to find dataset identifiers
for i in range(min(5, dataset.shape[0])):
    print(f"\nDataset {i}:")
    row = dataset[i]
    # First field might be the name/ID
    if isinstance(row[0], np.ndarray) and row[0].size > 0:
        try:
            print(f"  Field 0: {row[0]}")
        except:
            print(f"  Field 0: (complex structure)")
