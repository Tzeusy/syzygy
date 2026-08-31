---
id: RFC-0004
title: Observation Sources and Evidence — the general observer/adapter contract
status_source: owner-act-record
module: general-contract
clauses: RFC4-1..RFC4-9 (no gaps, no retirements, no merges)
governs: [observers, adapters, declaration-set, emission-obligations, adapter-registry, version-skew, substitution]
applies_to: [kernel, trajectory, orrery]
depends_on: [RFC-0002, RFC-0003]
tags: [observation, adapters, registry, determinism-class, sdr-6, vis-5, vis-7, sec-5]
---

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — either owner-adopted (bootstrap,
uncorrelated) or Syzygy-verified, with the exact provenance state always
visible (RFC3-16). Absent such a record, this contract binds
nothing.

**Package:** module 1 of 4 of the RFC 0004 contract package. Index, clause map,
lookup rule, package-level integration and deferrals: `README.md`. Rationale,
amendment history, alternatives, and answered §8 questions:
`../../history/RFC-0004-history.md`.

**Serves:** VIS-1, VIS-5, VIS-7; SEC-5; architecture.md (typed authority;
adapter-mediated externals; the closed snapshot rule); trust-and-evidence.md
(the evidence definition; staleness). Implements **owner rulings** SDR-6
(generalized at RFC4-8(c)), SDR-10, and part of SDR §5 question 7 (the adapter
version registry).

---

## 0. Module scope and reader map (non-normative)

*If this section and a clause disagree, the clause wins.*

This module owns **what an observer or adapter is, what it must declare before
anything it emits is admissible, and what happens when versions move**. Read it
to answer: *may this output enter the graph at all?* Every other module in this
package presupposes it — a named adapter (module 2), an Execution Record
(module 3), or a fidelity label (module 4) produced by an observer that does
not satisfy RFC4-2 and RFC4-7 is inadmissible regardless of its own content.

Two rules carry most of the weight here: an external authority is reached
through **exactly one registered adapter** (RFC4-1), and a registry entry is
**not self-authenticating** — it is honored only under RFC3-16(a), because
admitting an adapter is what makes its output a deterministic fact at all
(RFC4-7). The anti-duplication invariant (RFC4-5) fixes which store may write
which field in both directions.

---

## 3. The contract

Clauses are numbered `RFC4-n` for stable citation. Amend in place; retire
rather than renumber.

### 3.1 Observers and adapters — the general contract

**RFC4-1 — Two roles, one discipline.** An **observer** captures facts from a
source Syzygy only reads (source trees, report files, runtime datasets). An
**adapter** is an observer that additionally mediates a typed external
authority (version control, hosting, the work scheduler, the OpenSpec CLI) and
may carry an explicitly authorized write surface (VIS-5). Every external
authority is reached through exactly one registered adapter per project;
nothing else in Syzygy touches that authority directly.

**RFC4-2 — Mandatory declaration set.** Every observer/adapter declares, in
its registry entry (RFC4-7), before any output is admissible:

1. **identity** — stable opaque identifiers for the observer role and for the
   implementation realizing it (substrates are substitutable);
2. **versions** — implementation version, and the version of *this contract's
   per-adapter clauses* it implements;
3. **declared inputs** — the source classes it reads, each mapped to the
   snapshot minimum-input list (RFC2-1);
4. **declared outputs** — the evidence and fact classes it emits, with each
   class's identity scheme;
5. **determinism class** — per output class: *derivation-deterministic* (same
   captured inputs always yield the same output; inside the VIS-7 identity
   test) or *capture* (a recording of what an external source said at a
   capture instant — immutable and identity-bearing, but a re-capture may
   legitimately differ);
6. **failure states** — which RFC2-23 degradation states it can enter, and the
   mapping from its internal errors onto them;
7. **authority boundary** — which typed-authority question(s) it answers, and
   (for adapters) the exact write surface, **which must be empty unless
   explicitly authorized**.

**RFC4-3 — Emission obligations.** Every emitted fact or evidence artifact
carries: source identity; **capture instant and capturing observer identity +
version**, distinct from any instant the source itself claims [Observed:
trust-and-evidence.md]; scope; and provenance sufficient to re-locate the
source. Observer and adapter identities and versions are snapshot inputs
(RFC2-1 item 7); an output from an observer whose identity/version is not in
the snapshot must not influence that snapshot's deterministic claims (RFC2-2).

