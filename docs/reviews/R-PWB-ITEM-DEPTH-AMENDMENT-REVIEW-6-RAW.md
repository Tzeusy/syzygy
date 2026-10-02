# Independent review round 3 — PWB item depth amendment

Reviewed commit: 13778bd8d2cbb1841a6db66fd3ca16fe692b0702
Manifest SHA-256: 6ea880ab78b7a93666784e582bcd585caa12ca9d5bdb2ebf23510406e7a6f85b
Verdict: CONFIRM WITH EXCEPTIONS

## Method

[Observed] Read via a detached worktree at the commit above; nothing in the repository was edited. Manifest-file sha256sum computed at that commit equals the value in the head.

[Observed] Mechanics. `build_pwb_item_depth_amendment.py --check` reports "matches 11 proposed subjects; 0 pending sibling spec patches compose (6 applied, 1 declined, none unclassified)"; `--selftest` ran every case to "caught" (63 package predicates fail closed); `--diff` prints the six subject diffs. I applied all six patches with `git apply` in a scratch copy of `openspec/` taken from the commit: each applied cleanly, and all eleven manifest rows re-derived by sha256sum matched (OK x11). Over the patched copy, `build_polaris_project_wide_contract_coverage.py --check` ("matches regeneration — 324 clauses represented") and `build_polaris_project_wide_spec_dependencies.py --check` ("17 requirement(s)") pass. The worktree stayed clean, so no signed byte was touched. The `--apply` refusal and failed-check no-write cases are covered by the selftest lines "apply without --at-adoption refuses and writes no signed subject" and "apply at adoption with a corrupt/stale ... writes no signed subject"; I did not run a separate scratch mirror.

[Observed] Ledger counts re-derived with the published predicates at 4d51679: 1,816 paths, 4 binary; literal `PWB-REQ-015\b` 49 files; run predicate adds 10 with no literal; union 59. All match IMPACT-LEDGER.md. (My first run of the run predicate gave 9 because my own range expansion was wrong; corrected, it gives 10.)

[Inferred] Substance read against PWB-REQ-007 (spec.md:630-824), PWB-REQ-011 (986-1095), PWB-REQ-013 (1141-1175), PWB-REQ-020 (1320+) and the full proposed PWB-REQ-015 in `proposed/spec.md.patch` and SEMANTIC-DELTA.md.

## Criteria summary

1. Scope: the delta widens the subject from capability detail to the declared catalog-entry population only; no capability or item is invented, and non-matching capabilities get no detail. Holds.
2. Bands: argument, contract, reality, same order, no fourth class. Holds.
3. Relation: single primary reason before the bound (`no-currency-bound-declared`, consistent with the PWB-REQ-007 scenario at spec.md:738-764) and one result per population after it (none, compatible set, any exclusive pair). Exclusion is defined only by an admitted declaration, never prose, class, label or precedence. A source is stated as not yet admitted. Total and deterministic. Holds.
4. Exact intent: text only through PWB-REQ-011's exact-source route; excluded, missing, unreadable and gate-failed sources have a stated result. Holds.
5. Identity/parity: item and relation tuples are separate and recoverable in both channels; URL, label, path and coordinate are excluded from identity. Holds.
6. Proposals: capability-only, matching exactly one item. Holds, subject to Finding 1.
7. Neighbouring authority: no new contradiction beyond the four disclosed open points, except the notes below.
8. Mechanics: verified above.
9. Owner boundary: package says it binds nothing, asserts no chain position, and sign-off authorizes no implementation. Holds.
10. Comprehension: the relation diagram matches the text (no-bound, none, compatible set, exclusive pair, capability-only proposal) and adds no state or route.

## Findings

**Finding 1 — PWB-REQ-013's scenario also reads false for an unmatched capability** (note)
`proposed/spec.md.patch` makes a capability matching no item or several render "no proposal material anywhere". PWB-REQ-013's scenario "Proposal is shown only in affected capability detail" (spec.md:1166-1169) says WHEN a capability has an active OpenSpec change THEN its detail presents the proposal beside current intent; for such a capability there is no detail, so the scenario reads false. SEMANTIC-DELTA.md "What explicitly does NOT change" (line ~330) says PWB-REQ-013 "still confines proposal material to matching capability detail", and open point 3 (lines ~418-432) names only PWB-REQ-011's scenario as made false. The fact is disclosed in substance ("gets no detail and renders no proposal"), so the omission is of one named consequence, not of the behavior. Suggest adding PWB-REQ-013's scenario to open point 3's list of consequences.

**Finding 2 — The Unknown disclosure for an unmatched capability has no stated claim subject** (note)
The amended text says an unmatched capability "receives no item detail and no identity from this requirement" yet "is disclosed as Unknown with the RFC2-24 reason". PWB-REQ-007 requires every claim to carry a stable semantic Claim identity. The disclosure presumably attaches to the capability's existing identity from another requirement, but the text does not say which, so an implementation could mint a claim here. Low risk because the text forbids minting an identity from this requirement; flagged for the implementation-authorization stage.

**Finding 3 — A contradicted population is not surfaced before a currency bound exists** (note)
While the class has no effective bound, every relation claim carries only `no-currency-bound-declared`, "whatever its population" (including a mutually exclusive pair). That follows the PWB-REQ-007 rule of one primary reason and is internally consistent; the text does not say whether the contradiction may appear as a closed secondary reason. Since no relation is capturable today the exclusive-pair arm is unreachable; the owner may wish to rule on the secondary reason when a source is admitted. This is disclosed in kind by open point 1 (inert until a source is admitted).

**Finding 4 — The Observed and contradicted arms are untestable against production until a source is admitted** (note)
Because no extraction class admits a relation declaration, the Observed and `contradicted-pending-adjudication` arms can be exercised only by the hard-coded oracle populations the Case (sweep) specifies. The package states this in open point 1 and in the Case; I record it so the sign-off reader knows the conformance evidence for those arms will be fixture-only.

## Disposition

No blocking or revise defect. All findings are notes; the bytes at the reviewed commit are cleared if the owner accepts the notes.
