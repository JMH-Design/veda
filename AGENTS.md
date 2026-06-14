# Veda — Codex

When the user invokes **Veda** (`veda-agent` skill) or says "Hey Veda":

1. Load skill from `.agents/skills/veda-agent/`, `~/.codex/skills/veda-agent/`, or project `skills/veda-agent/`.
2. Run introduction per `skills/veda-agent/references/introduction.md`.
3. For calibration Steps B–D, **must** call **`ask_user_question`** using payloads in `skills/veda-agent/references/calibration-codex.md`.
4. For voice (Step 2a) and **VOICE** command, **must** call **`ask_user_question`** using `skills/veda-agent/references/voices.md`.
5. Do not use plain numbered lists when `ask_user_question` is available.
6. If only in Code mode and the tool is blocked, switch to Plan mode or use text fallback in `calibration.md` / `voices.md`.
7. After Q&A, echo captured choices in chat for the session log.

Sanctum default: `_bmad/sanctum/veda/`

**ChatGPT:** structured choice UI is not available for custom skills — use `calibration.md` and `voices.md` text fallback.
