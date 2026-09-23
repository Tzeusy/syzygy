# Polaris SVG graph diagrams — feature-request candidate

> **DESIGN CANDIDATE — BINDS NOTHING. OWNER HOLD.** This document is the
> design-only outcome authorized by P-83 question 5 and bead
> `syzygy-dov.16.5`. It changes no code, specification, doctrine, registry,
> consent, read surface, or act record. It supplies no implementation warrant,
> creates no implementation bead, and approves no SVG, fence, schema,
> renderer, curation, or source-read change. A merge, review, or general
> approval changes none of those facts. Any build re-enters the feature-request
> funnel and must pass the owner and specification gates in this document.

Date: 2026-09-23. Status claims in this document are scoped to repository
commit `44c51b54054b7181e63f71917380faaa302a2df2` unless another revision is
named.

## One-sentence proposal

Add a bounded, server-rendered, inline SVG view over an already-admitted
project graph, paired with a complete text rendering of the *same* nodes and
edges, so Polaris can show hierarchy, fan-in, fan-out, and cycles without
minting identity, hiding epistemic state, reading another source, or making a
picture authoritative.

## Authority and non-authority

The owner ruled P-83 arm A on 2026-09-21: Q5 is design only and must re-enter
through feature-request before any build. The ruling is recorded in
`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`.
It is authority to prepare this candidate, not to accept or implement it.

The design serves:

- `VIS-1`: the visual may simplify presentation, never its truth content;
- `VIS-3`: a human reader must be able to understand the graph;
- `VIS-7`: identities, links, and legend meanings must remain faithful;
- `RFC1-9`, `RFC1-10`, and `RFC1-25(d)`: identity comes from its owning
  authority, labels never become identity, and relation spelling is never
  relation identity;
- `RFC6-17`, `RFC6-20`, and `RFC6-22`: aggregation discloses, internal links
  resolve, and renderings agree semantically rather than pixel-for-pixel;
- `PWB-REQ-014`: Polaris presentation stays non-citable and never becomes an
  authority source; and
- `PWB-REQ-020`: human and machine forms keep the same project-shape facts.

The candidate does not claim those clauses already specify this feature.
The mapping gate below decides that before any implementation is scheduled.

## Current surface and deduplication boundary

[Observed] `polaris-markdown.ts` already consumes literal fence lines. Its
`flow` fence accepts one bounded arrow sequence; its `relations` fence accepts
a bounded JSON list, escapes text, and leaves malformed or unsupported input
as literal code. It emits ordered-list and stacked relationship HTML, not SVG.

[Observed] `polaris-reading.ts` still uses JavaScript character offsets in a
digest-bound reading plan. `applyReadingPlan` slices the already-admitted
declaration and constructs the `flow` or `relations` fence presented to the
Markdown renderer. The stitch site is its summary map; it is not the fence
parser and the offsets are not byte offsets.

[Observed] A separate generator *draft preview* already emits SVG for an
intermediate editorial draft. It uses draft-local handles and source excerpts,
is labeled unreviewed/unadopted, and is not the project-shape graph. Its
existence is not permission to reuse draft handles as project identities or to
copy its renderer into Polaris. Shared future primitives are permitted only if
they consume the graph contract below and preserve each surface's authority
labels.

[Inferred] The gap is therefore not “Syzygy has no SVG.” It is narrower: the
authoritative Polaris reading surface has no project-graph view capable of
showing hierarchy, fan-in, fan-out, or a cycle as such.

## Proposed graph contract

This is a presentation contract over data already present in one identified
evaluation. It is not a new kernel graph, source adapter, or storage format.

### Graph envelope

Each diagram input has:

| Field | Meaning | Constraint |
|---|---|---|
| `graphKey` | Presentation key for this view | Deterministically derived from the evaluation identity, the figure definition's existing presentation key, and ordered member identities; non-authoritative and non-citable. |
| `evaluationId` | Evaluation supplying every member | Exactly one; mixed-evaluation diagrams refuse visual rendering. |
| `title` | Human label | Presentation only; never identity. |
| `nodes` | Closed member population | Every member references an already-minted durable project, graph, claim, or anchor-target identity. |
| `edges` | Closed relationship-instance population | Every edge carries an already-minted model relationship-instance identity, its typed-relation class, and two member identities. |
| `hierarchyRelationId` | Optional typed-relation class used as parent→child | Zero or one existing RFC1-25(d) typed-relation identifier; edge instances of this class are the sole hierarchy truth carrier. |
| `roots` | Top-level hierarchy members | Derived from the parent relation; never separately authoritative. |
| `filters` | Declared view scope | Rendered beside the graph and copied into the text form. |

