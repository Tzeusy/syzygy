# Review — Polaris opening-band aggregate scenario package (round 10, fresh context)
Reviewed commit: 80c4b5200e4bb0a221a7c01f95826b7b4fa7af70
Manifest SHA-256: 7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context session, no authoring context (CC-REV-1). Read-only
against a detached worktree at the reviewed commit (`git worktree add
--detach … 80c4b52`); nothing under the repository's own working tree was
opened, edited or staged — the one exception is `bd show` on five bead ids,
a read of the tracker, not of the tree. Every mutation and every patch
composition ran in a copy under the session scratchpad, never in the
worktree. Inputs: the package in full (`SEMANTIC-DELTA.md` 1,280 lines,
`IMPACT-LEDGER.md` 313, `OWNER-DECISION-PACKET.md` 351, `REVIEW-BRIEF.md`
176, `PWB-OPENING-BAND-SCENARIO-MANIFEST.txt`, `proposed/spec.md.patch`,
`proposed/GOVERNING-DEPENDENCIES.md.patch`,
`scripts/build_pwb_opening_band_scenario.py`); the governing references the
brief names (the signed PWB specification at every cited range, POC-REQ-032,
RFC2-26 at its defined clause via `DIRECTIVE-REGISTER.md` line 260,
PWB-REQ-007/010/011/012/020); the ruling record's head and rows P-71,
P-71-Q5, P-74, P-75, P-78; the two 2026-09-23 owner-direction records; the
M2, M3 and M4 funnels at the cited lines; the semantic-delta template; and
the ten retained raws (rounds 1–9 and the parallel B) for disposition
checking only. `scripts/check_governance.py` was read at `59733d3`,
`3ee1b0b`, `9d74185`, `807cecf`, `d3d5d9d`, `28086f6`, `815785a` and
`80c4b52` by `git show`, never by inference (rule 4). The manifest digest on
line 3 was computed twice (`sha256sum` and Python `hashlib`), never
transcribed (rule 3); it equals the packet's copy (packet line 55) and line
3 of every one of the ten prior raws.

**Package bytes.** `git diff 815785a 80c4b52 -- <package> docs/README.md`
touches `SEMANTIC-DELTA.md`, `OWNER-DECISION-PACKET.md`, `REVIEW-BRIEF.md`
and `docs/README.md` only [Observed]. `git log 815785a..80c4b52` lists
**four** commits, not the three a reader of the commission would expect
(`c83f9a6`, `4c3716a`, `c6b2e32` and `80c4b52` itself); `git diff 815785a
c6b2e32` over the package, the builder and `docs/README.md` is empty, so the
three intervening commits touch nothing reviewed here [Observed]. Two of
them do touch files this package *cites*: `4c3716a` adds +41/−1 to
`scripts/check_governance.py` and `c83f9a6` adds a 32nd directory under
`contracts/candidates/` — both examined below; neither stales a package
sentence. The manifest, both patches and the builder have blob ids
`43b8adbd…`, `45b12133…`, `ceebdb53…` and `edbcd982…` at every one of the
thirteen commits `59733d3`, `3ee1b0b`, `9d74185`, `dfb605c`, `76b4beb`,
`194f8cd`, `7fd2db3`, `2c5745e`, `d3d5d9d`, `210b864`, `28086f6`, `815785a`
and `80c4b52` [Observed, `git rev-parse <commit>:<path>` at all thirteen];
`IMPACT-LEDGER.md` is blob `59417deb…` from `7fd2db3` through `80c4b52`.
`815785a` is an ancestor of `80c4b52`; `59733d3` is not (rebase-merge), so it
was compared by blob.

The verdict rests on no revise finding. One note (48) is recorded; it does
not make a sentence false on the reading its own context fixes. Both round-9
notes are repaired at the site their disposition names, each new sentence is
true, and each superseded fragment quotes its predecessor exactly against
`git show 815785a:<path>`. Nothing in the patches, the manifest or the
builder needs to move.

---

## Findings

Numbering continues from 47.

**Finding 48 — note. `SEMANTIC-DELTA.md` lines 1274–1275 (the round-9
section's "What no round-9 disposition changed"): "one wrapped code span at
the finding-36 marker".** Criterion 11; rule 8's spirit (a locator should
point at the thing).

- [Observed] The wrapped span is `git show` + `<commit>:scripts/check_governance.py`
  at delta lines 671–672, inside the round-1 §Review paragraph's evidence
  bracket ("[Observed: `git show … at `59733d3`, `9d74185`, `807cecf` and
  `d3d5d9d`, fixed-string grep for each anchor]"). It is the only
  odd-backtick non-fence line pair over the four prose files (2,120 lines,
  fences and the blockquoted `yaml` fence excluded). `git diff d3d5d9d
  28086f6` shows both lines as `+` and `git show d3d5d9d:<delta>` has 0 hits
  for the span, so it was written by the round-7 repair of finding 36, as
  the round-9 raw says ("pre-dates the round-8 repair").
