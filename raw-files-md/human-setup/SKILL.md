---
name: human-setup
description: First-run setup and dependency check for the Human Skills plugin. Connects the official Magnific MCP and installs/logs in the Higgsfield CLI, with OS-specific steps for Mac and Windows. Defines the three render paths every Human skill must offer before rendering — 1) Magnific MCP direct (plan credits), 2) Magnific Hybrid Run Unlimited (zero credits, user clicks in browser), 3) Higgsfield (paid) — and the rule to always ask the user which one to use. Use whenever a render provider is missing or not authenticated, when a user installs the plugin for the first time, or when the user asks to "set up", "install dependencies", "connect Magnific", "log in to Higgsfield", "configurar", "instalar dependencias", "conectar Magnific", "logar no Higgsfield", or when any Human skill preflight check reports a provider is not ready.
---

# Human Setup

> Render economics, validated 2026-06-10: via MCP every generation debits **plan credits** (e.g. Nano Banana 2 at 1K = 75 credits) — never pay-per-use API money. The web app's "Run Unlimited" mode (0 credits) is NOT exposed through MCP; for zero-credit batches use the Hybrid Unlimited workflow below.

Onboarding and dependency setup for the Human Skills plugin. Run this the first time a user installs the plugin, or any time a render provider is missing. Mirror the user language; keep steps copy-pasteable.

## What this plugin needs

Two render providers power the Human skills — Magnific (official MCP) and Higgsfield — and together they offer **three render paths**. A user needs at least one provider.

- Magnific — connected via the **official Magnific MCP server** (`https://mcp.magnific.com`), authenticated with OAuth on the user's own Magnific account. Generations debit the user's Magnific **plan credits** (included in their subscription), never pay-per-use API credits.
- Higgsfield — a CLI/MCP tool authenticated per machine, with the user's own account and credits.

A user only needs Higgsfield for the Higgsfield render path and for video models exclusive to it. Every skill (including human-carrossel, which is pinned to the GPT Image 2 model family) has at least one Magnific path — Magnific alone is enough to start.

## The three render paths — always ask which one

Whenever a Human skill is about to render images or video, present these three options and let the user pick. Never assume — ask every time, since the user may choose differently per job.

1. **Magnific MCP direto** — Claude generates immediately via `images_generate` / `video_generate`. Costs **plan credits** (e.g. Nano Banana 2 at 1K = 75 credits/image), no extra money. Best for one-offs, quick iterations, and anything urgent.
2. **Magnific Híbrido (Run Unlimited)** — **zero credits**. Claude builds a Space with pre-filled generator nodes (`spaces_create` + `spaces_edit`), shares the `webUrl`, the user clicks **Run Unlimited** in the browser, then Claude collects the results (`creations_search` / `spaces_state`) and continues the pipeline. Best for big batches or zero credit spend; requires one manual click from the user.
3. **Higgsfield** — the paid path with the user's Higgsfield account and credits (CLI/MCP), as before. The route for Higgsfield-exclusive models; install: `npm install -g @higgsfield/cli`, login: `higgsfield auth login`, probe: `higgsfield account status` (there is no `whoami` command).

Phrase the question simply, e.g.: "Como você quer renderizar? 1) Magnific direto (créditos do plano), 2) Híbrido Run Unlimited (zero créditos, você clica no navegador), 3) Higgsfield (pago)."

## Detect what is already set up

Before guiding any install, check current state. Do not make the user redo steps they already did.

- Magnific: check whether the `magnific-mcp` tools are available (call `account_balance` — the cheapest probe; it also shows the plan tier and remaining plan credits). If the tools respond, Magnific is connected, skip its setup.
- Higgsfield: run a non-destructive identity check (MCP `balance` tool, or `higgsfield account status` in the shell). If it responds, Higgsfield is ready, skip its setup.

Report what is already working and only walk through what is missing.

## Connect Magnific (free default — official MCP)

The official Magnific MCP lives at `https://mcp.magnific.com` and uses OAuth. On enterprise Claude plans the connector directory may be locked, so the reliable path is `mcp-remote` (public npm package that handles the OAuth handshake and stores the token locally in `~/.mcp-auth`).

1. Ensure Node.js LTS is installed (`node --version`; on Mac: `brew install node`, on Windows: nodejs.org installer).
2. Install the bridge: `npm install -g mcp-remote`.
3. Register the server at user scope (works in every project):
   `claude mcp add --scope user magnific-mcp -- mcp-remote https://mcp.magnific.com`
   (on Mac with Homebrew, the binary is at `/opt/homebrew/bin/mcp-remote` — use the full path if `mcp-remote` is not on PATH for GUI sessions).
4. Trigger the OAuth login once by running the bridge directly: `mcp-remote https://mcp.magnific.com`. A browser window opens — the user signs in to their Magnific account and approves. After "Proxy established successfully" appears, the process can be killed (Ctrl+C); the token is saved.
5. Verify: `claude mcp list` must show `magnific-mcp … ✓ Connected`. In a new session, call `account_balance` to confirm plan and credits.