`graphKey` exists only to keep DOM ids and fixture handles stable. It is not a
kernel identity, anchor identity, source identity, or cross-evaluation join
key. A diagram may not mint an identity the input model lacks.

### Nodes

Each node carries these required values:

- `identity`: the exact durable identity supplied by its owning authority;
- `label`: captured display text, allowed to change without changing identity;
- `kind`: the source model's closed entity or claim kind;
- `claimRole`: exactly one of the existing presentation roles
  `anchored-project-fact`, `epistemic-claim`, or
  `non-normative-framing`;
- `epistemic`: the complete tuple when the member is a claim, not a color-only
  shorthand;
- `anchorIds`: zero or more existing durable targets, with zero lawful only
  for explicitly non-normative framing;
- `provenance`: the captured anchor identities and evaluation identity from
  which this presentation member was derived.

Two nodes with the same label and different identities remain two nodes. A
rename changes only the label. A missing or duplicate identity fails the
diagram closed and leaves the complete text facts available.

### Edges

Each edge carries three deliberately separate concepts:

- `relationshipInstanceId`: the exact model relationship-instance identity;
  this owns graph membership and survives independently of every other
  instance of the same typed relation;
- `typedRelationId`: the `RFC1-25(d)` typed-relation class — relation name plus
  ordered endpoint-domain pair — shared lawfully by many relationship
  instances; and
- `label`: presentation wording, never either identity.

The remaining edge fields are:

- `edgeKey`: a deterministic DOM/fixture key over graph key and
  `relationshipInstanceId`; it is not a replacement relation identity;
- `fromIdentity` and `toIdentity`: exact member identities;
- `kind`: semantic relation class copied from the typed relation;
- `direction`: directed or explicitly undirected, never inferred from layout;
- `claimRole`, `epistemic`, and `provenance`: the same honesty fields as a
  node where the relationship instance is itself claim-bearing.

Layout never reverses an edge. A missing endpoint, undeclared relation kind,
duplicate relationship-instance identity or edge key, typed-relation metadata
that disagrees with its registered class, or hierarchy node with two parents
refuses visual rendering. Any number of distinct relationship instances may
share one typed relation within the density budget; each stays separate in
SVG, text, and parity.

### Hierarchy, fan-in, fan-out, and cycles

- Hierarchy is derived only from relationship instances whose
  `typedRelationId` equals the envelope's `hierarchyRelationId`. Nodes carry no
  independent parent field and edges carry no independent hierarchy boolean.
  The parent map and root set are derived values, never input truth.
- The derived hierarchy is a forest: zero or one incoming hierarchy instance
  per node and no hierarchy cycle. A hierarchy edge with a missing endpoint,
  two parents, or a cycle is invalid input, not a layout challenge.
- Non-hierarchy relations may have any fan-in or fan-out within the density
  budget. The view must not duplicate a node merely to make a tree easier to
  draw.
- Directed cycles are valid. Strongly connected components are computed only
  for layout and disclosure. Every original node and edge remains present;
  the component receives a visible `Cycle` label and the text form lists its
  members and traversing edges.
- Self-loops are valid only when present in the model. They carry a visible
  `Self-loop` label and a literal text relation.
- No inferred edge may be drawn to make the graph appear connected.

## Deterministic, non-identity layout

Coordinates, ranks, bends, ports, and collision offsets are presentation
state and never enter graph identity, evidence, anchors, or parity comparisons.

The proposed layout pipeline is deterministic:

1. validate the full graph and budgets;
2. derive the hierarchy forest;
3. compute strongly connected components for non-hierarchy relations;
4. rank components by hierarchy depth, then directed dependency depth;
5. order ties by opaque identity bytes, never label or source path;
6. assign fixed node boxes from the bounded label measure;
7. route orthogonal edges with deterministic port order; and
8. emit coordinates rounded to integer CSS pixels in canonical member order.

