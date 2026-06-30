# Workflow: Understand Anything

```yaml
workflow:
  skill: veda-agent
  module: veda
  owner: veda
  produces: docs/understanding/{topic}.md
  on_complete: "Run veda-next for the next move."
```

## Goal

Deep understanding — build durable mental models, practice reasoning, repair confusion, and
decide well — with Veda modeling the learner's state across sessions.

## Entry

Invoke **`veda-agent`**. Veda runs the **introduction**, then **diagnoses** what the learner
needs and routes to a mode:

| Need | Mode | Template |
| --- | --- | --- |
| Understand a topic | `BUILD` (`veda-build`) | `templates/learning-artifact.md` |
| Reps on a model | `PRACTICE` (`veda-practice`) | `templates/practice-log.md` |
| Repair confusion | `DEBUG` (`veda-debug`) | Misconception Ledger |
| Decide | `DECIDE` (`veda-decide`) | `templates/decision-memo.md` |
| One thinking lens | `LENS` (`veda-lens`) | artifact deep-dive |
| What's next? | `NEXT` (`veda-next`) | — |

Every mode runs the **Tutor Loop** (`core/tutor-loop.md`). Legacy codes (LEARN/ANALYZE/HEUR/HELP) still route.

## Lens menu (anytime)

Bring in one lens by code — see `lenses/index.md`.

## Artifacts

Default path: `docs/understanding/{topic-slug}.md` (config: `understanding_artifacts`).

## Memory

Sanctum: `_bmad/sanctum/veda/` — init via `veda-agent/scripts/init-sanctum.py`.

## Session close

Per `core/memory-guidance.md`:

1. Write/update artifact (Mastery Card / memo / practice row)
2. Session log → `sessions/YYYY-MM-DD.md`
3. Curate durable models → `MEMORY.md`; update `LEARNER.md` / `MISCONCEPTIONS.md` only on a durable pattern
