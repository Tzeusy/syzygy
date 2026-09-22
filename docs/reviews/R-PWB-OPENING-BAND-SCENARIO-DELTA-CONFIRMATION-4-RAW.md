# Review — Polaris opening-band aggregate scenario package (round 5, fresh context)
Reviewed commit: 7fd2db355ef2742cc5ac792ef571d19a05613f8e
Manifest SHA-256: 7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46
Verdict: REVISE

Reviewer: fresh-context session, no authoring context (CC-REV-1). Read-only
against a detached worktree at the reviewed commit; every mutation and every
patch composition ran in a copy under the session scratchpad, never in the
worktree. Inputs: the package in full (`SEMANTIC-DELTA.md`,
`IMPACT-LEDGER.md`, `PWB-OPENING-BAND-SCENARIO-MANIFEST.txt`,
`OWNER-DECISION-PACKET.md`, `proposed/spec.md.patch`,
`proposed/GOVERNING-DEPENDENCIES.md.patch`,
`scripts/build_pwb_opening_band_scenario.py`), `REVIEW-BRIEF.md` in full,
the governing references it names, the two 2026-09-23 owner decisions, the
M2/M3/M4 funnels, the semantic-delta template and the normative-change
workflow, `DIRECTIVE-REGISTER.md` for clause sites, and the five retained
raws for disposition checking only. The verdict is formed over the bytes at
`7fd2db3`.

The verdict rests on one finding (23). Findings 24–30 are notes. The
repair for 23 is one clause; nothing in the patches, the manifest or the
builder needs to move.

---

## Findings

Numbering continues from 22.

**Finding 23 — revise. `SEMANTIC-DELTA.md` lines 632–634: "the reviewer's
machine findings (items 2–10 and 13–16 of the raw) still hold at this
commit" is false for two of the fourteen items it names.** Criterion 9 and
11; rules 4 and 10.

- [Observed] Item 9 of `docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-RAW.md`
  (lines 65–76) records "the continuation-form pattern (0/0)" and "all five
  reproduce exactly". At the reviewed commit the package's own
  `IMPACT-LEDGER.md` line 96 gives that pattern 6 files / 7 occurrences,
  and `SEMANTIC-DELTA.md` §Review round 2 finding 4 (lines 692–699) says
  the 0/0 figure "were false". Item 9 therefore does not hold at this
  commit; the file contradicts itself across lines 633 and 692.
- [Observed] Item 13 of the same raw (lines 106–123) cites
  `apps/three-surface-poc/src/polaris.ts` "lines 920–931" for
  `gapReasonCounts`. At `7fd2db3` the function occupies lines 951–960
  (read at source; body identical). The item's substance — only
  `reasons.primary` is read — holds; its line pointer does not, which is
  the same drift round 4 finding 21 repaired in the delta's own text.
- [Observed] The sentence's evidence bracket, "[Observed: builder `--check`
  and `--selftest` re-run after the repairs]", covers items 3 and 4 only.
- [Inferred] The sentence was true when written (the ledger still said 0/0
  at `9d74185`, which is why round 2 found it there) and went false when
  the round-2 repair moved the ledger's figure at `76b4beb`; rounds 3 and
  4 did not re-read this paragraph against the repaired ledger.

Correct text: anchor the claim to a commit and except the two items —
e.g. "the reviewer's machine findings (items 2–10 and 13–16 of the raw)
held at the round-1 disposition commit; at this commit item 9's
continuation-form figure (0/0) is retracted by round 2 finding 4, and item
13's `polaris.ts` line range has moved (round 4 finding 21); the rest
hold." Mark at the sentence; do not delete it (it is quoted by nothing
else in the package, but the project's own lesson is to mark staleness in
place).