Same graph, filters, evaluation, and figure definition must produce the same
serialized SVG bytes. A different legal layout is not a different graph, but
the implementation must choose one algorithm/version and include that version
in its presentation input so a cache never serves coordinates from another
algorithm.

Layout failure, overlap beyond the collision threshold, or a budget breach
falls back to the complete text form with a presentation-only explanation.
It does not turn a project claim Unknown, change the model, or truncate the
member population.

## Visual grammar and legend

The legend is generated from encodings actually present in the diagram. It is
visible beside the figure and repeated in text. Color is never the only cue.

| Meaning | Shape or line | Required text cue |
|---|---|---|
| Anchored project fact | Solid rectangle | `Anchored fact` plus its epistemic label. |
| Epistemic claim | Rounded rectangle | `Claim` plus label, tier, primary reason, freshness, and challenge state. |
| Non-normative framing | Dashed outline with diagonal corner notch | Visible `Framing — non-normative` marker; never green, approved, or verified. |
| Hierarchy parent | Containment band and thin solid connector | `Contains` in legend and text relation. |
| Directed relation | Solid arrow with a printed relation label | `From — relation — to` in text. |
| Undirected relation | Solid line with endpoint ticks | Explicit `Undirected` text. |
| Cycle | Loop badge around the component, not a state color | `Cycle` plus member count and listed edges. |
| Unknown claim | Existing Unknown symbol and token plus node shape | Literal `Unknown` and its reason; color alone is insufficient. |

Stroke width, dash, shape, icon, and label together carry meaning. Theme
tokens supply colors; the feature does not introduce raw color literals.
Implementation review verifies WCAG 2.2 AA contrast in every theme supported
at that time and refuses a token combination that drops below the required
ratio. The current forced-dark baseline counts as one theme; a light palette
remains the separate P-83 Q6 design question.

Text must meet 4.5:1 against its background, large text 3:1, and graph strokes,
node boundaries, focus indicators, and non-text state cues 3:1. The checker
records the measured token pairs and ratios; visual inspection is not proof.

## Same-graph text and assistive rendering

The SVG is a convenience view, not the accessible name of the graph and not a
second truth store. It is `aria-hidden` and has no focusable descendants. A
semantic HTML block immediately following it carries the complete graph:

1. figure title, evaluation, declared filters, node count, and edge count;
2. a nested node list reflecting the hierarchy without duplicating fan-in or
   fan-out nodes;
3. for every node: exact label, kind, role, full epistemic tuple when present,
   provenance routes, and cycle membership;
4. one relationship list containing every edge exactly once in canonical
   order; and
5. the same legend meanings in prose.

The text block is always served and visible under the heading `All nodes and
relationships`; it is not collapsed behind a control. If CSS, SVG, or
JavaScript is unavailable, the complete text graph remains ordinary document
flow.

Internal source routes are generated only from the already-authorized anchor
table outside the diagram payload. The SVG itself contains no anchors or
URLs. An unresolved target is rendered as unresolved text and fails the link
oracle; it is never guessed from a label or path. Routes use native links with
accessible names, visible focus, a 24 by 24 CSS-pixel hard minimum target, and
a 44 by 44 preferred target where layout permits.

## Interaction, zoom, reflow, and motion

The first version is deliberately non-interactive:

- zero pan, drag, hover-only disclosure, clickable SVG nodes, or script-driven
  zoom controls;
- zero keyboard stops inside the SVG;
- zero script-driven focus movement; activating an existing source route uses
  the route's ordinary focus/target behavior;
- browser zoom and text resizing are the zoom mechanisms;
- at a viewport of 640 CSS px or narrower, the SVG is removed from visual flow
  and the complete text graph remains visible;
- at 320 CSS px and at 400% zoom, the page has no horizontal document scroll,
  labels wrap, and every route remains usable;
- at wider widths the SVG may sit in a bounded local overflow container, but
  no fact exists only outside its initial viewport;
- no animation or transition communicates topology or state; and
- `prefers-reduced-motion` changes nothing because the diagram has no motion.

If later research proposes interactive expansion, panning, or zoom, that is a
new feature request with new keyboard, focus-return, reduced-motion, and
state-persistence scenarios. It is not latent authority in this candidate.

## Literal fences and the offset-stitch successor

