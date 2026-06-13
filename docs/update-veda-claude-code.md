# Update Veda — Claude Code agent instructions

**Audience:** Claude Code agent (VS Code extension or CLI).  
**Goal:** Install or refresh Veda to the latest release from GitHub without losing user memory.

**Repository:** https://github.com/JMH-Design/veda  
**Default branch:** `main`

---

## When to run this procedure

Run when the user says any of:

- "Update Veda"
- "Get the latest Veda"
- "Refresh Veda skills"
- "Upgrade Veda"
- "Sync Veda from GitHub"

Also run **once** at the start of a session if the user reports missing calibration UI, old `pu-*` skill names, or behavior that doesn't match the GitHub README.

---

## What this updates vs preserves

| Updates (safe to overwrite) | Preserves (never delete) |
| --- | --- |
| `~/.claude/skills/veda-*` (all 29 skills) | `_bmad/sanctum/veda/` — memory, BOND, sessions |
| `~/.claude/skills/veda-agent`, workflows | `docs/understanding/*.md` — learning notes |
| Project `CLAUDE.md` (from repo) | `config.user.toml` — local overrides |
| Optional: `.claude/skills/` in project | User's calibration in `BOND.md` |

**Never** run `git clean`, `rm -rf _bmad`, or delete sanctum files during an update.

---

## Preferred method — run the update script

From the **user's project root**:

```bash
# First time or no cache — clone then run
git clone --depth 1 https://github.com/JMH-Design/veda.git ~/.cache/veda-repo
bash ~/.cache/veda-repo/scripts/update-veda-claude-code.sh
```

```bash
# Already have cache — pull then run
git -C ~/.cache/veda-repo pull --ff-only origin main
bash ~/.cache/veda-repo/scripts/update-veda-claude-code.sh
```

**Environment overrides** (only if user specifies):

| Variable | Default | Purpose |
| --- | --- | --- |
| `VEDA_INSTALL_DIR` | `~/.claude/skills` | Global Claude Code skills path |
| `VEDA_PROJECT_ROOT` | current directory | Where to write `CLAUDE.md` |
| `VEDA_CACHE_DIR` | `~/.cache/veda-repo` | Git clone cache |
| `VEDA_MIRROR_PROJECT_SKILLS` | unset | Set to `1` to also copy to `.claude/skills/` |

---

## Manual method — if the script fails

Execute these steps in order. Confirm each step before continuing.

### Step 1 — Fetch latest source

```bash
CACHE="$HOME/.cache/veda-repo"
if [ -d "$CACHE/.git" ]; then
  git -C "$CACHE" pull --ff-only origin main
else
  git clone --depth 1 https://github.com/JMH-Design/veda.git "$CACHE"
fi
git -C "$CACHE" log -1 --oneline
```

Record the commit hash and report it to the user.

### Step 2 — Install all skills globally

```bash
DEST="$HOME/.claude/skills"
mkdir -p "$DEST"
for skill in "$CACHE/skills"/*/; do
  name=$(basename "$skill")
  rm -rf "$DEST/$name"
  cp -R "$skill" "$DEST/$name"
done
ls "$DEST" | grep -c '^veda'   # expect 29
```

Expected skill folders:

- `veda-agent`
- `veda-learn`, `veda-analyze`, `veda-heuristic`, `veda-help`
- `veda-agent-*` (24 specialists)

### Step 3 — Update project CLAUDE.md

```bash
cp "$CACHE/CLAUDE.md" ./CLAUDE.md
```

If the project already has a custom `CLAUDE.md`, **merge** rather than blind overwrite:

1. Read existing `CLAUDE.md`.
2. Ensure the **Veda — Claude Code** block from the repo is present (Veda invocation + `AskUserQuestion` calibration rules).
3. Do not remove unrelated project instructions.

### Step 4 — Verify installation

```bash
test -f "$HOME/.claude/skills/veda-agent/references/calibration-hosts.md" && echo "OK: calibration-hosts"
test -f "$HOME/.claude/skills/veda-agent/references/calibration-claude-code.md" && echo "OK: Claude calibration"
grep -q "AskUserQuestion" "$HOME/.claude/skills/veda-agent/references/introduction.md" && echo "OK: intro wired"
```

All three should print `OK`.

### Step 5 — Tell the user what to do next

1. **Start a new Claude Code session** (resumed chats may cache old skill text).
2. Invoke **`veda-agent`** or say **"Hey Veda"**.
3. If they want the **new calibration flow** and already have a sanctum, either:
   - Clear `## Calibration` in `_bmad/sanctum/veda/BOND.md` and say `INTRO`, or
   - Continue as returning user (calibration skipped until BOND lacks calibration).

---

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Old `pu-agent-*` or `bmad-agent-veda` names | Skills not updated — re-run Step 2 |
| Plain numbered lists, no choice UI | Missing `CLAUDE.md` hook or `AskUserQuestion` blocked — copy `CLAUDE.md`, check tool permissions |
| "Skill not found" | Install path wrong — confirm `~/.claude/skills/veda-agent/SKILL.md` exists |
| Memory lost | Update touched sanctum — restore from backup; updates should never delete `_bmad/sanctum/veda/` |
| Git auth fails | Use HTTPS URL above (public repo) or user's SSH: `git@github.com:JMH-Design/veda.git` |

---

## Report to user (template)

After a successful update, reply with:

> **Veda updated** to `{commit}` from github.com/JMH-Design/veda  
> **Skills:** 29 installed → `~/.claude/skills/`  
> **Hook:** `CLAUDE.md` updated in `{project}`  
> **Memory:** unchanged (`_bmad/sanctum/veda/`)  
> **Next:** Start a new Claude Code session → `veda-agent` or "Hey Veda"

---

## Agent permissions

This procedure requires:

- `Bash` / shell — git clone, cp, rm on skill dirs only
- `Read` / `Write` — project `CLAUDE.md` only when merging

Do not request secrets. The repo is public.

---

## Related files (post-update)

| File | Role |
| --- | --- |
| `CLAUDE.md` | Claude Code project hook |
| `skills/veda-agent/references/introduction.md` | Intro flow |
| `skills/veda-agent/references/calibration-claude-code.md` | `AskUserQuestion` payloads |
| `skills/veda-agent/references/calibration-hosts.md` | Host router |
| `docs/getting-started.md` | Human-readable overview |
