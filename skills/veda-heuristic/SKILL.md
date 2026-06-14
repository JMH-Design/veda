---
name: veda-heuristic
description: >
  Route a thinking heuristic to its dedicated specialist agent (FP→Petra,
  ANA→Anya, RC→Clio, etc.). Veda's delegation workflow.
type: workflow
owner: veda
---

# veda-heuristic

## Overview

Resolve a heuristic **code** to its **dedicated specialist agent** and delegate. Each technique has its own stateless agent with a distinct persona. See `{module-root}/resources/agents/index.md`.

Specialists run **Teach-Before-Ask** (`{module-root}/references/teach-before-ask.md`) — not opening with Apply now recall questions.

## Input

- **Code** (required): e.g. `FP`, `ANA`, `RC`, `5W` — see `index.md`
- **Context** (required): topic, decision, or pasted text
- **Artifact path** (optional): defaults to active session file
- **Calibration** (optional): from `BOND.md` — anchor domains, topic familiarity, mental models

## Steps

1. Resolve code → specialist skill via `{module-root}/resources/agents/index.md` or `registry.yaml`.
2. Confirm delegation: "Routing to {icon} {name} ({title}) for {code}."
3. Pass context: topic, artifact path, calibration from `BOND.md`, prior session notes, planned sequence if any.
4. **Invoke specialist skill** (e.g. `veda-agent-first-principles`) — do not run heuristic inline.
5. Specialist delivers lens brief → insight probe → dialogue; writes artifact section and hands back to Veda on complete.

## Code → specialist map

| Phase | Codes → skills |
| --- | --- |
| 1 | `FP`→`veda-agent-first-principles` `DEC`→`veda-agent-decomposition` `KD`→`veda-agent-key-drivers` `SM`→`veda-agent-structural-mapping` `ZOOM`→`veda-agent-levels-of-abstraction` |
| 2 | `ANA`→`veda-agent-analogical-reasoning` `CHUNK`→`veda-agent-pattern-chunking` `ARCH`→`veda-agent-systems-archetypes` `RC`→`veda-agent-reference-class` `SN`→`veda-agent-signal-noise` |
| 3 | `INV`→`veda-agent-inversion` `5W`→`veda-agent-five-whys` `SOC`→`veda-agent-socratic-questioning` `REF`→`veda-agent-reframing` `CA`→`veda-agent-challenging-assumptions` |
| 4 | `LAT`→`veda-agent-latticework` `ABS`→`veda-agent-abstraction` `INT`→`veda-agent-integrative-thinking` `XPOL`→`veda-agent-cross-pollination` `PERSP`→`veda-agent-multiple-perspectives` |
| 5 | `HYP`→`veda-agent-hypothesis-testing` `FB`→`veda-agent-seek-feedback` `EVD`→`veda-agent-evidence-adjustment` `PRED`→`veda-agent-prediction-tracking` |

Invalid code → show roster from `resources/agents/index.md`, ask again.

## Output

Specialist-owned artifact section (Lens brief, Insight probe, Dialogue, Insights). User returns to Veda for next routing.

## Fallback

If specialist skill unavailable, load heuristic from `resources/heuristics/` and apply per `references/specialist-protocol.md` + `references/teach-before-ask.md` — then note degradation in chat.
