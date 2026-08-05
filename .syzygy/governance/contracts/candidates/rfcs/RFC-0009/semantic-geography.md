---
id: RFC-0009
title: Orrery (Map Surface) — semantic geography, anchoring, and layout determinism
status_source: owner-act-record
module: semantic-geography
clauses: RFC9-1..RFC9-23 (sub-clauses RFC9-8(a), RFC9-9(a), RFC9-9(b), RFC9-13(a), RFC9-14(a), RFC9-15(b), RFC9-16(d); no gaps, no retirements)
governs: [map-surface-identity, home-geography, analytical-plane, anchoring, layout-version, layout-baseline, append-stability, relocation-trigger, placement, shared-component, identity-counting, repository-overlay, authority-overlay]
applies_to: [orrery, machine-clients]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006]
tags: [surface, spatial, determinism, sdr-21, sdr-22, sdr-23, vis-7, sec-2, sec-3, sec-5]
---

# RFC 0009 — Orrery (Map Surface): semantic geography, anchoring, and layout determinism

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — as an owner-adopted bootstrap act until the
independent A1 correlation mechanism exists, and as a Syzygy-verified effective
act only after correlation (RFC3-16). Absent such a record, this contract binds
nothing.

**Package:** module 1 of 3. Index and lookup rule: `README.md`. Rationale,
amendment history, alternatives, answered §8 questions:
`../../history/RFC-0009-history.md`.

**Serves:** VIS-1, VIS-2, VIS-3, VIS-7; SEC-2, SEC-3, SEC-5; architecture.md
(constitutional spatial requirement); v1.md; SDR-3, SDR-21, SDR-22, SDR-23,
SDR-29, SDR-30. Package-level `Serves`: `README.md`.

---

## 0. Module scope and reader map (non-normative)

*If this section and a clause disagree, the clause wins.*

This module owns **where things are and why they are there**: surface identity
and the semantics-only boundary; what may and may never anchor position; the one
home geography versus explicitly selected analytical planes; the layout input
tuple and the determinism, append-stability and relocation obligations built on
it; shared-component placement and identity counting; repository and authority
overlays. Read it to answer: *may this thing move? what does nearness mean? who
may re-lay the map? where does a shared or undeclared component live? what does
this count?* For colour, height, edges, lenses, scenes and aggregates, read
`visual-grammar-and-lenses.md` (RFC9-24..RFC9-45); for equivalence, release
gates, performance, motion and the OpenSpec boundary,
`interaction-parity-and-release.md` (RFC9-46..RFC9-52).

---

## 1. Surface identity and scope

**RFC9-1.** `map/` is the semantic/spatial representation of observed, intended,
proposed, **and historical** system state [Observed: architecture.md, as amended
by adopted owner amendment D1]. Historical scope is constitutional and
unconditional; what remains deferred is the concrete historical interaction
design (RFC9-41), which is candidate design, not contract. Orrery is a working UI
codename; technical names in schemas and APIs stay literal [Observed:
architecture.md, Vocabulary]. The map is a projection over the one shared kernel
— never independently authoritative; its vocabulary (labels, tiers, Unknown
reasons, freshness) is RFC 0002's, rendered verbatim (RFC2-24/25), and its
selection, drawer, and query semantics are RFC 0006's, not re-defined here.

**RFC9-2.** This contract binds semantics and determinism obligations only.
Rendering technology, layout algorithms, and their tuning are post-acceptance
material; no conforming choice may weaken a clause here.

**RFC9-3.** Everything the map shows must be explainable from identified
artifacts: for any selected element, the exact channel readings currently applied
and the metric behind each must be reachable at the point of selection.
**Encoding provenance is a surface-local "explain this encoding" affordance
layered over the shared drawer — never a member of the shared drawer fact set**,
because RFC6-18 fixes one fact set per (selection reference, evaluation identity,
scenario context) with no lens dimension (RFC6-7), and admitting lens channel
bindings would make a deterministic cross-surface fact set vary with personal
presentation state (VIS-6, exception (a); RFC3-21). The affordance is nonetheless
evidence-derived, not surface-invented: the channel registry it reads is a
governed artifact under `.syzygy/map/**` (RFC9-26, RFC9-18) and the underlying
metric values are drawer facts. A scene element whose encoding cannot be traced
to an identified artifact must not render that encoding. [Inferred — rejected
kernel-route alternative: history file §6.]

---

## 2. Semantic geography and anchoring

**RFC9-4.** **The anchoring rule.** Position in home geography is bound to
declared identity; measurement never moves a building. The spatial hierarchy,
coarse per v1.md: project → **capability district** (the anchor level,
RFC1-13/14) → **component block** (declared topology entry) → **plot/building**
(code element placed by a declared implementation mapping, SDR-4/RFC1-16 class
(i)). Interior detail below source/test evidence renders as evidence listings,
not modelled geometry — V0 owes no symbol-level layout contract. [Inferred —
hierarchy composition; anchor level Observed per architecture.md and RFC1-13.]

**RFC9-5.** **What may anchor geography:** adopted capability identities; adopted
topology entries and their declared placements; declared implementation mappings
— including `declared-only` tier mappings (RFC2-25): the *declaration* is the
Observed fact that assigns the address, while the unverified satisfaction claim
renders Unknown on the epistemic channels. **What may never anchor geography:**
drafted/unadopted declarations (they render in the proposed treatment with an
"unadopted" plate, outside the stable address space [Observed: v1.md; RFC1-14]);
inferred mappings (inference may **annotate** geography — hatched, with
provenance — never anchor it [Observed: trust-and-evidence.md]); file paths (a
path is an attribute, never an identity; path-derived arrangement is confined to
the unmapped district, RFC9-44); metrics of any kind; proposals (RFC1-22,
proposed *state* plane); personal presentation state (VIS-6, exception (a)).

