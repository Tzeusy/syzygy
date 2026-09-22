# Fresh-context adversarial review — PR #63 (syzygy-u05.8 slice 1)

Reviewer: fresh-context agent, no prior session state.
Subject: `Tzeusy/syzygy` PR #63, branch `agent/syzygy-u05.8-slice1`, head
`5cb8ab1119a9bb53cc4f7d1231fb73ff8ac20065`.
Method: `git worktree add` at the head commit, `npm ci` inside the worktree,
read every changed file in full, cross-derived the claimed evidence numbers
independently by hand (Python) against the pipeline's own extractor source,
ran the generator script and diffed its output against the checked-in
evidence file, mutated two predicates and re-ran the unit tests, ran the
full test suite, the POC build, and the governance checker, and diffed the
governance checker's output against the branch's own parent commit to
isolate this PR's marginal effect. The PR branch itself was never modified;
all edits described below were made and reverted inside the review worktree
only.

## Verdict

CONFIRM

## Scope of the single commit

`git diff 5cb8ab1119a9bb53cc4f7d1231fb73ff8ac20065~1 5cb8ab1119a9bb53cc4f7d1231fb73ff8ac20065 --stat`
touches exactly 7 files, 721 insertions, 0 deletions — identical to the file
list the PR description claims:

```
apps/three-surface-poc/src/pwb-n8-synthetic-corpus-coverage-matrix-main.ts | 132 ++
docs/evidence/pwb-n8-synthetic-corpus-coverage-matrix-2026-09-23.json      | 282 ++
package.json                                                              |   1 +
packages/three-surface-poc-core/src/fixtures/synthetic-corpora.ts         | 107 ++
packages/three-surface-poc-core/src/index.ts                              |   2 +
packages/three-surface-poc-core/src/synthetic-corpus-coverage.test.ts     | 103 ++
packages/three-surface-poc-core/src/synthetic-corpus-coverage.ts          |  94 ++
```

Confirmed: no diff to `project-shape-extraction.ts` or
`project-shape-manifest.ts` (the pipeline under measurement) between the
same two commits — the extractor really is unmodified. Confirmed: no diff
to `model.ts`, `polaris.ts`, `routes.ts`, or `main.ts` (the PR's "does not
touch" claim). Confirmed: nothing under `openspec/**` or `.syzygy/**`.

## 1. Is the 0/27 figure and each gap classification actually derived from running the real pipeline?

Yes. `packages/three-surface-poc-core/src/synthetic-corpus-coverage.ts:75`
calls `extractClass(cls, corpus.path, corpus.text)` — the same
`extractClass` exported at `project-shape-extraction.ts:582`, which
dispatches to the real per-class extractors (`extractPrinciples`,
`extractSuccessCriteria`, `extractCraftPolicies`, `extractProjectAccountSections`,
`extractCatalogEntries`, `extractDesignContracts`, `extractBaselineSpec`,
`extractTopologyComponents`, `extractRosterIdentity`, at
`project-shape-extraction.ts:359-577`). No mock, no stub, no shortcut. The
`repairFor` classifier at `synthetic-corpus-coverage.ts:57-71` reads only
the extractor's real `failure.reason` and compares it to the corpus's own
`targetClass` — it does not special-case any specific corpus.

I independently re-derived every one of the 27 cells by hand-tracing the
extractor source against each fixture's literal text and basename (not by
reading the evidence JSON), then cross-checked with a Python script over
the checked-in evidence JSON. Both agree, and both agree with the PR's
claimed distribution:

```
total 27
{'profile-row': 19, 'code-path': 3, 'unclassified': 5, 'extracted': 0}
```

Trace of the three "target class" cells (the ones the PR calls out
specifically):

- `principle-bullet-list` (`about/heart-and-soul/vision.md`, basename
  `vision.md`) / class `principle`: `extractPrinciples` admits the
  basename, finds heading "Non-Negotiable Rules" (matches
  `VISION_HEADINGS.principles`), finds 3 top-level list items, then fails
  at `if (!item.ordered) return failed('malformed-list', cls, item.line,
  'not a decimal-list item')` — the fixture's items are unordered bullets.
  Matches the test's expected `malformed-list` / `not a decimal-list item`
  / `code-path` exactly.
