# Surface Decision Record

> **Status:** Owner-ratified decisions — recorded 2026-07-30 from the owner's
> foundational-RFC phase directive, which resolved the rev6 surface-shaping
> founder rulings (R-1…R-20). Authority: the owner's directive itself.
> This record is the compact decision layer; the full ~132k-word research
> corpus behind it stays archived and **non-authoritative** in
> `_bootstrap/drafts/surface-shaping/` (+ `reviews/`). Do not load that corpus
> by default; cite this record, and follow its links only when depth is needed.

## 1. Shared product thesis

Syzygy is a specification-driven software control plane. Human-readable
governance artifacts define **desired state**; code, tests, CI, and runtime
define **observed implementation state**; scheduler and fleet records define
**execution state** — and work is never proof intent is satisfied
(vision.md, Thesis). Three surfaces — **Polaris** (`intent/`), **Trajectory**
(`work/`), **Orrery** (`map/`) — are projections over **one shared temporal
Project Graph and Reconciliation Kernel**: independently navigable and
plannable, never independently authoritative, semantics never forked.
Truth rendering obeys the exclusive three-label rule — **Observed / Inferred /
Unknown** — with no evidence rendering Unknown, never green, never zero.

## 2. Lean surface charter

**Polaris — Intent.** A cohesive visual argument for what a project is, why it
exists, what it promises, how it is architected, and what its specifications
require, progressively disclosing from white-paper narrative into exact
capabilities, requirements, contracts, evidence, and work. *Not satisfied by:*
a document tree, generated README, disconnected specification browser, or
attractive prose detached from authoritative intent.

**Trajectory — Work.** The owner's account of what remains, what is planned,
what is active, what is blocked, what changed, what it cost, and why the work
exists — with dependencies and provenance navigable from intent through
execution and verification. *Not satisfied by:* a Kanban board, Beads mirror,
or issue list that cannot account for execution and resulting changes.

**Orrery — Map.** A stable, semantically grounded spatial model of observed,
intended, proposed, and historical project state, supporting multiple truthful
measurement lenses through a reproducible 3D view with semantically equivalent
non-3D paths. *Not satisfied by:* a decorative 3D file tree, single-metric
software city, unstable layout, or scene whose encodings cannot be explained
from evidence.

*Doctrine note:* this charter is decision-layer, not doctrine. Its one
doctrine-text implication — adding **"historical"** to the `map/` definition in
architecture.md ("observed, intended, and proposed" state) — is drafted as a
minimal amendment packet (`DOCTRINE-AMENDMENT-D1-MAP-HISTORICAL.md`, this directory — extracted under FD-037)
and binds nothing until the owner adopts it. Adopted doctrine is not modified
by this record. **[Update, 2026-08-01: the owner ratified that packet as
amendment D1; architecture.md now carries "historical" at both sites, and the
doctrine README's amendment log records it. This paragraph is preserved as
written for the historical record.]**

## 3. Owner rulings (SDR-1 … SDR-37)

Indexed for citation as `SDR-n`. Where a ruling resolves a rev6 founder
question, the R-number is noted; where the owner ruled **differently from the
rev6 recommendation**, that is marked ⚑ — the divergence is deliberate.

### Vocabulary and kernel

- **SDR-1** (R-1 ⚑ — narrower than recommended): `Feature` is **not** a kernel
  entity and **not** a work-warrant class. `Capability` is the stable
  product-behavior identity. "Feature request" may remain workflow vocabulary;
  informal UI text may say "feature" only where it resolves to a Capability.
- **SDR-2** (R-12): Claim and gap identity have **two levels** — durable
  semantic identity across evaluations, and evaluation-specific instances
  carrying status, evidence, freshness, and challenge state.
- **SDR-3** (R-13): Capability-to-code relationships must distinguish
  (i) declared implementation mapping, (ii) inferred implementation mapping,
  (iii) deterministically observed structural relationships, and
  (iv) requirement/scenario verification. **A passing test does not by itself
  prove semantic ownership.**
- **SDR-4** (R-13 declaration site): governance mapping artifacts are the
  **primary declaration site**; optional code markers may supplement, never
  required.

### Trajectory and fleet evidence

- **SDR-5** (R-2): structured, **post-hoc execution telemetry enters V1**.
  Terminal-grade streaming, intervention, and live control remain deferred.
- **SDR-6** (R-2/R-11 corollary): missing token/cost information renders
  **Unknown, never zero**.
- **SDR-7** (R-5, option (a)): `.syzygy/work/**` owns approved execution
  intent **before materialization**; Beads owns lifecycle state **after**;
  materialization creates an **immutable one-way mapping record**.
- **SDR-8** (R-10 ⚑ — rejects the recommended new doctrine class): an
  **Execution Record is an Evidence artifact** under `.syzygy/work/**`. No new
  doctrine-level evidence class is invented.
