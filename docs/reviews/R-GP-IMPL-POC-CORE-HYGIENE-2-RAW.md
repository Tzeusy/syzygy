# R-GP-IMPL-POC-CORE-HYGIENE-2 — CC-REV-1 implementation review of syzygy-bpyt.7.6, round 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: edca4490
Subject: r2-review.diff sha256 be299245e2fcaeb6b1858f75702a462b6a8983c7a36a3abdbaddfa0d29108c10

Reviewer: fresh-context subagent (rev-503b), default model. I took no part in
authoring PR #503 (branch `agent/syzygy-bpyt.7.6`) or its round-1 review.
Date: 2026-10-22. I fetched and read no target repository content. Route probes
used the app's own fixture models, over a fixture repository I created in my
scratch directory and have since deleted.

Scope: this round covers what changed after `e81883f3`. I re-opened round-1
ground only where a repair touched it. Round 1's raw
(`R-GP-IMPL-POC-CORE-HYGIENE-1-RAW.md`, sha256
`6ab42458c789b9a1d01d95e29734365cac7742de70c9e89296b4cc3bb886d196` as read) was
used for its findings only.

**Answers to the brief's two questions:**
1. The repair introduces no error in any byte under `packages/` or `apps/`.
   It introduces four small evidence and documentation imprecisions. All four
   are notes (N8–N11) and none needs a byte change before merge.
2. The change as it stands is mergeable. CC-REV-1 class: **none**. I re-ruled
   it, and it is unchanged from round 1.

---

## 1. Subject identity checks

- [Observed] `sha256sum` over the brief's files:
  - `r2-review.diff` = `be299245e2fcaeb6b1858f75702a462b6a8983c7a36a3abdbaddfa0d29108c10`;
  - `r2-delta-pre-merge.diff` = `4da33252b4af3541aa6222c7ae3231763923cb3da5dfe4d8391097d5aaf262d9`;
  - `r2-delta-repair.diff` = `abd818407d91c446cb020c59c895728474c118f5bd5ef8bea8fb943404f5a96f`.

  All three equal the brief's digests.
- [Observed] In my own clone I regenerated `git diff 1d6731bb edca4490`,
  `git diff e81883f3 7bee932e` and `git diff 36a45cd2 edca4490` and hashed each
  one. The three hashes are byte-for-byte the same as above. Shortstats:
  - "42 files changed, 10308 insertions(+), 12 deletions(-)";
  - "6 files changed, 206 insertions(+), 7 deletions(-)";
  - "37 files changed, 6747 insertions(+), 1555 deletions(-)".
- [Observed] `git fetch https://github.com/Tzeusy/syzygy.git main agent/syzygy-bpyt.7.6`
  gave the branch at `edca4490f5dc6d1d98be14cc5afd0f0840981940` and main at
  `3000698f3706a7e583a21be37dfdc30e3ffef551`. `gh pr view 503` reports
  `headRefOid` `edca4490…` and 42 files.
- [Observed] `git merge-base edca4490 3000698f` = `1d6731bb073cb235aa47fa9043c3ce956b9b7ea6`.
- [Observed] **`36a45cd2` brought only main's bytes.**
  - Its parents are `7bee932e` and `1d6731bb`.
  - `git merge-tree --write-tree 7bee932e 1d6731bb` gives
    `70650d702b92619feac4d5385fb051fe837bf03b`. That equals
    `git rev-parse 36a45cd2^{tree}`, so the merge commit is the clean
    automatic merge, with no hand resolution.
  - The file sets changed since the common ancestor `b7697f6a` do not
    overlap: main changed 13 files, the branch 35, and `comm -12` printed
    nothing.
- [Observed] The two test files that reached the branch through the merge are
  byte-identical to main:
  - `body-read-authority.test.ts`: blob `24f5c3a7…` at both `1d6731bb` and
    `edca4490`;
  - `walkthrough-judgment.test.ts`: blob `49a63459…` at both.
- [Observed] Main's newest commit, `3000698f` (PR #500), does not touch the
  PR. Its 23 changed files share none with the PR's 42, and none is under
  `packages/three-surface-poc-core`. `git merge-tree --write-tree edca4490 3000698f`
  printed a single tree (`3b96ce19…`) and no conflict. So the coordinator's
  landing merge should be clean. [Inferred] I did not run checks on that
  merged tree.
- [Observed] The records' code commit is `47935fec`. `git diff --stat 47935fec edca4490 -- packages apps scripts .github`
  is empty. The 20 files changed after it all sit in
  `docs/evidence/poc-core-hygiene-2026-10-22/`.

## 2. Clauses relied on (quoted)

