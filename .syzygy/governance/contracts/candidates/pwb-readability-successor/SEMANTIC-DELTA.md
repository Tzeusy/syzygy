> **Candidate — binds nothing.** These proposed bytes leave the eleven signed
> PWB behavior artifacts unchanged. Only an owner sign-off of a version of this
> package, after a fresh independent review of its exact bytes, could make them
> effective. No phrase is offered here.

# Semantic delta PWB-READABILITY-1 — a newcomer can read the PWB specification

**Artifacts:** the eleven-artifact signed
`openspec/changes/polaris-project-wide-butlers-model/` behavior package. Four
proposed rows move: `specs/polaris-project-wide-butlers-model/spec.md`,
`proposal.md`, `design.md` and the regenerated `GOVERNING-DEPENDENCIES.md`.
The other seven manifest rows equal current bytes.

**Stable IDs affected:** all 17 `PWB-REQ-*` blocks are restyled in place. No
requirement or scenario identity is added, removed, renamed, renumbered or
reordered.

**Change class:** **Structural and Clarifying for the specification; Changed
for 15 non-normative units of the proposal and design.** Every requirement's
normative words, every scenario, every verification block and every warrants
block are equal under the builder's normalization (below). The proposal and
design also stop saying things that became false after later acts, and start
summarizing amendments that were signed after they were written; those 15
units are classified `changed`, not `clarified`. The classification is a
reviewable claim, recorded unit by unit in `SEMANTIC-MAP.json`, never a
blanket equivalence.

**Author:** agent drafting for bead `syzygy-73e.5.5`.

**Date:** 2026-10-02.

## Predecessor

The effective predecessor is the tree at
`1ecb99854c4859786cfa8626cfc1698b73271809` (`main` after the item-depth v1.0
sign-off). Its eleven bytes equal the item-depth package's manifest rows; the
builder checks that equality and fails when either side moves. Every PWB
behavior successor is performed, version-signed or declined at that head:

- performed acts: opening band, exact-source render mode, machine view;
- version-tagged v1.0 sign-offs: missing currency, dismissal expiry,
  container shape, item depth;
- declined: lane B (the scoped-attributes package).

## Current meaning

The specification reads as one dense paragraph per requirement, often fifteen
or more sentences, followed by Case, Observable, Oracle, Oracle-independence,
Falsifier and, for some, Mutation-proof bullets, then scenarios and warrants.
Nothing tells a first-time reader what the whole specification covers, how a
block is laid out, or that the file order is not numeric.

The proposal and design were written on 2026-08-31 and amended on
2026-09-02 and 2026-09-05. Seven amendments have changed the specification
since, and only two of them also touched the proposal (missing currency,
dismissal expiry) and two the design (render mode, item depth). So both
describe less than the specification now requires: the proposal names none of
the opening aggregate, project profiles, item depth, render modes or machine
views. Two sentences in each have also become false: the proposal calls the
2026-09-05 repair "a candidate" that "binds nothing" and the 2026-09-02 bytes
"the behavioral authority", and the design says that repair "remains inert
until a later owner act".

The complete current text is the signed predecessor. This delta does not copy
it; `proposed/*.patch` is the exact old-to-new record.

## Proposed meaning

The behavioral meaning of the specification is unchanged.

- **Reading guide.** `## Purpose` keeps its words and gains a guide marked
  non-normative, which states that it adds, removes and changes no
  requirement. It says what the specification covers, how a requirement block
  reads and that the order is file order with gaps, then gives one flow
  diagram and a table of the 17 requirements with their verbatim titles and
  groups. The builder checks each table title against its heading.
- **Requirement layout.** The group and form line is unchanged. The normative
  words follow:
  - in six requirements, as the same paragraph;
  - in two, one bullet per sentence;
  - in nine, as bullets under bold labels from a closed set of 56 labels (for
    example `**Read authority.**`, `**Relation results.**`). A label is a
    reading aid and adds no word to the requirement; the builder fails on a
    label outside the closed set.
- **Verification.** A `**Verification.**` line now separates the normative
  words from the Case bullets. The Case-to-Mutation-proof bullets, every
  scenario and every warrants block are byte-equal.
- **Proposal.** Rewritten answer-first in the present tense. A status banner
  names the 2026-08-31 sign-off and routes every later amendment to
  `ACCEPTANCE-ACT-RECORD.md` instead of listing them. The What Changes list
  now summarizes the signed opening aggregate, project profiles, item depth,
  render modes and machine views. The Capabilities, Impact and Scope lists
  keep their content; the Scope out-of-scope sentence and the coverage
  quotation are byte-checked.
- **Design.** Rewritten answer-first. Data Flow moves before the decisions
  with a diagram of the same ten steps, which stay byte-equal. Decisions gain
  short summaries of the signed project profiles, opening aggregate,
  missing-currency and dismissal rules and machine views, each naming the
  requirement that governs. The governing-intent relation diagram is
  byte-equal. The stale Migration Plan sentence is removed.
- **`GOVERNING-DEPENDENCIES.md`** moves only its generated source digest; the
  17-requirement, 100-authority union is unchanged.

