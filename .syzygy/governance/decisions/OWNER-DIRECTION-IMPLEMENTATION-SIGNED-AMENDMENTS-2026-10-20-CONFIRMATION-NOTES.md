# Confirmation notes — the 2026-10-20 implementation direction (2026-10-21)

Date: 2026-10-21

Sibling of: `OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-20.md`
(this directory), which this file does not edit and does not amend.

This is a record of what happened around the owner's confirmation of that
direction. It is not a direction, binds no artifact digest, adds no row to
`ACCEPTANCE-ACT-RECORD.md`, registers nothing in
`scripts/check_governance.py`, and authorizes nothing. The direction owns the
authorization; this file only holds what the direction's own text may not hold
once the owner has confirmed its bytes.

## The confirmation

[Observed: an owner decision questionnaire dated 2026-10-21, item
`sin5-confirm-direction`, answered through its token-gated local web form.
The questionnaire and its answers file sit outside the repository, are local
only, and are never authority.]

- The question as put: "Confirm the record of your 2026-10-20 implementation
  authorization (PR #489)?"
- Choice: **A**, whose full option text was "A. Confirm as recorded at
  `8c334f67`: the authorized rows, the two held rows, the three readings and
  the chain order".
- Actor/channel: owner via questionnaire web form (token-gated, from
  127.0.0.1). Answer recorded at 2026-10-21T11:59:04+00:00; the form was
  completed at 2026-10-21T11:59:38+00:00 with the owner's explicit
  instruction to apply the answers now.
- Owner edits: none. The record's body is therefore unchanged. The
  confirmation line in the record is the only edit made to it.
- The commit the owner was shown: `8c334f67e6883a5d229bf04512c65eeaa878a5ea`,
  head of draft PR #489 at that time. The record's SHA-256 at that commit is
  `f669546c788d5ed598b916cf1369d58b65e1825bd53adc33dec2b2f2ab963166`, computed
  by script and equal to the figure the PR reviewer recomputed.
- Independent review of the item before it was offered: reviewer
  `rev-p108-k7q2m9`, round 2, "Scope verdict: Pass" and "Recommendation
  verdict: Pass".

[Observed, provenance only: after the owner's answer the branch was rebased
onto a later `main`. The commit that carries the same record bytes on the
rebased branch is `4d3188e8583664217806cce9dace09ce1f16cbc3`, and the record
there has the same SHA-256. The commit `8c334f67` is therefore no longer
reachable from the branch, and a rebase-merge leaves both commits unreachable
from `main`. The SHA-256 is the stable anchor, as the reviewer's note 4 says
below.]

## The PR reviewer's round 3

Reviewer `rev-pr489-q8m3vt` had two `REVISE` rounds, each repaired once. Round
3 was a narrow verification at head `8c334f67`. Its verdict, copied exactly
from the raw: `Verdict: CONFIRM WITH EXCEPTIONS`. Its closing sentence, also
copied: "Nothing new of material weight was introduced. Under the declared
stopping rule, a notes-only round clears these bytes."

[Observed: the raw is `docs/reviews/R-PR489-SIGNED-AMENDMENTS-DIRECTION-3-RAW.md`,
retained byte-exact beside the round 1 and round 2 raws of the same
campaign. The five notes below are copied from it verbatim, labels included,
and the line citations in them refer to the record at `8c334f67`.]

Under the stopping rule of 2026-09-26, a notes-only round clears its bytes. The
notes are recorded here and the record is not repaired for them. Each
disposition is the recorder's.

### Note 1

> **Note. [Observed] The record contradicts itself on whether the gap-resolving authorization has a bead.** Record:246–247 says "The packet's third gate, the gap-resolving authorization, has no bead". Record:270–271 says it "is the drafted `syzygy-dov.19` continuation". The draft does fold it in: `pwb-m2-slice5-implementation-continuation/OWNER-DECISION-PACKET.md:61-65, 231-238` at `268f1773`. Reconcile the two sentences.

Disposition: not repaired, because the owner confirmed those bytes. Neither
sentence authorizes a row, and the rule that no row builds any part of the
missing-currency disclosure before the `syzygy-dov.19` act does not depend on
which of the two is read.

### Note 2

> **Note. [Observed / Inferred] The opening-band evidence answers a slightly different question.** The scenario's condition concerns registry declarations. The two constructors setting `FRESH` show only that the code never renders the condition.
>    - The conclusion still holds on both grounds: all 13 existing classes have registry rows, and the one class without a row (`governing-intent-relation`) is held back with item depth.
>    - Record:325–326 says "the classes with no bound", which has no existing referent.

Disposition: not repaired. The reviewer states that the conclusion holds on
both grounds, and that the phrase "the classes with no bound" has no existing
referent among the 13 declared classes.

### Note 3

> **Note, for the owner. [Observed / Unknown] A pre-existing defect is disclosed but not repaired.** Every tuple carries a constant `FRESH`, not a value derived from the 13 declared `maxAgeMs` bounds. The authorized opening band will aggregate those values.
>    - [Unknown] Whether any Butlers claim is older than its declared bound and is therefore shown fresh when it is not. I did not measure it.
>    - The record discloses this at record:316–331 and routes it to `syzygy-dov.2.2`. Under the declared stopping rule it goes to the owner as-is.

Disposition: this note was put to the owner as the item's central tradeoff.
The item offered option B, which would hold the opening band until
`syzygy-dov.2.2` lands, and recommended it; the owner selected A, which
confirms the record with the opening band authorized as recorded. The owner's
choice is preserved, not smoothed: the opening band may show counts built on
the constant `fresh` until `syzygy-dov.2.2` lands, as option A's own cost
column says. [Unknown] still stands for whether any Butlers claim is older
than its declared bound.

### Note 4

> **Note. [Observed / Inferred] The confirmation step has two follow-ups.**
>    - [Inferred] After a rebase-merge, the commit the line names will not be reachable from `main`. The SHA-256 remains the stable anchor, and the commit can still be fetched via `refs/pull/489/head`.
>    - The procedure does not say to move the PROJECT-STATUS gate row to the closed gates in the same commit. If that is skipped, the row will say "authorizes nothing" after a confirmed merge.

Disposition: the second follow-up is done. The commit that adds the
confirmation line also moves the `PROJECT-STATUS.md` gate row to the closed
gates. The first is accepted and is the reason the provenance paragraph above
exists. One correction to the note: this branch was rebased and pushed after
the owner's answer, so `refs/pull/489/head` no longer points at `8c334f67`;
the SHA-256 is the anchor, not the commit.

### Note 5

> **Note. [Observed] One sentence in the PR body overstates the mapping.** It says "Every selection maps to exactly one tag", but "Dismissal + item-depth" maps to two. The record itself says this correctly at record:94–95. Apart from that, the body matches the files at `8c334f67`: head, digest, mapping, sequencing, chain, bounds and check figures.

Disposition: repaired in the PR body, which is not a governed file, when the
PR was marked ready. The record was correct and is unchanged.

## Events after the confirmation

[Observed: the lead session relayed these; the first is also recorded in the
file named in it.]

- **The `syzygy-dov.19` continuation was given.** The owner gave it on
  2026-10-21T12:00:00Z in the words "Continue PWB implementation authorization
  for M2 slice 5 as drafted". Its record is
  `PWB-M2-SLICE-5-IMPLEMENTATION-CONTINUATION-DIRECTION.md` (this directory).
  It is dated after the confirmation instant above. The confirmed record's
  sentences that treat the `syzygy-dov.19` act as not yet performed were true
  when it was confirmed and are out of date now that the continuation's
  record is on `main`; that is marked here and not edited there.
- **What the continuation says about the two uses the confirmed record
  held.** [Observed: its B11 text.] It covers the relation claims of item
  depth (`syzygy-dov.14.4`) and the count of the opening band
  (`syzygy-dov.4.2`), through slice 5's one mechanism, with slice 5 landing
  ahead of both uses. It states that if the 2026-10-20 direction is not
  confirmed, B11 authorizes neither lane. The owner confirmed that direction
  at 2026-10-21T11:59:04+00:00, so that condition is met. The confirmed
  record's own rule still holds: no lane starts until its file is on `main`,
  and item depth starts only if the behaviour the continuation names covers
  its relation claims.
- **Three further answers were recorded the same day**, in
  `OWNER-DIRECTION-P108-IMPLEMENTATION-2026-10-21.md`,
  `POLARIS-RETAINED-EVALUATIONS-CLAIM-STATES-RULING-2026-10-21.md` and
  `PWB-DISMISSAL-RECORDS-AND-RETENTION-RULING-2026-10-21.md`. The second
  decides the record layout that `syzygy-dov.12.1`, link 3 of the confirmed
  chain, waited on. The third answers questions 2 and 7 that the confirmed
  record's Bounds section leaves unanswered; it removes no fence.

## What this does not do

- It does not repair, narrow or widen the confirmed record, and it does not
  authorize any row.
- It signs, adopts or accepts nothing (VIS-4).