**RFC9-6.** Capability identity continuity is RFC 0001's: rename changes a label
and no coordinate (RFC1-10); split/merge mints successors with `succeeds` edges,
rendered as an explicit identity event with both old and new identities visible —
never a silent relocation (RFC1-11); retirement ghosts the district and is a
rendered event. A selection or URL pinned to a retired district resolves per
RFC6-11 — never a 404, never an auto-redirect.

**RFC9-7.** Code that maps to no declared capability renders Unknown — never
silently inferred into a capability [Observed: v1.md] — and lives in the unmapped
district (RFC9-44), never in a plausible-looking neighborhood.

**RFC9-8.** The portfolio level is a **derived arrangement, not an entity**:
projects placed deterministically by project identity; grouping and ordering are
workspace-manifest concerns (SDR-29, RFC 0003); cross-project relations render
only where declared, otherwise unconfirmed/asymmetric (SDR-30) — and inferred
cross-project relations never anchor placement. Those declared relations are
**portfolio-profile relations** (`depends-on`, `subproject-of`,
`contains-project`; RFC1-7, RFC3-14, RFC3-31), not kernel relations, and they
legend as themselves under RFC9-9's profile-relation rule — declared, with their
profile and semantic class named, and never rendered or counted as RFC1-25's
observed `depends_on`. A derived hierarchy view (RFC3-31, SDR-28) is a rendering
over those declarations and never a plane fact. **Portfolio arrangement is
append-stable on RFC9-15's terms:** onboarding a project must not perturb the
placement of projects already arranged — determinism alone would permit a lawful
reshuffle of the whole portfolio on every onboarding, and the spatial-memory
premise applies at portfolio scale exactly as inside a project.

**RFC9-8(a) — The portfolio carries the machinery its obligation requires.** The
portfolio is not a project — SDR-29 and RFC3-21 put its arrangement in the
**workspace manifest**, not in any project's `.syzygy/map/**` — so it carries the
**same machinery at workspace scope**: a **portfolio layout version** and its
registry, reorganisation events with recorded rationale, and the RFC9-16(d) owner
gate, all held in the workspace manifest's governed space (RFC3-21), since no
project owns the arrangement of its peers. RFC9-15(b) applies unchanged at this
scope: fixed within a version, full regeneration only, order-independent; and
RFC9-13(a)'s stamp-and-refuse rule covers portfolio-scope saved cameras. Without
this machinery, append-stability inherited from RFC9-15 leaves **no lawful way
ever to re-lay the portfolio**.

Two limits, so the symmetry is not over-read: the portfolio has **no
declared-relatedness reading of proximity** (RFC9-9 reading 2 is
capability-scoped), so there is no portfolio backlog to partition; and the
arrangement remains a **derived arrangement, not an entity** — versioning how it
is laid out does not make it a plane fact. [Inferred]

---

## 3. Home geography and analytical planes (SDR-21)

**RFC9-9.** Every project has **exactly one home geography**: stable,
capability-anchored, reproducible (§4), append-stable, built for spatial memory.
In home geography **position and proximity never encode a measurement**. The
legend rule is *not* "proximity is inert": RFC9-4 builds project → district →
block → plot, so intra-district adjacency **is** declared capability membership
expressed positionally, and a generated legend line reading "proximity: inert"
would be false under VIS-7's exactly-true requirement.

**Proximity carries exactly two declared readings, and no third** *(owner
decision B12(a), reversing the drafted "proximity is inert beyond containment"
position; read with **RFC9-9(a)**, which adds a third **legend line** — residual
adjacency, carries no meaning — without adding a third reading)*:

1. **Declared containment** (RFC9-4) — intra-district adjacency is capability
   membership expressed positionally.
2. **Declared relatedness** — a `declared-dependency` edge (RFC1-25, minted by
   owner decision A6) *may* be expressed positionally, so that capabilities
   declared to depend on one another tend to sit near one another.

**Proximity never encodes a measurement**, and no undeclared *signal* may be an
input to placement: adjacency-by-observed-coupling, adjacency-by-authorship or
-ownership, and clustering on any measured or lens-bound quantity are barred,
because a reader cannot tell which basis produced a given nearness. The two
readings are the only ones proximity *carries*; they are not the only thing that
*produces* nearness, and RFC9-9(a) governs the remainder.

**Reading 2 is best-effort, and its shortfall is rendered, never hidden.**
Append-stability (RFC9-15) forbids relocating an existing district, so a newly
declared relatedness edge frequently cannot be satisfied without moving
something. When it cannot, the layout does not move anything and does not
pretend: each `declared-dependency` edge carries a rendered **honored /
not-honored** state on the map, and the count of not-honored declarations is a
first-class surfaced quantity (RFC9-15(b)). A not-honored edge is a true fact
about the current layout, not a defect and not an Unknown — the relation itself
is fully known; only its positional expression is unsatisfied, and the edge still
renders on its own explicit edge channel regardless.

[Inferred] The two readings are ordered: where containment and relatedness
compete for the same position, **containment wins**, because containment is
structural and total (every plot has exactly one district) while relatedness is
optional and partial. A layout that broke containment to honor relatedness would
falsify RFC9-4.

