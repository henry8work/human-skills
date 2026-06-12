---
name: human-setup
description: First-run setup and dependency check for the Human Skills plugin. Connects the Magnific MCP (free default render path) and installs/logs in the Higgsfield CLI (paid path), with OS-specific steps for Mac and Windows. Use whenever a render provider is missing or not authenticated, when a user installs the plugin for the first time, or when the user asks to "set up", "install dependencies", "connect Magnific", "log in to Higgsfield", "configurar", "instalar dependencias", "conectar Magnific", "logar no Higgsfield", or when any Human skill preflight check reports a provider is not ready.
---

# Human Setup

Onboarding and dependency setup for the Human Skills plugin. Run this the first time a user installs the plugin, or any time a render provider is missing. Mirror the user language; keep steps copy-pasteable.

## What this plugin needs

Two render providers power the Human skills. A user needs at least one.

- Magnific — the free default path. It is a Cowork connector (MCP), connected inside the app, not installed in a terminal.
- Higgsfield — the paid path. It is a CLI tool installed and authenticated per machine, with the user own account and credits.

A user only needs Higgsfield for the paid path or the carousel pipeline (human-carrossel is pinned to Higgsfield + GPT Image 2). For everything else, Magnific alone is enough.

## Detect what is already set up

Before guiding any install, check current state. Do not make the user redo steps they already did.

- Magnific: check whether the Magnific MCP tools are available (a quick account/credit balance call is the cheapest probe). If the tools respond, Magnific is connected, skip its setup.
- Higgsfield: run a non-destructive identity check in the shell, e.g. higgsfield account status (or higgsfield --version to test install, then whoami to test login). If it prints a user, Higgsfield is ready, skip its setup.

Report what is already working and only walk through what is missing.

## Connect Magnific (free default)

Magnific is connected as a Cowork connector, not via terminal.

1. Open the Cowork connectors / integrations panel.
2. Find Magnific in the connector list and authenticate with the user Magnific (Freepik) account.
3. Confirm with a balance/credit check once connected.

If Magnific does not appear in the connector list, search the connector registry for it and suggest it to the user. Magnific authentication is per user, each teammate connects their own account and uses their own credits.

## Install and log in to Higgsfield (paid)

Higgsfield is a CLI installed on each machine. Steps differ by OS.

### Mac

1. Ensure Node.js LTS is installed: node --version. If missing, install via Homebrew: brew install node.
2. Install the Higgsfield CLI globally: npm install -g @higgsfield/cli (use the package name from the Higgsfield docs if it differs).
3. Log in: higgsfield auth login and follow the browser/device prompt.
4. Verify: higgsfield account status.

### Windows

1. Ensure Node.js LTS is installed from nodejs.org, then check node --version in PowerShell.
2. Install the CLI: npm install -g @higgsfield/cli.
3. Log in: higgsfield auth login.
4. Verify: higgsfield account status.

Each teammate logs in with their own Higgsfield account and credits, logins are not shared.

## Other dependencies

- Node.js LTS + npm — required for human-motion (Remotion) and human-team (OpenSquad helpers).
- Python 3 — required for helper scripts in human-social and human-dna.

Check node --version and python3 --version; guide installation only if a skill that needs them is about to run.

## Done

Once at least one render provider is confirmed, tell the user they are ready and which skill to try first (for example, ask for an image to trigger human-image). If only the free path is set up, note that the paid Higgsfield path and human-carrossel will need the CLI later.
