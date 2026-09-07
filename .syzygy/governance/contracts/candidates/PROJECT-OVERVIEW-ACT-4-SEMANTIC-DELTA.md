> **Candidate — binds nothing, and nothing here has been applied.** This is
> a drafted proposal for the argument of owner act **4**, which has never
> been performed. `.syzygy/intent/OVERVIEW.md` is byte-unchanged; no word of
> it was edited to write this. An agent may draft a delta, never adopt one
> (VIS-4); the workflow this form sits inside is
> [`NORMATIVE-CHANGE-WORKFLOW.md`](policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md).

# Semantic delta OVW-1 — repair the two claims the public overview makes about doctrine and about current capability

**Artifact(s):**        `.syzygy/intent/OVERVIEW.md`
**Stable IDs affected:** none defined in this file. It cites **VIS-1** and
**VIS-2** by content today and by identifier under this proposal; it defines
no clause of its own.
**Change class:**        Clarifying (both edits), argued below
**Author:**              Claude Opus 5 agent session, drafted 2026-09-07
**Date:**                2026-09-07

## Why this exists

The owner ruled **P-58** and **P-59** on 2026-09-07, taking arm (a) on each:
repair both defects inside act 4's argument, folded into that act whenever it
is next taken up, and prepare the delta but do not perform it. Both defects
sit on the same page and cost the same one argument, so they travel as one
delta — a second edit later would retire whatever confirmation the first
earned. The ruling record is
[`DOCUMENTATION-ESTATE-OWNER-RULINGS-DECISION.md`](../../decisions/DOCUMENTATION-ESTATE-OWNER-RULINGS-DECISION.md);
the questions are P-58 and P-59 of
[`DOCUMENTATION-ESTATE-DECISION-PACKET.md`](../../decisions/DOCUMENTATION-ESTATE-DECISION-PACKET.md).

## Current meaning

**Edit 1 — the founding pair (line 22 and the two bullets below it).** The
page reads, exactly:

```text
Two rules everything else follows from:

- **No evidence means Unknown** — never green, never zero.
- **Doing the work is never proof the intent was satisfied.** Scheduled,
  completed, and merged are facts about *activity*, not about *intent*.
```

`README.md` opens with the same sentence and a different pair: VIS-1
(comprehensible truth, never comprehensible fiction) and VIS-2 (no evidence
means Unknown), each cited by identifier. So the two default-path front doors
each present a closed set of two founding rules, and the sets differ. In
`.syzygy/governance/doctrine/vision.md`, VIS-1 is at line 82 and VIS-2 at
line 96; the activity-is-not-proof clause is at line 23, inside the preamble,
and is not a numbered rule [Observed — swept 2026-09-06 and re-checked
2026-09-07 by `grep -nF` for each rule heading in `vision.md` and for the
shared sentence in both pages].

**Edit 2 — current capability (line 125, under *What exists today*).** The
page reads, exactly:

```text
**Nothing is implemented** — no daemon, no UI, no store, no endpoints, no
chosen language, framework, or database. This page describes intended shape,
not current capability.
```

Every clause of that sentence is false as of 2026-09-07. Capability 1 and its
local daemon are implemented and running; the bounded Three-Surface POC has a
runnable implementation with HTTP endpoints; the language, framework and store
questions were answered by that implementation.
[`PROJECT-STATUS.md`](../../../../PROJECT-STATUS.md) owns that row and answers
differently.

## Proposed meaning

**Edit 1.** Replace the block quoted above with:

```text
Two rules everything else follows from:

- **Comprehensible truth, never comprehensible fiction** (doctrine
  **VIS-1**) — a simpler presentation is never bought with a less true one.
- **No evidence means Unknown** (**VIS-2**) — never green, never zero.

Doing the work is never proof the intent was satisfied: scheduled,
completed, and merged are facts about *activity*, not about *intent*. That
is doctrine's own opening premise rather than a third numbered rule.
```

The enumerated pair becomes the pair doctrine numbers first, cited by
identifier so a reader can check it; the activity-is-not-proof sentence keeps
its place in the surrounding prose and stops being presented as one of two.

**Edit 2.** Replace the sentence quoted above with:

```text
What is implemented today is stated once, in `PROJECT-STATUS.md`, and is
deliberately not restated here: this file's bytes are frozen by an owner
act, and any capability claim frozen inside it would go quietly false the
first time that capability moved. This page describes intended shape.
```

This is the move the very next paragraph of the page already makes for the
gate table, applied to the one row above it that was restated instead of
routed.

The replacement is given as plain text. When it is installed in
`OVERVIEW.md`, `PROJECT-STATUS.md` takes the same relative Markdown link
form that next paragraph already uses for the gate table; it is not written
as a link here, because a relative path inside this candidate resolves from
this directory rather than from `.syzygy/intent/`, and the link checker
follows links inside fenced blocks.

## What explicitly does NOT change

- **No doctrine changes.** VIS-1 and VIS-2 are unedited, unrenumbered and
  unmoved; `vision.md` is not touched by this delta. The page's relationship
  to doctrine changes from paraphrase to citation, which is why the class is
  Clarifying and not Normative.
- **The activity-is-not-proof premise is not retired, softened or demoted in
  meaning.** It keeps its full text; it stops being counted as one of two.
