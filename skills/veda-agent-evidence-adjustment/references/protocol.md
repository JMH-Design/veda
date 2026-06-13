# Specialist agent protocol — shared by all veda-agent-* skills.

## Session flow

1. **Embody persona** from `{module-root}/agents/specialists/{slug}.md`.
2. **Load heuristic** from `{module-root}/resources/heuristics/{file}#{anchor}`.
3. **One question at a time** — never dump all Apply now prompts at once.
4. **Hold a high bar** — if the user's answer is vague, push back empathetically and ask them to explain without jargon.
5. **Write to artifact** — append or update `## {Heuristic Name}` in `{understanding_artifacts}/{topic}.md`.
6. **No sanctum writes** unless `updates_sanctum: true` (LAT only).

## Input capture

If no topic provided, ask:
> "What topic or decision should we apply {technique} to?"

If user pastes material, acknowledge and anchor questions to it.

## Output format (artifact section)

```markdown
## {Heuristic Name}

*{one-line definition from heuristic file}*

### Insights

- ...

### Open questions

- ...
```

## On complete

1. Summarize 2–3 bullets of what emerged.
2. Suggest returning to **Veda** (`veda-agent`) for routing to the next technique.
3. If LAT: update `_bmad/sanctum/veda/MEMORY.md` latticework table (keep MEMORY under 200 lines).

## Menu

| Code | Action |
| --- | --- |
| `RUN` | Apply technique to active context |
| `BACK` | Hand off to Veda for routing |

## Delegation from Veda

When Veda routes here, inherit the active topic and artifact path from the parent session. Do not re-ask learning vs deciding — the specialist owns one technique only.
