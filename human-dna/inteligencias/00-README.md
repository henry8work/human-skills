# Creative DNA V1.0

Master brand identity system for AI. It's not a config file — it's the **constitution** every other intelligence (Carousel, Video, Deck, Ads, UGC, Email, Landing) reads before producing anything.

The DNA is the brand's `CLAUDE.md`, expanded to the depth of a branding studio manual (Pentagram, Wolff Olins, Collins, Porto Rocha, Manual). It captures purpose, strategy, audience, voice, visuals, behavior and anti-patterns in a format an AI can read and follow.

**White-label.** The base system isn't tied to any brand. Every brand variable lives on the `🧬 DNA Master` page in Notion. Swapping the brand = swapping that page's content + visual references. Nothing in the code changes.

---

## Why it exists

Carousel V2.5 showed the pattern: AI agents produce with quality when they receive **dense, specific editorial context**. The Carousel's `🏷️ Brand Identity` page is good, but it's one page. It's not enough when the agent has to decide between 3 voices for a crisis email, or choose between 2 palettes for a product launch story, or refuse a topic because it doesn't speak to the primary persona.

Branding studios deliver 200+ page manuals because it's what's needed for ANY person (designer, copy, support, founder) to make coherent decisions without going back to the founder every time. **The Creative DNA is that, in a format an AI reads.**

The practical difference:
- **Without Creative DNA:** each agent needs a huge prompt and still produces "ok-but-generic". All tone management is manual. Each new agent must be taught from scratch.
- **With Creative DNA:** every agent reads the DNA first. Output comes with brand voice, correct palette, right persona, anti-patterns respected. **You've plugged in a brand brain that lives outside the prompts.**

---

## Architecture (V1.0 — Claude Desktop Routines)

| Component | Where it runs | Why |
|---|---|---|
| **R1 — Brand Scout** | Routine **Remote** (Anthropic cloud) | Continuous collection of inspirations, mention monitoring, competitor analysis — only talks to Notion + web search, sandbox covers |
| **R2 — DNA Routine** | Routine **Local** (Claude Code Desktop) | Compliant generation (copy, image, deck) + adherence audit (any existing asset vs. DNA) — needs Higgsfield CLI, real vision, render |
| **Initial setup** | Claude Code CLI + Notion Integration Token | Creates 4 databases + 14 sub-pages via REST API in ~60s, populates with discovery |

The architecture mirrors the Carousel's — two routines, local working folder, MCPs, Notion as source of truth — but the DNA is a parent layer. When the Carousel system runs, it reads the DNA from Notion BEFORE reading its own pages. When you create a new system (video, ads), it also reads the DNA.

---

## How the use cycle works

**1. One-time setup (once per brand, ~30-45 min)**
- Deep discovery wizard (52 questions in 7 phases) extracts raw DNA
- Optional audit: the agent analyzes the brand's Instagram/site/decks to extract observed DNA
- Synthesis: agent confronts declared DNA (questions) with observed DNA (audit) and returns a draft for you to refine
- After approval, populates 14 pages in Notion + creates 4 databases + activates 2 routines

**2. Passive use (every other intelligence)**
- Carousel system reads `🧬 DNA Master` before each execution, hydrates variables in the editorial pipeline and in the render prompts
- Video, Ads, Email system — any future agent — reads from the same place
- DNA is the single source of truth. Edit in Notion, the next execution of any agent already reflects it

**3. Active use (R2 DNA Routine)**
- **Generate mode:** "I need a welcome email copy" → R2 reads DNA, writes, returns adherent
- **Audit mode:** paste an existing post → R2 scores adherence (0-10 per dimension: voice, visual, persona, anti-patterns), suggests rewrite
- **Evolve mode:** "we're rethinking positioning" → R2 conducts mini-discovery, proposes diff on the DNA, applies after approval

**4. R1 Brand Scout (cloud, continuous)**
- Collects inspirations relevant to the brand's niche on design sites (Pinterest, Are.na, Behance, Dribbble — via web fetch)
- Monitors brand + competitor mentions (web search) and archives in the database
- Suggests `📚 Reference Library` updates when it finds strong exemplars

---

## DNA configuration

Everything via Notion. R2 and any derived agent reads these pages:

- `🧬 DNA Master` — canonical variables + executive synthesis (1 page, quick read)
- `🎯 Brand Strategy` — purpose, mission, vision, positioning, key insight
- `👥 Audience DNA` — primary + secondary + anti-persona, jobs-to-be-done
- `🗣️ Voice & Tone` — vocabulary, channel registers, constructions, expanded anti-AI-slop
- `🎨 Visual System` — logo, palette, typography, grid, space, motion
- `📸 Photography Direction` — 7 lighting setups, composition, mood, anti-photography
- `🖼️ Image Generation Engine` — Higgsfield CLI prompt templates by type, AI branding
- `🤝 Brand Behavior` — how it acts on each channel, crisis playbook, behavioral calendar
- `🚫 Anti-Patterns` — visual + verbal + behavioral + compared cases
- `📚 Reference Library` — approved canonical examples, inspiration refs, living library
- `🔍 Discovery Protocol` — discovery script for reuse in annual reviews
- `🔐 Configuração` — environment, connectors and Higgsfield CLI checklist

When the output comes without "brand tone", **edit the relevant page, not the prompt.** Re-run. Iterate. Same philosophy as the Carousel.

---

## Prerequisites

