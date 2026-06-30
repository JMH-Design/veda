# Migration — v1 → v2 (learner-state architecture)

> What changed when Veda moved from a workflow router to a learner-state-centered mentor, and
> how to migrate an existing install. Nothing in v1 is thrown away — the strongest parts are
> preserved and reframed.

---

## The shift in one line

```text
v1:  Veda → Route to Learn/Analyze/Help/Heuristic → Artifact → Memory
v2:  Veda → Learner State → Tutor Loop → Mode → Practice/Feedback → Memory
```

---

## Renamed modes (aliases preserved)

| v1 | v2 | Purpose | Back-compat |
| --- | --- | --- | --- |
| LEARN | **BUILD** | Build a durable mental model | `veda-learn` aliases `veda-build` |
| ANALYZE | **DECIDE** | Decision / tradeoff / plan | `veda-analyze` aliases `veda-decide` |
| HEUR | **LENS** | Apply one thinking lens | `veda-heuristic` aliases `veda-lens` |
| HELP | **NEXT** | Recommend the next move | `veda-help` aliases `veda-next` |
| — | **PRACTICE** | Reps: retrieval + transfer | new |
| — | **DEBUG** | Repair confusion / misconception | new |
| (optional) | **REVIEW** | Revisit prior models | new (lives in `veda-next`) |

Old codes (`LEARN`, `ANALYZE`, `HEUR`, `HELP`) still work and route to the new modes.

---

## New / moved files

**New canonical core (`veda/core/`):**
`tutor-loop.md` · `feedback-protocol.md` · `socratic-ladder.md` · `voice.md` · plus
`lesson-structure.md` and `memory-guidance.md` (canonical homes; the `references/` and
`skills/veda-agent/references/` copies become pointers/mirrors).

**New mode files (`veda/modes/`):** `build · practice · debug · decide · lens · next · review`.

**New lens library (`veda/lenses/`):** `index.md` (five groups, personas as flavor),
`registry.yaml` (moved generation source), `guides/`.

**New sanctum files (`_bmad/sanctum/veda/`):** `LEARNER.md`, `MISCONCEPTIONS.md`; `MEMORY.md`
reshaped to **durable models** (not session summaries); `INDEX.md`, `BOND.md`, `CAPABILITIES.md` updated.

**New / revised templates (`veda/templates/`):** `mastery-card.md` (new),
`learning-artifact.md` (replaces `learning-notes.md`), `practice-log.md` (new),
`decision-memo.md` (slimmed).

**New skills (`veda/skills/`):** `veda-build · veda-practice · veda-debug · veda-decide ·
veda-lens · veda-next`. Old `veda-learn/analyze/heuristic/help` are now thin aliases.

**New docs:** `architecture.md`, `migration-v2.md`; `system-overview.md` rewritten.

---

## Migration steps for an existing install

1. **Add sanctum files.** Create `LEARNER.md` and `MISCONCEPTIONS.md` (templates in this doc's
   sibling files). Reshape `MEMORY.md` to durable-model entries — move session narrative out.
2. **Keep artifacts.** Existing `docs/understanding/*.md` stay valid. New BUILD artifacts go in
   `topics/`, decisions in `decisions/`, practice in `practice/`. Add a Mastery Card to active
   topics when you next touch them.
3. **Regenerate lenses.** Run `python scripts/generate-lens-agents.py` so the 24 specialist
   skills reference `core/` + `modes/lens.md` and run Teach → Model → Practice.
4. **Sync host skills.** Regenerate/sync the Cursor mirror (`.cursor/skills/`) and any Claude
   Code skills from canonical sources. Mark generated files with the DO-NOT-EDIT banner.
5. **Update commands.** Prefer the new mode codes; old codes keep working via aliases.

---

## What did NOT change

- Veda is still the **memory orchestrator** with a sanctum.
- BUILD still builds **one durable mental model** via the **seven phases**.
- Lenses are still **stateless** and still **deepen after** the framework lands — never a chain.
- DECIDE still delays the recommendation until validation content exists.
- The anti-pattern against turning learning into a forced heuristic march is **stronger**, now
  joined by: don't confuse artifacts with learning, don't overuse personas, don't store noisy
  memory, don't be an answer vending machine, don't be a smug Socratic gatekeeper.

---

## Files retained for compatibility (will be reconciled)

- `references/lesson-structure.md` → superseded by `core/lesson-structure.md` (kept as mirror).
- `references/teach-before-ask.md` → lens plumbing; canonical behavior in `modes/lens.md`.
- `resources/agents/{registry.yaml,index.md}` → superseded by `lenses/`; registry copied to
  `lenses/registry.yaml` as the generation source.
- `templates/learning-notes.md` → replaced by `templates/learning-artifact.md`.
