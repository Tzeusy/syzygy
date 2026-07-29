# Structural philosophy

Constitutional structure only. Load-bearing technical contracts — graph
schemas, adjudication and certificate semantics, execution profiles, deeper
`.syzygy/**` schemas — belong to RFCs.

## Governed projects and the two-namespace plane

A **governed project** is one or more repositories with **exactly one
designated governance root** — the repository containing the Project's single
`openspec/**` and `.syzygy/**` plane — and one owner, explicitly brought under
Syzygy observation. Additional repositories in the Project are declared
**observed-source repositories**: read-only to Syzygy unless separately
onboarded as governed projects. Onboarding is a recorded, per-repository
consent (security.md SEC-4) — **every observed repository consents, governed
root or not**. Syzygy governs an orthogonal, **in-tree** plane at the
governance root, and its
**direct project-content write authority is confined to exactly two
namespaces: `openspec/**` and `.syzygy/**`** (vision.md VIS-5). No governance
manifest, configuration, or convention may extend that direct-write universe.
Syzygy may *read* declared implementation and evidence sources anywhere in the
project; it may never directly create, modify, move, or delete project content
outside its two roots. Effects on every other authority — version-control
metadata, configured work-scheduler state, CI, runtime systems — occur only
through typed, explicitly authorized adapters (see typed authority); those
stores are never Syzygy-owned content namespaces. Changes in code materialize
only through workers executing scheduled work.

**Schema ownership differs between the two roots.** `openspec/**` is governed
by the constitutional OpenSpec artifact contract: Syzygy writes it only in
OpenSpec-compatible form and may not reorganize it for its own convenience —
the OpenSpec CLI implementation is a substitutable adapter, but the artifact
contract is not silently replaceable. `.syzygy/**` is Syzygy's **native,
schema-versioned namespace**: Syzygy owns and may migrate its organization
through explicit, reviewable, identity-preserving migrations.

### The `.syzygy/` namespace

Stable literal technical directories; the poetic names are UI codenames only:

```
governance_root/
├── openspec/            # behavioral requirements (OpenSpec artifact contract)
└── .syzygy/
    ├── project.yaml     # project declaration: identity, consents, declared
    │                    #   observed-source repositories (format: RFC material)
    ├── governance/      # shared kernel plane — minimum reserved categories:
    │   ├── doctrine/    #   adopted doctrine (this cluster)
    │   ├── contracts/   #   accepted load-bearing contracts (RFCs)
    │   ├── policies/    #   quality, evidence, and security policies
    │   └── decisions/   #   recorded owner decisions
    ├── intent/          # intent surface artifacts        (UI codename: Polaris)
    ├── work/            # work/convergence surface state  (UI codename: Trajectory)
    ├── map/             # semantic/spatial representation of observed, intended,
    │                    #   and proposed system state     (UI codename: Orrery)
    ├── cache/           # derived, rebuildable projections (VIS-6)
    └── local/           # personal presentation state (VIS-6a; never truth-bearing)
```

The four `governance/` categories above are **constitutional minimums**;
schemas and deeper organization beneath them — and the placement of
identities, promoted annotations, dismissals, and declared topology within
`governance/` — remain RFC material. `governance/` is the shared
cross-surface location: surfaces remain projections over one shared semantic
kernel and must not become independently authoritative.

Some **required Genome material lives inside the code tree** — explicitly
designated executable specifications and declared handcrafted regions (both
defined under Project Genome, below). Syzygy governs code-resident Genome
material by *reference and annotation only*, never by edit: marking a region
handcrafted, or a test authoritative, is a governance annotation in
`.syzygy/governance/`, not a code change. Handcrafted regions are an explicit
carve-out from the "code is a replaceable realization" claim — they must
survive regeneration.

On **offboarding**, the plane — `openspec/**` and the governance, intent,
work, and map portions of `.syzygy/**`, including committed-out annotations
and dismissals — stays with the repository; Syzygy exports the owner's
remaining personal state (`.syzygy/local/`), then deletes its projections
(`.syzygy/cache/` and any external ones). The plane is in-tree by explicit
owner ruling; the orphan-branch alternative was considered and **rejected**
(FD-034, resolving OQ-006).

## Typed authority

There is no single universal source of truth; authority is typed by question,
each role naming its current realization (all substitutable — see "adapters";
deeper `.syzygy/governance/` layout is RFC material):

| Question | Authority (location / initial substrate) |
|---|---|
| Why does the project exist? What principles govern it? | Doctrine in `.syzygy/governance/` |
| How do load-bearing technical contracts work? | Accepted contracts (RFCs) in `.syzygy/governance/` |
| What observable behavior is required? | The behavioral-requirements system (`openspec/`; initial substrate: OpenSpec) |
| Where do intended components and boundaries sit? | Declared topology in `.syzygy/governance/` |
| What quality and evidence standards apply? | Quality and evidence policy in `.syzygy/governance/` |
| What currently exists? | Code, tests, CI, runtime observations |
| What work is scheduled, and in what state? | The work-scheduling system (initial substrate: Beads) — reached only through its typed adapter |
| What does Syzygy display? | A rebuildable projection of all the above |

