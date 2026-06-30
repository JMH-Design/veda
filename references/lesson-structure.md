# Lesson structure — Veda Learn pedagogy

**Goal:** Help the user leave **thinking differently** — not remembering 30 facts or surviving a heuristic interrogation.

**Core belief:** The highest-leverage teaching builds a **durable mental model** (a new way of seeing). Heuristics deepen parts of that model; they are not the primary spine of a Learn session.

**Load with:** `veda-learn`, `veda-agent`, `teach-before-ask.md`, `specialist-protocol.md`

---

## What went wrong (anti-pattern)

| Anti-pattern | Symptom |
| --- | --- |
| Probe-first | Lens brief → insight probe → dialogue feels like a quiz |
| Heuristic march | SN → 5W → KD chained before user owns one framework |
| Thin teaching | 5 bullets, then "your turn" — no examples walked through |
| No curiosity hook | Starts with landscape bullets, not a puzzle |
| No prior-model elicitation | Assumes or skips "what do you think X is?" |
| No retrieval | Never asks user to recreate or teach back the model |
| No guided practice | User analyzes unfamiliar cases only in dialogue, not as explicit phase |
| Formulas-before-intuition | Technique vocabulary before the question it answers |

---

## Session outcome (define first)

Before teaching anything, state **one sentence**:

> By the end of this session, you should be able to **[observable capability]**.

Examples:

- *…look at any AI trend headline and separate signal from story, mechanism from buzz.*
- *…explain why a statistical claim might mislead without knowing the formula.*
- *…describe who a product is for, what problem it solves, and what tradeoffs were made.*

Write to artifact `## Learning outcome`.

If the topic is too broad for one session, **narrow it** with the user until the outcome fits ~45–60 minutes of chat.

---

## The seven phases

Adapted from one-hour classroom design. In chat, phases flex in length but **order is fixed** unless user skips with consent.

```text
Outcome → Curiosity → Prior model → Framework → Examples → Retrieval → Practice → Reflection
```

| Phase | Purpose | Who leads | Chat budget |
| --- | --- | --- | --- |
| **1. Curiosity** | Hook with puzzle/contrast — no definitions | Veda | ~1 message |
| **2. Prior model** | Elicit what user already believe; don't correct yet | Veda asks, user writes | ~1 message |
| **3. Framework** | Reveal **one** simple model (≤6–7 nodes); ~2 min per node | Veda teaches | 1–2 messages |
| **4. Examples** | Walk 2–3 cases **through the framework** — not product lectures | Veda teaches | 2–3 messages |
| **5. Retrieval** | User recreates framework from memory; teach it back | User produces, Veda coaches | ~1–2 turns |
| **6. Practice** | Unfamiliar case — **user** analyzes using framework; tutor questions only | User leads | 2–4 turns |
| **7. Reflection** | Surprise / never look same way / use tomorrow | User answers | 1 message |

**Time mix target:** ~10% framework reveal · ~20% examples · ~40% discussion · ~20% practice · ~10% reflection.

**Pace:** One question per message during Prior model, Practice, and Reflection. Teaching phases may use longer messages with diagrams.

---

## Phase details

### 1 — Curiosity (don't start with definitions)

Open with a **contrast, puzzle, or headline** that creates productive disagreement.

Good:

- Two coffee mugs — "Which is better?" → "Better for *who*?"
- Jelly bean jar — "Can you know the exact count?"
- Two students, two sample means — "Who's correct?"
- Three trending AI labels — "Which are you overweighting because of your feed?"

Bad:

- Bullet list of topic landscape
- "Let's define signal vs noise"
- Immediate insight probe

Write hook + user reaction to artifact `## Session log` → Curiosity.

### 2 — Prior model (discover, don't correct)

Ask what they think the topic **is** or **is about**. Capture verbatim.

> What do you think **[topic]** actually is? Or: what do people in this space mostly get wrong?

**Do not correct.** List their model in the artifact. Corrections come through the framework and examples.

### 3 — Framework (one diagram, few concepts)

Draw **one** coherent model — ASCII or mermaid. Cap at **6–7 nodes**.

