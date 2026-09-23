# Review — PWB N11 slice 2 (PR #82)
Reviewed commit: 860abd0d55f471caf5f530f23a7b01c8738d5f12
Verdict: CONFIRM

## Commission

Fresh-context independent review (CC-REV-1, CC-REV-4, CC-REV-6) of GitHub
PR #82, implementing bead syzygy-u05.11 (N11) slice 2: "Scheduled mutation
gate workflow; generation-core mutation markers + evidence record; rule-6
re-run." Worked in the detached worktree
`/home/tze/GitHub/syzygy/.worktrees/pr82-review` at
860abd0d55f471caf5f530f23a7b01c8738d5f12. `npm ci` run first. No tracked
files edited, no commits, no pushes, no merges.

Acceptance criteria: `bd show syzygy-u05.11`'s slice-2 limb ("Add a
scheduled mutation-gate workflow and extend the pwb mutation tooling to
polaris-generation-core's four files with a docs/evidence record; re-run
the rule-6 mutation"), plus AGENTS.md Verification rules 3/4/6/7 and the
mutation-related Guardrails entries (rule-6 evidence record must store
old/new fragments and the commit it ran at; a mutation that throws at
describe time scores as survived; mutation scripts rewrite sources in
place).

Diff reviewed: `git diff origin/main...HEAD` — five files, 687
insertions, 1 deletion:
- `.github/workflows/generation-mutation-gate.yml` (new)
- `apps/three-surface-poc/src/polaris-generation/generation-mutation.ts` (new)
- `apps/three-surface-poc/src/polaris-generation/generation-mutation-run-main.ts` (new)
- `docs/evidence/polaris-generation-core-mutation-run-2026-09-23.json` (new)
- `package.json` (+1 script line)

## Findings

None rise to a blocking exception. All checks below passed; details are
recorded as observations.

## Observations (not exceptions)

1. **Workflow is read-only and correctly triggered.**
   `.github/workflows/generation-mutation-gate.yml:1-63`. `permissions:
   contents: read` (line 25-26); no `git commit`/`git push`/write steps
   anywhere in the file. Triggers: `schedule: cron: '0 5 * * *'` (daily
   05:00 UTC) + `workflow_dispatch: {}` (lines 20-24). Parsed with
   `python3 -c "import yaml; yaml.safe_load(...)"` — valid YAML; the sole
   PyYAML artifact is `on:` round-tripping to the boolean key `True` under
   YAML 1.1 (`json.dumps` showed `"true": {...}`), which is the exact same
   behavior `node-ci.yml` and `governance-docs.yml` already exhibit
   (verified all three parse identically) — a well-known, harmless GitHub
   Actions YAML quirk, not a defect introduced by this PR. `node-version:
   24` matches `node-ci.yml`'s pin.

2. **Fails on survivors and restore failures, confirmed by code and by
   experiment.** `generation-mutation-run-main.ts:190`: `return survived
   === 0 && restoreFailures === 0 ? 0 : 1;`, and `process.exitCode =
   main();` (line 197) — a nonzero return fails the GitHub Actions step
   (and thus the job) without needing `process.exit()`. The workflow adds
   a second, independent confirmation step ("confirm sources restored",
   lines 51-56) that runs `git status --porcelain` and asserts it is
   empty — belt-and-suspenders on top of the runner's own digest-verified
   restore. Minor observation: that confirmation step has no `if:
   always()`, so it is skipped when the mutation-gate step itself fails;
   this loses nothing in practice because the runner's own restoration
   (verified below) and its `restored` field already gate the same exit
   code, but a reviewer wanting the git-level confirmation to run even on
   a failed gate could add `if: always()` there. Not requested by the
   bead and not a defect.

