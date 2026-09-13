# Review brief — PWB scoped epistemic attributes amendment

Review the exact candidate commit and the manifest without authoring
context. The candidate is inert and must not be treated as an act. The
proposed bytes are the patches under `proposed/` over the current tree,
printed by `python3 scripts/build_pwb_scoped_attributes_amendment.py
--diff`; nothing in `openspec/` or the accepted contract is changed on the
reviewed commit.

This is the fourth round. The first three raw reviews,
`docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-RAW.md` (twenty findings),
`docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-2-RAW.md` (nine) and
`docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-3-RAW.md` (fifteen), all
returned REVISE; every finding is dispositioned in `SEMANTIC-DELTA.md`
§Review.
Judge the repaired bytes on their own, then check that every disposition
holds against them.

Required baseline:

- `VIS-1`, `VIS-2`, `VIS-4`, `VIS-7`;
- `CC-REV-2`, `CC-REV-4`, `CC-REV-6`, `CC-TEST-5`, `CC-TEST-6`;
- `RFC6-22`, `RFC6-23`, `RFC7-16`, `RFC7-33` and `RFC7-34` (both the
  installed module and its candidate mirror); `PWB-REQ-016`;
- the current signed PWB eleven-artifact package and its performed
  2026-09-05 amendment act (`PWB-TRUTH-READINESS-AMENDMENT-ACT.md`);
- the performed RFC-0008/0009 contract successor ceremony
  (`docs/POLARIS-NO-SIGNAL-AMENDMENT-TOOLING.md`) as the shape an RFC-0007
  successor would take;
- the P-67 ruling `POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`;
- the lane A evidence `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`
  and its review `docs/reviews/R-PWB-M1-POLARIS-LANE-A-RAW.md`;
- the comparator sites named in `IMPACT-LEDGER.md`.

Review criteria:

1. Contract: the inheritance rule is stated once, is complete (nearest
   enclosing scope; absent when no scope carries the field; a scope carries
   a field only when every claim under it has that value in the machine
   answer; Claim identity never inherited), and admits no rendering in which
   a claim's expanded tuple can differ from its machine tuple without a
   falsifier firing.
2. Unknown: no reading of the amended text lets a scope value stand in for
   an Unknown claim, fold Unknown into a positive scope, or drop a field
   from any claim in any channel.
3. Oracle: PWB-REQ-007 and -020 each keep an independent oracle that
   expands scopes with its own statement of the rule, imports no rendering
   code, and has a finite falsifier for a scope hiding a differing member;
   the mutation proof names the new class; both denominators are still
   reported.
4. Parity: one tuple per rendered claim survives expansion, multiplicity is
   preserved, and the `collapsed`/`duplicated` falsifiers keep their meaning.
5. Contract delta: the RFC7-33 patch is the smallest change that makes the
   spec text lawful, applies identically to both RFC-0007 mirrors, leaves
   the non-citability sub-clause in force for every rendering, and the
   package says plainly that it binds only by a separate contract act.
6. Unchanged boundaries: the machine answer, the tuple vocabulary, RFC7-16
   per-claim evaluation identity, PWB-REQ-014 (not patched), the per-unit
   claim role, anchors, and PWB-REQ-011/015/016/021/022 are untouched, and
   the delta's "does NOT change" list is accurate against the patches.
7. Package mechanics: the manifest hashes exactly the post-apply bytes of
   the eleven subjects, the builder's `--check`/`--selftest` fail closed for
   manifest drift, patch corruption and contract-mirror drift, the
   candidate cannot bind anything by merge, and the governance checks,
   registry and CI battery see the package.
8. Comprehension: a fresh reader can restate the rule, the saving it buys,
   the risks, the two-act path and the one owner choice without author
   context.
9. Owner packet: one direction decision with its options; the phrase is
   present but stated as not offered; silence and partial answers perform
   nothing; nothing in it authorizes an implementation or a contract change.
10. Non-visual recoverability: against the quoted text of PWB-REQ-016 and
    RFC7-34, a scope-carried value is recoverable by text and structure for
    a reader without vision, the requirement is in the amended clause with
    a falsifier, and the ledger names the accessibility checker.
11. The saving figure the owner is given is derived under the package's
    own rule from a named retained capture by a retained script, labeled,
    and the funnel's earlier figure is marked superseded at its sentences.

The raw review must state the exact reviewed commit, the manifest SHA-256,
one exact verdict from the set `CONFIRM`, `CONFIRM WITH EXCEPTIONS`,
`REVISE`, and every finding with the file
and line it anchors to. A reviewer who authors a semantic fix retires their
review; repaired bytes need a new fresh reviewer.
