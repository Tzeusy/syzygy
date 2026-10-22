# R-GP-IMPL-DECISIONS-SWEEP-1 — CC-REV-1 implementation review of syzygy-bpyt.8.20 with 8.22, round 1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: c6875163
Subject: r1-review.diff sha256 4456fd9a451e8b549978844e8fcc92ecce1c54a3c555377a4f021b51de8492c7

Reviewer: independent fresh-context CC-REV-1 reviewer (consent gate), default model. I did not author the change and did not
change it. I did not push, comment on the PR, merge, or run any `bd` mutation (`bd show` and `bd comments` only). No observed
repository's body was fetched or read: every world below is Syzygy's own checkout with in-memory overlays. No credential file
was opened. Every suite ran under a private TMPDIR (`/tmp/r512-1` … `/tmp/r512-4`).

Verdict in one line: the memo is correct and holds no state past one file in one call, so I found no path to a stale or more
lenient consent answer; 8.22's containment proof holds for every path and every folding; the evidence reproduces. Six notes,
none blocking: the classes are 1 and 4 (N1), M5 is a surviving cost mutant rather than an equivalent one (N2), the PR head has
moved past the reviewed commit (N3), AC1's absolute bound holds only under a load condition this host seldom met (N4), the
void mutant record says nothing about being void inside itself (N5), and one memo sentence about `gate-sources.ts` imports
is loose (N6).

## 1. Subject identity checks

1. [Observed] `sha256sum` of the brief's subject file `r1-review.diff`: `4456fd9a451e8b549978844e8fcc92ecce1c54a3c555377a4f021b51de8492c7`.
   It **matches** the brief.
2. [Observed] In a fresh scratch clone checked out at `c6875163a5200ab21506054be8cb829f42b684b6`,
   `git diff 4b31531c c6875163 | sha256sum` gives the same digest, `4456fd9a…92c7`. `git diff --stat`: 14 files,
   92,049 insertions, 72 deletions. 0 of the 14 paths are under `.syzygy/` or `openspec/`.
3. [Observed] The merge base of `c6875163` with GitHub `main` is `4b31531c0f7c687bac01d15d0d54eb8bfda80f00`
   (`gh api …/compare/main...c6875163`). `main` has since moved 6 commits ahead; that is the coordinator's at landing.
4. [Observed] The code diff `68c553b8 → 7deb8dfd` and the code diff `4b31531c → c6875163`, each restricted to
   `packages/polaris-generation-consent`, `scripts/differential_consent_act_families.mjs` and
   `scripts/measure_decisions_sweep.mjs`, have the same sha256 (`26a170b2…`). So the trees the records compare (old
   `68c553b8`, new `7deb8dfd`) differ in exactly the code this PR merges.
5. [Observed] `git diff --stat 7deb8dfd c6875163` over `packages/polaris-generation-consent`, `.syzygy/governance/decisions`,
   `packages/polaris-dossier/src/gate-sources.ts` and the three record-producing scripts is empty. `git diff --stat
   68c553b8 4b31531c` over the consent package, `gate-sources.ts` and the decisions directory is empty too. The decisions
   directory holds 184 tracked files at `c6875163` (`git ls-tree -r`).
6. [Observed] After `npm ci` and `npx tsc -b packages/polaris-generation-consent packages/polaris-dossier` in fresh clones,
   the sha256 of `package-reader.ts`, `dist/package-reader.js`, `gate-sources.ts`, `dist/gate-sources.js` and
   `dist/testing.js` equals the differential record's `trees[].sha256` for both trees: new (`c6875163`, rebuilt)
   `cf6c6e51…`, `dd9e5dc3…`, `95a8ffce…`, `ae64948f…`, `57cfd748…`; old (`68c553b8`) `6efd4c4e…`, `d7679a04…`, and the same
   three others. The script's own digest equals the record's `script.sha256`, `b23cb8e3…`.
7. [Observed] The mutant record's `testFileSha256` for all six test files equals the files at `c6875163`, and its
   `fileSha256` for `package-reader.ts` (`cf6c6e51…`) equals the file at `c6875163`.
8. [Observed] CI at `c6875163`: check runs `checks` and `node`, both `completed success`
   (`gh api repos/Tzeusy/syzygy/commits/c6875163…/check-runs`).
9. [Observed] **The PR head is not the reviewed commit.** `gh pr view 512` gives head `b5513ac0`. `gh api …/compare/c6875163…b5513ac0`:
   ahead by 1, commit `b5513ac0 docs: name syzygy-bpyt.4.13 for the load timeouts; state the M5 and M22b equivalence
   [syzygy-bpyt.8.20]`, one file, `docs/evidence/decisions-sweep-memo-2026-10-22.md`. I did not review those bytes (N3).

## 2. Clauses relied on (quoted)

