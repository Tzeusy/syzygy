> # Record beside the package — not authority, binds nothing
>
> Dispositions of the fifth fresh-context review of the PWB release-label
> amendment package (P-85). This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It classifies each
> round-5 finding and repairs nothing: every finding is open. It offers
> nothing and performs no act (VIS-4).
> *(Marked 2026-10-15, cycle 4: "repairs nothing: every finding is open" no
> longer describes the package. Under the owner's "One more cycle" answer
> every finding and note was repaired once; the mapping is §"Repairs,
> 2026-10-15 (cycle 4)" at the end. The table below keeps its **Open**
> marks, which describe the round-5 bytes.)*

# Round 5 dispositions — PWB release-label amendment

Reviewed record: docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-5-RAW.md

- **Reviewed commit (raw line 2):**
  `83b29c96775d9c2215292fa41e1599080f0b802c`, the merge of the cycle-3
  repair.
- **Manifest file digest (raw line 3):**
  `d7220b77fdc1b61f05a3a15f43e157ff279a179dc3bc84ca152b5e9832f1b1ad`.
  [Observed 2026-10-15] It re-derives from the manifest file's bytes on
  `governance/cycle-3-records` over `origin/main` `60995b23`, where the
  file is unchanged since the reviewed commit.
- **Verdict (raw line 4):** `REVISE`. One revise finding (1) and seven
  notes (1–7, numbered separately), no blocking finding (raw line 152:
  "Counts: 1 revise-level finding (1), 7 notes (1–7), 0 blocking.").
- **Why the round ran.** The owner's cycle-3 direction for P-85 and P-98,
  "One more cycle each", recorded in
  `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`.
  The brief's §"Round 5" set the stopping rule before the round: a
  `REVISE` goes to the owner with its findings open.
- **Stopping rule applied.** The package is not repaired here, and the
  bytes are not cleared. The only package edits are dated status marks at
  the "unconfirmed pending round 5" sentences in the packet, the delta and
  `ROUND-4-DISPOSITIONS.md`, with the old text kept. `REVIEW-BRIEF.md` is
  not edited; its heading "Round 5 (added 2026-10-14, cycle 3; not yet
  dispatched)" is no longer true, and this record carries the correction.
- **What the owner answered after this round.** "One more cycle" (round
  6), recorded in the cycle-3 record. That answer authorizes one more
  repair of these findings and one fresh round 6, made by a separate
  change; this record dispatches nothing and repairs nothing.
- **What the round confirmed.** Round-4 findings 2–8 are repaired and
  finding 1 mostly repaired (raw lines 53–62); criteria 1, 3, 4, 5 and 7
  are met, 6 met with notes (raw lines 64–72).

## Dispositions