Notes:
- Authentication is per user — each teammate connects their own Magnific account and uses their own plan credits.
- If the simple `/mcp` → Authenticate flow works in the user's Claude Code, that is also fine; `mcp-remote` is the fallback that always works (including enterprise plans where app connectors are restricted).

### Key Magnific MCP tools and models

- Image: `images_generate`. **The model is selected with the `mode` parameter** (NOT `model` — a wrong param name silently falls back to `mode: "auto"`, which may route to a pricier model). Slugs: `imagen-nano-banana-2-flash` = Nano Banana 2, `imagen-nano-banana-2` = Nano Banana Pro, `mystic-2-5`, `seedream-4-5`, `flux-2`, …. Default: `mode: "imagen-nano-banana-2-flash"`, `resolution: "1k"` (75 plan credits per image).
- Video: `video_generate` (slugs: `kling-25` = Kling 2.5, `kling-30`, `bytedance-seedance-pro-2.0`, `google-veo3_1`, …). Prefer `kling-25` as the default.
- Catalog: `images_models_list` / `video_models_list` for the current model roster.
- Results: generation returns a creation identifier; use `creations_wait` to block until the asset URL is ready, and share the `webUrl` with the user. `creations_get` shows the actual model and `credits` charged — use it to verify cost when in doubt.
- Account: `account_balance` for plan tier and remaining plan credits.

### Canonical model slugs (verified 2026-06-12 against both catalogs)

This is the single source of truth for model names across all Human skills. **Watch the naming trap**: on Higgsfield, the slug `nano_banana_2` is the model marketed as "Nano Banana **Pro**", while the slug `nano_banana_flash` is "Nano Banana 2".

| Model (marketing name) | Magnific `mode` | Higgsfield CLI slug | Use for |
|---|---|---|---|
| Nano Banana 2 (fast) | `imagen-nano-banana-2-flash` | `nano_banana_flash` | default photo/cinematic images |
| Nano Banana Pro (max fidelity) | `imagen-nano-banana-2` | `nano_banana_2` | finals, brand/product fidelity |
| GPT Image 2 (text/layout) | `gpt-2` | `gpt_image_2` | lettering, carousels, design pieces |
| Kling 2.5 (video, value) | `kling-25` | — | default silent 5-10s video |
| Kling 3.0 (video) | `kling-30` | `kling3_0` | hero video, multishot, up to 15s |
| Seedance 2.0 (video) | — | `seedance_2_0` | Seedance path (prompt in Chinese) |

When in doubt, re-check with `images_models_list`/`video_models_list` (Magnific) or `higgsfield model list` (CLI) — catalogs move.

### Hybrid Unlimited workflow (zero credits, for big batches)

The Magnific web app offers "Run Unlimited" (0 credits) on eligible models — e.g. Nano Banana 2 at 1K — but only when the run is triggered from the browser canvas (Spaces). The hybrid flow keeps the heavy lifting automated and the free click manual:

1. Claude creates a Space: `spaces_create {name}`.
2. Claude populates it headlessly with `spaces_edit` — one image-generator node per desired output, each pre-filled with prompt, `mode` (e.g. `imagen-nano-banana-2-flash`), `resolution` (`1k`) and aspect ratio. Poll `spaces_edit_status` until `allTerminal`, then verify with `spaces_state`.
3. Claude shares the Space `webUrl` with the user.
4. The user opens it in the browser and clicks **Run Unlimited** on the nodes (or selects all and runs) — this consumes **zero credits**.
5. Back in the session, Claude collects the finished assets with `creations_search` / `creations_get` (or reads node outputs via `spaces_state`) and downloads/uses them in the pipeline.

Use the direct MCP call for one-offs and iterations (75 credits is negligible); switch to the hybrid flow for large batches or when the user explicitly wants zero credit spend.

## Install and log in to Higgsfield (paid)

Higgsfield is a CLI/MCP installed on each machine. Steps differ by OS.

### Mac

1. Ensure Node.js LTS is installed: `node --version`. If missing, install via Homebrew: `brew install node`.
2. Install the Higgsfield CLI globally: `npm install -g @higgsfield/cli` (use the package name from the Higgsfield docs if it differs).
3. Log in: `higgsfield auth login` and follow the browser/device prompt.
4. Verify: `higgsfield account status`.

### Windows

1. Ensure Node.js LTS is installed from nodejs.org, then check `node --version` in PowerShell.
2. Install the CLI: `npm install -g @higgsfield/cli`.
3. Log in: `higgsfield auth login`.
4. Verify: `higgsfield account status`.

Each teammate logs in with their own Higgsfield account and credits, logins are not shared.

## Other dependencies

- Node.js LTS + npm — required for the Magnific bridge (`mcp-remote`), human-motion (Remotion) and human-team (OpenSquad helpers).
- Python 3 — required for helper scripts in human-social and human-dna.

Check `node --version` and `python3 --version`; guide installation only if a skill that needs them is about to run.

## Done

Once at least one render provider is confirmed, tell the user they are ready and which skill to try first (for example, ask for an image to trigger human-image). If only the free path is set up, note that the paid Higgsfield path and human-carrossel will need the CLI later.
