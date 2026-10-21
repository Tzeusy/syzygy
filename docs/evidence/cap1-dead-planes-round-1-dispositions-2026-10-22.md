# Capability 1 dead planes: round-1 review dispositions

[Observed] This record dispositions the notes of
`docs/reviews/R-GP-IMPL-CAP1-DEAD-PLANES-1-RAW.md`, the round-1 CC-REV-1 review
of `syzygy-bpyt.7.2` (pull request #498).

- Verdict: `CONFIRM WITH EXCEPTIONS` (line 2 of the raw).
- Reviewed commit: `9a6b308e` (line 3).
- Subject: `r1-review.diff` sha256
  `bb903636b35dc6c5bed53aaab427e6d1a2ff9d64abb8a37a62c6ccebf7d2683e` (line 4),
  equal to `git diff 32c16625 9a6b308ee2adf4fa26aafcad6c310b6f37b2f711`.

The raw says "No blocking findings." (section 4). Under the owner's notes-only
stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), the round clears the exact bytes it read, and those bytes are not
edited. This record sits beside them and holds every correction the notes ask
for. It is an implementation record and binds nothing.

Revise-severity findings: 0

## N1: the deletion rests on GP-Q0 part 1, and the PR is class 1 and class 4

The only GP-Q0 part 3 row for this bead
(`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`)
reads: "Paths are normalized before the `startsWith` check, if `write-guard.ts`
is kept. This narrows what `authorizeWrite` accepts". `write-guard.ts` was not
kept, so that row was not exercised.

- The deletion rests on GP-Q0 part 1 (behavior-preserving simplification). The
  reviewer judges it within the direction [Inferred by the reviewer].
- [Observed by the reviewer] No rendered byte, wire response, refusal string,
  exit code, state-directory file or fixture-tree file changes: 272 and 240
  identical responses over two independent probes (raw, section 3).
- The reviewer classifies the PR as CC-REV-1 **class 1 and class 4** (SEC-4
  governed-plane writes), not class 1 alone. Both classes require the same
  checks, and the PR's differential and rule-6 runs already meet them.

**Disposition:** the owner notice for the cycle report (`syzygy-bpyt.10`) says
three things:
1. `write-guard.ts` and its 22 tests were deleted under GP-Q0 part 1. The part 3
   row for 7.2 was not exercised.
2. The test-only `authorizeWrite` still accepts `openspec/../README.md`.
3. Any future governed write path is a new class 1/4 change that needs its own
   owner-visible review.

## N2: the CAP1-REQ-046 authority-exposure gap candidate was not filed

**Disposition:** filed as `syzygy-u2a.13`, "CAP1-REQ-046: production supplies
no authority exposures; effective status is derived only in tests". It is
owner-gated: wiring a source changes rendered bytes. It is linked from
`syzygy-u2a.7`, which already carried a provenance note from the
implementation lane.

## N3: three pull-request-body figures are wrong

**Correction.** The pull request body's figures are superseded by these, each
[Observed by the reviewer, reading `req-061.conformance.test.ts:21-154`]:

- `req-061.conformance.test.ts` has 16 tests: 6 pin the widening-field clause,
  5 pin `authorizeWrite`, 2 pin the effect report, and 3 exercise only
  `entry.ts`. `req-integration.conformance.test.ts:226-231` adds one more
  `authorizeWrite` test.
- Deleting `write-boundary.ts` would take conformance from 312 to **298**, not
  296.
- Deleting only `authorizeWrite` would take it to 306, above the bead's 305
  floor. So the widening-field clause does not explain keeping `authorizeWrite`.
  The reason it was kept is acceptance criterion 3, "305+ tests unchanged in
  count and titles".
- CG-1f reads 405 at both base and head, not "405 to 401".
- The CAP1-REQ-061 range in the pull request body, `spec.md:1785-1829`, stops
  inside the requirement's `warrants` block, which ends at line 1835.

**Disposition:** the REQ-061 and REQ-046 decision table, with these figures,
goes into the close reason of `syzygy-bpyt.7.2`. The pull request body is not
edited. No figure above is carried into the cycle report from the pull request
body.

## N4: the test-support entry is unguarded on the import side

**Disposition:** `syzygy-bpyt.7.8`'s acceptance criteria are widened. A second
assertion checks that no non-test `.ts` under `packages/*/src` or `apps/*/src`
imports `@syzygy/cap1-core/testing`, excluding `packages/cap1-conformance/src`
and `packages/cap1-system/src`. It has its own rule-6 mutant: that import
added to `packages/cap1-daemon/src/routes-human.ts`.

## N5: the rule-6 script is not re-runnable without editing it

`docs/evidence/syzygy-bpyt-7-2/mutate.py:14` hard-codes the implementation
worktree. Each result still stores `old`, `new`, `command` and `commitRunAt`,
so rule 6's record requirement is met, and the reviewer rebuilt the mutants
from the record alone.

**Disposition:** no change. Later evidence scripts in this run take the tree as
an argument, as `route-diff.mjs` does.

## N6: the REQ-061 conformance pins `authorizeWrite` without its false permit

**Disposition:** added to `syzygy-bpyt.7.7`, the audit of test-only cap1-core
functions. It will either pin the false permit with a test pointing to
`write-boundary.system.test.ts`, or delete `authorizeWrite` and its six tests as
an owner-visible test-count change.

## N7: consent scope, attribution and prose change no route output

This is pre-existing: base and head are byte-identical. [Observed by the
reviewer] 4 of the pull request's 16 mutated fixtures are byte-identical to the
unmutated one on all 16 route and authorization responses. The reviewer's
attribution and prose-comment fixtures are identical on all 20 of theirs.
CAP1-REQ-011 says scope, attribution and grant state "render with the coverage
boundary".

**Disposition:** routed to `syzygy-u2a.6`, whose outcome is the CAP1-REQ-010 to
016 consent coverage rows, as a provenance note. Later class 1 differentials in
this run report the number of output-distinct fixtures beside the fixture count.

## N8: two failure-path tests become valid-path tests if the builder default changes

**Disposition:** filed as `syzygy-bpyt.7.9`, "Conformance: make each corrupting
replace fail loudly when the builder default changes". Its acceptance is the
reviewer's mutant M03 killed in all five files, with titles unchanged. There is
no effect today, because the default equals the literal.