- `success-criterion-table` (`v1.md`) / class `success-criterion`:
  `extractSuccessCriteria` admits the basename, finds heading "Success
  Criteria" (`V1_HEADINGS.success`), calls `topLevelListItems` on a section
  whose only content is a pipe table (no `-`/`*`/digit-prefixed lines) →
  `list.length === 0` → `failed('malformed-list', cls, h.index+1, 'no
  top-level list')`. Matches exactly.
- `craft-policy-prose` (`README.md`) / class `craft-policy`:
  `extractCraftPolicies` admits the basename, finds heading "Reading Order"
  (`CRAFT_POLICY_HEADING`), calls `tablesOf` on prose paragraphs → no table
  → `failed('malformed-row', cls, heading.index+1, 'no table')`. Matches
  exactly.

Trace of the "always profile-row" claim: `baseline-spec` requires path
matching `^openspec/specs/([^/]+)/spec\.md$` (none of the three synthetic
paths match); `topology-component` requires basename `components.md`;
`roster-identity` requires path matching `^roster/([^/]+)/butler\.toml$`.
None of the three fixture paths (`about/heart-and-soul/vision.md`,
`about/spec-and-spine/v1.md`, `about/craft-and-care/README.md`) match any
of these, so all three are `unsupported-source` on all three corpora — 9 of
the 19 profile-row cells. The other 10 profile-row cells are the remaining
six classes gated on a basename the corpus doesn't carry (e.g. `principle`
gated on `vision.md` fails `unsupported-source` on the two corpora whose
basename isn't `vision.md`), each individually verified against its
extractor's own basename check.

The 5 "unclassified" cells are exactly the cases where a corpus's basename
coincidentally satisfies a class's admission gate for a class the corpus
was not authored for, and the extractor gets in far enough to fail on
missing/absent content rather than shape:

```
principle-bullet-list / project-account-section: missing-heading "What Butlers Is"
principle-bullet-list / success-criterion:        missing-heading "What Success Looks Like"
success-criterion-table / project-account-section: missing-heading "What v1 Ships"
success-criterion-table / catalog-entry:           missing-heading "Core Infrastructure"
craft-policy-prose / design-contract:              missing-heading "Index"
```

All five verified against the corresponding extractor's literal heading
requirements. None of these five carry a `repairKind`, matching
`repairFor`'s logic (only `unsupported-source` → `profile-row`, or
`cls === corpus.targetClass` → `code-path`; everything else falls through
to `undefined`).

Conformance-literal discipline (guardrail: expected values must be
hard-coded literals, never imported from the module under test): confirmed
in `synthetic-corpus-coverage.test.ts` — every expected string
(`'malformed-list'`, `'not a decimal-list item'`, `'code-path'`, etc.) is a
literal in the test file. The only imports from production code are
`EXTRACTION_CLASSES`/`SYNTHETIC_CORPORA` (used to assert population size and
identity, not to assert outcomes) and the function under test itself.
Fixtures are built in `beforeAll` (`synthetic-corpus-coverage.test.ts:18-20`),
not at describe time, matching the "mutation that throws at describe time
reports zero tests and scores as survived" guardrail.

## 2. Rule 6 — mutated 2 predicates, both mutants killed

**Mutant A** — made a corpus match Butlers' actual shape so a cell should
extract.

File: `packages/three-surface-poc-core/src/fixtures/synthetic-corpora.ts`

```diff
-  '- Every claim must cite the source it came from.',
-  '- Never silently drop a failing check.',
-  '- Treat committed history as durable evidence, not a draft.',
+  '1. **Every claim must cite the source it came from.**',
+  '2. **Never silently drop a failing check.**',
+  '3. **Treat committed history as durable evidence, not a draft.**',
```

(the exact Butlers shape: bold-led decimal list, matching `LEADING_BOLD` and
the `item.ordered` check in `extractPrinciples`).

Result: `npx vitest run packages/three-surface-poc-core/src/synthetic-corpus-coverage.test.ts`
— 1 of 7 tests failed:

```
× principle-bullet-list: an unordered, non-bold list is Unknown under "principle" — a code-path gap, not admission
  AssertionError: expected 'extracted' to be 'unknown'
```

Confirms the test suite actually distinguishes a real extraction from a
gap — it isn't vacuously true. Reverted with `git checkout --`.

**Mutant B** — inverted the gap classifier (`profile-row` ↔ `code-path`).

File: `packages/three-surface-poc-core/src/synthetic-corpus-coverage.ts`

