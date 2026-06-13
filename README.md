# Veda

A memory-guided learning system for **Cursor** and other [Agent Skills](https://agentskills.io)-compatible tools. Veda helps you **learn** complex topics and **decide** when you're stuck — using 24 dedicated thinking specialists (first principles, analogies, reference class, and more).

Thinking heuristics adapted from [`user-manual.md`](user-manual.md). Packaged as a [BMAD](https://github.com/bmad-code-org/BMAD-METHOD)-style module.

## What you get

| Component | What it does |
| --- | --- |
| **Veda** (`veda-agent`) | Memory orchestrator — welcomes you, asks your goal, routes to the right tool |
| **Learn** (`veda-learn`) | Guided exploration → Learning Notes in `docs/understanding/` |
| **Analyze** (`veda-analyze`) | Decision work → Decision Memo |
| **24 specialists** (`veda-agent-*`) | One agent per thinking technique — Petra (first principles), Clio (reference class), Anya (analogies), … |
| **Help** (`veda-help`) | Recommends your next step |

On first meeting, Veda asks your **name**, your **goal**, and shows a **skills catalog** in plain language. Say **`INTRO`** anytime to see it again.

## Quick install

```bash
git clone https://github.com/JMH-Design/veda.git
cd veda
chmod +x install.sh
./install.sh
```

Installs **29 skills** to `~/.cursor/skills/`. For other tools:

```bash
CURSOR_SKILLS=~/.claude/skills ./install.sh
```

### Start a project

See [`example-project/README.md`](example-project/README.md) for the suggested layout.

```bash
mkdir -p docs/understanding _bmad/sanctum/veda/sessions
python3 skills/veda-agent/scripts/init-sanctum.py \
  --sanctum ./_bmad/sanctum/veda \
  --owner "Your Name"
```

Invoke **`veda-agent`** in Cursor (or say **"Hey Veda"**).

## Usage examples

| You say | What happens |
| --- | --- |
| "Hey Veda" (first time) | Welcome → name → goal → skills catalog |
| "INTRO" | Full skills catalog |
| "Help me understand this paper" | Routes to **Learn** |
| "Should I take this job?" | Routes to **Analyze** |
| "Run first principles on X" | Routes to **Petra** (`veda-agent-first-principles`) |
| "What's next?" | **Help** |

Full specialist roster: [`resources/agents/index.md`](resources/agents/index.md)

## Repository layout

```txt
veda/
├── README.md
├── module.yaml
├── install.sh
├── user-manual.md
├── example-project/      # Suggested layout for your own repo
├── agents/               # Veda + 24 specialist personas
├── skills/               # All invokable skills (veda-agent, veda-learn, …)
├── resources/            # Heuristics + agent registry
├── templates/
└── scripts/
```

## Customize specialists

Edit `resources/agents/registry.yaml`, then:

```bash
pip install pyyaml   # if needed
python3 scripts/generate-specialist-agents.py
./install.sh
```

## Privacy

Veda's sanctum (`_bmad/sanctum/veda/`) stores personal memory. **Do not commit it.** See `.gitignore`.

## License

MIT — see [LICENSE](LICENSE).
