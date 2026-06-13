#!/usr/bin/env bash
# Install Veda skills into your AI tool's skills directory.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
SKILLS_SRC="$ROOT/skills"

DEST="${CURSOR_SKILLS:-$HOME/.cursor/skills}"

if [[ ! -d "$SKILLS_SRC" ]]; then
  echo "Error: skills not found at $SKILLS_SRC" >&2
  exit 1
fi

mkdir -p "$DEST"
count=0
for skill in "$SKILLS_SRC"/*/; do
  name="$(basename "$skill")"
  rm -rf "$DEST/$name"
  cp -R "$skill" "$DEST/$name"
  count=$((count + 1))
done

echo "Installed $count Veda skills to: $DEST"
echo ""
echo "Skills installed:"
ls -1 "$SKILLS_SRC" | sed 's/^/  - /'
echo ""
echo "Next steps:"
echo "  1. Open a project in Cursor (or your Agent Skills-compatible editor)"
echo "  2. Initialize Veda's memory (optional but recommended):"
echo "     python3 \"$ROOT/skills/veda-agent/scripts/init-sanctum.py\" \\"
echo "       --sanctum ./_bmad/sanctum/veda --owner \"Your Name\""
echo "  3. Invoke: veda-agent  (or say \"Hey Veda\")"
echo ""
echo "See README.md for full usage."
