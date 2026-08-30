# R-POC Product Review — Three-Surface POC, ten-minute demonstration

**Commit:** 2c1f8d5a955d5066c9065859d058b07b01454172 (verified `git rev-parse HEAD`) / **Reviewer:** syzygy-2m7 (independent fresh-reader agent, no prior involvement in Wave-A/B/C POC implementation) / **Date:** 2026-08-30 / **Node:** v24.6.0

This is a **one-shot product review** per the owner's Three-Surface POC review
budget (`decisions/THREE-SURFACE-POC-MODE-DIRECTION.md`; bead syzygy-2m7). No
second review cycle is implied or requested. Scope is bounded to the runnable
demo, its documented ten-minute script, and `GET /api/poc` — not a
repository-wide, governance, or spec-reconciliation review.

## Verdict: NOT FALSIFIED (all three), with one non-blocking doc-drift finding and three cosmetic/non-blocking findings

None of the three named assumptions was falsified by direct attempts to break
them. One finding (PRF-1) is a real, concrete gap — the documented walkthrough
is stale relative to what PRs #7–#10 actually shipped — but it does not defeat
the demonstration or truth floor, because the live UI is self-explanatory
without the doc. See findings below.

## Method and timings (all [Observed], this session, at commit 2c1f8d5)

1. `npm ci` inside the assigned worktree (worktree gotcha per AGENTS.md "Notes
   to self" — no local `node_modules` otherwise): **0.92s**.
2. Fresh-build clean run of the documented one-command demo,
   `npm run poc -- --repo /home/tze/GitHub/butlers` (`dist/` removed first to
   force a real `tsc -b --force` build, not a cached one): daemon printed its
   ready banner within **~9-10s** of invocation (build + start).
3. `GET /`, `/polaris`, `/trajectory`, `/orrery`: all **200**, each under
   **7ms** server time.
4. `GET /api/poc` without a token: **401**. With the printed credential-file
   token: **200** in **41ms**, 3.57MB JSON body.
5. Total wall time from a cold `npm ci` to having all four human surfaces and
   the authenticated machine endpoint open and cross-checked: **under two
   minutes** of pure command/page-load time — comfortably inside the
   documented ten-minute budget. Reading and reasoning about what the pages
   say (the actual "understand this" work a fresh reader does) took
   materially longer than that, driven mostly by Trajectory's 244-row board
   (198KB HTML) — see PRF-3.

## Assumption 1 — understandable without repository spelunking

**Verdict: NOT FALSIFIED, with one qualified exception (PRF-1).**

Every page carries an inline epistemic legend (`● Observed` / `? Unknown`),
every claim on Polaris and the home page cites its exact source file and
revision inline, and Trajectory's materialize panel explains itself in plain
prose before any action is taken ("Preview of the exact Bead this
human-triggered action would create. Nothing is written until the button
below is explicitly clicked; Syzygy never triggers this on its own."). I was
able to understand what each of the four human surfaces was claiming, and
why, from the rendered page alone, without opening a single source file, for
every page **except** one specific interaction outcome (below).

The one place I had to read source to resolve what looked like a
contradiction: after triggering materialize (see Assumption 2), the
Trajectory card for the affected item showed `wi-status: closed` and,
directly below it, `External worker: Planned`. Read cold, "closed" next to
"Planned" reads as contradictory. Reading `packages/three-surface-poc-core/src/model.ts`
and `materialization.ts` resolved it: these are two independent, correctly
each-honest fields (the Bead's own status vs. the worker-change git-observation
lifecycle state), and both were accurate — the underlying Bead really is
closed (a prior worker's test cleanup left it that way) and the
worker-change observer really has seen no git commits against it yet
("Planned" is that state machine's start state). This is not a bug, but nothing
on the card itself explains that these two badges are orthogonal. **PRF-2** (non-blocking).

**PRF-1 (non-blocking, but should be repaired in the next pass):**
`docs/THREE-SURFACE-POC.md` — the file `README.md` names by exact path as
"the ten-minute first-slice walkthrough" — has not been updated since PRs
#7–#10 landed materialize, worker-change observation, and test-artifact
verification. Its own "Deliberately absent in this slice" section still
reads:

> - No Beads item is materialized yet.
> - No worker is dispatched and no implementation code is changed.
> - No test-run artifact is captured or ingested.

All three of these are now demonstrably false as blanket claims: a
human-triggered materialize action exists and works (Assumption 2 below), a
worker-change observer tracks git activity against the materialized item, and
a real test-artifact ingestion/verification path was proven end-to-end this
same session per `AGENTS.md`'s own "Notes to self" record (83 real Butlers
pytest passes ingested and rendered Verified). The doc's five numbered
walkthrough steps (1–5) are still accurate as far as they go, but they never
mention the materialize button, Orrery's client-rendered spatial view, or
test-artifact verification at all — a reader who follows *only* the
documented script would miss roughly half of what actually ships at this
commit.
This does not defeat the demonstration itself: every page I loaded from
following the doc's five steps was self-explanatory on its own terms, and the
materialize panel's inline copy fully explains itself without the doc's help.
It is a genuine, low-effort-to-fix gap in the "documented ten-minute script"
specifically named in this bead's acceptance criteria, so I am flagging it as
the top non-blocking finding for the repair pass (`syzygy-2o3`).

## Assumption 2 — the work/evidence story is operationally useful

**Verdict: NOT FALSIFIED.**

I performed the actual human-triggered materialize action for real (`POST
/trajectory/materialize`, credential-class `human-open`, no auth token
required — deliberately human-only, matching its design intent), rather than
just reading its code. Result: `Reused bu-5o5tk in the configured Butlers
repository` — the system correctly detected a pre-existing Bead sharing the
same `external_ref` (`syzygy-poc:work:whatsapp-single-event-normalization`,
created and closed by a prior worker's own end-to-end test) via a live
`external_ref` lookup against Butlers' Beads Dolt database, and reused it
instead of minting a duplicate — exactly the idempotency the code comments
promise (`materialization.ts:270-276`). I independently confirmed via `bd sql`
against the real Butlers repo, both before and after, that **no new Bead was
created** by my action (the "found" path in `materializeWorkItem` never calls
`runCreate`), so this test left no new durable side effect on the shared
Butlers database.

Immediately after the click, every one of the four surfaces (home, Polaris,
Trajectory, JSON) updated in lockstep to `Materialized as Beads item
bu-5o5tk` with matching provenance citations — no restart needed, no stale
cache. This is a real, useful demonstration of the "approved intent →
human-triggered work" chain the POC claims: an owner-approved intent
(`REQ-switchboard-identity-001`) really does turn into a real, externally
visible unit of work with one click, and the system is honest that this is
*all* it currently proves — the very same materialize response, and every
surface after it, correctly kept "Focused pytest evidence: Unknown" and
"Verification: Not verified" (no `[<bead-id>]`-marked commit exists for this
run), refusing to claim more than it had evidence for. I attempted the
merge-as-proof counterexample directly here — expecting the system might
render "Verified" or "Complete" off of the Bead's mere existence or its
`closed` status — and it did not; the fail-closed design held under an actual
click, not just in the tests.

**PRF-3 (non-blocking):** Trajectory's board renders 244 of 6,974 real,
unrelated Butlers backlog items (all non-closed items plus the 50 most
recently closed) alongside the single item the POC's evidence chain actually
demonstrates. The page's scope notice states the count honestly, but nothing
on the page tells a first-time reader which one of the 244 cards is "the"
demonstrated item — the only visual differentiator is that `bu-5o5tk` alone
carries the extra worker-change badge block. A reader skimming the board
top-to-bottom (alphabetical by ID) would reach it only after scrolling past
roughly 200 unrelated real cards. This dilutes, without breaking, the
"coherent useful story" the board is meant to tell — most of what's on screen
has no relationship to the one capability the rest of the POC narrates.

## Assumption 3 — human and machine views agree

**Verdict: NOT FALSIFIED.**

Direct comparisons performed, all matching exactly:

| Fact | Human page | `GET /api/poc` |
|---|---|---|
| Observed code-structure file count | "6112 files" (Polaris) / Orrery scope notice | `codeStructure.files.length === 6112` |
| Observed work-item count | "6974 work items" (Polaris) | `workItems.items.length === 6974` |
| Trajectory board selection | "244 of 6974... 6730 outside" | `trajectory.renderedCount=244, excludedCount=6730, totalCount=6974` |
| Materialized Bead id/status, pre- and post-click | `bu-5o5tk`, `closed`, on home/Polaris/Trajectory | identical `beadId`/`status` in `entities`, `workItems.items`, `workerChange` |
| Worker-change lifecycle state | "External worker: Planned" | `workerChange.state === "planned"` |
| Unmapped-code disclosure | "1 of 6112... 6111 unmapped" (Orrery) | `codeStructure` vs. `mappedFileCount:1, unmappedFileCount:6111` in Orrery's embedded JSON |

I also swept every in-page anchor link (`href="#..."`) on all four rendered
pages against the `id="..."` attributes present on the same page
(dangling-link counterexample attempt): **0 of 266 anchors across
home/Polaris/Trajectory/Orrery were dangling.** `GET /nonexistent` and `GET
/api/nonexistent` both correctly 404.

**PRF-4 (cosmetic, non-blocking):** the relationship explanation text
rendered on Polaris/home for `relationship:intent-to-work` reads "The
human-triggered materialization step **created** Beads item bu-5o5tk" — but
in my actual run it did not create anything; it reused an existing closed
Bead (the materialize response page and the materialize-status line both say
"Reused" / "Already materialized... idempotent", correctly). The relationship
explanation string in `model.ts` is a static template that always says
"created" regardless of whether the underlying action created or reused. The
`beadId` and `status` themselves are accurate everywhere; only this one
sentence's verb is imprecise. Does not affect any epistemic label, provenance
citation, or truth-floor claim.

## Counterexample-class summary

| Class | Attempted | Result |
|---|---|---|
| Dangling link | Yes — swept all 266 in-page anchors + two out-of-route GETs | None found |
| False-green | Yes — checked whether "closed"/"Reused" ever renders as unqualified success | Not found; every claim stays scoped to what it actually observed |
| Merge-as-proof | Yes — materialized a real Bead and checked whether existence/closure alone triggered a "Verified" claim | Did not; verification stayed correctly Unknown absent a real observed commit |
| Human/machine drift | Yes — six independent fact comparisons across all 4 surfaces + JSON | No drift found |

## Findings for the repair pass (`syzygy-2o3`)

None are blocking. In priority order:

- **PRF-1 (non-blocking, do first):** Update `docs/THREE-SURFACE-POC.md` to
  reflect materialize, worker-change observation, and test-artifact
  verification, which now exist; its "Deliberately absent" list is stale.
- **PRF-2 (non-blocking):** Trajectory work-item cards that carry both a
  `wi-status` (Bead status) and a `worker-change-state` badge give no inline
  hint that these are two independent fields; consider one line of copy
  distinguishing "Bead status" from "observed worker-change state."
- **PRF-3 (non-blocking):** Trajectory mixes 243 unrelated real Butlers
  backlog cards with the one demonstrated item with no visual call-out;
  consider surfacing/pinning the demonstrated item, or a short intro line
  naming it, so a fresh reader isn't required to scroll/search for it.
- **PRF-4 (cosmetic):** the `relationship:intent-to-work` explanation string
  in `model.ts` always says "created" even on a reuse outcome; make it
  conditional on the `materialization.beadId`/record's created-vs-reused
  kind, matching the wording already used correctly elsewhere on the same
  page.

## Bottom line

Run from a genuinely fresh `npm ci`, the documented one-command demo starts
in well under ten minutes and both its self-explaining UI and its
authenticated JSON stay internally consistent under direct, adversarial
probing — including a real, state-changing exercise of the materialize
action, not just reading its code. I found no dangling links, no false-green
claims, no merge-as-proof reasoning, and no human/machine drift. The one
concrete gap (PRF-1) is that the doc named as "the ten-minute walkthrough"
undersells what's actually shipped; I judged this non-blocking because the
live UI itself never required me to fall back to source-reading to make
sense of what I was looking at, except for the one Bead-status/worker-change
interplay noted in PRF-2. I made no edits to application code; the only
mutation I performed against the external system was one materialize POST,
which I independently confirmed via `bd sql` created zero new database rows.

`python3 scripts/check_governance.py` at this commit: **32 OK, 19 WARN, 0
FAIL (51 checks)** — read from script output, not exit code; unaffected by
this docs-only addition. [Observed]
