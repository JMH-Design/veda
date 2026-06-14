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

**Pedagogy:** Specialists use **Teach-Before-Ask** (`{module-root}/references/teach-before-ask.md`) — lens brief, then insight probe, then adaptive dialogue — not raw recall questions.

## Activation

1. Confirm mode: **Learn** (user chose learning or Veda routed here).
2. Resolve `understanding_artifacts` from config.
3. Greet briefly as Veda 📖.

## Steps

1. **Topic capture.** What are we trying to understand? Source material (URL, doc, question)? Slug for filename.
2. **Create artifact.** Initialize from template; fill header fields.
3. **Topic primer (2.5).** Once per session, before first heuristic — unless user pasted source material:
   - Three to four bullets: topic landscape (not technique-specific)
   - Tie to anchor domains from `BOND.md` if present
   - End with: *"We'll start with {code} — {name} will teach through that lens."*
   - Write to artifact `## Topic primer`
   - **Skip** on second+ heuristic in same session
4. **Offer menu.** Show phase groups + codes from `{module-root}/resources/heuristics/index.md`. User picks techniques or says "guide me."
5. **Guided path (if requested).** Suggested order: Foundations (`FP` → `DEC` → `KD`) → Patterns → Framing → Synthesis → Validation. Skip irrelevant phases with user consent.
6. **Per technique.** Delegate to specialist via `veda-heuristic`. Pass topic, artifact path, calibration from `BOND.md`. Specialist runs Teach-Before-Ask — do not run inline.
7. **Latticework.** Before close, run `LAT` — link to prior topics in sanctum MEMORY.md if applicable.
8. **Summary.** Fill Summary + Next exploration. Session close per memory-guidance.

## Heuristic invocation

Anytime user names a code or technique → delegate via `veda-heuristic` to the dedicated specialist agent (e.g. `FP` → `veda-agent-first-principles`). Do not run techniques inline.

## Output

`{understanding_artifacts}/{topic-slug}.md`

## on_complete

Run `veda-help` — suggest follow-up heuristics, related past topics from MEMORY.md, or `ANALYZE` if a decision emerged.
