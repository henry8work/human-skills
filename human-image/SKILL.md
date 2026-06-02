---
name: human-image
description: Cinematic photo direction for AI image generation via Higgsfield CLI + Nano Banana 2. Use whenever the user asks for an image, photo, still, frame, key visual, product shot, cover art, thumbnail, hero image, static ad, or visual prompt — or pastes a reference and asks to reproduce/transform it. Triggers (EN/PT) — "create an image", "make a photo", "generate a visual", "image prompt", "Nano Banana", "Higgsfield", "editorial image", "static ad", "cinematic photo", "key visual", "product photo", "crie uma imagem", "faça uma foto", "gere um visual", "prompt de imagem", "imagem editorial", "ad estático", "foto de produto". Default model: Nano Banana 2 (`nano_banana_2`) via Higgsfield CLI, 2k, aspect ratio confirmed with the user.
---

# Human Image

Cinematic photo direction system with direct render. Turns a short idea, a visual reference, or a simple description into a high-level cinematic prompt and renders it via **Higgsfield CLI + Nano Banana 2** (`nano_banana_2`).

## Language

Mirror the user's language. If they write in Portuguese, respond in Portuguese. If in English, respond in English. **The image prompts themselves are always in English**, regardless of the conversation language — Nano Banana 2 was trained on English captions.

## Complete intelligence

Prompt logic (camera, lens, light, texture, composition, output formats) lives in [imageprompts.md](imageprompts.md). Read it before crafting any prompt.

## Mandatory flow

1. **Confirm or safely deduce** before rendering:
   - project name / run slug
   - quantity of images
   - aspect ratio: `auto`, `1:1`, `3:2`, `2:3`, `4:3`, `3:4`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`
   - resolution: `1k`, `2k` (default), `4k` (only when explicitly requested or for high-detail delivery)
   - references (if any, pass them as `--image`)
   - purpose (ad, editorial, hero, cover, thumb…)
   - output folder
2. **Build the prompt** following `imageprompts.md` — always with photographic physics: camera, lens, light, subject, foreground/midground/background, texture, tonal behavior, composition, art direction, aspect ratio, size.
3. **Render** via Higgsfield CLI with `nano_banana_2`. If the CLI isn't installed in the environment, deliver the prompt ready to copy + the exact command.
4. **Save** under a per-run subfolder with the prompt used and metadata:
   ```
   <cwd>/human-output/image/{run_slug}/
   ├── prompt.md
   ├── params.json
   ├── images/
   └── log.txt
   ```
5. **Final delivery** — report the final folder as a clickable link + list every non-`.md` file as clickable links (absolute paths).

## Non-negotiable rules

- Higgsfield CLI is the only path (never Higgs MCP, fal.ai, Flow AI).
- Nano Banana 2 is the default model; never switch without an explicit user request.
- Image prompts are always written in English.
- Never save loose into a generic `output/` — always a per-run subfolder.
- Before calling paid APIs or running external commands, confirm the config exists.

## Pre-render checklist

- [ ] Aspect ratio confirmed
- [ ] Resolution confirmed
- [ ] References located (if any)
- [ ] Prompt includes camera + lens + light + texture + composition
- [ ] Output folder ready
- [ ] Higgsfield CLI logged in (or prompt delivered as copy-paste fallback)

## Compatibility

Mac and Windows.
