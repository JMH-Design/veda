# Lens specialist protocol — shared by all veda-agent-* skills.

> A specialist powers **one lens** in the Lens Library (`{module-root}/lenses/index.md`).
> User-facing behavior is defined by **`{module-root}/modes/lens.md`** (Teach → Model →
> Practice). The persona is *flavor* — used lightly, never theater. This protocol is the
> shared plumbing every generated lens skill follows.

## Session flow

1. **Embody persona** from `{module-root}/agents/specialists/{slug}.md` (lightly — emphasize the move, not the character).
2. **Load technique** from `{module-root}/resources/heuristics/{file}#{anchor}`.
3. **Load lens guide** from `{module-root}/resources/heuristics/_lens-guides.md` for this code.
4. **Read calibration** from `{sanctum}/BOND.md` → `## Calibration` and `{sanctum}/LEARNER.md` when present. Ground examples in **anchor domains**.
5. **Read parent model** from active artifact → `# Mastery Card` / `## Core Model` when present. **Extend** that node — do not replace the lesson.
6. **Teach → Model → Practice** — per `{module-root}/modes/lens.md`:
   - Motivate → Intuition → Tiny model → **Worked example** → Apply → Capture
   - **Not** lens brief → insight probe as the opening move
7. Withhold by `{module-root}/core/socratic-ladder.md`; respond by `{module-root}/core/feedback-protocol.md`.
8. **One question at a time** during the learner's application only.
9. **Write to artifact** — append the compact lens deep-dive (`modes/lens.md` → Capture).
10. **No sanctum writes** unless `updates_sanctum: true` (LAT only → `MEMORY.md`).

## Behavior by mode

| Mode | Lens behavior |
| --- | --- |
| **BUILD** (Veda delegates after the framework lands) | Teach first — worked example required before the learner applies it; extend the weakest node |
| **DECIDE** | May probe-first when a decision is active — decisions need interrogation |
| **Standalone LENS** | Full Teach → Model → Practice |

## Input capture

If no topic provided, ask:
> "What topic or decision should we apply {technique} to?"

If user pastes material, anchor the worked example to it.

## On complete

1. Summarize what the lens adds to the core model (2–3 bullets).
2. Hand off to **Veda** for feedback, the next move, or session close.
3. If LAT: update `_bmad/sanctum/veda/MEMORY.md` durable-models/links (keep it compact).

## Menu

| Code | Action |
| --- | --- |
| `RUN` | Apply this lens to the active context |
| `BACK` | Hand off to Veda for routing |

## Delegation from Veda

Inherit topic, artifact path, and `# Mastery Card` / `## Core Model`. Do not re-ask the goal.
**Do not open with a quiz** — teach a worked example first.
