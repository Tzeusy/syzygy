# Round 3 dispositions — D7 doctrine amendment packet

> **Candidate — binds nothing.** The record of how each round-3 finding is
> classified. Nothing in the package is repaired here: every finding is
> open for the owner. A disposition is not a confirmation.
> *(Marked 2026-10-14, cycle 3: "Nothing in the package is repaired here:
> every finding is open" is no longer true. On the owner's cycle-3
> direction every finding was repaired once; see §"Repairs, 2026-10-14
> (cycle 3)" below. **Round-3 findings repaired once on 2026-10-14,
> unconfirmed pending round 4.**)*

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

*(Marked 2026-10-14, cycle 3: the first two bullets are no longer true.
The owner then directed one more cycle for P-101 in the lead session:
"One more cycle" — "Make Q5 consistent: state that choosing a reading of
accepted text is a contract act matter (Unknown otherwise), and align
§4/§6 and the ledger. Then one fresh review." [Observed: as relayed by the
lead session to this repair lane; not yet recorded under `decisions/`.]
The package was repaired once (below), and a round 4 is briefed in
`REVIEW-BRIEF.md` §"Round 4". The bytes are still not confirmed.)*

| # | Level | Finding (short) | Raw line | Disposition |
|---|---|---|---|---|
| 1 | revise | Q5 states its arms' consequences inconsistently: arm W carries an [Unknown] on whether a plain owner ruling suffices to fix the reading of accepted RFC2 text, while arm N (recommended) says "No further step", though choosing N is equally a ruling on that text; §4's merge-chain row and §6 item 1 treat a ruling as sufficient, and ledger row 117 drops the ruling route | 98 | **Open for the owner.** Raw's repair: state one position on whether an owner ruling can settle the reading of accepted RFC2 text (labelled [Unknown] if unknown), apply it symmetrically to N and W, and make §4's row, §6 item 1 and ledger row 117 agree; or argue why choosing N is not an interpretation of accepted text. *Repaired 2026-10-14 (cycle 3), below.* |
| 2 | note | §4.1 does not weigh RFC4's own reading of RFC2-19 (`named-adapters.md` lines 420 and 492, "ordinary human-triggered observation passes (RFC2-19)") | 143 | **Open.** Name the two lines in §4.1 and give the ledger's RFC4 row a disposition on the reading question. *Repaired 2026-10-14 (cycle 3), below.* |
| 3 | note | "Unlawful until shown" for a page open is the packet's reading, not something section 1 carries; Q3's strict arm ties the page-open burden to its hook arm | 165 | **Open.** Label the sentence as the packet's reading or an implementation obligation, and say in Q3 that the page-open burden does not depend on its arm. *Repaired 2026-10-14 (cycle 3), below.* |
| 4 | note | Two ledger cross-references are stale (§5 item 1 "packet §6.1", row 126 "packet §6.2"), and §4.1's line 146 citation should be 145–146 | 188 | **Open.** Trivial fixes. *Repaired 2026-10-14 (cycle 3), below.* |
| 5 | note | The cycle-2 repair left two unwrapped lines (at the reviewed commit, packet line 515, 128 columns; ledger line 153, 123 columns; the status marks above shift both) | 206 | **Open.** Rewrap; neither line holds a code span, so no citation splits. *Repaired 2026-10-14 (cycle 3), below.* |
| 6 | note | The warrant for round 3 is not recorded under `decisions/`, and the cycle-1 direction record still says no `REVISE` packet is repaired again | 219 | **Dispositioned outside the package.** The direction is recorded in `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`, and the stale sentence in `OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md` is marked at the sentence, dated, with the old text kept. *Also cited 2026-10-14 (cycle 3), below: the package now cites that record.* |

**Stale sentences outside the package.** Register row P-101 and
`docs/README.md`'s D7 row are updated directly. `REVIEW-BRIEF.md`'s
§"Round 3" warrant line ("not yet recorded under `decisions/`") is not
edited; the direction record above answers it. *(Marked 2026-10-14, cycle
3: "is not edited" is no longer true; cycle 3 marked that line at the
sentence, repair 6 below.)*

## Repairs, 2026-10-14 (cycle 3)

