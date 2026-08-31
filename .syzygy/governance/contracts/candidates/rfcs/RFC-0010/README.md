---
id: RFC-0010
title: Mission Control and Autonomy Envelopes — contract package index
status_source: owner-act-record
package: RFC-0010
modules: [mission-identity-approval-and-lifecycle, prevention-envelope-and-attention, budget-reservation, effects-recovery-and-stop, portfolio-and-cross-project-consent]
clauses: "RFC10-1..RFC10-24 (sub-clauses RFC10-17(a), RFC10-18(a), RFC10-19(a); no gaps, no retired numbers) — distributed non-contiguously across five modules; the clause map below is the lookup authority"
implementation_boundary:
  kind: requires-openspec
  clause: RFC10-16
governs: [missions, autonomy-envelopes, guardrails, attention-items, workspace-governance, service-boundary]
applies_to: [mission-control, workspace, all-surfaces, machine-clients]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008]
tags: [autonomy, human-control, budgets, escalation, platform]
---

# RFC 0010 — Mission Control and Autonomy Envelopes (package index)

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
each module file's exact content digest — either owner-adopted (bootstrap,
uncorrelated) or Syzygy-verified, with the exact provenance state always
visible (RFC3-16). Absent such a record, this contract binds nothing.

**Serves:** VIS-4 (always-human decision classes), VIS-5 (adapter
authorization), SEC-1..SEC-5; owner direction OD-R10-1/OD-R10-2 (recorded
in the rev10 owner-direction record, a bootstrap process artifact retained
with the delivery packet). New at rev10 — no rev9 predecessor; split into a
package at rev12 with clause text preserved verbatim. **Amendment history,
rationale, and violation cases:** `../../history/RFC-0010-history.md`
(non-normative).

## Clause map and lookup rule

**Every clause identity appears in exactly one module.** One `RFC10-n`
namespace, no duplicated normative clauses, no renumbering. Clause numbers
are **not contiguous per module**: the package was split along the
prevention/correction seam after the clauses were numbered, and clause
identities are never renumbered, so the map below — not range arithmetic —
is the lookup authority.

| Module | File | Clauses |
|---|---|---|
| 1 — platform boundary, mission identity, approval, lifecycle | `mission-identity-approval-and-lifecycle.md` | RFC10-1, RFC10-2, RFC10-3, RFC10-4, RFC10-5, RFC10-6, RFC10-14, RFC10-16, RFC10-24 |
| 2 — autonomy envelope, guardrail runtime, attention | `prevention-envelope-and-attention.md` | RFC10-7, RFC10-8, RFC10-9, RFC10-10, RFC10-11, RFC10-12, RFC10-13, RFC10-22 |
| 3 — budget reservation and release | `budget-reservation.md` | RFC10-17, RFC10-17(a) |
| 4 — completion adjudication, effects, recovery, stop | `effects-recovery-and-stop.md` | RFC10-18, RFC10-18(a), RFC10-19, RFC10-19(a), RFC10-20, RFC10-23 |
| 5 — portfolio authority, cross-project consent | `portfolio-and-cross-project-consent.md` | RFC10-15, RFC10-21 |

**Lookup rule (deterministic).** For any citation `RFC10-n`, find the one
row of the table whose clause list contains it; lettered sub-clauses live
with their parents. The table is exhaustive over RFC10-1…RFC10-24 with no
gaps and no duplicates. Modules are numbered for reading order only —
citations name clauses, never modules or sections.

