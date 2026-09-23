# Review — Polaris opening-band aggregate scenario package (round 8, fresh context)
Reviewed commit: 28086f67ab6658fb48feb6ed4f6aec3df3227a62
Manifest SHA-256: 7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context session, no authoring context (CC-REV-1). Read-only
against a detached worktree at the reviewed commit (`git worktree add
--detach … 28086f6`; nothing under the repository's own working tree was
opened or touched); every mutation and every patch composition ran in a
copy under the session scratchpad, never in the worktree. Inputs: the
package in full (`SEMANTIC-DELTA.md` 1,114 lines, `IMPACT-LEDGER.md` 313,
`OWNER-DECISION-PACKET.md` 340, `REVIEW-BRIEF.md` 170,
`PWB-OPENING-BAND-SCENARIO-MANIFEST.txt`, `proposed/spec.md.patch`,
`proposed/GOVERNING-DEPENDENCIES.md.patch`,
`scripts/build_pwb_opening_band_scenario.py`); the governing references the
brief names (the signed PWB specification at the cited ranges, POC-REQ-032,
RFC2-26 at its defined clause via `DIRECTIVE-REGISTER.md` line 260,
PWB-REQ-007/010/011/012/020); the ruling record's head, rows P-68…P-78,
P-71-Q5 and its cross-cutting section; the two 2026-09-23 owner-direction
records in full; the M2, M3 and M4 funnels at the cited lines; the
semantic-delta template and the normative-change workflow; and the eight
retained raws (rounds 1–7 and the parallel B) for disposition checking
only. `scripts/check_governance.py` was read at `59733d3`, `3ee1b0b`,
`9d74185`, `807cecf`, `d3d5d9d` and `28086f6` by `git show`, never by
inference. The manifest digest on line 3 was computed with `sha256sum`,
never transcribed (rule 3); it equals the packet's copy (packet line 49)
and every prior raw's line 3.

**Package bytes.** `git diff 210b864 28086f6 -- <package>
scripts/build_pwb_opening_band_scenario.py` is empty [Observed], so the
bytes reviewed are the round-7 repair commit's. The manifest, both patches
and the builder have blob ids `43b8adbd…`, `45b12133…`, `ceebdb53…` and
`edbcd982…` at every one of `59733d3`, `3ee1b0b`, `9d74185`, `dfb605c`,
`76b4beb`, `194f8cd`, `7fd2db3`, `2c5745e`, `d3d5d9d`, `210b864` and
`28086f6` [Observed, `git rev-parse <commit>:<path>` at all eleven];
`IMPACT-LEDGER.md` has blob `59417deb…` from `7fd2db3` onward, unchanged
by rounds 5, 6 and 7 as the delta says.

The verdict rests on no revise finding. Six notes (40–45) are recorded;
none makes a sentence false on the reading its own context fixes, and the
first (40) is the closest call, stated with both readings so the drafter can
repair it before any phrase is offered. Nothing in the patches, the manifest
or the builder needs to move.

---

## Findings

Numbering continues from 39.

**Finding 40 — note. `SEMANTIC-DELTA.md` lines 1074–1075: the round-7
summary says the reviewer "found every quotation byte-exact and every
cited source blob unchanged since `59733d3`".** Criterion 9; rules 2 and 9.

- [Observed] The round-7 raw's item-16 row (its line 156) says "every named
  source file has the same blob id as at `59733d3` (M2, M3, M4, RFC-0002,
  `DIRECTIVE-REGISTER.md`, both specs, the ruling record)" — a claim over
  the eight sources round-1 item 16 names — and its criterion-1 row (line
  413) adds the exception in the same breath: "the two files that moved,
  `polaris.ts` and `check_governance.py`, are cited by name and commit".
  Over those eight sources the claim holds at `28086f6` too: each has the
  same blob id as at `59733d3` [Observed, `git rev-parse`, all eight].
- [Observed] Read over every source the delta cites, the sentence is not
  true: `apps/three-surface-poc/src/polaris.ts` (Evidence bullet, lines
  261–264) is blob `87668005…` at `59733d3` and `800da823…` at `d3d5d9d`
  and `28086f6`; `scripts/check_governance.py` is `603d3c2e…` and
  `54f027ab…`; and the two owner-direction records the delta cites at
  lines 794–796 did not exist at `59733d3` (`git cat-file -e` fails). The
  same paragraph's own predecessor (lines 651–657) says two of those files'
  pointers moved.
- The sentence restates the raw's own word and drops its parenthetical
  restriction and its exception, so its population is unstated — the shape
  round 7 recorded as a note in finding 37. Labelled note on that basis.
  Correct text: "found every quotation byte-exact and the eight sources
  round-1 item 16 names unchanged in blob since `59733d3` (the two files
  cited by commit, `polaris.ts` and `check_governance.py`, excepted)".

**Finding 41 — note. Emphasis markers inside verbatim quotations, the
class round 3 finding 12 repaired at six other sites.** Criterion 1; rule 8.

