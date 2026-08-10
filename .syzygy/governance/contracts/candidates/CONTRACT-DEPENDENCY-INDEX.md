# Contract dependency index — derived, never authority

**Generated projection.** Rebuild with
`python3 scripts/build_dependency_index.py`; check for drift with
`--check`. **The modules win over this file, always.** Nothing here
is a clause and nothing here may be cited as authority (RFC11-7
rebuildable-projection rule).

## The three relations

| Relation | Meaning | Source of truth |
|---|---|---|
| `depends_on` | A must be loaded to interpret or modify B correctly | **authored** on the dependent |
| `constrains` | A restricts something B owns; B stays independently readable | **authored** on the constraining contract, anchored to a clause of it |
| `cites` | A refers to a clause of B for navigation, comparison, or a forward pointer | **derived** from a clause-reference scan |

**What a selector should do with each is deliberately not stated
here.** An earlier revision of this file carried a "Context Compiler
behaviour" column — mandatory-load, load-on-seam-crossing,
never-automatic — and **no clause states any of it**. A binding
selector rule homed in a file whose own banner reads *nothing here may
be cited as authority* is the defect this package keeps re-acquiring,
appearing inside the repair for it (review RD-4, finding F-15).

The proposal lives in `round-2026-08c/RELATION-MODEL-DECISION.md`,
marked as a proposal. Its home if adopted is **RFC11-4**, which
enumerates the deterministic selection inputs today and names
`depends_on` / `provides_to` and clause-level metadata — and does
**not** name `constrains`. Until that clause changes, a conformant
compiler would not read this relation at all.

`provides_to`, `constrained_by` and `cited_by` are the derived
inverses of the three and appear in no module's front matter. A
citation that is already a `depends_on` is recorded once, as the
stronger relation, and does not also appear under `cites`.

Coverage: **39 modules** across **11 contracts**.

## Contract-level graph — load obligations

One row per contract: the union of its modules' declared edges.

