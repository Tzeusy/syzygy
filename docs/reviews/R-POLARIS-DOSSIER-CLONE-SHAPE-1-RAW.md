# R-POLARIS-DOSSIER-CLONE-SHAPE-1
Verdict: REVISE
Reviewed commit: 1a45e1ae77dd15ad6d788f78f702ffb47e1f63fa
Subject: PR #392 (syzygy-qkea.24)

Reviewer: fresh-context agent, 2026-10-07. Network use was `git fetch origin`
of this repository only. No external or target repository was fetched,
cloned or read. Every probe repository was built locally with `git init` and
local commits in a scratch directory, and deleted afterwards. The scratch
worktree at the reviewed commit (after `npm ci`) was removed.

## Governing text

- The consent, `.syzygy/governance/contracts/candidates/public-repo-admission/instances/redis/OBSERVATION-CONSENT.md`
  (lines 43-44): "The operator fetches each admitted commit alone into a
  local repository used only for the run (`git fetch --depth=1 <upstream>
  <commit>`), so no ancestor commit is transferred". Its Scope (lines 37-41)
  covers "each admitted revision's commit object, and the tree and blob
  objects reachable from that commit's root tree", and not "any other commit".
- Packet row 1, `dossier-local-agent-acts/OWNER-SITTING-PACKET.md` lines
  50-55: "an empty repository, that one fetch, then check out the fetched
  commit. A normal full clone also carries history the consent does not name.
  ... your agent reads whatever the clone holds."
- Sitting brief item A, `REDIS-LOCAL-AGENT-SITTING-BRIEF.md` lines 117-119:
  "make the clone as the record says, one consented commit fetched alone into
  an empty repository, because your agent reads whatever the clone holds".
- Spec v1.1, REQ-polaris-generation-033 (`openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:13`):
  Syzygy's reads "SHALL honour no replacement objects, grafts,
  repository-local configuration, hooks or alternates". The agent's own reads
  are "the operator's own act" (spec.md:399). The spec does not itself require
  a clone-shape check. The check is this PR's protection of the consent's
  stated form, and the review judges it against the PR's own claim and
  criterion 2.

## What was run

- [Observed] Vitest over all of `packages/polaris-dossier` at the reviewed
  commit: 23 files, 710 passed, 1 skipped, 0 failed.
  `start-gates.test.ts`, `agent-texts.test.ts` and `cli.test.ts` alone:
  139 passed.
- [Observed] The nine subject sha256 values in
  `docs/evidence/polaris-dossier-preflight-clone-mutants-2026-10-07.json`
  (measured at `7b83e497`) equal the sha256 of the same nine files at
  `1a45e1ae`. The mutant record therefore describes the reviewed bytes:
  19 of 19 killed.
- [Observed] A probe test, placed in the scratch worktree only, ran the
  `init` sequence (`resolveCloneHead`, then `cloneRefShape`, then
  `openPinnedObjectReader(...).inventory()`, then `cloneStoreShape`, then
  `listTree`) against 40 local clones. It used git 2.53.0. Each extra git
  command that probed what the agent could see ran after the check had
  returned.

### Probe results (criterion 2)

