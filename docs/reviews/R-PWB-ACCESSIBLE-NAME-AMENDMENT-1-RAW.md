# R-PWB-ACCESSIBLE-NAME-AMENDMENT-1 — fresh-context review, PWB accessible-name amendment (PWB-REQ-016), round 1
Reviewed commit: 0241fb835471af3a2ea23119959bdfa34ef14464
Manifest SHA-256: 96516b62a2eeecc88ec37e3b7249bbb1609d19fd1493d393bf47937789b76e63
Verdict: REVISE

Package: `.syzygy/governance/contracts/candidates/pwb-accessible-name-amendment/`
(manifest `PWB-ACCESSIBLE-NAME-AMENDMENT-MANIFEST.txt`; the head digest above
is the sha256 of that file's bytes at the reviewed commit, computed by
`git show <commit>:<path> | sha256sum`). Brief:
`pwb-opening-index-amendment/REVIEW-BRIEF.md`. Reviewed in one round with the
opening-index package; this raw judges package C only.

## Mechanics run (fresh clone at the reviewed commit)

[Observed] All from the clone root, exit codes and output read:

- `build_pwb_accessible_name_amendment.py --check` — exit 0:
  "accessible-name candidate matches 11 proposed subjects (2 patched); 17
  requirements, 53 scenarios; structure, regeneration, contract coverage,
  sibling classification and pending-sibling composition verify".
- `build_pwb_accessible_name_amendment.py --selftest` — exit 0: "16
  structure mutants, declaration tampering, patch drift, drifted composition
  and an unclassified sibling all fail closed on their own predicates". Each
  mutant has a predicate-specific expected prefix
  (`pwb_requirement_amendment.py:497`).
- `build_pwb_opening_index_amendment.py --check` / `--selftest` — exit 0.
- `build_pwb_class_granular_extraction_amendment.py --check` and
  `build_pwb_release_label_amendment.py --check` — exit 0.
- `check_governance.py` — "31 OK, 21 WARN, 0 FAIL (52 checks)".
- `check_spec_reconciliation.py --check` — "7 of 7 predicates without FAIL;
  PASS" (R6 WARN on the two stale behaviour-contract pins, pre-existing).
- Composition, independently: all 24 application orders of the four pending
  spec patches apply and yield one identical result.
- `git diff c371339d 0241fb83 -- openspec` is empty. Reading the patch, each
  of the three `replaced` lines survives as the prefix of its extended limb,
  and the warrants block is untouched. The Three-Surface POC specification is
  not touched.
- Impact-ledger census re-derived with the ledger's published regex over the
  2,006 paths at `c371339d`: 92 files cite PWB-REQ-016, and every area count
  (27/22/28/5/1/2/7) reproduces.
- The delta's claims about today's checker hold at `c371339d`:
  `polaris-accessibility.ts:523-540` checks for a non-empty name on roles in
  `NAMED_ROLES` (line 356: link, heading, region, navigation) and compares
  link counts. The file has 0 occurrences of `level` over 567 lines.
- The finding ids cited (S15-F1, S2-F2, S2-F3) match the pursuit data file's
  titles for shared accessible names and the checker's small population. No
  figure from them is quoted in the package; the current figures are stated
  as [Unknown].

Criterion 2 (scope) is met: the patch touches only PWB-REQ-016, and slice D
is put to the owner with the one-category reasoning (packet question 4). The
revise finding is against criterion 3.

## Findings

**Finding 1 — The obligations bind every Polaris page, but the sweep covers "a page"; the page population has no denominator** (revise)

