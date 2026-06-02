# 08 — Design System

> **Where to paste:** `🎨 Design System` page in Notion.

---

## Paste the content below into the page

---

## What this page does

Defines the carousel's universal visual principles — hierarchy, rhythm, anti-patterns. These principles **become descriptive text in the GPT Image 2 (`gpt_image_2`) prompt** when R2 generates the slides.

> **Important:** the specific aesthetics (font, palette, mood) **do not live here** — they live on the `🖼️ Visual References` page, which you edit when you want to change the feed's look. This page is the part that **does not change** between aesthetics.
>
> The brand's palette comes from `🏷️ Brand Identity` (variables `{brand_color_primary}`, `{brand_color_dark}`, `{brand_color_light}`) and is automatically interpolated into the prompts.

---

## Fixed technical specifications

- **Final dimension:** the original PNG returned by the Higgsfield CLI. Do not downscale, crop, resize or convert to 1080×1350.
- **Generation dimension:** Higgsfield CLI with `--aspect_ratio "3:4"` and `--resolution "2k"`. Do not use the legacy fixed-size parameter. If the file comes in a high dimension (e.g. ~1856px on the longest edge), keep it as-is.
- **Resolution:** 72 DPI
- **Output format:** PNG
- **Color space:** sRGB
- **Standard slide count:** 9 (configurable: 5, 7, 9, 12)

---

## The rule of 3 hierarchy levels

Every slide has exactly 3 reading levels. Never more, never fewer.

| Level | What it is | Visual weight |
|-------|---------|------------|
| **1 — Anchor** | The element the eye sees first | Largest: big headline, giant number, or image |
| **2 — Context** | What explains the anchor | Medium: body text, paragraphs |
| **3 — Metadata** | What organizes without competing | Smallest: section tag, handle, discreet visual signature |

**Prompt rule:** when R2 assembles the slide prompt, always describe the 3 levels explicitly to GPT Image 2. Example:

```
Hierarchy:
- Level 1 (anchor, largest visual weight): the headline "TOPIC X" in bold condensed type
- Level 2 (context, medium weight): the body paragraph below
- Level 3 (metadata, smallest weight): the tag "THE PROBLEM" at top and the brand handle/detail signature at the bottom. Do not render slide numbers or counters.
```

**If a slide has 2 elements of the same weight → hierarchy broken.** Rewrite the prompt.

---

## Dark / light rhythm

The carousel alternates backgrounds to maintain the scroll. Suggested sequence of 9 slides:

| Slide | Function | Suggested background |
|-------|--------|-----------|
| 1 | Cover | Full-bleed photo/image with heavy dark gradient at the base |
| 2 | Hook | **Dark** with image (photo background OR texture) |
| 3 | Mechanism p1 | **Light** with image box |
| 4 | Mechanism p2 | **Dark** with image or texture |
| 5 | Proof | **Light** with table or giant number over side photo |
| 6 | Expansion | **Dark** with background photo |
| 7 | Application | **Light** with 3 mini-images (cards) |
| 8 | Direction | **Dark or Light** (depends on the refs — see below) |
| 9 | CTA | **Light** with logo |

**Rhythm functionality:**
- **Dark** = tension, revelation, mechanism. Serious tone.
- **Light** = data, proof, application. Accessible tone.

**Break rule:** never 3 consecutive slides of the same type.

**Density rule:** dark handles less text than light (tires the eye more). Max ~50 words on dark, ~70 on light. **Less is more.**

> **The dark/light rhythm is subordinate to `🖼️ Visual References`.** The table above is the default. If the brand's refs are predominantly light (or predominantly dark), the carousel follows the tonal register of the refs — don't force dark slides into a feed whose refs are light. R2 records the actual tonal register of the refs in the visual brief and that's what governs. The refs decide; the table does not override.

### Gradient — not the default

Previous V2 used a mandatory gradient on slide 8. **V2.5 changed this:** the use of a gradient is decided case-by-case, depending on what the brand's `🖼️ Visual References` suggest.

- If the visual refs have gradients integrated into the system → R2 may use them on slide 8 (or others)
- If the visual refs do NOT have a gradient (sober editorial mood, no effects) → R2 keeps slide 8 in dark/light, with no gradient
- Never apply a gradient just "because there has to be a gradient slide"

