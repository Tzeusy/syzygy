# Review — Polaris opening-band aggregate scenario package (round 9, fresh context)
Reviewed commit: 815785a9dbf8c90937039dfde977355c98551cee
Manifest SHA-256: 7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context session, no authoring context (CC-REV-1). Read-only
against a detached worktree at the reviewed commit (`git worktree add
--detach … 815785a`; nothing under the repository's own working tree was
opened, edited or staged — the one exception is `bd show` on five bead ids,
a read of the tracker, since `.beads/issues.jsonl` is not tracked at this
commit); every mutation and every patch composition ran in a copy under the
session scratchpad, never in the worktree. Inputs: the package in full
(`SEMANTIC-DELTA.md` 1,211 lines, `IMPACT-LEDGER.md` 313,
`OWNER-DECISION-PACKET.md` 346, `REVIEW-BRIEF.md` 173,
`PWB-OPENING-BAND-SCENARIO-MANIFEST.txt`, `proposed/spec.md.patch`,
`proposed/GOVERNING-DEPENDENCIES.md.patch`,
`scripts/build_pwb_opening_band_scenario.py`); the governing references the
brief names (the signed PWB specification at every cited range, POC-REQ-032,
RFC2-26 at its defined clause via `DIRECTIVE-REGISTER.md` line 260,
PWB-REQ-007/010/011/012/020); the ruling record's head and rows P-71,
P-71-Q5, P-74, P-75, P-78; the two 2026-09-23 owner-direction records at the
cited lines; the M2, M3 and M4 funnels at the cited lines; the semantic-delta
template and the normative-change workflow; and the nine retained raws
(rounds 1–8 and the parallel B) for disposition checking only.
`scripts/check_governance.py` was read at `59733d3`, `3ee1b0b`, `9d74185`,
`807cecf`, `d3d5d9d`, `28086f6` and `815785a` by `git show`, never by
inference (rule 4). The manifest digest on line 3 was computed with
`sha256sum`, never transcribed (rule 3); it equals the packet's copy (packet
line 53) and line 3 of every one of the nine prior raws.

**Package bytes.** `git diff 28086f6 815785a -- <package> docs/README.md`
touches `SEMANTIC-DELTA.md`, `OWNER-DECISION-PACKET.md`, `REVIEW-BRIEF.md`
and `docs/README.md` only [Observed]; `git diff 28086f6 7966294` over the
package, the builder and `docs/README.md` is empty, so the three intervening
commits (`193de50`, `1482b68`, `7966294`) touch nothing reviewed here
[Observed]. The manifest, both patches and the builder have blob ids
`43b8adbd…`, `45b12133…`, `ceebdb53…` and `edbcd982…` at every one of the
twelve commits `59733d3`, `3ee1b0b`, `9d74185`, `dfb605c`, `76b4beb`,
`194f8cd`, `7fd2db3`, `2c5745e`, `d3d5d9d`, `210b864`, `28086f6` and
`815785a` [Observed, `git rev-parse <commit>:<path>` at all twelve];
`IMPACT-LEDGER.md` is blob `59417deb…` from `7fd2db3` through `815785a`,
unchanged by rounds 5–8 as the delta says. `28086f6` is an ancestor of
`815785a`; `59733d3` is not an ancestor of `815785a` (rebase-merge), so it
was compared by blob.

The verdict rests on no revise finding. Two notes (46, 47) are recorded;
neither makes a sentence false on the reading its own context fixes. Every
round-8 note's repair is present, true, and quotes its predecessor exactly
against `git show 28086f6:<path>`. Nothing in the patches, the manifest or
the builder needs to move.

---

## Findings

Numbering continues from 45.

**Finding 46 — note. `SEMANTIC-DELTA.md` lines 1086–1088 (the round-8
repair of finding 40) and 1170–1172 (disposition 40): "the eight sources
round-1 item 16 names".** Criterion 9; rules 2 and 9.

- [Observed] Round-1 item 16 (its raw, lines 144–152) names **seven**
  source files: the PWB specification (three ranges, one file), RFC-0002,
  `DIRECTIVE-REGISTER.md`, M4, M2, M3 and the three-surface specification.
  It does not name the ruling record. The ruling record is round-1 **item
  11** ("Owner ruling record, read in full (102 lines)", raw line 65).
- [Observed] The "eight" is the round-7 raw's own list at its line 156 —
  "(M2, M3, M4, RFC-0002, `DIRECTIVE-REGISTER.md`, both specs, the ruling
  record)" — which the round-8 raw (lines 55–57) characterised as "a claim
  over the eight sources round-1 item 16 names". The round-8 repair copied
  that characterisation. So the population is stated, but attributed to a
  list that holds seven, not eight: the same class disposition 40 itself
  names ("a reviewer's sentence copied without its population"), one
  further step removed.
