# Independent review: bounded Trajectory selection
Reviewed commit: bbecf52136f79ebaa77377968e53adba8d5ef037
Subject manifest SHA-256: 5088b21a083eb3d428fb58518c5e94af0c0f814000db28b8691cefa478d8041b
Verdict: REVISE

[Observed] This review concerns the six changed files against base `3d03f693a52328cf03804f4f5ecb15236617ce15`. The source manifest below hashes each file obtained with `git show` at the reviewed commit. Its digest is SHA-256 over the exact `source-subjects.sha256` bytes, in the displayed order, with two spaces between digest and path and a terminating newline per row. The implementation owner's moving worktree was not modified.

## Blocking finding

1. **P2 — Define deterministic timestamp validity before ranking.** `packages/three-surface-poc-core/src/trajectory-projection.ts:56-61` passes strings directly to `Date.parse` and treats only `NaN` as invalid. The observation boundary (`packages/three-surface-poc-core/src/work-items.ts:154-181`, unchanged governing context) validates timestamp fields as strings and therefore supplies no timezone or calendar-validity guarantee. The helper introduces two reproducible violations of its stated rule:

   - [Observed] For one fixed synthetic observation, an open item's `updatedAt` of `2026-08-03T00:00:00` competes with another item's `2026-08-02T20:00:00Z`. With a non-closed limit of one, the timezone-less item is selected under `TZ=UTC` and `TZ=America/New_York`; the explicitly zoned item is selected under `TZ=Asia/Singapore`. The selected population depends on process configuration rather than only the recorded observation.
   - [Observed] `2026-02-30T23:00:00Z` is normalized by the parser and ranks ahead of the valid `2026-03-01T00:00:00Z`. This occurs for both `updatedAt` in the non-closed population and `closedAt` in the closed population, so the visible promise “missing or invalid times last” is false for impossible calendar dates.

   [Inferred] The first counterexample violates POC-REQ-041's “derive from instants recorded in the observed work-item facts ... never ... inferred ordering” and VIS-1's truth and observation-determinism priority. The second contradicts the new selection rule declared under POC-REQ-042. Both violate the canonical engineering bar's behavior-verification and regression-protection criteria. Fix the shared ranking helper with an explicit, deterministic supported timestamp grammar and calendar validation. Treat unsupported or ambiguous timestamps as invalid unless a source contract explicitly supplies their interpretation. Add literal regression cases for timezone-less input and impossible dates, covering both populations, while preserving valid timezone-offset ordering. The independent probe source and failing log are retained beside this raw.

## Non-blocking notes and unfinished evidence

- **P3 — Strengthen the input-immutability regression.** The added check at `packages/three-surface-poc-core/src/trajectory-projection.test.ts:41-42` uses an already ID-sorted input, so an accidental in-place ID sort would still pass. [Observed] The current implementation copies the array, and an independent probe passes with deeply frozen, unsorted observations across 64 deterministic permutations. An unsorted or frozen fixture would make the checked-in assertion protect that behavior. This is a regression-quality note, not a current mutation defect.
- [Observed] `docs/evidence/syzygy-blbu-trajectory-selection-2026-10-20.json:3` explicitly marks mutation, committed after-size and clean-clone gates pending. Its four declared implementation digests match the frozen source bytes. The candidate size comparison and rationale are present, but this prepared record does not establish final after-size or clean-clone success. CC-PERF-3 says: “Perf work without before/after evidence is unverified work.” A final review must inspect the completed receipts and exact final head; this raw provides no finished performance verdict.
- [Observed] The documentation correctly limits the fixed-count claim to card growth and states that selected text can still grow and response ceilings continue to apply. Retain that qualification.

## Verification and acceptance coverage

