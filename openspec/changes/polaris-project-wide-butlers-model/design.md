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

The source manifest is observation scope, not a second copy of Butlers facts.
It stores paths, extraction classes and the source revision. A declared item
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

The project-fact population is closed rather than accepting arbitrary injected
fact names. It consists of:

1. `item:<class>:<declared-key>` for each item in the signed nine-class
   extraction grammar;
2. `count:<class>` for each of those nine classes;
3. `catalog-count:<catalog-key>` for each of the nine signed V1 catalog
   headings; and
4. `project-account:<key>` for the six signed account keys.

A declaration enters one of those facts only from an admitted source and the
extractor assigned to that source. The root-index statement that Butlers has
eight domain butlers and the V1 `Butlers` catalog's derived population of nine
therefore both declare `catalog-count:Butlers`; neither is a side input.

Two additional root-index grammars are closed. Under the exact H2 `Key
Architectural Facts`, an unordered item whose leading bold label is
`<decimal> daemons` and whose own text contains the exact cardinal form
`<decimal> staffers ... + <decimal> domain butlers` emits only
`catalog-count:Staffers` and `catalog-count:Butlers`. Under the exact H3
`Precedence Order When Layers Disagree`, one pipe table with the exact columns
`#`, `Layer`, `Owns`, `Home` emits the seven ordered layer rules only when rows
1 through 7 each occur once and each layer/home is unique. Rows 1 through 5
carry exact normalized roots; row 6's exact `roster/{butler}/` template expands
only for declared roster keys; row 7's exact `src/, alembic/, tests/` literal
is inert because code owns no admitted fact. No other prose, number or table
mints a declaration or rule.

The registry freezes the exact `Layer`, `Owns` and `Home` semantic literals for
all seven rows. Raw `Layer` cells must be exactly one bold span; matching trims
outer ASCII whitespace and unwraps only complete inline code spans in `Owns`
and `Home`, preserving case, punctuation and internal whitespace. It also
freezes a closed family map: project-account, principle, success-
criterion and catalog-entry/count facts map to row 1; design-contract to row 2;
baseline-spec to row 3; craft-policy to row 4; topology-component to row 5;
roster-identity to row 6; and row 7 owns no fact in this content class. Mixed-
family prose or any altered `Owns` cell invalidates the table rather than
extending the grammar.

For one conflicting fact, the precedence table applies only when exactly one
declaration's source is under the lowest-numbered listed home assigned by that
closed map. The root summary is a non-owning declaration and
defers to such an owning layer; an unlisted source owns nothing. Missing,
malformed, duplicated, out-of-population, self-referential, inapplicable or
equally ranked rules select nothing. Thus the named live
`catalog-count:Butlers` conflict retains eight from the root summary and nine
from the Heart and Soul V1 catalog; the admitted row-1 Heart and Soul rule may
select nine only with that exact rule anchor and both declarations still
visible. Without that applicable rule the result is Unknown.

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

Before the first body read, the evaluation checks the exact per-repository
Butlers observation-consent record, the observing project's concrete
secret-detection/classification policy and the project-shape observer's
governance-plane registered adapter entry against effective human owner acts
under RFC3-16(a) and RFC3-16(b). Each act may independently be valid state (1)
or state (2); all-valid mixed states admit reads. Every artifact identity and
digest, act-record identity, act type and scope, provenance state, and A1 audit
identity or explicit absence is a deterministic input.

Missing or invalid act state produces zero body reads and a project-model
Unknown. Failed or indeterminate state-(2) correlation never falls back to
state (1). Human and machine outputs expose the exact state for each authority,
and state (1) carries the same-tree-forgeability limitation. These acts warrant
use of the consent, policy and registration; they are not evidence that
screening or reading succeeded. Specification sign-off mints none of these
artifacts. The admission oracle closes the invalid population at 195 cases:
55 owner-act/provenance cases for each of the three acts plus 30
authority-specific field cases.

### 6. Fail closed at the content boundary

Only exact Git objects under normalized repository-relative paths are read.
Absolute paths, traversal, NULs, working-tree symlinks, submodule traversal and
repository escape are rejected. Markdown is handled as untrusted text and is
context-encoded at every sink. Inline code spans and fenced code blocks are
inert contexts: markup-like examples inside them do not by themselves trigger
active-content exclusion and are never interpreted as markup or links. Secret
detectors still scan the complete transient body, including those contexts,
before parsing. Outside inert-code contexts, raw HTML elements/comments/
declarations, SVG, scripts, event-handler attributes and unsafe URL schemes in
Markdown destinations, autolinks or HTML attributes exclude the whole source.

The inert-context profile is closed and line-oriented. A fence begins with
zero to three spaces and at least three identical backticks or tildes; it ends
at the first zero-to-three-space run of the same character at least as long,
with trailing spaces only. A backtick opener's info text may contain no
backtick. Outside fences, an inline span closes only on the next backtick run
of exactly the opener length; different-length runs are content and backslash
does not escape them. Unclosed fences/spans and invalid backtick info strings
are malformed and excluded. Indented code and HTML `<code>` are not inert
contexts. The context mask affects only active-content detection; complete-body
secret scans run first.

