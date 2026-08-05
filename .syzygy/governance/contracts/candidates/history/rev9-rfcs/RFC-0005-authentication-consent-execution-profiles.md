# RFC 0005 — Authentication, Consent and Execution Profiles

**Status:** Proposed foundational contract. This line is a self-declaration at authoring time (RFC3-16): effective status is established solely by the owner-act record binding this file's exact content digest, and acceptance edits nothing here. Absent such a record, this contract binds nothing.
**Date:** 2026-07-30 (amended through 2026-08-02)
**Serves:** SEC-1, SEC-2, SEC-3, SEC-4, SEC-5; VIS-4 (always-human classes), VIS-5 (adapter authorization), VIS-7/trust floor (no secret in any surface); v1.md platform posture; SDR §5 q8 (owned here: machine-client authentication mechanism; execution profiles). Grounded in FD-009 (LAN posture), FD-018 as amended by FD-029 (A6-b execution profiles), OQ-007.

---

## 0. Reader's summary (non-normative)

*Plain-language orientation. If this section and a clause ever disagree, the
clause wins.*

- This RFC is the **security boundary**: who may talk to Syzygy, what may
  leave it, what may run inside it, and how every such act is recorded and
  revoked. **Default is deny everywhere**; every exception is a recorded
  owner act.
- **Being local proves nothing.** A request is classified by the credential
  it presents, never by network location — even on loopback, browsers need a
  session (with CSRF and DNS-rebinding defenses) and tools need an explicit
  machine credential. A fresh install serves loopback only.
- Sessions are the credential and nothing else (no device binding — decision
  B9), so **session lifetime and instant revocation are binding
  obligations**, the entire mitigation for a stolen session.
- **Consent comes in four separately revocable classes** per record:
  observe, write, egress (per provider, per content class), execute.
  Revoking one never silently revokes or preserves another.
- **Nothing leaves the machine without egress consent.** All outbound
  content passes one choke point that checks provider, content class, and —
  crucially — that the consent record itself has verifiable owner
  provenance (RFC3-16(a)). Content whose class can't be determined fails
  closed. Revocation takes effect at the next act, immediately, and forces
  a re-evaluation (decision B4).
- **Secrets are screened at every ingest boundary**, fail-closed: what can't
  be classified is excluded, and exclusions are recorded by hash, never by
  content.
- **No observed-project code runs without an execution profile**: a
  versioned, owner-approved artifact declaring isolation class, filesystem
  scope, injected credentials (never ambient, never any credential that
  authenticates to Syzygy itself), default-deny network, resource limits,
  and destructive-op gates. This applies to the owner's own repos too. A run
  that violates its profile terminates and its outputs cap at `report-fact`.
- Every authenticated act emits an **audit record** — the trail the
  owner-act provenance mechanism (A1) will correlate against.

Structure: §3 is the contract (RFC5-1 … RFC5-26); §4 violation cases; §8
owner questions, answered ones marked in place.

---

## 1. Summary

Syzygy's boundary contract: who may talk to it, what may leave it, what
may run inside it, and how every such act is recorded and revoked. It
defines the two client classes and their admission disciplines (browser
origin/CSRF including on loopback; explicit machine-client credentials),
the closed exposure-mode set (loopback; an owner-controlled overlay network
with device identity and TLS; owner-configured TLS LAN), the consent-class
taxonomy carried by RFC
0001's Consent record entity (observation, write, egress, execution),
egress consent for model providers over a closed content-class vocabulary,
fail-closed secret screening at every ingest boundary, and — the SEC-3
unblock this RFC exists to provide — the **execution profile**: a
declared, versioned, owner-approved artifact under which, and only under
which, observed-project code may ever run. It is **contract shape only**:
mechanism *classes* are enumerated (token, mutual TLS, signed request,
OS-mediated peer identity; process/namespace/VM isolation), no product or
stack is chosen; the one enumerated choice left open for acceptance is the
machine-client mechanism (§8 q1). This RFC is **blocking**: no
observed-project code executes until it is accepted and a per-project
profile exists (SEC-3).

---

## 2. Motivation and doctrine grounding

Syzygy indexes a whole portfolio, listens on a network, executes
observed-project code, sends derived content to model providers, and
writes into repositories it governs [Observed: security.md preamble].
Doctrine fixes SEC-1…5 and routes the contracts here: "the mechanism is
authentication-RFC material" (SEC-1); "the profile contract is RFC
material and blocking" (SEC-3). RFC 0002 already depends on this RFC for
the consent semantics behind Unknown reason #6 and for "execution profiles
gating fresh verification evidence" [Observed: RFC 0002, Integration].

[Inferred] The failure mode this contract guards against is the
**convenience default**: the loopback endpoint answering any local
process, the model call that ships a repository "because the feature
needed it," the test runner inheriting the host's SSH agent. Every clause
below states the default as deny and makes the exception a recorded owner
act — a permissive configuration is always an artifact, never an accident.

Owner history, preserved: FD-018 ruled "trust assumed" for the owner's own
projects; FD-029 amended it to A6-b (opt-in profiles: isolated
credentials, declared network, resource limits, destructive-op gates), and
adopted SEC-3 now binds observed code as untrusted **regardless of who
owns the project**. This RFC follows the adopted rule, not the superseded
ruling (§6.4).

---

## 3. The contract

Clauses are numbered `RFC5-n` for stable citation. Amend in place; retire
rather than renumber. Parentheticals beginning
*History:* are amendment records — when and why text changed — and carry
no normative force; the clause text around them is the contract.

### 3.1 Principals and the single-owner pre-commitment

**RFC5-1.** Every authenticated act binds to exactly one **principal**. The
V0/V1 principal classes are closed: the **owner** (the single human of
doctrine's glossary), **machine clients** (agent and CLI processes acting
on the owner's behalf under their own credentials, never the owner's), and
**Syzygy itself** (attribution of its writes and adapter effects, SEC-4).
Multi-user operation is deferred [Observed: v1.md deferral table]; to
avoid painting into a corner, the contract pre-commits to three properties
that make later principals additive rather than structural: (a)
authorization is evaluated against a principal's **scopes**, never against
the assumption that exactly one human exists; (b) every audit record,
consent record, and approval Decision names its principal explicitly,
never implying "the owner"; (c) admission ("authenticated") and permission
("authorized") are separate tests everywhere. What multi-user would add
(roles, delegation, per-principal consent authority) is deliberately
absent, not implicitly present.

