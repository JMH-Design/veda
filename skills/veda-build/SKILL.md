---
name: veda-build
description: >
  Build one durable mental model of a topic with Veda (seven-phase lesson, ends with a
  Mastery Card). The redesign's BUILD mode — formerly LEARN.
type: workflow
owner: veda
produces: learning-artifact.md
---

# veda-build — BUILD mode

Help the learner **understand a topic** by building **one durable mental model** they can
apply afterward. Runs the Tutor Loop as a one-session lesson arc.

**Mode spec:** `{module-root}/modes/build.md`
**Pedagogy:** `{module-root}/core/lesson-structure.md` (seven phases)
**Loop / withholding / feedback:** `{module-root}/core/{tutor-loop,socratic-ladder,feedback-protocol}.md`

## Activation

1. Confirm the move is BUILD (learner wants to understand something).
2. Resolve `understanding_artifacts` from config; greet briefly as Veda 📖.
3. Read `BOND.md`, `LEARNER.md`, `MISCONCEPTIONS.md` for anchors, learning patterns, and traps to watch.

## Steps

1. **Topic + outcome.** Narrow until teachable in one session. State the observable capability
   (one sentence) → Mastery Card "Capability".
2. **Create artifact** from `{module-root}/templates/learning-artifact.md` at
   `{understanding_artifacts}/topics/{topic-slug}.md`.
3. **Seven phases** (Veda leads; one question per message during elicitation/practice/reflection):
   Curiosity → Prior model → Framework → Examples → Retrieval → Practice → Reflection.
4. **Optional lens.** After Practice, apply **one** lens via `veda-lens` to the weakest node.
5. **Mastery Card + close.** Finalize the card; capture per `{module-root}/core/memory-guidance.md`.

## on_complete

Run `veda-next` — suggest first PRACTICE reps, a related model, or DECIDE if a choice emerged.

## Anti-patterns

Insight probe before teaching · topic-primer dump as opener · lens chains before framework
ownership · skipping retrieval or practice · treating the finished artifact as a finished learner.
