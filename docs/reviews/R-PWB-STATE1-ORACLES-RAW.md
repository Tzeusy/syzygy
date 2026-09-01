# Independent deterministic-observation, oracle and public-interface review

## Exact subject

- [Observed] Reviewed commit: `f31f8315ecd75d83dd73ebd6739f003c241e8584`.
- [Observed] Baseline: `bef7f8d23fe63df5150f1ce8fac5bf5d7d3d79e7`.
- [Observed] Reviewed manifest:
  `.syzygy/governance/contracts/candidates/pwb-state1-amendment/PWB-AMENDMENT-MANIFEST.txt`.
- [Observed] Manifest SHA-256:
  `657197d697abd3e502847085351741f403a8b7a9a93e10c12764fbfc72288ff5`.
- [Observed] The manifest contains the exact sorted eleven-path population,
  including unchanged `.openspec.yaml`; its row digests match the reviewed
  files.
- [Observed] The worktree was clean at the reviewed commit before this raw
  review file was added. No subject file was edited during review.

## Checks performed

- [Observed] `python3 scripts/build_pwb_state1_amendment_manifest.py --check`
  passed: `PWB amendment manifest matches regeneration — 11 artifacts`.
- [Observed] `python3 scripts/build_pwb_state1_amendment_manifest.py --selftest`
  passed its 11-row population, determinism, byte-mutation and path-mutation
  predicates.
- [Observed]
  `python3 scripts/build_general_trusted_bootstrap_transaction.py --check`
  passed with 30 contract paths, 5 historical PWB paths and 5 owner-act rows.
- [Observed]
  `python3 scripts/build_general_trusted_bootstrap_transaction.py --selftest`
  passed 10 transaction mutations, 0 failing. Superseding current PWB bytes
  left performed transaction bytes unchanged; mutations of the historical PWB
  manifest and outer transaction manifest were rejected.
- [Observed] `python3 scripts/check_governance.py --selftest` passed 178
  fixtures, 0 failing, including unsigned/one-sided/conflicting successor acts,
  10/12/duplicate/reordered/escaping successor rows, and post-successor current
  drift.
- [Observed] `openspec validate polaris-project-wide-butlers-model --strict`
  passed.
- [Observed] The dependency generator `--check`, contract-coverage generator
  `--check`, and contract-coverage generator `--selftest` passed; the effective
  matrix reports 324 clauses and 622 consequences.
- [Observed] The full `python3 scripts/check_governance.py` run examined 822
  tracked files and reported 32 OK, 19 WARN and 1 FAIL. The sole failing family
  was the expected pre-act CG-7h result: 76 predicates examined and 5 findings,
  one for each current PWB coverage artifact that differs from the performed
  2026-09-01 historical manifest while no successor owner act exists. This is
  fail-closed candidate behavior, not evidence that the candidate is already
  effective.
- [Observed] `git diff --check bef7f8d...f31f831` reported only new blank lines
  at EOF in `REVIEW-BRIEF.md` and `SEMANTIC-DELTA.md`; no code or manifest-row
  whitespace error was reported.

## Findings

### 1. BLOCKER — The invalid-arm population is not closed over the nine owner-act fields

Evidence:

- [Observed] RFC3-16(b) requires every act to bind project identity, stable
  artifact identity, exact digest, act type, owner attribution, act instant,
  scope, supersession/revocation relationship, and A1 identity or explicit
  absence at
  `.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md:250-276`.
- [Observed] PWB-REQ-005's oracle says it compares every RFC3-16(b) field, but
  its invalid-arm list names missing/malformed/non-human/unattributed,
  wrong-project/repository/class/scope/type, digest mismatch, stale, expired,
  superseded and revoked at
  `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md:226-257`.
  It does not close cases for a wrong-but-present owner, wrong stable artifact
  identity, future or otherwise invalid act instant, wrong supersession target,
  wrong act-record identity, or a wrong-but-present audit identity. Several of
  those are neither missing nor malformed.
- [Observed] PWB-REQ-022 has the same gap. It names missing attribution,
  staleness, expiry, revocation, supersession and correlation failure, then
  delegates to "every invalid act arm above" at `spec.md:842-875`; it does not
  enumerate the remaining wrong-but-present RFC3-16(b) values.
- [Observed] Tasks 4.1 and 4.6 require "every named" invalid arm at
  `openspec/changes/polaris-project-wide-butlers-model/tasks.md:74-92`. They do
  not add a closed field-by-field denominator beyond the requirement prose.

Why it matters:

- [Inferred] An implementation can ignore owner identity, act instant,
  supersession target or stable act/artifact identity while satisfying every
  explicitly enumerated negative fixture. The hard-coded expected table does
  not make an unproduced case fail. That leaves the body-read and judgment gates
  vulnerable precisely at values that distinguish an exact human act from a
  plausible same-tree record.

Minimum precise repair:

- Add one closed invalid-case table derived mechanically from all nine
  RFC3-16(b) fields plus the requirement-specific consent, policy, registry,
  run and judgment fields. Give the table a reported denominator.
- Exercise every wrong-but-present value independently for each of the three
  PWB-REQ-005 authority limbs and for PWB-REQ-022, including explicit state-(1)
  with a non-absent A1 identity and state-(2) with a mismatched A1 identity.
