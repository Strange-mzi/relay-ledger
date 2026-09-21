# Review the assigned artifact

Use the requested scope and project acceptance criteria. An implementer report is a navigation aid, not proof. Inspect the exact revision/diff and necessary call paths; preserve unrelated working-tree changes.

Review only. Do not fix code, switch roles, broaden to unrelated modules, or update a ledger forbidden by a read-only request. Use the host's native review facilities if available without claiming they were used when they were not.

Check behavior, boundary conditions, permissions, compatibility and acceptance requirements relevant to the diff. Run meaningful independent checks when permitted and feasible; avoid broad testing without a reason. Existing test success does not establish requirements coverage.
Map each in-scope acceptance ID to its actual implementation and verification evidence. Mark missing or unavailable evidence explicitly; task checkboxes and keyword matches alone cannot establish correctness. Report coverage gaps separately from confirmed bugs, and omit stylistic suggestions when the user requested bugs only.

Report actionable, demonstrable issues with severity, exact location, trigger and consequence. Distinguish newly introduced faults from pre-existing behavior that the batch explicitly promised to close. Respect a user's bugs-only scope; do not add stylistic, naming or refactoring requests.

If no issue is confirmed, say “No confirmed issue within this scope,” not “the entire system is safe.” State what was actually checked and what could not be checked. A previously accepted revision does not certify its successor.

Bind findings to stable IDs for follow-up. A fix claim remains pending until the relevant evidence has been checked. If the reviewer also implemented the change, disclose the conflict and classify the result as self-review rather than independent acceptance.
Keep a reviewer handoff neutral: requirements, revision and findings to recheck, not an instruction to confirm the implementer's conclusion. A new test report does not certify a different revision.

Where writing is authorized, place the review in a separate report with revision, scope, findings, checks and limitations. Let the coordinator update shared acceptance state. Where writing is forbidden, provide the report and proposed ledger changes in the response only. Stop after the review.
