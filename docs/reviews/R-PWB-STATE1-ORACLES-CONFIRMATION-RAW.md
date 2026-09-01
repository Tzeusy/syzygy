# Independent deterministic-observation, oracle and public-interface confirmation

## Exact repaired subject

- [Observed] Reviewed commit:
  `8c3b8cb3199efefd580ead08c8866877b7878799`.
- [Observed] Baseline: `bef7f8d23fe63df5150f1ce8fac5bf5d7d3d79e7`.
- [Observed] Repaired manifest:
  `.syzygy/governance/contracts/candidates/pwb-state1-amendment/PWB-AMENDMENT-MANIFEST.txt`.
- [Observed] Manifest SHA-256:
  `f5088ca4de9073e55ca11aa061cec73aa6cb478808cd4be95f58ea348204a520`.
- [Observed] The manifest contains the exact sorted eleven-path population,
  including unchanged `.openspec.yaml`; an independent `sha256sum -c` pass
  verified all eleven row digests.
- [Observed] The worktree was clean at the exact repaired commit before this
  raw confirmation file was added. No subject file was edited during review.

## Checks performed

- [Observed] `python3 scripts/build_pwb_state1_amendment_manifest.py --check`
  passed: `PWB amendment manifest matches regeneration — 11 artifacts`.
- [Observed]
  `python3 scripts/build_pwb_state1_amendment_manifest.py --selftest` passed
  its 11-row population, determinism, byte-mutation and path-mutation
  predicates.
- [Observed] The dependency generator `--check`, contract-coverage generator
  `--check`, and contract-coverage generator `--selftest` passed. The checked
  populations were 17 requirements and 324 accepted clauses; the generated
  effective matrix reports 622 consequences.
- [Observed] `openspec validate polaris-project-wide-butlers-model --strict`
  passed.
- [Observed]
  `python3 scripts/build_general_trusted_bootstrap_transaction.py --check`
  passed with 30 contract paths, 5 historical PWB paths and 5 owner-act rows.
  Its `--selftest` passed 10 transaction mutations, 0 failing.
- [Observed] `python3 scripts/check_governance.py --selftest` passed 178
  fixtures, 0 failing.
- [Observed] The full `python3 scripts/check_governance.py` run examined 825
  tracked files and reported 32 OK, 19 WARN and 1 FAIL. The sole failing family
  was the expected pre-act CG-7h result: 76 predicates examined and 5 findings,
  one for each current PWB coverage artifact that differs from the performed
  2026-09-01 historical manifest while no successor owner act exists. This is
  fail-closed candidate behavior, not evidence that the amendment is effective.
- [Observed] `git diff --check` from baseline
  `bef7f8d23fe63df5150f1ce8fac5bf5d7d3d79e7` through repaired commit
  `8c3b8cb3199efefd580ead08c8866877b7878799` reported no whitespace error.

## Prior-finding dispositions

### 1. CLOSED — The invalid-arm population is now mechanically closed over the owner-act fields

- [Observed] PWB-REQ-005 defines a closed 159-case table at
  `spec.md:231-249`, with no residual “other invalid” bucket. It names all nine
  RFC3-16(b) fields and independently requires missing, malformed and
  wrong-but-present treatment, including another-human and non-human owner
  fixtures, a future instant, wrong supersession/revocation target, wrong
  act-record identity, wrong artifact association and mismatched A1 identity.
- [Observed] Independent arithmetic reproduces the table: the common per-act
  population is `27 + 2 + 5 + 4 + 5 = 43`; three acts contribute 129 cases;
  the consent, policy and registry fields contribute `9 + 6 + 15 = 30`; total
  admission-invalid population is `159`.
- [Observed] Every invalid admission case is normatively bound to zero body
  reads, project-model Unknown and the RFC3-16(a) contradiction at
  `spec.md:251-253`. All eight valid state triples are exercised separately at
  `spec.md:265-280`.
- [Observed] PWB-REQ-022 reuses the exact 43-case owner-act population, then
  adds 15 run-record cases, 12 judgment-field cases and 2 governance-home
  cases: `43 + 15 + 12 + 2 = 72` present-invalid cases. It separately names
  the two absent cases at `spec.md:875-886`.
