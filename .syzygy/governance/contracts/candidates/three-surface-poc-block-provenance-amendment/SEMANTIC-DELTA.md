# Semantic delta — Three-Surface POC block-provenance amendment (N9, POC half)

> **Candidate — binds nothing.** This package proposes one amendment to the
> signed Three-Surface POC specification. Nothing here is signed, adopted or
> labelled accepted, and no implementation is authorized (VIS-4). Only the
> owner's sign-off binds it, and building it needs a fresh implementation
> authorization after that.

**Artifact(s):** `openspec/changes/three-surface-poc-experience/`:
`specs/three-surface-poc-experience/spec.md` (POC-REQ-001 and POC-REQ-010
only) and `GOVERNING-DEPENDENCIES.md` (regenerated; only its `Source:` digest
moves).
**Stable IDs affected:** POC-REQ-001, POC-REQ-010. No identifier is added,
renumbered or retired.
**Change class:** Normative. Both observations must state their provenance
once, in the shape the rest of the machine answer uses, and no row beneath
them may restate the observation's revision or capture instant. An
implementation that complied before does not comply now: today every row
restates its block's revision.
**Author:** a drafting session (Claude), bead `syzygy-u05.9`.
**Date:** 2026-10-03, over `main` at `71b4f525`.

**Sibling package.** The other half of N9 is a separate OpenSpec change
against the PWB specification: `pwb-anchor-resolution-amendment/`
(PWB-REQ-014). The two share one review round and are signed separately.
Neither depends on the other.

## Warrant

