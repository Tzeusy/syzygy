# Owner decision packet — launch-gate process-policy authority (P-34)

> **This file decides nothing, adopts nothing, approves nothing.** It is
> the exact owner decision required to put the launch-gate instrument into
> force as process policy. Queued in `PENDING-OWNER-DECISIONS.md` as
> **P-34**. Until this decision is recorded, the instrument is a candidate:
> its administrations are evidence the owner may weigh, and nothing more.
>
> *Rewritten 2026-08-11 as a bounded packet (owner charter §6.2). The
> repair chain it used to reproduce — thirteen versions, thirteen reviews —
> is linked, not restated. You should not need to understand a single
> Markdown parser failure to make this decision.*

## Question

Approve `launch-gate-pre-specifications.md` **v2.3** as this repository's
owner-approved **process policy** for evaluating pre-specification
readiness?

*(Repointed 2026-08-13 from v2.0, and 2026-08-16 from v2.2. This packet
once asked for v2.0 after the instrument had moved twice — it would have
routed the owner to bytes nobody offers, which is the defect review RD-8
called "the finding that converts act 1 from a knowing act into a
surprised one." Every v2.0, v2.1 and v2.2 digest is superseded and
satisfies nothing.)*

## What the policy governs

```text
the question set (A1–A6, B1–B5, C1–C7, D1–D4, E1–E6, F1–F6, G1)
the administration protocol — materials, order, who may administer
the closed verdict vocabulary
the verdict formula and its two pass branches
the launch-scope parameters (§8)
the structured administration record and its generated report
the trend log
```

## What it never governs

```text
whether specifications are authored          — that is your launch decision
the content of any artifact under judgment   — the gate judges, it does not author
any acceptance, adoption, or approval        — no verdict is an act (VIS-4)
```

A `READY` verdict authorizes nothing. It is evidence you may weigh when
making a separate launch decision, and a gate administered under an
approved policy is worth exactly as much as the administration behind it.

## What you would be binding

| Artifact | sha256 |
|---|---|
| `launch-gate-pre-specifications.md` (v2.3) | `3e65aaa39bd6525c70ce589fb3f0c029af91b1bb74b29966563d3f3dcf376294` |
| `launch-gate-administration.schema.json` | `e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb` |

The **schema digest is unchanged** across v2.0 through v2.3 — the
amendments changed how the instrument states its rules, not the record
format. That is the fact to check rather than take on trust.

Verify before acting — the digest belongs to the artifact, not to this
page:

```sh
# from the repository root — both artifacts live there, and this packet
# does not. Run from anywhere else and you get "No such file or directory",
# which reads like a missing artifact rather than a wrong directory.
cd "$(git rev-parse --show-toplevel)"
sha256sum launch-gate-pre-specifications.md launch-gate-administration.schema.json
```

## What changed at v2.0, in five lines — and what changed after it

The administration record stops being Markdown. It is JSON validated
against the schema above; the human report is generated from it and never
read back as authority; the verdict is computed and the schema **rejects** a
claimed one. §1, §3, §4 and §8 of the instrument are **byte-identical** to
v1.18 — no question's text moved, the formula is unchanged, and the
parameter block still binds. Full record of every change of meaning:
`../contracts/candidates/round-2026-08f/LAUNCH-GATE-v2.0-SEMANTIC-DELTA.md`.

**Why a format change rather than another fix:** thirteen consecutive
independent re-reviews of the Markdown record format each found a real
defect, and each repair minted the next. The chronology is
`launch-gate/HISTORY.md` and you do not need it to decide this.

