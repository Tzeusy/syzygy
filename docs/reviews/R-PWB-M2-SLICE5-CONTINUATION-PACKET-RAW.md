# Review — PWB M2 slice 5 implementation-continuation packet
Reviewed commit: 268f1773ab70ace456847be0cca5bc960082ffb7
Artifact SHA-256: 806898d4bdfbde1915d9eb5fac245fc8b283a8d3c688d88a9efc2160045bf28f
Verdict: REVISE

Scope: all three package files at `268f1773` (parent `29e036f4`; the commit adds exactly these 3 files, 718 lines). The digest above comes from `git show 268f1773:<package>/OWNER-DECISION-PACKET.md | sha256sum`, run in this session. Coordinator note: the brief asks for bead `syzygy-dov.19`'s acceptance criteria to be pasted into it, and they were not. I read them myself with the read-only `bd show syzygy-dov.19`.

## Instrument decision

A plain owner direction is the right instrument. [Observed] It sits in the same family as `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`, the 2026-10-15 direction and both read-gate directions. The signed missing-currency packet itself calls the `.19` gate "the plain implementation-continuation direction" (`pwb-missing-currency-disclosure-scenario/OWNER-DECISION-PACKET.md:110`).

[Inferred] Taken as built, no item in B1–B10 changes:
- a signed or act-bound byte;
- an accepted contract;
- a registry value or semantics sentence;
- consent or policy.

B3 reads the act-bound `measuredFrom` sentence. It does not change it. B4's two reason precedences are choices the signed text leaves open, and they are labelled as the drafter's.

Two gaps below (R3 and R4) are decisions the built-behaviour section has to state. Neither needs an amendment, as long as the packet resolves them inside B4 and B5 rather than leaving them to the implementer. Option (ii) of O1 would cross an escalation trigger (R6), and the drafted reply does not authorize it.

## Findings

**R1 — Revise — criterion 9 (overlap) — [Observed]**
At `OWNER-DECISION-PACKET.md:345-352` the packet says the `syzygy-sin5` direction "would authorize the signed text" and that "If both are given, they cover the same slice". Both statements are false at PR #489's head `e990c27e`, and also at its first commit `9e63b856` (line 176).

- At `e990c27e`, `OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-20.md:206-231` ("Selected but not authorized here") says the record "does not authorize its implementation bead, M2 slice 5" and routes it to `syzygy-dov.19`.
- Lines 253-263 then grant something narrower. Item-depth relation claims and the opening-band aggregate's separate count may build the scenario's disclosure, and no bound is read.

The packet does not account for three consequences of that carve-out:
- **(a) The arm will have live members.** PWB-REQ-015's relation claims belong to the class `governing-intent-relation` (`spec.md:1992-1999`). That class has no row among the 13, so once item depth lands those claims are live members of the scenario's arm. The `[Inferred]` "the arm should have no live members" (`OWNER-DECISION-PACKET.md:277-280`; `IMPACT-LEDGER.md:154`) would then be wrong.
- **(b) Two count mechanisms.** B5's general count of unbounded members and the opening-band count #489 authorizes have to be one mechanism.
- **(c) The decline text goes stale.** The default description "no claim renders its disclosure route" (`OWNER-DECISION-PACKET.md:125-126`) stops being true if #489 is confirmed.

Repair: describe #489 at a named commit, say how B2, B5 and B10 compose with its two carve-outs, and revise both the inference and the decline text.

**R2 — Revise — criterion 4 (B4 against B5) — [Observed]**
`claimClassAssignment` gives rows to `claim:class:<class>` and to `claim:project-shape`, and calls both of them aggregates. B4 calls the judge "once per assigned claim" (`OWNER-DECISION-PACKET.md:161-166`), so both get a freshness value. B5 says an aggregate with members under the arm "carries no freshness value of its own" (`:192-198`). The packet does not say which rule wins when, for example, `claim:project-shape` has an unbounded member.