The work-scheduling system is authoritative for work lifecycle state, and the
version-control system (initial substrate: git) for version history; neither
is authoritative for intent or observed system behavior, and both are external
authorities Syzygy affects only through typed, explicitly authorized adapters
(VIS-5) — never Syzygy-owned content namespaces.

A **contradiction** is a set of authoritative claims in the same declared
scope that cannot simultaneously be satisfied — whether the claims come from
different typed authorities or from one. It renders the affected conclusion
Unknown, routes to adjudication (the owner), is never silently resolved by
precedence, and is never auto-scheduled into work. No surface may silently
pick a winner. A contradiction is distinct from a **gap** — compatible desired
state not yet realized in observed state: the intent-vs-observed,
work-generating delta (v1.md, V1 scope).

**Substrate tools are adapters, not doctrine**: the Genome is defined by the
*questions* it must answer, and any substrate satisfying those questions is
substitutable without doctrine amendment. (The one carve-out is stated above:
the `openspec/` *artifact contract* is constitutional even though the OpenSpec
CLI is not.)

## Project Genome

The **Project Genome** is the complete normative corpus — everything that must
survive deletion of the implementation. The behavioral-requirements system
holds its behavioral portion, not its whole: "regenerate from the
specification" must never collapse into "regenerate from behavioral scenarios
alone."

Verification material splits three ways, and the split is load-bearing for
regeneration, write authority, and offboarding:

- the **verification contract** — acceptance criteria, invariants,
  tests-as-spec obligations, and the required classes of proof: the normative
  statement of what must be verified. Always Genome.
- **explicitly designated executable specifications** — concrete tests a
  project deliberately marks as authoritative, non-regeneratable verification
  artifacts. Genome only by that designation; their *content*, not merely a
  path reference, must survive deletion of the implementation.
- **generated or implementation-coupled tests** — realization artifacts that
  may be regenerated. Never Genome.

Genome inventory, three tiers. **Universally required** — doctrine and
behavioral requirements; topology and quality policy; the verification
contract; a **handcrafted/non-regeneratable-region declaration, which may be
empty** — every region it lists is Genome. **Required when present** — no
project is obliged to create these, but once adopted they are Genome: accepted
load-bearing RFCs; explicitly designated executable specifications; generation
policy and provenance; normative data contracts and external service
contracts. **Not genome** — observed and generated artifacts (current schemas,
generated or implementation-coupled tests, migration plans), environment and
dependency locks (high-level technology standards are genome-worthy; lockfiles
are not), and operational/incident knowledge — **raw incident records are
evidence (trust-and-evidence.md), never Genome**; a durable lesson earns
Genome status only by being distilled into a normative artifact.

### Definitions (owned by doctrine, computed by the kernel)

These meanings change only by doctrine amendment:

- **Project**: one or more repositories with exactly one designated
  governance root (holding the Project's single `openspec/**` + `.syzygy/**`
  plane) and one owner; additional repositories are declared observed-source
  repositories, read-only to Syzygy unless separately onboarded. The
  `project.yaml` representation of this declaration is RFC material.
- **Capability**: a named unit of declared behavior that the project's own spec
  or shape documents assert exists, at the granularity a human would use to
  describe what the project does.
- **Aligned**: a scoped relation between **one observed subject and one cited
  normative claim, at one identified evaluation** — the subject satisfies that
  claim, with the evidence trail current at the evaluation's as-of instant.
- **Converged**: an **aggregate state over a declared target scope**, at one
  identified evaluation: every mandatory normative claim in scope is aligned;
  the realization is behaviorally equivalent under the declared verification
  oracle and compliant with the project's declared architecture, quality,
  performance, security, and evidence policies; no unresolved contradiction
  touches the scope; and no actionable gap remains open in it.
- **Genome-complete**: a claim about the **normative corpus itself** — every
  required Genome element is present, current, and traceable at the
  evaluation. It says nothing about runtime realization evidence (that is
  Aligned/Converged territory). Deliberately *not* named "mature": maturity is
  multidimensional — shape, verification, operational/battle-tested, and
  freshness axes among others — and may never be collapsed into one status;
  those axes, and any composite maturity rendering, belong to the graph/status
  RFC. (The `/th-projects` substrate's own "Mature" shape rating is one such
  axis, not this concept.)

Convergence claims are scoped to the declared oracle and must render the
oracle's declared coverage alongside them. Oracle **adequacy is assessed by a
human or by a deterministic measure declared in the project's quality policy
(`.syzygy/governance/`)**; an inferred adequacy judgment carries only
challenge authority (trust-and-evidence.md): it may conservatively suspend a
claim to Unknown, rendered with its inferred provenance, but may never raise
one toward converged. An oracle whose adequacy is unassessed yields Unknown.
Behavioral equivalence has known limits — model nondeterminism and environment
dependence — which convergence claims must not paper over.