- **CC-REV-1** (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md`, at `c6875163`):
  - line 18: "Changes touching any of seven classes require review by an independent, fresh-context reviewer, and the agent
    performing the change never finally decides which classes it touches."
  - line 31: "1. **authority boundaries** — write-universe, typed-authority table, adapter authorization (VIS-5, VIS-6);"
  - line 37: "4. **security** — anything under SEC-1…SEC-5, auth surfaces, egress paths;"
  - line 49: "**The change record states** which classes the change touches, or "none," so a misclassification is a findable
    violation after the fact."
  - line 51: "**A reviewer or the owner** may reclassify at any time."
- **GP-Q0** (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`):
  - line 52–55: ""Behavior-preserving" means none of the following changes: … a consent, security or retention decision."
  - line 62: "**Which ones:** pull requests touching class 1 (authority boundaries), class 3 (deterministic observation) or class 4
    (security), and class-6 pull requests that remove an endpoint."
  - lines 64–66: "an old-versus-new differential over a mutated-record corpus that includes records with altered prose;" "a
    rule-6 mutant for each predicate;" "a non-blocking owner notice in the cycle report."
  - line 95: "Any change not listed here to what a gate accepts or refuses stops and returns to the owner."
- **AGENTS.md** (at `c6875163`), verification rules: 6 (line 126) "Mutate the input and confirm the check fails, per
  predicate, before trusting it"; 9 (line 132) "A claim of absence needs a sweep with a denominator."; 10 (line 133) "Freeze
  the bytes a review is bound to; any later edit retires the review."; 11 (line 134) "An evidence record names its subject
  and the subject's digest". Guardrail: "Fail-closed polarity: withdrawal defeats grant; future-dated evidence is stale; no
  evidence → Unknown."
- **Bead syzygy-bpyt.8.20**, acceptance criteria (verbatim): "1. A whole statementsFor call over the current decisions
  directory completes in a stated bound under recorded load, measured old against new with the load average beside each
  sample. 2. An old-versus-new differential over every recorded act and the PR #500 altered-prose corpus changes 0 answers,
  reported with its distinct answer vectors. 3. A rule-6 mutant per new predicate (for example, an index that skips a
  matching file) is killed. 4. Independent review raw retained; owner notice posted if the review rules class 1, 3 or 4."
  Its description: "with no change to which records are recognised".
- **Bead syzygy-bpyt.8.22**, acceptance criteria (verbatim): "1. ADMISSION_PATHS removed from the admission family's text
  needles only; its field needles are unchanged. 2. Old-versus-new differential over every decisions record and the
  altered-prose corpus: 0 answers changed, with a recorded negative-control run. 3. Rule-6 run retained. 4. Fresh-context
  class-4 review raw retained."
- **The lead's design ruling** (`bd comments syzygy-bpyt.8.20`, 2026-10-21 23:05): "D1, a per-file lazy text-forms memo …
  scoped to one findActRecords call, with no module state"; "D2 (a process-lifetime cross-sweep cache …) was rejected as a
  runtime-posture change"; "The eager-slack mutant is equivalent unless a natural NFKC throw exists. AC1 bound: every new
  sample at most 5 s at load1 <= 30, and median paired ratio at most 0.4."
- **Test-rigor bar** (`th-engineering/subskills/test-rigor/SKILL.md`): line 43 "**A test is worth keeping only if some
  plausible bug makes it fail.**"; bar 1 (line 53) "Assert behavior, not implementation"; bar 10 (line 94) "A test is worth
  *adding* only if it catches a plausible bug no existing test catches".

## 3. What I ran and the results

Clones under `scratchpad/rev-512/`: `clone` (subject `c6875163`), `old` (`68c553b8`), `mut` (subject, for in-place mutants),
`ctl2`, `ctl2b`, `ctl22` (subject with M2, M2b, M22a applied and rebuilt), `tc` (typecheck and governance). Each had its own
`npm ci`. Load average is quoted from `uptime` beside each run; the host is 12-CPU and other lanes were running throughout.

