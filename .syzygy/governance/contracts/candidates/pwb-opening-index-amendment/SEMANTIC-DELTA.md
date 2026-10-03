# Semantic delta — PWB opening-index amendment (PWB-REQ-010)

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. Only the owner's version-tagged sign-off binds it (VIS-4; Scope A,
> `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`).

**Drafted** 2026-10-03 on bead `syzygy-u05.12` (pursuit move N12, slice A),
register row P-98. Base: the signed PWB specification at `c371339d`. The
exact proposed bytes are `proposed/spec.md.patch`; read them with
`python3 scripts/build_pwb_opening_index_amendment.py --diff`. This file
says what they mean; where the two differ, the patch is what would be signed.

## Warrant

- **RFC7-1 and RFC7-13**, PWB-REQ-010's own primary and contract warrants:
  the first reading level presents the project before any one capability.
  This amendment adds a way in to that level and changes none of its
  content.
- **RFC7-30**, the cold-open criterion: a fresh reader "states in their own
  words" why the project exists, what it promises, what it refuses, its
  capabilities, where exactness lives and one thing it does not know
  (`.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md:134`).
  The index rows are those prompts, as PWB-REQ-021 names them.
- **RFC7-31**, the limit this amendment keeps: "The verdict is the owner's
  recorded human judgment — never rendered Observed, never a score"
  (same file, line 162).
- **VIS-1 and VIS-3** (comprehension; digestible by an unfamiliar human).

No warrant moves. PWB-REQ-010's `warrants:` block is byte-identical, so
`GOVERNING-DEPENDENCIES.md` changes only in the specification digest it
quotes and `CONTRACT-COVERAGE.md` regenerates byte-identical.

## Evidence or decision basis

- **The finding.** The 2026-09-22 vision pursuit, move N12
  (`docs/pursuits/2026-09-22-vision-pursuit.md`, section "N12"), finding
  L9-F1: on the capture it measured, the material for all nine cold-open
  questions had arrived well before the end of the page, and the page said
  so nowhere, so a reader had no licence to stop. [Unknown] How far into
  Butlers' Polaris that material ends today. No figure from that capture is
  quoted here: the capture is not tracked, and a figure is measured on a
  fresh private-daemon capture at a named commit when this is implemented.
- **The premise check.** The bead as written asked for a scripted
  comprehension probe and a line saying "the nine answers end here". Both
  fail RFC7-31 and PWB-REQ-021, which say readiness and the nine answers
  "SHALL remain execution facts, never a verdict or proof of comprehension"
  and "The implementation SHALL NOT score or decide the semantic correctness
  of the owner's own-words answers" (PWB spec, lines 1941–1945 at
  `c371339d`). The coordinator narrowed the bead to this slice and slice C
  (`syzygy-u05.12` notes, 2026-10-03). This draft keeps only what a machine
  can say without judging: where each declared target begins, and where the
  last one begins.

## Current meaning

PWB-REQ-010 says that when Polaris opens it presents Butlers' purpose,
promises, non-goals, architecture, V1 scope and success criteria before any
one capability's detail. It says nothing about an index, about how far into
the page each project question's material lies, or about where that
material ends.

## Proposed meaning

Three additions to PWB-REQ-010, plus verification limbs and two scenarios.

1. **An opening index of nine rows.** The first reading level begins with
   nine rows, one per PWB-REQ-021 answer identity, in PWB-REQ-021's order.
   The requirement itself declares each row's target in a table: purpose
   statements, promise statements, non-goal statements, the capability
   catalog, the first link to an exact requirement's text, the opening
   Unknown aggregate, the claim-strength legend, the architecture
   statements, and the V1 scope and success-criteria statements. No run,
   reader or model decides a target. If a target is not rendered, its row
   says so and routes nowhere; it never routes to a substitute. A row
   routes to its target's heading, or its first element when it has none,
   and its accessible name names its question.
2. **Reach offsets.** Each row shows its target's word offset: the number
   of counted words before the target's first counted word. Exactly one
   stopping line stands right after the first element of the
   last-beginning target and gives that offset and the page's word total.
   Words are counted one declared way, over the document as the browser
   holds it after load: maximal non-whitespace runs in text nodes, in
   document order. Left out: `script`, `style`, `template` and `noscript`
   content; anything hidden (`hidden`, `aria-hidden="true"`,
   `display: none`, `visibility: hidden`); the content of a `details`
   closed on first load, except its `summary`, which a reader sees; and the
   index and stopping line themselves.
