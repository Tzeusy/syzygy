REVISE

Reviewed exact diff `31571f6..c68b268a665e5872a96f3baf906ab929d413ec2e`.

1. **P1 — Named missing sources disappear.** `packages/three-surface-poc-core/src/project-shape-manifest.ts:474` skips every baseline-spec-shaped or roster-shaped named path. The subsequent tree rules restore only existing blobs. [Observed] An in-memory fixture declaring `openspec` and `roster` homes, whose indexes name an absent spec and absent butler configuration, reports `namedSources: 1` for each pillar but omits both named sources from the manifest. Non-blob entries have the same gap. This violates PWB-REQ-001’s complete population and the engineering bar’s failure-path requirement. Skip only sources actually supplied by the tree rules; retain missing/non-blob anchors and add regression coverage.

2. **P2 — Repeated discovery traversal is uncharged.** `packages/three-surface-poc-core/src/project-shape-observation.ts:479` derives pillar roots, then `project-shape-manifest.ts:413` repeats that derivation. [Observed] Both execute under the single charge at observation line 468; the comment explicitly acknowledges the repetition. The registry’s `resourceLimitSemantics.maxParsePassesPerSource` states “repeating a pass counts again.” [Inferred] The resource ledger therefore understates work and can admit processing beyond the declared parse envelope. Reuse the screened derivation or charge the repeated pass, with boundary coverage.

[Observed] The focused manifest and observation suites passed: 61 tests across two files. The missing-source reproduction used current TypeScript transpiled in memory and synthetic inputs; no files were edited or external repository bodies read. The retained ordering-mutation record was inspected but mutations were not rerun. The full governance battery and live walkthrough were outside this review.

The proposed fixes address both findings in principle; confirmation requires review and validation of their resulting exact head.
