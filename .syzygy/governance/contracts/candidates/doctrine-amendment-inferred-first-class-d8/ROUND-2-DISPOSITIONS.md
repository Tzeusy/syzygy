# Round 2 dispositions — D8 doctrine amendment packet

> **Candidate — binds nothing.** The record of how each round-2 finding is
> classified. Nothing in the package is repaired here: every finding is
> open for the owner. A disposition is not a confirmation.
> *(Marked 2026-10-14, later the same day: "nothing in the package is
> repaired" and "every finding is open" are no longer true. On the owner's
> direction of 2026-10-14 in the lead session, every finding was repaired
> once; see "Repairs, 2026-10-14 (cycle 2)" below. The table's
> classification is left as it was written.)*

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
*(Marked 2026-10-14, later the same day: "not repaired again" and "no
round 3 is dispatched" are superseded. The owner, in the lead session on
2026-10-14, directed one more cycle for this packet: repair every round-2
finding, notes included, once, then one fresh review under the same
stopping rule. The repair is below; round 3 is briefed in
`REVIEW-BRIEF.md` §"Round 3" and is not dispatched by the repairing
session.)* *(Marked 2026-10-14, round 3: round 3 was dispatched and
returned `REVISE`; see `ROUND-3-DISPOSITIONS.md`.)*

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

## Repairs, 2026-10-14 (cycle 2)

**Direction.** The owner, in the lead session on 2026-10-14, directed one
more cycle for this packet: repair every round-2 finding, notes included,
once; then one fresh review under the same stopping rule [Observed: as the
lead session relayed it to the repairing session; no decisions file
records it at `09c7a61d`]. The repairing session adopts, records and
dispatches nothing. The repaired bytes are **repaired once on 2026-10-14,
unconfirmed pending round 3** (`REVIEW-BRIEF.md` §"Round 3"). *(Marked
2026-10-14, round 3: "no decisions file records it" and "pending round 3"
are no longer true. The direction is recorded in
`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`,
and round 3 returned `REVISE`; see `ROUND-3-DISPOSITIONS.md`.)*

**Base.** Repairs were made on `09c7a61d759bd582227c38b6bec648fe1758fade`
(`origin/main` when the repair began). Every line number, quotation and
figure below was re-read or re-run from the file at that commit, not copied
from the raw. The three doctrine digests are unchanged there
(`sha256sum`, scripted).

