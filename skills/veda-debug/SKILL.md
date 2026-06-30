---
name: veda-debug
description: >
  Repair confusion, a misconception, or broken reasoning with Veda. Finds the exact break,
  fixes it kindly, updates the Misconception Ledger. New in the redesign.
type: workflow
owner: veda
produces: misconception-ledger-entry
---

# veda-debug — DEBUG mode

The learner is confused, stuck, wrong, overwhelmed, or holding a fragile model. Find the
**exact point where reasoning breaks** and repair it — kindly and clearly. Don't re-teach the topic.

**Mode spec:** `{module-root}/modes/debug.md`
**Feedback / withholding:** `{module-root}/core/{feedback-protocol,socratic-ladder}.md`

## Steps

1. **Locate the break** with one diagnostic question at a time: what stops making sense? what
   causes what? which distinction is blurry? what example contradicts the model? where does it fail?
2. **Name it without blame** — "that confusion is useful; it's pointing at the hinge."
3. **Repair** — sharper distinction + a small example that makes it click.
4. **Re-test** — learner re-applies the repaired model to the case that broke, then a fresh one.
5. **If overwhelmed** — "too many pieces on the table; let's reduce to the three that matter."
6. **Capture** — if the misconception is durable/repeated, add a row to
   `_bmad/sanctum/veda/MISCONCEPTIONS.md` (Topic | Misconception | Better model | Evidence | Review later?).

## on_complete

If the model was broadly fragile → `veda-practice` for reps. Else `veda-next`.
