# Review R1 — PWB tree framing amendment (pwb-tree-framing-amendment)

Reviewed commit: 509201592c13ba903bd3bfc5f91fb2e8aedf2742
Manifest SHA-256: d0d15eba246b64740e52c7c540f05c78013d736fbd43387e7783c73d1af5875f
Verdict: REVISE

Paths below are relative to `.syzygy/governance/contracts/candidates/pwb-tree-framing-amendment/` ("pkg") unless stated. Patch line numbers are lines of `pkg/proposed/spec.md.patch`.

## Mechanics checked (no finding)

- [Observed] `build_pwb_tree_framing_amendment.py --check` passes (11 subjects, 5 patched; 8 performed by record, 1 declined, none unclassified). `--selftest` passes (81 predicates). `--diff` runs.
- [Observed] The manifest file hashes to d0d15eba…; all 11 rows re-derived. The 6 unpatched rows equal current bytes. The 5 patched rows equal the bytes produced by applying the five patches to a scratch copy (spec 5509f236…, design ba2fee66…, proposal d039c6c0…, coverage 2697b6b3…, dependencies 3769ffb2…).
- [Observed] Over that patched scratch copy, `build_polaris_project_wide_spec_dependencies.py --check` and `build_polaris_project_wide_contract_coverage.py --check` both pass (17 requirements; 324 clauses).
- [Observed] Only the PWB-REQ-014 block, design decision 11 and its risk lines, two proposal sub-bullets, coverage row 33 and the generated dependencies move. No byte of another requirement or the reading guide moves. PWB-REQ-014's title is unchanged. Coverage totals 27 + 6 = 33 are correct.
- [Observed] The ten tracked `*/proposed/spec.md.patch` files targeting the PWB spec are this package plus 9 siblings (8 listed performed, each record file present, plus lane B declined). The ledger's counts match. The sibling-patch glob covers every tracked patch naming the PWB spec path.
- [Observed] Citer sweep re-derived with the published predicates over all 1,886 paths at a0d218a: 1,882 decoded, 4 binary, 99 literal + 9 run-only = 108. Breakdown 65 docs, 23 contracts, 8 apps, 6 openspec, 3 decisions, 2 scripts, 1 AGENTS.md. All match.
- [Observed] Page-size arithmetic: 1,650,000 − 1,467,147 = 182,853; 2,097,152 − 1,467,147 = 630,005; 1,650,000 − 1,473,252 = 176,748; 2,097,152 − 1,473,252 = 623,900. The projection (6,227 + 4,031 + about 32 × 600) is about 29.5 KB, so "roughly 30 KB" and "about 150 KB" headroom follow. Labels (Observed table, Inferred projection) are honest.
- [Observed] Rule 6, my own mutants. I applied each mutant to a scratch mirror of the package and ran `--write`, then `--check`.
  - Dropping `animation, ` from the allow-list sentence: the check fails ("expected one … found 0").
  - Renaming the "A failed or unsafe diagram" scenario: the check fails.
  - Replacing "SHALL NOT be drawn from prose, labels or inference": the check fails.
  - The fragment predicates fail closed.
- [Observed] The SVG excluded classes in the patch (script, event-handler attribute, animation, `foreignObject`, link, external or unsafe-scheme reference; allow-list of shapes, paths, text, styling) match the owner's 2026-09-28 ruling in `decisions/POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md` lines 22-29: "under PWB-REQ-006, 'active' governs the whole output list. SVG reduced to an allow-list of shapes, paths, text and styling is inert and may be emitted." PWB-REQ-006's own text ("emit active HTML, SVG, scripts…", spec.md line 637-638) is readable consistently with it, so not amending 006 is defensible. Butlers-source SVG still excludes the whole source (006 line 648). No phrase is offered, no chain position asserted (IMPACT-LEDGER.md line 107), and sign-off authorizes no implementation.

## Findings

