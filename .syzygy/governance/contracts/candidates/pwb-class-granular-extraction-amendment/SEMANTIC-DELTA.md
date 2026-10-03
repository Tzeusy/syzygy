# Semantic delta — PWB class-granular extraction amendment (M15)

> **Candidate — binds nothing.** This package proposes one amendment to the
> signed PWB specification. Nothing here is signed, adopted or labelled
> accepted, and no implementation is authorized (VIS-4). Only the owner's
> version-tagged sign-off binds it, and building it needs a fresh
> implementation authorization after that.

**Artifact(s):** `openspec/changes/polaris-project-wide-butlers-model/`:
`specs/polaris-project-wide-butlers-model/spec.md` (the reader definitions
and PWB-REQ-002), `proposal.md`, `design.md`, `CAPABILITY-COVERAGE.md`, and
`GOVERNING-DEPENDENCIES.md` (regenerated).
**Stable IDs affected:** PWB-REQ-002. No identifier is added, renumbered or
retired.
**Change class:** Normative. PWB-REQ-002's "never a partial item set" rule
is narrowed from the whole source to each class of a source, and two
obligations are added: surface unenumerated headings, and qualify counts made
without a read root index. An implementation that complied before does not
comply now.
**Author:** a drafting session (Claude), bead `syzygy-dov.15.1`.
**Date:** 2026-10-03, over `main` at `ef5d5f03`.

## Warrant

