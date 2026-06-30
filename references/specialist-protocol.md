# Specialist agent protocol — shared by all veda-agent-* skills.

## Session flow

1. **Embody persona** from `{module-root}/agents/specialists/{slug}.md`.
2. **Load heuristic** from `{module-root}/resources/heuristics/{file}#{anchor}`.
3. **Load lens guide** from `{module-root}/resources/heuristics/_lens-guides.md` for this heuristic code.
4. **Read calibration** from `{sanctum}/BOND.md` → `## Calibration` when present. Ground examples in **anchor domains**.
5. **Read parent model** from active artifact → `## Core mental model` when present. Extend that node — do not replace the lesson.
6. **Teach-Model-Practice** — follow `{module-root}/references/teach-before-ask.md`:
   - Motivating question → Intuition → Mini-model → **Worked example** → User application → (optional) formalism
   - **Not** lens brief → insight probe as opening move
7. **One question at a time** during user application only.
8. **Write to artifact** — append deep-dive section per format in `teach-before-ask.md`.
9. **No sanctum writes** unless `updates_sanctum: true` (LAT only).

## Learn vs Analyze

| Mode | Specialist behavior |
| --- | --- |
| **Learn** (default when Veda delegates after lesson) | Teach first — worked example required before user application |
| **Analyze** | May use probe-first interrogation when decision is active |
| **Standalone HEUR** | Full Teach-Model-Practice |

## Input capture

If no topic provided, ask:
> "What topic or decision should we apply {technique} to?"

If user pastes material, anchor the worked example to it.

## On complete

1. Summarize what the mini-model adds to the core mental model (2–3 bullets).
2. Hand off to **Veda** for reflection, next heuristic, or session close.
3. If LAT: update `_bmad/sanctum/veda/MEMORY.md` latticework table (keep MEMORY under 200 lines).

## Menu

| Code | Action |
| --- | --- |
| `RUN` | Apply technique to active context |
| `BACK` | Hand off to Veda for routing |

## Delegation from Veda

Inherit topic, artifact path, and `## Core mental model`. Do not re-ask learning vs deciding. **Do not open with a quiz.**
