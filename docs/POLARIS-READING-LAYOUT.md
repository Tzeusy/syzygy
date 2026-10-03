# Polaris reading layout and explanatory assets

Polaris uses a wider editorial column with a persistent desktop outline. On
smaller screens the outline becomes an in-flow drawer. Section links move
straight to their destinations; they do not animate through the entire document.
Opening the drawer changes presentation only.

The seven group shortcuts are native links ahead of the global navigation, so
they remain available when the full four-depth outline is closed or scripts do
not run. The server emits an outline link for every h2/h3 target in document
order; fragment targets remain outside disclosures. A no-script drawer states
its total link population. The optional local script recomputes the number
hidden when the drawer opens, closes or changes at the viewport breakpoint;
it stores no choice in cookies, storage or history. This is not catalog
filtering or pagination: all facts, source rows and links remain in the HTML.

Exact-source controls name the source path while their href remains the sole
carrier of the revision-bound identity. Source records occupy scoped columns
in the existing open, keyboard-scrollable table: identity, rule/pillar, and
outcome/anchor/digest. A source with no admitted body digest says “no body
read,” never an empty digest cell. Admitted Markdown headings map relative to
the shallowest heading in their fragment and start below their anchoring
heading; fenced and indented code cannot set that depth.

The architecture reading supports source-backed explanatory assets:

- Explicit `flow` fences render bounded sequences with a readable vertical
  arrangement on narrow screens or for longer sequences.
- `relations` fences render named endpoints with their complete explanations.
  Labels are escaped, descriptions use the safe Markdown renderer, and unknown
  fields or malformed payloads remain literal code.
- Source-bound chapter plans expose optional component guides. Their ranges must
  partition the complete declaration without gaps; the full-declaration control
  opens every chapter. Guide fragment targets stay outside native disclosures.

Diagrams carry curated provenance. Named elements reference the parent narrative's
canonical anchor when it has one unambiguous source; otherwise they carry an
explicit non-normative marking. Repeated references do not create additional
anchors. The original source explanations retain qualifications and remain the
text equivalent of the visual relationships.

The reading plan stores hashes and offsets rather than captured source bodies.
A changed source or invalid selection falls back to the complete declaration
and announces the withdrawal reason (`digest-mismatch`, `no-passages`, or
`plan-malformed`) beside it. A corrected reviewed digest can restore the
condensed selection.
The plan is presentation input, not adopted project intent or runtime evidence.
The current Butlers plan is a curated proving case; source-to-plan generation
and a reusable multi-project authoring workflow remain unfinished.

Relevant verification lives in the Markdown, reading-plan, narrative, parity
and real-browser tests. Browser checks exercise the desktop/mobile navigation,
source browsing, guide opening, complete-declaration control and diagram layout.
Final delivery also requires the actual gated Butlers capture and the canonical
repository battery at the reviewed commit. Captured content and screenshots
remain in local retention; committed evidence contains identities and outcomes.

Four named explanatory figures are selected from the same digest-bound architecture
account. The core-loop figure appears between Purpose and Promises; runtime,
connector and proactive-delivery figures open the architecture account. The section
outline links directly to each figure. Labels must lie inside the complete retained
explanations; source drift removes both figures and their navigation links.

For the reusable LLM-assisted authoring process and current tooling gaps, see
the [Polaris generation kit](polaris-generation/README.md).

## Honest encodings in the first reading

The Observed and Unknown treatment is declared once in the app's
`EPISTEMIC_ENCODING` table. Badges, project-shape tuples and Unknown
disclosures use its color and symbol; their visible words carry the meaning
when color or generated content is unavailable. A tuple may carry its label
locally or inherit the nearest `data-epistemic-scope-label`. The route sweep
counts each rendered encoding on Polaris, Trajectory and Orrery; Home is a
separate diagnostic. The browser census runs after scripts, so Orrery's
unmapped region participates as an Unknown disclosure even though its block
is created after the server response. A proposal uses the distinct `--proposed` token and
retains “Proposed change — not current authority.”

Before the catalog, a conditional band exposes existing Unknown whole-shape
and roster-identity claims with their reason, route, tuple and deep link. Its
count covers all Unknown project-shape claims, including members deeper on the
page. The item-state fixture exercises missing-source Unknown and contradicted
Unknown at the suspended tier without a new repository read. These are
synthetic renderer counterexamples: the current extraction grammar cannot
emit either item state from the admitted Butlers fixture.

Freshness remains the closed four-value field. If it is absent, an Unknown
claim shows a separate currency disclosure; an Observed claim is refused.
The disclosure is not a fifth freshness value or a route to the gated
currency-bound assessment.

The tier, freshness and challenge values have their own declared tables
beside `EPISTEMIC_ENCODING` in `design-tokens.ts`: six tiers, four freshness
values and `unchallenged`, each with a class, symbol, token, copy row and,
for freshness, the reason and route stated when no claim carries it.
`unstated` is the tier slot's absence and sits outside the six. Each tuple
stays one text node. Generated CSS keyed on the tuple's own attributes
renders each value's symbol in its token: the tier on the tuple's
`::after` (its `::before` is the label's symbol), freshness and challenge
on the two pseudo-elements of one empty `<i>` after it. That is the only
mark markup, about 7 bytes a tuple, and each field keeps its own token.
The words carry the value, so a mark's symbol has an empty alternative
text. The claim-state glossary rows are generated from the same tables and
carry the value classes. An undeclared value refuses to render.

A proposal is not a claim state. Its treatment is one declared disclosure row
(`PROPOSAL_DISCLOSURE`): the `proposal` section class with its `--proposed`
border, the `proposal-label` text marker ("Proposed change — not current
authority.") with its symbol, and one glossary row under "Not a claim state",
after the challenge list. That row counts the proposals served on the page
and states its reachability note exactly when there are none. The section
rule names `.claim-section` as well: the reading layout's later
`.claim-section { border: 0 }` otherwise removed the proposal border.

## Source legend and catalog reconciliation

One `POLARIS_COPY` sentence (`legend.sources`) sits directly before the
sources table, and the table region names it with `aria-describedby`. It
decodes the identity (repository, revision, path, Git object id) and the
Rule, Anchor, Outcome and Digest fields, and says a digest is neither
permission to read the bytes nor a verification of them. It is outside any
`<details>` and adds no link. `polaris-reconciliation.test.ts` holds it to
the five source rules, the anchor union and the four rendered outcomes.

One reconciliation line opens the catalog group. Counts read off the
machine answer (sources, items, the nine class counts) are Observed. The
two class sums and the item-marker count are Inferred. The marker count is
every `data-polaris-item` attribute occurrence in the final HTML, so the
line is a single placeholder substituted after the page is built; a
missing, repeated or truncated placeholder aborts the render. Markers minus
items is Unknown (`mapping-coverage-absent`), routed to matching each
marker's claim identity to one machine item. Every figure carries its state
as visible words and as `data-figure-state`, not as color. An unobserved
shape renders the line as Unknown with the shape's reason and route and no
number. The PWB-REQ-020 sweep compares every figure as a
`catalog-reconciliation` family.