- **CC-REV-1** (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md`, at edca4490):
  - :18-20: "Changes touching any of seven classes require review by an
    independent, fresh-context reviewer, and the agent performing the change
    never finally decides which classes it touches."
  - Class 1, :31-32: "**authority boundaries** — write-universe,
    typed-authority table, adapter authorization (VIS-5, VIS-6);"
  - Class 3, :35-36: "**deterministic observation** — snapshot composition,
    evaluation identity, the deterministic/inferred seam (VIS-7);"
  - Class 4, :37: "**security** — anything under SEC-1…SEC-5, auth surfaces,
    egress paths;"
  - Class 6, :40-41: "**public interface** — machine-queryable endpoints,
    adapter contracts, anything an external consumer can depend on;"
  - :51: "**A reviewer or the owner** may reclassify at any time."
- **GP-Q0 part 1** (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`):
  - :51: "Behavior-preserving refactors may proceed under the acts already in
    force. They may touch `apps/**`, `packages/**`, `scripts/**`, tests, CI and
    root manifests."
  - :52-55: "'Behavior-preserving' means none of the following changes:" "a
    rendered byte, a wire format, a refusal string or an exit code;" "a signed
    or digest-bound artifact;" "a consent, security or retention decision."
  - :56: "POC shared-model work stays at WIP one."
  - :60: "Each pull request states which CC-REV-1 classes it touches. Any pull
    request whose classes are not "none" gets the CC-REV-1 independent review,
    from a fresh-context reviewer on the default model."
  - :62: "**Which ones:** pull requests touching class 1 (authority
    boundaries), class 3 (deterministic observation) or class 4 (security),
    and class-6 pull requests that remove an endpoint."
- **AGENTS.md at edca4490:**
  - :95: "Never edit an artifact after an act has bound its digest."
  - :126: "6. Mutate the input and confirm the check fails, per predicate,
    before trusting it".
  - :132: "9. A claim of absence needs a sweep with a denominator."
  - :133: "10. Freeze the bytes a review is bound to; any later edit retires
    the review."
  - :134: "11. An evidence record names its subject and the subject's digest;
    a record that names neither cannot be re-checked against the bytes it
    describes."
  - :149: "POC shared-model changes have WIP one."
  - :237: "Fresh `git worktree`: run `npm ci` inside it first, or `NodeNext`
    silently resolves `@syzygy/*` to the main checkout's `node_modules`."
- **The bead** (`bd show syzygy-bpyt.7.6 --json`, read-only):
  - Design: "Delete orphans with their tests, or move them to a test-support
    entry; un-export test-only exports or mark each deliberate seam with a
    comment. Rendered bytes, wire output and model outputs unchanged. CC-REV-1
    class: none expected (dead code); state it."
  - Acceptance criteria: "1. Each orphan's consumer sweep recorded (method,
    denominator) and each removed or relocated. 2. The six test-only exports
    enumerated and resolved. 3. Suite green; Tests: +a ~b -c; rendered bytes
    unchanged on the POC fixtures."
- **Sources the new comments cite** (both at edca4490):
  - P-71, `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:58`:
    "Q3 arm (b), a pure drafter that writes no file".
  - `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:115` (candidate design
    material): "Arm (b): the drafter is pure and emits packet *data* on
    request, writing no file at all; an operator command renders it."

### Classification (re-ruled)

**None.** The repair changed what the PR touches in one direction only: it
removed the P1 gate from the touched set.

- **Class 1 and class 4.**
  - [Observed] `body-read-authority.ts` at edca4490 has sha256
    `f612651d13421c0ffcba0d8db9f5240dcb521aa2c0315b5316b92c52a7cb7b77`. That is
    the same as at `1d6731bb` and at `b7697f6a`. Its git blob is `c1337a19…`
    at both 1d6731bb and edca4490, and `git diff 1d6731bb edca4490` does not
    list it.
  - [Observed] Its four emitted files are byte-identical between my base and
    head builds: `.js`, `.d.ts`, `.js.map` and `.d.ts.map` (sha256 prefixes
    `0679e5813d5b46e5`, `ed256ce2da1df503`, `8b4c4304a154dfea` and
    `2639def0d9ccb3de`, each equal).
  - [Observed] `walkthrough-judgment.ts` (the PWB-REQ-022 evaluator) did not
    change after round 1: `git diff e81883f3 edca4490` does not list it. Its
    ordered `// mutation-point: <name>` population is the same at base and
    head: 88 named markers, list sha256 `a90cdaa8…` at both.

  No write-universe, typed-authority, adapter-authorization, SEC surface or
  egress path is touched.
- **Class 3.** [Observed] No emitted `.js` changes after round 1. The repair's
  emitted changes are comment lines only (section 6).
- **Class 6.**
  - [Observed] `packages/three-surface-poc-core/package.json` has `"private"`
    `True` and exports only `"."`. The barrel's export set did not change
    after round 1.
  - [Observed] All 19 routes per fixture answer identically base vs head
    (section 6).
- **WIP one.** [Observed] `gh pr list --state open` lists 506, 505, 503, 502
  and 487. For 506, 505, 502 and 487, `gh pr view <n> --json files` filtered
  to `packages/three-surface-poc-core/` returned `[]`.

