# Calibration — Claude Code (`AskUserQuestion`)

Use when running Veda in **Claude Code** (VS Code extension or CLI).

Load option text from `calibration.md`. Call **`AskUserQuestion`**. Do **not** add a manual "Other" option — Claude appends it automatically.

**Constraint:** max **4 options per question**. Split Steps C and D into two calls each (below).

---

## Step B — Topic familiarity (learn only)

One call — 4 options.

```json
{
  "questions": [
    {
      "header": "Familiarity",
      "question": "How well do you already know {topic}?",
      "multiSelect": false,
      "options": [
        { "label": "Brand new", "description": "I haven't really encountered this before" },
        { "label": "Some exposure", "description": "Heard or read about it; couldn't explain it well" },
        { "label": "Comfortable", "description": "I could explain the basics to someone else" },
        { "label": "Practitioner", "description": "I work with this regularly" }
      ]
    }
  ]
}
```

---

## Step C — Natural approach (2 calls)

**Call C1** — pick one:

```json
{
  "questions": [
    {
      "header": "Approach 1",
      "question": "When you hit a hard problem, what's your first instinct? (Part 1 of 2)",
      "multiSelect": false,
      "options": [
        { "label": "Break into parts", "description": "Split the problem into pieces I can tackle one at a time" },
        { "label": "Compare to cases", "description": "Look for what usually happens in situations like this" },
        { "label": "Ask why", "description": "Peel layers until I hit root cause" },
        { "label": "Challenge assumptions", "description": "List what I'm taking for granted and test each" }
      ]
    }
  ]
}
```

**Call C2** — only if user did not answer in C1:

```json
{
  "questions": [
    {
      "header": "Approach 2",
      "question": "Or is your instinct one of these? (Part 2 of 2)",
      "multiSelect": false,
      "options": [
        { "label": "Flip upside down", "description": "Imagine how this fails or what to avoid" },
        { "label": "Find what it's like", "description": "Bridge from something I already understand" },
        { "label": "Not sure yet", "description": "Still finding my approach — Veda can route by topic" }
      ]
    }
  ]
}
```

If user answered in C1, skip C2.

---

## Step D — Mental models (2 calls, multi-select)

**Call D1:**

```json
{
  "questions": [
    {
      "header": "Models 1",
      "question": "Which thinking tools do you already reach for? (Part 1 of 2 — pick any)",
      "multiSelect": true,
      "options": [
        { "label": "First principles", "description": "Rebuild from what must be true" },
        { "label": "Systems thinking", "description": "Feedback loops, stocks and flows" },
        { "label": "Base rates", "description": "What usually happens in cases like this" },
        { "label": "Inversion", "description": "Avoid failure; think backwards" }
      ]
    }
  ]
}
```

**Call D2:**

```json
{
  "questions": [
    {
      "header": "Models 2",
      "question": "Any others? (Part 2 of 2 — pick any)",
      "multiSelect": true,
      "options": [
        { "label": "Hypothesis testing", "description": "State beliefs and look for evidence" },
        { "label": "Key drivers", "description": "Find the few factors that move everything else" },
        { "label": "None yet", "description": "Still building my toolkit" }
      ]
    }
  ]
}
```

Merge selections from D1 + D2. If user picks only `None yet`, save `Mental models: None yet`.

---

## CLAUDE.md hook

Project `CLAUDE.md` should include:

> During Veda calibration (Steps B–D), **must** use `AskUserQuestion` — never plain numbered lists when the tool is available.

---

## Notes

- Add `allowed-tools: AskUserQuestion` on custom commands if you gate tools.
- If tool unavailable (e.g. non-interactive), fall back to `calibration.md` numbered list.
