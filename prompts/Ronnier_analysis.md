**Role**: You are an expert Python Color Scientist.
**Task**: Implement a "Classic Statistical Audit" pipeline for color difference datasets.
**Constraint**: You must strictly follow the libraries and logic defined below. Do not use `skimage` or `opencv`. Use `colour-science`.

---

## ⚙️ Global Configuration (Context)

* **Input Data**: `data/dataset_comprehensive.mat` (MATLAB struct).
* **Output Directory**: `results/classic_audit/` (Ensure this exists).
* **Required Libraries**:
```python
import numpy as np
import pandas as pd
from scipy.io import loadmat
import colour  # The 'colour-science' package
import matplotlib.pyplot as plt

```



---

## 📄 File 1: Calculation Pipeline Spec

**Target File**: `scripts/run_classic_audit.py`

### 1. Data Loading Strategy

* Function: `load_data(filepath)`
* Logic:
* Load `.mat` file using `scipy.io.loadmat`.
* Iterate over keys. **Ignore** keys starting with `__` (e.g., `__header__`, `__version__`).
* Each valid key represents a `Dataset`.



### 2. Processing Logic (Per Dataset)

* **Input Arrays**: Extract `Ref_XYZ` (Nx3), `Sam_XYZ` (Nx3), `DV` (Visual Difference, Nx1).
* **XYZ Scaling Check (CRITICAL)**:
* Check `np.max(Ref_XYZ)`.
* **If max > 1.5**: Assume data is in 0-100 range. **Divide XYZ by 100.0** to normalize to 0-1 range.
* **If max <= 1.5**: Assume data is already 0-1. Keep as is.


* **Color Conversion**:
* Convert XYZ to Lab using `colour.XYZ_to_Lab`.


* **Delta E Calculation**:
* Calculate `dE` using `colour.delta_E_CIE2000`.
* *Parameters*: `k_L=1, k_C=1, k_H=1`.


* **Ratio Calculation**:
* `Ratio = dE / DV`.
* Handle Edge Case: If `DV == 0`, set `Ratio = np.nan`.



### 3. Statistical Analysis & Aggregation

* **Step A**: Collect ALL rows from ALL datasets into a single Pandas DataFrame.
* Columns: `DatasetID`, `Ref_L`, `Ref_a`, `Ref_b`, `Sam_L`, `Sam_a`, `Sam_b`, `dV`, `dE`, `Ratio`.


* **Step B**: Calculate Global Statistics on the `Ratio` column.
* `Global_Mean = df['Ratio'].mean()`
* `Global_Std = df['Ratio'].std()`


* **Step C**: Outlier Detection.
* Add column `Is_Outlier`: Set to `True` if `abs(Ratio - Global_Mean) > 2 * Global_Std`.


* **Output**: Save DataFrame to `results/classic_audit/full_audit_data.csv`.

---

## 📄 File 2: Visualization Spec

**Target File**: `src/viz_audit.py`

### 1. Style Definition (Academic/Ronnier Style)

* Use `matplotlib.pyplot`.
* Set font to **Times New Roman**: `plt.rcParams["font.family"] = "serif"`, `plt.rcParams["font.serif"] = ["Times New Roman"]`.
* Set Grid: `alpha=0.3`, `linestyle='--'`.

### 2. Plot A: Bias Check (Scatter)

* **Function**: `plot_global_bias(df)`
* **X-axis**: `dV` (Visual Difference).
* **Y-axis**: `dE` (Computed CIEDE2000).
* **Features**:
* Scatter points: Color `#1f77b4` (muted blue), `alpha=0.3`, `s=10`.
* Reference Line: Plot `y=x` (black dashed line, `linewidth=1`).
* Labels: "Visual Difference ()" vs "Computed Difference ()".


* **Save**: `results/classic_audit/fig1_bias.png` (DPI=300).

### 3. Plot B: Outlier Ranking (Bar Chart)

* **Function**: `plot_outlier_rates(df)`
* **Logic**:
* Group by `DatasetID`.
* Calculate `Outlier_Rate %` = (Count of Outliers / Total Count) * 100.
* Sort values descending (Worst dataset at top).


* **Features**:
* Horizontal Bar Chart (`barh`).
* Color Logic: If Rate > 10%, bar color = 'red'. Else, bar color = 'gray'.
* X-axis Limit: 0 to 100.


* **Save**: `results/classic_audit/fig2_outlier_ranking.png`.

---

## 🚀 Execution Instructions for Codex

1. **Generate `scripts/run_classic_audit.py**` first based on File 1 Spec.
2. **Generate `src/viz_audit.py**` second based on File 2 Spec.
3. Ensure `main` block in `run_classic_audit.py` calls the processing function first, then imports `src.viz_audit` to generate plots immediately after calculation.
