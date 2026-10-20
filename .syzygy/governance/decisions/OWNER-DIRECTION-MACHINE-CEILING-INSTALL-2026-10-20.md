# Owner direction — sign and implement the P-114 machine ceiling

Date: 2026-10-20

Owner: Tzeusy

Decision ID: `OWNER-DIRECTION-MACHINE-CEILING-INSTALL-2026-10-20`

This plain direction records the owner's paired signature selection and
bounded implementation authorization. It carries no digest argument and
does not replace the dedicated gate-readable registry act. That act, its
patch and its implementation must be recorded and verified together.

## The owner's answer

[Observed] In the attended Codex owner conversation on 2026-10-20, the lead
offered two actions and asked "Approve both?" The second action was:

> Sign **`pwb-registry-machine-ceiling-amendment-v1.0`** and authorize its exact Ask 2 implementation scope.

The first action was the bounded v4 span installation, recorded in the
sibling screening direction. The owner replied, verbatim:

> yes, approve both

The final offer linked the independently reviewed local decision packet,
item `p114-ceiling-transaction`. The answer selects its option A without
edits: both the named version and its paired implementation, in the same
exchange. No further implementation question is required for that scope.

## Exact transaction

The signed selection is the single manifest row of
`contracts/candidates/pwb-registry-machine-ceiling-amendment/`, version
`pwb-registry-machine-ceiling-amendment-v1.0`, cleared by
`docs/reviews/R-PWB-REGISTRY-MACHINE-CEILING-AMENDMENT-2-RAW.md` with the
three notes retained in `ROUND-2-DISPOSITIONS.md`. Only the registry entry's
machine ceiling changes: 8,388,608 to 16,777,216 bytes. The package and its
reviewed source remain frozen.

Implementation is exactly `OWNER-DECISION-PACKET.md` Ask 2 items 1–5:

1. The runtime `PWB_RESOURCE_LIMITS.maxMachineResponseBytes` constant.
2. The registry gate's record, act identity, recording tag and supersession
   pointers, retaining the scope anchors.
3. Necessary tests pinning the previous value or act.
4. The four specifically named builder/recorder successors in impact-ledger
   part B2, each recognizing only this package's performed amendment row.
5. This sign-off's dedicated recorder, governance registration and performed
   history, plus builder/recorder battery and hosted-workflow entries and
   their derived count sentence.

Record, patch and implement as one reviewed logical transaction. Preserve
the predecessor act and performed manifests. Distinguish static builder
checks, registry/runtime parity, recorder predicates and full authority
evaluation; a pass in one proves no other. Run the canonical battery in a
clean clone, appropriate code gates and a private size-only measurement
under existing source consent before completion. Create and push the named
version tag on the main commit carrying the record. Work item:
`syzygy-59s5`.

## Order and bounds

- Serialize shared authority-gate changes after the screening install's
  reconciliation; do not duplicate an active implementation lane.
- No other registry value, version string, human ceiling, policy, source
  scope, repository read or provider egress change.
- P-100 reinstatement remains a separate already-authorized work item with
  its own review and measurement. This direction does not perform it.
- P-115 remains subsequent specification work under the existing
  ceiling-first direction; this answer does not sign or implement it.
- No release, deployment, live activation, second repository or edit to
  previously bound bytes. Withdrawal defeats grant.
