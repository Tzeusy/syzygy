# R-GP-IMPL-POC-CORE-HYGIENE-1 — CC-REV-1 implementation review of syzygy-bpyt.7.6, round 1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: e81883f3
Subject: r1-review.diff sha256 1f3fd9bb472af2a3b62fbf3e2899b3e7c902f2db9ce99ddc1f8bb919efffba86

Reviewer: fresh-context subagent (rev-503), default model, no part in authoring
PR #503 (branch `agent/syzygy-bpyt.7.6`). Date: 2026-10-22. No target repository
content was fetched or read. Route probes used the app's own fixture models only.

CC-REV-1 classes, as decided by this reviewer: **none**. Adjacent classes 1, 3,
4 and 6 were checked and are not touched (section 2, "Classification").

Every finding below is a note (N1 to N7). None needs the reviewed bytes changed
before merge, and none needs to go to the owner first. N1 matters for the merge
itself: the PR head has moved past the reviewed commit.

---

## 1. Subject identity checks

- [Observed] `sha256sum r1-review.diff` gives
  `1f3fd9bb472af2a3b62fbf3e2899b3e7c902f2db9ce99ddc1f8bb919efffba86`. That equals
  the brief's digest.
- [Observed] In my own clone I wrote
  `git diff b7697f6ac82c7fdb47c6858f70b23febdd3f505c e81883f3d44d033425280e8b57f338b6acf29bc2`
  to a file and hashed it. The hash is the same: `1f3fd9bb…ba86`. The diff has 31
  files: "31 files changed, 4917 insertions(+), 12 deletions(-)".
- [Observed] `git fetch https://github.com/Tzeusy/syzygy.git agent/syzygy-bpyt.7.6`
  followed by `git rev-parse FETCH_HEAD` returned
  `e81883f3d44d033425280e8b57f338b6acf29bc2` at the start of this review.
- [Observed] `git merge-base e81883f3 <GitHub main>` returned
  `b7697f6ac82c7fdb47c6858f70b23febdd3f505c`, which matches the brief.
  e81883f3 is a merge commit with parents `9314fe45` and `b7697f6a`. The local
  checkout's `main` (`32c16625`) is stale and was not used as the base.
- [Observed] **The PR head has moved.** Later in this review, `gh pr view 503`
  reported `headRefOid` `7bee932e9988d5be1c0f48acd865e296647b545e` and 35 files.
  `git log e81883f3..7bee932e` lists three more commits:
  - `ebdbbbe4` "refactor: cite each kept module's consumer by path:line"
  - `95193747`
  - `7bee932e`

  `git diff --stat e81883f3 7bee932e` shows source edits to
  `packages/three-surface-poc-core/src/evidence-population.ts` and
  `packages/three-surface-poc-core/src/index.ts`, plus four new evidence files.
  **This review covers e81883f3 only** (AGENTS.md rule 10). See N1.
- [Observed] The PR's evidence records were not taken at the reviewed pair.
  They name base `26ff52ce` and code commit `01b0fb79`. Between 01b0fb79 and
  e81883f3, `git diff --stat 01b0fb79 e81883f3 -- packages apps scripts` shows
  only main's merged `packages/polaris-dossier` changes (4 files). So the source
  delta under review is the same in both pairs. I re-ran the behaviour checks at
  the exact reviewed pair (b7697f6a, e81883f3); see section 3.

## 2. Clauses relied on (quoted)

- **CC-REV-1** (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md:18-19`):
  "Changes touching any of seven classes require review by an independent,
  fresh-context reviewer, and the agent performing the change never finally
  decides which classes it touches."
  - Class 1 (:31): "**authority boundaries** — write-universe, typed-authority
    table, adapter authorization (VIS-5, VIS-6)".
  - Class 3 (:35): "**deterministic observation** — snapshot composition,
    evaluation identity, the deterministic/inferred seam (VIS-7)".
  - Class 4 (:37): "**security** — anything under SEC-1…SEC-5, auth surfaces,
    egress paths".
  - Class 6 (:40): "**public interface** — machine-queryable endpoints, adapter
    contracts, anything an external consumer can depend on".
  - Reclassification (:51): "**A reviewer or the owner** may reclassify at any
    time."
- **GP-Q0 part 1** (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`):
  - :51: "Behavior-preserving refactors may proceed under the acts already in
    force. They may touch `apps/**`, `packages/**`, `scripts/**`, tests, CI and
    root manifests."
  - :52-55: "'Behavior-preserving' means none of the following changes: a
    rendered byte, a wire format, a refusal string or an exit code; a signed or
    digest-bound artifact; a consent, security or retention decision."
  - Review rule, :60: "Each pull request states which CC-REV-1 classes it
    touches. Any pull request whose classes are not "none" gets the CC-REV-1
    independent review, from a fresh-context reviewer on the default model."
  - Review rule, :62: "**Which ones:** pull requests touching class 1 (authority
    boundaries), class 3 (deterministic observation) or class 4 (security), and
    class-6 pull requests that remove an endpoint."
  - Review rule, :64-66: "an old-versus-new differential over a mutated-record
    corpus that includes records with altered prose; a rule-6 mutant for each
    predicate; a non-blocking owner notice in the cycle report."
