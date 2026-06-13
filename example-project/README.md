# Example project layout

This folder is a **minimal skeleton** showing where Veda expects files in *your* project — not a runnable app. Copy these paths into any repo where you use Veda.

## What's inside

```txt
example-project/
├── README.md                          # This file
├── docs/
│   └── understanding/
│       └── .gitkeep                   # Learning notes & decision memos go here
└── _bmad/
    └── sanctum/
        └── veda/
            └── README.md              # Placeholder — sanctum files created by init
```

| Path | Purpose |
| --- | --- |
| `docs/understanding/` | Where Veda writes **Learning Notes** and **Decision Memos** (`{topic}.md`) |
| `_bmad/sanctum/veda/` | Veda's **personal memory** — name, preferences, latticework, session logs |

Nothing here runs on its own. After copying the structure, install skills and initialize memory.

## Setup in your project

```bash
# 1. Install Veda skills (from the veda repo root)
/path/to/veda/install.sh

# 2. Create folders in YOUR project
mkdir -p docs/understanding _bmad/sanctum/veda/sessions

# 3. Initialize Veda's memory
python3 /path/to/veda/skills/veda-agent/scripts/init-sanctum.py \
  --sanctum ./_bmad/sanctum/veda \
  --owner "Your Name"

# 4. Invoke veda-agent in Cursor
```

## Git

Add to your project's `.gitignore` if memory and notes are private:

```gitignore
_bmad/sanctum/veda/
docs/understanding/*.md
```

Or version your learning notes in git — your choice.
