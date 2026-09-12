# Generator request security and audit — candidate

Proposed behavior for REQ-polaris-generation-021/022. This document grants no
credential, consent, exposure change or operational effect. Existing RFC5
mechanism choices and effective owner acts remain controlling.

## Authenticate the caller, then authorize the operation

Every authenticated act names exactly one principal: owner, machine client or
Syzygy acting through its adapter. Authorization uses that principal's explicit
scopes and project access, never the assumption that one human owns everything.
Audit/consent/approval records name their principal. A successful login is not
permission to start a run, read another project, export or adopt a draft.

Requests have only the existing two client classes. A valid machine credential
classifies the request as machine; other requests must satisfy browser discipline.
Network location, first-party packaging and absent Origin headers classify no
identity. Official CLI/protocol clients use their own machine credentials;
session cookies are not transferable machine credentials. A browser presenting
a machine credential does not obtain a browser session.

The route inventory covers project/source selection, request preparation,
start/resume/retry, progress and artifact retrieval, cancellation/rejection,
profile/consent/approval ceremonies, authorship, reversal, export and recovery.
Each route declares whether it serves project data or changes state, required
principal scopes, project/subject resolution, and the effective gates it invokes.
Changing an identifier in a request never changes what the caller may access.

## Browser and machine admission

Data-bearing and state-changing browser routes require an owner-attended session,
including on loopback. Sessions have declared maximum lifetime and immediate
owner revocation effective at the next request. Without a declared lifetime they
do not persist beyond the process. Session identity is credential-based, not
device/IP-based. Reauthentication restores admission, not revoked project consent.

Every state-changing browser request requires per-session anti-forgery proof.
Present Origin and Sec-Fetch-Site values must satisfy the active allowlist;
absent headers neither admit nor condemn, and the proof still applies. Host must
belong to the exposure mode's closed hostname set before application logic.
Origin matching alone is not a session or anti-forgery proof.

Machine credentials identify one opaque machine client, are explicitly scoped,
and are issued only through the existing owner-attended ceremony. An unscoped
credential is invalid. Rotation preserves client identity and uses only the
owner-declared overlap; revocation can target identity or instance and applies
at the next request. The server stores only a verifier, not a presentable secret.
Credential governance metadata contains identity, scopes, issuance/expiry and
revocation, never secret bytes. Neither another machine credential nor observed
project content can issue one.

Unauthenticated access is limited to health/liveness and authentication bootstrap,
without project data; the existing interface-qualified device restrictions and
owner-attended issuance still apply. Fresh installation stays loopback-only.
Any non-loopback serving requires the effective exposure act, declared hosts,
TLS and owner-device restriction, plus full application authentication. Overlay
device identity is not client identity. This feature enables no new exposure mode.

## Keep request, execution and adapter identities distinct

A background run uses its independently valid execution warrant and Syzygy's
authorized adapter credentials. Expiry of the initiating browser session blocks
subsequent requests from that session; it does not retroactively revoke a valid
execution warrant. A worker cannot continue using the expired session as its own
credential. Each later effect still checks current consent/profile/adapter scope.

Adapter credentials are a separate, per-adapter/per-authority population, scoped
to the permitted effects, never indexed or surfaced. They and credentials that
authenticate to Syzygy are never injectable into observed-project execution.
Adapter effects are attributed to Syzygy, with initiating request provenance
linked separately rather than pretending the owner's browser performed them.

## Revocation changes enforcement immediately

Request admission, provider egress and artifact writes check current credential,
consent and applicable profile state at the attempted act. An earlier scheduler
observation, dispatch reservation or authored-write commitment is no exemption.
Already transmitted work may be in flight; revocation does not prove remote
termination or erase incurred charges. Supported cancellation, uncertain effects
and late receipts retain their real outcomes. Observed-code execution, if ever
separately authorized, retains its own stricter profile termination obligations.

