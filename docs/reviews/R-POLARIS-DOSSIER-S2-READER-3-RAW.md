Title: R-POLARIS-DOSSIER-S2-READER-3
Reviewed commit: ff481704ca70f5320f91d03b1d7c81ac9dd80da7
Verdict: APPROVE WITH NOTES

Scope: PR #367 at ff481704, which repairs R-POLARIS-DOSSIER-S2-READER-2 (REVISE over f3743f51). Files reviewed:
- `packages/polaris-dossier/src/git-object-reader.ts` (sha256 3798eeb26814b2e38688e66ae346faa015ffc9290695b27c30b9edd87815efdb)
- `packages/polaris-dossier/src/git-object-reader.test.ts` (sha256 169df1e4f405da60280a8d27d9f805203df8c6d07e2111939e86f146aab9fa6c)

The code commits after f3743f51 are 90c35653 (the repair) and 10d4d044 (test bounds). The other four commits touch only `docs/README.md` and the round-2 raw (`git log --stat f3743f51..ff481704`).

Governing text: REQ-polaris-generation-033's reads sentences, `openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md` line 13. I found it with `grep -F "Because the clone's object store lies within the agent sessions' write reach"`. It requires that reads honour no replacement objects, grafts, repository-local configuration, hooks or alternates. It also requires: "Syzygy SHALL recompute the object identifier of every commit, tree and blob it reads on the path from the pinned commit to each blob it uses, from the bytes it read, at every step that uses the object."

Method:
- **Worktree and tests.** I made a scratch worktree at ff481704 and ran `npm ci`. The reader's test file, run with the repository's vitest 3.2.7, gave 58 passed, 0 failed, in 6.33 s [Observed].
- **Prior probes.** I transpiled the reader with esbuild. Round 1's `poc.mjs` (names, bigoffset, swap, cycle, fifo, idxdir, amp ×2) and round 2's `probe2.mjs` (pad, loosepad, wide, dotgit) ran unchanged against it [Observed].
- **New probes.** A new `probe3.mjs` covered:
  - how zlib reports the bytes it consumed when trailing bytes follow the stream;
  - padding inside the bound, reused across many deltas;
  - a loose object padded under the default limits;
  - a 20,000- to 80,000-deep tree chain;
  - a 200,000-entry tree read path by path.
- **Real git stores.** Under `realgit.sh` and `readall.mjs`, git 2.x wrote 15 stores:
  - SHA-1 at `core.compression` -1, 0, 1 and 9, each kept loose, after `gc`, and after `gc --aggressive`;
  - SHA-256 loose and after `gc`;
  - one repack at `--depth=4095 --window=250`.

  Each held a 3 MB random file, a growing random file, a 200,000-line text file, an empty file, a symbolic link and a nested file, over 31 commits. Every blob was listed and read, and its returned bytes were re-hashed independently. Finally, the same script read this repository's own store at origin/main 154e4767 in full [Observed].

## Round-2 findings: confirmed or refuted