[Observed] Ruling P-82, on funnel move M15, in
`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
line 70. Its Ruled column, quoted:

> **A** — Q1 arm (b), draft the delta only; Q2 design `partially-extracted`
> inside it, build only after sign-off and a fresh authorization; Q3 design
> the `unenumerated-heading` reason as surface-flag (a counted, routed
> Unknown); Q4 design the root-independence flags in the same delta.

The record's "What it means" column, which is the recorder's gloss and not
the owner's words, reads: "One CC-REV-2 semantic delta to PWB-REQ-002 under
`NORMATIVE-CHANGE-WORKFLOW.md`, sequenced behind lane B's open manifest; no
extraction, manifest or coverage code changes; no Butlers source read beyond
the consented class."

- **The sequencing condition is spent.** [Observed] Lane B was declined and
  closed on 2026-10-02
  (`decisions/POLARIS-LANE-B-DECLINED-AND-TARGET-REVISED-DIRECTION.md`).
- **The base is the signed container-shape text.** [Observed] The
  container-shape profile amendment (N8) was signed as v1.0 on 2026-10-02
  (`decisions/PWB-CONTAINER-SHAPE-PROFILE-AMENDMENT-SIGNOFF-v1.0.md`) and its
  patches are applied. This delta is drafted over those applied bytes, as a
  separate package. That package's question 8 asked whether to keep the two
  separate and recommended keeping them separate; it was signed alone.
  [Inferred] That is the separation this package follows; the sign-off
  record quotes the owner's selection, which does not name question 8.
- **The sign-off route.** [Observed] The Scope A direction
  (`decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`, item
  1) covers "the PWB specification deltas". This package is one, so it is
  signed by version tag, with no phrase or digest argument.

## Evidence or decision basis

- **The funnel packet the owner ruled on:**
  `docs/design/POLARIS-M15-PIPELINE-TRUTHFULNESS-FUNNEL.md`, with its four
  questions, their arms and its measurements at Syzygy `a9f671e`.
- **The code it measured**, re-read at `ef5d5f03` [Observed]:
  - `packages/three-surface-poc-core/src/project-shape-extraction.ts`
    states the current contract in its module comment, lines 14–17: "Any
    grammar failure … makes the whole source's item denominator Unknown. A
    source never yields a partial item set."
  - `extractSource` (same file, from line 628) returns
    `{ kind: 'unknown', … }` on the first class that fails, discarding the
    items the loop already holds.
  - `CATALOG_HEADINGS` (lines 56–66) is nine literals, and
    `extractCatalogEntries` (from line 438) reads only those nine headings.
    Nothing scans for a tenth.
- **No Butlers body was read** for this package.

## What changes, and why each part has the shape it has

### 1. Class granularity (P-82 Q1 and Q2)

Each class a source is assigned is read on its own. A grammar failure fails
the one class whose row it reads, in that source. The source's other classes
keep their items and their own denominators. A source with some failed and
some read classes is **partially extracted**: its own item denominator is
Unknown, and it states each class's outcome. A class that fails still yields
none of its items: the "no partial item set" rule now holds per class, not
per source.

- **Aggregates.** A class's denominator across its sources, and its
  category's, is Unknown whenever the class is Unknown in any source. This
  is the rule the container-shape amendment already states for an
  unreadable class ("that class's item denominator and its category's item
  denominator render Unknown"), applied to a failed class.
- **"Fails the source".** The signed shape and key-form sentences say a
  defect "fails the source as missing-heading", and so on. Rather than
  rewrite each, one sentence in the shared heading rules defines it: it
  fails the class whose row it reads, in that source.
- **What still fails a whole source.** An unavailable, unclassifiable or
  excluded body, or a resource-limit breach, leaves no class readable.
  PWB-REQ-003 and PWB-REQ-006 own those cases, and nothing about them moves.

### 2. Unenumerated headings (P-82 Q3, "surface-flag")

A list or table row that declares two or more headings at one level
**encloses** that level. In each section one level up that holds one of
them, any other heading at that level that no row of the source's grammar
declares is an **unenumerated heading**.

- **It mints nothing and fails nothing.** The declared headings keep their
  items.
- **It is surfaced:** text, level and exact source anchor, with a route to
  the source. That is the "routed" part of the ruling.
- **It is counted:** the class's item denominator in that source renders
  Unknown with the reason `unenumerated-heading` and the count of such
  headings. That is the "counted Unknown" part.

[Inferred] Why the denominator is Unknown rather than counting each heading
as one Unknown item: the items beneath an unenumerated heading are not read,
so the true denominator is not known. Treating the heading as one item would
give a known denominator that is wrong (VIS-2). The modeled items stay
modeled, so nothing true is withdrawn.

[Inferred] Why the rule is drawn at list and table rows with two or more
headings at one level: that is the shape of the V1 catalog (nine level-3
headings, one bulleted-list row), the case the funnel measured. A
`heading-section` row is excluded on purpose: Butlers' V1-scope row names two
level-2 headings in the V1 index, and enclosing that level would flag every
undeclared level-2 heading in that file, where a level-2 heading need not name
a category at all. Separately, the "no row of the source's grammar declares"
clause keeps a heading that another class reads from being flagged.

[Unknown] Whether Butlers' V1 index has a level-3 heading outside the nine
inside the level-2 sections that hold the catalog. No Butlers body was read
for this package. If it has, building this amendment makes Butlers'
catalog-entry and Heart and Soul denominators Unknown until the heading is
declared or removed. That is the honest outcome, and it is stated here
before signing so it is not a surprise.

Out of scope: the funnel also named root-summary and precedence headings.
Those grammars belong to PWB-REQ-004, not PWB-REQ-002, so this delta leaves
them alone (see "What explicitly does not change").

### 3. Root independence (P-82 Q4)

Each population rule declares whether it needs the root index read, and
every source carries the name of the rule that admitted it.

- **Values.** The pillar-root and pillar-index rules need it. The
  baseline-spec and roster rules do not, because these definitions write
  their path patterns rather than the root index naming them.
- **Unread root index, rule that needs it:** it mints no item. Each source
  its tree pattern matches stays counted with an Unknown item denominator
  and the reason that the root index was not read.
- **Unread root index, rule that does not need it:** it still admits its
  sources, and every class and category count that includes one of them
  says it was derived without a read root index.
- **Loaded profiles.** A profile's tree population declares
  `rootIndexRequired`, true or false. One that does not declare it needs
  the root index: the fail-closed default.
- **Butlers.** Its baseline-spec and roster tree populations are declared
  as not needing it, so Butlers' manifest admits the same sources as today.
  The funnel's own falsifier for this slice was that Butlers' manifest
  digest must not move; that is an implementation check, named in the
  ledger.

[Inferred] Why baseline specs and roster directories are declared
independent rather than dependent: their existence in the Git tree is
observed directly, and declaring them dependent would turn true counts into
Unknown for a reader that already has the evidence. The funnel's
counter-argument stands, and is put to the owner as question 3 in the
packet: whether those two populations are "genuinely" root-independent is a
reader-definition choice. Either way, the qualification means no count made
under an unread root index is shown as if the root had been read (VIS-1).

## Current meaning, and proposed meaning

Quoted from the patch, hunk by hunk, in file order. "Current" is the signed
text the hunk replaces; a hunk with no current text only adds. Every other
byte of the specification is unchanged, and the builder checks that.

### Hunk 1 — Reader definitions — the source-path population

Current:

```text
(nothing; this hunk only adds)
```

Proposed:

```text
  - Each rule declares whether it needs the root index read, and every
    source carries the name of the rule that admitted it. The pillar-root and
    pillar-index rules need the root index; the baseline-spec and roster
    rules, whose path patterns these definitions write, do not.
  - When the root index was not read, a rule that needs it mints no item:
    each source its tree path pattern matches stays counted in the
    source-path population with an Unknown item denominator, giving the
    reason that the root index was not read.
  - When the root index was not read, a rule that does not need it still
    admits its sources, and every class and category item denominator that
    counts one of them states that it was derived without a read root index.
