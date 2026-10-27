# R-GP-IMPL-NON-HUMAN-PINS-1 — CC-REV-1 implementation review of syzygy-bpyt.6.8, round 1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: df2f67e1
Subject: r1-review.diff sha256 3f6e1daeb2508375a90a998749aed21cbdab188251b868fa6e2104c7163ffe58

Reviewer: fresh-context CC-REV-1 reviewer (Opus 5.5, default model), 2026-10-22. I did not
author the change. No target-repository content was fetched or read; every input below is a
Syzygy file, the bead, or the PR body. Exceptions: notes N1–N4, none blocking.

## 1. Subject identity checks

- [Observed] `sha256sum` of the brief's subject file,
  `lead/b68/r1-review.diff`:
  `3f6e1daeb2508375a90a998749aed21cbdab188251b868fa6e2104c7163ffe58`. **Matches** the brief.
- [Observed] In a scratch clone, `git fetch https://github.com/Tzeusy/syzygy.git
  agent/syzygy-bpyt.6.8` gave `FETCH_HEAD` = `df2f67e14da12b5d553276b4324511227288b009`, the
  reviewed commit. `gh pr view 504` reports `headRefOid` `df2f67e14da12b5d553276b4324511227288b009`,
  base `main`, state `OPEN`, 10 files.
- [Observed] `git merge-base df2f67e1 <GitHub main>` = `b7697f6ac82c7fdb47c6858f70b23febdd3f505c`,
  the brief's base.
- [Observed] I re-derived the diff with `git diff b7697f6a… df2f67e1… --output=<scratch>/rederived.diff`
  and hashed it: `3f6e1daeb2508375a90a998749aed21cbdab188251b868fa6e2104c7163ffe58`. **Byte-equal**
  to the subject.
- [Observed] Commits base..head, 4: `41aa82cf` (harness), `a2d4a23b` (test pins), `017e2afb`
  (mutant records), `df2f67e1` (verification record).

## 2. Clauses relied on (quoted)

**RFC3-16(a)**, `.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md`,
the clause that the non-human-owner refusal implements:

- line 218–220: "An effective owner act is an actual human owner act whose record is current,
  attributable, scope-matched and bound to the artifact's exact digest under RFC3-16(b)."
- line 246–248, "Trust premise for state (1)": "A well-formed file, stored owner name, machine
  submission or agent assertion is never by itself an owner act."
- line 318–321, "Effect when the owner-act gate fails": "Missing, digest-mismatched,
  wrong-scope, stale, expired, superseded, revoked, unattributed or non-human act state blocks the
  dependent effect, renders the authorization Unknown and mints a contradiction routed to owner
  adjudication."

**PWB-REQ-005** case population,
`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md:678`:
"Owner attribution has four independent cases: missing, malformed, another human and a
non-human principal." **PWB-REQ-022**, the same file, line 2520: "Apply PWB-REQ-005's exact
55-case common population to the judgment act, including separate another-human/non-human owner
cases".

The rule's own statement, `packages/three-surface-poc-core/src/act-fields.ts:7–11` (unchanged by
this PR): "No spec enumerates the non-human shapes, so the rule here is the union of both former
copies: an owner field either copy refused as non-human is refused as non-human by both. Under
VIS-4 an AI principal never stands in for the owner."

[Observed] I found no clause that enumerates non-human shapes. A reviewer script
(`tools/nonhuman_hits.py`) went over every `*.md` under `openspec/` and `.syzygy/` at the reviewed
commit. It found 17 files with 25 lines containing "non-human" (case-folded). Only 4 of those 25
lines also name a shape token (`agent`, `bot`, `machine`, `service`, `ci`, `pipeline`, `model`,
`claude`, `codex`, `gpt`, `copilot`, `llm`, `daemon` or `automation`, as whole words), and all
4 speak of machine submissions or actors, not of owner-name shapes. The shapes are therefore
owner-approved only as bead 6.2's union.

**GP-Q0**, `.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`:

- line 60: "Each pull request states which CC-REV-1 classes it touches. Any pull request whose
  classes are not "none" gets the CC-REV-1 independent review, from a fresh-context reviewer on
  the default model."
