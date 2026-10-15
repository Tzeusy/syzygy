# R-PWB-OPENING-INDEX-IMPL-2 — code review, syzygy-u05.23
Reviewed commit: 0115086fc4111987ad004e7efc479de76692b1f4
Scope: diff origin/main...0115086fc4111987ad004e7efc479de76692b1f4 against pwb-opening-index-amendment v1.0 (PWB-REQ-010), round 2
Verdict: CONFIRM WITH EXCEPTIONS

## Basis

- [Observed] Worktree HEAD is `0115086fc4111987ad004e7efc479de76692b1f4`, tree clean. The review diff hashes to `120454947f0d8302fa4a05ce5a70e94369976b5ca5bc910ee64a3f67f6f75671`, matching the brief.
- Read: the signed patch, the owner answers Q2–Q12 as given in the brief, the acceptance criteria, the round-1 raw (`docs/reviews/R-PWB-OPENING-INDEX-IMPL-1-RAW.md`), the implementer's dispositions, and `git diff 1afdb082 HEAD` in full (apps and evidence). For context I also read `polaris-opening-index.ts` at HEAD in full, `polaris-first-reading.test.ts` lines 280-310, and `syntheticPage` and the tie body in the oracle file.
- [Observed] `git diff --stat 0883ecfa 89b96979 -- apps/` lists only `polaris-first-reading.test.ts` and `polaris-opening-index.browser.test.ts`. No renderer, shell or copy file changed after 0883ecfa. So the bytes served for the size measurement and the live capture (both at 0883ecfa) are the renderer bytes at HEAD. 89b96979 → 0115086f touches only `docs/evidence/`.
- [Observed] The diff still touches nothing under `packages/`: no PocModel or shared-model change, no new reader, no new egress.
- Ran `npx vitest run` on `polaris-opening-index.browser.test.ts` and `polaris-first-reading.test.ts`: 2 files, 27 passed, 1 skipped (the `SYZYGY_P98_PAGE` capture test, because the variable was unset). The 8 printed fixture and synthetic reports carry `violations: []`. Both new keyboard tests passed.
- I did not run the mutation script. I read no Butlers content.

## Findings

1. **note (round-1 finding 1, resolved by evidence)**: `apps/three-surface-poc/src/polaris-opening-index.browser.test.ts:373-413`; `polaris-first-reading.test.ts:290-309`.
   - [Observed] The new `followExactRow` test asserts, on the `observed` fixture, that after Enter on the row:
     - `document.activeElement === target`;
     - the target's disclosure is open;
     - the next Tab lands on the first visible focusable that follows the target in document order.
     The synthetic case (`nextInside: true`) puts a focusable *before* the target inside the same disclosure and one *after* it. Tab reaches the one after, so Chrome did not restart sequential focus at the details' first focusable. That restart is the stranding the project guardrail records.
   - [Inferred] The round-1 probe saw Tab land on "Sources — craft-policy" outside the target's details. This test shows that is the correct continuation: focus was already on the target, and in the fixture nothing focusable follows it inside its disclosure (`nextInside: false`). The round-1 claim that the routed link and "the rest of that opened population" were skipped does not hold. The revise finding is resolved.
   - [Observed] Dropping the focus handler is sound: per the disposition its three mutants survived, so it added nothing the browser does not already do.
   - [Observed] The narrowed invariant test now exempts only the exact-requirement row's id from the index-target check. The comment no longer claims a signed exception and says the tension is disclosed to the owner.
   - [Inferred] The keyboard tests characterize Chrome over the renderer's output. They hold only while the target stays a focusable `<a>`, and the evidence record says so (`keyboard`).

2. **note**: promised disclosures are not yet recorded anywhere I could observe.
   - Dispositions 1 and 2 say the cross-requirement tension (an index target inside a disclosure) and the new legend heading are "disclosed in the PR".
   - Dispositions 4, 7 and 8 say they are "carried to the follow-up bead".
   - [Observed] `gh pr list --head impl/p98-opening-index --state all` returns `[]`. `bd comments syzygy-u05.23` returns none. A sweep of `bd list --all --json` (616 beads) for `u05.23`, `OPENING-INDEX-IMPL` or `P-98` finds only `syzygy-u05.23`, `syzygy-00ls`, `syzygy-bb4x` and `syzygy-u05.12`. None of them is a follow-up carrying items 4, 7 or 8.
   - [Unknown] Whether these are staged to land with the PR.
   - Exception: before merge, the PR body must name the tension and the legend heading, and the follow-up bead must exist with items 4, 7 and 8.

3. **note (round-1 note 3, repaired)**: `polaris-opening-index.browser.test.ts:176,199-201`.
   - [Observed] The line must now match `^[0-9]+( \/ [0-9]+)? words$` exactly (`line-text`).
   - [Observed] The claim-markup check now tests the index and each line, both with `matches` and with `querySelector`.
   - [Observed] The mutants `line-separator` (en dash) and `line-as-claim` are recorded with their `old`/`new` fragments at commit `89b96979…` and are killed.
   - [Inferred] The verdict-word scan over `lines` still cannot fire on its own, because any word fails `line-text` first. The falsifier stays enforced, through the stricter limb.

4. **note (round-1 notes 5 and 6, repaired)**: `docs/evidence/pwb-p98-polaris-size-measurement-2026-10-15.json`; `pwb-p98-opening-index-oracle-2026-10-15.json`.
   - [Observed] The size items now sum to 1,779 + 2,674 + 423 + 224 + 209 = 5,309. With the 11 bytes taken by difference that makes 5,320, the measured delta. Both records are stated at Butlers `36f0e0eb`. The 11-byte attribution is labelled [Inferred].
   - [Observed] `casesSigned` now gives the reason each synthetic case is synthetic.
   - [Observed] The scripting-off behaviour (round-1 note 7) is stated in `scriptingOff`.
   - [Unknown] The per-node `getComputedStyle` cost on an observed page is still unmeasured.

5. **note**: `docs/evidence/pwb-p98-opening-index-oracle-2026-10-15.json` (`testsPassed`, `pages`, `subject.syzygyCommit`).
   - [Observed] The record gives `Tests  14 passed (14)` and `pages: 10`. My run without `SYZYGY_P98_PAGE` gives 13 passed, 1 skipped and 8 pages. The record therefore reflects a run with the operator capture present, which is consistent with its `liveCapture` block.
   - [Inferred] The subject commit `89b96979` together with a capture served from `0883ecfa` is consistent, because the renderer bytes are identical across that range (Basis).
   - [Observed] The record does not state that the 14/10 figures depend on the capture variable. A reader re-running without it gets 13 passed and 8 pages, and could mistake that for a regression.
   - Optional: say so in the record.

Count: 5 findings — 0 blocking, 0 revise, 5 note.
