---
id: RFC-0004
title: Observation Sources and Evidence — provenance joins, fidelity labeling, code mappings, and the derivation-first invariant
status_source: owner-act-record
module: fidelity-joins-and-mappings
clauses: RFC4-22..RFC4-30 (no gaps, no retirements, no merges)
governs: [provenance-joins, join-basis, worker-liveness, reduced-fidelity-labels, degradation-mapping, code-mappings, code-markers, mapping-coverage, derivation-first, enrichment-roadmap]
applies_to: [kernel, trajectory, orrery]
depends_on: [RFC-0001, RFC-0002, RFC-0003]
tags: [provenance, liveness, reduced-fidelity, coverage, derivation-first, sdr-3, sdr-4, sdr-31, sdr-33, vis-1, vis-2]
---

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — as an owner-adopted bootstrap act until the
independent A1 correlation mechanism exists, and as a Syzygy-verified effective
act only after correlation (RFC3-16). Absent such a record, this contract binds
nothing.

**Package:** module 4 of 4 of the RFC 0004 contract package. Index, clause map,
lookup rule, package-level integration and deferrals: `README.md`. Rationale,
amendment history, alternatives, and answered §8 questions:
`../../history/RFC-0004-history.md`.

**Serves:** VIS-1, VIS-2, VIS-7; trust-and-evidence.md (staleness; the trust
floor); architecture.md (the human-triggered loop). Implements **owner rulings**
SDR-3, SDR-4, SDR-31, SDR-33.

---

## 0. Module scope and reader map (non-normative)

*If this section and a clause disagree, the clause wins.*

This module owns **how honestly a fact is labeled once it exists**: the
declared basis of every provenance join (RFC4-22); worker liveness, which is
never guessed (RFC4-23); the closed `reduced-fidelity` cause list and what a
coarse fact may never be asked (RFC4-24); the per-observer degradation mapping
(RFC4-25); where a capability↔code mapping may lawfully be declared, including
the marker-adoption gate (RFC4-26); the executed coverage record behind every
absence claim (RFC4-27); and the derivation-first invariant with its
never-required enrichment roadmap (RFC4-28, RFC4-29).

Read it to answer: *how much may I actually conclude from this fact?* Three
rules bind hardest: a convention-based join is legitimate but labeled, because
**a convention is a practice, not a guarantee**; only an actual progress signal
may render a worker live — never a coordinator heartbeat, a lock label, or a
worktree; and an absence claim without an executed coverage record renders
Unknown, because **an unexecuted mapping is not evidence of absence**. The
marker-adoption policy of RFC4-26 is **authorization-bearing** and honored only
under RFC3-16(a) — markers are written by workers into the untrusted code tree,
so the policy gate is the whole defense.

The joins and labels here are emitted by the adapters of module 2 and carried
on the records of module 3, all under the general contract of module 1.

---

## 3. The contract

Clauses are numbered `RFC4-n` for stable citation. Amend in place; retire
rather than renumber.

### 3.5 Provenance joins and liveness honesty

**RFC4-22 — Declared join bases.** Every adapter-owned link of the
change-accounting chain — work item ↔ branch/worktree, branch → commits,
commit → PR, PR → merge fact, gate outcome → artifact — declares its
**basis**: `recorded-identity` (an explicit identifier written by an actor) or
`naming-convention` (derived from a path/branch/message convention).
Convention-based joins are legitimate and labeled as such; they are
`reduced-fidelity` with cause `derived-from-convention`, because a convention
is a practice, not a guarantee [Observed]. A join that can no longer be
established (branch deleted, message tag absent) renders Unknown — never
fuzzy-matched.

**RFC4-23 — Worker liveness honesty.** No worker-side liveness signal exists
in the initial substrate: workers never heartbeat; the coordinator's heartbeat
attests **the coordinator's own claim**, and lock labels and worktree
existence outlive the processes they describe [Observed]. Therefore:

1. The coordinator heartbeat may be rendered only as coordinator-claim
   liveness, never as worker liveness.
