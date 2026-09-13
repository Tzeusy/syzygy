# Impact ledger — PWB scoped epistemic attributes

> **Candidate — binds nothing.** Companion to `SEMANTIC-DELTA.md`.

Baseline: commit `a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d`.

## Discovery method

Two sweeps over every tracked file at the baseline, run 2026-09-14
(verification rules 2 and 9; enumerated below, nothing sampled):

1. Python `re` over the UTF-8 text of every path in `git ls-files -z`:
   `PWB-REQ-0(07|14)\b|PWB-REQ-020\b` counted per file, plus a second
   pattern for continuation forms (`PWB-REQ-007/014/020`, `… 007, 014 and
   020`) — every file matching a continuation form also matched the full
   form, so the continuation pattern added no file.
2. `git grep -l -F` for each of the three literal identifiers, union.

Both methods return the same **80 files** over a denominator of **1,216**
tracked files. `.beads/issues.jsonl` is untracked (ignored) and outside the
denominator; the beads that cite these identifiers are `syzygy-dov.1` and
`syzygy-dov.17`, read directly.

## Classes

| class | files | disposition |
|---|---|---|
| signed package | 6 | the amendment subject itself; three rows change, eight are byte-identical (the coverage files restate the clause titles only and stay true) |
| unbound spec companion | 3 | not in the manifest; `tasks.md` takes implementation rows after adoption, the two coverage parts restate parity findings that remain true |
| other openspec change | 1 | cites PWB-REQ-014/020 as the parity floor the generator inherits; the floor is unchanged in the machine form |
| renderer / model | 8 | implementation sites after adoption: the claim element, the narrative unit and the shared model's tuple emission; no change while candidate |
| oracle / test | 9 | implementation sites after adoption: each oracle gains its own scope expansion and the sweep gains the scope-hidden mutant class |
| script | 1 | the state-(1) recorder names PWB-REQ-020 in its docstring; historical, untouched |
| docs / plans | 5 | plans and the funnel/pursuit records that led here; the funnel's draft delta is superseded by this package and says so by date |
| retained review | 23 | raw reviewer output; never edited (CC-REV-6) |
| evidence record | 17 | frozen evidence; never edited; a lane B measurement is a new record in the lane A shape |
| decision record | 3 | performed acts and rulings; never edited |
| governance package | 3 | the performed 2026-09-02 package; never edited |
| root page | 1 | AGENTS.md's parity guardrail (per tuple, never per id) stays true; expansion keeps one tuple per claim |

Sum: 80. Files the implementation must change after adoption are marked
**must** in the last column; every other row is untouched by this package.

## Every citing file

