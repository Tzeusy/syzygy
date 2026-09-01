# Independent raw review — PWB state-(1) amendment transaction

CONFIRM WITH EXCEPTIONS

## Review identity

- [Observed] Exact reviewed commit: `f31f8315ecd75d83dd73ebd6739f003c241e8584`.
- [Observed] Declared baseline: `bef7f8d23fe63df5150f1ce8fac5bf5d7d3d79e7`.
- [Observed] Exact reviewed manifest:
  `.syzygy/governance/contracts/candidates/pwb-state1-amendment/PWB-AMENDMENT-MANIFEST.txt`.
- [Observed] Manifest SHA-256:
  `657197d697abd3e502847085351741f403a8b7a9a93e10c12764fbfc72288ff5`.
- [Observed] Initial inspection found the worktree clean at the reviewed
  commit. No subject artifact was edited during this review; later concurrent
  review outputs are outside the reviewed manifest.

## Findings

### Blocker / revise severity

None.

### Non-blocking exception — advisory severity

- [Observed] `git diff --check bef7f8d..f31f831` reports one new blank line at
  EOF in `REVIEW-BRIEF.md` and one in `SEMANTIC-DELTA.md`. These are mechanical
  whitespace warnings outside the eleven-artifact owner manifest; they do not
  change the amendment semantics or weaken an authority boundary. Editing
  either reviewed input would nevertheless retire this review and require a
  fresh review of the new commit.

## Authority and behavioral review

- [Observed] PWB-REQ-005 admits the complete two-by-two-by-two population of
  consent, observing-project secret policy and adapter-registry provenance:
  eight all-valid triples across state (1) and state (2). It rejects every
  named invalid arm before a body read, requires zero read calls, renders the
  project model Unknown, and retains the RFC3-16(a) contradiction. A record
  claiming state (2) with failed, unavailable or indeterminate correlation is
  invalid and has no state-(1) fallback.
- [Observed] Each authority act is required through RFC3-16(a) and bound under
  RFC3-16(b); the independent oracle checks every RFC3-16(b) field, including
  exact subject identity/digest, project/scope, act type, provenance state and
  A1 audit identity or explicit absence. State (1) requires explicit human
  selection and explicit audit-record absence. Tree attribution, a commit,
  tag, machine submission, agent assertion or specification sign-off cannot
  substitute for the human act.
- [Observed] The exact state-(1) disclosure is normative and byte-identical in
  PWB-REQ-005 and PWB-REQ-022:
  `Owner-trusted only; same-tree forgeable from Syzygy's perspective. Digest detects drift, not authorship or attendance.`
  Both requirements demand identical disclosure across the human surface,
  machine answer and export. PWB-REQ-020 exhausts the authority/judgment state
  and disclosure marker populations with an order-insensitive,
  multiplicity-preserving comparator. Only state (2) may be called
  independently verified.
- [Observed] Exact-pair/class consent, the observing project's own policy,
  governance-homed registry, read-only/empty-write scope, repository
  containment, secret exclusion, authentication inheritance and
  no-observed-code-execution floors remain conjunctive. No weakened alternative
  path appears in proposal, design, requirement, coverage or task surfaces.
- [Observed] PWB-REQ-022 keeps the kernel walkthrough execution record and the
  owner judgment separate. Absence invents no verdict and remains
  Unknown-never-met. A present invalid judgment records exact
  `verdict-unlawful`, retains the contradiction and remains Unknown-never-met.
  Valid state (1) and state (2) judgments preserve their exact state; later
  correlation does not rewrite the provenance of an earlier judgment.
- [Observed] Acts are consistently described as warrants rather than evidence
  that reading, screening, secret freedom, truth, comprehension or effect
  success occurred. This preserves VIS-1, VIS-2 and RFC3-16(c)'s evidence
  boundary.
- [Inferred] A fresh reader can restate the amendment as follows: profile A
  changes only the signed PWB child gates and their parity obligations so a
  genuine, exact-scope human act may be effective in state (1) or state (2);
  it does not remove any effect-specific gate and does not itself perform an
  effect.

## CC-REV-2 and coverage closure

- [Observed] The impact ledger contains the declared 35-row disposition
  population: 11 signed PWB artifacts, 9 lifecycle/generator/checker rows, 6
  candidate-package rows, 6 historical-evidence classes and 3 parent/effect
  boundary rows. Every changed proposal, design, requirement, capability
  coverage, governing dependency, base-matrix interpretation, effective
  matrix consequence and test obligation is dispositioned in the same logical
  change. Current-state summaries are correctly held for the later act-recording
  change rather than made to claim unsigned behavior now.
- [Observed] The base/overlay contract is truthful. The three signed matrix
  files are explicitly labeled base snapshots whose embedded counts describe
  base bytes only. The repair overlay names 80 replacement rows superseding 71
  unique base rows. Independent recomputation gives `613 - 71 + 80 = 622`
  effective consequences: 137 covered, 237 Unknown-uncovered and 248 believed
  not applicable. The repair-only totals independently reproduce 61 covered,
  16 Unknown-uncovered and 3 believed not applicable. No believed-N/A row is
  presented as an owner-reviewed N/A judgment.