- [Observed] This file uses "marker" for a superseded-wording note kept in
  place, and "the finding-36 marker" already has a referent: disposition 44
  (lines 1211–1212) says "the finding-36 marker says "included"", which is
  the sentence at lines 688–695 ("the third, the round-6 repair, said item
  15's pointers "moved to 2022, 2236 and 2371 …""). The wrapped span is not
  there; it is sixteen lines earlier in the same paragraph.
- [Inferred] A reader sent to the finding-36 marker finds no wrapped span
  and has to search the paragraph. The object is correctly identified (one
  span, `check_governance.py` whole on line 672, the basename sweep not
  defeated) and the disposition — leave it — is sound, so the sentence is
  imprecise rather than false. Note on that basis. Correct text: "one
  wrapped code span in the round-1 §Review paragraph's evidence bracket
  (delta 671–672, written by the round-7 repair)".

No other finding. Four observations that are not findings, each recorded so
the next reader need not re-derive it:

(i) The brief's "**Nine reviews have been run against this brief.**" (line
10) and the packet's "nine fresh-context reviews have run against
`REVIEW-BRIEF.md`" (line 12) count the numbered rounds; ten raws exist, and
the parallel B round (its raw's head: a "fresh-reader confirmation review …
over the bytes at the commit above, against" the brief) is named in the next
sentence of each paragraph. The same structure has stood since round 3
("Eight reviews" at `815785a` with nine files, passed by round 9 at its
item 3). Context fixes the reading; recorded, not a finding.

(ii) The round-9 raw's finding 46 cites round-1 item 11 at "raw line 65";
it is at line 85 (line 65 is item 9). The raw is uneditable (CC-REV-6) and
the delta's round-9 section does not copy the pointer — it names the item,
not the line — so nothing in the package inherits the slip.

(iii) `4c3716a` moved the `check_governance.py` anchors at `80c4b52`:
`def _act_subjects()` 2037, `ACT_DIGEST_COPY_FILES = {` 2253, the activation
comment naming `PWB-SCOPED-ATTRIBUTES-AMENDMENT-ACT.md` 2411 (file 8,141
lines). A fixed-string grep over the four prose files for every pointer the
delta has ever carried (1976/2173/2300, 2010/2222/2355, 2022/2236/2371,
1518–1523, 1548, 1552, 1537–1541, 1557–1563, 1631–1638) finds each one only
in a per-commit clause or a marked predecessor — no package sentence states
a current line of that file — so the +41 stales nothing. The round-9 raw's
own current-line pointers (1552, 1537–1541, 1631–1638) are true at
`815785a` and bound there.

(iv) `c83f9a6` added `polaris-edit-repair-deletion-scenario/` — 32
directories under `contracts/candidates/` now, not the 31 the round-9 raw
counted at `815785a`. Its `proposed/spec.md.patch` targets
`openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`,
not the PWB specification and not the three-surface specification, so the
PWB-spec sibling population is still four (composition below) and the
ledger's "the second is not [drafted]" (line 309) still holds: no
`proposed/*.patch` under any of the 32 targets the three-surface
specification, and only this package's four files name `syzygy-dov.26` or
`P-75` [Observed]. The delta's three "four sibling" sentences (905, 965,
1247) each attribute the count to a named round's raw and are true of it.

---

## The two round-9 notes, each repair checked (commission item 1)

| Round-9 note | Repair site at `80c4b52` | Predecessor at `815785a` (`git show`) | New sentence true? | Population stated? |
|---|---|---|---|---|
| 46 | delta 1093–1096 ("the eight sources the round-7 raw's item-16 row lists (round-1 items 11 and 16's sources; the round-8 repair wrote "round-1 item 16 names", a list of seven that omits the ruling record — round 9 finding 46) unchanged in blob since `59733d3`"); disposition 40's heading at 1180–1182 ("the eight sources its item-16 row lists") with its parenthetical at 1189–1193 | 1087: "eight sources round-1 item 16 names unchanged in blob since `59733d3`"; 1170–1172 heading "eight sources round-1 item 16 names" — the marked fragment "round-1 item 16 names" is exact at both | [Observed] Round-1 raw item 16 (lines 144–152) names seven files: the PWB spec (three ranges), RFC-0002, `DIRECTIVE-REGISTER.md`, M4, M2, M3, the POC spec — not the ruling record; item 11 (line 85, "**Owner ruling record**, read in full (102 lines)") is the ruling record; the round-7 raw's item-16 row (line 156) lists "(M2, M3, M4, RFC-0002, `DIRECTIVE-REGISTER.md`, both specs, the ruling record)" — eight. All eight have the same blob id at `59733d3`, `815785a` and `80c4b52` (M2 `a4c74249`, M3 `e7f493a7`, M4 `6f3482a2`, RFC-0002 `b3fe589e`, register `ad31b541`, PWB spec `543469dc`, POC spec `1280a62e`, ruling record `f7101da5`); the two files cited by commit differ (`polaris.ts` `87668005` → `800da823`; `check_governance.py` `603d3c2e` → `54f027ab` → `eddd39b0` at `80c4b52`); the two owner-direction records are absent at `59733d3` (`git rev-parse` fails). Every clause of the repaired sentence reproduces | Yes: the round-7 row (8) and round-1 items 11 + 16 (1 + 7), both named |
| 47 | delta 290–293 (the M2 blockquote now ends "…does not reach it, and RFC2-10's disclosure route is exactly what it is: a fact of the render."), with the recording sentence at 295–296 | 289–292: the blockquote ended "…complete-tuple requirement does not reach it." | [Observed] M2 lines 472–475 read, word for word, "**The probe's own freshness.** The probe claim carries no freshness value, before slice 5 and after it. It is not a project-shape claim, so PWB-REQ-007's complete-tuple requirement does not reach it, and RFC2-10's disclosure route is exactly what it is: a fact of the render." — the quotation is now the whole sentence, ending where M2's sentence ends (line 475, before "Its bracket"). The recording sentence's quoted predecessor ""does not reach it."" is exact. R-3's inline re-use (354–355) still closes before any punctuation and is exact against M2 473–474 | n/a (a quotation) |