**Finding 24 — note. `SEMANTIC-DELTA.md` lines 358–360: "RFC2-26, quoted at
the defined clause (… `rendering-vocabularies.md` line 196)" — the quoted
sentence does not sit at line 196.** Criterion 1; rule 8. [Observed] The
clause **RFC2-26** opens at line 196 (`DIRECTIVE-REGISTER.md` line 260
agrees); the sentence quoted at lines 362–365 of the delta ("Before
implementation, every observable consequence either maps … no
independently testable behavior.") sits at lines 201–205 of the RFC
module. The words are byte-exact. The Evidence section (delta line 244)
gives the whole clause as 196–221, which contains them. Correct text:
"lines 201–205, inside the clause defined at line 196".

**Finding 25 — note. `SEMANTIC-DELTA.md` lines 236–237: "the slice 3, 4
and 5 designs (lines 820–914)" — the range ends on the next slice's
heading.** Criterion 1. [Observed] In
`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md`, `### Slice 3` opens at 820,
slice 5's last text line is 912, 913 is blank and 914 is `### Slice 6 — Run
the return path once`. Correct: 820–913.

**Finding 26 — note. `SEMANTIC-DELTA.md` line 239: "`POLARIS-M2-…` lines
441–480 — slice 2, the currency probe" — the range is a fragment of the
slice, not the slice.** Criterion 1. [Observed] `### Slice 2 — The evidence
horizon` opens at 441 and the next heading, `### Slice 3`, is at 514. The
two passages the delta quotes lie at 443–446 and 472–475, inside 441–480,
so nothing quoted is misplaced. Correct: "lines 441–513" or "lines 443–446
and 472–475".

**Finding 27 — note. A tension the delta does not surface: which reading
of PWB-REQ-020's population reaches an aggregate.** Criterion 6 (rule 6 of
the template). [Observed] The delta's "What does NOT change" item 3 (lines
180–183) states that the aggregate is inside PWB-REQ-020's parity
population "which PWB-REQ-020's own text already reaches through 'or
disclosure Polaris presents'", and the scenario's fourth bullet writes
"the machine answer carries the same aggregate under PWB-REQ-020" on that
reading. The delta's own party 1, the M2 funnel, flags the alternative at
`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` lines 462–464: "the
clause's Case attaches 'disclosure' to the PWB-REQ-022 judgment state, so
on the narrower reading the probe's facts fall outside the enumerated
population entirely". The Case at spec lines 912–914 reads "every
PWB-REQ-005 authority state and PWB-REQ-022 judgment state and disclosure".
[Inferred] The wider reading is the one that lets this scenario land
without touching PWB-REQ-020; the narrower one would make the fourth
bullet a scope claim about a requirement the package says it does not
amend — the same shape OQ-3 refuses for PWB-REQ-007. The wider reading is
defensible (the Mutation-proof line's "disclosure marker class" is broad),
so no sentence is false; but the reading is taken rather than named. Owner
answers to OQ-1–OQ-5 do not touch it. Suggested: name both readings beside
item 3 (an OQ-6, or a sentence stating which is taken and why).

**Finding 28 — note. `OWNER-DECISION-PACKET.md` lines 3–6: the head banner
does not itself name the owner act that would give the package effect.**
Criterion 11. [Observed] The banner says "Inert offering. This packet
performs nothing … authorizes no implementation"; the act is named lower
on the same page (the manifest paragraph at 34–43 and step 3 at 248–250),
and every other file head names it in the banner. Rounds 1–4 passed
criterion 11 on these bytes; recorded only because the criterion says
"every file head".

**Finding 29 — note. `SEMANTIC-DELTA.md` lines 371–372: "this
specification's subject, which its own proposal states as the declared
shape of the configured project" is a paraphrase, not a quotation, and is
not marked as one.** Criterion 1. [Observed] `proposal.md` §Scope (lines
88–91) reads "all project shape declared by its authoritative project
artifacts: purpose and boundaries, architecture, V1 scope and success
criteria, and the declared … catalogs"; "declared shape of the configured
project" occurs nowhere in `proposal.md` (fixed-string sweep, 0 hits). The
sentence is not presented in quotation marks, so criterion 1 is not
breached; noted because the sweep was to be exhaustive.

**Finding 30 — note. The current specification source digest appears in
`proposed/GOVERNING-DEPENDENCIES.md.patch` (its `-` line) while
`IMPACT-LEDGER.md` lines 73–76 say it "is **not** reproduced anywhere in
this package's prose".** Criterion 11. [Observed] Both true: a unified diff
must carry the line it removes, and the patch is not prose. CG-7e and
CG-15 pass on the battery at this commit (32 OK, 20 WARN, 0 FAIL). No
change needed; recorded so a later reader does not count the patch as a
prose copy.

---

## Internal cross-reference sweep

**Method and denominator.** Python `re` over the four prose files
(`SEMANTIC-DELTA.md` 884 lines, `IMPACT-LEDGER.md` 313, `OWNER-DECISION-
PACKET.md` 316, `REVIEW-BRIEF.md` 161) extracting every line pointer,
section/cell/§ reference, step number, finding number, item number, round
word or round count, row reference, number-word count claim, filename
token and seven-hex commit token. The extractor is deliberately
over-inclusive: **496 matches**, of which a small number are false
positives (e.g. "P-78 rows", "2026-09-21 review", "finding by finding",
"1 files" inside an identifier) and are marked as such below. Every
non-false-positive pointer was resolved against its target at `7fd2db3`;
line pointers to quotations were checked to land on the quoted text.

| Category | Matches | Resolve exactly | Do not resolve exactly |
|---|---|---|---|
| Line pointers (`line N`, `lines N–M`) | 24 | 21 | 3 — delta 236–237 "820–914" (finding 25); delta 239 "441–480" (finding 26); delta 359–360 "line 196" for a quotation at 201–205 (finding 24) |
| Section / cell / § / Gate references | 29 | 29 | 0 (every "§Review finding N" lands on the numbered disposition; "What it means" cells, Gate 5 at M4 1031–1453, PROJECT-STATUS §"How to verify this page" at line 227 all resolve) |
| Step numbers | 4 | 4 | 0 (delta migration step 1 and packet step 1 both name four rounds and a round 5; "step 4" is quoted as the withdrawn label) |
| Finding numbers (1–22, A, B) | 41 | 38 | 0 unresolved; 3 false positives ("finding b" = "finding by finding" ×3). Round 1 = 1–3 (all notes); round 2 = 4–5 revise, 6–10 note; round 3 = 11, 13, 14 revise, 12, 15–18 note; round 4 = 20 revise, 19, 21, 22 note; B = A, B — all match the retained raws |
| Item numbers | 1 | 1 resolves as a pointer; content stale (finding 23) | see finding 23 |
| Round words and round counts | 66 | 66 | 0 ("Done four times", "four reviews", "three notes", "five notes", "one revise finding and three notes", "no byte … moved in three rounds", "six sites", "six mutations", "all four sibling spec patches" all reproduce against the raws or against my own re-runs) |
| Row references (P-68…P-78, manifest row 8) | 6 | 6 | 0 (row 8 of the manifest is `contract-coverage-matrix/RFC-0007-0009.md`) |
| Count claims | 101 | all claim-bearing ones reproduce | 0 false; ~12 false positives from numbers inside identifiers or dates |
| Filename tokens | 189 (59 distinct) | 57 distinct exist as tracked files or basenames at `7fd2db3` | 2 distinct are non-existent by design: the `-RAW.md` suffix pattern (brief line 159) and the future `PWB-OPENING-BAND-SCENARIO-ACT.md` (packet line 283, "would" register) |
| Commit tokens | 35 (6 distinct) | 6 | 0 — `59733d3` 2026-09-21, `a4a3451` 2026-09-21 (merge-base of the branch: [Observed]), `9d74185` 2026-09-22 with "(#52)" in its subject, `76b4beb` 2026-09-23, `194f8cd` 2026-09-23, `dfb605c` 2026-09-23 with the package byte-identical to `9d74185` ([Observed] empty diff) |
| "carries / does not carry PWB-REQ-010" claims | 4 | 4 | 0 — `CAPABILITY-COVERAGE.md` ×1, `contract-coverage-matrix/RFC-0007-0009.md` ×4, neither class-3 JSON, no class-4 file, `pwb-mutation-sweep-main.ts` run-form only — each re-swept at `a4a3451` |

Total swept: **496**; not resolving exactly: **3** (all line-range
imprecisions, findings 24–26, none making a sentence false) plus the one
stale content claim behind an item pointer (finding 23).

**Quotation fidelity, every quotation read at source** (criterion 1): PWB-
REQ-010 (spec 596–630), PWB-REQ-007's aggregate sentence (448–450) and
Observable (457–458), PWB-REQ-020 (906–910), the proposed scenario (equal
to the patch's `+` lines), the P-71 row's arm and "What it means" cell and
the record head's "Nothing here is an act …" (ruling record lines 58 and
14–16), P-74 and P-78 closing sentences (lines 64, 66), P-75 Q2 (line 63),
M4 Q7 cell (line 119: "same region", "builds the band container and owns
its single ordering oracle", "own honest target", the block-order
reservation), M4 slice 3 (827, 836), M4 Gate 5 table cells ("None found.",
"Unavailable", 41/55, "None — the three sweeps …", "in place … which an
opening aggregate is not"), M2 (443–446, 472–475, Q6 cell line 50, success
criterion 4 at 130–131), M3 (905–909, 914–916, 922–923), RFC2-26 (196–221
including "Rows are per observable consequence, not per clause."),
POC-REQ-032 (578–580 and Observable 589–590), the template's change-class
table and rules 2, 6, 7 and its "I only touched X" line, lane B hunks
(`@@ -450,22`, `@@ -473,11`, `@@ -907,23`; PWB-REQ-007's only scenario at
spec 470), the sibling currency-disclosure patch (`@@ -469,3`),
`PocEpistemic`'s Unknown arm (`model.ts` line 42), `gapReasonCounts` at
`194f8cd` 951–960 and `a4a3451` 922–931, the owner's OQ answers (OWNER-
VALUES lines 79–88; OPEN-QUESTIONS lines 33–62). All byte-exact where
presented as quotations, with the three range imprecisions noted above.

