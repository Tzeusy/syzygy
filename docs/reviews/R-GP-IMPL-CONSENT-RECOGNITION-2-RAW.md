# R-GP-IMPL-CONSENT-RECOGNITION-2 — CC-REV-1 implementation review of syzygy-bpyt.8.10, round 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 09a9807a
Subject: r2-review.diff sha256 a0e75a25b612d52479c2275301dfa6557f159a0fec1fe22ca6bb18aab80f5ded

Reviewer: fresh-context CC-REV-1 class-4 (consent boundary) reviewer (rev-500b), 2026-10-22. PR #500, branch
`agent/syzygy-bpyt.8.10`, base `b7697f6a`. I did not write the change or the round-1 review.

I fetched no content of any observed repository. Git traffic went only to the Syzygy repository: a clone of the local main
checkout, then a fetch of the PR branch from `https://github.com/Tzeusy/syzygy.git`. I also read the PR body (`gh pr view 500`)
and the beads `syzygy-bpyt.8.10` and `syzygy-bpyt.2.2` (`bd show`, read-only). Every command ran in a scratch clone at the
reviewed commit. I edited nothing under `/home/tze/GitHub/syzygy` or its `.worktrees/`, and I made no bd mutation, push, PR
comment or merge. I re-ran the reader sweep without `--remote`, so I checked the recording tags locally only.

Short form. All seven round-1 findings are repaired, and I re-derived each repair's figures by a second method:
- **F1:** the claims are scoped to the consent readers, and the PWB P1 gate's reading of v4 is named and measured end to end.
- **F2:** T3 is costed beside K, T1 and T2 as an owner choice, and its tag census is right on all six records.
- **N1–N5:** each is stated as round 1 proposed.

I re-ran three of the lane's records and each reproduced:
- the PWB probe: every field except the commit, the `dist` digests included;
- the reader sweep: every field except the commit and the remote columns I did not request;
- the selected-test mutant re-run: every field except the commit and the run time, failed test names included.

The gate is unchanged. I raise two low notes, both about the wording of evidence; neither changes a verdict or a gate byte.

## 1. Subject identity checks

- [Observed] `sha256sum` of the subject files, as the brief gives them:
  - `a0e75a25b612d52479c2275301dfa6557f159a0fec1fe22ca6bb18aab80f5ded  …/lead/b810/r2-review.diff`
  - `4cfccd2536c510566394901afdf58ad5db5ed3ba3682a9d22b9a6c258234331a  …/lead/b810/r2-repair.diff`
  - `9cdd61c47eda71b160597e286132051b68cf553334d46200171b3d8ac758ea46  …/lead/b810/R-GP-IMPL-CONSENT-RECOGNITION-1-RAW.md`
  All three match the brief.
- [Observed] The diffs regenerate exactly in the clone:
  - `git diff b7697f6a… 09a9807a… --output=full.diff` hashes `a0e75a25…5ded`, equal to the subject.
  - `git diff 6a7619ff 09a9807a --output=repair.diff` hashes `4cfccd25…331a`, equal to the repair file.
- [Observed] The fetched `FETCH_HEAD` and the `headRefOid` from `gh pr view 500` are both
  `09a9807a1e075db64f76ce199aa3e3ed4e31eb12`.
- [Observed] `git diff --stat b7697f6a 09a9807a` reports `19 files changed, 6033 insertions(+), 5 deletions(-)`. The repair
  diff has `7 files changed, 2139 insertions(+), 46 deletions(-)`: the report, three records and three scripts.
- [Observed] The merge `6a7619ff` brought only main's bytes. Its parents are `c08a015d b7697f6a`, and the merge base of those two
  is `26ff52ce`.
  - Main's side: `git diff c08a015d 6a7619ff` and `git diff 26ff52ce b7697f6a` both hash
    `3f597ea074449dadce9b0fd3c0b2ea705f175325b28335a5dbdc528b3702b635`. Both list the same 10 files from PR #499; none is a
    PR-500 file.
  - The PR's side: `git diff 26ff52ce c08a015d` and `git diff b7697f6a 6a7619ff` both hash
    `97c05f9c0e5d8f906b9a0d3d789c3292f8b4b5e983f22c63f0c819dcc1f249e2`, which is round 1's subject digest. So the merge changed
    none of the PR's 13 round-1 files.
