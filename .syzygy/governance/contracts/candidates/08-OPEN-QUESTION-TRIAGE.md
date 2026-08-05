# Open-question triage — rev10 (directive §9)

Scope: the 21 open §8 questions carried at the rev9 gate (record §6 — this
set is identical to the "21 unanswered Tier C register items"; [Observed]
RFC 0002 q3/q4 already carry ANSWERED annotations, so the Tier C register
adds no distinct open item) **plus** the six new §8 questions minted by
RFCs 0010/0011. Classification vocabulary (closed):

```text
must close before compacted RFC acceptance
may remain open before OpenSpec
must close before V0 implementation
must close before Mission Control V1
post-V1
```

Per the directive, no blanket "none blocks specification": each row states
*why* its open default cannot alter the meaning of the specifications to be
authored — or is classified to close before the phase where it could.

| Q | Subject | Class | Why the default cannot alter spec meaning (or why it closes) |
|---|---|---|---|
| RFC1 q1 | judgment lapse on split/merge identity | must close before V0 implementation | Drafted default is semantically complete; specs encode it explicitly and a later owner reversal is an in-place amendment to one identity-continuity scenario. Closing at V0 because implementation of continuity is where the answer becomes observable. |
| RFC1 q2 | no doctrine-claim kernel entities at V0 | may remain open before OpenSpec | Pure scope narrowing: either answer adds or omits an entity class; specs authored against the narrowed set stay valid if the owner later widens (additive, non-breaking). |
| RFC1 q3 | decomposition approval inheritance | must close before V0 implementation | Default (no silent inheritance) is the narrow reading; specs encode it; widening later is additive. Observable at V0 approval flows. |
| RFC3 q1 | monorepo subprojects | may remain open before OpenSpec | V0 posture is one governed project per root (drafted default); subproject support is additive structure, not a re-meaning of existing clauses. |
| RFC3 q2 | workspace-manifest classification | must close before Mission Control V1 | Largely settled by RFC10-15: the manifest **stays personal presentation state**; typed portfolio authority lives in the separate workspace governance store. Residual (the manifest's exact category home) cannot alter specs that never treat it as authority — but must close before the store ships, or the boundary blurs. |
| RFC3 q4 | `declarations/` category | **must close before compacted RFC acceptance** | Structural: it fixes RFC3-15's reserved-home set, which every governance spec cites. Already an owner-attention gate item at rev9 (record §9); riding further would bake the drafted default into the accepted digest without a knowing ruling. |
| RFC4 q2 | evidence-envelope minimality | must close before V0 implementation | Envelope fields are additive metadata; the drafted minimum is complete and specs cite the envelope by identity, not by field count. |
| RFC4 q3 | marker-adoption granularity | must close before V0 implementation | Granularity choices select among RFC4-26-conforming policies; the adoption gate's meaning (owner act required) is fixed either way. |
| RFC4 q4 | capture-cadence duty | must close before V0 implementation | Drafted resolution in force; cadence changes staleness *facts*, not staleness *semantics* — RFC2/RFC11-6 disclose staleness whatever the cadence. Owner confirm flagged (it is a duty, so someone must own it at V0). |
| RFC5 q1 | machine-client mechanism | must close before V0 implementation | Rev10-scoped in RFC 0005: selects among RFC5-7's enumerated mechanisms, **each satisfying RFC5-6's contract shape identically**; Mission Control/CLI/MCP specs cite the shape, never the mechanism. Deliberate, knowing deferral — flagged to the owner as before. |
| RFC5 q4 | destructive-op class closure | must close before Mission Control V1 | RFC10-7 envelopes name prohibited surfaces by class; an open class list cannot be cited by a binding envelope. Until closed, envelopes treat unlisted destructive classes as prohibited (narrow reading, RFC10-7). |
| RFC5 q5 | rotation overlap default | may remain open before OpenSpec | Operational default; either value satisfies RFC5-6's rotation contract; observable only as a configuration bound. |
| RFC6 q1 | unpinned-URL default | may remain open before OpenSpec | Exactly the choice OpenSpec authoring makes; the RFC deliberately leaves both readings lawful, and the owner approves the spec that picks one. |
| RFC6 q2 | `not-applicable` scope | may remain open before OpenSpec | Same: vocabulary-application choice made and owner-approved at spec authoring. |
| RFC6 q4 | successor convenience | post-V1 | Pure convenience affordance; absence changes no answer's truth, only navigation effort. |
| RFC7 q2 | primary-narrative cardinality | must close before V0 implementation | Cardinality shapes the Polaris data model; the spec that fixes it is owner-approved, and the RFC's constraint (a primary narrative exists) holds under either answer. |
| RFC7 q4 | rejected-draft retention | must close before V0 implementation | Retention default; either answer preserves the adoption-gate semantics; becomes observable at V0 storage behavior. |
| RFC8 q2 | queue realization | must close before V0 implementation | Drafted default (derived queue, no second store) is complete; realization choices cannot change board semantics, which RFC 0008 fixes; flagged at spec authoring because queue *rendering* is observable. |
| RFC8 q3 | blocked-time cause split | must close before V0 implementation | Metric decomposition; totals and semantics fixed, split adds detail. |
| RFC8 q4 | Unknown-provenance visibility default | must close before V0 implementation | Display default over fixed honesty semantics (Unknown always rendered; only prominence varies). Spec authoring surfaces it; owner approves. |
| RFC9 q2 | undeclared shared-component placement | must close before V0 implementation | Placement default among RFC9-19..21-conforming options; identity counting semantics fixed either way. |
| RFC10 q1 | mission lifecycle × RFC8 work-state review | must close before Mission Control V1 | The lifecycle is explicitly provisional (RFC10-5); its freeze happens *by* the OpenSpec review this question names. Specs authored before the review cite the candidate vocabulary as candidate. |
| RFC10 q2 | autonomy-level floor | must close before Mission Control V1 | Until enumerated, RFC10-7's narrow reading caps every envelope at propose-only — safe default; the enumeration can only widen by owner act. |
| RFC10 q3 | workspace governance store home/schema | must close before Mission Control V1 | Authority split already fixed (RFC10-15); home/schema are structure. Store cannot ship without them. |
| RFC11 q1 | context-budget figure custody | may remain open before OpenSpec | The binding rules (no silent overrun, no mandatory-context drop) are fixed in RFC11-11; the number is a policy default evidenced in the load map. |
| RFC11 q2 | profile registry home | must close before Mission Control V1 | Profiles route fleet work; narrow reading until then: no profile, no routed dispatch beyond direct assignment. |
| RFC11 q3 | memory-promotion act granularity | must close before Mission Control V1 | Default propose-only in force (VIS-4-conservative); batch-approval is a widening only the owner can grant. |

**Summary (machine-recounted from the table above at the rev10 review —
an earlier hand-written summary transposed two figures):** 1 must close
at the compacted-acceptance gate (RFC3 q4 — owner-attention item,
unchanged from rev9); 6 may remain open before OpenSpec (RFC1 q2, RFC3
q1, RFC5 q5, RFC6 q1, RFC6 q2, RFC11 q1); 12 must close before V0
implementation; 7 must close before Mission Control V1 (RFC3 q2, RFC5
q4, RFC10 q1/q2/q3, RFC11 q2/q3); 1 post-V1. Special-attention items from directive §9
are all covered above (RFC5 q1; RFC3 q2 vs RFC10-15; RFC4 q4; RFC8 q2/q3;
RFC8 q4). The **historical-map bundle** (D1-gated, RFC9-41) and **Factory
scene profile** (RFC9-36) are deliberate deferrals with their own owner
gates, not open questions — unchanged at rev10.

## Addendum — the RFC9-9 follow-on (non-numbered open item, rev10)

| Q | Subject | Class | Why |
|---|---|---|---|
| RFC-0009 §10 follow-on | Do RFC9-9's legend/edge-channel rules (three-class edge taxonomy; profile-relation limb; who may add a profile relation, under what gate) need a pass now that A6 minted `declared-dependency` as a kernel relation? Home: RFC1-7/RFC1-26 | must close before V0 implementation | Owner-scoped taxonomy question left open by A6 (which closed only the kernel-minting half of RFC-0001 §8 q6). Safe meanwhile: an unregistered profile relation fails closed under RFC9-26 and never renders unlegended. Map-surface spec authoring (last in the recommended sequence) surfaces it naturally |

Revised summary: **28 open items** — 1 at the gate, 6 may stay open before
OpenSpec, **13** before V0 implementation (12 §8 questions + this
follow-on), 7 before Mission Control V1, 1 post-V1 (the follow-on is not
a §8 question; numbering unaffected).