```

### Hunk 2 — Reader definitions — shared heading rules

Current:

```text
(nothing; this hunk only adds)
```

Proposed:

```text
  - Wherever a shape or key form below fails the source, it fails the class
    whose row it reads, in that source, as the exactness rules below state.
  - A list or table row that declares two or more headings at one level
    encloses that level: within the section of each heading one level higher
    that holds one of them (or the whole file, when the level is 1 or no
    such heading holds them), a heading at that level that no row of the
    source's grammar declares is an unenumerated heading.
    - An unenumerated heading mints no item and fails nothing: the row's
      declared headings keep their items.
    - It is surfaced, never skipped: the machine answer and Polaris give its
      text, its level and its exact source anchor, and route to that source.
    - The class's item denominator in that source renders Unknown with the
      reason unenumerated-heading and the count of such headings, because the
      items beneath them are not read.
```

### Hunk 3 — Reader definitions — the project profile's tree population

Current:

```text
    `<key>` segment is a single directory name.
```

Proposed:

```text
    `<key>` segment is a single directory name, and by `rootIndexRequired`,
    true or false; a tree population that does not declare it needs the root
    index.
```

### Hunk 4 — Reader definitions — exactness

Current:

```text
  - A missing heading, malformed row/list/TOML, unexpected duplicate key or
    ambiguous leading label makes the enclosing source's item denominator
    Unknown; it never produces a partial item set.
```

Proposed:

```text
  - Each class a source is assigned is read on its own. A missing heading,
    malformed row/list/TOML, unexpected duplicate key or ambiguous leading
    label in any of a class's rows fails that class in that source: the
    class's item denominator in that source is Unknown, with the failure as
    its reason, and the class yields none of its items from that source. A
    class that fails never produces a partial item set; an unenumerated
    heading is not a failure, and the items it leaves in place are complete
    for the headings the row declares.
  - A source in which a class fails keeps every other class it is assigned:
    each class that reads without failure keeps its items and its own item
    denominator. A source in which some classes fail and others read is
    partially extracted: its own item denominator is Unknown, and it states
    for each class either its items and denominator or its failure and
    reason.
  - A class's item denominator across its sources, and its category's, is
    Unknown whenever the class is Unknown in any of those sources; the items
    of the sources where it read stay modeled and counted.
  - A source whose body is unavailable, unclassifiable or excluded, or whose
    read breaches a resource limit, has no class that reads: every class it is
    assigned has an Unknown item denominator in it.
