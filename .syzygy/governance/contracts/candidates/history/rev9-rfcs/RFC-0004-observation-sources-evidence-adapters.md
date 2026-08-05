# RFC 0004 — Observation Sources, Evidence, Execution Records and Adapters

**Status:** Proposed foundational contract. This line is a self-declaration at authoring time (RFC3-16): effective status is established solely by the owner-act record binding this file's exact content digest, and acceptance edits nothing here. Absent such a record, this contract binds nothing.
**Date:** 2026-07-30 (amended through 2026-08-02)
**Serves:** VIS-1, VIS-2, VIS-5, VIS-6, VIS-7; SEC-2, SEC-3, SEC-4, SEC-5;
architecture.md (typed authority; adapter-mediated externals; the closed
snapshot rule); trust-and-evidence.md (the evidence definition; staleness;
the trust floor). Implements owner rulings SDR-3, SDR-4, SDR-5, SDR-6, SDR-7,
SDR-8, SDR-9, SDR-10, SDR-31, SDR-32, SDR-33, and resolves SDR §5 question 7
(run envelope schema; adapter version registry; reduced-fidelity labeling).

---

## 0. Reader's summary (non-normative)

*Plain-language orientation. If this section and a clause ever disagree, the
clause wins.*

- This RFC governs **how Syzygy sees the outside world**: every source (git,
  CI, the work scheduler, spec files, code) is read through a registered
  observer or adapter that declares up front what it reads, what it emits,
  its version, and how it fails.
- The core anti-fiction rule: an adapter **never silently normalizes,
  interpolates, or forgets**. Coarse data is labeled `reduced-fidelity` with
  its cause; missing data renders Unknown, never zero, never a default.
- **A green gate requires provenance, not just a file.** A test report is
  `gate-backed` (able to support a green status) only via one of four
  routes: a Syzygy-launched profiled run; an external CI run whose
  confirmation the adapter **captured at observation time** into snapshot
  identity (RFC4-13(a)); an owner-declared trusted oracle (scoped and
  expiring); or the recorded execution of a **governed checker** over a
  doc-only/governance-only diff — deterministic and re-runnable is
  necessary but **not sufficient**; the checker's definition must be
  lawfully governed for the clause it certifies (RFC4-13(b)). A well-formed
  report a worker wrote itself proves non-tampering, not genuineness — it
  caps at "an artifact asserting this exists".
- **One store per fact.** Syzygy never keeps an editable copy of an external
  system's field, and never writes its own facts into external stores except
  as re-derivable pointers.
- Every fleet run gets an **Execution Record** — an immutable evidence
  artifact with a minimum envelope (identity, work item, warrant, outcome,
  cost…). Where the toolchain records nothing, fields render Unknown; where
  two runs are indistinguishable, that is disclosed, never collapsed into
  one record.
- The work scheduler **forgets by design** (garbage collection, squash
  merges), so scheduler-resident facts must be captured before the horizon;
  a fact lost to the horizon renders "Unknown citing the retention event",
  never "no work existed".
- **Worker liveness is never guessed**: only actual progress signals count;
  a coordinator's heartbeat or a leftover worktree never renders a worker
  "active".
- Syzygy must be **fully truthful with zero toolchain changes** — richer
  instrumentation only upgrades labeled Unknowns; nothing may require it.

Structure: §3 is the contract (RFC4-1 … RFC4-29); §4 violation cases; §8
owner questions, answered ones marked in place.

---

## 1. Summary

This RFC is the contract between Syzygy and everything it observes. It fixes:
what any observer or adapter must declare and emit; the adapter version
registry and behavior under version skew; the named adapters for the
designated initial substrates (OpenSpec, git/hosting, code structure,
test/CI/runtime reports, Beads) with each one's authority boundary and
degraded modes; the **Execution Record** — an Evidence artifact under
`.syzygy/work/**` (SDR-8) — and its **minimum durable run envelope**;
model/timing/token/cost semantics under Unknown-never-zero (SDR-6); the
adapter-owned provenance joins of the change-accounting chain and the honest
treatment of worker liveness; the reduced-fidelity labeling schema (SDR-33);
declared-versus-inferred code mappings and the executed-coverage rule behind
every absence claim (SDR-3/4); and the derivation-first posture — V1 is fully
truthful from existing toolchain traces alone, with instrumentation as
optional co-evolving enrichment, never a hard dependency (SDR-31). It is
**contracts only**: no storage engine, wire format, transport, or language is
chosen; physical schemas belong to RFC 0003.

---

## 2. Motivation and doctrine grounding

Doctrine routes every question about what currently exists to code, tests,
CI, and runtime observations, and every effect on an external authority
through a typed, explicitly authorized adapter — those stores are never
Syzygy-owned namespaces [Observed: architecture.md, typed authority; VIS-5].
Evidence must be durable, identified, and integrity-verifiable, carrying
source, capture time, scope, and provenance [Observed: trust-and-evidence.md].
The snapshot rule closes the loop: observer, adapter, parser, and policy
versions are themselves deterministic inputs, and an uncaptured source must
not influence a claim [Observed: architecture.md; RFC2-1 item 7, RFC2-2].

The research corpus's audit of the actually-installed actuator toolchain
found the substrate both richer and more forgetful than assumed: no run
identity, model, runtime, timestamp, or cost is recorded anywhere; gate
results are LLM assertions with no retained artifact; the squash-merge plus
post-closure branch deletion path destroys per-commit evidence exactly when a
work item closes; and `bd gc`/`bd prune` delete closed issues and their
events on an undeclared horizon [Observed: `04-OBSERVATION-AND-FLEET-EVENT-
BRIEF` §5; `06-TRAJECTORY-BRIEF` §8.2 — non-authoritative substrate audit,
findings adopted here where cited]. The owner resolved the resulting scope
and posture questions: post-hoc telemetry enters V1 (SDR-5), the Execution
Record is an Evidence artifact and no new doctrine class (SDR-8), observation
is derivation-first (SDR-31), anchors resolve or render Unknown (SDR-32), and
fidelity loss is labeled, never papered over (SDR-33). This RFC turns those
rulings into a binding contract. [Inferred] The failure mode it guards
against is the *confident adapter*: an integration that silently normalizes,
silently interpolates, or silently forgets — manufacturing exactly the
comprehensible fiction VIS-1 forbids.

---

## 3. The contract

Clauses are numbered `RFC4-n` for stable citation. Amend in place; retire
rather than renumber. Parentheticals beginning
*History:* are amendment records — when and why text changed — and carry
no normative force; the clause text around them is the contract.

### 3.1 Observers and adapters — the general contract

**RFC4-1 — Two roles, one discipline.** An **observer** captures facts from a
source Syzygy only reads (source trees, report files, runtime datasets). An
**adapter** is an observer that additionally mediates a typed external
authority (version control, hosting, the work scheduler, the OpenSpec CLI)
and may carry an explicitly authorized write surface (VIS-5). Every external
authority is reached through exactly one registered adapter per project;
nothing else in Syzygy touches that authority directly.

**RFC4-2 — Mandatory declaration set.** Every observer/adapter declares, in
its registry entry (RFC4-7), before any output is admissible:

1. **identity** — a stable, opaque identifier for the observer role and one
   for the implementation realizing it (substrates are substitutable;
   architecture.md);
2. **versions** — implementation version and the version of *this contract's
   per-adapter clauses* it implements;
3. **declared inputs** — the source classes it reads, each mapped to the
   snapshot minimum-input list (RFC2-1);
4. **declared outputs** — the evidence classes and fact classes it emits,
   with each class's identity scheme;
5. **determinism class** — per output class: *derivation-deterministic*
   (same captured inputs always yield the same output; inside the VIS-7
   identity test) or *capture* (a recording of what an external source said
   at a capture instant — the record is immutable and identity-bearing, but
   a re-capture may legitimately differ);