- **Finding 1 (padded zlib streams escaped the per-call budget): confirmed repaired.** [Observed]
  - **Pack entries.** `inflateAt` (git-object-reader.ts:397-407) reads `min(storedBound(size), end - start)` once (399). It inflates with `maxOutputLength: size + 1` (402) and refuses `corrupt-object` when the stream needs more (403). The window no longer doubles, and nothing is re-read.
  - **Charging.** Stored bytes consumed are charged (404), beside `size` (398) and delta output (382, 491).
  - **Loose objects.** Loose files are capped at `storedBound(maxObjectBytes)` before reading (330). After inflating, the stored bytes are charged (341), and trailing bytes refuse (342), as does a loose object stored in more than `storedBound(inflated.length)` (343).
  - **Memory.** `readAt` now allocates at most `storedBound(size)` per entry, bounded by `maxObjectBytes`. It no longer allocates up to the pack size.
  - **Probe `pad 50 268435456`.** Round 2 returned all 50 blobs in 51.8 s. Now one, all 50, and all 50 under a 1 MiB budget each refuse `corrupt-object … does not inflate within the 1025 stored bytes git writes for its size`, in 87 ms, 4 ms and 2 ms.
  - **Probe `loosepad 20 134217728`.** Round 2 returned all 20 in 6.9 s. Now it refuses `budget-exceeded` in 404 ms under the 1 MiB budget.
  - **New probe `padloose 268435456` (default limits).** It refuses `corrupt-object … stored in more bytes than git writes for its size` after one pass, in 1,152 ms at 566 MiB RSS.
  - **Padding inside the bound is charged on every reuse.** New probe `inbound 67108864 200 4294967296` builds a 64 MiB base padded to 75,498,489 stored bytes, 7 under `storedBound` (75,498,496), with 200 offset deltas over it. It refuses `budget-exceeded` at the 31st blob (`t00030`), after 7.5 s. That is about 30 × (64 MiB + 72 MiB) ≈ 4 GiB charged, so each reuse pays its stored and inflated bytes.
  - **zlib reports only the stream it consumed.** `bytesWritten` stops at the stream's end when trailing bytes follow: a 19-byte stream plus 17 junk bytes reports 19, and a 217-byte stream plus 100,000 bytes reports 217 (probe `consumed`). So `consumed` in 339 and 402 is the stream's length, and the trailing-bytes check at 342 is sound.
- **Finding 2 (spread regression on a large nested subtree): confirmed repaired.** [Observed]
  - **The fix.** `list` (190-198) threads one accumulator down the recursion and pushes one entry at a time (195). Nothing is spread as arguments any more.
  - **Probe `wide 200000`.** The flat case lists 200,000 in 628 ms. The nested case, which round 2 saw refuse `store-unreadable (RangeError)`, now lists 200,000 in 563 ms.
  - **Order and depth.** Order is unchanged: depth first, in tree order, and the new test pins the first and last paths. A chain of 80,000 nested trees lists in 9.8 s, linear in depth (probe `deep`), so the recursion does not exhaust the stack.
- **Note 3 (fsck spellings of `.git`): repaired.** [Observed] `isDotGit` (218-219) is applied in `parseTree` (231). All seven spellings from round 2's `dotgit` probe now refuse `malformed-tree`. The new test adds 13 refused spellings and 10 accepted near misses (test.ts:531-557).
  - **Against git's predicates.** [Inferred, from general knowledge of git's `is_hfs_dotgit` and `is_ntfs_dotgit`] The predicate covers both. It is slightly broader on NTFS: git stops scanning at the first `:`, but the reader tests every backslash component (for example, it refuses `a:b\.git`, which git accepts). Over-refusal is the safe direction.
  - **No false matches from case folding.** No non-ASCII code point lower-cases to ASCII `g`, `i` or `t` under `toLowerCase`, so the case folding adds none.
- **Note 6 (reader bugs blamed on the store): repaired.** [Observed]
  - **The split.** `step` (121-134) now gives `store-unreadable` only for an error whose `code` matches `^E[A-Z0-9]+$` (129). Every other error is `reader-fault` (130).
  - **Tested.** The new test feeds a bigint `maxObjectBytes` and gets `reader-fault … (TypeError)`.
  - **Node's own codes.** Node's `ERR_*` codes contain an underscore, so they fall to `reader-fault`. Note 3 below covers the one store-caused case this mislabels.

## Earlier probes re-run at the head [Observed]

