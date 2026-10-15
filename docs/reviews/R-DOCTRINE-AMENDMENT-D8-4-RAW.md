# Review - D8 doctrine amendment packet (Inferred first-class, P-102) — round 4
Reviewed commit: 79f51fdfa5350feb747162af91137758dc3b38ed
Package digest: 21198cac259b3ef68462632d774c83ed6dcba00361cf3dad643fa58db21bd8c3
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: a fresh-context agent that drafted none of this package (CC-REV-1).
Round 4 under `REVIEW-BRIEF.md` §"Round 4". Date 2026-10-14.

## Method

- `git fetch origin main`, then `git checkout --detach 79f51fdf`.
  `git rev-parse HEAD` returned
  `79f51fdfa5350feb747162af91137758dc3b38ed`, and `git status --short` was
  empty.
- **Package digest.** I computed it with a Python script that follows the
  brief's method. It takes `git ls-files` of the package directory, sorts
  by bytes, writes one `<sha256>  <path>` line per file, and hashes the
  concatenation. The population is 7 files: IMPACT-LEDGER.md,
  OWNER-DECISION-PACKET.md, REVIEW-BRIEF.md, ROUND-1-DISPOSITIONS.md,
  ROUND-2-DISPOSITIONS.md, ROUND-3-DISPOSITIONS.md and SEMANTIC-DELTA.md.
  As a second method, a plain `sha256sum` of IMPACT-LEDGER.md gave the
  same per-file hash as the script (`48f37307…`).
- **What I read.**
  - Package files: all seven, plus the diff of the package from the
    round-3 commit `b913d1ef` to the reviewed commit.
  - Doctrine: `trust-and-evidence.md` lines 30–70, 95–96, 134–137 and 144;
    `vision.md` lines 220–262; `architecture.md` lines 10–120.
  - Contract: RFC7-2 (lines 87–100) and the RFC7-20 and RFC7-21 locations
    in `narrative-contract.md`.
  - Code: `gate-acts.test.ts` lines 298–300, and
    `record_polaris_understanding_adoption.py` lines 240 and 592.
  - D7: its packet's Q6 and its ledger's recorder row (line 215).
  - Records: the round-3 raw, register row P-102 (now line 1245), and the
    `decisions/` listing.
- **Anchors and digests.** Checked by script:
  - All three doctrine sha256 values in packet §1 and in the delta match
    the bytes at the reviewed commit.
  - Six anchor quotations are byte-exact as blockquotes in the packet:
    `trust-and-evidence.md` 95–96, 44–49, 134–137 and 57–67; `vision.md`
    232–234; `architecture.md` 18–27.
  - Each insertion position (line 49/50, 67/68, 96/97, 137/138; `vision.md`
    234; `architecture.md` 27/28) lands where the prose says.
- **Full application probe at the reviewed commit.** I made two scratch
  clones at `79f51fdf`, one to apply the blocks to and one as a baseline.
  - In the applied clone, a script extracted exactly seven `markdown`
    fences from the packet. It asserted the three doctrine digests and
    each anchor line, then inserted every block at its stated position.
  - In each clone, the canonical battery block was read from
    `PROJECT-STATUS.md` and run line by line.
  - Results: baseline **100 commands, 0 nonzero**; applied **100 commands,
    6 nonzero**.
  - The 6 failures, each confirmed in its own output:
    - CG-18 FAIL, "20 measurements examined, 16 findings — 10 fixture(s) ×
      2 predicates";
    - budget report DRIFT in fixtures 1, 3, 5, 6, 7, 8, 9 and 10 and in
      `CONTEXT-BUDGET-REPORT.md`;
    - "05-CONTRACT-INDEX.yaml differs from regeneration";
    - "DIRECTIVE-REGISTER.md is stale";
    - the recorder's `--check`: "review retired by changed input:
      .syzygy/governance/doctrine/vision.md";
    - the recorder's `--selftest`: "candidate input drift" on the same path.
  - After insertion, VIS-7 sits at line 260 of the applied `vision.md`.
  - This reproduces the ledger's cycle-3 probe exactly, at a later commit
    with the same doctrine digests.
  - No repository file was edited.
- **Not re-run.** The term sweep and the static reader sweep. Round 3
  reproduced both at `09c7a61d`, and the cycle-3 repair did not touch
  them. One exception: the 13-reader prose, which I checked directly with
  a fixed-string `git grep` (below).
- **Process note.** The brief names `docs/reviews/R-DOCTRINE-AMENDMENT-D8-4-RAW.md`
  as the output path. The dispatcher told me to write this raw to a session
  scratchpad and to edit no repository file, and I did so. The head is the
  brief's four-line contract.

## Round-3 findings, checked in the bytes

