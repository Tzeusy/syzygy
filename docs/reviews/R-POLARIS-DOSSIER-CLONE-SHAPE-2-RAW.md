# R-POLARIS-DOSSIER-CLONE-SHAPE-2
Verdict: REVISE
Reviewed commit: 41c334ba759726985bfa2c7e7859ee506ce407d2
Subject: PR #392 (syzygy-qkea.24)

Reviewer: a fresh-context agent, 2026-10-07. This is round 2.

Network use was limited to `git fetch origin` on this repository. No external
or target repository was fetched, cloned or read. Every probe repository was
built from scratch with `git init` and local commits, and fetched between my
own scratch repositories over `file://`. Two local Docker images already on
the machine were run with `--network none`, only to list their git version
and default template. The scratch worktree at the reviewed commit (after
`npm ci`) and all probe repositories were deleted afterwards. The local git
is 2.53.0.

## What was run

- [Observed] Vitest over `packages/polaris-dossier` at the reviewed commit
  ran 25 files: 726 passed, 1 skipped, 0 failed. This count includes my one
  scratch probe file, which was never committed.
- [Observed] I recomputed sha256 over all nine subjects in
  `docs/evidence/polaris-dossier-clone-allowlist-mutants-2026-10-07.json`
  (`measuredOn.commit` 809bf7f2). At 41c334ba each of the nine equals its
  recorded value. The record therefore describes the reviewed bytes: 39 of
  39 killed.
- [Observed] Mutant Y2 (drop `O_NOFOLLOW`) was re-applied by hand from the
  record's `old`/`new`. The test "reads shallow without following a link"
  then failed, so Y2 is killed as recorded. The file was restored.
- [Observed] A probe test, kept in the scratch worktree only, ran init's
  sequence over about 40 local clones. The sequence was `resolveCloneHead`,
  `cloneGitDirShape`, `openPinnedObjectReader(...).inventory()`, then
  `cloneStoreShape`. After each check, plain git commands ran in the clone
  to see what the agent's git could obtain. The origin held A (root),
  P (parent-only file `secret-parent.txt`), B (the consented commit, parent
  P), and a side branch S (`secret.txt` = `UNCONSENTED-SIDE`).

## Round-1 findings: disposition

