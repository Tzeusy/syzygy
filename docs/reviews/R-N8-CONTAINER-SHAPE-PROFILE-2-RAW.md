# R-N8-2 — confirmation review of PR #124
Verdict: REVISE
Reviewed commit: c1035231e1f19c0fcb26a0c6ce755687555925d5
Manifest sha256: c8e2cfef5a7e62bf8fd396b7d238b7b73fc91b5e90007ca70d1921edf2020ab0

Reviewer: fresh-context, read-only confirmation reviewer dispatched by the
team lead, 2026-09-27. Subject: PR #124, `origin/agent/tier4-n8` at the
commit above (parent `cefca2d`, base `08d4d02`): the package
`.syzygy/governance/contracts/candidates/pwb-container-shape-profile-amendment/`,
`scripts/build_pwb_container_shape_profile_amendment.py` and its
`scripts/check_governance.py` registration. Detached worktree at the reviewed
commit; nothing in the main checkout or any branch was edited, nothing
pushed. The manifest digest in the head above was re-derived (command 2) and
equals the dispatch's value. `syzygy-dov.24` material read: only `SHAPES`
and `ITEM_KEY_SENTENCES` of its builder at `1395d44` (plus running its
`--check`, output read, source not read). Bare-digest copies escaping CG-7e
(`syzygy-eau`) are known and not re-reported.

## Commands run and output read

1. `git worktree add --detach … c103523`; `git diff --stat origin/main...HEAD`
   → 13 files, the package's 8, the builder, `check_governance.py`,
   `check_docs_review_campaign_partition.py`, `docs/README.md`, the round-1
   raw [Observed].
2. Manifest digest, two methods: `sha256sum` and Python `hashlib` over
   `PWB-CONTAINER-SHAPE-PROFILE-MANIFEST.txt` → both
   `c8e2cfef5a7e62bf8fd396b7d238b7b73fc91b5e90007ca70d1921edf2020ab0`, equal
   to the two packet copies (`OWNER-DECISION-PACKET.md:24`, `:166`)
   [Observed].
3. Builder `--check` → "matches 11 proposed subjects (3 patched, 8
   unchanged); 9 shapes, 8 key forms, 8 profile rules, 9 loaded-profile
   rules, the hoisted exactness bullet, 10 PWB-REQ-002 rules, 3 scenarios,
   the retained Butlers grammar, dependency and contract-coverage
   regeneration and 12 declared sibling-composition outcomes verify" plus
   "shape and key-form sentences are a copy: … is not in this tree, so they
   are compared only once it lands", exit 0 [Observed].
4. Builder `--selftest` → "selftest: 106 mutants killed — …", exit 0
   [Observed].
5. `python3 scripts/check_governance.py` → "32 OK, 20 WARN, 0 FAIL (52
   checks)", exit 0; CG-7d subject line "SIGN OFF PWB CONTAINER-SHAPE
   PROFILE AMENDMENT — 1 quotation(s), 0 finding(s), 0 performed digest(s)"
   [Observed]. `--selftest` → "268 fixtures, 0 failing", exit 0 [Observed].
6. `python3 scripts/check_docs_review_campaign_partition.py` →
   "total=246 assigned=246 raw=221 other=25 unmatched=0 overlaps=0", row
   "N8 container-shape profile gate 1", exit 0; `ls docs/reviews | wc -l`
   → 246 [Observed].
7. `git archive HEAD openspec` to a scratch dir, `git apply` of the three
   patches (all applied), `openspec validate polaris-project-wide-butlers-model
   --strict` (openspec 1.9.0 on PATH) → "Change
   'polaris-project-wide-butlers-model' is valid" [Observed].
8. Python byte comparison, base vs patched `spec.md`: the nine Butlers class
   bullets are byte-identical (True); the hoisted exactness bullet equals the
   base paragraph whitespace-folded after the "For every grammar, loaded or
   built-in," opening (True); patched file is NFC (True) [Observed].
