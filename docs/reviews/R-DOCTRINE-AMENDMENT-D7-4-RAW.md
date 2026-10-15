# Review - D7 doctrine amendment packet (held derived computation, P-101), round 4
Reviewed commit: 79f51fdfa5350feb747162af91137758dc3b38ed
Package digest: b237bc50abf8bf53384a8591830db75d05dcd520b6081c127ec67c9f7cba36e7
Verdict: REVISE

Reviewer: one fresh-context agent. I had no access to the drafting session,
the earlier review rounds or the cycle-1 to cycle-3 repair lanes. Brief:
`.syzygy/governance/contracts/candidates/doctrine-amendment-held-derived-computation-d7/REVIEW-BRIEF.md`,
§"Round 4": head contract, stopping rule, subject and references. As that
section asks, I read the three earlier raws and `ROUND-3-DISPOSITIONS.md`.
I checked each round-3 finding against the current bytes, not against the
dispositions' account of them.

Method: a git worktree detached at the reviewed commit. `git rev-parse HEAD`
equals it, and `git status --porcelain` is empty. Package digest: the sandbox
would not run the brief's `$(git ls-files …)` form as one command, so I put
that exact pipeline in a scratch shell script and ran it at the worktree
root. `git ls-files` lists seven paths, already in C order, and the result
is `b237bc50…`. I did not transcribe any digest; all of them were scripted.
The probe ran in a separate scratch clone at the same commit. I did not
read any Butlers repository.

## What was confirmed

- [Observed] Section 1's proposed doctrine bytes have not changed since
  rounds 2 and 3. I extracted both `markdown` blocks by script from the
  packet and from the delta at `8f1fbec7` (round 2), `7071a744` (round 3)
  and the reviewed commit, and hashed them. All six extractions give the
  same two block digests. The §1.2 block begins with the anchor's lines
  329–334 and has ten lines, as §1.2 and the delta say.
- [Observed] The anchor sha256 values hold at the reviewed commit. I
  compared full values by script: `vision.md` 93cc5fbb…, `architecture.md`
  d1987f7f…, `RFC-0002/reconciliation-chain.md` 7d7f876b…,
  `RFC-0002/snapshot-and-evaluation-core.md` 7f573ba1…,
  `RFC-0005/admission-and-boundary.md` a742a77f… and the P68–P83 decision
  a59294d4…. Both anchor quotations occur in the packet byte for byte
  (`vision.md` 105–107, `architecture.md` 329–334). `git grep -F` for the
  two doctrine digests finds only the D7 and D8 packages and the three
  files of `docs/evidence/polaris-understanding-reconciliation-2026-09-28/`,
  as the ledger and the delta say.
- [Observed] The clause citations are correct. RFC4 `named-adapters.md`
  420–421 reads "Capture runs inside ordinary human-triggered observation
  passes / (RFC2-19)", and line 492 reads "ordinary human-triggered
  observation passes (RFC2-19)". RFC2-17 is at 122–124, RFC2-18's scope
  sentence at 141–142, "the merge facts carried by RFC2-1 items 1 and 3"
  at 145–146 ("— the" ends line 145), "merged" at 153, the
  reconciliation-pending bullet at 155–157 and RFC2-19 at 245–247. RFC2-1
  item 1 is at core 78–79. `grep -F "merge fact"` returns the eight hits
  §4.1 lists.
- [Observed] The recorder gate is as recorded. In a scratch clone at the
  reviewed commit, a script took the packet's two `markdown` blocks and
  asserted both anchors' sha256 and positions before each insertion.
  - Baseline `--check`: `PASS`.
  - §1.1 alone: `--check` exits 1 with "FAIL exact digest reconciliation
    unresolved: review retired by changed input:
    .syzygy/governance/doctrine/vision.md". `--selftest` exits 1 with
    "candidate input drift: .syzygy/governance/doctrine/vision.md".
  - `vision.md` restored and §1.2 alone: `--check` prints `PASS`. So did
    `--selftest`, which the ledger did not claim.

  The constants match the ledger's line numbers: `VISION` at 240,
  `FROZEN_PATHS` at 243–244, `HISTORY_PATHS` at 250, and the
  retired-review check at 592. Ledger §4, the delta's marked migration
  note, packet §9 and Q6 all agree with this output. For whether Q6's
  arms are complete, see note 2.
