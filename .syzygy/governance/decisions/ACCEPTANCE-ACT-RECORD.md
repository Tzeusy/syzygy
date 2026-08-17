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
