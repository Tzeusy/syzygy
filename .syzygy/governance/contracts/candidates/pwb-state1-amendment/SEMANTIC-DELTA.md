# Semantic delta — PWB state-(1) owner-act consumption

> **Candidate — binds nothing.** Owner direction
> `PWB-STATE1-AMENDMENT-DIR-2026-09-02` authorizes drafting and independent
> review only. The currently signed PWB bytes remain authoritative until a
> later exact-digest human owner act supersedes them.

Date: 2026-09-02

Baseline: `bef7f8d23fe63df5150f1ce8fac5bf5d7d3d79e7`

Affected stable requirement IDs: `PWB-REQ-005`, `PWB-REQ-020`,
`PWB-REQ-022`. No requirement is minted, retired or renumbered.

## Problem

The generalized trusted-bootstrap transaction made a valid human owner act
effective in either state (1), `owner-adopted (bootstrap, uncorrelated)`, or
state (2), `Syzygy-verified`. The signed PWB requirements deliberately remained
state-(2)-only. The owner chose profile A: amend both the body-read authority
gate and the walkthrough-judgment gate to consume the generalized rule.

## Normative changes

### PWB-REQ-005

The body-read gate accepts consent, secret-policy and adapter-registry acts
independently in either valid provenance state, including mixed all-valid
triples. Every act binds RFC3-16(b)'s exact fields. The human and machine
surfaces retain each authority's exact state.

State (1) renders the exact limitation:

> Owner-trusted only; same-tree forgeable from Syzygy's perspective. Digest
> detects drift, not authorship or attendance.

Only state (2) may be called independently verified. A missing, malformed,
non-human, unattributed, wrong-project, wrong-repository, wrong-class,
wrong-scope, wrong-act-type, digest-mismatched, stale, expired, superseded or
revoked act fails closed with zero body reads, Unknown and the RFC3-16(a)
contradiction. Failed, unavailable or indeterminate state-(2) correlation does
not downgrade to state (1).

The consent remains exact-pair and exact-class; the observing project's own
policy still governs; the registry remains governance-homed, read-only and
empty-write. An act warrants use of its artifact and is not evidence that a
read occurred, screening succeeded, content is secret-free or a claim is true.
Later correlation does not rewrite the provenance of an earlier read.

The invalid denominator is closed at 195 cases: 55 common owner-act cases for
each of the three authorities plus 30 authority-specific field cases. The
common set includes complete RFC3-16(b), act-record identity, provenance-state
input, false-substitute, lifecycle, state-mechanics and state-(1) exact owner
phrase/recording-context cases. Another-human and non-human owner attribution
are independent cases.

### PWB-REQ-022

The walkthrough criterion accepts an exact-scope human owner judgment in valid
state (1) or state (2), exposes the exact state on both surfaces and applies the
same state-(1) disclosure and failed-correlation no-fallback rule.

The execution record and judgment remain separate. Absence creates
Unknown-never-met without inventing a verdict. A present invalid judgment
records `verdict-unlawful`, retains the contradiction and remains
Unknown-never-met. The judgment is recorded human judgment, never Observed and
never a score. Its act, digest, correlation and execution record do not prove
comprehension succeeded. Later correlation does not rewrite the provenance of
an earlier judgment.

The judgment denominator is closed at 84 present-invalid cases: the same 55
common owner-act cases plus 15 run-record, 12 judgment-field and 2
governance-home cases. Two absent cases remain separate because absence
invents no verdict.

### PWB-REQ-020

The exhaustive parity population now includes every PWB-REQ-005 authority
state, every PWB-REQ-022 judgment state and every state-(1) disclosure. The
human and machine channels preserve multiplicity and exact provenance state.

## Required tests

- Exercise all eight valid consent/policy/registry state combinations.
- Exercise the closed 195-case admission-invalid denominator independently,
  including missing, malformed and wrong-but-present values for every
  RFC3-16(b) and authority-specific field.
- Prove zero reads and Unknown for any invalid admission limb.
- Exercise valid state-(1), valid state-(2), the closed 84-case present-invalid
  judgment denominator and both absent cases, including exact
  `verdict-unlawful` behavior.
- Prove the state-(1) oracle checks record semantics and disclosure without
  claiming to prove human attendance.
- For every invalid case, mutate the implementation toward unlawful admission
  or success and retain fail-then-restore evidence. Separately mutate exact
  state, disclosure, audit identity/absence, act scope, digest, no-fallback and
  prior-evaluation history one predicate at a time.
- Compare every authorization and judgment marker across the human and machine
  channels with an order-insensitive, multiplicity-preserving oracle and
  mutation-prove missing, duplicate, changed, collapsed and wrong-evaluation
  markers.

## Accepted risk

State-(1) consent, policy, registry and judgment records remain same-tree
forgeable from Syzygy's perspective. Exact digests detect drift but cannot
establish authorship or owner attendance. The owner accepted this residual
risk only for the bounded local one-Butlers-repository POC. The specification
exposes the limitation rather than claiming to eliminate it.

## Unchanged boundaries

- Humans remain the only owners; a file, attribution, commit, tag, machine
  submission or agent assertion is not by itself an owner act.
- State (1) is never independently verified; only state (2) uses A1.
- Every scope, secret-screening, authentication, containment, read-only,
  empty-write, no-execution, no-egress and fail-closed gate remains conjunctive.
- The amendment creates no consent, policy, registry or judgment act.
- The amendment authorizes no body read, implementation, write, egress,
  execution, deployment, release, recovery or mission.
- The six signed `three-surface-poc-experience` artifacts remain unchanged.
- Historical acts, packets, reviews, manifests and prior digests remain
  immutable evidence.

## Supersession and rollback

The later owner act must bind all eleven PWB signed artifacts as one package,
including unchanged `.openspec.yaml`, and supersede the six still-current
2026-08-31 digests plus the five coverage digests superseded on 2026-09-01.
No partial act is effective.

Before sign-off, rollback is deletion of this candidate branch. After sign-off,
restoring state-(2)-only behavior requires a new reviewed exact-digest owner
amendment; earlier acts and evaluations retain their historical provenance.

## Warrant and evidence basis

- `.syzygy/governance/decisions/PWB-STATE1-AMENDMENT-DIRECTION.md`
- `.syzygy/governance/decisions/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md`
- `.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md`
  — RFC3-16(a), RFC3-16(b), RFC3-16(c)
- `openspec/changes/polaris-project-wide-butlers-model/`
- independent amendment-map and security-design reviews prepared from baseline
  `bef7f8d`
