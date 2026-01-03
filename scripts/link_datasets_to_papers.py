#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
from scipy.io import loadmat


@dataclass(frozen=True)
class MatchResult:
    dataset: str
    status: str  # strong | token | weak | missing
    match_token: Optional[str]
    papers: Tuple[str, ...]


ALNUM_BOUNDARY_TEMPLATE = r"(?<![A-Za-z0-9]){token}(?![A-Za-z0-9])"
KNOWN_SUFFIXES = (
    "-LCD",
    "-Display",
    "-Surface",
    "-NS",
    "-S",
    "-All",
)


@dataclass(frozen=True)
class PaperRecord:
    display: str  # what we print in the report (current filename cleaned)
    match_text: str  # what we match against (stable identifier)


def _to_python_scalar(value):
    if isinstance(value, np.ndarray):
        if value.size == 0:
            return None
        if value.size == 1:
            return value.item()
    return value


def _to_string(value) -> Optional[str]:
    value = _to_python_scalar(value)
    if value is None:
        return None
    if isinstance(value, (bytes, np.bytes_)):
        return value.decode("utf-8", errors="replace")
    if isinstance(value, (str, np.str_)):
        return str(value)
    return None


def _non_dunder_keys(mat: Dict) -> List[str]:
    return sorted([k for k in mat.keys() if not k.startswith("__")])


def _find_dataset_column(arr: np.ndarray) -> int:
    if arr.ndim != 2:
        raise ValueError(f"Expected 2D array, got shape={getattr(arr, 'shape', None)}")
    rows, cols = arr.shape
    if rows < 2:
        raise ValueError(f"Expected >=2 rows (header + data), got rows={rows}")

    # Prefer explicit header match in the first row.
    for j in range(cols):
        header = _to_string(arr[0, j])
        if header and header.strip().lower() == "dataset":
            return j

    # Fallback: pick the column with most string-like entries in the first few rows.
    sample_rows = min(rows, 6)
    best_j = 0
    best_score = -1
    for j in range(cols):
        score = 0
        for i in range(sample_rows):
            if _to_string(arr[i, j]) is not None:
                score += 1
        if score > best_score:
            best_score = score
            best_j = j

    return best_j


def extract_source_datasets(mat_path: Path) -> Tuple[List[str], List[str], str]:
    if not mat_path.exists():
        raise FileNotFoundError(f"MAT file not found: {mat_path}")

    mat = loadmat(str(mat_path))
    keys = _non_dunder_keys(mat)
    if not keys:
        raise ValueError("No non-dunder keys found in MAT file.")

    # Prefer a key that looks like it contains the dataset table, otherwise take the first key.
    chosen_key = next((k for k in keys if "dataset" in k.lower()), keys[0])
    raw = mat[chosen_key]
    if not isinstance(raw, np.ndarray):
        raise ValueError(f"MAT value for {chosen_key!r} is not an ndarray: {type(raw)}")

    if raw.dtype != object:
        raise ValueError(
            f"Expected object array for {chosen_key!r}; got dtype={raw.dtype}, shape={raw.shape}"
        )

    dataset_col = _find_dataset_column(raw)

    datasets: List[str] = []
    for i in range(1, raw.shape[0]):  # skip header row
        name = _to_string(raw[i, dataset_col])
        if not name:
            continue
        name = name.strip()
        if not name or name.lower() == "dataset":
            continue
        datasets.append(name)

    # Preserve order but drop duplicates if any.
    seen = set()
    deduped: List[str] = []
    for name in datasets:
        if name in seen:
            continue
        seen.add(name)
        deduped.append(name)

    return deduped, keys, chosen_key


def scan_existing_papers(papers_dir: Path) -> List[str]:
    if not papers_dir.exists():
        raise FileNotFoundError(f"Papers directory not found: {papers_dir}")

    names: List[str] = []
    for path in sorted(papers_dir.glob("*.md")):
        if path.name.startswith("."):
            continue
        base = path.name
        if base.lower().endswith(".md"):
            base = base[:-3]
        base = base.replace("_by_PaddleOCR-VL", "")
        if base.lower().endswith(".pdf"):
            base = base[:-4]
        names.append(base.strip())
    return names


def _git_available() -> bool:
    try:
        proc = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            capture_output=True,
            text=True,
            check=False,
        )
        return proc.returncode == 0 and proc.stdout.strip() == "true"
    except Exception:
        return False