## 3. What I ran, and the results

Setup:
- Two clones of `/home/tze/GitHub/syzygy`, `base` at `1d6731bb` and `head` at
  `edca4490`, under `scratchpad/rev-503b/`. Each got its own `npm ci`
  ("exit=0"), then `npm run build:poc` and `npm run build` (each "exit=0").
- [Observed] `readlink -f` on `node_modules/@syzygy/three-surface-poc-core`
  resolves inside each clone's own `packages/` directory.

| Check | Result (verbatim where quoted) |
|---|---|
| poc-core vitest project (head) | [Observed] "Test Files  33 passed \| 2 skipped (35)" / "Tests  1111 passed \| 2 skipped (1113)", exit 0 |
| poc app vitest project (head) | [Observed] "Test Files  88 passed \| 1 skipped (89)" / "Tests  1077 passed \| 2 skipped (1079)", exit 0. Includes "polaris-authority-sweep.test.ts (5 tests)", "pwb-mutation-sweep.test.ts (4 tests)" and "pwb-mutation.test.ts (5 tests)", all ✓ |
| Full `npx vitest run` (head) | [Observed] "Test Files  229 passed \| 3 skipped (232)" / "Tests  4982 passed \| 5 skipped (4987)", exit 0, with no timeout on this run. This equals the PR body's 4,982 |
| `npm run typecheck` (head, after `build:poc` and `build`) | [Observed] exit 0 |
| `python3 scripts/check_governance.py` | [Observed] head and base both "32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted". `diff` of the two outputs shows only the repo-root line, scope "3039" vs "3072" tracked, CG-2a "1931" vs "1946 files examined" and CG-3 "1810" vs "1811". Head: "CG-7e … 95 files examined, 0 findings"; "CG-7h  performed bootstrap transaction subjects remain exact — 317 predicates examined, 0 findings"; "CG-15 … 11 quotations examined, 0 findings" |
| `python3 scripts/check_quotations.py` | [Observed] exit 0 at both. `diff` of the base and head outputs: identical |
| PWB-REQ-014 authority sweep | [Observed] `polaris-authority-sweep.test.ts (5 tests)` passed in the app run |
| Census selftest (`record_selftest.py`) | [Observed] "selftest: 28 of 28 cases hold". Header "# tool sha256: c04bece0…2122". Body from the command line onward is identical to the stored `selftest-export-census-2026-10-22.txt`, which differs only on its "# tree commit:" line (47935fec vs my edca4490) |
| Census mutants (`mutate_census.py`) | [Observed] "mutants=24 killed=24 (failed case 24, crash only 0) survivors=[]". My record equals the stored one except `ranAtCommit` |
| Reviewer's own census mutants | [Observed] two survivors, see N9 |
| Census at base/head (`assemble_census.py base head`) | [Observed] base lexer "exports 589, {'dead': 3, 'internal': 134, 'public': 131, 'self-only': 233, 'test-only': 88}"; after lexer "exports 586, {'dead': 1, 'internal': 133, 'public': 131, 'self-only': 233, 'test-only': 88}". It equals the stored record except `afterCommit` |
| Lexer vs TypeScript printer, all tracked code files | [Observed] head: "files=496 differing=1"; base: "files=495 differing=1". The one file is `trajectory-projection.ts`, where the numeric literal `1_000_000n` gives lexer token `_000_000n` against printer token `n`. That is a numeric literal, not an identifier. The oracle detects the three known lexer limit forms (N9) |
| Comment-only check (`comment_only_check.py head e81883f3 … --merge-with 1d6731bb`) | [Observed] "changed=4 allCommentOnly=True retainedExport={'moduleExportsFunction': True, 'barrelReexportsSameFunction': True}". Baseline tree `6a08cd6f…`, equal to the record's `baselineTree`. My record equals the stored one except `treeCommit` |
| Comment-only mutants (`mutate_comment_only.py`) | [Observed] "controls=[True, True] mutants=6 killed=6 survivors=[]". Equal to the stored record except `ranAtCommit`. See N8 for what "6" counts |
| My own comment-only comparison (TypeScript printer, `removeComments: true`) | [Observed] `6a08cd6f` vs `edca4490`, `packages apps`: "changed=4 commonCode=477 identicalAfterPrint=477 differ=0 onlyOld=0 onlyNew=0". Each of the 4 files gives "printEqual=true" |
| Same, base vs head | [Observed] `1d6731bb` vs `edca4490`, `packages apps scripts`: "changed=9 commonCode=487 identicalAfterPrint=484 differ=3". The three are exactly `content-classification.ts`, `project-shape-coverage.ts` and `walkthrough-judgment.ts`, the round-1 deletion sites |
| Emitted code (`dist_code_diff.py base head`) | [Observed] "compared=948 differing=4 inOnlyOneTree=0". The four are the three deleted declarations plus the elided import. `projects` equals the stored record (True) |
| My raw byte diff of every `dist/` file, 10 projects | [Observed] "filesCompared=1906 differ=33 onlyOneTree=0": 3 `.tsbuildinfo`, 18 maps and 12 `.js`/`.d.ts`. In the 12, the only non-comment changed lines are the three deleted declarations and the constant's import and body (section 6). Round 1 counted 36; the 3 fewer are the gate's `.js`, `.js.map` and `.d.ts.map`, now byte-identical |
| Consumer sweeps (`consumer_sweep.py`) | [Observed] base: "tracked=3039 read=3039 commit=1d6731bb…", equal to the stored record. Head with `--exclude docs/evidence/poc-core-hygiene-2026-10-22/`: "tracked=3039 read=3039 commit=edca4490…". It differs from the stored record only in `treeCommit` and `trackedFilesExcluded` (33 vs 28: the directory has 33 files at edca4490 and 28 at 47935fec). Every subject agrees; the three deleted names give "files=  0" |
| Route capture (three runs, one fixture repository I made) | [Observed] each run: "variants=5 routesPerVariant=19,19,19,19,19 responses=230". My fixture `.json` gave revision `1f892687d53c829f9c2a4ee99bccccb23d6158df`, equal to the records' revision at a different path. Base run 1 and base run 2 are byte-identical files (`917f45af…`) |
| `compare_captures.py` over my three captures | [Observed] "responses=230 fixtures=5 distinct=5 keysVarying=30/46"; "cap-base-2.json (1d6731bb): variants bytes equal True, differing responses 0"; "cap-head.json (edca4490): variants bytes equal True, differing responses 0". Fixtures, distinct output, keys, 73 distinct bodies and the status mix `{'200': 150, '401': 40, '403': 20, '502': 20}` all equal the stored comparison |
| My capture vs the stored base capture | [Observed] 230 keys, same key set; 150 responses differ, all status 200, each with equal body length; the other 80 are equal. This agrees with the records' disclosure that 200-bodies depend on the fixture path |
| Comparison-tool mutants (`mutate_compare_captures.py`) | [Observed] on the stored captures: "control holds=True mutants=5 killed=5 survivors=[]", equal to the stored record except `ranAtCommit`. On my captures: the same line |
| Capture leak check (`route_capture_leak_check.py`, `TMPDIR` in my scratch) | [Observed] "holds=True real left=[] mutant left=['syzygy-poc-surface-fixture-<random>']". Tool and subject digests equal the stored record. My TMPDIR was empty afterwards |
| `/tmp` around my three captures | [Observed] `ls -d /tmp/syzygy-poc-surface-fixture-* /tmp/zz-route-capture-*` gave 250 entries before and the same 250 after (`comm -13` empty). The fixed capture script leaks nothing |
| Test-name lists | [Observed] `npx vitest list` gave 4989 lines at base and 4989 at head, both exit 0. My two list files are byte-identical (`dd1fd96f…`; the stored base list has the same digest). `compare_test_lists.py`: "Tests: +0 ~0 -0 (base 4989, head 4989)" |
| Record identity (my `record_identity.py`) | [Observed] "files=33 scripts=15 records=18". 18 of 18 records name at least one 40-hex commit. Records that name a tool digest name the head bytes: `comment_only_check.py` `553f08bb…`, `compare_captures.py` `7bc7d982…`, `export_census.py` `c04bece0…`, `route_capture_leak_check.py` `402d25bb…` and `route-capture.mjs` `42f35b84…`, each equal to `sha256sum` at edca4490 |
| Digest citers of the base bytes of the three files the repair edited | [Observed] over 3072 tracked files at edca4490 (full sha256, 16/12/8-hex prefixes and blob id): `evidence-population.ts` 0, `index.ts` 0, `test-cleanup.ts` 0 citers |
| Gate and evaluator records | [Observed] `git grep -l -F f612651d…7cb77 edca4490` gives the four `bpyt-6-2`/owner-act records plus this PR's `comment-only-check` and `dispositions`. `walkthrough-judgment.ts` sha256 at edca4490 is `a64ef4c0d3891a5e5e7073ef63d14b9c19d0c50bd40a1f96ed1a3341a24e808e`, named only by `dispositions-2026-10-22.json` |
| Canonical PROJECT-STATUS battery | **[Unknown] not re-run.** The PR body reports "commands=110 nonzero=0" at edca4490 (lane-reported) |

