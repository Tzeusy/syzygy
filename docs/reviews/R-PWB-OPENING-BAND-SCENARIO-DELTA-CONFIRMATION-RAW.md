# Review — PWB opening-band aggregate scenario (round 2, confirmation)
Reviewed commit: 9d741859dceee935f256b99ebb68e095545b868b
Manifest SHA-256: 7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46
Verdict: REVISE

Reviewer: fresh-context session, no authoring context. I read nothing under
`.syzygy/local/`, no commit message bodies (`git log` was run with
`--format='%h %ad'` only), and consulted no other agent. The detached
checkout at commit `9d74185` was treated as read-only: `git status
--porcelain` returned **0 lines** before I started and **0 lines** after my
last command; every mutation ran in an `rsync -a` scratch copy under
`scratchpad/review-ob-scratch/tree/` (node_modules, `.git` and `dist`
excluded), with each mutated file restored from the checkout afterwards.
Inputs: `AGENTS.md` in full; the package's `REVIEW-BRIEF.md`; the round-1
raw `docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-RAW.md`;
`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`,
`PWB-OPENING-BAND-SCENARIO-MANIFEST.txt`, both `proposed/*.patch` and
`scripts/build_pwb_opening_band_scenario.py` in full; `git diff 59733d3
9d74185 -- <package>`; the PWB specification at the cited line ranges; the
three-surface specification's POC-REQ-032; RFC2-26 at
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`
lines 194–221 (via `DIRECTIVE-REGISTER.md` line 260); the ruling record
`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
in full (102 lines); the M2, M3 and M4 funnels at the cited lines;
`SEMANTIC-DELTA-TEMPLATE.md` and `NORMATIVE-CHANGE-WORKFLOW.md` in
`policy-candidates/`; `scripts/check_governance.py`, `PROJECT-STATUS.md`
and `.github/workflows/governance-docs.yml` at the lines that name this
package; `apps/three-surface-poc/src/polaris.ts` lines 918–933;
`packages/three-surface-poc-core/src/model.ts`'s `PocEpistemic` type.
Class: confirmation round over repaired prose (CC-REV-4, CC-REV-6), against
the brief's twelve criteria plus the round-1 dispositions and the OQ-1/OQ-2
byte question the commissioning message added. The review's `rsync` scratch
copy path in the commissioning message named a session id that does not
exist on disk (`…f4722eaf7d0c`); the checkout and scratch actually live
under `…f4722eeb97c4`, and I used those.

---

## What I ran

All against the checkout unless marked *scratch*. Output is what I read,
not exit codes.

1. `git rev-parse HEAD` → `9d741859dceee935f256b99ebb68e095545b868b`;
   `git status --porcelain | wc -l` → `0` (start) and `0` (end).
   `git merge-base --is-ancestor 59733d3 9d74185` → **no**: the round-1
   commit is not an ancestor of the reviewed commit (rebase-merge), so the
   comparison below is by blob, not by history.
2. `sha256sum PWB-OPENING-BAND-SCENARIO-MANIFEST.txt` →
   `7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46`.
   Computed, never transcribed (rule 3). Equals the value at
   `OWNER-DECISION-PACKET.md` line 28 and the round-1 raw's line 3.
3. `git rev-parse 59733d3:<path> 9d74185:<path>` for every package file
   [Observed]: `PWB-OPENING-BAND-SCENARIO-MANIFEST.txt` (blob
   `43b8adbd…`), `proposed/spec.md.patch` (`45b12133…`),
   `proposed/GOVERNING-DEPENDENCIES.md.patch` (`ceebdb53…`) and
   `scripts/build_pwb_opening_band_scenario.py` (`edbcd982…`) are
   **byte-identical** across the two commits. Four prose files differ:
   `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md` **and
   `REVIEW-BRIEF.md`** (13 lines: its status paragraph, criteria untouched).
   `git diff --stat 59733d3 9d74185` over the package, builder and raw: 5
   files, 400 insertions, 24 deletions, of which 267 insertions are the new
   raw review file — see finding 8 for the fourth prose file.