**The two planes, and the acceptance seam.** Modules 1, 2, 3 and 5 are the
**prevention plane**: they make out-of-envelope Syzygy-mediated acts
impossible before they happen — including spend, which module 3 bounds by
reservation at dispatch. Module 4 is the **correction plane**: what happens
after something goes wrong — adjudication, compensation, recovery, stop.
The two planes are independently acceptable: a propose-only mission posture
(RFC10-7's cap) is safe under the prevention plane alone, because the only
effects it can cause are drafts inside the two governed namespaces,
consented provider disclosure, and reserved spend — each bounded by modules
1–3 and 5. Effect-bearing autonomy levels are inoperative until the
correction plane is accepted *and* the autonomy-level vocabulary is
enumerated by owner act. Cross-module references from the prevention plane
into module 4 (the release table's recovery hooks, RFC10-18 naming in
lifecycle text) are **staged references**: they bind when module 4 is
accepted and, until then, mark duties that cannot yet arise because no
effect class that would trigger them is authorized.

Module sizes are deliberately not stated here; the current measurement
lives in the generated budget report `../../CONTEXT-BUDGET-REPORT.md`,
which is regenerated, never transcribed.

## 0. Reader's summary (non-normative)

A human approves one bounded **Mission**; agent fleets then plan, execute,
verify, re-plan, and recover inside an approved **autonomy envelope** they can
never widen, until the mission ends or a terminal condition fires. Mission
Control is a workspace-level operator domain over the same one canonical
Syzygy service and semantic API that serves Polaris, Trajectory and Orrery —
**not** a fourth project truth surface. Human attention arrives as
decision-ready **Attention Items**, never event streams. Portfolio authority
lives in a typed **workspace governance store** that can never override
project-internal truth.

## 1. Summary

This package fixes: the platform boundary (one service, one semantic API,
many clients — RFC10-1..3); Mission identity and lifecycle (RFC10-4..6); the
autonomy envelope and the no-self-widening rule (RFC10-7..9); the guardrail
runtime as distinct from semantic correctness (RFC10-10..11); attention and
escalation (RFC10-12..13); project-bound versus portfolio missions and the
workspace governance store (RFC10-14..15); the OpenSpec phase rule
(RFC10-16); budget reservation and release (RFC10-17, RFC10-17(a));
independent completion adjudication and the independently established
effects-applied determination (RFC10-18, RFC10-18(a)); effect reversibility,
recovery and sibling disposition (RFC10-19, RFC10-19(a)); what stop
guarantees (RFC10-20); cross-project consent composition (RFC10-21);
attention-queue bounds (RFC10-22); separately recorded effect dimensions
(RFC10-23); and the doctrine precondition on operation (RFC10-24). Autonomy
level enumerations, lifecycle
freeze, store schema, and all transport/language/packaging choices are
explicitly deferred (§7, §8).

## 2. Motivation and doctrine grounding

Doctrine holds that Syzygy is not an unattended reconciler by default and
that certain decision classes are always human (VIS-4). The owner's settled
direction (OD-R10-2) adds: a human may deliberately approve one **bounded
mission** rather than one work item at a time — high-level human control,
not silent default autonomy. [Observed] Nothing in RFCs 0001–0009 gives that
act a home: work is one-item-grained (RFC 0008) and the workspace manifest
is presentation-only (RFC 0003). This package supplies the missing
authority shape without weakening the doctrine posture. Owner ruling
`BOUNDED-MISSION-DOCTRINE-INTERPRETATION-2026-08-31` records that exact
human-approved missions and envelopes satisfy doctrine's human-triggered
boundary, as RFC10-24 now states. The ruling does not accept this candidate,
sign its required OpenSpec behavior, or approve a mission; operation remains
unavailable until those independent gates and every mission gate pass.

## 4. Violation cases

**Moved to `../../history/RFC-0010-history.md` §"Violation cases"** —
twenty-one worked scenarios, one per clause, each naming the escape it
closes. They are non-normative teaching examples.

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

`../../history/RFC-0010-history.md` (Tier 2, non-normative) holds the
rev11, rev11a and rev11b entries in full, and the rev12 package-split
entry. An amendment log records how the contract got here; it is not part
of what the contract says.

## 6. Alternatives considered (summary; full rationale in the history file)

A fourth truth surface ("Missions" beside Polaris/Trajectory/Orrery) —
rejected: missions are operator authority over the same truth, not a new
truth class. A project-local orchestrator script as the architecture —
rejected by owner direction (OD-R10-1). Extending the workspace manifest
into portfolio governance — rejected: presentation state and typed authority
must not share one artifact (RFC10-15). Keeping the contract in one file —
rejected at rev12: twenty-two clauses and three sub-clauses across two
planes had reached the per-module word ceiling, every amendment displaced
non-normative text, and the single file coupled the mature prevention plane
to correction-plane findings still under repair; the split is the package
convention seven of eleven contracts already follow.

## 7. Deliberately deferred

Autonomy-level enumeration; mission-lifecycle freeze (both to surface
specification / OpenSpec review); workspace governance store home and
schema; attention-queue SLA and batching policy; checkpoint format; fleet
scheduling algorithms; all transport/language/packaging choices.

## 8. Open questions for acceptance

Numbering is stable across the package and never shifts; each question's
full text lives in the module owning its clause.

| # | Subject | State | Lives in |
|---|---|---|---|
| q1 | Lifecycle × work-state review (RFC10-5) | **open** | `mission-identity-approval-and-lifecycle.md` §8 |
| q2 | Autonomy levels (RFC10-7) | **open** | `prevention-envelope-and-attention.md` §8 |
| q3 | Workspace governance store (RFC10-15) | **open** | `portfolio-and-cross-project-consent.md` §8 |

## Phase boundary

The phase rule **RFC10-16** binds the whole package: this contract fixes
mission-control semantics and is not a specification of record from which
implementation work may be scheduled. The clause text is in
`mission-identity-approval-and-lifecycle.md` §2.4, and its
clause-to-requirement coverage matrix must cover **RFC10-1…RFC10-24 across
all five modules**, not module 1 alone.

---

*End of RFC 0010 package index. Clauses RFC10-1 … RFC10-24 with sub-clauses
RFC10-17(a), RFC10-18(a), RFC10-19(a), distributed across five modules per
the clause map; no gaps, no retired numbers.*
