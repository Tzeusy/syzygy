# R-GP-IMPL-ADAPTER-CREDENTIALS-1 — CC-REV-1 implementation review of syzygy-bpyt.8.9, round 1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 4cd9a511
Subject: r1-review.diff sha256 a63d5501d0c518a6e67baf1ba3537b3a357bf427902d4320e44fe6e96d6ce88d

Reviewer: a fresh-context CC-REV-1 reviewer for class 4 (security). I did not write the change and did not change it. I fetched no
target-repository content, read no observed repository body, and opened no real credential file; the Claude Code login path is
reasoned about from `polaris.ts` alone. Every harness and mutant ran in scratch clones under the brief's `rev-499/` directory, now
deleted. I ran no bd mutation, did not push, comment on the PR or merge, and edited no worktree under `.worktrees/`.

## 1. Subject identity checks

- [Observed] `sha256sum` of the brief's subject file: `a63d5501d0c518a6e67baf1ba3537b3a357bf427902d4320e44fe6e96d6ce88d`.
- [Observed] In a clone of `/home/tze/GitHub/syzygy`, `git fetch https://github.com/Tzeusy/syzygy.git agent/syzygy-bpyt.8.9` gives
  `FETCH_HEAD` = `4cd9a5119ca18e0f852cda24d8be5a466ad04269`. `gh pr view 499 --json headRefOid` gives the same commit, base `main`.
- [Observed] `git merge-base 4cd9a511 origin/main` = `32c16625e3a14e6db995adff81379cf32baf49c3`.
- [Observed] `git diff 32c16625… 4cd9a511… --output=rederived.diff`, then `sha256sum`: `a63d5501d0c518a6e67baf1ba3537b3a357bf427902d4320e44fe6e96d6ce88d`.
  **It matches the brief's digest.** `--stat`: 7 files, 8273 insertions, 11 deletions.
- [Observed] Two commits: `72cf9c4b` (the 4 source files) and `4cd9a511` (only the 3 `docs/evidence/` JSON files). So the sources at
  `72cf9c4b`, where the evidence was made, are the sources at the reviewed commit. `sha256sum` at `4cd9a511`:
  `credential-probe.ts` `0c5e699f…02ff5`, `execution-rule.ts` `5a9163a9…30b08`, `index.ts` `9a664c60…5421a`. All three equal the
  `subjectSha256` rows of the differential record, and `credential-probe.ts` equals the mutants record's row.
- [Observed] Nothing under `.syzygy/**` or `openspec/**` changes. The 7 paths are 3 under `docs/evidence/` and 4 under
  `packages/polaris-dossier/src/`.

## 2. Clauses relied on (quoted)

- **GP-Q0** (`OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md:95-96`): "Any change not listed here to what a gate accepts or
  refuses stops and returns to the owner." Part 1 (`:52-55`): behavior-preserving means none of "a rendered byte, a wire format, a
  refusal string or an exit code", nor "a consent, security or retention decision". Review rule (`:62-66`): class-4 PRs get "an
  old-versus-new differential over a mutated-record corpus that includes records with altered prose; a rule-6 mutant for each
  predicate; a non-blocking owner notice in the cycle report."
- **GP-Q7** (`:128`): "Signing it enables the execution-permitting arm of `packages/polaris-dossier/src/execution-rule.ts`. The flag
  flips only after the implementation is verified to disclose what REQ-polaris-generation-033 requires, and after a CC-REV-1 class-4
  review." `:129`: "Once signed, SEC-3's credential clause binds. Under the accepted note N2, that is permanent once Syzygy holds a
  credential." `:132-134`: "Separate beads cover: - the stale unlock comment on the flag; - a credential list that fails closed when
  a configured adapter declares a credential the list lacks."
- **The note GP-Q7 came from** (`docs/reviews/R-GREENFIELD-PARITY-PACKET-2-RAW.md:136`): "The real risk is that the hand-kept list
  goes stale once Syzygy holds a credential. Fail closed when any configured adapter declares a credential missing from the list, or
  derive the list." The hand-kept list is `CONFIGURED_ADAPTER_CREDENTIALS`.