- **Owner ruling P-71**
  (`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:58`):
  "Q3 arm (b), a pure drafter that writes no file". The same row's "What it
  means" column also says "slice 7's drafter writes no file".
- **Arm (b)'s own text** (`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:115`;
  candidate design material, quoted for N2 only): "Arm (b): the drafter is pure
  and emits packet *data* on request, writing no file at all; an operator
  command renders it."
- **AGENTS.md at e81883f3:**
  - :149: "POC shared-model changes have WIP one."
  - :237-238: "Fresh `git worktree`: run `npm ci` inside it first, or `NodeNext`
    silently resolves `@syzygy/*` to the main checkout's `node_modules`."
  - Rule 6 (:126-127): "Mutate the input and confirm the check fails, per
    predicate, before trusting it".
  - Rule 10 (:133): "Freeze the bytes a review is bound to; any later edit
    retires the review."
  - Rule 11 (:134-135): "An evidence record names its subject and the subject's
    digest; a record that names neither cannot be re-checked against the bytes
    it describes."
  - :95: "Never edit an artifact after an act has bound its digest."
- **The bead** (`bd show syzygy-bpyt.7.6 --json`, read-only):
  - Design: "Delete orphans with their tests, or move them to a test-support
    entry; un-export test-only exports or mark each deliberate seam with a
    comment. Rendered bytes, wire output and model outputs unchanged. CC-REV-1
    class: none expected (dead code); state it."
  - Acceptance criteria: "1. Each orphan's consumer sweep recorded (method,
    denominator) and each removed or relocated. 2. The six test-only exports
    enumerated and resolved. 3. Suite green; Tests: +a ~b -c; rendered bytes
    unchanged on the POC fixtures."
- **The source of "six"** (`bd show syzygy-bpyt.7.2`, description): "28
  test-only exports (cap1-core 18, daemon 4, poc-core 6)". The audit plan
  (`docs/plans/2026-10-21-greenfield-parity-audit.md`) does not list the six.
  A `git grep` for "test-only export", "poc-core 6" and "appendEvaluation" in it
  returned no lines.

### Classification

I classify this change as **none**. The adjacent classes were checked one at a
time:

- **Class 1 / class 4.** `body-read-authority.ts` is the P1 body-read gate.
  - [Observed] It changed by comments only. TypeScript's parser printed both
    versions with `removeComments: true`, and the two prints are identical.
    The emitted `dist/body-read-authority.js` differs only by three added `//`
    lines (raw byte diff, section 3).
  - [Observed] Its predicate population is unchanged: 85 `// mutation-point:`
    markers, 85 of them followed by `if (`, with the same ordered names (sha256
    prefix `d303898075b4744a`) at base and head.

  `walkthrough-judgment.ts` is the PWB-REQ-022 evaluator.
  - [Observed] It lost one exported constant that nothing reads, plus that
    constant's value import of `COMMON_INVALID_CASES`. Its predicates are
    unchanged: 88 markers, 85 predicate markers, same ordered names (sha256
    prefix `ee9bf50722164f55`).
  - [Observed] Because only type imports from `./body-read-authority.js`
    remain, TypeScript now drops that import from the emitted
    `walkthrough-judgment.js`. So the compiled evaluator no longer loads the
    gate module.
  - [Observed] There is no import cycle: `body-read-authority.js` imports only
    `act-fields.js`, `authority-artifact-fields.js` and `owner-act-record.js`.
    It has no top-level call statements (`grep -E '^[A-Za-z_$][A-Za-z0-9_$.]*\('`
    on the compiled file: 0 lines).
  - [Inferred] Dropping the edge has no behavioural effect.

  No write-universe, typed-authority table, adapter authorization,
  SEC-1…SEC-5 surface or egress path is touched.
- **Class 3.** `ClassificationOutcome` (content classification) and
  `FactFamilyKind` (coverage) were type aliases. [Observed] Their deletion
  changes no emitted `.js` file: only the two `.d.ts` lines that declared them
  are gone. No snapshot composition or evaluation identity changes.
- **Class 6.**
  - [Observed] The package barrel loses three names. But
    `packages/three-surface-poc-core/package.json` is `"private": true` and
    exports only `"."`.
  - [Observed] No tracked file at base names any of the three outside its own
    declaration (section 3). No `.d.ts` in any of the ten built projects
    references them.
  - [Observed] No endpoint is removed. All 19 routes per fixture answer
    byte-identically (section 5).
  - [Observed] The one consumer found outside the source tree is the
    measurement script embedded in a retained evidence record. It requires
    `dist/evidence-population.js`, and that file's exports and path are
    unchanged.

