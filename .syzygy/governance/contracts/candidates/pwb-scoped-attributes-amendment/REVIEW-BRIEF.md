# Review brief — PWB scoped epistemic attributes amendment

Review the exact candidate commit and the manifest without authoring
context. The candidate is inert and must not be treated as an act. The
proposed bytes are `proposed/*.patch` over the current tree, printed by
`python3 scripts/build_pwb_scoped_attributes_amendment.py --diff`; nothing
in `openspec/` is changed on the reviewed commit.

Required baseline:

- `VIS-1`, `VIS-2`, `VIS-4`, `VIS-7`;
- `CC-REV-2`, `CC-REV-4`, `CC-REV-6`, `CC-TEST-5`, `CC-TEST-6`;
- `RFC6-22`, `RFC6-23`, `RFC7-16`, `RFC7-33`;
- the current signed PWB eleven-artifact package and its performed
  2026-09-05 amendment act (`PWB-TRUTH-READINESS-AMENDMENT-ACT.md`);
- the P-67 ruling `POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`;
- the lane A evidence `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`
  and its review `docs/reviews/R-PWB-M1-POLARIS-LANE-A-RAW.md`;
- the comparator sites named in `IMPACT-LEDGER.md`.

Review criteria:

1. Contract: the inheritance rule is stated once, is complete (nearest
   enclosing scope; absent when no scope carries the field; Claim identity
   never inherited), and admits no rendering in which a claim's expanded
   tuple can differ from its machine tuple without a falsifier firing.
2. Unknown: no reading of the amended text lets a scope value stand in for
   an Unknown claim, fold Unknown into a positive scope, or drop a field
   from any claim in any channel.
3. Oracle: PWB-REQ-007, -014 and -020 each keep an independent oracle that
   expands scopes with its own statement of the rule, imports no rendering
   code, and has a finite falsifier for a scope hiding a differing member;
   the mutation proof names the new class; both denominators are still
   reported.
4. Parity: one tuple per rendered claim survives expansion, multiplicity is
   preserved, and the `collapsed`/`duplicated` falsifiers keep their meaning.
5. Unchanged boundaries: the machine answer, the tuple vocabulary, RFC7-16
   per-claim evaluation identity, the per-unit claim role, anchors, and
   PWB-REQ-011/015/016/021/022 are untouched, and the delta's "does NOT
   change" list is accurate against the patch.
6. Package mechanics: the manifest hashes exactly the post-apply bytes of
   the eleven subjects, the builder's `--check`/`--selftest` fail closed for
   drift and corruption, and the candidate cannot bind anything by merge.
7. Comprehension: a fresh reader can restate the rule, the saving it buys,
   the risks and the one owner choice without author context.
8. Owner packet: one decision, one exact phrase binding exact bytes; silence
   and partial answers perform nothing; nothing in it authorizes an
   implementation.

The raw review must state the exact reviewed commit, the manifest SHA-256,
one exact verdict (`CONFIRM` or `REVISE`), and every finding with the file
and line it anchors to. A reviewer who authors a semantic fix retires their
review; repaired bytes need a new fresh reviewer.
