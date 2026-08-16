# Owner decision packet — the specification-acceptance craft act (P-41)

> **This file decides nothing.** Written 2026-08-10 (RD30-07) so the
> blocking Capability 1 prerequisite P-41 has a packet like every other
> launch-critical decision, instead of only a register row. Repaired
> 2026-08-16 against review **RD-63** (`REVISE`,
> `../contracts/candidates/round-2026-08h/reviews/RD-63-p41-spec-acceptance-packet-RAW.md`);
> the repaired packet has had no fresh read. **Updated 2026-08-17 to
> offering-ready state**: the subject's review cycle closed (RD-69 →
> blocker repair → RD-70 `CONFIRM WITH EXCEPTIONS`) and act 6 was minted
> at the offering.

## Question

Which route puts a specification-acceptance standard in force before the
first spec is authored — review-then-act, author against the unconfirmed
candidate, or no written standard? The candidate is
`../contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`
(**CC-SPEC-1…CC-SPEC-11**): what a spec must name, how testability is
judged, and the two coverage bars (CC-SPEC-8 clause coverage, CC-SPEC-11
capability completeness) a spec is reviewed against. It binds nothing
until its own `CONFIRM CRAFT AMENDMENT` act.

## Review state — stated plainly

**This act is performable: the offer is open.** The review chain, in
order: **RD-51** (`REVISE`,
`../contracts/candidates/round-2026-08f/reviews/RD-51-spec-acceptance-and-impact-RAW.md`)
→ the 2026-08-13 repair → the 2026-08-17 amendment (SDR-37 re-grounding,
CC-SPEC-11, CC-SPEC-8) → the combined fresh-context review **RD-69**
(`REVISE`, one launch blocker) → the one blocker-only repair → the
confirming review **RD-70** (**`CONFIRM WITH EXCEPTIONS`**, 2026-08-17:
blocker cleared on all five limbs, no new blocker). Raw reviews and the
disposition register: `../contracts/candidates/round-2026-08i/reviews/`.
The nine open findings (RD-69 N1–N5, RD-70 N1–N4) are all non-blocking
and travel with the offer, disclosed below.

**The ceremony phrase is minted — acceptance record §1, act 6:**

```
CONFIRM CRAFT AMENDMENT: CC-SPEC@9889b7e311ad941eec84d01dc2c035c7e2502a57cf18e68a1028a76d5b814871
```

The argument is the policy file's sha256 — the exact bytes RD-70
examined. Recompute it at the act (`sha256sum`, command below); if it no
longer matches, the bytes have moved, both reviews are retired, and the
act must not be performed. **Perform jointly with act 7 (P-42), one
sitting** — the two files are one model.

**The formerly open findings — repaired, reviewed once, blocker repaired.**
RD-51 f14 (no completeness-against-capability clause) was deliberately
open until a charter directed its closure; the owner's convergence
direction (2026-08-17, §9.2) supplied that authority, and **CC-SPEC-11**
now states the bounded coverage model. f15's two open limbs were repaired
the same day, and the combined fresh-context review **RD-69**
(`VERDICT: REVISE`, raw in `../contracts/candidates/round-2026-08i/reviews/`)
found that repair's home claim to be its one launch blocker: CC-SPEC-8
had declared itself the reviewed-N/A rule's one home over nine contract
modules that already state the rule with a stricter owner gate. The
blocker was repaired 2026-08-17 — CC-SPEC-8 now cites
RFC1-33/RFC6-28/RFC7-38/RFC8-32/RFC9-52 for the judgment's home, gate,
unit, and effect, keeping the "applicable" definition and the production
obligation. The confirming review **RD-70** returned
**`VERDICT: CONFIRM WITH EXCEPTIONS`** (2026-08-17): the blocker is
cleared on all five limbs, no new blocker, four non-blocking findings
batched to the next authoring pass (register in
`../contracts/candidates/round-2026-08i/reviews/`). `E5`'s "complete"
limb remains not `Met` until the craft act is performed and a formal
administration says otherwise.
Delta (both amendments): `../contracts/candidates/round-2026-08i/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA-2.md`.

## Ordering constraint (RD30-13) — satisfied 2026-08-16

**P-40 was ruled 2026-08-16** (SDR-37, the drafted rule confirmed as
written), so the constraint this section stated — do not freeze or review
CC-SPEC-1 before the granularity ruling — is **satisfied, not removed**:
CC-SPEC-1 is re-grounded on the recorded SDR-37 (2026-08-17 amendment)
and the freeze conditional is discharged. The review may now be
commissioned.

## Options

- **(a)** Perform the act — the review-then-act route's review half is
  **done** (RD-69/RD-70 above). Verify the digest, then perform act 6
  jointly with act 7, recorded in the craft `INSTALL-RECORD.md` per the
  CC-TEST-2 precedent. Cost: minutes. Benefit: the standard is in force
  and citable, and `E5` finally has a citable owner — though only a
  formal administration can pronounce `E5` `Met`.
