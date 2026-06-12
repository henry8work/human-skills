# 👋 Start here

A system to build the **Creative DNA** of your brands — visual style, tone of voice, tools — in two deliverables: `DNA.md`, which any AI (Claude, ChatGPT, Gemini) reads to produce content already in the brand's identity, and `DNA.pdf`, an editorial document, laid out to present and share. The project also generates a `CLAUDE.md` so Claude Code uses this DNA automatically.

---

## 3 steps to get started

### 1. Install Claude Code (first time only)

Open the Terminal (**Mac:** `Cmd + Space` → type `Terminal` → enter. **Windows:** Windows key → `PowerShell` → enter) and paste:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Already have Claude Code installed? Skip to step 2.

### 2. Enter this folder via Terminal

In the Terminal:

1. Type `cd ` (with a **trailing space**)
2. **Drag this folder** from Finder/Explorer into the Terminal window (the full path fills in by itself)
3. `Enter`
4. Type `claude` and `Enter`

### 3. Say `hi`

The AI takes over. It will list existing projects (if any) or create a new one with you. A new project is born with `referencias/` and `resultado/`: first you place materials in `referencias/`, then the Maestro reads everything and generates the DNA.

---

## Stuck or lost?

In Claude Code, type `help`. The system will guide you.

---

## What comes out at the end

For each project, three main files come out:

- `projetos/[your-brand]/resultado/DNA.md` — the complete brand manual;
- `projetos/[your-brand]/resultado/DNA.pdf` — the editorial document, laid out with palette, references, images and usage instructions;
- `projetos/[your-brand]/CLAUDE.md` — the file that tells Claude Code to read and follow this DNA.

You use the DNA in 3 ways:

1. **Paste into any AI** at the start of the conversation — it produces in your voice and visual style from the start
2. **Open the project in Claude Code** — the `CLAUDE.md` tells the AI to read the DNA before producing
3. **Share the PDF with collaborators** (designer, copywriter, agency) — everyone works from the same visual and strategic reference

At the end of the block, the Maestro also tests a small piece and uses your feedback to refine the DNA in real time.

Multiple brands? Each becomes a sub-folder inside `projetos/`. No limit.

---

## Structure of this folder

```
02. DNA Criativo/
├── COMECE-AQUI.md         ← this file
├── CLAUDE.md              ← brain of the system (do not touch)
├── inteligencias/         ← kernel (do not touch)
└── projetos/              ← your brands live here
    └── [your-brand]/
        ├── CLAUDE.md      ← Claude Code guidance for this brand
        ├── referencias/   ← you drop raw material here
        └── resultado/     ← DNA.md and DNA.pdf come out here
```

You only touch `projetos/`. The rest is technical — the Maestro handles it.

---

## Costs

- **Claude Code** — Anthropic's Pro+ plan (required)
- **Notion** — optional, connector enabled in Claude Desktop
- **Higgsfield CLI** — optional, only if generating image/video