- [Observed] Each of the 72 present-invalid judgment cases must record exact
  `verdict-unlawful`, render Unknown-never-met and mint or retain the
  contradiction; either absent case must render Unknown-never-met without an
  invented verdict (`spec.md:888-896`).

### 2. CLOSED — The undefined export channel was removed

- [Observed] PWB-REQ-005, PWB-REQ-020 and PWB-REQ-022 now define only the
  human surface and machine answer as the bounded parity channels
  (`spec.md:269-280`, `spec.md:759-790`, `spec.md:898-912`).
- [Observed] A fixed-string and case-insensitive export sweep across the live
  signed specification, proposal, design, semantic delta and implementation
  tasks found zero undefined export-channel occurrences. The historical raw
  REVISE review remains unchanged and is the only reviewed-finding record that
  retains the old wording.
- [Observed] PWB-REQ-020 independently extracts both channels, compares
  order-insensitive multiplicity-preserving multisets, reports both
  denominators and fails on missing, duplicate, changed, collapsed or
  wrong-evaluation markers (`spec.md:763-790`). This closes the reachable
  two-channel interface rather than leaving a third unnamed interface.

### 3. CLOSED — Fail-then-restore mutation proof is now signed

- [Observed] PWB-REQ-005 requires a fail-then-restore mutation for every one of
  the 159 invalid instances and separate mutations of exact state, exact
  disclosure, no-fallback and prior-evaluation history, with retained evidence
  (`spec.md:281-286`). Digest, scope and A1 identity/absence mutations are
  already members of the 159-case population.
- [Observed] PWB-REQ-022 requires mutations for every one of the 72
  present-invalid cases, each of the two absent cases, exact state, disclosure,
  no-fallback and history, all failing before restoration with retained
  evidence (`spec.md:913-918`).
- [Observed] PWB-REQ-020 requires missing, duplicated, changed, collapsed and
  wrong-evaluation mutations for each fact, authority-state, judgment-state
  and disclosure marker class; the independent comparator must fail before
  restoration and report both channel denominators for every run
  (`spec.md:777-780`).
- [Observed] These obligations are inside the manifest-bound specification at
  SHA-256 `1074078e6882664f2dd30a3a99b15562d6d9fff5359c1b252d7f107e1a579f75`;
  they are no longer confined to unsigned semantic-delta or task prose.

## Oracle independence and human-machine parity

- [Observed] PWB-REQ-005 and PWB-REQ-022 require hard-coded expected tables
  and controlled fixtures outside the production validator and state
  vocabulary. PWB-REQ-005 additionally places the authority fixtures and read
  spy outside the observer (`spec.md:274-280`, `spec.md:907-912`).
- [Observed] Both requirements expressly limit the state-(1) oracle to record
  semantics and disclosure and prohibit claiming that it proves human
  attendance.
- [Observed] The exact same-tree-forgeability disclosure occurs twice in the
  signed specification, once in each changed gate, and PWB-REQ-020 includes
  every authorization state, judgment state and disclosure in its two-channel
  multiset population.
- [Observed] Failed, unavailable or indeterminate state-(2) correlation remains
  invalid without state-(1) fallback, and later correlation does not rewrite
  the earlier read or judgment provenance.

## New findings

[Observed] No new BLOCKER, DEFECT, WARNING or NOTE arose within this bounded
deterministic-observation, oracle and public-interface confirmation.

## Verdict

**VERDICT: CONFIRM**

[Inferred] The exact repaired bytes close all three findings from
`R-PWB-STATE1-ORACLES-RAW.md`: both invalid populations now terminate at
mechanically declared denominators and fail-closed outcomes, the unsupported
export channel is gone, and the independent mutation-sensitive human/machine
oracles are signed into the eleven-artifact package.

**OWNER SIGN-OFF MAY BE OFFERED on commit
`8c3b8cb3199efefd580ead08c8866877b7878799` at manifest SHA-256
`f5088ca4de9073e55ca11aa061cec73aa6cb478808cd4be95f58ea348204a520`.**

This verdict confirms the assigned oracle/public-interface repair only. It
does not perform owner sign-off, make the candidate effective, authorize
implementation or grant any consent, observation, read, write, egress,
execution, deployment, release, recovery or mission authority.
