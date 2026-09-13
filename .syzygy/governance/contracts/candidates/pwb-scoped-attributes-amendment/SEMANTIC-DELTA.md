# Semantic delta — PWB scoped epistemic attributes (PWB-REQ-007/020, RFC7-33)

> **Candidate — binds nothing.** Agents drafted these bytes under the owner's
> 2026-09-13 P-67 ruling (question 2: draft lane B after lane A is measured).
> Only the human owner may supersede the signed PWB behavior or amend the
> RFC-0007 module (`contracts/rfcs/RFC-0007/rendering-and-surface.md`, in
> force), each by its own act. Silence, a commit, a
> review, a merged pull request or a manifest performs no act. Nothing here
> authorizes an implementation.

**Artifact(s):**

- `openspec/changes/polaris-project-wide-butlers-model/` (the
  eleven-artifact signed PWB behavioral package). Three of the eleven
  change: `specs/polaris-project-wide-butlers-model/spec.md`, `design.md`
  and the regenerated `GOVERNING-DEPENDENCIES.md` (its source-digest line
  only). The other eight rows of `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`
  equal current bytes.
- `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`
  (accepted contract module) and its byte-identical candidate mirror
  `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`.
  One clause changes, RFC7-33, by the insert-only patch
  `proposed/contract/RFC-0007-rendering-and-surface.md.patch`. The
  contract module is **not** a row of the behavior manifest: it binds only
  by a contract successor act of its own (see "Migration").

**Stable IDs affected:** `PWB-REQ-007`, `PWB-REQ-020`, `RFC7-33`. No
requirement or clause is minted, retired or renumbered. No warrant list
changes. `PWB-REQ-014` was in the first draft and is **not** amended: its
`non-citable` / `presentation-artifact` attributes stay on every unit,
because RFC7-33's sub-clause "Non-citability travels, on every rendering"
names them as the one field a consumer holding a detached unit cannot
recover (review 1, F1).

**Change class:** Normative (behavioral and contract). The amended spec
clauses admit a human rendering the current clauses forbid and add one
falsifier class; the contract clause gains one permission paragraph for
the interactive surface. Nothing is newly forbidden; no falsifier is
weakened.

**Author:** the pursuit session for bead `syzygy-dov.17` (agents), drafting
only.

**Date:** 2026-09-14 (second draft; the first draft's review is
dispositioned under "Review").

**Baseline:** commit `a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d` (main).
The proposed bytes are the patches under `proposed/` applied to that
baseline; `scripts/build_pwb_scoped_attributes_amendment.py --diff` prints
them and `--check` verifies that the three behavior patches still apply,
that the manifest hashes their result, that the contract patch applies to
both RFC-0007 mirrors and that the mirrors are identical. The bytes are
deliberately **not** applied in place while this is a candidate: CG-7h
binds the current package bytes to the performed 2026-09-05 act, and a
drafted edit in place reads as drift (verified 2026-09-14 in a scratch
worktree: with the spec, design and contract patches applied in place,
`check_governance.py` fails CG-7a, CG-7h and CG-18 with 1, 9 and 2
findings; the signed contract-coverage matrix's `--check` still passes,
because its line references are frozen text).

## Why

Polaris renders the whole declared Butlers project behind one 2 MiB
response ceiling. The 2026-09-13 lane A trim (bead `syzygy-dov.1`, evidence
`docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`, review
`docs/reviews/R-PWB-M1-POLARIS-LANE-A-RAW.md`, verdict CONFIRMED WITH
FINDINGS) left the page at these sizes [Observed, that record]:

| form | before lane A | after lane A | over the ruled 1,400,000 target |
|---|---|---|---|
| direct | 2,132,656 | 1,478,637 | 78,637 |
| tailnet mount | 2,138,506 | 1,484,487 | 84,487 |

