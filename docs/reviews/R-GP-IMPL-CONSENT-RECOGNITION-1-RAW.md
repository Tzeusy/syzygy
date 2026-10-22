# R-GP-IMPL-CONSENT-RECOGNITION-1 — CC-REV-1 implementation review of syzygy-bpyt.8.10, round 1
Verdict: REVISE
Reviewed commit: c08a015d
Subject: r1-review.diff sha256 97c05f9c0e5d8f906b9a0d3d789c3292f8b4b5e983f22c63f0c819dcc1f249e2

Reviewer: fresh-context CC-REV-1 class-4 reviewer (rev-500), 2026-10-22. PR #500, branch `agent/syzygy-bpyt.8.10`, base `26ff52ce`.
No content of any observed repository was fetched or read. Every command ran in a scratch clone at the reviewed commit, never in
a worktree under `.worktrees/`. No bd mutation, push, PR comment or merge.

Short form: the measurement of the consent readers is right, and I re-derived it by my own method. The characterization tests are
sound, and the gate is unchanged. Two things must change before merge.

- **F1.** The report states as [Observed] that "No gate decision reads a field-parsed record's prose". The PWB P1 body-read
  authority gate contradicts this for one of the six field-parsed records.
- **F2.** The proposal leaves out a recognition model that already runs in the tree. That model covers all six field-parsed
  records today with no template copies and no constants in code.

There are five notes as well.

## 1. Subject identity checks

- [Observed] `sha256sum` of the subject file:
  `97c05f9c0e5d8f906b9a0d3d789c3292f8b4b5e983f22c63f0c819dcc1f249e2  …/lead/b810/r1-review.diff`, which matches the brief.
- [Observed] I regenerated `git diff 26ff52ce… c08a015d…` in the clone by script and got
  `regenerated diff sha256 97c05f9c…49e2 bytes 173777` and `equal to subject file True`.
- [Observed] The clone's `git rev-parse HEAD` is `c08a015dae4b57b9f62b328d35924dd3eec31f1b`. `gh pr view 500` reports the
  same `headRefOid`.
- [Observed] The `git diff --stat` reports `13 files changed, 3940 insertions(+), 5 deletions(-)`. Those 13 files are 5 under
  `docs/evidence/`, 3 `*.test.ts`, `recorder-fixtures.testkit.ts`, `testing.ts` and 3 under `scripts/`. None of them is under
  `.syzygy/`, `openspec/`, `.github/` or `PROJECT-STATUS.md`.
- [Observed] `c08a015d` merges `fa0fc3ab` with `26ff52ce` (main), and `git show --cc c08a015d` prints no conflict hunks. The
  PR's own commits are `f5f5512d`, `5361fe30`, `78cd0511` and `fa0fc3ab`.
- [Observed] The evidence was measured at earlier commits: the census at `5361fe30`, the timing and mutants at `78cd0511`. Between
  `5361fe30` and `c08a015d` the subject paths change only in `launched.ts` and tests. Nothing under the consent package, the
  dossier gate sources, `decisions/`, `PROJECT-STATUS.md` or `.github/` changes. For every file both mutant records name, the
  sha256 at `c08a015d` equals the recorded value, and so does the runner's.

## 2. Clauses relied on (quoted)

