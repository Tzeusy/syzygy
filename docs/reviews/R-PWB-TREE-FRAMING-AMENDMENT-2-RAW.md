# Independent review, round 2 — PWB tree framing amendment (PWB-REQ-014)

Reviewed commit: 8e45097e2af3be8bbff929c717eb3eefae59d608
Manifest SHA-256: dbbceeae1e62cd6c103bb7581e619efcdc4414241716ba2587ba57456ac2f9cf
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer context: fresh; read through a detached worktree in a private scratch directory; repository unedited. ROUND-1-DISPOSITIONS.md treated as repair history only.

## Mechanics (all [Observed])

- Manifest file SHA-256 recomputed at the commit: `dbbceeae1e62cd6c103bb7581e619efcdc4414241716ba2587ba57456ac2f9cf` (matches).
- `build_pwb_tree_framing_amendment.py --check`: "matches 11 proposed subjects (5 patched); 0 pending sibling spec patches compose (0 applied, 8 performed by record, 1 declined, none unclassified)". `--selftest`: every line "caught", "117 package predicates fail closed". `--diff` runs.
- All five patches applied in a scratch mirror; `sha256sum -c` over the eleven manifest rows: zero mismatches. `build_polaris_project_wide_contract_coverage.py --check` ("324 clauses represented") and `build_polaris_project_wide_spec_dependencies.py --check` ("17 requirement(s)") pass over it. `check_governance.py` on the pristine commit: 0 FAIL.
- Scope: `git diff -U0` of spec.md shows every hunk between lines 1363 and 1558, inside the PWB-REQ-014 block (heading at 1344, PWB-REQ-015 heading at 1564 after patch). Requirement count stays 17. No other requirement, scenario or the reading guide moves. No signed byte is edited by the candidate (applying happens only in scratch).
- CAPABILITY-COVERAGE rows re-derived: 33 rows, 27 covered, 6 lawfully out of scope (matches the patch).
- Citer sweep re-run with the ledger's published predicates at a0d218a: 1,886 paths, 4 binary; literal 99; run-predicate adds 9; 108 total; split 23/3/1/8/65/6/2 (matches). Sibling spec patches: 12 tracked, minus this package, minus 2 other-specification patches = 9 (8 performed + 1 declined), matches the ledger.
- `--apply` without `--at-adoption` is refused (rc 2, nothing written). `--apply --at-adoption` over a mutated patch ("SEC-3" removed) refuses with fragment, dependency-digest and manifest findings and leaves every signed-subject byte unchanged (only the mutated patch showed in `git status`).
- Rule 6, mutation 1 (the patch's "SHALL NOT count claims, sources or rows" replaced by "MAY count claims"): `--check` fails with "expected one 'An opening SHALL NOT count claims, sources or rows', found 0". Mutation 2 (sibling classification guard: an extra hunk appended to the performed `pwb-item-depth-amendment` spec patch): `--check` fails "sibling spec patch is neither pending, applied, performed nor declined". Mutation 3 (the doctrine warrant): caught by the pinned fragment. Mutation 4 (a falsifier clause removed) was caught only by digest drift; see Finding 4.

## Findings

**Finding 1 — an opening over a group with no rendered child has no weakest label** (note)
`proposed/spec.md.patch` "An opening SHALL carry the weakest label among that group's children, in the order Observed, Inferred, Unknown". For an empty project catalog or evidence group the minimum is over the empty set. Read with VIS-2 the intended answer is Unknown, and an empty group may fall under the "withheld child counts as Unknown" clause, but the text does not state it. Not a counterexample to any neighbouring requirement; an implementer would have to choose. Worth one clause at the next amendment.

**Finding 2 — the followed review record has no stated failure path** (note)
The Diagrams clause requires the machine narrative to name the review record by path and SHA-256, and a relationship that record does not list owes nothing. It does not say what a page does when no record is named, or when the named record cannot be read or does not hash to the stated digest. Read literally the owed set is then empty and the page conforms silently, the favourable direction under VIS-2. The delta's open point 2 covers who decides which diagrams are owed, not this binding failure. Disclosed-as-Unknown behaviour would close it.

**Finding 3 — openings are labelled claims that carry only a label** (note)
PWB-REQ-007 requires a tier, one primary reason and freshness for every project-fact claim and for aggregates. The patch gives an opening a label, scope and routes, mints no reason and no tier or freshness, and the delta argues it is neither an aggregate nor a Claim (PWB-REQ-014 keeps narrative blocks a distinct machine type). That reading holds and I could not build a counterexample, but the opening's copy role `project-fact` shares a name with PWB-REQ-007's "project-fact claim". The two role vocabularies are distinct (012 copy role; 014 claim role), yet an implementer or a later reviewer may conflate them. Also, an opening that must state a label, a scope and a route within PWB-REQ-012's twenty-word lede cap is satisfiable only by stating few children; the patch permits that (scope is named), so no contradiction.

**Finding 4 — the added verification bullets and falsifier clauses are pinned only by the manifest digest** (note)
`REQUIRED_ONCE` in `scripts/build_pwb_tree_framing_amendment.py` (lines 279-346) pins the Tree form, Diagrams, scenario and warrant fragments, but none of the additions to the case, oracle, oracle-independence and falsifier bullets. I removed a falsifier clause and ran `--write` then `--check`: both passed. The manifest digest does bind the bytes to this review, so rule 10 holds; the selftest does not claim to mutate those bullets. A pinned fragment per added bullet would make a later hand edit fail on meaning, not only on a digest that `--write` re-mints.

**Finding 5 — a supported edge whose endpoint has no claim has no stated reason** (note)
"Drawable" needs one supported edge and every drawn node needs a claim; an undrawn element carries an Unknown claim's reason or `missing-declaration` "where no claim establishes it". An Observed edge claim whose endpoint node no claim establishes is neither drawable (no node) nor in either reason class. In the current model edge claims relate model entities, so I could not construct it from today's data; it is a totality gap only if the model ever holds an edge claim over an unclaimed node. Not blocking.

## Criteria walk-through

1. Scope: no moved byte outside PWB-REQ-014, design decision 11 and its two risk lines, the two proposal sub-bullets, coverage row 33 and the regenerated dependencies. Holds.
2. Butlers text verbatim: the opening "names only which declared text follows", "SHALL NOT paraphrase, condense or stand in", tree form is stated for "Syzygy-authored framing". I could not build a reading that licenses paraphrase. Holds.
3. True summaries: "states only what that group's own rendered children state" is testable via the claim-to-child mapping named in the oracle-independence bullet; an omitted Unknown child still forces the Unknown label. The four group classes are enumerable; one copy role and one claim role are stated. Holds (Findings 1, 3).
4. One aggregate: openings count nothing, so no second Unknown aggregate; the label rule is the weakest child. Holds.
5. Diagram support: edgeless or all-Unknown relationships are not drawn and carry each element's reason; a partly supported relationship is drawn partial with undrawn elements named; a node drawn from a label is barred; an element is drawn Unknown only where a claim establishes it; a prose-sufficient relationship owes nothing. Holds (Findings 2, 5).
6. Inert render: allow-list classes match the 2026-09-28 SVG ruling (shapes, paths, text, styling; script, handlers, animation, foreignObject, links, external or unsafe references excluded); validation precedes a sink; failure emits no SVG and keeps the text equivalent. PWB-REQ-006 is not amended; its own sink-scan oracle still reads any `<svg>` as an active sentinel, and the 014 oracle clause plus the ledger disclose this. Acceptable.
7. Neighbouring authority: I found no counterexample to PWB-REQ-006, 007, 010, 011, 012, 015, 016, 020, 021 or RFC7-2/13/17 beyond the points above. The six open points are accurate and complete for what I could test.
8. Package mechanics: see Mechanics above.
9. Budget: the table is labelled [Observed] and the projection [Inferred]; the 32-opening count is marked Inferred with its non-retention disclosed; the machine JSON sink is marked [Unknown]. 32 x 600 B plus 6,227 and 4,031 B is about 29 KB, consistent with the stated ~30 KB and ~150 KB headroom. Honest.
10. Owner boundary: no phrase offered, no chain position, no landing order, no implementation authorized. Holds.
11. Comprehension: the resolution diagram repeats the text and adds no state or route; the two later gates (sign-off, then fresh implementation authorization) are stated in the delta's migration plan.

No blocking or revise defect found.
