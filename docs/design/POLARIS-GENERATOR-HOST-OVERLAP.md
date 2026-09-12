# Generator host and PWB overlap disposition

Candidate engineering analysis against the baseline recorded in the [structured inventory](../evidence/polaris-generator-host-overlap-2026-09-12.json). This document is not an act, owner N/A, source/provider permission or implementation authorization.

The chosen integration is additive: retain the current bounded PWB observer, exact-source routes, narrative wire form and Dolt observation; introduce explicit source and presentation adapters plus generator-specific operation admission and execution records. Existing code is reused only for the behavior named below. A function with a similar name is not proof of the new contract.

The structured inventory owns exact approved requirement/scenario references, source digests, implementation seams and verification obligations for every row. References were checked against their containing requirement, not merely found elsewhere in the file.

| ID | Observable operation | Disposition |
|---|---|---|
| H01 | Retain current machine coverage admission | reuse-unchanged |
| H02 | Admit generator browser reads and mutations | new-behavior |
| H03 | Issue rotate revoke generator credentials | new-behavior |
| H04 | Host deployment and shared-origin credential isolation | unresolved |
| H05 | Read existing Butlers project-shape source | reuse-unchanged |
| H06 | Admit a second project and classify provider-bound composites | new-behavior |
| H07 | Screen incoming sources and generated artifacts | new-behavior |
| H08 | Adapt captured anchors into generic draft bundles | new-behavior |
| H09 | Serve exact requirements beside generated interpretation | reuse-unchanged |
| H10 | Observe scheduler-owned work lifecycle | reuse-unchanged |
| H11 | Prepare and materialize generalized warranted work | new-behavior |
| H12 | Reserve dispatch and expose run progress/cancel/retry | new-behavior |
| H13 | Register and resolve provider/lifecycle/artifact adapters | new-behavior |
| H14 | Protect audit and enforce prospective effect revocation | unresolved |
| H15 | Change an existing adopted route or PWB behavior instead of preserving adapter boundaries | required-signed-spec-amendment |

## Concrete integration decisions

- The current origin helper validates Host and a present Origin, but admits missing Origin without session or anti-forgery proof. Preserve that legacy helper's existing contract; do not mistake it for generator act admission. Generator routes need the new principal/session/scope checks before their handler runs.
- The current daemon mints and persists a presentable token at startup and captures its expected value. The generator credential store must instead implement its declared verifier, ceremony, scope and next-request revocation behavior. Existing CAP1 token admission remains a separate compatibility surface.
- The current materializer handles one fixed packet and external reference. Its lost-local-record recovery constructs a record from an existing bead. Generalized materialization must preserve uncertainty and its immutable join/adjudication requirements; calling this old helper does not implement them.
- PWB capture and exact-source rendering keep their existing read gates and source population. Another project uses a separately admitted adapter. Generic wire support does not widen Butlers' content policy.
- Generic anchors adapt from the PWB wire form explicitly. Revision, evaluation and narrative identity remain different; unsupported conversion yields an explicit inability.
- Stage receipts and budget control are execution metadata. Dolt remains the source of scheduler lifecycle, and completion does not prove reconciled intent.

## Remaining decisions

H04 requires a concrete host/process/origin boundary and a route inventory demonstrating that legacy human-open routes cannot expose protected generator artifacts or credentials. H14 requires a protected audit and protective-stop substrate, including actual denied writes by the generating actor. These are necessary effect-host decisions, not a request to build a generalized identity platform. They remain unresolved here and are owned by the separate host/audit design work.

H15 is conditional: the additive choices avoid changing the listed adopted PWB/CAP1 outcomes. If implementation instead changes one, its exact semantic delta requires the signed amendment before that change. This document neither declares a blanket exemption nor silently amends accepted files.

No approved requirement is invented for new provider dispatch, generalized materialization or generator sessions. The adjacent approved scenarios in those rows protect the existing behavior; the candidate requirement owns the proposed additional operation, subject to its adoption and implementation gates.

## Verification status

[Observed] This pass inspected current implementation and checked each named scenario within its exact approved requirement. The JSON records source digests for reproducibility. No runtime behavior was changed or tested, no external project body was read, and no provider was invoked. Implementation evidence must still exercise each row's requiredVerification and the final owner flow; this inventory is an overlap disposition, not a conformance report.