- lines 62–66: "**Which ones:** pull requests touching class 1 (authority boundaries), class 3
  (deterministic observation) or class 4 (security) … **The checks:** an old-versus-new
  differential over a mutated-record corpus that includes records with altered prose; a rule-6
  mutant for each predicate; a non-blocking owner notice in the cycle report."
- line 87 (part 3 table): "`6.2` | One non-human-principal rule. Refusal reasons change for
  inputs that are already refused".
- lines 94–95: "Any change not listed here to what a gate accepts or refuses stops and returns
  to the owner."

**CC-REV-1**, `.syzygy/governance/policies/craft-and-care/review-and-documentation.md:37`:
"4. **security** — anything under SEC-1…SEC-5, auth surfaces, egress paths". Line 45: "Class
membership is contested by default and is never finally determined by the agent performing the
change".

**AGENTS.md** at the reviewed commit:

- rule 6 (line 126): "Mutate the input and confirm the check fails, per predicate, before
  trusting it".
- rule 11 (line 134): "An evidence record names its subject and the subject's digest; a record
  that names neither cannot be re-checked against the bytes it describes."
- line 261: "A mutation that throws at describe time reports zero tests and scores as survived".
- line 263: "A rule-6 evidence record must store each mutant's `old`/`new` fragment and the
  commit it ran at".
- line 273: "Conformance expected values are hard-coded literals, never imported from the module
  under test."

**The bead** (`bd show syzygy-bpyt.6.8 --json`, read-only). Acceptance criteria, verbatim:
"1. Both NON_HUMAN_OWNERS tables gain one owner per uncovered alternative, with literal expected
ids. 2. A rule-6 record under docs/evidence/ stores each deletion mutant's old/new fragment, the
commit, subject digests and killed counts; every mutant in section 3H of
R-GP-IMPL-OWNER-ACT-FIELDS-1-RAW.md is killed. 3. No gate outcome or reason changes:
act-fields.ts is untouched, stated with before/after test counts and Tests: +a ~b -c." The
description adds: "Not in scope: changing the rule itself (any change to what a gate accepts or
refuses returns to the owner, GP-Q0 part 3)."

**The predecessor raw**, `docs/reviews/R-GP-IMPL-OWNER-ACT-FIELDS-1-RAW.md`, section 3H: deleting
`agent`, `bot`, `service`, `system`, `pipeline` or `model` "from both line-start arms: each
**survives**"; deleting `ci` from both: "killed, 4 failing"; deleting `:` from the first arm's
class: "**survives**". Finding N1's proposed fix names the seven owners the bead copies.

## 3. What I ran and the results

All in a scratch clone of `/home/tze/GitHub/syzygy` at `df2f67e1` after `npm ci` (exit 0), plus
a detached worktree of the same clone at base `b7697f6a` for the Python checks.

**A. Changed-path sweep (denominator 10).** [Observed] `git diff --name-status b7697f6a df2f67e1`:

| Status | Path | Class |
|---|---|---|
| A | `docs/evidence/non-human-principal-pins-2026-10-22/assemble_verification.py` | evidence |
| A | `…/compare_test_lists.py` | evidence |
| A | `…/mutants-after-2026-10-22.json` | evidence |
| A | `…/mutants-before-2026-10-22.json` | evidence |
| A | `…/mutate_non_human_principal.py` | evidence |
| A | `…/regex-differential.mjs` | evidence |
| A | `…/test-lists-2026-10-22.json` | evidence |
| A | `…/verification-2026-10-22.json` | evidence |
| M | `packages/three-surface-poc-core/src/body-read-authority.test.ts` | test |
| M | `packages/three-surface-poc-core/src/walkthrough-judgment.test.ts` | test |

8 evidence, 2 test, **0 of 10** other. [Observed] `git grep -F non-human-principal-pins df2f67e1`
finds the directory named only by its own two files, so nothing outside it imports or runs it.

