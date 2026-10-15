# Round 4 dispositions — D7 doctrine amendment packet

> **Candidate — binds nothing.** The record of how each round-4 finding is
> classified. Nothing in the package is repaired here: every finding is
> open. A disposition is not a confirmation, and this record edits no
> doctrine byte (VIS-4).

**Round:** 4, fresh context. **Raw:**
`docs/reviews/R-DOCTRINE-AMENDMENT-D7-4-RAW.md`, retained verbatim.
**Reviewed commit (raw line 2):** `79f51fdfa5350feb747162af91137758dc3b38ed`.
**Package digest reviewed (raw line 3):**
`b237bc50abf8bf53384a8591830db75d05dcd520b6081c127ec67c9f7cba36e7`
(re-derived 2026-10-15 by the brief's method over the seven tracked files,
on `governance/cycle-3-records` over `origin/main` `60995b23` before this
change edited them; it matches).
**Verdict, copied from the raw (line 4):** `Verdict: REVISE`.
**Findings:** 5 — one revise-level (1) and four notes (2–5), per the raw's
closing count (line 293).

Reviewed record: docs/reviews/R-DOCTRINE-AMENDMENT-D7-4-RAW.md

**Why round 4 ran.** The owner's cycle-3 direction for P-101, "One more
cycle", now recorded in
`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`.
The brief's §"Round 4" set the stopping rule before the round: a `REVISE`
goes back to the owner with its findings open (raw lines 289–291).

**What the owner answered after round 4.** "Park until RFC2 decided":
the packet is parked, an RFC2-18/19 contract clarification draft fixing
which reading binds is commissioned, and D7 is redrafted against it
(the cycle-3 record). So:

- **The package is not repaired.** The only edits after the round are
  this record, a dated PARKED banner at the head of the packet and dated
  status marks at the "unconfirmed pending round 4" and "not yet recorded
  under `decisions/`" sentences in the packet, the delta, the ledger and
  `ROUND-3-DISPOSITIONS.md`, with the old text kept. `REVIEW-BRIEF.md` is
  not edited; its §"Round 4" warrant line ("not yet recorded under
  `decisions/`", line 187) is no longer true, and this record carries the
  correction.
- **No round 5 is dispatched.** The next review reads the redraft, made
  after the commissioned clarification.
- **The bytes are not confirmed.** This record and the marks move the
  package's directory digest away from the value above; the reviewed bytes
  stay retrievable at the reviewed commit.

| # | Level | Finding (short) | Raw line | Disposition |
|---|---|---|---|---|
| 1 | revise | The one-position rule ("which reading binds is fixed only by a contract act … [Unknown] until then") is applied to the narrow and wide readings but not to the broadest (RFC4 `named-adapters.md` 420–421, 492). §0, §4.1 row 1, §6 item 1, Q5 arm U, the "Narrow D7" arm, §2, the ledger's merge-chain row and the delta's RFC2 bullet give three different accounts of the no-merge row | 117 | **Open; routed by the owner's answer.** The commissioned RFC2-18/19 clarification decides which reading binds, which removes the premise of this finding; the redraft states arm A's reach against it. Raw's repairs, kept for the redraft: apply the rule to all three readings, or argue in §4.1 why the broadest is not a reading under the rule. |
| 2 | note | Q6's "Reconcile" arm may not be available without the recorder change the other arm names (`record_polaris_understanding_adoption.py`: fixed `REVIEW-RAW.md`, `reviewed_template`, `introduction`, `check_evidence`) | 185 | **Open.** State what recording a fresh review would need, or name the recorder mechanism that admits one; the same applies to D8's Q-A1. [Inferred by the reviewer, not tested by mutation.] |
| 3 | note | Stale present-tense sentences unmarked in `ROUND-2-DISPOSITIONS.md` repairs rows 1, 3 and 7; `ROUND-3-DISPOSITIONS.md` line 44 says "Q1–Q5"; register row P-101's "unblocks" cell says "an RFC2 amendment on the wide reading" | 213 | **Open in the package.** The register cell sits outside the package and is marked there, at the cell, dated. |
| 4 | note | §4's RFC2-19 row cites RFC4 "lines 420 and 492" (420–421 elsewhere); §9 puts "Step 1 waits for Q6's answer" after the step it constrains | 236 | **Open.** |
| 5 | note | The cycle-3 warrant is not yet recorded under `decisions/` | 245 | **Dispositioned.** Recorded in `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`; the stale labels are marked at the sentence. |
