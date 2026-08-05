# Contract dependency index — derived, never authority

**Generated projection.** Rebuild with
`python3 scripts/build_dependency_index.py`; check for drift with
`--check`. Every `depends_on` and `applies_to` cell restates the
front matter of the active contract modules under `rfcs/`; every
`provides_to` cell is **derived** by reversing `depends_on`.
**The modules win over this file, always.** Nothing here is a clause
and nothing here may be cited as authority. No `depends_on` edge
appears that a module does not declare, and no `provides_to` edge
appears that is not the exact reverse of one (charter §11.5; RFC11-7
rebuildable-projection rule).

Coverage: **32 modules** across **11 contracts**.

## Contract-level graph

One row per contract: the union of its modules' declared edges.

| Contract | Title | applies_to | depends_on | provides_to |
|---|---|---|---|---|
| `RFC-0001` | Project Graph, Identity and State Planes | all-surfaces, kernel | — (none) | RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0002` | Observation, Evaluation and Reconciliation — contract package index | all-surfaces, kernel | RFC-0001, RFC-0003, RFC-0004, RFC-0005 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0003` | Project, Workspace and .syzygy/** Manifests — contract package index | all-surfaces, kernel, workspace | RFC-0001, RFC-0002, RFC-0004, RFC-0005 | RFC-0002, RFC-0004, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0004` | Observation Sources, Evidence, Execution Records and Adapters — contract package index | kernel, orrery, trajectory | RFC-0001, RFC-0002, RFC-0003, RFC-0005 | RFC-0002, RFC-0003, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0011 |
| `RFC-0005` | Authentication, Consent and Execution Profiles — contract package index | all-surfaces, kernel, machine-clients | RFC-0001, RFC-0002, RFC-0003, RFC-0004 | RFC-0002, RFC-0003, RFC-0004, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0006` | Cross-Surface Selection, Query and Evidence Drawer | all-surfaces, kernel, machine-clients | RFC-0001, RFC-0002 | RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0007` | Polaris (Intent Surface) — contract package index | polaris | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0009 | RFC-0008, RFC-0009 |
| `RFC-0008` | Trajectory (Work Surface) — contract package index | trajectory | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007 | RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0009` | Orrery (Map Surface) — contract package index | machine-clients, orrery | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008 | RFC-0007 |
| `RFC-0010` | Mission Control and Autonomy Envelopes | all-surfaces, machine-clients, mission-control, workspace | RFC-0001, RFC-0002, RFC-0003, RFC-0005, RFC-0006, RFC-0008 | RFC-0011 |
| `RFC-0011` | Context Compiler and Governed Context Packets | all-surfaces, context, machine-clients, mission-control | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008, RFC-0010 | — (none) |

## Module-level graph

One row per module file, as declared in that file's own front matter.
A package README and its sibling modules may declare different edges;
both are reproduced, neither is reconciled here.

| Module | Contract | depends_on | provides_to |
|---|---|---|---|
| `rfcs/RFC-0001-project-graph-identity-state-planes.md` | `RFC-0001` | — (none) | RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | `RFC-0006` | RFC-0001, RFC-0002 | RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0010-mission-control-autonomy.md` | `RFC-0010` | RFC-0001, RFC-0002, RFC-0003, RFC-0005, RFC-0006, RFC-0008 | RFC-0011 |
| `rfcs/RFC-0011-context-compiler.md` | `RFC-0011` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008, RFC-0010 | — (none) |
| `rfcs/RFC-0002/README.md` | `RFC-0002` | RFC-0001, RFC-0003, RFC-0004, RFC-0005 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0002/challenge-lifecycle.md` | `RFC-0002` | RFC-0001, RFC-0003, RFC-0005 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0002/reconciliation-chain.md` | `RFC-0002` | RFC-0001, RFC-0004 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0002/rendering-vocabularies.md` | `RFC-0002` | RFC-0001, RFC-0005 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0002/snapshot-and-evaluation-core.md` | `RFC-0002` | RFC-0001, RFC-0003, RFC-0005 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0003/README.md` | `RFC-0003` | RFC-0001, RFC-0002, RFC-0004, RFC-0005 | RFC-0002, RFC-0004, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | `RFC-0003` | RFC-0001, RFC-0002, RFC-0004, RFC-0005 | RFC-0002, RFC-0004, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0003/manifests-and-namespace.md` | `RFC-0003` | RFC-0001, RFC-0002, RFC-0004, RFC-0005 | RFC-0002, RFC-0004, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0004/README.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003, RFC-0005 | RFC-0002, RFC-0003, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0011 |
| `rfcs/RFC-0004/execution-record.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003, RFC-0005 | RFC-0002, RFC-0003, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0011 |
| `rfcs/RFC-0004/fidelity-joins-and-mappings.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003 | RFC-0002, RFC-0003, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0011 |
| `rfcs/RFC-0004/general-contract.md` | `RFC-0004` | RFC-0002, RFC-0003 | RFC-0002, RFC-0003, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0011 |
| `rfcs/RFC-0004/named-adapters.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003, RFC-0005 | RFC-0002, RFC-0003, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0011 |
| `rfcs/RFC-0005/README.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003, RFC-0004 | RFC-0002, RFC-0003, RFC-0004, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0005/admission-and-boundary.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003 | RFC-0002, RFC-0003, RFC-0004, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0005/consent-egress-secrets.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003 | RFC-0002, RFC-0003, RFC-0004, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0005/execution-profiles.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003, RFC-0004 | RFC-0002, RFC-0003, RFC-0004, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0007/README.md` | `RFC-0007` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0009 | RFC-0008, RFC-0009 |
| `rfcs/RFC-0007/narrative-contract.md` | `RFC-0007` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006 | RFC-0008, RFC-0009 |
| `rfcs/RFC-0007/rendering-and-surface.md` | `RFC-0007` | RFC-0001, RFC-0003, RFC-0006, RFC-0009 | RFC-0008, RFC-0009 |
| `rfcs/RFC-0008/README.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007 | RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0008/accounting-reconciliation-and-release.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006 | RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0008/identity-authority-materialization.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006, RFC-0007 | RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0008/state-vocabulary-and-cost.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006 | RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0009/README.md` | `RFC-0009` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008 | RFC-0007 |
| `rfcs/RFC-0009/interaction-parity-and-release.md` | `RFC-0009` | RFC-0002, RFC-0006, RFC-0007, RFC-0008 | RFC-0007 |
| `rfcs/RFC-0009/semantic-geography.md` | `RFC-0009` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006 | RFC-0007 |
| `rfcs/RFC-0009/visual-grammar-and-lenses.md` | `RFC-0009` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008 | RFC-0007 |

## Graph consistency

**The graph is closed by construction.** `depends_on` is the single
authored direction; `provides_to` is derived by reversing it and
appears in no module's front matter. The two therefore cannot
disagree — the 20 asymmetric edges this section used to report were
not a data-entry problem but a consequence of maintaining both
directions by hand. Their per-edge dispositions are recorded in
`round-2026-08b/DEPENDENCY-CLOSURE-REPORT.md`.

What remains checkable is **dangling** edges: a declared dependency
on a contract with no module in this package.

**No dangling edges** at generation: every contract named by a
`depends_on` has at least one module in this package (11 contracts resolved).

The contract graph is **not acyclic** — mutual edges between kernel
contracts are declared deliberately (a contract can both rely on and
feed another). Read it as a reference graph for context selection, not
as a build order.
