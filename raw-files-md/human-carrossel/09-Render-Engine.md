# 09 — Render Engine (V3 — Higgsfield CLI)

> **Where to paste:** `⚙️ Render Engine` page in Notion (no API key, just method).
> The actual execution happens **inside the Local Routine session** (`13-R2-Routine-Local.md`) — Claude uses Bash + Read + Higgsfield CLI to orchestrate everything.

---

## What changed from V1 → V2 → V2.5 → V3

**V1 (Web Routine — broke):** R2 called an external image API directly from the sandbox. The sandbox allowlist did not permit that path → render impossible.

**V2 (local script):** R2 became `~/{brand-slug}/r2/run.sh` scheduled by `launchd`. Runs as a normal Mac process: has open network, ImageMagick, Python, real vision via `claude` CLI subprocess, rclone.

**V2.5 (Local Routine):** R2 becomes **a Local Routine** in Claude Desktop. Runs inside a Claude session, with native Bash + Read/Write + WebFetch + Notion MCP + Drive MCP. No atomic scripts, no launchd, no Homebrew. Same render method, but orchestrated by the prompt.

**V3 (Higgsfield CLI):** R2 keeps the Local Routine, but replaces any older direct API call, Flow AI, legacy script or Higgs MCP with the Higgsfield CLI. The visual flow becomes: `higgsfield upload create` for local refs, `higgsfield generate create` for render and `higgsfield generate wait` for collection. Do not use Higgs MCP.

The rest of the method remains: visual reference via CLI, 3:4 generation, and delivery of the original PNG downloaded from Higgsfield. There is no final normalization to 1080×1350, downscale, crop or aspect-ratio change.

Render of slides 2-9 is **parallel**: the cover is generated first; then all internal slides use the cover + the brand's visual references as reference UUIDs. This keeps the aesthetic anchored to the cover and the refs, avoids depending on the previous slide and reduces total delivery time.

---

## Provider and model

- **Provider:** Higgsfield CLI
- **Mandatory image model:** GPT Image 2 (`gpt_image_2`)
- **Mandatory quality:** `--quality high`
- **Commands:** `higgsfield upload create`, `higgsfield generate create`, `higgsfield generate wait`
- **References:** local images become Higgsfield UUIDs and enter as `--image`
- **Text-to-image fallback:** same CLI, without `--image`, only when the brand has no ref attached

### Higgsfield CLI features that matter
- References get more stable when each local image is first uploaded with `higgsfield upload create`
- Final render must record UUIDs, prompt, model, job_id and output URL
- For the Instagram carousel, generate with `--aspect_ratio "3:4"`, `--resolution "2k"` and `--quality high` because that's the portrait option accepted by the current CLI.
- The final output is the PNG downloaded from Higgsfield in the original returned size. If it comes back at 1856px or another 3:4 high-resolution size, keep it.

---

## Authentication

The Higgsfield CLI must be installed and logged in locally.

In Step 0 of the Routine prompt, R2 runs:

```bash
higgsfield account status
```

If it fails, guide:

```bash
npm install -g @higgsfield/cli
higgsfield auth login
```

> Environment page details in `03-Notion-template.md` (section "🔐 Configuration page").

---

## Image strategy — when to use the news photo, generate a new one, or go without

The image is what stops the scroll. **A cover with no good image does not go viral.**

> **Where the news photo comes from:** R1 (Remote) does not download images — its sandbox blocks direct HTTP. The one who extracts the real photo is R2, in **Step 1.5** (`13-R2-Routine-Local.md`), which runs Local with open network. R2 downloads the hero to `state/{TODAY}/news-hero.jpg` and uploads it to a public URL (`hero_url`). If extraction fails, R2 uses the `Visual hint` written by R1 to generate a coherent image (Path B).

### Decision filter

Every image that enters the carousel passes 3 questions:

1. Did Step 1.5 manage to extract the real hero of the news (`news-hero.jpg`)?
2. If yes, is it visually good (resolution, composition, on-topic)?
3. Does it match the aesthetic defined in `🖼️ Visual References` or can it be re-styled via overlay/treatment?

| Scenario | Action |
|---------|------|
| Has good image + matches aesthetic | Use directly as content reference (Path A) |
| Has good image + does not match aesthetic | Use as reference but with re-styling instruction (Path C) |
| Has image but it's weak (logo, bad screenshot, low res) | Generate new one with textual direction (Path B) |
| Has no image at all | Generate new one with editorial textual direction (Path B) |

### Base rule per slide (V2.5 default — more images)

