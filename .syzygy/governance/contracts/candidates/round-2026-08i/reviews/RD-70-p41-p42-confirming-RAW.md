# RD-70 — confirming review of the CC-SPEC-8 blocker repair — RAW

> **Raw reviewer output, stored verbatim. Never edited.** Everything below
> the `---` rule is the reviewer's text exactly as delivered.
>
> - **Review:** RD-70, the one confirming review of the RD-69 blocker-only
>   repair — the closing review of the pass's single
>   repair→review→repair→confirm cycle.
> - **Subjects and frozen digests** (sha256, at commit `bef5de1`):
>   - `policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` —
>     `9889b7e311ad941eec84d01dc2c035c7e2502a57cf18e68a1028a76d5b814871`
>   - `policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` —
>     `cd6ec838e701f0258889d0c3c2776fc91fe1686829379b789ae5b151b04c27c0`
>     (byte-unchanged since RD-69; coherence scope only)
>   - `policy-candidates/CC-REV-2-LAGGING-SPECIFICATION-AMENDMENT-OFFER.md`
>     (P-44) —
>     `beb84463d916502178eca5db2201431588efbed73bbefe58661402bcea27b2f7`
>     (byte-unchanged since RD-69; coherence scope only)
> - **Protocol:** fresh context — the reviewer was given the subjects,
>   their governing references, and the acceptance criterion (RD-69's
>   BLOCKER 1 statement plus the five-part launch-blocker test), and was
>   barred from `round-*/reviews/`, disposition registers, and semantic
>   deltas. Its independence statement is in §2 below.
> - **Reviewer provenance:** a separate Claude-family session (subagent),
>   dispatched 2026-08-17. **Same model family as the author session** —
>   under the launch-gate's independence rule this review supports repair
>   only, never a formal administration.
> - **Delivery:** two parts over inter-session messages, 2026-08-17
>   (+08:00), stored in order.
> - **Verdict, copied exactly:** `VERDICT: CONFIRM WITH EXCEPTIONS`
> - **Outcome:** BLOCKER 1 cleared on all five limbs; no new launch
>   blockers; four non-blocking findings (dispositioned in
>   `RD-69-DISPOSITION-REGISTER.md`, RD-70 section). Per verification
>   rule 10, the subject bytes are not edited after this review — the
>   non-blocking fixes batch into the next authoring pass.

---
# RD-70 — Confirming review of the CC-SPEC-8 blocker repair

## 1. Digest verification

`[Observed]` — `sha256sum` run 2026-08-17 in `.syzygy/governance/contracts/candidates/`:

| Subject | Expected | Actual | Result |
|---|---|---|---|
| `policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` | `9889b7e3…14871` | `9889b7e311ad941eec84d01dc2c035c7e2502a57cf18e68a1028a76d5b814871` | **MATCH** |
| `policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` | `cd6ec838…4c27c0` | `cd6ec838e701f0258889d0c3c2776fc91fe1686829379b789ae5b151b04c27c0` | **MATCH** |
| `policy-candidates/CC-REV-2-LAGGING-SPECIFICATION-AMENDMENT-OFFER.md` | `beb84463…7b2f7` | `beb84463d916502178eca5db2201431588efbed73bbefe58661402bcea27b2f7` | **MATCH** |

## 2. Independence statement

`[Observed]` I worked fresh-context, from only the materials named in my instructions. I read: the three subject files; `rfcs/RFC-0001-project-graph-identity-state-planes.md`, `rfcs/RFC-0006-cross-surface-selection-query-drawer.md`, `rfcs/RFC-0007/rendering-and-surface.md`, `rfcs/RFC-0008/accounting-reconciliation-and-release.md`, `rfcs/RFC-0009/interaction-parity-and-release.md`, `rfcs/RFC-0003/governance-homes-and-owner-acts.md`; `policies/craft-and-care/testing-and-verification.md` (CC-TEST-4); `PROCESS-GLOSSARY.md`. I read **no** `round-*/reviews/` file, **no** DISPOSITION-REGISTER, **no** semantic delta, and no `round-2026-08i/` content — I confirmed three referenced paths *exist* by `ls` only, without opening them. Sweeps used Python `re`, not ugrep.

## 3. BLOCKER 1 — limb-by-limb

