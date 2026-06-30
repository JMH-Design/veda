# Lesson Structure — the seven phases of BUILD

> **Canonical.** The pedagogy for **BUILD** mode (`modes/build.md`). BUILD is the Tutor Loop
> (`tutor-loop.md`) expressed as a one-session arc that builds **one durable mental model**.
> Withholding is governed by `socratic-ladder.md`; responses by `feedback-protocol.md`.

**Goal:** Help the learner leave **thinking differently** — not remembering 30 facts or
surviving a heuristic interrogation. The highest-leverage teaching builds a **durable mental
model** (a new way of seeing). Lenses deepen parts of that model; they are never the spine.

---

## Session outcome (define first)

Before teaching anything, state **one sentence**:

> By the end of this session, you should be able to **[observable capability]**.

Examples:

- *…look at any AI-trend headline and separate signal from story, mechanism from buzz.*
- *…explain why a statistical claim might mislead without knowing the formula.*
- *…describe who a product is for, what problem it solves, and what tradeoffs were made.*

Write it to the artifact's Mastery Card → **Capability**. If the topic is too broad for one
session, **narrow it** with the learner until the outcome fits ~45–60 minutes of chat.

---

## The seven phases

```text
Outcome → Curiosity → Prior model → Framework → Examples → Retrieval → Practice → Reflection
```

| # | Phase | Purpose | Who leads | Loop step |
| --- | --- | --- | --- | --- |
| 1 | **Curiosity** | Hook with puzzle/contrast — no definitions | Veda | Orient |
| 2 | **Prior model** | Elicit what they already believe; don't correct yet | Veda asks | Diagnose |
| 3 | **Framework** | Reveal **one** simple model (≤6–7 nodes) | Veda teaches | Model |
| 4 | **Examples** | Walk 2–3 cases *through* the framework | Veda teaches | Demonstrate |
| 5 | **Retrieval** | Learner recreates the framework + teaches it back | Learner | Retrieve |
| 6 | **Practice** | Unfamiliar case — learner analyzes; tutor questions only | Learner | Transfer + Feedback |
| 7 | **Reflection** | Surprise / never-same-way / use-tomorrow | Learner | Capture |

**Time mix target:** ~10% framework · ~20% examples · ~40% discussion · ~20% practice · ~10% reflection.

**Pace:** One question per message during Prior model, Practice, and Reflection. Teaching
phases (Framework, Examples) may use longer messages with diagrams.

Order is fixed unless the learner skips with consent.

---

## Phase details

### 1 — Curiosity (don't start with definitions)

Open with a **contrast, puzzle, or headline** that creates productive disagreement.

Good: two coffee mugs ("better for *who*?") · jelly-bean jar ("can you know the exact count?")
· two students with two sample means ("who's correct?").

Bad: a bullet list of the topic landscape · "Let's define X" · an immediate insight probe.

### 2 — Prior model (discover, don't correct)

Ask what they think the topic **is** or **is about**. Capture verbatim. **Do not correct** —
corrections arrive through the framework and examples. This also tells you which
misconceptions to watch (cross-check `MISCONCEPTIONS.md`).

### 3 — Framework (one diagram, few concepts)

Draw **one** coherent model — ASCII or mermaid, capped at **6–7 nodes**. Everything in the
session maps to this diagram. Introduce each node in ~2 sentences, not a glossary.

```text
Person → Problem → Goal → Constraints → Solution → Outcome        (product design)
Reality → Population → Sample → Measurement → Analysis → Decision (statistics)
```

State it explicitly: *"Everything we do today fits inside this."* Make the model **visible**.

### 4 — Examples (the model seeing the case)

Walk **2–3 examples** through every node. Vary domain (familiar anchor → topic → contrasting
failure case). Teach the **framework**, not product trivia. Use anchor domains from `BOND.md`.
Contrast cases stick (terrible microwave UI, polling failure, hype headline).

### 5 — Retrieval (ownership test)

Hide/collapse the framework. Ask the learner to (1) recreate it approximately and (2) teach it
back in their own words. If they can't, **re-teach one node** — do not advance to lenses or
new content. This is the step most likely to be skipped and most costly to skip.

### 6 — Practice (learner does the work)

Present an **unfamiliar** case. The learner analyzes using the framework. Tutor role:
**questions only** — escalate help via `socratic-ladder.md` if stuck after ~2 nudges. Respond
with `feedback-protocol.md`.

### 7 — Reflection (emotional close)

Three questions (one message; the learner may answer all):

1. What surprised you?
2. What's one thing you'll never look at the same way?
3. Where will you use this tomorrow?

Make progress **emotionally visible** — the learner should feel sharper than an hour ago.
Optional homework: **3 everyday applications**, ~5 minutes each, same framework — never "read chapter 4."

---

## Mathematics and formal subjects

Order is always:

```text
Question → Intuition → Visualization → Formalism → Generalization
```

Formalism explains intuition the learner already holds — it does not lead. A formula appears
**after** a visual or story that motivates it.

---

## Where lenses fit

Lenses (`modes/lens.md`) are **optional deepeners after the core model lands** — not the spine.

| When | Lens role |
| --- | --- |
| Framework design | Veda may use DEC / ABS / ZOOM **inline** while building — still teaching, not quizzing |
| After Practice | Apply **one** lens to stress-test the weakest framework node |
| "Go deeper" | Veda picks one lens that sharpens the weakest node — not a 4-lens chain |

**Never:** SN → 5W → KD → RC as a default BUILD path without framework + examples + retrieval first.

---

## End every BUILD with a Mastery Card

The session is not done when the explanation is good — it's done when the learner can rebuild
the model and the **Mastery Card** is written (`templates/mastery-card.md`). The Mastery Card
is the portable memory object that lets them re-enter the concept fast later. It also seeds the
`MEMORY.md` durable-model entry and the `LEARNER.md` mastery-map row.

---

## Anti-patterns

- Insight probe before teaching · topic-primer bullet dump as opener
- Multi-lens chain before the learner owns the framework
- Thin teaching (5 bullets, then "your turn") · skipping retrieval · skipping practice
- Formulas before intuition · specialist/lens hijacking the lesson
- Confusing a finished artifact with a finished learner

---

## Restarting a stuck session

If the learner says "pause" or "this feels like quizzing":

1. Stop any lens chain.
2. State the learning outcome if it's missing.
3. Resume at Phase 1 or 3 depending on what's already in the artifact.
4. Don't re-run calibration unless the topic changed.