| Slide | Function | Image? | Type |
|-------|--------|---------|------|
| 1 Cover | Cover | **Always** | Full-bleed background + small logo if `brand_has_logo` |
| 2 Hook | Initial tension | **Often** | Image box at top OR background photo with dark overlay |
| 3 Context | What data shows | **Always** | Rectangular image box at the top |
| 4 Mechanism p1 | How it works | **Often** | Large typography + supporting photo on half the slide |
| 5 Proof | Data / table | Often | Table or big stat next to contextual photo |
| 6 Expansion | The turn | **Always** | Background photo with dark overlay |
| 7 Application | Practical cases | **Always** | 3 horizontal cards with mini-images |
| 8 Direction | Pivotal direction | **Often** | Photo + overlay OR solid dark/light with hero typography. **Gradient only if visual refs suggest it.** |
| 9 CTA | Signature | May have bg | **Large centered logo/lockup** + short CTA |

Typically **7-8 slides with image** out of 9 total (vs 5 in previous V2). The carousel is more visual, with leaner text.

**Gradient**: stopped being mandatory on slide 8. Only used if the visual briefing decoded from `🖼️ Visual References` mentions a gradient as part of the system. Otherwise, slide 8 stays solid dark/light with a strong headline.

---

## Creative direction of the images inside the slide

> The slide is a composition: **design (typography, hierarchy, palette) + embedded high-impact image**. The carousel's quality is decided as much by the design as by the image. A generic image = a generic carousel, no matter how good the design.

Each slide with image needs an **image brief** that the Routine builds before the render. The brief is injected into the Higgsfield CLI prompt as a descriptive block of the image that must appear inside the slide.

### The 5 principles of the image brief

**1. Visual specificity (not vague adjectives)**
Don't write "beautiful image of technology". Write:
- **Specific colors** (saturated terracotta against desaturated petrol blue; or monochromatic warm-gray with 1 primary-color point)
- **Identifiable style** (35mm editorial photography, 2-color risograph illustration, matte 3D render, analog collage, etc.)
- **Defined lighting** (raking light from the right creating hard shadow; golden rim light against dark background; diffuse neutral catalog)
- **Camera angle** (frontal close-up, detail shot, overhead, dramatic low-angle)
- **Concrete elements** in the frame (not "a scene", but "a pair of hands typing on an old silver laptop on a dark wooden table with a coffee mug on the left")

**2. Purpose connected to the narrative**
Each image serves the slide's function. The brief makes explicit the feeling the image must convey:
- Hook slide → tension, visual contradiction, urgency
- Mechanism slide → revelation, "looking inside", before/after contrast
- Proof slide → authority, materiality of the data (paper, physical chart, screen)
- Expansion slide → scale, broader context, panoramic
- Application slide → humanity, gesture, ordinary moment
- CTA slide → brand signature, negative space, short CTA

**3. No ambiguity — clear visual metaphors**
Explicit metaphor > vague metaphor. Instead of "abstract idea of creativity", write "a hand holding a brush with dripping orange paint, touching a gray canvas". The AI renders what is described; it doesn't infer the abstract well.

