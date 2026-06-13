# Getting started with Veda

## 1. Install the module

Copy `veda/` into your BMAD project or install via the BMad Method installer when published.

## 2. Initialize Veda's memory

```bash
python veda/skills/veda-agent/scripts/init-sanctum.py \
  --sanctum _bmad/sanctum/veda \
  --owner "Your Name"
```

Or invoke `veda-agent` — Veda will guide First Breath on first run.

## 3. Copy skills to your tool

Place skill folders under your AI tool's skills directory:

**Orchestrator & workflows:**
- `veda-agent`
- `veda-learn`, `veda-analyze`, `veda-heuristic`, `veda-help`

**Specialists (24 agents — one per heuristic):**
- `veda-agent-first-principles` (Petra 🪨)
- `veda-agent-analogical-reasoning` (Anya 🌉)
- `veda-agent-reference-class` (Clio 📊)
- … full list in [`resources/agents/index.md`](../resources/agents/index.md)

Tip: copy all `veda-agent-*` folders, or only the specialists you use often.

### Host-specific choice UI

Calibration uses clickable options when the host supports it:

| Host | Config file | Tool |
| --- | --- | --- |
| Cursor | `.cursor/skills/veda-agent/` | `AskQuestion` |
| Claude Code | `CLAUDE.md` | `AskUserQuestion` |
| Codex | `AGENTS.md` | `ask_user_question` |
| ChatGPT | — | text fallback |

Details: `skills/veda-agent/references/calibration-hosts.md`

## 4. Start a session

Say: **"Hey Veda"** or invoke `veda-agent`.

**First meeting**, Veda will:

1. Welcome you
2. Ask your **name**
3. Ask your **goal** (learn, decide, explore, or one technique)
4. **Calibrate** — anchor domains; choice UI for approach & models (Cursor / Claude Code / Codex — see `calibration-hosts.md`)
5. Show the **skills catalog** in plain language — workflows + 24 specialists

**Returning visits:** greet by name, ask goal. Say **`INTRO`** anytime to see the full catalog again.

Introduction: `skills/veda-agent/references/introduction.md` · Calibration: `skills/veda-agent/references/calibration.md`

### Examples

| You say | Routes to |
| --- | --- |
| "Hey Veda" (first time) | Introduction → name → goal → calibration → catalog |
| "INTRO" | Full skills catalog |
| "Help me understand how DNS works" | `LEARN` |
| "Should I take this job offer?" | Veda → `ANALYZE` |
| "Run inversion on my launch plan" | Veda → `HEUR` → Iris (`veda-agent-inversion`) |
| "Talk to Petra about AI architecture" | `veda-agent-first-principles` directly |
| "What's next?" | Veda → `HELP` |

## 5. Two ways to use a heuristic

1. **Through Veda** — say "Run FP" and she delegates to Petra.
2. **Direct specialist** — invoke `veda-agent-first-principles` for a focused session.

Specialists are stateless (fresh each time). Veda holds memory and latticework.

## 6. Artifacts

Outputs land in `docs/understanding/` by default:

- `{topic}.md` — Learning Notes or Decision Memo
- Configure path via `understanding_artifacts` in module config

## 7. Specialist cheat sheet

| Code | Agent | Skill |
| --- | --- | --- |
| `FP` | 🪨 Petra | `veda-agent-first-principles` |
| `ANA` | 🌉 Anya | `veda-agent-analogical-reasoning` |
| `RC` | 📊 Clio | `veda-agent-reference-class` |
| `INV` | 🔄 Iris | `veda-agent-inversion` |
| `LAT` | 🔗 Lia | `veda-agent-latticework` |

Full roster: [`resources/agents/index.md`](../resources/agents/index.md).

## Source material

Heuristics from [`user-manual.md`](../../user-manual.md) (source user manual, pages 2–6).
