---
id: RFC-0011
title: Context Compiler — deterministic selection and the budget posture
status_source: owner-act-record
module: deterministic-selection-and-budget
clauses: "RFC11-4, RFC11-11, RFC11-13..RFC11-16 (non-contiguous — see the package clause map)"
governs: [context-selection]
applies_to: [mission-control, context, machine-clients]
depends_on: [RFC-0002, RFC-0010]
tags: [context, selection, determinism, budgets, fail-closed]
---

# RFC 0011 — Context Compiler: deterministic selection and the budget posture

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — as an owner-adopted bootstrap act until
the independent A1 correlation mechanism exists, and as a Syzygy-verified
effective act only after correlation (RFC3-16). Absent such a record, this
contract binds nothing.

**Package:** module 2 of 2 of the RFC 0011 contract package. Index, clause
map, lookup rule, package-level integration and deferrals: `README.md`.

**Serves:** VIS-7 (deterministic identity), SEC-2; owner direction
OD-R10-3/OD-R10-4.

## 1. Scope of this module

How a packet's **mandatory set is derived**: the deterministic selection
inputs (RFC11-4), the implementation-boundary declaration every selected
contract must carry (RFC11-13), the traversal rules (RFC11-14), doctrine
and craft ownership metadata (RFC11-15), clause-anchored constraint
consumption (RFC11-16), and the context-budget posture with the
non-shardable core (RFC11-11). This module is acceptable only when its
selection rules can reproduce the blind golden selection fixtures — the
acceptance criterion is stated with the fixtures, not here, because a
criterion inside its own subject cannot gate it.

## 2. The contract

**RFC11-4.** **Mandatory context is selected deterministically** — same
inputs, same selection — from, at minimum: stable entity and relation
identities in the objective's scope; the work/mission warrant; affected
capabilities and components; contract dependencies (`depends_on`,
traversed under RFC11-14) and clause-anchored cross-contract constraints
(`constrains`, consumed under RFC11-16); explicit `applies_to` and
clause-level metadata (the contract-index projection — a rebuildable
RFC11-7 projection of the governed artifacts' own front matter and clause
text); declared doctrine and craft ownership metadata (RFC11-15); the
declared risk and change class; and the active state/evaluation. The
selection rule set is versioned with the compiler (RFC11-1's version
identity). The mandatory set always includes, for every selected contract,
**what that contract's implementation-boundary declaration names
(RFC11-13)**, consumed from the contract's own index and recorded in the
packet: the declared kind and named clause, always; and, where the declared
kind is `requires-openspec` **and the task itself sits on that boundary** —
authoring or scheduling observable behavior at the OpenSpec seam — the
module **defining** the named phase-rule clause. An index's restatement of
a phase rule is never the clause: the restatement points, the defining
module carries. A packet that selects a contract without loading its index
records the declaration verbatim together with the digest of the index it
was read from. A selector never searches for a clause class a contract does
not claim to have; a selected contract with no implementation-boundary declaration
renders the packet **incomplete under RFC11-6**. Before selecting from any
generated projection, the compiler **verifies the projection regenerates
faithfully from the governed artifacts** (RFC11-7); selection from a stale
or unfaithful projection is a violation, and the packet records the
projection verification it performed.

**RFC11-13. Every active contract declares its implementation boundary.**
Each active contract carries, in the front matter of its index (the package
README, or the file itself for a single-file contract):

```yaml
implementation_boundary:
  kind: none | requires-openspec | craft-policy
  clause: RFCx-y | null
```

- `requires-openspec` names the contract's own binding phase-rule clause:
  user-observable consequences of the contract receive approved OpenSpec
  requirements before implementation, and the named clause is where that
  boundary is stated.
- `none` states that the contract fixes structural design invariants with
  no independently observable behavior of its own; the per-clause routing
  classification supporting that claim is recorded review material, never
  authority, and the declaration — not the classification — is what a
  selector consumes.
- `craft-policy` states that the contract's observable consequences are
  governed by a named craft policy rather than an OpenSpec phase rule; the
  `clause` field then names the craft clause that owns the boundary.

