# Carousel Unfolding

Takes a folder with text + images, generates native pieces for Instagram Feed, Instagram Stories, and LinkedIn Feed using the **GPT Image 2 model family** — `gpt_image_2` on the Higgsfield CLI (scripted path via `desdobrar.py`) or `mode: "gpt-2"` on Magnific MCP, per the three-path routing rule in [SKILL.md](SKILL.md). Each piece is a **direct unfolding of the master art**: same photo/visual, same font language, same colors, same graphic elements, with format adaptation, copy, and safe zones.

One skill (`/desdobrar`), one infra script, zero ceremony. The user is a photographer/art director, **not technical** — every configuration is discovered, asked, and saved by the agent itself in the skill flow.

---

## How the user uses it

```
/desdobrar /path/to/folder
```

(On Mac, the user drags the folder from Finder to the chat — the absolute path pastes itself.)

The folder must have:
- 1 `.txt` file with the original caption/briefing (any name)
- 1+ images (`.png`, `.jpg`, `.jpeg`, `.webp`)

Output goes in `<folder>/desdobramento/`:
```
desdobramento/
├── instagram-feed.png             1080×1440, 3:4
├── instagram-feed.txt             short native IG caption (hook + CTA)
├── instagram-stories/
│   ├── story-01.png               1080×1920, safe zones respected
│   ├── story-02.png
│   ├── story-03.png
│   └── roteiro.txt                frame-by-frame script + stickers
├── linkedin-feed.png              1920×1080, 16:9, same master art in LinkedIn register
├── linkedin-feed.txt              LinkedIn caption (substantive, 1st person)
├── apresentacao-desdobramento.pdf PDF with base, pieces, and texts
├── output/                        clean folder with the finals for the user
└── manifest.json                  technical map of what was generated
```

When done, the most user-friendly folder is `<folder>/desdobramento/output/`. It gathers Feed, Stories, LinkedIn, and PDF with no logs, prompts, or technical files mixed in.

When finishing, report this final folder as a clickable link and list all generated files as clickable links, using absolute paths. Do not list `.md` files individually unless the person asks. If there are many files, still list all non-`.md`, grouped by format or subfolder. The complete technical folder stays in `<folder>/desdobramento/`.

---

## First run — zero-tech onboarding

The first time the user runs `/desdobrar`, the agent:

1. Checks whether the Higgsfield CLI is installed and logged in (`check-cli`).
2. If no CLI: explains in plain language that the Higgsfield CLI must be installed (`npm install -g @higgsfield/cli`).
3. If CLI exists but login is missing: asks the user to complete `higgsfield auth login`.
4. Then confirms with `higgsfield account status`.
5. If everything is OK: continues without talking about token, API key, or internal configuration.

**The user never touches a config file.** They do not see `.env`, token, or API key. For them, it is "Higgsfield is connected" and that's it.

---

## How each network is treated (unfolding, not redesign)

| Axis | IG Feed | IG Stories | LinkedIn Feed |
|---|---|---|---|
| **Consumption** | Thumb scrolling, 1-2s | 3-7s vertical mobile | Active reading 30-90s |
| **Virality** | Save + share + comment | View-through rate | Substantive comment + reshare |
| **Image** | Same master art in 3:4 | 3 variations in 9:16 of the same campaign/character | Same master art in 16:9 |
| **Lighting** | Preserve the original | Preserve the original | Preserve the original |
| **Palette** | Preserve the original | Preserve the original | Preserve the original |
| **Headline** | Keep typographic style of the master art | Same style, safe zones | Same style, more readable if needed |
| **Copy density** | 60-120 words, hook-in-2-lines | Minimal, 1 idea/frame | 160-320 articulated words |
| **Copy register** | Oral, rhythmic | Mobile telegram | Substantive editorial, 1st person |
| **CTA** | Light ("save", "comment") | Micro ("reply here") | Open question or silence |
| **Hashtag** | 3-7 at the end | Not used | 2-4 at the end |

The base image should not change by platform. The agent's first decision is to choose the **master art**:

- If there is an image already laid out with photo + lettering, it is the master art.
- If there are several images, choose the one closest to a finished piece.
- If there is no laid-out piece, choose the main image and keep its visual language.

All formats are born from this same master art, using `--base`. Other images only enter as secondary reference when they are clearly part of the same visual system. The script default is `--reference-mode base-only` to avoid drift.

The prompt should be short. GPT Image 2 understands the image: do not do a long analysis of the art. Just say the target format, the text that needs to go in, and what changes: crop, background/canvas, hierarchy, safe area, or lettering. Reinforce fidelity to the visible elements of the master art: do not remove, do not swap, do not invent objects.

