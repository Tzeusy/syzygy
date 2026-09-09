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
A changed source or invalid selection falls back to the complete declaration.
The plan is presentation input, not adopted project intent or runtime evidence.
The current Butlers plan is a curated proving case; source-to-plan generation
and a reusable multi-project authoring workflow remain unfinished.

Relevant verification lives in the Markdown, reading-plan, narrative, parity
and real-browser tests. Browser checks exercise the desktop/mobile navigation,
source browsing, guide opening, complete-declaration control and diagram layout.
Final delivery also requires the actual gated Butlers capture and the canonical
repository battery at the reviewed commit. Captured content and screenshots
remain in local retention; committed evidence contains identities and outcomes.