4. `python3 scripts/build_pwb_opening_band_scenario.py --check` → "PWB
   opening-band scenario manifest matches 11 proposed behavior subjects (2
   patched, 9 unchanged); the proposed declaration equals its regeneration
   and the spec patch composes with the lane B spec patch in both orders",
   exit 0.
5. `--selftest` → "selftest: closed population, byte drift, path order,
   subject drift, patch corruption, lane B composition (both orders and a
   corrupted case), generated-declaration tampering and the
   declaration-patch collision all fail closed", exit 0. Matches criterion
   10's predicate list. Note the selftest's "closed population" is
   `len(BEHAVIOR_SUBJECTS) == 11` at builder lines 265–267 — a check on the
   hard-coded constant, not on the change directory (finding 5).
6. `--diff` → its bytes `cmp` equal to the concatenation of
   `proposed/GOVERNING-DEPENDENCIES.md.patch` then `proposed/spec.md.patch`
   (name order, builder line 110). Identical.
7. `python3 scripts/check_governance.py` → "32 OK, 20 WARN, 0 FAIL (52
   checks) — counts derived, not asserted". The run names this package:
   CG-7d "[subject] SIGN OFF PWB OPENING-BAND SCENARIO — 0 quotation(s), 0
   finding(s), 0 performed digest(s)" and "[registered]
   …/pwb-opening-band-scenario/OWNER-DECISION-PACKET.md — declares 1 current
   and 0 performed-history act(s); 1 current, 0 historical valid". The 20
   WARNs are report-only families (CG-8, CG-22b, CG-23, CG-24, CG-27 etc.);
   CG-27's 17 findings are all in `.syzygy/governance/decisions/README.md`,
   outside this package. `--selftest` → "261 fixtures, 0 failing — a check
   that cannot fail is not a check".
8. **Registration state at `9d74185`** (grep, read): `check_governance.py`
   lines 1548–1553 (`PWB_OPENING_BAND_LABEL/_DIR/_SUBJECT/_ACT`), 1615
   (`PWB_OPENING_BAND_SUBJECTS = PWB_STATE1_SUBJECTS`), 2055
   (`_act_subjects()` entry), 2271–2272 (`ACT_DIGEST_COPY_FILES` row for the
   packet), 2411–2417 (existence-gated activation); `PROJECT-STATUS.md`
   lines 256–257 (both battery lines); `governance-docs.yml` lines 124–128
   (both CI steps). `PWB_SUCCESSOR_CHAIN` (line 1619) has **three** links
   and the comment at lines 1537–1541 says the opening-band package is
   "deliberately NOT a `PWB_SUCCESSOR_CHAIN` link yet" [Observed]. See
   finding 7.
9. **Ledger re-derivation, scripted** (`ledger_rederive.py` in my session
   scratchpad; `git ls-tree -r -z` + `git cat-file --batch` per commit, no
   checkout). Population: `a4a3451` **1,334**, `59733d3` **1,342**,
   `9d74185` **1,376** tracked paths. At every one of the three commits:
   **4** paths fail UTF-8 decode (the four `docs/evidence/*orrery*-2026-09-09.png`
   the ledger names, exactly) and **6** carry a NUL byte (those four plus
   `packages/three-surface-poc-core/src/owner-act-record.ts` and
   `packages/three-surface-poc-core/src/project-shape-coverage.test.ts`)
   [Observed]. Both predicates reproduce the ledger's figures exactly; the
   ledger's "1,343" is `59733d3`'s 1,342 plus the raw review, consistent
   with the branch state it describes. Five pattern sweeps at the baseline
   `a4a3451`, Python `re` and `git grep -l -F` agreeing on every file
   count: `PWB-REQ-010` **36 / 110**; the patched spec path **51 / 113**;
   the patched `GOVERNING-DEPENDENCIES.md` path **9 / 13**; the current
   spec digest (computed as sha256 of the `a4a3451:spec.md` blob, prefix
   `42d073cd`) **13 / 13** — all four reproduce. The continuation form does
   **not** reproduce under the form the corpus actually uses — finding 4.
   At `9d74185` the same sweeps give 45 / 152, 65 / 142, 18 / 32 and 17 /
   17 (the four other P-68…P-83 packages merged in #52 cite the same
   paths); the ledger's baseline figures remain true of `a4a3451`.
