---
name: veda-lens
description: >
  Apply one thinking lens to deepen a model or decision (Teach → Model → Practice). Resolves a
  lens code to its stateless specialist. The redesign's LENS mode — formerly HEUR.
type: workflow
owner: veda
---

# veda-lens — LENS mode

Apply **one** thinking lens. The learner experiences a *thinking move at the right time*, not a
roster of characters. Powered internally by a stateless specialist (`veda-agent-{slug}`).

**Mode spec:** `{module-root}/modes/lens.md`
**Lens Library:** `{module-root}/lenses/index.md` (code → lens map, five groups)

## Input

- **Code or named lens** (required): e.g. `RC`, `INV`, `SN`, "reference class"
- **Context** (required): topic, decision, or pasted text
- **Artifact path** (optional): the active session file
- **Core model** (passed in BUILD/DECIDE): the framework node to deepen

## Steps

1. Resolve the code → lens via `{module-root}/lenses/index.md` (or `lenses/registry.yaml`).
2. Confirm briefly: "Let's bring in {lens} to sharpen {node}." (Persona optional, light.)
3. Pass context: topic, artifact path, `BOND.md`/`LEARNER.md` calibration, `# Mastery Card`/`## Core Model`.
4. **Invoke** `veda-agent-{slug}` — it runs **Teach → Model → Practice**
   (`{module-root}/modes/lens.md`): Motivate → Intuition → Tiny model → **Worked example** →
   Apply → Capture. Never quiz-first; never a default chain.
5. Specialist appends the **compact result** to the artifact and hands back to Veda.

## Rules

- A LENS must not hijack BUILD — it runs after the framework lands, on the weakest node.
- Write back the useful result, not the teaching transcript.
- Invalid code → show `{module-root}/lenses/index.md`, ask again.

## Fallback

If the specialist skill is unavailable, load the technique from `resources/heuristics/` and run
Teach → Model → Practice per `references/specialist-protocol.md` — note the degradation in chat.
