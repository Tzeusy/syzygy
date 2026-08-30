# Independent confirmation report

## Exact subject and checks

[Observed] Review subject: exact commit `8069742258e4affcb813cfa69c545c8453c167cb` (`spec: repair project-wide Polaris review findings [syzygy-1z3]`).

[Observed] The reviewed change, generator, and review files have no working-tree differences from that commit. The unrelated `.gitignore` modification was excluded.

[Observed] The frozen raw review digest is `b47fbb0eb73507d0f6a4d4cc50f72908c6330c8a82be689477ce1f59209587dc`, matching `docs/reviews/R-POLARIS-PROJECT-WIDE-SPEC-REVIEW-DISPOSITION.md:3-7`.

[Observed] All requested commands passed:

- dependency generator `--selftest` and `--check`;
- contract-coverage generator `--selftest` and `--check`;
- `openspec validate polaris-project-wide-butlers-model --strict`.

[Observed] Independent structural analysis found:

- 324/324 accepted clause identities represented;
- 66 repair rows superseding 62 base rows;
- four intentional one-to-many splits;
- 140 mechanically covered rows;
- zero covered-row/current-warrant identifier mismatches;
- but 616 actual effective consequence rows, not the generated manifest’s claimed 615.

[Observed] All six signed parent artifacts match the digests at `.syzygy/governance/decisions/THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md:36-49`; `git diff db5eaee..8069742` reports no signed-parent change.

[Observed] Semantic sampling covered every RFC family. RFC8 and RFC9’s believed-not-applicable posture agrees with the Polaris-only scope. RFC1, RFC2, RFC6, and RFC7 contain material repair-overlay overclaims detailed below.

## Per-finding verdicts

### 1. Consequence-granular contract review — NOT CONFIRMED

[Observed] The replacement matrix is genuinely consequence-granular and retains authority spans, applicability reasoning, and dispositions. However, it is not exhaustive as processed:

- `contract-coverage-matrix/RFC-0001-0003.md:9-12` declares 209 base consequences.
- `CONTRACT-COVERAGE.md:21` reports only 208 for that part.
- `RFC-0001-0003.md:177` uses applicability `yes/no`.
- `scripts/build_polaris_project_wide_contract_coverage.py:33-37` accepts only `yes`, `no`, or `unknown`, and `:65-83` silently consumes only matching rows.
- Consequently RFC3-7.c2 is absent from the generated effective population.

[Observed] Some repaired splits also under-enumerate their governing clause. RFC7-16’s accepted text prohibits metric walls, trends, and counts at default density (`RFC-0007/narrative-contract.md:316-340`), while the replacement rows at `CONTRACT-COVERAGE-REPAIR-DELTA.md:35-37` cover composite status and leave minimal density/drawer handoff Unknown but omit the metric-wall/trend/count consequence.

[Inferred] A green generator still does not establish consequence completeness. The original blocker remains.

### 2. Warrant overclaims — NOT CONFIRMED

[Observed] Identifier-level agreement is clean: every effective `covered:` row cites a current requirement whose `contracts[]` contains that clause.

[Observed] Semantic agreement is not clean. Examples from the exhaustively reviewed repair delta:

- `CONTRACT-COVERAGE-REPAIR-DELTA.md:19` marks durable Claim identity covered by PWB-REQ-007, but `spec.md:237-253` requires the evaluation identity and epistemic tuple, not durable semantic identity.
- `CONTRACT-COVERAGE-REPAIR-DELTA.md:20` replaces RFC1-18.c2 while dropping its challenge-state consequence, which remains binding at `RFC-0001-project-graph-identity-state-planes.md:326-336`.
- `CONTRACT-COVERAGE-REPAIR-DELTA.md:32` claims aggregate label/tier/reason/freshness counts are covered. PWB-REQ-007 requires only primary/secondary reason counts for aggregates at `spec.md:241-251`; RFC6-17 requires the full composition at `RFC-0006-cross-surface-selection-query-drawer.md:274-299`.
- `CONTRACT-COVERAGE-REPAIR-DELTA.md:52` marks anchor target-state carriage and no-rewrite behavior covered by PWB-REQ-014. That requirement at `spec.md:468-490` contains neither the captured label/tier/reason target state nor a later-read immutability oracle required by `RFC-0007/narrative-contract.md:204-223`.
- `CONTRACT-COVERAGE-REPAIR-DELTA.md:54,56-57` overclaims verbatim doctrine/non-goal coverage; PWB-REQ-015 at `spec.md:514-529` byte-checks current requirements/scenarios, not doctrine and non-goal text.
- `CONTRACT-COVERAGE-REPAIR-DELTA.md:66,69` claims personal-state separation and a machine type distinct from kernel Claim, neither of which is required by PWB-REQ-014/015.