| R1 item | Round-1 tag | Disposition at 41c334ba | Evidence |
|---|---|---|---|
| 1 commondir, modules/ | REVISE | **Repaired.** The top level is an allowlist (`GIT_DIR`, clone-shape.ts:37-40), and every other name is refused (clone-shape.ts:117-121). | [Observed] probe 15a: `commondir` refused. Test "refuses every top-level name..." covers commondir, gitdir, modules, worktrees, ORIG_HEAD, BISECT_EXPECTED_REV and rebase-merge. Mutants T1 and T2 are killed. |
| 2 alternates / http-alternates | REVISE | **Repaired.** Both are refused by name, whatever kind of entry, before the walk (clone-shape.ts:107-114). | [Observed] probe 15b refused. Tests cover a file, a link and a relative path. A1 and A2 are killed. |
| N1 non-object names under objects/ | NOTE | **Repaired.** Allowed are fan-out loose objects, an empty `info/`, and paired `.pack`/`.idx` with an optional `.rev`. `.promisor`, `.keep`, `.bitmap`, `tmp_*` and unpaired packs are refused (clone-shape.ts:155-180). | Tests are in "refuses in the object store...". S1-S5 are killed. |
| N2 promisor | NOTE | **Partly repaired.** `*.promisor` is refused. **The promisor configuration in `config` still passes, and it lazily fetches unconsented objects on a plain read.** | See new finding 1 (REVISE). |
| N3 pseudo-refs elsewhere | NOTE | **Repaired** by the allowlist. Reflogs are limited to `logs/HEAD` naming the commit or the zero id (clone-shape.ts:143-153). `info/grafts` is refused. | O1-O3 and L1 are killed. |
| N4 worktrees as a symlink | NOTE | **Repaired.** Every listing entry is `lstat`ed and any link is refused (clone-shape.ts:72-74). | The symlink test covers worktrees, objects/zz, hooks, refs/heads and FETCH_HEAD. Y1 is killed. |
| N5 working tree | NOTE | **Repaired (disclosed).** Both skill texts now say "refuses a `.git` that holds more" and "does not inspect the working tree ... put nothing else in that directory". `init.ts` adds a disclosure. | I3, K3 and K4 are killed. |
| N6 reftable | NOTE | **Not addressed. It stays a NOTE.** | [Observed] probe 02d: under `feature.experimental=true`, git 2.53 makes a reftable repository. The head stage refuses it before clone-shape, which fails closed. This predates the PR. |
| N7 lstat-then-read | NOTE | **Repaired.** `readRegular` opens with `O_NOFOLLOW \| O_NONBLOCK`, checks with `fstat`, and bounds the read (clone-shape.ts:49-67). | Y2 and Y3 are killed. Y2 was re-run by me. |
| N8 unbounded listings | NOTE | **Repaired.** `opendirSync` is read one entry at a time against one walk budget (clone-shape.ts:65-82). | Z1 and Z2 are killed. |
| N9 test gaps | NOTE | **Repaired.** There are fixtures for the non-regular and symlink arms, both bounds, FETCH_HEAD naming another commit, and init running on the printed-commands clone (start-gates.test.ts, preflight round-trip). | — |
| N10 criterion 1 met | NOTE | No change was needed. The printed commands are unchanged since round 1. | — |
| N11 design.md still shows a full clone | NOTE | **Not addressed in this PR.** It is governed, so it is a queue item and not a defect here. It stays a NOTE. | — |

## Probe results (criteria 2 and 3)

