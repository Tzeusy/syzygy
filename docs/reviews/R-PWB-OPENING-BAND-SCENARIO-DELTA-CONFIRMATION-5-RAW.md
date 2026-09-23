# Review — Polaris opening-band aggregate scenario package (round 6, fresh context)
Reviewed commit: 2c5745e90ff017cdc4484990e79243d1772eb265
Manifest SHA-256: 7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46
Verdict: REVISE

Reviewer: fresh-context session, no authoring context (CC-REV-1). Read-only
against a detached worktree at the reviewed commit; every mutation and every
patch composition ran in a copy under the session scratchpad, never in the
worktree. Inputs: the package in full (`SEMANTIC-DELTA.md` 975 lines,
`IMPACT-LEDGER.md` 313, `OWNER-DECISION-PACKET.md` 322, `REVIEW-BRIEF.md`
164, `PWB-OPENING-BAND-SCENARIO-MANIFEST.txt`, `proposed/spec.md.patch`,
`proposed/GOVERNING-DEPENDENCIES.md.patch`,
`scripts/build_pwb_opening_band_scenario.py`), the governing references the
brief names (the signed PWB specification, POC-REQ-032, RFC2-26 at its
defined clause, PWB-REQ-007/010/011/012/020), the ruling record rows P-68,
P-69, P-71, P-71-Q5, P-72, P-74, P-75, P-78 and its head, the two 2026-09-23
owner decisions, the M2/M3/M4 funnels, the semantic-delta template and the
normative-change workflow, `DIRECTIVE-REGISTER.md` for clause sites, and the
six retained raws for disposition checking only. The verdict is formed over
the bytes at `2c5745e`.

The verdict rests on one finding (31), in the same sentence round 5's finding
23 repaired: the repaired count is wrong by one under the standard the
sentence itself applies. Findings 32–35 are notes. Nothing in the patches,
the manifest or the builder needs to move.

---

## Findings

Numbering continues from 30.

**Finding 31 — revise. `SEMANTIC-DELTA.md` lines 646–652: "at the current
bytes two of the fourteen do not … The other twelve hold [Observed: … the
rest re-read at source in round 5]" — a third item does not hold under the
sentence's own standard, and the bracket claims a re-read the round-5 raw
does not record.** Criteria 9 and 11; rules 2, 4, 9 and 10.

- [Observed] The sentence excepts item 13 of
  `docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-RAW.md` solely because
  its `polaris.ts` "line range has moved" — the item's substance holds, as
  round 5 finding 23 said. That fixes the standard: a moved line pointer
  means the item does not hold at the current bytes.
- [Observed] Item 15 of the same raw (lines 132–143) cites
  `scripts/check_governance.py` anchors "`_act_subjects()` at line 1976,
  `ACT_DIGEST_COPY_FILES` at line 2173, and an existence-gated activation
  comment referencing `PWB-SCOPED-ATTRIBUTES-AMENDMENT-ACT.md` at line
  2300". At `59733d3` and at the round-1 disposition commit `3ee1b0b` those
  are lines 1976, 2173 and 2300 (`git show <commit>:scripts/check_governance.py`,
  fixed-string grep). At `2c5745e` they are lines **2022, 2236 and 2371**:
  the registration landed at `9d74185` (+139 lines in that file) and moved
  all three. The constants at 1518–1523 did not move. Item 15's substance
  (the lane B pattern exists) holds exactly as item 13's does.
- [Observed] So the count is three of fourteen, not two, and "The other
  twelve hold" is false for item 15 by the sentence's own test. This is the
  class round 5 returned REVISE on: a claim over a population of items, made
  without re-reading each item against the current bytes.
- [Observed] The evidence bracket attributes the re-read of "the rest" to
  round 5. The round-5 raw records no check of item 15's
  `check_governance.py` line pointers and does not record running `--diff`
  (item 5); its quotation-fidelity list and builder section cover items 2,
  3, 4, 6, 7, 8, 10, 11, 12, 14 and 16. I ran `--diff` this session: its
  output's sha256 equals that of the two patch files concatenated
  (`368ecc58…`, both), so item 5 holds — but not on round 5's evidence.
