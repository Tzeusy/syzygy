Title: Rendered-design review verdict (syzygy-73e.10) — code review 1
Verdict: REVISE
Reviewed: bb76bae
Reviewer: independent fresh-context agent

## Material findings

**M1 — Fail-open: a prose-sufficient relationship skips every drawing rule, so an unsupported relationship can be drawn in a produced diagram and still pass.** (`packages/polaris-generation-core/src/rendered-design.ts:95`, `:128`)

- **The cause.** `relationshipRule` returns `null` for `judgment === 'prose-sufficient'` before it looks at `support` or `diagram`. The `claims` count at `:128` also only includes `diagram-clearer` relationships.
- **Why it matters.** The judgment only decides whether a diagram is *required*. The spec forbids drawing an unsupported element whatever the judgment: REQ-polaris-generation-004 says "an unsupported element is never drawn but disclosed as a gap", and the "Partly supported diagram" scenario says "an unsupported element is never drawn, whether marked Inferred, Unknown or not at all". The schema lets a prose-sufficient relationship name a diagram, and the spec lets one be drawn "on another basis". So the record can say "this relationship is unsupported and figure X draws it", and the verdict ignores that.
- **Inputs I ran, each against a valid draft with the correct digest.** All three returned `blocking: false`:
  1. `relationships: [{ judgment: 'prose-sufficient', support: 'unsupported', diagram: { kind: 'named', diagramId: 'deps' /* produced */ }, gaps: [] , …}]`. Expected `unsupported-relationship-drawn`.
  2. `[rel('r1') /* diagram-clearer, supported, names deps */, { judgment: 'prose-sufficient', support: 'unsupported', diagram: named deps }]`. Expected a block: the produced figure draws an unsupported relationship.
  3. `{ judgment: 'prose-sufficient', support: 'partly-supported', diagram: named deps, gaps: [] }`. The drawn figure has no disclosed gap. Expected `undisclosed-gap`.
- **Suggested repair.** Apply `unsupported-relationship-drawn` and `undisclosed-gap` to any relationship that names a produced diagram, whatever its judgment. Keep the `missing-diagram`, `diagram-not-produced` and `undrawable-without-recorded-omission` requirements for diagram-clearer relationships only. Add tests for inputs 1–3.

## Notes (non-blocking)

- **N1 — Folding "undrawable" into `support: 'unsupported'`.** This is a reasonable encoding. The spec defines drawable as admitted premises supporting at least one edge, so partly-supported means drawable and unsupported means undrawable. The type comment says so, and the record does "name whether each enumerated relationship was drawable" through the `support` enum. Consider saying this in the module doc as well.
- **N2 — "Recorded omission" is only partly checked.** For an undrawable relationship, the verdict accepts any named draft diagram with an `omitted` disposition. It does not check the spec's other conditions: that "its gap is disclosed in the rendered account at the depth it affects", or the "unless the request … require[s] that visual" basis. `requestedAssets` is not an input. That is defensible for Phase A, since required-asset omission is enforced in `validateStage`, but the module doc should say it is out of scope. Otherwise `blocking: false` there reads as the full scenario.
- **N3 — Binding by `draftDigest`.** Canonical-JSON sha256 over the validated draft is sound, and the retired review blocks as REQ-006 needs. I recomputed the pinned `DRAFT_DIGEST` independently in Python (`json.dumps(sort_keys=True, separators=(',',':'))`) and got the same value, `ddefc70c…`. Retirement is evaluated after validation, so a malformed retired record still throws, which is correct polarity.
- **N4 — `validateDraftRecord` is lighter than it may look.** It does not check `diagram.sectionId`/`deepDive.sectionId` against sections. A draft with a dangling `sectionId` validated and got a digest in my probe. The docstring discloses that it "never substitutes" for stage validation, so this is acceptable, but a verdict can be computed over a draft that `validateStage` would reject.
- **N5 — Ambiguous finding targets.** Relationship ids share the target namespace with section and diagram ids, and nothing stops a relationship id from equalling a section id. That makes a reviewer finding's target ambiguous. Minor.
- **N6 — One untested branch.** No test covers the `judgment === 'diagram-clearer'` filter in the claims count. For example, a diagram-clearer and a prose-sufficient relationship naming the same diagram should not count as shared. Removing the filter would survive the suite. After M1's repair, decide deliberately whether a prose-sufficient claim should count toward sharing.
- **N7 — Other fail-open paths I tried, all of which hold:**
  - a missing, null, extra-field or wrong-enum record throws;
  - duplicate relationship ids throw;
  - gaps on a relationship that is not partly supported throw;
  - an unknown finding target throws;
  - a nonexistent `diagramId` blocks (`missing-diagram` or `undrawable-without-recorded-omission`);
  - an unresolved or omitted figure for a supported relationship blocks;
  - a diagram shared between two diagram-clearer relationships blocks both, including two undrawable relationships sharing one omission;
  - extra produced figures do not stand in;
  - reviewer advisory findings never clear anything, and blocking ones add.

## provider-draft.ts refactor

The change adds code only. `check`, the schemas and `validateStage` are byte-unchanged, so existing validation behaves the same. The new exports (`ClosedSchema`, `checkClosedSchema`, `schemaParts`, `validateDraftRecord`) are module-level but not re-exported from `index.ts`. `package.json` `exports` exposes only `"."`, so the package's public API grows only by `renderedDesignVerdict`, `renderedDesignSubjectDigest` and their types. `validateDraftRecord` repeats the edge/node check from `validateStage`, which is acceptable duplication.

## Test quality

- Expected values are hard-coded literals, and the digest is pinned from an external computation.
- Fixtures are plain constants, with no describe-time throws.
- Each rule has a test that fails if that rule is removed. The shared-diagram, not-produced, undrawable and undisclosed-gap tests all assert exact `[id, rule]` pairs.
- The retired test uses a relationship that would not otherwise block, so it isolates the digest check.
- Gaps: M1's inputs are untested, and so is the N6 branch.

## Checks run

- `npx tsc -b packages/polaris-generation-core && npx vitest run packages/polaris-generation-core`: builds clean; 8 files and 140 tests pass, 17 of them in `rendered-design.test.ts`.
- A temporary probe test for M1 inputs 1–3 and N4. I deleted it afterwards, and `git status` was clean.
- A Python recomputation of the pinned fixture digest, which matched.
