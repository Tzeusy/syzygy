# Code structure through `git ls-tree -z`: round-3 review dispositions

[Observed] This record dispositions the four notes of
`docs/reviews/R-GP-IMPL-CODE-STRUCTURE-3-RAW.md`, the round-3 CC-REV-1 review
of `syzygy-bpyt.6.1`.

- Verdict: `CONFIRM WITH EXCEPTIONS` (line 2 of the raw).
- Reviewed commit: `8afbafcb` (line 3).
- Subject: `r3-review.diff` sha256
  `f893bc67913b132ea7dcc46fa21b837a0c39d5f23d124498c3fd7786a4d52f0c` (line 4),
  equal to `git diff fdc866afc4430a63074d52e13418ae319c9aa0a6 8afbafcb16e35f875326cab1798f1e8c9dd99b74`.

The round has no revise-severity finding ("No finding in this round is
blocking. All four are notes.", section 5). Under the owner's notes-only
stopping rule (`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), it clears the exact bytes it read. Those bytes are not edited.
This record sits beside them and holds every correction the notes ask for.
This is an implementation record, and it binds nothing.

Revise-severity findings: 0

## R3-N1: a strict injected runner turns a non-UTF-8 gitlink into Unknown

[Observed] The gitlink byte filter lives only in the private `defaultRunGit`.
A runner injected through the `runGit` seam that decodes strictly, as the
seam's contract asks, still throws on a non-UTF-8 gitlink path, and the
observer then names the wrong reason. No production caller injects a runner,
so no output a production gate serves changes.

**Disposition:** carried to `syzygy-bpyt.6.5` ("one GitRunner") as a comment
dated 2026-10-21. That comment also records round 2's N3 deferral, which the
round-3 reviewer found missing from the bead. The pull request states that the
gitlink repair covers the default runner only.

## R3-N2: the gitlink filter tests only a seven-byte prefix

[Observed] A record that merely starts with `160000 ` is dropped without a
refusal when it comes through an injected runner. Real git cannot emit such a
record.

**Disposition:** filed as `syzygy-bpyt.6.9`, together with R3-N3. Under that
bead, a record is dropped only when its head is a well-formed gitlink, with
tests for the reviewer's cases I1 and I2.

## R3-N3: no test pins the filter's start-of-record anchor

[Observed] Mutants that rewrite the prefix test as "contains" survive both
full projects. At this commit no file record is dropped: the reviewer's G9 and
G10 probes record `160000 x.ts` and `160000 commit/a.ts`. No test holds that
outcome.

**Disposition:** filed as `syzygy-bpyt.6.9`, which must add a real-git blob at
`160000 x.ts` and must kill the three "contains" mutants.

## R3-N4: two sentences in the r3 evidence are inaccurate or under-specified

**Correction 1.** `docs/evidence/code-structure-ls-tree-z-differential-2026-10-21-r3.json`
line 5 says the r2 record is "retained unchanged".

- That is inaccurate. Commit `0e9937b4` renamed the r2 record's two harness
  keys, at lines 21 and 251, from `source` to `text`.
- Values, line numbers and `harness.sha256` are unchanged.
- Read the round-2 raw's quotation of line 251 (`"source": …`) against that
  rename.

**Correction 2.** The same record's `fixtureByteIdentity.fixedPath` (line 288)
reads `<scratchpad>/lead/b61/r2/fixed-fixture`.

- `<scratchpad>` stands for
  `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad`.
- The full path is therefore
  `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/lead/b61/r2/fixed-fixture`.
- Five of the six per-part digests, and `all`, hash that exact string as
  `repoRoot`.
- The identity harness recreates the fixture at that path when it is absent,
  so the string alone is enough to re-derive the digests.
- The round-3 reviewer re-derived every one of them at this path (raw,
  section 6, criterion 3).

## Out of scope, noted by the reviewer

- `code-structure.test.ts:90-94` (the "mutation check" falsifier test)
  predates this change and is now vestigial.
- Round 2's P18 (a top-level directory named `(root)` merging with root files
  in Orrery) is untouched.

Neither is carried here.
