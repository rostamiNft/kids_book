# Page Prompt Template — the approved standard

Every page in books 01–10 and 15 was generated with the same five-block prompt.
Copy the skeleton, fill the brackets, keep the order. The order matters: style
first, locks second, scene third, text last.

---

## Skeleton

```
High-quality 3D animated children's illustration (cinematic children's
animation), warm cosy painterly rendering with honey-gold lamplight, floating
dust motes and rich textures. Portrait 9:16 children's picture-book page,
768x1376.

[B1 — REFERENCE LINE, optional but strongly recommended]
Match the characters' clothing and faces EXACTLY to the reference image.

[B2 — CHARACTER LOCK, restated in full on every single page]
Character consistency is critical. <NAME> must be exactly: <hair, eyes, skin,
clothing, footwear, prop>. <SECOND CHARACTER> must be exactly: <...>.

[B3 — SCENE]
<One unified scene. Camera angle, where the characters are, what they are
doing, what is in the background, the light.>

[B4 — TEXT]
Storybook page text embedded directly in the artwork, painted into the
illustration as beautiful rounded playful 3D children's-book lettering, warm
cream with a deep chestnut-brown outline and a gentle drop shadow, large and
perfectly legible, centered in the lower third of the image:
"<EXACT TEXT>"

[B5 — NEGATIVES AND TEXT GUARDS]
Reproduce these words exactly, word for word, with NO dropped words, NO
repeated words and no extra lines. <QUOTATION RULE>. No barcode, no ISBN,
no page numbers, no watermark, no logos, no extra text anywhere.
```

---

## Variant: narrative prose (no quotation marks)

```
Reproduce these words exactly, word for word, with NO repeated words and no
extra lines. This is narrative prose and must have NO quotation marks at all,
neither single nor double. No barcode, no ISBN, no page numbers, no watermark,
no logos, no extra text anywhere.
```

## Variant: dialogue (double quotes, every opening mark present)

```
Reproduce these words exactly, word for word, with NO dropped words, NO
repeated words and no extra lines. Use DOUBLE quotation marks exactly as
written, including each opening quotation mark. No barcode, no ISBN, no page
numbers, no watermark, no logos, no extra text anywhere.
```

## Variant: front cover

```
Storybook cover text embedded directly in the artwork, painted into the
illustration as beautiful rounded playful 3D children's-book lettering, warm
cream with a deep chestnut-brown outline and a gentle drop shadow, large and
perfectly legible, arranged in the upper third of the image in three lines:
"<TITLE LINE 1>
<TITLE LINE 2>
<TITLE LINE 3>"

Below it, near the bottom of the image, in smaller elegant script lettering,
the credit exactly: "Created by Hamidreza Rostami"

Reproduce ONLY this cover text, exactly, word for word, and nothing else.
No barcode, no ISBN, no page numbers, no watermark, no logos, no extra text anywhere.
```

## Variant: back cover (three separated paragraphs + credit)

```
The upper third of the image is the illustration; the lower two thirds fade
into a clean smooth cream-to-warm-amber gradient panel, calm and uncluttered,
for the text.

Storybook back-cover text embedded directly in the artwork, painted into the
illustration as beautiful rounded playful 3D children's-book lettering, warm
cream with a deep chestnut-brown outline and a gentle drop shadow, large and
perfectly legible, centered in the lower two thirds of the image, set as THREE
clearly separated paragraphs with a visible blank gap between each one:

Paragraph 1: "<blurb, what the book is>"
Paragraph 2: "<blurb, the two turns of the story>"
Paragraph 3: "<thematic closing line, which carries the moral>"

Below the third paragraph, in smaller elegant script lettering, the credit
exactly: "Created by Hamidreza Rostami"

Reproduce ONLY this back-cover text, exactly, word for word, and nothing else.
No barcode, no ISBN, no page numbers, no watermark, no logos, no extra text anywhere.
```

---

## Hard-won rules (each one fixed a real, repeated defect)

### Text defects
| Defect seen | Fix clause to add |
|---|---|
| Narrative prose wrapped in quotation marks | "This is narrative prose and must have NO quotation marks at all, neither single nor double." |
| A word or phrase silently dropped ("It rolled down the sidewalk" → "It rolled down") | List the sentences as numbered/labelled lines, then: "NO dropped words"; quote the phrase that must stay intact. |
| A line printed twice ("Ms. Willow nodded." ×2) | "The sentence '<x>' appears EXACTLY ONCE." |
| A word repeated mid-sentence ("A beautiful" twice) | "with NO repeated words and no extra lines" |
| A word clipped at line end ("story" → "sty") | "The word '<x>' must be spelled in full and complete every time it appears." |
| Missing opening quotation mark | "The text must BEGIN with a double opening quotation mark immediately before the word '<w>'." |
| More than ~6 text lines turns into a garbled fragment | Shorten the page text to ≤5 short lines. Split the beat across two pages instead. |

### Character defects
| Defect seen | Fix clause to add |
|---|---|
| Protagonist's clothes change colour or garment (shirt → t-shirt, jumper → tee, shoes appear) | Pass approved pages via `images=[...]`, open with "Match the character's clothing EXACTLY to the reference image", and put the garment in caps: "MUSTARD-YELLOW KNITTED JUMPER (a thick knitted sweater with a ribbed crew neck, NOT a t-shirt)". |
| Socks/shoes drift | "MISMATCHED SOCKS - one bright RED sock and one BLUE sock, clearly different", "NO SHOES AT ALL". |
| Wooden objects come out black | "warm honey-brown wood, never black" |
| Night pages bleach the protagonist to white/cream | state the skin/hair colour in the lock even at night |
| Fear or strain wording produces a serene face | describe the expression as concrete features (brows, mouth, eyes) in its own sentence |
| An extra copy of a creature appears | "there is exactly one <creature> in the image" |
| A prop gets a second, invented version | describe the prop once, with its colour and material, in the lock |
| Background signage renders as gibberish | keep such props blank ("a completely blank chalkboard"), or accept it if it is unreadable at page scale |

### Composition defects
| Defect seen | Fix clause to add |
|---|---|
| Prompt packs three beats into one image and it drifts | one unified scene per page; put remembered/dream content in a soft luminous glow in the upper third rather than a second full scene |
| Text collides with busy art | "clean cream-to-warm-amber gradient in the lower third for the text, calm and uncluttered" |
| Long thin objects painted out of proportion | give the aspect in words ("a small round box, wider than it is tall") |

---

## Budget and ordering

- Image generation is capped (10 images per turn in the Arena agent). Plan the
  queue: new pages first, retries after, and never reference a page that is
  generated in the same parallel batch — a reference image must already exist
  on disk.
- Generate the pages in order. Later prompts can then reuse earlier approved
  pages as reference images, which is what keeps the protagonist stable.