- GP-Q0 review rule (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md:58-66`).
  For class-1, class-3 and class-4 PRs: "an old-versus-new differential over a mutated-record corpus that includes records with
  altered prose; a rule-6 mutant for each predicate; a non-blocking owner notice in the cycle report."
- GP-Q0 (same file, :95-96): "Any change not listed here to what a gate accepts or refuses stops and returns to the owner."
- GP-Q0 part 2, row "How the consent gate recognizes an act" (same file, :80): "**Kept as is.** The two-copy template stays,
  held by the independent oracle test. … A finding bead covers field-parsed act records whose prose has been altered".
- GP-Q0 part 1 (same file, :51-54): "'Behavior-preserving' means none of the following changes: a rendered byte, a wire format,
  a refusal string or an exit code; a signed or digest-bound artifact; a consent, security or retention decision."
- SEC-2 (`.syzygy/governance/doctrine/security.md:42-45`): "No governed-project content, or anything derived from it, is sent to
  a store or service the owner does not control — model providers included — without explicit, recorded, per-project consent."
  This is why the recognition of a statement or admission act is a consent decision.
- The bead `syzygy-bpyt.8.10` acceptance criteria: "1. Per-family table with denominators. 2. Altered-prose fixtures and
  recorded verdicts. 3. Proposal; no gate behaviour change." Its step 3 reads: "Any tightening changes what counts as an act:
  it returns to the owner as a decision bead under syzygy-bpyt.1 (GP-Q0 boundary)."
- AGENTS.md verification rules 6 ("Mutate the input and confirm the check fails, per predicate"), 9 ("A claim of absence needs a
  sweep with a denominator") and 11 ("An evidence record names its subject and the subject's digest").
- `packages/polaris-dossier/src/gate-sources.ts:549` (`RECORDS_WITHIN_REACH`): "the consent, registry, policy and statement
  records the gates read lie in Syzygy's checkout, which the agent sessions can write; Syzygy re-reads and re-checks them at
  every step, and cannot rule out that a session changed them".
- `packages/three-surface-poc-core/src/body-read-authority.ts:559`: `if (tag.value !== expected.recordingTag ||
  input.recordingTag.kind !== 'resolved') return invalid('recording-tag-mismatched', …)`.
- `apps/three-surface-poc/src/governance-inputs.ts`, comment above `resolveRecordingTag`: "A recording tag resolves only if it
  names a commit whose tree carries the act record at the recorded path". The function returns `resolved` only when
  `sameBytes(recordedBytes, currentRecordBytes)`.

## 3. What I ran and the results

| # | Run | Result (verbatim where quoted) |
|---|---|---|
| 1 | New consent tests: `vitest run --project @syzygy/polaris-generation-consent package-reader.test.ts digest-bound-act.test.ts -t syzygy-bpyt.8.10` | `Tests  11 passed \| 333 skipped (344)` |
| 2 | New dossier tests: `vitest run --project @syzygy/polaris-dossier gate-acts.test.ts -t syzygy-bpyt.8.10` | `Tests  3 passed \| 130 skipped (133)` |
| 3 | Both whole projects, consent and dossier | `Tests  1601 passed \| 1 skipped (1602)`, 34 files |
| 4 | `npm run typecheck` | clean (no diagnostics) |
| 5 | `python3 scripts/check_governance.py` | `32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted` |
| 6 | `python3 scripts/check_quotations.py` | `OK    QC-1  … 33 quotations examined in 15 of 919 .md files scanned …, 0 findings` |
| 7 | `apps/three-surface-poc/src/polaris-authority-sweep.test.ts` | `Tests  5 passed (5)` |
| 8 | Base check: test files at `26ff52ce` that contain `syzygy-bpyt.8.10` | 0 |
| 9 | My own analytic census (`tools/analytic_census.py`). It derives each field-parsed record's seen lines from the readers' code, without the lane's script | Each of the 6 records reports `matchesCensusLineLists True`; `field-parsed totals {'nonBlank': 385, 'unseenAppend': 337, 'unseenDelete': 327}` |
| 10 | The same tool on all 15 records: non-blank counts, sha256, byte-exact and pinned totals; forms re-derived from the form tables and `git ls-tree -z` | All 15 counts and digests match the census record. Byte-exact 3 of 265 and 0, pinned 0 of 250 and 0, 21 forms with 15 present: all as reported |
| 11 | Census re-run A at `c08a015d`, unpatched build, provider v2 record left out (14 records, 1759 reads) | `records compared: 14 of 15 recorded; field diffs (readTiming excluded): 0`; `families equal: True`; `probe rows equal: True`; the three superseded-version probes `exit 0 argumentMatch True control exit 1` |
| 12 | Census re-run B at `c08a015d`, built `SLOT.line` patched to `[^\S\r\n]*\S[^\r\n]*` (15 records, 1887 reads; the slowest v2 read took 1 ms) | `records compared: 15 of 15 recorded; field diffs (readTiming excluded): 0`; `families equal: True` |
| 13 | Timing on the production path: `readDigestBoundActState({ form: PROVIDER_V2_FORM })` over the real record, its last line altered (`tools/time_provider_v2_gate_read.mjs`). Run once per pattern | Original: `last-line: refused (invalid-records) in 62787 ms`. Unambiguous: `last-line: refused (invalid-records) in 0 ms`. Unaltered record read `ok` in 3–4 ms |
| 14 | My own prose alterations (not `PROSE_ALTERATIONS`) on real records, one per model (`tools/own_alterations.mjs`) | See the table below |
| 15 | Appended-text probe on the Redis observation act's `Owner:` line, which the census lists as unseen on append | `append " [altered]": ok PUBLIC-OBS-REDIS-2026-10-03`; `append " <!-- reviewer": refused: invalid-records` |
| 16 | My own rule-6 re-run (`tools/rerun_mutants_new_tests_only.py`): every mutant applied from its record's `old`/`new`, only the 14 new tests selected | `baseline @syzygy/polaris-generation-consent 11 ran 0 failed`; `baseline @syzygy/polaris-dossier 3 ran 0 failed`; `mutants 43 killed by new tests 43`. Per mutant: field 1 each, template 1 each, consent no-ops 4 each, dossier no-ops 2, 2, 2, 3, 1. This matches the report |
| 17 | The lane's `scripts/rule6_mutation_runner.py`, re-run on the dossier record used as SPEC (the workaround: one record per project) | 18 of 18 `killed`, with outcome, `failedTests` and `totalTests` identical to the record per mutant. Runner sha and test-file sha equal. The subject lists 3 of the record's 6 files (see N2) |
| 18 | Sweep for production sources that name the 15 records (`tools/record_reader_sweep.py`) | `records 15 sources 231`, then `files naming a record 3 records named 13`. The 3 files are `package-reader.ts`, `gate-sources.ts` and `apps/three-surface-poc/src/governance-inputs.ts:62,67` (v4 and v3). The other 2 records (D9, RFC7-20 reading) are named by constructed stems at `gate-sources.ts:306,315` |
| 19 | PWB owner-act parser on the real v4 record under the lane's `PROSE_ALTERATIONS` (`tools/pwb_parser_probe.mjs`) | `as committed: anchors in Effect 3/3`; `effect-widened: anchors in Effect 0/3`; the other three alterations and the Date control 3/3 |
| 20 | Recording-tag census over the 15 records (`tools/recording_tag_census.py`) | All 6 field-parsed records carry `- recording tag:` lines whose tag exists and whose blob at the tag equals the blob at `c08a015d` (`blob equal`). So do the 3 historical pinned records and 4 of the 5 byte-exact ones. The owner answers record and the sign-off have no tag line |
| 21 | `git ls-remote --tags origin` for the 6 field-parsed tags (Syzygy only) | All 6 are present on origin |
| 22 | Importers of the testing entry (`git grep` at `c08a015d` over packages, apps, scripts and `vitest.config.ts`) | Only `*.test.ts`, `testing.ts` itself, the `vitest.config.ts:8` alias and the evidence scripts (via `dist/testing.js`) import it. None of the 231 production sources does |
| 23 | Battery and CI lines naming the three new scripts (`git grep` in `PROJECT-STATUS.md` and `.github/`) | 0 |

These are the results of run 14 (one record per recognition model, read through the production readers over an in-memory copy):

| Record (model) | Effect rewritten | Revocation sentence appended | Ceremony deleted | Control: project identity changed |
|---|---|---|---|---|
| Redis observation act (field-parsed, admission) | ok | ok | ok | refused: invalid-records |
| Screening-scope v4 (field-parsed, policy chain) | ok | ok | ok | refused: invalid-records |
| D9 sitting act (byte-exact) | refused | refused | refused | refused |
| Registry sign-off (byte-exact) | refused | refused | does not apply | refused |
| Historical policy act (digest-pinned) | refused | refused | refused | refused |

I did not re-run the PROJECT-STATUS canonical battery, because the host is loaded. The PR's `commands=110 nonzero=0` is
therefore [Unknown] to me. I ran the slow `SLOT.line` read once.

## 4. Findings

### F1 — blocking, medium: false [Observed] claim that no gate decision reads a field-parsed record's prose

**Evidence.**
- The report's own text:
  - `docs/evidence/consent-gate-recognition-models-2026-10-21.md:64-70` says: "[Observed] No gate decision reads a
    field-parsed record's prose. … the one runtime consumer that re-reads the record text, `loadPublicSourceScreen` … checks
    the same head fields again … and nothing else."
  - Headline bullet 3 (:37-44) says every field-parsed record "still counts … on all six real records".
  - Residual 3 (:247-253) says "a prose edit to a field-parsed record in an operator's checkout counts at runtime".
- [Observed] Another production reader takes the v4 record. `apps/three-surface-poc/src/governance-inputs.ts:62` names
  screening-scope v4 as `PWB_ACT_RECORDS.policy`, and `:67` names v3 as the expected supersession target.
  `loadBodyReadAuthorityInputs` reads v4's text and bytes. It is called in production at `production-reobserve.ts:100-105`
  with `governanceRevision: capture.observerRevision`, so it reads the committed tree, not the working tree.
- [Observed] The PWB evaluator (`body-read-authority.ts`) reads v4's prose through `parseOwnerActRecord`:
  - the Ceremony phrase (`:551`);
  - the recording tag (`:559`);
  - the whole `## Effect` section, against three scope anchors (`:466`).
- [Observed] It also requires the record's bytes to equal its blob at the recording tag's commit (`resolveRecordingTag` /
  `sameBytes`, then `:559`). Run 20 shows v4 resolves today, with the same blob id at the tag and at `c08a015d`.
- [Observed] In run 19, `effect-widened` removes all 3 policy scope anchors from v4's Effect.
- [Inferred] The PWB gate would therefore refuse every alteration in `PROSE_ALTERATIONS`: each changes the bytes, so the tag
  check fails (`recording-tag-mismatched`). `effect-widened` would also fail `scope-wrong`. I did not run the evaluator end to
  end.
- [Observed] Residual 5 marks the PWB parser [Unknown] and "not measured". It does not say that this parser reads one of the
  six measured records, so a reader cannot connect the two.

**Failure scenario.** The owner, or bead `syzygy-bpyt.1.8`, reads the report and decides K/T1/T2 on two premises:
- that prose is read by no gate;
- that a working-tree edit to any of the six records "counts at runtime".

For v4 both premises are false. The PWB P1 gate already holds v4 byte for byte, at a committed revision. The absence claim also
had no sweep or denominator (rule 9). It is an [Observed] claim in a class-4 evidence record, and once merged it will be cited.

**Proposed fix (to the report and the PR body).**
1. Scope the :64 sentence and headline bullet 3 to the Polaris generation and dossier readers (`package-reader.ts`,
   `gate-sources.ts`, `public-source-screening.ts`).
2. Add, as a row or a paragraph, that screening-scope v4 is also read by the PWB P1 body-read authority gate
   (`governance-inputs.ts:62` → `body-read-authority.ts`). That gate reads the committed tree and requires the record to be
   byte-identical to its recording tag's blob, and it reads the Ceremony phrase and the Effect scope. Add that v3 is named
   there only as a supersession target.
3. Restate residual 3 for the consent readers only.
4. Replace residual 5's [Unknown] with that observation, or keep it [Unknown] but name v4.
5. Publish the reader sweep with its denominator. Mine is 231 production `.ts` sources, 3 naming records literally and 2 records
   named by stem, which a basename sweep cannot see.

### F2 — blocking, medium: the proposal leaves out recording-tag byte equality, a model already in the tree

**Evidence.**
- [Observed] In run 20, all 6 field-parsed records carry a `- recording tag:` line. Each tag exists locally and on origin (run
  21), and each record's blob at its tag equals its blob at `c08a015d`.
- [Observed] The PWB gate already enforces exactly this check for v4 (F1 evidence).
- [Observed] The proposal (:269-289) costs only K (keep, relying on `2.2`'s CI ledger), T1 (8 template copies) and T2 (code
  constants, with "recording an act would then require a code change").
- [Observed] Its K rationale says "the remaining exposure is residual 3, a working-tree edit between CI runs". Residual 3 itself
  is broader: an edit "counts at runtime whether or not CI ever sees it".

**Failure scenario.** The owner chooses among K, T1 and T2 without seeing a fourth arm (call it T3), which the recorders already
supply and which the PWB gate already applies to one of the same records:

- no template copies;
- no code pins;
- no change to the act ceremony.

T3 closes residual 3 at runtime for all six records today. It has its own costs [Inferred]:
- The consent readers take a filesystem port (`PackageReaderFs`), so T3 needs a git/tag port and a committed-revision read.
- A checkout without tags (a shallow CI checkout, for example) would refuse.
- Anyone who can write the checkout can move a local tag, so residual 4 stands.

None of this is stated. GP-Q0 and the bead route the choice to the owner, so the option set the owner sees should be complete.

**Proposed fix.**
1. Add a T3 row to the proposal: the record's bytes must equal its blob at its own recording tag (the PWB `resolveRecordingTag`
   pattern). Give its cost (a git port in the consent readers, tag availability, the tag-mutability caveat) and how it fits with
   8.4 and 2.2. Or state why it is excluded.
