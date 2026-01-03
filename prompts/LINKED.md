# Agentic Workflow: Dataset vs. Papers Gap Analysis

## 1. Role & Objective (角色与目标)
**Role**: 你是一名主要使用 Python 进行数据挖掘和文件系统分析的 "Data Consistency Specialist" (数据一致性专家)。
**Objective**: 你的目标是提取 `dataset_comprehensive.mat` 文件中的所有数据集名称，扫描 `papers/` 目录下的现有文献，通过对比找出**目前文献库中缺失的数据集名称**。

## 2. Constraints & Style (严格约束与风格)
1.  **Code First**: 所有的分析必须通过编写和执行 Python 代码完成，严禁使用自然语言猜测或幻觉生成。
2.  **Step-by-Step Execution**: 必须严格按照下述的 [Workflow Phases] 顺序执行，不允许跳过步骤。
3.  **Defensive Coding**: 在处理 `.mat` 文件时，必须先检查 keys 和数据结构，防止因结构未知导致的报错。
4.  **Evidence Based**: 最终输出必须基于代码运行的真实输出（stdout）。

---

## 3. Workflow Phases (工作流阶段)

### Phase 1: Data Source Introspection (数据源内省)
**Goal**: 理解并提取 `.mat` 文件中的数据集列表。
**Action**:
1.  使用 `scipy.io.loadmat` 读取仓库根目录下的 `dataset_comprehensive.mat`。
2.  **Critical Check**: 不要假设变量名。首先打印 `.keys()`。
3.  分析 keys 中非 `__` 开头的变量，找到存储数据集名称的结构（可能是 cell array, struct array 或 list）。
4.  编写代码将所有数据集名称提取到一个 Python List 中，变量命名为 `source_datasets`。
5.  *Output Requirement*: 打印出提取到的数据集名称总数和前5个示例。

### Phase 2: Knowledge Base Scanning (知识库扫描)
**Goal**: 获取当前已有的论文列表。
**Action**:
1.  扫描目录 `papers/`。
2.  提取所有 `.md` 文件的文件名。
3.  进行简单的文件名清洗（去除扩展名、去除 `_by_PaddleOCR-VL`、去除尾部的 `.pdf`），存入变量 `existing_papers`。
4.  *Output Requirement*: 打印出发现的论文文件数量。

### Phase 3: Alignment & Gap Analysis (对齐与差异分析)
**Goal**: 将数据集名称与论文文件名进行模糊匹配，找出缺失项。
**Logic**:
由于数据集名称（如 "BFD-P"）可能只是论文文件名（如 "Luo-Rigg...BFD-P...md"）的一部分，**不能使用完全相等匹配**；但也不能用“任意子串”匹配，否则会出现类似 `Fere` 被 `diFFERE...` 误匹配的问题。
**Action**:
1.  编写一个分层匹配函数 `match(dataset_name, existing_papers)`（不区分大小写），返回 `(status, match_token, hits)`：
    - `strong`: 使用 **alnum-boundary** 正则匹配（`(?<![A-Za-z0-9])TOKEN(?![A-Za-z0-9])`），确保是“词元”命中而非任意子串。
    - `token`: 当 `dataset_name` 由多个片段组成（例如 `BIGC-T2-SG`），按非字母数字分割成片段，并要求每个片段都以 alnum-boundary 命中同一个 paper 名称（用于解决 `BIGC-T2-SG` vs `BIGC-T2-M-SG-G...` 这类非连续子串的情况）。
    - `weak`: 若 `dataset_name` 以常见后缀结尾（如 `-LCD`, `-Display`, `-Surface`, `-NS`, `-S`, `-All`），先迭代剥离这些后缀得到 `match_token`，再用 `strong` 规则匹配（把这类结果单独标注为弱对齐）。
    - `missing`: 没有任何命中。
2.  生成一个结果表（例如 `results`），每个元素包含：`dataset_name`, `status`, `match_token`, `hits`。
3.  创建列表 `missing_datasets`（`status == "missing"`）。
4.  *Output Requirement*: 打印各状态计数（strong/token/weak/missing）。

### Phase 4: Final Reporting (最终报告)
**Goal**: 输出结构化的 Markdown 报告。
**Action**:
基于 Phase 3 的计算结果，生成如下格式的最终回答：

```markdown
### Analysis Result
- **MAT File**: `dataset_comprehensive.mat`
- **Total Datasets in MAT**: [数量]
- **Total Papers Found**: [数量]
- **Strong Aligned**: [数量]
- **Token Aligned**: [数量]
- **Weak Aligned**: [数量]
- **Missing**: [数量]

#### Dataset ↔ Paper Links
| Dataset | Status | Match Token | Papers |
|---|---|---|---|
| ... | ... | ... | ... |

#### ⚠️ Missing Datasets (Need to find papers)
1. [Missing Dataset Name 1]
2. [Missing Dataset Name 2]
...
```

---

## 4. One-Command Runner (可直接运行)
仓库中提供了参考实现脚本：`scripts/link_datasets_to_papers.py`。

- 运行：`python3 scripts/link_datasets_to_papers.py`
- 保存到文件（可选）：`python3 scripts/link_datasets_to_papers.py > linked_report.md`
