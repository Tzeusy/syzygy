# R-DOV24 — independent review of PR #123
Verdict: REVISE
Reviewed commit: 31305bc2c10efd663447023dd41ce319c78739fc
Manifest sha256: 3a46186a59d3d18597a011469fc6555ea2613c3a435d36bef2f7e779e62a104f

Reviewer: fresh-context, read-only. Worktree detached at `31305bc` (base
`origin/main` `23b486c`). Package:
`.syzygy/governance/contracts/candidates/pwb-registry-loaded-profile-amendment/`
and `scripts/build_pwb_registry_loaded_profile_amendment.py`. Judged against
the package's own `REVIEW-BRIEF.md` criteria 1–7, P-74 in
`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`, the 2026-09-23 and
2026-09-26 owner records, the act in force, the PWB spec reader definitions,
and `packages/three-surface-poc-core/src/project-shape-{manifest,extraction}.ts`.

Butlers repository paths are written unquoted, never in code spans.

## Commands run and outputs read

1. `python3 scripts/build_pwb_registry_loaded_profile_amendment.py --check` → exit 0.
   Output: "matches the 1 proposed subject (.18 pending: current bytes + .18
   patch); 6 grammar keys added, 15 class-grammar rows, 9 container shapes, 8
   extraction bindings; … every literal found in the specification and the
   code constants". [Observed]
2. `… --selftest` → exit 0, "selftest: 68 predicates … all fail closed".
   [Observed]
3. `python3 scripts/check_governance.py` → "32 OK, 20 WARN, 0 FAIL (52
   checks)". The sorted WARN/FAIL line set is byte-identical to the same run
   over a `git archive 23b486c` tree (`diff` empty), so the PR adds no warning.
   [Observed]
4. `python3 scripts/check_governance.py --selftest` → "265 fixtures, 0
   failing". [Observed]
5. `python3 scripts/check_docs_review_campaign_partition.py` → "total=241
   assigned=241 raw=216 other=25 unmatched=0 overlaps=0". [Observed]
6. Manifest row recomputed independently: `git archive HEAD` into a scratch
   dir, `git apply` the `.18` patch then this package's patch, `sha256sum`
   the subject → equals the manifest's single row; the result parses as JSON.
   (Row digest deliberately not copied here.) [Observed]
7. Criterion 4, structural JSON diff of `.18`-applied bytes vs proposed bytes
   (Python walk): exactly 8 differences — `registryVersion` and
   `entries[0].observerVersion` 1.2.0-candidate.1 → 1.3.0-candidate.1, and ADD
   of the six keys `rootIndex`, `pillars`, `sourcePopulation`,
   `containerShapes`, `classGrammar`, `sourceGrammarSemantics`, appended after
   `precedence`. Criterion 4 met. [Observed]
