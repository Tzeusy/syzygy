# R-GP-IMPL-CODE-STRUCTURE-2 — CC-REV-1 implementation review of syzygy-bpyt.6.1, round 2
Verdict: REVISE
Reviewed commit: 04ba5c8d
Subject: review-r2.diff sha256 27a2e9eafd0671df7bde8ad57ba46bd31ab037fdced49ae44ae27ebc208865eb

Reviewer: a fresh-context CC-REV-1 reviewer (class 3, deterministic observation), date 2026-10-21. I did not author the change, and I did not write round 1.

I was read-only on the worktree `/home/tze/GitHub/syzygy/.worktrees/parallel-agents/syzygy-bpyt.6.1`. All mutants, probes and harnesses ran in two scratch clones under `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/lead/b61/reviewer2/`. Each clone was made with `git clone -q` from the worktree, and `npm ci` was run inside it.

I fetched nothing from the network. I read no observed repository: every repository I observed was a fixture I built locally with `git mktree -z`, plus this repository's own tree.

Two read-only commands touched the worktree directly:
- `python3 scripts/check_docs_review_campaign_partition.py --check docs/README.md`;
- `bd show syzygy-bpyt.6.1` and `bd show syzygy-bpyt.6.7`.

`git status --porcelain` in the worktree was empty at the end.

## 1. Subject identity

- [Observed] `sha256sum review-r2.diff` gives `27a2e9eafd0671df7bde8ad57ba46bd31ab037fdced49ae44ae27ebc208865eb`, which matches the brief.
- [Observed] `git diff fdc866afc4430a63074d52e13418ae319c9aa0a6 04ba5c8d` in the worktree regenerates a file with the same sha256. The regenerated copy is `reviewer2/regen.diff`.
- [Observed] HEAD is `04ba5c8da2de05b05f573de71afd5b79fe50feb5`, and `fdc866af` equals `origin/main`.
- [Observed] `git log fdc866af..HEAD` lists the six commits named in the brief, in that order.
- [Observed] Subject file hashes, computed by script (`reviewer2/hash_at.py`):

| File | Commit | sha256 |
|---|---|---|
| `code-structure.ts` | `fdc866af` (base) | `126a454de2d8645cb91cdf643ef5a9de5ae1c32714cbaaf18e0e0a7eed6eb1be` |
| `code-structure.ts` | `9908b016` and `98be568a` (pre-repair) | `d006cfd87a73f053959919eec2ab8f9a3ad396eec6dc18347ce0ef222588fab9` |
| `code-structure.ts` | `45360ea0` and `04ba5c8d` | `bd7a8142b7594e1590d2ad380d56e0b7b1e6045318edbb69f8fe099e31eafb57` |
| `model.test.ts` | `45360ea0` and `04ba5c8d` | `b9a5d094a19d2a947675f232d0a41e3f25f83837e90db0953e23d7b8811d56d7` |
| `git-tree.ts` | base and HEAD | unchanged |

  All of these equal the values the two r2 evidence records state.
- [Observed] `c7ffd991` touches only the two r2 evidence files. `04ba5c8d` touches only `docs/README.md` and `scripts/check_docs_review_campaign_partition.py`. No code changed after `45360ea0`.
- [Observed] The committed round-1 raw is byte-identical (sha256 `0623fa88efed27757065df0708efe49d2b54f2d03bdfc4a5ec5b67944af90a57`) to the round-1 reviewer's own file in `…/lead/b61/reviewer/`. It was retained verbatim.

## 2. Governing clauses relied on (quoted)

- **CC-REV-1, class 3** (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md:35-36`): "**deterministic observation** — snapshot composition, evaluation identity, the deterministic/inferred seam (VIS-7);".
- **CC-REV-1, the reviewer** (`:26-27`): the reviewer "receives the artifact, its governing doctrine/RFC references, and acceptance criteria — not the author's reasoning or a desired verdict."
- **VIS-2** (`.syzygy/governance/doctrine/vision.md:133-135`): "**VIS-2 — No evidence means Unknown, not success.** Nothing turns green, and no project is declared aligned, converged, or genome-complete (defined in architecture.md), without current evidence."
- **POC-REQ-001** (`openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md:69-73`): "it SHALL produce one identified observation naming the exact git revision observed, containing a directory and file inventory (paths, sizes, per-file content digests, and declared language classifications)". Its falsifier (`:105-107`): "a sampled entry's size or digest, that differs from the repository's own state at the named commit".
- **POC-REQ-002** (`:137-138`): "The POC SHALL NOT index, store, or serve observed file contents from the code-structure observation."
- **POC-REQ-003** (`:179-182`): "WHEN the code-structure observation cannot be produced (repository unreadable, revision unresolvable, observer failure), the POC SHALL serve the code-structure region as Unknown carrying a named reason, and SHALL NOT serve a partial inventory as if complete." Its oracle (`:189-190`): "the reason field is non-empty and names the failure class".
- **POC-REQ-004** (`:220-221`): "For any revision R of the configured project, two code-structure observations of R SHALL produce identical fact content."
- **Owner direction, GP-Q0 Part 3** (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`):
  - line 87: "| `6.1` | `git ls-tree -z`, so quoted paths are recorded, not dropped |";
  - lines 95-96: "Any change not listed here to what a gate accepts or refuses stops and returns to the owner."