2. Restate K's remaining exposure in residual 3's own terms.
3. The coordinator should carry the same arm into `syzygy-bpyt.1.8`. This review does not touch bd.

The recommendation may stay K. It must stay labelled [Inferred], as it is now.

### N1 — note, low (availability): `SLOT.line` reachability belongs in the report and in the owner notice; a follow-up is the right route

**Evidence.**
- [Observed] Run 13: one production-path read of the altered real v2 record took 62787 ms, against 0 ms with the unambiguous
  pattern.
- [Observed] The callers: `statementsFor` (`gate-sources.ts:483-499`) reads the v1 form, whose exempt-record check renders the v2
  template, and then the v2 successor form. `statementsFor` is called from `preflight.ts:49`, `init.ts:133`, `reverify.ts:155`,
  `session-handover.ts:289` and `session-statement.ts:65`. `cli.ts:183` builds the sources the CLI uses.
- [Observed] `RECORDS_WITHIN_REACH` (§2) says agent sessions can write these records.
- [Observed] A sweep of the non-test dossier and app sources found no timeout around gate reads.
- [Inferred] One edit to the v2 record, by an agent session or by hand, makes each such command spend about 1 min per template
  evaluation, two per `statementsFor`, before it refuses. That cost grows with slot lengths and slot count, which I did not
  measure.