3. **Denominator is honest and the 12 mutants target real fail-closed
   predicates, not dead code or comments.** `generation-mutation.ts:41-158`
   defines exactly 12 `LiteralMutation` entries, 3 each over
   `canonical-json.ts`, `parse-json.ts`, `pipeline.ts`,
   `provider-draft.ts` — matching the bead's "four files" and the
   evidence's `summary.literalMutations: 12`. I grepped every mutation's
   `from` fragment against the live source with
   `grep -n "<fragment>" packages/polaris-generation-core/src/<file>.ts`
   and all 12 occur verbatim, each guarding a real invariant (sorted-key
   canonicalization, cycle/Proxy rejection, duplicate/pollution-key
   rejection, byte-limit precheck, call/repair-cycle budget enforcement,
   late-receipt handling, duplicate-handle/unknown-source/unknown-target
   rejection in provider drafts) — none are comments or unreachable
   branches. `applyLiteralMutation` (generation-mutation.ts:29-35) also
   self-checks that each fragment occurs exactly once before mutating,
   so no fragment is ambiguous across its file. The runner's
   `summary.planned`/`summary.literalMutations`/`summary.killed` fields
   (generation-mutation-run-main.ts:173-179) distinguish a filtered
   `--only` run from the full population, so a partial run cannot silently
   present itself as the full denominator.

4. **Evidence record matches the actual run and names the commit it ran
   at, independently reproduced.**
   `docs/evidence/polaris-generation-core-mutation-run-2026-09-23.json`
   records `commit: 5affbeee2c7e418feca7d2e1a5e6e8e4546f9f2c` — I confirmed
   `git rev-parse 5affbee` resolves to that exact 40-char hash and it is
   HEAD's immediate parent (the commit the run executed at, before the
   slice-2 commit that adds the runner and this evidence file itself —
   the only possible ordering). I independently re-derived
   `sourceDigestsBefore`/`sourceDigestsAfter` for all four subject files
   with `git show 5affbee:<path> | sha256sum` and `sha256sum <path>` in
   the current worktree; all eight digests matched the JSON exactly
   (rule 3: digests are scripted, never transcribed). Each of the 12
   `mutations[]` entries carries its exact `old`/`new` fragment
   verbatim (rule-6 guardrail requirement), `mustFail`, `observed`
   totals, `killed`, and `restored`. I then ran `npm run
   poc:generation-mutation-run` myself at the same commit: `baseline:
   76/76 passed; 12 mutations`, all 12 `killed`, `summary: 12/12 killed,
   0 survived, 0 restore failures` — identical to the committed record
   (my run wrote a same-content sibling file dated one day earlier,
   `docs/evidence/polaris-generation-core-mutation-run-2026-09-22.json`,
   under UTC-vs-local-date skew in `new Date().toISOString()`; I deleted
   it afterward, `git status --porcelain` returned clean). `python3
   scripts/check_evidence_currency.py` (the slice-1 tool) independently
   recognizes the committed record as `digest=current (8/8 in-tree
   subject digest(s) match current bytes); mutant fragments
   {'still-present': 12, 'moved-on': 0, 'subject-unresolved': 0} (of
   12)` — a third, independent confirmation.

5. **Three mutants manually re-verified outside the runner, matching the
   recorded `observed` counts exactly.** I hand-applied and hand-restored
   (via `sed`/`cp` + `git status --porcelain` clean afterward) three
   mutations directly and ran the matching test file with plain `npx
   vitest run`:
   - `canonical-json-cycle-check-disabled` (`canonical-json.ts:74`):
     1 failed — `accepts shared data but rejects cyclic data` failed with
     `expected [Function] to throw error including 'cycle' but got
     'Canonical JSON rejected: depth-limit'`. Matches recorded
     `observed: {failed: 1}`.
   - `parse-json-pollution-key-check-disabled` (`parse-json.ts:73`):
     4 failed — all four `rejects pollution keys: <key>` cases. Matches
     recorded `observed: {failed: 4}`.
   - `pipeline-max-calls-disabled` (`pipeline.ts:199`): 1 failed —
     `stops when calls or repairs are exhausted and when usage is
     unknown`. Matches recorded `observed: {failed: 1}`.
   All three restores left `git status --porcelain` clean and byte-identical
   to `HEAD` (`diff <(git show HEAD:<path>) <path>` empty).

