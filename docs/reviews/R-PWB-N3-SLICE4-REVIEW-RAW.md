# R-PWB-N3-SLICE4 review — PR #96 at 25874a4

Verdict: REVISE

## Scope

PR #96 (head `25874a4390dfa2c15b18f3b3b0b2be14c189fab7`), against `syzygy-u05.3`
DESIGN slice 4 ("Population block in the M1 measurement script and evidence
shape; re-measure and record beside the lane A record") and its acceptance
clause ("every retained page-size evidence record carries a population
block; re-measurement recorded beside pwb-m1-polaris-lane-a-measurement").

Diff (`git diff origin/main...25874a4390dfa2c15b18f3b3b0b2be14c189fab7 --stat`):
```
docs/evidence/pwb-m1-polaris-lane-a-population-2026-09-23.json | 86 ++
packages/three-surface-poc-core/src/evidence-population.test.ts | 119 ++
packages/three-surface-poc-core/src/evidence-population.ts | 80 ++
packages/three-surface-poc-core/src/index.ts | 1 +
4 files changed, 286 insertions(+)
```
`model.ts`, `polaris.ts`, `routes.ts` do not appear — confirmed untouched (check f, below).

## Findings

### 1. (REVISE) Acceptance clause "every retained page-size evidence record carries a population block" is not met, and the gap is not disclosed

The bead's WHAT/ACCEPTANCE text is unqualified: "Every retained page-size
evidence record gains a population block... every retained page-size
evidence record carries a population block." The PR satisfies this only for
the one new record it creates.

Denominator (rule 9): a `grep -l '"polaris-direct.html"' docs/evidence/*.json`
sweep — records that actually captured a `/polaris` page-byte payload — finds
10 tracked files:
```
polaris-m10-machine-contract-funnel-2026-09-15.json
polaris-m13-navigation-scale-funnel-2026-09-15.json
polaris-m16-renderer-visual-system-funnel-2026-09-17.json
polaris-m9-one-identity-funnel-2026-09-15.json
polaris-m14-provenance-depth-funnel-2026-09-17.json
polaris-m5-agent-briefing-funnel-2026-09-14.json
polaris-m4-owner-loop-funnel-2026-09-14.json
pwb-laneb-strict-scope-estimate-2026-09-14.json
pwb-m1-polaris-lane-a-measurement-2026-09-13.json   <- the M1 lane A record itself
pwb-p63-polaris-trim-measurement-2026-09-07.json    <- P-63 arm A trim measurement, also retained/cited (AGENTS.md Notes to self quotes its byte deltas)
```
Not one of these 10 pre-existing records carries a population block after
this PR; only the brand-new `pwb-m1-polaris-lane-a-population-2026-09-23.json`
does. The lane-A record — the very one this slice is anchored to — has none,
and the PR does not touch it (correctly, per the historical/bound-record
rule — see finding 2). The new record's own `comparisonToLaneA` field is
honest about one consequence of this ("this record cannot compute a numeric
population delta against [lane A]"), but nowhere in the PR body, the bead
comment, or the evidence record is it stated that the broader acceptance
text ("every retained... record") is being read narrowly as "one new record
next to lane A," or that `pwb-p63-polaris-trim-measurement-2026-09-07.json`
(also a retained page-size record, also cited elsewhere as evidence) is out
of scope. The bead comment simply declares "Slice 4... done." This is the
overclaim the task brief asked me to check for: the acceptance wording says
"every," the delivered state is "one," and the shortfall is silent.

This also undercuts the feature's own stated purpose (WHY: "V1-F2/F4: this
pass had to reconstruct population attribution by hand... so growth is
attributable without reconstruction") — attribution against the nearest
retained baseline (lane A, 10 days prior) still requires exactly the manual
reconstruction the slice exists to avoid, because lane A has no block.

Recommendation: either extend population blocks to the other retained
page-size records (at minimum `pwb-p63-polaris-trim-measurement-2026-09-07.json`,
since it and lane A are the two measurements Notes-to-self already treats as
comparable), or explicitly narrow and disclose the acceptance clause's scope
in the PR body and bead comment, with a follow-up bead filed for the rest.

### 2. (Informational, not blocking) No persistent "M1 measurement script" exists to wire into — the PR's approach matches established repo convention

I searched for a checked-in M1 measurement script (`find scripts -iname
"*polaris*" -o -iname "*m1*measur*"`, then a repo-wide grep for
`derivePopulationBlock`/`evidence-population` outside the new files) and
found none: `derivePopulationBlock` is referenced nowhere else in the tree.
There is no `scripts/measure-polaris-page-size.*` or similar file for any
prior M1-family record either — `pwb-m1-polaris-lane-a-measurement-2026-09-13.json`
and `pwb-p63-polaris-trim-measurement-2026-09-07.json` both embed their own
bash `measurementScript` as a JSON string field, each written fresh per
measurement, matching `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`'s
ad hoc, no-persistent-tooling framing.

Given that convention, "wiring into the M1 measurement script" cannot mean
patching a reusable file — there isn't one. The PR follows the same pattern:
it ships a pure, unit-tested, importable module
(`packages/three-surface-poc-core/src/evidence-population.ts`) and embeds an
updated `measurementScript` string in the new record that calls it. That is
consistent with how this evidence family already works.

The caveat worth naming explicitly (not a defect, but a real limitation):
nothing forces a *future* M1-style measurement to include the population
step. Since each measurement's script is hand-written from the nearest
precedent, a future agent that copies the older lane-A script text (which
predates this module) would silently omit the population block again. There
is no test, lint, or schema check enforcing the block's presence on new
page-size records. This is a soft, human-memory dependency, not a "wired in,
automatic" guarantee — the PR/bead language ("done") does not flag this
either.

### 3. (Non-blocking, but real) My own rule-6 mutation of `decodeHtmlAttr` survived all 8 tests — the entity-decoding behavior is untested

Per task (e), I mutated `packages/three-surface-poc-core/src/evidence-population.ts`
myself (not the two mutations already recorded in the PR/evidence file) by
deleting the `&amp;` → `&` replacement in `decodeHtmlAttr`:
```
-    .replace(/&amp;/g, '&');
+    ;// &amp; decode removed (mutation)
```
Result: `npx vitest run packages/three-surface-poc-core/src/evidence-population.test.ts`
— **8/8 still passed**. Reverted (`git status --short` on the file came back
clean afterward, confirmed byte-identical restore).

Root cause: the one test that exercises decoding
("decodes HTML entities before counting, so an escaped id is not
double-counted as a distinct value") uses a fixture with exactly one
`data-claim-id` occurrence and asserts `renderedClaimIdCount(...) === 1`.
That assertion is true whether or not decoding happens (there is nothing to
double-count against). The test's own docstring claims a property
(prevents double-counting an escaped id) that no fixture actually exercises
(e.g., two occurrences of the same id, one written with `&amp;`/`&#39;`-style
escaping and one written literally, decoding to the same string). This is
the same class of gap AGENTS.md's copy-oracle note warns about: a label or
assertion that happens to pass by coincidence rather than because the
behavior under test occurred. Low practical severity in production, since a
single rendered HTML document consistently escapes attribute values the same
way, so an in-page double-count from encoding is unlikely — but the claimed
rule-6 coverage ("mutated... confirmed on both derivation functions") does
not actually cover decoding, and the PR's own verification section implies
it does.

Recommendation: add a fixture with two `data-claim-id` occurrences of the
same underlying value where one is HTML-escaped and one is not, asserting
the count collapses to 1 (not 2) — or drop the decode-specific claim from the
docstring/PR verification language if it is considered out of scope.

### 4. (c) Figures are derived, not hard-coded; predicate and measured commit are recorded

- `population.itemCount` (426) is internally consistent with
  `population.modelCountsFull.items` (426) and traces to
  `projectShape.counts.items` per `derivedFrom.itemCount`.
- `population.claimIdCount` (719) states its predicate explicitly:
  `"derivedFrom.claimIdCount": "distinct data-claim-id attribute values
  rendered in /polaris HTML, decoded and de-duplicated; identical (719) on
  both the direct and tailnet-Host capture forms"` — this satisfies the task's
  ask that the predicate (distinct `data-claim-id`) be stated in the record.
- `butlersRevision` (`27bf71b0709b20970f4d3731d8e6f020f58b8a9f`) is recorded,
  cross-checked in the record against `git -C butlers rev-parse HEAD`, and I
  independently confirmed it is a real, reachable Butlers commit dated
  2026-09-22 (`git cat-file -t` → `commit`; `git log -1 --format=%cd` →
  `Tue Sep 22 20:01:09 2026 +0000`; subject `fix: render canonical entity
  activity stream [bu-bbwur] (#4057)`), consistent with a 2026-09-23
  measurement.
- The measured Syzygy commit is recorded (`syzygy.measuredAtCommit`:
  `0326aa8cdb8a64c4cee31dc185da10ec5643248a`, with the pre-rebase commit
  `dd01b58b3297a2bbb3190ef335ba33c0f04c7462` also named as provenance); both
  objects exist locally (`git cat-file -t` on each returns `commit`), so the
  citation is not fabricated, and the rebase-renaming caveat is disclosed in
  the record itself per the rebase-merge lesson in AGENTS.md.

I could not independently *re-run* the daemon capture to reproduce 426/719
from scratch: `apps/three-surface-poc/src/git-observation.ts` rejects any
`--repo` other than the one locator baked in at build/config time
(`{ kind: 'rejected', reason: 'locator-mismatched' }`, reproduced live by
pointing a built daemon at a scratch Butlers worktree checked out to the
exact recorded revision). This is the documented, known limitation in
AGENTS.md ("the daemon serves only the registered locator... so a repaired
Butlers page cannot be measured on a private daemon from a scratch clone").
I did not attempt to work around it by mutating the live, in-use
`/home/tze/GitHub/butlers` checkout (it currently has uncommitted changes and
is on a different branch/HEAD than the recorded revision, and rewriting it
would be destructive to the user's own work outside this review's scope).
Full independent reproduction of the two counts was therefore not feasible
in this session; what I did verify (unit tests, mutation testing of the
derivation logic itself, and the reachability/plausibility of the cited
Butlers commit) is the practical ceiling for this environment.

### 5. (d) PWB-REQ-014 authority sweep passes

`npx vitest run apps/three-surface-poc/src/polaris-authority-sweep.test.ts` →
4/4 passed. I also swept the new evidence JSON's keys (recursive walk over
all object keys) for `source`/`provenance`/`evidence`/`anchor` (the exact
trap AGENTS.md documents from the PWB-REQ-014 lesson) — zero hits. The record
uses `derivedFrom`, `measuredAtCommit`, `revision`, `method`, `butlers`,
etc., none of which collide with the sweep's flagged key names.

### 6. (f) model.ts, polaris.ts, routes.ts untouched — confirmed

`git diff origin/main...25874a4390dfa2c15b18f3b3b0b2be14c189fab7 --stat`
lists exactly the 4 files above; none of `model.ts`, `polaris.ts`,
`routes.ts` appear. The new module only reads `ProjectShapePopulationView`
(a narrowed structural view, not the real discriminated union) and raw
`/polaris` HTML/`/api/poc` JSON, matching the PR's claim that it consumes
already-serialized runtime output rather than adding a new observation path.

### 7. Build and test results (task g)

- `npm ci` in the worktree: clean.
- `npm run build:poc` (full `tsc -b --force` across cap1-core, cap1-daemon,
  three-surface-poc-core, apps/three-surface-poc): clean.
- `npx tsc -b packages/three-surface-poc-core packages/polaris-generation-core`: clean, no output.
- `npx tsc --noEmit -p apps/three-surface-poc`: clean, no output.
- `npm test` (full suite): **1 failed | 135 passed | 3 skipped (139 files)**,
  **1 failed | 1812 passed | 3 skipped (1816 tests)**. The one failure is
  `apps/three-surface-poc/src/production-reobserve.test.ts`'s "keeps served
  bytes and asOf stable when the same capture is rebuilt across wall-clock
  instants" — `Test timed out in 5000ms`. Re-run in isolation
  (`npx vitest run apps/three-surface-poc/src/production-reobserve.test.ts`):
  **4/4 passed**, confirming this is the known load-timeout artifact the PR
  describes, not a regression from this change.
- `packages/three-surface-poc-core/src/evidence-population.test.ts`: 8/8
  passed on its own, and I ran my own rule-6 mutation beyond the two the PR
  recorded (finding 3) — reverted cleanly.
- `python3 scripts/check_governance.py`: **32 OK, 20 WARN, 0 FAIL (52
  checks)** — matches the PR's claim; all WARNs are pre-existing/advisory
  (CG-19b, CG-22b, CG-23, CG-24, CG-27 items unrelated to this diff).
- `python3 scripts/check_evidence_currency.py`: exit 0. Confirmed via
  `echo $?` after the run. It is a read-only drift report over 113 tracked
  `docs/evidence/*.json` files; the new record does not appear in its
  drift/actionable listing (i.e., it classifies as `unknown`, matching the
  PR's claim, since its subjects are scratch capture files never committed
  to the tree).

## Overall assessment

The new module itself is well-built: pure, narrowly-typed, honestly
commented about what it does and does not read, exported cleanly through
`index.ts`, and its test suite mostly does what it says (hard-coded
literals, `beforeAll` fixtures, two recorded rule-6 mutations that do fail as
claimed). Governance and typecheck gates are clean, and the known
`production-reobserve.test.ts` flake is correctly identified and does not
reproduce in isolation.

The REVISE is for two things, both concrete: (1) the acceptance clause
"every retained page-size evidence record carries a population block" is not
met — only one of at least 10 retained page-size-bearing evidence records
(by my own denominator, `grep -l '"polaris-direct.html"' docs/evidence/*.json`)
carries the block, including the flagship lane-A record itself, and this
shortfall against the bead's own literal acceptance text is not disclosed
anywhere in the PR body, bead comment, or evidence record; and (2) my own
independent rule-6 mutation (removing HTML-entity decoding) survived the
full test suite, showing the decode step's stated purpose is not actually
covered despite the PR's rule-6 claims. Neither finding requires touching
`model.ts`/`polaris.ts`/`routes.ts`; both are fixable within the new
evidence-population module/test and by either widening the record's scope
or explicitly disclosing and following up on the narrower one actually
delivered.