- [Observed] `SEMANTIC-DELTA.md` 464–466 and `OWNER-DECISION-PACKET.md`
  199–201 quote PWB-REQ-010 as "SHALL **first** present Butlers' purpose,
  promises, non-goals, architecture, V1 scope and success criteria"; the
  spec's line 600 reads "SHALL first present" with no emphasis (`grep -c -F
  '**first**'` over the spec → 0).
- [Observed] `SEMANTIC-DELTA.md` 331–332 quotes the proposed scenario as
  "**exactly one** such aggregate is rendered there"; `proposed/spec.md.patch`
  line 14 reads "exactly one such aggregate is rendered there" with no
  emphasis.
- The words are exact; the markup is the delta's. Correct: drop the
  asterisks at all three sites, or move the emphasis outside the quotation
  marks.

**Finding 42 — note. `SEMANTIC-DELTA.md` line 463: the Q7 quotation ends
"rather than three independent claims on 'first'."** Criterion 1.
[Observed] M4 line 119 reads `three independent claims on "first".` — double
quotation marks, and the sentence's period outside them. The delta's nested
single quotes are the conventional rendering of a quotation inside a
quotation and change no word; recorded only because the criterion asks for
byte-exactness and rounds 2–7 called this sentence exact.

**Finding 43 — note. `OWNER-DECISION-PACKET.md` lines 93–94: "Three
independent "renders first" assertions are three oracles over one piece of
page order."** Criteria 1 and 5; rule 8. [Observed] The phrase "renders
first" occurs nowhere in `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md`
(`grep -c -F 'renders first'` → 0); M4's words at line 119 are "three
independent "renders before the first catalog section" assertions are three
oracles over a single piece of page order", which the delta's own R-1
(lines 328–330) quotes correctly. The packet's quotation marks present a
paraphrase as a quotation, in the owner-facing summary of the
reconciliation. The substance is right. Correct: drop the quotation marks
("Three independent renders-first assertions"), or quote M4's phrase.

**Finding 44 — note. `SEMANTIC-DELTA.md` lines 653–655 "(+139 lines)" and
line 674 "what `9d74185` landed was this package's registration".**
Criterion 9; rule 9. [Observed] `git diff 59733d3 9d74185 --
scripts/check_governance.py` is 139 insertions, 0 deletions, and it adds
three packages' registrations, not one: `PWB_RENDER_MODE_*`,
`PWB_MACHINE_VIEW_*` and `PWB_OPENING_BAND_*` constants and their three
`_SUBJECTS` aliases all first appear in that diff. The pointer claim the
parenthetical supports is true (2010, 2222 and 2355 at `9d74185`; table
below), and this package's registration did land there; but the count word
"+139" is the commit's whole delta to the file and "what `9d74185` landed"
reads as exhaustive when it is one of three. Correct: "when this package's
registration landed at `9d74185`, beside the render-mode and machine-view
packages' (+139 lines to the file)".

**Finding 45 — note. `SEMANTIC-DELTA.md` lines 663–664: "items 6, 7, 8, 10
and 16 were re-read at source by the round-5 reviewer".** Criterion 9;
rule 4. [Observed] The round-5 raw establishes all five, but by re-running
three of them, not re-reading: item 7 is its mutation M2 (raw line 233,
"flip one hex char of the manifest's `spec.md` row" → "manifest differs from
exact regeneration over the proposed bytes"), item 8 is its composition
paragraph (243–249), item 10 is its "undecodable | 4 (the four PNGs named) |
4, same paths" row (271). Items 6 (212–218) and 16 (175–195) are re-reads
at source. Item 14's split attribution (hunks and line 470 to round 5, raw
189–191; line 487 to round 7, raw line 106) is exact. The attribution is
right for every item; the verb is loose for three. Correct: "re-established
by the round-5 reviewer (6 and 16 re-read at source; 7, 8 and 10 re-run)".

No other finding. In particular, every per-commit claim in the repaired
sentence (criterion 9, rule 4) is true at the commit named, and every
superseded-wording marker quotes its predecessor exactly (tables below).

---

## The item-15 anchors, per commit (rule 4: read at each commit, never inferred)

`git show <commit>:scripts/check_governance.py`, fixed-string grep for each
anchor; the lane B constants are lines 1518–1523 (`PWB_SCOPED_AMENDMENT_LABEL`
1518, `_DIR` 1519, `_SUBJECT` 1520–1521, `_ACT` 1522–1523), whose six-line
block hashes identically at every commit read.

| Commit | File lines | `def _act_subjects()` | `ACT_DIGEST_COPY_FILES = {` | activation comment naming `PWB-SCOPED-ATTRIBUTES-AMENDMENT-ACT.md` | lane B constants 1518–1523 | `PWB_OPENING_BAND_*` | `PWB_MISSING_CURRENCY_*` |
|---|---|---|---|---|---|---|---|
| `59733d3` (round-1 draft) | 7,936 | 1976 | 2173 | 2300 | present, block hash `92ab81fa…` | absent | absent |
| `3ee1b0b` (round-1 disposition commit) | 7,936 | 1976 | 2173 | 2300 | same | absent | absent |
| `9d74185` (#52 merge; +139, 0 deletions) | 8,075 | **2010** | **2222** | **2355** | same | 1548–1552 (first appearance) | absent |
| `807cecf` (missing-currency package; 28+/2−, net +26) | 8,101 | **2022** | **2236** | **2371** | same | 1548–1552 | 1557–1563 (first appearance) |
| `d3d5d9d` (round-7 reviewed) | 8,101 | 2022 | 2236 | 2371 | same | 1548–1552 | 1557–1563 |
| `28086f6` (this review) | 8,101 | 2022 | 2236 | 2371 | same | 1548–1552 | 1557–1563 |

`git log a4a3451..28086f6 -- scripts/check_governance.py` names exactly two
commits, `9d74185` and `807cecf` [Observed]; `check_governance.py` is
byte-identical at `a4a3451` and `59733d3`, so "pre-date this draft" holds
for the lane B constants. Every clause of the repaired sentence at delta
649–661 — 1976/2173/2300 at `59733d3`; 2010/2222/2355 at `9d74185`; +139;
2022/2236/2371 at `807cecf` and "at the current bytes"; +26; "this
package's own registration landed at `9d74185`"; "the missing-currency
package's registration"; "the lane B constants at 1518–1523 pre-date this
draft and never moved"; the evidence bracket's four commits — checks
against the file at the commit named [Observed]. Finding 44 is the one
imprecision.

---

## The thirteen round-1 items, each re-checked at `28086f6`

Population derived from the round-1 raw's "What I ran" (items 1–16 at its
lines 21–152): items 2–10 are nine, 13–16 are four, **thirteen** [Observed].
The sentence's standard, fixed by its treatment of item 13: a moved line
pointer means the item does not hold as written.

| Item | Claim in the raw | At `28086f6` | Holds as written? | My evidence |
|---|---|---|---|---|
| 2 | manifest sha256 = the raw's line 3 | equal | yes | `sha256sum`, computed |
| 3 | `--check` exit 0 with the quoted success line | identical text, exit 0 | yes | run from the worktree root |
| 4 | `--selftest` exit 0 naming the nine predicates | identical text, exit 0 | yes | run from the worktree root |
| 5 | `--diff` equals the two patch files | `cmp` equal to the declaration patch followed by the spec patch (name order); differs from the reverse order | yes | run and compared |
| 6 | both patches apply; scenario after the WhatsApp scenario, before `warrants` | post-apply: WhatsApp 615, new scenario 621, `warrants` fence 637, PWB-REQ-011 at 648; post-apply files hash to manifest rows 5 and 11 (`86b1b49f…`, `9a44bdb6…`) | yes | `git apply` in a `git init` scratch tree |
| 7 | flipping one hex of the manifest's `spec.md` row → "manifest differs from exact regeneration over the proposed bytes" | same text, exit 1; restored → pass | yes | mutation R8-M1 |
| 8 | lane B AB and BA compose byte-identically | one digest both orders, `de6516e4…` | yes | `git apply`, independent of the builder |
| 9 | five figures reproduce; continuation form 0/0 | 36/110, 51/113, 9/13, 13/13 reproduce; continuation form is 6/7 | **no** — retracted at ledger line 96 (round 2 finding 4) | re-derived, two methods (below) |
| 10 | 4 undecodable, the four PNGs | same four paths | yes | re-derived over 1,334 blobs |
| 13 | `gapReasonCounts` at `polaris.ts` 920–931 | body identical; sits at 951–960 (922–931 at `a4a3451`) | **no** — pointer moved (round 4 finding 21); substance holds | read at `a4a3451`, `194f8cd`, `28086f6` |
| 14 | lane B hunks `@@ -450,22`, `@@ -473,11`, `@@ -907,23`; PWB-REQ-007's only scenario at 470; next requirement at 487 | all exact; PWB-REQ-007 at 439, its one `#### Scenario` at 470, `### Requirement: PWB-REQ-004` at 487 | yes | lane B patch and spec blob (`543469dc…`) unchanged since `59733d3` |
| 15 | `_act_subjects()` 1976, `ACT_DIGEST_COPY_FILES` 2173, activation comment 2300; constants 1518–1523 | 2022, 2236, 2371; constants unmoved | **no** — three pointers moved (round 6 finding 31); substance holds; the repaired history clause is now true at every commit it names (table above) | six commits read |
| 16 | quotation spot checks exact at the named ranges | every quoted passage exact; every named source file has the same blob id as at `59733d3` | yes | each range read at source; blob ids compared |

Three do not hold as written (9, 13, 15); ten hold. Both counts confirm the
sentence. Its evidence bracket is accurate for every item; finding 45 is
the one loose verb.

---

## The three superseded-wording markers and the packet's superseded recommendation (c, d)

| Marker at `28086f6` | Predecessor (`git show <commit>:<path>`) | Exact? |
|---|---|---|
| delta 667: the first said all "still hold at this commit" | `7fd2db3` delta line 633: "…machine findings (items 2–10 and 13–16 of the raw) still hold at this commit" | yes |
| delta 668–670: the second said "two of the fourteen" do not and "the other twelve hold" | `2c5745e` delta 648 "at the current bytes two of the fourteen do not" and 651 "The other twelve hold" | yes, modulo the sentence-initial capital on "The", folded inside a mid-sentence fragment |
| delta 672–674: the third said item 15's pointers "moved to 2022, 2236 and 2371 when the lane B registration landed at `9d74185`" | `d3d5d9d` delta 654–655: "moved to 2022, / 2236 and 2371 when the lane B registration landed at `9d74185`" (joined across the wrap) | yes |
| packet 311–313: "Recommended after lane B, matching P-68's ordering and this package's separate gate bead; the owner may say otherwise [Inferred]" | `d3d5d9d` packet 301–303: "Recommended after lane B, matching P-68's / ordering and this package's separate gate bead; the owner may say / otherwise [Inferred]." (joined) | yes |

The packet's new paragraph (306–314) against
`.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`
§6 (lines 110–129) [Observed]: the record's verbatim answer is "Readiness
order, lane B last (Recommended)"; its reading runs `.21`, then `.30`, then
`.22`, then lane B; and it closes "The `.21` packet's recommendation to
chain after lane B is superseded by this answer, not edited." The packet
paraphrases the answer without quotation marks ("readiness order, lane B
last — `.21`, then `.30`, then `.22`, then lane B") and states the
superseded-not-edited sentence in its own words; the one quotation it makes
is its own predecessor, exact per the table. The record is dated 2026-09-23
in its title and its commit (`dfb605c`, 2026-09-23) [Observed]. "The
composition claim above is order-independent either way" is true: the
builder composes both orders (below).

---

## Round-7 repairs and count words, each checked

| Round-7 finding | Repair site at `28086f6` | Truthful? |
|---|---|---|
| 36 (revise) | delta 649–677 | [Observed] Every per-commit value and attribution true at the commit named (table above); superseded wording marked in place with its predecessor quoted exactly. Finding 44 is an imprecision in the parenthetical count. |
| 37 | delta 1017–1018 "exercised the nine scratch mutations its raw counts (eight tabulated; its numbering skips M7 — round 7 finding 37)" | [Observed] The round-6 raw's table (its lines 239–248) lists M1–M6, M8, M9: eight rows, no M7; its line 235 says nine. Exact. |
| 38 | delta 663–666 | [Observed] Item 14's hunks and line 470 are at round-5 raw 189–191; "487" occurs nowhere in that raw (fixed-string, 0 hits) and at round-7 raw line 106. Exact. |
| 39 | packet 306–314 | [Observed] See the table above; §6 cited, the answer given, the recommendation kept as superseded text. |
| Round-count sentences (brief 10–36, packet 12–36 and 236–257, delta 583–591 and 1059–1082) | all three files | [Observed] Each names seven rounds and the parallel round, the round-7 verdict word REVISE (copied from the raw's line 4), "one revise finding and three notes" (36 revise; 37–39 three notes), the round-7 raw's filename, and "a round 8"; packet step 1's "three notes, all repaired in prose" matches dispositions 37, 38, 39. |
| Round-7 section count words | delta 1071–1077 | [Observed] "thirteen", "three", "ten" — derived above; "1,026" is the round-7 raw's own figure (its line 194); "eleven scratch mutations" — the raw's table has eleven rows (M1, M3, M7, M9–M16); "seven earlier raws" — rounds 1, 2, B, 3, 4, 5, 6; "findings 1 to 35" and "findings 37 to 39 are notes" match the raw. Finding 40 is the one clause that does not reproduce on its natural reading. |

`git diff d3d5d9d 28086f6` over the package touches only
`SEMANTIC-DELTA.md`, `OWNER-DECISION-PACKET.md` and `REVIEW-BRIEF.md`
[Observed]; `IMPACT-LEDGER.md`, both patches, the manifest and the builder
are unchanged (blob table in the head).

---

## Internal cross-reference sweep

**Method and denominator.** Python `re` over the four prose files
(`SEMANTIC-DELTA.md` 1,114 lines, `IMPACT-LEDGER.md` 313,
`OWNER-DECISION-PACKET.md` 340, `REVIEW-BRIEF.md` 170 — **1,937 lines**;
the extractor counts 1,941 with each file's trailing newline) extracting
every `line N` / `lines N–M` pointer, backticked filename or path token
with a file extension, backticked seven-hex commit token, `finding N`,
`round N`, `OQ-N`, `P-NN` row reference, backticked bead id, `step N`,
`item N`, number word (one…seventeen, thirty-nine, forty-one, ninety-six),
`§` section reference and `Gate N` / `QN` token. Over-inclusive by design:
**1,081 matches**. Every match was resolved against its target at
`28086f6`; line pointers were read to confirm the quoted text lands inside
them.

| Category | Matches | Resolve | Do not resolve |
|---|---|---|---|
| Line pointers | 33 | 33 | 0 — every one read at source: spec 596–630, 448–450 (and 457–458), 906–910, 912–914, 470, 487, 469 (sibling hunk `@@ -469,3`); M2 50, 441–513, 443 (443–446), 462–464, 472 (472–475); M3 903–935, 905, 914 (913–915); M4 119, 827, 836 (836–839), 820–913, 1210; RFC-0002 196–221 and 201–205; register 260; POC spec 578–580 (Observable 589–590); lane B 450–471, 473–483; `polaris.ts` 951–960 at `194f8cd` and 922–931 at `a4a3451`; `check_governance.py` 1976/2173/2300, 2010/2222/2355, 2022/2236/2371, 1518–1523 at the commits named; `model.ts` `PocEpistemic` Unknown arm at 41–42 (a `reason` and nothing else) |
| Filename / path tokens | 222 (67 distinct) | 62 distinct are tracked files or tracked basenames | 5 distinct non-files by design: the `-RAW.md` suffix pattern, the future `PWB-OPENING-BAND-SCENARIO-ACT.md` (constant `PWB_OPENING_BAND_ACT` at `check_governance.py` 1552), the globs `docs/evidence/*.json` and `docs/pursuits/2026-09-13-*.json`, and `proposed/*.patch` |
| Commit tokens | 68 (10 distinct) | 10 | 0 — `59733d3` 2026-09-21 (not an ancestor of HEAD: rebase-merge; compared by blob), `a4a3451` 2026-09-21, `9d74185` 2026-09-22 "(#52)", `807cecf` 2026-09-22, `dfb605c` 2026-09-23 (package byte-identical to `9d74185`: same blob ids), `76b4beb`, `194f8cd` "(#57)", `7fd2db3`, `2c5745e`, `d3d5d9d`, all 2026-09-23 |
| Finding numbers | 49 | 49 | 0 — every reference is to 1–39 or A/B and each carries the label its raw gives it: round 1 = 1–3 notes; round 2 = 4–5 revise, 6–10 notes; B = A, B; round 3 = 11, 13, 14 revise, 12, 15–18 notes; round 4 = 20 revise, 19, 21, 22 notes; round 5 = 23 revise, 24–30 notes; round 6 = 31 revise, 32–35 notes; round 7 = 36 revise, 37–39 notes |
| Round words | 80 | 80 | 0 — "round 8" occurs four times, each as the next step |
| OQ / P-row / bead / step / item / Gate-Q tokens | 55 / 71 / 20 / 4 / 17 / 47 | all | 0 — `OQ-6` occurs once, as "No OQ-6 is minted"; every quoted row sentence byte-exact at ruling-record lines 55–66 (P-71 arm and "What it means" at 58, P-71-Q5 at 59, P-75 Q2 at 63, P-74 at 64, P-78 at 66, head at 14–16, the one-registry-act bullet at 75–77); `syzygy-dov.17/.18/.20/.21/.26` exist with the roles given (`bd show`); "items 2–10 and 13–16" is thirteen |
| Number words | 392 | claim-bearing ones reproduce | 0 false; "17 requirements, 96 distinct authorities" equal the declaration's own line on both sides of the patch; "eleven", "two patched, nine unchanged" equal the manifest and `sha256sum -c` (9 OK, 2 FAILED, exactly `GOVERNING-DEPENDENCIES.md` and `spec.md`); the ledger's 41, 39, 36, 6/7, 5, 12, 11, 6, 4, 2, 1 reproduce below; "+139" and "+26" are the two commits' deltas to the file (finding 44 on the first's population) |
| § references | 23 | 23 | 0 (`§Review finding N` lands on the numbered disposition; `§Scope` is `proposal.md` line 86; `PROJECT-STATUS.md` §"How to verify this page" carries the two builder lines at 256–257) |

Total swept: **1,081**; not resolving: **0**; resolving with an imprecise
content claim: **3** (findings 40, 44, 45).

**Quotation fidelity (criterion 1), every quotation read at source:**
PWB-REQ-010 in full (596–630), PWB-REQ-007's aggregate sentence (448–450)
and Observable (457–458), PWB-REQ-020 (906–910) and its Case (912–914), the
proposed scenario (equal to the patch's `+` lines and to post-apply
621–635), P-71's arm and "What it means" cell, the record head, P-71-Q5,
P-74 and P-78 closing sentences (plain verbs), P-75 Q2, M4 Q7 cell (119:
"same region", "builds the band container and owns its single ordering
oracle", "own honest target", the block-order reservation — finding 42 on
its nested quotes), M4 slice 3 (827–830, 836–839), M4 Gate 5 cells ("None
found.", "Unavailable", 41/55, both "None — the three sweeps …", "in place …
which an opening aggregate is not"; the table has eight rows, 1305–1312),
M2 (443–446, 472–475, Q6 cell 50, success criterion 4 at 130–131, 462–465),
M3 (905–911, 914–916, 922–923), RFC2-26 (196–221 including "Rows are per
observable consequence, not per clause." at 212), POC-REQ-032 (578–580,
Observable 589–590), the template's change-class table (99–104), rule 2
(111–112), rule 6 (123) and "I only touched X" (57), the owner's OQ answers
(OWNER-VALUES 79–80 and §6 110–129; OPEN-QUESTIONS 33–35 and 39–64), the
proposal's §Scope (86–91; "declared shape of the configured project" occurs
nowhere in it and the delta marks it as a paraphrase). All byte-exact where
presented as quotations, with the markup and nested-quote exceptions of
findings 41 and 42 and the packet's paraphrase of finding 43. Every quoted
source file (M2, M3, M4, RFC-0002, `DIRECTIVE-REGISTER.md`, both signed
specs, the ruling record, `proposal.md`, the template) has the same blob id
as at `59733d3` [Observed].

---

## Builder

Run from the worktree root at `28086f6`:

- `--check` → exit 0: "PWB opening-band scenario manifest matches 11
  proposed behavior subjects (2 patched, 9 unchanged); the proposed
  declaration equals its regeneration and the spec patch composes with the
  lane B spec patch in both orders".
- `--selftest` → exit 0: "selftest: closed population, byte drift, path
  order, subject drift, patch corruption, lane B composition (both orders
  and a corrupted case), generated-declaration tampering and the
  declaration-patch collision all fail closed" — criterion 10's nine
  predicates, by name.
- `--diff` → exit 0; output `cmp`-equal to the declaration patch followed by
  the spec patch (the builder emits `proposed/*.patch` sorted by name) and
  not to the reverse order.
- Manifest semantics by hand: `sha256sum -c` over the eleven rows against
  the tree passes nine and fails exactly `GOVERNING-DEPENDENCIES.md` and
  `specs/…/spec.md`; after `git apply` of both patches in a `git init`
  scratch tree those two hash to `86b1b49f…` and `9a44bdb6…`, the manifest's
  rows 5 and 11 [Observed]. The spec patch removes no line (0 `-` lines
  outside the header); the declaration patch changes the digest line only,
  "17 requirement(s), 96 distinct authorities" on both sides. The phrase
  "opening band" is absent from the spec patch (0 hits, case-insensitive).
- Manifest `sha256sum` → line 3 above, equal to the packet's copy.

**Mutations (rule 6, criterion 10), nine plus one by hand, in a scratch
copy holding `scripts/`, both openspec change directories (the dependency
generator resolves qualified parent requirements against the three-surface
spec, so it must be present) and the two candidate packages; baseline
`--check` passing before and after each; failure text read, not the exit
line; `diff -r` of the scratch package against the worktree package empty
after every restore:**

| # | Mutation | Failure text |
|---|---|---|
| R8-M1 | flip the first hex char of the manifest's `spec.md` row | "manifest differs from exact regeneration over the proposed bytes" |
| R8-M2 | patch text "exactly one such aggregate" → "at most one such aggregate" | "proposed GOVERNING-DEPENDENCIES.md differs from regeneration over the proposed spec bytes" + "manifest differs from exact regeneration over the proposed bytes" |
| R8-M3 | add a twelfth file `EXTRA.md` to the change directory | **passes** — the documented non-failure, ledger 148–151 |
| R8-M4 | drift tree `spec.md` line 619 ("complete catalog" → "whole catalog") | "spec.md.patch does not apply to the base bytes: error: patch failed: …spec.md:618" |
| R8-M5 | swap manifest rows 8 and 9 | "manifest path population or order differs" |
| R8-M6 | declaration patch `+` line "96 distinct" → "97 distinct" | "proposed GOVERNING-DEPENDENCIES.md differs from regeneration …" + "manifest differs …" |
| R8-M7 | remove lane B's `spec.md.patch` | "missing lane B spec patch: …pwb-scoped-attributes-amendment/proposed/spec.md.patch" |
| R8-M8 | append a line to unpatched `design.md` | "manifest differs from exact regeneration over the proposed bytes" |
| R8-M9 | delete `GOVERNING-DEPENDENCIES.md.patch` | "proposed/*.patch population differs from the declared patched subjects: spec.md.patch" + "declared patched subject is byte-identical: …GOVERNING-DEPENDENCIES.md" + the R8-M2 pair |
| R8-M10 | apply lane B's declaration patch, then this package's, by plain `git apply` | second apply fails "patch failed: …GOVERNING-DEPENDENCIES.md:8" — the collision delta 613–618 and ledger 295–299 describe |

Eight fail closed with distinct, correct text; R8-M3 is the documented
non-failure; R8-M10 reproduces the documented collision.

**Composition, independent of the builder:** this package's `spec.md.patch`
with lane B's and with the `pwb-missing-currency-disclosure-scenario`
sibling's, via `git apply` on a clean copy of the current spec, both orders:
each pair applies both ways and yields one digest (`de6516e4…` with lane B,
`95918129…` with the sibling) [Observed]. Over the 31 directories under
`contracts/candidates/`, no `proposed/*.patch` targets the three-surface
specification and only this package's delta names `syzygy-dov.26` or
`P-75`, so the ledger's "the second is not [drafted]" (line 309) holds over
that denominator [Observed].

**Governance battery:** `python3 scripts/check_governance.py` → "32 OK, 20
WARN, 0 FAIL (52 checks) — counts derived, not asserted". CG-7d lists
"[subject] SIGN OFF PWB OPENING-BAND SCENARIO — 0 quotation(s), 0
finding(s), 0 performed digest(s)" and the packet as "[registered] …
declares 1 current and 0 performed-history act(s); 1 current, 0 historical
valid". `--selftest` → "263 fixtures, 0 failing". `PWB_SUCCESSOR_CHAIN`
(`check_governance.py` 1631–1638) has three links and no opening-band link,
matching the withheld-link comment at 1537–1541; the battery lines sit at
`PROJECT-STATUS.md` 256–257 and the CI steps at `governance-docs.yml`
124–128 [Observed].

---

## Impact ledger re-derivation

**Method.** Python `re` over every blob of `git ls-tree -r -z --name-only
a4a3451` read by `git show` (no checkout), decoded as UTF-8, undecodable
blobs skipped; the five patterns as the ledger states them, including its
regex `PWB-REQ-\d{3}(?:(?:/|,\s|\s)\d{3})*?(?:/|,\s|\s)010\b` and the
current source digest computed as sha256 of the `a4a3451:spec.md` blob
(prefix `42d073cd`). Second method: `git grep -l -F` / `-o -F` for the
literals and `git grep -l -P` / `-o -P` for the regex at `a4a3451`.
Denominator: **1,334** tracked blobs (`git ls-tree -r --name-only a4a3451 |
wc -l` → 1,334) [Observed].

| Figure | Ledger | Re-derived (`re`) | Second method |
|---|---|---|---|
| tracked files | 1,334 | 1,334 | 1,334 |
| undecodable | 4, the four PNGs | 4, the same four paths | — |
| NUL-carrying | 6 (four PNGs + two `.ts`) | 6, the same six paths (over 1,334; the ledger states it over 1,343) | — |
| `PWB-REQ-010` | 36 / 110 | 36 / 110 | 36 / 110 |
| continuation forms | 6 / 7 | 6 / 7 | 6 / 7 |
| spec path | 51 / 113 | 51 / 113 | 51 / 113 |
| declaration path | 9 / 13 | 9 / 13 | 9 / 13 |
| current source digest | 13 / 13 | 13 / 13 | 13 / 13 |
| run-only adds | 5, named | the same 5 | — |
| both forms | `pwb-p4-2-mutation-sweep-2026-09-04.json` | same | — |
| citer union | 41 | 41 | — |

**Class 2 (9 files):** the nine unpatched manifest rows equal current bytes
(`sha256sum -c`, above). Literal carriers among the eleven rows at
`a4a3451`, each row swept: `CAPABILITY-COVERAGE.md` ×1,
`contract-coverage-matrix/RFC-0007-0009.md` ×4, plus the two class-1 files
(`GOVERNING-DEPENDENCIES.md` ×9, `spec.md` ×1); the other seven 0; no row
carries the run form [Observed]. R8-M3 confirms the twelfth-file sentence.

**Class 3 (2 files):** both JSON declarations carry the current source
digest in `governingBehaviorContract.version` (prefixed `sha256:`) beside
`signedBy` = "pending exact owner act over the PWB truth-and-readiness
amendment manifest"; neither carries `PWB-REQ-010` (0 and 0) [Observed].
Labelled Observed for the pins and Inferred for the repair's home in all
three prose files, as criterion 9 requires.

**Class 4:** no `decisions/` act record and no `*-MANIFEST.txt` is in the
41-citer union [Observed] (the digest sweep's 13 citers include the
performed truth-and-readiness act record and the truth-policy package's
manifest, cited here by path only).

**Class 5 (39):** 41 less the two class-1 files = 39, each placed in
exactly one kind by path rule from my own union list: implementation and
tests 6 (`polaris.ts`, `polaris-first-reading.test.ts`,
`polaris-project-shape.test.ts`, `polaris.test.ts`, `pwb-mutation-sweep.ts`,
`pwb-mutation-sweep-main.ts` — the last run-form only), generated coverage
views 4 (`CAPABILITY-COVERAGE.md`, `contract-coverage-matrix/RFC-0007-0009.md`,
`contract-coverage-parts/RFC-0007-0009.md`, `tasks.md`), design packets 2
(M3, M4), retained raws 11, dated evidence records 12 (ten
`docs/evidence/*.json` + two `docs/pursuits/2026-09-13-*.json`), plan +
dated review 2 (`docs/PWB-IMPLEMENTATION-PLAN.md`,
`docs/reviews/2026-09-09-polaris-editorial-repair.md`), pending register 1,
other spec's design note 1 (`openspec/changes/polaris-manifesto-generation/design.md`)
= **39**, none unplaced, none twice [Observed]. One raw
(`R-PWB-LIVE-EXACT-HEAD-ENGINEERING-RAW.md`) and three evidence records
reach the class only through the run form, as stated.

**Branch population:** `59733d3` has 1,342 tracked files (1,334 + eight);
`3ee1b0b` has 1,343 [Observed], matching ledger 34–35; at `3ee1b0b` the
ledger still said "adds no file" (its line 90), the anchors sat at
1976/2173/2300 and `polaris.ts` had the `a4a3451` blob, so "held at the
round-1 disposition commit" is true.

All figures reproduce by two methods.

---

## Disposition check — findings 1–39

| Finding | Round | Label | Disposition in `SEMANTIC-DELTA.md` §Review | Checked at `28086f6` |
|---|---|---|---|---|
| 1 | 1 | note | 683–691 repaired | ledger 31–51 enumerates 4 skipped and 6 NUL; both reproduce |
| 2 | 1 | note | 692–698 wording promoted, OQ-2 open | delta 419–428, packet 158–165; OQ-2 answered (A) 2026-09-23, no byte moved |
| 3 | 1 | note | 699–704 withdrawn | all three files cite the rows; "Q4" marked withdrawn |
| 4 | 2 | revise | 735–742 repaired | ledger regex, 6/7, 41, 39 all reproduce |
| 5 | 2 | revise | 743–749 repaired | ledger 145–153; R8-M3 confirms |
| 6 | 2 | note | 750–757, withdrawn in round 3 | delta 466–472 attributes to M2 line 50, M4 119 quotes it; exact |
| 7 | 2 | note | 758–762 marked at the sentence | ledger 255–261, packet 285–289 dated notes; registration sites verified |
| 8 | 2 | note | 763–765 repaired | delta 643–645 names the brief; criteria byte-identical from `59733d3` (brief diffs are its status paragraph only) |
| 9 | 2 | note | 766–770 repaired | P-74/P-78 sentences exact at record 64/66 in all three files, no emphasis |
| 10 | 2 | note | 771–772 repaired | packet 258–259 "may change" |
| A | B | non-blocking | 783–785 | same as 9 |
| B | B | editorial | 784–785 no change | — |
| 11 | 3 | revise | 830–834 repaired | as 6 |
| 12 | 3 | note | 835–837 repaired | no `**is**`/`**are**` in quotations (the surviving emphasis-in-quotation sites are finding 41's, a different clause) |
| 13 | 3 | revise | 838–846 repaired | class 5 partitions to 39 (above) |
| 14 | 3 | revise | 847–850 repaired | packet 12–36 names every round |
| 15 | 3 | note | 851–853 repaired | packet 272–273 |
| 16 | 3 | note | 854–858 marked | ledger 301–313 "at the baseline commit", sibling named, composition re-derived |
| 17 | 3 | note | 859–862 repaired | ledger 11–14 |
| 18 | 3 | note | 863–864 repaired | delta 634 "Round 1 verdict:" |
| 19 | 4 | note | 897–901 repaired | delta 583–591 names seven rounds and a round 8 |
| 20 | 4 | revise | 902–913 repaired | ledger 199–204, 221–227; ×1 and ×4 re-swept |
| 21 | 4 | note | 914–917 repaired | delta 262, 433–434 both ranges verified |
| 22 | 4 | note | 918–921 repaired | 472 and 836 verified |
| 23 | 5 | revise | 957–964 repaired | superseded wording marked; the current sentence is round 7's repair, true at every commit named |
| 24 | 5 | note | 965–967 repaired | 201–205 inside 196; verified |
| 25 | 5 | note | 968–969 repaired | 820–913 verified (914 is `### Slice 6`) |
| 26 | 5 | note | 970–972 repaired | 441–513, 443–446, 472–475 verified |
| 27 | 5 | note | 973–980 repaired | delta 180–195, both readings quoted exactly at spec 913–914 and M2 464 |
| 28 | 5 | note | 981–984 repaired | packet 3–7 names the act |
| 29 | 5 | note | 985–986 repaired | delta 385–387 marked as paraphrase; 0 hits for the phrase in `proposal.md` |
| 30 | 5 | note | 987–990 no change | battery CG-7e/CG-15 clean; the current digest appears only in the declaration patch's `-` line; 0 prose copies (the one 64-hex literal in prose is this package's own manifest digest, packet 49) |
| 31 | 6 | revise | 1028–1037 repaired | population thirteen, three excepted, ten held — confirmed; the item-15 history clause now true (round 7's repair) |
| 32 | 6 | note | 1038–1040 repaired | delta 261–264 "for OQ-3 below" verified |
| 33 | 6 | note | 1041–1043 no change | delta 180–195 unchanged |
| 34 | 6 | note | 1044–1047 repaired | packet 9–11; `3ee1b0b` is 2026-09-22 01:11 +0800 |
| 35 | 6 | note | 1048–1051 no change | M4 1303 heads the column `Limb 1`; the slice-3 cell (1307) opens "**Unavailable.** Limb 2 …" |
| 36 | 7 | revise | 1086–1096 repaired | per-commit table above; every value true at the commit named; superseded wording exact |
| 37 | 7 | note | 1097–1100 repaired | delta 1017–1018 verified against the round-6 raw's table |
| 38 | 7 | note | 1101–1104 repaired | delta 663–666 verified against both raws |
| 39 | 7 | note | 1105–1108 repaired | packet 306–314 verified against OWNER-VALUES §6 |

Every finding 1–39 carries a numbered disposition whose stated repair is
present at the cited site and describes the diff truthfully. No
disposition claims more than the bytes show.

---

## Per-criterion summary

| # | Criterion | Result |
|---|---|---|
| 1 | Quotation fidelity | **Pass with notes 41, 42, 43** — every quotation's words byte-exact at its cited lines; the exceptions are added emphasis markup at three sites, nested quotes rendered single at one, and one paraphrase in quotation marks in the packet's summary |
| 2 | Change class | **Pass** — Normative under the template table (99–104) and rule 2 (111–112): a renderer with two opening aggregates, a tuple-less one, or a hoisted member complied before and does not now; argued from obligation, not diff size |
| 3 | Scenario form | **Pass** — WHEN/THEN/AND at post-apply 621–635, after the existing scenario (615–619), before `warrants` (637); each clause falsifiable on an inspectable rendering or machine answer; no clause states a value; heading carries none of PWB-REQ-012's six words |
| 4 | One category, no overlap | **Pass** — the patch's one hunk is `@@ -618,6 +618,22 @@`; lane B's are 450–471, 473–483, 907+; the P-69 Q7a sibling inserts at 469; no candidate patch targets the three-surface specification; both compositions verified in both orders |
| 5 | Reconciliation performed | **Pass** — three parties from M4 Q7 (119), each quoted from its own packet at verified lines, R-1/R-2/R-3 each tied to a scenario clause; P-75 Q2 exact at record 63; note 43 is in the packet's summary, not the delta's reconciliation |
| 6 | Contradictions surfaced, not settled | **Pass** — OQ-1 to OQ-5 genuine, the easier reading named and not taken, each the owner's (answered by plain direction 2026-09-23, no proposed byte moved; OQ-5's order is a design value the package does not write); the PWB-REQ-020 reading surfaced at item 3 in the same form |
| 7 | RFC2-26 | **Pass** — both halves hold against 196–221: limb 1 for slice 3 only, conditioned on OQ-2 (answered (A)); slices 4–5 unmapped on M4's own eight-row table (1308–1309) and routed to `syzygy-dov.26` |
| 8 | What does not change | **Pass** — all eight items true against the patches: no requirement minted, `warrants` byte-identical (the patch removes no line), 17/96 unchanged, no implementation file, no observed-repository write (P-71-Q5 exact at record 59) |
| 9 | Impact ledger | **Pass in the ledger; notes 40, 44, 45 in the delta's §Review** — every ledger figure reproduces by two methods over a stated denominator; class-3 labelling correct; the three notes are population-unstated or loosely verbed restatements of raw findings, none making a figure wrong |
| 10 | Manifest and builder | **Pass** — eleven rows, two post-apply and nine current, verified by hand; nine predicates named; eight mutations fail closed with correct text, R8-M3 passes as documented, R8-M10 reproduces the documented collision |
| 11 | Governance hygiene | **Pass** — no performed act argument or truncated signed digest in prose (the current source digest occurs only in the declaration patch's `-` line; no 7–16-hex-plus-ellipsis anywhere); act records cited by path; no observed-repository path in a code span (every "butler" code span is a Syzygy-internal path; CG-1b clean); every head carries its candidate or inert banner naming the act; claims labelled (delta 10 Observed / 1 Inferred, ledger 12 / 3, packet 2 / 2); nothing labels the offering accepted, signed or adopted; signed change directory untouched (spec blob `543469dc…` unchanged since `59733d3`) |
| 12 | Scope of authority | **Pass** — nothing performs an act or schedules work; the scenario is conditional ("WHEN … renders an aggregate"), so a conforming implementation may render no opening aggregate; packet 71–74 says so; the owner's landing order is recorded as sequence only and the packet does not read it as more |

---

## Verdict rationale

**CONFIRM WITH EXCEPTIONS.** No sentence in the package is false at the
reviewed commit on the reading its own context fixes. The clause rounds 5,
6 and 7 each returned REVISE on — the round-1 §Review sentence about which
round-1 raw items still hold — is now true in every per-commit claim it
makes: 1976/2173/2300 at `59733d3`, 2010/2222/2355 at `9d74185` (+139),
2022/2236/2371 at `807cecf` (+26) and at the reviewed commit, the lane B
constants at 1518–1523 unmoved at all six commits read, and this package's
registration (not lane B's) at `9d74185` — each read in the file at that
commit, never inferred. Its three superseded-wording markers and the
packet's superseded recommendation quote their predecessors exactly; the
packet's new paragraph reports OWNER-VALUES §6 accurately; every count word
in the round-7 section derives from a population I re-derived. The bound
bytes have the same blob ids at all eleven commits from `59733d3` to
`28086f6`; the builder's three modes, nine scratch mutations and the
hand-reproduced declaration-patch collision behave as documented; every
ledger figure reproduces by two methods over 1,334 blobs; 1,081 extracted
pointers all resolve; and findings 1–39 are all dispositioned truthfully.
The six notes are: one restatement of the round-7 raw with its population
and exception dropped (40, the closest call, whose natural reading is false
for two files cited by commit and two records that post-date `59733d3` —
repair it before a phrase is offered); three quotation-markup or
paraphrase-in-quotes imprecisions (41–43); one count word whose population
is a commit's whole diff rather than this package's share of it (44); and
one loose verb in an evidence attribution (45). None moves a figure, a
patch byte, the open questions or the scenario's conditional character, and
none reads as performing an act or scheduling the band.
