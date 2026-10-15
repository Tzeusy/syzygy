> # Record beside the package — not authority, binds nothing
>
> Dispositions of the sixth fresh-context review of the PWB release-label
> amendment package (P-85). This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It classifies each
> round-6 finding and repairs nothing: every finding is open. It offers
> nothing and performs no act (VIS-4).
> *(Marked 2026-10-15, cycle 5: "repairs nothing: every finding is open" no
> longer describes the package. The owner's answer below directed one more
> repair; the mapping is §"Repairs, 2026-10-15 (cycle 5)" at the end. The
> table keeps its **Open** marks, which describe the round-6 bytes.)*

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

## The owner's answer after round 6

Given on 2026-10-15 by structured question in the lead session, relayed by
the coordinator and quoted verbatim:

- **Question:** "P-85 (release labels) failed round 6: a citation placed
  inside a sentence still passes every check, so 'never a stamp' promises
  more than the checks decide. The reviewer's fix drops that claim and
  states the gap as a limit, which weakens what Q6's recommended arm
  promises. What next?"
- **Answer:** "Weaker wording + review (Rec.)"
- **Option text:** "Drop 'never a stamp', state both gaps as limits, then
  one review; it comes back to you to sign."

So the round-6 finding and notes are repaired once, and one fresh round 7
follows under the same stopping rule. A notes-only round 7 clears the bytes
and makes P-85 ready for the owner's Question 1. It signs nothing, because
P-85 has no carry-over answer. A `REVISE` is classified and stops.

## Repairs, 2026-10-15 (cycle 5)

The repair base is `main` at `dd7242ca`, with P-98 and P-99 signed.
`--write` regenerated the derived patches and the manifest. Against the
round-6 manifest, 3 of 11 rows move: `spec.md` and `design.md` (the
repairs below) and `GOVERNING-DEPENDENCIES.md` (derived).

**Round-6 findings repaired once on 2026-10-15, unconfirmed pending round
7.**
*(Marked 2026-10-15, round 7: "unconfirmed pending round 7" is no longer
true. Round 7 returned `REVISE`
(`docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-7-RAW.md` line 4). F1 is
repaired in the requirement but not in the packet summary and one delta
choice, and the narrowed scenario still overclaims through an excepted
identity. N1–N3 are repaired. Open findings are in
`ROUND-7-DISPOSITIONS.md`.)*

Line numbers are in `proposed/spec.md.patch` (`spec`) at this commit.

| # | Finding | Repair |
|---|---|---|
| F1 | "Therefore never a stamp" does not follow (embedded citation; phrase-like locator) | The raw's preferred repair, as the owner directed. "A revision id in a sentence, a heading or any other running text is therefore never a stamp" is removed. In its place, "Two limits stay. Where a citation sits is not decided by this requirement: a citation placed inside a sentence, a heading or other running text passes these tests …" and "Which tokens an anchor's served locator holds is not decided either: … so a one-token locator that reads as a phrase passes" (spec 54–60), in the closed-list form the term list already uses. The fifth scenario is renamed "A citation's contents are decided, not its placement". Its THEN now speaks of the sentence outside a citation, and a new AND states the placement gap (spec 341–351). Question 6's recommended row drops "A sentence cannot be cast as a cite … The label then leads wherever the revision is named" and names both limits, with a dated note keeping the old words. |
| N1 | Six wordings guarded only by the digest | All six are in `REQUIRED_ONCE`, each killed by its own mutant, as are the new limit and scenario wordings: 77 structure mutants. |
| N2 | Design decision 13 and the delta not carried; "four scenarios" stale | `design.md.patch` decision 13 now has the cite-text rule and both gaps. It also has the closed identity population ("the evaluation identity or … one served source record's source identity, and no other record's") and the sweep's twelve-digit scope. These are guarded by three `DESIGN_PHRASES` and two mutants. The delta's §"What changes" carries the same rules and says "Five new scenarios", with a dated note. Packet Question 1 says five scenarios. |
| N3 | The prohibition swept only at twelve digits | The prohibition now says "These three are the namings the text sweep below finds, and "names the observed revision" means them: a shorter prefix of the object id is not decided by this requirement." (spec 32–35). The label-unit sentence reads "a naming being one that the text sweep below finds" (spec 18–20). Design decision 13 says "a shorter prefix is not decided". |

The round-7 brief is `REVIEW-BRIEF.md` §"Round 7 (added 2026-10-15, cycle
5)".
