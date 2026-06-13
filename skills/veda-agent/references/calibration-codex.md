# Calibration — Codex (`ask_user_question`)

Use when running Veda in **OpenAI Codex** (CLI or VS Code extension).

Load option text from `calibration.md`. Prefer **`ask_user_question`** (tabbed questionnaire UI). Fallback: **`request_user_input`** (max 3 options per question — use numbered list from `calibration.md` instead).

**Mode:** Tool may require **Plan mode** or `default_mode_request_user_input = true` in Codex config. If unavailable in Code mode, switch to Plan or use text fallback.

---

## Step B — Topic familiarity (learn only)

```json
{
  "questions": [
    {
      "id": "topic_familiarity",
      "header": "Familiarity",
      "question": "How well do you already know {topic}?",
      "options": [
        { "value": "new", "label": "Brand new", "description": "Haven't really encountered this before" },
        { "value": "exposure", "label": "Some exposure", "description": "Heard or read about it; couldn't explain well" },
        { "value": "comfortable", "label": "Comfortable", "description": "Could explain basics to someone else" },
        { "value": "practitioner", "label": "Practitioner", "description": "Work with this regularly" }
      ]
    }
  ]
}
```

---

## Step C — Natural approach

```json
{
  "questions": [
    {
      "id": "natural_approach",
      "header": "Approach",
      "question": "When you hit a hard problem, what's your first instinct?",
      "options": [
        { "value": "decompose", "label": "Break into parts", "description": "Split into pieces to tackle one at a time" },
        { "value": "compare", "label": "Compare to cases", "description": "What usually happens in situations like this" },
        { "value": "why", "label": "Ask why", "description": "Peel layers to root cause" },
        { "value": "assumptions", "label": "Challenge assumptions", "description": "Test what I'm taking for granted" },
        { "value": "invert", "label": "Flip upside down", "description": "Imagine failure or what to avoid" },
        { "value": "analogy", "label": "Find what it's like", "description": "Bridge from something I know" },
        { "value": "unsure", "label": "Not sure yet", "description": "Still finding my approach" }
      ]
    }
  ]
}
```

---

## Step D — Mental models (multi-select)

Codex multi-select: user toggles options, then **Enter** for Next / Submit.

```json
{
  "questions": [
    {
      "id": "mental_models",
      "header": "Models",
      "question": "Which thinking tools do you already reach for? Pick any that fit.",
      "multiSelect": true,
      "options": [
        { "value": "fp", "label": "First principles", "description": "Rebuild from what must be true" },
        { "value": "systems", "label": "Systems thinking", "description": "Feedback loops and unintended effects" },
        { "value": "base-rates", "label": "Base rates", "description": "What usually happens in cases like this" },
        { "value": "inversion", "label": "Inversion", "description": "Avoid failure; think backwards" },
        { "value": "hypothesis", "label": "Hypothesis testing", "description": "State beliefs; seek evidence" },
        { "value": "key-drivers", "label": "Key drivers", "description": "Few factors that move everything else" },
        { "value": "none", "label": "None yet", "description": "Still building my toolkit" },
        { "value": "other", "label": "Other", "description": "I'll describe something else" }
      ]
    }
  ]
}
```

If `other` selected, follow with free-text in chat or a second `ask_user_question` with no options (freeform question id).

---

## ChatGPT (web / desktop)

ChatGPT can load Agent Skills for code interpreter workflows but does **not** expose `ask_user_question` for custom Veda sessions today. Use **`calibration.md` fallback** (numbered lists). Revisit when OpenAI adds structured input to ChatGPT skills.

---

## AGENTS.md hook

Project `AGENTS.md` should include:

> During Veda calibration (Steps B–D), **must** use `ask_user_question` when available — never plain numbered lists.

---

## Notes

- One calibration step per tool call (pace like Cursor).
- After Q&A, echo choices back in chat so the session log shows what was captured.
- Legacy `request_user_input`: max 3 options — do not use for Veda calibration; use text fallback instead.