| Limb | Verdict | Evidence |
|---|---|---|
| **(a)** Any sentence still claiming/implying CC-SPEC-8 is the rule's home? | **CLEARED** | CC-SPEC-8 now reads: *"**The reviewed-N/A judgment's home, gate, unit, and effect rule are the contract's, not this clause's.**"* A whitespace-normalized `re` scan of the whole file for `one home` / `the one home` / `only statement` returns **4 hits, 0 normative** — all four are historical narration correctly describing the defect in past tense (banner ×1, the `*(History: …)*` note ×1, the f15 findings row ×1) plus the unrelated `## What this policy is not` closer "One fact, one home." |
| **(b)** Gate now the contract's (owner judgment, `decisions/` home, RFC3-16(a) provenance, Unknown-never-covered effect)? | **CLEARED** | CC-SPEC-8: *"a reviewed N/A judgment is a recorded **owner** judgment homed in `decisions/` (RFC3-15), honored only where its owner-act provenance is verifiable under **RFC3-16(a)**; where that provenance does not verify, the judgment maps nothing — the consequence remains unmapped and **renders Unknown, never covered** (VIS-2)."* Faithful reduction of RFC1-33 (l.759-764): *"A reviewed N/A judgment is a recorded owner judgment homed in `decisions/` (RFC3-15), and it is honored only where its owner-act provenance is verifiable under RFC3-16(a). Where that provenance does not verify, the judgment maps nothing: the consequence remains unmapped and renders Unknown, never covered (RFC3-16(a)'s effect rule; VIS-2)."* Verified byte-identical (modulo line wrap) at RFC6-28 (l.484-488), RFC7-38 (l.327-332), RFC8-32 (l.321-326), RFC9-52 (l.313). RFC3-15 and RFC3-16(a) exist in `rfcs/RFC-0003/governance-homes-and-owner-acts.md` (l.73; l.158 *"**RFC3-16(a). The owner-act provenance predicate.**"*) and say what is claimed. |
| **(c)** Unit per observable consequence? | **CLEARED** | CC-SPEC-8: *"The matrix's unit is the contract's, not this clause's: **rows are per observable consequence, not per clause** (RFC1-33, RFC6-28) — a clause with five observable consequences and one mapped requirement is not covered."* RFC1-33 (l.766-767) and RFC6-28 (l.490-491) both read *"**Rows are per observable consequence, not per clause.** A clause with five observable consequences and one mapped requirement is not covered"*. Citation correct and correctly numbered. |
| **(d)** False absence claim gone? | **CLEARED** | No sentence asserting "no other statement of it exists" survives (`re` scan: 0 hits for `no other statement` / `exists nowhere` / `only statement`). The five-field record is gone (0 hits for `five-field` outside history). The absence claim now appears only as *"defended that with an absence claim a 398-file sweep falsifies"* inside the `*(History: …)*` note. |
| **(e)** Do the retained additions contradict the cited modules? | **CLEARED** | `[Inferred]` The "applicable" definition opens no bypass: it routes non-applicability through the same gate — *"saying so is an N/A judgment, not an omission"* — and the production obligation forecloses reviewer-grade discharge in terms: *"A matrix whose N/A rows rest on anything less — the author's or a **reviewer's** say-so, a judgment recorded only inside the spec — does not discharge this clause."* The production obligation (*"the specification ships with its coverage matrix, and every N/A row in that matrix cites the owner judgment's record in `decisions/`"*) is additive to, not weaker than, the modules' deliverable obligation (RFC6-28: *"must produce, as a deliverable, a **clause-to-requirement coverage matrix**"*). |

**BLOCKER 1: CLEARED on all five limbs.**
## 3b. Citation check (task 3)

`[Observed]` All five clause identifiers CC-SPEC-8 now cites are real, correctly numbered, and carry the rule the clause attributes to them:

| Cited | Located at | Carries the home/gate sentence? | Carries the per-consequence unit? |
|---|---|---|---|
| RFC1-33 | `rfcs/RFC-0001-…-state-planes.md` l.750 | yes (l.759-764) | yes (l.766-767) |
| RFC6-28 | `rfcs/RFC-0006-…-drawer.md` l.473 | yes (l.484-488) | yes (l.490-491) |
| RFC7-38 | `rfcs/RFC-0007/rendering-and-surface.md` l.319 | yes (l.327-332) | yes (l.347-351) |
| RFC8-32 | `rfcs/RFC-0008/accounting-reconciliation-and-release.md` l.313 | yes (l.321-326) | yes (l.340-344) |
| RFC9-52 | `rfcs/RFC-0009/interaction-parity-and-release.md` l.304 | yes (l.313) | yes |

