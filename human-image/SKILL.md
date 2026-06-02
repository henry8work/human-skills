---
name: human-image
description: Cinematic photo direction for AI image generation. Use whenever the user asks for an image, photo, still, frame, key visual, product shot, cover art, thumbnail, hero image, static ad, or visual prompt — or pastes a reference and asks to reproduce/transform it. Triggers (EN/PT) — "create an image", "make a photo", "generate a visual", "image prompt", "Nano Banana", "Magnific", "Higgsfield", "editorial image", "static ad", "cinematic photo", "key visual", "product photo", "crie uma imagem", "faça uma foto", "gere um visual", "prompt de imagem", "imagem editorial", "ad estático", "foto de produto". Before rendering, the skill asks the user to choose Magnific (free default) or Higgsfield (paid).
---

# Human Image

Cinematic photo direction system with direct render. Turns a short idea, a visual reference, or a simple description into a high-level cinematic prompt and renders it through the chosen provider.

## Visual generation routing

<!-- IMAGE_GENERATION_ROUTE_RULE -->
> Image generation rule: always use `imageprompts.md` as the creative/prompt guide when present. Before rendering any image, ask the user to choose: **Magnific** via direct MCP/API (`nano-banana-pro-flash`, `resolution: "1K"`, intended free/default) or **Higgsfield** via MCP/CLI (paid). Do not use `mcp__magnific_oauth.images_generate` for routine Magnific image generation unless explicitly requested; use `magnific-oauth.account_balance` only to check/measure credits.
<!-- /IMAGE_GENERATION_ROUTE_RULE -->

**Default: Magnific (free).** Before each image render, briefly tell the user *"Going with Magnific (free) — switch to Higgsfield (paid)?"* If they don't push back, proceed with Magnific. If they ask for Higgsfield, switch. **Never silently render on Higgsfield** — the paid choice is always explicit.

Once the provider is chosen:
- **Magnific path:** `nano-banana-pro-flash`, `resolution: "1K"`, default rendering.
- **Higgsfield path:** Higgsfield CLI, default model `nano_banana_2`, 2k unless specified.

## Language

Mirror the user's language. If they write in Portuguese, respond in Portuguese. If in English, respond in English. **The image prompts themselves are always in English**, regardless of the conversation language — Nano Banana models were trained on English captions.

## Complete intelligence

Prompt logic (camera, lens, light, texture, composition, output formats) lives in [imageprompts.md](imageprompts.md). Read it before crafting any prompt.

## Mandatory flow

1. **Confirm or safely deduce** before rendering:
   - project name / run slug
   - quantity of images
   - aspect ratio: `auto`, `1:1`, `3:2`, `2:3`, `4:3`, `3:4`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`
   - resolution: `1k` (Magnific default), `2k` (Higgsfield default), `4k` (only when explicitly requested)
   - references (if any, pass them appropriately to the chosen provider)
   - purpose (ad, editorial, hero, cover, thumb…)
   - output folder
2. **Ask the routing question** (Magnific vs Higgsfield) per the rule above.
3. **Build the prompt** following `imageprompts.md` — always with photographic physics: camera, lens, light, subject, foreground/midground/background, texture, tonal behavior, composition, art direction, aspect ratio, size.
4. **Render** through the chosen provider. If the tooling isn't installed/logged in, deliver the prompt ready to copy + the exact command for that provider.
5. **Save** under a per-run subfolder with the prompt used and metadata:
   ```
   <cwd>/human-output/image/{run_slug}/
   ├── prompt.md
   ├── params.json
   ├── images/
   └── log.txt
   ```
6. **Final delivery** — report the final folder as a clickable link + list every non-`.md` file as clickable links (absolute paths).

## Non-negotiable rules

- Always follow the routing rule — never assume Magnific or Higgsfield without asking.
- Image prompts are always written in English.
- Never save loose into a generic `output/` — always a per-run subfolder.
- Before calling paid APIs or running external commands, confirm the config exists.
- Do not call `mcp__magnific_oauth.images_generate` for routine generation; use `magnific-oauth.account_balance` only to check credits.

## Pre-render checklist

- [ ] Provider chosen (Magnific or Higgsfield)
- [ ] Aspect ratio confirmed
- [ ] Resolution confirmed
- [ ] References located (if any)
- [ ] Prompt includes camera + lens + light + texture + composition
- [ ] Output folder ready
- [ ] Chosen provider logged in (or prompt delivered as copy-paste fallback)

## Compatibility

Mac and Windows.