6. **Runner restores on crash (try/finally), confirmed structurally and
   by a real I/O failure.** `generation-mutation-run-main.ts:131-136`
   wraps the mutate+test step in `try { writeFileSync(mutated); run =
   runTests(...) } finally { writeFileSync(original) }` per mutation, and
   the outer `try/finally` (117-194) unconditionally rewrites every
   loaded source's original bytes in `finally` regardless of where an
   exception is thrown inside the loop. I forced a real failure: `chmod
   444` on `canonical-json.ts`, then ran the compiled runner with `--only
   canonical-json-sorted-keys-disabled`. The mutating `writeFileSync`
   threw `EACCES` (uncaught, propagated out of `main()`, exit code 1 —
   verified via `echo $?` without piping through `tail`, since piping
   masks the real exit code); the file's content was unchanged and
   byte-identical to `HEAD` afterward (the write never landed, so there
   was nothing to restore in that particular case, but no corruption
   occurred and the job correctly fails closed). Separately, I verified
   the "describe-time throw scores as survived" guardrail: a top-level
   `throw` inserted at the head of `pipeline.ts` (simulating a
   module-load-time crash) produces `numTotalTests: 0, numFailedTests: 0`
   from vitest's JSON reporter, which the runner's `killed = run.failed >
   0 && missing.length === 0` correctly scores as **not killed**
   (survived) rather than falsely "killed" — matching the AGENTS.md
   guardrail exactly, and none of this PR's actual 12 mutations exercise
   that path (all are single-line boolean/condition literals, not
   syntax-breaking). This structure matches the established
   `pwb-mutation-run-main.ts` pattern verbatim (same restore-in-finally,
   same digest verification, same evidence shape), so it is not a novel
   risk.

7. **No collision with CG-26 or the hosted governance battery.**
   `generation-mutation-gate.yml` is a new, uniquely named workflow
   (`name: generation-mutation-gate`) not referenced by
   `governance-docs.yml` or `PROJECT-STATUS.md`'s published battery,
   and CG-26 only compares those two lists. `python3
   scripts/check_governance.py` reports `OK CG-26 published battery and
   hosted battery are one list — 36 checks examined, 0 findings — 36
   published, 36 hosted, 36 shared` — unaffected by this PR, matching the
   PR body's own stated intent ("CG-26/governance-docs.yml deliberately
   left alone... this is a separate scheduled gate, not a per-push battery
   member"). Full governance check: `32 OK, 20 WARN, 0 FAIL (52 checks)`
   — identical posture to the pre-existing baseline; none of the 20 WARNs
   concern this diff.

8. **No PWB-REQ-014 authority-sweep trip.** I ran the actual test,
   `apps/three-surface-poc/src/polaris-authority-sweep.test.ts` — 4/4
   pass, including the fourth test that greps every
   `.syzygy/governance|openspec|packages|apps|docs` file for a
   `source|authority|warrants?|primary|evidence|provenance|cites?|anchor`
   key naming the Polaris surface. I also independently re-implemented
   that exact regex pair in Python and swept the new evidence JSON
   directly — 0 hits. The JSON's top-level keys (`subject`, `date`,
   `commit`, `sourceDigestsBefore`/`sourceDigestsAfter`, `mutations[].
   {id,kind,file,description,old,new,mustFail,observed,mustFailMissing,
   killed,restored}`, `summary`) never use the bare key forms the sweep's
   key regex requires (e.g. `"sourceDigestsBefore"` does not match
   `["']?(source|...)["']?\s*[:=]`, since the regex requires the quote to
   close immediately after the bare word) — correctly following the
   AGENTS.md-documented `measuredOn`/`capture` naming lesson from the
   same guardrail family, even though this record doesn't use either of
   those specific words (it doesn't need to, since it names none of the
   trapped key forms at all).

