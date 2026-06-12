---
name: human-image
description: Cinematic photo direction for AI image generation. Use whenever the user asks for an image, photo, still, frame, key visual, product shot, cover art, thumbnail, hero image, static ad, or visual prompt — or pastes a reference and asks to reproduce/transform it. Triggers (EN/PT) — "create an image", "make a photo", "generate a visual", "image prompt", "Nano Banana", "Magnific", "Higgsfield", "editorial image", "static ad", "cinematic photo", "key visual", "product photo", "crie uma imagem", "faça uma foto", "gere um visual", "prompt de imagem", "imagem editorial", "ad estático", "foto de produto". Before rendering, the skill asks the user to choose one of three render paths — Magnific direct (plan credits), Magnific Hybrid Run Unlimited (zero credits), or Higgsfield (paid).
---

# Human Image

Cinematic photo direction system with direct render. Turns a short idea, a visual reference, or a simple description into a high-level cinematic prompt and renders it through the chosen provider.

## Preflight — confirm the render provider is ready (first run)

Before the first render in a session, confirm the chosen provider is actually connected. Do not assume it is.

- Magnific: verify the `magnific-mcp` tools respond (call `account_balance` — the cheapest probe; it also shows remaining plan credits). If they do not respond, the MCP is not set up — route the user to human-setup.
- Higgsfield (paid): verify the higgsfield CLI is installed and logged in (e.g. higgsfield account status). If the command is missing or not authenticated, it is not set up.

If the required provider is NOT ready:
1. Tell the user plainly which dependency is missing.
2. Route them to the human-setup skill for step-by-step, OS-specific setup (Mac/Windows).
3. Never hard-fail: meanwhile deliver the final English prompt ready to copy plus the exact provider command, so the user has something actionable immediately.

Only proceed to render once the provider is confirmed ready.

## Visual generation routing

<!-- IMAGE_GENERATION_ROUTE_RULE -->
> Image generation rule: always use `imageprompts.md` as the creative/prompt guide when present. Before rendering any image, ask the user to choose one of the **three render paths**: 1) **Magnific MCP direto** — `magnific-mcp` tools (`images_generate` with `mode: "imagen-nano-banana-2-flash"`, `resolution: "1k"`; video via `video_generate` with `mode: "kling-25"`). Costs plan credits (~75/image), no extra money. 2) **Magnific Híbrido (Run Unlimited)** — zero credits: build a Space (`spaces_create` + `spaces_edit`) with pre-filled generator nodes, share the `webUrl`, the user clicks **Run Unlimited** in the browser, then collect results via `creations_search`/`spaces_state`. 3) **Higgsfield** — paid, the user's Higgsfield account and credits (MCP/CLI). The model parameter on Magnific is `mode`, never `model`. Use `account_balance` only to check/measure credits.
<!-- /IMAGE_GENERATION_ROUTE_RULE -->

**Always ask the render path.** Before each image render (or batch), present the three options and wait for an explicit choice — never assume. Ask it as: *"Como você quer renderizar? 1) Magnific direto (créditos do plano), 2) Híbrido Run Unlimited (zero créditos, você clica no navegador), 3) Higgsfield (pago)."* **Never silently render on Higgsfield** — the paid choice is always explicit.

Once the provider is chosen:
- **Magnific paths (direto or Híbrido):** `mode: "imagen-nano-banana-2-flash"` (Nano Banana 2), `resolution: "1k"`. Direto = `images_generate`; Híbrido = Space nodes + user clicks Run Unlimited.
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
2. **Ask the routing question** (the three render paths) per the rule above.
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

- Always follow the routing rule — never render without an explicit choice among the three paths.
- Image prompts are always written in English.
- Never save loose into a generic `output/` — always a per-run subfolder.
- Before calling paid APIs or running external commands, confirm the config exists.
- On Magnific, the model parameter is `mode` (never `model`); use `account_balance` only to check credits.

## Pre-render checklist

- [ ] Render path chosen (Magnific direto, Magnific Híbrido or Higgsfield)
- [ ] Aspect ratio confirmed
- [ ] Resolution confirmed
- [ ] References located (if any)
- [ ] Prompt includes camera + lens + light + texture + composition
- [ ] Output folder ready
- [ ] Chosen provider logged in (or prompt delivered as copy-paste fallback)

## Compatibility

Mac and Windows.