**v2.1 through v2.3, in four more lines.** v2.1 repaired the two `REVISE`
verdicts returned against v2.0; its own two reviews returned `REVISE`
again, converging on one blocking defect, and v2.2 repaired that. v2.2's
two reviews (RD-61/RD-62, 2026-08-16) returned `REVISE` a third time —
**converging again on one defect**, in the v2.2 additions themselves —
and v2.3 is that repair, the version this packet now binds. **v2.3's own
pair (RD-65/RD-66, 2026-08-16) returned `REVISE` a fourth time**, this
round on the *class* of defect rather than one instance (see the verdicts
section). Deltas:
`../contracts/candidates/round-2026-08g/LAUNCH-GATE-v2.1-SEMANTIC-DELTA.md`,
`…/round-2026-08g/LAUNCH-GATE-v2.2-SEMANTIC-DELTA.md` and
`…/round-2026-08h/LAUNCH-GATE-v2.3-SEMANTIC-DELTA.md`.

**v2.3's own review pair was dispatched in the same round that repaired
it** (RD-65/RD-66) — the first time the repair and its re-review travel
together. **They returned 2026-08-16, and both returned `REVISE`** — the
fourth consecutive `REVISE` pair. This packet stays prepared, not offered,
and the fourth `REVISE` is now the live question under arm (c) below,
not a reason to route to a v2.4 that does not exist.

## Independent review verdicts

> **Two reviews are required, against the version being approved, before
> this decision is offerable.** The owner charter (§5.6, §14) commissions a
> policy-semantics review — *did this version weaken any readiness question
> or formula?* — and a structured-record review — *can malformed or
> contradictory data produce a false READY, and does the generated report
> faithfully present the canonical record?*
>
> **Status 2026-08-16: the required pair has now been run against v2.0,
> v2.1, v2.2 and v2.3 — eight reviews, eight `REVISE` verdicts.** The v2.3
> pair (RD-65/RD-66) returned this same day, both `REVISE`. This packet is
> therefore still **prepared, not offered**, but the reason has changed
> once more: it is no longer "nobody has looked at the repair" — the look
> is done, and it asked for more changes. That makes the fourth `REVISE`
> the decision arm (c) below now turns on.

| Review | Subject | Verdict (copied exactly) |
|---|---|---|
| Policy semantics | **v2.0** instrument | `REVISE` — RD-48, 2026-08-11, frozen commit `e2efda6` |
| Structured record | **v2.0** schema, validator, renderer | `REVISE` — RD-47, 2026-08-11, frozen commit `e2efda6` |
| Policy semantics | **v2.1** instrument | `REVISE` — RD-55, 2026-08-13 |
| Structured record | **v2.1** schema, validator, renderer | `REVISE` — RD-56, 2026-08-13 |
| Policy semantics | **v2.2** instrument | `REVISE` — RD-61, 2026-08-16, frozen commit `918574c` |
| Structured record | **v2.2** schema, validator, renderer | `REVISE` — RD-62, 2026-08-16, frozen commit `918574c` |
| Policy semantics | **v2.3** — the version this packet binds | `REVISE` — RD-65, 2026-08-16, frozen commit `494acab` |
| Structured record | **v2.3** | `REVISE` — RD-66, 2026-08-16, frozen commit `494acab` |

**Eight reviews, eight `REVISE` verdicts, across four versions.** Each pair
was dispatched separately in fresh context, neither seeing the other's
output. The v2.3 pair verified the repair account fairly: RD-65 confirmed
**nothing was weakened** v2.2→v2.3 and six of RD-61's eleven findings
repaired outright; RD-66 confirmed **eight of RD-62's thirteen** repaired,
each verified by reverting its fixture, with selftests at 119/34. But both
returned `REVISE`, and the pattern is no longer "narrower each round":
**RD-66's blocking finding is the same document-forgery class the tool has
closed twice before** (RD-47 f2 → RD-56 f2 → RD-62 f1), reproduced at a
free-text site — `prior_record.path` — that no prior review named, in a
record that validates with zero errors and exits 0. RD-65's third finding
is the same shape: RD-61 f1's eligible `READY FOR` outcome surviving at the
schema's new `HEAD` binding. RD-66 diagnoses the mechanism: each pass
repairs the *instances* its reviewers name and restates the result as a
*class property*, so the next review finds the class at a new address.

