# Veda — System Overview

> **Last updated:** 2026-06-28  
> Canonical reference for how the Veda module fits together — architecture, workflows, memory, pedagogy, and file layout.

Veda is a **BMAD module** for deep understanding. It combines a **memory orchestrator** (Veda 📖), **two main workflows** (Learn and Analyze), and **24 stateless heuristic specialists** (Petra, Anya, Clio, …) — each owning one thinking technique from the [User Manual](../../user-manual.md).

**Design goal:** Help you leave sessions **thinking differently** — with durable mental models and recorded reasoning — not memorizing technique lists.

---

## At a glance

| Layer | What it is | Persists? |
| --- | --- | --- |
| **Veda** (`veda-agent`) | Memory orchestrator — intro, routing, latticework | Yes — sanctum |
| **Learn** (`veda-learn`) | Build understanding of a topic | Artifacts + sanctum |
| **Analyze** (`veda-analyze`) | Work through a decision | Artifacts + sanctum |
| **Heuristic routing** (`veda-heuristic`) | Delegate one technique to a specialist | Artifact section |
| **24 specialists** (`veda-agent-{slug}`) | Stateless technique guides | No — fresh each invoke |
| **Help** (`veda-help`) | Inspect state, recommend next step | Read-only |

---

## Architecture

```text
                         ┌─────────────────────────────────┐
                         │  Veda 📖 (memory orchestrator)   │
                         │  sanctum · intro · routing       │
                         └───────────────┬─────────────────┘
                                         │
           ┌─────────────────────────────┼─────────────────────────────┐
           │                             │                             │
           ▼                             ▼                             ▼
    ┌─────────────┐              ┌─────────────┐              ┌─────────────┐
    │   LEARN     │              │   ANALYZE   │              │    HELP     │
    │ veda-learn  │              │veda-analyze │              │  veda-help  │
    └──────┬──────┘              └──────┬──────┘              └─────────────┘
           │                             │
           │    seven-phase lesson       │    decision memo + heuristics
           │    (Veda leads)             │    (probe-friendly)
           │                             │
           └──────────────┬──────────────┘
                          │ optional, after core work
                          ▼
                 ┌─────────────────┐
                 │  veda-heuristic  │
                 │  HEUR + code     │
                 └────────┬─────────┘
                          │
                          ▼
         ┌────────────────────────────────────────────┐
         │  Specialist (stateless) — e.g. Petra 🪨   │
         │  Teach-Model-Practice on one technique     │
         └────────────────┬───────────────────────────┘
                          │ writes section
                          ▼
              docs/understanding/{topic}.md
                          │
                          ▼
              hand off back to Veda → close / next step
```

### Memory vs stateless

| Agent type | Archetype | Remembers | Examples |
| --- | --- | --- | --- |
| **Veda** | memory | Sanctum, latticework, BOND preferences | `veda-agent` |
| **Specialists** | stateless | Nothing — read artifact + BOND each time | Petra, Sena, Wren, … |
| **Lia (LAT)** | stateless + sanctum write | Updates `MEMORY.md` latticework | `veda-agent-latticework` |

---

## Session lifecycle

### 1. Open — Introduction

Veda runs `skills/veda-agent/references/introduction.md`:

| Visit | Flow |
| --- | --- |
| **First meeting** | Welcome → name → goal → calibration → skills catalog → route |
| **Returning** | Welcome by name → goal → route (`INTRO` for full catalog) |

**Calibration** (`calibration.md`): anchor domains, topic familiarity, natural approach, mental models — saved to `BOND.md`. Host-specific UI in Cursor (`AskQuestion`), Claude Code, Codex, or text fallback.

**Pace:** One question per message during intro.

### 2. Route — Pick a workflow

| User intent | Code | Workflow | Output template |
| --- | --- | --- | --- |
| Understand a topic | `LEARN` | `veda-learn` | `templates/learning-notes.md` |
| Make a decision | `ANALYZE` | `veda-analyze` | `templates/decision-memo.md` |
| One technique | `HEUR` + code | `veda-heuristic` → specialist | Section in active artifact |
| What's next? | `HELP` | `veda-help` | Chat recommendations |
| Full catalog | `INTRO` | introduction Step 3 | — |

### 3. Work — Workflow-specific