| Contract | Title | applies_to | depends_on | provides_to |
|---|---|---|---|---|
| `RFC-0001` | Project Graph, Identity and State Planes | all-surfaces, kernel | — (none) | RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0002` | Observation, Evaluation and Reconciliation — contract package index | all-surfaces, kernel | RFC-0001, RFC-0003, RFC-0004, RFC-0005 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0003` | Project, Workspace and .syzygy/** Manifests — contract package index | all-surfaces, kernel, workspace | RFC-0001, RFC-0002, RFC-0005 | RFC-0002, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0004` | Observation Sources, Evidence, Execution Records and Adapters — contract package index | kernel, orrery, trajectory | RFC-0001, RFC-0002, RFC-0003, RFC-0005 | RFC-0002, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0005` | Authentication, Consent and Execution Profiles — contract package index | all-surfaces, kernel, machine-clients | RFC-0001, RFC-0002, RFC-0003, RFC-0004 | RFC-0002, RFC-0003, RFC-0004, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0006` | Cross-Surface Selection, Query and Evidence Drawer | all-surfaces, kernel, machine-clients | RFC-0001, RFC-0002, RFC-0003, RFC-0004 | RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0007` | Polaris (Intent Surface) — contract package index | polaris | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0009 | RFC-0008, RFC-0009 |
| `RFC-0008` | Trajectory (Work Surface) — contract package index | trajectory | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007 | RFC-0009, RFC-0010, RFC-0011 |
| `RFC-0009` | Orrery (Map Surface) — contract package index | machine-clients, orrery | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008 | RFC-0007 |
| `RFC-0010` | Mission Control and Autonomy Envelopes — contract package index | all-surfaces, machine-clients, mission-control, workspace | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008 | RFC-0011 |
| `RFC-0011` | Context Compiler and Governed Context Packets — contract package index | all-surfaces, context, machine-clients, mission-control | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008, RFC-0010 | — (none) |

## Contract-level graph — semantic constraints

A one-way restriction one contract places on something another owns —
**anchored to a clause of the constraining contract**, which is
verified below rather than asserted here.

These are edges `depends_on` cannot hold: they drive no load
obligation in the general case. What they have in common is that the
restricting text names what *other* contracts may do, and the
constrained contract does not carry it (owner item **P-21(a)**).

**Two things this table does not claim.** It does not claim the
constrained contract is silent — RFC-0007 states the SDR-18 seam in
RFC7-24 from its own authority, and an earlier revision of this
sentence generalised across every row and was false for one of them.
And it does not claim to be complete: the population was found by two
Python `re` sweeps over whole-file text (line-based and
whitespace-normalised) for restriction-shaped clause language, and a
sweep by the party that authored the edges is the weakest evidence in
this repository. **[Unknown]** whether a third edge exists.

An edge marked **(load-covered)** is one where the constrained
contract already declares `depends_on` the constraining one, so it
loads it regardless and the constraint is discharged by the
stronger relation. The unmarked edges are the whole reason this
relation exists.

| Contract | constrains | anchored at | constrained_by |
|---|---|---|---|
| `RFC-0001` | — (none) | — | RFC-0007 |
| `RFC-0002` | — (none) | — | RFC-0007 |
| `RFC-0004` | — (none) | — | RFC-0007 |
| `RFC-0005` | RFC-0006, RFC-0009 *(load-covered)*, RFC-0010 *(load-covered)*, RFC-0011 *(load-covered)* | `RFC5-3` | — (none) |
| `RFC-0006` | — (none) | — | RFC-0005 |
| `RFC-0007` | RFC-0001, RFC-0002, RFC-0004, RFC-0008 *(load-covered)* | `RFC7-3` | — (none) |
| `RFC-0008` | — (none) | — | RFC-0007 |
| `RFC-0009` | — (none) | — | RFC-0005 |
| `RFC-0010` | — (none) | — | RFC-0005 |
| `RFC-0011` | — (none) | — | RFC-0005 |

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
| `RFC-0001` | RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `RFC-0002` | RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0001 |
| `RFC-0003` | RFC-0004, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0001 |
| `RFC-0004` | RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0001, RFC-0003 |
| `RFC-0005` | RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0001 |
| `RFC-0006` | RFC-0008, RFC-0009 | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005 |
| `RFC-0007` | — (none) | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0010, RFC-0011 |
| `RFC-0008` | RFC-0009 | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006 |
| `RFC-0009` | RFC-0010 | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008, RFC-0010, RFC-0011 |
| `RFC-0010` | RFC-0007, RFC-0009 | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0009 |
| `RFC-0011` | RFC-0007, RFC-0009 | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005 |

## Module-level graph

One row per module file. `depends_on` is that file's own front matter;
`cites` is derived from that file's own body. A package README and its
sibling modules may declare different edges; both are reproduced,
neither is reconciled here.

| Module | Contract | depends_on | provides_to | cites |
|---|---|---|---|---|
| `rfcs/RFC-0001-project-graph-identity-state-planes.md` | `RFC-0001` | — (none) | RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | `RFC-0006` | RFC-0001, RFC-0002, RFC-0003, RFC-0004 | RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0008, RFC-0009 |
| `rfcs/RFC-0002/README.md` | `RFC-0002` | RFC-0001, RFC-0003, RFC-0004, RFC-0005 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0007 |
| `rfcs/RFC-0002/challenge-lifecycle.md` | `RFC-0002` | RFC-0001, RFC-0003, RFC-0005 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0006 |
| `rfcs/RFC-0002/reconciliation-chain.md` | `RFC-0002` | RFC-0001, RFC-0004 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0006, RFC-0008 |
| `rfcs/RFC-0002/rendering-vocabularies.md` | `RFC-0002` | RFC-0001, RFC-0003, RFC-0005 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0002/snapshot-and-evaluation-core.md` | `RFC-0002` | RFC-0001, RFC-0003, RFC-0005 | RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0006 |
| `rfcs/RFC-0003/README.md` | `RFC-0003` | RFC-0001, RFC-0002, RFC-0005 | RFC-0002, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | `RFC-0003` | RFC-0001, RFC-0002, RFC-0005 | RFC-0002, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0004, RFC-0007, RFC-0008, RFC-0009, RFC-0010 |
| `rfcs/RFC-0003/manifests-and-namespace.md` | `RFC-0003` | RFC-0001, RFC-0002, RFC-0005 | RFC-0002, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0004, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0004/README.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003, RFC-0005 | RFC-0002, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0004/execution-record.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003, RFC-0005 | RFC-0002, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0004/fidelity-joins-and-mappings.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003 | RFC-0002, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0004/general-contract.md` | `RFC-0004` | RFC-0002, RFC-0003 | RFC-0002, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0004/named-adapters.md` | `RFC-0004` | RFC-0001, RFC-0002, RFC-0003, RFC-0005 | RFC-0002, RFC-0005, RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0005/README.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003, RFC-0004 | RFC-0002, RFC-0003, RFC-0004, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0005/admission-and-boundary.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003 | RFC-0002, RFC-0003, RFC-0004, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 |
| `rfcs/RFC-0005/consent-egress-secrets.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003 | RFC-0002, RFC-0003, RFC-0004, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0005/execution-profiles.md` | `RFC-0005` | RFC-0001, RFC-0002, RFC-0003, RFC-0004 | RFC-0002, RFC-0003, RFC-0004, RFC-0007, RFC-0008, RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0007/README.md` | `RFC-0007` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0009 | RFC-0008, RFC-0009 | — (none) |
| `rfcs/RFC-0007/narrative-contract.md` | `RFC-0007` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006 | RFC-0008, RFC-0009 | — (none) |
| `rfcs/RFC-0007/rendering-and-surface.md` | `RFC-0007` | RFC-0001, RFC-0002, RFC-0003, RFC-0006, RFC-0009 | RFC-0008, RFC-0009 | — (none) |
| `rfcs/RFC-0008/README.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007 | RFC-0009, RFC-0010, RFC-0011 | RFC-0009 |
| `rfcs/RFC-0008/accounting-reconciliation-and-release.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007 | RFC-0009, RFC-0010, RFC-0011 | RFC-0009 |
| `rfcs/RFC-0008/identity-authority-materialization.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006, RFC-0007 | RFC-0009, RFC-0010, RFC-0011 | — (none) |
| `rfcs/RFC-0008/state-vocabulary-and-cost.md` | `RFC-0008` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006 | RFC-0009, RFC-0010, RFC-0011 | RFC-0009 |
| `rfcs/RFC-0009/README.md` | `RFC-0009` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008 | RFC-0007 | — (none) |
| `rfcs/RFC-0009/interaction-parity-and-release.md` | `RFC-0009` | RFC-0001, RFC-0002, RFC-0003, RFC-0006, RFC-0007, RFC-0008 | RFC-0007 | — (none) |
| `rfcs/RFC-0009/semantic-geography.md` | `RFC-0009` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006 | RFC-0007 | RFC-0010 |
| `rfcs/RFC-0009/visual-grammar-and-lenses.md` | `RFC-0009` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008 | RFC-0007 | — (none) |
| `rfcs/RFC-0010/README.md` | `RFC-0010` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008 | RFC-0011 | — (none) |
| `rfcs/RFC-0010/budget-reservation.md` | `RFC-0010` | RFC-0002, RFC-0004, RFC-0005, RFC-0008 | RFC-0011 | — (none) |
| `rfcs/RFC-0010/effects-recovery-and-stop.md` | `RFC-0010` | RFC-0002, RFC-0003, RFC-0004, RFC-0005 | RFC-0011 | — (none) |
| `rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md` | `RFC-0010` | RFC-0001, RFC-0002, RFC-0003, RFC-0005, RFC-0006, RFC-0008 | RFC-0011 | RFC-0007, RFC-0009 |
| `rfcs/RFC-0010/portfolio-and-cross-project-consent.md` | `RFC-0010` | RFC-0003, RFC-0005 | RFC-0011 | — (none) |
| `rfcs/RFC-0010/prevention-envelope-and-attention.md` | `RFC-0010` | RFC-0001, RFC-0002, RFC-0003, RFC-0005, RFC-0008 | RFC-0011 | — (none) |
| `rfcs/RFC-0011/README.md` | `RFC-0011` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008, RFC-0010 | — (none) | — (none) |
| `rfcs/RFC-0011/deterministic-selection-and-budget.md` | `RFC-0011` | RFC-0002, RFC-0010 | — (none) | — (none) |
| `rfcs/RFC-0011/packet-identity-provenance-and-memory.md` | `RFC-0011` | RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008, RFC-0010 | — (none) | RFC-0007, RFC-0009 |

## Graph consistency

**The graph is closed by construction.** `depends_on` is the single
authored direction; `provides_to` is derived by reversing it and
appears in no module's front matter. The two therefore cannot
disagree — the asymmetric edges this section used to report were not
a data-entry problem but a consequence of maintaining both
directions by hand. Their count, as measured at rev10, and their
per-edge dispositions are recorded in
`round-2026-08b/DEPENDENCY-CLOSURE-REPORT.md`; this file does not
restate a figure it cannot recompute.

What remains checkable is **dangling** edges: a declared dependency
on a contract with no module in this package.

**No dangling edges** at generation: every contract named by a
`depends_on` has at least one module in this package (11 contracts resolved).

### Reported, not a defect: `A constrains B` where `A depends_on B`

Both relations can be genuinely true of one pair. They are also
the exact shape of a constraint read off a dependency rather than
found in a clause, which is how the first misdirected edge in this
corpus was declared. Printed so it is re-examined; it fails
nothing.

- `RFC-0007` constrains `RFC-0001`, and also depends on it
- `RFC-0007` constrains `RFC-0002`, and also depends on it
- `RFC-0007` constrains `RFC-0004`, and also depends on it

The contract graph is **not acyclic** — mutual edges between kernel
contracts are declared deliberately (a contract can both rely on and
feed another). Read it as a reference graph for context selection, not
as a build order.