**RFC9-9(a) — Residual adjacency: the legend has three lines, not two.**
RFC9-16(a) **mandates** appending new entities into free space, so on a mature
map most nearness is neither containment nor honored relatedness but the residue
of the placement function, and a two-line legend would be **false about most of
the adjacency actually on the screen** — the exact failure VIS-7's
legend-fidelity floor exists to prevent. The residue is **not** adjacency-by
arrival order (insertion order is never an input to any coordinate) but
adjacency-by **baseline-delta**: "declared since the last full regeneration",
computed from (declaration set, layout baseline) without reference to order
within that set. The residue is therefore **declared**, in four binding parts:

1. **Three legend lines.** The position/proximity registry entry declares exactly
   three readings: *declared containment*; *declared relatedness, best-effort*;
   and **residual adjacency — carries no meaning**. All three are generated from
   the registry under RFC9-26. The third is a reading, not a footnote, and
   omitting it is an unlegended channel meaning.
2. **The residue must be reader-decidable, not merely disclaimed.** A nearness
   carries meaning only if it is **intra-district** — visible, because district
   boundary is a rendered reserved channel (RFC9-25) — or **accompanied by a
   rendered `declared-dependency` edge in honored state** — visible, because that
   edge renders on its own explicit channel with its state (RFC9-9(b)). Every
   other nearness is residual by construction. A reader can therefore decide
   which of the three readings applies to any given pair **from what is on the
   screen**, without access to the placement algorithm.
3. **The residue must not counterfeit the meaningful readings.** Free-space
   placement must not produce apparent grouping that mimics declared containment:
   no enclosure, shared boundary treatment, common plinth or ground plane, or
   visual clustering for entities related only by baseline-delta. The district
   boundary channel is reserved (RFC9-25) and residual placement may not
   approximate it — otherwise part 2 stops being answerable by eye and part 1's
   third line becomes unfalsifiable.
4. **The bar on undeclared signals stands, narrowed to *inputs*.** The test is on
   what the placement function reads, not on whether its output happens to look
   clustered. RFC9-14's input tuple is closed and names no observed, authored, or
   measured quantity, which is the enforcement point: a placement function
   reading observed coupling violates RFC9-14 before it violates this clause.
   Baseline-delta is admissible only because it is derivable from that closed
   tuple and because part 1 declares what it produces.

[Inferred — part 2's reader-decidability requirement is load-bearing. An
amendment keeping the third legend line while dropping part 2 or 3 has kept the
disclaimer and lost the property it disclaims.]

**RFC9-9(b) — The honored / not-honored state is a channel, and is registered as
one.** The positional-expression state of a `declared-dependency` edge is a
rendered distinction, so RFC9-26 binds it in full and it carries a registry entry
like any other channel:

- **Source metric / domain** — a closed three-value categorical domain:
  `honored` (endpoints positionally near under the current layout),
  `not-honored` (they are not), `unknown` (the layout cannot determine it).
  Nearness here is the layout's own declared adjacency predicate, which the
  registry entry names; it is not a measured distance and does not vary by lens
  (RFC9-25: position is lens-invariant).
- **Update cadence and freshness** — a function of the layout input tuple
  (RFC9-14), so it changes only on a relocation trigger (RFC9-16) or a
  declaration change, and it inherits the base layout's freshness carrier.
- **Epistemic class** — **[Observed]** with respect to the layout: computed from
  identified artifacts (the declaration set and the recorded base layout, RFC2-6)
  and re-derivable. It is emphatically *not* an epistemic class of the
  **relation** — the relation is fully known, and a `not-honored` edge is a true
  fact about the layout, never an Unknown capability and never a defect.
- **Evidence path** — resolvable to the governing declaration that minted the
  edge **and** to the layout version and baseline under which the state was
  computed (RFC9-18 registry entry). A state shown without its layout version is
  unresolvable, because the same edge is lawfully `honored` under one version and
  `not-honored` under the next.
