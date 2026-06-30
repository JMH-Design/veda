# Veda — System Overview

> **Last updated:** 2026-06-29 (v2 — learner-state architecture)
> Canonical reference for how the Veda module fits together — architecture, the Tutor Loop,
> modes, memory, lenses, and file layout.

Veda is a **BMAD module** that helps you build durable understanding, practice reasoning,
correct misconceptions, and leave each session thinking differently. It is built around a
**warm, rigorous, lightly funny mentor** who teaches you to think — not a workflow router.

**Design goal:** Veda should feel like *"a teacher who understands the learner, chooses the
right teaching move, helps them practice, corrects their reasoning, and preserves durable
understanding"* — not *"a system that routes the user into learning workflows."*

---

## The central shift (v1 → v2)

The old architecture asked: **"Which workflow should I run?"**

```text
Veda → Route to Learn / Analyze / Help / Heuristic → Write Artifact → Update Memory
```

The new architecture asks: **"What does this learner need next?"**

```text
Veda → Learner State → Tutor Loop → Mode → Practice / Feedback → Memory
```

**Learner state is the central object of the system.** Veda maintains an active model of what
the learner understands, misunderstands, how they learn best, which models are fragile vs.
durable, and what they should practice next.

---

## Architecture

```text
Veda 📖  (memory orchestrator + teacher identity)
│
├── Learner State            _bmad/sanctum/veda/
│   ├── BOND.md              identity + stable preferences
│   ├── LEARNER.md           HOW they learn + mastery map
│   ├── MEMORY.md            durable mental models (latticework)
│   ├── MISCONCEPTIONS.md    HOW they tend to be wrong
│   └── sessions/            raw history
│
├── Tutor Core               veda/core/
│   ├── tutor-loop.md        Diagnose→Orient→Model→Demonstrate→Retrieve→Transfer→Feedback→Capture
│   ├── lesson-structure.md  seven-phase BUILD pedagogy
│   ├── feedback-protocol.md kind, specific, useful correction
│   ├── socratic-ladder.md   when to withhold vs. answer
│   ├── memory-guidance.md   what to capture, where
│   └── voice.md             how Veda sounds
│
├── Modes                    veda/modes/
│   ├── BUILD   build a durable mental model
│   ├── PRACTICE strengthen via retrieval + transfer
│   ├── DEBUG   repair confusion / misconception
│   ├── DECIDE  work through a decision
│   ├── LENS    apply one thinking lens
│   ├── NEXT    recommend the next move
│   └── REVIEW  revisit prior models
│
├── Lens Library             veda/lenses/  (Foundations·Patterns·Framing·Synthesis·Validation)
│
└── Artifacts                docs/understanding/
    ├── topics/{topic}.md          (Mastery Card + session notes)
    ├── decisions/{decision}.md    (Decision Memo)
    └── practice/{topic}-practice.md (Practice Log)
```

---

## The Tutor Loop

Every mode runs the loop (`core/tutor-loop.md`) unless there's a clear reason not to:

```text
1. Diagnose   → what does the learner need now?
2. Orient     → say what we're doing and why (briefly)
3. Model      → simplest useful mental model
4. Demonstrate→ show the model seeing one example
5. Retrieve   → learner rebuilds the model from memory
6. Transfer   → learner applies it to an unfamiliar case
7. Feedback   → sharpen the reasoning (feedback-protocol.md)
8. Capture    → persist only durable value (memory-guidance.md)
```

Withholding within the loop follows the **Socratic Ladder** (`core/socratic-ladder.md`):
guide before answering *when learning improves* — but never riddle jail, and give the answer
the moment withholding stops serving the learner.

---

## Modes — teaching moves, not tools

| Code | Use when the learner… | Produces | Was |
| --- | --- | --- | --- |
| **BUILD** | wants to understand a topic | learning artifact (Mastery Card) | LEARN |
| **PRACTICE** | has a model, needs reps | practice log | new |
| **DEBUG** | is confused / wrong / stuck | Misconception Ledger entry | new |
| **DECIDE** | faces a choice or tradeoff | decision memo | ANALYZE |
| **LENS** | wants one thinking lens | artifact deep-dive section | HEUR |
| **NEXT** | asks what to do next | chat recommendation | HELP |
| **REVIEW** | wants to revisit a model | updated mastery row | new |

Veda diagnoses which move fits — it doesn't present a menu of tools. When intent is vague, it
makes a reasonable assumption and offers a direction.

### BUILD (the seven phases)

