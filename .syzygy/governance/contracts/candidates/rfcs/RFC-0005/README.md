---
id: RFC-0005
title: Authentication, Consent and Execution Profiles — contract package index
status_source: owner-act-record
package: RFC-0005
modules: [admission-and-boundary, consent-egress-secrets, execution-profiles]
clauses: RFC5-1..RFC5-27 (no gaps, no retired numbers, no merges; no lettered sub-clauses — RFC5-18(a)–(e) are list items inside RFC5-18)
implementation_boundary:
  kind: requires-openspec
  clause: RFC5-27
governs: [principals, sessions, machine-credentials, client-classes, exposure-modes, consent, egress, secrets, execution-profiles, adapter-credentials, audit, revocation]
applies_to: [kernel, all-surfaces, machine-clients]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004]
tags: [security-boundary, sec-1, sec-2, sec-3, sec-4, sec-5, blocking, execution-gate, client-classes]
---

# RFC 0005 — Authentication, Consent and Execution Profiles

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
each module file's exact content digest — as an owner-adopted bootstrap act
until the independent A1 correlation mechanism exists, and as a Syzygy-verified
effective act only after correlation (RFC3-16). Absent such a record, this
contract binds nothing.

**Date:** 2026-07-30 (amended through 2026-08-02; compacted and split into a
package at rev10). **Rationale, amendment history, alternatives, and answered
questions:** `../../history/RFC-0005-history.md` (non-normative).

**Serves:** SEC-1…SEC-5; VIS-1, VIS-4 (always-human classes), VIS-5 (adapter
authorization), VIS-7/trust floor (no secret in any surface); v1.md platform
posture; SDR §5 q8 (owned here: machine-client authentication mechanism;
execution profiles). Grounded in FD-009 (LAN posture), FD-018 as amended by
FD-029 (A6-b execution profiles), OQ-007. Implements owner decisions **A1**,
**A5**, **B4**, **B8**, **B9**.

---

## Clause map and lookup rule

**Every clause identity appears in exactly one module.** One `RFC5-n` namespace,
no duplicated normative clauses, no renumbering.

| Module | File | Clauses |
|---|---|---|
| 1 — admission and boundary | `admission-and-boundary.md` | RFC5-1..RFC5-11, RFC5-24..RFC5-27 |
| 2 — consent, egress, secrets | `consent-egress-secrets.md` | RFC5-12..RFC5-17 |
| 3 — execution profiles | `execution-profiles.md` | RFC5-18..RFC5-23 |

Module sizes are deliberately **not stated here**. A measurement copied into
contract prose goes stale the moment any module moves, and moves this
package's content digest for a reason that has nothing to do with what the
package says. This artifact is governed by the applicable context-budget
policy; the current measurement lives in the generated budget report
`../../CONTEXT-BUDGET-REPORT.md`, which is regenerated, never transcribed.

**Lookup rule (deterministic).** For any citation `RFC5-n`, read `n` as an
integer: `12–17` → module 2; `18–23` → module 3; **every other number → module
1**. Two bounded ranges and a catch-all, so the rule is total over the `RFC5-n`
namespace however the range grows, never needs a search, and cannot go stale
against the bytes the way an enumeration of ranges can — RFC5-27, the package's
phase-boundary clause, resolves to module 1, which is where it lives. RFC 0005 has **no lettered
sub-clauses**: limbs such as RFC5-18(a)–(e) are list items inside one clause
body and live with their parent. Modules are numbered for reading order only —
citations name clauses, never modules.

**Reading order for a cold reader:** module 1 → 2 → 3. Module 1 is presupposed
by both others (every egress and every launch is performed for a principal it
admitted, and emits into the audit trail it defines); modules 2 and 3 are
independently readable given it, though module 3 cites module 2's execution
consent (RFC5-12).

**Section numbering inside modules** follows the pre-compaction contract
numbering, so external citations of the form "RFC 0005 §3.9" still resolve:
§3.1–3.5 and §3.10–3.11 in module 1, §3.6–3.8 in module 2, §3.9 in module 3.

## Package reader map (non-normative)

*If this map and a clause disagree, the clause wins.*

This package is Syzygy's **security boundary**: who may talk to it, what may
leave it, what may run inside it, and how every such act is recorded and
revoked. Default is deny everywhere; every exception is a recorded owner act. It
is **contract shape only** — mechanism *classes* are enumerated, no product or
stack is chosen. It is **blocking**: no observed-project code executes until this
RFC is accepted and a per-project profile exists (SEC-3).

Five rules carry most of the weight:

- **Being local proves nothing** — classification is by credential presented,
  never by network location (module 1, RFC5-3); a fresh install serves loopback
  only (RFC5-10).