**RFC5-2.** Sessions and credentials are distinct. A **session** is a
bounded, revocable admission of a browser principal, established through an
owner-attended act (§3.2). A **machine credential** is a durable, scoped,
revocable admission of a machine client (§3.3). Neither is transferable
across client classes: a session cookie never admits a machine client; a
machine credential presented by a browser page does not create a session.

### 3.2 Client classes: browser discipline

**RFC5-3.** Every request is classified as exactly one of two client
classes, **by credential presented, never by network location or header
heuristics**: a request bearing a valid machine credential is a machine
client; every other request is browser-class. Loopback location alone never
proves client identity (SEC-1), and an absent browser `Origin` header is
neither automatically trusted nor treated as a browser-origin violation
(SEC-1): absence of a header classifies nothing — the request simply must
satisfy its class's full discipline.

**RFC5-4.** Browser-class discipline, **including on loopback**:

- **Session requirement.** State-changing and data-bearing endpoints
  require an established session; the session is minted only through an
  owner-attended act on a trusted channel (first-run pairing on the serving
  host, or an authenticated login under §3.4's non-loopback modes).
- **Session identity is the credential and nothing else** *(ruled at
  acceptance by owner decision B9, answering §8 q2).* A session is **not**
  bound to a device, a device identity, or any network-layer property. This
  is the strictest reading of SEC-1's "by credential presented, never by
  network location", and it declines the overlay-network device-identity
  exception §8 q2 offered rather than taking it.
- **Lifetime and revocation are therefore binding obligations, not
  defaults.** [Inferred — this consequence follows from the ruling and is
  stated because leaving it implicit would make the ruling less safe than
  the alternative it beat.] With no device binding, a session credential
  that escapes the owner's control is a **complete session anywhere**, and
  the only two mitigations remaining in the contract are how long it stays
  valid and how fast it can be killed. Accordingly: every session carries a
  **declared maximum lifetime** after which it is invalid without
  re-authentication (value is quality-policy material; an **undeclared
  lifetime means sessions do not persist beyond the process**, never an
  unbounded default); and **immediate, owner-initiated revocation of any or
  all sessions is a required capability**, effective at the next request
  rather than at the next evaluation, since it is an admission control and
  not a claim. An implementation offering no revocation path does not
  conform.
- **Anti-CSRF proof.** Every state-changing request carries a per-session
  anti-forgery proof (token or equivalent) that a foreign origin cannot
  read. When an `Origin` or `Sec-Fetch-Site` header is present it is
  validated against the mode's allowlist; when absent, the anti-forgery
  proof alone decides — per RFC5-3, absence neither admits nor condemns.
- **DNS-rebinding defense.** The `Host` header of every browser-class
  request is validated against the closed hostname set declared by the
  active exposure mode (§3.5); a request for an undeclared host is refused
  before any application logic runs. A browser-originated `localhost` fetch
  from an arbitrary web page must fail both this check's cousin (origin
  validation) and the anti-forgery proof — the SEC-1 violation example ("a
  loopback endpoint answering an arbitrary web page's fetch") must be
  structurally impossible, not merely discouraged.

**RFC5-5.** Machine clients are admitted **only** through an explicit
machine-client authentication mechanism (SEC-1). There is no anonymous
machine access on any interface, loopback included; a request with neither
session nor machine credential may reach only the endpoints an
unauthenticated visitor may see, and that set is closed: liveness/health
and the authentication bootstrap itself, none of which expose portfolio
data.

### 3.3 Machine-client credentials: the contract shape

**RFC5-6.** A machine credential's contract shape, binding whatever
mechanism is chosen:

- **Identity.** Each credential names one machine-client identity (e.g.
  "beads-adapter on host X", "owner CLI"), minted at issuance, opaque and
  never reused. Identity survives rotation; revocation is per-identity or
  per-credential-instance.
- **Issuance.** Only through an owner-attended ceremony on an
  already-trusted channel (an authenticated session, or the serving host's
  own console). Credentials are never self-issued, never minted by another
  machine credential, and never distributed through an observed project's
  content.
- **Scoping — deny by default.** A credential carries an explicit scope
  set: which projects it may read, whether it may submit proposals, trigger
  evaluations, or reach adapter-mediated effects. An unscoped credential is
  invalid, not all-powerful. Scope enumeration granularity is RFC 0003/0006
  schema material; the deny-by-default rule is this clause's.
- **Rotation.** Supported without identity change; the old instance is
  retired with an overlap window the owner declares (which may be zero).
- **Revocation.** Effective at the next request (§3.6, acts rule); recorded.
- **Storage.** Syzygy stores only a verifier (hash or public key), never
  the presentable secret; the credential record (identity, scopes,
  issuance, expiry, revocation state) is a governance-plane artifact and
  contains no secret material (SEC-5).

**RFC5-7.** The concrete mechanism is an **enumerated choice for
acceptance** (§8 q1), each satisfying RFC5-6: (a) per-client bearer tokens
over TLS (or loopback), random, hashed at rest; (b) mutual TLS with
per-client certificates; (c) per-client keypairs with signed requests;
(d) an OS-mediated local channel with kernel-verified peer identity (e.g. a
Unix domain socket with peer credentials) — which is *not* "loopback
location as identity": the kernel attests the peer process's identity, a
TCP source address attests nothing. More than one mechanism may be enabled
concurrently (e.g. (d) locally, (a) over the tailnet).

### 3.4 Exposure modes

**RFC5-8.** The exposure-mode set is **closed**: **loopback**;
**owner-controlled overlay network with device identity and TLS**
(the "tailnet" mode — *e.g. Tailscale Serve, named parenthetically only
because doctrine's decision record names it, OQ-007/FD-029; the class term
is the normative noun and no product is chosen here, per §1*); and
**owner-configured TLS LAN** (FD-009). Each non-loopback mode requires
authenticated, TLS-protected access limited to the owner's own devices
(SEC-1). Enabling any non-loopback mode is an explicit, recorded owner act
naming the mode and its hostname set; an unauthenticated network-exposed
configuration is not a weaker mode — it is an invalid configuration, and
Syzygy **refuses to serve** rather than serve it (fail closed).

**RFC5-9.** Per-mode obligations:

| Mode | Transport | Device restriction | Syzygy-layer auth |
|---|---|---|---|
| Loopback | Cleartext permitted on the loopback interface only | The serving host | **Full** RFC5-4/5 discipline — loopback never proves identity |
| Overlay network (tailnet) | TLS terminated by the overlay | The owner's overlay devices; network-layer device identity **may satisfy the device-restriction requirement, never the client-classification requirement** — sessions and machine credentials still apply | Full |
| TLS LAN | TLS with owner-provisioned certificates | Owner-declared; no overlay identity exists, so Syzygy-layer auth is the only identity | Full |

**RFC5-10.** A fresh install serves loopback only. Portfolio data is never
served on a non-loopback interface absent the RFC5-8 owner act — the SEC-1
violation ("a fresh install serving portfolio data on a LAN address with no
credential") is a configuration Syzygy must be unable to reach.

### 3.5 Acts versus claims: the temporal rule at the boundary

**RFC5-11.** RFC 0002's temporal machinery (identified evaluations, as-of
instants, degradation-only) governs **truth claims**. Boundary enforcement
— admitting a request, permitting an egress, launching a run — is an
**act**, judged at the instant it is attempted against the then-current
credential, consent, and profile state. Revocation therefore takes effect
at the next act, immediately, without waiting for a new evaluation; the
*recomputation* of revocation's consequences on claims (Unknown reasons,
degraded values) flows through RFC 0002's evaluations. [Inferred —
without this clause, RFC2-4 read literally would delay revocation until
someone triggers an evaluation, which no security rule could tolerate.]