| Probe | Result at ff481704 |
|---|---|
| names, plus the UTF-8 pair | `malformed-tree`, or `malformed-path` for `..` |
| bigoffset / hugeoffset | `invalid-pack-index` |
| swap / ref-delta-other-base | `identifier-mismatch` |
| cycle | `budget-exceeded` at depth 1,000, in 74 ms |
| fifo | `unsafe-store-entry` in 5 ms (the "still blocked after 5s" line is the PoC's own unconditional timer, as round 2 noted) |
| idxdir, three cases | `unsafe-store-entry` / `invalid-pack-index` / `unsafe-store-entry` |
| amp 100 × 256 MiB | `budget-exceeded` in 3,583 ms, 1.12 GB peak RSS |
| amp 1000 × 1 MiB | `identifier-mismatch` in 303 ms |
| pad / loosepad / wide / dotgit | as in the section above |

No probe from any round now returns content.

## Core guarantee

[Observed] No call returned a byte that fails to re-hash to the consented identifiers.

- **Every construction tried refused or returned verified bytes.** This covers all probes above and the 58 tests.
- **Every real store read in full.** All 15 git-written stores read with `mismatched=0` and listed counts equal to `git ls-tree -r`. That includes compression level 0 (stored blocks), level 9, aggressive repacks, depth-4095 chains and SHA-256. Reading this repository's own store at 154e4767 gave 2,411 entries and 55,399,739 bytes, `mismatched=0`, in 921 ms.
- **The bound does not refuse real git output.** So the new `storedBound` refuses nothing git wrote in these 16 stores.

[Inferred, from the code] The guarantee is structural.
- **Blob bytes.** Blob bytes leave only through `verified` (303-309), which hashes `type size\0body` under the identifier's algorithm and compares it with the identifier the walk reached the blob by.
- **Tree and commit content.** Tree entries and the root tree id are parsed only from bodies `verified` returned (161-164, 203).
- **Delta bases.** Bases are never trusted. Only the final output of a chain is hashed, so a forged base can at most cause a refusal.
- **Excluded inputs.** Nothing reads refs, config, alternates, grafts, `shallow`, `refs/replace/` or a commit-graph. The algorithm comes from the identifier's length (70-74).

## Findings

1. (note) [Observed] `readBlobs` is quadratic in path depth, and the store's author controls the depth. Neither per-call budget bounds this.
   - **Cause.** `blob` rebuilds the path prefix by joining every segment again at each level (`const at = segments.slice(0, i + 1).join('/')`, git-object-reader.ts:174). That is O(D²) characters for a path of D segments.
   - **Measured.** Probe `deep` builds a chain of D nested one-entry trees and reads the single path `a/…/a/f`:

     | D | readBlobs | listTree (same store) |
     |---|---|---|
     | 5,000 | 1.9 s | 1.9 s |
     | 10,000 | 3.0 s | 2.5 s |
     | 80,000 | 83.3 s (68.7 s CPU) | 9.8 s |

     listTree stays linear.
   - **Confirmed as the cause.** In a scratch copy of the transpiled reader (not the repository), I replaced only that line with a constant. `readBlobs` at D = 80,000 then took 9.3 s.
   - **How far it goes.** [Inferred] Only the object budget limits depth: one count per tree read, so about 10^6 per call. Extrapolating the excess quadratically, a 500,000-deep chain gives one call of the order of 45-50 minutes for one path. Such a chain is a pack of about 500,000 small trees, cheap to write.
   - **Why a note and not revise.** No bound the header claims is defeated: bytes, chain depth and objects all hold. The cost arises only if the caller asks for that path, a string of about 10^6 characters. [Inferred, general knowledge] git itself refuses trees deeper than `core.maxTreeDepth` (default 4,096, git 2.43 onward), so no legitimate repository needs more.
   - **Fix.** Accumulate `at` incrementally, or refuse a path deeper than git's tree-depth default. Add a test. Until then, S3 should bound the depth or length of the paths it requests.
2. (note) [Observed] Resolving many paths in one wide tree costs paths × entries. Each segment lookup is a linear `find` over the cached entries (175).
   - **Measured.** Probe `wideread 200000` (one tree of 200,000 blobs):
     - 300 paths at the front of the tree: 0.47 s;
     - 300 at the back: 1.52 s;
     - all 200,000 in one call: 295 s, 327 s CPU, 3.4 GB peak RSS.
   - **Who controls it.** The caller sets the number of paths. At the few hundred sources S3 is expected to read, the cost is about a second. The object budget (10^6) is the only ceiling.
   - **Fix.** A `Map` per verified tree (built in `tree`, 200-206) would make lookups constant. That is optional, unless S3 may read in bulk.
3. (note) [Inferred, from the code and Node's documented `ERR_FS_FILE_TOO_LARGE` limit] Two store-caused failures would still read as `reader-fault`. Only errors whose `code` matches `^E[A-Z0-9]+$` are store faults (129).
   - **Large files.** An `.idx` larger than Node's 2 GiB `readFile` limit (279) throws `ERR_FS_FILE_TOO_LARGE`. So does a loose object above it once `maxObjectBytes` is raised past about 1.7 GiB (331).
   - **A loose file that grows.** A loose file that grows between the size check `fh.stat()` (330) and `fh.readFile()` (331) is read at its new size. `readFile` takes its own `fstat`. The work is then caught: the file is refused at 342 or 343 once inflated. But it can briefly hold up to 2 GiB, and past 2 GiB the refusal reads `reader-fault`.
   - **Severity.** Neither returns content. Both mislabel only the run record's reason. A bounded `fh.read` of `storedBound(maxObjectBytes) + 1` bytes would close both loose cases.
4. (note) [Inferred, from the code] Peak memory is slightly above the stated "about three times `maxObjectBytes`" (34-35).
   - **Where.** While a delta inflates, the base, the stored chunk (up to `storedBound(size)`, about 1.125 × `maxObjectBytes`) and the inflated delta are held together. That is about 3.1 GiB at the default. A loose object holds its stored and inflated bytes together, about 2.1 GiB.
   - **Disposition.** "About" covers it. No change needed unless S3 sizes its process envelope from the comment.
5. (note) [Observed] Uncharged reads are small and bounded per object. The unconsumed tail of each chunk (399) is read but not charged: at most `storedBound(size) - consumed`, about `size/8 + 1024` bytes, for an entry whose `size` is already charged. So is each pack entry's 52- or 64-byte head (355). Both are proportional to what is charged or counted. The header's per-call claims (29-35) hold as written.
6. (note) [Observed] Rule-6 evidence for this repair is not on the branch at the reviewed head.
   - **What is there.** The newest reader mutant record at ff481704 is `docs/evidence/polaris-dossier-git-object-reader-mutants-repair-2026-10-06.json`, which records the round-1 repair at 740cb0bf.
   - **What 10d4d044 says.** Its message reports that the round-2 repair's mutants ran ("P11 and B14 survived the first run") and that the tests were tightened.
   - **What should land.** The record for the final run should store each mutant's `old`/`new` and the run commit, with the two file digests above as the stable anchor.
   - **Tests the round-2 fixes need killed.** The stored-bound refusal (403), the charge of `consumed` (404), the loose trailing-bytes check (342) and stored-bound check (343), the accumulator push (195), the `isDotGit` alternatives (219), and the `reader-fault` split (129-130).
   - **Matching tests exist at test.ts:684-785.** The two `padded` boundary tests sit exactly on `storedBound`, one block either side, so an off-by-one mutant in `storedBound` or its comparison is killed.

## Commits after the reviewed head

At the time of writing, `gh pr view 367` gives `headRefOid` ff481704ca70f5320f91d03b1d7c81ac9dd80da7: no later commit has landed. [Observed]

## Disposition sought

Both round-2 revise findings and both acted-on notes are repaired, with tests, and every probe from rounds 1-3 refuses or returns only verified bytes. Nothing is blocking or revise. Notes 1 and 2 are work costs, not breaches. Note 1 is a one-line fix worth making before S3 reads listed paths. Otherwise S3 should bound the depth of the paths it requests.