```

### Hunk 5 — Reader definitions — Butlers' `baseline-spec` grammar

Current:

```text
    openspec/specs/<one-directory>/spec.md; the one directory is the key.
```

Proposed:

```text
    openspec/specs/<one-directory>/spec.md; the one directory is the key; its
    tree population does not need the root index.
```

### Hunk 6 — Reader definitions — Butlers' `roster-identity` grammar

Current:

```text
    `[butler].name` must be non-empty.
```

Proposed:

```text
    `[butler].name` must be non-empty; its tree population does not need the
    root index.
```

### Hunk 7 — PWB-REQ-002 — requirement text

Current:

```text
(nothing; this hunk only adds)
```

Proposed:

```text
Each class of a source SHALL be accounted for on its own: a class that fails
in a source SHALL leave its own item denominator there Unknown without
withholding the items of any other class the source reads; a heading that a
class's grammar does not enumerate SHALL be surfaced, never skipped; and a
count derived without a read root index SHALL say so wherever it is shown.
```

### Hunk 8 — PWB-REQ-002 — Case and Observable

Current:

```text
  loaded profile.
  the machine answer and reachable from Polaris.
```

Proposed:

```text
  loaded profile; also a source assigned three classes in which one class
  fails and two read, a section enclosing the V1 catalog headings that holds
  a tenth level-3 heading, and an observation whose root index was not read
  while baseline specs and roster directories exist in the tree.
  the machine answer and reachable from Polaris, together with each partially
  extracted source's per-class outcome, each unenumerated heading with its
  anchor and route, and each root-index qualification.
```

### Hunk 9 — PWB-REQ-002 — Oracle and Falsifier

Current:

```text
  denominator.
- **Falsifier**: the independent extractors disagree, a malformed source emits
  a partial population, a known source disappears, an admitted item appears twice or
```

Proposed:

```text
  denominator. The comparison is made per source and class: both extractors
  must name the same failed classes with the same reasons, and the same
  identities and D for every class that reads, so a failed class's D is
  Unknown while each sibling's D is known; an independent scan of each
  enclosing section finds every unenumerated heading, and each one is
  surfaced; and with the root index unread, every source a rule that does not
  need it admitted carries the qualification, while no source of a rule that
  needs it mints an item.
- **Falsifier**: the independent extractors disagree, a failed class emits a
  partial population, a failed class withholds the items of a sibling class
  that reads, a class or category item denominator that counts a failed class
  or an unenumerated heading is presented as known, an unenumerated heading is
  skipped or mints an item, a count derived without a read root index is shown
  without that qualification, a rule that needs the root index mints an item
  when it was not read, a known source disappears, an admitted item appears twice or
```

### Hunk 10 — PWB-REQ-002 — scenarios

Current:

```text
(nothing; this hunk only adds)
```

Proposed:

```text

#### Scenario: A failing class keeps its siblings

- **WHEN** a source is assigned three classes and one of them fails its
  grammar while the other two read
- **THEN** the failed class's item denominator in that source, its class's
  and its category's item denominators render Unknown with the failure's
  reason
- **AND** the two classes that read keep their items modeled and their own
  item denominators known

#### Scenario: An unenumerated heading is surfaced, not skipped

- **WHEN** a section that holds the V1 catalog headings also holds a level-3
  heading outside the nine
- **THEN** that heading is surfaced with its text and exact source anchor,
  routes to its source and mints no item
- **AND** the items under the nine headings stay modeled while the
  catalog-entry and Heart and Soul item denominators render Unknown with the
  reason unenumerated-heading

#### Scenario: Counts derived without a read root index say so

- **WHEN** the root index was not read and the tree holds baseline specs and
  roster directories
- **THEN** the baseline-spec and roster sources are admitted and every class
  and category count that includes them states that it was derived without a
  read root index