**The rendering obligation** (RFC5-11, amended in place) *— post-draft
amendment under review 3's AS-R6.* Recording a revocation **immediately obliges every subsequent
served render of a dependent claim to carry the withdrawal label** (RFC2-23,
"Consent withdrawn"), before and independent of the next evaluation. The
obligation attaches at the revocation record, not at the evaluation that
processes it. The underlying claim is **not** recomputed outside an
evaluation: RFC 0002's evaluation identity and degradation-only rule
(RFC2-4) are preserved untouched, and no claim changes value as a side
effect of a security act. What changes is that the surface may no longer
present withdrawn-source content **unlabelled**.

**Revocation forces an evaluation** *(strengthened at acceptance by owner
decision B4, taking the stronger form §8 q6 offered).* Recording a revocation
**triggers a new identified evaluation** rather than waiting for the next
human-triggered one. The residual window therefore exists but is not
open-ended: it lasts as long as the forced evaluation takes, not as long as it
takes someone to run one.

**This does not weaken RFC2-4, and the distinction matters.** A security act
still changes no claim's value directly; it **schedules an evaluation**, and
the value changes inside that evaluation over a new snapshot that carries the
revocation record as an authoritative input — exactly the permitted improvement
route RFC2-4 names. What the draft got right is preserved: nothing is
recomputed outside an evaluation. What it left open was the *duration* of the
inconsistency, and the answer "until someone happens to evaluate" is the state
that teaches a reader to distrust the surface — a claim sitting green under a
withdrawal label for an unbounded time is worse than either honest end state.