- **SDR-9** (R-11): "a worker reported tests passed" may be **Observed as a
  report fact**; "tests passed" is Observed **only** when backed by a
  retained, resolvable gate artifact — otherwise Inferred or Unknown per
  provenance.
- **SDR-10** (R-6): compaction must preserve structured run summaries, work
  warrants, decisions, materialization mappings, known cost/token totals,
  evidence identities and hashes, and reconciliation outcomes. Raw transcripts
  and verbose logs may expire under policy.
- **SDR-11** (R-16): small inherited mutations appear in the **parent run
  summary** with rationale and touched surfaces — not one Bead each.
- **SDR-12** (R-15): V0 may show merged-but-unreconciled work as
  "reconciliation evidence absent / Unknown"; **V1 computes** the
  corresponding reconciliation gap.

### Polaris

- **SDR-13** (R-3 ⚑ — neither pure governance nor pure presentation, and not
  the recommended structure/prose split): Polaris narrative is a **governed
  presentation artifact** — versioned, attributed, revertible, human-readable,
  and **non-authoritative** relative to doctrine, contracts, and
  specifications.
- **SDR-14** (R-3/VIS-3 scope): fresh-reader review applies to **material
  narrative changes and release milestones**, not every prose correction.
- **SDR-15** (R-17): generated prose appears only as an explicit,
  **non-citable editorial draft** until a human adopts it into the curated
  narrative.
- **SDR-16** (P-I1 refinement): use **claim blocks or paragraph/section source
  anchors**, not a citation badge on every sentence.
- **SDR-17** (R-18): status display **minimal by default**; reader-controlled
  detail later.
- **SDR-18** (R-19): **Trajectory owns the drafting queue and work lifecycle;
  Polaris owns the contextual intent-authoring and adoption experience.**

### Orrery

- **SDR-19** (R-7): **City is required for V0**; Factory is a named later
  scene profile over the same graph, not a separate semantic model.
- **SDR-20** (R-4): V0 primary lenses: **Architecture** and **Verification**.
  V0 overlays: **work/construction** and **freshness/staleness**. Change/churn
  follows next; Risk and Runtime are later lenses.
- **SDR-21** (new — two spatial regimes): **Home geography** (stable,
  capability-oriented, reproducible, append-stable, built for spatial memory)
  vs **analytical planes** (explicitly selected alternate projections where
  position/proximity may encode a declared metric — always legended, visibly
  temporary, one action back to home).
- **SDR-22** (R-20a ⚑ — refines the sticky-home recommendation): do **not**
  force every shared component into one arbitrary capability district. Use a
  separate component/architecture plane, a shared-infrastructure district, or
  multi-capability edges with **identity-based counting**.
- **SDR-23** (R-20b): repository is an **overlay**, not the primary geography.
- **SDR-24** (R-20c ⚑ — the alternative, not the freeze): height has **one
  declared meaning per active lens**, always visible in the legend; **no
  universal height meaning is frozen now**.
- **SDR-25** (R-20d): unmapped code is **aggregated by default** with count,
  reason, and expandable detail. It must not disappear.
- **SDR-26** (R-20e): **no ambient motion in V0**; motion is reserved for
  labelled transitions, selected flows, and camera movement.
- **SDR-27** (R-20f): non-3D views are **co-equal and semantically/query
  equivalent** — same evaluation, filters, underlying graph, epistemic state.
  They may expose finer detail than an aggregated 3D scene; aggregation must
  disclose membership count and allow expansion.

### Portfolio

- **SDR-28** (R-9): V0 portfolio truth is **derived from governed projects**.
- **SDR-29** (R-9 refinement): a platform-level **workspace manifest** may own
  only workspace concerns — local project membership, grouping/ordering, saved
  cross-project views, owner-specific portfolio narrative and dashboard
  preferences.
- **SDR-30** (R-9/OQ-010): the workspace manifest is **not authoritative for
  project-internal truth**; cross-project semantic relationships come from
  project declarations or render **unconfirmed/asymmetric**.

### Adapter evolution

- **SDR-31** (R-14a): **derivation-first observation**; explicit
  instrumentation is optional enrichment on a deliberate co-evolution roadmap.
- **SDR-32** (R-14b): adapter contracts support **resolvable spec anchors**;
  missing anchors render Unknown rather than rejecting the project.
- **SDR-33** (R-14c): capture **event-time evidence where available**; where
  only PR-level data exists, render **reduced fidelity explicitly** rather
  than inventing event-level certainty.

### Launch-critical decisions (round 2026-08g)

