# R-GP-IMPL-ISLAND-DECOUPLING-1 — CC-REV-1 implementation review of syzygy-bpyt.8.1, round 1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 6ac21f2c
Subject: r1-review.diff sha256 3edfd5f6278f7eb1c593141c9d671e85e2571be1c2b1c80534c5e1433511bd82

Reviewer: rev-510, a fresh-context reviewer that did not author the change. Date: 2026-10-22. Scratch clones:
`old` at `c55acb73`, `new` at `6ac21f2c` and `mut`, a clone used for mutants and then for a trial merge. Each clone was built
with `npm ci` and `npm run build`. No Butlers or other target-repository content was read. No credential file was opened.
No bd mutation, push, PR comment or merge was made.

Verdict basis: no finding requires the reviewed bytes to change before merge. I found no input on which a gate accepts or
refuses differently, and no rendered byte that differs, over the populations named in section 3. N1–N6 below are notes.

## 1. Subject identity checks

- [Observed] `sha256sum r1-review.diff` returned
  `3edfd5f6278f7eb1c593141c9d671e85e2571be1c2b1c80534c5e1433511bd82`, which matches the brief.
- [Observed] `git diff c55acb73 6ac21f2c --output=regen.diff`, then `sha256sum`, returned the same digest
  (`3edfd5f6278f7eb1c593141c9d671e85e2571be1c2b1c80534c5e1433511bd82`). So the subject file is exactly that diff.
- [Observed] `git diff --shortstat c55acb73 6ac21f2c` returned ` 80 files changed, 38435 insertions(+), 745 deletions(-)`.
  `git diff --name-status -M` gives `{'M': 46, 'A': 34}`: there are no renames, copies or deletions.
- [Observed] `git merge-base 6ac21f2c 68c553b8` (current `origin/main`) returned `c55acb73753dc8d29d53b34b38b5d2af0cee6080`.
- [Observed] `ee89766a` has the parents `56948911cc08d93e3aee20fd9fdd51ac7273e83c` and `c55acb73753dc8d29d53b34b38b5d2af0cee6080`.
  `git diff --name-only ee89766a 6ac21f2c` lists 13 files, all under `docs/evidence/syzygy-bpyt-8-1/`. That confirms both
  claims: the code subject is `ee89766a`, and the head differs from it only in evidence.
- [Observed] `gh pr view 510` reports `headRefOid` `6ac21f2cd88c91e5fa5329ce01106737a8685ebd`, state `OPEN`.

## 2. Clauses relied on (quoted)

