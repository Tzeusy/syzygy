---
id: RFC-0004
title: Observation Sources and Evidence — named adapters, gate provenance, and capture duties
status_source: owner-act-record
module: named-adapters
clauses: RFC4-10..RFC4-17 (sub-clauses RFC4-13(a), RFC4-13(b); no gaps, no retirements, no merges)
governs: [openspec-adapter, vcs-adapter, hosting-sub-adapter, code-structure-observer, gate-observers, trusted-external-oracles, governed-checkers, runtime-observer, scheduler-adapter, capture-before-horizon, warrant-pointer]
applies_to: [kernel, trajectory, orrery]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0005]
tags: [adapters, gate-tiering, provenance, capture-before-horizon, anchors, sdr-3, sdr-7, sdr-9, sdr-32, sdr-33, sec-3, sec-5]
---

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — as an owner-adopted bootstrap act until the
independent A1 correlation mechanism exists, and as a Syzygy-verified effective
act only after correlation (RFC3-16). Absent such a record, this contract binds
nothing.

**Package:** module 2 of 4 of the RFC 0004 contract package. Index, clause map,
lookup rule, package-level integration and deferrals: `README.md`. Rationale,
amendment history, alternatives, and answered §8 questions:
`../../history/RFC-0004-history.md`.

**Serves:** VIS-1, VIS-2, VIS-5, VIS-6; SEC-3, SEC-4, SEC-5; architecture.md
(typed authority; the human-triggered loop); trust-and-evidence.md (staleness;
the trust floor); v1.md (V0 scope). Implements **owner rulings** SDR-3, SDR-7,
SDR-9, SDR-32, SDR-33, and carries owner decision **A2** (the four-route
`gate-backed` provenance predicate).

---

## 0. Module scope and reader map (non-normative)

*If this section and a clause disagree, the clause wins.*

This module owns **the named integrations and what each may and may not
claim**: the OpenSpec adapter and its anchors (RFC4-10); the git/VCS adapter
with its hosting sub-adapter and the squash-merge fidelity rule (RFC4-11); the
code-structure observer and its identity scheme (RFC4-12); the test/CI/gate
observers and the **four-route `gate-backed` provenance predicate** with its two
supporting artifacts (RFC4-13, RFC4-13(a), RFC4-13(b)); the runtime observer
(RFC4-14); the Beads/scheduler read contract (RFC4-15); the
capture-before-horizon duty (RFC4-16); and the warrant pointer (RFC4-17).

Read it to answer: *what is this source allowed to tell me, and what tier does
its evidence enter at?* The load-bearing rule is RFC4-13's: **a green gate
requires provenance, not just a file.** A retained, well-formed, revision-bound
artifact of unverifiable origin caps at `report-fact` — "an artifact asserting
Y exists" — because format and hash-carrying prove non-tampering, not
genuineness. Three of this module's clauses carry **authorization-bearing**
declarations honored only under RFC3-16(a): the trusted-external-oracle policy
(RFC4-13 route 3), the governed checker definition (RFC4-13(b)), and the
scheduler retention bound with its inter-pass interval (RFC4-16).

These adapters must satisfy the general contract (module 1); the records they
feed are module 3's; the fidelity labels and join bases they emit are module
4's.

---

## 3. The contract

Clauses are numbered `RFC4-n` for stable citation. Amend in place; retire
rather than renumber.

### 3.3 Named adapters and observers

Each names its authority boundary, minimum read surface, and degraded modes.
These bind the *initial substrate* integrations; the roles are substitutable
under RFC4-9.