A statement-less item still costs about 1,486 bytes (mean over the 324
compact-list entries in that record; the ruled target is under 1,000), and
that cost is the claim tuple plus its support citations. Under the current
PWB-REQ-007 every claim's element carries the complete tuple and its
evaluation identity even when every claim in one table carries the same
values, and the accepted contract clause RFC7-33 requires every
distinction "as a machine-readable attribute on the rendered unit". Lane B
lets shared tuple values be stated once per enclosing scope, in the
specification and in the contract. The funnel packet's estimate
(`docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`, lane B) was roughly 450 KB
on the pre-lane-A capture, of which about 100 KB was the two non-authority
attributes; with PWB-REQ-014 unchanged the estimate is about 350 KB
[Inferred; not yet measured on the lane A page].

## Current meaning (quoted, current bytes at the baseline)

PWB-REQ-007, the observable, oracle, independence and falsifier bullets:

```
- **Observable**: human and machine views expose identical complete tuples;
  invalid/missing currency stays Unknown and aggregates expand to members.
- **Oracle**: compare each tuple and tier meaning to independent literal
  vocabularies and provenance-verified currency inputs; verify stable semantic
  identity across the two evaluation instances; exhaust challenge/sibling
  separation, aggregate label/tier/freshness/reason counts and supports links;
  zero invalid, missing or folded values decides.
- **Oracle independence**: the checker hard-codes the accepted vocabularies and
  reads captured authority/evidence, importing no production vocabulary.
- **Falsifier**: a positive claim lacks current support, a tuple field is
  absent/out of vocabulary, a reason has no route, Unknown is folded into a
  total, or an aggregate claims its own headline status.
```

PWB-REQ-020, the prose's last words and every bullet:

```
evaluation in the machine answer, preserving multiplicity and exact provenance
state.

- **Case (sweep)**: enumerate every project-shape parity marker on Polaris and
  every corresponding machine-answer fact at one evaluation, including every
  PWB-REQ-005 authority state and PWB-REQ-022 judgment state and disclosure.
- **Observable**: both populations contain equivalent multisets.
- **Oracle**: an independent order-insensitive, multiplicity-preserving
  comparator reports both denominators and zero differences.
- **Oracle independence**: the comparator extracts each channel separately and
  imports no production vocabulary or rendering code.
- **Mutation proof**: for each fact, authority-state, judgment-state and
  disclosure marker class, independently inject a missing, duplicated,
  changed, collapsed and wrong-evaluation marker and confirm the comparator
  fails before restoration; report both channel denominators for every run.
- **Falsifier**: one fact, authority state, judgment state or disclosure is
  missing, duplicated, changed, collapsed or associated with a different
  evaluation in either channel.
```

RFC7-33, the opening paragraph (the sub-clause that follows it,
"Non-citability travels, on every rendering.", is unchanged and is not
quoted):

```
**RFC7-33 — Every distinction, machine-readable.** Every distinction this
package draws — **`non-citable` / `presentation-artifact`** (below),
claim-block kind (anchored / non-normative / labeled), the narrative
claim-block **type name** (below), band membership and its authority class,
curated-versus-computed provenance, adopted versus unadopted, editorial-draft
state, proposal-context membership, review state, RFC7-11(a)'s
**target-changed** state, label + tier + reason + freshness — is carried as a
**machine-readable attribute on the rendered unit**, served identically
through the machine-queryable endpoints (RFC6-13/14) and preserved in
plain-text or exported renderings [Observed: agents are a first-class consumer
from day one (vision.md); endpoints are V0-mandatory (v1.md)]. A distinction
available only to pixels does not survive an endpoint response, a copy-paste
into an agent prompt, or a reader who cannot see it.
```

## Proposed meaning (quoted, the bytes the patches produce)

PWB-REQ-007 gains one paragraph after its prose, the four bullets change,
and one scenario is added (`proposed/spec.md.patch`):

