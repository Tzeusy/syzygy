# Owner ruling — the retained evaluation record's `claimStates` key (2026-10-21)

Date: 2026-10-21 (the owner's answer, 11:59:19 UTC)

Owner: Tzeusy

Decision ID: `POLARIS-RETAINED-EVALUATIONS-CLAIM-STATES-RULING-2026-10-21`

Beside: `POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DIRECTION.md` (this
directory), the 2026-09-23 direction this ruling lays out and does not edit.
Its question is row P-79, arm A, of
`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`; gate bead
`syzygy-dov.28`; the bead this unblocks is `syzygy-dov.12.1`.

This is a plain owner direction in the sense of `PROCESS-GLOSSARY.md`, in the
family of the retention direction it sits beside.
- It binds no artifact digest.
- It adds no row to `ACCEPTANCE-ACT-RECORD.md`.
- It registers nothing in `scripts/check_governance.py`.
- It signs nothing and edits no signed byte, and it does not edit the
  retention direction.

## The owner's words

[Observed: an owner decision questionnaire dated 2026-10-21, item
`m12-retention-envelope`, answered through its token-gated local web form. The
actor and instants are those the form recorded in its local answers file. The
questionnaire and the answers file sit outside the repository, are local
only, and are never authority; this record quotes what it needs.]

- Actor/channel: owner via questionnaire web form (token-gated, from
  127.0.0.1).
- Answer recorded at: 2026-10-21T11:59:19+00:00. The form was completed at
  2026-10-21T11:59:38+00:00 with the owner's explicit instruction to apply
  the answers now.
- Questionnaire digest: the SHA-256 of the packet as ingested is
  `19b0fd4d7694569697eaa3f5af2e5e28df0d8b7f39513a0e3cb52d9bd593d1ae`.
- Owner edits: none. Post-answer review: none required, a plain selection of
  a presented option.
- Independent review of the item before it was offered: reviewer
  `rev-p108-k7q2m9`, round 2, "Scope verdict: Pass" and "Recommendation
  verdict: Pass" (the item's own adversarial-review record).

The question as put:

> May the retained evaluation record carry its per-claim states as a seventh
> top-level key?

Its "Decision needed":

> On 2026-09-23 you chose "six top-level keys" for the retained evaluation
> record, but none of the six holds the per-claim states the same direction
> authorizes. Decide whether the record may carry one more top-level key,
> `claimStates`, holding exactly those states. This is the only question that
> keeps M12 slice 1 (`syzygy-dov.12.1`) stopped. It has been stopped since
> 2026-10-04.

The owner selected **A**, whose full option text was:

> A. Add `claimStates` as a seventh top-level key; the six keys and the four
> `evaluation` members stay unchanged

The item's authorization boundary, as the owner answered over it:

> The owner selected this decision scope: one added top-level key,
> `claimStates`, in the retained evaluation record, whose entries hold only
> the claim identity, the epistemic tuple and the challenge state. The lead
> records the answer as a dated owner ruling beside the retention direction
> and on `syzygy-dov.12.1`, then rebases that branch (it forks at
> `178ca787`, 2026-10-04). Slice 1 then takes the shared-model slot at link 3
> of the PR #489 chain, under the retention direction and the 2026-09-05
> continuation act; it does not start at once. This packet releases no
> artifact mutation or live/external action; the canonical destination
> workflow must obtain and enforce every separate authorization it requires.

The item's explicit exclusions, copied verbatim:

> - renaming any of the six keys or the four `evaluation` members;
> - any fourth per-claim field;
> - dismissal (clause 7 excludes it);
> - a route or a listing of retained records;
> - pruning;
> - any change to clauses 2-9.

## The ruling

The retained evaluation record may carry **one added top-level key,
`claimStates`**. Its entries hold only the claim identity, the epistemic tuple
and the challenge state, which are the three per-claim things clause 1 of the
retention direction already authorizes. The six keys the owner chose on
2026-09-23 (`schema`, `evaluation`, `observerRevision`, `projectRevision`,
`claimCount`, `identityCount`) and the four `evaluation` members (`snapshot`,
`snapshotLabel`, `inputsDigest`, `asOf`) are unchanged.

The key set is therefore closed at the six named keys plus `claimStates`. The
exact-key test over a retained record asserts that set; a mutant that adds any
other key must fail it. [Inferred: the packet's recommendation, not the
owner's words; the owner's selection of A is the warrant for the key set and
the test is the lane's means of holding to it.]

Nothing about what is retained changes. [Inferred, the packet's reading: no
option changed what is retained, only where it sits in the record, so this is
a layout ruling and not a retention-posture change.] Clause 1's "Nothing
else" stands, and so do clauses 2-9 of the retention direction as issued:
the exclusions, the daemon-state-directory-only location, the unbounded
lifetime, the disclosure of record count and on-disk bytes, and the
withdrawal clause.

## How records are named, and what the owner did not ask

[Inferred: the lead's reading of the retention direction, which the packet
surfaced and the owner's selection of A did not rule on.] Each retained record
is named by the full evaluation identity of clause 1 (snapshot, snapshot
label, inputs digest, as-of instant), the identity that clause 4 and the
doctrine at `.syzygy/governance/doctrine/architecture.md` lines 295-298 carry
as four parts.

[Observed, disclosed rather than ruled: the offering the owner answered on
2026-09-23, `POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DECISION-PACKET.md`
(this directory), named records "by the evaluation's own input digest", and
its invariant I5 made naming by the as-of instant a mutation that must fail.
The owner did not adopt those invariants as authorization text, and the
2026-09-23 direction says so. The owner has not asked for digest naming. The
2026-10-21 item said that anyone who wants digest naming should say so in the
answer, and the answer says nothing of it.] [Inferred: the lead reads that
absence as no instruction to name records by input digest.] The reason the lead departs from
the offering: the same inputs at a later as-of instant can produce different
tuples, and digest naming would drop or refuse the later record, losing the
freshness transitions retention exists to keep. Clause 9 of the retention
direction still lets the owner narrow retention at any time.

[Observed: the packet's growth figure. The per-claim map measured 177,031
bytes over the 2026-09-13 population of 1,148 claims, in
`docs/evidence/polaris-m12-retained-evaluations-funnel-2026-09-15.json`.
[Unknown] the figure at today's population, which slice 1 measures. [Inferred]
under full-identity naming each human-triggered daemon start, re-observe and
materialize adds one record, about 177 MB per 1,000 records. Clause 5
discloses the on-disk total.]

## Placement

Slice 1 (`syzygy-dov.12.1`) takes link 3 of the chain recorded in
`OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-20.md`: after
opening band and container shape, immediately before dismissal. It runs under
the retention direction and
`PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`. The yield-the-slot
rule of the 2026-10-20 record applies to it, and it does not start at once.

The delta band's row cap (P-79 Q3) is untouched; the lead measures it at
slice 2.

## What this does not do

- It adds no per-claim field and renames nothing.
- It authorizes no dismissal; clause 7 of the retention direction excludes
  it, and the separate dismissal ruling of the same day keeps it so.
- It authorizes no route, listing or download of retained records, and no
  pruning.
- It changes no clause of the retention direction, and it widens no content
  class, read or egress.
- It signs, adopts or accepts nothing (VIS-4).

## Withdrawal

A later direction may narrow or withdraw this one; withdrawal defeats grant.