def _git_head_paper_blob_map(papers_dir: Path) -> Dict[str, List[str]]:
    # Maps blob sha -> list of historical filenames (base name only) under papers/.
    proc = subprocess.run(
        ["git", "ls-tree", "-r", "HEAD", "--", str(papers_dir)],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return {}
    mapping: Dict[str, List[str]] = {}
    for line in proc.stdout.splitlines():
        # Format: <mode> <type> <sha>\t<path>
        parts = line.split("\t", 1)
        if len(parts) != 2:
            continue
        meta, file_path = parts
        meta_parts = meta.split()
        if len(meta_parts) < 3:
            continue
        sha = meta_parts[2]
        base = Path(file_path).name
        mapping.setdefault(sha, []).append(base)
    return mapping


def _git_hash_object(path: Path) -> Optional[str]:
    proc = subprocess.run(
        ["git", "hash-object", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return None
    sha = proc.stdout.strip()
    return sha or None


def scan_paper_records(papers_dir: Path) -> List[PaperRecord]:
    """
    Returns PaperRecord items where:
      - display: cleaned current filename (APA names after renaming)
      - match_text: cleaned stable identifier derived from git HEAD filename when possible

    This keeps dataset↔paper matching stable even if the user renames files.
    """
    if not papers_dir.exists():
        raise FileNotFoundError(f"Papers directory not found: {papers_dir}")

    head_map: Dict[str, List[str]] = {}
    use_git = _git_available()
    if use_git:
        head_map = _git_head_paper_blob_map(papers_dir)

    def clean(name: str) -> str:
        base = name
        if base.lower().endswith(".md"):
            base = base[:-3]
        base = base.replace("_by_PaddleOCR-VL", "")
        if base.lower().endswith(".pdf"):
            base = base[:-4]
        return base.strip()

    records: List[PaperRecord] = []
    for path in sorted(papers_dir.glob("*.md")):
        if path.name.startswith("."):
            continue

        display = clean(path.name)
        match_name = path.name
        if use_git:
            sha = _git_hash_object(path)
            if sha and sha in head_map and len(head_map[sha]) == 1:
                match_name = head_map[sha][0]

        match_text = clean(match_name)
        records.append(PaperRecord(display=display, match_text=match_text))

    return records


def _boundary_hits(token: str, papers: Sequence[str]) -> List[str]:
    pat = re.compile(ALNUM_BOUNDARY_TEMPLATE.format(token=re.escape(token)), re.IGNORECASE)
    return [p for p in papers if pat.search(p)]


def _token_hits(dataset: str, papers: Sequence[str]) -> List[str]:
    segments = [s for s in re.split(r"[^A-Za-z0-9]+", dataset) if s]
    if len(segments) < 2:
        return []
    pats = [
        re.compile(ALNUM_BOUNDARY_TEMPLATE.format(token=re.escape(seg)), re.IGNORECASE)
        for seg in segments
    ]
    hits: List[str] = []
    for paper in papers:
        if all(pat.search(paper) for pat in pats):
            hits.append(paper)
    return hits


def _strip_known_suffixes(dataset: str) -> str:
    candidate = dataset
    changed = True
    while changed:
        changed = False
        for suffix in KNOWN_SUFFIXES:
            if candidate.endswith(suffix) and len(candidate) > len(suffix):
                candidate = candidate[: -len(suffix)]
                changed = True
                break
    return candidate


def match_datasets_to_papers(source_datasets: Sequence[str], papers: Sequence[str]) -> List[MatchResult]:
    results: List[MatchResult] = []
    for dataset in source_datasets:
        hits = _boundary_hits(dataset, papers)
        if hits:
            results.append(MatchResult(dataset=dataset, status="strong", match_token=None, papers=tuple(hits)))
            continue

        hits = _token_hits(dataset, papers)
        if hits:
            results.append(MatchResult(dataset=dataset, status="token", match_token=None, papers=tuple(hits)))
            continue

        reduced = _strip_known_suffixes(dataset)
        if reduced != dataset:
            hits = _boundary_hits(reduced, papers)
            if hits:
                results.append(
                    MatchResult(dataset=dataset, status="weak", match_token=reduced, papers=tuple(hits))
                )
                continue

        results.append(MatchResult(dataset=dataset, status="missing", match_token=None, papers=tuple()))
    return results


def _count_by_status(results: Sequence[MatchResult]) -> Dict[str, int]:
    counts: Dict[str, int] = {"strong": 0, "token": 0, "weak": 0, "missing": 0}
    for r in results:
        counts[r.status] = counts.get(r.status, 0) + 1
    return counts


def _render_markdown_report(
    mat_path: Path,
    papers_dir: Path,
    source_datasets: Sequence[str],
    papers: Sequence[str],
    results: Sequence[MatchResult],
    *,
    mat_keys: Sequence[str],
    chosen_mat_key: str,
) -> str:
    counts = _count_by_status(results)
    missing = [r.dataset for r in results if r.status == "missing"]

    lines: List[str] = []
    lines.append("### Analysis Result")
    lines.append(f"- **MAT File**: `{mat_path.as_posix()}`")
    lines.append(f"- **MAT Keys**: {', '.join(f'`{k}`' for k in mat_keys)}")
    lines.append(f"- **Chosen Key**: `{chosen_mat_key}`")
    lines.append(f"- **Total Datasets in MAT**: {len(source_datasets)}")
    lines.append(f"- **Total Papers Found**: {len(papers)}")
    lines.append(f"- **Strong Aligned**: {counts.get('strong', 0)}")
    lines.append(f"- **Token Aligned**: {counts.get('token', 0)}")
    lines.append(f"- **Weak Aligned**: {counts.get('weak', 0)}")
    lines.append(f"- **Missing**: {counts.get('missing', 0)}")
    lines.append("")

    lines.append("#### Dataset ↔ Paper Links")
    lines.append("| Dataset | Status | Match Token | Papers |")
    lines.append("|---|---|---|---|")
    for r in results:
        match_token = r.match_token or ""
        papers_joined = "; ".join(r.papers)
        lines.append(f"| {r.dataset} | {r.status} | {match_token} | {papers_joined} |")
    lines.append("")

    lines.append("#### ⚠️ Missing Datasets (Need to find papers)")
    if missing:
        for i, name in enumerate(missing, start=1):
            lines.append(f"{i}. {name}")
    else:
        lines.append("- (none)")
    lines.append("")

    lines.append("#### Notes")
    lines.append("- `strong`: exact dataset token found (alphanumeric boundary match).")
    lines.append("- `token`: all alphanumeric segments found as boundary tokens (e.g., `BIGC`, `T2`, `SG`).")
    lines.append("- `weak`: matched after stripping a known suffix (e.g., `-LCD`, `-Display`, `-Surface`, `-NS`, `-S`, `-All`).")
    return "\n".join(lines)


def main(argv: Sequence[str]) -> int:
    mat_path = Path("dataset_comprehensive.mat")
    papers_dir = Path("papers")

    print("== Phase 1: Data Source Introspection ==")
    source_datasets, mat_keys, chosen_mat_key = extract_source_datasets(mat_path)
    print("MAT keys:", mat_keys)
    print("Extracted datasets:", len(source_datasets))
    print("Examples:", source_datasets[:5])
    print()

    print("== Phase 2: Knowledge Base Scanning ==")
    paper_records = scan_paper_records(papers_dir)
    papers_match = [p.match_text for p in paper_records]
    papers_display = [p.display for p in paper_records]
    print("Papers found:", len(paper_records))
    print()

    print("== Phase 3: Alignment & Gap Analysis ==")
    # Match against stable identifiers, report current filenames.
    # We do this by projecting the match results back onto display names.
    display_by_match: Dict[str, str] = {}
    for rec in paper_records:
        # If two files share the same match_text, keep the first; it's still informative.
        display_by_match.setdefault(rec.match_text, rec.display)

    raw_results = match_datasets_to_papers(source_datasets, papers_match)
    results: List[MatchResult] = []
    for r in raw_results:
        mapped = tuple(display_by_match.get(h, h) for h in r.papers)
        results.append(MatchResult(dataset=r.dataset, status=r.status, match_token=r.match_token, papers=mapped))
    counts = _count_by_status(results)
    print("Counts:", counts)
    print()

    print("== Phase 4: Final Reporting ==")
    report = _render_markdown_report(
        mat_path,
        papers_dir,
        source_datasets,
        papers_display,
        results,
        mat_keys=mat_keys,
        chosen_mat_key=chosen_mat_key,
    )
    print(report)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
