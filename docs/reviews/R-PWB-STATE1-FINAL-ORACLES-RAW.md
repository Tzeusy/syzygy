# Final independent deterministic-oracle and public-interface confirmation

## Exact subject

- [Observed] Reviewed commit:
  `8847feef1442bf55fd5276a73248d3c58409e4db`.
- [Observed] Baseline:
  `bef7f8d23fe63df5150f1ce8fac5bf5d7d3d79e7`.
- [Observed] Reviewed manifest:
  `.syzygy/governance/contracts/candidates/pwb-state1-amendment/PWB-AMENDMENT-MANIFEST.txt`.
- [Observed] Manifest SHA-256:
  `14a84abadf0ba96d968e99bd5b60302895e8a44e6e005b4d2fc76345e7863b1e`.
- [Observed] The manifest contains eleven codepoint-sorted paths, including
  unchanged `.openspec.yaml`; every row digest matches both the worktree and
  the exact reviewed commit.
- [Observed] `HEAD` resolved to the reviewed commit, `git diff
  8847feef...HEAD` was empty, and the worktree was clean before this raw review
  file was added. No reviewed subject was edited during confirmation.
- [Observed] Desired verdict supplied: no.

## Prior-finding dispositions

### Prior oracle Finding 1 — closed

[Observed] The prior BLOCKER found that the invalid population was not closed
over RFC3-16(b)'s nine fields and the requirement-specific authority fields.
The repaired PWB-REQ-005 now defines a literal seven-group common population,
three authority-specific populations and an exact total; PWB-REQ-022 reuses
only the common population and adds its own exact run, judgment and home
populations.

[Observed] Independent enumeration produced:

| Population | Independent expansion | Result |
|---|---:|---:|
| RFC3-16(b) binding fields | eight ordinary fields x three arms, plus owner missing, malformed, another-human and non-human | 28 |
| Evaluation association | act-record identity missing, malformed and wrong; wrong authority pairing | 4 |
| Provenance-state input | missing, malformed and out-of-vocabulary | 3 |
| False substitutes | tree attribution, commit/tag, spec sign-off, machine submission, agent assertion | 5 |
| Lifecycle | stale, expired, superseded, revoked | 4 |
| State mechanics | state (1) not explicit; state (1) with A1 present; three failed state-(2) correlation arms | 5 |
| State-(1) record semantics | owner phrase and recording context, each missing, malformed and mismatched | 6 |
| **Common total** | **28 + 4 + 3 + 5 + 4 + 5 + 6** | **55** |

[Observed] The 55 identifiers were unique. The admission population is
`55 x 3` acts plus consent `3 x 3`, policy `2 x 3` and registry `5 x 3`:
`165 + 9 + 6 + 15 = 195`, with 195 unique identifiers and residual zero.
The requirement states `Every case above, no "other invalid" bucket.`

[Observed] The judgment population is `55 + (5 x 3) + (4 x 3) + 2 = 84`
present-invalid cases, with 84 unique identifiers and residual zero. The two
absent cases, no run record and no judgment, are separate and disjoint from
the present-invalid set. The requirement does not assign either absent case a
verdict.

### Prior oracle Finding 2 — closed

[Observed] The prior BLOCKER found an undefined third-channel export
obligation. `PWB-REQ-005`, `PWB-REQ-020`, `PWB-REQ-022`, proposal, design,
semantic delta and tasks now contain no export interface or export obligation.
The one `export` occurrence among the eleven signed subjects is an unchanged
base-matrix summary of RFC7-33.c4; it is `unknown-uncovered`, does not name a
PWB interface and does not enter any current PWB requirement oracle.

[Observed] PWB-REQ-020 now bounds parity to the human Polaris surface and the
machine answer. It requires equivalent multisets from the same evaluation,
order-insensitive and multiplicity-preserving comparison, both denominators
and zero differences. The comparator extracts both channels separately and
imports neither production vocabulary nor rendering code.

### Prior oracle Finding 3 — closed

[Observed] The prior DEFECT found that mutation evidence was required outside
the signed package but not by its signed requirements. The signed current
PWB-REQ-005 requires a fail-then-restore mutation for each of the 195 invalid
instances and separate state, disclosure, no-fallback and historical-state
mutations. Signed PWB-REQ-022 requires the same for each of 84 present-invalid
cases, each absent case and the additional state/disclosure/history
predicates. Signed PWB-REQ-020 requires missing, duplicate, changed, collapsed
and wrong-evaluation mutations for every fact, authority-state,
judgment-state and disclosure marker class. Each obligation requires the
independent comparator or test to fail before restoration and retained
evidence.

### Later security Finding 1 — closed