The scenario (`spec.md:1056-1062`) forbids two things: deriving a freshness value from the other members, and presenting the unbounded members as a freshness value. Read as "the aggregate has no freshness at all", B5 goes further than that. B5 also leaves out the scenario's requirement to present those members "only through the same outside-slot named disclosure, carrying that count and the stated reason". Repair: state the precedence for aggregates that are themselves claims, and restore the omitted limb.

**R3 — Revise — criteria 4, 5 and 10 (per-freshness counts do not exist) — [Observed]**
B5 relies on an aggregate's "per-freshness counts", and the RFC6-17.r1 row claims "label, tier and reason counts are unchanged" (`OWNER-DECISION-PACKET.md:192-195, 267`). PWB aggregates carry only `ReasonCounts { primary, secondary }` (`packages/three-surface-poc-core/src/project-shape-model.ts:176-179`).

My sweep found no per-label, per-tier or per-freshness aggregate counts in the POC code. It covered non-test TypeScript under `apps/three-surface-poc/src` and `packages/three-surface-poc-core/src`, with the patterns `composition|countBy|byLabel|byTier|freshnessCounts|perFreshness|byFreshness|freshness count|per-freshness|data-freshness-count`. The only hits were the fresh-checkout demo's reason `countBy` and cap1's `drawer.ts`.

So "membership = per-freshness counts + unbounded count" cannot hold unless slice 5 builds per-freshness counts, and B1–B10 do not say it does. Repair:
- state whether slice 5 builds per-freshness counts, and on which aggregates;
- correct the RFC6-17.r1 row;
- add `reasonCountsBlock` (`apps/three-surface-poc/src/polaris.ts:371-386`) and `ReasonCounts` to the ledger's consumer table.

**R4 — Revise — criterion 5 (RFC2-25 tier) — [Observed]**
Project-shape claims are Observed with tier `report-fact` (`project-shape-model.ts:228`). RFC2-25 places `report-fact` inside the Observed label only (`RFC-0002/rendering-vocabularies.md:168-178`).

B4's stale arm says "An Observed claim becomes Unknown with that primary reason" (`OWNER-DECISION-PACKET.md:173-174`) but never says what tier the claim then carries. The scenario says the claim "retains its tier" (`spec.md:1044`), and row RFC2-25.r1 is `covered:PWB-REQ-007` (`CONTRACT-COVERAGE-REPAIR-DELTA.md:50`). Slice 5 is the first change to move Observed claims to Unknown on currency grounds, so this is a contract consequence it newly reaches, and the packet does not route it. Repair: state the tier result for both arms — for example, untiered, which RFC2-25 allows at line 172 — label it as the drafter's composition, say how "retains its tier" is read, and add it to B10.

**R5 — Revise — criteria 8 and 11 (the reply points at bytes that will change) — [Observed]**
The question pulls in "The exact built behavior" by path (`OWNER-DECISION-PACKET.md:99-101`), and the reply says "as drafted" without naming a commit.

The planned record (`:372-378`) quotes the question, the reply and the bounds. It does not quote:
- B1–B10;
- the five-gap routing table;
- the O1 resolution;
- the reviewed commit.

The packet also says dispositions will be recorded "here" (`:385-388`), and the brief says any later edit retires the review (`REVIEW-BRIEF.md:31-33`). The file at that path will therefore not hold the bytes the owner answered.

The retention-posture precedent's record carries "the direction text as issued" (`POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DECISION-PACKET.md:589`). Repair:
- the record quotes B1–B10, the gap table and O1 verbatim;
- it names the reviewed commit and the retained raw as provenance (no digest ceremony needed, so bead criterion 5 still holds);
- dispositions go to a sibling record.

**R6 — Revise — criterion 6 (O1 framing) — [Observed]/[Inferred]**
[Inferred] Reading (i) is lawful. A blob has no committer instant, and the only commit the extraction reads through is the evaluated revision. That arguably makes (i) the more literal reading of "the exact Git object the declaration was extracted from".

