# Semantic delta — PWB behaviour-contract re-pin (registry entry and secret policy)

> **Candidate — binds nothing.** Drafted by an agent for bead
> `syzygy-jloi`. Effect over either subject would come only from that
> subject's own superseding owner act. No review has been run against
> these bytes.

**Artifact(s):**
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
and
`.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`.
The proposed bytes exist only as `proposed/*.patch` applied to the bytes
the acts in force bound.

**Stable IDs affected:** none minted, renamed or retired. The changed
field is `governingBehaviorContract` (keys `version` and `signedBy`), which
both artifacts carry for PWB-REQ-005's "governing behaviour contract"
reading. Requirement identities are untouched.

**Change class:** Normative.

**Author:** Claude agent session, 2026-10-02.

**Date:** 2026-10-02.

## Current meaning

Both artifacts carry, byte for byte (registry entry at `entries[0]`,
policy at the top level):

```json
"governingBehaviorContract": {
  "id": "polaris-project-wide-butlers-model",
  "version": "sha256:<the 2026-09-05 truth-and-readiness spec.md digest>",
  "signedBy": "pending exact owner act over the PWB truth-and-readiness amendment manifest"
}
```

The digest is elided here on purpose: it is a superseded act argument, and
the exact bytes are in the two files and in the patches' minus lines. Read
literally, each artifact declares that the PWB behaviour it governs is the
2026-09-05 `spec.md`, and that the act signing it is still pending. Both
statements are false today. [Observed] The 2026-09-05 act was performed
(`decisions/PWB-TRUTH-READINESS-AMENDMENT-ACT.md`), and eight later PWB
outcomes each moved `spec.md`: the opening-band act (2026-10-01), the
render-mode and machine-view acts, and the missing-currency,
dismissal-expiry, container-shape, item-depth and readability sign-offs
(2026-10-02). `scripts/check_spec_reconciliation.py` R6 reports both pins
as Unknown.

## Proposed meaning

```json
"governingBehaviorContract": {
  "id": "polaris-project-wide-butlers-model",
  "version": "sha256:<the spec.md row of PWB-READABILITY-SUCCESSOR-MANIFEST.txt>",
  "signedBy": "version-tagged sign-off pwb-readability-successor-v1.0, recorded at .syzygy/governance/decisions/PWB-READABILITY-SUCCESSOR-SIGNOFF-v1.0.md"
}
```

The pinned digest is the `spec.md` row of the signed package
`contracts/candidates/pwb-readability-successor/` (tag
`pwb-readability-successor-v1.0`), which is also the current `spec.md`.
The builder derives it from that row and refuses a package whose pin is
not the current `spec.md`.

Why Normative rather than Clarifying: the field names which behaviour the
entry and the policy serve. Moving it from the 2026-09-05 specification to
the current one changes what a reader may take each artifact to govern
(PWB-REQ-001 through PWB-REQ-022 as signed now, rather than the
2026-09-05 set). No reader is put out of compliance by it, but the
governed object changes. Hence Normative.

## What explicitly does NOT change

- Every other byte of both files, including `registryVersion` and the
  entry's `observerVersion` (`1.2.0-candidate.1`), the policy's
  `policyVersion` (`1.1.0-candidate.1`), discovery version, resource
  limits and their semantics, currency bounds, briefing ceiling, detectors,
  classification order, access boundary, and the two keys that carry the
  governance lifecycle (the top-level `status` value and the entry's
  adoption key). The
  builder checks this by parsing: with the old contract object put back,
  each proposed document equals its act-in-force document. It also checks
  that exactly two lines change.
- `governingBehaviorContract.id`.
- Consent. The observation consent and its act are not touched.
- No write, egress, execution or second-repository capability is added,
  and no new field is consumed by code.
- **Version labels stay where they are, by choice.** A version bump would
  change the read gate's scope anchors (`1.2.0-candidate.1` and
  `1.1.0-candidate.1` in `apps/three-surface-poc/src/governance-inputs.ts`)
  and the tests that read `policyVersion` from the file. The re-pin
  changes no declared mapping the implementation reads, so it keeps both
  labels. The owner may ask for a bump instead; open question 2 of the
  owner packet sets out the cost.

## Warrant

Bead `syzygy-jloi`, found by the `syzygy-73e.5.6` reconciliation (R6).
The prior disclosures of the stale pin are in
`pwb-opening-band-scenario/IMPACT-LEDGER.md` (Class 3) and
`pwb-missing-currency-disclosure-scenario/IMPACT-LEDGER.md`
("Behavior-contract pins"). The P-74 and P-78 rows recorded that the
registry entry is edited on no arm of those moves. This package is the
separate repair those notes deferred.

## Evidence or decision basis

- The two acts in force: `decisions/PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md`
  (registry) and `decisions/PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md`
  (policy). The builder requires the current subject bytes to hash to each
  record's `Exact digest (SHA-256)` line.
- The signing record: `decisions/PWB-READABILITY-SUCCESSOR-SIGNOFF-v1.0.md`
  and its package manifest.
- `decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`, for
  why the policy is outside Scope A and why the registry is offered by a
  digest act anyway (owner packet, "Signing path").

## Terms introduced / retired

None.

## Downstream impact

See `IMPACT-LEDGER.md`. In short: [Observed] no TypeScript under
`packages/` or `apps/` reads `governingBehaviorContract` (0 matches).
The impact is on governance tooling and on the body-read gate's act
pointers, not on observation behaviour.

## Migration / supersession plan

Two superseding owner acts, one per subject, in the shape of the
2026-09-05 pair (Decisions 2 and 3 of `pwb-truth-policy-amendment`), plus
one plain continuation direction that re-points the body-read gate. Each
act's recorder applies its own patch through
`scripts/build_pwb_behavior_contract_repin.py --apply <subject>
--at-adoption` in the change that writes its record. The superseded records
stay immutable history. The adoption-change list is in the owner packet.

## Review

**Required class:** CC-REV-1 fresh-context review of the package (the
brief is `REVIEW-BRIEF.md`).
**Reviewer:** not yet dispatched.
**Verdict:** none.
