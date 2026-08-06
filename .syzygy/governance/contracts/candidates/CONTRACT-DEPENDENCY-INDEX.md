# Contract dependency index — derived, never authority

**Generated projection.** Rebuild with
`python3 scripts/build_dependency_index.py`; check for drift with
`--check`. **The modules win over this file, always.** Nothing here
is a clause and nothing here may be cited as authority (RFC11-7
rebuildable-projection rule).

## The three relations, and what a selector does with each

| Relation | Meaning | Source | Context Compiler behaviour |
|---|---|---|---|
| `depends_on` | A must be loaded to interpret or modify B correctly | **authored** on the dependent | **mandatory load**, transitively |
| `constrains` | A restricts something B owns; B stays independently readable | **authored** on the constraining contract | loaded **when the task class crosses the constrained seam** — editing B loads A's constraining clauses; otherwise not |
| `cites` | A refers to a clause of B for navigation, comparison, or a forward pointer | **derived** from a clause-reference scan | **never automatic**. Navigational evidence a human or an agent may follow; it enters no packet by itself |

`provides_to`, `constrained_by` and `cited_by` are the derived
inverses of the three and appear in no module's front matter. A
citation that is already a `depends_on` is recorded once, as the
stronger relation, and does not also appear under `cites`.

Coverage: **32 modules** across **11 contracts**.

## Contract-level graph — load obligations

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

## Contract-level graph — semantic constraints

A one-way restriction one contract places on something another owns.
These are the edges `depends_on` could not hold: they drive no load
obligation in the general case, and before this relation existed they
were stated in one contract, acknowledged by no clause in the other,
and enforced by neither (owner item **P-21(a)**).

| Contract | constrains | constrained_by |
|---|---|---|
| `RFC-0005` | — (none) | RFC-0006 |
| `RFC-0006` | RFC-0005 | — (none) |
| `RFC-0007` | — (none) | RFC-0008 |
| `RFC-0008` | RFC-0007 | — (none) |

## Contract-level graph — citations

Derived, never authored: contract A cites contract B where a module of
A references a clause `RFC<B>-n` in its body and A's `depends_on` does
not already carry B. **A citation is not a reliance.** Most of these
are forward references from a lower layer to the surface that consumes
it; turning them into dependencies would make the kernel depend on
everything, which is backwards. Whether any one of them is a genuine
missed dependency is owner item **P-21(b)**.

| Contract | cites | cited_by |
|---|---|---|
| `RFC-0001` | RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0009 | — (none) |
| `RFC-0002` | RFC-0006, RFC-0007 | RFC-0001 |
| `RFC-0003` | RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010 | RFC-0001, RFC-0006 |
| `RFC-0004` | RFC-0008 | RFC-0001, RFC-0010 |
| `RFC-0005` | — (none) | RFC-0001 |
| `RFC-0006` | RFC-0003, RFC-0009 | RFC-0001, RFC-0002, RFC-0003 |
| `RFC-0007` | — (none) | RFC-0002, RFC-0003, RFC-0010, RFC-0011 |
| `RFC-0008` | RFC-0009 | RFC-0003, RFC-0004 |
| `RFC-0009` | — (none) | RFC-0001, RFC-0003, RFC-0006, RFC-0008, RFC-0010, RFC-0011 |
| `RFC-0010` | RFC-0004, RFC-0007, RFC-0009 | RFC-0003 |
| `RFC-0011` | RFC-0007, RFC-0009 | — (none) |

## Module-level graph

One row per module file. `depends_on` is that file's own front matter;
`cites` is derived from that file's own body. A package README and its
sibling modules may declare different edges; both are reproduced,
neither is reconciled here.

