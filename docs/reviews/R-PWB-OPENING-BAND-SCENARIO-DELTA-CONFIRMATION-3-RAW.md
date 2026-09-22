# Review — PWB opening-band scenario (confirmation round 4)
Reviewed commit: 194f8cd1e90877842786d7adae9df10893ed2495
Manifest SHA-256: 7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46
Verdict: REVISE

Reviewer: fresh-context session, no authoring context (CC-REV-1). I read
nothing under `.syzygy/local/`, ran `git log` with `--format='%h %ad'`
only, and consulted no other agent. The detached checkout at `194f8cd`
(`origin/main`) was read-only throughout: `git status --porcelain` printed
**0 lines** before my first command and **0 lines** after my last; every
mutation and every patch composition ran in an `rsync -a` copy or a
`git init` scratch tree under `scratchpad/out4/scratch/`, each mutated file
restored from a backup, and `diff -r` of the package directory and the
signed change directory against the checkout was empty afterwards. Inputs,
in the order read: `AGENTS.md` (procedure, not authority); the package's
`REVIEW-BRIEF.md`, `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`,
`OWNER-DECISION-PACKET.md`, `PWB-OPENING-BAND-SCENARIO-MANIFEST.txt`, both
`proposed/*.patch`; the round-3 raw
`docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-CONFIRMATION-2-RAW.md` in
full, the heads and findings sections of the round-1, round-2 and parallel
round-2 raws; `git diff 76b4beb 194f8cd -- <package>` in full; the ruling
record `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md` at rows P-74 and
P-78 and the fragments the delta quotes; both 2026-09-23 owner-direction
records at their answer tables; `docs/design/POLARIS-M2-*` lines 50,
118–135, 183–187, 443, 470–475; `POLARIS-M3-*` 905, 912–916;
`POLARIS-M4-*` 119, 827, 834–840, 1210; RFC2-26 at
`rendering-vocabularies.md` 196–221 via `DIRECTIVE-REGISTER.md` line 260;
POC-REQ-032 at the three-surface spec 576–584; the signed PWB spec at
596–632; `scripts/check_governance.py` at its opening-band constants;
`apps/three-surface-poc/src/polaris.ts` and
`packages/three-surface-poc-core/src/model.ts` at the sites the delta
cites. Class: re-review after REVISE over repaired prose (CC-REV-4,
CC-REV-6), against the brief's twelve criteria and the round-3
dispositions.

---

## What I ran

Output read, never exit codes alone (rule 4). All against the checkout
unless marked *scratch*.

1. `git rev-parse HEAD` → `194f8cd1e90877842786d7adae9df10893ed2495`;
   `git status --porcelain | wc -l` → `0` at start and `0` at end. 18
   commits between `76b4beb` and `194f8cd`; `dfb605c` is an ancestor.
2. `sha256sum` and Python `hashlib` over the manifest, both →
   `7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46`
   (computed, rule 3). Equals `OWNER-DECISION-PACKET.md` line 38 and the
   header line of all four earlier raws.
3. Blob ids by `git rev-parse <commit>:<path>` and `git ls-tree`
   [Observed]: manifest `43b8adbd…`, `proposed/spec.md.patch`
   `45b12133…`, `proposed/GOVERNING-DEPENDENCIES.md.patch` `ceebdb53…`,
   builder `edbcd982…` — **byte-identical at `76b4beb` and `194f8cd`**
   (and equal to the ids the round-3 raw reports for `59733d3` and
   `9d74185`). `git diff --stat 76b4beb 194f8cd -- <package>` → four prose
   files changed, 185 insertions, 50 deletions: `SEMANTIC-DELTA.md` (119
   lines), `IMPACT-LEDGER.md` (51), `OWNER-DECISION-PACKET.md` (49),
   `REVIEW-BRIEF.md` (16, its status paragraph only; the section from
   `## What the reviewer receives` onward is context in the one hunk).
   `git diff --stat dfb605c 9d74185 -- <package>` → empty, so the delta's
   "byte-identical to `9d74185` for this package" holds.
4. `python3 scripts/build_pwb_opening_band_scenario.py --check` → "PWB
   opening-band scenario manifest matches 11 proposed behavior subjects
   (2 patched, 9 unchanged); the proposed declaration equals its
   regeneration and the spec patch composes with the lane B spec patch in
   both orders", exit 0.