`Curiosity → Prior model → Framework → Examples → Retrieval → Practice → Reflection`, building
**one** durable mental model and ending with a **Mastery Card**. Opens with a puzzle, never a
definition dump. Full detail: `core/lesson-structure.md`.

---

## Lens Library

The 24 thinking techniques are presented as a **Lens Library** (`lenses/index.md`), grouped
Foundations → Patterns → Framing → Synthesis → Validation. Each lens is *a thinking move*; the
persona behind it (Petra, Sena, Clio, …) is **flavor**, used lightly. Internally each lens is a
stateless specialist agent (`veda-agent-{slug}`) that runs **Teach → Model → Practice**
(`modes/lens.md`). Lenses deepen a model **after** the learner owns the core framework — never
a forced chain.

**Generation source of truth:** `lenses/registry.yaml`.

---

## Memory — the sanctum (learner state)

**Default path:** `_bmad/sanctum/veda/`. Load order on rebirth: `INDEX` → `PERSONA`, `CREED`,
`BOND`, `LEARNER`, `MEMORY`, `MISCONCEPTIONS`, `CAPABILITIES`.

| File | Holds |
| --- | --- |
| `BOND.md` | Identity + stable preferences |
| `LEARNER.md` | **How** they learn; current mastery map |
| `MEMORY.md` | **Durable mental models** (not summaries) |
| `MISCONCEPTIONS.md` | **How** they tend to be wrong (raw material, never shame) |
| `sessions/` | Append-only raw logs (not loaded on rebirth) |

Capture rule (`core/memory-guidance.md`): **only durable value.** Memory is not a junk drawer.

---

## Artifacts — a growing library of understanding

| Mode | Artifact | Template |
| --- | --- | --- |
| BUILD | `topics/{topic}.md` (opens with Mastery Card) | `templates/learning-artifact.md` |
| DECIDE | `decisions/{decision}.md` | `templates/decision-memo.md` |
| PRACTICE | `practice/{topic}-practice.md` | `templates/practice-log.md` |
| — | the portable object | `templates/mastery-card.md` |

---

## Module layout

```text
veda/
├── module.yaml · config.toml · README.md
├── docs/      system-overview.md · getting-started.md · architecture.md · migration-v2.md
├── core/      tutor-loop · lesson-structure · feedback-protocol · socratic-ladder · memory-guidance · voice
├── modes/     build · practice · debug · decide · lens · next · review
├── lenses/    registry.yaml · index.md · guides/
├── agents/    veda.md · specialists/ (24 lens personas, generated)
├── references/ specialist-protocol.md · teach-before-ask.md (lens plumbing) · lesson-structure.md (→core)
├── resources/ heuristics/ (technique content) · agents/ (legacy roster)
├── skills/    veda-agent · veda-build/practice/debug/decide/lens/next · veda-agent-{slug} ×24
│              (+ legacy aliases: veda-learn/analyze/heuristic/help)
├── scripts/   generate-lens-agents.py (formerly generate-specialist-agents.py)
└── templates/ learning-artifact · mastery-card · practice-log · decision-memo
```

**Canonical protocols live in `core/`.** Mode behavior in `modes/`. The Cursor mirror
(`.cursor/skills/`) and any Claude Code skills are generated/synced from these — see
`migration-v2.md`. Mark generated files: `<!-- GENERATED FROM veda/core/…. DO NOT EDIT. -->`.

---

## Pedagogical rules (all modes)

1. Don't answer too early — guide when it helps (Socratic Ladder).
2. Don't withhold too long — no riddle jail.
3. Make the model visible.
4. Use examples as bridges, not decoration.
5. Require retrieval.
6. Require transfer.
7. Correct kindly and clearly.
8. Capture only durable value.
9. Prefer one good next step over a curriculum.
10. Make progress emotionally visible.

---

## Key reference map

| Question | Read |
| --- | --- |
| How does Veda decide what to do? | `core/tutor-loop.md` |
| How does BUILD teaching work? | `core/lesson-structure.md` |
| When does Veda answer vs. ask? | `core/socratic-ladder.md` |
| How does Veda respond to an answer? | `core/feedback-protocol.md` |
| How does Veda sound? | `core/voice.md` |
| What gets remembered, where? | `core/memory-guidance.md` |
| What are the lenses? | `lenses/index.md` |
| What changed from v1? | `docs/migration-v2.md` |

---

## Related docs

- [Getting started](./getting-started.md)
- [Architecture](./architecture.md)
- [Migration v1 → v2](./migration-v2.md)
