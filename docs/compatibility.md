# Compatibility is about the host, not a model name

| Environment | Mode | Limits |
| --- | --- | --- |
| Claude Code | Native `.claude/skills` or thin `.claude-plugin` manifest | Choose standalone or plugin route; no duplicate installation |
| Codex | Native `.agents/skills` or supported `.codex-plugin` manifest | Existing installations may use `.codex/skills`; use the recognized host location |
| Agent Skills host with file tools | Native `SKILL.md` discovery; read one role reference | Discovery path and invocation syntax vary |
| Host with native plans/tasks | Keep native task tracking; ledger is a durable handoff | Do not duplicate the entire native plan |
| Host with authorized native subagents | Scoped task brief plus independent report | No forced model selection or automatic fan-out |
| Host without subagents | Work inline or hand off to a separate session | No simulated independent reviewer |
| Chat-only model | Portable prompt plus user-supplied small excerpts | No claimed disk writes, Git checks or automatic recovery |
| Parallel sessions | Native atomic assignment, or single coordinator | No distributed lock implemented by this package |

Installation does not give every new session knowledge of an arbitrary project. The host must discover the skill and the project must expose its current record path. Add a short pointer to existing project instructions only when authorized; do not paste the entire skill into global rules.

The core is model-neutral and contains no vendor-specific tool invocations. The optional Codex skill metadata is an adapter for display, not a requirement. Both plugin manifests load the same canonical skill. No benchmark across Claude, GPT, Gemini, Grok or other model families has been performed for this release; native packaging compatibility is not behavioral equivalence. See [native installation](native-install.md).

Checks that can be automated locally: package layout, frontmatter, relative links, context-size ceiling and accidental local path leakage. Behavioral routing, factual recovery and instruction adherence need scenario testing in each intended host. Record model/host version, input, evidence and observed result when running those scenarios.