6. **failure states** — which RFC2-23 degradation states it can enter, and
   the mapping from its internal errors onto them;
7. **authority boundary** — which typed-authority question(s) it answers,
   and (for adapters) the exact write surface, which must be empty unless
   explicitly authorized.

**RFC4-3 — Emission obligations.** Every emitted fact or evidence artifact
carries: source identity; **capture instant and capturing observer identity +
version** — distinct from any instant the source itself claims [Observed:
evidence definition, trust-and-evidence.md; the distinction is `04` §4's,
adopted as binding]; scope; and provenance sufficient to re-locate the source.
Observer and adapter identities and versions are snapshot inputs (RFC2-1
item 7); an output from an observer whose identity/version is not in the
snapshot must not influence that snapshot's deterministic claims (RFC2-2).

**RFC4-4 — Failure is rendered, never invisible.** On failure an observer
degrades to its last-good observation record marked `stale`/`broken`
[Observed: trust-and-evidence.md, Staleness]; new claims depending on it
render Unknown (`source-uncaptured-or-unreachable`, RFC2-24 #10). An observer
that cannot classify content excludes it, fails closed, and renders the
exclusion (SEC-5; RFC2-24 #7).

**RFC4-5 — The two-limb anti-duplication invariant.** Binding for every
adapter [adopted from `06` §5.2, which proposed it; the wording here is
normative]:

- **Inward limb.** For every mutable field of an externally owned record,
  exactly one store is writable, and it is not Syzygy. Syzygy may hold a
  projection of that field only if it is stamped with the identified
  evaluation that read it, is never presented as editable in a Syzygy
  surface, and is discarded and re-derived at the next evaluation — never
  merged. Any surviving, editable Syzygy copy of an external field is a
  second source of truth and forbidden. **The limb governs mutable
  projections of *current* external state; it does not govern captured
  evidence about the past.** An immutable, evaluation-stamped observation
  record or Execution Record capturing that a transition *occurred* — a
  historical fact about the external store, never rewritten and never
  presented as that field's current value — is not a second source of truth
  for the field and is not forbidden here; where a durable Syzygy record
  depends on such a fact, RFC4-16(2) *requires* the capture. What this limb
  forbids is a Syzygy-side record of what the field **is now** that survives
  the evaluation that read it. [Inferred — the distinction the limb already
  turns on, stated explicitly so the capture duty and the anti-mirror rule
  are not read as opposed.]
- **Outward limb.** No Syzygy-owned fact is written into an externally
  writable store except as a **derived, re-derivable pointer**: stamped with
  the evaluation that produced it, re-asserted (never merged) on divergence,
  and treated as a cache of the Syzygy-side record, which stays
  authoritative. Where the external store permits third-party edits of that
  field, divergence is **rendered as a substrate annotation** — never
  adjudicated as a contradiction, because only one authority exists.

The asymmetry is deliberate: inward, the external value wins; outward,
Syzygy's record wins. Edits to external state go through the adapter,
synchronously and attributably, followed by a re-read — never write-locally-
and-sync-later.

**RFC4-6 — Substrate-term translation.** An adapter translates substrate
vocabulary on read and never lets it impersonate kernel vocabulary. In
particular, the scheduler's own "reconciliation" (state-repair passes,
`scheduler_state.reconciled`) is translated per RFC2-17 and never shares a
field, count, or UI string with doctrinal reconciliation. Substrate-native
identifiers (`bead_id`, PR numbers) are carried as substrate-qualified
aliases of the substrate-neutral identity, never as the primary key
[Observed: `04` §4 `work_item_id`/`bead_id` analysis].

### 3.2 The adapter version registry

**RFC4-7 — The registry.** A per-project, versioned **adapter registry**
lives in the governance plane (`.syzygy/governance/`; physical schema:
RFC 0003). One entry per registered observer/adapter, holding the RFC4-2
declaration set plus the entry's own adoption status. The registry is a
snapshot input; an output attributed to an adapter absent from the snapshot's
registry state is inadmissible as a deterministic fact and renders Unknown
(`source-uncaptured-or-unreachable`). An entry's **adoption status is not
self-authenticating** (RFC3-16): admitting an adapter is what makes its
output a deterministic fact at all, so an entry is honored **only under
RFC3-16(a)** — an entry an untrusted writer could mint would register an
arbitrary adapter and launder whatever it emits into the deterministic base
graph, which no downstream tier or freshness check inspects. An entry whose
owner-act provenance does not verify admits nothing: outputs attributed to
it render Unknown exactly as if the adapter were unregistered.

**RFC4-8 — Version skew.** (a) Observation records permanently carry the
observer/adapter versions that produced them; an upgrade never reinterprets
existing records. (b) An adapter upgrade or registry change is a new
snapshot, never an in-place refresh [Observed: architecture.md — versions are
snapshot inputs]. (c) When an adapter implements an older per-adapter
contract version than the kernel expects, its outputs are admitted **at the
declared version**: fields the older contract does not emit render Unknown
with their reason — never defaulted, guessed, or zero-filled (SDR-6
generalized). (d) When an adapter claims a contract version this RFC does not
define, its outputs are inadmissible until the registry entry is corrected.
(e) Cross-version joins (an old record joined to a new one) are permitted
only on identity fields whose scheme both versions declare identically;
otherwise the join renders Unknown rather than fuzzy-matching.

**RFC4-9 — Substitution.** Replacing an implementation (a different VCS
host, a different scheduler) is a registry event: the role identity persists,
a new implementation identity is registered, and prior records keep resolving
under the old one. Substitution never rewrites history and never migrates
substrate-native aliases into the new substrate's namespace.

### 3.3 Named adapters and observers

Each named contract states: authority boundary, minimum read surface,
degraded modes. These bind the *initial substrate* integrations; the roles
are substitutable under RFC4-9.

**RFC4-10 — OpenSpec adapter.** *Authority:* the behavioral-requirements
system — content and identity of requirements and scenarios under the
constitutional OpenSpec artifact contract; never intent adjudication, never
status. *Reads:* per-artifact content and hash pinned to the repository
revision; requirement/scenario identities; declared relationships;
change-proposal state; the artifact-contract version (itself a snapshot
input). *Anchors (SDR-32):* the adapter declares its **spec-anchor scheme**
in the registry — how a requirement/scenario reference resolves to an
artifact location. Every anchor it emits must be resolvable at the snapshot
that carries it (trust-floor link rule); an anchor that does not resolve, or
a work item/execution record with no anchor at all, renders **Unknown —
never a rejection** of the project, the event, or the record. Whether
OpenSpec identities survive edit and rename is [Unknown] (RFC1-15); the
adapter therefore declares its anchor **stability class** (identity-stable
vs content-hash vs path+heading), and where continuity across an edit cannot
be established it renders the reference Unknown rather than guessing a
successor. *Degraded modes:* unreadable artifacts → RFC2-23 source-
unreachable; a malformed artifact is a fact about the source, rendered as
such, never silently skipped.

**RFC4-11 — Git/VCS adapter (with hosting sub-adapter).** *Authority:*
version history only — never intent, never observed behavior
[Observed: architecture.md]. *Reads:* repository identity → revision map;
ref → tip map; working-tree state descriptor; commit facts (SHA, parents,
author/committer identities and instants, message, changed-path summary);
branch existence; and, through the hosting sub-adapter, PR facts (identity,
head SHA, base, state, created/merged instants, review decision, review
threads, check conclusions) and **merge facts**. A merge fact comes only from
this adapter — never inferred from scheduler closure (RFC2-20). *Writes:*
only the commit-out of Syzygy-authored governance artifacts into the two
namespaces (VIS-5/VIS-6), attributed and revertable (SEC-4). *Fidelity
(SDR-33):* where the toolchain's merge path is squash-plus-branch-deletion,
per-commit facts for closed work become unreachable [Observed: `04` §5.4(a)].
The adapter emits event-time-grade commit evidence **where available**
(in-flight and unmerged work, or captured before deletion) and otherwise
emits PR-granularity facts explicitly labeled `reduced-fidelity` with cause
`post-merge-history-unreachable` (RFC4-28) — it never reconstructs commit
history it cannot reach. *Degraded modes:* unreachable remote or hosting API
→ last-good marked stale; a SHA referenced by evidence but no longer
reachable renders the reference broken, not the evidence deleted.

**RFC4-12 — Code-structure observer.** *Authority:* what code exists —
structure only, never semantic ownership (SDR-3). *Reads:* file inventory
within consented scope (secret exclusions applied and counted, SEC-5,
**under the observing project's own secret-detection policy — never the
observed source's**, RFC3-30 — and only a version of that policy whose
owner-act provenance verifies under **RFC3-16(a)**, since a worker-minted
policy would let this observer index the content SEC-5 requires excluded);
symbols, modules, containment; deterministically observed structural
relations (`calls`, `exposes`, `accesses`) with parser version identified.
*Code-element identity (obligation from RFC1-5):* adapter-defined and **not
path-only**. The scheme, declared per language in the registry, must derive
identity from at least (repository identity, element kind, language-qualified
symbol name) with a content digest as disambiguator, so that a file move that
preserves the qualified name preserves identity. Where continuity cannot be
established across a change, the observer reports new/retired elements and
lets the kernel's successor machinery render the change (RFC1-11) — it never
silently re-binds an identity by similarity. *Boundary:* static parsing only;
anything requiring the project's toolchain to execute is blocked until the
execution-profile RFC (SEC-3).

**RFC4-13 — Test, CI, and gate observers.** *Authority:* verification
evidence as it exists on disk or in CI systems — Syzygy reads reports; it
does not run them (SEC-3) [Observed: v1.md V0 scope]. *Reads:* report
identity and hash; suite/case identities and outcomes; **the revision the
report claims to describe** — a report is evidence only for that revision
(RFC2-11); CI run identity, conclusion, instants, and log/artifact
references. *Gate tiering (SDR-9; RFC2-25):* a gate outcome is emitted
`gate-backed` only when **both** predicates hold — the **retention/format
predicate** (a retained, resolvable artifact bound to the exact revision is
captured with it) **and the provenance predicate below**; a structured
report asserting an outcome without such an artifact is emitted
`report-fact` (the report's existence and content are Observed; the outcome
is not); a bare LLM assertion is emitted `asserted-by-worker`. The observer
never upgrades a tier; only new evidence in a new snapshot can.

*Provenance predicate on `gate-backed` (post-draft amendment under review
3's AS-R3; routes confirmed and bounded at acceptance by owner decision A2,
route 4 added by the same decision).* An artifact qualifies for `gate-backed`
only through **exactly one of four routes**:

1. it was **produced by a Syzygy-launched profiled run** (RFC5-21), and so
   passed the isolation floor that exists to contain untrusted code;
2. it is **carried by an external CI or hosting system whose run identity
   and authenticity the sub-adapter independently confirmed at observation
   time and captured** (the hosting sub-adapter's PR/check facts, RFC4-11) —
   confirmation by the system, not by the artifact's own content, and the
   confirmation itself is a captured artifact inside snapshot identity, per
   **RFC4-13(a)**, never a query re-run against the provider at some later
   read;
3. it is **covered by an owner-declared trusted-external-oracle policy** in
   the governance plane, naming the oracle and the scope it may back — a
   policy that is itself authorization-bearing and therefore honored only
   under **RFC3-16(a)**. *(History: bounded at acceptance.)* Such a policy is scoped
   to a named **(project, gate class)** pair and **carries an expiry**; it may
   not be declared project-wide, gate-class-wide, or indefinitely. An expired
   or unscoped oracle declaration backs nothing and the artifacts under it
   fall to `report-fact`. The bound exists because route 3 is the only route
   whose sufficiency rests on the owner's word rather than on capture: without
   scope and expiry, a single declaration silently makes everything
   `gate-backed` forever, and nothing in this contract would later surface
   that it had;
4. it is the recorded execution of a **governed checker** — a deterministic,
   re-runnable satisfaction check over a declared diff and the clause it
   claims to satisfy, where the checker's definition is lawfully governed
   for that clause or clause class and the execution artifact binds exact
   inputs and revisions, both per **RFC4-13(b)**. *(History: added at acceptance,
   answering RFC 0002 §8 q3; hardened at the rev7 rework, blocker A5.)*
   This route exists for **documentation-only and governance-only work**,
   which has no execution gate to run and would otherwise cap permanently at
   `report-fact`. [Inferred] Determinism and re-runnability are
   **necessary but not sufficient**: a checker whose body is `return PASS`
   is perfectly deterministic and re-runnable, and certifies nothing. What
   makes the route lawful is governance of *what the check means* —
   RFC4-13(b) — on top of determinism of *how it runs*. A check whose
   inputs are not snapshot-identified, whose verdict a re-run can change,
   or whose definition is not lawfully governed for the clause it certifies
   is **not** this route and its outputs cap at `report-fact`.

A retained, well-formed, revision-bound artifact of **unverifiable origin
caps at `report-fact`** — "an artifact asserting Y exists" — which per
RFC2-25 can never support a positive status claim (Aligned, Converged,
reconciled, green). [Inferred] Format, retention, and hash-carrying prove
**non-tampering, not genuineness**: an untrusted fleet worker (SEC-3's
actor class, extended to committed artifacts at RFC3-16(a)) with
ordinary write access can author a syntactically valid report naming the
exact revision. Craft-and-care states the routes-1-and-2 capture side of
this rule — "a report the worker itself wrote and attached is an
emitter-captured **report fact** … integrity-verifiability proves
non-tampering, not genuineness" (CC-TEST-2, amended at the rev7 rework to
name routes 3 and 4 as the owner-created exceptions with their own guards)
— and this clause is the contract carrying the full four-route model.
Note that route 1 and route 2 both amount to **capture by an observer
distinct from the emitter**; route 3 is the owner's explicit escape hatch
for oracles Syzygy cannot itself confirm.

*Degraded modes:* revision mismatch → stale on the primary surface; missing
referenced artifact → the outcome's tier drops and the dangling reference is
rendered broken; **origin unverifiable under all four routes → the outcome
caps at `report-fact`, rendered with that cap visible, never rejected**.

**RFC4-13(a) — The external-confirmation capture artifact.** *(History: added at the
rev7 rework, blocker A3: route 2 as originally worded left the confirmation
an unstored act, which RFC8-27 then read as re-performable "at read time" —
making a stored evaluation's meaning depend on a mutable external system.)*
When route 2 is exercised, the confirming sub-adapter performs the
confirmation **at observation/capture time** and mints an
**external-confirmation capture artifact** recording, at minimum:

1. the **provider identity** (which external CI or hosting system);
2. the **external run/check identity** the provider was asked about;
3. the **provider's response or result content** as received;
4. the **capture instant**;
5. a **digest or integrity identity of the response**, so later readers can
   detect tampering with the stored capture;
6. the **confirming adapter/sub-adapter identity and version**;
7. the **confirmation outcome** (confirmed / not confirmed / indeterminate,
   with the provider's stated reason where one exists).

The source snapshot **contains or references this artifact** (RFC2-1 item 4),
and evaluations consume **only captured, identified inputs** (RFC2-2): route
2 is satisfied by the captured confirmation, never by a live query. "Read
time" in any statement about this route means **the adapter's observation/
capture time**, not the time a surface later displays or a query later
resolves the evaluation. Consequences: a provider that later expires its
run records **changes nothing** about any existing observation record — the
record is immutable (RFC2-6) and its tiers stand as evaluated; a later
**re-confirmation attempt is a new observation** producing a new snapshot
and new evaluation, which may lawfully find the provider no longer confirms
and degrade the tier there (RFC2-4's new-snapshot path); and an evaluation
whose route-2 evidence lacks a resolvable capture artifact treats the route
as unsatisfied and the outcome caps at `report-fact`. [Inferred — the
artifact schema; Observed — the immutability and consumption rules it
restates from RFC2-1/2/6.]

**RFC4-13(b) — The governed checker.** *(History: added at the rev7 rework, blocker
A5: route 4 as originally worded demanded only determinism and
re-runnability, which a checker whose body is `return PASS` satisfies.)*
Route 4 has two artifacts, and `gate-backed` requires both.

A **governed checker definition** is a governance-plane artifact carrying,
at minimum:

1. a **stable checker identity** and a **version/content identity** (the
   exact checker text or binary digest);
2. **declared applicability** — which clause identities or clause classes it
   may certify, and for what work classes (documentation-only,
   governance-only);
3. **declared satisfaction semantics** — what, in human-reviewable terms,
   a PASS asserts about the diff against the clause;
4. an **input contract** (which snapshot-identified inputs it reads — the
   diff, the clause revision, declared context) and an **output contract**
   (the closed result vocabulary it may emit);
5. its **governing authority and adoption provenance** — who adopted it for
   that applicability, and under what act.

Because a checker that can unblock positive status **fixes the meaning of a
certification**, its definition is authorization-bearing under RFC3-16(a)'s
own predicate and is honored only with verifiable owner-act/governance
provenance; its applicability and satisfaction semantics must be stated so a
human reviewer can judge whether the check means what the clause requires.

A **checker execution artifact** records, at minimum: the **exact diff or
revision pair** checked; the **exact clause revision** certified against;
the **exact checker identity and version** run; the **exact inputs**
consumed (all snapshot-identified); the **deterministic result** in the
checker's output vocabulary; and capture provenance (executing party,
capture instant, and — where the run was Syzygy-launched — the RFC4-19
execution-record linkage).

**Separation of authorship and certification.** A worker **may run** a
governed checker over its own change; it may **not author, select, or amend**
the checker definition that certifies that same change — a change and the
authority that certifies it may not originate in the same untrusted act, and
a checker definition edit rides the same adoption gate as any other
authorization-bearing artifact, never lands silently. An execution artifact
naming a checker version whose adoption provenance does not verify, or whose
declared applicability does not cover the clause certified, is not route 4
and caps at `report-fact`. **Acceptance test this clause must survive:** a
checker whose body is `return PASS` — deterministic, re-runnable, and
certifying every diff — cannot lawfully back a `gate-backed` outcome,
because its satisfaction semantics cannot truthfully state what a PASS
asserts, and no lawful adoption of that semantics for a real clause class
exists. [Inferred — the two-artifact contract; Observed — the RFC3-16(a)
predicate it instantiates.]

**RFC4-14 — Runtime observer.** *Authority:* runtime observations. *Reads:*
externally produced datasets, traces, and incident records, each with **the
window it covers**, its capture instant, and the deployed revision it
describes — dataset and window are both snapshot inputs [Observed:
architecture.md]. A one-off capture is legitimate evidence; reproducibility
is a declared property of the class, not a prerequisite [Observed:
trust-and-evidence.md]. *Boundary:* ingestion only; collection that requires
executing observed code is blocked under SEC-3.

**RFC4-15 — Beads adapter: the read contract.** *Authority:* work lifecycle
state, after materialization only (SDR-7) — never intent, never observed
behavior, never why the work exists [Observed: architecture.md; `06` §5.3].
*Reads:* work-item identity (emitted as the substrate-neutral identity with
`bead_id` as its substrate-qualified alias, RFC4-6); **the status vocabulary
as the tool declares it** — statuses and their categories read from the
substrate (`bd statuses`, including custom statuses), transmitted verbatim
with the export's capture instant, never hardcoded: the installed toolchain's
own documentation covers only five of the substrate's seven built-in statuses
[Observed: `06` §3.1], and the adapter must not inherit a client's drift.
Also: assignee; dependency edges with their types; labels; `external_ref`;
notes blocks as opaque annotated text; created/updated/closed instants; and
transition history (`bd history`, `--as-of`) **within the declared retention
bound** (RFC4-16). The **normalized work-state mapping** — how substrate
statuses project into Trajectory's state vocabulary — is RFC 0008's; this
adapter's duty ends at faithful, capture-stamped transmission. *Writes*
(each an explicitly authorized adapter effect): work-item creation at
materialization; lifecycle mutations commanded through Syzygy surfaces
(synchronous, attributed, re-read after write); and warrant pointers under
RFC4-17. *Degraded modes:* export unavailable → last-good marked stale;
replace-in-place note fields (heartbeat, review-cycle) are current values,
not histories — the adapter emits them as such, `reduced-fidelity` with
cause `replace-in-place-source` for any per-cycle question [Observed:
`04` §5.1].

**RFC4-16 — Capture-before-horizon.** The scheduler substrate forgets by
default: `bd gc` deletes closed issues past a default horizon, `bd prune`
permanently deletes closed beads with their dependencies, labels, events,
and comments, and `compact`/`flatten` squash the underlying history; the
issue database is not in the git tree [Observed: `06` §8.2]. Therefore:

1. Scheduler history is a **convenience, never an authority**, for anything
   older than the declared retention bound. The bound is a declared policy
   in the governance plane and a snapshot input; until declared, claims
   depending on scheduler history render Unknown
   (`no-currency-bound-declared` mechanics, RFC2-9 applied to retention).
   The bound is an owner-approved policy declaration that unblocks claims
   and is therefore honored only under **RFC3-16(a)** — a retention bound
   an untrusted writer could mint would unblock exactly the claims the
   horizon is supposed to render Unknown. The same holds for RFC2-9's
   currency-bound declaration wherever this RFC's observers depend on it.
2. Every scheduler-resident fact that a durable Syzygy record depends on —
   the run envelope's inputs, materialization joins, transition history
   feeding an account — must be captured into Syzygy-owned artifacts
   (Execution Records, observation records) **before** the horizon.
   Capture runs inside ordinary human-triggered observation passes
   (RFC2-19); the operational obligation is that passes be run within the
   horizon, and the contract's obligation is honesty when they were not.
   **The quality policy must declare a maximum inter-pass interval tied to
   the declared retention bound**, so pre-horizon history loss is *bounded*
   rather than merely rendered honestly; until that interval is declared,
   claims depending on pre-horizon scheduler history render Unknown on the
   same mechanics as an undeclared bound — and, on the same mechanics again,
   the interval is honored **only under RFC3-16(a)**, since it gates the same
   claims by the same route as the retention bound in (1) and an untrusted
   writer could otherwise declare an interval wide enough to unblock them
   while bounding nothing. **Declaring the interval is the
   obligation; running a scheduler that enforces it is not** — the loop
   stays human-triggered (architecture.md), so the contract binds the
   declaration and the honest rendering when the declared interval was
   exceeded, never an autonomous trigger. *(History: post-draft amendment under
   review 3's AS-R16, taking §8 q4's stricter option.)*
3. A fact lost to the horizon before capture renders **Unknown citing the
   retention event** — never silently absent, and never "no work existed"
   [adopted from `06` §8.3's honest-degradation rule].
4. Per-record substrate protections (`pinned`, `--no-history`) may be used
   as supplements but never as the primary durability guarantee — they live
   in a store Syzygy does not own.

**RFC4-17 — The warrant pointer (outward limb applied).** At
materialization, the adapter writes the warrant reference (resolvable spec
anchor or decision identity) into the substrate's provenance field
(`spec_id`/metadata) as a **derived, re-derivable pointer** under RFC4-5:
the `.syzygy/work/**` materialization record stays authoritative; a
substrate-side edit of the field is rendered as an annotation ("edited in
substrate at T; not a warrant claim") and the pointer is re-asserted at the
next evaluation — no contradiction is manufactured on the chain's
load-bearing join [Observed: the failure analysis in `06` §5.3].

### 3.4 The Execution Record and the minimum run envelope

**RFC4-18 — Classification (SDR-8).** An **Execution Record** is an
**Evidence artifact** — durable, identified, integrity-verifiable, immutable
once recorded — residing under `.syzygy/work/**`. It is a *kind* of the
existing Evidence class (RFC1-5); **no new doctrine-level evidence class
exists**. It is execution-plane evidence (RFC1-22): it may support claims
about what the fleet did, and it may never satisfy a desired-state claim —
work is never proof intent is satisfied. It is captured historical evidence
and, like all evidence, is not required to be rebuildable from a source that
no longer exists; observation records cite it (RFC2-1 item 6).

**RFC4-19 — The minimum durable run envelope.** One Execution Record per
execution run (RFC1-5), including Syzygy's own propagation acts. Field
classes: **R** = required (record inadmissible without it), **EA** =
`expected-where-available` — expected wherever the source can supply it,
**Unknown-with-reason otherwise** (never zero, never defaulted) — and **O**
= optional enrichment. *(The class was labeled `required-where-available`
(RA) in the draft; renamed under review 3's AS-N3 because "required where
available" states no obligation. The rule is unchanged.)*

| Field | Class | Semantics |
|---|---|---|
| record identity + envelope schema version | R | Deterministically derived; schema version is RFC 0003's to physically encode |
| capture metadata | R | Capture instant; capturing observer identity + version; references to the source artifacts the record was derived from (RFC4-3) |
| project identity | R | The governed project (never a filesystem path) |
| run identity | R | Toolchain-emitted where it exists; otherwise **adapter-derived** deterministically from durable joins (work item, branch, dispatch-distinguishing facts), labeled `derived` — the two origins are queryably distinct. **Derivation collision must be detected and disclosed:** where the derivation inputs cannot distinguish two dispatches, the affected records render `reduced-fidelity` with cause `indistinguishable-runs` (RFC4-24) and the **run count renders Unknown** — never a silent single record (RFC4-20) |
| parent run identity | EA | Null at the root; what makes nested spans truthful rather than guessed |
| work item identity + substrate alias | R | Substrate-neutral identity primary; `bead_id` as alias (RFC4-6). Unattributable runs are admissible only rendered as unattributed execution noise, never dropped [Observed: vision.md anchoring mandate via `04` §3.1] |
| warrant reference | EA | The materialization record identity, and through it the pinned intent revision and resolvable spec anchor (SDR-32). Absent or unresolvable → Unknown, never rejection |
| run start / end instants | EA | Toolchain-recorded where available; else derivation bounds (first/last commit, report instants) labeled `reduced-fidelity` |
| runtime + model | EA | Provider-qualified or not at all [Observed: `04` §4]; absent → Unknown |
| worktree | O | Descriptive, machine-local; never identity-bearing |
| branch + base revision | EA | The convention-grade correlation join, with its basis declared (RFC4-26) |
| commits produced | EA | SHA set where reachable at capture; post-squash → PR-granularity, `reduced-fidelity` (RFC4-11) |
| PR identity + merge-fact reference | EA | From the hosting sub-adapter, never from scheduler closure |
| terminal outcome + blocker set | R | The toolchain's closed report-status vocabulary, transmitted verbatim with the substrate qualified; blockers structured as reported |
| gate outcomes + artifact references | EA | Each with its RFC2-25 tier; `gate-backed` only under **both** RFC4-13 predicates — a retained resolvable artifact bound to the exact revision (SDR-9) **and** a qualifying provenance route; unverifiable origin caps at `report-fact` |
| tokens / cost | EA | Per RFC4-21; absent → Unknown, never zero (SDR-6) |
| **profile identity + version** | EA | The execution profile the run launched under, as RFC5-18(e) requires; absent for runs Syzygy did not launch, rendered Unknown-with-reason, never blank. A run Syzygy *did* launch with no recoverable profile identity is not attributable and its outputs cannot be `gate-backed` (RFC4-13 route 1) |
| **policy-violation flags** | EA | Whether the run violated its declared profile policy (undeclared egress, write outside scope, resource bound exceeded, out-of-purpose credential use), as RFC5-21 requires recorded on the Execution record; a violating run terminates and its outputs cap at `report-fact`. Absent → Unknown-with-reason, never read as "no violation" |
| prose fields (summary, reasons) | O | Admitted only through **the observing project's** declared secret-detection policy (SEC-5; RFC3-30); unclassifiable content excluded, exclusion rendered. Prompt/transcript bodies never enter; a prompt hash may — the authority for what may be *stored* is **SEC-5 and RFC5-17** (screening; hash-not-body provenance), not SEC-2, which governs egress [Observed: `04` §4] |

**RFC4-20 — Enrichment is explicitly non-required.** Fine-grained
heartbeats, nested tool events, phase transitions, per-span telemetry, and
streaming capture are **optional enrichment**: their absence never blocks a
record, never degrades the record below its envelope, and no kernel or
surface behavior may require them (SDR-31; SDR-5 keeps live streaming and
control deferred entirely). Multiple runs against one work item are distinct
records — redispatches and attempts are countable only from records, never
inferred from a mutation trail.

**Derivation collision is detected and disclosed, never collapsed.** Where
run identity is adapter-derived (RFC4-19) and the derivation inputs cannot
distinguish two genuine dispatches — a redispatch after a failed attempt, an
owner re-run on the same work item and branch, with the substrate recording
no dispatch-distinguishing fact — deterministic identity is by construction
non-unique, and the records would otherwise collapse into one. The adapter
must instead: emit the affected records at the `reduced-fidelity` tier with
cause **`indistinguishable-runs`** (RFC4-24), and render the **run count for
that work item Unknown** rather than reporting the collapsed number. A
silent single record is a violation. [Inferred] This is SDR-6's
Unknown-never-zero generalized to counts: an undisclosed undercount of
attempts is the same fiction as a zero-filled cost. **This safeguard is
normative regardless of how §8 q1 (derive versus austerity) is ruled** —
under austerity the identity itself renders Unknown, and the count
obligation here is what stops the austere form from silently under-joining
either.

**RFC4-21 — Model, timing, token, and cost semantics.** Values come only
from runtime-reported or toolchain-recorded facts captured as evidence; a
cost computed from token counts and a rate table is **Inferred** (rate
tables drift) and labeled with its derivation [Observed: `06` §6]. Absent
values render Unknown, never zero (SDR-6). **Partial aggregates are
disclosed**: any sum, average, or account over runs where some values are
Unknown must state its coverage ("cost known for n of m runs") and must
never render as a complete total — an undisclosed partial aggregate is the
zero-fallacy at portfolio scale. Cost measures stay independent; no
composite "effort" number [Observed: `06` §6, per the maturity ruling's
logic]. Event instants are execution facts, distinct from any evaluation's
as-of instant; they never alter a status outside a new identified evaluation.

### 3.5 Provenance joins and liveness honesty

**RFC4-22 — Declared join bases.** Every adapter-owned link of the
change-accounting chain — work item ↔ branch/worktree, branch → commits,
commit → PR, PR → merge fact, gate outcome → artifact — declares its
**basis**: `recorded-identity` (an explicit identifier written by an actor)
or `naming-convention` (derived from a path/branch/message convention).
Convention-based joins are legitimate and labeled as such; they are
`reduced-fidelity` with cause `derived-from-convention`, because a
convention is a practice, not a guarantee [Observed: `04` §4 `branch`;
`06` §7 links 6–7]. A join that can no longer be established (branch
deleted, message tag absent) renders Unknown — never fuzzy-matched.

**RFC4-23 — Worker liveness honesty.** No worker-side liveness signal exists
in the initial substrate: workers never heartbeat; the coordinator's
heartbeat attests **the coordinator's own claim**, and lock labels and
worktree existence outlive the processes they describe [Observed: `06`
§3.2a]. Therefore:

1. The coordinator heartbeat may be rendered only as coordinator-claim
   liveness, never as worker liveness.
2. Worker activity is derived exclusively from the **last progress signal**
   — branch tip moved, new commit, PR state changed — rendered with its
   instant and the declared staleness bound (bound value: policy material;
   the obligation to declare is binding here). The bound is an owner-approved
   declaration that unblocks a claim class — until it is declared `active` is
   unrenderable (RFC8-16) — so it is honored **only under RFC3-16(a)**: a
   bound an untrusted writer could mint would make `active` renderable, and a
   generous one would hold a dead worker green indefinitely on a signal that
   never comes. An unverifiable bound is no declaration: liveness stays
   unrenderable rather than degrading to a permissive default.
3. Between signals, worker liveness renders **Unknown**; past the bound,
   the item renders stale-or-dead with the last-signal instant shown —
   never "active", never green.
4. Not admissible as liveness, ever: the coordinator heartbeat, lock
   labels, worktree existence.

### 3.6 Reduced fidelity and degradation labeling

**RFC4-24 — The labeling schema (SDR-33; delegated by RFC2).** Event-time
evidence is captured where available. Where only coarser data exists, the
fact is emitted at the `reduced-fidelity` tier (RFC2-25) carrying, as one
structured label: **declared granularity** (what the fact truthfully
resolves, e.g. PR-level); **unavailable granularity** (what it does not,
e.g. per-commit); **cause**, from a closed list extendable only by amending
this RFC — `post-merge-history-unreachable`, `replace-in-place-source`,
`retention-horizon-passed`, `derived-from-convention`,
`approximated-boundary` (timing bounds from first/last durable trace),
`terminal-report-only` (a run knowable only from its terminal report),
`indistinguishable-runs` (derived run identity cannot separate two genuine
dispatches; the run count renders Unknown — RFC4-19/RFC4-20, added
post-draft under review 3's AS-R4) — and **upgrade path** (which instrumentation or capture would raise it,
cross-referencing RFC4-27). Finer-granularity questions against a
reduced-fidelity fact render Unknown; interpolation and invention are
forbidden — full Observed authority holds *at the declared granularity
only* (RFC2-25).

**RFC4-25 — Degradation mapping.** Every registered observer names, in the
registry, which RFC2-23 states it can enter and what its last-good rendering
is. Staleness and brokenness are rendered on the primary surface, judged at
the evaluation's as-of instant [Observed: trust-and-evidence.md].

### 3.7 Code mappings: declared, inferred, and covered

**RFC4-26 — Declaration sites (SDR-3/4).** The four capability↔code relation
classes of RFC1-16 remain queryably distinct end to end: the observers of
this RFC emit class (iii) structural facts and class (iv) verification
facts; class (i) declared mappings come from the governance mapping artifact
— the **primary declaration site**; class (ii) inferred mappings enter only
through the inference profile with challenge authority only. **Optional code
markers** are a supplement, never required: the code-structure observer
reads markers and emits them as marker facts, but a marker constitutes a
*declared* mapping only where a governance-plane policy has adopted
marker-sourced declarations for that project; otherwise markers render as
unadopted candidate declarations — surfaced for adoption, anchoring nothing.
**The adopting policy is authorization-bearing and is honored only under
RFC3-16(a)**: markers are written by workers into the untrusted code tree,
so a marker-adoption policy an untrusted writer could mint would convert
in-code text into anchoring declarations by the same act — the policy gate
is the whole defense, and it must be a verifiable owner act, not a file.
A project with no markers anywhere is fully supported (SDR-4).

**RFC4-27 — Executed coverage behind every absence claim.** An absence claim
— "no code implements capability C", "this code maps to no capability",
Orrery's empty plot — is a status claim and requires an executed **mapping
coverage record**: which mapping pass ran, over which declared scope
(repositories, exclusions counted), with which observer/adapter versions,
at which evaluation, and what it found. Absent that record, the claim
renders Unknown (`mapping-coverage-absent`, RFC2-24 #5) — an unexecuted
mapping is not evidence of absence. Coverage records are deterministic
facts inside the observation record (RFC2-6).

### 3.8 Derivation-first, instrumentation-optional (SDR-31)

**RFC4-28 — The invariant.** Syzygy is fully truthful from derivable facts
alone. At V1, without any toolchain change, the adapters derive: work-item
state and transition history within the retention bound; branch/worktree/
commit/PR/merge joins for in-flight work; terminal worker and reviewer
report facts where persisted; PR-granularity change history for closed work
(`reduced-fidelity`); lead time at work-item granularity; and approximated
run boundaries — everything else renders Unknown with its reason or
reduced-fidelity with its cause. A sparse-but-honest pane is the correct
output, not a defect (VIS-1, VIS-2).

**RFC4-29 — The enrichment roadmap, named but never required.** The
emissions the adapters would consume, each upgrading a labeled Unknown or
reduced-fidelity fact to event-time Observed: durable run identity and
parent-run identity; dispatch records (model, runtime, instant); event
timestamps; worker progress/heartbeat signals; retained gate artifacts with
reported references; tokens/cost from the runtime; resolvable spec anchors
on work items; per-subworker report contracts. These evolve with the
actuator toolchain on a deliberate co-evolution roadmap; **no Syzygy claim,
surface, or acceptance test may require them** — a project whose toolchain
emits nothing is a first-class citizen rendered honestly. Where enrichment
lands in the substrate's own typed event store, Syzygy consumes it as one
more read source; any Syzygy-authored record placed there is governed by
the outward limb (RFC4-5) and the durable authority stays in
`.syzygy/work/**` (RFC4-16) — the substrate's store is never the primary
home of Syzygy's run records [Observed: `06` §5.3 routing note; SDR-8].

---

## 4. Violation cases

1. *(RFC4-2/7)* An unregistered script's output feeds a deterministic claim;
   or an adapter upgrade silently reinterprets last month's observation
   records.
2. *(RFC4-5)* A Trajectory board stores an editable copy of scheduler status
   and syncs it back nightly; or a substrate-side `spec_id` edit is
   adjudicated as a contradiction instead of rendered as an annotation.
3. *(RFC4-8)* A field an old adapter version never emitted is backfilled
   with a default; an aggregate treats those defaults as data.
4. *(RFC4-10)* A work item whose spec anchor does not resolve is rejected
   from ingest; or the adapter guesses which renamed requirement an old
   anchor "must have meant".
5. *(RFC4-11/22)* Per-commit history for squash-merged work is rendered at
   commit granularity by parsing the squash body; a branch-name join renders
   without its convention basis.
6. *(RFC4-13)* `--quality-gate tests=pass` with no retained artifact turns
   an indicator green; a report evidencing SHA A is rendered current for
   SHA B; **or a well-formed test report a worker wrote and left on disk,
   naming the exact revision, is emitted `gate-backed` because it is
   retained, resolvable, and hash-carrying — origin unverified.**
7. *(RFC4-15)* The adapter hardcodes five statuses and drops items in
   `pinned`/`hooked`; or normalizes states itself instead of leaving the
   mapping to RFC 0008.
8. *(RFC4-16)* A fleet account silently omits work pruned by `bd gc`; or
   renders "no work existed" where the honest output is Unknown citing the
   retention event.
9. *(RFC4-19/21)* A run record with no cost data renders `$0.00`; a
   portfolio cost total sums twelve known and eight Unknown runs without
   disclosing coverage; **or a redispatched work item shows "1 run" because
   both attempts derived the same identity and no `indistinguishable-runs`
   label was emitted.**
10. *(RFC4-23)* A dead worker renders "active" because the coordinator's
    heartbeat is fresh and the worktree exists.
11. *(RFC4-24)* PR-level data answers a per-commit question by
    interpolation; a reduced-fidelity label is dropped in aggregation.
12. *(RFC4-26/27)* A code marker anchors a capability with no adopting
    policy; an empty Orrery plot renders "no code implements this" with no
    executed coverage record.

---

## 5. Integration

**Relies on RFC 0001:** entity classes and minting authorities (RFC1-5,
RFC1-9) — this RFC supplies the code-element identity obligations and the
execution-run identity realization RFC1 delegates; the act-assignment rule
(RFC1-23) classifying verification as observed and execution records as
execution; materialization records (RFC1-29) as the warrant join. **Relies
on RFC 0002:** the evidence semantics execution records satisfy; the tier
registry (RFC2-25) whose `gate-backed`/`report-fact`/`asserted-by-worker`/
`reduced-fidelity` tiers this RFC's observers emit; Unknown reasons
(RFC2-24); failure states (RFC2-23); the substrate-translation duty
(RFC2-17) realized by RFC4-6.

**Defects found in the foundations (reported, not silently diverged from):**

1. **RFC1-29 / RFC2-18 mismatch — resolved (retained for the trail).** This
   RFC reported that RFC2-18 required the reconciliation snapshot to include
   "the exact intent revision … as pinned in the immutable materialization
   record" while RFC1-29 defined that record as only (proposal identity →
   work-item identity set). **Satisfied by the RFC1-29 amendment of
   2026-07-30**: the materialization record now pins the exact warranted
   intent revision, and RFC1-5's materialization-record row carries it, so
   this RFC's warrant reference (RFC4-19) rests on a field RFC 0001
   requires. No RFC 0001 or RFC 0002 change is outstanding on this item
   (review 3, AS-R8).
2. **RFC1-5 "Verification run … run identity + input snapshot identity" —
   resolved (retained for the trail).** As reported: external CI runs
   identify the *revision under test*, not a Syzygy source snapshot, so read
   literally no external run could ever qualify, and this RFC interpreted
   "input snapshot identity" as the identified revision(s) the run claims to
   describe (RFC2-11's binding). RFC1-5's Verification run row now states
   that reading directly — "run identity + **identity of the revision(s)
   under test (the run's claimed subject, RFC2-11)**" [Observed — RFC1-5 as
   of 2026-08-01]. No RFC 0001 change is outstanding on this item.
3. **RFC1-5 execution-run identity "minted by the actuator toolchain via
   adapter" — resolved (retained for the trail).** As reported: no run
   identity exists in the installed toolchain [Observed: `04` §5.3], and a
   toolchain-only reading would leave these records identity-less until
   instrumentation lands — contradicting SDR-31 — so RFC4-19 read "via
   adapter" as licensing a deterministic adapter-derived identity, queryably
   labeled `derived`. RFC1-5's Execution run row now carries that licence
   upstream — "**Toolchain-emitted run identity where one exists, else
   adapter-derived deterministically and labeled `derived`**" [Observed —
   RFC1-5 as of 2026-08-01]. No RFC 0001 change is outstanding on this item;
   what the owner still rules is *whether* to derive at all (§8 q1), not
   whether RFC 0001 permits it.
4. **RFC1-6 delegates "first-class VCS entities" to RFC 0004 — resolved
   (retained for the trail).** As reported: RFC1-5 closes the V0-core
   vocabulary, which only an RFC 0001 amendment can reopen, so the
   delegation as written granted a power RFC1-5 reserves (no conflict
   materialized — this RFC declines the delegation, §6). RFC1-6 now closes
   the grant in its own text: first-class VCS entities "enter only through
   an amendment to this RFC informed by RFC 0004's findings — RFC 0004
   itself declines to mint them; **RFC1-5's closure is reopened by amendment
   here, never by delegation**" [Observed — RFC1-6 as of 2026-08-01]. No
   RFC 0001 change is outstanding on this item.

**Provides to:** **RFC 0003** — the registry, envelope, coverage-record, and
reduced-fidelity-label semantics it must physically encode; **RFC 0005** —
the machine-client surface adapters authenticate through, and the SEC-3
execution-profile boundary this RFC's observers stop at. RFC 0005's
run-envelope obligations (RFC5-18(e) profile identity and version; RFC5-21
policy-violation recording) are **carried as named rows of RFC4-19**, not as
a gesture in this section — the envelope's minimum content is stated in one
place (review 3, AS-R9). **RFC 0008** — the
faithful substrate-state feed (RFC4-15) its normalized work ontology maps,
and the liveness rules (RFC4-23) Trajectory renders; **RFC 0009** — the
coverage records (RFC4-27) behind every empty plot. **Not this RFC's:**
retention-bound and staleness-bound *values* (quality/evidence policy);
normalized work-state mapping (RFC 0008); live streaming and control
(deferred, SDR-5).

---

## 6. Alternatives considered

- **A new doctrine-level "captured execution evidence" class** (the research
  corpus's FRC-04-3 recommendation). Rejected by SDR-8, followed here: the
  Execution Record is an Evidence kind; the immutability and identity rules
  the proposed class wanted are delivered by RFC4-18/19 without a doctrine
  amendment or a new frozen noun.
- **Requiring toolchain instrumentation for V1** (FRC-04-5 option ii as a
  dependency). Rejected by SDR-31: derivation-first is the invariant;
  enrichment is a named roadmap. The reverse — derivation-only forever —
  is equally rejected: it would freeze model, cost, and liveness at Unknown
  permanently and forfeit the co-evolution the owner controls.
- **Primary run-record storage in the substrate's typed event store**
  (`bd --type event`). Rejected: Syzygy-authored durable records inside a
  scheduler-owned, GC-governed store invert the authority split (SDR-7/8)
  and put the fleet account under a retention horizon Syzygy does not own
  (RFC4-16). Permitted only as outward-limb pointers/enrichment.
- **Accepting worker report assertions as gate-backed Observed** because the
  report is machine-formatted. Rejected: the emit script formats the claim,
  it does not verify it; an LLM assertion is Inferred, never Observed
  [Observed: trust-and-evidence.md] — SDR-9 and RFC2-25 already draw the
  line this RFC enforces at the observer.
- **Hardcoding the scheduler status vocabulary** in the adapter. Rejected:
  the substrate's statuses are configurable and already drift from the
  toolchain's own docs; reading the vocabulary from the tool is the only
  form that survives substitution (RFC4-9).
- **Autonomous event-time capture daemons** to beat the squash-merge and gc
  horizons. Rejected: the loop is human-triggered [Observed:
  architecture.md]; the honest alternative is capture-before-horizon inside
  triggered passes plus labeled reduced fidelity when the horizon won
  (RFC4-16, RFC4-24).
- **First-class VCS entities** (commit/ref nodes). Declined: commits and
  PRs serve every current need as evidence artifacts and join fields
  (RFC1-6, RFC1-25); adding node types would reopen RFC1-5's closed
  vocabulary for no query this RFC needs.

### Post-draft adjustments (review 3)

- **`gate-backed` on retention and format alone** — the draft's original
  test, which discriminated on the *artifact's* properties (retained,
  resolvable, revision-bound) and not on any attestation that a gate
  actually ran. Rejected under AS-R3 and replaced by RFC4-13's
  three-route provenance predicate. An untrusted fleet worker (SEC-3's
actor class, extended to committed artifacts at RFC3-16(a)) could
  otherwise write a well-formed report naming the exact revision and have it
  enter at the one tier RFC2-25 lets support a positive status claim —
  and RFC5-19's "observation, not execution" boundary means the profile
  floor that would have capped a Syzygy-launched policy-violating run never
  applies to reading a file off disk. Craft-and-care's CC-TEST-2 already
  held this line; RFC4-13 was the weaker text. **Cost, deliberately taken:**
  projects with no confirmable CI lose green status on gates whose artifacts
  Syzygy cannot attribute; those claims convert to `report-fact`. Route 3
  (owner-declared trusted external oracle) is the escape hatch. Routed to
  acceptance as §8 q6.
- **A new `reduced-fidelity` cause, `indistinguishable-runs`** (RFC4-24,
  under AS-R4). The cause list is closed and extendable only by amending
  this RFC; this is that amendment, recorded here as a deliberate
  adjustment. It exists because deterministic derivation of run identity
  from identical inputs is non-unique across distinct-but-identically-keyed
  dispatches, and the draft stated no behavior for the collision — so as
  written it was silent, which is the one outcome VIS-1 forbids. The
  alternative of leaving the collision to §8 q1's ruling was rejected: the
  safeguard is normative under *either* ruling.
- **Deferring the capture-cadence obligation to policy without requiring
  a declaration** (RFC4-16, under AS-R16). Rejected: honest degradation that
  can be perpetually deferred bounds nothing. §8 q4's stricter option is
  taken — the quality policy must *declare* a maximum inter-pass interval
  tied to the retention bound. Enforcing it by scheduler was **not** taken:
  the loop stays human-triggered (architecture.md).

---

## 7. Deliberately deferred

Physical schemas for the registry, envelope, coverage records, and labels →
RFC 0003. Machine-client authentication for adapter/agent access, and every
execution-profile question (fresh test execution, build-required parsing) →
RFC 0005 (SEC-3 blocks until accepted). Normalized work-state vocabulary and
its projection of RFC4-15's feed → RFC 0008. Retention-bound, staleness-
bound, and currency-bound values → quality/evidence policy. Live streaming,
intervention, and control — deferred with telemetry as their entry criterion
(SDR-5). Inference-profile machinery over these sources (semantic
clustering, drift challenges) → RFC 0002's challenge lifecycle and the
inference profile; this RFC only feeds them deterministic inputs. Whether
per-subworker report contracts are worth an actuator change → the
co-evolution roadmap (RFC4-29), owner-paced.

---

## 8. Open questions for acceptance

1. **Adapter-derived run identity (RFC4-19).** Where the toolchain emits no
   run identity, this RFC has the adapter derive one deterministically,
   labeled `derived`. The alternative — run identity renders Unknown and
   records join on (work item, capture) only — is more austere and makes
   multi-attempt accounting near-impossible. Confirm derivation, or direct
   austerity? **The collision safeguard is not part of this question.**
   RFC4-20's rule — a derivation collision renders `reduced-fidelity` with
   cause `indistinguishable-runs` and the run count Unknown, never a silent
   single record — is normative *whichever way this is ruled* (review 3,
   AS-R4); ruling austerity narrows what is derived, it does not remove the
   obligation to disclose what could not be distinguished.

   > **ANSWERED at acceptance — B11.** **Derive, and disclose collisions.** Run identity is derived from what the adapter can see; where two runs collide, the surface renders an `indistinguishable-runs` marker with an Unknown count. Austerity (Unknown identity) is not taken — but the collision safeguard is normative either way: **never a silent single record**.
2. **Envelope minimality.** `terminal outcome` is required (R); a run whose
   worker vanished without any report would then be recordable only as an
   `unknown-terminal` outcome value. Should the envelope instead admit
   records with outcome Unknown-by-reason, keeping R for the field but not
   the value? Proposed: yes — the field is required, `unknown-terminal` is
   a legal value; stated here for explicit confirmation.
3. **Marker adoption granularity (RFC4-26).** Marker-sourced declarations
   activate per project by policy. Should activation be per-repository
   instead (a monorepo may want markers in one subtree only)? Proposed:
   the policy may scope itself; confirm. *(Scoping controls the blast
   radius; it does not touch the authenticity requirement — the adopting
   policy is honored only under RFC3-16(a) at any granularity.)*
4. **Capture cadence duty (RFC4-16) — resolved in the draft, confirm.**
   The contract makes un-captured horizon loss *honest* but cannot make it
   *rare*. **The stricter option was taken** (review 3, AS-R16): RFC4-16(2)
   now requires the quality policy to declare a maximum inter-pass interval
   tied to the declared retention bound, and claims depending on pre-horizon
   scheduler history render Unknown until it is declared. Declaring is the
   obligation; enforcing by scheduler is not — the loop stays
   human-triggered. Confirm, or direct that rendering the risk was enough?
5. **Defect resolutions (§5) — all closed; confirmation, not a decision.**
   Every defect this RFC reported against RFC 0001 has since been fixed in
   RFC 0001's own text: the RFC1-29 pinned-intent-revision gap by the
   amendment of 2026-07-30 (§5 defect 1, AS-R8), and the RFC1-5
   verification-run wording, the RFC1-5 execution-run identity licence, and
   the RFC1-6 delegation overreach in the drafts under review (§5 defects
   2–4). **No RFC 0001 touch-up remains outstanding, and this item blocks
   nothing at `ACCEPT FOUNDATIONAL RFCS`.** What is left is confirmation:
   the interpretations this RFC stated are now RFC 0001's normative wording,
   so accepting the pair accepts them as the reading of record. Confirm —
   or, if any of the four upstream amendments reads as having gone further
   than the defect it closes, name which.

   > **CONFIRMED at acceptance — all §5 defects closed.** *Recorded here because a stale confirmation is how a fixed defect becomes a live question:* during packet assembly the lead raised a decision item from this question's earlier wording ("what remains for an RFC 0001 touch-up") **without checking RFC 0001's current text**. All three reported defects were already fixed. The item was **retired, and the retirement recorded rather than deleted** — it is the same failure as a stale defect report, one layer up, and the clearest evidence for why the defect-freshness sweep exists.
6. **The `gate-backed` provenance predicate (RFC4-13) — added post-draft
   under review 3's AS-R3.** `gate-backed` now requires a qualifying
   provenance route, not merely a retained revision-bound artifact. **The
   cost is real:** a project whose CI Syzygy cannot independently confirm,
   or whose gate artifacts are written by the worker that ran them, loses
   green status on those gates — the claims convert to `report-fact` ("an
   artifact asserting Y exists"), which per RFC2-25 supports nothing
   positive. Some currently-plausible green renderings become honest
   non-green. **Route 3 — an owner-declared trusted-external-oracle
   policy — is the escape hatch**, and its existence should be confirmed
   rather than assumed: it lets the owner declare an oracle whose artifacts
   Syzygy honors at `gate-backed` without independent confirmation, at the
   owner's risk and under RFC3-16(a). Confirm the predicate and the escape
   hatch, or direct a narrower closure (e.g. routes 1 and 2 only, no owner
   override)?

   > **ANSWERED at acceptance — A2.** All **three** admission routes confirmed, with route 3 **bounded**: an owner-declared trusted oracle is scoped to a named (project, gate class) pair and carries an **expiry**; unscoped or expired, it backs nothing. A **fourth route** is added by the same decision — a deterministic, re-runnable diff-satisfies-clause check, for doc-only and governance-only work. See RFC4-13.

---

*End of RFC 0004. Clauses RFC4-1 … RFC4-29, with sub-clauses RFC4-13(a) and RFC4-13(b).*
