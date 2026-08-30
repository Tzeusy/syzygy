## Context

The current shared model contains one manually selected WhatsApp capability.
Polaris faithfully renders that small model, but the owner walkthrough showed
that this does not explain Butlers. See `proposal.md` and
`docs/reviews/R-POC-OWNER-WALKTHROUGH-POLARIS.md`.

Butlers already declares its project shape through the five-pillar index in
its about/README.md, with roster identity below it. The sources
are rich enough for a project account but are not perfectly consistent. For
example, the Butlers about/README.md says there are eight domain butlers while
its about/heart-and-soul/v1.md declares nine. Polaris must expose that conflict
instead of choosing whichever value is easier to render.

## Goals / Non-Goals

**Goals:**

- Build a revision-bound, deterministic model of all declared Butlers project
  shape.
- Give Polaris a project-level entry with capability drill-down.
- Make omissions and contradictions visible with reconciling denominators.
- Use short headings and direct project language.
- Retain the existing provenance, Unknown, parity and accessibility floors.

**Non-Goals:**

- Semantic indexing of every source file.
- LLM generation or inference at observation or render time.
- Treating every open proposal as current project truth.
- Writing or repairing Butlers artifacts.
- Generalizing this POC adapter to a second project.

## Decisions

### 1. Observe the declared shape, not the whole filesystem

The source population starts from Butlers' own about/README.md five-pillar
index and the roster identity rule it declares. The observer reads only
allowlisted project-shape artifacts and inventories referenced baseline specs,
RFCs and roster identities. It never treats arbitrary Markdown or source code
as project intent.

The source manifest is observation scope, not a second copy of Butlers facts.
It stores paths, extraction classes and the source revision. Entity names and
project statements come from the referenced Butlers artifacts.

Rejected alternatives:

- **Hard-code a larger Butlers summary in Syzygy.** Fast, but it creates a
  drifting second source of project truth.
- **Ask an LLM to summarize the repository.** Broad, but nondeterministic,
  unbounded, difficult to falsify and contrary to the owner's copy concern.
- **Treat every file as Polaris input.** Confuses intent with implementation;
  repository geography belongs to Orrery.

### 2. Model coverage as data

Each declared category carries `declared`, `modeled`, `unknown` and
`contradicted` populations. Their identities and totals reconcile against the
source manifest. A missing or unreadable source does not shrink the declared
population. When two declarations disagree, the model retains both anchors,
applies documented precedence only when it is explicit, and discloses the
conflict either way.

The machine answer and Polaris consume the same coverage object. A page cannot
claim whole-project coverage from a smaller hidden model.

### 3. Separate the project account from capability detail

The Polaris entry follows the accepted RFC7 progression:

1. Overview
2. Boundaries
3. Architecture
4. V1 scope and success
5. Project catalog
6. Capability detail
7. Evidence and gaps

The existing WhatsApp material moves under capability detail. Active and
proposed OpenSpec work appears only there, marked with its lifecycle state.

### 4. Use direct copy

Headings name Butlers concepts. Supporting sentences state project facts,
Unknowns, contradictions or actions. Copy does not explain “the reading,” “the
document,” “movements,” or the presentation mechanism. Provenance remains
available without being repeated in every sentence.

### 5. Fail closed at the content boundary

Only allowlisted project-shape files are opened. Secret detection and content
classification run before content enters the model. Suspected or
unclassifiable content is excluded with hash-not-body provenance and renders
Unknown. No observed-project code executes.

## Data Flow

1. Bind the configured Butlers repository to an exact Git revision.
2. Load the project-shape source manifest.
3. Read and classify allowlisted sources; record exclusions.
4. Extract declared entities, statements, catalogs and source anchors.
5. Reconcile coverage and contradictions.
6. Add the existing capability deep-dive facts.
7. Freeze one shared model for the human and machine surfaces.
8. Render project-level Polaris and capability drill-down from that model.

## Risks / Trade-offs

- **Butlers Markdown changes shape** → parsing failures render Unknown and the
  denominator remains visible; focused contract tests pin each extraction
  class.
- **The manifest misses a declared source** → a source-discovery sweep compares
  the five-pillar indexes and roster population against the manifest.
- **The primary page becomes encyclopedic** → progressive disclosure keeps the
  first read concise while catalogs and exact artifacts remain reachable.
- **Sensitive text enters a surface** → allowlisting and fail-closed secret
  classification precede model construction.
- **A stale summary conflicts with a higher authority** → both are retained;
  explicit Butlers precedence selects the effective statement and Polaris
  discloses the disagreement.

## Migration Plan

The new model fields are additive. During implementation, the current
single-capability page remains available until the project-wide page passes
parity and cold-open evaluation. Rollback restores the old renderer and model
builder; it does not alter Butlers or any governed artifact.