**Finding 1 — A partly supported relationship silently drops its unsupported edges** (revise)
`proposed/spec.md.patch` lines 32-40. A relationship is drawable when at least one edge is a model claim. Every drawn element must draw a claim, and an element is drawn Unknown only where a claim establishes it. No clause says what a reader is told about the listed relationship's other edges. Counterexample: a listed relationship has 4 edges and 1 is a model claim. The text draws one edge and omits three. The reader sees a smaller graph and takes the missing edges as absent. That is absence rendered as nothing, contrary to VIS-2 and to the "coarser true account" the delta promises (PWB-REQ-011 line 1146). The all-or-nothing disclosure applies only to the not-drawable case (patch lines 33-35, scenario at line 120). Fix: require each listed-but-undrawn edge or node to be disclosed in the text equivalent or in place with its reason, or state that none is permitted.

**Finding 2 — "Drawable" uses two different predicates, so the Unknown-only case is undetermined** (revise)
Patch line 32 says drawable when an edge "is a claim the shared model holds". The scenario at line 119 and the design flow say "no edge that a model claim *supports*". The resolution diagram says "Does a model claim support at least one edge?". An Unknown-state claim is held by the model but supports nothing. For a relationship whose only edges are Unknown, line 32 makes it drawable (draw an all-Unknown graph). The scenario and flow make it not drawable (disclose a gap). The brief's criterion 5 asks for each result to be stated, and this one is not. The related failure text ("disclosed in place … with its reason", lines 33-35, 52) does not say whether the reason is an RFC2-24 value with a resolution route, as PWB-REQ-007 (spec.md line 756-757) requires of an Unknown reason. Fix: use one predicate (state "holds" or "supports" and define it for Unknown-state claims), state the all-Unknown result, and say what the disclosed reason is.

**Finding 3 — The opening required above Butlers text carries three roles, against PWB-REQ-012's exactly-one-role rule** (revise)
Patch lines 17-18: the opening "names only the leaf's source, its epistemic state and its route". PWB-REQ-012 (spec.md line 1262-1264) requires every owner-visible string to carry exactly one role from `project-fact`, `epistemic-disclosure`, `action-label`, `scope-instruction`. A source is a project fact, a state is an epistemic disclosure, and a route is an action. The delta says "Openings obey PWB-REQ-012" and the ledger says "one role" (IMPACT-LEDGER.md), but the one-sentence opening the patch demands cannot satisfy both. The twenty-word cap and the six prohibited words ("document", "page", "reading", "section", "presentation", "movement") also apply to a sentence that must name a source, which may itself contain them. Fix: split the opening from a separate route/state element, or state which single role the opening takes and where state and route are rendered.

**Finding 4 — "top-level" can restrict the whole group list, contradicting open point 3's drafted arm** (revise)
Patch line 8: "Each top-level project category, catalog, item detail and evidence group SHALL open…". "top-level" reads as modifying every noun, giving the eight top-level groups. The delta (Proposed meaning, "Which groups open") and packet say the drafted arm is every category, catalog, item detail and evidence group (about 32), with "only the eight top-level groups" as the other arm. The patch text can be read as the other arm. "Evidence group" and "item detail group" are also not defined anywhere in the spec (a grep for "evidence group" and "project category" returns nothing), so the brief's criterion 3, enumerating the set on a rendered page, is not met. Fix: drop "top-level" or scope it explicitly, and enumerate the group classes, for example by reference to PWB-REQ-011's levels and PWB-REQ-015's bands.

**Finding 5 — "States only what its children state" is subset-soundness only; omission can make an opening misleading, and the opening has no tuple or role** (revise)
Patch lines 12-15 and 99. The soundness rule forbids a claim found nowhere beneath. It does not forbid omitting an Unknown, contradicted or withheld child. Counterexample: a group has one Observed child and one Unknown child. An opening stating only the Observed child satisfies the clause, but a reader who stops there holds a more favourable account than the group supports. Yet the text and scenario assert that stopping leaves "a coarser true account". Related gaps:
- The opening's own epistemic tuple (PWB-REQ-007 line 752-756, "every project-fact claim… complete tuple") is never specified for mixed-state children.
- Which of PWB-REQ-014's three claim roles (line 1348-1349) an opening takes is never specified. If it is an anchored project fact, the minimal-anchor rule needs an anchor set that covers N children yet stays "small enough to identify which anchor supports which claim".
- The Verification oracle says expected openings come "from the machine model" (patch line 83-ish). A free-prose sentence has no model-derived expected text, so the oracle is untestable or circular.
Fix: require the opening to carry the weakest (or each) child state it summarizes, forbid omitting a non-Observed child, and name the claim role and anchor rule.

