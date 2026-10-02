> # Record beside the package — not authority, binds nothing
>
> Dispositions the findings of the first fresh-context review of the PWB
> tree-framing package. It is not a package artifact: the manifest does not
> hash it and no builder reads it. It offers nothing and performs no act
> (VIS-4).

# Round 1 dispositions — tree-framing package

- **Reviewed commit:** `509201592c13ba903bd3bfc5f91fb2e8aedf2742`.
- **Verdict (raw line 5):** `REVISE`; eleven findings: five revise (1-5) and
  six notes (6-11), counted from the raw's finding headings.
- **Effect:** the package bytes the review read are retired by the repair
  below (rule 10). A fresh review of the repaired bytes is required before any
  sign-off is offered.

Reviewed record: docs/reviews/R-PWB-TREE-FRAMING-AMENDMENT-1-RAW.md

[Observed] Re-derived after the repair from the files themselves: the
builder's `--check` passes (11 subjects, 5 patched; 8 performed by record, 1
declined, none unclassified) and its `--selftest` reports 117 predicates
failing closed, up from 81 at the reviewed commit. The manifest was
regenerated with `--write`; no other tracked file carried a copy of the
reviewed manifest's digest, so no digest copy needed updating.

## Dispositions

### 1 — a partly supported relationship silently drops its unsupported edges (revise)

Repaired. The review record now lists the nodes and edges it expects for
each relationship. A drawn diagram accounts for its whole listed
relationship: every listed node or edge it does not draw is named in the text
equivalent as not drawn, with its reason, and the figure is marked partial.
A new scenario, *A partly supported relationship names what it leaves out*,
states the counterexample's result. The selftest mutates each new fragment.

### 2 — "drawable" uses two predicates, so the Unknown-only case is undetermined (revise)

Repaired. One predicate, `supported`: a model claim establishes the element
with an Observed or Inferred label. Drawable means at least one edge is
supported, so a relationship whose only claimed edges are Unknown is not
drawable; the scenario and both resolution diagrams now use the same words.
The disclosed reason is stated: an Unknown claim's own RFC2-24 reason and
resolution route, or the existing value `missing-declaration` and its route
where no claim establishes the element. No reason value is minted. Whether an
all-Unknown relationship should instead be drawn is a new open point (6).

### 3 — the opening above Butlers text carries three roles (revise)

Repaired. An opening's one copy role is `project-fact`, and its one claim
role is epistemically labeled claim. Its label marker and its routes are
separate `epistemic-disclosure` and `action-label` strings. Above Butlers
text the opening names only which declared text follows; a source identity
holding a word PWB-REQ-012 bars from a lede is named in the route string,
never in the opening.

### 4 — "top-level" can restrict the whole group list (revise)

Repaired. The text defines a group as one of four classes: a project-level
category of PWB-REQ-010's first reading level (a top-level group), a project
catalog of PWB-REQ-011, an item detail of PWB-REQ-015, or an evidence group,
defined as the group that renders the source records and Unknown disclosures
of one category, catalog or item. Every group opens. "Top-level" now names
only the first class, which is open point 3's other arm.

### 5 — "states only what its children state" is subset-soundness only (revise)

Repaired.
- An opening carries the weakest label among its children, with a withheld or
  excluded child counted as Unknown.
- An opening that states fewer than all its children names its scope.
- An Unknown opening mints no reason and routes to each Unknown child's own
  reason and route.
- The counterexample is now a scenario: *An opening over an Unknown child is
  never more favourable*.
- The machine narrative carries each opening's group, label and child
  identities, which stand in place of an anchor set. Claim role is answered
  under finding 3.
- The oracle no longer derives expected openings from the model. Groups,
  child sets, labels and elements come from the model and the named review
  record, and an independent claim-to-child mapping judges each opening's
  statements.

Naming Unknown counts was the other route; it is open point 5's other arm.

### 6 — placement of the item-detail opening relative to PWB-REQ-015's bands (note)

Fixed in package prose. An item detail's opening precedes its `argument`
band and belongs to no band, so neither band's limit governs it; the delta
and ledger say so under PWB-REQ-015.

### 7 — a counting opening cannot fit the disclosure it must carry (note)

Fixed in package prose. No opening counts claims, sources or rows, so
PWB-REQ-010's opening aggregate stays the only aggregate before the first
capability catalog and no count wall forms; counts stay on demand under
PWB-REQ-007. Allowing counted openings with full disclosure is open point 5's
other arm.

### 8 — the set of diagrams is whatever an unbound review record lists (note)

Fixed in package prose. The machine narrative names the review record a page
follows by path and SHA-256, and a relationship that record does not list
owes no diagram, which makes the rule total over the named record. Which
relationships a later review lists stays out of this package's scope.

### 9 — label text and the PWB-REQ-006 sink scan are not addressed (note)

Fixed in package prose. Label text is encoded as SVG text content at both
sinks, so a markup-like code span in a label stays inert text. The oracle
says PWB-REQ-006's sink scan admits an emitted SVG only when the independent
allow-list scan passes it, and the delta and ledger disclose this under
PWB-REQ-006, whose text stays unamended.

### 10 — the builder classifies a performed sibling by record existence alone (note)

Repaired in the builder. `PERFORMED_SIBLINGS` pins each sibling's spec-patch
SHA-256 as performed. `performed_record` returns true only when three things
hold:
- the patch still hashes to that digest;
- the record exists and names the package directory;
- the record carries its act's binding: the live SHA-256 of the sibling's
  manifest file for a digest-bound act, or the `Package:` and `Tag:` lines of
  a version-tagged sign-off.

The selftest holds eight cases over scratch copies of real siblings (two
history cases, six mutants that must classify). [Observed] The reviewer's two
mutants, and a third that edits a digest-bound sibling's manifest, each make
`--check` fail with an unclassified sibling. Five mutants of the predicate
itself each leave at least one selftest case `SURVIVED`.

The tag's presence in Git is not checked, since a checkout may lack tags.

### 11 — page-size evidence covers the human page only; the opening count is unsourced (note)

Dispositioned, partly fixed in prose. The ledger and packet now label the
machine JSON sink [Unknown]: not measured or projected here. The
implementation must measure it against its own ceiling, beside both human
forms, before merge.

The figure 32 is the drafting session's count of groups on the served page.
That enumeration was not retained, so the ledger now says the count is
Inferred and that the implementation re-derives it. Re-measuring needs a
private daemon, and the brief does not require it.
