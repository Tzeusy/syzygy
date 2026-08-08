---
id: RFC-0011
title: Context Compiler and Governed Context Packets — contract package index
status_source: owner-act-record
package: RFC-0011
modules: [packet-identity-provenance-and-memory, deterministic-selection-and-budget]
clauses: "RFC11-1..RFC11-16 (no gaps, no retired numbers) — distributed non-contiguously across two modules; the clause map below is the lookup authority"
implementation_boundary:
  kind: requires-openspec
  clause: RFC11-12
governs: [context-packets, context-selection, governed-memory, agent-profiles]
applies_to: [mission-control, context, all-surfaces, machine-clients]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008, RFC-0010]
tags: [context, provenance, memory, selection, agents]
---

# RFC 0011 — Context Compiler and Governed Context Packets (package index)

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
each module file's exact content digest — as an owner-adopted bootstrap act
until the independent A1 correlation mechanism exists, and as a
Syzygy-verified effective act only after correlation (RFC3-16). Absent such
a record, this contract binds nothing.

**Serves:** VIS-7/trust floor (what an agent saw is a provable fact, not a
guess); SEC-2 (deny-by-default context/tool grants); owner direction
OD-R10-3/OD-R10-4 (recorded in the rev10 owner-direction record, a
bootstrap process artifact retained with the delivery packet). New at
rev10 — no rev9 predecessor; split into a package at rev12 with clause text
preserved verbatim.

## Clause map and lookup rule

**Every clause identity appears in exactly one module.** One `RFC11-n`
namespace, no duplicated normative clauses, no renumbering. Clause numbers
are **not contiguous per module**: the package was split along the seam
between what a packet *is* and how its mandatory content is *selected*,
after the clauses were numbered, and clause identities are never
renumbered, so the map below — not range arithmetic — is the lookup
authority.

| Module | File | Clauses |
|---|---|---|
| 1 — packet identity, provenance, memory, profiles | `packet-identity-provenance-and-memory.md` | RFC11-1, RFC11-2, RFC11-3, RFC11-5, RFC11-6, RFC11-7, RFC11-8, RFC11-9, RFC11-10, RFC11-12 |
| 2 — deterministic selection and budget | `deterministic-selection-and-budget.md` | RFC11-4, RFC11-11, RFC11-13, RFC11-14, RFC11-15, RFC11-16 |

**Lookup rule (deterministic).** For any citation `RFC11-n`, find the one
row of the table whose clause list contains it. The table is exhaustive over
RFC11-1…RFC11-16 with no gaps and no duplicates. Modules are numbered for
reading order only — citations name clauses, never modules or sections.

**The seam, and the acceptance boundary.** Module 1 fixes what a Context
Packet **is** — its identity, immutability, execution-record binding, the
mandatory/suggested distinction, the incomplete-is-Unknown rule, the
no-second-truth-store rule, governed memory, agent profiles, and the phase
rule. Module 1 **does not claim deterministic selection is solved**: a
packet's honesty (exact inclusions, exact omissions, disclosed
incompleteness) is contractually fixed even while the selection policy that
fills it remains under repair. Module 2 fixes how the mandatory set is
**derived** — the deterministic selection inputs and the budget posture —
and is acceptable only when its rules can reproduce the blind golden
selection fixtures. References from module 1 to module 2's selection
semantics are staged until module 2 is accepted; until then a conforming
packet is compiled against module 1's identity and disclosure duties with
its selection basis stated.

Module sizes are deliberately not stated here; the current measurement
lives in the generated budget report `../../CONTEXT-BUDGET-REPORT.md`,
which is regenerated, never transcribed.

## 0. Reader's summary (non-normative)

No agent is ever told to "read all project documentation." Every governed
run — mission, plan, work item, review, query task — receives a **Context
Packet**: a versioned, immutable, digest-bound artifact stating exactly
which doctrine rules, contract clauses, requirements, policies, evidence,
decisions, and permissions the agent saw, what applicable material was
omitted and why, and under which evaluation instant. Mandatory context is
selected **deterministically** from graph and applicability rules; inference
may suggest more, never silently remove. The packet digest lands in the
resulting execution record, so "what did the agent know?" is answerable
forever. Chat transcripts are not project memory; durable memory is
governed artifacts.

## 1. Summary

This package fixes: packet identity and immutability (RFC11-1..3);
deterministic selection semantics and the incompleteness rule (RFC11-4..7);
governed memory boundaries (RFC11-8..9); the minimal agent/model profile for
routing (RFC11-10); the context-budget posture (RFC11-11); the OpenSpec
phase rule (RFC11-12); the implementation-boundary declaration every active
contract carries (RFC11-13); defined dependency traversal (RFC11-14);
doctrine/craft ownership metadata (RFC11-15); and clause-first `constrains`
consumption (RFC11-16). Storage engines, retrieval technology, and the
exact token-budget number are explicitly not chosen here.