5. `--selftest` → "selftest: closed population, byte drift, path order,
   subject drift, patch corruption, lane B composition (both orders and a
   corrupted case), generated-declaration tampering and the
   declaration-patch collision all fail closed", exit 0.
6. `--diff` → `cmp` equal to the concatenation
   `proposed/GOVERNING-DEPENDENCIES.md.patch` then `proposed/spec.md.patch`
   (and not the reverse order).
7. `python3 scripts/check_governance.py` → "32 OK, 20 WARN, 0 FAIL (52
   checks) — counts derived, not asserted", exit 0. The string `FAIL`
   occurs once in the output, in that summary line. CG-27's 17 findings
   are all in `.syzygy/governance/decisions/README.md` (17 path hits, 0
   inside this package); the one `PROJECT-STATUS.md` token in that block
   is inside a finding's text. CG-7d lists this package's subject with
   "0 quotation(s), 0 finding(s), 0 performed digest(s)" and the packet as
   "[registered] … declares 1 current and 0 performed-history act(s); 1
   current, 0 historical valid". `--selftest` → "263 fixtures, 0
   failing".
8. **Ledger re-derivation at `a4a3451`, scripted, read-only**
   (`partition.py` in my scratch: `git ls-tree -r -z --name-only` for the
   population, `git show <commit>:<path>` for every blob, the ledger's
   regex verbatim under Python `re`, no `DOTALL`). Second method: `git
   grep -l -F` / `-o -F` for the literals and `git grep -l -E` with the
   ERE translation for the run form. Figures in the finding-13 section.
9. *Scratch*: pairwise composition of this package's `spec.md.patch` with
   each of the four sibling `proposed/spec.md.patch` files, both orders,
   by `git apply` in a `git init` scratch tree holding a copy of the
   current `spec.md`. Table below.
10. *Scratch*, rule 6: six mutations against `--check`, baseline passing
    before and after. Table below.
11. Hygiene sweeps over the seven package files (Python `re`, not ugrep):
    64-hex literals, 7–16-hex-plus-ellipsis truncations, code spans
    containing "butler", the words accepted/adopted/signed off/approved,
    label counts. Results under criterion 11.
12. Quotation checks at source: every fragment the delta quotes from M2,
    M3, M4, the ruling record and RFC2-26 returned `grep -c -F` ≥ 1 in its
    named file, joined across hard wraps where needed; the line positions
    are in finding 22.

---

## Findings 6 and 11–18 — discharged?

