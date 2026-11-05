#!/usr/bin/env python3
"""
qa_crop.py -- visual QA helpers (read-only; never modifies book pages).

Two modes:

1) Crop and enlarge a region of one page, so the embedded lettering can be
   read at a glance during QA:

       python tools/qa_crop.py illustrations/page_11.png \
              --box 0,900,768,1376 --scale 2 --out /tmp/p11_text.png

   Without --box it crops the bottom third, which is where the story text
   always sits. The crop is written to /tmp, never next to the book.

2) Build a contact sheet of a whole book (5 columns x 4 rows) to review all
   20 pages at once for consistency, colour drift, and page-number mistakes:

       python tools/qa_crop.py --sheet 10_The_Little_Library_of_Lost_Things \
              --out /tmp/book10_sheet.png
"""

from __future__ import annotations

import argparse
import glob
import os


def natural_page_key(path: str) -> int:
    digits = "".join(ch for ch in os.path.basename(path) if ch.isdigit())
    return int(digits) if digits else 0


def crop_page(page: str, box: str | None, scale: float, out: str) -> None:
    from PIL import Image

    im = Image.open(page).convert("RGB")
    if box:
        parts = [int(float(v)) for v in box.split(",")]
        if len(parts) != 4:
            raise SystemExit("--box needs four values: left,top,right,bottom")
        region = im.crop(tuple(parts))
    else:
        w, h = im.size
        region = im.crop((0, int(h * 0.62), w, h))

    if scale != 1:
        region = region.resize(
            (int(region.width * scale), int(region.height * scale)), Image.LANCZOS
        )
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    region.save(out)
    print(f"{page} -> {out} ({region.width}x{region.height})")


def contact_sheet(book_dir: str, out: str, cols: int, thumb_w: int) -> None:
    from PIL import Image, ImageDraw

    pages = sorted(glob.glob(os.path.join(book_dir, "illustrations", "page_*.png")),
                   key=natural_page_key)
    if not pages:
        raise SystemExit(f"no pages in {book_dir}/illustrations")

    first = Image.open(pages[0])
    ratio = first.height / first.width
    thumb_h = int(thumb_w * ratio)
    pad = 10
    rows = (len(pages) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (thumb_w + pad) + pad,
                              rows * (thumb_h + pad + 22) + pad), (24, 24, 28))
    draw = ImageDraw.Draw(sheet)

    for i, page in enumerate(pages):
        im = Image.open(page).convert("RGB").resize((thumb_w, thumb_h), Image.LANCZOS)
        c, r = i % cols, i // cols
        x = pad + c * (thumb_w + pad)
        y = pad + r * (thumb_h + pad + 22)
        sheet.paste(im, (x, y))
        draw.text((x + 4, y + thumb_h + 4), os.path.basename(page), fill=(230, 230, 230))

    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    sheet.save(out)
    print(f"{len(pages)} pages -> {out} ({sheet.width}x{sheet.height})")


def main() -> None:
    ap = argparse.ArgumentParser(description="Visual QA crops and contact sheets.")
    ap.add_argument("page", nargs="?", help="path to one page image")
    ap.add_argument("--box", default=None, help="crop box left,top,right,bottom in px")
    ap.add_argument("--scale", type=float, default=2.0, help="enlargement factor (default 2)")
    ap.add_argument("--sheet", metavar="BOOK_DIR", default=None, help="build a contact sheet for a book")
    ap.add_argument("--cols", type=int, default=5)
    ap.add_argument("--thumb-w", type=int, default=240)
    ap.add_argument("--out", default=None, help="output path (default under /tmp)")
    args = ap.parse_args()

    if args.sheet:
        out = args.out or f"/tmp/{os.path.basename(os.path.abspath(args.sheet))}_sheet.png"
        contact_sheet(args.sheet, out, args.cols, args.thumb_w)
    elif args.page:
        out = args.out or f"/tmp/{os.path.splitext(os.path.basename(args.page))[0]}_crop.png"
        crop_page(args.page, args.box, args.scale, out)
    else:
        ap.error("give a page image, or --sheet BOOK_DIR")


if __name__ == "__main__":
    main()
