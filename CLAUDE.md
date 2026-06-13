# Veda — Claude Code

When the user invokes **Veda** (`veda-agent` skill) or says "Hey Veda":

1. Load skill from `.claude/skills/veda-agent/` or `~/.claude/skills/veda-agent/`.
2. Run introduction per `skills/veda-agent/references/introduction.md`.
3. For calibration Steps B–D, **must** call **`AskUserQuestion`** using payloads in `skills/veda-agent/references/calibration-claude-code.md`.
4. Do not use plain numbered lists when `AskUserQuestion` is available.
5. Claude Code allows max 4 options per question — split Steps C and D per that file.

Sanctum default: `_bmad/sanctum/veda/`
