---
name: human-carrossel
description: Creates editorial Instagram carousels at scale — on-demand from a simple theme/text or automated via R1 (News Scout) + R2 (Carousel Creator). Does news research, editorial angle, headline, narrative spine, slide-by-slide copy, and visual render via Higgsfield CLI + GPT Image 2. Use whenever the user asks for "carousel", "Instagram carousel", "editorial carousel", "news-to-carousel post", "set up Notion + Routines automation", "re-render today's carousel", "swap the chosen news", "adjust a slide". Triggers (EN/PT) — carousel, carrossel, slide, Instagram editorial post, headline, manchete, narrative spine, espinha dorsal, R1 News Scout, R2 Carousel, Notion template, design system, GPT Image 2.
---

# Human Carrossel

System for creating editorial Instagram carousels. On-demand (simple theme/proprietary text) or automated (R1 monitors news → R2 creates and renders).

## Preflight — confirm the render provider is ready (first run)

Before the first render in a session, confirm the chosen provider is actually connected. Do not assume it is.

- Magnific (default, free): verify the Magnific MCP is connected — a quick account/credit balance check is the cheapest probe. If the Magnific MCP tools are not available, the connector is not set up.
- Higgsfield (paid): verify the higgsfield CLI is installed and logged in (e.g. higgsfield whoami). If the command is missing or not authenticated, it is not set up.

If the required provider is NOT ready:
1. Tell the user plainly which dependency is missing.
2. Route them to the human-setup skill for step-by-step, OS-specific setup (Mac/Windows).
3. Never hard-fail: meanwhile deliver the final English prompt ready to copy plus the exact provider command, so the user has something actionable immediately.

Only proceed to render once the provider is confirmed ready.

## Language

Mirror the user's language. Conversation in EN or PT. The carousel **copy itself** is produced in the brand's audience language — ask if not obvious.

## Complete intelligence (17 docs — read on demand)

- [00-README.md](00-README.md) — system overview
- [01-Brand-Identity.md](01-Brand-Identity.md) — brand identity operating the carousel
- [02-Setup-Wizard.md](02-Setup-Wizard.md) — initial wizard (identity, sources, Routines)
- [03-Notion-template.md](03-Notion-template.md) — Notion structure created by setup
- [04-Fontes-noticias.md](04-Fontes-noticias.md) — trusted news sources
- [05-Manual-Editorial.md](05-Manual-Editorial.md) — editorial rules + anti-AI-slop
- [06-Engine-de-Headlines.md](06-Engine-de-Headlines.md) — headline engine
- [07-Arquitetura-Narrativa.md](07-Arquitetura-Narrativa.md) — slide narrative spine
- [08-Design-System.md](08-Design-System.md) — visual system
- [09-Render-Engine.md](09-Render-Engine.md) — render via Higgsfield CLI
- [10-Referencias-de-Qualidade.md](10-Referencias-de-Qualidade.md), [11-Referencias-Visuais.md](11-Referencias-Visuais.md)
- [12-R1-News-Scout.md](12-R1-News-Scout.md) — R1 Routine (cloud)
- [13-R2-Routine-Local.md](13-R2-Routine-Local.md) — R2 Routine (local)
- [14-Input-Proprio.md](14-Input-Proprio.md) — on-demand carousel from a simple theme
- [15-Como-usar.md](15-Como-usar.md) — daily ops
- [16-Troubleshooting.md](16-Troubleshooting.md) — error diagnostics

## Internal routing

1. **New setup** → `02-Setup-Wizard.md` + `03-Notion-template.md`
2. **On-demand carousel** → `14-Input-Proprio.md`
3. **Daily ops** → `15-Como-usar.md`
4. **Configure Routines** → `12-R1-News-Scout.md` (cloud) + `13-R2-Routine-Local.md` (local)
5. **Error** → `16-Troubleshooting.md`

## Default output

```
<cwd>/human-output/carrossel/{run_slug}/
├── headline.md
├── spine.md
├── slides/
│   ├── 01.png
│   ├── 02.png
│   └── ...
├── copy.md
├── prompt.md
├── params.json
└── log.txt
```

## Non-negotiable rules

- **Visual render: Higgsfield CLI + GPT Image 2** (`gpt_image_2`), never Nano Banana 2 here. Always pass references as `--image` when they exist.
- Editorial > AI-slop: follow `05-Manual-Editorial.md` strictly.
- Headlines go through the engine `06-Engine-de-Headlines.md`.
- Slide structure follows `07-Arquitetura-Narrativa.md`.
- Before generating: confirm topic/news, slide count, aspect ratio (default 4:5 or 1:1), resolution, references, brand/identity, output folder.
- When something turns out bad, **edit the source of truth** (Notion/docs) — not just the Routine prompt.

## Final delivery

Final folder as clickable link + all generated PNGs/JPGs/JSONs as clickable links.