- [Inferred] It fails closed: nothing is admitted.
- [Observed] On whether "same language" is shown or only sampled, it is shown:
  - Proof: both patterns accept exactly the CR/LF-free strings that contain a `\S`. Split the string at its first `\S`.
  - Proof: within `templateFields` the captured groups are identical. Both patterns try the slot's end positions in the same
    descending order. The original only revisits ends it has already tried, so the first end at which the rest of the regex
    succeeds is the same, and so are the captures and backreferences.
  - The report shows the language claim only on 7 cases. Run 12 confirms it empirically: 0 field diffs over 1887 reads.

**Failure scenario.** The cycle report's owner notice or the follow-up `syzygy-bpyt.8.17` describes this as a census artifact,
not a gate-availability defect that an agent session can trigger. The owner then never weighs it.

**Proposed fix.** This does not block the merge, because the PR neither introduces nor changes this code.
- Residual 2 should state reachability: who can trigger it (any writer of the v2 record, agent sessions included) and which
  commands it stalls.
- The GP-Q0 owner notice in `syzygy-bpyt.10` should name it as a class-4 availability finding.
- `syzygy-bpyt.8.17` should cite this raw and the proof above. With the proof, the fix needs no further evidence of equal
  behaviour beyond a rule-6 mutant.

### N2 — note, low (rule 11): the "only the 14 new tests" re-run is not retained, and runner output used as SPEC loses fields

