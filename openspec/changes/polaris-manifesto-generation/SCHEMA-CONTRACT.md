# Generator interchange — candidate schema contract

Proposed representation for review, before executable schemas and registration.
This is not an installed plane schema, migration or implementation. It refines
INTERFACES.md and ASSET-CONTRACT.md without replacing kernel identities, source
state vocabularies or effective owner-act evaluation.

## One owning record for each kind of information

| Record | Owns | References, never replaces |
|---|---|---|
| Generation request | Request identity, requested assets, audience/profile input, budget and selected route | Project/snapshot, effective permissions, policy and existing work binding |
| Source inventory | Independently prepared review denominator and omission dispositions | Owning source identities, declarations and captured evidence |
| Run controls | Local reservation, dispatch-admission and finalization ordering facts | Scheduler observations, execution authority and immutable Execution Records |
| Asset bundle | Editorial composition and generated content | Source anchors, existing claim tuples, source inventory and review bindings |
| Execution Record | Historical execution envelope | Source receipts, run/work identities and their declared joins |
| Authored artifact | Adopted presentation and its attributed version | Effective per-block act, reviewed candidate and predecessor/application receipt |

All records carry their declared class/version and project identity. Version
selection is explicit; missing versions are invalid. Record digests bind canonical
bytes after validation, never stand in for adoption, and never include mutable
render-time presentation state. Exact canonicalization rules and executable
encodings are implementation artifacts reviewed against this contract, not an
opportunity to change identifier semantics.

## Requested assets and output assets are different records

A requested asset has a stable request-local identity, requested kind, role,
requiredness and the source of that requirement (request, reading obligation or
frozen acceptance criterion). It has no fabricated output identity or digest.
Requiredness cannot be downgraded by provider output.

Each request resolves to exactly one disposition:

| Disposition | Required payload | Invariant |
|---|---|---|
| Produced | References to one or more validated output assets | Every reference resolves in the same bundle; produced does not mean reviewed, adopted or acceptable |
| Omitted | Reviewable reason and supporting disposition reference | Only optional assets whose omission preserves every reading obligation; not a substitute for unavailable capability |
| Unresolved | Missing support, permission, capability or failed-validation reason, with the relevant references | No output digest or asset is invented; the affected readiness obligation stays unmet |

A produced asset may satisfy several requests when the relationship is explicit.
Multiple placements may reuse one asset without cloning its identity. Every
produced asset also records why it exists in the reading structure, including
assets chosen by the generator that were not individually requested by the owner.
Unresolved requests remain visible separately from the valid produced population.

The six produced kinds are the ASSET-CONTRACT.md roles. Their common envelope
contains asset identity, class/version, project and bundle identity, editorial
state, input/generation provenance and review references. Type-specific fields
are required only for that produced kind; unresolved computed references do not
pretend to contain a successful renderer digest or text equivalent.

## Content structure and identities

The bundle stores unique definitions for sections, claim blocks, supporting
assets, glossary entries and source anchors, with explicit typed references
between them. Identical labels never merge objects. Repeated rendered occurrences
retain the owning object identity; occurrence count is not distinct-claim count.
Distinct summaries offered simultaneously are separate blocks with their own
support and review bindings. Editing an existing unit follows its governing
identity/version discipline; it never changes the bytes or meaning of a
historical revision silently.

Provider-local handles are temporary references, never minted presentation or
kernel identities. The trusted recorded authoring operation issues opaque
presentation identities under RFC7-5 and retains the local-to-issued mapping in
its provenance. Generating a draft is recorded as draft production, not a human
authorship/adoption act. Existing identities can be referenced only through
validated owning records; neither a provider-supplied UUID nor an existing label
permits reuse or replacement. Effective editorial/profile/adoption state is
evaluated separately from serialized producer assertions. An unsigned profile
keeps every narrative element visibly unadopted even when generation succeeded.


The narrative roles remain anchored-project-fact, non-normative-framing and
epistemic-claim. Support references are confined to claims within their owning
block and must make each claim's actual support recoverable; an ambiguous block
must be split, not excused because every anchor resolves.

