# R-GP-IMPL-CODE-STRUCTURE-3 — CC-REV-1 implementation review of syzygy-bpyt.6.1, round 3
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 8afbafcb
Subject: r3-review.diff sha256 f893bc67913b132ea7dcc46fa21b837a0c39d5f23d124498c3fd7786a4d52f0c

Reviewer: a fresh-context CC-REV-1 reviewer (class 3, deterministic observation), date 2026-10-21. I did not author the change, and I wrote neither round 1 nor round 2.

I was read-only on the worktree `/home/tze/GitHub/syzygy/.worktrees/parallel-agents/syzygy-bpyt.6.1`. All harnesses, probes and mutants ran in one scratch clone, `…/lead/b61/reviewer3/clone`, made with `git clone -q` from the worktree, with `npm ci` run inside it. Here and below, `…` stands for `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad`.

I fetched nothing from the network. I read no observed repository. Every repository I observed was a fixture I built locally with `git mktree -z` or `git hash-object --literally`, plus this repository's own tree.

The commands that touched the worktree directly were read-only: `git diff`, `git log`, `git rev-parse` and `git status`; `bd show syzygy-bpyt.6.1`, `bd show syzygy-bpyt.6.5`, `bd show syzygy-bpyt.6.7` and `bd comments syzygy-bpyt.6.5`. I made no `bd` mutation, no commit and no push. `git status --porcelain` in the worktree was empty at the end, and HEAD was still `8afbafcb16e35f875326cab1798f1e8c9dd99b74`.

## 1. Subject identity

- [Observed] `sha256sum …/lead/b61/r3-review.diff` gives `f893bc67913b132ea7dcc46fa21b837a0c39d5f23d124498c3fd7786a4d52f0c`, which matches the brief.
- [Observed] `git diff fdc866afc4430a63074d52e13418ae319c9aa0a6 8afbafcb16e35f875326cab1798f1e8c9dd99b74` in the worktree regenerates a file with the same sha256 (`…/lead/b61/reviewer3/regen.diff`).
- [Observed] HEAD is `8afbafcb16e35f875326cab1798f1e8c9dd99b74`. `git log fdc866af..HEAD` lists twelve commits; the six after round 2's subject `04ba5c8d` are, oldest first, `38dde4a0`, `0078dedc`, `0e9937b4`, `41225e4a`, `eddf9677` and `8afbafcb`, as the brief states.
- [Observed] The local `main` ref is stale (`29e036f4`, an ancestor of `fdc866af`) and the local `origin/main` is `fe20dd5f`. Neither affects the frozen subject, which is defined against `fdc866af`.
- [Observed] Files touched per commit (`git log --name-status 04ba5c8d..8afbafcb`):
  - `38dde4a0` adds only `docs/reviews/R-GP-IMPL-CODE-STRUCTURE-2-RAW.md`;
  - `0078dedc` changes `code-structure.ts`, `code-structure.test.ts`, `model.ts` and `test-artifact-verification.live.test.ts`;
  - `0e9937b4` changes only the r2 differential record;
  - `41225e4a` changes `code-structure.ts` and `code-structure.test.ts`;
  - `eddf9677` changes only `code-structure.test.ts`;
  - `8afbafcb` changes `docs/README.md` and adds the two r3 evidence records.
- [Observed] Subject file hashes, computed by script (`…/reviewer3/hash_at.py`):

| File | Commit(s) | sha256 |
|---|---|---|
| `code-structure.ts` | `fdc866af` (base) | `126a454de2d8645cb91cdf643ef5a9de5ae1c32714cbaaf18e0e0a7eed6eb1be` |
| `code-structure.ts` | `45360ea0`, `04ba5c8d`, `38dde4a0` (round 2) | `bd7a8142b7594e1590d2ad380d56e0b7b1e6045318edbb69f8fe099e31eafb57` |
| `code-structure.ts` | `0078dedc`, `0e9937b4` | `55fe87b83be2fc323ab7fb48c13786b7447f87a28303c998b315c4035030e95d` |
| `code-structure.ts` | `41225e4a`, `eddf9677`, `8afbafcb` | `ef137dafdd666104b9249d5516b0567e8daf9db7a5814c68c29e362f87ca56c1` |
| `code-structure.test.ts` | `eddf9677`, `8afbafcb` | `e8a24275514e38c870fdeb7e5cce7b61082eaa9b264b74f4349d51a274b170d7` |
| `model.test.ts` | `45360ea0` through `8afbafcb` | `b9a5d094a19d2a947675f232d0a41e3f25f83837e90db0953e23d7b8811d56d7` |
| `git-tree.ts` | base through HEAD | `990d17dcf904bc28dc7c8336d5111321c80df053841bd7b19a8a665fd01578a3`, unchanged |

  The r3 records state the same `old.sha256`, `new.sha256`, `subjectTests.testFileSha256` and mutant `subjectSha256` values. The records name `eddf9677` as their commit; its three subject files are byte-identical to `8afbafcb`'s.
- [Observed] The committed round-2 raw (sha256 `469a0a84d31c69a9a5ef51f7e48dd2359e7ce61ccad252bad8b72d43bca140e6`) is byte-identical to the round-2 reviewer's own file in `…/lead/b61/reviewer2/`. It was retained verbatim. The round-1 raw is unchanged since round 2 (`0623fa88…`).

