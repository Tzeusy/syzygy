---
id: RFC-0008
title: Trajectory (Work Surface) — the normalized work-state vocabulary, liveness, and cost
status_source: owner-act-record
module: state-vocabulary-and-cost
clauses: RFC8-12..RFC8-20 (no gaps, no retirements, no merges)
governs: [work-states, normalized-state-vocabulary, state-derivations, liveness, blocked-causes, cost-measures, telemetry]
applies_to: [trajectory]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006]
tags: [closed-vocabulary, state-machine, honest-absence, unknown-never-zero, no-effort-score, staleness-bound, sdr-5, sdr-6, sdr-11]
---

# RFC 0008 — Trajectory (Work Surface): state vocabulary, liveness, cost

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — either owner-adopted (bootstrap,
uncorrelated) or Syzygy-verified, with the exact provenance state always
visible (RFC3-16). Absent such a record, this contract binds
nothing.

**Package:** module 2 of 3 of the RFC 0008 contract package. Index, clause map,
lookup rule, package-level integration and deferrals: `README.md`. Rationale,
amendment history, rejected alternatives, and answered §8 questions:
`../../history/RFC-0008-history.md`.

**Serves:** VIS-1, VIS-2, VIS-5; SEC-2, SEC-3; architecture.md (typed
authority; the Genome-complete note); trust-and-evidence.md (the reservation of
`Inferred` for declared inference processes). Implements **owner rulings**
SDR-4, SDR-5, SDR-6, SDR-9, and resolves the work-ontology portion of SDR §5
q10.

---

## 0. Module scope and reader map (non-normative)

*If this section and a clause ever disagree, the clause wins.*

This module owns **the vocabulary every Trajectory rendering speaks**: the
closed thirteen-value normalized work state and its partitions (RFC8-12), a
derivation and an honest-absence behavior for every one of those values
(RFC8-13), the rule that raw provider status stays visible behind the lens
(RFC8-14), the prohibition on any normalized "done" (RFC8-15), liveness and the
declared staleness bound (RFC8-16), the closed blocked-cause taxonomy
(RFC8-17), cost as independent measures with no composite score
(RFC8-18/8-19), and the V0/V1 telemetry staging (RFC8-20). Read it to answer:
*what may this item's state be called, what does that word derive from, and
what must be said when it cannot be determined?*

Four rules carry most of the weight. The vocabulary is **closed at thirteen
values in three partitions** — eight live, one terminal, four state-local
absence values — and **no implementation may mint, spell, or force-fit a value
outside it** (RFC8-12; owner decision A8). The normalized state is **one of two
separate fields**, travelling always beside the RFC2-18 chain state defined
in module 3 (RFC8-28), never folded into it and never substituted for it —
separate, not orthogonal, because normalized `reconciled` is a projection of
the chain value `reconciled@E` (RFC8-12). `active` is **unrenderable
until a staleness bound is declared** (RFC8-16). And **no synthetic "effort"
number may ever be computed, rendered, or served** (RFC8-18).

**Security-bearing clause.** RFC8-12's substrate-to-normalized derivation
mapping is an **authorization-bearing governance artifact honored only under
RFC3-16(a)**: `.syzygy/governance/**` is writable by untrusted fleet workers,
and a mapping row projecting a custom substrate status into `ready` or `active`
would make the board and the endpoints report dispatch-eligible and live work
on the strength of a file no owner act authorized. RFC3-16(a)'s own example
list cites RFC8-12.

---

## 3. The contract

Clauses are numbered `RFC8-n` for stable citation. Amend in place; retire
rather than renumber.

### 3.5 The normalized state vocabulary

**RFC8-12.** Trajectory renders work through a **closed normalized state
vocabulary**, partitioned so the distinction between being in flight, being
finished with, and not being determinable stays legible:

- **eight live states** — `future`, `planned`, `ready`, `active`, `blocked`,
  `review`, `merged`, `reconciled`;