**Evidence.**
- [Observed] The report (:213-220) and the PR body both claim, as [Observed], a re-run with `-t syzygy-bpyt.8.10` in which each
  mutant fails at least one new test. Neither mutant record stores that run: they store the full-file runs, whose
  `failedTests` include existing tests.
- [Observed] Run 16 reproduces the claim: 43 of 43, with the same per-mutant counts.
- [Observed] The runner's docstring says "a previous OUT.json is a valid SPEC". OUT does not carry the per-mutant `project` (the
  lane says so) or `subjectFiles`. In run 17, my rerun's subject lists 3 files where the record lists 6, and the three test files
  are missing.

**Failure scenario.** A later reader cannot re-check the restricted claim from a stored record, and a rerun from OUT silently
narrows the subject.

**Proposed fix.**
1. Retain the restricted run as a third evidence JSON. It needs the commit, each mutant's `old`/`new`, the selector, and the
   failed new-test names per mutant.
2. Or downgrade the sentence to cite this review's run.
3. In a separate bead, make the runner write `project` and `subjectFiles` into OUT.

### N3 — note, low: "any appended text" overclaims

**Evidence.**
- [Observed] Run 15: appending ` [altered]` to an unseen-on-append line counts, while appending ` <!-- reviewer` to the same
  line refuses.