The current Markdown fence parser is retained as the safety boundary:

- only an admitted fence name invokes a diagram parser;
- the parser receives the literal normalized lines between the opening and
  closing fence;
- malformed, unknown, over-budget, or incomplete data stays escaped literal
  code; and
- the body never contains interpreted HTML, SVG, CSS, script, or URL data.

The candidate does **not** authorize a new `graph` fence grammar. Before one
exists, the owner must choose its place:

- **Arm A — model reference (recommended):** a literal fence carries only a
  version and a closed list of existing model identities plus view options;
  the renderer resolves them inside the already-served evaluation. Labels,
  roles, relations, and provenance always come from the model.
- **Arm B — literal graph value:** the fence carries complete typed node and
  edge values. This is simpler to preview but creates a second statement of
  model truth and therefore requires an explicit parity contract and stronger
  drift handling.
- **Arm C — no new fence:** figures are selected only by a reviewed reading
  plan and the existing `flow`/`relations` fences remain unchanged.

The future replacement for character-offset stitching is likewise separate.
A reviewed reading plan should select a complete literal fence block by its
declaration digest and a stable presentation selection key; a fence parser then extracts
that entire block from the already-admitted in-memory declaration. It must not
assemble a new fence by slicing labels and descriptions from several offsets.
This adds no source read and stores no additional source body. If a proposal
instead stores literal source bodies in the plan, it changes the retention
and governed-data posture and requires the corresponding owner gate before a
line of implementation.

## Inert rendering and trust boundary

Diagram values are data, never markup. The eventual implementation must use a
closed emitter and escape every text node. The allowed SVG vocabulary is the
minimum needed for static geometry and text; the following are forbidden:

- arbitrary markup or pass-through attributes;
- scripts, event-handler attributes, embedded HTML, animation, or style
  payloads;
- images, external resources, fonts, imports, network fetches, or URL-valued
  paint/filter data;
- links, `href`/legacy link attributes, document fragments, or base changes;
- user-provided element ids, class names, CSS, path commands, coordinates, or
  transforms; and
- reads of source bodies, files, providers, or endpoints not already present
  in the identified evaluation.

The renderer owns all element names, attributes, ids, geometry, classes, and
styles. Hostile strings that resemble markup, script, URLs, CSS escapes, or
SVG path syntax are either escaped as labels or rejected by the typed input
validator. The page's response ceiling remains the final authority: a diagram
never bypasses, degrades, or reinterprets it.

## Proposed populations and budgets

These are owner-facing design values, not inherited authority. A build packet
must confirm or replace each one and re-run the byte measurement against the
then-current page.

Three populations stay distinct:

1. **Complete semantic text:** every supplied node and relationship instance,
   with no diagram-specific byte or density cap and no truncation.
2. **Additive visual bytes:** SVG geometry plus its visual legend. Density and
   the 24/96 KiB limits decide only whether these bytes are added.
3. **Whole encoded response:** text, SVG when eligible, and every other page
   byte under the registry's authoritative `maxHumanResponseBytes`. At the
   reviewed baseline that ceiling is 2,097,152 bytes; the implementation must
   re-read rather than copy it. A breach serves nothing, including no text-only
   fallback.

| Population or budget | Proposed hard limit | Failure behavior |
|---|---:|---|
| Diagrams per Polaris response | 4 | Additional figures render as complete text only, with a counted presentation notice. |
| Nodes per diagram | 20 | SVG withheld; full text graph retained. |
| Edges per diagram | 32 | SVG withheld; full text graph retained. |
| Hierarchy depth | 6 | SVG withheld; full text graph retained. |
| Parallel edges per endpoint pair | 4 | SVG withheld; every relation remains in text. |
| Node label | 64 Unicode scalar values, 3 wrapped lines | Long labels remain complete in text; SVG uses a visibly disclosed truncation. |
| Relation label | 48 Unicode scalar values, 2 wrapped lines | Same rule as node labels. |
| Complete semantic text | 100% of supplied nodes and relationship instances; no diagram cap | Never truncate or omit. If the whole response breaches its authoritative ceiling, serve nothing. |
| Additive SVG plus visual legend | 24 KiB per figure | Withhold those visual bytes; complete text is unchanged. |
| Aggregate additive SVG plus visual legends | 96 KiB per response | Withhold later visual bytes; complete text is unchanged. |
| Whole encoded response | Registry `maxHumanResponseBytes` (2,097,152 bytes at reviewed baseline) | Existing bounded-response behavior serves nothing; never partial or success-shaped output. |
| Script and external-resource requests | 0 | Any emitted script/resource reference fails the inertness oracle. |
| SVG keyboard stops | 0 | Any focusable SVG descendant fails accessibility review. |
| Visual/text graph difference | 0 missing or surplus node identities or relationship-instance identities | Parity test fails; no SVG is served. |
| Layout serialization drift | 0 bytes for the same identified input and algorithm version | Determinism test fails. |

