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

**Orchestrator & modes:**
- `veda-agent`
- `veda-build`, `veda-practice`, `veda-debug`, `veda-decide`, `veda-lens`, `veda-next`
- (legacy aliases, still work: `veda-learn`, `veda-analyze`, `veda-heuristic`, `veda-help`)

**Lenses (24 stateless specialists — one per thinking move):**
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

**Claude Code — keep Veda current:** `docs/update-veda-claude-code.md` (or say "update Veda")

## 4. Start a session

Say: **"Hey Veda"** or invoke `veda-agent`.

**First meeting**, Veda will:

1. Welcome you
2. Ask your **name**
3. Ask your **voice** — Tutor, Scientist, Sparring Partner, or Explorer (`VOICE` anytime to switch)
4. Ask your **goal** (learn, decide, explore, or one technique)
5. **Calibrate** — anchor domains; choice UI for approach & models (learn only)
6. Show the **skills catalog** in plain language — workflows + 24 specialists

**Returning visits:** greet by name, offer to keep or change voice, ask goal. Say **`INTRO`** for catalog, **`VOICE`** to switch tone.

Introduction: `skills/veda-agent/references/introduction.md` · Calibration: `skills/veda-agent/references/calibration.md`

### How Veda teaches

Veda diagnoses what you need, then runs the **Tutor Loop** through one **mode**. It teaches a
model, shows it on an example, makes you **retrieve** and **transfer** it, gives sharp feedback,
and captures only durable value.

- **BUILD** sessions follow the **seven-phase lesson** ([`core/lesson-structure.md`](../core/lesson-structure.md)):
  curiosity → prior model → one framework → examples → retrieval → practice → reflection, ending
  with a **Mastery Card**. Lenses deepen **after** practice — never a default chain.
- Withholding follows the **Socratic Ladder** ([`core/socratic-ladder.md`](../core/socratic-ladder.md)) —
  guide when it helps, answer when it doesn't.
- Lenses run **Teach → Model → Practice** ([`modes/lens.md`](../modes/lens.md)).

**Full system map:** [`docs/system-overview.md`](system-overview.md) · **Why it's shaped this way:** [`docs/architecture.md`](architecture.md)

### Examples

| You say | Mode |
| --- | --- |
| "Hey Veda" (first time) | Introduction → name → voice → goal → calibration → catalog |
| "VOICE" | Voice picker — Tutor / Scientist / Sparring Partner / Explorer |
| "Help me understand how DNS works" | `BUILD` |
| "I get the idea but it's fuzzy — quiz me" | `PRACTICE` |
| "I'm confused why X causes Y" | `DEBUG` |
| "Should I take this job offer?" | `DECIDE` |
| "Run inversion on my launch plan" | `LENS` → Iris (`veda-agent-inversion`) |
| "What's next?" | `NEXT` |

## 5. Two ways to use a lens

1. **Through Veda** — say "Run FP" and it brings in the First Principles lens.
2. **Direct** — invoke `veda-agent-first-principles` for a focused lens session.

Lenses are stateless (fresh each time). Veda holds the learner state and latticework.

## 6. Artifacts

Outputs land in `docs/understanding/` by default:

- `topics/{topic}.md` — learning artifact (opens with a Mastery Card)
- `decisions/{decision}.md` — decision memo
- `practice/{topic}-practice.md` — practice log
- Configure the base path via `understanding_artifacts` in module config

## 7. Lens cheat sheet

| Code | Lens | Skill |
| --- | --- | --- |
| `FP` | First Principles 🪨 | `veda-agent-first-principles` |
| `RC` | Reference Class 📊 | `veda-agent-reference-class` |
| `INV` | Inversion 🔄 | `veda-agent-inversion` |
| `SN` | Signal vs Noise 📡 | `veda-agent-signal-noise` |
| `LAT` | Latticework 🔗 | `veda-agent-latticework` |

Full library: [`lenses/index.md`](../lenses/index.md).

## Source material

Heuristics from [`user-manual.md`](../../user-manual.md) (source user manual, pages 2–6).
