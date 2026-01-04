**Objective**: Generate a publication-quality "Statistical Audit Report" summarizing the performance of 32 datasets.
**Methodology**: **Scaled Ratio Analysis** () to examine performance consistency across magnitudes.
**Executor**: Claude 3.5 Sonnet (via Claude Code).

---

## 📚 Step 1: Context & Style Learning

**Instruction**:
"Internalize the academic style of Prof. Ronnier Luo. Focus on how **STRESS** and **Scaling Factors** are described."

**Key Concepts to Master**:

* **Scaling Factor ()**: A multiplier applied to visual data () to minimize the sum of squared errors between  and . Used to bring different datasets (threshold vs. suprathreshold) onto a common scale.
* **Magnitude Dependency**: The phenomenon where a model predicts well for small color differences but fails for large ones (or vice versa).
* **Systematic Bias**: A consistent over- or under-prediction trend.

**Reference Papers**:

1. `papers/Wang-Wang-2012-Evaluation colour-difference formulae.md` (CRITICAL: Look for how they discuss "Performance Factor" and magnitude).
2. `papers/Comprehensive-Luo-2023-Test colour-difference formulae.md`.

---

## 📊 Step 2: Data Synthesis & Interpretation

**Instruction**:
"Analyze `results/classic_audit/full_audit_data.csv`. The `Ratio` column is now `dE / (F * dV)`. Ideally, this should be 1.0."

**Analysis Tasks**:

1. **Global Precision**: What is the Global Mean and Std of the *Scaled Ratio*? (Mean should be close to 1.0 by definition of scaling; Std indicates scatter/noise).
2. **Magnitude Trend Check**: Look at **Fig A** (`fig_ronnier_ratio_trend.png`).
* *Question*: Does the cloud of points tilt?
* *If Left > Right*: The model over-predicts small differences relative to large ones.
* *If Flat*: The model is consistent across magnitudes (Good).


3. **Outlier Identification**: Identify datasets with the highest % of points outside the  range.

---

## 📝 Step 3: Draft the Report (`results/reports/Audit_Report_v2.md`)

**Structure Spec**:

### **1. Introduction**

* **Objective**: To validate the `Meta-Color` data infrastructure against the CIEDE2000 benchmark.
* **Methodology (Crucial)**:
* Explicitly state: "To account for the scaling differences between datasets (e.g., threshold ellipses vs. suprathreshold pairs), a **Scaling Factor ()** was computed for each dataset to minimize the least-squares error between  and ."
* Metric: "The analysis focuses on the **Scaled Ratio** ."



### **2. Performance Consistency (The "Ronnier Plot")**

* **Visual Analysis**: Reference **Fig 1** (`results/classic_audit/fig_ronnier_ratio_trend.png`).
* **Interpretation**:
* Describe the distribution of points relative to the Mean line (Red).
* **Trend Diagnosis**: "The scatter plot reveals [no significant / a slight] dependency on color difference magnitude. The standard deviation bands (blue/green dashed lines) indicate that..."


* **Implication**: Does CIEDE2000 hold up across the 32 datasets?

### **3. Dataset Heterogeneity (The "Naughty List")**

* **Outlier Ranking**: Reference **Fig 2** (`results/classic_audit/fig2_outlier_ranking.png`).
* **High-Noise Datasets**: List the top 3 datasets with the highest outlier rates.
* *Hypothesis*: Why are they noisy? (Check `dataset_paper_mapping.md`: Is it a complex texture? High Dynamic Range?)



### **4. Conclusion**

* **Summary**: The pipeline successfully harmonized 32 datasets using individual scaling factors.
* **Verdict**: The baseline performance confirms the data integrity. The observed outliers in specific datasets suggest the need for weighted modeling in Module 2.

---

## 🎨 Step 4: Formatting

* **Tone**: Strict, objective, quantitative. Avoid "I think" or "We feel". Use "The data suggests...".
* **Formatting**: Standard Markdown. Use LaTeX for math (, ).
* **Citations**: Use `[Author, Year]` format.

---

### 💡 提示：

给 Claude Code 发送时，请附加：

> "Please write this report as if you are preparing a draft for a standard CIE technical committee meeting. The audience (Prof. Luo) is highly sensitive to whether the 'Scaling Factor' was applied correctly, so ensure the Methodology section is precise."