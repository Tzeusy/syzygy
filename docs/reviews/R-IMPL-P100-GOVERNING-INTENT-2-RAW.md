# R-IMPL-P100-GOVERNING-INTENT-2 — implementation review of syzygy-u05.20 (round 2)
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: abda604d
Subject: /home/tze/.cache/syzygy-impl-lane/p100-review-2.diff

Reviewer: fresh-context implementation confirmation review (CC-REV-1), round 2, 2026-10-15.

## Inputs checked

All items here are [Observed].

- These four files hash to the digests in the brief:
  - the subject diff, `p100-review-2.diff`: 33f383827e97cbe4524475059522ab4eb5b8da0a247455e533b81c02e1fd3191;
  - the repair diff, `p100-repair.diff`: 8f6690da3dd12293068fb7c158d3242f2404db64cc77c28cb6ef3be8a1e3e510;
  - the round-1 raw: 70a34ed17aeb7793b55ac7b54fb69f3feb62bf0cf315c22512d06fe9d9d87b93;
  - the signed-requirement extract: 438b9eb9e10ed38733c6eb8bc39e584b3fe1c199733d9bd208bea7acae2abe9b.
- The worktree HEAD is abda604dc37b0852a12545e372248079653397ba, and the tree is clean.
- `git diff --stat eec027b7 abda604d` touches only `docs/README.md` and the evidence JSON. So the mutants' `ranAt` commit, eec027b7, carries the same code bytes as the reviewed commit.
- I hashed the seven files in the evidence record's `subject.files` at HEAD. All seven match the recorded digests.

## What I ran

All items here are [Observed].

- The nine test files the evidence record names in `rule6Mutants.tests`:
  - Command: `TMPDIR=/var/tmp/syzygy-impl-lane-tmp npx vitest run …`.
  - Result: 9 files and 136 tests passed, none failed. That equals the record's `testsRun: 136`.
  - The browser test file ran both of its tests. It was not skipped.
- The full suites, `npx vitest run apps/three-surface-poc packages/three-surface-poc-core`:
  - 119 files passed and 3 skipped; 1973 tests passed and 3 skipped.
  - Round 1 counted 1971 tests. The difference is exactly the two new tests.
- `npx tsc --noEmit -p packages/three-surface-poc-core`: no errors.
- `python3 scripts/check_docs_review_campaign_partition.py`: total=442, assigned=442, unmatched=0, overlaps=0. That agrees with the count sentence in `docs/README.md`.

## Round-1 findings: resolution

### Finding 1 (revise): resolved

The finding was an Unknown Trajectory board beside observed work items. I checked the author's answer against the model builder, independently of the new test. Both statements below are [Observed] in code.

- **No seeds.** `packages/three-surface-poc-core/src/model.ts:1025-1030` sets `workItems` to `kind: 'unknown'` ("No seed-backed work-item prefix was supplied…") whenever `seeds === undefined`. The trajectory branch at `model.ts:1104-1110` is taken under that same condition. So the conditional spread `workItems.kind === 'observed' ? { observedItemCount … }` at `model.ts:1109` can never fire at runtime. Round 1 read that spread as reachable; it is not.
- **With seeds.** `projectTrajectory` (`trajectory-projection.ts:72-78`) returns `kind: 'unknown'` only when `workItems.kind === 'unknown'`. Every other path returns `kind: 'observed'`.

So in `buildPocModel`, an Unknown board implies an Unknown work-item read. An Unknown read has no served item set. The signed text, "Both channels SHALL serve how many served items carry that Unknown, over the served item set", then has nothing to count on either channel. The channels agree:

- the machine answer serves no `governedBy` and no count;
- the page serves the `region:work-items` Unknown disclosure.