**B. Rule and gate byte identity.** [Observed] `git ls-tree -z` at base and head give the same
blobs: `act-fields.ts` `df4f885830ca7fbac8298a1752479316c681f769`, `body-read-authority.ts`
`c1337a19bf8cf6f57c030dc423c508388dae5a98`, `walkthrough-judgment.ts`
`b7cd87b508ba665143b693ade87d480174dfcfd4`. sha256 of `act-fields.ts`: base (via `git cat-file
blob`) and head are both `09a7c2e5c0514349e10b2b82a0aaf55aee9f3fac261385716ec3f70672552986`,
equal to `subjectDigests` in both mutant records.

**C. The two changed test files.** [Observed]

- Head: `body-read-authority.test.ts (322 tests)`, `walkthrough-judgment.test.ts (141 tests)`,
  "Tests  463 passed (463)".
- Base test files checked out over the head tree (the gates are byte-identical, B):
  "(270 tests)", "(123 tests)", "Tests  393 passed (393)".
- Delta: +52 and +18, so +70. [Inferred] 17 owners × 3 kinds + 1 human name = 52, and
  17 + 1 = 18, which matches the added rows. The bead's `Tests: +70 ~0 -0` holds.

**D. three-surface-poc-core project.** [Observed] `vitest run --project
@syzygy/three-surface-poc-core`: "Test Files  33 passed | 2 skipped (35)", "Tests  1111 passed |
2 skipped (1113)". No timeout appeared.

**E. Typecheck.** [Observed] `npm run typecheck` (`tsc -b` over ten projects) printed no
diagnostics and exited 0.

