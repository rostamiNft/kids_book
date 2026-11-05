# How to build a book in this style (agent playbook)

This is the exact method used for books 01–10. Follow it in order. It assumes an
agent with an image-generation tool, a code tool (bash), and a git remote.

**The one rule that defines the style:** every page is a single AI-generated
image that contains its own artwork *and* its own text. Code is allowed only at
the very end, to stitch finished images into a PDF. No HTML, CSS, canvas, PIL
text, SVG, or PDF text anywhere in the page-making process.

---

## Step 0 — Environment

```bash
pip install --break-system-packages -r tools/requirements.txt
# or: pip install --break-system-packages Pillow pypdf
python -c "import PIL, pypdf; print('ok')"
```

Folder contract for a book (`NN_Title_Case_With_Underscores/`):

```
manuscript/story.txt          the 20-page page map (text + art direction per page)
illustrations/page_01.png     one finished page per file, 768x1376 RGB
pdf/<Book Title>.pdf          assembled from the images only
metadata/metadata.json        locks, moral, format, characters
production_report.md          QA table, regeneration log
```

## Step 1 — Read the source story and plan 20 pages

1. Read `manuscript/story.txt` (or the old spread layout) first. Never write a
   prompt without the exact line in front of you.
2. Fix the skeleton: **1 front cover + 18 story pages + 1 back cover = 20.**
3. Place the beats before you place the pictures. Mark which page holds the
   climax and which page demonstrates the moral. **If the climax or the moral
   has no page, the map is wrong** — this is the single most damaging mistake,
   because it only shows up after 20 images exist.
4. One beat per page. If a page needs three things to happen, it needs two pages.
5. Keep the six longest text blocks for the quiet, wide, uncluttered images.

## Step 2 — Write the manuscript as a prompt-ready spec

Rewrite `manuscript/story.txt` with, at the top, the blocks that will be
repeated on every page:

- **TARGET / MORAL / VISUAL STYLE / FORMAT**
- **CHARACTER LOCK** — hair, eyes, skin, garment, footwear, prop, for every
  recurring character, in the same words every time.
- **SETTING** — one paragraph of fixed geography and palette.
- **TEXT RULE** — narrative prose has no quotation marks; dialogue keeps double
  quotation marks; no contractions (write "do not", "did not", "cannot", "it is")
  so that no stray apostrophes can appear.

Then one block per page:

```
== PAGE 7 ==
Text: <the exact words to be painted, verbatim>
Art: <one unified scene, camera, light, background>
```

Use `tools/templates/story_template.txt` as the starting point.

## Step 3 — Generate the pages, in order

Use `tools/PROMPT_TEMPLATE.md`. For every page, restate the character lock in
full — never write "the same girl as before"; the model does not have memory.

Practical loop:

1. Generate pages 1–5 (cover first: if the title lettering is wrong, nothing
   else matters).
2. **Look at every page** before generating more (the QA step below).
3. From page 6 onward, pass one or two approved pages as `images=[...]` and open
   with "Match the character's clothing and faces EXACTLY to the reference
   image." This is what keeps a protagonist's wardrobe from drifting.
4. Respect the per-turn image budget (10 in Arena). New pages first; retries
   after. Never reference a page generated in the same parallel batch.
5. Keep scene props free of written words (blank chalkboards, blank tags,
   unlabelled jars), because background lettering renders as gibberish.

## Step 4 — QA every page (visual + text)

Read the full-size image for every page and check, in this order:

1. **Text is the exact words** — read it character by character; look for
   dropped words, doubled sentences, clipped words, missing opening quotes.
2. **Text belongs to the right page** (page ordering, no repeats).
3. **Character lock holds** — garment, colour, footwear, prop, hair.
4. **One unified scene**, nothing duplicated, no second copy of a creature.
5. **No barcode / ISBN / page number / watermark / logo.**
6. **Mood** — sad beats gentle, night scenes warm, nothing frightening.

Zoom in on the lettering when in doubt:

```bash
python tools/qa_crop.py illustrations/page_11.png --out /tmp/p11_text.png
python tools/qa_crop.py illustrations/page_11.png --box 60,900,700,1000 --scale 3
```

Review the whole book at once for drift:

```bash
python tools/qa_crop.py --sheet 10_The_Little_Library_of_Lost_Things
```

**Any page that fails gets deleted and regenerated.** Do not ship a fixed page:
the fix is a new image with a new clause in the prompt (see the defect tables in
`PROMPT_TEMPLATE.md`). Keep replacing until it passes.

## Step 5 — Assemble the PDF (the only code step)

```bash
python tools/build_pdf.py 10_The_Little_Library_of_Lost_Things
```

This validates 20 images, 768×1376, RGB, one image per page, then writes the PDF
and reads it back with pypdf to confirm 20 pages of a single page size.

## Step 6 — Write metadata and the production report

`tools/templates/metadata_template.json` and
`tools/templates/production_report_template.md`. The regeneration log is not
paperwork: it is the reason a second run of the same book is faster.

## Step 7 — Verify the book, then push

```bash
python tools/check_book.py 10_The_Little_Library_of_Lost_Things
python tools/check_book.py --all          # the whole series
git add -A <book_dir> && git commit -m "Book NN COMPLETE: 20 pages + PDF + metadata"
git push
```

Delete the legacy spreads/PDF for that book in the same commit — only the
20-page portrait version should remain in the tree (git keeps the history).

---

## Briefing an agent in a new environment

Paste this, adapted:

> Build a 20-page children's picture book in the established style of this
> repository. Read `tools/WORKFLOW.md`, `tools/PROMPT_TEMPLATE.md` and
> `15_The_Little_Cloud_Who_Found_Her_Voice/manuscript/story.txt` first; they are
> the standard. Every page must be one AI-generated portrait image, 768×1376
> px, RGB, with its story text painted inside the artwork; code may only
> assemble the finished images into a PDF with `tools/build_pdf.py`. Plan
> 1 cover + 18 story pages + 1 back cover, confirm the climax and the moral have
> pages before generating, QA every page visually and regenerate anything that
> fails, then write metadata + production report and run
> `python tools/check_book.py`.

## Style reference, in one paragraph

Cinematic 3D animated children's film look: soft sculpted characters with big
warm eyes, painterly cosy backgrounds, honey-gold lamplight or dreamy starlight,
dust motes, rich wood/wool/candy textures, a warm cream page-text lettering with
a deep brown outline and gentle drop shadow sitting in the calm lower third of
each page. Sweet, safe, wondrous, never frightening; positive ending, moral
shown rather than stated.