---

## Builder

Run from the worktree root at `7fd2db3`:

- `--check` → exit 0: "PWB opening-band scenario manifest matches 11
  proposed behavior subjects (2 patched, 9 unchanged); the proposed
  declaration equals its regeneration and the spec patch composes with the
  lane B spec patch in both orders".
- `--selftest` → exit 0: "selftest: closed population, byte drift, path
  order, subject drift, patch corruption, lane B composition (both orders
  and a corrupted case), generated-declaration tampering and the
  declaration-patch collision all fail closed" — the nine predicates
  criterion 10 names, exactly.
- Manifest semantics (criterion 10) re-derived by hand: `sha256sum` over
  the eleven current files equals the manifest row for the nine unpatched
  paths and differs for `spec.md` and `GOVERNING-DEPENDENCIES.md`; after
  applying both patches in a scratch export of the change directory the
  two files hash to the manifest's rows 11 and 5 exactly [Observed]. The
  proposed scenario sits at post-apply lines 621–635, after the WhatsApp
  scenario (615) and before the `warrants` fence (637).
- `sha256sum` of the manifest → the value on line 3 above, equal to the
  packet's copy (line 40) and to every prior raw's.
- The manifest, both patches and the builder are byte-identical at
  `59733d3`, `9d74185`, `76b4beb`, `194f8cd` and `7fd2db3` (git blob ids
  equal at all five) [Observed].