- **Unknown value** — required by RFC9-27 and non-hypothetical: an edge with an
  endpoint that has no home placement (unmapped district, RFC9-44) has no
  adjacency to evaluate. It renders the reserved Unknown treatment with reason
  `missing-declaration` (RFC2-24 #1) where the placement declaration is absent,
  and it is **not** counted in either partition of the RFC9-15(b) part 4 backlog
  — an Unknown is not a not-honored edge, and folding it into the
  refresh-clearable count would put a number in front of the owner that a refresh
  cannot move.
- **Fail-closed** — with no registry entry the state does not render, and the
  edge renders without it. RFC9-26's rule admits no exception here.

[Inferred — the Unknown limb and the backlog exclusion are what a naive
implementation gets wrong: both RFC9-15(b) part 4 partitions presuppose two
placed endpoints.]

Dependency edges render on their own explicit, resolvable edge channel,
**legended by the relation that actually exists** — the kernel relation from
RFC1-25's closed vocabulary, or, where an adopted extension profile *adds* a
relation rather than the kernel closing one, that **profile relation named as
itself**. Three classes of intra-project dependency edge exist, and **no edge of
one class is ever evidence of another** (RFC1-25(b)'s twelve-pair invariant,
mechanically checkable, binding this surface as much as the query endpoints):

- **Observed** — `depends_on` code→code, `structurally_related`. Adapter- and
  snapshot-backed.
- **Execution-class** — `depends_on` work→work. Scheduler-authoritative.
- **Declared** — `declared-dependency` between capabilities, or between topology
  entries (RFC1-25, **minted at acceptance by owner decision A6**).
  Desired/declared, owner-adopted through a governance artifact.

No edge may be legended "declared" unless a declared relation backs it —
legending an observed edge as a declaration is exactly the conflation SDR-3
forbids. An *undeclared* dependency is never inferred from an observed one:
absence of a `declared-dependency` edge renders Unknown (`missing-declaration`),
never "no dependency".

**The declared channel is also the positional one.** RFC9-9 reading 2 expresses
`declared-dependency` — and only `declared-dependency` — through proximity.
Observed and execution-class edges render on the edge channel alone and never
influence position, because doing so would be the adjacency-by-observed-coupling
that reading 2's bound explicitly bars.

**Profile relations legend as themselves (RFC1-26, second limb).** RFC1-26
permits an adopted profile to add relations without re-typing the closed set, and
the portfolio profile does exactly that: `depends-on`, `subproject-of` and
`contains-project` are Project→Project relations of **Desired (declared)**
semantic class and owner-adopted authority (RFC1-7; RFC3-14; RFC3-31) — and since
RFC 0003 §7 leaves the cross-project type vocabulary deliberately open, this is a
standing shape, not one relation. An edge carrying a profile relation renders on
the same explicit channel, and its legend names (i) the relation's own declared
name, (ii) the profile that adds it, and (iii) its semantic class and authority.
It is never coerced into the nearest kernel relation, and never left unlegended
because RFC1-25's table does not name it. The channel registry is the enforcement
point: a profile relation with **no registry entry does not render**, under
RFC9-26's fail-closed rule — and, on RFC9-35's pattern, a profile relation that
is to render arrives with its registry entry, legend, Unknown behavior and
tabular equivalent in the same increment, never as an edge drawn first and
declared later.

**RFC1-25's anti-conflation rule binds here as a rendering rule.** A declared
project-scope edge is **never rendered, legended, filtered, counted, or
query-answered as** RFC1-25's observed `depends_on`, and neither is evidence of
the other; the two may not share a mark, a channel treatment, a legend entry, or
a count. The relation names themselves carry no separation — the owner
deliberately kept the one-character `depends_on`/`depends-on` collision at
acceptance (**B20**/RFC3-14) — so this surface is where RFC1-25(b)'s twelve-pair
invariant must hold at the place a reader actually sees it. One-sided or mutually
incompatible declarations render **unconfirmed/asymmetric**, never as a resolved
mutual dependency and never silently reconciled (RFC9-8; SDR-30; RFC1-7;
RFC3-14; RFC3-31).

[Inferred — the operational form of SDR-21's "home" regime. **§8 q7 is closed**
(owner decision B12(a)), not open.]

[**A maintenance note, not a ruling.** The profile-relation rule is written
**generally**, not for `depends-on` alone, because RFC 0003 §7 leaves the
cross-project relation vocabulary open by design. What this surface does **not**
decide is *who may add a profile relation, and under what gate* — that belongs to
**RFC1-7 and RFC1-26**, and it is safe here under either answer: an unregistered
profile relation fails closed and does not render. See §10's open follow-on.]

**RFC9-10.** An **analytical plane** is an explicitly selected alternate
projection in which position and/or proximity encode a **declared metric or
relation** (dependency-distance, component/architecture, churn-clustering). Every
analytical plane must: (a) declare its position and proximity semantics as
first-class legend entries; (b) carry a persistent, non-dismissible marker that
it is not home; (c) be **visibly temporary, with return to home geography always
available and discoverable** — the reader is never stranded outside home, and the
*interaction cost* of returning is not bound here (**the owner granted this
relaxation at acceptance, decision B21**, over the drafted position that SDR-21's
"one action" is ratified text a contract clause may not narrow by prose; SDR-21's
bound is relaxed by the ratifier, the only party who may relax it, and the
recorded cost is that a release check could have counted actions and can no
longer, on the surface whose whole contract is checkability — CC-VIZ-5 is amended
to match); (d) name the evaluation it projects. Analytical-plane layouts are
deterministic per (analytical-plane definition, evaluation) but carry **no
append-stability or cross-evaluation coordinate promise**, and must say so.
[Observed: SDR-21; obligations (a)–(d) Inferred as its contract form.]

**RFC9-11.** **The mode boundary is a contract: an analytical layout may never
masquerade as home.** The surface's default scene is home geography; entering an
analytical plane is an explicit, labelled act; no analytical plane may suppress
its marker; spatial-memory affordances (saved camera homes, "you are here"
continuity) attach to home only. A view that binds position to a metric without
the analytical-plane marker is a violation identical in class to an unlegended
channel (VIS-7). [Inferred]

**RFC9-12.** Lens switching within home geography re-skins and never moves
anything: same camera, same selection, same geography, visible legend swap. Any
view change that moves entities is by definition an analytical-plane or scenario
switch and is labelled as one. [Inferred, from RFC9-4 + SDR-21]

**RFC9-13.** Personal presentation state — camera, filters, bookmarks, saved
lens/analytical-plane selections — lives in `.syzygy/local/` and never affects
truth-bearing encodings (VIS-6, exception (a); RFC3-21). A filter that hides
entities shows a persistent count of what it hid.

**RFC9-13(a) — Coordinate-bearing personal state is stamped with the layout
version, and never restores silently across one.** A saved camera home is stored
**coordinates**, and a layout version change (RFC9-16(d)) moves every declared
entity — so the saved home comes to point not at a dangling reference, which
would be visible, but at a *different district*, which is not. RFC 0006's
protections do not reach it: RFC6-1, RFC6-9 and RFC6-11 govern identity-bearing
**selection references**, and camera state is not one. Three obligations:

1. **Stamp.** Every coordinate-bearing item of personal state (saved camera
   homes, "you are here" continuity anchors, position-anchored bookmarks) records
   the layout version and baseline it was saved under.
2. **Anchor where an anchor exists.** Where the save was made against a selected
   entity, it records that **identity** alongside the coordinates and restores by
   re-resolving the identity under the current layout — the RFC6-9 treatment
   applied to the one artifact left out of it.
3. **Never land silently on a mismatch.** With no identity anchor and a version
   mismatch, the surface **does not restore the raw coordinates silently**. It
   marks the saved home **stale-layout**, names the version it was saved under
   and the current one, offers the reorganisation event's before/after
   (RFC9-16(d)), and restores raw coordinates only on an explicit act that says
   what is being done.

[Inferred — obligation 3 is load-bearing; 1 and 2 without it merely record enough
to know the restore was wrong. The failure is RFC9-45's exact release signature,
reached through a lawful, announced, owner-gated act with nothing marked wrong.]

---

## 4. Layout determinism and stability

**RFC9-14.** **Two-tier layout contract.** The **declared-identity base layout**
is a deterministic function of the **layout input tuple** —

> **(declaration set, layout baseline, layout version)**

— and nothing else; it is part of the deterministic observation record and inside
the VIS-7 identity test [Observed: architecture.md — determinism is asserted over
the observed graph *and base layout*; layout versions are snapshot inputs, RFC2-1
item 7].

**RFC9-14(a) — The three inputs, defined.**

- **Declaration set** — the closed set of declared facts the layout may read: the
  deterministic observed graph's declared identity set; declared topology entries
  and their `placed_in` edges (RFC1-25); and **adopted `declared-dependency`
  edges** (RFC1-25), named explicitly because a formulation omitting edges leaves
  an implementer unable to honor RFC9-9 reading 2 at all. Unadopted declarations
  are not members (RFC1-22: proposed never anchors).
- **Layout baseline** — the declaration set **as it stood at the most recent full
  regeneration** (RFC9-15(b) part 2). It is a governed, identified artifact under
  `.syzygy/map/**` (RFC9-18), written by the regeneration act, immutable
  thereafter, and a **snapshot input** (RFC2-1 item 7, alongside layout version).
  It is what makes append-stability expressible: the layout holds fixed whatever
  the baseline placed, and appends fill free space around it.
- **Layout version** — the placement algorithm's governed version (RFC9-18).

**The baseline is a real input and is recorded as one**, and recording it is what
discharges RFC9-47's determinism gate: without it two implementations handed only
(declaration set, layout version) can lawfully disagree on every coordinate and on
the RFC9-15(b) backlog count — a release-blocking disagreement under RFC6-22/23,
and a recorded base layout (RFC2-6) that no longer reproduces. [Inferred]

The **path-derived arrangement** — the interior of the unmapped district — is
deterministic given the snapshot's declared working-tree state but is explicitly
excluded from the cross-snapshot stability guarantee and says so on its face.

**RFC9-15.** **Append-stability.** Adding one capability, component, building, or
— at portfolio scale (RFC9-8) — one project must not perturb the coordinates or
placement of any existing declared entity. Determinism alone does not give
stability: a reproducible layout that reshuffles on every addition destroys the
spatial memory that justifies the 3D mandate. Append-stability is a
release-gated, fixture-tested property (RFC9-47), not a trusted one. [Inferred —
obligation; mechanism deliberately unspecified.]

**RFC9-16.** **The closed relocation-trigger set.** A declared entity's home
coordinates change only on: (a) capability/topology creation or retirement
(append to free space; ghost then remove); (b) split/merge — rendered as an
identity event per RFC9-6; (c) a declared placement change — announced with its
governing decision or declaration link; (d) a **layout version change** —
announced as a reorganisation event naming the old and new layout versions, with
before/after reachable, **and carrying a recorded rationale naming what the new
layout buys and what it moves** (recorded with the reorganisation event under
`.syzygy/map/**`, RFC9-18). A version change with no recorded rationale is not a
lawful trigger. Every trigger is a rendered event; none is a silent teleport. The
reorganisation event is also what coordinate-bearing personal state resolves
against when found stale (RFC9-13(a)); announcing the move to the *scene* is not
by itself announcing it to the reader's saved views.

**RFC9-16(d) is owner-gated, with one narrow carve-out** *(owner decision A3,
narrowed by the same owner after review 8).* A layout version change is an **owner
governance act** carrying the recorded rationale above — **except** where the two
versions are demonstrated to be the **same placement function**, in which case a
recorded note suffices.

**"Same placement function" means agreement on every input, not on one.** The
demonstration must establish that for **all** layout input tuples (RFC9-14) the
two versions compute identical coordinates. In practice this covers versions
whose placement path is unchanged — refactors, renames, dependency bumps, changes
confined to rendering rather than placement — and **little else**. A version that
changes placement behaviour for any input, however rare, does not qualify however
many inputs it agrees on. *(Agreement on declaration set D says nothing about
D ∪ {X}; the failure case that fixes the narrow reading is in history, RFC9-16(d).)*

**The demonstration is not an RFC2-3 identity test, and this clause does not cite
it as one.** RFC2-3's test is explicitly *intra*-evaluation — "two runs of
**one** identified evaluation" — and layout version is a snapshot input (RFC2-1
item 7), so two layout versions are two evaluations. What is required is a
distinct **layout-equivalence check**: a harness that exercises both versions over
a declared input space and compares coordinates, whose result is recorded with
the note. An *asserted* equivalence is not a carve-out — it is an ungated
relocation — and absent the recorded check the governance act is required.

**RFC9-15(b) — Fixed locations, manually refreshed.** *(Owner-proposed model at
acceptance, superseding the layout tiebreak decision B12(a) would otherwise have
required.)* Home coordinates are **fixed within a layout version and regenerated
only by owner act between versions.** Four binding parts:

1. **Within a version, nothing moves.** Incremental declarations append into free
   space (RFC9-16(a)) and never relocate an existing entity. Declared relatedness
   (RFC9-9 reading 2) that cannot be honored without moving something is simply
   not honored, and renders as such.
2. **Regeneration is full, never partial.** An owner-run refresh repositions
   **every** district from the current declaration set. Scoped regeneration —
   refreshing "core" zones while others hold — is **barred**: it would make
   coordinates a function of refresh history, and it breaks spatial memory
   unevenly, which is worse than breaking it wholly and announcing it.
3. **Both placements are pure functions of the RFC9-14 input tuple —
   (declaration set, layout baseline, layout version) — and insertion order is
   never an input to any coordinate.** Two conforming implementations given the
   same tuple, in any order, must produce identical coordinates. Append-stability
   does not imply order-independence — hence the separate statement; without it
   the RFC2-6 recorded base layout is checkable but not reproducible.
4. **The backlog is surfaced, and split by what can actually clear it.** The
   not-honored declared-relatedness edges are rendered as a first-class quantity,
   partitioned into:
   - **refresh-clearable** — a full regeneration could honor them; and
   - **structurally unhonorable** — no layout at any version can honor them,
     because containment wins (RFC9-9) and the two endpoints sit in different
     districts whose extents cannot both contain the pair. Cross-district
     `declared-dependency` between **topology entries** is the systematic case:
     each is pinned inside its own capability district by `placed_in`, and at
     most the few pairs meeting at a shared district boundary can ever be
     adjacent.

   **The partition is mandatory, and an unpartitioned backlog count must not
   render.** An owner told "12 not honored" cannot distinguish twelve a refresh
   would fix from twelve nothing will ever fix, and would be invited to pay the
   model's maximum cost — a full reorganisation invalidating every memorized
   location — for no benefit. Only the **refresh-clearable** count is a refresh
   signal; the structural count is a standing fact about the declaration set,
   whose resolution route is a declaration or placement change, never a refresh.

   A refresh is never automatic and never triggered by declaration change; the
   trigger is an owner act under RFC9-16(d).

**Explicitly not a trigger: a district exhausting its reserved extent.** The
trigger set is closed, and growth is not on it. Reservation policy is unbounded in
principle (RFC9-17), so ordinary growth never *forces* a relocation; an
implementation choosing between displacing neighbours (forbidden by RFC9-15/17)
and bumping the layout version has a reservation defect, and the correct response
is to fix the reservation policy, not to take the (d) hatch.

[Inferred. **§8 q6 is closed** (**owner decision A3**, narrowed after review 8 to
RFC9-16(d)'s single carve-out). The gate is an **extension of VIS-4's shape-level
sign-off list made by owner decision at acceptance**, not a restatement of
existing doctrine — neither RFC3-18 nor doctrine supplied it. RFC9-16's
obligations bind independently of the gate; the gate adds who may pull the
trigger.]

**RFC9-17.** **Forbidden churn.** None of the following may change a declared
entity's home coordinates: file move/rename/reformat or any refactor that
preserves the declared mapping; any metric change in any lens; a new evaluation
over an unchanged snapshot, at any as-of instant (the base layout is inside the
identity test); lens switching, filters, camera, or personal state;
footprint/size band changes (a measured band varies only within its reserved
extent and never displaces a neighbor). Any of these causing movement is a
defect, not a preference. **Reservation policy must be unbounded in principle:** a
district's or block's reserved extent must be capable of accommodating any lawful
growth of its declared membership without displacing a neighbour, so that growth
never requires a layout-version change (RFC9-16(d)). Exhausting a reservation is
a defect in the reservation policy, never a licence to relocate. [Inferred, from
RFC9-4/14; reserved-extent device adopted from the research disposition of O-F3.]

**RFC9-18.** Layout versions are governed artifacts under `.syzygy/map/**`
(RFC3-18): version registry and reorganisation-event records are governed;
computed geometry is rebuildable projection (`cache/`, RFC3-20); camera and view
state are personal (`local/`, RFC3-21). **Registry entries fix which layout
version a scene's positions *mean*** — the reference every reorganisation event
and every stability guarantee (§4) is read against — so they are honored **only
under RFC3-16(a)**; an entry whose owner-act provenance does not verify does not
establish a version, and scenes resolving against it render Unknown rather than
silently against a version an untrusted writer declared. [Inferred] Nothing in
`map/` becomes independently authoritative over kernel semantics.

*(RFC9-18 is one of two artifacts RFC3-16(a) cites as encoding-meaning-fixing —
the **layout version registry**; the other is RFC9-26's **channel registry**.)*

---

## 5. Shared components and identity counting (SDR-22)

**RFC9-19.** A code element or component may carry declared mappings to multiple
capabilities (RFC1-17). The map must support all **three placement mechanisms**
and never force a shared component into one arbitrary capability district
[Observed: SDR-22]: (a) the **component/architecture plane** — an analytical
plane (§3) rendering the full multi-capability edge structure; (b) a
**shared-infrastructure district** in home geography, membership by declaration;
(c) **multi-capability presence**: the component stands at its declared home
placement, and every other mapped district renders a link marker that resolves to
the one entity — **never a clone**. *(Mechanism (c) is available only where a
**determinate** declared home exists; where declarations compete, RFC9-20 governs
and the entity is Unknown-placed.)* Two separately selectable copies of one
identity break identity-based counting (RFC1-17, RFC9-21) and selection identity
(RFC6-1) — which, not the trust-floor link rule, is what the no-clone rule rests
on.

**RFC9-20.** Home placement of a multi-capability component comes only from
declaration: a declared primary placement in topology, or declared
shared-infrastructure membership. Absent any declared basis, the component
renders in the shared-infrastructure district's explicitly marked
**placement-undeclared** aggregation (Unknown reason `missing-declaration`,
RFC2-24 #1, routing to the drafting affordance) — the map never mints a home by
heuristic or tie-break: an undeclared placement decided by an algorithm is a
governance answer given by a renderer.

**Over-declaration is a Contradiction, not a precedence problem.** Where a
component carries two co-unsatisfiable declared placements in one scope — a
declared primary topology placement and a declared shared-infrastructure
membership naming different homes — the map renders it **Unknown-placed** with
the conflict marker and the adjudication route surfaced (RFC2-15; RFC9-24's
Contradicted treatment), exactly as the undeclared case renders its
placement-undeclared aggregation. No precedence rule may resolve it: "primary
placement wins" is the same renderer-decides-governance error this clause exists
to prevent, and no surface may silently pick a winner [Observed:
architecture.md]. [Inferred — SDR-22 applied; deliberately diverges from the
research's minted-sticky-home rule (history file, §6).]

**The general case: two `placed_in` edges.** `placed_in` is **not functional and
carries no primacy marker** (RFC1-25(c)), so a topology entry with two adopted
`placed_in` edges has **two declared homes and no declared basis for choosing
between them**. That is the same Contradiction and takes the same treatment:
**Unknown-placed**, conflict marker, adjudication route surfaced. It is not a
case for RFC9-19(c), because (c) requires a determinate declared home and there
is none; and it is not a case for a tie-break, because every available tie-break
— lexical, adoption order, edge order, "first declared wins" — is a renderer
answering a governance question. The word "primary" above names a **declared**
primacy where a governance artifact supplies one; it never licenses a surface to
designate one. Counting follows placement, without exception: an Unknown-placed
entry counts in **neither** candidate district's composition and once in the
Unknown-placed aggregation — not in both (RFC9-21 double-counting against an
identity with no home) and not in one (the tie-break re-entering through the
count after being barred from the layout).

**RFC9-21.** **Identity-based counting, never double-counting.** Aggregates count
each identity once per query subject (RFC1-17): a shared component counts once in
each district that queries it and once at project scope. Because district totals
may therefore sum to more than the project total, the disclosure trigger is
scoped to the **scene**, not to a table: **wherever a shared contribution is
counted into more than one rendered aggregate, every rendered aggregate that
includes it discloses the shared-contribution count** ("N shared, counted once at
project scope"). A trigger written in the tabular idiom — "any view presenting
district aggregates side-by-side with a project aggregate" — would not fire here,
because a 3D scene presents every district side-by-side with every other and
rarely renders an explicit numeric project aggregate, leaving a reader to sum
three tall districts by eye. A district total that silently absorbs shared
components — or a project total computed by summing districts — is comprehensible
fiction (VIS-1).

---

## 6. Repository and authority overlays (SDR-23)

**RFC9-22.** Repository membership is an **overlay, never the primary
geography**: a capability district may contain buildings from several
repositories; repository boundaries render as a toggleable boundary treatment.
Partitioning space by repository first would re-anchor geography to a storage
fact [Observed: SDR-23; architecture.md]. A repository present but unconsented
renders as an explicit walled, Unknown-filled zone — never empty ground, which
reads as "nothing there" (RFC1-3).

**RFC9-23.** Authority and trust boundaries are a first-class overlay: governance
root as a civic marker — legended as the only place Syzygy writes **project
content directly** (VIS-5); adapter-mediated authorities (VCS metadata,
scheduler, CI, runtime) as a distinct boundary kind with the adapter and its
authorization visible; consent scopes rendered on the project's surface
[Observed: SEC-2]; execution-profile boundaries [Observed: SEC-3; RFC5-20];
secret-exclusion zones as sealed markers at a **declared minimum aggregation** —
never content, and never a per-element match count (the granularity bound is
RFC9-29) [Observed: SEC-5]. Write authority a reader cannot see is the surprise
this overlay exists to prevent.

---

## 7. Violation cases (module-owned)

Each is recognizable, not rhetorical:

1. *(RFC9-4/17)* A mapping-preserving refactor reshuffles a district; a metric
   change or lens switch moves a building.
2. *(RFC9-5/7)* An inferred mapping places a building; a drafted capability
   anchors a district; unmapped code renders inside its "probable" capability.
3. *(RFC9-11/16)* A layout clustered by **observed** coupling renders without the
   analytical-plane marker and readers memorize it as home (declared relatedness
   under RFC9-9 reading 2 is lawful in home geography; observed coupling is not,
   and the two are distinguishable only because RFC1-25(b) keeps the relations
   separate); a layout-version upgrade re-lays the map with no reorganisation
   event or no recorded rationale; a version bump claims the RFC9-16(d) carve-out
   without running the demonstration; a district that has outgrown its reserved
   extent is re-laid out under trigger (d).
3a. *(RFC9-15(b))* A newly declared relatedness edge relocates an existing
   district; a refresh regenerates some zones and not others; two implementations
   given the same declaration set in different insertion orders produce different
   coordinates; a relatedness edge the layout could not honor renders as honored,
   as an Unknown, or as nothing at all, rather than as **not-honored**; the
   not-honored backlog is not surfaced, leaving the owner no signal that a
   refresh is due.
4. *(RFC9-20/21)* A renderer tie-breaks an undeclared shared component into a
   district; a precedence rule resolves two co-unsatisfiable declared placements
   instead of rendering the Contradiction; district totals silently double-count,
   or a project total sums districts; a shared contribution is counted into
   several rendered aggregates with no disclosure on any of them.
5. *(RFC9-22)* Geography partitioned by repository; an unconsented repository
   rendered as empty ground.

*(Cases 6–10 and 11 belong to modules 2 and 3.)*

---

## 8. Integration (module-scoped)

**RFC 0001:** capability identity as the map anchor with
rename/split/merge/retirement (RFC1-10/11/13/14); mapping classes never conflated
(RFC1-16); multi-capability edges with identity-based counting (RFC1-17); state
planes — proposed never anchors (RFC1-22); `placed_in` and `declared-dependency`
(RFC1-25, minted by owner decisions **A7** and **A6**); the twelve-pair
anti-conflation invariant (RFC1-25(b)); `placed_in` non-functional (RFC1-25(c));
profile relations (RFC1-7, RFC1-26). **RFC 0002:** degradation-only time
(RFC2-4); the recorded base layout in the observation record (RFC2-6);
Contradiction treatment (RFC2-15); Unknown reasons (RFC2-24); tiers (RFC2-25).
**RFC 0003:** `map/` as a schema-versioned governed namespace (RFC3-18);
cache/local boundaries (RFC3-20/21); the RFC3-16(a) owner-act predicate;
identity-preserving migration (RFC3-23); workspace-manifest arrangement (RFC3-21,
RFC3-31). **RFC 0004:** code-element identity continuity (RFC4-12); mapping
declaration sites (RFC4-26). **RFC 0006:** selection references and cross-surface
sync (RFC6-1/2/3); outcome set incl. retired/never-redirect (RFC6-5/11); the
single drawer (RFC6-18/19).

**Discharged foundation defect, retained because it carries owner decisions.**
RFC1-25 formerly had neither a declared topology-entry→capability placement
relation nor a declared dependency relation; both were discharged at acceptance —
`placed_in` by **owner decision A7**, `declared-dependency` by **owner decision
A6**. **The drafting restraint that produced them is unchanged and still binds:**
the relations exist because the *owner* minted them, not because this RFC took
the closed vocabulary into its own hands, and an observed edge is still never
legended as declared. The omission was at *capability, topology-entry and
code-element* scope only; at **project** scope the portfolio profile's
`depends-on` (RFC1-7; RFC3-14) already existed under RFC1-26's second limb.
The three remain **distinct relations differing by one character** —
`depends_on`/`depends-on`/`declared-dependency` — kept apart here by RFC1-25(b).
RFC2-6's omission of the base layout (defect 5) is **resolved upstream** as of
2026-08-01. Full trail: history file, §5.

---

## 9. Deliberately deferred (module-scoped)

Layout algorithms and their tuning → post-acceptance spec material; none may
weaken a clause here (RFC9-2). Interaction design, including the **form and cost
of the return-to-home affordance** (RFC9-10(c) binds only that return is always
available and discoverable, per **B21**; which action it is, how many steps it
takes, and how it is placed and labelled, is not bound here) → craft-and-care.
The analytical-plane catalog beyond the component/architecture plane →
map-surface specs, each entering under RFC9-10. Modelled interiors below
source/test evidence → post-V0 elaboration, no promise made.

---

## 10. Owner questions (module-owned)

Stable package numbering; answered items keep a stub so numbers never shift.
Full text and decision cites: `../../history/RFC-0009-history.md` §8.

- **q1** — the placement relation (§5 defect 1). **Answered — owner decision A7.**
- **q5** — the declared dependency relation (§5 defect 1, second half).
  **Answered — owner decision A6.**
- **q2 — Undeclared shared-component placement (RFC9-20).** **Open.** Confirm
  the placement-undeclared aggregation over the research's minted-sticky-home
  alternative. The trade: honest-but-lumpy (the shared district grows on
  undeclared projects) versus prettier-but-renderer-decided homes. **Current
  contract position, binding unless and until the owner rules otherwise:**
  RFC9-20 as written — the map never mints a home by heuristic or tie-break.
- **q6** — layout-version change as an owner-gated governance act (RFC9-16(d)).
  **Answered — owner decision A3**, narrowed after review 8.
- **q7** — proximity's declared meaning beyond containment (RFC9-9, RFC9-4).
  **Answered — owner decision B12(a).**

**Open follow-on, flagged by the rev10 RFC-0001 pass (not a numbered §8
question).** **Owner decision A6** minted `declared-dependency` in RFC1-25 and
thereby closed RFC-0001 §8 q6's *kernel-minting* question. A6 did **not** address
the adjacent part that question also raised: **whether RFC9-9's legend and
edge-channel rules need a pass now that a kernel-level declared dependency
relation exists** — whether the three-class edge taxonomy and the
profile-relation limb are correctly divided now that the declared class is a
kernel relation rather than only a profile one, and, beneath it, *who may add a
profile relation and under what gate* (which RFC9-9's maintenance note above
routes to **RFC1-7 and RFC1-26**). **No normative change is made on this pass** —
resolving it is owner-scoped and its home is RFC 0001, not this surface. The
surface is safe meanwhile under either answer: an unregistered profile relation
fails closed under RFC9-26 and never reaches a reader as an unlegended edge.
Recorded for the open-question triage; see history §8.

---

*End of module 1. Clauses RFC9-1 … RFC9-23, plus sub-clauses RFC9-8(a),
RFC9-9(a), RFC9-9(b), RFC9-13(a), RFC9-14(a), RFC9-15(b) and RFC9-16(d); no gaps,
no retired or merged numbers. Lettered limbs (RFC9-10(c), RFC9-19(b)) are parts
of their parent clause, not sub-clauses. Amend in place, never renumber.*
