> **Approved** — owner decision D2 (2026-08-01), amendment B21 applied where noted. **This directory (`.syzygy/governance/policies/craft-and-care/`) is the canonical home of these policies.** The bootstrap-phase copy is preserved separately as historical review evidence. Binding force on implementation work begins with the owner's digest-bound acceptance of the foundational design contracts (the act defined in the active acceptance record; the policies cite RFC clauses that bind nothing until then).

# Performance and visual discipline

Neither speed nor beauty is ever bought with truth: performance spends only
declared scope, and anything a viewer could plausibly read as data either
is data or is identifiable as decoration.

- **Performance policies** are `CC-PERF-n`.
- **Visual policies** are `CC-VIZ-n`, avoiding collision with doctrine's
  `VIS-n`.

## Performance

Performance spends only declared scope, treats caches as sacrificial, and
backs every performance claim with a retained measurement artifact and its
conditions, or labels it [Unknown].

### CC-PERF-1 — The only legal currency for performance is declared scope

Performance is never purchased with truth, determinism, or completeness;
its only legal currency is declared scope [Observed — vision.md,
Performance].

- **The permitted currency** is VIS-1, rank 4 — breadth of scope and fidelity
  of presentation — and only above the comprehension constraint.
- **What performance may do:** **narrow an explicitly declared scope**.
- **What it may never do:** present incomplete coverage as complete within a
  declared scope.
- **Sampling, truncation, and lazy evaluation** are legal exactly when the
  surface says so.
- *Violation:* an evaluation that times out after scanning 80% of a
  repository and renders the result as the whole repository's status,
  unannotated.

### CC-PERF-2 — Derived conveniences are sacrificial; correctness of caches is not optional

Caches, incremental refresh, and other derived conveniences are droppable
under pressure and never load-bearing for truth.

- **Rank:** they are VIS-1, rank 5 material.
- **A cache is always a rebuildable projection** (VIS-6).
- **When correctness of a cached answer is in doubt**, the system recomputes
  or renders Unknown; it never serves a doubtful cached value as current.
- *Violation:* an invalidation bug worked around by extending the cache TTL,
  trading truth for latency.

### CC-PERF-3 — Performance claims carry measurement evidence

Any claim that a change improves or regresses performance carries a
retained measurement artifact with its conditions, or it is labeled
[Unknown].

- **Responsiveness targets are contractual** (RFC/spec material), not
  constitutional [Observed — vision.md].
- **The evidence bar:** a retained measurement artifact with its conditions,
  or the claim is labeled [Unknown].
- **Perf work without before/after evidence** is unverified work.
- *Violation:* "made the map load faster" in a change record, with no
  measurement, becoming a cited fact in the next planning round.

## Visual discipline

Every encoding declares its source, units/scale, legend, Unknown behavior and
freshness; decoration never silently misstates truth; Unknowns stay visible,
including inside aggregates; non-3D views tell the same truth as the 3D scene;
and layout is reproducible.

### CC-VIZ-1 — Every encoding declares source, units, legend, Unknown behavior, and freshness

Every visual encoding means exactly what its declared legend says, and
declares its source, units/scale, legend, Unknown behavior, and freshness.

- **Encodings include:** color, height, size, position, motion.
- **Each declares:**
  - the data source it renders;
  - its units/scale;
  - a legend stating exactly what it means;
  - how Unknown values render;
  - the freshness of the underlying evaluation.
- **An encoding means exactly what its legend says.** The trust floor (VIS-7)
  makes an unfaithful legend release-blocking.
- **One meaning per lens (SDR-24):** a dimension like height has **one
  declared meaning per active lens**, always visible in the legend; no
  universal meaning is frozen now.
- *Violation:* a heatmap whose legend says "test coverage" while the shader
  mixes coverage with change-frequency "for visual interest."

### CC-VIZ-2 — No decorative element may silently misstate project truth

Decoration is permitted; deception is not.

