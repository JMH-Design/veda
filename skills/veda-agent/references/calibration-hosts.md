# Calibration hosts — structured question UI

Veda calibration uses **host-native choice tools** when available. Shared steps and option text live in `calibration.md`. **Tool payloads** live in host files below.

## Host detection

| Host | Tool | Host file | Root config |
| --- | --- | --- | --- |
| **Cursor** (Agent) | `AskQuestion` | `calibration-cursor.md` | `.cursor/skills/veda-agent/` |
| **Claude Code** (VS Code / CLI) | `AskUserQuestion` | `calibration-claude-code.md` | `CLAUDE.md` |
| **Codex** (CLI / VS Code) | `ask_user_question` | `calibration-codex.md` | `AGENTS.md` |
| **ChatGPT** (web / desktop) | *(none for custom skills)* | — | numbered-list fallback in `calibration.md` / `voices.md` |
| **Unknown / no tool** | — | — | `calibration.md` → Fallback |

**On session open:** detect host from environment, then load the matching host file for calibration Steps B–D and voice Step 2a (`voices.md`). Always use free text for calibration Step A (anchor domains).

## Rules (all hosts)

1. **One structured step per tool call** — never batch C + D in one form (Cursor/Codex may allow multi-question calls; Veda still paces one calibration step at a time).
2. **Same option labels** as `calibration.md` — only the tool schema changes.
3. **Save identically** to `BOND.md` → `## Calibration` regardless of host.
4. **Step B** only when goal is Learn.

## Install pointers

| Tool | Install skills to |
| --- | --- |
| Cursor | `~/.cursor/skills/` or `.cursor/skills/` |
| Claude Code | `~/.claude/skills/` or `.claude/skills/` |
| Codex | `~/.codex/skills/` or `.agents/skills/` |
| ChatGPT | Upload skill bundle / mount in code-interpreter environment when supported |

Run `./install.sh` for Cursor. For other hosts, copy `skills/veda-agent/` to the path above and place `CLAUDE.md` / `AGENTS.md` in the project root.