1. **Reading the memo (the heart of the review).** [Observed] `package-reader.ts:626-637`: `textForms(text)` returns three
   closures over one string, each `??=`-memoised: `plain = stemFolds(text)`, `slack = stemFolds(loose(text))`,
   `folded = fold(text)`. `findActRecords` (line 674) builds one per file, in the loop, from `await swept(rel, text)` (the same
   swept text the old code passed), and passes it to `namesAct`, which is synchronous and is called once per file. Nothing is
   held at module level: over the 989 lines of `package-reader.ts`, a Python sweep finds 0 top-level `let`/`var` and 0
   `globalThis`; of its 7 lines with `new Map`/`Set`/`WeakMap`/`WeakSet`/`WeakRef`, two are module-level constants (the
   admission `pins` at line 284 and `HISTORICAL_POLICY_ACTS` at line 363, with 0 `.set`/`.delete`/`.clear` calls on either)
   and five are locals inside functions.
   `gate-sources.ts:11` says the records are "each re-read on every call and never cached", and a case-insensitive sweep of
   that file for `cache|memo|new Map|??=` finds only that comment line.
   - **Key and invalidation.** The memo is keyed by nothing: it is one call frame's view of one string value, unreachable when
     the loop moves to the next file. There is no per-process, per-path, digest or mtime key, so there is nothing to
     invalidate.
   - **Same values, same order, same short-circuit.** Old `has(text, needle)` was `carries` or `carriesLoosely` (lines 88,
     563): `stemFolds(needle)[0]` then `stemFolds(text)`, and for a loose sweep on a miss `stemFolds(loose(needle))[0]` then
     `stemFolds(loose(text))`. `formsCarry` (631-637) computes the same values in the same order (the only reordering is that
     `loose(text)`, a shrinking regex replace, is computed after `loose(needle)` rather than before; neither can throw on a
     reachable input). `namesAct`'s name tests (no text fold), the `AGGREGATE_RECORD` exemption, the `some` over
     `[...stems, ...needles]`, and the field-line test over `forms.folded()` keep the old order and return points.
     [Inferred] So for every input the answer, the refusal string and the throw site (a `RangeError` from NFKC expansion) are
     the old ones.
   - **Added, edited, withdrawn or superseded between reads.** Within one `findActRecords` call the walk lists the directory
     and then reads each file once, before and after this change alike (the loop's only changed line is 674). The three sweeps
     of one `statementsFor` call each walk and read afresh; the memo cannot carry a value between them. A file added after a
     walk is missed by that walk on both trees (a pre-existing listing race, unchanged). [Inferred] No new path to a stale
     answer exists in the reviewed bytes.
   - **Long-lived processes.** preflight, init, reverify, session-handover, session-statement, the daemon and the polaris
     supervisor all reach the sweep through `findActRecords`; none can hold a `TextForms` across evaluations because none is
     ever returned or stored. [Observed for the reader and `gate-sources.ts`; Inferred for the entry points, which call
     those.]
   - **Does the bound skip a file?** No. [Observed] Every file that is not a form record, a pin or an exempt record still
     reaches `namesAct`; there is no name or head pre-filter (the design ruling rejected one). The withdrawal-in-name test
     (`sweep.withdrawal`) is unchanged. Fail-closed polarity is untouched.
   - **Deadlines.** [Observed] `check.ts:307-319` captures `started` before the reverify read and compares the deadline to
     `started`, so a faster sweep cannot flip a deadline refusal there. [Inferred] No gate decision I found depends on how long
     the sweep takes.
2. **8.22's containment proof, by script** (`tools/containment_822.mjs`, which extracts `fold`, `stemFolds`, `carries`,
   `ADMISSION_STEMS` and `ADMISSION_PATHS` from the built `dist/package-reader.js` rather than retyping them). [Observed]
   For each of the 4 paths, `stemFolds(path)[0]` equals the path in lower case, both stem forms are equal, and it contains
   `public-repo-admission` (2 paths) or `public-egress-v2` and `public-egress-` (2 paths): `containmentHoldsForEveryPath:
   true`. The proof is substring transitivity: the needle side is one fixed string, so if a text form contains a path's needle
   spelling it contains the stem's, for every folding of the text. A seeded fuzz over 20,000 texts (10 spellings: upper case,
   underscores, soft hyphens, zero-width spaces, en dashes, whitespace runs, fullwidth, doubled dashes, mixed; plus junk
   inserts, including NFKC-expanding U+FDFA and the `ﬁ` ligature) found 15,675 texts carrying a path and **0** carrying a path
   without a stem. The admission sweep is `loose: false` (line 285), so no loose arm is involved. [Observed] Field needles:
   the diff changes only `needles: ADMISSION_PATHS` to `needles: []`; `fields: everyField(ADMISSION_NEEDLES)` and
   `ADMISSION_NEEDLES = [...ADMISSION_STEMS, ...ADMISSION_PATHS]` (line 276) are unchanged. `ADMISSION_PATHS` and
   `ADMISSION_FAMILY` are used nowhere else in `packages/`, `apps/` or `scripts/` (one file hit).
