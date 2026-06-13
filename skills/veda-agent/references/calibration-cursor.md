# Calibration — Cursor (`AskQuestion`)

Use when running Veda in **Cursor Agent**. One tool call per calibration step.

Load option text from `calibration.md`. Call **`AskQuestion`** with these payloads.

---

## Step B — Topic familiarity (learn only)

```json
{
  "title": "Topic familiarity",
  "questions": [
    {
      "id": "topic_familiarity",
      "prompt": "How well do you already know {topic}?",
      "options": [
        { "id": "new", "label": "Brand new — I haven't really encountered this before" },
        { "id": "exposure", "label": "Some exposure — heard or read about it, couldn't explain well" },
        { "id": "comfortable", "label": "Comfortable — I could explain the basics to someone else" },
        { "id": "practitioner", "label": "Practitioner — I work with this regularly" }
      ],
      "allow_multiple": false
    }
  ]
}
```

---

## Step C — Natural approach

```json
{
  "title": "Natural approach",
  "questions": [
    {
      "id": "natural_approach",
      "prompt": "When you hit a hard problem, what's your first instinct?",
      "options": [
        { "id": "decompose", "label": "Break it into parts" },
        { "id": "compare", "label": "Compare to past cases" },
        { "id": "why", "label": "Ask why repeatedly" },
        { "id": "assumptions", "label": "Challenge assumptions" },
        { "id": "invert", "label": "Flip it upside down" },
        { "id": "analogy", "label": "Find what it's like" },
        { "id": "unsure", "label": "Not sure yet" }
      ],
      "allow_multiple": false
    }
  ]
}
```

---

## Step D — Mental models

```json
{
  "title": "Mental models",
  "questions": [
    {
      "id": "mental_models",
      "prompt": "Which thinking tools do you already reach for? Pick any that fit.",
      "options": [
        { "id": "fp", "label": "First principles" },
        { "id": "systems", "label": "Systems thinking" },
        { "id": "base-rates", "label": "Base rates" },
        { "id": "inversion", "label": "Inversion" },
        { "id": "hypothesis", "label": "Hypothesis testing" },
        { "id": "key-drivers", "label": "Key drivers" },
        { "id": "none", "label": "None yet" },
        { "id": "other", "label": "Other — I'll describe in chat" }
      ],
      "allow_multiple": true
    }
  ]
}
```

If `other` selected, ask free-text follow-up: *"What else do you use?"*

---

## Notes

- Requires **Agent mode** (Plan mode also works in some Cursor versions).
- If `AskQuestion` unavailable, fall back to `calibration.md` numbered list.
