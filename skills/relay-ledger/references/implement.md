# Implement the assigned batch

Read the current brief and the project instructions applying to its files. Check relevant existing changes first. Do not replay all historical sessions or infer new requirements from unrelated ledger notes.

Implement only the authorized batch, using the host's native tools and existing project conventions. Follow dependency and data-compatibility boundaries in the brief. Do not overwrite another worker's changes or restore stashes without authorization.

Perform checks meaningful for the change. Report actual commands and outcomes, not predicted success. A failed environment setup is a verification limitation, not a code failure or a pass.

Commit only when the assignment authorizes it. Identify the reviewed artifact precisely: commit, or a working-tree snapshot with changed files and timestamp/digest. Never claim an unstaged fix is part of an older commit.

Write a scoped report when permitted:

- Batch ID, role and actual baseline/result revision.
- Behavior delivered and files changed.
- Checks run, results and evidence locations.
- Known gaps, unverified boundaries and relevant concurrent work.
- Status: reported-complete or blocked, not independently-verified.

Do not review your own implementation under a second persona and label it independent. The coordinator or user selects a separately scoped reviewer; if no independent reviewer is available, say so.

If only one session is active and it owns the pointer, update it to review-pending. With separate coordinator ownership, write your report and return its path; do not race to rewrite shared state. Stop after this batch, including when the full roadmap contains more work.
