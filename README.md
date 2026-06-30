# Veda

A BMAD module built from the [User Manual](../user-manual.md).

**Veda** 📖 is a warm, rigorous, lightly funny **mentor** that teaches you to think. It models
your **learner state** — what you understand, misunderstand, and how you learn best — then
chooses the right teaching move.

> "I'm not here to think for you. I'm here to help you become the kind of person who can think
> through this yourself — and maybe enjoy it more than expected."

## Quick start

1. Install or copy this module into your BMAD project.
2. Invoke **`veda-agent`** (or say "Hey Veda").
3. On first meeting, Veda learns your name, voice, anchor domains, and how you like to think.
4. Each session: Veda **diagnoses what you need**, then runs the right mode.
5. Say **`INTRO`** anytime to see the modes + lens library in plain language.

## Modes — teaching moves

| Code | Use when you… | Produces | Was |
| --- | --- | --- | --- |
| `BUILD` | want to understand a topic | learning artifact (Mastery Card) | LEARN |
| `PRACTICE` | have a model, need reps | practice log | new |
| `DEBUG` | are confused / stuck / wrong | Misconception Ledger entry | new |
| `DECIDE` | face a choice or tradeoff | decision memo | ANALYZE |
| `LENS` | want one thinking lens | artifact deep-dive | HEUR |
| `NEXT` | ask what to do next | recommendation | HELP |
| `REVIEW` | want to revisit a model | updated mastery row | new |

Legacy codes (`LEARN`, `ANALYZE`, `HEUR`, `HELP`) still work.

## Architecture

```
Veda → Learner State → Tutor Loop → Mode → Practice / Feedback → Memory

Tutor Loop:  Diagnose → Orient → Model → Demonstrate → Retrieve → Transfer → Feedback → Capture
```

**Full system reference:** [`docs/system-overview.md`](docs/system-overview.md) ·
**Why it's shaped this way:** [`docs/architecture.md`](docs/architecture.md) ·
**v1→v2:** [`docs/migration-v2.md`](docs/migration-v2.md)

## Module layout

```txt
veda/
  module.yaml · config.toml
  core/        tutor-loop · lesson-structure · feedback-protocol · socratic-ladder · memory-guidance · voice
  modes/       build · practice · debug · decide · lens · next · review
  lenses/      registry.yaml (source of truth) · index.md · guides/
  agents/      veda.md · specialists/ (24 lens personas, generated)
  resources/   heuristics/ (technique content) · agents/ (legacy roster)
  skills/      veda-agent · veda-build/practice/debug/decide/lens/next · veda-agent-{slug} ×24
               (+ legacy aliases: veda-learn/analyze/heuristic/help)
  scripts/     generate-lens-agents.py
  templates/   learning-artifact · mastery-card · practice-log · decision-memo
  docs/        system-overview · architecture · getting-started · migration-v2
```

## Regenerate lenses

After editing `lenses/registry.yaml`:

```bash
python scripts/generate-lens-agents.py
```

## Source

Heuristics transcribed from source user manual (pages 2–6). Section 5 validation heuristics are inferred from the intro where the source was incomplete.
