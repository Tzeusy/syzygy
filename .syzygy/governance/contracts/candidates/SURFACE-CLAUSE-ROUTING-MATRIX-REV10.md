> # SUPERSEDED — 2026-08-05b
>
> **This revision is retained as history and must not be used to decide
> whether anything may be implemented.** It is replaced by
> [`SURFACE-CLAUSE-ROUTING-MATRIX.md`](SURFACE-CLAUSE-ROUTING-MATRIX.md),
> which routes all **199** clause identities of RFC 0006–0011 into the four
> routes (OS / N/A / CR / IR), one route each.
>
> Why it was replaced, in one line: this file used `DESIGN-INVARIANT (DI)` as
> though it were a routing decision. It is not — it answers *does this stay in
> the RFC?*, not *does this have behavior a spec must pin?* — so 129 DI rows
> here carry **no routing decision at all**, RFC-0006 has **zero** rows, and
> RFC-0007 is enumerated at 39 rows against 45 declared clause identities.
> Re-deciding those DI rows on the merits moved 47 of RFC-0009's 50 to OS.
>
> Nothing in this file is wrong about *what a clause says*; its rationale
> column was a useful input to the replacement. It is wrong about *coverage*,
> and coverage is what it was consulted for.

# Surface-clause routing matrix — rev10 regeneration (directive §10)

