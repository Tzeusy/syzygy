# Impact ledger — PWB scoped epistemic attributes

> **Candidate — binds nothing.** Companion to `SEMANTIC-DELTA.md`.

Baseline: commit `a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d`; none of the
eleven behavior subjects or the RFC-0007 module changes between it and the
commit that carries this draft.

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

At the commit that carries this draft the same two sweeps, over every
tracked file at that commit — this package's own files, its retained
reviews, the estimate script and record, and the register row included —
return **94 files** over **1,232**. The 14 files beyond the baseline 80
are enumerated here so the figure can be re-derived rather than re-read;
none is an implementation site, and the table below stays the baseline
table:

- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/IMPACT-LEDGER.md`
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/OWNER-DECISION-PACKET.md`
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/REVIEW-BRIEF.md`
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/SEMANTIC-DELTA.md`
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/proposed/GOVERNING-DEPENDENCIES.md.patch`
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/proposed/design.md.patch`
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/proposed/spec.md.patch`
- `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`
- `docs/evidence/pwb-laneb-strict-scope-estimate-2026-09-14.json`
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-2-RAW.md`
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-3-RAW.md`
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-4-RAW.md`
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-RAW.md`
- `scripts/estimate_pwb_scoped_attributes_saving.py`

## Classes

| class | files | disposition |
|---|---|---|
| signed package | 6 | six of the eleven manifest rows cite the identifiers; separately, three of the eleven rows change under the patches (`spec.md`, `design.md`, and `GOVERNING-DEPENDENCIES.md`, whose source-digest line and `RFC7-34` row follow the spec) and eight are byte-identical, the coverage files among them restating clause titles that stay true |
| unbound spec companion | 3 | not in the manifest; `tasks.md` takes implementation rows after adoption, the two coverage parts restate parity findings that remain true |
| other openspec change | 1 | cites PWB-REQ-014/020 as the parity floor the generator inherits; the floor is unchanged in the machine form |
| renderer / model | 8 | implementation sites after adoption: the claim element, the narrative unit and the shared model's tuple emission; no change while candidate |
| oracle / test | 9 | implementation sites after adoption: each oracle gains its own scope expansion and the sweep gains the scope-hidden and over-asserting-scope mutant classes |
| script | 1 | the state-(1) recorder names PWB-REQ-020 in its docstring; historical, untouched |
| docs / plans | 5 | plans and the funnel/pursuit records that led here; the funnel's draft delta is superseded by this package and says so by date |
| retained review | 23 | raw reviewer output; never edited (CC-REV-6) |
| evidence record | 17 | frozen evidence; never edited; a lane B measurement is a new record in the lane A shape |
| decision record | 3 | performed acts and rulings; never edited |
| governance package | 3 | the performed 2026-09-02 package; never edited |
| root page | 1 | AGENTS.md's parity guardrail (per tuple, never per id) stays true; expansion keeps one tuple per claim |

Sum: 80. The last column takes three values: **must** (a file the
implementation bead after both acts must change), `model` (the shared
model whose emission is deliberately unchanged, listed because it decides
what the renderer may scope), and `—` (no change is expected of the file by
this package or its implementation; if the bead finds one, the ledger is
wrong and is corrected before the bead closes). This package itself changes
no file outside its own directory, the governance checks, the CI battery
and the register.

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
| `apps/three-surface-poc/src/polaris-accessibility.ts` | renderer / model | 0 | 0 | 1 | **must** |
| `apps/three-surface-poc/src/polaris-copy.ts` | renderer / model | 1 | 1 | 0 | **must** |
| `apps/three-surface-poc/src/polaris-narrative.ts` | renderer / model | 0 | 3 | 0 | — |
| `apps/three-surface-poc/src/polaris.ts` | renderer / model | 3 | 2 | 0 | **must** |
| `apps/three-surface-poc/src/routes.ts` | renderer / model | 0 | 1 | 0 | — |
| `packages/three-surface-poc-core/src/project-shape-model.ts` | renderer / model | 4 | 0 | 1 | model |
| `apps/three-surface-poc/src/polaris-authority-sweep.test.ts` | oracle / test | 0 | 1 | 0 | — |
| `apps/three-surface-poc/src/polaris-epistemic-tuples.test.ts` | oracle / test | 2 | 0 | 0 | **must** |
| `apps/three-surface-poc/src/polaris-first-reading.test.ts` | oracle / test | 0 | 0 | 2 | — |
| `apps/three-surface-poc/src/polaris-narrative.test.ts` | oracle / test | 0 | 2 | 0 | — |
| `apps/three-surface-poc/src/polaris-parity-sweep.test.ts` | oracle / test | 0 | 0 | 3 | **must** |
| `apps/three-surface-poc/src/polaris-presentation-route.test.ts` | oracle / test | 0 | 2 | 0 | — |
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

- `apps/three-surface-poc/src/polaris.ts` — emits the per-claim tuple span;
  gains the scope element and the shared-value hoist per item table, under
  the strict rule (a field is hoisted only when every claim in the table
  has that value in the machine answer). The per-unit non-authority
  attributes it emits are unchanged.
- `apps/three-surface-poc/src/polaris-copy.ts` — the claim-states lede
  (`label.claim-states`) restates the inheritance rule for the reader.
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
  member's differing value) and the `over-asserting-scope` mutant (a scope
  value one member does not have, the member carrying its own) beside
  missing/duplicated/changed/collapsed/wrong-evaluation.
- `apps/three-surface-poc/src/polaris-accessibility.ts` — the PWB-REQ-016
  checker; gains its own expansion of the rule, or the assertion that every
  scope's text precedes the claims it covers in reading order.
- `packages/three-surface-poc-core/src/project-shape-model.ts` — the
  machine-form tuple emission is unchanged by design; listed because it
  cites the clauses.

Not implementation sites, though the first draft listed them:
`polaris-narrative.ts`, `polaris-authority-sweep.test.ts`,
`polaris-presentation-route.test.ts` and `polaris-narrative.test.ts` read
or emit the two PWB-REQ-014 attributes per unit, and PWB-REQ-014 is no
longer amended.

## RFC7-33 citers (the contract patch)

The contract patch touches one clause, so a second sweep with its own
denominator, same population and predicate as above: `RFC7-33\b` by Python
`re`, and `git grep -l -F RFC7-33`, agree on **82 files** over **1,232**
(the ledger itself, the P-68 register row, the spec and dependency patches
that carry PWB-REQ-007's warrant line, and the four retained reviews of
this package are members). None quotes the paragraph the patch inserts
(the paragraph is new). RFC7-33's opening sentence gains a parenthetical;
the sweep `grep -F "on the rendered unit**, served identically"` over the
same population returns **13 files** (review 3, F3; earlier drafts said
two), every one enumerated here, and none of them is a citer that would go
false — the frozen records quote the sentence as it stood, which stays
true as history, and the package's own files quote it as the before-text:

- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/IMPACT-LEDGER.md` — this ledger (the sweep literal)
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/SEMANTIC-DELTA.md` — the delta's before/after quotation
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/proposed/contract/RFC-0007-rendering-and-surface.md.patch` — the contract patch's context lines
- `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md` — its candidate mirror
- `.syzygy/governance/contracts/candidates/round-2026-08g/reviews/RD-60-capability-1-outline-exercise-RAW.md` — a retained round review quoting the clause as it stood
- `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md` — the module
- `docs/evidence/polaris-generator-rfc7-coverage-2026-09-12.json` — frozen generator coverage evidence carrying the clause text as it stood
- `docs/evidence/polaris-generator-rfc7-coverage-v2-2026-09-12.json` — frozen generator coverage evidence carrying the clause text as it stood
- `docs/evidence/polaris-generator-rfc7-coverage-v3-2026-09-12.json` — frozen generator coverage evidence carrying the clause text as it stood
- `docs/evidence/polaris-generator-rfc7-coverage-v4-2026-09-12.json` — frozen generator coverage evidence carrying the clause text as it stood
- `docs/evidence/polaris-generator-rfc7-coverage-v5-2026-09-12.json` — frozen generator coverage evidence carrying the clause text as it stood
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-2-RAW.md` — the second retained review of this package
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-4-RAW.md` — the fourth retained review of this package