- **Any element a viewer could plausibly read as data** must either be data
  (with CC-VIZ-1's declarations) or be identifiable as decoration.
- **The durable principle:** **motion reads as change, and unearned
  change-signals are fiction.**
  - Motion is reserved for labelled transitions, selected flows, and camera
    movement.
  - Ambient motion is excluded at the current lifecycle stage per SDR-26 — a
    stage-scoped ruling this policy cites, not a meaning frozen here.
- *Violation:* idle "activity shimmer" on buildings in an unobserved
  district, read by the owner as a busy fleet.

### CC-VIZ-3 — Unknowns are visible, aggregated honestly, never disappeared

Unknown and unmapped regions render as such, and an aggregate discloses its
count, composition and members rather than hiding them.

- **Unmapped code** is aggregated by default **with count, reason, and
  expandable detail** — it must not disappear (SDR-25).
- **Honest simplification aggregates** ("Unknown ×40"); it never substitutes
  a confident state for an Unknown one (VIS-1).
- **Every aggregation, anywhere, discloses** **membership count, the full
  aggregation-composition tuple, and expansion to members** — the standing
  pattern (SDR-27).
- **The tuple is bound normatively elsewhere.**
  - **RFC6-17** binds it, and, for the map surface, **RFC9-43**.
  - This policy **cites it rather than restating it**: a local restatement is
    how earlier copies of the obligation drifted into narrower forms.
  - Whatever those clauses enumerate is what a compliant aggregate discloses.
- *Violation:* a "clean" default view that filters out Unknown regions
  entirely, presenting a fully-green city over a half-observed project.
- *Violation:* a district panel reading "Observed ×30, Unknown ×10" over
  members that are all `reduced-fidelity`, a dozen of them stale — the count
  is disclosed and expandable, the composition is not, and the aggregate
  reads as a well-evidenced current district.

### CC-VIZ-4 — Non-3D paths are co-equal and semantically equivalent

Non-3D views are **co-equal and semantically/query equivalent** to the 3D
scene: a user who cannot or will not use 3D receives undegraded truth.

- **Non-3D views:** 2D, tabular, keyboard-navigable.
- **Equivalent means** same evaluation, same filters, same underlying graph,
  same epistemic state (SDR-27).
- **They may expose finer detail** than an aggregated scene; they may never
  expose a *different truth*.
- **Keyboard and non-3D navigation are always available** (v1.md).
- **This is two obligations at once:** accessibility and trust.
- *Violation:* a status filter implemented only in the 3D scene, so the
  tabular view answers the same query with different rows.

### CC-VIZ-5 — Layout is reproducible; geography is stable; analytical planes are labelled

The map's home geography is stable and reproducible, alternate projections
are labelled and temporary, and layout is a pure function of its input
tuple.

```mermaid
flowchart LR
    T["Layout input tuple:<br/>declaration set, layout baseline, layout version"] --> L["Layout (pure function)"]
    L --> C["Coordinates, fixed within the layout version"]
    C -->|"only by full, manual regeneration (an owner act)"| N["Next layout version"]
```

- **Home geography** (architecture.md; SDR-21):
  - it anchors to capability identities, not file paths;
  - layout is reproducible from the same snapshot;
  - refactors must not randomly relocate the map.
- **Analytical planes** are alternate projections where position encodes a
  metric.
  - They are explicitly selected, always legended, and visibly temporary.
  - **Return to home is always available and discoverable.**
  - Source: SDR-21 as relaxed by the owner at RFC acceptance — the earlier
    "one action back to home" wording is superseded; RFC9-10(c) governs.
- **Repository structure is an overlay**, never the primary geography
  (SDR-23).

**Layout is a pure function of the layout input tuple — (declaration set,
layout baseline, layout version)** — never of insertion order, never of
refresh history.

- **Order-independence:** two implementations given the same tuple in
  different orders must produce identical coordinates.
- **Within a layout version**, positions are fixed and nothing relocates.
- **Regeneration** is full, manual, and an owner act (RFC9-14(a),
  RFC9-15(b), RFC9-16(d)).
- Correction (review 8): an earlier two-input wording omitted the
  **baseline**, which is what makes "hold what the last regeneration placed"
  expressible at all; that form was false, and two conforming
  implementations could satisfy it while disagreeing on every coordinate.
- *Violation:* a layout seeded from iteration order of an unordered store, so
  every restart shuffles the city and destroys the owner's spatial memory; a
  layout in which adding a capability moves an existing one; a partial refresh
  that regenerates some zones while others hold.