- **one terminal state** — `closed-unmerged`: the scheduler closed the item
  and no merge fact exists (RFC8-15). It is named here, in the contract,
  precisely so that no implementer has to name it: it is **never** `done`,
  `complete`, `finished`, or `resolved`, because "done" is exactly the word
  the closure fallacy needs (README §6, Alternatives considered; RFC8-30);
- **four absence values** — `state-undetermined`, `eligibility-undetermined`,
  `activity-undetermined`, `stale-or-dead`.

**Thirteen values, closed** *(partitioned closure ratified at acceptance —
owner decision A8, answering §8 q1)*, each with its derivation and
honest-absence behavior in RFC8-13. **The field renders no value outside this
list**, and no implementation may mint, spell, or force-fit one — a value the
contract never names can be neither carried verbatim on a machine answer
(RFC6-14) nor checked for parity, and RFC6-22/23 make the resulting
disagreement release-blocking under the trust floor. `unadopted draft` and
`dismissed by decision` are sibling *surface* states (RFC2-25; RFC8-8), never
members of it. Every value is a **per-evaluation derived projection**, never a
stored or editable field.

**The normalized state is a separate field from the chain state, and the two
are never substituted for one another.** The closure above binds *this* field
and closes nothing else. The **RFC2-18 chain state** (`merged`,
`reconciliation-pending`, `reconciled@E`, `unsatisfied`,
`contradiction-raised`, `Unknown(reason)`) is a **separate field with its own
closed vocabulary** (RFC8-28), carried beside the normalized state on every
rendering, filter, count, and machine answer, and **never folded into it**: an
item whose normalized state is `merged` may carry any of three chain states,
and rendering all three as normalized `merged` alone is exactly the merge
RFC2-17's word reservation forbids. Every consumer, RFC9-32's
work/construction overlay included, **conforms by consuming both fields and
rendering every value each field currently carries** — an addition to either
vocabulary crosses the seam without amending any consumer's contract, and a
value the consumer cannot render is a defect in the consumer, never a licence
to fold it into a neighbour. This clause is the conformance rule's single
home; README §5 restates it for orientation. [Inferred]

**Separate is not independent, and the difference bites at one value.** The
two fields are **not orthogonal**, and this clause does not claim they are:
the normalized value `reconciled` is **defined as** the chain value
`reconciled@E` (RFC8-13), so for that one value the normalized field is a
**projection of the chain field** and carries no information the chain field
lacks.
**Normalized `reconciled` never substitutes for the chain state.** The
argument RFC8-28 gives for carrying both fields — that normalized `merged` is
compatible with three chain states — is true of `merged` and false of
`reconciled`, and an implementer reasoning from that argument alone would
drop the chain state exactly where the verdict lives. Both fields are carried
on every element regardless of value; no value of either field licenses
dropping the other.

**Field qualification is mandatory on every machine answer.** Two values —
`merged` and `reconciled` — are spelled identically in the two vocabularies
while RFC6-14 requires both be carried verbatim beside each other. Every
machine answer, filter, count, and export therefore **names the field each
value belongs to**; a bare `merged` or `reconciled` with no field
qualification is not a conforming answer. It is the same collision hazard
RFC1-25(b) closes with its twelve-pair invariant for
`depends_on`/`depends-on`/`declared-dependency`, arising here in the one place
this package reproduces it.

**The normalized state is not a Claim** (RFC1-24; RFC2-5) *(ruled at
acceptance by owner decision B14, answering §8 q5)*: a derived rendering of
scheduler and repository facts, not a status claim about a capability, so it
carries no RFC2-5 two-level claim identity, no RFC2-25 tier, and no membership
in the observation record (RFC2-6). Its four absence values are therefore
**state-local** — never stamped with, counted among, or absorbed by an
aggregate of RFC2-24 Unknown reasons (RFC6-6); a board's
"`state-undetermined` ×12" must never contaminate the project's Unknown-reason
counts. For RFC6-14 label parity every machine answer carries the state value
**verbatim**, the raw substrate status it derives from (RFC8-14), and the
evaluation identity (RFC6-15); epistemic label, rendering tier, and Unknown
reason belong to the *claims* rendered beside the state, never to the state
itself.

