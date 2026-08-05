> **Approved** — owner decision D2 (2026-08-01), amendment B21 applied where noted. **This directory (`.syzygy/governance/policies/craft-and-care/`) is the canonical home of these policies.** The bootstrap-phase copy is preserved separately as historical review evidence. Binding force on implementation work begins with the owner's digest-bound acceptance of the foundational design contracts (the act defined in the active acceptance record; the policies cite RFC clauses that bind nothing until then).

# Performance and visual discipline

Two disciplines that share one constraint: neither speed nor beauty is ever
bought with truth. Performance policies are `CC-PERF-n`; visual policies are
`CC-VIZ-n` (avoiding collision with doctrine's `VIS-n`).

## Performance

### CC-PERF-1 — The only legal currency for performance is declared scope

Performance is never purchased with truth, determinism, or completeness. The
permitted currency is VIS-1, rank 4 — breadth of scope and fidelity of
presentation — and only above the comprehension constraint: performance may
**narrow an explicitly declared scope**; it may never present incomplete
coverage as complete within a declared scope [Observed — vision.md,
Performance]. Sampling, truncation, and lazy evaluation are legal exactly
when the surface says so.

*Violation:* an evaluation that times out after scanning 80% of a repository
and renders the result as the whole repository's status, unannotated.

### CC-PERF-2 — Derived conveniences are sacrificial; correctness of caches is not optional

Caches, incremental refresh, and other derived conveniences are VIS-1,
rank 5 material — droppable under pressure, never load-bearing for truth. A cache
is always a rebuildable projection (VIS-6): when correctness of a cached
answer is in doubt, the system recomputes or renders Unknown; it never
serves a doubtful cached value as current.

*Violation:* an invalidation bug worked around by extending the cache TTL,
trading truth for latency.

### CC-PERF-3 — Performance claims carry measurement evidence

Responsiveness targets are contractual (RFC/spec material), not
constitutional [Observed — vision.md]. Any claim that a change improves or
regresses performance follows the evidence bar: a retained measurement
artifact with its conditions, or the claim is labeled [Unknown]. Perf work
without before/after evidence is unverified work.

*Violation:* "made the map load faster" in a change record, with no
measurement, becoming a cited fact in the next planning round.

## Visual discipline

### CC-VIZ-1 — Every encoding declares source, units, legend, Unknown behavior, and freshness

Every visual encoding (color, height, size, position, motion) declares: the
data source it renders, its units/scale, a legend stating exactly what it
means, how Unknown values render, and the freshness of the underlying
evaluation. An encoding means exactly what its legend says — the trust floor
(VIS-7) makes an unfaithful legend release-blocking. Per SDR-24, a dimension
like height has **one declared meaning per active lens**, always visible in
the legend; no universal meaning is frozen now.

*Violation:* a heatmap whose legend says "test coverage" while the shader
mixes coverage with change-frequency "for visual interest."

### CC-VIZ-2 — No decorative element may silently misstate project truth

Decoration is permitted; deception is not. Any element a viewer could
plausibly read as data must either be data (with CC-VIZ-1's declarations) or
be identifiable as decoration. The durable principle: **motion reads as
change, and unearned change-signals are fiction** — motion is reserved for
labelled transitions, selected flows, and camera movement. Ambient motion
is excluded at the current lifecycle stage per SDR-26 (a stage-scoped
ruling this policy cites, not a meaning frozen here).

*Violation:* idle "activity shimmer" on buildings in an unobserved district,
read by the owner as a busy fleet.

### CC-VIZ-3 — Unknowns are visible, aggregated honestly, never disappeared

Unknown and unmapped regions render as such: unmapped code is aggregated by
default **with count, reason, and expandable detail** — it must not
disappear (SDR-25). Honest simplification aggregates ("Unknown ×40"); it
never substitutes a confident state for an Unknown one (VIS-1). Aggregation
anywhere discloses **membership count, the full aggregation-composition
tuple, and expansion to members** — the standing pattern (SDR-27). The tuple
is bound normatively by **RFC6-17** (and, for the map surface, **RFC9-43**),
and this policy **cites it rather than restating it**: a local restatement is
how earlier copies of the obligation drifted into narrower forms, and
whatever those clauses enumerate is what a compliant aggregate discloses.

*Violation:* a "clean" default view that filters out Unknown regions
entirely, presenting a fully-green city over a half-observed project.

*Violation:* a district panel reading "Observed ×30, Unknown ×10" over
members that are all `reduced-fidelity`, a dozen of them stale — the count
is disclosed and expandable, the composition is not, and the aggregate reads
as a well-evidenced current district.

### CC-VIZ-4 — Non-3D paths are co-equal and semantically equivalent

Non-3D views (2D, tabular, keyboard-navigable) are **co-equal and
semantically/query equivalent** to the 3D scene: same evaluation, same
filters, same underlying graph, same epistemic state (SDR-27). They may
expose finer detail than an aggregated scene; they may never expose a
*different truth*. Keyboard and non-3D navigation are always available
(v1.md). This is an accessibility obligation and a trust obligation at
once: a user who cannot or will not use 3D receives undegraded truth.

*Violation:* a status filter implemented only in the 3D scene, so the
tabular view answers the same query with different rows.

### CC-VIZ-5 — Layout is reproducible; geography is stable; analytical planes are labelled

Home geography anchors to capability identities, not file paths; layout is
reproducible from the same snapshot; refactors must not randomly relocate
the map (architecture.md; SDR-21). Alternate projections where position
encodes a metric are **analytical planes**: explicitly selected, always
legended, visibly temporary, and **return to home is always available and
discoverable** (SDR-21 as relaxed by the owner at RFC acceptance — the earlier
"one action back to home" wording is superseded; RFC9-10(c) governs).
Repository structure is an overlay, never the primary geography (SDR-23).

**Layout is a pure function of the layout input tuple — (declaration set,
layout baseline, layout version)** — never of insertion order, never of refresh
history. *(Corrected after review 8: an earlier wording named two inputs and
omitted the **baseline**, which is what makes "hold what the last regeneration
placed" expressible at all; the two-input form was false, and two conforming
implementations could satisfy it while disagreeing on every coordinate.)*
Within a layout version, positions are fixed and nothing relocates;
regeneration is full, manual, and an owner act (RFC9-14(a), RFC9-15(b),
RFC9-16(d)). Two implementations given the same tuple in different orders must
produce identical coordinates.

*Violation:* a layout seeded from iteration order of an unordered store, so
every restart shuffles the city and destroys the owner's spatial memory; a
layout in which adding a capability moves an existing one; a partial refresh
that regenerates some zones while others hold.