**4. Faithful reinterpretation when there's a news hero**
When the news brings a hero image and the path is A or C, the image brief must **faithfully describe the content of the hero** (what's in it, what matters, what must be preserved) + **indicate the style of reinterpretation** (re-render as editorial 35mm, keep but with primary-color overlay, crop and isolate the main subject against a new background, etc.).

The Routine looks at the hero (real vision), describes it textually, sends the hero and the refs to Higgsfield with `higgsfield upload create`, and injects the UUIDs with `--image` together with the prompt — combining the two, it generates a stylized version coherent with the brand's visual system.

**5. The cover is ALWAYS very striking**
The cover is the slide that stops the scroll. Additional rules for it:
- **Cinematic composition** (rule of thirds, leading lines, depth, foreground/background separated by focus)
- **Dramatic lighting** (chiaroscuro, rim light, golden hour, harsh side light) — never diffuse neutral catalog
- **Single strong focal element** (a face, an object, a symbol) — not a scattered scene
- **Selective saturation** — desaturated background, focal point saturated in the brand's primary color
- **Narrative tension** — something is happening in the captured instant (movement, gesture, about to, on the brink of) — never static posed
- **Absolute anti-stock photo** — no corporate handshake, no laptop with glowing chart, no group smiling at the camera, no hands generically typing

### Master rule of image_brief — refs rule, subject obeys

Above the 5 principles, the principle that governs all of them: **each field of the image_brief is filled from the "Imagery style" and "Tonal register" of the decoded visual brief, not from a literal reading of the news.**

- `style` → copy the type of image from the refs (editorial photographic / human / object still / illustration). Never a style the refs don't have.
- `color_treatment` and `lighting` → respect the tonal register of the refs. Light refs → light lighting and color treatment. Don't darken.
- `subject` and `metaphor` → translate the news subject INTO the language of the refs. Refs with people → the subject has people. Editorial refs → the subject isn't a screenshot or diagram.
- `avoid` → always includes "any style, palette or luminosity that contradicts the brand's reference images".

When the news is about software/AI and the refs are humanized, the conflict ALWAYS resolves in favor of the refs: the image shows the human scene that represents the news's impact, not the product interface.

### image_brief schema per slide

Step 3 of the Routine prompt (Visual plan per slide) produces, for each slide with image:

```json
{
  "slide_N": {
    "path": "A | B | C",
    "hero_url": "...|null",
    "image_brief": {
      "purpose": "narrative tension of generational urgency",
      "subject": "an old Nokia 3310 phone fallen onto a café table next to a spilled cappuccino",
      "composition": "overhead 90°, objects in the lower third, negative space in the upper",
      "lighting": "natural side light, hard shadows, ~10am",
      "color_treatment": "dominant warm-gray + 1 terracotta-orange point in the spilled liquid",
      "style": "35mm editorial photography, fine grain, medium depth",
      "mood": "abandonment, silent rupture, pause",
      "metaphor": "a generation that hangs up the modern phone and stumbles on the analog one",
      "avoid": "no hands in frame, no face, no text over the image"
    }
  }
}
```

This JSON enters slide N's prompt as structured textual description.

### Variation by slide type

| Slide | Ideal image type | Base mood |
|---|---|---|
| 1 Cover | Cinematic, strong focal, dramatic | Maximum narrative tension |
| 2 Hook | Detail loaded with conflict | Unease |
| 3 Mechanism p1 | Diagram-object / setup / reveal | Attention, analytical focus |
| 4 Mechanism p2 | Before/after contrast OR close-up of process | Show how |
| 5 Proof | Materiality of the data (paper, screen, physical chart, printed number) | Authority, weight |
| 6 Expansion | Panoramic, scale, broad cultural context | Significance |
| 7 Application | Human, gesture, ordinary moment in diverse niche | Applicability |
| 8 Direction | Condensed symbol, visual sentence | Directional focus |
| 9 CTA | Large centered logo/lockup, short CTA below, quiet composition | Signature |

### image_brief block inside the slide's final prompt

When the Routine assembles the `higgsfield generate create` call's prompt, the block looks like this:

```
[decoded visual_brief block from the refs — already exists]

[NEW — image_brief block specific to this slide:]
Image embedded in this slide:
- Subject: {subject}
- Composition: {composition}
- Lighting: {lighting}
- Color treatment: {color_treatment}
- Style: {style}
- Mood: {mood}
- Metaphor: {metaphor}
- AVOID in the image: {avoid}

The image occupies {image_box_or_fullbleed_or_background}. The image is 
NOT generic stock — it is a specific, intentional visual that carries 
the slide's narrative function.

[rest of the prompt — slide composition, hierarchy, brand bar, etc.]
```

Result: the Higgsfield CLI does not receive "a generic AI image" in the slide's background field. It receives a specific, intentional visual direction.

---

## Decoding visual references — real vision + grid detection

Before generating the cover, the Routine reads `🖼️ Visual References` via the Notion MCP, downloads **all** attached images (typically 3 to 7, or a grid), and processes them with **native Claude session vision**.

**Grid detection:** each image is evaluated — is it unitary or is it a grid with multiple slides? If a grid (signals: spatial regularity, repeated borders, similar rectangles side by side), the Routine mentally decomposes it into N exemplars (3×3 grid = 9 refs; feed screenshot = 6+ refs) and observes each one separately. **A single good grid image is enough** — there's no need to require 5 separate images.

**Detail signature:** the Routine explicitly identifies which is the **repeated consistency element** across the observed exemplars (thin footer line with date, side micro-graphic, tiny tag, typographic signature). This detail signature enters the briefing as a dedicated section and is replicated on ALL 9 slides of the generated carousel, with no slide number.

```bash
# Inside the Routine session — Bash via tool:
mkdir -p ./state/$TODAY/refs/

# For each image URL extracted via the Notion MCP:
curl -fsS "$IMG_URL" -o "./state/$TODAY/refs/ref-01.jpg"
curl -fsS "$IMG_URL_2" -o "./state/$TODAY/refs/ref-02.jpg"
# ... etc
```

Then the session uses the **Read tool** on each downloaded image file. Claude has native vision — it sees the image directly, without needing a `claude --print --files` subprocess.

The briefing is compiled by the session itself (Claude describes what it saw) and saved at `./state/$TODAY/visual-brief.txt`.

### Fidelity to references — recurring errors to correct

Two errors appear frequently when R2 decodes the refs. The briefing must explicitly neutralize both:

**Error 1 — darkening what isn't dark.** R2 tends to pull the palette toward dark even when the refs are light, mid or colorful. This changes the identity of the feed. Correction:
- When observing each ref, record the **actual tonal register**: is the image predominantly light, mid or dark? What is the dominant luminosity of the background?
- If the refs are light/mid, the carousel is light/mid. **The dark/light rhythm of the Design System is subordinate to the refs** — if the refs don't have dark slides, don't invent dark slides.
- The slide backgrounds reproduce the luminosity observed in the refs, not a dark default.
- The briefing explicitly declares the approximate brightness of the backgrounds (e.g. "light slides background ~#F1ECE3, near-white; refs show no dark slides, keep the whole carousel light/mid").

**Error 2 — illustrating the subject literally.** R2 tends to generate a literal image of the news topic (news about an app → screenshot of the app) even when the refs show a different visual language (people, gesture, human scene, editorial photography). Correction:
- The **image style comes from the refs**, not from the subject. If the refs are humanized (people, hands, faces, real scenes), the carousel images are humanized — even though the news is about software.
- The news subject enters as a **visual metaphor in the refs' style**, not as a literal illustration.
- The briefing has an "Imagery style" section describing the type of image of the refs — and that section governs the image_brief of each slide.

### Structure of the decoded briefing

```
VISUAL BRIEF (decoded from references):

Color palette:
- Primary: {brand_color_primary} (warm orange, terracotta-leaning, slightly burnt)
- Background dark: {brand_color_dark}
- Background light: {brand_color_light}
- Accent secondary: [observed in references]

Tonal register / luminosity (CRITICAL — do not drift darker than the refs):
- Dominant register of the references: [light / mid / dark] — [describe]
- Background luminosity observed: [e.g. "backgrounds are near-white warm
  cream, ~90% luminance; NO dark slides present in refs"]
- Slide backgrounds for this carousel must match this register. If the refs
  are light/mid, the carousel is light/mid. Do NOT default to dark backgrounds.
- The dark/light rhythm from the Design System applies ONLY if the refs
  actually show both. Refs decide; the rhythm table does not override them.

TYPOGRAPHY LOCK (verbatim from 🖼️ Visual References — NOT re-derived):
- Display font (headlines): exact locked name + locked description
- Text font (body, tag, brand bar, signature): exact locked
  name + locked description
- The exact size/weight table — one fixed value per role, never a range.
This whole block is copied verbatim into EVERY slide prompt — same fonts,
weights and sizes on every slide of every carousel. Never paraphrase,
substitute or vary between slides.

Mood and atmosphere:
- Editorial, magazine-like, sober. References European design publications
  (Eye Magazine, Wallpaper, It's Nice That). Subtle film grain texture.

Imagery style (what KIND of image the refs use — overrides literal subject):
- Type of imagery in the refs: [editorial photography / humans & gesture /
  object stills / illustration / abstract texture / mixed — describe]
- If the refs are human/photographic, the carousel images are human/
  photographic too — even when the news is about software or an abstract
  topic. The news subject becomes a visual metaphor IN THIS STYLE, never a
  literal screenshot/diagram that contradicts the refs.
- Level of literalness observed: [literal depiction / metaphorical / editorial]

Composition style:
- Left-aligned text, generous negative space in upper portion,
  content anchored to lower two-thirds.
- Higher image-to-text ratio observed — 7 of 9 slides feature an image
  element. Text is concise — short headlines + 1-2 lines of body max.

Texture and finish:
- Subtle paper grain. No glossy or 3D elements.

Use of gradient:
- [Observed in refs / NOT observed in refs] — apply accordingly.
  If NOT observed, slide 8 stays dark or light solid with hero typography.

Detail signature / footer:
- Consistent element repeated across all 9 slides — [describe what was 
  observed in refs: e.g. "thin horizontal line at the very bottom with 
  date + handle text, e.g. '2026.05.14 · @humanacademy', font-size ~12px, 
  opacity 55%"]. This makes the feed feel curated.

What to AVOID:
- No emojis, no decorative icons, no stock photo aesthetic,
  no 3D effects, no glossy reflections, no generic gradients,
  no AI faces, no random abstract shapes, no Y2K, no neon glow.
```

The briefing is saved to `state/{TODAY}/visual-brief.txt` and is injected as a fixed block into **all** the prompts (cover and internal slides) of that run.

---

## Absolute rule — all slide text is rendered INSIDE the image

The carousel is generated as an **image with the text already integrated** — it is not a background image to receive text later. GPT Image 2 renders text inside the image; therefore, the prompt must be direct, integrated and faithful to the references. Every render call — cover and slides 2-9 — **must** contain, in the prompt, the exact copy blocks of that slide, transcribed literally.

**Never** generate a slide just with the visual briefing and the image_brief without the text. That produces a pretty empty image, which later can't receive the copy without rework.

### What enters the prompt of each slide, every time

For each slide N, the render prompt carries a block `═══ TEXT CONTENT (render this text inside the image) ═══` with:
- The slide's **tag** (uppercase, small) — slides 2-8
- The slide's **headline / internal title**, transcribed exactly as in `narrativa.json`
- **All body blocks** of that slide (text 3+4, 5+6, etc.), transcribed exactly
- The **keywords** that receive accent in the primary color
- Brand bar, handle and detail signature

On slide 9, the rule changes: the text block contains only the short CTA (`text 17`) and, if there's no logo, the textual/handle lockup (`text 18`). Do not render a tag, slide number, paragraph, summary, final question or additional body. The logo or `{brand_name}` must dominate the composition, with the CTA below in smaller hierarchy.

**Forbidden on any slide:** visible carousel number, counter, index, numbered dots, position marker or any textual pagination. The slide number exists only in the internal file/prompt, never in the final art.

The prompt explicitly instructs: *"Render ALL the text below as crisp, legible, correctly-spelled typography composed into the slide. The text is the primary content of this slide — not decoration. Do not paraphrase, do not omit any block, do not invent text that is not listed."*

### Mandatory post-render verification

After downloading each slide, the Routine **opens the PNG with the Read tool (vision)** and checks:
- [ ] All slide copy blocks appear in the image
- [ ] The text is legible and free of spelling errors
- [ ] No text was cut off by the edge

If a slide came back **without the text** or with illegible/cut/swapped text → counts as a **render failure** → re-runs that slide (up to 2x). A slide without the integrated copy is never accepted as final.

---

## Absolute rule — slide dimension via Higgsfield CLI

Higgsfield may return files larger than 1080px (e.g. ~1856px). That's fine. The carousel delivers the original PNG downloaded from Higgsfield, without downscale, crop, resize or conversion to 1080×1350.

**1. Every render call — cover and slides 2-9 — passes explicit CLI flags.**

```bash
--aspect_ratio "3:4" --resolution "2k" --quality high
```

Never omit these flags. Never trust the default. Never use a legacy fixed-size parameter: that was old-provider instruction, not the current Higgsfield CLI.

**2. Why 3:4 and not 4:5 directly.** The current CLI does not accept `4:5` as `--aspect_ratio`. Use `3:4` and keep the returned file. Don't convert to 4:5 afterwards.

**3. The prompt reinforces the format.** The first line of every slide prompt declares: *"A portrait Instagram carousel slide, aspect ratio 3:4."* This prevents the model from drifting into square or landscape suggesting a later crop.

**4. Post-download validation — no squish.** After downloading each PNG, read the dimensions (Pillow):
- Came back at proportion **3:4** → ok, proceed.
- Came back at a proportion other than **3:4** (square, landscape, cropped) → it's a **render failure**. Re-run the slide (up to 2x). **NEVER force a PNG of the wrong proportion into another size — that squishes the image and distorts it.**

**5. Logo composition without changing dimension.** When you need to apply the logo to slides 1 and 9, use Pillow only to compose the logo over the original PNG, keeping the width, height and aspect ratio of the downloaded file.

---

## Step 1 — Cover generation (slide 1)

### Which command

The cover ALWAYS goes with the brand refs as `--image` UUIDs — it's what anchors aesthetic and font. Use the Higgsfield CLI on both paths:

| Path | Command | References |
|---------|----------|--------------|
| B — no news photo | `higgsfield generate create gpt_image_2` | brand refs |
| A or C — with news photo | `higgsfield generate create gpt_image_2` | news photo + brand refs |

Rare fallback: if the brand has NO ref attached, use the same command without `--image`.

### Path B call (Bash inside the Routine)

Path B = no news photo. But the cover ALWAYS receives the brand refs as UUIDs:

```bash
REF_FLAGS=$(cat ./state/$TODAY/higgsfield-ref-flags.txt)
COVER_JOB=$(higgsfield generate create gpt_image_2 \
  --prompt "$PROMPT_CAPA" \
  $REF_FLAGS \
  --aspect_ratio "3:4" \
  --resolution "2k" \
  --quality high \
  --json | grep -oiE '[0-9a-f-]{36}' | head -1)

COVER_JSON=$(higgsfield generate wait "$COVER_JOB" --timeout 30m --json)
COVER_URL=$(echo "$COVER_JSON" | grep -oE 'https://[^ "]+\\.(png|jpg|jpeg|webp)' | head -1)
echo "$COVER_URL" > ./state/$TODAY/cover-url.txt
```

### Path A/C call (with news photo)

The news photo enters first as a UUID, followed by the brand refs:

```bash
NEWS_UUID=$(higgsfield upload create "./state/$TODAY/news-hero.jpg" | grep -oiE '[0-9a-f-]{36}' | head -1)
REF_FLAGS="--image $NEWS_UUID $(cat ./state/$TODAY/higgsfield-ref-flags.txt)"
COVER_JOB=$(higgsfield generate create gpt_image_2 \
  --prompt "$PROMPT_CAPA" \
  $REF_FLAGS \
  --aspect_ratio "3:4" \
  --resolution "2k" \
  --quality high \
  --json | grep -oiE '[0-9a-f-]{36}' | head -1)
```

### Cover prompt template

```
A portrait Instagram carousel cover slide, aspect ratio 3:4.

{VISUAL_BRIEF_DECODED}

Internal role: COVER. Do not draw any page index, carousel counter, sequence marker or visible slide number.
It establishes the visual identity for the entire carousel. The cover MUST be visually arresting — magazine
cover quality, the kind of image that stops the scroll.

═══ EMBEDDED IMAGE (full-bleed background) ═══
{IMAGE_BRIEF_DA_CAPA}

The embedded image carries the cover. Treat it with cinematic care:
- Composition: {composition} — strong focal point, rule of thirds,
  leading lines if applicable, foreground/background separated by focus
- Lighting: {lighting} — dramatic (chiaroscuro, rim light, golden hour, 
  or harsh side light). NEVER flat catalog lighting.
- Color: {color_treatment} — selective saturation: muted backdrop, 
  saturated focal point ideally in {brand_color_primary}
- Style: {style} (editorial 35mm photo / risograph illustration / 
  matte 3D render / analog collage / etc — never generic AI gloss)
- Mood: {mood} — narrative tension. Something is happening or about to.
- Metaphor: {metaphor}

═══ COVER COMPOSITION ═══
- Full-bleed image background as described above
- Heavy dark gradient overlay at the bottom 55-60% to ensure 4.5:1 
  contrast against headline
- Thin accent bar (6px) at the very top in {brand_color_primary}
- {LOGO_INSTRUCTION_IF_HAS_LOGO}
- Headline anchored in lower 35% of canvas, left-aligned, generous 
  left margin (~80px)
- Handle "{brand_handle}" small, above the headline block

═══ TEXT CONTENT — render ALL of this text inside the image ═══
This text is the primary content of the cover, not decoration. Render it
as crisp, legible, correctly-spelled typography. Do not omit, paraphrase
or invent text.
- Brand bar (very top, small, low opacity): 
  "BY {brand_name}  |  {brand_handle}  |  2026"
- Handle: "{brand_handle}"
- Headline (largest element, bold condensed uppercase, tight kerning):
  "{HEADLINE_DA_CAPA}"
- Highlight in {brand_color_primary}: {KEYWORD_LIST}

═══ TYPOGRAPHY LOCK — use EXACTLY these fonts, verbatim ═══
{TYPOGRAPHY_LOCK_BLOCK}
(copied verbatim from the locked font system in 🖼️ Visual References:
the 2 fonts and the exact size/weight table. Same fonts, weights and sizes
on every slide of every carousel — never substitute, never vary.)

═══ DETAIL SIGNATURE ═══
{DETAIL_SIGNATURE_DESCRIBED_IN_VISUAL_BRIEF}
(footer consistency element repeated across all 9 slides)

═══ ABSOLUTE NO-GO ═══
Do NOT include: emojis, decorative icons, stock photo aesthetic, 
3D glossy effects, lens flares (unless cinematic intent), generic 
gradients, AI-rendered faces with uncanny features, corporate 
handshakes, smiling group photos to camera, hands typing generically 
on laptop, lightbulb-as-idea cliché, gears-as-strategy cliché.

═══ MOOD TARGET ═══
This cover should look like it was art-directed by a design magazine —
not generated by AI. Confidence. Sharpness. Specificity. Tension.
```

Download the PNG locally and keep the original size returned by Higgsfield:

```bash
curl -fsS "$COVER_URL" -o ./state/$TODAY/slides/slide-01-raw.png
uv run --with pillow python3 -c "
from PIL import Image
img = Image.open('./state/$TODAY/slides/slide-01-raw.png').convert('RGBA')
w, h = img.size
ratio = round(w / h, 3)
# 3:4 = 0.75. Any other proportion is a render failure — re-run the cover.
assert abs(ratio - 0.75) < 0.01, f'WRONG PROPORTION {w}x{h} (ratio {ratio}) — re-run the cover, DO NOT force resize'
# If brand_has_logo=true, apply the logo on a final copy without changing w/h.
# The logoless cover stays at slide-01-raw.png and will be used as a reference for the internals.
img.convert('RGB').save('./state/$TODAY/slides/slide-01.png', quality=95)
"
```

If the `assert` fires, the cover came back with the wrong proportion → re-run the cover (do not proceed to slides 2-9 with a distorted cover). Do not crop, resize or downscale. The `slide-01-raw.png` copy must remain, because it becomes the logoless cover reference for the internal slides.

> **Classic bug:** capturing a filesystem URL instead of the render response. **Always write `cover-url.txt` IMMEDIATELY** after capturing the response from `generate wait`. Slides 2-9 depend on it.

---

## Step 2 — Slides 2-9 (parallel with cover + refs)

Slides 2-9 are generated in **parallel**. Each slide references the generated cover and all the brand's visual references. Do not use the previous slide as reference: that makes the task slow and makes the visual depend on a link that may have come out weak.

All use `higgsfield generate create gpt_image_2`. The references enter as `--image` UUIDs.

**References of each internal slide (`--image`):**
- **Slides 2-9** → `[logoless cover]` + **all brand refs**.
- Any slide that uses the news photo (Path A/C) appends `hero_url` at the end.
- The logo never enters as `--image` (it enters via Pillow on slide 9).

**Why cover + refs on every one:** the cover gives the final direction already generated; the visual refs bring image, typography and composition repertoire that the cover alone doesn't carry. This way, the internal slides can run together and still keep the aesthetic.

The Notion refs are downloaded locally and sent to Higgsfield with `higgsfield upload create`. The finished slides come from the `url-N.txt` files returned by Higgsfield.

```bash
COVER_UUID=$(higgsfield upload create "./state/$TODAY/slides/slide-01-raw.png" | grep -oiE '[0-9a-f-]{36}' | head -1)
BASE_REF_FLAGS="--image $COVER_UUID $(cat ./state/$TODAY/higgsfield-ref-flags.txt)"

for N in 2 3 4 5 6 7 8 9; do
  (
  PROMPT_FILE="./state/$TODAY/prompts/slide-$N.txt"
  REF_FLAGS="$BASE_REF_FLAGS"
  # If the visual-plan marks Path A/C, append the news hero UUID here.

  JOB=$(higgsfield generate create gpt_image_2 \
    --prompt "$(cat "$PROMPT_FILE")" \
    $REF_FLAGS \
    --aspect_ratio "3:4" \
    --resolution "2k" \
    --quality high \
    --json | grep -oiE '[0-9a-f-]{36}' | head -1)

  RESP=$(higgsfield generate wait "$JOB" --timeout 30m --json)
  SLIDE_URL=$(echo "$RESP" | grep -oE 'https://[^ "]+\\.(png|jpg|jpeg|webp)' | head -1)
  echo "$SLIDE_URL" > "./state/$TODAY/url-$N.txt"

  # download and validate 3:4 ratio; keep the original Higgsfield size
  curl -fsS "$SLIDE_URL" -o "./state/$TODAY/slides/slide-0$N.png"
  uv run --with pillow python3 - <<PY
from PIL import Image
img = Image.open("./state/$TODAY/slides/slide-0$N.png")
w, h = img.size
assert abs(w/h - 0.75) < 0.01, f"WRONG PROPORTION {w}x{h} — re-run slide $N, DO NOT force resize"
PY
  ) &
done
wait
```

**Parallel robustness:** if a slide fails even after the retries (500/502), mark only that slide as a failure. The others don't depend on it and continue.

Expected total time: **1-3 min** for the 8 internal slides in parallel, depending on queue/model.

---

## Error handling

| Error | Action |
|---|---|
| `higgsfield: command not found` | Install `@higgsfield/cli` and stop the run |
| Missing login | Run `higgsfield auth login`, then `higgsfield account status` |
| Rate limit | `sleep 5` between calls |
| Insufficient credits | Top up the Higgsfield account |
| Invalid aspect ratio | Use `--aspect_ratio "3:4"` and download the original PNG; if it comes in another proportion, re-render |
| 5xx/timeout error | Retry up to 2x. If it persists, mark the slide as failed; does not block others |
| Timeout >60s | Cancel, retry once |
| No URL in `generate wait` output | Log raw output for debug, mark slide as failed |

**Parallel:** slides 2-9 do not depend on each other. Each uses cover + visual refs. If a slide fails after the retries, the others continue and the final caption lists which slides failed.

---

## Cost

Costs depend on the model and the credits of the active Higgsfield account. Before a real render, run:

```bash
higgsfield account status
```

Recommendation:
- iterate a little before render;
- generate only necessary variations;
- log model, job_id and attempt;
- stop if the account indicates insufficient credits.

---

## Attach slides to Notion via files/URLs returned by Higgsfield

The Routine can pass the Higgsfield-returned URL as `external.url` in the PATCH to the entry via the Notion MCP, and must also save a local + Drive backup:

```python
# Conceptual — the Routine uses native Notion MCP tools:
notion.pages.update(carousel_page_id, properties={
  "Slides": {
    "files": [
      {
        "name": f"slide-{i:02d}.png",
        "type": "external",
        "external": {"url": cover_url if i == 1 else slide_urls[i-2]}
      }
      for i in range(1, 10)
    ]
  }
})
```

Advantages:
- Appears **immediately** in Notion (no upload)
- Doesn't blow up the session context (no base64)
- External URLs appear quickly in Notion
- Drive becomes an independent backup via MCP (parallel, does not block Notion)

---

## Re-render — cheap flow

When the editorial pipeline is OK but the visual came out weak:

**Option A — in the active session:**
```
> --re-render
```

**Option B — Run now in the panel:**
```
[Routine] → Run now → "--re-render"
```

The Routine:
1. Reads `state/$TODAY/narrativa.json` (already-validated narrative architecture; if only an old snapshot exists, migrate to the new name before proceeding)
2. Reads `state/$TODAY/visual-plan.json`
3. Re-runs the visual brief (re-runs vision on the refs, may capture changes)
4. Re-runs render (cover first; slides 2-9 in parallel with cover + refs)
5. PATCH on the existing Notion entry (same page, replaces Slides)
6. Increments `Render attempts` on the entry

Cost: check Higgsfield credits before re-rendering. Time: depends on queue/model.

When to use `--re-render`:
- Visual ended up generic → edited `🖼️ Visual References`, regenerate
- Color came out wrong → adjusted `🏷️ Brand Identity`, regenerate
- Slides 2-9 not coherent with cover → redo with more restricted prompts/refs

When NOT to use `--re-render` (use a new run):
- Copy ended up weak → adjust `📚 Editorial Manual`, run full
- Chosen news was bad → `--news=N` to override

---

## Execution order by the Routine (summary)

```
1. Reads 🏷️ Brand Identity → hydrates variables
2. Reads 🖼️ Visual References (via Notion MCP) → image URLs
3. Bash curl downloads images to state/$TODAY/refs/
4. Read tool on images (native vision) → compiles visual brief as text
5. Saves state/$TODAY/visual-brief.txt
6. Reads validated narrative architecture (`state/$TODAY/narrativa.json`; if only an old snapshot exists, migrate to the new name before proceeding)
7. Reads visual plan (state/$TODAY/visual-plan.json)
8. Generates cover via Higgsfield CLI with brand refs as `--image` UUIDs
9. Captures cover URL from output, saves to state/$TODAY/cover-url.txt
10. Downloads PNG, validates 3:4 proportion and keeps the original size returned by Higgsfield
11. Slides 2-9 in PARALLEL:
    - Higgsfield CLI; all use [logoless cover] + brand visual refs (+ hero when applicable)
    - Each saves url-N.txt and slide-0N.png independently
12. PATCH on Notion entry via MCP with external URLs (no upload)
13. Google Drive MCP upload in parallel (does not block)
14. Marks .completed in state/$TODAY/
```

**Average time:** 6-10 min total (2-4 min editorial pipeline + 1-2 min vision brief + 30s cover + 1-3 min internal slides in parallel + 30s Notion patch + 30s Drive backup).
