#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
YEAR_RE = re.compile(r"\b(19\d{2}|20\d{2})\b")


BAD_TITLE_PATTERNS = (
    "page proof instructions",
    "instructions and queries",
)


@dataclass(frozen=True)
class CrossrefWork:
    doi: str
    title: str
    year: Optional[int]
    authors: Tuple[Tuple[Optional[str], Optional[str]], ...]  # (family, given)


def _http_get_json(url: str, *, user_agent: str, timeout_s: int = 20) -> Dict:
    last_err: Optional[Exception] = None
    for attempt in range(1, 5):
        req = urllib.request.Request(url, headers={"User-Agent": user_agent})
        try:
            with urllib.request.urlopen(req, timeout=timeout_s) as resp:
                return json.load(resp)
        except Exception as e:
            last_err = e
            # Basic backoff (helps for transient 429/5xx).
            time.sleep(min(2.0 * attempt, 6.0))
    raise last_err  # type: ignore[misc]


def _normalize_for_match(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.casefold()
    text = re.sub(r"[\s\-_–—]+", " ", text)
    text = re.sub(r"[^a-z0-9 ]+", "", text)
    return text.strip()


def _similarity(a: str, b: str) -> float:
    na = _normalize_for_match(a)
    nb = _normalize_for_match(b)
    if not na or not nb:
        return 0.0
    return SequenceMatcher(None, na, nb).ratio()


def _pick_year(work: Dict) -> Optional[int]:
    for key in ("issued", "published-print", "published-online", "created"):
        issued = work.get(key, {})
        parts = issued.get("date-parts")
        if isinstance(parts, list) and parts and isinstance(parts[0], list) and parts[0]:
            year = parts[0][0]
            if isinstance(year, int):
                return year
    return None


def _pick_title(work: Dict) -> Optional[str]:
    titles = work.get("title")
    if isinstance(titles, list) and titles:
        if isinstance(titles[0], str):
            return titles[0]
    if isinstance(titles, str):
        return titles
    return None


def _pick_authors(work: Dict) -> Tuple[Tuple[Optional[str], Optional[str]], ...]:
    authors = work.get("author") or []
    out: List[Tuple[Optional[str], Optional[str]]] = []
    if isinstance(authors, list):
        for a in authors:
            if not isinstance(a, dict):
                continue
            out.append((a.get("family"), a.get("given")))
    return tuple(out)


def crossref_by_doi(doi: str, *, user_agent: str) -> Optional[CrossrefWork]:
    doi = doi.strip()
    if not doi:
        return None
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    try:
        data = _http_get_json(url, user_agent=user_agent)
    except Exception:
        return None
    msg = data.get("message")
    if not isinstance(msg, dict):
        return None
    title = _pick_title(msg)
    if not title:
        return None
    year = _pick_year(msg)
    authors = _pick_authors(msg)
    return CrossrefWork(doi=doi, title=title, year=year, authors=authors)


def crossref_by_title(title: str, *, user_agent: str, author_hint: Optional[str] = None) -> Optional[CrossrefWork]:
    title = title.strip()
    if not title:
        return None
    params = {"query.title": title, "rows": 5}
    if author_hint:
        params["query.author"] = author_hint
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    try:
        data = _http_get_json(url, user_agent=user_agent)
    except Exception:
        return None
    msg = data.get("message")
    if not isinstance(msg, dict):
        return None
    items = msg.get("items") or []
    if not isinstance(items, list) or not items:
        return None

    best: Optional[Tuple[float, Dict]] = None
    for item in items:
        if not isinstance(item, dict):
            continue
        it_title = _pick_title(item)
        if not it_title:
            continue
        score = _similarity(title, it_title)
        if best is None or score > best[0]:
            best = (score, item)

    if best is None:
        return None
    score, item = best
    if score < 0.62:
        return None

    doi = item.get("DOI")
    if not isinstance(doi, str) or not doi:
        return None
    it_title = _pick_title(item)
    year = _pick_year(item)
    authors = _pick_authors(item)
    return CrossrefWork(doi=doi, title=it_title or title, year=year, authors=authors)


def extract_doi_from_text(text: str) -> Optional[str]:
    # DOIs often appear in reference lists; prefer early occurrences.
    matches: List[Tuple[int, str]] = []
    for idx, line in enumerate(text.splitlines()):
        m = DOI_RE.search(line)
        if not m:
            continue
        matches.append((idx, m.group(0)))
    if not matches:
        return None

    # Strong preference: first ~80 lines (usually header/abstract).
    for idx, doi in matches:
        if idx < 80:
            return doi
    return None


def extract_h1_title(text: str) -> Optional[str]:
    first: Optional[str] = None
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("# "):
            continue
        title = line[2:].strip()
        # Drop common OCR footnote artifacts like: $ ^{*} $
        title = re.sub(r"\$\s*\^\{[^}]+\}\s*\$", "", title).strip()
        title = re.sub(r"\s+", " ", title)
        if not title:
            continue
        if first is None:
            first = title
        if not is_bad_title(title):
            return title
    return first


def is_bad_title(title: str) -> bool:
    t = title.strip().casefold()
    if not t:
        return True
    if len(t) < 6:
        return True
    for pat in BAD_TITLE_PATTERNS:
        if pat in t:
            return True
    return False


def title_from_filename(path: Path) -> str:
    name = path.name
    if name.lower().endswith(".md"):
        name = name[:-3]
    name = name.replace("_by_PaddleOCR-VL", "")
    if name.lower().endswith(".pdf"):
        name = name[:-4]

    # If it looks like "Author - Title", keep the title part.
    if " - " in name:
        parts = [p.strip() for p in name.split(" - ", 1)]
        if len(parts) == 2 and parts[1]:
            name = parts[1]
    else:
        # Handle "AuthorName-Title" (no spaces) used by some imports.
        m = re.match(r"^[A-Za-z]+(?:\s+[A-Za-z]+){0,2}-(.+)$", name)
        if m:
            tail = m.group(1).strip()
            if tail:
                name = tail

    # Heuristic: strip leading dataset-ish tokens like "BIGC-T1-SG-" / "ZJU-Xu-" etc.
    name = re.sub(r"^[A-Z0-9]{2,}(?:-[A-Za-z0-9]{1,}){1,6}[- ,]+", "", name)
    name = name.replace("_", " ")
    name = re.sub(r"\s+", " ", name).strip()
    return name or path.stem


def author_hint_from_text(text: str) -> Optional[str]:
    lines = [ln.strip() for ln in text.splitlines()[:80]]
    for ln in lines:
        if not ln:
            continue
        if ln.startswith("#"):
            continue
        lowered = ln.casefold()
        if any(k in ln for k in ("University", "Laboratory", "Department", "School", "@")):
            continue
        if any(k in lowered for k in ("journal", "title", "received", "abstract", "doi", "http")):
            continue
        if lowered.startswith("the ") or "society" in lowered:
            continue
        if any(ch in ln for ch in (":", "&", "(", ")")):
            continue
        # Very rough: keep short-ish lines that look like a name.
        ln_clean = re.sub(r"\$[^$]*\$", "", ln).strip()
        if 3 <= len(ln_clean) <= 60 and re.search(r"[A-Za-z]", ln_clean):
            # Use last token as family name hint.
            tokens = re.split(r"[\s,]+", ln_clean)
            tokens = [t for t in tokens if t and t not in {"and", "AND"}]
            if tokens:
                family = tokens[-1]
                family = family.strip(".")
                if (
                    family
                    and family[0].isupper()
                    and re.fullmatch(r"[A-Za-z][A-Za-z'\-]+", family)
                ):
                    return family
    return None


def sanitize_filename_component(text: str, *, max_len: int = 180) -> str:
    text = unicodedata.normalize("NFKC", text).strip()
    text = re.sub(r"\s+", " ", text)
    # Avoid characters that are annoying across platforms / shells.
    text = text.replace("/", "-")
    text = text.replace(":", " -")
    text = text.replace("\\", "-")
    text = text.replace("\0", "")
    text = text.replace("\"", "")
    text = text.replace("’", "'")
    text = text.replace("“", "")
    text = text.replace("”", "")
    text = text.replace("?", "")
    text = text.replace("*", "")
    text = text.replace("<", "")
    text = text.replace(">", "")
    text = text.replace("|", "-")
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > max_len:
        text = text[: max_len - 1].rstrip()
    return text


def author_label(work: CrossrefWork) -> str:
    families = [a[0] for a in work.authors if a and a[0]]
    if not families:
        return "Unknown"
    if len(families) == 1:
        return families[0]
    if len(families) == 2:
        return f"{families[0]} & {families[1]}"
    return f"{families[0]} et al."


def build_new_filename(work: CrossrefWork) -> str:
    year = str(work.year) if work.year else "n.d."
    authors = sanitize_filename_component(author_label(work), max_len=60)
    title = sanitize_filename_component(work.title, max_len=140)
    return f"{authors} ({year}) - {title}.md"


def unique_path(target: Path) -> Path:
    if not target.exists():
        return target
    stem = target.stem
    suffix = target.suffix
    for i in range(2, 1000):
        candidate = target.with_name(f"{stem} ({i}){suffix}")
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"Unable to create unique filename near: {target}")


