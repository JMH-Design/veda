#!/usr/bin/env bash
# Update Veda skills for Claude Code from GitHub.
# Safe: replaces skills + CLAUDE.md hook only — never touches sanctum or artifacts.
set -euo pipefail

REPO_URL="${VEDA_REPO_URL:-https://github.com/JMH-Design/veda.git}"
INSTALL_ROOT="${VEDA_INSTALL_DIR:-$HOME/.claude/skills}"
CACHE_DIR="${VEDA_CACHE_DIR:-$HOME/.cache/veda-repo}"
PROJECT_ROOT="${VEDA_PROJECT_ROOT:-$(pwd)}"
BRANCH="${VEDA_BRANCH:-main}"

echo "==> Veda update for Claude Code"
echo "    Skills dest:  $INSTALL_ROOT"
echo "    Project root: $PROJECT_ROOT"
echo "    Cache:        $CACHE_DIR"

if [[ -d "$CACHE_DIR/.git" ]]; then
  echo "==> Pulling latest from $REPO_URL ($BRANCH)"
  git -C "$CACHE_DIR" fetch origin "$BRANCH"
  git -C "$CACHE_DIR" checkout "$BRANCH"
  git -C "$CACHE_DIR" pull --ff-only origin "$BRANCH"
else
  echo "==> Cloning $REPO_URL ($BRANCH)"
  mkdir -p "$(dirname "$CACHE_DIR")"
  rm -rf "$CACHE_DIR"
  git clone --branch "$BRANCH" --depth 1 "$REPO_URL" "$CACHE_DIR"
fi

COMMIT="$(git -C "$CACHE_DIR" rev-parse --short HEAD)"
echo "==> Source commit: $COMMIT"

SKILLS_SRC="$CACHE_DIR/skills"
if [[ ! -d "$SKILLS_SRC" ]]; then
  echo "Error: skills/ not found in repo at $SKILLS_SRC" >&2
  exit 1
fi

mkdir -p "$INSTALL_ROOT"
count=0
for skill in "$SKILLS_SRC"/*/; do
  name="$(basename "$skill")"
  rm -rf "$INSTALL_ROOT/$name"
  cp -R "$skill" "$INSTALL_ROOT/$name"
  count=$((count + 1))
done
echo "==> Installed $count skills to $INSTALL_ROOT"

if [[ -f "$CACHE_DIR/CLAUDE.md" ]]; then
  cp "$CACHE_DIR/CLAUDE.md" "$PROJECT_ROOT/CLAUDE.md"
  echo "==> Updated $PROJECT_ROOT/CLAUDE.md"
fi

# Optional: project-local skills mirror
LOCAL_SKILLS="$PROJECT_ROOT/.claude/skills"
if [[ -d "$PROJECT_ROOT/.claude" ]] || [[ "${VEDA_MIRROR_PROJECT_SKILLS:-}" == "1" ]]; then
  mkdir -p "$LOCAL_SKILLS"
  for skill in "$SKILLS_SRC"/*/; do
    name="$(basename "$skill")"
    rm -rf "$LOCAL_SKILLS/$name"
    cp -R "$skill" "$LOCAL_SKILLS/$name"
  done
  echo "==> Mirrored skills to $LOCAL_SKILLS"
fi

echo ""
echo "Done. Veda $COMMIT is ready in Claude Code."
echo ""
echo "Preserved (not modified):"
echo "  - _bmad/sanctum/veda/     (your memory)"
echo "  - docs/understanding/     (your artifacts)"
echo ""
echo "Verify:"
echo "  ls $INSTALL_ROOT/veda-agent/references/calibration-hosts.md"
echo ""
echo "Start a new Claude Code session and invoke veda-agent."
