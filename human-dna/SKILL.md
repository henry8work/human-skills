---
name: human-dna
description: Creates, edits, audits, and operationalizes the Creative DNA of a brand — visual identity, tone of voice, strategy, behavior, audience, anti-patterns, photography, tools, and applications. Generates a canonical `DNA.md` + a per-project `CLAUDE.md` so Claude Code follows the brand style. Use whenever the user asks for "create brand", "creative DNA", "branding", "visual identity", "tone of voice", "brand audit", "manifesto", "positioning", "voice and tone", "brand book", "rebrand", or wants to generate/refine materials respecting a specific brand. Triggers (EN/PT) — brand, branding, creative DNA, DNA criativo, identidade visual, tom de voz, auditoria de marca, manifesto, posicionamento, voice and tone, manual da marca, rebrand, brand book. Brand image generation asks the user to choose Magnific (free default) or Higgsfield (paid). Multi-project: each brand lives in `projetos/{slug}/`.
---

# Human DNA

System for creating and operating a brand's Creative DNA. Each brand becomes a canonical `DNA.md` + a per-project `CLAUDE.md` + state.

## Visual generation routing

<!-- IMAGE_GENERATION_ROUTE_RULE -->
> Image generation rule: always use `imageprompts.md` as the creative/prompt guide when present. Before rendering any image, ask the user to choose: **Magnific** via direct MCP/API (`nano-banana-pro-flash`, `resolution: "1K"`, intended free/default) or **Higgsfield** via MCP/CLI (paid). Do not use `mcp__magnific_oauth.images_generate` for routine Magnific image generation unless explicitly requested; use `magnific-oauth.account_balance` only to check/measure credits.
<!-- /IMAGE_GENERATION_ROUTE_RULE -->

**Default: Magnific (free).** Before each brand-image render, briefly tell the user *"Going with Magnific (free) — switch to Higgsfield (paid)?"* If they don't push back, proceed with Magnific. If they ask for Higgsfield, switch. **Never silently render on Higgsfield.**

Applies to every brand-image render in this skill (test pieces, audit material, photo direction examples, etc.). The brand's `DNA.md` may also pin a preferred provider — when it does, still confirm with the user before paying.

## Language

Mirror the user's language. Conversation can be EN or PT. The `DNA.md` and `CLAUDE.md` generated for each brand are produced in the brand's working language (ask if unclear).

## Complete intelligence

- [CLAUDE.md](CLAUDE.md) — DNA maestro: tone, flow, delivery rules (63K — read in full before operating)
- [👋 COMECE-AQUI.md](👋%20COMECE-AQUI.md) — human getting-started guide (PT)
- [imageprompts.md](imageprompts.md) — brand image engine
- [inteligencias/](./inteligencias) — specialist "doctors" by discipline:
  - `01-DNA-Master.md` — canonical `DNA.md` template
  - `02-Setup-Wizard.md`, `03-Notion-template.md`, `04-Discovery-Protocol.md`
  - `05-Brand-Strategy.md`, `06-Audience-DNA.md`, `07-Voice-and-Tone.md`
  - `08-Visual-System.md`, `09-Photography-Direction.md`, `10-Image-Generation-Engine.md`
  - `11-Brand-Behavior.md`, `12-Anti-Patterns.md`, `13-Reference-Library.md`
  - `14-R1-Brand-Scout.md`, `15-R2-DNA-Routine-Local.md`
  - `16-Como-usar.md`, `17-Troubleshooting.md`, `18-Design-Director.md`
  - `_template/CLAUDE.md` — per-project customized template
- [projetos/](./projetos) — brand container
- [scripts/](./scripts) — utilities (`render-dna-pdf.py`, `collect-instagram.py`)

## Mandatory flow

1. **List** existing projects in `<cwd>/human-output/dna/projetos/`.
2. **Ask** which one to open or to create a new brand.
3. **New structure:** create from `_template/` into `<cwd>/human-output/dna/{slug}/`.
4. **Conversational briefing:** **one question per message**, save progress.
5. **Generate** `dna-criativo/DNA.md` following `01-DNA-Master.md`.
6. **Generate** `CLAUDE.md` at the project root from `_template/CLAUDE.md`.
7. **Test** a small piece following the DNA → ask provider per the routing rule.
8. **Refine** with feedback or record adherence approval.
9. **Review** consistency DNA ↔ test ↔ refinement.
10. **Use** the finished DNA to generate, audit, or edit materials.

## Default output

```
<cwd>/human-output/dna/{slug}/
├── CLAUDE.md
├── materiais/
├── dna-criativo/
│   └── DNA.md
├── .brand.json
└── other state files
```

## Non-negotiable rules

- **One question per message** in the briefing — never stack.
- Read `CLAUDE.md` in full before operating.
- Brand image generation always asks the routing question (Magnific or Higgsfield).
- Notion/Drive/Routines are optional.
- Before generating any visual: confirm project, quantity, aspect ratio, resolution, references, purpose, folder.

## Final delivery

Final project folder as a clickable link + non-`.md` files generated as clickable links.
