> # Record beside the package — not authority, binds nothing
>
> Dispositions of the sixth fresh-context review of the PWB release-label
> amendment package (P-85). This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It classifies each
> round-6 finding and repairs nothing: every finding is open. It offers
> nothing and performs no act (VIS-4).

# Round 6 dispositions — PWB release-label amendment

Reviewed record: docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-6-RAW.md

- **Reviewed commit (raw line 2):**
  `e661dce481c5512642f9f532ba740a7b3d2146a7`, the merge of the cycle-4
  repair (#460).
- **Manifest file digest (raw line 3):**
  `9cb39438caf580e6a2b8af8758e02e27ef8591b9324c0d2fb7f9b4ece5947002`.
  [Observed 2026-10-15] It re-derives by script from the manifest file's
  bytes at the reviewed commit (1,961 bytes).
- **Verdict (raw line 4):** `REVISE`. One revise finding and three notes,
  no blocking finding (raw line 131: "Counts: 0 blocking, 1 revise (Finding
  1), 3 notes (1–3).").
- **Why the round ran.** The owner's answer "One more cycle" to round 5,
  recorded in
  `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`.
  The brief's §"Round 6" set the stopping rule before the round: "Any
  other verdict sends the package to the owner with its findings open. No
  round 7 is dispatched without a new owner instruction."
- **Stopping rule applied.** The package is not repaired here, the bytes
  are not cleared, and no round 7 is dispatched. The only package edits
  are dated status marks at the "unconfirmed pending round 6" sentences in
  the packet, the delta and `ROUND-5-DISPOSITIONS.md`, with the old text
  kept.
- **What the round confirmed.** The round-5 raw's literal falsifier page
  now fails (raw line 18). Round-5 Notes 1 and 3–7 are repaired or
  dispositioned; Finding 1 and Note 2 are partly repaired (raw lines
  31–38). Criteria 3, 4 and 5 are met, 1 and 7 met with qualifications, 6
  met with exceptions, and 2 not fully met (raw lines 42–48).

## Dispositions

| # | Level | Finding (short) | Raw line | Disposition |
|---|---|---|---|---|
| F1 | revise | "A revision id in a sentence … is therefore never a stamp" still does not follow. A citation embedded in the sentence passes every decide-line (route A, undisclosed), and the disclosed phrase-like locator limit is contradicted by the requirement and the new scenario (route B) | 52 | **Open.** The raw's proposed repair is to withdraw "therefore never a stamp", reword the scenario's THEN to what the decide-lines check, state both gaps in the requirement in the closed-list form ("not decided by this requirement"), and reword Question 6's recommended row. It names a placement rule as a weaker alternative and prefers the disclosure. [Inferred] Either way this changes what Question 6's recommended option promises, so it is a content choice for the owner. |
| N1 | note | Six cycle-4 wordings are guarded only by the dependency digest; "every new F1 … wording" overstates | 106 | **Open.** Guard the six, or narrow the claim. |
| N2 | note | The cycle-4 repairs are not carried into `design.md` decision 13 or the delta's §"What changes"; "four scenarios" is stale in the delta and in packet Question 1 (five are added) | 119 | **Open.** |
| N3 | note | "Names the observed revision only in a label unit" is swept only at twelve digits; a shorter prefix passes | 127 | **Open.** Say "as the sweep defines it", or state the gap beside the term-list gap. |

**Stale sentences outside the package.** Register row P-85 and
`docs/README.md`'s release-label row are updated directly.
