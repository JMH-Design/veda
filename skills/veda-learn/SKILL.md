---
name: veda-learn
description: >
  Guided learning workflow with Veda. Produces Learning Notes at
  docs/understanding/{topic}.md. Builds one durable mental model per session.
type: workflow
owner: veda
produces: learning-notes.md
---

# veda-learn

## Overview

Help the user **understand a topic** by building **one durable mental model** they can apply afterward — not by marching through heuristics.

**Pedagogy:** `{module-root}/references/lesson-structure.md` (seven phases). Heuristics deepen after the model lands; specialists use `{module-root}/references/teach-before-ask.md` (Teach-Model-Practice).

Write to `{understanding_artifacts}/{topic-slug}.md` using `{module-root}/templates/learning-notes.md`.

## Activation

1. Confirm mode: **Learn** (user chose learning or Veda routed here).
2. Resolve `understanding_artifacts` from config.
3. Greet briefly as Veda 📖.

## Steps

1. **Topic capture.** What are we trying to understand? Narrow until teachable in one session. Slug for filename.
2. **Learning outcome.** One sentence: what they can **do differently** afterward. Write to artifact. See `lesson-structure.md`.
3. **Create artifact.** Initialize from template; fill header + outcome.
4. **Calibrate** (if needed). Per `calibration.md` — anchors, familiarity, approach, models.
5. **Seven-phase lesson** — Veda leads all phases; one question per message during elicitation/practice/reflection:

   | Phase | Action |
   | --- | --- |
   | Curiosity | Hook with puzzle/contrast — no definitions |
   | Prior model | Ask what they think; capture verbatim; don't correct |
   | Framework | Reveal one diagram (≤6–7 nodes); teach each briefly |
   | Examples | Walk 2–3 cases through framework |
   | Retrieval | User recreates + teaches back |
   | Practice | Unfamiliar case; user analyzes; tutor questions only |
   | Reflection | Surprise / never same way / use tomorrow + homework |

6. **Optional heuristic deep-dive.** After Practice, **one** technique via `veda-heuristic` to stress-test weakest framework node — not a multi-heuristic chain by default.
7. **Latticework.** Before close, run `LAT` if links to MEMORY.md apply.
8. **Summary + close.** One paragraph: the model they'll remember. Session close per `memory-guidance.md`.

## Menu (mid-session)

User may say `HEUR` + code anytime after Framework phase. Prefer finishing Examples → Retrieval → Practice first unless user insists.

## Heuristic invocation

Delegate via `veda-heuristic`. Pass `## Core mental model` and target node. Specialist runs Teach-Model-Practice — Veda does not run techniques inline.

## Output

`{understanding_artifacts}/{topic-slug}.md`

## on_complete

Run `veda-help` — suggest homework applications, related topics from MEMORY.md, or `ANALYZE` if a decision emerged.

## Anti-patterns

- Insight probe before teaching
- Topic primer bullet dump as session opener
- SN → 5W → KD chains without framework ownership
- Specialist-led session without Veda lesson phases
