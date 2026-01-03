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
