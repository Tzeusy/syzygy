---
id: RFC-0010
title: Mission Control and Autonomy Envelopes — the autonomy envelope, guardrail runtime, and human attention
status_source: owner-act-record
module: prevention-envelope-and-attention
clauses: "RFC10-7..RFC10-13, RFC10-22 (non-contiguous — see the package clause map)"
governs: [autonomy-envelopes, guardrails, attention-items, escalation]
applies_to: [mission-control, workspace, all-surfaces, machine-clients]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0005, RFC-0008]
tags: [autonomy, human-control, no-self-widening, escalation, prevention-plane]
---

# RFC 0010 — Mission Control: the autonomy envelope, guardrail runtime, and human attention

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — either owner-adopted (bootstrap,
uncorrelated) or Syzygy-verified, with the exact provenance state always
visible (RFC3-16). Absent such a record, this contract binds nothing.

**Package:** module 2 of 5 of the RFC 0010 contract package. Index, clause
map, lookup rule, package-level integration and deferrals: `README.md`.
Rationale, amendment history, and violation cases:
`../../history/RFC-0010-history.md` (non-normative).

**Serves:** VIS-4 (always-human decision classes), SEC-1..SEC-5; owner
direction OD-R10-2.

## 1. Scope of this module

The **prevention plane's core**: the autonomy envelope and its
narrowest-reading rule, with `propose-only` defined (RFC10-7); the
no-self-widening rule (RFC10-8); envelope act provenance (RFC10-9); the
guardrail policy runtime as distinct from semantic correctness (RFC10-10);
bound exhaustion (RFC10-11); decision-ready human attention (RFC10-12,
RFC10-13); and the bounded attention queue (RFC10-22).

## 2. The contract

### 2.1 The autonomy envelope

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
independent reviews**, including the **completion establisher and
effects-determination evaluator** (RFC10-18, RFC10-18(a)); **evidence and
reconciliation requirements**;
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
`.syzygy/**` and `openspec/**` **of the mission's declared target projects**
rendered unadopted (RFC3-16) — a path grant reaching another project's
checkout confers no authorship in that project's governed namespaces (the
content-keyed reasoning of RFC10-21, applied to the write side). It may **not**
cause any effect outside those two namespaces: no version-control push or
pull request, no merge, no deploy, no package or artifact publication, no
mutation of an external service or database, and no RFC5-22
destructive-operation class **whether or not the granted execution profile
standing-approved it**. Egress to a model provider remains permitted only
under an RFC5-14 consent record naming the provider and content classes.
**Consented provider disclosure and metered spend are effects in their own
recorded dimensions** — external disclosure and resource consumption
(RFC10-23) — pre-authorized by the consent record and the reserved budget;
a `propose-only` mission that disclosed content or spent budget is **never
rendered as having had "no effects"**, and the effects-applied predicate
that engages the correction plane (RFC10-18(a)) is scoped to the
external-mutation dimension, so the consented-egress grant requires no
irreversible-mutation class on the envelope's face and an egress-only
mission does not route to `failed` on that ground alone. A
level above `propose-only` is inoperative until both the vocabulary is
enumerated by owner act and each level's permitted effect set is stated
**by that same owner act — an OpenSpec requirement may specify behavior for
a level; it never fixes a level's permitted effect set**. Because this cap
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
children can never jointly exceed what the one owner act authorized. **The
debit covers attention allowance as it covers budget**: a child's maximum
outstanding attention count and maximum item rate (RFC10-22) are debited
from the parent's declared maxima at grant time under the same sibling-sum
invariant — one owner act never mints more outstanding attention demand
than its envelope declares. A derived child **inherits the parent's
declared completion establisher and effects-determination evaluator**
(RFC10-18, RFC10-18(a)): an establisher named by the deriving agent binds
nothing, and a child left without an inherited establisher never reaches
`completed`. Every child grant carries a **maximum time to first dispatch**
(RFC10-17(a)), so a grant held by a child that never starts is released,
never stranded. An
*attempted* self-widening is a violation: the mission transitions to
`blocked`, the attempt is recorded as evidence, and an Attention Item is
minted. **A violation item survives the mission**: park expiry may
terminate the mission (RFC10-5) and never resolves the item — an Attention
Item minted for a self-widening attempt terminates only in a recorded human
resolution or an explicit human dismissal (RFC10-13), persisting past the
mission's terminal record as a workspace-level attention fact, and the
terminal reason of a mission that expired with the item outstanding records
the violation as unresolved-at-expiry. Waiting clears nothing.

