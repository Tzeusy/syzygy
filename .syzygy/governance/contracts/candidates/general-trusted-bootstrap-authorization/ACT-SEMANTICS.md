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
| 1 | `accept-contract-amendment` | accepted RFC 0001-0009 contract set | contract-amendment manifest `c2c3b7087d39696061385fcc5a4ca2f9cbec327619e6b09859e86ee77396d818` | Accept the generalized effective-owner-act model: valid state (1) and state (2) acts may satisfy existing owner gates, exact state always renders, invalid acts fail closed, and acts remain warrants rather than evidence | Supersedes the current bytes accepted through the historical Wave A/B acts; those acts, manifests and prior bytes remain immutable historical evidence |
| 2 | `sign-off-coverage-amendment` | Capability 1 change `project-registration-and-honest-shape-visibility`, `CONTRACT-COVERAGE.md` only | `15431d8ba1fe25a61e4dc2713c4d51fad1cf6d25ef7a9103cc616265102289c9` | Reconcile contract traceability to the amended RFC3-16 model; change no requirement, proposal, design or implementation authorization | Supersedes only that artifact's digest in the 2026-08-20 adoption; all other adopted digests remain |
| 3 | `sign-off-coverage-amendment` | signed change `three-surface-poc-experience`, `CONTRACT-COVERAGE.md` only | `9904e93cf38fdcfb9fa95407d6f77de289075f414c9a18505ce2d7561d53369a` | Reconcile contract traceability to the amended RFC3-16 model; change no POC requirement, scope or implementation authority | Supersedes only that artifact's digest in the 2026-08-30 sign-off; all other signed digests remain |
| 4 | `sign-off-coverage-amendment` | signed change `polaris-project-wide-butlers-model`, contract-coverage bundle | PWB coverage manifest `cf485f39b375bdfb7038161a97b0d4c0ffa3731c177837af6ee9ecacc575d1ba` | Reconcile five signed coverage artifacts while leaving PWB-REQ-005 and PWB-REQ-022 deliberately stricter at state (2); change no requirement, proposal, design or implementation authority | Supersedes only the five artifact digests listed by the PWB coverage manifest; every other 2026-08-31 sign-off digest remains |
| 5 | `confirm-craft-amendment` | in-force policy `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` (CC-SPEC-1..11) | `cd2511a00d391e5e61410a65ab7a215264064ab5d0e6e1618ee83224c8a8f503` | Amend CC-SPEC-8's reviewed-N/A owner-act gate to accept valid state (1) or state (2), render the exact state, and fail closed on absent or invalid acts; no other craft obligation changes | Supersedes the policy digest confirmed by craft act 6; that performed act, digest and prior bytes remain immutable historical evidence |

The five rows are one same-logical-change transaction under CC-REV-2. A
partial ceremony performs none of them. Editing any subject, manifest or this
mapping retires the offering and requires fresh exact-byte review.

This transaction performs no consent, policy approval, registry adoption,
write, egress, execution, deployment, release, recovery or mission act. It
does not accept RFC 0010 or RFC 0011, sign Mission Control behavior, amend
doctrine, implement PWB, or authorize observation of a repository body.
