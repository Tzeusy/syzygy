> **Candidate — binds nothing.** This semantic delta is drafted under P-81 Q5
> and CC-REV-2. It performs no act, amends no signed byte and authorizes no
> implementation. The 2026-09-05 PWB specification remains in force unless the
> owner later performs a dedicated amendment act over the final reviewed
> manifest.

# Semantic delta PWB-ITEM-DEPTH-1 — every declared catalog item can be read in depth

**Artifact(s):** the eleven-artifact signed
`openspec/changes/polaris-project-wide-butlers-model/` behavior package. Five
proposed rows move: `spec.md`, `design.md`, `CAPABILITY-COVERAGE.md`,
`CONTRACT-COVERAGE-REPAIR-DELTA.md` and the regenerated
`GOVERNING-DEPENDENCIES.md`. The other six manifest rows equal current bytes.

**Stable IDs affected:** `PWB-REQ-015`, amended in place. `PWB-REQ-011`,
`PWB-REQ-014`, `PWB-REQ-016` and `PWB-REQ-020` are reached and unchanged.
No identifier is minted, retired, renamed or renumbered.

**Change class:** **Normative.** A conforming implementation today may expose
only one capability deep dive. The proposed obligation covers the complete
declared `catalog-entry` population and adds observable identity, mapping,
absence and path requirements. Someone conforming before may not conform
afterward.

**Author:** agent drafting for bead `syzygy-dov.14.2`.

**Date:** 2026-09-27.

## Current meaning

PWB-REQ-015 currently reads, in full:

```markdown
### Requirement: PWB-REQ-015 — Capability detail preserves authority bands and exact intent

Group: Presentation. Form: **invariant**.

Every capability deep dive SHALL contain, in order, an `argument` band marked
non-normative, a `contract` band with verbatim current requirement/scenario,
governing doctrine and non-goal text, and a `reality` band sourced only from
the shared model. Draft capabilities SHALL remain unadopted. Proposed deltas SHALL be adjacent to current text,
visibly distinct, non-anchorable and unable to grant status; competing
proposals SHALL remain separate candidate futures.
The default reading mode SHALL be `Base` and include observed reality. Every
block SHALL carry exactly one of the three band-class attributes. No
reorganized or stored normative copy of doctrine, non-goal, requirement or
scenario text SHALL exist outside its owning artifact.

- **Case (sweep)**: enumerate every capability deep dive at an evaluation that
  includes current intent, a draft capability and two incompatible proposals.
- **Observable**: Base mode, band class/order, verbatim current text, proposal lifecycle,
  non-anchorability and separate futures are recoverable in both channels.
- **Oracle**: compare current requirement/scenario, doctrine and non-goal bytes
  to their owning artifacts, compare
  proposal identities/exclusivity to captured changes, exhaust band and anchor
  populations and perform a static-source sweep for normative copies; exact
  bytes/order, exactly one class per block, zero stored copies and zero proposal
  authority decide.
- **Oracle independence**: current/proposed artifacts and exclusivity inputs
  come from captured OpenSpec state, not Polaris.
- **Falsifier**: a missing/misordered band, summarized normative text, draft
  rendered adopted, proposal substituted/interleaved/anchored/green, or
  competing proposals collapsed.

#### Scenario: Proposed work stays beside exact current intent

- **WHEN** a declared capability has an active proposal
- **THEN** the contract band renders current requirement text verbatim
- **AND** the proposal remains adjacent, distinct, non-anchorable and non-status-bearing

```yaml
warrants:
  primary: RFC7-17
  doctrine: [VIS-1, VIS-2, VIS-4]
  contracts: [RFC1-14, RFC1-27, RFC7-12, RFC7-13, RFC7-14, RFC7-15, RFC7-17, RFC7-18, RFC7-26, RFC7-27, RFC7-29, RFC7-33]
  policies: [CC-BAR-3, CC-BAR-5, CC-TEST-5]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: []
