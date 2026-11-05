# Production Report — The Last Leaf of Autumn

**Book number:** 08
**Book title:** The Last Leaf of Autumn
**Creator / Publisher:** Hamidreza Rostami
**Language:** English (100%)
**Target age:** 3–9 years
**Moral lesson:** Letting go is not the end of something. It is the beginning of something new.
**Number of pages:** 20 (1 front cover + 18 story pages + 1 back cover)
**Page dimensions:** 768 × 1376 pixels (9:16 aspect ratio, portrait)
**Color model:** RGB (digital screen optimized)
**Visual style:** High-quality 3D animated children's illustration (cinematic children's animation), warm golden autumn light, painterly rendering with glowing sunbeams and soft bokeh
**Image-generation model:** AI image-generation model — every page, character, background, and typography was generated as AI artwork; all story text is embedded directly into the generated images
**PDF assembly tool:** Python (Pillow) — used exclusively to assemble the 20 AI-generated page images into one PDF; no text rendering or layout drawing performed by code
**Rebuild date:** 2026-11-04
**Branch:** arena/304f4401-kids-book

## Rebuild Note
This book was originally produced in a legacy format (15 landscape pages with two-page spreads, a separate title page and a copyright page, ending on spread page 28). It was fully rebuilt to the Book 15 standard: 20 single portrait pages, one image per PDF page, with all text embedded inside the AI artwork.

Four design rules were written into the manuscript and repeated on every prompt:
- **Character lock:** Rustle is always the same maple leaf with the same face, stem and lobed points.
- **Colour progression lock:** his colour changes exactly as the story demands and never reverts — green with gold edges, then a mid-transformation page, then full red and gold. On the night pages he stays red and gold, only silvered by moonlight, never washed out to white or cream.
- **Wind rule:** the wind is never drawn as a creature, face or body. It appears only as soft luminous spiral ribbons of air and curved light lines.
- **Punctuation lock:** dialogue uses double quotation marks, narrative prose uses none, and contractions were rewritten out ("I am", "do not", "it is", "cannot") so no stray apostrophes can appear.

## Structural Correction
The first 20-page outline compressed the story so tightly that the whole ending was lost: the gentle fall, the landing on the leaf carpet and the Emma scene that *shows* the moral rather than stating it had no pages, and the book ended flatly on "and he let go". Two page-pairs were therefore merged to make room:

| Merged | Into | Result |
|---|---|---|
| old 2 + old 3 | new page 2 | one establishing image holding the perfect branch and the view of the world |
| old 12 + old 13 | new page 11 | one blue jay image carrying both lines of dialogue |

That freed three pages for the correct ending: page 17 (the moment of letting go), page 18 (the fall and the welcome) and page 19 (Emma). The manuscript was rewritten so that the text recorded for each page is the exact text painted into that page's artwork.

## Deliverables
1. Final illustrated PDF book: `pdf/The_Last_Leaf_of_Autumn.pdf` (20 pages, one image per page)
2. Individual AI-generated page images: `illustrations/page_01.png` through `page_20.png`
3. Manuscript: `manuscript/story.txt`
4. Metadata: `metadata/metadata.json`
5. This production report

## Page Map
| Page | Content |
|------|---------|
| 1 | Front cover — "THE LAST LEAF OF AUTUMN" + "Created by Hamidreza Rostami" |
| 2 | The perfect branch, the morning sun, the cool breeze, watching the world |
| 3 | All spring growing, all summer dancing, and now autumn |
| 4 | The other leaves changing and letting go, Rustle still green |
| 5 | Amber and Golden twirl down: "The ground is soft! And the wind is fun!" |
| 6 | "I am not ready. Not yet." |
| 7 | Colder days, stronger winds, the tree getting bare |
| 8 | Crimson: "You will be the last one!" — "I like it here." |
| 9 | The colour change begins at his edges |
| 10 | "He was becoming beautiful." |
| 11 | The blue jay: "You are the most beautiful leaf on the tree!" |
| 12 | The blue jay flies away, Rustle alone again |
| 13 | The stronger wind: "I am not ready," he whispered |
| 14 | Night, the moon, the wind singing through the branches |
| 15 | "Let go, little one. Falling is not the end." |
| 16 | The leaf carpet below, the stars above, and himself |
| 17 | Dawn: he loosens his grip and lets go |
| 18 | The gentle fall, the dance, the leaves welcoming him |
| 19 | Emma holds him high: "You are the most beautiful of all!" |
| 20 | Back cover — story blurb + "Created by Hamidreza Rostami" |

## Quality Assurance Results
| Check | Result |
|-------|--------|
| All pages portrait orientation | ✅ PASSED |
| Consistent dimensions (768 × 1376) on all pages | ✅ PASSED |
| All text in English only | ✅ PASSED |
| Correct spelling and grammar, no broken/hyphenated words | ✅ PASSED |
| Text embedded directly in AI artwork (no code-rendered text) | ✅ PASSED |
| Typography large and readable on smartphone screens | ✅ PASSED |
| Character design consistent across all pages | ✅ PASSED |
| Colour progression consistent with the story | ✅ PASSED |
| Wind never depicted as a creature | ✅ PASSED |
| Consistent double quotation marks for dialogue | ✅ PASSED |
| Vibrant, harmonious, child-friendly colours | ✅ PASSED |
| Night scenes magical rather than frightening | ✅ PASSED |
| One book page per PDF page (no spreads, no blanks) | ✅ PASSED |
| PDF page count matches image count (20) | ✅ PASSED |
| RGB color model | ✅ PASSED |
| Front cover: title + "Created by Hamidreza Rostami" | ✅ PASSED |
| Back cover: three separated blurb paragraphs + "Created by Hamidreza Rostami", no barcode/ISBN | ✅ PASSED |
| Moral lesson shown through the story and the ending | ✅ PASSED |
| Page-by-page visual inspection completed | ✅ PASSED |

## Regeneration Log
- **Page 2** (original outline) — regenerated: single quotation marks wrapped the narrative prose.
- **Page 3** (original outline) — regenerated: stray quotation marks on narrative prose.
- **Page 18** — regenerated: the painted text contained a garbled fragment ("m suth'ay leave,"); the line list was shortened and the reproduction instruction tightened.
- **Page 20** — accepted on first attempt; the three-paragraph layout with visible gaps held.
- **Structural rebuild** — pages renumbered after the two merge operations; two dropped pages were re-rendered from scratch as the merged pages 2 and 11.

**Overall QA status: PASSED — all acceptance criteria met.**
