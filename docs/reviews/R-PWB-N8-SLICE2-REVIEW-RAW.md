# Review — PR #73 N8 slice 2
Reviewed commit: fe4f9e9a9e302d1f01af2d253b114fb589f74867
Verdict: REVISE

Reviewer: fresh-context agent, no prior authoring context.
Method: `git worktree add --detach` at the PR head, `npm ci` inside the
worktree, read `AGENTS.md` (verification rules 1-10, conformance-literal
rule, rule-6 mutation rule), `bd show`/`bd comments syzygy-u05.8`, `gh pr
view 73`, and `git diff origin/main...fe4f9e9` in full. Read the changed
files end to end, read `project-shape-extraction.ts`'s full
`EXTRACTION_FAILURES` union and every `failed(...)` call site, read the
bound spec text (`openspec/changes/polaris-project-wide-butlers-model/
specs/polaris-project-wide-butlers-model/spec.md`) and the two governance
JSON artifacts the PR cites, independently regenerated the evidence record
by running the built generator and diffed it byte-for-byte against the
committed JSON, diffed slice 1's evidence JSON against slice 2's cell by
cell, applied and reverted both rule-6 mutants myself, and ran the full
test suite, `build:poc`, and `check_governance.py`, reading their output
rather than their exit codes. All edits made during review were reverted;
`git status --short` is clean and the worktree is being removed after this
report.

## Findings

### 1. [Major] `SHAPE_MISMATCH_REASONS` omits `'malformed-toml'`, the genuine container-shape-mismatch reason for the one TOML-shaped class — the PR's own justifying claim is wrong for that class

`packages/three-surface-poc-core/src/project-shape-extraction.ts:33-40`
defines the full failure-reason union as seven members:
`unsupported-source, missing-heading, malformed-list, malformed-row,
malformed-toml, duplicate-key, ambiguous-leading-label`. The new constant
at `synthetic-corpus-coverage.ts:57`,
`const SHAPE_MISMATCH_REASONS = ['malformed-list', 'malformed-row'] as
const;`, and its governing comment (`synthetic-corpus-coverage.ts:30-39`)
assert these two are "the only two extraction failures a genuine shape
mismatch can produce" and that every other reason, explicitly including
"a malformed TOML table", "is a defect in the fixture's own authoring, not
a generality finding about the pipeline". That is incorrect for the
`roster-identity` class.

`extractRosterIdentity` (`project-shape-extraction.ts:548-575`) is gated on
`ROSTER_TOML = /^roster\/([^/]+)\/butler\.toml$/` (the basename/path
admission gate, analogous to `vision.md`/`v1.md`/`README.md`/
`components.md` for the other eight classes). Once that gate admits a
source, the walker looks for `[butler]` TOML tables and a `name` key; if
the body is shaped as something else entirely (YAML, JSON, a bullet list,
prose — i.e. exactly the class of "a container shape Butlers does not use"
that N8 exists to measure), it fails with `'malformed-toml'`
(`"no [butler] table"`, line 573) — the direct TOML analogue of "no
top-level decimal list" (`malformed-list`, line 411) or "no table"
(`malformed-row`, line 469). This is structurally the same failure class
as the two reasons the PR does include, not a "fixture-authoring defect"
like a misnamed heading or a missing bold lead.

No fixture in `SYNTHETIC_CORPORA` targets `roster-identity` (all three
target `principle`/`success-criterion`/`craft-policy`), so this does not
change the current 27-cell matrix — it is a dormant gap, not a live wrong
number. But it directly contradicts the classifier's own purpose (never
mislabel a genuine shape gap as a fixture defect): a future synthetic
corpus targeting `roster-identity` in a non-TOML shape — the natural next
fixture for exactly this slice's stated goal — would have its real
container-shape gap silently reclassified from `code-path` to
`unclassified` (no repair note at all) by the current code, and the false
"malformed TOML table … is a fixture-authoring defect" claim is now
written into a permanently retained, dated evidence record
(`docs/evidence/pwb-n8-synthetic-corpus-coverage-matrix-2026-09-23-slice2.json`,
`slice2GovernanceStop` field) as well as the code comment and the PR body.
Per the review brief's own question 1 ("are those really the only failure
reasons a container-shape mismatch produces?") — no.

Fix: add `'malformed-toml'` to `SHAPE_MISMATCH_REASONS`, or, if TOML is
deliberately out of scope for this slice, say so explicitly in the
comment/evidence record instead of the current unqualified "is a
fixture-authoring defect, not a generality finding" claim, which is false
for this class.