**One carve-out, stated rather than left to collide: `reconciled`.** Seven
live values derive from scheduler and repository facts; `reconciled` derives
from a **reconciliation verdict claim** — RFC2-18's "positive status claim
requiring gate-backed Observed evidence" — and it is the one value in the
enum that is green-capable. Carried in the normalized field with the
non-Claim rule applied unqualified, it would arrive stripped of the RFC2-25
tier that is the sole licence for a positive claim and outside the immutable
observation record. So: **normalized `reconciled` renders only together with
the underlying verdict claim's RFC2-25 tier and its evaluation identity, read
from the chain field's `reconciled@E`, and never on its own.** It remains a
projection, not a second claim: it mints no RFC2-5 two-level claim identity
and no observation-record membership of its own, and the verdict claim the
tier belongs to is the chain field's. Where the tier or the evaluation
identity is not available, the normalized field does not render `reconciled`
— `merged` with the chain state beside it is the honest answer, which is
already V0's (RFC8-13; RFC8-29).

The substrate-to-normalized mapping is a **declared, versioned derivation
artifact** in the governance plane and a snapshot input (**RFC2-1 item 7** —
the observer/adapter/parser/policy version list; not item 8, which is
deterministic parsing configuration). It is an **authorization-bearing
governance artifact and is honored only under RFC3-16(a)** (policy-declaration
class): `.syzygy/governance/**` is writable by untrusted fleet workers (SEC-3's
actor class, extended to committed artifacts by the premise RFC3-16(a)
states), and a mapping row projecting a custom substrate status into `ready`
or `active` would make the board and the endpoints report dispatch-eligible
and live work on the strength of a file no owner act authorized. Substrate
statuses are read from the tool, verbatim, per RFC4-15.

**RFC8-13.** The derivations. Every value RFC8-12 enumerates has a row here,
and every row states its honest-absence behavior. **Live states:**

| State | Meaning | Derivation | Honest absence |
|---|---|---|---|
| `future` | Approved execution intent, pre-materialization | `.syzygy/work/**`: Proposal approved or queued-for-materialization; no materialization record | Sub-state (approved vs queued, queue order) always visible; drafted proposals are *unadopted draft*, not `future`. **Exclusivity binds here:** two proposals in one exclusivity group never render as parallel `future` work and never sum into one remaining-work total — the honest render is *N candidate futures*, selectable one at a time (RFC1-27; RFC6-24), and a scenario context naming both resolves `incompatible-scenario` (RFC6-5) |
| `planned` | Materialized, open, not dispatch-eligible | Scheduler read: open with unmet dependency edges, or deliberately frozen (`deferred`/equivalent, with its reason) | Frozen-vs-dependency distinction rendered; an unreadable dependency set renders `eligibility-undetermined`, not `planned` |
| `ready` | Open, unblocked, dispatch-eligible | A derived query at the answering evaluation **over snapshot inputs only** — the work-state export captured in the snapshot (RFC2-1 item 3) plus RFC4-15's dependency feed — recomputed per evaluation, never cached as truth. **No implementation may invoke the substrate's live readiness computation at answer time**: a source not identified in the snapshot must not influence that evaluation's answers (RFC2-2), and calling a substrate whose state has moved defeats RFC2-3's identity test on re-run — the same rule RFC2-18 states for chain states | A ready-set without its evaluation identity is not a ready-set; where the work-state export or the dependency feed is uncaptured, the item renders `eligibility-undetermined`, never `ready` |
| `active` | Claimed, with current progress | Claimed (in-progress + assignee) **and** a progress signal — branch tip moved, new commit, PR state changed — within the declared staleness bound (RFC4-23) | See RFC8-16: no declared bound ⇒ `activity-undetermined`; signal older than the bound ⇒ `stale-or-dead`; never `active` in either case |
| `blocked` | Open, waiting on something nameable | Substrate blocked/waiting status, dependency edges, gates | Carries its blocked-cause **set** — every cause whose declared derivation resolves — or cause-Unknown where none does (RFC8-17) |
| `review` | An open review lane bound to an exact head SHA | Open PR facts (hosting sub-adapter) + review work item/labels + `external_ref` | Lane-open is derivable; **reviewer activity is never claimed** (a review lock label is a lock, not liveness); a merge-readiness verdict binds to its head SHA and expires when the head moves |
| `merged` | The change reached the integration branch | **A VCS merge fact only** (RFC4-11) — never inferred from scheduler closure | Execution state: never done, never green; enters the RFC2-18 chain as `reconciliation-pending` at the evaluation that first captures the merge fact |
| `reconciled` | `reconciled@E` per RFC2-18 | A reconciliation verdict claim, gate-backed Observed (RFC2-25), rendered with its evaluation identity | V0: never renders (`accounting-reconciliation-and-release.md` §3.14); merged-but-unreconciled renders "reconciliation evidence absent / Unknown" |

