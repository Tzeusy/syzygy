# Round 3 dispositions — D7 doctrine amendment packet

> **Candidate — binds nothing.** The record of how each round-3 finding is
> classified. Nothing in the package is repaired here: every finding is
> open for the owner. A disposition is not a confirmation.

**Round:** 3, fresh context. **Raw:**
`docs/reviews/R-DOCTRINE-AMENDMENT-D7-3-RAW.md`, retained verbatim.
**Reviewed commit (raw line 2):** `7071a7440fbf85e8d12f13e804dbd57af400a453`.
**Package digest reviewed (raw line 3):**
`cc9709730aeab80f51256b57f1ac5d27515d9be229f3e957df6c66524af1490f`
(re-derived 2026-10-14 by the brief's method over the six tracked files at
that commit; it matches).
**Verdict, copied from the raw (line 4):** `Verdict: REVISE`.
**Findings:** 6 — one revise-level (1) and five notes (2–6), per the raw's
closing count (line 262).

Reviewed record: docs/reviews/R-DOCTRINE-AMENDMENT-D7-3-RAW.md

**Why round 3 ran.** The owner's direction of 2026-10-14 for a second
cycle, now recorded in
`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`:
repair every finding, notes included, then one fresh review under the same
stopping rule. The brief's §"Round 3" set that rule before the round.

**Stopping rule applied.** A verdict of `REVISE` goes back to the owner
with its findings open: no further repair and no round 4 without a new
owner direction (brief §"Round 3"; raw lines 258–260). So:

- **The package is not repaired again.** The only edits after the round
  are dated status marks at the "unconfirmed pending round 3" sentences in
  the packet, the delta, the ledger and `ROUND-2-DISPOSITIONS.md`, with the
  old text kept. The two unwrapped lines and stale cross-references the raw
  names (notes 4 and 5) are not touched; fixing them is their repair.
- **No round 4 is dispatched.**
- **The bytes are not confirmed.** This record and the marks move the
  package's directory digest away from the value above; the reviewed bytes
  stay retrievable at the reviewed commit. This record recommends nothing
  on Q1–Q5.

| # | Level | Finding (short) | Raw line | Disposition |
|---|---|---|---|---|
| 1 | revise | Q5 states its arms' consequences inconsistently: arm W carries an [Unknown] on whether a plain owner ruling suffices to fix the reading of accepted RFC2 text, while arm N (recommended) says "No further step", though choosing N is equally a ruling on that text; §4's merge-chain row and §6 item 1 treat a ruling as sufficient, and ledger row 117 drops the ruling route | 98 | **Open for the owner.** Raw's repair: state one position on whether an owner ruling can settle the reading of accepted RFC2 text (labelled [Unknown] if unknown), apply it symmetrically to N and W, and make §4's row, §6 item 1 and ledger row 117 agree; or argue why choosing N is not an interpretation of accepted text. |
| 2 | note | §4.1 does not weigh RFC4's own reading of RFC2-19 (`named-adapters.md` lines 420 and 492, "ordinary human-triggered observation passes (RFC2-19)") | 143 | **Open.** Name the two lines in §4.1 and give the ledger's RFC4 row a disposition on the reading question. |
| 3 | note | "Unlawful until shown" for a page open is the packet's reading, not something section 1 carries; Q3's strict arm ties the page-open burden to its hook arm | 165 | **Open.** Label the sentence as the packet's reading or an implementation obligation, and say in Q3 that the page-open burden does not depend on its arm. |
| 4 | note | Two ledger cross-references are stale (§5 item 1 "packet §6.1", row 126 "packet §6.2"), and §4.1's line 146 citation should be 145–146 | 188 | **Open.** Trivial fixes. |
| 5 | note | The cycle-2 repair left two unwrapped lines (at the reviewed commit, packet line 515, 128 columns; ledger line 153, 123 columns; the status marks above shift both) | 206 | **Open.** Rewrap; neither line holds a code span, so no citation splits. |
| 6 | note | The warrant for round 3 is not recorded under `decisions/`, and the cycle-1 direction record still says no `REVISE` packet is repaired again | 219 | **Dispositioned outside the package.** The direction is recorded in `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`, and the stale sentence in `OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md` is marked at the sentence, dated, with the old text kept. |

**Stale sentences outside the package.** Register row P-101 and
`docs/README.md`'s D7 row are updated directly. `REVIEW-BRIEF.md`'s
§"Round 3" warrant line ("not yet recorded under `decisions/`") is not
edited; the direction record above answers it.