**RFC4-10 — OpenSpec adapter.** *Authority:* the behavioral-requirements
system — content and identity of requirements and scenarios under the
constitutional OpenSpec artifact contract; never intent adjudication, never
status. *Reads:* per-artifact content and hash pinned to the repository
revision; requirement/scenario identities; declared relationships;
change-proposal state; the artifact-contract version (itself a snapshot
input). *Anchors (SDR-32):* the adapter declares its **spec-anchor scheme** in
the registry — how a requirement/scenario reference resolves to an artifact
location. Every anchor it emits must be resolvable at the snapshot carrying it
(trust-floor link rule); an anchor that does not resolve, or a work
item/execution record with no anchor at all, renders **Unknown — never a
rejection** of the project, the event, or the record. Whether OpenSpec
identities survive edit and rename is [Unknown] (RFC1-15); the adapter
therefore declares its anchor **stability class** (identity-stable vs
content-hash vs path+heading), and where continuity across an edit cannot be
established it renders the reference Unknown rather than guessing a successor.
*Degraded modes:* unreadable artifacts → RFC2-23 source-unreachable; a
malformed artifact is a fact about the source, rendered as such, never
silently skipped.

**RFC4-11 — Git/VCS adapter (with hosting sub-adapter).** *Authority:* version
history only — never intent, never observed behavior [Observed:
architecture.md]. *Reads:* repository identity → revision map; ref → tip map;
working-tree state descriptor; commit facts (SHA, parents, author/committer
identities and instants, message, changed-path summary); branch existence;
and, through the hosting sub-adapter, PR facts (identity, head SHA, base,
state, created/merged instants, review decision, review threads, check
conclusions) and **merge facts**. A merge fact comes only from this adapter —
never inferred from scheduler closure (RFC2-20). *Writes:* only the commit-out
of Syzygy-authored governance artifacts into the two namespaces (VIS-5/VIS-6),
attributed and revertable (SEC-4). *Fidelity (SDR-33):* where the toolchain's
merge path is squash-plus-branch-deletion, per-commit facts for closed work
become unreachable [Observed]. The adapter emits event-time-grade commit
evidence **where available** (in-flight and unmerged work, or captured before
deletion) and otherwise emits PR-granularity facts explicitly labeled
`reduced-fidelity` with cause `post-merge-history-unreachable` (RFC4-28) — it
never reconstructs commit history it cannot reach. *Degraded modes:*
unreachable remote or hosting API → last-good marked stale; a SHA referenced
by evidence but no longer reachable renders the reference broken, not the
evidence deleted.

**RFC4-12 — Code-structure observer.** *Authority:* what code exists —
structure only, never semantic ownership (SDR-3). *Reads:* file inventory
within consented scope (secret exclusions applied and counted, SEC-5, **under
the observing project's own secret-detection policy — never the observed
source's**, RFC3-30 — and only a version of that policy whose owner-act
provenance verifies under **RFC3-16(a)**, since a worker-minted policy would
let this observer index the content SEC-5 requires excluded); symbols,
modules, containment; deterministically observed structural relations
(`calls`, `exposes`, `accesses`) with parser version identified.
*Code-element identity (obligation from RFC1-5):* adapter-defined and **not
path-only**. The scheme, declared per language in the registry, must derive
identity from at least (repository identity, element kind, language-qualified
symbol name) with a content digest as disambiguator, so a file move preserving
the qualified name preserves identity. Where continuity cannot be established
across a change, the observer reports new/retired elements and lets the
kernel's successor machinery render the change (RFC1-11) — it never silently
re-binds an identity by similarity. *Boundary:* static parsing only; anything
requiring the project's toolchain to execute is blocked until the
execution-profile RFC (SEC-3).

**RFC4-13 — Test, CI, and gate observers.** *Authority:* verification evidence
as it exists on disk or in CI systems — this observer reads reports and
never executes anything; execution happens only through RFC5-18's profiled
launch gate, whose retained outputs route 1 below then reads (SEC-3)
[Observed: v1.md V0 scope]. *Reads:* report identity and hash;
suite/case identities and outcomes; **the revision the report claims to
describe** — a report is evidence only for that revision (RFC2-11); CI run
identity, conclusion, instants, and log/artifact references.

