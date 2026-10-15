> # Record beside the package — not authority, binds nothing
>
> Dispositions of the seventh fresh-context review of the PWB release-label
> amendment package (P-85). This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It classifies each
> round-7 finding and repairs nothing: every finding is open. It offers
> nothing and performs no act (VIS-4).

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