```diff
   if (extraction.failure.reason === 'unsupported-source') {
     return {
-      kind: 'profile-row',
+      kind: 'code-path',
       ...
     };
   }
   if (cls === corpus.targetClass) {
     return {
-      kind: 'code-path',
+      kind: 'profile-row',
       ...
     };
   }
```

Result: 4 of 7 tests failed (the three target-class tests each asserting
`'code-path'` now got `'profile-row'`, and the "always gated" test asserting
`'profile-row'` for `baseline-spec`/`roster-identity`/`topology-component`
now got `'code-path'`). Reverted with `git checkout --`.

Both mutants confirm the tests are load-bearing on both (a) the real
extraction outcome and (b) the classification logic, not just on structural
shape (field presence, array length).

## 3. Is the evidence JSON reproducible byte-for-byte by `npm run poc:pwb-n8-coverage-matrix`? Any forbidden `source`/`provenance`/`evidence`/`anchor` keys naming Polaris?

Reproducibility: copied the checked-in
`docs/evidence/pwb-n8-synthetic-corpus-coverage-matrix-2026-09-23.json`
aside, deleted it, ran `npm run poc:pwb-n8-coverage-matrix`. The script
wrote a file with a different name
(`pwb-n8-synthetic-corpus-coverage-matrix-2026-09-22.json` — the sandbox's
system clock reads 2026-09-22 in UTC, one day behind the "today" the
harness states; this is an environment artifact, not a PR defect, since the
script always names the file by the actual current date unless `--date` is
passed). Diffing the two JSON objects in Python with the `generatedAt` key
removed from both: **byte-identical**. `generatedAt` (an ISO timestamp) is
the only field that varies run-to-run, which is expected and appropriate
for a "when was this generated" field — every substantive field (corpus
text, cell outcomes, repair classifications, summary counts) is fully
deterministic. Restored the original file afterward (`git status --short`
is clean).

Forbidden-key sweep: `apps/three-surface-poc/src/polaris-authority-sweep.test.ts`
(unmodified by this PR) flags any line in `.syzygy/governance`, `openspec`,
`packages`, `apps`, `docs` matching
`^\s*["']?(source|authority|warrants?|primary|evidence|provenance|cites?|anchor)["']?\s*[:=]`
whose value names the Polaris surface. Ran it against the worktree with
this PR's new files present (evidence JSON, generator script, fixture,
coverage module) — **4/4 tests pass**, including the "no source/authority/
provenance field... names the Polaris surface" sweep. Manually confirmed
none of the evidence JSON's keys (`subject`, `bead`, `releasedBy`,
`dossier`, `generatedAt`, `generator`, `method`, `classes`, `denominator`,
`summary`, `corpora[].id/description/shape/targetClass/path/text/
denominator/extractedCount/unknownCount/cells[].class/outcome/count/
denominator/failureReason/failureDetail/repairKind/repairNote`) match the
flagged key-name pattern at all (`denominator`, `generator`, `class`,
`description` etc. are not in the flagged set); grepped the four new
source/evidence files for `authority|provenance|warrant` — zero hits.

## 4. Honest labeling — are "unclassified" cells truly not generality findings? Any overclaim?

Verified each of the 5 unclassified cells by hand (§1 above): all 5 are a
basename coincidentally admitted under an unrelated class, immediately
failing on missing headings the corpus was never authored to carry
(`project-account-section` wants "What Butlers Is"/"What v1 Ships" on a
`vision.md`/`v1.md`-shaped file; `catalog-entry` wants "Core Infrastructure"
h3 headings on a `v1.md` about something else; `design-contract` wants an
"Index" heading on a `README.md` about something else). None of these say
anything about container-shape generality — the module correctly declines
to attach a `repairKind` to them, and the PR text and bead comment describe
them accurately as "5 unclassified coincidental-basename misses ... not a
generality finding."

Checked the PR body and the 2026-09-22 17:45 bead comment on `syzygy-u05.8`
line by line against what the code and evidence actually show:

- "0/27 cells extracted" — matches (§1, independently re-derived).
- "19 profile-row / 3 code-path / 5 unclassified" — matches.
- "The pipeline was not changed to make any fixture pass" — matches (zero
  diff to `project-shape-extraction.ts`/`project-shape-manifest.ts`).