Recording revocation immediately labels every subsequently served dependent
claim with withdrawal and triggers a new identified evaluation. Until it
completes, the previous evaluated value remains with the withdrawal visible;
the security act does not rewrite immutable claim values itself. The owner can
see what was revoked, when, by whom and the resulting dependent states. Restoring
permission requires a fresh grant/record, not silently flipping a revoked flag.

## Protected audit trail

Each admission, denial, egress, run launch, adapter effect, consent grant or
revocation, and credential issuance/rotation/revocation emits an audit record.
It carries principal, credential or session identity, act, subject, exposure
mode, actual act instant and outcome, plus durable evidence identity, integrity,
source, capture time, scope and provenance. An unresolved identity on a refused
request is explicit; the recorder never fabricates an owner principal or logs a
presented credential to fill the field. Act instant, capture time and claim
evaluation/as-of time remain distinct.

The trail resides outside the governed plane and outside the untrusted actor
class's write reach. A work record, file in the repository, or owner-user-only
directory writable by the same untrusted process is not that boundary. The
chosen recorder/storage must demonstrate protection against those writers.
Audit records contain no credential values, secrets or excluded bodies; rejected
offending payloads use permitted digest provenance, never payload values.
An unverifiable audit correlation cannot make an owner-act record effective.

The proposed outage behavior is a design choice, not an atomicity claim in
RFC5-25: before a new spending, content-release, generation/adoption or artifact
write effect, the recorder must durably accept its identified admission/attempt
record. If it cannot, refuse that new effect with audit availability explicitly
unresolved. Do not claim the failed audit write was recorded.

Audit outage does not delay an authenticated, authorized local run stop,
cancellation of an existing attempt through its permitted control route, or denial
of further use of the identity/permission named by a valid revocation request.
These specific stop controls still require current caller authority; the exception
permits no new generation, export, content release, artifact reversal/deletion or
permission grant. Local cancellation retains its ordering against dispatch and
write commitment; remote cancellation is only attempted where permitted and its
outcome is never presumed.

Apply the protective hold immediately and retain permitted pending-event metadata
through the trusted recorder/recovery boundary. If required durable audit or
owner-act correlation cannot be established, show enforcement held with formal
revocation/audit pending, not a successfully verified revocation or an invented
fallback authority state. The hold cannot silently clear on service recovery;
resolve it through the governing revocation/grant mechanism with trustworthy
records. Missing pending-event durability stays Unknown and cannot be reconstructed
as trusted ceremony evidence from a mutable work file. Once revocation is validly
recorded, its ordinary withdrawal-label and forced-evaluation rules apply. A pending attempt proves only admission/intent to attempt, not
provider transmission, run success or a completed write.

After the effect, append the actual outcome linked to that identity. A lost
outcome acknowledgment does not prove no effect and never permits blind replay.
Recover from authoritative receipts under current permission and append the
missing outcome idempotently; unavailable evidence stays uncertain. Existing
protected records remain immutable. This protocol does not promise a transaction
spanning the audit store and an external provider or rollback of an incurred
effect. Audit-dependent confirmation remains unmet while required evidence is
missing. Exact durable recorder/transport behavior needs implementation testing.

## Existing-host integration evidence

[Observed] In this worktree, the POC browser-origin helper checks host/origin, and
the credential helper persists a presentable token used for comparison. Those
inspected behaviors alone do not establish session/anti-forgery admission,
per-client scopes and rotation, verifier-only server storage or protected audit.
Relevant source: `apps/three-surface-poc/src/browser-origin.ts` and
`packages/cap1-daemon/src/credentials.ts`. No credential store was read.

Reuse the existing host mechanisms where their contracts and behavior match;
repair or extend the remaining integration explicitly. Required changes to
existing capability behavior must appear in the overlap/impact review before
sign-off. This document does not treat current route labels or passing read-only
admission tests as proof for the new mutating operations.

## Proposed implementation binding

EFFECT-HOST-DESIGN.md specifies the local origin/process isolation, protected
recorder principals and append/query/recovery interfaces for this candidate.
It also names the excluded-actor and restart/outage tests. Its deployment must
prove those boundaries before real effects; ordinary same-user files or test
adapters cannot stand in for the protected recorder.