### 2. [Major] The evidence-record/comment claim "the admission basenames are proven byte-equal to the act-bound registry/policy JSON in project-shape-manifest.test.ts" is false

This sentence appears three times: `synthetic-corpus-coverage.ts:24-26`,
the PR body's governance-stop paragraph, and
`docs/evidence/…-slice2.json`'s `slice2GovernanceStop` field. I read
`project-shape-manifest.test.ts`'s only test that compares constants
against the registry/policy JSON
(`describe('constants bound to the adopted PWB artifacts')`, lines
573-583). It checks exactly three things against
`.syzygy/governance/declarations/adapter-registry/
POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` and
`.syzygy/governance/policies/
POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`:
`PWB_DISCOVERY_VERSION`, `PWB_ROOT_INDEX_PATH` (`policy.sourceAdmission.
phaseA.fixedSeedPaths`, which is `["about/README.md"]`), and
`PWB_INDEX_DEPTH` against `registry.entries[0].resourceLimits.
maxIndexDepth`. It never touches the nine extraction classes' own
admission basenames (`vision.md`, `v1.md`, `README.md`, `components.md`,
the `roster/*/butler.toml` pattern).

I greped both cited JSON files directly for those basenames: the registry
JSON lists only the nine class *names* (`"principle"`, `"success-
criterion"`, …, line ~139-147), never a basename; the policy JSON's only
path-shaped literal anywhere is the single fixed seed path
`"about/README.md"` (line 43). Neither document encodes `vision.md` →
`principle`, `v1.md` → `success-criterion`, etc. There is no test anywhere
in the package (I grepped every `*.test.ts` for these basenames plus
`registry`/`policy`) that establishes byte-equality between the per-class
admission basenames in `project-shape-extraction.ts` and any registry or
policy JSON. The half of the sentence anchored to the bound spec text
*is* correct and independently verified — I read
`openspec/changes/polaris-project-wide-butlers-model/specs/
polaris-project-wide-butlers-model/spec.md:33-34` and confirmed `principle`
is literally specified as "each top-level decimal-list item under
vision.md H2 'Non-Negotiable Rules'", matching the extractor exactly — so
the governance-stop's underlying conclusion (admitting a new container
shape needs a PWB-REQ-002 amendment, not a code change) still holds on
that citation alone. But the added "proven byte-equal to the act-bound
registry/policy JSON" clause is an unsubstantiated, false evidentiary
claim now baked into a retained dated evidence record, which this repo's
own culture (AGENTS.md rule 8, and the "Governance prose and docs" notes
on false/overstated citations) treats as a real defect regardless of
whether the conclusion it decorates happens to be right anyway.

Fix: drop the "proven byte-equal to the act-bound registry/policy JSON"
clause (the spec-text citation alone is sufficient and correct), or add
the missing test if that equality is actually meant to be enforced
mechanically.

### 3. [Informational, not a PR defect] One unrelated flaky test under full-suite load

`npm test` on this worktree showed 1 failure:
`apps/three-surface-poc/src/production-reobserve.test.ts > … keeps served
bytes and asOf stable when the same capture is rebuilt across wall-clock
instants` — `Test timed out in 5000ms`. This file is untouched by the PR
diff and has no dependency on `synthetic-corpus-coverage.ts`. Re-running
that file alone (`npx vitest run apps/three-surface-poc/src/production-
reobserve.test.ts`) passed cleanly (4/4, ~4.8s), consistent with resource
contention under the full parallel run rather than a regression from this
PR. My full-suite totals were 133 passed files / 1 failed / 3 skipped,
1768 passed / 1 failed / 3 skipped tests — different raw totals from the
PR's claimed "129 files … 1750 passed / 3 skipped / 0 failed" (likely
environment/parallelism variance in file scheduling, not a discrepancy in
which tests exist), but with the one flake isolated and explained, I found
no test-count evidence contradicting the PR's claim of a clean run.

## Verification of the PR's other claims (no issues found)

- **`repairFor` narrowing correctly implements the confirmed slice-1
  advisory.** Bead comment on `syzygy-u05.8` (2026-09-22 17:54) quotes the
  advisory verbatim: narrow to `malformed-list`/`malformed-row`. The diff
  at `synthetic-corpus-coverage.ts:87` does exactly that
  (`cls === corpus.targetClass && (SHAPE_MISMATCH_REASONS as readonly
  string[]).includes(extraction.failure.reason)`). Correctly implements
  the advisory as written (see Finding 1 for why the advisory itself,
  written against only the three list/table fixtures, didn't anticipate
  the TOML class).
