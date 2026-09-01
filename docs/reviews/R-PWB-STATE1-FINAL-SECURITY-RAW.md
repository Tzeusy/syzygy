# Raw independent final confirmation — PWB state-(1) authority boundary and security

## Review identity

- [Observed] Reviewed commit:
  `8847feef1442bf55fd5276a73248d3c58409e4db`.
- [Observed] Reviewed manifest:
  `.syzygy/governance/contracts/candidates/pwb-state1-amendment/PWB-AMENDMENT-MANIFEST.txt`.
- [Observed] Manifest SHA-256:
  `14a84abadf0ba96d968e99bd5b60302895e8a44e6e005b4d2fc76345e7863b1e`.
- [Observed] Baseline: `bef7f8d23fe63df5150f1ce8fac5bf5d7d3d79e7`.
- [Observed] Review class: final fresh authority-boundary and security
  confirmation of the repaired candidate bytes.
- [Observed] Desired verdict supplied: no.
- [Observed] The worktree was clean at the exact reviewed commit before this raw
  review was written. The manifest digest matched both the worktree file and
  `git show` of the committed file. Independent worktree and committed-object
  sweeps each found 11 rows, 11 matching subject digests and 0 mismatches; the
  row population is codepoint-sorted.

## Findings

No new findings.

- BLOCKER: 0
- MAJOR: 0
- MINOR: 0

## Prior security-finding dispositions

- [Observed] `R-PWB-STATE1-SECURITY-RAW.md` reported no findings. Its positive
  conclusions were rechecked against this exact commit rather than inherited.
- [Observed] Finding 1, BLOCKER, from
  `R-PWB-STATE1-SECURITY-CONFIRMATION-RAW.md` is **CLOSED**. The repaired
  requirement now closes every previously omitted act-record identity,
  provenance-state and state-(1)-record semantic and counts the another-human
  and non-human owner failures separately.

### Independent denominator recomputation

[Observed] The common owner-act denominator is **55** cases for one act:

- eight RFC3-16(b) fields other than owner attribution, each with missing,
  malformed and wrong-but-present cases: `8 × 3 = 24`;
- owner attribution: missing, malformed, another human and a non-human
  principal: `4`;
- evaluation association: act-record identity missing, malformed or wrong but
  present, plus pairing to a different authority artifact: `4`;
- provenance-state input: missing, malformed and well-formed outside the
  two-state vocabulary: `3`;
- false substitutes: attribution-only, commit/tag-only, specification sign-off,
  machine submission and agent assertion: `5`;
- lifecycle: stale, expired, superseded and revoked: `4`;
- provenance-state mechanics: unselected state (1), state (1) with non-absent
  A1 identity, and claimed state (2) with failed, unavailable or indeterminate
  correlation: `5`; and
- state-(1) record semantics: exact owner phrase missing, malformed or
  mismatched, and recording commit/tag missing, malformed or mismatched: `6`.

The arithmetic is `24 + 4 + 4 + 3 + 5 + 4 + 5 + 6 = 55`.

[Observed] The PWB-REQ-005 admission-invalid denominator is **195**:

- the 55 common cases applied independently to consent, policy and registry
  acts: `55 × 3 = 165`;
- consent-specific observing-project, configured-repository and observation-
  class fields: `3 × 3 = 9`;
- policy-owning-project and policy-version fields: `2 × 3 = 6`; and
- registry governance-home, project, repository, read-only-authority and
  empty-write-surface fields: `5 × 3 = 15`.

The arithmetic is `165 + 9 + 6 + 15 = 195`.

[Observed] The PWB-REQ-022 present-invalid denominator is **84**:

- the exact 55-case common owner-act population: `55`;
- five run-record fields, each missing, malformed and wrong but present:
  `5 × 3 = 15`;
- four judgment fields, each missing, malformed and wrong but present:
  `4 × 3 = 12`; and
- the two wrong-governance-home cases: `2`.

The arithmetic is `55 + 15 + 12 + 2 = 84`. The no-run-record and no-judgment
cases are the separate **2 absent cases**; neither invents a verdict.

### Closure of declared inputs and state-(1) record semantics

- [Observed] PWB-REQ-005's declared authority-artifact identity and digest map
  to RFC3-16(b)'s stable-identity and exact-digest cases. Project, act type,
  owner, instant, scope, supersession/revocation and A1 identity-or-absence are
  all independently closed in the 28-case binding-field group.
- [Observed] Act-record identity is separately closed by missing, malformed,
  wrong-but-present and wrong-artifact association cases. Provenance state is
  separately closed by its three input cases and five state-mechanics cases.
- [Observed] RFC3-16(c)'s exact state-(1) owner phrase, exact content digest,
  act record and recording commit/tag are all closed: phrase and recording
  context contribute six explicit cases, while digest and act-record identity
  are closed by the binding and association groups. These checks expressly
  validate trusted-record semantics and do not claim to establish attendance.
- [Observed] PWB-REQ-022's execution-record identity is closed in the run-record
  group; its judgment artifact identity/digest, act-record identity, act
  type/scope, provenance state and A1 identity-or-absence are closed by the
  inherited exact 55-case population. Surface version, evaluation identity,
  mode, traversed paths, verdict, rationale, judging party, exact run reference
  and both governance homes are independently closed by the remaining 29
  present-invalid cases.
