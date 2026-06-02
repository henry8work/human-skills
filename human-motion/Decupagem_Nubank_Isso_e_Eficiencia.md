<!-- IMAGE_GENERATION_ROUTE_RULE -->
> Image generation rule: always use `imageprompts.md` as the creative/prompt guide when present. Before rendering any image, ask the user to choose: **Magnific** via direct MCP/API (`nano-banana-pro-flash`, `resolution: "1K"`, intended free/default) or **Higgsfield** via MCP/CLI (paid). Do not use `mcp__magnific_oauth.images_generate` for routine Magnific image generation unless explicitly requested; use `magnific-oauth.account_balance` only to check/measure credits.
<!-- /IMAGE_GENERATION_ROUTE_RULE -->

# EXECUTABLE VISUAL BREAKDOWN — NUBANK "THIS IS EFFICIENCY"

**Format:** 1080×1920 (9:16) · 30fps · 750 frames · 25.0s
**Safe padding:** 250px top + 250px bottom on all scenes (vertical usable area: 1420px)
**Render target:** Remotion (React) / Three.js / After Effects
**Version:** v1.1 — real assets plugged in, only the photo of the man on the sofa (C3) remains to be generated

## ASSETS AVAILABLE IN FOLDER `nubank/`

| File                                             | Use                                  | State              |
|--------------------------------------------------|--------------------------------------|---------------------|
| `Nubank_logo_2021.svg.png`                       | "nu" monogram logo — C1 and C7        | ✅ ready (purple, turns white via CSS filter) |
| `C2_mulher_aeroporto_1080x1920.png`              | Airport lifestyle photo — C2          | ✅ ready (already at 1080×1920) |
| `C3_homem_sofa_1080x1920.png`                    | Sofa lifestyle photo — C3             | ⏳ generate via `_PROMPT_C3_homem_sofa.md` |
| `card1_nubank.png`                               | Ecosystem card 1 — C4                 | ✅ ready (cropped from official) |
| `card2_ultravioleta.png`                         | Ecosystem card 2 — C4                 | ✅ ready |
| `card3_nuempresas.png`                           | Ecosystem card 3 — C4                 | ✅ ready |
| `high.mp4`                                       | 3D cards video — C6                   | ✅ ready (1080×1080, 30fps, 3.93s — centered composite) |

---

## 1. VISUAL PHILOSOPHY

**Clean bank-editorial** aesthetic, inherited from nubank.com.br: solid purple as affirmation, white/cream as breathing room, typography in regular weight dominating over bold. No dark mode, no neon glow, no decorative particles. The shine comes from composition and negative space, not from effects.

**Camera language:** lively but serene camera. Discreet push-ins (12–25px of Z), horizontal micro-orbits (±3°), never shake. Every transition between scenes uses interpolated `cameraBlend`, never a hard cut.

**Rhythm:** consolidated brand breathing. BPM 95 of the score aligns with entry timing (frames multiple of ~19 = 1 beat). Visual peaks on beats 4, 8, 12, 16, 20.

**Tone:** serene confidence, discreet scale (100M without ostentation), efficiency as a quiet affirmation at the close.

---

## 2. TECHNICAL PALETTE

| Token              | HEX        | Use                                                        |
|--------------------|------------|------------------------------------------------------------|
| `purple/primary`   | `#820AD1`  | Main background scenes 1, 5, 7                             |
| `purple/deep`      | `#420680`  | Text on cream background, icons, counters                  |
| `purple/soft`      | `#A23DE0`  | Internal background gradient (radial, 30% opacity)         |
| `cream/base`       | `#FAF7F2`  | Background scenes 2, 3, 4, 6                               |
| `white/pure`       | `#FFFFFF`  | Text on purple, final logo, CTA button                     |
| `white/85`         | `#FFFFFF` α0.85 | Floating badges over lifestyle photos                |
| `text/dark`        | `#1A1A1A`  | Card titles in the ecosystem (scene 4)                     |
| `text/muted`       | `#6B6B6B`  | Sub-labels and mini-CTAs                                   |
| `noise/overlay`    | `#000000` α0.025 | Subtle film grain on all backgrounds                 |
| `shadow/soft`      | `#000000` α0.08  | Card and badge shadows (blur 24px, y-offset 12px)    |

**Forbidden:** saturated gradients, dark surfaces, neon glow, `screen`/`overlay` blend modes on backgrounds (always natural colors).

---

## 3. SOUND DIRECTION

**Base score:** electronic minimal ambient — synth pad (Prophet-style, attack 200ms, release 800ms) + sub bassline (sine wave, 55Hz, ducked -3dB on the beats), discreet crystalline arpeggio entering from frame 240. **BPM: 95**. 4/4 time signature.

**Dynamic arc:**