- [Observed] The claim holds over both candidate populations: all eight
  files of the round-7 list have the same blob id at `59733d3`, `28086f6`
  and `815785a` (table below), and so, a fortiori, do item 16's seven. No
  reader who re-derives from either list is misled about what is unchanged.
  Note on that basis. Correct text: "the eight sources the round-7 raw's
  item-16 row lists (round-1 items 11 and 16's sources)".

**Finding 47 — note. `SEMANTIC-DELTA.md` lines 289–292: the M2 quotation
"**The probe's own freshness.** The probe claim carries no freshness value,
before slice 5 and after it. It is not a project-shape claim, so
PWB-REQ-007's complete-tuple requirement does not reach it."** Criterion 1;
rule 8. [Observed] M2 line 474 reads "…complete-tuple requirement does not
reach it, and RFC2-10's disclosure route is exactly what it is: a fact of the
render." The quotation ends the sentence at the clause boundary with a period
the source does not have and no elision mark. Every word is exact and the
sense is unchanged (the omitted clause concerns RFC2-10, not the boundary
the delta relies on); the delta's inline re-use at lines 350–351 closes the
quotation before any punctuation and is exact. Rounds 2–8 called this
passage exact; recorded because the criterion asks for byte-exactness.
Correct: end the quotation at "reach it" with the period outside the marks,
or carry the rest of M2's sentence.

No other finding. Two observations that are not findings: (i) the code span
`git show <commit>:scripts/check_governance.py` at delta lines 665–666 wraps
across a line break (the one odd-backtick line pair in 2,043 non-fence lines
over the four prose files, fences and the blockquoted `yaml` fence at 74/83
excluded); it pre-dates the round-8 repair, CommonMark renders it as one
span, and the basename `check_governance.py` sits whole on line 666, so no
basename sweep is defeated — but the repository's own lesson says never to
let a reflow break a code span. (ii) Mutation R9-M14 below rewrites the
builder's own collision predicate to return `True` unconditionally and the
selftest still passes: a selftest exercises inputs, not its own code, so
this is expected and not a defect, but it bounds what "fails closed" means.

---

## The six round-8 notes, each repair checked (commission item 1)

| Round-8 note | Repair site at `815785a` | Predecessor at `28086f6` (`git show`) | New sentence true? | Population stated? |
|---|---|---|---|---|
| 40 | delta 1086–1093 | 1074–1075: "found every quotation byte-exact and every cited source blob unchanged since `59733d3`" — the marked fragment "every cited source blob unchanged since `59733d3`" is exact (joined across the wrap) | [Observed] Yes: the eight files of the round-7 list have identical blobs at `59733d3` and `815785a` (M2 `a4c74249`, M3 `e7f493a7`, M4 `6f3482a2`, RFC-0002 `b3fe589e`, register `ad31b541`, PWB spec `543469dc`, POC spec `1280a62e`, ruling record `f7101da5`); the two files cited by commit differ (`polaris.ts` `87668005` → `800da823`; `check_governance.py` `603d3c2e` → `54f027ab`); the two owner-direction records are absent at `59733d3` (`git rev-parse` fails) — every part of the repair's own parenthetical reproduces | Stated, but attributed to item 16 — finding 46 |
| 41 | delta 464 ("SHALL first present"), 332 ("exactly one such aggregate"); packet 204 | packet 200 `"SHALL **first** present`; delta 332 `"**exactly one** such aggregate`; delta 464 `"SHALL **first** present` | [Observed] `grep -c -F '**first**'` → 0 in the spec, the delta and the packet; `'**exactly one**'` → 0 in the delta and the patch; spec line 600 reads "SHALL first present" | n/a |
| 42 | delta 459–463 | 28086f6 line 463: `…claims on 'first'."` | [Observed] The joined delta quotation is byte-present in M4 line 119, double marks and the period outside them | n/a |
| 43 | packet 97–98 "Three independent renders-first assertions" | packet 93 `Three independent "renders first"` | [Observed] `'renders first'` → 0 in M4 and 0 in the packet (its one delta hit is disposition 43 quoting the finding); M4 119 carries "three independent "renders before the first catalog section" assertions are three oracles over a single piece of page order", which delta 328–329 quotes | n/a |
| 44 | delta 659–662 and 684–687 | 656 `(+139 lines)`; 674–675 `what `9d74185` landed was this package's / registration` (joined) — both marked fragments exact | [Observed] `git diff --numstat 59733d3 9d74185 -- scripts/check_governance.py` → 139 insertions, 0 deletions; `PWB_RENDER_MODE_LABEL`, `PWB_MACHINE_VIEW_LABEL` and `PWB_OPENING_BAND_LABEL` definitions are all `+` lines of that diff and absent at `59733d3` and `3ee1b0b` (0, 0, 0 hits) and present at `9d74185` (9, 5, 5); `PWB_MISSING_CURRENCY_LABEL` first appears at `807cecf` (0 → 5); `9d74185..807cecf` is 28+/2−, net +26. "For all three" and "one of three" are exact | Yes (the commit's whole delta, three registrations) |
| 45 | delta 668–674 | 663–664 `items 6, 7, 8, / 10 and 16 were re-read at source by the round-5 reviewer` — the marked fragment "re-read at source" is exact | [Observed] Round-5 raw: 175–195 is its quotation-fidelity re-read (item 16); 212–218 its by-hand manifest and post-apply placement (item 6); 233 its mutation M2, "flip one hex char of the manifest's `spec.md` row" (item 7); 243–249 its composition paragraph (item 8); 271 its "undecodable | 4 (the four PNGs named)" row (item 10). Item 14's split — hunks and line 470 at round-5 raw 189–191; "487" at 0 hits in that raw and at round-7 raw line 106 — holds | Yes (2 re-read, 3 re-run, each named) |

`git diff 28086f6 815785a` over the package is prose in three files;
`IMPACT-LEDGER.md`, both patches, the manifest and the builder are unchanged
(blob table in the head) [Observed].

---

## The round-8 section of `SEMANTIC-DELTA.md` (1135–1211), every figure against the round-8 raw (commission item 2)

| Sentence at `815785a` | In the round-8 raw | Derived from |
|---|---|---|
| "commissioned … with the eight earlier raws" (1139) | raw 21–22: "the eight retained raws (rounds 1–7 and the parallel B)" | 7 + 1 = 8; `ls docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-*` at `28086f6` gives 8 files |
| "read `check_governance.py` at six commits" (1148) | raw 23–24 names `59733d3`, `3ee1b0b`, `9d74185`, `807cecf`, `d3d5d9d`, `28086f6`; "six commits read" at 197 and 528 | six, listed; my own read at those six plus `815785a` reproduces every value (table below) |
| "1976/2173/2300 at `59733d3` and `3ee1b0b`; 2010/2222/2355 at `9d74185`; 2022/2236/2371 at `807cecf`, `d3d5d9d` and `28086f6`; the lane B constants hash-identical at all six" (1150–1152) | raw table 154–161 | reproduced below at seven commits |
| "the three superseded-wording markers and the packet's superseded recommendation quoting their predecessors exactly" (1152–1155) | raw 206–213 | re-checked below |
| "the bound files' blob ids identical at all eleven commits from `59733d3` to `28086f6`" (1155–1156) | raw 32–35 lists eleven commits | reproduced at all eleven plus `815785a` (head) |
| "ran the builder's three modes, nine scratch mutations and the declaration-patch collision by hand" (1156–1157) | raw 331: "nine plus one by hand"; table 341–350 has R8-M1…R8-M9 and R8-M10 "by plain `git apply`" | 9 + 1 |
| "reproduced every ledger figure by two methods over 1,334 blobs" (1158) | raw 387–388, 392 | re-derived below |
| "resolved 1,081 extracted pointers over 1,937 lines with none unresolved" (1158–1159) | raw 253 (1,937 lines), 260 (1,081 matches), 275 (0 not resolving) | the raw's own figures, correctly copied |
| "findings 1 to 39 dispositioned truthfully" (1159–1160) | raw 449–497 | — |
| "no revise finding; findings 40 to 45 are notes, the first of them the reviewer's "closest call"" (1160–1162) | raw 39–41 ("Six notes (40–45)… the first (40) is the closest call"), 540 | — |
| "the round-8 CONFIRM WITH EXCEPTIONS is bound to `28086f6` alone" (1165–1166) | raw line 2 and 4 | — |
| Dispositions 40–45 (1169–1203): each states the raw's finding and the repair made | each repair verified in the table above | — |

The round-7 section's repaired count words: "thirteen" (round-1 items 2–10
and 13–16: 9 + 4) and "three … and ten" reproduce from the round-1 raw's
"What I ran" (its lines 21–152, sixteen items, item heads read); "1,026" is
the round-7 raw's own figure (its line 194); "eleven scratch mutations" is
the round-7 raw's table (eleven rows); "the eight sources" — finding 46.
Every number word in the round-8 section derives from a stated population.

---

## Status heads, step-1 sentences, brief head, README row (commission item 3)

- Delta step 1 (583–595): "Done eight times", the eight rounds with their
  commits and verdict words, "round 8, over `28086f6`, CONFIRM WITH
  EXCEPTIONS (six notes, no revise finding)", "A round 9 over these bytes is
  the next step" [Observed — each verdict word equals line 4 of its raw; each
  commit is the one its raw names on line 2].
