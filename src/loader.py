"""
Data loader for color difference datasets

This module loads the .mat file containing color pair data and merges it
with metadata from metadata_registry.json.
"""

import json
import scipy.io as sio
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass

from src.schema import DatasetMetadata, PaperInfo, ExperimentalConditions


@dataclass
class ColorPair:
    """Represents a single color pair with white point and two colors"""
    xyz_w: np.ndarray  # White point XYZ (shape: 3,) - columns 0-2
    xyz_1: np.ndarray  # First color XYZ (shape: 3,) - columns 3-5
    xyz_2: np.ndarray  # Second color XYZ (shape: 3,) - columns 6-8
    visual_difference: float  # Visual difference assessment - column 9


@dataclass
class Dataset:
    """Complete dataset with metadata and color pairs"""
    metadata: DatasetMetadata
    color_pairs: List[ColorPair]
    raw_data: np.ndarray  # Original data array from .mat file

    @property
    def name(self) -> str:
        return self.metadata.id

    @property
    def n_pairs(self) -> int:
        return len(self.color_pairs)

    def __repr__(self):
        return f"Dataset(name='{self.name}', n_pairs={self.n_pairs})"


class DataLoader:
    """Loads and manages color difference datasets"""

    def __init__(self,
                 mat_file: str = 'dataset_comprehensive.mat',
                 metadata_file: str = 'data/metadata_registry.json'):
        """
        Initialize DataLoader

        Parameters
        ----------
        mat_file : str
            Path to the .mat file containing dataset arrays
        metadata_file : str
            Path to the JSON file containing metadata
        """
        self.mat_file = mat_file
        self.metadata_file = metadata_file
        self._mat_data = None
        self._metadata_dict = None
        self._datasets = None

    def load(self) -> List[Dataset]:
        """
        Load all datasets with metadata

        Returns
        -------
        List[Dataset]
            List of Dataset objects containing metadata and color pairs
        """
        if self._datasets is not None:
            return self._datasets

        # Load .mat file
        print(f"Loading .mat file: {self.mat_file}")
        self._mat_data = sio.loadmat(self.mat_file)

        # Load metadata
        print(f"Loading metadata: {self.metadata_file}")
        with open(self.metadata_file, 'r', encoding='utf-8') as f:
            metadata_list = json.load(f)

        # Create metadata dictionary keyed by dataset ID
        self._metadata_dict = {m['id']: m for m in metadata_list}

        # Extract datasets from .mat file
        mat_datasets = self._mat_data['dataset_comprehensive']

        # Skip header row (row 0)
        datasets = []
        for row_idx in range(1, mat_datasets.shape[0]):
            row = mat_datasets[row_idx]

            # Extract dataset information
            dataset_id = str(row[1][0]) if row[1].size > 0 else None
            if dataset_id is None:
                continue

            # Get XYZ data array
            xyz_data = row[2]

            # Get metadata if available
            if dataset_id in self._metadata_dict:
                metadata_dict = self._metadata_dict[dataset_id]
                metadata = self._dict_to_metadata(metadata_dict)
            else:
                # Create minimal metadata if not found
                print(f"Warning: No metadata found for {dataset_id}, using minimal metadata")
                metadata = self._create_minimal_metadata(dataset_id, row)

            # Update sample size from actual data
            metadata.sample_size = xyz_data.shape[0]

            # Parse color pairs
            color_pairs = self._parse_color_pairs(xyz_data)

            # Create Dataset object
            dataset = Dataset(
                metadata=metadata,
                color_pairs=color_pairs,
                raw_data=xyz_data
            )

            datasets.append(dataset)
            print(f"Loaded dataset: {dataset_id} with {len(color_pairs)} pairs")

        self._datasets = datasets
        return datasets

    def _dict_to_metadata(self, metadata_dict: Dict[str, Any]) -> DatasetMetadata:
        """Convert dictionary to DatasetMetadata object"""
        paper = PaperInfo(
            title=metadata_dict['paper']['title'],
            authors=metadata_dict['paper']['authors'],
            year=metadata_dict['paper']['year'],
            citation_key=metadata_dict['paper']['citation_key']
        )

        conditions = ExperimentalConditions(
            medium_type=metadata_dict['conditions']['medium_type'],
            magnitude=metadata_dict['conditions']['magnitude'],
            texture=metadata_dict['conditions']['texture'],
            background_luminance=metadata_dict['conditions']['background_luminance']
        )

        return DatasetMetadata(
            id=metadata_dict['id'],
            name_in_paper=metadata_dict['name_in_paper'],
            paper=paper,
            conditions=conditions,
            sample_size=metadata_dict['sample_size'],
            observer_count=metadata_dict['observer_count'],
            notes_file_path=metadata_dict['notes_file_path']
        )

    def _create_minimal_metadata(self, dataset_id: str, row: np.ndarray) -> DatasetMetadata:
        """Create minimal metadata when not found in registry"""
        # Extract medium type from .mat file if available
        medium_type = 'unknown'
        if row[6].size > 0:
            medium_str = str(row[6][0]).lower()
            if 'surface' in medium_str:
                medium_type = 'surface'
            elif 'display' in medium_str:
                medium_type = 'display'

        paper = PaperInfo(
            title=f"Paper for {dataset_id}",
            authors=["Unknown"],
            year=0,
            citation_key=dataset_id
        )

        conditions = ExperimentalConditions(
            medium_type=medium_type,
            magnitude='unknown',
            texture='unknown',
            background_luminance=None
        )

        return DatasetMetadata(
            id=dataset_id,
            name_in_paper=dataset_id,
            paper=paper,
            conditions=conditions,
            sample_size=0,
            observer_count=None,
            notes_file_path=""
        )

    def _parse_color_pairs(self, xyz_data: np.ndarray) -> List[ColorPair]:
        """
        Parse color pairs from XYZ data array

        Data structure (confirmed):
        - Columns 0-2: XYZw (white point)
        - Columns 3-5: XYZ1 (first color)
        - Columns 6-8: XYZ2 (second color)
        - Column 9: Visual difference
        """
        color_pairs = []

        for row in xyz_data:
            # Extract data according to correct structure
            xyz_w = row[0:3].copy()    # White point
            xyz_1 = row[3:6].copy()    # First color
            xyz_2 = row[6:9].copy()    # Second color
            visual_diff = float(row[9])  # Visual difference

            color_pair = ColorPair(
                xyz_w=xyz_w,
                xyz_1=xyz_1,
                xyz_2=xyz_2,
                visual_difference=visual_diff
            )

            color_pairs.append(color_pair)

        return color_pairs

    def get_dataset(self, dataset_id: str) -> Optional[Dataset]:
        """
        Get a specific dataset by ID

        Parameters
        ----------
        dataset_id : str
            Dataset identifier (e.g., 'BFD-P', 'BIGC-T1-SG')

        Returns
        -------
        Optional[Dataset]
            Dataset object if found, None otherwise
        """
        if self._datasets is None:
            self.load()

        for dataset in self._datasets:
            if dataset.name == dataset_id:
                return dataset

        return None

    def get_all_datasets(self) -> List[Dataset]:
        """
        Get all loaded datasets

        Returns
        -------
        List[Dataset]
            List of all Dataset objects
        """
        if self._datasets is None:
            self.load()

        return self._datasets

    def __repr__(self):
        n_datasets = len(self._datasets) if self._datasets is not None else 0
        return f"DataLoader(n_datasets={n_datasets})"
