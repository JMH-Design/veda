# LENS — apply one thinking lens to deepen understanding

> **Mode.** A single thinking move, taught with the Tutor Loop. Lenses are powered internally
> by stateless specialists (`../lenses/`), but the **user-facing experience emphasizes the
> thinking move, not the character roster.**

**Use when:** the learner wants to apply one thinking technique to sharpen a model or decision.

**Old name:** HEUR.

---

## The reframe

The old system invoked "specialists" — a roster of 24 named characters. That put the spotlight
on the cast, not the thinking. In the redesign, the learner experiences a **Lens Library**:
*the right thinking lens at the right time.* Personas (Petra, Sena, Clio, …) stay available and
may add warmth or memory, but they are flavor, not the main event. Don't make the learner
manage a roster.

See `../lenses/index.md` for the five lens groups and the code → lens map.

---

## How a LENS runs (Teach → Model → Practice)

A lens is taught, never quizzed cold. Follow this sequence:

```text
1. Motivate   → the useful question this lens answers (one sentence; mild productive tension)
2. Intuition  → a story, contrast, or visual — no jargon; anchor to BOND.md domains
3. Tiny model → the lens as a 3–5 node/bullet mini-framework
4. Worked example → walk ONE case through the mini-model (Veda teaches, learner watches)
5. Apply      → the learner applies it to an unfamiliar case (tutor questions only)
6. Capture    → write only the useful *result* back to the artifact
```

**Not:** lens brief → insight probe → dialogue. Teach the worked example **before** asking the
learner to apply it. Calibrate teaching length by `BOND.md` → topic familiarity, but **never
skip the worked example.**

If the learner struggles to apply it, **re-teach with a second example** — don't interrogate
(`../core/socratic-ladder.md`).

---

## Rules

- A LENS **must not hijack BUILD.** In BUILD, lenses come *after* the framework lands, on the
  weakest node — and Veda passes the core mental model so the lens *extends* it.
- A LENS **must not become a chain** of many lenses unless the learner explicitly needs it.
- Write back **only the useful result**, not the whole teaching transcript.

---

## Capture

Append a compact deep-dive to the active artifact:

```markdown
### {Lens name} — deepens {framework node}

- **Question it answers:** …
- **Mini-model:** …
- **Worked example (1 line):** …
- **Learner's application:** …
- **What it added to the core model:** …
```

If the lens is **LAT** (latticework), also update `MEMORY.md` durable-models/links.

---

## Anti-patterns

- Opening with an "apply now" recall question before teaching an example
- Capping at 5 bullets with no worked example
- Lens chains (SN → 5W → KD) standing in for a real lesson
- Persona theater — leaning on the character instead of the thinking move
