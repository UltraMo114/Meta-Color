# Meta-Color Framework

A comprehensive Python framework for color perception reliability analysis, transitioning from MATLAB to modern Python with enhanced capabilities.

## Project Overview

The Meta-Color Framework implements a rigorous, modular system for evaluating color difference formulas against empirical datasets. This project addresses the fundamental question: **How reliably do color difference formulas predict human visual perception?**

### Key Features

- **Multi-Model Support**: CIELAB, CIEDE2000, CAM16-UCS color difference models
- **Comprehensive Metrics**: STRESS, dE/dV ratio, RMSE, Pearson correlation
- **Publication-Quality Visualizations**: Forest plots, scatter plots, ratio distributions
- **Rigorous Validation**: Physics-based verification tests
- **Metadata-Rich**: Structured dataset metadata with experimental conditions

## Project Structure

```
Meta-Color/
├── src/                      # Core framework modules
│   ├── schema.py            # Data structures and metadata schemas
│   ├── models.py            # Color difference model wrappers
│   ├── loader.py            # Dataset loading and management
│   ├── metrics.py           # Performance metrics (STRESS, ratios)
│   └── viz_style.py         # Publication-quality plotting
├── tests/                    # Verification tests
│   └── test_physics.py      # Physics-based model validation
├── scripts/                  # Utility scripts
│   ├── extract_metadata.py  # Metadata extraction from papers
│   ├── inspect_mat.py       # .mat file inspection tools
│   └── demo_ratio_analysis.py  # Analysis demonstration
├── data/                     # Data directory
│   └── metadata_registry.json  # Dataset metadata
├── papers/                   # Research papers (markdown)
├── results/                  # Output directory
│   └── figures/             # Generated plots
└── dataset_comprehensive.mat # Raw color pair data
```

## Installation

### Prerequisites

- Python 3.10+
- UV package manager (recommended) or pip

### Setup

```bash
# Clone the repository
git clone <repository-url>
cd Meta-Color

# Install dependencies using UV
uv sync

# Or using pip
pip install -e .
```

### Dependencies

Core dependencies:
- `colour-science` - Color science computations
- `numpy` - Numerical operations
- `scipy` - Scientific computing and .mat file loading
- `pandas` - Data manipulation
- `matplotlib` - Plotting
- `seaborn` - Statistical visualizations
- `pytest` - Testing framework

## Quick Start

### 1. Load Datasets

```python
from src.loader import DataLoader

# Load all datasets
loader = DataLoader()
datasets = loader.load()

# Get specific dataset
bfd_p = loader.get_dataset('BFD-P')
print(f"Dataset: {bfd_p.name}")
print(f"Pairs: {bfd_p.n_pairs}")
```

### 2. Evaluate Color Difference Models

```python
from src.models import CIEDE2000, CIELAB
from src.metrics import evaluate_model_performance
import numpy as np

# Initialize model
model = CIEDE2000()

# Calculate predictions
predicted = []
observed = []

for pair in bfd_p.color_pairs:
    dE = model.predict(pair.xyz_1, pair.xyz_2, input_type='XYZ', whitepoint=pair.xyz_w)
    predicted.append(dE)
    observed.append(pair.visual_difference)

# Evaluate performance
metrics = evaluate_model_performance(np.array(predicted), np.array(observed))
print(f"STRESS: {metrics['stress']:.2f}")
print(f"Mean dE/dV: {metrics['mean_ratio']:.3f}")
```

### 3. Generate Visualizations

```python
from src.viz_style import plot_scatter_with_diagonal, plot_forest

# Scatter plot
fig, ax = plot_scatter_with_diagonal(
    predicted, observed,
    title="CIEDE2000 Performance",
    save_path="results/figures/scatter_ciede2000"
)

# Forest plot (requires data from multiple datasets)
forest_data = {
    'BFD-P': (1.15, 1.05, 1.25),
    'Leeds': (1.08, 0.98, 1.18),
    # ... more datasets
}

fig, ax = plot_forest(
    forest_data,
    xlabel="dE/dV Ratio",
    save_path="results/figures/forest_plot"
)
```