**Comment accuracy of the repaired comments**, checked at edca4490:
- [Observed] `index.ts`. Over the 73 tracked files under
  `packages/three-surface-poc-core/src`, `git grep -i -F "by design"` returns
  0 lines. The two cited lines say what the comment attributes to them (quoted
  in section 2). The note's reason holds:
  `docs/evidence/syzygy-dov41-unknown-routes-rule6-2026-10-03.json:31` names
  `owner-act-drafter.ts` with `1dfea09c…62e3`, which is that file's sha256 at
  edca4490.
- [Observed] `evidence-population.ts`. Line 8 of the lane-A population record
  is `"measurementScript"`, and it contains `dist/evidence-population.js`.
  The M1 note carries "candidate design material … binds nothing by itself"
  at :385-386. For the cited range, see N11.
- [Observed] `test-cleanup.ts`. `git grep -F test-cleanup` over `packages`,
  `apps`, `scripts` and `.github` finds importers only in `model.test.ts:17`
  and `test-cleanup.test.ts:3`. The comment now names both.

## 4. Round-1 findings, status

| Round-1 note | Status | Evidence |
|---|---|---|
| N1 head moved past the reviewed commit | **Repaired** | [Observed] This round binds edca4490. The delta is comment-only, by the lane's tool (reproduced) and by my own printer comparison: "identicalAfterPrint=477 differ=0". `36a45cd2` is the clean merge (section 1). See N8 for a limit of the lane's tool that does not affect this delta |
| N2 overstated comments | **Repaired**, one new imprecision | [Observed] All three wording issues are fixed (section 3). The new path:line citation in `evidence-population.ts` is narrower than its passage: N11 |
| N3 census selftest gaps, undisclosed lexer limits | **Partly repaired** | [Observed] The 5 new cases and 4 new mutants are present. Each round-1 mutant is killed: template-expression by 3 cases, regex-class by 1 new case, brace-depth by 1, division-after-paren by 1. The brace-depth mutant is killed only by "comment after braces inside a template expression is a comment", so it is not equivalent. Both limits are in the docstring. **Not repaired:** two further lexer predicates survive 28/28, and the docstring misstates which way the limits err (N9). No figure is affected (lexer = printer over 496/495 files) |
| N4 record identity and re-runnability | **Repaired** | [Observed] (a) 18/18 records name a commit. (b) The usage line now reads `node route-capture.mjs <tree> <out.json> <fixture-repo-path>`, matching `process.argv[4]`. (c) Path, revision and construction are recorded; the claim is scoped to "equality between the compared trees only"; my independent fixture reproduces the revision and every equality. The stored digests are not byte-reproducible because the recorded fixture path, under the lane's scratch directory, no longer exists; the record says so. (d) The leak is fixed, and the leak check plus its mutant reproduce. Residual: `assemble_verification.py` reads gate logs that are not retained, so the verification record is re-derivable only by re-running the gates. I re-ran each gate and every figure matches |
| N5 AC1 met by disposition | **Repaired by disclosure; coordinator action open** | [Observed] The PR body's Residuals carry the N5 text. The bead's `notes` do not yet record it, as expected before close. N10 adds the same treatment for one AC2 subject |
| N6 AC2 selection predicate | **Repaired** | [Observed] The `dispositions` `selection` field states the predicate and "testOnlyAtBase": 88, then a count of 9 (names listed), the 3 orphan entry functions removed, and "remaining" 6. My re-run of the census at 1d6731bb gives the same 9 `selfZero` rows, which leave exactly the six. The assembler raises `SystemExit` if the predicate does not reproduce the subjects (`assemble_dispositions.py:146`) |
| N7 mutation records for gate and evaluator | **Repaired** | [Observed] The gate is byte-identical to base (section 2). The four retained records name its current digest. The evaluator's head digest `a64ef4c0…808e` is recorded, and its predicate-marker population is unchanged |

