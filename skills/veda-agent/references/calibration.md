# Calibration — user context for specialists

Run during **first meeting** after name and goal (introduction Step 2c). Specialists read `BOND.md` before their first question.

**Pace:** One step at a time.

## Host-specific UI

Structured steps B–D use the **host's choice tool** when available:

| Host | Tool | Payloads |
| --- | --- | --- |
| Cursor | `AskQuestion` | `calibration-cursor.md` |
| Claude Code | `AskUserQuestion` | `calibration-claude-code.md` |
| Codex | `ask_user_question` | `calibration-codex.md` |
| ChatGPT / no tool | — | **Fallback** below |

Read `calibration-hosts.md` for detection and install paths. Step A is always free text on every host.

---

## When to run

| Situation | Run |
| --- | --- |
| First meeting, after goal | Full calibration (Steps A → D; B only if learning) |
| Returning, `BOND.md` missing anchor domains or natural approach | Full calibration |
| Returning, goal is **Learn**, topic seems outside saved anchor domains | Step B only + optional Step A refresh |
| Returning, goal is Decide / Explore / one technique | Skip calibration |

---

## Step A — Anchor domains (free text)

Always on first calibration. **No multiple choice** — user names their own domains.

Ask:

> **What are 2–3 areas you're already fluent in?**
>
> These become the home base for analogies and examples — your job, hobbies, fields you've studied, domains you work in daily.
>
> For example: *clinical pharmacology, product design, parenting, competitive chess*.

On answer:

1. Parse into a short list (2–4 items). Normalize casing; keep their words.
2. Save to `BOND.md` under `## Calibration` → `Anchor domains:`.
3. Mirror top items to `## Interests` if empty.

---

## Step B — Topic familiarity (learn only)

**Only when goal maps to Learn** (introduction Step 2b: learn, or user states a topic to understand).

Use the host tool (`allow_multiple: false` / `multiSelect: false`). Claude Code: split per `calibration-claude-code.md`.

| id | label |
| --- | --- |
| `new` | **Brand new** — I haven't really encountered this before |
| `exposure` | **Some exposure** — I've heard or read about it, but couldn't explain it well |
| `comfortable` | **Comfortable** — I could explain the basics to someone else |
| `practitioner` | **Practitioner** — I work with this regularly |

Prompt: *"How well do you already know **{topic or 'this topic'}**?"*

If topic not yet stated, ask for topic first in one line, then Step B.

Save to `BOND.md` → `Topic familiarity:` (use label text, not id).

**Teaching use:** Familiarity calibrates **lens brief length** and **insight probe difficulty** in Learn mode. It does **not** skip the brief — even Practitioner gets a minimal teach-before-ask beat. See `references/teach-before-ask.md`.

---

## Step C — Natural approach (multiple choice)

Use the host tool (`allow_multiple: false` / `multiSelect: false`). Claude Code: split per `calibration-claude-code.md`.

| id | label | Routes toward |
| --- | --- | --- |
| `decompose` | **Break it into parts** — split the problem into pieces I can tackle one at a time | `DEC` Modulus |
| `compare` | **Compare to past cases** — look for what usually happens in situations like this | `RC` Clio |
| `why` | **Ask why repeatedly** — peel layers until I hit the root cause | `5W` Wren |
| `assumptions` | **Challenge assumptions** — list what I'm taking for granted and test each one | `CA` Ada |
| `invert` | **Flip it upside down** — imagine how this fails or what to avoid | `INV` Iris |
| `analogy` | **Find what it's like** — bridge from something I already understand | `ANA` Anya |
| `unsure` | **Not sure yet** — I'm still finding my approach | Veda routes by topic |

Prompt: *"When you hit a hard problem, what's your first instinct?"*

Save to `BOND.md` → `Natural approach:` (label text). If `unsure`, save as `Not sure yet`.

---

## Step D — Mental models (multiple choice)

Use the host tool (`allow_multiple: true` / `multiSelect: true`). Claude Code: two calls per `calibration-claude-code.md`.

| id | label |
| --- | --- |
| `fp` | **First principles** — rebuild from what must be true |
| `systems` | **Systems thinking** — feedback loops, stocks and flows, unintended effects |
| `base-rates` | **Base rates** — what usually happens in cases like this |
| `inversion` | **Inversion** — avoid failure, think backwards |
| `hypothesis` | **Hypothesis testing** — state beliefs and look for evidence |
| `key-drivers` | **Key drivers** — find the few factors that move everything else |
| `none` | **None yet** — still building my toolkit |
| `other` | **Other** — I'll describe in chat |

Prompt: *"Which thinking tools do you already reach for? Pick any that fit."*

**If `other` selected:** follow with one short free-text question: *"What else do you use?"* Append to the list.

**If `none` only:** save `Mental models: None yet` — specialists start with analogies and decomposition, not latticework.

Save to `BOND.md` → `Mental models:` (comma-separated labels).

Seed `MEMORY.md` latticework table — one row per model (skip `none`):

```markdown
| {model} | User toolkit (calibration) | — |
```

Keep MEMORY under 200 lines.

---

## BOND.md format after calibration

```markdown
## Calibration

- Anchor domains: pharmacology, product design, trail running
- Topic familiarity: Some exposure — heard about it, couldn't explain well
- Natural approach: Compare to past cases
- Mental models: First principles, Base rates

## Preferences

- Session style: {{SESSION_STYLE}}
- Typical mode: learning | deciding | both
```

---

## Specialist handoff

When delegating to `veda-agent-*`, pass in session context:

- Read `BOND.md` → `## Calibration`
- Ground **all examples and analogies** in anchor domains
- **Topic familiarity** → brief length + probe difficulty (never skip lens brief on Learn)
- Run **Teach-Before-Ask** per `references/teach-before-ask.md` before Apply now pool
- Prefer routing aligned with natural approach when user didn't pick a technique
- Link new insights to listed mental models in `LAT` and artifact prose

---

## Fallback (ChatGPT, Ask mode, or no structured tool)

Present options exactly as in the tables above. User may reply with number(s), id, or label. Accept partial matches.

**ChatGPT** (web/desktop): skills run without a choice UI today — always use this fallback there.

---

## Examples

**First meeting, learn goal:**

> Veda: What are 2–3 areas you're already fluent in?
> User: nursing, hiking, sci-fi
> Veda: [AskQuestion — topic familiarity]
> User: Some exposure
> Veda: [AskQuestion — natural approach]
> User: Find what it's like
> Veda: [AskQuestion — mental models, multi]
> User: Base rates, Systems thinking
> Veda: [Continue to skills catalog or route]

**First meeting, decide goal — skip Step B:**

> Steps A → C → D only (no topic familiarity question).