**RFC10-9.** The envelope, every amendment to it, and mission approval are
**authorization-bearing governance artifacts** under RFC3-16(a). Each is
honored only through an effective human owner act that is current,
attributable, scope-matched, and bound to the exact artifact digest under
RFC3-16(b). State (1), `owner-adopted (bootstrap, uncorrelated)`, and state
(2), `Syzygy-verified`, are both effective; every surface and API renders the
exact provenance state, and state (1) is never described as independently
verified. Mission approval and every envelope amendment remain exact human
acts: a machine-submitted record is not an act, and a failed, unavailable, or
indeterminate A1 attempt never creates state (1) or silently downgrades a
record claiming state (2). An absent, invalid, stale, revoked, superseded,
wrong-scope, or digest-mismatched act authorizes nothing, and the mission does
not leave `awaiting-approval`. No act may widen a child beyond its parent or
relax any other envelope, consent, execution, evidence, stop, recovery, or
escalation gate.

### 2.2 The guardrail policy runtime

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
never the wider claim. **For resource consumption this prevention is
discharged by RFC10-17's enforced-limit admission rule**: a mediated
dispatch or provider transmission is admitted only against an enforced
limit with remaining headroom, and refused otherwise. RFC10-17's recorded
`overrun` quantity is reachable only from the non-mediated sources that
clause enumerates — a declared unmediated surface, bounded telemetry lag,
or a provider's violation of its own limit — so this clause's MUST and
RFC10-17's ledger are both true at once: what Syzygy mediates cannot
conformingly overrun, and what it cannot mediate is visible, bounded, and
attributed. Every guardrail decision —
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

### 2.3 Human attention and escalation

**RFC10-12.** The **Attention Item** is a first-class identified entity of
RFC1-7's **mission extension profile** (minted by the control-plane service,
deterministic over the triggering condition and its mission) — a
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

### 2.4 The attention queue is bounded

**RFC10-22. The attention queue is bounded.** Every Attention Item
additionally carries an **urgency class** from a closed vocabulary fixed at
surface specification, and the **envelope bound, gate, or protected surface
it implicates** where one exists. Every envelope declares a **maximum
outstanding attention count** and a **maximum item rate** for the missions
under it; an undeclared maximum means one outstanding item — the narrowest
reading (RFC10-7). **On reaching either bound the mission pauses rather than
enqueueing further items**: a mission may not convert the owner's finite
attention into throughput.

**Exactly two classes of item are exempt from both bounds, and the
enumeration is closed.** **(i)** The item reporting that a bound was
reached, or the resulting state change — minted and delivered at the
maximum, because a safe behaviour the owner cannot be told about is, at the
queue, the unsafe one: at the default of one outstanding item the mission
would otherwise pause and be forbidden to say so. **(ii)** An item another
clause mandates **at or after a terminal transition** — RFC10-19's
irreversible-effect enumeration and RFC10-20(d)'s failed-stop enumeration —
because a terminal mission cannot take this clause's pause response, and
terminal duties may not be suppressed by a full queue. Both classes are
deduplicated like any other item. An exemption not in this enumeration
returns the queue to unbounded; adding one is an amendment to this clause,
never a reading of it.

**Where a mandated mint meets a full queue on a non-terminal mission, the
mandating clause's state prescription wins** — a self-widening attempt
still transitions to `blocked` under RFC10-8, never re-routed to `paused`
by this clause — and the mandated item is **held and minted when a slot
frees**: the hold is recorded as attributable evidence, disclosed in the
queue's own rendered state, and a held item is not a silent disappearance
(RFC10-13).

Items presenting the same decision are
deduplicated into one item recording its multiplicity. Every item's expiry
falls within a declared **maximum item expiry** beyond which its stated
default is no longer presumed safe; **an undeclared maximum item expiry
means the mission's remaining wall-clock budget at mint time** — wall-clock
is a budget, an undeclared budget is zero delegated wall-clock (RFC10-7),
so every runnable mission has this default and it is finite. An item whose
expiry exceeds the applicable maximum is not well-formed.
RFC10-13's anti-streaming rule bounds *granularity*; this clause bounds
*volume*, and without both, denial of owner attention is reachable without
widening anything.

## 8. Owner questions

*Package numbering; question numbers never shift. Full package index:
`README.md` §8.*

2. **Autonomy levels — OPEN.** The level vocabulary (propose-only … merge,
   deploy) is an open default fixed at surface specification; does the owner
   want a floor fixed now (e.g. nothing above open-PR before further act)?

---

*End of RFC 0010 module 2. Clauses RFC10-7 … RFC10-13 and RFC10-22 —
non-contiguous by design; the package README's clause map is the lookup
authority. Nothing merged, nothing retired.*
