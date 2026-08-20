<!-- Owner act, recorded verbatim. Never edit below the line.
     Act family: implementation authorization (rests on the adopted
     Capability 1 specification — decisions/CAPABILITY-1-SPECIFICATION-
     ADOPTION-ACT.md, verified present at recording).
     Act dated 2026-08-21 by the owner; recorded 2026-08-21 by the session
     the owner instructed, at repository state 9a67b76. The prepared packet
     this act supersedes is
     contracts/candidates/round-2026-08k/CAPABILITY-1-IMPLEMENTATION-
     AUTHORIZATION-PREPARED.md (banner-marked performed, preserved).
     Everything below this line is the owner's act, byte-for-byte. -->

OWNER ACT — CAPABILITY 1 IMPLEMENTATION AUTHORIZATION
Date: 2026-08-21
Owner: Tzeusy

Resting on the adopted Capability 1 specification recorded at:

.syzygy/governance/decisions/CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md

I authorize implementation planning and implementation for:

Capability 1 — Project registration and honest shape visibility.

This authorization includes:

1. preparing one concise implementation plan;
2. selecting the implementation stack and detailed repository layout;
3. creating and maintaining a bounded Capability 1 Beads backlog;
4. creating application and library code, tests, developer tooling, and
   ordinary build configuration;
5. running the authorized worker and review workflows needed to implement,
   test, and integrate Capability 1.

Stack and layout selection are delegated to the implementation-planning
process. They do not require another owner act unless the proposed choice:

- changes adopted doctrine or an accepted contract;
- requires an amendment to the adopted Capability 1 specification;
- changes security posture, privacy or retention obligations, or a
  normative data contract;
- exceeds the recorded operating constraints or resource envelope;
- or materially expands the implementation beyond Capability 1.

The implementation plane may use ordinary repository-root implementation
paths, including `apps/**`, `packages/**`, supporting test/tooling paths,
and root build or dependency manifests. The implementation plan shall name
the exact selected layout before substantive code is added.

`openspec/**` and `.syzygy/**` remain the governed project-artifact plane.
Implementation code shall not be placed there. The Syzygy product itself
remains prohibited from directly writing implementation code; code changes
are materialized by explicitly authorized worker agents or humans through
the development workflow.

The currently in-force craft-and-care policies and vendored
`th-engineering` standards govern implementation. In particular:

- implementation must trace to the adopted specification requirements;
- every implemented requirement must have corresponding verification;
- defect fixes require reproducing tests except for lawfully recorded
  infeasibility;
- no success or positive status may be produced without current evidence;
- Unknown, stale, absent, and failure paths are first-class test cases;
- non-trivial and risk-floor-touching changes receive independent review;
- verification claims require retained, resolvable evidence;
- implementation changes remain reviewable and are split before becoming
  oversized.

The first implementation output shall be a concise plan that identifies:

- the selected stack and its rationale;
- the selected repository layout;
- the initial implementation slices;
- the mapping from those slices to CAP1 requirement IDs;
- the testing and retained-evidence approach;
- the applicable risk and review classes.

That plan is implementation guidance, not behavioral authority. The adopted
OpenSpec specification remains the authority for required behavior.

This authorization covers Capability 1 only.

It does not authorize:

- authoring or implementing another capability;
- changing the adopted Capability 1 specification outside its governed
  amendment process;
- accepting or implementing deferred Waves C1, C2, D1, or D2;
- substantive Mission Control behavior;
- the full Polaris, Trajectory, or Orrery products;
- deployment to a production or externally accessible environment;
- onboarding or observing an external project;
- weakening any doctrine, contract, security, evidence, identity, or write
  boundary.

Local development, test execution, and a local demonstration are authorized.
Production deployment, external-project onboarding, and any broader release
remain separate future decisions.

All implementation remains within the recorded P-35 operating constraints
and P-45/A6 resource envelope.

Record this act verbatim at:

.syzygy/governance/decisions/CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md

Then:

1. update PROJECT-STATUS.md and AGENTS.md to record that Capability 1
   implementation is authorized;
2. correct the stale status statement saying the authorization packet was
   not prepared;
3. prepare the concise implementation plan;
4. initialize the bounded Capability 1 Beads backlog;
5. begin implementation through the authorized worker workflow;
6. preserve the adopted specification artifacts unchanged;
7. do not begin another repository-wide project-shape or launch review.
