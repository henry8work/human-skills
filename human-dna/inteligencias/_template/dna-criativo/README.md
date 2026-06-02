# 📦 dna-criativo/ — where your deliverable comes out

This folder is the **destination of your Creative DNA**. When the Maestro finishes the briefing, it will create a file here called `DNA.md` — the central deliverable of the process. It also creates a `CLAUDE.md` at the project's root so Claude Code uses this DNA automatically.

---

## What is `DNA.md`

It's **the master file of your brand**. Any AI (Claude, ChatGPT, Gemini, any of them) that will create brand content reads this file FIRST and produces with your identity from the start.

You use it in 3 ways:

### 1. Paste at the start of any AI conversation

Open ChatGPT, Claude, Gemini. Paste the contents of `DNA.md`. Ask for what you want ("write a welcome email", "carousel idea about X"). The AI produces in your voice/visual style.

### 2. Open the project in Claude Code

The project's `CLAUDE.md` tells Claude Code to read this `DNA.md` before creating, auditing or editing any piece of the brand.

### 3. Share with collaborators

Freelance designer, copywriter, agency, new team member — they all read `DNA.md` before touching anything. Single point of truth.

---

## What about Notion?

If you had the Notion connector active in Claude Desktop when you ran the briefing, the Maestro also replicated everything there in an organized structure (main page + sub-pages + databases). It's the same content as `DNA.md`, just navigable and collaboratively editable.

If you didn't have Notion active, no problem — the `DNA.md` here works on its own. You can activate Notion later and ask the Maestro to replicate.

---

## What is the project's `CLAUDE.md`

The `CLAUDE.md` sits one level above this folder, at:

```text
projetos/[your-brand]/CLAUDE.md
```

It tells Claude Code to read `dna-criativo/DNA.md` before creating, auditing or editing any piece of the brand. The `CLAUDE.md` does not replace the DNA; it's the operational layer for Claude Code.

---

## What if I edit the DNA later?

You can edit `DNA.md` directly in this file (any text editor works). When you run the Maestro again, it reads what's here — so your edit will already take effect on the next pieces it generates.

If you also have Notion synced, edit there or here — the Maestro keeps both aligned (with confirmation first).

---

## Other files that may appear here

As you use the system, this folder may gain:

- `DNA.md` — the central deliverable (always)
- `../CLAUDE.md` — Claude Code guidance to use the DNA
- `dna-snapshot-{date}.md` — old versions of the DNA for history (when you evolve the DNA)
- `manifesto.md` — optional, public text that synthesizes purpose + positioning (generated if you ask)
- `sample-pack/` — optional, folder with sample pieces generated with the DNA (caption, email, post, etc.) for your reference

Everything here is yours — you can move, copy, version in Git, send to the team.