- [Observed] Installed dependencies with `npm ci --no-audit --no-fund` inside a detached disposable clone at the reviewed commit. Output is in `npm-ci.log`.
- [Observed] Ran `npx vitest run packages/three-surface-poc-core/src/trajectory-projection.test.ts apps/three-surface-poc/src/trajectory.test.ts --reporter=verbose`: **23 passed / 23**, in two files. The complete output is in `targeted-tests.log`.
- [Observed] Ran independent synthetic probes from `trajectory-review.test.ts`: **2 passed, 3 failed / 5**. The passing probes cover literal selection membership over 64 permutations of a deeply frozen ten-item observation spanning the seven declared statuses, reconciliation at 5 rendered + 5 excluded = 10, and distinct empty versus Unknown results. The three failures are the timezone and two calendar counterexamples above. Complete output is in `independent-probes.log`. These are direct calls to the public projection, without mocking its internal helpers.
- [Observed] The checked-in tests exercise production limits through `buildPocModel` and the actual `/api/poc` route: 252 machine work items, 250 human cards, 2 exclusions, and 50 Done cards. They also preserve the demonstrated-item outside-selection callout for both open and closed items. Offset ordering and ID-tie behavior have literal expected memberships; the new tests replace the previous self-check-only falsified-count assertions. The recorded test delta is +5, modified 3, removed 2, net +3.
- [Observed] Source inspection shows fixed model limits of 200 non-closed and 50 closed; status-to-column mapping and card rendering remain unchanged; the full `workItems` observation is retained, while `trajectory.rendered` is the selected projection. The selection declaration and rendered/excluded/total counts remain visible. Frozen source order and copied arrays avoid input mutation on the exercised unique-ID observations.
- [Observed] Enumerated the six changed paths with both `git diff --name-only` and `git diff --raw` at the frozen commit. Their path sets match. The diff changes no adopted specification, read/egress path, response ceiling, registry, or P-100 governing-intent implementation. P-100's deliberate base revert remains outside this review.
- [Unknown] Full mutation gates, final committed live size receipts, and clean-clone full gates were being performed by the implementation owner and were not completed evidence in this frozen subject. They were intentionally not duplicated in this independent targeted review. No Butlers repository bodies or live response bodies were read for this review; only synthetic fixtures were exercised.

## Governing references read at the frozen commit

- `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`: POC-REQ-040, POC-REQ-041, POC-REQ-042 and adjacent POC-REQ-043. POC-REQ-042 requires the selection rule and counts inside and outside the selection; POC-REQ-040 requires declared status-column placement.
- `.syzygy/governance/decisions/THREE-SURFACE-POC-MODE-DIRECTION.md` and `THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md`: bounded non-release experiment, one shared fact model, WIP one, review-derived repair and exact-commit confirmation.
- `.syzygy/governance/doctrine/vision.md`: VIS-1, VIS-2 and Performance. Its scope-narrowing rule says: “Performance may narrow an explicitly declared scope; it may never present incomplete coverage as complete within that scope.”
- `.syzygy/governance/policies/craft-and-care/engineering-bar.md`: CC-BAR-1/2/5/6, with the canonical engineering-bar skill adopted by reference; `.syzygy/governance/policies/craft-and-care/performance-and-visual-discipline.md`: CC-PERF-1/3. The test-rigor skill was used to challenge behavior, boundary cases and independent expected values.
- Actual repository `AGENTS.md` was read as operating procedure, not cited as project authority.

## Exact source subjects

| Path | SHA-256 |
|---|---|
| `apps/three-surface-poc/src/trajectory.test.ts` | `032c46a9987c845de085e36f161d0a6e104870149435a63d88e6c19f6dcd486f` |
| `docs/THREE-SURFACE-POC.md` | `3ccbad862ed2d73fc6568d74e86696f6a0e2b06ae3df1041155df7239d44da9c` |
| `docs/evidence/syzygy-blbu-trajectory-selection-2026-10-20.json` | `e87b89577105189601f1baa1ef6fe1e819cf0eb3972a1f94b8b1c852ffa99090` |
| `packages/three-surface-poc-core/src/model.ts` | `c31c6937ec4592fca828fe511ac87e896ca2bd047a3d9b08ccbc185340eb0460` |
| `packages/three-surface-poc-core/src/trajectory-projection.test.ts` | `be3d30f84d24b3011d688904c9c007312029b0ecfbba73fe592682e6e70ab102` |
| `packages/three-surface-poc-core/src/trajectory-projection.ts` | `6e403030b266f2e49cfd53514324ab2547dc0110bd4b54334e39289b314bcfb8` |

[Inferred] Final disposition: **REVISE** for the P2 timestamp-ranking defect. The bounded selection structure, full machine population, reconciliation and demonstrated-item disclosures pass the scoped checks above. Repair and freeze a new head, then obtain a fresh review; this raw remains unchanged.