The prior P-63 headroom measurement is historical evidence, not a reservation.
The 96 KiB additive proposal is therefore not justified by “available
headroom.” It is a bounded visual price to put before the owner, not a cap on
truth. The current page and complete text population must be measured again
from a clean committed tree before implementation.

## Fixture matrix and independent oracle

The fixtures are project-neutral and hand-authored. Expected node identities,
relationship-instance identities, typed-relation classes, derived hierarchy
parents and roots, strongly connected components, roles, and provenance sets
are literals in the test, never imported from renderer code.

| Fixture | Must prove | Required counterexample |
|---|---|---|
| `chain` | Two distinct relationship instances of one typed relation survive SVG, text, and parity | Collapse by typed-relation id; relationship-instance set fails. |
| `diamond` | Four instances of one typed relation express fan-out and fan-in without node duplication | Collapse same-class edges or duplicate the join node; instance/identity sets fail. |
| `hierarchy-authority` | Hierarchy edges alone derive six levels, one parent map, and one root set | Mutate the derived parent to disagree with its edge, name a missing parent endpoint, or render a child as a root; exact parent/root oracle fails. |
| `cycle` | Three-node directed cycle plus incoming edge | Drop the closing edge or cycle label; SCC/text parity fails. |
| `self-loop` | One explicit self-loop | Infer a loop on an isolated node; surplus edge fails. |
| `parallel` | Two differently typed relations over one endpoint pair | Coalesce them; edge-key set fails. |
| `same-label` | Two identities sharing one label stay separate | Key by label; node identity set fails. |
| `roles` | All three claim roles and an Unknown tuple | Remove non-normative text cue or Unknown reason; role oracle fails. |
| `hostile-text` | Markup-, script-, URL-, and path-shaped labels remain inert text | Any forbidden element/attribute or resource reference fails. |
| `density-boundary` | At the limit SVG is additive; limit plus one removes only SVG. Measure complete-text node/edge sets and bytes, additive visual bytes, and whole-response bytes before and after fallback | Any text-population/byte change, nonzero fallback SVG bytes, or unmeasured whole response fails. |
| `response-ceiling` | Both visual and text-only forms are checked against the authoritative whole-response ceiling | Serving truncated text or any success-shaped body after a ceiling breach fails. |
| `mobile-no-js` | 320 px, 400% zoom, scripts disabled, full graph usable | Horizontal document scroll or missing focus cue fails. |
| `mixed-evaluation` | Visual renderer refuses mixed evaluations | Any SVG emitted fails. |
| `literal-fence` | Complete admitted fence block reaches parser unchanged | Offset-stitched body or partial fence fails fidelity digest. |

The independent oracle reads the typed fixture and the rendered artifact by
separate parsers. It compares:

1. node identity sets and counts;
2. relationship-instance identities, typed-relation ids, edge keys, and exact
   `(from, typed relation, to, direction)` tuples;
3. hierarchy edges against independently derived parent maps and root sets,
   plus cycle component sets;
4. roles, full epistemic tuples, and provenance targets;
5. the SVG data representation against the semantic HTML representation;
6. legend entries against encodings actually used; and
7. complete-text bytes, additive SVG/legend bytes, and whole-response bytes as
   three separate measurements before and after visual fallback; and
8. forbidden markup, attributes, URLs, scripts, resources, and focus targets.

The oracle imports neither the layout engine nor the SVG emitter. Coordinates
are tested only for bounds, overlap, and deterministic serialization; they
are never used to decide semantic parity.

Every predicate receives a rule-6 mutation. A mutation run records the exact
old/new fragment, subject digest, test population, and outcome so it can be
re-run after a rebase or refactor.

