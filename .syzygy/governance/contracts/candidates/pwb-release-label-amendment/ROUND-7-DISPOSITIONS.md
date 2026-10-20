> # Record beside the package — not authority, binds nothing
>
> Dispositions of the seventh fresh-context review of the PWB release-label
> amendment package (P-85). This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It classifies each
> round-7 finding and repairs nothing: every finding is open. It offers
> nothing and performs no act (VIS-4).
> *(Marked 2026-10-20, cycle 6: "repairs nothing: every finding is open"
> is no longer true of the package. The lead's cycle-6 decision repaired
> every round-7 finding once; §"Repairs, 2026-10-20 (cycle 6)" below maps
> them. This record still repairs nothing itself.)*

# Round 7 dispositions — PWB release-label amendment

Reviewed record: docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-7-RAW.md

- **Reviewed commit (raw line 2):**
  `decd32d8c9daa06c632d39674cdf5aa250244a4e`, the merge of the cycle-5
  repair (#468).
- **Manifest file digest (raw line 3):**
  `36c8750691dfe1a5bb0126052df2c517ea33bf876f323a1d58c59b0b3f0d49b1`.
  [Observed 2026-10-15] It re-derives by script from the manifest file's
  bytes at the reviewed commit (1,961 bytes).
- **Verdict (raw line 4):** `REVISE`. Two revise findings and three notes,
  no blocking finding (raw line 109: "Counts: 0 blocking, 2 revise
  (Findings 1–2), 3 notes (1–3).").
- **Why the round ran.** The owner's answer to round 6, "Weaker wording +
  review (Rec.)", quoted in `ROUND-6-DISPOSITIONS.md`. The brief's
  §"Round 7" set the stopping rule before the round: "Any other verdict is
  classified and stops, and no round 8 is dispatched without a new owner
  instruction."
- **Stopping rule applied.** The package is not repaired here, the bytes
  are not cleared, and no round 8 is dispatched. The only package edits are
  dated status marks at the "unconfirmed pending round 7" sentences in the
  packet, the delta and `ROUND-6-DISPOSITIONS.md`, with the old text kept.
  *(Marked 2026-10-20, cycle 6: "is not repaired here" and "no round 8 is
  dispatched" are superseded by the lead decision quoted below.)*
- **What the round confirmed.** The withdrawal and both limits are in the
  requirement, and round-6 Notes 1–3 are repaired (raw lines 38–41). The
  two stated limits are "both true" (raw line 84). Criteria 1, 3, 4 and 5
  are met, 7 met with a note, 2 not fully met (Finding 2) and 6 not met
  (Finding 1) (raw lines 45–51).

## Dispositions

| # | Level | Finding (short) | Raw line | Disposition |
|---|---|---|---|---|
| F1 | revise | The withdrawal is incomplete. The packet's "What you would be signing" still says "an id in a sentence or heading never does", and the delta's cycle-3 choice 1 still says "is never a stamp" with no dated mark | 55 | **Open.** The raw's repair: reword the packet summary to match Question 6's recommended row, and add a dated mark at the delta choice that keeps the old words. [Inferred] Prose only; no requirement byte changes. |
| F2 | revise | Scenario 5's THEN is still not decided. An excepted identity, which contains the full object id, placed in a sentence passes every decide-line, and neither stated limit covers it | 64 | **Open.** The raw's repair, in the owner-chosen form: extend the first limit to "Where a citation or an excepted identity sits is not decided by this requirement", and narrow the THEN to "outside a citation and an excepted identity", or make the AND name both. The raw says a placement rule for identities would be a content change for the owner, not a repair. |
| N1 | note | Question 6's table is broken by the dated note between its rows | 93 | **Open.** Move the note below the table. |
| N2 | note | The delta's residual census still reads 17, 60 and 5 | 97 | **Open.** Mark it with 68 and 6, or cite the ledger row. |
| N3 | note | Two cycle-5 wordings (which gaps decision 13 names; scenario 5's WHEN) are guarded only by the digest | 101 | **Open.** |

**Stale sentences outside the package.** Register row P-85 and
`docs/README.md`'s release-label row are updated directly.

## Repairs, 2026-10-20 (cycle 6)

**Direction.** The coordinator relayed the lead session's decision, taken
under the owner's autonomy direction: "Lead decision (process, owner
autonomy direction): one more P-85 cycle. Repair round-7 findings using the
reviewer's fix that keeps the owner's chosen approach: widen the placement
limit to cover excepted identities (full revision id in a sentence), narrow
scenario 5's THEN, fix the packet's "What you would be signing" summary and
the delta design choice that still say an id in a sentence never counts;
repair the 3 notes. Regenerate, fresh-context round 8." It is a process
decision: it signs, adopts and authorizes nothing (VIS-4).

| # | Repair |
|---|---|
| F2 | The first limit now reads "Where a citation or an excepted identity (below) sits is not decided by this requirement: a citation or an identity placed inside a sentence, a heading or other running text passes these tests, though its words then name the revision outside a label unit, an identity by the revision's full object id." The identity bullet ends "It shows that identity whole, and where it sits is the first limit above;". The fifth scenario is renamed "Citation and identity contents are decided, not placement"; its THEN reads "outside a citation and an excepted identity the sentence shows neither R's full object id nor its first twelve hexadecimal digits", and its last AND reads "whether that citation or an excepted identity sits inside the sentence is not decided by this requirement". Design decision 13's gap list reads "where the citation or an excepted identity sits (inside a sentence passes)". Question 6's recommended row names both. No decide-line, falsifier or sweep changes. |
| F1 | The packet's "What you would be signing" first exception now says "A bare id in a sentence or heading, outside any citation, fails (Question 6)", followed by a paragraph stating the placement limit for citations and identities and a dated note keeping the old words. The delta's cycle-3 choice 1 carries a dated mark at the stale sentence, old words quoted. |
| N1 | Question 6's cycle-5 note moved below the table; a cycle-6 note sits beside it. |
| N2 | The delta's residual census carries a dated re-measure at `8340fa22`: 17 requirements and 63 scenarios with PWB-REQ-001 at 1; after `--apply`, 17, 68 and 6. |
| N3 | `DESIGN_PHRASES` guards decision 13's gap list and its polarity; `REQUIRED_ONCE` guards the fifth scenario's WHEN, anchored to the following THEN so that a widened WHEN does not still contain it, and the identity bullet's pointer. Four new mutants ("identity placement limit dropped", "scenario WHEN widened", "design gap polarity flipped", "design identity gap dropped") each fail on their own predicate; the existing limit, THEN, AND and scenario-title mutants were retargeted to the new bytes. `--selftest` reports 81 structure mutants. |

**What moved in the manifest.** Three rows changed: the spec, the design
and `GOVERNING-DEPENDENCIES.md` (which names the spec digest). The other
eight subjects hash as before. The builder still prints "17 requirements,
68 scenarios".

**Not cleared.** No round has read these bytes. They are not offered for
sign-off until round 8 returns `CONFIRM`, or `CONFIRM WITH EXCEPTIONS` with
notes only; even then Question 1 is the owner's, since this package has no
carry-over answer.