**Regenerated at the rev10 compaction.** All rev9 clause identities and
classifications carry forward unchanged — the compaction retired, merged,
and renumbered nothing (04-CLAUSE-MIGRATION-MATRIX). Deltas in this
regeneration: (1) module targets — RFC 0007/0008/0009 clauses now live in
package modules (lookup rules in each package README; the class and
routing of every row is unchanged); (2) two new contracts, RFC-0010 and
RFC-0011, classified in their own sections below; (3) the binding phase
rule now comprises **six** clauses — RFC6-28, RFC7-38, RFC8-32, RFC9-52,
**RFC10-16, RFC11-12** — all shape-parallel ("this contract schedules
nothing"); (4) a clause-to-future-spec coverage skeleton is appended.
The stated judgment on RFC 0001–0005 (their observable consequences pass
through the rule-carrying contracts; any bypass found is a gap to route,
never a licence to schedule) **now extends to RFC-0010/0011's own
dependencies the same way**.

New future-spec domains minted for routing (provisional):
`spec/mission-control`, `spec/context-packets`, joining the rev9 set.

---


**Status:** Working routing aid, produced at the rev7 rework (Pass B, B1).
**Date:** 2026-08-02
**Purpose:** classify every normative clause of the three surface RFCs by
where its content belongs *after* foundational acceptance, so the later
`project-feature-request` phase can turn OPENSPEC-CANDIDATE rows into
specification deltas without re-litigating the contracts. **This file is not
a contract and creates no OpenSpec changeset.** Where it and an RFC clause
disagree, the clause wins.

## The five classes

| Class | Meaning | Where it lands |
|---|---|---|
| **DESIGN-INVARIANT** (DI) | Binds any conforming implementation; stays normative in the RFC | Retained in the RFC, cited by later specs |
| **OPENSPEC-CANDIDATE** (OS) | Concrete behavior to be specified as owner-approved OpenSpec requirements post-acceptance | Future OpenSpec domain named per row; the RFC keeps the constraint, OpenSpec gets the elaboration |
| **CRAFT-OR-RELEASE-POLICY** (CR) | Testing, review, release-gate, or process obligation | Craft-and-care / the `governance/policies/**` release policy |
| **INFORMATIVE-RATIONALE** (IR) | Context and reasoning; binds nothing | Retained in the RFC as non-normative text |
| **DI + OS** | A mixed clause whose invariant limb stays normative in the RFC while a named limb routes to a future spec domain | Both columns of its row name their target; the rationale names the retained DI limb explicitly (rev10 formalization of the rev9 "DI row with a routed limb" convention) |

A clause with mixed content is classed by its **dominant normative
content**, with the split named in the rationale column. Bracketed
`[Inferred]`/`[Observed]` passages and §0/§1/§5/§6 prose are IR by
definition and are not enumerated row-by-row; §7 boundary sections are IR
**except** where an entry states an obligation does not defer — those two
obligations are enumerated in their own section below.

Future OpenSpec domains referenced below (names provisional, minted here
only for routing): `spec/intent-surface`, `spec/work-surface`,
`spec/map-surface`, `spec/map-scenes`, `spec/map-lenses`,
`spec/selection-api` (RFC 0006's post-acceptance wire material).

## RFC 0007 — Polaris (intent surface)

| Clause | Class | Routes to | Rationale |
|---|---|---|---|
| RFC7-1 | DI | RFC | Surface charter; projection-only authority |
| RFC7-2 | DI | RFC | Composition-never-custody; per-claim anchoring floor |
| RFC7-3 | DI | RFC | Nothing cites the rendering; deletion invariant |
| RFC7-4 | DI | RFC | Non-authority total across narrative states |
| RFC7-5 | DI + OS | RFC; routed limb per rationale | Entity ontology; concrete schemas → `spec/intent-surface` |
| RFC7-6 | DI | RFC | One primary narrative per project |
| RFC7-7 | DI | RFC | Governed-presentation-artifact class (SDR-13) |
| RFC7-8 | DI | RFC | Narrative neither cache nor governance authority |
| RFC7-9 | DI | RFC | Citation unit granularity/covering/minimality |
| RFC7-10 | DI + OS | RFC; routed limb per rationale | Typed anchor contract; concrete anchor syntax → `spec/intent-surface` |
| RFC7-11 | DI | RFC | Broken anchor ⇒ Unknown, never silent |
| RFC7-11(a) | DI | RFC | Drifted anchor rendering; never silently current |
| RFC7-12 | DI | RFC | Restatement discipline (about, never instead-of) |
| RFC7-13 | DI + OS | RFC; routed limb per rationale | Disclosure obligation is DI; the named **V0 default path** is OS → `spec/intent-surface` |
| RFC7-14 | DI | RFC | Verbatim requirement leaf |
| RFC7-15 | DI | RFC | Catalog is a projection; honesty floor |
| RFC7-16 | DI + OS | RFC; routed limb per rationale | Three only-home invariants: status kernel-computed at an identified evaluation with the label + tier + reason + freshness vocabulary carried **verbatim**; **tier in the at-rest set** (fixed here, nowhere upstream); no composite number until an owner-adopted definition. The SDR-17 minimal-density default and its disclosure interaction are the OS part → `spec/intent-surface` |
| RFC7-17 | DI + OS | RFC; routed limb per rationale | The three authority classes are foundational DI; the three-band count and ordering are a **V0 default under B7** — the same split as RFC7-13 — with the default's elaboration OS → `spec/intent-surface` |
| RFC7-18 | DI | RFC | Never a second computation or copy |
| RFC7-19 | DI | RFC | Empty renders honest |
| RFC7-20 | DI | RFC | Draft state non-citable |
| RFC7-21 | DI | RFC | Adoption is a human act (RFC3-16(a) consumer) |
| RFC7-22 | OS | `spec/intent-surface` | Pending-draft queue mechanics. Retained DI: the queue is **Trajectory's** (SDR-18; RFC7-24/RFC8-9 depend on it), and a rejected draft **leaves the intent surface entirely** — never retained as half-adopted prose — with the rejection recorded on the queue's work item |
| RFC7-23 | DI | RFC | Acts-and-gates table |
| RFC7-24 | DI | RFC | SDR-18 seam with Trajectory |
| RFC7-25 | CR | Review/release policy | Review cadence/process is CR. Retained DI: the **computable materiality floor** (reading order, section set, anchor targets, manifesto/thesis always material); **B6's asymmetric declaration** (a party may declare material, never immaterial); the verdict honored **only under RFC3-16(a)** — an unverifiable pass does not clear the freeze; "on the surface" is a rendering duty, never a storage location |
| RFC7-26 | DI | RFC | Two reading modes in kernel vocabulary (`Base`/`Proposed`) |
| RFC7-27 | DI | RFC | No fictitious consensus |
| RFC7-28 | DI | RFC | Curated diagrams are narrative content under RFC7-2 |
| RFC7-29 | DI | RFC | Boundary table (what this RFC does not own) |
| RFC7-30 | CR | Release policy | Comprehension-test criterion consumed by the RFC9-45-shared release policy. Retained DI: the non-visual run is **RFC7-34's evidence limb** — a DI clause's proof obligation, not process |
| RFC7-31 | CR | Release policy | Verdict discipline is CR. Retained DI: fail-closed floors — absent record ⇒ **Unknown, never met**; judgment honored only under **RFC3-16(a)** (unverifiable ⇒ Unknown, never met); the two non-judgment failure floors (dangling link; surface-attributable wrong answer); artifact homes (records/, decisions/) via RFC 0003 |
| RFC7-32 | CR | Release policy | Cadence is CR. Retained DI: the record home named by RFC7-25/31 |
| RFC7-33 | DI | RFC | Machine parity of every distinction |
| RFC7-34 | DI + OS | RFC; routed limb per rationale | Non-visual recoverability; concrete interaction → `spec/intent-surface` |
| RFC7-35 | DI | RFC | Multi-project entry from workspace manifest only |
| RFC7-36 | DI | RFC | Portfolio narrative owner-local, never project truth |
| RFC7-37 | DI | RFC | Subprojects render as declared relations |
| RFC7-38 | DI | RFC | Binding phase rule: no implementation of observable behavior scheduled from this RFC alone; coverage matrix required at surface specification (rev8 item 7) |

## RFC 0008 — Trajectory (work surface)

| Clause | Class | Routes to | Rationale |
|---|---|---|---|
| RFC8-1 | DI | RFC | Three state planes rendered, labeled |
| RFC8-2 | DI | RFC | Binding anti-thesis (a)–(c) |
| RFC8-3 | DI | RFC | Rebuildable projection (VIS-6) |
| RFC8-4 | DI | RFC | No new kernel entity |
| RFC8-5 | DI | RFC | Deliberate non-reifications recorded |
| RFC8-6 | DI | RFC | Compaction record durable and identified |
| RFC8-7 | DI | RFC | Approved-Proposal lifecycle rendering |
| RFC8-8 | DI | RFC | "What remains?" enumerates three labeled planes |
| RFC8-9 | DI | RFC | Drafting-queue ownership (SDR-18) |
| RFC8-10 | DI | RFC | Materialization one-way door |
| RFC8-11 | DI | RFC | Divergence renders; never adjudicated by surface |
| RFC8-12 | DI | RFC | Closed thirteen-value normalized state vocabulary; substrate mapping artifact is RFC3-16(a) material |
| RFC8-13 | DI | RFC | Derivation table, one row per value |
| RFC8-14 | DI + OS | RFC; routed limb per rationale | Raw provider status visible behind disclosure; disclosure interaction → `spec/work-surface` |
| RFC8-15 | DI | RFC | Closure is not "done" |
| RFC8-16 | DI | RFC | `active` needs a signal within a declared bound; fail-closed |
| RFC8-17 | DI | RFC | `blocked` cause taxonomy closed |
| RFC8-18 | DI | RFC | Cost as independent measures, never composite |
| RFC8-19 | DI | RFC | Absent means Unknown, never zero |
| RFC8-20 | OS | `spec/work-surface` | V1 telemetry staging is OS. Retained DI (only home of both): **nothing at V0 may simulate telemetry**, and V1 telemetry renders **exclusively from captured Execution Records** — constraints on whatever is later specified, not behavior to specify |
| RFC8-21 | DI | RFC | Warrant chain walkable both directions |
| RFC8-22 | DI | RFC | Broken join renders |
| RFC8-23 | DI | RFC | Unwarranted work renders as such |
| RFC8-24 | DI | RFC | Unknown-reason renderings with resolution routes |
| RFC8-25 | DI | RFC | Inherited-mutation coverage test; the "small" threshold declaration is owner policy (§8 q6) |
| RFC8-26 | DI | RFC | Binding preservation set |
| RFC8-27 | DI | RFC | Expired-detail rendering; capture-time confirmation (RFC4-13(a)) |
| RFC8-28 | DI | RFC | Chain states first-class and queryable |
| RFC8-29 | DI | RFC | V0 absence rendered honestly |
| RFC8-30 | DI | RFC | Closure fallacy forbidden |
| RFC8-31 | DI | RFC | RFC 0006 conformance |
| RFC8-32 | DI | RFC | Binding phase rule: no implementation of observable behavior scheduled from this RFC alone; coverage matrix required at surface specification (rev8 item 7) |

## RFC 0009 — Orrery (map surface)

| Clause | Class | Routes to | Rationale |
|---|---|---|---|
| RFC9-1 | DI | RFC | Surface scope incl. historical (D1) |
| RFC9-2 | DI | RFC | Semantics-and-determinism-only boundary |
| RFC9-3 | DI | RFC | Encoding explainability from identified artifacts |
| RFC9-4 | DI | RFC | Anchoring rule for home geography |
| RFC9-5 | DI | RFC | Closed list of what may anchor geography |
| RFC9-6 | DI | RFC | Capability identity continuity is RFC 0001's |
| RFC9-7 | DI | RFC | Unmapped code renders Unknown |
| RFC9-8 | DI | RFC | Portfolio level derived, not authoritative |
| RFC9-8(a) | DI | RFC | Portfolio inherits the machinery its obligations need |
| RFC9-9 | DI | RFC | One home geography; stability contract |
| RFC9-9(a) | DI | RFC | Three-line residual-adjacency legend; the judged part is named in RFC9-47 (CR) |
| RFC9-9(b) | DI | RFC | honored/not-honored as registered channel |
| RFC9-10 | DI | RFC | Analytical plane explicit selection; marker |
| RFC9-11 | DI | RFC | Mode boundary (masquerade) contract |
| RFC9-12 | DI | RFC | Lens switch never moves entities |
| RFC9-13 | DI + OS | RFC; routed limb per rationale | Personal state never truth-bearing; concrete state kinds → `spec/map-surface` |
| RFC9-13(a) | DI | RFC | Layout-version stamping of coordinate-bearing state |
| RFC9-14 | DI | RFC | Two-tier layout contract |
| RFC9-14(a) | DI | RFC | The three layout inputs, defined |
| RFC9-15 | DI | RFC | Append-stability |
| RFC9-15(b) | DI | RFC | Fixed-within-version; full manual regeneration |
| RFC9-16 | DI | RFC | Closed relocation-trigger set |
| RFC9-16(d) | DI | RFC | Owner-gated version adoption; narrow carve-out |
| RFC9-17 | DI | RFC | Forbidden churn list |
| RFC9-18 | DI | RFC | Layout version registry governed (RFC3-16(a) consumer) |
| RFC9-19 | DI | RFC | Multi-mapping rendering; no double-counting |
| RFC9-20 | DI | RFC | Placement is governance, never renderer choice |
| RFC9-21 | DI | RFC | Identity-based counting |
| RFC9-22 | DI | RFC | Repository as overlay |
| RFC9-23 | DI | RFC | Authority/trust boundaries as overlay |
| RFC9-24 | DI + OS | RFC; routed limb per rationale | Reserved epistemic palette; concrete texture/color values → `spec/map-surface` |
| RFC9-25 | DI | RFC | Reserved channels |
| RFC9-26 | DI | RFC | Channel declaration contract; fail-closed legend |
| RFC9-27 | DI | RFC | Unknown never invisible; earned emptiness |
| RFC9-28 | DI | RFC | Height single-meaning per lens |
| RFC9-29 | DI | RFC | Text is a channel; secret exclusion |
| RFC9-30 | DI | RFC | Inferred treatment |
| RFC9-31 | DI | RFC | Lens as explicit binding |
| RFC9-32 | OS | `spec/map-lenses` | V0 lens set and staging — product scoping; the two-field work-state consumption invariant inside it stays DI |
| RFC9-33 | OS | `spec/map-lenses` | Post-V0 lens staging is OS. Retained DI: Risk requires a **policy-declared composite** (an undeclared risk heatmap is a VIS-7 violation); Runtime is **hard-gated by SEC-3** through RFC 0005 execution profiles; unmeasured flow renders explicitly unmeasured |
| RFC9-34 | DI | RFC | No synthesized completeness |
| RFC9-35 | DI | RFC | Lens addition is a contract act |
| RFC9-36 | OS | `spec/map-scenes` | Scene-profile staging (City required, Factory later); the one-graph invariant stays DI |
| RFC9-37 | DI | RFC | Factory honesty obligations bound now |
| RFC9-38 | DI | RFC | Evaluation named on-surface; motion rules |
| RFC9-39 | DI | RFC | Base and approved-intent scenes; marked-vacancy floor |
| RFC9-40 | DI | RFC | Proposed-scene fidelity |
| RFC9-41 | DI + OS | RFC; routed limb per rationale | Historical scope binding sentence is DI; the **candidate interaction bundle** (ghost steps, milestone scenes, scrubber) is OS → `spec/map-scenes`, only after its own owner approval |
| RFC9-42 | DI | RFC | LOD epistemic invariance |
| RFC9-43 | DI | RFC | Aggregate disclosure |
| RFC9-44 | DI | RFC | Unmapped district never disappears |
| RFC9-45 | CR | Release policy | Comprehension walkthrough gate — execution record (`records/`), judgment (`decisions/`), authority from the adopted release policy; the grey-map diagnosis sentence stays DI |
| RFC9-46 | DI | RFC | Non-3D co-equality and equivalence tuple |
| RFC9-47 | CR | Release policy / craft | The release-check obligation registry |
| RFC9-47(a) | CR | Release policy / craft | Part 2 (the per-release completeness check) is CR. Retained DI: part 1's **same-logical-change invariant** binds RFC amendment acts — authority a craft checklist does not have |
| RFC9-48 | DI | RFC | Non-visual parity |
| RFC9-49 | CR | Craft (performance policy) | Declared responsiveness budgets; the honest-narrowing invariant stays DI |
| RFC9-50 | DI | RFC | No ambient motion at V0 |
| RFC9-51 | DI | RFC | Illumination as interaction state |
| RFC9-52 | DI | RFC | Binding phase rule: no implementation of observable behavior scheduled from this RFC alone; coverage matrix required at surface specification (rev8 item 7) |

## §7 boundary sections — non-deferring obligations

§5/§6 prose is IR by definition; **§7 boundary routings are IR except where
a §7 entry states an obligation does not defer**. Two such obligations
exist, and both are DESIGN-INVARIANT despite living outside a numbered
clause:

- **RFC 0008 §7 (board-layout ladder):** any board or queue laid out as an
  ordered column sequence must place the terminal (`closed-unmerged`) and
  absence values **off the ladder**, never at its end — the one rule
  standing between RFC8-12's partition and RFC8-2(b)'s anti-thesis board.
- **RFC 0007 §7 (link-integrity cadence):** the verification cadence routes
  to quality policy, but the obligation and its trust-floor consequence
  bind in the RFC.

## The binding phase rule this matrix operates under

Added at the rev8 rework (directive item 7) and extended at rev10, six
contracts now carry an identically-shaped clause — **RFC6-28, RFC7-38,
RFC8-32, RFC9-52, RFC10-16, RFC11-12** —
binding that **no implementation work for user-observable behavior may be
scheduled solely from that RFC**: every observable consequence must first
map to an approved OpenSpec requirement/scenario or carry an explicit,
reviewed N/A judgment, and the surface-specification phase must deliver a
**clause-to-requirement coverage matrix** per RFC. (RFC6-28 was added on
the rev8 final review's finding that RFC 0006 — selection, URLs, the nine
resolution outcomes, the drawer, endpoint parity — sat outside the rule
while being the most directly user-observable cross-surface contract.)
Consequence for this file: the DI/OS classification here is a **routing
aid only** — a DI or CR class never exempts a clause's observable
consequences from OpenSpec coverage. The coverage matrices required by those clauses
are a later, surface-specification deliverable; this file is their input,
not their substitute. **This matrix routes RFC 0007–0009 and RFC-0010/0011; RFC 0006's
clause-level routing (including its `spec/selection-api` material) is a
surface-specification deliverable under RFC6-28's coverage matrix, not
re-enumerated here.**

**Stated judgment on RFC 0001–0005 (recorded so the boundary is a
decision, not an omission):** those five RFCs fix kernel, workspace,
observation, and authority semantics whose user-observable consequences
are rendered exclusively *through* the RFC 0006–0009 contracts, which
carry the phase rule — e.g. RFC2-24/2-25's Unknown-reason renderings reach
users only via surface clauses (RFC8-21, RFC9-29, RFC6-14) that are
covered. One residue is named rather than hidden: RFC 0005's ceremony,
login, and consent *experiences* are user-observable and not themselves a
surface RFC; any implementation of them is surface work and falls under
the same OpenSpec-coverage obligation via the surface RFC that renders
them. (Narrowed at rev10: RFC10-16 now places CLI commands, API endpoints
and their answers, and agent-protocol tooling under the phase rule, and
RFC10-3 binds machine-client admission to RFC5-5/5-6 — the genuine
remainder is human login and consent-ceremony UX.) If a later phase finds an RFC 0001–0005 consequence reaching users
without passing through a rule-carrying contract, that is a gap to route,
not a licence to schedule.


## RFC 0010 — Mission Control and autonomy envelopes (new at rev10)

| Clause | Class | Routes to | Rationale |
|---|---|---|---|
| RFC10-1 | DI | RFC | Operator domain, not a truth surface; no second source of truth |
| RFC10-2 | DI | RFC | One canonical service + semantic API; clients-only topology (technology open) |
| RFC10-3 | DI | RFC | RFC5-3 class exhaustiveness applied; mission-affecting scopes distinct |
| RFC10-4 | DI + OS | RFC; creation/approval surface → spec/mission-control | Retained DI: pinned inputs are **immutable for the mission's life** — a pinned-input change never silently retargets a running mission; it raises an escalation whose choices include re-approval. Mission identity fields → concrete creation/approval requirements and scenarios |
| RFC10-5 | DI + OS | RFC; lifecycle freeze → spec/mission-control | Retained DI: every terminal state recorded with its reason; `expired`/`cancelled` always reachable by human act; **no state transition widens the envelope**. Candidate lifecycle; freeze happens BY the OpenSpec review vs RFC 0008 states (§8 q1) |
| RFC10-6 | DI | RFC | Mission-is-not-work; evidence-gated completion; no gate bypass |
| RFC10-7 | DI + OS | RFC; envelope editing → spec/mission-control | Envelope minimum content + narrow-reading default are invariants; the editing/authoring surface is OS |
| RFC10-8 | DI | RFC | No self-widening — load-bearing safety invariant |
| RFC10-9 | DI | RFC | Envelope is RFC3-16(a) artifact under the 16(c) two-state model |
| RFC10-10 | DI | RFC | Two enforcement planes; preventive choke point; recorded guardrail decisions |
| RFC10-11 | DI | RFC | Bound exhaustion never self-extends |
| RFC10-12 | DI + OS | RFC; queue rendering → spec/mission-control | Retained DI: expiry defaults are safe — expiry may narrow, pause, or block and **may never widen an envelope or approve anything** (§4 violation case 4 rests on this). Attention Item packet fields → rendering/resolution requirements |
| RFC10-13 | DI + OS | RFC; queue behavior → spec/mission-control | Compression + never-silently-disappear are invariants; queue UX is OS |
| RFC10-14 | DI | RFC | Governed mission home under RFC 0003 discipline |
| RFC10-15 | DI | RFC | Portfolio/project authority split; store never authoritative for project truth (home/schema deferred, §8 q3) |
| RFC10-16 | DI | RFC (phase rule) | Schedules nothing; coverage matrix at surface specification |

## RFC 0011 — Context Compiler and governed context packets (new at rev10)

| Clause | Class | Routes to | Rationale |
|---|---|---|---|
| RFC11-1 | DI + OS | RFC; packet inspection → spec/context-packets | Identity/immutability invariant; the packet-viewing surface is OS |
| RFC11-2 | DI | RFC | Packet digest in every execution record; versioned amendment |
| RFC11-3 | DI | RFC | Packet required for governed runs; "read everything" unlawful |
| RFC11-4 | DI | RFC | Deterministic mandatory selection; versioned rule set |
| RFC11-5 | DI | RFC | Inference suggests, never suppresses |
| RFC11-6 | DI | RFC | Incomplete-is-Unknown; blocks when policy requires complete |
| RFC11-7 | DI | RFC | No second truth store; rebuildable projections |
| RFC11-8 | DI | RFC | Chat is not canonical memory; explicit promotion acts |
| RFC11-9 | DI | RFC | Retention/privacy boundaries; egress-consent gate unbypassed |
| RFC11-10 | DI + OS | RFC; profile registry → spec/mission-control | Profile floor + never-widens invariant; registry surface is OS (§8 q2) |
| RFC11-11 | DI | RFC | Budget posture: disclosed exceptions, never silent trimming (figure is policy, §8 q1) |
| RFC11-12 | DI | RFC (phase rule) | Schedules nothing; coverage matrix at surface specification |

## Clause-to-future-spec coverage skeleton (directive §10)

To be filled at surface specification — one row per OS/DI+OS clause, per
domain; a clause with no requirement row at spec time needs a reviewed
N/A judgment. Skeleton (counts per domain):

| Future spec domain | Sourcing clauses (from this matrix) |
|---|---|
| spec/intent-surface | RFC7-22 (OS) + the routed limbs of RFC7-5/10/13/16/17/34 (DI + OS) |
| spec/work-surface | RFC8-20 (OS) + the routed limb of RFC8-14 (DI + OS) |
| spec/map-surface, spec/map-scenes, spec/map-lenses | RFC9-32/33/36 (OS) + the routed limbs of RFC9-13, RFC9-24 (map-surface) and RFC9-41 (map-scenes, its bundle D1-gated) |
| spec/selection-api | RFC 0006 clause routing — deliverable of RFC6-28's coverage matrix |
| spec/mission-control | RFC10-4(part), RFC10-5(part), RFC10-7(part), RFC10-12(part), RFC10-13(part), RFC11-10(part) |
| spec/context-packets | RFC11-1(part) |

Binding rule (restated from the six phase-rule clauses): **no
user-observable Polaris, Trajectory, Orrery, Mission Control, CLI, API,
or context-packet behavior may be scheduled for implementation solely
from RFC prose** — every observable consequence maps to an approved
OpenSpec requirement and scenario, or carries a reviewed N/A judgment.
The OpenSpec changesets themselves are NOT authored in this phase.

## Tallies

Machine-recounted at rev10 review (per-RFC, row classes as they stand
in this file):

| Contract | DI | DI + OS | OS | CR | rows |
|---|---|---|---|---|---|
| RFC 0007 | 28 | 6 | 1 | 4 | 39 |
| RFC 0008 | 30 | 1 | 1 | 0 | 32 |
| RFC 0009 | 50 | 3 | 3 | 4 | 60 |
| RFC 0010 | 11 | 5 | 0 | 0 | 16 |
| RFC 0011 | 10 | 2 | 0 | 0 | 12 |

Carried rev9 rows kept their substance; ten carried DI rows whose
rationale already routed a limb were relabelled `DI + OS` at the rev10
review (RFC7-5/10/13/16/17/34, RFC8-14, RFC9-13/24/41 — no
classification substance changed), and RFC10-4/5/12 gained their retained
DI limbs in the rationale column. As at rev9: no clause was found to be
pure INFORMATIVE-RATIONALE. Phase-rule clauses: six. No clause of any
contract is scheduled for implementation by this matrix.
