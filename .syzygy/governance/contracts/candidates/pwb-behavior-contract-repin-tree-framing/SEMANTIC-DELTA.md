# Semantic delta — PWB behaviour-contract re-pin to the tree-framing sign-off (registry entry and secret policy)

> **Candidate — binds nothing.** Drafted by an agent for bead
> `syzygy-2g0d`. Effect over either subject would come only from that
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

**Author:** Claude agent session, 2026-10-03.

**Date:** 2026-10-03.

## Current meaning

Both artifacts carry, byte for byte (registry entry at `entries[0]`,
policy at the top level):

```json
"governingBehaviorContract": {
  "id": "polaris-project-wide-butlers-model",
  "version": "sha256:<the spec.md row of PWB-READABILITY-SUCCESSOR-MANIFEST.txt>",
  "signedBy": "version-tagged sign-off pwb-readability-successor-v1.0, recorded at .syzygy/governance/decisions/PWB-READABILITY-SUCCESSOR-SIGNOFF-v1.0.md"
}
```

The digest is elided here on purpose; the exact bytes are in the two files
and in the patches' minus lines. They are the bytes the 2026-10-02
behaviour-contract re-pin acts bound
(`decisions/PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md`
and `decisions/PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md`). Read
literally, each artifact declares that the PWB behaviour it governs is the
`spec.md` signed as `pwb-readability-successor-v1.0`. That stopped being
true on 2026-10-03. [Observed] The version-tagged sign-off
`pwb-tree-framing-amendment-v1.0`
(`decisions/PWB-TREE-FRAMING-AMENDMENT-SIGNOFF-v1.0.md`) applied a
`spec.md` patch that added seven PWB-REQ-014 scenarios, and
`scripts/check_spec_reconciliation.py` R6 again reports both pins as
Unknown.

## Proposed meaning

```json
"governingBehaviorContract": {
  "id": "polaris-project-wide-butlers-model",
  "version": "sha256:<the spec.md row of PWB-TREE-FRAMING-AMENDMENT-MANIFEST.txt>",
  "signedBy": "version-tagged sign-off pwb-tree-framing-amendment-v1.0, recorded at .syzygy/governance/decisions/PWB-TREE-FRAMING-AMENDMENT-SIGNOFF-v1.0.md"
}
```

The pinned digest is the `spec.md` row of the signed package
`contracts/candidates/pwb-tree-framing-amendment/` (tag
`pwb-tree-framing-amendment-v1.0`), which is also the current `spec.md`.
The builder derives it from that row and refuses a package whose pin is
not the current `spec.md`.

Why Normative rather than Clarifying: the template's test is whether
someone who complied before may not comply now. The field names which
behaviour the entry and the policy serve, and the newly pinned `spec.md`
adds seven PWB-REQ-014 tree-framing scenarios. An observer that conformed
to the readability-successor `spec.md` the artifacts declared until now
may not conform to the one they would declare. Hence Normative, the class
the 2026-10-02 re-pin took for the same move.

## What explicitly does NOT change

- Every other byte of both files, including `registryVersion` and the
  entry's `observerVersion` (`1.2.0-candidate.1`), the policy's
  `policyVersion` (`1.1.0-candidate.1`), discovery version, resource
  limits and their semantics, currency bounds, briefing ceiling, detectors,
  classification order, access boundary, and the two keys that carry the
  governance lifecycle (the top-level `status` value and the entry's
  adoption key). The builder checks this by parsing: with the old contract
  object put back, each proposed document equals its act-in-force
  document. It also checks that exactly two lines change.
- `governingBehaviorContract.id`.
- Consent. The observation consent and its act are not touched.
- No write, egress, execution or second-repository capability is added,
  and no new field is consumed by code.
- **Version labels stay where they are, by choice**, as in the 2026-10-02
  re-pin. A bump would change the read gate's scope anchors
  (`1.2.0-candidate.1` and `1.1.0-candidate.1` in
  `apps/three-surface-poc/src/governance-inputs.ts`) and the tests that read
  `policyVersion` from the file. Open question 2 of the owner packet sets
  out the cost.

## Warrant

Bead `syzygy-2g0d`. `scripts/check_spec_reconciliation.py` R6, re-derived
over the tree-framing sign-off on 2026-10-03 (`syzygy-73e.9`), reports both
pins as Unknown. The 2026-10-02 re-pin packet's open question 3 disclosed
that the next `spec.md` change would reopen this gap; this is that case,
one day later.

## Evidence or decision basis

- The two acts in force: `decisions/PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md`
  (registry) and
  `decisions/PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md`
  (policy). The builder requires the current subject bytes to hash to each
  record's `Exact digest (SHA-256)` line.
- The signing record: `decisions/PWB-TREE-FRAMING-AMENDMENT-SIGNOFF-v1.0.md`
  and its package manifest.
- `decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`, for
  why the policy is outside Scope A and why the registry is offered by a
  digest act anyway (owner packet, "Signing path").

## Terms introduced / retired

None.

## Downstream impact

See `IMPACT-LEDGER.md`. In short: [Observed] no TypeScript under
`packages/` or `apps/` reads `governingBehaviorContract` (one match, a
comment in `governance-inputs.ts` saying so). The impact is on governance
tooling and on the body-read gate's act pointers, not on observation
behaviour.

## Migration / supersession plan

Two superseding owner acts, one per subject, in the shape of the
2026-10-02 pair, plus one plain continuation direction that re-points the
body-read gate. Each act's recorder applies its own patch through
`scripts/build_pwb_behavior_contract_repin_tree_framing.py --apply
<subject> --at-adoption` in the change that writes its record. The
superseded records stay immutable history. The adoption-change list is in
the owner packet.

## Review

**Required class:** CC-REV-1 fresh-context review of the package (the
brief is `REVIEW-BRIEF.md`).
**Reviewer:** not yet dispatched.
**Verdict:** none.