- [Observed] Round-3 finding 1, for narrow versus wide, is repaired. The
  packet no longer relies on either reading. It states one position: a
  reading is chosen only by a contract act and is [Unknown] until then.
  For the narrow and wide readings it applies that position symmetrically
  in §0, §2, §4's merge-chain row, §4.1, §6 items 1 and 2, §7 and §8, in
  the ledger's RFC2 rows and closing paragraph, and in the delta's RFC2
  bullet and summary. The owner-ruling alternative is gone from §4's row
  and §6 item 1. The ledger row now names a contract act in either form.
  The claim that the round-2 N and W arms collapse is argued (Q5): each
  is a choice of reading, and a plain Q5 answer cannot make one. The
  round-2 arms are quoted and dated. Finding 1 below concerns the third
  reading.
- [Observed] Round-3 note 2 is repaired. §4.1 names RFC4 lines 420–421 and
  492 and weighs them fairly. It argues against the broadest reading from
  the "human-triggered" wording and RFC2-19's grammatical subject, and
  labels that weighing [Inferred]. Its statement of the broadest reading's
  effect is limited to re-observation, which is not overstated. The
  ledger's RFC4 row now addresses the reading question.
- [Observed] Round-3 note 3 is repaired. §2's residual paragraph and §6
  item 7 now say that section 1 states a condition and no burden of proof,
  and label the showing obligation as this packet's reading and an
  implementation obligation [Inferred]. Q3's strict arm covers hooks only.
  The "Not an arm" line and §6 item 7 ("It holds whichever way Q3 is
  answered") make the page-open condition independent of Q3. Nothing
  claims that a test exists.
- [Observed] Round-3 note 4 is repaired. Ledger §5 item 1 cites packet §6
  item 2, and the `polaris-manifesto-generation` row cites §6 item 3. Both
  carry dated notes. §4.1 cites 145–146.
- [Observed] Round-3 note 5 is repaired. A scripted column check over all
  seven files found only these non-table lines over 80 columns:
  - packet: line 1 (a heading), line 310 (a heading) and line 419 (86
    columns, one unbroken code span);
  - delta: lines 194 and 199 (paths);
  - ledger: line 33 (the fenced predicate);
  - `REVIEW-BRIEF.md`: paths and fenced titles.

  This matches disposition repair 5.
- [Observed] Round-3 note 6 is dispositioned as stated. The cycle-2
  direction is recorded at
  `decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`, which the
  package cites. Brief line 106 is marked at the sentence.
- [Observed] The round-1, round-2 and round-3 raws are not edited. D7-1 and
  D7-2 do not appear in `git diff 7071a744..79f51fdf`. D7-3 has exactly one
  commit in its history (`fcd1cfa7`). Every package file is NFC.
- [Observed] `python3 scripts/check_governance.py` at the reviewed commit
  ran 53 checks: 32 OK, 21 WARN, 0 FAIL. I counted the `^(OK|WARN|FAIL) `
  lines (53) and the `^WARN ` lines (21); `^FAIL ` matched nothing. No
  output line names `held-derived-computation-d7`.

## Findings

1. **[Observed] revise-level: the one-position rule is applied to the
   narrow and wide readings but not to the broadest. As a result, Q5's
   recommended arm, the ledger and the delta state a consequence that the
   packet's own rule makes [Unknown].**

   The packet's rule (§4.1 lines 411–418) is "All three are readings of
   accepted contract text. Which one binds is fixed only by a contract act
   … until one fixes it, the reading is **[Unknown]** … This applies to
   every reading alike". The ledger's RFC4 row agrees for the third
   reading: "which reading binds is a contract-act matter, like the other
   two". On the broadest reading, "no unprompted re-observation is lawful
   at all" (§0 line 107, §4.1 lines 397–401).

   It follows that, until a contract act fixes the reading, whether arm A
   makes unprompted re-observation of a repository with no merge lawful is
   itself [Unknown]. The packet instead uses its own weighing against the
   broadest reading ([Inferred], §4.1 lines 405–406) to discount it. That
   weighing is a choice among readings, which §4.1 says "neither this
   packet, nor a doctrine amendment, nor a plain owner answer to Q5"
   makes. The files then disagree on the no-merge row:
   - **Hedged, with a condition that the packet's rule already settles:**
     - §0 lines 118–121: "lawful … on the narrow and wide readings
       ([Unknown] only if the broadest reading is a live one)";
     - §4.1 table row 1, last column: the same wording.

     Until a contract act acts, whether the broadest reading is "live" is
     exactly what the rule says is Unknown.
   - **Self-contradictory:** §6 item 1 lines 483–487, "What adoption does
     make lawful here, **whatever the reading**: unprompted re-observation
     of a repository whose history carries no merge at all … ([Unknown]
     only on section 4.1's broadest reading …)".
   - **Unqualified:**
     - Q5 arm U, the recommended arm (lines 678–680): "arm A, if adopted,
       makes unprompted re-observation of a repository whose history
       carries no merge lawful at the doctrine level";
     - the ledger's merge-chain row: "Until then arm A makes unprompted
       re-observation lawful at the doctrine level only for a repository
       with no merge in its history";
     - the delta's RFC2 bullet (lines 157–159): "Until then D7 makes
       unprompted re-observation lawful at the doctrine level for a
       repository with no merge in its history".
   - **False on the broadest reading:** Q5's "Narrow D7 instead" arm
     (lines 699–702) says "The question then never decides D7's reach"
     and "arm A then reaches only repositories with no merge in their
     history". On the broadest reading the question still decides reach:
     arm A then reaches no re-observation at all.
   - **Incomplete:** §2's "unprompted" paragraph (lines 281–285) lists
     what the confinement excludes on the narrow and wide readings only.

   This is the class of round-3 finding 1. The consequence that the
   recommended arm presents to the owner omits an [Unknown] that the
   packet's stated rule requires. The brief's test is whether the packet
   "appl[ies] it to every reading alike" and whether §0, §2, §4, §4.1, §6,
   §7, §8, the ledger and the delta "say the same thing about what arm A
   permits for each class of repository". They do not, for the no-merge
   class.

   Repair, either way:
   - Apply the rule to all three readings. Row 1 becomes "[Unknown] until
     a contract act fixes the reading; lawful on the narrow and wide
     readings, and the packet weighs the broadest against [Inferred]".
     Restate Q5 U, the "Narrow D7" arm, §6 item 1, §2, the ledger row and
     the delta bullet to match.
   - Or argue, in §4.1, why the broadest reading is not a reading of
     RFC2-18/RFC2-19 text that falls under the rule. Then correct the
     ledger's "like the other two" and §4.1's "All three are readings of
     accepted contract text".

2. **[Inferred] note: Q6's "Reconcile" arm may not be available without
   the recorder change that the other arm names.**

   Q6 (lines 723–724) offers "a fresh reconciliation review over the
   amended `vision.md`, recorded the way the recorder requires". The
   ledger's recorder row says resolving the gate "needs a fresh
   reconciliation review … **or** a reviewed recorder change". In
   `scripts/record_polaris_understanding_adoption.py`, however, the C1
   review is one fixed path, `RAW = EVIDENCE + 'REVIEW-RAW.md'` (line 234),
   and three checks constrain it:
   - `reviewed_template` requires that path's current bytes to equal the
     blob at its introducing commit ("retained C2 review changed").
   - `introduction` refuses a reintroduced file ("reintroduced evidence").
   - The recorded technical record must equal the template filled with
     that raw's digest (`check_evidence`, "technical record differs from
     reviewed template").

   The numbered `HISTORY-REVIEW-n-RAW.md` mechanism binds only the
   recorder's own bytes (`history_review`), and the readability-successor
   rows apply to adoption subjects, not to the frozen review inputs that
   line 592 compares. I found no route by which a fresh reconciliation
   review could be recorded under the recorder as written. If there is
   none, the "Reconcile" arm also needs a reviewed recorder change, and
   the two arms differ only in which change is made. I did not test this
   by mutation, so it is [Inferred]. Repair: state what recording a fresh
   review would need, or name the recorder mechanism that admits one. The
   same applies to D8's Q-A1, which the packet says shares this answer.

3. **[Observed] note: some stale present-tense sentences remain unmarked.**
   - `ROUND-2-DISPOSITIONS.md` repairs row 1 says "The packet **relies on
     the narrow reading**" and lists Q5's arms as "N (narrow,
     recommended), W …". Both are no longer true after cycle 3.
   - Repairs row 3 says "Q3's strict arm states the same burden for page
     opens", which cycle 3 removed.
   - Repairs row 7 says "on the narrow reading D7 licenses more
     unprompted computation". After cycle 3 that holds only if a contract
     act fixes the narrow reading.

   Cycle 3 marked other sentences in that file (lines 10–11 and 54–60)
   but not these. These rows log what cycle 2 did. They sit, however,
   under the round-2 brief's own standard (mark at the stale sentence),
   and a reader of the dispositions would take them as the packet's
   current state.

   Smaller items:
   - `ROUND-3-DISPOSITIONS.md` line 44 says "recommends nothing on Q1–Q5".
     It is still true, but the package now has Q6.
   - Outside the package: the P-101 register row's "unblocks" cell still
     says "an RFC2 amendment on the wide reading". It should say a
     contract act, with the reading [Unknown].

4. **[Observed] note: two small inconsistencies.**
   - §4's RFC2-19 row cites RFC4 "lines 420 and 492". §4.1 and the ledger
     cite 420–421, the correct range.
   - §9 puts "Step 1 waits for Q6's answer" inside step 3, after the step
     it constrains. The delta (line 263) has the same sentence correctly
     attached to its migration plan.

   Neither changes a consequence.

5. **[Observed] note: the cycle-3 warrant is not yet recorded.** At the
   reviewed commit no file under `decisions/` records the owner's cycle-3
   direction for P-101. `grep -F` for "One more cycle" and "cycle-3" over
   `decisions/` finds only:
   - the cycle-2 record, whose "One more cycle" is the cycle-2 option;
   - the pending register, whose P-101 row quotes the cycle-3 direction
     "as relayed by the lead session";
   - `decisions/README.md`.

   The package labels the direction honestly as "[Observed: as relayed …;
   not yet recorded under `decisions/`]" (brief lines 183–188, packet
   lines 43–48, `ROUND-3-DISPOSITIONS.md` lines 47–51). As the dispatch
   said, the lead session is to record it. This round's stopping rule
   rests on that direction until it is recorded.