8. Criterion 5 in a throwaway copy: `--apply --at-adoption` before `.18` →
   "refusing to apply: the .18 act has not been applied", exit 1; `--apply`
   without `--at-adoption` → exit 2. Then `.18`'s builder `--apply
   --at-adoption`; this builder's `--check` → exit 0, "(.18 adopted: current
   bytes)"; `--apply --at-adoption` → subject hashes to the same row as step 6.
   So the bytes are state-independent. But see R7: `--selftest` crashes in
   that state, and `--check` fails after this package's own apply. [Observed]
9. Impact-ledger sweeps re-derived at `23b486c` by (a) Python `re.escape`
   search over UTF-8 text of every `git ls-tree -r -z` path of `23b486c` and
   (b) `git grep -l -F <id> 23b486c`. Denominator 1,540 tracked paths; 1,536
   decode, 4 skipped. All 17 ledger rows reproduce exactly and both methods
   return identical file lists: containerShapes 0, classGrammar 0,
   sourceGrammarSemantics 0, extractionBindings 0, treePopulations 0,
   pillarRootTable 0, ProjectShapeProfile 5, PWB_ROOT_INDEX_PATH 11,
   extractionClassesFor 3, VISION_HEADINGS 4, V1_HEADINGS 4, CATALOG_HEADINGS
   8, PWB_OBSERVER_IDENTITY 5, observationGrammar 18, registryVersion 8,
   observerVersion 39, subject stem 68. Extra identifiers the ledger did not
   sweep (same two methods, agreeing): `sourcePopulation` 10,
   `rootIndexRequired` 5, `rootIndependent` 0, `pillarRootLinks` 0,
   `indexChainDepth` 0. [Observed]
10. Own rule-6 mutations of the restatement witnesses (script imports the
    builder, mutates the proposed JSON, runs `unchanged_findings`,
    `structure_findings`, `spec_findings`, `code_findings` — i.e. everything
    `--check` runs except the manifest comparison, which `--write` would
    regenerate). 18 mutants, 2 killed, 16 survived:

    ```
    SURVIVED M1 purpose/refusals heading texts swapped
    SURVIVED M2 principle heading level 2->3
    SURVIVED M3 catalog headingLevel 3->2
    KILLED   M4 principle container -> top-level-list | container shape declared and never used: ['top-level-decimal-list']
    SURVIVED M5 principle source vision.md -> v1.md
    SURVIVED M6 craft column File -> Path
    SURVIVED M7 roster field name -> id
    SURVIVED M8 rootIndependent true -> false
    SURVIVED M9 roster companion dropped
    SURVIVED M10 pillarRootTable directoryColumn -> Dir
    SURVIVED M11 pillarIndexBasename -> INDEX.md
    SURVIVED M12 pillar-index binding relativePath -> INDEX.md
    SURVIVED M13 baseline binding relativePath -> SPEC.md
    SURVIVED M14 success-criterion v1 itemKey prefix vision:
    SURVIVED M15 containerShapes sentence rewritten
    SURVIVED M16 design-contract heading gets level 1
    SURVIVED M17 project-account key purpose heading 'Non-Negotiable Rules'
    KILLED   M18 pillars label swap (HS<->LL labels) | project-shape-manifest.ts does not carry "  'heart-and-soul': 'Legends and Lore',"
    ```
    M4 was killed only incidentally (the shape became unused). [Observed]
11. Extraction behaviour probed by running the real `project-shape-extraction.ts`
    (copied to scratch, `.js` imports rewritten to `.ts`, Node 24 type
    stripping):

    ```
    ordinal H2 "1st Layer" (sentence admits)          FAILED missing-heading H2 beginning with a decimal ordinal
    ordinal H2 "3a Layer"                             items=1 3a:A
    ordinal H2 first cell not bold                    FAILED malformed-row first column is not a bold label
    ordinal table under H3 inside ordinal H2          items=1 3:A
    no ordinal H2                                     FAILED missing-heading H2 beginning with a decimal ordinal
    principles with 1) marker                         items=2 A | B
    principles empty section                          FAILED malformed-list no top-level decimal list
    principles duplicate bold key                     FAILED duplicate-key A
    principle item without bold                       FAILED ambiguous-leading-label
    principle indented " 1." item only                FAILED malformed-list no top-level decimal list
    success-criterion empty list                      FAILED malformed-list no top-level list
    architecture no H2                                FAILED missing-heading any H2
    design-contract Index at H3                       items=1 R1
    design-contract Index no table                    FAILED malformed-row no table
    design-contract first cell not link               FAILED malformed-row first column is not a link
    design-contract 2nd table malformed only          items=1 R1
    toml name unquoted                                FAILED malformed-toml [butler].name empty or missing
    toml name twice in other table                    items=1 x
    ```
    [Observed]
12. Quotes checked at source: act lines 76–77 of
    `PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` read "An edit to the artifact
    breaks this act's digest binding; changes travel as a / new act." —
    matches SEMANTIC-DELTA.md:64–66. P-74 row (rulings record line 64) contains
    verbatim "Q2 one registry-entry amendment act before slice 5's fifth limb
    only, the first four limbs thread a profile parameter with current
    constants as default", "Slice 5's fifth limb waits for the registry act"
    and "The consent record, the registry entry and PWB-REQ-005 are edited on
    no arm." — all match SEMANTIC-DELTA.md:118–124. "One registry act, not
    two" is at rulings record line 75. Sitting §6 (sitting record lines
    135–150) supports SEMANTIC-DELTA.md:91–99. The current subject's sha256
    appears in the act record (2 occurrences). [Observed]
13. Criterion 6 sweep over the six package files and the builder: one 64-hex
    string in the package, the manifest row; none in any Markdown file; the
    act phrase at OWNER-DECISION-PACKET.md:26–28 carries no digest; no
    "accepted"/"adopted" label on package material ("in force" appears only
    for the act in force). Criterion 6 met. [Observed]

## Findings

### R1 — revise — the restatement check is much weaker than the package says

SEMANTIC-DELTA.md:103–108: "No class, heading, source, shape or key is added
to what the observer reads. `--check` proves the restatement two independent
ways". OWNER-DECISION-PACKET.md:46–51: "How we know it restates today's
reading and adds nothing … Both checks were mutation-tested: 68 deliberately
wrong versions, every one caught".

The witnesses check that literals *exist* (heading text as a quoted substring
anywhere in `project-shape-extraction.ts`, builder `expected_code_lines`
lines ~421–423; heading text anywhere in the reader-definitions block,
`spec_findings`), not that each row binds the right literal to the right
class, source, level or shape. Step 10: 16 of 18 mutants survive, including a
heading moved to a different class (M17), two headings swapped between rows
(M1), a row's source file changed (M5), heading levels changed (M2, M3, M16),
the craft `column`, roster `table`/`field`, `rootIndependent`, `companions`,
`pillarRootTable` column names, `pillarIndexBasename`, the pillar-index and
baseline binding `relativePath`s (the code witness for a `pillar-index`
binding ignores `relativePath`; the `baseline-spec-tree` branch emits only
`return ['baseline-spec'];`), `itemKey` and every `containerShapes` sentence.
None of the 68 selftest predicates targets level, source or row association
[Observed, builder selftest `code_mutants` and step 10].

SEMANTIC-DELTA.md:149–153 does say the check "does not prove the code has no
rule the rows omit" [Observed], but that is about omissions; the two
sentences above claim the rows themselves are proven, and they are not.
Brief criterion 3 ("Name any claim the builder makes that no mutant covers"):
every field named in this paragraph. Either extend the code witness to bind
each row to its constant (e.g. `VISION_HEADINGS.purpose` for key `purpose`,
`oneHeading(doc, 2, …)` levels, `CRAFT_POLICY_FILE_COLUMN`) with a mutant per
field, or narrow both sentences to what is checked.

### R2 — revise — container-shape sentences looser than the code (criterion 2)

Brief criterion 2: "Each says what is read and what fails … a sentence that
is looser or stricter than the code is a finding." Evidence: step 11 and
`project-shape-extraction.ts` line numbers below. [Observed]

- `every-level-2-section` (patch line 153): states no failure. Code
  (extraction.ts:381–382) fails `missing-heading` when the file has no H2.
  The row declares no heading, so `headingMatch` does not cover it either.
- `top-level-decimal-list` (patch 154): omits that a section with no
  top-level list item fails `malformed-list` (extraction.ts:411), and does
  not say "top-level" means column 0 (an indented " 1." is not an item;
  step 11). Accepts `1)` as well as `1.` (extraction.ts:214) — "numbered"
  covers this, acceptable.
- `top-level-list` (patch 155): omits the empty-list `malformed-list`
  failure (extraction.ts:431).
- `first-table-rows` (patch 157): omits "no table under the heading" →
  `malformed-row` (extraction.ts:469). The row-level failures (first cell not
  a whole-cell link, extraction.ts:485; no `File` column or non-link File
  cell, extraction.ts:532–538) appear nowhere as failures.
- `ordinal-section-table-rows` (patch 158): states no failure at all. Code
  fails `missing-heading` when no ordinal H2 exists (extraction.ts:506),
  `malformed-row` on any column-count mismatch in any such table
  (extraction.ts:511) and when a first cell is not exactly one bold span
  (extraction.ts:516). Its ordinal predicate is looser than the code:
  `ORDINAL_H2 = /^(\d+[a-z]?)(?![\w])/` (extraction.ts:500) rejects "1st
  Layer", which the sentence ("begins with a decimal ordinal and an optional
  lowercase suffix") admits (step 11). The sentence copies the spec's words;
  the code is stricter than both.
- `toml-table-field` (patch 160): "anything else fails the source" is
  broader than the code, which ignores a `name` key outside `[butler]` and
  ignores a `name` line in an unrecognised form (it then fails only as
  "missing"). Note-level.
- `heading-section` (patch 152): the `v1-scope` row uses it with two headings,
  and code concatenates both bodies prefixed by their heading texts
  (extraction.ts:396); the shape says "one exact heading". Note-level.

### R3 — revise — rules in the two TypeScript files the rows leave out (criterion 1)

The `scope` sentence (patch 312) says loading the fields "must reproduce the
current source manifest and observation digests byte for byte", and
`missingField` (patch 316) forbids falling back to built-in values. A loader
built from these fields alone could not do that, because these rules are
stated nowhere in the six fields [Observed, read at source]:

- Duplicate item key within a class fails `duplicate-key`
  (extraction.ts:338–348); a missing leading label fails
  `ambiguous-leading-label` (extraction.ts:417, 453–454). The spec states both
  ("A duplicate key in one class is a contradiction"; "unexpected duplicate
  key or ambiguous leading label").
- Key normalization: NFC plus whitespace collapse (`declarationKey`,
  extraction.ts:326); bold by `**` or `__` (extraction.ts:322); the dash after a
  catalog label may be `-`, `–` or `—` (extraction.ts:325); bullets `-*+`
  (extraction.ts:215); fenced code excluded from headings, lists and tables
  (extraction.ts:159–181).
- Pillar-root table: the Directory cell must be exactly one code span ending
  in `/`; the Pillar cell matches the label optionally wrapped in bold or a
  link; only the first table with both columns is read; rows with a wrong
  cell count or unrecognised values are skipped, not failed
  (manifest.ts:268–312, `rootIndexPillarRoots` from 285). `rootIndex.pillarRootTable` names only the columns.
- Pillar-index link grammar and exclusions: inline links and reference
  definitions, images excluded, code spans stripped, fragment/query dropped,
  and the five ignored-link reasons (external, escapes-repository,
  outside-pillar-root, names-a-directory, self) (manifest.ts:120, 175–229,
  449–469).
- Tree rules take precedence over a pillar-named file that is a baseline spec
  or roster `butler.toml` blob (manifest.ts:478); missing or non-blob named
  targets stay counted (manifest.ts:476–486).

Some of these may belong to the discovery grammar rather than
`observationGrammar`, but the package claims a complete restatement under a
no-fallback rule; either state the rules or say explicitly which are left to
code and why the `scope` sentence still holds. [Inferred]

### R4 — revise — the delta misdescribes the pillar-link rule

SEMANTIC-DELTA.md:78: `rootIndex` carries "the link rule used when that
table is absent". Code applies root-index links **always**, after the table,
and a link naming a different root for the same pillar marks it ambiguous
(`declaredPillarRoots`, manifest.ts:365–380). The registry sentence itself
("also declares that pillar's root", patch line 32) is correct; the delta's
table row is not. [Observed]

### R5 — revise — landing order states an order the owner did not rule

OWNER-DECISION-PACKET.md:89–90: "The Polaris gate packages land in this
order: `.21` → `.30` → `.22` → lane B, then `.20` and `.18`." The owner's
ruling (`POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md` §6, lines
110–128; restated unchanged at the close of the 2026-09-26 sitting record,
lines 157–158) fixes only ".21 → .30 → .22 → lane B" for the spec-touching
packages. "then `.20` and `.18`" occurs in exactly one tracked file at
`31305bc`, this packet (`git grep -n -E "lane B, then|then \`?\.20\`? and
\`?\.18"` → 1 hit). The sentence presents an agent ordering as settled and
fuses it with the owner's. Attribute the four-step order to §6 and label
`.20`/`.18`'s position (and this package's "after `.18`", which is a design
constraint of the builder, not an owner ruling) as unruled. [Observed]

