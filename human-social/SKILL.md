---
name: human-social
description: Unfolds a folder containing text + images into native pieces for Instagram Feed, Instagram Stories, and LinkedIn Feed — not a resize, creates new images per platform with platform-native captions. Image render asks the user to choose Magnific (free default) or Higgsfield (paid). Use whenever the user asks to "unfold this folder", "adapt for Instagram and LinkedIn", "create versions for feed/stories/linkedin", "make a post from this material", or points at a folder path asking for social content. Triggers (EN/PT) — unfold content, social adaptation, feed/stories/linkedin from folder, desdobrar pasta, adaptar pra Instagram e LinkedIn, criar versões pra redes, post a partir de pasta. Can be triggered as a sub-flow from any other skill that needs to unfold material into social pieces.
---

# Human Social

Takes a folder containing text + images and generates **native** pieces (not resize) for:
- Instagram Feed
- Instagram Stories (multi-card)
- LinkedIn Feed

Each platform gets a fresh image referencing the original material + its own caption.

## Visual generation routing

<!-- IMAGE_GENERATION_ROUTE_RULE -->
> Image generation rule: always use `imageprompts.md` as the creative/prompt guide when present. Before rendering any image, ask the user to choose: **Magnific** via direct MCP/API (`nano-banana-pro-flash`, `resolution: "1K"`, intended free/default) or **Higgsfield** via MCP/CLI (paid). Do not use `mcp__magnific_oauth.images_generate` for routine Magnific image generation unless explicitly requested; use `magnific-oauth.account_balance` only to check/measure credits.
<!-- /IMAGE_GENERATION_ROUTE_RULE -->

**Default: Magnific (free).** At the start of each unfold run, briefly tell the user *"Going with Magnific (free) — switch to Higgsfield (paid)?"* If they don't push back, proceed with Magnific for all three platforms. If they ask for Higgsfield, switch. **Never silently render on Higgsfield.**

## Language

Mirror the user's language. **Captions are written in the audience language** — ask if not obvious from the briefing.

## Complete intelligence

- [CLAUDE.md](CLAUDE.md) — skill overview
- [.claude/skills/desdobrar/SKILL.md](.claude/skills/desdobrar/SKILL.md) — full unfolding pipeline (inside the original skill)
- [scripts/desdobrar.py](scripts/desdobrar.py) — Python infra
- [origem/](./origem) — example input

## Expected input

A folder containing:
- 1 `.txt` file with caption/briefing
- 1+ images (`.png`, `.jpg`, `.jpeg`, `.webp`)

## Mandatory flow

1. **Confirm the input folder path**.
2. **Validate** that it has `.txt` + at least one image.
3. **Ask the routing question** (Magnific vs Higgsfield) per the rule above.
4. **Validate** the chosen provider is logged in.
5. **Generate** Instagram Feed (1:1 or 4:5) with its own caption.
6. **Generate** Instagram Stories (9:16, multi-card with script).
7. **Generate** LinkedIn Feed (1.91:1 or 1:1) with a professional caption.
8. **Save** inside the input folder itself.

## Default output (EXCEPTION to the global rule)

Unlike other skills, Human Social writes **inside the input folder**, not under `human-output/`:

```
<input-folder>/desdobramento/
├── instagram-feed.png
├── instagram-feed.txt
├── instagram-stories/
│   ├── story-01.png
│   ├── story-02.png
│   └── roteiro.txt
├── linkedin-feed.png
├── linkedin-feed.txt
└── manifest.json
```

## Non-negotiable rules

- **No resize** — always create a fresh image per platform with a reference chain.
- Always ask the routing question before rendering.
- Per-platform caption strategy:
  - IG Feed: visual, emotional, light CTA
  - IG Stories: conversational, can break into cards
  - LinkedIn: professional, strong hook, no excessive hashtags
- `manifest.json` always present for traceability.

## Shared sub-flow

If another skill needs to unfold a material it produced into IG Feed/Stories/LinkedIn, it can trigger `human-social` as a sub-flow pointing to the source folder.

## Final delivery

`desdobramento/` folder as clickable link + all generated PNGs/JPGs/JSONs/captions as clickable links.
