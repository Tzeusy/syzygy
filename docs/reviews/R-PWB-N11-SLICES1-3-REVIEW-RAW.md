REVISE

1. **Central finding (blocking) — `scripts/check_evidence_currency.py:253,258,345,350`**: `sweep_evidence_records` and `sweep_mutation_records` enumerate `docs/evidence/*.json` via `evidence_dir.glob("*.json")` (working tree) and read each record's bytes via `path.read_text()` (working tree), instead of using the `read_bytes`/`make_git_reader(rev)` primitive already bound in the same functions (line 252, 344) and already used correctly by `sweep_reading_plans` (line 151-152) for population (a). This directly contradicts the script's own docstring (lines 8-10): "Digests are recomputed only from `git show <rev>:<path>` bytes (never the working tree...) so a report is valid only for the commit it names (AGENTS.md rule 7)." Demonstrated: `--rev 44c51b5` run inside the f3447908 working tree still enumerates 107 evidence files, not the true 106 at that rev, because the self-referential `n11-evidence-currency-first-run-2026-09-23.json` physically exists on disk regardless of `--rev`. Independently confirmed the true counts via a from-scratch git-object-only reimplementation: 106 at 44c51b5, 107 at f3447908, matching the tool's own numbers only when it happens to be run against a clean tree at the commit it's already checked out to. Beyond reproducibility, this is a soundness gap for populations (b)/(c) — 137 of the tool's records, effectively its entire deliverable: an uncommitted edit to an evidence record's stored digest is invisible to `--rev` pinning and would be read as if historically committed, which could produce a false "current" verdict from a dirty tree. No test (self-test or otherwise) exercises `--rev` against a historical commit with real `docs/evidence` content, so this went uncaught. **Repair**: replace both `evidence_dir.glob("*.json")` + `path.read_text()` pairs with `git ls-tree -r --name-only -z <rev> -- docs/evidence` (filtered to `*.json`, one path segment deep) plus `read_bytes(rel_path)`, mirroring `sweep_reading_plans`'s already-correct pattern.

2. **Minor — `pipeline.ts:54` `InvalidOutputReason` / `pipeline.test.ts`**: `digest-failed` has zero test coverage (only `parse-failed`, `schema-rejected`, `encode-failed` are exercised with hard-coded literal expectations) and appears structurally near-unreachable, since `digestCanonicalJson` re-runs `encodeCanonicalJson` on data that already passed the identical encode step moments earlier. Non-blocking — the PR's own description only claims coverage for the three reachable reasons and doesn't overclaim `digest-failed`. Repair (optional): either add a test via an injectable failure point or add a one-line comment noting the believed-unreachable status so a future reader doesn't chase it.

3. **Minor/architectural — `pipeline.ts:262-264`**: `detail = error.message.slice(0, 200)` is safe today because the only real adapter, `provider-draft.ts`'s `check()`, and `parse-json.ts`/`canonical-json.ts` throw only generic coded messages (confirmed by reading all three). But nothing in `pipeline.ts`'s types, docs, or `PipelinePorts.validate` contract constrains a *future* injected validator from embedding provider content or secrets into `Error.message`, which would then flow untouched into the durable `AttemptOutcome` record. Currently the only concrete `record` port implementation in the tree is the in-memory demo (`apps/three-surface-poc/src/polaris-generation/pipeline-demo.ts`), so there is no live persistence/render risk yet. Repair (optional): document the "no provider content in thrown messages" contract explicitly on `PipelinePorts.validate` or `AttemptOutcome`.

4. **Minor — rule-6 selftest robustness**: I added two independent mutations (digest-equality flip; digest-key regex broken so no leaf is ever recognized) beyond the script's own `--selftest`. Both were caught (exit 1), but the regex-break mutation surfaces via an uncaught `IndexError` traceback rather than a clean per-predicate assertion failure, meaning later fixtures in that run go unverified once the exception fires — the same class of gap AGENTS.md's own guardrail warns against ("a mutation that throws at describe time... build fixtures in beforeAll"). Non-blocking; repair is to wrap each fixture predicate independently so one broken predicate doesn't abort the rest.

