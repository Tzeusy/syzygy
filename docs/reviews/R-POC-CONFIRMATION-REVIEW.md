# R-POC Confirmation Review — PRF-1 repair

**Commit:** f1c2901ecacf063c176242c06eefe46557185a64 / **Reviewer:** syzygy-2m7 (same independent fresh-reader agent as the original review) / **Date:** 2026-08-30 / **Node:** v24.6.0

This is the one-shot confirmation pass named by `syzygy-2o3` AC3 — no further
findings or cycle follow this. Original review:
`docs/reviews/R-POC-PRODUCT-REVIEW.md` (commit 2c1f8d5, merged as syzygy-2m7).
Repaired in PR #12, branch `agent/syzygy-2o3`.

## Verdict: CONFIRMED

### Checks performed (each with [Observed]/[Inferred] and evidence)

1. **HEAD identity and diff scope.** [Observed] `git rev-parse HEAD` =
   f1c2901ecacf063c176242c06eefe46557185a64; working tree clean before and
   after. `git diff main...HEAD --stat` shows exactly one file touched by the
   repair commit: `docs/THREE-SURFACE-POC.md` (53 insertions, 10 deletions).
   No application source, test, or config file differs from `main` at this
   commit — confirmed with a second, narrower diff excluding both review docs
   (`git diff main...HEAD --stat -- . ':!docs/THREE-SURFACE-POC.md'
   ':!docs/reviews/R-POC-PRODUCT-REVIEW.md'`), which produced no output.

2. **PRF-1 is genuinely resolved, not just reworded.** [Observed] The old
   "Deliberately absent in this slice" list claimed "No Beads item is
   materialized yet," "no worker is dispatched," and "No test-run artifact is
   captured or ingested" — all three now demonstrably false given PRs #7-#10.
   The repaired doc removes exactly those three false claims and replaces
   them with: an accurate description of the materialize action (including
   its idempotent "Re-run materialize" label), the worker-change badge and
   its three-state vocabulary, the "Verified"/"Not verified" badge, and a new
   "Capturing test-run evidence" section naming the real
   `npm run poc:capture-test-artifact` command. I checked each specific claim
   against source rather than trusting the diff on its face:
   - "Re-run materialize (idempotent)" button label — matches
     `apps/three-surface-poc/src/materialize-action.ts:82` exactly
     (`beadId === null ? 'Materialize this work item' : 'Re-run materialize
     (idempotent)'`).
   - "External worker: Planned / Active / Changed / merged" — matches the
     real state vocabulary `['planned', 'active', 'changed-or-merged']`
     (`worker-change-observation.ts:3`) and its rendered label map
     (`trajectory.ts:54`, `'changed-or-merged': 'Changed / merged'`) verbatim;
     the doc's phrasing initially read to me as naming four states, but it is
     an accurate concatenation of the three real rendered labels.
   - "Verification: Verified — …" / "Verification: Not verified" — matches
     `trajectory.ts:59,61` verbatim.
   - `npm run poc:capture-test-artifact -- --repo <butlers> --scope <path>
     --state-dir <dir> [--python <bin>]` — matches the real script in
     `package.json:17` and the CLI's actual flags.
   I also re-ran the live demo (below) and confirmed the materialize panel,
   worker-change badge, and verification badge it describes render exactly
   as the new doc says they will.

3. **PRF-2/3/4 are confirmed untouched, as intended (not a defect).**
   [Observed] The scope check in item 1 already proves no application source
   changed. Specifically re-checked against the running app: the same
   `bu-5o5tk` card still shows `wi-status: closed` directly beside `External
   worker: Planned` with no inline distinguishing text (PRF-2, unchanged);
   Trajectory's board still renders 244 mixed real/demo items with no visual
   call-out for the one demonstrated item (PRF-3, unchanged, confirmed by the
   unchanged `trajectory.ts` diff); the `relationship:intent-to-work`
   explanation string in `model.ts` is untouched (PRF-4, unchanged — `git
   diff main...HEAD -- packages/three-surface-poc-core/src/model.ts` is
   empty). This matches the coordinator's statement that PRF-2/3/4 were
   deliberately deferred, and confirms scope discipline held: the repair
   touched only what PRF-1 named.

4. **No regression — full gates re-run at f1c2901, all green.** [Observed]
   - `npm ci` (fresh worktree, no prior `node_modules`): clean, 0
     vulnerabilities.
   - `npm run typecheck` → clean, no output (pass).
   - `npm test` → **74 files / 535 tests passed, 2 skipped** (the 2 skips are
     the pre-existing live-gated `*.live.test.ts` files, gated by
     `SYZYGY_POC_BUTLERS_REPO`/`SYZYGY_POC_BUTLERS_PYTHON`, same as at the
     original review).
   - `npm run build` → clean, no output (pass).

5. **Real fresh-checkout ten-minute demo, re-run against this exact commit.**
   [Observed] `dist/` removed from all four POC-adjacent packages to force a
   genuine `tsc -b --force` rebuild, then `npm run poc -- --repo
   /home/tze/GitHub/butlers` from cold: daemon printed its ready banner
   within ~10s. `GET /`, `/polaris`, `/trajectory`, `/orrery` all **200** (1-5ms
   server time each); `GET /api/poc` **401** without a token, **200** in
   ~32ms with the printed credential-file token. This is a narrower
   confirmation pass, not the original review's full adversarial sweep (per
   the bead's own instruction not to redo that) — I re-verified the mechanics
   the doc change describes are live and correct, not a fresh falsification
   attempt.

6. **Governance check.** [Observed] `python3 scripts/check_governance.py` at
   f1c2901: **32 OK, 19 WARN, 0 FAIL (51 checks)** — read from script output,
   identical totals to the original review's run at 2c1f8d5. Unaffected by
   this docs-only repair, as expected.

### Bottom line

The repair is real, accurate, and scoped exactly to PRF-1: every new claim in
`docs/THREE-SURFACE-POC.md` checks out against the actual running system and
its source, the three false "deliberately absent" claims are gone, and
nothing outside that one file changed — PRF-2, PRF-3, and PRF-4 remain
exactly as I found them, as intended. Tests, typecheck, build, and the real
fresh-checkout demo all pass at this exact commit with no regression from the
originally-reviewed commit. **CONFIRMED.** No further findings; per the
bead's own non-goals, this closes the review budget for this POC.

Strictly read-only against application code: no repo edits beyond this
confirmation record itself; the one live materialize-adjacent state (the
reused, closed `bu-5o5tk` Bead from the original review) was left as-is —
no new mutation performed against the external Butlers repository this pass.