- Packet head (12–40): eight rounds and the parallel round, each with its
  raw's filename and verdict word copied exactly; "await a round 9 — the
  round-8 confirmation covers `28086f6`, and its six notes were repaired in
  prose after it" [Observed, true: the six repairs are the diff]. Packet step
  1 (240–263): "Done eight times", round 8 "no revise finding, six notes, all
  repaired in prose", "a round 9 over these bytes is the next step"
  [Observed; dispositions 40–45 are all "Accepted and repaired"].
- Brief head (10–39): "Eight reviews have been run against this brief",
  round 8 sentence with its raw's filename [Observed]. Its "What the reviewer
  receives" and "Criteria" sections are byte-identical to `59733d3` (diff
  from that heading to end of file is empty) [Observed].
- `docs/README.md` line 84: P-71 row count **9**; `ls
  docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-*` → 9 files; `git
  ls-files docs/reviews | wc -l` → 225 [Observed]. Line 93: "225 files, 225
  assigned"; `python3 scripts/check_docs_review_campaign_partition.py --check
  docs/README.md` from the worktree root → "second-method PASS: git
  ls-files=225; git ls-tree=225; exact path sets equal" and "partition PASS:
  denominator=225; assigned=225; raw=200; other=25; unmatched=0; overlaps=0;
  campaigns=50" [Observed]. The row's text — eighth review CONFIRM WITH
  EXCEPTIONS at `…-CONFIRMATION-7-RAW.md:4`, six notes, no revise finding,
  awaits a round 9 — is true.

---

## The item-15 anchors, per commit (commission item 4; rule 4: read at each commit, never inferred)

`git show <commit>:scripts/check_governance.py`, fixed-string grep for each
anchor; lane B constants are lines 1518–1523 at every commit and the six-line
block hashes identically (`92ab81fa…`) at all seven.

| Commit | File lines | `def _act_subjects()` | `ACT_DIGEST_COPY_FILES = {` | activation comment naming `PWB-SCOPED-ATTRIBUTES-AMENDMENT-ACT.md` | `PWB_OPENING_BAND_LABEL =` | `PWB_MISSING_CURRENCY_LABEL =` |
|---|---|---|---|---|---|---|
| `59733d3` | 7,936 | 1976 | 2173 | 2300 | absent | absent |
| `3ee1b0b` | 7,936 | 1976 | 2173 | 2300 | absent | absent |
| `9d74185` (+139/−0) | 8,075 | 2010 | 2222 | 2355 | 1548 | absent |
| `807cecf` (+28/−2) | 8,101 | 2022 | 2236 | 2371 | 1548 | 1557 |
| `d3d5d9d` | 8,101 | 2022 | 2236 | 2371 | 1548 | 1557 |
| `28086f6` | 8,101 | 2022 | 2236 | 2371 | 1548 | 1557 |
| `815785a` | 8,101 | 2022 | 2236 | 2371 | 1548 | 1557 |

`git log a4a3451..815785a -- scripts/check_governance.py` names exactly
`807cecf` and `9d74185`; the file's blob is identical at `a4a3451` and
`59733d3` (`603d3c2e…`), so "pre-date this draft and never moved" holds for
the lane B constants [Observed]. Every per-commit clause of the round-1
§Review paragraph (delta 653–691) — 1976/2173/2300 at `59733d3`;
2010/2222/2355 at `9d74185` beside two siblings' registrations, +139 for all
three; 2022/2236/2371 at `807cecf`, +26; the evidence bracket's four
commits; "included this package's registration … one of three" — is true at
the commit named [Observed].

**The three superseded-wording markers and the packet's superseded
recommendation** re-checked at `815785a` against `git show`: delta 677
"still hold at this commit" ↔ `7fd2db3` delta 633; delta 679–680 "two of the
fourteen" / "the other twelve hold" ↔ `2c5745e` delta 648 and 651; delta
682–683 "moved to 2022, 2236 and 2371 when the lane B registration landed at
`9d74185`" ↔ `d3d5d9d` delta 654–655 (joined across the wrap); packet
317–319 "Recommended after lane B, matching P-68's ordering and this
package's separate gate bead; the owner may say otherwise [Inferred]" ↔
`d3d5d9d` packet 301–303 — all exact [Observed]. The packet's §6 paragraph
(309–320) against OWNER-VALUES lines 110–129: the verbatim answer is
"Readiness order, lane B last (Recommended)", the reading runs `.21`, `.30`,
`.22`, lane B, and the record closes "The `.21` packet's recommendation to
chain after lane B is superseded by this answer, not edited" — the packet
paraphrases without quotation marks and quotes only its own predecessor,
exactly [Observed]. Both owner-direction records were added 2026-09-23
(`dfb605c`, `39bc2dc`) [Observed].

---

## Internal cross-reference sweep (commission item 5)

**Method and denominator.** Python `re` over the four prose files
(`SEMANTIC-DELTA.md` 1,211 lines, `IMPACT-LEDGER.md` 313,
`OWNER-DECISION-PACKET.md` 346, `REVIEW-BRIEF.md` 173 — **2,043 lines**)
extracting every backticked filename or path token with a file extension,
backticked seven-hex commit token, `finding N`, `round N`, `OQ-N`, `P-NN`,
backticked bead id, `line N` / `lines N–M`, `step N` / `item N` and `§`
reference: **701 matches**, over-inclusive by design. Every match resolved
against its target at `815785a`.

| Category | Matches | Resolve | Do not resolve |
|---|---|---|---|
| Filename / path tokens | 239 (68 distinct) | 67 distinct are tracked files, tracked basenames, package-relative files, the future `PWB-OPENING-BAND-SCENARIO-ACT.md` (constant at `check_governance.py` 1552) or the two globs | 1 by design: the `-RAW.md` suffix pattern in the brief |
| Commit tokens | 92 (12 distinct) | 12 — `59733d3`, `3ee1b0b`, `9d74185`, `dfb605c`, `76b4beb`, `194f8cd`, `7fd2db3`, `2c5745e`, `d3d5d9d`, `807cecf`, `28086f6`, `a4a3451` all `git cat-file -e` as commits | 0 |
| Finding numbers | 58 | all in 1–45; the delta carries a numbered disposition for every one of 1–45 (`^\s{0,4}N\. \*\*`, none missing) | 0 |
| Round words | 91 | all in 1–9; "round 9" occurs three times (packet ×2, delta ×1), each as the next step | 0 |
| OQ / P-row / bead / step-item / § | 56 / 71 / 20 / 19 / 22 | OQ-1…OQ-6 (OQ-6 only as "No OQ-6 is minted"); P-68, 69, 70, 71, 72, 74, 75, 78 all rows of the ruling record; `syzygy-dov.17/.18/.20/.21/.26` exist with the roles given (`bd show`: .17 lane B draft, .18 registry act gate, .20 PWB-REQ-007 clarification gate, .21 this scenario's gate, .26 the three-surface package gate) | 0 |
| Line pointers | 33 | 33 — each read at source: spec 596–630, 448–450, 457–458, 906–910, 912–914, 439, 469, 470, 487, 615–619; M2 50, 130–131, 441, 443–446, 462–464, 472–475, 513; M3 903, 905–911, 914–916, 922, 935; M4 119, 820, 827–830, 836–839, 914 (`### Slice 6`), 1210, 1303–1312; RFC-0002 196, 201–205, 212; register 258 (RFC2-24), 260 (RFC2-26); POC 578–580, 589–590; template 57, 99–104, 111–112, 123; proposal 86–91; `model.ts` 41–42; `polaris.ts` 951–960 at `194f8cd` and `815785a`, 922–931 at `a4a3451`; `check_governance.py` 1537–1541, 1548–1552, 1557–1563, 1631–1638, 2022, 2236, 2371; `PROJECT-STATUS.md` 256–257; `governance-docs.yml` 124–128; ruling record 14–16, 58, 59, 63, 64, 66; OWNER-VALUES 79–80, 110–129; OPEN-QUESTIONS 33–35, 39–64 | 0 |

Total swept: **701**; not resolving: **0**; resolving with an imprecise
content claim: **2** (findings 46, 47).

**Quotation fidelity (criterion 1), every blockquote and inline quotation
read at source:** PWB-REQ-010 in full (delta 49–83 = spec 596–630, line for
line); PWB-REQ-007's aggregate sentence (448–450, the quoted sentences exact;
the blockquote starts and ends at sentence boundaries inside the cited
lines) and Observable (457–458, exact); PWB-REQ-020 (906–910, exact); the
proposed scenario (delta 125–139 = the patch's sixteen `+` lines less the
trailing blank, and = post-apply 621–635); M4 Q7 (119: the region sentence,
"builds the band container and owns its single ordering oracle", "own honest
target", the block-order reservation with its nested double marks — finding
42 repaired); M4 slice 3 (827–830, 836–839, exact); M4 Gate 5 cells ("None
found.", "Unavailable", "the three sweeps above find no requirement naming
the field" / "reaching the home route", "in place … which an opening
aggregate is not" at 1307–1309; eight rows 1305–1312; 41 approved
requirements and 55 scenarios = 17 + 24 and 31 + 24 by `### Requirement:` and
`#### Scenario:` counts); M2 (443–446 exact; 472–475 — finding 47; Q6 cell
50; success criterion 4 at 130–131; 462–464 "fall outside the enumerated
population entirely"); M3 (905–911, 914–916 exact; "A count with no member
rendered in place…" at 922); RFC2-26 (201–205 exact inside the clause
defined at 196; "Rows are per observable consequence, not per clause." at
212); POC-REQ-032 (578–580, Observable 589–590); the template's class table
(99–104), rule 2 (111–112), rule 6 (123), "I only touched X" (57); the
ruling record (P-71 arm and "What it means" at 58; head 14–16 — the
quotation closes before "in the shape of…" with the period outside the
marks; P-71-Q5 at 59; P-75 Q2 at 63; P-74 at 64 and P-78 at 66, plain
verbs); the owner's OQ answers (OWNER-VALUES 79–80 and 110–129;
OPEN-QUESTIONS 33–35, 39–64); the proposal's §Scope (86–91; "declared shape
of the configured project" occurs 0 times and is marked as a paraphrase). All
byte-exact where presented as quotations, with the punctuation exception of
finding 47. The OQ-1 sweep figures reproduce on M4's own predicates:
`(?i)\bhome\b` → 0 in the POC spec, 6 in the PWB spec (lines 247, 277, 510,
511, 518, 523); the backticked literal `surfaces` and `model.surfaces` → 0
in both (the bare word occurs 6 and 4 times, as M4 line 1183 itself says).