| # | Clone | Result | Within a stated residual? |
|---|---|---|---|
| 01 | consented form, commit with parent (loose objects) | PASSED | n/a (correct) |
| 01b | consented form, 300-file commit (pack + .idx + .rev) | PASSED | n/a (correct) |
| 01c | consented form, root commit | PASSED | n/a (correct) |
| 02 | full clone detached at B | refused, refs (`refs/remotes/origin/HEAD`) | — |
| 02b | full clone with refs/ and packed-refs stripped | refused, store (not shallow, 1 parent) | — |
| 03 | depth-2 fetch | refused, store (shallow at 1 commit, not B) | — |
| 04a/b/c | extra loose branch / packed branch / tag | refused, refs | — |
| 05a/b/c | FETCH_HEAD / ORIG_HEAD / MERGE_HEAD naming another commit | refused, refs | — |
| 05d/e | `BISECT_EXPECTED_REV`, `rebase-merge/orig-head` naming another commit | PASSED | names only, no object; see N3 |
| 06a | `objects/info/alternates` → a full clone's objects | **PASSED**. In that clone, `git cat-file -p S:secret.txt` printed the unconsented blob | see R2 |
| 06b | `objects/info/http-alternates` | PASSED | see R2 |
| 07 | `objects/info/packs` | PASSED | harmless |
| 08a | `.keep` beside the consented pack | PASSED | harmless |
| 08b | `.promisor` pack plus promisor-remote config | PASSED; the agent's git then lazily fetched the unconsented commit on first use | check-runs-only-at-init; see N2 |
| 08c | a foreign `.pack` with no `.idx` | PASSED. `git index-pack` (an agent act) then made it readable | close to the ".idx omits" residual; see N1 |
| 09a | `.git/commondir` → a full clone's `.git` | **PASSED**. `git log --all` listed the foreign history and `cat-file` printed the unconsented blob | **no**; see R1 |
| 09b | `--separate-git-dir` (`.git` is a file) | refused, head stage | — |
| 09c | linked worktree | refused, refs | — |
| 09d | `.git/worktrees` as a symlink to a directory with entries | PASSED | no object admitted; see N4 |
| 10 | reflogs naming another commit | PASSED | names only, no object; see N3 |
| 11 | stash | refused, refs (`refs/stash`) | — |
| 12 | replace ref | refused, refs | — |
| 13a/b/c/g | symlink in refs/, HEAD, packed-refs, shallow | refused | — |
| 13d | objects fan-out directory as a symlink | refused, listing stage (`unsafe-store-entry`) | — |
| 13e/f | symlink under `objects/info`, or `objects/zz` → a foreign pack directory | PASSED | not followed; see N1 |
| 14 | another commit's tree in a pack with a valid .idx | refused, store | — |
| 15 | a foreign loose object under a non-object name (`objects/tmp_obj_<id>`) | PASSED | close to the stated "names it gives" residual; see N1 |
| 16 | a full nested clone in the working tree | PASSED | outside the check's scope; see N5 |
| 17 | consented form under `--ref-format=reftable` | refused, head stage (already the case before this PR) | see N6 |
| 18 | `info/grafts` naming another commit | PASSED | names only |
| 20 | `.git/modules/deps` holding a full gitdir | **PASSED**. `git --git-dir=.git/modules/deps cat-file` printed the unconsented blob | **no**; see R1 |
| 21 | alternates relative into `.git/extra-objects` (a copy of a full store) | **PASSED**. `cat-file` printed the unconsented blob | see R2 |

## Findings

1. **REVISE: the clone may hold unconsented repositories inside `.git`
   under names the check never looks at (`commondir`, `modules/`).**
   [Observed] Probe 09a: a consented-form clone with `.git/commondir` pointing
   at a full clone's `.git` passes every stage. git honours the file:
   `git log --all` in that clone lists the side branch, and
   `git cat-file -p <S>:secret.txt` prints its blob. Probe 20: a full gitdir
   copied to `.git/modules/deps` passes, and git reads it with `--git-dir`.
   The cause is in `packages/polaris-dossier/src/clone-shape.ts`. Its scan is
   a denylist of known locations: HEAD (lines 39-41), `refs/` (43-60),
   `packed-refs` (62-67), `worktrees` (69-75), and `*_HEAD` names at the top
   level (20, 78-84). It also checks `objects/` through the inventory.
   Nothing reads `commondir` or `modules/`, or any other entry of `.git`. The
   header (lines 4-14) states two residuals: init-only, and "the store's
   identifiers are the names it gives". Neither covers these cases. This
   admits unconsented objects, so it breaks criterion 2.
   *Repair:* invert the `.git` scan to an allowlist, with every entry read by
   `lstat` and not followed. At the top level allow only the names the
   consented form and later git use leave there, refusing everything else.
   [Observed] after the printed commands the top level holds `FETCH_HEAD`,
   `HEAD`, `config`, `description`, `hooks`, `index`, `info`, `logs`,
   `objects`, `refs` and `shallow`. [Inferred] `packed-refs` (header-only),
   `ORIG_HEAD`, `COMMIT_EDITMSG` and `branches` are also benign. Refuse
   `commondir`, `gitdir`, `modules` and any unknown name by name. Add one
   fixture for each, and a mutant that drops the allowlist.

