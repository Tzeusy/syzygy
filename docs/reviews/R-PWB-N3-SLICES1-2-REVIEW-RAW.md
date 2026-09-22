# Review — PWB N3 slices 1-2 (PR #81)
Reviewed commit: 8965020d00ec7f480a3fa4cd1f4c5a28400f5853
Verdict: REVISE

## Commission

Independent, fresh-context review (CC-REV-1/4/6) of GitHub PR #81, which
implements bead `syzygy-u05.3` (N3, vision pursuit 2026-09-22) slices 1-2:
"resource ledger summary headroom + parse-pass margin guard." Scope: the
three-file diff `git diff origin/main...HEAD` —
`packages/three-surface-poc-core/src/resource-ledger.ts`,
`resource-ledger.test.ts`, `project-shape-model.test.ts`. Work done entirely
in `/home/tze/GitHub/syzygy/.worktrees/pr81-review`, detached at the reviewed
commit; no tracked file left modified (confirmed below). Acceptance
criteria: `bd show syzygy-u05.3` (slices 1-2 only: "summary() exposes
declared/observed/remaining for all seven limits plus the cost record; a
guard test fails when a registry pass identity pushes the worst source past
the declared margin and names the source"), plus AGENTS.md's "Epistemic and
change discipline", "Verification rules" and "Guardrails" at the reviewed
commit.

## Findings

### Finding 1 — `byLimit` renders "no evidence" as a false, internally-contradicted zero for three of the seven limits (VIS-2)

`resource-ledger.ts:93-108`'s own comment states that `maxSources`,
`maxBytesPerSource`, `maxIndexDepth`, `maxHumanResponseBytes` and
`maxMachineResponseBytes` are "evaluated and, on breach, recorded... this
ledger keeps no separate running count for them, so `observed` is the
highest value any breach already recorded here carries for that limit, or
0 when none has been recorded" (`observedFor`, `resource-ledger.ts:266-270`;
`observedFromBreaches`, `resource-ledger.ts:263-264`). The type
(`ResourceLimitUsage.observed: number`, `resource-ledger.ts:109-114`) gives
no way to distinguish "verified zero usage" from "never measured" — a
consumer sees the same shape either way.

This is not hypothetical: `project-shape-model.test.ts`'s own updated
fixture (the `byLimit` block added in this diff, around line 890) reports
`byLimit.maxSources = { declared: 512, observed: 0, remaining: 512 }` in
the *same* `ResourceLedgerSummary` object that reports `sourcesTraversed:
14` and `cost.bodiesRead: 14` two lines away. A reader of `byLimit.maxSources`
alone would conclude "0 of 512 sources used, full headroom" — false, by the
object's own other fields, in the very same test fixture the PR added. This
is exactly VIS-2's own violation example: "'spec-aligned ✓' computed from a
stale index... turn anything green... without current evidence"
(`.syzygy/governance/doctrine/vision.md:791-801`). It also directly recreates
the doctrine gap `syzygy-u05.3`'s own WHY section names as the problem this
bead exists to fix ("VIS-2 (the owner's 'what does this cost me' is an
Unknown rendered as nothing)") — trading "Unknown rendered as nothing" for
"Unknown rendered as a specific false zero" is not a fix, it is the same
doctrine violation in the opposite fail-open direction (never green, never
zero — AGENTS.md "Fail-closed polarity" guardrail).

