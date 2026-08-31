---
id: RFC-0006
title: Cross-Surface Selection, Query and Evidence Drawer
status_source: owner-act-record
clauses: "RFC6-1..RFC6-28 (no gaps; none retired, merged, or renumbered)"
implementation_boundary:
  kind: requires-openspec
  clause: RFC6-28
governs: [selection-reference, url-identity, resolution-outcome, evidence-drawer, query-answer, label-parity, scenario-context]
applies_to: [all-surfaces, kernel, machine-clients]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004]
tags: [selection, urls, queries, drawer, machine-endpoints, equivalence, scenario, consent, secrets]
---

# RFC 0006 — Cross-Surface Selection, Query and Evidence Drawer

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — either owner-adopted (bootstrap,
uncorrelated) or Syzygy-verified, with the exact provenance state always
visible (RFC3-16). Absent such a record, this
contract binds nothing.

**Date:** 2026-07-30 (amended through 2026-08-02; compacted at rev10)
**Serves:** VIS-1, VIS-2, VIS-3, VIS-7 (trust floor: link rule, legend
fidelity); SEC-2, SEC-5; SDR-2, SDR-17, SDR-25, SDR-27; resolves SDR §5
question 9 (selection/URL/query semantics; the single evidence drawer).
Refines the research selection contract SC-1…SC-9, superseded where this RFC
differs.

Rationale, amendment history, and rejected alternatives:
`../history/RFC-0006-history.md` (non-normative).

---

## 0. Reader map (non-normative)

*If this map and a clause ever disagree, the clause wins.*

One identity space (§3.1) · nine typed resolution outcomes, nothing fails
silently (§3.2) · rename-proof URLs, two temporalities (§3.3) · machine
answers carry the same facts and labels humans see (§3.4) · one evidence
drawer per selection (§3.5) · rendering equivalence (§3.6) · explicit scenario
context — base, proposed, historical (§3.7) · consent and secrets render as
policy states, never as absence (§3.8) · this contract schedules no
implementation work (§3.9).

Then: §4 violation cases · §5 integration · §6 alternatives (in history) ·
§7 deferrals · §8 open questions. Contract range RFC6-1…RFC6-28, no gaps.

---

## 1. Scope

The contract that makes "one kernel, three surfaces" observable from outside:
how anything in the project graph is **selected**; how a selection is **pinned
in a URL** that survives renames and outlives retirement; how
**machine-queryable endpoints** (V0-mandatory) answer with exactly the fact
set and epistemic labels the UI renders; and what the **single
evidence/provenance drawer** contains. **Semantics only**: no wire format, no
query language, no layout, no URL spelling.

---

## 2. Motivation and doctrine grounding

