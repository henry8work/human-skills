---
name: human-cinematic
description: Full cinematic production — impossible product shots, video campaigns, scripts, character sheets, approved frames, and videos. Images via Magnific or Higgsfield (user choice); videos via Higgsfield (Seedance/Kling). Use whenever the user asks for "product shot", "cinematic product ad", "video campaign", "short film", "film/commercial script", "frame per scene", "video with Seedance/Kling", "recurring character", or pastes an amateur product photo asking for a premium ad. Triggers (EN/PT) — product shot, premium ad, cinematic campaign, script, roteiro, storyboard, character sheet, frame, Seedance, Kling, Nano Banana, Magnific, Higgsfield, IMAX, foto de produto pra ad, anúncio premium. HERO-FIRST flow for single product shots; video only after frames are approved.
---

# Human Cinematic

Cinematic production system. Guides from idea → campaign with script, references, characters, character sheets, approved frames, and videos.

## Visual generation routing

<!-- IMAGE_GENERATION_ROUTE_RULE -->
> Image generation rule: always use `imageprompts.md` as the creative/prompt guide when present. Before rendering any image, ask the user to choose: **Magnific** via direct MCP/API (`nano-banana-pro-flash`, `resolution: "1K"`, intended free/default) or **Higgsfield** via MCP/CLI (paid). Do not use `mcp__magnific_oauth.images_generate` for routine Magnific image generation unless explicitly requested; use `magnific-oauth.account_balance` only to check/measure credits.
<!-- /IMAGE_GENERATION_ROUTE_RULE -->

**Default: Magnific (free).** Before the first image render of each campaign batch, briefly tell the user *"Going with Magnific (free) — switch to Higgsfield (paid)?"* If they don't push back, proceed with Magnific. If they ask for Higgsfield, switch. **Never silently render on Higgsfield.**

Video generation is always Higgsfield (Seedance or Kling) — the routing question applies only to image frames/refs/character sheets, not to video render.

## Language

Mirror the user's language. Conversation can be EN or PT. **Image prompts are always in English. Video prompts for Seedance are in Chinese** when the framework requires (see `seedance-prompt-framework.md`).

## Complete intelligence

- [CLAUDE.md](CLAUDE.md) — core agent rules
- [COMECE-AQUI.md](COMECE-AQUI.md) — main operational manual (PT, methodology applies regardless of language)
- [PRODUCT-SHOTS.md](PRODUCT-SHOTS.md) — premium Product Shots flow
- [SCRIPT_AI_SYSTEM.md](SCRIPT_AI_SYSTEM.md) — script system
- [seedance-prompt-framework.md](seedance-prompt-framework.md) — prompt framework
- [SETUP-GUIDE.md](SETUP-GUIDE.md) — technical setup
- [_template/](./_template) — base template for new campaigns
- [campaigns/](./campaigns) — existing campaigns

## Internal routing by intent

1. **Detect the mode:**
   - Impossible Product Shots → `PRODUCT-SHOTS.md`
   - Full campaign (script + frames + video) → `COMECE-AQUI.md`
   - Script only → `SCRIPT_AI_SYSTEM.md`
   - Status / continue campaign → `campaigns/{name}/`
2. **Product Shots:** Visual Intent → ask provider (Magnific/Higgsfield) → generation/iteration/inpainting → final polish.
3. **Campaign:** detect if user has a script or needs Script AI → create `campaigns/{name}/` from `_template/` → references in `internal/` → character sheets when there's a recurring character → ask provider for each image batch → 1 frame per scene → **human approval** → videos (Higgsfield Seedance/Kling).

## Default output

```
<cwd>/human-output/cinematic/{run_slug}/
├── internal/      (handoff, refs, UUIDs, descriptors, logs, feedback)
└── output/        (clean numbered results)
```

## Non-negotiable rules

- **Video only after frames are approved** by the human.
- Always follow the image routing rule above — ask Magnific or Higgsfield before rendering.
- Video render: Higgsfield (Seedance or Kling).
- Image prompts in English; Seedance prompts in Chinese when the framework requires.
- Before generating: confirm project, quantity, aspect ratio, resolution, references, purpose, output folder.

## Final delivery

Report the **final folder** as a clickable link + list non-`.md` files as clickable links.

## Compatibility

Mac and Windows. Possible dependencies: Claude Code, Node/npm, Magnific MCP/API or Higgsfield CLI logged in.