[Observed] The later security BLOCKER identified missing and malformed
act-record-identity and provenance-state cases, incomplete state-(1) owner
phrase/recording-context cases, and a collapsed wrong-owner count. The current
55-case common population closes all three arms for act-record identity and
provenance state, all six state-(1) phrase/context arms, and separately counts
another-human and non-human principals. PWB-REQ-022 applies that exact common
population to the judgment act.

[Observed] State-(1) record checks are expressly limited to trusted record
semantics. Both admission and judgment oracle-independence clauses state that
they do not claim to prove human attendance. Every attendance occurrence in
the current behavioral/amendment text either states that the digest cannot
prove it, forbids treating a tag as proof, or makes that oracle limitation
explicit. No state-(1) attendance claim remains.

## Exact parity and oracle confirmation

- [Observed] All eight valid consent/policy/registry state triples are required:
  the independent product `{1,2}^3` contains eight combinations.
- [Observed] The two normative state-(1) disclosure literals in PWB-REQ-005
  and PWB-REQ-022 decode to the same exact literal value:
  `Owner-trusted only; same-tree forgeable from Syzygy's perspective. Digest
  detects drift, not authorship or attendance.`
- [Observed] PWB-REQ-005 requires exact per-authority state and disclosure
  equality between human and machine channels. PWB-REQ-022 requires the same
  for judgments. PWB-REQ-020 exhausts the combined fact, authority-state,
  judgment-state and disclosure multiset at one evaluation.
- [Observed] Admission fixtures, hard-coded expectations and the read spy live
  outside the observer and import neither its validator nor state vocabulary.
  Judgment fixtures and expected values live outside the surface and
  provenance validator and import neither production validator nor state
  vocabulary. The parity comparator extracts the two wire channels
  independently and imports no production rendering code or vocabulary.
- [Observed] Any admission-invalid case requires zero body reads, Unknown and
  the RFC3-16(a) contradiction. Every judgment-present-invalid case requires
  exact `verdict-unlawful` and Unknown-never-met. Failed, unavailable and
  indeterminate state-(2) correlation never falls back to state (1).
- [Observed] Acts remain warrants only. The requirements deny that an act,
  digest, correlation or run record proves a read, screening, secret-freedom,
  truth, comprehension or success, and later correlation cannot rewrite an
  earlier evaluation's provenance.

## Read-only validation evidence

- [Observed] `python3 scripts/build_pwb_state1_amendment_manifest.py --check`
  reported `PWB amendment manifest matches regeneration — 11 artifacts`.
- [Observed] Its self-test passed the 11-row population, determinism,
  byte-mutation and path-mutation predicates.
- [Observed] The dependency check reported 17 requirements. The coverage check
  reported 324 clauses represented, and its self-test passed exact IDs and
  dispositions, columns, family/total/repair counts, warrants and determinism.
- [Observed] `npx openspec validate polaris-project-wide-butlers-model
  --strict` reported the change valid.
- [Observed] The performed trusted-bootstrap transaction check reported 30
  contract paths, 5 historical PWB paths and 5 owner-act rows frozen and
  valid. Its ten mutation cases had zero failures.
- [Observed] `python3 scripts/check_governance.py --selftest` reported 178
  fixtures and zero failing.
- [Observed] The ordinary governance run examined 76 CG-7h predicates and
  failed on exactly the five expected current-PWB digest differences against
  the immutable 2026-09-01 historical manifest while no successor owner act
  exists. Overall output was `32 OK, 19 WARN, 1 FAIL (52 checks)`. This is the
  required pre-act fail-closed candidate posture, not evidence that the
  amendment is effective.
- [Observed] `git diff --check bef7f8d...8847fee` produced no output.

## New findings

- BLOCKER: 0
- MAJOR: 0
- MINOR: 0

No new findings.

## Verdict and owner gate

**VERDICT: CONFIRM**

[Inferred] The exact repaired bytes close the three prior oracle findings and
the later security denominator finding for the deterministic-oracle and
public-interface review class. The 55/195/84+2 populations are closed,
independent and signed; human/machine parity is exact and bounded; no PWB
export interface or state-(1) attendance claim remains.

**THIS REVIEW CLASS NO LONGER BLOCKS OFFERING OWNER SIGN-OFF** for commit
`8847feef1442bf55fd5276a73248d3c58409e4db` at manifest
`14a84abadf0ba96d968e99bd5b60302895e8a44e6e005b4d2fc76345e7863b1e`,
provided every other review class required by `REVIEW-BRIEF.md` independently
confirms these same frozen bytes. This confirmation performs no owner act,
grants no effect or implementation authority and does not make the candidate
effective.
