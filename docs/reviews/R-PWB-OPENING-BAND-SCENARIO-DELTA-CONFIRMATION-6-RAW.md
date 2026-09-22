# Review — Polaris opening-band aggregate scenario package (round 7, fresh context)
Reviewed commit: d3d5d9dc5cbeff46fdc2782842442ce48c076c5b
Manifest SHA-256: 7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46
Verdict: REVISE

Reviewer: fresh-context session, no authoring context (CC-REV-1). Read-only
against a detached worktree at the reviewed commit (`git status --porcelain`
empty); every mutation and every patch composition ran in a copy under the
session scratchpad, never in the worktree. Inputs: the package in full
(`SEMANTIC-DELTA.md` 1,044 lines, `IMPACT-LEDGER.md` 313,
`OWNER-DECISION-PACKET.md` 329, `REVIEW-BRIEF.md` 167,
`PWB-OPENING-BAND-SCENARIO-MANIFEST.txt`, `proposed/spec.md.patch`,
`proposed/GOVERNING-DEPENDENCIES.md.patch`,
`scripts/build_pwb_opening_band_scenario.py`), the governing references the
brief names (the signed PWB specification, POC-REQ-032, RFC2-26 at its
defined clause, PWB-REQ-007/010/011/012/020), the ruling record's head and
rows P-68…P-78 plus its cross-cutting section, the two 2026-09-23 owner
decisions, the M2/M3/M4 funnels, the semantic-delta template and the
normative-change workflow, `DIRECTIVE-REGISTER.md` for clause sites, and the
seven retained raws for disposition checking only. The manifest digest on
line 3 was computed with `sha256sum`, never transcribed (rule 3), and equals
the packet's copy (packet line 47) and every prior raw's line 3.

The verdict rests on one finding (36), inside the sentence round 6's finding
31 repaired: the repair states, for the third excepted item, a commit and an
attribution that the file history contradicts. Findings 37–39 are notes.
Nothing in the patches, the manifest or the builder needs to move; all three
have the same blob ids at every reviewed commit from `59733d3` to `d3d5d9d`
[Observed, `git ls-tree` at eight commits].

---

## Findings

Numbering continues from 35.

**Finding 36 — revise. `SEMANTIC-DELTA.md` lines 652–656: "item 15's three
`check_governance.py` line pointers (1976, 2173 and 2300) moved to 2022,
2236 and 2371 when the lane B registration landed at `9d74185`" — false on
two counts.** Criteria 9 and 11; rules 4 and 10.

- [Observed] `git show 9d74185:scripts/check_governance.py` (8,075 lines,
  +139 over the 7,936 at `59733d3` and `3ee1b0b`) carries `def
  _act_subjects()` at line **2010**, `ACT_DIGEST_COPY_FILES = {` at **2222**
  and the activation comment naming `PWB-SCOPED-ATTRIBUTES-AMENDMENT-ACT.md`
  at **2355** — not 2022, 2236 and 2371. Those three values first appear at
  `807cecf` (2026-09-22 22:55 +0800, "draft missing-currency disclosure
  amendment [syzygy-dov.20]", +26 lines, 8,101 total), the only other
  commit touching that file between `59733d3` and `d3d5d9d`, and they hold
  at `2c5745e` and `d3d5d9d`. The sentence therefore names the wrong commit
  for the figures it gives.
- [Observed] What landed at `9d74185` was not "the lane B registration".
  Lane B's constants `PWB_SCOPED_AMENDMENT_LABEL/_DIR/_SUBJECT/_ACT` sit at
  lines 1518–1523 at `59733d3`, before this branch's own draft; the round-1
  raw's item 15 cites them as already present. `9d74185` (the merge of PR
  #52, "draft the five P-68…P-83 owner-gate packages") added **this
  package's** registration — `PWB_OPENING_BAND_LABEL/_DIR/_SUBJECT/_ACT` at
  1548–1552 exist at `9d74185` and not at `59733d3` [fixed-string grep,
  both commits] — which is exactly what `IMPACT-LEDGER.md` lines 255–258
  and `OWNER-DECISION-PACKET.md` lines 280–284 say about that commit. The
  delta's own sentence contradicts the ledger's.
- [Observed] The remaining clauses hold: 1976, 2173 and 2300 are exact at
  `59733d3` and `3ee1b0b`; 2022, 2236 and 2371 are exact at `d3d5d9d`; the
  constants at 1518–1523 did not move at any of the five commits read;
  item 15's substance (the lane B pattern exists) holds.
- [Inferred] The round-6 raw's own correct-text proposal (its lines 71–79)
  wrote "when the registration landed at `9d74185`" having checked only
  `59733d3`, `3ee1b0b` and `2c5745e`; the repair copied that and added
  "lane B". The first error is inherited, the second is new to this round.

This is the class rounds 5 and 6 returned REVISE on — a per-commit pointer
claim in the round-1 section, made without reading the file at the commit
named — and it is the paragraph a reader is told to trust for which round-1
items still hold. Correct text: "item 15's three `check_governance.py`
line pointers (1976, 2173 and 2300) moved to 2010, 2222 and 2355 when this
package's own registration landed at `9d74185` and again to 2022, 2236 and
2371 at `807cecf`, the missing-currency package's registration; the lane B
constants at 1518–1523 never moved (round 6 finding 31)". Mark the
superseded clause in place, as the sentence already does for its two
predecessors.

**Finding 37 — note. `SEMANTIC-DELTA.md` line 1006: the round-6 summary says
the reviewer "exercised nine scratch mutations"; the round-6 raw's own table
enumerates eight.** Criterion 9; rule 2. [Observed]
`docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-CONFIRMATION-5-RAW.md` lines
239–248 tabulate M1, M2, M3, M4, M5, M6, M8 and M9 — eight rows, no M7 —
while its line 235 says "nine" and its criterion-10 row says "eight
mutations fail closed, the ninth passes as documented" (which would need
eight failing rows plus M9; the table has seven failing). The raw is
uneditable (CC-REV-6) and internally inconsistent; the delta restates the
raw's word rather than its table. Not false as a report of what the raw
says; the count word does not derive from an enumerated population. If
touched: "exercised the nine scratch mutations its raw counts (eight
tabulated; its numbering skips M7)".