| class | files | disposition |
|---|---|---|
| Capability 1 code | 5 | honours RFC7-33 per unit; the permission is opt-in and Capability 1 does not take it; no change |
| accepted contract module | 4 | `rfcs/RFC-0007/rendering-and-surface.md` is the amendment subject of the contract act and changes only by that act; the RFC-0007 README, the narrative module and the RFC-0008 module cite the clause and are untouched |
| candidate contract mirror | 4 | each must equal its accepted module byte for byte; the contract patch applies to the rendering module's mirror exactly as to the module, the other three are untouched |
| contract history | 2 | takes the successor entry when the contract act is performed; unchanged until then |
| decision record | 2 | performed administrations; never edited |
| docs | 2 | coverage and design notes citing the clause; unchanged, none quotes the amended paragraph |
| evidence record | 6 | frozen evidence; never edited |
| generated index or candidate record | 10 | generated views and candidate records that cite the clause identifier; regenerated or unchanged, none quotes the amended paragraph |
| generated register | 1 | regenerated by `build_directive_register.py`; RFC7-33's own definition line is unchanged, every RFC-0007 clause defined after the insert point moves |
| openspec change | 16 | specifications that warrant on RFC7-33; the permission is opt-in and none of these takes it, so their text stays true |
| pending register | 1 | the P-68 row; edited only when the owner rules |
| retained review | 18 | raw reviewer output; never edited |
| round record | 3 | historical round material; never edited |
| script | 1 | this package's builder, which names the clause |
| this package | 7 | the candidate package's own prose and patches, which cite the clause they amend |

