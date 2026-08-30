# R-POC Cycle-4 Confirmation Review — C3-2/gk9 repair

**Commit:** a1ce5e9697708b9c59940bfacada50a9d018fbe1 / **Reviewer:**
independent fresh-context confirmation reviewer (no prior involvement in
this POC's implementation or any earlier review pass) / **Date:** 2026-08-30.

Scope: confirm whether commit a1ce5e96 ("fix: cycle-4 repairs — C3-2
Polaris narrative, gk9 build-output timeout [syzygy-qdj]") actually repairs
the deferred C3-2 NOTE recorded in `docs/reviews/R-POC-CYCLE-3-REVIEW.md`
and the `build-output.test.ts` timing flake recorded in
`docs/reviews/R-POC-CYCLE-3-CONFIRMATION.md`, run the two POC test
projects and read their output, and hunt for regressions. Read-only against
application code; the only file written is this one.

## Verdict: CONFIRMED

### Commit identity

[Observed] `git log -1`: `a1ce5e9697708b9c59940bfacada50a9d018fbe1 fix:
cycle-4 repairs — C3-2 Polaris narrative, gk9 build-output timeout
[syzygy-qdj]`, HEAD of `main`. `git log --oneline -1 -- polaris.ts
polaris.test.ts build-output.test.ts` returns the same commit for each —
nothing later touched them, so this review is of the repaired state as it
stands at HEAD. `git status --short` shows only the pre-existing, unrelated
`.gitignore` modification. `git show a1ce5e96 --stat`: 3 files changed, 99
insertions, 9 deletions — `apps/three-surface-poc/src/build-output.test.ts`,
`apps/three-surface-poc/src/polaris.test.ts`,
`apps/three-surface-poc/src/polaris.ts`.

## Per-finding verdicts

### C3-2 (NOTE) — Polaris had no narrative connective tissue

**Verdict: REPAIRED.** [Observed] `polaris.ts` adds a `MOVEMENTS` array of
three `{beforeEntityId, heading, lede}` records rendered via
`movementHeader()` immediately before the anchor entity's section
(`project:butlers`, `code:identity-resolution`,
`work:whatsapp-single-event-normalization`), a fourth movement header
("The inventories behind the map") before the code-structure/work-items
regions, an opening `<p class="framing">` paragraph, and a
`<p class="relationships-lede">` inside the "How these connect" section.
Entity/region `<h2>` headings are demoted to `<h3>`, nested under the new
movement `<h2>`s, so the document now has one heading level for its
top-level narrative arc and a second for the claims within each arc segment.

[Inferred, but I judge this to genuinely resolve the finding rather than
just add markup] The three movement ledes each state *why* that order was
chosen ("intent precedes realization and realization precedes evidence" —
stated explicitly in the framing paragraph, echoed in each lede's "opens
with… moves to… closes with" language), and the relationships lede states
what the following list actually is ("how far the evidence actually
reaches between them"). This is exactly the three things C3-2 said were
missing: a framing paragraph, a stated ordering rationale, and sentences
that span/introduce claims rather than atomize them. The page now reads as
a document with a beginning, middle, and end, not a flat list of `<h2>`+
sentence+citation blocks reformatted from `exact-tables.ts`.

**Epistemic-bar sweep (the critical check):** [Observed] I read every new
string literal added in this commit (the four movement `heading`/`lede`
pairs, the framing paragraph template, the inventories lede, and the
relationships lede — 8 sentences total). All are framing about the
document's own structure or the codebase's own architecture, never a new
positive claim about the observed Butlers project:
- The three movement ledes and the framing paragraph's ordering sentence
  talk about "the reading," "this document," "the sections below" — meta
  language about the page, not new facts.
- "Orrery and Trajectory render from these two observations" (inventories
  lede) is a claim about *this codebase's* architecture, not the observed
  project. I verified it is true: `packages/three-surface-poc-core/src/model.ts:536`
  computes `orreryProjection = projectOrrery(codeStructure, …)` and
  `model.ts:543` computes `trajectoryProjection = projectTrajectory(workItems, …)`
  — so the sentence is [Observed] accurate, not an unprovenanced assertion.
- The framing paragraph's one number-bearing sentence — "Of the N entity
  and relationship claims it makes, O are Observed with citations and U
  are disclosed Unknown" — is the only place a quantity is asserted, and it
  is computed at render time from `model.entities`/`model.relationships`
  (`polaris.ts:143-145`), not hand-written. I confirmed this by reading the
  computation inline (`claims.filter(claim => claim.epistemic.label ===
  'Observed').length`) rather than trusting the comment that says so.
No sentence anywhere states a number, name, date, or fact about Butlers
itself outside the pre-existing per-entity/relationship claim sections
(which were not touched by this commit and were already covered by the
cycle-3 sweep).

### syzygy-gk9 — `build-output.test.ts` 15s timeout flake

**Verdict: REPAIRED.** [Observed] The `it()` timeout parameter changes from
`15_000` to `60_000`, with a new comment explaining two sequential
`tsc -b --force` builds run here (~7.5s each unloaded) and that 15s
intermittently timed out under load, but the forced rebuild itself is the
trust boundary and must stay. The test body itself
(`writeFileSync`/`execSync('npm run build:poc')` twice/`readFileSync`
assertions) is unchanged — only the timeout budget moved. The forced
double-build is confirmed still present in the diff (no line removing or
weakening `tsc -b --force` from the test or from `build:poc`'s script
definition). This session's run of `build-output.test.ts` completed in
5.8s (well inside 60s), consistent with the flake being a margin problem
under load rather than something requiring redesign.

## New test verification (C3-2)

[Observed] `polaris.test.ts` gains one new test, "frames the reading with
movements, an honest computed tally, and a relationships lede (C3-2)." It
asserts, per movement anchor, that `data-polaris-movement="<anchor>"`
appears in the HTML at an index strictly before
`data-polaris-section="<anchor>"`; asserts the `region:code-structure`
movement marker exists; independently recomputes the observed/unknown
tally from the fixture model and asserts the exact tally sentence appears
verbatim; and asserts the relationships-lede class and its "never bridged
by prose" text appear. Reverting `polaris.ts` to its pre-a1ce5e96 state
would fail every one of these assertions (none of the asserted strings/
attributes exist in the old file, confirmed by diffing against
`/tmp/polaris_old.ts` in this session) — this is a genuine falsifier, not
markup-presence theater. I did not need to run a live mutation since the
old file (available via `git show a1ce5e96~1:…`) already serves as the
"reverted" state and demonstrably lacks every asserted string.

## Test run

[Observed] `npx vitest run --project '@syzygy/three-surface-poc-core'
--project '@syzygy/three-surface-poc-app'`:

```
Test Files  20 passed | 2 skipped (22)
     Tests  117 passed | 2 skipped (119)
```

117 passing, up from cycle-3's confirmed 115 passing + 1 failing. The
arithmetic reconciles exactly: 115 (cycle-3 passing) + 1 (the previously
failing `build-output.test.ts` case, now passing under the raised budget)
+ 1 (the new C3-2 `polaris.test.ts` test) = 117. The 2 skipped tests are
the same pre-existing env-gated `test-artifact-verification.live.test.ts`
and `work-items.live.test.ts` — unchanged. No test file count changed (22
in both cycles); no new test *file* was added, only new `it()` blocks
inside existing files, consistent with `git show --stat` touching only
`polaris.test.ts` and `build-output.test.ts`.

## Regression hunt

**Heading-hierarchy / stale-id dependents:** [Observed] Repo-wide grep for
`polaris-` outside `dist/` and outside `polaris.ts`/`polaris.test.ts`:
zero hits. `surface-routes.test.ts` and `cross-cutting.test.ts` import
`renderPolarisPage`/`POLARIS_HUMAN_PATH` but assert only on the skip-link,
legend, reduced-motion-media-query, and no-foreign-script-origin
properties — none inspect heading levels or the demoted `h2`→`h3` ids. No
test or code outside `polaris.ts` depends on the old `<h2 id="polaris-…">`
structure.

**Machine-JSON leakage:** [Observed] The `MOVEMENTS` array, framing
paragraph, and all new lede strings are local to `polaris.ts` — computed
inline inside `renderPolarisPage(model)` from the `model` argument, never
written back onto `PocModel` or any of its fields. `routes.test.ts`'s
parity test does `expect(wireModel).toEqual(model)` against the live
`GET /api/poc` JSON body and does not invoke `renderPolarisPage` in that
assertion at all — the machine wire body is the same `PocModel` object,
untouched by anything in this commit. Structurally, no code path exists
for Polaris prose to reach the JSON endpoint. `routes.test.ts` passed in
this session's run.

**Parity oracle (`routes.test.ts`):** [Observed] Both tests in
`routes.test.ts` passed — the human/machine parity test (`wireModel` deep-
equal to `model`, plus `visibleParityTuples(html)` equal to
`parityTuples(wireModel)` against the *home page's* exact tables, which
this commit does not touch) and the HTML-escaping test.

**No other regression found.** [Observed] Full-suite run above is 20/22
files and 117/119 tests passing with the same 2 pre-existing skips as
every prior cycle; no test outside `polaris.test.ts` and
`build-output.test.ts` changed behavior.

## New findings

None. [Observed] The C3-2 repair adds only framing/structural prose and
computed arithmetic, verified against the model's own fields; the gk9
repair only widens a timeout while preserving the forced-rebuild trust
boundary the finding explicitly required to stay. No stale reference to
the old Polaris heading structure exists anywhere in the repo outside
`polaris.ts`/`polaris.test.ts` themselves.

## Bottom line

C3-2 is genuinely repaired: Polaris now has a stated ordering rationale, a
framing paragraph with a model-computed (not hand-written) tally, and
connective ledes at each movement boundary and before the relationships
list — the qualitative "reads as a document" bar is met, not just satisfied
by markup. Every added sentence is framing about the document/codebase or
computed arithmetic over the shared model; none asserts an unprovenanced
new fact about the observed Butlers project. syzygy-gk9 is genuinely
repaired: the timeout budget was raised with a documented rationale, and
the forced double `tsc -b --force` rebuild — the actual trust boundary —
is untouched. 117 of 119 non-skipped-adjusted tests passed in this
session's run (117 passed, 2 skipped, 0 failed), with no regression found
in heading-hierarchy dependents, machine-JSON parity, or the home-page
exact-table parity oracle.

No repository edits were made beyond this review file. This file is FROZEN
as of this write — any further edit to it retires this review per
AGENTS.md verification rule 10.

## Verdict

CONFIRMED