- **The move.** [Observed] Bead `syzygy-u05.9`, pursuit move N9 of
  `docs/pursuits/2026-09-22-vision-pursuit.md`, released for drafting when
  the pursuit's hold gate `syzygy-dca` closed. It merges agent moves S6-M1
  ("one provenance shape reused by every bulk key") and L11-M3 ("delete two
  per-row fields that restate their own block header"), and asks to "land the
  rule that a row may not repeat a value its block declares".
- **The coordinator's ruling, 2026-10-03.** [Observed] Recorded in the bead's
  notes: the per-row rule is POC-specification scope, against POC-REQ-010, so
  it is drafted as its own POC-family change and no OpenSpec change crosses
  categories. The drafter put POC-REQ-001 in the same package because the
  same rule and the same evidence govern the code-structure block, and
  S6-F2's "three provenance shapes" finding is about this route.
- **The bead's ordering clause is stale.** [Observed] It said the change "must
  land before dov.10.1 publishes the response-identity digest". dov.10.1
  merged on 2026-09-22 (PR #56), and `/api/poc` already serves
  `responseIdentity`. This change will move that digest like any other change
  to the body; nothing orders the two any more.
- **The sign-off route is an open question.** The Scope A direction names
  "the PWB specification deltas, the observer registry entry and the contract
  successors queued behind them". A POC specification amendment is not in
  that list. The pending POC identity amendment already asks the owner the
  same question (P-84, its question 2); this package inherits the answer.

## Evidence or decision basis

Every figure below is [Observed] at Syzygy `71b4f525` and Butlers
`32f38feb`, from one private-daemon evaluation, recorded in
`docs/evidence/n9-machine-channel-provenance-measurement-2026-10-03.json`
with both captures' byte counts and digests. The script is
`scripts/measure_machine_channel_provenance.py`.

- **Three provenance shapes.** `entities[]` and `relationships[]` carry a
  `provenance` list of records with `kind`, `source`, `revision` and, where
  one exists, `digest`. `workItems` carries `kind`, `beadPrefix`,
  `doltRevision` and `capturedAt` in its header. `codeStructure` carries
  `kind`, `revision` and `capturedAt` in its header. A consumer has to know,
  per key, which of the three it is reading.
- **Every row restates its header.** All 7,952 work items carry a
  `doltRevision` equal to the header's, and all 6,950 code-structure files
  carry a `revision` equal to the header's.
- **What that costs.** In the compact body those fields take 50 bytes per
  work item and 54 per file: 397,600 + 375,300 = 772,900 bytes, 13.44% of the
  5,751,883-byte `/api/poc` body. The pursuit's "~740 KB / 13.2%" was
  measured at an earlier Butlers revision over 7,527 items and 6,749 files;
  the figure grows with row count.
- **Nothing else in the body repeats a header this way.** A sweep over every
  list of records in the body, comparing each record field against the
  enclosing object's scalar field of the same key, finds four populations:
  the two above, and two inside `projectShape.facts[].fact.declarations[]`
  (`fact` 416 of 416, `value` 415 of 416). Those two are per-declaration
  evidence, owned by the PWB specification. The one `value` that differs
  shows why a declaration carries its own: that fact is Unknown and states no
  value, while its declaration still records what it declared.

## What changes, and why each part has the shape it has

### 1. One statement of provenance per observation

Each observation states its provenance once, as one record in the shape the
machine answer's entities and relationships carry, and names its revision
nowhere else. The second clause matters: without it, an implementation could
add the shared record and keep `doltRevision` beside it, which is a second
statement of the same value inside the same block. The text names the shape
by reference to the entities and relationships, not by field names, so the
specification does not freeze a type name.

[Inferred] The existing provenance kinds have no Dolt kind. Adding one is an
implementation choice inside the shared shape, not a second shape.

### 2. No row restates the observation's identity

"Identified observation" is already defined in the reader notes as the pair
(source revision, capture instant). The rule forbids exactly those two values,
compared as whole field values, in any row field. It is narrower than the
bead's "a row may not repeat a value its block declares", on purpose:

- the general form would also reach the PWB-owned declaration fields above,
  where repetition is evidence, and this package may not amend the PWB
  specification;
- a whole-value comparison against two named values has an exhaustive oracle
  and no judgment call; "a value its block declares" would need a list of
  what each block declares, per block.

Each row still carries the revision as provenance. The signed sentence
"whose every entry carries that revision as provenance" stays in both
requirements, and the amendment says how: by belonging to the observation.

### 3. The oracles become sweeps

Both requirements were sampled checks. Each now adds a sweep over every
served row, with the complete served set as its denominator, comparing field
values against the two identity values.

## Current meaning, and proposed meaning

The proposed bytes are `proposed/spec.md.patch`; read them with
`python3 scripts/build_three_surface_poc_block_provenance_amendment.py --diff`.
The builder lists every signed line the patch replaces (13 in POC-REQ-001,
11 in POC-REQ-010) and fails if any other signed line is lost.

| Part | POC-REQ-001 now | POC-REQ-001 proposed |
|---|---|---|
| Required behavior | One identified observation; every entry carries the revision as provenance | Unchanged sentence, plus **One statement of provenance**: one shared-shape record names the revision, the revision appears nowhere else, no entry carries the revision or capture instant |
| Case | Run at a known commit | Plus a sweep of every served entry, denominator the complete inventory |
| Observable | Revision and inventory in the machine answer | The provenance record and inventory in the machine answer |
| Oracle | Served revision vs `git rev-parse HEAD`; sampled size and digest | The record's revision vs `git rev-parse HEAD`; sampled size and digest; every entry's fields vs the two identity values |
| Falsifier | An entry whose revision, size or digest differs; no revision | A differing record revision or sampled size or digest; no record, another shape, or the revision twice; an entry carrying the revision or capture instant |
| Scenario | Identified by R; every entry cites R as its provenance revision | Identified by R, whose one record names R; every entry takes R from that record; AND no entry carries R or the capture instant |

POC-REQ-010 changes the same way, with "Dolt revision" for "revision" and
"work-item fact" for "inventory entry". Its signed sentence "with every served
work-item fact carrying that revision as provenance" stays.

The warrants blocks do not move, so no `CONTRACT-COVERAGE.md` row moves.

## What explicitly does NOT change

- Every other requirement, the reader notes, the warrants, the proposal, the
  design and the contract-coverage matrix are byte-identical; `--check`
  enforces it.
- Requirement and scenario counts: 24 and 24. No scenario is added; each
  amended scenario gains one AND line.
- Which facts are served, their values, the registered bead-prefix rule
  (POC-REQ-011) and the metadata-only rule (POC-REQ-002).
- The human surfaces' content. [Observed] Polaris, Trajectory and Orrery
  read the block headers' revisions, never a row's (sweep in
  `IMPACT-LEDGER.md`).
- The PWB specification, including the per-anchor revision PWB-REQ-014
  requires on every anchor.

## Terms introduced / retired

- **One statement of provenance** (introduced, as a bullet label): the
  obligation above.

None retired.

## Downstream impact

See `IMPACT-LEDGER.md`. In short, once signed and authorized: the two
observation types and their constructors in `packages/three-surface-poc-core`
lose the per-row field and gain one shared-shape record, and every reader of
`workItems.doltRevision` or `codeStructure.revision` reads the record instead.
`/api/poc` shrinks by about 773 KB at this capture.

## Migration / supersession plan

- **Sign-off.** By the route the owner chooses for POC amendments (P-84
  question 2). The sign-off change runs `--apply --at-adoption` and carries
  the reconciliation updates in `IMPACT-LEDGER.md`.
- **Order against the identity amendment.** It patches the reader notes,
  adds POC-REQ-054 and 055 and amends POC-REQ-060, not 001 or 010. The two spec patches compose in either
  order, and `--check` proves it. Both rewrite the dependency declaration's
  `Source:` line, so whichever is signed later is regenerated with `--write`
  over the earlier one's applied bytes.

## Review

**Required class:** fresh-context review (CC-REV-1), one round shared with
the PWB half; stopping rule: on REVISE, repair once, dispatch no second round,
and route the result to the owner.
**Reviewer:** a fresh-context subagent that did not draft this package.
**Verdict:** recorded verbatim in the raw under `docs/reviews/`, and in the
PWB half's `ROUND-1-DISPOSITIONS.md`, which covers both packages.
