# Round 2 dispositions — Three-Surface POC governing-intent amendment

> **Candidate — binds nothing.** This record classifies each round-2
> finding. Nothing in the package is repaired here: every finding is open
> for the owner. It is not itself reviewed.
> *(Marked 2026-10-14, later the same day: "Nothing in the package is
> repaired here: every finding is open" is no longer true. Every finding
> was repaired once in cycle 2; see §"Repairs, 2026-10-14 (cycle 2)"
> below. Round-2 findings repaired once on 2026-10-14, unconfirmed pending
> round 3.)*

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
*(Marked 2026-10-14, later the same day: "The only edits after the round
are dated status marks" and "No round 3 is dispatched" are no longer true.
The owner then directed one more cycle — repair every finding, notes
included, then one fresh review under the same stopping rule — in the lead
session, relayed to this repair lane [Observed: as relayed; not recorded
under `decisions/` at this commit]. The package was repaired once (below),
and round 3 is briefed in `REVIEW-BRIEF.md` §"Round 3"; this lane
dispatches no review. The bytes are still not cleared, and this record still
recommends nothing on Q1–Q3.)*

| # | Class | Finding (raw title, short) | Raw line | Disposition |
|---|---|---|---|---|
| 1 | revise | The Trajectory arms of the oracle contradict signed POC-REQ-042's bounded board | 40 | **Open.** Raw's repair: state the Trajectory arms over Trajectory's rendered selection, or say how the narrowed view relates to the excluded population; re-judge the RFC8-23 "filterable" row. *Repaired 2026-10-14 (cycle 2), below.* |
| 2 | revise | The oracle still does not decide the per-item marker, the resolution sentence or the non-green encoding the requirement and covered rows claim | 43 | **Open.** Add them to the oracle with a decision procedure, or narrow the RFC8-23 and RFC8-24 covered rows. *Repaired 2026-10-14 (cycle 2), below.* |
| 3 | revise | RFC8-24, newly mapped, has two unlisted limbs (aggregation rule; claim-reasons-only / no absorption) | 46 | **Open.** Add a row for each. *Repaired 2026-10-14 (cycle 2), below.* |
| 4 | revise | The ledger and delta omit the P-97 block-provenance sibling, whose dependency patch makes this one's fail at its `Source:` hunk | 49 | **Open.** Name P-97 in the ledger, delta and packet. [Observed 2026-10-14] P-97's builder `--check` still passes on the integration branch and warns of the declared P-84/P-100 exclusive pair. *Repaired 2026-10-14 (cycle 2), below; P-97 was signed v1.0 the same day, so the patches were regenerated over its applied bytes.* |
| 5 | note | The orphaned-work sentence is a SHALL with no reachable case or oracle | 52 | **Open.** *Repaired 2026-10-14 (cycle 2), below.* |
| 6 | note | RFC2-24's Part A rows do not record POC-REQ-014 | 55 | **Open.** *Repaired 2026-10-14 (cycle 2), below.* |
| 7 | note | Reason #10 is the best fit weighed; its route and the RFC8-21 B2 rationale are weaker than stated | 58 | **Open.** *Repaired 2026-10-14 (cycle 2), below.* |
| 8 | note | Packet plainness; status sentences this round makes stale (packet Status, register P-100, `docs/README.md`) | 61 | **Dispositioned for the stale sentences.** The packet Status and `ROUND-1-DISPOSITIONS.md` are marked at the sentence, dated; register row P-100 and the `docs/README.md` campaign row are updated. The jargon half is **open**. *Jargon half repaired 2026-10-14 (cycle 2), below.* |
| 9 | note | Items confirmed without exception | 64 | **No action.** Recorded as the reviewer's confirmation of criteria 1, 4, 5 and most of 6 |

## Repairs, 2026-10-14 (cycle 2)

On the owner's further direction of 2026-10-14 (above), each finding was
repaired once. Every figure below was re-derived from the bytes at the
commit named, not copied from the raw. The base is `origin/main` `814fbcc1`,
where P-97 (the block-provenance amendment) is signed v1.0. The four patches
under `proposed/` were regenerated there: the round-2 `spec.md`,
`CONTRACT-COVERAGE.md` and `proposal.md` patches applied in a scratch
worktree (the spec patch at offset 54), edited, then
`scripts/build_three_surface_poc_spec_dependencies.py` regenerated
`GOVERNING-DEPENDENCIES.md`, and `git diff` wrote the four patches.
"Packet" is `OWNER-DECISION-PACKET.md`; "the delta" is `SEMANTIC-DELTA.md`.

