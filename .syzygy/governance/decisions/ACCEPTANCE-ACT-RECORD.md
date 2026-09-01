# Acceptance-act record

> **The record of performed owner acts** over the final pre-specification
> package, created at the first act per
> `contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`
> §2 step 4. Entries are appended, dated, and never edited. Each entry is
> an **owner-adopted bootstrap act** under RFC3-16(c)'s two-state model:
> a governance fact preserved as phrase + exact digest + commit/tag,
> **"owner-adopted (bootstrap, uncorrelated)" — never "verified"** — until
> the one-time correlation act (RFC3-16(b)) exists and is performed.

## Act A — Wave A accepted, 2026-08-17

**Phrase, exactly as written by the owner (in-interaction, 2026-08-17):**

```
ACCEPT FOUNDATIONAL WAVE A: 8972d9630b95f5d4266432dbb1b3602114576bbd6c0f29d6f9bd6f905b1f884a
```

| | |
|---|---|
| Argument | sha256 of `contracts/candidates/wave-manifests/WAVE-A-MANIFEST.txt`, verified equal to the phrase at the act |
| Accepts | the 19 modules of RFC 0001–0006 at the per-module digests in that manifest |
| Confirmation | RD-31b, `VERDICT: CONFIRM`, on this exact argument (2026-08-10; raw at `contracts/candidates/round-2026-08e/reviews/RD-31b-wave-a-RAW.md`) |
| Ceremony verification (step 2) | `sha256sum -c` — 19 of 19 rows OK from the candidates root; `build_active_manifest.py --check` — manifests match regeneration; manifest digest equals the phrase argument `[Observed, this act]` |
| Install (step 3, shape (M) per the P-33 ruling) | the 19 modules copied to `.syzygy/governance/contracts/rfcs/` with their package structure, **and nothing else** — no companions, neither manifest. Verified: `sha256sum -c candidates/wave-manifests/WAVE-A-MANIFEST.txt` run from `.syzygy/governance/contracts/`, 19 of 19 OK; the installed tree holds exactly 19 files |
| Disclosed at the act | the 88 dangling path strings across the installed waves resolve in the candidates tree, not beside the installed copies — the (M) ruling's disclosed property (`WAVE-A-INSTALL-SHAPE-DECISION.md`); §7's Wave-A riders ride in as recorded there |
| Commit / tag (step 5) | the commit carrying this entry and the installed tree; annotated tag `wave-a-accepted-2026-08-17` |

Effective status of the 19 modules for human governance: **accepted —
owner-adopted (bootstrap, uncorrelated)**. Constraints bind at full
strength; nothing consumed as an authorization-for-effect satisfies
RFC3-16(a) from this record alone.

## Act B — Wave B accepted, 2026-08-17

**Phrase, exactly as written by the owner (in-interaction, 2026-08-17,
after the Wave A act — the A → B ordering is satisfied):**

```
ACCEPT FOUNDATIONAL WAVE B: 193e3c1e15e4b1375f938d62c9e8c1a442984313e0794ada5965d2cdf9d7e3ed
```

| | |
|---|---|
| Argument | sha256 of `contracts/candidates/wave-manifests/WAVE-B-MANIFEST.txt`, verified equal to the phrase at the act |
| Accepts | the 11 modules of RFC 0007–0009 (Polaris, Trajectory, Orrery) at the per-module digests in that manifest |
| Confirmation | RD-32c, `VERDICT: CONFIRM`, on this exact argument (2026-08-10; raw at `contracts/candidates/round-2026-08e/reviews/RD-32c-wave-b-RAW.md`) |
| Ordering | performed **after** the Wave A act (Act A above), so every RFC 0001–0006 reliance in these modules resolves into **accepted** text — the acceptance record row B's performed-alone caveat never triggered |
| Ceremony verification (step 2) | `sha256sum -c` — 11 of 11 rows OK from the candidates root; `build_active_manifest.py --check` — manifests match regeneration; manifest digest equals the phrase argument `[Observed, this act]` |
| Install (step 3, shape (M) per the P-33 ruling) | the 11 modules copied to `.syzygy/governance/contracts/rfcs/` with their package structure, **and nothing else**. Verified: `sha256sum -c candidates/wave-manifests/WAVE-B-MANIFEST.txt` run from `.syzygy/governance/contracts/`, 11 of 11 OK; the installed tree holds exactly the 30 files of Waves A + B |
| Disclosed at the act | the (M) dangling-path property (Act A above) extends over these modules; the installed-tree class is reported by `check_governance.py` CG-1i |
| Commit / tag (step 5) | the commit carrying this entry and the installed modules; annotated tag `wave-b-accepted-2026-08-17` |

