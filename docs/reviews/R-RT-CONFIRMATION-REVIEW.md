# R-RT Confirmation Review — RTF-1 repair
**Commit:** 00d6020 / **Reviewer:** rt9-confirm (independent fresh-context agent) / **Date:** 2026-08-23

## Verdict: CONFIRMED

### Checks performed (each with [Observed]/[Inferred] and evidence)

1. **HEAD identity.** [Observed] `git rev-parse HEAD` = 00d60208102b26852780e79fb689a66ae553c725; working tree clean before and after review. Full range f0a0f45..00d6020 touches exactly three files: apps/syzygy/src/main.ts, packages/cap1-system/src/state-dir.system.test.ts (new), docs/reviews/R-RT-RUNTIME-REVIEW.md (the review record itself). Nothing else changed since the reviewed commit.

2. **The repair judges symlink reality on both sides.** [Observed] main.ts adds `nearestExistingAncestor` (terminates at '/'), `realLocation` (realpath of nearest existing ancestor + unbuilt tail re-appended — same discipline as the two write-guards), and `governedPlaneViolation(root, stateDir)` which compares `realLocation(stateDir)` against `path.join(realLocation(root), 'openspec'|'.syzygy')` with exact-or-`+ path.sep` prefix. It runs in main() immediately after parseCli, before `evaluateProject`, before `createDaemon`, before any write; a violation folds into the same named `invalid` arm → stderr + exit 1.

3. **RTF-1's exact scenario is refused, verified externally against the built daemon.** [Observed] I reproduced the finding's attack in /tmp (read-only w.r.t. the repo): fixture with `.syzygy/x`, `ln -s <root>/.syzygy/x /tmp/.../sd`, spawned `apps/syzygy/dist/main.js --root <root> --state-dir <sd> --port 0`. Result: exit 1; stderr = "state directory … really resolves to …/.syzygy/x, inside the governed plane (…/.syzygy)"; stdout empty (never "listening at"); find-sweep of `.syzygy/` before/after identical — zero writes.

4. **Falsification on a disposable copy (rule 6 spirit, repo untouched).** [Observed] `git archive f0a0f45` into /tmp, hardlinked node_modules, built, ran the identical scenario against the PRE-fix dist: the daemon STARTED ("listening at http://127.0.0.1:40195/") and wrote `machine-credential.token` (mode 0600) inside `<root>/.syzygy/x/` via the link — the defect exists pre-fix and is closed post-fix; the differential is real, not a vacuous check. Disposable copy deleted.

5. **Residual-bypass probes, all clean.** [Observed]
   - Symlink at an INTERMEDIATE component with a not-yet-existing tail (`mid → .syzygy`, state-dir `mid/sub`): refused, named, real location `…/.syzygy/sub` reported.
   - Root itself reached via symlink (`--root rootlink`, state-dir lexically inside the REAL root's `.syzygy/y`, which the lexical check alone would pass): refused — `realLocation(root)` closes it.
   - DANGLING symlink into a nonexistent governed path (`dangle → .syzygy/gone`): the realpath check cannot resolve it, but the daemon fails closed downstream — exit 1, named `failed to start (credential-unprovisionable): … ENOENT … mkdir`, and `ls` confirms nothing was created inside `.syzygy/` (mkdir(2) on a trailing symlink returns EEXIST/ENOENT rather than following it). No write lands; see residual note below.

6. **The reproducing test is real.** [Observed] state-dir.system.test.ts spawns the BUILT entry via `daemonEntry(REPO_ROOT)` → `apps/syzygy/dist/main.js` (`npm run test:system` runs `npm run build` first, so dist carries the fix); asserts exit code === 1, stderr contains "inside the governed plane" AND the concrete governed target path, stdout lacks "listening at"; and verifies zero writes harness-externally via `snapshotTree` (harness's own sha256+mtime recursive sweep, imports no daemon/core code) with additions/deletions/modified all `[]` and an explicit denominator `compared === before.size`. Second test proves the legitimate case: a state-dir symlink whose real target is benign still starts and serves `/` → 200, clean stop → exit 0. Both passed in the suite run.

7. **No regression; suites better than baseline.** [Observed] Run this session at 00d6020: `npm test` → 53 files, **408 passed**, 0 failed (= review baseline). `npm run typecheck` → clean, exit 0. `npm run test:system` → **14 passed | 1 skipped** across 6+1 files (baseline was 12+1; the +2 are exactly the new state-dir tests; fresh-clone remains gated off by default, as at review time).

8. **No other main.ts behavior changed.** [Observed] The diff adds only: the `node:fs` import, a two-line comment in parseCli, the three new functions, and the main() pre-check. The lexical parseCli check is retained verbatim (parseCli stays fs-pure); flags/envs (`--root/--state-dir/--port`, SYZYGY_*), USAGE, default port/state-dir name, help/invalid exit codes (0/1), refusal format (`syzygy daemon: <detail>\n\n<USAGE>`), clock read, signal handling, and daemon wiring are all untouched.

### Residual risks
- **Dangling-symlink state dir refuses by a different named arm.** A `--state-dir` symlink whose target does not yet exist inside the governed plane passes the startup containment check (realpath cannot see through a dangling link) and instead dies at credential provisioning (`credential-unprovisionable`, ENOENT, exit 1) — fail-closed, zero governed-plane writes observed. Not a write bypass; only the refusal's name is less specific. [Observed]
- **TOCTOU** between `governedPlaneViolation` and the credential write (operator swaps the link mid-startup) persists, matching the prior review's accepted TOCTOU posture for a loopback single-user daemon; `authorizeStateWrite` guards stateDir containment, not the governed plane, so the startup check is the sole governed-plane defense — as designed. [Inferred]

Strictly read-only: no repo edits, no staging, no commits; all fixtures confined to /tmp and deleted; `git status` clean at close.
