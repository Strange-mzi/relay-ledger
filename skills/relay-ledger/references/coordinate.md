# Coordinate one batch

Restore the goal and latest controlling decisions before choosing work. Later explicit user decisions supersede older plans; mark the replaced decision and update only affected future work. A temporary deferral is not a change to the final goal.

Use an existing project acceptance record. If it is long, keep a small pointer with section references, not a duplicate history. With multiple streams, pointers are per stream; never silently switch the active one for another running session.

Reconcile only relevant claims with available evidence. An implementer report can establish “reported complete”; it cannot establish independent acceptance. A new fix revision reopens verification of affected findings. Preserve unaffected historical results with their original scope.

Useful states (use the project's vocabulary if it already has one):

- planned / implementing
- reported-complete / review-pending
- changes-requested / independently-verified
- user-accepted / deployed

Verification is not deployment authorization. Record source, revision, scope, command/result where available, and limitations. Never infer deployment from a commit, a passing test, or elapsed time.

Prepare only the next bounded assignment:

1. Goal and explicit non-goals.
2. Baseline, dependencies and minimum files/sections to read.
3. Correct actor/target boundaries and relevant data invariants.
4. Observable acceptance criteria: normal, denied, boundary and compatibility behavior as appropriate.
5. Minimal meaningful checks; distinguish implementer evidence from independent review.
6. Report destination, reviewer handoff, and stop condition.

Do not mix a UI move, permission redesign, money calculation and migration into one assignment merely because they share a screen. Parallel work needs disjoint write ownership or a concrete reconciliation plan. Do not automatically create branches, commit, publish, spawn agents or start the next batch.

Workers append their reports independently. The coordinator consolidates the accepted snapshot and issues; reread the current pointer before updating it, and stop on unexpected concurrent changes rather than overwriting them. Without atomic coordination, do not promise safe concurrent pointer edits.

End with: what changed in the record, what is verified versus reported, and the next assignment. Ask only for missing information that materially changes this decision.