2. Worker activity is derived exclusively from the **last progress signal** —
   branch tip moved, new commit, PR state changed — rendered with its instant
   and the declared staleness bound (bound value: policy material; the
   obligation to declare is binding here). That bound is an owner-approved
   declaration that unblocks a claim class — **until it is declared, this
   contract yields no admissible liveness input, so `active` cannot be
   rendered from it** (the surface-side statement of the same obligation is
   RFC8-16, a parallel-obligation pointer, not this rule's source) — so it
   is honored **only under RFC3-16(a)**: a
   bound an untrusted writer could mint would make `active` renderable, and a
   generous one would hold a dead worker green indefinitely on a signal that
   never comes. An unverifiable bound is no declaration: liveness stays
   unrenderable rather than degrading to a permissive default.
3. Between signals, worker liveness renders **Unknown**; past the bound, the
   item renders stale-or-dead with the last-signal instant shown — never
   "active", never green.
4. Not admissible as liveness, ever: the coordinator heartbeat, lock labels,
   worktree existence.

### 3.6 Reduced fidelity and degradation labeling

**RFC4-24 — The labeling schema (SDR-33; delegated by RFC2).** Event-time
evidence is captured where available. Where only coarser data exists, the fact
is emitted at the `reduced-fidelity` tier (RFC2-25) carrying, as one
structured label: **declared granularity** (what the fact truthfully resolves,
e.g. PR-level); **unavailable granularity** (what it does not, e.g.
per-commit); **cause**, from a closed list extendable only by amending this
RFC — `post-merge-history-unreachable`, `replace-in-place-source`,
`retention-horizon-passed`, `derived-from-convention`, `approximated-boundary`
(timing bounds from first/last durable trace), `terminal-report-only` (a run
knowable only from its terminal report), `indistinguishable-runs` (derived run
identity cannot separate two genuine dispatches; the run count renders Unknown
— RFC4-19/RFC4-20) — and **upgrade path** (which instrumentation or capture
would raise it, cross-referencing RFC4-27). Finer-granularity questions
against a reduced-fidelity fact render Unknown; interpolation and invention
are forbidden — full Observed authority holds *at the declared granularity
only* (RFC2-25).

**RFC4-25 — Degradation mapping.** Every registered observer names, in the
registry, which RFC2-23 states it can enter and what its last-good rendering
is. Staleness and brokenness are rendered on the primary surface, judged at
the evaluation's as-of instant [Observed: trust-and-evidence.md].

### 3.7 Code mappings: declared, inferred, and covered

**RFC4-26 — Declaration sites (SDR-3/4).** The four capability↔code relation
classes of RFC1-16 remain queryably distinct end to end: the observers of this
RFC emit class (iii) structural facts and class (iv) verification facts; class
(i) declared mappings come from the governance mapping artifact — the
**primary declaration site**; class (ii) inferred mappings enter only through
the inference profile with challenge authority only. **Optional code markers**
are a supplement, never required: the code-structure observer reads markers
and emits them as marker facts, but a marker constitutes a *declared* mapping
only where a governance-plane policy has adopted marker-sourced declarations
for that project; otherwise markers render as unadopted candidate declarations
— surfaced for adoption, anchoring nothing. **The adopting policy is
authorization-bearing and is honored only under RFC3-16(a)**: markers are
written by workers into the untrusted code tree, so a marker-adoption policy
an untrusted writer could mint would convert in-code text into anchoring
declarations by the same act — the policy gate is the whole defense, and it
must be a verifiable owner act, not a file. A project with no markers anywhere
is fully supported (SDR-4).

**RFC4-27 — Executed coverage behind every absence claim.** An absence claim —
"no code implements capability C", "this code maps to no capability", Orrery's
empty plot — is a status claim and requires an executed **mapping coverage
record**: which mapping pass ran, over which declared scope (repositories,
exclusions counted), with which observer/adapter versions, at which
evaluation, and what it found. Absent that record, the claim renders Unknown
(`mapping-coverage-absent`, RFC2-24 #5) — an unexecuted mapping is not
evidence of absence. Coverage records are deterministic facts inside the
observation record (RFC2-6).

### 3.8 Derivation-first, instrumentation-optional (SDR-31)

**RFC4-28 — The invariant.** Syzygy is fully truthful from derivable facts
alone. At V1, without any toolchain change, the adapters derive: work-item
state and transition history within the retention bound;
branch/worktree/commit/PR/merge joins for in-flight work; terminal worker and
reviewer report facts where persisted; PR-granularity change history for
closed work (`reduced-fidelity`); lead time at work-item granularity; and
approximated run boundaries — everything else renders Unknown with its reason
or reduced-fidelity with its cause. A sparse-but-honest pane is the correct
output, not a defect (VIS-1, VIS-2).

**RFC4-29 — The enrichment roadmap, named but never required.** The emissions
the adapters would consume, each upgrading a labeled Unknown or
reduced-fidelity fact to event-time Observed: durable run identity and
parent-run identity; dispatch records (model, runtime, instant); event
timestamps; worker progress/heartbeat signals; retained gate artifacts with
reported references; tokens/cost from the runtime; resolvable spec anchors on
work items; per-subworker report contracts. These evolve with the actuator
toolchain on a deliberate co-evolution roadmap; **no Syzygy claim, surface, or
acceptance test may require them** — a project whose toolchain emits nothing
is a first-class citizen rendered honestly. Where enrichment lands in the
substrate's own typed event store, Syzygy consumes it as one more read source;
any Syzygy-authored record placed there is governed by the outward limb
(RFC4-5) and the durable authority stays in `.syzygy/work/**` (RFC4-16) — the
substrate's store is never the primary home of Syzygy's run records (SDR-8).

---

### 3.9 Authority boundary at the OpenSpec seam (binding phase rule)

**RFC4-30.** This contract schedules nothing: **it is not a specification of
record from which implementation work may be scheduled**. No implementation
work for user-observable consequences of this contract — adapter
configuration and observation capture behavior, execution-record surfaces,
fidelity, staleness and degradation rendering, mapping displays — may be
scheduled solely from this RFC. Before implementation, every observable
consequence either maps to an approved OpenSpec requirement and scenario in
the governance root's `openspec/**` plane, or carries a reviewed N/A judgment
proving it purely structural with no independently testable behavior. **The
reviewed N/A judgment's home and gate.** A reviewed N/A judgment is a recorded
owner judgment homed in `decisions/` (RFC3-15), and it is honored only where
its owner-act provenance is verifiable under RFC3-16(a). Where that provenance
does not verify, the judgment maps nothing: the consequence remains unmapped
and renders Unknown, never covered (RFC3-16(a)'s effect rule; VIS-2).

**Rows are per observable consequence, not per clause.** A clause with five
observable consequences and one mapped requirement is not covered; the matrix
discloses the consequences it enumerates for each clause, so a
complete-looking matrix over under-enumerated consequences is a defect of the
matrix. At
surface specification a clause-to-requirement coverage matrix over
RFC4-1..RFC4-30 is produced — **that matrix is review material, never
authority**. This clause creates no OpenSpec content now (none may exist
during bootstrap). This clause binds the whole RFC 0004 package, not this
module alone. (Shape-parallel with RFC6-28, RFC7-38, RFC8-32, RFC9-52,
RFC10-16, RFC11-12.)

## 4. Violation cases

*Package numbering; cases are distributed across modules, never renumbered.*

10. *(RFC4-23)* A dead worker renders "active" because the coordinator's
    heartbeat is fresh and the worktree exists.
11. *(RFC4-24)* PR-level data answers a per-commit question by interpolation;
    a reduced-fidelity label is dropped in aggregation.
12. *(RFC4-26/27)* A code marker anchors a capability with no adopting policy;
    an empty Orrery plot renders "no code implements this" with no executed
    coverage record.

Case 5 spans module 2 and this module and is held at the package level
(`README.md` §4).

---

## 5. Integration (module-local)

**Relies on RFC 0001:** the four capability↔code relation classes (RFC1-16)
this module keeps queryably distinct. **On RFC 0002:** coverage records as
deterministic facts inside the observation record (RFC2-6); the
`mapping-coverage-absent` Unknown reason (RFC2-24 #5); the tier registry and
its declared-granularity rule (RFC2-25); the failure states each observer names
(RFC2-23). **On RFC 0003:** RFC3-16(a) gating the staleness bound (RFC4-23) and
the marker-adoption policy (RFC4-26).

**Provides to RFC 0003:** the reduced-fidelity label and coverage-record
semantics it must physically encode. **To RFC 0008:** the liveness rules
(RFC4-23) Trajectory renders — RFC4-23(2) cites **RFC8-16** for the rule that
`active` is unrenderable until the staleness bound is declared, a forward
citation into RFC 0008. **To RFC 0009:** the coverage records (RFC4-27) behind
every empty plot. **To RFC 0011:** the fidelity and coverage labels that bound
what a context packet may assert from a given fact.

---

## 8. Owner questions

*Package numbering; answered items keep their number and their reasoning is in
`../../history/RFC-0004-history.md` §8. Full package index: `README.md` §8.*

3. **Marker adoption granularity (RFC4-26) — OPEN.** Marker-sourced
   declarations activate per project by policy. Should activation be
   per-repository instead (a monorepo may want markers in one subtree only)?
   Proposed: the policy may scope itself; confirm. *(Scoping controls blast
   radius only; the authenticity requirement is untouched — the adopting
   policy is honored only under RFC3-16(a) at any granularity.)*