- **Bead syzygy-bpyt.6.1** (`bd show`):
  - the scope text: "Anything else that would change rendered bytes, a wire format, a signed or digest-bound artifact, a spec, or a consent, security or retention decision is out of scope: stop and return it to the owner as a new decision bead under syzygy-bpyt.1."
  - the notes: "list each changed output or refusal in the PR. Any other change to what a gate accepts or refuses returns to the owner."
- **AGENTS.md**:
  - guardrail: "`git ls-tree` needs `-z`, or quoted paths break the parser."
  - guardrail at `AGENTS.md:560-565`: "**The PWB-REQ-014 authority sweep reads evidence-record keys.** A JSON key named `source`, `provenance`, `evidence` or `anchor` whose value names the Polaris capture or route fails the fourth test in `polaris-authority-sweep.test.ts` … name the measured subject `measuredOn` / `capture`."
  - verification rules 4, 6, 7, 9 and 11.

## 3. What I ran, and the results

| # | Run (scratch clone at `04ba5c8d` unless stated) | Result |
|---|---|---|
| R1 | `vitest run` on `code-structure.test.ts`, `model.test.ts` and `git-tree.test.ts` | [Observed] 3 files, 32/32 passed |
| R2 | `vitest run --project @syzygy/three-surface-poc-core` | [Observed] `Test Files 33 passed \| 2 skipped (35)`, `Tests 966 passed \| 2 skipped (968)`. The 2 skipped files are the env-gated `test-artifact-verification.live.test.ts` and `work-items.live.test.ts` |
| R3 | `vitest run --project @syzygy/three-surface-poc-app` | [Observed] **`Test Files 1 failed \| 87 passed \| 1 skipped (89)`, `Tests 1 failed \| 1074 passed \| 2 skipped (1077)`**. The skipped file is `project-shape-discovery.live.test.ts`. The one failure is N1 (§5) |
| R4 | `polaris-authority-sweep.test.ts` alone, three times: at `04ba5c8d`, at `45360ea0` and at `c7ffd991` | [Observed] It fails at `04ba5c8d` (1 failed, 4 passed), so it is not a load flake. It passes at `45360ea0` (5/5) and fails at `c7ffd991`: commit `c7ffd991` introduced it |
| R5 | `npm run typecheck` (`tsc -b` over all ten projects) | [Observed] exit 0 |
| R6 | `python3 scripts/check_governance.py` | [Observed] `32 OK, 21 WARN, 0 FAIL (53 checks)`. No WARN line names a file this diff touches; I grepped the log for `code-structure`, `R-GP-IMPL`, `docs/README.md` and `check_docs_review_campaign`, and got 0 lines |
| R7 | The partition check `--check docs/README.md`, in the clone and in the worktree, plus `--selftest` | [Observed] `partition PASS: denominator=487; assigned=487; raw=453; other=34; unmatched=0; overlaps=0; campaigns=103`. The second method gives 487 = 487. `selftest PASS: 14 fixtures` |
| R8 | The new tests against the **base** module (`fdc866af` copied over `code-structure.ts`) | [Observed] With `code-structure.test.ts` alone: `Tests 3 failed \| 5 passed (8)`, so all three new tests fail. With `model.test.ts` added: `4 failed \| 21 passed (25)`; the fourth failure is the `-z` argument assertion at `model.test.ts:765` |
| R9 | The new tests against the **pre-repair** module (`98be568a`), using the record's exact command | [Observed] `Tests 2 failed \| 6 passed (8)`, the two recorded test names and the two recorded assertion lines. This equals `newTestsOnPreRepairCode` |
| R10 | The 12 recorded r2 mutants, each applied by its exact `old`→`new` fragment (each occurs exactly once), with the recorded command | [Observed] All 12 killed. Every `testsLine`, `exitCode` and failing-test set equals the record. The tracked tree was clean afterwards |
| R11 | Three mutants I added (§3b) | [Observed] 2 killed, 1 survived, and it also survived the full core and app projects (N4) |
| R12 | The stored differential harness, extracted from the record (sha256 `dcde328d…f98a9f` equal to `harness.sha256`) and run beside the base module (sha256 `126a454d…6eb1be`) | [Observed] Part A: 27 rows, 19 changed. Part B: 8 rows, 6 changed. Both are deep-equal to the record, row by row |
| R13 | The stored identity harness (sha256 `682145a6…e3eaf5` equal to `harness.sha256`): new module, base module swapped in, new again | [Observed] At my own fixed path, all 6 parts are identical between old and new, and new equals new again. Only `codeStructure` equals the record's digest. At the author's fixed path, all 6 per-part digests and `all` equal the record (see §3c and N5) |
| R14 | My real-git probes, old versus new (§3d, `reviewer2/harness/zz-r2-probes.test.ts`, output `reviewer2/probes.json`) | [Observed] See the table in §3d |
| R15 | Caller sweep by two methods (§3e) | [Observed] See §3e |

