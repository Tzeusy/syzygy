# Manifesto assets — candidate interchange

Proposed detail for REQ-polaris-generation-003/004/012/014. This declares the
intended interchange for review; it is not a registered schema, a new source of
project truth or authority to read, generate or embed additional content.

## Composition, not a fixed page template

The generator chooses an argument, section order and useful supporting assets
from the admitted project material. The introduction explains the supported
purpose. Later sections develop that argument and let the reader choose deeper
explanation. A contents list, glossary or diagram appears because it helps that
project's reader; none is an obligatory empty section. Different projects may
need different structures while sharing accessible rendering primitives.

Every requested asset has a produced, omitted or unresolved disposition under
SCHEMA-CONTRACT.md; unresolved names unsupported capability or the blocking
admission/fidelity condition. A required asset
cannot be marked unnecessary merely because it is hard to produce. Independent
review checks omissions against the source inventory and reading needs. Missing
required material leaves the relevant generation/quality criterion unmet, even
when another part of the bundle is usable.

## Versioned records

Each asset has an opaque identity, schema version, kind, project/bundle identity,
editorial state, role in the reading order, generation provenance and review
bindings. Claim-bearing content uses the existing block/anchor model. Layout
positions, labels and file paths do not create identities or factual support.
The following kinds form the proposed closed interchange; unknown variants and
unrecognized effect-bearing fields are refused rather than rendered as HTML.

| Kind | Structured content | Renderer and fidelity obligations |
|---|---|---|
| Narrative section | Heading, ordered prose/list blocks and references to supporting assets | Develop a project-specific argument; preserve claim support and qualifications. Model output supplies content, never executable markup or styles. |
| Contents | References to actual sections and selected reading depths | Derive labels and destinations from the bundle's reading structure. No fabricated destinations, repeated giant index or navigation obscuring prose. |
| Glossary | Term, supported explanation, aliases where supported, relevant block references | Explain unfamiliar project vocabulary. Preserve unresolved meanings as Unknown; no invented definitions to fill a template. Contextual definitions and glossary links share the same entry. |
| Comparison table | Column meanings, ordered rows and claim-bearing cell blocks | Make a real comparison clearer; retain qualifications, explicit missing values, semantic headers and a usable narrow-screen reading. Absence is not a zero. |
| Curated relationship diagram | Named elements, explicit edges and their meanings, legend, anchors or non-normative/proposed markings, equivalent structured text | Explain supported relationships. Each named element has its required marking; every factual edge has support. Proposed structure cannot look existing. Geometry cannot imply an undeclared factual relationship. |
| Computed visual reference | Existing renderer/visual identity and version, evaluation/snapshot, selection, scenario, declared lens/filter/view scope, content digest, resolution outcome and governed text/query equivalent | Resolve only through the approved shared-model renderer. Preserve its semantics, provenance and applicable map obligations. This is selection/composition of a computed visual, not provider-authored geometry passed off as computation. |

These are semantic roles, not six mandatory page sections. Sections may contain
several assets or none. Typographic emphasis, spacing and native graphical
decoration belong to the trusted design system; they must not imply unsupported
project facts. The design review assesses the full composition, not the number
of asset kinds used.

## Curated and computed visuals remain distinct

Each visual exposes curated/computed provenance in human and machine forms.
Generated relationship diagrams remain editorial-draft until the applicable
human authorship act. Curated describes composition, not adoption. They are
editorial composition under RFC7-28: their
recipe may be replayable but their geometry is not reproducible project-map
truth. Anchors, legend and equivalent text carry the same relationships and
states. Renderer-generated positions cannot make a curated diagram imitate the
computed Orrery map or acquire its status authority.

A computed visual reference preserves the governing renderer's complete output
contract. Embedding it inherits the applicable RFC9 geography, legend, scenario,
selection, identity, query and nonvisual obligations; calling it an optional
asset exempts none of them. The provider cannot supply replacement coordinates,
state labels, evidence tiers, arbitrary SVG/HTML, URLs or code for that renderer.
The reference and rendering must resolve at the identified evaluation and
scenario. Missing, stale, incompatible or unsupported references have their
typed visible outcomes, not a screenshot or invented diagram presented as the
requested computation.

This change does not activate deferred live Orrery transclusion. A static
computed visual is eligible only when the governing renderer supports that
specific embedding and its full obligations are mapped and verified. Otherwise
the asset request remains explicitly unsupported/unproven. Curated explanation
or a doorway may still help the reader, but cannot be counted as satisfying a
required computed visual. Actual renderer capability and RFC9 applicability must
be resolved before claiming this kind implemented; existing POC map output is
not blanket proof of a reusable embedding contract.

## Shared rendering and bounded generation

HTML and machine views consume the same bundle and asset dispositions. All
references use trusted resolution; rendering initiates no implicit external
font, image, script or model requests. Provider-generated text and structured
data remain untrusted and screened under the existing admission and active
content rules. Unknown kinds are never interpreted as executable extensions.

The generation policy bounds asset count, nodes/edges, table cells, text size
and total output using declared limits before dispatch and validation. Exceeding
a bound produces a visible failed/partial generation outcome with the affected
asset identified, not silent truncation or an apparently complete page. Valid
retained portions keep their actual review state; they do not make the omitted
portion reviewed. Regeneration and adoption use the existing whole-bundle and
per-block review/invalidation rules.

## First-version supported production

The initial generalized generator produces narrative/contents/glossary/comparison
and curated relationship assets, including focused deep dives composed from those
roles. A computed-visual reference remains a recognized request kind but has no
production renderer enabled in this version. Its disposition is unresolved with
the unsupported renderer named; required computed output keeps the relevant
readiness criterion unmet. Neither a curated diagram nor a screenshot substitutes.
Enabling a computed renderer requires its specific applicable coverage, registry,
implementation and effect gates first. No full Orrery implementation is smuggled
into the curated-diagram delivery scope, and no computed support is claimed.

## Preserve source relation meaning

A source-to-asset adapter preserves the owning kernel's typed relation identity,
direction, multiplicity and evaluation. A declared dependency is not coerced into
an operative depends_on edge; neither is an implementation mapping. Multiple
placed_in relations remain nonfunctional and cannot become a guessed unique
placement because the layout prefers a tree. Curated explanatory edges use their
own supported meanings and do not mint or substitute kernel relations. Unsupported
conversion is unresolved, not a lossy relabeling into an attractive diagram.
