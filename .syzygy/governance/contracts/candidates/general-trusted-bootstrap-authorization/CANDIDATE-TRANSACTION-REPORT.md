# Historical candidate transaction report — general trusted-bootstrap authorization

> **PERFORMED 2026-09-01 — transaction ceremony satisfied.** The owner
> performed the exact indivisible transaction and its act is recorded at
> `.syzygy/governance/decisions/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md`.
> This report remains non-bound historical evidence; the act record owns the
> authority state.

## Transaction

`TRANSACTION-MANIFEST.txt` sha256:
`1885a323c659364f98e81cdf04479cebfecf5b22d350928d046ebb5b7c5268f6`.

The manifest binds `ACT-SEMANTICS.md`, the complete impact ledger, the
30-module contract-amendment manifest, the five-artifact PWB coverage manifest,
the Capability 1 and three-surface coverage amendments, and the amended
CC-SPEC policy. Its five act rows are indivisible.

## What changes

- RFC3-16(a/b/c) recognizes two effective provenance states. A real human
  state-(1) act is owner-trusted and visibly uncorrelated; only state (2) is
  independently verified. Invalid acts still fail closed.
- Every direct accepted consumer and all nine OpenSpec phase rules carry the
  same rule. Owner acts remain warrants, never evidence of substantive
  success.
- Candidate RFC 0010 consumes the shared rule and records the performed
  doctrine interpretation, while remaining candidate and non-operative.
- Seven signed coverage artifacts are reconciled without changing their
  behavioral requirements. PWB remains deliberately stricter at state (2).
- CC-SPEC-8 is amended in the same logical change because its in-force text
  restated the old A1-only reviewed-N/A gate.
- Performed Wave A/B manifests remain byte-immutable act arguments. The active
  manifest and unperformed C1/C2/D1/D2 manifests track current bytes; tooling
  and mutation tests enforce the split.

## Measured scope

- Contract amendment: 30 accepted modules, each byte-identical to its
  candidate mirror.
- Impact ledger: 204 unique baseline files across seven exact text
  populations. `git grep` and an independent `git archive` byte sweep agree on
  every path set.
- PWB coverage remains 622 effective consequences: 132 covered, 242 Unknown
  uncovered, 248 believed not applicable. The repair overlay remains 71 rows
  over 62 superseded base rows: 52 covered, 16 Unknown, 3 believed not
  applicable.

## Historical pre-act verification before fresh review

- All three OpenSpec changes validate `--strict`.
- Current manifest, contract index, dependency index, context-budget report,
  task router, Capability 1 views/dependencies, PWB coverage, transaction and
  impact generators match regeneration; their applicable selftests pass.
- `build_active_manifest.py --selftest`: 8/8 pass, including lawful amendment
  of a performed-wave module without Wave A rewrite and fail-closed performed
  manifest tampering.
- `check_governance.py --selftest`: 158 fixtures, 0 failing.
- The remaining main governance result is deliberately **not green**:
  **31 OK, 18 WARN, 2 FAIL**. CG-7d and CG-7e report the four old CC-SPEC
  digest quotations in the performed offering/act/install records because the
  amended policy digest has no new owner act yet. The historical records are
  not rewritten to simulate that act. This is the exact owner gate; after a
  ceremony, a new append-only act entry and current-state check semantics must
  reconcile it.

## Historical pre-act authorization state

This candidate does not consent to repository observation or writes, approve a
secret policy or adapter registry entry, authorize egress or execution, accept
RFC 0010/0011, start a mission, deploy, release, recover, or implement PWB.
The superseded Polaris-only transaction remains never-effective history.