## UX and accessibility walkthrough

- **Entry:** a figure appears beside the source-backed narrative it explains;
  the text form follows immediately and the outline links to the figure only
  when that figure exists.
- **First glance:** title, declared scope, node/edge counts, and legend precede
  geometry. Unknown and non-normative qualifications are visible without
  hover.
- **Pace:** no client work, loading state, or delayed layout exists; the
  server-rendered text remains usable if SVG is withheld.
- **Repetition:** there are no diagram controls to double-fire. Existing
  source-route links retain their ordinary idempotent navigation behavior.
- **Defaults:** complete text is the default truth form; SVG is additive.
- **Recovery:** invalid input, density, or layout removes only the SVG and says
  why. It never removes nodes or edges from text. The separate whole-response
  ceiling remains authoritative: its breach serves nothing, not a partial
  text fallback.
- **Habit:** frequent readers can follow existing source routes in the text
  form; no pointer-only gesture is required.

The implementation accessibility review must verify keyboard-only use,
visible focus, screen-reader reading order, every then-supported theme's contrast,
200% text resizing, 400% zoom/320 px reflow, scripts disabled, and reduced
motion. Screenshots alone are insufficient evidence.

## Owner and specification gates

No build starts until all gates below are recorded in order.

1. **Feature disposition:** the owner chooses one P-83 Q5 arm: this combined
   graph-and-literal-fence design, literal-fence work alone, named changes, or
   no feature. Silence and `Agreed` are not choices.
2. **Design values:** the owner confirms or changes the graph membership,
   three claim roles, visual grammar, mobile text-first behavior, and every
   budget in the table. A changed value retires prior design review.
3. **Requirement mapping:** a fresh consequence matrix maps graph identity,
   hierarchy/fan-in/fan-out/cycle rendering, legend, same-graph text parity,
   inertness, reflow, and literal-fence fidelity to adopted OpenSpec scenarios.
   Any independently testable behavior with no exact scenario requires one
   coherent OpenSpec change under CC-REV-2 and owner sign-off; an RFC citation
   alone schedules nothing (`RFC1-33`).
4. **Authority classification:** the owner confirms that model
   `relationshipInstanceId` owns edge membership, `typedRelationId` names only
   the RFC1-25(d) class, and `graphKey`/`edgeKey` are presentation keys only.
   No new kernel/anchor identity is minted. Any identity-bearing alternative
   requires the owning RFC and act before specification or code work.
5. **Retention/security classification:** the chosen fence successor stores no
   source body and adds no read, URL, provider, egress, or active-content
   class. Any alternative that does changes security/privacy/retention posture
   and requires its own owner act and registry/policy reconciliation.
6. **Implementation authority:** only after the preceding records exist may an
   implementation packet name exact files, dependencies, tests, byte ceiling,
   and rollback. This design and its PR are not that authorization.
7. **Fresh exact-head review:** independent design and accessibility reviews
   cover the final candidate bytes; raw output is retained verbatim under a new
   distinct filename ending exactly `-RAW.md`, exact verdict words are copied,
   and every finding is dispositioned. Historical reconstruction and earlier
   raw reviews are never overwritten. Any semantic repair retires that review
   and receives confirmation.

Rollback before implementation is deletion of this candidate. After a future
implementation, rollback is removal of the additive SVG view while retaining
the complete text graph; no project identity, claim, evidence, or source body
depends on the SVG.

## Review evidence routing

The file
`docs/reviews/R-POLARIS-SVG-GRAPH-DIAGRAMS-FEATURE-CANDIDATE-RAW.md`
is a historical reconstruction written during the first correction pass. It
is preserved byte-for-byte, but it is synthesized prose, not verbatim reviewer
output and not a raw review record.

The actual Review 1 output is retained verbatim at
`docs/reviews/R-POLARIS-SVG-GRAPH-DIAGRAMS-FEATURE-CANDIDATE-REVIEW-1-RAW.md`.
**Verdict, copied exactly: REVISE** — two blocking findings and one medium
finding.

The review is bound to commit
`6e2c183744cecb3dcc1072f7a0a633a6ddc0aa83` and candidate SHA-256
`ecabd87459a317ab9ad24fe88fe60281775194388571d7f1958bd1add0fb07da`.
The repairs below change semantic bytes, so the verdict is evidence about that
reviewed commit, not confirmation of this successor.