The new test (`apps/three-surface-poc/src/governing-intent-sweep.test.ts:240-256`) builds both Unknown-board states: no seeds, and seeds with an unreachable Dolt. For each state it asserts four things:
- both kinds are Unknown;
- no `governedBy` leaf appears anywhere in the served JSON;
- no count region is rendered;
- the work-items Unknown disclosure is present.

It also guards against regression. If a future change let the no-seeds build observe work items, the first soft assertion would fail.

The answer is therefore correct, and with the test it is sufficient. The state round 1 described is unreachable through the served model. The residual is that the type still admits that state; see finding 4 below.

### Notes 3, 4, 6 and 7

- **Note 3: resolved.** The doc comment now sits directly above `countGoverningIntentUnknown` (`packages/three-surface-poc-core/src/work-items.ts:68-70`).
- **Note 4: resolved.** The new browser test (`apps/three-surface-poc/src/trajectory-narrowing.browser.test.ts:64-96`) runs on a 54-item board.
  - Before narrowing, 52 cards render, with figures 54 / 52 / 2.
  - It focuses the native checkbox and presses Space, a real CDP key event (the `cdp-browser.ts` `Space` key spec). It asserts the box is checked.
  - It then asserts that the visible set after narrowing equals the set before, and that its size equals the region's rendered inside figure.
  - So a single run drives the real narrowing over a board with outside items, and keyboard operation is now exercised.
- **Note 6: partly resolved.** The code comment now says why only this route is literal (`packages/three-surface-poc-core/src/project-shape-model.ts:99-100`). The stale design-doc sentence is untouched; see finding 1 below.
- **Note 7: partly resolved.** `governingIntentRegion` now builds a `Map` once per render (`apps/three-surface-poc/src/trajectory.ts:148-151`). `itemCard` now does one lookup where it did two, and passes the subject to `itemGoverningIntent`. The O(R²) term remains; see finding 2 below.

### Notes 2 and 5 (left for the PR)

I accept the reasons given:
- Note 2, admitted-state size: blocked on a recording tag outside this change. The evidence record re-measured the non-admitted live sizes at eec027b7: `/api/poc` 6,480,955 bytes, 0.7726 of the ceiling. The admitted state is still [Unknown].
- Note 5, column counts: no effect while every item is Unknown.

Neither is a signed-text defect.

## Findings

1. **note** — Round-1 note 6 is recorded as taken, but its design-doc half was not done.
   - Anchors: `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:584-596`, `docs/README.md:147` and the record's `readings.routeLiteral`.
   - The design doc still counts "**7** differ", and still lists `source-uncaptured-or-unreachable` ("observer/source" vs "observer or source") among the routes that differ from the RFC. That has been false since ruling (a) made the value literal, so the count is now 6.
   - `docs/README.md:147` says "notes 3, 4, 6 and 7 are taken in `eec027b7`", which overstates note 6.
   - Fix: mark the stale sentence in place and date it, keeping the superseded text, per the repository's "mark staleness at the stale sentence" practice. Or have the README row say that note 6 was taken in part.

2. **note** — Round-1 note 7 is reduced, not removed.
   - Anchors: `apps/three-surface-poc/src/trajectory.ts:173` (`itemCard`) and `:129` (`itemVerification`).
   - Each rendered card still makes linear `unknownSubjects.find` scans, and the subject list still grows by one entry per rendered card. The constant fell; the order is still O(R²).
   - This is not a defect at today's sizes: the live render returned 200. Passing the per-render `Map` down to `itemCard` would finish the repair.

3. **note** — The review-campaign row joins two entries without a separator.
   - Anchor: `docs/README.md:147`.
   - The P-100 entry was appended directly after "note 5 needs no change" from the P-97 entry ("…needs no change P-100 (`syzygy-u05.20`) round 1 …"). That reads as one run-on sentence. A period or semicolon between the two entries fixes it.
   - The partition count is correct: 442 / 442, as re-derived above.

