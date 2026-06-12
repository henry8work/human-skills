# 📁 projetos/ — one folder per brand

This folder is the **container for all the projects/brands** you build using the system. Each project lives in its own sub-folder, isolated from the others.

---

## Structure

```
projetos/
├── README.md          ← this file
├── marca-x/           ← real project
├── marca-y/           ← real project
└── marca-z/           ← real project
```

> The **base template** of projects does not live here — it lives in `../inteligencias/_template/`. It's part of the system kernel, not the workspace. The Maestro copies from it when you create a new project.

---

## How it works

When you run `claude` in the root folder `02. DNA Criativo/` and say "hi", the Maestro:

1. **Lists existing projects** (subfolders inside `projetos/`)
2. **Asks:** "Do you want to work on a new project or an existing one?"
3. **Routes accordingly:**
   - **New** → creates `projetos/[new-name]/` copying the structure from `inteligencias/_template/`, sets it as the working folder, goes to Path A (initial briefing)
   - **Existing** → loads that project's DNA, shows a short summary that proves it understood the brand, offers next steps (generate piece, audit, edit DNA, consult)

---

## Each project has

- **`materiais/`** — raw-material entry (logos, fonts, visual refs, tone examples, competitors, anti-refs, other)
- **`dna-criativo/`** — deliverable output (`DNA.md` + snapshots + optional manifesto)
- **`.brand.json`** — canonical brand variables (created during setup)
- Other invisible technical files (`.discovery-progress.json`, `notion-ids.json` if Notion was synced, etc.)

---

## How to create a new project manually (rare)

The Maestro usually creates them automatically. But if you want to do it manually:

1. Copy the kernel's template to a new name:
   ```bash
   cp -r ../inteligencias/_template marca-nova
   ```
2. Run `claude` in the root folder and say "work on the project marca-nova"

---

## Don't touch `inteligencias/_template/`

This template is the model structure used to create new projects. Touching it affects future creation. If you want to customize the template, edit carefully — but the default template usually serves all projects.
