# Semantic delta — PWB scoped epistemic attributes (PWB-REQ-007/014/020)

> **Candidate — binds nothing.** Agents drafted these bytes under the owner's
> 2026-09-13 P-67 ruling (question 2: draft lane B after lane A is measured).
> Only the human owner may supersede the signed PWB behavior, by the exact
> phrase in `OWNER-DECISION-PACKET.md`. Silence, a commit, a review, a merged
> pull request or a manifest performs no act. Nothing here authorizes an
> implementation.

**Artifact(s):** `openspec/changes/polaris-project-wide-butlers-model/`
(the eleven-artifact signed PWB behavioral package). Three of the eleven
change: `specs/polaris-project-wide-butlers-model/spec.md`, `design.md` and
the regenerated `GOVERNING-DEPENDENCIES.md` (its source-digest line only).
The other eight rows of `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` equal current
bytes.

**Stable IDs affected:** `PWB-REQ-007`, `PWB-REQ-014`, `PWB-REQ-020`. No
requirement is minted, retired or renumbered. No warrant list changes.

**Change class:** Normative (behavioral). The amended clauses admit a human
rendering the current clauses forbid, and add one falsifier class.

**Author:** the pursuit session for bead `syzygy-dov.17` (agents), drafting
only.

**Date:** 2026-09-14.

**Baseline:** commit `a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d` (main).
The proposed bytes are `proposed/*.patch` applied to that baseline;
`scripts/build_pwb_scoped_attributes_amendment.py --diff` prints them and
`--check` verifies they still apply and that the manifest hashes their
result. The bytes are deliberately **not** applied in place while this is a
candidate: CG-7h binds the current package bytes to the performed
2026-09-05 act, and a drafted edit in place reads as drift (verified
2026-09-14: appending one byte to the spec in a scratch worktree fails CG-7h
with six findings).

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
PWB-REQ-007 every claim's element carries the complete tuple, its evaluation
identity and, under PWB-REQ-014, both non-authority attributes, even when
every claim in one table carries the same values. Lane B lets those shared
values be stated once per enclosing scope. The funnel packet's estimate
(`docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`, lane B) is roughly 450 KB on
the pre-lane-A capture [Inferred; not yet measured on the lane A page].

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

PWB-REQ-014, the first sentence, the observable, the oracle's opening and
the falsifier:

```
Every owner-visible narrative unit SHALL carry `presentation-artifact` and
`non-citable` attributes and exactly one claim role: anchored project fact,
explicitly non-normative framing, or epistemically labeled claim.
```

```
- **Observable**: claim roles and non-authority attributes are machine-readable;
  every claim has exact/minimal anchors and no downstream authority reference
  targets Polaris.
- **Oracle**: independent claim-to-source mapping establishes covering,
```

```
- **Falsifier**: an unclassified narrative unit, uncovered claim, surplus or
  ambiguous anchor, missing non-citable attribute, or downstream citation to
  Polaris.
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

## Proposed meaning (quoted, the bytes `proposed/spec.md.patch` produces)

PWB-REQ-007 gains one paragraph after its prose, the four bullets change,
and one scenario is added:

```
In the human view, a tuple field whose value is identical for every claim
under one enclosing scope MAY be carried once on that scope instead of on
each claim; the claim still carries the field by the inheritance rule, and a
claim whose value differs from its scope's SHALL carry the field itself. The
inheritance rule is: a claim's value for a field it does not carry is the
value of the nearest enclosing scope that carries the field; a claim under no
such scope leaves the field absent. A scope SHALL be one element carrying a
machine-readable scope marker; every claim under it SHALL carry its Claim
identity itself. A page whose claims would carry two distinct evaluation
identities SHALL fail to render rather than carry either on a scope. The
machine answer SHALL carry every field on every claim and SHALL not inherit.
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
  the inheritance rule and reads captured authority/evidence, importing no
  production vocabulary or rendering code.
- **Falsifier**: a positive claim lacks current support, a tuple field is
  absent/out of vocabulary after expansion, a scope carries a value that
  differs from a claim under it that does not carry the field itself, a reason
  has no route, Unknown is folded into a total, or an aggregate claims its own
  headline status.
```

```
#### Scenario: A field shared by every claim under one scope is carried once

- **WHEN** every claim under one scope has the same value for a tuple field
- **THEN** the scope may carry that field once and each claim's expanded tuple
  equals its machine tuple
- **AND** a claim whose value differs carries the field itself, and a scope
  whose value would hide that difference fails the oracle
```

PWB-REQ-014:

```
Every owner-visible narrative unit SHALL carry `presentation-artifact` and
`non-citable` attributes and exactly one claim role: anchored project fact,
explicitly non-normative framing, or epistemically labeled claim. In the human
view the two attributes MAY be carried once by an enclosing scope under the
PWB-REQ-007 inheritance rule; every owner-visible narrative unit under that
scope then carries them by that rule, the claim role stays on each unit, and
the machine form carries both attributes on every unit.
```

```
- **Observable**: claim roles are machine-readable on every unit and the
  non-authority attributes are machine-readable on every unit directly or by
  scope expansion; every claim has exact/minimal anchors and no downstream
  authority reference targets Polaris.
