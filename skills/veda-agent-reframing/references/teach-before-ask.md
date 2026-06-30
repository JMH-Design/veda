# Teach → Model → Practice — lens teaching protocol

> **Canonical home:** `{module-root}/modes/lens.md`. This file is the detailed plumbing the
> generated `veda-agent-*` lens skills follow. Withholding: `{module-root}/core/socratic-ladder.md`.
> Feedback: `{module-root}/core/feedback-protocol.md`.

Used by `veda-agent-*` specialists (lenses) when **delegated after the core framework lands**
(BUILD) or for **standalone LENS sessions**.

**Primary BUILD pedagogy:** `{module-root}/core/lesson-structure.md` — Veda owns the
seven-phase lesson; a lens extends one node.

**Load with:** `{module-root}/resources/heuristics/_lens-guides.md`

---

## When to use this protocol

| Situation | Protocol |
| --- | --- |
| Normal **veda-learn** session | Follow `lesson-structure.md` first. Delegate specialist **only after Practice** (phase 6) or for explicit `HEUR` request |
| Standalone **HEUR** ("Run FP on X") | Full Teach-Model-Practice below |
| **veda-analyze** | Original probe-first flow ok — decisions need interrogation |

---

## Teach-Model-Practice (replaces probe-first)

```text
Motivating question → Intuition → Mini-model → Worked example → User application → (optional) formalism
```

**Not:** Lens brief → insight probe → dialogue.

| Phase | What | Rules |
| --- | --- | --- |
| **Motivating question** | The problem this technique exists to solve | One sentence; creates mild confusion |
| **Intuition** | Story, contrast, or visual — no jargon | Anchor domains from `BOND.md` |
| **Mini-model** | Technique as 3–5 bullet framework | Topic-specific; ties to parent mental model if passed |
| **Worked example** | Walk one case through the mini-model | Veda/specialist **teaches** — user watches |
| **User application** | One unfamiliar case — user tries first | Tutor questions only; max 2 nudges before hint |
| **Formalism** *(optional)* | Vocabulary, heuristic definition, formula | Only after intuition lands |

**Pace:** Phases 1–4 may share 1–2 messages. User application: one question at a time.

---

## Lens brief (redefined)

**Purpose:** Teach the technique's **mini-model**, not prep for a quiz.

**Format:** ~150–250 words OR structured mini-model + one worked example sketch.

**Must include:**

1. Motivating question this technique answers
2. Mini-model (3–5 nodes or bullets)
3. One **worked example** through the model (even abbreviated)
4. Tie to anchor domains from `BOND.md`
5. Link to the parent **core model** (Mastery Card → `## Core Model`) when Veda passed one

**Must not:**

- End with an insight probe before teaching an example
- Cap at 5 bullets with no example walkthrough
- Use Apply now questions verbatim as the opening move

**Calibrate length** by `BOND.md` → Topic familiarity — longer teaching for brand new, shorter for practitioner — but **never skip worked example**.

---

## Insight probe (repositioned)

**Only after** worked example. Purpose: user **applies** the mini-model, not discovers missing background.

Rules:

- One question
- Requires using the mini-model on a **new** case
- Not recall of the brief

If user struggles, **re-teach with a second example** — do not interrogate.

---

## Dialogue (adaptive)

After user application:

1. Affirm what they used correctly from the model
2. One follow-up from Apply now **pool** only if a dimension is missing
3. Stop after 0–2 follow-ups
4. If vague: offer a hint framed as model node — not "try harder"

---

## Artifact format

When specialist writes to artifact:

```markdown
### {Heuristic Name} *(deep-dive)*

*{one-line definition}*

#### Motivating question

...

#### Mini-model

...

#### Worked example

...

#### Your application

- **Prompt:** ...
- **User:** ...
- **{Specialist}:** ...

#### Insights

- ...
```

---

## Topic primer (veda-learn — Veda only)

**Deprecated as bullet landscape.** Replace with Phase 1 **Curiosity hook** per `lesson-structure.md`.

Old primer bullets are only ok **inside** the framework phase as supporting context — never as session opener.

---

## Delegation context

When Veda routes via `veda-heuristic`, pass:

- Topic + artifact path
- `# Mastery Card` / `## Core Model` from artifact (required if exists)
- `BOND.md` → Calibration
- Which framework **node** to deepen

Specialist: extend that node — do not restart topic from zero.

---

## Worked example — SN after core lesson

**Context:** AI trends session · Core model: Story → Mechanism → Evidence → Incentive → Deployment → Durability

**Motivating question (Sena):** *"Why do smart people build elaborate theories from one viral demo?"*

**Intuition:** Hermes week — everyone talking. Story layer explodes. Mechanism layer (local + recursive learning) may be real but is buried in noise.

**Mini-model (signal check):**

```text
Claim → Sample size → Incentive of teller → Deployment proof → Repeat across orgs
```

**Worked example:** "87% of dentists recommend…" — walk all five nodes.

**User application:** Pick one AI headline from this week. Run the five-node check. Which node fails first?

*(Not: "Which trend are you overweighting?" before teaching the check.)*
