# Review — PWB opening-band aggregate scenario (round 3, re-review after REVISE)
Reviewed commit: 76b4bebcbf7819bda36b9b049ada109b1c6e3db8
Manifest SHA-256: 7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46
Verdict: REVISE

Reviewer: fresh-context session, no authoring context. I read nothing under
`.syzygy/local/`, no commit message bodies (`git log` was run with
`--format='%h %ad'` only), and consulted no other agent. The detached
checkout at `76b4beb` was treated as read-only: `git status --porcelain`
returned **0 lines** before I started and **0 lines** after my last command
in it; every mutation ran in an `rsync -a` scratch copy under
`scratchpad/review3-ob-scratch/tree/` (`.git`, `node_modules` and `dist`
excluded), each mutated file restored from a backup afterwards, and
`diff -r` of the package and change directories against the checkout was
empty at the end. Inputs, in the order read: `AGENTS.md` in full; the
package's `REVIEW-BRIEF.md`; the round-1 raw
`docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-RAW.md` and the round-2 raw
`docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-CONFIRMATION-RAW.md` in
full; `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`,
`PWB-OPENING-BAND-SCENARIO-MANIFEST.txt`, both `proposed/*.patch` and
`scripts/build_pwb_opening_band_scenario.py` in full; `git diff 9d74185
76b4beb -- <package>`; the two owner-direction records
`.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`
and
`.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md`
in full; the ruling record
`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
at rows P-74 and P-78 (lines 63–68); `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md`
line 119; `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` lines 40–50,
100–135 and 183–187; `scripts/check_governance.py` at the lines naming this
package; `PROJECT-STATUS.md` lines 256–257;
`.github/workflows/governance-docs.yml` lines 124–128; the sibling package
`pwb-missing-currency-disclosure-scenario`'s `SEMANTIC-DELTA.md` head and
`proposed/spec.md.patch` hunk lines. Class: re-review after REVISE over
repaired prose (CC-REV-4, CC-REV-6), against the brief's twelve criteria and
the round-2 dispositions.

---

## What I ran

All against the checkout unless marked *scratch*. Output is what I read,
not exit codes (rule 4).

1. `git rev-parse HEAD` → `76b4bebcbf7819bda36b9b049ada109b1c6e3db8`;
   `git status --porcelain | wc -l` → `0` (start) and `0` (end).
   `git merge-base --is-ancestor 9d74185 76b4beb` → yes; `44c51b5` → yes.
   Eleven commits between `9d74185` and `76b4beb`, dated 2026-09-22/23.
2. `sha256sum PWB-OPENING-BAND-SCENARIO-MANIFEST.txt` →
   `7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46`;
   computed, never transcribed (rule 3). Equals `OWNER-DECISION-PACKET.md`
   line 28 and the header line of both earlier raws.
3. `git rev-parse <commit>:<path>` for every package file at `59733d3`,
   `9d74185` and `76b4beb` [Observed]: the manifest (blob `43b8adbd…`),
   `proposed/spec.md.patch` (`45b12133…`),
   `proposed/GOVERNING-DEPENDENCIES.md.patch` (`ceebdb53…`) and the builder
   (`edbcd982…`) are **byte-identical across all three commits**. Four
   prose files differ between `9d74185` and `76b4beb`: `SEMANTIC-DELTA.md`,
   `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`, `REVIEW-BRIEF.md` (the
   brief's one hunk is `@@ -7,12 +7,16 @@`, its status paragraph; the
   section from `## What the reviewer receives` to end hashes identically at
   all three commits, prefix `0c570fba…`).
4. `python3 scripts/build_pwb_opening_band_scenario.py --check` → "PWB
   opening-band scenario manifest matches 11 proposed behavior subjects (2
   patched, 9 unchanged); the proposed declaration equals its regeneration
   and the spec patch composes with the lane B spec patch in both orders",
   exit 0.
5. `--selftest` → "selftest: closed population, byte drift, path order,
   subject drift, patch corruption, lane B composition (both orders and a
   corrupted case), generated-declaration tampering and the
   declaration-patch collision all fail closed", exit 0.