Effective status of the 11 modules for human governance: **accepted —
owner-adopted (bootstrap, uncorrelated)**. Constraints bind at full
strength; nothing consumed as an authorization-for-effect satisfies
RFC3-16(a) from this record alone.

## Acts 6 and 7 — the CC-SPEC and CC-IMPACT craft amendments confirmed, 2026-08-17

**Phrases, exactly as written by the owner (in-interaction, 2026-08-17,
one sitting — the two policies are one model and were offered jointly):**

```
CONFIRM CRAFT AMENDMENT: CC-SPEC@9889b7e311ad941eec84d01dc2c035c7e2502a57cf18e68a1028a76d5b814871
CONFIRM CRAFT AMENDMENT: CC-IMPACT@cd6ec838e701f0258889d0c3c2776fc91fe1686829379b789ae5b151b04c27c0
```

| | |
|---|---|
| Arguments | each policy file's own sha256, re-verified by script at the act and equal to its phrase — the exact bytes the confirming review examined |
| Confirms | **CC-SPEC-1…11** (the specification-acceptance standard) and **CC-IMPACT-1…7** (the shape-to-spec impact rule) as owner-confirmed craft policy, in force at those digests |
| Review chain | RD-51 `REVISE` → repair → RD-69 `REVISE` (one blocker, repaired same day) → **RD-70 `CONFIRM WITH EXCEPTIONS`** on these digests (raw + register: `contracts/candidates/round-2026-08i/reviews/`) |
| Disclosed at the act | the nine open non-blocking findings (RD-69 N1–N5, RD-70 N1–N4) travel into force, per the offering packets — the first post-act amendment's worklist |
| Recording | `policies/craft-and-care/INSTALL-RECORD.md` (the act-2 precedent); the files bind at their committed home, uncopied and unedited — an edit after the act retires it |
| What this changes | launch-gate **E5** and **E6** now have owner-confirmed, citable owners; the first specification, when the owner authorizes authoring, is judged under a standard in force |
| Commit / tag (step 5) | the commit carrying this entry; annotated tag `craft-acts-6-7-confirmed-2026-08-17` |

Effective status for human governance: **confirmed craft policy —
owner-adopted (bootstrap, uncorrelated)**.

## General trusted-bootstrap authorization transaction — performed 2026-09-01

**Phrase, exactly as written by the owner (in-interaction, 2026-09-01):**

```text
SIGN OFF GENERAL TRUSTED-BOOTSTRAP AUTHORIZATION TRANSACTION: 1885a323c659364f98e81cdf04479cebfecf5b22d350928d046ebb5b7c5268f6
```

**Performed nested row-5 act argument, bound by the outer transaction
ceremony:**

```text
CONFIRM CRAFT AMENDMENT: CC-SPEC@6093dbbe519dad6c35a5aaeeb31355d2e435d76ec4f0c2c9affb0d1e5b6b5621
```

