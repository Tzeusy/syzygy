# R-GP-IMPL-OWNER-ACT-FIELDS-1 — CC-REV-1 implementation review of syzygy-bpyt.6.2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: ecb68fce
Subject: review.diff sha256 1033b4f6b47ac0d5f4a23619e97ce18a0e5f362c8d3959da72c6e4a6c12bbdf0

Reviewer: independent fresh-context CC-REV-1 reviewer (default model). I did
not author the change and did not share the authoring session's context. I
read no observed repository body (Butlers or any other), made no network
fetch, and edited nothing in the worktree. Every mutant, probe and harness
ran in scratch clones I created under
`/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/lead/b62/reviewer/`.

The exceptions are five notes. None is blocking. Each is stated under
"Findings" with evidence, a failure scenario and a proposed fix.

## 1. Subject identity checks

- [Observed] `sha256sum` of the frozen subject
  `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/lead/b62/review.diff`
  is `1033b4f6b47ac0d5f4a23619e97ce18a0e5f362c8d3959da72c6e4a6c12bbdf0`.
  This matches the digest in the brief.
- [Observed] I regenerated the diff with
  `git diff fdc866afc4430a63074d52e13418ae319c9aa0a6 ecb68fcea81a264a19bc798c9f2bed0d250b9168 --output=<reviewer>/regen.diff`.
  It hashes to the same `1033b4f6…bbdf0`, so the frozen subject is exactly the
  base-to-head diff.
- [Observed] In the worktree, `git rev-parse HEAD fdc866af origin/main` gives
  `ecb68fce…`, `fdc866af…` and `fdc866af…`. The base is origin/main.
- [Observed] The branch has three commits:
  - `88c79070`: the code change;
  - `027fd501`: re-points three PWB literal mutations at a renamed test;
  - `ecb68fce`: adds evidence only.
- [Observed] `git diff --name-status fdc866af ecb68fce` lists 11 paths:
  - 6 modified: `apps/three-surface-poc/src/pwb-mutation.ts`,
    `body-read-authority.ts`, `body-read-authority.test.ts`,
    `walkthrough-judgment.ts` and `walkthrough-judgment.test.ts`;
  - 1 added module: `packages/three-surface-poc-core/src/act-fields.ts`;
  - 5 added evidence files under `docs/evidence/`.
- [Observed] Nothing under `.syzygy/**` or `openspec/**` changed. No evidence
  file was modified or deleted: all five `docs/evidence/` entries are status
  `A`.
- [Observed] I read the bead with `bd show syzygy-bpyt.6.2`, read-only. Its
  acceptance criteria 1–5 are the ones the brief restates.

## 2. Clauses relied on