| # | Round-3 finding | Discharged? | Evidence |
|---|---|---|---|
| 6 | OQ-5 quotation attribution (round-2 repair had made it false) | **Yes** | Delta 447–453 now attributes the sentence to M2's Q6 cell, line 50, and says M4's Q7 cell (line 119) quotes it. M2 line 50 carries "…the page's first human-visible instant moves from 58.0% depth into the opening band." (`grep -c -F` → 1); M4 line 119 carries it inside "its own honest target is that '…'" (→ 1). M2's numbered list under "**Success, falsifiable.**" (lines 118–135), item 4, reads "The first human-visible instant on the page appears before the first / catalog section", which the delta joins correctly and now calls "success criterion 4". Disposition 6 (delta 702–709) says the round-2 repair was withdrawn and why — truthful [Observed]. |
| 11 | "M4's words, not M2's" false | **Yes** | Same evidence as 6: the phrase is gone; delta 449 reads "M2's words, which M4's Q7 cell (line 119) quotes as M2's 'own honest target'". Disposition 11 (delta 782–786) matches the diff. Its "Verified at source this session before the repair was written" is a process claim I cannot check [Unknown]; the result is right. |
| 12 | `**is**`/`**are**` inside quotations | **Yes** | `grep -F` for `**is** edited` and `**are** edited` over the four prose files → 0 hits; the only remaining `**is**`/`**are**` strings are inside code spans in disposition 9 (delta 720), describing what was dropped. The diff shows exactly six sites changed (ledger 172–174, packet 210–212, delta 523–525). Disposition 9 no longer says "verbatim" [Observed]. Record lines 64 and 66 carry plain "are" / "is". |
| 13 | Class-5 remainder 39, stated 37 | **Yes, with a new false sentence beside it (finding 20)** | Union of literal and run-form citers at `a4a3451` = **41** by both methods (item 8). Minus `spec.md` and `GOVERNING-DEPENDENCIES.md` = **39**. Every one of the 39 places in exactly one of the ledger's kinds: implementation and tests 6 (`polaris.ts`, three `polaris*.test.ts`, `pwb-mutation-sweep.ts`, `pwb-mutation-sweep-main.ts`), generated 4 (`CAPABILITY-COVERAGE.md`, `contract-coverage-matrix/RFC-0007-0009.md`, `contract-coverage-parts/RFC-0007-0009.md`, `tasks.md`), design 2 (M3, M4), raws 11, evidence 12 (ten `docs/evidence/*.json` + two `docs/pursuits/2026-09-13-*.json`), plan and dated review 2, register 1, other spec 1 — sum 39, no file twice, none unplaced [Observed]. Disposition 13 (delta 791–798) matches the diff. |
| 14 | Packet head reported one review | **Yes** | Packet 8–25 now names rounds 1, 2, 3 and the parallel round with each verdict word and raw path; every word and path matches the raw heads (item 12 of the round-3 raw; my own read of lines 1–4 of all four raws). Step 1 at 225–235 says "Done three times" with the round-3 findings summarised correctly (three revise, five notes) [Observed]. |
| 15 | "Slices 4 and 5 still need OQ-1 answered" | **Yes** | Packet 250–251: "still need the `syzygy-dov.26` amendment that the OQ-1 answer routes them to". OWNER-VALUES line 79 answers OQ-1 "Fold into dov.26 package (Recommended)" [Observed]. |
| 16 | "Not drafted at this commit" stale | **Yes** | Ledger 295–303: "not drafted at the baseline commit `a4a3451`. As of 2026-09-23 the first is drafted, as the sibling candidate `pwb-missing-currency-disclosure-scenario/` … (`spec.md` line 469) and composes with this package's patch in both orders to one digest … the second is not." Verified: that sibling's hunk is `@@ -469,3 +469,20 @@`; both orders compose to one digest (composition table); over the 31 directories under `contracts/candidates/`, only this package's delta names `syzygy-dov.26` or `P-75`, and all five sibling `proposed/spec.md.patch` files target the PWB spec, none the three-surface spec — so "the second is not [drafted]" holds over that denominator [Observed]. |
| 17 | "plus this package's own untracked files" | **Yes** | Ledger 12–14: "over the tracked files of that commit, this session, except where a paragraph names another population." The published figures reproduce over exactly the 1,334 tracked files of `a4a3451` (item 8) [Observed]. |
| 18 | §Review head verdict unqualified | **Yes** | Delta 613: "**Round 1 verdict:**" [Observed]. |

---

## New findings

**Finding 19 — note. `SEMANTIC-DELTA.md` 564–570, Migration step 1, is
the stale sentence finding 14 repaired in the packet and not here.** It
reads "**Done twice**: round 1 CONFIRM WITH EXCEPTIONS; round 2, over the
repaired bytes at `9d74185`, REVISE … A round 3 over these bytes is the
next step." At `194f8cd` three rounds have run and the packet's parallel
step 1 (225–235) says so; the delta's §Review at 757–778 says so. The
sentence does not make the package read as more confirmed than it is —
the latest verdict it names is REVISE and it says these bytes carry none
— which is why it is a note and not the revise finding 14 was. Criterion
11. Repair: "Done three times", the round-3 summary, "a round 4".