9. **`npm test`, `npm run build:poc`, `python3 scripts/check_governance.py`
   all run clean, modulo one pre-existing, disclosed, unrelated flake.**
   `npm run build:poc` — exit 0. `python3 scripts/check_governance.py` —
   `0 FAIL` (see #7). `npm test` — 1770 passed, 2 failed, 3 skipped
   (1775 total) on the first full run:
   `apps/three-surface-poc/src/production-reobserve.test.ts` (timeout) and
   `apps/three-surface-poc/src/polaris-copy.test.ts` (timeout). Neither
   file is touched by this diff. I re-ran both files together — only
   `production-reobserve.test.ts` failed (a *different* one of its three
   timing-sensitive tests timed out that time), and `polaris-copy.test.ts`
   passed clean — consistent with CPU-contention flakiness rather than a
   real regression. I then ran `production-reobserve.test.ts` fully
   isolated: 4/4 passed. This matches the PR body's own disclosed gap
   verbatim ("npm test has one pre-existing flaky timeout in
   production-reobserve.test.ts unrelated to this change (passes 4/4
   isolated)") and the bead's own tracked follow-up (1z3.28, explicitly
   slice 4 of this same bead, not in scope for slice 2). No new flake was
   found; `polaris-copy.test.ts`'s single failure did not recur and is
   not mentioned as a known issue anywhere, so I treat it as ordinary
   load-induced timeout noise from having just run heavy mutation-testing
   CPU load beforehand, not a PR-caused defect — worth a note for whoever
   next runs the full suite under load, but not an exception here.

10. **Scope discipline matches the bead exactly.** `polaris-generation-core`
    has a fifth file with tests, `prompts.ts`/`prompts.test.ts`, which
    this mutation gate deliberately excludes — the bead text says "extend
    the pwb mutation tooling to polaris-generation-core's **four** files",
    and the four chosen are exactly the four this PR covers. Not a gap.

## Commands run

```
npm ci
git diff origin/main...HEAD --stat
git diff origin/main...HEAD -- .github/workflows/generation-mutation-gate.yml package.json
grep -n "<literal fragments>" packages/polaris-generation-core/src/{canonical-json,parse-json,pipeline,provider-draft}.ts
python3 -c "import yaml; ... yaml.safe_load(...)"  # workflow YAML validity + on:-key check against node-ci.yml/governance-docs.yml
python3 -c "... sha256 checks over docs/evidence/polaris-generation-core-mutation-run-2026-09-23.json"
git show 5affbee:packages/polaris-generation-core/src/<file>.ts | sha256sum   # x4, vs sha256sum <file> in worktree
npm run poc:generation-mutation-run                       # full independent re-run: 12/12 killed, 0 survived, 0 restore failures
rm docs/evidence/polaris-generation-core-mutation-run-2026-09-22.json && git status --porcelain
# manual mutant verification x3 (cycle-check, pollution-key, max-calls) with sed + npx vitest run + restore + git status/diff clean
# crash-path test: chmod 444 canonical-json.ts; node .../generation-mutation-run-main.js --only ...; echo $?; chmod 644; git status/diff clean
# describe-time-throw simulation: top-level `throw` in pipeline.ts; npx vitest run --reporter=json; numTotalTests/numFailedTests == 0; restore; git status clean
python3 scripts/check_evidence_currency.py   # cross-check: new record reads digest=current, 12/12 mutant fragments still-present
npx vitest run apps/three-surface-poc/src/polaris-authority-sweep.test.ts --reporter=basic   # 4/4 pass
python3 -c "... independent PWB-REQ-014 key/POLARIS_SURFACE regex sweep over the new evidence JSON"  # 0 hits
npm test                                                    # 1770 passed, 2 failed (both pre-existing/unrelated, see #9), 3 skipped
npx vitest run apps/three-surface-poc/src/polaris-copy.test.ts apps/three-surface-poc/src/production-reobserve.test.ts --reporter=basic
npx vitest run apps/three-surface-poc/src/production-reobserve.test.ts --reporter=basic   # 4/4 isolated
npm run build:poc                                           # exit 0
python3 scripts/check_governance.py                         # 32 OK, 20 WARN, 0 FAIL
git status --porcelain                                      # clean at every checkpoint above and at the end
```
