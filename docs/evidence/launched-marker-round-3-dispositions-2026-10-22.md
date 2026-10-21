# Launched-marker reader: round-3 review dispositions

[Observed] This record dispositions the notes of
`docs/reviews/R-GP-IMPL-LAUNCHED-MARKER-3-RAW.md`, the round-3 CC-REV-1 review
of `syzygy-bpyt.8.12` (pull request #497).

- Verdict: `CONFIRM WITH EXCEPTIONS` (line 2 of the raw).
- Reviewed commit: `c76050f9` (line 3).
- Subject: `r3-review.diff` sha256
  `3fc4a0b78057e578ca73a7375e3b5facad258dd1aff043d266bd291e43331f0a` (line 4),
  equal to `git diff 32c16625 c76050f9ed21c2e5a7dbfb4b78d6042b5562109e`.

The raw says "No finding is blocking. Each of the following is a note."
(section 5), and counts the changed outcomes as "**More lenient: 0.**"
(section 6). Under the owner's notes-only stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), the round clears the exact bytes it read, and those bytes are not
edited. This record sits beside them and holds every correction the notes ask
for. It is an implementation record and binds nothing.

Revise-severity findings: 0

## R3-N1: the FIFO row's `syzygy-launched` assertion runs on a drained pipe

[Observed by the reviewer] `packages/polaris-dossier/src/launched.test.ts:115-121`
calls `launchFormRefusal` three times on one planted fixture, and the FIFO
fixture writes the marker's bytes once. Under the `any-file-type` mutant the
`terminal` call consumes them, so the `bang` and `syzygy-launched` calls see an
empty pipe. The mutant is still killed, and correctly.

**Correction.** The pull request says the FIFO row is asserted "at
`launchFormRefusal`, where it must count no `syzygy-launched` form". That
holds at the fix only because `isFile()` refuses before any read. The
`syzygy-launched` assertion is never evaluated with data in the pipe.

**Disposition:** filed as `syzygy-bpyt.8.14` (P3, test-only): refill the FIFO,
or plant a fresh one, before each of the three calls.

## R3-N2: the grow-between-reads test fails at `c571fb9f` because its hook never fires there

[Observed by the reviewer] At `c571fb9f` the marker is read with
`fs.readFileSync(fd, 'utf8')`, which on Node v24.6.0 makes 0 calls to
`fs.readSync`. So the `readSync` hook at `launched.test.ts:98` never rewrites the
file, and the test fails at its first `expect` on the unchanged marker. The
fstat-growth case (`:96`) is the one that stages its race at base. At the fix,
the between-reads case is what kills the `read-once` mutant.

**Disposition:** recorded here. The pull request's line "Two tests fail with
`expected 'launched' to be 'unreadable'`" stays literally true, but only the
fstat-growth failure is the race its name describes. The reviewer's
assertion-order fix (assert `rewritten` before the state) is carried in
`syzygy-bpyt.8.14`.

## R3-N3: two of the mutants record's failed-test sets include failures that do not reproduce

[Observed by the reviewer] All 31 mutant outcomes in
`docs/evidence/launched-marker-fail-closed-mutants-2026-10-21-r3.json`
reproduce. Two failed-test sets do not reproduce exactly:

- `rule-unreadable-reason-off` records `Tests  4 failed | 275 passed (279)`.
  Its fourth failure, `review-check > observes only the packet, its digest
  and that the verdict names it: …`, passes in three unloaded re-runs, each
  giving `Tests  3 failed | 276 passed (279)`.
- `foreign-shape-absent` gave 2 extra `review-check` failures on one loaded
  re-run. Unloaded re-runs give the recorded 15.

[Inferred by the reviewer] The extras are timeouts against Vitest's default
5 s test timeout on a loaded host.

**Disposition:** the r3 mutants record is not edited (rule 10). Its
reproducible claim is each mutant's outcome. Its failed-test sets are as
observed under the host's load when it ran. Later mutant harnesses in this
run store each failed test's first error line beside its name, so a timeout
can be told from an assertion failure.

## R3-N4: the docs review-campaign partition check fails at the pull request head on its date alone

[Observed by the reviewer] At `c76050f9` the helper derived the date
`2026-10-22` from the merge commit's committer date, while the count sentence
in `docs/README.md` said `2026-10-21`.

**Disposition:** answered in the commit that retains this raw. The
greenfield-parity campaign row and the count sentence are re-derived by
`scripts/check_docs_review_campaign_partition.py` at that commit, and again
on the final head before merge.