| file | class | 007 | 014 | 020 | implementation |
|---|---|---|---|---|---|
| `openspec/changes/polaris-project-wide-butlers-model/CAPABILITY-COVERAGE.md` | signed package | 2 | 2 | 2 | — |
| `openspec/changes/polaris-project-wide-butlers-model/CONTRACT-COVERAGE-REPAIR-DELTA.md` | signed package | 16 | 15 | 1 | — |
| `openspec/changes/polaris-project-wide-butlers-model/GOVERNING-DEPENDENCIES.md` | signed package | 20 | 17 | 15 | — |
| `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0004-0006.md` | signed package | 0 | 0 | 9 | — |
| `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0007-0009.md` | signed package | 0 | 0 | 2 | — |
| `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` | signed package | 1 | 1 | 1 | — |
| `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-parts/RFC-0004-0006.md` | unbound spec companion | 0 | 0 | 12 | — |
| `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-parts/RFC-0007-0009.md` | unbound spec companion | 0 | 0 | 7 | — |
| `openspec/changes/polaris-project-wide-butlers-model/tasks.md` | unbound spec companion | 1 | 1 | 3 | — |
| `openspec/changes/polaris-manifesto-generation/design.md` | other openspec change | 0 | 1 | 1 | — |
| `apps/three-surface-poc/src/fresh-checkout-demo-main.ts` | renderer / model | 0 | 0 | 1 | — |
| `apps/three-surface-poc/src/fresh-checkout-verdict.ts` | renderer / model | 0 | 0 | 1 | — |
| `apps/three-surface-poc/src/polaris-accessibility.ts` | renderer / model | 0 | 0 | 1 | — |
| `apps/three-surface-poc/src/polaris-copy.ts` | renderer / model | 1 | 1 | 0 | — |
| `apps/three-surface-poc/src/polaris-narrative.ts` | renderer / model | 0 | 3 | 0 | **must** |
| `apps/three-surface-poc/src/polaris.ts` | renderer / model | 3 | 2 | 0 | **must** |
| `apps/three-surface-poc/src/routes.ts` | renderer / model | 0 | 1 | 0 | — |
| `packages/three-surface-poc-core/src/project-shape-model.ts` | renderer / model | 4 | 0 | 1 | model |
| `apps/three-surface-poc/src/polaris-authority-sweep.test.ts` | oracle / test | 0 | 1 | 0 | **must** |
| `apps/three-surface-poc/src/polaris-epistemic-tuples.test.ts` | oracle / test | 2 | 0 | 0 | **must** |
| `apps/three-surface-poc/src/polaris-first-reading.test.ts` | oracle / test | 0 | 0 | 2 | — |
| `apps/three-surface-poc/src/polaris-narrative.test.ts` | oracle / test | 0 | 2 | 0 | **must** |
| `apps/three-surface-poc/src/polaris-parity-sweep.test.ts` | oracle / test | 0 | 0 | 3 | **must** |
| `apps/three-surface-poc/src/polaris-presentation-route.test.ts` | oracle / test | 0 | 2 | 0 | **must** |
| `apps/three-surface-poc/src/polaris-proposed-work.test.ts` | oracle / test | 0 | 1 | 0 | — |
| `apps/three-surface-poc/src/polaris-reachability.test.ts` | oracle / test | 0 | 0 | 2 | — |
| `apps/three-surface-poc/src/pwb-mutation-sweep.ts` | oracle / test | 0 | 0 | 4 | **must** |
| `scripts/record_pwb_state1_amendment.py` | script | 0 | 0 | 1 | — |
| `docs/PWB-IMPLEMENTATION-PLAN.md` | docs / plans | 2 | 2 | 4 | — |
| `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` | docs / plans | 7 | 5 | 10 | — |
| `docs/pursuits/2026-09-13-vision-pursuit-data.json` | docs / plans | 9 | 2 | 9 | — |
| `docs/pursuits/2026-09-13-vision-pursuit-harvest.json` | docs / plans | 4 | 1 | 5 | — |
| `docs/pursuits/2026-09-13-vision-pursuit.md` | docs / plans | 1 | 0 | 0 | — |
| `docs/reviews/2026-09-05-pwb-live-exact-head-packet.md` | retained review | 0 | 1 | 0 | — |
| `docs/reviews/R-POLARIS-GUIDE-NAVIGATION-RACE-2026-09-10-RAW.md` | retained review | 0 | 1 | 0 | — |
| `docs/reviews/R-POLARIS-PROJECT-WIDE-SPEC-CONFIRMATION-1-RAW.md` | retained review | 3 | 2 | 0 | — |
| `docs/reviews/R-POLARIS-PROJECT-WIDE-SPEC-CONFIRMATION-3-RAW.md` | retained review | 6 | 3 | 0 | — |
| `docs/reviews/R-POLARIS-PROJECT-WIDE-SPEC-CONFIRMATION-4-RAW.md` | retained review | 2 | 1 | 0 | — |
| `docs/reviews/R-POLARIS-PROJECT-WIDE-SPEC-CONFIRMATION-FINAL-RAW.md` | retained review | 1 | 0 | 0 | — |
| `docs/reviews/R-POLARIS-PROJECT-WIDE-SPEC-REVIEW-DISPOSITION.md` | retained review | 2 | 0 | 0 | — |
| `docs/reviews/R-POLARIS-READING-ASSETS-CODE-2026-09-10-RAW.md` | retained review | 0 | 1 | 1 | — |
| `docs/reviews/R-POLARIS-READING-ASSETS-REPAIR-2026-09-10-RAW.md` | retained review | 0 | 1 | 0 | — |
| `docs/reviews/R-PWB-LIVE-EXACT-HEAD-TRUTH-RAW.md` | retained review | 1 | 2 | 1 | — |
| `docs/reviews/R-PWB-M1-POLARIS-LANE-A-RAW.md` | retained review | 1 | 1 | 2 | — |
| `docs/reviews/R-PWB-P63-POLARIS-TRIM-RAW.md` | retained review | 0 | 1 | 0 | — |
| `docs/reviews/R-PWB-RECOVERY-RECONCILIATION-GEN1-RAW.md` | retained review | 1 | 1 | 2 | — |
| `docs/reviews/R-PWB-STATE1-ACT-SECURITY-RAW.md` | retained review | 0 | 0 | 1 | — |
| `docs/reviews/R-PWB-STATE1-FINAL-ORACLES-RAW.md` | retained review | 0 | 0 | 4 | — |
| `docs/reviews/R-PWB-STATE1-FINAL-SECURITY-RAW.md` | retained review | 0 | 0 | 2 | — |
| `docs/reviews/R-PWB-STATE1-FINAL-TRANSACTION-RAW.md` | retained review | 0 | 0 | 1 | — |
| `docs/reviews/R-PWB-STATE1-ORACLES-CONFIRMATION-RAW.md` | retained review | 0 | 0 | 4 | — |
| `docs/reviews/R-PWB-STATE1-ORACLES-RAW.md` | retained review | 0 | 0 | 3 | — |
| `docs/reviews/R-PWB-STATE1-SECURITY-CONFIRMATION-RAW.md` | retained review | 0 | 0 | 1 | — |
| `docs/reviews/R-PWB-STATE1-SECURITY-RAW.md` | retained review | 0 | 0 | 1 | — |
| `docs/reviews/R-PWB-STATE1-TRANSACTION-CONFIRMATION-RAW.md` | retained review | 0 | 0 | 3 | — |
| `docs/reviews/R-PWB-STATE1-TRANSACTION-RAW.md` | retained review | 0 | 0 | 1 | — |
| `docs/evidence/polaris-generator-host-overlap-2026-09-12.json` | evidence record | 0 | 2 | 1 | — |
| `docs/evidence/polaris-generator-rfc7-coverage-2026-09-12.json` | evidence record | 0 | 37 | 17 | — |
| `docs/evidence/polaris-generator-rfc7-coverage-v2-2026-09-12.json` | evidence record | 0 | 37 | 17 | — |
| `docs/evidence/polaris-generator-rfc7-coverage-v3-2026-09-12.json` | evidence record | 0 | 37 | 17 | — |
| `docs/evidence/polaris-generator-rfc7-coverage-v4-2026-09-12.json` | evidence record | 0 | 38 | 18 | — |
| `docs/evidence/polaris-generator-rfc7-coverage-v5-2026-09-12.json` | evidence record | 0 | 38 | 18 | — |
| `docs/evidence/polaris-manifesto-example-mutation-2026-09-09.json` | evidence record | 0 | 0 | 3 | — |
| `docs/evidence/polaris-pipeline-synthetic-verification-2026-09-13.json` | evidence record | 1 | 2 | 1 | — |
| `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json` | evidence record | 2 | 6 | 10 | — |
| `docs/evidence/pwb-p2-7-model-mutation-run-2026-09-04.json` | evidence record | 0 | 0 | 1 | — |
| `docs/evidence/pwb-p3-8-reachability-mutation-run-2026-09-04.json` | evidence record | 1 | 0 | 9 | — |
| `docs/evidence/pwb-p4-2-mutation-sweep-2026-09-04-parity-markers.json` | evidence record | 0 | 0 | 183 | — |
| `docs/evidence/pwb-p4-2-mutation-sweep-2026-09-04.json` | evidence record | 0 | 0 | 1 | — |
| `docs/evidence/pwb-p4-2-mutation-sweep-2026-09-06-parity-markers.json` | evidence record | 0 | 0 | 233 | — |
| `docs/evidence/pwb-p63-polaris-trim-measurement-2026-09-07.json` | evidence record | 0 | 1 | 1 | — |
| `docs/evidence/pwb-recon-gen1-reviewer-mutation-run-2026-09-06.json` | evidence record | 0 | 2 | 0 | — |
| `docs/evidence/pwb-recon-gen2-reviewer-mutation-run-2026-09-06.json` | evidence record | 0 | 0 | 1 | — |
| `.syzygy/governance/decisions/DECISION-HISTORY.md` | decision record | 1 | 0 | 0 | — |
| `.syzygy/governance/decisions/POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md` | decision record | 1 | 0 | 0 | — |
| `.syzygy/governance/decisions/PWB-STATE1-AMENDMENT-ACT.md` | decision record | 0 | 0 | 1 | — |
| `.syzygy/governance/contracts/candidates/pwb-state1-amendment/IMPACT-LEDGER.md` | governance package | 0 | 0 | 1 | — |
| `.syzygy/governance/contracts/candidates/pwb-state1-amendment/REVIEW-BRIEF.md` | governance package | 0 | 0 | 1 | — |
| `.syzygy/governance/contracts/candidates/pwb-state1-amendment/SEMANTIC-DELTA.md` | governance package | 0 | 0 | 2 | — |
| `AGENTS.md` | root page | 0 | 0 | 1 | — |

