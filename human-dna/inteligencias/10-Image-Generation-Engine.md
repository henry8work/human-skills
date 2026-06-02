# 10 — Image Generation Engine

> **Master document of the AI image generation discipline.** Written with the authority of a senior prompt engineer + AI art director. In the Human Agent Lab, real image generation uses Higgsfield CLI + Nano Banana 2 (`nano_banana_2`); other references serve only as conceptual and historical repertoire.
>
> This file is the image generation reference for the ENTIRE system. The Maestro consults it before generating any piece via AI, before auditing a generated image, before deciding between engines.

---

## Table of contents

0. **Doctrine** — authority and premise
1. **Reference literature** — papers, repositories, blogs
2. **The 12 founding principles**
3. **Generation stack** — engine choice by context
4. **The 5 image brief principles** (prompt structure)
5. **Canonical templates by piece type**
6. **Branding with AI** (logo placements, character/product consistency)
7. **3-stage pipeline** (Visual Intent → Generation → Polish)
8. **What is a GOOD vs BAD AI image**
9. **What is FAST vs SLOW generation** (cost + time)
10. **What WORKS vs DOESN'T WORK** in production
11. **What SELLS vs REPELS** (commercial application)
12. **Generative AI anti-patterns**
13. **Costs and quality tiers**
14. **Error handling**
15. **When the Maestro should call me**
16. **Operational checklist**

---

## 0. Doctrine

AI image generation is the biggest technical shift in visual production since digital replaced analog in the 90s. In 2026, a small brand can produce premium-quality images in minutes, at a cost of pennies. But the curve is treacherous: **cheap tools easily generate generic images; generating an image that looks intentional, professional and unique requires direction as specific as traditional photography.**

The biggest difference between a brand that uses AI well and a brand that uses AI poorly isn't the tool — it's direction. Higgsfield CLI can render high-level images and video, but if the brief is "a beautiful nature scene", the output is generic stock. If the brief is "golden light at 5pm in Tuscany, old stone terrace, half-full wine glass in the foreground, open book lying down, page folded at the corner, blurred waves of olive trees in the background, warm air with suspended particles, warm naturalist color grade" — the output can be editorial.

Every decision in this document starts from a premise: **prompt is creative direction, not command**. Prompt engineering = engineering of clear, complete, hierarchical instruction with real references. Whoever writes prompts like writing a professional photographer's briefing generates professional images. Whoever writes "make a beautiful image of X" gets what they asked for: generic beauty.

---

## 1. Reference literature

### Fundamental academic papers

- **Ramesh et al.** — *Hierarchical Text-Conditional Image Generation with CLIP Latents* (2022). Historic paper on CLIP and generation.
- **Saharia et al.** — *Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding* (2022). Imagen paper.
- **Rombach et al.** — *High-Resolution Image Synthesis with Latent Diffusion Models* (2022). Stable Diffusion paper.
- **Podell et al.** — *SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis* (2023).
- **Technical reports of image models** — used only as conceptual repertoire.

### Prompt engineering (living texts, updated frequently)

- **Anthropic Prompt Engineering Guide** (docs.anthropic.com). Universal LLM prompting principles applicable to image-gen.
- **Riley Goodside** (@goodside on X) — living reference in prompt engineering.
- **Simon Willison** (simonwillison.net) — continuous technical blog on LLMs and generation.
- **Ethan Mollick** (oneusefulthing.org) — practical application of creative AI.
- **Lex Fridman** podcast (interviews with OpenAI, Anthropic, DeepMind researchers).
- **Andrej Karpathy** — "Intro to LLMs" and "Tokens" lectures.

### Reference communities and galleries

- **Prompt galleries and visual showcases** — used only for repertoire, never as operational engine.
- **Civitai** — Stable Diffusion + LoRAs community.
- **Promptbase** — prompt marketplace (curiosity, not definitive source).
- **r/midjourney**, **r/StableDiffusion**, **r/ChatGPT** — living communities.
- **Visual generation communities** — source of repertoire and quality standards.

### Official engine documentation (absolute reference)