R2 reads the visual briefing decoded from `🖼️ Visual References` and decides.

---

## The lower-third principle

Textual content occupies the **lower and middle third** of the slide. The upper third is visual breathing room.

**Exceptions where the top is filled:**
- Slide with a rectangular image at the top
- Slide with a giant number in the center-top (e.g. "2,300%")
- Cover slide (full-bleed photo)
- Slide with a large headline that fills it naturally

---

## Typography — universal principles

> The project's fonts (the 2 families, exact weights and sizes) are **LOCKED** in the "Font system — LOCKED" section of the `🖼️ Visual References` page — it is the typographic source of truth. What's here are the **universal usage rules**. In case of divergence, the locked table in `🖼️ Visual References` wins.

### Mandatory typographic contrast
- **Headline** always in a **personality** font (condensed, serif, or strong geometric), bold/black weight, uppercase, negative kerning
- **Body** always in a **readability** font (neutral sans-serif), regular weight, sentence case, neutral kerning
- **Never use the same font/weight/size** for two different elements

### Size hierarchy (reference scale)

> The values below are reference ranges. R2 **does not use ranges** — it uses the **exact values** from the locked table in `🖼️ Visual References` → "Font system — LOCKED" (one size and one weight per role). A range generates size variation between slides; an exact value does not.

| Element | Reference size | Weight |
|---------|-------------------|------|
| Cover headline | 88–108px | 900 |
| Internal headline (dark) | 72–80px | 900 |
| Internal headline (light) | 64–72px | 900 |
| Gradient headline | 72–80px | 900 |
| Body | 36–40px | 400 |
| Body strong (highlight) | 36–40px | 700 |
| Section tag | 13px | 700, uppercase, high letter-spacing |
| Brand bar / handle | 17px | 700 |

### Text color
- **Dark slides:** body in white at 55% opacity, strong in 100% white, accent in the primary color
- **Light slides:** body in black at 60% opacity, strong in 100% black, accent in the primary color
- **Accent (primary color)** appears only on **keywords**, never on entire sentences

---

## Palette generation from the dominant color

The palette comes from `🏷️ Brand Identity`. The agent injects the variables and R2 derives intermediate tones when necessary:

```
PRIMARY        = {brand_color_primary}        (defined in Brand Identity)
PRIMARY_LIGHT  = primary lightened ~20%       (derived by R2)
PRIMARY_DARK   = primary darkened ~30%        (derived by R2)

LIGHT_BG       = {brand_color_light}          (default warm-cream #F1ECE3)
DARK_BG        = {brand_color_dark}           (default warm-dark #1B1411)

GRADIENT       = linear-gradient(165deg, PRIMARY_DARK 0%, PRIMARY 50%, PRIMARY_LIGHT 100%)
```

Current defaults (Human Academy):
```
PRIMARY        = #EC5E26  (warm orange)
LIGHT_BG       = #F1ECE3  (warm cream)
DARK_BG        = #1B1411  (warm dark)
```

**Contrast rule:** the primary color **NEVER appears as a text background**. Always as accent on keywords, or in cover headlines, or as fill on the gradient slide (slide 8).

---

## Visual components — when to use each

Each slide may use **one visual component** depending on the content. R2 describes the chosen component in the GPT Image 2 prompt.

### Card (slides with a quote or short list)
**Use when:** text needs extra highlight, or list of 2-3 items inside the slide.
**Don't use when:** the slide already has a headline + body (card becomes noise).

### Table (data slide — typically slide 5)
**Use when:** 3+ comparable items (indicator + value).
**Don't use when:** fewer than 3 data points (looks disproportionate).

### Big Stat (giant number)
**Use when:** a single number is the slide's protagonist (e.g. "2,300%", "115k", "1,168 posts").
**Don't use when:** the slide has multiple data points of equal weight.

### Image Box (image rectangle at the top)
**Use when:** the slide has less than 60% textual filling.
**Don't use when:** the slide is already dense.

### Arrow Rows (sequential list)
**Use when:** 2-3 sequential points (not parallel).
**Don't use when:** more than 4 items (becomes a list, loses impact).

---

## Mandatory elements on every slide

### Accent bar (top)
Thin line, 6-7px, gradient of the primary color. Crosses the slide horizontally.