---

## Builder (commission item 5, criterion 10)

Run from the worktree root at `815785a`:

- `--check` → exit 0: "PWB opening-band scenario manifest matches 11
  proposed behavior subjects (2 patched, 9 unchanged); the proposed
  declaration equals its regeneration and the spec patch composes with the
  lane B spec patch in both orders".
- `--selftest` → exit 0: "selftest: closed population, byte drift, path
  order, subject drift, patch corruption, lane B composition (both orders
  and a corrupted case), generated-declaration tampering and the
  declaration-patch collision all fail closed".
- `--diff` → exit 0; `sha256` of its output `368ecc58…` equals `sha256` of
  `proposed/GOVERNING-DEPENDENCIES.md.patch` followed by
  `proposed/spec.md.patch` (`368ecc58…`) and differs from the reverse order
  (`193cf8ec…`) [Observed].
- Manifest semantics by hand: `sha256sum -c` over the eleven rows against
  the tree → 9 OK, exactly `GOVERNING-DEPENDENCIES.md` and `spec.md` FAILED;
  after `git apply` of both patches in a `git init` scratch tree those two
  hash to `86b1b49f…` and `9a44bdb6…`, the manifest's rows 5 and 11
  [Observed]. Post-apply: `### Requirement: PWB-REQ-010` 596, WhatsApp
  scenario 615, the new scenario 621, `warrants` fence 637, PWB-REQ-011 648.
  The spec patch removes no line (0 `-` lines outside the header); the
  declaration patch changes the digest line only, "17 requirement(s), 96
  distinct authorities" on both sides; "opening band" is absent from the
  spec patch (0 hits, case-insensitive); the current spec hashes to
  `42d073cd…`, the digest the declaration patch's `-` line carries.
