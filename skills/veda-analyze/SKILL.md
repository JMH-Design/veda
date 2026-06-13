---
name: veda-analyze
description: >
  Guided decision/analysis workflow with Veda. Produces Decision Memo at
  docs/understanding/{topic}.md. User menu for heuristics anytime.
type: workflow
owner: veda
produces: decision-memo.md
---

# veda-analyze

## Overview

Help the user **decide or analyze** a choice, plan, or stuck problem. Write to `{understanding_artifacts}/{topic-slug}.md` using `{module-root}/templates/decision-memo.md`.

## Activation

1. Confirm mode: **Analyze** (user chose deciding or Veda routed here).
2. Resolve `understanding_artifacts` from config.
3. Greet briefly as Veda 📖.

## Steps

1. **Decision capture.** What decision? Options? Stakes? Timeline? Slug for filename.
2. **Create artifact.** Initialize from template.
3. **Offer menu.** Heuristic codes from index — emphasize `RC`, `INV`, `CA`, `REF` for decisions.
4. **Guided path (if requested).** Suggested order: Foundations (`FP`, `KD`) → Patterns (`RC`, `SN`) → Framing (`REF`, `INV`, `CA`, `5W`) → Synthesis (`INT`, `PERSP`) → Validation (`HYP`, `PRED`).
5. **Per technique.** Delegate to specialist via `veda-heuristic` (e.g. `RC` → Clio, `INV` → Iris). Do not run inline.
6. **Recommendation.** Only after validation section has content — state recommendation + confidence + falsifiers.
7. **Session close.** Log + update latticework if decision pattern is reusable.

## Heuristic invocation

User can jump to any code mid-flow → delegate via `veda-heuristic` to the dedicated specialist agent.

## Output

`{understanding_artifacts}/{topic-slug}.md`

## on_complete

Run `veda-help` — note review date for predictions, suggest `LEARN` if knowledge gaps remain.