**Finding 20 — revise. `IMPACT-LEDGER.md` 199–201 and 219–221: a
manifest row carries `PWB-REQ-010`, and the ledger says twice that it does
not.** The round-3 repair added, at 199–201: "no class-2, class-3 or
class-4 file carries the identifier at `a4a3451` except
`CAPABILITY-COVERAGE.md`, which is counted below." The pre-existing kind
text at 216–221 lists `contract-coverage-matrix/RFC-0007-0009.md` among
the four generated views and says "The first is a manifest row (class 2);
the other three are outside the bound eleven." Both are false for the same
file: `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0007-0009.md`
is row 8 of the eleven-row manifest (manifest line 15), so it is class 2,
and at `a4a3451` it carries the literal **4** times (`git show
a4a3451:<path> | grep -c -F` → 4; it is in the 41-file union by both
methods). Sweeping all eleven manifest rows at `a4a3451`: `spec.md` 1,
`GOVERNING-DEPENDENCIES.md` 9, `CAPABILITY-COVERAGE.md` 1,
`contract-coverage-matrix/RFC-0007-0009.md` 4, the other seven 0. Neither
class-3 JSON carries it (0 and 0), and no file under
`.syzygy/governance/decisions/` is in the union except the register, which
the ledger places in class 5 — so the sentence is right about classes 3
and 4 and wrong about class 2 by one file [Observed]. **What survives:**
the 41, the 39, the eight kind counts and the placement of every file
(finding 13 above) — the matrix file is counted once, in "generated (4)",
and the arithmetic is unaffected. **What does not:** a rule-9 absence
claim introduced by this round's repair ("no class-2 … except …") is
false, and a sentence about what the manifest binds ("outside the bound
eleven") is false for a file the owner's act would hash. The round-3 raw's
own finding-13 text said "no class-3 or class-4 file carries the
identifier" and did not say class 2; the repair widened the reviewer's
sentence to class 2 without re-sweeping the eleven rows. Criterion 9
(rules 2 and 9) and criterion 10 (the manifest's membership, misdescribed
in prose). Repair, two sentences in one file: at 199–201 name both
class-2 citers (`CAPABILITY-COVERAGE.md` and
`contract-coverage-matrix/RFC-0007-0009.md`), and at 219–221 say "the
first two are manifest rows (class 2); the other two are outside the bound
eleven". No figure, patch, manifest row or scenario byte moves.

**Finding 21 — note. `SEMANTIC-DELTA.md` 247–248 and 415: `polaris.ts`
"lines 922–931" for `gapReasonCounts` is stale at `194f8cd`.** The
function sits at 922–931 at `a4a3451` and at `76b4beb`, and at 951–960 at
`194f8cd` (`apps/three-surface-poc/src/polaris.ts` changed by 38 lines in
the 18 commits after round 3, none of them a package commit). The claim
itself — it reads `claim.epistemic.reasons.primary` and increments one
map — is still true of that function (line 955) [Observed]. Tree drift
outside the package, dated by the delta's "this session"; not introduced by
the repair. For the record, `countReasonsOf` (at `a4a3451` line 950, now
979) already computes both primary and secondary maps for a different
rendering; the delta's OQ-3 sentence is about the projection M4's design
names and remains accurate. Criterion 1. Repair, if taken: cite by function
name and drop the line numbers, or re-date them.

**Finding 22 — note. Two quoted line positions in the reconciliation
section are off, and were off at every commit since `59733d3`.** Delta
272 "and, at line 473" — M2's "**The probe's own freshness.**" paragraph
starts at line **472** at `a4a3451`, `76b4beb` and `194f8cd`. Delta 301
"and, at line 838" — M4's "**One count, two renderings, one
denominator.**" starts at **836** at all three commits. Delta 288 "at line
914" for M3's "The band states the count of Unknowns…" is a sentence
spanning 913–915, acceptable. The quoted words are exact in every case
(item 12); only the line pointers are wrong, by one and by two. Criterion
1 asks for the line range given; three rounds checked the words and not
the numbers. Repair: 472 and 836.

---

## Machine checks

| Check | Result |
|---|---|
| builder `--check` | pass, exit 0, the success line quoted in item 4 |
| builder `--selftest` | pass, exit 0, nine predicates named |
| builder `--diff` | equals declaration patch + spec patch, `cmp` empty |
| `check_governance.py` | 32 OK, 20 WARN, 0 FAIL of 52; no FAIL, no WARN finding inside the package |
| `check_governance.py --selftest` | 263 fixtures, 0 failing |
| manifest SHA-256 | equals packet line 38 and all four raw headers |
| manifest, both patches, builder `76b4beb` → `194f8cd` | byte-identical (blob ids, item 3) |
| package prose `76b4beb` → `194f8cd` | 4 files, 185+/50− |
| ledger sweep at `a4a3451`, method 1 / method 2 | population 1,334; undecodable 4 (the four PNGs); NUL 6; literal 36 / 110 (36 / 110); run form 6 / 7 (6 files); run-only 5; union 41 (41); spec path 51 / 113 (51 / 113); declaration path 9 / 13 (9 / 13); current digest 13 / 13 (13 / 13) — every published figure reproduces |
| coverage views over the proposed spec (*scratch*) | `build_polaris_project_wide_contract_coverage.py` run in the scratch tree with the spec patch applied: `CONTRACT-COVERAGE.md`, `CAPABILITY-COVERAGE.md` and `contract-coverage-matrix/RFC-0007-0009.md` `cmp` equal to the checkout, so "no row moves" (ledger 218–219) holds and the nine unchanged manifest rows are consistent |

## Mutations

Rule 6, *scratch* copy, each file restored; baseline passed before and
after.

| Id | Mutation | `--check` output | Exit |
|---|---|---|---|
| M-B | manifest `spec.md` row digest, first hex `9a44bdb6` → `0a44bdb6` | "manifest differs from exact regeneration over the proposed bytes" | 1, caught |
| M-C | `proposed/spec.md.patch`: "exactly one such aggregate" → "at most one such aggregate" | "proposed GOVERNING-DEPENDENCIES.md differs from regeneration over the proposed spec bytes" and "manifest differs from exact regeneration" | 1, caught on both predicates |
| M-D | tree `spec.md` line 619 "complete catalog" → "whole catalog" | "spec.md.patch does not apply to the base bytes: error: patch failed: …/spec.md:618" | 1, caught |
| M-E (mine) | `proposed/GOVERNING-DEPENDENCIES.md.patch` `+` digest line, last hex of `9a44bdb6` → `9a44bdb7` | "proposed GOVERNING-DEPENDENCIES.md differs from regeneration" and "manifest differs from exact regeneration" | 1, caught |
| M-F (mine) | manifest rows 1 and 2 swapped | "manifest path population or order differs" | 1, caught |
| M-G (mine) | lane B `proposed/spec.md.patch`, first ` - **Observable**` context line corrupted to `-- **Observable**` | "spec patches do not compose in the order spec.md.patch, spec.md.patch: … error: corrupt patch" | 1, caught |

## Composition

*Scratch*, `git apply` on a copy of the current `spec.md`, both orders.

| Sibling (its hunks) | This first | Sibling first | Same bytes |
|---|---|---|---|
| `pwb-exact-source-render-mode-scenario` (637–652, 664–669) | composes | composes | yes, `14e01af3…` |
| `pwb-machine-view-amendment` (903–908) | composes | composes | yes, `55faf032…` |
| `pwb-missing-currency-disclosure-scenario` (469–471) | composes | composes | yes, `95918129…` |
| `pwb-scoped-attributes-amendment`, lane B (450–471, 473–483, 907–929) | composes | composes | yes, `de6516e4…` |

This package's hunk is `@@ -618,6 +618,22 @@`; it touches no line any
sibling touches (criterion 4). Each sibling patch alone also applies to
the checkout (`git apply --check`). Context only, not a finding against
this package: all five in path order fail at lane B, and lane B after
`pwb-missing-currency-disclosure-scenario` fails while the reverse order
composes — those two overlap at 469–471, which is the OQ-2 (B) collision
the delta describes at 390–394.

## Criteria confirmed without exception at `194f8cd`

- **1 (quotation fidelity):** every quoted fragment found verbatim at
  source (item 12); the two line pointers of finding 22 and the stale
  implementation lines of finding 21 are the only imprecisions, and the
  OQ-5 attribution is now correct.
- **2 (change class):** delta 156–163 unchanged; Normative, argued from
  added obligation.
- **3 (form):** patch lines 9–23 unchanged since `59733d3`: WHEN/THEN/AND,
  inserted after the WhatsApp scenario's last bullet (spec 618–619),
  before `warrants` (621); every clause falsifiable on a rendering.
- **4 (one category, no overlap):** composition table; PWB-REQ-007,
  PWB-REQ-020 and the three-surface spec untouched.
- **5 (reconciliation performed):** delta 252–345 unchanged in the diff;
  M2, M3 and M4 each quoted from its own file (item 12).
- **6 (contradictions surfaced):** OQ-1–OQ-5 still stated with the easier
  reading named and not taken; the owner's answers are recorded as plain
  direction outside the package. Checked against the records: OQ-1 "Fold
  into dov.26 package (Recommended)", OQ-2 "(A) Under PWB-REQ-010
  (Recommended)" (OWNER-VALUES 79–80); OQ-3 "Keep clause; code adds
  secondary (Recommended)", OQ-4 "Clarify inside .26 (Recommended)", OQ-5
  "Account first, then band (Recommended)" (OPEN-QUESTIONS 33–35); both
  records open "Plain owner direction. Performs no act." The delta's
  summaries at 743–755 match [Observed].
- **7 (RFC2-26):** delta 355–411 unchanged; the clause at
  `rendering-vocabularies.md` 196–210 reads "Before implementation, every
  observable consequence either maps to an approved OpenSpec requirement
  and scenario … or carries a reviewed N/A judgment" (joined across the
  wrap at 201–202) and 212 "Rows are per observable consequence, not per
  clause." Slice 3 only, OQ-2 as precondition, no satisfaction claim.
