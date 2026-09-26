> # Record beside the package — not authority, binds nothing
>
> This file dispositions the notes of the eleventh fresh-context review of
> the opening-band scenario package. It is the "record beside the package"
> the owner's 2026-09-26 sitting record calls for (item 1, "Notes-only
> clears"); it is not a package artifact: `PWB-OPENING-BAND-SCENARIO-MANIFEST.txt`
> does not hash it, `scripts/build_pwb_opening_band_scenario.py` does not
> read it, and no act names it. `SEMANTIC-DELTA.md` §Review stays the record
> for rounds 1–10 and says nothing about round 11, as the sitting record
> directs. Nothing here offers a phrase or performs an act (VIS-4).

# Round 11 dispositions — opening-band scenario package

Written 2026-09-26 by the lead session that dispatched the round. Every
figure below was re-derived from the named source at the named commit in
this session, never copied from the raw (`git show "<commit>:<path>"`).

## The round

- **Reviewed commit:** `9162d622d67e3cba17c9691a5f19c3a8e4d2eded`. The
  sitting record names the package's current bytes as `3369410`;
  `git diff --stat 3369410 9162d62 -- .syzygy/governance/contracts/candidates/pwb-opening-band-scenario scripts/build_pwb_opening_band_scenario.py`
  is empty [Observed], so the round read the bytes the record names.
- **Raw:** `docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-CONFIRMATION-10-RAW.md`,
  retained verbatim (CC-REV-6); 595 lines; its head is four lines with no
  blank line, and its line 3 carries the manifest digest the reviewer
  computed twice [Observed].
- **Verdict (copied exactly from the raw's line 4):** `CONFIRM WITH EXCEPTIONS`.
- **Findings:** 49–52, all notes; no revise-severity finding [Observed —
  the raw's §Findings names no revise finding and its §Verdict rationale
  says so].
- **Effect under the sitting record, item 1:** a confirmation round that
  raises no revise-severity finding clears the exact bytes it read. This
  round clears the package bytes at `9162d62`, identical to `3369410`. The
  package is not edited by this record or by the commit that adds it:
  editing the reviewed bytes would retire the clearance.
- **What this does not do.** It performs no act and offers no phrase. The
  record's own "The recorder" bullet says the recorder accepts only an
  exact `Verdict: CONFIRM` line as of 2026-09-26 and may be changed only
  with its own fixtures and independent review; until that lands, no
  ceremony can rely on this round's verdict word. Landing order is the
  owner's (`.21` first, per the record's closing section).

## Dispositions

Numbering continues the package's: rounds 1–10 used findings 1–48.

### 49 — "sixteen scratch mutations and the hand-reproduced collision" (delta line 1314)

- [Observed] `SEMANTIC-DELTA.md` line 1314 at `9162d62` reads "ran the
  builder's three modes, sixteen scratch mutations and the hand-reproduced
  collision". The round-10 raw
  (`docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-CONFIRMATION-9-RAW.md`)
  uses exactly those words at its line 513.
