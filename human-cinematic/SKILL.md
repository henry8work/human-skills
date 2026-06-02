---
name: human-cinematic
description: Full cinematic production — impossible product shots, video campaigns, scripts, character sheets, approved frames, and videos via Higgsfield. Use whenever the user asks for "product shot", "cinematic product ad", "video campaign", "short film", "film/commercial script", "frame per scene", "video with Seedance/Kling", "recurring character", or pastes an amateur product photo asking for a premium ad. Triggers (EN/PT) — product shot, premium ad, cinematic campaign, script, roteiro, storyboard, character sheet, frame, Seedance, Kling, Nano Banana 2, IMAX, foto de produto pra ad, anúncio premium. HERO-FIRST flow for single product shots; video only after frames are approved.
---

# Human Cinematic

Cinematic production system. Guides from idea → campaign with script, references, characters, character sheets, approved frames, and videos via Higgsfield.

## Language

Mirror the user's language. Conversation can be EN or PT. **Image prompts for Nano Banana 2 are always in English. Video prompts for Seedance are in Chinese** when the framework requires it (see `seedance-prompt-framework.md`).

## Complete intelligence

- [CLAUDE.md](CLAUDE.md) — core agent rules
- [COMECE-AQUI.md](COMECE-AQUI.md) — main operational manual (campaigns, refs, frames, videos) — PT, but methodology applies regardless of language
- [PRODUCT-SHOTS.md](PRODUCT-SHOTS.md) — premium Product Shots flow (Visual Intent → iteration → inpainting → final polish)
- [SCRIPT_AI_SYSTEM.md](SCRIPT_AI_SYSTEM.md) — script system
- [seedance-prompt-framework.md](seedance-prompt-framework.md) — prompt framework (Seedance in Chinese, Nano Banana 2 in English)
- [SETUP-GUIDE.md](SETUP-GUIDE.md) — technical setup
- [_template/](./_template) — base template for a new campaign
- [campaigns/](./campaigns) — existing campaigns

## Internal routing by intent

1. **Detect the mode:**
   - Impossible Product Shots → `PRODUCT-SHOTS.md`
   - Full campaign (script + frames + video) → `COMECE-AQUI.md`
   - Script only → `SCRIPT_AI_SYSTEM.md`
   - Status / continue campaign → `campaigns/{name}/`
2. **Product Shots:** Visual Intent → generation/iteration/inpainting → final polish with upscale and product-fidelity checklist.
3. **Campaign:** detect if user has a script or needs Script AI → create `campaigns/{name}/` from `_template/` → references in `internal/` → character sheets when there's a recurring character → 1 frame per scene → **human approval** → videos.

## Default output

```
<cwd>/human-output/cinematic/{run_slug}/
├── internal/      (handoff, refs, UUIDs, descriptors, logs, feedback)
└── output/        (clean numbered results)
```

## Non-negotiable rules

- **Video only after frames are approved** by the human.
- Higgsfield CLI is the only render path.
- Images: Nano Banana 2 (`nano_banana_2`); video: Seedance or Kling depending on the request.
- Nano Banana 2 prompts in English; Seedance prompts in Chinese when the framework requires.
- Before generating: confirm project, quantity, aspect ratio, resolution, references, purpose, output folder.

## Final delivery

Report the **final folder** as a clickable link + list non-`.md` files as clickable links.

## Compatibility

Mac and Windows. Possible dependencies: Claude Code, Node/npm, Higgsfield CLI logged in, models Seedance/Nano Banana 2/Kling.
