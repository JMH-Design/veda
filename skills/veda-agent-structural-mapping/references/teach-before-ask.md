# Teach-Before-Ask — specialist learning protocol

Used by all `veda-agent-*` specialists in **Learn** mode (and when user is exploring a topic). Replaces opening with raw **Apply now** recall questions.

**Load with:** `{module-root}/resources/heuristics/_lens-guides.md` for technique-specific teaching anchors.

---

## Flow

```text
Lens brief → Insight probe → Dialogue (adaptive) → Write artifact → Hand off
```

| Phase | What | Rules |
| --- | --- | --- |
| **Lens brief** | Teach topic through this technique's lens | Before any question |
| **Insight probe** | One non-obvious question | Not answerable from the brief |
| **Dialogue** | Follow-ups from Apply now **pool** | Only where the answer left gaps |
| **Artifact** | Persist brief, probe, dialogue, insights | Per specialist-protocol |

**Pace:** Lens brief + insight probe may share one message. Dialogue stays one question at a time.

---

## Lens brief

**Purpose:** Give the user shared context so questions test *thinking*, not *missing background*.

**Format:** Max 5 bullets or ~120 words.

**Must include:**

1. Technique in one line (from heuristic definition)
2. Two to four **topic-specific** facts seen through this lens
3. One tie to user's **anchor domains** from `BOND.md` → `## Calibration` (if present)

**Must not include:**

- The answer to the insight probe
- Verbatim copy of all three Apply now questions

**Calibrate length by topic familiarity** (`BOND.md` → `Topic familiarity`):

| Familiarity | Brief |
| --- | --- |
| Brand new | Longer — define terms, one concrete example |
| Some exposure | Medium — assume basic vocabulary |
| Comfortable | Short — sharp facts only |
| Practitioner | Minimal — one to two non-obvious facts they'd overlook |

**Familiarity never skips the brief** — it only shortens it.

---

## Insight probe

**Purpose:** Start the thinking phase. User must synthesize, judge, or apply — not repeat the brief.

**Rules:**

- Exactly **one** question at session start (per technique)
- Must require judgment beyond the brief (not recall)
- Do **not** use Apply now question #1 verbatim as the probe
- Draw probe *style* from `_lens-guides.md` → `Good insight probes`; instantiate for topic

**Calibrate difficulty by familiarity:**

| Familiarity | Probe |
| --- | --- |
| Brand new | Scaffolded — name a tradeoff or pick between two classes |
| Some exposure | Apply lens to their specific topic |
| Comfortable | Edge case, falsifier, or "which comparable misleads you?" |
| Practitioner | Stress-test or steelman the weakest part of their model |

---

## Dialogue (adaptive follow-ups)

After the user answers the insight probe:

1. **Affirm** what was strong; **push back** on vagueness (per voice and persona).
2. Check Apply now **pool** in heuristic file — ask a follow-up **only** if a dimension is missing or thin.
3. Do **not** march through all three Apply now questions by default.
4. One question at a time. Stop when the lens feels sufficiently explored (typically 0–2 follow-ups).

**Apply now pool** = the numbered questions under **Apply now — ask:** in the heuristic file. Use as ammunition, not a script.

---

## Artifact format

Append or update in `{understanding_artifacts}/{topic}.md`:

```markdown
## {Heuristic Name}

*{one-line definition}*

### Lens brief

- ...

### Insight probe

> {question asked}

### Dialogue

- **User:** ...
- **{Specialist}:** ...

### Insights

- ...

### Open questions

- ...
```

---

## Worked example — RC on AI product architecture

**Context:** Jared · Comfortable · Anchors: product/UX design, marathon running · Voice: Sparring Partner

### Lens brief (Clio)

- **Reference class** grounds you in what *usually* happens in comparable cases — not what makes yours special.
- AI product architecture today is mostly a **platform-shift hybrid**: deterministic software core + probabilistic LLM layer — closer to cloud/API adoption than greenfield AI-native apps.
- Base rates that matter: unit economics (tokens vs. value), trust (deterministic/probabilistic boundary), and whether the feature delivers enough user value to survive deprecation.
- *Your UX lens:* architecture choices are trust affordances — like race-day conditions you can't control but must pace around.

### Insight probe

> Consumer AI apps and dev tools like Claude Code don't share the same base rates. **Which class of comparable products is most likely to mislead you** if you copy its success pattern — and why?

*(Not: "What broad class does this belong to?" — that's recall, covered in the brief.)*

### Dialogue (adaptive)

- User answers with dev-tool vs. consumer gap → affirm, one follow-up from pool: *"What's the base rate you implicit assume for profitability — and what would falsify it?"*
- Skip "why might this case differ" if already covered in probe answer.

---

## Topic primer (veda-learn only)

Before the **first** heuristic in a Learn session, Veda (not the specialist) may deliver a **topic primer**:

- Three to four bullets: topic landscape (not technique-specific)
- End with: *"We'll start with {code} — {name} will teach through that lens."*
- **Skip** if user supplied source material (URL, doc, paste) — use their material instead
- **Skip** on second+ heuristic in the same session (specialist lens brief covers it)

See `veda-learn` step 2.5.

---

## Delegation context

When Veda routes via `veda-heuristic`, pass:

- Topic + artifact path
- `BOND.md` → Calibration (anchors, familiarity, mental models)
- `PERSONA.md` → Voice (Veda's voice; specialist keeps own persona)
- Planned technique sequence if any

Specialist: read calibration → lens brief → probe → dialogue. Do not re-ask topic if already provided.
