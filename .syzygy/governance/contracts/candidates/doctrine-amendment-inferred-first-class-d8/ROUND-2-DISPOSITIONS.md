# Round 2 dispositions — D8 doctrine amendment packet

> **Candidate — binds nothing.** The record of how each round-2 finding is
> classified. Nothing in the package is repaired here: every finding is
> open for the owner. A disposition is not a confirmation.

**Round:** 2, fresh context. **Raw:**
`docs/reviews/R-DOCTRINE-AMENDMENT-D8-2-RAW.md`, retained verbatim.
**Reviewed commit (raw line 2):** `8f1fbec7723a4e60b8c00f03f260a1979e3d7738`.
**Package digest reviewed (raw line 3):**
`bf095a565049e4900a0744b2cb82a39f7bec9b5d59791307bb79f6560e091c34`
(re-derived 2026-10-14 by the brief's method over the five tracked files at
that commit; it matches).
**Verdict, copied from the raw (line 4):** `Verdict: REVISE`.
**Findings:** 12 — three revise-level (1–3) and nine notes (4–12), per the
raw's summary (lines 280–281).

Reviewed record: docs/reviews/R-DOCTRINE-AMENDMENT-D8-2-RAW.md

**Why round 2 ran.** The brief's stopping rule (`REVIEW-BRIEF.md` lines
9–12) said one round only; the reviewer recorded the departure (raw lines
33–36). The owner's direction of 2026-10-14
(`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`)
ordered one fresh confirmation round per packet before the owner is asked
the content questions. The brief is not edited.

**Stopping rule applied.** One repair and one review per packet; a packet
still `REVISE` goes to the owner with its findings, not into another loop.
D8 had its repair (round 1's) and now its review. So the package is not
repaired again (the only edits are dated status marks at the sentences
finding 4 names), no round 3 is dispatched, and the bytes are not
confirmed. This record recommends nothing on the packet's questions.

| # | Level | Finding (short) | Raw line | Disposition |
|---|---|---|---|---|
| 1 | revise | Clause (e) denies self-observation records to the "release verdict" while letting them evidence the trust floor, which is the release verdict; floor bullets 3 and 4 left under the denial | 92 | **Open.** Raw's repair: drop "release verdict" from the denial, or state that evidence for all four floor properties may come from any subject and say what "release verdict" excludes |
| 2 | revise | Clause (a) on Polaris collides with accepted RFC7-20 (generated prose only as `editorial-draft`), which the §0 (a) premise check does not name | 120 | **Open.** Cite RFC7-20 in §0 and §1 (a); scope (a) outside RFC 0007 or to adopted narrative, or route an RFC7-20 question beside Q-S1; recheck Q1's "decline" rationale |
| 3 | revise | IMPACT-LEDGER §5 item 2 still quotes clause (e)'s pre-repair trigger as current text | 152 | **Open.** Quote the current trigger, or mark the item superseded at the sentence |
| 4 | note | Review-state sentences ("no round 2 ran") go stale when this round lands | 171 | **Dispositioned.** Packet line 14 and the delta's Review section are marked at the sentence, dated; register row P-102 is updated; this record names the direction |
| 5 | note | §2's (f) row says `editorial-draft` "before and after" the authorship act; `editorial-draft` applied to figures extends RFC2-25's semantics | 183 | **Open** |
| 6 | note | "Observing project" attributed to P-76 Q2, which uses it for self-observation | 195 | **Open.** Cite the M4 funnel Q3, or say both senses exist |
| 7 | note | The P-71 Q3 statement omits that the owner declined the arm placing content in Syzygy's own decisions directory | 207 | **Open.** Keep the owner's trade-off visible |
| 8 | note | (d1) brings `writeSurface` into doctrine undefined; whether an observed-only project is a governed project; placement as a sibling bullet | 218 | **Open** |
| 9 | note | (d2)'s dismissals cannot stay unlinked to the observed project's entities (Q-C2 arm); offboarding of such dismissals unstated | 229 | **Open** |
| 10 | note | (e) sits inside the normative trust floor without saying whether it is release-blocking | 240 | **Open** |
| 11 | note | Q3's §7 rationale lags the reclassification of (c); the delta's (a) row says "regenerate on change" | 248 | **Open** |
| 12 | note | Figures and absence claims pinned to `59fbf787`; several moved by the reviewed commit (term sweep, digest absence, D9, battery) | 259 | **Open.** Lawful under the ledger's rule-7 scope; re-derive at the sign-off commit |