- Manifest `sha256sum` → line 3 above.

**Mutations (rule 6), in a scratch copy holding `scripts/` in full, both
openspec change directories and the two candidate packages; baseline
`--check` and `--selftest` passing before and after; failure text read,
not the exit line; `diff -r` of the scratch package, `scripts/`, the change
directory and lane B against the worktree empty after every restore
(`__pycache__` excluded):**

| # | Mutation | Failure text |
|---|---|---|
| R9-M1 | flip the first hex char of the manifest's `spec.md` row | "manifest differs from exact regeneration over the proposed bytes" |
| R9-M2 | patch text "exactly one such aggregate" → "at most one such aggregate" | "proposed GOVERNING-DEPENDENCIES.md differs from regeneration over the proposed spec bytes" + "manifest differs …" |
| R9-M3 | add a twelfth file `EXTRA.md` to the change directory | **passes** — the documented non-failure, ledger 145–153 |
| R9-M4 | drift tree `spec.md` line 619 ("complete catalog" → "whole catalog") | "spec.md.patch does not apply to the base bytes: error: patch failed: …spec.md:618" |
| R9-M5 | swap manifest rows 8 and 9 | "manifest path population or order differs" |
| R9-M6 | declaration patch `+` line "96 distinct" → "97 distinct" | "proposed GOVERNING-DEPENDENCIES.md differs …" + "manifest differs …" |
| R9-M7 | remove lane B's `spec.md.patch` | "missing lane B spec patch: …pwb-scoped-attributes-amendment/proposed/spec.md.patch" |
| R9-M8 | append a line to unpatched `design.md` | "manifest differs from exact regeneration over the proposed bytes" |
| R9-M9 | delete `GOVERNING-DEPENDENCIES.md.patch` | "proposed/*.patch population differs from the declared patched subjects: spec.md.patch" + "declared patched subject is byte-identical: …GOVERNING-DEPENDENCIES.md" + the R9-M2 pair |
| R9-M10 | lane B's declaration patch, then this package's, by plain `git apply` | second apply fails "patch failed: …GOVERNING-DEPENDENCIES.md:8" — the collision delta 617–622 and ledger 295–299 describe |
| R9-M11 | alter the selftest's drift-fixture target line in the tree, then `--selftest` | selftest itself fails at `proposed_bytes()`: "spec.md.patch does not apply to the base bytes … :618" — it cannot run over drifted bytes |
| R9-M12 | swap the two patched rows' digests in the manifest (paths in order) | "manifest differs from exact regeneration over the proposed bytes" |
| R9-M13 | add a trailing space to lane B's first context line | "spec patches do not compose in the order spec.md.patch, spec.md.patch: … patch failed: …spec.md:450", reported for both orders |
| R9-M14 | rewrite `dependency_patches_collide()` to return `True` unconditionally, then `--selftest` | **passes** — observation (ii) above: a code mutation, outside rule 6's input-mutation scope |

