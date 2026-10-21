# R-GP-IMPL-CAP1-DEAD-PLANES-1 — CC-REV-1 implementation review of syzygy-bpyt.7.2, round 1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 9a6b308e
Subject: r1-review.diff sha256 bb903636b35dc6c5bed53aaab427e6d1a2ff9d64abb8a37a62c6ccebf7d2683e

Reviewer: independent fresh-context CC-REV-1 reviewer (Claude Opus 5.5), 2026-10-22. I read no
body of Butlers or of any other observed repository. All fixtures used below are synthetic
(the cap1-system harness fixture and my own mutations of it).

## 1. Subject identity checks

- [Observed] `sha256sum r1-review.diff` →
  `bb903636b35dc6c5bed53aaab427e6d1a2ff9d64abb8a37a62c6ccebf7d2683e`. **Matches** the brief.
- [Observed] In a fresh scratch clone, `git fetch https://github.com/Tzeusy/syzygy.git
  agent/syzygy-bpyt.7.2` gave `FETCH_HEAD` = `9a6b308ee2adf4fa26aafcad6c310b6f37b2f711`, and
  `gh pr view 498 -R Tzeusy/syzygy --json headRefOid` returned the same commit.
- [Observed] `git merge-base 32c16625… 9a6b308e…` = `32c16625e3a14e6db995adff81379cf32baf49c3`.
- [Observed] `git diff 32c16625… 9a6b308e… | sha256sum` →
  `bb903636b35dc6c5bed53aaab427e6d1a2ff9d64abb8a37a62c6ccebf7d2683e`. **Matches** the subject
  file. `--stat`: "64 files changed, 5783 insertions(+), 1385 deletions(-)"; name-status
  22 A, 2 D, 40 M.
- [Observed] Paths under `.syzygy/` or `openspec/` in the diff: 0 of 64, by two methods
  (`grep -c -E '^(\.syzygy|openspec)/'` over `--name-only`, and `git diff --name-only … --
  .syzygy openspec | wc -l`).
- [Observed] The evidence record names code commit `b17e94ba…` and base `e26a615d…`, not the
  reviewed pair. `git diff --stat` over `packages/cap1-core packages/cap1-daemon
  packages/cap1-conformance packages/cap1-system apps/syzygy vitest.config.ts package.json
  package-lock.json` is empty both for `b17e94ba..9a6b308e` and for `e26a615d..32c16625`. So
  the measured cap1 bytes are the reviewed cap1 bytes on both sides. The merge brought in only
  `three-surface-poc-core` work, one review raw and one script change from main.

## 2. Clauses relied on (quoted)