[Inferred] If the owner or a later reviewer reclassified this PR as class 1,
the GP-Q0 extra checks would not yet be met:
- No old-versus-new differential over a mutated-record corpus with
  altered-prose records was run for the gate or the evaluator. The route
  capture uses five well-formed fixtures.
- No new per-predicate mutants were run. They would mostly re-check the
  unchanged predicates, which the existing `pwb-mutation*.test.ts` and
  `pwb-mutation-sweep.test.ts` fragment checks cover statically.
- There is no owner notice in the cycle report.

**WIP one.** [Observed] `gh pr list --state open` lists PRs 503, 502, 501, 500
and 487. For each of 502, 501, 500 and 487, `gh pr view <n> --json files`
filtered to `packages/three-surface-poc-core/` returned `[]`. No other open PR
touches the shared-model package.

## 3. What I ran, and the results

Setup:
- Two scratch clones of `/home/tze/GitHub/syzygy`, each with its own `npm ci`:
  `base` at b7697f6a and `head` at e81883f3.
- [Observed] The workspace links resolve inside their own clone:
  `readlink -f base/node_modules/@syzygy/three-surface-poc-core` resolves to
  `…/rev-503/base/packages/three-surface-poc-core`, and the same holds for head.
- In each clone I ran `npm run build:poc` and then `npm run build` (all ten
  projects). Both exited 0.