Eleven fail closed with distinct, correct text; R9-M3 is the documented
non-failure; R9-M10 reproduces the documented collision; R9-M14 is a code
mutation and passes as a selftest must.

**Composition, independent of the builder:** this package's `spec.md.patch`
with each of the four sibling `proposed/spec.md.patch` files
(scoped-attributes `@@ -450,22 @@`/`-473,11`/`-907,23`; missing-currency
`@@ -469,3 @@`; machine-view `@@ -903,6 @@`; exact-source render-mode
`@@ -637,16 @@`/`-664,6`) via `git apply` on a clean copy of the current
spec, both orders: every pair applies both ways and yields one digest
(`de6516e4…`, `95918129…`, `55faf032…`, `14e01af3…`) [Observed]. Over the 31
directories under `contracts/candidates/`, no `proposed/*.patch` targets the
three-surface specification and only this package's four files name
`syzygy-dov.26` or `P-75`, so the ledger's "the second is not [drafted]"
(line 309) holds over that denominator [Observed].

**Governance battery:** `python3 scripts/check_governance.py` → "32 OK, 20
WARN, 0 FAIL (52 checks) — counts derived, not asserted"; CG-7d lists
"[subject] SIGN OFF PWB OPENING-BAND SCENARIO — 0 quotation(s), 0
finding(s), 0 performed digest(s)" and the packet as "[registered] …
declares 1 current and 0 performed-history act(s); 1 current, 0 historical
valid". `--selftest` → "263 fixtures, 0 failing". `PWB_SUCCESSOR_CHAIN`
(1631–1638) has three links and no opening-band link, matching the
withheld-link comment at 1537–1541; the battery lines sit at
`PROJECT-STATUS.md` 256–257 and the CI steps at `governance-docs.yml`
124–128 [Observed].

---

## Impact ledger re-derivation (commission item 5, criterion 9)

**Method.** Python `re` over every blob of `git ls-tree -r -z --name-only
a4a3451` read by `git show` (no checkout), decoded as UTF-8, undecodable
blobs skipped; the five patterns as the ledger states them, including its
regex `PWB-REQ-\d{3}(?:(?:/|,\s|\s)\d{3})*?(?:/|,\s|\s)010\b` and the
current source digest computed as sha256 of the `a4a3451:spec.md` blob
(prefix `42d073cd`). Second method: `git grep -l -F` / `-o -F` for the
literals and `-l -P` / `-o -P` for the regex at `a4a3451`. Denominator:
**1,334** tracked blobs [Observed].

| Figure | Ledger | Re-derived (`re`) | Second method |
|---|---|---|---|
| tracked files | 1,334 | 1,334 | 1,334 |
| undecodable | 4, the four PNGs | 4, the same four paths | — |
| NUL-carrying | 6 (four PNGs + two `.ts`) | 6, the same six paths (over 1,334; the ledger states it over 1,343) | — |
| `PWB-REQ-010` | 36 / 110 | 36 / 110 | 36 / 110, same file set |
| continuation forms | 6 / 7 | 6 / 7 | 6 / 7 |
| spec path | 51 / 113 | 51 / 113 | 51 / 113, same set |
| declaration path | 9 / 13 | 9 / 13 | 9 / 13, same set |
| current source digest | 13 / 13 | 13 / 13 | 13 / 13, same set |
| run-only adds | 5, named | the same 5 | — |
| both forms | `pwb-p4-2-mutation-sweep-2026-09-04.json` | same | — |
| citer union | 41 | 41 | — |

**Class 2 (9 files):** the nine unpatched manifest rows equal current bytes
(`sha256sum -c`, above). Literal carriers among the eleven rows at
`a4a3451`: `CAPABILITY-COVERAGE.md` ×1, `contract-coverage-matrix/
RFC-0007-0009.md` ×4, `GOVERNING-DEPENDENCIES.md` ×9, `spec.md` ×1; the
other seven 0; no row carries the run form [Observed]. R9-M3 confirms the
twelfth-file sentence.

**Class 3 (2 files):** both JSON declarations carry the current source
digest in `governingBehaviorContract.version` (prefixed `sha256:`) beside a
`signedBy` naming a pending exact owner act; neither carries `PWB-REQ-010`
(0 and 0) [Observed]. Labelled Observed for the pins and Inferred for the
repair's home in all three prose files.