**v2.3 repaired the RD-61/RD-62 findings; its own review is now complete and
returned `REVISE`.** A repair session could not confirm its own repairs, and
the fresh reading did not confirm them either. The full disposition of all
eleven v2.3 findings, with a fix shape for each, is
`../contracts/candidates/round-2026-08h/reviews/DISPOSITION-REGISTER.md`;
the raw bytes are `RD-65-launch-policy-v2.3-RAW.md` and
`RD-66-launch-machinery-v2.3-RAW.md` beside it. Tracked as `syzygy-6j8`,
which stays open.

Both reviewers are the **same model family as the corpus authors**, so
under the charter each supports repair and neither is the formal launch
administration. Raw bytes:
`../contracts/candidates/round-2026-08f/reviews/RD-47-launch-record-schema-RAW.md`
and `…/RD-48-launch-policy-v2.0-RAW.md`; the repair account, including
which findings are open and why, is that directory's
`DISPOSITION-REGISTER.md`.

**What they found, in one line each.** RD-48: **no readiness question,
row-level verdict word, or trend column was dropped, renamed, or made
unreachable** — the weakening question the charter asked is answered *no*.
It nonetheless found two structural discrepancies: the *computed* formula
carries a sixth core conjunct that §4 does not state (a strengthening,
grounded in §3's E3 rule, but not a term the instrument carries), and the
gate-level verdict word `NOT READY` has no home in §1–§8 although the tool
emits it. RD-47 found five material defects in the validator's decision
path, of which the load-bearing one is that the schema audit never requires
an object schema to close, so deleting a single `additionalProperties`
re-opens the claimed-verdict route the v2.0 design rests on.

**Those v2.0 findings were repaired at v2.1, whose own reviews then returned
`REVISE`, repaired in turn at v2.2, whose reviews returned `REVISE`, repaired
at v2.3, whose reviews (RD-65/RD-66) returned `REVISE` on 2026-08-16.** What
has never happened, across four versions and eight reviews, is a review that
returned anything other than `REVISE`.

## Known residuals

Carried from the delta's disclosed limits — each measured, none
generalized:

1. The validator reads the instrument's own §8 prose in **one** place, to
   bind E4's fixed cases. Bounded and fail-closed, and disclosed rather
   than claimed absent.
2. The JSON Schema interpreter is a documented **subset**. Its safety
   property is that it rejects any keyword it does not implement; it is not
   the reference implementation.
3. Presence tests on free-text fields are **content-blind** by design. A
   reviewer who writes a plausible false evidence quote defeats this tool,
   and no version of it has claimed otherwise.
4. **No administration has been performed under any v2.x version.** The
   verdict path is fixture-proven, not field-proven. The only administration
   on record anywhere is the 2026-08-09 pilot, at v1.3, which returned
   `GATE VERDICT: NOT READY`.
5. F5 (assurance independence) is **not** a conjunct of the formula. Every
   administration so far has been by the corpus authors' model family.
   Promoting F5 to a conjunct is an owner option — see below.

## Your options

**(a) Approve v2.3 as process policy now.** *(Cost restated 2026-08-16
after RD-65/RD-66 returned.)* The v2.0 through v2.2 findings **have** been
repaired — that is what v2.3 is — and the independent reading of v2.3 is
now **complete**, not in flight. What it means is therefore sharper than
before: **approving bytes two fresh-context reviews have just returned
`REVISE` on**, with eleven open findings — one of them a BLOCKING
document-forgery that renders a false `READY FOR` into the report of a
record validating with zero errors (RD-66 f1). None of the eleven changes
a record's *eligibility* (RD-65 and RD-66 both confirm no new false-eligible
`READY` path was opened by the amendment; RD-66 f1 is a report-rendering
forgery, and RD-65 f3 requires a committed governance violation to trigger)
— so this is a lawful owner choice to approve a policy whose reviewers ask
for more, with the residuals known and listed rather than hidden. The
instrument becomes the standard a formal administration is run under.

