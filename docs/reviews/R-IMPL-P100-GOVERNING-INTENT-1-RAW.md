# R-IMPL-P100-GOVERNING-INTENT-1 — implementation review of syzygy-u05.20
Verdict: REVISE
Reviewed commit: d966ff3e
Subject: /home/tze/.cache/syzygy-impl-lane/p100-review.diff

Reviewer: fresh-context implementation review (CC-REV-1), 2026-10-15.

Inputs checked:
- The subject diff hashes to sha256 9b51d897d03558cdc61d4e7829165221d2fd97b9a17d7706460564c7b6b8cde4.
- The signed-requirement extract hashes to 438b9eb9e10ed38733c6eb8bc39e584b3fe1c199733d9bd208bea7acae2abe9b.
- Both match the brief. The worktree HEAD is d966ff3ec2d6c3abded81f484f1b8227d2bc831c and the tree is clean.

What I ran (all [Observed]):
- The eight test files the evidence record names (`TMPDIR=/var/tmp/syzygy-impl-lane-tmp npx vitest run …`): 8 files, 121 passed, 0 failed. The browser test ran; it was not skipped. That matches the record's `testsRun: 121`.
- The full suites, `npx vitest run apps/three-surface-poc packages/three-surface-poc-core`: 119 files passed and 3 skipped; 1971 tests passed and 3 skipped. No regression elsewhere in the two projects.
- `npx tsc --noEmit -p packages/three-surface-poc-core`: no errors.
- I hashed the six files in the record's `subject.files` at HEAD. All six match the recorded digests. `git diff --stat 0d1cb92e d966ff3e` touches only the evidence JSON, so the mutants' `ranAt` commit carries the same code bytes as the reviewed commit.
- RFC2-24 row 10 (`rendering-vocabularies.md:139`) reads "Repair the observer/source; new snapshot". That is identical to the new `UNKNOWN_REASON_ROUTES` value and to the test literal `ROUTE`.

## Findings

1. **revise** — On Trajectory, the count is missing when the board is Unknown.
   - Anchors: `apps/three-surface-poc/src/trajectory.ts:217-223`, `apps/three-surface-poc/src/trajectory.ts:145-146` and `packages/three-surface-poc-core/src/model.ts:571,582,1104-1109`.
   - Behavior today: when no seeds are supplied, `trajectoryProjection` is `kind: 'unknown'`. `workItems` can still be `observed`, and then `observedItemCount` is set (model.ts:1109). In that state the machine answer still serves every item with `governedBy` and serves `governedByUnknownCount`.
   - The page takes the `trajectory.kind === 'unknown'` branch. That branch prints only "Independently observed work-item denominator: N". It shows no governing-intent count, reason, route or warrant statement. The region's machine twin is also added only under `input.trajectory.kind === 'observed'` (model.ts:571).
   - What the signed text requires:
     - Required behavior: "Both channels SHALL serve how many served items carry that Unknown, over the served item set."
     - Scope: "items outside that selection are counted on Trajectory, not rendered".
   - With no rendered selection, all N served items lie outside it. They must still be counted on Trajectory, as N with 0 inside and N outside, beside the reason, the route and the warrant statement. Today the human channel serves nothing for them, so the two channels diverge in that state.
   - Test gap: the sweep exercises only an observed board. The `no-seeds` denominator in `unknown-route-sweep.test.ts` stays at 2, consistent with no region being rendered. That is [Inferred] from the code above plus the unchanged figure; I did not render the no-seeds page.
   - Fix, either:
     - render the region in the unknown-board branch, with its twin added whenever `workItems` is observed, and add a no-seeds case to the sweep; or
     - have the coordinator record a reading that scopes the Trajectory arms to an observed board, and cite it in the evidence record's `readings`.

2. **note** — Live headroom is unmeasured in the admitted state.
   - Anchors: `docs/evidence/p100-governing-intent-implementation-2026-10-15.json`, `liveSize.fractionOfCeiling` and `liveSize.caveat` (lines 170-174 of the file).
   - The live figures: `/api/poc` grew by 2,535,681 bytes to 6,480,949, which is 0.7726 of the 8 MiB ceiling.
   - The record states honestly that both runs were `pwb-unobserved-not-admitted`. The admitted response adds the project-shape block on top, by an amount marked [Unknown].
   - A response-ceiling breach answers 503 and serves nothing, with no ledger trace. So a walkthrough in the admitted state could lose the whole machine answer with no other sign.
   - This is not a signed-text defect, and ruling (B) already trims the basis sentence. Before the change is relied on in an admitted walkthrough, the admitted `/api/poc` should be measured, or the project-shape block's size bounded from a retained capture.

3. **note** — A doc comment is detached in `packages/three-surface-poc-core/src/work-items.ts:61-69`.
   - The comment "How many items carry the governing-intent Unknown, counted over the served item set (POC-REQ-014), never assumed equal to its length" sits directly above the `governingIntentDisclosure` doc comment and function.
   - It is therefore separated from `countGoverningIntentUnknown`, the function it describes. Editors and TSDoc attach it to nothing, or to the wrong symbol. Move it down to `countGoverningIntentUnknown`.