### 3a. Test results stated plainly

- [Observed] The full app project fails one test at HEAD: `apps/three-surface-poc/src/polaris-authority-sweep.test.ts` > "no source/authority/provenance field in the governance, spec, code or docs trees names the Polaris surface".
- The hit it reports is `docs/evidence/code-structure-ls-tree-z-differential-2026-10-21-r2.json:251: "source": "import { createHash } from 'node:crypto';…`.
- Everything else in both projects passes.

### 3b. Mutants I added (recorded command: `npx vitest run …/code-structure.test.ts …/model.test.ts`)

| id | `old` → `new` (in `code-structure.ts`) | Outcome |
|---|---|---|
| R2-nul-check-includes | `if (raw !== '' && !raw.endsWith('\0')) {` → `if (raw !== '' && !raw.includes('\0')) {` | killed, `1 failed \| 24 passed (25)` |
| R2-non-utf8-silent-empty | `throw new NonUtf8GitOutput();` → `return '';` | killed, `1 failed \| 24 passed (25)` |
| R2-every-throw-is-non-utf8 | `if (error instanceof NonUtf8GitOutput) {` → `if (error instanceof Error) {` | **survived**, `25 passed (25)`. In the full core and app projects, the only failures were the N1 test and my three env-less scratch harnesses. No project test kills it (N4) |

The definitions are in `reviewer2/extra_mutants.json`, the results in `reviewer2/extra_mutants_results.json` and the full-project log in `reviewer2/mutant-every-throw-full.log`.

### 3c. Byte identity (AC3), re-derived

- [Observed] Using the stored identity harness unchanged, with my fixed path `…/reviewer2/fixed-fixture`, every part is byte-identical between the new module and the base module: model, Orrery, Polaris, Trajectory, POC page and code structure. A second run of the new module equals the first.
  - The fixture is revision `1f892687d53c829f9c2a4ee99bccccb23d6158df`, with 8 files.
- [Observed] My per-part digests at that path differ from the recorded ones for 5 of the 6 parts, and for `all`. Only `codeStructure` (`346af3cb0ff68e8789b3533b9045e99e83f4b8ae4125343efba70b3d6406afb5`) matches.
  - My model is 32117 bytes against the recorded 32103, and my Trajectory is 28790 against 28783. My path is 7 characters longer than the author's.
  - [Inferred] The model JSON carries `repoRoot` twice and Trajectory carries it once. Orrery, Polaris and the POC page are byte-length-equal but differ in digest, so they embed a value derived from the path.
- [Observed] The author's fixed path, `…/lead/b61/r2/fixed-fixture`, still exists in the lead's scratch. I ran the harness with `B61_FIXED` set to it.
  - Every recorded per-part digest re-derived exactly, and so did `all` (`83c58590d3d4e8ff65e127d8fc82b3066f3479516108f65e50f4e93daeb98ad8`). Old equalled new there too.
  - I snapshotted that directory (path, size, sha256 and mtime of all 103 entries) before and after the run, and the two snapshots are identical. I wrote nothing into it.
  - The record does not name this path (`:248`: `B61_FIXED=<fixed path>`). That is N5.
- [Observed] On a realistic tree, this repository at `04ba5c8d`, old and new each observe 2947 files, and their `files` arrays are JSON-identical. 2947 equals the record count of `git ls-tree -r -z -l` there.

AC3 holds on the current fixtures. [Observed]

### 3d. Real-git probes (git 2.53.0, node v24.6.0; trees built with `git mktree -z --missing`, so path bytes are raw)

