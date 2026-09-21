# Templates — copy only what is needed

Use an existing record if available. Replace illustrative values; do not create every file automatically.

## Small current pointer

```markdown
# Current workstream
Project: local project identifier
Workstream: stable slug
Goal: one sentence
Record: relative path and relevant section
Current batch: B03
Brief: relative path
Stage: review-pending
Owner: coordinator/session identity if available
Assignments: implementer completed; reviewer unassigned
Authorized role/action: review revision abc123; no code edits
Evidence: relative report path
Open issues: B03-01
Next: review the fix; do not start B04
Updated: actual timestamp
```

## Batch brief

```markdown
# B03 — Observable outcome
Goal:
Baseline:
Scope / non-goals:
Dependencies and write ownership:
Read first: specific files or sections
Controlling decisions and invariants:
Acceptance criteria:
Verification appropriate to this change:
Report destination:
Commit/publication permissions:
Stop: complete this batch; hand off for review
```

## Durable acceptance record

```markdown
# Project acceptance
Original goal:
Final behavior and non-goals:
Current controlling decisions:
Superseded decisions: reason and replacement

| Batch | Outcome | Status/source | Revision | Evidence | Open issues |
| --- | --- | --- | --- | --- | --- |

| Issue ID | Trigger and impact | Found in | Fix revision | Recheck | Status |
| --- | --- | --- | --- | --- | --- |

Next batch and dependencies:
Deployment/user acceptance evidence: unverified until established
```

Store results and short facts, not transcripts or hidden reasoning. A private label does not enforce access control: choose storage based on the project's actual sharing policy.