### R6 — revise — undisclosed overlap with P-82 Q4's root-independence design

The package introduces `rootIndependent` on each tree population plus a
`rootIndependent` semantics sentence (patch lines 71, 79, 315). P-82 (rulings
record line 70) rules: "Q4 design the root-independence flags in the same
delta" — the M15 CC-REV-2 delta to PWB-REQ-002 (`.15.1`, after `.17`). The M15
funnel (`docs/design/POLARIS-M15-PIPELINE-TRUTHFULNESS-FUNNEL.md` line 72)
designs that flag as `rootIndexRequired` with rule provenance
(`rootIndexRequired` occurs in 5 tracked files at `23b486c`, step 9). This
package names the same concept differently, fixes it in a registry act, and
neither the impact ledger's Table 4 nor the open questions mention P-82 Q4,
M15 or `.15.1`. Disclose the overlap and add an open question (or drop the
flag and leave it to M15's delta). [Observed for the texts; Inferred that
they are the same concept]

### R7 — revise — `--selftest` is unrunnable in the state where the act is performed

After `.18` is applied (step 8), `--selftest` aborts with a traceback:

```
  File ".../build_pwb_registry_loaded_profile_amendment.py", line 552, in selftest
    assert drifted != current
AssertionError
```

The drift mutant replaces `"registryVersion": "1.1.0`, which no longer exists
once `.18` is applied. The packet's "How to verify this package before
acting" (OWNER-DECISION-PACKET.md:156–162) lists `--selftest`, and the act can
only be performed after `.18` (packet :61–62), so the owner's verification
command crashes exactly when it matters. It fails closed, but it verifies
nothing. Brief criterion 5 is met for the bytes and the refusal, not for the
selftest. [Observed]

