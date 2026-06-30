---
name: veda-practice
description: >
  Strengthen an existing mental model through retrieval and transfer reps with Veda.
  Produces/updates a practice log. New in the redesign.
type: workflow
owner: veda
produces: practice-log.md
---

# veda-practice — PRACTICE mode

The learner **already has a model** and needs reps — retrieval, transfer, contrast cases,
error correction, fluency, confidence calibration. Do **not** re-teach unless the model breaks.

**Mode spec:** `{module-root}/modes/practice.md`
**Loop / withholding / feedback:** `{module-root}/core/{tutor-loop,socratic-ladder,feedback-protocol}.md`

## Steps

1. **Load the model.** Pull the Mastery Card from the topic artifact, or have the learner
   recreate it cold (rep #1).
2. **Create/open** `{understanding_artifacts}/practice/{topic-slug}-practice.md` from
   `{module-root}/templates/practice-log.md`.
3. **Run reps** — one case at a time, retrieval first then transfer to less familiar cases.
   Learner does the work; tutor uses the Socratic Ladder.
4. **Feedback each rep** — name the error pattern, not just right/wrong.
5. **Escalate difficulty through transfer** (novel cases), not more content.
6. **Log** each rep + fluency note. If the model breaks → `veda-debug`. Recurring error →
   `MISCONCEPTIONS.md`. Mastery moved → update `LEARNER.md` mastery-map row.

## on_complete

Run `veda-next` — more reps, REVIEW later, or LENS for depth once reps land cleanly.