**The residual is still explicit.** Between the revocation and the completion
of the forced evaluation, a dependent claim's *value* is the pre-revocation one
and it renders **with the withdrawal visible**, never as current. [Inferred —
the forced trigger is the owner's decision; its reconciliation with RFC2-4 is
this RFC's, and is the reason the trigger is lawful rather than a carve-out.]

### 3.6 Consent classes and consent records

**RFC5-12.** RFC 0001's **Consent record** entity (RFC1-3) carries a closed
set of **consent classes**; one record instance grants exactly one class
(so each is individually revocable and individually renderable):

- **Observation consent** — per repository: Syzygy may read and index it
  (RFC1-3; architecture.md onboarding). Absent: no observation, Unknown —
  never an empty graph read as absence.
- **Write consent** — per repository: Syzygy may write its two namespaces
  and reach declared adapter effects (SEC-4). Absent: read-only.
- **Egress consent** — **one record per *(Project, provider)* pair, naming
  the set of permitted content classes** (§3.7; SEC-2's own wording;
  RFC3-7). Not one record per content class. *(History: post-draft amendment under
  review 3's AS-R10, aligning this bullet to RFC5-14's model and keeping
  RFC3-7's record shape single. The granularity question was **answered at
  acceptance by owner decision B8** — one record per (project, provider);
  the per-repository alternative was declined — see RFC 0003 §8 q3.)*
- **Execution consent** — per project: the owner's approval Decision for a
  specific execution-profile version (§3.9). Absent: no observed code runs.

Every consent record names its class, subject, scope, granting principal,
grant instant, and revocation state. Representation (`project.yaml`,
governance-plane schema) is RFC 0003 material.

**RFC5-13.** Consent revocation is prospective: it stops future acts
(RFC5-11) and renders dependent claims Unknown
(`unconsented-source-or-provider`, RFC2-24 #6) at the next evaluation —
**while every render served in the interim already carries the withdrawal
label under RFC5-11's rendering obligation**, so the interval before that
evaluation never presents withdrawn-source content as current.
Immutable artifacts produced under then-valid consent — observation
records, inference overlays, execution records — remain, rendered with the
withdrawal visible (RFC2-23); revocation never rewrites history. A revoked
provider's overlays are never recomputed and admit no **new** challenges;
**challenges already admitted are unaffected by the revocation and leave the
lifecycle only by an RFC2-13 resolution act** — that rule is RFC2-13's, where
the challenge lifecycle is defined, and this clause cites it rather than
setting it. What is this clause's is the revocation side: no recomputation, no
new admissions, and no un-suspension as a side effect of the consent record
changing.

### 3.7 Egress consent and model providers

**RFC5-14.** Governed-project content leaves owner-controlled
infrastructure only under a recorded egress-consent record naming the
**provider** and the permitted **content classes** (SEC-2). Model providers
are such providers. The content-class vocabulary is closed at this RFC
(amend to extend):

| Class | Contents |
|---|---|
| `governance-text` | Doctrine, spec, decision, policy text |
| `code-structure` | Identifiers, paths, symbols, structural graph — no bodies |
| `code-content` | Source and test bodies |
| `work-history` | Work items, run summaries, telemetry, cost data |
| `evidence-content` | Evidence artifact contents (reports, logs) |
| `derived-composites` | Prompts, summaries, embeddings composed from the above |

A composite (a prompt, a summary) inherits the **highest** class of any
content it embeds; `derived-composites` consent alone never launders an
unconsented class into an egress. The vocabulary is closed here, but the
**declared policy that classifies concrete content into it** is a governance
artifact, and it is honored **only under RFC3-16(a)** — a policy an untrusted
writer could mint would classify `code-content` as `code-structure` and pass
RFC5-15's check on a consent record that is genuinely in force, defeating the
choke point without forging a consent record at all. RFC5-15 accordingly
verifies both provenances, not one. Providers not named require fresh
consent; absent consent the inferred layer **is not computed** and renders
Unknown (RFC2-7). The active consents are rendered on the project's surface
(SEC-2).

**Classification is determinable, provenance-tracked, and fails closed**
*(post-draft amendment under review 3's AS-R5, giving egress the secret
rule's spine — RFC5-16/17).* Content class is a **property of what enters
the choke point, tracked from where the content originated**, not an
attribute the composing step asserts about its own output: composition
**carries embedded classes forward**, so a composite's class is computed
from the classes of what it embeds and remains attributable to them. A
composite whose class **cannot be determined fails closed** — the egress is
**refused and the refusal rendered** — exactly as content that cannot be
classified is excluded rather than indexed (RFC5-16). The
**classification-policy version is a snapshot input** (RFC2-1 item 7), so
what class was asserted, under which policy, is auditable at every
evaluation. [Inferred] Without the undeterminable case the highest-embedded-
class rule has no floor: a step that concatenates identifiers
(`code-structure`, consented) with an inlined function body
(`code-content`, not consented) and cannot say which it produced would
default to whatever it claimed, and SEC-2's per-content-class scoping would
be defeated with every RFC5-15 field nominally satisfied.

**RFC5-15.** Egress enforcement sits at a **single choke point**: every
network transmission of governed-project content passes one consent check
naming (provider, content classes, project) and emits an audit record
(§3.11). The check has three parts, all of which must pass: the consent
record is **in force**; the content's class is **determinable and within
the consented set** under a classification policy whose own owner-act
provenance verifies (RFC5-14 — undeterminable fails closed, and so does
unverifiable, since a forged classification passes this part while telling
the truth about the consent record); and the
consent record's **owner-act provenance is verifiable under RFC3-16(a)** —
a consent record present in the governed tree without it does not authorize
an egress, blocks the transmission, and mints a contradiction, because the
tree the consent lives in is writable by fleet workers — SEC-3's untrusted
actor class, extended to committed artifacts by the premise RFC3-16(a)
states.
A feature that transmits as a side effect without traversing the choke
point is the SEC-2 violation, whatever its intent. Remote backing
dependencies (a remote database, FD-009) are permitted under the same
consent rule — a backing store the owner does not control is a provider.

### 3.8 Secret handling at ingest boundaries

**RFC5-16.** The declared secret-detection policy (SEC-5,
`.syzygy/governance/policies/`) is applied at **every ingest boundary** —
*before* content enters any Syzygy store, surface, or endpoint. The
enumeration that follows is **illustrative of every ingest boundary, not
exhaustive**: observation capture; evidence intake; adapter reads —
**including a cross-project read of an observed source's entire tree
(RFC3-30)**; **workspace-manifest import** (RFC3-11); execution-run output
capture (§3.9); and telemetry. A path not on this list is not thereby
exempt; if content crosses into a Syzygy store, it crossed an ingest
boundary. **The governing policy is the observing project's own** (RFC3-30):
Project A screens what it ingests from observed source B under **A's**
policy, never B's — content read from B's governance plane is data, never
governing policy for A. Screening is fail-closed: content matching the
policy is excluded; content that **cannot be classified is excluded, not
indexed**. The policy version is a snapshot input (RFC2-1 item 7), so what
was screened is part of every evaluation's identity — and the policy is
honored **only under RFC3-16(a)**: it is an owner-approved declaration whose
effect is to widen what Syzygy may take in, so a permissive version an
untrusted writer could mint would admit at every ingest boundary exactly the
content SEC-5 requires excluded, and the exclusion counts would render honest
about a screen that never screened. An unverifiable policy does not fail
open: the ingest is blocked on RFC3-16(a)'s effect rule, never performed
under the unverified policy. *(Enumeration scope and the observer-policy
rule: post-draft amendments under review 3's AS-R14 and AS-R7.)*

**RFC5-17.** Exclusions carry **hash-not-body provenance**: an excluded
item is recorded as (content digest, location reference, policy version,
redaction class) — never the content itself, in any store including the
audit trail. Redaction classes are closed: `excluded-artifact` (whole
artifact withheld), `redacted-span` (artifact retained, matching spans
replaced by markers with a count), `unclassifiable-excluded` (fail-closed
default). Exclusions render with counts (RFC2-23 "Excluded content").

**The classes map to Unknown differently** *(post-draft amendment under
review 3's AS-R12; a scoping fix, **not** a vocabulary extension — no new
Unknown reason is added, and RFC2-24's closure is untouched)*:

- `excluded-artifact` and `unclassifiable-excluded` withhold the artifact
  entirely, so **every claim that depended on it renders Unknown**
  (`excluded-content`, RFC2-24 #7) with the exclusion count shown.
- `redacted-span` **retains** the artifact with counted markers. A claim
  over the **surviving content** may still stand, **at the tier it
  otherwise earned**, with the redaction count disclosed on the claim; only
  a claim that **depends on a redacted span** renders Unknown
  (`excluded-content`). Mapping the whole artifact to a blanket Unknown
  would over-degrade usable partial evidence, which VIS-1 no more permits
  than over-claiming does.

A secret reproduced in any surface,
store, or endpoint is a trust-floor violation regardless of this clause's
observance elsewhere (trust-and-evidence.md floor bullet 4).

### 3.9 Execution profiles — the SEC-3 unblock

**RFC5-18.** **The gate.** Observed-project code executes only when all of:
(a) this RFC is accepted; (b) an **execution profile** for the project
exists as a declared, versioned artifact in the governed plane; (c) the
owner has approved that exact profile version by a recorded Decision (the
execution-consent record, RFC5-12) **whose owner-act provenance the gate
cross-checks under RFC3-16(a) before launching** — an approval Decision
present in the governed tree without verifiable provenance does not
approve anything, blocks the launch, and mints a contradiction, since the
plane the Decision lives in is writable by the untrusted actor class
(SEC-3); (d) the launching principal is
authenticated and authorized; (e) the run is captured as an Execution
record citing the profile identity and version (SDR-8). Absent any of
these, the run does not launch, and claims needing the evidence it would
have produced render Unknown with the **primary** reason
**`execution-blocked`** (RFC2-24 #12), routed to its resolving action —
unblock or authorize the run — and expandable to which of (a)…(e) failed.

*(History: amended at acceptance by owner decision A5, answering this RFC's §8 q3 and
RFC 0002 §8 q1 together.)* The draft rendered this as `missing-evidence` with
the blocked execution disclosed as a bare fact of the render, on the reasoning
that RFC2-24's secondary-annotation vocabulary is closed to the primary list
and blocked execution was not in it. That reasoning was sound and its
conclusion was the wrong half of the fork: because the secondary vocabulary
**is** the primary list, there was no lawful value to annotate with, so the
honest fix was to amend the list rather than to route around it — which is what
RFC2-24's own text directs ("the honest move is to amend this list, never to
annotate outside it"). `missing-evidence` also misdescribed the remedy: it
sends a reader to capture evidence when the capture path itself is what is
blocked.

**RFC5-19.** **The trust distinction** (FD-018 as amended by FD-029).
Syzygy's own body — its services, kernel, adapters — runs trusted; its
integrity is release-gated by the trust floor (VIS-7), not by profiles.
**Observed-project code is untrusted everywhere, regardless of who owns the
project** (SEC-3): the owner's own repositories get no ambient-trust
carve-out. An owner may approve a *permissive* profile for a trusted
project — that is the recorded, revocable form the old "trust assumed"
posture takes; RFC5-21's floor still binds it. Consuming evidence produced
**outside Syzygy** (the project's own CI artifacts, a worker's retained
gate artifact) is observation, not execution — no profile is required to
read a report; profiles govern only code Syzygy itself launches.

**This boundary governs whether a profile is required; it confers no tier**
*(clarified post-draft under review 3's AS-R3).* That Syzygy may read an
artifact without a profile says nothing about what the artifact may
support: the evidence tier is set by RFC4-13's provenance predicate, under
which an artifact of unverifiable origin caps at `report-fact` however
retained, well-formed, and revision-bound it is. Reading is free; being
believed is not. [Inferred] Read the other way, this clause would let the
profile floor be sidestepped entirely — untrusted code writes a report to
disk, Syzygy reads it as "observation", and the artifact enters at the one
tier that can turn an indicator green without ever passing the containment
that exists for exactly that actor.

**RFC5-20.** **Profile contents.** An execution profile declares, at
minimum:

- **Isolation mechanism class** — one of the closed classes of RFC5-21;
- **Filesystem scope** — the readable set (project working tree, declared
  inputs) and writable set (a scratch area, declared outputs); nothing
  else is visible;
- **Credential scope — deny by default.** The host environment is
  stripped; **no ambient credential is ever inherited** (SEC-3's named
  violation). Each injected credential is enumerated by reference to a
  secret source and a stated purpose; the profile stores references,
  never secret material (SEC-5). **No credential that authenticates to
  Syzygy itself may be injected** — see RFC5-24;
- **Network policy** — default-deny egress, with the allowed set declared
  from a closed grammar: `none`, `loopback-only`, or an enumerated
  destination list (named hosts/services, no wildcards). **Every declared
  policy excludes Syzygy's own listening interfaces**: `loopback-only` does
  not reach Syzygy's loopback endpoints, and an enumerated destination list
  **may not name them** — a profile that does is invalid, not permissive.
  [Inferred] Syzygy serves under full discipline on loopback (RFC5-9), so
  without this exclusion `loopback-only` would read as a route to Syzygy's
  own control plane *(post-draft amendment under review 3's AS-R2)*;
- **Resource limits** — bounds on CPU time, memory, disk, wall clock, and
  process count; exceeding any bound terminates the run, recorded;
- **Destructive-operation gates** — per RFC5-22.

**RFC5-21.** **Isolation mechanism classes**, closed and stack-neutral —
each names a *class of guarantee*, not a product: **process-sandbox**
(OS-enforced restricted user, filesystem and syscall confinement),
**namespace/container isolation**, **VM/microVM isolation**. Every class
must certify the same floor: no ambient credential access, **no channel to
Syzygy's own control plane** (RFC5-20's network-policy exclusion, enforced
by the isolation mechanism and not merely declared), filesystem confinement
to the declared scope, enforced network policy, enforced resource limits,
and a kill switch that terminates the run and its descendants. There is
**no "none" class**: a profile that cannot certify the floor is not a
permissive profile, it is an invalid one. A run that
violates its declared policy terminates; the violation is recorded on its
Execution record (RFC4-19's policy-violation flags); and its outputs are
inadmissible as `gate-backed` evidence — at most `report-fact` (RFC2-25)
[Inferred — a gate artifact from a run that broke its own contract proves
nothing about the subject]. **The violation set** always includes: an
undeclared egress attempt; **any attempt to reach Syzygy's own control
plane** (RFC5-20); a write outside the declared scope; a resource bound
exceeded; and **consuming a credential beyond its stated purpose**
*(relocated here from RFC5-22's enable-able classes under review 3's
AS-R13: it contradicts RFC5-20's per-credential stated-purpose enumeration,
so it can never be a capability an owner standing-approves — out-of-purpose
credential use is a broken contract, not an enabled feature)*.

**RFC5-22.** **Destructive-operation gates.** Operations whose effects
outlast the sandbox form closed, default-blocked classes: pushing to
version-control remotes; publishing packages or artifacts to registries;
mutating external services, databases, or infrastructure; deleting or
rewriting data outside the declared scratch scope. *(**Consuming a
credential beyond its stated purpose** was listed here in the draft and has
been moved to RFC5-21's violation set under review 3's AS-R13 — it
terminates the run and caps its outputs at `report-fact`. It is not an
enable-able class at any approval level: RFC5-20 requires every injected
credential to carry a stated purpose, so "use it beyond that purpose" is
a contradiction of the profile's own declaration, not a capability.)*
A profile may enable a class only by naming it,
and every enabled class is either **per-run human-gated** (the owner
confirms each invocation) or **standing-approved** by the profile's
approval Decision — except that classes touching security posture, privacy
or retention obligations, or normative data contracts are **always
per-run human-gated**, mirroring VIS-4's always-human class; no profile
can standing-approve them.

**RFC5-23.** **Profile lifecycle.** A profile is versioned; any amendment
mints a new version requiring fresh owner approval — approval never
carries across versions silently. The profile identity and version are
snapshot inputs (RFC2-1 item 7): two evaluations consuming execution
evidence produced under different profile versions are distinguishable by
identity. Revoking execution consent (RFC5-13) blocks new runs at the next
act; running processes are terminated. Profiles are per-project; a
portfolio-wide profile template may exist as convenience, but each
project's approval Decision names its own concrete version — no project
executes under another project's consent.

### 3.10 Adapter credentials

**RFC5-24.** Credentials Syzygy itself holds to reach external authorities
through typed adapters (scheduler, version control, CI — VIS-5) are a
distinct credential population from both machine-client credentials (§3.3)
and execution-profile injections (§3.9). They are enumerated per adapter
and per authority, scoped to the adapter's authorized effect set, stored
under SEC-5 discipline (never in any indexed store or surface), and never
visible to observed-project code.

**The injection prohibition, stated at its proper width** *(post-draft
amendment under review 3's AS-R2; the draft forbade only adapter
credentials)*: **no execution profile may name as an injectable any
credential that authenticates to Syzygy itself.** That covers adapter
credentials **and machine-client credentials (§3.3) explicitly**, and any
future credential population admitted at Syzygy's own boundary. Rationale,
in one line: **SEC-3 classes observed code as untrusted everywhere, so it
may never hold an authenticated route to the authorized surface** — an
injected machine credential would satisfy RFC5-3's classification and
RFC5-5's no-anonymous-access rule *by itself*, turning the isolation floor
inside out into an escalation path. This binds together with RFC5-20's
network-policy exclusion and RFC5-21's floor: no credential to Syzygy, and
no route to Syzygy.

Every adapter effect is an authenticated act attributed to Syzygy and
audited (§3.11).

### 3.11 Audit and revocation

**RFC5-25.** **Every authenticated act is attributable.** Each admission,
denial, egress, run launch, adapter effect, consent grant or revocation,
credential issuance, rotation, or revocation emits an **audit record**:
principal, credential or session identity, act, subject, exposure mode,
instant, and outcome. Audit records are **Evidence artifacts** in RFC
0001's sense — durable, identified, integrity-verifiable, carrying source,
capture time, scope, and provenance — and are therefore citable by claims
and consumable by evaluations. They contain no secret material and no
excluded content bodies (RFC5-17): a rejected request's offending payload
is recorded by digest, never by value.

**Where the trail lives — a normative constraint, not a schema choice.**
*(History: bound here at the rev7 rework, review 9 finding F1, promoting the
derived constraint recorded at owner decision A1 from a §8 annotation to
clause text.)* The audit trail lives **outside `.syzygy/**` and outside
the untrusted actor class's write reach** (SEC-3 as extended at
RFC3-16(a)). This is load-bearing, not organizational: RFC3-16(a)'s class
of acceptable owner-act verification mechanisms includes correlation to a
Syzygy-mediated ceremony **recorded in this trail**, and RFC3-16(b) item 9
requires the binding to be verifiable against it — a trail placed in the
governed tree (including `governance/records/`, which the untrusted class
can write) would let any fleet worker forge the very correlation every
RFC3-16(a) gate rests on, defeating the predicate with no downstream check
able to notice. The trail's storage schema and medium remain
implementation-slice choices; its exclusion from the governed tree and
from untrusted write reach does not.

**RFC5-26.** Revocation semantics, uniformly: a revocation (credential,
session, consent, profile approval) is a recorded governance act, effective
at the next act per RFC5-11, never retroactive on immutable artifacts, and
always renderable — what was revoked, when, by whom, and what its
dependents now render as (Unknown reasons per RFC 0002). Nothing is ever
silently un-revoked: restoration is a fresh grant with a fresh record.

---

## 4. Violation cases

1. *(RFC5-3/4)* A loopback endpoint answering an arbitrary web page's
   fetch; a machine client admitted because it connected from 127.0.0.1; a
   request rejected *solely* for an absent `Origin` header.
2. *(RFC5-5/6)* An agent CLI reading portfolio data credential-less
   "because it's local"; a credential minted by another machine
   credential; a presentable token recoverable from any Syzygy store.
3. *(RFC5-8/10)* A fresh install reachable on a LAN address; serving an
   unauthenticated non-loopback configuration instead of refusing.
4. *(RFC5-11)* A revoked credential admitted "until the next evaluation."
5. *(RFC5-14/15)* Source sent to an unnamed model provider; `code-content`
   embedded in a prompt sent under `derived-composites` consent alone; an
   index synced to a third-party service as a feature side effect; a
   composite whose embedded class could not be determined egressing under
   the class its composer asserted; an egress honored on a consent record
   whose owner-act provenance was never verified (RFC3-16(a)).
6. *(RFC5-16/17)* Unclassifiable content indexed "pending review"; an
   excluded secret's body in the audit trail; a connection string in a map
   tooltip (SEC-5's named violation); Project A screening B's tree under
   B's secret-detection policy; a `redacted-span` artifact rendering its
   entire surviving content Unknown.
7. *(RFC5-18/19)* Observed-project code executing before acceptance, or
   under an unapproved profile version; the owner's own repository running
   unprofiled "because trust is assumed."
8. *(RFC5-20/21)* A profile inheriting the host environment "for
   convenience" (SEC-3's named violation); a "none" isolation class; a run
   that egressed to an undeclared host yielding `gate-backed` evidence.
9. *(RFC5-22)* Standing approval of remote pushes touching normative data
   contracts; a destructive op executed because its class was merely
   undeclared rather than enabled.
10. *(RFC5-24/25)* A profile injecting an adapter credential, **or a
    machine-client credential "so the harness can query the graph"**; a
    profile declaring `loopback-only` and thereby reaching Syzygy's own
    endpoints; an adapter effect with no audit record; an authenticated act
    whose principal cannot be recovered from the audit trail.
11. *(RFC5-11/13)* Consent is revoked and the dashboard keeps showing
    overlays and indexed content from the revoked source **unlabelled**
    until someone triggers the next pass.
12. *(RFC5-18(c))* An execution profile is approved by a Decision file a
    fleet worker committed, and the gate launches observed code on it.

---

## 5. Integration

**Relies on RFC 0001:** the Consent record entity (RFC1-3) this RFC's
class taxonomy specializes; the Decision entity as approval/revocation
warrant; Evidence-artifact semantics for audit and execution records
(SDR-8); Proposal/materialization machinery for how approved work reaches
execution.
**Relies on RFC 0002:** evaluation identity and snapshot inputs (profile
and policy versions, RFC2-1 item 7); Unknown reasons #6 and #7 and the
failure-state renderings (RFC2-23); the tier registry that caps
policy-violating runs at `report-fact` (RFC2-25).
**Provides to RFC 0002:** the consent-record semantics behind reason #6;
the execution gate behind fresh gate-backed verification evidence; the
acts-versus-claims rule (RFC5-11) its temporal machinery presupposes.
**Provides to RFC 0003:** the fields consent records, credential records,
profiles, and audit records must encode; RFC 0003 owns physical schema and
migration.
**Provides to RFC 0004:** the adapter-credential discipline (RFC5-24);
the ingest-boundary screening obligation on every adapter read (RFC5-16),
under the *observing* project's policy (RFC3-30); and the run-envelope
fields for profile identity/version (RFC5-18(e)) and policy-violation flags
(RFC5-21), which RFC4-19 now carries as named rows.
**Relies on RFC 0003:** RFC3-16(a), the owner-act provenance predicate that
this RFC's egress choke point (RFC5-15) and execution gate (RFC5-18(c))
cross-check — stated once there and cited, never restated here.
**Relies on RFC 0004:** RFC4-13's provenance predicate on `gate-backed`,
which sets what an externally produced artifact may support; RFC5-19's
observation/execution boundary governs only whether a profile is required.
**Provides to RFC 0006 and surfaces:** session semantics for URL/selection
state; the consent-rendering obligation (SEC-2) and exclusion counts.
**Not this RFC's:** secret-detection policy *content* (quality/policy
material); scope-enumeration granularity and wire formats (0003/0006);
concrete sandbox tooling choices (implementation under the accepted
class); multi-user roles (deferred).

---

## 6. Alternatives considered

- **6.1 Network-perimeter trust** (loopback or tailnet membership as
  identity). Rejected — SEC-1 forbids it explicitly; DNS rebinding and
  arbitrary local processes make "local" an attacker class, not a trust
  class. Tailnet identity is retained only for the device-restriction
  requirement (RFC5-9), never client classification.
- **6.2 One monolithic consent record per project.** Rejected — a single
  grant conflates observation, write, egress, and execution, so revoking
  one revokes all or (worse) none; per-class records keep each revocable
  and renderable independently. Cost: more records; accepted.
- **6.3 A "none" isolation class for trusted projects.** Rejected — SEC-3
  binds "regardless of who owns the project," and its named violation is
  precisely ambient-credential inheritance for convenience. The permissive-
  profile path (RFC5-19) preserves owner autonomy inside the floor.
- **6.4 Following FD-018 literally ("trust assumed" for own projects).**
  Rejected — FD-029 amended it and adopted doctrine supersedes the earlier
  ruling; the owner's actual trade-off is preserved as the recorded,
  revocable permissive profile, not as an ambient exemption.
- **6.5 Routing revocation through evaluations only.** Rejected — it would
  let a revoked credential act until someone triggers an evaluation.
  RFC5-11's acts/claims split keeps RFC 0002's determinism for truth while
  making enforcement immediate.
- **6.6 Choosing the machine-client mechanism now.** Declined — all four
  enumerated classes satisfy RFC5-6, the choice is reversible beneath the
  contract, and stack-neutrality is a bootstrap boundary; acceptance may
  fix one or admit several (§8 q1).
- **6.7 Act-timed re-render on revocation** — path (a) of review 3's AS-R6:
  making a recorded revocation itself force a degrade-to-Unknown *as an
  act*, immediately, outside any evaluation. **Rejected; path (b), the
  rendering obligation (RFC5-11), was taken instead.** Path (a) would let a
  security event change a claim's *value* outside an identified evaluation,
  which is precisely the coupling RFC5-11's act/claim split exists to
  prevent and which RFC2-4's degradation-only, per-snapshot fixed point
  forbids: truth would become a function of when a revocation happened to
  be recorded, and two runs of one evaluation could disagree (VIS-7). Path
  (b) obtains the security outcome — no withdrawn-source content is ever
  presented as current — by binding the *render*, which is not a truth
  computation. **Cost, deliberately taken and stated in RFC5-11:** a
  residual window exists in which the claim's value is still the
  pre-revocation one, labelled but not yet recomputed; it closes at the
  next evaluation, whose timing the human-triggered loop owns. Routed to
  acceptance as §8 q6 where the owner may take the stronger form.
- **6.8 Patching authorization authenticity per artifact class.** Declined
  in favor of citing RFC 0003's single predicate (RFC3-16(a)) from this
  RFC's gates. Restating the obligation locally at RFC5-12, RFC5-15 and
  RFC5-18 in different words would let the three drift, and would leave any
  artifact class added later unguarded — review 3's named risk 1. One
  predicate, one home, cited from every consuming gate.

---

## 7. Deliberately deferred

Concrete schemas for consent records, credential records, profiles, and
audit records → RFC 0003. Adapter read-screening mechanics and run-envelope
fields → RFC 0004. Session/URL semantics detail → RFC 0006. Secret-
detection policy content and audit-retention periods → quality/evidence
policy (craft). Multi-user principals, roles, delegation → post-V1, behind
the RFC5-1 pre-commitments. Execution-profile *templates* and a default
profile library → craft/product material once the contract is accepted.
Certificate interactions → post-V1 certificate RFC.

---

## 8. Open questions for acceptance

1. **Machine-client mechanism (SDR §5 q8).** Accept one of RFC5-7's
   classes as V0's mechanism — (a) hashed bearer tokens, (b) mutual TLS,
   (c) signed requests, (d) OS-mediated peer identity — or accept (d)
   for local plus (a) for tailnet as the proposed pairing?
2. **Overlay-network device identity for browser sessions — a deliberate
   trade, not a default.** RFC5-9 lets overlay ("tailnet") device identity
   satisfy the *device-restriction* requirement while still requiring a
   Syzygy session. The question is whether the **owner-attended pairing act
   may be waived on the overlay**, letting device identity bootstrap the
   session. **The trade, stated plainly:** waiving it means a
   **network-layer identity establishes a Syzygy session**, which softens
   RFC5-3's and SEC-1's "by credential presented, never by network
   location" — the very principle §3.2 is built on. It would be a
   controlled and recorded exception (owner-declared, revocable, on an
   owner-controlled overlay with device identity and TLS), not an
   unbounded one; but it is an exception to a doctrine rule, and doctrine
   rules are the owner's to except. Against that: waiving removes a
   per-device attended step the owner performs once, on a network the
   owner already controls. **This RFC proposes no resolution** — the
   author must not select it (review 3, AS-N4). Rule it either way at
   acceptance, and the ruling is recorded as the exception it is.

   > **ANSWERED at acceptance — B9.** The exception is **declined**. Session identity is the credential and nothing else — no device or network-layer binding. Consequence, now binding in RFC5-4: a declared maximum session lifetime (undeclared = no persistence beyond the process) and an immediate owner-initiated revocation capability are the **entire** remaining mitigation.
3. **Execution-blocked Unknown reason.**

   > **ANSWERED at acceptance — A5, together with RFC 0002 §8 q1: option B.**
   > RFC2-24 is amended with a **twelfth primary reason**,
   > `execution-blocked`, whose resolution route — unblock or authorize the
   > run — differs from "produce/capture evidence." RFC5-18 is amended to
   > render it. **Option A is superseded.**

   *The question as posed, retained so the trade is legible.* RFC2-24 states
   that the **secondary**-annotation vocabulary is closed and is the *same*
   list as the primary one, so a secondary "blocked execution" was never
   available. **Option A** (the drafted position): render blocked execution
   Unknown — `missing-evidence`, with the blocked execution disclosed as a
   named, expandable **fact of the render**. *Consequence:* the vocabulary
   stays small, but the resolution route a reader sees on the reason itself is
   "produce/capture evidence," which is the **wrong action** for this case —
   the right one is reachable only through the disclosed fact beside it.
   **Option B** (taken): amend RFC2-24 with a further **primary** reason.
   *Consequence:* the reason routes correctly and RFC6-14 carries a value that
   means what it says; the price is a twelfth reason, an amendment to a
   vocabulary deliberately kept small, and a reason whose condition is a
   *governance* block rather than an evidence state — which is also true of
   #3, #6 and #7, so the vocabulary already mixes both kinds.
4. **Destructive-op class closure.** RFC5-22's list is now **four**
   enable-able classes — out-of-purpose credential use moved to RFC5-21's
   violation set (review 3, AS-R13). Is that the right closure, or should
   filesystem deletion inside the declared writable scratch also gate
   (stricter, noisier)?
5. **Rotation overlap default.** RFC5-6 lets the owner declare an overlap
   window per rotation. Should the default be zero (strict) or a bounded
   nonzero grace (operationally kinder)? Proposed: zero.
6. **Revocation rendering versus re-evaluation (RFC5-11) — the residual
   window.** Review 3's AS-R6 found that revocation stopped *acts*
   immediately while dependent claims kept rendering as current until the
   next human-triggered evaluation. **The drafted fix binds the render**:
   from the revocation record onward, every served render of a dependent
   claim carries the withdrawal label, while the claim's *value* is
   recomputed only at the next evaluation (preserving RFC2-4 and the
   act/claim split — see §6.7 for why the act-timed re-render was
   rejected). **What the owner is accepting:** a window of unbounded
   duration in which a labelled claim still carries its pre-revocation
   value. **Stronger forms available:** (i) recording a revocation
   *triggers* an evaluation; (ii) the quality policy declares a **maximum
   interval between a revocation and the re-evaluation that clears it**,
   with the claim degrading to Unknown once exceeded. Both cost more than
   labelling; (ii) is the lighter of the two and composes with RFC4-16's
   declared-interval pattern. Accept the drafted form, or direct (i) or
   (ii)?

   > **ANSWERED at acceptance — B4.** The **stronger form** is taken: revocation forces a new identified evaluation rather than waiting for the next human-triggered one. RFC2-4 is unweakened — the security act *schedules* an evaluation, it does not mutate a claim.

---

*End of RFC 0005. Clauses RFC5-1 … RFC5-26. Lettered limbs cited inside
their parent clauses (e.g. RFC5-18(a)–(e)) are parts of those clauses —
list items within one clause body — not separate sub-clauses with their own
headings. The clause range is closed: amend in place, never renumber.*