```
```

This requires the three bands for capability deep dives, but does not require
one detail per declared catalog item or define the honest result when an item
has no unique declared relation to current normative intent.

## Proposed meaning

The proposed replacement is exactly the `spec.md.patch` result. It preserves
the warrant block byte-for-byte:

```markdown
### Requirement: PWB-REQ-015 — Item detail preserves authority bands and exact intent

Group: Presentation. Form: **invariant**.

Every item in the complete declared `catalog-entry` population SHALL have one
item-detail reading keyed by that item's stable semantic claim identity. An
existing capability deep dive SHALL be that reading for the matching declared
catalog item; no second detail or identity SHALL be created for it.

Every item detail SHALL contain, in order, an `argument` band marked
non-normative, a `contract` band, and a `reality` band sourced only from the
shared model. The argument band SHALL NOT create intent, authority, status or
a capability identity. The contract band SHALL contain only captured governing
identities and verbatim-reachable current requirement/scenario, governing
doctrine and non-goal text. When the evaluation captures no unique declared
mapping from the item to such current intent, the contract band SHALL collapse
to one honest absence carrying the item's Unknown reason and resolution route;
it SHALL NOT infer a mapping from a label, basename, similarity or generated
prose. Draft capabilities SHALL remain unadopted. Proposed deltas SHALL be
adjacent to current text, visibly distinct, non-anchorable and unable to grant
status; competing proposals SHALL remain separate candidate futures.

The catalog-to-detail-to-exact-source path SHALL preserve the item's stable
identity and complete epistemic state at every altitude, in both channels,
without making a URL, label, path or coordinate part of that identity.
The default reading mode SHALL be `Base` and include observed reality. Every
block SHALL carry exactly one of the three band-class attributes. No
reorganized or stored normative copy of doctrine, non-goal, requirement or
scenario text SHALL exist outside its owning artifact.

- **Case (sweep)**: enumerate the complete declared `catalog-entry` population
  at an evaluation that includes a uniquely mapped current intent, an item with
  no declared intent mapping, a draft capability, a contradicted item and two
  incompatible proposals.
- **Observable**: every declared item reaches exactly one item detail; Base
  mode, stable identity, complete epistemic state, band class/order, verbatim
  current text or honest absence, proposal lifecycle, non-anchorability and
  separate futures are recoverable in both channels.
- **Oracle**: derive the expected item population and identity/state tuples
  from the shared model; derive item-to-intent mappings only from captured
  declared relations; compare current requirement/scenario, doctrine and
  non-goal bytes to their owning artifacts; compare proposal identities and
  exclusivity to captured changes; exhaust detail, band and anchor populations;
  and perform a static-source sweep for normative copies. Exact population,
  identity/state equality, exact bytes/order, exactly one class per block,
  honest absence for every unmapped item, zero stored copies and zero proposal
  authority decide.
- **Oracle independence**: expected items and tuples come from the shared model,
  while current/proposed artifacts, declared mappings and exclusivity inputs
  come from captured authority, never from Polaris or route output.
- **Mutation proof**: independently drop and duplicate an item detail, map an
  item by label alone, remove the unmapped-item absence, reorder two bands,
  assign two classes to one block, substitute proposal text for current text,
  and source a reality fact outside the shared model; confirm the oracle fails
  before restoration and reports the complete item denominator each time.
- **Falsifier**: a missing/duplicate item detail, changed item identity or
  epistemic state, inferred or ambiguous intent mapping, hidden empty contract
  band, missing/misordered/multiply-classed band, summarized normative text,
  second reality computation, draft rendered adopted, proposal substituted,
  interleaved, anchored or green, or competing proposals collapsed.

#### Scenario: Catalog item reaches exact current intent or honest absence

- **WHEN** a reader opens a declared catalog item from the catalog
- **THEN** its detail preserves the item's identity and epistemic state and its
  contract band renders uniquely declared current intent verbatim
- **AND** if no unique declared mapping exists, the band renders one honest
  Unknown absence with reason and route rather than guessed intent
- **AND** every proposal remains adjacent, distinct, non-anchorable,
  non-status-bearing and separate from competing candidate futures

```yaml
warrants:
  primary: RFC7-17
  doctrine: [VIS-1, VIS-2, VIS-4]
  contracts: [RFC1-14, RFC1-27, RFC7-12, RFC7-13, RFC7-14, RFC7-15, RFC7-17, RFC7-18, RFC7-26, RFC7-27, RFC7-29, RFC7-33]
  policies: [CC-BAR-3, CC-BAR-5, CC-TEST-5]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: []
