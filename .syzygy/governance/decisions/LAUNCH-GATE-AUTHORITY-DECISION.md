# Owner decision packet — launch-gate process-policy authority

> **This file decides nothing, adopts nothing, approves nothing.** It is
> the exact owner decision required to put the launch-gate instrument into
> force as process policy. Queued in `PENDING-OWNER-DECISIONS.md` as
> **P-34**. Until this decision is recorded, the instrument is a candidate:
> its administrations are evidence the owner may weigh, and nothing more.

## Question

Approve `launch-gate-pre-specifications.md` **v1.10** as this repository's
owner-approved **process policy** for evaluating pre-specification
readiness?

> **Offer status (2026-08-10):** not yet offerable. v1.5's re-review
> (RD-33, `VERDICT: REVISE`) was closed by v1.6; v1.6's re-review (RD-34,
> `VERDICT: REVISE`) by v1.7; v1.7's re-review (RD-35, `VERDICT: REVISE`
> — one BLOCKING: the new citation-existence check shipped inverted) by
> v1.8; v1.8's re-review (RD-36, `VERDICT: REVISE`) by v1.9; v1.9's
> re-review (RD-37, `VERDICT: REVISE` — all seven RD-36 repairs verified,
> both decisive ones by mutation; instrument §1–§8 found byte-identical
> for the third amendment running; two MAJOR new findings: the v1.9
> negation rule, shared across checks of opposite polarity, silently
> LOOSENED LG-13 into accepting enumerated reopen lists led by a negation
> clause — a measured regression against v1.8 — and three §5 fields
> still resolved by first match, so a decoy line silently discarded the
> honest answer) is closed by v1.10 — a **validator-and-records batch**
> a third time; instrument §1–§8 have now gone four amendments
> byte-unchanged. The v1.10 batch adopts RD-37's uniformity rule: the
> shared predicate is split, every declared field parses through one
> disagreement-detecting helper, and a source-scan meta-fixture asserts
> the uniformity itself. Because the same session that authored the
> v1.10 bytes may not confirm them, the offer waits on a fresh-context
> re-review of the v1.10 delta (**RD-38**). The formal administration
> must not run on any earlier validator (the closing directions of RD-33
> through RD-37).

## What approval binds — and what it never binds

Approval makes the instrument the governing rule for **how readiness is
evaluated**: the question set, administration protocol, closed verdict
vocabulary, launch-scope parameters (§8), verdict formula, results-record
format, and trend log. That this list and the instrument's own `governs:`
header state the same scope is a **reviewable claim by the repair pass**
(RD24-03 asked for the alignment), not a settled fact: the owner verifies
it by comparing the two lists at the act, and rejecting the alignment —
narrowing either list — is open under option (b). Administration records
produced under it are evidence at a named commit.

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

