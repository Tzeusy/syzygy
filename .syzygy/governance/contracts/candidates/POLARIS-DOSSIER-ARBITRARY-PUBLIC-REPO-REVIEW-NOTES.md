# Polaris dossier for an arbitrary public repository — round-3 review notes

> **Candidate — binds nothing.** This is the sibling record for the notes of
> the third fresh-context review of the candidate OpenSpec change
> `polaris-dossier-arbitrary-public-repo` (PR #400, bead `syzygy-mzge`).
> Under the owner's notes-only rule
> (`../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1), a round
> with no revise-level finding clears the exact bytes it read, and its notes
> go in a sibling record, never into the reviewed bytes. So this file sits
> outside the change directory and edits nothing in it. It signs nothing
> off, adopts nothing and performs no act: only the owner's own acts do that
> (VIS-4). It quotes no act digest, so nothing here is registered in
> `check_governance.py`.

Reviewed record: docs/reviews/R-ARBITRARY-PUBLIC-REPO-3-RAW.md

## What was confirmed

- **Subject:** the change directory
  openspec/changes/polaris-dossier-arbitrary-public-repo/, on PR #400.
- **Reviewed commit:** `b7a7758c22eb0e546a399340b3e2f3e827e137ee`.
- **Verdict:** `CONFIRM WITH EXCEPTIONS`, on line 2 of the raw named on the
  `Reviewed record:` line above, with seven findings, each a note; the raw
  closes "Every remaining finding is a note."
- Round 1 returned `REVISE` over `8a661db7` and round 2 `REVISE` over
  `9d8a9b12`; both raws are retained beside the round-3 raw
  (`R-ARBITRARY-PUBLIC-REPO-1-RAW.md`, `R-ARBITRARY-PUBLIC-REPO-2-RAW.md`), and
  their repairs are in the change's own history on PR #400.

## The notes and what happens to each

None is repaired in the reviewed bytes. **Notes 1, 2, 3, 4 and 6 are
owner-facing:** the owner should read them before answering packet Q2
(notes 1, 2 and 3), Q4 and Q5 (note 4) and Q6 (note 6). Notes 5 and 7 go to
implementation and to the next successor version.

### 1 — A "no" to Q2 does not cleanly strike every history passage (owner-facing, before Q2)

The change says every passage that admits history is marked and struck on a
"no". The review found history-dependent passages that carry no marker: the
clone-shape conditional "Where the standing record does not admit history",
the WHEN clauses of two scenarios, the disclosure and Case arms, falsifier
arms, and REQ-038's Case. The identity screen is referenced outside the
paragraph that defines it. So after a marker-only strike, the standing
record's history field would still decide the one-commit clone shape, and a
later standing-record version that "admits history" could lift the
local-commit refusal without any spec change (ancestor reads would stay
barred). The packet also does not say that a "yes" lifts the refusal of a
local commit made on top of a public one.

**Disposition.** Owner-facing. If the owner answers Q2 "no", the strike is
performed at sign-off by the successor that applies it, and it must: make
the clone-shape rule and the two scenarios unconditional; strike every
history-dependent passage the raw lists (raw, note 1) whether marked or not,
keeping the guard arms that refuse ancestor reads; and strike the history
field from the standing record (`design.md` §1). If the owner answers "yes",
the owner should know that a commit made locally on top of a public one is
then no longer refused by the clone-shape check, and rests on the operator's
publication declaration.

### 2 — Under "no", the pinned commit's own author and committer lines lose their withholding rule (owner-facing, before Q2)

The rule withholding author, committer and signature lines sits inside the
history paragraph. Under the recommended "no", REQ-037 has no rule for the
identity lines of the one commit object every standing run reads; REQ-033
has none either, so Redis runs have the same gap today. Exposure is small,
because commit messages cannot be cited without history.

**Disposition.** Owner-facing. The successor that applies Q2 moves the
author, committer and signature withholding out of the history paragraph so
it covers the pinned commit of every standing run, and keeps that falsifier
arm outside the strike list.

### 3 — The identity screen's limits (owner-facing, before Q2)

"An e-mail address pattern" is not a published predicate. The trailer list
is closed, so name-only trailers outside it (`Helped-by:`, `Approved-by:`,
`Requested-by:`, `Bisected-by:`, `Authored-by:`) pass, and they are not
"free prose" under the disclosed residual. A folded trailer's continuation
line is not withheld. A hash-not-body record of a short line such as a
sign-off can be confirmed by guessing.

**Disposition.** Owner-facing: if the owner answers Q2 "yes", these are the
privacy limits being accepted. The successor that keeps history publishes
the pattern (an over-match only withholds), adds a generic `-by:` trailer arm
beside the named list, withholds continuation lines, and notes the guessable
hash in Q2's privacy sentence.

### 4 — Maintainer text under `deps/` or `extern/` loses maintainer-stated status (owner-facing, before Q4 and Q5)

The third-party path class is defined by path, so text the maintainers
themselves wrote under one of its segments (for example a project's own
`deps/` README about how it vendors, or an `extern/` module of its own code)
is no longer maintainer-stated. REQ-038's "withdraws no maintainer-stated
advantage except one quoted from third-party text" and the packet's "no
advantage you have today is lost" therefore overclaim. [Unknown] Whether any
advantage in the existing Redis dossier quotes such a path was not checked.

**Disposition.** Owner-facing: before Q4 and Q5, the owner should read the
rule as withdrawing maintainer-stated status from all text inside the class,
whoever wrote it; that over-exclusion is the heuristic's cost. The next
successor rewords the sentence and either checks the Redis dossier's
advantage anchors against the class or states the Unknown in Q4.

### 5 — Three predicates are not yet testable as written (implementation)

`.gitattributes` semantics (set, unset, `=false`, deeper files and macros),
filesystem-path normalisation (lexical or symlink-resolving), and the
location from which the compared consent records are enumerated.

**Disposition.** Implementation obligation, fixed in the slice that
implements each predicate (`design.md`, slices 4 and 6): count
`linguist-vendored` only when git's attribute resolution at the pinned tree
sets it to true; state whether the path comparison resolves symbolic links;
name the directories or registry the compared records come from, with the
gate and its oracle reading the same list. Each choice is written into the
next successor's text, not decided silently in code.

### 6 — A later reversal of 10b would let REQ-038 reconstruct advantages (owner-facing, before Q6)

REQ-038 fails a reconstructed advantage "while that ruling stands
unreversed". If the owner answers Q6 "no" now and later reverses 10b by a
plain direction, REQ-038 starts admitting reconstructed advantages with no
new spec version (still barred from naming another project without a
maintainer quotation). The packet presents the reversal's effect as REQ-039
alone.

**Disposition.** Owner-facing: reversing 10b later, by itself, would also
let 038 reconstruct advantages, though not comparisons with named projects;
039 only adds outside-source comparisons. The next successor adds that
sentence to Q6.

### 7 — Small accuracy items (next successor)

The packet says "four accepted contracts" where the change amends three
contract modules (RFC 0001, 0003, 0005) and seven clauses; `AMENDMENTS.md`'s
"four accepted contract clauses" fits only the consent half of its sentence.
`IMPACT-LEDGER.md` names only the round-1 raw where the change also retained
the round-2 raw and its `docs/README.md` row.

**Disposition.** Accuracy fix for the next successor version: "three
accepted contracts (seven clauses)", and "the round 1 and round 2 raws".