**F. `check_governance.py`.** [Observed] Head: "32 OK, 21 WARN, 0 FAIL (53 checks) — counts
derived, not asserted". Base and head at the same directory depth, `diff` of the full outputs:
only the repo-root line, the scope line ("3029 file(s) examined" → "3037") and CG-2a ("1926 files
examined" → "1929"). [Inferred] +8 tracked files is the 8 added evidence files. The PR body's
"3029 to 3035 and 1926 to 1928" was measured at `017e2afb`, two files earlier, so it is
consistent with this.

**G. `check_quotations.py`.** [Observed] Base and head outputs are byte-identical, both sha256
`ee0324224cb7c33dd4f407f04a8c26677c658d198178c506180d336354bd1726`. That equals the
`quotations-base.txt`/`quotations-head.txt` digest in `verification-2026-10-22.json`, so that one
log digest is reproducible. Head line: "OK    QC-1  a quotation beside a path:line locator was said
by that file — 33 quotations examined in 15 of 919 .md files scanned … 0 findings".

**H. PWB-REQ-014 authority sweep.** [Observed] `apps/three-surface-poc/src/polaris-authority-sweep.test.ts`:
"Tests  5 passed (5)".

**I. Mutation harness, all 53 mutants, both states.** I re-ran
`mutate_non_human_principal.py <clone> <scratch out>`:

- After (head test files): [Observed] my run's record equals the committed
  `mutants-after-2026-10-22.json` in subject digests, rule, corpus (12,355 strings, 4,198
  original matches) and baseline (463/0). Over all 53 mutants, `fragments`, `killed`, `observed`,
  the failing-test name set, `differentialOverCorpus` and `restored` are equal: "mutants
  differing: 0 of 53". Summary: `"killed": 45, "survivors": 8`, `"section3HKilled": "8 of 8"`,
  `"allRestored": true`. Tracked tree clean before and after.
- Before (base test files checked out, which my run records as two `M` entries): [Observed] equal
  to the committed `mutants-before-2026-10-22.json`, "mutants differing: 0 of 53". `"killed":
  27`, `"section3HKilled": "1 of 8"`. 3H's surviving set equals the predecessor raw's seven
  (both-arms `agent`, `bot`, `service`, `system`, `pipeline`, `model`, plus the arm-1 colon), and
  `both-arms-drop-ci` is killed with 4 failing, as the raw says.
- Restoration: [Observed] after both runs `act-fields.ts` hashes to `09a7c2e5…2986`, and `git status
  --porcelain` is empty once I restored the head test files.
- Totals: [Observed] every mutant run in both committed records reports the full count (393 × 53
  before, 463 × 53 after), never 0. No mutant was scored by a load failure.
- Kills by the intended pin: [Observed] I printed the failing test names for 11 mutants of the
  after record. Each fails only on the owner written for it:
  - `both-arms-drop-agent` fails on "agent: nightly" and "agent/triage";
  - `arm1-sep-drop-colon` on "machine: build-42";
  - `arm3-drop-agent` on "agent/triage";
  - `arm3-drop-model` on "model/v2";
  - `arm1-sep-drop-\s` on "machine runner";
  - `arm1-sep-drop--` on "machine-7";
  - `arm3-sep-drop-\s` on "daemon nightly";
  - `arm3-sep-drop--` on "daemon-7";
  - `anchor-arm2-leading-boundary` on "Annagpt Lee" only, 1 per file;
  - `arm1-drop-machine` on the four machine owners;
  - `arm3-sep-drop-/` on `ci/release` and the six new slash owners.

  Each first error line has the form "AssertionError: expected 'consent:owner-another-human' to
  be 'consent:owner-non-human' // Object.is equality".
- Rule 6 on the harness's own guard: [Observed] in the base worktree I changed `copilot|llm)` to
  `copilot|llm|gemini)` in `act-fields.ts` and ran the harness with `--differential-only`. It
  exited 1 with "the rule is not the four arms this script mutates:", printing both literals.
  I restored the file with `git checkout`, and status was empty.

**J. Arm attribution of each new owner.** [Observed] I wrote a reviewer script that tests each
owner against each word-alternative of each arm separately:

| Owner | Alternatives that match it |
|---|---|
| `bot`, `service: deploy`, `system`, `pipeline-7`, `model: x`, `agent: nightly` | two each: `arm1:<word>` and `arm3:<word>` |
| `machine: build-42`, `machine runner`, `machine-7` | `arm1:machine` only |
| `agent/triage`, `bot/deploy`, `system/cron`, `service/gateway`, `pipeline/build`, `model/v2` | `arm3:<word>` only |
| `daemon nightly`, `daemon-7` | `arm3:daemon` only |
| `Annagpt Lee` | none (human) |

**K. Human-name probe of the unchanged rule.** [Observed] With `node -e` and the literal rule:
`"Claude Monet" true`, `"Jean-Claude Van Damme" true`, `"Marie-Claude Lee" true`,
`"Ci Wang" true`, `"Tzeusy" false`, `"Annagpt Lee" false`, `"Talbot" false`, `"Lee Ci" false`.
Order of predicates: [Observed] `body-read-authority.ts:456` and `walkthrough-judgment.ts:660`
test `NON_HUMAN_PRINCIPAL` before the expected-owner comparison at `:458` and `:662`.

Not run: the full 110-command battery and the full `npx vitest run`. The brief does not require
them; the PR reports "commands=110 nonzero=0" and "4982 passed" [Unknown to me, lane-reported].

## 4. Findings

No F-findings. Four notes.

**N1 — note (owner-facing, low). The pinned union rule refuses some real human names as
non-human. Keep the pins; put the question to the owner.**

- Evidence:
  - [Observed] 3K: "Claude Monet", "Jean-Claude Van Damme" and "Marie-Claude Lee" match through
    `\b(claude|…)\b`. "Ci Wang" matches through `^ci` plus whitespace, which is in both
    line-start arms.
  - [Observed] The non-human test runs before the expected-owner test in both gates, so the
    refusal applies even when the name is the registered owner's.
  - [Inferred] Claude, Jean-Claude and Marie-Claude are common French given names. Ci is a
    romanized Chinese name, rarer.
  - None of the PR's 17 new owners is a human name, and its one new human name, `Annagpt Lee`,
    is correctly held human. So no new pin locks a human name in as non-human.
  - [Observed] Two of the new pins do fix the whitespace separator that produces the "Ci Wang"
    class: `machine runner` for arm 1 and `daemon nightly` for arm 3. Deleting `\s` from either
    arm alone now fails a test (3I).
  - [Observed] The `claude` class was already pinned before this PR, by `Anthropic Claude`
    (non-human) and `Claudette` (human).
- Is the verdict what the clause intends? For every new owner, yes [Inferred]:
  - Each is a role word, a role word with a separator, or a separator form of a former gate's
    rule. RFC3-16(a) says a "machine submission or agent assertion is never by itself an owner
    act", and the union is the owner-approved bead 6.2 row of GP-Q0 part 3.
  - The defect is the rule's false positives on real names. No clause enumerates shapes
    (act-fields.ts:7–8; section 2). This PR neither introduced the rule nor changed it.
- Failure scenario:
  - A project whose registered owner is named, for example, "Jean-Claude Martin" has every
    consent, policy, registry and judgment act refused as `owner-non-human`. This is fail-closed:
    nothing is admitted wrongly, but the owner cannot authorize at all and the reason given is
    false.
  - At today's expectation (owner `Tzeusy`), the only effect is that some third-party human
    names get the wrong refusal reason.
- Proposed fix: none in these bytes. Narrowing the rule is a change to what a gate refuses, so
  it returns to the owner (GP-Q0 lines 94–95). Carry the question in the syzygy-bpyt.10 owner
  notice (N2), beside the P3 owner decision on merging the two line-start arms already recorded
  in the bead notes.
  - If the owner keeps the behavior: add one human-name row, for example
    `['Jean-Claude Martin', 'known false positive, owner-ruled <date>']`, expecting
    `owner-non-human`, so that a later narrowing shows up as a test edit.
  - If the owner narrows the rule: these pins are what make the narrowing visible. Do not drop
    them.

**N2 — note (process). Class 4: GP-Q0's extra checks are two of three met; the owner notice is
outstanding.**

- My classification is **class 4 (security), at the test-oracle level only**. The tests guard
  `owner-non-human` on the PWB-REQ-005 consent, policy and registry acts, which is an auth
  surface. No gate byte changes (3A, 3B).
  - Not class 1: no write-universe, typed-authority-table or adapter change.
  - Not class 3: no snapshot or evaluation-identity change.
  - Not classes 2, 5, 6 or 7.
  - I reclassify the PR's "none (contestable class 4)" to class 4. It got the review that class 4
    requires.
- The three GP-Q0 checks:
  1. **Old-versus-new differential over a mutated-record corpus with altered prose: met
     vacuously.** Every non-test, non-evidence file is byte-identical between base and head
     (0 of 10 changed paths; gate blobs equal). `act-fields.ts` declares itself "Pure: no file,
     process or clock". So any such differential returns zero changed rows [Inferred, from the
     byte identity]. Nothing in the retained evidence says this; a disposition should.
  2. **A rule-6 mutant for each predicate: met.** 53 mutants. 45 are killed, and the 8 survivors
     are language-equivalent (section 7). Reproduced 53 of 53 (3I).
  3. **Non-blocking owner notice in the cycle report: not yet present.** It belongs to
     `syzygy-bpyt.10`, not to these bytes.