- [Observed] The sentence's other clauses hold: item 9 (0/0) is retracted at
  ledger line 96 (6 / 7); item 13's range is 951–960 at `2c5745e` (function
  body identical to the raw's block); "held at the round-1 disposition
  commit" is true — at `3ee1b0b` the ledger still said 0/0, `polaris.ts`
  was unchanged and the anchors sat at 1976/2173/2300.

Correct text: "at the current bytes three of the fourteen do not: item 9's
continuation-form figure (0/0) is retracted by round 2 finding 4 below (the
ledger now gives 6 files / 7 occurrences), item 13's `polaris.ts` line range
has moved (round 4 finding 21), and item 15's three `check_governance.py`
line pointers (1976, 2173, 2300) moved to 2022, 2236 and 2371 when the
registration landed at `9d74185`, its constants at 1518–1523 unmoved. The
other eleven hold [Observed: builder `--check`, `--selftest` and `--diff`
re-run this session cover items 3, 4 and 5; the rest re-read at source in
round 6]." Mark the superseded "two … twelve" in place, as the sentence
already does for its own predecessor.

**Finding 32 — note. `SEMANTIC-DELTA.md` lines 261–263: "the
`gapReasonCounts` function … — the projection for finding R-3 below" points
at the wrong section.** Criterion 11; rule 5. [Observed] R-3 (lines
348–360) cites `PocEpistemic`'s Unknown arm in `model.ts` and never names
`gapReasonCounts`; the section built on that projection is OQ-3 (lines
429–440), which is where the same two line ranges recur (432–433). The
pointer resolves to an existing section, so no sentence is false; the
Evidence bullet should read "for OQ-3 below". Unchanged since `59733d3`
(round-1 raw item 13 already paired the function with OQ-3).

**Finding 33 — note. The new PWB-REQ-020 two-readings passage
(`SEMANTIC-DELTA.md` lines 183–195, "What does NOT change" item 3) is a
surfaced tension left to the owner and its quotations are exact.**
Criteria 1 and 6 (template rule 6). [Observed] "every PWB-REQ-005 authority
state and PWB-REQ-022 judgment state and disclosure" is byte-exact at
`spec.md` 913–914, inside the Case at 912–914; "fall outside the enumerated
population entirely" is byte-exact at
`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` line 464, inside the
bracket at 462–465 that the funnel itself labels [Inferred]. The passage
names both readings, says which one this change lands under, states the
consequence of the other (a PWB-REQ-020 amendment outside this category),
and closes "it is named here, not settled: an owner who holds the narrower
reading should say so before any act". That is the form round 5 finding 27
asked for and template rule 6 permits — surfaced, not silently reconciled;
no OQ-6 is minted and the reason is stated. [Inferred] "this package takes
the wider one" is a description of what the drafted bytes presuppose, not a
ruling; the decision is expressly the owner's. No change needed; recorded
because the brief asked for this passage in particular.

