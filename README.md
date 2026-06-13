# Veda

A BMAD module built from the [User Manual](../user-manual.md).

**Veda** 📖 is your memory orchestrator — she remembers your latticework and routes you to the right workflow or specialist.

**24 heuristic specialists** each own one thinking technique (Petra for first principles, Anya for analogies, Clio for reference classes, …).

## Quick start

1. Install or copy this module into your BMAD project.
2. Invoke **`veda-agent`** (or say "Hey Veda").
3. On first meeting, Veda runs **First Breath** — learns your name, interests, and how you like to think.
4. Each session: Veda **welcomes you**, asks your **goal**, and on first meeting shows the **skills catalog**.
5. Say **`INTRO`** anytime to see workflows + specialists in plain language.

## Invoke a specialist directly

| Say | Routes to |
| --- | --- |
| "Run FP" / "Talk to Petra" | `veda-agent-first-principles` 🪨 |
| "Run ANA" / "Talk to Anya" | `veda-agent-analogical-reasoning` 🌉 |
| "Run RC" / "Talk to Clio" | `veda-agent-reference-class` 📊 |
| Full roster | [`resources/agents/index.md`](resources/agents/index.md) |

## What you get

| Skill | Code | Produces |
| --- | --- | --- |
| Veda (orchestrator) | — | Memory, routing, latticework |
| Learn workflow | `LEARN` | `docs/understanding/{topic}.md` (Learning Notes) |
| Analyze workflow | `ANALYZE` | `docs/understanding/{topic}.md` (Decision Memo) |
| Heuristic routing | `HEUR` + code | Delegates to specialist agent |
| 24 specialists | `veda-agent-{slug}` | Focused technique sessions |
| Help / routing | `HELP` | Recommends next specialist or workflow |

## Architecture

```
Veda (memory orchestrator)
  ├─ LEARN / ANALYZE workflows
  └─ HEUR {code} → veda-agent-{slug} (stateless specialist)
       └─ writes artifact → hand off back to Veda
```

## Module layout

```txt
veda/
  module.yaml
  config.toml
  agents/
    veda.md                 memory orchestrator
    specialists/            24 heuristic personas (generated)
  resources/
    agents/
      registry.yaml         source of truth for specialists
      index.md              roster table
    heuristics/             technique reference content
  skills/
    veda-agent/        Veda launcher + sanctum
    veda-agent-{slug}/        24 specialist launchers (generated)
    veda-learn/ veda-analyze/ veda-heuristic/ veda-help/
  scripts/
    generate-specialist-agents.py
  templates/
  docs/getting-started.md
```

## Regenerate specialists

After editing `resources/agents/registry.yaml`:

```bash
python scripts/generate-specialist-agents.py
```

## Source

Heuristics transcribed from source user manual (pages 2–6). Section 5 validation heuristics are inferred from the intro where the source was incomplete.