| Finding | Disposition |
|---|---|
| F1 — typed-relation identity was used as edge-instance identity | **Repaired.** The contract now separates model `relationshipInstanceId` (membership), RFC1-25(d) `typedRelationId` (class), and `label` (presentation). `edgeKey` derives from the instance identity. The chain and diamond fixtures require multiple same-class instances to survive SVG, text, and parity. |
| F2 — node parent and hierarchy edge were two truth carriers | **Repaired.** Nodes carry no parent input and edges carry no hierarchy boolean. One envelope `hierarchyRelationId` selects the typed relation; its model edge instances alone derive parent map and roots. The hierarchy fixture mutates disagreement, a missing parent endpoint, and a child rendered as root. |
| F3 — visual byte limits also purported to bound complete text | **Repaired.** Complete semantic text is uncapped by diagram limits; 24/96 KiB govern additive SVG/legend only; the registry whole-response ceiling remains authoritative and serves nothing on breach. Density and ceiling fixtures measure complete text, additive visual bytes, and whole-response bytes separately before and after fallback. |

## Review 2 and disposition

The actual Review 2 output is retained verbatim at
`docs/reviews/R-POLARIS-SVG-GRAPH-DIAGRAMS-FEATURE-CANDIDATE-REVIEW-2-RAW.md`.
**Verdict, copied exactly: REVISE** — one blocking review-evidence finding.
It is bound to commit
`674cfaa4e81a022ecaadf742f027f874a0883276` and candidate SHA-256
`303958396129b66810c50cfc1dec042077201f46b6905bf408529d3986294f54`.

| Finding | Disposition |
|---|---|
| Review 1 was not retained verbatim | **Repaired without changing graph-design semantics.** The committed reconstruction remains untouched and is labeled honestly above. The supplied Review 1 and Review 2 outputs now live unchanged under distinct filenames ending exactly `-RAW.md`, and every candidate review reference routes to the actual files. This evidence-routing repair changes the candidate bytes, so Review 2 confirms the three design repairs at its tested commit but cannot confirm this successor. |

## Confirmation status and review brief

**Pending. No independent confirmation verdict exists for these evidence-routed
bytes.** Review 2 confirmed the three design repairs and returned one blocking
review-evidence finding; that finding is dispositioned above. This routing
change requires fresh exact-head confirmation under gate 7.

A fresh reviewer receives this candidate, both actual raw reviews, and these
governing references: P-83/Q5, `VIS-1`, `VIS-3`, `VIS-7`, `RFC1-9`,
`RFC1-10`, `RFC1-25(d)`, `RFC1-33`, `RFC6-17`, `RFC6-20`, `RFC6-22`,
`PWB-REQ-014`, `PWB-REQ-020`, the current `polaris-markdown.ts`,
`polaris-reading.ts`, `polaris-narrative.ts`, and the separate draft-preview
renderer. The historical reconstruction is supplied only to verify that it is
preserved and no longer represented as raw evidence. The reviewer answers:

1. Does the contract keep relationship-instance identity, RFC1-25(d)
   typed-relation class, and presentation label distinct, with multiple
   same-class chain/fan-in/fan-out instances surviving SVG, text, and parity?
2. Does every visual encoding have a literal legend and complete same-graph
   text equivalent, including roles, epistemic state, and provenance?
3. Are hierarchy edges the sole truth carrier, with parent maps and roots
   derived and disagreement/missing-parent/false-root mutations killed?
4. Do keyboard, focus, no-JS, zoom, reflow, contrast, and motion requirements
   meet WCAG 2.2 AA as a floor?
5. Do hostile diagram values remain inert with zero markup, script, URL, or
   resource interpretation and zero new reads?
6. Are complete text, additive SVG/legend bytes, and the authoritative
   whole-response ceiling distinct and measured before/after fallback?
7. Does the literal-fence successor correct the actual character-offset stitch
   site without falsely claiming the fence renderer is offset-based today?
8. Do the owner/specification gates prevent this candidate from turning into
   implementation authority by implication?

Until that review and the owner gates land, the default is the current
text-arrow presentation and the current literal fence renderer. No SVG graph
feature is approved.