Stories are always 3 frames. The three use the same master art as identity reference, but they cannot be a copy with swapped text. The image behind the text must change across the trio. Each Story must have its own text and background/image: vary crop, angle, pose, lighting, extended background, solid area, breathing room, or a nearby situation with the same character/product/campaign. One frame can be closer to the original, but the trio must look like a sequence with visual rhythm, without changing brand, font, palette, or language.

If the user requests a punctual swap on a piece already created, use the piece itself as `--base` and ask only for the swap. Example: keep everything the same and replace the headline with another, without changing photo, background, font, palette, or layout.

---

## Architecture

```
08. Desdobramento/
├── SKILL.md                           entrypoint + routing rule (three render paths)
├── AGENTS.md                          routing rules and compatibility
├── CLAUDE.md                          this file (internal refs for me)
├── DESDOBRAR.md                       full pipeline + inline prompts
└── scripts/desdobrar.py               Python stdlib infra calling Higgsfield CLI
```

Script subcommands (internal agent use, not exposed to user):
```
python3 "$SKILL_DIR/scripts/desdobrar.py" check-cli                                # status JSON
python3 "$SKILL_DIR/scripts/desdobrar.py" prep <folder>                            # scaffold + lists inputs
python3 "$SKILL_DIR/scripts/desdobrar.py" generate <folder> <format> <prompt> ...  # calls Higgsfield CLI + downloads
python3 "$SKILL_DIR/scripts/desdobrar.py" presentation-pdf <folder>                # final delivery PDF
python3 "$SKILL_DIR/scripts/desdobrar.py" download <url> <out>                     # debug
```

Formats accepted by `generate`: `ig-feed`, `ig-stories`, `linkedin-feed`.

`generate` uploads the master art with `higgsfield upload create`, captures the UUID, and calls `higgsfield generate create gpt_image_2` with `--image`. Uses `--base <name>` to define the master art. By default, the script sends only this base (`--reference-mode base-only`) to maintain consistency; use `--reference-mode all` only when the other images are deliberate references of the same system.

`presentation-pdf` assembles the final delivery as a PDF:
```
python3 "$SKILL_DIR/scripts/desdobrar.py" presentation-pdf <folder>
```
The PDF shows base text, base images, generated pieces, and final copies in a 16:9 presentation, with explicit sections for Base, Instagram Feed, Instagram Stories, Stories script, LinkedIn, and clean delivery. It should have clear layout, font with correct accents, identifiable pages, and no filenames on the page.

---

## Internal configuration

Generation depends on the local Higgsfield CLI login.

Optional variable:

```text
HIGGSFIELD_SOCIAL_IMAGE_MODEL=gpt_image_2
HIGGSFIELD_SOCIAL_IMAGE_QUALITY=high
HIGGSFIELD_IMAGE_RESOLUTION=2k
```

If not set, the script uses `gpt_image_2`, `high` quality, and `2k` resolution. The GPT Image 2 family is the mandatory **model** for all Human Social unfoldings (the final pieces have lettering, design, and text rendered together with the image) — but the **render path** (Higgsfield CLI scripted, Magnific direct with `mode: "gpt-2"`, or Magnific Hybrid Run Unlimited) follows the user's choice in the SKILL.md routing question.

---

## Principles

- **Zero-tech onboarding.** All necessary config is a question in chat, not a file instruction.
- **Always GPT Image 2 (the model family).** Every Human Social visual unfolding uses GPT Image 2 — `gpt_image_2` on Higgsfield or `mode: "gpt-2"` on Magnific, per the chosen render path.
- **Unfolding, not redesign.** The new piece must look like a direct sibling of the master art, not a new campaign inspired by it.
- **Base image always attached.** `generate` sends the master art as first reference. The default is to use only that base to preserve photo, font, palette, elements, and hierarchy.
- **Minimum prompt.** The model already sees the piece; the agent only states format, exact text, and allowed adjustments.
- **Stories in a trio.** Always generate 3 Stories from the same master art, with different texts, different images/backgrounds, and controlled variation of composition/scene/lighting.
- **Real native vision.** Claude opens each image with Read tool and decodes palette/mood on the fly. No cache, no pre-decoded save.
- **3 different copies from scratch.** IG ≠ LinkedIn. If they look alike, redo.
- **Final delivery in PDF.** Every completed execution must generate `apresentacao-desdobramento.pdf` with base, pieces, and texts.
- **Clean output.** Every completed execution syncs `desdobramento/output/` with the final files for the user.
- **Stateless.** Each run is fresh. No state, no multi-project, no multi-brand.
- **Failure in 1 format does not bring down the others.** Manifest records `ready` or `partial`.