**Finding 6 — Placement of the item-detail opening relative to PWB-REQ-015's three bands is unspecified** (note)
PWB-REQ-015 line 1427-1431: an item detail contains, in order, an `argument` band (non-normative; "SHALL NOT create intent, authority, status"), a `contract` band ("only captured governing identities… embeds no body text of its own"), and a `reality` band. The patch makes an item detail a group that must open, but does not say whether the opening sits outside all bands or inside one. Inside the contract band it breaks "only identities". Inside the argument band it may "create status". The delta's "RFC7-17 bands … keep their structure" (patch line 20) is the only guard. The conflict is arguable, hence a note.

**Finding 7 — A counting opening cannot fit the disclosure it must carry** (note)
Patch lines 19-22 require a counting opening to carry PWB-REQ-007's aggregate disclosure: label, tier, freshness and separate primary/secondary reason counts. PWB-REQ-012 caps the lede at twenty words. PWB-REQ-007 line 764-765 also says default presentation renders no "count walls". About 32 openings that each count could be one. The text does not say whether the disclosure lives inside the sentence or beside it, so in practice counting is forbidden everywhere, which is stricter than the stated rule. "Counts Unknown claims" is also undefined for counts of sources or rows that imply Unknown (for example "seven of nine read").

**Finding 8 — The set of diagrams is whatever an unbound review record lists** (note)
Patch lines 26-30: the rendering is owed "where the independent rendered-design review judges" it. The text does not bind which review record (version, digest, evaluation) a conforming page must follow. A relationship the review never lists is neither drawn nor disclosed, and the package states no totality rule. Because the brief puts the contents of that review out of scope, this is a note. The spec text is still hard to test without a named binding.

**Finding 9 — Label text and the PWB-REQ-006 sink scan are not addressed** (note)
PWB-REQ-006's scenario "Markup examples in code remain inert" (spec.md line 719-726) lets code-span content such as an SVG or handler example sit inside an admitted source, to be "encoded as text" at both sinks. Diagram node and edge labels draw such claims (patch line 36-40). The patch says an allow-list validation precedes every sink and a failure emits no SVG. It does not say that labels are text-encoded, so a legitimate label containing markup-like code-span text either blanks the figure or depends on implementation. PWB-REQ-006's oracle is "complete sink-byte scans" for active sentinels (line 703). That oracle will see legitimate `<svg>` bytes once diagrams exist. The delta correctly leaves 006 unamended, but does not disclose that its sink scan must now distinguish emitted diagrams from injected sentinels.

**Finding 10 — Builder classifies a listed performed sibling by record-file existence alone (fail-open)** (note)
`scripts/build_pwb_tree_framing_amendment.py` lines 502-523: `performed_record(name)` is true when the listed name's decision-record file exists, and nothing else is checked. Two mutants I ran in a scratch mirror both left `--check` green (8 performed, none unclassified):
- Appending a new hunk to `pwb-item-depth-amendment/proposed/spec.md.patch` that rewrites PWB-REQ-014 text. That patch would now be pending and conflict with this one, yet it is never composed or classified.
- Truncating the record `PWB-ITEM-DEPTH-AMENDMENT-SIGNOFF-v1.0.md` to zero bytes.
The ledger accurately says the record "counts as history only while that record exists", so this is disclosed. It is still a hole: nothing binds the sibling patch bytes or the record's content (for example, a digest or a "performed" marker). Whether other governance checks freeze those patch bytes was not verified. Fix: pin each performed sibling's patch digest, or require the record to name that digest.

**Finding 11 — Page-size evidence covers the human page only, and the opening count is unsourced** (note)
IMPACT-LEDGER.md "Page size" lines 110-135. PWB-REQ-006 gives each sink its own ceiling (human HTML and machine JSON). The new obligations also add openings, anchors, each diagram's node-and-edge source and the text equivalent to the machine narrative. No machine-JSON measurement or projection is given, although the ledger's own consumers table says the machine narrative carries them. "About 32 openings" and "roughly 600 bytes" are labelled Inferred, but the derivation of 32 is not shown, and the text equivalents are assumed to reuse existing lists. The label honesty is fine. The completeness of the budget claim is not.

## Out-of-scope observations

None.