- The report (:31-33) says 337 lines "can carry any appended text".

**Failure scenario.** A reader takes the 337 as a bound on every possible edit, when it is a count under the census's one
suffix.

**Proposed fix.** Say "take the census's appended suffix (` [altered]`)", and note that the reader refuses some content
anywhere: an HTML comment opener is one case.

### N4 — note, low (rule 11): the census and timing records bind a commit, not the build they executed

**Evidence.**
- [Observed] Both scripts import `packages/*/dist`, which git ignores, and the census record's clean-tree flag comes from
  `git status`.
- [Observed] My census run B ran with a patched `dist/recorder-template.js` at a clean `c08a015d`, and its record still reports a
  clean tree.
- [Observed] The measured commits `5361fe30` and `78cd0511` are reachable only through this branch. A rebase-merge would leave
  them reachable from no ref.

**Failure scenario.** A stale or edited `dist` produces a census that its record attributes to a commit whose sources it did not
run.

**Proposed fix.**
1. Record the sha256 of each `dist` file the script imports, or have the script run `tsc -b` itself and say so.
2. Name the record bytes, which are already digested per record, as the stable anchor beside the commit.

### N5 — note, low: the three new scripts are outside the battery and CI, and the report does not say so

**Evidence.** [Observed] Run 23 found 0 battery or CI lines. The report's "How to re-run" gives the commands, but it never says
that nothing runs them. The census takes about 15 minutes, 890 s of it on the provider v2 record, on up to 11 worker threads.

**Failure scenario.** A reader assumes that CI keeps the census current. It does not, and its figures go stale as records are
added.

**Proposed fix.** Add one sentence:
- The three scripts are evidence tools, run by no battery line and no workflow.
- Their figures hold at the measured commit only.
- A re-run costs about 15 minutes until `syzygy-bpyt.8.17` lands, which makes it about 1 s per v2 read.

## 5. Every changed output (or the evidence that there is none)

- [Observed] Production bytes:
  - `git diff --stat 26ff52ce c08a015d -- packages apps ':!*.test.ts' ':!*.testkit.ts'` lists only `testing.ts`: its one export
    line gains `HEAD_FIELD_ALTERATION` and `PROSE_ALTERATIONS`.
  - `testing.ts` is imported by none of the 231 production sources (run 22), and the consent `index.ts` does not re-export it.
  - The `./testing` export in `package.json` predates this PR.
- [Inferred] The testing entry has no guard test against a production import. That gap predates this PR, and no importer exists.
- [Observed] The scripts and the evidence files are executed by nothing in the battery or CI (run 23).
- [Observed] Gate verdicts:
  - Census re-run A at `c08a015d` reproduces the recorded census, measured at `5361fe30`, field for field over 14 records and
    1759 reads, with probe rows equal (run 11). Run 12 does the same over 15 records with the unambiguous slot.
  - The consent and dossier projects pass (run 3).
- [Observed] Rendered bytes, wire formats, refusal strings, exit codes, signed or digest-bound artifacts: no file under
  `.syzygy/`, `openspec/` or `.github/` and no `PROJECT-STATUS.md` change (§1). No source a gate executes changes.
- [Observed] Test changes: the 5 deleted lines are import and export lines only (2 in `gate-acts.test.ts`, 1 each in
  `digest-bound-act.test.ts`, `package-reader.test.ts` and `testing.ts`). No existing test body changed. I count 14 new tests
  (runs 1–2, 8), which is consistent with the PR's `+14 ~0 -0`. I did not re-run `vitest list` at both commits.