Sum: 82.

| file | class |
|---|---|
| `.syzygy/governance/contracts/candidates/04-CLAUSE-MIGRATION-MATRIX.md` | generated index or candidate record |
| `.syzygy/governance/contracts/candidates/05-CONTRACT-INDEX.yaml` | generated index or candidate record |
| `.syzygy/governance/contracts/candidates/CAPABILITY-1-CHARTER.yaml` | generated index or candidate record |
| `.syzygy/governance/contracts/candidates/CAPABILITY-1-GENERATED-VIEWS.md` | generated index or candidate record |
| `.syzygy/governance/contracts/candidates/FIRST-OPENSPEC-SEQUENCE.md` | generated index or candidate record |
| `.syzygy/governance/contracts/candidates/POLARIS-TRUSTED-BOOTSTRAP-OBSERVATION-SEMANTIC-DELTA.md` | generated index or candidate record |
| `.syzygy/governance/contracts/candidates/SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md` | generated index or candidate record |
| `.syzygy/governance/contracts/candidates/SURFACE-CLAUSE-ROUTING-MATRIX.md` | generated index or candidate record |
| `.syzygy/governance/contracts/candidates/TASK-ROUTER.md` | generated index or candidate record |
| `.syzygy/governance/contracts/candidates/history/RFC-0007-history.md` | contract history |
| `.syzygy/governance/contracts/candidates/history/rev9-rfcs/RFC-0007-polaris-intent-surface.md` | contract history |
| `.syzygy/governance/contracts/candidates/matrix-rows/RFC-0007-rows.md` | generated index or candidate record |
| `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/IMPACT-LEDGER.md` | this package |
| `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/OWNER-DECISION-PACKET.md` | this package |
| `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/REVIEW-BRIEF.md` | this package |
| `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/SEMANTIC-DELTA.md` | this package |
| `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/proposed/GOVERNING-DEPENDENCIES.md.patch` | this package |
| `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/proposed/design.md.patch` | this package |
| `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/proposed/spec.md.patch` | this package |
| `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/README.md` | candidate contract mirror |
| `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md` | candidate contract mirror |
| `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md` | candidate contract mirror |
| `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/accounting-reconciliation-and-release.md` | candidate contract mirror |
| `.syzygy/governance/contracts/candidates/round-2026-08/reviews/RB-4-contract-compaction-RAW.md` | retained review |
| `.syzygy/governance/contracts/candidates/round-2026-08b/matrix-parts/RFC-0007-0011.md` | round record |
| `.syzygy/governance/contracts/candidates/round-2026-08b/reviews/RC-5-rfc-openspec-boundary-RAW.md` | retained review |
| `.syzygy/governance/contracts/candidates/round-2026-08c/reviews/RD-2-human-clarity-RAW.md` | retained review |
| `.syzygy/governance/contracts/candidates/round-2026-08d/reviews/RD-10-human-view-RAW.md` | retained review |
| `.syzygy/governance/contracts/candidates/round-2026-08d/reviews/RD-19-wave-b-RAW.md` | retained review |
| `.syzygy/governance/contracts/candidates/round-2026-08e/WAVE-B-SEMANTIC-DELTA.md` | round record |
| `.syzygy/governance/contracts/candidates/round-2026-08e/reviews/RD-32-wave-b-RAW.md` | retained review |
| `.syzygy/governance/contracts/candidates/round-2026-08f/CAPABILITY-1-CONTEXT-ROUTE-REPORT.md` | round record |
| `.syzygy/governance/contracts/candidates/round-2026-08f/CAPABILITY-1-SPEC-OUTLINE-EXERCISE-RAW.md` | retained review |
| `.syzygy/governance/contracts/candidates/round-2026-08f/reviews/RD-53-capability-1-task-route-RAW.md` | retained review |
| `.syzygy/governance/contracts/candidates/round-2026-08g/reviews/RD-60-capability-1-outline-exercise-RAW.md` | retained review |
| `.syzygy/governance/contracts/rfcs/RFC-0007/README.md` | accepted contract module |
| `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md` | accepted contract module |
| `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md` | accepted contract module |
| `.syzygy/governance/contracts/rfcs/RFC-0008/accounting-reconciliation-and-release.md` | accepted contract module |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | pending register |
| `.syzygy/governance/decisions/launch-gate/ADMINISTRATION-2026-08-18-CAPABILITY-1.json` | decision record |
| `.syzygy/governance/decisions/launch-gate/ADMINISTRATION-2026-08-18-CAPABILITY-1.md` | decision record |
| `DIRECTIVE-REGISTER.md` | generated register |
| `docs/design/POLARIS-GENERATOR-RFC7-COVERAGE.md` | docs |
| `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` | docs |
| `docs/evidence/polaris-generator-non7-current-binding-bridge-2026-09-12.json` | evidence record |
| `docs/evidence/polaris-generator-rfc7-coverage-2026-09-12.json` | evidence record |
| `docs/evidence/polaris-generator-rfc7-coverage-v2-2026-09-12.json` | evidence record |
| `docs/evidence/polaris-generator-rfc7-coverage-v3-2026-09-12.json` | evidence record |
| `docs/evidence/polaris-generator-rfc7-coverage-v4-2026-09-12.json` | evidence record |
| `docs/evidence/polaris-generator-rfc7-coverage-v5-2026-09-12.json` | evidence record |
| `docs/reviews/R-POLARIS-PROJECT-WIDE-SPEC-CONFIRMATION-2-RAW.md` | retained review |
| `docs/reviews/R-POLARIS-PROJECT-WIDE-SPEC-CONFIRMATION-3-RAW.md` | retained review |
| `docs/reviews/R-POLARIS-PROJECT-WIDE-SPEC-CONFIRMATION-4-RAW.md` | retained review |
| `docs/reviews/R-PWB-LIVE-EXACT-HEAD-TRUTH-RAW.md` | retained review |
| `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-2-RAW.md` | retained review |
| `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-3-RAW.md` | retained review |
| `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-4-RAW.md` | retained review |
| `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-RAW.md` | retained review |
| `docs/reviews/R-PWB-STATE1-FINAL-ORACLES-RAW.md` | retained review |
| `openspec/changes/polaris-manifesto-generation/DESIGN-ACCEPTANCE.md` | openspec change |
| `openspec/changes/polaris-manifesto-generation/GOVERNING-DEPENDENCIES.md` | openspec change |
| `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md` | openspec change |
| `openspec/changes/polaris-manifesto-understanding-amendment/GOVERNING-DEPENDENCIES.md` | openspec change |
| `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md` | openspec change |
| `openspec/changes/polaris-project-wide-butlers-model/CONTRACT-COVERAGE-REPAIR-DELTA.md` | openspec change |
| `openspec/changes/polaris-project-wide-butlers-model/GOVERNING-DEPENDENCIES.md` | openspec change |
| `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0007-0009.md` | openspec change |
| `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-parts/RFC-0007-0009.md` | openspec change |
| `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` | openspec change |
| `openspec/changes/project-registration-and-honest-shape-visibility/CONTRACT-COVERAGE.md` | openspec change |
| `openspec/changes/project-registration-and-honest-shape-visibility/GOVERNING-DEPENDENCIES.md` | openspec change |
| `openspec/changes/project-registration-and-honest-shape-visibility/specs/project-registration-and-honest-shape-visibility/spec.md` | openspec change |
| `openspec/changes/three-surface-poc-experience/CONTRACT-COVERAGE.md` | openspec change |
| `openspec/changes/three-surface-poc-experience/GOVERNING-DEPENDENCIES.md` | openspec change |
| `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md` | openspec change |
| `packages/cap1-core/src/distinction.ts` | Capability 1 code |
| `packages/cap1-core/src/epistemic.ts` | Capability 1 code |
| `packages/cap1-core/src/parity.ts` | Capability 1 code |
| `packages/cap1-daemon/src/routes-human.ts` | Capability 1 code |
| `packages/cap1-daemon/src/routes-machine.ts` | Capability 1 code |
| `scripts/build_pwb_scoped_attributes_amendment.py` | script |