`git diff 815785a 80c4b52` over the package is prose in three files;
`IMPACT-LEDGER.md`, both patches, the manifest and the builder are unchanged
(blob table in the head) [Observed]. Disposition 46's "at both sites" and
"The blob-unchanged claim holds over both the seven and the eight" are true
(table row 46); disposition 47's "the quotation now carries the rest of
M2's sentence, and a sentence beneath it records the earlier ending" and
"The delta's inline re-use in R-3 … was exact and is unchanged" are true
(row 47).

---

## The round-9 section of `SEMANTIC-DELTA.md` (1227–1280), every figure against the round-9 raw (commission item 2)

| Sentence at `80c4b52` | In the round-9 raw | Derived from |
|---|---|---|
| "commissioned 2026-09-23 with the nine earlier raws" (1231–1232) | raw 23–24: "the nine retained raws (rounds 1–8 and the parallel B)" | 8 + 1 = 9; `git ls-tree 815785a docs/reviews/` → 9 files matching `R-PWB-OPENING-BAND-SCENARIO-DELTA-*`; the raw's commit `80c4b52` is dated 2026-09-23 08:51 +0800 |
| "asked to check each round-8 repair at its site against `git show 28086f6`, every figure the round-8 section attributes to the round-8 raw, every per-commit claim at the commit named, and every count word against a stated population" (1233–1236) | raw section heads "commission item 1" (111), "item 2" (128), "item 4" (185); raw 150 "Every number word in the round-8 section derives from a stated population" | — |
| "found every round-8 note repaired at the site its disposition names, each new sentence true and each superseded fragment quoting its predecessor exactly" (1241–1243) | raw 47–49 | — |
| "read the per-commit anchors at seven commits from `59733d3` to `815785a`" (1243) | raw 25–26 names seven; table 191–199 has seven rows | seven, listed; my own read at those seven plus `80c4b52` reproduces every value (table below) |
| "the bound files' blob ids at twelve" (1243) | raw 37–40 lists twelve commits | reproduced at all twelve plus `80c4b52` (head) |
| "ran the builder's three modes and thirteen scratch mutations" (1244–1245) | raw 292–303 (three modes); raw 527–528 "thirteen scratch mutations and the hand-reproduced collision"; table 324–339 has R9-M1…R9-M14, of which R9-M10 is the by-hand `git apply` | 14 rows − 1 by-hand = 13, the raw's own figure |
| "reproduced every ledger figure by two methods over 1,334 blobs" (1245–1246) | raw 378–379, 422 | re-derived below |
| "resolved 701 extracted pointers over 2,043 lines with none unresolved" (1246–1247) | raw 234 (2,043 lines), 238 (701 matches), 250 (0 not resolving) | 1,211 + 313 + 346 + 173 = 2,043 at `815785a` [Observed, `wc -l` on `git show 815785a:<path>`] |
| "composed the spec patch with all four sibling patches in both orders" (1247–1248) | raw 345–351 names four siblings | four, and still four at `80c4b52` (observation iv) |
| "findings 1 to 45 dispositioned truthfully" (1248–1249) | raw 426–485 | — |
| "no revise finding; findings 46 and 47 are notes" (1249–1250) | raw 46 | — |
| "the round-9 CONFIRM WITH EXCEPTIONS is bound to `815785a` alone" (1253) | raw lines 2 and 4 | — |
| "The two non-finding observations in the raw (one wrapped code span …, and a builder-code mutation outside rule 6's input scope)" (1274–1276) | raw 97–107, (i) and (ii) | finding 48 on the locator; the substance is the raw's |
| Dispositions 46–47 (1258–1270) | each repair verified in the table above | — |

Every number word in the round-9 section derives from a stated population.

---

## Status heads, step-1 sentences, brief head, README row (commission item 3)

- Delta step 1 (587–601): "Done nine times", the nine rounds with their
  commits and verdict words, "round 9, over `815785a`, CONFIRM WITH
  EXCEPTIONS (two notes, no revise finding)", "A round 10 over these bytes is
  the next step" [Observed — each verdict word equals line 4 of its raw;
  each commit is the one its raw names on line 2].
