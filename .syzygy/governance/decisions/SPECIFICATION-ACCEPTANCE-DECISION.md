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
(**CC-SPEC-1…CC-SPEC-10**): what a spec must name, how testability is
judged, and the coverage bar (CC-SPEC-8) a spec is reviewed against. It
binds nothing until its own `CONFIRM CRAFT AMENDMENT` act.

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

**What stays open under every arm.** RD-51 f14 is deliberately open: no
clause tests a specification for **completeness against its capability**,
so launch-gate `E5`'s "complete" limb stays unclosed **even under (a)** —
and the instrument forbids a halfway verdict (*"a caveat that matters
makes it `Not met`"*). Closing it means minting a clause no charter
directed, which would enlarge exactly what this act asks the owner to
approve; that choice rides with this ruling. f15 is repaired in part:
*"applicable"* remains undefined and the reviewed-N/A rule's identifier is
unresolved.

## Ordering constraint (RD30-13)

**Rule P-40 (granularity) before this act.** `CC-SPEC-1` states the
proposed granularity rule inline and says of itself: *"This clause may not
be frozen before P-40 is ruled."* If the owner rules P-40 differently or
declines it, the clause is amended before the craft act, not silently
re-pointed — so commissioning the review or freezing the bytes first would
spend a review cycle on bytes a P-40 ruling then amends.

## Options

- **(a)** Order the review-then-act route: a fresh-context review of the
  candidate (CC-SPEC-1…10), repairs disposed, then the
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
Stated with its limit: (a) makes `E5`'s other limbs citable; it does not
close f14's completeness limb, which no arm here closes.

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

**Pre-work required:** **rule `P-40` first** — the ordering constraint
above.

**Review required:** one fresh-context review of `CC-SPEC-1…10`, and it
must cover the **repaired** bytes: the candidate was rewritten on
2026-08-13 and no independent reader has seen the result. Commission it
**jointly with `P-42`**, for two independent reasons: `CC-IMPACT-1`'s
spec-level declaration is generated as the union of `CC-SPEC-2`'s six
fields, and `CC-IMPACT-2`'s trigger set **is** `CC-SPEC-2`'s warrant set —
accepting one alone reintroduces two blocking defects. The combined
review's subject also includes **P-44**'s CC-REV-2 lagging-specification
amendment offer, so it is a three-subject review, not two.

**Exact next transaction.**

- Under **(a)**: rule P-40; commission the joint review; disposition every
  finding; freeze the bytes; then `CONFIRM CRAFT AMENDMENT` over the
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
