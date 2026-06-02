---
name: human-social
description: Unfolds a folder containing text + images into native pieces for Instagram Feed, Instagram Stories, and LinkedIn Feed — not a resize, creates new images per platform with platform-native captions. Use whenever the user asks to "unfold this folder", "adapt for Instagram and LinkedIn", "create versions for feed/stories/linkedin", "make a post from this material", or points at a folder path asking for social content. Triggers (EN/PT) — unfold content, social adaptation, feed/stories/linkedin from folder, desdobrar pasta, adaptar pra Instagram e LinkedIn, criar versões pra redes, post a partir de pasta. Can be triggered as a sub-flow from any other skill that needs to unfold material into social pieces.
---

# Human Social

Takes a folder containing text + images and generates **native** pieces (not resize) for:
- Instagram Feed
- Instagram Stories (multi-card)
- LinkedIn Feed

Each platform gets a fresh image referencing the original material + its own caption.

## Language

Mirror the user's language. **Captions are written in the audience language** — ask if not obvious from the briefing.

## Complete intelligence

- [CLAUDE.md](CLAUDE.md) — skill overview
- [.claude/skills/desdobrar/SKILL.md](.claude/skills/desdobrar/SKILL.md) — full unfolding pipeline (inside the original skill)
- [scripts/desdobrar.py](scripts/desdobrar.py) — Python infra: validates key, prepares folder, generates and downloads assets
- [origem/](./origem) — example input (the previously generated `desdobramento/` was stripped from the distribution)

## Expected input

A folder containing:
- 1 `.txt` file with caption/briefing
- 1+ images (`.png`, `.jpg`, `.jpeg`, `.webp`)

## Mandatory flow

1. **Confirm the input folder path** (Mac: drag-and-drop; Windows: paste path from Explorer).
2. **Validate** that it has `.txt` + at least one image.
3. **Validate Higgsfield login**.
4. **Generate** Instagram Feed (1:1 or 4:5) with its own caption.
5. **Generate** Instagram Stories (9:16, multi-card with script).
6. **Generate** LinkedIn Feed (1.91:1 or 1:1) with a professional caption.
7. **Save** inside the input folder itself.

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
- Higgsfield CLI + Nano Banana 2 for visual render.
- Per-platform caption strategy:
  - IG Feed: visual, emotional, light CTA
  - IG Stories: conversational, can break into cards
  - LinkedIn: professional, strong hook, no excessive hashtags
- `manifest.json` always present for traceability.

## Shared sub-flow

If another skill (`human-team`, `human-cinematic`, `human-carrossel`, etc.) needs to unfold a material it produced into IG Feed/Stories/LinkedIn, it can trigger `human-social` as a sub-flow pointing to the source folder.

## Final delivery

`desdobramento/` folder as clickable link + all generated PNGs/JPGs/JSONs/captions as clickable links.
