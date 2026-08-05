# RFC 0009 — Orrery (Map Surface)

**Status:** Proposed foundational contract. This line is a self-declaration at authoring time (RFC3-16): effective status is established solely by the owner-act record binding this file's exact content digest, and acceptance edits nothing here. Absent such a record, this contract binds nothing.
**Date:** 2026-07-30 (amended through 2026-08-02)
**Serves:** VIS-1, VIS-2, VIS-3, VIS-7 (trust floor: legend fidelity, link rule); SEC-2, SEC-3, SEC-5; architecture.md (constitutional spatial requirement; exact 2D/tabular equivalents); v1.md (3D V0 mandate, coarse granularity, predominantly-Unknown maps); SDR §2 (Orrery charter and anti-thesis); SDR-3, SDR-19, SDR-20, SDR-21, SDR-22, SDR-23, SDR-24, SDR-25, SDR-26, SDR-27; resolves the map-surface portion of SDR §5 question 10. Historical state is part of `map/`'s constitutional scope by **adopted** doctrine amendment D1 (architecture.md, owner-ratified 2026-08-01); the concrete historical *interaction design* (ghost steps, milestone scenes, timeline scrubber) remains a non-binding candidate bundle held behind its own owner approval (RFC9-41).

---

## 0. Reader's summary (non-normative)

*Plain-language orientation. If this section and a clause ever disagree, the
clause wins.*

- Orrery is the **map surface**: a 3D/2D spatial rendering of the project as
  a city, built for spatial memory. Its named enemy is **spectacle
  displacing truth** — a green district with no evidence, a layout that
  quietly reshuffles, proposed structure rendered solid.
- **Home geography is anchored to capability identity, not file paths.**
  Renaming or refactoring code never moves the map. Position in home
  geography encodes only declared structure; alternate projections where
  position encodes a metric are explicitly selected, legended **analytical
  planes**, with return to home always available and discoverable.
- **Layout is a pure function of three inputs**: the declaration set, the
  layout baseline (declarations as of the last full regeneration), and the
  layout version. Insertion order is never an input. Within a version,
  positions are fixed; regeneration is full (never partial), manual, and an
  owner act with recorded rationale.
- **Nearness carries exactly three legend meanings**: declared containment
  (same district), declared relatedness (a rendered dependency edge,
  best-effort honored), and **residual adjacency — which carries no
  meaning**. The legend says so, and a reader can decide which is which.
- **Unknown is a first-class color.** A predominantly-grey map on an
  undeclared project is correct output. The unmapped district never
  disappears; aggregates disclose count, reason, and composition; absent a
  coverage record, "no code implements this" is Unknown, not an empty lot.
- Every visual channel (color, height, edges…) is **registered and
  legended** — height means one declared thing per lens; unregistered
  encodings fail closed and never reach a reader.
- **Non-3D views are co-equal**: same evaluation, same facts, same counts —
  a table and the scene disagreeing over one scope is release-blocking.
- Personal camera/view state is stamped with layout version + baseline and
  **never silently restores across a layout change**.
- Where the adopted release policy requires it, release needs a lawful
  **comprehension-walkthrough pass** — three artifacts: a kernel-recorded
  execution record, an attributed human judgment, and the owner-approved
  release policy that gives the pass its authority (RFC9-45) — plus the
  layout-obligation gates of RFC9-47.

Structure: §3 is the contract (RFC9-1 … RFC9-52 plus lettered sub-clauses);
§4 violation cases; §8 owner questions, answered ones marked in place.

---

## 1. Summary

The semantic contract of `map/` — the spatial comprehension surface (UI
codename Orrery): a **home geography** anchored to capability identity and
built for spatial memory, versus explicitly selected **analytical planes**
where position may encode a declared metric (SDR-21); layout-determinism
and append-stability obligations with a closed relocation-trigger set;
shared-component placement without double-counting (SDR-22); repository as
overlay (SDR-23); a reserved epistemic palette and per-channel declaration
contract; per-lens height (SDR-24); the V0 lens set and staging (SDR-20);
City-first scene profiles over one graph (SDR-19); base/intended/
proposed/historical scenarios (historical scope constitutional under adopted
amendment D1; its interaction design a non-binding candidate bundle,
RFC9-41); aggregation, semantic zoom, and
the never-disappearing unmapped district (SDR-25); the 3D/non-3D
equivalence gate (SDR-27); accessibility parity; performance as declared
scope-narrowing; no ambient motion at V0 (SDR-26). It is **semantics
only**: no rendering engine, graphics API, layout algorithm, or stack
choice appears here — determinism *obligations* are bound; algorithms are
not.

---

## 2. Motivation and doctrine grounding

The constitutional requirement is a spatial comprehension surface anchored
to **capability identities, not file paths** — refactoring must not
randomly relocate the map, layout must be reproducible from the same
snapshot, exact 2D/tabular equivalents always available [Observed:
architecture.md, "One kernel, three surfaces"]. V0 realizes it in 3D at
coarse granularity, capability identities from the project's own declared
artifacts, and **a predominantly-Unknown map on an undeclared project is
the correct output, not a defect** [Observed: v1.md]. The trust floor
makes every visual encoding mean exactly what its legend says and every
rendered map entity resolve to its identified target [Observed:
trust-and-evidence.md, floor]. The charter's anti-thesis names the
recognizable failures: a decorative 3D file tree, a single-metric software
city, an unstable layout, a scene whose encodings cannot be explained from
evidence [Observed: SDR §2].

[Inferred] The failure this contract guards against is **spectacle
displacing truth**: spatial rendering is the product's most seductive
surface and its cheapest place to lie — a synthesized flow, a green
district with no evidence, a layout that quietly reshuffles, a proposed
structure rendered solid. Every clause below makes one of those lies a
recognizable violation rather than an aesthetic choice.

---

## 3. The contract

Clauses are numbered `RFC9-n` for stable citation. Amend in place; retire
rather than renumber. Parentheticals beginning
*History:* are amendment records — when and why text changed — and carry
no normative force; the clause text around them is the contract.

### 3.1 Surface identity and scope

**RFC9-1.** `map/` is the semantic/spatial representation of observed,
intended, proposed, **and historical** system state [Observed:
architecture.md, as amended by adopted owner amendment D1]. Historical
scope is constitutional and unconditional; what remains deferred is the
concrete historical interaction design (§3.10, RFC9-41), which is candidate
design, not contract. Orrery is a working UI codename; technical names in schemas and
APIs stay literal [Observed: architecture.md, Vocabulary]. The map is a
projection over the one shared kernel — never independently authoritative;
its vocabulary (labels, tiers, Unknown reasons, freshness) is RFC 0002's,
rendered verbatim (RFC2-24/25), and its selection, drawer, and query
semantics are RFC 0006's, not re-defined here.

**RFC9-2.** This contract binds semantics and determinism obligations only.
Rendering technology, layout algorithms, and their tuning are
post-acceptance material; no conforming choice may weaken a clause here.

**RFC9-3.** Everything the map shows must be explainable from identified
artifacts: for any selected element, the exact channel readings currently
applied and the metric behind each must be reachable at the point of
selection. **Encoding provenance is a surface-local "explain this
encoding" affordance layered over the shared drawer — never a member of
the shared drawer fact set.** RFC6-18 fixes one fact set per (selection
reference, evaluation identity, scenario context), with no lens dimension,
consumed identically by every surface (RFC6-7); admitting the active
lens's channel bindings into it would make a deterministic, cross-surface
fact set vary with personal presentation state (VIS-6, exception (a);
RFC3-21), and having the kernel compute Orrery's channel bindings so they
could be shared would make a rendering concern a kernel fact and give
Polaris and Trajectory drawer fields about a map they do not render. The
affordance is nonetheless evidence-derived, not surface-invented: the
channel registry it reads is a governed artifact under `.syzygy/map/**`
(RFC9-26, RFC9-18) and the underlying metric values are drawer facts. A
scene element whose encoding cannot be traced to an identified artifact
must not render that encoding.

### 3.2 Semantic geography and anchoring

**RFC9-4.** **The anchoring rule.** Position in home geography is bound to
declared identity; measurement never moves a building. The spatial
hierarchy, coarse per v1.md: project → **capability district** (the anchor
level, RFC1-13/14) → **component block** (declared topology entry) →
**plot/building** (code element placed by a declared implementation
mapping, SDR-4/RFC1-16 class (i)). Interior detail below source/test
evidence renders as evidence listings, not modelled geometry — V0 owes no
symbol-level layout contract. [Inferred — hierarchy composition; anchor
level Observed per architecture.md and RFC1-13.]

**RFC9-5.** **What may anchor geography:** adopted capability identities;
adopted topology entries and their declared placements; declared
implementation mappings — including `declared-only` tier mappings
(RFC2-25): the *declaration* is the Observed fact that assigns the address,
while the unverified satisfaction claim renders Unknown on the epistemic
channels. **What may never anchor geography:** drafted/unadopted
declarations (they render in the proposed treatment with an "unadopted"
plate, outside the stable address space [Observed: v1.md; RFC1-14]);
inferred mappings (inference may **annotate** geography — hatched, with
provenance — never anchor it [Observed: trust-and-evidence.md]); file
paths (a path is an attribute, never an identity; path-derived arrangement
is confined to the unmapped district, §3.11); metrics of any kind;
proposals (RFC1-22, proposed *state* plane); personal presentation state
(VIS-6, exception (a)).

**RFC9-6.** Capability identity continuity is RFC 0001's: rename changes a
label and no coordinate (RFC1-10); split/merge mints successors with
`succeeds` edges, rendered as an explicit identity event with both old and
new identities visible — never a silent relocation (RFC1-11); retirement
ghosts the district and is a rendered event. A selection or URL pinned to a
retired district resolves per RFC6-11 — never a 404, never an
auto-redirect.

**RFC9-7.** Code that maps to no declared capability renders Unknown —
never silently inferred into a capability [Observed: v1.md] — and lives in
the unmapped district (§3.11), never in a plausible-looking neighborhood.

**RFC9-8.** The portfolio level is a **derived arrangement, not an
entity**: projects placed deterministically by project identity; grouping
and ordering are workspace-manifest concerns (SDR-29, RFC 0003);
cross-project relations render only where declared, otherwise
unconfirmed/asymmetric (SDR-30) — and inferred cross-project relations
never anchor placement. Those declared relations are **portfolio-profile
relations** (`depends-on`, `subproject-of`, `contains-project`;
RFC1-7, RFC3-14, RFC3-31), not kernel relations, and they legend as
themselves under RFC9-9's profile-relation rule — declared, with their
profile and semantic class named, and never rendered or counted as RFC1-25's
observed `depends_on`. A derived hierarchy view (RFC3-31, SDR-28) is a
rendering over those declarations and never a plane fact. **Portfolio arrangement is append-stable on
RFC9-15's terms:** onboarding a project must not perturb the placement of
projects already arranged. Determinism alone would permit a lawful
reshuffle of the whole portfolio view on every onboarding, and the
spatial-memory premise that justifies the 3D mandate applies at portfolio
scale exactly as it does inside a project.

