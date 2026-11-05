# Children's Picture Books — Hamidreza Rostami

A series of 15 English picture books for readers aged 3–9, built to one strict
house standard.

## The standard

- **20 pages per book:** 1 front cover + 18 story pages + 1 back cover.
- **Portrait 9:16, 768 × 1376 px, RGB**, one page image per PDF page, no spreads.
- **All artwork and all text are AI-generated images.** Story text, cover title,
  back-cover blurb and the "Created by Hamidreza Rostami" credit are painted
  directly into the illustration on each page.
- **Code does one job only:** assembling the finished page images into a PDF.
  No HTML, CSS, canvas, SVG, PIL text, or PDF text is ever used to make a page.
- English only. Positive ending. The moral is shown through the story, never
  announced. No ISBN, no barcode, no page numbers.

## Where things are

| Path | What it is |
|---|---|
| `01_…` – `15_…` | one folder per book: `manuscript/`, `illustrations/page_01…20.png`, `pdf/`, `metadata/`, `production_report.md` |
| `15_The_Little_Cloud_Who_Found_Her_Voice/` | the reference book — the approved look and rhythm |
| `BOOK_CATALOG.md` | full catalogue, per-book morals, rebuild status |
| `tools/` | the method: playbook, prompt template, PDF assembler, QA scripts, templates |

## Quick start

```bash
pip install --break-system-packages -r tools/requirements.txt

python tools/check_book.py --all         # structural QA of the whole series
python tools/build_pdf.py 10_The_Little_Library_of_Lost_Things
python tools/qa_crop.py --sheet 09_The_Boy_Who_Painted_Dreams
```

## Making a new book in this style

Read **`tools/WORKFLOW.md`** (the agent playbook) and
**`tools/PROMPT_TEMPLATE.md`** (the exact prompt skeleton plus a table of every
text/character drift encountered and the clause that fixes it). Copy from
`tools/templates/`, follow the 20-page map, QA every page, then assemble.

## Status

Books **01–10 and 14–15** are complete at the current standard.
Books **11–13** still carry their legacy landscape/partial layouts and are due
for a rebuild with the same method.
