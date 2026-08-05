---
id: RFC-0010
title: Mission Control and Autonomy Envelopes
status_source: owner-act-record
clauses: "RFC10-1..RFC10-22"
governs: [missions, autonomy-envelopes, guardrails, attention-items, workspace-governance, service-boundary]
applies_to: [mission-control, workspace, all-surfaces, machine-clients]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0005, RFC-0006, RFC-0008]
tags: [autonomy, human-control, budgets, escalation, platform]
---

# RFC 0010 — Mission Control and Autonomy Envelopes

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — as an owner-adopted bootstrap act until
the independent A1 correlation mechanism exists, and as a Syzygy-verified
effective act only after correlation (RFC3-16). Absent such a record, this
contract binds nothing.

**Serves:** VIS-4 (always-human decision classes), VIS-5 (adapter
authorization), SEC-1..SEC-5; owner direction OD-R10-1/OD-R10-2
(recorded in the rev10 owner-direction record, a bootstrap process
artifact retained with the delivery packet). New at rev10 — no rev9
predecessor.

## 0. Reader's summary (non-normative)

A human approves one bounded **Mission**; agent fleets then plan, execute,
verify, re-plan, and recover inside an approved **autonomy envelope** they
can never widen, until the mission ends or a terminal/escalation condition
fires. Mission Control is a workspace-level operator domain over the same
one canonical Syzygy service and semantic API that serves Polaris,
Trajectory, and Orrery — it is **not** a fourth project truth surface. Human
attention arrives as decision-ready **Attention Items**, not event streams.
Portfolio-level authority lives in a typed **workspace governance store**
that can never override project-internal truth.

## 1. Summary

This contract fixes: the platform boundary (one service, one semantic API,
many clients — RFC10-1..3); Mission identity and lifecycle (RFC10-4..6); the
autonomy envelope and the no-self-widening rule (RFC10-7..9); the guardrail
runtime as distinct from semantic correctness (RFC10-10..11); attention and
escalation (RFC10-12..13); project-bound versus portfolio missions and the
workspace governance store (RFC10-14..15); and the OpenSpec phase rule
(RFC10-16). A **correction plane** is added beside the prevention plane:
budget reservation (RFC10-17), independent completion adjudication
(RFC10-18), effect reversibility and recovery (RFC10-19), what stop
guarantees (RFC10-20), cross-project consent composition (RFC10-21), and
attention-queue bounds (RFC10-22).
Autonomy level enumerations, lifecycle freeze, store schema, and
all transport/language/packaging choices are explicitly deferred (§7, §8).

## 2. Motivation and doctrine grounding

Doctrine holds that Syzygy is not an unattended reconciler by default and
that certain decision classes are always human (VIS-4). The owner's settled
direction (OD-R10-2) adds: a human may deliberately approve one **bounded
mission** rather than one work item at a time — high-level human control,
not silent default autonomy. [Observed] Nothing in RFCs 0001–0009 gives that
act a home: work is one-item-grained (RFC 0008) and the workspace manifest
is presentation-only (RFC 0003). This contract supplies the missing
authority shape without weakening the doctrine posture. A narrow doctrine
clarification is drafted separately (proposed amendment **D3**, delivered
with the rev10 packet; if adopted it lands in the doctrine amendment log)
and **is not applied by this RFC**; until the owner rules on it, this
contract's reading of human-triggered propagation stands only as far as
doctrine already permits — which means missions can be *specified* under
this contract but cannot lawfully *operate* under unamended doctrine's
one-pass trigger.

## 3. The contract

### 3.1 Platform capability, not a truth surface

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

### 3.2 Mission identity and scope