9. Shared text with `syzygy-dov.24` (its builder at `1395d44` copied into the
   worktree `scripts/`, removed afterwards):
   - `--check` with it present → "shape and key-form sentences match the
     loaded-profile amendment's builder", exit 0 [Observed].
   - `shared_text_findings(module)` with in-memory mutants: `tree-path`
     sentence edited → "shape sentences differ…"; `craft` key sentence edited
     → "key-form sentences differ…"; an extra key form added → key-form
     finding; trailing space on `heading-section` → shape finding. All killed
     [Observed].
   - On-disk mutants of the copied builder: a full stop added to `tree-path`
     → `--check` prints "does not verify: shape sentences differ…"; a full
     stop added to `fixed` → exit 1. Killed [Observed].
   - `syzygy-dov.24` worktree at `1395d44` with N8's `spec.md.patch` applied:
     its `--check` exit 0 ("… 15 class-grammar rows, 9 container shapes, 8
     extraction bindings …"); N8's `shared_text_findings()` on that tree → `[]`
     [Observed]. Worktree removed.
10. Shape and key sentences read against
    `packages/three-surface-poc-core/src/project-shape-extraction.ts`:
    `sectionOf` 190, `bodyText` 199, `ORDERED_ITEM`/`UNORDERED_ITEM` 214-215,
    `topLevelListItems` 221, `tablesOf` 296, `LEADING_BOLD`/`LEADING_CODE`/
    `LINK`/`DASH_AFTER_LABEL` 322-325, `oneHeading` 347,
    `extractProjectAccountSections` 359, `extractPrinciples` 405,
    `extractSuccessCriteria` 423, `extractCatalogEntries` 438, `headedTable`
    462, `ORDINAL_H2` 500, `extractTopologyComponents` 502,
    `extractCraftPolicies` 526, `TOML_TABLE`/`TOML_NAME` 545-546,
    `extractRosterIdentity` 548, `extractSource` 628 [Observed].
11. Decisions read at source:
    `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md` table header (the
    "Ruled" and "What it means" columns), line 64 (P-74) and line 70 (P-82);
    `POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §6 and "What this does not
    do"; `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md` §6
    [Observed].
12. Doctrine quotes: `.syzygy/governance/doctrine/vision.md:96-98` (VIS-2) and
    `:184-185` (VIS-7) match `SEMANTIC-DELTA.md:162-169` [Observed].
13. N4 citer re-derivation at `08d4d02`, denominator
    `git ls-tree -r -z --name-only 08d4d02` = 1,545 paths, 4 undecodable:
    - literal `PWB-REQ-002`: `git grep -l -F` → 49; Python substring → 49
      [Observed].
    - run/range only (not literal), method A, Python `re`, case-sensitive:
      `PWB-REQ-(\d{3})((?:\s*(?:/|,|,?\s*and|,?\s*or|\.\.|…|–|—|-|to|through)\s*(?:PWB-REQ-)?\d{3})+)`,
      counted when 002 is a member or lies strictly inside a range pair →
      **14** [Observed].
    - method B, `git grep -l -P`
      `PWB-REQ-00[01]\s*(\.\.|…|–|—|-|to|through)\s*(PWB-REQ-)?0(0[2-9]|[1-9]\d)|PWB-REQ-\d{3}(/\d{3})*/002`
      minus the literal set → **14**, the same files [Observed].
    - The fourteenth is `packages/three-surface-poc-core/src/project-shape-model.ts:2`
      ("PWB-REQ-001…007", U+2026). Total 63, not 62. See N-5.
14. Reviewer rule-6 mutations of the proposed `spec.md`, run through
    `requirement_findings` (in memory; no file edited):
    - KILLED: "Until Butlers' profile" → "Until a project's profile";
      "Except for Butlers," prefixed to the no-substitute sentence; "nine
      shapes" → "ten shapes"; `<key>` "a single directory name" → "one or more
      directory names"; the `pathPattern` sentence deleted; duplicate-key rule
      → "is dropped" [Observed].
    - SURVIVED: scenario 1 WHEN "Butlers is observed" → "any project is
      observed"; scenario 2 WHEN negated with the checked phrase kept;
      scenario 3 THEN given "except that the source leaves the source-path
      population"; "**Falsifier**" → "**Non-falsifier**"; "Each admitted item
      SHALL" → "MAY"; the unchanged source-path bullet's "is Unknown" → "is 0";
      the declared-item bullet's "one extraction rule" → "any extraction rule"
      [Observed]. See N-7.
    - One fixture (the oracle's first "identities and D") matched nothing
      because of a line break; not scored [Observed].
15. Reviewer rule-6 mutations of the CG registration (reverted with
    `git checkout` each time): packet phrase copy at `:166` edited → CG-7d
    FAIL, "32 OK, 19 WARN, 1 FAIL"; manifest byte appended → "31 OK, 19 WARN,
    2 FAIL" and builder `--check` "manifest differs from exact regeneration"
    [Observed].
16. `bd show syzygy-dov.15.1` → OPEN, not drafted; no M15 package under
    `contracts/candidates/` [Observed].

## Round-1 resolution

| Finding | Status | Basis |
|---|---|---|
| R1 profile slot cannot express Butlers | **Resolved** [Inferred] | Patched `spec.md:98-107`: "Each class above has one or more rows", each with source, "the heading or headings, each with its level when it has one", every parameter "such as a table column, a TOML table and field or a key prefix", one shape, one key form. Worked through all nine: project-account-section 6 rows (3 × vision.md `heading-section`/`fixed`; architecture.md `every-level-2-section`/`fixed`; v1.md two-heading `heading-section` for v1-scope, one-heading for v1-success); success-criterion 2 rows `top-level-list`/`prefixed-ordinal` (`vision`, `v1`); principle `top-level-decimal-list`/`leading-bold`; catalog nine rows `top-level-bulleted-list`/`leading-bold-or-code` (duplicate across headings fails, as `items()` does); design `first-table-rows`/`first-cell-link-text`; baseline `tree-path`/`tree-key`; topology `ordinal-section-table-rows`/`ordinal-and-label`; craft `first-table-rows`/`link-target-basename` with column File; roster one `toml-table-field` row (table `butler`, field `name`) keyed `tree-key`. Each reproduces the code's identities and D, so scenario 1 is satisfiable. Residuals N-2, N-3. |
| R2 interim default vs P-74 Q2 | **Resolved, with a new defect on the refused-profile path** [Observed] | `spec.md:108-110` "Until Butlers' profile is loaded, the observer reads Butlers by the grammar written below, as a built-in default". P-74's Ruled cell (line 64): "the first four limbs thread a profile parameter with current constants as default" — faithful; "no other project has a built-in default" is the draft's, not attributed to the owner. `SEMANTIC-DELTA.md:155-158` and packet `:77-80` quote the Ruled cell exactly. Q7 now asks only what P-74 Q2 leaves open. See R-A. |
| R3 landing order | **Resolved** [Observed] | Packet `:146-152`, ledger `:137-138` attribute only `.21` → `.30` → `.22` → lane B; `.20` "Not in the ruled order". Matches owner-values §6 option text. But see R-B for a different attribution. |
| R4 VIS-2 on missing rule | **Resolved for loaded profiles; open on two other paths** [Inferred] | `spec.md:111-119`: class with no row or an invalid row → class and category denominators Unknown, every source stays in the population; scenarios "Loaded profile gives one class no row" and "… names a shape outside the vocabulary" added. Not covered: see R-A. |
| R5 shape sentences / exactness Butlers-only | **Resolved** [Observed] with residual N-3 | Sentences equal dov.24's (command 9); each code failure I traced is stated (empty decimal/top-level list; no table; zero ordinal H2; `ORDINAL_H2` lookahead as "a character that is not an ASCII letter, digit or underscore"; architecture joined in file order with one blank line). Exactness hoisted to "For every grammar, loaded or built-in" (command 8). |
| N1 oracle omits D | Resolved [Observed] | `spec.md` oracle: "must produce the same identities and D" on both legs. |
| N2 builder guards phrases | Partly, as dispositioned [Observed] | Exactness and Butlers bullets now compared to base bytes; survivors in command 14. N-7. |
| N3 bare digest | Not changed; checker-wide, tracked as `syzygy-eau` | — |
| N4 run/range citers | **Not fully resolved** [Observed] | Regex published, 13 listed; re-derivation gives 14. N-5. |
| N5 M15 sibling | Resolved in form; see R-B, N-4 | Ledger `:142`, packet Q8. |
| N6 doctrine quotes | Resolved [Observed] | Command 12. |
| N7 key-form wording | Resolved [Observed] | Full sentences carried. |
| N8 "whole subject" | Resolved [Observed] | `SEMANTIC-DELTA.md:21-23`, packet `:17-21`. |
| N9 recording | Resolved [Observed] | Raw retained, partition row present (command 6). |

## New findings

### R-A — revise [Observed text; Inferred consequence]: "until … loaded" lets a refused Butlers profile fall back to the built-in grammar

Patched `spec.md:108-110`: "Until Butlers' profile is loaded, the observer
reads Butlers by the grammar written below, as a built-in default". Same
bullet, `:117-119`: "A loader that instead refuses the whole profile meets
this rule only if every source stays in the source-path population with an
Unknown item denominator." A Butlers profile that is declared but refused is,
literally, not loaded, so the first sentence sends the observer back to the
built-in grammar while the second requires everything Unknown. The falsifier
(`:239-240`, "a loaded profile's missing or invalid rule is replaced by a
built-in one") and PWB-REQ-002's body ("or, before Butlers' profile is
loaded, the Butlers grammar written there") are both keyed to "loaded", so
neither catches the fallback. The path is likely, not hypothetical: see N-1
(key-form names differ from dov.24's). The trigger "loaded" is right for the
interval P-74 Q2 ruled (registry act done, limb 5 not built), so the repair
is not to rekey on the registry but to close the refusal path, e.g. "A
Butlers profile the loader refuses never returns Butlers to the built-in
default", with a scenario.

Second uncovered path [Inferred, note weight within this finding]: a project
other than Butlers with no loaded profile. "No other project has a built-in
default" (`:110`) and every Unknown rule speaks of "the loaded profile";
nothing says such a project's classes are Unknown rather than empty. The
ledger itself names the case (`IMPACT-LEDGER.md:141`, dov.25's second
registry entry "would need a profile under this text"). One sentence closes
it.

### R-B — revise [Observed]: recorder readings presented as the owner's rulings

- P-82: `SEMANTIC-DELTA.md:236-237` "P-82 ruled 'One CC-REV-2 semantic delta
  to PWB-REQ-002', behind lane B"; `OWNER-DECISION-PACKET.md:126-127` "P-82
  ruled 'One CC-REV-2 semantic delta to PWB-REQ-002', sequenced behind lane
  B"; `IMPACT-LEDGER.md:142` "P-82 rules one CC-REV-2 delta to
  `PWB-REQ-002`, behind lane B". The quoted phrase and the sequencing are
  from line 70's "What it means" column ("One CC-REV-2 semantic delta to
  PWB-REQ-002 under `NORMATIVE-CHANGE-WORKFLOW.md`, sequenced behind lane B's
  open manifest"), not its "Ruled" cell, which reads: "**A** — Q1 arm (b),
  draft the delta only; Q2 design `partially-extracted` inside it, build only
  after sign-off and a fresh authorization; Q3 design the
  `unenumerated-heading` reason as surface-flag (a counted, routed Unknown);
  Q4 design the root-independence flags in the same delta." The ordering
  "behind lane B" is the same class of error as round-1 R3.
- §6: `OWNER-DECISION-PACKET.md:92` "Your §6 reading speaks of 'container
  shapes'". The sitting's owner answer cell is only "Draft it now
  (Recommended)"; "Reading:" is the recorder's. `SEMANTIC-DELTA.md:151`
  correctly says "Its reading"; the packet does not.

Repair: quote the Ruled cell, and label the effect column as the record's
reading.

### N-1 — note [Observed]: six of eight key-form names differ from dov.24's, undisclosed

N8's closed set names `leading-bold`, `leading-bold-or-code`,
`first-cell-link-text`, `tree-key`, `ordinal-and-label`,
`link-target-basename`; dov.24's `ITEM_KEY_SENTENCES` keys are `principle`,
`catalog`, `design`, `tree`, `topology`, `craft` (builder `KEY_FORMS` maps
them). Round-1 R1 asked to "align names with dov.24"; the disposition says
"This matches syzygy-dov.24's rows". Under `spec.md:111-113` a row "naming a
… key form outside these closed sets" is unreadable, so a registry that
names forms by dov.24's labels would make every such Butlers class Unknown
(and, with R-A, might instead fall back). Whether dov.24's registry names
the form or carries the sentence is [Unknown] to this reviewer (that patch is
withheld). Align, or state that a key form is identified by its sentence.

### N-2 — note [Observed]: multiple headings are defined only for `heading-section`

`spec.md:101` lets any row declare "the heading or headings"; only the
`heading-section` sentence says what two headings mean. The list and table
shapes read "the section" (singular). dov.24's `--check` reports "15
class-grammar rows"; with six project-account and two success rows that
leaves one catalog row, so dov.24 appears to give catalog one row with nine
headings [Inferred], a form N8's text gives no meaning. Nine one-heading rows
work under N8, so scenario 1 stays satisfiable; the two drafts do not yet
say the same thing.

### N-3 — note [Observed]: "every way it fails" is overstated for heading-located shapes

`spec.md:32`: "Each shape's sentence says what is read and every way it
fails". Not in any shape sentence: a declared heading occurring twice fails
as `duplicate-key` (`oneHeading` 347-351, `headedTable` 462-466); the table
shapes' heading is matched at any level (`headedTable` filters by text only).
The missing heading is covered by the exactness bullet (`:123`); the
repeated heading only loosely, as "unexpected duplicate key". Also left to
code: the list markers (`-`, `*`, `+`), ATX-only headings, fenced lines
skipped, whitespace allowed around `=` and a trailing `#` comment in TOML.
Since the sentences are shared verbatim, fix both or narrow the claim.

### N-4 — note [Inferred]: the M15 (P-82) disclosure is partly inaccurate

Packet Q8 (`:129-132`) and `SEMANTIC-DELTA.md:238-240` say this delta "defers
to the exactness sentence … without saying how much of the file fails". But
the package also makes that sentence govern every grammar ("For every
grammar, loaded or built-in", `spec.md:120`), so "it never produces a
partial item set" now binds every loaded profile; and it adds a new
propagation, the class's **category** denominator Unknown (`:113-114`),
which the base text does not state. M15 is ruled to design
`partially-extracted` and root-independence flags; both sentences are in
its path. The "regenerated and re-reviewed" consequence is disclosed; the
claim that nothing here decides how much fails is not accurate. Whether
root-independence flags touch category propagation is [Unknown] (M15 not
drafted, command 16).

### N-5 — note [Observed]: citer count is 63, not 62; a code citer is missing from Table 2

Command 13: the ledger's SEP (`IMPACT-LEDGER.md:47`) has no U+2026 ellipsis,
so `packages/three-surface-poc-core/src/project-shape-model.ts:2`
("PWB-REQ-001…007") is missed by both published methods. It is code and is
absent from Table 2 (`:110-118`). Literal 49 confirmed by two methods.

### N-6 — note [Observed]: stale sentence in the packet

`OWNER-DECISION-PACKET.md:169`: "it is **not offered**: no independent review
has run." Round 1 ran (`:210-231`). The head banner (`:7-8`, "not offered
until the exact bytes pass a fresh independent review") is correct.

### N-7 — note [Observed]: claims no mutant covers

Command 14 survivors: scenario WHEN clauses (scenario 1's restriction to
Butlers is unguarded), requirement-body SHALL, the "Falsifier" label, the
unchanged source-path and declared-item bullets. Disclosed as "Partly" in the
review record; listed so the claim set is explicit.

### N-8 — note [Observed]: the declared-item bullet still says "one extraction rule"

`spec.md:15` (unchanged): "A **declared item** has one class from this
closed set and one extraction rule". The new text gives a class "one or more
rows". Readable as "the class's rule, made of rows", but the two sentences
now pull against each other; "category" (`:113-114`) also has no class →
category mapping in the reader definitions. Packet Q9 leaves that bullet
alone deliberately.

## Confirmations (not findings)

- Nothing is labelled accepted, adopted or in force; the phrase is marked not
  offered (`:162-172`); VIS-4 respected [Observed].
- Ruled landing order attributed only as `.21` → `.30` → `.22` → lane B
  [Observed].
- Open questions 4, 6, 7 are genuine and not ruled in the records read; 8 is
  genuine but its premise needs N-4 [Observed/Inferred].
- Question 1 (widening beyond "container shapes") is honestly put; the
  answer cell ("Draft it now (Recommended)") does not settle it [Observed].
- The oracle's second leg is falsifiable: a profile row differing from the
  written grammar changes identities or D and fails it [Inferred].
- `git status --short` in the worktree clean after every mutation [Observed].