- Require each case to decide the literal zero-read/Unknown/contradiction or
  `verdict-unlawful` outcome rather than letting "malformed" absorb distinct
  semantic failures.

### 2. BLOCKER — Export parity is required but no export interface or exhaustive export oracle is defined

Evidence:

- [Observed] PWB-REQ-005 and PWB-REQ-022 each require the exact state-(1)
  disclosure to be identical in the human surface, machine answer and export at
  `spec.md:246-261` and `spec.md:860-875`.
- [Observed] No amended artifact defines which export is in scope, how it is
  produced, its route or artifact identity, or the complete marker population
  to extract from it. The only other occurrences of `export` in the reviewed
  PWB behavior are those two observables.
- [Observed] PWB-REQ-020 quantifies only over Polaris and the machine answer at
  `spec.md:734-761`; its comparator has two channel populations, not three.
  Parent POC-REQ-020 likewise compares client-rendered facts with the machine
  answer at
  `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md:377-404`.
- [Observed] Implementation task 4.3 requires only human markers against
  `/api/poc` at `tasks.md:82-84`. It supplies no export-channel check.

Why it matters:

- [Inferred] The exact disclosure can be absent, duplicated or changed in a
  plain-text/exported rendering while the specified PWB-REQ-020 and task-4.3
  parity gates remain green. "Export" without a named reachable interface and
  denominator is not a terminating independent oracle under CC-SPEC-4.

Minimum precise repair:

- Name the exact export interface and its evaluation binding.
- Extend PWB-REQ-020 or add an equally binding oracle that independently
  extracts human, machine and export populations, reports all three
  denominators, and compares order-insensitive multiplicity-preserving tuples
  containing authority identity, state and exact disclosure.
- Add the export sweep to the signed verification obligation rather than
  leaving it only as an observable word in PWB-REQ-005/022.

### 3. DEFECT — The signed implementation obligations do not require mutation proof for the new behavior oracles

Evidence:

- [Observed] `SEMANTIC-DELTA.md:72-82` requires mutations of exact state,
  disclosure, audit identity/absence, act scope, digest, no-fallback and prior
  evaluation history.
- [Observed] The exact-digest owner package binds the eleven manifest subjects;
  `SEMANTIC-DELTA.md` and unsigned `tasks.md` are not among those eleven rows.
- [Observed] Signed PWB-REQ-005/020/022 contain concrete falsifier prose, but do
  not require temporarily injecting those defects and observing the independent
  tests fail. Unsigned task 4.2 still lists only the older source denominator,
  coverage, precedence, secret, capability-first and meta-copy mutations at
  `tasks.md:79-81`.
- [Observed] The transaction/manifest verifier mutations do run and pass, but
  they exercise package history and current-byte predicates, not the future
  body-read, judgment and three-channel disclosure oracles.

Why it matters:

- [Inferred] A tautological or coupled implementation of the future state and
  parity tests can satisfy the signed prose without demonstrated sensitivity to
  the specific regressions this amendment introduces. The semantic delta
  recognizes that risk, but the proposed exact-digest act does not bind that
  test obligation.

Minimum precise repair:

- Carry the semantic delta's mutation list into the signed requirement oracle
  or falsifier obligations, with one named mutation per protected predicate and
  recorded fail-then-restore evidence during implementation confirmation.

## Confirmed properties

- [Observed] The normative valid-state rule admits state (1) or state (2)
  independently for consent, policy and registry, so its stated valid
  population is the complete eight triples; mixed states preserve each limb's
  identity.
- [Observed] Failed, unavailable or indeterminate state-(2) correlation is
  explicitly invalid and cannot fall back to state (1) in both PWB-REQ-005 and
  PWB-REQ-022.
- [Observed] State (1) is never called independently verified. Both requirement
  oracles explicitly restrict themselves to record semantics and disclosure
  and explicitly disclaim proof of human attendance.
- [Observed] Invalid PWB-REQ-005 admission produces zero reads, Unknown and a
  contradiction. Acts remain warrants rather than evidence of reads,
  screening, secret-freedom or truth.
- [Observed] PWB-REQ-022 keeps the execution record and owner judgment in
  distinct homes, assigns no verdict to absence, and assigns exact
  `verdict-unlawful` to a present invalid judgment while retaining
  Unknown-never-met.
- [Observed] Later A1 correlation affects only a later evaluation; both
  requirements prohibit rewriting the state of earlier reads or judgments.
- [Observed] The consent pair/class, observing-project policy, governance-home,
  read-only/empty-write, containment, authentication, secret and no-execution
  floors are retained. The candidate grants no effect or implementation
  authority.
- [Observed] The historical/current transaction predicates keep the performed
  2026-09-01 manifest immutable and require matching aggregate and dedicated
  successor acts before the eleven current PWB rows supersede the five
  historical current-path checks.

## Verdict

**VERDICT: REVISE**

[Inferred] The state distinction, fail-closed judgment behavior and historical
transaction mechanics are directionally sound, but the exact-digest package
does not yet provide a closed invalid-act oracle or a bounded third-channel
export parity oracle. These are acceptance-criterion failures at the authority
and public-interface seams, not implementation polish.

**OWNER SIGN-OFF MAY NOT BE OFFERED on commit
`f31f8315ecd75d83dd73ebd6739f003c241e8584`.** Repair the frozen candidate,
regenerate its eleven-row manifest, and obtain fresh independent confirmation
of the new exact bytes.