**RFC10-4.** A **Mission** is a first-class identified entity (minted under
RFC 0001's identity rules) binding at minimum: its **objective and
rationale**; its **target** (workspace, projects, capabilities, and/or
requirements); its **exact pinned inputs** — the doctrine, contract,
specification, policy, and evaluation revisions it runs under, by digest or
revision identity; its **initiating owner act** (mission approval is an
authorization-bearing act under RFC3-16(a) — a mission without verifiable
owner-act provenance authorizes nothing); its **parent mission**, if any;
its lifecycle state and terminal outcome. Pinned inputs are immutable for
the mission's life: a change to any pinned input does not silently retarget
a running mission — it raises an escalation (RFC10-13) whose choices include
re-approval against the new inputs.

**RFC10-5.** The candidate mission lifecycle vocabulary is:

```text
draft → awaiting-approval → approved → running
running ⇄ paused
running → blocked (→ running on unblock)
running → completed | failed | cancelled | expired
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

### 3.3 The autonomy envelope

**RFC10-7.** Every approved mission carries an **autonomy envelope** that
bounds, at minimum: permitted **change classes**; **prohibited and
human-only surfaces** (the VIS-4 always-human classes are non-delegable and
appear here as a floor, not a choice); the **maximum autonomy level** —
levels are an enumerated vocabulary to be fixed at surface specification
(e.g. propose-only, materialize work, open PR, merge, deploy; the
enumeration is an explicit open default, §8 q2); allowed **projects,
repositories, and paths**; allowed **tools, model/provider classes, and
execution profiles** (by RFC5-18 profile identity); **budgets** — token,
monetary, wall-clock, retry, and concurrency; **required gates and
independent reviews**; **evidence and reconciliation requirements**;
**stop, pause, cancellation, and expiry conditions**; **checkpoint and
recovery obligations**; **escalation triggers**; and the **completion
predicate**. An envelope field left unstated is the *narrowest* reading,
never the widest: absence of a budget is zero delegated spend of that kind,
absence of a path grant is no write access. A bound stated **ambiguously**
likewise resolves to its narrowest defensible reading, and genuine
ambiguity in a load-bearing bound is an escalation trigger (RFC10-13),
never a call the running agent adjudicates for itself. Until the
autonomy-level vocabulary is enumerated by owner act (§8 q2), the maximum
autonomy level of every envelope is capped at **propose-only**: a stated
higher level has no enumerated vocabulary to bind to and does not take
effect.

The narrowest-reading rule applies to grants and obligations **in opposite
directions and to the same effect**: an unstated *grant* is the narrowest
grant; an unstated *obligation* is the strictest obligation. Absence of a
declared gate set means every otherwise-applicable gate is required; absence
of declared checkpoint and recovery obligations means no effect outside
`.syzygy/**` and `openspec/**` is authorized until they are declared; absence
of declared escalation triggers means RFC10-13's minimum set binds in full.
No field's absence ever relaxes a duty. (Both worked examples above are
grants; read alone they would have let every obligation-shaped envelope field
fail open, which is the reading a self-interested fleet prefers.)

**`propose-only`, defined.** Until the autonomy-level vocabulary is
enumerated by owner act, `propose-only` means exactly: a mission may read
consented sources, compile context packets, run agents within its reserved
budget (RFC10-17), and author drafts, proposals, and submissions into
`.syzygy/**` and `openspec/**` rendered unadopted (RFC3-16). It may **not**
cause any effect outside those two namespaces: no version-control push or
pull request, no merge, no deploy, no package or artifact publication, no
mutation of an external service or database, and no RFC5-22
destructive-operation class **whether or not the granted execution profile
standing-approved it**. Egress to a model provider remains permitted only
under an RFC5-14 consent record naming the provider and content classes. A
level above `propose-only` is inoperative until both the vocabulary is
enumerated and each level's permitted effect set is stated. Because this cap
is what makes several other deferrals safe, it may not be read as
provisional: a cap binding to an undefined term is not a cap.

**RFC10-8.** **No self-widening — the load-bearing rule.** No agent, fleet,
worker, or Mission Control component may widen any bound of the envelope it
runs under: not budgets, not autonomy level, not surfaces, not paths, not
tools, not gates, not by creating a child mission whose envelope exceeds the
parent's remaining envelope, not by consuming another mission's budget, and
not by re-interpreting an ambiguous bound in its own favor (ambiguity
resolves narrow, per RFC10-7). Widening is exclusively a human act carrying
RFC3-16(a) owner-act provenance. An agent-proposed widening is a
**proposal** — it renders as an Attention Item and has no effect until the
act. **Child missions are reservations, not copies:** an agent may mint a
child mission only where the parent envelope **explicitly grants
decomposition** (an owner-approved envelope field; absent the grant, the
narrow reading is no children). A derived child's authorizing provenance
is the **parent's owner act plus a recorded derivation** — never a new
self-minted act; RFC10-4's initiating-act field binds the parent act for
such a child. Every child grant is **debited from the parent's remaining
envelope at grant time**: the parent's own spend plus the sum of
outstanding child grants never exceeds any parent budget, so sibling
children can never jointly exceed what the one owner act authorized. An
*attempted* self-widening is a violation: the mission transitions to
`blocked`, the attempt is recorded as evidence, and an Attention Item is
minted.

**RFC10-9.** The envelope (and every amendment to it) is an
**authorization-bearing governance artifact** under RFC3-16(a): it is
honored only with **verifiable** owner-act provenance. Mission approval is
a *runtime* act performed while Syzygy exists, so it is always an
A1-mechanism act — an owner-attended, Syzygy-mediated ceremony correlated
to the external audit trail — never a bootstrap-shaped tree record: an
approval resting on a state-(1) record (RFC3-16(c)) has **not** satisfied
the predicate, and its mission does not leave `awaiting-approval`.
Shipping that ceremony is therefore a hard precondition of Mission Control
operating at V0 — the same pre-A1 posture RFC5-15 and RFC5-18(c) already
impose on egress and execution. The two-state rendering vocabulary
("owner-adopted (bootstrap, uncorrelated)") applies to the *foundational
corpus a mission cites*, never to the mission's own authorization. An
envelope present in a governed tree without verifiable act provenance
authorizes nothing (RFC3-16(a)'s effect rule); its mission cannot leave
`awaiting-approval`.

### 3.4 The guardrail policy runtime

**RFC10-10.** Two enforcement planes, never conflated:

```text
semantic correctness — established through specifications, evidence,
    and reconciliation (RFC 0002); Syzygy does not make untruth impossible,
    it makes truth-status visible

execution guardrail enforcement — budgets, permissions, write boundaries,
    risk floors, stop conditions, protected surfaces, required approvals;
    Mission Control MUST prevent every act it mediates from exceeding
    the approved authority and resource envelope
```

Guardrail enforcement is **preventive**, not merely observational: an
out-of-envelope act is refused at the choke point (the same single-choke
posture as RFC5-15), not performed-then-flagged. The MUST is scoped
honestly to **Syzygy's own choke points**: an actor holding
externally-granted toolchain credentials can act outside Syzygy's
mediation, and those effects are bounded by the adapter and credential
authorization (VIS-5) — not by this runtime. The guardrail runtime makes
out-of-envelope *Syzygy-mediated* acts impossible and out-of-envelope
*external* acts visible (doctrine: not an enforcement engine outward) —
never the wider claim. Every guardrail decision —
allow, refuse, halt — is recorded as identified evidence attributable to its
mission, work item, and principal (RFC5-25 attributability).

**RFC10-11.** **Bound exhaustion never self-extends.** Reaching any envelope
bound (budget, time, retries, risk floor) halts further materialization and
execution under that mission — transition to `paused` or `blocked` with an
Attention Item — and never silently raises the bound, borrows against
another mission, or downgrades the required gate set. Partial work already
lawfully dispatched completes or checkpoints per the envelope's recovery
obligations, **strictly within the budget reserved for it at dispatch
(RFC10-17): completion headroom is reserved in advance or the work is
checkpointed and halted, never funded by spending past the exhausted
bound.**

### 3.5 Human attention and escalation

**RFC10-12.** The **Attention Item** is a first-class identified entity — a
decision-ready packet binding at minimum: **what happened**; **why human
attention is required**; the affected mission, work, and project; the
**evidence and its uncertainty** (Unknowns rendered as Unknowns, RFC 0002);
the **available choices**; the **consequence of each choice**; the
**default and expiry if ignored** — an expiry default must be safe: expiry
may narrow, pause, or block, and may never widen an envelope or approve
anything; what work is **blocked** and whether the situation is
**reversible**; and, on resolution, the **resolution act and its
provenance** (a resolution that authorizes anything is an RFC3-16(a) act).
One authorizing resolution act resolves **one** item — or explicitly
enumerates each resolved item's identity and the option chosen for it; a
bulk act over unenumerated items resolves nothing.

**RFC10-13.** The attention queue **compresses event volume into
decision-ready packets**; streaming every run event to the human is a
violation of this clause, not a conservative default. Attention Items never
silently disappear: every item terminates in a recorded resolution,
expiry-to-safe-default, or explicit human dismissal — each attributable and
queryable afterwards. Escalation triggers fire on, at minimum: envelope
bound approach/exhaustion; risk exceeding the delegated threshold; a
protected or human-only surface in the proposed path; an unresolved
contradiction or genuine product choice; evidence unable to establish
progress; unsafe recovery.

### 3.6 Project-bound and portfolio missions

**RFC10-14.** Project-bound mission artifacts (the mission record, envelope,
checkpoints, attention items scoped to it) live under a governed project
home — `.syzygy/work/missions/<mission-id>/` — subject to RFC 0003's
governance-home discipline: typed, provenance-labeled, and never a parallel
truth store for anything another contract already governs. The
mission-approval **act record** does not live here: it is appended to
`.syzygy/governance/decisions/`, binding the envelope's exact digest
(RFC3-16(b) item 3) — the in-tree envelope file plus any stamp is never
itself the approval.

**RFC10-15.** **Portfolio authority is a distinct plane.** A cross-project
mission never makes one project authoritative over another. Portfolio-level
governance — workspace missions, portfolio priorities, global and
per-project budgets, fleet capacity and concurrency, project
pause/maintenance-only modes, cross-project attention and scheduling
policy — lives in a typed, platform-level **workspace governance store**,
distinct from the presentation-only workspace manifest (which remains
personal presentation state, RFC 0003). The store's entries that authorize
anything are RFC3-16(a) artifacts. The store **must never become
authoritative for project-internal doctrine, contracts, specifications, or
behavior** — its writ ends at scheduling, budget, and attention policy.
Where the writ's own enumeration (per-project budgets, pause and
maintenance-only modes) meets that prohibition, **the prohibition wins**:
pausing a project means Syzygy refuses to schedule against it, and never
mutates project-internal state or status. Its concrete home and schema are
deferred (§8 q3) — and minting the store is an authority-plane widening
that requires an RFC3-15-style recorded owner widening, not merely a
schema decision.

### 3.7 The correction plane — what happens after something goes wrong

RFC10-1..RFC10-16 are a **prevention** plane: they make out-of-envelope acts
impossible at Syzygy's choke points. Prevention is not enough, because
prevention only ever addresses the *future*. These six clauses address the
*past*: work already dispatched, money already spent, effects already
applied, and a human who needs to be able to stop all of it. Pause is not
rollback; refusing the next act does not undo the last one.

**RFC10-17. Budget is reserved, not merely observed.** Every budget in an
envelope is accounted in five distinct quantities: **authorized** (the owner
act's figure), **reserved** (committed at dispatch to work not yet complete),
**spent** (measured consumption), **released** (reserved-but-unspent,
returned on completion or termination), and **overrun** (spend exceeding
authorized). **No work is dispatched without reserving its declared maximum
cost against the envelope at dispatch time**, and reserved + spent never
exceeds authorized — the sibling-sum invariant RFC10-8 states for child
missions, applied to every dispatch. Work whose maximum cost cannot be
declared is not dispatchable under that budget. **Where measured spend
against a bound is Unknown (RFC8-19, RFC2-23), the bound is treated as
reached**: the mission transitions per RFC10-11 and an Attention Item states
the measurement gap — Unknown spend is never read as zero spend. Any overrun
is recorded as attributable evidence against the mission and mints its own
Attention Item; a mission record showing a respected bound with unrecorded
overrun is a violation of this clause.

**RFC10-18. Completion is reported by the executor and established by
another.** A mission's executing agents, fleets, and workers **may report**
that the completion predicate is satisfied and **may never establish it**.
The `running → completed` transition is taken only by (a) an owner act, or
(b) a declared, owner-approved evaluation independent of the executing
principal and whose supporting evidence is `gate-backed` (RFC2-25) — never by
the principal that performed the work, and never by a principal that
principal routed. A mission's terminal state is an **authorization-bearing
determination** under RFC3-16(a) where it discharges an owner act's
objective. Where no independent establisher is available for a mission's
objective class — including wherever RFC2-19 leaves reconciliation
uncomputed — the mission terminates as `blocked` with an Attention Item,
never as `completed`. An unstated minimum evidence tier means `gate-backed`;
"the strongest applicable tier" (RFC10-6) is never a judgment the executing
principal makes for itself.

**RFC10-19. Effects are classified before they are authorized.** Every effect
class an envelope permits is declared **reversible**, **compensatable** (with
the compensating action named), or **irreversible**. An effect class not so
classified is not authorized — RFC10-7's unstated-is-narrowest rule applied
to effects. An envelope permitting any irreversible class states that class
explicitly on its own face; **a destructive-operation class reaches a mission
only where the envelope names it, never by inheritance from an execution
profile's standing approval (RFC5-22)**. Where a mission enters `failed`,
`cancelled`, or `expired` with effects already applied: every compensatable
effect's compensating action is attempted and its outcome recorded as
evidence; every irreversible effect is enumerated in a single Attention Item
naming what cannot be undone; and the mission's terminal reason (RFC10-5)
states the reversibility disposition of every applied effect. **Pause is not
rollback**: transitioning to `paused` or `blocked` discharges no obligation
under this clause. A **named recovery owner** — the owner, or a principal the
envelope designates — is bound at approval time, and resumption from `paused`
re-verifies the pinned inputs (RFC10-4), the remaining reserved budget
(RFC10-17), and the envelope's continued act provenance (RFC10-9) before any
dispatch.

**RFC10-20. What stop guarantees.** A human stop, cancellation, or expiry of
a mission (RFC10-5) has three effects, all immediate at the act: **(a)** no
further work is dispatched and no further Syzygy-mediated act is admitted
under that mission; **(b)** every run Syzygy launched under the mission is
terminated together with its descendants, through the kill switch RFC5-21
requires of every isolation class — a stop that leaves Syzygy-launched runs
executing does not conform; **(c)** each terminated run's partial state is
checkpointed and recorded as evidence, and any effect already applied is
classified and dispositioned under RFC10-19. The envelope declares a
**maximum stop latency**; an undeclared latency means stop is synchronous —
the act does not return until (a) and (b) hold. Effects produced outside
Syzygy's mediation by externally-granted credentials are **not** covered by
(b); the mission's stop record states that boundary explicitly rather than
implying a completeness the runtime cannot deliver (RFC10-10).

**RFC10-21. Cross-project composites carry every embedded project's consent
requirement.** A context packet, prompt, summary, embedding, or any other
composite assembled under a mission spanning more than one project is
subject, at the RFC5-15 choke point, to the egress-consent record of **every
project whose content it embeds** — not one of them, and never the project
the composing step names for itself. A composite embedding content from a
project for which the naming (project, provider) consent is absent, not in
force, or of unverifiable provenance **fails closed and the refusal renders**,
exactly as an undeterminable content class does (RFC5-14). Evidence gathered
within one project never satisfies a completion predicate scoped to another.
Where the workspace governance store's per-project budget and an envelope's
budget both bind (RFC10-15, RFC10-7), **the lesser binds**, and a portfolio
mission's spend against a project is debited from that project's budget as
well as the mission's.

**RFC10-22. The attention queue is bounded.** Every Attention Item
additionally carries an **urgency class** from a closed vocabulary fixed at
surface specification, and the **envelope bound, gate, or protected surface
it implicates** where one exists. Every envelope declares a **maximum
outstanding attention count** and a **maximum item rate** for the missions
under it; an undeclared maximum means one outstanding item — the narrowest
reading (RFC10-7). **On reaching either bound the mission pauses rather than
enqueueing further items**: a mission may not convert the owner's finite
attention into throughput. Items presenting the same decision are
deduplicated into one item recording its multiplicity. Every item's expiry
falls within a declared maximum beyond which its stated default is no longer
presumed safe; an item whose expiry exceeds that maximum is not well-formed.
RFC10-13's anti-streaming rule bounds *granularity*; this clause bounds
*volume*, and without both, denial of owner attention is reachable without
widening anything.

### 3.8 Authority boundary at the OpenSpec seam (binding phase rule)

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

## 4. Violation cases

1. *(RFC10-8)* A worker raises its own retry budget "to finish the
   objective"; a planner spawns a child mission with a wider path grant than
   the parent's remainder. Both: blocked mission, recorded attempt,
   Attention Item.
2. *(RFC10-11)* A budget exhausts and the runtime "helpfully" extends it 10%
   to complete in-flight planning.
3. *(RFC10-1)* Mission Control keeps its own copy of requirement states that
   drifts from kernel answers and is consulted as truth.
4. *(RFC10-13)* An attention item expires and thereby approves the pending
   deploy (expiry widened authority).
5. *(RFC10-6)* A mission marks itself completed because all its work items
   closed, with no evidence satisfying the completion predicate.
6. *(RFC10-15)* A workspace-store entry sets a project's requirement
   priority, overriding the project's own Polaris intent.
7. *(RFC10-2)* An agent integration parses the Mission Control web UI's
   HTML table because "the API lacked that column."
8. *(RFC10-17)* Five workers dispatch concurrently against one budget with
   nothing reserved; the fourth's spend is what discovers the bound. Or: cost
   telemetry is unavailable, the runtime reads the missing figure as zero,
   and the mission runs on.
9. *(RFC10-18)* The fleet that did the work declares the objective met and
   the mission closes on its own report.
10. *(RFC10-19)* A mission fails after publishing a package. It transitions
    to `failed`, halts cleanly, and no record says the package is still
    published or who owns undoing it.
11. *(RFC10-20)* The owner hits stop; dispatch ceases; the twelve agent runs
    already executing keep running to completion.
12. *(RFC10-21)* A portfolio mission summarizes projects A and B into one
    prompt and ships it under A's model-provider consent; B never consented.
13. *(RFC10-22)* Overnight, a mission mints 400 individually well-formed
    Attention Items. Each expires safely; the owner's morning is gone and the
    envelope was never widened.

## 5. Integration

- **RFC 0001:** Mission and Attention Item are identified entities;
  relations (mission targets requirement, attention blocks work) carry
  semantic classes, never planes.
- **RFC 0002:** completion predicates, guardrail decisions, and escalation
  facts are evidence; Unknown is first-class in attention packets.
- **RFC 0003:** mission approval, envelope, and workspace-store
  authorizations are RFC3-16(a) artifacts under the RFC3-16(c) two-state
  model; mission homes follow RFC3-15 discipline.
- **RFC 0005:** clients per RFC5-3/5/6; execution under RFC5-18 profiles;
  attribution per RFC5-25; consent/egress gates unbypassed (RFC10-6).
- **RFC 0006:** mission and attention data are served by the same semantic
  API with human/machine parity (RFC6-13/RFC6-14).
- **RFC 0008:** missions materialize work; work states, dispatch, and
  execution records remain RFC 0008's; lifecycle interaction reviewed
  before freeze (RFC10-5). Mission views consume **two fields** — the
  RFC8-12 normalized work state and the RFC8-28 chain state — never folded
  into one; no mission aggregate renders a closed item as done absent
  `reconciled@E` (RFC8-30), and `closed-unmerged` is never rendered as
  complete.
- **RFC 0011:** every mission-spawned agent run receives a governed context
  packet; the envelope is a mandatory packet input.

## 5a. Amendment log

**rev11 (2026-08-05) — the correction plane.** An adversarial safety review
found that RFC10-1..16 closed every *authority-widening* route it constructed
and left every *post-failure* question unanswered: `rollback`, `compensat`,
`revert`, `irreversib`, `resume`, `reserve` and `atomic` were all
zero-occurrence in this file. Six clauses were added (RFC10-17..22) and three
existing clauses amended in place — RFC10-6 (disagreeing evidence), RFC10-7
(`propose-only` defined; obligations fail closed), RFC10-11 (in-flight
completion funded from reservation). No existing clause was renumbered or
retired. Three of the added seams — reservation, adjudication, stop — bite
**today, under the propose-only cap**: a propose-only mission still spends
money, still declares itself complete, and still could not be reliably
stopped. The prior round's disposition of these as "inert until the cap
lifts" did not hold, and is recorded here rather than quietly dropped.

## 6. Alternatives considered (summary; this contract is new at rev10 and has no history file)

A fourth truth surface ("Missions" beside Polaris/Trajectory/Orrery) —
rejected: missions are operator authority over the same truth, not a new
truth class. A project-local orchestrator script as the architecture —
rejected by owner direction (OD-R10-1). Extending the workspace manifest
into portfolio governance — rejected: presentation state and typed authority
must not share one artifact (RFC10-15).

## 7. Deliberately deferred

Autonomy-level enumeration; mission-lifecycle freeze (both to surface
specification / OpenSpec review); workspace governance store home and
schema; attention-queue SLA and batching policy; checkpoint format; fleet
scheduling algorithms; all transport/language/packaging choices.

## 8. Open questions for acceptance

1. **Lifecycle × work-state review.** Does the owner accept RFC10-5's
   candidate lifecycle as the *working* vocabulary pending the OpenSpec
   review against RFC 0008's states, or require the review first?
2. **Autonomy levels.** The level vocabulary (propose-only … merge, deploy)
   is an open default fixed at surface specification; does the owner want a
   floor fixed now (e.g. nothing above open-PR before further act)?
3. **Workspace governance store.** Home and minimal schema — platform-level
   typed store, location to be proposed at surface specification.

---

*End of contract. Clauses RFC10-1..RFC10-22; no gaps, no retired numbers.*
