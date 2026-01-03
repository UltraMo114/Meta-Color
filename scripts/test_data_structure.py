"""
验证数据结构修正是否正确
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.loader import DataLoader
from src.models import CIELAB, CIEDE2000
import numpy as np

print("="*80)
print("验证数据结构修正")
print("="*80)

# 加载数据
print("\n1. 加载数据集...")
loader = DataLoader()
datasets = loader.load()

print(f"   成功加载 {len(datasets)} 个数据集")

# 获取第一个数据集
first_dataset = datasets[0]
print(f"\n2. 检查第一个数据集: {first_dataset.name}")
print(f"   颜色对数量: {first_dataset.n_pairs}")

# 检查第一个颜色对
first_pair = first_dataset.color_pairs[0]
print(f"\n3. 检查第一个颜色对的结构:")
print(f"   XYZw (白点):  {first_pair.xyz_w}")
print(f"   XYZ1 (颜色1): {first_pair.xyz_1}")
print(f"   XYZ2 (颜色2): {first_pair.xyz_2}")
print(f"   Visual (视觉差异): {first_pair.visual_difference}")

# 验证数据范围
print(f"\n4. 验证数据范围:")
xyz_w_values = [pair.xyz_w for pair in first_dataset.color_pairs[:100]]
xyz_1_values = [pair.xyz_1 for pair in first_dataset.color_pairs[:100]]
xyz_2_values = [pair.xyz_2 for pair in first_dataset.color_pairs[:100]]
visual_values = [pair.visual_difference for pair in first_dataset.color_pairs[:100]]

print(f"   XYZw Y值范围: {min(p[1] for p in xyz_w_values):.2f} - {max(p[1] for p in xyz_w_values):.2f}")
print(f"   XYZ1 Y值范围: {min(p[1] for p in xyz_1_values):.2f} - {max(p[1] for p in xyz_1_values):.2f}")
print(f"   XYZ2 Y值范围: {min(p[1] for p in xyz_2_values):.2f} - {max(p[1] for p in xyz_2_values):.2f}")
print(f"   Visual值范围: {min(visual_values):.4f} - {max(visual_values):.4f}")

# 测试模型计算
print(f"\n5. 测试颜色差异计算:")
model = CIEDE2000()

# 取前5个颜色对
for i in range(min(5, first_dataset.n_pairs)):
    pair = first_dataset.color_pairs[i]

    # 计算 CIEDE2000
    dE = model.predict(pair.xyz_1, pair.xyz_2, input_type='XYZ')

    print(f"   颜色对 {i+1}: dE={dE:.4f}, Visual={pair.visual_difference:.4f}, 比率={dE/pair.visual_difference:.3f}")

print("\n" + "="*80)
print("✓ 数据结构验证完成！")
print("="*80)