```
In the human view, a tuple field whose value is the same for every claim
under one enclosing scope MAY be carried once on that scope instead of on
each claim. The inheritance rule is: a claim's value for a field it does not
carry itself is the value of the nearest enclosing scope that carries the
field; a claim under no such scope leaves the field absent, which the
falsifier below forbids. A scope SHALL be one element carrying a
machine-readable scope marker, SHALL carry a field only when every claim
under it has that value in the machine answer, and contributes no tuple of
its own after expansion. Where claims under one element differ in a field,
that element carries nothing for the field and each claim carries it itself;
this holds for evaluation identity as for every other field, and nothing
fails to render. Claim identity is never carried by a scope. The machine
answer SHALL carry every field on every claim and SHALL not inherit.
```

```
- **Observable**: human and machine views expose identical complete tuples
  once the human view is expanded under the inheritance rule; invalid/missing
  currency stays Unknown and aggregates expand to members.
- **Oracle**: expand every scope with the checker's own statement of the
  inheritance rule, then compare each tuple and tier meaning to independent
  literal vocabularies and provenance-verified currency inputs; verify stable
  semantic identity across the two evaluation instances; exhaust
  challenge/sibling separation, aggregate label/tier/freshness/reason counts
  and supports links; zero invalid, missing, folded or scope-hidden values
  decides.
- **Oracle independence**: the checker hard-codes the accepted vocabularies and
  the inheritance rule and reads captured authority/evidence and the machine
  answer, importing no production vocabulary or rendering code.
- **Falsifier**: a positive claim lacks current support, a tuple field is
  absent/out of vocabulary after expansion, a claim's expanded value for any
  field differs from the value the machine answer carries for that claim (a
  scope value hiding a differing member), a reason has no route, Unknown is
  folded into a total, or an aggregate claims its own headline status.
```

```
#### Scenario: A field shared by every claim under one scope is carried once

- **WHEN** every claim under one scope has the same value for a tuple field
  in the machine answer
- **THEN** the scope may carry that field once and each claim's expanded
  tuple equals its machine tuple
- **AND** where claims under one element differ, each carries the field
  itself, and a scope value that would hide the difference fails the oracle
```

PWB-REQ-020:

```
evaluation in the machine answer, preserving multiplicity and exact provenance
state. Recoverability is judged after the human view is expanded under the
PWB-REQ-007 inheritance rule; a scope value SHALL never stand in for a claim
whose own value differs, and a scope element contributes no marker of its
own after expansion.

- **Case (sweep)**: enumerate every project-shape parity marker on Polaris,
  expanding scopes, and every corresponding machine-answer fact at one
  evaluation, including every PWB-REQ-005 authority state and PWB-REQ-022
  judgment state and disclosure.
- **Observable**: both populations contain equivalent multisets.
- **Oracle**: an independent order-insensitive, multiplicity-preserving
  comparator expands scopes with its own statement of the inheritance rule
  and reports both denominators and zero differences.
- **Oracle independence**: the comparator extracts each channel separately and
  imports no production vocabulary or rendering code; its expansion of the
  inheritance rule is its own.
- **Mutation proof**: for each fact, authority-state, judgment-state and
  disclosure marker class, independently inject a missing, duplicated,
  changed, collapsed, wrong-evaluation and scope-hidden marker (a scope value
  that hides one member's differing value) and confirm the comparator fails
  before restoration; report both channel denominators for every run.
- **Falsifier**: one fact, authority state, judgment state or disclosure is
  missing, duplicated, changed, collapsed, hidden behind a scope value or
  associated with a different evaluation in either channel.
```

RFC7-33 gains one paragraph between its opening paragraph and the
non-citability sub-clause (`proposed/contract/RFC-0007-rendering-and-surface.md.patch`,
insert-only, applied identically to the installed module and the candidate
mirror):