### Brand bar (top)
Small line of text right below the accent bar:
```
Powered by {brand_name}    |    {brand_handle}    |    2026 ®
```
- Opacity 100% (no transparency)
- Size 13–14px
- Light slides: color in dark gray 45%
- Dark slides: color in white 45%

### Detail signature (footer) — feed consistency

Small element, repeated on **all 9 slides**, that gives the carousel its "signature". **The exact content is decided from `🖼️ Visual References`** — R2 observes the recurring detail in the refs and replicates it.

Common patterns seen in quality feeds:
- Thin horizontal line + small text (date + handle): `2026.05.14 · @humanacademy`
- Side mini-graphic (geometric symbol repeated on all slides)
- Tiny section tag in the bottom corner (e.g. `EDITORIAL · @humanacademy`)
- Discreet bar without textual numbering, if the references show this device

The function: **make the feed look like a curated collection, not 9 loose slides**. Without a detail signature, each slide looks isolated.

### Progress bar (footer)
Small horizontal bar at the bottom of the slide, showing progress:
- 3px track, 2px border-radius
- Fill proportional to ((current_slide / total) × 100)%
- No text counter. Never render any number, index or slide position marker.

May coexist with the detail signature or replace it if the refs suggest it.

### Brand logo (cover and CTA)

If `brand_has_logo = true` in `🏷️ Brand Identity`:
- **Slide 1 (cover):** **small** logo, in the bottom-right corner or aligned with the handle. Discreet — does not compete with the headline. Size ~60-80px.
- **Slide 9 (CTA):** **large** logo, horizontally centered and optically between 50% and 56% of the height. Size ~320-420px, adjusted to the file. It is the slide's visual protagonist.
- **Slides 2-8:** **no logo.** The feed breathes.

If `brand_has_logo = false`:
- Slides 1 and 9 use a typographic lockup with `{brand_name}` in the cover font (condensed bold), optional monogram. On slide 9, this lockup takes the logo's place and stays large/centered.

### Final CTA rule

- Slide 9 has at most one short CTA, with up to 8 words.
- The CTA sits below the logo/lockup, with smaller hierarchy and lots of breathing room.
- No paragraph, summary, rhetorical question or two text blocks enter.
- The handle may appear small below the CTA, but never compete with the brand.

### Do not use
- ❌ "Swipe →" arrows on the slide (swipe is native to Instagram)
- ❌ Generator watermarks
- ❌ Decorative emojis
- ❌ Generic stock icons
- ❌ Brand logo on slides 2-8 (disrupts breathing room)

---

## Visual anti-patterns — never do

- ❌ Centered text on content slides (only the CTA can have centered elements)
- ❌ Two paragraphs of the same size and weight
- ❌ Image without overlay compromising legibility
- ❌ Accent color on more than 3 words per slide
- ❌ Card inside a card
- ❌ Table with fewer than 3 rows
- ❌ Headline in sentence case (always uppercase in condensed)
- ❌ Body text in uppercase (never)
- ❌ More than 100 words on a dark slide
- ❌ Slide with only a tag + 1 short sentence (looks incomplete)
- ❌ Generic colored gradients as text background
- ❌ Glow effects, neon, hologram, Y2K
- ❌ Stock photo as background on internal slides

---

## Cover slide — special rules

The cover is the most important slide. It's the one that **sets the visual aesthetic** of the entire carousel (because it becomes the reference for the rest of the slides via image-to-image).

Requirements:
- Full-bleed image (photo, abstract background, or strong texture)
- Dark gradient at the base — strong enough for 4.5:1 contrast with white text
- Large headline in condensed/serif font (per visual reference)
- Keywords in primary color (accent)
- Instagram handle left-aligned, in the headline block
- **No decorative badges** (date, content type, etc.) — the cover is clean: image + headline + handle
- Headline + handle in the lower third of the slide (bottom ~120px)

---

## Legibility guarantees — always verify

Before approving any slide:

- [ ] Text/background contrast ≥ 4.5:1
- [ ] No text over a light area of the image without a protective gradient
- [ ] Headline does not overflow the slide area
- [ ] Body does not overlap the progress bar (minimum 80px padding-bottom)
- [ ] Safe horizontal margins (minimum 52px)
- [ ] Accent words only on keywords, not entire blocks
- [ ] Perceptible 3-level hierarchy
