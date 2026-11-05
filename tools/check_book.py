#!/usr/bin/env python3
"""
check_book.py -- automated structural QA for one or more books.

Checks everything a machine can check, so that the human/agent QA pass can
concentrate on what a machine cannot: typography correctness, character
consistency, mood, and story flow.

Usage
-----
    python tools/check_book.py 10_The_Little_Library_of_Lost_Things
    python tools/check_book.py --all
    python tools/check_book.py --all --expect 20

Exit code 0 if every checked book passes, 1 otherwise.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys

# Keys every book must carry, whichever metadata schema it was written with.
REQUIRED_METADATA_KEYS = [
    "title", "author", "language", "moral_lesson", "page_count", "main_characters",
]
# Two schemas exist in the series and both are accepted:
#   schema A (books 01-10): creator_credit / format{} / page_structure{}
#   schema B (books 11-15): creator_publisher / resolution / aspect_ratio /
#                           orientation / color_model / book_structure


def metadata_dimensions(meta: dict) -> str:
    """Return the page dimensions declared by either schema, as 'WxH'."""
    fmt = meta.get("format") or {}
    declared = fmt.get("pixel_dimensions")
    if not declared:
        declared = meta.get("resolution", "")
    digits = str(declared).replace("×", "x")
    token = ""
    for chunk in digits.split():
        if "x" in chunk:
            token = chunk
            break
    return token


def natural_page_key(path: str) -> int:
    digits = "".join(ch for ch in os.path.basename(path) if ch.isdigit())
    return int(digits) if digits else 0


def check_book(book_dir: str, expect: int, width: int, height: int) -> tuple[bool, list[str]]:
    from PIL import Image

    problems: list[str] = []

    pages = sorted(glob.glob(os.path.join(book_dir, "illustrations", "page_*.png")),
                   key=natural_page_key)
    if not pages:
        return False, ["no illustrations/page_*.png found"]
    numbers = [natural_page_key(p) for p in pages]
    missing = [n for n in range(1, max(numbers) + 1) if n not in numbers]
    if missing:
        problems.append(f"missing page numbers {missing}")
    if expect and len(pages) != expect:
        problems.append(f"{len(pages)} page images, expected {expect}")

    bad = []
    for p in pages:
        im = Image.open(p)
        if im.size != (width, height):
            bad.append(f"{os.path.basename(p)} size {im.size}")
        elif im.mode != "RGB":
            bad.append(f"{os.path.basename(p)} mode {im.mode}")
    if bad:
        problems.append("bad images: " + "; ".join(bad))

    pdfs = glob.glob(os.path.join(book_dir, "pdf", "*.pdf"))
    if not pdfs:
        problems.append("no PDF in pdf/")
    else:
        try:
            from pypdf import PdfReader
            reader = PdfReader(pdfs[0])
            boxes = {(round(float(p.mediabox.width)), round(float(p.mediabox.height)))
                     for p in reader.pages}
            if len(reader.pages) != len(pages):
                problems.append(f"PDF has {len(reader.pages)} pages, {len(pages)} images")
            if boxes != {(width, height)}:
                problems.append(f"PDF page sizes {boxes}")
        except Exception as exc:  # noqa: BLE001
            problems.append(f"PDF unreadable: {exc}")

    meta_path = os.path.join(book_dir, "metadata", "metadata.json")
    if not os.path.exists(meta_path):
        problems.append("missing metadata/metadata.json")
    else:
        try:
            meta = json.load(open(meta_path, encoding="utf-8"))
            lack = [k for k in REQUIRED_METADATA_KEYS if k not in meta]
            if lack:
                problems.append(f"metadata missing keys {lack}")
            if meta.get("page_count") not in (None, len(pages)):
                problems.append(f"metadata page_count {meta.get('page_count')} != {len(pages)}")
            declared = metadata_dimensions(meta)
            if declared and declared != f"{width}x{height}":
                problems.append(f"metadata declares page size {declared!r}")
            if meta.get("language") != "English":
                problems.append(f"metadata language {meta.get('language')!r}")
        except Exception as exc:  # noqa: BLE001
            problems.append(f"metadata unreadable: {exc}")

    for name in ("manuscript/story.txt", "production_report.md"):
        if not os.path.exists(os.path.join(book_dir, name)):
            problems.append(f"missing {name}")

    return (not problems), problems


def main() -> int:
    ap = argparse.ArgumentParser(description="Structural QA for the book series.")
    ap.add_argument("book_dirs", nargs="*", help="book folders")
    ap.add_argument("--all", action="store_true", help="check every NN_Title folder")
    ap.add_argument("--expect", type=int, default=20)
    ap.add_argument("--width", type=int, default=768)
    ap.add_argument("--height", type=int, default=1376)
    ap.add_argument("--quiet", action="store_true", help="only print failures")
    args = ap.parse_args()

    targets = list(args.book_dirs)
    if args.all:
        targets += sorted(d for d in glob.glob("[0-9][0-9]_*") if os.path.isdir(d))
    if not targets:
        ap.error("give at least one book folder, or --all")

    failures = 0
    for book in targets:
        ok, problems = check_book(book, args.expect, args.width, args.height)
        if ok:
            if not args.quiet:
                print(f"PASS  {book}")
        else:
            failures += 1
            print(f"FAIL  {book}")
            for p in problems:
                print(f"        - {p}")

    print(f"\n{len(targets) - failures}/{len(targets)} books passed all structural checks")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