```
**Scope-carried values on the interactive surface.** On the interactive
human surface only, a distinction other than `non-citable` /
`presentation-artifact` whose value is the same for every unit under one
enclosing element MAY be carried once on that element, marked
machine-readably as a scope, in place of on each unit; a unit under a scope
then carries the value by expansion, under an inheritance rule the governing
specification states once and every oracle restates independently. A scope
never carries a value that any unit under it lacks, never carries a unit's
identity, and is expanded before any parity comparison. The machine-queryable
endpoints and every plain-text or exported rendering carry every distinction
on the unit itself, unchanged by this paragraph. A unit copied out of the
interactive surface without its scope has lost what the scope carried, which
is why non-citability is excluded from this permission: the sub-clause below
stands in full.
```

`design.md` gains decision 9, "Carry a shared claim field once per scope",
before "Data Flow" (`proposed/design.md.patch`); it restates the rule,
names the `scope-hidden` falsifier beside the unchanged `collapsed` and
`duplicated` ones, says why PWB-REQ-014's attributes stay per unit, dates
its measured figures to the lane A evidence record, and lists the rejected
alternatives. It binds nothing the spec does not.

## What explicitly does NOT change

- The machine answer. Every claim in the machine form carries every tuple
  field, its evaluation identity and both non-authority attributes exactly as
  today; the machine form never inherits. RFC7-33's endpoint and export
  sentence is restated, not relaxed, by the new paragraph.
- The tuple vocabulary: label, tier, exactly one primary reason, zero or more
  closed secondary reasons, freshness, challenge state, evaluation identity,
  RFC2-24 Unknown reasons verbatim with routes. No field is dropped for any
  claim in any channel; "absent after expansion" is a falsifier.
- One tuple per claim in the parity multiset. Expansion restores one complete
  tuple per rendered claim before comparison, a scope element contributes no
  tuple or marker of its own, so the comparator still reports both
  denominators and PWB-REQ-020's `collapsed` and `duplicated` falsifiers
  keep their meaning. Claim identity is never inherited.
- Unknown never folds. A scope carries a field only when every claim under
  it has that value in the machine answer, so a scope can carry a positive
  label only over claims that are all positive; an Unknown claim under any
  element carries its own label, and the `scope-hidden` falsifier fires if a
  scope value hides it.
- Evaluation identity per claim (RFC7-16). It is a tuple field like every
  other: carried once by a scope only when every claim under it has the same
  identity in the machine answer, and carried by each claim itself where
  claims differ. Nothing fails to render on that account.
- PWB-REQ-014 in full: the claim role and the `presentation-artifact` /
  `non-citable` attributes stay on every owner-visible narrative unit in
  every channel. The contract paragraph excludes them by name.
- RFC7-33's sub-clause "Non-citability travels, on every rendering" and every
  other clause of RFC-0007; RFC7-33's opening paragraph is not edited, only
  followed by the new one.
- Anchor sets, anchor identity classes, the non-authority of Polaris, and
  PWB-REQ-011/015/016/021/022.
- Oracle independence. Each checker expands scopes with its own statement of
  the rule and still imports no production vocabulary or rendering code.
- Aggregates (the existing "aggregates expand to members") are unrelated to
  scopes: an aggregate is a claim about a population; a scope is a carrier of
  shared field values for the claims under it.

## Warrant

