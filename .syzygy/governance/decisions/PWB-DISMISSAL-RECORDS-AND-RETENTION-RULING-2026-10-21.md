# Owner ruling — where dismissal records live, and whether keeping one readable is a retention change (2026-10-21)

Date: 2026-10-21 (the owner's answer, 11:59:35 UTC)

Owner: Tzeusy

Decision ID: `PWB-DISMISSAL-RECORDS-AND-RETENTION-RULING-2026-10-21`

Answers questions 2 and 7 of the dismissal package
`.syzygy/governance/contracts/candidates/pwb-dismissal-expiry-amendment/OWNER-DECISION-PACKET.md`,
signed as `PWB-DISMISSAL-EXPIRY-AMENDMENT-SIGNOFF-v1.0.md` (this directory).
The register row is P-79 (`DECISION-HISTORY.md`); the beads are
`syzygy-dov.12.3` (dismissal) and `syzygy-dov.12.1`.

This is a plain owner direction in the sense of `PROCESS-GLOSSARY.md`.
- It binds no artifact digest.
- It adds no row to `ACCEPTANCE-ACT-RECORD.md`.
- It registers nothing in `scripts/check_governance.py`.
- It signs nothing and edits no signed byte.

## The owner's words

[Observed: an owner decision questionnaire dated 2026-10-21, item
`dismissal-records-and-retention`, answered through its token-gated local web
form. The actor and instants are those the form recorded in its local answers
file. The questionnaire and the answers file sit outside the repository, are
local only, and are never authority; this record quotes what it needs.]

- Actor/channel: owner via questionnaire web form (token-gated, from
  127.0.0.1).
- Answer recorded at: 2026-10-21T11:59:35+00:00. The form was completed at
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

> Whether any Butlers claim may be dismissed live, and where its record would
> live

Its "Decision needed":

> Answer the two questions the signed dismissal package left to you:
> - **Q2:** where dismissal records live and who writes them;
> - **Q7:** whether keeping a dismissal readable from a retained evaluation is
>   a retention change.

The owner selected **A**, whose full option text was:

> A. Q2: no home for now. Q7: yes, either way of keeping a dismissal readable
> is a retention change, and none is made now. The no-home arm is built on
> fixtures; the retained re-read limb stays unbuilt

The item's authorization boundary, as the owner answered over it:

> The owner selected this decision scope: the dismissal package's Q2 (home and
> writer) and Q7 (retention reach). A authorizes nothing new:
> `syzygy-dov.12.3` builds the signed no-home arm under the PR #489 record
> once it lands, after `dov.12.1`, and the retained re-read limb stays
> unbuilt. The lead records the answer as a dated owner ruling under
> `decisions/` (with the P-79 row and `DECISION-HISTORY.md`), and notes it on
> `dov.12.3`. This packet releases no artifact mutation or live/external
> action; the canonical destination workflow must obtain and enforce every
> separate authorization it requires.

The item's explicit exclusions, copied verbatim:

> Explicit exclusions, under every option:
> - any retention change, including a fourth retained field;
> - records in Syzygy's own tree;
> - any Butlers read outside `declared-project-shape-text`;
> - any write without its own act.

## The ruling

**Q2, where dismissal records live and who writes them: no home for now.**
No governed-plane home for dismissal records is designated, and no writer is
named. Syzygy writes no dismissal record, anywhere. Nothing is dismissed
live.

**Q7, whether keeping a dismissal readable from a retained evaluation is a
retention change: yes.** Either way of keeping it readable is a retention
change: keeping the record's bytes reachable from a retained evaluation, or
keeping a fourth field beside the three the retention direction lists per
claim (`POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DIRECTION.md`, clause
1). Each would need its own direction. **None is made now.**

**Consequences, as the option states them.**
- The signed no-home arm is built on fixtures. When an evaluation cannot read
  a dismissal record set, or no governed-plane home is designated, it
  dismisses no claim and discloses its dismissed count and the count of each
  record class as Unknown, never as zero (PWB-REQ-007, "Dismissal records").
- The retained re-read limb stays unbuilt, on fixtures as well as live. It is
  the clause of "A dismissal lapses only through a new evaluation" that says
  "reading the first evaluation again after the expiry instant has passed
  renders the same claim state". A lane that reaches it stops. The reason is
  now settled rather than open: building it needs a retention change, and the
  owner has made none.
- The question of where records would live reopens only with a later direction
  or act naming a home. The packet's other arms were B (the owner writes
  records by hand in Butlers' own governed plane, which Syzygy reads) and C
  (Syzygy writes the records into Butlers). Neither is chosen and neither is
  authorized here. [Inferred, the packet's reading: because the record set is
  injected, B can later be added as a new source rather than a rewrite.]

## Relation to the 2026-10-20 direction

`OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-20.md` forbids a
lane to build a write path for dismissal records, to read dismissal records
from Butlers, to choose or hard-code a home, to decide that dismissal bytes
stay reachable from a retained evaluation, and to change what the retention
direction keeps. Its sentence "This record answers neither" was true of that
record when written and stays so: it is that record's text, which this ruling
does not edit. This ruling answers questions 2 and 7 in the way that record
already fenced, so it removes no fence and adds none. The lane bound stays as
that record states it.

## What this does not do

- It authorizes no write, no read of dismissal records, no designated home and
  no retention change.
- It admits no record in Syzygy's own tree, and no Butlers read outside
  `declared-project-shape-text`.
- It builds nothing by itself. `syzygy-dov.12.3` builds the no-home arm under
  the 2026-10-20 record once that record is on `main`, after
  `syzygy-dov.12.1`; the claim-states ruling of the same day
  (`POLARIS-RETAINED-EVALUATIONS-CLAIM-STATES-RULING-2026-10-21.md`) decides
  the record layout `syzygy-dov.12.1` waited on.
- It signs, adopts or accepts nothing (VIS-4).

## Withdrawal

A later direction may narrow or withdraw this one; withdrawal defeats grant.