**Finding 38 — note. `SEMANTIC-DELTA.md` lines 659–660: "items 6, 7, 8, 10,
14 and 16 were re-read at source by the round-5 reviewer" — for item 14 the
round-5 raw records part of the item.** Criterion 9; rules 4 and 9.
[Observed] Round-1 item 14 makes three claims: lane B's hunk headers, the
PWB-REQ-007 scenario heading at spec line 470, and "the next requirement at
line 487". The round-5 raw (lines 189–191) records the hunks and line 470;
the string `487` occurs nowhere in it (fixed-string grep, 0 hits). Items 6,
7, 8, 10 and 16 are each recorded there (its lines 212–218, M2, 243–249, the
"undecodable 4" row, 175–195). Item 14 holds at `d3d5d9d` on my own
re-read: the spec blob is unchanged since `59733d3`, `### Requirement:
PWB-REQ-004` is at line 487, `#### Scenario: Missing current evidence
remains explicit Unknown` at 470, and lane B's hunks are `@@ -450,22`,
`@@ -473,11`, `@@ -907,23`. The sentence's conclusion is right; its
evidence attribution is one sub-claim short.

**Finding 39 — note. `OWNER-DECISION-PACKET.md` lines 298–303 recommend the
successor-chain position "after lane B, matching P-68's ordering … the owner
may say otherwise [Inferred]" without noting that the owner has said
otherwise.** Criteria 11 and 12. [Observed]
`.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`
§6 (lines 110–129) records the owner's answer "Readiness order, lane B last
(Recommended)", reads it as `.21` → `.30` → `.22` → lane B, and closes "The
`.21` packet's recommendation to chain after lane B is superseded by this
answer, not edited." The packet cites that same record at step 2 (line 256)
for OQ-1 and OQ-2 only. `SEMANTIC-DELTA.md` lines 607–609 ("either may be
adopted first") and `IMPACT-LEDGER.md` lines 290–291 stay true — the
composition claim is order-independent — and the sentence is a labelled
recommendation, so nothing is false; but the owner-facing packet does not
tell its reader the order is already fixed by direction. If touched: a dated
mark at the sentence citing §6 of that record.

No other finding. The round-6 repairs of findings 32 and 34, and the
round-count sentences in all three files, are exact (table below).

---

## The thirteen round-1 items, each re-checked at `d3d5d9d`

**Population, derived from the raw.** `docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-RAW.md`
"What I ran" numbers its items 1–16 (lines 21–152). Items 2–10 are nine and
13–16 are four: **thirteen**, as the repaired sentence says [Observed]. Items
1, 11 and 12 are outside the sentence's population by its own definition
(commit identity, the ruling-record read, the Gate 5 read). The standard the
sentence applies, fixed by its own treatment of item 13: a moved line
pointer means the item does not hold "as written".

| Item | Claim in the raw | At `d3d5d9d` | Holds as written? | Evidence this session |
|---|---|---|---|---|
| 2 | manifest sha256 = the value on line 3 | equal | yes | `sha256sum`, computed |
| 3 | `--check` exit 0 with the quoted success line | identical text, exit 0 | yes | run from the worktree root |
| 4 | `--selftest` exit 0 naming nine predicates | identical text, exit 0 | yes | run from the worktree root |
| 5 | `--diff` equals the two patch files | byte-equal to the declaration patch followed by the spec patch (`sha256` of both concatenations equal; `diff` empty) | yes | run and compared |
| 6 | both patches apply; scenario sits after the WhatsApp scenario and before `warrants` | post-apply: WhatsApp at 615, new scenario 621–635, `warrants` fence 637; post-apply `spec.md` hashes to manifest row 11 | yes | `git apply` in a scratch copy |
| 7 | flipping one hex of the manifest's `spec.md` row makes `--check` fail with "manifest differs from exact regeneration over the proposed bytes" | same text, exit 1; restored → pass | yes | mutation M13 below |
| 8 | lane B AB and BA compose byte-identically | one digest both orders | yes | `git apply`, independent of the builder |
| 9 | five figures reproduce, continuation form **0/0** | 36/110, 51/113, 9/13, 13/13 reproduce; continuation form is **6/7** | **no** — retracted at ledger line 96 (round 2 finding 4) | re-derived, two methods |
| 10 | 4 undecodable files, the four PNGs | same 4 paths | yes | re-derived over 1,334 blobs |
| 13 | `gapReasonCounts` at `polaris.ts` lines 920–931 | body identical to the raw's block; sits at 951–960 | **no** — pointer moved (round 4 finding 21); substance holds | read at `a4a3451` (922–931), `194f8cd` and `d3d5d9d` (951–960) |
| 14 | lane B hunks `@@ -450,22`, `@@ -473,11`, `@@ -907,23`; scenario heading at 470; next requirement at 487 | all exact | yes | lane B patch and spec blobs unchanged since `59733d3` |
| 15 | `_act_subjects()` 1976, `ACT_DIGEST_COPY_FILES` 2173, activation comment 2300; constants 1518–1523 | 2022, 2236, 2371; constants unmoved | **no** — three pointers moved (round 6 finding 31); substance holds; **the repaired sentence misdates the move (finding 36)** | five commits read |
| 16 | quotation spot checks exact at spec 596–630, 444–458, 906–910; RFC-0002 196; register 260; M4 119 and 820–918; M2 441–480; M3 903–935; POC spec 578 | every quoted passage exact; every named source file has the same blob id as at `59733d3` (M2, M3, M4, RFC-0002, `DIRECTIVE-REGISTER.md`, both specs, the ruling record) | yes | each range read at source; blob ids compared |

Three do not hold as written (9, 13, 15); ten hold. Both counts confirm the
repaired sentence. The sentence's evidence bracket is accurate for items 2,
3, 4, 5, 6, 7, 8, 10 and 16 and one sub-claim short for item 14 (finding
38). Its clause on item 15's history is false (finding 36).

---

## Round-6 repairs, each checked

| Round-6 finding | Repair site at `d3d5d9d` | Truthful? |
|---|---|---|
| 31 (revise) | delta 648–668 | Population thirteen, three excepted, ten held — all confirmed above. **The item-15 clause names the wrong commit and the wrong registration — finding 36.** Superseded wordings kept marked in place. |
| 32 | delta 261–264 "the projection for OQ-3 below (an earlier bullet said 'finding R-3'; round 6 finding 32)" | [Observed] OQ-3 at 430–441 is the section built on `gapReasonCounts`; exact. |
| 33 | no change | [Observed] delta 180–195 unchanged from `2c5745e` (diff empty over those lines); still a surfaced tension with exact quotations, decision left to the owner. |
| 34 | packet 9–11 "repaired 2026-09-22 and 2026-09-23 — an earlier line said 2026-09-21 … round 6 finding 34" | [Observed] `3ee1b0b` is 2026-09-22 01:11:11 +0800; `76b4beb`, `7fd2db3`, `2c5745e`, `fe1a289` are 2026-09-23. Exact. |
| 35 | no change | [Observed] M4 line 1303 heads the column `Limb 1`; the slice-3 cell (1307) opens "**Unavailable.** Limb 2 is unavailable as designed". The delta's line 113 reports the header faithfully. |
| Round-count sentences (brief 10–31, packet 12–34 and 234–252, delta 583–591 and 987–1011) | all three files | [Observed] Each names six rounds, the round-6 verdict word REVISE (copied from the raw's line 4), "one revise finding and four notes" (31 revise; 32–35 four notes), the round-6 raw's filename, and "a round 7"; packet step 1 "two repaired in prose and two needing no change" matches dispositions 32 and 34 repaired, 33 and 35 "no change". |

`git diff 2c5745e d3d5d9d` over the package touches only
`SEMANTIC-DELTA.md`, `OWNER-DECISION-PACKET.md` and `REVIEW-BRIEF.md`
[Observed]; `IMPACT-LEDGER.md`, both patches, the manifest and the builder
have the same blob ids at `59733d3`, `3ee1b0b`, `9d74185`, `76b4beb`,
`194f8cd`, `7fd2db3`, `2c5745e` and `d3d5d9d`. The round-6 repair
introduced one new false clause (finding 36) and no other.

---

## Internal cross-reference sweep

**Method and denominator.** Python `re` over the four prose files
(`SEMANTIC-DELTA.md` 1,044 lines, `IMPACT-LEDGER.md` 313,
`OWNER-DECISION-PACKET.md` 329, `REVIEW-BRIEF.md` 167 — **1,853 lines**)
extracting every `line N` / `lines N–M` pointer, backticked filename or path
token, seven-hex commit token in backticks, `finding N`, `round N`, `OQ-N`,
`P-NN` row reference, backticked bead id, `step N`, `item N`, number word
(one…seventeen, thirty-nine, forty-one, ninety-six), `§` section reference,
and `Gate N` / `QN` token. The extractor is over-inclusive: **1,026
matches**. Every match was resolved against its target at `d3d5d9d`; line
pointers were read to confirm the quoted text lands inside them.

| Category | Matches | Resolve | Do not resolve |
|---|---|---|---|
| Line pointers | 30 | 30 | 0 — every one read at source: spec 596–630, 448–450, 457–458, 906–910, 912–914, 470, 469; M2 50, 441–513, 443 (443–446), 462–464, 472 (472–475); M3 903–935, 905, 914; M4 119, 827, 836 (836–839); RFC-0002 196–221, 201–205; register 260; POC spec 578–580; lane B 450–471, 473–483; `polaris.ts` 951–960 at `194f8cd` and 922–931 at `a4a3451`. Bare pointers outside the regex also read: `check_governance.py` 1976/2173/2300, 2022/2236/2371, 1518–1523 (finding 36 on the commit they are tied to); M4 820–913 and 1210; `model.ts` `PocEpistemic` Unknown arm at 41–42 (carries `reason` only, as R-3 says) |
| Filename / path tokens | 235 | all tracked files, tracked basenames, or by-design non-files | 0 — the by-design set: the directory tokens `proposed/`, `decisions/`, `openspec/**`, `pwb-missing-currency-disclosure-scenario/` (exists), the branch `agent/gate-opening-band-scenario` (exists on `origin`), identifier runs and the ledger's regex quoted as literals, one command line, the `docs/evidence/*.json` and `docs/pursuits/2026-09-13-*.json` globs, the future `PWB-OPENING-BAND-SCENARIO-ACT.md` (constant `PWB_OPENING_BAND_ACT` at `check_governance.py` 1552), the `-RAW.md` suffix |
| Commit tokens | 51 (8 distinct) | 8 | 0 — `59733d3` 2026-09-21 22:47, `a4a3451` 2026-09-21 22:02 (merge-base of `origin/agent/gate-opening-band-scenario`), `9d74185` 2026-09-22 08:00 "(#52)", `dfb605c` 2026-09-23 01:29 (package byte-identical to `9d74185`, empty diff), `76b4beb` 01:40, `194f8cd` 02:39 "(#57)", `7fd2db3` 03:03, `2c5745e` 03:25 — all resolve; **one commit is named for facts that hold at a different commit (finding 36)** |
| Finding numbers | 37 | 37 | 0 — round 1 = 1–3 notes; round 2 = 4–5 revise, 6–10 notes; B = A, B; round 3 = 11, 13, 14 revise, 12, 15–18 notes; round 4 = 20 revise, 19, 21, 22 notes; round 5 = 23 revise, 24–30 notes; round 6 = 31 revise, 32–35 notes — each matched against its raw's heading and label |
| Round words / counts | 71 | 71 | 0 — "six reviews", "Done six times", "seven notes", "four notes", "two repaired … two needing no change", "592 extracted pointers", "496 extracted pointers", "eight scratch mutations", "six scratch mutations" (round-4 raw table: M-B…M-G, six), "all four sibling spec patches" reproduce against the raws or my re-runs; "nine scratch mutations" reproduces the raw's word and not its table (finding 37) |
| OQ / P-row / bead / step / item / Gate-Q tokens | 55 / 71 / 20 / 4 / 13 / 47 | all | 0 — `OQ-6` occurs only as "No OQ-6 is minted"; every quoted row sentence byte-exact at ruling-record lines 55–66; `syzygy-dov.17/.18/.20/.21/.26` exist with the roles given (`bd show`); "items 2–10 and 13–16" is thirteen |
| Number words | 371 | claim-bearing ones reproduce | 0 false; "thirteen", "three", "ten" (the round-1 population) derived above; "17 requirements, 96 distinct authorities" equal the declaration's own line; "eleven", "two patched, nine unchanged" equal the manifest; "41", "39", "36", "6/7", "5", "12", "11", "6", "4", "2", "1" of the ledger reproduce (below) |
| § references | 21 | 21 | 0 |

Total swept: **1,026**; not resolving: **0**; resolving with a false content
claim: **1** (finding 36); resolving to the raw's word rather than its
table: **1** (finding 37).

**Quotation fidelity (criterion 1), every quotation read at source:**
PWB-REQ-010 in full (596–630), PWB-REQ-007's aggregate sentence (448–450)
and Observable (457–458), PWB-REQ-020 (906–910) and its Case (912–914), the
proposed scenario (equal to the patch's `+` lines and to post-apply
621–635), P-71's arm and "What it means" cell (record line 58), the record
head (14–16), P-71-Q5 (59), P-74 and P-78 closing sentences (64, 66, plain
verbs, no emphasis), P-75 Q2 (63), the cross-cutting "one registry act"
bullet (P-69 Q2(a) with P-72 Q2, gate `syzygy-dov.18`), M4 Q7 cell (119:
"same region", "builds the band container and owns its single ordering
oracle", "own honest target", the block-order reservation, the
`home`/`surfaces` counts), M4 slice 3 (827–830, 836–839), M4 Gate 5 cells
("None found.", "Unavailable", 41/55, both "None — the three sweeps …", "in
place … which an opening aggregate is not"), M2 (443–446, 472–475, Q6 cell
50, success criterion 4 at 130–131, 462–465), M3 (905–911, 914–916,
922–923), RFC2-26 (196–221 including "Rows are per observable consequence,
not per clause."), POC-REQ-032 (578–580, Observable 589–590), the
template's change-class table (101–104) and rules 2, 6 and 7 (111–128) and
"I only touched X" (57), the owner's OQ answers (OWNER-VALUES 79–80 and §6,
OPEN-QUESTIONS 33–35 and 39–64), the proposal's §Scope (86–91; the phrase
"declared shape of the configured project" occurs nowhere in it, 0 hits,
and the delta marks it as a paraphrase). All byte-exact where presented as
quotations.

---

## Builder

Run from the worktree root at `d3d5d9d`:

- `--check` → exit 0: "PWB opening-band scenario manifest matches 11
  proposed behavior subjects (2 patched, 9 unchanged); the proposed
  declaration equals its regeneration and the spec patch composes with the
  lane B spec patch in both orders".
- `--selftest` → exit 0: "selftest: closed population, byte drift, path
  order, subject drift, patch corruption, lane B composition (both orders
  and a corrupted case), generated-declaration tampering and the
  declaration-patch collision all fail closed" — criterion 10's nine
  predicates, by name.
- `--diff` → exit 0; output byte-equal to the declaration patch followed by
  the spec patch (the builder emits `proposed/*.patch` sorted by name).
- Manifest semantics by hand: `sha256sum -c` over the eleven rows against
  the tree passes nine and fails exactly `GOVERNING-DEPENDENCIES.md` and
  `spec.md`; after `git apply` of both patches in a scratch copy those two
  hash to the manifest's rows 5 and 11 [Observed]. The spec patch removes
  no line (0 `-` lines outside the header); the declaration patch changes
  the digest line only, "17 requirement(s), 96 distinct authorities" on
  both sides. The new scenario heading carries none of PWB-REQ-012's six
  prohibited words (spec line 687).
- Manifest `sha256sum` → line 3 above, equal to the packet's copy.

**Mutations (rule 6, criterion 10), eleven, in a scratch copy of `scripts/`,
`openspec/changes/` and the two candidate packages, baseline `--check`
passing before and after each; failure text read, not the exit line:**

| # | Mutation | Failure text |
|---|---|---|
| M1 | append a line to unpatched `design.md` | "manifest differs from exact regeneration over the proposed bytes" |
| M3 | swap manifest rows 8 and 9 | "manifest path population or order differs" |
| M7 | delete `GOVERNING-DEPENDENCIES.md.patch` | "proposed/*.patch population differs from the declared patched subjects: spec.md.patch" + "declared patched subject is byte-identical: …GOVERNING-DEPENDENCIES.md" + "proposed GOVERNING-DEPENDENCIES.md differs from regeneration …" + "manifest differs …" |
| M9 | add a twelfth file `EXTRA.md` to the change directory | **passes** — confirms ledger lines 148–151 |
| M10 | patch text "exactly one such aggregate" → "at most one such aggregate" | "proposed GOVERNING-DEPENDENCIES.md differs from regeneration over the proposed spec bytes" + "manifest differs …" |
| M11 | remove lane B's `spec.md.patch` | "missing lane B spec patch: …pwb-scoped-attributes-amendment/proposed/spec.md.patch" |
| M12 | drift spec line 618 ("that slice" → "the slice") | "spec.md.patch does not apply to the base bytes: error: patch failed: …spec.md:618" |
| M13 | flip the first hex char of the manifest's `spec.md` row | "manifest differs from exact regeneration over the proposed bytes" (round-1 item 7's text, exactly) |
| M14 | declaration patch `+` line "96 distinct" → "97 distinct" | "proposed GOVERNING-DEPENDENCIES.md differs from regeneration …" + "manifest differs …" |
| M16 | hand-edit the tree's `GOVERNING-DEPENDENCIES.md` ("## doctrine (8)" → "(9)") | "GOVERNING-DEPENDENCIES.md.patch does not apply to the base bytes: … patch failed: …GOVERNING-DEPENDENCIES.md:8" |
| M15 | apply lane B's declaration patch, then this package's, by plain `git apply` | second apply fails "patch failed: …GOVERNING-DEPENDENCIES.md:8" — the collision delta 613–618 and ledger 295–299 describe |