2. **REVISE: `objects/info/alternates` and `http-alternates` are not
   refused.** [Observed] Probes 06a and 21 pass, with absolute and with
   relative alternates. In both, git in the clone returns the unconsented blob.
   The reader already detects the file
   (`git-object-reader.ts:349-350`, `alternatesPresent`), but uses it only to
   word an `object-missing` message. The inventory's interface comment
   (`git-object-reader.ts:103`, "an object only an alternate would supply, is
   not named and not counted") states a limit of the count. It is not a
   statement that a clone with alternates passes. The clone-shape header
   cites it only as "see StoreInventory" (clone-shape.ts:13-14). The PR's
   stated residuals for the reviewer were "a pack entry its .idx omits" and
   "init only". [Inferred] The consented form never creates either file, so
   refusing them cannot refuse a correct clone.
   *Repair:* in `cloneStoreShape`, or in the allowlist of R1, refuse when
   `objects/info/alternates` or `objects/info/http-alternates` exists at all,
   whether file, link or anything else. Add a fixture and a mutant for each.

3. **NOTE N1: names under `objects/` that are not objects are passed over,
   so foreign object bytes can sit in the clone.** [Observed] Probes 08c (a
   `.pack` with no `.idx`), 15 (`objects/tmp_obj_<id>`) and 13f
   (`objects/zz` → a foreign pack directory) pass.
   `git-object-reader.ts:360` says "Any other name under `objects/` is not an
   object and is passed over", and line 342 lists `.idx` files only. git
   itself does not serve these objects without an agent act such as
   `index-pack`. They are closest to the stated ".idx omits" residual, which
   names a pack entry rather than a whole pack or a loose file.
   *Repair (cheap):* allow under `objects/` only fan-out directories of valid
   hex names, `info/` (with `packs` and `commit-graph`), and `pack/` holding
   `pack-<hex>.{idx,pack,rev,bitmap,keep,mtimes}` in matched pairs. Refuse
   `.promisor`, a `.pack` without an `.idx`, any symlink, and any other name.
   Otherwise, state the wider residual in the header.

4. **NOTE N2: a promisor configuration passes, and the agent's git then
   fetches unconsented objects silently.** [Observed] In probe 08b, a
   `.promisor` file with `remote.origin.promisor=true` and
   `extensions.partialClone` passes init. The first `git cat-file` for an
   absent object then fetched it from the configured remote. This lies under
   the "check runs only at init" residual, and an agent can always fetch for
   itself. Refusing `*.promisor` (N1) closes the silent form at no cost to
   the consented form. Reading `config` would conflict with the reader's "no
   configuration" posture, so it is not proposed.

5. **NOTE N3: the pseudo-ref check covers `*_HEAD` and `AUTO_MERGE` at the
   top level only** (clone-shape.ts:20, 78-84). [Observed] Probes 05d, 05e,
   10 and 18 pass with `BISECT_EXPECTED_REV`, `rebase-merge/orig-head`,
   reflogs and `info/grafts` naming another commit. They name identifiers
   only, and the store check refuses the objects themselves, so none admits
   content. Either the allowlist of R1 covers them, or the header should say
   that other files may name other identifiers.

6. **NOTE N4: `worktrees` reached through a symlink is not refused.**
   (clone-shape.ts:70). `lstat(...).isDirectory()` is false for a link, so it
   falls through as "no worktree". [Observed] Probe 09d passes. No object is
   admitted, because the store is unchanged. The header promises that a link
   is refused ("a symbolic link or special file refused", line 12), so refuse
   any non-ENOENT `worktrees` that is not a real empty directory.

7. **NOTE N5: the working tree outside `.git` is not checked.** [Observed]
   Probe 16: a full nested clone in the clone directory passes. This is
   consistent with "never reads the working tree" (spec.md:13). But the
   skill texts' "`init` refuses a clone that holds more" (Claude SKILL.md:44,
   Codex SKILL.md:19) could be read as covering it. *Repair:* qualify it as
   "a `.git` that holds more", or have the texts say the directory must
   contain nothing but the printed commands' result.

8. **NOTE N6: the consented form under reftable is refused.** [Observed]
   Probe 17: with `init.defaultRefFormat=reftable` or `--ref-format=reftable`,
   the printed commands make a clone whose HEAD names `refs/heads/.invalid`.
   The existing head stage refuses it (clone-head.ts), before clone-shape.
   This fails closed and predates the PR. [Inferred] It will matter if a
   future git makes reftable the default. *Repair:* print
   `git init --ref-format=files <dir>`, or say in the skill texts that a
   files-format repository is required.

