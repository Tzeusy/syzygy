# 03 — One Kernel, Three Surfaces

> **Reviewed draft — grounded in proposed foundational contracts (currency note, not an ordering precondition: this bundle's own gate is §2 act 3 of the acceptance record and does not wait on the RFC act).** Reviewed fresh-context (reviews 5–7, dispositions recorded); updated at the rev7 rework for the corrected contracts (D1 historical scope, five governance categories, walkthrough three-way split, captured external confirmation, `Base` scenario context). Becomes canonical only by its **own owner act** — `ACCEPT TOPOLOGY: <bundle-manifest-digest>`, binding the exact digest of every file in the bundle — never implicitly on the RFC gate (RFC3-16: this stamp is a self-declaration; effective status lives in the owner-act record).
>
> Rendering: Mermaid is the durable, renderable fallback chosen for this phase; an Excalidraw + SVG upgrade is a tracked follow-up.

> Restyled 2026-09-28 for readability (no change of meaning); reviews 5–7 reviewed the prior bytes, and this restyle's review is recorded in [the topology restyle packet](../../governance/decisions/TOPOLOGY-TREE-RESTYLE.md).

## What this shows

One semantic kernel computes truth, and four co-equal consumers project it;
no surface is ever independently authoritative.

- **The kernel:** temporal project graph plus evaluation engine.
- **The consumers:** three human surfaces and the machine query plane.
- **The shared input:** one evidence drawer fact set feeds all of them,
  one per selection, evaluation and scenario context.

```mermaid
flowchart TB
    subgraph Kernel["One shared semantic kernel [target] — semantics live in .syzygy/governance/, never forked (architecture.md)"]
        Graph["Temporal Project Graph<br/>closed V0-core entities + closed relation set (RFC1-5/25);<br/>six state planes: desired / proposed / observed /<br/>inferred / execution / historical (RFC1-22)"]
        Eval["Evaluation engine<br/>evaluation = (source snapshot, as-of instant);<br/>deterministic layer identical across runs (RFC2-3; VIS-7)"]
        Drawer["Single evidence drawer fact set —<br/>one per (selection, evaluation, scenario context):<br/>identity, epistemic state, evidence links, provenance,<br/>warrant, challenges, policy visibility (RFC6-18/19)"]
    end

    subgraph SurfacesBox["Projections [target] — independently navigable and plannable, never independently authoritative"]
        Polaris["Polaris — intent/<br/>intent & comprehension surface"]
        Trajectory["Trajectory — work/<br/>gaps, work, convergence surface"]
        Orrery["Orrery — map/<br/>spatial twin: observed, intended,<br/>proposed, historical (D1 adopted)"]
        API["Machine query plane —<br/>co-equal, V0-mandatory (v1.md);<br/>agents see what the owner sees"]
    end

    Eval -->|"produces immutable observation records (deterministic facts only, RFC2-6)"| Graph
    Graph -->|"computes one fact set per selection (RFC6-18)"| Drawer
    Drawer -->|"same facts, same labels, same provenance — presentation may differ, facts may not"| Polaris
    Drawer -->|"same fact set"| Trajectory
    Drawer -->|"same fact set"| Orrery
    Drawer -->|"label parity: label + tier + reason + freshness verbatim (RFC6-13/14)"| API
```

## Authority boundaries

Only the kernel computes truth; every projection, human or machine, shows
the same facts for the same selection at one evaluation.

- **The kernel is the only truth-computer** [Observed: architecture.md, "One
  kernel, three surfaces"]: surfaces render; they never adjudicate, never
  pick winners among contradictions, never fork the shared definitions.
  - The owner ruled a single repository (monorepo) the constitutional
    realization of this invariant.
- **The machine plane is co-equal, not secondary** [Observed: vision.md two
  first-class consumers; RFC6-13]: no endpoint-only facts, no UI-only facts.
  - Anything a surface renders is queryable and vice versa.
- **One drawer** [Observed: RFC6-18]: two surfaces showing different
  evidence for one selection at one evaluation is a kernel defect, not a UI
  inconsistency.
  - Selection references use only kernel identities — never file paths,
    scene handles, or row indices (RFC6-1).
- **Rendering equivalence** [Observed: SDR-27; RFC6-22/23]: 3D, 2D, table,
  and machine answers must agree over the same declared scope.
  - They agree on entities, edges, labels, tiers, reasons, freshness, and
    counts.
  - Disagreement is release-blocking under the trust floor.

## [target] vs already true

Everything drawn is target; the surface charter, codenames and directory
names are already fixed, and Orrery's historical scope is constitutional.

- **[target]:** everything in the diagram — kernel, graph, evaluation
  engine, drawer, all four projections.
  - These are drafted contracts (RFC 0001/0002/0006), not running systems.
- **[Observed] today:** the surface charter and codenames are owner-ratified
  decisions (SDR §1–2).
  - The `.syzygy/` directory names (`intent/`, `work/`, `map/`) are fixed by
    adopted doctrine, though only `governance/` is populated in this
    repository.
- **[Observed]:** "Orrery includes historical state" rests on owner
  amendment **D1** — constitutional scope, no longer conditional.
  - Source: D1, ratified 2026-08-01, applied to
    `.syzygy/governance/doctrine/architecture.md`.
  - The concrete historical interaction design (ghost steps, milestone
    scenes, scrubber) remains a non-binding candidate bundle behind its own
    approval (RFC9-41).