- **Higgsfield CLI docs/internal manual** — models, parameters, ref upload, generate/wait
- **Higgsfield CLI docs/internal manual** — models, parameters, ref upload, generate/wait
- **Stability AI** — SDXL, SD 3.5
- **External visual tools documentation** — only repertoire and historical comparison
- **Runway** (runwayml.com/docs) — Gen-3 Alpha video
- **Sora API** (sora.openai.com) — OpenAI video
- **Kling AI** — high-quality Chinese video
- **Luma Dream Machine** — video
- **Higgsfield AI** — video with camera control

### Reference technical blogs

- **fxguide.com** — VFX + AI technique
- **AI Filmmaking** (Caleb Ward, Curious Refuge)
- **AndrewMayneblog** — OpenAI insider
- **Replicate blog** (replicate.com/blog)

### Brazilian references in creative AI

- **Felipe Ueno** — Brazilian engineer publishing about generative AI infrastructure
- **Stormy AI community** — Brazilian creative agents
- **Renan Vieira** — design + AI
- Human Academy, AI Video Lab, Agent Lab workshops

> Whoever uses an AI engine without having read the engine's official documentation is guessing. Each model has specific parameters, specific anti-prompts, known behaviors.

---

## 2. The 12 founding principles

### Principle 1 — Prompt is briefing, not command

The difference between amateur prompt and professional prompt is in the amount of **specific direction embedded**. Amateur prompt: "make a beautiful sunset". Professional prompt: "Editorial photograph, golden hour 35mm, 17:30 light angle, Mediterranean coastal town, terracotta rooftops in foreground out-of-focus, sea horizon middle ground, distant mountains backdrop, color grade warm naturalistic, slight haze, shot on Leica Q with 28mm Summilux".

The difference isn't in the model — it's in the richness of the briefing. The same model generates both.

### Principle 2 — Specificity > volume

A long prompt isn't always better. A **dense** prompt always is. Every word of the prompt should carry direction. Vague adjectives ("beautiful", "amazing", "stunning") are token waste — they take up space without giving instruction.

A 50-word dense prompt beats a 200-word prompt with 80% empty adjectives.

### Principle 3 — Real references anchor the output

Image models were trained on millions of cataloged photos. Citing real references (photographers, films, magazines, places) activates rich associations that generic adjectives can't.

> Vague: "moody portrait"
> Anchored: "portrait in style of Peter Lindbergh, black-and-white, 35mm Tri-X grain, environmental light from window left, subject contemplative not posed, reminiscent of Vogue Italia editorial 1990s"

### Principle 4 — Hierarchical prompt structure

Models respond to hierarchy. A well-structured prompt has order:

