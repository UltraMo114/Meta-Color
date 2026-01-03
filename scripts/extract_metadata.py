"""
Extract metadata from papers and create metadata_registry.json
"""
import json
import os
import re
from pathlib import Path

# Add parent directory to path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.schema import DatasetMetadata, PaperInfo, ExperimentalConditions


def extract_metadata_from_papers():
    """Extract metadata from markdown files in papers/ directory"""

    # Dataset mapping based on dataset_paper_mapping.md
    # Format: dataset_id -> (paper_file, name_in_paper, medium_type, magnitude, texture)
    dataset_mapping = {
        # SCDs Group (Small Colour Difference - Surface)
        'BFD-P': ('BFD-P-Luo-1986-Chromaticity discrimination ellipses.md',
                  'BFD-P', 'surface', 'threshold', 'glossy'),
        'Leeds': ('Leeds-Luo-Rigg-1987-BFD colour-difference formula.md' if os.path.exists('papers/Leeds-Luo-Rigg-1987-BFD colour-difference formula.md') else 'BFD-P-Luo-1986-Chromaticity discrimination ellipses.md',
                  'Leeds/BFD', 'surface', 'threshold', 'matte'),
        'Witt': ('Witt-Witt-1999-Geometric relations small differences.md' if os.path.exists('papers/Witt-Witt-1999-Geometric relations small differences.md') else None,
                 'Witt', 'surface', 'threshold', 'glossy'),
        'BIGC-T1-SG': ('BIGC-T1-SG-Huang-2012-Evaluation threshold differences.md',
                       'BIGC-T1-SG', 'surface', 'threshold', 'semi-gloss'),
        'BIGC-T2-M': ('BIGC-T2-M-Huang-2010-Small difference different gloss.md',
                      'BIGC-T2-M', 'surface', 'suprathreshold-small', 'matte'),
        'BIGC-T2-SG': ('BIGC-T2-SG-Huang-2010-Small difference different gloss.md',
                       'BIGC-T2-SG', 'surface', 'suprathreshold-small', 'semi-gloss'),
        'BIGC-T2-G': ('BIGC-T2-G-Huang-2010-Small difference different gloss.md',
                      'BIGC-T2-G', 'surface', 'suprathreshold-small', 'glossy'),
        'BIGC-S-SG': ('BIGC-S-SG-Huang-2011-Testing uniform colour spaces.md' if os.path.exists('papers/BIGC-S-SG-Huang-2011-Testing uniform colour spaces.md') else
                      'BIGC-S-SG-Huang-2012-Testing uniform colour spaces.md',
                      'BIGC-S-SG', 'surface', 'suprathreshold-small', 'semi-gloss'),
        'HDR-Surface': ('HDR-Surface-Xu-2019-Wide range luminance levels.md' if os.path.exists('papers/HDR-Surface-Xu-2019-Wide range luminance levels.md') else None,
                        'HDR-Surface', 'surface', 'suprathreshold-small', 'unknown'),

        # SCDd Group (Small Colour Difference - Display)
        'HDR-Display': ('HDR-Display-Xu-2019-Wide range luminance levels.md' if os.path.exists('papers/HDR-Display-Xu-2019-Wide range luminance levels.md') else None,
                        'HDR-Display', 'display', 'suprathreshold-small', 'unknown'),
        'WCG': ('WCG-Xu-2021-Testing uniform spaces wide gamut.md' if os.path.exists('papers/WCG-Xu-2021-Testing uniform spaces wide gamut.md') else None,
                'WCG', 'display', 'suprathreshold-small', 'unknown'),
        'Parametric-NS': ('Parametric-NS-Xu-2022-Parametric effects evaluation.md' if os.path.exists('papers/Parametric-NS-Xu-2022-Parametric effects evaluation.md') else None,
                          'Parametric-NS', 'display', 'suprathreshold-small', 'unknown'),
        'Parametric-S': ('Parametric-S-Xu-2022-Parametric effects evaluation.md' if os.path.exists('papers/Parametric-S-Xu-2022-Parametric effects evaluation.md') else None,
                         'Parametric-S', 'display', 'suprathreshold-small', 'unknown'),
        'Liang': ('Liang-Liang-2018-Evaluation using display colours.md' if os.path.exists('papers/Liang-Liang-2018-Evaluation using display colours.md') else None,
                  'Liang', 'display', 'suprathreshold-small', 'unknown'),
        'Cui-NS': ('Cui-Cui-2001-Evaluation using CRT colours Part I.md',
                   'Cui-NS', 'display', 'suprathreshold-small', 'unknown'),
        'Cui-S-All': ('Cui-Cui-2001-Evaluation using CRT colours Part I.md',
                      'Cui-S-All', 'display', 'suprathreshold-small', 'unknown'),

        # LCD Group (Large Colour Difference)
        'Pointer': ('Pointer-Pointer-1997-Visual scaling large differences.md' if os.path.exists('papers/Pointer-Pointer-1997-Visual scaling large differences.md') else None,
                    'Pointer', 'surface', 'suprathreshold-large', 'unknown'),
        'Guan-LCD': ('Guan-LCD-Guan-1999-Formula large differences.md' if os.path.exists('papers/Guan-LCD-Guan-1999-Formula large differences.md') else None,
                     'Guan-LCD', 'surface', 'suprathreshold-large', 'unknown'),
        'OSA': ('OSA-MacAdam-1974-Uniform color scales.md' if os.path.exists('papers/OSA-MacAdam-1974-Uniform color scales.md') else None,
                'OSA', 'surface', 'suprathreshold-large', 'unknown'),
        'Munsell': ('Munsell-Newhall-1940-OSA Munsell spacing.md' if os.path.exists('papers/Munsell-Newhall-1940-OSA Munsell spacing.md') else None,
                    'Munsell', 'surface', 'suprathreshold-large', 'matte'),
    }

    papers_dir = Path('papers')
    metadata_list = []

    for dataset_id, (paper_file, name_in_paper, medium_type, magnitude, texture) in dataset_mapping.items():
        if paper_file is None:
            print(f"Warning: No paper file found for {dataset_id}, skipping...")
            continue

        paper_path = papers_dir / paper_file

        if not paper_path.exists():
            print(f"Warning: Paper file not found: {paper_path}, skipping...")
            continue

        # Extract paper info from filename
        # Format: DatasetName-Author-Year-Title.md
        parts = paper_file.replace('.md', '').split('-')

        # Try to extract year from filename
        year = None
        authors = []
        title = ""

        # Parse filename to extract basic info
        for part in parts:
            if part.isdigit() and len(part) == 4:
                year = int(part)
                break

        # Read paper content for more details
        try:
            with open(paper_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Try to extract title (usually in first heading)
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if title_match:
                title = title_match.group(1).strip()

            # Try to extract authors - look for common patterns
            # This is tricky as papers have different formats
            # For now, use filename
            if len(parts) >= 2:
                author_part = parts[1] if len(parts) > 1 else "Unknown"
                # Handle cases like "Luo-Rigg" or single author
                authors = [a.strip() for a in author_part.replace('_', ' ').split() if a]

        except Exception as e:
            print(f"Error reading {paper_path}: {e}")
            continue

        # Create PaperInfo
        paper_info = PaperInfo(
            title=title if title else f"Paper for {dataset_id}",
            authors=authors if authors else ["Unknown"],
            year=year if year else 0,
            citation_key=dataset_id
        )

        # Create ExperimentalConditions
        conditions = ExperimentalConditions(
            medium_type=medium_type,
            magnitude=magnitude,
            texture=texture,
            background_luminance=None  # Not available in all papers
        )

        # Create DatasetMetadata
        # Note: sample_size and observer_count would need to be extracted from paper content
        # For now, setting them to placeholder values
        metadata = DatasetMetadata(
            id=dataset_id,
            name_in_paper=name_in_paper,
            paper=paper_info,
            conditions=conditions,
            sample_size=0,  # To be filled from .mat file later
            observer_count=None,  # Not available in all papers
            notes_file_path=str(paper_path)
        )

        metadata_list.append(metadata)
        print(f"Extracted metadata for {dataset_id}")

    return metadata_list


def save_metadata_registry(metadata_list, output_file='data/metadata_registry.json'):
    """Save metadata list to JSON file"""

    # Convert dataclass objects to dictionaries
    metadata_dicts = []
    for metadata in metadata_list:
        metadata_dict = {
            'id': metadata.id,
            'name_in_paper': metadata.name_in_paper,
            'paper': {
                'title': metadata.paper.title,
                'authors': metadata.paper.authors,
                'year': metadata.paper.year,
                'citation_key': metadata.paper.citation_key
            },
            'conditions': {
                'medium_type': metadata.conditions.medium_type,
                'magnitude': metadata.conditions.magnitude,
                'texture': metadata.conditions.texture,
                'background_luminance': metadata.conditions.background_luminance
            },
            'sample_size': metadata.sample_size,
            'observer_count': metadata.observer_count,
            'notes_file_path': metadata.notes_file_path
        }
        metadata_dicts.append(metadata_dict)

    # Save to JSON
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(metadata_dicts, f, indent=2, ensure_ascii=False)

    print(f"\nSaved {len(metadata_dicts)} dataset metadata entries to {output_file}")


if __name__ == '__main__':
    metadata_list = extract_metadata_from_papers()
    save_metadata_registry(metadata_list)