Ruled 2026-08-16 via an adversarially-reviewed owner-decision questionnaire
packet, not the rev6 founder-ruling corpus §3's other entries derive from —
no R-number applies to these four. Full background, options, and recorded
authorization boundary for each: `PENDING-OWNER-DECISIONS.md` (rows P-31,
P-36, P-37, P-40) and each row's own bounded packet in this directory.

- **SDR-34** (P-31): the merged-but-unreconciled Unknown reason ratifies the
  drafted `RFC2-19(a)` exemption as written. The condition is disclosed as a
  **fact of the render**, never dressed as a thirteenth `RFC2-24` reason;
  the closed twelve-reason list (decision `A5`) stays closed at twelve.
- **SDR-35** (P-36): the two-term vocabulary rule — **no verifying evidence →
  `Unknown`; evidence of non-satisfaction → `Gap`.**
- **SDR-36** (P-37): the seven project-shape facets (Registered, Shape
  present, Human-understandable, Observable, Traceable, Mission-ready,
  Reconciled) are adopted, **no cross-facet rollup**; the vocabulary's
  drafting site is the **Capability 1 specification** (site a2), not an
  RFC-0006 amendment — naming only the facets without the site leaves the
  question open in the form this packet was previously corrected for.
- **SDR-37** (P-40): the specification-granularity rule — **one OpenSpec
  change governs one coherent capability, or one coherent change to one**:
  one owner-readable product argument, one acceptance decision per change.

## 4. V0-core entity vocabulary

The kernel RFC defines these exactly; this list fixes *which* concepts are
V0-core (everything else enters via an extension profile). Names are
draft-local until RFC 0001 freezes them.

**Governance / desired:** Project · Governance root · Observed-source
repository · Consent record · Capability · Requirement + Scenario (OpenSpec
references) · Decision · Policy · Declared region (Genome) · Declared
implementation mapping (SDR-4).
**Temporal / epistemic:** Source snapshot · Evaluation (snapshot, as-of
instant) · Observation record (immutable) · Evidence artifact (incl.
Execution Record, SDR-8) · Claim (two-level, SDR-2) · Gap (two-level) ·
Contradiction · Challenge.
**Proposal / work:** Proposal · Approved plan item (pre-materialization home
`.syzygy/work/**`, SDR-7; kernel representation is an RFC 0001 question) ·
Materialization record (immutable, one-way) · Work item (substrate alias
"bead") · Execution run · Verification run · Reconciliation evaluation
(SDR-12).
**Structure:** Code element (identity adapter-defined, not path-only) ·
Component/topology entry · Observer/adapter identity.

**Extension profiles** (defined by RFCs, loaded per project need, never
presumed): *inference profile* (inference records, inferred mappings,
challenge machinery beyond admissibility floor); *presentation profile*
(personal view state, narrative composition entities, reading order);
*map profile* (districts, scenes, lenses, layout records); *portfolio
profile* (workspace manifest concerns, SDR-29); *annotation/dismissal
profile* (dismissals with reason+expiry, designations, milestones).

## 5. Remaining RFC-owned questions

1. Kernel representation of the approved-but-unmaterialized plan item —
   dedicated entity vs a Proposal kind (rev6 `10` R-5 sub-options) → RFC 0001.
2. Capability identity minting/continuity scheme; split/merge/rename → RFC 0001.
3. Relation vocabulary closure; realization of "Aligned" as claim predicate →
   RFC 0001.
4. Unknown-reason vocabulary closure + a **closed registry of rendering tiers
   with parent epistemic labels** (report-fact vs gate-backed per SDR-9;
   declared-only per SDR-3) → RFC 0002.
5. Currency bounds per claim class; challenge lifecycle detail → RFC 0002.
6. `project.yaml`, workspace manifest, `.syzygy/**` schema versioning and
   migration → RFC 0003.
7. Run envelope schema; adapter version registry; reduced-fidelity labeling →
   RFC 0004.
8. Machine-client authentication mechanism; execution profiles (blocking
   observed-code execution) → RFC 0005.
9. Selection/URL/query semantics; the single evidence drawer → RFC 0006.
10. Surface contracts (narrative model, work ontology, geography/lens
    grammar) → RFCs 0007–0009.
11. Certificate semantics — post-V1 RFC (unchanged).

## 6. Research corpus links (archived, non-authoritative)

`_bootstrap/drafts/surface-shaping/`: `01`-readiness · `02`-charter (full
clause-classified version of §2) · `03`-kernel (37-entity catalog, 26
relations, selection contract SC-1…9, invariants KI-1…16) · `04`-observation/
fleet events · `05`-Polaris · `06`-Trajectory · `07`-Orrery · `08`-vertical
slice · `09`-routing matrix · `10`-founder rulings (superseded by §3 above) ·
`reviews/` (5 fresh-context reviews + 5 disposition files). Bundle:
`syzygy-adoption-vet-rev6.zip` (external vet, 2026-07-30).
