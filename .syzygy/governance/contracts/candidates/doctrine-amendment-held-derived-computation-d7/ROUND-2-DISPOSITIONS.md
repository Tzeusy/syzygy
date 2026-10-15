# Round 2 dispositions — D7 doctrine amendment packet

> **Candidate — binds nothing.** The record of how each round-2 finding is
> classified. Nothing in the package is repaired here: every finding is
> open for the owner. A disposition is not a confirmation.
> *(Marked 2026-10-14, later the same day: "Nothing in the package is
> repaired here: every finding is open" is no longer true. Every finding
> was repaired once in cycle 2; see §"Repairs, 2026-10-14 (cycle 2)"
> below. The repairs are unconfirmed pending round 3.)*
> *(Marked 2026-10-14, round 3: round 3 returned `REVISE`; see
> `ROUND-3-DISPOSITIONS.md`.)*

**Round:** 2, fresh context. **Raw:**
`docs/reviews/R-DOCTRINE-AMENDMENT-D7-2-RAW.md`, retained verbatim.
**Reviewed commit (raw line 2):** `8f1fbec7723a4e60b8c00f03f260a1979e3d7738`.
**Package digest reviewed (raw line 3):**
`63f16c10a03f34a91eac5499261dd42c0a7b8c834d954ca386d1fd8eb79f377d`
(re-derived 2026-10-14 by the brief's method over the five tracked files at
that commit; it matches).
**Verdict, copied from the raw (line 4):** `Verdict: REVISE`.
**Findings:** 8 — one revise-level (1) and seven notes (2–8), per the raw's
closing count (line 209).

Reviewed record: docs/reviews/R-DOCTRINE-AMENDMENT-D7-2-RAW.md

**Why round 2 ran.** The brief's stopping rule (`REVIEW-BRIEF.md` lines
9–12) said one round only. The owner's direction of 2026-10-14
(`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`)
ordered one fresh confirmation round per packet before the owner is asked
the content questions. The brief and the round-1 raw are not edited (raw
finding 8).
*(Marked 2026-10-14, later the same day: "The brief … not edited" is no
longer true of the brief. Cycle 2 marked its stopping-rule sentence at the
sentence and appended a Round 3 section; its round-1 text is otherwise
unchanged. The round-1 raw is not edited.)*