- Failure scenario: the cycle report omits this PR, and the owner never sees N1's question or
  the class-4 classification. That is a gap in what the record says was checked (rule 11).
- Proposed fix: when `syzygy-bpyt.10` is drafted, add one line for PR 504 covering:
  - class 4, test-only;
  - 45/53 killed, 8 equivalent;
  - differential vacuous by byte identity;
  - N1's owner question.

**N3 — note (low). The test comment, and the PR body's headline, overstate what each owner
kills.**

- Evidence:
  - [Observed] `body-read-authority.test.ts:638–643` and `walkthrough-judgment.test.ts:568–573`
    say: "one owner per remaining alternative of NON_HUMAN_PRINCIPAL, each matched by no other
    alternative, so deleting that alternative (or a separator it alone relies on) changes a
    verdict here". 3J shows that the first six (`bot`, `service: deploy`, `system`,
    `pipeline-7`, `model: x`, `agent: nightly`) are each matched by **two** alternatives. They
    kill only section 3H's both-arms deletion. Deleting `arm3:bot` alone is killed by
    `bot/deploy`, never by `bot`; deleting `arm1:bot` alone survives as an equivalent mutant.
  - [Observed] The comment's "the rest pin the slash and whitespace forms of the second
    line-start arm" leaves out `daemon-7`, a hyphen form.
  - [Observed] The PR body's Outcome line says "every alternative of `NON_HUMAN_PRINCIPAL` now
    has a test that fails when it is deleted". For eight alternatives no test can fail, because
    those mutants are equivalent. The body's Residuals list them, so the remainder is disclosed,
    but the headline is an "every" claim with exceptions.
