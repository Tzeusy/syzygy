RAW FRESH-CONTEXT CORRECTION RE-REVIEW — PR #136
Reviewed commit: 91f84c532b2f64ab95345c02c3f0af0dc8ca22a8
Base commit: 3c915991fbb0eebc38f8daaaea4d05679914b6b8
Manifest-file SHA-256: 221f1ececa321bf0cc6cd5e01f401e9eada38466c3c00dde43095f8cb8a0cd4d
Verdict: REVISE

Fresh-reader restatement: this candidate is a readability-only successor for
the six signed Three-Surface POC artifacts. It keeps the configured Butlers
repository as the one observed project, keeps the POC bounded and non-release,
and changes no implementation or current signed byte. The proposal explains
the scope and non-goals first. The design shows exact-revision code-structure
and revision-stamped Dolt observations entering one PocModel, then feeding
Polaris, Trajectory, Orrery and the machine answer. The specification keeps 24
requirements: each opens with its required behavior, with quantified scope in
a child bullet, while its cases, oracles, scenarios and warrants retain their
predecessor meaning. Missing evidence remains Unknown; no proposal, review,
manifest or merge performs the later owner successor act or grants release.

Fresh-reader ambiguity: none found in the corrected proposal, design or
specification. The Butlers-only boundary is explicit in the top answer,
capability statement, both observation bullets, non-goal, write boundary and
Known Unknown. The three inputs, one-model flow and four consumers are legible
from the diagram and its adjacent text. The later gates are also clear: an
exact owner successor act, then an independently reviewed atomic recorder.

Prior findings:

- The Butlers-scope finding is resolved at this exact head. The proposed
  proposal admits no alternate single-repository reading.
- The unsafe serial signed-byte apply finding is resolved at this exact head.
  The candidate builder exposes no apply command, and a rejected `--apply`
  invocation leaves all six predecessor hashes unchanged.

1. BLOCKING — `scripts/build_three_surface_poc_readability_successor.py:345`:
   the new “late patch failure leaves every signed subject byte-identical”
   predicate never exercises the removed CLI write path. It calls the pure
   `check(late_patches)`, which applies and validates only inside its own
   temporary directory, then rereads the untouched real tree. Running the
   identical predicate against the original buggy commit
   `5db2853e1613d34940e6c33aeb7eaf39a04de98c` returns true even though that
   builder still exposes the serial `--apply --at-adoption` path. The test
   therefore does not fail on the pre-fix behavior and does not protect the
   correction. Exercise the public CLI in an isolated clone or equivalent
   scratch root, corrupt the final patch, require a refusal with all six
   predecessor hashes unchanged, and confirm that restoring the old serial
   apply path makes the regression test fail. Thread:
   https://github.com/Tzeusy/syzygy/pull/136#discussion_r4116243829

Confirmed: the six manifest rows match the exact proposed bytes: four patched
subjects and byte-identical `.openspec.yaml` and `CONTRACT-COVERAGE.md` rows.
An independent parser found 24 predecessor and 24 successor requirements, 24
scenario headings on each side, unchanged ID/title/order, group/form,
normalized normative body, case/oracle/scenario tail and warrants for every
requirement. Strict OpenSpec validation passes. Independent dependency
regeneration reports 24 requirements and 85 distinct authorities and produces
the proposed dependency bytes unchanged. D5, D6 and CC-REV-8 are respected:
the documents are answer-first, the one-model flow has a Mermaid diagram, and
normative modals and qualifications remain attached to their requirement and
scope bullets.

The first raw review remains byte-identical to its evidence commit. The builder
`--check` passes and all 11 current selftest predicates report caught, but the
new predicate has the blocking false-confidence defect above. Governance
reports 32 OK, 20 advisory WARN and 0 FAIL; governance selftest reports 282
fixtures and 0 failing. The docs review partition reports 249 assigned before
this second raw is added, with 0 unmatched and 0 overlaps. Hosted governance
and node checks pass at the reviewed head. Ten open PRs were inspected and none
directly edits the signed Three-Surface POC package. The two original review
threads are resolved; the new regression-test thread remains unresolved.

PR #136 remains Draft. No owner sign-off was offered or performed, no merge or
implementation-ready claim is made, and no Beads lifecycle state was changed.