3. **Targeted tests on the subject (`clone`).**
   - `decisions-sweep.test.ts` at load1 56.53: "Tests  19 passed (19)", exit 0.
   - `package-reader.test.ts` alone at load1 74.52 (start): "Tests  3 failed | 296 passed (299)". All 3 are "Error: Test
     timed out in 5000ms." ("egress version 2 record > is read from the recorder's act…" 6041ms; "…refuses when version 2 did
     not take effect strictly after version 1…" 5662ms; "the policy port and the strict policy chain agree > on every world…"
     8825ms). This is the pre-existing load flake tracked as `syzygy-bpyt.4.13`. Re-run alone with
     `--testTimeout=120000` at load1 31.44: "Tests  299 passed (299)", the three at 3,848, 4,717 and 7,673 ms.
   - The consent project (all 7 files) at load1 61.96: "Test Files  1 failed | 6 passed (7)", "Tests  2 failed | 501 passed
     (503)"; both "Test timed out in 5000ms." in `package-reader.test.ts` (the same flake, `syzygy-bpyt.4.13`); the 120 s
     re-run of that file above passes all 299.
4. **`npm run typecheck`** (in `tc`): `typecheck-exit=0`. **`python3 scripts/check_governance.py`**: "32 OK, 21 WARN, 0 FAIL
   (53 checks) — counts derived, not asserted", exit 0.
5. **Rule 6, reproduced** (`clone/scripts/rule6_timeout_rerun.py` over `mut` at `c6875163`, the retained record's own
   fragments, the same six test files, the per-test timeout raised to 120,000 ms so that only assertions can kill; spec
   `review-spec.json`, output `results-rule6-review.json`). Each fragment occurs exactly once in `package-reader.ts` at
   `c6875163` (`tools/mutant_fragments.py`), so the runner's first-occurrence replacement is unambiguous. [Observed]

   | Mutant | Tests | Failed | Record says | Load1 |
   |---|---|---|---|---|
   | M0 unmutated control | 489 | 0 | 0 | 31.91 |
   | M2 forms reused across files | 489 | 23 | 23 | 30.96 |
   | M4 memo removed | 489 | 1 (the cost test) | 1 | 33.64 |
   | M22a admission stem removed | 489 | 28 | 28 | 36.44 |
   | M5 slack eager | 489 | 0 | 0 at 120 s (timeout re-run) | 42.91 |
   | M2b forms keyed by name, process-wide | 489 | 116 | 116 | 41.93 |
   | R2 (mine) forms from the unswept text | 489 | 5 | — | 39.09 |
   | R0 (mine) control, my scratch non-loose cost test | 1 | 0 | — | 38.65 |
   | R5 (mine) M5's fragment, my scratch non-loose cost test | 1 | 1 | — | 38.28 |

   R2 replaces `textForms(await swept(rel, text))` with `textForms(text)`; its 5 failures are the tooling-citation tests
   (for example "every stem counts wherever it sits, save exact tooling citations in an allowlisted file (R-361-1) …"). R0 and
   R5 use `tools/zz-review-cost.test.ts`, an uncommitted copy of the committed cost test aimed at the admission sweep (not
   loose) with a bound of two folds per file. [Observed] Its count over 6 files: **12** on the subject, **18** under M5, **60**
   on the old tree `68c553b8` (run directly with the count printed). See N2.
6. **Differential sample, reproduced** (`results-diff-sample.json`; kinds `base`, `base-reduced`, `edited-between-reads`,
   `policy-bytes`, `real-file`, `named`; old `68c553b8` against new `c6875163`, 4 workers, 12:30:52–12:49:46, load1 35.81 at
   the start and 36.67 at the end).
   [Observed] "655 worlds, 4919 answers compared, 0 mismatches, 229 distinct answer vectors, 154 distinct label vectors",
   exit 0. `tools/compare_rows.py` keys each world by (kind, base, subject, operator): 655 of 655 found in the record, 0 keys
   duplicated in the record, and **655 of 655** worlds have the record's answer vector and label vector exactly. The `--count`
   run over the whole corpus reproduces the record: 4,643 worlds, the same counts per kind, corpus digest
   `1d5d50dbc270cff3fab1cd0e23fb41b612a2adfb9288da173b7f11459315834a`, 67 needles.
7. **The record's own figures** (by `jq`, never read whole). [Observed] `totals`: 4,643 worlds, 36,515 answers, 0 mismatches,
   1,648 distinct answer vectors, 256 distinct label vectors; `mismatches` length 0; 0 rows with `same != true`. The 46 named
   alterations start with the imported PR #500 five (`effect-widened`, `limits-removed`, `selection-replaced`,
   `withdrawal-appended`, `date-field-altered`), from `dist/testing.js` of the new tree. Over the `named` worlds the four prose
   alterations each apply to 10 records and the date alteration to 15. `policy-chain@2026-10-08T09:30:00Z` answers `ok` in 1
   world (the V2 policy bytes from `3409ef5a`), so N6 of the PR #505 review is addressed.