**Rule 10, re-derivation.** [Observed] The repaired figures are re-derived at
the new base, not copied from round 1:
- tracked files: 3039 at 1d6731bb, against round 1's 3029 at b7697f6a;
- dist comparison: 948;
- test lists: 4989 / 4980;
- sweeps and census: re-run at 1d6731bb.

The one figure carried from round 1, "the reviewer's printer cross-check over
the 494 tracked code files", is labelled in the PR body as "reviewer's
measurement, not re-run here". I re-ran it at 1d6731bb and edca4490 (495 and
496 files) and it holds.

## 5. New findings

No blocking findings (F) in this round. Four notes, numbered after round 1's
N1–N7.

### N8 — The comment-only check cannot see whitespace edits inside template literals, and its "6 of 6 mutants" includes a negative control (severity: low; evidence tool)
- **Evidence.**
  - [Observed] `comment_only_check.py` compares
    `[line.rstrip() for line in strip_comments(text).splitlines() if line.strip()]`.
    This drops trailing blanks and blank lines everywhere, including inside
    template literals and strings. My probe (`tools/probe_norm.py`) printed:
    - "trailing space inside a template literal: normEqual=True rawEqual=False"
    - "blank line added inside a template literal: normEqual=True rawEqual=False"
    - "code token added (control, must differ): normEqual=False rawEqual=False"
    - "comment edited (control, must be equal): normEqual=True rawEqual=False"
  - [Observed] The TypeScript-printer predicate I used tells those cases apart
    (`tools/probe_printer.mjs`): "trailing space inside a template literal:
    printEqual=false", "blank line added inside a template literal:
    printEqual=false", "comment edited (must be equal): printEqual=true",
    "JSDoc edited (must be equal): printEqual=true".
  - [Observed] In `mutants-comment-only-check-2026-10-22.json`, record
    `source-comment-edit-is-not-a-failure` has `"expectedFailure": "comment-only-true"`
    and `"killed": true`. That record is a negative control: it is passed by
    staying silent. So "6 of 6 mutants killed" (PR body, N1 row) is 5
    mutants plus 1 control, alongside the 2 named controls.
  - [Observed] Effect on this PR: none. The four files the check covers print
    identically with comments removed, and every changed line in their raw
    diff begins with `//`.
