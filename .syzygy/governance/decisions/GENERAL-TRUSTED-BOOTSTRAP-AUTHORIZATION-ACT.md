# Owner act — general trusted-bootstrap authorization transaction

Date: 2026-09-01

Owner: Tzeusy

Act identity: `GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-2026-09-01`

Project identity: `project:syzygy`

Provenance state: `owner-adopted (bootstrap, uncorrelated)`

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner performed the offered indivisible transaction by writing exactly:

```text
SIGN OFF GENERAL TRUSTED-BOOTSTRAP AUTHORIZATION TRANSACTION: 1885a323c659364f98e81cdf04479cebfecf5b22d350928d046ebb5b7c5268f6
```

The argument is the sha256 of
`.syzygy/governance/contracts/candidates/general-trusted-bootstrap-authorization/TRANSACTION-MANIFEST.txt`.
It was re-computed at recording and matched the phrase. All seven bound
top-level subjects, all 30 contract-amendment rows and all five nested PWB
coverage rows verified at their recorded digests.

Frozen transaction provenance:

- reviewed subject: `92cfbf3e3a644bff7ac738d2cf7084c06548381c`;
- owner-packet head: `a5f2c4fe22f9ae3c50ee8902a0b7d78207f910a2`;
- security confirmation: `CONFIRM`;
- contract/fresh-reader confirmation: `CONFIRM WITH EXCEPTIONS`, no blockers;
- impact/transaction confirmation: `CONFIRM WITH EXCEPTIONS`, no blockers;
  and
- planned recording tag:
  `general-trusted-bootstrap-authorized-2026-09-01`, on the commit carrying
  this act record.

The packet-head commit added the owner-facing offering and did not alter any
transaction-bound subject reviewed at `92cfbf3`.

## Five indivisible act rows

All five rows below were performed together. Their wording is copied exactly
from the transaction-bound `ACT-SEMANTICS.md`.

| # | Act type | Stable subject identity | Exact digest(s) | Scope | Supersession / revocation |
|---|---|---|---|---|---|
| 1 | `accept-contract-amendment` | accepted RFC 0001-0009 contract set | contract-amendment manifest `480c06d79f237f3a8d18d40a3de97e772a2da70db6cf976578eeab5c177cc4b1` | Accept the generalized effective-owner-act model: valid state (1) and state (2) acts may satisfy existing owner gates, exact state always renders, invalid acts fail closed, and acts remain warrants rather than evidence | Supersedes the current bytes accepted through the historical Wave A/B acts; those acts, manifests and prior bytes remain immutable historical evidence |
| 2 | `sign-off-coverage-amendment` | Capability 1 change `project-registration-and-honest-shape-visibility`, `CONTRACT-COVERAGE.md` only | `15431d8ba1fe25a61e4dc2713c4d51fad1cf6d25ef7a9103cc616265102289c9` | Reconcile contract traceability to the amended RFC3-16 model; change no requirement, proposal, design or implementation authorization | Supersedes only that artifact's digest in the 2026-08-20 adoption; all other adopted digests remain |
| 3 | `sign-off-coverage-amendment` | signed change `three-surface-poc-experience`, `CONTRACT-COVERAGE.md` only | `f29a01f6a5725f4ac7085fa04a62de757fd16153d507ae5e415ae0b501fdc0a4` | Reconcile contract traceability to the amended RFC3-16 model; change no POC requirement, scope or implementation authority | Supersedes only that artifact's digest in the 2026-08-30 sign-off; all other signed digests remain |
| 4 | `sign-off-coverage-amendment` | signed change `polaris-project-wide-butlers-model`, contract-coverage bundle | PWB coverage manifest `5cda673c604f298cc45d05ca358b2cc410b6a74f1664c55f4f1056ce8c1f45ea` | Reconcile five signed coverage artifacts while leaving PWB-REQ-005 and PWB-REQ-022 deliberately stricter at state (2); change no requirement, proposal, design or implementation authority | Supersedes only the five artifact digests listed by the PWB coverage manifest; every other 2026-08-31 sign-off digest remains |
| 5 | `confirm-craft-amendment` | in-force policy `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` (CC-SPEC-1..11) | `6093dbbe519dad6c35a5aaeeb31355d2e435d76ec4f0c2c9affb0d1e5b6b5621` | Amend CC-SPEC-8's reviewed-N/A owner-act gate to accept valid state (1) or state (2), render the exact state, and fail closed on absent or invalid acts; no other craft obligation changes | Supersedes the policy digest confirmed by craft act 6; that performed act, digest and prior bytes remain immutable historical evidence |

## Effect and provenance

The accepted RFC 0001–0009 contract set, the seven signed coverage artifacts
and CC-SPEC-8 are amended at the exact digests above. The five rows are one
same-logical-change transaction under CC-REV-2; no row was performed alone.

This is a genuine human state-(1) act. It is effective for only the exact act
types, subjects and scopes above, is owner-trusted, and remains visibly
uncorrelated. The A1 audit identity is explicitly absent; this act is **not
independently verified**. The commit and planned tag preserve the record but
do not establish human attendance or state (2). The act is a warrant, never
evidence that any authorized effect occurred or succeeded.

The historical Wave A/B acts, coverage sign-offs and craft act 6 remain
immutable historical evidence at their former digests. This transaction
supersedes only the current bytes and artifact digests its five rows name.

## What this act does not authorize

Apart from row 5's CC-SPEC craft amendment, this transaction performs no
effect-specific consent or policy approval, registry adoption, repository
observation or write, egress, execution, deployment, release, recovery,
implementation or mission act. It does not accept RFC 0010 or RFC 0011, sign
Mission Control behavior, amend doctrine, implement PWB, authorize observation
of a repository body, or start any automatic follow-on work. Every later
effect still requires its own exact conjunctive gates and evidence.