See [Learn mode](#learn-mode) and [Analyze mode](#analyze-mode) below.

### 4. Close — Memory guidance

Per `references/memory-guidance.md`:

1. Finalize artifact (`Summary`, `Next exploration`)
2. Append session log → `_bmad/sanctum/veda/sessions/YYYY-MM-DD.md`
3. Curate latticework → `MEMORY.md` (keep under 200 lines)
4. Run `veda-help` for follow-up suggestions

---

## Learn mode

**Skill:** `veda-learn`  
**Pedagogy:** `references/lesson-structure.md`  
**Artifact:** `docs/understanding/{topic}.md`

### Philosophy

Learn sessions build **one durable mental model** per session — not a forced march through heuristics. The goal is an observable capability:

> *By the end, I can look at X and explain Y.*

Heuristics **deepen** after the model lands; they are not the default spine.

### Seven phases (Veda leads)

| # | Phase | Purpose |
| --- | --- | --- |
| 1 | **Curiosity** | Hook with puzzle/contrast — no definitions |
| 2 | **Prior model** | Elicit what user already believes; don't correct |
| 3 | **Framework** | Reveal one diagram (≤6–7 nodes) |
| 4 | **Examples** | Walk 2–3 cases through the framework |
| 5 | **Retrieval** | User recreates + teaches back |
| 6 | **Practice** | Unfamiliar case — user analyzes, tutor questions only |
| 7 | **Reflection** | Surprise / never same way / homework applications |

**Time mix target:** ~10% framework · ~20% examples · ~40% discussion · ~20% practice · ~10% reflection.

### Optional heuristic deep-dive

After **Practice**, Veda may delegate **one** specialist via `veda-heuristic` to stress-test the weakest framework node. Not SN → 5W → KD chains by default.

### Anti-patterns (Learn)

- Insight probe before teaching
- Topic-primer bullet dump as session opener
- Multi-heuristic chains without framework ownership
- Specialist-led session skipping lesson phases

---

## Analyze mode

**Skill:** `veda-analyze`  
**Artifact:** Decision Memo in `docs/understanding/{topic}.md`

Analyze sessions target **choices, plans, and stuck problems**. Heuristic interrogation is appropriate here — suggested path emphasizes reference class, inversion, challenging assumptions, reframing, validation.

Flow: decision capture → artifact → menu or guided path → delegate specialists → recommendation only after validation content exists.

---

## Specialist system

### Roster

24 specialists — one heuristic each. Source of truth:

- [`resources/agents/registry.yaml`](../resources/agents/registry.yaml)
- [`resources/agents/index.md`](../resources/agents/index.md)

Five phase groups: **Foundations → Patterns → Framing → Synthesis → Validation**.

### Invocation

1. **Through Veda** — "Run FP on this" → `veda-heuristic` → Petra
2. **Direct** — invoke `veda-agent-first-principles` for a focused session

### Specialist protocol

**Reference:** `references/specialist-protocol.md` + `references/teach-before-ask.md`

| Mode | Specialist behavior |
| --- | --- |
| **Learn** (after core lesson) | **Teach-Model-Practice** — motivating question → intuition → mini-model → **worked example** → user application |
| **Analyze** | May probe-first when decision is active |
| **Standalone HEUR** | Full Teach-Model-Practice |

**Learn delegation:** Veda passes `## Core mental model` from artifact; specialist extends one node — does not replace the lesson or open with a quiz.

### Regenerate specialists

After editing `registry.yaml`:

```bash
python veda/scripts/generate-specialist-agents.py
```

---

## Memory — the sanctum

**Default path:** `_bmad/sanctum/veda/`

| File | Purpose |
| --- | --- |
| `INDEX.md` | Sanctum map — loaded on every Veda rebirth |
| `PERSONA.md` | Voice and style |
| `CREED.md` | Mission and values |
| `BOND.md` | Owner name, preferences, **calibration** |
| `MEMORY.md` | Curated latticework (<200 lines) |
| `CAPABILITIES.md` | Built-in + learned capabilities |
| `sessions/` | Raw session logs (not loaded on rebirth) |

**Init:**

```bash
python veda/skills/veda-agent/scripts/init-sanctum.py \
  --sanctum _bmad/sanctum/veda \
  --owner "Your Name"
```

---

## Artifacts

**Default path:** `docs/understanding/` (config: `understanding_artifacts` in `config.toml`)

| Template | Used by | Structure |
| --- | --- | --- |
| `templates/learning-notes.md` | Learn | Outcome → session log → core model → examples → retrieval → practice → optional heuristic deep-dives |
| `templates/decision-memo.md` | Analyze | Decision framing + heuristic sections + recommendation |

Artifacts are your **growing library of understanding** — linkable from `MEMORY.md`.

---

## Module layout

```text
veda/
├── module.yaml              # Module manifest, phases, agent registry
├── config.toml              # understanding_artifacts, language
├── README.md                # Quick start (links here for depth)
├── docs/
│   ├── system-overview.md   # ← this file
│   └── getting-started.md   # Install + first session steps
├── agents/
│   ├── veda.md              # Orchestrator persona
│   └── specialists/         # 24 heuristic personas
├── references/              # Shared protocols (canonical)
│   ├── lesson-structure.md  # Learn pedagogy (seven phases)
│   ├── teach-before-ask.md  # Specialist Teach-Model-Practice
│   ├── specialist-protocol.md
│   └── memory-guidance.md
├── resources/
│   ├── agents/              # registry.yaml, index.md
│   └── heuristics/          # Technique content + lens guides
├── skills/
│   ├── veda-agent/          # Orchestrator launcher + intro/calibration refs
│   ├── veda-learn/
│   ├── veda-analyze/
│   ├── veda-heuristic/
│   ├── veda-help/
│   └── veda-agent-{slug}/   # 24 specialist launchers
├── scripts/
│   └── generate-specialist-agents.py
└── templates/
    ├── learning-notes.md
    └── decision-memo.md
```

### Cursor install mirror

Skills are copied to `.cursor/skills/` in this project. **Canonical protocols** live under `veda/references/`; skill folders may duplicate `references/` subsets (e.g. `veda-agent/references/introduction.md`).

When editing pedagogy, update **`veda/references/`** first, then sync dependent skill docs.

---

## Key reference map

| Question | Read |
| --- | --- |
| How do I start? | `docs/getting-started.md` |
| How does Learn teaching work? | `references/lesson-structure.md` |
| How do specialists teach? | `references/teach-before-ask.md` |
| Session introduction flow | `skills/veda-agent/references/introduction.md` |
| Calibration | `skills/veda-agent/references/calibration.md` |
| Which specialist for code X? | `resources/agents/index.md` |
| Heuristic definitions | `resources/heuristics/` |
| Lens guide per code | `resources/heuristics/_lens-guides.md` |
| Veda menu commands | `agents/veda.md` |

---

## Configuration

**Team scope** (`config.toml` / installer):

- `understanding_artifacts` — default `docs/understanding`
- `communication_language` — default `en`

**User scope** (sanctum / BOND):

- `owner_name`
- Calibration: anchor domains, familiarity, approach, mental models
- Session style, typical mode (learning / deciding)

---

## What was outdated (pre-2026-06-28)

These files described the **old Learn pedagogy** (probe-first, heuristic chains):

| File | Stale content |
| --- | --- |
| `README.md` | Architecture diagram omits seven-phase Learn |
| `docs/getting-started.md` | "Lens brief → insight probe" as primary Learn flow |
| `agents/veda.md` | Learn mode: "lens brief → insight probe → dialogue" |
| `skills/veda-heuristic/SKILL.md` | Step 5 still says lens brief → insight probe first |

**Current truth:** Learn = `lesson-structure.md` (seven phases, one mental model). Specialists = Teach-Model-Practice after core lesson or standalone HEUR.

---

## Quick command reference

| Say | Result |
| --- | --- |
| "Hey Veda" | Introduction → route |
| `LEARN` + topic | Seven-phase lesson |
| `ANALYZE` + decision | Decision memo workflow |
| `HEUR` + `FP` | Route to Petra |
| `INTRO` | Full skills catalog |
| `HELP` | Next-step recommendations |
| `MEM` | Latticework summary from sanctum |
| `ROSTER` | All 24 specialists |
| `VOICE` | Switch Tutor / Scientist / Sparring Partner / Explorer |

---

## Source material

Heuristics transcribed from [`user-manual.md`](../../user-manual.md) (pages 2–6). Phase 5 validation heuristics inferred where source was incomplete.

---

## Related docs

- [Getting started](./getting-started.md) — install and first session
- [Update Veda for Claude Code](./update-veda-claude-code.md) — sync skills to Claude Code
