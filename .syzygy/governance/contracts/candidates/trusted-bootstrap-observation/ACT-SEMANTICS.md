# Trusted-bootstrap observation act semantics

> **Candidate — binds nothing.** The transaction manifest binds this file's
> exact digest. The owner ceremony supplies the act instant and performs all six
> rows together.

Project identity for every act: `project:syzygy`

Owner attribution for every act: Tzeusy

Provenance state at the ceremony: `owner-adopted (bootstrap, uncorrelated)`;
no external RFC5-25 audit identity exists. This state is trusted only as the
amended contract permits.

| # | Act type | Stable subject identity | Exact digest(s) | Scope | Supersession / revocation |
|---|---|---|---|---|---|
| 1 | `accept-contract-amendment` | foundational Wave A contract package | Wave-A manifest `505c46c6702ebde0908328fd67e684c26501a7f26dbb37e451ca05661a2c9034` | Accept the amended Wave-A bytes, including the closed trusted-bootstrap read-only observation mode; no other effect class changes | Supersedes Wave A manifest argument `8972d9630b95f5d4266432dbb1b3602114576bbd6c0f29d6f9bd6f905b1f884a` for current contract bytes; historical act remains |
| 2 | `sign-off-behavior-amendment` | OpenSpec change `polaris-project-wide-butlers-model` | the eleven exact PWB digests listed in `TRANSACTION-MANIFEST.txt` | Replace PWB-REQ-001/005/006 and their proposal/design/coverage consequences with trusted-bootstrap read-only observation semantics | Supersedes `.syzygy/governance/decisions/POLARIS-PROJECT-WIDE-SPEC-SIGNOFF-ACT.md` for current PWB bytes; historical act remains |
| 3 | `sign-off-coverage-scope-amendment` | `three-surface-poc-experience` contract-coverage artifact | `858e5f1af675eef82fad70b20702aca14e24c54edec6e1b4845038b5e507749f` | Scope original-slice absence claims away from separately governed child changes; change no requirement or consequence disposition | Supersedes only the prior digest of that coverage artifact; every other parent sign-off digest remains |
| 4 | `consent-observation` | `PWB-CONSENT-2026-08-31` | `766f1fb9b031fc04f2c814bdf0c464911e943890ceb71e94111cec52971538cc` | Read-only declared-project-shape observation of `(project:syzygy, repository:butlers-configured-poc)`; no write, egress, execution, credential/environment access or second repository | No earlier consent; revocable by a later owner act |
| 5 | `approve-secret-policy` | policy `polaris-butlers-project-shape-secrets@1.0.0` | `67a5f00d321afe746eb739fedaeb477a02dc57ce198ce8fb615bcf028e1b26f3` | Govern both project-shape discovery phases and every named sink; fail closed; retain hash-not-body exclusions | No earlier approval; superseded only by a later exact-digest owner act |
| 6 | `adopt-adapter-entry` | adapter `polaris-butlers-project-shape@1.0.0` | `c8bbc200da492d54410cd72a2f24952ca71fa020953d0a0d8ad93f30f8400629` | Admit deterministic facts only for the exact read-only Git authority and subject in the entry; all non-read authority remains empty | No earlier adoption; superseded or revoked only by a later owner act |

The PWB eleven-digest set in row 2 is exactly the contiguous block between the
Wave-A manifest row and parent-coverage row in `TRANSACTION-MANIFEST.txt`.
Changing the manifest order, membership, any digest or this mapping retires the
offering and requires fresh review.
