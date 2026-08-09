# Owner decision packet — launch-gate process-policy authority

> **This file decides nothing, adopts nothing, approves nothing.** It is
> the exact owner decision required to put the launch-gate instrument into
> force as process policy. Queued in `PENDING-OWNER-DECISIONS.md` as
> **P-34**. Until this decision is recorded, the instrument is a candidate:
> its administrations are evidence the owner may weigh, and nothing more.

## Question

Approve `launch-gate-pre-specifications.md` **v1.4** as this repository's
owner-approved **process policy** for evaluating pre-specification
readiness?

## What approval binds — and what it never binds

Approval makes the instrument the governing rule for **how readiness is
evaluated**: the question set, administration protocol, closed verdict
vocabulary, launch-scope parameters, verdict formula, results-record
format, and trend log. Administration records produced under it are
evidence at a named commit.

Approval never delegates the launch decision itself: no administration
verdict — including `READY FOR <target>` — authorizes specification
authoring. That authorization is a separate owner act, taken reading the
evidence (VIS-4). The instrument's own header states this and approval
ratifies that statement.

## Current authority

None. The instrument is self-declared "not authority"; v1.3 was
administered once (2026-08-09, pilot) without any owner approval of the
instrument. The pilot's `NOT READY` verdict is steering evidence the owner
has already directed this pass to respect.

## Options

- **(a) Approve v1.4 as offered.** The amendment record is
  `contracts/candidates/round-2026-08e/LAUNCH-GATE-v1.4-SEMANTIC-DELTA.md`
  (ten deltas; no question weakened; three questions added from the
  pilot's G1; launch-scope parameters for Capability 1 fixed in §8).
- **(b) Approve with amendments** — state them; the changelog takes a
  v1.5 entry and the semantic delta extends.
- **(c) Decline** — the gate remains an informal checklist; readiness
  claims fall back to ad-hoc reports, the class this repository has twice
  found stale in the documents owners were sent to.

## Consequences

- (a/b): the next administration can be **formal** (Administration 1 of
  the trend log) once the §2 integrity requirements are met; F1 trend
  claims become possible at Administration 2.
- (c): no administration can be more than advisory; E-section closure has
  no agreed evaluator, and "ready" returns to being asserted rather than
  administered.

## Recommendation

`[Inferred]` **(a)**. The pilot demonstrated the instrument finds real
defects (its C1 finding — a retired phrase standing as the live gate in
two digest sets — was independently confirmed by the round-08d reviews),
and v1.4's changes are exactly the pilot's own recorded gaps.

## Mechanism (the lawful transaction, prepared not performed)

The owner-act model here is digest-bound approval, as with craft policy
(D2 / `INSTALL-RECORD.md`), not a magic phrase. To approve:

1. Verify the instrument digest:
   `sha256sum launch-gate-pre-specifications.md`
2. Record in this file, below this line, an approval block:

   ```text
   APPROVED — launch-gate v1.4 as process policy
   date: <date>
   instrument sha256: <the digest verified in step 1>
   scope: process policy for pre-specification readiness evaluation;
          no administration verdict is an owner act
   by: the owner
   ```

3. Commit with the approval in the message. The instrument's `status:` header — a governance-lifecycle state —
   header is then updated from candidate to in-force in the same change
   (that edit is part of the act, not a later drift).

## Earliest required gate

Before the **formal** launch administration (the one a Capability 1 launch
decision would rely on). The pilot has already run; nothing else waits.

## Independent work

Everything — repairs, packets, reviews — proceeds regardless. Only the
formal administration's standing waits on this.