- **Failure scenario.** The tool sits under `docs/evidence/` and is the
  natural check for the next "comment-only" follow-up. That follow-up edits
  whitespace inside a multi-line template literal that renders page text,
  which changes a rendered byte. The check reports `allCommentOnly=True`, and
  a review accepts it.
- **Proposed fix.** No byte change before merge. When the tool is reused:
  - compare TypeScript prints with `removeComments: true` (as in
    `tools/ts_print_compare.mjs`), or compare `strip_comments` output with
    blank-line removal limited to positions outside literals;
  - add a mutant "whitespace inside a template literal", expected
    comment-only-false;
  - report `source-comment-edit-is-not-a-failure` under `controls`, giving
    "5 of 5 mutants, 3 controls".

### N9 — The census selftest still leaves two template predicates unpinned, and the docstring says the limits only under-count (severity: low; evidence tool, carries into the 233-export follow-up)
- **Evidence.**
  - [Observed] Two single-fragment mutants of `export_census.py` at edca4490
    each leave `--selftest` at "selftest: 28 of 28 cases hold", exit 0
    (`tools/my_census_mutants.py`):
    1. `nested-template-not-entered`:
       ``"        if c == '`':\n            out.append(c); i += 1; in_template = True; continue"``
       → ``"        if c == '`' and not tpl:\n            out.append(c); i += 1; in_template = True; continue"``.
       A backtick inside a `${ }` expression no longer opens a template.
    2. `expression-close-stays-in-code`:
       `"tpl.pop(); out.append(c); i += 1; in_template = True; continue"`
       → `"tpl.pop(); out.append(c); i += 1; in_template = False; continue"`.
       Text after a template expression's `}` is lexed as code.
  - [Observed] Two cases kill them and pass on the original
    (`tools/my_census_killers.py`):
    - ``const s = `${`/* X`}`; X`` (expected 2): original 2,
      nested-template-not-entered 0, expression-close-stays-in-code 2;
    - ``const g = `${d}/*`; X /* c */`` (expected 1): original 1,
      nested-template-not-entered 1, expression-close-stays-in-code 0.
  - [Observed] The case added as the nested-template test, "comment after a
    nested template in a template expression is a comment", is killed by
    exactly the same two mutants as "comment inside a template expression is a
    comment" (`lexer-block-comment-kept` and
    `lexer-template-expression-never-entered`). It does not pin nesting. (The
    270c00bd commit message claims only that it "also kills 'template
    expressions never entered'", which is true.)
  - [Observed] The new docstring says "Known limits of the lexer. Both
    under-count uses, so an export in use could be classed `dead`". The same
    misread also over-counts when the regex holds a quote: the quote opens a
    string, and the lexer keeps string text, comments included. Probes:
    - `if (a) /'/.test(s); // X\nY` gives X expected 0, got 1;
    - `export default /'/; // X\nY` gives X expected 0, got 1.

    The TypeScript-printer oracle flags both ("lexerOnly= {'X': 1}"). The
    docstring's advice, to cross-check "Before trusting a `dead` or
    `self-only` class", therefore does not cover an over-count. An over-count
    can lift a truly dead or self-only export into `test-only`, `internal`
    or `public`.
  - [Observed] Effect on this PR: none. Lexer and printer identifier
    multisets agree on 495 of 495 code files at base and 496 of 496 at head,
    apart from the `1_000_000n` numeric literal.
- **Failure scenario.** The 233-export un-export follow-up reuses this tool
  as-is. A regression in either predicate passes `--selftest`. Or a file with
  a quote-bearing regex after `)` or `export default` hides a self-only
  export from the sweep, and nobody cross-checks, because the docstring says
  only `dead`/`self-only` need it.
- **Proposed fix.** In the follow-up bead, before reuse:
  - add the two killing cases above to `selftest()`;
  - add the two mutants to `mutate_census.py`'s `MUTANTS`;
  - reword the limit paragraph to "can under- or over-count uses; before
    trusting any class on such a corpus, cross-check against TypeScript's
    printer", or run the printer oracle (`tools/print_tree.mjs` plus
    `tools/lexer_vs_printer.py`, with `setParentNodes` true) as a standing
    step of the census.