**Terminal state:**

| State | Meaning | Derivation | Honest absence |
|---|---|---|---|
| `closed-unmerged` | The scheduler closed the item and no merge fact exists — abandoned, superseded, deduplicated, or unexplained | Scheduler read: item closed (RFC4-15) **and** no VCS merge fact joins to it (RFC4-11/RFC4-22). Closure alone never derives `merged`, and this state never derives `reconciled` | The substrate's closure reason renders **verbatim**; where the substrate recorded none, the reason renders Unknown citing the substrate's silence — never guessed. Never `done`, `complete`, or green (RFC8-15/8-30); the closure event stays queryable execution history, and a `closed-unmerged` item is never counted among satisfied, reconciled, or completed work |

**Absence values** (state-local per RFC8-12 — never RFC2-24 Unknown reasons):

| Value | Meaning | Derivation | Honest absence |
|---|---|---|---|
| `state-undetermined` | The declared mapping has no row for this item's raw substrate status | The verbatim substrate status (RFC4-15) falls outside the declared substrate-to-normalized mapping (RFC8-12/8-14) | Raw status always rendered and queryable beside it; the item is never dropped and never force-fitted into a neighbouring state. Resolution: amend the declared mapping, honored only under RFC3-16(a) |
| `eligibility-undetermined` | Materialized and open; dispatch-eligibility could not be computed | The dependency set or the work-state export needed to decide `planned` vs `ready` was not readable at the answering evaluation — adapter degraded (RFC4-15), uncaptured (RFC2-2), or lost past the retention horizon (RFC4-16) | The open fact is never suppressed and the item never renders `ready` or `planned` on a guess; the render cites *what* could not be read, and where the cause is a retention event it cites that event (RFC8-24) |
| `activity-undetermined` | Claimed, but no staleness bound is declared, so no signal can count as current | A claim fact exists and RFC4-23's staleness bound is undeclared — RFC2-9's mechanics applied to liveness | `active` is **unrenderable** until the bound is declared (RFC8-16). The claim fact and its instant still render; resolution is a governance act — declare the bound — not fresh evidence |
| `stale-or-dead` | Claimed; the last progress signal is older than the declared staleness bound | A claim fact plus a last-signal instant older than the declared bound (RFC4-23) | The last-signal instant is always shown; never `active`, never green. The coordinator heartbeat, lock labels, and worktree existence are never admissible as signal (RFC8-16) |

**RFC8-14.** **Raw provider status stays visible and queryable** behind every
normalized state, substrate-qualified (RFC4-6): the normalized state is a
lens, never a replacement. A substrate status the declared mapping does not
cover (`pinned`, `hooked`, a custom status) renders its raw status with
normalized state **`state-undetermined`** (resolution: amend the declared
mapping, honored only under RFC3-16(a)) — never dropped, never force-fitted.
`state-undetermined` is a **state-local absence value**: it is not the RFC2-24
Unknown reason `missing-declaration`, is never stamped with one, and is never
counted among a project's Unknown-reason totals (RFC8-12; RFC6-6). *(Confirmed
at acceptance — owner decisions A5 / B15, answering §8 q7: no new RFC2-24
reason is minted; where a **claim** depends on the missing mapping, its reason
stays #1 `missing-declaration`.)*