4. **note** — No single run drives the real narrowing over a board with outside items.
   - Anchors: `apps/three-surface-poc/src/governing-intent-sweep.test.ts:69` (`narrowed`) and `apps/three-surface-poc/src/trajectory-narrowing.browser.test.ts:47-58`.
   - The oracle asks for the rendered items to be enumerated "before and after narrowing the board". Two tests split that work:
     - The sweep's "after narrowing" set is the checker's re-statement of the CSS rule as an attribute filter. It is not an enumeration of what the narrowing actually shows.
     - The Chrome test does drive the real toggle, but on the 5-item default fixture, where every item is rendered and none falls outside. It also never reads the region's inside figure.
   - Together they cover the limbs, and M17, M18 and M19 are killed. The browser test would be closer to the signed procedure if it ran on the 54-item fixture and asserted that the after-narrowing visible set's size equals the region's `governed-by-unknown-inside` figure.
   - Minor: the toggle is activated by a scripted `label.click()`, so keyboard operation (Space on the focused checkbox) is not exercised.

5. **note** — Column counts go stale while the board is narrowed.
   - Anchors: `apps/three-surface-poc/src/trajectory.ts:209` and `apps/three-surface-poc/src/trajectory.ts:238`.
   - The CSS-only narrowing hides cards. Each column heading's `(n)` count and the scope statement's "Rendering R of N" are static, and no live region announces the change.
   - Today this has no effect, because every card carries the Unknown and nothing is hidden. Once any item can be warranted, sighted and screen-reader users will read a count that no longer matches the visible cards.
   - The toggle itself is accessible: a native checkbox, a `for`-associated label with plain-language text, a `:focus-visible` outline on the label, and hidden cards removed from tab order by `display: none`. No finding against it.

6. **note** — The route change leaves a design doc stale and the route table mixed.
   - Anchors: `packages/three-surface-poc-core/src/project-shape-model.ts:99-103` and `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:588-594`.
   - I judge ruling (a) as stated and do not relitigate it.
   - The design doc lists `source-uncaptured-or-unreachable` ("observer/source" vs "observer or source") among the reasons whose implementation route differs from the RFC, and says "Every difference is …". That sentence is now false for this reason. The record names this hit (`readings.routeLiteral`) but the diff does not touch it.
   - The table now carries one RFC literal beside five retained paraphrases (`missing-evidence`, `no-currency-bound-declared`, `mapping-coverage-absent`, `challenge-suspended`, `execution-blocked`).
   - Mark or amend the doc sentence at the stale claim, and say in the code comment why only this route is literal: POC-REQ-014 pins it.

7. **note** — `unknownSubject` lookups grow quadratically with the rendered count.
   - Anchors: `apps/three-surface-poc/src/trajectory.ts:148-151` (the `governingIntentRegion` inside filter), `itemGoverningIntent`, and `itemCard`'s `governedBy` lookup.
   - Each rendered card adds three linear `model.unknownSubjects.find` scans, and the subject list itself grew by one entry per rendered card. That is O(R²) per render.
   - The live render succeeded, so this is not a defect today. A `Map` from id to subject, built once per render, would remove it.

## Coverage of the signed clauses (summary)

All items in this section are [Observed] unless marked otherwise.

- **Required behavior.** On an observed board:
  - every served item carries `governedBy` = {Unknown, `source-uncaptured-or-unreachable`, RFC2-24 route};
  - `governedByUnknownCount` is counted over the served set, not assumed;
  - Trajectory shows the count with inside/outside figures, the reason, the route and the warrant statement;
  - every card is marked with the POC-REQ-060 Unknown class;
  - a native toggle narrows the board.

  Nothing is taken from the title. The gap is the unknown-board state (finding 1).
- **Scope.** No new work-item column or field is read: the diff leaves the SQL in `work-items.ts` untouched. There is no new Butlers content class, read or provider egress, and the daemon executes no observed code. No edge is defined, and nothing is claimed about orphaned work.
- **Oracle and independence.**
  - Both denominators are the checker's own enumerations: served items read from the parsed answer, and cards parsed from the page.
  - The reason and route are typed literals that match RFC2-24 row 10.
  - The expected encoding is pinned to `EPISTEMIC_ENCODING`. The one import from the module under test is the one the signed oracle names, and the test also asserts the table's Unknown row equals the literal class.
  - The fixture title is the checker's own, supplied through an injected work-item read.
  - `countGoverningIntentUnknown` and `governingIntentUnknown` are imported from core. Their use builds counterexample inputs; no expected value is derived from them.
- **Falsifier.** Each limb has a predicate-level counterexample in the sweep: 7 answer cases and 12 page cases. Each limb also has a recorded rule-6 mutant with old/new fragments and `ranAt`:

  | Limb | Mutant(s) |
  |---|---|
  | guessed from title | M01 |
  | green | M02 |
  | omitted | M03 (killed via a thrown build, disclosed) |
  | miscount | M04, M05, M09 |
  | inside/outside | M10, M11 |
  | missing reason | M06, M12 |
  | missing or wrong route | M07, M08, M13 |
  | missing resolution statement | M14 |
  | encoding | M15, M16 |
  | narrowing | M17, M18, M19 |

  In all: 19 killed, and M00, the unmutated baseline, survived.
- **Scenarios.** "Every item's governing intent is Unknown" holds on the 54/52/2 fixture. "A title names a requirement" holds: `bu-titled` carries the same Unknown, and POC-REQ-010 appears in the answer only under `.title` paths.

## Summary

The implementation matches POC-REQ-014 on an observed board. The tests are rigorous, use literal expectations, and are backed by a complete and re-checkable rule-6 record whose digests match the reviewed bytes. One clause is not met: when the board is Unknown (no seeds) but work items are observed, the machine channel serves the governing-intent count and Trajectory serves none (finding 1). That is the one revise finding. The six notes are non-blocking: admitted-state size headroom, a misplaced doc comment, the split between the narrowing tests, column counts that go stale under narrowing, a stale design-doc sentence after ruling (a), and quadratic subject lookups.

Revise: 1. Notes: 6.