The declaration lives in the governed artifact itself and is consumed, never
re-derived, inferred, or overridden by a selector (RFC11-7). A contract
whose declaration is absent, or whose named clause does not exist, makes
every packet selecting that contract **incomplete (RFC11-6)** — never
silently complete.

**RFC11-14. Dependency traversal is defined, bounded, and recorded.** The
mandatory set is computed by these rules, and no rule admits unstated
narrowing:

1. **Start** from the task's directly governed entities, clauses, and
   declared change class.
2. **Direct `depends_on`.** Add the direct `depends_on` obligations of
   every selected module. An edge is **satisfied by loading at least one
   module of the depended-on contract; where an edge is left unsatisfied,
   the clause identities the loaded modules cite from the depended-on
   contract are enumerated and disposed of individually in the omission
   register.**
3. **No silent transitivity.** Traverse beyond direct edges only where an
   edge is explicitly marked transitive.
4. **Constraints.** Load a `constrains` source clause when the task touches
   the declared seam (RFC11-16).
5. **Citations are not reliances.** Never traverse `cites` automatically.
6. **Termination.** Stop at identities already included: a module, clause,
   or artifact enters the mandatory set once, and re-encountering it adds
   nothing.
7. **Omissions are enumerated.** Every excluded applicable candidate is
   recorded in the packet's omission register with its reason.
8. **Undecidable fails closed.** Where applicability is undecidable from
   declared metadata, the packet is incomplete (RFC11-6) — never silently
   thinned.
9. **Scope travels.** The task's scope and risk class are part of the
   packet identity (RFC11-1).

**RFC11-15. Doctrine and craft rule ownership is declared, not judged.**
Selection of doctrine rules and craft policy clauses consumes deterministic
**ownership metadata**: for each rule identifier, at minimum, the owning
authoritative artifact, the task classes it applies to, and the risk
classes that make it mandatory. The metadata is authored in, or
deterministically derived from, the authoritative artifact; rebuildable;
clone-visible; and covered by validation — never a hand-maintained second
authority (RFC11-7). Where a task class or risk class has no declared
ownership metadata, doctrine/craft selection for it is **not claimed
deterministic**, and the packet states that basis rather than implying a
derivation that did not happen.

**RFC11-16. `constrains` is consumed clause-first.** Where a selected
clause, module, or the task's declared seam is the target of a
clause-anchored `constrains` relation, the mandatory set includes the
**constraining clause** — not automatically the entire constraining
contract. The constraining clause's direct dependencies enter only where
required to interpret that clause. The packet records why each constraint
entered.

**RFC11-11.** Packets carry a **size estimate** (words/tokens) and the
compiler enforces the governing policy's budget posture: a normal bounded
implementation task should receive a packet well below whole-corpus size,
with sharding or explicit exception (owner-visible, reasoned) when risk
genuinely requires more. [Inferred] The concrete numeric target is a policy
default, not doctrine — it must not be frozen into contract text without an
owner act; the working figure and its test evidence live in the rev10
context-load map and context-selection fixtures (delivery-packet evidence
artifacts, not part of this contract), and its permanent custody is §8 q1.
What binds here: exceeding the posture is a disclosed, reasoned event,
never silent; and budget pressure never justifies dropping mandatory
context (RFC11-5) — the lawful responses are sharding, narrowing the
objective, or escalating. Sharding has a **non-shardable core**: every
shard carries the envelope in full, the prohibited and human-only
surfaces, the applicable doctrine rules, and the governing phase rules
(RFC11-4) — a shard from which any of these is absent is not a lawful
packet.

## 8. Owner questions

*Package numbering; question numbers never shift. Full package index:
`README.md` §8.*

1. **Budget figure custody — OPEN.** The working target (well below
   whole-corpus; evidenced in the rev10 load map) is a policy default — does
   the owner want it recorded as a named policy artifact at V0, or left to
   the OpenSpec phase?

---

*End of RFC 0011 module 2. Clauses RFC11-4, RFC11-11, RFC11-13 … RFC11-16 —
non-contiguous by design; the package README's clause map is the lookup
authority. Nothing merged, nothing retired.*
