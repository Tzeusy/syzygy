---
id: RFC-0005
title: Execution Profiles — the SEC-3 unblock for running observed-project code
status_source: owner-act-record
module: execution-profiles
clauses: RFC5-18..RFC5-23 (no gaps, no retirements, no merges)
governs: [execution-profiles, execution-gate, isolation-classes, credential-injection, network-policy, resource-limits, destructive-operation-gates, profile-lifecycle]
applies_to: [kernel, machine-clients]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004]
tags: [sec-3, vis-4, vis-7, blocking, execution-blocked, no-none-class, fail-closed, rfc3-16a-gate]
---

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — as an owner-adopted bootstrap act until the
independent A1 correlation mechanism exists, and as a Syzygy-verified effective
act only after correlation (RFC3-16). Absent such a record, this contract binds
nothing.

**Package:** module 3 of 3 of the RFC 0005 contract package. Index, clause map,
lookup rule, package-spanning integration and the package question list:
`README.md`. Rationale, amendment history, alternatives, and answered §8
questions: `../../history/RFC-0005-history.md`.

**Serves:** SEC-3 (observed code untrusted regardless of project ownership),
VIS-4 (always-human classes), VIS-7/trust floor. Implements owner decision **A5**
(`execution-blocked` as a primary Unknown reason) and **FD-018 as amended by
FD-029** (A6-b execution profiles).

**This module is blocking.** No observed-project code executes until RFC 0005 is
accepted and a per-project profile exists (SEC-3). RFC 0002 depends on it for
execution profiles gating fresh verification evidence.

---

## 0. Module scope and reader map (non-normative)

*If this section and a clause disagree, the clause wins.*

This module owns **what may run inside Syzygy, under what containment, and what
happens when a run breaks its own contract**. Read it to answer: *may this code
launch, and what may its output be believed to prove?* It presupposes module 1
(the launching principal must be authenticated and authorized) and module 2
(execution consent is one of the four consent classes; run output capture is an
ingest boundary).

Four rules carry most of the weight:

- **The gate is five-part and absent any part the run does not launch**
  (RFC5-18), rendering Unknown with the primary reason `execution-blocked`,
  routed to *unblock or authorize the run* — never to "capture evidence."
- **Observed-project code is untrusted everywhere, regardless of who owns the
  project** (RFC5-19). The owner's own repositories get no ambient-trust
  carve-out; a permissive profile is the recorded, revocable form the old "trust
  assumed" posture takes.
- **There is no "none" isolation class** (RFC5-21). A profile that cannot certify
  the floor is not permissive, it is invalid; a run that violates its declared
  policy terminates and its outputs cap at `report-fact`.
- **No credential to Syzygy, and no route to Syzygy** (RFC5-20 with RFC5-24):
  the network policy excludes Syzygy's own listening interfaces, and no
  credential that authenticates to Syzygy may be injected.

One boundary is easy to misread and is stated explicitly at RFC5-19: reading an
externally produced artifact needs no profile, but reading it confers no tier —
RFC4-13's provenance predicate still caps an artifact of unverifiable origin at
`report-fact`.

---

## 3. The contract

Clauses are numbered `RFC5-n` for stable citation. Amend in place; retire rather
than renumber. A pointer *(history §RFC5-n)* means amendment narrative, prior
wording, or originating decision text was extracted at the rev10 compaction;
that material is non-normative and the clause text is the contract. Decision
identifiers named inline (A5, FD-018/FD-029) remain binding provenance here.

### 3.9 Execution profiles — the SEC-3 unblock

