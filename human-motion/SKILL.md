---
name: human-motion
description: Terminal-based video and motion graphics via Remotion — creates motion-graphics Reels, edits existing videos with titles/captions/cuts, applies pacing, beat-matching, caption design, and renders MP4. When an AI-generated image/frame/texture/background is needed, generates via Higgsfield CLI + Nano Banana 2 and feeds it as a local file into the Remotion project. Use whenever the user asks for "Reel", "motion graphics", "video from the terminal", "Remotion", "create a Reel from a prompt", "edit video with title/caption", "rhythm/pacing/beat-match", "animated captions", "render MP4". Triggers (EN/PT) — motion graphics, animated Reel, Remotion, caption design, beat-matching, decupagem, render MP4 terminal, vídeo no terminal.
---

# Human Motion

Video and motion graphics system via Remotion in the terminal. Creates Reels, edits existing videos, applies pacing/beat-matching, renders MP4.

## Language

Mirror the user's language. **Caption design respects the audience language** — ask if not obvious.

## Complete intelligence

- [Motion.md](Motion.md) — operating system of the Human Motion agent
- [AGENTS.md](AGENTS.md) — core rules
- [Decupagem_Nubank_Isso_e_Eficiencia.md](Decupagem_Nubank_Isso_e_Eficiencia.md) — deep "decupagem" case study (scene-by-scene visual breakdown of a public Nubank ad, used as a methodology reference for rhythm, beats, asset planning, and Remotion translation). The referenced asset files (in a `nubank/` folder) are not included in this distribution — the case study is for **method**, not for reproduction.

## Mandatory flow

1. **Briefing** — understand if it's a new Reel (motion graphics) or an edit of an existing video.
2. **Beat sheet** — break the script into beats with timing.
3. **Timeline** — sequence of scenes, transitions, easing.
4. **Caption design** — typography, position, animation.
5. **Asset plan** — list images/frames/textures needed. If AI-generated, render via Higgsfield CLI + Nano Banana 2 **before** Remotion reads them.
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
│   ├── images/      (Higgsfield → Nano Banana 2)
│   ├── video-in/
│   └── audio/
├── remotion/        (local Remotion project)
├── renders/
│   └── final.mp4
└── log.txt
```

## Non-negotiable rules

- AI assets: Higgsfield CLI + Nano Banana 2. Before generating: confirm project, quantity, aspect ratio, resolution, references, purpose, folder.
- Don't skip QC — pacing, legibility, and render must be checked before declaring done.
- Mac and Windows compatible (Node LTS, npm, Remotion, FFmpeg via Remotion env).
- Reels in 9:16 by default; document when it's another aspect.

## Possible dependencies

- Claude Code
- Node.js LTS + npm
- Remotion (`npx create-video@latest` when a new project is needed)
- Higgsfield CLI for any AI visual asset
- FFmpeg/codecs (ship with Remotion env)

## Final delivery

`{project_slug}/` folder as clickable link + `final.mp4` and all generated MP4/PNG/MP3/WAV as clickable links.