- Packet head (12–42): nine rounds and the parallel round, each with its
  raw's filename and verdict word copied exactly; "await a round 10 — the
  round-8 and round-9 confirmations cover `28086f6` and `815785a`, and their
  six and two notes were repaired in prose after each" [Observed, true: the
  two repairs are the diff]. Packet step 1 (242–268): "Done nine times",
  round 9 "no revise finding, two notes, both repaired in prose", "a round
  10 over these bytes is the next step" [Observed; dispositions 46 and 47
  are both "Accepted and repaired"].
- Brief head (10–42): "Nine reviews have been run against this brief",
  round 9 sentence with its raw's filename [Observed; observation (i)]. Its
  "What the reviewer receives" and "Criteria" sections are byte-identical
  to `59733d3` [Observed].
- `docs/README.md` line 84: P-71 row count **10**; `ls
  docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-*` → 10 files; `git
  ls-files docs/reviews | wc -l` → 226 [Observed]. Line 93: "226 files, 226
  assigned"; `python3 scripts/check_docs_review_campaign_partition.py --check
  docs/README.md` from the worktree root → "second-method PASS: git
  ls-files=226; git ls-tree=226; exact path sets equal" and "partition PASS:
  denominator=226; assigned=226; raw=201; other=25; unmatched=0; overlaps=0;
  campaigns=50", exit 0 [Observed]. The row's text — ninth sequential review
  CONFIRM WITH EXCEPTIONS at `…-CONFIRMATION-8-RAW.md:4` (line 4 of that
  file is its verdict line), two notes, no revise finding, after round 8's
  with six, awaits a round 10 — is true.

---

## The item-15 anchors, per commit (commission item 4; rule 4: read at each commit, never inferred)

`git show <commit>:scripts/check_governance.py`, fixed-string grep for each
anchor; lane B constants are lines 1518–1523 at every commit and the
six-line block hashes identically (`92ab81fa…`) at all eight.

| Commit | File lines | `def _act_subjects()` | `ACT_DIGEST_COPY_FILES = {` | activation comment naming `PWB-SCOPED-ATTRIBUTES-AMENDMENT-ACT.md` | `PWB_OPENING_BAND_LABEL =` | `PWB_MISSING_CURRENCY_LABEL =` | blob |
|---|---|---|---|---|---|---|---|
| `59733d3` | 7,936 | 1976 | 2173 | 2300 | absent | absent | `603d3c2e` |
| `3ee1b0b` | 7,936 | 1976 | 2173 | 2300 | absent | absent | `603d3c2e` |
| `9d74185` (+139/−0) | 8,075 | 2010 | 2222 | 2355 | 1548 | absent | `c4e8e838` |
| `807cecf` (+28/−2) | 8,101 | 2022 | 2236 | 2371 | 1548 | 1557 | `54f027ab` |
| `d3d5d9d` | 8,101 | 2022 | 2236 | 2371 | 1548 | 1557 | `54f027ab` |
| `28086f6` | 8,101 | 2022 | 2236 | 2371 | 1548 | 1557 | `54f027ab` |
| `815785a` | 8,101 | 2022 | 2236 | 2371 | 1548 | 1557 | `54f027ab` |
| `80c4b52` (+41/−1 at `4c3716a`) | 8,141 | 2037 | 2253 | 2411 | 1548 | 1557 | `eddd39b0` |

`git log a4a3451..80c4b52 -- scripts/check_governance.py` names exactly
`9d74185`, `807cecf` and `4c3716a`; the file's blob is identical at `a4a3451`
and `59733d3`, so "pre-date this draft and never moved" holds for the lane B
constants [Observed]. Every per-commit clause of the round-1 §Review
paragraph (delta 659–697) — 1976/2173/2300 at `59733d3`; 2010/2222/2355 at
`9d74185` beside two siblings' registrations, +139 for all three;
2022/2236/2371 at `807cecf`, +26; the evidence bracket's four commits;
"included this package's registration … one of three" — is true at the
commit named [Observed]. No clause claims a value at `80c4b52`, where the
values have moved again (observation iii).

**The three superseded-wording markers and the packet's superseded
recommendation** re-checked at `80c4b52` against `git show`: delta 683
"still hold at this commit" ↔ `7fd2db3`; delta 685–686 "two of the
fourteen" / "the other twelve hold" ↔ `2c5745e`; delta 688–689 "moved to
2022, 2236 and 2371 when the lane B registration landed at `9d74185`" ↔
`d3d5d9d` (joined across the wrap); packet 322–324 "Recommended after lane
B, matching P-68's ordering and this package's separate gate bead; the owner
may say otherwise [Inferred]" ↔ `d3d5d9d` — all exact and unchanged since
round 9 [Observed]. The packet's §6 paragraph (314–325) against OWNER-VALUES
line 114 ("Readiness order, lane B last (Recommended)") and 128 ("superseded
by this answer, not edited") paraphrases without quotation marks and quotes
only its own predecessor, exactly [Observed].

---

## Internal cross-reference sweep (commission item 5)

**Method and denominator.** Python `re` over the four prose files
(`SEMANTIC-DELTA.md` 1,280 lines, `IMPACT-LEDGER.md` 313,
`OWNER-DECISION-PACKET.md` 351, `REVIEW-BRIEF.md` 176 — **2,120 lines**)
extracting every backticked path token with a file extension, backticked
seven-hex commit token, `finding N` (with its continuation forms), `round
N`, `OQ-N`, `P-NN`, and backticked bead id: **662 matches**, over-inclusive
by design; line pointers (33 distinct targets) were read separately, each
at source, and are listed under quotation fidelity. Every match resolved
against its target at `80c4b52`.

| Category | Matches | Resolve | Do not resolve |
|---|---|---|---|
| Path tokens | 248 | all are tracked files, tracked basenames, package-relative files, the future `PWB-OPENING-BAND-SCENARIO-ACT.md` (a constant in `check_governance.py`) or the brief's `-RAW.md` suffix pattern | 2 by design: the globs `docs/evidence/*.json` and `docs/pursuits/2026-09-13-*.json` in the ledger |
| Commit tokens | 102 (13 distinct) | 13 — `59733d3`, `3ee1b0b`, `9d74185`, `dfb605c`, `76b4beb`, `194f8cd`, `7fd2db3`, `2c5745e`, `d3d5d9d`, `807cecf`, `28086f6`, `815785a`, `a4a3451` all `git cat-file -e` as commits | 0 |
| Finding numbers | 63 | all in 1–47; the delta carries a numbered disposition for every one of 1–47 (`^\s{0,4}N\. \*\*`, none missing) | 0 |
| Round words | 102 | all in 1–10; "round 10" occurs only as the next step | 0 |
| OQ / P-row / bead | 56 / 71 / 20 | OQ-1…OQ-6 (OQ-6 only as "No OQ-6 is minted"); P-68, 69, 70, 71, 72, 74, 75, 78 all rows of the ruling record; `syzygy-dov.17/.18/.20/.21/.26` exist with the roles given (`bd show`: .17 lane B draft, in progress; .18 registry act gate; .20 PWB-REQ-007 clarification gate; .21 this scenario's gate, open; .26 the three-surface package gate, open) | 0 |

Total swept: **662**; not resolving: **0** (the two globs excepted);
resolving with an imprecise content claim: **1** (finding 48).

**Quotation fidelity (criterion 1), every blockquote and inline quotation
read at source:** PWB-REQ-010 in full (delta 49–83 = spec 596–630, line for
line); PWB-REQ-007's aggregate sentence (448–450, the quoted sentence exact
at sentence boundaries inside the cited lines) and Observable (457–458,
exact); PWB-REQ-020 (906–910, exact); the Case phrase at 912–914; the
proposed scenario (delta 125–139 = the patch's `+` lines less the trailing
blank, and = post-apply 621–635); M4 Q7 (119: the region sentence, "builds
the band container and owns its single ordering oracle", "own honest
target", the block-order reservation with its nested double marks); M4
slice 3 (827–830, 836–839, exact); M4 Gate 5 cells ("None found.",
"Unavailable", both "the three sweeps above …" sentences, "which an opening
aggregate is not"); M2 (443–446 exact; 472–475 now the whole sentence —
finding 47 repaired; Q6 cell 50; success criterion 4 at 130–131; 462–464
"fall outside the enumerated population entirely"); M3 (905–911, 914–916
exact; "A count with no member rendered in place…" at 922); RFC2-26
(201–205 exact inside the clause defined at 196; "Rows are per observable
consequence, not per clause." at 212); `DIRECTIVE-REGISTER.md` 260 defines
RFC2-26 at that file; POC-REQ-032 (578–580, Observable 589–590); the
template's class table (99–104), rule 2 (111–112: "Class is determined by
what changes in the obligation, never by diff size."), rule 6 (123), "I only
touched X" (57); the ruling record (P-71 arm and "What it means"; head
14–16, the quotation closing before "in the shape of…"; P-74 and P-78
closing sentences; P-75 Q2 "PWB-REQ-007 reaches only the project-shape
plane"); the owner's OQ answers (OWNER-VALUES 79–80: OQ-1 "Fold into dov.26
package", OQ-2 "(A) Under PWB-REQ-010"; 114 and 128; OPEN-QUESTIONS 33–35
and 39–58: OQ-3 "Keep clause; code adds secondary", OQ-4 "Clarify inside
.26", OQ-5 "Account first, then band"); the proposal's §Scope (86–91, marked
as a paraphrase); `gapReasonCounts` at `polaris.ts` 951 at `194f8cd` and
`80c4b52`, 922 at `a4a3451`, reading `reasons.primary`; `PocEpistemic`'s
Unknown arm at `model.ts` 41–42 carrying `reason` only. All byte-exact where
presented as quotations.

---

## Builder (commission item 5, criterion 10)

Run from the worktree root at `80c4b52`:

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
  hash to `9a44bdb6…` and `86b1b49f…`, the manifest's rows 11 and 5
  [Observed]. Post-apply: `### Requirement: PWB-REQ-010` 596, WhatsApp
  scenario 615, the new scenario 621, `warrants` fence 637, PWB-REQ-011 648.
  The spec patch removes no line (0 `-` lines outside the header); the
  declaration patch changes the digest line only, "17 requirement(s), 96
  distinct authorities" on both sides; "opening band" is absent from the
  spec patch (0 hits, case-insensitive).
- Manifest `sha256sum` and `hashlib` → line 3 above.

**Mutations (rule 6), in a scratch copy holding `scripts/` in full, both
openspec change directories (the PWB change and the three-surface change,
which the declaration generator reads to resolve qualified parent
requirements) and the two candidate packages; baseline `--check` and
`--selftest` passing before and after; failure text read, not the exit
line; `diff -r` of the scratch copy against its pristine twin empty after
every restore (`__pycache__` and `.git` excluded):**

| # | Mutation | Failure text |
|---|---|---|
| R10-M1 | flip the first hex char of the manifest's `spec.md` row | "manifest differs from exact regeneration over the proposed bytes" |
| R10-M2 | patch text "exactly one such aggregate" → "at most one such aggregate" | "proposed GOVERNING-DEPENDENCIES.md differs from regeneration over the proposed spec bytes" + "manifest differs …" |
| R10-M3 | add a twelfth file `EXTRA.md` to the change directory | **passes** — the documented non-failure, ledger 145–153 |
| R10-M4 | drift tree `spec.md` line 619 ("complete catalog" → "whole catalog") | "spec.md.patch does not apply to the base bytes: error: patch failed: …spec.md:618" |
| R10-M5 | swap manifest rows 8 and 9 | "manifest path population or order differs" |
| R10-M6 | declaration patch `+` line "96 distinct" → "97 distinct" | "proposed GOVERNING-DEPENDENCIES.md differs …" + "manifest differs …" |
| R10-M7 | remove lane B's `spec.md.patch` | "missing lane B spec patch: …pwb-scoped-attributes-amendment/proposed/spec.md.patch" |
| R10-M8 | append a line to unpatched `design.md` | "manifest differs from exact regeneration over the proposed bytes" |
| R10-M9 | delete `GOVERNING-DEPENDENCIES.md.patch` | "proposed/*.patch population differs from the declared patched subjects: spec.md.patch" + "declared patched subject is byte-identical: …GOVERNING-DEPENDENCIES.md" + the R10-M2 pair |
| R10-M10 | append a newline to unpatched `.openspec.yaml` | "manifest differs from exact regeneration over the proposed bytes" |
| R10-M11 | change PWB-REQ-010's `primary: RFC7-1` to `RFC7-2` in the tree spec | "spec.md.patch does not apply to the base bytes … :618" — the patch's context reaches the `warrants` fence, so a warrant edit under the host requirement is caught as drift before regeneration |
| R10-M12 | add a trailing space to lane B's first context line | "spec patches do not compose in the order spec.md.patch, spec.md.patch: … patch failed: …spec.md:450", reported for both orders |
| R10-M13 | rename `spec.md.patch` → `spec2.md.patch` | "proposed/*.patch population differs from the declared patched subjects: GOVERNING-DEPENDENCIES.md.patch, spec2.md.patch" + both composition orders "can't open patch" |
| R10-M14 | declaration patch `+` digest one hex off | "proposed GOVERNING-DEPENDENCIES.md differs …" + "manifest differs …" |
| R10-M15 | delete lane B's declaration patch, then `--selftest` | "SELFTEST FAILED: the declaration patches no longer collide; the packet's regeneration note must be re-derived" |
| R10-M16 | lane B's declaration patch, then this package's, by plain `git apply` | second apply fails "patch failed: …GOVERNING-DEPENDENCIES.md:8" — the collision delta 623–628 and ledger 295–299 describe |

Fourteen fail closed with distinct, correct text (M1, M2, M4–M15); R10-M3
is the documented non-failure; R10-M16 reproduces the documented collision.

**Composition, independent of the builder:** this package's `spec.md.patch`
with each of the four sibling `proposed/spec.md.patch` files that target
the PWB specification (scoped-attributes `@@ -450,22`/`-473,11`/`-907,23`;
missing-currency `@@ -469,3`; machine-view `@@ -903,6`; exact-source
render-mode `@@ -637,16`/`-664,6`) via `git apply` on a clean copy of the
current spec, both orders: every pair applies both ways and yields one
digest (`de6516e4…`, `95918129…`, `55faf032…`, `14e01af3…`), the same four
digests the round-9 raw reports [Observed]. The fifth candidate patch added
at `c83f9a6` targets a different specification (observation iv).

**Governance battery:** `python3 scripts/check_governance.py` → "32 OK, 20
WARN, 0 FAIL (52 checks) — counts derived, not asserted"; CG-7d lists
"[subject] SIGN OFF PWB OPENING-BAND SCENARIO — 0 quotation(s), 0
finding(s), 0 performed digest(s)" and the packet as "[registered] …
declares 1 current and 0 performed-history act(s); 1 current, 0 historical
valid". `--selftest` → "263 fixtures, 0 failing" [Observed].

---

## Impact ledger re-derivation (commission item 5, criterion 9)

**Method.** Python `re` over every blob of `git ls-tree -r -z --name-only
a4a3451` read by `git show` (no checkout), decoded as UTF-8, undecodable
blobs skipped; the five patterns as the ledger states them, including its
regex `PWB-REQ-\d{3}(?:(?:/|,\s|\s)\d{3})*?(?:/|,\s|\s)010\b` and the
current source digest computed as sha256 of the `a4a3451:spec.md` blob
(prefix `42d073cd`, the digest the declaration patch's `-` line carries).
Second method: `git grep -l -F` / `-o -F` for the literals and `-l -P` /
`-o -P` for the regex at `a4a3451`. Denominator: **1,334** tracked blobs
[Observed].

| Figure | Ledger | Re-derived (`re`) | Second method |
|---|---|---|---|
| tracked files | 1,334 | 1,334 | 1,334 |
| undecodable | 4, the four PNGs | 4, the same four paths | — |
| NUL-carrying | 6 (four PNGs + two `.ts`) | 6, the same six paths (over 1,334; the ledger states it over 1,343) | — |
| `PWB-REQ-010` | 36 / 110 | 36 / 110 | 36 / 110, same file set |
| continuation forms | 6 / 7 | 6 / 7 | 6 / 7, same set |
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
other seven 0 [Observed]. R10-M3 confirms the twelfth-file sentence.

**Class 3 (2 files):** both JSON declarations carry the current source
digest in `governingBehaviorContract.version` beside a `signedBy`; neither
carries `PWB-REQ-010` (0 and 0) [Observed]. Labelled Observed for the pins
and Inferred for the repair's home in all three prose files.

**Class 4:** no `decisions/` act record and no `*-MANIFEST.txt` is in the
41-citer union (the one `decisions/` path in it is the pending register,
class 5) [Observed].

**Class 5 (39):** 41 less the two class-1 files = 39, each placed in
exactly one kind by path rule: implementation and tests 6, generated
coverage views 4, design packets 2, retained raws 11 (one via the run form
only), dated evidence records 12 (ten `docs/evidence/*.json`, three via the
run form only, + two `docs/pursuits/2026-09-13-*.json`), plan + dated
review 2, pending register 1, other spec's design note 1 = **39**, none
unplaced, none twice [Observed].

**Branch population:** `59733d3` has 1,342 tracked files; `3ee1b0b` has
1,343 [Observed], matching ledger 34–35.

All figures reproduce by two methods.

---

## Disposition check — findings 1–47 (commission item 6)

Line numbers are the numbered dispositions at `80c4b52` (each found by
`^\s{0,4}N\. \*\*`; all 47 present, none missing). Findings 1–45 were
re-checked at the sites the round-9 raw's table names, shifted by the
round-9 repair's line movement (+4 in the reconciliation section, +6 to +69
in §Review); every stated repair is present at its site and describes the
diff truthfully — the round-9 raw's per-finding evidence reproduces at
`80c4b52` since the only bytes that moved between `815785a` and `80c4b52`
are the two round-9 repairs, the status sentences and the new round-9
section [Observed, the diff]. In particular:

| Finding | Round | Label | Disposition line | Checked at `80c4b52` |
|---|---|---|---|---|
| 1–3 | 1 | notes | 701, 710, 717 | ledger 31–51; delta 423–432 and packet 164–171; "Q4" withdrawn in all three files |
| 4–10 | 2 | 2 revise, 5 notes | 753–790 | ledger regex and figures reproduce (table above); ledger 145–153 (R10-M3); M2 line 50; dated notes at ledger 255–261 and packet 296–300; brief named at delta 653–655; P-74/P-78 exact at record; packet 269–270 "may change" |
| A / B | B | non-blocking / editorial | 801–803 | same as 9; no change needed |
| 11–18 | 3 | 3 revise, 5 notes | 848–883 | M2 attribution; no emphasis in quotations; class 5 partitions to 39; packet head names every round; packet 282–284; ledger 301–313; ledger 11–14; delta 644 "Round 1 verdict:" |
| 19–22 | 4 | 1 revise, 3 notes | 915–940 | delta step 1 names nine rounds and a round 10; ledger 199–209, 221–227 (×1 and ×4 re-swept); `gapReasonCounts` at 951 / 922; 472 and 836 |
| 23–30 | 5 | 1 revise, 7 notes | 975–1009 | superseded wording marked at 683; 201–205 inside 196; 820–913; 441–513 with 443–446 and 472–475 (finding 47 repaired); delta 180–195; packet 3–7; delta 385–391 paraphrase; CG-7e/CG-15 clean |
| 31–35 | 6 | 1 revise, 4 notes | 1046–1070 | population thirteen; delta 261–264 "for OQ-3 below"; delta 180–195; packet 9–11; M4 1303 |
| 36–39 | 7 | 1 revise, 3 notes | 1114–1136 | per-commit table above; delta 1035–1037; delta 674–682; packet 314–325 |
| 40–45 | 8 | notes | 1179–1218 | 40 repaired at 1093–1096 with the round-9 attribution repair on top; 41 three sites clean (`**first**` 0, `**exactly one**` 0); 42 M4's marks; 43 packet 99–100; 44 delta 665–669 and 690–695; 45 delta 674–682 |
| 46–47 | 9 | notes | 1257, 1266 | table in "The two round-9 notes" above |

Every finding 1–47 carries a numbered disposition whose stated repair is
present at the cited site and describes the diff truthfully. No disposition
claims more than the bytes show. The "Author's standing" sentences and the
"What no round-9 disposition changed" sentence are true in substance: the
round-9 diff moves no patch byte, manifest row, requirement, scenario text,
ledger figure or owner answer (finding 48 is the locator inside that
sentence, not its substance).

---

## Per-criterion summary

| # | Criterion | Result |
|---|---|---|
| 1 | Quotation fidelity | **Pass** — every quotation byte-exact at its cited lines, the round-9 M2 repair included; the one quotation round 9 noted now carries M2's whole sentence |
| 2 | Change class | **Pass** — Normative under the template table (99–104) and rule 2 (111–112); argued from obligation |
| 3 | Scenario form | **Pass** — WHEN/THEN/AND at post-apply 621–635, after the existing scenario (615–619), before `warrants` (637); each clause falsifiable on a rendering or a machine answer; heading carries none of PWB-REQ-012's six words |
| 4 | One category, no overlap | **Pass** — one hunk `@@ -618,6 +618,22 @@`; lane B's are 450, 473, 907; the P-69 Q7a sibling inserts at 469; no candidate patch targets the three-surface specification (32 directories swept); composition with all four PWB-spec siblings verified in both orders |
| 5 | Reconciliation performed | **Pass** — three parties from M4 Q7 (119), each quoted from its own packet at verified lines, R-1/R-2/R-3 each tied to a scenario clause; P-75 Q2 exact |
| 6 | Contradictions surfaced, not settled | **Pass** — OQ-1 to OQ-5 genuine, the easier reading named and not taken, each answered by plain direction 2026-09-23 with no proposed byte moved |
| 7 | RFC2-26 | **Pass** — both halves hold against 196–221: limb 1 for slice 3 only, conditioned on OQ-2 (answered (A)); slices 4–5 unmapped on M4's own table, routed to `syzygy-dov.26` |
| 8 | What does not change | **Pass** — all eight items true against the patches: no requirement minted, `warrants` byte-identical (the patch removes no line), 17/96 unchanged, no implementation file, no observed-repository write |
| 9 | Impact ledger | **Pass** — every ledger figure reproduces by two methods over a stated denominator; class-3 labelling correct; the round-9 population attribution is repaired |
| 10 | Manifest and builder | **Pass** — eleven rows, two post-apply and nine current, verified by hand; fourteen mutations fail closed with correct text, R10-M3 passes as documented, R10-M16 reproduces the documented collision |
| 11 | Governance hygiene | **Pass with note 48** — no performed act argument or truncated signed digest in prose; act records cited by path; every code span containing "butler" is a Syzygy-internal path (CG-1b clean); every head carries its candidate or inert banner naming the act; claims labelled (delta 10 Observed / 1 Inferred, ledger 12 / 3, packet 2 / 2, brief none needed); nothing labels the offering accepted, signed or adopted; signed change directory untouched (spec blob `543469dc…` unchanged since `59733d3`); one locator in the new section points at the wrong sentence of the right paragraph |
| 12 | Scope of authority | **Pass** — nothing performs an act or schedules work; the scenario is conditional ("WHEN … renders an aggregate"), so a conforming implementation may render no opening aggregate; packet 77–80 says so |

---

## Verdict rationale

**CONFIRM WITH EXCEPTIONS.** No sentence in the package is false at the
reviewed commit on the reading its own context fixes. Both round-9 notes
are repaired at the site the disposition names — the eight unchanged
sources now attributed to the round-7 raw's row and to round-1 items 11 and
16 together, the seven-file list marked as the superseded attribution, the
blob claim true over both populations (46); the M2 quotation carried to the
end of its sentence, byte-exact against lines 472–475, with the earlier
ending recorded beneath it (47) — and each superseded fragment is quoted
exactly against `git show 815785a:<path>`. The new round-9 section
attributes to the round-9 raw only figures that raw carries, and every count
word in it derives from a population I re-derived. The status heads, step-1
sentences, brief head and README row all say nine rounds, the round-9
verdict word, two notes, and a round 10 next; the README partition passes at
226/226 and the row count equals the ten retained raws. Every per-commit
value in the round-1 §Review paragraph is true at the commit named, read in
the file at eight commits, and no package sentence claims a current value of
a file that moved again at `80c4b52`. The bound bytes have the same blob ids
at all thirteen commits from `59733d3` to `80c4b52`; the builder's three
modes, sixteen scratch mutations and the hand-reproduced collision behave as
documented; every ledger figure reproduces by two methods over 1,334 blobs;
662 extracted pointers and 33 line-pointer targets all resolve; and findings
1–47 are all dispositioned truthfully. The one note is a locator in the
round-9 section's closing sentence that names "the finding-36 marker" for a
wrapped code span that sits sixteen lines earlier in the same paragraph, in
the evidence bracket the finding-36 repair wrote (48). It moves no figure,
no patch byte, no open question and no verdict word, and it does not read as
performing an act or scheduling the band; whether it must be repaired before
a phrase is offered, or recorded beside the offering as this verdict's one
exception, is the owner's call — on these bytes the package may go to the
owner with note 48 recorded beside it.