8. **What the `edited-between-reads` worlds mutate.** [Observed] In the script (worker handler), a world with `steps` is read
   once per step: each step builds a fresh overlay file system and calls every reader again, in the same worker, whose loaded
   modules persist across steps and worlds. So the bytes change **between whole reader calls inside one long-lived process**,
   not between the three sweeps of one `statementsFor` call or between a walk and its reads. That is the right probe for the
   staleness a memo could cause (a value outliving a call); within-call edits would show the subject and the old tree reading
   the same bytes, since neither holds anything across reads. The record's labels show the named step changing the answers
   of the readers that sweep for its needle (a refusal, or a provider statement marked `withdrawn`; for example
   `step2:registry-git-source`: "10x ok … | 1x refused: …/ZZ-PROBE.md names the act without being its record"), and every
   step-3 reader giving one label in all 11 worlds, the same as its step-1 label.
9. **Negative controls, reproduced and extended.**
   - M2 (8.20): `results-control-m2.json`, `--kinds edited-between-reads,base-reduced`. [Observed] "15 worlds, 697 answers
     compared, 570 mismatches", corpus digest `29d79193…7d11` and mutated-tree digests `86664158…`/`e386855c…`, each equal to
     the retained record's, and the set of 570 mismatches (kind, subject, operator, reader, old and new answer digests)
     **identical** to the record's.
   - M2b (mine; the cross-call reuse D2 would bring): `results-control-m2b.json`, `--kinds edited-between-reads`. [Observed]
     "11 worlds, 561 answers compared, 20 mismatches", all at step 2, and 19 of the 20 are lenient: old refused or threw,
     the mutant answered `ok` (for example `step2:in-force-egress`: old "refused: invalid-records", new "ok
     PUBLIC-EGRESS-anthropic"). So the differential does see a memo that serves a stale, more lenient consent answer.
   - M22a (8.22): [Observed] `ctl22`'s `package-reader.ts` and `.js` digests (`ed3ede47…`, `bcdb0c02…`) equal the retained
     control's mutated-tree digests, so that record ran on M22a exactly. Its 152 mismatches lie in 76 worlds over 6 needle
     subjects, all containing `public-repo-admission`, in the `admission` and `in-force-egress` readers only.
     I did not complete a re-run of it (item 11).
10. **Timing, reproduced** (`results-timing.json`; `measure_decisions_sweep.mjs --rounds 4`, old `68c553b8` against new
    `c6875163`, recorded `dist` digests `d7679a04…`/`dd9e5dc3…`). [Observed] "old 12342-18938 ms, new 3922-5578 ms, median
    ratio 0.305, load1 34.11-37.48, bound holds: false"; paired ratios 0.272, 0.278, 0.332, 0.405; `answersAgree: true`. Two of
    four new samples exceeded 5,000 ms (5,578 and 5,149 ms), at load1 36.02 and 35.26. See N4.
11. **M22a negative control re-run: started, stopped, no result.** I started the same control over the `probe` kind
    (1,541 worlds, 4 workers) at 12:51:36 (load1 37.50). At 13:06:36 load1 was 83.16 and the run had reached
    "250/1541 worlds, 906 s", so it would have held four workers on the shared host for about another 80 minutes. I stopped
    it; it wrote no record and I count nothing from it. 8.22's control rests on item 9 (the retained record's mutated-tree
    digests checked against `ctl22`) and on M22a's rule-6 kill (item 5).

## 4. Findings

No blocking finding (no F). Six notes.

### N1 — Classes 1 and 4, not 4 alone (note)
- Severity: note (classification; no evidence is owed).
- Evidence: the memo (lines 7–8) and the PR body claim "CC-REV-1 class 4 (availability of the consent gate)". The changed
  `namesAct` / `findActRecords` (`package-reader.ts:639-679`) is the sweep of `readDigestBoundActState` (line 736) and
  `readVersionedSignoffState` (line 873). `gate-sources.ts:510-514` reads the latter for `registryEntry`, which decides
  whether the source-acquisition adapter is authorized: CC-REV-1 class 1, "adapter authorization (VIS-5, VIS-6)". This is the
  same ruling as N1 of `docs/reviews/R-GP-IMPL-ACT-FAMILIES-1-RAW.md`, which the coordinator accepted
  (`docs/evidence/consent-act-families-round-1-dispositions-2026-10-22.md`, "## N1: classes 1 and 4, not 4 alone"). Class 4
  holds for SEC-2 consent and egress. Not class 3 (no snapshot composition or evaluation identity), not class 6 (nothing
  exported changes: `TextForms`, `textForms` and `formsCarry` are module-private, `index.ts` is unchanged).
- Failure scenario: the owner notice and the landing record name class 4 only, so a later audit of class-1 changes misses
  this PR.
- Fix: the PR body and the owner notice on `syzygy-bpyt.10` say "classes 1 and 4". GP-Q0 line 62 sets the same three checks
  for both, so nothing further is owed. Do not edit the memo for this: record the reclassification in the dispositions.