On the owner's cycle-3 direction of 2026-10-14 (quoted above), each
finding was repaired once, notes included. Every clause text and line
number below was re-read from the file at `origin/main` `7460aec8` (this
branch's base), not copied from the raw. At that commit `vision.md`,
`architecture.md` and `RFC-0002/reconciliation-chain.md` still hash to the
sha256 values in `SEMANTIC-DELTA.md`, and section 1's proposed doctrine
bytes did not change. "Packet" is `OWNER-DECISION-PACKET.md`.

| # | Repair |
|---|---|
| 1 | **One position, applied to every reading:** choosing which reading of accepted RFC2-18/RFC2-19 text binds is a contract-act matter, and the reading is **[Unknown]** until a contract act fixes it (the owner's cycle-3 wording). Neither the packet, a doctrine amendment, nor a plain owner answer to Q5 fixes it, for the narrow reading any more than the wide. The packet no longer "relies on" any reading. Stated in: packet §0 (a three-row reach list: no merge in history, lawful at the doctrine level on the narrow and wide readings; merges but no materialized merged work, [Unknown]; materialized merged work, unlawful), §2's "unprompted" paragraph, §4's merge-chain row, §4.1 (new "Choosing a reading is a contract-act matter" paragraph and a reach table with an "until a contract act fixes the reading" column), §6 item 1 and item 2's hook sub-bullet, §7's weight paragraph (now conditional on a later contract act), and §8's introduction; ledger header, §3's `vision.md` row, merge-chain row and closing paragraph; the delta's RFC2 bullet and downstream summary. The owner-ruling alternative is gone from §4's row and §6 item 1, and the ledger row's "until RFC2 is amended" now names a contract act in either form. **Q5 restructured: the arms collapse.** "Adopt against N" and "adopt against W" are both a choice of reading, which a plain Q5 answer cannot make, so Q5 now asks how the reading is to be fixed: **U** leave it to a contract act and fix none here (recommended; the middle row stays [Unknown]), **K** commission a contract act carrying a named reading (form [Unknown], not drafted; combinable with U), or **narrow D7's own text** (redraft and fresh review). The round-2 arms are quoted in a dated parenthesis. §4.1 names the owner's RFC7-20 reading act as an example of an exact-bytes act binding a reading of one accepted clause, and labels [Unknown] whether that form would serve for RFC2. |
| 2 | Packet §4.1 gains a bullet weighing accepted RFC4's citations of RFC2-19, "Capture runs inside ordinary human-triggered observation passes (RFC2-19)" (`named-adapters.md` lines 420–421; the raw cited 420, where the quotation begins) and "ordinary human-triggered observation passes (RFC2-19)" (492), as evidence for a third, broadest reading on which no unprompted re-observation is lawful at all; the packet weighs it against [Inferred] and shows it as a column of the reach table. Packet §0 and §4's RFC2-19 row name it. The ledger's RFC4 row gains a disposition on the reading question. |
| 3 | Packet §2's residual paragraph and §6 item 7 now say section 1 states a condition ("when the trigger is a human act"), not a burden of proof, and label the obligation to show a page-open trigger was human as the packet's reading and an implementation obligation that does not travel with the doctrine bytes [Inferred]. Q3's strict arm now covers hooks only, and a following line marked "Not an arm" says the page-open condition does not depend on Q3. |
| 4 | Ledger §5 item 1 now cites packet §6 item 2, and the `openspec/changes/polaris-manifesto-generation/` row of ledger §3 cites §6 item 3, each with a dated note. Packet §4.1 and the ledger's merge-chain row cite "the merge facts carried by RFC2-1 items 1 and 3" at lines 145–146 (re-read: "— the" ends line 145, "merge facts carried" begins line 146). |
| 5 | Packet Q2 arm B's long line and the ledger §3 closing paragraph's long line are rewrapped. Every prose line the repair wrote in the packet, ledger and delta is at most 80 columns outside table rows, except one packet §4.1 line that holds the RFC7-20 reading act's path in a single code span, which is not broken (86 columns); the four other lines over 80 columns in those files (two headings, two delta paths) predate this repair [Observed: scripted column check over the three files]. |
| 6 | The cycle-2 direction is cited as `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md` (packet status note, this record's head and `ROUND-2-DISPOSITIONS.md`), and `REVIEW-BRIEF.md` §"Round 3"'s warrant sentence ("not yet recorded under `decisions/`") is now marked at the sentence, dated. The **cycle-3** direction this repair runs on is quoted as relayed by the lead session and is **not yet recorded under `decisions/`** [Observed: no `decisions/` file names it at `7460aec8`]; the same gap note 6 found for cycle 2 is open again for cycle 3 and is left to the lead session. |

**Also repaired: the recorder gate, found by the D8 lane.** Ledger §4
said `scripts/record_polaris_understanding_adoption.py` is "unaffected: it
reads history, not today's bytes". It is not. The recorder binds
`vision.md` as a frozen input outside its history set
(`VISION`, line 240; `FROZEN_PATHS`, 243–244; `HISTORY_PATHS`, 250) and
fails any input whose current digest differs from its C1 review's (line
592). A probe in a scratch worktree at `7460aec8` [Observed, this
session]: baseline `--check` prints `PASS`; with only section 1.1 applied,
`--check` fails "review retired by changed input:
.syzygy/governance/doctrine/vision.md" and `--selftest` fails "candidate
input drift" on the same path; with only section 1.2 applied, `--check`
passes. The ledger row now says so, the evidence row beside it says the
review is retired for the recorder's purposes, ledger §4 records the probe,
the delta's migration note is marked at the sentence, packet §9 makes
step 1 wait for the answer, and **owner question Q6 is added**: reconcile
by a fresh review, move `vision.md` into the recorder's history set by a
reviewed change, or decline arm A; shared with D8's Q-A1.

**What was not changed.** Section 1's doctrine text, the change class
(Normative), the four-effect class, the strict hook test, the entry
criteria, and the recommendations on Q1–Q4. The round-1, round-2 and
round-3 raws are not edited.