- [Observed] That raw's mutation table has sixteen rows, `R10-M1` to
  `R10-M16` (`grep -c -F '| R10-M'` → 16 over the file), and row `R10-M16`
  (raw line 359) is the by-hand collision ("lane B's declaration patch,
  then this package's, by plain `git apply`"). Raw lines 361–362 partition
  the sixteen as fourteen fail-closed, `R10-M3` the documented non-failure,
  and `R10-M16` the collision.
- [Observed] The round-9 section, one section earlier in the delta, uses
  the other convention ("thirteen scratch mutations" over a fourteen-row
  table whose `R9-M10` is the collision).
- **Disposition — recorded, not edited.** The delta sentence attributes to
  the round-10 raw what that raw says, and the raw is uneditable. Read
  against the raw's table, the population is sixteen rows of which one is
  the collision, so the precise form would be "fifteen scratch mutations
  and the hand-reproduced collision, sixteen rows in all". This is the
  class of finding 37 (a raw's rationale counts differently from its own
  table; see the round-7 disposition in `SEMANTIC-DELTA.md` §Review). The
  sentence stands as the raw's words; a reader wanting the population
  reads the table. Under item 1 of the sitting record the sentence is not
  edited.

### 50 — five "put to the owner / no round 11" sentences

- [Observed] At `9162d62`: delta step 1 (lines 599–609, "**No round 11 is
  dispatched by this draft's author.**" … "the offering is the owner's to
  make"), the delta's round-10 section tail (lines 1324–1325, "whether a
  round 11 over these bytes is required is put to the owner (step 1
  above)"), the packet's status head (lines 43–46, "No round 11 has been
  dispatched.** Whether three consecutive confirmations with notes only…
  satisfy this gate"), packet step 1 (lines 274–276, "No round 11 is
  dispatched by the author: whether one is required is your call"), and
  the P-71 row of `docs/README.md` (line 85 at `9162d62`, "whether a
  further round is required is put to the owner").
- [Observed] Each was true when written (the bead's 2026-09-23 01:09
  comment put the question). The owner answered on 2026-09-26 (sitting
  record item 1: "One further round over them is next"), and this round is
  that round, dispatched by the lead session, not the draft's author.
- **Disposition — dispositioned by the ruling.** Item 1 of the sitting
  record says an exception the owner has already ruled on counts as
  dispositioned by that ruling. The four package sentences are stale as
  live state and stay unedited; the next reader routes to the sitting
  record and to this file. The fifth sentence, the README row, is a
  re-derived campaign row outside the package and is rewritten in the same
  commit that adds this record (rows there are re-derived, never
  maintained).

### 51 — "What explicitly does NOT change" item 3, the PWB-REQ-020 reading

- [Observed] Delta lines 183–195 at `9162d62` name two readings of
  PWB-REQ-020's "or disclosure Polaris presents", take the wider one
  without amending the requirement, and say "an owner who holds the
  narrower reading should say so before any act (round 5 finding 27)".
- [Observed] Sitting record item 2 answers "Wider reading (Recommended)"
  and says it "settles round-5 finding 27 of the `.21` review".
- **Disposition — dispositioned by the ruling.** The passage is the form
  round 5 asked for and round 6 (finding 33) passed; the owner has now
  said. No edit.

### 52 — builder rule-6 polarity of `dependency_patches_collide()`

- [Observed] `scripts/build_pwb_opening_band_scenario.py` lines 187–206 at
  `9162d62`: the function copies the current declaration into a scratch
  tree, applies `[theirs, mine]` (lane B's declaration patch, then this
  package's) and returns `True` on the first `ValueError`, whichever patch
  raised it. Its docstring reads "True when this package's and lane B's
  declaration patches conflict."
- [Observed, by reading the code] A lane B declaration patch that cannot
  apply at all therefore also returns `True`, so `--selftest`'s collision
  predicate passes on a broken lane B patch (the raw's `R11-M13c`), while a
  well-formed lane B patch that composes (`R11-M13d`) and a deleted lane B
  patch (`R10-M15`, the `is_file()` guard) both fail closed with the
  documented text. The raw's own reproduction is at its Finding 52; this
  record re-derives the polarity from the code, not from the raw's run.
- [Inferred] The package's sentences about the collision (delta 632–636,
  ledger 295–299, packet 296–298) hold for the shapes they contemplate: lane
  B's patch changing to one that composes, or its deletion. The undetected
  input, a lane B patch broken beyond applying, is lane B's own `--check`'s
  to report, and this package's `--check` catches it the moment the tree's
  declaration moves (its own patch then fails first).
- **Disposition — recorded; tightening deferred to the owner.** No package
  sentence is false on its context's reading. The builder is not a proposed
  byte and the manifest does not hash it, but a tightening changes the
  fixtures the package's prose describes and is a change under rule 10
  that needs its own round. It is filed as follow-up work on the tracker
  (see the bead comment of 2026-09-26 on `syzygy-dov.21` for its id) and
  is not done here.

## The raw's six non-finding observations

Recorded by the reviewer so the next reader need not re-derive them; none
asks for a change. One is dispositioned here because it is outside the
package and was already repaired:

- Observation (ii): at `9162d62`,
  `python3 scripts/check_docs_review_campaign_partition.py --check docs/README.md`
  exited 1 on the P-73 row (README 2 versus derived 4) and the count
  sentence (237 versus 239 tracked files). [Observed] PR #116 (`3ee61c7`,
  2026-09-26) recounted the P-73 row and the sentence to 239/239 over 52
  rows before this record was written; the commit that adds this record
  re-derives both again over 240 tracked files.
- Observations (i), (iii), (iv), (v) and (vi) (the `--selftest` traceback on
  a drifted `spec.md`, the `check_governance.py` anchor moves at `fe71755`,
  the "line 65" self-consistency, the ruling-record closing sentences, and
  the four-sibling composition population) are read as recorded and need
  nothing.

## What a later reader should check

- That the package bytes are still those of `3369410` / `9162d62`:
  `git diff --stat 9162d62 HEAD -- .syzygy/governance/contracts/candidates/pwb-opening-band-scenario scripts/build_pwb_opening_band_scenario.py`
  must be empty. Any non-empty diff retires this clearance (rule 10; sitting
  record item 1).
- That no act has been performed: `ACCEPTANCE-ACT-RECORD.md` carries no
  `SIGN OFF PWB OPENING-BAND SCENARIO` row as of 2026-09-26.