5. **Non-blocking, unrelated to this diff — `npm test`**: The PR/bead claims "125 test files passed, 3 skipped (1719 tests, 3 skipped)," implying zero failures. My rerun (full suite, then isolated) reproducibly shows 1 file / 2 tests failing via `Error: Test timed out in 5000ms` in `apps/three-surface-poc/src/polaris-copy.test.ts`. Confirmed via `git diff 44c51b5 f3447908 --stat` that this file is completely untouched by the PR's 5-file diff, so this is a pre-existing, environment-dependent timeout unrelated to slices 1/3's reviewed code (matches the class of the already-separately-tracked, still-open `syzygy-1z3.28` flake bead, which this PR correctly and explicitly declines to address as out of scope). Flagging only because the unqualified test-plan checkbox is not reproducible as literally stated this session — recommend the PR note "environment-dependent, unrelated to this diff" rather than an unqualified pass count.

6. `build:poc` (exit 0), `check_governance.py` (32 OK, 20 WARN, 0 FAIL), and `check_evidence_currency.py --selftest` all reproduced exactly as claimed — no overclaim there.

7. Items 1 (arithmetic/denominators), 2 (no Butlers/daemon reads), 3 (Unknown discipline), and 6 (PWB-REQ-014 key sweep, reproducibility) all passed independent verification with no defects found, beyond what's captured in findings 1 and 5 above.

---

Full raw review text (for `docs/reviews/R-PWB-N11-SLICES1-3-REVIEW-RAW.md`):

