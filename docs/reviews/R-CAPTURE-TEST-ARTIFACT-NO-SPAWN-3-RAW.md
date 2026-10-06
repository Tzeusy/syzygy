# R-CAPTURE-TEST-ARTIFACT-NO-SPAWN-3
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 5fd41040793b8ab0e9ca394a466f6af39c3ac452
Subject: PR #383 (syzygy-4mbu)

Reviewer: fresh-context agent, 2026-10-07, round 3 (final). I read the bytes
with `git diff origin/main...5fd41040…`, `git diff 0e6b5492 5fd41040` and
`git show 5fd41040…:<path>`. I ran tests in a scratch
`git worktree add --detach` at the head, after `npm ci`. The evidence file's
five-file command gave 5 files and 111/111 passed [Observed].
`scripts/check_governance.py` in that clone reported "32 OK, 21 WARN, 0 FAIL
(53 checks)" [Observed]. `check_docs_review_campaign_partition.py --check
docs/README.md` reported "denominator=365; assigned=365 … unmatched=0;
overlaps=0; campaigns=77" [Observed]. I fetched no content of any target or
external repository. The scratch worktree has been removed. All mutants
below were applied only to that scratch tree.

## Governing references (located by `DIRECTIVE-REGISTER.md`, quoted)

- Direction `REDIS-LOCAL-AGENT-SITTING-2026-10-07` item 4
  (`.syzygy/governance/decisions/REDIS-LOCAL-AGENT-SITTING-DIRECTION.md:42-49`):
  "The test-capture tool (`npm run poc:capture-test-artifact`) is to stop
  running the observed project's tests itself: it prints the command for the
  operator to run and ingests only the result file the operator hands it."
- SEC-3 (register `DIRECTIVE-REGISTER.md:49` →
  `.syzygy/governance/doctrine/security.md:61`), "Observed code is untrusted,
  everywhere". Its binding scope was quoted in round 2 and is unchanged at
  this head.
- RFC5-18 (register :342 →
  `.syzygy/governance/contracts/rfcs/RFC-0005/execution-profiles.md:91`):
  "Absent any of these the run does not launch, and claims needing the
  evidence it would have produced render Unknown with the **primary** reason
  **`execution-blocked`** (RFC2-24 #12)".
- RFC5-19 (register :343 → same file :130): "an artifact of unverifiable
  origin caps at `report-fact` however retained, well-formed, and
  revision-bound it is. Reading is free; being believed is not."
- RFC2-25 (`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`),
  tier table row: "`report-fact` | **Observed** | "X reported Y" is Observed
  as a fact about the report; Y itself is not thereby Observed (SDR-9)".

## Round-2 finding dispositions

| R2 # | Round-2 tag | Disposition | Evidence |
|---|---|---|---|
| 1 | REVISE (AC1, AC5): `process.stdout.constructor.constructor` evasion | **Repaired; residual stated** | [Observed] `FORBIDDEN_MEMBER_NAMES` (`capture-test-artifact-main.test.ts:104-107`) holds `constructor`, `prototype`, `__proto__`, the reflection names and `Proxy`. They are refused as an identifier, a string literal or a no-substitution template (`:131-133`). Every element access with a key that is not a literal is refused (`:134-136`), and so is every computed property name that is not a literal (`:137-139`). The `indirect` regex is widened to match. Ten respelling fragments sit in the `it.each` list. Mutants M18 (the round-2 evasion verbatim) and M19 (a split `constructor` key) are each recorded with `shSentinelWritten: true` and killed by the source check. I added my own respelling, with every name written as a `\uXXXX` escape (`process.stdout.constructor`, `g.getBuiltinModule('child_process').spawnSync('sh', …)`). The AST check killed it (`reaches constructor` ×2, `names getBuiltinModule`), although every regex missed it. The residual is stated at `:18-27`: "a static guard against a determined edit cannot be complete … it does not prove no route exists." The new note 1 below is a residual of a different class. |
| N2 | NOTE: no-provenance record renders Verified | **Repaired (stronger than asked)** | [Observed] A record with no provenance now resolves to `{kind:'unknown', reason: UNMARKED_RECORD_REASON}` (`test-artifact-verification.ts:397, 478`). This happens after the commit, scope and status checks, so a defective record still names its own defect. The `verified` kind, `ObservedRunTestArtifactRecord` and `buildTestArtifactRecordFromJUnit` are removed. Trajectory has no Verified arm (`trajectory.ts:74`). Tests cover the resolver, a state-file round trip and the card. M20 is killed. |
| N3 | NOTE: consumer sweep omits the machine channel | **Repaired; residual stated** | [Observed] `CONSUMER` now matches the bare field name, so a destructuring reader is caught. `WHOLE_MODEL` matches `JSON.stringify(model)` and requires exactly `routes.ts`. The comment block states what the sweep cannot find (a computed key, `Object.values`, a spread, a serializer over another variable name). M21 (destructuring) and M22 (serializer) are killed. |
| N4 | NOTE: reason code `missing-evidence` for a reported run | **Repaired** | [Observed] The code is now `execution-blocked` (`model.ts:575`). This is RFC5-18's own required reason for "claims needing the evidence it would have produced" when the run does not launch. The docs disclose it. M23 is killed. |
| N5 | NOTE: digest of decoded text, not bytes | **Repaired** | [Observed] `readBoundedRegularFile` returns the `Buffer`. `junitDigest` hashes the bytes (`test-artifact-verification.ts:308`), and the ceiling is checked in bytes (`:339`). A test feeds bytes that are not valid UTF-8 and compares against `createHash` over the raw buffer. M24 and M25 are killed. |
| N6 | NOTE: duplicate attributes last-wins | **Repaired** | [Observed] A repeated attribute makes the tag unreadable: `if (attrs.has(name)) return null;` (`:234`), and `parseJUnitRootTotals` returns null. Four cases are tested, including a repeat in the nested suite under a wrapper that carries totals. M26 is killed. |
| (R1-8) | carried residual: barrel import | **Unchanged; see note 2** | [Observed] No action was required in round 2. Note 2 adds an aliasing gap in the guard that holds it. |

## New findings

1. **NOTE (AC1): the permitted `execFileSync` binding, reached without
   direct-call syntax, runs any command, and both guards pass it.**
   I applied the following, in scratch only, as the first line of the
   `print` branch of `capture-test-artifact-main.ts`:
   ```ts
   execFileSync.call(null, 'sh', ['-c', 'touch <scratchpad>/EVADED-R3-E1']);
   ```
   Result [Observed]: the five-file command passed 111/111, and the sentinel
   `EVADED-R3-E1` existed afterwards, so `sh` was started. Why each guard
   passes it:
   - The test "runs exactly one command, the literal git" (`:247-250`)
     matches only `execFileSync\s*\(`, so a `.call`/`.apply` call or
     `const run = execFileSync; run(…)` is invisible to it.
   - The `starters` regex deliberately excludes `execFileSync`.
   - The AST check has no rule on the binding's uses.
   - The run check's trap is only the `--python` binary. A mutant that ran
     the operator's `python` this way would be caught.
   - A mutant that runs another binary that executes observed code would
     start observed code with both guards green [Inferred]. Examples: a path
     under `repoRoot` such as its `.venv/bin/python`, or `sh -c` with a
     command that enters the repository.

   The shipped code is unaffected [Observed by reading]. Its one process is
   `execFileSync('git', ['-C', repoRoot, 'rev-parse', 'HEAD'], …)`, and the
   run check passes at the head. The residual statement at `:18-27` is true
   as written. However, it describes routes to "the global object and the
   module table", not reuse of the permitted binding, and the test name
   over-claims.

   *Repair:* add an AST rule. Every `Identifier` named `execFileSync`, other
   than the import specifier, must be the `expression` of a `CallExpression`
   whose first argument is the `StringLiteral` `'git'`. Add
   `execFileSync.call(null, 'sh', [])` and `const r = execFileSync; r('sh');`
   to the `it.each` list, and record the mutant above in the evidence file.
   This rule closes the class, because the binding is the only process
   starter the file may import.

2. **NOTE (AC1): the "calls into the core package only through the module
   the check covers" guard reads local names, so it can be bypassed by an
   alias or a namespace import.**
   `coreImports` collects `element.name.text`
   (`capture-test-artifact-main.test.ts:165`), which is the local name. As a
   result:
   - `import { someOtherExport as readBoundedRegularFile }` passes;
   - `import * as core from '@syzygy/three-surface-poc-core'` adds no names
     and passes.

   Either form reaches every barrel export. [Observed by `git grep`] The
   core modules that start processes run only the fixed binaries `git`
   (`code-structure.ts:82`, `project-shape-observation.ts:105`,
   `worker-change-observation.ts:66`) and `bd` (`materialization.ts:217`,
   `work-items.ts:52`). So this route starts no observed code, but it does
   start a process other than the stated git call.

   *Repair:* use `element.propertyName ?? element.name`, and refuse
   `NamespaceImport` and default imports from the core package.

3. **NOTE (AC4, scope): removing Verified is a fail-closed narrowing. It
   needs no owner act, but the owner should be told one 2026-08-29
   demonstration item is now unreachable.**
   - **Signed-off specification.** It has no positive obligation [Observed]:
     - `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`
       contains one verification requirement, POC-REQ-043, a
       **prohibition**: "Trajectory SHALL NOT render work-item activity,
       closure, or merge state as intent satisfaction or verification". Its
       scenario requires "not verified/Unknown" when no artifact is
       ingested.
     - `proposal.md:74-75` lists test evidence among the Known Unknowns: "The
       work-item/test-evidence/live-runtime relationships stay Unknown until
       their existing POC work lands authoritative artifacts."
     - No requirement obliges a Verified or Observed test-artifact state.
   - **Owner direction POC-DIR-2026-08-29.** It does carry a positive
     demonstration item
     (`.syzygy/governance/decisions/THREE-SURFACE-POC-MODE-DIRECTION.md:18-21`):
     "It must demonstrate … captured test evidence, verification against
     the named intent revision". That is a plain direction, not a
     digest-bound act. The same direction's invariants include "no evidence
     means Unknown". RFC5-18 and RFC5-19, quoted above, make an
     operator-reported or unlaunched run Unknown (`execution-blocked`),
     capped at `report-fact`. So this is a narrowing consistent with VIS-2,
     not a spec departure [Inferred].
   - **What the owner was told.** The sitting brief's item M
     (`contracts/candidates/REDIS-LOCAL-AGENT-SITTING-BRIEF.md`, §M) told the
     owner that print-the-command "keeps the test-artifact evidence
     obtainable". It did not say that Trajectory could then never show
     Verified. Neither does any text in this PR outside
     `docs/THREE-SURFACE-POC.md` ("When verification renders `Verified`:
     never").

   *Repair:* add one sentence to `docs/THREE-SURFACE-POC.md` and the PR body.
   It should say that the 2026-08-29 direction's "verification against the
   named intent revision" now renders Unknown (`execution-blocked`) until an
   execution profile exists. Carry the sentence into the next owner report.
   No act is needed.

4. **NOTE (honesty vocabulary, RFC2-25): the tier `report-fact` is carried
   on an Unknown-labelled element.**
   - The reported-run badge is `class="epistemic epistemic-unknown" …
     data-evidence-tier="report-fact"` (`trajectory.ts:83`). The machine
     value carries `tier: 'report-fact'` beside an Unknown subject.
   - RFC2-25 places `report-fact` inside the parent label **Observed**, as
     a fact about the report: "a tier … may only *restrict* its parent
     label's authority". It also lists "any tier rendered as a fourth label"
     as violation case 14.
   - Here two claims share one element. The report fact ("the operator
     reported N passed") is Observed/`report-fact`. The verification
     relationship is Unknown/`execution-blocked`.

   Nothing renders as Observed or Verified, so AC3 holds [Observed]. The
   encoding is fail-closed but not in the closed vocabulary's shape. This
   was introduced in round 1's repair and not raised in round 2.

   *Repair:* do one of two things:
   - render the two halves separately, as RFC2-25 does for `declared-only`
     ("Both halves must render"): an Observed/`report-fact` span for the
     report and the Unknown span for the verification;
   - or drop `data-evidence-tier` from the Unknown span and name the tier
     only in its text and disclosure.

   This is not blocking for a non-release POC.

## Mutant evidence (AC5)

[Observed] `docs/evidence/capture-test-artifact-no-spawn-mutants-2026-10-07.json`:
- `commit` is `64d4d8ab…`. `git diff --stat 64d4d8ab 5fd41040` changes only
  the evidence file, so the subject bytes are those at the reviewed head.
- It lists 26 mutants (M1–M26), each with `old`/`new` fragments, `exit`,
  `tests: 111`, the failing test names, `killed: true` and
  `shSentinelWritten`.
- I recomputed all 10 `subjectDigests` with `sha256sum` in the scratch clone
  at the head. All 10 match: `c913063d…`, `d56544de…`, `8fdd9465…`,
  `2fc5fd68…`, `119fe69c…`, `20caf506…`, `b4aa6b80…`, `6f51a195…`,
  `680f1440…`, `a66754b0…`, for the files in the record's order.

## Acceptance criteria summary

- **AC1, met.** The shipped tool starts only `git rev-parse HEAD`
  [Observed by reading; run check green]. The round-2 evasion, its split-key
  and escaped-name respellings, the prototype-chain names and non-literal
  computed keys are all rejected [Observed]. The residual is stated. Notes 1
  and 2 are further residuals of other classes.
- **AC2, met.** Every round-2 item is repaired (table).
- **AC3, met** [Observed]. No operator-reported or unmarked record reaches
  an Observed or Verified encoding:
  - the human surface has no Verified arm;
  - `/api/poc` serves `kind: 'reported'` or `kind: 'unknown'`, never
    `verified`, because that kind no longer exists in the type;
  - the Unknown subject carries `execution-blocked`.

  Note 4 concerns the vocabulary's shape only.
- **AC4, met.** There is no spec obligation for a Verified state, and the
  removal is a fail-closed narrowing (note 3).
- **AC5, met** [Observed]. Fragments, commit and digests are present; 10 of
  10 digests were recomputed and match.
- **AC6, met** [Observed]. The PR touches no file under `.syzygy/**` or
  `openspec/**`. The two prior raws were each added once and never modified.
  Their blobs (`6424fa6a…`, `686b4061…`) are identical, by
  `git hash-object`, to the retained scratch copies. `docs/README.md`
  carries the campaign row, and the partition script carries its pattern.

## Count

Round-2 findings: 6 of 6 repaired (R, N2–N6). The R1-8 residual is unchanged
and needs no action.
New findings: 4, all NOTE (1, 2, 3, 4); 0 REVISE.
