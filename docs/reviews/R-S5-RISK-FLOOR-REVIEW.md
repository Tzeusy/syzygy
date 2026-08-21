# R-S5 Risk-Floor Review — Parity Engine, Epistemic State, Authority, Drawer

**Slice:** S5 (syzygy-6v7)
**Risk class:** Parity engine (CAP1-REQ-041/043)
**Reviewer:** R-S5-review-2 (independent fresh-context agent)
**Date:** 2026-08-22

## Verdict: CONFIRM WITH EXCEPTIONS

### Files reviewed (11)

1. `packages/cap1-core/src/parity.ts` (344 lines)
2. `packages/cap1-core/src/epistemic.ts` (139 lines)
3. `packages/cap1-core/src/authority.ts` (149 lines)
4. `packages/cap1-core/src/drawer.ts` (350 lines)
5. `packages/cap1-core/src/index.ts` (17 lines)
6. `packages/cap1-conformance/src/req-040.conformance.test.ts` (276 lines)
7. `packages/cap1-conformance/src/req-041.conformance.test.ts` (353 lines)
8. `packages/cap1-conformance/src/req-043.conformance.test.ts` (195 lines)
9. `packages/cap1-conformance/src/req-044.conformance.test.ts` (140 lines)
10. `packages/cap1-conformance/src/req-045.conformance.test.ts` (165 lines)
11. `packages/cap1-conformance/src/req-046.conformance.test.ts` (151 lines)

### Confirmed properties (verbatim from reviewer)

- serveMachine: facts by reference, no copy step (RFC6-13)
- renderHuman: every fact placed exactly once via placedIndices; no subtraction path (RFC6-21, CAP1-REQ-041)
- fullDisclosure extracts from OUTPUT ITSELF, never shared model — oracle independence (CAP1-REQ-041)
- ParityDisagreement has no winner/preferred-channel field (CAP1-REQ-043)
- ParityComparison closed union; non-empty tuple prevents zero-disagreement defect arm
- compareRenderings: envelope equality before fact comparison; declared-filter difference correctly non-comparable (RFC6-23)
- Count facet catches total-count mismatches (lines 324-331)
- reasonFacet distinguishes deferred-posture Unknown from standard Unknown (SDR-36 rule 3)
- EpistemicState: three-arm discriminated union, no unlabeled arm
- ServedFact requires epistemic — no unlabeled-fact arm at type level (RFC6-14)
- citeBasis fail-closed: generated-presentation refused (CAP1-REQ-045)
- deriveEffectiveStatus: no record → 'unadopted' (fail-closed floor)
- AuthorityExposure: stamp and effective as two separate named fields
- ExplanationFactSet mirrors RFC6-19's twelve classes
- Unavailable arm structurally incapable of summary
- AggregateRendering: no aggregate-level epistemic field (RFC6-14)
- All six conformance test files: hard-coded expected values, disclosed denominators, oracle independence

### Exception (WARNING — not blocking)

**compareRenderings oracle Map-collapse on duplicate-named facts**

File: `packages/cap1-core/src/parity.ts`, lines 290-291

The oracle's `firstByName`/`secondByName` Maps collapse duplicate-named
facts to their last entry. If two channels served duplicate-named facts
with the same total count but different per-fact content at matching
positions, the per-facet comparison would miss the disagreement.

Unreachable by construction: both channels serve from the same FactModel
by reference — serveMachine returns model.facts, renderHuman assigns
model.facts objects into sections. No channel modifies facts.

**Disposition:** Routed to follow-up bead syzygy-ydr for oracle hardening
(multiset or positional comparison in compareRenderings).

### Pre-commit repair applied (by orchestrator, not reviewer)

Before the review, the orchestrator identified and fixed a real defect in
renderHuman: the original name-keyed Map (`new Map(model.facts.map(f =>
[f.name, f]))`) silently dropped the first of any duplicate-named facts.
Fixed by switching to index-based tracking (`placedIndices: Set<number>`).
Rule-6 mutation check confirmed: re-introducing the defect fails the two
new falsifier tests (duplicate-named facts without and with presentation).

## Evidence

- 214 tests passing (33 files), including 2 new duplicate-name falsifiers
- Typecheck clean (cap1-core, cap1-conformance)
- Rule-6 mutation check: defect re-introduced → falsifiers fail; fix restored → green