Anchor: `proposed/spec.md.patch:6` ("On a Polaris page, two interactive
elements …"), `:13` ("A Polaris page SHALL have exactly one level-1
heading"), `:16-19` ("The checks in this requirement SHALL run over the
complete interactive and heading population of a page rendered from a
whole-project evaluation"), and the Case at `:31-33` ("run the distinct-name
and heading-order checks over a page rendered from a whole-project
evaluation").

CC-SPEC-4 requires an invariant to state "the scope of quantification, a
counterexample schema, and the sweep whose denominator bounds it". Here the
scope is every Polaris page, but the sweep is one page, and nothing says
which. Polaris serves more than its entry page: PWB-REQ-011's exact-source
route serves each admitted source in `requirement-sections` or `whole-body`
mode, and PWB-REQ-016's own signed Case already traverses "every …
exact-source path". The pursuit finding this slice rests on (S15-F1) is
about links into that route. The new falsifier, "a check run over a
population smaller than the rendered page's", bounds elements within a page
and not pages within Polaris. An implementation could check `/polaris` only
and satisfy the oracle while every other Polaris page goes unchecked.

[Inferred, not checked against the renderer, which is outside this brief's
reading list] If the exact-source route is in scope, the heading-order rule
may conflict with PWB-REQ-011's verbatim rendering whenever a served Butlers
body's own heading structure skips a level and is rendered as HTML headings.
The amendment should say whether verbatim source bodies are inside the
heading population, and if so which requirement yields.

Repair direction: name the page population, for example the entry page, each
item-detail page and each exact-source route response at one evaluation, and
make the page count a reported denominator beside the per-page ones. Or
narrow "a Polaris page" to the entry page and say so.

**Finding 2 — "Target" is defined for links and disclosures only; other controls and the heading population are underdetermined** (note)

Anchor: `proposed/spec.md.patch:6-9` ("links, buttons, `summary` disclosures
and form controls) whose targets or controlled regions differ") and the
Oracle at `:42-45` ("group the interactive elements by computed accessible
name and compare each group's targets"). A link's target is its resolved
`href`, and a `summary`'s controlled region is its `details`. A button or
form control has no stated target unless it carries `aria-controls`, so the
oracle cannot decide whether two same-named buttons "differ". [Observed]
Today's checker already reports any `button` role in the accessibility tree
as a violation (`polaris-accessibility.ts:532`, "a button role reached the
accessibility tree"), so the case may be empty in practice. The specification
should still define it or drop the class. The heading rule does not say
whether headings inside a `details` closed on load, or under `hidden`, count
"in document order". The DOM order and the accessibility-tree order differ
for those.

**Finding 3 — Disambiguated accessible names meet PWB-REQ-012 and the visible label with no stated rule** (note)

Anchor: `proposed/spec.md.patch:10-11` ("A visible label repeated once per
item or source SHALL be told apart in the accessible name by the item or
source it belongs to"). The amendment does not say whether the computed name
must contain the visible label. Speech-input users activate controls by the
visible label, the common label-in-name convention. Nor does it say whether
an accessible name that differs from the visible text is an "owner-visible
Polaris string" under PWB-REQ-012, which carries one `action-label` per
control and a prohibited-term list. PWB-REQ-014 already routes a source
identity "holding a word PWB-REQ-012 bars from a lede" into "the route
string". The same question arises when that identity enters an accessible
name. Worth one sentence before signing.

**Finding 4 — The register rows P-98 and P-99 do not exist at the reviewed commit** (note)

Anchor: `SEMANTIC-DELTA.md:8` ("register row P-99"),
`OWNER-DECISION-PACKET.md:8`, and the sibling
`pwb-opening-index-amendment/IMPACT-LEDGER.md:22` ("P-98 is added by this
change"). [Observed] A fixed-string search for `P-98` and `P-99` over
`.syzygy/governance/decisions/` at `0241fb83` returns nothing. The register's
last rows are P-85, P-86 and P-95, and the commit touches no file under
`decisions/`. Applies to both packages.

**Finding 5 — Pair-checking and "do not overlap" claims overstate what was checked** (note)

Anchor: `IMPACT-LEDGER.md:57-58` ("All four spec patches touch different
requirements and compose in either order; this package's builder checks each
pair") and `OWNER-DECISION-PACKET.md:87-88` ("Their changes do not overlap
and compose in any order"). `composition_findings`
(`scripts/pwb_requirement_amendment.py:383-408`) checks only this package
against each other pending sibling: 3 of the 6 unordered pairs. P-85 and
P-86 overlap outside the spec: their builders say "both add design decision
12 and capability row 34". [Observed] My run of all 24 orders shows that the
spec-composition conclusion itself holds. Applies to both packages.

**Finding 6 — Engine blind spot: a replaced line may silently lose signed text** (note)

Anchor: `scripts/pwb_requirement_amendment.py:283`, which exempts each
`replaced` line by membership and never requires its signed text to survive
as a prefix. [Observed] A probe deleting the signed falsifier words "or
failed cold-open path" from this package's replaced Falsifier line, over the
proposed bytes, produced no finding from `spec_findings`. I checked by hand
that all three replaced lines survive as prefixes in this version, so
criterion 4 holds for these bytes. A later `--write` regeneration would not
be protected. Applies to both packages.

**Finding 7 — If both packages are signed, the opening index's rows may collide with same-named links** (note)

Anchor: `IMPACT-LEDGER.md:50-52` ("the index rows are links and fall under
this package's distinct-name check"). [Inferred] Package A's rows route to
"the first element of its target", which may differ from where an existing
same-named navigation link routes, such as a group heading. Under this
package those two links then need different accessible names. The collision
is disclosed, but neither package says which string changes. Applies to both
packages.