- CC-REV-1 (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md:31-41`):
  "1. **authority boundaries** — write-universe, typed-authority table, adapter authorization (VIS-5, VIS-6)"; "3.
  **deterministic observation** — snapshot composition, evaluation identity, the deterministic/inferred seam (VIS-7)"; "4.
  **security** — anything under SEC-1…SEC-5, auth surfaces, egress paths"; "6. **public interface** — machine-queryable
  endpoints, adapter contracts, anything an external consumer can depend on".
  - My ruling: classes 1, 3, 4 and 6 are touched, and classes 2, 5 and 7 are not. This agrees with the PR's declaration.
  - Class 1: the injected-renderer adapter, and the import specifiers on the gated modules `reverify.ts`, `check.ts`,
    `screen.ts` and `class-gate.ts`.
  - Class 3: the quote-flag seam that feeds the Inferred and Unknown labels.
  - Class 4: the provider egress code's reachability from the CLI, and the page-sink "escaped-text-under-csp" contract.
  - Class 6: the package `exports` maps.
  - Classes 2, 5 and 7: no identity minting, no `.syzygy/**` schema change and no certificate code.
- GP-Q0 (`OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md:52-55`): "'Behavior-preserving' means none of the
  following changes: a rendered byte, a wire format, a refusal string or an exit code; a signed or digest-bound artifact; a
  consent, security or retention decision."
- GP-Q0 (same file, lines 62-66): "**Which ones:** pull requests touching class 1 (authority boundaries), class 3
  (deterministic observation) or class 4 (security), and class-6 pull requests that remove an endpoint." "**The checks:**
  an old-versus-new differential over a mutated-record corpus that includes records with altered prose; a rule-6 mutant for
  each predicate; a non-blocking owner notice in the cycle report."
- GP-Q0 (same file, lines 95-96): "Any change not listed here to what a gate accepts or refuses stops and returns to the
  owner."
- GP-Q8 (same file, line 81): "| The parked provider island | **Kept parked.** Bead `8.1` decouples it. Deletion is revisited
  at the next audit |"
- AGENTS.md verification rules at `6ac21f2c`:
  - rule 6: "Mutate the input and confirm the check fails, per predicate, before trusting it";
  - rule 9: "A claim of absence needs a sweep with a denominator.";
  - rule 11: "An evidence record names its subject and the subject's digest; a record that names neither cannot be
    re-checked against the bytes it describes."
- Bead acceptance, quoted from the brief, which quotes `bd show syzygy-bpyt.8.1`:
  - (1) "Import-boundary test lists the island and fails when a CLI-reachable module imports it (rule-6 recorded).";
  - (2) "Brief, render and provider goldens byte-identical.";
  - (3) "Reachability report before/after attached."
- Test-rigor bar (`th-engineering/subskills/test-rigor/SKILL.md`):
  - Core Rule: "A test is worth keeping only if some plausible bug makes it fail.";
  - bar 4: "Expected values are literals or independently derived.";
  - workflow step 2: "name a one-line bug in the code under test this test would *not* catch but should."
- Dependency-hygiene bar (`th-engineering/subskills/dependency-hygiene/SKILL.md`):
  - bar 2: "**No cycles, at any granularity**";
  - bar 3: "A module exports what its contract promises, not whatever happens to be defined."

## 3. What I ran, and the results

All test runs used a private TMPDIR (`/tmp/r510-1` to `/tmp/r510-4`). Load average was between about 17 and 64 on 12 cores
throughout (`cat /proc/loadavg` read `64.06 55.34 44.08` during the trial-merge runs).

1. **Typecheck.** `npm run typecheck` in `new` printed only the `tsc -b …` command line. It reported no diagnostics and exited
   0 [Observed]. The same holds on the trial merge (item 15).
2. **Targeted tests at `6ac21f2c`.** I ran island-boundary, `polaris-dossier` brief and render,
   `dossier-render-provider-golden`, `dossier-render` and `page-sink`. The JSON report:
   `{'numTotalTestSuites': 21, 'numTotalTests': 129, 'numPassedTests': 129, 'numFailedTests': 0, 'numPendingTests': 0,
   'success': True}`. Per file: 4/4, 26/26, 42/42, 1/1, 53/53, 3/3 [Observed].
   The daemon-entry pin (`packages/cap1-system`, `daemon-entry-unchanged`) returned `Test Files  1 passed (1)` and
   `Tests  15 passed (15)` [Observed].
3. **Projects** `@syzygy/polaris-generation-core`, `@syzygy/polaris-dossier` and `@syzygy/three-surface-poc-app` at the head:
   `Test Files  1 failed | 138 passed | 1 skipped (140)` and `Tests  2 failed | 3067 passed | 3 skipped (3072)`.
   - Both failures are in `packages/polaris-dossier/src/start-gates.test.ts`, which this PR does not change:
     `Error: Test timed out in 5000ms.` (×2) [Observed].
   - Re-run alone together with `package-reader.test.ts`: `Tests  403 passed (403)` [Observed].
   - So this is load [Inferred]. See item 15 and N6 for the lane's `package-reader.test.ts` timeouts.
4. **`python3 scripts/check_governance.py`**, run from each clone. Both outputs end
   `32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted` [Observed].
   - `diff cg-old.txt cg-new.txt` shows only the repo-root and scope lines (`3150` → `3184` tracked files) and one count:
     `OK    CG-2a  retired acceptance phrase confined — 1985 files examined` → `1993 files examined`, both
     `0 findings` [Observed].
   - (One accidental first invocation ran in the main checkout's working directory. It is read-only, and I discarded it.)
5. **`python3 scripts/check_quotations.py`** in each clone: the two outputs are byte-identical (`diff` is empty). The first
   line: `OK    QC-1  a quotation beside a path:line locator was said by that file — 33 quotations examined in 15 of 926 .md
   files scanned (loc-paren-quote 2, loc-colon-quote 21, quote-paren-loc 10), 0 findings` [Observed].
6. **The lane's 25 mutants, re-run in `mut` at `6ac21f2c`** with a byte copy of `mutate.py` (runner sha256 `01d7daa5…`,
   identical to the record's).
   - Every id has the same outcome as `mutants.json`: 23 `killed`, and `S4-local-view-runs-the-quote-check` and
     `S4b-local-view-runs-the-quote-check-dossier-render-step` `survived` [Observed].
   - `fileSha256` and `testFileSha256` equal the record's, and every old/new fragment equals the record's [Observed].
7. **Reviewer mutants R1–R9** (my spec: `rev-510/tools/reviewer-mutants-spec.json`). Each targets
   `island-boundary.test.ts`. Output verbatim:
   ```
   R1-non-literal-dynamic-import-of-core-root-in-render-step survived 0
   R2-template-literal-dynamic-import-of-core-root-in-render-step killed 1
   R3-export-star-of-core-root-in-class-gate killed 1
   R4-live-subpath-node-condition-resolves-to-core-root survived 0
   R5-broker-client-entry-imports-core-root survived 0
   R6-create-require-of-core-root-in-render-step survived 0
   R7-import-type-node-of-core-root-in-class-gate killed 1
   R8-relative-cross-package-island-import-in-screen killed 1
   R9-island-import-hidden-inside-the-exception survived 0
   ```
   The fragments:
   - R1: `const ISLAND_SPECIFIER = '@syzygy/polaris-generation-core'; … import(ISLAND_SPECIFIER)` in `render.ts`.
   - R4: a `"node": "./dist/index.js"` key placed before `"import"` in core's `./live` export.
   - R5: `import '@syzygy/polaris-generation-core';` in `broker-client.ts`.
   - R6: `createRequire(import.meta.url)('@syzygy/polaris-generation-core')` in `render.ts`.
   - R9: `import '../../polaris-generation-core/src/pipeline.js';` in `consent-ports.ts`.
8. **My independent static reachability sweep** (`rev-510/tools/static_reach.mjs`).
   - Method: it walks every reached `src/*.ts` file's TypeScript AST and resolves each specifier with
     `ts.resolveModuleName` under NodeNext, which applies the real `exports` maps, conditions and `.js`→`.ts`. It maps
     workspace `dist` back to `src`, and records static, type-only, re-export, `import =`, literal and non-literal
     `import()`, import-type nodes, `require` calls and process or worker spawns.
   - Results, each verbatim from the record's `summary`:
     - before (`c55acb73`): `{"reached": 138, "edges": 644, "islandReached": 7, "intoIsland": 14, "rootImporters": 22,
       "problems": 0}`;
     - before, with `consent-ports.ts` not followed: `"islandReached": 7, … "rootImporters": 21`;
     - after (`6ac21f2c`): `{"reached": 143, "edges": 657, "islandReached": 7, "intoIsland": 11, "rootImporters": 1,
       "problems": 0}`. The one root importer is
       `packages/polaris-generation-consent/src/consent-ports.ts:2 import @syzygy/polaris-generation-core`, and all 11
       into-island edges are re-exports in core `index.ts`;
     - after, with `consent-ports.ts` not followed: `{"reached": 135, "edges": 618, "islandReached": 0, "intoIsland": 0,
       "rootImporters": 0, "problems": 0}`;
     - from `dossier-site.ts` alone at the head: `{"reached": 83, "edges": 274, "islandReached": 0, "intoIsland": 0,
       "rootImporters": 0, "problems": 0}`;
     - from `broker-client.ts`, before and after: `{"reached": 1, "edges": 1, "islandReached": 0}` [Observed].
   - The reached-module counts equal the lane's source graph (138 → 143). My edge counts are higher because I also count
     builtin and external edges.
   - Over the 143 reached modules: 0 non-literal `import()`, 0 `require` calls and 0 worker constructions. The only Node
     file launches are `polaris.ts:53` `new URL('./broker-client.js', import.meta.url)`, run via a shim at line 355, and
     `polaris.ts:113`, which spawns `process.execPath` on `apps/syzygy/dist/main.js` (the same entry) [Observed].
   - Exports maps: across all 12 workspace subpaths, Node's condition choice (the first of `node`/`import`/`default`)
     equals the test's `import ?? default` choice [Observed].
   - Island list: the test's 20 entries equal the bead's 20 modules, 7 in core and 13 in the app [Observed,
     `git ls-files`].
9. **My runtime reachability probe** (`rev-510/tools/runtime_reach.mjs`). It uses a `registerHooks` load hook and loads the
   compiled modules `main.ts` imports, including both dynamic branches.
   - head: `"loadedInRepo": 139` with 7 core island `dist/*.js` loaded;
   - head with `consent-ports.js` stubbed: `"loadedInRepo": 131, "islandLoaded": []`;
   - base: `"loadedInRepo": 134` with the same 7, whether or not it is stubbed [Observed].
   - Each count is one below the lane's runtime graph (135 → 140) [Inferred: my probe does not count `main.js` itself].
10. **Differential re-run** (`old` against `new`). This is a copy of the lane's `differential.mjs` plus one added comparison
    (`localRenderViaXorEntry`: the old XOR entry `renderDossier({local, sources})` against the new `renderLocalDossier`).
    - `localRender {"fixtures": 16, "identical": 16, "distinctOutputs": 15}`;
    - `localRenderViaXorEntry {"fixtures": 16, "identical": 16, "distinctOutputs": 15}`;
    - `providerRender {"fixtures": 26, "identical": 26, "distinctOutputs": 16}`;
    - brief: `"fixtures": 3, "identical": 3, "distinctOutputs": 3`. The guidance on both sides has
      `"oldVersion": "polaris-author-dossier-v2", "newVersion": "polaris-author-dossier-v2", "identical": true, "sha256":
      "17ea6ff5bc05f02b27343da8184033104295b1c02b82ca5e784d6316d1ecea69", "bytes": 4469`. The brief rows include
      `altered-prose`;
    - `validators {"fixtures": 62, "identical": 62, "distinctOutcomes": 18, "refusals": 51}`;
    - `compiledModules {"modules": 24, "identicalAfterLiveSpecifier": 20, "identicalOutsideImportStatements": 23,
      "identicalCodeOutsideImportStatements": 24}` [Observed].
    - The one module that differs outside its import statements but not in code is `admitted-input.js`, an island
      module [Observed].
    - The gate modules `check.js`, `reverify.js`, `screen.js` and `class-gate.js` are byte-identical once the `/live`
      specifier is set back to the root [Observed]. So is `render.js`, which runs the page-sink check.
11. **Exports and bindings.**
    - TypeScript-checker export surfaces at both commits:
      - core `.`: 239 → 245, none removed, 6 types added (`DossierDraft`, `DraftBlock`, `DraftDiagram`,
        `DraftDiagramEdge`, `DraftDiagramNode`, `DraftParagraph`);
      - core `./live`: 165 names, a subset of the root;
      - `./dossier-render`: 4 → 4, the same names;
      - `./dossier-site`: 8, new;
      - consent: 57, unchanged. `consent-ports.ts` 12, the dossier index 331, `provider-draft.ts` 32,
        `dossier-evaluation.ts` 33, `brief.ts` 13, `draft-preview.ts` 5 and `local-render.ts` 12, each unchanged
        [Observed].
    - At runtime:
      - 94 of 94 value names in `/live` are `===` the root's;
      - `DossierRenderError` and `sourceRoute` from `dossier-render` are the same objects as from `dossier-site`;
      - `renderDossier.pageSinkContract` and `renderLocalDossier.pageSinkContract` both equal
        `'polaris/page-sink/escaped-text-under-csp/1'` [Observed].
      - `render.ts:65` compares `renderer.pageSinkContract !== PAGE_SINK_CONTRACT` by string, and `render.ts:181` is the
        one production call, `renderer({ local, sources: built.sources })` [Observed].
12. **Generators and splits.**
    - `regen_check.py`, with inputs `3000698f` (provider-draft) and `0d4d5098` (dossier-render), reproduces all 5 files
      (`"allIdentical": true`). Both inputs equal the `c55acb73` bytes (empty `git diff`) [Observed].
    - My line-conservation check on the two splits (`rev-510/tools/conserve.py`):
      - `provider-draft.ts`: the only changes are comments and the annotations of `text` and `handle`, now
        `Extract<Schema,{type:'string'}>`;
      - `dossier-render.ts`: the only changes are the `View`→`DossierView`/`quoteFindings` seam and the adapter
        [Observed].
13. **Bound records.**
    - Citer sweep in the base tree (`rev-510/tools/citers_at.py`, scanning `c55acb73`): `tracked scanned 3150; modified
      files 46; with a digest or blob citer 21`, `citing records: 23 | outside docs/evidence/: []`,
      `governed-plane citers: []` [Observed]. This matches the PR's 21 and 23.
    - The same sweep scanning the head reports 46 of 46. The extra citers are the lane's own records in
      `docs/evidence/syzygy-bpyt-8-1/` [Observed].
    - A path sweep of `.syzygy/**`, `openspec/**` and `*MANIFEST*` finds governed files that name 15 of the 46 changed
      paths. `grep -c` over the sweep output counts 15 lines with a non-empty path-citer list and 31 with an empty one,
      which sum to 46. None of those governed files carries the path's base digest or blob id [Observed].
      The classification policy JSON is the one governed citer whose path references a runtime rule keys on
      [Inferred, from file kinds: the others are Markdown packets, raws, an openspec proposal and design, and a `.patch`].
      Its path-keyed symbols are checked in item 18.
    - The PR has no renames or deletions (item 1), so no path pin can break [Observed].
    - Locators: the lane's `locator_check.py`, re-run at `6ac21f2c`, gives the same figures and rows as `locators.json`
      (made at `ee89766a`): `locators 494`, `ambiguousSkipped 355`, `staleAtOld 337`, `shifted 23`,
      `shifted sets equal: True`, `row keys equal: True rows differing in a field: 0`. The governed-plane rows that were
      accurate at the base and are shifted number 0 out of 30 governed rows [Observed].
    - Spot-checks:
      - `main.ts:258` and `:270`, cited by `R-GP-IMPL-POC-APP-HYGIENE-1-RAW.md:213`, read
        ``const { renderDossier } = await import('@syzygy/three-surface-poc-app/dossier-render');`` at the raw's reviewed
        commit `4f3c3ebf`, exactly as at the base;
      - `brief.ts:248-250`, cited by `R-GP-IMPL-LAUNCHED-MARKER-2-RAW.md:213` at `cf3ba3fe`, is likewise equal to the
        base [Observed].
    - The 10 snapshot locators sit in `docs/pursuits/2026-09-22-vision-pursuit-{data,harvest}.json`. No tracked file under
      `scripts/`, `apps/`, `packages/` or `.github/` names those files [Observed, `git grep -l -F vision-pursuit-`].
14. **Evidence index (rules 6 and 11)** (`rev-510/tools/evidx.py`):
    - `records entries 13 match 13 mismatch 0`;
    - `scripts entries 13 match 13 mismatch 0`;
    - `files in the directory not indexed: []`;
    - `subjectFileSha256 entries 76 match at subject 76 mismatch 0` [Observed].
    - `evidence.json` names `subjectCommit` `ee89766a…` and `commitBefore` `c55acb73…`. `mutants.json` names its commit,
      its runner sha256 and each mutant's `old`/`new` fragment [Observed].
15. **Trial merge with `origin/main` `68c553b8`.**
    - #505 landed as `68c553b8`. `git merge-tree --write-tree` is clean (tree `a3205ce9`). I made a local merge commit
      `7b691f14` in `mut`, which was never pushed.
    - `npm run typecheck` reports no diagnostics, and `island-boundary.test.ts` is `passed 4` [Observed].
    - `act-families.test.ts`, from main:
      - first run: `Hook timed out in 10000ms.`;
      - re-run: 65/65 passed, as at `68c553b8` alone (65/65) [Observed].
    - `package-reader.test.ts`:
      - on the merge, alone: `'numPassedTests': 297, 'numFailedTests': 2`;
      - at `68c553b8` alone, without this PR: `'numPassedTests': 298, 'numFailedTests': 1`. The same test, "the policy
        port and the strict policy chain agree on every world in the fixture set, at every instant", ran 8300 ms [Observed].
    - So that timeout reproduces without this PR's bytes. This is load [Inferred]; see N6.
16. **Cycles** (`rev-510/tools/sccs.py`, over every in-repo edge kind): 3 strongly connected components before and the same
    3 after, of sizes 4, 7 and 2 [Observed].
    - The size-4 and size-7 components are in `three-surface-poc-core`, and the size-2 component is `design-review.ts`↔
      `review.ts`. None includes a changed module.
    - `dossier-site.ts` does not import `dossier-render.ts` [Observed].
17. **Consent census (the 8.10 corpus, GP-Q0's altered-prose differential).**
    - I ran `scripts/measure_consent_gate_recognition.mjs` as committed in `old`. The lane's
      `consent_differential.py`, comparing the lane's `consent-census-before.json` with my re-run, gives
      `"records": 15, "recordsIdentical": 15`, `"fixtureCount": 1890`, `"distinctAnswers": 9`,
      `"checkLinesIdentical": true`, `"supersededRegenerationIdentical": true`, `"wholeDocumentIdentical": true` [Observed].
      So the base census reproduces.
    - I ran the same script as committed in `new` (head `6ac21f2c`). My base run against my head run gives
      `"old": {"commit": "c55acb73…"}`, `"new": {"commit": "6ac21f2c…"}`, `"sameScript": true`, `"records": 15,
      "recordsIdentical": 15`, `"fixtureCount": 1890`, `"distinctAnswers": 9`, `"checkLinesIdentical": true`,
      `"supersededRegenerationIdentical": true` and `"wholeDocumentIdentical": true`. Per-row: 15 of 15 identical over
      1890 fixtures [Observed].
    - The lane's `consent-census-after.json` (at `ee89766a`) against my head run is likewise 15 of 15, with
      `wholeDocumentIdentical` `True` [Observed].
    - The corpus includes altered prose: `PROSE_ALTERATIONS` from `recorder-fixtures.testkit.ts`, plus every non-blank
      line appended to and deleted.
18. **Classification-policy symbols and provider sent text (classes 1 and 4).**
    `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json` classifies the instruction
    text by path and symbol:
    - `instructionTextRule.closedList`: `prompts.ts`/`promptForStage` and `provider-draft.ts`/`stageSchema`;
    - the exclusion-reason symbol: `generation-source.ts`/`GENERATION_EXCLUSION_REASONS`;
    - `runProfileRule`: `dossier-profile.ts`/`DOSSIER_READER_QUESTIONS` and `DOSSIER_REQUESTED_ASSETS`.

    At the head, each of the five symbols is still declared at the path the policy names:
    - `provider-draft.ts:44` `export function stageSchema` (it was at line 79 at the base);
    - `prompts.ts:193`, unchanged;
    - `generation-source.ts:93`;
    - `dossier-profile.ts:19` and `:31` [Observed, `git grep` at both commits].

    `scripts/derive_generator_sent_text.mjs` derives, from the compiled code, what the generator hands its `generate`
    port. That covers the system prompt and response schema of every stage, with byte counts and sha256s, and the field
    classes. Run in each tree, its outputs are byte-identical [Observed]:
    - the default output: sha256 `28c5e43e…`, 7013 bytes;
    - `--discovery` (6 pipeline stages plus 2 discovery stages): `53069a6e…`, 11555 bytes;
    - `--table` (the egress table the admission builder embeds): `9ea4557d…`, 1262 bytes.

    `scripts/build_public_source_screening_scope.py --check` prints identical output in both trees: the same pre-existing
    `FINDING policy already carries publicSourceScope` and `STALE` lines, and the same 22 exclusion reasons read from
    code. Both exit 1 [Observed]. That exit is the superseded v1 builder's own state at the base and does not come from
    this PR.

### Answer on #505

The boundary test's one exception names `consent-ports.ts`, not `package-reader.ts` (`island-boundary.test.ts:49`). Its
comment (lines 41-47) names `package-reader.ts` as one of two importers of `consent-ports.ts`.
- [Observed] Nothing in this PR's code depends on what `package-reader.ts` imports.
  - The PR changes no file in `packages/polaris-generation-consent`.
  - The consent package's compiled JS is 13 of 13 byte-identical between the base and the head.
- [Observed] At `68c553b8`, `package-reader.ts` still imports `./admission-record.js`, `./consent-ports.js`,
  `./citation-allowlist.js` and `./recorder-template.js`, with no core-root import. On the trial merge, the boundary test
  passes.
- [Inferred] Two later changes would interact with the test:
  - If a later change dropped `package-reader.ts`'s import of `consent-ports.ts`, the barrel (`index.ts:2`) would still
    reach it. The test would pass, but its "Two importers" comment would be stale.
  - If `package-reader.ts` imported the core root, the test would fail loudly (a reached root importer). It would not
    pass silently.

## 4. Findings

There are no blocking findings (no F ids).

### N1 — The CLI still loads the core island at runtime through `consent-ports.ts` (the declared residual)

- **Severity:** note, a disclosed and coordinator-ruled residual.
- **Evidence:**
  - [Observed] Item 9: at the head, the CLI's dossier branches load the 7 core island modules
    (`admitted-input`, `discovery-provider`, `discovery`, `excerpt`, `pipeline`, `provider-draft`, `rendered-design`).
    They load only via `consent-ports.js` → core `index.js`, and 0 load when `consent-ports.js` is stubbed.
  - [Observed] Item 8: `rootImporters` falls from 22 to 1, and that one is `consent-ports.ts:2`.
- **Failure scenario:** the bead's outcome, "no CLI-reachable module imports a provider-mode module", is not yet true. A
  bead closure or cycle report that says it is would overstate the result.
- **Proposed fix:** close the bead with the residual named. syzygy-bpyt.8.19, steps (a)–(e), removes the edge, including
  step (e)'s consent `./live` subpath for `screen.ts` and `gate-sources.ts`. The test's last case already fails once the
  exception stops reaching the island (mutant B7 killed).

### N2 — The boundary test sees only literal specifiers, from one entry, with one condition choice

- **Severity:** note. No escaping form occurs today.
- **Evidence:**
  - [Observed] Item 7: R1 (non-literal `import()`), R4 (a `node` condition ahead of `import`), R5 (an import in
    `broker-client.ts`) and R6 (`createRequire`) all survive.
  - [Observed] The test reads edges with `ts.preProcessFile(…).importedFiles` (`island-boundary.test.ts:91`). It takes
    `import ?? default` from an exports target (`:76`), and it has one `ENTRY` (`:16`).
  - [Observed] Item 8: over the 143 reached modules there are 0 non-literal `import()`, 0 `require` and 0 workers. All 12
    exports subpaths choose the same target under Node as under the test. `broker-client.ts` reaches only `node:net`.
  - [Observed] The PR body says: "It follows every edge: static, type-only, re-export and dynamic." The test's own comment
    is narrower and correct ("dynamic with a literal specifier").
- **Failure scenario:** a later edit adds `import(spec)` with a computed specifier, a `createRequire` call, an exports
  entry with a `node` key ahead of `import`, or an import in `broker-client.ts`. The test stays green while the CLI loads
  the island.
- **Proposed fix**, in `island-boundary.test.ts`:
  - (a) Walk the TypeScript AST rather than `preProcessFile`. Fail on any `import()` whose argument is not a string
    literal or a no-substitution template, and on any `require`/`createRequire` call in a reached module.
  - (b) Resolve exports conditions in Node's order (the first key among `node`, `import`, `default`). Or assert that
    every workspace exports target has only the `types`, `import` and `default` keys.
  - (c) Add `packages/polaris-dossier/src/broker-client.ts` as a second entry. Or derive the entries from
    `new URL('./*.js', import.meta.url)` launches in reached modules.
  - Each fix should come with a mutant (R1, R4, R5, R6 are ready in the reviewer spec). In the bead closure or the
    dispositions, state the test's reach as "literal specifiers".

### N3 — The exception unfollows a whole module, so anything `consent-ports.ts` imports is unexamined

- **Severity:** note.
- **Evidence:**
  - [Observed] Item 7: R9, a direct `import '../../polaris-generation-core/src/pipeline.js';` added to
    `consent-ports.ts`, survives.
  - [Observed] The exception is the node list `UNFOLLOWED = ['packages/polaris-generation-consent/src/consent-ports.ts']`
    (`:49`). The lapse check (B7) shows the exception still matters, but not that it hides nothing new.
- **Failure scenario:** before 8.19 lands, `consent-ports.ts` gains another import into the island, or a wider one, and
  nothing reports it.
- **Proposed fix:** make the exception an edge rather than a node. Follow `consent-ports.ts`, but allow only its current
  root import: line 2's `@syzygy/polaris-generation-core`, which carries `digestCanonicalJson` and the pipeline types.
  Alternatively, pin `consent-ports.ts`'s import list in the test until 8.19 removes it. Add R9 as the mutant.

### N4 — GP-Q0's third check, the owner notice, is not recorded

- **Severity:** note. The clause makes the notice non-blocking.
- **Evidence:**
  - [Observed] GP-Q0 lines 63-66 list three checks, the third being "a non-blocking owner notice in the cycle report".
  - [Observed] The PR body says: "The GP-Q0 extras apply. Both are in Evidence", and lists the differential and the
    mutants only.
  - [Observed] `bd show syzygy-bpyt.10 --json` (read-only) returns 0 comments and no notes field. Its description names
    the notice as part of the procedure.
- **Failure scenario:** the owner is never told that 8.1 touched classes 1, 3, 4 and 6, or about its residual (N1).
- **Proposed fix:** the coordinator adds the 8.1 notice to the cycle report (`syzygy-bpyt.10`). It should cover:
  - the classes;
  - the additive exports (`./live`, `./dossier-site`, and 6 root type names);
  - the CLI's renderer injection change (`renderLocalDossier`);
  - the `consent-ports.ts` residual and syzygy-bpyt.8.19.

### N5 — `prompts.ts`, the provider stage prompts, is in `/live` but no CLI-path module uses it

- **Severity:** note, a scope question for the coordinator or owner. The bead's island list governs.
- **Evidence:**
  - [Observed] `prompts.ts` exports `promptForStage` and the stage illustration constants.
  - [Observed] Its importers at the head are `live.ts:21`, the island modules `pipeline.ts:6` and
    `discovery-provider.ts:28`, the island's type-only `provider-draft.ts:1`, and tests.
  - [Observed] A `git grep -w` of its 9 exported names over `polaris-dossier/src`, `apps/syzygy/src`, consent `src` and
    the five app renderer modules finds 0 hits at the head. At the base, `brief.ts:5,37` used `promptForStage`.
  - [Observed] Item 9 shows `dist/prompts.js` is loaded at runtime at the head, even with `consent-ports.js` stubbed.
  - The lane lists this as a residual.
- **Failure scenario:** `/live` ships with 165 names, including provider-prompt names that no live consumer uses
  (dependency-hygiene bar 3). Removing them after merge is a class-6 endpoint removal, which needs GP-Q0's extras.
- **Proposed fix:** before this PR merges, decide whether `prompts.ts` belongs to the island. If it does, drop its
  re-export from `live.ts`; `/live` is new, so narrowing it now removes nothing anyone depends on. If not, record the
  decision in syzygy-bpyt.8.19 or the next audit's island list.

### N6 — Load-sensitive timeouts reproduce on main without this PR

- **Severity:** note, pre-existing and outside this PR.
- **Evidence:**
  - [Observed] Item 3: 2 × `Error: Test timed out in 5000ms.` in `start-gates.test.ts` at the head, at load about 17. The
    file passes alone.
  - [Observed] Item 15: at `68c553b8` alone, `package-reader.test.ts` has 1 failure, "the policy port and the strict policy
    chain agree on every world in the fixture set, at every instant", at 8300 ms. On the merge, the same test and one more
    fail (`'numFailedTests': 2`). The file's compiled consent code is byte-identical with or without this PR.
  - This confirms the brief's load reading of the lane's 3 timeouts in `package-reader.test.ts` [Inferred].
- **Failure scenario:** a battery run on a loaded host goes red in files nobody changed, and the timeouts train people to
  ignore red (test-rigor bar 6).
- **Proposed fix:** a follow-up bead for the two `package-reader.test.ts` world-sweep tests, which take 6.7–13 s under
  load: give them an explicit timeout sized to their fixture count, or reduce their per-test fixture work. Check the
  `start-gates.test.ts` init cases the same way.

## 5. Every changed output, or the evidence that there is none

- **Rendered bytes: none found.**
  - Local renders 16 of 16 (15 distinct). The XOR entry against the new local entry is 16 of 16 (15 distinct).
  - Provider renders 26 of 26 (16 distinct). Briefs 3 of 3 (3 distinct, including altered prose).
  - The provider golden passes, and its JSON is unchanged.
  - The guidance constant's version and its 4469 bytes are identical (items 2 and 10) [Observed].
- **Provider sent text and the egress table: none changed.** All three derivations are byte-identical (item 18), and every
  policy-named symbol stays at its named path [Observed].
- **Refusal strings and gate answers: none found.**
  - Validators: 62 of 62 identical, including 51 refusals.
  - Consent census: 15 of 15 records over 1890 fixtures, base against head (item 17).
  - The gate modules' compiled code is identical outside the specifier (item 10).
  - The page-sink contract string is unchanged (item 11) [Observed].
- **Exit codes and CLI behaviour.**
  - The daemon-entry pin's 15 cases pass, including `dossier render <missing>` and `dossier status <missing>` (item 2)
    [Observed].
  - The CLI now injects `renderLocalDossier` (`main.ts:260,273`). For the only production input shape
    (`render.ts:181`, `{ local, sources }`), it returns the same files as the old XOR entry (item 10) [Observed].
  - The XOR check that `renderLocalDossier` drops cannot fire on that shape [Inferred, from the call site].
- **Module load set.** The CLI's runtime load set changes from 134 to 139 in-repo files. The island stays loaded through
  `consent-ports.js` (item 9, N1) [Observed]. This is the change's purpose, not a rendered or wire output.
- **Public interface (class 6): additive only.** Item 11 lists the counts: no name is removed from any entry, and
  `./live` and `./dossier-site` are new [Observed]. No endpoint is removed, so GP-Q0's class-6 trigger does not apply.
- **Signed or digest-bound artifacts: none touched.** No `.syzygy/**` or `openspec/**` file changes. No governed digest
  citer exists for any changed file. The 13 shifted raw-review locators read the same lines at their own reviewed commits
  (item 13) [Observed].
- **Governance outputs.** `check_governance` changes only in file counts (item 4). `check_quotations` output is identical
  (item 5) [Observed].
- **Test harness and docs.**
  - The `vitest.config.ts` alias and the no-egress esbuild alias list `/live` before the root.
  - The daemon pin's `line` literal changed. C1–C4 are killed (item 6), so its ordering assertions still bite.
  - The core README gains an "Entry points" section [Observed, from the diff].

## 6. Verdict per acceptance criterion

1. "Import-boundary test lists the island and fails when a CLI-reachable module imports it (rule-6 recorded)."
   **Met, with exceptions.**
   - It lists all 20 island modules [Observed].
   - It fails for type-only, relative, literal-dynamic, `export *`, import-type and export-map edges. Mutants B1–B9, B5b,
     R2, R3, R7 and R8 are killed [Observed].
   - Rule 6 is recorded with fragments, the commit and the runner digest, and the record reproduces [Observed].
   - The exceptions are the declared `consent-ports.ts` residual (N1), the escape forms R1, R4, R5 and R6 (N2), and the
     unfollowed node's own imports, R9 (N3).
2. "Brief, render and provider goldens byte-identical." **Met** [Observed, items 2 and 10].
3. "Reachability report before/after attached." **Met.**
   - `reach-before.json` and `reach-after.json` are present and indexed [Observed, item 14].
   - My independent sweep agrees with their source-graph module counts and with the 0-island result when
     `consent-ports.ts` is not followed [Observed, items 8 and 9].

## 7. Test quality

- `island-boundary.test.ts`:
  - It asserts a reachability property against a literal island list rather than re-deriving it from the code (bar 4)
    [Observed].
  - It has failure-path cases: an unresolved specifier, and the exception lapsing with its reason (B7) [Observed].
  - Its gap, under workflow step 2's one-line-bug test, is the forms in N2 and N3. For example,
    `const s = '@syzygy/polaris-generation-core'; import(s)` in any reached module would not be caught but should be.
- `brief.test.ts` pins the guidance by a literal sha256 and version (G1 and G2 are killed).
- `page-sink.test.ts` adds an operator-agent canary (P1–P4 are killed).
- `dossier-render.test.ts` pins the XOR refusal (S3 is killed).
- The daemon pin still bites after its literal change (C1–C4 are killed) [Observed].
- S4 and S4b are equivalent mutants.
  - [Observed] `label` and `quoteNote` (`dossier-site.ts:179-181`) are read only on the `local === undefined` branch
    (`:224-225`). With `quoteFindings: null` (`:143`), the operator-agent view never builds quote flags.
  - [Inferred] Setting `quoteFindings` to `[]` therefore changes no operator-agent byte unless `checkDraftQuotes` throws,
    and from my reading it throws only on its empty-match guard.
- Growth: `Tests: +7 ~9 -0`. Each addition pins a new predicate or entry (bar 10) [Observed, `tests-delta.json`].
- Dependency hygiene:
  - The new leaf modules depend on nothing in the island. Item 8's 0-island closure of `dossier-site.ts`, and of the CLI
    with the exception unfollowed, bears this out [Observed].
  - No new import cycle appears (item 16) [Observed].
  - `/live` is broader than its CLI consumers need (N5).
- The full-suite red is load in untouched files (N6) [Inferred].

## 8. Cleanup

- [Observed] I deleted the scratch clones `rev-510/old`, `rev-510/new` and `rev-510/mut` with `rm -rf`, one command each.
  The local trial-merge commit `7b691f14` existed only in `mut`, was never pushed, and is gone with it.
- [Observed] I deleted the TMPDIRs `/tmp/r510-1` through `/tmp/r510-4`. A later `ls -d` reports
  `No such file or directory` for all four.
- [Observed] The scratch directory `rev-510/` now holds only:
  - this raw;
  - `tools/` (my sweep, probe, differential, mutant and comparison scripts, and `reviewer-mutants-spec.json`);
  - `out/` (every record quoted above);
  - the `npm ci` and build logs, and two diff copies.
- No worktree under `/home/tze/GitHub/syzygy/.worktrees/` was edited. No process was killed. All four background runs
  (the lane mutants, the reviewer mutants and the two censuses) exited 0 before cleanup.
