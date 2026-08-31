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

### 1. Discover a closed source population

The source population is finite and revision-bound:

1. the five pillar roots named by Butlers' about/README.md;
2. the files named by each pillar's own README index, restricted to that pillar
   root;
3. baseline `openspec/specs/*/spec.md` files listed by the exact Git tree; and
4. top-level roster directories that contain `butler.toml`, plus their
   `MANIFESTO.md` when present.

Narrative links do not recurse. Active changes are inventoried separately for
capability drill-down and never enter the current project account.

Discovery is one deterministic transaction at one exact revision. Phase A
reads only the Butlers path “about/README.md”, the README index under each of its five declared
pillar roots and Git-tree metadata needed to enumerate baseline specs and
roster candidates. Every transient body is secret-screened before parsing.
Phase A emits a manifest containing normalized paths, exact Git object
identities, extraction classes, discovery version and digest. An independent
validator checks that manifest against the signed PWB grammar at the same
repository identity, approved locator, object database and revision before
Phase B reads any manifest object. A Phase-A or validation failure blocks all
Phase-B reads and leaves the project model Unknown.

The source manifest is derived evaluation scope, not an authorization artifact
or a second copy of Butlers facts. Owner acts bind the signed grammar and
discovery algorithm; the derived manifest digest becomes an evaluation input
only after validation. A declared item
identity is `(item class, declared key)`; repository-relative paths and content
hashes are source-anchor state, not identity. The closed extraction classes are
the six project-account sections, numbered non-negotiables, success list items,
top-level V1 catalog entries, RFC index rows, baseline spec directories,
topology component-table first-column identities (qualifying H2s provide
context and mint nothing), craft policy-file identities and roster directories
containing butler.toml. No arbitrary heading or narrative link mints an item.
Duplicate keys in one class surface a contradiction.

Rejected alternatives:

- **Hard-code a larger Butlers summary in Syzygy.** Fast, but it creates a
  drifting second source of project truth.
- **Ask an LLM to summarize the repository.** Broad, but nondeterministic,
  unbounded, difficult to falsify and contrary to the owner's copy concern.
- **Treat every file as Polaris input.** Confuses intent with implementation;
  repository geography belongs to Orrery.

### 2. Model coverage as data

Coverage separates two populations. The source-path denominator is known from
Git and never shrinks. The within-source item denominator exists only for a
body admitted by consent and classification. If a body is unavailable, the
source remains counted but its item denominator is Unknown; the model never
reuses a fixture count as current truth. Admitted items carry `modeled`,
`unknown` or `contradicted` state and reconcile within each source.

When two declarations disagree, the model retains both anchors, applies
documented precedence only when it is explicit, and discloses the conflict
either way.

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

### 4. Use direct copy with a finite rubric

Every owner-visible string has one role: `project-fact`,
`epistemic-disclosure`, `action-label` or `scope-instruction`. Headings use at
most six words; entry ledes use at most twenty. Heading, lede and notice text
may not use “page,” “document,” “reading,” “section,” “movement” or
“presentation.” One scope instruction may state the POC boundary at entry;
action labels name their action. Provenance remains available without being
repeated in every sentence.

### 5. Gate body reads on owner authority

Before the first body read, the evaluation resolves exact digest-bound owner
acts for a per-repository Butlers observation-consent record, the observing
project's concrete secret-classification policy and the project-shape
observer's governance-plane registered adapter entry. All three A1-correlated
acts select `independently-verified`; an otherwise-valid tuple with at least one
uncorrelated act selects `owner-trusted-bootstrap` under the signed owner
direction. No other tuple permits reads. Missing, mismatched, stale, revoked,
wrong-scope or effect-widening authority produces zero body reads and a
project-model Unknown.

Trusted mode remains visibly `owner-adopted (bootstrap, uncorrelated)` in
Polaris and `/api/poc`; it is never called independently verified. It authorizes
only the declared read-only Git observation. Write, database, network, egress,
credential, environment and execution surfaces remain empty. Specification
sign-off itself mints none of the three authority artifacts.

### 6. Fail closed at the content boundary

Both phases read only exact Git objects under normalized repository-relative
paths from the approved locator and object database at one revision. Absolute
paths, traversal, NULs, working-tree reads, symlinks, submodule traversal,
filters, credential helpers, alternate object databases, remote fetches and
repository escape are rejected. Markdown is secret-screened before parsing as
inert text; raw HTML, SVG, scripts, event handlers and unsafe URL schemes never
reach browser output.

The adapter declares source-count, byte, depth, parse-time and rendered-output
budgets in the model. A limit leaves the affected source counted and Unknown.
Secret detection and content classification cover the model, caches, logs,
HTML, JSON and walkthrough records. Exclusions carry hash-not-body provenance.
No observed-project code executes.

## Data Flow

1. Bind the opaque Butlers identity, approved locator and object database to an
   exact Git revision.
2. Resolve the consent, secret-policy and observer-registry acts and select the
   closed authorization mode.
3. Run Phase A over the fixed seed objects and Git-tree metadata under the
   secret policy.
4. Derive, digest and independently validate the closed source manifest.
5. Run Phase B over only the manifest's exact Git objects; classify content and
   record exclusions.
6. Extract declared entities, statements, catalogs and source anchors.
7. Reconcile coverage and contradictions.
8. Add the existing capability deep-dive facts.
9. Freeze one shared model for the human and machine surfaces.
10. Render project-level Polaris and capability drill-down from that model.

## Risks / Trade-offs

- **Butlers Markdown changes shape** → parsing failures render Unknown and the
  denominator remains visible; focused contract tests pin each extraction
  class.
- **The manifest misses a declared source** → a source-discovery sweep compares
  the five-pillar indexes and roster population against the manifest.
- **The primary page becomes encyclopedic** → progressive disclosure keeps the
  first read concise while catalogs and exact artifacts remain reachable.
- **Sensitive text enters a surface** → allowlisting and fail-closed secret
  classification precede parsing in both discovery phases and model
  construction.
- **A source escapes or becomes active content** → exact-object containment,
  inert parsing and context-aware encoding reject it before model admission.
- **The trusted act is forged in-tree** → the owner explicitly accepts that
  risk for read-only observation; every channel discloses the uncorrelated
  basis and no non-read effect inherits it.
- **A corpus exceeds local budgets** → the affected source stays counted and
  renders Unknown with the breached limit.
- **A stale summary conflicts with a higher authority** → both are retained;
  explicit Butlers precedence selects the effective statement and Polaris
  discloses the disagreement.

## Migration Plan

The new model fields are additive. During implementation, the current
single-capability page remains available until the project-wide page passes
parity and cold-open evaluation. Rollback restores the old renderer and model
builder; it does not alter Butlers or any governed artifact.