Terminology check: CC-SPEC-8 calls these *"the confirmed contract modules"*. `PROCESS-GLOSSARY.md` defines **confirmed** as *"An independent fresh-context reviewer examined the exact bytes and returned `CONFIRM`. Says the bytes are ready to be offered — **still binds nothing**"*, distinct from **accepted**. The word is used correctly and asserts no binding force.

## 4. New findings

**No new launch blockers.** Four non-blocking findings.

**N1 — Stale cross-reference: CC-SPEC-11 still points at CC-SPEC-8 for a confirmer pattern the repair deleted.** `[Observed]` CC-SPEC-11 reads *"The table is **confirmed by a party other than the specification's author** (the CC-TEST-4 pattern, as CC-SPEC-8)."* CC-TEST-4 does carry that pattern (*"the classification … is **never made by the implementing agent alone** … confirmed by the change's reviewer (or the owner where no reviewer exists)"*), so that half is sound. But the repair's own history note states *"the contract's owner gate subsumes the 2026-08-13 confirmer limb"* — CC-SPEC-8 no longer instantiates a reviewer-grade confirmer. The trailing "as CC-SPEC-8" now re-implies the exact reviewer-grade confirmer BLOCKER 1 removed. **Five-part test: fails (2)** — no adopted doctrine, owner-approved policy, or confirmed contract clause is violated; CC-SPEC-11's obligation stands on CC-TEST-4 independently, so implementation cannot be led astray. **Suggested fix:** drop "as CC-SPEC-8", or repoint to CC-SPEC-6, which retains its confirmer limb (l.219).

**N2 — CC-SPEC-8's headline and first coverage sentence still use the per-clause unit.** `[Observed]` *"Applicable contract **clauses** are covered or lawfully N/A … every applicable clause is covered by requirements or carries a reviewed N/A judgment"*, corrected two sentences later by the explicit unit sentence. **Fails (5)** — self-correcting inside one paragraph; a reader reaching its end is not misled. Cosmetic.

**N3 — The citation names 5 of the 9 modules that state the rule, with no non-exhaustive marker.** `[Observed]` Python `re` sweep, **denominator 343 `.md` files under `contracts/candidates/`**, for the whitespace-normalized string `reviewed N/A judgment is a recorded owner judgment homed in`: **9 files, 9 occurrences** — RFC-0001; RFC-0002/`rendering-vocabularies.md`; RFC-0003/`manifests-and-namespace.md`; RFC-0004/`fidelity-joins-and-mappings.md`; RFC-0005/`admission-and-boundary.md`; RFC-0006; RFC-0007/`rendering-and-surface.md`; RFC-0008/`accounting-reconciliation-and-release.md`; RFC-0009/`interaction-parity-and-release.md`. This independently corroborates the banner's "nine contract modules". CC-SPEC-8 cites five of them. Because the text is identical in all nine, the citation is representative rather than wrong. **Fails (3)** — no counterexample yields a different outcome. Suggest inserting "including".

**N4 — Contract-side, noted not raised.** `[Observed]` RFC1-33's parenthetical *"(Shape-parallel with RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16, RFC11-12.)"* names RFC10-16 and RFC11-12, which returned **0 hits** in the sweep above. Out of scope for this review (neither is a subject); flagged for whoever owns the contract plane.

**Subjects 2 and 3 (task 4, coherence scope).** `[Observed]` `grep -F "CC-SPEC-8"`: **1 hit in subject 2** — the banner line *"the sibling file gained CC-SPEC-11 and a completed CC-SPEC-8, neither of which alters the six-class identity this file consumes"* — a scope statement, not a reliance on CC-SPEC-8 being the rule's home, and still true after the repair. **0 hits in subject 3.** Neither subject contains a statement that relied on the deleted home claim. Both remain coherent with the repaired clause.

**Rest of subject 1 (task 4).** Banner, the f14/f15 findings rows, and the `*(History: …)*` note all describe the home claim as a *past, repaired* defect and match the current bytes. No contradiction found. `[Observed]` The three paths the banner references (`round-2026-08i/reviews/RD-69-p41-p42-combined-RAW.md`, `round-2026-08i/reviews/RD-69-DISPOSITION-REGISTER.md`, `round-2026-08i/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA-2.md`) all exist; their contents are `[Unknown]` to me by design.

VERDICT: CONFIRM WITH EXCEPTIONS