```
# R-PWB-N11-SLICES1-3-REVIEW-RAW

Reviewed commit: f3447908f20837cf075751bc5f937f5a10d05697 (PR #68, branch agent/syzygy-u05.11-slices1-3)
Merge-base: 44c51b54054b7181e63f71917380faaa302a2df2
Verdict: REVISE
Date: 2026-09-23

## Scope

Fresh-context adversarial review of bead syzygy-u05.11 (N11) slices 1 and 3
only, per explicit task scope:
- Slice 1: scripts/check_evidence_currency.py (sha256 drift sweep over
  reading-plan anchors, docs/evidence/*.json records, and retained mutation
  records), plus docs/evidence/n11-evidence-currency-first-run-2026-09-23.json.
- Slice 3: typed InvalidOutputReason in
  packages/polaris-generation-core/src/pipeline.ts and its test additions.

Reviewed in a fresh worktree of the PR head, `npm ci` run first. PR branch
never modified; nothing committed or pushed from the review worktree.

## 1. Denominators and arithmetic (population b: docs/evidence/*.json)

Claim (PR body, bead comment, first-run JSON): 106 records total, 81 carry a
recognizable subject-digest key, current=6, drift=38, unknown=62 (6+38+62=106).

Re-derived independently with a from-scratch script
(independent_check.py) that reads population (b) via `git ls-tree -r
--name-only -z <rev> -- docs/evidence` + `git show <rev>:<path>` only --
zero working-tree reads, reimplementing the digest-leaf walk from scratch
rather than importing the PR's module (AGENTS.md rule 2, second method).

At rev 44c51b5 (the recorded first-run commit): independent script produced
denominator=106, carriesDigestKey=81, current=6, drift=38, unknown=62 --
EXACT MATCH to the PR's claimed numbers.

Arithmetic sanity: 81 records carry a digest-ish key, but only 44 (6+38)
resolve to an in-tree subject; the other 37 have a key but no leaf resolves
to a subject present in the git tree at that rev (unresolved subject path,
or resolved path absent from the tree) and are correctly folded into
"unknown" alongside the 25 records with no digest-ish key at all
(25+37=62). This is internally consistent, not a bug.

Sampled 5 drift records in full and adjudicated each:
- docs/evidence/polaris-pipeline-synthetic-verification-2026-09-13.json --
  names packages/polaris-generation-core/src/pipeline.ts by digest; this
  PR's own commit c0b4b7b modified pipeline.ts, so the record now
  legitimately drifts. TRUE byte drift, correctly resolved.
- docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json -- drifted
  subjects trace to review2..review7's `reviewed_files_at_that_commit` flat
  digest maps, explicitly a historical "as of that commit" snapshot. Drift
  here is inherent by design, not actionable staleness -- the sweep's
  "N/M mismatch" text is not false, but it does not disambiguate this class
  from actionable drift. Non-blocking, soft finding.
- docs/evidence/pwb-p2-4-classification-mutation-run-2026-09-04.json -- a
  genuine rule-6 mutation record for
  packages/three-surface-poc-core/src/content-classification.ts, correctly
  resolved via the "file" sibling key. TRUE, actionable drift (needs
  re-run) -- the intended positive use case.
- docs/evidence/polaris-generator-approval-offer-2026-09-12.json and
  polaris-generator-rfc1-4-coverage-2026-09-12.json -- drifted subjects are
  append-only governance ledgers
  (.syzygy/governance/decisions/DECISION-HISTORY.md,
  ACCEPTANCE-ACT-RECORD.md) and RFC/openspec docs; legitimate ~11-day
  evolution, not mis-resolution.

No mis-resolved subject paths or false drift/current claims found in the
sample. All 5 are true byte drift with correct subject resolution; the
tool's binary current/drift/unknown taxonomy doesn't distinguish
"actionable staleness" from "expected historical/append-only drift," which
is a usability gap, not a VIS-2 falsehood.

## 2. Butlers / live-daemon reads

Population (a) (reading-plan anchors) always reports not-measured/Unknown
with a stated reason ("subject text is Butlers repository body content...
never stored in the Syzygy git tree"), and the sweep code path for (a)
(sweep_reading_plans) only ever calls make_git_reader/read_bytes against
the Syzygy repo itself (apps/three-surface-poc/src/polaris-reading-plan.ts).
No subprocess, socket, or HTTP call anywhere in the script targets a
Butlers repository or a running daemon. Confirmed clean.

## 3. Unknown discipline (never zero, never green)

Confirmed: 62/106 records in population (b) are Unknown, none miscounted
as passing. A record with no digest-ish key, or a key whose leaf(s) never
resolve to an in-tree subject, is Unknown, never zero-drift. No instance
found of a no-evidence case being reported as clean/current.

## 4. Rule 6 -- selftest and independent mutations

Built-in `python3 scripts/check_evidence_currency.py --selftest` passes:
"selftest: all fixture predicates behaved as asserted (mutate-and-confirm-
fails, rule 6)".

Added two independent mutations beyond the script's own fixtures:
- mut1.py: `if sha256_hex(current) == leaf["digest"]:` flipped to `!=`.
  --selftest correctly failed with 2 clear assertion messages (old:
  `== leaf["digest"]`, new: `!= leaf["digest"]`).
- mut2.py: DIGEST_KEY_RE broken (`sha[_-]?256` ->
  `sha[_-]?256_NEVER_MATCH`, `digest` -> `digest_NEVER_MATCH`), so no leaf
  is ever recognized. --selftest failed (exit 1) but via an uncaught
  IndexError traceback rather than a clean per-predicate assertion list --
  a minor robustness gap: later fixture predicates in that run go
  unverified once the exception fires, the same class of gap AGENTS.md's
  own notes-to-self warn against for describe-time throws.

Both mutations were caught, satisfying rule 6's letter; mut2's crash mode
is a non-blocking repair item.

## 5. Central finding: --rev is not honored for populations (b)/(c)

scripts/check_evidence_currency.py:253 --
`files = sorted(evidence_dir.glob("*.json"))` -- and :258 --
`data = json.loads(path.read_text(encoding="utf-8"))` -- inside
sweep_evidence_records; identically at :345 and :350 inside
sweep_mutation_records. Both functions bind `read_bytes, _ =
make_git_reader(rev)` (lines 252, 344) and use it correctly to resolve
SUBJECT bytes, but enumerate the evidence directory and read each
record's OWN bytes from the live working tree, not from `git show
<rev>:<path>`.

This contradicts the script's own docstring (lines 8-10): "Digests are
recomputed only from `git show <rev>:<path>` bytes (never the working
tree, never a live daemon...) so a report is valid only for the commit it
names (AGENTS.md rule 7)." sweep_reading_plans (population a, lines
151-152) gets this right, reading the plan file exclusively via
read_bytes(rev-pinned). sweep_evidence_records/sweep_mutation_records do
not extend the same discipline to enumeration or content.

Demonstrated concretely: running
`python3 scripts/check_evidence_currency.py --json --rev 44c51b5` inside
the f3447908-checked-out working tree returns denominator=107 (not the
true 106 at that rev), because
docs/evidence/n11-evidence-currency-first-run-2026-09-23.json (added by
this very PR, after 44c51b5) still physically exists on disk and gets
enumerated regardless of --rev. Cross-checked against an independent,
from-scratch git-object-only implementation (see item 1): true count at
44c51b5 is 106, true count at f3447908 is 107 -- confirming the script's
--rev flag is not honored for populations (b)/(c) enumeration or content.

Beyond reproducibility this is a soundness gap: since a record's own JSON
bytes (including its stored subject-digest value) are read from the
working tree rather than git-at-rev, an uncommitted edit to an evidence
record is invisible to --rev pinning and is read as if it were the
historically committed content -- a dirty-tree edit could produce a false
"current" verdict for a tool whose entire purpose is asserting trustworthy
currency (VIS-2 exposure). No test in this PR (the --selftest fixtures,
nor any other) exercises --rev against a historical commit with the real
docs/evidence population, so this went uncaught.

Repair: in both functions, replace the working-tree enumeration/read with
`git ls-tree -r --name-only -z <rev> -- docs/evidence` (filtered to
*.json, one path segment below docs/evidence) plus `read_bytes(rel_path)`
for content -- exactly the pattern already used for subject-byte
resolution in the same two functions, and already used correctly by
sweep_reading_plans.

This is the review's one blocking finding: mechanical, narrowly scoped,
and fixable by reusing machinery already present in the same file, but it
must be fixed before this tool can be trusted as the rev-pinned currency
oracle its own docstring and this PR's description claim it to be.

## 6. pipeline.ts typed InvalidOutputReason

packages/polaris-generation-core/src/pipeline.ts:54:
`export type InvalidOutputReason = 'parse-failed' | 'schema-rejected' |
'encode-failed' | 'digest-failed';`

Confirmed `stop: (reason: StopReason) => never` (line 140, throws
PipelineStop) always throws -- no fallthrough after the catch block at
lines 245-268.

Tests (pipeline.test.ts) cover parse-failed, schema-rejected, and
encode-failed with hard-coded literal expectations, e.g.:
`expect(h.fullOutcomes).toEqual([{ kind: 'invalid-output', usageUnits: 1,
reason: 'parse-failed', detail: 'Bounded JSON rejected: duplicate-key'
}]);` -- literals, not imported from the module under test, matching
AGENTS.md's conformance-literal guardrail.

digest-failed has zero test coverage and is structurally near-unreachable:
digestCanonicalJson (canonical-json.ts) internally re-runs
encodeCanonicalJson on data that already passed the identical encode step
moments earlier via a deterministic, idempotent canonical encoder. Not
claimed as tested by the PR description (which lists only the three
reachable reasons) -- not an overclaim, but worth a comment or an injected
failure-path test.

Error-message safety: read parse-json.ts and canonical-json.ts in full --
both throw only generic coded messages ("Bounded JSON rejected: ${code}",
"Canonical JSON rejected: ${code}"), explicitly documented as containing
"neither provider content nor property names." Read provider-draft.ts's
check() -- throws only generic messages ("invalid-string",
"invalid-structure", "invalid-property", etc.), never embedding actual
values. For the currently wired adapter and validators, the
`detail = error.message.slice(0, 200)` truncation at pipeline.ts:262 is
safe.

Structurally, though, nothing in PipelinePorts.validate's type or in
AttemptOutcome constrains a future injected validator from putting
provider content or secrets into Error.message, which would flow
unfiltered (truncated to 200 chars) into the durable record. Traced where
AttemptOutcome flows: the only concrete `record` port implementation in
the tree is apps/three-surface-poc/src/polaris-generation/pipeline-demo.ts,
an in-memory array push, not persisted or rendered anywhere outside that
demo -- no live persistence/render risk today. Recommend documenting the
"no provider content in thrown messages" contract explicitly, non-blocking.

## 7. PWB-REQ-014 evidence-key sweep and reproducibility

Read apps/three-surface-poc/src/polaris-authority-sweep.test.ts:117-132 for
the exact key-matching regex (source|authority|warrants?|primary|evidence|
provenance|cites?|anchor, exact key match combined with a Polaris-surface
regex on the same line). Recursively scanned
docs/evidence/n11-evidence-currency-first-run-2026-09-23.json for every
key; the only source/provenance/evidence/anchor-adjacent keys are
structural ("anchors", "populationA_readingPlanAnchors",
"populationB_evidenceRecords"), no exact match, and the file makes no
Polaris-surface reference. Clean.

Reproducibility: ran `check_evidence_currency.py --json` twice at default
HEAD -- byte-identical. Compared the live default-HEAD run against the
recorded first-run file: resolvedCommit differs (f3447908 live vs.
44c51b5 recorded) and counts differ (107/5/39/63 live vs. 106/6/38/62
recorded), because HEAD has since gained a commit that both added the
self-referential evidence file and modified pipeline.ts (flipping the
synthetic-verification record's pipeline.ts subject from current to
drift). This difference is explicitly disclosed in the PR body and bead
comment ("First run recorded... at HEAD 44c51b5"), so it is not a hidden
discrepancy -- it is exactly the --rev-pinning behavior the tool intends,
undermined in practice by finding 5 above.

## 8. Test/build/governance battery (task item 7)

- `npm test`: reproducibly 1 file / 2 tests FAIL --
  apps/three-surface-poc/src/polaris-copy.test.ts, both
  "Error: Test timed out in 5000ms" (lines 206, 270), reproduced both in
  the full suite and in isolation. `git diff 44c51b5 f3447908 --stat`
  confirms this file is untouched by the PR's 5-file diff (only
  docs/evidence/n11-evidence-currency-first-run-2026-09-23.json,
  packages/polaris-generation-core/src/{index.ts,pipeline.ts,
  pipeline.test.ts}, scripts/check_evidence_currency.py changed) --
  pre-existing, environment-dependent timeout unrelated to slices 1/3,
  matching the class of the already-separately-tracked, still-open
  syzygy-1z3.28 flake bead (which this PR correctly declines to address,
  out of its stated scope). The PR/bead's unqualified "125 test files
  passed... 3 skipped" (implying 0 failures) does not reproduce as
  literally stated this session; non-blocking given it's demonstrably
  outside the diff, but worth disclosing as environment-dependent rather
  than an unqualified pass.
- `npm run build:poc`: exit 0, clean. Matches claim.
- `python3 scripts/check_governance.py`: "32 OK, 20 WARN, 0 FAIL (52
  checks)". Exact match to claim.
- `python3 scripts/check_evidence_currency.py --selftest`: "selftest: all
  fixture predicates behaved as asserted". Matches claim.

No overclaim found in the PR body or bead comment beyond the npm test
discrepancy in item 8, which is disclosed here as unrelated to the
reviewed diff.

## Verdict rationale

REVISE, not CONFIRM WITH EXCEPTIONS, because finding 5 is not cosmetic: it
falsifies the tool's own stated contract (its docstring's explicit rule-7
claim) for populations (b) and (c), which constitute the entirety of the
tool's practical evidence-sweep surface (137 of its records), and creates
a genuine soundness gap (dirty-tree edits bypassing --rev pinning) in a
tool whose sole purpose is asserting trustworthy, commit-pinned currency.
The repair is small and mechanical -- reuse the make_git_reader/read_bytes
primitive already bound in both functions, exactly as sweep_reading_plans
already does -- so this should be a fast fix-and-reconfirm, not a redesign.
Findings 2-4 and 6 are non-blocking and can land with the fix or as
fast-follows at the owning lead's discretion; finding 8's npm test
discrepancy is unrelated to this diff and should not block on its own.
```

**Files referenced**: `/tmp/claude-1000/-home-tze-GitHub-syzygy/ccd96075-5583-47ef-bd84-510b69d24ac7/scratchpad/pr68-review/scripts/check_evidence_currency.py` (lines 8-10, 64-81, 151-172, 251-274, 343-366), `/tmp/claude-1000/-home-tze-GitHub-syzygy/ccd96075-5583-47ef-bd84-510b69d24ac7/scratchpad/pr68-review/packages/polaris-generation-core/src/pipeline.ts` (lines 52-58, 140, 245-268), `packages/polaris-generation-core/src/pipeline.test.ts`, `packages/polaris-generation-core/src/parse-json.ts`, `packages/polaris-generation-core/src/canonical-json.ts`, `packages/polaris-generation-core/src/provider-draft.ts`, `apps/three-surface-poc/src/polaris-generation/pipeline-demo.ts`, `apps/three-surface-poc/src/polaris-copy.test.ts`, `docs/evidence/n11-evidence-currency-first-run-2026-09-23.json`. No files were modified, committed, or pushed in the review worktree.