- "generated, not hand-written" — matches (`writeFileSync` in
  `pwb-n8-synthetic-corpus-coverage-matrix-main.ts:122`, and the byte-for-
  byte reproduction in §3 confirms it).
- "zero egress ... no git I/O, no authority gate" — confirmed: neither
  `synthetic-corpus-coverage.ts` nor `fixtures/synthetic-corpora.ts` import
  `fs`, `node:https`, `child_process`, or any git-reading module; the only
  I/O in the whole change is `writeFileSync` of the evidence file in the
  generator script, which is local and expected.
- "Does not touch model.ts, polaris.ts, routes.ts, or main.ts" — matches
  (§ "Scope of the single commit").
- Does not claim this generalizes beyond these three shapes, does not claim
  the profile-row gaps are trivial to fix, does not claim slices 2-4 are
  done. No overclaim found.

One non-blocking observation on the classifier's robustness (not a defect
in what's shipped, since it's fully verified correct for these 3 fixtures):
`repairFor` at `synthetic-corpus-coverage.ts:64-69` labels a cell
`code-path` whenever `cls === corpus.targetClass`, regardless of the
specific `failure.reason` — it doesn't require the reason to actually be a
shape-grammar failure (`malformed-list`/`malformed-row`). For all three
current fixtures this is safe because each target-class heading is present
and matches, so the only way to fail is a genuine shape mismatch. But if a
future fixture (slice 2+) accidentally misnamed its own target heading, the
same code path would mislabel a `missing-heading` failure as `code-path`
("only new parsing logic closes this") instead of flagging the fixture
itself as broken. Worth a narrower guard (`reason === 'malformed-list' ||
reason === 'malformed-row'`) before slice 2 adds more fixtures, but this is
advisory, not a finding against slice 1 as shipped.

## 5. `npm test`, `npm run build:poc`, `python3 scripts/check_governance.py`

`npm test` (full suite, at PR head, after `npm ci` in a fresh worktree):

```
Test Files  126 passed | 3 skipped (129)
     Tests  1724 passed | 3 skipped (1727)
  Duration  37.33s
```

Matches the PR's claimed "126 passed | 3 skipped test files, 1724 passed |
3 skipped tests, 0 failures" exactly. Read the summary line, not an exit
code.

`npm run build:poc`:

```
> tsc -b --force packages/cap1-core packages/cap1-daemon packages/three-surface-poc-core apps/three-surface-poc
```

No errors emitted, clean exit. This also validates the `index.ts` barrel
export addition (`export * from './fixtures/synthetic-corpora.js'` /
`export * from './synthetic-corpus-coverage.js'`) compiles and that the
generator script imports resolve through the built `@syzygy/
three-surface-poc-core` package (it's how `npm run poc:pwb-n8-coverage-matrix`
was able to run in §3).

`python3 scripts/check_governance.py`:

```
32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted
```

Matches the PR's claim ("32 OK, 20 WARN ... 0 FAIL") exactly. To isolate
this PR's marginal effect (rather than trust "all pre-existing" as
asserted), I checked out the branch's parent commit
(`5cb8ab1119a9bb53cc4f7d1231fb73ff8ac20065~1`, i.e. `dfb605c`) in the same
worktree and re-ran the checker: **identical 32 OK, 20 WARN, 0 FAIL**, and
the 17 individual CG-27 findings are the same `.syzygy/governance/
decisions/README.md` staleness items on both commits. This PR introduces
zero new governance findings. Restored the worktree to the PR head
afterward (`git status --short` clean).

`git diff --check` on the single commit: clean (exit 0), matching the PR's
claim.

## Summary

Every checkable claim in the PR description and bead comment was
independently reproduced from source, not merely read and trusted: the
0/27 figure and all three repair-kind counts were re-derived by hand from
the unmodified extractor code and cross-checked against the evidence JSON;
two independent mutants (a fixture whose shape actually matches Butlers',
and an inverted classifier) both correctly failed the test suite; the
evidence file regenerates byte-for-byte aside from its own timestamp; the
Polaris-authority sweep passes with the new files present and no forbidden
key names Polaris; the "unclassified" cells are genuinely not generality
findings; and the full test suite, build, and governance checker all match
the PR's stated numbers, with the governance checker additionally shown to
be unchanged from the branch's parent commit. No blocking issues found. One
advisory (non-blocking) note on `repairFor`'s classification robustness for
future fixtures is recorded in §4 for whoever picks up slice 2.
