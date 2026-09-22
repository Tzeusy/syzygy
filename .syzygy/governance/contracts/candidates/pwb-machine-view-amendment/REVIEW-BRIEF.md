# Review brief — PWB machine-view amendment

Review the exact candidate commit and the manifest without authoring
context. The candidate is inert and must not be treated as an act. The
proposed bytes are the patches under `proposed/` over the current tree,
printed by `python3 scripts/build_pwb_machine_view_amendment.py --diff`;
nothing in `openspec/` is changed on the reviewed commit.

**Three rounds have been run against this brief** (the first draft said
here "This is the first round. No review has been run against these
bytes"). Round 1 returned CONFIRM WITH EXCEPTIONS
(`docs/reviews/R-PWB-MACHINE-VIEW-DELTA-RAW.md`); round 2, over the repaired
bytes at `9d74185`, returned CONFIRM WITH EXCEPTIONS
(`docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-RAW.md`); round 3, over
the repaired bytes at `76b4beb`, returned CONFIRM WITH EXCEPTIONS
(`docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-2-RAW.md`).
Dispositions of all three are in `SEMANTIC-DELTA.md` §Review; the repairs
after each round edited prose only and are not covered by that round's
verdict (rule 10). This brief stays live as the commission for any further
round.

Required baseline:

- `VIS-1`, `VIS-2`, `VIS-4`, `VIS-7`;
- `CC-REV-1`, `CC-REV-2`, `CC-REV-4`, `CC-REV-6`, `CC-TEST-5`, `CC-TEST-6`;
- `CC-SPEC-*` and `CC-IMPACT-*` in
  `.syzygy/governance/contracts/candidates/policy-candidates/` (in force
  despite the path);
- `RFC6-13`, `RFC6-14`, `RFC6-21`, `RFC6-22`, `RFC6-23`, `RFC7-1`,
  `RFC7-18`, `RFC7-33` — PWB-REQ-020's own warrant set, plus `RFC6-21`,
  which this package argues about and does not amend;
- `PWB-REQ-004`, `PWB-REQ-011`, `PWB-REQ-014`, `PWB-REQ-016` and
  `PWB-REQ-020` in the signed PWB eleven-artifact package, and its performed
  2026-09-05 amendment act (`PWB-TRUTH-READINESS-AMENDMENT-ACT.md`);
- the owner's ruling record
  `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
  — P-72, P-76, P-77, P-78 and its cross-cutting readings;
- the sibling candidates
  `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/`
  (same eleven subjects) and the registry-currency package that mints the
  briefing ceiling;
- the sites named in `IMPACT-LEDGER.md`, in particular
  `apps/three-surface-poc/src/routes.ts`,
  `apps/three-surface-poc/src/polaris-presentation-route.test.ts` and
  `packages/three-surface-poc-core/src/project-shape-observation.ts`;
- `SEMANTIC-DELTA-TEMPLATE.md` and `NORMATIVE-CHANGE-WORKFLOW.md`, against
  which the form and the class claim are judged.

Review criteria:

1. **Change class.** The delta claims Normative and contradicts its own
   source analysis, which recommends Clarifying. Test the claim in both
   directions: is any added obligation real (a compliant route that stops
   being compliant), and is anything narrowed or removed that the delta
   does not disclose?
2. **Closure.** Both categories are closed by enumeration. Check that no
   reading of the inserted text admits an unnamed route by inference, that
   the stated way in (a later amendment naming a member) is unambiguous,
   and that "a route in neither category is neither admitted nor forbidden
   by this requirement" does not accidentally license a route the project
   has not authorized elsewhere.
3. **The two categories are genuinely two.** Check the disjointness claim:
   a generated draft is not composed from the machine answer, and the
   second category therefore cannot be a widening of the first. Check that
   the draft view's "contributes to neither multiset" sentence is true of
   every field such a view would carry.
4. **Parity is not weakened.** PWB-REQ-020's Case, Observable, Oracle,
   Oracle-independence, Mutation proof, Falsifier, Scenario and warrants
   must be byte-identical, and the scoping sentence must not let a fact
   leave the compared multisets by being rendered in a derived view.
5. **`RFC6-21`.** The delta takes a narrow reading of "endpoints always
   serve the full set" and discloses the wide one. Decide it. If the wide
   reading holds, an `RFC-0006` amendment and a second owner act are
   needed, and that is a finding, not a question.
6. **The ceiling precondition.** The specification states a precondition on
   service without naming a registry field. Check that this is coherent
   when the registry act has not been performed, that it creates no
   dangling literal, and that it does not silently constrain the existing
   member, whose ceiling the registry already declares.
7. **Unchanged boundaries.** The delta's "What explicitly does NOT change"
   list is a claim about eleven things. Test it against the patches,
   especially the four not-amended requirements, `design.md`, the
   contract-coverage matrix and the registry entry.
8. **Blast radius.** The ledger's 121-over-1,334 figure, its two methods,
   its nine continuation-form files and its "nothing becomes false"
   conclusion. Re-derive rather than re-read; the denominator must cover
   the forms the identifier occurs in.
9. **Package mechanics.** The manifest hashes exactly the post-apply bytes
   of the eleven subjects; the dependency declaration is regenerated from
   the proposed specification rather than transcribed; the builder's
   `--check` and `--selftest` fail closed for manifest drift, context-line
   and added-line patch corruption, a transcribed declaration, a spec whose
   warrants stop validating, sibling drift and a missing sibling patch; and
   the candidate cannot bind anything by merge.
10. **Sibling ordering.** The claim that the two specification patches
    compose in either order, that only the generated declaration is
    order-dependent, and that the second package signed must be regenerated
    before its act.
11. **Comprehension.** A fresh reader can restate what the two categories
    are, which routes are members, what a member must satisfy, what the
    owner is being asked, and what adoption does *not* authorize, without
    author context.
12. **Owner packet.** One decision with its options; the sign-off phrase
    present but stated as not offered; the quoted manifest digest equal to
    the file the builder writes; silence, a commit and a merge perform
    nothing; nothing in it authorizes an implementation, a route or a
    registry edit.

The raw review must state the exact reviewed commit, the manifest SHA-256,
one exact verdict from the set `CONFIRM`, `CONFIRM WITH EXCEPTIONS`,
`REVISE`, and every finding with the file and line it anchors to. A reviewer
who authors a semantic fix retires their review; repaired bytes need a new
fresh reviewer.