- [Observed] The three new records were measured at `9216ca29`, and `git diff --stat 9216ca29 09a9807a` lists only the report
  and those three records. So every script and every source they ran has the same bytes at the reviewed commit.

## 2. Clauses relied on (quoted)

- GP-Q0 part 2, row "How the consent gate recognizes an act"
  (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md:80`): "**Kept as is.** The two-copy
  template stays, held by the independent oracle test. Bead `8.4` never moves a byte-exact act onto field parsing, and bead
  `2.2` keeps the act-record hashes. A finding bead covers field-parsed act records whose prose has been altered".
- GP-Q0 part 3 (same file, :95-96): "Any change not listed here to what a gate accepts or refuses stops and returns to the
  owner."
- GP-Q0 part 1 (same file, :52-55), a lead line and three bullets:
  - `"Behavior-preserving" means none of the following changes:`
  - `a rendered byte, a wire format, a refusal string or an exit code;`
  - `a signed or digest-bound artifact;`
  - `a consent, security or retention decision.`
- GP-Q0 review rule (same file, :62-66). Line 62 covers "pull requests touching class 1 (authority boundaries), class 3
  (deterministic observation) or class 4 (security)". Lines 64-66 list the checks:
  - "an old-versus-new differential over a mutated-record corpus that includes records with altered prose;"
  - "a rule-6 mutant for each predicate;"
  - "a non-blocking owner notice in the cycle report."
- SEC-2 (`.syzygy/governance/doctrine/security.md:42-45`): "No governed-project content, or anything derived from it, is sent to
  a store or service the owner does not control — model providers included — without explicit, recorded, per-project consent."
  This is why recognizing an admission or statement act is a consent decision.
- The bead's acceptance criteria (`bd show syzygy-bpyt.8.10`): "1. Per-family table with denominators. 2. Altered-prose
  fixtures and recorded verdicts. 3. Proposal; no gate behaviour change." Its step 3: "Any tightening changes what counts as an
  act: it returns to the owner as a decision bead under syzygy-bpyt.1 (GP-Q0 boundary)."
- `AGENTS.md` at `09a9807a`, verification rules (:120-135):
  - 2: `No "zero / all / 100%" claim without running that exact sweep this session,`
    `confirmed by a second method. Enumerate remainders.`
  - 4: "Read a check's output, not its exit code, and check its denominator against the whole population."
  - 9: "A claim of absence needs a sweep with a denominator."
  - 10: "Freeze the bytes a review is bound to; any later edit retires the review."
  - 11: "An evidence record names its subject and the subject's digest; a record that names neither cannot be re-checked
    against the bytes it describes."
- `packages/three-surface-poc-core/src/body-read-authority.ts:559`, in two pieces:
  `if (tag.value !== expected.recordingTag || input.recordingTag.kind !== 'resolved')`
  `return invalid('recording-tag-mismatched', …)`.
- `apps/three-surface-poc/src/governance-inputs.ts:304-305`, above `resolveRecordingTag` at :306: "A recording tag resolves only
  if it names a commit whose tree carries the act record at the recorded path". At :318 it returns `resolved` only when
  `sameBytes(recordedBytes, currentRecordBytes)`.
- `packages/polaris-dossier/src/gate-sources.ts:549` (`RECORDS_WITHIN_REACH`): "the consent, registry, policy and statement
  records the gates read lie in Syzygy's checkout, which the agent sessions can write".

## 3. What I ran and the results

Setup: `git clone /home/tze/GitHub/syzygy`, then I fetched the branch, checked out `09a9807a` and ran `npm ci`. All ten
`node_modules/@syzygy/*` links resolve into the clone's own `packages/` and `apps/`. I ran
`npx tsc -b packages/polaris-generation-consent packages/polaris-dossier apps/three-surface-poc` in the clone, and it exited 0.
Every vitest run used `--root <clone>`.

| # | Run | Result (verbatim where quoted) |
|---|---|---|
| 1 | New consent tests, `vitest run --project @syzygy/polaris-generation-consent package-reader.test.ts digest-bound-act.test.ts -t syzygy-bpyt.8.10` | `Tests  11 passed \| 333 skipped (344)` |
| 2 | New dossier tests, `vitest run --project @syzygy/polaris-dossier gate-acts.test.ts -t syzygy-bpyt.8.10` | `Tests  3 passed \| 130 skipped (133)` |
| 3 | Both whole projects, consent and dossier | `Test Files  34 passed (34)`; `Tests  1609 passed \| 1 skipped (1610)`. Round 1 had 1602; the 8 more come with PR #499's `credential-probe.test.ts`, which the merge brought in |
| 4 | `npm run typecheck` | The `tsc -b …` line and nothing after it: no diagnostics |
| 5 | `python3 scripts/check_governance.py` | `32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted` |
| 6 | `python3 scripts/check_quotations.py` | `OK    QC-1  a quotation beside a path:line locator was said by that file — 33 quotations examined in 15 of 920 .md files scanned (loc-paren-quote 2, loc-colon-quote 21, quote-paren-loc 10), 0 findings` |
| 7 | `apps/three-surface-poc/src/polaris-authority-sweep.test.ts` | `Tests  5 passed (5)` |
| 8 | `apps/three-surface-poc/src/sync-child-process-guard.test.ts` (the testkit spawns `python3`) | `Tests  6 passed (6)` |
| 9 | **PWB probe**: `node scripts/probe_pwb_gate_on_altered_policy_act.mjs <clone> --out pwb-probe.json`, on the `dist` I had just built | stderr: `as committed: admits true, policy {"kind":"valid","provenance":"state-1"}` · `effect-widened: admits false, policy {"kind":"invalid","caseId":"policy:scope-wrong"}` · `limits-removed: … "policy:recording-tag-mismatched"` · `selection-replaced: … "policy:recording-tag-mismatched"` · `withdrawal-appended: … "policy:recording-tag-mismatched"` · `date-field-altered: … "policy:act-instant-malformed"`. Consent and registry are `valid` in all 6 cases |
| 10 | My field-by-field comparison of run 9 with the committed `…-pwb-gate-2026-10-22.json` (`tools/cmp_json.py`) | `DIFF $.measuredOn.commit \| 9216ca29… \| 09a9807a…` and `diffs 1`. So `measuredOn.built` is equal for all three `dist` directories (180, 73 and 13 `.js` files), and so are every result, `record.sha256`, `tagCommit` and `blobAtTagEqualsHead` |
| 11 | `git status --porcelain` in the clone after run 9 | empty |
| 12 | **Reader sweep**: `python3 -I scripts/sweep_consent_act_record_readers.py <clone> --out readers.json`, without `--remote` | `population 231 records 15 named 15 sources naming a record 3 decisions-directory sources 15`. All 13 tag rows `blob equal`; the owner answers and the sign-off have no tag line |
| 13 | Run 12 compared with the committed `…-readers-2026-10-22.json` | 15 diffs. One is `measuredOn.commit`, one is `recordingTags.remote` (`None`, because I passed no remote), and 13 are the `remoteCommit` cells my run did not request. All other fields are equal |
| 14 | My own sweep (`tools/own_sweep.py`), using `git ls-tree -r -z` and `git show` with substring tests rather than the lane's regexes | `population A (lane predicate) 231`. `A sources naming a record basename 3`: `governance-inputs.ts` (v3, v4), `gate-sources.ts` (provider v2, Redis agent statement v1) and `package-reader.ts` (11 records). `records named by basename in A 13 of 15`; `missing from basename sweep ['DOSSIER-LOCAL-AGENT-D9-IN-FORCE-ACT.md', 'DOSSIER-LOCAL-AGENT-RFC7-20-READING-IN-FORCE-ACT.md']`. `A sources containing substring "decisions" 15`, and 12 of them name no record: the same 12 the report lists |
| 15 | Second method for constructed names (`tools/construct_sweep.py`): every line in the 231 that interpolates or concatenates and mentions `.md` or `-ACT`; then every source holding a ≥12-character multi-token fragment of a record stem | `interpolating/concatenating lines naming .md or -ACT 20`. Only `gate-sources.ts:190` (`` `DOSSIER-LOCAL-AGENT-${a.stem}-ACT.md` ``) builds a census record's name. The other fragment holders (`render.ts`, `state-directory.ts`, `status.ts`, `session-handover.ts`, `content-classification.ts`) carry direction identifiers or a policy path in comments; none builds a record path |
| 16 | File types under `packages/` and `apps/` | `{'.ts': 476, '.json': 21, '.md': 2, '.mjs': 1}`. The one `.mjs` is `apps/three-surface-poc/src/test-fixtures/restart-listener.mjs`. So no production code outside `.ts` is left out |
| 17 | YAML and declarations sweep (`tools/yaml_decl_sweep.py`) | `population 17 yaml 15 under declarations/ 2`; `hits 0`. In code, the Capability 1 loader always appends `.yaml` (`consent-loading.ts:178`, `` join(root, `${reference}${CONSENT_RECORD_EXTENSION}`) ``), so it cannot open a `.md` record at all. That is stronger than the report's [Inferred] |
| 18 | Recording tags checked locally, 6 of 6 field-parsed records, with plain `git rev-parse <tag>^{commit} <tag>:<path> HEAD:<path>` | v4 `7c152bd6…`, blob `727efcd1…` at the tag and at HEAD. Redis admission `3409ef5a…`, `5943ffdd…` at both. RFC5-14 `3409ef5a…`, `eee82b88…` at both. v1 `3409ef5a…`, `82b30034…` at both. v2 `3409ef5a…`, `fc5c7188…` at both. v3 `d3a9b753…`, `9c800b26…` at both. Each tag commit equals the record's `tagCommit` |
| 19 | T3's "recorders already write the tag line": `git grep -F "recording tag:"` over the 8 recorders T1 counts | 8 of 8: `record_public_repo_admission_acts.py:356`, `record_public_egress_v2_act.py:383`, `record_public_source_screening_scope_act.py:335`, `…_v2_act.py:400`, `…_v3_act.py:370`, `…_v4_act.py:416`, `record_rfc5_project_documentation_act.py:331`, `record_public_admission_registry_entries_acts.py:342` |
| 20 | **Selected-test mutant re-run**: `python3 -I scripts/rerun_rule6_mutants_selected_tests.py <clone> --selector syzygy-bpyt.8.10 --out selected.json <both mutant records>` | `totals {'mutants': 43, 'killed': 43}`. `git status --porcelain` was empty afterwards |
| 21 | Run 20 compared with the committed `…-mutants-selected-2026-10-22.json` | `DIFF $.ranAt …`, `DIFF $.subject.commit \| 9216ca29… \| 09a9807a…` and `diffs 2`. Every mutant's `old`/`new`, outcome and failed test names are identical |
| 22 | The committed selected record (`tools/check_selected.py`) | Every one of the 43 is killed by at least one named failing test; none is killed only by "zero selected" or by a file error. Field-parsed: 20 × 1 test. Template: 13 × 1. Consent no-ops: 5 × 4. Dossier no-ops: 2, 2, 2, 3, 1. Baselines `{'selected': 11, 'failed': [], 'fileErrors': []}` and `{'selected': 3, …}`. The script sha256 in the record equals the file at HEAD. Each source record's sha256 equals its bytes at HEAD. Each `filesAsRecorded` and `testFilesAsRecorded` value is `True` |
| 23 | Who names the six evidence scripts (`tools/script_citers.py`) over all 3043 tracked files | `battery/workflow files 4 ['PROJECT-STATUS.md', '.github/workflows/generation-mutation-gate.yml', '.github/workflows/governance-docs.yml', '.github/workflows/node-ci.yml']` and `hits in those 0`. Outside the scripts themselves, the only citers are the report and each script's own record |
| 24 | Gate bytes: `git diff --stat b7697f6a 09a9807a -- packages apps .syzygy openspec .github PROJECT-STATUS.md package.json package-lock.json vitest.config.ts tsconfig.json ':!*.test.ts' ':!*.testkit.ts'` | `packages/polaris-generation-consent/src/testing.ts \| 2 +-`, `1 file changed` |
| 25 | Importers of the testing entry and the testkit at `09a9807a` (`git grep` over packages, apps, scripts, `vitest.config.ts`, `package.json`) | Only `*.test.ts`, `testing.ts` itself, the `vitest.config.ts:8` alias, a string key in `sync-child-process-guard.test.ts` and two evidence-script comments import or name them. No non-test source does |
| 26 | Code anchors the repair cites | `governance-inputs.ts:62` is `PWB_ACT_RECORDS.policy` = v4, `:67` is v3 as the supersession target, and `:306` is `resolveRecordingTag`. `production-reobserve.ts:102` is `governanceRevision: capture.observerRevision`, and that file is the only non-test caller of `loadBodyReadAuthorityInputs` (`:100`). `body-read-authority.ts:466` is `scope-wrong` over `scope.value`, `:551` is `phrase-mismatched` and `:559` is `recording-tag-mismatched`. `owner-act-record.ts:217-222` takes scope from the whole `## Effect` section; `:203-215` takes the tag from `## Ceremony` |
| 27 | Residual 2 anchors | `statementsFor` begins at `gate-sources.ts:484`, and `:352` and `:371` are as described. The five callers are at `init.ts:133`, `preflight.ts:49`, `reverify.ts:155`, `session-handover.ts:289` and `session-statement.ts:65`. `grep -i -E "timeout\|AbortSignal\|setTimeout\|Promise.race"` over those 5 files and `gate-sources.ts` matches only prompt text (`WAIT_TIMEOUT_ADVICE`), never a bound on the read |

Not run: the PROJECT-STATUS canonical battery (the host is loaded). The PR's `commands=110 nonzero=0` is therefore [Unknown] to me.
I ran no `SLOT.line` read.

## 4. Round-1 findings

- **F1 — repaired.** [Observed]
  - Every unscoped claim is now scoped. The "no prose" sentence (:88) is limited to "consent-reader" decisions. Headline bullet 3
    (:51-59) says "through the consent readers". Residual 3 (:398-401) ends "This residual is the consent readers'".
  - Bullet 4 (:60-66) and the new subsection (:135-166) name the PWB P1 reading of v4, with code anchors that hold at
    `09a9807a` (§3 run 26).
  - The end-to-end probe runs the real loader and evaluator from a `dist` that is byte-identical to my fresh build of the
    reviewed tree (runs 9–10). It alters only the in-memory blob `<HEAD>:<record>`, and the tree stayed clean (run 11).
  - The refusal reasons are the `caseId` values `evaluateBodyReadAuthority` returns. Round 1 predicted `scope-wrong` plus tag
    mismatches, and the gate's check order (scope at :466 before the tag at :559) explains why `effect-widened` reports only
    `scope-wrong`.
  - The reader sweep, with its denominator, re-derives as 231 / 3 / 2 / 12 by two methods of my own (runs 12–15).
  - Residual 5 now names v4 and keeps [Unknown] for the other two PWB records.
- **F2 — repaired.** [Observed]
  - The T3 row (:448) sits in the same table as K, T1 and T2, with "What changes", "Cost" and "Fit" columns. Its
    observed costs carry [Observed] and its predicted costs [Inferred].
  - T3 is offered as a choice ("Choose T3 if the owner wants that exposure closed at runtime", :458). The recommendation stays
    K, labelled [Inferred] (:450).
  - The tag census is right for all 6 records, by local git commands of my own (run 18). "Recorders already write the tag
    line" holds for all 8 recorders T1 counts (run 19).
  - K's exposure (:452-456) is now stated in residual 3's own terms: "whether or not it is ever committed".
  - T1, T2 and T3 "each change what counts as an act and return to the owner as a decision under `syzygy-bpyt.1`" (:465-466).
- **N1 — repaired.** [Observed] Residual 2 (:363-381) states who can trigger the stall, the five callers (verified, run 27), the
  absence of a timeout (verified), that it fails closed, and that the fix belongs to `syzygy-bpyt.8.17`. The owner notice
  belongs to `syzygy-bpyt.10`, outside these bytes.
- **N2 — repaired.** [Observed] The restricted run is retained with its commit, selector, `old`/`new` fragments and failed test
  names. It reproduces exactly at `09a9807a` (runs 20–22). The runner's `project`/`subjectFiles` gap is disclosed in the PR body's
  residuals, as round 1 proposed for a separate bead.
- **N3 — repaired.** [Observed] The report (:43-50, :240-251) now says "take the census's appended suffix" and "does not bound every
  possible append", and cites `outsideFences`/`one`. The line anchor `:73-78` covers the doc comment at 73-74 and `one` at 75-78.
- **N4 — repaired, with one exception (new N1 below).** [Observed] Residual 7 (:419-433) states that the census and timing
  records do not bind their `dist`, and names the per-record digests as the stable anchor. The new probe digests three `dist`
  directories, but its import closure reaches a fourth.
- **N5 — repaired.** [Observed] :481-489 says the six scripts are run by no battery line and no workflow. My full-tree sweep gives
  0 hits over those 4 files, with the citers enumerated (run 23).

Rule 10 check: the repair took none of its figures from round 1. Each figure comes from a script committed with its record,
and my re-runs reproduce each one. Two figures are explicitly attributed to round 1, the "about 63 s" read and "Its run 15", and
neither is restated as the lane's own measurement. I found no round-1 judgment to dispute. Round 1's runs 18 and 20 agree with
the lane's records and with my runs 12–18.

## 5. New findings

### N1 — note, low (rule 11): the PWB probe's `measuredOn.built` digests three of the four `dist` directories it loads

**Evidence.**
- [Observed] Residual 7's last bullet (:432-433) says the probe record "names a digest of each `dist` directory it loaded from
  (`measuredOn.built`)". The script's own comment (lines 12-13) is narrower: "every built file it could have loaded from the three
  `dist` directories".
- [Observed in built code] The import chain reaches a fourth directory:
  - `apps/three-surface-poc/dist/governance-inputs.js:18` imports `@syzygy/three-surface-poc-core`.
  - That package's `exports["."]` is `./dist/index.js`, whose source `index.ts:25` has `export * from './project-shape-model.js'`.
  - `packages/three-surface-poc-core/dist/project-shape-model.js:18` has
    `import { FRESHNESS_STATES, RENDERING_TIERS, UNKNOWN_REASONS, } from '@syzygy/cap1-core'`.
  - So `packages/cap1-core/dist` is loaded, and `DISTS` (script line 24) does not digest it.
- [Observed in code] No verdict depends on it. `body-read-authority.ts` imports only `act-fields.js`,
  `authority-artifact-fields.js` and `owner-act-record.js`, and `governance-inputs.ts` takes from the core index only
  `A1_CORRELATION_UNAVAILABLE`, `AUTHORITY_KINDS` and `supersessionTargetsOf`. In `three-surface-poc-core/src`, cap1-core is
  imported only by `model.ts`, `owner-act-drafter.ts`, `project-shape-model.ts`, `proposed-work.ts` and `work-items.ts`, and
  none of them is on the evaluator path.
- [Observed] For the three directories it does digest, the record matches a fresh build of the reviewed tree (run 10).

**Failure scenario.** A later reader trusts residual 7's sentence as a complete binding of the probe's executed code. A stale
`cap1-core/dist` would then go unrecorded. [Inferred] Today that cannot change a PWB verdict, but the sentence claims more than
the record holds.

**Proposed fix.** Pick one:
- In a follow-up, add `packages/cap1-core/dist` to `DISTS`, or derive the set from the loaded module graph.
- Reword residual 7's bullet to "names a digest of each of the three `dist` directories the script lists; its import closure also
  loads `packages/cap1-core/dist`, which it does not digest and which no evaluator check reads".

Either fits the dispositions record. Neither needs a re-run of the probe for this PR.

### N2 — note, low (rule 4): "production" mislabels the reader sweep's population, and `scripts/` is outside it unsaid

**Evidence.**
- [Observed] The report states the population exactly (:100-102): "every tracked `.ts` file under `packages/` and `apps/` whose
  name does not end in `.test.ts`, `.testkit.ts` or `.d.ts`: 231 sources". Three other places call those 231 "production"
  sources:
  - the PR body: "Reader sweep: of 231 production `.ts` sources";
  - the readers record's `text`: "which production sources name the census records";
  - the script's docstring, line 2: "Which production sources name the consent-gate census's act records".
- [Observed] The 231 include test support whose own headers say so:
  - `packages/polaris-generation-consent/src/testing.ts:1`: "Test support, imported by tests and testkits only."
  - `apps/three-surface-poc/src/test-walkthrough-judgment-fixture.ts:1`: "Test fixture: one lawful cold-open walkthrough pair".
  - `packages/cap1-system/src/harness.ts:1`: "RT6 — the system-test harness".
  The report itself files two of these under "test support" (:128).
- [Observed] The set is a superset of production `.ts`: the only non-`.ts` code under `packages/` and `apps/` is one `.mjs` test
  fixture (run 16). So the absence direction is conservative, and no production source is missed.
- [Observed] Outside the population, 23 tracked files under `scripts/` name a census record by file name. They are recorders and
  builders, `check_governance.py`, `check_spec_reconciliation.py`, `install_redis_sitting.py`, `simulate_redis_sitting.py`, and 3
  of this PR's evidence scripts (run 14). [Inferred] None of them is a runtime gate: they are operator and CI tools. The heading
  "Other readers of the same records" does not say that `scripts/` was not swept.

**Failure scenario.** Bead `syzygy-bpyt.8.4` or `syzygy-bpyt.1` reads "231 production sources, 3 name a record" as the whole
population of record readers. It then misses that CI checks and operator installers also read these records by name. That
matters if T3 or T1 changes the bytes those tools regenerate or compare.

**Proposed fix.** In the dispositions record:
- Call the population "non-test-named `.ts` under `packages/` and `apps/` (runtime code plus test support)".
- Add one sentence: `scripts/` was not swept; 23 tracked files there name census records, all operator or CI tooling.

Any future version of the sweep script should say "non-test-named" rather than "production". Neither the committed record nor
the report needs regenerating.

## 6. Every changed output (or the evidence that there is none)

- [Observed] Gate bytes: only `packages/polaris-generation-consent/src/testing.ts` changes among non-test sources under
  `packages/` and `apps/`. Its one export line gains `HEAD_FIELD_ALTERATION` and `PROSE_ALTERATIONS` (run 24).
  - No non-test source imports the testing entry or the testkit (run 25).
  - Nothing under `.syzygy/`, `openspec/` or `.github/` changes, nor do `PROJECT-STATUS.md`, `package.json`,
    `package-lock.json`, `vitest.config.ts` or `tsconfig.json`.
  - The 5 deleted lines in the full diff are all import or export lines: 2 in `gate-acts.test.ts`, 1 each in
    `digest-bound-act.test.ts`, `package-reader.test.ts` and `testing.ts`.
  - No source a gate executes changes. So no refusal string, exit code, rendered byte, wire format, signed or digest-bound
    artifact or consent decision changes (GP-Q0 part 1).
- [Observed] Evidence bytes do not reach any gate.
  - The PWB-REQ-014 authority sweep passes (run 7).
  - `check_governance.py` passes, with 0 FAIL (run 5).
  - The new records name the measured subject `measuredOn`, not `source`, `provenance`, `evidence` or `anchor`.
- [Observed] Where the three new scripts write:
  - **The reader sweep** writes only `OUT.json`. It runs only read-only git commands (`show`, `rev-parse`, `ls-tree`, and
    `ls-remote` when `--remote` is given).
  - **The PWB probe** writes `--out`. Its one non-read git call is `git status --porcelain --untracked-files=no` (line 73),
    issued without `--no-optional-locks`. [Inferred] That call may refresh `.git/index` stat data. It touches no tracked
    content, and the gate's own `defaultRunGit` passes that flag.
  - **The selected-test re-run** rewrites tracked sources in place and restores each with `git checkout -- <file>`. It writes
    vitest's report into a `TemporaryDirectory` and finally writes `OUT.json`. The report discloses this (:493-494: "rewrites
    sources in place, so run it in a clean clone"), and the script asserts a clean tree at start and end.
  - In my clone, `git status --porcelain` was empty after each script (runs 11 and 20).
- [Observed] Test count: the 14 new tests are the 11 + 3 that `-t syzygy-bpyt.8.10` selects (runs 1–2).
  `git grep -c "syzygy-bpyt.8.10" b7697f6a -- '*.test.ts'` finds no file. The repair diff touches no test file. That is consistent with
  `+14 ~0 -0`, though I did not run `vitest list` at both commits.
- GP-Q0 differential: there is no code delta to diff. The census (round 1 re-ran it) and the new PWB probe are the
  mutated-record corpus over the unchanged gates, and rule 6 is covered by the retained and reproduced records.

## 7. Verdict per acceptance criterion

1. **Per-family table with denominators: met.**
   - The table and the 15-record, 21-form population are unchanged since round 1, which re-derived them.
   - The scope is now explicit: the consent readers, plus the PWB P1 reading of v4, measured separately.
   - The reader sweep gives its predicate and denominator (231), which I re-derived twice. N2 is a labelling note only.
2. **Altered-prose fixtures and recorded verdicts: met.**
   - The 14 characterization tests pass.
   - The PWB gate's verdicts on the same alterations are recorded, and they reproduce exactly.
   - The `Date:` control refuses in every family, and at the PWB gate (`policy:act-instant-malformed`).
3. **Proposal; no gate behaviour change: met.**
   - The gate is unchanged (§6).
   - K, T1, T2 and T3 are costed comparably and routed to the owner under `syzygy-bpyt.1`.
   - The recommendation K is labelled [Inferred], and T3's census is right.

No finding has to change the reviewed bytes before merge or go to the owner first. Under the owner's notes-only stopping rule,
this round clears `09a9807a` (subject sha256 `a0e75a25…5ded`). N1 and N2 go to the dispositions record.

## 8. Cleanup

- I deleted the scratch clone `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/rev-500b/repo`
  after writing this file. Its tracked tree was clean after every script run, and nothing in it was edited by hand.
- Reviewer tools and outputs stay, for re-running against a fresh clone at `09a9807a`:
  - tools in `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/rev-500b/tools/`:
    `cmp_json.py`, `own_sweep.py`, `construct_sweep.py`, `yaml_decl_sweep.py`, `script_citers.py` and `check_selected.py`;
  - outputs beside them: `pwb-probe.json`, `readers.json`, `selected.json`, `full.diff`, `repair.diff`, `merge-side.diff`,
    `main-side.diff`, `pr-r1.diff` and `pr-merged.diff`.
- I edited no file under `/home/tze/GitHub/syzygy` or its `.worktrees/`. I killed no process.
