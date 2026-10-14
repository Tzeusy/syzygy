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
**Date:** 2026-10-03, over `main` at `ef5d5f03`. Repaired 2026-10-14 over
`main` at `8f1fbec7`, under the owner's direction of that day (relayed to
the drafting session by the lead session; no decision record holds it yet
— *marked 2026-10-14: the direction is now recorded in
`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`*),
for the eight round-2 findings (`ROUND-2-DISPOSITIONS.md`). [Observed] The
signed change directory and the two code files cited below are
byte-identical at the two commits (`git diff --stat ef5d5f03 8f1fbec7` over
those paths is empty), so every [Observed at `ef5d5f03`] claim about them
still holds. These repaired bytes are **unconfirmed**: no round has read
them. *(Marked 2026-10-14: round 3 read them at `00e24fd2` and returned
`REVISE`.)* Repaired again 2026-10-14 (cycle 2), over `main` at `814fbcc1`,
for the five round-3 findings (`ROUND-3-DISPOSITIONS.md`), on a further
owner direction of that day for one more cycle. [Observed] The anchor-resolution
sign-off (P-96, v1.0) moved the signed `spec.md` and its regenerated
dependency file between `8f1fbec7` and `814fbcc1`; the patches were
regenerated over those bytes by the builder's `--write`. The two code files
cited below are byte-identical at `8f1fbec7` and `814fbcc1` (`git diff
--stat` over them is empty). **Round-3 findings repaired once on
2026-10-14, unconfirmed pending round 4.**

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
some read classes is **partially extracted**, and states each class's
outcome. A class that fails still yields none of its items: the "no partial
item set" rule now holds per class, not per source.

- **The source's own denominator.** A source's own item denominator is
  Unknown whenever any class it is assigned is Unknown in it, for any
  reason: a failed class, or a class with an unenumerated heading. So a
  source whose every class reads but one carries an unenumerated heading is
  extracted, not partially extracted, and its own denominator is still
  Unknown. [Inferred] Without this, the V1 index could show a known item
  total while the items under an extra heading go unread (VIS-1).