| # | Level | Finding (short) | Raw line | Disposition |
|---|---|---|---|---|
| F1 | revise | The citation predicate leaves the cite's visible text free, so a sentence naming the revision can be cast as a citation, and "therefore never a stamp" does not follow; Q6's recommended sentence overclaims | 76 | **Open.** Raw's repair: constrain the cite's whole visible text to a value the checker reads from the named record (source path, observer or tool name, or the anchor's served label), add that equality to the citation decide-line, and add the falsifier case "a cite whose text is not its record's served name"; or withdraw "therefore never a stamp" and the Q6 sentence and disclose the gap as a named limit. |
| N1 | note | The identity exception's record population is open; "a record of its own" is hard to parse | 113 | **Open.** Name the evaluation snapshot and source identity records, or the record classes PWB-REQ-001 and PWB-REQ-020 define. |
| N2 | note | Five new load-bearing wordings are guarded only by the dependency digest | 117 | **Open.** Add them to `REQUIRED_ONCE`; guard the identity exception and page population as whole sentences. |
| N3 | note | Question 5's options still say "Leave it to the POC specification" | 127 | **Open.** Reword the option or mark the row. |
| N4 | note | Stale current-state cells in the impact ledger (lines 41 and 43) | 131 | **Open.** Mark them at the cell. |
| N5 | note | "changes no … contract-coverage row" beside a superseded row | 138 | **Open.** Say "no base matrix row's bytes; one row is superseded through the repair delta". |
| N6 | note | The cycle-3 owner direction is unrecorded | 142 | **Dispositioned.** Recorded in `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`. |
| N7 | note | Sibling builders at this commit; the three pending `GOVERNING-DEPENDENCIES.md.patch` files do not compose in any order | 146 | **Open.** After the P-99 sign-off in the same change as this record, this package's builder is expected to fail until it is regenerated over P-99. |

**Stale sentences outside the package.** Register row P-85 and
`docs/README.md`'s release-label row are updated directly.

## Repairs, 2026-10-15 (cycle 4)

Made under the owner's answer "One more cycle" to round 5, recorded in
`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`:
repair every round-5 finding, notes included, once, then one fresh round 6
under the same stopping rule (a notes-only round clears its bytes; a
`REVISE` returns to the owner). P-85 has no carry-over answer, so cleared
bytes still wait for the owner's Question 1.

**The base moved.** The accessible-name (P-99) and opening-index (P-98)
amendments were signed v1.0 on 2026-10-15. Their sign-offs changed the
signed `spec.md` and `GOVERNING-DEPENDENCIES.md`. [Observed 2026-10-15]
This package's authored patches still applied; the derived
`GOVERNING-DEPENDENCIES.md.patch` and the manifest were regenerated with
`--write`, never hand-edited. The repair base is `main` at `c5acaf59`, the
P-98 sign-off. Against the round-5 manifest (at `83b29c96`), 2 of its 11
rows move: `spec.md` (the repair below and the two sign-offs' bytes beneath
it) and `GOVERNING-DEPENDENCIES.md` (derived). The other nine rows are
unchanged, so the capability, design, proposal and contract-coverage
patches are as round 5 read them.

**Round-5 findings repaired once on 2026-10-15, unconfirmed pending round
6.** None of these repairs is accepted until round 6 reads it.

Line numbers below are in `proposed/spec.md.patch` (`spec`) and
`scripts/build_pwb_release_label_amendment.py` (`builder`) at this commit.

| # | Finding | Repair |
|---|---|---|
| F1 | Cite text free | The raw's first repair, not its withdrawal. The cite's whole visible text, whitespace-normalized, equals the served locator of the anchor it names or the served path of the source record it names; it holds no whitespace unless it is a path in the checker's own Git listing, and holds no swept occurrence (spec 40–50). It is observable (spec 178–179), decided (spec 231–233) and falsified (spec 270–272), and the new scenario "A sentence naming the revision is not a provenance stamp" carries it (spec 331–339). The raw's falsifier page fails: its cite "Declared project shape of butlers at revision" holds whitespace, is no path, and equals no served locator. One residual is disclosed in `SEMANTIC-DELTA.md` §"Repaired a fourth time" as a named limit: a served locator is the system's own output, bounded to one token but not to a fixed token set. Question 6's recommended option is reworded to say what the text decides and to name that limit. |
| N1 | Identity population open | The exception names its two records, the evaluation identity and the source identity of one served source record, and adds "These two are the whole population: an identity of any other record is not excepted." (spec 51–56). The decide-line and the falsifier limb name the same two (spec 234–236, 273–275). "A record of its own" is gone. |
| N2 | Wordings guarded only by the digest | `REQUIRED_ONCE` holds every new F1 and N1 wording, the three "not a revision's id alone" clauses, the Observable addition and the whole page-exclusion sentence (builder 225–240), each killed by its own selftest mutant (builder 923–974): 66 structure mutants in all. |
| N3 | Question 5's options | Reworded: "**Leave it ungoverned on Polaris** (this version)", and the second row now says "a component Trajectory and Orrery share", with a dated note keeping the old words. |
| N4 | Stale ledger cells | Both cells marked at the cell, dated, with the current state: the three siblings are performed, and the census this sign-off would write is 17 requirements and 68 scenarios, PWB-REQ-001 at six. |
| N5 | "no contract-coverage row" | Reworded to "no base matrix row's bytes (one row, `RFC4-11.c4`, is superseded through the repair delta)", with a dated note keeping the old words. |
| N6 | Direction unrecorded | Dispositioned before this cycle (table above). |
| N7 | Sibling builders | `SEMANTIC-DELTA.md` §"Pending siblings" is marked: no sibling is pending. The release-label builder's `--selftest` had assumed one; its order selftests now add a synthetic pending sibling (`SELFTEST_PENDING`, builder 1132–1144), so the all-orders and companion-order checks are still exercised. |

The round-6 brief is `REVIEW-BRIEF.md` §"Round 6 (added 2026-10-15, cycle
4)".