**Finding 34 — note. `OWNER-DECISION-PACKET.md` line 9: "repaired
2026-09-21 and 2026-09-23".** Criterion 11. [Observed] The round-1
dispositions are one commit, `3ee1b0b`, authored 2026-09-22 01:11 +0800
(the round-1 raw's own commit `90eee3d` is 2026-09-21 23:04 +0800); the
later repairs are `76b4beb`, `7fd2db3` and `2c5745e`, all 2026-09-23. No
package commit is dated 2026-09-21 other than the draft `59733d3`. [Inferred] The 21st is the working date of an author who
committed after midnight; the sentence is imprecise, not false. If touched:
"repaired 2026-09-22 and 2026-09-23", or cite the commits.

**Finding 35 — note, outside the package. `SEMANTIC-DELTA.md` line 113
reads M4's Gate 5 table as giving "**Unavailable**" for slice 3 "under limb
1".** Criterion 1. [Observed] The eight-row table's fourth column is headed
`Limb 1` (`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` line 1303), so the
delta reports the header faithfully; the cell itself opens "**Unavailable.**
Limb 2 is unavailable as designed …" (line 1307). The inconsistency is the
funnel's, not the delta's, and the funnel is read-only to this package. No
change; recorded so a later reader does not count it against criterion 1.

---

## Round-5 repairs, each checked

| Round-5 finding | Repair site at `2c5745e` | Truthful? |
|---|---|---|
| 23 (revise) | delta 643–658 | Repaired as directed; the superseded wording is kept in place and dated to `9d74185`. **The repaired count is short by one — finding 31.** |
| 24 | delta 371–373 "lines 201–205, inside the clause defined at line 196" | [Observed] The quoted sentence sits at RFC-0002 `rendering-vocabularies.md` 201–205; the clause opens at 196; `DIRECTIVE-REGISTER.md` line 260 agrees. Exact. |
| 25 | delta 248–249 "820–913" | [Observed] `### Slice 3` at 820; slice 5's last text line 912; 913 blank; 914 is `### Slice 6`. Exact. |
| 26 | delta 251–253 "441–513 … 443–446 and 472–475" | [Observed] `### Slice 2` at 441, `### Slice 3` at 514; the currency-probe paragraph is 443–446 and "**The probe's own freshness.**" 472–475. Exact. |
| 27 | delta 183–195 | See finding 33: both readings named, quotations exact, decision left to the owner. |
| 28 | packet 3–7 | [Observed] The banner now ends "Only a dedicated amendment act of the owner naming the manifest digest below could give the proposed bytes effect." Every file head now names the act. |
| 29 | delta 385–386 "(paraphrased here, from `proposal.md` §Scope)" | [Observed] `proposal.md` §Scope is lines 86–91; "declared shape of the configured project" occurs nowhere in it (fixed-string, 0 hits) and the sentence is marked as a paraphrase. |
| 30 | no change | [Observed] The current source digest appears only in the declaration patch's `-` line; the ledger's "not reproduced anywhere in this package's prose" stands; `check_governance.py` at this commit: 32 OK, 20 WARN, 0 FAIL, CG-7e and CG-15 clean. |
| Round-count sentences (brief 10–29, packet 10–30 and 230–245, delta 584–589) | all three files | [Observed] Each names five rounds, the round-5 verdict word REVISE (copied exactly from the raw's line 4), "one revise finding and seven notes" (23 revise; 24–30 = seven notes), the round-5 raw's filename, and "a round 6"; packet step 1 "six repaired in prose and one needing no change" matches dispositions 24–29 repaired and 30 "no change". |

No round-5 repair introduced a new false sentence other than the count in
finding 31. The `git diff 7fd2db3 2c5745e` over the package touches only
the three prose files named in delta 928–931; `IMPACT-LEDGER.md`, both
patches, the manifest and the builder have the same blob ids at `59733d3`,
`9d74185`, `76b4beb`, `194f8cd`, `7fd2db3` and `2c5745e` [Observed,
`git ls-tree` at all six].

---

## Internal cross-reference sweep

**Method and denominator.** Python `re` over the four prose files
(`SEMANTIC-DELTA.md` 975 lines, `IMPACT-LEDGER.md` 313,
`OWNER-DECISION-PACKET.md` 322, `REVIEW-BRIEF.md` 164 — 1,774 lines)
extracting every `line N` / `lines N–M` pointer, backticked filename token,
seven-hex commit token in backticks, `finding N` reference, `round N`
word, `step N`, `item N`, `P-NN` row reference, `§…` section reference,
`OQ-N`, backticked bead id, `Gate N` and `QN` token. The extractor is
over-inclusive: **592 matches**. Every match was resolved against its
target at `2c5745e`; line pointers were read to confirm the quoted text
lands inside them.

| Category | Matches | Resolve | Do not resolve |
|---|---|---|---|
| Line pointers | 30 | 30 | 0 — every one read at source: spec 596–630, 448–450, 457–458, 906–910, 912–914, 470, 469 (sibling hunk `@@ -469,3`); M2 50, 130–131, 441–513, 443–446, 462–464, 472–475; M3 903–935, 905, 914; M4 119, 820–913, 827, 836, 1210, 1303/1307; RFC-0002 196–221, 201–205; register 260; POC spec 578–580, 589–590; lane B hunks 450–471, 473–483, 907; `polaris.ts` 951–960 at `194f8cd`/`2c5745e` and 922–931 at `a4a3451`; `model.ts` 41–42 |
| Filename tokens | 201 (64 distinct) | 60 distinct are tracked files or basenames at `2c5745e` | 4 distinct non-existent by design: `docs/evidence/*.json` and `docs/pursuits/2026-09-13-*.json` (globs, ledger 231–232), the future `PWB-OPENING-BAND-SCENARIO-ACT.md` (packet 289, "would" register; constant `PWB_OPENING_BAND_ACT` exists at `check_governance.py` 1552), the `-RAW.md` suffix pattern (brief 162) |
| Commit tokens | 43 (7 distinct) | 7 | 0 — `59733d3` 2026-09-21, `a4a3451` 2026-09-21 (merge-base of `origin/agent/gate-opening-band-scenario` [Observed]), `9d74185` 2026-09-22 "(#52)", `76b4beb`, `194f8cd` "(#57)", `dfb605c` (package byte-identical to `9d74185`: empty diff), `7fd2db3`, all 2026-09-23 |
| Finding numbers | 35 | 35 | 0 — round 1 = 1–3 notes; round 2 = 4–5 revise, 6–10 notes; B = A, B; round 3 = 11, 13, 14 revise, 12, 15–18 notes; round 4 = 20 revise, 19, 21, 22 notes; round 5 = 23 revise, 24–30 notes — each matched against its raw's heading and label |
| Round words / counts | 61 | 61 | 0 ("five reviews", "Done five times", "seven notes", "six repaired … one needing no change", "all 22 prior findings", "496 extracted pointers", "eight scratch mutations", "all four sibling spec patches" reproduce against the raws or my re-runs) |
| Step / item numbers | 4 / 5 | 4 / 4 | 1 item pointer resolves but its content claim is short by one (finding 31) |
| Row references (P-68…P-78, P-71-Q5, P-69 Q2(a), P-72 Q2, manifest row 8) | 71 | 71 | 0 — every quoted row sentence byte-exact at ruling-record lines 55–66; row 8 of the manifest is `contract-coverage-matrix/RFC-0007-0009.md` |
| Section references (§Review, §Scope, "What it means", Gate 5, "How to verify this page" at `PROJECT-STATUS.md` 227) | 23 | 23 | 0 |
| Bead ids | 20 (5 distinct) | 5 | 0 — `syzygy-dov.17/.18/.20/.21/.26` all exist with the roles the package gives them (`bd show`) |
| OQ / Gate / Q tokens | 53 / 2 / 44 | all | 0 (one section-pointer imprecision, finding 32, resolves to an existing section) |

"X carries / does not carry PWB-REQ-010" claims (4): `CAPABILITY-COVERAGE.md`
×1, `contract-coverage-matrix/RFC-0007-0009.md` ×4, neither class-3 JSON, no
class-4 file, `pwb-mutation-sweep-main.ts` run-form only — each re-swept at
`a4a3451` and exact. Total swept: **592**; not resolving: **0**; resolving
with a false content claim: **1** (finding 31); resolving to the wrong
section: **1** (finding 32).

**Quotation fidelity (criterion 1), every quotation read at source:**
PWB-REQ-010 in full (596–630), PWB-REQ-007's aggregate sentence (448–450)
and Observable (457–458), PWB-REQ-020 (906–910) and its Case (912–914),
the proposed scenario (equal to the patch's `+` lines and to post-apply
621–635), P-71's arm and "What it means" cell (record line 58), the record
head (14–16), P-71-Q5 (59), P-74 and P-78 closing sentences (64, 66), P-75
Q2 (63), M4 Q7 cell (119: "same region", "builds the band container and
owns its single ordering oracle", "own honest target", the block-order
reservation), M4 slice 3 (827–830, 836–838), M4 Gate 5 cells ("None
found.", "Unavailable", 41/55, both "None — the three sweeps …", "in place
… which an opening aggregate is not", the `home`/`surfaces` counts), M2
(443–446, 472–475, Q6 cell 50, success criterion 4 at 130–131, 462–465),
M3 (905–911, 914–916, 922–923), RFC2-26 (196–221 including "Rows are per
observable consequence, not per clause."), POC-REQ-032 (578–580, Observable
589–590), the template's change-class table (101–104), rules 2, 6 and 7
(111–128) and "I only touched X" (57), the owner's OQ answers (OWNER-VALUES
79–80, OPEN-QUESTIONS 33–35 and 52–59), `PocEpistemic`'s Unknown arm
(`model.ts` 41–42), `gapReasonCounts` at both commits. All byte-exact where
presented as quotations.

---

## Builder

Run from the worktree root at `2c5745e`:

- `--check` → exit 0: "PWB opening-band scenario manifest matches 11
  proposed behavior subjects (2 patched, 9 unchanged); the proposed
  declaration equals its regeneration and the spec patch composes with the
  lane B spec patch in both orders".
- `--selftest` → exit 0: "selftest: closed population, byte drift, path
  order, subject drift, patch corruption, lane B composition (both orders
  and a corrupted case), generated-declaration tampering and the
  declaration-patch collision all fail closed" — criterion 10's nine
  predicates.
- `--diff` → exit 0; its bytes hash equal to the two patch files
  concatenated [Observed].
- Manifest semantics by hand: `sha256sum -c` over the eleven rows against
  the tree passes nine and fails exactly `spec.md` and
  `GOVERNING-DEPENDENCIES.md`; after `git apply` of both patches in a
  scratch copy those two hash to `9a44bdb6…` and `86b1b49f…`, the manifest's
  rows 11 and 5 [Observed]. The proposed scenario sits at post-apply
  621–635, after the WhatsApp scenario (615–619) and before the `warrants`
  fence (637). Its heading carries none of PWB-REQ-012's six prohibited
  words (line 687 of the spec).
- `sha256sum` of the manifest → the value on line 3 above, equal to the
  packet's copy (line 43) and to every prior raw's line 3.

**Mutations (rule 6, criterion 10), nine, each in a scratch copy of
`scripts/`, `openspec/` and `.syzygy/`, baseline `--check` passing before
and after each, failure text read:**

| # | Mutation | Failure text |
|---|---|---|
| M1 | append a line to unpatched `design.md` | "manifest differs from exact regeneration over the proposed bytes" |
| M2 | flip the last hex char of the manifest's `spec.md` row | "manifest differs from exact regeneration over the proposed bytes" |
| M3 | swap manifest rows 8 and 9 | "manifest path population or order differs" |
| M4 | patch text "exactly one such aggregate" → "at most one such aggregate" | "proposed GOVERNING-DEPENDENCIES.md differs from regeneration over the proposed spec bytes" + "manifest differs …" |
| M5 | declaration patch `+` line 96 → 97 | same two lines as M4 |
| M6 | remove lane B's `spec.md.patch` | "missing lane B spec patch: …pwb-scoped-attributes-amendment/proposed/spec.md.patch" |
| M8 | drift spec line 618 (the patch's context line) | "spec.md.patch does not apply to the base bytes: error: patch failed: …spec.md:618" |
| M9 | add a twelfth file `EXTRA.md` to the change directory | **passes** — confirms ledger lines 148–151 (a twelfth file is outside the bound subject and is not hashed) |

All fail closed with distinct, correct text except M9, which is the
documented non-failure.

**Composition, independent of the builder:** this package's
`spec.md.patch` with each of the four sibling `proposed/spec.md.patch`
files (scoped-attributes, missing-currency-disclosure, machine-view,
exact-source-render-mode) via `git apply` on a clean copy of the current
spec, both orders: every pair applies and each pair yields one digest
regardless of order [Observed]. The two `GOVERNING-DEPENDENCIES.md`
patches collide ("patch failed: …GOVERNING-DEPENDENCIES.md:8" after either
is applied), as delta 611–616 and ledger 295–299 say.

**Governance battery:** `python3 scripts/check_governance.py` → "32 OK, 20
WARN, 0 FAIL (52 checks)". CG-7d lists "SIGN OFF PWB OPENING-BAND SCENARIO
— 0 quotation(s), 0 finding(s), 0 performed digest(s)" and the packet as a
registered copy "1 current, 0 historical valid". `PWB_SUCCESSOR_CHAIN`
(`check_governance.py` 1631–1638) has three links and no opening-band link,
matching the withheld-link note at 1537–1541 and the packet's "fourth link"
sentence. The battery lines sit at `PROJECT-STATUS.md` 256–257 and the CI
steps at `governance-docs.yml` 124–128, all added at `9d74185`.

---

## Impact ledger re-derivation

**Method.** Python `re` over every blob of `git ls-tree -r -z a4a3451`,
decoded as UTF-8, undecodable blobs skipped; the five patterns as the ledger
states them, including its regex
`PWB-REQ-\d{3}(?:(?:/|,\s|\s)\d{3})*?(?:/|,\s|\s)010\b`. Second method:
`git grep -l -F` (and `-P` for the regex) at `a4a3451`; `git grep -o` for
occurrences. Denominator: **1,334** tracked blobs [Observed].

| Figure | Ledger | Re-derived (`re`) | Second method |
|---|---|---|---|
| tracked files | 1,334 | 1,334 | — |
| undecodable | 4, the four PNGs | 4, same paths | — |
| NUL-carrying | 6 (four PNGs + two `.ts`) | 6, same paths (over 1,334; the ledger states 1,343) | — |
| `PWB-REQ-010` | 36 / 110 | 36 / 110 | 36 / 110 |
| continuation forms | 6 / 7 | 6 / 7 | 6 |
| spec path | 51 / 113 | 51 / 113 | 51 |
| declaration path | 9 / 13 | 9 / 13 | 9 |
| current source digest | 13 / 13 | 13 / 13 | 13 |
| run-only adds | 5, named | the same 5 | — |
| both forms | `pwb-p4-2-mutation-sweep-2026-09-04.json` | same | — |
| citer union | 41 | 41 | — |

**Class 2 (9 files):** the nine unpatched manifest rows equal current bytes
(`sha256sum -c`). Literal carriers among the eleven rows at `a4a3451`:
`CAPABILITY-COVERAGE.md` ×1, `contract-coverage-matrix/RFC-0007-0009.md`
×4, plus the two class-1 files (`GOVERNING-DEPENDENCIES.md` ×9, `spec.md`
×1); no other row [Observed]. M9 above confirms the twelfth-file sentence.

**Class 3 (2 files):** both JSON declarations are among the 13 digest
citers and neither carries `PWB-REQ-010` [Observed]; labelled Observed for
the pins and Inferred for the repair's home, as criterion 9 requires.

**Class 4:** no `decisions/` act record and no `*-MANIFEST.txt` is in the
41-citer union, so no history file carries the identifier [Observed].

**Class 5 (39):** 41 less the two class-1 files = 39, placed in exactly one
kind each from my own union list: implementation and tests 6 (`polaris.ts`,
three `polaris*.test.ts`, `pwb-mutation-sweep.ts`,
`pwb-mutation-sweep-main.ts`), generated coverage views 4, design packets 2
(M3, M4), retained raws 11, dated evidence records 12 (ten
`docs/evidence/*.json` + two `docs/pursuits/2026-09-13-*.json`), plan +
dated review 2, pending register 1, other spec's design note 1 = **39**.
Every path the ledger names is in my list and no citer is unplaced. One raw
(`R-PWB-LIVE-EXACT-HEAD-ENGINEERING-RAW.md`) and three evidence records
reach the class only through the run form, as stated.

**Branch population:** `59733d3` has 1,342 tracked files (1,334 + eight);
`3ee1b0b` (branch tip) has 1,343 [Observed], matching ledger 34–35.

All figures reproduce by two methods.

---

## Disposition check — findings 1–30

| Finding | Round | Label | Disposition in `SEMANTIC-DELTA.md` §Review | Checked at `2c5745e` |
|---|---|---|---|---|
| 1 | 1 | note | 662–670 repaired | ledger 31–51 enumerates 4 skipped and 6 NUL; both reproduce |
| 2 | 1 | note | 671–677 wording promoted, OQ-2 open | delta 418–427, packet 152–159; OQ-2 answered (A) 2026-09-23, no byte moved |
| 3 | 1 | note | 678–683 withdrawn | all three files cite the rows, "Q4" marked withdrawn |
| 4 | 2 | revise | 714–721 repaired | ledger regex, 6/7, 41, 39 all reproduce |
| 5 | 2 | revise | 722–728 repaired | ledger 145–153; M9 confirms |
| 6 | 2 | note | 729–736, withdrawn in round 3 | delta 465–471 attributes to M2 line 50, M4 119 quotes it; exact |
| 7 | 2 | note | 737–741 marked at the sentence | ledger 255–261, packet 273–277 dated notes |
| 8 | 2 | note | 742–744 repaired | delta 640–643 names the brief; `3ee1b0b` touched four files |
| 9 | 2 | note | 745–749 repaired | P-74/P-78 sentences exact at record 64/66 in all three files, no emphasis |
| 10 | 2 | note | 750–751 repaired | packet 246–247 "may change" |
| A | B | non-blocking | 762–764 | same as 9 |
| B | B | editorial | 764 no change | — |
| 11 | 3 | revise | 809–813 repaired | as 6 |
| 12 | 3 | note | 814–816 repaired | no `**is**`/`**are**` in quotations |
| 13 | 3 | revise | 817–825 repaired | class 5 partitions to 39 (above) |
| 14 | 3 | revise | 826–829 repaired | packet 10–30 names every round |
| 15 | 3 | note | 830–832 repaired | packet 259–261 |
| 16 | 3 | note | 833–837 marked | ledger 301–313 "at the baseline commit", sibling named, composition re-derived (above) |
| 17 | 3 | note | 838–841 repaired | ledger 11–14 |
| 18 | 3 | note | 842–843 repaired | delta 632 "Round 1 verdict:" |
| 19 | 4 | note | 876–880 repaired | delta 584–589 names five rounds |
| 20 | 4 | revise | 881–892 repaired | ledger 199–204, 221–227; ×1 and ×4 re-swept |
| 21 | 4 | note | 893–896 repaired | delta 262, 432–433 both ranges verified |
| 22 | 4 | note | 897–900 repaired | 472 and 836 verified |
| 23 | 5 | revise | 936–943 repaired | **count short by one — finding 31** |
| 24 | 5 | note | 944–946 repaired | verified |
| 25 | 5 | note | 947–948 repaired | verified |
| 26 | 5 | note | 949–951 repaired | verified |
| 27 | 5 | note | 952–959 repaired | finding 33 |
| 28 | 5 | note | 960–963 repaired | verified |
| 29 | 5 | note | 964–966 repaired | verified |
| 30 | 5 | note | 967–969 no change | verified |

Every finding 1–30 carries a numbered disposition whose stated repair is
present at the cited site; disposition 23's repair is present but its
figure is wrong (finding 31). No disposition claims more than the bytes
show, with that one exception.

---

## Per-criterion summary

| # | Criterion | Result |
|---|---|---|
| 1 | Quotation fidelity | **Pass** — every quotation byte-exact at its cited lines, the three round-5 range repairs exact; one paraphrase now marked (29); finding 35 is the source's own inconsistency |
| 2 | Change class | **Pass** — Normative under the template table (101–104, rule 2 at 111–112): a renderer with two opening aggregates, a tuple-less one, or a hoisted member complied before and does not now; argued from obligation |
| 3 | Scenario form | **Pass** — WHEN/THEN/AND at post-apply 621–635, after the existing scenario, before `warrants`; each clause falsifiable on an inspectable rendering or machine answer; no clause states a value; heading clear of PWB-REQ-012's words |
| 4 | One category, no overlap | **Pass** — the patch touches 618–621 only; lane B's hunks 450–483 and 907+; the P-69 Q7a sibling inserts at 469; the P-75 Q1 package is against the other specification; all four sibling compositions verified in both orders |
| 5 | Reconciliation performed | **Pass** — three parties from M4 Q7, each quoted from its own packet at verified lines, R-1/R-2/R-3 each tied to a scenario clause; P-75 Q2 exact at record 63 |
| 6 | Contradictions surfaced, not settled | **Pass** — OQ-1 to OQ-5 genuine, easier reading named and not taken, each the owner's (now answered by plain direction, no byte moved); the PWB-REQ-020 reading round 5 flagged is now surfaced at item 3 in the same form (finding 33) |
| 7 | RFC2-26 | **Pass** — both halves hold against 196–221: limb 1 for slice 3 only, conditioned on OQ-2 (answered (A)); slices 4–5 unmapped on M4's own table (1308–1309) and routed to `syzygy-dov.26` |
| 8 | What does not change | **Pass** — all eight items true against the patches: no requirement minted, `warrants` byte-identical, 17/96 unchanged, no implementation file, no observed-repository write (P-71-Q5 exact at record 59) |
| 9 | Impact ledger | **Pass in the ledger; fail in the delta's §Review sentence (finding 31)** — every ledger figure reproduces by two methods; class-3 labelling correct; the false count is at delta 646–652 |
| 10 | Manifest and builder | **Pass** — eleven rows, two post-apply and nine current, verified by hand; nine predicates named; eight mutations fail closed, the ninth passes as documented |
| 11 | Governance hygiene | **Pass with notes 32, 34** — no performed act argument or truncated signed digest in prose; act records by path; no observed-repository path in a code span (swept the four files; CG-1b clean); every head names the act (28 repaired); claims labelled; nothing labelled accepted; signed change directory untouched |
| 12 | Scope of authority | **Pass** — nothing performs an act or schedules work; the scenario is conditional ("WHEN … renders an aggregate"), so a conforming implementation may render no opening aggregate; packet 65–68 says so |

---

## Verdict rationale

**REVISE.** One sentence in the package is false at the reviewed commit:
`SEMANTIC-DELTA.md` lines 646–652's repaired count that "two of the
fourteen" round-1 machine items do not hold and "the other twelve hold",
when item 15's three `check_governance.py` line pointers moved at
`9d74185` in exactly the way item 13's `polaris.ts` range did — the very
test the sentence uses to except item 13 — and the evidence bracket
attributes to round 5 a re-read the round-5 raw does not record for that
item. It is the class rounds 2–5 returned REVISE on, in the same paragraph
round 5 repaired, and the repair is one clause. Everything else holds: the
bound bytes are unchanged across six commits, the builder and nine
mutations behave, every ledger figure reproduces by two methods, every
quotation is exact, the round-5 line-range repairs are exact, the new
PWB-REQ-020 passage is a surfaced tension left to the owner, and findings
32–35 are notes. A round 7 over the repaired bytes may be confined to that
paragraph and any text the repair touches.
