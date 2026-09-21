# Relay Ledger

**Small context. Native agents. Verifiable handoffs.**

[简体中文](README.zh-CN.md) · [Native Claude / Codex installation](docs/native-install.md) · [Skill](skills/relay-ledger/SKILL.md) · [Design and sources](docs/design.md)

Relay Ledger is an instruction-only Agent Skill for continuing bounded project work across sessions and assistants. It preserves the goal, current assignment, role and acceptance evidence without feeding every session the entire project history.

## What it does

- Routes an explicit request to coordination, implementation or review.
- Restores a short current pointer and one batch brief; loads one role reference on demand.
- Separates reported completion from independently verified acceptance and deployment.
- Links each acceptance criterion to implementation and verification evidence; checks blockers before handing off dependent work.
- Produces a small handoff, including what the next agent is authorized to do.
- Works alongside existing project records instead of installing a second project manager.

It is not an agent runtime. It does not launch models, force chain-of-thought, inject prompts every turn, read chat databases, install hooks, run a background loop, upload state or change your global instructions. A Markdown assignment is not a distributed lock.

## Install

No runtime dependencies, hooks or MCP servers are bundled. Use your host's existing plugin manager and Git; **no extra Node.js lifecycle scripts or `/hooks` approval step**.

### Claude Code

Run these as **two separate messages** inside Claude Code:

```text
/plugin marketplace add Strange-mzi/relay-ledger
```

```text
/plugin install relay-ledger@relay-ledger
```

Start a new session and invoke `/relay-ledger:relay-ledger`. This applies to Claude Code, including the Code environment in Claude Desktop; ordinary Claude chat uses a different skill mechanism.

### Codex

Run these as **two terminal commands**:

```sh
codex plugin marketplace add Strange-mzi/relay-ledger
```

```sh
codex plugin add relay-ledger@relay-ledger
```

Start a new task; if the desktop app does not show it yet, restart the app. Select Relay Ledger in the skill picker or invoke `$relay-ledger`. The app/CLI must use the same Codex home; installing in WSL does not automatically install in Windows.

### Manual skill or temporary plugin

Copy **the whole `skills/relay-ledger` directory** to your tool's native Agent Skills directory. Keep the references and assets alongside `SKILL.md`.

| Host | Project install | Personal install | Direct invocation |
| --- | --- | --- | --- |
| Claude Code | `.claude/skills/relay-ledger/` | `~/.claude/skills/relay-ledger/` | `/relay-ledger` |
| Codex | `.agents/skills/relay-ledger/` | `~/.agents/skills/relay-ledger/` | `$relay-ledger` |

Thin native plugin manifests are also included; both load the **same** `skills/` tree. See [native installation](docs/native-install.md) for session-local Claude plugin loading and Codex packaging details. No plugins or host configuration are installed automatically.

For Codex project-local discovery:

```text
your-project/.agents/skills/relay-ledger/SKILL.md
```

Use the directory documented by your host; support and discovery paths belong to the host, not the model. The optional `agents/openai.yaml` provides Codex display metadata; the core does not require it. Avoid installing multiple copies of the same skill.

No Python, Node, API key or network access is required **to use** the skill. Python 3.10+ is used only by this repository's maintainer checks.

For chat-only assistants, paste [the portable prompt](docs/portable-prompt.md) and attach the small current brief. Without filesystem/tool access they can propose updates, not claim to have saved or verified them.

## Use

```text
Use relay-ledger. Continue this workstream.
```

```text
使用接力簿，更新验收记录，给我下一批任务。不要修改业务代码。
```

```text
Review commit abc123 against batch B03. Read-only; report bugs only.
```

The exact invocation syntax is host-specific. An explicit role overrides the recorded role. “Continue” preserves the existing authorization; it does not turn a review assignment into permission to write code.

## Context and state

Prefer your existing acceptance record. Optionally create `.relay/current.md` as a short pointer to it. The target is <=60 lines for the pointer and <=120 for the current brief, with links to necessary detail. These are operational guidelines, not measured token guarantees or enforced limits.

Do not commit private project records to this skill's repository. Keep project state in the project or its approved private location. Nothing is archived/deleted automatically, and nothing is silently added to `.gitignore` in your project.

For simultaneous workers, use native atomic assignments if available. Otherwise a single coordinator owns shared state and workers submit separate reports. Unknown ownership means clarify, not steal or duplicate work.

## Compatibility and validation

The package follows [Agent Skills](https://agentskills.io/specification). It uses ordinary Markdown and tool-neutral instructions: no fixed model names, context-window assumptions or mandatory subagent APIs. This enables portability, not a claim of identical behavior across all models.

See [compatibility and evaluation boundaries](docs/compatibility.md). Validation includes package checks, host manifest validation, [scenario expectations](evals/scenarios.md) and [structured cases](evals/cases.json); no cross-model performance benchmark is claimed.

```sh
python scripts/check_package.py
python -m unittest discover -s tests -v
```

MIT licensed. Original instructions, informed by the projects credited in [design notes](docs/design.md). Contributions should preserve narrow activation, evidence provenance and minimal context loading.