**RFC8-15.** **Closure is not a normalized "done."** Scheduler closure without
a merge fact (abandoned, superseded, deduplicated, unexplained) renders as the
terminal state **`closed-unmerged`** (RFC8-12/8-13) with the substrate's
reason verbatim — never `merged`, never `reconciled`, never green (RFC2-20),
and never under any label meaning done, complete, finished, or resolved.
Closure *with* a merge fact renders `merged` and enters the reconciliation
chain; the closure event stays queryable execution history.

### 3.6 Activity and liveness

**RFC8-16.** `active` requires a **progress signal within a declared staleness
bound** (bound value: quality-policy material; the obligation to declare is
binding — RFC4-23(2), **including that clause's requirement that the bound be
honored only through an effective owner act under RFC3-16(a)**: a valid
state-(1) or state-(2) act is effective with state rendered, while a
worker-minted bound with a missing or invalid act leaves this clause's floor
exactly where an undeclared one does). Until the bound is declared,
`active` is unrenderable: claimed items render **`activity-undetermined`** on
RFC2-9's mechanics applied to liveness (the condition RFC2-24 reason
`no-currency-bound-declared` names for claims; the *state* value is
state-local per RFC8-12, never that reason, never counted among a project's
Unknown-reason totals — RFC6-6). Between signals, worker liveness renders
**Unknown**; past the bound, **`stale-or-dead` with the last-signal instant
shown** — never `active`, never green. **Never admissible as liveness:** the
coordinator heartbeat (coordinator-claim only), lock labels, worktree
existence (RFC4-23) [Observed: substrate audit — workers never heartbeat in
the initial substrate].

### 3.7 Blocked causes

**RFC8-17.** `blocked` carries **a cause set** drawn from the **closed
taxonomy** {`dependency`, `pr-wait`, `external`, `decision`}, each a
**declared derivation**: `dependency` from unmet work-item dependency edges;
`pr-wait` from an open PR awaiting review or corrections (`external_ref` +
PR/review state); `external` from a declared external event (CI in flight,
timer or substrate gate); `decision` from a pending human gate, owner
decision, or adjudication (an unresolved contradiction renders here, the
conclusion Unknown per RFC2-15).

**The set is every cause whose declared derivation resolves, not one of
them.** A work item genuinely blocks on several things at once — an unmet
dependency edge *and* an open PR awaiting review satisfy two declared
derivations — and a single-valued cause forces an implementation to pick,
which sends the owner to clear a blocker that was never the whole blockage.
Every resolving cause renders, and every rendering, filter, count, and machine
answer carries the set (RFC6-14), never a chosen member of it. Where the
substrate conflates causes and **no** declared derivation resolves — the empty
set — the item renders **blocked with cause Unknown**; cause-Unknown is
reserved for that case and is never mixed into a non-empty set. The blocked
fact is never suppressed and a cause is never guessed.

### 3.8 Cost without an effort score