## 2. Governing clauses relied on (quoted)

- **CC-REV-1, class 3** (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md:35-36`): "**deterministic observation** — snapshot composition, evaluation identity, the deterministic/inferred seam (VIS-7);".
- **CC-REV-1, the reviewer** (`:22-27`): the reviewer "did not author the change; does not share the authoring session's context; receives the artifact, its governing doctrine/RFC references, and acceptance criteria — not the author's reasoning or a desired verdict."
- **VIS-2** (`.syzygy/governance/doctrine/vision.md:133-135`): "**VIS-2 — No evidence means Unknown, not success.** Nothing turns green, and no project is declared aligned, converged, or genome-complete (defined in architecture.md), without current evidence."
- **POC-REQ-001** (`openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md:69-73`): "it SHALL produce one identified observation naming the exact git revision observed, containing a directory and file inventory (paths, sizes, per-file content digests, and declared language classifications)". Its falsifier (`:105-107`): "a sampled entry's size or digest, that differs from the repository's own state at the named commit".
- **POC-REQ-002** (`:137-138`): "The POC SHALL NOT index, store, or serve observed file contents from the code-structure observation."
- **POC-REQ-003** (`:179-182`): "WHEN the code-structure observation cannot be produced (repository unreadable, revision unresolvable, observer failure), the POC SHALL serve the code-structure region as Unknown carrying a named reason, and SHALL NOT serve a partial inventory as if complete." Its oracle (`:189-190`): "the reason field is non-empty and names the failure class".
- **POC-REQ-004** (`:220-221`): "For any revision R of the configured project, two code-structure observations of R SHALL produce identical fact content."
- **Owner direction** (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`):
  - Part 1, review rule (`:59-67`): pull requests touching class 3 also get "an old-versus-new differential over a mutated-record corpus that includes records with altered prose; a rule-6 mutant for each predicate; a non-blocking owner notice in the cycle report."
  - Part 3 (`:87`): "| `6.1` | `git ls-tree -z`, so quoted paths are recorded, not dropped |".
  - Part 3 (`:95-96`): "Any change not listed here to what a gate accepts or refuses stops and returns to the owner."
- **Bead `syzygy-bpyt.6.1`** (`bd show`):
  - the scope text: "Anything else that would change rendered bytes, a wire format, a signed or digest-bound artifact, a spec, or a consent, security or retention decision is out of scope: stop and return it to the owner as a new decision bead under syzygy-bpyt.1."
  - the notes: "list each changed output or refusal in the PR. Any other change to what a gate accepts or refuses returns to the owner."
  - acceptance criterion 2: "New fixture test fails on the old code and passes on the new (both runs recorded)."
- **AGENTS.md**:
  - guardrail: "`git ls-tree` needs `-z`, or quoted paths break the parser."
  - guardrail: "A rule-6 evidence record must store each mutant's `old`/`new` fragment and the commit it ran at; ids and outcomes alone are not re-runnable".
  - guardrail: "**The PWB-REQ-014 authority sweep reads evidence-record keys.** A JSON key named `source`, `provenance`, `evidence` or `anchor` whose value names the Polaris capture or route fails the fourth test in `polaris-authority-sweep.test.ts`".
  - verification rules 2, 4, 6, 7, 9, 10 and 11.

## 3. What I ran, and the results

All runs were in the scratch clone at `8afbafcb` unless stated (git 2.53.0, node v24.6.0).

