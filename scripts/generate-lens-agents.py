#!/usr/bin/env python3
"""Generate lens specialist personas and skill folders from lenses/registry.yaml.

Each lens in the Lens Library (lenses/index.md) is implemented as a stateless specialist
agent. This script regenerates their persona files (agents/specialists/) and skill launchers
(skills/veda-agent-{slug}/) from the single source of truth.

Usage (from veda/):
    python scripts/generate-lens-agents.py
"""

from __future__ import annotations

import textwrap
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "lenses/registry.yaml"
SPECIALISTS_DIR = ROOT / "agents/specialists"
SKILLS_DIR = ROOT / "skills"
PROTOCOL_SRC = ROOT / "references/specialist-protocol.md"
TEACH_SRC = ROOT / "references/teach-before-ask.md"

GEN_BANNER = "<!-- GENERATED FROM lenses/registry.yaml by scripts/generate-lens-agents.py. DO NOT EDIT DIRECTLY. -->"


def load_registry() -> list[dict]:
    data = yaml.safe_load(REGISTRY.read_text())
    return data["specialists"]


def persona_md(entry: dict) -> str:
    code = entry["code"]
    agent_code = code.lower() if code != "5W" else "five-whys"
    return textwrap.dedent(
        f"""\
        # {entry['name']} — {entry['title']}

        {GEN_BANNER}

        ```yaml
        agent:
          code: {agent_code}
          name: {entry['name']}
          title: {entry['title']}
          icon: "{entry['icon']}"
          team: understanding
          phase: {entry['phase']}
          archetype: stateless
          heuristic_code: {code}
          skill: veda-agent-{entry['slug']}
          role: >
            {entry['role'].strip()}
          communication_style: >
            {entry['style'].strip()}
          principles:
            - Own exactly one lens: {code} ({entry['slug'].replace('-', ' ')}).
            - Teach -> Model -> Practice: motivate, intuition, tiny model, WORKED EXAMPLE, then the learner applies it.
            - Never quiz-first. Withhold by core/socratic-ladder.md; respond by core/feedback-protocol.md.
            - Extend the learner's core model (Mastery Card) — do not restart the topic.
            - Emphasize the thinking move, not the persona. Write the useful result; hand off to Veda.
            - Never fake memory — stateless rebirth each session.
        ```

        ## Lens

        Group: **{entry['phase']}** · Library: `{{module-root}}/lenses/index.md`
        Technique source: `{{module-root}}/resources/heuristics/{entry['heuristic_file']}#{entry['anchor']}`

        ## When to invoke

        - The learner wants **{entry['title'].replace(' Guide', '')}** applied to a topic or decision
        - Veda brings in this lens via `LENS` (`veda-lens`) with code `{code}`
        - Mid-BUILD/DECIDE when the learner picks `{code}` to deepen the weakest node

        ## Handoff

        On complete → summarize what the lens added; hand back to `veda-agent` (Veda) for the next move.
        """
    )


def skill_md(entry: dict) -> str:
    slug = entry["slug"]
    code = entry["code"]
    agent_code = code.lower() if code != "5W" else "five-whys"
    updates = entry.get("updates_sanctum", False)
    sanctum_note = (
        "\n10. **Sanctum:** Update `_bmad/sanctum/veda/MEMORY.md` durable-models/links (keep it compact)."
        if updates
        else ""
    )

    return textwrap.dedent(
        f"""\
        ---
        name: veda-agent-{slug}
        description: >
          {entry['icon']} {entry['name']} — {entry['title']}. Stateless specialist powering the
          {code} lens. Apply {entry['slug'].replace('-', ' ')} to any topic.
        type: agent
        agent_code: {agent_code}
        archetype: stateless
        heuristic_code: {code}
        owner: veda
        ---

        # veda-agent-{slug}

        {GEN_BANNER}

        Stateless specialist powering the **{code}** lens — {entry['name']} {entry['icon']}.
        User-facing behavior: `{{module-root}}/modes/lens.md` (Teach -> Model -> Practice).

        ## Activation

        1. Load persona: `{{module-root}}/agents/specialists/{slug}.md`
        2. Load technique: `{{module-root}}/resources/heuristics/{entry['heuristic_file']}#{entry['anchor']}`
        3. Load lens guide: `{{module-root}}/resources/heuristics/_lens-guides.md` (section for {code})
        4. Load protocol: `{{module-root}}/references/specialist-protocol.md`
        5. Load core: `{{module-root}}/core/socratic-ladder.md` + `{{module-root}}/core/feedback-protocol.md`
        6. Read learner state: `{{sanctum}}/BOND.md` + `{{sanctum}}/LEARNER.md` (anchor domains, how they learn).
        7. Resolve `understanding_artifacts` and `communication_language` from config.
        8. Greet lightly as {entry['icon']} **{entry['name']}** — one sentence on the {code} move (persona is flavor, not theater).
        9. Run **Teach -> Model -> Practice** (`{{module-root}}/modes/lens.md`): motivate -> intuition -> tiny model -> WORKED EXAMPLE -> learner applies -> capture the useful result to the artifact.{sanctum_note}

        ## Menu

        | Code | Action |
        | --- | --- |
        | `RUN` | Apply the {code} lens to the active context |
        | `BACK` | Hand off to Veda (`veda-agent`) |

        ## On complete

        Summarize what the lens added to the core model -> hand back to Veda for the next move.
        """
    )


def customize_toml(entry: dict) -> str:
    return textwrap.dedent(
        f"""\
        [agent]
        customizable = "yes"

        [agent.persistent_facts]
        facts = [
          "Powers the {entry['code']} lens only (Lens Library: lenses/index.md).",
          "Behavior: modes/lens.md — Teach -> Model -> Practice; worked example before apply.",
          "Protocol: references/specialist-protocol.md",
          "Withhold: core/socratic-ladder.md · Feedback: core/feedback-protocol.md",
          "Lens guide: resources/heuristics/_lens-guides.md",
          "Extend the learner's Mastery Card; hand off to veda-agent when done.",
          "Technique: {entry['heuristic_file']}#{entry['anchor']}",
        ]

        [agent.activation_steps_prepend]
        steps = [
          "You are {entry['name']} — powering the {entry['code']} lens. Stateless. Emphasize the move, not the character.",
        ]
        """
    )


def main() -> None:
    entries = load_registry()
    SPECIALISTS_DIR.mkdir(parents=True, exist_ok=True)

    for entry in entries:
        slug = entry["slug"]
        (SPECIALISTS_DIR / f"{slug}.md").write_text(persona_md(entry))

        skill_dir = SKILLS_DIR / f"veda-agent-{slug}"
        skill_dir.mkdir(parents=True, exist_ok=True)
        (skill_dir / "SKILL.md").write_text(skill_md(entry))
        (skill_dir / "customize.toml").write_text(customize_toml(entry))

        refs = skill_dir / "references"
        refs.mkdir(exist_ok=True)
        if PROTOCOL_SRC.exists():
            (refs / "protocol.md").write_text(PROTOCOL_SRC.read_text())
        if TEACH_SRC.exists():
            (refs / "teach-before-ask.md").write_text(TEACH_SRC.read_text())

    print(f"Generated {len(entries)} lens personas in {SPECIALISTS_DIR}")
    print(f"Generated {len(entries)} skill folders in {SKILLS_DIR}")


if __name__ == "__main__":
    main()