| Check | Result (verbatim where quoted) |
|---|---|
| poc-core vitest project (head) | [Observed] "Test Files  33 passed \| 2 skipped (35)" / "Tests  1041 passed \| 2 skipped (1043)", exit 0 |
| poc app vitest project (head) | [Observed] "Test Files  88 passed \| 1 skipped (89)" / "Tests  1077 passed \| 2 skipped (1079)", exit 0. Includes `polaris-authority-sweep.test.ts (5 tests)`, `pwb-mutation-sweep.test.ts (4 tests)` and `pwb-mutation.test.ts (5 tests)`, all passing |
| Full suite `npx vitest run` (head) | [Observed] "Test Files  229 passed \| 3 skipped (232)" / "Tests  4912 passed \| 5 skipped (4917)", exit 0. This is 8 more tests than the PR body's 4,904, which was counted at 01b0fb79, before main's credential-probe tests were merged |
| `npm run typecheck` (head) | [Observed] exit 0 |
| `python3 scripts/check_governance.py` | [Observed] head: "32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted". The base output differs only in file counts: scope 3029 vs 3050 tracked; CG-2a 1926 vs 1936 files; CG-3 1808 vs 1809 files |
| `python3 scripts/check_quotations.py` | [Observed] base and head outputs are byte-identical (`diff` printed nothing) |
| PWB-REQ-014 authority sweep | [Observed] `polaris-authority-sweep.test.ts (5 tests)` passed in the app run above |
| Census selftest | [Observed] "selftest: 23 of 23 cases hold". My output is byte-identical to the stored `selftest-export-census-2026-10-22.txt` |
| Census mutants (the PR's runner, re-run) | [Observed] "mutants=20 killed=20 (failed case 20, crash only 0) survivors=[]". The tool's sha256 at e81883f3 is `992d1902…e5b9`, the same as the record's `subjectSha256`, and `git diff 19eed39b e81883f3` over the tool and its runner is empty |
| Census at base / head (lexer mode) | [Observed] base: "exports scanned: 589; dead=3; internal=134; public=131; self-only=233; test-only=88". Head: "exports scanned: 586; dead=1; internal=133; public=131; self-only=233; test-only=88". These equal the stored totals |
| Consumer sweep (the PR's script, re-run at b7697f6a) | [Observed] "tracked=3029 read=3029". Each deleted name: "files=  1 agree=True", in core-src only |

**Deletions: my own consumer sweep.**
- Method: a substring search, case-sensitive and case-insensitive, over every
  tracked blob at b7697f6a, read from git objects (`git ls-tree -r -z` and
  `git cat-file --batch`). Denominator: 3029 blobs; 4 were not UTF-8 and were
  read as latin-1.
- [Observed] Results:
  - `JUDGMENT_INVALID_CASE_IDS`: 1 hit (`walkthrough-judgment.ts:131`); 1 file
    case-insensitive.
  - `ClassificationOutcome`: 1 hit (`content-classification.ts:282`); 1 file.
  - `FactFamilyKind`: 1 hit (`project-shape-coverage.ts:79`); 1 file.
- [Observed] So no docs, candidate packets, evidence records or `scripts/`
  name them. A substring search also catches compounds (`…Outcomes`) and
  identifiers inside prose.
- [Observed] Built outputs: in the base `packages/` and `apps/` trees,
  `grep -r -l -F -w` over `*.d.ts` and `*.js` finds the three names only in
  their own declaring `dist` files.
- [Observed] The PR's count of 3,024 tracked files is the count at 26ff52ce.
  At b7697f6a there are 3029: main added five files in between.

**Keeps.**
- `evidence-population.ts`.
  - [Observed] `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md:380-386` says "any
    new M1 (or related Polaris page-size) evidence record must carry a
    `population` block derived with `derivePopulationBlock` in
    `packages/three-surface-poc-core/src/evidence-population.ts`". The same
    passage ends: "This note is candidate design material like the rest of
    this document and binds nothing by itself."
  - [Observed] `docs/evidence/pwb-m1-polaris-lane-a-population-2026-09-23.json`
    embeds
    `require('$WT/packages/three-surface-poc-core/dist/evidence-population.js')`
    and calls `derivePopulationBlock`.
  - [Observed] The base-to-head byte diff of `dist/evidence-population.js` adds
    six comment lines and nothing else. So the same names are exported at the
    same compiled path, and the retained script's require still resolves. I
    did not run that script: it reads a target repository.
- `owner-act-drafter.ts`.
  - [Observed] The P-71 quote above is correct.
  - [Observed] The file's sha256 at head is `1dfea09c…62e3`, the same as the
    value `docs/evidence/syzygy-dov41-unknown-routes-rule6-2026-10-03.json:31`
    records.
  - [Observed] `draftOwnerAct` is called only from `owner-act-drafter.test.ts`.
- `test-cleanup.ts`.
  - [Observed] It is not in `index.ts` and not in the package's `exports` map.
    Its only importers are `model.test.ts` and `test-cleanup.test.ts`.
  - [Observed] `apps/three-surface-poc/src/temporary-directory.ts:15` exports
    `removeTemporaryDirectory`.

**Path and line locators.**
- [Observed] No tracked file is moved, renamed or deleted.
- [Observed] Manifests: `git grep -l -F` over `*MANIFEST*`, `*manifest*` and
  `*.yaml` at base, for the ten changed source paths, found no file.
- [Observed] Digest citers. A sweep of every tracked blob at base for each
  changed file's base sha256 (full, 12-hex and 8-hex) and its git blob id found
  54 hits.
  - They sit in 15 files: 13 records under `docs/evidence/` and 2 raw
    reviews.
  - They cover 6 of the 10 changed files: body-read-authority,
    walkthrough-judgment, project-shape-model, test-artifact-verification,
    content-classification and project-shape-coverage.
  - None is under `.syzygy/**` or `openspec/**`.
  - No script, app, package, workflow, `package.json` or `PROJECT-STATUS.md`
    names any of the 13 records. `git grep -n -F` for the 13 basenames found
    one line, `apps/three-surface-poc/src/pwb-mutation-sweep.ts:96`
    `'named-absent-file-dropped',`. That line is a mutation id, not a
    reference to the record. CG-7h ("317 predicates examined, 0 findings")
    passes at head. So no act or check binds the current source bytes. See N7
    for the gate files.
- [Observed] Line locators. I matched `<basename>:N`, `:N-M`, `#LN` and
  `line N` forms for the ten changed basenames over all 3029 blobs, and mapped
  each through the diff hunks.
  - 422 locators were found, and the cited line moves for 74 of them.
  - Every one of the 74 sits in a raw review, a dated evidence or pursuit
    record, or a design note anchored to an older commit (for example "At
    `a9f671e`"). None is in `.syzygy/**` or `openspec/**`.
  - A second sweep of `.syzygy` and `openspec` for "`<file>.ts` line(s) N"
    forms found one governed locator that this PR shifts. The signed
    container-shape-profile packet cites
    `packages/three-surface-poc-core/src/project-shape-coverage.ts` "lines
    85-95" for `CLASS_ROWS` (`SEMANTIC-DELTA.md:188`,
    `OWNER-DECISION-PACKET.md:345`). `CLASS_ROWS` was already at 86-96 at base,
    and it is at 87-97 at head.
  - The claim those lines support is unchanged: the mapping is the same. The
    drift predates this PR. The packet cannot be edited (AGENTS.md :95), and
    this is not a finding.
  - [Observed] The raws that cite `project-shape-coverage.ts:78` for
    `FACT_FAMILIES` are bound to their own reviewed commits. The new comment's
    claim that the registry-currency packet "cites it by name" is accurate: the
    packet's `REVIEW-BRIEF.md:99` and `SEMANTIC-DELTA.md:422`, and the builder
    script's comment at line 68, name it without a line number.

**Comment accuracy**, checked against the code at e81883f3:
- [Observed] All six "Test seam" claims hold. Each export's only callers are
  the named tests. The `// mutation-point: history-append-only` marker is at
  `walkthrough-judgment.ts:791`, inside `appendJudgmentEvaluation`.
  `materialization.test.ts:330,365,376` are the three rollback verdicts the
  comment names.
- [Observed] `docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md:230-243`
  discusses reusing the `appendEvaluation` pattern ("there is a proven *shape*
  to copy").
- [Observed] The `FACT_FAMILIES` note holds: no code reads the list after the
  deletion (census lexer class: dead).
- See N2 for the two wording issues.

## 4. Findings

No blocking findings (F) in this round.

### N1 — The PR head moved past the reviewed commit (severity: medium, merge hygiene)
- **Evidence.** [Observed] `gh pr view 503 --json headRefOid` returned
  `7bee932e9988d5be1c0f48acd865e296647b545e`. The reviewed commit is
  `e81883f3`. `git diff --stat e81883f3 7bee932e` shows:
  - `packages/three-surface-poc-core/src/evidence-population.ts`: 14 lines
    changed;
  - `packages/three-surface-poc-core/src/index.ts`: 7 lines changed;
  - four new files under `docs/evidence/poc-core-hygiene-2026-10-22/`
    (`comment_only_check.py`, `mutate_comment_only.py` and two records).
- **Failure scenario.** The PR is merged at its current head on the strength of
  this raw. That lands source edits in the shared-model package that no
  reviewer has read. Rule 10 retires a review when its bytes change.
- **Proposed fix.** Choose one:
  - merge only e81883f3, with `--match-head-commit e81883f3` after resetting
    the branch;
  - or dispatch a round-2 review over `e81883f3..7bee932e` before merging the
    current head.

  In either case, cite this raw only for e81883f3.

### N2 — Two comments overstate their sources (severity: low)
- **Evidence.**
  - [Observed] `packages/three-surface-poc-core/src/index.ts:12` at e81883f3
    reads "Unwired by design: the P-71 Q3 arm (b) drafter …". But arm (b)'s
    design text includes the wiring: "an operator command renders it"
    (`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:115`, also quoted in the D7
    packet, `OWNER-DECISION-PACKET.md:341`). The next sentence, "No command
    renders its output yet", is accurate, so the two sentences disagree.
  - [Observed] The head comment of `evidence-population.ts` states the M1
    design note's "must carry" as a standing rule. It drops the note's own
    qualifier, "candidate design material … binds nothing by itself"
    (`POLARIS-M1-PAGE-SIZE-FUNNEL.md:385-386`).
  - [Observed] Minor: `test-cleanup.ts:1` says "only this package's tests call
    it (model.test.ts)". Its own `test-cleanup.test.ts` also calls it.
- **Failure scenario.** A later hygiene or un-export pass reads "by design" as
  a ruling that the drafter stays unwired. It then never builds arm (b)'s
  operator command, or it deletes the drafter as permanently unused.
- **Proposed fix.**
  - Reword `index.ts` to something like "Unwired: the P-71 Q3 arm (b) drafter,
    pure, writes no file; arm (b) has an operator command render it, and that
    command is not built."
  - Add "(candidate design note, binds nothing)" to the evidence-population
    citation.
  - `ebdbbbe4`, after the reviewed commit, rewrites both comments. Confirm the
    wording in the N1 round-2 review rather than here.

### N3 — The census selftest misses four lexer predicates; two lexer limitations are undisclosed (severity: low)
- **Evidence.** [Observed] On scratch copies of `export_census.py`, these four
  single-fragment mutants each leave `--selftest` at "selftest: 23 of 23 cases
  hold" (exit 0):
  1. `if c == '$' and i + 1 < n and src[i + 1] == '{':` → `if False:`
     (template expressions never entered);
  2. `                        in_class = True` →
     `                        in_class = False` (regex character classes
     ignored);
  3. `        if c == '{' and tpl:\n            tpl[-1] += 1` →
     `        if c == '{' and tpl:\n            pass` (brace depth inside
     `${}` ignored);
  4. `REGEX_PRECEDERS = set('(,=:[!&|?{};+-*%<>~^')` →
     `REGEX_PRECEDERS = set('(,=:[!&|?{};+-*%<>~^)')` (division after `)`
     read as a regex).

  My 25-case probe file kills mutants 1, 2 and 4. Mutant 3 survives the probes
  too and may be equivalent on these inputs. The killing cases are:
  - for mutant 1: ``const s = `${/* X */ 1}`; X`` (expected 1; the mutant gives
    2), and the nested-template case;
  - for mutant 2: `const r = /[/]\/*x/; X /* c */` (expected 1; the mutant
    gives 0);
  - for mutant 4: `const q = (a) / b; // X\nX` (expected 1; the mutant gives
    2).
- **Undisclosed limits.** [Observed] The unmutated lexer reads a regex literal
  after the `)` of a control header, or after `export default`, as division.
  It then drops code up to a later `*/`:
  - `if (a) /\/*/.test(s); X /* c */` → X counted 0, expected 1;
  - `export default /\/*/; X /* */` → X counted 0, expected 1.

  The docstring does not mention either limit.
- **Mitigation.** [Observed] Neither the gaps nor the limits affect any figure
  in this PR. I parsed all 494 tracked code files at base with TypeScript's
  `createSourceFile` and printed them back with
  `createPrinter({ removeComments: true })`. The lexer's identifier multiset
  equals that print's multiset in all 494 files ("files=494 differing=0"),
  after excluding numeric-separator tokens (`1_000` → `_000`), which the
  printer normalises. The deletions also rest on the consumer sweeps, not on
  the census.
- **Failure scenario.** The tool is kept under `docs/evidence/` and is the
  natural tool for the 233-export un-export follow-up. A regression in one of
  these four predicates would pass `--selftest`. A corpus that later contains
  one of the two limit forms would silently under-count uses, and an export
  in use could be classed `dead`.
- **Proposed fix.** In the follow-up bead, or before the tool is reused:
  - add the three killing cases to `selftest()`;
  - add the four mutants to `mutate_census.py`'s `MUTANTS`;
  - state the two limits in the docstring.

  Alternatively, cross-check with the TypeScript printer, as above, whenever
  the census decides a deletion.

### N4 — Evidence records: subject identity and re-runnability (severity: low; rules 6 and 11)
- **Evidence.**
  - (a) [Observed] These records name no commit or tree of their own:
    - `route-capture-2026-10-22.json` (the variants object only);
    - `test-lists-2026-10-22.json`;
    - `selftest-export-census-2026-10-22.txt`;
    - `route-capture-comparison-2026-10-22.json`, which names the two
      captures it compares (`cap-base-2.json`, `cap-head-final.json`) only by
      scratch filename and digest.

    `verification-2026-10-22.json` covers them only by its top-level subject
    block (`baseCommit` 26ff52ce, `codeCommit` 01b0fb79).
  - (b) [Observed] The usage line of `route-capture.mjs` is
    `node route-capture.mjs <tree> <out.json>`, but line 23 reads a required
    third argument. Run as documented, it fails with "TypeError
    [ERR_INVALID_ARG_TYPE]: The "paths[0]" argument must be of type string.
    Received undefined".
  - (c) [Observed] The stored reference capture (sha256 `f2d667c4…68e2`)
    cannot be reproduced from what the records hold. The fixture repository's
    path and revision are not recorded, and they enter the 200-response
    bodies. With a fresh fixture repository I got `bc27ce25…6f8e` for base
    twice and for head. Against the stored file, 150 of 230 responses differ:
    all 150 are the status-200 responses, each the same body length.

    The base-versus-head equality, which is the actual claim, does reproduce
    (section 5).
  - (d) [Observed] The script also leaks a temporary directory.
    `fixtureRepoWithGit([])` creates `/tmp/syzygy-poc-surface-fixture-*`; the
    script copies it to the fixed path and never removes the original. My
    first run left `/tmp/syzygy-poc-surface-fixture-XqvMdz`, timestamped within
    2 ms of my fixed repository's `.json`. I deleted it.
- **Failure scenario.** A later reader cannot tell from
  `route-capture-2026-10-22.json` or `test-lists-2026-10-22.json` which bytes
  they describe. A re-run as documented crashes. A re-run with the argument
  cannot reproduce the stored digest, so the record reads as contradicted when
  it is not. Repeated runs add one `/tmp` directory each (the 2026-10-15 inode
  incident).
- **Proposed fix.**
  - Have each record carry its tree commit (and, for the capture, the fixture
    repository's path and revision).
  - Correct the usage line.
  - `rmSync(made.repoRoot, …)` after the copy.
  - State in the comparison record that only equality between trees is
    claimed.

### N5 — Acceptance criterion 1 is met in substance, not in its words (severity: low; coordinator action, no byte change)
- **Evidence.**
  - [Observed] AC1 says "each removed or relocated". Three of the four
    subjects are kept in place:
    - `evidence-population.ts` and `owner-act-drafter.ts`, because the
      consumers in section 3 falsify the orphan premise;
    - `test-cleanup.ts`, although the bead design and the 7.2 description
      ("fold into the test kit") asked for a move.
  - [Observed] The dispositions record gives a reason for each. The PR body
    says the coordinator was told before any deletion.
  - [Inferred] Keeping is the conservative, behaviour-preserving choice.
- **Failure scenario.** The bead is closed against a literal AC1 that the
  merged bytes do not satisfy, and a later audit flags it as unmet.
- **Proposed fix.** In the bead's notes or close reason, have the coordinator
  record that AC1 is met by disposition: two kept, because they are consumed;
  one kept as test support, with the reason. Alternatively, amend AC1.

### N6 — AC2's selection predicate is not published (severity: low; rule 9)
- **Evidence.**
  - [Observed] The six names are hard-coded: `SUBJECT_NAMES` in
    `assemble_census.py:22-27` and `SUBJECTS` in `consumer_sweep.py:25-41`.
  - [Observed] The census classes 88 poc-core exports `test-only` at base. In
    this tool, "test-only" includes exports that their own file calls
    (`self` > 0), so 88 is not "six".
  - [Observed] The six can be re-derived from `census-base`. Take rows with
    class `test-only` and `self == 0`: there are 9. Remove the three
    orphan-module entry functions (`derivePopulationBlock`, `draftOwnerAct`,
    `removeFixtureDirectory`). That leaves 6, exactly the PR's six. Neither
    the records nor the PR body states this.
- **Failure scenario.** A reader cannot re-derive "the six" from the record,
  and a future census run cannot be compared with it.
- **Proposed fix.** Add the predicate and the 88 → 9 → 6 counts to
  `dispositions-2026-10-22.json` (`notInScope` or a new `selection` field).

### N7 — After merge, no mutation record names the gate's or the evaluator's current bytes (severity: low)
- **Evidence.**
  - [Observed] Base `body-read-authority.ts`
    (`f612651d13421c0ffcba0d8db9f5240dcb521aa2c0315b5316b92c52a7cb7b77`) is
    named by:
    - `docs/evidence/pwb-mutation-run-2026-10-21-bpyt-6-2.json`;
    - `docs/evidence/pwb-mutation-run-2026-10-21-bpyt-6-2-r2.json`;
    - `docs/evidence/owner-act-non-human-rule-mutants-2026-10-21.json`;
    - `docs/evidence/owner-act-live-records-before-after-2026-10-21.json`.
  - [Observed] Base `walkthrough-judgment.ts`
    (`c33d0140539525175a267382d2f61f9ca891abbf4abed91bafa0ad33e1a716e6`) is
    named by
    `docs/evidence/pwb-p4-2-mutation-sweep-2026-10-21-bpyt-6-2-judgment-invalid-cases.json`
    and by the two owner-act records.
  - [Observed] The head digests are `aeca9768…4dcd` and `a64ef4c0…808e`.
  - [Observed] `docs/PWB-IMPLEMENTATION-PLAN.md:1012-1015` records a design
    preference: "The 55 common predicates are deliberately duplicated rather
    than shared with `body-read-authority.ts`, so the body-read risk floor and
    its act-bound mutation evidence stay byte-identical."
  - [Observed] No check reads these records (section 3), and CG-7h passes.
    Equivalence is shown here:
    - identical predicate-marker populations for both files;
    - an identical comment-free TypeScript print of `body-read-authority.ts`;
    - for `walkthrough-judgment.ts`, a print that differs only by the deleted
      constant and its import specifier.
- **Failure scenario.** A later reader, or a recorder that matches mutation
  evidence to the gate's current digest, finds the P1 gate with no mutation
  record for its bytes. The PR's records do not say why the last runs still
  apply.
- **Proposed fix.** Choose one:
  - in the dispositions record, state that the bpyt.6.2 mutation runs remain
    applicable, because the gate's change is comment-only and the evaluator's
    is outside every predicate, and cite this raw's section 2 evidence (or
    the branch's later `comment_only_check.py`, once reviewed);
  - or drop the three-line comment from `body-read-authority.ts`, so that the
    gate's bytes, and its record match, are kept.

## 5. Every changed output

**None changed.** The evidence, all at the reviewed pair b7697f6a → e81883f3:

- **Rendered and wire bytes.**
  - [Observed] I ran the PR's `route-capture.mjs` against my base and head
    builds with one shared fixed fixture repository. Each run reported
    "variants=5 routesPerVariant=19,19,19,19,19 responses=230".
  - [Observed] The base capture, a second base capture and the head capture
    all have sha256 `bc27ce25946d4d985045d80126e5469855ef70ba33ae99663c38457166ba6f8e`.
  - [Observed] `compare_captures.py` printed "responses=230 fixtures=5
    distinct=5 keysVarying=30/46", then "cap-base-2.json: bytes equal True,
    differing responses 0" and "cap-head-1.json: bytes equal True, differing
    responses 0".

  So 230 of 230 responses are identical. **5 of 5 fixtures give distinct
  output**, and 30 of 46 request keys vary across fixtures, so the probe can
  tell the fixtures apart. The status mix covers 200, 401, 403 and 502
  responses. Credentialed requests ran with and without the bearer token.
- **Emitted code.**
  - [Observed] The PR's `dist_code_diff.py` printed "compared=948 differing=4
    inOnlyOneTree=0". The four files are:
    - `content-classification.d.ts` (−`ClassificationOutcome`);
    - `project-shape-coverage.d.ts` (−`FactFamilyKind`);
    - `walkthrough-judgment.d.ts` (−`JUDGMENT_INVALID_CASE_IDS`);
    - `walkthrough-judgment.js` (− the constant and the elided
      `import { COMMON_INVALID_CASES, } from './body-read-authority.js';`).
  - [Observed] Independently, a raw byte comparison of every file under each
    of the ten projects' `dist/` covered 1906 files, 948 of them `.js` or
    `.d.ts`. 36 differ:
    - 3 `.tsbuildinfo` files;
    - 20 source maps;
    - 13 `.js`/`.d.ts` files. Their raw diffs add only comment lines, except
      for the four above.
  - [Observed] No file under `apps/three-surface-poc/dist`, other than
    `.tsbuildinfo`, differs.
- **Source.** [Observed] The TypeScript print of every tracked code file with
  comments removed gives "identical_after_print=491" of 494 common files. The
  3 that differ are exactly the three deletion sites. The one new file is the
  evidence script `route-capture.mjs`.
- **Tests.**
  - [Observed] `npx vitest list` at base listed 4919 lines; at head it listed
    4916. Sorted, the only difference is three `session-view.test.ts` tests
    that are absent from the head list. Those tests are `it.skipIf(!hasBwrap)`,
    where `hasBwrap` comes from running `bwrap` at collection time.
  - [Observed] Re-listed alone at head, the file gives 11 tests, the same as
    the base list.
  - So the name multisets are equal: **`Tests: +0 ~0 -0`**. The PR's 4,911 was
    counted at 26ff52ce.
- **Governance outputs.** [Observed] `check_quotations.py` output is
  byte-identical between base and head. `check_governance.py` differs only in
  file counts (section 3).
- **Not re-run.** [Unknown] I did not re-run the canonical PROJECT-STATUS
  battery. The PR body reports "commands=110 nonzero=0" at e81883f3.

## 6. Verdict per acceptance criterion

| AC | Verdict | Basis |
|---|---|---|
| 1. Each orphan's consumer sweep recorded (method, denominator) and each removed or relocated | **Met in substance; literal wording not met** (N5) | [Observed] Each sweep is recorded, with method and denominator (`consumer-sweep-base/code`: two methods, "agree=True", tracked 3024 at 26ff52ce; re-run at b7697f6a over 3029). Each subject has a disposition: one deleted, two kept as consumed, one kept as test support |
| 2. The six test-only exports enumerated and resolved | **Met**, with N6 | [Observed] Six are enumerated by name. Each is resolved by a "Test seam" comment, which the bead design allows ("mark each deliberate seam with a comment"), and each comment is accurate. The selection predicate is unpublished |
| 3. Suite green; Tests: +a ~b -c; rendered bytes unchanged on the POC fixtures | **Met** | [Observed] Full suite: 4912 passed, 5 skipped, exit 0. `Tests: +0 ~0 -0`. 230 of 230 fixture responses are identical base vs head, and 5 of 5 fixtures are distinct |

## 7. Test quality

- [Observed] The PR adds no product tests and changes none, which fits a
  dead-code change. The existing tests carry the safety:
  - `pwb-mutation.test.ts` and `pwb-mutation-sweep.test.ts` assert that every
    literal mutation fragment "occurs exactly once in its current source".
    Both pass at head, so no sweep site was orphaned by the deletion or by the
    new comments.
  - The predicate-marker populations are unchanged (section 2).
- [Observed] The census selftest is meaningful for what it covers:
  - the glob-in-string case that broke the regex version ("glob then block
    comment later");
  - strings, template text and expressions, quotes inside regex classes,
    `return`-led regexes and escaped quotes;
  - an 11-row classification fixture whose expected classes are hand-written
    literals, not read from the tool;
  - a raw-mode case.

  Its mutation record stores each mutant's `old` and `new` fragment, the
  commit and the tool digest, and it re-runs to the same result (rule 6
  satisfied for the twenty listed). The gaps are in N3.
- [Observed] The route probe's distinctness figure ("distinct=5",
  "keysVarying=30/46") shows the comparison can see a difference. The status
  spread shows that refusal paths are covered as well as successes. It does
  not include malformed or altered-prose records, which only matters under a
  class-1 reclassification (section 2).
- [Observed] A comparison by `vitest list` is sensitive to the environment.
  `it.skipIf` tests whose condition is probed at collection time (here,
  `bwrap`) drop out of the list on a loaded host. That produced a false
  three-test difference in my run, so list comparisons should re-list
  conditional files on their own before reporting `-c`.

## 8. Cleanup

- Removed: the two scratch clones (`rev-503/base` and `rev-503/head`), my
  copied fixture repository and the mutant copies under `rev-503/`, and the
  leaked `/tmp/syzygy-poc-surface-fixture-XqvMdz` from my first capture run
  (N4).
- Kept: this raw, small tool scripts under `rev-503/tools/`, and my capture and
  comparison JSON under `rev-503/` (no repository content).
- Not done, as instructed: no `bd` mutation, no push, no PR comment, no merge.
  No worktree under `/home/tze/GitHub/syzygy/.worktrees/` was touched.