| Probe | Old (base) | New (HEAD) | Class |
|---|---|---|---|
| P1 two files `\xf1.md`, `\xf2.md` | 2 C-quoted paths | Unknown "code-structure observation produced a path that is not valid UTF-8" | wrong Observed → named Unknown |
| P2 two top-level dirs `\xe8te/`, `\xe9te/` | 2 quoted districts | Unknown (same reason) | wrong Observed → named Unknown |
| P3 nested `src/\xe9/a.ts` beside `src/ok.ts` | 2 files, split into **two** districts `"src` and `src` | Unknown (same reason) | wrong Observed → named Unknown |
| P4 `ok.ts` beside `\xff.ts` (mixed valid and invalid) | quoted plus plain | Unknown (same reason) | wrong Observed → named Unknown |
| P5 overlong `C0 AF`; P6 CESU-8 surrogate `ED A0 80`; P7 truncated `a`+`C3` | quoted | Unknown (same reason) | wrong Observed → named Unknown |
| P8 NFC `é.md` and NFD `e◌́.md` | 2 quoted | 2 exact paths, **distinct** | listed change; injective |
| P9 astral `😀.md`; P10 a name starting with U+FEFF (the first record); P11 literal U+FFFD (valid UTF-8) | quoted | exact, with the BOM preserved | listed change |
| P12 `dir é/x.ts`, `dir é/y.ts` | one quoted district | one district `dir é`, `fileCount` 2 | listed change |
| **P13** gitlink at `\xe9sub` beside `a.ts` | **Observed 1 (`a.ts`), correct** | **Unknown "…path that is not valid UTF-8"** | **correct Observed → Unknown (N2)** |
| **P14** gitlink at `"sub` beside `a.ts` | **Observed 1, correct** | **Unknown "…malformed inventory entry"** | **correct Observed → Unknown (N2)** |
| **P15** gitlink at `su\nb` beside `a.ts` | **Observed 1, correct** | **Unknown "…malformed inventory entry"** | **correct Observed → Unknown (N2)** |
| P16 gitlink at `süb` (valid UTF-8) | Observed 1 | Observed 1 | unchanged |
| **P17** nested gitlink `vendor/\xe9` beside `vendor/ok.ts` | **Observed 1, correct** | **Unknown "…path that is not valid UTF-8"** | **correct Observed → Unknown (N2)** |
| P18 a top-level directory literally named `(root)` beside `README.md` | one district `(root)`, `fileCount` 2 | the same | unchanged; pre-existing, out of scope (§7) |
| Empty tree (`commit-tree` of the empty tree) | Observed 0 | **Observed 0** | unchanged (AC5) |
| Unborn `HEAD`; missing repository path | — | Unknown "repository or revision was unreadable during code-structure observation" | unchanged |

Injected-seam probes, all against the new module:

| Injected `runGit` | Result |
|---|---|
| A runner that passes `ls-tree` to real git with `encoding: 'utf8'`, the form at `test-artifact-verification.live.test.ts:124`, over P1 | **Observed 2, both `�.md`, 1 distinct path** |
| The same runner over P2 | one district `�te`, `fileCount` 2. This is F1's collision, reached through the seam (N3) |
| The literal string `…\t�.md\0` | Observed `�.md` |
| `'\0'` alone | Observed 0 |
| A NUL-terminated record followed by `\n` | Unknown (malformed) |
| Two records joined by `\n` and ending in NUL | Unknown (malformed) |

### 3e. Callers of the strict decoder (rules 2 and 9)

- The denominator is 484 tracked `.ts/.tsx/.mts/.cts/.js/.mjs/.cjs` files at `04ba5c8d`.
- I used two methods, `git grep -l -F` and a Python substring scan over `git ls-files -z`, and they agree on every needle below (`reviewer2/caller_sweep.py`).
- [Observed] `NonUtf8GitOutput` appears in 1 file, `code-structure.ts`.
- [Observed] `observeCodeStructure` appears in 4 files:
  - `code-structure.ts` itself;
  - `code-structure.test.ts`;
  - `model.ts`, at `:1020`, the only production caller;
  - `work-items.live.test.ts`, which is env-gated.
- [Observed] `defaultRunGit` appears in 5 files. The code-structure one, `code-structure.ts:96`, is not exported, and `index.ts:3`'s `export *` re-exports only exported names. Its single call site is `observeCodeStructure` (`:122`, `:125`), inside the `try` whose `catch` (`:126-134`) converts `NonUtf8GitOutput` to the new Unknown.
  - The other four files are separate runners that this diff does not change:
    - `worker-change-observation.ts:65` has its own runner;
    - `governance-inputs.ts:189` has its own runner;
    - `walkthrough-inputs.ts` and `polaris-keyboard-sweep-main.ts` import `governance-inputs.ts`'s runner.
  - No caller of this runner, or of the observer, now sees a thrown error where it used to see a string. [Observed]
