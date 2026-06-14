#!/usr/bin/env python3
"""Generate specialist agent personas and skill folders from registry.yaml.

Usage (from veda/):
    python scripts/generate-specialist-agents.py
"""

from __future__ import annotations

import textwrap
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "resources/agents/registry.yaml"
SPECIALISTS_DIR = ROOT / "agents/specialists"
SKILLS_DIR = ROOT / "skills"
PROTOCOL_SRC = ROOT / "references/specialist-protocol.md"
TEACH_SRC = ROOT / "references/teach-before-ask.md"


def load_registry() -> list[dict]:
    data = yaml.safe_load(REGISTRY.read_text())
    return data["specialists"]


def persona_md(entry: dict) -> str:
    code = entry["code"]
    return textwrap.dedent(
        f"""\
        # {entry['name']} — {entry['title']}

        ```yaml
        agent:
          code: {code.lower() if code != '5W' else 'five-whys'}
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
            - Own exactly one technique: {code} ({entry['slug'].replace('-', ' ')}).
            - Teach through lens before probing; insight question before recall questions.
            - One question at a time; curiosity beats certainty.
            - Write insights to the active artifact; hand off to Veda when done.
            - Never fake memory — stateless rebirth each session.
        ```

        ## Heuristic source

        `{entry['heuristic_file']}#{entry['anchor']}`

        ## When to invoke

        - User wants **{entry['title'].replace(' Guide', '')}** applied to a topic or decision
        - Veda routes here from `HEUR` menu with code `{code}`
        - Mid-workflow in `veda-learn` or `veda-analyze` when user picks `{code}`

        ## Handoff

        On complete → suggest `veda-agent` for next heuristic or latticework.
        """
    )


def skill_md(entry: dict) -> str:
    slug = entry["slug"]
    code = entry["code"]
    agent_code = code.lower() if code != "5W" else "five-whys"
    updates = entry.get("updates_sanctum", False)
    sanctum_note = (
        "\n8. **Sanctum:** Update `_bmad/sanctum/veda/MEMORY.md` latticework table."
        if updates
        else ""
    )

    return textwrap.dedent(
        f"""\
        ---
        name: veda-agent-{slug}
        description: >
          {entry['icon']} {entry['name']} — {entry['title']}. Stateless specialist for
          heuristic {code}. Apply {entry['slug'].replace('-', ' ')} to any topic.
        type: agent
        agent_code: {agent_code}
        archetype: stateless
        heuristic_code: {code}
        owner: veda
        ---

        # veda-agent-{slug}

        Stateless specialist launcher for **{code}** — {entry['name']} {entry['icon']}.

        ## Activation

        1. Load persona: `{{module-root}}/agents/specialists/{slug}.md`
        2. Load heuristic: `{{module-root}}/resources/heuristics/{entry['heuristic_file']}#{entry['anchor']}`
        3. Load lens guide: `{{module-root}}/resources/heuristics/_lens-guides.md` (section for {code})
        4. Load protocol: `{{module-root}}/references/specialist-protocol.md`
        5. Load teach-before-ask: `{{module-root}}/references/teach-before-ask.md`
        6. Resolve `understanding_artifacts` and `communication_language` from config.
        7. Greet as {entry['icon']} **{entry['name']}** — embody {entry['title']}. One sentence on your technique.
        8. Ask what topic or decision to apply {code} to (unless context already provided by Veda).
        9. Run **Teach-Before-Ask**: lens brief → insight probe → adaptive dialogue; write to artifact.{sanctum_note}

        ## Menu

        | Code | Action |
        | --- | --- |
        | `RUN` | Apply {code} to active context |
        | `BACK` | Hand off to Veda (`veda-agent`) |

        ## On complete

        Summarize insights → suggest Veda for next step or `veda-help`.
        """
    )


def customize_toml(entry: dict) -> str:
    slug = entry["slug"]
    return textwrap.dedent(
        f"""\
        [agent]
        customizable = "yes"

        [agent.persistent_facts]
        facts = [
          "Specialist for heuristic {entry['code']} only.",
          "Protocol: references/specialist-protocol.md",
          "Teach-Before-Ask: references/teach-before-ask.md",
          "Lens guide: resources/heuristics/_lens-guides.md",
          "Hand off to veda-agent when done.",
          "Heuristic: {entry['heuristic_file']}#{entry['anchor']}",
        ]

        [agent.activation_steps_prepend]
        steps = [
          "You are {entry['name']} — {entry['title']}. Stateless specialist.",
        ]
        """
    )


def main() -> None:
    entries = load_registry()
    SPECIALISTS_DIR.mkdir(parents=True, exist_ok=True)

    for entry in entries:
        slug = entry["slug"]
        persona_path = SPECIALISTS_DIR / f"{slug}.md"
        persona_path.write_text(persona_md(entry))

        skill_dir = SKILLS_DIR / f"veda-agent-{slug}"
        skill_dir.mkdir(parents=True, exist_ok=True)
        (skill_dir / "SKILL.md").write_text(skill_md(entry))
        (skill_dir / "customize.toml").write_text(customize_toml(entry))

        refs = skill_dir / "references"
        refs.mkdir(exist_ok=True)
        protocol_dst = refs / "protocol.md"
        if PROTOCOL_SRC.exists():
            protocol_dst.write_text(PROTOCOL_SRC.read_text())
        teach_dst = refs / "teach-before-ask.md"
        if TEACH_SRC.exists():
            teach_dst.write_text(TEACH_SRC.read_text())

    print(f"Generated {len(entries)} specialist agents in {SPECIALISTS_DIR}")
    print(f"Generated {len(entries)} skill folders in {SKILLS_DIR}")


if __name__ == "__main__":
    main()