| # | Clone | init check | What the agent's git then did |
|---|---|---|---|
| 01 | consented form, B (loose) | PASSED. Top level: FETCH_HEAD, HEAD, config, description, hooks, index, info, logs, objects, refs, shallow | n/a |
| 01b | consented form, A (root) | PASSED | n/a |
| 02 | consented form, default template plus an empty `branches/` (the pre-2.49 default; see finding 2) | **REFUSED**: ".git holds branches, which the consented form never leaves there" | n/a |
| 02b | `init.defaultBranch=trunk` | PASSED | n/a |
| 02c | `init.templateDir` with a real `hooks/pre-commit` | REFUSED: "hooks/pre-commit is not a sample hook" | n/a |
| 02d | `feature.experimental=true` | REFUSED, head stage (reftable; round-1 N6) | n/a |
| 02e/f/g/h | `fetch.writeCommitGraph=true`; `core.logAllRefUpdates=false`; `fetch.unpackLimit=1` (pack kept); `--object-format=sha1` | PASSED (all four) | n/a |
| 03 | consented form, then in `config`: `repositoryformatversion=1`, `extensions.partialClone=origin`, `remote.origin.url=file://<origin>`, `remote.origin.promisor=true`. No `.promisor` file | **PASSED** | `git cat-file -p <P>` printed the unconsented parent commit. `git cat-file -p <S:secret.txt>` printed `UNCONSENTED-SIDE`. Both exited 0, with no network command run by the agent |
| 03b | only `remote.up.url` plus `remote.up.promisor=true`, format v0, no extension | **PASSED** | `cat-file -p <side blob>` printed `UNCONSENTED-SIDE` |
| 03c | `include.path` pointing to a file outside the clone that holds the 03 promisor config | **PASSED** | `git show <side blob>` printed `UNCONSENTED-SIDE` |
| 03d | `includeIf.gitdir:/.path` pointing to the same file | **PASSED** | `cat-file -p <side blob>` printed `UNCONSENTED-SIDE` |
| 03e | `git fetch --depth=1 --filter=blob:none <url> <id>` into an empty repository | the pack carries `.promisor`, so it is refused | config gained `remote "<url>".promisor=true` |
| 04 | `index` naming a foreign blob (`update-index --info-only`) | PASSED | without a promisor, `git diff` failed: "unable to read <id>" |
| 04b | 04 plus `remote.up.promisor=true` | **PASSED** | `git diff` printed `-UNCONSENTED-SIDE` (lazily fetched) |
| 05 | `core.worktree` pointing to another directory | PASSED | `git diff` showed that directory's files against the consented tree. These are files, not objects |
| 06 | `core.alternateRefsCommand` | PASSED | `git log` was unaffected. It is used only in fetch and push negotiation |
| 07 | `git remote add origin <url>` then `fetch --depth=1 origin <id>` (an operator variant) | PASSED. Same top level as 01 | `log --all` showed B only, and `cat-file -e <side blob>` exited 1. History arrives only on an explicit `git fetch` or `pull` |
| 08a/b | `extensions.objectFormat=sha256` and `extensions.refStorage=reftable` on a files/sha1 clone | PASSED | `git log` printed "your current branch appears to be broken" (fails closed) |
| 09 | FETCH_HEAD with pasted free text, an upper-case foreign id, and an id glued to a letter | PASSED | — |
| 09b | FETCH_HEAD whose first line is an upper-case foreign id | PASSED | `git rev-parse FETCH_HEAD` resolved it to the foreign id (a name only; the store check refuses the object) |
| 10 | an empty `refs/remotes/origin/` directory | PASSED | harmless |
| 10b | `refs/` absent | PASSED | git no longer recognises the repository (harmless) |
| 11 | arbitrary text in `info/exclude`, `description` and `hooks/evil.sample` | PASSED | the content is not inspected |
| 12a | `core.hooksPath` pointing to a directory outside with a `post-checkout` hook | **PASSED** | the agent's `git checkout --detach HEAD` ran the hook. The hook ran `git fetch --unshallow`, and `rev-list --all --count` became 4 (full history) |
| 12b | `core.fsmonitor=<command>` | **PASSED** | the agent's `git status` ran the command |
| 13 | `objects/pack` and `objects/info` removed | PASSED | harmless |
| 14 | `logs/HEAD` and `hooks/` removed | PASSED | harmless |
| 16 | `config` of 2 MiB | PASSED | config is not read, so it is not bounded either |
| 17 | `submodule.x.url` in config | PASSED | harmless without a gitlink in the tree |

## New findings

1. **REVISE: `config` is admitted by name and never read. Promisor, include
   and hook configuration in it lets the agent's ordinary read commands
   obtain unconsented objects silently.**
   - [Observed] clone-shape.ts:24-25 says "`config`, `description` and
     `index` must be regular files and are not read (the reader honours no
     repository configuration)", and `GIT_DIR` (clone-shape.ts:38) admits
     `config`.
   - Probes 03, 03b, 03c, 03d and 04b each pass init. Afterwards a
     non-network read by the agent (`git cat-file -p <id>`, `git show <id>`,
     `git diff`) lazily fetched and printed unconsented objects: the
     consented commit's parent and a side-branch blob.
   - Probe 03b needs no `extensions.partialClone` and no `.promisor` pack.
     `remote.<name>.promisor=true` with a URL is enough. Probes 03c and 03d
     put the configuration in a file outside the clone through
     `include.path` or `includeIf`.
   - Probes 12a and 12b show `core.hooksPath` and `core.fsmonitor` running
     an arbitrary command on the agent's `git checkout` or `git status`.
     Probe 12a's hook unshallowed the clone to full history.
   - The reader's "honours no repository configuration" protects Syzygy's
     own reads. It does not protect the agent's git, which is what the
     brief's "your agent reads whatever the clone holds" concerns.
   - None of this is left by the consented form. Each entry has to be
     written into the clone, and the consented form's whole config is the
     four `[core]` lines `repositoryformatversion = 0`, `filemode = true`,
     `bare = false`, `logallrefupdates = true` [Observed, probe 01]. But the
     PR's claim is that init refuses a `.git` holding more than that form
     leaves. A config naming a promisor remote is more, and it is admitted
     without a word in the stated residuals.

   *Repair:*
   - Read `config` the way the other files are read: `O_NOFOLLOW`,
     bounded, as a regular file. Parse it as git's ini syntax, or
     conservatively by line.
   - Admit only a `[core]` section whose keys are among
     `repositoryformatversion` (value 0, or 1 only with no `extensions.*`),
     `filemode`, `bare` (false), `logallrefupdates`, and the
     platform-written `ignorecase`, `precomposeunicode`, `symlinks` and
     `autocrlf`, plus blank and comment lines.
   - Refuse any other section or key by name in the reason: `include`,
     `includeIf`, `remote`, `extensions`, `core.hooksPath`,
     `core.fsmonitor`, `core.worktree` and so on.
   - Reading `config` in order to refuse it is not "honouring" it. Add a
     fixture for each of 03, 03b, 03c, 12a and 12b, and a mutant that skips
     the config check.
   - State the remaining residual: global and system configuration and the
     environment (`~/.gitconfig`, `GIT_CONFIG_*`) lie outside the clone and
     are not checked.

