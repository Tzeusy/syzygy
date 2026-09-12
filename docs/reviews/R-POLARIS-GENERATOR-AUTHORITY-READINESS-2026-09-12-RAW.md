# Polaris generator authority and lifecycle readiness review

Verdict: NOT READY FOR SPECIFICATION AND IMPLEMENTATION APPROVAL.

Scope: bounded candidate/design readiness review, not implementation confirmation,
owner judgment, an applicability waiver or a completed full-contract sweep.
Reviewed requirements 013, 015-022, 025, 028-029 and their supporting contracts,
plus the delivery proposal. No observed-project bodies or credential stores read.

## Findings requiring concrete disposition

### AR-1 — The proposed delivery staging has not changed the mandatory contract

REQ-polaris-generation-028 remains v1-mandatory and requires normalized work
fields on every rendering/filter/count/export/machine answer. Its scenario
“Generation activity lacks a qualifying worker signal” explicitly leaves the
bound-but-no-signal case as a conformance finding. WORK-STATE-CONTRACT.md records
it as unresolved, and tasks.md 2.13 makes resolution part of delivery. The new
delivery proposal correctly says it is not a binding N/A, so it cannot make this
candidate approvable by itself.

Action: edit requirement 028, that scenario, WORK-STATE-CONTRACT.md, tasks.md,
CAPABILITY-COVERAGE.md and the consequence coverage together to state exact phase
applicability. Keep stage receipts, cancellation, actual failure/partial outcomes,
shared lifecycle and same-run identity required in the initial data path. Identify
which specific normalized-worker consumers are deferred, mapped to existing
approved requirements, or require a reviewed owner-bound N/A/amendment. A mere
“where applicable” qualifier is insufficient. If the complete chosen workflow
still projects a claimed worker with effective bound but no qualifying signal,
resolve that predicate before claiming complete support; no provider receipt can
substitute for RFC4-23 progress. This finding does not require the no-signal
amendment before pure source/authoring/preview mechanics are staged.

Governing evidence: RFC8-13 defines active from a claimed item and qualifying
progress; activity-undetermined currently addresses an undeclared bound.
RFC7-38 requires per-observable-consequence approved coverage or effective
reviewed N/A, not a drafting agent's scope assertion.

### AR-2 — Approval coverage and existing-capability overlap remain unfinished

CAPABILITY-COVERAGE.md is explicitly only MG-01..17 product mapping, not
CC-SPEC-8/11 confirmation. GOVERNING-DEPENDENCIES.md is a union of warrants,
not consequence-level applicability. proposal.md explicitly leaves host-auth
and existing-capability overlap to a future review. Consequently the package
cannot yet establish what the owner would amend versus newly authorize.

Action: extend coverage with consequence, applicability rationale, exact target
requirement/scenario, existing approved requirement where reused, and amendment
or reviewed-N/A disposition. For requirements 017/019/021/022/025 specifically,
resolve PWB source adaptation, host data/mutation admission, credential storage,
protected audit and classification/retention against their current capability
homes. Preserve the signed PWB files; put necessary changes in a successor
amendment package rather than editing their bytes. Requirements 013/020 must
identify the actual scheduler/materialization integration, not imply current POC
fixtures already implement it. Retain all later owner-flow and portability
obligations; this is not permission to approve only a CLI and call it complete.

Governing evidence: RFC7-38 says every observable consequence must map, rather
than one requirement per clause. RFC8-9 expressly preserves scheduler authority
after materialization; it is not just a Polaris-versus-Trajectory UI convention.

### AR-3 — The protected-effect implementation route is still a design obligation

SECURITY-CONTRACT.md correctly rejects same-untrusted-user writable audit storage
and explicitly says the chosen recorder must demonstrate the boundary. The
delivery proposal places persistence/effects at an app boundary but names no
trusted storage/recorder arrangement. This is not a flaw in the abstract security
requirement; it is an unresolved prerequisite to a concrete implementation/effect
approval. Reusing an ordinary application file cannot satisfy the stated design.

Action: add a bounded implementation decision naming the recorder trust boundary,
which process/principal may append, verification and recovery interfaces, and
how tests attempt writes as the excluded actor. Add explicit scenarios under 022
for forged/replaced audit records and unavailable trusted recovery across restart;
retain the current stop-during-outage exception without upgrading mutable pending
work metadata to ceremony evidence. Tie the chosen arrangement directly to
provider and authorship effects; do not expand into unrelated platform hardening.

Governing evidence: RFC5-25 requires the trail outside the governed tree and
outside untrusted write reach; storage medium is an implementation-slice choice.

## Non-blocking clarifications and preserved strengths

The candidate already distinguishes source/provider/write/execution consent,
current checks before effects, incomplete dispatch from no effect, per-block
human adoption, editorial inference and kernel truth. Requirements 016/018/019
provide useful atomic receipt, actual-history and identity/version boundaries.
No independent semantic defect is established here for those representations.