- [Observed] There are two non-test `buildPocModel` callers, `production-reobserve.ts:126` and `test-model-fixture.ts:185`. Neither passes a top-level `runGit`, so both use the strict `defaultRunGit`.
- [Observed] The top-level `BuildPocModelInput.runGit` (`model.ts:284`) is forwarded to both the code-structure observer (`:1025`) and the worker-change observer (`:1051`).

### 3f. POC-REQ-002

- [Observed] The observer still issues exactly one git command, `ls-tree -r -z -l <rev>` (`code-structure.ts:125`).
- [Observed] The strict decode works on `ls-tree` metadata only.
- [Observed] The sentinel test passes (R1).

Nothing in the repair reads blob content.

## 4. Disposition check for round 1's F1–F5

- **F1 (blocking): non-UTF-8 path bytes recorded lossily, and distinct paths colliding.**
  - **Repaired for the default runner.** [Observed] `defaultRunGit` now returns `STRICT_UTF8.decode(bytes)` (`code-structure.ts:94`, `:102`) and maps a decode failure to its own reason (`:127-129`).
  - Probes P1–P7 (§3d) and the r2 Part B rows all give "…path that is not valid UTF-8".
  - No two distinct committed names become one string: P8 keeps NFC and NFD apart, and UTF-8 decoding is injective on valid input. [Inferred] The decoder's BOM stripping cannot fire, because `ls-tree` output always begins with a mode digit; P10 confirms a BOM-leading name survives.
  - The docstring (`:113-119`) and the new test title (`code-structure.test.ts:97`) are now accurate for the default runner.
  - **Two residuals remain.** The strict decode also takes down correct inventories (N2, blocking). The seam is unprotected (N3, note).
  - On the U+FFFD question in AC4, I judge that rejecting U+FFFD in `entry.path` would be wrong. A real committed U+FFFD name (P11, valid UTF-8 `EF BF BD`) would then become Unknown, while it is now correctly Observed. The injected-string case matters only through the seam (N3).
- **F2 (note): a path beginning with `"` or containing LF makes the inventory Unknown.**
  - **Filed as `syzygy-bpyt.6.7`**, as the disposition says. [Observed] `bd show syzygy-bpyt.6.7` is OPEN (P3). It quotes F2, proposes the opt-in strict-NUL mode, and routes the output change to the owner under `syzygy-bpyt.1`.
  - [Observed] The behaviour is unchanged in this round. `code-structure.test.ts:132` still pins it.
  - Round 1 also asked that this output "be listed explicitly among the changed outputs and in the class-3 owner notice". The PR body and the cycle report are not part of the subject, so that is [Unknown]. §6 AC7 gives the full list the PR needs.
  - The bead does not cover the gitlink variant of the same parser rule (P14, P15). That is part of N2.
- **F3 (note): no check that the listing is NUL-terminated.**
  - **Repaired.** [Observed] `code-structure.ts:141` makes a non-empty listing that does not end in NUL malformed.
  - The round-1 survivor `model-stub-newline-format` is now killed (R10). So are `nul-format-check-off`, `empty-listing-malformed` and my `R2-nul-check-includes`.
  - With real git, the empty tree still gives Observed 0 (§3d).
- **F4 (note): byte-identity evidence not re-derivable.**
  - **Partly answered.** [Observed] The identity harness is now stored verbatim, and its digest matches.
  - The record does not name the fixed path, and 5 of the 6 per-part digests, plus `all`, depend on it. A cold reader can re-derive "old equals new", but not the recorded values (N5).
- **F5 (note): the changed-output list omitted realistic cases.**
  - **Answered for the two named cases.** [Observed] Part B now has a real missing-blob row (`mktree --missing`, old Observed 1 → new Unknown) and three real non-UTF-8 rows. Both re-derive (R12).
  - The corpus still has no gitlink with an awkward path. Its two gitlink rows use `vendor/sub` and `sub`. That class is N2.

## 5. New findings

### N1 — blocking — the r2 evidence record fails the PWB-REQ-014 authority sweep, so the app test project, and hosted `node-ci`, are red at HEAD

