# Fresh independent confirmation — PWB state-(1) transaction and CC-REV-2

**VERDICT: REVISE**

## Review identity

- [Observed] Exact reviewed commit:
  `8c3b8cb3199efefd580ead08c8866877b7878799`.
- [Observed] Declared baseline:
  `bef7f8d23fe63df5150f1ce8fac5bf5d7d3d79e7`.
- [Observed] Exact reviewed manifest:
  `.syzygy/governance/contracts/candidates/pwb-state1-amendment/PWB-AMENDMENT-MANIFEST.txt`.
- [Observed] Manifest SHA-256:
  `f5088ca4de9073e55ca11aa061cec73aa6cb478808cd4be95f58ea348204a520`.
- [Observed] No desired verdict was supplied. The worktree was initially clean
  at the reviewed commit. A concurrent reviewer later added
  `docs/reviews/R-PWB-STATE1-ORACLES-CONFIRMATION-RAW.md`; it is outside the
  eleven-artifact manifest and was not used to decide this verdict. No reviewed
  subject was edited during this confirmation.

## Findings

### BLOCKER — The claimed closed invalid populations undercount the owner field

- [Observed] PWB-REQ-005 declares exactly 159 independently decided invalid
  cases and defines a nine-field RFC3-16(b) group as missing, malformed and
  wrong-but-present for each field, counted as `27 × 3 acts = 81`
  (`spec.md:231-246`). In that same row, the owner-attribution wrong-but-present
  case is required to include both another human and a non-human principal
  (`spec.md:238`). Those are two independently required semantic inputs, not
  one input instance. The row therefore describes 28 field cases per act, not
  27.
- [Observed] Retaining both required owner variants makes the common per-act
  population `28 + 2 + 5 + 4 + 5 = 44`, not 43
  (`spec.md:238-249`). Across the three PWB-REQ-005 authorities, the closed
  admission-invalid population is therefore `44 × 3 + 30 = 162`, not 159.
- [Observed] PWB-REQ-022 imports the same alleged 43-case common population and
  therefore reports 72 present-invalid cases (`spec.md:875-885`). With both
  owner variants retained, its population is `44 + 15 + 12 + 2 = 73`.
- [Inferred] Treating both inputs as one counted case would make “independently
  decided cases,” per-case mutation evidence, and the reported denominator
  disagree about the actual fixture population. Dropping either variant would
  leave the signed oracle short of a distinct wrong-owner or non-human
  authority failure. The checker cannot resolve this semantic counting defect;
  it validates only the authored table and generated artifacts.
- [Observed] The incorrect denominators propagate into the review brief
  (`REVIEW-BRIEF.md:29-31,44-47`), semantic delta
  (`SEMANTIC-DELTA.md:72-79`), design, capability coverage, specification and
  unsigned implementation tasks. Acceptance criteria 1, 7, 9 and 15 are
  therefore not met on the frozen bytes.

Minimum repair: make the independently executed fixture population, table
rows, totals and mutation obligations agree. If both currently required owner
variants remain, the natural totals are 162 admission-invalid and 73
present-invalid judgment cases. Propagate the selected exact population
through every invalidated candidate and signed artifact, regenerate the
eleven-row manifest, and obtain fresh confirmation of the new exact commit and
manifest.

### Other severities

- MAJOR: 0
- MINOR: 0

## Prior finding disposition

- [Observed] The prior undefined-export finding is repaired. PWB-REQ-005,
  PWB-REQ-020 and PWB-REQ-022 now bind the two actual channels, human Polaris
  and the machine answer. The review brief, semantic delta, design, capability
  coverage and tasks agree; no new export interface is invented.
- [Observed] The prior missing mutation-proof finding is repaired in signed
  requirements. PWB-REQ-005 binds fail-then-restore proof for every declared
  invalid case and the exact-state/disclosure/no-fallback/history predicates;
  PWB-REQ-020 binds missing, duplicate, changed, collapsed and
  wrong-evaluation marker mutations; PWB-REQ-022 binds every declared
  present-invalid and absent case plus state/disclosure/no-fallback/history
  mutations.
- [Observed] The prior wrong-but-present-field finding is repaired in kind:
  the table now names every RFC3-16(b) field, association, substitute,
  lifecycle and provenance mechanic. The blocker above is the remaining
  closure/count error in that repair, not a return to the former open-ended
  list.
- [Observed] The former trailing-blank-line exception is closed.
  `git diff --check bef7f8d..8c3b8cb` and
  `git diff --check f31f831..8c3b8cb` both returned no output and success.

## Exact package and CC-REV-2 closure

- [Observed] The manifest contains exactly 11 unique codepoint-sorted paths,
  including unchanged `.openspec.yaml`. Independent `sha256sum -c` verification
  passed 11 of 11 rows with zero mismatches. The manifest generator reported
  `PWB amendment manifest matches regeneration — 11 artifacts`; its self-test
  reported that the 11-row population, determinism, byte mutation and path
  mutation hold.
- [Observed] Repair propagation reaches the affected signed specification,
  design, capability coverage and generated governing-dependency union, plus
  the unsigned tasks, semantic delta and review brief. Seven manifest subjects
  remain byte-identical because their semantics were not invalidated:
  `.openspec.yaml`, proposal, contract-coverage manifest, repair overlay and
  the three base matrices. Their current digests nevertheless reverify inside
  the indivisible 11-row package.