2. **REVISE: a correct consent-form clone made by a mainstream git older
   than about 2.49 is refused, because its default template leaves an empty
   `.git/branches/`.**
   - [Observed] Probe 02 is git 2.53's default template plus an empty
     `branches/` directory, with otherwise the exact printed commands. It
     is refused: ".git holds branches, which the consented form never
     leaves there".
   - [Observed] On this machine, fifteen repositories under
     `/home/tze/GitHub` hold an empty `.git/branches/`. In
     `ai-bootstrap/.git` and `property-agent/.git` its mtime equals
     `description`'s (2026-03-10 and 2026-03-07), so `git init` created it.
     The dpkg logs show git 1:2.34.1-1ubuntu1 installed until 2026-06-12.
   - [Observed] The default templates of git 2.49.1 (docker:28-dind) and
     2.50.1 (an Ubuntu-based runner image), and of the local 2.53.0, hold
     only `description`, `hooks` and `info`.
   - [Inferred] Upstream dropped `branches` from the default template
     somewhere between 2.35 and 2.49. The exact release is [Unknown]: the
     local RelNotes do not name it.
   - [Inferred] Debian 12 (2.39.x), Ubuntu 24.04 LTS (2.43.0) and Apple's
     Xcode git (2.39.x) are mainstream gits a sitting operator is likely to
     use, and they still create it. On those systems every correct
     consent-form clone is refused.
   - The refusal is not actionable. Re-running the printed commands
     reproduces it, and nothing tells the operator that `branches` is
     template residue.
   - The header names this ("a git ... that leaves more in `.git` than git
     2.53.0's default does is refused, failing closed",
     clone-shape.ts:27-28), but the brief's acceptance bar is that the
     consented form made by a mainstream git passes.

   *Repair:*
   - Admit `branches` as an empty directory. Any entry in it, which is a
     legacy remote shorthand, is refused.
   - Derive the allowlist again against at least one pre-2.45 template.
     Copying git's `templates/` from 2.39 or 2.43 into a fixture template
     directory is enough to make a test.
   - Add the fixture, and a mutant that removes `branches`.

3. **NOTE: refusals caused by a non-default template or configuration do
   not say what to change.**
   - [Observed] Probe 02c (an `init.templateDir` with a real hook) is
     refused with "hooks/pre-commit is not a sample hook...". Probe 02d
     (`feature.experimental`) is refused at the head stage.
   - Failing closed is right, and the header discloses it. But the operator
     sees only the reason and the printed command form.

   *Repair:* when the refused entry is a hook, `branches` or another
   template entry, append "make the clone with `git init --template=` (an
   empty template) or git's default template, and no global init
   configuration". Optionally print `git init --template= <dir>` in
   preflight, which also sidesteps finding 2 [Inferred: an empty template
   leaves no hooks, info or description, all of which the allowlist treats
   as optional].