- **No gate, act, status row or capability claim moves.** Edit 2 removes a
  claim and routes to the page that owns it; it asserts nothing new about
  what is implemented.
- **`README.md` is not edited by this delta.** It already carries the
  proposed pair, cited by identifier; that is why the pair below is the one
  that moves.
- **The four-layer progressive-disclosure structure, the drawers, the
  machine-query-plane list and every other section are byte-unchanged.**
- **No other artifact's bytes change.** Only the act-4 argument's own digest
  is re-minted (below).

## Warrant

The owner's ruling of 2026-09-07 on P-58 arm (a) and P-59 arm (a). Before
that ruling, CC-REV-3: the same question — *which rules is everything else
downstream of?* — is answered in two homes and the homes disagree, and an
agent that finds this surfaces the contradiction rather than picking a
winner. Edit 2 additionally repairs a page restating state it does not own,
the failure shape three other default-path pages carried for nineteen days.

## Evidence or decision basis

- Register rows P-58 and P-59 in
  [`PENDING-OWNER-DECISIONS.md`](../../decisions/PENDING-OWNER-DECISIONS.md)
  as they stood before the ruling, and the packet sections that state each
  question in full.
- Act 4's row in
  [`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`](FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md)
  line 61, which names the file and its current argument. The argument is not
  quoted here: recompute it with `sha256sum` against that row (CG-7e/CG-15).
- `PROJECT-STATUS.md` for what is implemented, which this delta routes to
  rather than restates.

## Terms introduced / retired

None. No new durable term; no term renamed or retired. Both edits move
existing vocabulary already in the term registry.

## Downstream impact

Method: a full-corpus `grep -rlF` over all 1,003 tracked files, run
2026-09-07, for three strings — the path `intent/OVERVIEW.md`, the sentence
`Two rules everything else follows from`, and the sentence
`Nothing is implemented` — plus a fourth sweep for the act phrase
`ADOPT PROJECT OVERVIEW`.

- **Quoting either sentence:** five files besides the overview itself.
  Three — the packet, the register and `AGENTS.md` — quote it *because* it
  is the defect, and are repaired by the same pass that performs the act.
  The fourth is `README.md`, which carries the shared opening sentence with
  its own (correct) pair; this delta makes the two pages agree and edits
  neither of `README.md`'s bullets. The fifth,
  `round-2026-08b/reviews/RC-2-vision-polaris-RAW.md`, is retained raw
  reviewer output quoting it as evidence; per CC-REV-6 it is never
  rewritten, and its quotation becomes historical the moment the act is
  performed. **A review's referent may not be edited out from under it, but
  that constraint binds the review's own bytes, not the page's** — the raw
  keeps saying what the page said on the day it was reviewed.
- **Citing the path but not either sentence:** 96 files, out of 101 path
  citers over 1,003 tracked files. None of them reproduces either sentence,
  so none goes stale on this edit — the two figures share one denominator
  and the five above are the whole remainder (rule 9).
- **Machine-checked:** `scripts/check_governance.py` recomputes the
  overview's sha256 and compares it to the digest quoted in the acceptance
  record (the check is registered at lines 1880-1881), and CG-8 measures the
  page's authored region as part of the default load. Both must be re-run
  after the edit; the digest check **will fail until the acceptance record's
  act-4 row is re-minted**, which is the point of the migration step below.
- **`ACCEPTANCE-PHRASE-REGISTRY.yaml`** carries act 4's label and subject
  path, neither of which changes; it holds no digest.

## Migration / supersession plan

One logical change, in this order (CC-REV-2):

1. The owner applies both edits to `.syzygy/intent/OVERVIEW.md`, or directs
   that they be applied. **The file is act 4's prepared argument; editing it
   regenerates that argument and retires any confirmation bound to it.**
2. Recompute the file's sha256 by script, never by transcription (rule 3).
3. Re-mint act 4's row in
   [`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`](FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md)
   with the new digest, in that row's own established house form: a dated
   **re-quoted** note saying what moved the bytes and that the prior argument
   is stale and satisfies nothing. That row has been re-quoted four times
   before for exactly this reason, and each retirement is recorded there.
4. Re-run `python3 scripts/check_governance.py` and confirm the digest check
   passes and CG-8 raises no band finding.
5. Repair the three current-plane pages that quote the old sentences as
   defects — this delta's own packet row, the register row, and the
   `AGENTS.md` note that names the false sentence as queued under P-59 — so
   none of them goes on describing a defect that no longer exists. The
   retained raw review is not touched.
6. Only then may the owner perform act 4 against the new argument, if and
   when they take that act up. **This delta does not schedule act 4 and is
   not a request to perform it.** Applying steps 1-5 without performing the
   act is lawful and leaves the page correct and the act still open.

If the owner would rather not spend the argument now, the delta simply
waits — nothing is gated on it, and P-58's arm (b) (repair `README.md`
instead, which binds nothing) remains available as an interim, though the
owner did not choose it.

## Review

**Required class:** CC-REV-1 review of the class claim. Both edits are
argued Clarifying: no obligation is added, removed, narrowed or widened, and
the page carries no obligations to move. A reviewer who finds that promoting
VIS-1 into the enumerated pair changes what a reader is *bound* by should
reclassify this Normative and say so.
**Reviewer:** not yet assigned — must not have authored this delta or shared
its session.
**Verdict:** none. No review has been run against this draft.