def main(argv: Sequence[str]) -> int:
    parser = argparse.ArgumentParser(description="Rename papers/*.md to an APA-like filename via Crossref.")
    parser.add_argument("--papers-dir", default="papers", help="Directory containing paper markdown files.")
    parser.add_argument("--apply", action="store_true", help="Perform the renames (default is dry-run).")
    parser.add_argument("--json", action="store_true", help="Output mapping as JSON.")
    args = parser.parse_args(argv)

    user_agent = "Meta-Color/0.1 (mailto:example@example.com)"

    papers_dir = Path(args.papers_dir)
    paths = sorted([p for p in papers_dir.glob("*.md") if not p.name.startswith(".")])
    if not paths:
        print(f"No .md files found in {papers_dir}")
        return 1

    mappings: List[Tuple[Path, Path, Optional[str], Optional[str]]] = []  # (old, new, doi, note)

    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        doi = extract_doi_from_text(text)

        # Try Crossref by DOI first.
        work: Optional[CrossrefWork] = None
        note: Optional[str] = None
        if doi:
            work = crossref_by_doi(doi, user_agent=user_agent)
        if work is None:
            h1 = extract_h1_title(text)
            candidate_title = h1 if h1 and not is_bad_title(h1) else title_from_filename(path)
            author_hint = author_hint_from_text(text)
            work = crossref_by_title(candidate_title, user_agent=user_agent, author_hint=author_hint)
            if work is None and author_hint:
                work = crossref_by_title(candidate_title, user_agent=user_agent, author_hint=None)
            if work is None:
                # Last fallback: use local title + year.
                year_m = YEAR_RE.search(path.name) or YEAR_RE.search(text)
                year = int(year_m.group(0)) if year_m else None
                title = candidate_title
                work = CrossrefWork(doi="n/a", title=title, year=year, authors=tuple())
                note = "fallback_local"

        new_name = build_new_filename(work)
        new_path = unique_path(path.with_name(new_name))
        mappings.append((path, new_path, work.doi, note))

    if args.json:
        out = [
            {
                "from": str(old),
                "to": str(new),
                "doi": doi,
                "note": note,
            }
            for old, new, doi, note in mappings
        ]
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        for old, new, doi, note in mappings:
            suffix = []
            if doi:
                suffix.append(f"doi={doi}")
            if note:
                suffix.append(note)
            extra = f"  [{' | '.join(suffix)}]" if suffix else ""
            print(f"{old.name} -> {new.name}{extra}")

    if not args.apply:
        return 0

    # Apply renames.
    for old, new, _, _ in mappings:
        if old == new:
            continue
        old.rename(new)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
