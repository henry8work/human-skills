# 11 — Visual References

> **Where to paste:** `🖼️ Visual References` page in Notion.
> This is the page **you edit whenever you want to change the feed's aesthetic**. R2 reads everything here and uses it as a brief for GPT Image 2 (`gpt_image_2`).

---

## ⚠️ Critical learning — real vision + grids

V1 of the system ran R2 as a Web Routine and **only read text** from this page. The visual brief came out generic → the first carousels were mediocre even with rich inspiration images.

In V2.5, R2 runs as a Local Routine. **It downloads the bytes of the attached images and does real vision** (Claude's native Read tool). It extracts the real visual system (observed typography, hierarchy, secondary colors, mood) and compiles the brief.

### Tonal and style fidelity — two errors R2 must avoid

Even with real vision, two deviations appeared in use:

**Darkening too much.** R2 pulls the palette toward dark even when the refs are light or mid. Result: the feed feels more somber than the inspiration. R2 now records the **tonal register** of each ref and reproduces that luminosity — if the refs are light, the carousel is light. The Design System's dark/light rhythm only applies if the refs show both.

**Literalness with the subject.** R2 illustrates the news topic literally (news about an app → image of an interface) even when the refs use another language (people, gesture, editorial photography). The **image style comes from the refs** — if the refs are humanized, the carousel images are humanized, and the subject becomes a visual metaphor in that style.

That's why: attach refs that faithfully represent the luminosity AND the type of image you want. R2 follows what it sees.

**Implication for you:**
- **Attach real images — don't try to describe the aesthetic only in text.** Text guides, but it's the image that teaches the system.
- **Quantity is not the focus — consistency is.** It can be 1 good grid, or 3 to 7 separate images. What matters: they all need to show the SAME visual and typographic language. Divergent refs generate a divergent feed.

### Refs as a grid (critical understanding)

Usually, when someone saves visual inspiration on Pinterest, Behance or Are.na, they bundle **multiple slides into a single grid image** — a Behance page with 9 slides arranged in a 3×3 grid, an Instagram timeline screenshot with 6 covers, a moodboard spreadsheet.

**The Routine understands this.** When you attach an image here:

- If it's **a single slide** (one cover, one loose post) → counts as 1 reference
- If it's a **grid** with multiple visible slides → each region of the grid counts as an independent reference. A 3×3 grid image delivers **9 different slide references** to the system

The Routine looks at each image and decides internally: "is this unitary or a grid?". If a grid, it mentally decomposes and observes each exemplar — typography, hierarchy, colors, composition — as if they were N separate exemplars.

**Practical implication:** **a single good grid image may be enough.** Don't force quantity — attach what actually represents the aesthetic you want.

---

## Paste the content below into the page

(After pasting, **attach your inspiration images** in the indicated sections — drag the image straight onto the Notion page.)

---

## Dominant color

**Primary:** `{brand_color_primary}` (comes from `🏷️ Brand Identity`)

Default example: `#EC5E26` — warm orange, earthy, with a slight burn — not neon-vibrant, not pastel.

R2 derives the full palette from this color.

---

## General feed mood

Describe in 3-5 sentences the visual tone you want to convey:

> Editorial, sober, magazine-like — references European design publications (Eye Magazine, Wallpaper, It's Nice That). Typography with presence and personality. Generous negative space. No ornament, no generic illustration, no cutesy AI gradient. Subtle texture — film grain, imperfect paper. When color shows up, it shows up with intent, on a keyword, never as a colorful background.

> An aesthetic that looks designer-made, not template-made.

---

## Font system — LOCKED

> **This section is the typographic source of truth of the project.** R2 uses EXACTLY
> these fonts — same family, same weight, same size — on every slide of every
> carousel. It does NOT re-derive typography from the images each run and does NOT vary between
> slides. To change the feed's typography, edit HERE — and only here.

**Why lock it:** GPT Image 2 should not receive vague font instruction — it renders
descriptions. A vague description ("a bold condensed") makes the model pick a different
font on every slide and every carousel — that was exactly the problem observed. The
solution is a single, exact, always-identical description, with R2 copying it verbatim
into every prompt — together with the use of the cover and visual refs as fixed references.

The project uses **exactly 2 fonts**: one DISPLAY (headlines) and one TEXT (everything
else — body, tag, brand bar, detail signature). Two and only two.

> **How to pick:** look at your visual refs, identify the headline font and the text
> font, and name both below. When in doubt, ask R2 to suggest from the refs.
> Once picked, they stay locked — don't change them on every carousel.

### Font 1 — DISPLAY (cover and internal headlines)

- **Name:** `Druk Wide Bold` *(swap for another if you want — keep only ONE)*
- **Locked description** (R2 copies this exact sentence into the prompt):
  `heavy wide grotesque display typeface, weight 900, all-caps, very tight
  letter-spacing, bold geometric letterforms with strong magazine-cover presence`

### Font 2 — TEXT (body, tag, brand bar, signature)

- **Name:** `Söhne` *(swap for another if you want — e.g. Inter, Plus Jakarta Sans)*
- **Locked description:**
  `clean neutral humanist sans-serif, even stroke weight, medium x-height,
  highly legible at small sizes, no decorative details`

### Application table — EXACT values (never ranges)

R2 applies these fixed values. Each role has ONE size and ONE weight — never a
range. The "tiny upper fonts" (tag and brand bar) are also locked here.

| Role | Font | Weight | Reference size | Case | Tracking |
|---|---|---|---|---|---|
| Cover headline | Display | 900 | 96px | UPPERCASE | -3px |
| Internal headline | Display | 900 | 74px | UPPERCASE | -2px |
| Body | Text | 400 | 38px | sentence case | 0 |
| Body strong (highlight) | Text | 700 | 38px | sentence case | 0 |
| Section tag | Text | 700 | 14px | UPPERCASE | +2px |
| Brand bar / handle | Text | 600 | 16px | as written | +0.4px |
| Detail signature (footer) | Text | 500 | 13px | as written | +0.3px |

> R2 injects this entire section — names, descriptions and table — as the
> `TYPOGRAPHY LOCK` block in EVERY slide prompt (cover and 2-9), always with the same text.
> That, combined with the cover + visual refs across all slides, is what keeps the font identical between slides
> and between carousels.

---

## Inspiration images

> **How to use this section:** attach **3 to 7 images** (drag them onto the Notion page), or a grid. It can be:
> - Single images (one cover, one loose post) — each counts as 1 reference
> - **Grids** with multiple visible slides (feed screenshot, Behance page, moodboard) — each region of the grid counts as an independent reference
>
> The more refs consistent with each other, the more stable the result. If you have more than 3 images, add "Reference 4", "Reference 5"… sections below.
> Write 1-2 lines next to each image explaining what makes it work — highlighting, if it's a grid, how many exemplars are there and what to observe.

### Reference 1
**[attach image here]**

Description: _Unitary example — "condensed bold headline on 5 lines, keyword in orange, black background with grain. Very clear hierarchy: headline dominates, small handle below. It's the cover type reference I want."_

_Grid example — "3x3 grid with 9 carousel slides by @brand-x. Pay special attention to slide 2 (dark with image box) and slide 5 (table on a light background). Detail that appears on all: thin horizontal line at the footer with date + small handle."_

### Reference 2 (optional)
**[attach image here]**

Description:

### Reference 3 (optional)
**[attach image here]**

Description:

---

## Anti-examples — what we do NOT want

List explicitly. The more specific, the better the result.

- We don't want generic Apple minimalism (too cold, too clean)
- We don't want "purple AI gradient" (cliché)
- We don't want a blue SaaS dashboard
- We don't want basic Bauhaus with colorful geometric shapes
- We don't want torn-paper / fake-vintage texture
- We don't want decorative emojis on any slide
- We don't want stock photos as background
- We don't want glow / neon / Y2K / glitch effects
- We don't want 3D, hologram, Unreal Engine render
- We don't want AI-generated faces
- We don't want handwritten / brush-script text

---

## Preferred composition

**Internal slides (light and dark):**
- Text on the left, aligned to the top or middle
- Minimum 80px side margin
- Content occupies the lower and middle third of the slide
- Upper third stays as breathing room
- Small tag at the top (above the brand bar)
- Discreet progress bar in the footer

**Cover slide:**
- Full-bleed image or textured background
- HUGE headline in the lower third, left-aligned
- Small Instagram handle above the headline
- No other elements (no date, no category, no badge)

**Gradient slide (slide 8):**
- Diagonal gradient from primary dark → primary → primary light
- Short headline, centered
- Arrow list (→) listing 3 points

---

## Color application

The primary color appears:

- ✅ On keywords inside headlines and body (1-3 words per slide at most)
- ✅ As fill of the progress bar on light slides
- ✅ As the color of the small tag at the top of each slide
- ✅ As the base of the gradient on slide 8
- ✅ As a thin accent bar at the top of each slide (6-7px)

The primary color does NOT appear:

- ❌ As a text background on internal slides
- ❌ In large solid color blocks
- ❌ On more than 3 words per slide

---

## Final block for R2 (do not edit — used by the routine)

```
INSTRUCTION FOR R2:

When you read this page:

1. Identify the dominant color (field "Primary").
2. Derive the full palette per the rules of "🎨 Design System".
3. Read the entire "General mood" — use as an atmosphere descriptor in the prompt.
4. Read the entire "Font system — LOCKED" section (names of the 2 fonts,
   locked descriptions and the size/weight table). Copy it VERBATIM as the
   briefing's "TYPOGRAPHY LOCK" block — DO NOT re-derive typography from the images,
   DO NOT paraphrase, DO NOT vary. This block goes identically into every slide prompt.
5. For each image attached on this page:
   a. Open the image (Claude's native vision — Read tool).
   b. DECIDE: is it a unitary image or a GRID with multiple slides?
      - Grid signals: spatial regularity (rows/columns), repeated borders, 
        square or rectangular format subdivided, multiple similar 
        rectangles side by side.
      - If grid: mentally decompose into N exemplars (e.g. 3x3 grid 
        = 9 exemplars; feed screenshot = 6+ exemplars). Observe each 
        exemplar separately as if they were independent refs.
      - If unitary: treat as 1 ref.
   c. Combine your observation (including each grid exemplar if any) 
      with the textual description next to the image.
   d. Extract: hierarchy, rhythm, texture, composition,
      recurring details (footer, accent bar, signature) that appear 
      in several exemplars — these are the feed's consistency markers 
      you need to replicate.
   e. TONAL REGISTER: observe whether each exemplar is light, mid or dark,
      and the dominant luminosity of the backgrounds. DO NOT darken the palette
      beyond what the refs show — this is a recurring error. If the refs
      are light, the carousel is light.
   f. IMAGE STYLE: observe what TYPE of image the refs use —
      photography, humanized people/gesture, object still, illustration,
      abstract texture. The carousel's images follow that style, not
      a literal illustration of the news subject.
6. List all anti-examples from the "Anti-examples" section — they enter 
   as "DO NOT" in the negative prompt.
7. Compile everything into a decoded visual brief in the format defined in
   "⚙️ Render Engine". MANDATORY SECTIONS in the brief: "TYPOGRAPHY LOCK"
   (the "Font system — LOCKED" section copied VERBATIM — names of the 2
   fonts, locked descriptions and size table), "Tonal register /
   luminosity" (refs' tonal register + background luminosity + order
   NOT to darken beyond the refs), "Imagery style" (type of image of the refs —
   photographic/human/object/illustration — which governs each slide's image_brief),
   "Use of gradient", "Detail signature / footer" (recurring consistency
   element: line + small text? micro-graphic? date + handle?) and
   "Composition style".
8. This brief enters as a fixed block in ALL prompts (cover and 
   internal slides).
```