Doctrine rules that surfaces are projections over one shared kernel, never
independently authoritative [Observed: architecture.md, "One kernel, three
surfaces"]; that agents consume **the same observed truth the owner sees**
through machine-queryable endpoints [Observed: v1.md, V0 ships; vision.md, two
first-class consumers]; and that the trust floor requires every rendered
internal project-entity link to resolve to its identified target [Observed:
trust-and-evidence.md, floor bullet 2]. Owner rulings: non-3D views co-equal
and semantically/query equivalent (SDR-27), status display minimal by default
(SDR-17), claim/gap identity two-level with selection anchored on the durable
level (SDR-2).

[Inferred] The failure mode prevented is **divergent truth by projection**:
three surfaces each honestly rendering the kernel yet disagreeing — different
evidence for one selection, a machine answer omitting an Unknown a human would
have seen, a bookmark silently landing on a different entity after a refactor.
Individually small, collectively fatal to the observatory's reason to exist
[Observed: trust-and-evidence.md, floor preamble].

---

## 3. The contract

Clauses are numbered `RFC6-n` for stable citation. Amend in place; retire
rather than renumber.

### 3.1 Selection references and the one identity space

**RFC6-1 — One selection identity space.** *(refines SC-1)* A **selection
reference** is the tuple **(entity kind, durable entity identity)**, optionally
qualified by an **evaluation identity** and a **scenario context** (§3.7).
Entity kinds and identities are exactly RFC 0001's (RFC1-5, RFC1-9/10): the
kernel mints nothing new for selection, and **no surface-local handle — file
path, node index, work-item row, layout coordinate, scene object id — is ever
a selection identity**. Surfaces may keep private handles for rendering; every
handle must resolve to a selection reference before it crosses a surface
boundary, a URL, or an endpoint.

**RFC6-2 — Everything selectable, one way.** Every V0-core entity (RFC1-5),
and every entity of an extension profile loaded **for the project** (RFC1-7 —
the mission profile's Mission and Attention Item included, on the staging
RFC1-7 states for that profile), is selectable by reference. **Entities loaded
at the workspace level rather than for a project are outside this clause and
are deferred with the portfolio profile** (SDR-29/30; §7): RFC6-8 pins a
selection inside a project identity and has no workspace-identity limb, so
declaring such an entity selectable here would make it selectable with no URL
form, against RFC6-12's openable-in-any-surface rule and VIS-7's link rule.
Selection targets the **durable identity level**
(SDR-2): selecting a claim or gap selects its durable identity; the evaluation
qualifier picks which instance answers.

**RFC6-3 — Cross-surface synchronization.** One selection reference resolves
**identically in all three surfaces**: same entity, same evaluation, same
scenario context, same drawer fact set (§3.5). A surface that can only answer
at a different evaluation (stale adapter, partial refresh) must render the
skew explicitly — naming both evaluation identities — never silently mix
evaluations *(SC-5, adopted as binding)*.

**RFC6-4 — Evaluation defaulting is stamped, never silent.** A selection
without an evaluation qualifier resolves at the **latest identified evaluation
available at resolution time**, and the answer names that evaluation. There is
no such thing as an unstamped answer: "current" is always somebody's
evaluation identity (RFC2-3), so the same unqualified selection may honestly
answer differently tomorrow — always naming which evaluation answered — and
status never changes without a new identified evaluation (RFC2-4).

### 3.2 Total resolution and typed outcomes

**RFC6-5 — Total resolution.** *(refines SC-2)* Every selectable reference
resolves to exactly one outcome from the **closed outcome set** below, in
every surface and every endpoint. Silence, an empty panel, a dropped
selection, a bare 404, or an unexplained error page are all violations — this
is VIS-2 applied to navigation: absence of a projection is never rendered as
absence of the thing.

| Outcome | Meaning | Obligations |
|---|---|---|
| `resolved` | The reference resolves at the evaluation | Full drawer fact set available |
| `resolved-absent` | The entity's durable identity is known, but the entity is absent from the selected evaluation's snapshot (appeared later, or vanished — absence is a fact, RFC1-31) | Name the evaluations where it is present; never render as error |
| `retired` | The durable identity is retired, with or without successors (RFC1-11) | Render the retirement record and `succeeds` edges; offer successors; **never auto-redirect** (§3.3) |
| `unknown` | The reference resolves but the governing claims render Unknown | Carry **each governing claim instance's primary RFC2-24 reason with its resolution route**, and any secondary annotations beside it (RFC2-24: one primary per claim instance, secondaries drawn from the same twelve) — never collapsed to a single reference-level reason, since an entity may have several governing claims Unknown for different causes |
| `not-applicable` | The entity has no projection on this surface | Legitimate **per surface only**, never for the kernel, a URL, or an endpoint; must still offer the drawer and name the surfaces where the entity does project — never a dead end |
| `excluded` | Content excluded by secret-detection policy (SEC-5) | Rendered as *excluded* with count, never as absent (§3.8) |
| `unconsented` | Resolution requires an unconsented source or provider (SEC-2/SEC-4) | Renders Unknown (`unconsented-source-or-provider`), visibly policy (§3.8) |
| `unresolvable` | The kernel cannot resolve the reference at all — a dangling identity, a broken external-authority anchor (RFC1-15) | A **typed failure naming what failed to resolve**; a trust-floor incident for kernel-emitted links (VIS-7; RFC1-26), an honest degrade for externally-minted references |
| `incompatible-scenario` | The scenario context names proposals the kernel may not union (§3.7) | Name the exclusivity-group conflict; render *N candidate futures*, never a merged fiction |

**The nine values are disjoint by precedence, fail-closed.** A reference
regularly satisfies more than one row's condition — a reference that resolves
whose governing claim is Unknown, a retired identity whose retirement record
sits behind an unconsented source, an absent entity inside an excluded scope,
an unresolvable reference named in an incompatible scenario. The outcome is the
**first** of the following whose condition holds, and no other: **1**
`excluded` · **2** `unconsented` · **3** `incompatible-scenario` · **4**
`unresolvable` · **5** `retired` · **6** `resolved-absent` · **7** `unknown` ·
**8** `resolved`. Policy states rank above identity states, which rank above
claim state — the fail-closed direction, so a policy condition is never masked
by an answer about the thing. `not-applicable` is deliberately **not in the
ordering**: it is legitimate per surface only, and it never displaces the
kernel outcome — a surface with no projection for the entity renders
`not-applicable` *in place of its own projection*, while the kernel outcome
above, and the drawer fact set, stand unchanged and are what RFC6-7's
determinism binds. Without this ordering RFC6-7's determinism would be asserted
over a value domain in which two conforming surfaces could lawfully answer
differently for one (reference, evaluation identity, scenario context) — a
disagreement RFC6-23 makes release-blocking. [Inferred — the ordering; Observed
— the fail-closed direction from SEC-5's unclassifiable rule and RFC6-26/27.]

**RFC6-6 — Outcomes are not Unknown reasons.** `not-applicable`, `retired`,
`resolved-absent`, and `unresolvable` are **navigation outcomes**, not claim
statuses: they must not be stamped with, or counted among, RFC2-24 Unknown
reasons, and an aggregate of Unknowns never absorbs them. [Inferred —
conflating them would corrupt the diagnosis-routing property RFC2-24 exists
for.]

**RFC6-7 — Resolution is deterministic per evaluation.** For one (reference,
evaluation identity, scenario context), the outcome and fact set are part of
the deterministic layer: identical across runs and across surfaces (VIS-7).
Only display formatting is excluded.

### 3.3 Stable URLs

**RFC6-8 — What a URL pins.** A Syzygy URL pins, at most: **(project
identity, selection reference [entity kind + durable identity], optional
evaluation identity, optional scenario context)**, plus optional
**presentation hints** (preferred surface, view state). The first four are
identity-bearing; presentation hints **never affect resolution** — stripping
them yields the same entity, evaluation, and fact set. URL *spelling* (path
shape, parameter names, encoding) is deliberately unbound: any spelling that
pins exactly these semantics conforms. [Inferred — semantics-only per this
phase's scope.]

**RFC6-9 — Rename-stability.** URLs embed durable identifiers, never labels,
paths, or coordinates (RFC1-10: identifiers are opaque; names are labels).
Renaming a capability, moving a file, or re-laying-out the map changes **no
URL**. A URL that would break on rename has embedded a surface-local handle
and violates RFC6-1.

**RFC6-10 — Two URL temporalities.** An **evaluation-pinned URL** (evaluation
identity present) is permanently stable: it resolves against the immutable
observation record (VIS-6 exception (b)) and renders with staleness visible
once superseded — it never silently shows newer state. An **unpinned URL**
resolves per RFC6-4: latest evaluation, stamped. Sharing an unpinned URL
shares a *question*; sharing a pinned URL shares an *answer*. Both are
legitimate; the rendering must make which-one-this-is visible.

**RFC6-11 — Retired and merged identities.** A URL pinning a retired identity
resolves to outcome `retired`: the retirement record, its `succeeds` edges,
and its successors (RFC1-11) — **never a 404, and never a silent redirect to
a successor**, because a merge or split is a governance event the reader must
see, not an equivalence the kernel may assume *(SC-8, now discharged by
RFC1-11's mechanism)*. Following a successor is a reader act. Evaluation-
pinned URLs to the retired identity keep resolving forever against their
observation records.

**RFC6-12 — URLs are surface-independent.** Every URL-pinned selection is
openable in any surface (subject to `not-applicable` per RFC6-5). A URL naming
a preferred surface still pins the same reference; the same URL body with a
different surface hint is the **same selection**, and bookmarks made in one
surface are honored by all.

### 3.4 Query semantics and label parity

**RFC6-13 — One truth, two consumers.** Machine-queryable endpoints
(V0-mandatory [Observed: v1.md]) answer from **the same kernel-computed fact
set** the surfaces render — the drawer fact set for selections (§3.5), the
same graph, claims, and labels for queries. No endpoint-only facts, no
UI-only facts: anything a surface renders is queryable, and anything queryable
is renderable. This is SDR-27's semantic/query equivalence stated as a
bidirectional obligation.

**RFC6-14 — Label parity.** Every entity and claim instance in a
machine answer carries its epistemic state **verbatim from the RFC 0002
vocabulary**: the label (Observed / Inferred / Unknown), the rendering tier
(RFC2-25), the Unknown reason where applicable (RFC2-24), and the freshness
state (RFC2-10). **Secondary Unknown annotations travel with the primary**,
verbatim and marked as secondary (RFC2-24 opens them and closes their
vocabulary to the same twelve); an answer carrying the primary alone has
dropped part of the claim instance's epistemic state. **An aggregate carries
no epistemic state of its own** — no aggregate-level label, tier, Unknown
reason, or freshness state — and carries instead its members' composition per
RFC6-17: RFC 0002 defines those four for claim instances, not for sets, and a
headline label over mixed membership is VIS-1's named violation ("rendering
that region green because its neighbors are green") whether or not an honest
composition is disclosed beside it. **A machine answer never omits epistemic
state**: an answer
listing entities without their labels, or a count that folds Unknowns into a
total silently, is a violation — an agent must be exactly as unable to mistake
Unknown for success as the owner is (VIS-2). Sibling surface states
(*dismissed by decision*, *unadopted draft*, *editorial draft* — the three
RFC2-25 places deliberately outside the registry) travel with the same
fidelity, and so does `challenge-pending` (RFC2-13) — the named disclosure a
claim carries while a submitted, not-yet-admitted challenge stands against it.
It is neither a tier nor an Unknown reason and never displaces the four values
above; it travels **beside** them.

**RFC6-15 — Every answer is evaluation-stamped.** Every query answer names the
evaluation identity (source snapshot + as-of instant) it was computed at.
**Same evaluation + same filters ⇒ same answer** in the deterministic layer
(VIS-7; RFC6-7). An answer that cannot name its evaluation is not an answer;
mixed-evaluation answers must declare the skew per RFC6-3.

**RFC6-16 — Filters are declared scope.** The filters applied to an answer are
part of the answer's envelope: an answer names what was filtered and never
presents a filtered or partial result as full scope — the VIS-1 permitted move
is narrowing the *declared* scope, never faking coverage (RFC2-23,
partial-snapshot rule, applied to queries).

**RFC6-17 — Aggregation discloses.** *(SDR-25, SDR-27, RFC2-24 rendering rule,
unified)* Any aggregate — in a scene, a table, or a machine answer — discloses
its membership count and epistemic composition and supports expansion to its
members. **The disclosed composition is the full RFC6-22 equivalence tuple**:
per-label, per-tier, per-Unknown-reason and per-freshness-state counts, **the
sibling surface states**, the `challenge-pending` disclosure (RFC2-13), and —
where the aggregate's members carry them — per-value counts of the **chain
state** and the **normalized work state** of RFC6-19 class 8, so an aggregate
can never satisfy this clause in full while disclosing nothing about
reconciliation. **Per-Unknown-reason counts are computed over primary reasons
only** — one claim instance contributes exactly one — with secondary
annotations (RFC2-24) disclosed separately and never folded into the primary
counts; otherwise two conforming surfaces could produce different Unknown-reason
totals over one declared scope while both satisfying this clause, which RFC6-23
would then class as a release-blocking disagreement. The tier counts cover
**all six** of RFC2-25's
tiers (`gate-backed`, `report-fact`, `asserted-by-worker`, `reduced-fidelity`,
`declared-only`, `suspended`), not a subset, and the sibling surface states are
the three RFC2-25 places deliberately outside the registry (*dismissed
by decision*, *unadopted draft*, *editorial draft*, per RFC6-14) — never label
and Unknown reason alone. The aggregation obligation is exactly as wide as the
equivalence obligation over the same objects: labels may not be dropped at the
moment elements merge. "Observed ×30" is honest only when the reader can also
see that all 30 are `reduced-fidelity` and 12 are stale; "Inferred ×8" only
when it discloses that all eight are `asserted-by-worker` — the one tier whose
parent label is Inferred — with no retained artifact.

### 3.5 The single evidence drawer

**RFC6-18 — One drawer, one fact set.** *(SC-4, adopted as binding)* For one
(selection reference, evaluation identity, scenario context) the kernel
computes **one fact set**, consumed by every surface and by the endpoints.
Surfaces may differ in presentation — ordering, grouping, progressive
disclosure, SDR-17's minimal-by-default status display — they may **not**
differ in which facts, labels, or provenance exist: the full fact set is
reachable from every surface, and two surfaces showing different evidence for
one selection at one evaluation is a **kernel defect, not a UI
inconsistency**. The public-facing name of this fact set is **"Why this
answer?"** — several of its classes are authority, policy, and work, not
evidence, so "evidence drawer" names the container's dominant class, never
its extent; both names denote the one fact set and neither adds or subtracts
a fact. The human and machine paths receive the same facts (RFC6-13).

**RFC6-19 — Drawer content classes.** The fact set contains, per selection:

1. **Identity** — entity kind, durable identity, current label(s), lifecycle
   state (including *unadopted draft* and *retired with successors*),
   succession edges where present, and the **state plane** each rendered
   fact belongs to (desired, proposed, observed, inferred, execution,
   historical — RFC1-22's assignment).
2. **Epistemic state** — label + tier + Unknown reason (verbatim RFC 0002
   vocabulary) and freshness state, for the entity's governing claims at this
   evaluation; open-challenge suspension renders with the deterministic basis
   visible (RFC2-14).
3. **Evidence** — every supporting evidence artifact, each a **resolvable
   link** carrying source, capture time, scope, and integrity identity;
   evidence–revision binding visible (an artifact naming a different revision
   renders stale, RFC2-11).
4. **Provenance** — the producing evaluation (snapshot + as-of instant), the
   typed authority that answered each question **with the governing
   normative revision** (the revision or digest identity of the doctrine
   rule, contract clause, requirement, or policy the answer rests on), and
   observer/adapter identities and versions.
5. **Warrant** — the decisions, requirements, and policies that motivate or
   govern the selection; dismissals rendered *dismissed by decision* with
   reason and expiry, never green (RFC1-20).
6. **Challenge and contradiction state** — **every open challenge against the
   selection's claims, each with its RFC2-13 lifecycle state**, with inference
   provenance; contradictions pending adjudication. `submitted` challenges
   belong to the fact set exactly as `admitted` ones do — RFC2-13 requires a
   `submitted` challenge to render visibly on the affected claim as
   `challenge-pending`, and a fact a surface renders that the fact set lacks is
   the kernel defect RFC6-18 names. The lifecycle state travels, never
   flattened: `admitted` suspends the claim (Unknown, `challenge-suspended`,
   `suspended` tier); `challenge-pending` suspends nothing and leaves the
   deterministic status standing.
7. **Policy visibility** — exclusions (with counts), the **coverage
   boundary**, and consent state (§3.8). The coverage boundary is the union
   of two defined constructs, never a free-standing judgment about what the
   evaluation "could observe": the producing evaluation's executed **mapping
   coverage records** (RFC4-27 — which pass ran, over which declared scope
   with exclusions counted, with which observer/adapter versions, and what it
   found; deterministic facts inside the observation record, RFC2-6) and, where
   the snapshot was partial, its **explicitly declared captured scope**
   (RFC2-23, partial-snapshot rule).
8. **Work and reconciliation state** — where work bears on the selection,
   **two fields, never folded into one and never rendered as proof of
   satisfaction** (work is never proof): (i) the relevant items' **chain
   state**, defined at RFC2-18 (`merged`, `reconciliation-pending`,
   `reconciled@E`, `unsatisfied`, `contradiction-raised`, `Unknown(reason)`)
   and read at this evaluation under RFC2-19's V0 staging — this is the
   selection's reconciliation state, and an uncomputed reconciliation renders
   Unknown, never green; and (ii) the items' **normalized work state**
   (RFC8-12 — a forward reference, informative until RFC 0008 is accepted:
   until then the field is not required, its absence renders as absence, and
   nothing may be substituted for it). Trajectory's rendering of the chain
   state is RFC8-28, likewise informative until RFC 0008 is accepted; the
   definition this class binds is RFC2-18's.

**RFC6-20 — Drawer links obey the floor.** Every internal link in the fact set
resolves to its identified target; the kernel does not emit a reference it
cannot resolve (RFC1-26). Citations of doctrine rules and accepted contracts —
which are not V0-core graph entities (RFC1-6) — are rendered by their stable
identifiers (`VIS-n`, RFC clause numbers); if a surface renders such a citation
*as a link*, that link must resolve to the identified artifact. External URLs
are classified external and may be unavailable without falsifying the internal
graph *(SC-7)*.

**RFC6-21 — Minimal display never subtracts facts.** SDR-17's
minimal-by-default status display is a presentation depth, not a fact-set
subset: what is hidden at rest must be the same fact set when disclosed, on
every surface, and endpoints always serve the full set. [Inferred — otherwise
"minimal" becomes a fourth epistemic state.]

### 3.6 Rendering equivalence (SDR-27)

**RFC6-22 — The equivalence definition.** Two renderings (3D scene, 2D view,
table, machine answer) are **equivalent** iff they present: the same evaluation
identity, the same declared filters, the same underlying graph (entities and
edges), the same epistemic states (label + tier + reason + freshness), the
same sibling surface states (dismissed-by-decision, unadopted-draft,
editorial-draft — RFC6-14), the same **`challenge-pending` disclosure**
(RFC2-13), and the same **chain state** and **normalized work state** where
those are carried (RFC6-19 class 8), and the same scenario context (RFC6-24)
for every presented element. Equivalence is over *semantics and query results*,
never over pixels. The last two additions are what make the closure arguments
of RFC2-13 and RFC8-12 true: each justifies naming its values in the contract
by this clause checking them for parity, and a facet outside this tuple is
checked by nothing.

**RFC6-23 — Finer detail is allowed; contradiction is not.** A non-3D
rendering may expose **finer detail** than an aggregated 3D scene (SDR-27) —
that is a filter/aggregation difference and must be disclosed as one
(RFC6-16/17). What no pair of equivalent renderings may do is disagree: on an
entity's existence, an edge, a label, a tier, a reason, a freshness state, a
sibling surface state, a `challenge-pending` disclosure, a chain state, a
normalized work state, a scenario context, or a count over the same declared
scope. Any such disagreement is a kernel or projection defect,
release-blocking under the trust floor.

### 3.7 Scenario context: base, proposed, historical

**RFC6-24 — Scenario context is explicit and singular.** Every selection
carries exactly one scenario context; absent an explicit one, the context is
**base**. The contexts:

- **Base** — the base graph at the selected evaluation, with no proposal
  overlay and no superseded-evaluation selection. The default; nothing extra
  to declare. **A base context over a non-default revision** (a branch or PR
  tree evaluation) **is still Base at that evaluation, but every surface must
  carry an explicit non-default marker naming the revision** — never render as
  if it were the default branch. Base is distinct from the *layout baseline*
  (RFC9-14), which is a layout input, never a scenario. *(Renamed from
  `Current` at the rev7 rework, semantics unchanged — see history.)*
- **Proposed** — (base evaluation, selected proposal set). The set must be
  mutually compatible: the kernel **refuses** to resolve a context naming two
  proposals in one exclusivity group, or proposals of undeclared
  compatibility, returning `incompatible-scenario` and rendering *N candidate
  futures* selectable one at a time (RFC1-27). Proposed structure remains
  visually and queryably distinct from observed structure everywhere it
  appears — drawer, scene, table, and endpoint alike [Observed:
  trust-and-evidence.md, rendering rule] — and has no status authority: a
  proposed context never turns anything green, closes a gap, or anchors the
  map.
- **Historical** — a superseded evaluation, resolved against its immutable
  observation record, staleness visible on the primary surface [Observed:
  trust-and-evidence.md, Staleness]. Drawer and query access to historical
  evaluations rests on VIS-6 exception (b) and needs no doctrine change. **Map
  rendering of historical state** rests on adopted doctrine: owner amendment
  **D1** (ratified 2026-08-01) makes historical state part of `map/`'s
  constitutional scope unconditionally. The *concrete historical interaction
  design* is a separate deferred candidate-design bundle (RFC9-41; §7); nothing
  in this clause depends on it.

**RFC6-25 — Context travels with the selection.** Cross-surface
synchronization (RFC6-3), URLs (RFC6-8), and query answers all carry the
scenario context. A surface may never silently swap context — rendering a
proposed structure in response to a base-context selection, or vice versa, is
a violation even when the fact sets overlap.

### 3.8 Consent, secrets, and policy visibility

**RFC6-26 — Unconsented renders as policy, never as error.** *(refines SC-9)*
Where resolution or the inferred portion of a fact set requires an unconsented
source or provider, that portion renders **Unknown with reason
`unconsented-source-or-provider`** (RFC2-24 #6), presented as what it is — a
standing policy state with its resolution route (record consent) — never as a
failure, a broken link, or an empty region. The consented remainder of the
fact set renders normally; consent state is itself a drawer fact (RFC6-19
class 7).

**RFC6-27 — Excluded is a rendered state.** Content excluded by the
secret-detection policy renders as *excluded* with a count, never as absent
(SEC-5; unclassifiable fails closed). Nothing derived from excluded content
appears in any surface, drawer, or endpoint — a secret in a query answer is a
trust-floor violation, identical in gravity to one in a tooltip.

### 3.9 Authority boundary at the OpenSpec seam (binding phase rule)

**RFC6-28 — This contract schedules nothing.** This RFC fixes the semantics of
selection, URLs, resolution outcomes, the evidence drawer, and the machine
query plane; it is **not a specification of record from which implementation
work may be scheduled**. No implementation work for **user-observable behavior
under this contract** — selection and URL behavior, the nine typed resolution
outcomes, retirement rendering, drawer content, endpoint answers and their
label parity — may be scheduled solely from this RFC: before implementation,
every observable consequence of **every clause of this contract other than
this one** must either **map to an approved OpenSpec requirement or scenario**
in the governance root's `openspec/**` plane, or carry an **explicit, reviewed
N/A judgment** recording why that consequence needs no requirement. **The
reviewed N/A judgment's home and gate.** A reviewed N/A judgment is a recorded
owner judgment homed in `decisions/` (RFC3-15), and the judgment is honored only
through an effective owner act under RFC3-16(a), in state (1) or state (2),
with that state rendered; absent or invalid acts map nothing and leave the
consequence unmapped and Unknown, never covered (RFC3-16(a)'s effect rule;
VIS-2).

**Rows are per observable consequence, not per clause.** A clause with five
observable consequences and one mapped requirement is not covered; the matrix
discloses the consequences it enumerates for each clause, so a
complete-looking matrix over under-enumerated consequences is a defect of the
matrix. The
surface-specification phase
must produce, as a deliverable, a **clause-to-requirement coverage matrix**
for this RFC — every clause mapped to requirement identities or to its
reviewed N/A — and that matrix is review material, never authority. This
clause creates no OpenSpec content now (none may exist during bootstrap); it
binds the phase boundary so RFC prose is never quietly treated as an
implementable behavioral spec.

---

## 4. Violation cases

Each is recognizable, not rhetorical:

1. *(RFC6-1/9)* A URL or endpoint parameter carries a file path, scene node
   id, or work-item row as the selection key; renaming a capability breaks its
   bookmarks.
2. *(RFC6-3/25)* Selecting a capability in Orrery opens a different
   evaluation's facts in Trajectory with no skew rendered; a proposed-context
   deep link renders as current structure.
3. *(RFC6-5)* Selecting an unmapped entity yields an empty panel; a retired
   capability's URL returns 404.
4. *(RFC6-11)* A bookmark to a merged capability silently lands on the larger
   successor.
5. *(RFC6-14)* An endpoint returns entities without labels, or a count where
   Unknowns are silently included in — or dropped from — a green total.
6. *(RFC6-15/16)* Two identical queries at one evaluation differ; a filtered
   answer presented as full project scope.
7. *(RFC6-18/21)* Polaris's drawer shows an evidence artifact Trajectory's
   omits for the same selection and evaluation; an endpoint serves only the
   "minimal" display subset.
8. *(RFC6-23)* The 3D scene and the table disagree on a freshness state or a
   count over one declared scope.
9. *(RFC6-24)* Two proposals in one exclusivity group rendered as one merged
   future.
10. *(RFC6-26/27)* An unconsented repository rendered as an error page; an
    excluded secret's shape leaking through per-file match counts.

---

## 5. Integration

**Relies on RFC 0001:** entity vocabulary and identity scheme (RFC1-5/9/10) as
the selection space; succession/retirement (RFC1-11/12) behind RFC6-11;
two-level claim identity (RFC1-18) behind RFC6-2; exclusivity groups (RFC1-27)
behind RFC6-24; no-unresolvable-emission (RFC1-26) behind RFC6-20.

**Relies on RFC 0002:** evaluation identity (RFC2-3) behind RFC6-4/10/15; the
label + tier + reason + freshness vocabulary (RFC2-10/24/25) rendered verbatim
per RFC6-14/19; challenge lifecycle (RFC2-13) and suspension visibility
(RFC2-14); the aggregation rule (RFC2-24 rendering rule). The dangling-anchor
case (RFC1-15 degrade) maps to outcome `unresolvable`; its claim-status
counterpart is RFC2-24 reason **#11 `reference-unresolvable`**, **retained by
owner decision A5** — the defect this RFC recorded against RFC 0002 is thereby
answered (history: §8 q3).

**Relies on RFC 0003:** RFC3-16's owner-act record, which establishes this
contract's own effective status (Status, above), and RFC3-16(a)'s predicate
behind RFC6-28's reviewed N/A judgment; RFC3-15's `decisions/` category as that
judgment's home.

**Relies on RFC 0004:** RFC4-27's executed mapping coverage record, the defined
construct behind RFC6-19 class 7's coverage boundary (with RFC2-6, which makes
coverage records deterministic facts of the observation record).

**Forward references are informative.** Where a clause of this RFC cites a
sibling *draft* by clause number — RFC8-12 and RFC8-28 in RFC6-19 class 8,
RFC9-14 in RFC6-24, RFC9-41 in RFC6-24 and §7 — the citation is **informative
until that RFC is accepted**: it names where an obligation will be discharged
or how another surface renders a facet this contract defines, never a
dependency of this contract's meaning, and a renumbering in a sibling draft
changes nothing here. Load-bearing are citations to **adopted doctrine**, to
the **SDR**, and to RFC 0001, RFC 0002, RFC 0003 and RFC 0004 as enumerated
above. Where such a forward citation appears inside a normative enumeration —
RFC6-19 class 8's normalized-work-state limb — that limb states its condition
in its own text rather than relying on this paragraph, so a reader at
acceptance is never left deciding whether an obligation is inert or binding but
unsatisfiable.

**Provides to RFC 0005:** the resolution and query semantics its
authentication contract wraps — client class never changes an answer's fact
set or labels, only whether the client is admitted (SEC-1).

**Provides to RFCs 0007–0009:** the selection reference, outcome set, drawer
fact set, and equivalence definition each surface contract must honor. SC-3's
per-surface projection duties (what Polaris/Trajectory/Orrery must each
*reveal* for a selection) are deliberately not bound here; this RFC binds only
the shared row (the drawer).

**Not this RFC's:** endpoint wire formats, query language, pagination, URL
spelling, auth (RFC 0005), drawer layout and interaction, per-surface duties,
certificate rendering (post-V1).

---

## 6. Alternatives considered

Moved to `../history/RFC-0006-history.md` §6. Three remain load-bearing for
reading live clauses: silent redirect from retired identities to successors
was rejected as asserting an unadopted equivalence (RFC6-11); a
`not-applicable` Unknown reason was rejected because navigation outcomes
stamped as Unknown reasons corrupt Unknown counts (RFC6-6); label-bearing
URLs were rejected because slugs break on rename or demand a second identity
store (RFC6-9).

---

## 7. Deliberately deferred

- Endpoint wire format, query language/filter grammar, pagination, and URL
  spelling → post-acceptance spec/RFC material (stack-adjacent; none may
  weaken the semantics here).
- Machine-client authentication and client classes → RFC 0005 (SEC-1).
- Per-surface projection duties for a selection (SC-3's table) → RFCs
  0007–0009.
- Drawer presentation, disclosure ordering, and SDR-17's reader-controlled
  detail mechanism → surface contracts and craft.
- Saved-selection collections, cross-project selection, and workspace-level
  URLs → portfolio profile (SDR-29/30).
- Historical-map mechanics (renderable evaluations, retention) → RFC 0009.
  Constitutional scope is settled (doctrine amendment D1, adopted); the
  concrete interaction design remains a non-binding candidate-design bundle
  under RFC9-41 pending owner approval.
- Certificate rendering in the drawer → post-V1 certificate RFC.

---

## 8. Open questions for acceptance

1. **Unpinned-URL default (RFC6-4/10).** Alternative to latest-evaluation
   resolution: a chooser when the latest evaluation differs from the last one
   the reader saw. Proposed: latest-with-stamp; the chooser is presentation
   and can come later. Confirm?
2. **`not-applicable` scope (RFC6-5).** Is a surface ever permitted this
   outcome for a V0-core entity, or must every surface render at least the
   drawer inline (making `not-applicable` purely a layout decision)? Proposed:
   permitted, with the never-a-dead-end obligation.
3. *(Answered at acceptance — owner decision A5; question and answer in
   history.)*
4. **Successor convenience (RFC6-11).** Never-auto-redirect is proposed as
   absolute. Should a *reader-enabled* preference ("follow sole successors
   automatically, with a rendered notice") be permitted as personal
   presentation state (VIS-6 exception (a)), given it never alters the fact
   set — or is even opt-in auto-follow too close to silent relocation?

---

*End of RFC 0006. Clauses RFC6-1 … RFC6-28 — complete range, no gaps, none
retired or merged.*