Counts are occurrences of the full identifier per file.

## Implementation sites, for the bead that follows adoption

Read at the baseline; line numbers are for that commit only.

- `apps/three-surface-poc/src/polaris.ts` — emits the per-claim tuple span
  and the per-unit non-authority attributes; gains the scope element, the
  shared-value hoist per item table and the one-evaluation assertion.
- `apps/three-surface-poc/src/polaris-narrative.ts` — narrative units carry
  the two attributes; may hoist them to the enclosing section.
- `apps/three-surface-poc/src/polaris-parity-sweep.test.ts` — `leafMarkers`
  (line 110) reads every claim's attributes from the leaf; the claim-tuple
  extraction (lines 415–423) joins eight fields per claim. It gains its own
  expansion of the inheritance rule before `compareMultisets`, keeping one
  tuple per rendered claim.
- `apps/three-surface-poc/src/polaris-epistemic-tuples.test.ts` —
  `TUPLE_FIELDS` (line 83) and the claim-tuple regular expression (line 94)
  assume every field on the span; the evaluation-id checks at lines 231–233
  assume it on every claim. Both gain expansion.
- `apps/three-surface-poc/src/pwb-mutation-sweep.ts` — gains the
  `scope-hidden` mutant per marker class (a scope value that hides one
  member's differing value) beside missing/duplicated/changed/collapsed/
  wrong-evaluation.
- `apps/three-surface-poc/src/polaris-authority-sweep.test.ts`,
  `polaris-presentation-route.test.ts`, `polaris-narrative.test.ts` — read
  the two attributes per unit; gain expansion or assert the scope.
- `packages/three-surface-poc-core/src/project-shape-model.ts` — the
  machine-form tuple emission is unchanged by design; listed because it
  cites the clauses.

## Merge and effect boundary

Merging this package to main changes no authority: the manifest rows hash
bytes that are not in the tree, the builder refuses `--apply` without
`--at-adoption`, and CG-7h keeps binding the 2026-09-05 package. The owner
phrase in `OWNER-DECISION-PACKET.md` is registered in
`scripts/check_governance.py` so that a stale copy of its argument fails
CG-7d and CG-7e before the act exists.