[Inferred] Several high-risk RFC7 authority and machine-envelope consequences remain mechanically labeled covered without an effective oracle. The original blocker remains.

### 3. Capability denominator includes refusals — PARTIAL

[Observed] The table now includes positive obligations and explicit refusals, including arbitrary body reads, inference, external writes, second-project support, release, autonomy, multi-user behavior, and weakened truth/security floors at `CAPABILITY-COVERAGE.md:8-34`.

[Observed] Its totals are false. The 27 rows contain 21 `covered`, 6 `lawfully out of scope`, and 0 Unknown dispositions, while `CAPABILITY-COVERAGE.md:36` reports 20 covered and 7 out of scope.

[Inferred] The original omission of refusals is repaired, but the claimed partition has not been accurately demonstrated. Confirmation is therefore partial.

### 4. Observation consent and concrete secret policy — CONFIRMED

[Observed] PWB-REQ-005 now requires consent, concrete secret policy, and registered observer provenance before any body read, with zero reads and project-model Unknown on invalid authority at `spec.md:152-190`.

[Observed] The security acts remain separate owner gates rather than being minted by spec sign-off: `design.md:107-114`, `tasks.md:9-14`, and `proposal.md:78-85`.

[Observed] PWB-REQ-003 extends secret exclusion checks across model, cache, log, HTML, JSON, and record sinks at `spec.md:110-150`.

[Inferred] The original consent/policy blocker is fixed. A separate internal triple-versus-pair defect is recorded under new findings.

### 5. Closed item identity and discovery — PARTIAL

[Observed] The source-path population is now finite, revision-bound, and nonrecursive, and source-path versus within-source item denominators are separated at `design.md:36-55,66-80` and `spec.md:8-20`.

[Observed] Stable item identity is defined as source class, path, and declared key.

[Unknown] The within-source extraction procedure is still not closed enough for two independent implementations to derive the same D. “Indexed heading” is not accompanied by a finite heading/type grammar, and the requirements do not define which syntax mints staffer, domain-butler, module, connector, or major-interface items. PWB-REQ-002 refers circularly to “the closed extraction rule” at `spec.md:71-87`.

[Inferred] Source discovery and denominator failure behavior are repaired; item discovery remains under-specified.

### 6. Path, active-content, and resource controls — CONFIRMED

[Observed] PWB-REQ-006 requires exact Git-object reads, normalized repository-relative containment, rejection of absolute/traversal/NUL/symlink/submodule paths, no observed-content execution, inert output, explicit limits as evaluation inputs, and Unknown-on-limit behavior at `spec.md:192-230`.

[Observed] Design-level sink coverage and context-aware encoding are stated at `design.md:116-127,150-155`.

[Inferred] These controls satisfy the original path, browser-active-content, and resource-exhaustion repair request for a bounded local POC.

### 7. Plain-copy oracle — CONFIRMED

[Observed] PWB-REQ-012 has a closed four-role vocabulary, finite word limits, a finite prohibited-term set, instruction cardinalities, an exhausted string population, and an independent DOM/text oracle at `spec.md:384-426`.

[Observed] Human comprehension remains independently owner-judged under PWB-REQ-021 rather than being conflated with the mechanical copy sweep.

[Inferred] The original subjective escape hatch is removed.

### 8. Complete RFC7-30 prompt — CONFIRMED

