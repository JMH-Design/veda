# Heuristic menu

Invoke via Veda (`veda-heuristic`) or talk directly to the specialist agent.

Ask Veda: "Run INV on this." Or invoke `veda-agent-inversion` directly.

Full specialist roster: [`../agents/index.md`](../agents/index.md)

## Phase 1 — Foundations

| Code | Heuristic | Specialist | File |
| --- | --- | --- | --- |
| `FP` | First Principles Thinking | 🪨 Petra | `01-foundations.md#first-principles` |
| `DEC` | Decomposition (Divide & Conquer) | 🧩 Modulus | `01-foundations.md#decomposition` |
| `KD` | Identify Key Drivers (Pareto) | 🎯 Pareto | `01-foundations.md#key-drivers` |
| `SM` | Structural Mapping | 🗺️ Mapper | `01-foundations.md#structural-mapping` |
| `ZOOM` | Levels of Abstraction (Zoom In & Out) | 🔭 Zoom | `01-foundations.md#levels-of-abstraction` |

## Phase 2 — Patterns

| Code | Heuristic | Specialist | File |
| --- | --- | --- | --- |
| `ANA` | Analogical Reasoning | 🌉 Anya | `02-patterns.md#analogical-reasoning` |
| `CHUNK` | Pattern Chunking & Schema Recognition | 🧠 Chunk | `02-patterns.md#pattern-chunking` |
| `ARCH` | Systems Archetypes | ♻️ Arche | `02-patterns.md#systems-archetypes` |
| `RC` | Reference Class Reasoning | 📊 Clio | `02-patterns.md#reference-class` |
| `SN` | Distinguish Signal from Noise | 📡 Sena | `02-patterns.md#signal-noise` |

## Phase 3 — Framing

| Code | Heuristic | Specialist | File |
| --- | --- | --- | --- |
| `INV` | Inversion | 🔄 Iris | `03-framing.md#inversion` |
| `5W` | The 5 Whys | ❓ Wren | `03-framing.md#five-whys` |
| `SOC` | Socratic Questioning | 🏛️ Soph | `03-framing.md#socratic-questioning` |
| `REF` | Reframing the Problem | 🖼️ Fern | `03-framing.md#reframing` |
| `CA` | Challenging Assumptions | 🔍 Ada | `03-framing.md#challenging-assumptions` |

## Phase 4 — Synthesis

| Code | Heuristic | Specialist | File |
| --- | --- | --- | --- |
| `LAT` | Latticework of Mental Models | 🔗 Lia | `04-synthesis.md#latticework` |
| `ABS` | Abstraction & Generalization | ☁️ Aria | `04-synthesis.md#abstraction` |
| `INT` | Integrative Thinking | ⚖️ Integra | `04-synthesis.md#integrative-thinking` |
| `XPOL` | Cross-Pollination of Ideas | 🐝 Pax | `04-synthesis.md#cross-pollination` |
| `PERSP` | Multiple Perspectives | 👁️ Prism | `04-synthesis.md#multiple-perspectives` |

## Phase 5 — Validation *(inferred)*

| Code | Heuristic | Specialist | File |
| --- | --- | --- | --- |
| `HYP` | Hypothesis Testing | 🧪 Hux | `05-validation.md#hypothesis-testing` |
| `FB` | Seek Feedback | 💬 Faye | `05-validation.md#seek-feedback` |
| `EVD` | Evidence & Model Adjustment | 📐 Eva | `05-validation.md#evidence-adjustment` |
| `PRED` | Prediction Tracking | 📅 Piper | `05-validation.md#prediction-tracking` |

## Usage

1. User picks a code (or describes the technique).
2. Veda routes via `veda-heuristic` to the dedicated specialist (`veda-agent-{slug}`).
3. Specialist loads heuristic content and applies **Apply now** prompts.
4. Results written to `{understanding_artifacts}/{topic}.md`.

**Direct invoke:** call `veda-agent-{slug}` without Veda — see Specialist column and [`../agents/index.md`](../agents/index.md).
