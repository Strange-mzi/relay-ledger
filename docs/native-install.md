# Native Claude Code and Codex support

One canonical skill, two thin manifests. No prompt duplication and no lifecycle injection.

## Claude Code

**Direct skill**: copy `skills/relay-ledger/` to either the project's `.claude/skills/relay-ledger/` or your personal `~/.claude/skills/relay-ledger/`. Invoke `/relay-ledger`.

**Session-local plugin**: clone this repository, then point Claude at the repository root:

```sh
git clone https://github.com/Strange-mzi/relay-ledger.git
claude --plugin-dir ./relay-ledger
```

The `.claude-plugin/plugin.json` manifest uses native `skills/` discovery. The plugin invocation is `/relay-ledger:relay-ledger`. Do not also install the standalone skill in the same host.

Metadata and discovery can be checked without making a model request:

```sh
claude plugin validate ./relay-ledger --strict
claude --plugin-dir ./relay-ledger plugin list --json
```

See [Claude skills](https://code.claude.com/docs/en/skills) and [plugin reference](https://code.claude.com/docs/en/plugins-reference). Claude Code is the tested packaging target; Claude chat/Cowork use their own skill upload and discovery mechanisms, not these CLI flags.

## Codex

**Direct skill**: copy `skills/relay-ledger/` to the project's `.agents/skills/relay-ledger/` or your personal `~/.agents/skills/relay-ledger/`. If your current Codex installation manages skills under `~/.codex/skills/`, keep using that recognized location rather than installing a duplicate. Invoke `$relay-ledger` or select it in the skill picker.

**Plugin distribution**: `.codex-plugin/plugin.json` declares `skills: "./skills/"`. A Codex marketplace can reference this repository as its plugin package. This release does not install or rewrite your marketplace. For one skill, the direct route above needs no marketplace or runtime dependency.

See [Codex local skills](https://learn.chatgpt.com/docs/build-skills) and [supported Codex plugin layout](https://developers.openai.com/plugins/build/plugins).

## Other models and operating systems

The model does not choose the filesystem layout; its host does. Use the same standard skill in another compatible host, or [the portable prompt](portable-prompt.md) in chat-only tools. On Windows, `~` means the home directory of the environment running the agent; WSL and Windows homes are distinct. Do not assume installing into one installs into the other.

Native plans, subagents, approvals and context compaction stay under host control. The package neither forces a model nor requests broader tools. A validated manifest proves packaging, not instruction adherence across all models.