### N2 — M5 is a surviving cost mutant, not an equivalent one (note)
- Severity: note (a test gap on a cost property; no answer can change).
- Evidence: M5 makes the slack spelling eager (`slack … = stemFolds(loose(text))` at construction). It changes no answer
  (section 3 item 5: 0 of 489 fail at 120 s), and I agree it moves a throw site only on inputs no natural file reaches.
  But 8.20 exists to cut cost, and the change's own doc comment (`package-reader.ts:619`) promises that each spelling is
  "computed on its first use". M5 breaks that promise and adds a whole-text fold to every file of every sweep that is not
  loose (the admission, policy and class sweeps, `loose: false` at lines 285, 382, 471): [Observed] 12 → 18 folds over 6
  files (+50 %) on the admission sweep, against 60 on the old tree. The committed cost test reads only a loose sweep, so it
  allows M5 (3 per file either way). M4 is treated, rightly, as a mutant "only a cost test can kill" (memo); M5 is the same kind
  of mutant, and an equally cheap deterministic test kills it: R5, my scratch extension, fails under M5 ("expected 18 to be
  less than or equal to 12") and passes on the subject (R0). The record and the memo's "equivalent" therefore misdescribe
  M5. The "killed" outcome in the reference record was a 5 s timeout, and its single-sample durations under shifting load
  (my run: M0 6,915 ms at 31.91, M5 10,290 ms at 42.91) cannot settle the cost question either way. The memo discloses the
  gap ("M5's cost on the sweeps that are not loose has no test", line 471) and the lead's ruling chose not to build a test.
- Failure scenario: a later "simplify" refactor computes all three spellings up front; the admission, policy and class reads
  on preflight, init and reverify pay one more whole-text NFKC fold per decisions file, silently; no test fails and no
  answer changes.
- Fix: in the dispositions, record M5 as "survived: cost-only, accepted by the lead's ruling", not "equivalent". File a
  follow-up bead to extend the cost contract to one non-loose sweep: the admission read over the cost test's six files,
  folds ≤ 2 per file (the body of `tools/zz-review-cost.test.ts` beside this raw is a working draft). AC1 is not affected:
  `statementsFor` runs only loose sweeps.

### N3 — The PR head has moved past the reviewed commit (note)
- Severity: note for landing (rule 10).
- Evidence: section 1 item 9. Head `b5513ac0` adds one commit after `c6875163` that edits
  `docs/evidence/decisions-sweep-memo-2026-10-22.md` ("name syzygy-bpyt.4.13 for the load timeouts; state the M5 and M22b
  equivalence"). This raw binds `c6875163` (subject digest above) and says nothing about those bytes. It touches the M5
  wording that N2 is about.
- Failure scenario: the PR merges at `b5513ac0` with this raw cited as its review, and the merged memo carries text no
  reviewer read.
- Fix: land the reviewed bytes, or have the coordinator dispose of `b5513ac0`'s memo edit explicitly (a reviewed delta, or a
  dispositions entry naming it as an unreviewed evidence-prose edit). If it restates M5 as equivalent, align it with N2's
  disposition.

### N4 — AC1's absolute bound holds only under a load condition this host seldom met (note)
- Severity: note (honesty of the claim; the criterion is met as written).
- Evidence: the bound was set before measurement (lead, 2026-10-21 23:05): every new sample ≤ 5 s at load1 ≤ 30, median
  ratio ≤ 0.4. The record of reference holds it at load1 25.27–27.39 (new ≤ 3,048 ms, median 0.253). The retained high-load run
  (35.68–50.36) does not: one new sample at 5,254 ms. My reproduction just above the condition (34.11–37.48) does not either:
  two of four new samples over 5 s (5,578 and 5,149 ms), median ratio 0.305 (one pair at 0.405). During this review load1
  ranged about 31–75 (the `uptime` lines in my logs). The median ratio held in all three runs (0.253, 0.207, 0.305); the
  absolute figure held only in the run under the condition.
- What it means: [Inferred] the 5 s figure is a property of a lightly loaded host, not a guarantee; on this host at load1
  34–50 a whole `statementsFor` call took 2.4–5.6 s on the new tree against 12.3–23.0 s on the old (the high-load record and
  mine together). The bead says these calls run "with no timeout", so exceeding 5 s costs latency, never a refusal or a
  grant.
- Failure scenario: the owner notice quotes "at most 3,048 ms" and a reader takes it as the operating figure.
- Fix: the owner notice states the ratio first (about 0.2–0.3 in every run) and the absolute figure with its condition, and
  cites both timing records.

### N5 — The void mutant record does not say it is void (note)
- Severity: low.
- Evidence: `docs/evidence/decisions-sweep-mutants-void-high-load-2026-10-22.json` has the keys `mutants, project, ranAt,
  runner, runnerPath, runnerSha256, subject` and no void or control field (0 occurrences of `"void`); it records M5, M22b and
  M22c as `killed`. Only its filename and the memo (line 231, "marked by its name") say the run is void.
- Failure scenario: a reader who opens the JSON alone, or a tool that globs `decisions-sweep-mutants-*.json`, takes M5, M22b
  and M22c as killed.
- Fix: do not edit the generated record. Make sure every index that lists it (the memo already does) says "void"; a later
  runner could write a `void`/`reason` field when a run has no passing control.

### N6 — One memo sentence about `gate-sources.ts` imports is loose (note)
- Severity: low (wording; the digests it supports are exact).
- Evidence: memo line 29: "`gate-sources.ts` imports only the consent package and a type." [Observed] Its imports are the
  consent package (line 1), `node:fs/promises` `readdir` (line 7), `node:path` (line 8) and a type from `./governed.js`
  (line 9). The point it supports, that its compiled file's digest is the whole of the dossier code the differential runs
  over, stands (section 1 item 6).
- Fix: none needed for this PR; say "only the consent package, Node built-ins and a type" if the memo is touched again.

## 5. Every changed output, or the evidence that there is none

- **Consent, security and retention decisions:** none. [Observed] 0 mismatches over 36,515 answers in the record; my
  reproduction of 655 worlds (4,919 answers) gives the record's answer and label vectors in 655 of 655. [Inferred, from section
  3 items 1 and 2] none on any input: the memo computes the same pure values in the same order with the same short-circuits,
  and 8.22 removes needles a stem already implies.