Related note: after this package's own `--apply --at-adoption`, `--check`
fails ("… (.18) does not apply …") because `base_bytes` no longer recognises
the tree state; the manifest header's "It matches the tree only after
--apply" has no command that confirms it. Note-level. [Observed]

### N1 — note — ledger sweeps half the added keys; one name already in use

IMPACT-LEDGER.md:41 "Six zeros: none of the new key names is used anywhere
yet" — the six zeros are three added keys (`containerShapes`, `classGrammar`,
`sourceGrammarSemantics`) plus three sub-keys; the added keys `rootIndex`,
`pillars` and `sourcePopulation` were not swept. `sourcePopulation` already
occurs in 10 tracked files at `23b486c`, 7 of them code
(`packages/three-surface-poc-core/src/resource-ledger.ts` and its test;
five files in `packages/polaris-generation-core/src/`) (step 9).
SEMANTIC-DELTA.md:147 says "The four new key names occur in no tracked file
today", which matches neither the ledger's six nor the six added keys.
[Observed]

### N2 — note — "exact constant source lines" overstates the heading witness

SEMANTIC-DELTA.md:106–108 says heading texts "appear as the exact constant
source lines in the two TypeScript files". The witness checks
`'<heading text>'` as a substring anywhere in `project-shape-extraction.ts`
(builder, `expected_code_lines`), not the constant's line. [Observed]