**Mutations (rule 6, criterion 10), eight, each in a scratch copy holding
`scripts/`, the two openspec change directories and the two candidate
packages, baseline `--check` passing before and after each; failure text
read, not the exit line:**

| # | Mutation | Failure text |
|---|---|---|
| M1 | append a line to unpatched `design.md` | "manifest differs from exact regeneration over the proposed bytes" |
| M2 | flip one hex char of the manifest's `spec.md` row | "manifest differs from exact regeneration over the proposed bytes" |
| M3 | swap manifest rows 8 and 9 | "manifest path population or order differs" |
| M4 | edit the patch's added text ("exactly one" → "at most one") | "proposed GOVERNING-DEPENDENCIES.md differs from regeneration over the proposed spec bytes" + "manifest differs …" |
| M5 | hand-edit the declaration patch's `+` totals (96 → 97) | same two lines as M4 |
| M6 | remove lane B's `spec.md.patch` | "missing lane B spec patch: …pwb-scoped-attributes-amendment/proposed/spec.md.patch" |
| M7 | delete `GOVERNING-DEPENDENCIES.md.patch` | "proposed/*.patch population differs from the declared patched subjects: spec.md.patch" + "declared patched subject is byte-identical: …GOVERNING-DEPENDENCIES.md" + the M4 pair |
| M8 | drift spec line 618 (the patch's context line) | "spec.md.patch does not apply to the base bytes: error: patch failed: …spec.md:618" |

All eight fail closed with distinct, correct text.

**Composition, independent of the builder:** this package's `spec.md.patch`
applied with each of the four sibling `proposed/spec.md.patch` files
(scoped-attributes, missing-currency-disclosure, machine-view,
exact-source-render-mode) in both orders via `git apply` on a clean copy of
the current spec; every pair applies in both orders and yields one digest
per pair [Observed]. This confirms `IMPACT-LEDGER.md` lines 304–309 and
round 4's sibling claim.

**Governance battery:** `python3 scripts/check_governance.py` at `7fd2db3`
→ "32 OK, 20 WARN, 0 FAIL (52 checks)". CG-7d lists "SIGN OFF PWB
OPENING-BAND SCENARIO — 0 quotation(s), 0 finding(s), 0 performed
digest(s)" and the packet as a registered copy with "1 current, 0
historical valid". No WARN names this package.

---

## Impact ledger re-derivation

**Method.** Python `re` over every blob of `git ls-tree -r -z a4a3451`
(the ledger's baseline), decoded as UTF-8, undecodable blobs skipped; the
five patterns as the ledger states them, including its regex
`PWB-REQ-\d{3}(?:(?:/|,\s|\s)\d{3})*?(?:/|,\s|\s)010\b`. Second method:
`git grep -l -F` (and `-P` for the regex) at `a4a3451`. Denominator:
**1,334** tracked blobs [Observed].

| Figure | Ledger | Re-derived | Second method |
|---|---|---|---|
| tracked files | 1,334 | 1,334 | — |
| undecodable | 4 (the four PNGs named) | 4, same paths | — |
| NUL-carrying | 6 (four PNGs + the two `.ts`) | 6, same paths (at 1,334; the ledger states it over the 1,343 branch population) | — |
| `PWB-REQ-010` | 36 / 110 | 36 / 110 | 36 files |
| continuation forms | 6 / 7 | 6 / 7 | 6 files |
| spec path | 51 / 113 | 51 / 113 | 51 |
| declaration path | 9 / 13 | 9 / 13 | 9 |
| current source digest | 13 / 13 | 13 / 13 | 13 |
| run-only adds | 5, named | the same 5 | — |
| citer union | 41 | 41 | — |

**Class 5 (39):** placing each of the 41 union citers in exactly one kind:
implementation and tests 6, generated coverage views 4, design packets 2,
retained raws 11, dated evidence records 12 (ten `docs/evidence/*.json` +
two `docs/pursuits/2026-09-13-*.json`), plan + dated review 2, pending
register 1, other spec's design note 1 = **39**, plus the two class-1
files = 41. Every path the ledger names is in my list and no citer is
unplaced [Observed]. One raw and three evidence records reach the class
only through the run form, as stated.

**Class 2:** `CAPABILITY-COVERAGE.md` ×1 and
`contract-coverage-matrix/RFC-0007-0009.md` ×4 carry the literal; no other
manifest row does [Observed]. **Class 3:** both JSON declarations carry the
current source digest and neither carries `PWB-REQ-010` [Observed].
**Class 4:** the four history files (two performed PWB act records and
their two candidate-package manifests) are in the digest/path sweeps and
none carries `PWB-REQ-010` [Observed]; the ledger does not enumerate them
by path, which is consistent with citing act records by path only.

**Branch population:** `59733d3` has 1,342 tracked files (1,334 + the
package's eight); the branch tip `origin/agent/gate-opening-band-scenario`
(`3ee1b0b`) has 1,343 [Observed], matching ledger lines 34–35. Baseline
`a4a3451` is the merge-base of that branch [Observed].

All figures reproduce; the class-3 finding is labelled [Observed] for the
pins and [Inferred] for the repair's home, as criterion 9 requires.

---

## Per-criterion summary

| # | Criterion | Result |
|---|---|---|
| 1 | Quotation fidelity | **Pass** — every quotation byte-exact at source; three line-range imprecisions (24, 25, 26), none misplacing a quoted word |
| 2 | Change class | **Pass** — Normative is correct under the template table (an obligation is added; a renderer with two opening aggregates or a tuple-less one complied before and does not now); argued from obligation, not diff size |
| 3 | Scenario form | **Pass** — WHEN/THEN/AND, post-apply lines 621–635, after the existing scenario, before `warrants`; every clause is falsifiable on an inspectable rendering or machine answer (count of aggregates, category order, evaluation identity, tuple fields, route per counted reason, population/count equality, per-member disclosure and reachability, machine parity); no clause states a value |
| 4 | One category, no overlap | **Pass** — the patch touches spec 618–621 only; lane B's hunks are 450–483 and 907+; the P-69 Q7a sibling inserts at 469; the P-75 Q1 package is against the other specification; composition verified in both orders with all four siblings |
| 5 | Reconciliation performed | **Pass** — three parties named from the M4 Q7 cell, each quoted from its own packet at verified lines, each agreement (R-1, R-2, R-3) tied to a scenario clause; P-75 Q2 quoted from the ruling record |
| 6 | Contradictions surfaced, not settled | **Pass with note 27** — OQ-1 to OQ-5 are genuine, each names the easier reading and does not take it, each is left to the owner (and now answered by plain direction with no proposed byte moved); one further reading tension not named (PWB-REQ-020's "disclosure") |
| 7 | RFC2-26 | **Pass** — both halves hold against the clause at 196–221: limb 1 supplied for slice 3 only, conditioned on OQ-2 (now answered (A)); slices 4–5 remain unmapped on M4's own eight-row table and are routed to `syzygy-dov.26` by the OQ-1 answer |
| 8 | What does not change | **Pass** — all eight items true against the patches: no requirement minted, `warrants` byte-identical, 17/96 unchanged, no implementation file, no observed-repository write (P-71-Q5 quoted correctly) |
| 9 | Impact ledger | **Pass with finding 23** — every figure reproduces by two methods; the class-3 labelling is correct; the stale sentence is in the delta's §Review, not the ledger |
| 10 | Manifest and builder | **Pass** — eleven rows, two post-apply and nine current, verified by hand; selftest names the nine predicates; eight independent mutations fail closed with correct text |
| 11 | Governance hygiene | **Pass with notes 28, 30** — no performed act argument or truncated signed digest quoted in prose; act records cited by path; no observed-repository path in a code span (battery CG-1b clean); banners present; claims labelled; nothing labelled accepted; signed change directory untouched |
| 12 | Scope of authority | **Pass** — nothing performs an act or schedules work; the scenario is conditional ("WHEN … renders an aggregate"), so a conforming implementation may render no opening aggregate; the packet says so at lines 62–65 |

---

## Prior findings 1–22 — all dispositioned

Each of findings 1–22 in the four raws has a numbered disposition in
`SEMANTIC-DELTA.md` §Review (1–3, 4–10, 11–18, 19–22), and the parallel
round's A and B are recorded (delta 731–746). I re-checked the four
repairs round 4 required or noted: 19 (delta 570–575 now names four rounds
and a round 5), 20 (ledger 199–209 and 221–227 name both class-2 citers,
verified ×1 and ×4 at `a4a3451`), 21 (delta 248–249 and 418–419 carry
both ranges, verified at both commits), 22 (M2 472 and M4 836, verified).
All discharged with truthful dispositions.

---

## Verdict rationale

**REVISE.** One sentence in the package is false at the reviewed commit:
`SEMANTIC-DELTA.md` line 633's claim that round-1 raw items 2–10 and 13–16
"still hold at this commit", when item 9's continuation-form figure is
retracted two subsections later in the same file and item 13's line range
has moved. It is the class rounds 2–4 returned REVISE on — a sentence made
false by a later repair and not re-read — and it needs marking at the
sentence before the package goes to the owner. Everything else holds: the
bound bytes are unchanged across five commits, the builder and eight
mutations behave, every ledger figure reproduces by two methods, every
quotation is exact, and the three range imprecisions and the unsurfaced
PWB-REQ-020 reading are notes. A round 6 over the repaired bytes may be
confined to the §Review paragraph and any text the repair touches, since
no other statement in the four prose files failed to resolve.
