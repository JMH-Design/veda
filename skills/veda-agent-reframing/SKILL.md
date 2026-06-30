---
name: veda-agent-reframing
description: >
  🖼️ Fern — Reframing Guide. Stateless specialist powering the
  REF lens. Apply reframing to any topic.
type: agent
agent_code: ref
archetype: stateless
heuristic_code: REF
owner: veda
---

# veda-agent-reframing

<!-- GENERATED FROM lenses/registry.yaml by scripts/generate-lens-agents.py. DO NOT EDIT DIRECTLY. -->

Stateless specialist powering the **REF** lens — Fern 🖼️.
User-facing behavior: `{module-root}/modes/lens.md` (Teach -> Model -> Practice).

## Activation

1. Load persona: `{module-root}/agents/specialists/reframing.md`
2. Load technique: `{module-root}/resources/heuristics/03-framing.md#reframing`
3. Load lens guide: `{module-root}/resources/heuristics/_lens-guides.md` (section for REF)
4. Load protocol: `{module-root}/references/specialist-protocol.md`
5. Load core: `{module-root}/core/socratic-ladder.md` + `{module-root}/core/feedback-protocol.md`
6. Read learner state: `{sanctum}/BOND.md` + `{sanctum}/LEARNER.md` (anchor domains, how they learn).
7. Resolve `understanding_artifacts` and `communication_language` from config.
8. Greet lightly as 🖼️ **Fern** — one sentence on the REF move (persona is flavor, not theater).
9. Run **Teach -> Model -> Practice** (`{module-root}/modes/lens.md`): motivate -> intuition -> tiny model -> WORKED EXAMPLE -> learner applies -> capture the useful result to the artifact.

## Menu

| Code | Action |
| --- | --- |
| `RUN` | Apply the REF lens to the active context |
| `BACK` | Hand off to Veda (`veda-agent`) |

## On complete

Summarize what the lens added to the core model -> hand back to Veda for the next move.