## 2. Motivation and doctrine grounding

[Observed] The rev9 corpus offered no answer to "which context did this
agent receive?" — the packet gap named at rev10
adversarial finding F7 (a bootstrap process record retained with the
delivery packet) — and whole-corpus loading was the only
safe instruction, which OD-R10-3 rules an architecture problem. [Inferred]
Context selection is a **provenance** problem, not a convenience problem: an
execution record whose inputs are unrecorded cannot support the trust floor
(VIS-7), and an agent that silently dropped a constraint is indistinguishable
from one never given it. The optimization target, verbatim from the owner:
"minimum complete governed context required for one decision or work item,
not minimum document count."

## 4. Violation cases (non-normative)

1. *(RFC11-3)* A fleet worker is dispatched with "read `.syzygy/` and the
   RFCs, then implement" — no packet, no omission accounting.
2. *(RFC11-5)* A retrieval layer ranks a mandatory doctrine rule below its
   cutoff and drops it; the packet shows no omission because "the selector
   never saw it."
3. *(RFC11-2)* An execution record says "context: latest docs" with no
   packet digest; six weeks later nobody can establish which revision of the
   envelope the agent saw.
4. *(RFC11-6)* Two applicable policies contradict; the compiler picks the
   newer one silently and the packet renders complete.
5. *(RFC11-8)* A planning chat's conclusions are cited as project authority
   ("as agreed in the transcript") without promotion to a governed decision.
6. *(RFC11-9)* A packet containing observed-project code is sent to a model
   provider under a consent covering only metadata.
7. *(RFC11-10)* A review is routed to an agent whose profile lacks the
   independence property the review class requires, because fallback order
   ignored it.

## 5. Integration

- **RFC 0001/0002:** packets pin evaluations and as-of instants; packet
  facts and omissions are identified; Unknown is first-class (RFC11-6).
- **RFC 0003:** packet and memory homes follow governance-home discipline;
  the contract-index projection (RFC11-7) is rebuildable, never
  authoritative; effective-status inputs come from owner-act records under
  the RFC3-16(c) two-state model — a packet states correlation gaps
  honestly.
- **RFC 0004:** evidence references enter packets by identity; capture
  cadence limits are disclosed as staleness, not hidden.
- **RFC 0005:** packets respect scopes (RFC5-6), egress consent (RFC5-14),
  and secret exclusion (RFC5-16/17); compiler acts are attributable
  (RFC5-25).
- **RFC 0006:** packet contents are queryable through the same semantic API
  with human/machine parity (RFC6-13/RFC6-14).
- **RFC 0010:** the envelope is a mandatory packet input; incomplete-context
  escalation flows through Attention Items; profiles never widen envelopes.

## 6. Alternatives considered (summary; this contract is new at rev10 and has no history file)

Pure retrieval ("embed everything, let relevance decide") — rejected:
non-deterministic mandatory selection cannot support the trust floor.
Whole-corpus loading as the safe default — rejected by OD-R10-3. Manual
per-task reading lists — rejected: hand-maintained selection is the drift
RFC11-7 forbids. Keeping the contract in one file — rejected at rev12: the
stable packet/provenance contract and the still-unsatisfiable selection
policy shared one acceptance digest, so the mature half was held hostage by
the half under repair; the split is the package convention most contracts
already follow.

## 7. Deliberately deferred

Storage and retrieval technology; embedding/index formats; the numeric
token budget (policy default, evidenced in the load map); packet transport;
compiler scheduling; profile registry home.

## 8. Open questions for acceptance

Numbering is stable across the package and never shifts; each question's
full text lives in the module owning its clause.

| # | Subject | State | Lives in |
|---|---|---|---|
| q1 | Budget figure custody (RFC11-11) | **open** | `deterministic-selection-and-budget.md` §8 |
| q2 | Profile registry home (RFC11-10) | **open** | `packet-identity-provenance-and-memory.md` §8 |
| q3 | Promotion act granularity (RFC11-8) | **open** | `packet-identity-provenance-and-memory.md` §8 |

## Phase boundary

The phase rule **RFC11-12** binds the whole package: this contract fixes
context-compilation semantics and is not a specification of record from
which implementation work may be scheduled. The clause text is in
`packet-identity-provenance-and-memory.md` §2.5, and its
clause-to-requirement coverage matrix must cover **RFC11-1…RFC11-16 across
both modules**, not module 1 alone.

---

*End of RFC 0011 package index. Clauses RFC11-1 … RFC11-16, distributed
across two modules per the clause map; no gaps, no retired numbers.*