| # | Repair |
|---|---|
| 1 | **Scoped to what POC-REQ-042 lets Trajectory show; no owner question needed.** POC-REQ-014's required behavior, scope, case, observable, oracle, falsifier and scenario 1 now run the item-level Trajectory arms over Trajectory's rendered selection: Trajectory shows the served count beside how many of those items its selection holds and how many fall outside it; it marks every item it renders; the narrowed board lists exactly the items the un-narrowed board renders. The oracle's second denominator is the checker's own enumeration of rendered items; the inside figure must equal it, and inside plus outside must equal the count. Scenario 1 now reads "N work items and Trajectory renders a selection of R of them (POC-REQ-042)". The RFC8-23 covered row is re-judged to "filterable within Trajectory's rendered selection", and a new Unknown row carries filtering of items outside it. The delta's §"What the delta says" and §"Denominators" and the packet's §"What is already drafted" say so; the packet tells the owner plainly that items off the board are counted, not filterable. [Inferred] Scoping, not an owner question, because POC-REQ-042 is signed and the raw's first suggested repair is exactly this. |
| 2 | The oracle now decides each arm by a stated procedure. **Marker and non-green rendering:** every rendered item's governing-intent encoding equals the encoding POC-REQ-060's checked-in table gives Unknown, and none carries an encoding the table gives another state; the required behavior says the same, so "never as warranted, green or complete" is decided against that table. **Resolution statement:** the count's region, read as text alone, contains the reason name and its RFC2-24 route literally, and the word "warrant" in a statement that supplying it resolves an item. Oracle independence names the table as the expected value; the falsifier names each failure. The delta gains §"How each Trajectory arm is decided". The RFC8-23 and RFC8-24 covered rows now claim only what these checks observe. |
| 3 | Three RFC8-24 rows added, the clause text re-read at `814fbcc1` (`RFC-0008/accounting-reconciliation-and-release.md` lines 176–180): **covered**, the aggregation rule as far as the oracle observes it (one count; one reason, so the count is that reason's count; expansion to members within the rendered selection); **Unknown**, expansion beyond the selection and the full RFC6-17 disclosure that RFC2-24's rendering rule (`RFC-0002/rendering-vocabularies.md` lines 155–163) says any aggregate owes; **Unknown**, the claim-reasons-only limb, since Trajectory renders no RFC8-12 normalized state with absence values. The delta's RFC8-24 bullet quotes the continuation and lists each limb. |
| 4 | P-97 named in the delta (§"Overlap with sibling packages (P-97, P-84)"), the ledger (§"Sibling packages", the Baseline line and the tooling list) and the packet (§"Order against the other POC changes"). [Observed at `814fbcc1`] Before regeneration, the round-2 `spec.md.patch` applied at offset 54 and `GOVERNING-DEPENDENCIES.md.patch` failed at its `Source:` line, as the raw found. After regeneration, all four patches pass `git apply --check` against the signed bytes; the generator's `--check` over the applied tree reports "25 requirement(s), 88 distinct authorities"; the new `Source:` digest equals the `sha256sum` of the proposed `spec.md`. The P-84 exclusive pair is restated in all three files; P-84 is under repair in a separate lane and is not edited or re-tested here. The P-97 builder's own `--check` exits 1 at `814fbcc1` because its patches are now the signed bytes; it is not in the battery, and the ledger records this for the sign-off change. "Both packages" wording in the delta and ledger is re-derived per sibling. |
| 5 | The orphaned-work SHALL is removed from the required behavior. The Scope says the requirement makes no claim about orphaned work, and that RFC8-23's rule (the Contradiction governs) is left to the amendment that specifies orphaned-work detection. The RFC8-23 orphaned-work Unknown row's reason is rewritten to match. The raw's second suggested repair (move it to the Scope as a non-claim) was chosen. |
| 6 | The signed RFC2-24 reason-#10 row now lists `POC-REQ-003, POC-REQ-013, POC-REQ-014` and adds "Amendment: POC-REQ-014's oracle reads this exact reason, and its RFC2-24 route, on every served item's governing-intent claim". No new row; the delta's RFC2-24 bullet says so. |
| 7 | (a) The delta's reason section gains §"Where #10 fits weakly, stated": the #10 route will not resolve this Unknown by itself (only an owner act and an amendment can admit a source), and is still served with the reason, citing RFC2-24's own statements that RFC6-14 requires the reason "verbatim from this vocabulary" and that "every reason routes to its resolving action"; RFC8-24's #10 gloss names neither case, and the fit rests on RFC2-24's condition text. The RFC8-23 resolution is now stated as RFC8-23's own requirement; the delta no longer relies on RFC2-24's "fact of the render" sentence, and says why. (b) **RFC8-21 moves from Part B2 to Part B1**, one Unknown row ("no requirement walks the chain or renders any other link"); its signed B2 row is removed by the patch. The delta's §"RFC8-21 moves" quotes Part B2's own test ("neither renders, stores, transitions, queries, nor crosses") and says why: POC-REQ-014 renders the chain's first link. Totals re-derived by a Python sweep over the applied matrix: family RFC8 8 / 1 / 23; totals 77 / 28 / 219 = 324; Part A 122 rows over 77 clauses, 98 covered, 24 Unknown, 0 other; Part B1 29 rows over 28 clauses, all Unknown; Part A, B1 and B2 clause sets pairwise disjoint; Part A clause set equals the generated `contracts[]` set (77, symmetric difference empty). The spec reads 25 requirements and 26 scenarios. |
| 8 | Jargon: the packet's Q1 row 2 now says what PWB-REQ-005 and "PWB" are (the signed specification for how Polaris reads the Butlers project); Q3 says the same and replaces "the shared model" with "the one data model all three surfaces share". Stale sentences marked at the sentence, dated, old text kept: this record's head and §"Stopping rule applied"; the packet's Status; `ROUND-1-DISPOSITIONS.md` rows 5, 8, 9 and its first re-check bullet. Packet, delta and ledger carry the state "round-2 findings repaired once on 2026-10-14, unconfirmed pending round 3". Register row P-100 and the `docs/README.md` N10 row are updated. `REVIEW-BRIEF.md` gains a Round 3 section. The round-1 and round-2 raws are not edited. |
| 9 | No action. |

**The route (Q2).** P-97's answer extended Scope A to Three-Surface POC
specification amendments generally
(`../../../decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md`).
The packet's Q2 route sentences are marked at the sentence and the route
table is kept as it stood; Q2's sign / decline / revise table, Q1 and Q3 are
unchanged in substance.

**What was not changed.** The reason (#10), the field name `governedBy`, the
title counterexample, the no-new-column scope, the warrants block, and the
recommendations on Q1 and Q3. No owner question was added. P-84's package
is not edited. The direction record
`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md` is not
edited here; its sentence that none of the `REVISE` packets is repaired
again predates the owner's further direction and is left to the lead
session.