### N10 — AC2 for `appendEvaluation` is now met by a recorded disposition, not by the design's comment (severity: low; coordinator action, no byte change)
- **Evidence.**
  - [Observed] The bead design reads "un-export test-only exports or mark
    each deliberate seam with a comment".
  - [Observed] The N7 repair removed the gate's comment, as round 1's second
    option allowed. At edca4490 there are 5 "Test seam" lines in 4 files
    under `packages/three-surface-poc-core/src`, one for each of the five
    other subjects. `body-read-authority.ts` has none.
  - [Observed] `dispositions-2026-10-22.json` records `appendEvaluation` as
    "kept unchanged; no comment added (body-read-authority.ts stays
    byte-identical to the base)", with its reason. The PR body states the same
    ("The sixth, `appendEvaluation`, is in `body-read-authority.ts`, the P1
    gate, which this PR leaves **byte-identical to the base**").
  - [Inferred] Keeping the gate's act-bound mutation evidence on its exact
    bytes outweighs a comment. This is the right trade.
- **Failure scenario.** The bead is closed as "six resolved by Test seam
  comment". A later audit, or the un-export sweep, finds `appendEvaluation`
  unmarked, reads it as an oversight, and edits the P1 gate to add the
  comment. That retires the four records that name its digest.
- **Proposed fix.** At close, the coordinator records AC2 as: five resolved by
  a Test seam comment, and one (`appendEvaluation`) by its recorded
  disposition, to keep the gate's bytes. Record it beside the N5 note for AC1.
  If a visible marker is wanted later, put it next to
  `export * from './body-read-authority.js'` in `index.ts` (no digest citer at
  base, section 3). That would be a new review round, and it is not needed
  for merge.

### N11 — The M1 citation names a narrower range than its claim, and three artifacts give three ranges (severity: cosmetic)
- **Evidence.**
  - [Observed] `evidence-population.ts:3-5` at edca4490 reads
    "docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md:382-383 (candidate design
    note, binds nothing) -- any new page-size evidence record carries a
    `population` block derived with `derivePopulationBlock` from this path".
  - [Observed] In the note, "any new M1 (or related Polaris page-size)
    evidence record must carry a `population` block" is at :380-381. Lines
    :382-383 hold only "with `derivePopulationBlock` in" and the path. "This
    note is candidate design material like the rest of this document and
    binds nothing by itself" is at :385-386.
  - [Observed] The same passage is cited as `:380-384` in
    `dispositions-2026-10-22.json` (`citations`) and as `:380-386` in the PR
    body.
- **Failure scenario.** A reader follows `:382-383` and finds a sentence
  fragment. The attribution the comment gives ("binds nothing") is in
  neither the comment's range nor the record's.
- **Proposed fix.** No byte change before merge. The next time this comment
  or the record is edited for another reason, cite `:380-386` in both.

## 6. Every changed output

**None changed.** The evidence, at base 1d6731bb vs head edca4490:

- **Rendered and wire bytes.**
  - [Observed] Three captures over one fixture repository (made in my scratch
    directory, revision `1f892687…`):
    - 230 of 230 responses equal, base vs head;
    - the `variants` objects byte-equal across all three (canonical sha256
      prefix `a380ae18292b2836` for each);
    - "fixtures=5 distinct=5 keysVarying=30/46", so the probe can tell the
      fixtures apart;
    - statuses 200×150, 401×40, 403×20, 502×20, so refusal paths are
      covered.
  - [Observed] Credentialed GETs ran with and without the bearer token, which
    is the script's design.
- **Emitted code.**
  - [Observed] 948 `.js`/`.d.ts` files, comments stripped: 4 differ, all
    deletion sites:
    - `content-classification.d.ts` "-export type ClassificationOutcome = ClassificationRecord['outcome'];";
    - `project-shape-coverage.d.ts` "-export type FactFamilyKind = (typeof FACT_FAMILIES)[number];";
    - `walkthrough-judgment.d.ts` "-export declare const JUDGMENT_INVALID_CASE_IDS: readonly JudgmentInvalidCase[];";
    - `walkthrough-judgment.js`, the constant's lines and
      "-import { COMMON_INVALID_CASES, } from './body-read-authority.js';".
  - [Observed] Raw bytes: 1906 files, 33 differ, none in only one tree. The
    gate's four emitted files are byte-identical, and no file under
    `apps/three-surface-poc/dist` differs other than `.tsbuildinfo`.
- **Source.** [Observed] With comments removed:
  - 484 of 487 common code files under `packages`, `apps` and `scripts` print
    identically base vs head. The three that differ are the round-1 deletion
    sites.
  - Since round 1, 477 of 477 print identically against the
    `e81883f3`-plus-main baseline.
- **Tests.** [Observed] The test-name lists are byte-identical (4989 lines
  each): **`Tests: +0 ~0 -0`**. The full suite passes: 4982 passed, 5 skipped.
