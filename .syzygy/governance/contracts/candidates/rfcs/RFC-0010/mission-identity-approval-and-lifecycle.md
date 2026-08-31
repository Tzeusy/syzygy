---
id: RFC-0010
title: Mission Control and Autonomy Envelopes — platform boundary, mission identity, approval, and lifecycle
status_source: owner-act-record
module: mission-identity-approval-and-lifecycle
clauses: "RFC10-1..RFC10-6, RFC10-14, RFC10-16, RFC10-24 (non-contiguous — see the package clause map)"
governs: [missions, service-boundary, mission-lifecycle, mission-homes, phase-boundary]
applies_to: [mission-control, workspace, all-surfaces, machine-clients]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0005, RFC-0006, RFC-0008]
tags: [autonomy, human-control, platform, identity, lifecycle]
---

# RFC 0010 — Mission Control: platform boundary, mission identity, approval, and lifecycle

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — either owner-adopted (bootstrap,
uncorrelated) or Syzygy-verified, with the exact provenance state always
visible (RFC3-16). Absent such a record, this contract binds nothing.

**Package:** module 1 of 5 of the RFC 0010 contract package. Index, clause
map, lookup rule, package-level integration and deferrals: `README.md`.
Rationale, amendment history, and violation cases:
`../../history/RFC-0010-history.md` (non-normative).

**Serves:** VIS-4 (always-human decision classes), VIS-5 (adapter
authorization), SEC-1..SEC-5; owner direction OD-R10-1/OD-R10-2 (recorded in
the rev10 owner-direction record, a bootstrap process artifact retained with
the delivery packet).

## 1. Scope of this module

The platform boundary (one service, one semantic API, many clients —
RFC10-1..3); Mission identity, approval provenance at the identity level, the
lifecycle vocabulary and its bounded-park rule, and the mission/work seam
(RFC10-4..6); where project-bound mission artifacts live (RFC10-14); and the
binding phase rule at the OpenSpec seam (RFC10-16), which binds the whole
package.

## 2. The contract

### 2.1 Platform capability, not a truth surface

**RFC10-1.** Mission Control is a **workspace-level operator domain**, not a
fourth project-specific truth surface. It mints no project truth: project
doctrine, contracts, specifications, evidence, evaluations, and work
semantics remain governed exclusively by their own contracts (RFC 0001–0009
and successors). No Mission Control artifact, cache, or store may become a
second project-internal source of truth; a Mission Control view of project
state is a projection of kernel answers (RFC 0006), rebuildable and
non-authoritative.