- **Evidence.**
  - [Observed] `docs/evidence/code-structure-ls-tree-z-differential-2026-10-21-r2.json:251` stores the identity harness under the JSON key `"source"`. Its value imports `./polaris.js`, which `POLARIS_SURFACE` (`polaris-authority-sweep.test.ts:22`, `(^|[^A-Za-z0-9-])\/polaris\b`) matches.
  - The fourth sweep (`polaris-authority-sweep.test.ts:180-203`) flags any line whose key is `source|authority|warrants?|primary|evidence|provenance|cites?|anchor` and whose value names the Polaris surface.
  - The same record's `:21` also uses `"source"`, but its value does not name Polaris.
  - Results R3 and R4: the test fails at `04ba5c8d` and at `c7ffd991`, and passes at `45360ea0`.
  - `.github/workflows/node-ci.yml` runs `npm test`, which is `vitest run`, on every `pull_request` to `main`.
  - AGENTS.md:560-565 records this exact trap.
- **Failure scenario.** The PR for this bead opens with a red `node-ci` run. Alternatively, if the battery is trusted from its exit code without its output (rule 4), a branch merges with a failing PWB-REQ-014 test on `main`.
- **Proposed fix.**
  - Rename the harness key at `:251`, and for consistency at `:21`, to a key the sweep does not read, for example `"text"`. The recorded `harness.sha256` is a digest of the value, so it stays valid, and line numbers do not move.
  - [Observed] I applied exactly this rename in a scratch clone, and `polaris-authority-sweep.test.ts` then passed 5/5.
  - Re-run both full projects after the edit.
  - The round-1 record keeps its key. Its harness does not name Polaris, and round 1's raw cites it by line.

### N2 — blocking — a gitlink whose path is not valid UTF-8, begins with `"`, or holds LF now makes a correct inventory Unknown; this changed output is outside the owner-listed change

- **Evidence.**
  - [Observed] Probes P13, P14, P15 and P17 (§3d). In each, the base module returns a correct, complete file inventory. It always skipped `commit` records before looking at their path (base `code-structure.ts`: `if (match === null || match[2] !== 'blob') { continue; }`), and gitlinks are not files of the revision.
  - The head module returns a whole-inventory Unknown in each case, for two reasons:
    - `defaultRunGit` decodes the entire stdout strictly (`code-structure.ts:102`), so one non-UTF-8 gitlink path fails the whole listing. This came in with `45360ea0`.
    - `parseGitLsTree` rejects every record whose path starts with `"` or contains `\n` before the type filter at `code-structure.ts:150` runs (`git-tree.ts:35`). This came in with `9908b016`.
  - Neither r2 differential corpus covers this class.
- **Why this is outside the listed change.**
  - The owner approved "quoted paths are recorded, not dropped" (`OWNER-DIRECTION-…-2026-10-21.md:87`). AC7 also admits a fail-closed move from a wrong or partial Observed to a named Unknown.
  - This class moves from a correct Observed to Unknown. It is not the listed outcome, and it is not a repair of a wrong or partial one.
  - It changes rendered bytes: the Orrery map becomes Unknown.
  - The bead's scope text sends any such change back to the owner, and so does the owner's line 95: "Any change not listed here to what a gate accepts or refuses stops and returns to the owner."
  - [Inferred] It is lawful under VIS-2, because it is fail-closed and the reason is named. The reason "malformed inventory entry" misnames P14 and P15, as F2 already noted for files.
- **Failure scenario.** A repository with a submodule checked out at a Latin-1-named directory, or at a path beginning with a double quote, loses its whole Orrery map and its machine-answer inventory. Before this change, both were correct. [Inferred] Such paths are rare.
- **Proposed fix.** Choose one of these before merge.
  - (a) Restore the old outcome for gitlinks. Drop records whose mode is `160000` from the raw bytes before the strict decode and the parse.
    - [Observed] I applied this proof of concept in a scratch clone (`reviewer2/poc_gitlink_fix.py`): about ten lines in `defaultRunGit` that split on NUL and drop records starting with `160000 `.
    - P13–P17 then returned exactly the old, correct output (`reviewer2/probes-poc-gitlink.json`).
    - Every other probe was unchanged. `code-structure.test.ts` passed 8/8 and `model.test.ts` 17/17.
    - Add a real-git test with a non-UTF-8 gitlink and a `"`-leading gitlink beside a blob, plus a mutant that removes the filter.
  - (b) Keep the behaviour, list it in the PR as a changed output, and return it to the owner as a decision bead under `syzygy-bpyt.1`, as the bead's scope text requires.

  Under either choice, add the class to the differential corpus.

### N3 — note — the strict-UTF-8 guarantee lives only in `defaultRunGit`; an injected runner can still record lossy, colliding paths as Observed