1. **Repaired: revise-level, on the owner's ruling.**
   - **The dismissal is gone from (d2).** (d2)'s examples now read "a
     promoted annotation, an attributed answer". The general phrase
     "content Syzygy authors" is closed by an explicit exclusion: "A
     dismissal of such a project's gap is not committed there: it takes
     effect only in the project's own governed plane, so it waits for an
     act that names that write."
   - **This applies the ruling faithfully.** The owner said: "Dismissals
     of an observed-only project's gaps can't live in the observing
     project's tree, so VIS-6 stays intact."
   - **It is consistent with doctrine.** `trust-and-evidence.md` line 42
     says a decision "takes effect only once committed out to the governed
     plane". VIS-6's violation sentence (lines 246–248) names "a dismissal
     taking effect without living in the governed plane". The new sentence
     places the dismissal exactly where both require, so the dilemma
     round 3 found no longer arises.
   - **"A promoted annotation" is right.** VIS-6(a) promotes a note "(as
     an annotation or a dismissal)", and `architecture.md` line 102 uses
     "promoted annotations".
   - **"Never suppresses a gap" does not overreach.** Among the records
     doctrine names, only a recorded human decision may suppress a gap
     (line 40), and (b) already keeps an answer "beside an Unknown, never
     in its place". See note 5 for one scoping point in the last sentence.
   - **The restated places agree** [Observed]: §1 (d)'s "It is a governed
     project" paragraph, the SDR-30 caution, the offboarding sentence, the
     P-71 trade-off paragraph, the no-change arm, §2's (d) row, Q-C2,
     Q-D1, the delta's (d) meaning and its VIS-6 "does not change" bullet.
2. **Repaired: note.**
   - "(vision.md VIS-7)" is dropped from (e)'s bytes.
   - The Unknown sentence now reads "such a claim, resting only on such
     records, has no evidence and renders Unknown", scoped to the denied
     kind.
   - The heading is now "Self-observation never certifies Syzygy's own
     alignment", which matches the rule.
   - §1 (e) states the drafter's intent for the other triggers, and Q5
     gains a widening arm. That arm is stated fairly and not drafted.
   - The delta's "cites VIS-4 and VIS-6" is true of the bytes: (b) cites
     both and (d1) cites VIS-6.
   - Two residues remain outside the bytes (notes 1 and 2).
3. **Repaired: note.** (a) now reads "is no claim while it stays one".
   - This defers to RFC7-20 while the text is a draft.
   - It leaves RFC7-21's adoption act free to make the text curated
     narrative. Under RFC7-2(c), curated narrative admits "Inferred with
     its inference provenance".
   - It licenses nothing beyond RFC7-20 and RFC7-21: the clause still adds
     only obligations.
   - The dated note on freshness binding the draft "as a rendered object"
     answers round 3's side remark.
4. **Repaired in the ledger; one residue remains in the packet** (note 3).
   - `gate-acts.test.ts` lines 298–300 are as the ledger says: `const
     readme = '.syzygy/governance/doctrine/README.md'`, `write(root,
     readme, real(readme))`, `sha(real(readme))`.
   - A fixed-string `git grep` for `doctrine/README` over
     `packages/polaris-dossier` and the two dossier scripts returns exactly
     that one line [Observed].
   - Packet §9 step 3 now says the glossary edit is unprobed.
5. **Dispositioned as stated.** Register row P-102 carries the round-3
   mark at the Q1 sentence and a cycle-3 mark that describes the repair
   accurately. The row moved from line 1179 to line 1245; that is not a
   package matter.

## What holds [Observed unless marked]

- Acceptance criterion 4:
  - the diff `b913d1ef..79f51fdf` touches no doctrine file;
  - the package edits no contract, specification or code byte;
  - nothing is labelled adopted.
- D7 composition (§8, ledger §5 item 4):
  - D7's ledger line 215 now reads "**a gate, not a regeneration.**",
    with its own probe messages;
  - D7's packet carries Q6 (line 713);
  - the "Shared gate" bullet and Q-A1's cell are accurate.
- The recorder citations hold: `VISION` is at line 240 and "review retired
  by changed input" is at line 592.
- The ledger's cycle-3 sentence "Repaired (d2) is three lines longer, so
  VIS-7 now moves from line 250 to 260" reproduces: the block is now
  10 lines against the earlier 7.
- The dated marks at the "pending round 3" and "all open" sentences in the
  packet, delta, ledger and `ROUND-2-DISPOSITIONS.md` are at the sentences,
  with the old text kept.

## Findings

### 1. Note [Observed]: §2's (e) row still states the clause's pre-repair scope

The (e) row's Tier cell says that such records "never back a claim about
Syzygy's own status".

