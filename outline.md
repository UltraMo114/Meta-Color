# outline.md: 跨数据集一致性与不确定性量化研究框架

## 🌲 Root: Color Perception Reliability Framework
> **核心目标**：从底层统计学特性出发，通过量化心理物理学实验中的“不确定性”，重新定义色差公式在多数据集融合下的性能边界。

---

### 📂 Module 0: Data Infrastructure (实验平台层)
* **Data_Loader**: 统一 32 个色差数据集格式（包含反射稿、自发光、阈值级/阈值上数据）。
* **Model_Interface**: 封装主流色差公式（CIELAB, CIEDE2000, CAM16-UCS等）计算接口。
* **Metric_Base**: 基础指标计算引擎（$dE$, $dV$, $STRESS$, $PLCC$, $MCDM$）。

---

### 📂 Module 1: Branch-Pragmatic (导师进度分支)
* **Task**: 快速响应 Ronnier 关于 $dE/dV$ 比率一致性的验证。
* **Sub-nodes**:
    * **Ratio_Analysis**: 计算每个数据集的 $dE/dV$ 均值与标准差（$std$）。
    * **Global_Consistency**: 汇总 32 个数据集的总偏差，建立直观的误差热力图。
    * **Toy_Report_Gen**: 自动化生成包含排名表和基础趋势图的实验简报。
    * **Goal**: 完成工程交付，证明模型在现有简单指标下的表现。

---

### 📂 Module 2: Branch-Diagnostic (异质性挖掘分支)
* **Task**: 利用高阶统计学（元分析）定位数据集间的系统性冲突。
* **Sub-nodes**:
    * **Heterogeneity_Test**: 计算 $I^2$ 统计量与 Cochran's $Q$，量化“变异”中由实验环境导致的比例。
    * **Outlier_Detection**: 通过敏感性分析（Leave-one-out）识别异常数据集。
    * **Subgroup_Insight**: 对比不同介质（屏幕 vs 纸张）下 $dE/dV$ 比例的统计分布差异。
    * **Goal**: 发现隐藏的“金矿”数据或系统偏差。
    


---

### 📂 Module 3: Branch-Scientific (不确定性量化分支 - 核心创新)
* **Task**: 通过双层/分层建模（Hierarchical Modeling）拆解感知边界。
* **Sub-nodes**:
    * **Aleatoric_Estimator**: 提取**受试者间变异 (Subject Variation)**，确定该数据集的物理理论上限。
    * **Epistemic_Estimator**: 提取**数据集偏置 (Dataset Bias)**，量化不同实验室环境带来的认知不确定性。
    * **Likelihood_Boundary**: 绘制各颜色区域的性能天花板（Performance Ceiling）。
    * **Goal**: 证明模型优化已触及人类感知的统计极限。



---

### 📂 Module 4: Branch-Synthesis (模型改良与标准分支)
* **Task**: 基于不确定性分析结果，推导新的参数推荐。
* **Sub-nodes**:
    * **Uncertainty_Aware_Weighting**: 根据数据集的信噪比动态调整训练权重（改良 Loss 函数）。
    * **Boundary_Optimization**: 针对高不确定性区域进行局部流形约束。
    * **CIE_Candidate_Proposal**: 生成符合 CIE 推荐规范的新一代色觉模型参数。
    * **Goal**: 输出具备学术严谨性和统计学解释性的最终结论。

---

### 📂 Module 5: Automation Layer (MCP 自动化执行层)
* **Task**: 将上述逻辑封装为可调用的 Agent 工具链。
* **Tool_Sets**:
    * `run_ratio_audit`: 自动执行 Branch 1。
    * `calculate_uncertainty_bounds`: 调用贝叶斯推断引擎执行 Branch 3。
    * `auto_latex_formatter`: 自动将统计图表转化为符合 TVCG/CRA 格式的 LaTeX 代码。