- **8 (what does not change):** the spec patch has no `-` line; the
  declaration patch changes one line with "17 requirement(s), 96 distinct
  authorities" on both sides; no write verb into any repository.
- **10 (manifest and builder):** eleven rows; M-B…M-G caught; nine
  unchanged rows equal current bytes and the regenerated coverage views
  (machine-check table). The ledger's prose about row membership is
  finding 20.
- **11 (hygiene):** the specification's current source digest occurs in
  the package only as the `-` line of the declaration patch (mechanical
  diff context); the packet's one 64-hex literal is this package's own
  manifest digest; the manifest's eleven are its rows; no
  7–16-hex-plus-ellipsis truncation anywhere; code spans containing
  "butler" are only the two Syzygy-internal `POLARIS-BUTLERS-*.json`
  paths and the `openspec/changes/polaris-project-wide-butlers-model/`
  paths — no observed-repository path; "accepted/adopted/approved" hits
  are the brief's own criterion, the packet's "a general 'approved'
  performs no act", quoted "Approved requirement", "may be adopted first"
  and the dispositions' "Accepted and repaired" — nothing labels the
  offering accepted, signed or adopted. Labels: delta 8 Observed / 1
  Inferred, ledger 11 / 3, packet 2 / 2, brief 0. Every prose head carries
  its candidate or inert banner naming the P-71 warrant. The parallel-round
  paragraph (delta 728–741) describes the B raw accurately: verdict
  CONFIRM WITH EXCEPTIONS, finding A the P-74 verb, finding B editorial,
  and no test of the continuation sweep or the twelfth-file sentence (0
  hits for those terms in that raw).
