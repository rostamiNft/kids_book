# Children's Book Collection

**Creator:** Hamidreza Rostami
**Language:** English
**Reader age:** 3–9 years
**Series standard:** 20 pages per book — 1 front cover + 18 story pages + 1 back cover —
portrait 9:16, **768 × 1376 px, RGB, one image per PDF page, no double-page spreads.**

All artwork *and all text* (title, story, blurb, page copy, credit) is generated
as AI imagery and painted directly into each page image. Program code is used for
one thing only: stitching the finished page images into a PDF.

---

## Status

| # | Title | Pages | Format | Status |
|---|-------|-------|--------|--------|
| 01 | The Little Cloud Who Wanted to Rain | 20 | 768×1376 portrait | ✅ rebuilt |
| 02 | Luna and the Moonlight Garden | 20 | 768×1376 portrait | ✅ rebuilt |
| 03 | The Robot Who Wanted to Dance | 20 | 768×1376 portrait | ✅ rebuilt |
| 04 | The Day the Colors Ran Away | 20 | 768×1376 portrait | ✅ rebuilt |
| 05 | Captain Whiskers and the Great Yarn Adventure | 20 | 768×1376 portrait | ✅ rebuilt |
| 06 | The Tiny Giant | 20 | 768×1376 portrait | ✅ rebuilt |
| 07 | The Quiet Little Drum | 20 | 768×1376 portrait | ✅ rebuilt |
| 08 | The Last Leaf of Autumn | 20 | 768×1376 portrait | ✅ rebuilt |
| 09 | The Boy Who Painted Dreams | 20 | 768×1376 portrait | ✅ rebuilt |
| 10 | The Little Library of Lost Things | 20 | 768×1376 portrait | ✅ rebuilt |
| 11 | The Little Star Who Lost Her Twinkle | 14 | 1376×768 landscape | ⏳ legacy, awaiting rebuild |
| 12 | The Little Moon Who Wanted to Shine | 20 | 1376×768 landscape | ⏳ legacy, awaiting rebuild |
| 13 | The Little Rainbow Who Found Her Colors | 15 | 768×1376 portrait | ⏳ legacy, awaiting rebuild |
| 14 | The Little Seed Who Grew Brave | 20 | 768×1376 portrait | ✅ current standard |
| 15 | The Little Cloud Who Found Her Voice | 20 | 768×1376 portrait | ✅ current standard (reference) |

`python tools/check_book.py --all` verifies every row above mechanically.

---

## What each book contains

Every book folder follows the same contract:

```
NN_Title/
├── manuscript/story.txt     20-page page map: exact page text + art direction
├── illustrations/           page_01.png … page_20.png  (768×1376, RGB)
├── pdf/<Title>.pdf          20 pages, one image per page
├── metadata/metadata.json   locks, moral, format, characters, themes
└── production_report.md     QA table + regeneration log
```

## Morals (one per book)

| # | Moral |
|---|-------|
| 01 | Letting go takes courage — and it can turn you into something new. |
| 02 | Believe in magic, and your belief can bring it back to life. |
| 03 | You do not have to be perfect to feel joy — just brave enough to try. |
| 04 | Notice and appreciate the beauty around you, because it is always there. |
| 05 | Sometimes being part of something bigger is even better than owning it. |
| 06 | Being big is not about size. It is about the heart. |
| 07 | You do not have to be loud to matter. |
| 08 | Letting go is not the end of something. It is the beginning of something new. |
| 09 | Imagination belongs to the person who makes it, and you can always go back to what you create. |
| 10 | Every lost thing has a story, and every story deserves to be heard. |
| 14 | Courage and patience help you grow into who you are meant to be. |
| 15 | Your voice matters — speak up with kindness and courage. |

---

## Making another book in this style

The method and the tooling live in [`tools/`](tools):

- **`tools/WORKFLOW.md`** — the step-by-step agent playbook (plan 20 pages →
  lock the characters → generate → QA → assemble → document → push), including a
  ready-made briefing paragraph for a new environment.
- **`tools/PROMPT_TEMPLATE.md`** — the approved page-prompt skeleton, the four
  text variants (narrative, dialogue, cover, back cover), and a defect/fix table
  for every text and character drift actually encountered.
- **`tools/templates/`** — manuscript, metadata, and production-report templates.

Scripts (the only code in the pipeline):

```bash
pip install --break-system-packages -r tools/requirements.txt

python tools/build_pdf.py <book_dir>        # validate 20 images -> assemble PDF -> pypdf read-back
python tools/check_book.py --all            # structural QA for the whole series
python tools/qa_crop.py <page.png>          # zoom the lettering for visual QA
python tools/qa_crop.py --sheet <book_dir>  # contact sheet of all 20 pages
```

`15_The_Little_Cloud_Who_Found_Her_Voice/` is the reference implementation: when
in doubt about tone, page rhythm, or text length, open that book.

## Repository notes

- `BOOK_QA/` — per-book QA notes from the original build.
- `PROJECT_*.md` — history of the original (pre-standard) production run.
- The root-level `create_*.py` / `generate_*.py` / `final_pdf_generator.py`
  scripts are legacy: they typeset text with code, which the current standard
  forbids. They are kept only for history. Use `tools/` instead.