## How "keeps its words" is decided

`scripts/build_pwb_readability_successor.py` splits each requirement into its
group line, its normative region and its tail (from the first `- **Case`
bullet). For the normative region it removes only: line breaks, list markers,
a line-end hyphen or slash rejoined with its continuation, the closed label
set and the `**Verification.**` separator. It then requires:

- the normalized words to be equal;
- the sequence of modal words (`SHALL NOT`, `SHALL`, `MUST NOT`, `MUST`,
  `MAY`) to be equal, over whitespace-normalized text;
- the group line, the tail and the warrants block to be byte-equal;
- every scenario heading and body to be byte-equal, in the same order.

A weakened modal, a modal swapped for MAY, a dropped Unknown qualification, a
dropped fail-closed refusal, a dropped refusal clause, an added label word and
a relabel outside the closed set are among the 52 mutants `--selftest` kills.

## Semantic map

`SEMANTIC-MAP.json` holds one row per unit, 120 in all, each classified
`preserved`, `clarified` or `changed` with its observable, coverage, contract
and implementation consequence:

| Population | Units | preserved | clarified | changed |
|---|---:|---:|---:|---:|
| Requirements | 17 | 17 | 0 | 0 |
| Scenarios | 44 | 44 | 0 | 0 |
| Purpose | 3 | 2 | 1 | 0 |
| Proposal | 35 | 23 | 3 | 9 |
| Design | 21 | 12 | 3 | 6 |

The builder recomputes `changed_count` (15) and fails when a requirement or
scenario is anything but `preserved`, when a unit is missing, or when a
classification is outside the closed three.

The 15 changed units, all in non-normative prose:

1. Proposal status banner: present tense, routes amendments to the act record.
2. Proposal What Changes: the opening Unknown aggregate (PWB-REQ-010).
3. Proposal What Changes: project profiles (PWB-REQ-002, container shape).
4. Proposal What Changes: capability detail becomes every catalog item in
   depth (PWB-REQ-015, item depth).
5. Proposal What Changes: exact-source render modes (PWB-REQ-011).
6. Proposal What Changes: human and machine views match, two machine-view
   categories (PWB-REQ-020).
7. Proposal Authority: the false "is a candidate and binds nothing" sentence
   removed.
8. Proposal Authority: the 2026-09-05 amendment's own history removed; that
   act's record carries it.
9. Proposal Authority: "no widening, no implementation authority" restated
   for the whole specification rather than for one amendment.
10. Design Context: the one-capability model put in the past tense.
11. Design Decision 1: project profiles summarized.
12. Design Decision 3: the opening aggregate summarized.
13. Design Decision 9: missing currency bound and dismissal summarized.
14. Design Decision 10: machine views summarized.
15. Design Migration Plan: the false "remains inert until a later owner act"
    sentence removed.

Each summary restates signed requirement text and names the requirement that
governs; none adds a rule. Whether each summary is faithful is review
criterion 6.

## What explicitly does NOT change

- Any `PWB-REQ-*` identity, title, group, form, modal, condition, scenario,
  verification block or warrant.
- Any Unknown, refusal, fail-closed, denominator, parity, provenance,
  accessibility or non-inference obligation.
- The requirement order, including PWB-REQ-004 after PWB-REQ-007.
- `CAPABILITY-COVERAGE.md`, `CONTRACT-COVERAGE-REPAIR-DELTA.md`,
  `CONTRACT-COVERAGE.md`, the three `contract-coverage-matrix/` parts and
  `.openspec.yaml`: byte-equal rows, regenerated or checked by the
  repository's own generators over the proposed bytes.
- `tasks.md` and `contract-coverage-parts/`, which are outside the
  eleven-row subject.
- The consent record, secret policy, observer registry entry, implementation
  authorization and any code.

## Warrant

The owner directed the progressive readability rewrite on 2026-09-27 under
`syzygy-73e`. D5, D6 and CC-REV-8 are in force. VIS-3 requires the successor
to stay intelligible to a fresh reader; VIS-4 reserves adoption to the owner.
Sign-off is by version under
`decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`.

## Terms introduced / retired

None. The bold labels and `Verification` are presentation aids, not project
vocabulary or behavioral fields; the guide says so.

## Downstream impact

`IMPACT-LEDGER.md` records the reference population and its disposition.

## Migration / supersession plan

1. A fresh independent review of the exact candidate head.
2. Every finding dispositioned; any edit retires the review.
3. On a clearing verdict, the owner is asked once whether to sign off v1.0.
4. On sign-off, `scripts/record_versioned_signoff.py` applies the four patches
   in one change, proves every manifest row against the tree, writes the
   record and tags the merged commit. The same change wires one
   `VERSIONED_PWB_PACKAGES` row, one `VERSIONED_LATER` entry and one battery
   line.
5. The predecessor's bytes stay as history in their sign-off records.

Before sign-off, rollback is deleting this candidate. After it, rollback is a
later signed version.

## Review

**Required class:** fresh independent semantic and VIS-3 fresh-reader review
over the exact candidate head (`REVIEW-BRIEF.md`).

**Verdict:** not yet reviewed.
