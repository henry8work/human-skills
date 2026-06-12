---
name: human-team
description: Creative multi-agent team (OpenSquad) that turns an idea, reference, or material into a full production — brief, plan, concept, script, art direction, storyboard, teaser/main/secondary assets, ads in 9:16/4:5/16:9, copy-pack, Notion calendar, and handoff. Image rendering asks the user to choose one of three render paths — Magnific direct (plan credits), Magnific Hybrid Run Unlimited (zero credits), or Higgsfield (paid); video is always Higgsfield (Seedance/Kling). Use whenever the user asks for "full campaign", "creative team", "virtual agency", "multi-agent production", "OpenSquad", "turn this reference into a campaign", "I want the whole package — images, ads, copies, emails, calendar", "improve this script with the team", "finish this campaign". Triggers (EN/PT) — full campaign, creative squad, OpenSquad, campanha completa, time criativo, agência virtual, produção multi-agente. Routes to the default creative squad (not a generic menu).
---

# Human Team

Creative multi-agent team based on OpenSquad. Takes an idea/reference/material and returns structured production with human approval at checkpoints.

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

**Always ask the render path.** Before the visual phase begins, present the three options and wait for an explicit choice — never assume. Ask it as: *"Como você quer renderizar? 1) Magnific direto (créditos do plano), 2) Híbrido Run Unlimited (zero créditos, você clica no navegador), 3) Higgsfield (pago)."* **Never silently render on Higgsfield.**

Ask once at the start of the visual phase; the choice applies to teaser + main + secondary assets + ads. Video render is always Higgsfield (Seedance/Kling).

## Language

Mirror the user's language. Deliverables (briefs, scripts, copy) are produced in the target audience language — ask if not obvious.

## Complete intelligence

- [CLAUDE.md](CLAUDE.md) — general OpenSquad rules
- [README.md](README.md) — overview
- [squads/team/](./squads/team) — default creative squad
  - `pipeline/pipeline.yaml` + `pipeline/steps/` — execution pipeline (14 steps with human checkpoints)
  - `pipeline/data/campaign-delivery-system.md` — central reference for full campaign
  - `pipeline/data/expertise/` — per-role expertise files
  - `agents/` — the 10 specialized agents (Planner, Scout, Creative Director, Scriptwriter, Art Director, Storyboarder, Producer, Editor, Social Manager, Content Multiplier)
  - `_memory/` — clean seeds for memories/run history (copied to `<cwd>/human-output/team/_state/` on first run; never write inside the plugin directory)
- [_opensquad/core/](./_opensquad/core) — OpenSquad engine + base prompts
- [skills/](./skills) — helper skills (some need API keys; see "Helper-skill credentials" below)
- [dashboard/](./dashboard) — optional local Vite/React/Phaser dashboard (run `npm install && npm run dev` inside `dashboard/`; reads `_state/state.json`)
- The `/team` command lives at the plugin root (`commands/team.md`) and orchestrates this squad
- Playwright MCP config ships at the plugin root (`.mcp.json`)

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
- Always ask the image routing question (the three render paths) before rendering.
- Video render: Higgsfield (Seedance/Kling).
- Notion MCP is optional.
- Before generating any visual asset: confirm project, quantity, aspect ratio, resolution, references, purpose, output folder.

## Possible dependencies

- Claude Code, Node/npm/npx
- Playwright/MCP (web investigation)
- Notion MCP (calendar)
- OpenSquad engine (bundled)
- Magnific MCP/API or Higgsfield CLI logged in

## Helper-skill credentials

Some helper skills under [skills/](./skills) call external services that need API keys: **apify**, **blotato**, **canva**, **resend**, **instagram-publisher** (imgBB + Instagram Graph token). These are all **optional** — never block the pipeline on them. When a step would use one:

1. Check the corresponding env var (e.g. `APIFY_TOKEN`, `RESEND_API_KEY`) or ask the user where they keep it.
2. If the user doesn't have the key, say so in one sentence and offer the manual fallback (e.g. deliver the caption + image files for manual posting instead of instagram-publisher).
3. Never store keys in files inside the plugin directory; suggest the user's own `.env` in their project.

## Final delivery

`{run_id}/` folder as clickable link + list **all** non-`.md` files as clickable links.