**RFC9-8(a) — The portfolio needs the machinery it inherits the obligation
from.** *(History: added after review 8's ML-R15.)* RFC9-15's terms include a **closed**
relocation-trigger set (RFC9-16) whose only reorganisation route is a layout
version change, and layout versions are governed artifacts under a *project's*
`.syzygy/map/**` (RFC9-18). The portfolio is not a project — SDR-29 and
RFC3-21 put its arrangement in the **workspace manifest** — so as written it
inherited append-stability with no version registry, no reorganisation event,
no rationale record and no owner gate, and therefore **no lawful way ever to
re-lay it**. A workspace that grows to hundreds of projects one append at a
time reaches an unusable arrangement that an implementation can only refuse to
fix or fix unlawfully.

The portfolio therefore carries the **same machinery at workspace scope**: a
**portfolio layout version** and its registry, reorganisation events with
recorded rationale, and the RFC9-16(d) owner gate — all held in the workspace
manifest's governed space (RFC3-21) rather than in any project's
`.syzygy/map/**`, since no project owns the arrangement of its peers. RFC9-15(b)
applies unchanged at this scope: fixed within a version, full regeneration
only, order-independent, and RFC9-13(a)'s stamp-and-refuse rule covers
portfolio-scope saved cameras.

Two limits, stated so the symmetry is not over-read: the portfolio has **no
declared-relatedness reading of proximity** — RFC9-9 reading 2 is
capability-scoped, and the portfolio's declared relations are profile relations
whose positional expression this RFC does not bind — so there is no portfolio
backlog to partition. And the portfolio arrangement remains a **derived
arrangement, not an entity**: versioning how it is laid out does not make it a
plane fact. [Inferred — the obligation was already binding; only its
machinery was missing, and the workspace manifest is where RFC 0003 already
puts arrangement concerns.]

### 3.3 Home geography and analytical planes (SDR-21)

**RFC9-9.** Every project has **exactly one home geography**: stable,
capability-anchored, reproducible (§3.4), append-stable, built for spatial
memory. In home geography **position and proximity never encode a
measurement**.

The legend rule is *not* "proximity is inert." RFC9-4 builds project →
capability district → component block → plot, so intra-district adjacency
**is** declared capability membership expressed positionally; since RFC9-26
generates all legend text from the channel registry and VIS-7 requires the
legend to be exactly true, a generated line reading "proximity: inert"
would be false for intra-district adjacency — and suppressing the
containment reading to make it true would contradict RFC9-4.

**Proximity carries exactly two declared readings, and no third**
*(History: amended at acceptance by owner decision B12(a), which reversed the draft's
"proximity is inert beyond containment" position; read with **RFC9-9(a)**,
which adds a third **legend line** — residual adjacency, carries no meaning —
without adding a third reading):*

1. **Declared containment** (RFC9-4) — intra-district adjacency is capability
   membership expressed positionally.
2. **Declared relatedness** — a `declared-dependency` edge (RFC1-25, minted by
   owner decision A6) *may* be expressed positionally, so that capabilities
   declared to depend on one another tend to sit near one another.

**Proximity never encodes a measurement**, and no undeclared *signal* may be an
input to placement: adjacency-by-observed-coupling, adjacency-by-authorship or
-ownership, and clustering on any measured or lens-bound quantity are barred,
because a reader cannot tell which basis produced a given nearness. The two
readings above are the only ones proximity *carries*; they are not the only
thing that *produces* nearness, and RFC9-9(a) governs the remainder.

**Reading 2 is best-effort, and its shortfall is rendered, never hidden.**
Append-stability (RFC9-15) forbids relocating an existing district, so a newly
declared relatedness edge frequently *cannot* be satisfied without moving
something. When it cannot, the layout does not move anything and does not
pretend: each `declared-dependency` edge carries a rendered **honored /
not-honored** state on the map, and the count of not-honored declarations is a
first-class surfaced quantity (RFC9-15(b)). A not-honored edge is a true fact
about the current layout, not a defect and not an Unknown — the relation itself
is fully known; only its positional expression is unsatisfied, and the edge
still renders on its own explicit edge channel regardless.

[Inferred] The two readings are ordered: where containment and relatedness
compete for the same position, **containment wins**, because containment is
structural and total (every plot has exactly one district) while relatedness is
optional and partial. A layout that broke containment to honor relatedness
would falsify RFC9-4.

**RFC9-9(a) — Residual adjacency: the legend has three lines, not two.**
*(History: added after review 8's ML-R3, which found the two-line form false as written.
The finding is recorded here rather than silently repaired, because the false
version read as the stricter and more honest one.)*

The earlier text barred "adjacency-by-recency" in the same breath as
adjacency-by-observed-coupling. That is not a bound this contract can keep.
RFC9-16(a) **mandates** appending new entities into free space, and entities
that entered after the layout baseline take free space together. On a mature
map most nearness is neither containment nor honored relatedness — it is the
residue of the placement function. A generated legend (RFC9-26) reading only
"proximity: declared containment; declared relatedness" would be truthful about
what proximity is *permitted to encode* and **false about most of the adjacency
actually on the screen**, which is precisely the failure VIS-7's legend-fidelity
floor exists to prevent.

*One correction to the finding's mechanism, which matters for RFC9-15(b) part 3.*
The residue is not adjacency-by-**arrival order** — insertion order is never an
input to any coordinate, and that clause stands. It is adjacency-by
**baseline-delta**: "declared since the last full regeneration" is a shared
property of a set of entities, computed from (declaration set, layout baseline)
without reference to the order within it. Coarser than recency, deterministic,
and reproducible — and still a basis for nearness that is neither of the two
declared readings. The finding's conclusion therefore holds even though its
mechanism is one step off, and the repair is the same.

The repair is not to bar the mechanism and not to weaken the readings. It is to
**declare the residue**, in four binding parts:

1. **Three legend lines.** The position/proximity registry entry declares
   exactly three readings: *declared containment*; *declared relatedness,
   best-effort*; and **residual adjacency — carries no meaning**. All three are
   generated from the registry under RFC9-26. The third is a reading, not a
   footnote, and omitting it is an unlegended channel meaning.
2. **The residue must be reader-decidable, not merely disclaimed.** A nearness
   carries meaning only if it is **intra-district** — visible, because district
   boundary is a rendered reserved channel (RFC9-25) — or **accompanied by a
   rendered `declared-dependency` edge in honored state** — visible, because
   that edge renders on its own explicit channel with its state (RFC9-9(b)).
   Every other nearness is residual by construction. A reader can therefore
   decide which of the three readings applies to any given pair **from what is
   on the screen**, without access to the placement algorithm. This is what
   makes the third line honest rather than an escape hatch: a legend saying
   "some proximity means nothing and you cannot tell which" would be worse than
   the false two-line legend it replaces.
3. **The residue must not counterfeit the meaningful readings.** Free-space
   placement must not produce apparent grouping that mimics declared
   containment: no enclosure, shared boundary treatment, common plinth or
   ground plane, or visual clustering for entities related only by
   baseline-delta. The district boundary channel is reserved (RFC9-25) and
   residual placement may not approximate it. Otherwise part 2's
   decision procedure — "is it intra-district?" — stops being answerable
   by eye, and part 1's third line becomes unfalsifiable.
4. **The bar on undeclared signals stands, narrowed to *inputs*.** The test is
   on what the placement function reads, not on whether its output happens to
   look clustered. RFC9-14's input tuple is closed and names no observed,
   authored, or measured quantity, which is the enforcement point: a placement
   function reading observed coupling violates RFC9-14 before it violates this
   clause. Baseline-delta is admissible only because it is derivable from that
   closed tuple and because part 1 declares what it produces.

[Inferred — the finding is review 8's ML-R3; parts 1–4 are the drafter's
repair, and the reader-decidability requirement in part 2 is the load-bearing
one. A future amendment that keeps the third legend line while dropping part 2
or 3 has kept the disclaimer and lost the property it disclaims.]

**RFC9-9(b) — The honored / not-honored state is a channel, and is registered
as one.** *(History: added after review 8's ML-R5, which found the state asserted with no
epistemic class, no registry entry, no evidence path and no Unknown value —
i.e. rendered meaning outside the contract that governs all rendered meaning.)*

The positional-expression state of a `declared-dependency` edge is a rendered
distinction, so RFC9-26 binds it in full and it carries a registry entry like
any other channel:

- **Source metric / domain** — a closed three-value categorical domain:
  `honored` (the edge's endpoints are positionally near under the current
  layout), `not-honored` (they are not), and `unknown` (the layout cannot
  determine it — see below). Nearness here is the layout's own declared
  adjacency predicate, which the registry entry names; it is not a measured
  distance and does not vary by lens (RFC9-25: position is lens-invariant).
- **Update cadence and freshness** — the state is a function of the layout
  input tuple (RFC9-14), so it changes only on a relocation trigger
  (RFC9-16) or a declaration change, and it inherits the base layout's
  freshness carrier rather than defining its own.
- **Epistemic class** — the state is **[Observed]** with respect to the layout:
  it is computed from identified artifacts (the declaration set and the
  recorded base layout, RFC2-6) and is re-derivable. It is emphatically *not*
  an epistemic class of the **relation** — the relation is fully known, and a
  `not-honored` edge is a true fact about the layout, never an Unknown
  capability and never a defect (RFC9-9 above).
- **Evidence path** — resolvable to the governing declaration that minted the
  edge **and** to the layout version and baseline under which the state was
  computed (RFC9-18 registry entry). A state shown without the layout version
  it was computed under is unresolvable, because the same edge is lawfully
  `honored` under one version and `not-honored` under the next.
- **Unknown value** — required by RFC9-27 and non-hypothetical: an edge whose
  endpoints include an entity with no home placement (unmapped district,
  RFC9-44) has no adjacency to evaluate. It renders the reserved Unknown
  treatment with reason `missing-declaration` (RFC2-24 #4) where the placement
  declaration is absent, and it is **not** counted in either partition of the
  RFC9-15(b) part 4 backlog — an Unknown is not a not-honored edge, and folding
  it into the refresh-clearable count would put a number in front of the owner
  that a refresh cannot move.
- **Fail-closed** — with no registry entry the state does not render, and the
  edge renders without it. RFC9-26's rule admits no exception here.

[Inferred — review 8's ML-R5. The Unknown limb and the backlog-exclusion are
the parts a naive implementation gets wrong: both partitions in RFC9-15(b) part
4 presuppose two placed endpoints.]

Dependency edges render on their own explicit, resolvable edge channel,
**legended by the relation that actually exists** — the kernel relation from
RFC1-25's closed vocabulary, or, where an adopted extension profile *adds* a
relation rather than the kernel closing one, that **profile relation named as
itself**. Three classes of intra-project dependency edge exist, and **no edge
of one class is ever evidence of another** (RFC1-25(b)'s twelve-pair
invariant, which is mechanically checkable and binds this surface as much as
the query endpoints):

- **Observed** — `depends_on` code→code, `structurally_related`. Adapter- and
  snapshot-backed.
- **Execution-class** — `depends_on` work→work. Scheduler-authoritative.
- **Declared** — `declared-dependency` between capabilities, or between
  topology entries (RFC1-25, **minted at acceptance by owner decision A6**).
  Desired/declared, owner-adopted through a governance artifact.

No edge may be legended "declared" unless a declared relation backs it —
legending an observed edge as a declaration is exactly the conflation SDR-3
forbids. **The declared-dependency channel this RFC previously promised with
nothing to fill it is now backed by a real relation**; the foundation defect
reported at §5 defect 1 and the acceptance question at §8 q5 are **discharged
by A6**, and both are marked accordingly rather than left standing. An
*undeclared* dependency is still never inferred from an observed one: absence
of a `declared-dependency` edge renders Unknown (`missing-declaration`), never
"no dependency".

**The declared channel is also the positional one.** RFC9-9 reading 2 expresses
`declared-dependency` — and only `declared-dependency` — through proximity.
Observed and execution-class edges render on the edge channel alone and never
influence position, because doing so would be the adjacency-by-observed-coupling
that reading 2's bound explicitly bars.

**Profile relations legend as themselves (RFC1-26, second limb).** RFC1-26
permits an adopted profile to add relations without re-typing the closed set,
and the portfolio profile does exactly that: `depends-on`,
`subproject-of` and `contains-project` are Project→Project relations of
**Desired (declared)** semantic class and owner-adopted authority (RFC1-7;
RFC3-14; RFC3-31), and RFC 0003 §7 leaves the cross-project type vocabulary
deliberately open to further portfolio-profile material — so this is a
standing shape, not one relation. An edge carrying a profile relation renders
on the same explicit channel, and its legend names (i) the relation's own
declared name, (ii) the profile that adds it, and (iii) its semantic class and
authority. It is never coerced into the nearest kernel relation, and never
left unlegended because RFC1-25's table does not name it. The channel
registry is the enforcement point: a profile relation with **no registry
entry does not render**, under RFC9-26's fail-closed rule that governs every
other channel — and, on RFC9-35's pattern for lenses, a profile relation that
is to render arrives with its registry entry, legend, Unknown behavior and
tabular equivalent in the same increment, never as an edge drawn first and
declared later.

**RFC1-25's anti-conflation rule binds here as a rendering rule.** A declared
project-scope edge is **never rendered, legended, filtered, counted, or
query-answered as** RFC1-25's observed `depends_on`, and neither is evidence
of the other; the two may not share a mark, a channel treatment, a legend
entry, or a count. A portfolio view drawing declared project intent in the
same stroke as observed code coupling has made a Desired-plane assertion look
like an observation — the conflation RFC1-25(b)'s twelve-pair invariant
exists to prevent (the relation names themselves carry no separation: the
owner deliberately kept the one-character `depends_on`/`depends-on`
collision at acceptance, B20/RFC3-14), reproduced one layer out, at the
place a reader actually sees it. One-sided
or mutually incompatible declarations render **unconfirmed/asymmetric**,
never as a resolved mutual dependency and never silently reconciled (RFC9-8;
SDR-30; RFC1-7; RFC3-14; RFC3-31).

[Inferred — the operational form of SDR-21's "home" regime. **§8 q7 is
closed**, not open: the owner settled at acceptance (decision B12(a)) that
adjacency carries the second declared reading, and RFC9-9's two readings,
RFC9-9(a)'s three legend lines and RFC9-9(b)'s state channel are that decision's
consequences. *(History: corrected after review 8's ML-N2 — this note still described the
question as surfaced and unanswered, which would route a reader who reached
§8 q7 into re-deciding a settled matter.)* The profile-relation limbs are
Inferred as the legend-fidelity form of RFC1-26's second sentence.]

[**A maintenance note, not a ruling.** The profile-relation rule above is
written **generally**, not for `depends-on` alone, because RFC 0003 §7
leaves the cross-project relation vocabulary open by design and more profile
relations are expected. What this surface does **not** decide is *who may add
a profile relation, and under what gate* — that belongs to **RFC1-7 and
RFC1-26**, which govern profiles, and it is the same authority question §8 q4
and q9 pose for analytical planes and lenses. The rule here is safe under
either answer: an unregistered profile relation fails closed and does not
render, so an ungoverned addition cannot reach a reader as an unlegended
edge.]

**RFC9-10.** An **analytical plane** is an explicitly selected alternate
projection in which position and/or proximity encode a **declared metric or
relation** (a dependency-distance analytical plane, a
component/architecture analytical plane, a churn-clustering analytical
plane). Every analytical plane must: (a) declare its position and
proximity semantics as first-class legend entries; (b) carry a persistent,
non-dismissible marker that it is not home; (c) be **visibly temporary, with
return to home geography always available and discoverable** — the reader is
never stranded outside home, and the *interaction cost* of returning is not
bound here (§8 q10; **the owner granted this relaxation at acceptance,
decision B21**, over the drafted position that SDR-21's "one action" is
ratified text a contract clause may not narrow by prose). SDR-21's bound is
relaxed by the ratifier, which is the only party who may relax it; the
recorded cost is that a release check could have counted actions and can no
longer, on the surface whose whole contract is checkability. CC-VIZ-5 is
amended to match. (d) name the evaluation it projects.
Analytical-plane layouts are deterministic per (analytical-plane definition, evaluation) but carry **no
append-stability or cross-evaluation coordinate promise**, and must say so.
[Observed: SDR-21; obligations (a)–(d) Inferred as its contract form.]

**RFC9-11.** **The mode boundary is a contract: an analytical layout may
never masquerade as home.** The surface's default scene is home geography;
entering an analytical plane is an explicit, labelled act; no analytical
plane may suppress its marker; spatial-memory affordances (saved camera
homes, "you are here" continuity) attach to home only. A view that binds
position to a metric without the analytical-plane marker is a violation
identical in class to an unlegended channel (VIS-7). [Inferred]

**RFC9-12.** Lens switching within home geography re-skins and never moves
anything: same camera, same selection, same geography, visible legend swap.
Any view change that moves entities is by definition an analytical-plane
or scenario switch and is labelled as one. [Inferred, from RFC9-4 +
SDR-21]

**RFC9-13.** Personal presentation state — camera, filters, bookmarks,
saved lens/analytical-plane selections — lives in `.syzygy/local/` and
never affects
truth-bearing encodings (VIS-6, exception (a); RFC3-21). A filter that
hides entities shows a persistent count of what it hid.

**RFC9-13(a) — Coordinate-bearing personal state is stamped with the layout
version, and never restores silently across one.** *(History: added after review 8's
ML-R12.)*

A saved camera home is stored **coordinates**, and a layout version change
(RFC9-16(d)) moves every declared entity. The saved home therefore comes to
point not at a dangling reference — which would be visible — but at a
*different district*, which is not. RFC 0006's protections do not reach this:
RFC6-1's no-surface-local-handle rule, RFC6-9's rename stability and RFC6-11's
never-404-never-auto-redirect all govern **selection references**, which are
identity-bearing; camera state is not one. And RFC9-13's own "personal state
never affects truth-bearing encodings" is protection in the wrong direction —
here the truth-bearing layout silently invalidates the personal state.

Three obligations, and they are cheap:

1. **Stamp.** Every coordinate-bearing item of personal state (saved camera
   homes, "you are here" continuity anchors, position-anchored bookmarks)
   records the layout version and baseline it was saved under.
2. **Anchor where an anchor exists.** Where the save was made against a
   selected entity, it records that **identity** alongside the coordinates,
   and restores by re-resolving the identity under the current layout. This is
   the RFC6-9 treatment applied to the one artifact that had been left out of
   it, and it is the behaviour that preserves the reader's actual intent.
3. **Never land silently on a mismatch.** With no identity anchor and a
   version mismatch, the surface **does not restore the raw coordinates
   silently**. It marks the saved home **stale-layout**, names the version it
   was saved under and the current one, offers the reorganisation event's
   before/after (RFC9-16(d)), and restores raw coordinates only on an explicit
   act that says what is being done.

*Why this is contract material and not interaction polish.* Spatial memory is
the entire stated justification for the 3D mandate (RFC9-15), and a saved
camera home is the one artifact in this contract that **is** materialized
spatial memory. The failure it produces is RFC9-45's exact release signature —
a reader stating something false that the map supported ("Billing has
collapsed", when the camera landed on Auth) — reached through a lawful,
announced, owner-gated act with nothing anywhere marked wrong. [Inferred —
review 8's ML-R12; obligation 3 is the load-bearing one, since 1 and 2 without
it merely record enough to know the restore was wrong.]

### 3.4 Layout determinism and stability

**RFC9-14.** **Two-tier layout contract.** The **declared-identity base
layout** is a deterministic function of the **layout input tuple** —

> **(declaration set, layout baseline, layout version)**

— and nothing else; it is part of the deterministic observation record and
inside the VIS-7 identity test [Observed: architecture.md — determinism is
asserted over the observed graph *and base layout*; layout versions are
snapshot inputs, RFC2-1 item 7].

**RFC9-14(a) — The three inputs, defined.** *(History: added after review 8's ML-R1 and
ML-N1; the earlier two-input form was **false as written** — see RFC9-15(b).)*

- **Declaration set** — the closed set of declared facts the layout may read:
  the deterministic observed graph's declared identity set; declared topology
  entries and their `placed_in` edges (RFC1-25); and **adopted
  `declared-dependency` edges** (RFC1-25). The third item is named explicitly
  because the earlier wording said "declared identity set, declared topology
  and placements", which excludes edges — an implementer following it literally
  could never honor RFC9-9 reading 2 at all. Unadopted declarations are not
  members (RFC1-22: proposed never anchors).
- **Layout baseline** — the declaration set **as it stood at the most recent
  full regeneration** (RFC9-15(b) part 2). It is a governed, identified artifact
  under `.syzygy/map/**` (RFC9-18), written by the regeneration act, immutable
  thereafter, and a **snapshot input** (RFC2-1 item 7, as a layout input
  alongside layout version). It is what makes append-stability expressible: the
  layout holds fixed whatever the baseline placed, and appends fill free space
  around it.
- **Layout version** — the placement algorithm's governed version (RFC9-18).

**The baseline is a real input and is recorded as one.** Without it the model is
over-determined and non-reproducible: whether a `declared-dependency` edge is
honored depends on whether it was present at the last regeneration, so two
implementations handed only (declaration set, layout version) can lawfully
disagree on every coordinate and on the RFC9-15(b) backlog count — a
release-blocking trust-floor disagreement under RFC6-22/23, and a recorded base
layout (RFC2-6) that no longer reproduces. Recording the baseline is what
discharges RFC9-47's determinism gate. [Inferred — the defect and this repair
are review 8's ML-R1; the owner's refresh model always implied a baseline, and
the earlier clause simply failed to name it.]

The **path-derived arrangement** — the
interior of the unmapped district — is deterministic given the snapshot's
declared working-tree state but is explicitly excluded from the
cross-snapshot stability guarantee and says so on its face.

**RFC9-15.** **Append-stability.** Adding one capability, component,
building, or — at portfolio scale (RFC9-8) — one project must not perturb
the coordinates or placement of any existing declared entity.
Determinism alone does not give stability — a reproducible layout that
reshuffles on every addition destroys the spatial memory that justifies the
3D mandate. Append-stability is a release-gated, fixture-tested property
(§3.12), not a trusted one. [Inferred — obligation; mechanism deliberately
unspecified.]

**RFC9-16.** **The closed relocation-trigger set.** A declared entity's
home coordinates change only on: (a) capability/topology creation or
retirement (append to free space; ghost then remove); (b) split/merge —
rendered as an identity event per RFC9-6; (c) a declared placement change —
announced with its governing decision or declaration link; (d) a **layout
version change** — announced as a reorganisation event naming the old and
new layout versions, with before/after reachable, **and carrying a
recorded rationale naming what the new layout buys and what it moves**
(recorded with the reorganisation event under `.syzygy/map/**`, RFC9-18).
A version change with no recorded rationale is not a lawful trigger.
Every trigger is a rendered event; none is a silent teleport. The
reorganisation event is also what coordinate-bearing personal state resolves
against when it is found stale (RFC9-13(a)); announcing the move to the
*scene* is not by itself announcing it to the reader's saved views.

**RFC9-16(d) is owner-gated, with one narrow carve-out** *(settled at acceptance
by owner decision A3; narrowed by the same owner after review 8's ML-R2 and
ML-R7).* A layout version change is an **owner governance act** carrying the
recorded rationale above — **except** where the two versions are demonstrated to
be the **same placement function**, in which case a recorded note suffices.

**"Same placement function" means agreement on every input, not on one.**
The demonstration must establish that for **all** layout input tuples
(RFC9-14), the two versions compute identical coordinates. In practice this
covers versions whose placement path is unchanged — refactors, renames,
dependency bumps, changes confined to rendering rather than placement — and
**little else**. A version that changes placement behaviour for any input,
however rare that input, does not qualify however many inputs it agrees on.

*Why the carve-out is this narrow.* [Inferred — review 8's ML-R2, whose failure
case is recorded here because the earlier, looser form read as reasonable.] The
clause previously required rendering **one** declaration set under both versions
and comparing. But a layout version is not a claim about one declaration set; it
is a function applied to every set the project will subsequently reach.
Agreement on D says nothing about D ∪ {X}. A version that widens its spacing
above eight districts agrees perfectly on a six-district project — the note is
filed honestly, no governance act occurs — and then relocates every district on
the ninth append, under trigger (a), with no reorganisation event, no rationale,
and no owner act anywhere in the sequence. The narrow form closes that path at
the cost of making most real layout changes gated, which is the correct side to
err on for the property the whole 3D mandate rests on.

**The demonstration is not an RFC2-3 identity test, and this clause no longer
cites it as one.** *(History: corrected after review 8's ML-R7.)* RFC2-3 identifies an
evaluation as (source snapshot, as-of instant) and its test is explicitly
*intra*-evaluation — "two runs of **one** identified evaluation". Layout version
is a snapshot input (RFC2-1 item 7), so two layout versions are two snapshots and
two evaluations, and RFC2-3 says nothing about comparing them. What is required
here is a distinct **layout-equivalence check**: a harness that exercises both
versions over a declared input space and compares coordinates, whose result is
recorded with the note. An *asserted* equivalence is not a carve-out — it is an
ungated relocation — and absent the recorded check the governance act is
required.

**RFC9-15(b) — Fixed locations, manually refreshed.** *(History: added at acceptance;
owner-proposed model, superseding the layout tiebreak that decision B12(a)
would otherwise have required.)* Home coordinates are **fixed within a layout
version and regenerated only by owner act between versions.** The model has
four binding parts:

1. **Within a version, nothing moves.** Incremental declarations append into
   free space (RFC9-16(a)) and never relocate an existing entity. Declared
   relatedness (RFC9-9 reading 2) that cannot be honored without moving
   something is simply not honored, and renders as such.
2. **Regeneration is full, never partial.** An owner-run refresh repositions
   **every** district from the current declaration set. Scoped regeneration —
   refreshing "core" zones while others hold — is **barred**: it would make
   coordinates a function of refresh history, reintroducing exactly the
   path-dependence part 3 exists to remove, and it breaks spatial memory
   unevenly, which is worse than breaking it wholly and announcing it.
3. **Both placements are pure functions of the RFC9-14 input tuple —
   (declaration set, layout baseline, layout version) — and insertion order is
   never an input to any coordinate.** Two conforming implementations given the
   same tuple, in any order, must produce identical coordinates. *(History: corrected
   after review 8's ML-R1. The clause previously named a **two**-input tuple,
   omitting the baseline; that form was **false**, and demonstrably so: parts 2
   and 3 are jointly non-vacuous only if a baseline input exists, since
   "regenerate some zones while others hold" is unexpressible in a function with
   nothing to hold from. The requirement was right; the input list was wrong,
   and the omission would have let two conforming renderings disagree on every
   coordinate.)* Append-stability does not imply order-independence, which is
   why part 3 states it separately: without it the RFC2-6 recorded base layout
   is checkable but not reproducible.
4. **The backlog is surfaced, and split by what can actually clear it.** The
   not-honored declared-relatedness edges are rendered as a first-class
   quantity, partitioned into:
   - **refresh-clearable** — a full regeneration could honor them; and
   - **structurally unhonorable** — no layout at any version can honor them,
     because containment wins (RFC9-9) and the two endpoints sit in different
     districts whose extents cannot both contain the pair. Cross-district
     `declared-dependency` between **topology entries** is the systematic case:
     each is pinned inside its own capability district by `placed_in`, and at
     most the few pairs meeting at a shared district boundary can ever be
     adjacent.

   **The partition is mandatory, and an unpartitioned backlog count must not
   render.** *(History: added after review 8's ML-R4.)* A signal with a permanent,
   unannounced nonzero floor is not a signal: an owner told "12 not honored"
   cannot distinguish twelve a refresh would fix from twelve nothing will ever
   fix, and part 4's own stated purpose invites them to pay the model's maximum
   cost — a full reorganisation that invalidates every memorized location — for
   no benefit. Only the **refresh-clearable** count is a refresh signal; the
   structural count is a standing fact about the declaration set, and its
   resolution route is a declaration or placement change, never a refresh.

   A refresh is never automatic and never triggered by declaration change; the
   trigger is an owner act under RFC9-16(d).

**Explicitly not a trigger: a district exhausting its reserved extent.**
The trigger set is closed, and growth is not on it. Reservation policy is
unbounded in principle (RFC9-17), so ordinary growth of a district's or
block's declared membership never *forces* a relocation; an implementation
that finds itself choosing between displacing neighbours (forbidden by
RFC9-15/17) and bumping the layout version has a reservation defect, and
the correct response is to fix the reservation policy, not to take the
(d) hatch. Without this the (d) hatch is reached by ordinary growth rather
than by deliberate reorganisation.

[Inferred. **§8 q6 is closed; this note records how.** *(History: rewritten after
review 8's ML-R14; the earlier text still read "nothing currently gates it,"
which contradicted RFC9-16(d) two clauses above.)* The drafted position — that
a layout version change should be an **owner-gated governance act**, not an act
Syzygy, an agent, may take unannounced — was **routed to the owner and adopted**
(decision A3), then narrowed after review 8's ML-R2 to the single carve-out
RFC9-16(d) states. The gate accordingly lives in RFC9-16(d) and binds now.

What remains true from the earlier note is only the *provenance* of that gate,
which is worth keeping because it explains why the clause reads as it does:
neither RFC3-18 nor doctrine supplied it. RFC3-18 binds the namespace class and
confers no adoption gate, and VIS-4's shape-level sign-off list does not name
layout. The gate is therefore an **extension of VIS-4's list made by owner
decision at acceptance**, not a restatement of existing doctrine — which is why
it is recorded as A3 and attributed to the owner rather than to this RFC's
drafter. The obligations in RFC9-16 bind independently of the gate; the gate
adds who may pull the trigger.]

**RFC9-17.** **Forbidden churn.** None of the following may change a
declared entity's home coordinates: file move/rename/reformat or any
refactor that preserves the declared mapping; any metric change in any
lens; a new evaluation over an unchanged snapshot, at any as-of instant
(the base layout is inside the identity test); lens switching, filters,
camera, or personal state; footprint/size band changes (a measured band
varies only within its reserved extent and never displaces a neighbor).
Any of these causing movement is a defect, not a preference.
**Reservation policy must be unbounded in principle:** a district's or
block's reserved extent must be capable of accommodating any lawful growth
of its declared membership without displacing a neighbour, so that growth
never requires a layout-version change (RFC9-16(d)). Exhausting a
reservation is a defect in the reservation policy, never a licence to
relocate. [Inferred, from RFC9-4/14; reserved-extent device adopted from
the research disposition of O-F3.]

**RFC9-18.** Layout versions are governed artifacts under `.syzygy/map/**`
(RFC3-18): version registry and reorganisation-event records are governed;
computed geometry is rebuildable projection (`cache/`, RFC3-20); camera
and view state are personal (`local/`, RFC3-21). Registry entries fix which
layout version a scene's positions *mean* — the reference every
reorganisation event and every stability guarantee (§3.4) is read against —
so they are honored **only under RFC3-16(a)**; an entry whose owner-act
provenance does not verify does not establish a version, and scenes
resolving against it render Unknown rather than silently against a version
an untrusted writer declared. [Inferred] Nothing in `map/` becomes
independently authoritative over kernel semantics.

### 3.5 Shared components and identity counting (SDR-22)

**RFC9-19.** A code element or component may carry declared mappings to
multiple capabilities (RFC1-17). The map must support all **three
placement mechanisms** and never force a shared component into one
arbitrary capability district [Observed: SDR-22]: (a) the
**component/architecture plane** — an analytical plane (§3.3) rendering
the full multi-capability edge structure; (b) a **shared-infrastructure
district** in home geography, membership by declaration; (c)
**multi-capability presence**: the component stands at its declared home
placement, and every other mapped district renders a link marker that
resolves to the one entity — **never a clone**. *(Mechanism (c) is available
only where a **determinate** declared home exists; where the declarations
compete, RFC9-20 governs and the entity is Unknown-placed. See RFC9-20's
general case, added after review 8's ML-R8.)* Two separately selectable
copies of one identity break identity-based counting (RFC1-17, RFC9-21)
and selection identity (RFC6-1: each copy would carry its own handle for a
single identified entity). The trust-floor link rule is not the rule at
stake — both copies would still resolve to the identified target — which
is why the no-clone rule rests on counting and selection identity instead.

**RFC9-20.** Home placement of a multi-capability component comes only
from declaration: a declared primary placement in topology, or declared
shared-infrastructure membership. Absent any declared basis, the
component renders in the shared-infrastructure district's explicitly
marked **placement-undeclared** aggregation (Unknown reason
`missing-declaration`, RFC2-24 #1, routing to the drafting affordance) —
the map never mints a home by heuristic or tie-break: an undeclared
placement decided by an algorithm is a governance answer given by a
renderer.

**Over-declaration is a Contradiction, not a precedence problem.** Where a
component carries two co-unsatisfiable declared placements in one scope —
a declared primary topology placement and a declared shared-infrastructure
membership naming different homes — the map renders it **Unknown-placed**
with the conflict marker and the adjudication route surfaced (RFC2-15;
RFC9-24's Contradicted treatment), exactly as the undeclared case renders
its placement-undeclared aggregation. No precedence rule may resolve it:
"primary placement wins" is the same renderer-decides-governance error
this clause exists to prevent, and no surface may silently pick a winner
[Observed: architecture.md]. [Inferred — SDR-22 applied; deliberately
diverges from the research's minted-sticky-home rule, §6.]

**The general case: two `placed_in` edges.** *(History: added after review 8's ML-R8.
The paragraph above was written narrowly — "a declared primary topology
placement and a declared shared-infrastructure membership naming different
homes" — and did not visibly cover the plainest form of the conflict, which
left RFC9-19(c) and this clause giving opposite answers for it.)*

`placed_in` is **not functional and carries no primacy marker** (RFC1-25(c)),
so a topology entry with two adopted `placed_in` edges has **two declared
homes and no declared basis for choosing between them**. That is the same
Contradiction, and it takes the same treatment: **Unknown-placed**, conflict
marker, adjudication route surfaced. It is not a case for RFC9-19(c), because
(c) requires a determinate declared home to stand at and there is none; and it
is not a case for a tie-break, because every available tie-break — lexical,
adoption order, edge order, "first declared wins" — is a renderer answering a
governance question, which is exactly what this clause forbids. The word
"primary" in the paragraph above names a **declared** primacy where a
governance artifact supplies one; it never licenses a surface to designate one.

Counting follows placement, without exception: an Unknown-placed entry counts
in **neither** candidate district's composition and once in the Unknown-placed
aggregation. It does not count in both (that would be RFC9-21 double-counting
against an identity with no home) and does not count in one (that would be the
tie-break re-entering through the count after being barred from the layout).

**RFC9-21.** **Identity-based counting, never double-counting.**
Aggregates count each identity once per query subject (RFC1-17): a shared
component counts once in each district that queries it and once at project
scope. Because district totals may therefore sum to more than the project
total, the disclosure trigger is scoped to the **scene**, not to a table:
**wherever a shared contribution is counted into more than one rendered
aggregate, every rendered aggregate that includes it discloses the
shared-contribution count** ("N shared, counted once at project scope").
A trigger written in the tabular idiom — "any view presenting district
aggregates side-by-side with a project aggregate" — would not fire on the
surface this RFC governs: a 3D scene presents every district side-by-side
with every other and rarely renders an explicit numeric project aggregate,
so a shared component contributing its full measured value to three
districts would render three tall districts and a reader would sum by eye
and conclude there is three times as much there as there is. A district
total that silently absorbs shared components — or a project total
computed by summing districts — is comprehensible fiction (VIS-1).

### 3.6 Repository and authority overlays (SDR-23)

**RFC9-22.** Repository membership is an **overlay, never the primary
geography**: a capability district may contain buildings from several
repositories; repository boundaries render as a toggleable boundary
treatment. Partitioning space by repository first would re-anchor geography
to a storage fact [Observed: SDR-23; architecture.md]. A repository present
but unconsented renders as an explicit walled, Unknown-filled zone — never
empty ground, which reads as "nothing there" (RFC1-3).

**RFC9-23.** Authority and trust boundaries are a first-class overlay:
governance root as a civic marker — legended as the only place Syzygy
writes **project content directly** (VIS-5); adapter-mediated authorities
(VCS metadata, scheduler, CI, runtime) as a distinct boundary kind with the
adapter and its authorization visible; consent scopes rendered on the
project's surface [Observed: SEC-2]; execution-profile boundaries
[Observed: SEC-3; RFC5-20]; secret-exclusion zones as sealed markers at a
**declared minimum aggregation** — never content, and never a per-element
match count (the granularity bound is RFC9-29) [Observed: SEC-5]. Write
authority a reader cannot see is the surprise this overlay exists to
prevent.

### 3.7 Visual grammar: reserved palette and channel contract

**RFC9-24.** **The reserved state palette.** The map renders these states
with reserved, mutually distinct treatments no lens may repurpose. Only
**Observed / Inferred / Unknown** are epistemic labels (exclusive,
trust-and-evidence.md); the rest are sibling states rendered alongside a
label, never fourth labels (RFC2-25): **Contradicted** (Unknown base +
conflict marker + adjudication route — no surface silently picks a winner
[Observed: architecture.md]); **Dismissed by decision** (struck plate with
reason + expiry; never green, resolved, or aligned); **Proposed/
speculative** (wireframe + translucency — never looks like existing
structure [Observed: trust-and-evidence.md]); **Unadopted draft** (proposed
treatment + "unadopted" plate; anchors nothing). The freshness family —
fresh / stale / broken / superseded — applies on top of any state
(RFC2-10): stale desaturates with an age plate; broken shows last-good
marked broken, never failing invisibly; superseded ghosts. Concrete
treatment *values* (hues, materials) are design-contract material; the
role reservations are bound here.

**RFC9-25.** **Reserved channels.** Position, district boundary, the
epistemic rim/plate carrier, and saturation/chroma (the freshness carrier)
are lens-invariant. **Freshness owns the saturation channel exclusively: no
lens ramp may vary saturation**, so a desaturated element always means stale
and never "low on this ramp." A lens ramp varies whatever channels the
chosen color model leaves free once saturation is reserved — which channels
those are, and how the reservation is realized, is rendering material this
RFC does not bind (RFC9-2; §7), but the reservation itself is a
legend-fidelity obligation and holds in every profile. Body color, height,
heat, and other measured channels are lens-bound under RFC9-28. [Inferred
— operational form of the legend-fidelity floor.]

**RFC9-26.** **The channel declaration contract.** Every channel that
carries meaning declares, in a machine-readable registry from which all
legend text is generated (never hand-authored per channel): its **source
metric**, **unit or category domain** (with measurement window where
windowed — the window is part of the meaning and renders beside the
legend), **update cadence**, **freshness behavior**, **Unknown
rendering**, **evidence path** (resolvable per the floor's link rule), and
**legend semantics**. A channel carrying no meaning is declared inert in
its legend. One channel, one meaning at a time, never unlegended
(VIS-7 floor bullet 3). **The registry is fail-closed: a channel with no
registry entry must not render.** There is no hand-authored fallback
legend and no default meaning — an unregistered channel is a missing
declaration, and rendering it would put meaning on the scene that no
generated legend can account for. [Inferred — the registry's failure mode,
stated so the first unregistered channel does not ship with a
hand-authored legend.] **An entry present is not thereby an entry
authorized:** because all legend text is generated from this registry, an
entry fixes what an encoding *means*, so entries are honored **only under
RFC3-16(a)**, and an entry whose owner-act provenance does not verify is
treated exactly as an absent one — the channel does not render. [Inferred]
A forged entry is the sharper failure than a missing one: absence stops the
render, while a re-declared meaning leaves every claim, tier and freshness
check passing and re-points the legend under a correct scene, which is a
direct attack on the VIS-7 trust floor that no downstream status check
inspects.

**RFC9-27.** **Unknown is never invisible.** Every channel defines a
mandatory Unknown value, visually distinct from both ends of its own scale
and from any "good" reading — never green, never zero/empty/absent-looking
(an Unknown height is a marked stub, never zero; an unmeasured heat region
is marked unmeasured, never cold; a missing quantity renders Unknown,
never 0, SDR-6). Every Unknown element carries its RFC2-24 reason,
rendered verbatim, with the reason's resolution route as an affordance. No
epistemic state is carried by color alone: each carries at least two of
{surface treatment, plate/badge, label} (§3.12).

**Unknown is never invisible *at any scale*.** The rule binds per channel
per element and, in the same reserved vocabulary, per channel per
**aggregate**: an aggregated measured channel carries its Unknown
contribution rather than quietly aggregating over only the members that
have values (RFC9-43 states the aggregate form and its legend obligation).
Merging elements into a block or district is not a place where Unknown
becomes zero. This is one rule with two scopes, not two rules.

**Empty-looking is earned, not defaulted:** a **plot, block, or district**
renders *empty* ("declared, nothing built here") only when backed by an
executed mapping coverage record (RFC4-27) covering its declared scope;
absent that record it renders Unknown with reason
`mapping-coverage-absent` (RFC2-24 #5) — an unexecuted mapping is not
evidence of absence. The rule binds **every level of the hierarchy**
(plot, block, district) and **every scenario scene, including the
approved-intent and proposed scenes** (§3.10): nothing anywhere on the map
is permitted to look empty by default, and no level of aggregation is a
place where the obligation lapses.

**RFC9-28.** **Height (SDR-24).** Height has exactly **one declared
meaning per active lens**, always visible in the legend; **no universal
height meaning is frozen** by this contract. A lens's height metric obeys
RFC9-26 in full; the Unknown height treatment of RFC9-27 is lens-invariant.
The "software city where height = LOC is the whole product" is the named
anti-thesis, excluded by the lens contract, not by freezing the channel.

**RFC9-29.** **Text is a channel.** Labels, plates, counts, breadcrumbs,
and tooltips state only what identified artifacts state; truncation is
marked, never silent; an Unknown entity carries an explicit "Unknown"
label, never an omitted one. No text may derive from secret-matched or
unclassifiable content — a connection string in a map tooltip is doctrine's
own named violation [Observed: SEC-5]; excluded content contributes only a
sealed-marker disclosure **at a declared minimum aggregation, never a
per-element match count**. A per-building sealed marker carrying its own
match count *is* a per-file match count rendered spatially — RFC6-27's
violation case 10 — disclosing the *shape* of the excluded material (which
files, how many matches each, clustered where) while withholding only its
content. SEC-5 sanctions rendering **the exclusion**, not its shape; the
map is the surface where that shape is most legible, so the granularity
bound is stated here and applies to every sealed marker (RFC9-23).

**RFC9-30.** Inferred contributions render in the inferred treatment
(hatched + provenance) and never raise a status-bearing encoding; an open
admitted challenge suspends the displayed claim to Unknown
(`challenge-suspended`, `suspended` tier) with the deterministic basis
visible (RFC2-8/13/14). Absent SEC-2 consent, inference-dependent renderings
degrade to Unknown (`unconsented-source-or-provider`) — never error out,
never fall back to a heuristic.

### 3.8 Lens contract and the V0 set (SDR-20)

**RFC9-31.** A **lens** is an explicitly selected binding of measured
channels over home geography. A lens may bind: body color, height, heat,
banded footprint-within-reserved-extent, and edge weight — each under
RFC9-26. A lens may never: repurpose a reserved channel or palette state
(RFC9-24/25), move an entity (RFC9-12), suppress an overlay's epistemic
content, or render without its full legend. Exactly one lens is active at
a time.

**Overlays are lens-independent, and the rule that makes them so is a
constraint, not an observation: an overlay may never bind a
measured-magnitude channel.** An overlay carrying epistemic content
(freshness/staleness) or non-epistemic, non-magnitude content — including
execution-plane fact such as scheduler state (RFC1-22) — renders as
**categorical or state marks**, under the same legend and channel-
declaration discipline a lens obeys (RFC9-26), never as body-colour ramp,
height, heat, footprint band, or edge weight. Were an overlay free to bind
a measured channel, a lens-bound measured encoding and an overlay-bound
measured encoding would run simultaneously and the reader could not
attribute which channel carries which meaning.

**RFC9-32.** **V0 ships:** primary lenses **Architecture** ("what is this
made of and how does it hang together") and **Verification** ("what is
proven here, and how stale is the proof" — no evidence renders Unknown,
never failure and never success); always-available overlays
**work/construction** (scheduler state via its typed adapter; "scaffolding
is never proof the implementation satisfies intent" — completed work
removes scaffolding, it never turns anything green [Observed: vision.md,
Thesis]) and **freshness/staleness** [Observed: SDR-20]. Work/construction
qualifies as an overlay **not** because scheduler state is epistemic — it
is execution-plane fact (RFC1-22) — but because it renders as
**categorical state marks** (scaffolding present/absent and its declared
work state) and binds no measured-magnitude channel, per RFC9-31.
Scaffolding density by open-work-item count would be a measured binding
and is therefore forbidden to an overlay.

The declared work state is consumed **verbatim from RFC 0008, and it is two
orthogonal fields, not one** (RFC8-12; RFC8-28; RFC 0008 §5). The overlay
consumes and renders both:

- the **normalized work state** — RFC8-12/13's closed vocabulary, whose
  values are partitioned into live states, a terminal state, and
  **state-local absence values**. The overlay renders each value as itself:
  an absence value is **never folded into an Unknown aggregate**, never
  counted among RFC2-24 Unknown reasons, and never rendered as scaffolding
  absent — "no work state could be determined" and "no work is scheduled
  here" are different facts, and a district that renders them alike has
  manufactured the second from the first;
- the **RFC2-18 chain state** — `merged`, `reconciliation-pending`,
  `reconciled@E`, `unsatisfied`, `contradiction-raised`, `Unknown(reason)` —
  carried on every element and every aggregate that carries a normalized
  state. **RFC2-17's word reservation binds this overlay**: *reconciled at E
  with evidence*, *merged, not yet evaluated*, *evaluated and unsatisfied*,
  and *evaluated, contradiction raised* are four answers and **never share a
  mark, a mark's color, a count, or a legend entry** (RFC8-28); an
  `unsatisfied` mark and a `contradiction-raised` mark are never merged into
  one, since one routes to a gap and the other to owner adjudication alone.
  A district rendering normalized `merged` while dropping the chain state
  has shown scaffolding removed and concealed that nothing was reconciled —
  the closure fallacy at map scale (RFC8-30). **Staging:** per RFC8-29 the
  verdict-bearing outcomes (`reconciled@E`, `unsatisfied`,
  `contradiction-raised`) are not produced at V0, where the field carries
  `merged`, `reconciliation-pending` and `Unknown(reason)` only; the overlay
  binds on all of them regardless, so the V1 computation lands on a surface
  that already renders its outcomes distinctly rather than one being widened
  to accept them.

Neither field's vocabulary is fixed by this clause: the overlay consumes
whatever values each field currently carries, and a value it cannot render
is a defect here, never grounds to fold that value into a neighbouring one
(RFC 0008 §5). [Inferred — composition of RFC 0008's two-field handoff with
RFC6-6's rule that non-claim absence values are separately counted, RFC2-17's
reservation, and RFC9-43's aggregate-composition obligation.]

**RFC9-33.** **Staging:** **Change/churn** is the next lens after V0
(VCS-history-sourced, window always rendered, reduced fidelity labelled
per RFC4-11/24). **Risk** and **Runtime** are later: Risk requires a
policy-declared composite — an undeclared risk heatmap is inference
wearing a deterministic costume and the most seductive VIS-7 violation;
Runtime is hard-gated by SEC-3 through RFC 0005's execution profiles and
by an evidence class for captured traces — until then flow paths render
explicitly unmeasured [Observed: SDR-20; SEC-3].

**RFC9-34.** No lens may synthesize data to look complete: a lens whose
inputs are absent for a region renders that region in the reserved Unknown
treatment with its reason — a lens never narrows the entity set (that is a
filter, disclosed as one per RFC6-16).

**RFC9-35.** Adding a lens is a contract act: a new lens ships with its
channel declarations (RFC9-26), its Unknown behavior, its legend, and its
tabular equivalent (§3.12) in the same increment — never as a
3D-only skin.

**The promotion predicate — one rule, not a per-kind enumeration** *(History: minted
as clause text at rev7 review 9, finding F9; previously stated only as §8
answer annotations to B12(c)/B17)*: for **lenses, analytical planes, and
profile relations alike**, personal definition and use is free (VIS-6
exception (a) territory — it affects no truth, work, or status), and
**promotion to a named, governed, versioned artifact others can select is
an owner governance act honored only under RFC3-16(a)** — whether or not
the promoted thing binds a registered channel or mints a relation. A
promotion that registers no channel and adds no relation does not thereby
escape the act: the predicate rides on *promotion itself*, so nothing
reaches shared, selectable status through accretion.

### 3.9 Scene profiles: City V0, Factory later (SDR-19)

**RFC9-36.** **City is the required V0 scene profile.** **Factory is a
named later profile over the same graph and the same truth** — a second
emphasis (dynamics at the same addresses, so spatial memory transfers),
never a second semantic model. All invariants here — geography, palette,
legend, evidence paths, equivalence, counting — bind every profile
identically. Factory remains named and sequenced so it cannot be quietly
dropped. [Observed: SDR-19.]

**RFC9-37.** Factory's specific honesty obligations, bound now so its
later contract cannot relax them: the capture window renders at all times;
motion stops and marks when its source stales (continuing motion reads as
liveness); an unmeasured factory renders visibly unmeasured, never as a
calm, orderly, working one; **no flow is ever synthesized for
illustration**; live views, when they exist under the fleet-observability
mandate, never contribute to status claims [Observed: vision.md].

### 3.10 Scenarios and time

**RFC9-38.** Every scene names its evaluation — (source snapshot, as-of
instant) — on the surface, not in a menu; time is an explicit input, never
ambient [Observed: architecture.md]. A scene rendering an evaluation of a
non-default snapshot (a branch or PR tree) is Observed truth *about that
snapshot* and renders a persistent non-default marker. Between-evaluation
motion is a labelled transition; no interpolated frame is a claim; time
travel is between identified evaluations only, and gaps look like gaps.
A later as-of instant may only degrade a claim (RFC2-4); a building never
visibly decays by wall clock. **Subject to RFC9-41:** rendering motion
across *superseded* evaluations is map rendering of historical state —
constitutionally in scope (doctrine amendment D1, adopted), but its concrete
interaction design is the unapproved candidate bundle RFC9-41 holds. Until
the owner approves that design, this clause governs motion between
*non-superseded* evaluations of different snapshots only, and the map offers historical
access through the drawer. Read alone, this clause licenses no particular
historical rendering design.

**RFC9-39.** **Base and intended.** The base scene is the base graph
at the selected evaluation. The **approved-intent scene** renders adopted
declarations — the kernel's Desired/intended *state* plane (RFC1-22),
named in the kernel's own vocabulary per RFC9-1 — against observed state;
base-vs-intended comparison renders three visible sets —
present-and-intended, present-and-unintended, intended-and-absent — the
last **as absence at V0, never as gap objects** [Observed: v1.md, V0/V1
boundary]. ("Target" is not used for this scene: the kernel's words are
*desired* and *intended*, and RFC2-16 already spends "declared **target
scope**" on the scope over which convergence is claimed.)

**The approved-intent scene carries scenario context `Base`** *(RFC6-24's
context — History: renamed from `Current` at the rev7 rework — directive
item B6, not owner decision B6)* — it is a
comparison *within* Base, **not a fourth context**. RFC6-24 enumerates
exactly three contexts and requires exactly one on every selection, and this
scene selects no proposal set (which would make it Proposed) and no
superseded evaluation (which would make it Historical): it compares the base
graph at the selected evaluation against declarations that are *already
adopted*, i.e. against currently approved intent. The context RFC6-25
propagates into this scene's URLs, cross-surface synchronizations, and query
answers is therefore `base`, and **no implementation may mint a fourth
context value for it** — RFC6-24's enumeration is exact, and a minted value
would travel outside it into endpoint answers by RFC6-25's own machinery.
RFC9-12 is not engaged: the scene re-marks home geography and moves no
entity — intended-and-absent renders as a marked vacancy at its declared
site, never as a re-layout — and a rendering that *did* move entities would
by definition be an analytical-plane or scenario switch and would have to be
labelled as one. [Inferred — the only reading consistent with RFC6-24's
exact enumeration; surfaced because the scene's context was previously
unstated.]

**Rendered as absence is a positive obligation, not the omission of one.**
An intended-and-absent capability, block, or plot renders as a **marked,
labelled, expandable vacancy** carrying its RFC2-24 reason and that
reason's resolution route — **never negative space, never vacant ground**.
RFC9-27's earned-emptiness rule binds this scene at every level of the
hierarchy, and RFC9-22 already binds the identical sentence for
unconsented repositories ("never empty ground, which reads as 'nothing
there'"); an unmarked gap inside the approved-intent scene is that same
failure, located where the largest piece of missing work is, and a reader
scanning it would conclude the intent is substantially met. What V0 defers
is the **gap object** — a first-class, selectable, trackable entity for
the missing thing — not the marker.

An intended state whose approved inputs contradict renders the
contradicted region Unknown with its adjudication route — never a resolved
intent.

**RFC9-40.** **Proposed.** Proposed scenes obey RFC1-27 and RFC6-24:
the kernel refuses to union proposals in one exclusivity group or of
undeclared compatibility — the honest render is *N candidate futures*,
selectable one at a time; **proposed structure never looks like existing
structure** in any profile at any zoom; every proposed scene names its
base on-surface (default: the observed base graph; proposal-over-intended only as
an explicitly labelled stacked scenario); structurally divergent proposals
compare side-by-side in their own address spaces with shared declared
districts as registration anchors — their union is never one scene.
A deterministically computed merge projection is a derived projection in
the proposed treatment, never solid: determinism of a computation is not
evidence of existence.

**RFC9-41.** **Historical.** *(History: rewritten at the rev7 rework: the original
conditioned everything on a then-pending doctrine amendment; D1 is adopted,
and the two things the original bundled — constitutional scope and concrete
interaction design — are now stated separately.)* Drawer and query access to
superseded evaluations rests on VIS-6, exception (b), and needs no doctrine
change (RFC6-24). **Rendering historical state in the map is within `map/`'s
constitutional scope** — unconditionally, by adopted owner amendment D1
[Observed: architecture.md as amended]. What binds when historical scenes
render: they render Observed + superseded (ghosted or otherwise visibly
distinct from current, with the superseding evaluation named), staleness on
the primary surface, and retention/renderable-evaluation selection per the
quality/evidence policy.

**Candidate design, non-binding.** The concrete interaction bundle the
original clause described — ghost-step opacity for superseded structure,
milestone scenes, the timeline scrubber over identified evaluations — is
**candidate design only**. D1's adoption did not activate it and nothing in
this RFC does; it becomes binding only through its own later owner approval
(as a craft/OpenSpec candidate after RFC acceptance). Until then the map
offers historical access through the drawer, and any historical scene an
implementation does render must satisfy the binding sentence above without
claiming the candidate bundle is contract. [Observed: D1; the candidate
bundle Inferred and explicitly non-binding.]

### 3.11 Aggregation, semantic zoom, and unmapped code

**RFC9-42.** **LOD epistemic invariance.** Zoom and level-of-detail may
reduce geometric fidelity and label density freely; they may never change
a fact's epistemic state — only its aggregation. The epistemic treatment
set (texture class, plate presence, proposed-vs-existing distinction) is
LOD-invariant, surviving by substitution: where per-entity treatment is
illegible, an Unknown or proposed *region* renders as an aggregate in the
same reserved vocabulary ("Unknown ×40", a wireframed proposed district) —
never as ordinary solid mass. Zoom never fabricates detail: an unavailable
interior renders Unknown, not generic geometry. [Inferred — VIS-1 honest
simplification, operationalized.]

**RFC9-43.** Every aggregate discloses its membership count and epistemic
composition and supports expansion to members (RFC6-17; SDR-27). **The
disclosed composition is the full RFC9-46 equivalence tuple** — per-label,
per-tier, per-Unknown-reason and per-freshness-state counts **and sibling
surface states** — the tier counts covering all six of RFC2-25's tiers
(`gate-backed`, `report-fact`, `asserted-by-worker`, `reduced-fidelity`,
`declared-only`, `suspended`), and the sibling surface states being the three
RFC2-25 places deliberately outside the registry (*dismissed by
decision*, *unadopted draft*, *editorial draft*, per RFC6-14) — never label
and Unknown reason alone. An aggregate obligation
narrower than the equivalence obligation over the very same objects would
let `reduced-fidelity`, `asserted-by-worker`, `stale` and *dismissed by
decision* evaporate at
the district layer, and those are precisely the labels doctrine spends
clauses making unloseable [Observed: SDR-33; trust-and-evidence.md,
Staleness — "staleness must be visible on the primary surface, not buried
in drill-down"]. A district disclosing "Observed ×30, Unknown ×10" while
all 30 are `reduced-fidelity`, 12 are stale and 3 are dismissed by
decision reads as a well-evidenced, current district to a human and to an
agent querying the same aggregate under RFC6-13. `asserted-by-worker` is the
same failure one label over: an aggregate disclosing "Inferred ×8" without
disclosing that all eight are worker assertions with no retained artifact
(RFC2-25) has laundered the weakest tier the registry carries into an
ordinary Inferred count. RFC6-17 binds the same enumeration at the
foundation layer (§5, defect 4); the two are deliberately identical, and any
divergence between them is a defect to close rather than a surface-local
variation.

**Aggregated measured channels carry their Unknown contribution — RFC9-27
at scale.** Where an aggregate renders a lens-bound measured channel over
epistemically mixed members, the aggregate must carry its Unknown
contribution in **the same reserved vocabulary the per-element rule uses**:
a **marked stub fraction**, a **hatched band**, or a **refusal to render a
magnitude at all**. The aggregate's per-zoom legend must state which of the
three it does. Aggregating over only the members that have values, and
letting the rest vanish, is Unknown rendered as zero at the map's most
legible scale — SDR-6 and RFC2-23's "no aggregate silently treats absent
as 0", reached without breaking any other clause: a district of 2 measured
and 38 Unknown buildings renders short, RFC9-42 does not fire because the
district is not *wholly* Unknown, the composition panel honestly reports
"Unknown ×38" on expansion, and the reader — who is reading the scene, not
the panel — concludes the district is small. **At V0 this is the normal
case, not an edge case:** v1.md fixes the proving ground as
predominantly-Unknown projects, so nearly every district is epistemically
mixed, and an aggregate rule that only bites on wholly-Unknown regions
would bite almost nowhere.

Aggregate legends are per-zoom-level, because a district-level aggregate is
not the same measure as a building-level reading.

**RFC9-44.** **The unmapped district (SDR-25).** Unmapped code is
**aggregated by default** — with count, RFC2-24 reasons, and expandable
detail — and **never disappears**: no filter default, LOD step, lens, or
profile may drop it. Its entities carry a **"path-derived placement (may
move on refactor)"** marker (RFC9-14 tier 2): what is path-derived and
unstable is the *arrangement*, never the identity. Code-element identity
is adapter-minted and stable — explicitly "not path-only" (RFC1-5;
RFC4-12) — so selection references and URLs into the unmapped district
survive refactor under RFC6-1's no-surface-local-handle rule and RFC6-9's
rename stability. A marker asserting path-derived *identity* would break
both and dangle every bookmark into this district, which matters most
precisely here. On an undeclared proving-ground
project it will be most of the map — the correct output — and its primary
affordance routes to V0's first-pass drafting of declarations for owner
sign-off [Observed: v1.md; SDR-25].

**RFC9-45.** **The grey map is diagnosis, not breakage.** At 90% Unknown
the map must remain legible and useful: Unknown regions aggregate with
RFC2-24 reasons and resolution routes rendered verbatim. The acceptance
posture is v1.md's comprehension test (within-reader, recorded
walkthrough, owner-judged); its first task on an undeclared project is
the grey-map first impression. Binding failure signature: a reader
stating something false that the map supported is a trust-floor incident,
release-blocking. Frame rate, entity count, polish, and demo reaction are
explicitly non-criteria. [Observed: v1.md; SDR §2; signature form
Inferred.]

**Three artifacts, not one.** *(History: separated at the rev7 rework, blocker A4:
the original conflated the record of the walkthrough, the judgment about it,
and the authority that makes the judgment gate a release.)*

1. The **walkthrough execution record** — a `kernel-recorded` durable fact
   (RFC3-2) in **`.syzygy/governance/records/`** (RFC3-15) minted when a
   walkthrough runs: the project and surface walked, the participants, the
   start/end or capture identity, the submission identity, and what was on
   the screen — the **evaluation** walked ((source snapshot, as-of instant),
   RFC9-38), the **layout version and layout baseline** in force (RFC9-14(a),
   RFC9-18), the **scenario context** and **active lens** (RFC6-24; RFC9-31),
   and the **declared filter scope**, including any RFC9-49 narrowing.
   *(The screen-content list was added after review 8's ML-R10: a name and a
   rationale make a false pass **attributable**, not **findable** —
   findability requires knowing what was rendered. Without it, "was the
   misleading rendering present at test time, or introduced by the version
   bump since?" has no answer.)* Every listed item is a governed or
   snapshot-identified fact this RFC already requires the *scene* to name.
   The execution record asserts only that a walkthrough occurred as
   described; it judges nothing and authorizes nothing.
2. The **walkthrough judgment** — an attributed human adjudication recorded
   in **`.syzygy/governance/decisions/`** (RFC3-15: a decision is a warrant,
   never evidence), naming the judging party, the outcome (**pass / fail /
   insufficient-to-judge**), the rationale, the execution record(s) judged,
   the scope the judgment covers, its instant, and any earlier judgment it
   supersedes. *(Attribution ruled at acceptance by owner decision B12(b),
   escalating v1.md's success test to a gate.)* The judgment is honored
   **only under RFC3-16(a)** — it is an adjudication Decision in
   `decisions/`, squarely inside that predicate's example list, and the
   home establishes durability, never authorship: an owner judgment a
   fleet worker could commit is not an owner judgment. An unattributed or
   unreasoned verdict is not a lawful gate outcome in either direction — a
   false pass must be findable afterward, and it is only findable with a
   name and reasoning attached. The judgment is **never rendered Observed**
   and is **never evidence about the project**: it is a recorded human
   judgment about the surface, and no claim instance, gate outcome, or
   reconciliation verdict may consume it as project implementation evidence.
3. The **release policy** — an owner-approved, authorization-bearing policy
   under **`.syzygy/governance/policies/`** (honored only under RFC3-16(a))
   that says whether a walkthrough is required for a given release class,
   **which judgment classes qualify and who may judge**, what freshness and
   scope the judgment must have, and that a lawful qualifying pass clears
   the gate. **Release authority comes from this adopted policy — never
   from the kernel having stored a verdict.** **Absence of an adopted
   policy is not a permissive default** *(History: pinned at rev7 review 9, finding
   F2, matching RFC2-13's undeclared-sweep posture)*: with no adopted —
   or no RFC3-16(a)-verifiable — release policy, **owner decision B12(b)
   binds directly**: the comprehension walkthrough is required at every
   release milestone, the owner judges, and release requires a lawful
   qualifying pass. An adopted policy **configures and may narrow** that
   default (release classes, qualifying judgment classes, freshness,
   scope); only an explicit, RFC3-16(a)-verified owner act may waive the
   walkthrough for a release class, and no policy silence ever does.

Orrery **references** the execution record and judgment (drawer-linkable per
RFC6-19); it owns neither, and nothing gate-bearing lives under
`.syzygy/map/**`.

**An unlawful outcome does not clear the gate.** *(History: added after review 8's
ML-R11, which found the clause defining what an unlawful verdict *is not* and
never saying what the release state then *is* — exploitable precisely in the
direction with teeth, since an unattributed **fail** would otherwise be no
lawful fail at all.)* The gate is **fail-closed, like every other closure on
this surface** (RFC9-26's registry, RFC9-18's unverified entry, RFC9-27's
absent coverage record; and v1.md for this very test: "absent its artifact, a
test renders Unknown, never met"). Concretely: **where the walkthrough is
required — by the adopted release policy, or by B12(b)'s default when no
policy is adopted — release requires a lawful qualifying pass.** An unattributed or unreasoned verdict — in either direction — is not
a lawful pass, so it blocks release exactly as a fail does. It is recorded as
**verdict-unlawful** — a state of the judgment record, *not* an RFC2-24
Unknown reason (that vocabulary is closed at twelve and governs claims about
the project, not outcomes of Syzygy's own release gates) — rather than
converted into a fail, because the walkthrough's actual outcome is not thereby
known and recording a fail would assert something no one judged. **A judgment
whose owner-act provenance does not verify under RFC3-16(a) is unlawful in
exactly the same way** — attributed and reasoned prose a fleet worker could
commit clears nothing — and is recorded as **verdict-unlawful** likewise.
Absence of an execution record, absence of a judgment, and a judgment whose
scope or freshness the policy rejects are likewise not a pass. In every one
of these cases the walkthrough test itself renders **Unknown, never met**
(v1.md's own words), the gate stays closed, and the remedy is to re-run the
walkthrough and record it lawfully. *(This paragraph and RFC7-31 state one
protocol: defective verdict → recorded `verdict-unlawful` on the judgment
record, test renders Unknown-never-met, gate fail-closed — the same outcome
on both surfaces.)*

### 3.12 Non-3D equivalence and accessibility (SDR-27)

**RFC9-46.** Non-3D views (2D, tabular) are **co-equal product surfaces**
— the precision, debugging, and assistive-technology paths — not derived
exports. For one (evaluation, scenario context, lens, declared filter
scope), the 3D scene and the non-3D view are equivalent per RFC6-22/23:
same entity set, same edges, same epistemic states (label + tier + reason
+ freshness **and sibling surface states**), same counts, same evidence
links, same scenario context, and — wherever the work/construction overlay
is active — **both work-state fields: the normalized work state and the
RFC2-18 chain state** (RFC9-32; RFC8-12/8-28). A tabular view that carries
the normalized state and drops the chain state is not a finer-detail
difference under RFC6-23; it answers the reconciliation question differently
from the scene, which is precisely the disagreement RFC6-23 forbids. Non-3D
views may expose finer detail than an aggregated scene — a disclosed
aggregation difference, never a contradiction (RFC6-23).

**Added to the tuple at acceptance: the positional-expression state and the
backlog partitions.** *(Review 8's ML-R6 — the B12(a) amendment added exactly
the class of surface-local, reader-actionable field the maintenance note below
predicts will be lost, and did not add it here. The RFC had run its own
predicted failure.)* The tuple additionally carries, for the same
(evaluation, scenario context, lens, declared filter scope):

- the **RFC9-9(b) positional-expression state** — `honored` / `not-honored` /
  `unknown` — for every rendered `declared-dependency` edge; and
- **both RFC9-15(b) part 4 partition counts**, refresh-clearable and
  structurally unhonorable, separately (the unpartitioned total is not a
  lawful rendering on either surface).

**These are not statements about pixels, and the table does not compute them
from its own geometry.** The state is a function of the layout input tuple
(RFC9-14) and is evaluated against the **recorded base layout** (RFC2-6),
which is a governed artifact both surfaces read. A tabular view therefore has
everything it needs, and an implementation that derives the count from a
table's non-existent geography and reports `0` has not found a limit of the
tabular surface — it has read the wrong artifact. Scene says 12 and table says
0 over the same declared scope is an RFC6-23 release-blocking disagreement,
and it is now inside the gate rather than outside it.

*Why this one matters beyond bookkeeping:* the tabular view is RFC9-48's
designated screen-reader surface. Without these fields a screen-reader user
could not learn from **any** surface available to them that the layout is
twelve declarations behind and a refresh is due — while a sighted reader sees
it prominently. That is a parity failure, not a detail difference.

[**A maintenance note, not a ruling.** This tuple is a **hand-maintained
enumeration**, not a list derived from anything: it restates RFC6-22's
cross-surface tuple and then names, item by item, the surface-local fields
this surface adds — the work-state pair being the current instance. Whether
an equivalence tuple should enumerate surface-local fields *in general*, or
be defined so they cross automatically, is **unresolved and belongs to
RFC6-22 at the foundation layer**, not to this clause. Until it is resolved,
anyone adding a surface-local field that a reader could act on must add it
here explicitly; an omission does not fail loudly anywhere.]

**RFC9-47.** **The equivalence gate is a release check** for Syzygy's own
releases, alongside: layout determinism (two runs, one evaluation,
identical base layout); refactor stability (mapping-preserving refactor
moves nothing); append-stability (RFC9-15, fixture-tested); no
double-counting (RFC9-21, fixture-tested); legend completeness and
registry-generated legend text (RFC9-26); Unknown coverage (no Unknown
renders green or absent, every reason rendered, **including the aggregate
form of RFC9-27 — no aggregated measured channel renders without its
Unknown contribution, RFC9-43**); empty-plot coverage records (RFC9-27, at
every level of the hierarchy and in the approved-intent and proposed
scenes); **proposed-scene fidelity** (RFC9-40: the exclusivity-group union
refusal — no scene unions proposals in one exclusivity group or of
undeclared compatibility, the honest render being *N candidate futures*
selectable one at a time; and **proposed structure never looks like existing
structure in any profile at any zoom**, checked per profile and per zoom
step, since a proposed district that reads as built is the most seductive
lie this surface can tell); **work-state two-field consumption** (RFC9-32:
every element and every aggregate that carries a normalized work state
carries its RFC2-18 chain state beside it — no rendering, filter, count,
legend entry, or tabular row shows one in place of the other; and
`unsatisfied` and `contradiction-raised` never share a mark, a mark's color,
a count, or a legend entry with each other, with `merged`, or with
`reconciled@E`, per RFC2-17's word reservation and RFC8-28 — run against a
fixture carrying **every chain outcome the release can produce**, co-located
on one district, since a gate exercised only over
merged-not-yet-evaluated data passes vacuously; per RFC8-29 that is
`merged`, `reconciliation-pending` and `Unknown(reason)` at V0, the
verdict-bearing outcomes entering the fixture with the V1 computation that
first produces them); **declared-vs-observed relation separation** (RFC9-9:
every rendered profile relation legends as itself with its profile and state
class named — the registry side of this is already covered by legend
completeness above — and no declared project-scope edge shares a mark, a
channel treatment, a legend entry, or a count with an observed `depends_on`
edge, RFC1-25's anti-conflation rule run as a rendering check; exercised over
a portfolio fixture carrying both an observed intra-project dependency and a
declared `depends-on` edge, since a single-project fixture cannot
reach it); LOD
epistemic invariance (RFC9-42); link
resolution for every map entity; secret exclusion (RFC9-29, including the minimum-
aggregation granularity bound); **the masquerade check** (no view binds
position or proximity to a metric without the analytical-plane marker —
RFC9-11 makes this a violation identical in class to an unlegended
channel, VIS-7); **non-visual parity** (RFC9-48: full keyboard navigation
of every action, tabular equivalent as the screen-reader surface, textual
epistemic labels for every state, reduced-motion honored — accessibility
is a truth requirement, and keyboard navigation is V0 scope per v1.md);
**no ambient motion** (RFC9-50); **encoding explainability** (RFC9-3:
every rendered encoding traceable to an identified artifact, with the
RFC9-26 fail-closed rule — no channel renders without a registry entry).

**Six layout obligations added at acceptance.** *(Review 8's ML-R9 — the
B12(a)/B12(b)/A3 amendments created checkable obligations and routed none of
them to the only list that gets tested. §4 case 3a already named four of them
as violation cases, which made the omission sharper, not softer.)*

- **Order-independence** (RFC9-15(b) part 3): the same layout input tuple
  presented in any order yields identical coordinates. **The existing "two
  runs, one evaluation" determinism check does not cover this** — two runs
  inside one implementation share an insertion order by construction, so the
  natural implementation (iterate declarations in adoption order, pack
  greedily) passes every gate on this list and fails only after release, when
  a second implementation or a re-ordered cache rebuild disagrees. The check
  must permute the declaration set, not repeat it.
- **Baseline recording** (RFC9-14(a)): the layout baseline exists as an
  identified artifact and the recorded base layout reproduces from
  (declaration set, baseline, version). A base layout that is checkable but
  not reproducible fails here.
- **Full-not-scoped regeneration** (part 2): a refresh repositions every
  district; a scoped refresh is rejected, not honored partially.
- **Not-honored rendering** (part 1, RFC9-9(b)): an unhonorable declared
  relatedness edge renders `not-honored` — never as honored, never Unknown,
  never nothing — with its registry entry present and its Unknown value
  exercised by an edge with an unplaced endpoint.
- **Backlog partitioning** (part 4): both counts render separately and an
  unpartitioned total does not render, on both surfaces (RFC9-46).
- **The carve-out demonstration is actually run** (RFC9-16(d)): a layout
  version shipped under the note-only route carries a recorded
  layout-equivalence check result. An asserted equivalence fails the gate.

**Also gated: the residual-adjacency legend line** (RFC9-9(a)) — the
position/proximity registry entry declares all three readings, and residual
placement produces no enclosure, shared boundary, plinth or common ground
plane that mimics declared containment. This one is partly a judged check
rather than a computed one, and is named here rather than omitted for that
reason.

**And: stale-layout personal state** (RFC9-13(a)) — a saved camera home
carrying an older layout version does not restore silently; run against a
fixture that bumps the version between save and restore, since a
single-version fixture cannot reach the failure.

**And: the walkthrough artifacts' completeness and the fail-closed gate**
(RFC9-45) — an execution record naming no evaluation, layout version,
baseline, scenario context, lens or filter scope is not a lawful record; an
unattributed or unreasoned judgment blocks release rather than clearing it;
and a pass may clear release only through the adopted release policy, never
because a verdict is stored.

[Inferred — the checkable form of the trust floor for this surface; the
gates' place in the release process is craft-and-care material. This list
is what craft-and-care consumes, so an obligation absent from it is tested
nowhere. That sentence has now been demonstrated twice: once by review 8's
ML-R9 finding six absences, and once by ML-R6 finding the equivalence tuple
short of two fields the gate then could not see.]

**RFC9-47(a) — The registry maintains itself or it is wrong.** *(History: added at
the rev7 rework — directive item B4 of
`_bootstrap/rfc-phase/REV7-REWORK-DIRECTIVE.md`, not owner decision B4:
the list above has already been caught incomplete
twice, each time by an expensive fresh-context review; a hand-maintained
enumeration whose completeness is checked only by luck is not a release
gate, it is a hope.)*

Two obligations make the list self-maintaining:

1. **The same-logical-change invariant.** Any amendment to this RFC — or to
   a contract this RFC consumes — that **creates, removes, or changes a
   release-blocking obligation on this surface** must update this clause's
   list **in the same logical change** (the same amendment act, reviewed and
   adopted together). An amendment that creates a checkable obligation and
   does not route it here is an incomplete amendment; the review that
   accepts it must treat the omission as a defect of the amendment, not a
   later housekeeping task. The same rule binds the craft-and-care release
   checklist that consumes this list.
2. **The mechanical validation contract.** The release process must include
   a **registry-completeness check**: a mechanical or checklist pass that
   walks every clause of this RFC (and every consumed cross-RFC gate this
   list cites) whose text names a release-blocking or fixture-tested
   obligation, and verifies each is either present in this list or
   explicitly recorded as out-of-scope with a reason. The check's form
   (script, structured checklist, review template) is an
   implementation-slice choice; what binds is that it exists, runs at each
   release, and its result is recorded. A release that cannot show the
   completeness-check result fails this gate exactly as it would fail a
   missing fixture.

[Inferred — the maintenance contract; Observed — the two demonstrated
omissions that motivate it.]

**RFC9-48.** **Non-visual parity.** Every distinction the scene renders
has a non-visual path: full keyboard navigation of every action —
traverse, select, zoom, lens, analytical plane, scenario, drawer, filter —
without
pointer or camera; the tabular equivalent as the screen-reader surface;
textual epistemic labels for every state (RFC9-27's two-carrier rule);
reduced-motion honored with no loss of meaning; text contrast maintained
in every profile. Accessibility here is a truth requirement: a reader who
cannot perceive "Unknown" is being shown comprehensible fiction.

### 3.13 Performance as a contract obligation

**RFC9-49.** Responsiveness budgets are declared, per scene class, in the
surface's spec (values are craft material; the obligation to declare is
not), and **the budget values must exist before V0 ships** — the same
same-increment obligation RFC9-35 binds for lenses, for the same reason:
an undeclared budget is an obligation that never becomes checkable. When a
budget cannot be met, the surface degrades **only by narrowing an
explicitly declared scope, rendered as narrowed** — in the 3D scene and
the non-3D equivalent identically, so the equivalence gate is evaluated
over the same narrowed scope. **The narrowing is a declared filter under
RFC6-16 and travels in the answer's envelope**, recorded with the answer:
the narrowing scopes available to a scene class are declared in the
surface's spec beside that class's budget, the surface may select only
among those declared scopes, and the selected scope is named in the answer
it produces. It is never a render-time scope improvised from device
capability. Were it render-time, two readers — or the owner and an agent consuming the
same selection under RFC6-13's one-truth-two-consumers rule — would
receive different entity sets for the same URL at the same evaluation,
each honestly labelled, with no clause naming the divergence (RFC6-3
covers evaluation skew, not scope skew). Silent decimation, silent entity
dropping, and stripping epistemic carriers for speed are forbidden; the
permitted currency is VIS-1 rank 4, never rank 1 [Observed: vision.md,
Performance]. Truth is never purchased with frame rate.

### 3.14 Motion (SDR-26)

**RFC9-50.** **No ambient motion at V0.** Motion is reserved for labelled
transitions, explicitly selected flows, and camera movement [Observed:
SDR-26]. Any later motion (Factory, selected replay) obeys RFC9-37:
capture window visible, stops-and-marks on staleness, never synthesized,
never the sole carrier of any state, reduced-motion honored.

**RFC9-51.** Illumination and highlight are interaction state — selection,
search hits, cross-surface highlight (RFC6-3) — personal, never
truth-bearing, and legended as such. Binding light to a metric would imply
liveness the evidence may not support. [Inferred]

### 3.15 Authority boundary at the OpenSpec seam (binding phase rule)

**RFC9-52 — This contract schedules nothing.** *(History: added at the rev8 rework,
directive item 7.)* This RFC fixes the semantics of the map surface; it is
**not a specification of record from which implementation work may be
scheduled**. No implementation work for **user-observable Orrery behavior**
may be scheduled solely from this RFC: before implementation, every
observable consequence of RFC9-1…RFC9-51 must either **map to an approved
OpenSpec requirement or scenario** in the governance root's `openspec/**`
plane, or carry an **explicit, reviewed N/A judgment** recording why that
consequence needs no requirement. The surface-specification phase must
produce, as a deliverable, a **clause-to-requirement coverage matrix** for
this RFC — every clause mapped to requirement identities or to its reviewed
N/A — and that matrix is review material, never authority. This clause
creates no OpenSpec content now (none may exist during bootstrap); it binds
the phase boundary so RFC prose is never quietly treated as an
implementable behavioral spec.

---

## 4. Violation cases

Each is recognizable, not rhetorical:

1. *(RFC9-4/17)* A mapping-preserving refactor reshuffles a district; a
   metric change or lens switch moves a building.
2. *(RFC9-5/7)* An inferred mapping places a building; a drafted
   capability anchors a district; unmapped code renders inside its
   "probable" capability.
3. *(RFC9-11/16)* A layout clustered by **observed** coupling renders
   without the analytical-plane marker and readers memorize it as home
   (declared relatedness under RFC9-9 reading 2 is lawful in home
   geography; observed coupling is not, and the two are distinguishable
   only because RFC1-25(b) keeps the relations separate); a
   layout-version upgrade re-lays the map with no reorganisation event or
   no recorded rationale; a version bump claims the RFC9-16(d)
   position-preserving carve-out without running the demonstration; a
   district that has outgrown its reserved extent is re-laid out under
   trigger (d).
3a. *(RFC9-15(b))* A newly declared relatedness edge relocates an existing
   district; a refresh regenerates some zones and not others; two
   implementations given the same declaration set in different insertion
   orders produce different coordinates; a relatedness edge the layout
   could not honor renders as honored, as an Unknown, or as nothing at
   all, rather than as **not-honored**; the not-honored backlog is not
   surfaced, leaving the owner no signal that a refresh is due.
4. *(RFC9-20/21)* A renderer tie-breaks an undeclared shared component
   into a district; a precedence rule resolves two co-unsatisfiable
   declared placements instead of rendering the Contradiction; district
   totals silently double-count, or a project total sums districts; a
   shared contribution is counted into several rendered aggregates with no
   disclosure on any of them.
5. *(RFC9-22)* Geography partitioned by repository; an unconsented
   repository rendered as empty ground.
6. *(RFC9-24/27/39/43)* An Unknown region rendered green because its
   neighbors are; a proposed component rendered solid; an Unknown rendered
   zero-height or absent; an empty plot, block, or district with no
   coverage record; a district aggregate whose measured channel renders
   short because its Unknown members contributed nothing to it; an
   intended-and-absent capability rendered as vacant ground in the
   approved-intent scene.
7. *(RFC9-26/28)* An unlegended channel carries meaning; legend text
   hand-authored per channel drifts from the palette registry; a heat
   layer renders without its window; height changes meaning with no
   legend change.
8. *(RFC9-33/37)* A risk heatmap from an undeclared composite; a runtime
   flow animating with no captured trace (SEC-3); motion continuing from
   a stale source.
9. *(RFC9-38/40/41)* A scene with no visible evaluation identity; two
   exclusivity-grouped proposals merged into one future; a computed merge
   rendered solid; the historical interaction bundle (ghost steps,
   milestone scenes, scrubber) shipped as if binding while it remains an
   unapproved candidate design — or a claim that doctrine amendment D1's
   adoption activated it by itself.
10. *(RFC9-42/43/44)* Zoomed-out Unknown regions solidify into ordinary
    mass; a district aggregate discloses label and Unknown reason while
    dropping tier, freshness, and sibling states; the unmapped district
    vanishes under a default filter; its entities are marked as carrying
    path-derived *identities*.
11. *(RFC9-46/49)* Scene and table disagree on a freshness state or
    count; the 3D view silently narrows scope while the table stays
    full-scope.

---

## 5. Integration

**Relies on RFC 0001:** capability identity as the map anchor with
rename/split/merge/retirement semantics (RFC1-10/11/13/14); the four
mapping classes never conflated (RFC1-16); multi-capability edges with
identity-based counting (RFC1-17); state planes — proposed never anchors
(RFC1-22); exclusivity groups (RFC1-27). **Relies on RFC 0002:** the
label + tier + reason + freshness vocabulary rendered verbatim
(RFC2-10/24/25, incl. `declared-only`); degradation-only time (RFC2-4);
suspension visibility (RFC2-14); failure states (RFC2-23). **Relies on
RFC 0003:** `map/` as a schema-versioned governed namespace (RFC3-18);
cache/local boundaries (RFC3-20/21); identity-preserving migration keeps
map anchors resolving (RFC3-23). **Relies on RFC 0004:** code-element
identity continuity (RFC4-12); mapping declaration sites (RFC4-26);
coverage records behind every empty plot (RFC4-27); reduced-fidelity
labeling for churn inputs (RFC4-11/24). **Relies on RFC 0005:** execution
profiles gating every runtime-lens input (RFC5-20…23; SEC-3). **Relies on
RFC 0006:** selection references and cross-surface sync (RFC6-1/2/3);
outcome set incl. retired/never-redirect (RFC6-5/11); the single drawer
(RFC6-18/19); aggregation disclosure (RFC6-17); equivalence (RFC6-22/23);
scenario context (RFC6-24/25).

**Defects found in the foundations (reported, not silently diverged
from):**

1. **~~RFC1-25 has no declared placement relation from Topology entry to
   Capability.~~ DISCHARGED at acceptance — owner decision A7.** RFC1-25
   now carries **`placed_in`** (Topology entry → Capability,
   Desired/declared, minted by a governance artifact), added by owner
   amendment rather than by extending `part_of` — whose own rule confines
   it to a single authority's hierarchy and directs cross-authority
   nesting to a typed relation. The district/block hierarchy (RFC9-4),
   SDR-22 placement, the shared-infrastructure district (RFC9-19(b)) and
   every "components of capability C" aggregate now rest on a declared
   edge that exists. RFC9-20's rule is unchanged and now enforceable: an
   entry with no `placed_in` edge renders in the unmapped district
   (RFC9-44), never in a placement guessed by a renderer. **§8 q1 is
   answered and marked as such.**

   **The same table also had no *declared dependency* relation — DISCHARGED
   AT ACCEPTANCE BY A6.** *(Marked here after review 8's ML-R13, which found
   this half still standing in the present tense and factually false about
   the amended kernel, while RFC9-9 asserted it had been marked.)*
   `declared-dependency` (Capability→Capability; Topology entry→Topology
   entry, Desired/declared) is now in RFC1-25, recorded at RFC1-25(a). RFC9-9
   reading 2, the honored/not-honored state (RFC9-9(b)) and the RFC9-15(b)
   backlog all rest on it and are all buildable. **§8 q5 is answered and
   marked as such.**

   *As reported, and retained for the trail:* RFC9-9 requires dependency
   edges to render on their own explicit, resolvable edge channel, but at V0
   every dependency edge RFC1-25 then offered was observed (`depends_on`
   code→code, `structurally_related`) or execution-class, and RFC1-26 says
   relations outside the table do not exist at V0. This RFC accordingly
   declined to legend any V0 dependency edge as "declared" (that conflation
   is what SDR-3 forbids) and declined to mint the relation itself, routing
   the gap to acceptance (§8 q5) alongside the placement relation, since both
   were the same closed-vocabulary omission. **That restraint is unchanged
   and still binds:** the relation exists because the *owner* minted it at
   acceptance, not because this RFC took the vocabulary into its own hands,
   and an observed edge is still never legended as declared.

   **Scope, stated precisely because the portfolio profile makes it easy to
   misread:** the (former) omission was at *capability, topology-entry and
   code-element* scope. At **project** scope a declared relation already
   existed — the portfolio profile's `depends-on` (RFC1-7; RFC3-14), with
   `subproject-of`/`contains-project` alongside it — added under RFC1-26's
   second limb rather than minted in RFC1-25's table. RFC9-9 legends those as
   profile relations. The two remain **distinct relations that differ by one
   character**, `depends_on`/`depends-on`/`declared-dependency`, and
   RFC1-25(b)'s twelve-pair anti-conflation invariant is what keeps them
   apart on this surface.
2. **RFC6-22's equivalence enumeration omits sibling surface states and
   scenario context.** — **RESOLVED UPSTREAM 2026-08-01; retained for the
   trail, no longer outstanding.** As reported: RFC6-22 tested label + tier
   + reason + freshness, but *dismissed by decision* and *unadopted draft*
   travel per RFC6-14 and context must travel per RFC6-25, so as literally
   defined the equivalence test would not have caught a scene/table
   disagreement on a dismissal or a context swap. RFC 0006 has since folded
   both in: RFC6-22 now reads "…the same sibling surface states
   (dismissed-by-decision, unadopted-draft — RFC6-14), and the same scenario
   context (RFC6-24) for every presented element." [Observed — RFC6-22 as of
   2026-08-01.] **No RFC 0006 change is outstanding on this item.** Defect 4
   below reported a distinct narrowness in RFC6-17; it does not depend on
   this one, and it has since been closed on its own terms.
3. **RFC6-24's context taxonomy leaves the observed non-default snapshot
   implicit.** — **RESOLVED UPSTREAM 2026-08-01; retained for the trail, no
   longer outstanding.** As reported: a branch/PR-tree evaluation is
   technically "current at that evaluation," but nothing in RFC 0006 obliged
   marking it non-default, and the reader-facing distinction between "the
   project now" and "this branch's truth" carries real misreading risk.
   RFC 0006 has since named the case for all surfaces: RFC6-24's base-context
   bullet (the context then named `Current`, renamed `Base` at the rev7
   rework) now reads that such a context is still that context at that
   evaluation, but **every surface must carry an explicit non-default marker
   naming the revision** — never render as if it were the default branch.
   [Observed — RFC6-24 as of 2026-08-01.] RFC9-38's persistent non-default
   marker is accordingly a surface-local restatement of an upstream
   obligation, not a marker this RFC binds alone. **No RFC 0006 change is
   outstanding on this item.**
4. **RFC6-17's aggregation disclosure is narrower than RFC6-22's
   equivalence tuple over the same objects.** — **RESOLVED UPSTREAM
   2026-08-01; retained for the trail, no longer outstanding.** As reported:
   it required per-label and per-Unknown-reason counts only, so tier
   (any of RFC2-25's six, `asserted-by-worker` and `reduced-fidelity`
   most consequentially),
   freshness, and sibling surface states (*dismissed by decision*,
   *unadopted draft*) could all be dropped at the moment elements merge into
   an aggregate — in a scene, a table, or a machine answer. That is label
   laundering at the aggregate layer, and it defeats doctrine's rule that
   staleness stays visible on the primary surface [Observed: SDR-33;
   trust-and-evidence.md]. RFC6-17 now binds **the full RFC6-22 equivalence
   tuple** — "per-label, per-tier, per-Unknown-reason and per-freshness-state
   counts **and sibling surface states** … never label and Unknown reason
   alone" [Observed — RFC6-17 as of 2026-08-01] — which is exactly what
   RFC9-43 binds for this surface, so the two layers now agree. **No
   RFC 0006 change is outstanding on this item.** (This RFC caught the same
   pattern in RFC6-22 at defect 2 and had reproduced it one layer down in
   its own RFC9-43.)
5. **RFC2-6's observation-record contents omit the base layout.** —
   **RESOLVED UPSTREAM 2026-08-01; retained for the trail, no longer
   outstanding.** As reported: RFC9-14 asserts the declared-identity base
   layout is part of the deterministic observation record, and doctrine
   names it inside the identity test ("over the deterministic observed graph
   **and base layout**" [Observed: architecture.md]) — but RFC2-6's
   enumeration (evaluation identity, deterministic observed graph, claim
   instances, coverage records, freshness states, challenge/contradiction
   sets, observer/adapter versions) did not list it, so an implementer
   building the record from RFC2-6 would never persist it and RFC9-47's "two
   runs, one evaluation, identical base layout" gate would have no recorded
   artifact to compare against — making the layout-determinism claim
   untestable after the fact. RFC2-6's enumeration now carries "**the
   declared-identity base layout**", with the identity-test reason stated
   inline [Observed — RFC2-6 as of 2026-08-01]. This was a correction rather
   than a new decision, since doctrine already named it. **No RFC 0002
   change is outstanding on this item.**

**Provides to:** RFC 0007/0008 — the map-side rendering obligations behind
cross-surface highlights (same reserved palette semantics for shared
states); craft-and-care — the release-gate list (RFC9-47), legend/
palette registry discipline, and the interaction-cost material this
contract deliberately declines to bind (the return-to-home affordance's
*form and cost* — what the action is, its placement, its labelling, and how
many steps it takes — RFC9-10(c) binding only that return is always available
and discoverable, per B21); the first map-surface spec — every declared-value slot
this RFC deliberately leaves open (budget values, treatment values, band
counts, analytical-plane catalog).

**Not this RFC's:** rendering engine, layout algorithms and tuning,
concrete visual treatment values, legend layout, lens metric formulas,
V1 gap-object rendering (V0 renders absence), certificate rendering
(post-V1, future-tagged), live fleet streaming (deferred mandate).

---

## 6. Alternatives considered

- **One geography with lenses only (the research brief's frame), no
  analytical planes.** Rejected by SDR-21: real analytical questions
  (dependency distance, component architecture) genuinely want positional
  encoding; forbidding it everywhere pushes those views out of the
  product or, worse, into home geography by stealth. Two regimes with a
  hard masquerade boundary keep both honest.
- **Minted sticky home for undeclared shared components** (research
  §1.3). Rejected in favor of RFC9-20: SDR-22 refuses the forced single
  district, and a renderer-minted home — even sticky and visible — is a
  placement governance answer produced by an algorithm; the
  placement-undeclared aggregation renders the truth (nobody decided) and
  routes to the deciding act.
- **Freezing height to one V0 meaning** (research FRC-6 recommendation).
  Rejected by SDR-24 ⚑: per-lens height with mandatory legend; the
  learnability bet is revisitable via amendment after comprehension
  walkthroughs, without breaking any truth rule.
- **Factory at V0 alongside City.** Rejected by SDR-19: Factory's honest
  inputs are largely SEC-3-gated; work state rides City as an overlay;
  shipping Factory early tempts synthesized motion, the sharpest fiction
  risk on this surface.
- **Repository as first-class partition.** Rejected by SDR-23: it
  re-anchors geography to a storage fact and relocates the map whenever
  code moves repositories.
- **Rendering unmapped code as individual buildings by default.**
  Rejected by SDR-25: overwhelming, and it renders unstable path-derived
  identities as stable places; aggregate-with-expansion is VIS-1's
  endorsed pattern.
- **Historical rendering now, amendment later.** Rejected at drafting:
  building it unconditionally would have treated a then-pending doctrine
  amendment as adopted. *(Outcome: the owner ratified that amendment as D1,
  so the constitutional scope is now unconditional — but the rejection's
  second half stands: the concrete interaction design still goes through
  its own approval, per RFC9-41 as rewritten.)*
- **Encoding provenance as a new RFC6-19 drawer content class**
  (RFC9-3). Rejected in favor of a surface-local "explain this encoding"
  affordance. The requirement — an encoding a reader cannot explain from
  evidence is the charter's named failure — is satisfied either way, but
  the kernel route costs doctrine: RFC6-18's one-fact-set invariant is
  fixed per (selection reference, evaluation identity, scenario context)
  with no lens dimension, so an eighth content class would either make
  the shared fact set vary with personal presentation state (VIS-6,
  exception (a); RFC6-7) or hand Polaris and Trajectory drawer fields
  about a surface they do not render. The surface-local affordance is the
  cheapest fix that costs no doctrine, and it stays evidence-derived
  because the channel registry it reads is itself a governed artifact
  (RFC9-26/18). Recorded here rather than discarded silently, since the
  alternative is the one a later RFC 0006 revision might prefer.

---

## 7. Deliberately deferred

Rendering technology, layout algorithms and tuning, and concrete visual
treatment values → post-acceptance spec/design-contract material (none
may weaken a clause here). Performance budget *values* and the
release-gate operating procedure → craft-and-care / quality policy. The
analytical-plane catalog beyond the component/architecture analytical
plane → map-surface specs, each analytical plane entering under RFC9-10.
Interaction design, including the **form and cost** of the return-to-home
affordance (RFC9-10(c) binds only that return is always available and
discoverable, per B21; which action it is, how many steps it takes, and how it
is placed and labelled, is not bound here) →
craft-and-care. Lens metric
formulas and band edges → per-lens spec + quality policy. Factory's full
scene contract → its own later spec under RFC9-36/37's bound invariants.
Historical-scene retention and renderable-evaluation selection →
quality/evidence policy, active only under RFC9-41. Modelled interiors
below source/test evidence → post-V0 elaboration, no promise made. V1
gap-object rendering on the map → V1 RFC, over the same identities.

---

## 8. Open questions for acceptance

1. **The placement relation (Integration defect 1).** Amend RFC 0001 to
   carry a declared topology-entry→capability placement edge (extend
   `part_of` vs a new `placed_in`), or rule that district membership is
   derived solely from implementation mappings' capability edges (leaving
   component blocks unplaced when mappings are absent)? This RFC assumes
   the declared edge; the map cannot render its L4 level without an
   answer.

   > **ANSWERED at acceptance — A7.** `placed_in` (Topology entry → Capability, Desired/declared) added to RFC1-25 by owner amendment rather than by extending `part_of`. Integration defect 1 discharged.
2. **Undeclared shared-component placement (RFC9-20).** Confirm the
   placement-undeclared aggregation over the research's minted-sticky-home
   alternative. The trade: honest-but-lumpy (shared district grows on
   undeclared projects) versus prettier-but-renderer-decided homes.
3. **Historical conditionality (RFC9-41).** Accept the dormant-clause
   design, or adopt the amendment packet at the same gate so the clause
   activates with acceptance? Adopting together avoids a second ruling;
   keeping them separate keeps doctrine amendment visibly distinct from
   RFC acceptance (VIS-4).

   > **ANSWERED at acceptance — D1, in part.** The doctrine amendment making `map/` include historical state **is adopted**, so the dormant clause's premise holds. The historical *design* — ghost-step opacity, milestone scenes, scrubber — is **held behind its own review** and does not go live on this adoption.
4. **Analytical-plane governance (RFC9-10/18).** May an owner promote a
   personal analytical-plane definition into a named, governed analytical
   plane under `.syzygy/map/**` (shareable, versioned, still
   marker-bound), or do all analytical-plane definitions ship
   product-defined at V0? Proposed: promotion permitted — it is a
   governance act like any promotion (VIS-6), and the masquerade boundary
   does not depend on who authored the analytical plane.

   > **ANSWERED at acceptance — B12(c)/B17.** One rule for lenses, analytical planes and profile relations alike: personal definition and use is free; **promotion** to a named, governed, versioned artifact is an owner governance act under RFC3-16(a).
5. **The declared dependency relation (Integration defect 1, second
   half).** RFC9-9 requires dependency edges to render on their own
   explicit, resolvable channel, but RFC1-25 offers only *observed*
   (`depends_on` code→code, `structurally_related`) and execution-class
   dependency edges at V0. Amend RFC 0001 to carry a declared dependency
   relation between capabilities and/or topology entries, or rule that V0
   renders observed and execution dependency edges only — legended as
   what they are, with no "declared" dependency channel until the
   vocabulary carries one? This RFC takes the second position provisionally
   (it will not legend an observed edge as declared) but the map's
   dependency channel is thinner than RFC9-9's intent until the relation
   exists. **The question is intra-project only.** At project scope the
   portfolio profile already supplies a declared relation
   (`depends-on`, RFC3-14) under RFC1-26's second limb, and RFC9-9
   legends it as a profile relation; answering this question either way
   changes nothing there. RFC 0001 §8 q6 puts the adjacent and distinct
   question — whether a declared dependency relation belongs in the *kernel*
   vocabulary at all, or stays a profile relation — and the two should be
   read together.

   > **ANSWERED at acceptance — A6.** `declared-dependency` minted in RFC1-25. Integration defect 1's second half discharged; the declared-dependency channel is now backed by a relation that exists.
6. **Is a layout-version change an owner-gated governance act (RFC9-16(d),
   RFC9-18)?** The technical bounds are bound here regardless: a recorded
   rationale naming what the change buys and what it moves, and
   reservation policy unbounded in principle so ordinary growth never
   forces a bump. The open question is the **gate**. RFC3-18 binds the
   namespace class and confers no adoption gate, and VIS-4's shape-level
   sign-off list does not name layout — so making the bump an owner act
   extends that list, which is the owner's call. Drafted position:
   **owner-gated**, because the bumper is Syzygy (an agent), the act
   relocates every declared entity on every governed project, and
   append-stability — the property the whole 3D mandate rests on — is
   otherwise defeasible at an agent's discretion.

   > **ANSWERED at acceptance — A3, narrowed after review 8.** Owner-gated governance act with recorded rationale, **except** where the two versions are demonstrated to be the **same placement function** — agreement on every layout input tuple, not on one declaration set — which needs only a recorded note. The demonstration is a **layout-equivalence check**, not the RFC2-3 identity test (RFC2-3 is intra-evaluation and says nothing about comparing two layout versions; the earlier citation here was wrong, ML-R7). An asserted exemption is not a carve-out. See RFC9-16(d).
7. **Does proximity in home geography carry any declared meaning beyond
   containment (RFC9-9/RFC9-4)?** This RFC binds "proximity encodes
   declared containment and nothing else; it never encodes a
   measurement". The alternative the owner has not been asked about is
   richer: adjacency also expressing **declared topology nesting** (a
   component block sited next to the block it is declared to sit under).
   SDR-21 requires home to be stable, capability-oriented, reproducible
   and append-stable — it does not require proximity to be meaningless,
   so the narrower rule forecloses a family of home layouts by prose
   rather than by ruling. Either answer keeps the measurement prohibition
   intact.

   > **ANSWERED at acceptance — B12(a), reversing the drafted position.** Proximity carries **two** declared readings: containment (RFC9-4) and **declared relatedness** via `declared-dependency`. It never encodes a measurement, and undeclared *inputs* to placement stay barred. Reading 2 is best-effort; its shortfall renders **not-honored**, on a registered channel with its own Unknown value (RFC9-9(b)). Review 8 (ML-R3) then established that the legend needs a **third** line — *residual adjacency, carries no meaning* — because append-into-free-space produces nearness on a basis that is neither reading, and a two-line legend would be false for most adjacency on screen. See RFC9-9, RFC9-9(a), RFC9-9(b) and RFC9-15(b).
8. **Is the comprehension test a release gate (RFC9-45)?** This RFC makes
   "a reader stating something false that the map supported" a
   release-blocking trust-floor incident. v1.md frames the comprehension
   test as an owner-judged **success** test, re-judged at stage gates and
   explicitly "never rendered Observed". Converting it into a release gate
   is defensible — a reader misled by the map *is* a trust-floor breach —
   but it hands a release veto to a subjective walkthrough outcome, and
   the escalation has not been ruled. Confirm, or keep the walkthrough as
   a judged success signal with a separately defined release criterion.

   > **ANSWERED at acceptance — B12(b).** Yes, a release gate — **with attributed judgment**: every pass or fail names the judging party and records its rationale. The verdict is never rendered Observed. *(Rev7 rework, directive item A4 — not owner decision A4: the gate's structure is now three artifacts — kernel-recorded execution record in `records/`, attributed judgment in `decisions/`, and the owner-approved release policy in `policies/` that alone confers release authority.)*
9. **Who may adopt a lens (RFC9-32/35)?** RFC9-35 calls adding a lens "a
   contract act" without naming whose act it is, and q4 above asks only
   about governed analytical planes. Lenses bind **height** — the channel
   SDR-24 deliberately left unfrozen — so lens adoption authority
   determines who may change what height means. Product-defined only at
   V0; owner-promotable like analytical planes; or a distinct authority?
   **Answer this for extension profiles generally, not for lenses alone.**
   The same authority question arises three times in this RFC — lens
   adoption here, analytical-plane promotion at q4, and **who may add a
   profile *relation*** (RFC9-9's new profile-relation rule; RFC1-7,
   RFC1-26's second limb). All three add vocabulary that changes what a
   rendered encoding *means*, which is the third limb of RFC3-16(a)'s
   predicate. Answering two of the three and leaving the third to be
   settled by whoever first needs it is the asymmetry this section exists
   to avoid. *(The surface is safe under either answer meanwhile: an
   unregistered profile relation fails closed under RFC9-26 and never
   reaches a reader as an unlegended edge. The home of the general rule is
   RFC1-7/RFC1-26, not this clause.)*

   > **ANSWERED at acceptance — B12(c)/B17**, with q4 and the profile-relation limb. Same single rule.
10. **Does the return-to-home bound stay "one action" (RFC9-10(c);
    SDR-21)?** SDR-21's ratified wording is that analytical planes are
    "always legended, visibly temporary, **one action back to home**". A
    draft of RFC9-10(c) had restated this as "always available and
    discoverable"; the restatement has been reverted, because a contract
    clause may not narrow ratified text by prose. The question is put here
    instead. **For relaxing:** the truth-bearing obligation really is that
    the reader is never stranded outside home, and interaction cost really
    is craft-and-care material — this RFC defers every other interaction
    cost, and "one action" reaches into affordance design in a way no other
    clause here does. **Against:** SDR-21 is ratified text, and "one action"
    is a **testable bound** — a release check can count actions — where
    "available and discoverable" is a judgement no gate can run, so the
    relaxation converts a checkable obligation into an unfalsifiable one on
    the surface whose whole contract is checkability. Confirm SDR-21's bound
    as written (current position), or grant the relaxation explicitly, in
    which case CC-VIZ-5 is amended to match rather than left carrying the
    stricter form.

    > **ANSWERED at acceptance — B21, granting the relaxation.** The obligation is that the reader is never stranded outside home; the return affordance is "always available and discoverable" rather than a counted action bound. CC-VIZ-5 has been amended to match, so no artifact is left carrying the stricter form. The owner accepted the stated cost: a checkable bound becomes a judged one on the surface whose contract is checkability, and no release gate can count actions any more. See RFC9-10(c) and CC-VIZ-5.

---

*End of RFC 0009. Clauses RFC9-1 … RFC9-52, plus lettered sub-clauses
RFC9-8(a), RFC9-9(a), RFC9-9(b), RFC9-13(a), RFC9-14(a), RFC9-15(b),
RFC9-16(d) and RFC9-47(a); lettered limbs cited inside their parent clauses (e.g.
RFC9-10(c), RFC9-19(b)) are parts of those clauses, not separate sub-clauses.
The clause range is closed: amend in place, add lettered sub-clauses, never
renumber.*