Ten fail closed with distinct, correct text; M9 is the documented
non-failure; M15 reproduces the documented collision.

**Composition, independent of the builder:** this package's `spec.md.patch`
with each of the four sibling `proposed/spec.md.patch` files
(scoped-attributes, missing-currency-disclosure, machine-view,
exact-source-render-mode) via `git apply` on a clean copy of the current
spec, both orders: every pair applies and each pair yields one digest
regardless of order [Observed].

**Governance battery:** `python3 scripts/check_governance.py` → "32 OK, 20
WARN, 0 FAIL (52 checks)". CG-1b examines 6,812 references, 0 findings;
CG-7e 37 files, 0 findings, with the packet registered "1 current, 0
historical valid"; CG-15 15 quotations, 0 findings; CG-7d lists "SIGN OFF
PWB OPENING-BAND SCENARIO — 0 quotation(s), 0 finding(s), 0 performed
digest(s)". `PWB_SUCCESSOR_CHAIN` (1631–1638) has three links and no
opening-band link, matching the withheld-link note at 1537–1541. The
battery lines sit at `PROJECT-STATUS.md` 256–257 and the CI steps at
`governance-docs.yml` 124–128.

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
×1); the other seven 0; no row carries the run form [Observed, each row
swept]. M9 confirms the twelfth-file sentence.