| # | Run | Result |
|---|---|---|
| R1 | `npx vitest run --project @syzygy/three-surface-poc-core` | [Observed] ` Test Files  33 passed \| 2 skipped (35)` and `      Tests  968 passed \| 2 skipped (970)`. The log has 0 `FAIL` lines and 0 `×` lines. The two skipped files are the env-gated live tests. Round 2 had 966 tests; the 2 new ones are the unterminated-tail and real-git gitlink tests |
| R2 | `npx vitest run --project @syzygy/three-surface-poc-app` | [Observed] ` Test Files  88 passed \| 1 skipped (89)` and `      Tests  1075 passed \| 2 skipped (1077)`. The log has 0 `FAIL` lines and 0 `×` lines. `polaris-authority-sweep.test.ts (5 tests)` passed. Round 2's one failure (N1) is gone |
| R3 | `npm run typecheck` | [Observed] exit 0; the log holds only the npm and `tsc -b …` echo lines, with 0 `error TS` lines |
| R4 | `python3 scripts/check_governance.py` | [Observed] `32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted`. The only log lines naming a subject file are 7 WARN rows that resolve relative scratch paths cited inside the round-2 raw (`reviewer2/caller_sweep.py` and the like), in the same unresolved-citation WARN that lists many other retained raws |
| R5 | `python3 scripts/check_docs_review_campaign_partition.py --check docs/README.md`, then `--selftest` | [Observed] `second-method PASS: git ls-files=488; git ls-tree=488; exact path sets equal`, `partition PASS: denominator=488; assigned=488; raw=454; other=34; unmatched=0; overlaps=0; campaigns=103`, and `selftest PASS: 14 fixtures` |
| R6 | `code-structure.test.ts` (the r3 record's `subjectTests.command`), and the same with `model.test.ts`, with the head, base, round-2 (`45360ea0`) and `0e9937b4` modules written in turn over `code-structure.ts` (`…/reviewer3/swap_runs.py`, output `swap_runs.json`) | [Observed] head: `Tests  10 passed (10)` and `27 passed (27)`. Base: `4 failed \| 6 passed (10)`, the four tests the record names; with `model.test.ts`, `5 failed \| 22 passed (27)`, the fifth being the `-z` argument assertion. Round 2: `2 failed \| 8 passed (10)`, the injected-runner test and the real-git gitlink test. `0e9937b4`: `1 failed \| 9 passed (10)`, the injected-runner test only. Restored and digest-checked; the tracked tree was clean |
| R7 | The stored r3 differential harness, extracted from the record (sha256 `4ad6cfcba5e5b03537cc0348002c1c785734c8c1bfb0496c77b669b49f1a68c6`, equal to `differential.harness.sha256`), run beside the base module | [Observed] Part A 28 rows, 19 changed; Part B 13 rows, 6 changed. Every row is deep-equal to the record, and each `changed` flag equals `old !== new` (`compare_diff.py`) |
| R8 | The stored identity harness (sha256 `682145a61475e8d5dd1821d9eebd4e3542d5f2491c2896978e77679474e3eaf5`, equal to the record's) with head, base and head again, at two fixed paths (`run_identity.py`) | [Observed] At the author's path `…/lead/b61/r2/fixed-fixture` every per-part digest and `all` (`83c58590d3d4e8ff65e127d8fc82b3066f3479516108f65e50f4e93daeb98ad8`) equal the record, for all three runs. At my own path, head, base and head again are equal to each other, and only `codeStructure` equals the record's digest (see §3d) |
| R9 | The stored r3 mutants harness (`mutants.py`, extracted from `harnessText`), unchanged, against the clone | [Observed] `{'planned': 18, 'killed': 18}`. For all 18, the id, fragment, exit code, tests line, outcome, `restored` flag and failing-test set (timings stripped) equal the record (`compare_mutants.py`). The first twelve are exactly round 2's twelve fragments. The tree was clean before and after |
| R10 | Four mutants I added, plus the record's historical claim (`extra_mutants.py`, output `extra_mutants_results.json`) | [Observed] See §3c. Three survived; they are R3-N3 |
| R11 | My real-git and injected probes (`…/reviewer3/harness/zz-r3-probes.test.ts`, sha256 `e32943fd6383fb3fe89b7a572e2cd428ecb14fd1a13f0b8127e2bde720bd1848`; output `probes.json`) | [Observed] See §3a and §3b |
| R12 | Caller sweep, two methods (`caller_sweep.py`) | [Observed] See §3e |
| R13 | N1 sweep, two methods (`n1_sweep.py`) | [Observed] See §3f |

### 3a. Real-git probes, default runners (old = base `fdc866af`, r2 = `45360ea0`, new = HEAD)

Trees were built with `git mktree -z --missing`, so path bytes are raw. Each row also ran with two injected passthrough runners; those columns are in §3b.

| Probe | Old | r2 | New | new = old |
|---|---|---|---|---|
| G1 gitlink at `\xe9sub` beside `ok.ts` | Observed `ok.ts` | Unknown, not UTF-8 | Observed `ok.ts` | yes |
| G2 gitlink at `"sub` beside `ok.ts` | Observed `ok.ts` | Unknown, malformed | Observed `ok.ts` | yes |
| G3 gitlink at `su\nb` beside `ok.ts` | Observed `ok.ts` | Unknown, malformed | Observed `ok.ts` | yes |
| G4 gitlink at `süb` (valid UTF-8) | Observed `ok.ts` | Observed `ok.ts` | Observed `ok.ts` | yes |
| G5 gitlink one level down at `vendor/\xe9` beside `vendor/ok.ts` | Observed `vendor/ok.ts` | Unknown, not UTF-8 | Observed `vendor/ok.ts` | yes |
| G6 gitlink at `\xe9dir/sub`, inside a non-UTF-8 directory that holds only it | Observed `ok.ts` | Unknown, not UTF-8 | Observed `ok.ts` | yes |
| G7 gitlink two levels down at `a/b/\xff\xfe` beside `a/b/c.ts` | Observed `a/b/c.ts` | Unknown, not UTF-8 | Observed `a/b/c.ts` | yes |
| G8 gitlink whose path is `sub` + LF + a complete fake blob record (`100644 blob 1…1      12\tfake.ts`) | Observed `ok.ts` | Unknown, malformed | Observed `ok.ts` | yes |
| G9 a **blob** named `160000 x.ts` beside a gitlink | Observed `160000 x.ts` | same | Observed `160000 x.ts` | yes |
| G10 a **blob** at `160000 commit/a.ts` | Observed `160000 commit/a.ts` | same | same | yes |
| G11 non-UTF-8 gitlinks as the first (`!\xe9`) and last (`\xff`) records, a blob between | Observed `m.ts` | Unknown, not UTF-8 | Observed `m.ts` | yes |
| G12 only gitlinks (`\xe9`, `"sub`, `s\nub`) | Observed 0 | Unknown, not UTF-8 | Observed 0 | yes |
| G13 non-UTF-8 gitlink beside a non-UTF-8 blob `\xf1.md` | Observed, quoted path | Unknown, not UTF-8 | Unknown, not UTF-8 | no: class (b), §6 AC7 |
| G14 gitlink at `tab\tsub`; G15 gitlink at the ASCII name `"\351sub"` | Observed `ok.ts` | G14 Observed, G15 Unknown malformed | Observed `ok.ts` | yes |
| G16 control, files only | Observed 2 | same | same | yes |
| M1 literal tree, blob under mode `100664` | Observed 2 | same | same | yes |
| M2, M3, M4 literal trees: a blob id under modes `170000`, `10644` and `160000` | Observed `ok.ts` | same | same | yes |
| E1 empty tree; E2 missing repository path; E3 unresolvable revision | Observed 0; Unknown unreadable; Unknown unreadable | same | same | yes |

- [Observed] `ls-tree -r -z -l` prints M2, M3 and M4 as `160000 commit <blob id>       -`. Git prints a non-canonical mode as a gitlink and derives the type from the mode. [Inferred] So real git never emits a `160000` record whose type is not `commit`, and the head's gitlink filter never sees a real file record that starts with `160000 `.
- [Observed] G8's raw listing is a single NUL-terminated record whose path holds an LF and a record-shaped tail. Under `-z` that is one gitlink, so dropping the whole segment is correct.
- [Observed] G9 and G10 show the filter keeps a blob whose path contains `160000 `, because the filter tests the start of each NUL-terminated record and a path never starts a record.

### 3b. Injected runners

Two passthrough runners were run over every real-git probe: a strict one (`new TextDecoder('utf-8', { fatal: true }).decode(execFileSync('git', …))`, the form now at `test-artifact-verification.live.test.ts:124`) and a lossy one (`encoding: 'utf8'`).

- [Observed] Strict passthrough, with any non-UTF-8 gitlink path (G1, G5, G6, G7, G11, G12): new and r2 both give **Unknown "repository or revision was unreadable during code-structure observation"**; old gives the correct Observed. The runner throws a `TypeError` before the observer's gitlink filter can run, and the observer maps any throw other than its private `NonUtf8GitOutput` to the unreadable reason. This is R3-N1.
- [Observed] Strict passthrough with quote-leading or LF gitlinks (G2, G3, G8, G15): new gives the old outcome, through the string-level filter at `code-structure.ts:167`.
- [Observed] Lossy passthrough: every gitlink row gives the old outcome in new. G13's non-UTF-8 blob becomes Observed `�.md` (round 2's N3, unchanged).

Injected `-z` strings. The old column feeds the base module the same records with LF terminators, since it asks for the newline format:

| Listing | Old (LF form) | r2 | New |
|---|---|---|---|
| I1 a blob, then `160000 garbage` | Observed `a.ts` (line skipped) | Unknown, malformed | Observed `a.ts` (segment dropped) |
| I2 `160000 blob <40 hex>      12\ta.ts` | Observed `a.ts` | Observed `a.ts` | **Observed 0** (segment dropped) |
| I3 a gitlink and a blob joined by LF, one final NUL | Observed `a.ts` | Unknown, malformed | Observed 0 (one gitlink, as G8) |
| I4 a blob, then `100644 commit … x` | Observed `a.ts` | same | same (non-blob skipped) |
| I5 a blob, then an unterminated gitlink | Observed `a.ts` | Unknown, malformed | Unknown, malformed |
| I6 `\0` alone; I7 a lone gitlink; I8 a blob then an empty record | Observed 0; 0; `a.ts` | same | same |
| I9 a seven-digit mode `0160000` | Observed `a.ts` | Unknown, malformed | Unknown, malformed |
| I10 `160000  commit` (two spaces) | Observed `a.ts` (line skipped) | Unknown, malformed | Observed `a.ts` (segment dropped) |

I1, I2 and I10 are R3-N2.

### 3c. Mutants I added (recorded command: `npx vitest run …/code-structure.test.ts …/model.test.ts`)

| id | `old` → `new` (in `code-structure.ts`) | Outcome |
|---|---|---|
| R3-byte-filter-contains | `if (!record.subarray(0, GITLINK_RECORD.length).equals(GITLINK_RECORD)) kept.push(record);` → `if (!record.includes(GITLINK_RECORD)) kept.push(record);` | **survived**, `Tests  27 passed (27)` |
| R3-string-filter-contains | `.filter((record) => !record.startsWith('160000 '))` → `.filter((record) => !record.includes('160000 '))` | **survived**, `27 passed (27)` |
| R3-both-filters-contain | both edits above | **survived** the recorded command, and also both full projects: core `Test Files  33 passed \| 2 skipped (35)`, `Tests  968 passed \| 2 skipped (970)`; app `Test Files  88 passed \| 1 skipped (89)`, `Tests  1075 passed \| 2 skipped (1077)` (`mutant-both-contain-*.log`) |
| R3-string-filter-drops-unparseable | `.filter((record) => !record.startsWith('160000 '))` → `.filter((record) => /^1[02]0[0-7]{3} blob /.test(record) \|\| record === '')` | killed, `1 failed \| 26 passed (27)` |

- [Observed] R3-both-filters-contain is not equivalent. With it applied, my probes G9 and G10 return **Observed 0**, silently dropping the real files `160000 x.ts` and `160000 commit/a.ts`, while G16 is unchanged (`probes-mutant-both-contain.json`). This is R3-N3.
- [Observed] The mutants record's `reading` says that a first run at `41225e4a` left `gitlinks-admitted` surviving. I reproduced this: with `code-structure.test.ts` from `41225e4a` (sha256 `26cdcb0f…`) and that mutant applied, the result is `Tests  27 passed (27)`, a survivor. With the `eddf9677` tests it is killed (R9).

### 3d. Byte identity (AC3), re-derived

- [Observed] At the author's fixed path, every recorded digest re-derives exactly (R8). I snapshotted that directory (path, size, sha256 and mtime of all 103 entries) before and after the runs, and the snapshots are identical (`author-fixed-before.json`, `author-fixed-after.json`).
- [Observed] At my own path, `…/lead/b61/reviewer3/fixed-fixture`, head, base and head again are equal for all six parts. The fixture is revision `1f892687…`, with 8 files. The model is 32117 bytes against the recorded 32103, and Trajectory is 28790 against 28783; my path is 6 characters longer. Orrery, Polaris and the POC page match the recorded lengths but differ in digest. Only `codeStructure` (1435 bytes) equals the recorded digest.
- [Observed] The record names the path as `"fixedPath": "<scratchpad>/lead/b61/r2/fixed-fixture"` (`…-r3.json:288`). `<scratchpad>` is not expanded anywhere in the record. I could re-derive the five path-dependent digests only because this session's scratchpad prefix was in my brief (R3-N4).
- [Inferred] The fixture holds no gitlink and no awkward path, so identity on it is expected. The differential (R7) and my probes (§3a) carry the behavioural comparison.

### 3e. Callers (rules 2 and 9)

The denominator is 484 tracked `.ts/.tsx/.mts/.cts/.js/.mjs/.cjs` files at `8afbafcb`. I used `git grep -l -F` and a Python substring scan over `git ls-tree -r -z`, and they agree on every needle.

- [Observed] `observeCodeStructure` appears in 4 files: `code-structure.ts`, `code-structure.test.ts`, `model.ts` and the env-gated `work-items.live.test.ts`.
- [Observed] `buildPocModel(` appears in 12 files. The non-test callers are `production-reobserve.ts:126` and `test-model-fixture.ts:185`. Neither file contains the string `runGit` at all, so both use the default runners.
- [Observed] `NonUtf8GitOutput`, `withoutGitlinkRecords`, `GITLINK_RECORD` and the literal `'160000 '` each appear in exactly 1 file, `code-structure.ts`.
- [Observed] So no production path injects a git runner into the code-structure observer. The only passthrough injector is the env-gated `test-artifact-verification.live.test.ts:124`, and it asserts nothing about `codeStructure` (`:129-137`).

### 3f. N1 sweep (AC5)

The population is the 15 files the diff adds or modifies. 14 of them fall under the fourth sweep's roots and extensions, and 2 of those are raws the sweep exempts.

- [Observed] Method 1 is the sweep's own line predicate, reproduced in Python: 0 hits in 15 files.
- [Observed] Method 2 parses each JSON record and walks every key: 0 swept keys (`source|authority|warrants?|primary|evidence|provenance|cites?|anchor`) hold a value naming the Polaris surface.
- [Observed] The only values naming Polaris are `fixtureByteIdentity.harness.text` in the r2 and r3 records. Both are under `text`, which the sweep does not read.

## 4. Disposition check

- **Round 2 N1 (blocking): an r2 evidence key the PWB-REQ-014 sweep reads.** **Repaired.**
  - [Observed] `0e9937b4` changes exactly lines 21 and 251 of the r2 differential record. Parsing both versions and renaming `source`→`text` on the two harness strings gives equal JSON (`r2_rename_check.py`).
  - [Observed] The full app project passes (R2), and the two-method sweep finds nothing (§3f).
  - [Observed] Neither the pre-rename digest (`983ad896…`) nor the post-rename digest (`730712c1…`) is cited by any of the 2950 tracked files.
  - The rename was the round-2 reviewer's own proposed fix, but the r3 record calls the r2 record "retained unchanged" (R3-N4).
- **Round 2 N2 (blocking): gitlinks at awkward paths made a correct inventory Unknown.** **Repaired for the default runner.** [Observed] Every real-git gitlink probe returns exactly the base outcome: non-UTF-8, quote-leading and LF-holding paths; nested one and two levels down; inside a non-UTF-8 directory; first and last records; gitlinks only; the non-canonical-mode trees (§3a). With a contract-conforming strict injected runner, non-UTF-8 gitlinks still become Unknown with the unreadable reason (R3-N1). That path is test-only (§3e), so I grade it a note, not a re-opening of N2.
- **Round 2 N3 (note): the seam's decoding contract.** **Answered in part.**
  - [Observed] The contract is now stated on both seams (`code-structure.ts:88`; `model.ts:284-285`), and the live test's passthrough decodes strictly (`test-artifact-verification.live.test.ts:124`).
  - [Observed] The disposition routes a byte seam to `syzygy-bpyt.6.5`. `bd show syzygy-bpyt.6.5` (132 lines) has 0 lines naming `R-GP-IMPL`, `N3`, `decoded` or `Buffer`, and `bd comments` reports "No comments on syzygy-bpyt.6.5". So the deferral is not recorded where it is routed. Folded into R3-N1.
- **Round 2 N4 (note): the unreadable reason was unpinned.** **Repaired.** [Observed] `code-structure.test.ts:87` asserts the exact object. The recorded mutant `every-throw-is-non-utf8` is killed (R9).
- **Round 2 N5 (note): identity path and base and head runs unrecorded.** **Mostly answered.**
  - [Observed] `subjectTests` records the head, base and round-2 runs, and all three re-derive (R6).
  - [Observed] The fixed path is named only with an unexpanded `<scratchpad>` placeholder (R3-N4).
- **Round 1 items.**
  - F2 stays filed as `syzygy-bpyt.6.7`, and `bd show` reports it OPEN at P3.
  - F4 is now re-derivable except for the path prefix (R3-N4).
  - F5's missing gitlink class is now in Part B, rows 9 to 13, and re-derives (R7).

## 5. New findings

No finding in this round is blocking. All four are notes.

### R3-N1 — note — a contract-conforming injected runner still turns a non-UTF-8 gitlink into Unknown, with a misnamed reason

- **Evidence.**
  - [Observed] `ObserveCodeStructureInput.runGit` must return "git's stdout decoded as strict UTF-8, or throws" (`code-structure.ts:88`; the same at `model.ts:284-285`). The gitlink byte filter lives only inside the private `defaultRunGit` (`code-structure.ts:103-125`).
  - A conforming injected runner therefore throws on a non-UTF-8 gitlink path before any filter runs. The observer's `catch` (`:147-155`) maps that throw to "repository or revision was unreadable during code-structure observation".
  - §3b reproduces this for G1, G5, G6, G7, G11 and G12, where the base gives a correct Observed.
  - The shared `BuildPocModelInput.runGit` also feeds the worker-change observer. That observer's own default runner decodes lossily (`worker-change-observation.ts:65-71`, `encoding: 'utf8'`). So the stated contract is stricter than one of the two defaults it replaces. [Inferred] A conforming runner would make that observer fall into its "unreadable during worker-change observation" Unknown on non-UTF-8 output.
  - The byte-seam deferral is not recorded on `syzygy-bpyt.6.5` (§4, N3).
- **Failure scenario.** A future caller injects a strict runner, as the seam's own comment asks, against a repository with a submodule under a Latin-1 path. The code-structure region turns Unknown, and its reason misnames the failure class that POC-REQ-003's oracle checks. [Observed] No production caller injects today (§3e), so no gate's output changes.
- **Proposed fix.** Pick one:
  - export the gitlink-dropping strict decoder (`(bytes: Buffer) => string`) and state on the seam that a runner must apply it, or let the seam return bytes;
  - or add a comment and a line on `syzygy-bpyt.6.5` naming this residual and the N3 deferral, so the byte seam inherits it.

  Either way, say in the PR that the gitlink repair covers the default runner only.

### R3-N2 — note — the gitlink filter is a seven-byte prefix test, so an injected record that merely starts with `160000 ` is dropped without a refusal

- **Evidence.**
  - [Observed] Both filters test only the record's first seven bytes or characters: `code-structure.ts:108` and `:167`.
  - Through an injected runner, `160000 garbage` (I1) and `160000  commit …` (I10) are dropped silently, where round 2 refused them as malformed.
  - `160000 blob <id>      12\ta.ts` (I2) is dropped where the base and round 2 recorded `a.ts`. That changes Observed 1 to Observed 0, which is neither the owner-listed output nor a move to Unknown.
  - [Observed] Real git cannot emit these segments: it prints every non-canonical mode as `160000 commit <id>       -` (M2–M4, §3a).
- **Failure scenario.** A test double, or a future runner with its own formatting, emits a malformed record that starts with `160000 `. The record vanishes silently, against AC1's "an unreadable record never becomes a silent skip". [Inferred] Production cannot reach this.
- **Proposed fix.** Drop a record only when its head is a well-formed gitlink: `/^160000 commit [0-9a-f]{40,64} +-\t/` on the decoded string, and the same ASCII head test on the bytes. Everything else then reaches `parseGitLsTree` and refuses. Every real-git row in §3a keeps its outcome under that rule, because each real gitlink head matches it. Add I1 and I2 to the injected test.

### R3-N3 — note — no test pins the filter's start-of-record anchor; a filter that drops real files survives both full projects

- **Evidence.**
  - [Observed] R3-byte-filter-contains, R3-string-filter-contains and R3-both-filters-contain all survive the recorded command (§3c). The combined mutant also survives the full core and app projects.
  - With it applied, the real files `160000 x.ts` and `160000 commit/a.ts` silently disappear (G9, G10).
  - The real-git gitlink test (`code-structure.test.ts:174-198`) has no blob whose path contains `160000 `.
  - This is the AC4 question, "a gitlink filter cannot drop a file record". The code at HEAD answers it correctly (G9, G10), but no test holds it.
  - The owner's review rule asks for "a rule-6 mutant for each predicate" (`OWNER-DIRECTION-…-2026-10-21.md:59-67`).
- **Failure scenario.** A refactor rewrites the prefix test as `includes`, or as an unanchored regex, perhaps while folding it into the 6.5 GitRunner. Every test stays green, and Orrery silently omits a file whose path contains `160000 `. That is a partial inventory served as complete, which POC-REQ-003 forbids.
- **Proposed fix.** Add `record(`100644 blob ${blob}`, Buffer.from('160000 x.ts'))` beside the gitlinks in the real-git test, expect it in the result, and add R3-both-filters-contain to the mutants record as killed.

### R3-N4 — note — two sentences in the r3 evidence are inaccurate or not re-derivable from the record alone

- **Evidence.**
  - [Observed] `…-r3.json:5` says the r2 record is "retained unchanged because docs/reviews/R-GP-IMPL-CODE-STRUCTURE-2-RAW.md cites it". `0e9937b4` changed two of its lines (§4, N1). Values, line numbers and `harness.sha256` are preserved, but "unchanged" is false.
  - [Observed] `…-r3.json:288` gives the fixed path as `<scratchpad>/lead/b61/r2/fixed-fixture`, and the placeholder is defined nowhere in the record. Five of the six recorded per-part digests, and `all`, depend on the full path string (§3d).
  - The stored driver resolves the fixture as `HERE.parent / 'r2' / 'fixed-fixture'`, relative to wherever the driver happens to sit.
- **Failure scenario.** Under rules 10 and 11, a cold reader without this session's scratchpad prefix cannot check the recorded model, Orrery, Polaris, Trajectory and POC digests against the bytes. Separately, a reader trusting "unchanged" would compare the round-2 raw's `:251` quotation (`"source": …`) against a line that now reads `"text"`.
- **Proposed fix.**
  - Write the literal absolute path into `fixedPath` (the harness recreates the fixture there if it is absent, so the string is enough), or normalize `repoRoot` in the harness.
  - Reword `supersedes` to "retained; `0e9937b4` renamed its two harness keys from `source` to `text`, values and line numbers unchanged".

## 6. Verdict per acceptance criterion

1. **`-z` through the shared parser; no unreadable record silently skipped; only gitlinks and non-blob records dropped.** **Met for real git; one injected-only exception (R3-N2).**
   - [Observed] `code-structure.ts:146` asks for `ls-tree -r -z -l` and `:167` calls `parseGitLsTree`. A malformed parse, a missing size, a non-SHA-1 id and a non-NUL-terminated listing each return Unknown (`:162-177`).
   - [Observed] Records dropped without refusal: gitlinks (`:108`, `:167`); non-blob records (`:173`, tree records, I4); and empty records between NULs (`git-tree.ts:31`, I8), which real git never emits.
   - Answer to "whether any other record can be dropped silently": yes, through an injected runner only. Any NUL-terminated segment starting with `160000 ` is dropped whether or not it parses (I1, I10) and even when it is typed `blob` (I2). With real git, no other record is dropped, on the 23 real-git and literal-tree probes run (§3a). [Inferred] This holds generally, since git canonicalizes modes.
2. **New tests fail on base and pass on head; the gitlink tests fail on `45360ea0`.** **Met.** [Observed]
   - R6: base fails the four recorded tests (five with `model.test.ts`).
   - The round-2 module fails both N2 tests, the injected-runner test and the real-git gitlink test.
   - Head passes 10/10 and 27/27.
   - Each run equals the record's `subjectTests`.
3. **Model and Orrery byte-identical on the current fixtures; r3 identity digests re-derive at the named path.** **Met, with R3-N4.** [Observed] All six parts are identical between head and base at two paths. Every recorded digest re-derives at `…/lead/b61/r2/fixed-fixture`, which is the named path once `<scratchpad>` is expanded to this session's prefix.
4. **Round-2 N2 fixed for every gitlink path, default and injected runners; a gitlink filter cannot drop a file record.** **Met for the default runner and for injected strings; not met for a strict injected runner over non-UTF-8 gitlink bytes (R3-N1).**
   - [Observed] §3a: every gitlink class gives the base outcome through the default runner, including a non-UTF-8 gitlink one level down (G5) and two levels down (G7).
   - [Observed] Injected strings with quote-leading or LF gitlinks give the base outcome.
   - [Observed] No file record is dropped by the filter at HEAD (G9, G10), but no test holds that (R3-N3).
5. **Round-2 N1 fixed.** **Met.** [Observed] `polaris-authority-sweep.test.ts` passes 5/5 inside the full app project (R2). Two methods find no swept key naming the Polaris surface in the 15 changed files (§3f).
6. **N3–N5 dispositions hold, and both r3 records reproduce.** **Met for reproduction; dispositions hold in part.**
   - [Observed] All 41 differential rows (R7), all 18 mutants (R9), all identity digests at the author's path (R8) and all three subject-test runs (R6) re-derive at `8afbafcb`, whose subject bytes equal the recorded `eddf9677`.
   - N4 holds. N3 holds except that its deferral is not on bead 6.5 (R3-N1). N5 holds except for the placeholder (R3-N4).
7. **Scope.** **Met for every output a production gate serves; two injected-seam outcomes are listed as notes.** Each changed output, from round 2's list:
   - (a) Owner-listed: valid-UTF-8 paths git would C-quote are now exact Observed (Part A tab, `a "b".txt`, `back\slash.ts`, `ñ.md`; Part B U+FFFD). Unchanged from round 2.
   - (b) Fail-closed: non-UTF-8 file or directory paths go from a wrong quoted Observed to Unknown "code-structure observation produced a path that is not valid UTF-8" (Part B rows 2–4; G13).
   - (c) Fail-closed: blob paths beginning with `"` or holding LF go from a wrong quoted Observed to Unknown malformed (F2, bead 6.7).
   - (d) Fail-closed: a missing blob goes from a partial Observed to Unknown malformed (Part B row 6).
   - (e) Fail-closed: non-40-hex ids go from a false Observed 0 to Unknown malformed.
   - (f) Injected only: unparseable records go to Unknown malformed, except those starting with `160000 ` (see (i)).
   - (g) Injected only, plus the fake-git test for the default runner: newline-format or unterminated listings go to Unknown malformed.
   - (h) **Gone for the default runner.** [Observed] Every real-git gitlink row equals the base (§3a; Part B rows 7 and 9–13). It survives only on the injected seam, as the strict-runner residual (R3-N1).
   - (i) New, injected only: a segment starting with `160000 ` that is not a well-formed gitlink is dropped without refusal. I2 moves from Observed `a.ts` to Observed 0 (R3-N2).
   - Judgement: [Observed] no production caller injects (§3e), and real git cannot emit (i)'s input (§3a). So no changed outcome that a production gate serves lies outside the owner's listed change and the fail-closed class. (h)'s residual and (i) are recorded as notes R3-N1 and R3-N2, not as owner questions. The PR must list (a)–(g), and should mention (h)'s seam residual and (i). Whether it does is [Unknown], because the PR body and the cycle report's owner notice are not in the subject.
8. **Partition.** **Met.** [Observed]
   - R5: 488 files, 488 assigned, 0 unmatched, 0 overlaps, 103 campaigns; `--selftest` 14 fixtures PASS.
   - The README row at `docs/README.md:155` quotes round 1 `REVISE` at `R-GP-IMPL-CODE-STRUCTURE-1-RAW.md:2` ("Verdict: REVISE") over `99adbd03` (`:3`, "Reviewed commit: 99adbd03"), with "one blocking finding and four notes" (F1 blocking, F2–F5 notes, `:121-179`).
   - It quotes round 2 `REVISE` at `R-GP-IMPL-CODE-STRUCTURE-2-RAW.md:2` ("Verdict: REVISE") over `04ba5c8d` (`:3`, "Reviewed commit: 04ba5c8d"), with "two blocking findings and three notes" (N1 and N2 blocking, N3–N5 notes, `:195-269`). All of these match.
   - The row's count column (2) equals the two `R-GP-IMPL-*-RAW.md` files at HEAD. Retaining this raw will make it 3 and the directory 489 files, so the row and the count sentence at `:157` need one integration edit when this raw lands.

**Overall: CONFIRM WITH EXCEPTIONS.**
- Both round-2 blocking findings are repaired at `8afbafcb`. Every recorded row, digest and mutant re-derives, and both test projects, the typecheck and the governance battery pass.
- R3-N1 to R3-N4 are notes. None changes an output a production gate serves, so none blocks merge. Under the owner's stopping rule, this notes-only round clears the bytes it read.

## 7. Out of scope, unchanged by this diff

- [Observed] `code-structure.test.ts:90-94` ("mutation check: a falsifier (empty reason) would fail this assertion") predates this change. It tests a `toBeGreaterThan(0)` assertion that the POC-REQ-003 test no longer uses, so it is now vestigial. It is not a finding against this diff.
- [Observed] Round 2's P18 (a top-level directory literally named `(root)` merging with root files in Orrery) is untouched by this round.

## 8. Cleanup

- [Observed] The worktree's `git status --porcelain` is empty and HEAD is `8afbafcb16e35f875326cab1798f1e8c9dd99b74`. I placed nothing in it.
- [Observed] The lead's `…/lead/b61/r2/fixed-fixture` was used read-only, and its 103-entry snapshot is unchanged.
- [Observed] The scratch clone, my fixed-fixture copy and all probe repositories were deleted after the runs. Before deletion, the reviewer-only files were removed from the clone and the tracked tree was clean.
- Retained under `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/lead/b61/reviewer3/`:
  - harnesses, in `harness/`: the four extracted r3 harnesses (`zz-b61r3-differential.test.ts`, `zz-b61r2-identity.test.ts`, `drive.py`, `mutants.py`) and my `zz-r3-probes.test.ts`;
  - scripts: `hash_at.py`, `extract.py`, `place.py`, `swap_runs.py`, `run_identity.py`, `snapshot_dir.py`, `compare_diff.py`, `compare_mutants.py`, `extra_mutants.py`, `survivor_full.py`, `caller_sweep.py`, `n1_sweep.py`, `r2_rename_check.py`;
  - outputs: `probes.json` (sha256 `2ebf4cde…`), `probes-mutant-both-contain.json`, `differential-rerun.json`, `recorded_mutants_rerun.json`, `extra_mutants_results.json`, `swap_runs.json`, `identity-authorpath-*.json`, `identity-mypath-*.json`, `author-fixed-before.json`, `author-fixed-after.json`;
  - logs: `full-core.log`, `full-app.log`, `typecheck.log`, `check-governance.log`, `recorded_mutants_rerun.log`, `survivor_full.log`, `mutant-both-contain-core.log`, `mutant-both-contain-app.log`, `npm-ci.log`;
  - `regen.diff`.