- **CC-REV-1** (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md`):
  - line 16: "## CC-REV-1 — Mandatory independent review classes";
  - lines 31–32: "1. **authority boundaries** — write-universe, typed-authority table, adapter authorization (VIS-5, VIS-6);";
  - line 37: "4. **security** — anything under SEC-1…SEC-5, auth surfaces, egress paths;";
  - line 40: "6. **public interface** — machine-queryable endpoints, adapter contracts, anything an external consumer can depend on;";
  - lines 45–46: "Class membership is contested by default and is never finally determined by the agent performing the change".
- **VIS-4** (`.syzygy/governance/doctrine/vision.md:168-170`): "Humans steer the
  vision; agents shape within it. Shape-defining changes always need the
  owner's sign-off; Syzygy and its agents may draft them, never adopt them."
  The change's comment reads it as "an AI principal never stands in for the
  owner" (`act-fields.ts:10-11`). That is a reasonable reading of the
  owner-act gates. The doctrine sentence itself does not define principal
  shapes.
- **SEC-2** (`.syzygy/governance/doctrine/security.md:42-45`): "No
  governed-project content … is sent to a store or service the owner does not
  control … without explicit, recorded, per-project consent." The body-read
  gate is the consent precondition for reading Butlers content, so a change
  to it is a consent decision under class 4.
- **PWB-REQ-005**
  (`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`):
  - line 636: "Consent and policy authority precede every body read";
  - lines 652–653: "Specification sign-off, tree attribution, a Git commit or tag, a machine submission or an agent assertion SHALL NOT substitute for any act.";
  - line 678: "Owner attribution has four independent cases: missing, malformed, another human and a non-human principal."
- **PWB-REQ-022** (same file):
  - line 2472: "Absent or unlawful owner judgment never becomes success";
  - line 2520: "Apply PWB-REQ-005's exact 55-case common population to the judgment act, including separate another-human/non-human owner cases".
- **CAP1-REQ-011 as amended**
  (`openspec/changes/cap1-trusted-bootstrap-consent/specs/project-registration-and-honest-shape-visibility/spec.md`):
  - line 7: "… or known non-human act state SHALL refuse the dependent observation";
  - line 43: "the diagnostic distinguishes missing owner-act evidence from recognized non-human evidence".
- **CAP1-REQ-046** (same file, line 92): the consent decision's "human fact
  set and machine answer SHALL expose … the precise refusal reason with
  authorization Unknown".
- **RFC3** (`.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md:319-320`):
  "Missing, digest-mismatched, … unattributed or non-human act state blocks
  the dependent effect".
- **The owner's directions:**
  - `OWNER-DIRECTION-GREENFIELD-PARITY-SIMPLIFICATION-2026-10-20.md:45-48`:
    "'Behavior-preserving' means that none of the following changes: a
    rendered byte, a wire format, a refusal string or an exit code; … a
    consent, security or retention decision."
  - `OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md:62-66` (GP-Q0
    Part 1): class 1, 3 or 4 pull requests get "an old-versus-new
    differential over a mutated-record corpus that includes records with
    altered prose; a rule-6 mutant for each predicate; a non-blocking owner
    notice in the cycle report."
  - Same file, line 67: `6.2` is among the beads "known to touch a class".
  - Same file, line 88 (Part 3): "`6.2` | One non-human-principal rule.
    Refusal reasons change for inputs that are already refused".
  - Same file, lines 95–96: "Any change not listed here to what a gate
    accepts or refuses stops and returns to the owner."
- **AGENTS.md** verification rules 1–11, and these guardrails:
  - "Conformance expected values are hard-coded literals, never imported from the module under test";
  - "A rule-6 evidence record must store each mutant's `old`/`new` fragment and the commit it ran at";
  - "The PWB-REQ-014 authority sweep reads evidence-record keys";
  - "`npm run poc:pwb-*-mutation-*` rewrites sources in place".

**Premise check: does any spec define the set of non-human principal shapes?**

- [Observed] No. I ran a Python `re` sweep over every tracked `.md` file under
  `openspec/` and `.syzygy/governance/contracts/`: 876 files. The pattern was
  `non[- ]?human|nonhuman|machine principal|actor class|automated principal|AI principal|bot account`,
  case-insensitive, and it matched 88 lines.
- Every `openspec/` hit is one of these lines, and none enumerates a shape:
  - PWB spec lines 678 and 2520;
  - in `cap1-trusted-bootstrap-consent`: `spec.md:7,32,42,43,75`, `design.md:42` ("Recognized non-human acts are refused"), `CONTRACT-COVERAGE.md:27`, `CAPABILITY-COVERAGE.md:22` and `REVIEW-DISPOSITION.md:17`.
- The contract hits are "untrusted actor class" prose and the RFC3-16 failure
  list. None names a string shape either.
- The bead's fallback therefore governs: the union of both former rules,
  fail-closed. The change's comment states this (`act-fields.ts:7-11`), but
  the change carries no file:line premise record. See finding N5.

**My class determination.** I agree that classes 1 (authority boundaries) and
4 (security) are touched. Both gates decide whether an owner act is effective,
and the body-read gate is the consent precondition for every Butlers read. I
add class 6 as touched in a minor way: the machine rendering of the refusal
reason changes for some already-refused inputs (finding N4). No endpoint is
removed, so class 6 adds no GP-Q0 check beyond the class 1 and class 4 ones.

## 3. What I ran and the results

**Clones.**
- `clone-head` is `git clone -q <worktree>` at `ecb68fce`, then `npm ci`.
- `clone-base` is the same clone checked out at `fdc866af`, then `npm ci`.
- [Observed] In both clones, `node_modules/@syzygy/*` symlink into the clone
  itself.

**Battery at head** (`clone-head`, before any reviewer file was added). Result
lines verbatim:

- `npm run typecheck` printed the `tsc -b …` banner and no diagnostics. I
  appended the exit status: `exit 0`.
- `npx vitest run --project @syzygy/three-surface-poc-core` (via `npm run test -- --project …`):
  - ` Test Files  33 passed | 2 skipped (35)`
  - `      Tests  1033 passed | 2 skipped (1035)`
- `npx vitest run --project @syzygy/three-surface-poc-app`:
  - ` Test Files  88 passed | 1 skipped (89)`
  - `      Tests  1075 passed | 2 skipped (1077)`
- `python3 scripts/check_governance.py`:
  - `32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted`
  - `exit 0`
  - The 21 WARN lines are the checker's standing report-only and downgraded
    families (CG-1c … CG-27). None names a file this diff touches.
- [Observed] There was no timeout or flake, so nothing needed a re-run.

**A. Shared helpers are byte-for-byte the former predicates**
(`compare_helpers.py`, sha256 `ea1bd043…`).

- [Observed] The script compared these definitions in base
  `body-read-authority.ts`, base `walkthrough-judgment.ts` and head
  `act-fields.ts`, after stripping only a leading `export `:
  - 7 regexes: `PROJECT_IDENTITY`, `SHA256`, `SLUG`, `ISO_DATE`, `ACT_IDENTITY`, `PHRASE` and `TAG`;
  - 2 labels: `STATE_1_LABEL` and `STATE_2_LABEL`;
  - 6 functions: `isGovernancePath`, `isIsoDate`, `isHumanName`, `sha256`, `provenanceFromLabel` and `deepFreeze`.
- Result: `ALL SHARED RULES IDENTICAL`. Each of the 15 is present in all
  three files, except the two labels. Before the change those were defined
  only in body-read and imported by the judgment evaluator.
- Rule 6 for this check: a mutated copy changing `<= 200` to `<= 201` in
  `isHumanName` printed `DIFFERENT` and `MISMATCH`.
- [Observed] `git grep NON_HUMAN_PRINCIPAL` at head finds one definition,
  `act-fields.ts:33`. It has exactly two uses: `body-read-authority.ts:456`
  and `walkthrough-judgment.ts:660`, each `NON_HUMAN_PRINCIPAL.test(owner.value)`.
- At base there were two definitions, `body-read-authority.ts:340` and
  `walkthrough-judgment.ts:424`, and the same two uses. No test imports
  `act-fields`.

**B. The union claim is exact** (`union_check.mjs`, sha256 `c4f55197…`). The
script reads the two former rules from the base source text and the shared
rule from head `act-fields.ts`.

- [Observed] Structural check: the shared rule's `source` is exactly
  `oldBody.source + '|' + oldJudgment.source`, and all three flags are `i`.
  It printed `true`.
- [Observed] Behavioural check over 323,482 strings: hand seeds, every
  keyword with 17 separators on each side, upper-case forms and 300,000
  random strings. Result: `union-true 42298, differing 0`.
- Rule 6: with the `-agent` suffix alternative deleted from the shared rule,
  the same run printed `structural … false` and `differing 6126`.
- [Inferred, from ECMAScript semantics] Without `g` or `y` flags,
  `RegExp.prototype.test` is true iff some start position matches. A
  top-level disjunction matches at a position iff some alternative does, and
  no lookaround or backreference crosses the alternatives. So for every
  string, the new rule matches iff either former rule matched. Both gates
  call only `.test`, so capture-group renumbering has no effect.

**C. Live records on main, re-derived independently** (`live_diff.mjs`,
sha256 `eedf318b…`).

The script ran under the base build and under the head build, each after
`npm run build:poc`, over the same governance revision `fdc866af`.

- [Observed] Production loaders: both gates through
  `loadBodyReadAuthorityInputs` and `walkthroughJudgmentInputsFor`.
  - body-read: consent, policy and registry are each `valid`, and
    `admits: true`.
  - judgment: `absent / no-run-record`.
  - The base and head evaluations are deep-equal. The canonical-JSON sha256
    of the body evaluation is `49698f8f…` at both.
- [Observed] The judgment denominator on main is zero. There is no
  `.syzygy/governance/records/` directory at `fdc866af`, and none of the
  scheduled run-record, judgment or judgment-act paths exist. The judgment
  gate's live evaluation therefore never reaches an owner predicate.
- [Observed] Record population. I enumerated every tracked blob at `fdc866af`
  with `git ls-tree -r -z`, which the harness reads as `names`: 2,942 blobs,
  of which 2,938 decode as UTF-8 and 4 do not.
  - Running `parseOwnerActRecord` over all 2,938 finds 148 non-missing
    `Owner:` fields: 117 in `.syzygy/**/*.md`, 28 in `scripts/*.py` and 3 in
    `packages/**/*.ts`. The 31 code hits are recorder templates and fixtures.
  - There are 3 distinct values: `Tzeusy` (139), `{{OWNER}}` (8) and
    `{owner}` (1).
  - [Observed] Python `re` with the former body rule, the former judgment
    rule and the union finds each of the three human under all three rules.
  - The owner list is identical under base and head code.
- [Observed] The author's record counts 1,691 Markdown files and 117 Owner
  fields. My Markdown count is the same: 1,691 of the 2,942 blobs, with the
  same 117 fields. My additional 31 come from non-Markdown files (finding N3).
- Conclusion: no live record changes outcome, and none changes refusal
  reason. The retained record's conclusion holds.

**D. New tests fail on the base where they should.**

- [Observed] I copied the two head test files into `clone-base` and ran them
  against the base gates.
- `body-read-authority.test.ts`: 270 tests, 49 new. Exactly 21 new tests
  fail: the 7 "(flipped)" principals × consent, policy and registry.
  - The 7 principals: `daemon`, `automation: nightly`, `syzygy`, `ci/release`, `renovate[bot]`, `deploy-bot` and `review-agent`.
  - The 21 non-flipped tests and the 7 human-name tests pass. No pre-existing
    test fails.
- `walkthrough-judgment.test.ts`: 123 tests, 21 new. Exactly 6 new tests
  fail: `machine`, `Anthropic Claude`, `codex`, `gpt-5`, `GitHub Copilot`
  and `an llm`.
  - The other 15 new tests pass, and no pre-existing test fails.
- At head, all 393 tests pass. The base suites are therefore the 221-test
  body suite (the 195-case population plus its other cases) and the 102-test
  judgment suite (84+2 plus its other cases), and both stay green.
- [Observed] The new cases hard-code the owner strings and the expected case
  ids `owner-non-human`, `${kind}:owner-non-human` and `owner-another-human`
  as literals. Nothing is imported from the module under test.

**E. Retained rule-6 evidence** (`verify_digests.py`, sha256 `4ec92a52…`;
`rerun_mutants.py`, sha256 `c438ae4f…`).

- [Observed] All 22 `(commit, path, sha256)` claims in the five new evidence
  records match `git show <commit>:<path>`, and every head-side subject digest
  is also the digest at `ecb68fce`. The script printed
  `claims 22 mismatched 0`.
- [Observed] `owner-act-non-human-rule-mutants-2026-10-21.json` names its
  subject, commit `88c79070`, the digests of its three subject files, its test
  files, and each mutant's `old`/`new` fragments. Its harness source is
  embedded.
  - I re-ran all 13 mutants in `clone-head` by applying the recorded
    fragments. Each `old` occurs exactly once, and every mutant's bytes were
    restored and digest-verified.
  - Result: `mutants 13 killed 13 identical-to-record 13`. For every mutant,
    the failed count and the set of failing test names equal the record:
    baseline 393/0; failed counts 4, 20, 16, 12, 2, 4, 2, 4, 4, 2, 8, 21 and 6.
- [Observed] `pwb-p4-2-mutation-sweep-2026-10-21-bpyt-6-2-judgment-invalid-cases.json`
  records commit `88c79070` and 98 of 98 killed. I re-ran the whole group in
  `clone-head` at `ecb68fce`:
  - command: `node apps/three-surface-poc/dist/pwb-mutation-sweep-main.js --group judgment-invalid-cases --date reviewer-b62`;
  - result: `summary: 98/98 killed, 0 survived, 0 restore failures`, with
    `uncommittedChanges: []`;
  - the source digest is `c33d0140…`, as recorded;
  - per mutant, the observed counts, failing sets and killed flags are
    identical to the retained record: 98 ids, 0 differing.
- [Observed] `pwb-mutation-run-2026-10-21-bpyt-6-2.json` records commit
  `88c79070` and 94 of 97 killed.
  - The three survivors are `exact-state-inflate`,
    `disclosure-independently-verified-forced` and
    `disclosure-state-1-label-inflated`.
  - They failed 11, 8 and 8 tests, so they were detected. Each has
    `mustFailMissing: ["evaluates the three real 2026-09-02 PWB acts"]`.
  - [Observed] At the base the test is titled "evaluates the three real
    current PWB acts" (`governance-inputs.test.ts:439`). `git log -S` places
    the rename at `de472fa5`, before this bead.
  - The runner's kill rule is `run.failed > 0 && missing.length === 0`
    (`pwb-mutation-run-main.ts:150-151`). So the three "survivals" were a
    stale must-fail title, not undetected mutants.
- [Observed] `027fd501` changes only those three `mustFail` strings, in
  `pwb-mutation.ts:135,189,198`. The r2 record at `027fd501` shows 97 of 97
  killed, and those three now have `mustFailMissing: []` with the same failed
  counts. The r1 record is retained beside r2, and the `ecb68fce` commit
  message discloses it.
- [Observed] I re-ran the full PWB-REQ-005 runner in `clone-head` at
  `ecb68fce`, built at head:
  - command: `node apps/three-surface-poc/dist/pwb-mutation-run-main.js --date reviewer-b62`;
  - result: `summary: 97/97 killed, 0 survived, 0 restore failures`, with
    baseline 296/296 and `uncommittedChanges: []`;
  - the source digests equal r2's;
  - per mutant, the observed counts, killed flags and `mustFailMissing` are
    identical to the retained r2 record: 97 ids, 0 differing.
- [Observed] None of the five new evidence files has a key named `source`,
  `provenance`, `evidence` or `anchor` anywhere in its JSON tree. This is the
  PWB-REQ-014 sweep hazard, and the app suite's sweep test passed.

**F. Export surface and module wiring** (`exports.mjs`, sha256 `0fbd394d…`).

- [Observed] Runtime export names and string values are identical at base and
  head, built dist for both. `diff` of the two listings is empty:
  - `index.js`: 255 exports;
  - `body-read-authority.js`: 11, still exporting `STATE_1_LABEL` and `STATE_2_LABEL`;
  - `walkthrough-judgment.js`: 15.
- [Observed] `act-fields.ts` is not in `index.ts`, so it adds no `export *`
  collision, and `tsc -b` passes. `ProvenanceLabel` is still exported as a
  type from `body-read-authority.ts:67`.
- [Observed] Both file paths are kept.
- [Observed] No governed file under `.syzygy/` or `openspec/` cites the base
  digest of either gate source. The only citers of `647a9583…` and
  `81be5932…` are older `docs/evidence/*.json` records and one review raw.

**G. Old-versus-new differential over a mutated-record corpus** (finding N2).

The retained evidence has no such differential, so I built one.

- Two vitest harness files, each a verbatim copy of the fixture section of
  the respective test file plus an evaluation loop:
  - the body-read fixture prefix is 334 lines, sha256 `c90cf593…`;
  - the judgment fixture prefix is 263 lines, sha256 `5cfa6f4a…`;
  - the shared corpus module is `zz-reviewer-corpus.ts`, sha256 `1823ba39…`.
- Identical bytes were installed in both clones, asserted by
  `install_harness.py`, sha256 `6ad4bfd7…`.
- The corpus:
  - 7,248 owner values: 20 keywords × 11 separators on each side × 4 shapes,
    plus 56 hand-picked values (deduplicated, then filtered). The count is
    derived from the output: 43,488 unaltered-prose body rows ÷ (3 kinds × 2
    modes);
  - 15 altered-prose mutations of the act record, each run with the 56
    hand-picked owners:
    - title claims agent drafting;
    - ceremony intro says Claude Code performed the act;
    - effect paragraph gains an agent sentence, is paraphrased without its
      scope anchors, or is reflowed;
    - an extra head paragraph adds `Recorded by: agent: …`, a duplicate
      `Owner: codex`, a duplicate `Owner: daemon`, or a `[bot]` note;
    - the Owner label is bolded or lower-cased;
    - the Owner line is continued onto a second line, or gains trailing prose;
    - the not-authorize section is altered;
    - `Owner:` lines are appended after the headings;
  - 2 expected-owner modes: production (`Tzeusy`), and the expected owner
    equal to the act's owner. For the judgment gate the judging party is set
    to match, with the digests re-bound.
- [Observed] Body-read: 48,528 rows, and the base and head row sets are
  equal. 2,970 rows change:
  - production mode: 1,485 `owner-another-human → owner-non-human`;
  - expected-owner-equal mode: 1,422 `valid → owner-non-human` and 63
    `scope-wrong → owner-non-human`;
  - every changed row ends in `owner-non-human`, and 0 go from refused to
    admitted;
  - 0 admitted rows flip under production expectations.
- [Observed] Walkthrough-judgment: 16,176 rows. 2,440 change:
  - production mode: 1,221 `owner-another-human → owner-non-human`;
  - expected-owner-equal mode: 1,138 `lawful → owner-non-human`, 72
    `owner-another-human → owner-non-human` and 9 `scope-wrong → owner-non-human`;
  - every changed row ends in `owner-non-human`, and 0 go from refused to
    admitted;
  - 0 flips under production expectations.
- [Observed] The altered-prose rows that change are:
  - 126 per prose mutation for body-read, and 18 per prose mutation for the
    judgment gate;
  - the judgment gate's `owner-line-trailing-prose` (75) and
    `owner-line-continued` (71) rows, where the trailing text "…Claude Code
    session" makes the parsed owner match `\bclaude\b`.
- [Observed] Every changed row ends in `owner-non-human`, so no prose
  mutation changes any other predicate's outcome between base and head.
  [Inferred] Altered prose changes an outcome only through the Owner value
  the parser extracts.
- [Observed] Prediction check, `compare_diff.py`, sha256 `5e87b0fe…`. For the
  unaltered-prose rows, an independent Python model of the two former rules
  predicts which rows change.
  - It matches all 43,488 body rows and all 14,496 judgment rows except 168
    and 160. In every one of those, the owner contains a tab: the parser or
    `isHumanName` refuses it as `owner-malformed` before the non-human
    predicate, at both base and head. They show a gap in my model, not a
    behavioural change.
- [Observed] Mutated live records, part of `live_diff.mjs`. The corpus is the
  three real act records at `fdc866af`, with the Owner line substituted with
  20 values, × 8 prose mutations, through the real body-read inputs: 480 rows.
  - 144 change, all `<kind>:owner-another-human → <kind>:owner-non-human`.
    The owners are `daemon`, `automation: nightly`, `syzygy`, `ci/release`,
    `renovate[bot]`, `deploy-bot`, `review-agent` and `Tzeusy-bot`.
  - 0 admit flips.
  - The 36 `valid` rows, the live owner with prose that keeps the act valid,
    stay `valid`.
- Raw outputs:
  - `diff-body-{base,head}.jsonl`, sha256 `609276e8…` and `d278fe9b…`;
  - `diff-judg-{base,head}.jsonl`, sha256 `8bc6ca67…` and `666fcfda…`;
  - `live-{base,head}.json`, sha256 `78fe13b5…` and `b8024d62…`.

**H. The reviewer's own alternative-level mutants** (`reviewer-mutants.json`,
sha256 `9624050b…`; results `reviewer-mutants-result.json`, sha256 `4fd8c080…`;
finding N1).

- [Observed] I applied each mutant to `act-fields.ts` in `clone-head` and ran
  the same 393 tests:
  - deleting `agent`, `bot`, `service`, `system`, `pipeline` or `model` from
    both line-start arms: each **survives**, with 0 failing;
  - deleting `ci` from both line-start arms: killed, 4 failing;
  - deleting `:` from the first arm's separator class, `([:\s-]|$)` →
    `([\s-]|$)`: **survives**, with 0 failing.

## 4. Findings

**N1 — note. Six alternatives shared by both former rules, and the first
arm's colon separator, have no killing test.**

- Evidence:
  - [Observed] Section 3H: 7 reviewer mutants of `act-fields.ts:34` survive
    the full 393-test pair of suites.
  - [Observed] The only pre-existing `owner-non-human` fixture in either
    suite is `'agent: Claude Code'` (`body-read-authority.test.ts:364`,
    `walkthrough-judgment.test.ts:324`). The model-name arm `\bclaude\b` also
    catches it, so it does not pin the `agent` prefix.
  - [Inferred] The same deletions would have survived at the base, since
    those suites had the same single fixture. The gap is narrowed by this
    change, not introduced by it.
- The bead's gate species is "new cases for each principal that flips (one
  per pattern arm)". The change meets that: every flipping alternative has a
  case. GP-Q0's "a rule-6 mutant for each predicate" is met at arm level by
  the 13 retained mutants. It is not met at alternative level.
- Failure scenario: a later edit drops `service` from the rule, for example
  while trimming it. An owner field `service: deploy` then becomes "human" to
  both gates, and CI stays green.
  - At production expectations the act is still refused, as
    `owner-another-human`, so this is not a fail-open.
  - But the refusal reason drifts silently: the same class of drift this
    bead repairs.
- Proposed fix: add one owner per uncovered alternative to both
  `NON_HUMAN_OWNERS` tables, each with no other arm matching. For example:
  - `bot`, `service: deploy`, `system`, `pipeline-7`, `model: x`;
  - an `agent` form with no model name, such as `agent: nightly`;
  - `machine: build-42`, for the colon in the first arm.

  Record the mutants above, with old/new fragments, in the rule-6 evidence.

**N2 — note. The retained evidence does not contain GP-Q0's old-versus-new
differential over a mutated-record corpus with altered prose.**

- Evidence: [Observed]
  - `owner-act-live-records-before-after-2026-10-21.json` evaluates the
    unmutated live records, plus owner values parsed from tracked files.
  - `owner-act-non-human-rule-mutants-2026-10-21.json` mutates code, not
    records.
  - The new test cases vary only the Owner value of a fixed fixture.
  - None of these is a mutated-record corpus with altered prose, which
    `OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md:64` requires for
    a class 1/3/4 pull request.
- What my differential shows (section 3G):
  - Over 64,704 fixture rows and 480 mutated live-record rows, every outcome
    change ends in `owner-non-human`.
  - Under production expectations, every change is a refusal-reason change
    of an input already refused.
  - No prose alteration changes any other predicate's outcome.
  - Nothing goes from refused to admitted.
- Failure scenario: the owner notice in the cycle report (`syzygy-bpyt.10`)
  cites only the retained evidence. It then asserts a check the record does
  not hold, which is the rule-11 failure mode.
- Proposed fix: retain the differential with the pull request. Cite this
  raw, or add an evidence record that carries this harness (the files named
  in 3G with their digests) and the summary counts.

**N3 — note. The live-record denominator is restricted to Markdown, and the
judgment population is zero without saying so.**

- Evidence: [Observed]
  - The retained record's parser method covers 1,691 `.md` files and 117
    Owner fields. Its second method covers line-start Owner lines in `.md`
    files only.
  - Over all 2,942 tracked blobs, there are 148 parsed Owner fields with 3
    distinct values, adding `{owner}`.
  - The judgment gate's live input has no run record, judgment or act at
    `fdc866af`. The record shows `kind: absent`, but no sentence states that
    the judgment-record denominator is 0.
- The conclusion is unchanged: every value is human under all three rules.
- Failure scenario: a later reader re-derives "every act record on main"
  over all tracked files, gets 148, and cannot reconcile it with 117. Or the
  reader takes the judgment row as having been exercised.
- Proposed fix: in the PR's before/after table, state both populations, and
  state "judgment records on main: 0 (no `.syzygy/governance/records/`)".

**N4 — note. Acceptance changes for a configured non-human expected owner.
This is unreachable today, but the listed description does not say it.**

- Evidence:
  - [Observed] In section 3G's expected-owner-equal mode, 1,422 body-read
    rows and 1,138 judgment rows change from admitted to `owner-non-human`.
    In each, the act's owner and the configured `expectations.owner` are both
    a name in the symmetric difference of the former rules: for body-read
    `daemon`, `syzygy` or `x-bot`; for the judgment gate `codex`, `machine`
    or `GitHub Copilot`.
  - [Observed] Production cannot reach these rows. The only non-test owner
    literals in `apps/` and `packages/` are `owner: 'Tzeusy'` at
    `governance-inputs.ts:83` and `walkthrough-inputs.ts:113`. The third, at
    `test-walkthrough-judgment-fixture.ts:16`, is a test fixture.
    `PWB_AUTHORITY_EXPECTATIONS_BY_PROJECT` has one entry
    (`governance-inputs.ts:137-139`), and an unknown project throws.
  - The bead itself names this "defense-in-depth check that would catch a
    non-human name configured as the expected owner". The direction is
    fail-closed.
- The finding: GP-Q0 Part 3 (line 88) and the `88c79070` commit message
  describe the effect as "Refusal reasons change for inputs that are already
  refused". That is exact for every reachable input. It is not exact for the
  exported evaluators' input domain.
- Class 6, minor: the changed case id is rendered.
  - `authority-disclosure.ts:114-117` renders it as `invalidCase` and in the
    disclosure sentence.
  - `polaris.ts:887` renders it as `data-parity-field="judgment-case"`.
  - So for already-refused inputs the machine and human renderings change
    value. That is the approved output change; it is not a new interface.
- Failure scenario:
  - The owner reads the cycle-report notice as "only refusal reasons
    changed".
  - Later, a second observing project registers an owner whose name matches
    one former rule only, such as a team account `deploy-bot`. The gate
    refuses it, and nobody can trace the refusal to an approved decision.
- Proposed fix: no code change. In the pull request's changed-case list and
  the `syzygy-bpyt.10` owner notice, add one sentence: "the shared rule also
  refuses an expected owner configured with a name either former rule
  called non-human; no such configuration exists (`expectations.owner` is
  the literal `Tzeusy` in both loaders)." State classes 1, 4 and 6, the last
  as value-only, with no endpoint change.

**N5 — note. The rule-6 records of the PWB runners carry no old/new
fragments, and their commit pins will not survive a rebase-merge. The spec
premise check has no file:line record.**

- Evidence: [Observed]
  - In both `pwb-mutation-run-…-bpyt-6-2*.json` files and in the
    judgment-sweep record:
    - each `disable-predicate` mutation stores `id`, `file`, `caseName`,
      `line` and the outcome;
    - each `literal` mutation stores `id`, `description`, `mustFail` and the
      outcome, but no `from`/`to`.
    - [Inferred] This is the pre-existing runner format, not introduced by
      this change.
  - The fragments are recoverable from `pwb-mutation.ts` and
    `pwb-mutation-sweep.ts` at the recorded commit. But `88c79070` and
    `027fd501` become reachable from no ref if the branch is rebase-merged.
    That is the guardrail's own warning.
  - The body-read run's `sourceDigests*` list only the files it mutates. It
    omits `act-fields.ts`, whose rules the gate's predicates now apply. The
    non-human mutants record does carry `act-fields.ts`'s digest.
  - The bead's criterion 1 asks for the spec premise check "recorded with
    file:line". The change records only the conclusion, at
    `act-fields.ts:7-8` and in the commit message.
- Mitigation [Observed]:
  - every recorded source digest equals the bytes at `ecb68fce`;
  - `pwb-mutation.ts` at `ecb68fce` equals its bytes at `027fd501`;
  - I reproduced the whole judgment sweep at `ecb68fce` (section 3E).
- Failure scenario: after a rebase-merge, a reader holding r1 cannot
  recover the fragments from the recorded commit, and must trust that main's
  `pwb-mutation.ts` is the same.
- Proposed fix: in the pull request, cite the file:line premise sweep from
  section 2 of this raw. Then either keep the commits reachable, by a merge
  commit or a tag, or add one sentence to the evidence index: the fragments
  for these runs are those of `apps/three-surface-poc/src/pwb-mutation.ts`
  and `pwb-mutation-sweep.ts` at the merged commit, whose bytes equal
  `027fd501`'s.

There are no blocking findings.

- [Observed] No input changes from refused to admitted, in any corpus I ran.
- No reachable admitted input becomes refused.
- The shared helpers are byte-identical.
- The export surface is identical.
- `pwb-mutation.ts` changes only the three must-fail titles, which were
  stale before this bead. It does not change what a gate accepts or refuses.

## 5. Verdict per acceptance criterion

1. **One `NON_HUMAN_PRINCIPAL`, imported by both validators; premise check;
   exact union. Met.**
   - One definition, imported by both (section 3A).
   - My premise sweep finds no spec that enumerates the shapes (section 2).
   - The rule is exactly the union: structurally, behaviourally over 323,482
     strings, and by ECMAScript semantics (section 3B).
   - The premise check is not recorded with file:line in the change (N5).
2. **Every owner-act and judgment record on main, before and after, with a
   stated denominator. Met.**
   - Independently re-derived over all 2,942 tracked blobs: 148 Owner
     fields, 3 values, all human under all rules.
   - The production gates' output is identical at base and head.
   - The judgment population is 0.
   - The stated denominators should be broadened (N3).
3. **New cases for every principal whose outcome changed; both suites green.
   Met.**
   - 21 body-read and 6 judgment new cases fail on the base exactly where
     the principal flipped, and pass at head (section 3D).
   - The 195-case and 84+2-case suites stay green.
   - The coverage gap at alternative level is N1.
4. **Fresh rule-6 evidence for both gates retained, old evidence untouched.
   Met.**
   - All 22 digest claims are verified.
   - The 13 shared-rule mutants reproduce identically.
   - The judgment sweep reproduces 98 of 98, identically.
   - The full body-read runner reproduces r2's 97 of 97, identically.
   - No prior evidence file was modified.
   - Format remainders are in N5.
5. **Behaviour preservation beyond the owner-listed change. Met, with a
   disclosure exception (N4).**
   - The only behavioural change is the union rule.
   - Under production expectations it changes refusal reasons only for
     already-refused inputs.
   - Under a non-production expected owner it can also refuse an input the
     base admitted. That is fail-closed and unreachable today.
   - The other moved rules are byte-identical, the export surface is
     identical, and the `pwb-mutation.ts` change is harness-only.
6. **Old-versus-new differential over a mutated-record corpus with altered
   prose. Not met by the retained evidence; supplied by this review.**
   - The retained evidence does not contain one (N2).
   - My differential (section 3G) shows no change outside the approved
     description, except the unreachable N4 rows.

Overall verdict: **CONFIRM WITH EXCEPTIONS**. The exceptions are notes N1–N5.
None blocks merging. N2 and N4 should be repaired in the pull request text
and evidence index before the owner notice is written.

## 6. Cleanup

- [Observed] Before deletion, `git status --short` in `clone-head` showed no
  modified tracked file. The only entries were untracked: my three harness
  files and the two runner outputs. All mutants were restored, and the
  digests were verified by each runner.
- I copied the two runner outputs out of the clone:
  - `pwb-mutation-run-reviewer-b62.json`, sha256 `122d4370…`;
  - `pwb-p4-2-mutation-sweep-reviewer-b62-judgment-invalid-cases.json`,
    sha256 `05fd8e0e…`.
- I then deleted `clone-head`, `clone-base` and the comparator fixture
  directory with `rm -rf`.
- [Observed] The worktree's `git status --short` is empty: the worktree was
  not modified.
- Kept: every harness, input and output named above, plus the logs. They are
  in
  `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/lead/b62/reviewer/`,
  so the lead can retain or discard them.
- I made no `bd` mutation, no commit and no push.
