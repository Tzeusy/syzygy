# Semantic delta — PWB accessible-name amendment (PWB-REQ-016)

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. Only the owner's version-tagged sign-off binds it (VIS-4; Scope A,
> `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`).

**Drafted** 2026-10-03 on bead `syzygy-u05.12` (pursuit move N12, slice C),
register row P-99. Base: the signed PWB specification at `c371339d`. The
exact proposed bytes are `proposed/spec.md.patch`; read them with
`python3 scripts/build_pwb_accessible_name_amendment.py --diff`. This file
says what they mean; where the two differ, the patch is what would be signed.

## Warrant

- **RFC7-34**, PWB-REQ-016's primary warrant: "Every such distinction is
  recoverable **without colour, position, or layout** — by label, text, or
  structure", and its reachability limb: "Every traversal of the disclosure
  path must be operable **without a pointing device**"
  (`.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`,
  lines 241 and 249–251). A screen-reader user who meets many links with the
  same name cannot tell their targets apart by label; one who meets a
  heading tree with skipped levels cannot recover the page's structure.
- **POC-REQ-061**, PWB-REQ-016's parent: the accessibility floor on every
  surface. This amendment stays on Polaris; it does not touch the POC
  specification.
- **VIS-1, VIS-3 and VIS-7.**

No warrant moves. PWB-REQ-016's `warrants:` block is byte-identical, so
`GOVERNING-DEPENDENCIES.md` changes only in the specification digest it
quotes and `CONTRACT-COVERAGE.md` regenerates byte-identical.

## Evidence or decision basis

- **The findings.** The 2026-09-22 vision pursuit, move N12
  (`docs/pursuits/2026-09-22-vision-pursuit.md`, section "N12"), findings
  S15-F1, S2-F2 and S2-F3: on the capture it measured, many links and
  disclosures shared a small number of visible names, and the accessibility
  checker's fixture covered a small part of the page and could not see them.
  [Unknown] How many interactive elements and headings Butlers' Polaris has
  today and how many names they share. No figure from that capture is quoted
  here: the capture is not tracked, and the figures are measured on a fresh
  private-daemon capture at a named commit when this is implemented.
- **What the checker does today.** [Observed at `c371339d`]
  `apps/three-surface-poc/src/polaris-accessibility.ts` checks that every
  link, heading, region and navigation node in the browser's accessibility
  tree has a non-empty name, and that the tree has one link per rendered
  link (lines 523–540). It does not compare names across targets and does
  not read heading levels: the file contains no `level` token.
- **Scope.** The coordinator narrowed the bead to this slice and slice A
  (`syzygy-u05.12` notes, 2026-10-03). The cross-surface part is POC-REQ-061
  work and is not drafted (packet, question 4).

## Current meaning

PWB-REQ-016 says every distinction and summary-to-source path on Polaris is
recoverable by text and operable by keyboard, and that a nonvisual or
keyboard-only cold-open walkthrough runs and records its mode. It does not
say that links with different targets must have different names, says
nothing about heading levels, and does not say what population its sweep
must cover.

## Proposed meaning