Data contracts split three ways: **normative** (data meaning, invariants,
required relationships, privacy/retention obligations, compatibility promises,
migration safety) — Genome material; **observed** (current DDL, migration
history, indexes, volumes) — never enshrined in specs; **generated** (target
schemas, migration plans, adapters) — governance artifacts Syzygy may author
but never apply (VIS-5). The regeneration target is a realization that
satisfies the logical data contract and can safely migrate or adapt observed
state — never a byte-identical schema.

## Snapshots and the loop

The constitutional definition of a **snapshot** is a closed semantic rule: **a
snapshot identifies every deterministic input capable of affecting the
observed graph or a status claim.** Its representation — one tuple or a
composite of source, evidence, and policy snapshots — is RFC material. At
minimum it identifies, by version or hash: the repository and declared
working-tree state; governance artifacts; the work-state export; consumed test
and CI reports; the runtime observation dataset and window, when used;
observer, adapter, policy, and layout versions; and deterministic
configuration affecting parsing or classification. **A source not captured in
the snapshot must not influence its deterministic claims** — it renders
unavailable or Unknown instead.

**Time is an explicit input, never an ambient one.** A **status evaluation**
is identified by the pair (source snapshot, **as-of instant**); every
time-sensitive judgment — evidence currency, staleness, dismissal expiry — is
computed at the evaluation's as-of instant. A wall clock never silently
alters a displayed status: the passage of time changes a status only through
a new identified evaluation, and it may only degrade a claim (toward stale or
Unknown), never establish or improve one — **improvement requires a new
source snapshot containing a permitted authoritative input, such as new
evidence or an adjudication result**.

An **observation record** is the immutable result of one identified
evaluation and contains deterministic facts only. Determinism (VIS-7) is
asserted per identified evaluation, over the deterministic observed graph and
base layout — **including logical freshness state (fresh, stale, broken,
superseded), which changes status and is therefore identity-bearing**.
Excluded from the identity test is only display formatting — localized
timestamps and relative-age strings; extending that exclusion is a doctrine
amendment. The **inferred layer is a separate artifact**: it records the
model, version, and inputs that produced it, carries its own declared
reproducibility standard, is excluded from the VIS-7 identity test, and holds
no positive status authority — its bounded power to suspend a claim is
defined in trust-and-evidence.md.

The loop: intent → observation → gaps → reviewed work → fleet execution →
verification, with one upward arrow — verification and runtime evidence may
open spec-indictment gaps that route to the owner. The loop is
**human-triggered**: someone specs a desired shape, then deliberately triggers
a propagate/sync pass. Work-to-code and code-to-deployment belong to the
orchestration toolchain, outside Syzygy's body.

**Observation determinism and idempotence of authoritative effects are
constitutional; zero-token synchronization, cache reproducibility, and
byte-identical inference output are engineering goals** — craft and RFC
targets, sacrificial under VIS-1's rank 5, never doctrine. The idempotence
invariant, exactly: a pass over an unchanged, no-gap source snapshot — at any
as-of instant — must not mutate authoritative project artifacts, must not
create or reprioritize work, and must not establish or improve any status
claim (a later evaluation over the same snapshot may only degrade claims, per
the temporal rule above).

## One kernel, three surfaces

The kernel's shared semantics — the definitions above, materialized in
`.syzygy/governance/` — must never fork across surfaces, and surfaces are
never independently authoritative. The owner has ruled a **single repository
(monorepo)** the constitutional realization of that invariant (an explicit
founder decision; revisiting it is a doctrine amendment).

- **`intent/`** — the intent and comprehension surface (UI codename Polaris),
- **`work/`** — the gaps, work, and convergence surface (UI codename
  Trajectory),
- **`map/`** — the semantic/spatial representation of observed, intended, and
  proposed system state, including the spatial view (UI codename Orrery).

Surfaces are independently testable, navigable, feature-plannable, and — later,
if useful — deployable; they are projections over the one shared kernel.

The constitutional visualization requirement is a spatial comprehension surface
anchored to **capability identities, not file paths** — refactoring must not
randomly relocate the map, layout must be reproducible from the same snapshot —
with exact 2D/tabular equivalents always available. The concrete V0 rendering
mandate (3D) is scope, recorded in v1.md.

## Vocabulary

Technical nouns — project, capability, gap, contradiction, evidence, warrant,
aligned, converged, genome-complete, genome, snapshot, evaluation, observation
record — are frozen at adoption and stable for citation. "Mature" is
deliberately not frozen (see Genome-complete above). Poetic surface names
(Syzygy, Polaris, Trajectory, Orrery): adopting this doctrine ratifies them as
**working codenames only** — final product naming is a separate, later owner
decision; the technical directory names (`intent/`, `work/`, `map/`,
`governance/`) and technical domain names in APIs, schemas, and RFCs stay
literal.
