---
id: RFC-0010
title: Mission Control and Autonomy Envelopes — budget reservation and release
status_source: owner-act-record
module: budget-reservation
clauses: "RFC10-17 with sub-clause RFC10-17(a) (see the package clause map)"
governs: [budgets, reservation, spend-accounting]
applies_to: [mission-control, workspace, machine-clients]
depends_on: [RFC-0002, RFC-0004, RFC-0005, RFC-0008]
tags: [budgets, reservation, unknown-fails-closed, prevention-plane]
---

# RFC 0010 — Mission Control: budget reservation and release

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — either owner-adopted (bootstrap,
uncorrelated) or Syzygy-verified, with the exact provenance state always
visible (RFC3-16). Absent such a record, this contract binds nothing.

**Package:** module 3 of 5 of the RFC 0010 contract package. Index, clause
map, lookup rule, package-level integration and deferrals: `README.md`.
Rationale, amendment history, and violation cases:
`../../history/RFC-0010-history.md` (non-normative).

**Serves:** VIS-2 (Unknown spend is never zero spend), VIS-4; SEC-2.

## 1. Scope of this module

Budget as **reservation bound to enforcement, not observation**: the six
accounted quantities, the resource-kind classification that fixes what
"hard" may honestly mean, the dispatch-time admission rule, independent
spend measurement, and the release table that guarantees no reservation is
held indefinitely (RFC10-17, RFC10-17(a)). This module is prevention-plane
material: it bounds what a mission can consume before anything goes wrong.
What happens *after* something goes wrong is module 4,
`effects-recovery-and-stop.md`, which this module's release table names
where a release depends on recovery duties having fired.

## 2. The contract

