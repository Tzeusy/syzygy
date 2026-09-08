# Existing Orrery height encoding — independent raw finding

Verdict: CONFIRM FINDING (bounded synthetic POC evidence).

[Observed] Inspected both retained screenshots visually, browser JSON, fixture HTML data island and current orrery.ts. No code edits or external project reads performed. No independent live DOM measurement is claimed; browser JSON reports viewport/scroll dimensions but not per-block rectangles.

## Frozen evidence

- `apps/three-surface-poc/src/orrery.ts` — `8e96af68029148938b070eb2817ded28e881ceb976bf637e9611f0bcfdac3d4d`
- `docs/evidence/polaris-existing-orrery-fixture-2026-09-09.html` — `792eace9aec7b296132791744065276e4e1ff388141f35c332ffa61366665cab`
- `docs/evidence/polaris-existing-orrery-browser-2026-09-09.json` — `786a871dbd7f9e283379cbd6a9d5956e410c8263fe2362fd3a77cd11976fdd97`
- `docs/evidence/polaris-existing-orrery-wide-2026-09-09.png` — `3db157c75f25311d1d4735460e5eacc1e89e7205ee4663933bcfa6489985cbc6`
- `docs/evidence/polaris-existing-orrery-narrow-2026-09-09.png` — `a90a1bb18ee22a38191ee96eaee7a920229e0ee6d3ae82df00e34b476af18047`

## Height finding

[Observed] The wide screenshot displays the six directory blocks with equal top and bottom boundaries despite different data. Independently extracted fixture data yields (directory, bytes, prescribed minimum rem): root 15/3.56, apps 26/3.96, docs 45/4.67, openspec 162/9.00, src 31/4.15, tests 26/3.96. The CSS grid has no vertical item alignment override, and blocks use min-height rather than a fixed height. The mapped and unmapped tiles also stretch to the same visible row height.

[Inferred] Grid cross-axis stretch makes every auto-sized item fill its row track, which is sized by the tallest minimum. Thus unequal --block-height minima do not produce unequal visible district heights within a row. The narrow screenshot is consistent with row-relative equalization rather than an independent encoded height.

[Observed] There is a second, separate semantic defect in the height description: the formula is 3 + 6 * bytes / largestBytes, while the legend calls the entire block height proportional. The additive 3rem baseline makes full height affine, not proportional; repairing stretch alone does not make that description correct.

## Bounded suggested repair

[Inferred] Bottom-align the grid items (align-items: end or equivalent item alignment) so their individual minima are not stretched across a row. Keep a readable baseline and revise the legend to describe the fixed baseline plus size-scaled increment; do not imply full-height ratios equal byte ratios. Make mapped/unmapped reference tiles explicitly unmeasured by this encoding. Verify actual browser rectangles for a same-row fixture with deliberately unequal bytes, plus the stated formula and narrow wrapping. This is a repair to the existing POC encoding, not implementation of a reusable computed-asset renderer or RFC9 conformance.

[Unknown] Content height can exceed a minimum for long labels; a min-height encoding must either disclose its readability floor or use a separate measured glyph if exact ratios are desired. The bounded repair should test a long label before claiming the encoded height follows the formula exactly.

## Separate narrow overflow observation

[Observed] At nominal 390px width the browser JSON reports document scrollWidth 404px. The narrow screenshot shows a page-level horizontal scrollbar as well as a separately scrolling navigation row. This confirms overflow in that retained fixture; it does not identify the responsible element. Keep it as a separate finding and do not expand the height repair without diagnosis/scope selection.

## Limits

[Unknown] No live Butlers state, production health, whole-page accessibility, broad layout correctness or generalized renderer conformance was evaluated. Frozen artifact evidence only; later changes require fresh browser validation.