- **Evidence.**
  - [Observed] `ObserveCodeStructureInput.runGit` (`code-structure.ts:88`) and `BuildPocModelInput.runGit` (`model.ts:284`) both return a `string`. Their contract does not say the string must be a faithful decode.
  - `BuildPocModelInput.runGit` is shared with the worker-change observer (`model.ts:1025`, `:1051`). So a caller that injects a runner for worker-change also replaces the code-structure decoder.
  - The one existing injector that passes `ls-tree` through to real git is `test-artifact-verification.live.test.ts:124`, which uses `{ encoding: 'utf8' }`, Node's replacing decoder. My seam probe with that form reproduces F1 exactly: two paths `�.md`, and one district `�te` with `fileCount` 2 (§3d).
  - [Observed] No production caller injects (§3e), and that live test is env-gated and skipped here.
  - The docstring sentence "The bytes are decoded as strict UTF-8" (`code-structure.ts:115-116`) holds only for the default runner.
- **Failure scenario.** [Inferred] A future production caller injects one runner to drive worker-change, for example to pin a git binary or an environment. That re-opens F1 silently, and no test fails.
- **Proposed fix.**
  - State the contract on both seams: the runner returns git's stdout decoded strictly, or throws.
  - Change the live test's passthrough to decode strictly.
  - Or let the seam return bytes. Bead `syzygy-bpyt.6.5` ("one GitRunner") is the natural home for that.

### N4 — note — only one arm of the new Unknown-reason discrimination is pinned

- **Evidence.**
  - [Observed] Mutant `R2-every-throw-is-non-utf8` changes `instanceof NonUtf8GitOutput` to `instanceof Error`. It makes a missing repository, or an unresolvable revision, report "…path that is not valid UTF-8".
  - It survives the recorded command, and it survives both full projects (§3b).
  - The POC-REQ-003 test asserts only `expect(result.reason.length).toBeGreaterThan(0)` (`code-structure.test.ts:88`). The recorded mutant `non-utf8-reason-merged` pins only the other arm.
- **Failure scenario.** A refactor of the `catch` labels every git failure as a UTF-8 problem. POC-REQ-003's oracle ("names the failure class") is then false, and no test notices.
- **Proposed fix.** At `code-structure.test.ts:88`, assert the exact object `{ kind: 'unknown', reason: 'repository or revision was unreadable during code-structure observation' }`. Then record the mutant as killed (rule 6: one mutant per predicate arm).

### N5 — note — two pieces of evidence are not re-derivable from the records alone

- **Evidence.**
  - [Observed] `fixtureByteIdentity.command` (`…-r2.json:248`) is `B61_FIXED=<fixed path> …`, and the record does not name the path.
    - The recorded model, Orrery, Polaris, Trajectory and POC digests, and `all`, re-derive only at the author's path, `…/lead/b61/r2/fixed-fixture` (§3c). I recovered that path from the lead's scratch directory, not from the record.
  - [Observed] `newTestsOnPreRepairCode` records the new tests against `98be568a`, not against the base.
    - The bead's AC2 reads "New fixture test fails on the old code and passes on the new (both runs recorded)".
    - No retained record holds the base run of the non-UTF-8 test, or a head run. Round 1's record holds the base run of the first two tests.
    - My base run is R8: `Tests 3 failed | 5 passed (8)`.
- **Failure scenario.** Under rules 10 and 11, a later reader cannot check the recorded digests, or the AC2 base failure, against the bytes. Only an independent re-derivation can, as here.
- **Proposed fix.** Record the fixed path, or have the harness hash with `repoRoot` normalized to a constant. Add the base and head runs of `code-structure.test.ts` to the record.

## 6. Verdict per acceptance criterion

1. **`-z` through the shared parser; no silent skip of an unreadable record.** **Met.** [Observed]
   - `code-structure.ts:125` passes `-z`, and `:144` calls `parseGitLsTree`.
   - A malformed parse, a missing size, a non-SHA-1 id and a non-NUL-terminated listing each return Unknown (`:141-154`).
   - The only filters left are the documented gitlink exclusion (`:150`) and the parser's skip of empty records between NULs (`git-tree.ts:31`), which real git does not emit.
2. **The new tests fail on base and pass on head.** **Met.** [Observed] R8: on base, all three new tests fail, plus the `-z` assertion in `model.test.ts`. R1: on head, 8/8 and 17/17. The record covers the pre-repair code rather than the base (N5).
3. **Model and Orrery byte-identical on the current fixtures.** **Met.** [Observed] §3c: all six parts are identical at two paths, and the repository's own tree gives 2947 identical files. The recorded digests re-derive only at the unrecorded path (N5).
4. **F1 fixed.** **Met for the default runner; not met in full.**
   - [Observed] With real git, every non-UTF-8 file or directory name, mixed with valid names or not, nested or top-level, is Unknown with a named reason.
   - No two distinct committed paths become one, on the probes run.
   - An injected U+FFFD string is Observed. I judge that this does not matter for production, and that rejecting U+FFFD would refuse a real valid name (P11). The seam residual is N3.
   - The strict decode also takes down correct inventories (N2).