**RFC10-17. Budget is reserved, and reservation is enforcement, never
accounting alone.** Every budget in an envelope is accounted in six distinct
quantities: **authorized** (the owner act's figure), **reserved_remaining**
(committed at dispatch to work not yet complete, and not yet consumed),
**spent** (measured consumption), **released** (reserved-but-unspent,
returned on completion or termination), **overrun** (spend exceeding what an
enforced bound covers — see the residual rule below), and
**recovery_reserve** (carved out of `authorized` at approval time — or, for
a derived child mission, at grant time by the deriving record — and held
undispatchable so that RFC10-19's compensating actions are fundable after an
RFC10-11 exhaustion). **No work is dispatched without reserving its declared
maximum cost against the envelope at dispatch time**, and the admission
inequality is `reserved_remaining + spent ≤ authorized − recovery_reserve`,
checked at every dispatch and conserved by every consumption event — the
sibling-sum invariant RFC10-8 states for child missions, applied to every
dispatch. The budget bound RFC10-11 fires on is `authorized −
recovery_reserve`: work never dispatches into the reserve, and the reserve
is spendable only by RFC10-19's compensating actions. Work whose maximum
cost cannot be declared is not dispatchable under that budget.

**A reservation admits a dispatch only where it is bound to an enforced
limit.** A dispatch is admitted only where its declared maximum cost is
bound to an **enforced runtime limit at the launch gate** — RFC5-21's
enforced resource limits for the run — and, for model-provider
transmissions, to a **remaining-headroom predicate evaluated at the RFC5-15
choke point for every transmission**: a transmission whose declared
incremental cost exceeds the run's remaining reservation is refused at the
choke point, before egress. **At every measured consumption event,
`reserved_remaining` decreases and `spent` increases by the same amount,
atomically.** A declared maximum with no enforced limit admits nothing.

**Every budget names its resource kind, and the kind fixes what "hard" may
honestly mean:**

- **hard-enforceable** — a Syzygy choke point (the RFC5-21 launch gate, the
  RFC5-15 egress gate) can refuse the act that would exceed the bound
  *before it happens*. Only this kind supports autonomous dispatch without
  further condition.
- **provider-quota-enforceable** — an external provider enforces a
  provider-side limit at or below the delegated figure. Delegation requires
  the provider-side limit to be set, and its setting captured as evidence,
  before first dispatch.
- **monitoring-only** — consumption is measurable but not refusable at any
  choke point. A monitoring-only kind is never rendered as a hard bound and
  supports no autonomous dispatch on its own.
- **non-delegable** — no enforcement point or no reliable measurement
  exists. Consumption of this kind requires per-act human approval.

A delegated budget may be called **hard** only where its kind is
hard-enforceable or provider-quota-enforceable. For model-provider monetary
spend: use a provider-side hard limit where available; otherwise cap the
individual call and the remaining headroom at the launch/egress choke
point; where neither is enforceable, the kind is non-delegable.

**Where measured spend against a bound is Unknown (RFC8-19, RFC2-23), the
bound is treated as reached**: the mission transitions per RFC10-11 and an
Attention Item states the measurement gap — Unknown spend is never read as
zero spend.

**Overrun is a residual of the unmediated world, never a conforming
mediated outcome.** Under this clause a Syzygy-mediated act cannot
conformingly produce overrun: the act that would exceed an enforced limit
is refused (RFC10-10). `overrun` remains a first-class recorded quantity
because exactly three sources outside the mediated path can produce it:
(i) effects on a declared unmediated effect surface (RFC10-18(a));
(ii) measurement lag within a declared, bounded telemetry interval,
disclosed per resource kind — lag defers knowledge of spend, never its
ceiling, because the per-run enforced limit still bounds it; and (iii) a
provider's violation of its own enforced limit. Every overrun is recorded
as attributable evidence against the mission and mints its own Attention
Item; an overrun from any other source, or a mission record showing a
respected bound with unrecorded overrun, is a violation of this clause.

**Who measures, and who sizes.** `spent` is admitted from the execution
record of a Syzygy-launched profiled run (RFC5-18, RFC4-18..RFC4-21; RFC5-21
governs admissibility) or from an adapter-backed provider record (RFC 0004)
— **never from a self-report by the principal whose spend it is**, on the
same independence rule RFC10-18 states for completion. A principal's own
figure is evidence, never the measurement: the Unknown rule above closes
*absent* telemetry, and this limb closes *false* telemetry. The evidence
tier of `spent` is the admitting record's own tier and is disclosed with
the figure; where a cost is computed (token counts × rate table) it is
Inferred and renders as such (VIS-2) — prevention rests on the enforced
limit at the choke point, never on the ledger figure alone. The **declared
maximum cost** sizing a reservation is declared by the envelope or by the
dispatching authority, never by the worker being dispatched — **and the
dispatching authority inside a running mission is itself a
Mission-controlled component (RFC10-8), so its declaration binds only
through the enforced limit the launch gate places on the run**: a run
reaching its declared maximum is halted at the gate, not billed past it.
Chronic under-declaration renders as a recorded pattern of
halted-at-limit runs attributable to the declaring authority.

**RFC10-17(a). Every reservation has a stated release point.** Reserved
budget is *released* — returned to the envelope's available headroom, and for
a child mission to the parent's remaining envelope (RFC10-8) — at the points
below, and each release is recorded as attributable evidence stating the
quantity returned.

| The mission reaches | Reservation disposition |
|---|---|
| `completed` | released in full at the terminal record |
| `failed` | released in full **after** RFC10-19's compensating actions are attempted — their own cost is drawn from `recovery_reserve`, which is committed *before* they run, so recovery is never funded past an exhausted bound |
| `cancelled` | as `failed` |
| `expired` | as `failed` |
| `blocked` or `paused`, no applied effects | **held**, for no longer than RFC10-5's maximum park duration; released at the resulting transition to `expired` |
| `blocked` or `paused` after its Attention Item expires | the item's expiry takes its declared safe default (RFC10-12) — where that default parks or re-parks the mission, the park duration continues to bound the hold. The item's expiry alone releases nothing; the park duration is what ends the hold |
| `blocked` **with** applied effects | as above, and RFC10-19's duties fire at the expiry, not at the park |
| `draft`, `awaiting-approval`, or `approved` — a child mission holding a grant it has not yet run under | **held from grant time (RFC10-8), and bounded**: every child grant carries a **maximum time to first dispatch**, declared by the parent's envelope, defaulting to the parent's maximum park duration; at that maximum the child transitions to `expired` and its grant is released to the parent's remaining envelope. A grant held by a child that never starts is a reservation, and this row is its stated release point |
| the **parent** of outstanding child grants reaches any terminal state | the stop propagates to every derived child (RFC10-20(b)); each child grant is released at that child's resulting terminal record, to the parent's terminal accounting. No child grant survives its parent's terminal record except a reservation retained for a run that did not terminate, named under the row below |
| unrecoverable stop — RFC10-20 limb (b) not achieved | released at the stop record **except** for the runs that did not terminate, whose reservations are retained and **named individually**: a reservation may not be returned while the work it funds may still spend |

**No non-terminal state holds a reservation indefinitely** — parked,
pre-running, or otherwise. A runtime holding reservation past the
applicable maximum violates this clause, and so does a mission record
showing headroom that reserved work still holds. **`recovery_reserve` is
sized, not merely present**: each compensating action an envelope names
carries a **declared maximum cost** (RFC10-19), and `recovery_reserve` is
not less than the sum of those declared maxima over every effect class the
envelope permits; an envelope failing that inequality — including a
derived child grant with no recovery_reserve of its own — authorizes no
effect class that requires compensation.

---

*End of RFC 0010 module 3. Clause RFC10-17 with sub-clause RFC10-17(a) —
the package README's clause map is the lookup authority. Nothing merged,
nothing retired.*
