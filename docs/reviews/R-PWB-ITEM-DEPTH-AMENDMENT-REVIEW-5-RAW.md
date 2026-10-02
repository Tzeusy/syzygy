# Independent review, round 2 — PWB item depth amendment
Reviewed commit: 5ad3efcb30175f85e44290f198811205935e3d0c
Manifest SHA-256: 4aff2dfa1fc4c8964dafebf9acec8adbd5baa01b4b58c1c7509e4cff995462f6
Verdict: REVISE

## Mechanics checked (all passed)

- Manifest file sha256sum at the reviewed commit equals the head digest.
- Builder `--check` passed ("11 proposed subjects; 0 pending sibling spec patches compose (6 applied, 1 declined, none unclassified)"). `--selftest` ended "52 package predicates fail closed". `--diff` ran. `--apply` without `--at-adoption` was refused and the tree stayed clean.
- I applied all six patches to a scratch copy with `patch`. All six applied. All 11 manifest rows re-hashed with 0 mismatches. `build_polaris_project_wide_contract_coverage.py --check` ("324 clauses represented") and `build_polaris_project_wide_spec_dependencies.py --check` ("17 requirement(s)") both passed on the patched copy.
- I re-derived the ledger counts at 4d51679, which is an ancestor of the reviewed commit. There are 1,816 paths, 1,812 decoded and 4 binary. The literal predicate returns 49 files, which `git grep -F` confirms. The run predicate adds 10, for a union of 59. All of these match IMPACT-LEDGER.md.
- The band/order/class rules, the retained-phrase boundary and the owner gates are present and consistent. I found no fourth band class.

## Findings

**Finding 1 — The absent-relation arm names a primary reason that PWB-REQ-007 forbids until a currency bound is declared** (revise)
Spec.md.patch, the PWB-REQ-015 sweep case and Oracle, says that with no admitted relation source "every item's relation claim is the absent-relation arm" with RFC2-24 `missing-declaration`. The Scenario's third AND bullet says an absent relation renders `missing-declaration`. SEMANTIC-DELTA.md open point 1 and OWNER-DECISION-PACKET.md say "every item shows the absent arm meanwhile".

The same text says the `governing-intent-relation` class has no declared currency bound. PWB-REQ-007's scenario "No effective currency bound is disclosed outside freshness" (spec.md, about lines 740-760) requires that claim to render Unknown with primary reason `no-currency-bound-declared`. PWB-REQ-007 allows exactly one primary reason per claim.

The text applies "exactly one result" only "once the class's currency bound applies". Before that, the claim's primary reason is therefore `no-currency-bound-declared`. This is the only state that can exist until both a source and a bound are admitted. The drafted sweep, the Oracle ("honest relation absence for every unmapped or contradicted item"), the falsifier and the packet's choices table all demand `missing-declaration` at an evaluation where that bound is absent.

Two conforming oracles can therefore disagree on the primary reason of every relation claim today. The text does not say which reason is primary and which is secondary. It also does not say whether `missing-declaration` can be reported at all while the bound is missing.

The diagram in SEMANTIC-DELTA.md and design.md has only three result nodes and no `no-currency-bound-declared` arm. This is a CC-REV-8 fidelity gap against the text.

Required: state the primary reason of each claim before and after the bound applies. State whether the currency reason is primary and the declaration reason secondary. Draw the fourth arm in both diagrams.

**Finding 2 — Applied text makes PWB-REQ-011's "Capability reaches exact requirements" scenario false, and removes today's capability contract band, without disclosure** (revise)
The amended contract band "SHALL contain only captured governing identities", and the text says no relation is captured for any item until a source is admitted. A matching capability's contract band is therefore empty.

Today `apps/three-surface-poc/src/capability-detail.ts` (lines 69-85 and 254-260) renders the capability's baseline-spec requirement sections verbatim. That is the capability's own current-intent leaf, and it is not a relation declaration. Under the amended text that rendering becomes non-conforming ("embeds no body text of its own", and "only captured governing identities").

PWB-REQ-011's unchanged scenario says: WHEN a reader opens a declared capability from the catalog THEN its detail links to the governing requirement identities AND exact requirement text remains reachable. With zero captured relations this cannot hold. Brief criterion 7 asks me to show that PWB-REQ-011 becomes false under the applied text. Here is a counterexample, and the drafted text discloses no such open point.

IMPACT-LEDGER.md says PWB-REQ-011 is "reached, unchanged" and the delta says neither requirement "becomes false". Open point 3 covers only capabilities that match no item or several. It does not cover matching capabilities that lose their verbatim leaf.

The repair-delta rewording of RFC7-13.r1 to "verbatim declared intent or an honest unmapped absence" relaxes RFC7-13.c2 ("every capability narrative reaches a verbatim specification leaf"). The owner packet does not list this as a choice.

Required: either let the contract band include the matching capability's own baseline-spec leaf, or add this regression as a fifth open point and packet row. In both cases correct the PWB-REQ-011 "unchanged / does not become false" claims.

**Finding 3 — Relation-source totality gaps left implicit** (note)
- A declaration that names an item identity absent from the declared `catalog-entry` population has no stated result. It is presumably not a relation of any item, but the text does not say so.
- Duplicate relations to the same artifact, and an exclusion declaration naming a relation that was not itself captured, are not addressed. The set semantics and "exclude one another" imply the intended handling, but they do not state it.
- The gate-failure arm names a related source that may be a doctrine or non-goal file served `whole-body`, while a requirement or scenario is served `requirement-sections`. The arm is total in effect, but the text leaves the per-mode wording implicit.
These are not blocking. A reviewer applying the text literally gets the intended answer in each case.

**Finding 4 — Capability-key matching is unverifiable and may empty all deep dives** (note)
Open point 3 discloses this accurately. I add one observation. Baseline-spec keys are directory names, and catalog-entry keys are literal bold or code spans (for example a capitalized name). Exact, unnormalized equality is therefore plausibly never satisfied for the real Butlers population. In that case the rule would remove every capability deep dive, not only the edge cases. The disclosure covers the mechanism. The owner should read it as potentially total, not marginal.

**Finding 5 — Ledger and mechanics note** (note)
The ledger's helper script is not tracked, so the predicates are the whole method. I re-ran the stated predicates and obtained the stated counts, so the figures reproduce. The statement "0 pending siblings" depends on the 6/1/0 classification, which `--check` re-proves each run.