- **12 (scope of authority):** the WHEN at patch lines 11–13 is
  conditional; a rendering with no opening aggregate satisfies it
  vacuously; the packet carries no ceremony phrase, schedules nothing, and
  records OQ-5's block order as a design value not written into the
  specification.

---

## Verdict

**REVISE.**

Rationale. All nine round-3 items are discharged: the OQ-5 sentence is
M2's again with its line and M4's quotation noted (6, 11); the six
emphasis markers are gone (12); the class-5 remainder is 39 and every one
of the 41 citers places in exactly one kind by my own two-method sweep
(13); the packet head, the OQ-1 sentence, the ledger's population and
sibling sentences and the §Review head are all repaired as their
dispositions say (14–18). No byte of the patches, the manifest or the
builder has moved in four rounds; the manifest digest computed here
equals the packet's; `--check`, `--selftest`, `--diff` and the governance
battery read clean; six mutations fail closed; the spec patch composes
with all four siblings in both orders. The verdict is REVISE on finding
20 alone: the round-3 repair added a rule-9 absence sentence to the ledger
— "no class-2 … file carries the identifier … except
`CAPABILITY-COVERAGE.md`" — that is false for
`contract-coverage-matrix/RFC-0007-0009.md`, a manifest row carrying the
identifier four times, and the sentence beside it that calls that file
"outside the bound eleven" is false about what the owner's act would hash.
That is the same class as round 2's finding 5 and round 3's finding 11: a
false sentence about the bound subject or its sweep, introduced or left
standing by a repair, in the artifact whose job is re-derivable figures.
The figures themselves survive; the repair is two sentences in one file,
and the narrow re-run it needs is ledger class 5 plus, if the drafter takes
them, the three notes (19, 21, 22). Findings 19, 21 and 22 alone would not
have moved the verdict off CONFIRM WITH EXCEPTIONS.

`git status --porcelain` in the checkout after my last command: **0
lines**.
