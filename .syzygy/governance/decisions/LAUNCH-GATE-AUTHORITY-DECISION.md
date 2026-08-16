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
and v2.3 is that repair, the version this packet now binds. Deltas:
`../contracts/candidates/round-2026-08g/LAUNCH-GATE-v2.1-SEMANTIC-DELTA.md`,
`…/round-2026-08g/LAUNCH-GATE-v2.2-SEMANTIC-DELTA.md` and
`…/round-2026-08h/LAUNCH-GATE-v2.3-SEMANTIC-DELTA.md`.

**v2.3's own review pair was dispatched in the same round that repaired
it** (RD-65/RD-66) — the first time the repair and its re-review travel
together. Until they return `CONFIRM`, this packet is prepared, not
offered.

## Independent review verdicts

> **Two reviews are required, against the version being approved, before
> this decision is offerable.** The owner charter (§5.6, §14) commissions a
> policy-semantics review — *did this version weaken any readiness question
> or formula?* — and a structured-record review — *can malformed or
> contradictory data produce a false READY, and does the generated report
> faithfully present the canonical record?*
>
> **Status 2026-08-16: the required pair has been run against v2.0, v2.1
> and v2.2 — six reviews, six `REVISE` verdicts — and the v2.3 pair is
> dispatched with verdicts pending.** This packet is therefore **prepared,
> not offered**, and the reason has changed with each round: first nobody
> had looked; then reviewers asked for changes; then the changes were made
> and nobody had looked at the result; now the look is running.

| Review | Subject | Verdict (copied exactly) |
|---|---|---|
| Policy semantics | **v2.0** instrument | `REVISE` — RD-48, 2026-08-11, frozen commit `e2efda6` |
| Structured record | **v2.0** schema, validator, renderer | `REVISE` — RD-47, 2026-08-11, frozen commit `e2efda6` |
| Policy semantics | **v2.1** instrument | `REVISE` — RD-55, 2026-08-13 |
| Structured record | **v2.1** schema, validator, renderer | `REVISE` — RD-56, 2026-08-13 |
| Policy semantics | **v2.2** instrument | `REVISE` — RD-61, 2026-08-16, frozen commit `918574c` |
| Structured record | **v2.2** schema, validator, renderer | `REVISE` — RD-62, 2026-08-16, frozen commit `918574c` |
| Policy semantics | **v2.3** — the version this packet binds | **dispatched, pending** — RD-65 |
| Structured record | **v2.3** | **dispatched, pending** — RD-66 |

**Six reviews, six `REVISE` verdicts, across three versions.** Each pair
was dispatched separately in fresh context, neither seeing the other's
output — and **each pair independently converged on one blocking defect**:
the eligibility limbs at v2.1, the schema's byte identity at v2.2. A
defect two independent readings land on is not a matter of taste, twice
over. The RD-61/RD-62 pair also verified the prior repairs held: nothing
weakened across v2.1 → v2.2, all ten RD-55 findings closed, an 814-site
injection sweep with zero leaks.

**v2.3 repaired the RD-61/RD-62 findings, and its own review is pending.**
A repair session cannot confirm its own repairs. The bytes this packet
binds are repaired-with-review-in-flight, and that is the single most
important thing on this page. Tracked as `syzygy-6j8`.

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
`REVISE`, repaired in turn at v2.2.** What has never happened is a review that
returned anything other than `REVISE`, and what has not happened yet is any
review of v2.2 at all.

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

**(a) Approve v2.3 as process policy now.** *(Repointed 2026-08-16.)* The
v2.0 through v2.2 findings **have** been repaired — that is what v2.3
is — so this arm no longer means approving an instrument with
known-unmade changes. What it does mean is **approving bytes whose
independent reading is still in flight**: the repair was made by the
session that received the verdicts, and a repair session cannot confirm
its own repairs. A lawful owner choice, and the cost is stated rather
than hidden. The instrument becomes the standard a formal administration
is run under.

**(b) Approve v2.3 with F5 promoted to a conjunct.** Same as (a), plus: a
`Not met` F5 blocks a READY verdict. This would block a pass on any
administration run by this corpus's own model family — the strictest
available reading of assurance independence, and a real constraint on who
can administer the gate.

**(c) Wait for RD-65/RD-66, then decide.** The two fresh-context reviews
of v2.3's exact bytes are **already dispatched** — for the first time in
the same round as the repair, so this arm's former cost (commissioning a
review nobody had ordered) is already paid. **Recommended `[Inferred]`,
as of 2026-08-16.**

*(The observable history:* **the review pair has been taken three times
and returned `REVISE` all three.** Each round's findings were narrower —
v2.2's were confined to v2.2's own additions, with everything earlier
verified closed. So the honest form of this recommendation is: **the
pending pair is the one that could return `CONFIRM`.** If it returns
`REVISE` a fourth time, that is itself the answer to whether this
instrument converges, and it should be weighed against arm (a) rather
than absorbed as another round.*)

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
