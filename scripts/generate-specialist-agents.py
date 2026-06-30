#!/usr/bin/env python3
"""DEPRECATED — renamed to generate-lens-agents.py (v2 Lens Library).

The "specialist roster" is now the Lens Library. This shim forwards to the new generator so
existing commands keep working. Prefer:

    python scripts/generate-lens-agents.py
"""

from __future__ import annotations

import runpy
from pathlib import Path

if __name__ == "__main__":
    print("[deprecated] generate-specialist-agents.py -> generate-lens-agents.py")
    target = Path(__file__).resolve().parent / "generate-lens-agents.py"
    runpy.run_path(str(target), run_name="__main__")
