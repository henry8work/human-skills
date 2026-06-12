# Install — Human Skills

Setup the eight Human skills (`human-image`, `human-cinematic`, `human-dna`, `human-carrossel`, `human-social`, `human-team`, `human-motion`, `human-setup`) on a fresh machine.

> Fastest path: after symlinking the skills, open Claude Code and say "set up the human skills" — the `human-setup` skill checks what's connected and guides Magnific + Higgsfield install for your OS.

## 1. Prerequisites

| Tool | Why | Install |
|---|---|---|
| **Claude Code** | The host that runs skills | https://claude.com/claude-code |
| **Git** | Cloning this repo | `brew install git` (Mac) · `winget install Git.Git` (Windows) |
| **Node.js LTS + npm** | Higgsfield CLI, Remotion (`human-motion`), OpenSquad helpers (`human-team`) | https://nodejs.org (use the LTS installer) |
| **Python 3** | `human-social` and `human-dna` helper scripts | https://www.python.org/downloads/ |
| **Higgsfield CLI** | All image/video generation | `npm install -g @higgsfield/cli` then `higgsfield auth login` |

After installing Higgsfield CLI, verify access to the models the skills depend on:
- `nano_banana_2` — default image model
- `gpt_image_2` — only `human-carrossel`
- `seedance` / `kling` — `human-cinematic` video

You'll need a Higgsfield account with credits for the models above. Each colleague uses their own account.

## 2. Clone the repo

```bash
git clone <REPO_URL> ~/repos/human-skills
```

On Windows (PowerShell):

```powershell
git clone <REPO_URL> $HOME\repos\human-skills
```

> Replace `<REPO_URL>` with the actual URL once the repo is pushed to GitHub.

## 3. Install the skills into Claude Code

Claude Code auto-discovers skills under `~/.claude/skills/`. Symlink each of the seven folders so updates from `git pull` apply instantly.

### macOS / Linux

```bash
mkdir -p ~/.claude/skills
for d in human-image human-cinematic human-dna human-carrossel human-social human-team human-motion human-setup; do
  ln -sf "$HOME/repos/human-skills/$d" ~/.claude/skills/$d
done
```

### Windows (PowerShell, **run as Administrator** to create symlinks)

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.claude\skills" | Out-Null
$skills = @('human-image','human-cinematic','human-dna','human-carrossel','human-social','human-team','human-motion','human-setup')
foreach ($s in $skills) {
  New-Item -ItemType SymbolicLink -Force -Path "$HOME\.claude\skills\$s" -Target "$HOME\repos\human-skills\$s"
}
```

If you can't run as Administrator, replace `SymbolicLink` with `Junction` or copy the folders instead:

```powershell
foreach ($s in $skills) {
  Copy-Item -Recurse -Force "$HOME\repos\human-skills\$s" "$HOME\.claude\skills\$s"
}
```

(With copies you'll need to re-copy after each `git pull`.)

## 4. Verify

Open a new Claude Code session in any folder and type something that should trigger a skill, for example:

```text
I need a key visual for a perfume campaign, editorial mood
```

Claude Code should route to `human-image` and start asking about aspect ratio, references, and output folder.

To list which skills are loaded:

```text
/skills
```

You should see the eight `human-*` names in the output.

## 5. Update later

```bash
cd ~/repos/human-skills
git pull
```

If you symlinked, that's it — Claude Code reads the latest content on each invocation. If you copied, re-run the install loop from step 3.

## Troubleshooting

**Skills don't appear in `/skills`:**
- Check that `~/.claude/skills/human-*/SKILL.md` actually exists.
- On Windows, broken symlinks happen when not running as Admin — switch to `Junction` or `Copy-Item`.

**"Higgsfield CLI not found":**
- Run `which higgsfield` (Mac) / `where higgsfield` (Windows). If empty, `npm install -g @higgsfield/cli` again with `sudo` (Mac) or as Admin (Windows).
- Restart the terminal after install.

**"Model nano_banana_2 unavailable":**
- Check `higgsfield models` to see what's available on your account.
- Confirm credits in your Higgsfield dashboard.

**Python scripts fail with `ModuleNotFoundError`:**
- The DNA/Social scripts may need `pip install pillow requests` (or similar). Check the import block at the top of the failing script.

**Skill conversation comes out in the wrong language:**
- The skills mirror your language. If you wrote the first message in Portuguese, they'll respond in Portuguese. Restart the message in English (or vice versa) and they'll switch.

## Need help?

Ping the Human team channel or open an issue on this repo.
