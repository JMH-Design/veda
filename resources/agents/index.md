# Specialist agent roster

Veda 📖 is the **memory orchestrator**. Each heuristic has a **dedicated stateless specialist** with its own persona and skill.

Invoke directly: `veda-agent-first-principles`, `veda-agent-analogical-reasoning`, etc.  
Or ask Veda: "Run FP" / "Talk to Petra" → Veda routes to the specialist.

Full registry (source of truth): [`registry.yaml`](registry.yaml)

## Phase 1 — Foundations

| Code | Agent | Skill | Technique |
| --- | --- | --- | --- |
| `FP` | 🪨 Petra | `veda-agent-first-principles` | First Principles |
| `DEC` | 🧩 Modulus | `veda-agent-decomposition` | Decomposition |
| `KD` | 🎯 Pareto | `veda-agent-key-drivers` | Key Drivers |
| `SM` | 🗺️ Mapper | `veda-agent-structural-mapping` | Structural Mapping |
| `ZOOM` | 🔭 Zoom | `veda-agent-levels-of-abstraction` | Levels of Abstraction |

## Phase 2 — Patterns

| Code | Agent | Skill | Technique |
| --- | --- | --- | --- |
| `ANA` | 🌉 Anya | `veda-agent-analogical-reasoning` | Analogical Reasoning |
| `CHUNK` | 🧠 Chunk | `veda-agent-pattern-chunking` | Pattern Chunking |
| `ARCH` | ♻️ Arche | `veda-agent-systems-archetypes` | Systems Archetypes |
| `RC` | 📊 Clio | `veda-agent-reference-class` | Reference Class |
| `SN` | 📡 Sena | `veda-agent-signal-noise` | Signal vs Noise |

## Phase 3 — Framing

| Code | Agent | Skill | Technique |
| --- | --- | --- | --- |
| `INV` | 🔄 Iris | `veda-agent-inversion` | Inversion |
| `5W` | ❓ Wren | `veda-agent-five-whys` | Five Whys |
| `SOC` | 🏛️ Soph | `veda-agent-socratic-questioning` | Socratic Questioning |
| `REF` | 🖼️ Fern | `veda-agent-reframing` | Reframing |
| `CA` | 🔍 Ada | `veda-agent-challenging-assumptions` | Challenging Assumptions |

## Phase 4 — Synthesis

| Code | Agent | Skill | Technique |
| --- | --- | --- | --- |
| `LAT` | 🔗 Lia | `veda-agent-latticework` | Latticework *(updates Veda sanctum)* |
| `ABS` | ☁️ Aria | `veda-agent-abstraction` | Abstraction |
| `INT` | ⚖️ Integra | `veda-agent-integrative-thinking` | Integrative Thinking |
| `XPOL` | 🐝 Pax | `veda-agent-cross-pollination` | Cross-Pollination |
| `PERSP` | 👁️ Prism | `veda-agent-multiple-perspectives` | Multiple Perspectives |

## Phase 5 — Validation

| Code | Agent | Skill | Technique |
| --- | --- | --- | --- |
| `HYP` | 🧪 Hux | `veda-agent-hypothesis-testing` | Hypothesis Testing |
| `FB` | 💬 Faye | `veda-agent-seek-feedback` | Seek Feedback |
| `EVD` | 📐 Eva | `veda-agent-evidence-adjustment` | Evidence & Model Adjustment |
| `PRED` | 📅 Piper | `veda-agent-prediction-tracking` | Prediction Tracking |

## Architecture

```
User → Veda (memory, routing, latticework)
         ├─ LEARN / ANALYZE workflows
         └─ HEUR {code} → delegate to veda-agent-{slug}
                └─ Specialist (stateless, one technique)
                     └─ writes artifact → hand off to Veda
```

Regenerate skills after editing registry:

```bash
python scripts/generate-specialist-agents.py
```