**Class 3 (2 files):** both JSON declarations carry the current source
digest in `governingBehaviorContract.version` (prefixed `sha256:`) beside
`governingBehaviorContract.signedBy` = "pending exact owner act over the PWB
truth-and-readiness amendment manifest", neither carries `PWB-REQ-010`, and
both are unchanged at `d3d5d9d` [Observed]; labelled Observed for the pins
and Inferred for the repair's home in all three files, as criterion 9
requires.

**Class 4:** no `decisions/` act record and no `*-MANIFEST.txt` is in the
41-citer union [Observed].

**Class 5 (39):** 41 less the two class-1 files = 39, placed in exactly one
kind each by path rule from my own union list: implementation and tests 6
(`polaris.ts`, three `polaris*.test.ts`, `pwb-mutation-sweep.ts`,
`pwb-mutation-sweep-main.ts`), generated coverage views 4, design packets 2
(M3, M4), retained raws 11, dated evidence records 12 (ten
`docs/evidence/*.json` + two `docs/pursuits/2026-09-13-*.json`), plan +
dated review 2, pending register 1, other spec's design note 1 = **39**,
none unplaced. Every path the ledger names is in my list.

**Branch population:** `59733d3` has 1,342 tracked files (1,334 + eight);
`3ee1b0b` has 1,343 [Observed], matching ledger 34–35.

