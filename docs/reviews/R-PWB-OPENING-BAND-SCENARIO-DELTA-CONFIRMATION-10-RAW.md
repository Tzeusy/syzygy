# Review — Polaris opening-band aggregate scenario package (round 11, fresh context)
Reviewed commit: 9162d622d67e3cba17c9691a5f19c3a8e4d2eded
Manifest SHA-256: 7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context session, no authoring context (CC-REV-1). Read-only
against a detached worktree at the reviewed commit (`git worktree add
--detach … 9162d62`); nothing under the repository's own working tree was
opened, edited or staged, with two tracker/remote reads outside the tree
(`bd show syzygy-dov.21`; `gh pr view 116`). Every mutation and every patch
composition ran in a `git archive` copy under the session scratchpad with a
pristine twin, `diff -r` empty after every restore; never in the worktree.
Inputs: the package in full (`SEMANTIC-DELTA.md` 1,347 lines,
`IMPACT-LEDGER.md` 313, `OWNER-DECISION-PACKET.md` 359, `REVIEW-BRIEF.md`
179, `PWB-OPENING-BAND-SCENARIO-MANIFEST.txt`, `proposed/spec.md.patch`,
`proposed/GOVERNING-DEPENDENCIES.md.patch`,
`scripts/build_pwb_opening_band_scenario.py`); the governing references the
brief names, each read at its cited lines; the ruling record's head and rows
P-71, P-71-Q5, P-74, P-75, P-78; the two 2026-09-23 owner-direction records;
the owner's 2026-09-26 sitting record
`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
(read from the PR #116 branch; `gh pr view 116` reports the PR merged at
2026-09-26T03:32Z with head `3ac3448`, and the record's commit is `68505fb`
— the record is not in the reviewed commit's tree); the M2, M3 and M4
funnels at the cited lines; the semantic-delta template; and the eleven
retained raws (rounds 1–10 and the parallel B) for disposition checking only.
`scripts/check_governance.py` was read at `59733d3`, `3ee1b0b`, `9d74185`,
`807cecf`, `d3d5d9d`, `28086f6`, `815785a`, `80c4b52` and `9162d62` by `git
show` through a Python wrapper, never by inference (rule 4). The manifest
digest on line 3 was computed twice (`sha256sum` and Python `hashlib`), never
transcribed (rule 3); it equals the packet's copy (packet line 60) and line 3
of every one of the eleven prior raws.

**The reading this verdict is written on.** The owner's 2026-09-26 record,
item 1, rules that a confirmation round with no revise-severity finding
clears the exact bytes it read, that its notes are dispositioned in a record
beside the package and never by editing it, and that an exception the owner
has already ruled on counts as dispositioned by that ruling; item 2 takes the
wider reading of PWB-REQ-020's "and disclosure", settling round-5 finding 27.
So the package will not be edited after this round. REVISE below would mean
a sentence false on the reading its own context fixes, or a proposed byte
that must change. Nothing rises to that. Four notes (49–52) are recorded;
two of them (50, 51) are stale-by-ruling sentences the record itself
dispositions.

**Package bytes.** `git diff --stat 3369410 9162d62 -- <package>
scripts/build_pwb_opening_band_scenario.py` is **empty** [Observed]: the
bytes reviewed here are the bytes the sitting record names as "current bytes
(`3369410`)". `git diff 80c4b52 9162d62 -- <package>` touches
`OWNER-DECISION-PACKET.md` (+28/−… 3 hunks), `REVIEW-BRIEF.md` (1 hunk) and
`SEMANTIC-DELTA.md` (4 hunks, 101 insertions in all across the three files)
— the round-10 repair, landed at `3369410` — and nothing else; `git log
80c4b52..9162d62 -- <package>` names `3369410` alone [Observed]. The
manifest, both patches and the builder have blob ids `43b8adbd…`,
`45b12133…`, `ceebdb53…` and `edbcd982…` at every one of the fifteen
commits `59733d3`, `3ee1b0b`, `9d74185`, `dfb605c`, `76b4beb`, `194f8cd`,
`7fd2db3`, `2c5745e`, `d3d5d9d`, `210b864`, `28086f6`, `815785a`, `80c4b52`,
`3369410` and `9162d62`; `IMPACT-LEDGER.md` is blob `59417deb…` from
`7fd2db3` through `9162d62`; the tree's `spec.md` (`543469dc…`) and
`GOVERNING-DEPENDENCIES.md` (`72cedb7a…`) are unchanged at all fifteen
[Observed, `git rev-parse <commit>:<path>`]. `815785a`, `80c4b52` and
`3369410` are ancestors of `9162d62`; `59733d3` is not (rebase-merge), so it
was compared by blob.

---

## Findings

Numbering continues from 48.

**Finding 49 — note. `SEMANTIC-DELTA.md` line 1314 (the new round-10
section): "ran the builder's three modes, sixteen scratch mutations and the
hand-reproduced collision".** Criterion 11; the brief's own test for this
round ("count words must derive from a stated population"); the class of
finding 37.

- [Observed] The round-10 raw's own rationale (raw line 513) uses exactly
  these words, so the sentence attributes to the raw what the raw says.
- [Observed] The raw's mutation table (raw lines 344–359) has sixteen rows,
  R10-M1 to R10-M16, and **R10-M16 is the hand-reproduced collision**
  ("lane B's declaration patch, then this package's, by plain `git apply`").
  The raw's own summary line 361–362 partitions the sixteen as fourteen
  fail-closed + R10-M3 (documented non-failure) + R10-M16 (the collision).
- [Observed] The round-9 section, one section earlier, uses the same
  construction with the other convention: "thirteen scratch mutations" over
  a fourteen-row table whose R9-M10 is the by-hand collision (round-9 raw
  lines 335, 342, 527 — 14 − 1 = 13, as the round-10 raw itself derived at
  its item-2 table).
- [Inferred] Read against the table it rests on, "sixteen … and the
  hand-reproduced collision" counts R10-M16 twice; the population is
  sixteen rows of which one is the collision, i.e. fifteen builder-input
  mutations plus the collision, or sixteen including it. The figure is the
  raw's, the raw is uneditable (CC-REV-6), and the package copied it — the
  same shape as finding 37 ("the raw counts nine and tabulates eight"). Not
  false on the reading "what the raw says"; imprecise on the reading "what
  the raw's table shows". Note; to be dispositioned beside the package, not
  by editing it.

**Finding 50 — note, dispositioned by the 2026-09-26 record. Five sentences
that put the further-round question to the owner are now answered.**
Criterion 11 (a sentence true when written, stale as the live state — the
class of findings 16 and 39).

- [Observed] The sentences: delta step 1 (lines 599–609, "**No round 11 is
  dispatched by this draft's author.** … Whether three consecutive
  confirmations … satisfy this gate, or a further round over the final
  bytes is required, is the owner's to say; the question is put to the
  owner … and is recorded on bead `syzygy-dov.21`"); the delta's round-10
  section tail (lines 1324–1325, "whether a round 11 over these bytes is
  required is put to the owner (step 1 above)"); the packet head (lines
  43–46, "**No round 11 has been dispatched.** Whether … is yours to say; it
  is put to you beside the machine-view package's exception question");
  packet step 1 (lines 274–276, "No round 11 is dispatched by the author:
  whether one is required is your call"); and `docs/README.md` line 85's
  P-71 row ("whether a further round is required is put to the owner").
- [Observed] Each was true when written: the question is on the bead as its
  2026-09-23 01:09 comment ("STOPPED — no round 11 dispatched. OWNER
  QUESTION …"), and no round-11 raw exists at `9162d62` (`ls
  docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-*` → 11 files: rounds 1–10
  and B).
- [Observed] The owner answered on 2026-09-26 (record §1: "`.21`. The
  opening-band package's current bytes (`3369410`) carry no review. One
  further round over them is next. If that round raises no revise finding,
  its notes are dispositioned beside the package, on the bead or in a
  sibling file"; the bead's 2026-09-26 03:28 comment says the same), and
  this review is that round. "No round 11 is dispatched by this draft's
  author" remains literally true — this round was dispatched by the lead,
  not the author.
- [Inferred] Stale, not false; dispositioned by the ruling under its own
  item 1 ("An exception the owner has already ruled on counts as
  dispositioned by that ruling"). Recorded so the next reader knows the
  question is closed. No edit.

**Finding 51 — note, dispositioned by the 2026-09-26 record. "What
explicitly does NOT change" item 3 leaves the PWB-REQ-020 reading to the
owner; the owner has now taken the wider reading.** Criterion 6.

- [Observed] Delta item 3, lines 183–195: "Two readings of that clause exist and
  this package takes the wider one without amending the requirement … The
  wider reading is the one under which this change lands without touching
  PWB-REQ-020; it is named here, not settled: an owner who holds the
  narrower reading should say so before any act (round 5 finding 27)." The
  spec Case (lines 912–914) and the M2 funnel's flag (lines 462–464) are
  quoted exactly [Observed at source].
- [Observed] Record §2: "Wider reading (Recommended)" — "the opening band's
  aggregate is therefore inside the parity population as the `.21` package
  already assumes, and no PWB-REQ-020 amendment is needed. This settles
  round-5 finding 27 of the `.21` review."
- [Inferred] The passage is the form round 5 asked for and round 6 (finding
  33) passed; the owner has said. Dispositioned by the ruling; no edit.

**Finding 52 — note, builder, rule 6. `dependency_patches_collide()` reads
any failure in the sequence [lane B's declaration patch, this package's]
as a collision, so a lane B declaration patch that cannot apply at all
passes `--selftest`'s collision predicate.** Criterion 10.

- [Observed] Builder lines 187–206: the function applies `[theirs, mine]`
  in a scratch tree and returns `True` on the first `ValueError`, whichever
  patch raised it. Its docstring says "True when this package's and lane B's
  declaration patches conflict."
- [Observed] R11-M13c: lane B's `GOVERNING-DEPENDENCIES.md.patch` with one
  context line corrupted so it applies to nothing (`git apply` alone → exit
  1) → `--selftest` exit 0, the full "all fail closed" line; `--check` exit
  0 (it never reads that file). R11-M13d: lane B's declaration patch
  replaced by a well-formed `git diff` editing line 135 of the declaration,
  far from the digest line, so both patches apply in sequence → `--selftest`
  exit 1, "SELFTEST FAILED: the declaration patches no longer collide; the
  packet's regeneration note must be re-derived". R10-M15 (deletion) fails
  closed the same way (the round-10 raw; `is_file()` guard, line 196).
- [Observed] Two of my own earlier attempts were not mutations: shifting a
  hunk header (`@@ -8,7` → `@@ -80,7`) is re-located by `git apply` by
  content, and a `git diff` whose three-line context reaches line 11 still
  collides in `git apply` terms. Recorded so a later reader does not repeat
  them.
- [Inferred] The package's sentences (delta 632–636: "The builder's
  `--selftest` asserts that collision, so if lane B changes shape the claim
  fails loudly instead of going stale"; ledger 295–299; packet 296–298) hold for the shape they
  contemplate — lane B's patch changing to one that composes — and for its
  deletion. The undetected input is a lane B declaration patch that has
  itself broken, which lane B's own `--check` would report and which this
  package's `--check` would also catch the moment the tree's declaration
  moved (its own patch then fails first, R11-M5/M11). Narrow; no sentence
  false on its context's reading; the builder is not a proposed byte and
  the manifest does not hash it, but any tightening is a package edit that
  needs its own round under rule 10 — the owner's to weigh, not this
  review's. Note.

No other finding. Six observations that are not findings, each recorded so
the next reader need not re-derive it:

(i) `--selftest` over a tree whose `spec.md` has drifted at the existing
scenario (R11-M14, "complete catalog" → "full catalog") exits 1 through an
uncaught `ValueError` traceback ("spec.md.patch does not apply … patch does
not apply") rather than a `SELFTEST FAILED:` line: `proposed_bytes()` raises
before the drift fixture is reached. `--check` on the same tree reports the
clean "does not apply to the base bytes" finding, and the battery runs
`--check` first. Fail-closed either way.

(ii) `docs/README.md` line 85: the P-71 row's count **11** equals `ls
docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-* | wc -l` → 11; its date
range 2026-09-22 → 2026-09-23 matches the raws' first-commit dates
(`9d74185` 2026-09-22 for round 1; the other ten 2026-09-23); its text —
tenth sequential review CONFIRM WITH EXCEPTIONS at
`…-CONFIRMATION-9-RAW.md:4` (that file's line 4 is its verdict line), one
note, no revise finding, after rounds 8 and 9 with six and two — is true
(the closing clause is finding 50). **`python3
scripts/check_docs_review_campaign_partition.py --check docs/README.md`
from the worktree root at `9162d62` → exit 1:** "ERROR: stale campaign row:
P-73 edit/repair deletion gate: README=(2, 2026-09-23); derived=(4,
2026-09-23)" then "second-method PASS: git ls-files=239; git ls-tree=239;
exact path sets equal". Line 95's count sentence says 237 files over 52
rows; `git ls-files docs/reviews | wc -l` → 239. Both are outside this
package (the P-73 row and two raws it does not own); the commission says PR
#116 repairs it. Reported as instructed, whatever it is.

(iii) `fe71755` (#107) moved the `check_governance.py` anchors again at
`9162d62` (+72/−5): `def _act_subjects()` 2043, `ACT_DIGEST_COPY_FILES = {`
2266, the activation comment naming `PWB-SCOPED-ATTRIBUTES-AMENDMENT-ACT.md`
2436 (file 8,208 lines; blob `0100871b…`). A fixed-string grep over the four
prose files for every pointer value the delta has ever carried (1976, 2173,
2300, 2010, 2222, 2355, 2022, 2236, 2371, 1518, 1548, 1557, 1552, 1537,
1631, 2037, 2253, 2411, 2043, 2266, 2436) finds hits only at delta lines
672–697 (the round-1 §Review paragraph's per-commit clauses), 1124–1125
(disposition 36) and 1167–1168 (the round-8 summary) — every one in a
per-commit clause or a marked predecessor; 1548, 1557, 1552, 1537, 1631 and
every post-`815785a` value have 0 hits. No package sentence claims a current
line of that file.

(iv) The only occurrence of "line 65" in the package is the round-10
section's own sentence saying the round-9 raw's "raw line 65" pointer "was
never copied into this package" (delta 1340) — self-consistent: the pointer
appears only inside the sentence that disclaims it. Round-1 raw line 85 is
item 11, line 65 is item 9 [Observed].

(v) "The registry entry is edited on no arm." closes both the P-77 and the
P-78 rows of the ruling record (2 hits, lines 65 and 66); "The consent
record, the registry entry and PWB-REQ-005 are edited on no arm." closes
P-74 alone (line 64). The package attributes the first to P-78 and the
second to P-74, which is true; it claims no exclusivity.

(vi) `c83f9a6` added `polaris-edit-repair-deletion-scenario/` (31
directories under `contracts/candidates/` at `815785a`, 32 at `80c4b52` and
32 at `9162d62`, same set). Its `proposed/spec.md.patch` targets
`openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`;
no `proposed/*.patch` under any of the 32 targets the three-surface
specification (`git grep -l -F 'three-surface-poc-experience/specs' --
'…/proposed/*.patch'` → 0), so the four-sibling composition population and
the ledger's "the second is not [drafted]" (line 309) still hold, as the
round-10 section says.

---

## The round-10 repair, finding 48 (commission item 1)

| Site at `9162d62` | Predecessor at `80c4b52` (`git show`) | New locator true? |
|---|---|---|
| delta 1284–1290: "one wrapped code span in the round-1 §Review paragraph's evidence bracket, the bracket the round-7 finding-36 repair wrote, sixteen lines before the finding-36 marker — an earlier locator here said "at the finding-36 marker", round 10 finding 48 — and a builder-code mutation outside rule 6's input scope" | 1274–1275: "one wrapped code span at the\nfinding-36 marker, and a builder-code mutation outside rule 6's input\nscope" — the marked fragment "at the finding-36 marker" is exact across the wrap | [Observed] The odd-backtick non-fence line pair over the four prose files (2,198 lines; fences and the blockquoted `yaml` fence excluded) is exactly one: delta 679–680, `git show` + `<commit>:scripts/check_governance.py`, inside the bracket "[Observed: `git show … at `59733d3`, `9d74185`, `807cecf` and `d3d5d9d`, fixed-string grep for each anchor]". The finding-36 marker ("the third, the round-6 repair, said item 15's pointers "moved to 2022, 2236 and 2371 …"") begins at line 696: 696 − 680 = **16**. `git diff d3d5d9d 28086f6` shows both span lines as `+` (the round-7 repair). Every clause true |

Disposition 48 (delta 1328–1333): "the locator now names the bracket and
its author round, with the earlier locator kept marked. The object was
correctly identified and the span is left as it is" — true (table row; the
span is unchanged, basename `check_governance.py` whole on line 680)
[Observed].

## The round-10 section of `SEMANTIC-DELTA.md` (1295–1347), every figure against the round-10 raw (commission item 2)

| Sentence at `9162d62` | In the round-10 raw | Derived from |
|---|---|---|
| "commissioned 2026-09-23 with the ten earlier raws and their dispositions" (1300–1301) | raw 22–23: "the ten retained raws (rounds 1–9 and the parallel B)" | 9 + 1 = 10; `git ls-tree 80c4b52 docs/reviews/` → 10 matching files; the raw's commit `3369410` is dated 2026-09-23 09:12 +0800 |
| "asked to check both round-9 repairs at their sites against `git show 815785a`, every figure the round-9 section attributes to the round-9 raw, every per-commit claim at the commit named, and every count word against a stated population" (1301–1305) | raw section heads at 132, 150 and 206; raw 169 "Every number word in the round-9 section derives from a stated population" | — |
| "found both round-9 repairs at their sites, true, and quoting their predecessors exactly" (1310–1311) | raw 49–51; the table under its line-132 heading | — |
| "read the per-commit anchors in `check_governance.py` at eight commits from `59733d3` to `80c4b52`" (1311–1313) | raw 25–27 names eight; table 212–221 has eight rows | eight, listed; my own read at those eight plus `9162d62` reproduces every value (table below) |
| "noting that `4c3716a` moved the anchors again at `80c4b52` while no package sentence claims a current line" (1313–1314) | raw observation (iii), 107–116 | observation (iii) above re-derives it at `9162d62` |
| "found every figure the round-9 section attributes to the round-9 raw in that raw" (1314–1316) | raw 150–169 | — |
| "ran the builder's three modes, sixteen scratch mutations and the hand-reproduced collision" (1316–1317) | raw 513 verbatim; table 343–359 has sixteen rows, R10-M16 the collision | **finding 49** |
| "reproduced every ledger figure by two methods over 1,334 blobs" (1318) | raw 383–405 | re-derived below |
| "resolved 662 extracted pointers and 33 line-pointer targets over 2,120 lines with none unresolved" (1318–1320) | raw 253 (2,120 lines), 256 (662 matches), 257 (33 distinct targets), 269 (0 not resolving) | 1,280 + 313 + 351 + 176 = 2,120 at `80c4b52` [Observed, `wc -l` on `git show 80c4b52:<path>`] |
| "found findings 1 to 47 dispositioned truthfully" (1320–1321) | raw 439–470 | — |
| "no revise finding; finding 48 is a note, and the raw says the package may go to the owner with it recorded" (1321–1323) | raw 49; 523 | — |
| "the repair below edited `SEMANTIC-DELTA.md`, `OWNER-DECISION-PACKET.md` and `REVIEW-BRIEF.md` after that commit; `IMPACT-LEDGER.md` and every patch and manifest byte are unchanged" (1323–1326) | — | the `80c4b52..9162d62` diff (head) |
| "The round-10 CONFIRM WITH EXCEPTIONS is bound to `80c4b52` alone; whether a round 11 over these bytes is required is put to the owner (step 1 above)" (1326–1328) | raw lines 2 and 4 | **finding 50** for the closing clause |
| "The raw's four non-finding observations" (1335–1344): the brief's count of ten numbered rounds with B named next; "raw line 65" never copied; the `+41` anchor move claimed by no sentence; the thirty-second directory at `c83f9a6` patching a different specification | raw (i)–(iv), 93–118 | four, listed; each re-checked: brief line 10 "Ten reviews" + B in its next sentence; observation (iv); observation (iii); observation (vi) |

Every number word in the round-10 section derives from a stated population,
finding 49's excepted as described.

## Status heads, step-1 sentences, brief head, README row (commission items 2 and 3)

- Delta step 1 (587–609): "Done ten times", the ten rounds with their
  commits and verdict words, "round 10, over `80c4b52`, CONFIRM WITH
  EXCEPTIONS (one note, no revise finding)" [Observed — each verdict word
  equals line 4 of its raw; each commit is the one its raw names on line 2];
  the further-round sentences are finding 50.
- Packet head (12–50): ten rounds and the parallel round, each with its
  raw's filename and verdict word copied exactly; "the round-8, round-9 and
  round-10 confirmations cover `28086f6`, `815785a` and `80c4b52`, and
  their six, two and one notes were repaired in prose after each"
  [Observed, true: the three repairs are the diffs `28086f6..815785a`,
  `815785a..80c4b52`, `80c4b52..3369410`, prose only]. Packet step 1
  (248–277): "Done ten times", round 10 "no revise finding, one note,
  repaired in prose" [Observed; disposition 48 is "Accepted and repaired"].
- Brief head (10–45): "Ten reviews have been run against this brief", the
  round-10 sentence with its raw's filename [Observed; the round-10 raw's
  observation (i) covers the count]. Its "What the reviewer receives" and
  "Criteria" sections are byte-identical to `59733d3` [Observed, `diff`].
- `docs/README.md` line 85 and the partition check: observation (ii).

## The item-15 anchors, per commit (commission item 4; rule 4: read at each commit, never inferred)

`git show <commit>:scripts/check_governance.py`, fixed-string search for
each anchor; lane B constants are lines 1518–1523 at every commit and the
six-line block hashes identically (`93af31cb…`) at all nine.

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
| `9162d62` (+72/−5 at `fe71755`) | 8,208 | 2043 | 2266 | 2436 | 1548 | 1557 | `0100871b` |

`git log a4a3451..9162d62 -- scripts/check_governance.py` names exactly
`9d74185`, `807cecf`, `4c3716a` and `fe71755`; the blob is identical at
`a4a3451` and `59733d3`, so "pre-date this draft and never moved" holds for
the lane B constants [Observed]. Every per-commit clause of the round-1
§Review paragraph (delta 667–705) — 1976/2173/2300 at `59733d3`;
2010/2222/2355 at `9d74185` beside two siblings' registrations, +139 for
all three; 2022/2236/2371 at `807cecf`, +26; the evidence bracket's four
commits; "included this package's registration … one of three" — is true
at the commit named [Observed]. The three superseded-wording markers (delta
691 ↔ `7fd2db3`; 693–694 ↔ `2c5745e`; 696–697 ↔ `d3d5d9d`, joined across
the wrap) and the packet's superseded recommendation (330–332 ↔ `d3d5d9d`)
were verified exact by rounds 8–10 and the lines they sit on are unchanged
in the `80c4b52..9162d62` diff [Observed, the diff].

## Internal cross-reference sweep (commission item 5)

**Method and denominator.** Python `re` over the four prose files
(`SEMANTIC-DELTA.md` 1,347 lines, `IMPACT-LEDGER.md` 313,
`OWNER-DECISION-PACKET.md` 359, `REVIEW-BRIEF.md` 179 — **2,198 lines**),
extracting every backticked path token with a file extension (258, of which
3 are globs and 2 the future act record / the `-RAW.md` suffix pattern),
backticked seven-hex commit token (116; 16 distinct: `194f8cd`, `28086f6`,
`2c5745e`, `3ee1b0b`, `4c3716a`, `59733d3`, `76b4beb`, `7fd2db3`,
`807cecf`, `80c4b52`, `815785a`, `9d74185`, `a4a3451`, `c83f9a6`,
`d3d5d9d`, `dfb605c` — all `git cat-file -e` as commits), `finding N` with
continuation forms (65), `round N` (109; rounds 1–11, 11 only as "No round
11"), `OQ-N` (56; OQ-1…OQ-6, OQ-6 only as "No OQ-6 is minted"), `P-NN` (71;
rows 68, 69, 70, 71, 72, 74, 75, 78 — all rows of the ruling record) and
backticked bead ids (21; `syzygy-dov.17/.18/.20/.21/.26`): **696 matches**,
over-inclusive by design; **0 not resolving** [Observed]. The delta carries a
numbered disposition for every one of 1–48 (`^\s{0,4}N\. \*\*`, none
missing, none extra). Line-pointer targets (27 distinct `line(s) N(–M)`
tokens) were read at source and are listed under quotation fidelity.

**Quotation fidelity (criterion 1), every blockquote and inline quotation
read at source:** PWB-REQ-010 in full (delta 49–83 = spec 596–630, `diff`
empty after stripping the blockquote marker); PWB-REQ-007's aggregate
sentence (448–450) and Observable (457–458); PWB-REQ-020 (906–910) and its
Case phrase (912–914); the proposed scenario (delta 125–139 = the patch's
`+` lines less the blank, `diff` empty); M4 Q7 (line 119: the region
sentence, "builds the band container and owns its single ordering oracle",
"own honest target", the block-order reservation with its nested double
marks — 1 hit for `three independent claims on "first"` in M4 and in the
delta); M4 slice 3 (827–830, 836–839); M4 slice headings 820/855/876 and
slice 6 at 914; Gate 5's subsection at 1210 and its cells at 1307–1309
("None found.", "None — the three sweeps above find no requirement …",
"Unavailable"); M2 (Q6 cell line 50; success criterion 4 at 130–131;
443–446; 462–464 "fall outside the enumerated population entirely";
472–475 the whole sentence, ending "a fact of the render."); M3 (905–911,
914–916, "A count with no member rendered in place" at 922); RFC2-26
(201–205 inside the clause defined at 196; "Rows are per observable
consequence, not per clause." at 212; `DIRECTIVE-REGISTER.md` line 260
gives that definition site); POC-REQ-032 (578–580, Observable 589–590);
the template's class table (99–104), rule 2 (111–112) and rule 6 (123), "I
only touched X" (57); the ruling record (P-71 arm and "What it means"
sentences; head 14–16 with "It is a plain owner direction" joined across
the wrap; P-74 and P-78 closing sentences — observation (v); P-75 Q2
"PWB-REQ-007 reaches only the project-shape plane"); the owner's OQ
answers (OWNER-VALUES 79–80, 114, 128; OPEN-QUESTIONS 33–35); the
proposal's §Scope (86–91, marked as a paraphrase at delta 390);
`gapReasonCounts` at `polaris.ts` 922 at `a4a3451`, 951 at `194f8cd` (966
at `9162d62`, cited by no sentence), reading `reasons.primary` only;
`PocEpistemic`'s Unknown arm at `model.ts` 42 carrying `reason` only. All
byte-exact where presented as quotations. No `**first**`, `**exactly
one**`, `**is**` or `**are**` inside a quotation (0 hits; the one `**is**`
/ `**are**` line is disposition 9 naming the dropped markers in code spans).

## Builder (commission item 5, criterion 10)

Run from the worktree root at `9162d62`:

- `--check` → exit 0: "PWB opening-band scenario manifest matches 11
  proposed behavior subjects (2 patched, 9 unchanged); the proposed
  declaration equals its regeneration and the spec patch composes with the
  lane B spec patch in both orders".
- `--selftest` → exit 0: "selftest: closed population, byte drift, path
  order, subject drift, patch corruption, lane B composition (both orders
  and a corrupted case), generated-declaration tampering and the
  declaration-patch collision all fail closed".
- `--diff` → exit 0; `sha256` of its output
  `368ecc584be37c8aabdb2becdd51d1630621c693d4aaf7c613fd237a267a51fa` equals
  `sha256` of `proposed/GOVERNING-DEPENDENCIES.md.patch` followed by
  `proposed/spec.md.patch` and differs from the reverse order
  (`193cf8ec…`) [Observed].
- Manifest semantics by hand: `sha256sum -c` over the eleven rows against
  the tree → 9 OK, exactly `GOVERNING-DEPENDENCIES.md` and `spec.md` FAILED
  [Observed]. The spec patch's one hunk is `@@ -618,6 +618,22 @@`, removes
  no line, and its context reaches the `warrants` fence; the declaration
  patch changes the digest line only, "17 requirement(s), 96 distinct
  authorities" on both sides; "opening band" is absent from the spec patch
  (0 hits, case-insensitive); the new heading carries none of PWB-REQ-012's
  six words (0 hits).
- Manifest `sha256sum` and `hashlib` → line 3 above.
- `python3 scripts/check_governance.py` → "32 OK, 20 WARN, 0 FAIL (52
  checks) — counts derived, not asserted"; CG-7d lists "[subject] SIGN OFF
  PWB OPENING-BAND SCENARIO — 0 quotation(s), 0 finding(s), 0 performed
  digest(s)". `--selftest` → "265 fixtures, 0 failing" [Observed].

**Mutations (rule 6), in a `git archive` copy of the whole tree with a
pristine twin; baseline `--check` and `--selftest` passing before and after;
failure text read, not the exit line; `diff -r` of the copy against its twin
empty after every restore (`__pycache__` excluded):**

| # | Mutation | Failure text |
|---|---|---|
| R11-M1 | flip the last hex char of the manifest's `.openspec.yaml` row | "manifest differs from exact regeneration over the proposed bytes" |
| R11-M2 | spec patch `+` line "claims no headline status" → "claims no headline" | "proposed GOVERNING-DEPENDENCIES.md differs from regeneration over the proposed spec bytes" + "manifest differs …" |
| R11-M3 | spec patch context line "labeled" → "labelled" | "spec.md.patch does not apply to the base bytes: error: patch failed: …spec.md:618" |
| R11-M4 | tree spec: an `extra: []` field added to PWB-REQ-010's `warrants` | "proposed spec warrants do not validate: PWB-REQ-002: warrants fields must be exactly {primary, doctrine, contracts, policies, decisions, topology, parent_requirements}" + "manifest differs …" — the patch still applies (its context ends at `primary: RFC7-1`), and the generator's schema catches the field |
| R11-M5 | tree declaration "96 distinct" → "95 distinct" | "GOVERNING-DEPENDENCIES.md.patch does not apply to the base bytes … :8" |
| R11-M6 | append a byte to unpatched `CONTRACT-COVERAGE.md` | "manifest differs from exact regeneration over the proposed bytes" |
| R11-M7 | delete manifest row 3 | "manifest path population or order differs" |
| R11-M8 | edit the manifest's `# 11 artifacts` header comment | "manifest differs from exact regeneration over the proposed bytes" |
| R11-M10 | add a third file `design.md.patch` to `proposed/` | "proposed/*.patch population differs from the declared patched subjects: GOVERNING-DEPENDENCIES.md.patch, design.md.patch, spec.md.patch" + "design.md.patch does not apply …" |
| R11-M11 | declaration patch `-` line digest one hex off | "GOVERNING-DEPENDENCIES.md.patch does not apply to the base bytes … :8" |
| R11-M12 | three-surface spec: `### Requirement: POC-REQ-030` renamed | "proposed spec warrants do not validate: qualified parent requirement does not resolve: three-surface-poc-experience/POC-REQ-030" — the generator reads the parent specification |
| R11-M13c | lane B declaration patch context corrupted so it applies to nothing, `--selftest` | **passes** — finding 52 |
| R11-M13d | lane B declaration patch replaced by a well-formed `git diff` far from the digest line (both apply), `--selftest` | "SELFTEST FAILED: the declaration patches no longer collide; the packet's regeneration note must be re-derived" |
| R11-M14 | tree spec "complete catalog" → "full catalog", `--selftest` | exit 1 via traceback (observation (i)); `--check` on the same tree: "spec.md.patch does not apply to the base bytes … :618" |
| R11-M16 | lane B spec patch: one context line's content corrupted | "spec patches do not compose in the order spec.md.patch, spec.md.patch: … patch failed: …spec.md:450", reported for both orders |

Two attempts (R11-M9, a hunk-header shift; the first R11-M13b, a `git diff`
whose context reached line 11) turned out not to be mutations under `git
apply` and are excluded from the count; R11-M15 was a null replacement by
construction and is excluded. Fourteen distinct mutations ran: twelve fail
closed with distinct, correct text (M1–M8, M10–M12, M13d, M16 — thirteen
rows less M13c and M14's traceback form), M14 fails closed by traceback, and
M13c is the predicate gap finding 52 records.

**Composition, independent of the builder:** this package's `spec.md.patch`
with each of the four sibling `proposed/spec.md.patch` files that target
the PWB specification (`pwb-scoped-attributes-amendment`,
`pwb-missing-currency-disclosure-scenario`, `pwb-machine-view-amendment`,
`pwb-exact-source-render-mode-scenario`) via `git apply` in a `git init`
scratch tree holding the current spec, both orders: every pair applies both
ways and yields one digest (`de6516e4…`, `95918129…`, `55faf032…`,
`14e01af3…`), the same four digests the round-9 and round-10 raws report
[Observed]. The 21 `proposed/*.patch` files under the 32 candidate
directories were enumerated by `+++` target; exactly these four siblings
and this package target the PWB `spec.md`; none targets the three-surface
specification (observation (vi)). The hand-reproduced collision: lane B's
declaration patch applies to the current declaration (exit 0) and this
package's then fails ("patch failed: …GOVERNING-DEPENDENCIES.md:8"), as
delta 623–628 and ledger 295–299 describe [Observed].

## Impact ledger re-derivation (commission item 5, criterion 9)

**Method.** Python `re` over every blob of `git ls-tree -r -z --name-only
a4a3451` read by `git show` (no checkout), decoded as UTF-8, undecodable
blobs skipped; the five patterns as the ledger states them, including its
regex `PWB-REQ-\d{3}(?:(?:/|,\s|\s)\d{3})*?(?:/|,\s|\s)010\b` and the current
source digest computed as sha256 of the `a4a3451:spec.md` blob (the digest
the declaration patch's removed line carries; not copied here). Second
method: `git grep -l -F` / `-o -F` for the literals and `-l -P` / `-o -P`
for the regex at `a4a3451`. Denominator: **1,334** tracked blobs
[Observed].

| Figure | Ledger | Re-derived (`re`) | Second method |
|---|---|---|---|
| tracked files | 1,334 | 1,334 | 1,334 |
| undecodable | 4, the four PNGs | 4, the same four paths | — |
| NUL-carrying | 6 (four PNGs + two `.ts`) | 6, the same six paths (over 1,334; the ledger states it over 1,343 — `3ee1b0b` has 1,343 tracked files, `59733d3` 1,342 [Observed]) | — |
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
other seven 0 [Observed]. The ledger's twelfth-file sentence (145–153) is
the documented non-failure the round-10 raw's R10-M3 confirmed; not re-run
this round.

**Class 3 (2 files):** both JSON declarations carry the current source
digest in `governingBehaviorContract.version` beside a `signedBy`, at
`a4a3451` and still at `9162d62`; neither carries `PWB-REQ-010` (0 and 0)
[Observed]. Labelled Observed for the pins and Inferred for the repair's
home in all three prose files.

**Class 5 (39):** 41 less the two class-1 files = 39, each placed in exactly
one kind by path rule: implementation and tests 6, generated coverage views
4, design packets 2, retained raws 11, dated evidence records 12, plan +
dated review 2, pending register 1, other spec's design note 1 = **39**,
none unplaced, none twice [Observed].

All figures reproduce by two methods.

## Disposition check — findings 1–48 (commission item 6)

All 48 numbered dispositions are present at `9162d62` (sweep above). The
only package bytes that moved between `80c4b52` and `9162d62` are the
round-10 repair (the diff in the head: step-1 sentences, the packet's status
head and step 1, the brief's head, the round-9 tail's locator and the new
round-10 section), so the round-10 raw's per-finding verification of 1–47
at `80c4b52` carries to these bytes for every site outside that diff
[Observed, the diff]. Independently re-established this session: 1 (ledger
31–51, the four and the six named); 4 (regex and every figure, two
methods); 5 (builder never lists the directory — code read, lines 94–110);
9 and 3 (P-74/P-78 sentences at record lines 64/66, "Q4" withdrawn in all
three files); 11 and 6 (M2 line 50 is the Q6 cell); 13 and 20 (class 5 = 39
with both class-2 citers, ×1 and ×4); 21 (`gapReasonCounts` 951 / 922); 22
(M2 472, M4 836); 23, 31, 36, 44 (the per-commit table); 24–26 (RFC2-26
201–205 inside 196; M4 820–913; M2 441–513 with 443–446 and 472–475); 27
and 33 (finding 51); 28 (packet banner lines 3–7 name the act); 29
(paraphrase marked, delta 390); 30 (CG-7e/CG-15 pass in the battery); 40
and 46 (delta 1101–1110, the eight and the two exceptions); 41 (0 emphasis
hits); 42 (M4's nested marks present); 47 (M2 472–475 whole sentence); 48
(table above). Every disposition's stated repair is present at its site and
describes the diff truthfully; none claims more than the bytes show. The
"Author's standing" sentences and the "What no round-10 disposition
changed" sentence are true: the round-10 diff moves no patch byte, manifest
row, requirement, scenario text, ledger figure or owner answer.

## Per-criterion summary

| # | Criterion | Result |
|---|---|---|
| 1 | Quotation fidelity | **Pass** — every quotation byte-exact at its cited lines |
| 2 | Change class | **Pass** — Normative under the template table (99–104) and rule 2 (111–112); argued from obligation |
| 3 | Scenario form | **Pass** — WHEN/THEN/AND, one hunk after the existing scenario and before `warrants`; each clause falsifiable on a rendering or a machine answer; heading clean of PWB-REQ-012's six words |
| 4 | One category, no overlap | **Pass** — hunk `@@ -618,6 +618,22 @@`; lane B's are 450, 473, 907; the P-69 Q7a sibling inserts at 469; no candidate patch targets the three-surface specification (32 directories, 21 patches enumerated); composition with all four PWB-spec siblings verified in both orders |
| 5 | Reconciliation performed | **Pass** — three parties from M4 Q7 (119), each quoted from its own packet at verified lines, R-1/R-2/R-3 each tied to a scenario clause; P-75 Q2 exact |
| 6 | Contradictions surfaced, not settled | **Pass** — OQ-1 to OQ-5 genuine, the easier reading named and not taken, each answered by plain direction 2026-09-23 with no proposed byte moved; the item-3 PWB-REQ-020 tension now answered 2026-09-26 (finding 51) |
| 7 | RFC2-26 | **Pass** — both halves hold against 196–221: limb 1 for slice 3 only, conditioned on OQ-2 (answered (A)); slices 4–5 unmapped on M4's own table, routed to `syzygy-dov.26` |
| 8 | What does not change | **Pass** — all eight items true against the patches: no requirement minted, `warrants` byte-identical (the patch removes no line), 17/96 unchanged, no implementation file, no observed-repository write |
| 9 | Impact ledger | **Pass** — every figure reproduces by two methods over a stated denominator; class-3 labelling correct |
| 10 | Manifest and builder | **Pass with note 52** — eleven rows, two post-apply and nine current, verified by hand; the intended mutation for every named predicate fails closed with correct text; one unintended input (a lane B declaration patch that cannot apply at all) passes the collision predicate |
| 11 | Governance hygiene | **Pass with notes 49–51** — no performed act argument or truncated signed digest in prose; act records cited by path; every code span containing "butler" is a Syzygy-internal path (CG-1b clean); every head carries its candidate or inert banner naming the act; claims labelled; nothing labels the offering accepted, signed or adopted (the "Accepted" hits are disposition verbs); signed change directory untouched; one count word copied from the raw with the raw's own double count (49); five further-round sentences and the item-3 reservation stale by the 2026-09-26 ruling (50, 51) |
| 12 | Scope of authority | **Pass** — nothing performs an act or schedules work; the scenario is conditional ("WHEN … renders an aggregate"), so a conforming implementation may render no opening aggregate; packet 83–86 says so |

## Verdict rationale

**CONFIRM WITH EXCEPTIONS.** No sentence in the package is false at the
reviewed commit on the reading its own context fixes, and no proposed byte
must change. The round-10 repair is at the site its disposition names, its
new locator is true (delta 679–680, sixteen lines before the finding-36
marker at 696, written by the round-7 repair), and its superseded fragment
quotes its predecessor exactly against `git show 80c4b52`. The new
round-10 section attributes to the round-10 raw only figures that raw
carries; every count word in it derives from a population I re-derived,
with one exception — "sixteen scratch mutations and the hand-reproduced
collision" copies the raw's own words over a sixteen-row table whose
sixteenth row is the collision (49, the class of finding 37). The status
heads, step-1 sentences, brief head and README row all say ten rounds, the
round-10 verdict word, one note, and put the further-round question to the
owner; the owner answered on 2026-09-26 and this is the round the answer
names, so those sentences and the item-3 PWB-REQ-020 reservation are stale
by ruling and dispositioned by it (50, 51). Every per-commit value in the
round-1 §Review paragraph is true at the commit named, read in the file at
nine commits, and no package sentence claims a current line of a file that
has moved twice since `815785a`. The bound bytes have the same blob ids at
all fifteen commits from `59733d3` to `9162d62`; the builder's three modes
behave as documented; fourteen scratch mutations behave as documented
except that a lane B declaration patch broken beyond applying reads as a
collision (52, a narrow rule-6 polarity note on a predicate whose intended
mutation does fail closed); every ledger figure reproduces by two methods
over 1,334 blobs; 696 extracted pointers resolve with none unresolved;
findings 1–48 are all dispositioned truthfully; the composition with all
four PWB-spec siblings holds in both orders; and the README partition fails
at this commit on a row this package does not own, reported as instructed.
Under the owner's 2026-09-26 item 1, a round with no revise-severity finding
clears the exact bytes it read: these are the bytes at `3369410` and
`9162d62`, and the four notes above are for the record beside the package,
not for an edit. Whether a phrase is offered is the owner's.