- **Governance outputs.**
  - [Observed] `check_quotations.py`: identical.
  - [Observed] `check_governance.py`: same verdict line. Only file counts
    differ, because the evidence directory adds 33 tracked files.
- **Digest-bound artifacts.**
  - [Observed] No act-bound file is edited: CG-7e, CG-7h and CG-15 pass.
  - [Observed] The three files the repair edited have 0 digest citers at
    base. The P1 gate's bytes, and the four records that name them, are
    preserved.

## 7. Verdict per acceptance criterion

| AC | Verdict | Basis |
|---|---|---|
| 1. Each orphan's consumer sweep recorded (method, denominator) and each removed or relocated | **Met in substance; literal wording met by disposition** (round-1 N5, coordinator action open) | [Observed] The sweeps are recorded with two methods that agree, and denominator 3039 at both trees, which I re-ran. Disposition per orphan: one deleted, two kept as consumed, one kept as test support |
| 2. The six test-only exports enumerated and resolved | **Met**, with N10 | [Observed] The six are enumerated by a published predicate, which I re-derived: 88 → 9 → 6. Five are resolved by a Test seam comment, and the comments are accurate. One (`appendEvaluation`) is resolved by a recorded disposition that keeps the gate's bytes |
| 3. Suite green; Tests: +a ~b -c; rendered bytes unchanged on the POC fixtures | **Met** | [Observed] The full suite gives 4982 passed, 5 skipped, exit 0, at edca4490. `Tests: +0 ~0 -0`. 230 of 230 fixture responses are identical, and 5 of 5 fixtures are distinct |

## 8. Test quality

- [Observed] The PR adds and changes no product tests. Since round 1, the
  only test-file changes under `packages/` are main's PR #504 pins, which
  arrived byte-identical through the merge. Two existing tests carry the
  safety: `pwb-mutation.test.ts` and `pwb-mutation-sweep.test.ts` (each
  literal fragment "occurs exactly once in its current source"). Both pass at
  head.
- [Observed] **New census selftest cases: none of the five is unable to fail.**
  Each is killed by at least two of the 24 recorded mutants:
  - template-expression comment: 2 mutants;
  - nested-template: 2;
  - braces: 3, including the only kill of brace-depth;
  - regex class: 2;
  - division after `)`: 2.

  This is from my re-run, which equals the stored `failedCases`. The
  expected values are hand-written literals. The weakness is coverage, not
  vacuity: the nested-template case does not pin nesting, and two template
  predicates survive (N9).
- [Observed] The comment-only check's mutants are real perturbations of the
  tree, restored in a `finally` block; `git status` was clean after my run.
  Its "baseline predicate observable" control (without `--merge-with` it
  reports "changed=6 allCommentOnly=False") is a good control. N8 covers
  its blind spot and its count.
- [Observed] The comparison tool's rule-6 record perturbs the inputs: digest,
  status, a dropped key, fixture revision and fixture path. 5 of 5 are
  detected, and the record reproduces on my captures as well as on the
  stored ones.
- [Observed] The leak check uses a private `TMPDIR` and a deletion mutant
  that leaves exactly one directory. It is a sound rule-6 record for the N4(d)
  fix.
- [Observed] The route probe still uses five well-formed fixtures. It has no
  malformed or altered-prose records, which would matter only under a
  class-1 reclassification, and class none stands.

## 9. Cleanup

- Removed:
  - both scratch clones (`rev-503b/head`, `rev-503b/base`);
  - my fixture repository and its `.json` (`rev-503b/fixture/`);
  - the census mutant copies (`rev-503b/mut/`);
  - my private TMPDIR for the leak check (`rev-503b/tmpdir/`, empty when
    removed);
  - the large printer dumps and test lists under `rev-503b/out/`.
- Kept, with no repository-body or target content:
  - this raw;
  - my tool scripts under `rev-503b/tools/`;
  - my small records under `rev-503b/out/`: captures, comparison, mutant
    re-runs, sweeps, census, gate outputs and vitest logs;
  - my regenerated diffs (`my-review.diff`, `my-pre.diff` and
    `my-repair.diff`, byte-equal to the brief's).
- **Left in place, not attributable.** Two directories appeared in `/tmp`
  during my full-suite window: `/tmp/syzygy-poc-surface-fixture-kA5F78`
  (05:53:59) and `/tmp/syzygy-poc-surface-fixture-yVNvD1` (05:53:45), each a
  synthetic fixture tree (`README.md apps docs openspec src tests`).
  - [Inferred] Either my `npx vitest run` or another lane's concurrent tests
    created them. 250 such directories predate this review.
  - I did not delete them, because they may belong to a live run in another
    session. They are not produced by this PR's capture script: my three
    capture runs left `/tmp` unchanged.
- Not done, as instructed: no `bd` mutation, no push, no PR comment, no merge.
  No worktree under `/home/tze/GitHub/syzygy/.worktrees/` was touched. No
  process was killed.