[Observed] PWB-REQ-021 explicitly retains the complete RFC7-30 prompt set and includes the fact-strength/strengthening prompt at `spec.md:624-665`, matching `RFC-0007/rendering-and-surface.md:133-152`.

[Observed] PWB-REQ-007 supplies the complete epistemic tuple at `spec.md:233-273`, and PWB-REQ-016 adds nonvisual/keyboard execution at `spec.md:551-587`.

[Inferred] The original omitted prompt is fixed. A separate record/judgment artifact conflict is listed below.

### 9. Proposal authority language — CONFIRMED

[Observed] The proposal now states that sign-off is necessary but not sufficient; work also requires finding-derived improvement-cycle authority and satisfied security prerequisites at `proposal.md:78-85`.

[Observed] This agrees with the authoring-only direction at `.syzygy/governance/decisions/POLARIS-PROJECT-WIDE-POC-EVALUATION-DIRECTION.md:31-38` and the non-widening rule at `OPENSPEC-MULTI-CHANGE-DIRECTION.md:25-36`.

## New findings

### N1. BLOCKER — The generator silently drops syntactically invalid consequence rows

[Observed] RFC3-7.c2 is a table row at `contract-coverage-matrix/RFC-0001-0003.md:177`, but its `yes/no` applicability cannot match `BASE_ROW_RE` at `scripts/build_polaris_project_wide_contract_coverage.py:33-37`. The parser has no rejected-row or table-row denominator check at `:65-83`.

[Observed] The true population is 612 base rows and 616 effective rows; the generated manifest reports 611 and 615.

[Inferred] This defeats exact denominator and mutation confidence while `--selftest`, `--check`, and 324-clause representation all remain green.

Minimum precise fix: split RFC3-7.c2 into separate observation and egress consequences with one closed applicability each; make the generator reject every consequence-looking table row that fails the grammar; add a self-test proving `yes/no` or any malformed row fails; regenerate totals and digests.

### N2. DEFECT — PWB-REQ-005 alternates between a triple and a pair

[Observed] The SHALL statement and case require three authorities—consent, policy, registry—at `spec.md:156-165`. The observable says “invalid pairs” and “valid pair,” and the oracle verifies “the two owner-act provenances” at `:166-169`.

[Inferred] An implementer cannot tell whether registry provenance is part of the exhaustive decision oracle even though RFC4-7 requires it.

Minimum precise fix: use “triple,” “three owner-act provenances,” and all-three-valid terminology consistently in the case, observable, oracle, and falsifier.

### N3. DEFECT — PWB-REQ-021 places owner judgment inside the walkthrough record

[Observed] PWB-REQ-021 says one retained walkthrough record contains the owner judgment at `spec.md:637-645`. PWB-REQ-022 separately and correctly requires an execution record in `records/` and a judgment in `decisions/` at `:671-686`. RFC7-31 requires two artifacts and two homes at `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md:171-190`.

[Inferred] The two requirements permit incompatible record schemas and blur evidence versus decision authority.

Minimum precise fix: make PWB-REQ-021’s execution record contain only answers, paths, evaluation/surface identity, and mode; require a separate owner-judgment decision referencing that execution record.

## Security verdict

**SECURITY VERDICT: REVISE**

[Observed] PWB-REQ-005/006 materially improve consent, secret-policy, observer-registration, path-containment, inert-content, sink-screening, and resource-limit controls.

[Observed] The effective contract manifest silently omits the RFC3-7 exact consent-subject consequence, PWB-REQ-005’s authority oracle is internally inconsistent, and PWB-REQ-021 conflates an execution fact with owner judgment.

[Inferred] These are authority-boundary defects, not editorial issues. The candidate is not yet acceptable as the security contract for implementation.

## Overall verdict

**REVISE**

[Inferred] Findings 4, 6, 7, 8, and 9 are repaired; finding 5 is partial; findings 1 and 2 remain materially unresolved; finding 3’s refusal population exists but its partition totals are false. The false generated denominator and semantic covered-row overclaims prevent exact confirmation.