- **SEC-3** (`DIRECTIVE-REGISTER.md:49` routes to `.syzygy/governance/doctrine/security.md:61`). Credential bullet (`:87-89`):
  "Syzygy keeps every credential it holds for its typed adapters where neither the session nor any process it starts, directly or
  not, can read it at the operating-system level, for as long as any of them runs." Whom it binds (`:90-91`): "Syzygy never gives
  the instruction to a session it started or to one left running unattended". Cost (`:95-97`): "the session runs with the owner's
  own credentials and network, including Syzygy's endpoints and any Syzygy credential readable on that host."
- **CC-SEC-3** (`DIRECTIVE-REGISTER.md:98` routes to `.syzygy/governance/policies/craft-and-care/security-and-secrets.md:63`),
  `:68-70`: "Until the execution-profile RFC is accepted: no observed-project code executes, period".
- **REQ-polaris-generation-033** (`openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:19`): "Syzygy
  SHALL NOT, from the issue of a brief that permits execution, hold or write a typed-adapter credential where the operator's user can
  read it, and SHALL, before it issues such a brief and at every later step it takes for the run (each check, inventory check, review
  check and render, and close), attempt as the operator's user to read every credential that Syzygy holds for its typed adapters."
  Its falsifier (`:215`) includes: "a credential read is skipped at a check, inventory check, review check, render or close after a
  permitting brief".
- **Doctrine on adapters.** `doctrine/README.md:53-54` lists among the substrates "**the `/th-*` skills and claude/codex CLIs** —
  the agent toolchain for workers and actuators". `doctrine/architecture.md:168`: "**Substrate tools are adapters, not doctrine.**"
  Doctrine defines no "typed adapter" term [Observed: `grep -i -F 'typed adapter'` over `doctrine/` gives 4 lines, none a definition].
- **The bead** (`bd show syzygy-bpyt.8.9`). Acceptance criteria: "1. Comment names the CC-SEC-3 gate. 2. Probe refuses on a
  declared-but-unlisted credential; fixtures cover it. 3. Rule-6 mutant recorded."
- **AGENTS.md** verification rules 2, 4, 6, 9 and 11, and "No evidence yields Unknown — never green, never zero (VIS-2)."

## 3. What I ran and the results

Head clone at `4cd9a511`, base clone at `32c16625`, `npm ci` in each (exit 0).

1. `vitest run packages/polaris-dossier/src/credential-probe.test.ts` (head): "Tests  32 passed (32)". (One run by mistake in the main
   checkout, which is at the base, gave "Tests  24 passed (24)". It ran read-only and changed nothing.)
2. `vitest run --project @syzygy/polaris-dossier` (head): "Test Files  29 passed (29)", "Tests  1183 passed | 1 skipped (1184)". No
   timeouts.
3. `npm run typecheck` (head): `tsc -b …` printed no diagnostics, "[exited with code 0]".
4. `python3 scripts/check_governance.py` (head): "32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted".
5. `python3 scripts/check_quotations.py` (head): "OK    QC-1  a quotation beside a path:line locator was said by that file — 33
   quotations examined in 15 of 916 .md files scanned (loc-paren-quote 2, loc-colon-quote 21, quote-paren-loc 10), 0 findings".
6. `vitest run apps/three-surface-poc/src/polaris-authority-sweep.test.ts` (head): "Tests  5 passed (5)".
7. **The differential, re-run from the record.** I wrote `harnessSource`, `driverSource` and `builderSource` out of the tracked
   record, under the names the driver reads. The extracted harness hashes to the recorded `harnessSha256`
   (`94df4440…1c06f14d`). Then `drive.py <head clone> 32c16625… <scratch> raw.json` printed "done 154 154", and
   `build_differential.py` printed `{"cases": 154, "unchanged": 91, "stricter": 18, "refusalReasonChanged": 45, "moreLenient": 0,
   "otherChange": 0, "casesWithNoUnlistedDeclaration": 91, "ofThoseUnchanged": 91, "casesWithAnUnlistedDeclaration": 63,
   "ofThoseNewRefusesWithTheDeclarationReasonAloneReadingNothing": 63}`. The re-run rows equal the tracked record's rows
   (`rows equal True`), and so do the subject digests. Only `fix` differs: `4cd9a511` against `72cf9c4b`, the same source bytes.
   The tree was clean before and after.