- **Refusal strings and exit codes:** none. The one refusal string in `findActRecords` is on an unchanged line; the diff
  touches no CLI, exit path or renderer.
- **Rendered bytes and wire formats:** none. No renderer, route or schema file is in the diff.
- **Signed or digest-bound artifacts:** none. 0 of 14 changed paths are under `.syzygy/` or `openspec/`; `check_governance`
  reports 0 FAIL. The PR #505 record `docs/evidence/consent-act-family-differential-2026-10-22.json` is not in the diff and has
  no commit in `68c553b8..c6875163`.
- **Exported interface:** none. The three new symbols are module-private; `index.ts` is unchanged.
- **What does change** [Observed unless marked]: time (section 3 item 10); the count of `String.prototype.normalize` calls on
  swept texts (loose sweeps 19 → ≤ 3 per file; admission 10 → 2 per file); [Inferred] peak memory inside one `namesAct` call,
  which now keeps up to five text-sized strings alive at once where the old code let each fold go. On a pathological file
  near V8's string limit that could exhaust the heap where the old code did not; that is a process crash, which grants nothing
  (fail-closed), and no decisions file is anywhere near that size.
- **GP-Q0 line 95:** [Inferred] no answer this change could alter is a change to what a gate accepts or refuses, so nothing
  here falls outside GP-Q0 Part 1's behaviour-preserving refactors, and nothing returns to the owner.

## 6. Verdict per acceptance criterion

### syzygy-bpyt.8.20
1. **Met, under its stated condition** (N4). The record holds the lead's pre-set bound at load1 ≤ 30 with the load beside every
   sample, old against new, in fresh processes; the high-load run is retained and honestly marked `holds: false`. My
   reproduction at 34–37 shows the ratio holding and the absolute figure not.
2. **Met.** 0 of 36,515 answers differ over 4,643 worlds, including the PR #500 altered-prose corpus imported from the built
   `testing.js`, with 1,648 answer vectors and 256 label vectors reported. Corpus digest, tree digests and a 655-world sample
   reproduced exactly; the M2 negative control reproduced exactly; my M2b control shows the corpus sees a stale-lenient memo.
3. **Met, with N2.** The scope predicates (M2, M2b), the loose arm (M1, M6), the plain arm (M7), the field fold (M3) and the
   memo (M4) are killed; I reproduced M0, M2, M2b and M4 (and M5 surviving). M5 survives as a cost mutant and should be
   recorded as such.
4. **Discharged by this raw** once retained. The owner notice is still owed, naming classes 1 and 4 (N1).

### syzygy-bpyt.8.22
1. **Met.** The diff changes `needles: ADMISSION_PATHS` to `needles: []` and nothing else in the family; the field needles are
   `everyField(ADMISSION_NEEDLES)` as before.
2. **Met.** The same differential compares a tree that tests the paths in text with one that does not, over all 184
   decisions files with a needle appended and the four paths in 92 probe and 12 real-file worlds: 0 differ. The containment
   proof (section 3 item 2) shows why. The negative control (M22a) is retained and its mutated-tree digests check out.
   [Inferred] The shared differential could in principle hide two changes that cancel; here 8.20 cannot add or remove a
   refusal at all (item 1), so it cannot cancel 8.22.
