---
name: human-team
description: Creative multi-agent team (OpenSquad) that turns an idea, reference, or existing material into a structured full production — brief, plan, dossier, concept, script, art direction, storyboard, production sheet, teaser/main/secondary assets, ads in 9:16/4:5/16:9, copy-pack, Notion calendar, and handoff. Use whenever the user asks for "full campaign", "creative team", "virtual agency", "multi-agent production", "OpenSquad", "turn this reference into a campaign", "I have a product brief and want the whole package — images, ads, copies, emails, and calendar", "improve this script with the team", "finish this campaign". Triggers (EN/PT) — full campaign, creative squad, multi-agent pipeline, OpenSquad, campanha completa, time criativo, agência virtual, produção multi-agente, brief de produto pacote completo. Routes to the default creative squad (not a generic menu).
---

# Human Team

Creative multi-agent team based on OpenSquad. Takes an idea/reference/material and returns structured production with human approval at checkpoints.

## Language

Mirror the user's language. Deliverables (briefs, scripts, copy) are produced in the target audience language — ask if not obvious.

## Complete intelligence

- [CLAUDE.md](CLAUDE.md) — general OpenSquad rules
- [README.md](README.md) — overview
- [squads/team/](./squads/team) — default creative squad
  - `pipeline/` — execution pipeline
  - `pipeline/data/campaign-delivery-system.md` — central reference for full campaign
  - `agents/` — specialized agents (Planner, Art Director, Producer, Social Manager, Content Multiplier…)
- [_opensquad/core/](./_opensquad/core) — OpenSquad engine + base prompts
- [skills/](./skills) — helper skills
- [dashboard/](./dashboard) — local Vite/React/Phaser dashboard (optional)
- [BUD/](./BUD) — auxiliary resources
- [.mcp.json](.mcp.json) — MCP config

## Routing by intent

The skill **does not open a generic menu**. It identifies the entry mode immediately:

1. **Start from scratch** — just an idea
2. **Continue a base** — existing material
3. **Improve something** — refine script/piece
4. **Analyze reference** — extract angle from example
5. **Finalize production** — close what's missing
6. **Full campaign** — full scope → activates `campaign-delivery-system.md`

In full-campaign mode: Planner defines the package → Art Director handles visual identity and continuity → Producer organizes assets and folders → Social Manager builds Notion MCP/CSV calendar → Content Multiplier closes derivatives and copies.

## Default output

```
<cwd>/human-output/team/{run_id}/
├── brief.md
├── projeto.md
├── plano.md
├── dossie.md
├── conceito.md
├── roteiro.md
├── art-bible.md
├── storyboard.md
├── folha-producao.md
├── copy-pack.md
├── master.md
├── publicacao.md
├── multiplicacao.md
├── handoff.md
├── assets/
│   ├── teaser/
│   ├── principais/
│   └── secundarias/
├── ads/
│   ├── 9x16/
│   ├── 4x5/
│   └── 16x9/
└── calendar/
    ├── notion-calendar.md
    └── calendar.csv
```

## Full-campaign delivery

- `projeto.md` with objective, audience, promise, channels, formats, success criteria, risks
- Teaser + main + secondary assets with continuity of outfit/look/product
- Ads in 9:16, 4:5, 16:9 with headline, primary text, CTA, safe zones
- `copy-pack.md` with campaign copy, posts, ads, emails, CTAs, voiceover
- Calendar ready for Notion MCP or CSV import
- `handoff.md` with files, pendings, external tools, next actions

## Non-negotiable rules

- **Do not skip human checkpoints.**
- Video only after frames are approved.
- Visual render: Higgsfield CLI + Nano Banana 2 (images); Seedance/Kling (video).
- Notion MCP is optional.
- Before generating any visual asset: confirm project, quantity, aspect ratio, resolution, references, purpose, output folder.

## Possible dependencies

- Claude Code, Node/npm/npx
- Playwright/MCP (web investigation)
- Notion MCP (calendar)
- OpenSquad engine (bundled)
- Higgsfield CLI logged in

## Final delivery

`{run_id}/` folder as clickable link + list **all** non-`.md` files as clickable links.
