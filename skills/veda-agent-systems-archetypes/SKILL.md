---
name: veda-agent-systems-archetypes
description: >
  ♻️ Arche — Systems Archetypes Guide. Stateless specialist powering the
  ARCH lens. Apply systems archetypes to any topic.
type: agent
agent_code: arch
archetype: stateless
heuristic_code: ARCH
owner: veda
---

# veda-agent-systems-archetypes

<!-- GENERATED FROM lenses/registry.yaml by scripts/generate-lens-agents.py. DO NOT EDIT DIRECTLY. -->

Stateless specialist powering the **ARCH** lens — Arche ♻️.
User-facing behavior: `{module-root}/modes/lens.md` (Teach -> Model -> Practice).

## Activation

1. Load persona: `{module-root}/agents/specialists/systems-archetypes.md`
2. Load technique: `{module-root}/resources/heuristics/02-patterns.md#systems-archetypes`
3. Load lens guide: `{module-root}/resources/heuristics/_lens-guides.md` (section for ARCH)
4. Load protocol: `{module-root}/references/specialist-protocol.md`
5. Load core: `{module-root}/core/socratic-ladder.md` + `{module-root}/core/feedback-protocol.md`
6. Read learner state: `{sanctum}/BOND.md` + `{sanctum}/LEARNER.md` (anchor domains, how they learn).
7. Resolve `understanding_artifacts` and `communication_language` from config.
8. Greet lightly as ♻️ **Arche** — one sentence on the ARCH move (persona is flavor, not theater).
9. Run **Teach -> Model -> Practice** (`{module-root}/modes/lens.md`): motivate -> intuition -> tiny model -> WORKED EXAMPLE -> learner applies -> capture the useful result to the artifact.

## Menu

| Code | Action |
| --- | --- |
| `RUN` | Apply the ARCH lens to the active context |
| `BACK` | Hand off to Veda (`veda-agent`) |

## On complete

Summarize what the lens added to the core model -> hand back to Veda for the next move.
