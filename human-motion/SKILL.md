---
name: human-motion
description: Terminal-based video and motion graphics via Remotion — creates motion-graphics Reels, edits existing videos with titles/captions/cuts, applies pacing, beat-matching, caption design, and renders MP4. When an AI-generated image/frame/texture/background is needed, asks the user to choose Magnific (free default) or Higgsfield (paid). Use whenever the user asks for "Reel", "motion graphics", "video from the terminal", "Remotion", "create a Reel from a prompt", "edit video with title/caption", "rhythm/pacing/beat-match", "animated captions", "render MP4". Triggers (EN/PT) — motion graphics, animated Reel, Remotion, caption design, beat-matching, decupagem, render MP4 terminal, vídeo no terminal.
---

# Human Motion

Video and motion graphics system via Remotion in the terminal. Creates Reels, edits existing videos, applies pacing/beat-matching, renders MP4.

## Preflight — confirm the render provider is ready (first run)

Before the first render in a session, confirm the chosen provider is actually connected. Do not assume it is.

- Magnific (default, free): verify the Magnific MCP is connected — a quick account/credit balance check is the cheapest probe. If the Magnific MCP tools are not available, the connector is not set up.
- Higgsfield (paid): verify the higgsfield CLI is installed and logged in (e.g. higgsfield whoami). If the command is missing or not authenticated, it is not set up.

If the required provider is NOT ready:
1. Tell the user plainly which dependency is missing.
2. Route them to the human-setup skill for step-by-step, OS-specific setup (Mac/Windows).
3. Never hard-fail: meanwhile deliver the final English prompt ready to copy plus the exact provider command, so the user has something actionable immediately.

Only proceed to render once the provider is confirmed ready.

## Visual generation routing

<!-- IMAGE_GENERATION_ROUTE_RULE -->
> Image generation rule: always use `imageprompts.md` as the creative/prompt guide when present. Before rendering any image, ask the user to choose: **Magnific** via direct MCP/API (`nano-banana-pro-flash`, `resolution: "1K"`, intended free/default) or **Higgsfield** via MCP/CLI (paid). Do not use `mcp__magnific_oauth.images_generate` for routine Magnific image generation unless explicitly requested; use `magnific-oauth.account_balance` only to check/measure credits.
<!-- /IMAGE_GENERATION_ROUTE_RULE -->

**Default: Magnific (free).** When the asset plan needs AI-generated stills, briefly tell the user *"Going with Magnific (free) — switch to Higgsfield (paid)?"* If they don't push back, proceed with Magnific for all stills. If they ask for Higgsfield, switch. **Never silently render on Higgsfield.**

Applies to every still asset the Remotion timeline consumes (frames, textures, backgrounds, thumbs). Ask once per project at the asset-plan stage; the choice applies to all stills in the run.

## Language

Mirror the user's language. **Caption design respects the audience language** — ask if not obvious.

## Complete intelligence

- [Motion.md](Motion.md) — operating system of the Human Motion agent
- [AGENTS.md](AGENTS.md) — core rules
- [Decupagem_Nubank_Isso_e_Eficiencia.md](Decupagem_Nubank_Isso_e_Eficiencia.md) — deep "decupagem" case study (scene-by-scene visual breakdown of a public Nubank ad, used as a methodology reference). The referenced asset files (in a `nubank/` folder) are not included in this distribution — the case study is for **method**, not for reproduction.

## Mandatory flow

1. **Briefing** — new Reel (motion graphics) or edit of existing video?
2. **Beat sheet** — break the script into beats with timing.
3. **Timeline** — sequence of scenes, transitions, easing.
4. **Caption design** — typography, position, animation.
5. **Asset plan** — list images/frames/textures needed. If AI-generated, **ask the routing question** (Magnific vs Higgsfield) and render **before** Remotion reads them.
6. **Remotion project** — create local project or reproducible technical plan.
7. **Preview/render** — commands `npm start` (preview) and `npx remotion render` (MP4).
8. **Final QC** — pacing, legibility, beat-matching, audio sync.

## Default output

```
<cwd>/human-output/motion/{project_slug}/
├── brief.md
├── beat-sheet.md
├── timeline.md
├── caption-design.md
├── asset-plan.md
├── assets/
│   ├── images/      (chosen provider per the routing rule)
│   ├── video-in/
│   └── audio/
├── remotion/        (local Remotion project)
├── renders/
│   └── final.mp4
└── log.txt
```

## Non-negotiable rules

- Always ask the image routing question before rendering any still.
- Don't skip QC — pacing, legibility, render checked before declaring done.
- Mac and Windows compatible (Node LTS, npm, Remotion, FFmpeg via Remotion env).
- Reels in 9:16 by default; document when it's another aspect.

## Possible dependencies

- Claude Code
- Node.js LTS + npm
- Remotion (`npx create-video@latest` when a new project is needed)
- Magnific MCP/API or Higgsfield CLI (for AI stills)
- FFmpeg/codecs (ship with Remotion env)

## Final delivery

`{project_slug}/` folder as clickable link + `final.mp4` and all generated MP4/PNG/MP3/WAV as clickable links.