### 4. Run Demo Analysis

```bash
# Run the demonstration script
python scripts/demo_ratio_analysis.py
```

## Module Architecture

### Module 0: Data Infrastructure (Phase 2-3)

**Purpose**: Foundation for all analysis

**Components**:
- `src/schema.py` - Metadata structures (DatasetMetadata, PaperInfo, ExperimentalConditions)
- `src/loader.py` - Dataset loading from .mat files and metadata
- `src/models.py` - Unified color difference model interface

**Key Features**:
- Metadata extraction from research papers
- Flexible .mat file parsing
- Abstract model interface for extensibility

### Module 1: Pragmatic Analysis (Phase 5)

**Purpose**: Rapid evaluation of color difference formulas

**Components**:
- `src/metrics.py` - Performance metrics
  - STRESS (Standardized Residual Sum of Squares)
  - dE/dV ratio analysis
  - RMSE, Pearson correlation
- `src/viz_style.py` - Publication-quality visualizations
  - Forest plots for meta-analysis
  - Scatter plots with regression
  - Ratio distributions

**Outputs**:
- Performance rankings across datasets
- Visual comparison plots
- Statistical summaries

## Testing

### Run All Tests

```bash
# Using UV
PYTHONPATH=. uv run pytest tests/ -v

# Using pytest directly
PYTHONPATH=. pytest tests/ -v
```

### Test Coverage

- **Physics Verification** (`tests/test_physics.py`):
  - Zero-difference sanity checks: dE(A,A) = 0
  - Symmetry: dE(A,B) = dE(B,A)
  - Positive definiteness
  - Cross-validation against known values

## Data Format

### Dataset Structure

Each dataset in `dataset_comprehensive.mat` contains a 10-column array:

**Column Structure (N × 10 array)**:
- **Columns 0-2**: XYZw - White point (D65 illuminant)
- **Columns 3-5**: XYZ1 - First color of the pair
- **Columns 6-8**: XYZ2 - Second color of the pair
- **Column 9**: Visual - Observed visual difference

**ColorPair Object**:
```python
@dataclass
class ColorPair:
    xyz_w: np.ndarray              # White point (columns 0-2)
    xyz_1: np.ndarray              # First color (columns 3-5)
    xyz_2: np.ndarray              # Second color (columns 6-8)
    visual_difference: float       # Visual difference (column 9)
```

### Metadata Schema

```python
@dataclass
class DatasetMetadata:
    id: str                          # Dataset identifier (e.g., 'BFD-P')
    name_in_paper: str              # Name used in original paper
    paper: PaperInfo                # Citation information
    conditions: ExperimentalConditions  # Experimental setup
    sample_size: int                # Number of color pairs
    observer_count: Optional[int]   # Number of observers
    notes_file_path: str           # Path to source paper
```

## Key Metrics

### STRESS (Standardized Residual Sum of Squares)

```
STRESS = 100 * sqrt(Σ(ΔV - f·ΔE)² / Σ(ΔV)²)
```

where f is an optimal scaling factor.

**Interpretation**:
- Lower is better (0 = perfect fit)
- Typical values: 20-60 for good formulas
- >60 indicates poor performance

### dE/dV Ratio

```
Mean ratio = mean(ΔE / ΔV)
```

**Interpretation**:
- 1.0 = perfect prediction on average
- >1.0 = over-prediction (formula exaggerates differences)
- <1.0 = under-prediction (formula underestimates differences)

## Future Enhancements

### Module 2: Heterogeneity Analysis (Planned)
- Dataset clustering by experimental conditions
- Mixed-effects modeling
- Prediction interval estimation

### Module 3: Bayesian Integration (Planned)
- Hierarchical Bayesian models
- Prior elicitation from physics
- Posterior predictive checks

## License

[Specify License]

## Authors

[Your Name/Team]

---

**Status**: Module 0 and Module 1 (Phase 1) Implementation Complete ✓

For questions or issues, please open a GitHub issue.
