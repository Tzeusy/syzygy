# General trusted-bootstrap authorization act semantics

> **Candidate — binds nothing.** The transaction manifest binds this file's
> exact digest. The owner ceremony supplies the act instant and performs the
> five rows together.

Project identity for every act: `project:syzygy`

Owner attribution for every act: Tzeusy

Provenance state at the ceremony: `owner-adopted (bootstrap, uncorrelated)`;
RFC3-16(b) item 9 records the A1 audit identity as explicitly absent. This is
an effective owner act only if the human owner performs the exact ceremony.

| # | Act type | Stable subject identity | Exact digest(s) | Scope | Supersession / revocation |
|---|---|---|---|---|---|
| 1 | `accept-contract-amendment` | accepted RFC 0001-0009 contract set | contract-amendment manifest `480c06d79f237f3a8d18d40a3de97e772a2da70db6cf976578eeab5c177cc4b1` | Accept the generalized effective-owner-act model: valid state (1) and state (2) acts may satisfy existing owner gates, exact state always renders, invalid acts fail closed, and acts remain warrants rather than evidence | Supersedes the current bytes accepted through the historical Wave A/B acts; those acts, manifests and prior bytes remain immutable historical evidence |
| 2 | `sign-off-coverage-amendment` | Capability 1 change `project-registration-and-honest-shape-visibility`, `CONTRACT-COVERAGE.md` only | `15431d8ba1fe25a61e4dc2713c4d51fad1cf6d25ef7a9103cc616265102289c9` | Reconcile contract traceability to the amended RFC3-16 model; change no requirement, proposal, design or implementation authorization | Supersedes only that artifact's digest in the 2026-08-20 adoption; all other adopted digests remain |
| 3 | `sign-off-coverage-amendment` | signed change `three-surface-poc-experience`, `CONTRACT-COVERAGE.md` only | `f29a01f6a5725f4ac7085fa04a62de757fd16153d507ae5e415ae0b501fdc0a4` | Reconcile contract traceability to the amended RFC3-16 model; change no POC requirement, scope or implementation authority | Supersedes only that artifact's digest in the 2026-08-30 sign-off; all other signed digests remain |
| 4 | `sign-off-coverage-amendment` | signed change `polaris-project-wide-butlers-model`, contract-coverage bundle | PWB coverage manifest `5cda673c604f298cc45d05ca358b2cc410b6a74f1664c55f4f1056ce8c1f45ea` | Reconcile five signed coverage artifacts while leaving PWB-REQ-005 and PWB-REQ-022 deliberately stricter at state (2); change no requirement, proposal, design or implementation authority | Supersedes only the five artifact digests listed by the PWB coverage manifest; every other 2026-08-31 sign-off digest remains |
| 5 | `confirm-craft-amendment` | in-force policy `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` (CC-SPEC-1..11) | `6093dbbe519dad6c35a5aaeeb31355d2e435d76ec4f0c2c9affb0d1e5b6b5621` | Amend CC-SPEC-8's reviewed-N/A owner-act gate to accept valid state (1) or state (2), render the exact state, and fail closed on absent or invalid acts; no other craft obligation changes | Supersedes the policy digest confirmed by craft act 6; that performed act, digest and prior bytes remain immutable historical evidence |

The five rows are one same-logical-change transaction under CC-REV-2. A
partial ceremony performs none of them. Editing any subject, manifest or this
mapping retires the offering and requires fresh exact-byte review.

Apart from row 5's CC-SPEC craft amendment, this transaction performs no
effect-specific consent or policy approval, registry adoption, write, egress,
execution, deployment, release, recovery or mission act. It
does not accept RFC 0010 or RFC 0011, sign Mission Control behavior, amend
doctrine, implement PWB, or authorize observation of a repository body.