- **Aggregates.** A class's denominator across its sources, and its
  category's, is Unknown whenever the class is Unknown in any source. This
  is the rule the container-shape amendment already states for an
  unreadable class ("that class's item denominator and its category's item
  denominator render Unknown"), applied to a failed class.
- **"Fails the source".** The signed shared heading rules, shape sentences
  and key-form sentences say a defect "fails the source as missing-heading",
  and so on. Rather than rewrite each, one sentence placed after the shared
  heading rules defines it for all three: wherever the shared rules above
  it, or a shape or key form below it, fail the source, the failure fails
  the class whose row it reads, in that source. (Round 2 found that the
  first wording, "a shape or key form below", left out the shared rule
  directly above it.)
- **Signed text whose meaning changes without a byte changing.** Two signed
  passages are kept word for word, but read differently once the exactness
  rule is per class:
  - the loaded-profile sentence that a class with an invalid or missing row
    "is unreadable: … each source any of its rows names fails as a source in
    which a class fails";
  - the signed scenario "Loaded profile names a shape outside the
    vocabulary".

  Under the signed exactness rule, "a source in which a class fails" lost
  every class it was assigned. Under this amendment it is a source in which
  that one class fails: the unreadable class is Unknown there, and every
  other class the source is assigned keeps its items and its own item
  denominator. The source is partially extracted and its own item
  denominator is Unknown. [Inferred] This is the intended effect, and it is
  named here because no byte of those passages shows it.
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
level-2 headings in `v1.md`, and enclosing that level would flag every other
level-2 heading in the file, including those other classes declare. The
"declared by any row of the source's grammar" clause stops a heading another
class reads from being flagged.

[Unknown] Whether Butlers' `v1.md` has a level-3 heading outside the nine
inside the level-2 sections that hold the catalog. No Butlers body was read
for this package. If it has, building this amendment makes Butlers'
catalog-entry and Heart and Soul denominators Unknown until the heading is
declared or removed. That is the honest outcome, and it is stated here
before signing so it is not a surprise.

**Not carried: root-summary and precedence headings.** The funnel's Q3,
which you ruled on without narrowing it, also named "an unenumerated
root-summary or precedence heading". Those grammars belong to PWB-REQ-004,
not PWB-REQ-002, so this delta leaves them alone (see "What explicitly does
not change"). That leaves half of the Q3 ruling undesigned. The drafter took
this reading from the record's gloss ("One CC-REV-2 semantic delta to
PWB-REQ-002"), which is not the owner's words, so the packet puts it to you
as question 6: defer the root grammars to a separate PWB-REQ-004 delta, or
widen this package. It is also the open owner question under "Migration /
supersession plan" below.

### 3. Root independence (P-82 Q4)

Every source carries the name of the rule that admitted it, and each
population rule declares whether it needs the root index read.

- **Rule names, bound to the four signed rules.** The signed sentence closes
  the source-path population by four rules and names none of them. This
  amendment binds a closed set of five names to them:

  | Signed rule | What it admits | Name |
  |---|---|---|
  | 1 — the five pillar roots named in the root index | the root index itself | `root-index` |
  | 1 | each named pillar root's own index file | `pillar-index` |
  | 2 — files named by each pillar's own index | each such file | `pillar-named-file` |
  | 3 — baseline `openspec/specs/*/spec.md` entries | each baseline spec | `baseline-spec-tree` |
  | 4 — roster directories containing `butler.toml` | each `butler.toml` and its `MANIFESTO.md` | `roster-tree` |

  A source that a loaded profile's tree population admits carries that
  population's `pathPattern` as its rule name.
  - **A source two rules admit carries one name** (added 2026-10-14 for
    round-3 finding 1). The four signed rules overlap: a pillar declared at
    `openspec/` can name a baseline spec, a pillar declared at `roster/` a
    `butler.toml` or a `MANIFESTO.md`, and a pillar's index file could be
    named by another pillar's index. The reader definitions now state the
    order: the root index is always `root-index`; a pillar's index file is
    always `pillar-index`; a baseline spec, a roster `butler.toml`, or a
    source of a loaded profile's tree population, is admitted by that tree
    population alone, with its class, whoever else names it; any other file a
    pillar's index names, a roster `MANIFESTO.md` included, is
    `pillar-named-file`; and a source two tree populations of one loaded
    profile admit takes the first the profile declares.
    - [Observed at `814fbcc1`] For Butlers' built-in grammar this is the
      code's order in `project-shape-manifest.ts`: `addSource` keeps the
      first registration (line 393); the root index is registered first
      (lines 403–405); rule 2 skips a named blob matching the baseline-spec
      or roster `butler.toml` pattern so that rules 3 and 4 own it "whoever
      names it" (lines 470–478); and a roster `MANIFESTO.md` is not skipped,
      so a pillar-named one keeps `pillar-named-file` (line 478 tests only
      `butler.toml`). The earlier text's "the fourth admits … its
      `MANIFESTO.md` … as `roster-tree`" stays true for a `MANIFESTO.md` no
      pillar index names, which is the only case the fourth rule alone
      admits.
    - [Inferred] One case differs from the code. The code registers pillars
      one at a time in `PILLAR_KEYS` order (line 47), each pillar's index and
      then its named files, so a pillar index that an *earlier* pillar's
      index names (possible only when one declared pillar root lies inside
      another) is filed `pillar-named-file`. The text files it
      `pillar-index`. [Unknown] Whether Butlers declares nested pillar roots
      at `32f38feb`; no Butlers body was read. The packet puts the choice to
      the owner as question 8: the text's order, with the code changed at
      build, or the code's order written into the text.
    - [Inferred] The loaded-profile clauses are readings: no loader exists
      (no `pathPattern` occurs in `packages/` at `814fbcc1`), so no code
      settles them. They follow the code's own reason for rules 3 and 4,
      that the tree population carries the class. Question 8 covers them.
    - The oracle and falsifier now decide a doubly admitted source by this
      order, and a fourth new scenario asserts the `openspec/` and `roster/`
      cases.
  - [Observed at `8f1fbec7`] These are exactly the five values of
    `SOURCE_RULES` in `packages/three-surface-poc-core/src/project-shape-manifest.ts`
    line 71, and that module's own comment files the root index under
    rule 1 ("Rule 1 — the root index and the pillar roots it names", line
    403).
  - [Inferred] Reading the root index itself as a rule-1 source is a
    reading of the signed sentence, which names the root index only as what
    rule 1 reads. The alternative, scoping the provenance obligation to the
    sources the four rules name and leaving the root index unnamed, would
    leave the provenance oracle unable to name the one source every
    observation admits. Round 2 found the first wording ("the pillar-root and
    pillar-index rules") undecidable for exactly that source: its labels
    matched neither the spec nor the code.
- **Values of the flag.** Rules 1 and 2 need the root index. Rules 3 and 4
  do not, because these definitions write their path patterns rather than
  the root index naming them.
- **The flag belongs to the rule.** A loaded profile sets it for each tree
  population it declares.
- **What "read" means.** The root index is read when its body is read:
  present at the revision, admitted, and read within its resource limits. A
  body that is read but whose grammar fails is still read.
  - A pillar root it does not name unambiguously leaves that pillar's index
    and named files unadmitted (today's code records that pillar as Unknown,
    `not-named-in-root-index` or `named-root-ambiguous`).
  - A failing PWB-REQ-004 root grammar is that requirement's failure.
  - Neither qualifies a rule 3 or rule 4 count, because the root index was
    read.
  - [Inferred] This matches the code's three root-index states, `read`,
    `unavailable` and `missing-at-revision` (`RootIndexState`, same file
    line 126). The other reading, that a grammar failure also counts as
    unread, would qualify baseline-spec and roster counts whenever any root
    grammar fails, though those counts never use that grammar. The packet
    puts the choice to the owner as question 7.
- **Unread root index, rule that needs it:** it mints no item. Where the rule
  is a tree population, each source its path pattern matches stays counted
  with an Unknown item denominator and the reason that the root index was
  not read. Rule 1 then admits only the root index itself, and rule 2 admits
  no source. For Butlers' built-in grammar, then, only "mints no item" has
  effect.
- **Unread root index, rule that does not need it:** it still admits its
  sources, and every class and category count, and every source-path
  population total, that includes one of them says it was derived without a
  read root index.
- **Rule provenance is checked.** [Observed at `8f1fbec7`]
  `ManifestSource` in `project-shape-manifest.ts` already carries the rule
  that admitted a source, from the five names above. The oracle compares it
  with an independent derivation of the source-path population, and a
  scenario asserts it, naming the root index's own rule.
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
  - Every source carries the name of the rule that admitted it, from this
    closed set: the first rule admits the root index itself as `root-index`,
    and the index file of each pillar root it names as `pillar-index`; the
    second rule admits each file a pillar's index names as
    `pillar-named-file`; the third admits each baseline spec as
    `baseline-spec-tree`; and the fourth admits each roster `butler.toml`, and
    its `MANIFESTO.md`, as `roster-tree`. A source that a loaded profile's tree
    population admits carries that population's `pathPattern` as its rule
    name.
  - A source that more than one rule admits carries one rule name, decided
    in this order: the root index is `root-index`, whatever else admits it;
    a pillar's index file is `pillar-index`, even when another pillar's
    index names it; a baseline spec, a roster `butler.toml`, or a source a
    loaded profile's tree population admits, is admitted by that tree
    population alone and carries its name, even when a pillar's index names
    it; and any other file a pillar's index names, a roster `MANIFESTO.md`
    included, is `pillar-named-file`. A source that two tree populations of
    one loaded profile admit carries the name of the first the profile
    declares.
  - Each rule declares whether it needs the root index read. The flag belongs
    to the rule; a loaded profile sets it for each tree population it
    declares. The first and second rules need the root index; the third and
    fourth, whose path patterns these definitions write, do not.
  - The root index is read when its body is read: present at the revision,
    admitted and read within its resource limits. A root index whose body is
    read but whose grammar fails is still read: a pillar root it does not name
    unambiguously leaves that pillar's index and named files unadmitted, a
    PWB-REQ-004 root grammar that fails is that requirement's failure, and
    neither qualifies a count of the third or fourth rule.
  - When the root index was not read, a rule that needs it mints no item.
    Where that rule is a tree population, each source its path pattern
    matches stays counted in the source-path population with an Unknown item
    denominator, giving the reason that the root index was not read. The
    first rule then admits only the root index itself, and the second admits
    no source.
  - When the root index was not read, a rule that does not need it still
    admits its sources, and every class and category item denominator, and
    every source-path population total, that counts one of them states that
    it was derived without a read root index.
```

### Hunk 2 — Reader definitions — shared heading rules

Current:

```text
(nothing; this hunk only adds)
```

Proposed:

```text
  - Wherever the shared rules above, or a shape or key form below, fail the
    source, the failure fails the class whose row it reads, in that source, as
    the exactness rules below state.
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
    partially extracted, and states for each class either its items and
    denominator or its failure and reason.
  - A source's own item denominator is Unknown whenever any class it is
    assigned has an Unknown item denominator in it, for any reason: a failed
    class, or a class with an unenumerated heading. A source whose every
    class reads but one carries an unenumerated heading is extracted, not
    partially extracted, and its own item denominator is still Unknown.
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
withholding the items of any other class the source reads; a source with a
class whose item denominator is Unknown SHALL leave its own item denominator
Unknown; an unenumerated heading SHALL be surfaced, never skipped; and a
count derived without a read root index SHALL say so wherever it is shown.
```

### Hunk 8 — PWB-REQ-002 — Case and Observable

Current:

```text
  loaded profile.
[… signed lines between are unchanged …]
  the machine answer and reachable from Polaris.
```

Proposed:

```text
  loaded profile; also a source assigned three classes in which one class
  fails and two read, a section enclosing the V1 catalog headings that holds
  a tenth level-3 heading, an observation whose root index was not read
  while baseline specs and roster directories exist in the tree, and a
  pillar index that names a baseline spec, a roster `butler.toml` and that
  roster directory's `MANIFESTO.md`.
[… signed lines between are unchanged …]
  the machine answer and reachable from Polaris, together with each partially
  extracted source's per-class outcome, each unenumerated heading with its
  anchor and route, and each root-index qualification.
```

### Hunk 9 — PWB-REQ-002 — Oracle and Falsifier

Current:

```text
  denominator.
[… signed lines between are unchanged …]
- **Falsifier**: the independent extractors disagree, a malformed source emits
  a partial population, a known source disappears, an admitted item appears twice or
```

Proposed:

```text
  denominator. The comparison is made per source and class: both extractors
  must name the same failed classes with the same reasons, and the same
  identities and D for every class that reads, so a failed class's D is
  Unknown while each sibling's D is known, and each source with a class whose
  D is Unknown has its own D Unknown; an independent scan of each enclosing
  section finds every unenumerated heading, the count per source and class
  equals the count the answer gives, and each one is surfaced; every source
  names the rule that an independent derivation of the source-path
  population admits it under, by the stated order for a source more than
  one rule admits; and with the root index unread, every source a
  rule that does not need it admitted carries the qualification, while no
  source of a rule that needs it mints an item.
[… signed lines between are unchanged …]
- **Falsifier**: the independent extractors disagree, a failed class emits a
  partial population, a failed class withholds the items of a sibling class
  that reads, a class or category item denominator that counts a failed class
  or an unenumerated heading is presented as known, a source with a class
  whose item denominator is Unknown presents its own item denominator as
  known, an unenumerated heading is skipped or mints an item or is
  miscounted, a source names no rule or a rule other than the one that
  admitted it, a source that more than one rule admits names a rule other
  than the one the stated order gives it, a count derived without a read
  root index is shown without that qualification, a rule that needs the
  root index mints an item when it was not read, a known source disappears,
  an admitted item appears twice or
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
- **AND** the source's own item denominator renders Unknown, and the source
  is shown as partially extracted with each class's outcome

#### Scenario: An unenumerated heading is surfaced, not skipped

- **WHEN** a section that holds the V1 catalog headings also holds a level-3
  heading outside the nine
- **THEN** that heading is surfaced with its text and exact source anchor,
  routes to its source and mints no item
- **AND** the items under the nine headings stay modeled while the
  catalog-entry and Heart and Soul item denominators, and the V1 index's own
  item denominator, render Unknown with the reason unenumerated-heading

#### Scenario: Counts derived without a read root index say so

- **WHEN** the root index was not read and the tree holds baseline specs and
  roster directories
- **THEN** the baseline-spec and roster sources are admitted, and every class
  and category count, and the source-path population total, that includes
  them states that it was derived without a read root index
- **AND** no source of a rule that needs the root index mints an item, nor
  does any source of a loaded profile's tree population that does not
  declare `rootIndexRequired`
- **AND** every admitted source names the rule that admitted it, the root
  index itself as `root-index`

#### Scenario: A source two rules admit carries one rule name

- **WHEN** a pillar's index names a baseline spec, a roster `butler.toml`
  and that roster directory's `MANIFESTO.md`
- **THEN** the baseline spec is named `baseline-spec-tree` and the
  `butler.toml` `roster-tree`, each with its tree population's class
- **AND** the `MANIFESTO.md` is named `pillar-named-file`
- **AND** the root index is named `root-index` and each pillar's index file
  `pillar-index`, whichever index also names them
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
  warrants and every other verification limb stay byte for byte. "A
  malformed source emits a partial population" is the one falsifier limb
  replaced, by the per-class limbs. One kept scenario, "Loaded profile names
  a shape outside the vocabulary", keeps its bytes but not its old reach:
  see "Signed text whose meaning changes without a byte changing" in part 1.
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
*unenumerated heading*, with the reason `unenumerated-heading`; the profile
field `rootIndexRequired`; the five rule names `root-index`, `pillar-index`,
`pillar-named-file`, `baseline-spec-tree` and `roster-tree`; and what it
means for the root index to be *read*. None is retired.

## Downstream impact

See `IMPACT-LEDGER.md` for the sweep, its predicate and its denominator. In
short:

- **Companions** in the same change (CC-REV-2): a proposal bullet, design
  decision 12 and a design note on the discovery rules, capability row 34,
  and the regenerated dependency file.
- **Implementation:** the extraction, coverage and manifest modules and
  their tests. Sign-off authorizes none of it.
- **The pending siblings** (as of 2026-10-14 at `814fbcc1`; until that day
  this bullet named the release-label amendment alone, which round 3 found
  short of the builder's list): three unsigned packages patch the same PWB
  spec, and the builder's `PENDING_SIBLINGS` lists all three.
  - The release-label amendment (P-85) also adds a design decision 12 and a
    capability row 34. Whichever is signed second is regenerated over the
    first's applied bytes and re-reviewed.
  - The opening-index amendment (P-98, PWB-REQ-010) and the accessible-name
    amendment (P-99, PWB-REQ-016) each touch one other requirement and the
    generated dependency file: they compose, all orders checked.
  - The anchor-resolution amendment (P-96, PWB-REQ-014), pending when round
    3 read this package, was signed v1.0 on 2026-10-14; the builder now
    lists it as performed, and these patches are regenerated over its
    applied bytes.
  - [Observed at `814fbcc1`] The builder's all-orders check applies this
    spec patch and the three pending siblings' in every order and gets one
    result.
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
     at 9 (it is 51 and 6 today). *Marked 2026-10-14: those figures were
     right at `ef5d5f03`; [Observed at `814fbcc1`] the builder's `--check`
     now reads 17 requirements and 56 proposed scenarios, with PWB-REQ-002
     at 10, against 52 and 6 signed — the anchor-resolution sign-off added
     one scenario, and the cycle-2 repairs a fourth new one here.* The
     signing change updates the literal census and `census.json`, and
     appends this sign-off to the PWB child's successor tuple.
  3. Add the builder's `--check` to the `PROJECT-STATUS.md` battery under
     the CG-26 coupled-triple rule. A draft leaves the battery alone.
  4. The observer registry entry and the secret-classification policy pin a
     PWB spec digest; both are already stale and Unknown until their own
     act (`syzygy-jloi`). *Marked 2026-10-14 (round-3 finding 3):
     `syzygy-jloi` was performed on 2026-10-02 and is closed. [Observed at
     `814fbcc1`] `check_spec_reconciliation.py --check` R6 attributes both
     stale pins to `syzygy-2g0d`, the tree-framing re-pin package routed to
     the owner as P-95, whose acts are unperformed.* Signing this moves the
     digest again.
- **Open owner question, not a signing-change task.** Half of the Q3
  ruling, unenumerated root-summary and precedence headings, is not designed
  here. Packet question 6 asks whether a separate PWB-REQ-004 delta carries
  it or this package widens. (Until 2026-10-14 this was listed as residual 5
  above; round 2 found that it is neither an observation nor a task the
  signing change performs.)
- **Implementation** needs its own authorization, after sign-off.

## Review

**Required class:** full review (Normative, CC-REV-1), one fresh-context
round, raw retained verbatim.
**Reviewer:** a fresh-context agent that did not draft this package.
**Verdict:** round 1 `REVISE`, copied from
`docs/reviews/R-PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-1-RAW.md` line 4 and
dispositioned in `ROUND-1-DISPOSITIONS.md` beside this file. Findings 1–9
were repaired; finding 10 changed nothing. Round 2 (bead `syzygy-418x`),
over the repaired bytes at `1701c88f`, returned `REVISE`, copied from
`docs/reviews/R-PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-2-RAW.md` line 4:
one revise finding and seven notes, dispositioned in
`ROUND-2-DISPOSITIONS.md`. On 2026-10-14 the owner directed one new version
repairing all eight, then one fresh round. All eight were repaired once
that day; the repaired bytes are **unconfirmed** pending round 3, and are
not offered for sign-off until a round over them returns `CONFIRM`, or
`CONFIRM WITH EXCEPTIONS` with notes only. *(Marked 2026-10-14: round 3 has
run.)* Round 3, over `00e24fd2`, returned `REVISE`, copied from
`docs/reviews/R-PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-3-RAW.md` line 4:
one revise finding and four notes, dispositioned in
`ROUND-3-DISPOSITIONS.md`. On 2026-10-14 the owner directed one more
cycle. **Round-3 findings repaired once on 2026-10-14, unconfirmed pending
round 4**; the bytes are not offered for sign-off until a round over them
returns `CONFIRM`, or `CONFIRM WITH EXCEPTIONS` with notes only.