- Failure scenario: a maintainer pruning the table trusts the comment, treats `bot/deploy` as
  redundant with `bot`, and deletes it. `arm3-drop-bot` then survives again with CI green, which
  is N1's original drift class from the predecessor raw.
- Proposed fix: a follow-up, test-comment-only edit:
  - say that the first six are matched by the word in both line-start arms and kill section
    3H's both-arms deletions;
  - say that the slash, whitespace and hyphen owners kill the single-arm and separator
    deletions;
  - in any disposition or cycle-report text, quote the headline as "every alternative whose
    deletion changes the language".

**N4 — note (low). Evidence re-checkability gaps and a missing harness guard. These fit the
already-planned P3 "harness selftest" follow-up.**

- Evidence:
  - [Observed] `verification-2026-10-22.json` `logDigests` names seven logs, none of which is
    in the tree (3A). Their digests cannot be checked against bytes (rule 11). Only the
    quotations digest is reproducible by re-running, and it reproduced (3G).
  - [Observed] Its governance `note`, "the two outputs differ only in the examined-file counts
    (3029 to 3035 and 1926 to 1928) …", is a string literal in `assemble_verification.py`, not
    derived from the logs. My diff (3F) is consistent with it [Inferred], but the record cannot
    show that it was derived.
  - [Observed] `tree.head` in the record is `017e2afb`, not the reviewed `df2f67e1`. This is
    unavoidable for a record committed after its own run, and harmless here because `017e2afb`
    → `df2f67e1` adds only the record and its assembler.
  - [Observed] The mutant records store commit, old/new, subject digests and first error lines,
    so they are re-runnable, and I re-ran them. They do not store the harness's own digest. The
    predecessor record `owner-act-non-human-rule-mutants-2026-10-21.json` embedded
    `harnessSource`.
  - [Observed] `run_tests` scores `killed = failed > 0` and never compares `observed.total` with
    the baseline. A future mutant that broke module load would show total 0 and count as a
    survivor (AGENTS.md:261). Invalid regexes are refused before running, and every recorded
    total equals the baseline, so this did not happen here.
- Failure scenario:
  - A later edit to the harness makes the 2026-10-22 records unattributable to the bytes that
    produced them once the branch commits are unreachable.
  - A future non-regex mutant that fails at load is reported as an unkillable survivor.
- Proposed fix, in the P3 harness-selftest bead:
  - record `sha256` of `mutate_non_human_principal.py` and `regex-differential.mjs` in each
    mutants record;
  - stop the run when any mutant's `observed.total != baseline.total`;
  - either retain the seven logs beside the record or drop `logDigests`;
  - derive the governance note from a diff of the two logs.

## 5. Every changed output (or the evidence that there is none)

There is none.

- Rendered bytes, wire formats, refusal strings, exit codes: there is no change to any file that
  produces them [Observed: 0 of 10 changed paths are non-test, non-evidence (3A); gate and rule
  blobs equal (3B)].
- Gate verdicts: [Observed] the same 393 pre-existing tests pass at head, inside the 463, with
  0 failed (3C).
- Governance outputs: [Observed] they differ only in examined-file counts (3F). Quotations
  output is byte-identical (3G).
- Signed or digest-bound artifacts: none touched. No `.syzygy/**` or `openspec/**` path is in
  the diff (3A).

## 6. Verdict per acceptance criterion

1. **Met.**
   - Both `NON_HUMAN_OWNERS` tables gain the same 17 rows. The diff shows +23 lines per file:
     17 rows and a 6-line comment.
   - Expected ids are literals: `` `${kind}:owner-non-human` `` over the literal tuple
     `['consent','policy','registry']`, `'owner-non-human'`, `'owner-another-human'` and
     `'consent:owner-another-human'`. None is imported from the module under test.
   - Scope: the bead's seven are present verbatim. The ten extra owners each kill a mutant that
     was a non-equivalent survivor before (3I: `arm3-drop-{agent,bot,system,service,pipeline,model}`,
     `arm1-sep-drop-{\s,-}`, `arm3-sep-drop-{\s,-}`), and `Annagpt Lee` kills
     `anchor-arm2-leading-boundary`. Each is an "uncovered alternative" in the bead title's
     sense ("Pin each alternative … with a test that kills its deletion"), and the bead's list
     is introduced by "e.g.". So the extras are inside the bead's scope.
   - They are inside GP-Q0: they add tests only, and change no gate's accepts or refuses.