All figures reproduce by two methods.

---

## Disposition check — findings 1–35

| Finding | Round | Label | Disposition in `SEMANTIC-DELTA.md` §Review | Checked at `d3d5d9d` |
|---|---|---|---|---|
| 1 | 1 | note | 672–680 repaired | ledger 31–51 enumerates 4 skipped and 6 NUL; both reproduce |
| 2 | 1 | note | 681–687 wording promoted, OQ-2 open | delta 419–428, packet 156–163; OQ-2 answered (A) 2026-09-23, no byte moved |
| 3 | 1 | note | 688–693 withdrawn | all three files cite the rows, "Q4" marked withdrawn |
| 4 | 2 | revise | 724–731 repaired | ledger regex, 6/7, 41, 39 all reproduce |
| 5 | 2 | revise | 732–738 repaired | ledger 145–153; M9 confirms |
| 6 | 2 | note | 739–746, withdrawn in round 3 | delta 466–472 attributes to M2 line 50, M4 119 quotes it; exact |
| 7 | 2 | note | 747–751 marked at the sentence | ledger 255–261, packet 280–284 dated notes |
| 8 | 2 | note | 752–754 repaired | delta 643–645 names the brief; `3ee1b0b` touched four files, criteria byte-identical from `59733d3` to `d3d5d9d` |
| 9 | 2 | note | 755–759 repaired | P-74/P-78 sentences exact at record 64/66 in all three files, no emphasis |
| 10 | 2 | note | 760–761 repaired | packet 253–254 "may change" |
| A | B | non-blocking | 772–774 | same as 9 |
| B | B | editorial | 774 no change | — |
| 11 | 3 | revise | 819–823 repaired | as 6 |
| 12 | 3 | note | 824–826 repaired | no `**is**`/`**are**` in quotations |
| 13 | 3 | revise | 827–835 repaired | class 5 partitions to 39 (above) |
| 14 | 3 | revise | 836–839 repaired | packet 12–34 names every round |
| 15 | 3 | note | 840–842 repaired | packet 266–268 |
| 16 | 3 | note | 843–847 marked | ledger 301–313 "at the baseline commit", sibling named, composition re-derived (above) |
| 17 | 3 | note | 848–851 repaired | ledger 11–14 |
| 18 | 3 | note | 852–853 repaired | delta 634 "Round 1 verdict:" |
| 19 | 4 | note | 886–890 repaired | delta 583–591 names six rounds |
| 20 | 4 | revise | 891–902 repaired | ledger 199–204, 221–227; ×1 and ×4 re-swept |
| 21 | 4 | note | 903–906 repaired | delta 262, 433–434 both ranges verified |
| 22 | 4 | note | 907–910 repaired | 472 and 836 verified |
| 23 | 5 | revise | 946–953 repaired | superseded wording marked; the current sentence is round 6's repair — finding 36 |
| 24 | 5 | note | 954–956 repaired | 201–205 inside 196; verified |
| 25 | 5 | note | 957–958 repaired | 820–913 verified (914 is `### Slice 6`) |
| 26 | 5 | note | 959–961 repaired | 441–513, 443–446, 472–475 verified |
| 27 | 5 | note | 962–969 repaired | delta 180–195, both readings quoted exactly |
| 28 | 5 | note | 970–973 repaired | packet 3–7 names the act |
| 29 | 5 | note | 974–976 repaired | delta 385–386 marked as paraphrase; 0 hits for the phrase |
| 30 | 5 | note | 977–979 no change | battery CG-7e/CG-15 clean; no prose copy of the digest (0 hits in all four files) |
| 31 | 6 | revise | 1015–1024 repaired | population, three excepted, ten held — confirmed; **item-15 history clause false — finding 36** |
| 32 | 6 | note | 1025–1027 repaired | delta 261–264 verified |
| 33 | 6 | note | 1028–1030 no change | delta 180–195 unchanged |
| 34 | 6 | note | 1031–1034 repaired | packet 9–11; commit dates verified |
| 35 | 6 | note | 1035–1038 no change | M4 1303/1307 verified |

