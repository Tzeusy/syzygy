# Polaris reading layout and explanatory assets

Polaris uses a wider editorial column with a persistent desktop outline. On
smaller screens the outline becomes an in-flow drawer. Section links move
straight to their destinations; they do not animate through the entire document.
Opening the drawer changes presentation only.

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
currency-bound assessment. Tier, freshness and challenge treatment tables
and the full proposal legend are later work.