| Module | Contract | depends_on | provides_to | cites |
|---|---|---|---|---|
| `rfcs/RFC-0001-project-graph-identity-state-planes.md` | `RFC-0001` | — (none) | RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0009 |
| `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | `RFC-0006` | RFC-0001, RFC-0002 | RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0003, RFC-0009 |
| `rfcs/RFC-0010-mission-control-autonomy.md` | `RFC-0010` | RFC-0001, RFC-0002, RFC-0003, RFC-0005, RFC-0006, RFC-0008 | RFC-0011 | RFC-0004, RFC-0007, RFC-0009 |
| `rfcs/RFC-0011-context-compiler.md` | `RFC-0011` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008, RFC-0010 | — (none) | RFC-0007, RFC-0009 |
| `rfcs/RFC-0002/README.md` | `RFC-0002` | RFC-0001, RFC-0003, RFC-0004, RFC-0005 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0007 |
| `rfcs/RFC-0002/challenge-lifecycle.md` | `RFC-0002` | RFC-0001, RFC-0003, RFC-0005 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0006 |
| `rfcs/RFC-0002/reconciliation-chain.md` | `RFC-0002` | RFC-0001, RFC-0004 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0006 |
| `rfcs/RFC-0002/rendering-vocabularies.md` | `RFC-0002` | RFC-0001, RFC-0005 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0006, RFC-0007 |
| `rfcs/RFC-0002/snapshot-and-evaluation-core.md` | `RFC-0002` | RFC-0001, RFC-0003, RFC-0005 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0003/README.md` | `RFC-0003` | RFC-0001, RFC-0002, RFC-0004, RFC-0005 | RFC-0002, RFC-0004, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | `RFC-0003` | RFC-0001, RFC-0002, RFC-0004, RFC-0005 | RFC-0002, RFC-0004, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0007, RFC-0008, RFC-0009, RFC-0010 |
| `rfcs/RFC-0003/manifests-and-namespace.md` | `RFC-0003` | RFC-0001, RFC-0002, RFC-0004, RFC-0005 | RFC-0002, RFC-0004, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0006, RFC-0007 |
| `rfcs/RFC-0004/README.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003, RFC-0005 | RFC-0002, RFC-0003, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0011 | — (none) |
| `rfcs/RFC-0004/execution-record.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003, RFC-0005 | RFC-0002, RFC-0003, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0011 | — (none) |
| `rfcs/RFC-0004/fidelity-joins-and-mappings.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003 | RFC-0002, RFC-0003, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0011 | RFC-0008 |
| `rfcs/RFC-0004/general-contract.md` | `RFC-0004` | RFC-0002, RFC-0003 | RFC-0002, RFC-0003, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0011 | — (none) |
| `rfcs/RFC-0004/named-adapters.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003, RFC-0005 | RFC-0002, RFC-0003, RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0011 | — (none) |
| `rfcs/RFC-0005/README.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003, RFC-0004 | RFC-0002, RFC-0003, RFC-0004, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0005/admission-and-boundary.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003 | RFC-0002, RFC-0003, RFC-0004, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0005/consent-egress-secrets.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003 | RFC-0002, RFC-0003, RFC-0004, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0005/execution-profiles.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003, RFC-0004 | RFC-0002, RFC-0003, RFC-0004, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0007/README.md` | `RFC-0007` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0009 | RFC-0008, RFC-0009 | — (none) |
| `rfcs/RFC-0007/narrative-contract.md` | `RFC-0007` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006 | RFC-0008, RFC-0009 | — (none) |
| `rfcs/RFC-0007/rendering-and-surface.md` | `RFC-0007` | RFC-0001, RFC-0003, RFC-0006, RFC-0009 | RFC-0008, RFC-0009 | — (none) |
| `rfcs/RFC-0008/README.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007 | RFC-0009, RFC-0010, RFC-0011 | RFC-0009 |
| `rfcs/RFC-0008/accounting-reconciliation-and-release.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006 | RFC-0009, RFC-0010, RFC-0011 | RFC-0009 |
| `rfcs/RFC-0008/identity-authority-materialization.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006, RFC-0007 | RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0008/state-vocabulary-and-cost.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006 | RFC-0009, RFC-0010, RFC-0011 | RFC-0009 |
| `rfcs/RFC-0009/README.md` | `RFC-0009` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008 | RFC-0007 | — (none) |
| `rfcs/RFC-0009/interaction-parity-and-release.md` | `RFC-0009` | RFC-0002, RFC-0006, RFC-0007, RFC-0008 | RFC-0007 | — (none) |
| `rfcs/RFC-0009/semantic-geography.md` | `RFC-0009` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006 | RFC-0007 | — (none) |
| `rfcs/RFC-0009/visual-grammar-and-lenses.md` | `RFC-0009` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008 | RFC-0007 | — (none) |

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