- **(b)** Knowingly author the first spec against the unaccepted
  candidate, recording that choice at the launch decision. Cost: the
  first spec's acceptance is judged against text with no act behind it —
  the judgment binds by the owner's acceptance of the spec itself, not by
  a standard in force; a later act may then invalidate criteria the spec
  was already judged by. (The candidate is now review-confirmed, which
  shrinks this arm's risk but does not change its structure.)
- **(c)** Decline a written standard for the first spec entirely; judge
  Capability 1's acceptability ad hoc at its own acceptance decision.
  Cost: launch-gate `E5` is `Not met`, and the instrument's §4 formula
  requires **every** E question `Met` for `READY FOR <target>` and for
  `READY-WITH-DEFERRALS` alike — E conjuncts are never deferrable — so
  (c) forecloses a `READY` verdict under the instrument as written, and
  the second spec inherits no bar.

## Recommendation

`[Inferred]` **(a)** — the review cycle is complete, the act is minutes,
and `E5` is the one launch-gate criterion whose owner is entirely inside
this repository's control. The precedent for the form exists (the
CC-TEST-2 amendment of 2026-08-02 — noting its own confirming act, act 2,
is still unperformed, so no craft amendment has yet completed this route
end to end; acts 6 and 7 performed jointly would be the first).

**Disclosed with the offer — the open items an owner should see before
acting** (full dispositions in
`../contracts/candidates/round-2026-08i/reviews/RD-69-DISPOSITION-REGISTER.md`):

- **RD-69 N1** `[Unknown]` — SDR-37's second limb ("one coherent change
  to one" capability) has no acceptance criteria yet; for Capability 1's
  *first* spec, change and capability coincide, so nothing blocks. What
  settles it: a change-scoped acceptance rule, decided when the first
  amendment-sized change exists.
- **RD-69 N2** — a requirement warranted by a ruled-but-unnumbered
  decision (P-33/P-35/P-38/P-39 pattern) is not distinguishable, on the
  face of a `decisions[]` citation, from a forbidden pending-decision
  citation; open row **P-43** owns the settling question.
- **RD-69 N5** `[Unknown]` — CC-IMPACT-7's blind-exercise pass (RD-59) is
  structurally invisible to any fresh-context review (its record lives in
  a barred `round-*/reviews/` file), so no combined review can confirm
  that satisfaction claim; the record exists at
  `../contracts/candidates/round-2026-08g/reviews/DISPOSITION-REGISTER.md`.
- **RD-69 N3, RD-70 N1–N3** — wording-level items (the six-class
  "warrant" set beside doctrine's four-class work-warrant set; a stale
  "as CC-SPEC-8" cross-reference; a per-clause headline corrected two
  sentences later; a five-of-nine citation without "including"), batched
  because editing the reviewed bytes before the act would retire the
  reviews (rule 10).
- **RD-70 N4** — contract-plane: RFC1-33's shape-parallel list names
  RFC10-16/RFC11-12, which do not carry the standardized sentence;
  deferred Wave C/D material, routed via `DEFERRED-WAVE-POSTURE.md`.

## Digest consequences and the exact next transaction

*(Added 2026-08-13.)*

| Arm | Wave A / Wave B manifests | Confirmations | What binds |
|---|---|---|---|
| **(a)** review, then act | **unchanged** | **both survive** | the **policy file's own digest**, computed at the act (`CC-TEST-2` precedent), never transcribed in advance |
| **(b)** author against the unconfirmed candidate | unchanged | both survive | nothing — the spec's acceptance rests on the owner accepting the spec, not on a standard in force |
| **(c)** no written standard | unchanged | both survive | nothing — no act is performed, so no digest binds; that absence is the recorded state |

**No arm touches a contract wave.** This is craft policy: neither manifest
regenerates and neither confirmation is retired under any arm (*retire* /
*survive* per `PROCESS-GLOSSARY.md`). What differs is whether anything is
in force when the first specification is judged.

**Pre-work required:** none remaining — the P-40 ordering constraint is
satisfied (ruled 2026-08-16, SDR-37).

**Review required: discharged.** The three-subject combined review
(CC-SPEC + CC-IMPACT + the P-44 offer) ran as **RD-69**, its one blocker
was repaired, and **RD-70** confirmed the repair — both fresh-context,
raw output stored verbatim in `../contracts/candidates/round-2026-08i/reviews/`.
Both reviews are same-model-family as the authoring sessions: sufficient
for this craft offering, **never for a formal launch-gate
administration**, which requires an out-of-family reviewer.

**Exact next transaction.**

- Under **(a)**, in one sitting, from the repository root:
  1. verify: `python3 scripts/check_governance.py` (CG-7d covers both
     act arguments), and
     `sha256sum .syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md .syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`
     — the results must equal act 6's and act 7's arguments exactly;
     any mismatch means the reviews are retired and the act stops;
  2. perform **act 6** and **act 7** (acceptance record §1 — the exact
     phrases live there);
  3. record both in the craft `INSTALL-RECORD.md` per the act-2 precedent.
- Under **(b)**: no act; record at the launch decision that the first
  spec is authored against a review-confirmed but unaccepted candidate.
- Under **(c)**: one row in `SURFACE-DECISION-RECORD.md` recording that
  the first specification is judged ad hoc with no standard in force,
  naming the `E5` consequence above; the queue row closes citing it.

## Earliest required gate

Before the first specification is authored (`FIRST-OPENSPEC-SEQUENCE.md`
prerequisite row); after P-40.
