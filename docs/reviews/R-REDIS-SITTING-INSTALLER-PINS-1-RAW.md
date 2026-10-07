# R-REDIS-SITTING-INSTALLER-PINS-1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 24a7ea0f666fdd72ecfc69454ec148d9c902723e
Subject: PR #395 (syzygy-s6xo)

Reviewer: fresh-context agent, 2026-10-07. Scope: the PR's own diff
(`git diff origin/main...24a7ea0f`; merge base `75ffd9c2`, 10 files), read
against `REDIS-LOCAL-AGENT-SITTING-BRIEF.md` and its `-REVIEW-NOTES.md`
sibling (notes 1, 4, 5, 6). No owner act was performed, recorded or labelled.
Every record named below was written by scripts in a disposable scratch clone,
and none left it.

## What was run

- [Observed] A rehearsal over the PR head merged into current `origin/main`
  `7f2b8631` (this includes #394's H1-heading stems):
  `scripts/simulate_redis_local_agent_sitting.py --merge refs/remotes/origin/fix/sitting-real-tree-pins --start-instant 2026-10-07T00:05:00Z --vitest --keep`
  (run at 00:28Z, so every act instant was in the past). It used the brief's
  accept-all answers: A, B, C, D variant none, E, F as "No drawer
  (Recommended)" alone (the drawer statement, no provider statement), G, H
  and I. v1.1 was already on the base and was dropped. Results:
  - install exit 0, with all nine recorders and `installed: registrations, rfc5, battery-copies, policy, profile, moved, reconcile, battery, p-104`;
  - the gate sweep accepted every decisions/ file, and `--check` exited 0;
  - `check_governance` reported 32 OK, 21 WARN, 0 FAIL, and the partition exited 0;
  - the battery ran 91 commands with 0 failing;
  - the Butlers read-gate loader test passed after install;
  - full Vitest at the start: 3818 passed and 4 skipped. At the end: 1 failed
    and 3817 passed, and the failure passed on a one-file rerun, so none
    failed beyond the baseline. The report said `green=True`. The scratch
    head was `7ab34c68`.
- [Observed] The `gate-acts.test.ts` real-tree pin (`expectFollowsTree(REAL_ROOT, Date.now())`) passed on that tree. So D9, the
  RFC7-20 reading, the drawer and the registry entry each read `ok`, or
  `stated: true`, with their records present. `real-tree.test.ts` refused
  nothing.
- [Observed] Resolved row written (register line 1115):
  `| P-104 | [Observed] **Resolved 2026-10-07:** the local-agent Redis sitting recorded A (row 1), E (row 2), F (row 3), G (row 4) and H (row 5), by the item letters of the sitting brief, each a separate act. Each act's record is listed in `ACCEPTANCE-ACT-RECORD.md`. | owner acts recorded | a local-agent Redis dossier run, once the post-sitting install and battery pass | `contracts/candidates/REDIS-LOCAL-AGENT-SITTING-BRIEF.md` |`
  It has five cells, matching the register's header. The open-heading
  counts read "the resolved P-53 row included", so resolving the row in
  place does not change them.
- [Observed] Probe for #394: a scratch file
  `decisions/ZZ-SITTING-LOG-PROBE.md` carried only the drawer statement's H1,
  "No kernel evidence drawer — redis-redis". With it present, installer
  `--check` exited 1 and the gate sweep failed:
  `gate-acts.test.ts > … follow this checkout's tree` with
  `ZZ-SITTING-LOG-PROBE.md names the act without being its record`. The
  sweep therefore reads the gate's own form list, headings included, not a
  copy. The probe was removed afterwards.
- [Observed] Second run on the installed tree: it refused at
  `screening-v1 --record exited 1: FAILED: dedicated act already exists`.
  Afterwards `git status --porcelain` was empty and `git stash list` was
  empty, so nothing changed.
- [Observed] Partial answers, on the scratch's pre-install commit: G, C and
  D declined, and F given as the drawer plus `redis-agent-anthropic`. Install
  exited 0, and the row read "… A (row 1), E (row 2), F (rows 3 and 3a) and
  H (row 5) … Row 4 was not taken: the agent may not build or run Redis. …".
  After committing, `--check` exited 0 and `check_governance` reported
  0 FAIL. These six files passed, 253 tests: `screen.test.ts`,
  `check.test.ts`, `public-source-screening.test.ts`, `gate-acts.test.ts`,
  `real-tree.test.ts` and `governance-inputs.test.ts`.
  `governance-inputs.test.ts` read `absent` before the commit, because the
  loader reads committed state. That is a property of the scratch, not a
  defect.
- [Observed] `--selftest` held 39 of 39. Among them: no answer for each
  REQUIRED item is refused; D without C is refused; "a refusal of the answers
  writes nothing"; a P-104 row in neither form is refused; and a P-104 row in
  DECISION-HISTORY.md is refused.

Acceptance criteria: 1 met [Observed]; 2 met [Observed] for the files this
sitting writes; 3 met [Observed for G/C/D declined; Observed via selftest for
required-declined and D-without-C]; 4 met for idempotence and refusal, with
the TS caveat in finding 4; 5 met with the caveats in finding 5.

## Findings

1. NOTE — a date or start instant that is ahead of the clock refuses only
   after every recorder has run.
   `scripts/install_redis_local_agent_sitting.py:191-202` checks only that
   the instants stay on `date`. It never checks that the last instant is at
   or before now. The gate sweep (`:664-668`) then fails, because
   `expectFollowsTree` expects `ok` for a record that exists but is not yet
   in force, and the run stashes. The owner sits at UTC+8 [Inferred from
   commit timestamps], so a local date in the answers file is the likely
   slip. Example: `"date": "2026-10-08"` written at 07:00 local
   (2026-10-07T23:00Z). The default instants then leave the date, which is
   refused with the advice "give a start_instant earlier in the day". Any
   `start_instant` on that date is in the future, so it records everything
   and then refuses. Nothing is left in the tree either way, so this is not
   REVISE. Separately, `simulate_redis_local_agent_sitting.py:226-228` and
   `:257-261` say a future instant makes "the suite pass for the wrong
   reason". [Inferred] For the gate-acts pin the opposite holds: it fails.
   Repair: in `validate_answers`/`plan`, refuse before writing when any
   instant is later than now, and say that `date` is the UTC date. Correct
   the simulator's help text.

2. NOTE — a second run is safe, but its message is misleading. A rerun with
   the same answers fails at the first recorder ("dedicated act already
   exists"), and then prints "the partial state is stashed". In fact nothing
   was written, and no stash was made because the tree was clean.
   Repair: before planning, refuse with "already recorded; run `--check`"
   when the first answered act's dedicated record exists.

3. NOTE — `step_p104` (`:548-562`) matches the open row by prefix
   (`P104_OPEN`, `:525`). Any text an editor later appends to the open row is
   overwritten without notice. One example is a dated stale-sentence marker,
   which AGENTS.md asks for at the sentence. The gate pins the open row by
   its exact sha (`package-reader.ts:550`, `P104_ROW_SHA256`), so an edited
   row already breaks the gate before the sitting. Cosmetic: when F is all
   three statements, the row reads "F (rows 3 and 3a and 3b)".
   Repair: match the whole open row against the gate's pinned digest, or
   refuse when it differs from the bytes pinned on main. Join three row
   numbers as "3, 3a and 3b".

4. NOTE — criterion 4, "never edits TS or test files", holds for this PR's
   delta. It does not hold for the installer as a whole. [Observed] Scratch
   commit `7ab34c68` shows the installer writing:
   - `apps/three-surface-poc/src/governance-inputs.ts` and `governance-inputs.test.ts`;
   - `packages/three-surface-poc-core/src/git-object-reader.ts`;
   - `content-classification.test.ts` and `project-shape-model.test.ts`.

   The cause is the pre-existing `install_redis_sitting.step_policy`
   (`scripts/install_redis_sitting.py:927-967`), called from `install()`
   (`:569`). This is the read-gate re-pin that brief item B, Q2, places in
   the recording commit, so the behaviour is sanctioned and not introduced
   here. The PR adds no TS or test write, and its pins are tree-conditional
   as claimed.
   Repair: none needed in this PR. State the exception in Note 6 or in the
   docstring, so that "the installer never edits TS" is not read as true of
   the whole script.

5. NOTE — evidence records (rule 11 and rule 6):
   - (a) The after arm of the mutant records names commit `4e503a56`, which
     does not exist in this object store (`git cat-file -t` fails). The
     before arm's `c505e00f` is reachable from no ref. Both arms carry
     `subjectDigests` and `old`/`new` per edit for S1–S10, so they can still
     be re-checked by bytes. However, the recorded `check.test.ts` digest
     (`4638b5a3…`) is not the PR head's (`170ed249…`). The whole difference
     is the base-side `schemaVersion: 'polaris-dossier-local-draft-v2'` line
     brought in from main, and the pin under test is unchanged.
   - (b) Both rehearsal records name `baseHead` and `scratch_head`, but give
     no digest of the overlaid installer scripts, which the simulator copies
     from the working directory and not from a commit.
   - (c) `redis-local-agent-sitting-rehearsal-s6xo-p104-2026-10-07.json` is
     `green: false`, because of ENOSPC in
     `check_spec_reconciliation.py --selftest`.
   - (d) Both PR rehearsals ran on a base before #394 (`fa44f77b`,
     `660358d3`), so neither covers the H1 stems. This review's run does,
     over `7f2b8631`.
   - (e) The simulator records only the count of the flaked test, never its
     name.

   Repair: re-run the mutants on a commit pushed to a ref. Record a sha256
   for each overlay file in the rehearsal report, and name rerun-passed
   tests. Cite this review's run, or a fresh one, as the evidence after
   #394.

6. NOTE — the gate sweep's coverage is narrower than "established". In
   `real-tree.test.ts:38-41`, the policy chain, class act and egress reads
   are only required to be `not 'refused'`. So a screening chain that read
   `absent` with its records present would pass the sweep. [Observed] The
   accept-all run did establish it: `screen.test.ts` and `check.test.ts`
   took their recorded arms in the full suite. The gap is only in what
   `gate_sweep` alone proves.
   Repair: add `screen.test.ts` to `GATE_TESTS`, or have the consent
   real-tree test expect `ok` when a policy act record exists.

No REVISE finding. A correctly held sitting, answered as the brief's
accept-all line or with G, C and D declined, installs over the PR head merged
with current main. Every gate source reads ok or established, and Vitest is
green beyond one flake that passed on rerun. Neither the resolved P-104 row
nor any decisions file the run wrote carries a swept form, headings
included.