10. **Rule 6, six mutations in the scratch copy**, each followed by
    `--check` and a restore from the checkout; baseline in the scratch
    copy passed before and after:
    - M1 manifest row digest flip (`^bd2504cb` → `cd2504cb`, the
      `.openspec.yaml` row) → "manifest differs from exact regeneration
      over the proposed bytes", exit 1. **Caught.**
    - M2 scenario text inside `proposed/spec.md.patch` ("exactly one such
      aggregate" → "at most one such aggregate") → "proposed
      GOVERNING-DEPENDENCIES.md differs from regeneration over the proposed
      spec bytes" and "manifest differs from exact regeneration over the
      proposed bytes", exit 1. **Caught**, on both predicates.
    - M3 the new digest line in `proposed/GOVERNING-DEPENDENCIES.md.patch`
      (`9a44bdb6` → `9a44bdb7`) → the same two lines, exit 1. **Caught.**
    - M4 a new file `NEW-ARTIFACT.md` written into
      `openspec/changes/polaris-project-wide-butlers-model/` → the
      unchanged success line, **exit 0. Not caught** — finding 5.
    - M5 the tree's `spec.md` line 619 drifted ("complete catalog" →
      "whole catalog") → "spec.md.patch does not apply to the base bytes:
      error: patch failed: …/spec.md:618", exit 1. **Caught.**
    - M6 manifest header "# 11 artifacts" → "# 12 artifacts" → "manifest
      differs from exact regeneration over the proposed bytes", exit 1.
      **Caught.**
11. Quotation fidelity, every quoted passage re-read at source: PWB-REQ-010
    (spec.md 596–630) byte-exact; PWB-REQ-007's aggregate sentence and
    Observable (448–450, 457–458) exact; PWB-REQ-020 (906–910) exact;
    RFC2-26 first paragraph (196–204) exact and "Rows are per observable
    consequence, not per clause" at 212 exact; POC-REQ-032 (578–580)
    exact; the P-71 arm and "What it means" cell (record line 58), the
    P-71-Q5 ruling (59), the head's "Nothing here is an act…" (14–16),
    P-75 Q2 (63), the cross-cutting registry-act sentence (75–77) all
    exact; M4 Q7 cell (119) "same region" sentence, "builds the band
    container and owns its single ordering oracle" and the block-order
    sentence exact; M4 827–830 and 836–839 exact; M4 row 3 of the Gate 5
    table (1307): "None found.", "requires the Unknown disclosed **in
    place** in the narrative flow, which an opening aggregate is not", and
    the "**41** approved requirements and **55** scenarios (POC spec 24 and
    24, PWB spec 17 and 31)" denominator all exact — and the 17/31 and
    24/24 counts re-derived by `grep -c '^### Requirement:'` /
    `'^#### Scenario:'` on both specs; M4 rows 4–5 (1308–1309) exact; M2
    443–446 and 472–474 exact; M3 905–909, 914–916 and 922–923 exact.
    Two exceptions: findings 6 and 9. Two line-anchor nits, not findings:
    the delta says "at line 473" for a paragraph that begins at M2 line
    472, and "at line 838" for a paragraph that begins at M4 line 836; the
    quoted text is exact in both.