- **Governed-plane discipline.** `git diff origin/main...fe4f9e9
  --name-status` touches exactly four files, all under `apps/` or
  `packages/` plus one new file under `docs/evidence/`; nothing under
  `openspec/**` or `.syzygy/**`. None of the four excluded shared-model
  files (`model.ts`, `polaris.ts`, `routes.ts`, and the unmodified
  `project-shape-extraction.ts`/`project-shape-manifest.ts`) were touched
  — confirmed directly from the diff, not merely asserted.
- **Slice 1's evidence record is untouched.** `git log --oneline --
  docs/evidence/pwb-n8-synthetic-corpus-coverage-matrix-2026-09-23.json`
  shows exactly one commit (the slice-1 merge, `0ea74d3`), and `git diff
  origin/main fe4f9e9 -- <that path>` is empty.
- **New evidence record is honest and re-derivable.** I ran `npm run
  build:poc` (clean) then `node apps/three-surface-poc/dist/pwb-n8-
  synthetic-corpus-coverage-matrix-main.js --date <scratch>` and diffed the
  output against the committed `…-slice2.json` (ignoring only
  `generatedAt`): byte-identical. I also diffed slice 1's and slice 2's
  committed JSONs cell-by-cell (corpus id, class, outcome, failureReason,
  repairKind): identical across all 27×2 cells, confirming the PR's "no
  visible movement" claim. Independently recomputed the summary from the
  raw cells: 0/27 extracted, 19 profile-row / 3 code-path / 5 unclassified
  — matches the record's own `summary` block and the bead comment.
- **Tests use hard-coded literal expected values** (conformance-literal
  rule): every new assertion in the slice-2 `describe` block
  (`synthetic-corpus-coverage.test.ts:117-176`) compares against literal
  strings (`'missing-heading'`, `'ambiguous-leading-label'`, `'code-path'`,
  `undefined`, etc.), never against a value imported from the module under
  test. Fixtures are declared as `const` outside `beforeAll`/`it`, but are
  plain literal objects (not derived from production code), so this does
  not trip the "mutation that throws at describe time" guardrail — no
  side-effecting call happens at describe time.
- **Rule-6 mutants.** I applied both mutants described in the PR myself
  (not merely read the PR's report of having done so):
  - Mutant A — reverted the guard to bare `cls === corpus.targetClass`:
    `npx vitest run … synthetic-corpus-coverage.test.ts` → exactly 2/10
    tests fail (the two new negative-case tests), 8 pass. Matches the PR's
    claim exactly.
  - Mutant B — inverted `SHAPE_MISMATCH_REASONS` to `['missing-heading',
    'ambiguous-leading-label']`: exactly 6/10 tests fail (the 2 negative
    cases, the "does not over-narrow" case, and the 3 slice-1 tests
    asserting `code-path` on the real corpora). Matches the PR's claim
    exactly.
  - Both mutants reverted; `git diff --stat` and `git status --short` came
    back empty after each revert, confirmed byte-identical to the
    pre-mutation file.
- **`npm run build:poc`** — clean, no errors.
- **`python3 scripts/check_governance.py`** — read the summary line, not
  the exit code: `32 OK, 20 WARN, 0 FAIL (52 checks)`, matching the PR's
  claim exactly. The 17 CG-27 findings are all pre-existing
  `.syzygy/governance/decisions/README.md` staleness items unrelated to
  this PR's files.

## Why REVISE and not CONFIRM WITH EXCEPTIONS

Both Major findings are specifically about the accuracy of the PR's central
epistemic claims — the exact two questions this review was asked to check
(is the narrowing's reason-set actually exhaustive; is the governance-stop
citation actually proven the way it says it is) — and both claims, as
written, are false in a way that is now embedded in a retained, dated
evidence record and a permanent code comment, not just PR-description
prose. Neither defect currently corrupts the computed 27-cell matrix (both
are dormant/citation-accuracy issues rather than live wrong numbers), and
the mechanically-checked parts of the PR (narrowing behavior for the three
shipped fixtures, hard-coded test literals, rule-6 mutation coverage,
build, full test suite modulo one unrelated flake, governance checker) are
all independently verified clean. This is why the verdict is REVISE rather
than REJECT: the fix is narrow (extend `SHAPE_MISMATCH_REASONS` or scope
the claim; correct or remove the false byte-equality citation), not a
redesign.