The framing still leaves out three things:
- **Design evidence for (ii).** The funnel designed the field as "what the bound is measured from (the source's committer instant)" (`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md:650`), and its rejected trade-off (a) says "the classes genuinely differ" (`:703-704`). Both point toward (ii).
- **An unlabelled claim.** "many more claims render Unknown" (`OWNER-DECISION-PACKET.md:297`) carries no epistemic label, and nothing measured supports it.
- **(ii)'s authority cost.** (ii) reads per-source Git history beyond the evaluated revision. That is a new observation, which this packet's own Bounds (`:313-315`) and escalation trigger (`:360-361`) bar. So it needs more than "a revised packet" (`:301-303`).

Is this an owner question? Under the 2026-10-15 standing autonomy direction as applied (`OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15.md:124-130`), the lead may choose (i), because it reads nothing new. Showing it to the owner inside the one reply is acceptable. The reply does authorize (i) only (`:303`).

**N1 — Note — criterion 4 — [Inferred]**
If the registry act is not effective, the body-read gate refuses. B1 and B4 would then make `no-currency-bound-declared` the primary reason on the refused whole-shape claim, displacing the gate's reason (`project-shape-model.ts:388, 500, 701`). The scenario's WHEN arguably compels this. The packet should say so, say whether NOT_EVALUATED claims fall under the scenario, and have B10's "ineffective registry act" fixture check it.

**N2 — Note — criteria 1 and 13 — [Observed]**
- **Two gates, one reply.** The signed packet names the continuation and "a fresh implementation authorization" as separate gates (`pwb-missing-currency-disclosure-scenario/OWNER-DECISION-PACKET.md:109-112`). Answering both with one reply (`OWNER-DECISION-PACKET.md:64-66`) is a reading, so label it `[Inferred]`.
- **"Sign-off and act".** P-69 requires the Q7a scenario's "sign-off and act". The gate table (`:80`) should say that under Scope A (`OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md:30-34`; sign-off record `:25`) the version-tagged sign-off is that act.

**N3 — Note — bead criterion 2 — [Observed]**
The question describes the successor records (`OWNER-DECISION-PACKET.md:95-98`) but does not name them by record file or tag.

**N4 — Note — criterion 8 — [Observed]**
Two wording tensions:
- "in your own words" (`:7-8`) against "Any other wording … continues nothing" (`:109-110`);
- "The gate bead … closing is what would unblock" (`:382-383`) against "a bead closing … continues nothing" (`:9`).

**N5 — Note — criterion 10 and rule 9 — [Observed]**
The ledger's predicates reproduce exactly at `29e036f4`: 2,939 tracked files, the same 4 PNGs skipped, and figures of 8/12, 6/6, 22/55, 26/133, 97/177 and 13/20. But the continuation-form pattern misses the slash-run form. A broad sweep (`dov\.19\b|(?<![\w.])\.19\b(?!\.\d)`) finds 16 files, not 14. The two extra files are:
- `pwb-missing-currency-disclosure-scenario/REVIEW-BRIEF.md:88` (`.17/.18/.19`);
- `docs/pursuits/2026-09-22-vision-pursuit-harvest.json` (7 matches).

Neither changes what gets edited.

**N6 — Note — criterion 10 — [Observed]**
"four test files" with `currencyBounds: []` literals (`IMPACT-LEDGER.md:129`) is not right:
- three files carry the literal: `production-reobserve.test.ts:43`, `reobserve-session.test.ts:32` and `test-model-fixture.ts:218` (a fixture module, not a test file);
- `polaris-parity-sweep.test.ts:627` asserts `toEqual([])` instead.

Every other line range in the table matches.

**N7 — Note — criterion 5 — [Inferred]**
RFC2-9 says an effective act renders "with its exact provenance state rendered" (`snapshot-and-evaluation-core.md:230-231`; row RFC2-9.r1, `CONTRACT-COVERAGE-REPAIR-DELTA.md:47`). B6 carries the rows but not that state. The existing authority line (`polaris.ts:850-856`) probably satisfies it, and the packet should say so. RFC2-10.r1 (`:48`) is also left unmentioned: it was already `unknown-uncovered`, and slice 5 bears on it.