- **Exactly two client classes, exhaustive and closed** (module 1, RFC5-3/5-5) —
  a browser holding a session, or a machine client holding its own machine
  credential. Web UI, official `syzygy` CLI, agent-protocol adapter (e.g. MCP),
  scripts, and fleet workers are all covered by those two, and **no later
  contract may introduce a third**.
- **Consent is four separately revocable classes** — observe, write, egress,
  execute — and nothing leaves the machine except through one choke point that
  also verifies the consent record's owner provenance (module 2, RFC5-12/5-15).
- **Fail closed in both directions** — a composite whose content class cannot be
  determined is refused egress; content that cannot be classified at ingest is
  excluded, not indexed (module 2, RFC5-14/5-16).
- **No observed-project code runs without an approved execution profile**
  (module 3, RFC5-18) — the owner's own repositories included. A
  profile-violating run terminates and its outputs cap at `report-fact`.

Two invariants span the package. **No credential to Syzygy, and no route to
Syzygy**: RFC5-24's injection prohibition (module 1) and RFC5-20/RFC5-21's
network-policy exclusion and isolation floor (module 3) bind together, so
observed code can never hold an authenticated route to the authorized surface.
And **the untrusted-tree premise**: the governed plane is writable by fleet
workers, so a consent record, a classification policy, a secret-detection policy,
and an execution-approval Decision are each honored **only under RFC3-16(a)** —
which in turn is why the audit trail must live outside that tree (RFC5-25).

## Scope

Who may talk to Syzygy and how they are admitted (principals, sessions, machine
credentials, the closed exposure-mode set); the acts-versus-claims rule that
makes revocation immediate without disturbing RFC 0002's evaluation determinism;
the consent-class taxonomy carried by RFC 0001's Consent record entity; egress
consent for model providers over a closed content-class vocabulary at a single
choke point; fail-closed secret screening at every ingest boundary with
hash-not-body exclusion provenance; the **execution profile** — the SEC-3
unblock — under which, and only under which, observed-project code may run;
adapter-credential discipline; and the audit trail every authenticated act emits
into. **Not this RFC's:** secret-detection and classification policy *content*
(quality/policy material); scope-enumeration granularity and wire formats
(RFC 0003 / RFC 0006); concrete sandbox tooling (implementation under the
accepted class); multi-user roles (deferred).

## Doctrine grounding (non-normative)

Syzygy indexes a whole portfolio, listens on a network, executes
observed-project code, sends derived content to model providers, and writes into
repositories it governs [Observed: security.md preamble]. Doctrine fixes SEC-1…5
and routes the contracts here: "the mechanism is authentication-RFC material"
(SEC-1); "the profile contract is RFC material and blocking" (SEC-3).

[Inferred] The failure mode guarded against is the **convenience default** — the
loopback endpoint answering any local process, the model call that ships a
repository "because the feature needed it," the test runner inheriting the
host's SSH agent — so every clause states the default as deny and makes the
exception a recorded owner act: a permissive configuration is always an
artifact, never an accident.

Owner history, preserved: FD-018 ruled "trust assumed" for the owner's own
projects; FD-029 amended it to A6-b (opt-in profiles), and adopted SEC-3 now
binds observed code as untrusted **regardless of who owns the project**. This
RFC follows the adopted rule, not the superseded ruling (RFC5-19; history
§RFC5-19).

## 4. Violation cases — package-spanning

*Cases 1–4, 10 and 13 are in module 1, cases 5–6 in module 2, cases 7–9 and 12
in module 3. Numbering is the stable package numbering; cases are distributed,
never renumbered. Only case 11 spans two modules and is held here.*

11. *(RFC5-11/13)* Consent is revoked and the dashboard keeps showing overlays and
    indexed content from the revoked source **unlabelled** until someone triggers
    the next pass.

## 5. Integration — package-level

**Relies on RFC 0001:** the Consent record entity (RFC1-3) module 2's class
taxonomy specializes; the Decision entity as approval/revocation warrant;
Evidence-artifact semantics for audit and execution records (SDR-8);
Proposal/materialization machinery for how approved work reaches execution.
**On RFC 0002:** evaluation identity and snapshot inputs (profile, classification
and secret-policy versions, RFC2-1 item 7); Unknown reasons #6, #7 and #12 and
the failure-state renderings (RFC2-23); the tier registry capping
policy-violating runs at `report-fact` (RFC2-25); RFC2-4's degradation-only rule,
which RFC5-11 reconciles against rather than excepts.
**On RFC 0003:** RFC3-16(a), the owner-act provenance predicate that gates four
clauses across all three modules — the egress choke point (RFC5-15), the
classification policy (RFC5-14), the secret-detection policy (RFC5-16), and the
execution gate (RFC5-18(c)) — stated once there and cited, never restated here;
RFC3-16(b) item 9, which RFC5-25's location constraint exists to keep
unforgeable; RFC3-7, RFC3-11, RFC3-30.
**On RFC 0004:** RFC4-13's provenance predicate on `gate-backed`, which sets what
an externally produced artifact may support; RFC5-19's observation/execution
boundary governs only whether a profile is required.

