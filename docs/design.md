# Design and provenance

The instructions in this repository are original. These public projects informed the design; no implementation or prompt text is vendored from them.

| Source | Borrowed idea | Deliberate boundary |
| --- | --- | --- |
| [Agent Skills specification](https://agentskills.io/specification) | Progressive disclosure and portable file layout | No runtime-specific core tools |
| [Ponytail](https://github.com/DietrichGebert/ponytail), [portability](https://github.com/DietrichGebert/ponytail/blob/main/docs/agent-portability.md), [debt skill](https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail-debt/SKILL.md) | Reuse and native capabilities before extra machinery; thin adapters; explicit revisit triggers for deferrals | No persistent persona, every-turn injection, code-golf rule or copying of upstream benchmark claims |
| [Planning with Files](https://github.com/OthmanAdi/planning-with-files) | Disk-backed continuity and explicit task selection | No mandatory three-file rewrite, per-turn hooks or transcript replay |
| [Superpowers](https://github.com/obra/superpowers) | Scoped implementer/reviewer handoffs; evidence before completion claims | No mandatory TDD, model choice, worktree creation or automatic delegation |
| [GSD recovery workflow](https://github.com/gsd-build/get-shit-done/blob/main/get-shit-done/workflows/resume-project.md) | Restore position and interrupted work before choosing the next action | No full runtime, pipeline or automatic phase progression |

Sources were inspected on 2026-09-21. Upstream branches can change. GSD's old repository now points to [GSD Core](https://github.com/open-gsd/gsd-core); the linked recovery file is a design reference, not installation guidance.

## Context contract

The entrypoint routes; one mode explains the task; the current brief supplies facts. Archives are references, not default context. No workflow can promise zero context pollution, so claims here describe loading rules rather than a measured token reduction.

## Role contract

Role comes from current explicit intent, then the authorized assignment. State cannot grant authority. Review remains read-only when requested. Independent acceptance requires an independently scoped reviewer and identifiable evidence, not a role label change.

## Persistence contract

Existing records remain the source of truth. A pointer is a navigation aid, not a replacement database. Old accepted evidence stays bound to its revision; new fixes have their own review status. Project state is not bundled or uploaded by this skill.