**RFC5-18.** **The gate.** Observed-project code executes only when all of: (a)
this RFC is accepted; (b) an **execution profile** for the project exists as a
declared, versioned artifact in the governed plane; (c) the owner has approved
that exact profile version by a recorded Decision (the execution-consent record,
RFC5-12) **whose owner-act provenance the gate cross-checks under RFC3-16(a)
before launching** — an approval Decision present in the governed tree without
verifiable provenance approves nothing, blocks the launch, and mints a
contradiction, since the plane the Decision lives in is writable by the untrusted
actor class (SEC-3); (d) the launching principal is authenticated and authorized;
(e) the run is captured as an Execution record citing the profile identity and
version (SDR-8). Absent any of these the run does not launch, and claims needing
the evidence it would have produced render Unknown with the **primary** reason
**`execution-blocked`** (RFC2-24 #12), routed to its resolving action — unblock
or authorize the run — and expandable to which of (a)…(e) failed. *(Amended at
acceptance by owner decision A5, answering this RFC's q3 and RFC 0002's
corresponding open question together; the superseded `missing-evidence`
rendering and the reasoning that replaced it are at history §q3.)*

**RFC5-19.** **The trust distinction** (FD-018 as amended by FD-029). Syzygy's
own body — services, kernel, adapters — runs trusted; its integrity is
release-gated by the trust floor (VIS-7), not by profiles. **Observed-project
code is untrusted everywhere, regardless of who owns the project** (SEC-3): the
owner's own repositories get no ambient-trust carve-out. An owner may approve a
*permissive* profile for a trusted project — the recorded, revocable form the old
"trust assumed" posture takes; RFC5-21's floor still binds it. Consuming evidence
produced **outside Syzygy** (the project's own CI artifacts, a worker's retained
gate artifact) is observation, not execution — no profile is required to read a
report; profiles govern only code Syzygy itself launches.

**This boundary governs whether a profile is required; it confers no tier.** That
Syzygy may read an artifact without a profile says nothing about what the
artifact may support: the evidence tier is set by RFC4-13's provenance predicate,
under which an artifact of unverifiable origin caps at `report-fact` however
retained, well-formed, and revision-bound it is. Reading is free; being believed
is not. [Inferred] Read the other way, the profile floor could be sidestepped
entirely: untrusted code writes a report to disk, Syzygy reads it as
"observation", and the artifact enters at the one tier that can turn an indicator
green without ever passing containment.

**RFC5-20.** **Profile contents.** An execution profile declares, at minimum:

- **Isolation mechanism class** — one of the closed classes of RFC5-21;
- **Filesystem scope** — the readable set (project working tree, declared inputs)
  and writable set (a scratch area, declared outputs); nothing else is visible;
- **Credential scope — deny by default.** The host environment is stripped; **no
  ambient credential is ever inherited** (SEC-3's named violation). Each injected
  credential is enumerated by reference to a secret source and a stated purpose;
  the profile stores references, never secret material (SEC-5). **No credential
  that authenticates to Syzygy itself may be injected** — see RFC5-24;
- **Network policy** — default-deny egress, the allowed set declared from a
  closed grammar: `none`, `loopback-only`, or an enumerated destination list
  (named hosts/services, no wildcards). **Every declared policy excludes Syzygy's
  own listening interfaces**: `loopback-only` does not reach Syzygy's loopback
  endpoints, and an enumerated destination list **may not name them** — a profile
  that does is invalid, not permissive. [Inferred] Syzygy serves under full
  discipline on loopback (RFC5-9), so without this exclusion `loopback-only`
  would read as a route to Syzygy's own control plane;
- **Resource limits** — bounds on CPU time, memory, disk, wall clock, and process
  count; exceeding any bound terminates the run, recorded;
- **Destructive-operation gates** — per RFC5-22.

**RFC5-21.** **Isolation mechanism classes**, closed and stack-neutral — each
names a *class of guarantee*, not a product: **process-sandbox** (OS-enforced
restricted user, filesystem and syscall confinement), **namespace/container
isolation**, **VM/microVM isolation**. Every class must certify the same floor:
no ambient credential access, **no channel to Syzygy's own control plane**
(RFC5-20's network-policy exclusion, enforced by the isolation mechanism and not
merely declared), filesystem confinement to the declared scope, enforced network
policy, enforced resource limits, and a kill switch terminating the run and its
descendants. There is **no "none" class**: a profile that cannot certify the
floor is not a permissive profile, it is an invalid one. A run that violates its
declared policy terminates; the violation is recorded on its Execution record
(RFC4-19's policy-violation flags); and its outputs are inadmissible as
`gate-backed` evidence — at most `report-fact` (RFC2-25) [Inferred — a gate
artifact from a run that broke its own contract proves nothing about the
subject]. **The violation set** always includes: an undeclared egress attempt;
**any attempt to reach Syzygy's own control plane** (RFC5-20); a write outside
the declared scope; a resource bound exceeded; and **consuming a credential
beyond its stated purpose** — a broken contract, never an enable-able capability,
since RFC5-20 requires every injected credential to carry a stated purpose
(history §RFC5-21).

**RFC5-22.** **Destructive-operation gates.** Operations whose effects outlast the
sandbox form closed, default-blocked classes: pushing to version-control remotes;
publishing packages or artifacts to registries; mutating external services,
databases, or infrastructure; deleting or rewriting data outside the declared
scratch scope. A profile may enable a class only by naming it, and every enabled
class is either **per-run human-gated** (the owner confirms each invocation) or
**standing-approved** by the profile's approval Decision — except that classes
touching security posture, privacy or retention obligations, or normative data
contracts are **always per-run human-gated**, mirroring VIS-4's always-human
class; no profile can standing-approve them.

**RFC5-23.** **Profile lifecycle.** A profile is versioned; any amendment mints a
new version requiring fresh owner approval — approval never carries across
versions silently. Profile identity and version are snapshot inputs (RFC2-1 item
7): two evaluations consuming execution evidence produced under different profile
versions are distinguishable by identity. Revoking execution consent (RFC5-13)
blocks new runs at the next act; running processes are terminated. Profiles are
per-project; a portfolio-wide template may exist as convenience, but each
project's approval Decision names its own concrete version — no project executes
under another project's consent.

---

## 4. Violation cases — this module

*Package numbering is stable; cases are distributed across modules, never
renumbered. Cases 1–4, 10 and 13 are in module 1, cases 5–6 in module 2, case 11
spans two modules and is held in `README.md`.*

7. *(RFC5-18/19)* Observed-project code executing before acceptance, or under an
   unapproved profile version; the owner's own repository running unprofiled
   "because trust is assumed."
8. *(RFC5-20/21)* A profile inheriting the host environment "for convenience"
   (SEC-3's named violation); a "none" isolation class; a run that egressed to an
   undeclared host yielding `gate-backed` evidence.
9. *(RFC5-22)* Standing approval of remote pushes touching normative data
   contracts; a destructive op executed because its class was merely undeclared
   rather than enabled.
12. *(RFC5-18(c))* An execution profile is approved by a Decision file a fleet
    worker committed, and the gate launches observed code on it.

---

## 5. Integration — this module

**Relies on RFC 0001:** the Decision entity as the approval warrant RFC5-18(c)
verifies; Evidence-artifact semantics for execution records (SDR-8).
**Relies on RFC 0002:** snapshot inputs (profile identity and version, RFC2-1
item 7); Unknown reason #12 `execution-blocked` (RFC2-24) and the failure-state
renderings (RFC2-23); the tier registry capping policy-violating runs at
`report-fact` (RFC2-25).
**Relies on RFC 0003:** RFC3-16(a), the owner-act provenance predicate the
execution gate (RFC5-18(c)) cross-checks — stated once there and cited, never
restated here.
**Relies on RFC 0004:** RFC4-13's provenance predicate on `gate-backed`, which
sets what an externally produced artifact may support; RFC5-19 governs only
whether a profile is required. RFC4-19 carries the policy-violation flags
RFC5-21 requires recorded.
**Relies on module 1:** RFC5-11 (revocation effective at the next act, which
RFC5-23 depends on); RFC5-24 (the injection prohibition RFC5-20 cites); RFC5-25
(the audit record every run launch emits).
**Relies on module 2:** RFC5-12 (execution consent is the approval Decision
RFC5-18(c) names); RFC5-13 (revoking execution consent); RFC5-16 (execution-run
output capture is an ingest boundary).
**Provides to RFC 0002:** the execution gate behind fresh gate-backed
verification evidence, and the condition under which `execution-blocked` renders.
**Provides to RFC 0003:** the fields execution profiles must encode; RFC 0003
owns physical schema and migration.
**Provides to RFC 0004:** the run-envelope fields for profile identity/version
(RFC5-18(e)) and policy-violation flags (RFC5-21), carried by RFC4-19 as named
rows.
**Provides to RFC 0010:** the execution gate (RFC5-18) any fleet-executed run
inside a bounded mission must clear.
**Not this module's:** concrete sandbox tooling choices (implementation under the
accepted class); profile *templates* and a default profile library.

---

## 7. Deliberately deferred — this module

Concrete schemas for profiles → RFC 0003. Run-envelope fields → RFC 0004.
Execution-profile *templates* and a default profile library → craft/product
material once the contract is accepted. Extension of the closed isolation-class
set (RFC5-21) or the closed destructive-operation class set (RFC5-22) → amendment
to those clauses, never by a profile declaring something outside them.

---

## 8. Owner questions owned by this module

Question numbers are **RFC-level and immutable** — q1…q6 keep their numbers
wherever they physically live. See `README.md` for the package question list.

**q3. Execution-blocked Unknown reason — ANSWERED (owner decision A5, together
with RFC 0002's corresponding question: option B).** RFC2-24 is amended with a
**twelfth primary reason**, `execution-blocked`, whose resolution route — unblock
or authorize the run — differs from "produce/capture evidence." RFC5-18 is
amended to render it; **option A is superseded**. The question as posed, both
options and their consequences, are preserved verbatim at
`../../history/RFC-0005-history.md` §q3.

**q4. Destructive-op class closure — OPEN.** RFC5-22's list is now **four**
enable-able classes — out-of-purpose credential use moved to RFC5-21's violation
set. Is that the right closure, or should filesystem deletion inside the declared
writable scratch also gate (stricter, noisier)?

---

*End of module 3 of the RFC 0005 package. Clauses RFC5-18 … RFC5-23. No retired
numbers, no merged numbers, and no clause identity shared with another module.*