**N8 — Note — [Observed]**
At `OWNER-DECISION-PACKET.md:222-225`, "a breach stops the lane" does not say which limit counts: the 2,097,152-byte ceiling or the 1,650,000-byte working target. Also, B6 makes the machine answer bigger, but B10 does not measure it against `maxMachineResponseBytes`.

**N9 — Note — [Observed]**
B2's "a claim id that matches no family takes the scenario's arm" (`:147-149`) is a composition of `undeclaredClass`, which speaks of "a claim whose class has no row". Label it `[Inferred]`.

**Checked with no finding:**
- **Readback (criterion 1).** It reproduces (see the commands below), and `:74` says the ruling "prepared these gates; it performed no continuation".
- **Quotations (criterion 2).** Each of these matches its source: the escalation-trigger block, the CG-7e sentence, the three "still owed" quotes, P-69, the RFC6-14, RFC6-17, RFC7-16, RFC7-33 and RFC2-10 clauses, the five rows (confirmed as exactly the five the v1.0 tag turned `unknown-uncovered`), `measuredFrom`, "the evaluation itself is the currency", and "RFC2-24 states none".
- **Phrase scope.** The phrase continues only `syzygy-dov.2.2`, whose only open blocker is `.19`.
- **Exclusions (criterion 7).** All are kept, and B9 keeps `maxBriefingResponseBytes` and `governingBehaviorContract` unread. The `staleness.ts` claims match: five returns, three states, no freshness at 98-103.
- **Claim-id families.** There are six `claim:` families plus the probe, and the four `claim:fact:` subfamilies (`item`, `count`, `catalog-count`, `project-account`) all fall under `claimClassAssignment`.
- **Precedent (criterion 11).** No manifest, digest, recorder, record row or registration. Neither precedent appears in `check_governance.py`.
- **Hygiene (criterion 12).** No odd-backtick line over 712 non-fence lines, no 12-or-more-hex token, no observed-repository path in a code span, and all banners are explicit.
- **Authority boundary (criterion 13).** Nothing claims slice 5 may be built now.

## Commands run (at the frozen commit unless noted)

- `git show 268f1773:<packet> | sha256sum`
- Python readback over the three registry tags and the tree:
  - currency fields equal under sorted-key JSON;
  - each tag's bytes hash to a digest present in its own act record;
  - the tree's bytes are equal to the machine-ceiling tag's and hash to that act's record (the earlier tags differ only in `resourceLimits` and `governingBehaviorContract`);
  - the scenario heading occurs once at the v1.0 tag and once in the tree, and the block is byte-identical (1,747 characters);
  - the spec hash differs from the `governingBehaviorContract` pin.
- The ledger's six predicates over `git ls-tree -r -z 29e036f4`: 2,939 files, 4 decode skips. Cross-checked with `git grep -c -F dov.19` (8 files) and the broad continuation sweep (16 files).
- `git diff` of `CONTRACT-COVERAGE-REPAIR-DELTA.md` across the v1.0 tag: exactly the 5 rows changed.
- `git grep` for `claim:` prefixes, `currencyBounds`, committer-instant carriers and aggregate-count patterns over the implementation trees.
- `python3 scripts/check_governance.py`: 32 OK, 21 WARN, 0 FAIL out of 53; no line names the package.
- `python3 scripts/check_quotations.py`: exit 0; no line names the package. Its locator population is 33 and none of them is this package's, so it did not examine these quotations. My manual checks above stand in for it (rule 4).
- `bd show syzygy-dov.19` and `bd show syzygy-dov.2.2` (read-only).
- `git show e990c27e` and `git show 9e63b856` of the PR #489 record.

## Owner-only decision still preventing these bytes from being offered

None beyond the reply itself. Every Revise finding above is a packet repair the lead can make, followed by a fresh review round.

Verdict: REVISE