## Answers to the brief's Round 4 questions

- **Round-3 findings.** All six are repaired as `ROUND-3-DISPOSITIONS.md`
  §"Repairs" says:
  - Notes 2–5 are fully repaired.
  - Note 6 is dispositioned, and the same gap is open again for cycle 3
    (note 5).
  - Finding 1 is repaired for the narrow and wide readings. The repair of
    note 2 added a third reading, and the one-position rule is not
    applied to it, which is finding 1 above.
- **Finding 1, one position.** One position is stated. It is applied to
  every reading in §4.1's prose, but the reach statements do not apply it
  to the broadest reading. As a result, §0, §4.1, §6, Q5 U, the ledger and
  the delta give three different accounts of the no-merge row. Q5 is
  well-formed in its structure, and the collapse of N and W is argued.
  Arm U's consequence and the "Narrow D7" arm's consequence omit the
  broadest-reading Unknown.
- **Note 2, RFC4's reading.** It is weighed fairly, and its effect is not
  overstated.
- **Note 3, page-open obligation.** It is labelled as the packet's
  reading and is independent of Q3 everywhere it appears.
- **Recorder gate.** The probe reproduces exactly at the reviewed commit.
  The ledger, the delta, §9 and Q6 agree with its output. Whether Q6's
  arms are complete is note 2.
- **Dated status marks.** They sit at the stale sentences, with the old
  text kept. The remainders are in note 3.
- **Section 1 bytes and anchors.** Section 1's bytes are unchanged from
  those rounds 2 and 3 read, and every anchor sha256 holds.

Under the brief's stopping rule, this `REVISE` goes to the owner with its
findings open. There is no further repair and no round 5 without a new owner
direction.

Revise-level findings: 1 (1). Notes: 4 (2–5).