12. Hygiene sweeps over the package (`grep -n`): the only occurrence of the
    current performed digest prefix `42d073c` is the `-` line of
    `proposed/GOVERNING-DEPENDENCIES.md.patch` (mechanical diff context,
    as round 1 found; CG-7d/CG-7e pass with the packet now registered).
    No 7–16-hex-plus-ellipsis truncated digest anywhere. Every code span
    containing "butler" is a Syzygy `openspec/changes/…` path, not an
    observed-repository path. "accepted/adopted/signed off/approved": every
    hit is either the brief's own criterion text, "either may be adopted
    first", "Approved requirement" quoted from RFC2-26/M4, or the §Review
    disposition vocabulary "Accepted and repaired / withdrawn" (a finding
    being accepted, not an artifact) — nothing labels the offering
    accepted. The phrase "opening band" is absent from
    `proposed/spec.md.patch` (0 hits), as §Terms claims. Label counts:
    delta 8, ledger 12, packet 4 `[Observed|Inferred|Unknown]` labels.
    "Q4" survives only inside the three withdrawal sentences and the M4
    question-table reference at delta line 234.
13. Lane B hunk coverage for OQ-2's (B): `grep -n '^@@'` on lane B's
    `proposed/spec.md.patch` → `@@ -450,22`, `@@ -473,11`, `@@ -907,23`;
    PWB-REQ-007's only scenario heading is spec.md line 470, inside the
    first hunk; the requirement runs 439–486 with exactly one `####
    Scenario` [Observed, heading sweep]. The delta's OQ-2 (b) sentence is
    true at this commit.
14. `git log --format='%h %ad' --date=short -- docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-RAW.md`
    → one commit, `9d74185 2026-09-22`. The raw was added once and its
    blob is what I read.

---

## Round-1 findings — discharged?

### Finding 1 (the ledger's "none did") — **discharged; disposition truthful**

`IMPACT-LEDGER.md` lines 30–40 now enumerate the four decode-failing paths,
name the population they were derived over (1,343) and state which
predicate the figure uses; lines 42–50 add the NUL-byte second method (six
files, the two `.ts` files named) and say the two extra were swept, not
skipped. Both figures reproduce exactly at all three commits (item 9): 4
decode failures, 6 NUL-carrying files, the same paths. The disposition at
`SEMANTIC-DELTA.md` lines 621–628 describes exactly what the diff shows
(`git diff 59733d3 9d74185`, ledger hunk `@@ -24,8 +24,30`). The
"[Observed]" labels at ledger lines 39 and 47 are earned. The sentence
"None can carry any of the five patterns below, so no reported figure
moves" (39–40) is true of the four PNGs. [Observed]

### Finding 2 (OQ-2 not to be rounded off) — **discharged; disposition truthful**

`SEMANTIC-DELTA.md` lines 401–411 and `OWNER-DECISION-PACKET.md` lines
137–144 now carry the precondition wording; both say the package never
asserts RFC2-26 is satisfied, and neither takes a placement. OQ-2 remains
listed as open in both files. The disposition (delta lines 629–636)
matches the diff. No decision was taken inside the delta [Observed]. See
the OQ section below for the effect of the owner's later answer.

### Finding 3 (the "Q4" tag) — **discharged; disposition truthful with one carried quotation drift**

All three prose files now cite the P-74 and P-78 *rows* (ledger 138–145,
delta 514–519, packet 199–202) and say the earlier "Q4" tag was the
package's inference and is withdrawn. I read both rows: P-74's "What it
means" cell (record line 64) closes "The consent record, the registry
entry and PWB-REQ-005 **are** edited on no arm."; P-78's (line 66) closes
"The registry entry **is** edited on no arm." The repair's characterisation
— a whole-row closing sentence, not a sub-question ruling — is correct
[Observed]. The quoted fragment "is edited on no arm", attributed to both
rows, matches P-78 verbatim and P-74 only modulo the verb (finding 9); this
drift pre-dates the repair and the repair did not introduce it.

---

## OQ-1 / OQ-2 — byte determination