The two response ceilings (`maxHumanResponseBytes`/`maxMachineResponseBytes`)
are a weaker instance of the same problem: I confirmed
`apps/three-surface-poc/src/routes.ts:135-141`'s `boundedResponse` computes
`observed`/`declared` entirely locally from `Buffer.byteLength(body)` and
never touches a `ResourceLedger` at all — no `ledger` parameter exists on
that function. So these two limits are, architecturally, never observed by
this ledger under any real request path (matching the pre-existing
AGENTS.md guardrail "A response-ceiling breach serves nothing and logs
nothing... no ledger... sees it"). Reporting `observed: 0, remaining:
declared` for these two is defensible as "genuinely unmeasured by this
component" rather than "known evidence discarded" (unlike `maxSources` and
`maxBytesPerSource`, see Finding 2) — but it is still surfaced as a bare
number indistinguishable from a true zero, which is the same VIS-2 gap at
lower severity.

**Suggested repair:** give `ResourceLimitUsage.observed` (and `remaining`) a
type that can carry "not measured" distinctly from `0` (e.g. `number |
'unmeasured'`, or an added `readonly measured: boolean` field), and populate
it honestly per limit. At minimum, fix the concrete case in Finding 2 below,
which removes the internal self-contradiction for `maxBytesPerSource`.

### Finding 2 — `maxBytesPerSource`'s true observed value is already sitting in the ledger's own `bodies` map and is not used

The code comment at `resource-ledger.ts:97-99` groups `maxBytesPerSource`
with "the five limits this ledger never counts itself," but this is not
accurate: `chargeBody` (`resource-ledger.ts:228-236`) already stores every
body's exact byte length in `bodies: Map<string, number>`
(`resource-ledger.ts:189`, keyed `path objectId`, set at line 234). The
largest single body already charged — the *exact* real value of
`maxBytesPerSource`'s "observed" — is one line away:
`Math.max(0, ...bodies.values())`, precisely mirroring the pattern already
used one function over for `maxParsePassesPerSource`
(`maxPassesOnOneSource = Math.max(0, ...passes.values())`,
`resource-ledger.ts:257`). Nothing new needs to be observed or counted
(consistent with the PR's own stated constraint, "pure projection... no new
observation and no new limit," `resource-ledger.ts:141-143`) — the data is
already there and simply isn't read. This is the concrete instance that
produces Finding 1's self-contradiction for `maxBytesPerSource` and should
be fixed regardless of how Finding 1 is resolved for the other limits.

**Suggested repair:** in `observedFor` (`resource-ledger.ts:266-270`), add a
`maxBytesPerSource` branch returning `Math.max(0, ...bodies.values())`,
same shape as the `maxTotalBytes`/`maxParsePassesPerSource` branches.

### Finding 3 (minor) — `maxIndexDepth`'s true value is a fixed constant, not a running count, and is also available but unused

`project-shape-observation.ts:544` compares a fixed import,
`PWB_INDEX_DEPTH` (from `project-shape-manifest.js`), against
`limits.maxIndexDepth`, and only calls `ledger.recordBreach` on breach
(`project-shape-observation.ts:544-546`). Unlike `maxSources` (a genuine
running count this ledger never receives except at breach),
`PWB_INDEX_DEPTH` is deterministic and always known — it is not "unmeasured"
in any real sense, it is simply not wired into `resource-ledger.ts`. Fixing
this needs a new value import (`PWB_INDEX_DEPTH` from
`project-shape-manifest.js`) into `resource-ledger.ts`, a small new coupling,
so I weight this below Finding 2 — but it is the same class of problem: real,
static evidence rendered as a possibly-false "0."

## Answers to the specific review questions

**(1) VIS-2 / fail-closed polarity for `observed: 0` on unmeasured limits:**
Yes, this is a real violation for `maxSources` and `maxBytesPerSource`
(Findings 1-2; the data is available and simply not used, so it is not
"absence of evidence," it is discarded evidence rendered as a specific false
claim). For `maxIndexDepth` it is a wiring gap over a constant (Finding 3).
For the two response ceilings it is a genuine architectural absence
(confirmed: `boundedResponse` never touches this ledger), so "0" there is
closer to defensible, but still collapses "never measured" into the same
numeric shape as "measured, zero" — the weaker instance of the same VIS-2
gap named above.

**(2) Is `summary()` still pure, with no new limit or observation?**
Yes. I read the full diff of `summary()`
(`resource-ledger.ts:252-297`): it derives `byLimit` and `cost` only from
existing closure state (`total`, `passes`, `breaches`, `bodies` indirectly
via `totalBytesNow`) and the seven identities in
`DECLARED_RESOURCE_LIMIT_IDENTITIES`, which is `as const satisfies readonly
(keyof PwbResourceLimits)[]` — I confirmed (via `grep`) there is no
`Date.now`, `process.*`, `Math.random` or `performance.*` call anywhere in
the file. `summary()` still does not mutate `breaches`/`bodies`/`passes`
(it copies `breaches` into a new array each call). No eighth limit is
invented; the "carries all seven declared identities, never an eighth" test
(`resource-ledger.test.ts`) checks this at runtime.

**(3) Is the guard test's 14-pass sequence and margin real, not invented?**
Yes, traced and independently re-derived. I temporarily instrumented
`chargePass` in `resource-ledger.ts` (one added `console.error` line, gated
on an env var) and ran the existing (pre-PR, unmodified) test
`project-shape-model.test.ts`'s "every body is taken from Git once, counted
once and validated once across both phases" test, which already asserted
`maxPassesOnOneSource: 14` before this PR. The captured charge order for
`about/README.md` was exactly: `utf8-and-nul-validation`,
`secret-private-key-fragments`, `secret-known-token-formats`,
`secret-credential-assignment`, `secret-credential-bearing-url`,
`markdown-code-context-mask`, `active-html-svg-script-handler`,
`unsafe-url-positions`, `phase-a-link-discovery`, [same four secret-*
passes repeated], `fact-and-precedence-extraction` — a byte-for-byte match
of the test's hand-typed `ABOUT_README_SEQUENCE`
(`resource-ledger.test.ts:363-379`). Same result for
`about/legends-and-lore/README.md` and `about/craft-and-care/README.md`
against `LEGENDS_README_SEQUENCE`/`CRAFT_README_SEQUENCE`, ending in
`declared-item-extraction` rather than `fact-and-precedence-extraction`
(consistent with `project-shape-extraction.ts:626`'s `ROOT_INDEX_PASS =
'fact-and-precedence-extraction'` applying only to the root index). I
reverted the instrumentation (`git checkout --`) before continuing. The
9-pass phase-A block traces to `classifyPhaseASeed` →
`detectSecrets`/`scanActiveContent` (`content-classification.ts:191-198`)
called from `project-shape-observation.ts:439-468`; the repeated 4-pass
secret block traces to phase B's `classifySource` →
`detectSecrets` (`content-classification.ts:363, 403-408`); the 14th pass
traces to `project-shape-extraction.ts:631-658`'s
`EXTRACTION_PASSES`/`ROOT_INDEX_PASS` charge. The margin (2 = 16 declared −
14 observed) is a real, computed number, not asserted independent of the
declared registry constant (`PWB_RESOURCE_LIMITS.maxParsePassesPerSource`,
`project-shape-observation.ts:80`).

**(4) Are expected values literals, never imports from the module under
test?** Yes. `TOTAL = 1357` (`project-shape-model.test.ts:860`) is a
hand-typed literal, and the added `byLimit` block's `declared` fields (512,
1048576, 16777216, 4, 16, 2097152, 8388608) are hand-typed number literals
matching `PWB_RESOURCE_LIMITS`, not references to the constant object
(consistent with the existing `bodiesCounted: 14` / `totalBytes: TOTAL`
style already in that fixture). `resource-ledger.test.ts`'s new describe
blocks build expected objects (`{ limit, declared, observed, remaining }`)
by hand throughout; no expected value is computed by calling an exported
helper of the module under test.

**(5) Rule-6 mutations, then revert.** I ran two, both against the
worktree's tracked source (not the test files), and reverted each with
`git checkout --` before the next step:
- **Reproducing the implementer's claimed mutation, against production
  code:** changed `PWB_RESOURCE_LIMITS.maxParsePassesPerSource` from `16`
  to `14` in `project-shape-observation.ts`, then ran
  `resource-ledger.test.ts -t "guard: maxPassesOnOneSource"`. Both guard
  tests failed as expected: the margin assertion (`16-14 !== 2` once the
  declared value itself is mutated) and the fixture builder (`chargePass`
  now throws at pass 15 during setup, since the hard limit is 14) — the
  guard is sensitive to the very quantity it names, not vacuous.
- **My own, independent mutation, against `resource-ledger.ts`:** flipped
  `remaining: declared - observed` to `remaining: declared + observed`
  (line 276). Ran `resource-ledger.test.ts` and `project-shape-model.test.ts`
  together: 3 failures, all `byLimit`-shaped assertion mismatches (the exact
  `remaining` fields the tests check), 49 other tests unaffected — confirms
  the new tests actually exercise `remaining`, not just `declared`/
  `observed`.
- Reverted both mutations with `git checkout --
  packages/three-surface-poc-core/src/project-shape-observation.ts` and
  `git checkout -- packages/three-surface-poc-core/src/resource-ledger.ts`
  respectively (plus the trace instrumentation from question 3). Final
  `git status --porcelain` is empty ("CLEAN", confirmed after the last
  revert).

**(6) Full battery.**
- `npm test`: 134 test files passed, 3 skipped; 1776 tests passed, 3
  skipped, 0 failed — matches the bd comment's reported numbers exactly.
- `npm run build:poc` (`tsc -b --force` across `cap1-core`, `cap1-daemon`,
  `three-surface-poc-core`, `apps/three-surface-poc`): clean, no errors.
- `python3 scripts/check_governance.py`: `32 OK, 20 WARN, 0 FAIL (52
  checks)` — matches the bd comment's reported numbers exactly; all WARNs
  are pre-existing, unrelated to this diff (default-path prose findings
  under `.syzygy/governance/decisions/`), none touch
  `packages/three-surface-poc-core`.

## Observations (not exceptions)

- The mutation test's inline comment (`resource-ledger.test.ts:381-385`)
  describes the appended `project-account-extraction` charge as "standing in
  for a future registry pass identity" — but `project-account-extraction` is
  already a real, currently-registered pass identity
  (`resource-ledger.ts:44`, charged elsewhere for the account section,
  `project-shape-extraction.ts:615`). The mutation is sound (it simulates an
  *existing* identity newly applying to *this* source, which is one honest
  way a 15th charge could arrive — L11-F2's WHY also names wholly new
  passes as a route), but "future" slightly overstates what's being
  simulated; "an identity not currently charged to this source" would be
  more exact.
- Slices 3-4 (human/machine surface rendering, population blocks in
  evidence records) are out of scope for this PR and untouched — correctly
  so, per the bead's own per-slice PR design.
- `DECLARED_RESOURCE_LIMIT_IDENTITIES`'s `as const satisfies readonly
  (keyof PwbResourceLimits)[]` guards against an invented eighth identity
  but does not by itself guard against a *missing* one at the type level;
  completeness is instead checked at runtime by the "carries all seven...
  never an eighth" test. Worth a comment noting this is intentional, since a
  future edit that both drops an identity from the array and drops the
  matching test assertion would compile clean.

## Commands run

```
cd /home/tze/GitHub/syzygy/.worktrees/pr81-review
git status; git rev-parse HEAD; git log --oneline -5
npm ci
git fetch origin main
git diff origin/main...HEAD --stat
git diff origin/main...HEAD -- packages/three-surface-poc-core/src/resource-ledger.ts
git diff origin/main...HEAD -- packages/three-surface-poc-core/src/resource-ledger.test.ts
git diff origin/main...HEAD -- packages/three-surface-poc-core/src/project-shape-model.test.ts
# trace instrumentation (added, traced, reverted):
RLREVIEW_TRACE=1 npx vitest run packages/three-surface-poc-core/src/project-shape-model.test.ts \
  -t "every body is taken from Git once" 2>&1 | grep RLTRACE
git checkout -- packages/three-surface-poc-core/src/resource-ledger.ts
# rule-6 mutation 1 (reproducing implementer's claim):
# edit PWB_RESOURCE_LIMITS.maxParsePassesPerSource 16 -> 14 in project-shape-observation.ts
npx vitest run packages/three-surface-poc-core/src/resource-ledger.test.ts -t "guard: maxPassesOnOneSource"
git checkout -- packages/three-surface-poc-core/src/project-shape-observation.ts
# rule-6 mutation 2 (my own):
# edit resource-ledger.ts: remaining: declared - observed -> declared + observed
npx vitest run packages/three-surface-poc-core/src/resource-ledger.test.ts packages/three-surface-poc-core/src/project-shape-model.test.ts
git checkout -- packages/three-surface-poc-core/src/resource-ledger.ts
git status --porcelain   # empty
npm test
npm run build:poc
python3 scripts/check_governance.py
```

bd `syzygy-u05.3` shown via `bd show syzygy-u05.3` for acceptance criteria;
VIS-2 read from `.syzygy/governance/doctrine/vision.md:791-801`.