3. **Met.** M22a is killed (28, reproduced). M22b is the change undone and is genuinely equivalent: 8.22 is behaviour-neutral by
   a proof, and 8.22 is not a cost change. M22c (field paths dropped) is genuinely equivalent by the same containment on field
   values (the field test is `carries` too, since the sweep is not loose), and it is outside 8.22's scope because criterion 1
   requires the field needles unchanged.
4. **Discharged by this raw** once retained.

### The coordinator's three conditions
1. **The PR #505 (8.4) evidence record is not edited:** met (section 5).
2. **8.22's criteria and evidence stated separately from 8.20's:** met. The PR body and the memo have a section per bead; each
   bead has its own negative-control record (`bead: syzygy-bpyt.8.22` for M22a); the shared differential is attributed to both
   with each bead's coverage stated.
3. **Class 4 with GP-Q0's extras:** the extras are present (differential with altered prose, a mutant per predicate; the owner
   notice is the coordinator's). I rule the classes **1 and 4** (N1); GP-Q0 asks the same extras of both.

## 7. Test quality

- **What the 19 new tests catch.** [Observed] `decisions-sweep.test.ts` (19 tests; the file lists `+19 ~0 -0` truthfully: it is
  the only test file in the diff, and the run reports 19).
  - The three "walked after" tests and the "edited between two reads" test assert literal verdicts and reasons (bar 4) and
    kill the scope mutants: M2 fails all four, and M2b fails the edited-between-reads test (and, through its by-name reuse of
    `NOTES.md`, all 12 path-spelling tests). They are the regression tests a memo needs.
  - The cost test is a deterministic count, not a timing (bar 6), and is the only test that kills M4 (114 against ≤ 18). It
    pins an implementation count, which bar 1 normally warns against; here cost is the contract, the test says so in its
    comment, and it counts whole-text folds only, so a refactor that keeps the fold count passes. Two gaps: it covers only a
    loose sweep (N2), and its bound is ≤ 3 × 6 over all six files rather than ≤ 3 per file, so a mutant that folds one file
    eight times and the rest twice would pass. Neither affects an answer.
  - The 12 path-spelling tests and their negative world pin 8.22's premise per path and per spelling. They pass on both trees.
    [Observed] M22a fails 6 of them (the two `public-repo-admission` paths, three spellings each) and 22 tests that predate
    this PR; the six `public-egress-v2` tests survive M22a because those paths still contain `public-egress-v2` and
    `public-egress-`, and would fail only if both stems went. So the 12 add little kill power over the existing suite
    (bar 10); they earn their place as the documentation of the containment the change rests on, and they are cheap. No
    finding.
- **Missing pins.** No test exercises a file whose bytes change *within* one call; none is needed, because the reader holds
  nothing across reads before or after (section 3 item 8). The throw-site claim is untested; no natural input reaches it.
- **Suite trustworthiness.** The pre-existing 5 s timeouts in `package-reader.test.ts` under load (3 tests in my run alone at
  load ~55–74, 2 in the project run; all pass at 120 s) are `syzygy-bpyt.4.13`. They make a default-timeout rule-6 run on
  this host unreliable, which is why the lane's first mutant run is void and why I ran mine at 120 s.
- **Rule 6 and rule 11 of the evidence.** [Observed] Every record names its subject commit and file digests; the mutant
  record carries each mutant's `old` and `new` fragments, the command and the runner's digest; the negative controls name the
  mutant in `controlNote` and the mutated tree's compiled digests with `clean: false`; the timing records carry both trees'
  compiled digests and the script's. The recorded commands omit the reporter flags (the PR #505 review's N8, already filed).

## 8. Cleanup

- Kept beside this raw, in `scratchpad/rev-512/`: `tools/` (`containment_822.mjs`, `mutant_fragments.py`, `apply_mutant.py`,
  `make_review_spec.py`, `compare_rows.py`, `zz-review-cost.test.ts`), `review-spec.json`, the results
  (`results-containment-822.txt`, `results-rule6-review.json`, `results-diff-sample.json`, `results-control-m2.json`,
  `results-control-m2b.json`, `results-timing.json`) and the run logs (`run-*.log`, `build.log`, `npm-ci.log`;
  `run-control-m22a.log` is the stopped run of section 3 item 11).
- Deleted after the last run: the clones `clone`, `old`, `mut`, `ctl2`, `ctl2b`, `ctl22` and `tc`, and the TMPDIRs
  `/tmp/r512-1` to `/tmp/r512-4`. Nothing outside those was deleted. The scratch cost test was never placed in any tracked
  tree other than these clones, and `git status --porcelain --untracked-files=no` was empty in `mut` and `old` after every
  mutant run.