Three additions to PWB-REQ-016, plus verification limbs and two scenarios.
*(Repaired 2026-10-14, cycle 2: this section describes the bytes as
repaired for the round-2 findings; `ROUND-2-DISPOSITIONS.md` §"Repairs,
2026-10-14 (cycle 2)" maps each change.)*

1. **Distinct accessible names.** Two interactive elements on a Polaris
   page (links, buttons, `summary` disclosures and form controls) whose
   targets or controlled regions differ have different accessible names,
   as the browser computes them. A link's target is its resolved `href`, a
   `summary`'s is its `details`, and a button's or form control's is the
   element its `aria-controls` names, or the control itself. The
   population is every such element in the document after load, including
   those inside a closed `details`, excluding hidden ones. Where elements
   with different targets share one visible label (their text, whitespace
   collapsed), each name begins with that label; where such an element
   leads to an exact-source page, the words after the label include that
   source's repository-relative path as the machine answer carries it. No
   other element is bound by those two rules. Two elements with the same
   target may share a name.
2. **Heading order.** One level-1 heading per page, and in document order
   no heading more than one level deeper than the heading before it. The
   population is every `h1`–`h6` and `role="heading"` element after load,
   including those in a closed `details`, excluding hidden ones. No
   heading is exempt.
3. **Whole-surface population.** Both checks run over every Polaris page
   served at one whole-project evaluation: the entry page and one
   exact-source route response for each source the machine answer lists,
   served or refused. The list comes from the machine answer, not from the
   renderer's links. Each check reports the page count and, per page, the
   element and heading populations. A smaller fixture never stands in.

The verification limbs add a separate Case running both checks over those
pages; Observable limbs for the properties and the denominators; an Oracle
that groups interactive elements by computed name and compares each
group's targets, groups them again by visible label and checks each shared
label's name prefix and, for exact-source targets, the path, reads heading
levels in order, and requires the page count to equal the pages listed from
the machine answer and each per-page denominator the defined population;
an independence line taking the page list and expected paths from the
machine answer; and Falsifier limbs for a shared name across different
targets, a shared-label name without its label prefix or expected path, a
skipped level or second level-1 heading, and a check over fewer pages or a
smaller population.

New scenarios: "Repeated source links are told apart by name" and "Name and
heading checks cover every Polaris page".

## Why each part has the shape it has

- **Why "as the browser computes them".** The visible label is not what a
  screen reader announces. Only the computed accessible name decides
  whether two links can be told apart without sight.
- **Why the same target may share a name.** Two links to the same place
  are not a distinction a reader needs to recover.
- **Why every page.** A fixture that covers part of a page cannot see a
  shared name between an element inside it and one outside it, which is how
  the pursuit's findings arose, and a check of one page says nothing about
  the others the obligation binds. A page count and per-page denominators
  equal to what the evaluation serves are the only ones that make "no
  shared names" mean anything (verification rule 4).
- **Why no heading is exempt.** *(Repaired 2026-10-14, round-2 finding 4.
  This bullet first said "Why verbatim headings are exempt": "PWB-REQ-011
  renders a Butlers body as written; a skipped level there is Butlers' and
  cannot be repaired by Polaris without breaking verbatim rendering". That
  reason did not hold.)* [Observed at `814fbcc1`] The exact-source route
  renders each verbatim body as escaped text in a `<pre>`
  (`apps/three-surface-poc/src/polaris-source.ts` line 123), so it puts no
  heading element on the page. Butlers-declared Markdown on the entry page
  goes through `apps/three-surface-poc/src/polaris-markdown.ts`, which sets
  each heading's level itself (line 179):
  `Math.min(6, anchorHeadingLevel + 1 + heading[1]!.length - shallowestHeading)`,
  where `heading[1]` is the heading's run of `#` marks. Polaris already chooses those
  levels, so it can close a gap without changing a word. [Inferred] That
  re-basing keeps Butlers' relative jumps, so a Butlers document that
  skips a level would render a skip today. The exemption covered nothing,
  and an exemption for those headings would have excused a gap Polaris can
  repair. Whether any exemption should return is put to the owner (packet,
  question 8).
- **Why the name begins with the visible label.** Speech-input users
  activate a control by saying what they see.
- **Why the label rules bind only shared labels, and the path only
  exact-source targets.** A label that no differently targeted element
  shares needs no telling apart. A path is the one name an oracle can take
  from outside the renderer for an exact-source target: PWB-REQ-011's
  machine recovery ties each route to its source, and the machine answer
  carries the source. For other shared labels, such as a disclosure
  toggle repeated per figure, the spec defines no target-to-item mapping
  an oracle could use, so only the label prefix and the distinct-name rule
  bind them. [Inferred] The model's source record carries a `path` field
  (`packages/three-surface-poc-core/src/project-shape-coverage.ts` line
  189 at `814fbcc1`). [Unknown] Whether the served machine answer exposes
  that path for every listed source was not checked here. If it does not,
  this rule also needs PWB-REQ-020 to carry it (packet, question 7).
- **Why the population includes links in a closed disclosure.** A reader
  who opens the disclosure meets them, so they can share a name with a
  link outside it. The heading population already counted them. Today's
  checker reads the accessibility tree
  (`apps/three-surface-poc/src/polaris-accessibility.ts` line 525), which
  leaves them out, so the two would report different denominators unless
  the requirement names one.
- **Why the page list comes from the machine answer.** A list taken from
  the renderer's own links would share the implementation's view of which
  pages exist (CC-SPEC-4's independence limb).
- **Why only Polaris.** PWB-REQ-016 governs Polaris. The other surfaces
  belong to POC-REQ-061 in the Three-Surface POC specification, which is a
  separate signed change.

## What explicitly does NOT change

- Every other requirement, the reader definitions and the text before the
  requirements: byte-identical (the builder checks this).
- PWB-REQ-016's existing text, scenario and warrants: every signed line
  survives except three limb-ending lines that the amendment extends, each
  listed in the builder as `replaced`; the builder checks that each one's
  signed text, less its full stop, still opens a proposed line.
- The keyboard-only walkthrough and its mode flag: unchanged.
- The capability table: row 19 already covers this ("Make every distinction
  and disclosure path nonvisual and keyboard-operable | covered —
  PWB-REQ-016"), so no row is added.
- The Three-Surface POC specification and POC-REQ-061: untouched.

## Terms introduced / retired

- **Accessible name**: the name the browser computes for the accessibility
  tree. Used, not newly defined; the amendment fixes that the computed name
  is the one checked.
- **Whole-surface population**: introduced, defined in the amended
  requirement.
- Nothing retired.

## Downstream impact

See `IMPACT-LEDGER.md`. Signing authorizes no build.

## Migration / supersession plan

- Signed by version tag under Scope A. The sign-off change runs
  `python3 scripts/build_pwb_accessible_name_amendment.py --apply --at-adoption`
  through `scripts/record_versioned_signoff.py`, which needs a registry entry
  for this package added in that change.
- The opening-index amendment (P-98), the anchor-resolution amendment
  (P-96), the class-granular extraction amendment (P-86) and the
  release-label amendment (P-85) are pending over
  the same signed subject. The spec patches touch different requirements and
  compose in any order: each builder checks its package against each other
  pending package, and all 120 orders of the five spec patches were applied
  on 2026-10-03 to one identical result. But every manifest
  hashes post-apply bytes against the current tree, so whichever is signed
  second is regenerated with `--write` first and its new manifest is
  reviewed again.
  *(Marked 2026-10-14: the anchor-resolution amendment (P-96) is no longer
  pending. It was signed v1.0 that day
  (`.syzygy/governance/decisions/PWB-ANCHOR-RESOLUTION-AMENDMENT-SIGNOFF-v1.0.md`),
  so its patch is now part of the signed `spec.md`, and four spec patches
  stay pending: this one, P-98, P-86 and P-85. This package was
  regenerated over the moved `spec.md` in the cycle-2 repair, as the
  sentence above foresaw.)*
- Signing moves PWB `spec.md`, so it interacts with the P-95
  behaviour-contract re-pin: pins re-written to the tree-framing sign-off
  go stale again, and P-95's acts, if not yet performed, are regenerated
  against the new `spec.md` first.
- `scripts/check_spec_reconciliation.py` carries a literal PWB census; the
  sign-off change updates it, as for every PWB amendment.

## Review

One fresh-context round over this package and the opening-index package
together returned `REVISE`. Under the coordinator's direction after the
round, the findings were repaired once and no round 2 was dispatched; see
`ROUND-1-DISPOSITIONS.md`. These bytes are unconfirmed.
*(Marked 2026-10-14: "no round 2 was dispatched" is no longer true. Round 2
ran on the owner's direction of 2026-10-14 and returned `REVISE`
(`docs/reviews/R-PWB-ACCESSIBLE-NAME-AMENDMENT-2-RAW.md` line 4); see
`ROUND-2-DISPOSITIONS.md`. The bytes remain unconfirmed.)*

**Round-2 findings repaired once on 2026-10-14, unconfirmed pending round
3.** On the owner's further direction that day, every round-2 finding,
notes included, was repaired once (`ROUND-2-DISPOSITIONS.md` §"Repairs,
2026-10-14 (cycle 2)"). One fresh round 3 is briefed in
`../pwb-opening-index-amendment/REVIEW-BRIEF.md` §"Round 3" and has not
run. The repair added packet questions 7 and 8.