**Class 4:** no `decisions/` act record and no `*-MANIFEST.txt` is in the
41-citer union (the one `decisions/` path in it is the pending register,
class 5) [Observed].

**Class 5 (39):** 41 less the two class-1 files = 39, each placed in
exactly one kind by path rule: implementation and tests 6, generated
coverage views 4, design packets 2, retained raws 11, dated evidence
records 12 (ten `docs/evidence/*.json` + two `docs/pursuits/2026-09-13-*.json`),
plan + dated review 2, pending register 1, other spec's design note 1 =
**39**, none unplaced, none twice [Observed].

**Branch population:** `59733d3` has 1,342 tracked files; `3ee1b0b` has
1,343 [Observed], matching ledger 34–35.

All figures reproduce by two methods.

---

## Disposition check — findings 1–45 (commission item 6)

Line numbers are the numbered dispositions at `815785a` (each found by
`^\s{0,4}N\. \*\*`; all 45 present, none missing).

| Finding | Round | Label | Disposition line | Checked at `815785a` |
|---|---|---|---|---|
| 1 | 1 | note | 695 | ledger 31–51 enumerates 4 skipped and 6 NUL; both reproduce |
| 2 | 1 | note | 704 | delta 419–428, packet 162–169; OQ-2 answered (A) at OWNER-VALUES 80, no byte moved |
| 3 | 1 | note | 711 | all three files cite the rows; "Q4" marked withdrawn |
| 4 | 2 | revise | 747 | ledger regex, 6/7, 41, 39 all reproduce |
| 5 | 2 | revise | 755 | ledger 145–153; R9-M3 confirms |
| 6 | 2 | note | 762 | delta 466–472 attributes to M2 line 50; M4 119 quotes it; exact |
| 7 | 2 | note | 770 | ledger 255–261, packet 291–295 dated notes; registration sites verified at 1548–1552, 2022, 2236, 2371, `PROJECT-STATUS.md` 256–257, workflow 124–128 |
| 8 | 2 | note | 775 | delta 647–649 names the brief; criteria byte-identical from `59733d3` |
| 9 | 2 | note | 778 | P-74/P-78 sentences exact at record 64/66 in all three files, no emphasis |
| 10 | 2 | note | 783 | packet 264–265 "may change" |
| A / B | B | non-blocking / editorial | 796–798 | same as 9; no change needed |
| 11 | 3 | revise | 842 | as 6 |
| 12 | 3 | note | 847 | no `**is**`/`**are**` in quotations; finding 41's three sites now also clean |
| 13 | 3 | revise | 850 | class 5 partitions to 39 (above) |
| 14 | 3 | revise | 859 | packet 12–40 names every round including 8 |
| 15 | 3 | note | 863 | packet 277–279 |
| 16 | 3 | note | 866 | ledger 301–313 "at the baseline commit", sibling named, composition re-derived |
| 17 | 3 | note | 871 | ledger 11–14 |
| 18 | 3 | note | 875 | delta 638 "Round 1 verdict:" |
| 19 | 4 | note | 909 | delta 583–595 names eight rounds and a round 9 |
| 20 | 4 | revise | 914 | ledger 199–209, 221–227; ×1 and ×4 re-swept |
| 21 | 4 | note | 926 | delta 262, 433–434; `gapReasonCounts` at 951 at `194f8cd` and `815785a`, 922 at `a4a3451` |
| 22 | 4 | note | 930 | 472 and 836 verified |
| 23 | 5 | revise | 969 | superseded wording marked; the current sentence true at every commit named (table above) |
| 24 | 5 | note | 977 | 201–205 inside 196; verified |
| 25 | 5 | note | 980 | 820–913; 914 is `### Slice 6` |
| 26 | 5 | note | 982 | 441–513, 443–446, 472–475 verified (finding 47 on the second's terminal punctuation) |
| 27 | 5 | note | 985 | delta 180–195, both readings quoted exactly at spec 912–914 and M2 462–464 |
| 28 | 5 | note | 993 | packet 3–7 names the act |
| 29 | 5 | note | 997 | delta 385–387 marked as paraphrase; 0 hits in `proposal.md` |
| 30 | 5 | note | 999 | battery CG-7e/CG-15 clean; the one 64-hex literal in prose is the package's own manifest digest (packet 53); no 7–16-hex-plus-ellipsis anywhere |
| 31 | 6 | revise | 1040 | population thirteen, three excepted, ten held — re-derived from the round-1 raw's sixteen item heads |
| 32 | 6 | note | 1050 | delta 261–264 "for OQ-3 below" |
| 33 | 6 | note | 1053 | delta 180–195 unchanged |
| 34 | 6 | note | 1056 | packet 9–11 |
| 35 | 6 | note | 1060 | M4 1303 heads the column `Limb 1`; the slice-3 cell opens "**Unavailable.**" |
| 36 | 7 | revise | 1105 | per-commit table above; superseded wording exact; the "included … one of three" repair true |
| 37 | 7 | note | 1116 | delta 1029–1031 verified against the round-6 raw's table |
| 38 | 7 | note | 1120 | delta 668–676 verified against both raws |
| 39 | 7 | note | 1124 | packet 309–320 verified against OWNER-VALUES §6 |
| 40 | 8 | note | 1169 | repaired at delta 1086–1093, predecessor exact; population attribution — finding 46 |
| 41 | 8 | note | 1180 | three sites clean (grep 0/0/0) |
| 42 | 8 | note | 1185 | M4's marks carried byte for byte |
| 43 | 8 | note | 1188 | packet 97–98, quotation marks dropped |
| 44 | 8 | note | 1192 | both sites repaired, predecessors exact, "+139 for all three" true |
| 45 | 8 | note | 1199 | bracket split re-read / re-run, each item's raw line verified |

Every finding 1–45 carries a numbered disposition whose stated repair is
present at the cited site and describes the diff truthfully. No disposition
claims more than the bytes show. The two "Author's standing" sentences and
the "What no round-8 disposition changed" sentence are true: the round-8
diff moves no patch byte, manifest row, requirement, scenario text, ledger
figure or owner answer.

---

## Per-criterion summary

| # | Criterion | Result |
|---|---|---|
| 1 | Quotation fidelity | **Pass with note 47** — every quotation's words byte-exact at its cited lines; the round-8 markup and nested-quote repairs are in; one quotation closes a source sentence early with a period the source does not carry |
| 2 | Change class | **Pass** — Normative under the template table (99–104) and rule 2 (111–112): a renderer with two opening aggregates, a tuple-less one, or a hoisted member complied before and does not now; argued from obligation |
| 3 | Scenario form | **Pass** — WHEN/THEN/AND at post-apply 621–635, after the existing scenario (615–619), before `warrants` (637); each clause falsifiable on a rendering or a machine answer; no clause states a value; heading carries none of PWB-REQ-012's six words |
| 4 | One category, no overlap | **Pass** — one hunk `@@ -618,6 +618,22 @@`; lane B's are 450, 473, 907; the P-69 Q7a sibling inserts at 469; no candidate patch targets the three-surface specification; composition with all four siblings verified in both orders |
| 5 | Reconciliation performed | **Pass** — three parties from M4 Q7 (119), each quoted from its own packet at verified lines, R-1/R-2/R-3 each tied to a scenario clause; P-75 Q2 exact at record 63; the packet's summary no longer presents a paraphrase as a quotation |
| 6 | Contradictions surfaced, not settled | **Pass** — OQ-1 to OQ-5 genuine, the easier reading named and not taken, each answered by plain direction 2026-09-23 with no proposed byte moved; the PWB-REQ-020 reading surfaced at item 3 in the same form |
| 7 | RFC2-26 | **Pass** — both halves hold against 196–221: limb 1 for slice 3 only, conditioned on OQ-2 (answered (A)); slices 4–5 unmapped on M4's own eight-row table (1308–1309), their sweeps reproduced, routed to `syzygy-dov.26` |
| 8 | What does not change | **Pass** — all eight items true against the patches: no requirement minted, `warrants` byte-identical (the patch removes no line), 17/96 unchanged, no implementation file, no observed-repository write (P-71-Q5 at record 59) |
| 9 | Impact ledger | **Pass in the ledger; note 46 in the delta's §Review** — every ledger figure reproduces by two methods over a stated denominator; class-3 labelling correct; the one note is a population attributed to the wrong round-1 item, with the claim over it true |
| 10 | Manifest and builder | **Pass** — eleven rows, two post-apply and nine current, verified by hand; nine predicates named; eleven mutations fail closed with correct text, R9-M3 passes as documented, R9-M10 reproduces the documented collision |
| 11 | Governance hygiene | **Pass** — no performed act argument or truncated signed digest in prose (the current source digest occurs only in the declaration patch's `-` line); act records cited by path; every "butler" code span is a Syzygy-internal path (nine, all under `.syzygy/` or `openspec/`; CG-1b clean); every head carries its candidate or inert banner naming the act; claims labelled (delta 10 Observed / 1 Inferred, ledger 12 / 3, packet 2 / 2, brief none needed); nothing labels the offering accepted, signed or adopted; signed change directory untouched (spec blob `543469dc…` unchanged since `59733d3`) |
| 12 | Scope of authority | **Pass** — nothing performs an act or schedules work; the scenario is conditional ("WHEN … renders an aggregate"), so a conforming implementation may render no opening aggregate; packet 75–78 says so; the owner's landing order is recorded as sequence only |

---

## Verdict rationale

**CONFIRM WITH EXCEPTIONS.** No sentence in the package is false at the
reviewed commit on the reading its own context fixes. Each of the six
round-8 notes is repaired at the site the disposition names, each repair's
new sentence is true — the eight blobs unchanged and the two commit-cited
files and two later records excepted (40); zero emphasis markers inside the
three quotations (41); M4's nested double marks carried (42); the packet's
paraphrase unquoted (43); +139 as the whole of `9d74185`'s delta covering
three registrations, and "included … one of three" (44); re-read for items 6
and 16, re-run for 7, 8 and 10 with the round-5 raw's lines (45) — and each
superseded fragment is quoted exactly against `git show 28086f6:<path>`. The
new round-8 section attributes to the round-8 raw only figures that raw
carries, and every count word in it derives from a population I re-derived.
The status heads, step-1 sentences, brief head and README row all say eight
rounds, the round-8 verdict word, six notes, and a round 9 next; the README
partition passes at 225/225. Every per-commit value in the round-1 §Review
paragraph is true at the commit named, read in the file at that commit at
seven commits. The bound bytes have the same blob ids at all twelve commits
from `59733d3` to `815785a`; the builder's three modes, thirteen scratch
mutations and the hand-reproduced collision behave as documented; every
ledger figure reproduces by two methods over 1,334 blobs; 701 extracted
pointers all resolve; and findings 1–45 are all dispositioned truthfully.
The two notes are: one population attributed to round-1 item 16, which names
seven of the eight files the sentence means (46 — the same copied-phrase
class as finding 40, and the reason a phrase should not yet be offered
without this one-word repair); and one quotation that ends a source sentence
early with its own period (47). Neither moves a figure, a patch byte, the
open questions or the scenario's conditional character, and neither reads as
performing an act or scheduling the band.
