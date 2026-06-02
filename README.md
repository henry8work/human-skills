# Human Skills

Seven self-contained Claude Code skills for creative production at Human. Each skill bundles all of its own intelligence — once installed, it works in any folder without depending on a parent repo or environment variables.

## The seven skills

| Skill | What it does |
|---|---|
| **human-image** | Cinematic photo direction — turns a brief into a high-level prompt and renders via Higgsfield CLI + Nano Banana 2. |
| **human-cinematic** | Full cinematic production — impossible product shots, video campaigns, scripts, character sheets, approved frames, videos via Higgsfield (Seedance / Kling / Nano Banana 2). |
| **human-dna** | Creates, edits, audits, and operationalizes a brand's Creative DNA. Generates a canonical `DNA.md` + a per-project `CLAUDE.md` so Claude Code follows the brand style across all materials. Multi-project. |
| **human-carrossel** | Editorial Instagram carousels at scale. On-demand (theme/text) or automated (R1 News Scout + R2 Creator). Renders slides via Higgsfield CLI + GPT Image 2. |
| **human-social** | Unfolds a folder of text + images into native pieces for Instagram Feed, Stories, and LinkedIn — not a resize, fresh images per platform with platform-specific captions. |
| **human-team** | Multi-agent creative team (OpenSquad) that produces a full campaign — brief, script, art direction, storyboard, ads in 9:16/4:5/16:9, copy-pack, Notion calendar, handoff. |
| **human-motion** | Video and motion graphics from the terminal via Remotion — Reels, captions, beat-matching, MP4 render. AI assets via Higgsfield CLI + Nano Banana 2. |

## How it works

Each skill is a self-contained folder under `~/.claude/skills/{skill-name}/` with a `SKILL.md` that Claude Code auto-discovers. When you describe your intent ("I need a key visual for…", "make me a Reel about…", "build a brand DNA for…"), Claude Code routes to the right skill automatically based on the skill's `description` triggers.

Skills speak **the user's language** — write to them in English or Portuguese and they respond in kind. Image prompts for Nano Banana 2 are always in English regardless (model constraint). Video prompts for Seedance follow the framework (Chinese when required).

## What you need

To actually run the skills you'll need:
- **Claude Code** (CLI, desktop, or web)
- **[Higgsfield CLI](https://higgsfield.ai)** logged in with your account (paid credits for image/video rendering)
- **Node.js LTS + npm** (for `human-motion` Remotion and `human-team` OpenSquad helpers)
- **Python 3** (for `human-social` and `human-dna` helper scripts)

Models used (provisioned through your Higgsfield account):
- `nano_banana_2` — default image model
- `gpt_image_2` — used only by `human-carrossel`
- `seedance` / `kling` — used by `human-cinematic` for video

See [INSTALL.md](INSTALL.md) for setup steps on Mac and Windows.

## Output conventions

Every skill writes its results into the **current working directory** (where you opened Claude Code), under:

```
human-output/{skill}/{run_slug}/
```

Exception: `human-social` writes into `{input-folder}/desdobramento/` because it operates on a user-provided folder.

After each run, the skill reports the final folder as a clickable link plus all non-`.md` deliverables (images, videos, JSONs, CSVs) as clickable links.

## Visual generation routing

Before rendering **any image**, the skill asks the user to choose between two providers:

- **Magnific** via direct MCP/API — model `nano-banana-pro-flash`, `resolution: "1K"`, the intended free/default path.
- **Higgsfield** via MCP/CLI — paid, higher-resolution alternative (`nano_banana_2` at 2k by default).

The full canonical rule lives in each skill's `SKILL.md` under the `IMAGE_GENERATION_ROUTE_RULE` block. Skills should not call `mcp__magnific_oauth.images_generate` for routine generation; `magnific-oauth.account_balance` is used only to check credits.

**Exceptions:**
- `human-carrossel` does **not** ask — its slide pipeline is pinned to `gpt_image_2` via Higgsfield CLI.
- `human-cinematic` / `human-team` / `human-motion` video rendering is always Higgsfield (Seedance or Kling). The routing question applies only to stills.

Before generating any asset, the skill also confirms: project name, quantity, aspect ratio, resolution, references, purpose, output folder.

## Authoring credits

Built and maintained by the Human team. These skills are the Claude Code expression of internal creative systems used in production.

## License

Internal — distribute within Human and partner teams only. Do not redistribute publicly without authorization.
