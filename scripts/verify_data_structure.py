"""
重新仔细检查 .mat 文件的数据结构
"""
import scipy.io as sio
import numpy as np

mat_data = sio.loadmat('dataset_comprehensive.mat')
dataset = mat_data['dataset_comprehensive']

# 获取 BFD-P 数据集（第2行，因为第1行是header）
bfd_p_row = dataset[1]

print("BFD-P 数据集结构：")
print("="*80)

# 打印每个字段
field_names = ['No.', 'Dataset', 'XYZ_data', 'La_Yb_surround', 'Lw', 'Separation', 'Medium', 'Background', 'FoV']

for i, (name, field) in enumerate(zip(field_names, bfd_p_row)):
    print(f"\n字段 {i}: {name}")
    if isinstance(field, np.ndarray):
        print(f"  类型: {type(field)}")
        print(f"  形状: {field.shape}")
        if i == 2:  # XYZ_data
            print(f"  这是 XYZ_data，包含 {field.shape[0]} 个颜色对")
            print(f"\n  前3行数据：")
            for j in range(min(3, field.shape[0])):
                print(f"    行 {j}: {field[j]}")

            print(f"\n  各列的统计信息：")
            for col in range(field.shape[1]):
                col_data = field[:, col]
                print(f"    列 {col}: min={col_data.min():.4f}, max={col_data.max():.4f}, mean={col_data.mean():.4f}, std={col_data.std():.4f}")

print("\n" + "="*80)
print("请问：")
print("1. 列 0-2 是 Reference 的 XYZ 吗？")
print("2. 列 3-5 是什么？Reference 的 Lab 值？")
print("3. 列 6-8 是 Sample 的 XYZ 还是 Lab？")
print("4. 列 9 是 Visual difference 吗？")
print("="*80)