## Files that name the module by path (what a contract act regenerates)

An identifier sweep cannot find the artifacts that cite the module by
**path**, and those are the ones a performed contract act must regenerate
in the same change. Over the same population, `git grep -l -F` and Python
`re` for `rfcs/RFC-0007/rendering-and-surface.md` agree on **50 files**:

- `.syzygy/governance/contracts/candidates/ACTIVE-CONTRACT-MANIFEST.txt`
- `.syzygy/governance/contracts/candidates/CAPABILITY-1-GENERATED-VIEWS.md`
- `.syzygy/governance/contracts/candidates/CONTEXT-BUDGET-REPORT.md`
- `.syzygy/governance/contracts/candidates/CONTRACT-DEPENDENCY-INDEX.md`
- `.syzygy/governance/contracts/candidates/TASK-ROUTER.md`
- `.syzygy/governance/contracts/candidates/fixtures/context-selection-8-openspec-authoring.md`
- `.syzygy/governance/contracts/candidates/general-trusted-bootstrap-authorization/CONTRACT-AMENDMENT-MANIFEST.txt`
- `.syzygy/governance/contracts/candidates/general-trusted-bootstrap-authorization/IMPACT-LEDGER.md`
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/IMPACT-LEDGER.md`
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/SEMANTIC-DELTA.md`
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/proposed/contract/RFC-0007-rendering-and-surface.md.patch`
- `.syzygy/governance/contracts/candidates/reviews/rev10-boundary-review.md`
- `.syzygy/governance/contracts/candidates/round-2026-08/CONTEXT-COMPILER-FIXTURE-REPORT.md`
- `.syzygy/governance/contracts/candidates/round-2026-08/reviews/RB-5-context-compiler-RAW.md`
- `.syzygy/governance/contracts/candidates/round-2026-08b/reviews/RC-4-contract-semantics-RAW.md`
- `.syzygy/governance/contracts/candidates/round-2026-08b/reviews/RC-5-rfc-openspec-boundary-RAW.md`
- `.syzygy/governance/contracts/candidates/round-2026-08b/reviews/RC-6-context-compiler-RAW.md`
- `.syzygy/governance/contracts/candidates/round-2026-08c/reviews/RD-2-human-clarity-RAW.md`
- `.syzygy/governance/contracts/candidates/round-2026-08d/reviews/LAUNCH-GATE-ADMINISTRATION-2026-08-09-RAW.md`
- `.syzygy/governance/contracts/candidates/round-2026-08e/WAVE-B-SEMANTIC-DELTA.md`
- `.syzygy/governance/contracts/candidates/round-2026-08e/reviews/RD-27-wave-b-RAW.md`
- `.syzygy/governance/contracts/candidates/round-2026-08e/reviews/RD-32-wave-b-RAW.md`
- `.syzygy/governance/contracts/candidates/round-2026-08e/reviews/RD-32b-wave-b-RAW.md`
- `.syzygy/governance/contracts/candidates/round-2026-08e/reviews/RD-32c-wave-b-RAW.md`
- `.syzygy/governance/contracts/candidates/round-2026-08f/CAPABILITY-1-CONTEXT-ROUTE-REPORT.md`
- `.syzygy/governance/contracts/candidates/round-2026-08f/reviews/RD-53-capability-1-task-route-RAW.md`
- `.syzygy/governance/contracts/candidates/round-2026-08g/reviews/RD-60-capability-1-outline-exercise-RAW.md`
- `.syzygy/governance/contracts/candidates/round-2026-08i/reviews/RD-70-p41-p42-confirming-RAW.md`
- `.syzygy/governance/contracts/candidates/scripts/build_task_router.py`
- `.syzygy/governance/contracts/candidates/wave-manifests/WAVE-B-MANIFEST.txt`
- `DIRECTIVE-REGISTER.md`
- `docs/evidence/polaris-generator-adoption-clone-validation-2026-09-12.json`
- `docs/evidence/polaris-generator-approval-offer-2026-09-12.json`
- `docs/evidence/polaris-generator-approval-tool-validation-2026-09-12.json`
- `docs/evidence/polaris-generator-concrete-offer-validation-2026-09-12.json`
- `docs/evidence/polaris-generator-rfc7-coverage-2026-09-12.json`
- `docs/evidence/polaris-generator-rfc7-coverage-v2-2026-09-12.json`
- `docs/evidence/polaris-generator-rfc7-coverage-v3-2026-09-12.json`
- `docs/evidence/polaris-generator-rfc7-coverage-v4-2026-09-12.json`
- `docs/evidence/polaris-generator-rfc7-coverage-v5-2026-09-12.json`
- `docs/evidence/polaris-pipeline-synthetic-verification-2026-09-13.json`
- `docs/evidence/polaris-understanding-adoption-clone-validation-2026-09-13.json`
- `docs/reviews/R-POLARIS-PROJECT-WIDE-SPEC-CONFIRMATION-1-RAW.md`
- `docs/reviews/R-POLARIS-PROJECT-WIDE-SPEC-REVIEW-RAW.md`
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-2-RAW.md`
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-3-RAW.md`
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-4-RAW.md`
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-RAW.md`
- `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-parts/RFC-0007-0009.md`
- `scripts/build_pwb_scoped_attributes_amendment.py`

Of these, three go stale when the patch is applied [Observed, review 2:
patch applied to both mirrors in a scratch copy, battery run]:
`ACTIVE-CONTRACT-MANIFEST.txt` (CG-7a, the module's digest row),
`DIRECTIVE-REGISTER.md` (`build_directive_register.py --check`, clause
lines after the insert point) and
`fixtures/context-selection-8-openspec-authoring.md` (CG-18, a stated
packet digest and word count). The rest are retained reviews, frozen
evidence, performed manifests that hash the *current* bytes and stay true
as history, generated views the recorder's post-apply battery re-checks,
and this package. The recorder's `--check` runs the whole published battery
after applying; nothing is assumed clean.

## Merge and effect boundary

Merging this package to main changes no authority: the manifest rows hash
bytes that are not in the tree, the builder refuses `--apply` without
`--at-adoption`, the contract patch is applied by no script at all (its
act's recorder does not yet exist), and CG-7h keeps binding the 2026-09-05
package while the accepted RFC-0007 stays as accepted. The owner
phrase in `OWNER-DECISION-PACKET.md` is registered in
`scripts/check_governance.py` so that a stale copy of its argument fails
CG-7d and CG-7e before the act exists.
