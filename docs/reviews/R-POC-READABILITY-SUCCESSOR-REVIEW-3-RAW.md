RAW FRESH-CONTEXT CORRECTION RE-REVIEW — PR #136
Reviewed commit: 073c9a47929dbc65a36c1e475b07d6acb2864874
Base commit: 3c915991fbb0eebc38f8daaaea4d05679914b6b8
Manifest-file SHA-256: 221f1ececa321bf0cc6cd5e01f401e9eada38466c3c00dde43095f8cb8a0cd4d
Reviewer: Tzeusy
Risk tier: high
Verdict: REVISE

Fresh-reader restatement: this candidate restyles the bounded, non-release
Three-Surface POC specification for the configured Butlers repository. It
keeps one shared fact model feeding Polaris, Trajectory, Orrery and the machine
answer; every Unknown remains visible, and the positive claims retain
provenance. The proposal states the project boundary, observations,
non-goals and known unknowns. The design shows exact-revision code-structure
and revision-stamped Dolt work observations entering that one model and then
feeding the surfaces. Each of the 24 requirements opens with its required
behavior, with quantified scope beneath it; scenarios and warrants retain
their predecessor meaning. This candidate leaves current signed bytes and
implementation authority unchanged. A later owner successor act and a
separately reviewed recorder remain distinct gates.

Fresh-reader ambiguity: none found in the candidate proposal, design or
requirements. The configured-Butlers boundary is explicit in the answer,
capability, both observation bullets, non-goal, write boundary and Known
Unknowns. The model and surface responsibilities are legible from the
answer-first design and Mermaid flow. The packet offers no sign-off phrase and
states that review, silence or merge performs no act or grants implementation,
deployment or release authority.

Prior findings verified fixed at this head:

- The proposal preserves the configured Butlers repository as the fixed
  observed-project boundary throughout; the former alternate-single-repository
  reading is gone.
- The builder exposes no signed-byte apply path. The current public CLI returns
  2 and leaves all six signed subjects unchanged.
- The new regression runs that public CLI in isolated scratch repositories.
  Restoring the serial writer behavior from 5db2853 makes the predicate fail:
  the old path exits 1 after changing GOVERNING-DEPENDENCIES, design and
  proposal before the corrupted final spec patch is refused. The vacuous
  pure-check test finding is resolved. The exactness qualification below is a
  separate evidence issue.

1. BLOCKING — `docs/evidence/three-surface-poc-readability-cli-mutation-2026-09-28.json:5,29`:
   the method says the exact serial-writer fragments from
   `5db2853e1613d34940e6c33aeb7eaf39a04de98c` were restored, but the complete
   `serial-source-2.new` parser fragment occurs zero times in that source
   commit: it includes the later `--selftest-evidence` option, which the
   historical parser does not have. The unsafe apply function and dispatch
   fragments are present in the historical source, and the behavioral
   counterexample remains valid; that does not make the four-fragment
   exactness statement accurate. Remove the later harness option from the
   historical replacement (or give a precise qualified mapping that meets the
   exact-fragment criterion), rerun the public-CLI mutation, and regenerate the
   evidence with the tested code commit and corrected fragments. Thread:
   https://github.com/Tzeusy/syzygy/pull/136#discussion_r4116429870

2. BLOCKING — `scripts/build_three_surface_poc_readability_successor.py:418`:
   the new regression predicate requires argparse's literal
   `unrecognized arguments: --apply --at-adoption` stderr wording. That wording
   is not a documented CLI contract. A scratch counterexample accepted the
   flags, printed `refusing: owner act and atomic recorder are absent`, exited
   2 and left all six signed subjects unchanged; the current predicate still
   returned false solely because its message differed. Keep the exit and
   unchanged-subject checks plus the historical mutant assertion, but remove
   the message dependency or establish that exact wording as a contract.
   Thread: https://github.com/Tzeusy/syzygy/pull/136#discussion_r4116439530

Exact-byte and semantic checks: the six signed subject blobs are identical at
base, this PR head and current `origin/main`; the candidate manifest has six
rows and hashes to the value above. Four subjects are proposed patches and the
`.openspec.yaml` and `CONTRACT-COVERAGE.md` rows remain byte-identical. The
independent old/new comparison found 24 requirements on each side with matching
IDs, titles, order, groups, forms, normalized normative bodies, scenario
headings and warrants. All 24 semantic-map entries say `meaning-preserved`,
with no semantic-change entries. Independent dependency regeneration reports
24 requirements and 85 distinct authorities. No signed predecessor, `tasks.md`, performed act or existing POC runtime/model
source is edited. The D5, D6, VIS-3/4
and CC-REV-8 source bytes are also unchanged between the PR base and current
main; the intervening main changes do not touch this signed POC subject.

Verification at the reviewed head: candidate `--check` passes; all 11
selftest predicates report caught; dependency `--check` reports 24 / 85;
strict OpenSpec validation reports 5 passed, 0 failed; governance reports 32
OK, 20 WARN and 0 FAIL across 52 checks; governance selftest reports 282
fixtures, 0 failing; and `git diff --check` passes. Hosted `checks` and `node`
are terminal SUCCESS with head SHA 073c9a4. The builder source blob at tested
commit b2c3687 equals the source blob at this reviewed head; the later change
is the retained evidence record. The PR body carries `Tests: +11 ~0 -0` and
identifies the round-two correction as `+0 ~1 -0`. The two exactness and
message-contract findings above remain open. The original scope and
all-or-none findings are resolved; the vacuous-regression thread was answered
and resolved after the independent CLI run.

The docs review partition was 250/250 assigned immediately before this
third-round raw was added, with zero unmatched and zero overlaps. After this
raw and its campaign-row update, run the partition check again. PR #136 remains
Draft and unmerged. No owner sign-off or Beads lifecycle change was performed.