Executable schema encodings may be implementation artifacts under the existing
SCHEMA-CONTRACT.md rule; an unimplemented JSON schema alone is not a reason to
extend specification drafting indefinitely. Likewise actual provider/model and
second-project choice can remain effect-admission inputs until real calls/reads,
but must be concrete and effective before those proofs are attempted.

REQ015's profile state and REQ010's authorship state remain distinct; do not
collapse them when integrating the new bundle renderer. Independent review is
not narrative adoption. The actual owner start/review experience, two real
projects and changed-source run remain completion requirements.

## Recommended approval route

Close AR-1/2 through a focused consequence and phase disposition, choose the
minimal protected effect arrangement in AR-3, freeze and independently review
the resulting exact specification/implementation package. Permit staged pure
mechanics only within that package's actual authorization. Bring concrete source,
provider and write permissions to the owner before real effects, with unchanged
approvals reused rather than asked repeatedly. Retain later stages as open until
the full owner-facing generator and real portability/quality evidence exist.

## Frozen subjects

The following hashes identify bytes examined, not adopted authority. Any edits
retire this review's applicability to those subjects.

- openspec/changes/polaris-manifesto-generation/CAPABILITY-COVERAGE.md: 3e9b61f585ab8fd72f58bbe71b60f9277c5dfd38e3eddb149e53f6eba427624d
- openspec/changes/polaris-manifesto-generation/INTERFACES.md: 96e7e396c825d614503253ea45cd0c4317051516c5159e8f120d2786be7243dc
- openspec/changes/polaris-manifesto-generation/design.md: fcb70c557d4723d4e9a7699f2ac34bfa7f0cf42cdd348c32b050a27fe49e6e31
- openspec/changes/polaris-manifesto-generation/SECURITY-CONTRACT.md: b4182fff554bfb5cf8053738b430e3a29f343670f2317f524fb21a4c8bdf488e
- openspec/changes/polaris-manifesto-generation/proposal.md: 9ffb130222b6b7251936fd4134d363c514b0f69f64c2e29b5f20df8d92367f18
- openspec/changes/polaris-manifesto-generation/OWNER-FLOW.md: 414d845d91b52578c58474446d5feb6c7dc9f1185d8625e4c8ae794edc48c5a9
- openspec/changes/polaris-manifesto-generation/ASSET-CONTRACT.md: c250ee69072b0d4d1bab8da246712f463b70f630fb30e92bb51f3b0f13869f15
- openspec/changes/polaris-manifesto-generation/WORK-STATE-CONTRACT.md: e7b96a532e3a64da10f2a5433e13e732c5d63df08ab1d7eaf9e906c66c68c9e7
- openspec/changes/polaris-manifesto-generation/DESIGN-ACCEPTANCE.md: d2ff62db58995ef1fe44b3b6044917743ab5546b56827ba492f1b8ff8580f067
- openspec/changes/polaris-manifesto-generation/ADAPTER-DECLARATIONS.md: 3836b93909611fd59890450383e897f9635ee4ba4cd4b5a22ccd611d9ea33564
- openspec/changes/polaris-manifesto-generation/SOURCE-POLICY.md: af26acc453396d8b8ddbad94d939bd56f3d87b30ef2a0d3a411c378c48fbba89
- openspec/changes/polaris-manifesto-generation/WORK-STATE-NO-SIGNAL-DELTA.md: ee031ece19eba7785fe0a44b2506bae23e98983900036985110ca528c5bebd76
- openspec/changes/polaris-manifesto-generation/.openspec.yaml: 2f19e85bc27192bfcfbe4fcfb49c1e49b7569f6d840f97966b535a07da28bc59
- openspec/changes/polaris-manifesto-generation/SCHEMA-CONTRACT.md: 722eea7233cfb913f4f2e21060f359d721a86336efa1a3851e31ba113a857e8f
- openspec/changes/polaris-manifesto-generation/GOVERNING-DEPENDENCIES.md: a9d1c255f10a5e20a4d5649aeec2dfe56dc376a71def6c417f008e7ef5bc89b1
- openspec/changes/polaris-manifesto-generation/tasks.md: 6f468f0d14a1512a4c4e5ff63ac7034c4d7529dfdcb075b250df2382e80539d4
- openspec/changes/polaris-manifesto-generation/ENTRY-AND-WALKTHROUGH.md: cdc817aed4f1ffae8f83a6a3e23ffa080eb5a0b0e16aed1efe9fda85bf98d0bf
- openspec/changes/polaris-manifesto-generation/NAVIGATION-CONTRACT.md: e30570230c93516adb8d44e30bb810dc4df5ccde3f7d9a32a215214af3cdc321
- openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md: 2606f49320712b8b1f25974dec4fc0295ad585d4aa0a75ae5cce2592c4dce2be
- docs/design/POLARIS-GENERATOR-DELIVERY.md: 51f878fe4cb0dc90ca033ecef399a61d3fa2b825794bf69fdcb256dfc1e407bb