- **Claude Code Desktop app** (Mac or Windows) with active **Pro+** plan
- **Notion** account with Integration Token + dedicated workspace for the brand
- **Google Drive** account (connected via MCP/connector in Claude Desktop)
- Higgsfield CLI installed and logged in (`higgsfield account status`)
- **Notion + Google Drive** enabled as connectors in Claude Desktop (tested at setup)

No need for: Homebrew, atomic scripts, local Python, `launchd`. Same stack as Carousel — if you've already run Carousel, the environment is ready.

---

## Reading order

1. `02-Setup-Wizard.md` — first step (discovery wizard)
2. `03-Notion-template.md` — how the agent creates the structure via API
3. `04-Discovery-Protocol.md` — the 52 questions in 7 phases (understand what the wizard asks)
4. `15-R2-DNA-Routine-Local.md` — heart of the system: full prompt of the Local Routine
5. `16-Como-usar.md` — day-to-day scenarios
6. `17-Troubleshooting.md` — when something goes wrong

Files 01, 05-13 are Notion instruction pages (you don't read them linearly, you read them when the setup references them). 14 is the Remote Routine (R1).

---

## Relation with the Carousel system

The Creative DNA **doesn't replace** the Carousel's `🏷️ Brand Identity` — **it feeds it**. The relationship:

| Carousel page (`01. Carrossel`) | Origin in the Creative DNA |
|---|---|
| `🏷️ Brand Identity` (variables: name, handle, color, etc.) | Reads from `🧬 DNA Master` (single source of truth) |
| `📚 Editorial manual` (tone, words, anti-AI-slop) | Reads from `🗣️ Voice & Tone` (expanded version) |
| `🎨 Design system` (universal visual principles) | Reads from `🎨 Visual System` (expanded version) |
| `🖼️ Visual references` (attachments for vision) | Reads from `📚 Reference Library` (living curation) |

When you install the Creative DNA on a brand that already has the Carousel running:
1. Setup creates the DNA structure in a separate workspace (or the same one)
2. The Carousel R2 starts reading from the DNA before reading its own pages
3. Edits in the DNA propagate to the Carousel automatically

When you install the Creative DNA from scratch (no Carousel yet):
1. Setup creates the DNA structure first
2. When you later install the Carousel, it already finds the DNA and uses it
3. Carousel pages become simpler (only the carousel-specific bits — backbone, headlines engine)

---

## Expected final structure

```
~/{brand-slug}/
├── docs/                          # these 18 .md files (knowledge)
├── .claude/settings.json          # permission allowlist (generated by setup)
├── .brand.json                    # brand master variables
├── .dna.json                      # DNA executive synthesis (quick cache)
├── notion-ids.json                # IDs of pages/databases
└── state/{YYYY-MM-DD}/            # snapshot of the day (R2 jobs)
    ├── audits/                    # audits of external assets
    ├── briefs/                    # processed briefs
    ├── outputs/                   # generated outputs (copy, image, deck)
    ├── refs/                      # images downloaded from Refs (vision)
    ├── log.txt
    └── .completed

Claude Desktop
├── Routines
│   ├── {brand_name} — Brand Scout (Remote)
│   └── {brand_name} — DNA Routine (Local)
└── Connectors
    ├── Notion
    └── Google Drive

Notion workspace
└── 🧬 {brand_name} — DNA Criativo/
    ├── 🧬 DNA Master              ← entry point, single source of truth
    ├── 🎯 Brand Strategy
    ├── 👥 Audience DNA
    ├── 🗣️  Voice & Tone
    ├── 🎨 Visual System
    ├── 📸 Photography Direction
    ├── 🖼️  Image Generation Engine
    ├── 🤝 Brand Behavior
    ├── 🚫 Anti-Patterns
    ├── 📚 Reference Library
    ├── 🔍 Discovery Protocol
    ├── 🔐 Configuração            ← Higgsfield CLI, connectors, integrations
    ├── 🗂️  Touchpoints (database) ← each brand channel/application
    ├── 📥 Briefs (database)       ← creative jobs run by R2
    ├── 🎯 Assets (database)       ← canonical library of outputs
    └── ✅ Compliance (database)    ← audit history

Google Drive
└── {brand-slug}/
    ├── DNA-Snapshots/{YYYY-MM-DD}/  ← quarterly snapshot of the entire DNA
    ├── Reference-Library/           ← archived inspiration library
    ├── Outputs/{YYYY-MM-DD}/        ← outputs generated by R2
    └── Audits/{YYYY-MM-DD}/         ← audited assets + reports
```

---

## Philosophy

Three principles that guide the whole system. Worth reading before installing.

**1. Density > brevity.** Brevity is easy for AI (it's already fluent in vague). Density is hard — it requires specificity. Every page of this system prefers one concrete sentence to three vague ones. "The brand is young and modern" is worth nothing. "The brand sounds like a Folha editor who left the newsroom to open an agency" is worth everything.

**2. The negative carries as much as the positive.** What the brand IS NOT (anti-patterns, anti-persona, anti-photography, anti-vocabulary) is what prevents generic output. AI tends to gravitate toward the generic. An explicit anti-pattern is what keeps the output specific.

**3. The DNA is alive.** Brands evolve. The DNA evolves with them. Quarterly, R2 suggests updates based on performance (what content is performing, which editorial decisions resulted in reach). The `🔍 Discovery Protocol` is re-run yearly for a larger refresh. **It's not a frozen 2026 manual — it's a living organism.**