Everything in the session maps to this diagram. Introduce each node briefly (~2 sentences), not a glossary.

Example frameworks:

**Product designer thinking:**

```text
Person → Problem → Goal → Constraints → Solution → Outcome
```

**Statistics under uncertainty:**

```text
Reality → Population → Sample → Measurement → Analysis → Decision
```

**AI trends (example for Jared's session):**

```text
Story (noise) → Mechanism → Evidence → Incentive → Deployment → Durability
```

State explicitly: *"Everything we do today fits inside this."*

Write full framework to artifact `## Core mental model`.

### 4 — Examples (framework repeatedly)

Walk **2–3 examples** through every node of the framework. Vary domain (familiar anchor → topic → contrasting failure case).

Rules:

- **Teach the framework**, not the product trivia
- Use anchor domains from `BOND.md` when possible
- Contrast cases stick (terrible microwave UI, polling failure, hype headline)

Write condensed walkthroughs to artifact `## Examples`.

### 5 — Retrieval (ownership test)

Hide or collapse the framework. Ask user to:

1. Recreate it approximately (ASCII ok)
2. **Teach it back** in their own words

If they can't explain it, **re-teach one node** — do not advance to heuristics or new content.

Write their retrieval to artifact `## Retrieval`.

### 6 — Practice (user does the work)

Present an **unfamiliar** case (product, headline, artifact, scenario). User analyzes using the framework.

Tutor role: **questions only** — no lecturing unless they're stuck after 2 nudges.

Good nudge: *"You named the story — what's the mechanism underneath?"*

Write practice dialogue to artifact `## Practice`.

### 7 — Reflection (emotional close)

Three questions (one message, user may answer all):

1. What surprised you?
2. What's one thing you'll never look at the same way?
3. Where will you use this tomorrow?

Optional homework: **3 everyday applications**, 5 minutes each, same framework — not "read chapter 4."

Write to artifact `## Reflection` and `## Next exploration`.

---

## Where heuristics fit

Heuristics are **optional deepeners after the core model lands** — not the session spine.

| When | Heuristic role |
| --- | --- |
| Framework design | Veda may use `DEC`, `ABS`, `ZOOM` **inline** while building the model — still teaching, not quizzing |
| After Practice | User picks or Veda suggests **one** code to stress-test a weak node |
| "Guide me" | Veda picks **one** heuristic that sharpens the weakest framework node — not a 4-heuristic chain |

**Delegation rule:** Invoke a specialist only when a single technique needs **extended** Teach-Model-Practice (see `teach-before-ask.md`). Pass the **core mental model** so the specialist extends it — does not replace it.

**Never:** SN → 5W → KD → RC as default Learn path without framework + examples + retrieval first.

---

## Mathematics and formal subjects

Order is always:

```text
Question → Intuition → Visualization → Formalism → Generalization
```

Formalism explains intuition the user already holds — it does not lead.

For math/stats topics: framework phase may include one carefully chosen formula **after** a visual or story that motivates it.

---

## Artifact sections (Learn template)

Session-first sections (fill in order):

1. `## Learning outcome`
2. `## Session log` (curiosity, prior model, reflection)
3. `## Core mental model`
4. `## Examples`
5. `## Retrieval`
6. `## Practice`
7. Heuristic sections (optional, after practice)
8. `## Summary` — one paragraph: the model they'll remember
9. `## Next exploration` — homework applications

Legacy heuristic buckets (Foundations, Patterns, …) remain for deep-dive sessions but are **not** the default Learn path.

---

## Veda vs specialist roles

| Role | Owns |
| --- | --- |
| **Veda** | Phases 1–7, framework, examples, retrieval, practice, reflection, artifact |
| **Specialist** | Optional deep-dive on one framework node via extended example + practice — see `teach-before-ask.md` |

---

## Restarting a stuck session

If user says "pause" or "this feels like quizzing":

1. Stop current heuristic chain
2. State learning outcome if missing
3. Resume at Phase 1 or 3 depending on what's already in artifact
4. Do not re-run calibration unless topic changed
