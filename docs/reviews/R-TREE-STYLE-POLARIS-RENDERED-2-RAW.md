Title: Rendered-design review verdict (syzygy-73e.10) — code review 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed: bb76bae..528a525
Reviewer: independent fresh-context agent

## Material findings

None. I found no input that wrongly returns `blocking: false`. The exceptions below are notes only.

## Review-1 disposition

- **M1: RESOLVED.** `packages/polaris-generation-core/src/rendered-design.ts:107-113`:
  ```ts
  if (item.judgment === 'prose-sufficient') {
    if (figure?.disposition.kind !== 'produced') return null;
    if (item.support === 'unsupported') return 'unsupported-relationship-drawn';
    if (item.support === 'partly-supported' && item.gaps.length === 0) return 'undisclosed-gap';
    return null;
  }
  ```
  - All three review-1 inputs now block with the right rule. The new test at `rendered-design.test.ts:106-113` asserts exact `[id, rule]` pairs for each.
  - It also has two negative controls: a prose-sufficient relationship with its gap disclosed, and a prose-sufficient unsupported relationship that names the omitted figure `skipped`. Both return `[]`.
  - `missing-diagram`, `diagram-not-produced` and the undrawable-omission requirement still apply only to diagram-clearer relationships, as review 1 suggested.
- **N1: RESOLVED.** The module doc at `:25-27` says `` `diagram-clearer` with `unsupported` support is the spec's undrawable relationship: its recorded omission is the named draft diagram carrying the `omitted` disposition ``.
- **N2: RESOLVED (disclosed).** The doc at `:27-30` names both conditions it leaves out: "that the gap is disclosed in the rendered account at the depth it affects, and whether a requested asset requires the visual anyway (`validateStage` owns requested-asset dispositions)". So `blocking: false` no longer reads as the full scenario.
- **N3: LEFT.** Reasonable: review 1 found nothing wrong here.
- **N4: LEFT.** Reasonable. `validateDraftRecord` (`provider-draft.ts:347-356`) still skips the `sectionId` check, and its docstring still says it "never substitutes for the authoring-stage validation".
- **N5: LEFT.** Reasonable; it is minor. `:139` still merges relationship, section and diagram ids into one target set.
- **N6: RESOLVED.** The new test at `rendered-design.test.ts:115-117` expects `[]` for `[rel('r1'), rel('p1', { judgment: 'prose-sufficient' })]`.
  - If the `judgment === 'diagram-clearer'` filter at `:144` were removed, `deps` would count as shared and `r1` would return `diagram-claimed-by-another-relationship`. So that mutant is killed.
  - The deliberate choice is that a prose-sufficient claim does not count toward sharing. That is sound: a prose-sufficient relationship satisfies no obligation, so it cannot compete for a figure.
- **N7: LEFT.** Nothing to act on; it listed paths that held. I re-probed the relevant ones (below) and they still hold.

## Fail-open probes

I ran these against the built `dist/rendered-design.js`, using a draft with figures `deps` and `extra` (produced), `skipped` (omitted) and `pending` (unresolved).

**Blocking, as they should:**
- A diagram-clearer supported relationship on `deps` plus a prose-sufficient unsupported one on `deps` → `[p1, unsupported-relationship-drawn]`.
- A diagram-clearer supported relationship on `pending` → `diagram-not-produced`.
- A diagram-clearer unsupported relationship on `pending`, or with `none` → `undrawable-without-recorded-omission`.
- A diagram-clearer partly-supported relationship on `skipped`, with gaps → `diagram-not-produced`.
- A retired digest → `blocking: true, retired: true`. This holds with an empty enumeration too, and when the draft changes in a single field (a diagram title).

**Throwing, as they should:** an uppercase digest, an extra field, empty `sourceIds`, a `__proto__` key, a `null` review, and a getter-backed `relationships`.

**Not blocking, and correct:**
- A diagram-clearer unsupported relationship on `skipped` plus a prose-sufficient one on `skipped`.
- A prose-sufficient relationship naming a dangling id or the `pending` figure. Nothing is drawn in either case.
- A diagram-clearer partly-supported relationship on `deps` with its gaps disclosed.
- A prose-sufficient relationship on `deps` alongside diagram-clearer relationships on `deps` and `extra`.
- An advisory reviewer finding.

## Notes (non-blocking)

- **R2-N1: One relationship can name only one figure.** `diagram` holds a single name. If an undrawable relationship is drawn in produced figure P and also has an omitted figure O, an honest reviewer cannot record both, and naming O passes.
  - The module doc defines the arm as "the one draft diagram it judged to draw that relationship", so a reviewer who names P gets a block, and naming O misstates the record rather than exposing a code defect.
  - Still, the arm means "draws it" for supported relationships and "records its omission" for undrawable ones. The doc could state that an undrawable relationship drawn in any produced figure must name that figure.
- **R2-N2: A prose-sufficient relationship may name a figure that doesn't exist.** A diagram-clearer relationship with a dangling `diagramId` blocks (`missing-diagram`), but the same name on a prose-sufficient relationship is silently accepted (probe D). It draws nothing, so nothing opens, but this may be better treated as a malformed record.
- **R2-N3: Relationship `sourceIds` are never resolved against anything.** They are shape-checked only (`refs`, min 1). Whether a relationship is supported rests on the reviewer's `support` value; the verdict does not check it against premises. That fits "the reviewer's enumeration and judgments are the input", but the doc could say so, just as it now does for rendered-account disclosure.
- **R2-N4: One spec condition is unchecked and not disclosed.** The "Partly supported diagram" scenario says "supported nodes drawn with none of the relationship's edges are not a produced diagram". The verdict trusts the figure's `produced` disposition for this. The N2 disclosure does not mention it.
- `528a525` also adds the review-1 raw as `docs/reviews/R-TREE-STYLE-POLARIS-RENDERED-1-RAW.md`. Its head matches the four-line form and the campaign partition counts it.

## Checks run

- `npx tsc -b packages/polaris-generation-core`: clean, exit 0.
- `npx vitest run packages/polaris-generation-core`: 8 files and 142 tests pass, 19 of them in `rendered-design.test.ts` (up from 140 and 17 at review 1).
- `python3 scripts/check_governance.py`: 32 OK, 20 WARN, 0 FAIL (52 checks).
- `python3 scripts/check_docs_review_campaign_partition.py`: total=267, assigned=267, raw=242, unmatched=0, overlaps=0.
- The probe script, run with node against `dist`, lives outside the worktree at `/tmp/claude-1000/-home-tze-GitHub-syzygy/42f1d844-9fb6-4091-8261-544ed369daaf/scratchpad/probe-rdr.mjs`. `git status` in the worktree is clean.
