#!/usr/bin/env python3
"""Initialize Veda sanctum from seed templates."""
from __future__ import annotations

import argparse
import shutil
from datetime import date
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize Veda sanctum")
    parser.add_argument(
        "--sanctum",
        default="_bmad/sanctum/veda",
        help="Sanctum output directory",
    )
    parser.add_argument("--owner", default="", help="Owner name for templates")
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parents[1]
    assets = skill_root / "assets"
    sanctum = Path(args.sanctum)
    sanctum.mkdir(parents=True, exist_ok=True)
    (sanctum / "sessions").mkdir(exist_ok=True)
    (sanctum / "capabilities").mkdir(exist_ok=True)

    replacements = {
        "{{OWNER_NAME}}": args.owner or "friend",
        "{{DATE}}": date.today().isoformat(),
        "{{SESSION_STYLE}}": "to be discovered",
        "{{TOPICS}}": "- ",
        "{{BOND_NOTES}}": "",
        "{{MEMORY_SEEDS}}": "",
        "{{VOICE_CHOICE}}": "The Tutor",
        "{{ANCHOR_DOMAINS}}": "—",
        "{{TOPIC_FAMILIARITY}}": "—",
        "{{NATURAL_APPROACH}}": "—",
        "{{MENTAL_MODELS}}": "—",
    }

    mapping = {
        "INDEX-template.md": "INDEX.md",
        "PERSONA-template.md": "PERSONA.md",
        "CREED-template.md": "CREED.md",
        "BOND-template.md": "BOND.md",
        "MEMORY-template.md": "MEMORY.md",
        "CAPABILITIES-template.md": "CAPABILITIES.md",
    }

    for src_name, dst_name in mapping.items():
        src = assets / src_name
        dst = sanctum / dst_name
        if dst.exists():
            continue
        text = src.read_text(encoding="utf-8")
        for key, val in replacements.items():
            text = text.replace(key, val)
        dst.write_text(text, encoding="utf-8")

    print(f"Sanctum initialized at {sanctum}")


if __name__ == "__main__":
    main()