Every finding 1–35 carries a numbered disposition whose stated repair is
present at the cited site; disposition 31's repair is present, its counts
are right, and one clause inside it is false (finding 36). No disposition
claims more than the bytes show, with that one exception.

---

## Per-criterion summary

| # | Criterion | Result |
|---|---|---|
| 1 | Quotation fidelity | **Pass** — every quotation byte-exact at its cited lines; every named source file has the same blob id as at `59733d3` (the two files that moved, `polaris.ts` and `check_governance.py`, are cited by name and commit, and only the second's history is misstated — finding 36 under criterion 9/11) |
| 2 | Change class | **Pass** — Normative under the template table (101–104, rule 2 at 111–112): a renderer with two opening aggregates, a tuple-less one, or a hoisted member complied before and does not now; argued from obligation, not diff size |
| 3 | Scenario form | **Pass** — WHEN/THEN/AND at post-apply 621–635, after the existing scenario (615–619), before `warrants` (637); each clause falsifiable on an inspectable rendering or machine answer; no clause states a value; heading clear of PWB-REQ-012's words |
| 4 | One category, no overlap | **Pass** — the patch's one hunk is `@@ -618,6 +618,22 @@`; lane B's are 450–471, 473–483, 907+; the P-69 Q7a sibling inserts at 469; the P-75 Q1 package is against the other specification; all four sibling compositions verified in both orders |
| 5 | Reconciliation performed | **Pass** — three parties from M4 Q7 (119), each quoted from its own packet at verified lines, R-1/R-2/R-3 each tied to a scenario clause; P-75 Q2 exact at record 63 |
| 6 | Contradictions surfaced, not settled | **Pass** — OQ-1 to OQ-5 genuine, easier reading named and not taken, each the owner's (answered by plain direction 2026-09-23, no byte moved; OQ-5's order is a design value the package does not write); the PWB-REQ-020 reading surfaced at item 3 in the same form |
| 7 | RFC2-26 | **Pass** — both halves hold against 196–221: limb 1 for slice 3 only, conditioned on OQ-2 (answered (A)); slices 4–5 unmapped on M4's own table (1308–1309) and routed to `syzygy-dov.26` |
| 8 | What does not change | **Pass** — all eight items true against the patches: no requirement minted, `warrants` byte-identical (patch removes no line), 17/96 unchanged, no implementation file, no observed-repository write (P-71-Q5 exact at record 59) |
| 9 | Impact ledger | **Pass in the ledger; fail in the delta's §Review sentence (finding 36)** — every ledger figure reproduces by two methods; class-3 labelling correct; the false clause is at delta 652–656; notes 37 and 38 |
| 10 | Manifest and builder | **Pass** — eleven rows, two post-apply and nine current, verified by hand; nine predicates named; ten mutations fail closed with correct text, M9 passes as documented, M15 reproduces the documented collision |
| 11 | Governance hygiene | **Pass with note 39** — no performed act argument or truncated signed digest in prose (0 hits in the four files); act records cited by path; no observed-repository path in a code span (CG-1b 0 findings; swept the four files); every head names the act; claims labelled (29 labels over the three substantive files); nothing labelled accepted, signed or adopted of the package itself (the only "accepted" tokens are disposition verbs and "may be adopted first"); signed change directory untouched (worktree clean, spec blob unchanged) |
| 12 | Scope of authority | **Pass** — nothing performs an act or schedules work; the scenario is conditional ("WHEN … renders an aggregate"), so a conforming implementation may render no opening aggregate; packet 69–72 says so; the owner's landing order (note 39) fixes sequence only and the packet does not read it as more |

---

## Verdict rationale

**REVISE.** One clause in the package is false at the reviewed commit:
`SEMANTIC-DELTA.md` lines 652–656 say item 15's three `check_governance.py`
pointers "moved to 2022, 2236 and 2371 when the lane B registration landed
at `9d74185`", when at `9d74185` they sit at 2010, 2222 and 2355, the
values given date from `807cecf`, and what `9d74185` landed was this
package's own registration — a fact the same package's ledger and packet
state correctly. It is the class rounds 5 and 6 returned REVISE on, in the
same paragraph, and the repair is one clause with the superseded wording
marked. Everything else holds: the bound bytes are unchanged across eight
commits, the builder and eleven mutations behave, every ledger figure
reproduces by two methods, every quotation is exact, the repaired counts
(thirteen, three, ten) are derived and confirmed item by item, the round-6
repairs of findings 32 and 34 are exact, and findings 37–39 are notes. A
round 8 over the repaired bytes may be confined to that paragraph and any
text the repair touches.