| | |
|---|---|
| Project / owner | `project:syzygy` / Tzeusy |
| Argument | sha256 of `contracts/candidates/general-trusted-bootstrap-authorization/TRANSACTION-MANIFEST.txt`, re-computed at recording and equal to the phrase |
| Provenance state | `owner-adopted (bootstrap, uncorrelated)` — a state-(1) human act, owner-trusted and never independently verified |
| A1 audit-record identity | explicitly absent, satisfying RFC3-16(b) item 9 for state (1) |
| Reviewed subject | `92cfbf3e3a644bff7ac738d2cf7084c06548381c` |
| Owner-packet head | `a5f2c4fe22f9ae3c50ee8902a0b7d78207f910a2`; it changed no transaction-bound subject after review |
| Review outcome | security `CONFIRM`; contract/fresh-reader and impact/transaction `CONFIRM WITH EXCEPTIONS`, no blockers |
| Ceremony verification | 7 of 7 top-level subjects, 30 of 30 contract rows and 5 of 5 PWB coverage rows verified at their recorded digests `[Observed, this act]` |
| Recording | `.syzygy/governance/decisions/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md`; planned annotated tag `general-trusted-bootstrap-authorized-2026-09-01` on the commit carrying these records |

All five rows below were performed together. Their wording is copied exactly
from the transaction-bound `ACT-SEMANTICS.md`.

| # | Act type | Stable subject identity | Exact digest(s) | Scope | Supersession / revocation |
|---|---|---|---|---|---|
| 1 | `accept-contract-amendment` | accepted RFC 0001-0009 contract set | contract-amendment manifest `480c06d79f237f3a8d18d40a3de97e772a2da70db6cf976578eeab5c177cc4b1` | Accept the generalized effective-owner-act model: valid state (1) and state (2) acts may satisfy existing owner gates, exact state always renders, invalid acts fail closed, and acts remain warrants rather than evidence | Supersedes the current bytes accepted through the historical Wave A/B acts; those acts, manifests and prior bytes remain immutable historical evidence |
| 2 | `sign-off-coverage-amendment` | Capability 1 change `project-registration-and-honest-shape-visibility`, `CONTRACT-COVERAGE.md` only | `15431d8ba1fe25a61e4dc2713c4d51fad1cf6d25ef7a9103cc616265102289c9` | Reconcile contract traceability to the amended RFC3-16 model; change no requirement, proposal, design or implementation authorization | Supersedes only that artifact's digest in the 2026-08-20 adoption; all other adopted digests remain |
| 3 | `sign-off-coverage-amendment` | signed change `three-surface-poc-experience`, `CONTRACT-COVERAGE.md` only | `f29a01f6a5725f4ac7085fa04a62de757fd16153d507ae5e415ae0b501fdc0a4` | Reconcile contract traceability to the amended RFC3-16 model; change no POC requirement, scope or implementation authority | Supersedes only that artifact's digest in the 2026-08-30 sign-off; all other signed digests remain |
| 4 | `sign-off-coverage-amendment` | signed change `polaris-project-wide-butlers-model`, contract-coverage bundle | PWB coverage manifest `5cda673c604f298cc45d05ca358b2cc410b6a74f1664c55f4f1056ce8c1f45ea` | Reconcile five signed coverage artifacts while leaving PWB-REQ-005 and PWB-REQ-022 deliberately stricter at state (2); change no requirement, proposal, design or implementation authority | Supersedes only the five artifact digests listed by the PWB coverage manifest; every other 2026-08-31 sign-off digest remains |
| 5 | `confirm-craft-amendment` | in-force policy `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` (CC-SPEC-1..11) | `6093dbbe519dad6c35a5aaeeb31355d2e435d76ec4f0c2c9affb0d1e5b6b5621` | Amend CC-SPEC-8's reviewed-N/A owner-act gate to accept valid state (1) or state (2), render the exact state, and fail closed on absent or invalid acts; no other craft obligation changes | Supersedes the policy digest confirmed by craft act 6; that performed act, digest and prior bytes remain immutable historical evidence |

Effective status: the amended contract set, seven amended coverage artifacts
and CC-SPEC amendment are **owner-adopted (bootstrap, uncorrelated)** at the
exact scopes and digests above. State (1) is effective but never supports the
claim “independently verified”; owner acts remain warrants, not evidence.

Apart from row 5's CC-SPEC amendment, this transaction grants no
effect-specific consent or policy approval, registry adoption, observation,
write, egress, execution, deployment, release, recovery, implementation or
mission authority. It does not accept RFC 0010 or RFC 0011, amend doctrine,
sign Mission Control behavior, implement PWB or start automatic follow-on
work.
