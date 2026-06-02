# News-to-Carrossel V2.5

Instagram carousel generation system with two fronts: on-demand carousel from a theme or original content, and daily automated generation from news. The editorial pipeline handles research, triage, headline, narrative architecture, validation and coherent visual render via fixed reference on the Higgsfield CLI: cover generated first, then internal slides in parallel using cover + brand visual references.

**White-label.** The base system is not tied to any brand. Visual and editorial identity come from the `🏷️ Brand Identity` page in Notion (color, handle, niche, audience, editorial reference outlet). Swapping brands = swap the content of that page + the visual references.

---

## Architecture (V2.5 — Claude Desktop Routines)

| Component | Where it runs | Why |
|---|---|---|
| **R1 — News Scout** | **Remote** Routine (Anthropic cloud) | Only talks to Notion, Drive, web search — the sandbox covers it, Mac can be closed |
| **R2 — Carousel Creator** | **Local** Routine (Claude Code Desktop, Mac/Windows) | Needs Higgsfield CLI, real vision on refs, parallel render — Local Routine has open network + filesystem + MCPs |
| **Initial setup** | Claude Code CLI + Notion Integration Token | Creates 2 databases + 10 sub-pages via REST API in ~30s |

V2.5 replaces the V2 apparatus of scripts + `launchd` + Homebrew (jq/imagemagick/rclone/local python) with **a single Local Routine** inside Claude Desktop. Schedule + catch-up built-in, with no external dependencies.

---

## How the daily cycle works

**1. During the day** (9am / 1pm / 5pm, configurable)
- R1 (**Remote** Routine) scans news sources via `web_search` + `web_fetch`, deduplicates, writes title/summary/relevance/link to the `🗞️ News Feed` database
- R1 does not download images (the Remote sandbox blocks direct HTTP) — it only does best-effort to discover the image URL and writes a textual **Visual hint**. Actual image extraction is left to R2 (Local)

**2. In the morning** (Schedule `*/30 8-22`, target 08:00)
- The **Local** R2 Routine fires on the first `*/30` tick of the day in which Claude Desktop is open
- Subsequent ticks detect `.completed` and soft-exit in ~2s (negligible cost)
- Automatic catch-up: if the app was closed for hours, it fires 1 missed run upon opening
- R2 reads Brand Identity, picks a news item, runs the entire editorial pipeline as **a single Claude session** with Bash + MCPs
- **Extracts the photo from the chosen news item** (Step 1.5 — local cascade, open network); if there is no good photo, generates from R1's Visual hint
- Decodes visual references with **native vision** (auto-detects grids)
- Generates cover via Higgsfield CLI + GPT Image 2 (`higgsfield upload create` + `higgsfield generate create gpt_image_2`)
- Generates slides 2-9 **in parallel** with **cover + brand visual refs + news photo** as reference UUIDs (slide-to-slide coherence)
- Applies the logo via Pillow composition (slides 1 and 9) without changing proportion/size, saves the 9 slides to the local folder and to Drive, logs in Notion

**3. The next morning**
- You open Notion, see the carousel ready, download, post on Instagram
- If the visual came out weak: send `--re-render` in the Routine's session (re-runs only visual, reusing the editorial pipeline already done — cheap)
- If the chosen news wasn't good: override via `--news=N` in the first message of the next Run now

---

## How it works for a theme or original content

When someone asks something simple like:

```text
/carrossel I want a carousel about electric bicycles in São Paulo
```

the system does not expect a perfect brief. It takes ownership of the research and the strategy:

1. interprets the theme;
2. researches context, recent data and behavioral signals;
3. chooses a specific editorial angle;
4. creates the headline and 9-slide narrative architecture;
5. generates caption and visual direction;
6. renders when the brand is already configured, or delivers the complete plan for rendering.

This mode lives in `14-Input-Proprio.md` and uses the same editorial intelligence as the automated flow. The difference is the source of the pitch: instead of coming from the News Feed, it comes from an idea, sentence, text or brief pasted by the user.

---

## Editorial configuration

Everything via Notion. R2 reads these pages EVERY time it runs:

- `🏷️ Brand Identity` — brand variables (name, handle, color, niche, audience, voice)
- `📚 Editorial Manual` — 7 parameters, anti-AI-slop, Folha tone
- `🎯 Headline Engine` — hook families, outlier bank, internal verdict
- `🧭 Narrative Architecture` — 18-field / 9-slide structure
- `🎨 Design System` — universal visual principles
- `📐 Quality References` — 2 anchor carousels
- `🖼️ Visual References` — real inspiration images (real local vision)
- `📋 News Sources` — structured table of monitored sources

When the system outputs a mediocre carousel, **edit the page, not the Routine prompt.** Re-run. Iterate.

---

## Prerequisites

- **Claude Code Desktop app** (Mac or Windows) with an active **Pro+** plan
- **Notion** account with Integration Token + dedicated workspace
- **Google Drive** account (connected via MCP/connector in Claude Desktop)
- Higgsfield CLI installed and logged in (`higgsfield account status`)
- **Notion + Google Drive** enabled as connectors in Claude Desktop (tested at setup)

No need for: Homebrew, `jq`, `imagemagick`, `rclone`, local Python, `launchd`, `.plist`, Higgs MCP or external generation key. Everything you need runs via Claude Desktop + Higgsfield CLI.

---

## Reading order

1. `02-Setup-Wizard.md` — first step (brand identity wizard)
2. `03-Notion-template.md` — how the agent creates the structure via API
3. `13-R2-Routine-Local.md` — heart of the system: full prompt of the Local Routine
4. `14-Input-Proprio.md` — on-demand carousel from a simple theme or pasted content
5. `15-Como-usar.md` — day-to-day scenarios
6. `16-Troubleshooting.md` — when something goes wrong

Files 01, 04-11 are Notion instruction pages (you don't read them linearly, you read them when setup references them). File 12 is the Remote Routine (R1).

---

## Expected final structure

```
~/{brand-slug}/
├── docs/                       # these 17 .md files (knowledge)
├── .brand.json                 # brand variables (generated by setup)
├── notion-ids.json             # IDs of pages/databases (generated by setup)
└── state/{YYYY-MM-DD}/         # snapshot of the day
    ├── news.json
    ├── narrativa.json
    ├── visual-plan.json
    ├── visual-brief.txt
    ├── refs/
    ├── logo.png                # logo downloaded from Notion (if brand_has_logo)
    ├── slides/                 # slide-01.png … slide-09.png (source of truth)
    ├── cover-url.txt
    ├── url-2.txt … url-9.txt
    ├── drive-urls.json
    ├── log.txt
    └── .completed

Claude Desktop
├── Routines
│   ├── {brand_name} — News Scout (Remote)
│   └── {brand_name} — Carousel Creator (Local)
└── Connectors
    ├── Notion
    └── Google Drive

Notion workspace
└── 🚀 {brand_name} — News-to-Carrossel/
    ├── 🗞️  News Feed (database)
    ├── 🎨 Carrosséis (database)
    ├── 🏷️  Brand Identity        ← logo PNG attached here
    ├── 🔐 Configuration          ← Higgsfield CLI checklist
    ├── 📋 News Sources
    ├── 📚 Editorial Manual
    ├── 🎯 Headline Engine
    ├── 🧭 Narrative Architecture
    ├── 🎨 Design System
    ├── ⚙️  Render Engine
    ├── 📐 Quality References
    └── 🖼️  Visual References

Google Drive
└── {brand-slug}/
    ├── Noticias/{YYYY-MM-DD}/
    └── Carrosseis/{YYYY-MM-DD}/slide-NN.png
```