- [Observed] The impact ledger has 35 dispositions: 11 signed artifacts, 9
  lifecycle/generator/checker artifacts, 6 candidate-package artifacts, 6
  historical-evidence classes and 3 parent/effect boundary classes. No
  discovered row is left without a disposition. This structural CC-REV-2
  accounting is sound apart from the semantic denominator blocker above.
- [Observed] Independent matrix parsing reproduced 613 base consequences; 80
  repair rows superseding 71 unique base rows; and 622 effective consequences,
  partitioned into 137 covered, 237 Unknown-uncovered and 248 believed not
  applicable. Repair-only counts are 61 covered, 16 Unknown-uncovered and 3
  believed not applicable. No believed-N/A row is presented as owner-reviewed.
- [Observed] Independent capability-coverage parsing reproduced 27 rows: 21
  covered, 6 lawfully out of scope and 0 Unknown/unresolved. The dependency
  generator reports 17 requirements and the generated artifact reports 96
  distinct authorities, with the amendment direction attached only to
  PWB-REQ-005, PWB-REQ-020 and PWB-REQ-022.

## Historical/current transaction integrity

- [Observed] Existing historical acts, the append-only aggregate act record,
  the performed general-bootstrap transaction directory, the old PWB sign-off
  packet, raw coverage parts, superseded bootstrap deltas and the six parent
  Three-Surface POC signed artifacts have zero changed paths from the baseline.
  The three `R-PWB-STATE1-*-RAW.md` files are newly recorded prior-review
  outputs in the repaired commit, not edits to an earlier historical file.
- [Observed] The performed general trusted-bootstrap outer manifest remains
  bound at
  `1885a323c659364f98e81cdf04479cebfecf5b22d350928d046ebb5b7c5268f6`;
  its historical five-row PWB manifest remains bound at
  `5cda673c604f298cc45d05ca358b2cc410b6a74f1664c55f4f1056ce8c1f45ea`.
- [Observed] `build_general_trusted_bootstrap_transaction.py --check` reports
  30 frozen contract paths, 5 historical PWB paths and 5 owner-act rows valid.
  Its 10 mutation cases pass, including rejection of mutated historical and
  outer manifests and acceptance of superseding current PWB bytes without
  rewriting act-time history.
- [Observed] `check_governance.py --selftest` reports 178 fixtures and 0
  failures. The successor-gate fixtures reject unsigned, one-record-only,
  conflicting-digest, post-successor-drift, 10-row, 12-row, duplicate,
  reordered and escaping-path cases, and accept the exact valid 11-row case at
  89 predicates.

## Candidate status and authority boundary

- [Observed] No dedicated `PWB-STATE1-AMENDMENT-ACT.md` exists and no
  `SIGN OFF PWB STATE-(1) AMENDMENT: <digest>` act is recorded. The semantic
  delta, proposal, design, impact ledger, review brief and manifest all label
  the amendment candidate and preserve the currently signed state-(2)-only
  behavior until a later exact-digest human owner act.
- [Observed] The ordinary governance run reports `32 OK, 19 WARN, 1 FAIL` over
  52 checks. CG-7h examines 76 predicates and reports exactly five current-path
  mismatches against the immutable 2026-09-01 historical PWB rows. CG-7d
  reports zero quotations of the successor phrase. This is the intended
  fail-closed unsigned-candidate posture, not evidence of an effective act.
- [Observed] Matching aggregate and dedicated successor records are required
  before current-byte authority can switch to the exact 11-row successor.
  Candidate bytes or a one-sided/conflicting act cannot activate it.
- [Observed] The candidate creates no consent, secret-policy approval,
  adapter-registry adoption, walkthrough judgment, body-read authority,
  implementation authorization, write, egress, execution, deployment,
  release, recovery or mission authority. State (1) remains explicitly
  owner-trusted and same-tree forgeable; only state (2) may be called
  independently verified; acts remain warrants rather than effect-success
  evidence.

## Targeted command evidence

- [Observed] `npx openspec validate polaris-project-wide-butlers-model --strict`
  — `Change 'polaris-project-wide-butlers-model' is valid`.
- [Observed] Dependency generator check and self-test — 17 requirements;
  qualified-parent success/failure and determinism hold.
- [Observed] Coverage generator check and self-test — 324 accepted clauses
  represented; exact IDs/dispositions, columns, family/total/repair counts,
  warrants and determinism hold.
- [Observed] Manifest check/self-test and independent digest verification — 11
  artifacts, 11 of 11 rows valid.
- [Observed] Performed-transaction check/self-test — 30 contract paths, 5
  historical PWB paths, 5 owner-act rows; 10 mutations, 0 failing.
- [Observed] Governance self-test — 178 fixtures, 0 failing.

## Exact verdict and owner gate

**EXACT VERDICT: REVISE**

**OWNER SIGN-OFF MAY BE OFFERED: NO.** The exact package at commit
`8c3b8cb3199efefd580ead08c8866877b7878799` and manifest SHA-256
`f5088ca4de9073e55ca11aa061cec73aa6cb478808cd4be95f58ea348204a520`
does not yet carry a self-consistent closed invalid-case denominator. Repair,
regenerate and obtain fresh independent confirmation before any owner packet is
offered. This review performs no act and grants no downstream authority.