- **GP-Q0, Part 1** (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md:52-55`):
  "'Behavior-preserving' means none of the following changes: a rendered byte, a wire format, a
  refusal string or an exit code; a signed or digest-bound artifact; a consent, security or
  retention decision."
- **GP-Q0 review rule** (same file, :62 and :67): the three further checks apply to "pull
  requests touching class 1 (authority boundaries), class 3 (deterministic observation) or
  class 4 (security)". The beads known to touch a class include "`7.2`".
- **GP-Q0, Part 3, the 7.2 row** (same file, :89): "Paths are normalized before the
  `startsWith` check, if `write-guard.ts` is kept. This narrows what `authorizeWrite` accepts".
  Then :95-96: "Any change not listed here to what a gate accepts or refuses stops and returns
  to the owner."
- **2026-10-20 direction** (`OWNER-DIRECTION-GREENFIELD-PARITY-SIMPLIFICATION-2026-10-20.md:80-81`):
  "It authorizes no new behavior. A change that would alter behavior is out of scope, even when
  it is simpler, and goes to the owner."
- **What the owner was told about 7.2** (`docs/reviews/R-GREENFIELD-PARITY-PACKET-2-RAW.md:59`):
  "`7.2` deletes or fixes `write-guard.ts` and `write-boundary.ts` (the write universe, CC-REV-1
  class 1)."
- **CAP1-REQ-061** (`openspec/changes/project-registration-and-honest-shape-visibility/specs/project-registration-and-honest-shape-visibility/spec.md`).
  The heading is at :1785: "Capability 1 observes and presents; its write boundary is the
  governed plane". The form is **prohibition** (:1787). Clause text, :1789-1795: "Capability
  1's behavior SHALL cause no mutation beyond governed proposals and Syzygy-owned presentation
  or specification artifacts inside `openspec/**` and `.syzygy/**` where accepted authority
  permits them. … no manifest field may widen that write universe: a field purporting to do so
  is inoperative and renders as a contradiction routed to the owner." Sweep, :1801: "record all
  writes and effects **externally to Syzygy**". Oracle independence, :1813-1815: "the effect
  population is established by the harness's own tracing over interfaces it controls, never
  solely by Syzygy's self-report".
- **CAP1-REQ-023** (same spec, :779-781): "Serving, maintaining, or drafting the human entry
  SHALL NOT cause Syzygy to write outside its two direct-write namespaces". Observable, :788-790:
  "the write record — captured **externally to Syzygy** by the checking harness". CAP1-REQ-053
  (:1713-1716) has the same form. These are the other two requirements the deleted module's
  header named as context.
- **CAP1-REQ-046** (same spec, :1501 and :1505-1511): "For every answer resting on a governance
  artifact, Syzygy SHALL expose the artifact's owning authority and governing revision, and
  SHALL distinguish the artifact's self-declared lifecycle stamp (untrusted content) from its
  effective status (derived from the owner-act record)."
- **CAP1-REQ-011** (same spec, :363-366), for one out-of-scope observation (N7): "the consent
  state Syzygy serves SHALL derive only from such records: their scope, attribution, and grant
  state render with the coverage boundary."
- **CC-REV-1** (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md`):
  "the agent performing the change never finally decides which classes it touches"; class 1
  "authority boundaries — write-universe"; class 4 "security — anything under SEC-1…SEC-5".
- **SEC-4** (`.syzygy/governance/doctrine/security.md:112-114`): "Writes are consented,
  attributed, and revertable. Syzygy writes into a governed repository only with recorded
  consent".
- **The deleted module's own decision text** (base `packages/cap1-daemon/src/write-guard.ts:12-17`):
  "Known core defect this module closes … core `authorizeWrite` compares the RAW candidate with
  `startsWith` … this guard is the one sanctioned runtime write path."
  `docs/reviews/R-RT-RUNTIME-REVIEW.md:29` says: "write-guard.ts is unreachable in
  Capability 1. … The daemon performs NO governed-plane writes … so the module is
  forward-defense exercised only by unit t[ests]".
- **Bead `syzygy-bpyt.7.2`**: "if the requirement is satisfied by the absence of writes and its
  oracle is external …, delete both and close the tracked startsWith issue as moot; if the spec
  requires an in-process boundary, keep it and fix startsWith (normalize first). Record which."
  It also says: "The authority-exposure plane is tracked nowhere: if a CAP1 requirement
  mandates it, it is a gap (file a gap candidate under u2a)".
- **AGENTS.md** rules 2, 4, 6, 9, 10 and 11, and the guardrail "Conformance expected values are
  hard-coded literals, never imported from the module under test."

## 3. What I ran, and the results

All runs were in my scratch clones: `clone` at `9a6b308e` and `base` at `32c16625`, each after
`npm ci`.

| Run | Result (verbatim where quoted) |
|---|---|
| `npm run typecheck` (head) | exit 0 |
| `npx vitest run --project @syzygy/cap1-conformance --project @syzygy/cap1-daemon` (head) | "Test Files  53 passed (53)" / "Tests  425 passed (425)". There is no `cap1-core` vitest project in `vitest.config.ts`; cap1-core has no test files of its own. Its tests are the conformance project. |
| `SYZYGY_FRESH_CLONE=1 npm run test:system` (head) | "Test Files  9 passed (9)" / "Tests  48 passed (48)". This includes "✓ RT6 — fresh-clone demonstration > a fresh clone installs, builds, starts the daemon, and serves the same facts on both channels" and "✓ RT6 — write boundary by harness-external filesystem observation > after requests to all routes, the only filesystem additions live under the state dir and the governed tree is untouched". `sweepWireParity` is called in `fresh-clone.system.test.ts:113` and `full-facts.system.test.ts:126`. |
| `npx vitest run` (head, full) | "Test Files  229 passed \| 3 skipped (232)" / "Tests  4895 passed \| 5 skipped (4900)" |
| `npx vitest list` (full), base vs head, sorted multisets | 4924 vs 4902 lines. 22 only at base and 0 only at head. All 22 are `[@syzygy/cap1-daemon] packages/cap1-daemon/src/write-guard.test.ts`. The PR's 4919/4897 were measured at `e26a615d`/`b17e94ba`; the +5 on both sides is main's merged work. |
| `npx vitest list --project @syzygy/cap1-conformance`, base vs head | 312 and 312 lines. Sorted lists byte-identical, sha256 `3d8a68103c582ffe5ae202ac1a017cbf95fc6e41d9c0d09cb19215a998bb9188` both, which equals the PR's figure. 312 distinct names. |
| `python3 scripts/check_quotations.py`, base vs head | exit 0 both. Output byte-identical (`cmp`). First line: "OK    QC-1  a quotation beside a path:line locator was said by that file — 33 quotations examined in 15 of 916 .md files scanned … 0 findings" |
| `python3 scripts/check_governance.py`, base vs head | exit 0 both. 32 OK and 21 WARN at head; 0 lines start `FAIL`. Diff vs base: the file-scope line (2997 → 3017), CG-2a (1914 → 1920 files examined, 0 findings), CG-3 (1799 → 1802, 0 findings) and the AGENTS.md word-count WARN details (6845 → 6897 words). CG-1f reads "405 references examined, 0 findings" at both. The PR body's "405 to 401" does not reproduce at the reviewed pair (N3). |
| Route differential: the PR's `route-diff.mjs`, read first, run on base and head | "fixtures=17 responses=272" both. The outputs are byte-identical, sha256 `bebd97b7fdc2aaf906f6327f4e94de90a3fc8622def752d3be8263136006b960` both. This **equals** `evidence.json` `routeDifferential.baseJsonSha256`/`headJsonSha256`. |
| My own probe `rev-498/probe.mjs` (independent corpus, base vs head) | 12 fixtures × 10 routes × 2 auth modes = 240 responses, plus every response header (minus `date` and `keep-alive`), daemon stdout/stderr and exit code. It also records a post-run listing of the fixture tree and the state dir. The fixtures: spec_root traversal, nested `writable_paths`/`deploy_target`, top-level `output_directory`, empty owner, consent reference `../../escape`, unknown grant state, `attribution: agent`, prose comment in a consent record, HTML/traversal text in the entry, README removed, entry removed. The routes: `HEAD`, `OPTIONS`, `DELETE`, `PUT`, `/../.syzygy/project.yaml`, `/%2e%2e/README.md` and four ordinary ones. The mutation helper throws if a target string is absent. "fixtures=12 responses=240" both. The output files are byte-identical, sha256 `c18739834f444c89ecdd61052d511ba0154f457cddbdbeb000bd83c2cc308436` both. Every fixture: `fixtureChanged=false`; state dir holds exactly `machine-credential.token`. |
| Call trace: the PR's recorder (read first), copied into each clone root | Base and head each "Test Files  45 passed (45)" / "Tests  312 passed (312)". 852 calls each, 59 distinct functions. Sorted sha256 `6ae85ec57514c0eb98008c07afa3ee5e60a16e53f4366532a58b6bf09e0a051b` both. This **equals** the stored `calls.sorted`. Sensitivity check: with the builder's `spec_root: openspec/` changed to `specs/` (a change no test sees: "Tests  312 passed (312)"), the trace hashes `318e6e7e…` and 606 lines differ (`comm -3`). The trace detects input changes the tests cannot. |
| Moved-oracle byte check | Base `parity.ts` lines 143-422 vs head `parity-oracle.ts` lines 14-end: `diff` empty, 280 = 280 lines. **Verbatim.** |
| Comment-only check | Non-comment changed lines in `credentials.ts` and `write-boundary.ts`: **0**. Every changed line starts `//`. `credentials.ts` numstat "9 9": each hunk replaces n lines with n, so line numbers are preserved. |
| My reviewer mutants (`rev-498/mutant.py`, file restored byte for byte, `git status` clean after) | **R1** makes `main.ts` append to the fixture `README.md` at startup. `write-boundary.system.test.ts`: "AssertionError: expected [ 'fixture/README.md' ] to deeply equal []". **Killed.** **R2** makes `parity-oracle.ts` `fullDisclosure` return `[]` for the machine channel. It fails, among others, "RT4 — … cross-channel parity" and four "CAP1-REQ-041" tests. **Killed.** |
| Base-side survivor check (`rev-498/base_survivor.py`, base clone, 23 files whose literals moved, restored after) | M01 at base: "replaced 26 occurrences of 'schema_version: \"1\"' -> 'schema_version: \"2\"'", then "Test Files  54 passed (54)" / "Tests  447 passed (447)". M02 at base: "replaced 25 occurrences of 'spec_root: openspec/' -> 'spec_root: specs/'", the same pass lines. **The survivors survive at base too.** |
| PR mutant M03 re-run by me (head; `sed` on `fixtures/index.ts`, restored by `git checkout`, `git status` clean) | "Tests  3 failed \| 309 passed (312)". Failing: REQ-002, REQ-004 and REQ-063 tests only (see N8). |
| Reachability: my import-aware closure (`rev-498/reach_check.py`; only names inside `import {…} from` count) | Head: "scope: 32 non-test .ts files; reached: 27". NOT REACHED: the two barrels, `parity-oracle.ts`, `testing.ts`, `write-boundary.ts`. Base: 31, 27 reached, NOT REACHED: the two barrels, `write-boundary.ts`, `write-guard.ts`. This agrees with the PR's `reach_sweep.py`, which uses a different, name-anywhere predicate. |
| Runtime-export check (`rev-498/runtime_reach.py`) plus `git grep -w` across `packages` and `apps` | `authority.ts` reaches production only by type (`AuthorityExposure`). Its runtime exports `deriveEffectiveStatus` and `artifactInForce` are named in no non-test file but their own: `git grep -l -w … ':!*.test.ts'` gives only `packages/cap1-core/src/authority.ts`. The same holds for `epistemicMarking` and `citeBasis` in `epistemic.ts`. All four are in `syzygy-bpyt.7.7`'s list. |
| Citer sweep of the 42 modified/deleted non-evidence paths (`rev-498/citer_sweep.py`, 2994 text files at head, PR evidence dir excluded) | **Manifest rows** (files with MANIFEST in the name): 0 for every code path. AGENTS.md is cited by 2 round-2026-08c review files with MANIFEST in their names, but AGENTS.md is a row of no `*MANIFEST*.txt`/`manifest*.json`, and its base digest `1780629e…` is cited by 0 files. **Path:line locators**: `write-guard.ts:1-48` in `docs/pursuits/2026-09-22-vision-pursuit-{data,harvest}.json`; `routes-human.ts` lines in the same two files and in `docs/reviews/R-PWB-P63-POLARIS-TRIM-RAW.md`; `credentials.ts` lines in the M11/M12 funnels and their evidence. The pursuit files' current digests are cited by 0 files. The raws are verbatim records. The M12 funnel pins every line number to `a9f671e` by its own stated convention (its digest is cited by its own evidence record; this PR does not edit it). No `credentials.ts` locator falls inside a changed hunk (21-25, 40-48, 128-131). `parity.ts` is named, without lines, by `pwb-scoped-attributes-amendment/IMPACT-LEDGER.md:332` ("Capability 1 code"), and the path still exists. **Nothing in a digest-bound file is falsified by this diff** [Inferred from the above plus the identical `check_quotations` output]. |
| bd (read-only) | `bd list --all --json` (732 beads). Filed follow-ups from this PR: `syzygy-9mid` (REQ-061 nested widening field), `syzygy-bpyt.7.6`, `.7.7`, `.7.8` (barrel guard) and `syzygy-enxk` (REQ-004 assertions). A regex sweep over title, description, notes and design for `getAuthorityExposures\|authority-exposure\|authority exposure\|REQ-046`, plus one restricted to beads created since 2026-10-21 for `authority\|046\|exposure` (32 such beads), finds **no** REQ-046 gap bead (N2). |

## 4. Findings

No blocking findings.

### N1 — The owner notice must say plainly that the deletion rests on GP-Q0 Part 1, not on the 7.2 row. Classify as classes 1 and 4.

- **Severity:** note, for the coordinator and the `syzygy-bpyt.10` cycle report.
- **Evidence:** The only 7.2 row the owner approved is conditional, and its condition was not
  met. It reads "if `write-guard.ts` is kept" (answers record :89). The deletion therefore rests
  on GP-Q0 Part 1 (behavior-preserving) and on the bead's instruction.
  - I judge that deletion within the direction [Inferred]. The owner was told "7.2 deletes or
    fixes `write-guard.ts`" (`R-GREENFIELD-PARITY-PACKET-2-RAW.md:59`). The row's own "if …
    kept" presupposes the not-kept arm. The guard had no production caller at base [Observed:
    my import-aware closure, `R-RT-RUNTIME-REVIEW.md:29`]. And no rendered byte, wire, refusal
    string, exit code, state-dir file or fixture-tree file changes [Observed: 272 + 240
    identical responses, §3].
  - What the deletion does remove is the only normalizing, symlink-aware governed-plane write
    mechanism. Base `write-guard.ts:17` called it "the one sanctioned runtime write path". Its
    subject is writes "into a governed repository" (SEC-4, `security.md:112-114`), so by
    CC-REV-1's own wording ("anything under SEC-1…SEC-5") I classify this PR as **class 1 and
    class 4**, not class 1 alone. The required checks are the same set for both classes, so no
    extra work follows. The PR's differential, rule-6 runs and flag already satisfy them.
- **Proposed fix:** The `syzygy-bpyt.10` owner notice states three things.
  1. `write-guard.ts` (22 tests) was deleted under GP-Q0 Part 1, and the Part-3 7.2 row was not
     exercised.
  2. Test-only `authorizeWrite` still accepts `openspec/../README.md`.
  3. Any future governed write path is a new class-1/4 change needing its own owner-visible
     review.
  - Name both classes. No byte change to this PR.

### N2 — The REQ-046 authority-exposure gap candidate the bead asks for was not filed.

- **Severity:** note, for the coordinator (bead action, not bytes).
- **Evidence:**
  - The bead says: "if a CAP1 requirement mandates it, it is a gap (file a gap candidate under
    u2a)". The PR finds that REQ-046 mandates the plane (spec.md:1505-1511, quoted in §2) and
    lists it only as "Candidate gap under `syzygy-u2a`".
  - My sweep (§3, bd row) finds no such bead.
  - [Observed] Production renders only the absent sentence (`routes-human.ts:389`, "No authority
    exposures were supplied at this evaluation."). The optional dependency
    `getAuthorityExposures?` (`routes-human.ts:100`, read at :740-742) is supplied by no
    non-test file: `git grep -n -E 'getAuthorityExposures|getDiscoverability' -- apps packages
    ':!*.test.ts'` returns only `routes-human.ts`'s own lines.
  - The derivation REQ-046 names, "effective status (derived from the owner-act record)", is
    `deriveEffectiveStatus` (`packages/cap1-core/src/authority.ts:109`). With `artifactInForce`
    (:146), it is named by no non-test file but its own.
- **Proposed fix:** File one gap bead under `syzygy-u2a`.
  - Title: "CAP1-REQ-046: production supplies no authority exposures; effective status is
    derived only in tests".
  - Cite `routes-human.ts:100-101,382-424,740-742` (head numbering) and
    `authority.ts:109,146`.
  - Wiring changes rendered bytes, so its first acceptance criterion is an owner answer, as in
    `syzygy-9mid`.

### N3 — Three figures in the PR body are wrong, and the decision record lives only in the PR body.

- **Severity:** note (PR text, not reviewed bytes). It matters if copied into the close reason or
  cycle report.
- **Evidence:**
  - (a) "`req-061.conformance.test.ts` pins it with 16 tests … Deleting it would take
    conformance from 312 to 296". [Observed, by reading `req-061.conformance.test.ts:21-154`]
    The 16 tests break down as follows.
    - **6** pin the widening-field clause (detect `write_roots`, all four names, ignore others,
      falsifier, report includes violations, `WIDENING_FIELD_NAMES`).
    - **5** pin `authorizeWrite` (lines 39-74).
    - **2** pin the effect report's empty effects and namespaces.
    - **3** exercise only `entry.ts` (`isInsideGovernedPlane` twice, `GOVERNED_WRITE_NAMESPACES`).
      These survive any deletion of `write-boundary.ts`.
    - `req-integration.conformance.test.ts:226-231` adds one more `authorizeWrite` test.
  - Deleting `write-boundary.ts` would therefore take conformance to 298, not 296. Deleting only
    `authorizeWrite` would take it to 306, which is above the bead's 305 floor. So the
    widening-field clause does not explain keeping `authorizeWrite`. What explains it is
    acceptance criterion 3's "unchanged in count and titles". That is a defensible reading of a
    bead whose description ("delete both") and criterion 3 conflict, but it should be stated as
    the reason.
  - (b) "CG-1f reference count 405 to 401": at the reviewed pair CG-1f reads 405 at both base and
    head (§3).
  - (c) The REQ-061/REQ-046 decision table with spec anchors is in the PR body and nowhere in
    the tree or the evidence record. `grep` for `spec.md:` and `REQ-061`/`REQ-046` in
    `evidence.json` returns nothing. The bead says "Record which." One small anchor slip: the
    PR's REQ-061 range "1785-1829" stops inside the requirement's `warrants` block, which ends
    at :1835.
- **Proposed fix:** When closing `syzygy-bpyt.7.2`, put the decision table in the close reason.
  Write the corrected figures (6/5/2/3 + 1; 298; 306) and give "AC3 unchanged count" as the
  reason `authorizeWrite` is kept. Do not carry the 296 or 405→401 figures into the cycle
  report. Editing the PR body is optional.

### N4 — The test-support boundary is unguarded on the import side as well as the barrel side.

- **Severity:** note.
- **Evidence:**
  - `testing.ts:1-4` says "Nothing here is reachable from the package barrel (index.ts) or from
    any production module".
  - That holds today [Observed: §3 reachability, two methods]. But `package.json` now exports
    `./testing` and the root vitest config aliases it, so any production module can import it
    and nothing fails.
  - `syzygy-bpyt.7.8` covers only the barrel re-export (mutant E05). Its AC: "Add a cheap test
    asserting the barrel's export names exclude every name the @syzygy/cap1-core/testing entry
    exports."
- **Proposed fix:** Widen `syzygy-bpyt.7.8` with a second assertion that no non-test `.ts` under
  `packages/*/src` or `apps/*/src` imports `@syzygy/cap1-core/testing`. Exclude
  `packages/cap1-conformance/src` and `packages/cap1-system/src`. Give it its own rule-6 mutant:
  add the import to `routes-human.ts`.

### N5 — The rule-6 script is not re-runnable without editing it.

- **Severity:** note.
- **Evidence:**
  - `docs/evidence/syzygy-bpyt-7-2/mutate.py:14` hard-codes
    `WT = Path('/home/tze/GitHub/syzygy/.worktrees/parallel-agents/syzygy-bpyt.7.2')`.
  - The record says pass 1 ran "from an earlier revision of mutate.py", which is not stored.
  - Each result does store `old`, `new`, `command` and `commitRunAt` [Observed: all 25 results
    carry `old`/`new`], so rule 6's record requirement is met. A reader can rebuild every mutant
    from the record alone.
  - `route-diff.mjs`, the recorders and `yaml-byte-equality.mjs` take their tree as an argument
    and reproduced exactly here (§3).
- **Proposed fix:** None required for merge. In later evidence, take the tree from `argv`, as
  `route-diff.mjs` does.

### N6 — The REQ-061 conformance file pins `authorizeWrite` without its known false permit.

- **Severity:** note, test quality, pre-existing.
- **Evidence:**
  - The file's oracle comment (`req-061.conformance.test.ts:16`) says "paths outside are
    refused". The reference model accepts `openspec/../README.md`; that input normalizes outside
    the plane. The model's own header records this (`write-boundary.ts:18-20`, "`openspec/../README.md`
    passes the prefix test"), but the conformance file and `req-integration`'s "write boundary
    holds" test show only green prefix cases.
  - [Inferred] A reader of the conformance suite alone would believe REQ-061's write limb is
    implemented in-process. It is not: the real oracle is `write-boundary.system.test.ts`, which
    kills R1, S01 and S02.
- **Proposed fix:** Outside this PR, because acceptance criterion 3 freezes titles, take one of
  two routes.
  - (a) Add a test that pins the false permit with a comment pointing to the system test.
  - (b) Delete `authorizeWrite` and its 6 tests as an owner-visible test-count change in the
    `syzygy-bpyt.10` report.
  - Either belongs with `syzygy-bpyt.7.7`'s audit.

### N7 — Out of scope and pre-existing: the differential's consent-prose fixtures do not discriminate, and REQ-011's "scope, attribution … render" looks unmet at the routes.

- **Severity:** note, for the coordinator to route. This is not this PR's change: base and head
  are byte-identical.
- **Evidence:**
  - [Observed, `rd-head.json`] 4 of the PR's 16 mutated fixtures are byte-identical to
    `complete` on all 16 route × auth responses: `widening-field-write-roots` (disclosed; see
    `syzygy-9mid`), `altered-prose-consent-extra-line`, `altered-prose-consent-scope` (`scope:
    full` → `scope: everything-and-more`) and `no-governed-content`.
  - My probe adds `consent-attribution-agent` (`attribution: owner` → `agent`) and
    `consent-prose-comment`. Both are identical to `complete` on all 20 responses.
  - The complete fixture's human page and `/api/project` body contain the substring
    `attribution` 0 times.
  - REQ-011 (:365-366) says scope, attribution and grant state "render with the coverage
    boundary". [Inferred] At the served routes, a consent record's scope value and attribution
    affect nothing for an in-force record. `coverage.ts:205-206` carries both into the citation;
    `distinction.ts:85` renders them only in the distinction plane.
  - The PR's "17 fixtures" therefore has 13 output-distinct inputs. Two of its three
    "altered-prose" records exercise nothing the routes show.
- **Proposed fix:** No change here.
  - Coordinator: check the REQ-011 rendering limb against `syzygy-u2a.1` and `u2a.6`, and file a
    gap candidate if neither covers it.
  - In later class-1 differentials, report how many fixtures are output-distinct from the
    unmutated one beside the fixture count.

### N8 — If the builder's default owner changes, two failure-path tests silently become valid-path tests.

- **Severity:** note, test quality. Introduced by this PR, but no effect today.
- **Evidence:**
  - Five tests derive an invalid declaration with
    `SOURCE.replace('owner: uniquosity@gmail.com', 'owner: ""')`: req-002:73, req-004:44,
    req-005:33, req-042:74 and req-063:128. The replaced literal used to sit in the same file.
    It is now the builder default `FIXTURE_OWNER` (`fixtures/index.ts:10`, used at :57).
  - [Observed] With the default changed to `'nobody@example.com'` (the PR's M03), conformance
    reports "Tests  3 failed | 309 passed (312)". The three failures are REQ-002 ("falsifier: no
    silent failure …"), REQ-004 ("a missing field is never defaulted …") and REQ-063
    ("falsifier: an unfavourable answer is never improved …").
  - The other two survive. In each, the replace no-ops and the test exercises the **valid**
    source while its name promises the invalid one.
    - `req-005` "invalid input is deterministic too — failure sets are deeply equal across runs".
    - `req-042`'s `registerProject(invalid)` query in "sweep: each Capability 1 query issued
      twice …".
  - Today the default equals the literal, so behavior is unchanged: the call trace is identical.
- **Proposed fix:** Follow-up, not for merge. Make each corrupting replace fail loudly. Either
  assert `expect(corrupted).not.toBe(SOURCE)` before use, or build the invalid source directly
  with `projectYaml({ …, owner: '""' })`. Kill the M03 mutant in all five files, and record that
  rule-6 run. Titles stay unchanged.

## 5. Changed outputs

None found. Evidence:

- **Served routes.** 272 of 272 (PR corpus, reproduced, digest equal to the record) and 240 of
  240 (my corpus) responses are identical. That covers status, content type, all non-date
  headers and body. Daemon stdout/stderr and exit code are identical. The state-dir listing is
  `machine-credential.token` only, on both sides, in all 12 of my fixtures. No fixture file was
  added or changed by either daemon.
- **Refusal strings.** The deleted module's refusal vocabulary (`degenerate-input`,
  `traversal`, `symlink-escape`, `outside-governed-plane`) was never emitted at runtime. Base
  reachability shows `write-guard.ts` unreached, and no route response differs.
- **Exit codes.** The `daemon-entry-unchanged.system.test.ts` cases pass, 15 of 15.
- **Governance outputs.** `check_quotations.py` is byte-identical. `check_governance.py`
  differs only in examined-file counts and AGENTS.md word counts (§3), with 0 FAIL on both sides.
- **Signed or digest-bound artifacts:** none edited (§1 governed-path count, and the §3
  citer sweep).
- **Interface changes that are not outputs** [Observed]:
  - `@syzygy/cap1-core`'s barrel no longer exports the 4 oracle functions, their types or the
    `write-boundary.ts` names.
  - `@syzygy/cap1-daemon`'s barrel no longer exports `authorizeRuntimeWrite`,
    `guardedWriteFile` or `RUNTIME_WRITE_REFUSALS`.
  - `@syzygy/cap1-core/testing` is new.
  - All in-repo consumers typecheck: `npm run typecheck` exits 0 over the ten projects.
  - A code-file sweep over `.ts/.mjs/.js/.cjs/.tsx/.py/.json` finds the moved names only in the
    conformance and daemon test files, the two defining modules, one comment in
    `consent-loading.ts:143`, and historical evidence/pursuit JSON.

## 6. Verdict per acceptance criterion

1. **CAP1-REQ-061 and authority-plane spec checks recorded with file:line; each removal
   justified by them — Met, with N3.**
   - Every anchor the PR cites resolves to the quoted text: spec.md:1785, :1793-1795, :1801,
     :1814-1815, :1501-1542; `credentials.ts:94`; `routes-human.ts:389`; `declaration.ts:147-150`,
     :234-237; `R-RT-RUNTIME-REVIEW.md:29`; answers record :67 and :89.
   - The one deletion, `write-guard.ts`, rests on REQ-061's external-oracle clauses (:1801,
     :1813-1815) and on REQ-023/053's same-form observables.
   - Exceptions: the record lives only in the PR body, and the "16 tests / 296" justification is
     inexact (N3).
2. **No production module in cap1-* is reachable only from tests, except deliberate test-support
   entry points (sweep stated) — Met.**
   - Two predicates agree: 3 unreached non-barrel modules at head, all test support.
   - Nuance: `authority.ts` reaches production only by type, and its runtime functions are
     test-only. That is covered by `syzygy-bpyt.7.7` and by N2.
3. **Conformance: 305+ tests unchanged in count and titles; fixture builder used by every file
   with the shared tail — Met, with one disclosed exception.**
   - 312 = 312, and the name lists are byte-identical.
   - At head the shared tail appears only in `fixtures/index.ts` and `req-003.conformance.test.ts`
     (`spec_root` sweep over the 17 non-builder files). `req-003` builds per-field fragments in
     order to omit one field at a time. The builder has no omission parameter, so that exception
     is reasonable [Inferred], and the PR discloses it.
   - 28 of 45 files import the builder.
4. **Fresh-clone system test and wire parity green — Met.** "Test Files  9 passed (9)" /
   "Tests  48 passed (48)", including the fresh-clone demonstration and both `sweepWireParity`
   callers.

## 7. Test quality

- **Expectations are untouched.** Changed lines in `packages/cap1-conformance/src/` that contain
  `expect`, `it(`, `describe(`, `toBe`, `toEqual`, `toThrow` or `assert`: **0**. The only hits
  are the two header-comment lines of `fixtures/index.ts`.
- **Inputs are identical, and that is shown, not asserted.** The call-trace multisets are equal
  (852/852, 59 functions), and the recorder detects a builder change the tests cannot see (§3).
  `FIXTURE_OWNER` and `FIXTURE_AS_OF` appear in no conformance test file: `grep` count 0. The
  builder imports only types from `@syzygy/cap1-core`, so no expected value comes from the module
  under test.
- **Reading the builder.** It is a plain string concatenation with no branching beyond empty
  sequences, so it is not itself a place where expectations hide. Five tests corrupt the source
  by `.replace('owner: uniquosity@gmail.com', …)`. They now depend on a builder default that is
  in another file. See N8: two of the five would degrade silently.
- **Are the seven survivors' equivalence claims right? Yes**, as "equivalent for this suite".
  - M01/M02: reproduced at base against the old inline literals (§3).
  - M01: the evidence matches `declaration.ts:147-150`, which checks only non-empty string.
  - M02: no non-test `cap1-core` file reads `spec_root`, which matches the record's note.
  - M15: matches `declaration.ts:234-237`, which accepts any mapping.
  - M05-M07: pre-existing assertion gaps, filed as `syzygy-enxk`.
  - E05: no barrel guard, filed as `syzygy-bpyt.7.8`.
  - None is a weakening introduced by this PR.
- **The deleted 22 tests tested only the deleted module.** What stands in for REQ-061's write
  limb is the external oracle. It kills S01 and S02 (the PR's) and R1 (mine, a root-README
  write).
- **The moved oracle is still exercised semantically**, not only by import: R2 is killed by
  REQ-041 and RT4 tests.
- **Weaknesses.**
  - Not introduced here: N6 (the REQ-061 reference model's false permit is unpinned) and N7 (the
    consent-prose fixtures do not discriminate).
  - Introduced here, minor: N8 (two failure-path tests can silently become valid-path tests if
    the builder's default owner changes).

## 8. Cleanup

- I deleted the scratch clones `rev-498/clone` and `rev-498/base` after writing this file.
- I kept my scripts and outputs beside this raw under
  `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/rev-498/`:
  `probe.mjs`, `probe-{base,head}.json`, `rd-{base,head}.json`, `calls-{base,head,mut}.sorted`,
  `mutant.py`, `base_survivor.py`, `reach_check.py`, `runtime_reach.py`, `citer_sweep.py`,
  `citers.txt`, and the `quot-*`, `gov-*`, `list-*` and `*.log` files.
- The two recorder files I copied into each clone root were removed with the clones; neither
  clone was ever pushed.
- I ran no bd mutation, no push, no PR comment and no merge. I edited no worktree under
  `/home/tze/GitHub/syzygy/.worktrees/`.