**RFC10-2.** **Service-and-client boundary.** One canonical long-lived
Syzygy control-plane service owns runtime state and the semantic API. The
web UI (including Mission Control's), the official `syzygy` CLI, scripts,
and agent-protocol adapters (e.g. MCP) are **clients** of that service. All
clients — human and machine — receive the same identities, evaluations,
evidence, missions, attention items, and policy results (RFC6-13's
one-truth-two-consumers property, with RFC6-14's label parity, extended to
mission data). Agents consume stable machine-readable
data; scraping human-rendered tables is never a conforming integration.
[Observed — owner direction] Exact implementation language, daemon
packaging, transport, and whether distribution is literally one binary
remain implementation choices; this clause binds the topology (one canonical
service, one semantic API), not the technology.

**RFC10-3.** Every Mission Control client is one of RFC5-3's two client
classes — there is no third. Machine clients (CLI, an MCP or equivalent adapter,
scripts, fleet workers) are admitted only under RFC5-5 with RFC5-6-shaped
credentials, scoped deny-by-default; mission-affecting scopes (approve,
pause, cancel, envelope change) are distinct scope entries, never implied by
read scopes. Holding a mission-affecting scope permits **submitting** the
corresponding act for owner attendance and nothing more — a machine
credential can never itself produce the owner act the submission awaits
(RFC10-8, RFC3-16(a)).

### 2.2 Mission identity and scope

**RFC10-4.** A **Mission** is a first-class identified entity of RFC1-7's
**mission extension profile** (minted under RFC 0001's identity rules; this
contract is the profile-defining RFC, and the minting authority is the
control-plane service at approval submission, deterministic over the
objective, target, and initiating act) binding at minimum: its **objective and
rationale**; its **target** (workspace, projects, capabilities, and/or
requirements); its **exact pinned inputs** — the doctrine, contract,
specification, policy, and evaluation revisions it runs under, by digest or
revision identity; its **initiating owner act** (mission approval is an
authorization-bearing act under RFC3-16(a) — a valid state-(1) or state-(2)
act is effective and its exact provenance state is rendered; an absent,
invalid, or machine-submitted record authorizes nothing); its **parent mission**, if any;
its lifecycle state and terminal outcome. Pinned inputs are immutable for
the mission's life: a change to any pinned input does not silently retarget
a running mission — it raises an escalation (RFC10-13) whose choices include
re-approval against the new inputs.

**RFC10-5.** The candidate mission lifecycle vocabulary is:

```text
draft → awaiting-approval → approved → running
draft | awaiting-approval | approved → expired   (maximum time to first
                                                  dispatch, RFC10-17(a))
running ⇄ paused
running → blocked (→ running on unblock)
blocked | paused → expired                       (park expiry)
running | paused | blocked → failed              (RFC10-18, RFC10-20(d))
any non-terminal state → cancelled | expired     (human act)
running → completed
```

[Inferred] This list is **provisional at this contract's acceptance**: per
owner direction it is not frozen until its interaction with Trajectory's
normalized work states (RFC 0008) is reviewed at surface specification —
freezing happens by OpenSpec requirement, not by this clause. What *is*
fixed now: every terminal state is recorded with its reason; `expired` and
`cancelled` are always reachable by human act; no state transition widens
the envelope; and exit from `blocked` where the block arose under RFC10-8
or RFC10-11 is a **human resolution act** — an agent's "condition cleared"
assertion never takes that transition.

**No park is indefinite — `blocked` or `paused`, whatever gave rise to it.**
Every non-terminal park carries a **maximum park duration**, declared by the
envelope; where none is declared the maximum is the expiry of the Attention
Item that park minted (RFC10-12), and where the park minted none it is the
envelope's shortest declared **duration-typed** maximum — counts and rates
(RFC10-22's queue bounds) are not durations and are outside this limb. The
set is never empty: wall-clock is a budget, an undeclared budget is zero
delegated wall-clock (RFC10-7), so every runnable mission declares a
wall-clock budget and this limb always has a referent. Silence buys no
unbounded park in any direction. At the maximum the mission transitions to **`expired`**, a terminal
state whose reason is recorded.

The rule covers **both** non-terminal states and **every** source — RFC10-8,
RFC10-11's `paused`-or-`blocked` disjunction, RFC10-18, and RFC10-22's
pause-on-attention-bound — because the defect is a lifecycle defect and not a
property of any one source: neither state is terminal, RFC10-17 releases a
reservation only on completion or termination, and a park is therefore a way
to hold budget that no clause elsewhere reaches. **A rule that bounded
`blocked` alone would leave `paused` as the park a mission is told to
enter** — the park RFC10-22 mandates outright, and one limb of the
disjunction RFC10-11 offers. Where a clause offers `paused` or `blocked`
without a decider, the narrowest reading takes `blocked` — the state whose
exit is a human act. Expiry from a park is a
**termination, never a resolution**: it widens nothing (RFC10-12), does not
substitute for the human resolution act where the paragraph above owes one,
and does not mark the condition cleared. It ends the mission and fires
RFC10-19's duties.

**RFC10-6.** **A mission is not work, and work is never proof.** Missions
authorize the *materialization* of work items; the work items themselves,
their states, dispatch, execution records, and evidence remain entirely
RFC 0008/0002 semantics. A mission's completion predicate is evaluated
against **evidence** (RFC 0002), never against work having been performed.
No mission bypasses evidence, reconciliation, consent (RFC5-12), egress
(RFC5-14), or execution-profile (RFC5-18) gates — a mission is authority to
*proceed inside* the gates, never authority to skip one. The completion
predicate declares the **minimum RFC2-25 evidence tier** it accepts
(unstated means, per RFC10-7's narrow reading, the strongest applicable
tier), and the completion render discloses the tier actually achieved
(VIS-2) — "all work items closed" or worker assertion alone never
satisfies a conforming predicate.

Where two or more admitted evidence artifacts bearing on one completion
predicate support opposing conclusions, **the predicate is not satisfied**:
the disagreement is recorded as evidence, the predicate's conclusion renders
Unknown, and the condition is an escalation trigger under RFC10-13. It is
never resolved by recency, by tier where the tiers are equal, by the
executing principal's selection among sources, or by any precedence rule.
Where the disagreeing artifacts support co-unsatisfiable authoritative
claims, RFC2-15's Contradiction machinery governs and owner adjudication is
the only exit.

### 2.3 Project-bound mission homes

**RFC10-14.** Project-bound mission artifacts (the mission record, envelope,
checkpoints, attention items scoped to it) live under a governed project
home — `.syzygy/work/missions/<mission-id>/` — subject to RFC 0003's
governance-home discipline: typed, provenance-labeled, and never a parallel
truth store for anything another contract already governs. The
mission-approval **act record** does not live here: it is appended to
`.syzygy/governance/decisions/`, binding the envelope's exact digest
(RFC3-16(b) item 3) — the in-tree envelope file plus any stamp is never
itself the approval.

### 2.4 Authority boundary at the OpenSpec seam (binding phase rule)

**RFC10-16.** This contract schedules nothing: **it is not a specification
of record from which implementation work may be scheduled**. No
implementation work for user-observable Mission Control behavior — mission
creation/approval flows, lifecycle displays, envelope editing, attention
queue rendering, CLI commands, API endpoints and their answers,
MCP-or-equivalent tools — may be scheduled solely from this RFC — including everything RFC10-17..22
requires of a runtime. Before
implementation, every observable consequence either maps to an approved
OpenSpec requirement and scenario in the governance root's `openspec/**`
plane, or carries a reviewed N/A judgment proving it purely structural
with no independently testable behavior. At surface specification a
clause-to-requirement coverage matrix over RFC10-1..RFC10-22 is produced —
**that matrix is review material, never authority**. This clause creates
no OpenSpec content now (none may exist during bootstrap). (Shape-parallel
with RFC6-28, RFC7-38, RFC8-32, RFC9-52.)

### 2.5 Doctrine precondition on operation

**RFC10-24.** Owner ruling
`BOUNDED-MISSION-DOCTRINE-INTERPRETATION-2026-08-31` records that unamended
doctrine permits bounded multi-pass mission operation after a human owner
approves the exact mission and exact envelope. That ruling satisfies this
clause's owner-ruling alternative; it does not accept RFC 0010, sign any
OpenSpec behavior, or approve or start a mission. RFC 0010 remains candidate
and binds nothing, so no mission may operate or leave `awaiting-approval`
unless this contract is accepted, its required OpenSpec behavior is signed,
RFC10-16 is satisfied, the exact mission and envelope carry effective owner
acts under RFC3-16(a), and every other independent mission gate passes.
State (1) and state (2) acts may satisfy the owner-act gate with their exact
provenance state rendered. Satisfaction of the doctrine alternative never
discharges RFC10-16 or any effect-specific gate.

## 8. Owner questions

*Package numbering; question numbers never shift. Full package index:
`README.md` §8.*

1. **Lifecycle × work-state review — OPEN.** Does the owner accept RFC10-5's
   candidate lifecycle as the *working* vocabulary pending the OpenSpec
   review against RFC 0008's states, or require the review first?

---

*End of RFC 0010 module 1. Clauses RFC10-1 … RFC10-6, RFC10-14, RFC10-16,
RFC10-24 — non-contiguous by design; the package README's clause map is the
lookup authority. Nothing merged, nothing retired.*
