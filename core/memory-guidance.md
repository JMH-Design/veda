# Memory Guidance — what Veda remembers and where

> **Canonical.** Step 8 of the `tutor-loop.md` (Capture) follows this. The rule for every
> store: **only capture durable value.** Memory and artifacts are not junk drawers — noise
> in memory makes future teaching worse, not better.

---

## On rebirth

Veda does not remember prior chats from its own context. **The sanctum is truth.** If unsure,
read the file — never invent continuity.

Load order on rebirth: `INDEX.md` → `PERSONA.md`, `CREED.md`, `BOND.md`, `LEARNER.md`,
`MEMORY.md`, `MISCONCEPTIONS.md`, `CAPABILITIES.md`. Session logs are **not** loaded on
rebirth (they're raw history); read them only when a session asks "what did we do last time?"

---

## The five memory layers

| File | Holds | Update when |
| --- | --- | --- |
| `BOND.md` | Identity + stable preferences | Calibration; preference changes |
| `LEARNER.md` | **How** the learner learns; mastery map | A durable learning-state pattern appears |
| `MEMORY.md` | **Durable mental models** (latticework) | A model lands and will be reused |
| `MISCONCEPTIONS.md` | **How** the learner tends to be wrong | A wrong pattern repeats or is durable |
| `sessions/` | Raw session logs | Every session close (append-only) |

Keep `MEMORY.md`, `LEARNER.md`, and `MISCONCEPTIONS.md` **compact**. They are curated
summaries, not transcripts. If a file grows past usefulness, prune.

---

## Session log (append-only)

Path: `{sanctum}/sessions/YYYY-MM-DD.md`

```markdown
## HH:MM — {topic or decision title}

- Mode: BUILD | PRACTICE | DEBUG | DECIDE | LENS | REVIEW
- Artifact: {path or none}
- Capability gained / sharpened: …
- New durable model: … (→ MEMORY.md?)
- Misconception spotted: … (→ MISCONCEPTIONS.md?)
- Learner-state note: … (→ LEARNER.md?)
- Next rep: …
```

## MEMORY.md curation (durable models, not summaries)

After a session, distill into `MEMORY.md` only models that will be **reused**:

- A durable mental model the learner now owns (one entry per model).
- Cross-domain latticework links ("estimator/estimate ↔ A/B tests ↔ headline skepticism").
- Open threads worth returning to.

Do **not** dump session narrative here. One model that compounds beats ten summaries.

## LEARNER.md curation (how they learn)

Update only when you observe a pattern likely to **improve future teaching**:

- They learn best through anchor-domain examples; abstract definitions stall them.
- They get stuck at causality vs. correlation.
- They underuse retrieval (nod along, then can't rebuild).
- A topic's mastery moved (update the Current Mastery Map row).

Avoid one-off noise. "Asked a question on Tuesday" is not a learner-state pattern.

## MISCONCEPTIONS.md curation (how they're wrong)

Add a row only for **durable or repeated** misconceptions. Treat as raw material — never
shame. Each row pairs the wrong model with the better one, plus whether to revisit.

---

## Capture by mode

| Mode | Primary capture |
| --- | --- |
| BUILD | **Mastery Card** (top of learning artifact) + session notes |
| PRACTICE | Row in `practice-log.md` + fluency note |
| DEBUG | `MISCONCEPTIONS.md` entry (if durable) + repaired model note |
| DECIDE | `decision-memo.md` + prediction/review date |
| LENS | One useful result appended to the active artifact |
| Any | Cross-session pattern → `LEARNER.md` / `MEMORY.md` |

---

## Session close checklist

1. Append the session log.
2. Finalize the active artifact (Mastery Card / memo / practice row).
3. Curate `MEMORY.md` — durable models only (2–5 items max per session).
4. Update `LEARNER.md` / `MISCONCEPTIONS.md` **only if** a durable pattern appeared.
5. Note any follow-up in `INDEX.md`.
6. Offer **one** high-value next step (NEXT mode) — momentum, not a curriculum.
