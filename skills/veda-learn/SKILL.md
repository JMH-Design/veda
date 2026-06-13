---
name: veda-learn
description: >
  Guided learning workflow with Veda. Produces Learning Notes at
  docs/understanding/{topic}.md. User menu for heuristics anytime.
type: workflow
owner: veda
produces: learning-notes.md
---

# veda-learn

## Overview

Help the user **understand a topic** using the User Manual heuristics. Conversational, user-menu driven — not a forced march through all 20 techniques. Write to `{understanding_artifacts}/{topic-slug}.md` using `{module-root}/templates/learning-notes.md`.

## Activation

1. Confirm mode: **Learn** (user chose learning or Veda routed here).
2. Resolve `understanding_artifacts` from config.
3. Greet briefly as Veda 📖.

## Steps

1. **Topic capture.** What are we trying to understand? Source material (URL, doc, question)? Slug for filename.
2. **Create artifact.** Initialize from template; fill header fields.
3. **Offer menu.** Show phase groups + codes from `{module-root}/resources/heuristics/index.md`. User picks techniques or says "guide me."
4. **Guided path (if requested).** Suggested order: Foundations (`FP` → `DEC` → `KD`) → Patterns → Framing → Synthesis → Validation. Skip irrelevant phases with user consent.
5. **Per technique.** Delegate to specialist via `veda-heuristic` (e.g. `FP` → Petra). Do not run inline.
6. **Latticework.** Before close, run `LAT` — link to prior topics in sanctum MEMORY.md if applicable.
7. **Summary.** Fill Summary + Next exploration. Session close per memory-guidance.

## Heuristic invocation

Anytime user names a code or technique → delegate via `veda-heuristic` to the dedicated specialist agent (e.g. `FP` → `veda-agent-first-principles`). Do not run techniques inline.

## Output

`{understanding_artifacts}/{topic-slug}.md`

## on_complete

Run `veda-help` — suggest follow-up heuristics, related past topics from MEMORY.md, or `ANALYZE` if a decision emerged.
