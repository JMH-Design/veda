---
name: veda-decide
description: >
  Work through a decision, tradeoff, or plan with Veda. Produces a Decision Memo; the
  recommendation comes last. The redesign's DECIDE mode — formerly ANALYZE.
type: workflow
owner: veda
produces: decision-memo.md
---

# veda-decide — DECIDE mode

Help the learner **decide well** — and become better at deciding — not just receive a verdict.
Delay the recommendation until the reasoning supports it.

**Mode spec:** `{module-root}/modes/decide.md`
**Lenses:** `{module-root}/modes/lens.md` + `{module-root}/lenses/index.md`

## Steps

1. **Clarify the decision** — what, by when, stakes. Slug for filename.
2. **Create artifact** from `{module-root}/templates/decision-memo.md` at
   `{understanding_artifacts}/decisions/{decision-slug}.md`.
3. **Options → Constraints → Assumptions.**
4. **Apply the few lenses that move it** (via `veda-lens`) — strong defaults: `RC`, `INV`,
   `CA`, `REF`, `PRED`. Not a forced chain.
5. **Stress-test the leading option** — where does it break? what would change the answer?
6. **Recommend — only now** — recommendation + confidence + what would raise/lower it.
7. **Prediction + review date** (PRED) so the decision teaches later.

## on_complete

Run `veda-next` — note the review date for REVIEW; suggest BUILD if a knowledge gap blocked the call.