- [Observed] Capability coverage independently reproduces 27 obligations: 21
  covered and 6 lawfully out of scope, with zero Unknown/unresolved. The
  generated dependency union reports 17 requirements and 96 distinct
  authorities and includes RFC3-16(a)/(b)/(c) plus
  `PWB-STATE1-AMENDMENT-DIR-2026-09-02` only on the three affected
  requirements.
- [Observed] `build_polaris_project_wide_contract_coverage.py` treats the base
  rows as immutable inputs and constructs the effective set by deleting only
  named superseded IDs and adding the repair rows. Its checker rejects missing
  base IDs, duplicate repair IDs, clause/ID mismatches, invalid dispositions,
  stale embedded counts and covered rows whose requirement warrants omit the
  clause. Its self-test passed.

## Exact package and historical/current transaction integrity

- [Observed] The generated successor manifest has exactly 11 unique,
  codepoint-sorted paths. Independent `sha256sum -c` verification passed for
  all 11 rows, including unchanged `.openspec.yaml`. Generator check and
  mutation self-test reported: `PWB amendment manifest matches regeneration —
  11 artifacts` and `11-row population, determinism, byte mutation and path
  mutation hold`.
- [Observed] Historical acts, performed manifests, parent signed artifacts,
  raw reviews and raw coverage parts have zero diff from the baseline. The
  performed general trusted-bootstrap outer manifest remains exactly
  `1885a323c659364f98e81cdf04479cebfecf5b22d350928d046ebb5b7c5268f6`;
  its nested PWB manifest remains exactly
  `5cda673c604f298cc45d05ca358b2cc410b6a74f1664c55f4f1056ce8c1f45ea`.
  The append-only aggregate act record, dedicated general-bootstrap act and
  original PWB sign-off act also match their baseline bytes exactly.
- [Observed] `build_general_trusted_bootstrap_transaction.py --check` validates
  the performed transaction as frozen act-time history: 30 contract paths, 5
  historical PWB paths and 5 owner-act rows. Its ten mutation cases all pass,
  including rejection of historical nested/outer mutations and acceptance of
  superseding current PWB bytes without rewriting performed history.
- [Observed] The current-state verifier activates a successor only when both
  `ACCEPTANCE-ACT-RECORD.md` and the dedicated
  `PWB-STATE1-AMENDMENT-ACT.md` record the latest exact manifest digest. It then
  requires the closed 11-path order and current digest match. Candidate bytes
  alone do not activate supersession. Governance self-test mutation fixtures
  cover unsigned successor, one-record-only, conflicting records, valid
  successor, post-successor drift, 10/12 rows, duplicate/reordered paths and an
  escaping path; all 178 governance fixtures pass.
- [Observed] Before the successor act, the full governance run is intentionally
  `32 OK, 19 WARN, 1 FAIL`. CG-7h examines 76 predicates and reports exactly
  five findings: the five current PWB coverage paths differ from the immutable
  2026-09-01 act-time rows. This is the correct candidate-only fail-closed
  state. CG-7d separately warns that the new sign-off phrase has zero
  quotations; no act or owner packet exists yet.

## Targeted command evidence

- [Observed] `npx openspec validate polaris-project-wide-butlers-model --strict`
  — `Change 'polaris-project-wide-butlers-model' is valid`.
- [Observed] Dependency generator check — `17 requirement(s)`.
- [Observed] Contract-coverage generator check — `324 clauses represented`;
  self-test passed exact IDs/dispositions, columns, family/total/repair counts,
  warrants and determinism.
- [Observed] PWB manifest check/self-test — 11 artifacts; all 11 independent
  digest checks passed.
- [Observed] General trusted-bootstrap transaction check/self-test — frozen and
  valid; `10 transaction mutations, 0 failing`.
- [Observed] Governance self-test — `178 fixtures, 0 failing`.

## Candidate status and authority boundary

- [Observed] The semantic delta, proposal, design, impact ledger, review brief
  and manifest consistently say the amendment is candidate and binds nothing
  before a later exact-digest human owner act. The current signed
  state-(2)-only behavior remains authoritative until then.
- [Observed] The candidate creates no consent, secret-policy approval,
  adapter-registry adoption, walkthrough judgment, body-read authority,
  implementation authorization, write, egress, execution, deployment,
  release, recovery or mission authority. Even after sign-off, separate
  effect-specific acts and separate implementation authorization remain
  mandatory.
- [Observed] The six signed parent `three-surface-poc-experience` artifacts are
  unchanged. Parent parity remains generic and the amendment is confined to
  the PWB child.
- [Unknown] This review does not establish that the other independently
  required review classes have completed, and it does not establish that any
  later owner act has occurred.

## Verdict and owner gate

**EXACT VERDICT: CONFIRM WITH EXCEPTIONS**

**OWNER SIGN-OFF MAY BE OFFERED: YES, from this review class, at manifest
SHA-256 `657197d697abd3e502847085351741f403a8b7a9a93e10c12764fbfc72288ff5`,
provided every other required independent review class is recorded against the
same frozen commit and manifest before the packet is offered.** The owner act
must bind all eleven rows together or none, and the aggregate and dedicated
act records must both record the exact performed digest. This review does not
perform that act.
