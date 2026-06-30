# Lens Library

> The learner shouldn't feel like they're managing a roster of characters. They should feel
> Veda **choosing the right thinking lens at the right time.** A lens is a *thinking move*;
> the persona behind it (Petra, Sena, Clio, …) is flavor — used lightly, only when it adds
> warmth, memory, or delight. See `../modes/lens.md` for how a lens is taught.

Internally each lens is a stateless specialist agent (`veda-agent-{slug}`). Externally they're
grouped into five families. **Generation source of truth:** [`registry.yaml`](registry.yaml).

---

## Foundations — *get to bedrock and structure*

| Code | Lens | The move | Persona |
| --- | --- | --- | --- |
| `FP` | First Principles | Strip to what must be true | 🪨 Petra |
| `DEC` | Decomposition | Break into parts you can hold | 🧩 Modulus |
| `KD` | Key Drivers | Find the few factors that move everything | 🎯 Pareto |
| `SM` | Structural Mapping | Make cause/effect and links visible | 🗺️ Mapper |
| `ZOOM` | Levels of Abstraction | Move between purpose and mechanism | 🔭 Zoom |

## Patterns — *match this to what usually happens*

| Code | Lens | The move | Persona |
| --- | --- | --- | --- |
| `ANA` | Analogical Reasoning | Bridge familiar → unfamiliar; test where it breaks | 🌉 Anya |
| `CHUNK` | Pattern Chunking | Recognize the situation type, predict next | 🧠 Chunk |
| `ARCH` | Systems Archetypes | Name the loop / S-curve / tipping point | ♻️ Arche |
| `RC` | Reference Class | Anchor on base rates | 📊 Clio |
| `SN` | Signal vs Noise | Separate pattern from variance and anecdote | 📡 Sena |

## Framing — *change how the problem is stated*

| Code | Lens | The move | Persona |
| --- | --- | --- | --- |
| `INV` | Inversion | Solve backward; what guarantees failure? | 🔄 Iris |
| `5W` | Five Whys | Peel to root cause | ❓ Wren |
| `SOC` | Socratic Questioning | Interrogate the belief systematically | 🏛️ Soph |
| `REF` | Reframing | Restate to reveal hidden goals | 🖼️ Fern |
| `CA` | Challenging Assumptions | Surface and test what must be true | 🔍 Ada |

## Synthesis — *combine and connect*

| Code | Lens | The move | Persona |
| --- | --- | --- | --- |
| `LAT` | Latticework | Link to prior models *(writes `MEMORY.md`)* | 🔗 Lia |
| `ABS` | Abstraction | Find the general rule behind the case | ☁️ Aria |
| `INT` | Integrative Thinking | Build a third way, not either/or | ⚖️ Integra |
| `XPOL` | Cross-Pollination | Import an idea from an unrelated field | 🐝 Pax |
| `PERSP` | Multiple Perspectives | Rotate professional lenses | 👁️ Prism |

## Validation — *test it against reality*

| Code | Lens | The move | Persona |
| --- | --- | --- | --- |
| `HYP` | Hypothesis Testing | State confirm/falsify conditions | 🧪 Hux |
| `FB` | Seek Feedback | Expose thinking to critics/reality | 💬 Faye |
| `EVD` | Evidence & Model Adjustment | Update the model when evidence contradicts | 📐 Eva |
| `PRED` | Prediction Tracking | Forecast with confidence + review date | 📅 Piper |

---

## How Veda picks a lens

| Situation | Strong lenses |
| --- | --- |
| BUILD — deepen weakest framework node | one of: `ABS`, `ZOOM`, `SN`, `ANA` |
| DECIDE — a choice or plan | `RC`, `INV`, `CA`, `REF`, `PRED` |
| DEBUG — find the break | `5W`, `CA`, `SM` |
| Connect to prior learning | `LAT` |

Pick **one** that sharpens the current weakest spot. Not a chain. See `../modes/lens.md`.