**RFC4-4 — Failure is rendered, never invisible.** On failure an observer
degrades to its last-good observation record marked `stale`/`broken`
[Observed: trust-and-evidence.md, Staleness]; new claims depending on it
render Unknown (`source-uncaptured-or-unreachable`, RFC2-24 #10). An observer
that cannot classify content excludes it, fails closed, and renders the
exclusion (SEC-5; RFC2-24 #7).

**RFC4-5 — The two-limb anti-duplication invariant.** Binding for every
adapter:

- **Inward limb.** For every mutable field of an externally owned record,
  exactly one store is writable, and it is not Syzygy. Syzygy may hold a
  projection only if it is stamped with the identified evaluation that read
  it, is never presented as editable in a Syzygy surface, and is discarded and
  re-derived at the next evaluation — never merged. Any surviving, editable
  Syzygy copy of an external field is a second source of truth and forbidden.
  **The limb governs mutable projections of *current* external state; it does
  not govern captured evidence about the past.** An immutable,
  evaluation-stamped observation record or Execution Record capturing that a
  transition *occurred* — a historical fact, never rewritten and never
  presented as the field's current value — is not a second source of truth and
  is not forbidden here; where a durable Syzygy record depends on such a fact,
  RFC4-16(2) *requires* the capture. What this limb forbids is a Syzygy-side
  record of what the field **is now** that survives the evaluation that read
  it. [Inferred — the distinction the limb already turns on, stated so the
  capture duty and the anti-mirror rule are not read as opposed.]
- **Outward limb.** No Syzygy-owned fact is written into an externally
  writable store except as a **derived, re-derivable pointer**: stamped with
  the evaluation that produced it, re-asserted (never merged) on divergence,
  and treated as a cache of the Syzygy-side record, which stays authoritative.
  Where the external store permits third-party edits of that field, divergence
  is **rendered as a substrate annotation** — never adjudicated as a
  contradiction, because only one authority exists.

The asymmetry is deliberate: inward, the external value wins; outward,
Syzygy's record wins. Edits to external state go through the adapter,
synchronously and attributably, followed by a re-read — never
write-locally-and-sync-later.

**RFC4-6 — Substrate-term translation.** An adapter translates substrate
vocabulary on read and never lets it impersonate kernel vocabulary. In
particular, the scheduler's own "reconciliation" (state-repair passes,
`scheduler_state.reconciled`) is translated per RFC2-17 and never shares a
field, count, or UI string with doctrinal reconciliation. Substrate-native
identifiers (`bead_id`, PR numbers) are carried as substrate-qualified aliases
of the substrate-neutral identity, never as the primary key.

### 3.2 The adapter version registry

**RFC4-7 — The registry.** A per-project, versioned **adapter registry** lives
in the governance plane (`.syzygy/governance/`; physical schema: RFC 0003).
One entry per registered observer/adapter, holding the RFC4-2 declaration set
plus the entry's own adoption status. The registry is a snapshot input; an
output attributed to an adapter absent from the snapshot's registry state is
inadmissible as a deterministic fact and renders Unknown
(`source-uncaptured-or-unreachable`). An entry's **adoption status is not
self-authenticating** (RFC3-16): admitting an adapter is what makes its output
a deterministic fact at all, so an entry is honored **only under RFC3-16(a)** —
an entry an untrusted writer could mint would register an arbitrary adapter
and launder whatever it emits into the deterministic base graph, which no
downstream tier or freshness check inspects. An entry without an effective
owner act admits nothing: outputs attributed to it render Unknown exactly as
if the adapter were unregistered. State-(1) and state-(2) acts both admit the
entry, with the exact provenance state carried on every resulting fact.

**RFC4-8 — Version skew.** (a) Observation records permanently carry the
observer/adapter versions that produced them; an upgrade never reinterprets
existing records. (b) An adapter upgrade or registry change is a new snapshot,
never an in-place refresh [Observed: architecture.md]. (c) When an adapter
implements an older per-adapter contract version than the kernel expects, its
outputs are admitted **at the declared version**: fields the older contract
does not emit render Unknown with their reason — never defaulted, guessed, or
zero-filled (SDR-6 generalized). (d) When an adapter claims a contract version
this RFC does not define, its outputs are inadmissible until the registry
entry is corrected. (e) Cross-version joins are permitted only on identity
fields whose scheme both versions declare identically; otherwise the join
renders Unknown rather than fuzzy-matching.

**RFC4-9 — Substitution.** Replacing an implementation (a different VCS host,
a different scheduler) is a registry event: the role identity persists, a new
implementation identity is registered, and prior records keep resolving under
the old one. Substitution never rewrites history and never migrates
substrate-native aliases into the new substrate's namespace.

---

## 4. Violation cases

*Package numbering; cases are distributed across modules, never renumbered.*

1. *(RFC4-2/7)* An unregistered script's output feeds a deterministic claim;
   an adapter upgrade silently reinterprets last month's observation records.
2. *(RFC4-5)* A Trajectory board stores an editable copy of scheduler status
   and syncs it back nightly; a substrate-side `spec_id` edit is adjudicated
   as a contradiction instead of rendered as an annotation.
3. *(RFC4-8)* A field an old adapter version never emitted is backfilled with
   a default; an aggregate treats those defaults as data.

Case 5 spans this module and module 4 and is held at the package level
(`README.md` §4).

---

## 5. Integration (module-local)

**Relies on RFC 0002:** the snapshot minimum-input list and the
uncaptured-source rule (RFC2-1 item 7, RFC2-2) that make observer identity and
version deterministic inputs; the degradation states RFC4-2 item 6 maps onto
(RFC2-23); Unknown reasons (RFC2-24 #7, #10); the substrate-translation duty
(RFC2-17) realized by RFC4-6. **Relies on RFC 0003:** the RFC3-16 owner-act
predicate, and specifically RFC3-16(a) gating the registry entry (RFC4-7).

**Provides to RFC 0003:** the adapter-registry semantics it must physically
encode. **To RFC 0011:** the evidence-emission identity every context packet
binds against — source identity, capture instant, and capturing observer
identity + version (RFC4-3), and the determinism class that distinguishes a
re-derivable output from a capture (RFC4-2 item 5). **To the rest of this
package:** the declaration set (RFC4-2), the emission obligations (RFC4-3), and
the degradation contract (RFC4-4) that every named adapter, Execution Record,
and fidelity label depends on.

This module owns no §8 owner question.