- **Oracle**: the oracle expands scopes with its own statement of the
  inheritance rule; independent claim-to-source mapping establishes covering,
```

```
- **Falsifier**: an unclassified narrative unit, uncovered claim, surplus or
  ambiguous anchor, a non-citable or presentation-artifact attribute missing
  after scope expansion, or downstream citation to Polaris.
```

PWB-REQ-020:

```
evaluation in the machine answer, preserving multiplicity and exact provenance
state. Recoverability is judged after the human view is expanded under the
PWB-REQ-007 inheritance rule; a scope value SHALL never stand in for a claim
whose own value differs.

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

`design.md` gains decision 9, "Carry a shared claim field once per scope",
after decision 8; it restates the rule and the rejected alternatives and
binds nothing the spec does not.

## What explicitly does NOT change

- The machine answer. Every claim in the machine form carries every tuple
  field, its evaluation identity and both non-authority attributes exactly as
  today; the machine form never inherits.
- The tuple vocabulary: label, tier, exactly one primary reason, zero or more
  closed secondary reasons, freshness, challenge state, evaluation identity,
  RFC2-24 Unknown reasons verbatim with routes. No field is dropped for any
  claim in any channel.
- One tuple per claim in the parity multiset. Expansion restores one complete
  tuple per rendered claim before comparison, so the comparator still reports
  both denominators and PWB-REQ-020's `collapsed` and `duplicated` falsifiers
  keep their meaning. Claim identity is never inherited.
- Unknown never folds. A scope may carry a value only when every claim under
  it has that value; an Unknown claim under a scope carrying a positive label
  carries its own label, and the scope-hidden falsifier fires if it does not.
- Evaluation identity per claim (RFC7-16). It may be carried by a scope only
  because a page that would carry two distinct identities fails to render.
- The claim role. PWB-REQ-014 keeps exactly one role on each narrative unit;
  only `presentation-artifact` and `non-citable` may be scoped.
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
RFC7-16 and RFC7-33 (evaluation identity and machine-readable distinctions on
every rendering, preserved by expansion), CC-TEST-5 and CC-TEST-6 (the
falsifier set grows by one class and the mutation proof names it). Decision
basis: `.syzygy/governance/decisions/POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`
(P-67, 2026-09-13, question 2) and the P-63 ceiling posture it builds on.

## Evidence or decision basis

- `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json` — the
  sizes and per-item cost above [Observed].
- `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` §"Lane B" and §"Draft
  semantic delta" — the sketch this delta finalizes and the saving estimate
  [Inferred].
- `docs/reviews/R-PWB-M1-POLARIS-LANE-A-RAW.md` — the lane A review, whose
  findings were dispositioned in the evidence record.

## Terms introduced or retired

Introduced: **scope** (one element carrying a machine-readable scope marker,
under which claims may inherit field values) and the **inheritance rule**
(stated once, in PWB-REQ-007). **scope-hidden** names the new falsifier and
mutant class. Nothing retired.

## Downstream impact

`IMPACT-LEDGER.md` in this directory: 80 tracked files cite at least one of
the three identifiers, over a denominator of 1,216 tracked files at the
baseline, by two methods that agree (Python regular expression over every
tracked file; `git grep -F` per identifier, union). Every file is classified
there; the ones the implementation must touch are the renderer, the three
oracles that read tuples or the two attributes, and the mutation sweep.

## Migration and supersession plan

1. This package is reviewed in fresh context (`REVIEW-BRIEF.md`); the raw is
   retained under `docs/reviews/` and its findings are dispositioned here.
2. The owner reads `OWNER-DECISION-PACKET.md` and answers it or does not.
3. On the exact phrase, a dedicated recorder (the 2026-09-05 shape) applies
   `proposed/*.patch` with the builder's `--apply --at-adoption`, verifies
   that every manifest row now hashes the tree, writes the dedicated act
   record and the aggregate section, and registers the act as the third
   link of the PWB successor chain — all in one change, so CG-7h never sees
   a drifted tree.
4. Only after that act does an implementation bead exist. It carries the
   renderer change, the comparator's own expansion, the one-evaluation
   assertion, the scope-hidden mutant class and a measurement in the lane A
   shape; `tasks.md` (unbound) takes its rows then.
5. Rollback is a later successor act; the 2026-09-05 package stays the
   authority until then and its records are never edited.

## Review

Class: fresh-context semantic review of a normative delta (CC-REV-4,
CC-REV-6). Reviewer, verdict verbatim and the raw's path are appended below
when the review lands; the section is empty until then.
