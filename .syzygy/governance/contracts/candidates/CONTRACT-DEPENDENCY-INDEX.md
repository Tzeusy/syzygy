# Contract dependency index — derived, never authority

**Generated projection.** Rebuild with
`python3 scripts/build_dependency_index.py`; check for drift with
`--check`. Every row restates the `depends_on` / `provides_to` /
`applies_to` front matter of the active contract modules under `rfcs/`.
**The modules win over this file, always.** Nothing here is a clause,
nothing here may be cited as authority, and no edge appears here that a
module does not declare — the generator reads edges, it never infers
them (charter §11.5; RFC11-7 rebuildable-projection rule).

Coverage: **32 modules** across **11 contracts**.

## Contract-level graph

One row per contract: the union of its modules' declared edges.

| Contract | Title | applies_to | depends_on | provides_to |
|---|---|---|---|---|
| `RFC-0001` | Project Graph, Identity and State Planes | all-surfaces, kernel | — (none) | RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0002` | Observation, Evaluation and Reconciliation — contract package index | all-surfaces, kernel | RFC-0001, RFC-0003, RFC-0004, RFC-0005 | RFC-0003, RFC-0004, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0003` | Project, Workspace and .syzygy/** Manifests — contract package index | all-surfaces, kernel, workspace | RFC-0001, RFC-0002 | RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0004` | Observation Sources, Evidence, Execution Records and Adapters — contract package index | kernel, orrery, trajectory | RFC-0001, RFC-0002, RFC-0003, RFC-0005 | RFC-0003, RFC-0005, RFC-0008, RFC-0009, RFC-0011 |
| `RFC-0005` | Authentication, Consent and Execution Profiles — contract package index | all-surfaces, kernel, machine-clients | RFC-0001, RFC-0002, RFC-0003, RFC-0004 | RFC-0002, RFC-0003, RFC-0004, RFC-0006, RFC-0008, RFC-0010, RFC-0011 |
| `RFC-0006` | Cross-Surface Selection, Query and Evidence Drawer | all-surfaces, kernel, machine-clients | RFC-0001, RFC-0002 | RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0007` | Polaris (Intent Surface) — contract package index | polaris | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006 | RFC-0008, RFC-0009 |
| `RFC-0008` | Trajectory (Work Surface) — contract package index | trajectory | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006 | RFC-0007, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0009` | Orrery (Map Surface) — contract package index | machine-clients, orrery | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008 | RFC-0007, RFC-0008, RFC-0010, RFC-0011 |
| `RFC-0010` | Mission Control and Autonomy Envelopes | all-surfaces, machine-clients, mission-control, workspace | RFC-0001, RFC-0002, RFC-0003, RFC-0005, RFC-0006, RFC-0008 | RFC-0011 |
| `RFC-0011` | Context Compiler and Governed Context Packets | all-surfaces, context, machine-clients, mission-control | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0010 | — (none) |

## Module-level graph

One row per module file, as declared in that file's own front matter.
A package README and its sibling modules may declare different edges;
both are reproduced, neither is reconciled here.

| Module | Contract | depends_on | provides_to |
|---|---|---|---|
| `rfcs/RFC-0001-project-graph-identity-state-planes.md` | `RFC-0001` | — (none) | RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | `RFC-0006` | RFC-0001, RFC-0002 | RFC-0005, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0010-mission-control-autonomy.md` | `RFC-0010` | RFC-0001, RFC-0002, RFC-0003, RFC-0005, RFC-0006, RFC-0008 | RFC-0011 |
| `rfcs/RFC-0011-context-compiler.md` | `RFC-0011` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0010 | — (none) |
| `rfcs/RFC-0002/README.md` | `RFC-0002` | RFC-0001, RFC-0003, RFC-0004, RFC-0005 | RFC-0003, RFC-0004, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0002/challenge-lifecycle.md` | `RFC-0002` | RFC-0001, RFC-0003, RFC-0005 | RFC-0003, RFC-0006, RFC-0007, RFC-0008, RFC-0009 |
| `rfcs/RFC-0002/reconciliation-chain.md` | `RFC-0002` | RFC-0001, RFC-0004 | RFC-0003, RFC-0004, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0002/rendering-vocabularies.md` | `RFC-0002` | RFC-0001, RFC-0005 | RFC-0003, RFC-0004, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0002/snapshot-and-evaluation-core.md` | `RFC-0002` | RFC-0001, RFC-0003, RFC-0005 | RFC-0003, RFC-0004, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0003/README.md` | `RFC-0003` | RFC-0001, RFC-0002 | RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | `RFC-0003` | RFC-0001, RFC-0002 | RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0003/manifests-and-namespace.md` | `RFC-0003` | RFC-0001, RFC-0002 | RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009 |
| `rfcs/RFC-0004/README.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003, RFC-0005 | RFC-0003, RFC-0005, RFC-0008, RFC-0009, RFC-0011 |
| `rfcs/RFC-0004/execution-record.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003, RFC-0005 | RFC-0003, RFC-0005, RFC-0008, RFC-0011 |
| `rfcs/RFC-0004/fidelity-joins-and-mappings.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003 | RFC-0003, RFC-0008, RFC-0009, RFC-0011 |
| `rfcs/RFC-0004/general-contract.md` | `RFC-0004` | RFC-0002, RFC-0003 | RFC-0003, RFC-0011 |
| `rfcs/RFC-0004/named-adapters.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003, RFC-0005 | RFC-0008, RFC-0011 |
| `rfcs/RFC-0005/README.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003, RFC-0004 | RFC-0002, RFC-0003, RFC-0004, RFC-0006, RFC-0008, RFC-0010, RFC-0011 |
| `rfcs/RFC-0005/admission-and-boundary.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003 | RFC-0002, RFC-0003, RFC-0004, RFC-0006, RFC-0008, RFC-0010, RFC-0011 |
| `rfcs/RFC-0005/consent-egress-secrets.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003 | RFC-0002, RFC-0003, RFC-0004, RFC-0006, RFC-0008, RFC-0010, RFC-0011 |
| `rfcs/RFC-0005/execution-profiles.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003, RFC-0004 | RFC-0002, RFC-0003, RFC-0004, RFC-0010 |
| `rfcs/RFC-0007/README.md` | `RFC-0007` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006 | RFC-0008, RFC-0009 |
| `rfcs/RFC-0007/narrative-contract.md` | `RFC-0007` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006 | RFC-0008 |
| `rfcs/RFC-0007/rendering-and-surface.md` | `RFC-0007` | RFC-0001, RFC-0003, RFC-0006 | RFC-0009 |
| `rfcs/RFC-0008/README.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006 | RFC-0007, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0008/accounting-reconciliation-and-release.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006 | RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0008/identity-authority-materialization.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006 | RFC-0007, RFC-0010 |
| `rfcs/RFC-0008/state-vocabulary-and-cost.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006 | RFC-0009, RFC-0010 |
| `rfcs/RFC-0009/README.md` | `RFC-0009` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008 | RFC-0007, RFC-0008, RFC-0010, RFC-0011 |
| `rfcs/RFC-0009/interaction-parity-and-release.md` | `RFC-0009` | RFC-0002, RFC-0006, RFC-0008 | RFC-0007, RFC-0008, RFC-0010, RFC-0011 |
| `rfcs/RFC-0009/semantic-geography.md` | `RFC-0009` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006 | RFC-0007, RFC-0008 |
| `rfcs/RFC-0009/visual-grammar-and-lenses.md` | `RFC-0009` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008 | RFC-0007, RFC-0008 |

## Graph consistency

`depends_on` and `provides_to` are two independently authored views of
the same edge set, so they can disagree. Each disagreement below is
**reported, not repaired**: adding the missing half would be inventing
an edge no module declares, and removing the stated half would delete
one. Resolving them is an edit to the modules' front matter, and
belongs to whoever owns those modules.

**20 asymmetric or dangling edges** at generation:

| From | To | Declared on | Disagreement |
|---|---|---|---|
| `RFC-0002` | `RFC-0003` | `depends_on` | `RFC-0002.depends_on` names RFC-0003, but `RFC-0003.provides_to` does not name RFC-0002 |
| `RFC-0002` | `RFC-0004` | `depends_on` | `RFC-0002.depends_on` names RFC-0004, but `RFC-0004.provides_to` does not name RFC-0002 |
| `RFC-0003` | `RFC-0006` | `provides_to` | `RFC-0003.provides_to` names RFC-0006, but `RFC-0006.depends_on` does not name RFC-0003 |
| `RFC-0004` | `RFC-0003` | `provides_to` | `RFC-0004.provides_to` names RFC-0003, but `RFC-0003.depends_on` does not name RFC-0004 |
| `RFC-0005` | `RFC-0002` | `depends_on` | `RFC-0005.depends_on` names RFC-0002, but `RFC-0002.provides_to` does not name RFC-0005 |
| `RFC-0005` | `RFC-0003` | `provides_to` | `RFC-0005.provides_to` names RFC-0003, but `RFC-0003.depends_on` does not name RFC-0005 |
| `RFC-0005` | `RFC-0006` | `provides_to` | `RFC-0005.provides_to` names RFC-0006, but `RFC-0006.depends_on` does not name RFC-0005 |
| `RFC-0006` | `RFC-0005` | `provides_to` | `RFC-0006.provides_to` names RFC-0005, but `RFC-0005.depends_on` does not name RFC-0006 |
| `RFC-0006` | `RFC-0011` | `provides_to` | `RFC-0006.provides_to` names RFC-0011, but `RFC-0011.depends_on` does not name RFC-0006 |
| `RFC-0007` | `RFC-0004` | `depends_on` | `RFC-0007.depends_on` names RFC-0004, but `RFC-0004.provides_to` does not name RFC-0007 |
| `RFC-0007` | `RFC-0005` | `depends_on` | `RFC-0007.depends_on` names RFC-0005, but `RFC-0005.provides_to` does not name RFC-0007 |
| `RFC-0007` | `RFC-0008` | `provides_to` | `RFC-0007.provides_to` names RFC-0008, but `RFC-0008.depends_on` does not name RFC-0007 |
| `RFC-0007` | `RFC-0009` | `provides_to` | `RFC-0007.provides_to` names RFC-0009, but `RFC-0009.depends_on` does not name RFC-0007 |
| `RFC-0008` | `RFC-0007` | `provides_to` | `RFC-0008.provides_to` names RFC-0007, but `RFC-0007.depends_on` does not name RFC-0008 |
| `RFC-0008` | `RFC-0011` | `provides_to` | `RFC-0008.provides_to` names RFC-0011, but `RFC-0011.depends_on` does not name RFC-0008 |
| `RFC-0009` | `RFC-0005` | `depends_on` | `RFC-0009.depends_on` names RFC-0005, but `RFC-0005.provides_to` does not name RFC-0009 |
| `RFC-0009` | `RFC-0007` | `provides_to` | `RFC-0009.provides_to` names RFC-0007, but `RFC-0007.depends_on` does not name RFC-0009 |
| `RFC-0009` | `RFC-0008` | `provides_to` | `RFC-0009.provides_to` names RFC-0008, but `RFC-0008.depends_on` does not name RFC-0009 |
| `RFC-0009` | `RFC-0010` | `provides_to` | `RFC-0009.provides_to` names RFC-0010, but `RFC-0010.depends_on` does not name RFC-0009 |
| `RFC-0009` | `RFC-0011` | `provides_to` | `RFC-0009.provides_to` names RFC-0011, but `RFC-0011.depends_on` does not name RFC-0009 |

The contract graph is **not acyclic** — mutual edges between kernel
contracts are declared deliberately (a contract can both rely on and
feed another). Read it as a reference graph for context selection, not
as a build order.
