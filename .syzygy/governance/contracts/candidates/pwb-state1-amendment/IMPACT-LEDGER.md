# Impact ledger — PWB state-(1) amendment

> **Candidate review input — never authority.** This ledger records the
> CC-REV-2 disposition of the complete discovered amendment population. It
> grants no effect and does not replace the signed artifacts it names.

Baseline: `bef7f8d23fe63df5150f1ce8fac5bf5d7d3d79e7`

## Population and method

Population sources were the eleven signed PWB artifacts, fixed-string searches
for `PWB-REQ-005`, `PWB-REQ-020`, `PWB-REQ-022`, `state (2)`, `state-(2)`,
`verifiable owner-act provenance`, `unverifiable`, and the performed
general-trusted-bootstrap PWB manifest, followed by direct dependency and
current-state routing inspection.

The complete disposition population is 35 rows: 11 signed PWB artifacts, 9
lifecycle/generator/checker artifacts, 6 candidate amendment artifacts, 6
historical evidence classes and 3 parent/current-state classes. Every row has
one disposition.

## Signed PWB package — 11 of 11

| Artifact | Disposition | Reason |
|---|---|---|
| `.openspec.yaml` | no semantic change; rebind | Schema and creation identity remain correct; indivisible sign-off package still binds it. |
| `proposal.md` | amend | State-(2)-only provenance wording and stale candidate/sign-off posture change. |
| `design.md` | amend | Admission, judgment, exact-state rendering, no-fallback and accepted-risk design change. |
| `specs/polaris-project-wide-butlers-model/spec.md` | amend | Complete PWB-REQ-005/020/022 blocks and warrants change. |
| `CAPABILITY-COVERAGE.md` | amend | Input, admission, judgment and refusal obligations change. |
| `CONTRACT-COVERAGE.md` | regenerate | Effective counts and all nested signed digests change. |
| `CONTRACT-COVERAGE-REPAIR-DELTA.md` | amend | Stale state-(2)-only dispositions are superseded and new requirement coverage is recorded. |
| `GOVERNING-DEPENDENCIES.md` | regenerate | New RFC3-16 subclause and owner-direction warrants enter the union. |
| `contract-coverage-matrix/RFC-0001-0003.md` | amend header | Label signed base snapshot and route current effective semantics through the repair overlay. |
| `contract-coverage-matrix/RFC-0004-0006.md` | amend header | Remove the stale claim that base dispositions reflect current warrants. |
| `contract-coverage-matrix/RFC-0007-0009.md` | amend header | Use the same explicit base/effective-matrix contract for fresh-reader consistency. |

## Lifecycle, generation and validation — 9 of 9

| Artifact | Disposition | Reason |
|---|---|---|
| `tasks.md` | amend; unsigned | Add superseding sign-off, effect-act, implementation and exhaustive state/invalid-arm gates. |
| `scripts/build_polaris_project_wide_spec_dependencies.py` | run; code no impact | Existing generator consumes changed warrants. |
| `scripts/build_polaris_project_wide_contract_coverage.py` | run and self-test; code no impact unless review changes counts contract | Existing overlay mechanism validates the changed effective matrix. |
| `scripts/build_pwb_state1_amendment_manifest.py` | create and mutation-test | Own the closed eleven-row population and exact digests; reject path or byte drift. |
| `scripts/check_governance.py` | amend and mutation-test | Performed 2026-09-01 nested PWB rows must become historical after a lawful superseding act, not be compared forever to current paths. |
| `scripts/build_general_trusted_bootstrap_transaction.py` | amend and self-test | Performed transaction generation must verify frozen act-time subjects without trying to regenerate them from superseding current paths. |
| `PROJECT-STATUS.md` | no edit before sign-off | Must continue to state state-(2)-only signed behavior; after sign-off update in the act-recording change. |
| `README.md` | no edit before sign-off | Same current-state rule; amend only after the owner act. |
| `AGENTS.md` and decisions indexes | no edit before sign-off | Operational/current-state summaries change only after sign-off; repository notes update only if durable knowledge remains. |

## Candidate amendment package — 6 of 6

| Artifact | Disposition |
|---|---|
| `SEMANTIC-DELTA.md` | create and review |
| `IMPACT-LEDGER.md` | create and independently confirm |
| `REVIEW-BRIEF.md` | create before reviewer dispatch |
| `PWB-AMENDMENT-MANIFEST.txt` | generate from the frozen eleven-artifact population |
| `CANDIDATE-REPORT.md` | generate after targeted checks and reviews |
| `OWNER-SIGNOFF-PACKET.md` | generate last from exact reviewed digests; owner act remains separate |

## Historical evidence — 6 of 6

| Class | Disposition |
|---|---|
| `POLARIS-PROJECT-WIDE-SPEC-SIGNOFF-ACT.md` and old acceptance rows | immutable historical evidence; no edit |
| `GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md` and its acceptance row | immutable historical evidence; no edit |
| `general-trusted-bootstrap-authorization/**` performed transaction bytes | immutable historical evidence; no regeneration |
| Existing `POLARIS-PROJECT-WIDE-SIGNOFF-PACKET.md` and raw PWB reviews | immutable historical evidence; no edit |
| Existing `R-GENERAL-*` reviews and transaction confirmations | immutable historical evidence; no edit |
| `contract-coverage-parts/*.md` and superseded Polaris bootstrap deltas | frozen raw/historical evidence; no edit |

## Parent and later-effect boundaries — 3 of 3

| Artifact/class | Disposition | Reason |
|---|---|---|
| Six signed `three-surface-poc-experience` artifacts | no behavioral impact | Parent parity is generic; this amendment changes only the PWB child. |
| Parent `CONTRACT-COVERAGE.md` statements that no consent/registry check runs | no impact now; mandatory re-review before body read | This amendment creates no effect artifact or runtime behavior. |
| Consent, policy, registry and walkthrough-judgment act candidates | no edit/rebind now | They are separate later effect acts and must consume the superseding signed PWB digest. |

## Result

All discovered impacts are dispositioned. The amended behavior remains
candidate, the performed transaction remains historical evidence, and no
current-state summary may present profile A as signed before the later owner
act.
