#!/usr/bin/env bash
# Builds dist/human-skills-v{VERSION}.plugin from raw-files-md/.
# Allowlist-based: only what's listed here ships. Client data, run outputs,
# build artifacts and lockfiles never enter the package.
set -euo pipefail

REPO="$(cd "$(dirname "$0")" && pwd)"
SRC="$REPO/raw-files-md"
VERSION="$(python3 -c "import json;print(json.load(open('$SRC/.claude-plugin/plugin.json'))['version'])")"
OUT="$REPO/dist/human-skills-v$VERSION.plugin"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

mkdir -p "$STAGE/skills" "$REPO/dist"

# Plugin root files
cp -R "$SRC/.claude-plugin" "$STAGE/.claude-plugin"
cp "$SRC/README.md" "$STAGE/README.md"
cp "$SRC/.mcp.json" "$STAGE/.mcp.json"
cp -R "$SRC/commands" "$STAGE/commands"

# Skills
for skill in human-carrossel human-cinematic human-dna human-image human-motion human-product-ad human-setup human-social human-team; do
  rsync -a "$SRC/$skill/" "$STAGE/skills/$skill/" \
    --exclude '.DS_Store' \
    --exclude '.claude/' \
    --exclude '.Codex/' \
    --exclude 'node_modules/' \
    --exclude 'dist/' \
    --exclude 'package-lock.json' \
    --exclude '*.tsbuildinfo' \
    --exclude 'SKILL.v1.md' \
    --exclude 'BUD/' \
    --exclude 'human-output/' \
    --exclude 'desdobramento/' \
    --exclude '__pycache__/' \
    --exclude '.env*' \
    --exclude 'projetos/[!_R]*/'
done

# Sanity checks — fail the build instead of shipping a broken package
test -f "$STAGE/skills/human-team/squads/team/pipeline/pipeline.yaml" || { echo "FATAL: human-team pipeline missing"; exit 1; }
test -f "$STAGE/commands/team.md" || { echo "FATAL: /team command missing"; exit 1; }
for s in "$STAGE"/skills/*/; do
  test -f "$s/SKILL.md" || { echo "FATAL: SKILL.md missing in $s"; exit 1; }
done
# description length limit (1024 chars)
python3 - "$STAGE" <<'PY'
import sys, re, json, pathlib
stage = pathlib.Path(sys.argv[1])
bad = False

# Plugin description: hard cap 500 chars (Claude desktop validator)
pj = json.loads((stage / ".claude-plugin" / "plugin.json").read_text())
pd = pj.get("description", "")
if len(pd) > 500:
    print(f"FATAL: plugin.json description {len(pd)}>500 chars"); bad = True

# Skill descriptions: <=1024 chars AND no XML-like tags (<...>)
for f in stage.glob("skills/*/SKILL.md"):
    m = re.search(r"^description: (.*?)$", f.read_text(), re.M | re.S)
    desc = re.split(r"\n(?=\w+:|---)", m.group(1))[0] if m else ""
    if len(desc) > 1024:
        print(f"FATAL: description >1024 chars ({len(desc)}) in {f}"); bad = True
    tags = re.findall(r"<[a-zA-Z/][^>]*>", desc)
    if tags:
        print(f"FATAL: XML-like tag(s) {set(tags)} in description of {f}"); bad = True
sys.exit(1 if bad else 0)
PY
# no client/run leftovers
if grep -rl "FT studio\|Budweiser\|petlove\|Petti" "$STAGE" >/dev/null 2>&1; then
  echo "FATAL: client data leaked into package:"; grep -rl "FT studio\|Budweiser\|petlove\|Petti" "$STAGE"; exit 1
fi

rm -f "$OUT"
(cd "$STAGE" && zip -qr "$OUT" . -x '.*.swp')
echo "Built: $OUT"
unzip -l "$OUT" | tail -1