VIS-1 (the honest whole is what the reader gets; the page must render inside
the ceiling rather than answer a 503 with nothing), VIS-2 (no field is
dropped, folded or made Unknown by the change), RFC6-22 and RFC6-23
(equivalent channels, no disagreement on label, tier, reason, freshness),
RFC7-16 (evaluation identity on every claim, restored by expansion),
CC-TEST-5 and CC-TEST-6 (the falsifier set grows by one class and the
mutation proof names it). RFC7-33 is the clause the spec change
invalidates, so CC-REV-2 ("invalidated accepted contracts must be updated
in the same logical change") is why the contract patch travels in this
package rather than being left to a later cleanup; its binding still needs
its own act, because a contract change is an act escalation trigger.
Decision basis:
`.syzygy/governance/decisions/POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`
(P-67, 2026-09-13, question 2) and the P-63 ceiling posture it builds on.

## Evidence or decision basis

- `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json` — the
  sizes and per-item cost above [Observed].
- `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` §"Lane B" and §"Draft
  semantic delta" — the sketch this delta finalizes and the saving estimate
  [Inferred]; the funnel's superseded note says which parts this package
  dropped.
- `docs/reviews/R-PWB-M1-POLARIS-LANE-A-RAW.md` — the lane A review, whose
  findings were dispositioned in the evidence record.
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-RAW.md` — the first review of
  this package (verdict REVISE), whose findings shaped this draft.
- The in-place trial recorded under "Baseline" above [Observed, scratch
  worktree, 2026-09-14; not retained as a file].

## Terms introduced or retired

Introduced: **scope** (one element carrying a machine-readable scope marker,
under which claims may inherit tuple field values) and the **inheritance
rule** (stated once, in PWB-REQ-007; restated by RFC7-33 as the rule "the
governing specification states once"). **scope-hidden** names the new
falsifier and mutant class. Nothing retired.

## Downstream impact

`IMPACT-LEDGER.md` in this directory. For the three PWB identifiers: 80
tracked files cite at least one, over a denominator of 1,216 tracked files
at the baseline, by two methods that agree (Python regular expression over
every tracked file; `git grep -F` per identifier, union); at the commit
that carries this draft the same sweep returns a larger figure, stated in
the ledger with the additions enumerated (they are this package's own
files and the retained raw review). For `RFC7-33` the ledger carries a
second sweep with its own denominator. Every file is classified there; the
ones the implementation must touch are the renderer, the claim-states copy,
the two oracles that read tuples, and the mutation sweep. No Capability 1
file changes: the contract paragraph is a permission, and Capability 1's
surfaces do not take it.

## Migration and supersession plan

Two acts, in this order; neither is offered yet.

1. This package is reviewed in fresh context (`REVIEW-BRIEF.md`); every raw
   is retained under `docs/reviews/` and dispositioned below.
2. The owner rules the direction question in `OWNER-DECISION-PACKET.md`
   (P-68: proceed on the two-act path, revise the target and close lane B,
   or decline).
3. **Contract successor (RFC-0007).** No RFC-0007 amendment has ever been
   performed, and the existing successor seam in `check_governance.py` is
   hard-coded to RFC-0008/0009 (`docs/POLARIS-NO-SIGNAL-AMENDMENT-TOOLING.md`
   records that ceremony). On a "proceed", that ceremony is generalized or
   copied for RFC-0007: a recorder whose subject is the module bytes after
   the contract patch, identical in `contracts/rfcs/` and the candidate
   mirror; a history entry in `contracts/candidates/history/RFC-0007-history.md`;
   a successor manifest; the seam extended; a packet with one phrase. Only
   that act changes RFC7-33.
4. **Behavior amendment (PWB).** On the exact phrase for the behavior
   manifest, a dedicated recorder (the 2026-09-05 shape) applies the three
   behavior patches with the builder's `--apply --at-adoption`, verifies
   that every manifest row now hashes the tree, writes the dedicated act
   record `PWB-SCOPED-ATTRIBUTES-AMENDMENT-ACT.md` and the aggregate
   section, and registers the act as the third link of the PWB successor
   chain, all in one change, so CG-7h never sees a drifted tree.
   `check_governance.py` already carries an existence-gated activation for
   that record's digest copy, a no-op until the file exists.
5. Only after both acts does an implementation bead exist. It carries the
   renderer change, the claim-states lede, the comparators' own expansion,
   the `scope-hidden` mutant class and a measurement in the lane A shape;
   `tasks.md` (unbound) takes its rows then.
6. Rollback is a later successor act on each side; the 2026-09-05 package
   and the accepted RFC-0007 stay the authorities until then and their
   records are never edited. A performed contract act with a declined
   behavior act leaves the RFC7-33 permission unused: the spec still
   forbids scoping and nothing renders differently.

## Review

Class: fresh-context semantic review of a normative delta (CC-REV-4,
CC-REV-6); reviewer given only the reviewed commit, `REVIEW-BRIEF.md` and
the governing references, read-only.

### Review 1

- Raw: `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-RAW.md` (retained
  verbatim). Reviewed commit `9098b0b11ab548b4ea00081b26ec4ad2b84e693e`;
  the manifest that commit carried is superseded by this draft's.
- Verdict, copied exactly: **REVISE**.
- Findings and dispositions (F1–F5 blocking, F6–F15 non-blocking, F16–F20
  editorial in the raw's own grouping):
  - F1, PWB-REQ-014 scoping contradicts accepted RFC7-33 and no contract
    amendment travelled: **accepted**. PWB-REQ-014 is no longer patched;
    the package carries the RFC7-33 contract patch and a two-act path.
  - F2, the scope-hidden falsifier was vacuous flat and over-fired nested:
    **accepted**. The falsifier now compares each claim's expanded value
    with the machine answer's value for that claim, in every nesting.
  - F3, hoisting precondition and override sentence inconsistent:
    **accepted**. One strict rule: a scope carries a field only when every
    claim under it has that value in the machine answer; where claims
    differ the element carries nothing and each claim carries it itself.
  - F4, "SHALL fail to render" on two evaluation identities was an
    undisclosed new prohibition: **accepted**. Removed; evaluation identity
    follows the same rule as every field and nothing fails to render.
  - F5, design.md attributed scope-hiding to the `collapsed` falsifier:
    **accepted**. Decision 9 names `scope-hidden` beside unchanged
    `collapsed` and `duplicated`.
  - F6, packet routes to a register row that did not exist: **accepted**.
    P-68 is a row of `PENDING-OWNER-DECISIONS.md` at this draft's commit.
  - F7, no existence-gated activation for the act record: **accepted**.
    `_activate_pwb_scoped_amendment_act_copy_registry()` added beside the
    truth-amendment precedent.
  - F8, builder not in CI: **accepted**. `--check` and `--selftest` steps
    added to the hosted workflow and the published battery (CG-26 holds).
  - F9, PWB-REQ-014 oracle-independence bullet unamended: **moot**, 014 is
    not patched.
  - F10, rule written for claims and applied to narrative units: **moot**
    for the spec (014 not patched); the contract paragraph speaks of
    units, which is RFC7-33's own noun, and defers the rule's statement to
    the governing specification.
  - F11, the scope element's own contribution to the multiset was
    unspecified: **accepted**. Both amended clauses say a scope contributes
    no tuple or marker after expansion.
  - F12, ledger column inconsistencies: **accepted**. `polaris-copy.ts` is
    marked must; the legend defines every value; the "every other row"
    sentence is replaced.
  - F13, the 80/1,216 figure did not hold at the reviewed commit:
    **accepted**. The ledger states the figure at the baseline and at this
    draft's commit, with the additions enumerated.
  - F14, decision 9 embedded a perishable measured claim: **accepted**. The
    figures are dated to the evidence record and stated as measured on
    that day.
  - F15, the manifest header goes false at the act: **accepted**. The
    header now says the rows bind only by the act that names the digest.
  - F16, "leaves the field absent" read as a grant: **accepted**, the
    resolution wording taken.
  - F17, the 014 falsifier broadening was an unstated change: **moot**,
    014 is not patched; the change class now enumerates every change.
  - F18, two populations in one ledger cell: **accepted**, split.
  - F19, the owner's option to revise the target was not on the page:
    **accepted**; it is option (b) of the direction decision.
  - F20, a bare builder run overwrote the manifest: **accepted**; `--write`
    is required and a bare run refuses.
- Lesson recorded: an RFC-0007 successor needs tooling that does not exist;
  a spec change that invalidates an accepted clause has to carry the
  contract delta from the first draft (CC-REV-2).

### Review 2

Pending. Appended when the second raw lands under `docs/reviews/` with the
same basename stem as the first and the suffix `-2-RAW.md`.
