**Role**: Expert Color Scientist & Data Analyst.
**Task**: Implement the "Classic Audit" with **Scaling Normalization** and **Magnitude-Dependent Ratio Analysis**.
**Changes**: Added per-dataset scaling and a specific "Ratio vs Computed DE" plot.

---

## ⚙️ Global Configuration

* **Libraries**: `numpy`, `pandas`, `scipy.io`, `colour`, `matplotlib.pyplot`, `seaborn`.
* **Input**: `data/dataset_comprehensive.mat`.
* **Output**: `results/classic_audit/`.

---

## 📄 File 1: Calculation Pipeline (`scripts/run_classic_audit.py`)

### 1. Data Loading & Scaling (CRITICAL UPDATE)

* **Logic**:
1. Load `.mat` file.
2. Create an empty list `all_data_rows`.
3. Iterate over each `DatasetID`:
* Extract `Ref_XYZ`, `Sam_XYZ`, `DV`.
* **XYZ Normalization**: If `max(XYZ) > 1.5`, divide by 100.
* **Compute dE**: Calculate `dE_00` using `colour.delta_E_CIE2000` (Lab computed from XYZ, D65).
* **Calculate Scaling Factor ()**:
* Formula:  (Minimize least squares error).
* *Note*: This aligns the visual scale to the computed scale.


* **Compute Scaled Ratio**:
* 
* 


* Store rows: `[DatasetID, Ref_L, ..., dE, dV, dV_scaled, Ratio, F]`.




* **Aggregation**: Convert `all_data_rows` to a Pandas DataFrame.

### 2. Outlier Detection

* Calculate `Global_Mean` and `Global_Std` of the **Ratio** column.
* Flag `Is_Outlier`: `True` if `abs(Ratio - Global_Mean) > 2 * Global_Std`.
* **Save**: `results/classic_audit/full_audit_data.csv`.

---

## 📄 File 2: Visualization (`src/viz_audit.py`)

### 1. Plot A: Ronnier's "Ratio vs Magnitude" Plot (NEW)

* **Function**: `plot_ratio_vs_magnitude(df)`
* **Data**: Use all valid data (exclude outliers for the lines calculation, but plot points lightly).
* **X-axis**: `dE` (Computed CIEDE2000).
* **Y-axis**: `Ratio` ().
* **Visual Elements**:
* **Scatter**: Gray dots, small size (`s=5`), high transparency (`alpha=0.2`). Show all data.
* **Reference Lines** (calculated from Global Ratio stats):
* **Mean**: Solid Red Line at  (should be approx 1.0).
* ****: Dashed Blue Lines.
* ****: Dotted Green Lines.


* **Limits**: Y-axis usually [0, 3]. X-axis [0, max(dE)].


* **Style**: Times New Roman, Academic.
* **Filename**: `results/classic_audit/fig_ronnier_ratio_trend.png`.

### 2. Plot B: Outlier Ranking (Updated)

* **Function**: `plot_outlier_ranking(df)`
* Same as before: Horizontal Bar Chart of % outliers per dataset.

---

## 🚀 Execution Instructions for Codex

1. **Step 1**: "Rewrite `scripts/run_classic_audit.py`. Implement the `Scaling Factor F` calculation logic inside the loop for each dataset. This is crucial for normalization."
2. **Step 2**: "Rewrite `src/viz_audit.py`. Implement `plot_ratio_vs_magnitude` strictly according to the specs: X=dE, Y=Ratio, with Mean/Std lines overlay."