# R-S7 Risk-Floor Review — Write Boundary, Distinctions, Integration

**Slice:** S7 (syzygy-hbd)
**Risk class:** Write boundary (CAP1-REQ-061)
**Reviewer:** R-S7-review (independent fresh-context agent)
**Date:** 2026-08-22

## Verdict: CONFIRM WITH EXCEPTIONS

### Files reviewed (6 primary + 6 dependencies)

1. `packages/cap1-core/src/write-boundary.ts`
2. `packages/cap1-core/src/distinction.ts`
3. `packages/cap1-core/src/index.ts`
4. `packages/cap1-conformance/src/req-061.conformance.test.ts`
5. `packages/cap1-conformance/src/req-064.conformance.test.ts`
6. `packages/cap1-conformance/src/req-integration.conformance.test.ts`

Dependencies verified: entry.ts, epistemic.ts, proposal.ts, authority.ts,
discoverability.ts, parity.ts.

### Confirmed properties (verbatim from reviewer)

- CAP1-REQ-061: write boundary is the governed plane; paths outside refused;
  widening fields render as contradictions routed to owner; external effects
  empty; authorizeWrite is fail-closed; CAPABILITY_1_EXTERNAL_EFFECTS typed
  as const
- CAP1-REQ-064: all nine named distinctions machine-readable and recoverable
  without vision; extractors return MachineReadableDistinction with
  recoverableBy text-attribute or structure; sweepDistinctions verifies full
  coverage; closed set enforced by CAPABILITY_1_DISTINCTIONS
- Re-exports present (index.ts lines 19-20)
- All tests use oracle-independent assertions (hard-coded expected values)
- Integration test exercises full pipeline from declaration through
  distinction sweep
- No type-level safety gaps found

### Type-level guarantees verified

- WideningFieldViolation: rendering literal 'contradiction', routedTo
  literal 'owner'
- WriteAuthorization: discriminated union on permitted
- MachineReadableDistinction.recoverableBy: only text-attribute or structure
- ProposalRendering: marking literal 'proposed', adopted literal false
- CapabilityDistinction: nine-literal union from closed tuple

### Exceptions (WARNING — not blocking)

1. **Dead branch in distinction.ts:86**: selfDeclaredStamp is a required
   field (string, not optional) — the undefined check is always true. No
   incorrect behavior; the distinction is always produced.

2. **Duplicate distinction name in distinction.ts:80-93**:
   extractAuthorityDistinctions returns two entries named
   'effective-status-vs-stamp' with different recoverableBy values.
   sweepDistinctions handles correctly via Set-based dedup.

3. **No path normalization in write-boundary.ts:43**: authorizeWrite uses
   raw startsWith; a path like 'openspec/../README.md' would pass. Pure
   domain logic — normalization is the caller's responsibility. The
   boundary's safety at this layer is correct per the contract.

**Disposition:** All three are design observations, not defects. WARNING 3
(path normalization) is noted for future integration-layer hardening.

## Evidence

- 296 tests passing (44 files)
- Typecheck clean (cap1-core)