**Provides to:** **RFC 0002** — the consent-record semantics behind Unknown
reason #6, the execution gate behind fresh gate-backed verification evidence, and
the acts-versus-claims rule (RFC5-11) its temporal machinery presupposes;
**RFC 0003** — the fields consent, credential, profile, and audit records must
encode, **including RFC5-25's out-of-tree location constraint**, which is
normative and not a schema choice; **RFC 0004** — the adapter-credential
discipline (RFC5-24), the ingest-boundary screening obligation on every adapter
read (RFC5-16) under the *observing* project's policy (RFC3-30), and the
run-envelope fields for profile identity/version (RFC5-18(e)) and
policy-violation flags (RFC5-21), which RFC4-19 carries as named rows;
**RFC 0006 and the surfaces (incl. RFC 0008)** — session semantics for
URL/selection state, the consent-rendering obligation (SEC-2) and exclusion
counts; **RFC 0010 and RFC 0011** — the closed two-class client contract
(RFC5-3, RFC5-5, RFC5-6) under which the official `syzygy` CLI, agent-protocol
adapters, scripts, and fleet workers reach the canonical service, the egress
choke point (RFC5-15) and ingest screening (RFC5-16) every governed context
packet passes, and the execution gate (RFC5-18) any fleet-executed run must
clear.

## 6. Alternatives considered

All eight rejected or declined alternatives are recorded in
`../../history/RFC-0005-history.md` §6. Three stay load-bearing for reading a
live clause: **network-perimeter trust** was rejected outright, so tailnet
identity is retained only for RFC5-9's *device-restriction* requirement, never
for client classification; **act-timed re-render on revocation** was rejected in
favour of RFC5-11's rendering obligation, because letting a security event change
a claim's *value* outside an identified evaluation is exactly what RFC2-4
forbids; and **restating authorization authenticity per artifact class** was
declined in favour of citing RFC 0003's single predicate (RFC3-16(a)) from every
consuming gate — one predicate, one home, no drift.

## 7. Deliberately deferred — package-level

Concrete schemas for consent, credential, profile, and audit records → RFC 0003.
Adapter read-screening mechanics and run-envelope fields → RFC 0004. Session/URL
semantics detail → RFC 0006. Secret-detection and classification policy content
and audit-retention periods → quality/evidence policy (craft). Multi-user
principals, roles, delegation → post-V1, behind the RFC5-1 pre-commitments.
Execution-profile *templates* and a default profile library → craft/product
material once the contract is accepted. Certificate interactions → post-V1
certificate RFC.

## 8. Owner questions — package index

Numbering is **RFC-level and immutable**: q1…q6 keep their numbers wherever they
physically live, so an external "RFC 0005 q1" resolves through this table. Each
question's full text lives in the module owning its clause; answered items'
reasoning is in `../../history/RFC-0005-history.md`.

| # | Subject | State | Lives in |
|---|---|---|---|
| q1 | Machine-client mechanism (RFC5-7) | **open — scoped** (rev10: must close before V0 implementation; does not block specification) | `admission-and-boundary.md` §8 |
| q2 | Overlay-network device identity for browser sessions (RFC5-4/RFC5-9) | **answered — owner decision B9** (declined) | `admission-and-boundary.md` §8; history §q2 |
| q3 | Execution-blocked Unknown reason (RFC5-18) | **answered — owner decision A5** (option B) | `execution-profiles.md` §8; history §q3 |
| q4 | Destructive-op class closure (RFC5-22) | **open** | `execution-profiles.md` §8 |
| q5 | Rotation overlap default (RFC5-6) | **open** (proposed: zero) | `admission-and-boundary.md` §8 |
| q6 | Revocation rendering versus re-evaluation (RFC5-11) | **answered — owner decision B4** (stronger form taken) | `admission-and-boundary.md` §8; history §q6 |

**The one open question with specification impact is q1, and it is scoped, not
answered.** The rev10 scope ruling (directive §2 / OD-R10-5) records that q1
selects among RFC5-7's four mechanism classes, each of which satisfies RFC5-6's
contract shape identically, so it cannot alter the meaning of any specification
authored against RFC5-6; the browser-versus-machine-client contract (RFC5-3,
RFC5-5, RFC5-6) is closed. Full text in `admission-and-boundary.md` §8.

---

*End of RFC 0005 package index. Clauses RFC5-1 … RFC5-27 distributed across
three modules, with no lettered sub-clauses. No retired numbers, no merged
numbers, no gaps in the range, and no clause identity in more than one module.*