9. **NOTE N7: `readRegular` checks then reads.** In clone-shape.ts:25-33 it
   runs `lstat` and then `readFileSync`, which follows a link swapped in
   between. The header (line 12) says files are read "as the object reader
   reads", but the reader opens with `O_NOFOLLOW | O_NONBLOCK` and checks the
   open handle (git-object-reader.ts `openRegular`). [Inferred] It is
   low-risk, because the race needs a concurrent writer at init. *Repair:*
   reuse the `O_NOFOLLOW` open-then-`fstat` pattern, or say "lstat, then
   read" in the header.

10. **NOTE N8: the bounds and reads match what is stated, with small
    unbounded listings.** [Observed] Every stored identifier and every tree
    entry is counted against `maxObjectsPerCall`
    (git-object-reader.ts:361-381, plus `reachable`). Refs entries are capped
    at 10,000 and files at 1 MiB (clone-shape.ts:18-19). No process is
    spawned. Bodies read are the commit (re-hashed twice, by `rootTree` and
    `parents`) and every tree under it; no blob is read, which matches the
    "every tree re-hashed (blobs are not read)" wording. The following are
    not bounded before the cap applies: `readdirSync(gitDir)` (line 78), each
    `readdirSync` in the refs walk (read in full before the per-entry count),
    `readdir(objects)` and each fan-out listing, and `.idx` bytes (already a
    stated reader residual). This is acceptable. Optionally, state it.

11. **NOTE N9: tests and mutants cover each stated predicate, but not
    clone-shape's own symlink and bound arms.** [Observed] The 19 mutants
    (Q1-Q4, C1-C15) each hit a predicate and all were killed. Fixtures
    `cloneAt` (start-gates.test.ts) and `consentedClone`
    (full-run.testkit.ts) build clones in the consent's form: `git init`,
    `fetch --depth=1 file://<origin> <commit>`, `checkout --detach
    FETCH_HEAD`. The preflight round-trip test runs the printed fixture-b
    block against a bare upstream and asserts `rev-list --all` = [B]. Gaps:
    - no fixture or mutant covers `readRegular`'s non-regular arm (a symlinked
      `packed-refs`, `shallow` or pseudo-ref), the `MAX_REF_ENTRIES` or
      `MAX_FILE_BYTES` caps, or a FETCH_HEAD naming another object (only
      ORIG_HEAD is tested);
    - the round-trip test does not run `init` on the clone that the printed
      commands made, so "printed form passes init" rests on `cloneAt` being
      the same form. [Observed] It is the same form.

    Add the fixtures for R1, R2 and N1 with mutants for each.

12. **NOTE N10: criterion 1 is met.** [Observed] preflight.ts:75-78 prints,
    per revision, `git init <dir>   # <label>: a new, empty directory for
    this revision alone`, then `git -C <dir> fetch --depth=1 <url>
    <commitId>`, then `git -C <dir> checkout --detach FETCH_HEAD`. The fetch
    line is the consent's `git fetch --depth=1 <upstream> <commit>` exactly
    (with `-C <dir>`). The three lines are the packet's "an empty repository,
    that one fetch, then check out the fetched commit". `url` is the parsed
    URL (preflight.ts:37), and no `git clone` is printed (test asserts it).
    Two side notes:
    - `git init` on an existing repository re-initialises it without error.
      The comment's "new, empty directory" and the init check together
      cover that case.
    - The consent's "never a checked-out working tree" (line 45) concerns
      Syzygy's reads. The packet endorses the checkout for the agent.

13. **NOTE N11: the texts and lint are consistent, but the governed design
    still shows a full clone.** [Observed] Both SKILL.md texts carry the
    sentence that `cloneFormFaults` (agent-texts.test.ts:162-166) requires,
    and mutants C14 and C15 are killed. The design of the signed-off spec,
    `openspec/changes/polaris-dossier-local-agent-mode/design.md:37`, still
    reads "git clone <url> <dir>; git checkout <consented revision>". It is
    governed and may not be edited here. Queue it for the next spec version
    (CC-REV-2) or a dated note at that sentence elsewhere, so that a reader of
    the design is not routed to the full-clone form.

## Counts

REVISE 2 (findings 1-2), NOTE 11 (findings 3-13; N1-N11).
Criterion 1: met. Criterion 2: broken by R1 and R2 (commondir, `modules/`,
alternates). Every other probe was refused or is within a stated or harmless
residual, as listed. Criterion 3: met, with N7 and N8. Criterion 4: met for
the stated predicates, with N9. Criterion 5: met, with N5 and N11.