Canonical anchors use RFC7-10's target-specific variants:

| Variant | Identity and state required |
|---|---|
| Kernel entity | Owning RFC6 selection reference and optional fragment; captured evaluation identity plus verbatim label, tier and reason at authoring |
| Doctrine or accepted-contract citation | Stable owning rule/clause identifier, optional fragment and captured artifact revision |
| OpenSpec anchor | Artifact-contract identity/anchor, optional fragment and captured artifact revision |
| Decision or policy | Owning identifier, optional fragment and captured artifact revision |
| Evidence artifact | Owning evidence identifier, integrity digest, optional fragment and captured artifact revision |

No variant targets narrative, rendering or editorial draft. Captured state is
observed at the recorded authoring operation and never rewritten on later reads.
Missing/broken source resolution follows the governing primary-surface and
machine Unknown/reason/route behavior; no guessed rebinding or automatic successor
redirect makes an old anchor valid. Locators remain descriptive, not identities.

The existing PWB wire form has six local classes (doctrine, contract, requirement,
decision, evidence and work) and a universal revision field. Preserve that adopted
surface through an explicit compatibility adapter; do not promote that TypeScript
shape into the generic wire schema or assume a revision is an evaluation identity.
The adapter resolves each target through its owning typed route and preserves
its exact meaning. If the required canonical identity/state cannot be recovered,
report the typed inability to adapt rather than inventing it. PWB-specific
unstated/none conventions are not new global epistemic values. No generic policy
or kernel variant widens Butlers' adopted source/anchor admission.

Content is an inert tree of paragraphs, text spans, emphasis, inline code, lists
and trusted references. Tables use explicit headers and cell blocks; glossary
links name glossary entries; contents name real sections. Provider content cannot
supply raw HTML, script, styles, event handlers, external requests or arbitrary
embed URLs. Exact normative leaves use the existing verbatim route and owning
text, never the generated prose tree as a replacement source.

Section/asset containment and stage-input dependency graphs are acyclic; required
internal references resolve. Glossary cross-references may cycle. This does not
forbid cycles in a project's actual relationship graph:
diagram edges can represent supported cycles. Diagram nodes and edges reference
defined elements and carry support/markings, legend and equivalent structured
text. Neither a missing node nor an unsupported edge is repaired by inventing a
fact. Reference validation checks both directions: no dangling references and no
unused anchors or accidentally orphaned required content.

## Parse, resolve and judge separately

1. Bound bytes before parsing, then reject duplicate object keys, unknown
   versions/kinds, duplicate definitions and undeclared effect-bearing fields.
   Finite numeric budgets and structural bounds are validated before effects;
   null, missing or a numeric sentinel never means unlimited.
2. Validate the variant's required fields and internal structure. An unavailable
   expected execution-envelope value has the prescribed Unknown representation
   and reason; it is not an invalid record merely because it is unavailable.
3. Resolve identities, revisions, source roles, captured states, permissions and
   profile/registry acts against owning records. Pure shape validation grants no
   authority and cannot establish source fidelity.
4. Apply the independent inventory/fidelity and rendered-design review. Produced
   and structurally valid remain separate from ready, authored and accepted.

Validation failure retains only permitted bounded diagnostics and the unresolved
asset/run disposition. It cannot silently drop an offending field or array tail
and call the original output complete. Last-good authored presentation remains
governed by its own source/drift state, not overwritten by malformed generation.

## Version and migration behavior

Per-class versions are snapshot inputs under RFC3-22. An unsupported newer plane
is never written or downgraded; uninterpretable content renders Unknown rather
than a partially understood whole. Older supported content is read through its
declared interpretation/migration path without mutation on read. A persisted
migration requires its own reviewed, attributed, atomic and reversible act.
Migrations preserve minted identities, adoption state, attribution, timestamps,
consent scope, dismissal reasons/expiry, evidence digests and citation resolution.
A change to those meanings is a semantic change at the owning artifact's gate,
not a schema cleanup. OpenSpec artifacts remain outside this migration authority.