- [Observed] Another-human and non-human principals occupy two independent
  owner-attribution cases. Neither is hidden inside one counted “wrong owner”
  fixture.

## Authority and security confirmation

- [Observed] PWB-REQ-005 admits all eight valid consent/policy/registry state
  triples: `(1,1,1)`, `(1,1,2)`, `(1,2,1)`, `(2,1,1)`, `(1,2,2)`, `(2,1,2)`,
  `(2,2,1)` and `(2,2,2)`. Every one of the 195 invalid cases requires zero
  body reads, project-model Unknown, the RFC3-16(a) contradiction and visible
  retention of the invalid state.
- [Observed] A record claiming state (2) with failed, unavailable or
  indeterminate correlation is invalid and never falls back to state (1), in
  both PWB-REQ-005 and PWB-REQ-022.
- [Observed] State (1) is effective but never called independently verified.
  Both requirements prescribe exactly:
  `Owner-trusted only; same-tree forgeable from Syzygy's perspective. Digest
  detects drift, not authorship or attendance.` PWB-REQ-020 requires the human
  and machine marker multisets to preserve exact state, disclosure and
  multiplicity at one evaluation.
- [Observed] The state-(1) independent-oracle clauses say they verify record
  semantics and disclosure without claiming to prove human attendance. A file,
  stored attribution, commit/tag, specification signature, machine submission
  or agent assertion cannot substitute for the human act. The accepted
  same-tree-forgeability risk is disclosed rather than converted into an
  independence claim.
- [Observed] The body-read conjunction remains exact-pair and exact-class,
  observing-project-policy governed, governance-homed, read-only and
  empty-write. Repository containment, inert parsing, bounded resources,
  fail-closed secret handling, inherited authentication, no observed-code
  execution and no provider egress are not disjoined by the provenance change.
- [Observed] Owner acts remain warrants only. They are not evidence that a read
  occurred, secret screening succeeded, admitted content is secret-free, a
  derived claim is true, a walkthrough occurred or comprehension succeeded.
  The walkthrough execution record and owner judgment remain separate.
- [Observed] Each of the 84 present-invalid judgment cases requires exact
  `verdict-unlawful`, Unknown-never-met and the RFC3-16(a) contradiction. The
  two absent cases remain Unknown-never-met without a fabricated verdict.
- [Observed] Later A1 correlation may change only a later evaluation; it does
  not rewrite the state under which an earlier read or judgment took effect.
- [Observed] The signed PWB-REQ-005 and PWB-REQ-022 clauses require a
  fail-then-restore mutation for every one of the 195 admission-invalid and 84
  present-invalid judgment instances, plus the two absence predicates and the
  exact-state, disclosure, no-fallback and prior-history predicates.
  PWB-REQ-020 separately requires missing, duplicated, changed, collapsed and
  wrong-evaluation parity-marker mutations. The mutation obligations are in the
  exact signed specification digest in this manifest.
- [Observed] The proposal, design, semantic delta, owner direction and review
  brief all keep the package candidate and indivisible. It creates no consent,
  policy, registry or judgment act and grants no repository-body read,
  implementation, write, egress, execution, deployment, release, recovery or
  mission authority. A later owner act must bind all eleven subjects together;
  separate effect-specific acts and implementation authorization remain
  prerequisites.

## Validation evidence

- [Observed] `python3 scripts/build_pwb_state1_amendment_manifest.py --check`
  reported `PWB amendment manifest matches regeneration — 11 artifacts`;
  `--selftest` reported that the 11-row population, determinism, byte mutation
  and path mutation hold.
- [Observed] The dependency check reported `17 requirement(s)`. The effective
  coverage check reported `324 clauses represented`; its self-test reported
  exact IDs/dispositions, columns, family/total/repair counts, warrants and
  determinism hold.
- [Observed] `npx openspec validate polaris-project-wide-butlers-model
  --strict` reported the change valid.
- [Observed] The performed trusted-bootstrap transaction check reported 30
  contract paths, 5 historical PWB paths and 5 owner-act rows frozen and valid.
  Its self-test reported `10 transaction mutations, 0 failing`.
- [Observed] `python3 scripts/check_governance.py --selftest` reported `178
  fixtures, 0 failing`, including successor-manifest population, one-sided act,
  conflicting digest, current-drift and exact-row mutation cases.
- [Observed] The ordinary governance run reported `32 OK, 19 WARN, 1 FAIL (52
  checks)`. CG-7h examined 76 predicates and reported the expected five current
  PWB digest mismatches against the immutable 2026-09-01 historical manifest
  while no superseding owner act exists. This is the candidate's fail-closed
  posture, not evidence that the amendment is effective.
- [Unknown] No implementation or runtime effect is reviewed or proven here.
  Body-read behavior, screening, authentication, parity and walkthrough results
  still require separately authorized implementation and retained evidence.

## Verdict and owner gate

**VERDICT: CONFIRM**

**OWNER SIGN-OFF MAY BE OFFERED** for commit
`8847feef1442bf55fd5276a73248d3c58409e4db` at manifest
`14a84abadf0ba96d968e99bd5b60302895e8a44e6e005b4d2fc76345e7863b1e`, once
the other required independent review classes are complete. This confirmation
is not owner sign-off, does not make the candidate effective and grants none of
the downstream authorities listed above.