4. **NOTE: `namesOnly` matches lower-case identifiers only, and git
   resolves upper-case ones.**
   - [Observed] clone-shape.ts:88-89 builds `[0-9a-f]` with `\b`. Probe 09b:
     a FETCH_HEAD whose first line is a foreign id in upper case passes,
     and `git rev-parse FETCH_HEAD` resolves it.
   - Only a name is admitted, because the store check still refuses the
     object. With finding 1 repaired, no lazy fetch can follow it.

   *Repair:* match `[0-9a-fA-F]` and lower-case before comparing, or
   require FETCH_HEAD to be exactly the one line git writes.

5. **NOTE: the contents of `description`, `info/exclude`, `hooks/*.sample`,
   `index` and FETCH_HEAD's free text are not inspected.**
   - [Observed] Probes 04 and 11 pass with arbitrary pasted text, or an
     index naming a foreign blob. Without a promisor, git cannot read a
     blob that the index names (probe 04: "unable to read").
   - The header discloses that `description` and `index` are not read. It
     does not say that the content of hooks samples and `info/exclude` is
     not read either.
   - This is the same class as the disclosed working-tree residual:
     content placed deliberately.

   *Repair:* one sentence in the header and the disclosure, such as "the
   content of the template files and the index is not inspected".

6. **NOTE: `core.worktree` and `core.alternateRefsCommand` admit no
   object.**
   - [Observed] Probe 05: `git diff` presents another directory's files as
     the working tree. Probe 06: the command runs only in fetch and push
     negotiation.
   - Both are covered by finding 1's config allowlist. Neither is separately
     REVISE.

7. **NOTE: an operator variant that adds a named remote passes.**
   - [Observed] Probe 07 (`git remote add origin <url>`, then
     `fetch --depth=1 origin <id>`) leaves the same top level as the
     printed form and passes. Nothing unconsented is held, and history
     arrives only on an explicit `git fetch` or `git pull`.
   - This is an agent-chosen network act, so it is a NOTE. Finding 1's
     config allowlist would refuse it. Decide whether that is wanted. It
     makes the check stricter than the consent's text, which names only the
     fetch, not the absence of a remote.

8. **NOTE: the absence of `refs/`, `hooks/` or `logs/HEAD` passes.**
   - [Observed] Probes 10b, 13 and 14 pass. 10b leaves a directory git no
     longer recognises as a repository.
   - This is harmless: it fails closed on the agent's side and admits
     nothing.

## Criteria

- Criterion 1 is met for 10 of the 13 round-1 items: R1, R2, N1, N3-N5 and
  N7-N9 are repaired, and N10 needed no change. N2 is only partly met:
  config-borne promisors remain, as finding 1. N6 and N11 carry over as
  NOTEs.
- Criterion 2 is **not met**. The allowlist admits `config` unread, and
  probes 03, 03b, 03c, 03d, 04b and 12a obtain unconsented objects through
  plain read or checkout commands (finding 1). FETCH_HEAD, `index`, `refs/`
  subdirectories and `info/exclude` admit names or text only (findings 4,
  5 and 8).
- Criterion 3 is **not met** for git older than about 2.49, where the
  default `branches/` is refused (finding 2). It is met for 2.49 to 2.53
  and for `init.defaultBranch`. A custom `init.templateDir` is refused with
  a reason that names the entry but not the remedy (finding 3).
- Criterion 4 is met:
  - the walk is bounded;
  - no process runs;
  - no link is followed;
  - all nine subject digests were re-derived and match;
  - one mutant (Y2) was re-run and killed;
  - each stated predicate has a mutant.

## Counts

REVISE 2 (findings 1 and 2). NOTE 6 (findings 3-8). Round-1 dispositions:
9 repaired, 1 partly repaired (N2, carried into finding 1), and 3 carried as
notes or unchanged (N6, N10, N11).
