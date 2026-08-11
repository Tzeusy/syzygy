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

Approve `launch-gate-pre-specifications.md` **v2.0** as this repository's
owner-approved **process policy** for evaluating pre-specification
readiness?

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
| `launch-gate-pre-specifications.md` (v2.0) | `05ecaa954e81ef95f6e2e2b409fbcb5bd5391037c10d9624ab4af3217a00f6d2` |
| `launch-gate-administration.schema.json` | `e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb` |

Verify before acting — the digest belongs to the artifact, not to this
page:

```sh
# from the repository root — both artifacts live there, and this packet
# does not. Run from anywhere else and you get "No such file or directory",
# which reads like a missing artifact rather than a wrong directory.
cd "$(git rev-parse --show-toplevel)"
sha256sum launch-gate-pre-specifications.md launch-gate-administration.schema.json
```

## What changed at v2.0, in five lines

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

## Independent review verdicts

> **Two reviews are required before this decision is offerable. Both have
> now been obtained, and both returned `REVISE`.** The owner charter (§5.6,
> §14) commissions a policy-semantics review — *did v2.0 weaken any
> readiness question or formula?* — and a structured-record review — *can
> malformed or contradictory data produce a false READY, and does the
> generated report faithfully present the canonical record?*
>
> **Status 2026-08-11: dispatched and returned; findings unrepaired.**
> *(Corrected 2026-08-11. An earlier revision of this section read "neither
> has been obtained … not dispatched" and carried two `[Unknown]` rows.
> That was true when written earlier the same day — the authoring session
> could not spawn reviewer agents — and stopped being true when the reviews
> were run synchronously.)* This packet is **prepared, not offered**, and
> the reason has changed: it is not that nobody has looked, it is that two
> reviewers looked and asked for revisions that have not been made.

| Review | Subject | Verdict (copied exactly) |
|---|---|---|
| Policy semantics | v2.0 instrument | `REVISE` — RD-48, 2026-08-11, frozen commit `e2efda6` |
| Structured record | schema, validator, renderer | `REVISE` — RD-47, 2026-08-11, frozen commit `e2efda6` |

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

**None of these is repaired.** Each needs an amendment to the instrument or
a change to the validator's error surface, and both belong in their own
version with their own delta and re-review rather than beside a repair
batch.

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
4. **No administration has been performed under v2.0.** The verdict path is
   fixture-proven, not field-proven.
5. F5 (assurance independence) is **not** a conjunct of the formula. Every
   administration so far has been by the corpus authors' model family.
   Promoting F5 to a conjunct is an owner option — see below.

## Your options

**(a) Approve v2.0 as process policy.** *(Recommendation restated
2026-08-11, now that the reviews have returned.)* The earlier form of this
option said "recommended **only after** the two reviews return". They have
returned, and both said `REVISE` — so the condition it named is met in
letter and fails in substance. **Approving v2.0 as it stands means
approving an instrument whose two independent reviews asked for changes
that were not made**, including a formula the tool computes differently
from the way the instrument states it. That is a lawful owner choice with
the cost now stated; it is no longer the recommended one. The instrument
becomes the standard a formal administration is run under.

**(b) Approve with F5 promoted to a conjunct.** Same as (a), plus: a
`Not met` F5 blocks a READY verdict. This would block a pass on any
administration run by this corpus's own model family — the strictest
available reading of assurance independence, and a real constraint on who
can administer the gate.

**(c) Amend first.** Name what to change; the change travels as a semantic
delta and a v2.1 entry, and the two reviews re-run on the changed bytes.
**Recommended `[Inferred]`, as of 2026-08-11**, and the reviews name the
change list rather than leaving it to be invented: bring §4's stated
formula and the tool's computed one into agreement, give `NOT READY` a home
in the instrument body, and close the schema audit's open-object route. The
recommendation is inferred from two same-family reviews and is not itself
reviewed.

**(d) Decline.** The gate stays a candidate. Administrations remain
evidence you may weigh; no formal administration can be said to have been
run under approved policy, and the readiness standard's "launch-gate
v2.0 is owner-approved" conjunct stays unsatisfied.

## The lawful transaction

There is no ceremony phrase for this decision and none is needed — it is a
recorded owner decision, not a digest-binding act. To approve, record in
this file, dated and signed in your own words:

```text
APPROVED — launch-gate v2.0 as process policy
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