**OQ-2 answered "PWB-REQ-010, as drafted" (placement (A)): no byte moves.**
`proposed/spec.md.patch` line 5 (`@@ -618,6 +618,22 @@`) inserts the
scenario after `spec.md` line 619 (the WhatsApp scenario's last bullet)
and before the `warrants` block at 621, i.e. under PWB-REQ-010 (heading at
596, next requirement at 632) — which is placement (A) as
`OWNER-DECISION-PACKET.md` line 123 defines it and as `SEMANTIC-DELTA.md`
line 390 lists it. `proposed/GOVERNING-DEPENDENCIES.md.patch` changes only
the digest line (its lines 9–10) and that digest is a function of the
proposed `spec.md` bytes, which (A) leaves as they are; `--check`
regenerates the declaration from them and passes (item 4). The manifest's
two patched rows therefore stay as they are and the manifest digest above
stands. [Observed against the bytes.] What the answer does *not* do: it
does not by itself discharge the package's own precondition sentence
(delta 401–411; packet 137–144) that the position half and the tuple half
sit under two requirements — that sentence is written "until it is
answered" and says nothing about after; whether choosing (A) is also the
owner ruling that the pair satisfies RFC2-26 limb 1 for slice 3 is the
owner's to state and no byte of this package needs to change for the
package to remain true. Recording the answer *inside* the package would be
a prose edit and would retire this review under rule 10; that is a choice,
not a consequence of the answer.

**OQ-1 answered "a further, separate OpenSpec amendment": no byte of this
package moves.** The package already holds that this scenario clears
RFC2-26 for slice 3 only (delta 375–377; packet 103–106), that slices 4–5
"still need their own RFC2-26 route (OQ-1)" (delta 570–571; packet 226),
and lists the chosen route as (a) at packet lines 111–113. The scenario's
WHEN (patch lines 11–13) names neither the home route nor the surface
descriptors, which is the "reading not taken" (delta 378–381). Nothing in
`proposed/`, the manifest or the builder references slices 4–5. [Observed]

**Consequence for one packet sentence.** `OWNER-DECISION-PACKET.md` lines
218–219: "An answer to OQ-2 or OQ-3 changes the proposed bytes and retires
the review." The OQ-2 answer just given changes no byte, so the sentence
is false as an unconditional; `SEMANTIC-DELTA.md` line 560's "may change"
is the accurate form — finding 10.

OQ-3, OQ-4 and OQ-5: not examined for an answer; treated as open.

---

## New findings

**Finding 4 — revise. The continuation-form figure "0 / 0" and the
sentence "The continuation sweep adds no file: every file it could have
matched also matches the literal identifier [Observed]" are false under the
continuation form this corpus actually uses.** `IMPACT-LEDGER.md` lines
56–59 state the predicate as "a neighbouring requirement identifier
followed by a bare `010` after a comma, slash or space", and lines 85 and
90–91 (and `SEMANTIC-DELTA.md` lines 490 and 495–497) report 0 files, 0
occurrences, adding no file. Run as literally stated — one identifier
immediately followed by `010` — the figure reproduces: 0 / 0 at `a4a3451`
[Observed]. Run over the run form `AGENTS.md` names as the corpus's habit
(`PWB-LIVE-02/03/05/15`), i.e. an identifier followed by any run of bare
three-digit members ending in `010`, it is **6 files / 7 occurrences** at
`a4a3451`, every one the literal `PWB-REQ-001/002/003/004/005/010` (or
`…/002/004/010`, `…/002/003/010`):
`apps/three-surface-poc/src/pwb-mutation-sweep-main.ts`,
`docs/evidence/pwb-p4-2-mutation-sweep-2026-09-04-parity-markers.json`,
`docs/evidence/pwb-p4-2-mutation-sweep-2026-09-04.json`,
`docs/evidence/pwb-p4-2-mutation-sweep-2026-09-06-parity-markers.json`,
`docs/evidence/pwb-p4-2-mutation-sweep-2026-09-09-named-absent-file-dropped.json`,
`docs/reviews/R-PWB-LIVE-EXACT-HEAD-ENGINEERING-RAW.md`. **Five of the six
do not contain the literal `PWB-REQ-010` at all** (`git grep -l -F`,
second method), so the citer population is 41 files, not 36, and class 5's
"remainder of the 36" (ledger line 161) undercounts by five: one
implementation file, three dated evidence records and one retained raw
review. The impact *conclusion* survives — none of the five carries an
obligation the scenario changes (evidence records and raws are never
edited; the sweep main lists identifiers) — but the ledger's stated
purpose for pattern 2 ("a full-identifier sweep alone produces a false
absence", line 59) is exactly what happened, one round after the same
section's first false absence was repaired, and the figure a reader is
given to check is wrong. Criterion 9; rules 2 and 9. Repair: state the
predicate as a regex (runs of any length, the separators, the case), give
the six files, recount the population (41) and class 5 (37), and remove
the "adds no file" sentence or restate it as "adds five files, all in
classes that carry no obligation". `SEMANTIC-DELTA.md`'s table and
sentence at 490–497 move with it.

**Finding 5 — revise. `IMPACT-LEDGER.md` lines 120–121: "The builder's
selftest asserts the population is closed: a new artifact appearing in
the change directory fails `--check`." False.** Mutation M4 (item 10)
wrote a twelfth file into the change directory and `--check` printed its
success line, exit 0. The builder never lists the directory: the eleven
paths are a hard-coded tuple (`BEHAVIOR_SUBJECTS`, builder lines 64–81),
`current_bytes()` reads only those (93–106), and the selftest's "closed
population" is `len(BEHAVIOR_SUBJECTS) != 11` (265–267). The population
*is* closed in the sense that the manifest hashes exactly eleven named
paths and a sibling edit to any of them fails `--check` (M5), which is what
the surrounding paragraph needs; the sentence claims a directory-scan
guarantee the code does not have, about the artifact that would be the
act's argument. Pre-existing at `59733d3` (the Class 2 paragraph was not
touched by the repairs); round 1 did not test it. Criterion 10; rule 6.
Repair: replace the sentence with what the builder does assert — eleven
named paths, any change to an unpatched one fails, a twelfth file is
outside the bound subject and is not hashed — or add the directory scan
and a selftest fixture for it.

**Finding 6 — note. A party quoted through the M4 summary.**
`SEMANTIC-DELTA.md` lines 447–449 (OQ-5) quote "M2 slice 2's stated target
that 'the page's first human-visible instant moves from 58.0% depth into
the opening band'". That sentence does not occur in
`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` (`grep -F` for
"into the opening band" and "moves from": 0 hits outside the Q6 cell,
which does not carry it; M2's own words are line 130 "The first
human-visible instant on the page appears before the first…" and line
185's 58.0% measurement). It occurs only in the M4 funnel's Q7 cell (line
119), as M4's rendering of M2's "own honest target". The substance is
M2's; the words are M4's. Criterion 1 (a paraphrase presented as a
quotation) and criterion 5's "quoted only through another party's summary"
— though OQ-5 is outside the reconciliation section, where all three
parties are quoted from their own packets correctly. Pre-existing at
`59733d3`. `OWNER-DECISION-PACKET.md` line 180–181 paraphrases the same
point without quotation marks and is fine. Repair: quote M2 line 130 or
attribute the sentence to M4 line 119.

**Finding 7 — note. The registration sentences are stale at `9d74185`.**
`OWNER-DECISION-PACKET.md` lines 238–240 ("Three edits were deliberately
**not** made on this branch … listed here so they can be made once, at
merge") and 276–277 ("Until they land, both commands were run by hand"),
and `IMPACT-LEDGER.md` lines 193–197 ("all three are left to merge time")
and 210–212, describe the branch. At the reviewed commit the merge has
happened and the edits are in: `check_governance.py` constants, subject
list, `_act_subjects()` entry, `ACT_DIGEST_COPY_FILES` row and activation
function; both `PROJECT-STATUS.md` battery lines; both CI steps (item 8).
One recommended item was **not** made and deliberately so: the "fourth
link in the PWB successor chain" (packet 250–255) — `check_governance.py`
lines 1537–1541 register the package "on the same terms as the render-mode
package … no `PWB_SUCCESSOR_CHAIN` link until an act fixes the performance
order". The packet labels its chain recommendation [Inferred] and defers
to the owner, so that is not a false sentence; the "not made / until they
land" sentences are the "page restating state it does not own goes stale
silently" shape `AGENTS.md` warns of. Criterion 11. Repair: a dated
sentence at each site saying the registration landed with the merge and
that the chain link was intentionally withheld pending the act, or cite
`check_governance.py` and `PROJECT-STATUS.md` as the owners of that fact.

**Finding 8 — note. §Review names three edited files; four changed.**
`SEMANTIC-DELTA.md` lines 607–610: "The three dispositions below edited
`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md` and `OWNER-DECISION-PACKET.md`
**after** that commit". `REVIEW-BRIEF.md` also differs between `59733d3`
and `9d74185` (blob `de6a85ba…` → `bd4b9818…`; its status paragraph at
lines 10–18, criteria unchanged). Read strictly, the sentence is about
what the *dispositions* edited and the brief edit is a status note, so it
is defensible; read as the package's account of what moved after the
review — which is how the commissioning message read it — it omits the
instrument itself. The verdict was bound to the brief as well as to the
package (rule 10), so the omission should be closed. Repair: name the
fourth file and say the criteria are byte-identical.

**Finding 9 — note. Quotation drift on "is edited on no arm" for P-74.**
`SEMANTIC-DELTA.md` 515–516, `IMPACT-LEDGER.md` 139–140 and
`OWNER-DECISION-PACKET.md` 199–200 quote or state that the P-74 and P-78
rows say the registry entry "is edited on no arm". P-78 (record line 66)
does; P-74 (line 64) says "The consent record, the registry entry and
PWB-REQ-005 **are** edited on no arm." Same substance, different sentence
— rule 8's "nearby prose is not the clause" in miniature. Pre-existing at
`59733d3`; round 1 item 11 verified the "closing sentences in both rows"
without noting the verb. Repair: quote each row's own sentence, or drop the
quotation marks for P-74.

**Finding 10 — note. `OWNER-DECISION-PACKET.md` lines 218–219 overstate.**
"An answer to OQ-2 or OQ-3 changes the proposed bytes and retires the
review." The OQ-2 answer given after round 1 (placement (A)) changes no
byte, as the OQ section shows; `SEMANTIC-DELTA.md` line 560 ("may change")
is the correct form and the packet should match it. Criterion 12 is not
implicated — nothing here reads as authorization — but an owner reading
the packet would expect a byte change that does not come. Repair: "may
change".

---

## Criteria confirmed without exception at `9d74185`

- **2 (change class):** Normative, argued from added obligation (delta
  156–163) against the template's table (`SEMANTIC-DELTA-TEMPLATE.md`
  lines 99–104) and its rule 2 at 111–112. Correct.
- **3 (form):** WHEN/THEN/AND, after the WhatsApp scenario, before
  `warrants`, each clause falsifiable on a rendering (count, displacement,
  same-evaluation read, tuple, no headline status, route per reason,
  population/count equality, in-place member disclosure, reachability,
  machine parity). No bare value.
- **4 (one category, no overlap):** the spec hunk is one contiguous
  insertion at 618–620; lane B's hunks are 450–471, 473–483 and 907–929;
  no hunk of either touches the other's lines and the builder's both-order
  composition passes (items 4, 10). PWB-REQ-007's and PWB-REQ-020's regions
  and the three-surface specification are untouched.
- **5 (reconciliation performed):** M2, M3 and M4 quoted from their own
  packets at 443–446 / 472–474, 905–909 / 914–916, 827–830 / 836–839, each
  traced to a bullet of the proposed scenario (R-1 → THEN "exactly one";
  R-2 → fourth bullet; R-3 → WHEN "project-shape claims"). Finding 6 sits
  in OQ-5, outside this section.
- **6 (contradictions surfaced):** five open questions, each with the
  easier reading named and not taken; the round-1 disposition of finding 2
  promoted wording only. Two of the five have since been answered outside
  the package, binding nothing; the package still lists all five as open,
  which is true of its own bytes.
- **7 (RFC2-26):** the clause at 196–204 requires "an approved OpenSpec
  requirement and scenario"; the M4 table rows 4 and 5 read "None" /
  "Unavailable, both limbs" as quoted; slice 3's row 3 reads "None found"
  with the 41/55 denominator, re-derived. The package claims limb 1 for
  slice 3 only and flags OQ-2 as the precondition; it never claims RFC2-26
  satisfied (`grep -i -F satisf` over the package: 9 hits — the ledger's
  "satisfies the existing scenario", the brief's "would satisfy neither",
  the two OQ-3 titles, the OQ-2 title's "whether … is satisfied", and
  three explicit negations; no affirmative claim).
- **8 (what does not change):** the eight items hold: the spec patch has
  no `-` line; the declaration patch changes one line with "17
  requirement(s), 96 distinct authorities" on both sides; no write verb
  into any repository in the scenario; no implementation file under
  `proposed/`.
- **9 (ledger):** decode-failure and NUL figures reproduce under both named
  predicates (item 9); four of five pattern figures reproduce; the fifth
  is finding 4.
- **10 (manifest and builder):** eleven rows, two patched rows hash
  post-apply bytes (M2/M3 show the spec row and the declaration digest
  line are coupled), nine equal current bytes; five of six external
  mutations caught; the sixth is finding 5.
- **11 (hygiene):** item 12. The four prose heads carry candidate/inert
  banners naming the warrant and the act that would give effect; no byte
  of the signed change directory is edited.
- **12 (scope of authority):** the WHEN at patch lines 11–13 is
  conditional; a rendering with no opening aggregate satisfies the scenario
  vacuously; delta 140–147 and packet 50–53 say so in words; P-71-Q5's "no
  write" is restated at delta 191–195 and packet 58–59. Nothing schedules
  slice 3.

---

## Verdict

**REVISE.**

Rationale. All three round-1 findings are discharged and their dispositions
describe the diff truthfully. No byte of `proposed/spec.md.patch`,
`proposed/GOVERNING-DEPENDENCIES.md.patch`, the manifest or the builder
moved between `59733d3` and `9d74185`; the manifest digest computed here
equals the packet's; `--check`, `--selftest`, `--diff` and the governance
battery read clean; the OQ-2 answer (placement (A)) produces no byte
different from the proposed diffs and the OQ-1 answer touches no byte of
this package. The verdict is REVISE rather than CONFIRM WITH EXCEPTIONS on
findings 4 and 5 alone: both are false sentences in the impact ledger, the
one artifact whose whole claim is re-derivability, in the same section
round 1's finding 1 repaired — a continuation-form absence claim that
fails under the form the corpus writes, and a directory-closure guarantee a
one-line mutation falsifies. Neither touches the proposed bytes, the
manifest, the open questions or the scenario's conditional character; the
repair is prose in `IMPACT-LEDGER.md` and `SEMANTIC-DELTA.md`, and the
re-run it needs is narrow: the ledger's method paragraph, results table and
Class 2 sentence, plus findings 6–10 if the drafter takes them. Findings
6–10 are notes and would not on their own move the verdict off CONFIRM
WITH EXCEPTIONS.