5. **F3 fixed; empty tree Observed 0 with real git.** **Met.** [Observed] §3d and R10.
6. **F4 and F5 reproduce from the stored harnesses; every recorded row and digest re-derives.** **Partly met.**
   - [Observed] Differential: all 35 rows re-derive exactly (R12).
   - Mutants: 12 of 12 re-derive exactly (R10).
   - Identity: every digest re-derives, but only at a path the record does not name (N5).
7. **Scope: every changed output is owner-listed, or a fail-closed move from a wrong or partial Observed to a named Unknown.** **Not met (N2).**
   - Owner-listed outputs:
     - (a) Valid-UTF-8 paths that git would C-quote are now exact Observed, with the correct language class, sort position and Orrery district. This covers tab, CR, a mid-path quote, backslash, non-ASCII including NFC and NFD, astral characters, a BOM and a literal U+FFFD.
   - Fail-closed moves from a wrong or partial Observed to a named Unknown:
     - (b) Non-UTF-8 file or directory paths: wrong quoted Observed → Unknown, with the new reason "code-structure observation produced a path that is not valid UTF-8".
     - (c) File paths beginning with `"` or holding LF: wrong quoted Observed → Unknown "malformed inventory entry" (F2, bead 6.7).
     - (d) A missing blob, where git prints `BAD`: partial Observed → Unknown malformed.
     - (e) SHA-256 or other non-40-hex ids: false Observed 0 → Unknown malformed.
     - (f) Unparseable records (garbage, corrupt mode or type, missing tab, empty path, non-numeric size, uppercase hex). These are injected only, and go from dropped records or Observed 0 → Unknown malformed.
     - (g) Newline-format or unterminated listings. These are injected only, and go from Observed → Unknown malformed.
   - Outside both:
     - (h) A gitlink with a non-UTF-8, `"`-leading or LF-holding path: correct Observed → Unknown (N2).
   - The PR must list (a) through (g). Whether it does is [Unknown], because the PR body is not in the subject. (h) must be fixed or returned to the owner.
8. **Partition.** **Met.** [Observed]
   - The check passes at HEAD in the clone and in the worktree: 487 files, 487 assigned, 0 unmatched, 0 overlaps, 103 campaigns. `--selftest` gives 14 fixtures PASS.
   - The README row's `REVISE` matches `R-GP-IMPL-CODE-STRUCTURE-1-RAW.md:2` ("Verdict: REVISE"), and its "over `99adbd03`" matches `:3`. "One blocking finding and four notes" matches §4 of that raw.
   - The row's claim that F4 is "answered" overstates it (N5). After this round, the row will need a round-2 entry.

**Overall: REVISE.** N1 makes the PR's own test battery fail. N2 is an unlisted output change, which the bead's scope rule sends back to the owner unless it is removed. N3, N4 and N5 are notes.

## 7. Out of scope, unchanged by this diff

[Observed] P18: a top-level directory literally named `(root)` merges with root-level files into one Orrery district (`orrery-projection.ts`, `topLevelDirectory`). The old and new code behave identically, so this is not a finding against this change. It may deserve its own bead.

## 8. Cleanup

- [Observed] The worktree's `git status --porcelain` is empty, and its branch is level with `origin/agent/syzygy-bpyt.6.1`.
- I placed nothing in the worktree. The lead's `…/lead/b61/r2/fixed-fixture` was read only, and its 103-entry snapshot is unchanged.
- Both scratch clones, my fixed-fixture copy and the probe repositories were deleted after the runs.
- Retained under `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/lead/b61/reviewer2/`:
  - harnesses, in `harness/`: the two extracted r2 harnesses and my `zz-r2-probes.test.ts`;
  - runners and scripts: `run_mutants.py`, `run_identity.py`, `run_one_mutant_full.py`, `caller_sweep.py`, `poc_gitlink_fix.py`, `rename_harness_key.py`, `snapshot_dir.py`, `hash_at.py`;
  - outputs: `recorded_mutants_rerun.json`, `extra_mutants_results.json`, `swaps_codestructure_only.json`, `differential-rerun.json`, `identity-*.json`, `identity-authorpath/`, `probes.json`, `probes-poc-gitlink.json`, `author-fixed-before.json`, `author-fixed-after.json`;
  - logs: `full-core.log`, `full-app.log`, `mutant-every-throw-full.log`, `check-governance.log`;
  - `regen.diff`.
