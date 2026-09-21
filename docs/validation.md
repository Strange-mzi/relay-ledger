# Release validation

Recorded: 2026-09-21, v0.2.0 release preparation.

| Check | Observed result |
| --- | --- |
| Standard-library package checker, Windows | Passed |
| Ten checker regression tests, Windows | Passed |
| Standard-library package checker, WSL Ubuntu | Passed |
| Ten checker regression tests, WSL Ubuntu | Passed |
| Local skill-creator frontmatter validation | Passed |
| Codex plugin-creator manifest validation | Passed |
| Claude Code 2.1.278 `plugin validate --strict` | Passed |
| Claude Code 2.1.278 session-local native plugin discovery | `relay-ledger@inline` version 0.2.0, enabled |
| Codex CLI 0.133.0 isolated marketplace discovery and installation | `relay-ledger` version 0.2.0, installed and enabled |

The checker verifies required files, skill identity, description bounds, local Markdown links, entrypoint ceiling, shared host-manifest versions and machine-specific path leakage. Its tests exercise failure cases as well as the release package. It is not a comprehensive secret scanner or behavioral evaluator.

Native discovery checks made no model requests. Codex used a temporary isolated home/marketplace; Claude used session-local `--plugin-dir`. Neither check changed the user's installed plugin configuration. Both hosts consume the same canonical skill directory; no hook or agent runtime was required.

The release contains only original generic instructions, templates, documentation and maintainer checks. No project acceptance ledger, user conversation or business repository file is included.

[Behavioral scenarios](../evals/scenarios.md) and [structured positive/negative cases](../evals/cases.json) are supplied for future host/model evaluations. They have **not** been executed as an independent cross-model benchmark. There are no claims about measured token savings, model accuracy or universal auto-discovery. The core entrypoint remains 620 whitespace-separated words / 4283 UTF-8 bytes; this is a file measurement, not a token-saving benchmark.

GitHub Actions runs the package checks on Windows and Ubuntu for pushed revisions. Consult the actual run for its result; this document does not pre-claim remote CI success.
