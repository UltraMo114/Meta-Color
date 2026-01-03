# AGENT_WORKFLOW.md: Meta-Color Framework Implementation (Module 0 & 1)

**Objective**: Implement the Data Infrastructure (Module 0) and Pragmatic Analysis (Module 1) for the Color Perception Reliability Framework.
**Context**: Transitioning from MATLAB to Python/colour-science.
**Reference**: `outline.md`, `dataset_paper_mapping.md`.

---

## 🟢 Phase 1: Environment & Dependency Setup

**Action**: Verify and install necessary Python packages.

1. Check `pyproject.toml` or create one.
2. Ensure the following dependencies are installed (use `uv add` or `pip install`):
* `numpy`
* `scipy` (for loading .mat files)
* `pandas`
* `colour-science` (Crucial: Standard library for color calculations)
* `matplotlib`
* `seaborn`
* `pytest` (For verification gates)
* `openpyxl` (If exporting Excel reports)



---

## 🟢 Phase 2: Module 0 - Data Infrastructure (Schema & Metadata)

**Goal**: Establish the `DatasetMetadata` contract and populate it using the existing markdown notes.

### Step 2.1: Define Schema (`src/schema.py`)

**Action**: Create `src/schema.py`. Use the following code structure exactly to ensure downstream compatibility.

```python
from dataclasses import dataclass, field
from typing import List, Optional, Literal

@dataclass
class PaperInfo:
    title: str
    authors: List[str]
    year: int
    citation_key: str

@dataclass
class ExperimentalConditions:
    """Attributes for Heterogeneity Analysis (Module 2)"""
    # medium_type: 'surface' (print/textile) or 'display' (CRT/LCD)
    medium_type: Literal['surface', 'display', 'projected', 'mixed', 'unknown']
    # magnitude: 'threshold' (<1dE), 'suprathreshold-small' (1-5dE), 'large' (>5dE)
    magnitude: Literal['threshold', 'suprathreshold-small', 'suprathreshold-large', 'unknown']
    texture: Literal['matte', 'glossy', 'semi-gloss', 'unknown']
    background_luminance: Optional[float] = None  # cd/m2

@dataclass
class DatasetMetadata:
    id: str                # Key matching the .mat file
    name_in_paper: str
    paper: PaperInfo
    conditions: ExperimentalConditions
    sample_size: int       # Number of pairs
    observer_count: Optional[int] = None
    
    # Metadata Source Check
    notes_file_path: str = "" # Which .md file this info came from

```

### Step 2.2: Extract Metadata via Agent

**Action**:

1. Read `dataset_paper_mapping.md` to understand the list of datasets.
2. Iterate through the corresponding markdown files in the `papers/` directory.
3. Extract information to instantiate `DatasetMetadata` for each dataset.
4. **Output**: Save the result as `data/metadata_registry.json`.
* *Note*: If specific fields (like `observer_count` or `luminance`) are missing in the notes, set them to `null`. Do not hallucinate.



---

## 🟢 Phase 3: Module 0 - Model Interface & Core Logic

**Goal**: Implement the Python version of color difference formulas using `colour-science`.

### Step 3.1: Create Model Wrappers (`src/models.py`)

**Action**: Implement the `Model_Interface` defined in `outline.md`.

* Create an abstract base class `ColorDifferenceModel`.
* Implement `CIELAB`, `CIEDE2000`, `CAM16UCS`.
* **Requirement**: Use `colour-science` library functions. Do NOT manually implement the math unless absolutely necessary.
* **Input Standard**: All `predict` methods must accept `XYZ` (0-100 range) or `Lab` as standard inputs.

### Step 3.2: Data Loader Implementation (`src/loader.py`)

**Action**:

1. Inspect `dataset_comprehensive.mat` structure. (List keys to understand how data is stored).
2. Create `DataLoader` class that:
* Loads the `.mat` file.
* Loads `metadata_registry.json`.
* Merges them: Returns a list of objects containing both *Metadata* and *Raw Arrays* (Reference XYZ, Sample XYZ, Visual Difference).



---

## 🟢 Phase 4: Module 0 - Verification Gate (The "Ronnier" Test)

**Goal**: Ensure Python results match specific expectations before proceeding.

### Step 4.1: Create Unit Tests (`tests/test_physics.py`)

**Action**: Create a `pytest` file.

1. **Sanity Check**: `dE(ColorA, ColorA)` must equal 0.
2. **Symmetry Check**: `dE(A, B)` must equal `dE(B, A)`.
3. **Cross-Validation Stub**:
* Create a test function `test_vs_matlab_benchmark()`.
* *Instruction*: Since we don't have the MATLAB output yet, define hardcoded input XYZ values (e.g., standard pairs) and print the Python `colour-science` output.
* *User Interaction*: Ask the user: "I have generated test values for CIEDE2000. Please verify these against your MATLAB baseline if strictly required, or authorize me to trust the `colour-science` library."



---

## 🟢 Phase 5: Module 1 - Pragmatic Analysis & Visualization

**Goal**: Calculate  and generate publication-quality plots.

### Step 5.1: Metric Calculation (`src/metrics.py`)

**Action**: Implement the specific metrics from `outline.md`:

* **STRESS**: Standardized Residual Sum of Squares.
* **dE/dV Ratio**: Mean ratio between calculated metric () and visual difference ().

### Step 5.2: Define Plotting Standard (`src/viz_style.py`)

**Action**: Create a centralized style configuration for `matplotlib`.

* **Font**: Times New Roman (preferred for IEEE/CRA) or Arial.
* **Font Size**: Axis labels 12pt, Ticks 10pt, Title 14pt.
* **Line/Markers**: Clear edge colors, avoid "default rainbow" colors.
* **Format**: PDF or high-res PNG (300 DPI).
* **Grid**: Minimal or None (Tufte style).

Code snippet for `viz_style.py`:

```python
import matplotlib.pyplot as plt

def apply_science_style():
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman"],
        "axes.labelsize": 12,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.dpi": 300,
        "axes.grid": True,
        "grid.alpha": 0.3,
        "grid.linestyle": "--"
    })

```

### Step 5.3: Generate Reports (Branch-Pragmatic)

**Action**:

1. **Ratio Analysis**: Calculate Mean/Std of  for all 32 datasets using CIEDE2000 and CAM16-UCS.
2. **Visualization**:
* Plot 1: **Forest Plot** (Error Bar Plot) showing the Mean  and Std Dev for each dataset.
* Plot 2: **Performance Ranking Table** (saved as CSV/Markdown).


3. Save figures to `results/figures/`.

---

## 🟢 Phase 6: Final Review

**Action**: Summarize what has been built.

1. List processed datasets.
2. Report any datasets that failed to load or lacked metadata.
3. Provide the path to the generated plots.

---