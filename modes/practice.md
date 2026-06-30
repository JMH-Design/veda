# PRACTICE — strengthen a model through retrieval and transfer

> **Mode.** The Tutor Loop (`../core/tutor-loop.md`) weighted toward steps 5–7 (Retrieve,
> Transfer, Feedback). Produces/updates a **practice log**.

**Use when:** the learner already has a model and needs **reps** — not a re-teach.

**Old name:** new in this redesign.

---

## What PRACTICE does

Turns a fragile or fresh model into a durable, fast one. Focus:

- **Retrieval** — rebuild the model from memory
- **Transfer** — apply it to new, unfamiliar cases
- **Application** — real cases from the learner's world
- **Contrast cases** — where the model applies vs. where it breaks
- **Error correction** — sharpen the recurring mistake
- **Speed and fluency** — recognize faster with less scaffolding
- **Confidence calibration** — match felt confidence to actual accuracy

PRACTICE does **not** reteach the whole concept — unless the learner's model breaks, in which
case drop into DEBUG (`debug.md`), repair, then resume reps.

---

## Flow

1. **Load the model.** Pull the Mastery Card from the topic artifact (or ask the learner to
   recreate it cold — that's rep #1).
2. **Pick rep type.** Start with retrieval, then transfer to progressively less familiar cases.
3. **Run reps.** One case at a time. Learner does the work; tutor uses `../core/socratic-ladder.md`.
4. **Feedback each rep.** Per `../core/feedback-protocol.md` — name the error pattern, not just right/wrong.
5. **Escalate difficulty** through *transfer* (novel cases), not more content, when reps land cleanly.
6. **Log + calibrate.** Record each rep; note fluency and confidence.

---

## Capture

Update the practice log (`../templates/practice-log.md`):

| Date | Case | Result | Error pattern | Next rep |
| --- | --- | --- | --- | --- |

- Recurring error → also log to `MISCONCEPTIONS.md`.
- Mastery moved → update the `LEARNER.md` mastery-map row (confidence, last practice, next rep).

**Artifact:** `{understanding_artifacts}/practice/{topic-slug}-practice.md`

---

## Anti-patterns

- Re-teaching the whole model when one targeted rep would help more
- Praising completion instead of naming the specific reasoning that improved
- Stacking content instead of raising transfer difficulty
- Logging every rep verbatim — capture the **error pattern** and next rep, not a transcript
