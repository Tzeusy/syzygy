# Round 2 dispositions — Three-Surface POC governing-intent amendment

> **Candidate — binds nothing.** This record classifies each round-2
> finding. Nothing in the package is repaired here: every finding is open
> for the owner. It is not itself reviewed.

**Raw review:** `docs/reviews/R-N10-POC-GOVERNING-INTENT-2-RAW.md`, stored
verbatim (CC-REV-6).

Reviewed record: docs/reviews/R-N10-POC-GOVERNING-INTENT-2-RAW.md

**Reviewed bytes:** commit `8f1fbec7723a4e60b8c00f03f260a1979e3d7738` (raw
line 2); package digest
`9dd50df37859406bb813a44b0b5cc553c8cf5c87d2d875c53ccd410b301b6640` (raw
line 3), over the nine tracked package files, re-derived 2026-10-14 by the
raw's stated method at that commit; it matches.

**Verdict, copied from the raw (line 4):** `Verdict: REVISE`

**Findings:** 9 — four `revise` (1–4) and five `note` (5–9), counted from
the raw's nine `**Finding N — <title>** (<class>)` headings (the raw has no
closing count line).

**Why round 2 ran.** Round 1's stopping rule said no round 2. The owner's
direction of 2026-10-14
(`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`)
ordered one fresh confirmation round per packet before the owner is asked
the content questions.

**Stopping rule applied.** One repair and one review per packet; a packet
still `REVISE` goes to the owner with its findings, not into another loop.
This package had its repair (round 1's) and now its review. **The bytes
are not cleared** and this version is not offered for sign-off. The only
edits after the round are dated status marks at the sentences finding 8
names. No round 3 is dispatched. This record recommends nothing on Q1–Q3.

| # | Class | Finding (raw title, short) | Raw line | Disposition |
|---|---|---|---|---|
| 1 | revise | The Trajectory arms of the oracle contradict signed POC-REQ-042's bounded board | 40 | **Open.** Raw's repair: state the Trajectory arms over Trajectory's rendered selection, or say how the narrowed view relates to the excluded population; re-judge the RFC8-23 "filterable" row |
| 2 | revise | The oracle still does not decide the per-item marker, the resolution sentence or the non-green encoding the requirement and covered rows claim | 43 | **Open.** Add them to the oracle with a decision procedure, or narrow the RFC8-23 and RFC8-24 covered rows |
| 3 | revise | RFC8-24, newly mapped, has two unlisted limbs (aggregation rule; claim-reasons-only / no absorption) | 46 | **Open.** Add a row for each |
| 4 | revise | The ledger and delta omit the P-97 block-provenance sibling, whose dependency patch makes this one's fail at its `Source:` hunk | 49 | **Open.** Name P-97 in the ledger, delta and packet. [Observed 2026-10-14] P-97's builder `--check` still passes on the integration branch and warns of the declared P-84/P-100 exclusive pair |
| 5 | note | The orphaned-work sentence is a SHALL with no reachable case or oracle | 52 | **Open** |
| 6 | note | RFC2-24's Part A rows do not record POC-REQ-014 | 55 | **Open** |
| 7 | note | Reason #10 is the best fit weighed; its route and the RFC8-21 B2 rationale are weaker than stated | 58 | **Open** |
| 8 | note | Packet plainness; status sentences this round makes stale (packet Status, register P-100, `docs/README.md`) | 61 | **Dispositioned for the stale sentences.** The packet Status and `ROUND-1-DISPOSITIONS.md` are marked at the sentence, dated; register row P-100 and the `docs/README.md` campaign row are updated. The jargon half is **open** |
| 9 | note | Items confirmed without exception | 64 | **No action.** Recorded as the reviewer's confirmation of criteria 1, 4, 5 and most of 6 |
