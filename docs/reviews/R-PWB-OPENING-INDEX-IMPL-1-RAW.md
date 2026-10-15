# R-PWB-OPENING-INDEX-IMPL-1 — code review, syzygy-u05.23
Reviewed commit: 1afdb082d1bbbb88b4994c25b5f34ce1cf5b97a0
Scope: diff origin/main...1afdb082d1bbbb88b4994c25b5f34ce1cf5b97a0 against pwb-opening-index-amendment v1.0 (PWB-REQ-010)
Verdict: REVISE

## Basis

- [Observed] Worktree HEAD is `1afdb082d1bbbb88b4994c25b5f34ce1cf5b97a0` and the tree is clean. The review diff hashes to `04bfe0764077483e5de909c5648c25d706102e7c925d5467da4ab13a160a0529`, which matches the brief. It touches 11 files: 8 under `apps/three-surface-poc/src/` and 3 under `docs/evidence/`. It touches nothing under `packages/`, so there is no shared-model or PocModel change, no new reader and no new egress path.
- Read: the signed patch (PWB-REQ-010 amendment v1.0), the owner answers Q2–Q12 as given in the brief, the whole diff, and the touched files at HEAD for context (`polaris.ts` around the body assembly, outline builder, `SECTION_NAV_SCRIPT`, `accountByKey`, `claimStatesBlock`; `polaris-copy.ts`; `polaris-copy.test.ts`). I also read `cdp-browser.ts` and `polaris-accessibility-variants.ts`, which the oracle imports, for their interfaces only.
- Ran: `npx vitest run` over the oracle file and the four touched test files: 5 files, 47 passed, 1 skipped (the `SYZYGY_P98_PAGE` capture test, skipped because the variable was unset). The oracle's printed reports are byte-identical in content to the fixture and synthetic reports in `pwb-p98-opening-index-oracle-2026-10-15.json`. I also ran the full `apps/three-surface-poc` suite: 86 files passed, 1 skipped; 1037 tests passed, 2 skipped.
- Ran one read-only browser probe from the scratchpad (vite-node with the repository's own `cdp-browser.ts`). It renders the `observed` variant at 1280x900, focuses the index's `exact requirements` row, presses Enter and then Tab. The result is in finding 1.
- I did not run mutation scripts. The mutation record was checked for limb coverage and for its stored `old`/`new` fragments and commit. Its outcomes were not re-run.
- I read no Butlers content.

What the diff gets right, checked against the signed text [Observed]:
- **Rows.** The nine names, their order and their identities match the table character for character (`polaris-copy.ts` index.* rows). Expected values in the oracle are typed literals (`SIGNED_ROWS`, `RECOGNIZER`), never imported from the module under test.
- **Recognizer.** It is published in the test file before the run. It keys only on exact visible heading text and on the exact-source route form, never on the `id`s the renderer uses. It is then compared element-for-element with the row's routed element (`routed !== target`).
- **Word counter.** It shares no code with the renderer's script: a recursive walk with an inherited flag, against the renderer's TreeWalker with an ancestor check. The exclusions match the signed list: `script`/`style`/`template`/`noscript`, `hidden`, `aria-hidden="true"`, computed `display: none`, parent `visibility`, closed-details content except its own `summary`, and the index and line themselves.
- **Stopping-line placement.** The outermost qualifying ancestor, the tie broken toward the later target, and the no-target case placing the line after the index with only the total all match the signed text.
- **Viewport.** It is declared and published per report (Q10).
- **No claim markup.** The index carries no claim, parity or tuple markup. The narrative-tree tests exclude the index from PWB-REQ-014 units (Q5).
- **Signed cases.** All five are exercised:
  - every target renders: `observed-degraded-unlawful`;
  - aggregate absent: `observed`;
  - tie: synthetic, hand-counted;
  - setter inside a closed details: both observed variants;
  - no target renders: synthetic.
- **Rule-6 mutants.** There are 28, covering every falsifier limb the brief lists. Each stores its `old`/`new` fragments and the commit `0883ecfa`. The only later change to the oracle file, in `4ba447e5`, adds the env-gated capture test.

## Findings

1. **revise** — `apps/three-surface-poc/src/polaris-first-reading.test.ts:291-303`; `apps/three-surface-poc/src/polaris-opening-index.ts:64,90-95`. The `exact requirements` row routes to a link inside a disclosure that is closed on load. A keyboard reader who follows that row cannot Tab to the target.
   - [Observed] Probe on the `observed` variant at 1280x900: the row link was focused (`exact requirements`) and Enter pressed. Chrome auto-expanded the enclosing details (`detailsOpen: true`, hash `#polaris-first-exact-requirement`, target at top 81px). The next Tab then landed on a `summary` reading "Sources — craft-policy". That summary follows the target but lies outside the target's own details: `isTarget: false`, `insideSameDetails: false`. So sequential focus skips the very link the row routed to, along with the rest of that opened population. This is the stranding the project's guardrail about fragment targets inside `<details>` records.
   - [Observed] The narrowed existing test calls this "One signed exception". The signed text fixes the target ("the first link, in document order, to an exact requirement's text"). It states no exception to the invariant that no fragment target sits inside a disclosure. That invariant is the one the test's own describe block attributes to PWB-REQ-011 as amended.
   - [Inferred] The conflict between the two requirements has been settled by editing a test rather than by disclosure. The keyboard outcome is not tested anywhere.
   - Repair, within the signed text: make the row's activation land focus on the target. For example, focus the routed link after the browser's auto-expand. The row keeps its href and target, so the routing is unchanged. Add a browser test that follows the row with Enter and asserts the focus that results. Reword the test comment so it does not cite a signed exception, and record the cross-requirement tension in the bead or PR for the owner.

2. **note** — `apps/three-surface-poc/src/polaris.ts:409-412`; `apps/three-surface-poc/src/polaris-copy.ts:30`; `polaris-reachability.test.ts` (65 → 66); `polaris-copy.test.ts` (150 → 159). The diff adds a new visible `h3` "What the claim states mean" (copy row `states.heading`, role `epistemic-disclosure`) and a wrapper `div` around the claim-state legend. The outline builder then adds a new link to that heading.
   - [Observed] The signed text does not mention this change.
   - [Inferred] It is an enabling change. The signed rule routes to "the target's heading when it has one", and the oracle-independence limb lets the recognizer key only on visible heading text, so without a heading the legend could not be recognized independently. The test-count changes follow from it and are each explained in their comments.
   - [Observed] The heading now sits directly above a summary that reads "What the claim states mean — definitions", so the same phrase is shown twice in a row.
   - Disclose this as a render change outside the amendment's literal text, in the PR or bead.

3. **note** — `apps/three-surface-poc/src/polaris-opening-index.browser.test.ts:129,176,179-180`. The oracle's stopping-line predicate is looser than the signed "its numbers and their unit, and nothing else". It admits `/ · , . : ; – — -` in any amount.
   - [Observed] The rendered line is "N / M words". The "/" is defensible as a separator, but "1199 – 3500 words" would pass as well.
   - [Inferred] Because any word disqualifies an element from being a "line", the verdict-word check over `lines` (lines 179-180) can never fire on a line. A verdict in the line is caught only as `line-count` = 0. The `line-extra-text` mutant is killed that way, so the falsifier is still enforced, but through a different limb.
   - [Observed] The claim, parity and tuple markup check (line 176) inspects the index only, never the stopping line.

4. **note** — `apps/three-surface-poc/src/polaris-opening-index.ts:121,170,186`. Several strings are hard-coded and do not come from `POLARIS_COPY`:
   - the offset words "after … words";
   - the line's " / " and " words";
   - the `aria-label="Opening index"`.
   - [Observed] The script writes the offsets and the line after load, so the PWB-REQ-012 copy tests, which scan the served HTML, never see their text. The signed text requires that "All of them obey PWB-REQ-012".
   - [Inferred] They obey it in substance: the roles are correct and nothing prohibited appears. But no mechanical check covers them.

5. **note** — `docs/evidence/pwb-p98-polaris-size-measurement-2026-10-15.json` (`addedBytes`).
   - [Observed] The itemized additions sum to 1,779 + 2,674 + 423 + 224 = 5,100 bytes. The measured delta against the P-99 record is 119,009 − 113,689 = 5,320 bytes direct, and the same 5,320 on the tailnet form. That leaves 220 bytes unitemized; the outline link and the inserted `id` attribute are the likely source [Inferred].
   - [Observed] The page is 1.89 MB under the 2 MB ceiling, and the record discloses that the observed-shape headroom is Inferred.
   - [Unknown] Whether the P-99 baseline was taken at the same Butlers revision. I did not read that record, since it is outside this review's inputs.

6. **note** — `apps/three-surface-poc/src/polaris-opening-index.browser.test.ts:257-268,497-523`. The tie case and the no-target case run on synthetic bodies under the renderer's real index and script, with the first-reading-level check turned off.
   - [Inferred] No `renderPolarisPage` output can produce the no-target case, because the claim-state legend always renders. The synthetic route is therefore the only way to exercise it, and that is acceptable. Say so in the evidence record's `casesSigned` entry, which currently says "synthetic body, hand-counted" without the reason.

7. **note** — `apps/three-surface-poc/src/polaris-opening-index.ts:140-188`.
   - [Observed] Offsets and the stopping line exist only after the script runs. With scripting off, rendered rows show no offset and there is no line. Q10 ("the page counts its own words after load") implies an in-page count, so this follows from the owner's answer, but it is worth stating in the evidence.
   - [Inferred] `counted` calls `getComputedStyle` for each ancestor of each text node. On the roughly 1.47 MB observed Butlers page this may add noticeable load-time work.
   - [Unknown] That cost was not measured, because the live shape is not-admitted.

8. **note** — `apps/three-surface-poc/src/polaris.ts` (`SECTION_NAV_SCRIPT`); `polaris-opening-index.ts:143`.
   - [Observed] The `closed` set is captured at `load`. Before that point, `SECTION_NAV_SCRIPT` opens the outline drawer according to viewport width, which is why the wide and narrow totals differ. At `DOMContentLoaded` it also opens a component guide named by the URL hash.
   - [Inferred] Chrome's auto-expand on fragment navigation can open a disclosure before `load` when the page is loaded with a hash. The "first-load state" then depends on the URL fragment, and a page loaded with a fragment shows different offsets from one loaded without. The signed text does not settle whether that counts as the first-load state.
   - [Unknown] The oracle never loads with a fragment, so this case is not exercised.

Count: 8 findings — 0 blocking, 1 revise, 7 note.