```
```

## What explicitly does NOT change

- The three bands, their order and their three closed authority classes.
- Current authority remains operative; proposal material remains adjacent,
  separate, non-anchorable and unable to grant status.
- Verbatim text remains owned by its authoritative artifact and is not stored
  in Polaris.
- Capability identity is still declared, never inferred from a catalog row.
- PWB-REQ-011's exact-source authority, content class and fail-closed gates.
- PWB-REQ-014's anchor and non-citability rules, PWB-REQ-016's nonvisual and
  keyboard requirements, and PWB-REQ-020's tuple parity.
- Consent, policy, registry, response ceilings, retention, egress, writes,
  execution, deployment, release and the one-repository POC boundary.

## Warrant

P-81 Q5 authorizes drafting this delta only. The ruling is recorded in
`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`; it explicitly says the
candidate binds nothing and implementation requires a fresh authorization.
The M14 funnel records the observed one-capability implementation and the
request to let catalog items reach per-item depth.

## Evidence or decision basis

- `docs/design/POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md`, Q5 and Gate 4 slice 5.
- `docs/evidence/polaris-m14-provenance-depth-funnel-2026-09-17.json`.
- PWB-REQ-015's current signed bytes and its performed 2026-09-05 act record.
- RFC7-12 through RFC7-19 and RFC7-26/27/29/33/34.

The funnel review is evidence of the question presented, not confirmation of
this later semantic delta.

## Terms introduced / retired

**Introduced:** `item detail`, the detail reading for one declared
`catalog-entry`, keyed by the item's existing stable semantic claim identity.
It generalizes the current capability deep dive without turning every item into
a capability.

**Retired:** none. `Capability deep dive` remains the item-detail form for a
matching declared capability.

## Downstream impact

`IMPACT-LEDGER.md` records the methods, denominator, overlap and disposition.
Five signed subjects move in the proposed bytes. Implementation files are
named only as future consumers and are unchanged here.

## Migration / supersession plan

1. Review the exact candidate and manifest in fresh context under
   `REVIEW-BRIEF.md`; retain raw output verbatim.
2. Resolve every finding. Any semantic repair retires the review and requires
   a fresh independent review of the repaired exact bytes.
3. The owner chooses this package's position relative to the already directed
   `.21 → .30 → .22 → lane B` chain and any intervening PWB successors.
4. Regenerate the patches, dependency declaration, manifest and packet digest
   against the actual predecessor. A changed predecessor retires prior review
   and any copied argument.
5. Only then may the owner be offered the dedicated act phrase. A recorder
   applies all proposed bytes and records the dedicated and aggregate act in
   one logical change. This draft creates no chain link.
6. Implementation remains a separate bead behind a fresh explicit owner
   authorization. Adoption alone authorizes no code or body read.

Rollback before adoption is deletion or reversion of this inert candidate.
After adoption, rollback is another reviewed and owner-signed successor; no
performed act or historical manifest is edited.

## Review

**Required class:** CC-REV-1 full fresh-context review plus CC-REV-4/VIS-3
fresh-reader comprehension. The package is Normative and gate-bound.

**Reviewer:** unassigned; must not have authored this package or shared this
session.

**Verdict:** not yet reviewed.
