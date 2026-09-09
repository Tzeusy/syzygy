REVISE

Reviewed exact diff `31571f6..52107bd6582bb2131974e1e1f65134d58a813ecb`.

1. **P2 — Mutation sweep targets obsolete source text.** `apps/three-surface-poc/src/pwb-mutation-sweep.ts:99` defines `named-absent-file-dropped` using the unconditional tree-rule skip. The repaired manifest now conditions that skip on an existing blob, so the fragment matches zero times. [Observed] The mutation-plan test fails with `named-absent-file-dropped occurrences: expected +0 to be 1`; the mutation applicator requires exactly one match. Update both replacement fragments to preserve the new existing-blob condition, then rerun the plan test and affected mutant. This violates the engineering bar’s behavior-verification and regression-protection criteria.

[Observed] The earlier missing/non-blob population finding is repaired: the skip now matches the tree rules’ blob eligibility, and explicit regression assertions preserve absent and non-blob named sources. The repeated root derivation is repaired by returning the screened derivation and consuming it without rereading root text. Admission-ordering, excluded/NUL root, ambiguous-home, and non-root widening cases have direct tests.

[Observed] Focused manifest and observation suites passed: 63 tests across two files. The mutation-plan suite passed three tests and failed one. Review covered the implementation/test diff and the signed PWB-REQ-001/005/006 plus registry read-authority and parse-budget semantics. No Butlers bodies were read, source mutations were not run, and the full governance battery and live walkthrough were outside this review.
