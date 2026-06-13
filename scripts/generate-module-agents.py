#!/usr/bin/env python3
"""Print agents: block for module.yaml from registry."""

from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
data = yaml.safe_load((ROOT / "resources/agents/registry.yaml").read_text())

print("agents:")
print("  - code: veda")
print("    name: Veda")
print('    title: Understanding Guide')
print('    icon: "📖"')
print("    team: understanding")
print("    phase: all")
print("    archetype: memory")
print("    description: >")
print("      Memory orchestrator. Routes to 24 heuristic specialists.")
print("      Asks learning vs deciding; remembers latticework.")

for e in data["specialists"]:
    ac = e["code"].lower() if e["code"] != "5W" else "five-whys"
    print(f"  - code: {ac}")
    print(f"    name: {e['name']}")
    print(f"    title: {e['title']}")
    print(f'    icon: "{e["icon"]}"')
    print("    team: understanding")
    print(f"    phase: {e['phase']}")
    print("    archetype: stateless")
    print(f"    heuristic_code: {e['code']}")
    print(f"    skill: veda-agent-{e['slug']}")
    print("    description: >")
    print(f"      Stateless specialist for {e['code']} — {e['slug'].replace('-', ' ')}.")
