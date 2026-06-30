# Veda — Architecture

> Why the system is shaped the way it is. For the map of files and modes, see
> [`system-overview.md`](./system-overview.md); for what changed, see
> [`migration-v2.md`](./migration-v2.md).

---

## One sentence

Veda is a **mentor** whose central object is the **learner's state**; it diagnoses what the
learner needs, runs the **Tutor Loop** through the appropriate **mode**, and preserves only
**durable understanding** in a learner-state memory.

---

## Four layers

```text
┌──────────────────────────────────────────────────────────────┐
│ IDENTITY        voice.md · PERSONA · CREED · BOND             │  who Veda is, who it teaches
├──────────────────────────────────────────────────────────────┤
│ TUTOR CORE      tutor-loop · lesson-structure · feedback ·    │  HOW Veda teaches (mode-agnostic)
│                 socratic-ladder · memory-guidance             │
├──────────────────────────────────────────────────────────────┤
│ MODES           build · practice · debug · decide · lens ·    │  WHICH teaching move, this turn
│                 next · review                                 │
├──────────────────────────────────────────────────────────────┤
│ KNOWLEDGE       LEARNER · MEMORY · MISCONCEPTIONS · artifacts │  what the learner knows / mis-knows
└──────────────────────────────────────────────────────────────┘
```

The Tutor Core is the heart. Modes are thin — each is the loop with a different center of
gravity (BUILD centers on Model/Demonstrate; PRACTICE on Retrieve/Transfer; DEBUG on Diagnose;
DECIDE on a live choice). This keeps behavior consistent across modes and avoids re-inventing
pedagogy per workflow.

---

## Why each change improves learning outcomes

| Change | Why it teaches better |
| --- | --- |
| **Learner state as the central object** | Teaching adapts to the person. A tutor who remembers how you learn and how you tend to be wrong is dramatically more effective than one who only remembers topics. |
| **Tutor Loop in every mode** | Guarantees the moves that actually build durable memory — **retrieval** and **transfer** — happen, instead of being optional. Explanation quality ≠ understanding. |
| **Socratic Ladder** | Calibrates struggle. Productive struggle deepens encoding; riddle jail and answer-vending both kill it. The ladder makes "how much help" an explicit decision. |
| **Feedback Protocol** | Most learning happens in the correction. Specific, kind feedback (what works → what's blurry → sharper model → retry) turns errors into gains; generic praise teaches nothing. |
| **Mastery Card** | A portable memory object lets the learner re-enter a concept in 60 seconds, enabling spaced REVIEW — the single biggest lever for retention. |
| **Misconception Ledger** | Great teaching tracks not just what's known but *how the learner is wrong*. Repaired-pattern pairs prevent re-teaching the same break. |
| **PRACTICE + REVIEW modes** | Understanding decays without reps and spacing. First-class modes make reinforcement a normal move, not an afterthought. |
| **DEBUG mode** | Confusion is localized. A mode dedicated to *finding the break* repairs faster and kinder than re-explaining the whole topic. |
| **Lens Library (demote personas)** | Foregrounds the *thinking move* over the character roster, so depth feels purposeful, not like managing a cast. Lenses still teach (Teach→Model→Practice), never quiz. |
| **One durable model per BUILD** | A single coherent model the learner owns beats a tour of facts they forget. Curiosity-first openings create the tension that makes the model stick. |
| **Capture only durable value** | Noisy memory degrades future teaching. Curated learner state keeps Veda sharp over time. |
| **One next step (NEXT)** | Momentum beats overwhelm. A single high-value rep is more likely to happen than a 12-week curriculum. |

---

## What's preserved from v1

Veda as memory orchestrator · the sanctum · one durable model per BUILD · the seven-phase
lesson · decision work · stateless lenses · lenses-deepen-after-the-framework · the
anti-pattern against forced heuristic marches. The redesign **reframes around learner state**;
it does not discard the strong core.

---

## Source of truth & generation

Canonical protocols live in `core/`; mode behavior in `modes/`; the lens registry in
`lenses/registry.yaml`. Host-specific skill folders (Cursor `.cursor/skills/`, Claude Code)
are **generated/synced** from these — never hand-duplicated as a separate source. Generated
files carry a banner: `<!-- GENERATED FROM veda/core/…. DO NOT EDIT DIRECTLY. -->`.