3. **Not a verdict.** The index, the offsets and the stopping line are
   presentation measurements. They carry no epistemic tuple, join no
   PWB-REQ-020 parity family, enter no PWB-REQ-021 record or readiness arm,
   and never say or imply that a prompt is, or can be, answered. Row names
   are `action-label` strings, the offsets and stopping line
   `scope-instruction` strings, and an unrendered row's text an
   `epistemic-disclosure`, all under PWB-REQ-012's copy rules; that
   requirement's one-instruction limit counts only the statement of the POC
   bound. The index sits before the PWB-REQ-014 narrative tree and is not
   one of its units.

The verification limbs add: a Case with every target rendered and one with
the opening Unknown aggregate absent; an Oracle in which an independent word
counter recomputes every offset and the total from the document after load,
each row's target is compared with the requirement's table (located by a
recognizer whose selectors are published with the oracle), never the
renderer's mapping, and exactly one stopping line must stand where the
requirement places it; and Falsifier limbs for a missing, duplicated,
misordered or misrouted row, a routed unrendered row, an offset that
differs from the independent count, a missing, repeated or misplaced
stopping line or one whose offset is not the largest, a stopping line that
claims an answer, and an offset presented as a claim, parity fact or
walkthrough fact.

New scenarios: "The opening index shows where each project question's
material begins" and "An unrendered index target is stated, not
substituted".

## Why each part has the shape it has

- **Why PWB-REQ-010, not PWB-REQ-011 or PWB-REQ-021.** PWB-REQ-010 owns the
  first reading level and what it presents first; the index is the head of
  that level. PWB-REQ-011 owns the route to exact sources, and the
  `exact-requirement` row only points at the first such link without
  changing the route. PWB-REQ-021 owns the walkthrough record; putting
  offsets there is slice B, not drafted (owner packet, question 4).
- **Why the table declares the targets.** If a run chose which element
  "answers" a question, that choice would be a machine judgment of
  comprehension, which RFC7-31 forbids. A fixed target is a navigation fact.
- **Why rows follow PWB-REQ-021's nine identities, not RFC7-13's
  categories.** They are the questions the walkthrough asks; RFC7-13's
  categories are already the order of the first reading level. The owner
  may prefer the other (packet, question 2).
- **Why closed `details` content is left out of the count.** It is not in
  the reader's flow until opened. Counting it would make the offsets
  describe a page no reader sees on arrival. A closed disclosure's
  `summary` is on screen, so it counts. The total uses the same rule so
  that the two numbers compare.
- **Why the index does not count itself.** Its rows show the offsets; if
  they were counted, every offset would depend on the digits of the others.
- **Why the stopping line says only numbers.** "Everything you need ends
  here" would be the verdict RFC7-31 reserves to the owner. The line marks
  where the last declared target begins, and nothing about understanding.

## What explicitly does NOT change

- Every other requirement, the reader definitions and the text before the
  requirements: byte-identical (the builder checks this).
- PWB-REQ-010's existing text, scenarios and warrants: every signed line
  survives except five limb-ending lines that the amendment extends, each
  listed in the builder as `replaced`; the builder checks that each one's
  signed text, less its full stop, still opens a proposed line.
- PWB-REQ-021: unchanged. The walkthrough record, its readiness arms and
  the owner's verdict are untouched.
- The capability table: row 9 already covers this ("Present the whole
  project before capability detail | covered — PWB-REQ-010"), so no row is
  added.
- No Butlers source is read differently and no new content class is read.

## Terms introduced / retired

- **Opening index**, **reach offset**, **stopping line**: introduced, each
  defined in the amended PWB-REQ-010.
- **Word**, for this requirement only: defined by the declared method above.
- Nothing retired.

## Downstream impact

See `IMPACT-LEDGER.md`. In short: implementation files a later build would
touch are named there for planning only; signing authorizes no build.

## Migration / supersession plan

- Signed by version tag under Scope A. The sign-off change runs
  `python3 scripts/build_pwb_opening_index_amendment.py --apply --at-adoption`
  through `scripts/record_versioned_signoff.py`, which needs a registry entry
  for this package added in that change.
- The accessible-name amendment (P-99), the class-granular extraction
  amendment (P-86) and the release-label amendment (P-85) are pending over
  the same signed subject. The spec patches touch different requirements and
  compose in any order: each builder checks its package against each other
  pending package, and all 24 orders of the four spec patches were applied
  on 2026-10-03 to one identical result. But every package's
  manifest hashes post-apply bytes against the current tree, so whichever is
  signed second is regenerated with `--write` first and its new manifest is
  reviewed again.
- `scripts/check_spec_reconciliation.py` carries a literal PWB census (17
  requirements and the scenario count); the sign-off change updates it, as
  for every PWB amendment.

## Review

One fresh-context round over this package and the accessible-name package
together returned `REVISE`. Under the coordinator's direction after the
round, the findings were repaired once and no round 2 was dispatched; see
`ROUND-1-DISPOSITIONS.md`. These bytes are unconfirmed.