| Section      | Frames    | Dynamics          | Active instruments                               |
|--------------|-----------|-------------------|--------------------------------------------------|
| Intro        | 0–105     | -12 LUFS          | Pad + sub bass                                   |
| Build 1      | 106–315   | -10 LUFS          | + Crystalline arpeggio + ticks                   |
| Plateau      | 316–540   | -9 LUFS           | + Closed hi-hat in eighth notes (scene 5)        |
| Apex         | 541–660   | -8 LUFS           | + Melodic pluck (3 notes: D-A-F#)                |
| Resolution   | 661–750   | -10 → -14 LUFS    | Pad tail + final sparkle, fade -∞                |

**SFX library (all synced to frame, see per-scene detailing):**

| ID          | Sound                                          | Duration | Use                                  |
|-------------|------------------------------------------------|----------|--------------------------------------|
| `whoosh-L`  | Aerial whoosh passing from right to left       | 18 fr    | Horizontal scene exits               |
| `whoosh-R`  | Aerial whoosh passing from left to right       | 18 fr    | Horizontal scene entries             |
| `whoosh-V`  | Vertical whoosh (rising)                       | 16 fr    | Vertical transitions                 |
| `tick-soft` | Filtered digital tick (1kHz, 40ms)             | 1 fr     | Each 100M counter increment          |
| `pop-text`  | Short sub-aural pop (200Hz, 30ms)              | 1 fr     | Appearance of each keyword           |
| `sparkle`   | Crystalline sparkle (5kHz–8kHz, 400ms)         | 12 fr    | Appearance of the final CTA          |
| `card-slide`| Subtle card friction (filtered)                | 22 fr    | Ecosystem carousel                   |
| `lock-click`| Soft mechanical click (300Hz, 60ms)            | 2 fr     | Final logo lockup                    |

**Planned mixing:** score -10 LUFS integrated, SFX -16 LUFS average, headroom -1 dBTP, ducking -2dB on SFX peaks. **Zero human voice on any layer.**

---

## 4. SCENE MAP

| #  | Frames     | Duration | Visual Type               | Camera               | IN Transition | OUT Transition       |
|----|------------|----------|---------------------------|----------------------|---------------|----------------------|
| 1  | 0–104      | 3.47s    | Purple typographic hero   | Smooth Z push-in     | Fade from black| Slide-out left + cameraBlend |
| 2  | 98–209     | 3.73s    | Airport lifestyle         | Z push-in + micro-orbit | Slide-in right | Slide-out up + cameraBlend |
| 3  | 202–314    | 3.73s    | Sofa lifestyle            | Z pull-back + breathing | Slide-in down | Slide-out right + cameraBlend |
| 4  | 307–449    | 4.77s    | 3D ecosystem carousel     | Lateral X truck      | Slide-in left | Slide-out down + cameraBlend |
| 5  | 442–584    | 4.77s    | "100M" hero + counter     | Slow Z push-in       | Slide-in up   | Slide-out left + cameraBlend |
| 6  | 577–674    | 3.27s    | 3D cards product          | Soft Y orbit         | Slide-in right | Quadruple Exit ↓    |
| 7  | 667–750    | 2.80s    | "This is efficiency" CTA lockup | Static + breathing 3D | Slide-in up | Fade-out + scale (final) |

**Standard overlap:** 7 frames between consecutive scenes (zero empty frames guaranteed).
**Exit alternation:** L → V↑ → R → V↓ → L → V↓ → fade (alternating axes per R5 of the spec).

---

## 5. PER-SCENE DETAILING

---

### SCENE 1 — PURPLE OPENING (frames 0–104, 3.47s)

#### Narrative
Opens on affirmation. Giant "nu" monogram logo centered on solid purple, slow push-in that breathes the brand before delivering the copy. The sentence arrives word-by-word from beat 2 to beat 5. No visual economy — the opening is the weight.

#### Camera Movement

**Initial Setup:**

| Property    | Value          |
|-------------|----------------|
| position    | X:0, Y:0, Z:0  |
| rotation    | X:0°, Y:0°, Z:0° |
| FOV         | 50°            |
| target      | (0, 0, -1000)  |

**Movement:**

| Frame | position (XYZ)      | rotation (XYZ)       | FOV   | Easing          | Purpose                  |
|-------|---------------------|----------------------|-------|-----------------|--------------------------|
| 0     | (0, 0, 0)           | (0°, 0°, 0°)         | 50°   | —               | start                    |
| 60    | (0, 0, -28)         | (0°, 0°, 0°)         | 49°   | cubicBezier(0.33, 0, 0.2, 1) | affirmative push-in |
| 104   | (0, 0, -42)         | (0°, 0.8°, 0°)       | 48.5° | cubicBezier(0.4, 0, 0.6, 1)  | Y micro-orbit, delivery to cut |

#### Design — Background (4 mandatory layers)

| Z   | Layer            | Spec                                                                                    |
|-----|------------------|-----------------------------------------------------------------------------------------|
| -500 | Solid base      | `#820AD1` fullscreen 1080×1920                                                          |
| -400 | Radial gradient | center (540, 960), radius 720px, `#A23DE0` α0.30 → `#820AD1` α0 (smoothstep)            |
| -380 | Noise overlay   | monochrome grain `#000000` α0.025, scale 1.0, animated at 8fps (loop 24 frames)         |
| -300 | Living element  | 3 circular particles Ø8px, `#FFFFFF` α0.06, blur 12px, vertical drift +6px/s            |

#### Main Element — "nu" Logo

| Property       | Value                                                                                  |
|----------------|----------------------------------------------------------------------------------------|
| asset          | `nubank/Nubank_logo_2021.svg.png` (official logo in purple `#820AD1`)                  |
| dimensions     | 520×520px (object-fit: contain, preserving PNG aspect ratio)                           |
| position       | center (540, 880) — offset -80px from vertical center                                  |
| z-position     | 0 (focal plane)                                                                        |
| rendered color | `#FFFFFF` — apply CSS `filter: brightness(0) invert(1)` in Remotion, or SVG mask       |
| stroke / glow  | none                                                                                   |
| micro-breathing | scale 1.000 ↔ 1.012, 90-frame cycle, sine easing                                      |

#### Typography (word-by-word)

**Sentence:** "The future of money / is simple as it should be."
**Font:** Graphik Semibold (replaceable by Inter SemiBold)
**Size:** 64px line 1, 56px line 2
**Color:** `#FFFFFF`
**Line-height:** 1.15
**Letter-spacing:** -0.5px
**Position:** X center, initial Y 1240px (line 1), Y 1320px (line 2)
**Padding:** respecting 250px top/bottom

| Word         | Entry frame | Y initial → final | Opacity 0→1 | Blur 8→0 | Easing                 | SFX        |
|--------------|-------------|-------------------|-------------|----------|------------------------|------------|
| The          | 38          | 1260 → 1240       | 0 → 1 (8fr) | 8 → 0    | cubicBezier(0.2,0,0,1) | pop-text   |
| future       | 42          | 1260 → 1240       | 0 → 1 (8fr) | 8 → 0    | cubicBezier(0.2,0,0,1) | pop-text   |
| of           | 46          | 1260 → 1240       | 0 → 1 (8fr) | 8 → 0    | cubicBezier(0.2,0,0,1) | —          |
| money        | 48          | 1260 → 1240       | 0 → 1 (8fr) | 8 → 0    | cubicBezier(0.2,0,0,1) | pop-text   |
| is           | 62          | 1340 → 1320       | 0 → 1 (8fr) | 8 → 0    | cubicBezier(0.2,0,0,1) | —          |
| simple       | 66          | 1340 → 1320       | 0 → 1 (8fr) | 8 → 0    | cubicBezier(0.2,0,0,1) | pop-text   |
| as           | 72          | 1340 → 1320       | 0 → 1 (8fr) | 8 → 0    | cubicBezier(0.2,0,0,1) | —          |
| it           | 74          | 1340 → 1320       | 0 → 1 (8fr) | 8 → 0    | cubicBezier(0.2,0,0,1) | —          |
| should       | 76          | 1340 → 1320       | 0 → 1 (8fr) | 8 → 0    | cubicBezier(0.2,0,0,1) | —          |
| be.          | 80          | 1340 → 1320       | 0 → 1 (8fr) | 8 → 0    | cubicBezier(0.2,0,0,1) | pop-text   |

#### Block Entry Animations

| Element  | Frame in | Property              | Initial → final value | Duration | Easing            |
|----------|----------|-----------------------|-----------------------|----------|-------------------|
| "nu" logo| 8        | scale + opacity       | 0.85→1.00 / 0→1       | 22 fr    | cubicBezier(0.33,1,0.68,1) |
| "nu" logo| 8        | blur                  | 6 → 0                 | 22 fr    | linear            |

#### Micro-animations (Breathing 3D)
- Logo: scale ±1.2% in 90fr cycle (defined above)
- Particles: continuous Y drift, opacity oscillating 0.04↔0.08 in 60fr

#### Exit — Quadruple Exit (frames 97–112, overlapping scene 2)

| Property    | Logo + Text: initial → final value   | Duration | Easing                  |
|-------------|--------------------------------------|----------|-------------------------|
| position X  | 540 → -240 (slide-out left)          | 15 fr    | cubicBezier(0.7,0,0.84,0) |
| blur        | 0 → 12px                             | 15 fr    | linear                  |
| opacity     | 1 → 0                                | 15 fr    | cubicBezier(0.4,0,1,1)  |
| scale       | 1.00 → 0.94                          | 15 fr    | cubicBezier(0.7,0,0.84,0) |

#### Audio
- **Score:** intro (-12 LUFS), pad + sub. At frame 60 an arpeggio hint enters (1 note, D4).
- **SFX:**
  - Frame 8: `pop-text` on logo (attenuated -6dB)
  - Frames 38–80: `pop-text` on each keyword as per table
  - Frame 97: `whoosh-L` (exit to left)

#### Transition to Scene 2
**Overlap:** frames 98–104 (7 frames). `cameraBlend` lerp:

```
camera.position = lerp(scene1.cam, scene2.cam, smoothstep(0,1, (frame-98)/7))
```

---

### SCENE 2 — AIRPORT LIFESTYLE (frames 98–209, 3.73s)

#### Narrative
Break from purple to cream. Vertical fullscreen photo of a woman with glasses in a departure lounge, with luggage and a purple phone. Real life anchoring the brand. "Digital account" badge floats over the photo. Copy enters in two lines, aligned at the base.

#### Camera Movement

**Initial Setup:**

| Property    | Value              |
|-------------|--------------------|
| position    | X:0, Y:0, Z:-30    |
| rotation    | X:0°, Y:0°, Z:0°   |
| FOV         | 48°                |
| target      | (0, 0, -1000)      |

**Movement:**

| Frame | position (XYZ)      | rotation (XYZ)      | FOV   | Easing                       | Purpose                |
|-------|---------------------|---------------------|-------|------------------------------|------------------------|
| 98    | (0, 0, -30)         | (0°, 0°, 0°)        | 48°   | —                            | entry with inertia     |
| 160   | (0, 0, -48)         | (0°, -1.2°, 0°)     | 47°   | cubicBezier(0.33,0,0.2,1)    | push-in + micro-orbit  |
| 209   | (0, 0, -62)         | (0°, -2.0°, 0°)     | 46.5° | cubicBezier(0.4,0,0.6,1)     | continuation of orbit  |

#### Design — Background (4 mandatory layers)

| Z    | Layer                | Spec                                                                                       |
|------|----------------------|--------------------------------------------------------------------------------------------|
| -500 | Cream base           | `#FAF7F2` fullscreen (visible only on safe-area edges, photo covers almost the whole frame) |
| -200 | **Main photo**       | Asset: `nubank/C2_mulher_aeroporto_1080x1920.png` (already at 1080×1920, woman in right third) |
| -180 | Soft vignette        | radial `#000000` α0→α0.12 from edges, attention containment                                |
| -100 | Film grain           | noise `#000000` α0.02, scale 1.2, animated 24-frame loop                                   |

##### Confirmed asset spec
- Real dimensions: 1080×1920 ✓
- Composition: woman with glasses seated on airport bench, **right** third of frame, holding purple phone, silver luggage to the left, plane taking off from the runway in the background, warm natural light
- Dominant palette: beige/off-white/brown + purple accent of the phone `#820AD1`
- Negative space: DEFINITIVE FRAMING — upper **left** area free for "Digital account" badge (between Y 480 and Y 720, X 80–500 available)
- **Note:** badge re-positioned from (760, 580) to **(180, 580)** because the woman occupies the right side (correction vs. v1.0)

##### Photo animation (subtle parallax)
| Frame | scale | position X | Easing |
|-------|-------|------------|--------|
| 98    | 1.04  | 0          | —      |
| 209   | 1.08  | -8px       | linear (slow drift) |

#### Main Element — "Digital account" Badge

| Property       | Value                                                  |
|----------------|--------------------------------------------------------|
| shape          | pill 280×64px, border-radius 32px                      |
| fill           | `#FFFFFF` α0.92                                        |
| stroke         | none                                                   |
| shadow         | `#000000` α0.08, blur 24px, offset (0, 12)             |
| backdrop-blur  | 18px                                                   |
| position       | **(180, 580)** — upper left corner (woman is in the right third) |
| z-position     | +120 (in front of photo plane, faster parallax)        |
| inner text     | "Digital account" — Graphik Medium 26px `#420680`      |
| icon           | dot Ø10px `#820AD1` left of text, offset -16px         |
| breathing      | scale 1.000 ↔ 1.015, 75-frame cycle                    |

#### Typography (word-by-word)

**Sentence:** "More than an account, / it's your life happening."
**Font:** Graphik Semibold line 1, Graphik Regular line 2
**Size:** 58px / 50px
**Color:** `#1A1A1A` (over light area of photo) — if the photo has a dark area in the lower third, fallback `#FFFFFF` with shadow `#000000` α0.4 blur 16px
**Position:** X center, Y 1440 (line 1), Y 1510 (line 2)

| Word         | Frame | Y initial → final  | Opacity | Blur | Easing                 | SFX      |
|--------------|-------|--------------------|---------|------|------------------------|----------|
| More         | 132   | 1460 → 1440        | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| than         | 136   | 1460 → 1440        | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | —        |
| an           | 140   | 1460 → 1440        | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | —        |
| account,     | 144   | 1460 → 1440        | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| it's         | 158   | 1530 → 1510        | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | —        |
| your         | 164   | 1530 → 1510        | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| life         | 168   | 1530 → 1510        | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| happening.   | 172   | 1530 → 1510        | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |

#### Block entry (frames 98–115)
- Photo: blur 24→0 (18fr), opacity 0→1 (12fr), scale 1.08→1.04 (18fr) — easing cubicBezier(0.33,1,0.68,1)
- Badge: 18fr delay, then scale 0.85→1.00 + opacity 0→1 + X (140→180) in 14 frames (enters from the left margin)

#### Micro-animations
- Badge: breathing scale ±1.5%
- Photo: parallax X drift -8px over the scene (linear)
- Z-parallax: badge (Z+120) moves 1.12× faster than photo (Z-200) in response to camera orbit, per R2: factor = 1 + (120/1000) = 1.12

#### Exit — Quadruple Exit (frames 195–209, vertical UP)

| Property    | Initial → final value  | Duration | Easing                    |
|-------------|------------------------|----------|---------------------------|
| position Y  | current → -480         | 14 fr    | cubicBezier(0.7,0,0.84,0) |
| blur        | 0 → 14px               | 14 fr    | linear                    |
| opacity     | 1 → 0                  | 14 fr    | cubicBezier(0.4,0,1,1)    |
| scale       | 1.00 → 0.96            | 14 fr    | cubicBezier(0.7,0,0.84,0) |

#### Audio
- **Score:** build 1 starts at 106 (-10 LUFS), crystalline arpeggio enters at 112 (3 notes A-C#-E loop 16fr)
- **SFX:**
  - Frame 98: `whoosh-R` (entry from right) -3dB
  - Frame 132: `pop-text` on "More"
  - Frames 144, 168, 172: `pop-text` on keywords
  - Frame 195: `whoosh-V` (exit upward)

#### Transition to Scene 3
**Overlap:** frames 202–209 (7 fr). `cameraBlend` lerp between C2 camera (orbit -2°) and C3 setup.

---

### SCENE 3 — SOFA LIFESTYLE (frames 202–314, 3.73s)

#### Narrative
Continuation of the real-life narrative. Man in lavender shirt on the sofa, relaxed, using the app. Camera enters pulling from above (Y axis opposite to C2's exit). "No-annual-fee card" badge floats. Copy enters in two lines.

#### Camera Movement

**Initial Setup:**

| Property    | Value              |
|-------------|--------------------|
| position    | X:0, Y:80, Z:-35   |
| rotation    | X:-2°, Y:0°, Z:0°  |
| FOV         | 48°                |
| target      | (0, 0, -1000)      |

**Movement (slow pull-back):**

| Frame | position (XYZ)      | rotation (XYZ)      | FOV   | Easing                       | Purpose                   |
|-------|---------------------|---------------------|-------|------------------------------|---------------------------|
| 202   | (0, 80, -35)        | (-2°, 0°, 0°)       | 48°   | —                            | vertical entry            |
| 240   | (0, 20, -20)        | (-0.5°, 0°, 0°)     | 49°   | cubicBezier(0.33,0,0.2,1)    | pull-back, opens space    |
| 314   | (0, 0, -8)          | (0°, 1.0°, 0°)      | 50°   | cubicBezier(0.4,0,0.6,1)     | micro-orbit to right      |

#### Design — Background (4 mandatory layers)

| Z    | Layer            | Spec                                                                |
|------|------------------|---------------------------------------------------------------------|
| -500 | Cream base       | `#FAF7F2` (visible only on edges)                                   |
| -200 | **Main photo**   | Asset: `nubank/C3_homem_sofa_1080x1920.png` (to generate — see `_PROMPT_C3_homem_sofa.md`) |
| -180 | Vignette         | radial `#000000` α0→α0.10                                           |
| -100 | Film grain       | noise α0.02, 24fr loop                                              |

##### Asset Spec — Sofa Man Photo (generate via AI)
- **Target dimensions:** 1080×1920 fullscreen
- **Crop framing:** man in **LEFT** third of frame (mirroring the airport woman in the right third — creates cinematic pair). Three-quarter visible, phone in hands
- **Shirt:** lavender `#C9B8E3`, linen or light fabric
- **Sofa:** beige/off-white, contemporary minimal Brazilian living room, cream wall
- **Phone:** purple Nubank case `#820AD1` visible
- **Light:** warm natural coming from frame right, late afternoon golden hour
- **Composition:** negative space on the **RIGHT** for "No-annual-fee card" badge
- **Treatment:** same warm tone as C2 (+5 temperature, -8 saturation, skin micro-contrast +4) — perfect aesthetic pair with airport photo
- **Full prompt:** see `nubank/_PROMPT_C3_homem_sofa.md`

##### Photo animation (parallax)
| Frame | scale | position X | Easing |
|-------|-------|------------|--------|
| 202   | 1.06  | -6         | —      |
| 314   | 1.02  | 0          | linear |

#### Main Element — "No-annual-fee card" Badge

| Property       | Value                                                  |
|----------------|--------------------------------------------------------|
| shape          | pill 340×64px, border-radius 32px                      |
| fill           | `#FFFFFF` α0.92                                        |
| shadow         | `#000000` α0.08, blur 24px, offset (0, 12)             |
| backdrop-blur  | 18px                                                   |
| position       | **(720, 620)** — upper **right** corner (man is in left third) |
| z-position     | +120                                                   |
| text           | "No-annual-fee card" — Graphik Medium 26px `#420680`   |
| icon           | mini-card 24×16px `#820AD1` on left                    |
| breathing      | scale 1.000 ↔ 1.015, 75 fr cycle                       |

#### Typography (word-by-word)

**Sentence:** "An app that simplifies / every decision of yours."
**Font:** Graphik Semibold line 1, Graphik Regular line 2
**Size:** 58px / 50px
**Color:** `#1A1A1A`
**Position:** X center, Y 1440 (line 1), Y 1510 (line 2)

| Word          | Frame | Y → Y      | Opacity | Blur | Easing                 | SFX      |
|---------------|-------|------------|---------|------|------------------------|----------|
| An            | 236   | 1460→1440  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| app           | 240   | 1460→1440  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| that          | 244   | 1460→1440  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | —        |
| simplifies    | 248   | 1460→1440  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| every         | 262   | 1530→1510  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | —        |
| decision      | 266   | 1530→1510  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| of yours.     | 272   | 1530→1510  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |

#### Block entry (frames 202–220)
- Photo: blur 22→0 (18fr), opacity 0→1 (12fr), Y 80→0 (18fr)
- Badge: 22fr delay, X (760→720) + scale 0.85→1.00 + opacity 0→1 in 14fr (enters from right margin)

#### Micro-animations
- Badge breathing ±1.5%
- Photo scale drift 1.06→1.02 continuous

#### Exit — Quadruple Exit (frames 300–314, slide-out RIGHT)

| Property    | Initial → final value  | Duration | Easing                    |
|-------------|------------------------|----------|---------------------------|
| position X  | current → +780         | 14 fr    | cubicBezier(0.7,0,0.84,0) |
| blur        | 0 → 14px               | 14 fr    | linear                    |
| opacity     | 1 → 0                  | 14 fr    | cubicBezier(0.4,0,1,1)    |
| scale       | 1.00 → 0.96            | 14 fr    | cubicBezier(0.7,0,0.84,0) |

#### Audio
- **Score:** build 1 sustained, arpeggio continues, bassline gains +1 ghost note at 260
- **SFX:**
  - Frame 202: `whoosh-V` (entry from above, pitched down -3 semitones)
  - Frames 236, 248, 266, 272: `pop-text`
  - Frame 300: inverted `whoosh-R` (right exit)

#### Transition to Scene 4
Overlap 307–314. `cameraBlend` resetting to C4's static frontal camera.

---

### SCENE 4 — ECOSYSTEM / 3D CAROUSEL (frames 307–449, 4.77s)

#### Narrative
The delivery of the ecosystem. Three vertical cards float in 3D formation, lateral trucking camera revealing each one. Official Nubank carousel style (covering photo + title + mini-CTA "Learn more"). Closing copy enters at the base after the three cards stabilize.

#### Camera Movement

**Initial Setup:**

| Property    | Value              |
|-------------|--------------------|
| position    | X:-280, Y:0, Z:-120 |
| rotation    | X:0°, Y:6°, Z:0°   |
| FOV         | 52°                |
| target      | (0, 0, -800)       |

**Movement (X truck — lateral):**

| Frame | position (XYZ)        | rotation (XYZ)    | FOV   | Easing                       | Purpose                  |
|-------|-----------------------|-------------------|-------|------------------------------|--------------------------|
| 307   | (-280, 0, -120)       | (0°, 6°, 0°)      | 52°   | —                            | reveals card 1           |
| 360   | (0, 0, -100)          | (0°, 0°, 0°)      | 51°   | cubicBezier(0.33,0,0.2,1)    | centers card 2           |
| 410   | (+280, 0, -120)       | (0°, -6°, 0°)     | 52°   | cubicBezier(0.4,0,0.6,1)     | reveals card 3           |
| 449   | (0, 0, -80)            | (0°, 0°, 0°)      | 50°   | cubicBezier(0.65,0,0.35,1)   | returns to center, prepares exit |

#### Design — Background (4 mandatory layers)

| Z    | Layer            | Spec                                                                |
|------|------------------|---------------------------------------------------------------------|
| -500 | Cream base       | `#FAF7F2` fullscreen                                                |
| -400 | Subtle gradient  | linear top→bottom `#FFFFFF` α0.4 → `#FAF7F2` α0                     |
| -300 | Guide lines      | 2 horizontal lines Ø1px `#820AD1` α0.06, Y=480 and Y=1440           |
| -100 | Grain            | noise α0.02, 24fr loop                                              |

#### Main Elements — 3 Vertical Cards

**v1.1 strategy:** the cards are **unit PNGs** extracted from the official Nubank carousel (already contain photo + title "Nubank/Nubank Ultravioleta/Nu Empresas" + "Learn more" pill). Do not rebuild internal typography in Remotion — use the entire PNG with border-radius and shadow applied to the container.

**Layout:** 3 cards in 3D formation, X spacing 380px, staggered Z distance.

##### Card 1 — Nubank
| Property       | Value                                                         |
|----------------|---------------------------------------------------------------|
| asset          | `nubank/card1_nubank.png` (472×771 → rendered 320×523)        |
| position       | (-380, 720, +20)  Z in front                                  |
| render dimensions | 320×523px (preserves PNG aspect ratio: 472/771 = 0.612)    |
| object-fit     | cover, border-radius 28px (mask)                              |
| shadow         | `#420680` α0.18, blur 36px, offset (0, 18)                    |
| breathing      | scale 1.000 ↔ 1.012, 80fr cycle                               |

##### Card 2 — Ultravioleta (highlighted card, slightly larger)
| Property       | Value                                                         |
|----------------|---------------------------------------------------------------|
| asset          | `nubank/card2_ultravioleta.png` (512×926 → rendered 320×579)  |
| position       | (0, 700, 0) central plane, Y -20 for emphasis                 |
| render dimensions | 320×579px (preserves aspect ratio: 512/926 = 0.553)        |
| object-fit     | cover, border-radius 28px                                     |
| shadow         | `#000000` α0.20, blur 36px, offset (0, 18)                    |
| breathing      | scale 1.000 ↔ 1.012, 80fr cycle, phase shifted 27fr           |

##### Card 3 — Nu Empresas
| Property       | Value                                                         |
|----------------|---------------------------------------------------------------|
| asset          | `nubank/card3_nuempresas.png` (507×771 → rendered 320×487)    |
| position       | (+380, 720, +20)                                              |
| render dimensions | 320×487px (preserves aspect ratio: 507/771 = 0.658)        |
| object-fit     | cover, border-radius 28px                                     |
| shadow         | `#000000` α0.08, blur 36px, offset (0, 18)                    |
| breathing      | scale 1.000 ↔ 1.012, 80fr cycle, phase 54fr                   |

> **Technical note:** the 3 PNGs have slightly different ratios — keeping original ratios creates the "real carousel" Nubank effect (Ultravioleta is the highlighted card). Titles and "Learn more" buttons are already **inside the PNG** — don't animate internal typography, animate the card as a block. The word-by-word copy below remains valid for scene close.

#### Typography (word-by-word)

**Sentence:** "Everything you need, / in one place."
**Font:** Graphik Semibold line 1, Graphik Regular line 2
**Size:** 56px / 48px
**Color:** `#1A1A1A`
**Position:** X center, Y 1430 (line 1), Y 1500 (line 2)

| Word        | Frame | Y → Y      | Opacity | Blur | Easing                 | SFX      |
|-------------|-------|------------|---------|------|------------------------|----------|
| Everything  | 380   | 1450→1430  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| you         | 387   | 1450→1430  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| need,       | 395   | 1450→1430  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| in          | 410   | 1520→1500  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | —        |
| one         | 417   | 1520→1500  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| place.      | 421   | 1520→1500  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |

#### Card entry (frames 307–360)
- Cards enter in cascade from the right, with pronounced Z-parallax:
  - Card 1: frame 312, X (-580→-380) + opacity 0→1 + scale 0.88→1.00 in 22fr
  - Card 2: frame 326, X (+200→0) + opacity 0→1 + scale 0.88→1.00 in 22fr (delay 14fr)
  - Card 3: frame 340, X (+780→+380) + opacity 0→1 + scale 0.88→1.00 in 22fr
- Easing: cubicBezier(0.33, 1, 0.68, 1)

#### Micro-animations
- Each card: breathing ±1.2% with shifted phases (creates visual undulation)
- Z parallax in response to X truck: cards Z+20 move 1.02× faster than background

#### Exit — Quadruple Exit (frames 435–449, slide-out DOWN)

| Property    | Initial → final value  | Duration | Easing                    |
|-------------|------------------------|----------|---------------------------|
| position Y  | current → +1240        | 14 fr    | cubicBezier(0.7,0,0.84,0) |
| blur        | 0 → 14px               | 14 fr    | linear                    |
| opacity     | 1 → 0                  | 14 fr    | cubicBezier(0.4,0,1,1)    |
| scale       | 1.00 → 0.94            | 14 fr    | cubicBezier(0.7,0,0.84,0) |

#### Audio
- **Score:** plateau starts at 316 (-9 LUFS), arpeggio expands (4 notes), bassline more present
- **SFX:**
  - Frame 307: inverted `whoosh-L` (left entry)
  - Frames 312, 326, 340: `card-slide` on each entering card
  - Frames 380, 391, 395, 417, 421: `pop-text` on keywords
  - Frame 435: pitched `whoosh-V` (descending exit)

#### Transition to Scene 5
Overlap 442–449. `cameraBlend` resetting to camera centered on "100M" hero.

---

### SCENE 5 — 100M MILESTONE + COUNTER (frames 442–584, 4.77s)

#### Narrative
The weight of scale. Giant typographic hero "100M" on purple, counter animated fluidly from 0 to 100 (in millions). The lower line "real stories of people who trust Nubank" enters in regular weight — not bold, per briefing. Slow camera push-in amplifies the sense of magnitude without ostentation.

#### Camera Movement

**Initial Setup:**

| Property    | Value              |
|-------------|--------------------|
| position    | X:0, Y:-60, Z:-100 |
| rotation    | X:1.5°, Y:0°, Z:0° |
| FOV         | 54°                |
| target      | (0, -100, -1000)   |

**Movement (slow push-in + descent):**

| Frame | position (XYZ)        | rotation (XYZ)    | FOV   | Easing                       | Purpose                  |
|-------|-----------------------|-------------------|-------|------------------------------|--------------------------|
| 442   | (0, -60, -100)        | (1.5°, 0°, 0°)    | 54°   | —                            | entry from below         |
| 510   | (0, -20, -40)         | (0.5°, 0°, 0°)    | 51°   | cubicBezier(0.33,0,0.2,1)    | push-in / centers        |
| 584   | (0, 0, -10)           | (0°, 0.5°, 0°)    | 49°   | cubicBezier(0.4,0,0.6,1)     | micro-orbit, delivery    |

#### Design — Background (4 mandatory layers)

| Z    | Layer            | Spec                                                          |
|------|------------------|---------------------------------------------------------------|
| -500 | Solid base       | `#820AD1` fullscreen                                          |
| -400 | Radial gradient  | center (540, 700), radius 900, `#A23DE0` α0.35→α0             |
| -380 | Noise            | `#000000` α0.025, 24fr loop                                   |
| -300 | Living element   | 5 particles Ø6–10px `#FFFFFF` α0.06, Y drift +4px/s           |

#### Main Element — "100M" Hero + Counter

**Hero wrapper:**

| Property       | Value                                                  |
|----------------|--------------------------------------------------------|
| position       | X center, Y 700 (vertical center of usable area)       |
| z-position     | 0 (focal plane)                                        |

**Numeric counter (animated 0→100):**

| Property       | Value                                                  |
|----------------|--------------------------------------------------------|
| font           | Graphik Bold (numeric uppercase)                       |
| size           | 320px                                                  |
| color          | `#FFFFFF`                                              |
| letter-spacing | -8px                                                   |
| position       | X centered, Y 700                                      |
| rendering      | tabular-nums (fixed width per digit, anti-jitter)      |

**"M" suffix (fixed, appears after counter stabilizes):**

| Property       | Value                                                  |
|----------------|--------------------------------------------------------|
| font           | Graphik Bold                                           |
| size           | 320px                                                  |
| color          | `#FFFFFF`                                              |
| position       | X = 720 + (stabilized number width), Y 700             |
| frame in       | 540                                                    |

**Counter animation (0→100):**

| Frame | Numeric value  | Easing                       |
|-------|----------------|------------------------------|
| 470   | 0              | start                        |
| 478   | 14             | easeOutQuart                 |
| 490   | 42             | easeOutQuart                 |
| 510   | 71             | easeOutQuart                 |
| 530   | 92             | easeOutQuart                 |
| 540   | 100            | landing, hold                |

Continuous interpolation between frames, **no stuttering** (mathematical lerp, not step):
```
value(frame) = round(lerp(0, 100, easeOutQuart((frame-470)/70)))
```

**SFX per increment:** `tick-soft` every 4 units incremented (~17 ticks across the 70 frames). Volume ramps -18dB at start → -12dB at end.

#### Lower typography (word-by-word, REGULAR weight)

**Sentence:** "real stories of people / who trust Nubank."
**Font:** Graphik **Regular** (not Semibold, not Bold — per briefing)
**Size:** 42px both lines
**Color:** `#FFFFFF` α0.92
**Position:** X center, Y 1380 (line 1), Y 1430 (line 2)
**Letter-spacing:** 0

| Word       | Frame | Y → Y      | Opacity | Blur | Easing                 | SFX      |
|------------|-------|------------|---------|------|------------------------|----------|
| real       | 548   | 1400→1380  | 0→1     | 6→0  | cubicBezier(0.2,0,0,1) | pop-text |
| stories    | 552   | 1400→1380  | 0→1     | 6→0  | cubicBezier(0.2,0,0,1) | —        |
| of         | 556   | 1400→1380  | 0→1     | 6→0  | cubicBezier(0.2,0,0,1) | —        |
| people     | 558   | 1400→1380  | 0→1     | 6→0  | cubicBezier(0.2,0,0,1) | pop-text |
| who        | 564   | 1450→1430  | 0→1     | 6→0  | cubicBezier(0.2,0,0,1) | —        |
| trust      | 567   | 1450→1430  | 0→1     | 6→0  | cubicBezier(0.2,0,0,1) | pop-text |
| Nubank.    | 574   | 1450→1430  | 0→1     | 6→0  | cubicBezier(0.2,0,0,1) | pop-text |

#### Block entry (frames 442–470)
- Counter: scale 0.94→1.00 + opacity 0→1 + Y (760→700) in 24fr (easing cubicBezier(0.33,1,0.68,1)), starts at 460
- "M": 70fr delay, scale 0.85→1.00 + opacity 0→1 in 12fr, easing cubicBezier(0.33,1,0.68,1)

#### Micro-animations
- Stabilized "100M": breathing scale ±0.8%, 110fr cycle
- Particles: continuous drift + oscillating opacity

#### Exit — Quadruple Exit (frames 570–584, slide-out LEFT)

| Property    | Initial → final value  | Duration | Easing                    |
|-------------|------------------------|----------|---------------------------|
| position X  | 540 → -360             | 14 fr    | cubicBezier(0.7,0,0.84,0) |
| blur        | 0 → 16px               | 14 fr    | linear                    |
| opacity     | 1 → 0                  | 14 fr    | cubicBezier(0.4,0,1,1)    |
| scale       | 1.00 → 0.94            | 14 fr    | cubicBezier(0.7,0,0.84,0) |

#### Audio
- **Score:** plateau, closed hi-hat in eighth notes enters at 460 (8 notes per measure)
- **SFX:**
  - Frame 442: `whoosh-V` (entry from below)
  - Frames 470–540: `tick-soft` spaced per counter (volume ramps -18→-12dB)
  - Frame 540: reinforced `pop-text` on the "M" (-3dB)
  - Frames 548, 558, 567, 574: `pop-text`
  - Frame 570: `whoosh-L` (left exit)

#### Transition to Scene 6
Overlap 577–584. `cameraBlend` to frontal product camera.

---

### SCENE 6 — PRODUCT IN MOTION / 3D CARDS (frames 577–674, 3.27s)

#### Narrative
Nubank cards floating in 3D fullscreen on cream background. No blend modes, no strong vignette — natural video colors breathe. Camera orbits slightly on the Y axis, revealing the three-dimensionality of the cards. Copy enters at the base.

#### Camera Movement

**Initial Setup:**

| Property    | Value              |
|-------------|--------------------|
| position    | X:60, Y:0, Z:-60   |
| rotation    | X:0°, Y:-3°, Z:0°  |
| FOV         | 50°                |
| target      | (0, 0, -800)       |

**Movement (soft Y orbit):**

| Frame | position (XYZ)        | rotation (XYZ)    | FOV   | Easing                       | Purpose                  |
|-------|-----------------------|-------------------|-------|------------------------------|--------------------------|
| 577   | (60, 0, -60)          | (0°, -3°, 0°)     | 50°   | —                            | lateral entry            |
| 625   | (0, 0, -30)            | (0°, 0°, 0°)      | 50°   | cubicBezier(0.33,0,0.2,1)    | orbits to center         |
| 674   | (-60, 0, -50)         | (0°, +3°, 0°)     | 50°   | cubicBezier(0.4,0,0.6,1)     | continues to other side  |

#### Design — Background (4 mandatory layers)

| Z    | Layer                    | Spec                                                                                  |
|------|--------------------------|---------------------------------------------------------------------------------------|
| -500 | Base                     | `#F3F3F3` fullscreen (perfect match with native background of `high.mp4`)             |
| -400 | Luminous gradient        | radial center (540, 800), radius 700, `#FFFFFF` α0.35 → `#F3F3F3` α0                  |
| -200 | **3D cards video**       | Asset: `nubank/high.mp4` (1080×1080, 30fps, 3.93s) — vertically centered composite    |
| -100 | Grain                    | noise α0.018, 24fr loop                                                                |

##### Real asset spec
- Format: MP4 H.264, **1080×1080** (square), 30fps, duration 3.93s (120 frames). Native loop if scene exceeds (scene lasts 97 frames, so it fits without loop)
- Content: 2 Nubank cards (dark purple "Gabriela Lima" + medium purple "Lucas Oliveira") in 3D composition, slightly misaligned, with visible chip and Mastercard logo
- **Video background color:** `#F3F3F3` (very light gray, almost off-white) — that's why the scene background was adjusted to match
- Lighting: soft top-down, discreet reflections, natural colors (no regrade applied)

##### Composite on timeline (video inside vertical canvas)
- Video position: X center (540), Y center 800 → video occupies Y 260–1340 (1080×1080 inside 1080×1920)
- Top headroom: 260px (10px beyond the 250 safe area)
- Lower space for copy: Y 1340–1670 (330px available, more than enough for 2 lines at Y 1450/1510)
- **Video border:** apply 80px radial feather on video edges (CSS `mask-image: radial-gradient(ellipse 95% 95% at center, black 85%, transparent 100%)`) — seamless visual blend with `#F3F3F3` background
- **No blend modes** between video and background (identical colors don't need blend; the feather is the visual bridge)

##### Video animation on timeline
- Frame 577: opacity 0, scale 1.05
- Frame 595: opacity 1, scale 1.00 (easing cubicBezier(0.33,1,0.68,1))
- Frames 595–674: native video playback (`startFrom={0}` in Remotion) + parallax X ±6px following Y camera orbit

#### Typography (word-by-word)

**Sentence:** "Transforming the way / you live your financial life."
**Font:** Graphik Semibold line 1, Graphik Regular line 2
**Size:** 50px / 44px
**Color:** `#1A1A1A`
**Position:** X center, Y 1450 (line 1), Y 1510 (line 2)

| Word           | Frame | Y → Y      | Opacity | Blur | Easing                 | SFX      |
|----------------|-------|------------|---------|------|------------------------|----------|
| Transforming   | 612   | 1470→1450  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| the            | 618   | 1470→1450  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | —        |
| way            | 621   | 1470→1450  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| you            | 634   | 1530→1510  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | —        |
| live           | 637   | 1530→1510  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| your           | 644   | 1530→1510  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | —        |
| financial      | 648   | 1530→1510  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |
| life.          | 652   | 1530→1510  | 0→1     | 8→0  | cubicBezier(0.2,0,0,1) | pop-text |

#### Micro-animations
- Cards: in addition to the video's native motion, global breathing of the composite scale ±0.8% 90fr cycle

#### Exit — Quadruple Exit (frames 660–674, slide-out DOWN)

| Property    | Initial → final value  | Duration | Easing                    |
|-------------|------------------------|----------|---------------------------|
| position Y  | current → +1100        | 14 fr    | cubicBezier(0.7,0,0.84,0) |
| blur        | 0 → 14px               | 14 fr    | linear                    |
| opacity     | 1 → 0                  | 14 fr    | cubicBezier(0.4,0,1,1)    |
| scale       | 1.00 → 0.94            | 14 fr    | cubicBezier(0.7,0,0.84,0) |

#### Audio
- **Score:** apex starts at 541 (-8 LUFS), melodic pluck (D-A-F#) enters at 595
- **SFX:**
  - Frame 577: `whoosh-R` (right entry)
  - Frame 595: reinforced `card-slide` (-3dB, marking card appearance)
  - Frames 612–652: `pop-text` per table
  - Frame 660: pitched down `whoosh-V` (downward exit)

#### Transition to Scene 7
Overlap 667–674. `cameraBlend` lerp to static frontal lockup camera.

---

### SCENE 7 — FINAL LOCKUP / CTA (frames 667–750, 2.80s)

#### Narrative
Close. Solid purple returns. White "nu" logo centered, slogan "This is efficiency." in regular weight below, white pill button "Open your account →" at the bottom with sparkle on appearance. Static camera, only 3D breathing on elements. Video ends with a soft global fade after the final CTA pulse.

#### Camera Movement

**Initial Setup:**

| Property    | Value              |
|-------------|--------------------|
| position    | X:0, Y:-40, Z:-20  |
| rotation    | X:1°, Y:0°, Z:0°   |
| FOV         | 50°                |
| target      | (0, 0, -1000)      |

**Movement (static with micro-push):**

| Frame | position (XYZ)     | rotation (XYZ)    | FOV   | Easing                       | Purpose                |
|-------|--------------------|-------------------|-------|------------------------------|------------------------|
| 667   | (0, -40, -20)      | (1°, 0°, 0°)      | 50°   | —                            | entry                  |
| 710   | (0, 0, 0)          | (0°, 0°, 0°)      | 50°   | cubicBezier(0.33,0,0.2,1)    | resolution, frontal    |
| 750   | (0, 0, -4)         | (0°, 0°, 0°)      | 49.8° | linear                       | imperceptible final micro-push |

#### Design — Background (4 mandatory layers)

| Z    | Layer            | Spec                                                          |
|------|------------------|---------------------------------------------------------------|
| -500 | Solid base       | `#820AD1` fullscreen                                          |
| -400 | Radial gradient  | center (540, 960), radius 800, `#A23DE0` α0.30→α0             |
| -380 | Noise            | `#000000` α0.025, 24fr loop                                   |
| -300 | Particles        | 4 particles Ø6–10px `#FFFFFF` α0.05, drift +3px/s             |

#### Main Elements

##### "nu" Logo (white, centered)
| Property        | Value                                                                              |
|-----------------|------------------------------------------------------------------------------------|
| asset           | `nubank/Nubank_logo_2021.svg.png` (same source as C1)                              |
| dimensions      | 280×280px (object-fit: contain)                                                    |
| position        | (540, 720) — centered, shifted upward                                              |
| z-position      | 0                                                                                  |
| rendered color  | `#FFFFFF` — CSS `filter: brightness(0) invert(1)` (logo is purple in source, becomes white at runtime) |
| breathing       | scale 1.000 ↔ 1.010, 100fr cycle                                                   |

##### Slogan "This is efficiency."
| Property       | Value                                                  |
|----------------|--------------------------------------------------------|
| font           | Graphik **Regular** (regular weight, per briefing)     |
| size           | 56px                                                   |
| color          | `#FFFFFF`                                              |
| letter-spacing | -0.5px                                                 |
| position       | X center, Y 980                                        |
| z-position     | 0                                                      |

##### CTA Button "Open your account →"
| Property       | Value                                                       |
|----------------|-------------------------------------------------------------|
| shape          | pill 600×112px, border-radius 56px                          |
| fill           | `#FFFFFF`                                                   |
| shadow         | `#000000` α0.12, blur 32px, offset (0, 16)                  |
| position       | (540, 1500) — base of usable area, respecting 250px padding |
| z-position     | +60                                                         |
| text           | "Open your account →" — Graphik Semibold 32px `#820AD1`     |
| arrow          | unicode → or icon, offset +12px from text                   |
| breathing      | scale 1.000 ↔ 1.015, 60fr cycle                             |
| pulse          | at frame 730: scale 1.00→1.04→1.00 in 16fr (easing easeOutBack) |

#### Entry Animation per element

**Word-by-word typography:**

| Element   | Word           | Frame | Animation                                          | SFX      |
|-----------|----------------|-------|---------------------------------------------------|----------|
| Logo      | "nu"           | 678   | scale 0.85→1.00 + opacity 0→1 (18fr) + blur 6→0   | pop-text |
| Slogan    | "This"         | 696   | Y 1000→980 + opacity 0→1 (10fr) + blur 8→0        | pop-text |
| Slogan    | "is"           | 700   | idem                                              | —        |
| Slogan    | "efficiency."  | 704   | idem                                              | pop-text |
| CTA Button| (pill shape)   | 720   | scale 0.92→1.00 + opacity 0→1 + Y (1520→1500) in 14fr, easing cubicBezier(0.33,1,0.68,1) | sparkle  |
| CTA Button| (text + arrow) | 728   | opacity 0→1 (8fr)                                 | —        |

#### Micro-animations
- Logo breathing ±1.0%
- Slogan: stable (no visible breathing)
- CTA button breathing ±1.5%, additional pulse at frame 730

#### Exit — End of video (frames 738–750)
Not a transition to another scene — it's the **final fade-out**.

| Property                   | Initial → final value  | Duration | Easing               |
|----------------------------|------------------------|----------|----------------------|
| global opacity (composite) | 1 → 0                  | 12 fr    | cubicBezier(0.4,0,1,1) |
| global scale               | 1.00 → 1.02            | 12 fr    | linear (subtle drift) |

#### Audio
- **Score:** resolution. Sustained pad, sub fades -∞ from frame 720, crystalline tail of arpeggio until 745
- **SFX:**
  - Frame 667: inverted `whoosh-V` (entry from below, pitched up +2 semitones)
  - Frame 678: `lock-click` on logo (-6dB)
  - Frame 720: `sparkle` on button appearance (crystalline, 5–8kHz, 400ms, -8dB)
  - Frame 730: reinforced `pop-text` on CTA pulse (-3dB)
- Master fade out -∞ between frames 738 and 750 (linear)

---

## 6. GENERAL TRANSITIONS TABLE

| From → To | Overlap (fr) | Exit                       | Entry                      | Direction      | Transition SFX                |
|-----------|--------------|----------------------------|----------------------------|----------------|-------------------------------|
| C1 → C2   | 7 (98–104)   | Slide-out LEFT + Quad      | Slide-in RIGHT             | Horizontal ←   | whoosh-L + whoosh-R           |
| C2 → C3   | 7 (202–209)  | Slide-out UP + Quad        | Slide-in DOWN              | Vertical ↑     | whoosh-V                      |
| C3 → C4   | 7 (307–314)  | Slide-out RIGHT + Quad     | Slide-in LEFT              | Horizontal →   | whoosh-R inv + whoosh-L inv   |
| C4 → C5   | 7 (442–449)  | Slide-out DOWN + Quad      | Slide-in UP                | Vertical ↓     | whoosh-V pitched              |
| C5 → C6   | 7 (577–584)  | Slide-out LEFT + Quad      | Slide-in RIGHT             | Horizontal ←   | whoosh-L + whoosh-R           |
| C6 → C7   | 7 (667–674)  | Slide-out DOWN + Quad      | Slide-in UP                | Vertical ↓     | whoosh-V pitched              |

**Rule fulfilled:** consecutive scenes exit in **opposite** directions or **alternating axes**. Zero hard cuts. Zero empty frames.

---

## 7. VALIDATION CHECKLIST

### Commandments (R1, R2, R3 of the spec)
- [x] Every scene with active camera has **Initial Setup + Movement** with XYZ values and easing
- [x] Every element with depth has declared `z-position`
- [x] Parallax factor `1 + (zDepth/1000)` applied on badges (z+120 → 1.12×) and cards (z+20 → 1.02×)
- [x] Every scene transition uses mathematical `cameraBlend` lerp in the 7-frame overlap

### Design
- [x] Each scene has ≥4 background layers (Base + Gradient + Noise + Living Element)
- [x] Every element brings anatomy: dimensions, HEX color + opacity, shadows, blur, XYZ position
- [x] Layer order explicit via z-position
- [x] No opening with background+text alone (Scene 1 has 520×520 logo + 4 BG layers + particles)
- [x] 250px top/bottom padding respected on all scenes

### Typography
- [x] All sentences enter word-by-word
- [x] Each word has: entry frame, Y initial → final, opacity, blur, easing
- [x] Weights respected (Regular where briefing requested: scene 5 lower, scene 7 slogan)

### Timing & Movement
- [x] Total of 750 frames / 25.0s at 30fps
- [x] Quadruple Exit pattern (position + blur + opacity + scale) on all exits
- [x] Consecutive scenes exit in opposite directions (L/V↑/R/V↓/L/V↓ alternation)
- [x] 7-frame overlap between scenes (zero empty frames)
- [x] No camera movement < 30 frames
- [x] Micro-animations (3D breathing) on every static element

### Audio
- [x] **Zero human voice** on any layer
- [x] Electronic minimal ambient score, BPM 95, dynamic arc defined in LUFS
- [x] Frame-synced SFX for each visual event
- [x] Whooshes on all transitions, ticks on counter, sparkle on CTA

### Pending
- [x] Asset: "nu" logo — `nubank/Nubank_logo_2021.svg.png` ✅
- [x] Asset: airport woman photo — `nubank/C2_mulher_aeroporto_1080x1920.png` ✅
- [ ] Asset: sofa man photo — **generate via prompt in `nubank/_PROMPT_C3_homem_sofa.md`** and save as `nubank/C3_homem_sofa_1080x1920.png`
- [x] Assets: ecosystem cards — `card1_nubank.png` / `card2_ultravioleta.png` / `card3_nuempresas.png` ✅
- [x] Asset: cards video — `nubank/high.mp4` ✅ (centered composite, no expand needed)
- [ ] Font confirmation (Graphik vs Inter as fallback) — dev decision
- [ ] Electronic minimal score licensing (original composition or library like Musicbed/Artlist/Epidemic Sound)

---

## 8. EXECUTION NOTES FOR REMOTION

- Composition: 1080×1920, 30fps, durationInFrames=750
- Each scene as `<Sequence from={...} durationInFrames={...}>` with explicit overlap
- 3D camera via `react-three-fiber` (`<Canvas>`) overlaid on DOM layers — alternative: CSS 3D transforms for badges/cards and Three.js only for global camera parallax
- Counter (scene 5): `interpolate(frame, [470, 540], [0, 100], { easing: Easing.bezier(0.25,1,0.5,1), extrapolateRight: 'clamp' })` + `Math.round()` + `tabularNums` in CSS
- Word-by-word typography: array of words with offset `inputRange`, `interpolate` for Y/opacity/blur
- Quadruple Exit: helper function `quadExit({ frame, exitFrame, direction })` returning style object
- Score + SFX: `<Audio>` per file with `startFrom` and interpolated `volume`

---

**Version 1.0 — ready for structural coding. When the photographic assets arrive, plug into the `pending` slots and the blueprint executes.**
