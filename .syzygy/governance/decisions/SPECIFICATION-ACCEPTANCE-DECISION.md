# Owner decision packet — the specification-acceptance craft act (P-41)

> **This file decides nothing.** Written 2026-08-10 (RD30-07) so the
> blocking Capability 1 prerequisite P-41 has a packet like every other
> launch-critical decision, instead of only a register row. Repaired
> 2026-08-16 against review **RD-63** (`REVISE`,
> `../contracts/candidates/round-2026-08h/reviews/RD-63-p41-spec-acceptance-packet-RAW.md`);
> the repaired packet has had no fresh read.

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

**This act is not performable today.** The candidate was reviewed as
**RD-51**
(`../contracts/candidates/round-2026-08f/reviews/RD-51-spec-acceptance-and-impact-RAW.md`),
verdict **`REVISE`**, and was repaired on 2026-08-13 **by the session that
read the verdict** — a repair session cannot confirm its own repairs, so
the repaired bytes have had no independent read. The disposition register
(`../contracts/candidates/round-2026-08g/reviews/DISPOSITION-REGISTER.md`)
grades the twenty findings: 15 repaired, 4 repaired in part, **1
deliberately open** (f14, next paragraph). No ceremony phrase or digest
subject is minted for this act in `ACCEPTANCE-PHRASE-REGISTRY.yaml` — the
phrase is minted at the offering, after the review, with the digest
computed at the act (never transcribed in advance). What the owner *can*
do in this sitting is choose the route below; the act itself follows the
review.

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
obligation. The blocker repair **awaits its one confirming review**; until
that returns, `E5`'s "complete" limb is repaired-in-candidate, not `Met`.
Delta (both amendments): `../contracts/candidates/round-2026-08i/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA-2.md`.

## Ordering constraint (RD30-13) — satisfied 2026-08-16

**P-40 was ruled 2026-08-16** (SDR-37, the drafted rule confirmed as
written), so the constraint this section stated — do not freeze or review
CC-SPEC-1 before the granularity ruling — is **satisfied, not removed**:
CC-SPEC-1 is re-grounded on the recorded SDR-37 (2026-08-17 amendment)
and the freeze conditional is discharged. The review may now be
commissioned.

## Options

- **(a)** Order the review-then-act route: a fresh-context review of the
  candidate (CC-SPEC-1…11), repairs disposed, then the
  `CONFIRM CRAFT AMENDMENT` act binding the reviewed digest, recorded in
  the craft `INSTALL-RECORD.md` per the CC-TEST-2 precedent. Cost: one
  full cycle before the first spec can be judged acceptable — review,
  disposition, possible repair pass, freeze, act; the elapsed time is the
  price (b) exists to avoid. Benefit: the standard is in force and
  citable. It does **not** by itself make `E5` `Met` — f14's
  completeness limb stays open under this arm too.
- **(b)** Knowingly author the first spec against the unconfirmed
  candidate, recording that choice at the launch decision. Cost: the
  first spec's acceptance is judged against text with no act behind it —
  the judgment binds by the owner's acceptance of the spec itself, not by
  a standard in force; a later act may then invalidate criteria the spec
  was already judged by.
- **(c)** Decline a written standard for the first spec entirely; judge
  Capability 1's acceptability ad hoc at its own acceptance decision.
  Cost: launch-gate `E5` is `Not met`, and the instrument's §4 formula
  requires **every** E question `Met` for `READY FOR <target>` and for
  `READY-WITH-DEFERRALS` alike — E conjuncts are never deferrable — so
  (c) forecloses a `READY` verdict under the instrument as written, and
  the second spec inherits no bar.

## Recommendation

`[Inferred]` **(a)** — the review is one cycle, the precedent for the
form exists (the CC-TEST-2 amendment of 2026-08-02 — noting its own
confirming act, act 2, is still unperformed, so no craft amendment has
yet completed this route end to end), and `E5` is the one launch-gate
criterion whose owner is entirely inside this repository's control.
Stated with its limit: `E5` becomes citable only after the combined
review confirms the 2026-08-17 repairs, including whether CC-SPEC-11
closes f14's completeness limb.

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

**Review required:** one fresh-context review of `CC-SPEC-1…11`, and it
must cover the **repaired** bytes: the candidate was rewritten on
2026-08-13 and amended again on 2026-08-17, and no independent reader has
seen the result. Commission it
**jointly with `P-42`**, for two independent reasons: `CC-IMPACT-1`'s
spec-level declaration is generated as the union of `CC-SPEC-2`'s six
fields, and `CC-IMPACT-2`'s trigger set **is** `CC-SPEC-2`'s warrant set —
accepting one alone reintroduces two blocking defects. The combined
review's subject also includes **P-44**'s CC-REV-2 lagging-specification
amendment offer, so it is a three-subject review, not two.

**Exact next transaction.**

- Under **(a)**: commission the joint review (P-40 is ruled); disposition
  every finding; freeze the bytes; then `CONFIRM CRAFT AMENDMENT` over the
  frozen digest, recorded in the craft `INSTALL-RECORD.md`. No
  `CC-SPEC`/`CC-IMPACT` act row exists in the acceptance record yet — the
  act and its ceremony phrase are minted at the offering, after the
  review, not now.
- Under **(b)**: freeze today's bytes, compute the digest, perform the act
  over them, record it in `INSTALL-RECORD.md`, and record at the launch
  decision that the standard entered force with its post-`REVISE` repair
  unreviewed.
- Under **(c)**: one row in `SURFACE-DECISION-RECORD.md` recording that
  the first specification is judged ad hoc with no standard in force,
  naming the `E5` consequence above; the queue row closes citing it.

## Earliest required gate

Before the first specification is authored (`FIRST-OPENSPEC-SEQUENCE.md`
prerequisite row); after P-40.