*Gate tiering (SDR-9; RFC2-25):* a gate outcome is emitted `gate-backed` only
when **both** predicates hold — the **retention/format predicate** (a
retained, resolvable artifact bound to the exact revision is captured with it)
**and the provenance predicate below**. A structured report asserting an
outcome without such an artifact is emitted `report-fact` (the report's
existence and content are Observed; the outcome is not); a bare LLM assertion
is emitted `asserted-by-worker`. The observer never upgrades a tier; only new
evidence in a new snapshot can.

*Provenance predicate on `gate-backed`* (owner decision **A2** confirmed the
three routes and bounded route 3; route 4 was added by the Tier C
**RFC 0002 §8 q3** ruling in the same record; history §RFC4-13). An artifact
qualifies for `gate-backed` only through **exactly one of four routes**:

1. it was **produced by a Syzygy-launched profiled run** (RFC5-21), and so
   passed the isolation floor that exists to contain untrusted code;
2. it is **carried by an external CI or hosting system whose run identity and
   authenticity the sub-adapter independently confirmed at observation time
   and captured** (the hosting sub-adapter's PR/check facts, RFC4-11) —
   confirmation by the system, not by the artifact's own content, and the
   confirmation itself is a captured artifact inside snapshot identity, per
   **RFC4-13(a)**, never a query re-run against the provider at some later
   read;
3. it is **covered by an owner-declared trusted-external-oracle policy** in
   the governance plane, naming the oracle and the scope it may back — a
   policy that is itself **authorization-bearing and therefore honored only
   under RFC3-16(a)**. Such a policy is scoped to a named **(project, gate
   class)** pair and **carries an expiry**; it may not be declared
   project-wide, gate-class-wide, or indefinitely. An expired or unscoped
   oracle declaration backs nothing and the artifacts under it fall to
   `report-fact`. The bound exists because route 3 is the only route whose
   sufficiency rests on the owner's word rather than on capture: without scope
   and expiry, a single declaration silently makes everything `gate-backed`
   forever, and nothing in this contract would later surface that it had;
4. it is the recorded execution of a **governed checker** — a deterministic,
   re-runnable satisfaction check over a declared diff and the clause it
   claims to satisfy, where the checker's definition is lawfully governed for
   that clause or clause class and the execution artifact binds exact inputs
   and revisions, both per **RFC4-13(b)**. This route exists for
   **documentation-only and governance-only work**, which has no execution
   gate to run and would otherwise cap permanently at `report-fact`.
   [Inferred] Determinism and re-runnability are **necessary but not
   sufficient** — a checker whose body is `return PASS` is deterministic,
   re-runnable, and certifies nothing (RFC4-13(b)'s acceptance test); what
   makes the route lawful is governance of *what the check means* on top of
   determinism of *how it runs*. A check whose inputs are not
   snapshot-identified, whose verdict a re-run can change, or whose definition
   is not lawfully governed for the clause it certifies is **not** this route
   and its outputs cap at `report-fact`.

A retained, well-formed, revision-bound artifact of **unverifiable origin caps
at `report-fact`** — "an artifact asserting Y exists" — which per RFC2-25 can
never support a positive status claim (Aligned, Converged, reconciled, green).
[Inferred] Format, retention, and hash-carrying prove **non-tampering, not
genuineness**: an untrusted fleet worker (SEC-3's actor class, extended to
committed artifacts at RFC3-16(a)) with ordinary write access can author a
syntactically valid report naming the exact revision. Craft-and-care states
the routes-1-and-2 capture side of this rule — "a report the worker itself
wrote and attached is an emitter-captured **report fact** …
integrity-verifiability proves non-tampering, not genuineness" (CC-TEST-2,
whose rev7 amendment naming routes 3 and 4 as the owner-created exceptions
with their own guards is confirmed by its own owner act — until that act,
CC-TEST-2 stands in its unamended form) — and this clause carries the full
four-route model. Routes 1 and 2 both amount to **capture by an observer
distinct from the emitter**; route 3 is the owner's explicit escape hatch for
oracles Syzygy cannot itself confirm.

*Degraded modes:* revision mismatch → stale on the primary surface; missing
referenced artifact → the outcome's tier drops and the dangling reference
renders broken; **origin unverifiable under all four routes → the outcome caps
at `report-fact`, rendered with that cap visible, never rejected**.

**RFC4-13(a) — The external-confirmation capture artifact.** When route 2 is
exercised, the confirming sub-adapter performs the confirmation **at
observation/capture time** and mints an **external-confirmation capture
artifact** recording, at minimum:

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
and evaluations consume **only captured, identified inputs** (RFC2-2): route 2
is satisfied by the captured confirmation, never by a live query. "Read time"
in any statement about this route means **the adapter's observation/capture
time**, not the time a surface later displays or a query later resolves the
evaluation. Consequently: a provider that later expires its run records
**changes nothing** about any existing observation record — the record is
immutable (RFC2-6) and its tiers stand as evaluated; a **re-confirmation
attempt is a new observation** producing a new snapshot and new evaluation,
which may lawfully find the provider no longer confirms and degrade the tier
there (RFC2-4); and an evaluation whose route-2 evidence lacks a resolvable
capture artifact treats the route as unsatisfied and caps at `report-fact`.
[Inferred — the artifact schema; Observed — the immutability and consumption
rules it restates from RFC2-1/2/6.]

**RFC4-13(b) — The governed checker.** Route 4 has two artifacts, and
`gate-backed` requires both.

A **governed checker definition** is a governance-plane artifact carrying, at
minimum:

1. a **stable checker identity** and a **version/content identity** (the exact
   checker text or binary digest);
2. **declared applicability** — which clause identities or clause classes it
   may certify, and for what work classes (documentation-only,
   governance-only);
3. **declared satisfaction semantics** — what, in human-reviewable terms, a
   PASS asserts about the diff against the clause;
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
revision pair** checked; the **exact clause revision** certified against; the
**exact checker identity and version** run; the **exact inputs** consumed (all
snapshot-identified); the **deterministic result** in the checker's output
vocabulary; and capture provenance (executing party, capture instant, and —
where the run was Syzygy-launched — the RFC4-19 execution-record linkage).

**Separation of authorship and certification.** A worker **may run** a
governed checker over its own change; it may **not author, select, or amend**
the checker definition that certifies that same change — a change and the
authority that certifies it may not originate in the same untrusted act, and a
checker definition edit rides the same adoption gate as any other
authorization-bearing artifact, never lands silently. An execution artifact
naming a checker version whose adoption provenance does not verify, or whose
declared applicability does not cover the clause certified, is not route 4 and
caps at `report-fact`. **Acceptance test this clause must survive:** a checker
whose body is `return PASS` — deterministic, re-runnable, and certifying every
diff — cannot lawfully back a `gate-backed` outcome, because its satisfaction
semantics cannot truthfully state what a PASS asserts, and no lawful adoption
of that semantics for a real clause class exists. [Inferred — the two-artifact
contract; Observed — the RFC3-16(a) predicate it instantiates.]

**RFC4-14 — Runtime observer.** *Authority:* runtime observations. *Reads:*
externally produced datasets, traces, and incident records, each with **the
window it covers**, its capture instant, and the deployed revision it
describes — dataset and window are both snapshot inputs [Observed:
architecture.md]. A one-off capture is legitimate evidence; reproducibility is
a declared property of the class, not a prerequisite [Observed:
trust-and-evidence.md]. *Boundary:* ingestion only; collection requiring
execution of observed code is blocked under SEC-3.

**RFC4-15 — Beads adapter: the read contract.** *Authority:* work lifecycle
state, after materialization only (SDR-7) — never intent, never observed
behavior, never why the work exists [Observed: architecture.md]. *Reads:*
work-item identity (emitted as the substrate-neutral identity with `bead_id`
as its substrate-qualified alias, RFC4-6); **the status vocabulary as the tool
declares it** — statuses and their categories read from the substrate
(`bd statuses`, including custom statuses), transmitted verbatim with the
export's capture instant, never hardcoded: the installed toolchain's own
documentation covers only five of the substrate's seven built-in statuses
[Observed], and the adapter must not inherit a client's drift. Also: assignee;
dependency edges with their types; labels; `external_ref`; notes blocks as
opaque annotated text; created/updated/closed instants; and transition history
(`bd history`, `--as-of`) **within the declared retention bound** (RFC4-16).
The **normalized work-state mapping** into Trajectory's vocabulary is
RFC 0008's; this adapter's duty ends at faithful, capture-stamped
transmission. *Writes* (each an explicitly authorized adapter effect):
work-item creation at materialization; lifecycle mutations commanded through
Syzygy surfaces (synchronous, attributed, re-read after write); and warrant
pointers under RFC4-17. *Degraded modes:* export unavailable → last-good
marked stale; replace-in-place note fields (heartbeat, review-cycle) are
current values, not histories — the adapter emits them as such,
`reduced-fidelity` with cause `replace-in-place-source` for any per-cycle
question [Observed].

**RFC4-16 — Capture-before-horizon.** The scheduler substrate forgets by
default: `bd gc` deletes closed issues past a default horizon, `bd prune`
permanently deletes closed beads with their dependencies, labels, events, and
comments, and `compact`/`flatten` squash the underlying history; the issue
database is not in the git tree [Observed]. Therefore:

1. Scheduler history is a **convenience, never an authority**, for anything
   older than the declared retention bound. The bound is a declared policy in
   the governance plane and a snapshot input; until declared, claims depending
   on scheduler history render Unknown (`no-currency-bound-declared`
   mechanics, RFC2-9 applied to retention). The bound is an owner-approved
   policy declaration that unblocks claims and is therefore honored **only
   under RFC3-16(a)** — a retention bound an untrusted writer could mint would
   unblock exactly the claims the horizon is supposed to render Unknown. The
   same holds for RFC2-9's currency-bound declaration wherever this RFC's
   observers depend on it.
2. Every scheduler-resident fact a durable Syzygy record depends on — the run
   envelope's inputs, materialization joins, transition history feeding an
   account — must be captured into Syzygy-owned artifacts (Execution Records,
   observation records) **before** the horizon. Capture runs inside ordinary
   human-triggered observation passes (RFC2-19); the operational obligation is
   that passes be run within the horizon, and the contract's obligation is
   honesty when they were not. **The quality policy must declare a maximum
   inter-pass interval tied to the declared retention bound**, so pre-horizon
   history loss is *bounded* rather than merely rendered honestly; until that
   interval is declared, claims depending on pre-horizon scheduler history
   render Unknown on the same mechanics as an undeclared bound — and, on the
   same mechanics again, the interval is honored **only under RFC3-16(a)**,
   since it gates the same claims by the same route and an untrusted writer
   could otherwise declare an interval wide enough to unblock them while
   bounding nothing. **Declaring the interval is the obligation; running a
   scheduler that enforces it is not** — the loop stays human-triggered
   (architecture.md), so the contract binds the declaration and the honest
   rendering when the declared interval was exceeded, never an autonomous
   trigger.
3. A fact lost to the horizon before capture renders **Unknown citing the
   retention event** — never silently absent, and never "no work existed".
4. Per-record substrate protections (`pinned`, `--no-history`) may be used as
   supplements but never as the primary durability guarantee — they live in a
   store Syzygy does not own.

**RFC4-17 — The warrant pointer (outward limb applied).** At materialization,
the adapter writes the warrant reference (resolvable spec anchor or decision
identity) into the substrate's provenance field (`spec_id`/metadata) as a
**derived, re-derivable pointer** under RFC4-5: the `.syzygy/work/**`
materialization record stays authoritative; a substrate-side edit of the field
is rendered as an annotation ("edited in substrate at T; not a warrant claim")
and the pointer is re-asserted at the next evaluation — no contradiction is
manufactured on the chain's load-bearing join.

---

## 4. Violation cases

*Package numbering; cases are distributed across modules, never renumbered.*

4. *(RFC4-10)* A work item whose spec anchor does not resolve is rejected from
   ingest; the adapter guesses which renamed requirement an old anchor "must
   have meant".
6. *(RFC4-13)* `--quality-gate tests=pass` with no retained artifact turns an
   indicator green; a report evidencing SHA A is rendered current for SHA B;
   **or a well-formed test report a worker wrote and left on disk, naming the
   exact revision, is emitted `gate-backed` because it is retained,
   resolvable, and hash-carrying — origin unverified.**
7. *(RFC4-15)* The adapter hardcodes five statuses and drops items in
   `pinned`/`hooked`; or normalizes states itself instead of leaving the
   mapping to RFC 0008.
8. *(RFC4-16)* A fleet account silently omits work pruned by `bd gc`; or
   renders "no work existed" where the honest output is Unknown citing the
   retention event.

Case 5 spans this module and module 4 and is held at the package level
(`README.md` §4).

---

## 5. Integration (module-local)

**Relies on RFC 0001:** the code-element identity obligation RFC1-5 delegates
and the successor machinery (RFC1-11) this module's observer defers to; the
[Unknown] status of OpenSpec identity survival (RFC1-15). **On RFC 0002:** a
report is evidence only for the revision it claims (RFC2-11); merge facts are
never inferred from scheduler closure (RFC2-20); the tier registry (RFC2-25);
the new-snapshot path (RFC2-4) and record immutability (RFC2-6) that make a
captured confirmation final; ordinary human-triggered observation passes
(RFC2-19); the currency-bound mechanics (RFC2-9) applied to retention; failure
states (RFC2-23). **On RFC 0003:** RFC3-16(a) gating the secret-detection
policy version (RFC4-12), the trusted-oracle policy and governed checker
(RFC4-13/13(b)), and the retention bound and inter-pass interval (RFC4-16);
RFC3-30 fixing whose secret-detection policy applies. **On RFC 0005:** the
Syzygy-launched profiled run that satisfies route 1 (RFC5-21), and the SEC-3
execution-profile boundary at which RFC4-12 and RFC4-14 stop.

**Provides to RFC 0008:** the faithful, capture-stamped substrate-state feed
(RFC4-15) its normalized work ontology maps — the normalized mapping itself is
RFC 0008's, never this adapter's. **To RFC 0011:** the capture-time evidence
identity and adapter-boundary semantics a context packet binds against,
including RFC4-13(a)'s rule that "read time" means the adapter's
observation/capture time.

---

## 8. Owner questions

*Package numbering; answered items keep their number and their reasoning is in
`../../history/RFC-0004-history.md` §8. Full package index: `README.md` §8.*

4. **Capture cadence duty (RFC4-16) — OPEN (confirmation).** The contract
   makes un-captured horizon loss *honest* but cannot make it *rare*. The
   stricter option was taken: RFC4-16(2) requires the quality policy to
   declare a maximum inter-pass interval tied to the declared retention bound,
   and claims depending on pre-horizon scheduler history render Unknown until
   it is declared. Declaring is the obligation; enforcing by scheduler is not
   — the loop stays human-triggered. **The interval value itself remains an
   undeclared open default, as do the retention, staleness, and currency
   bounds** (`README.md` §7). Confirm, or direct that rendering the risk was
   enough?
6. **The `gate-backed` provenance predicate (RFC4-13).** **ANSWERED — owner
   decision A2 plus the Tier C RFC 0002 §8 q3 ruling:** A2 confirmed all
   three admission routes and bounded route 3 to a named (project, gate
   class) pair with an expiry; the §8 q3 ruling added the fourth route
   for doc-only and governance-only work. The deliberately accepted cost —
   projects whose CI Syzygy cannot independently confirm lose green status on
   those gates, which convert to `report-fact` — is recorded in history.
