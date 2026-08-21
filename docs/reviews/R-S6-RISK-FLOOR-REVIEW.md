# R-S6 Risk-Floor Review — Human Entry + Repository Discoverability

**Slice:** S6 (syzygy-1vd)
**Risk class:** Write boundary (CAP1-REQ-023, CAP1-REQ-053)
**Reviewer:** R-S6-review (independent fresh-context agent)
**Date:** 2026-08-22

## Verdict: CONFIRM WITH EXCEPTIONS

### Files reviewed (14)

1. `packages/cap1-core/src/entry.ts` (125 lines)
2. `packages/cap1-core/src/discoverability.ts` (122 lines)
3. `packages/cap1-core/src/index.ts` (re-exports)
4. `packages/cap1-core/src/vocabulary.ts` (lines 43-51, DISCOVERABILITY_VALUES)
5. `packages/cap1-conformance/src/req-020.conformance.test.ts`
6. `packages/cap1-conformance/src/req-021.conformance.test.ts`
7. `packages/cap1-conformance/src/req-022.conformance.test.ts`
8. `packages/cap1-conformance/src/req-023.conformance.test.ts`
9. `packages/cap1-conformance/src/req-050.conformance.test.ts`
10. `packages/cap1-conformance/src/req-051.conformance.test.ts`
11. `packages/cap1-conformance/src/req-052.conformance.test.ts`
12. `packages/cap1-conformance/src/req-053.conformance.test.ts`
13. `packages/cap1-core/src/proposal.ts` (dependency)
14. `packages/cap1-core/src/epistemic.ts` (dependency)

### Confirmed properties (verbatim from reviewer)

**entry.ts:**
- CAP1-REQ-020: one fixed path, isIdentity: false
- CAP1-REQ-021: nonCitable: true and artifactClass 'presentation-artifact' on every rendering, enforced at type level
- CAP1-REQ-022: exhaustive five-arm discriminated union; absent is a finding not Unknown; unreadable carries reason; stale/contradictory disclose disagreement with authorityWins: true
- CAP1-REQ-023: GOVERNED_WRITE_NAMESPACES correct; module exports no write operations; all functions return pure data; isInsideGovernedPlane correctly classifies via startsWith

**discoverability.ts:**
- CAP1-REQ-050: four-value vocabulary; one finding per repository
- CAP1-REQ-051: yes/no only from captured evidence; missing evidence yields Unknown with verbatim reason
- CAP1-REQ-052: observed-source short-circuits to not-applicable before evidence; governance-root can never reach not-applicable
- CAP1-REQ-053: proposeEntryLink returns Proposal with plane 'proposed'; computeDiscoverabilityWithProposal delegates to renderState; finding returned by reference unchanged

No fail-open paths, no write-boundary violations, no subtraction bugs, no unclosed unions in production code.

### Exception (WARNING — test only, repaired)

**REQ-051 test conditional guard on reason assertions**

File: `packages/cap1-conformance/src/req-051.conformance.test.ts`

The `if (finding.epistemic.label === 'Unknown' && 'reasons' in finding.epistemic)` guards could pass vacuously if the implementation returned the deferred Unknown variant (no reasons). A future regression could silently skip the reason check.

**Repair:** Added unconditional `expect('reasons' in finding.epistemic).toBe(true)` assertions before each narrowed inner check, ensuring the test fails if reasons are absent.

## Evidence

- 254 tests passing (41 files)
- Typecheck clean (cap1-core)
- REQ-051 test fix verified green