- **AND** no source of a rule that needs the root index mints an item
```

## What explicitly does NOT change

- **Every other requirement.** PWB-REQ-001 and PWB-REQ-003 to PWB-REQ-022
  are byte-identical. In particular:
  - **PWB-REQ-003** still keeps a missing, unreadable, unclassifiable or
    excluded source counted with an Unknown item denominator.
  - **PWB-REQ-004** keeps its closed fact families. An unenumerated heading
    mints no `catalog-count` declaration; that family stays at nine. Its
    root-summary and precedence grammars are untouched.
  - **PWB-REQ-006** still makes a resource breach Unknown for the affected
    population.
  - **PWB-REQ-020** parity is unchanged in text. [Inferred] The new machine
    fields (per-class outcomes, unenumerated headings, the root-index
    qualification) fall under its existing "every fact Polaris presents"
    reach; the ledger names the parity families an implementation adds.
- **PWB-REQ-002's existing obligations.** Its six signed scenarios, its
  warrants and every other verification limb stay. "A malformed source
  emits a partial population" is the one falsifier limb replaced, by the
  per-class limbs.
- **The closed vocabularies.** Nine shapes, eight key forms and nine classes
  stay closed. `unenumerated-heading` is a denominator reason, not a new
  failure, shape or key form.
- **The source-path denominator** still never shrinks.
- **No contract-coverage row moves.** [Observed] `CONTRACT-COVERAGE.md`
  regenerates byte-identical over the proposed bytes (the builder refuses
  otherwise), and no warrant changes. [Inferred] The two rows nearest this
  change stay true: RFC6-16.c2, "Partial/filtered result never presented as
  full scope", and RFC2-23.c5, "Partial snapshot declares captured scope;
  uncaptured portion Unknown; no full-scope aggregate". A partially
  extracted source is exactly that kind of declared partial.
- **No doctrine, contract, policy, registry entry or performed act.**

## Terms introduced / retired

Introduced, each defined in the reader definitions: *partially extracted*;
*unenumerated heading*, with the reason `unenumerated-heading`; and the
profile field `rootIndexRequired`. None is retired.

## Downstream impact

See `IMPACT-LEDGER.md` for the sweep, its predicate and its denominator. In
short:

- **Companions** in the same change (CC-REV-2): a proposal bullet, design
  decision 12 and a design note on the discovery rules, capability row 34,
  and the regenerated dependency file.
- **Implementation:** the extraction, coverage and manifest modules and
  their tests. Sign-off authorizes none of it.
- **The pending sibling:** the release-label amendment (P-85) also adds a
  design decision 12 and a capability row 34. Whichever is signed second is
  regenerated over the first's applied bytes and re-reviewed. Both builders
  classify the other as pending.
- **The drafted registry fields:** `syzygy-dov.24` (PR #123, open) drafts the
  loaded profile's registry fields. `rootIndexRequired` would join them; that
  package does not carry it today.

## Migration / supersession plan

- **Supersession.** At sign-off, the patches apply in one change through
  `--apply --at-adoption`, which refuses unless the whole package verifies.
  The signing change becomes the next link in the PWB successor chain; the
  act, not this package, decides that.
- **Residuals the signing change must carry** [Observed at `ef5d5f03`]:
  1. Add the package to `scripts/record_versioned_signoff.py`
     `real_packages()`.
  2. `scripts/check_spec_reconciliation.py` hard-codes the PWB census. After
     `--apply` it reads 17 requirements and 54 scenarios, with PWB-REQ-002
     at 9 (it is 51 and 6 today). The signing change updates the literal
     census and `census.json`, and appends this sign-off to the PWB child's
     successor tuple.
  3. Add the builder's `--check` to the `PROJECT-STATUS.md` battery under
     the CG-26 coupled-triple rule. A draft leaves the battery alone.
  4. The observer registry entry and the secret-classification policy pin a
     PWB spec digest; both are already stale and Unknown until their own
     act (`syzygy-jloi`). Signing this moves the digest again.
- **Implementation** needs its own authorization, after sign-off.

## Review

**Required class:** full review (Normative, CC-REV-1), one fresh-context
round, raw retained verbatim.
**Reviewer:** a fresh-context agent that did not draft this package.
**Verdict:** recorded in `ROUND-1-DISPOSITIONS.md` beside this file, copied
from the raw.
