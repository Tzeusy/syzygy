# POC main wiring: review dispositions, round 1

[Observed] This record dispositions the CC-REV-1 review of `syzygy-bpyt.5.8`
(pull request #507). That change routes `materializeRoutes` through
`PocMainDeps` in `apps/three-surface-poc/src/poc-main.ts` and refills
`main.test.ts`. It answers notes N1 and N5 of
`docs/reviews/R-GP-IMPL-POC-APP-HYGIENE-2-RAW.md`.

| Round | Raw | Verdict (line 2) | Reviewed commit (line 3) | Subject (line 4) |
|---|---|---|---|---|
| 1 | `docs/reviews/R-GP-IMPL-POC-MAIN-WIRING-1-RAW.md` | `CONFIRM WITH EXCEPTIONS` | `fe46265d` | `r1-review.diff` sha256 `fedee71fede54ca972abc2b52a53c69e0d6a9fe6abc361277563d5b2e936c861` |
| 1 (re-issue) | `docs/reviews/R-GP-IMPL-POC-MAIN-WIRING-1-REISSUE-RAW.md` | `CONFIRM WITH EXCEPTIONS` | `fe46265d` | `r1-review.diff` sha256 `fedee71fede54ca972abc2b52a53c69e0d6a9fe6abc361277563d5b2e936c861` |

The subject equals `git diff 0d4d5098 fe46265d`, which is the diff between
main and this pull request. Main had not moved when this record was written.

The same reviewer issued the second raw for the same round, over the same
bytes, after the coordinator corrected the brief's TMPDIR advice. Chrome-driven
tests need a short private TMPDIR. The first raw is unchanged, and both are
retained (CC-REV-6).

The re-issue changes no verdict, finding or figure. It adds rows 20d and 20e:
the three-surface-poc app project passes at head (`Tests  1093 passed | 2
skipped (1095)`) and at base (`1087 passed | 2 skipped (1089)`) under a short
TMPDIR. That replaces the first raw's Unknown for that project. The re-issue
also corrects the first raw's attribution of leftover Chrome directories: they
come from the passing Chrome-driven test files, not from row 20's crashes. That
gap predates this change, and the reviewer raised no finding on it.

The reviewer found "No blocking (F) findings. Five notes." (section 4).
Under the owner's notes-only stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), the round clears the exact bytes it read, and those bytes are not
edited. This record sits beside them. It is an implementation record and binds
nothing.

Revise-severity findings open: 0

## N1: four record-level defects and a tool temp-directory leak

[Observed by the reviewer] No conclusion rests on these. The evidence records
under `docs/evidence/poc-main-wiring-2026-10-22/` are bound to the reviewed
bytes and are not edited, so this record carries the corrections:

1. `verification-2026-10-22.json`'s `productionChange["poc-main.ts"]` lists 236
   changed lines, and 232 of them belong to `main.test.ts`. The production
   change is 4 lines in `poc-main.ts`
   (`git diff --numstat 5837512f e8cb47d5 -- apps packages`).
2. `differential-2026-10-22.json`'s `nonVacuity.distinctScenarioTranscripts`
   reads 42 by construction, because each transcript carries its scenario
   name. Over the transcript bodies alone there are **39 distinct outputs
   across 42 scenarios**. Three pairs are identical, each being one classified
   refusal:
   - `help` / `help-short`;
   - `repo-git-fails-no-status` / `repo-git-status-out-of-range`;
   - `model-throws-custom-error` / `model-throws-string`.
3. The harness copy in `run_differential_fixed_roots.py` makes **six**
   replacements, three of which fix the roots. The script's docstring and the
   pull request text say "three statements".
4. Of the "4 of 4" extra mutants, `state-dir-digest-input` is already killed at
   base, so 3 of the 4 are new coverage.
5. `run_differential_fixed_roots.py` leaves one `zz-differential-*` directory
   per run, and `mutate_wiring.py` has the same shape [Inferred by the
   reviewer from code]. Both are one-shot evidence tools. Anyone re-running
   them should use a private TMPDIR and delete it afterwards.

**Disposition:** corrected here. The tools are not reused, so no bead is
filed.

## N2: the route capture is a control, not a test of this seam

[Observed by the reviewer] `docs/evidence/poc-hygiene-2026-10-22/route-capture.mjs`
composes the route modules itself and never imports `poc-main.js`. So its
230/230 byte equality is a control on the route modules and on main's merged
core. It cannot observe a change to `poc-main.ts`.

This pull request's "no changed output" rests on two other pieces of evidence:
- the 42-scenario differential, which calls `main` with `REAL_DEPS`;
- the emitted-output comparison, in which 2 of 376 shipped files differ
  (`poc-main.js` and `poc-main.d.ts`), by the seam lines only.

**Disposition:** corrected here. Any future change to `poc-main.ts` alone
should drive the capture through `main()`, or leave it off its "no changed
output" list.

## N3 and N4: the wait-bound relation and a misnamed test

[Observed by the reviewer]
- N3: The relation `2 * WAIT_MS < TEST_TIMEOUT_MS` in `main.test.ts:44-48` is
  checked only by the lane's `sweep_waits.py`, which no CI step runs. The
  mutant `WAIT_MS = 40_000` survives `main.test.ts`.
- N4: The test "reads the exact requirement text" at `main.test.ts:480` reads
  no text. Its root pin is sound, though: `verbatim-reader-root` fails it at
  `:493`.

**Disposition:** filed as `syzygy-bpyt.5.10` (P3, test-only).

## N5: the altered-prose limb of GP-Q0

**Disposition:** the coordinator accepts the reviewer's reading. For this
change, GP-Q0's old-versus-new differential over a mutated-record corpus that
includes altered prose is **met vacuously**:
- The only emitted difference is 5 lines across 2 files (`poc-main.js` and
  `poc-main.d.ts`), all seam wiring that passes one function reference.
- No record is read by the changed bytes.
- Every record reader in the 42-scenario differential is a fake.

The owner notice on `syzygy-bpyt.10` says so, citing raw section 4, N5.

## Risk class

Classes 1 (the P1 repository-binding composition) and 3
(`PocRuntimeCapture`), the same ruling as #501. GP-Q0's checks:
- the differential: met, vacuously in its altered-prose limb (N5);
- a rule-6 mutant per predicate: met, with 13 of 13 recorded mutants killed at
  head and 16 of 16 of the reviewer's own (raw section 3);
- the owner notice: posted at landing.