8. **My own checks over the re-run rows.**
   - In all 147 fixture rows, the new read attempts are a subset of the base's, and the new list reads are at most the base's.
   - 26 rows pass under the new code, and all 26 also pass at base. 44 pass at base.
   - The 7 CLI-shaped rows are all unchanged.
9. **The recorded mutants, re-run.** I extracted `mutants.py` from the record and ran it on the head clone: "summary {'planned': 13,
   'killed': 13, 'allRestored': True}". Each mutant's `old` and `new` fragments equal the record's, and so does its set of failed
   tests (durations stripped). None was blocked by timeout. Unmutated run: "Tests  32 passed (32)". Tracked tree clean before and
   after.
10. **My own mutants** (`credential-probe.ts`; one exact fragment replaced; restored, and the digest re-checked `0c5e699f…`):
    - R1, the operator list satisfies a declaration. `old`: `credentials.filter((file) => !configured.includes(file))`. `new`:
      `credentials.filter((file) => !configured.includes(file) && !(() => { const l = source.list(); return l.ok && l.paths.includes(file); })())`.
      **Killed**: "Tests  2 failed | 30 passed (32)" ("is not satisfied by the operator-declared list holding the path"; "refuses a
      declared credential the list does not hold, before reading …").
    - R2, case-folded membership. `new`: `credentials.filter((file) => !configured.map((c) => c.toLowerCase()).includes(file.toLowerCase()))`.
      **Survived**: "Tests  32 passed (32)".
    - R3, trimmed membership. `new`: `credentials.filter((file) => !configured.includes(file.trim().replace(/\/+$/, '')))`.
      **Survived**: "Tests  32 passed (32)".
    - R4, an adapter named `''` skipped. `old`: `adapters.flatMap(({ adapter, credentials }) =>`. `new`:
      `adapters.filter(({ adapter }) => adapter !== '').flatMap(({ adapter, credentials }) =>`. **Survived**. This mutant is
      contrived, and I do not count it as a finding.
11. **The head test file run against the base probe.** I copied the head test file into the base clone and ran it, then restored it:
    "Tests  6 failed | 26 passed (32)". The 6 that fail are the new tests other than "probes as before …" and "changes nothing …",
    as the PR says.
12. **Test name sets** (`vitest list --json`, base against head, over `credential-probe.test.ts`): "base 24 head 32 added 8 removed
    0". The diff of the test file has 73 added lines and 0 removed. This confirms `Tests: +8 ~0 -0`.
13. **The sweep, re-derived by my own script.** I ran Python `re` with the record's `linePattern` over `git ls-tree -r -z HEAD --
    packages apps`, keeping non-test `.ts/.mts/.cts/.js/.mjs/.cjs`: "sources 233 hit files 47 class rows 47 distinct 47". The six
    classes partition the 47 exactly ("hit minus classes []", "classes minus hit []"). The recorded `hitLines` file set is equal.
14. I did not re-run the PROJECT-STATUS canonical battery. [Unknown] The battery at `4cd9a511` rests on the implementer's report
    ("commands=110 nonzero=0").

## 4. Findings

No blocking finding.

### N1 — medium, latent until the flag flips. A declaration refusal skips the step's credential reads and hides a readable credential

- **Evidence.**
  - [Observed] `credential-probe.ts:141-145` returns before `source.list()` (`:146`) and before any `open` (`:153`).
  - [Observed] Differential row "lists-readable / configured readable / adapters declares-an-unlisted-path":
    - Base: `why` "adapter credentials readable by the operator's user: /f/listed-readable.token, /f/configured-readable.token",
      with both paths opened.
    - New: the declaration reason only, with `opens: []`.
    - Of the 45 rows whose reason changed, 21 had a base reason "adapter credentials readable by the operator's user" and 6 "the
      read attempt could not decide for". In all 27, an observation the base made is no longer made.
  - [Observed] REQ-033 (`spec.md:19`) requires a read "at every later step", and its falsifier (`:215`) names "a credential read is
    skipped at a check, inventory check, review check, render or close after a permitting brief".
- **Reachability.**
  - [Observed] Unreachable at `4cd9a511`. `PERMITTING_ARM_ENABLED = false` (`execution-rule.ts:17`), so no permitting brief exists,
    and `CONFIGURED_ADAPTER_DECLARATIONS` is empty.
  - [Inferred] After the flip, brief issuance runs the probe (`execution-rule.ts:125`) and would refuse a mismatched configuration.
    So the refusal can fire after a permitting brief only if the compiled constants change between the brief and a later step: a
    Syzygy rebuild or upgrade in the middle of a run.
  - [Observed] Base already has the same pattern for a failing list source. `:147` returns before `configured` is read, and the list
    file is within the agent sessions' write reach.
- **Failure scenario.**
  1. After the flip, the owner's run gets a permitting brief from build N.
  2. Build N+1 adds an adapter declaration that is missing from the list.
  3. `syzygy dossier check` refuses. That is fail-closed, and the permission lapses.
  4. But no read is attempted, so a credential the session could read at that instant is never observed or recorded, and the
     REQ-033 falsifier is met.
- **Proposed fix.** A follow-up bead that must close before `PERMITTING_ARM_ENABLED` flips, named in `syzygy-bpyt.1.6`'s "verified to
  disclose what REQ-polaris-generation-033 requires" condition.
  - At every probe, attempt the base's read set: `configured` together with `list.paths` when the list is ok, or `configured` alone
    when it is not.
  - Refuse when either the declaration check or the reads fail, with a reason that carries both.
  - No new read is introduced, because the read set stays the base's.
  - The declaration half sits within GP-Q7's listing. The list-source half changes a pre-existing refusal string, so it needs the
    owner's listing under GP-Q0. The alternative is to put to the owner, in the `syzygy-bpyt.1.6` packet, the reading that a
    fail-closed refusal without reads satisfies REQ-033.

### N2 — medium, latent. A non-read refusal renders as an Observed readability claim

- **Evidence.**
  - [Observed] `render.ts:605` renders every failed probe as "At this render an adapter credential was readable as the operator's
    user: ${credential.finding.why}. …" with `label: 'Observed'`.
  - [Observed] `credential-probe.ts:191` gives every failure the kind `adapter-credential-readable`.
  - [Observed] So a declaration refusal, where no read was attempted, would render as an Observed claim that a credential was
    readable.
  - [Observed] The PR's residual 4 discloses the same thing for list-source refusals. This PR adds a new trigger.
- **Failure scenario.** As in N1, with the render step: the dossier states, labelled Observed, that a credential was readable, when
  nothing was read. That is the VIS-2 "No evidence yields Unknown" failure.
- **Proposed fix.** An owner-listed change, before the flip, since it changes rendered bytes and a wire value: give configuration
  refusals (list source, declaration) their own finding kind and render text, not labelled Observed. Add it to the same pre-flip
  verification as N1.

### N3 — medium, routed to the owner through `syzygy-bpyt.1.6`. The Claude Code login copies need an owner ruling, not a stated classification

- **Evidence.**
  - [Observed] `polaris.ts:338-345` copies `~/.claude/.credentials.json` into `<stateRoot>/<runId>.agents/<role>/.claude/.credentials.json`
    with mode 0600, for each session Syzygy launches.
  - [Observed] `git grep -n -F '.agents' HEAD -- packages apps` gives 2 lines, both creators (`polaris.ts:340`, `:353`). No tracked
    implementation source removes the directory. [Inferred] The copies persist after the run.
  - [Observed] The new comment at `credential-probe.ts:123-124` states, unlabelled, that "no implementation source in `packages/` or
    `apps/` holds a typed-adapter credential path". The sweep record labels the same judgement "Inferred not a typed-adapter
    credential". The sibling comment at `:110-111` names its one exclusion (the cap1 `machine-credential.token`), but this comment
    does not name this one.
- **Judgement against SEC-3's text.** [Inferred] The classification is defensible for the attended session's own login. The cost
  bullet accepts "the owner's own credentials". It is contestable for copies that Syzygy itself writes and keeps for sessions it
  launched:
  - SEC-3 binds "every credential it holds for its typed adapters".
  - Doctrine lists the claude CLI as a substrate and says "Substrate tools are adapters".
  - REQ-033 forbids Syzygy to "hold or write a typed-adapter credential where the operator's user can read it" once a permitting
    brief is issued.
  - Doctrine does not define the term. Settling it is a security-posture decision, which belongs to the owner.
- **Before merge, or as a note?** As a note, but as an owner question in the packet. This PR neither declares nor excludes the copies
  in behavior, and its outcomes are unchanged. The arm is off, and SEC-3's credential clause binds only on the CC-SEC-3 sign-off
  (GP-Q7 `:129`), so that sign-off is the decision point. [Inferred] Launched runs never carry the permission (`security.md:90-91`
  and the launched marker), so the copies matter through their persistence on a host that later runs an attended session.
- **Failure scenario.**
  1. The owner signs CC-SEC-3 after reading a packet that calls the copies "the session's own login" as fact.
  2. If they are typed-adapter credentials, Syzygy already held one at signing, and N2 made the clause permanent at that moment.
  3. The list then omits them, and they are readable by the operator's user. On every host where `syzygy polaris` has run, the
     probe should refuse until the copies are removed.
- **Proposed fix.**
  - `syzygy-bpyt.1.6` presents this as an owner question with both arms and their consequences. If they are typed-adapter
    credentials: the list names them, the probe refuses while they are readable, and cleanup or relocation is required. If they are
    not: the packet records the ruling and its reason.
  - A comment-only follow-up qualifies `credential-probe.ts:123-124` in the style of `:110-111`. It names the `polaris.ts:343-345`
    copy, labels the classification Inferred, and points at the ruling.

### N4 — low. Exact membership is pinned only against `path.normalize`

- **Evidence.** [Observed] Mutants R2 (case-folded) and R3 (trimmed, trailing slash dropped) survive (section 3, item 10). Only D4
  (normalized) is killed, by `/x//a.token`.
- **Failure scenario.** A later refactor compares paths case-insensitively or trims them. On a case-sensitive file system, a
  declaration `/X/A.token` is then "held" by a listed `/x/a.token`, the probe reads only `/x/a.token`, and the declared credential
  goes unprobed while every test stays green.
- **Proposed fix.** Extend "refuses a declaration the list spells differently: membership is exact" with three declarations against
  `configured` = `['/x/a.token']`: `/X/A.token`, `/x/a.token/` and ` /x/a.token`. Each expects the refusal naming the declared
  spelling. Re-run R2 and R3 with the fragments above and record them killed.

### N5 — low. The declaration list is a second hand-kept constant beside the list it guards

- **Evidence.**
  - [Observed] `CONFIGURED_ADAPTER_DECLARATIONS` (`credential-probe.ts:125`) sits in the same file as `CONFIGURED_ADAPTER_CREDENTIALS`
    (`:113`). Neither adapter-registry entry has a credential field: 2 files, 2 entries, by JSON count and by `git grep -c -F
    '"observerId"'`.
  - [Observed] The PR's residual 1 discloses this.
- **Failure scenario.** The first credential-holding adapter is added without editing `CONFIGURED_ADAPTER_DECLARATIONS`. The list then
  goes stale silently, which is the bead's stated outcome failing.
- **Proposed fix.**
  - When the first such adapter lands, its module exports its own `AdapterCredentialDeclaration`, and `CONFIGURED_ADAPTER_DECLARATIONS`
    is built from the adapter modules, or from a registry field. A test asserts that every implementation source opening a credential
    path is represented.
  - `syzygy-bpyt.1.6` states this residual in plain words, because N2 makes the list's completeness load-bearing.

### N6 — low. The rendered disabled reason now disagrees with the comment above it

- **Evidence.** [Observed] `execution-rule.ts:18`, which is rendered into every brief through `notPermittedBecause` (`:96`), still
  says "it stays off until the execution choice (`syzygy dossier allow-execution`) and the adapter-credential probe (syzygy-qkea.5)
  are merged and the arm is switched on". `:16` now names the CC-SEC-3 sign-off. The PR's residual 3 discloses this, and it correctly
  leaves the string, since GP-Q0 Part 1 makes it a rendered byte.
- **Failure scenario.** A brief reader is told the gate is a merge that happened in PR #380.
- **Proposed fix.** Put the rewording to the owner as a listed output change, in the `syzygy-bpyt.1.6` packet or the flip bead.

### N7 — low, process. Authority citation and owner notice

- **Evidence.**
  - [Observed] The PR body ties the refuse-more change to "(GP-Q0 part 3)". Part 3's table (`:85-93`) does not list 8.9. GP-Q7
    (`:132-134`) does.
  - [Unknown] Whether the GP-Q0 "non-blocking owner notice in the cycle report" (`syzygy-bpyt.10`) has been made for this class-4 PR.
- **Proposed fix.** The dispositions record cites GP-Q7 `:132-134` as the listing that authorizes the new refusal, and confirms the
  cycle-report notice.

## 5. Every changed outcome

- **Production configuration: 0 changed outcomes.**
  - [Observed] All 6 production calls of `createCredentialProbe` are `cli.ts:233,244,276,309,322,353`, each `createCredentialProbe(credentialListFromEnv(env))`.
    Method 1: `git grep -n -F 'createCredentialProbe' -- packages apps scripts`. Method 2: my Python scan of all 3000 tracked files,
    counted twice (`git ls-files -z` and `git ls-tree -r -z`), with a paren-matched argument count. Both give 6 calls, `args=1` each.
    The only other match is the definition at `credential-probe.ts:132`.
  - [Observed] Both defaults are `Object.freeze([])` (`:113`, `:125`). The test asserts both at run time, so `unlisted` is `[]`, and
    the remaining path is the base code.
  - [Observed] The one reordering (`described` is computed before `source.list()`) reads only `source.describe`, a plain string
    property in both production sources (`:63`, `:98`), and `configured.length`.
- **The differential's 154 cases** (re-derived, section 3, items 7 and 8):
  - 91 unchanged: all 84 fixture cases with no unlisted declaration, and all 7 CLI-shaped cases.
  - 18 stricter, base pass to new refuse. These are the sources `empty`, `lists-absent` and `lists-the-declared-path`, crossed with
    configured `none` and `absent`, crossed with the shapes `declares-an-unlisted-path`, `two-adapters-mixed` and
    `declares-a-respelled-path`: 3 × 2 × 3.
  - 45 with the refusal reason changed: the 3 passing sources with configured `readable` (9), then `lists-readable`,
    `lists-undecidable`, `malformed` and `unset` (9 each).
  - 0 other.
- **More lenient: 0 of 154.** It is also 0 by construction [Observed]: when `unlisted` is non-empty the probe always refuses, and when
  it is empty the probe runs the base code. No input reaches a read the base would not reach, because declarations never enter
  `paths` (`:148`).

## 6. Verdict per acceptance criterion

- **Bead AC 1 (comment names the CC-SEC-3 gate): met.** `execution-rule.ts:16` names the amendment (`syzygy-bpyt.1.6`, GP-Q7) and
  both flip conditions, matching GP-Q7 `:128`. It replaces one line with one line, so every line locator holds.
  `check_quotations.py` reports 0 findings.
- **Bead AC 2 (refuses on a declared-but-unlisted credential; fixtures cover it): met.** See the 8 new tests and section 5.
- **Bead AC 3 (rule-6 mutant recorded): met.** 13 of 13 killed, reproduced exactly. N4 adds two survivors on one predicate.
- **Refuse-more only, inside GP-Q7's listing, nothing more lenient: met.** The new refusal is exactly the round-2 packet review's note 7, "fail
  closed when any configured adapter declares a credential missing from the list", with the list read as the hand-kept
  `CONFIGURED_ADAPTER_CREDENTIALS`. Nothing else changes (see N7 for the citation). The refusal runs before the list read and before
  any open. No input reaches a read the base would not.
- **"No outcome changes today": true.** Swept as in section 5, by two methods with denominators: 6 calls, 2 registry entries and 2
  constants. Also 47 of 233 implementation sources match the credential pattern, partitioned exactly into the six recorded classes.
- **Exact membership (operator-list paths do not satisfy a declaration): sound and pinned.** It matches the source note: the operator
  list is within the agent sessions' write reach. The rule is pinned by "is not satisfied by the operator-declared list holding the
  path" and killed mutant R1. Exactness itself is partly pinned (N4).
- **The `polaris.ts:338-345` classification: a note, not REVISE** (N3). It must reach the owner as a question in the `syzygy-bpyt.1.6`
  packet before CC-SEC-3 is signed, not before this merge.
- **The `execution-rule.ts` comment: accurate; locators hold.** The stale rendered string is N6.
- **Test soundness and the evidence claims: met** (section 7).

## 7. Test quality

- **Expected values are literals.**
  - [Observed] The refusal prefix, the `last()` sources and the empty-list disclosure string are written out, not imported.
  - The repository-constant test imports the constant under test, which is the subject itself.
- **Fixtures cannot fake a kill.**
  - [Observed] The describe-time fixtures (`REFUSAL`, `counted`, `opens`, `absent`) call no module code, so a mutant cannot throw at
    describe time.
  - The mutants harness counts a kill only on a non-zero exit with named failed tests, or on a timeout (none occurred). A file that
    throws at import would score as survived, not killed.
- **Ordering and side effects are asserted directly.**
  - [Observed] Ordering is asserted by list reads = 0 and opens = [].
  - The pass path is asserted with an injected open and a real 0600 file.
  - `opens` is cleared `afterEach`.
- **No test passes for the wrong reason, so far as I found.**
  - [Inferred] The 2 tests that pass at base are pass-path pins, as stated.
  - The 6 that fail at base fail on the new refusal (section 3, item 11).
- **Equivalence and leniency claims hold.**
  - [Observed] The mutants record claims no equivalent mutant.
  - The differential's "0 more lenient" and "91 of 91 unchanged" hold on re-run.
  - The corpus's altered-record variants are a respelled declaration, a malformed list (fixture and file), a missing file and a
    directory entry. [Inferred] It omits the list validator's wrong-format, extra-key and relative-path files, but that code is
    unchanged and every CLI call omits declarations, so they are identical by construction.
- **The evidence is re-runnable from what the records store (rules 6 and 11).**
  - [Observed] Each record names its subject paths and sha256, the commit, the command and the embedded sources.
  - The mutants record stores each `old`/`new` fragment.
  - I re-ran the differential and mutants from the embedded sources alone.
  - One gap: the differential's `command` does not say that the harness must be saved as `harness.test.ts` beside `drive.py`; that is
    readable only from the driver source.
- **Freeze depth.** [Observed] `Object.freeze` on `CONFIGURED_ADAPTER_DECLARATIONS` is shallow. Entries added later would carry
  mutable `credentials` arrays unless they are frozen too. The constant is not exported from `index.ts`, so the reach is
  package-internal.

## 8. Cleanup

The head clone, base clone, extracted harnesses, my scripts, `vitest list` outputs and the re-derived diff under
`/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/rev-499/` are deleted. Only this raw remains.
Before deletion, the head clone's tracked tree was clean (`git status --porcelain --untracked-files=no` printed nothing), and the
base clone's test file was restored with `git checkout`.