That is wider than the repaired rule. §1 (e) now says "the denial covers
only line 60's trigger". It also says that a green badge about Syzygy, or a
gap of Syzygy's "factually resolved or absent", "may still rest on
self-observation records". Q5 offers the wider reading as a separate,
undrafted arm: "widen the denial to every status-claim trigger about
Syzygy itself".

So the representability table describes the widening arm rather than the
arm recommended "as drafted". The doctrine bytes, §1 (e), §7 Q5 and the
delta's (e) meaning all agree with one another; only this cell disagrees.
Suggested repair: "never back a claim declaring Syzygy's own alignment,
convergence or genome-completeness".

### 2. Note [Inferred]: §1 (e)'s "green badge" example ignores the prose-form rule

§1 (e) says that a green badge about Syzygy itself (line 59) may still rest
on self-observation records. But `trust-and-evidence.md` lines 65–67 judge a
claim "whatever its prose form". A green badge that declares Syzygy's
alignment meets both the line-59 trigger and the line-60 trigger, so the
inserted bytes deny it.

The bytes are right ("a claim that declares Syzygy's own alignment…"). The
packet's gloss is too broad. "A green badge about Syzygy that declares no
alignment, convergence or genome-completeness" would be exact. This does
not change the clause.

### 3. Note [Observed]: packet §8 still carries the inaccuracy round-3 note 4 found in the ledger, unmarked

The packet's D9 bullet, lines 699–700, reads: "The thirteen doctrine
readers added since `59fbf787` read `security.md` or `v1.md` only (ledger
§4)."

The ledger now marks that claim as "not right as stated", because
`gate-acts.test.ts` line 298 reads the doctrine `README.md`. The cycle-3
mapping repaired the ledger and packet §9 step 3, but not §8. Under the
CG-27 lesson, this sentence should carry a dated mark at the sentence.

`ROUND-2-DISPOSITIONS.md` row 12 repeats the same words ("the 13 new
readers read only `security.md` or `v1.md`"). As a record of what cycle 2
claimed, it may stand, but a pointer would help.

Minor: three "for round 3 to test" tags remain (packet lines 204 and 708,
ledger line 309). They are stale routing but state nothing false.

### 4. Note [Observed]: ledger §4's failure table still says VIS-7 moves 250 → 257

The table row for `scripts/build_directive_register.py --check` reads
"insertion (d2) moves VIS-7 from line 250 to 257". The cycle-3 mark above
the table says 260, and my probe gives 260. The row itself carries no mark.
The marks above the table explain it, but under the at-the-sentence rule
the row should carry its own dated mark.

### 5. Note [Inferred]: (d2)'s last sentence does not say whose write the act must name

"A dismissal of such a project's gap … waits for an act that names that
write."

The sentence sits under "content Syzygy authors", and (d1) says "Syzygy
writes nothing there until an act names the write". So the intended reading
is that *Syzygy's* write waits for an act. Read alone, though, the sentence
could also be taken to say that a dismissal the observed project's own
owner commits by hand in that project's own plane needs an act first.
Doctrine does not require that: VIS-5 bounds Syzygy's writes, and
`trust-and-evidence.md` line 42 asks only that the dismissal be committed
to the governed plane.

"So Syzygy commits it there only once an act names that write" would close
the reading. The packet's §1 (d) paragraph ("reachable only by an act
naming the write") has the same scope.

### 6. Note [Observed]: the cycle-3 owner direction is not yet recorded under `decisions/`

A listing of `decisions/` at the reviewed commit shows only
`OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md` and
`OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md` for these cycles. The
packet, the delta, the brief and `ROUND-3-DISPOSITIONS.md` quote the ruling
as "[Observed: as relayed by the lead session …; not yet recorded under
`decisions/`]". That is disclosed honestly. Per the dispatcher, the lead
session will record it. Once it does, the "not yet recorded" sentences go
stale and need marks at those sentences.

## Summary

- Revise-level findings: 0.
- Notes: 6 (findings 1–6).
- All five round-3 findings are repaired in the bytes.
- The owner's ruling is applied faithfully: (d2) holds no dismissal, says
  in words where one lawfully lives, and no longer leaves the dilemma
  VIS-6's violation sentence posed.
- Every anchor, digest and quotation checked is exact.
- The full application probe at `79f51fdf` reproduces the ledger's cycle-3
  figures: 100/0 baseline, 100/6 applied, the same six messages, and
  VIS-7 at line 260.
- Notes 1 and 2 are packet-gloss residues of the (e) narrowing. Notes 3
  and 4 are stale sentences without marks at the sentence. None of the
  four changes a doctrine byte or an owner arm.
- Under the brief's Round 4 stopping rule, a verdict with no revise-level
  finding clears the exact bytes read (package digest above). These notes
  go in a sibling `ROUND-4-DISPOSITIONS.md`, and the package's other files
  are not edited. Clearance is not adoption: every §7 question stays the
  owner's (VIS-4).