**(b) Approve v2.3 with F5 promoted to a conjunct.** Same as (a), plus: a
`Not met` F5 blocks a READY verdict. This would block a pass on any
administration run by this corpus's own model family — the strictest
available reading of assurance independence, and a real constraint on who
can administer the gate.

**(c) Authorize one more repair round (v2.4), then re-review.**
**⇒ Owner ruling 2026-08-16: this arm is chosen.** The v2.4 repair round is
authorized and in progress — the eleven open findings repaired with RD-66's
structural fixtures at the core, a v2.4 semantic delta, and a fresh-context
re-review. This is a work authorization, not the policy approval: **P-34's
approve/decline stays open** and returns to the owner once the v2.4 review
pair reports. The v2.3 reviews (RD-65/RD-66) have now returned, both
`REVISE`, so this arm no
longer means "wait for the pending look" — that look is done. It now means
**spending a fifth repair-and-review cycle** on the eleven open v2.3
findings. What is genuinely new this time: RD-66 hands over a *structural*
fix, not another instance patch — drive the forgery test through **every**
schema-declared string field mechanically, and assert the sanitizer- and
lexicon-coverage sweeps themselves — which is aimed squarely at the
instance-vs-class mechanism the prior three rounds could not break. The
findings are bounded and each carries a fix shape (see the disposition
register). The cost is a fifth cycle and the standing risk, named in the
row below, that a class defect resurfaces at a site the v2.4 fixtures again
do not enumerate. **No longer a clean `[Inferred]` recommendation** — see
the weighing note.

*(The observable history, now complete for v2.3:* **the review pair has
been taken four times and returned `REVISE` all four.** Earlier rounds'
findings were narrower each time — v2.2's were confined to v2.2's own
additions — but the v2.3 pair broke that trend: RD-66's blocking finding
is the RD-47 f2 / RD-56 f2 / RD-62 f1 forgery class reproduced at a new
address, and RD-65's finding 3 is RD-61 f1's eligible-`READY FOR` outcome
surviving at a new address. This packet said, before the pair ran, that
"if it returns `REVISE` a fourth time, that is itself the answer to whether
this instrument converges, and it should be weighed against arm (a) rather
than absorbed as another round." **That fourth `REVISE` has now landed.**
The weighing arm (c) reserved for the owner is therefore live: (a) approve
v2.3 with its independent reading complete and asking for more changes, (c)
authorize the structural v2.4 fix that targets the recurrence directly, or
(d) decline. This session did not pre-empt that choice by repairing to
v2.4 — doing so would be the "absorbed as another round" this packet warns
against.)*

**(d) Decline.** The gate stays a candidate. Administrations remain
evidence you may weigh; no formal administration can be said to have been
run under approved policy, and the readiness standard's "the launch-gate
instrument is owner-approved" conjunct stays unsatisfied. *(That conjunct is
stated without a version number deliberately — naming one here is how this
page came to ask for v2.0 two versions after v2.0.)*

## The lawful transaction

There is no ceremony phrase for this decision and none is needed — it is a
recorded owner decision, not a digest-binding act. To approve, record in
this file, dated and signed in your own words:

```text
APPROVED — launch-gate as process policy, at the version whose digest is below
instrument sha256: <the digest you verified>
schema sha256:     <the digest you verified>
F5 promoted to a conjunct: yes / no
```

Then the queue row P-34 closes, and the formal administration becomes
runnable — by a reviewer outside this corpus's model family, or a human,
which is a requirement of the instrument and not of this packet.

## Earliest required gate

Before the **formal launch administration**. Not before the Wave A or Wave
B acts: the contract acts do not depend on this policy, and this policy
does not gate them.