- **(a) Approve v1.10 as offered.** The amendment records are
  `contracts/candidates/round-2026-08e/LAUNCH-GATE-v1.4-SEMANTIC-DELTA.md`
  (ten deltas; no question weakened; three questions added from the
  pilot's G1; launch-scope parameters for Capability 1 fixed in §8),
  `…/LAUNCH-GATE-v1.5-SEMANTIC-DELTA.md` (the RD-24 fresh instrument
  review's 21 findings closed — **read with the v1.6 delta's D-10**,
  which corrects two of its claims; the frozen record itself is not
  edited, RD34-10), `…/LAUNCH-GATE-v1.6-SEMANTIC-DELTA.md` (the RD-33
  re-review's twelve findings closed),
  `…/LAUNCH-GATE-v1.7-SEMANTIC-DELTA.md` (the RD-34 re-review's eleven
  findings closed — the `READY-WITH-DEFERRALS` predicate stated and
  checked, the citation shape test, the terminal-line parse; **read with
  the v1.8 delta's D-1**, which corrects D-2's existence-check claim),
  `…/LAUNCH-GATE-v1.8-SEMANTIC-DELTA.md` (the RD-35 re-review's
  seven findings closed — the citation-existence check un-inverted with
  its passing direction fixtured, the terminal line made the parsed
  anchor, the verdict-line target bound, E3's reopen-list enforced;
  **read with the v1.9 delta's D-1 and D-4**, which correct D-6's false
  `B-n` family claim and D-5's over-readable removal claim), and
  `…/LAUNCH-GATE-v1.9-SEMANTIC-DELTA.md` (the RD-36 re-review's seven
  findings closed — `B-n` out of the identifier family with the false
  taxonomy corrected everywhere it was asserted, empty fields made
  absent rather than borrowed, shadowed fields made errors, both
  citation forms existence-guarded; **read with the v1.10 delta's D-1**,
  which corrects D-4's false claim that the negation edge fails "never
  as a silent pass"), and `…/LAUNCH-GATE-v1.10-SEMANTIC-DELTA.md` (the
  RD-37 re-review's six findings closed — LG-13's emptiness made a
  positive closed-marker test with the shared predicate split, every
  declared field parsed through one disagreement-detecting helper with
  a meta-fixture asserting the uniformity, the G1 test anchored, the
  `--prior` record validated before trusted, the SDR guard anchored and
  scoped to made decisions; validator and records only — no question
  weakened; no ID renumbered; instrument §1–§8 byte-unchanged through
  four amendments).
- **(b) Approve with amendments** — state them; the changelog takes a
  v1.11 entry and the semantic delta extends. One prepared amendment the
  owner may take here: **promote F5 (assurance independence) from a
  recorded question to a verdict conjunct** — v1.10 deliberately leaves it
  non-gating at Administration 1 and discloses instead (RD24-12); making
  it a conjunct means no same-family administration can ever read READY.
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
v1.4's changes are exactly the pilot's own recorded gaps, v1.5's are
exactly the fresh instrument review's (RD-24: three of its findings were
mutation-proven against the named validator), v1.6's are exactly the
first re-review's (RD-33: five findings proven by constructing records
that validated clean and should not have), v1.7's are exactly the
second re-review's (RD-34: its BLOCKING finding was an all-Not-met record
validating clean under `READY-WITH-DEFERRALS`), v1.8's are exactly the
third re-review's (RD-35: its BLOCKING finding was the new existence
check rejecting every real decision path, invisible because no fixture
tested the passing direction), v1.9's are exactly the fourth
re-review's (RD-36: a pass verdict could rest on a deferral "granted"
by a review finding, certified by an accepting fixture asserting a
false taxonomy), and v1.10's are exactly the fifth re-review's (RD-37:
a record enumerating live E3 reopen items beside `E3 | Met` under a
READY verdict validated clean — the exact record §3 says cannot be
ready — because one predicate served three checks with two polarities;
each repair now has a fixture that fails without it — 86 in all, with
RD-37's uniformity discipline adopted and asserted by a meta-fixture,
and the four decisive repairs re-proven by mutation).

## Mechanism (the lawful transaction, prepared not performed)

The owner-act model here is digest-bound approval, as with craft policy
(D2 / `INSTALL-RECORD.md`), not a magic phrase. The order matters: the
status edit comes **first**, so the digest the approval binds is the digest
of the bytes that will actually be in force (RD24-01 — binding the
pre-edit digest would leave the approval attesting bytes that exist
nowhere once the header flips). To approve:

1. Edit the instrument's `status:` header — a governance-lifecycle state —
   from candidate to in-force, in the working tree. That edit is part of
   the act, not a later drift.
2. Compute the digest of the result:
   `sha256sum launch-gate-pre-specifications.md`
   This digest names the exact bytes being placed in force.
3. Record in this file, below this line, an approval block:

   ```text
   APPROVED — launch-gate v1.10 as process policy
   date: <date>
   instrument sha256: <the digest computed in step 2, post-status-edit>
   scope: process policy for pre-specification readiness evaluation;
          no administration verdict is an owner act
   by: the owner
   ```

4. Commit the status edit and the approval block in one change, with the
   approval in the message. Every later administration quotes and verifies
   this same digest (instrument §2 / LG-2), so the approval and the
   in-force bytes can never disagree.

Under **option (b)**, the ordering extends the same way (RD33-11): the
owner's amendments are applied to the instrument **in the working tree
before step 2's digest is computed** — together with the status edit and
the changelog's v1.11 entry — so the digest always binds the amended
bytes; the amendments, status edit, changelog entry, and approval block
travel in the one commit of step 4. An amendment applied after step 2
would recreate exactly the approval-attests-bytes-that-exist-nowhere
defect RD24-01 closed.

## Earliest required gate

Before the **formal** launch administration (the one a Capability 1 launch
decision would rely on). The pilot has already run; nothing else waits.

## Independent work

Everything — repairs, packets, reviews — proceeds regardless. Only the
formal administration's standing waits on this.