**Stopping rule applied.** The same direction's rule: one repair and one
review per packet; a packet still `REVISE` goes to the owner with its
findings, not into another loop. D7 had its repair (round 1's) and now its
review. So:

- **The package is not repaired again.** The only edits after the round
  are dated status marks at the sentences finding 8 names (packet, delta
  and `ROUND-1-DISPOSITIONS.md`), the old text kept.
- **No round 3 is dispatched.**
- **The bytes are not confirmed.** The owner decides on them with the
  findings below open. This record recommends nothing on Q1–Q4.

*(Marked 2026-10-14, later the same day: the first two bullets and "with
the findings below open" are no longer true. The owner then directed one
more cycle — repair every finding, notes included, then one fresh review
under the same stopping rule — in the lead session, relayed to this repair
lane [Observed: as relayed; not yet recorded under `decisions/`]. The
package was repaired once (below), and a round 3 is to follow. The bytes
are still not confirmed.)* *(Marked 2026-10-14, round 3: "not yet
recorded under `decisions/`" and "a round 3 is to follow" are no longer
true. The direction is recorded in
`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`,
and round 3 returned `REVISE`; see `ROUND-3-DISPOSITIONS.md`.)*

| # | Level | Finding (short) | Raw line | Disposition |
|---|---|---|---|---|
| 1 | revise | The R1-4 repair reads RFC2's "merge fact" as any merge in a repository's history; RFC2-18's scope is a materialized work item reaching merge, so arm A may leave more unprompted re-observation lawful than §0, §2, §4, §6 item 1 and the ledger's two RFC2 rows tell the owner | 90 | **Open.** Raw's repair: state both readings with RFC2-18's scope sentence, label the one relied on, and restate the named sections and rows. *Repaired 2026-10-14 (cycle 2), below.* |
| 2 | note | Ledger §4's reader breakdown does not sum to its own 11 (one generator, not two; "five tests" names four) | 123 | **Open.** Raw's repair: enumerate as the raw does and correct "five". *Repaired 2026-10-14 (cycle 2), below.* |
| 3 | note | The page-open trigger has the human-versus-agent problem Q3 addresses for hooks, with no test; "a commit" listed unqualified as a human act | 137 | **Open.** Name the residual or qualify the examples. *Repaired 2026-10-14 (cycle 2), below.* |
| 4 | note | §1.2's description of its own bytes is incomplete (lines 7–10 are added, not only line 6 extended) | 151 | **Open.** Correct the sentence. *Repaired 2026-10-14 (cycle 2), below.* |
| 5 | note | RFC5-11 cited at lines 320–323; the words sit on 321–323 | 158 | **Open.** Trivial line-range fix. *Repaired 2026-10-14 (cycle 2), below.* |
| 6 | note | Arm B's defect overstated: the bullet forbids reinterpretation only beyond VIS-4's bounds | 162 | **Open.** Drop or qualify "the bullet forbids". *Repaired 2026-10-14 (cycle 2), below.* |
| 7 | note | The "Not autonomous" intro stays true only on the packet's classification; weight grows under finding 1's narrower reading | 172 | **Open.** Recorded for the owner; no separate repair beyond finding 1. *Repaired 2026-10-14 (cycle 2), below: the weight is now stated in the packet and ledger.* |
| 8 | note | The round departs from the recorded stopping rule; several "no round 2" sentences go false | 179 | **Dispositioned.** The direction record names the warrant; the stale sentences in the packet, delta and round-1 dispositions are marked at the sentence, dated; the brief is not edited. *Further repaired 2026-10-14 (cycle 2), below.* |

## Repairs, 2026-10-14 (cycle 2)

On the owner's further direction of 2026-10-14 (above), each finding was
repaired once. Every line number, clause text and count below was
re-derived from the file at the commit named, not copied from the raw. The
doctrine and contract anchors were re-hashed at `origin/main` `09c7a61d`
(this branch's base) and are unchanged: `vision.md`, `architecture.md`,
`RFC-0002/reconciliation-chain.md` and `RFC-0005/admission-and-boundary.md`
each still hash to the sha256 the delta gives. Section 1's proposed doctrine
bytes did not change. "Packet" is `OWNER-DECISION-PACKET.md`.

| # | Repair |
|---|---|
| 1 | Packet §4.1 (new) states both readings of "merge fact", each with its clause text re-read at `09c7a61d`: **narrow**, RFC2-18's scope sentence (`reconciliation-chain.md` lines 141–142), "merged" (153), RFC2-17's reservation (122–124) and RFC2-19's "reconciliation evaluations" (245–247); **wide**, "merge facts carried by RFC2-1 items 1 and 3" (146) with RFC2-1 item 1 (`snapshot-and-evaluation-core.md` 78–79). The `grep -F "merge fact"` sweep of the RFC-0002 directory (8 hits: lines 61, 146, 156, 158, 225, 274, 334 of the chain module; line 101 of the core module) finds no definition. The packet **relies on the narrow reading** and says why (it is RFC2-18's stated scope, and the wider permission, so the owner rules on the most arm A could license). A table states what arm A permits on each reading. Restated to match: packet §0 (the "most of them" claim removed), §2's "unprompted" paragraph, §4's RFC2-19 and merge-chain rows, §6 items 1 and 2; ledger header and §3's two RFC2 rows and closing paragraph; the delta's RFC2 bullet and downstream summary. Whether the POC's repository carries materialized merged work is stated as **[Unknown]**. **Owner question added:** Q5 (packet §8), answered second: N (narrow, recommended), W (wide; an owner ruling on accepted RFC2 text, whether a plain ruling suffices being [Unknown]), or narrow D7's own text (redraft and fresh review). |
| 2 | Ledger §4 now enumerates the 11 readers as 1 + 2 + 1 + 4 + 1 + 2, re-derived at `66d42d09` by the ledger's Python predicate over the 417 files and confirmed by `git grep -l -E` (11 and 11). "Two generators" and "five tests" corrected; the contract-index generator is stated to sit outside the population (`.syzygy/governance/contracts/candidates/scripts/build_contract_index.py`, naming doctrine only as `../../doctrine`, line 46) and to have been found through `05-CONTRACT-INDEX.yaml`'s word counts. |
| 3 | Packet §2: the Trigger row's examples now read "a human opening a page, a human recording a security act; a commit a human makes, but only as relayed by a qualifying hook"; a new paragraph, "Showing that a trigger was human — a named residual", says an agent's or scheduled client's page open is not a human act, that a cadenced external client is a poller by proxy, and that the packet drafts no test. §6 item 7 (new) lists the showing as a separate implementation step; Q3's strict arm states the same burden for page opens. No owner choice was needed: the text already forbids non-human triggers. |
| 4 | Packet §1.2's sentence now reads: ten lines, the first five the anchor's lines 329–333 unchanged, the sixth beginning with line 334 and extended, lines 7–10 added. The delta's matching sentence says the same. `ROUND-1-DISPOSITIONS.md` row 15 is marked at the sentence. |
| 5 | Packet §3: RFC5-11 cited at lines 321–323 (re-read: line 320 blank, the quoted words on 321–323). |
| 6 | Packet Q2 arm B: "the 'reinterpretation' the bullet forbids" replaced by "B misrecords existing meaning: it records a Normative change as if it were Clarifying", with a parenthesis stating that the bullet's bar reaches only autonomy beyond VIS-4's bounds and so is not what B offends. |
| 7 | Packet §7 gains "The weight this puts on 'not autonomous'", and the ledger's `vision.md` row the same sentence: on the narrow reading D7 licenses more unprompted computation than round 1's text described, so the intro (lines 86–87) and the Q1 ruling carry more weight. |
| 8 | Stale sentences marked at the sentence, dated, old text kept: this record's head, "Why round 2 ran" and "Stopping rule applied"; each table row's "Open"; `REVIEW-BRIEF.md`'s stopping rule; `ROUND-1-DISPOSITIONS.md` rows 4, 12 and 15. Packet, delta and ledger heads carry the state "round-2 findings repaired once on 2026-10-14, unconfirmed pending round 3". `REVIEW-BRIEF.md` gains a Round 3 section with the head contract and the stopping rule. The round-1 and round-2 raws are not edited. |

**What was not changed.** Section 1's doctrine text, the change class
(Normative), the four-effect class, the strict hook test, the entry
criteria and the recommendation on Q1–Q4. The direction record
`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md` is
not edited here; its sentence that none of the eight `REVISE` packets is
repaired again predates the owner's further direction and is left to the
lead session.