### N3 — note — question 3 offers only one reading

Question 3 (OWNER-DECISION-PACKET.md:129–133) is a genuine owner question
[Inferred]. The same stock sentence recurs in other rows (P-78, line 66: "The
registry entry is edited on no arm."), and the act in force distinguishes an
*edit* from a new act (step 12). So a second reading exists besides the
packet's: "edited" means an in-place edit outside an act, which Q2's act is
not. The packet should put both readings to the owner. [Inferred]

### N4 — note — the other open questions are genuine

Checked against the 2026-09-23 record (§1 answered `.18` OQ3 only; §6
landing order) and the 2026-09-26 sitting (§6 authorizes N8 drafting only):
none of questions 1, 2, 4, 5, 6, 7, 8 is already ruled. Question 8's quote
"One registry act, not two" is accurate to line 75 of the rulings record,
which scopes it to P-69 Q2(a) and P-72 Q2. Question 5 asks about version
numbers, which the brief lists as out of scope for review; harmless.
[Observed]

### N5 — note — inconsistent heading-level encoding

The catalog row uses `headingsFrom` + `headingLevel: 3` (patch 264–265), while
every other row uses `heading.level`. `structure_findings` range-checks
`heading.level` but never checks `headingLevel`. [Observed]

## Criteria summary

| # | Result |
|---|---|
| 1 Pure restatement | Not shown; omitted rules named in R3; R1 shows row associations unchecked |
| 2 Nine shape sentences exact | No: R2 (five looser, two note-level) |
| 3 Verifies, meaningfully | `--check`/`--selftest` pass; 16 of 18 of my mutants survive (R1); selftest crashes post-`.18` (R7) |
| 4 Nothing else changed | Met (step 7) |
| 5 Stacking on `.18` | Bytes identical in both states and early apply refused (step 8); selftest not state-independent (R7) |
| 6 No act argument / authority claim | Met (step 13) |
| 7 Open questions honest | Genuine (N4); Q3 should carry both readings (N3); landing-order text overstates the ruling (R5); P-82 Q4 overlap missing (R6) |

Verdict: REVISE