| # | Level | Repair (where) |
|---|---|---|
| 1 | revise | Clause (e) rewritten and moved (packet §1 (e); delta class row and proposed meaning; §2 row unchanged). "Release verdict" dropped: the denial now covers exactly the line-60 triggers, "alignment, convergence or genome-completeness". The permissive sentence now reads "Evidence that any of the trust floor's four properties holds may come from any subject, this one included", so floor bullets 3 and 4 are no longer under the denial. The anchor moved from the trust floor (lines 175–180) to the status-claim triggers (lines 57–67, insert after line 67). A dated repair note under the block quotes what changed |
| 2 | revise | RFC7-20 named and quoted (line 416) in packet §0's (a) row and §1 (a); the (a) bytes now say a synthesis "renders Inferred, unless the surface admits generated prose only as a draft, where it is that draft and never a claim", deferring to RFC7-20 on Polaris without citing a contract number (doctrine cites none: 0 lines match `RFC ?[0-9]` in the six doctrine files). §2's (a) row, delta class row, current and proposed meaning, and ledger §3.4 (new RFC7-20 and RFC7-21 rows) updated. Q1's "decline" rechecked and kept, its reason now naming RFC7-20. The ledger §3.3 [Unknown] (a)/(f) overlap is resolved by the generator specification's line 528 ("A generated bundle SHALL remain editorial-draft…"), marked at the sentence and in §5 item 3. The owner's in-force RFC7-20 reading act is cited as consistent. **Owner question added: Q-C3** (an RFC7-20 amendment, asked, not drafted). Q-S1 now notes the `editorial-draft` consequence and PWB's own render-time generation exclusion (coverage part line 74) |
| 3 | revise | Ledger §5 item 2 now quotes the current trigger, "When Syzygy's observation pipeline evaluates Syzygy's own governance root as its subject", with a dated repair note naming the superseded quotation; the "main risk" wording is withdrawn |
| 4 | note | Already dispositioned by the 2026-10-14 confirmation-cycle record. The new cycle's state sentences are marked at the sentence, dated, in the packet's review state, the delta's head and Review section, the ledger head, this record's head and stopping-rule paragraph, and register row P-102 |
| 5 | note | §2's (f) row now reads "`editorial-draft` before the human authorship act (RFC2-25, RFC7-20); after it, presentation, non-citable (RFC7-4)"; the delta's (f) proposed meaning matches. §1 (f) discloses that applying `editorial-draft` to a figure or passage selection extends RFC2-25's "Narrative prose under revision", citing the generator specification's diagram rule (line 98) as the one existing precedent; ledger §3.4's RFC2-25 row says so |
| 6 | note | §1 (d) no longer attributes the phrase to P-76 Q2: it cites the M4 funnel Q3 for (d2)'s sense and says P-76 Q2 uses the phrase for self-observation |
| 7 | note | §1 (d) now states that the funnel's recommended arm (a) placed packets in "Syzygy's own `.syzygy/governance/decisions/`", quotes the funnel's own statement of that arm's cost, records that the owner chose (b) with no reason recorded (rulings file line 58), and says why (d) does not reopen the choice and what trade-off it does put to the owner |
| 8 | note | (d1) rewritten and moved: it now follows the repository bullet list (after `architecture.md` line 27) as its own paragraph; it says an observed-only project "is a governed project" and replaces "its write surface is empty" with "no act in force names a write into it", keeping `writeSurface` out of doctrine. §1 (d) explains the governed-project reading and line 14's "writes only" |
| 9 | note | Q-C2's arms rewritten: records cannot stay unlinked, so the question is whether naming another project's entity is an SDR-30 relationship or a reference. Offboarding: `architecture.md` lines 115–117 quoted in §1 (d); **owner question added: Q-D1**, with three arms and none drafted into (d2) |
| 10 | note | Repaired (e) says "The rule adds no property to the trust floor", and sits outside the floor's section. §1 (e) answers "Release-blocking? No, as drafted" and gives the reason; Q5 gains the arm "adopt as a fifth, release-blocking trust-floor bullet instead (not drafted)", noting it would also change VIS-7's list in `vision.md` |
| 11 | note | §7 Q3's cell now rests the decline on `trust-and-evidence.md` lines 118–119; the delta's (a) row replaces "regenerate on change" with the clause's own freshness and withdrawal rule |
| 12 | note | Ledger re-pinned to `09c7a61d`: term sweep 1,883 files, 151 hit files, 438 occurrences, set-equal by `git grep` (151); authority-lane file sets unchanged since `59fbf787`; the nine new decision occurrences are this packet's own P-102 row (line 1179); §3.2 line numbers re-read (P-98 1042 → 1175, decision history 48 → 88). Static reader sweep 962 files, 52 readers; the 13 new readers read only `security.md` or `v1.md`. Digest census: D7's packet (lines 94, 128) and delta (lines 12, 14) now carry the `vision.md` and `architecture.md` digests; the absence sentence is marked. Packet §8 adds D9 and re-checks D7's anchors at `09c7a61d`. The application probe was re-run over the repaired bytes at `09c7a61d` (ledger §4): baseline 96 commands, 0 nonzero; applied 96, 6 nonzero, the same six commands and messages as round 1's probe. Scripts that produced these figures reproduced the round-1 figures and lane rows exactly at `59fbf787` first |

### Found while repairing, not in either raw

- **REQ-polaris-generation-032**, the non-governed narrative profile
  (adopted 2026-10-07), defines a *non-governed* subject. Packet §8 now
  says it is not (d1)'s observed-only project and that (d2) says nothing
  about it [Inferred].
- **The owner's RFC7-20 reading act** of 2026-10-07 describes an agent
  draft as rendering "as an editorial draft"; cited in §0 as consistent with
  finding 2's reading.
- **D7 was repaired concurrently** and landed on `main` as `7071a744`
  while this repair was open; this branch was rebased onto it. At
  `7071a744` D7's anchors are unchanged (packet §8), and D7's ledger line
  201 still calls the Polaris understanding recorder "unaffected", which
  this repair's probe contradicts for any `vision.md` insertion (ledger §5
  item 4). D7's bytes are not edited here; routed to the coordinator.