6. `--diff` → `cmp` equal to the concatenation of
   `proposed/GOVERNING-DEPENDENCIES.md.patch` then `proposed/spec.md.patch`
   (the builder's name order, line 110).
7. `python3 scripts/check_governance.py` → "32 OK, 20 WARN, 0 FAIL (52
   checks) — counts derived, not asserted". CG-7d names this package:
   "[subject] SIGN OFF PWB OPENING-BAND SCENARIO — 0 quotation(s), 0
   finding(s), 0 performed digest(s)" and "[registered]
   …/pwb-opening-band-scenario/OWNER-DECISION-PACKET.md — declares 1 current
   and 0 performed-history act(s); 1 current, 0 historical valid". All 20
   WARNs are report-only families; CG-27's 17 findings are all in
   `.syzygy/governance/decisions/README.md`, outside this package. The one
   `PROJECT-STATUS.md` token in that block is part of a finding's text, not
   a finding path. `--selftest` → "263 fixtures, 0 failing".
8. **Ledger re-derivation, scripted, read-only** (`ledger_rederive3.py`
   in my session scratchpad: `git ls-tree -r -z --name-only <commit>` for
   the population, `git cat-file --batch` for blobs; nothing checked out).
   Results are in the finding-4 section. Second method for the literal:
   `git grep -l -F 'PWB-REQ-010' a4a3451` → 36 paths, the same set. Second
   method for the run form: `git grep -l -E` with the ERE translation of the
   ledger's regex → the same 6 paths; `git grep -c -F
   'PWB-REQ-001/002/003/004/005/010' a4a3451` → 5 files, 1 each.
   Third probe, for forms the regex does not cover: every other `/010`
   hit at `a4a3451` (M6/M7 funnels, two generator-coverage JSONs, the
   manifesto-generation `tasks.md`) is a `REQ-006/…/010` run of a *different*
   specification's identifiers, correctly outside the predicate; a sweep
   for range and conjunction forms (`PWB-REQ-NNN..010`, `–010`, `to 010`,
   `and 010`, `, and 010`) → 0 hits [Observed].
9. The same script at `76b4beb`: population **1,405**; literal **50 / 163**;
   run form **10 / 16** (6 without the literal); union **56**. See finding
   4's closing paragraph.
10. **Rule 6, four mutations in the scratch copy**, each followed by
    `--check` and a restore; baseline passed before and after:
    - **M-A** a twelfth file `NEW-ARTIFACT.md` written into
      `openspec/changes/polaris-project-wide-butlers-model/` → the unchanged
      success line, **exit 0** — as the repaired ledger sentence now says
      (finding 5).
    - **M-B** manifest `spec.md` row digest, first hex `9a44bdb6` →
      `0a44bdb6` → "PWB opening-band scenario manifest does not verify: /
      manifest differs from exact regeneration over the proposed bytes",
      exit 1. **Caught.**
    - **M-C** scenario text inside `proposed/spec.md.patch`, "exactly one
      such aggregate" → "at most one such aggregate" → "proposed
      GOVERNING-DEPENDENCIES.md differs from regeneration over the proposed
      spec bytes" and "manifest differs from exact regeneration over the
      proposed bytes", exit 1. **Caught**, on both predicates.
    - **M-D** the tree's `spec.md` line 619, "complete catalog" → "whole
      catalog" → "spec.md.patch does not apply to the base bytes: error:
      patch failed: …/spec.md:618", exit 1. **Caught.**
11. *Scratch*, independent of the builder: the sibling
    `pwb-missing-currency-disclosure-scenario/proposed/spec.md.patch` (hunk
    `@@ -469,3 +469,20 @@`, a scenario under PWB-REQ-007, drafted for gate
    `syzygy-dov.20`) and this package's spec patch applied with `git apply`
    in both orders on a copy of the current `spec.md`; both orders applied
    and the two results are byte-identical (`cmp` empty). The composed file
    carries the new scenarios at lines 470 and 638. See finding 16.
12. Quotation checks at source: P-74 row (record line 64) ends "The consent
    record, the registry entry and PWB-REQ-005 are edited on no arm. |";
    P-78 row (line 66) ends "The registry entry is edited on no arm. |";
    `grep -o -F` for the bold forms `**are** edited` / `**is** edited` in
    the record → 0 hits (finding 12). M4 line 119 carries "the page's first
    human-visible instant moves from 58.0% depth into the opening band"
    inside "its own honest target is that '…'" — a quotation of M2; M2 line
    50 (its question table, cell Q6, "Sequencing against the lane B
    package, and the honest target") carries the same sentence verbatim
    (finding 11). M2 lines 130–131, item 4 of the list under "**Success,
    falsifiable.**", read "The first human-visible instant on the page
    appears before the first / catalog section, …", which the delta's
    quotation joins correctly across the hard wrap; M2 line 185 carries the
    58.0% measurement.
13. Registration state at `76b4beb`: `scripts/check_governance.py` lines
    1548–1553 (label, dir, subject, act path), 1626 (subject list), 2067
    (`_act_subjects()`), 2285–2286 (`ACT_DIGEST_COPY_FILES`), 2427–2438
    (existence-gated activation); `PWB_SUCCESSOR_CHAIN` at 1631–1638 has
    **three** links; the comment at 1537–1541 reads "no
    `PWB_SUCCESSOR_CHAIN` link until an act fixes the performance order";
    `PROJECT-STATUS.md` 256–257 and `governance-docs.yml` 124–128 carry the
    two commands [Observed].
14. Hygiene sweeps over the package: the current performed spec digest
    occurs only as the `-` line of `proposed/GOVERNING-DEPENDENCIES.md.patch`
    (mechanical diff context, as rounds 1 and 2 found); no
    7–16-hex-plus-ellipsis truncation anywhere; the only code spans
    containing "butler" are the two Syzygy-internal
    `.syzygy/governance/…/POLARIS-BUTLERS-*.json` paths and the
    `openspec/changes/polaris-project-wide-butlers-model/` path — no
    observed-repository path; "accepted/adopted/signed off/approved" hits
    are the brief's own criterion, the packet's "a general 'approved'
    performs no act", and quoted "Approved requirement" — nothing labels the
    offering accepted. Label counts (Python `re`, not ugrep): delta 8,
    ledger 12, packet 4, brief 0.

---

## Findings 4–10 — discharged?

### Finding 4 (continuation form, the load-bearing one) — **discharged; disposition truthful; one adjacent figure does not partition (finding 13)**

Re-derived at `a4a3451` over `git ls-tree -r -z` (never a checkout), the
ledger's regex run verbatim under Python `re`, no `DOTALL`, case-sensitive,
with `git grep` as the second method. Mine beside the ledger's:

| Figure | Ledger (line) | Mine |
|---|---|---|
| Population | 1,334 (28) | **1,334** |
| Undecodable paths | 4 (35) | **4**, the same four PNGs |
| NUL-carrying paths | 6 (43) | **6**, the same six |
| `PWB-REQ-010` literal | 36 / 110 (94) | **36 / 110**; `git grep -l -F` 36 |
| continuation regex | 6 / 7 (95) | **6 / 7**; `git grep -l -E` 6 |
| run-form files without the literal | 5 (100) | **5** |
| the sixth, carrying both forms | `…2026-09-04.json` (101) | **the same file** |
| citer population (union) | 41 (109) | **41** |
| patched spec path | 51 / 113 (96) | **51 / 113** |
| patched declaration path | 9 / 13 (97) | **9 / 13** |
| current spec digest | 13 / 13 (98) | **13 / 13** |

The six run-form files and their matches: `pwb-mutation-sweep-main.ts`
(`PWB-REQ-001/002/003/004/005/010`), the three parity/named-absent evidence
JSONs and `…2026-09-04.json` (the same run each), and
`R-PWB-LIVE-EXACT-HEAD-ENGINEERING-RAW.md` (two: `PWB-REQ-001/002/003/010`,
`PWB-REQ-001/002/004/010`) — exactly the six the ledger names at lines
101–108, with the two-occurrence file identified correctly [Observed].

Class 5 kind counts: implementation 6 + generated 4 + design 2 + raws 11 +
evidence 12 + register 1 + other spec 1 = **37**, as stated. The five added
files landed where the ledger says: `pwb-mutation-sweep-main.ts` in
implementation (named at line 202 with "carries no literal" — true), the
three evidence JSONs in the evidence count (7 at `a4a3451` with the literal
under `docs/evidence/` + 3 = 10, plus two `docs/pursuits/*.json` = 12, the
only reading that reproduces 12 — see finding 13), and the one raw in the
raws count (10 → 11) [Observed].

At `76b4beb` the same regex returns **10 files / 16 occurrences**, six
without the literal, union 56 over 1,405 tracked paths. The four additions
are this package's own `IMPACT-LEDGER.md` (3 matches: the run example and
`PWB-REQ-009, 010`) and `SEMANTIC-DELTA.md` (3), the sibling
`pwb-machine-view-amendment/IMPACT-LEDGER.md` (2, no literal) and the
round-2 raw (1). The ledger states its baseline as `a4a3451` at line 11 and
its re-run "at the baseline commit" at lines 67–68, so the drift is
immaterial to every figure it publishes — but the package's own prose now
matches its own predicate, which is why finding 17 asks for the head
sentence at lines 12–13 to stop saying the population includes the
package's files.

Disposition 4 (delta 685–692) describes what the diff shows: the regex, the
six files, 41 and 37, the table and sentence moved in both files. Truthful
[Observed].

### Finding 5 (the twelfth-file sentence) — **discharged; disposition truthful**

`IMPACT-LEDGER.md` lines 144–152 now say `BEHAVIOR_SUBJECTS` is a hard-coded
tuple of eleven distinct paths, the manifest hashes exactly those, a change
to any unpatched one fails `--check`, and the builder never lists the change
directory so a twelfth file "neither fails `--check` nor enters the
manifest". Each clause is true of the builder: `BEHAVIOR_SUBJECTS` at lines
64–81 (eleven literal paths, `sorted`); `current_bytes()` at 93–106 iterates
only that tuple; the selftest's "closed population" at 265–267 is
`len(BEHAVIOR_SUBJECTS) != 11 or len(set(...)) != 11`; the byte-drift fixture
at 271–277 appends to the first unpatched subject and requires the manifest
to change. Mutation M-A reproduces the round-2 result — success line, exit 0
— which is now exactly what the sentence says [Observed]. Disposition 5
(delta 693–699) matches the diff, and its reason for not adding a directory
scan (the act's argument should not depend on files it does not hash) is a
design statement, not a claim about the code.

### Finding 6 (the OQ-5 quotation) — **not discharged: the repair replaced a correct attribution with a false one** (finding 11)

The round-2 finding rested on "That sentence does not occur in
`…M2-EVIDENCE-CURRENCY-FUNNEL.md` (`grep -F` … 0 hits outside the Q6 cell,
which does not carry it)". The Q6 cell **does** carry it: M2 line 50 reads
"…and the page's first human-visible instant moves from 58.0% depth into
the opening band. |" [Observed, `grep -c -F` → 1 in M2, 1 in M4]. M4 line
119 attributes it to M2 in so many words ("its own honest target is that
'…'"). So the sentence is M2's, M4 quotes it, and the delta's original text
at `9d74185` ("M2 slice 2's stated target that '…'") was a correct
quotation. The repaired text at delta 447–451 now says "as the M4 funnel's
Q7 cell renders it … — M4's words, not M2's; M2's own are its step 4, …".
"M4's words, not M2's" is false. Disposition 6 (delta 700–702) therefore
records a repair that moved a true sentence to a false one. Criterion 1;
rule 8. A lesser imprecision in the same sentence: M2's numbered list at
lines 120–135 sits under "**Success, falsifiable.**" — item 4 is a success
criterion, not a "step".

### Finding 7 (stale registration sentences) — **discharged; disposition truthful**

`IMPACT-LEDGER.md` 234–240 and 260–261, `OWNER-DECISION-PACKET.md` 248–252
and 293–294 carry dated "as of 2026-09-23" notes that the three edits landed
at the merge of PR #52 with the chain link deliberately withheld, and name
the owners of that fact; the drafted text stands beneath, unedited. Every
clause checks against the tree (item 13): constants, subject list,
`_act_subjects()` row, copy-file row, activation function, both battery
lines, both CI steps present; chain has three links; the comment the ledger
cites at line 238 exists at `check_governance.py` 1537–1541 and says what
the ledger says it says [Observed].

### Finding 8 (four files, not three) — **discharged**

Delta 617–623 now names `REVIEW-BRIEF.md` with "its criteria byte-identical";
the criteria section hashes identically at `59733d3`, `9d74185` and
`76b4beb` (item 3) [Observed].

### Finding 9 (P-74's verb) — **discharged in substance; the "verbatim" claim is inexact** (finding 12)

Ledger 171–173, delta 521–523 and packet 200–202 now quote each row's own
sentence with the right verb (P-78 "is", P-74 "are"), attributed to the
right row. The words match the record. The markup does not: all six quoted
sentences carry `**is**` / `**are**` emphasis that the record's lines 64
and 66 do not (item 12). The emphasis is the round-2 raw's own rendering
(raw lines 222–223, 389) copied into quotation marks. Disposition 9 (delta
711–713) says "each row's own closing sentence is quoted, verbatim"; the
sentence is quoted, not verbatim.

### Finding 10 ("changes" → "may change") — **discharged**

Packet 222–223: "An answer to OQ-2 or OQ-3 may change the proposed bytes,
which would retire the review." Matches delta 570–571 [Observed].

---

## The owner's answers, against the records

The package says (delta 717–729; packet 222–229) that OQ-1 and OQ-2 are
answered in the OWNER-VALUES record and OQ-3 to OQ-5 in the OPEN-QUESTIONS
record, both 2026-09-23, none changing a proposed byte. Checked against the
records [Observed]:

- OQ-1 "Fold into dov.26 package (Recommended)" (OWNER-VALUES line 79;
  reading at 82–85: route (a), the P-75 Q1 package at `syzygy-dov.26`).
  The packet's route (a) at 111–113 is that route. The delta says "in the
  two plain owner directions" and names no arm; consistent.
- OQ-2 "(A) Under PWB-REQ-010 (Recommended)" (line 80; reading at 85–86:
  "no patch byte moves and the reviewed manifest is unchanged"). Placement
  (A) is the drafted host; the spec patch inserts at line 618 under
  PWB-REQ-010 (heading 596, next requirement 632); manifest and patches are
  byte-identical to `59733d3` (item 3). No byte moved.
- OQ-3 "Keep clause; code adds secondary (Recommended)" (OPEN-QUESTIONS line
  33; reading 39–45). Delta 724–725 "keeps PWB-REQ-007 and leaves the
  secondary counts to slice 3's code" — matches. The scenario's third bullet
  is unchanged.
- OQ-4 "Clarify inside .26 (Recommended)" (line 34; reading 46–51). Delta
  725–726 "routes the POC-REQ-032 question to the `syzygy-dov.26` package"
  — matches.
- OQ-5 "Account first, then band (Recommended)" (line 35; reading 52–64:
  categories first, then the band with the currency probe before the
  Unknown aggregate; "a design value for slices 2 and 3, not a
  specification sentence"). Delta 726–729 and packet 228–229 say the same.
  The scenario's wording is unchanged and compatible.

Both records open "Plain owner direction. Performs no act." and the package
labels them so. Nothing in the package now reads as if an answer bound
anything.

---

## New findings

**Finding 11 — revise. Delta 447–451: "M4's words, not M2's" is false;
the repair for finding 6 replaced a correct quotation with a false
attribution.** Evidence in the finding-6 section above: M2 line 50 (its
Q6 cell) carries the sentence verbatim and M4 line 119 quotes it as M2's
"own honest target". Disposition 6 at delta 700–702 describes this move as
a repair. Criterion 1; rule 8. Repair: restore the attribution to M2 (cite
line 50, cell Q6, and optionally note that M4 line 119 quotes it), keep the
step-4 sentence beside it if wanted, and correct disposition 6 to say the
round-2 finding did not survive re-reading at source. The "step 4" label
should read "success criterion 4".

**Finding 12 — note. Emphasis markers inside verbatim quotations.**
`IMPACT-LEDGER.md` 171–173, `SEMANTIC-DELTA.md` 521–523,
`OWNER-DECISION-PACKET.md` 200–202 quote `**is**` and `**are**`; record
lines 64 and 66 carry plain "is" and "are" (0 bold hits, item 12).
Disposition 9's "verbatim" (delta 713) is inexact. Criterion 1; rule 8.
Repair: drop the asterisks in all six sites.

**Finding 13 — revise. `IMPACT-LEDGER.md` 194–197: "the remainder of the 41
`PWB-REQ-010` citers … (37 files)" does not partition the 41.** Classes 1–4
hold exactly two of the 41 citers — `spec.md` and `GOVERNING-DEPENDENCIES.md`
(class 1); `CAPABILITY-COVERAGE.md` is counted inside class 5's "generated
(4)" at 209–214 by the ledger's own words, and no class-3 or class-4 file
carries the identifier at `a4a3451` (union listing, item 8). The remainder
is therefore **39**, and the seven kinds sum to 37 only by leaving two citers
in no kind. Which two depends on a path the ledger never states: if "dated
evidence records (12)" means the ten `docs/evidence/*.json` plus the two
`docs/pursuits/2026-09-13-*.json` (the only reading that reaches 12), then
`docs/PWB-IMPLEMENTATION-PLAN.md` (five literal sites, e.g. line 377 "(a)
First reading (PWB-REQ-010)") and
`docs/reviews/2026-09-09-polaris-editorial-repair.md` (line 40, "PWB-REQ-010,
011, 012, 014, 016 and 020") are unplaced; if it means the plan and the
editorial-repair record, the two pursuit JSONs are. Pre-existing: at
`59733d3` the same section read 32 = 36 − 4 with the same two omitted, and
neither earlier round tested the partition; but the section was re-derived
and republished on 2026-09-23 as a recount, and delta 540–541 lists "the
implementation plan" among the class-5 citers in prose while the ledger's
kinds do not. The impact conclusion survives — neither file carries an
obligation the scenario changes — but a figure the reader is invited to
re-derive comes out 39, not 37. Criterion 9; rules 2 and 9. Repair: state
the paths behind "evidence (12)", add the two missing citers to a kind (or
a new "plan and dated review records (2)" kind), and make the remainder
arithmetic explicit (41 − 2 class-1 = 39).

**Finding 14 — revise. `OWNER-DECISION-PACKET.md` 8–15 misstates the
review of record.** "Date: 2026-09-21 (first draft; repaired the same day).
One fresh-context review has been run against `REVIEW-BRIEF.md` and
returned **CONFIRM WITH EXCEPTIONS** with three notes and no blocking
finding … All three notes are repaired in prose only". At `76b4beb` two
reviews have run, the second returned REVISE, and the file's own step 1 at
216–221 says so ("Done twice … round 2 … REVISE"). The head paragraph is the
first thing the owner reads and carries only the superseded verdict; the
repair also happened on 2026-09-23, not "the same day". Same shape as
round-2 finding 7 (a page restating state it does not own, gone stale), in
the owner-facing artifact. Criterion 11 (nothing may read as more confirmed
than it is) and 12. Repair: rewrite the head to say two rounds, both
verdicts, both raws, and that a round 3 is what these bytes await — or
replace the paragraph with a pointer to `SEMANTIC-DELTA.md` §Review as the
owner of that state.

**Finding 15 — note. `OWNER-DECISION-PACKET.md` 236: "Slices 4 and 5 still
need OQ-1 answered."** OQ-1 is answered (packet 222–227, OWNER-VALUES line
79). What slices 4 and 5 still need is the `syzygy-dov.26` amendment the
answer routes them to; delta 581–582 has the accurate form. Criterion 11.

**Finding 16 — note. `IMPACT-LEDGER.md` 280–282: "The P-69 Q7a clarification
scenario to PWB-REQ-007 (gate bead `syzygy-dov.20`) … are not drafted at
this commit."** At `76b4beb` the tree carries
`.syzygy/governance/contracts/candidates/pwb-missing-currency-disclosure-scenario/`,
whose delta head names P-69 arm B question 7a and gate `syzygy-dov.20`, and
whose `proposed/spec.md.patch` inserts a scenario at `spec.md` line 469
under PWB-REQ-007. Read as "at the baseline commit `a4a3451`" the sentence
is true; read as the live state the same paragraph's "It composes at this
commit [Observed]" (272) invites, it is stale. The two spec patches compose
in both orders, byte-identically (item 11); the builder asserts only lane B
composition, which is what the ledger claims for it, so no builder claim is
false. Criterion 4 is not breached — the hunks are 469 and 618. Repair: a
dated mark at the sentence naming the sibling package and the composition
result, or "at the baseline commit" in place of "at this commit".

**Finding 17 — note. `IMPACT-LEDGER.md` 11–13 versus 28 and 67–69.** "Every
figure below was produced at that commit plus this package's own untracked
files" cannot be true of the published figures: the package's own prose
carries the literal many times and, since this repair, the run-form
examples (item 9: 3 regex matches in the ledger, 3 in the delta), so a
population including it returns neither 36 nor 6. The figures are true of
the 1,334 tracked files of `a4a3451` alone, which is what lines 28 and
67–69 say. Criterion 9; rule 2. Repair: delete "plus this package's own
untracked files".

**Finding 18 — note. `SEMANTIC-DELTA.md` 611 "**Verdict:** **CONFIRM WITH
EXCEPTIONS**"** is unqualified by round while the round-2 subsection at
660–669 carries REVISE; a reader of the section head alone takes the
superseded verdict. Criterion 11. Repair: "Round 1 verdict:".

---

## Criteria confirmed without exception at `76b4beb`

- **2 (change class):** unchanged text at delta 156–163; Normative, argued
  from added obligation. Correct.
- **3 (form):** patch lines 9–23 unchanged since `59733d3`; WHEN/THEN/AND,
  after the WhatsApp scenario's last bullet (618–619), before `warrants`
  (621); every clause falsifiable on a rendering; no bare value.
- **4 (one category, no overlap):** the spec hunk is one contiguous
  insertion at 618; lane B's hunks are 450–471, 473–483, 907–929; the new
  `syzygy-dov.20` sibling's is 469–471; none touches another's lines; both
  compositions proven (items 4, 11). PWB-REQ-007's and PWB-REQ-020's
  regions and the three-surface specification are untouched.
- **5 (reconciliation performed):** delta 264–306 unchanged since round 2;
  the M2/M3/M4 quotations were verified byte-exact by both earlier rounds
  and the bytes are the same blob-region (the repair diff touches lines
  447–451 only within the OQ-5 paragraph, not the reconciliation section).
- **6 (contradictions surfaced):** all five OQs still stated with the
  easier reading named and not taken; the answers are recorded as the
  owner's, outside the package, binding nothing; no OQ is settled inside
  the delta.
- **7 (RFC2-26):** delta 355–411 unchanged; slice 3 only, OQ-2 as
  precondition, no claim that RFC2-26 is satisfied.
- **8 (what does not change):** eight items hold; the spec patch has no
  `-` line; the declaration patch changes one line with "17 requirement(s),
  96 distinct authorities" on both sides; no write verb into any repository
  in the scenario; nothing under `proposed/` but the two governed diffs.
- **10 (manifest and builder):** eleven rows; two patched rows hash
  post-apply bytes (M-C shows the spec row and the declaration digest line
  are coupled); nine equal current bytes; M-B, M-C, M-D caught; M-A passes
  and the ledger now says it does.
- **11 (hygiene):** item 14; every prose head carries its candidate/inert
  banner naming the warrant; no signed byte edited in place.
- **12 (scope of authority):** the WHEN at patch lines 11–13 is conditional;
  a rendering with no opening aggregate satisfies the scenario vacuously;
  delta 140–147 and packet 50–53 say so; P-71-Q5's "no write" is restated
  at delta 191–195 and packet 58–59; the owner's OQ-5 value is recorded as
  a design value and not written into the specification. The packet
  carries no sign-off phrase, and nothing in it schedules slice 3 or reads
  as permission to render the band.

---

## Verdict

**REVISE.**

Rationale. Findings 4, 5, 7, 8 and 10 are discharged and their dispositions
describe the diff truthfully; every figure of finding 4 reproduces at the
baseline by two methods, and the twelfth-file mutation now confirms the
ledger's sentence rather than falsifying it. No byte of the two patches,
the manifest or the builder has moved in three rounds; the manifest digest
computed here equals the packet's; `--check`, `--selftest`, `--diff` and
the governance battery read clean; the five owner answers match their
records and changed no proposed byte. The verdict is REVISE on findings 11,
13 and 14: the repair for finding 6 turned a correct quotation into a false
attribution in the delta (a criterion-1 defect introduced this round, with a
disposition that records it as a repair); the ledger's class-5 remainder is
39 by its own arithmetic and 37 only by leaving two citers unplaced, in the
section repaired for figures in both earlier rounds; and the owner packet's
head paragraph reports one review and one verdict when the verdict of
record is the second review's REVISE. None of the three touches the
proposed bytes, the manifest, the scenario's conditional character or the
open questions; the repair is prose in three files, and the narrow re-run
it needs is the OQ-5 paragraph and disposition 6, the class-5 kind list,
and the packet head — plus findings 12 and 15–18 if the drafter takes them.
Findings 12 and 15–18 are notes and would not on their own move the verdict
off CONFIRM WITH EXCEPTIONS.