The GP-Q0 old-versus-new differential has no code delta to diff. The census, re-run at the reviewed commit against the recorded
one, is the differential here, and it is empty.

## 6. Verdict per acceptance criterion

1. **Per-family table with denominators: met for the consent readers, not met as a statement about the runtime gate (F1).**
   - Every figure I re-derived matches: the 15 records and the 6/5/4 split, 21 forms with 15 present, 385/337/327, 3 of 265 and
     0, 0 of 250 and 0, and the regeneration of the CI `--check` lines and of v1–v3.
   - No record is misclassified for the reader the report names.
   - But v4 is also read at the PWB gate under a byte-equal-to-tag model that the table omits.
2. **Altered-prose fixtures and recorded verdicts: met.**
   - The 14 tests pass with literal expectations.
   - My own alterations reproduce each model's verdict on real records (run 14).
   - The `Date:` control refuses in every family that has it.
3. **Proposal, no gate behaviour change: gate unchanged, met (§5). Proposal not met as written (F2).**
   - K, T1 and T2 are presented as owner choices, and "Recommendation: K" is labelled [Inferred].
   - The costs re-derive: 8 recorders, and templates of 84, 90 and 73 lines (`sittingTemplate` 92–175, `PROVIDER_V2_TEMPLATE`
     211–300, `registrySignoffTemplate` 695–767).
   - But the option set omits the in-tree tag-equality model, and K's exposure is understated.

The bead's battery step (`Tests: +a ~b -c`) is reported in the PR body. I re-ran only the parts listed in §3, so the full
battery line is [Unknown] to me.

## 7. Test quality

- [Observed] Expectations are literal: identity strings, `{ state: 'refused', why: 'invalid-records' }` and full reader outputs.
  None is imported from the module under test.
- Each alteration is guarded with `expect(alter(text), name).not.toBe(text)`, so a no-op alteration fails. All 10 no-op
  mutants are killed by that guard or by the control.
- [Observed] Fixtures are safe at describe time:
  - `package-reader.test.ts` fills `texts` in `beforeAll`.
  - `gate-acts.test.ts` builds each `world(...)` inside `it`.
  - At describe time only literal constants and closures exist.
  - No mutant in either record errored at collection (`outcome` is `killed` for all 43, never `errored`).
- [Observed] A later tightening can change these tests deliberately:
  - The verdicts are keyed by alteration name (`EXPECTED(ok)[name]`), and each family asserts one literal.
  - T1 would flip named entries from `ok` to refused, a visible edit in one place per family.
  - A regression that loosened a byte-exact family would fail the refused literals.
  - The comment at each block says that changing a literal is an owner decision under GP-Q0.
- [Observed] Two small gaps, which need no change:
  - The provider v2 and sign-off cases have no `HEAD_FIELD_ALTERATION` control. The D9 case and the three consent families
    have one.
  - Each of those two cases asserts both an `ok` and a refused literal, so neither an always-ok regression nor an
    always-refuse regression survives. The control would only make the failure cause plainer.
- [Observed] Characterization of field-parsed policy uses the recorder-rendered version 1 fixture. Real v2–v4 are covered by
  the census and by run 14, not by a test. That is acceptable for a characterization whose subject is the reader.

## 8. Cleanup

- The scratch clone `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/rev-500/clone` had
  one untracked reviewer file before deletion (`scripts/review_census_no_v2.mjs`, the run-11 variant). Its tracked tree was
  clean after every mutant run (`git status --porcelain` showed only that file).
- I restored the patched `dist/recorder-template.js` from backup before run 13's original-pattern read. The clone is deleted
  after this file is written.
- Reviewer tools and outputs are kept for re-running, under
  `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/rev-500/tools/` and
  `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/rev-500/out/`. Each tool takes a
  repository root, so it re-runs against a fresh clone at `c08a015d`.
- No file under `/home/tze/GitHub/syzygy` or its `.worktrees/` was edited. My first run-1 attempt was a read-only vitest run
  whose cwd fell back to the main checkout: 333 skipped, nothing written to tracked files. I repeated it with `--root` set to the
  clone.