4. **note** — The unreachable state is still typed and still rendered.
   - Anchors: `packages/three-surface-poc-core/src/trajectory-projection.ts:40-41` (`observedItemCount?`), `packages/three-surface-poc-core/src/model.ts:1109` and `apps/three-surface-poc/src/trajectory.ts:217-223`.
   - `TrajectoryProjectionUnknown.observedItemCount` and the dead conditional spread still describe an Unknown board beside observed items. The renderer still has a branch for that state, and the branch prints no governing-intent count.
   - The new test pins the builder so the state cannot be produced. But a future builder change that made it reachable would bring back exactly the round-1 divergence. Only the first soft assertion of the new test would catch it, not a check on the region.
   - Fix: remove the dead field and branch, or file a bead. Neither is required by the signed text.

5. **note** — The M03 entry in the evidence record attributes a kill to a test that cannot observe the mutant.
   - Anchor: `docs/evidence/p100-governing-intent-implementation-2026-10-15.json`, M03 `killedBy`.
   - The entry lists `cdp-browser.test.ts > disposable browser shutdown waits for private Chrome group members…`.
   - That file imports only `cdp-browser.js` (`apps/three-surface-poc/src/cdp-browser.test.ts:1-3`). It never builds a model, so it cannot see a missing `governedBy`. The failure was most likely timing under the mutation run [Inferred].
   - M03's outcome is unaffected, since 31 other listed tests failed. But a `killedBy` list is evidence other readers will re-check. Note the entry as incidental, or re-run M03 alone.

## Acceptance criteria

All items in this section are [Observed] unless marked otherwise.

1. **The oracle passes over both denominators: met.**
   - The served item set is enumerated from the parsed answer.
   - The rendered items are enumerated before and after narrowing, both in the sweep and, since this round, in Chrome on a board with outside items.
   - Inside equals the enumeration (52), and inside plus outside equals the served count (52 + 2 = 54).
2. **The Trajectory arms are decided as signed: met.**
   - The encoding is the `EPISTEMIC_ENCODING` Unknown class, and M15 kills the alternative.
   - The count region, read as text, holds the reason, the RFC2-24 literal "Repair the observer/source; new snapshot" and the warrant statement. M12, M13 and M14 kill the omissions.
   - The narrowed board lists exactly the rendered items.
   - The Unknown-board state is unreachable (round-1 finding 1, above).
3. **Rule-6 mutants: met.**
   - Each falsifier limb has a killed mutant. The baseline M00 survived, and 19 of 19 mutants were killed at `ranAt` eec027b7.
   - Old/new fragments are recorded, and M16's and M19's `old` fragments were updated to the repaired bytes.
   - See finding 5 for one incidental `killedBy` entry.
4. **Exactly the signed text: met.**
   - The repair adds no read, column, field, content class or egress. The `bd` SQL is unchanged.
   - `cdp-browser.ts` gains a test-harness key only.
   - No observed code is executed.
5. **Literal expected values: met.**
   - The new tests use literal 52 / 54 / 2 figures and literal kinds.
   - The one value read from the page is the inside figure, and only after it has been asserted equal to the literal `'52'`.

## Rulings (a) and (B), judged as stated

- **Ruling (a).** The route is RFC2-24's literal, and the code comment now says why only this row is literal. The stale design-doc count is finding 1.
- **Ruling (B).** It is unchanged by the repair. The served `governedBy` carries no basis sentence, and the card twin keeps it through `governingIntentDisclosure` (`work-items.ts:63-66`).

## Summary

Round-1 finding 1 is resolved. Its premise is unreachable in `buildPocModel`, as the code at `model.ts:1025-1030` and `trajectory-projection.ts:77` shows, and a regression test now pins that. Notes 3 and 4 are resolved, and notes 6 and 7 are resolved in part. The suites pass at the reviewed commit (136/136 named, 1973 overall), and the evidence record's digests match. The five remaining items are notes. None is a revise finding.

Revise: 0. Notes: 5.
