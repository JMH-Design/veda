# Veda — Claude Code

## Running Veda

When the user invokes **Veda** (`veda-agent` skill) or says "Hey Veda":

1. Load skill from `.claude/skills/veda-agent/` or `~/.claude/skills/veda-agent/`.
2. Run introduction per `skills/veda-agent/references/introduction.md`.
3. For calibration Steps B–D, **must** call **`AskUserQuestion`** using payloads in `skills/veda-agent/references/calibration-claude-code.md`.
4. Do not use plain numbered lists when `AskUserQuestion` is available.
5. Claude Code allows max 4 options per question — split Steps C and D per that file.

Sanctum default: `_bmad/sanctum/veda/`

## Updating Veda

When the user asks to **update**, **upgrade**, **refresh**, or **sync Veda** (or reports outdated behavior):

1. Follow **`docs/update-veda-claude-code.md`** end to end.
2. Prefer: `bash scripts/update-veda-claude-code.sh` from a fresh clone, or from `~/.cache/veda-repo` after `git pull`.
3. Never delete `_bmad/sanctum/veda/` or `docs/understanding/`.
4. Report commit hash and remind user to start a **new session**.

Source repo: https://github.com/JMH-Design/veda (branch `main`)