1. **Piece type** (photograph / illustration / 3D render / poster)
2. **Main subject** (what is in focus)
3. **Action/moment** (what is happening)
4. **Setting** (where)
5. **Lighting** (how it's lit)
6. **Composition** (framing, angle, shot)
7. **Style/treatment** (aesthetic, color grade, grain)
8. **References** (artist/photographer/film)
9. **Technical** (camera, lens, aspect ratio, quality)
10. **Negative prompt** (what NOT to include)

Inversion of that order confuses the model. Put the most important first.

### Principle 5 — Negative prompt is as important as positive

What does NOT appear defines the image as much as what does. Negative prompt steers the model away from generic defaults:

> Negative: "stock photo aesthetic, generic smiling, corporate handshake, lens flare without intent, AI faces with uncanny features, hands with extra fingers, text on signs, watermarks"

Without negative prompt, the model tends to the generic average.

### Principle 6 — Visual reference (image-to-image) trumps text alone

When there's a reference image, **upload with `higgsfield upload create` and pass the UUID as `--image`**. The model understands visual context with precision that text alone can't reach. Color, composition, mood captured visually, not verbalized.

Use 3-7 references as a base when there's enough material.

### Principle 7 — Iteration is part of the process

Almost never is the first generation the final. Real pipeline:
1. Initial generation (4 variations, low quality to explore) — $0.05-0.10 total
2. Select the best direction
3. Generate 4 variations of the chosen one (medium quality) — $0.20-0.30
4. Select the final
5. Generate in high quality + upscale + polish — $0.50-1.00

Total cost ~$1-1.50 per excellent final image. Compare with photographer: R$2,000-15,000 per session.

### Principle 8 — Character consistency is a technical problem

Keeping the same character (model, mascot, founder) across multiple images is the hardest problem in generative AI. Solutions:

- **Master shot + image-to-image:** generate 1 excellent master, use as reference in all the next ones
- **Higgsfield CLI + Nano Banana 2:** use 1-3 anchor images as `--image` in all next generations
- **Anchor sheet:** create a master character/product sheet and reuse as reference
- **Variation control:** change one variable per iteration so as not to lose identity

### Principle 9 — Text inside the image is treacherous

Text inside the image still requires review. Even with Nano Banana 2, check every character. Strategies:

- **Render text separately in design tool** (Figma, then compose)
- **Keep text short** when it needs to come in the render
- **Inpaint/re-render** the correct text in a second pass
- **Logo via Pillow** (never let AI "draw" a logo — distorts)

### Principle 10 — Official image engine

In the Human Agent Lab, all real image generation uses **Higgsfield CLI + Nano Banana 2 (`nano_banana_2`)**. Other tools may appear as conceptual reference or historical comparison, but not as operational training flow.

### Principle 11 — Polish is half the work

Initial generation is raw. Professional polish includes:
- **Upscale** (clarity-upscaler, Topaz Photo AI) — 2x-4x resolution
- **Inpainting** (correct hands, faces, details)
- **Color correction** (LUTs, fine adjustments in Lightroom/Photoshop)
- **Final composition** (logo, text, layout in design tool)

Well-made AI image goes through 3-5 polish stages, not 1.

### Principle 12 — AI anti-patterns are detectable

The design community has trained its eye to detect badly-done AI. Signs:
- Hands with 6 fingers or wrong anatomy
- Glazed eyes, strange symmetry
- Incoherent text on signs/posters
- Inconsistent shadows (light in contradictory direction)
- Physically impossible reflections
- Very plastic skin
- Background with melting objects

A good AI image hides that it's AI. A brand that publishes obvious AI loses credibility.

---

## 3. Generation stack — official engine by context

### 3.1 — Decision by piece type

| Piece type | Recommended engine | Why |
|---|---|---|
| **Photorealistic hero shot** | Higgsfield CLI + Nano Banana 2 | Photorealism + atmosphere with refs |
| **Carousel cover with text** | Higgsfield CLI + Nano Banana 2 | Composition + reviewable short text |
| **Slide with text + photo** | Higgsfield CLI + Nano Banana 2 | Visual layout with brand refs |
| **Person in realistic context** | Higgsfield CLI + Nano Banana 2 | Consistency via image refs |
| **Consistent character in series** | Higgsfield CLI + Nano Banana 2 | Anchor sheet + recurring refs |
| **Illustration / visual vector** | Higgsfield CLI + Nano Banana 2 | Visual art direction; final vector can be redrawn if needed |
| **Icon / symbol** | Higgsfield CLI + Nano Banana 2 | Visual concept; final vector production if needed |
| **Poster with strong typography** | Higgsfield CLI + Nano Banana 2 | Short text + mandatory QA |
| **Premium product shot** | Higgsfield CLI + Nano Banana 2 | Visual Intent + refs + polish |
| **Fashion editorial** | Higgsfield CLI + Nano Banana 2 | Atmosphere + physical style by prompt |
| **Natural lifestyle** | Higgsfield CLI + Nano Banana 2 | Realism + composition |
| **Abstract / artistic** | Higgsfield CLI + Nano Banana 2 | Artistic versatility |
| **Video / motion frame** | Higgsfield CLI + Nano Banana 2 | Still frames; motion uses video product when applicable |

### 3.2 — Decision by budget (cost per generation)

| Tier | Cost per image | Engines |
|---|---|---|
| **Low** | Nano Banana 2 at `1k` | Quick iteration, exploration |
| **Mid** | Nano Banana 2 at `2k` | Internal approval and premium standard |
| **High** | Nano Banana 2 at `4k` when requested | Final version when extreme detail is required |
| **Premium** ($0.10-0.50) | Upscale + multiple iteration + polish | Hero campaign, important cover |

Video:
- **Runway Gen-3** — ~$0.05/second
- **Sora** — ~$0.10-0.30/second
- **Kling** — ~$0.05-0.15/second

### 3.3 — Decision by speed

| Speed | Configuration | Use case |
|---|---|---|
| **Fast** | Nano Banana 2 at `1k` | Live iteration |
| **Medium** | Nano Banana 2 at `2k` | Standard production |
| **Slow** | Nano Banana 2 at `4k` + polish | Final version when needed |

---

## 4. The 5 image brief principles

Every image generated via AI needs a structured **image brief**. The 5 principles:

### 4.1 — Visual specificity (not vague adjectives)

Don't write "beautiful image of technology". Write:
- **Specific colors** (saturated terracotta against desaturated petrol-blue; or monochromatic warm gray with 1 primary color point)
- **Identifiable style** (35mm editorial photography, 2-color risograph illustration, matte 3D render, analog collage)
- **Defined lighting** (raking light from the right side creating hard shadow; golden rim light against dark background; neutral catalog diffuse)
- **Camera angle** (frontal close-up, detail shot, overhead, dramatic low-angle)
- **Concrete elements** in the frame (not "a scene", but "a pair of hands typing on an old silver laptop on a dark wooden table with a coffee cup on the left")

### 4.2 — Purpose connected to narrative

Each image serves a narrative function. Brief makes the feeling explicit:

- Hero / cover → narrative tension, urgency
- Mechanism → revelation, "looking inside", before/after contrast
- Proof → authority, materiality of the data (paper, physical chart, screen)
- Expansion → scale, larger context, panoramic
- Application → humanity, gesture, ordinary moment
- CTA / closing → condensed symbol, symbolic closure

### 4.3 — Without ambiguity — clear visual metaphors

Explicit metaphor > vague metaphor. Instead of "abstract idea of creativity", write "a hand holding a brush with orange paint dripping, touching gray canvas". The AI renders what's described; doesn't infer the abstract well.

### 4.4 — Faithful reinterpretation when there's reference

When there's a reference photo, the brief needs to **faithfully describe the content of the reference** + **indicate the style of reinterpretation**. R2 looks at the reference (real vision), describes it textually, and injects that description + style directive.

### 4.5 — Cover ALWAYS very eye-catching

The cover is the slide/piece that stops the scroll. Additional rules:

- **Cinematic composition** (rule of thirds, leading lines, depth)
- **Dramatic lighting** (chiaroscuro, rim light, golden hour, harsh side light) — never neutral diffuse
- **Single strong focal element** (one face, one object, one symbol)
- **Selective saturation** — desaturated background, saturated focal point
- **Narrative tension** — something is happening in the instant
- **Absolute anti-stock photo**

---

## 5. Image brief schema (structured JSON)

Every piece produced via AI first generates a structured JSON:

```json
{
  "engine": "higgsfield_cli/nano_banana_2",
  "purpose": "narrative tension of generational urgency",
  "subject": "an old Nokia 3310 phone fallen on a coffee table next to a spilled cappuccino",
  "composition": "overhead 90°, objects in the lower third, negative space in the upper",
  "lighting": "natural lateral light, hard shadows, ~10am",
  "color_treatment": "predominant warm-gray + 1 orange-terracotta point in the spilled liquid",
  "style": "35mm editorial photography, fine grain, medium depth",
  "mood": "abandonment, silent rupture, pause",
  "metaphor": "generation that turns off the modern phone and trips over the analog",
  "avoid": "no hands in the frame, no face, no text over the image",
  "reference_images": ["url1", "url2"],
  "dimensions": {"width": 1088, "height": 1360},
  "resolution": "2k"
}
```

This JSON is built by R2 and injected into the final prompt.

---

## 6. Canonical prompt templates

### 6.1 — Hero / Cover (full-bleed, dramatic)

```
A {dimensions.width}x{dimensions.height} {format_descriptor} hero/cover image.

{VISUAL_BRIEF_DECODED}

This is a HERO image. It MUST be visually arresting — magazine cover quality, the kind of image that stops the scroll.

═══ EMBEDDED IMAGE (full-bleed background) ═══
{image_brief.subject}

Composition: {image_brief.composition} — strong focal point, rule of thirds, leading lines if applicable, foreground/background separated by focus

Lighting: {image_brief.lighting} — dramatic (chiaroscuro, rim light, golden hour, or harsh side light). NEVER flat catalog lighting.

Color: {image_brief.color_treatment} — selective saturation: muted backdrop, saturated focal point ideally in {brand_color_primary}

Style: {image_brief.style} — never generic AI gloss

Mood: {image_brief.mood} — narrative tension. Something is happening or about to.

Metaphor: {image_brief.metaphor}

═══ COMPOSITION ═══
- Full-bleed image background as described above
- Heavy dark gradient overlay at the bottom 55-60% to ensure 4.5:1 contrast against headline
- Thin accent bar (6px) at the very top in {brand_color_primary}
- {LOGO_INSTRUCTION_IF_HAS_LOGO}
- Headline anchored in lower 35% of canvas, left-aligned, generous left margin (~80px)
- Handle "{brand_handle}" small, above the headline block

═══ TEXT CONTENT ═══
- Brand bar (very top, small, low opacity): "BY {brand_name}  |  {brand_handle}  |  {year}"
- Handle: "{brand_handle}"
- Headline (largest element, bold condensed uppercase, tight kerning): "{HEADLINE_OF_THE_COVER}"
- Highlight in {brand_color_primary}: {LIST_OF_KEYWORDS}

═══ TYPOGRAPHY ═══
- Headline: bold condensed sans-serif, weight 900, 88-108px, uppercase, letter-spacing -3px, line-height 0.95 (similar in feel to: {brand_font_display})
- Handle: clean sans-serif, weight 600, 18px

═══ DETAIL SIGNATURE ═══
{DETAIL_SIGNATURE_DESCRIBED_IN_VISUAL_BRIEF}
(footer consistency element repeated across all pieces of this batch)

═══ ABSOLUTE NO-GO ═══
{image_brief.avoid}
+ universal no-go from brand:
Do NOT include: emojis, decorative icons, stock photo aesthetic, 3D glossy effects, lens flares (unless cinematic intent), generic gradients, AI-rendered faces with uncanny features, corporate handshakes, smiling group photos to camera, hands typing generically on laptop, lightbulb-as-idea cliché, gears-as-strategy cliché.

═══ MOOD TARGET ═══
This image should look like it was art-directed by a design magazine ({brand_aesthetic_anchor}) — not generated by AI. Confidence. Sharpness. Specificity. Tension.
```

### 6.2 — Internal slide / Post body

```
A {dimensions.width}x{dimensions.height} {format_descriptor} content image.

{VISUAL_BRIEF_DECODED}

This is slide [N] of [TOTAL] — the {section_function}. NOT a cover.

Match the visual STYLE (palette, typography, composition, footer detail signature) of the cover and brand reference images, but show DIFFERENT content. Use reference for visual consistency, not for copying content.

═══ EMBEDDED IMAGE ═══
[specific image_brief block — see schema above]

═══ COMPOSITION ═══
- Background: {dark|light|gradient}
- Tag at top: "{tag_text}" in mono, weight 700, 13px, uppercase, letter-spacing 3px, color {tag_color}
- Body text in {body_position} third of canvas, left-aligned
- Brand bar at very top: handle + 0X/0Y counter

═══ TEXT CONTENT (KEEP MINIMAL — 2 short blocks max) ═══
text A: "{text_block_a}"
text B: "{text_block_b}"

═══ ABSOLUTE NO-GO ═══
{universal_no_go} + slide-specific {avoid_list}
```

### 6.3 — Branding placement (logo in context)

```
A photograph showing the {brand_name} logo / product naturally integrated into an unexpected real-world context.

═══ THE PLACEMENT ═══
Context: {unexpected_context}
   (Examples: 
    - "logo painted on the side of an old delivery truck stopped at a traffic light in São Paulo's Vila Madalena, 1998 morning light"
    - "logo as a tattoo on a man's forearm, holding an espresso cup, café table in Lisbon, golden hour"
    - "logo printed on a vintage book cover, lying on a wooden desk with a pair of tortoise-shell glasses on top")

═══ THE BRAND ELEMENT ═══
Logo / element: {brand_logo_description}
Position in frame: {composition_placement}
Imperfections: include realistic wear, fade, lighting interaction with surface texture. The logo should feel like it has BEEN there for a while — not photoshopped onto the scene yesterday.

═══ COMPOSITION ═══
- Lighting: {chosen_setup_from_7}
- Camera angle: {angle}
- Color treatment: {color_treatment}
- Grain: subtle film grain, {iso_equivalent}

═══ ABSOLUTE NO-GO ═══
- Pristine logo placement (looks fake)
- Logo bigger than would be realistic
- Logo as the SUBJECT of the image (subject is the context; logo is a presence)
- Generic "branded mockup" template aesthetic
```

---

## 7. 3-stage pipeline

### Stage A — Visual Intent (Claude extracts creative direction from the briefing)

```
You are a brand art director {brand_aesthetic_anchor}. You received this briefing from the client:

[CLIENT BRIEFING]

Your task is to extract the visual direction in 6 dimensions:

1. SUBJECT (the product + context): visually describe what will appear in the frame.
2. LIGHTING: which of the 7 setups (Golden Hour, Low Key, Spotlight, Chiaroscuro, Cutter Lights, Hard Flash, Silhouette) best serves the mood?
3. COMPOSITION: angle, shot, position of product in the frame.
4. COLOR_TREATMENT: palette, saturation, where the primary color appears.
5. STYLE: 35mm editorial? Classic still life? Matte 3D render? Risograph?
6. MOOD + METAPHOR: feeling + visual metaphor

Return in JSON of the image_brief schema.
```

### Stage B — Generation + iteration

R2 calls Higgsfield CLI with image_brief + 3-5 references:

```bash
UUID_1=$(higgsfield upload create "ref-1.png" | grep -oiE '[0-9a-f-]{36}' | head -1)
UUID_2=$(higgsfield upload create "ref-2.png" | grep -oiE '[0-9a-f-]{36}' | head -1)
JOB_ID=$(higgsfield generate create nano_banana_2 \
  --prompt "[structured image_brief]" \
  --image "$UUID_1" \
  --image "$UUID_2" \
  --aspect_ratio "4:5" \
  --json | grep -oiE '[0-9a-f-]{36}' | head -1)
higgsfield generate wait "$JOB_ID" --wait-timeout 30m --json
```

Generates the necessary variation. If it doesn't serve, adjust image_brief and run again, recording attempt, model, UUIDs and job_id.

### Stage C — Final polish (upscale + micro-refinements)

```bash
# Refinement via new referenced generation
REFINED_JOB=$(higgsfield generate create nano_banana_2 \
  --prompt "[description of the localized refinement]" \
  --image "$CHOSEN_UUID" \
  --aspect_ratio "4:5" \
  --json | grep -oiE '[0-9a-f-]{36}' | head -1)
higgsfield generate wait "$REFINED_JOB" --wait-timeout 30m --json
```

Final output: PNG 2176×2720, final delivery quality, total cost ~$0.80-1.50 per final shot.

---

## 8. What is a GOOD vs BAD AI image

### 8.1 — GOOD AI (study)

**Brands that use AI well:**
- Editorial brands that use AI for conceptual illustration (without pretending to be a photo)
- Tech brands that use AI for abstract hero (geometry, digital landscape)
- Brands that use AI for moodboards and initial exploration (not final)
- Brands that combine AI + human post-production (color grading, inpaint)

**Characteristics:**
- Visible specific direction
- Style coherent with the brand
- No obvious AI signs (hands OK, natural faces)
- Embedded text legible and correct
- Intentional composition (not model default)

### 8.2 — BAD AI (avoid)

**Saturated anti-patterns:**
- Obvious "stable diffusion default" hero (perfect face, glazed eyes, generic blur background)
- Published person with 6 fingers or wrong anatomy (triggers distrust)
- Invented text on signs/posters (visual lorem ipsum)
- Generic "3D Pixar style" (saturated in 2023-2024)
- "AI founder selfie" — very dangerous (detectable and suspect)
- AI imitating photography without direction (looks like any photo)
- AI-drawn logo (always distorted, NEVER do)

**Brands to study as how NOT to do it** (anonymous, but recognizable):
- "AI coach" with AI avatars + motivational text
- E-commerce with AI product photos visibly melting
- "Influencer" with AI photos of "aspirational environments" without direction

---

## 9. What is FAST vs SLOW generation (cost + time)

### 9.1 — FAST (scalable)

- **Iteration in low quality** ($0.005-0.02 per image) — quick exploration
- **Reusable prompt templates** — don't write from scratch
- **Batch generation** (4-8 variations per prompt) — choose the best
- **Same model, specialized prompts per task** (Nano Banana 2 with refs and constraints)
- **Direct API + script** vs. manual interface

### 9.2 — SLOW (justifiable in specific cases)

- **High quality + upscale + polish** — worth it in hero campaign
- **10+ iterations** — when exact direction is critical
- **LoRA training for consistent character** — upfront investment, return at scale
- **Long video (>15s)** — always slow

### 9.3 — Efficiency: golden rule

> Common image (story, post, secondary slide): low quality, 1-2 iterations, $0.05 total
> Important image (carousel cover, hero): medium quality, 3-5 iterations, $0.30
> Hero campaign image (site cover, main ad): high quality + upscale + polish, 10+ iterations, $1.50-3.00

---

## 10. What WORKS vs DOESN'T WORK in production

### 10.1 — WORKS

- **Image-to-image** with clear reference > pure text-to-image
- **Explicit negative prompt** steers away from generic defaults
- **Aspect ratio multiple of 16** (1088×1360 for 4:5) — optimized models
- **Iteration with fixed seed** when wanting controlled variation
- **Prompt in English** (models trained majority in English)
- **Nominal real references** (artist names, film references)
- **Composition described by concrete elements** (not "a scene")

### 10.2 — DOESN'T WORK

- **Vague prompt** ("beautiful sunset", "professional logo") — comes out generic
- **Long text inside image** (>30 characters frequently wrong)
- **Multiple people in complex composition** (anatomy gets confused)
- **Hands in foreground** (still problem in 2026, better avoid foreground)
- **Famous logos requested** (models may refuse or distort)
- **Extreme style transfer** without visual reference (unpredictable results)
- **Abstract concept without visual metaphor** (model doesn't infer)

---

## 11. What SELLS vs REPELS (commercial application)

### 11.1 — SELLS

- Well-directed photorealistic hero shots (prize, atmosphere)
- Conceptual product shots (impossible to capture physically: floating product, extra dimension)
- Aspirational lifestyle (locations and moments costly to produce physically)
- Conceptual editorial for blog, newsletter cover, ad
- Mockups of packaging, cards, stationery
- Infinite variations of the same product in different contexts

### 11.2 — REPELS

- Obvious AI people in hero (immediate loss of credibility)
- "AI founder photo" (detected, generates commercial distrust)
- Product with distortions (wrong hands, strange anatomy)
- Poorly rendered AI text in published piece (absolute amateur)
- AI imitating documentary photography (reads fake)
- AI video with people in strange movement (uncanny valley)

### 11.3 — Central commercial principle

AI is great for **conceptual, abstract, contexts impossible to photograph**. Bad for **imitating documentary photography, portraits of real people, products with critical technical detail**. Use in the field where it shines; hire a photographer in the field where AI fails.

---

## 12. Generative AI anti-patterns

### 12.1 — Technical anti-patterns

- ❌ Hands with 6 fingers or abnormal anatomy
- ❌ Glazed eyes, strange symmetry, "dead" expression
- ❌ Incoherent text on signs/posters/books
- ❌ Inconsistent shadows (light in contradictory direction)
- ❌ Physically impossible reflections
- ❌ Plastic supersmoothed skin
- ❌ Background with melting objects
- ❌ Logo "drawn" by AI (always distorts)
- ❌ Generator watermark on final piece

### 12.2 — Saturated aesthetic anti-patterns

- ❌ Generic "3D Pixar style" (saturated 2023-2024)
- ❌ "Cyberpunk neon" without purpose (cliché)
- ❌ AI avatar "Notion illustrated style" (saturated)
- ❌ Generic "perfect" woman as AI influencer
- ❌ Hero with purple-blue gradient + floating human figure

### 12.3 — Ethical anti-patterns

- ❌ Imitation of living photographer without consent (legal gray)
- ❌ Imitation of real person (deepfake — illegal in several contexts)
- ❌ Appropriation of living artist's style without credit
- ❌ Generation of misleading content ("real" photo that isn't)

---

## 13. Costs and quality tiers

### 13.1 — Costs

Costs depend on the model, the queue and the credits of the active Higgsfield account. Before real render:

```bash
higgsfield account status
```

Record model, job_id, attempt and decision.

### 13.2 — Spending limit recommendation

| Monthly volume | Spending limit |
|---|---|
| Beginner (5-15 pieces/month) | $10/month |
| Operational (30-60 pieces/month) | $40/month |
| Intensive (100-200 pieces/month) | $100/month |
| Professional/agency (500+/month) | $300/month |

### 13.3 — Quality tiers — when to use each

| Tier | Use |
|---|---|
| **Low** | Composition iteration, validate layout |
| **Medium** | Internal pre-approval, mood board |
| **High** | Final for publication |

**Rule:** iterate in low, validate in medium, finalize in high. Costs nothing to test 4 versions in low, choose 1, finalize in high.

---

## 14. Error handling

| Error | Action |
|---|---|
| `higgsfield: command not found` | Install `@higgsfield/cli` |
| Missing login | Run `higgsfield login` |
| `429 Too Many Requests` | `sleep 5` between calls |
| `Insufficient credits` | Recharge on Higgsfield |
| Wrong aspect ratio | Fix `--aspect_ratio` |
| `500 / 502` | Retry up to 2x. If persists, mark piece as failed |
| Timeout >60s | Cancel, retry once |

---

## 15. When the Maestro should call me

### 15.1 — Always call me on:

- Generation of ANY image via AI (engine choice, prompt, iteration)
- Audit of AI-generated image
- Decision on upscale, inpainting, final composition
- Cost optimization (when to use low/medium/high)
- Logo placement in photo via AI (specific technique)
- Character consistency in series (advanced technique)

### 15.2 — Can be consulted on:

- Aspect ratio decision
- Custom negative prompt
- Comparison between engines for specific task
- Polish pipeline

### 15.3 — Don't call me for:

- Human photographic direction (call `09-Photography-Direction.md`)
- Visual system / palette (call `08-Visual-System.md`)
- Copy / tone of voice (call `07-Voice-and-Tone.md`)

---

## 16. Operational checklist

### Before generating image

1. Read this file (focus on sections 4, 5, 6)
2. Read DNA.md (section 3 — Visual style + 3.8 — Photographic direction)
3. Build structured image_brief (JSON)
4. Choose appropriate engine (section 3)
5. Define quality tier (low/medium/high) based on context
6. Generate 4 variations
7. Audit (anti-patterns section 12)
8. Polish (upscale, inpaint if needed)

### Before auditing AI image

1. Check technical anti-patterns (hands, eyes, text, shadows)
2. Check adherence to brand style
3. Diagnosis in prose + concrete suggestion

---

## Summary in one line

**Direct like a senior art director, prompt like an instruction engineer, choose engine like a strategist, polish like an editorial retoucher.**
