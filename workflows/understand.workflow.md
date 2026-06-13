# Workflow: Understand Anything

```yaml
workflow:
  skill: veda-agent
  module: veda
  owner: veda
  produces: docs/understanding/{topic}.md
  on_complete: "Run veda-help for next step."
```

## Goal

Deep understanding — whether learning a topic or deciding what to do — using the thinking heuristics, with Veda remembering your latticework across sessions.

## Entry

Invoke **`veda-agent`**. Veda runs the **introduction**:

1. **Welcome** — first meeting or welcome back by name
2. **Name** — asked on first meeting only
3. **Goal** — learn, decide, explore, or one technique
4. **Skills catalog** — plain-language overview of workflows + 24 specialists (always on first meeting; `INTRO` anytime)

Then route:

| Answer | Workflow | Template |
| --- | --- | --- |
| Learning | `veda-learn` | `templates/learning-notes.md` |
| Deciding | `veda-analyze` | `templates/decision-memo.md` |
| Either / technique only | `veda-heuristic` | — |
| Explore / what's available | `INTRO` | — |

## Heuristic menu (anytime)

User invokes by code — see `resources/heuristics/index.md`.

## Artifacts

Default path: `docs/understanding/{topic-slug}.md` (config: `understanding_artifacts`).

## Memory

Sanctum: `_bmad/sanctum/veda/` — init via `veda-agent/scripts/init-sanctum.py`.

## Session close

1. Write/update artifact
2. Session log → `sessions/YYYY-MM-DD.md`
3. Curate latticework → `MEMORY.md`