**RFC8-18.** Cost renders as **independent measures, never a composite**. The
V1 measure set (each with declared source and evidence class; the list is
amendable here, **the independence rule is not**): estimated effort and
declared complexity tier (**`declared-only`**, RFC2-25 — the declaration is
Observed, its accuracy Unknown, and **never `Inferred`**, which doctrine
reserves for a declared inference process carrying inference provenance
[Observed: trust-and-evidence.md] and which RFC2-7 requires to record model,
version, parameters, and exact inputs, none of which a human judgment has;
filing owner estimates in the inference plane would also render them Unknown
on any project without model-provider consent — the common proving-ground
case, RFC2-7/SEC-2 — and leave them with RFC2-8/RFC1-22 challenge authority
only, in place of a governance-plane declaration's standing); lead time;
active compute time; blocked time (split by RFC8-17 cause where history
supports it — and where an interval carries more than one resolving cause the
split discloses that, never attributing the interval to one member of the
set); input tokens; output tokens; billed or derived API cost
(derived-from-rates is Inferred, labeled — RFC4-21); attempts (countable only
from Execution Records, RFC4-20); review rounds; CI time; rework; touched
files/components/interfaces (from VCS; component granularity resolves through
the **declared implementation mapping** — a governance-plane artifact, RFC1-16
class (i), declared at RFC4-26/SDR-4; RFC 0009 consumes it and does not own
it). **No synthetic "effort" number may be computed, rendered, or served** —
collapsing independent measures is the error doctrine rejects for maturity
[Observed: architecture.md, Genome-complete note].

**RFC8-19.** **Absent means Unknown, never zero** (SDR-6; RFC2-23). Every
aggregate over partially-known measures discloses coverage ("cost known for n
of m runs") and never renders as a complete total (RFC4-21). A
predominantly-Unknown cost pane on the initial substrate is the correct
output, not a defect (VIS-1, VIS-2) [Observed: substrate audit — six of
thirteen measures are recorded nowhere today].

### 3.9 Telemetry staging (SDR-5)

**RFC8-20.** **V1** renders structured, **post-hoc** execution telemetry
exclusively from captured Execution Records (the RFC4-19 run envelope):
per-run model/runtime, timing, tokens/cost, attempts, gate outcomes at their
RFC2-25 tiers, parent/child run structure — absent fields Unknown. **Deferred
entirely**: terminal-grade streaming, live intervention, and control
[Observed: SDR-5; vision.md eventual mandate — live views never contribute to
status claims]. **V0** renders what the derivation-first adapters provide
(RFC4-28) and the rest Unknown; nothing at V0 may simulate telemetry.

---

## 4. Violation cases

*Package numbering; cases are distributed to the module owning their clauses
and are never renumbered. Cases 4 and 12 span modules and are held in
`README.md` §4.*

5. *(RFC8-13/16)* A dead worker renders `active` because the coordinator
   heartbeat is fresh and the worktree exists; `active` with no declared bound.
6. *(RFC8-13/15)* `merged` derived from scheduler closure; a `pinned` item
   dropped because the mapping had no row for it.
7. *(RFC8-17/18/19)* A blocked cause guessed from a title; a single
   "effort: 7.2" score; a cost total silently treating Unknown runs as zero.
13. *(RFC8-12/13/15)* A closure-without-merge rendered as `done`, `complete`,
    or a value the contract never names; a stale-or-dead item force-fitted
    into `blocked` because the board had no column for it.

---

## 5. Integration — this module

**Relies on RFC 0001:** the declared implementation mapping as a
governance-plane artifact, class (i) (RFC1-16), through which RFC8-18's
touched-components measure resolves; the non-Claim reading's grounding
(RFC1-24); challenge authority in the inference plane (RFC1-22). **RFC 0002:**
the label+tier+reason vocabulary rendered verbatim (RFC2-24/25, including
`declared-only`); snapshot closure, the uncaptured-source rule, and the
identity test (RFC2-1/2/3), with the derivation mapping and every declared
policy value entering as **RFC2-1 item 7** and the work-state export as item 3;
lawful tier degradation (RFC2-4); two-level claim identity and observation-record
membership, which the normalized state deliberately does **not** take on
(RFC2-5/2-6); currency mechanics applied to liveness (RFC2-9); the Unknown
rendering of a conclusion suspended pending adjudication (RFC2-15); the word
reservation (RFC2-17) and the chain states (RFC2-18/2-19); closure never
rendering as done (RFC2-20); degradation states (RFC2-23); the inference-overlay
requirements and consent boundary that keep declared estimates out of the
inference plane (RFC2-7, RFC2-8). **RFC 0003:** quality-policy material
(RFC3-15); **the owner-act provenance predicate governing the
substrate-to-normalized derivation mapping (RFC3-16(a))**. **RFC 0004:**
substrate-qualified raw status (RFC4-6); VCS merge facts, never scheduler
closure (RFC4-11); the `gate-backed` provenance predicate (RFC4-13); the
faithful scheduler feed read verbatim (RFC4-15); capture-before-horizon
(RFC4-16); the run envelope and its class-O prose fields (RFC4-19); attempts
countable only from Execution Records (RFC4-20); derived-rate cost labeling
(RFC4-21); join bases (RFC4-22); liveness honesty and the staleness bound,
honored only under RFC3-16(a) (RFC4-23, incl. RFC4-23(2)); the capability
mapping's declaration site (RFC4-26); the derivation-first adapter posture
(RFC4-28). **RFC 0006:** the closed navigation-outcome set incl.
`incompatible-scenario` (RFC6-5); outcomes are not Unknown reasons, the rule
this module applies to its four absence values (RFC6-6); label parity and
verbatim state carriage on every machine answer (RFC6-14); evaluation stamping
(RFC6-15); trust-floor parity between two renderings over one declared scope
(RFC6-22/23); scenario context (RFC6-24).

**Provides to RFC 0009:** the **normalized work state** half of the two-field
handoff RFC9-32 consumes — RFC8-12/8-13's closed vocabulary, at present
thirteen values in three partitions, not eight. The other half is the RFC2-18
chain state (RFC8-28, module 3); the **conformance rule binding both halves**
is stated once, at **RFC8-12** (README §5 restates it), and a consumer
conforms only by consuming both fields. **To RFC 0010:** the work-state vocabulary and liveness rules a
Mission lifecycle must interoperate with, and the cost measures a Mission
budget is accounted in.

---

## 7. Deliberately deferred — this module

Staleness bound, retention bound, and measure **values** → quality/evidence
policy. Only the *values* defer: the obligation to declare each is binding
here, and until a staleness bound is declared `active` is unrenderable
(RFC8-16). Live streaming, intervention, and control → deferred with telemetry
as their entry criterion (SDR-5); nothing at V0 may simulate telemetry
(RFC8-20). Board and queue presentation → craft, subject to the non-deferring
layout obligation in `README.md` §7.

---

## 8. Owner questions

*Package numbering; question numbers never shift. Answered items keep their
number here and their full text and reasoning live in
`../../history/RFC-0008-history.md` §8. Full package index: `README.md` §8.*

1. **Vocabulary closure (RFC8-12/13).** **ANSWERED — owner decision A8:** the
   partitioned closure is accepted — thirteen values in three partitions
   (eight live, one terminal `closed-unmerged`, four state-local absence
   values), each with a derivation row. See
   `../../history/RFC-0008-history.md` §8 q1.
3. **Blocked-time cause split (RFC8-18) — OPEN.** The split needs transition
   history the substrate GCs away (RFC4-16); until capture cadence is settled
   it renders Unknown for most items. Worth its capture obligation at V1, or an
   enrichment-roadmap item (RFC4-29)?
5. **Epistemic class of the normalized state (RFC8-12).** **ANSWERED — owner
   decision B14:** a derived rendering, not a Claim; it carries its own
   separately-counted absence values rather than RFC2-24 Unknown reasons. See
   `../../history/RFC-0008-history.md` §8 q5.
7. **The unmapped-substrate-value rendering (RFC8-14).** **ANSWERED — owner
   decisions A5 / B15, read with A8 / B14:** no new RFC2-24 reason is minted;
   the board field renders `state-undetermined`, and where a *claim* depends on
   the missing mapping its reason stays #1 `missing-declaration`. See
   `../../history/RFC-0008-history.md` §8 q7.

---

*End of RFC 0008 module 2. Clauses RFC8-12 … RFC8-20, contiguous — no gaps,
nothing merged, nothing retired.*