2. **Met.**
   - Both records store, per mutant, the old/new regex literal, the commit, subject digests, the
     killed flag, observed counts and the first error line of each failing test.
   - Section 3H is 8 of 8 killed at the head.
   - I reproduced both records mutant for mutant (3I). N4 lists the gaps that remain.
3. **Met.**
   - `act-fields.ts` is untouched: same blob and sha256 at base and head (3B).
   - Test counts go 393 → 463 (3C), and `Tests: +70 ~0 -0` is correct.
   - No gate outcome or reason changes (section 5).

## 7. Test quality

- **Literal expectations:** yes (section 6, criterion 1).
- **Describe-time safety:** `NON_HUMAN_OWNERS` is a module-level literal array. `it.each`
  iterates it at collection time, and every evaluator call is inside a test body.
  - [Observed] All 106 mutant runs (53 before, 53 after) report the full test count.
  - [Inferred] No regex mutant can throw at describe time: the rule is evaluated only inside
    `it`, and invalid regexes are refused before a run.
- **Equivalent survivors.** I checked all 8 by reasoning about the regex [Inferred: a deductive
  argument from the literal, not a corpus sample]:
  - **`arm1-drop-{agent,bot,service,system,ci,pipeline,model}`** (7): for each such word `w`,
    arm 1's branch accepts exactly the strings that start (case-insensitively, since one `/i`
    covers the whole literal) with `w` followed by `:`, `\s`, `-` or end of input. Arm 3 lists
    the same `w` with the same `^` and the class `[\s:/-]|$`, which contains every member of
    `[:\s-]|$`. No word in arm 1 is a prefix of another, so deleting `w` from arm 1 removes only
    strings that arm 3 still accepts. The language is unchanged, so no owner of any length can
    kill these mutants.
  - **`arm3-drop-claude`**: arm 3's `claude` branch accepts `claude` at input start, followed by
    `\s`, `:`, `/`, `-` or end. Those are all non-word characters, and the start of input is
    followed by the word character `c`. So `\b` holds on both sides and arm 2,
    `\b(claude|…)\b`, accepts the same string. Again the language is unchanged.
  - **The corpus.** For every word, it carries the suffixes `:`, `: x`, ` x`, `-x`, `-`, `-7`,
    `/`, `/x`, ` `, plus the non-members `_x`, `.x` and `ha`, in three casings. So it would hold
    a distinguishing separator form if one existed. Zero differing strings is what equality
    predicts.
  - **Killable by a short owner the PR omitted?** None of the 8 is.
  - Observation, not a finding: arm 1's seven shared words are redundant with arm 3. That is
    the cost of act-fields.ts:30–32's "verbatim" union, and removing them would not change the
    language.
- **Redundancy:** after the slash owners landed, the first six owners are redundant for every
  single-arm mutant. They still carry section 3H's both-arms mutants, which is what the bead
  asked for. N3 covers the comment.
- **`compare_test_lists.py`** writes `~0` as a constant. That is correct here only because
  `removed` = 0: a changed test would appear as one removal plus one addition.

## 8. Cleanup

- [Observed] I removed the scratch clone at
  `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/rev-504/clone`,
  together with its base worktree `rev-504/base`. Section 3I's `git status` checks were taken
  first.
- What remains under `rev-504/` is this raw, the reviewer scripts under `tools/`, the re-run
  records `rerun-before.json` (sha256 `f6727a3b…`) and `rerun-after.json` (sha256 `69838a45…`),
  the four check outputs, and `rederived.diff`.
- No edit was made under `/home/tze/GitHub/syzygy` or its `.worktrees/`. No `bd` mutation, push,
  PR comment or merge.