The adapter declares one evaluation-wide envelope. `maxSources` covers the
complete manifest. `maxBytesPerSource` covers each exact blob.
`maxTotalBytes` is one cumulative counter across phase A and phase B and counts
each `(path, object-id)` body once; it never resets between phases.
`maxIndexDepth` covers discovery. Deterministic parse work is bounded by
`maxParsePassesPerSource`: the registry enumerates the only twelve pass
identities. Each complete traversal of one source counts once, including a
helper traversal; repeating one counts again and an unregistered traversal is
forbidden. Human HTML and machine
JSON have separate final encoded-byte ceilings. A source/input breach keeps
the whole source population counted and makes every dependent fact Unknown. A
final-output breach emits only the bounded typed failure envelope with the
evaluation identity, breached limit, observed count and population counts; it
never emits a truncated success-shaped model. Every breach makes cold-open
readiness false. Secret detection and classification cover model, caches,
logs, HTML, JSON and walkthrough records. Exclusions carry hash-not-body
provenance. No observed-project code executes.

The recommended registry values are unchanged for source and cumulative bytes
(`512`, `1,048,576`, `16,777,216`, depth `4`), replace nondeterministic elapsed
parse time with `16` complete passes per source, retain `2,097,152` bytes for a
human HTML response, and set the machine JSON ceiling to `8,388,608` bytes.
The split does not waive concise human presentation; it recognizes that the
machine answer carries the complete fact population.

### 7. Keep execution and judgment separate

The cold-open execution record establishes only what walkthrough occurred. A
separate exact-scope human owner judgment decides whether the comprehension
criterion is met and may carry an effective state-(1) or state-(2) act. Human
and machine outputs expose the exact judgment-act state and the state-(1)
same-tree-forgeability limitation. Failed state-(2) correlation never falls
back to state (1), and later correlation never rewrites the state under which
an earlier judgment took effect. The judgment remains recorded human judgment,
never Observed evidence or a score; neither its act nor the execution record
proves comprehension succeeded.
The judgment oracle closes its invalid population at 84 present-invalid cases
plus two absent cases.

PWB-REQ-021 owns readiness and answer retention. Its execution record carries
exactly nine identified answer entries, one for each closed cold-open prompt,
and every traversed path used for readiness must be Polaris or a Polaris exact-
source route at the same surface/evaluation identity. Missing, duplicate,
unknown or wrong-prompt answers and non-Polaris paths make readiness false, but
do not make the run or judgment act malformed. PWB-REQ-022 continues to decide
only whether the separately retained run-record/judgment pair and owner act are
lawful; its 84 present-invalid plus two absent cases do not change.

### 8. Reach verbatim intent within the existing consent class

Baseline `openspec/specs/*/spec.md` Git objects are already members of the
signed source population, and PWB-REQ-011/015 already require exact requirement
text. The performed consent covers exact Git objects selected by that
population under `declared-project-shape-text`. The live route therefore needs
no wider content class: after the ordinary authority gate, exact-object check,
whole-body secret scan, inert-content classification and requirement-identity
digest check, the renderer may transiently encode only the requested verbatim
requirement and scenarios. It stores, logs, caches and returns no unselected
body. If any gate fails, exact text remains Unknown. Any proposal to read a
body outside that population or return a raw artifact requires a separate
consent amendment and act.

## Data Flow

1. Bind the configured Butlers repository to an exact Git revision.
2. Evaluate effective state-(1)/state-(2) consent, policy and registry acts and
   retain each exact state.
3. Discover and expose the closed source-path population.
4. Read exact Git objects and classify content; record exclusions.
5. Extract declared entities, statements, catalogs and source anchors.
6. Reconcile coverage and contradictions.
7. Add the existing capability deep-dive facts.
8. Freeze one shared model for the human and machine surfaces.
9. Render project-level Polaris and capability drill-down from that model.
10. Evaluate nine-answer readiness under PWB-REQ-021, then evaluate the
    separate walkthrough record and owner judgment under PWB-REQ-022 with the
    exact judgment-act state retained.

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
- **A source escapes or becomes active content** → exact-object containment,
  inert parsing and context-aware encoding reject it before model admission.
- **A corpus exceeds local budgets** → the affected source stays counted and
  renders Unknown with the breached limit.
- **A stale summary conflicts with a higher authority** → both are retained;
  explicit Butlers precedence selects the effective statement and Polaris
  discloses the disagreement.
- **State-(1) authority is same-tree forgeable from Syzygy's perspective** →
  exact digests detect later drift but cannot establish who authored or
  attended the act. The owner accepts that residual risk only for this bounded,
  local, one-repository POC; the exact state and limitation remain visible and
  every other security gate stays conjunctive.

## Migration Plan

The new model fields are additive. This amendment remains inert until a later
owner act signs the complete eleven-artifact package; the prior state-(2)-only
behavior remains authoritative until then. Even after sign-off, effect-specific
consent, policy and registry acts and separate implementation authorization are
required before implementation or any body read. During authorized
implementation, the current single-capability page remains available until the
project-wide page passes parity and cold-open evaluation. Rollback restores the
old renderer and model builder; it does not alter Butlers or any governed
artifact.
