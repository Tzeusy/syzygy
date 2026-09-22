# Review — PR #68 N11 slices 1+3, confirmation
Reviewed commit: 73b7f374d6cc4dd4f7138c8cbeb991e0aeb42c00
Verdict: CONFIRM

Fresh-context confirmation review (CC-REV-4) of the three repair commits
(8992715, 23447f3, 73b7f37) landed on top of f3447908 in response to the
prior REVISE review
(R-PWB-N11-SLICES1-3-REVIEW-RAW.md). Reviewed in a detached worktree at
`73b7f37` (`git worktree add --detach ... 73b7f37`, `npm ci` run first).
Nothing committed, pushed, or left dirty in the review worktree — confirmed
clean (`git status --porcelain` empty) both before writing this file and
after every mutation test below (each mutation was reverted with
`git checkout --`).

## 1. Finding 1 (blocking): `--rev` now honored for populations (b)/(c)

**Repaired.** `scripts/check_evidence_currency.py` commit 8992715 adds
`list_top_level_json_at_rev()` (lines 255–281), which enumerates
`docs/evidence/*.json` via `git ls-tree -r --name-only -z <rev> -- <dir>`
filtered to one path segment, and both `sweep_evidence_records` (l.384) and
`sweep_mutation_records` (l.496) now read every record's own bytes through
the same rev-pinned `read_bytes` closure used for subject resolution —
`Path.glob`/`path.read_text` are gone from both functions.

Verified three independent ways, not just by reading the diff:

- **Direct demonstration** (mirroring the original reviewer's repro): added
  an uncommitted extra file `docs/evidence/zzz-uncommitted-test.json`, ran
  `--json --rev 23447f358` — denominator stayed **107**, not 108. Removed
  the file, worktree clean again.
- **Rule 6, reintroducing the exact original bug**: mechanically patched
  `sweep_evidence_records` back to `sorted((repo_root/evidence_dir_rel).glob("*.json"))`
  + `path.read_text()` (syntax-checked via `ast.parse`) and re-ran
  `--selftest`: it now fails with exactly 3 assertions, all inside the new
  `rev_pinned_enumeration_ignores_working_tree` check ("must count only the
  committed record...", "must read the committed digest bytes...", "a naive
  working-tree glob must see 2 files ... or this fixture cannot distinguish
  the fix from the bug it repairs"). `git checkout --
  scripts/check_evidence_currency.py` afterward: `git status --porcelain`
  empty, `--selftest` passes again cleanly. This satisfies AGENTS rule 6
  (mutate the input, confirm the check fails, confirm a clean revert).
- **Rule 6, the original reviewer's second mutation**: re-broke
  `DIGEST_KEY_RE` to `sha[_-]?256_NEVER_MATCH|digest_NEVER_MATCH` (the exact
  mutation that produced an uncaught `IndexError` traceback and aborted the
  remaining checks in the prior review). This time: `selftest` reports
  **10 assertion-level failures across 10 independent checks**, explicitly
  naming `digest_leaf_sibling` and `digest_leaf_parent_key` as
  "raised and caught rather than aborting the run", and every other
  independent check (the rev-pinning check included) still ran and reported
  its own pass/fail rather than being skipped. This confirms repair item 4
  (selftest robustness) is also fixed, not just claimed.

No blocking issue remains here.

## 2. Denominators/counts re-derived independently (population b/c)

Ran the tool itself against `--rev 23447f358` (the tip after the first two
repair commits, matching the bead comment's stated measurement point):
`denominator=107, current=5, drift=39 (4 historical-only, 35
driftRecordsWithActionableDrift), unknown=63`; population (c) `denominator=31`.
Exact match to the claimed figures.

Independently counted the denominator with a from-scratch method, not the
tool under test (rule 4): `git ls-tree -r --name-only -z 23447f358 --
docs/evidence | tr '\0' '\n' | awk -F/ 'NF==3 && $NF ~ /\.json$/'` → **107**,
confirming population (b)'s denominator without importing the module.

Diffed the committed `docs/evidence/n11-evidence-currency-first-run-2026-09-23.json`
against a fresh `--rev 23447f358` run: byte-identical after pretty-printing
except the cosmetic `measuredOn.rev` string ("23447f358" vs. the full SHA I
passed vs. the full SHA the commit used) — `resolvedCommit` and every count
and record are identical. The committed first-run file is a faithful,
reproducible regeneration, not hand-edited.

## 3. Historical-by-design vs. actionable split — principled, no hidden drift found

Re-implemented `find_digest_leaves`'s historical-marking logic independently
with trigger-key provenance tracking, and confirmed it produces byte-for-byte
identical leaf lists (including the `historical` flag) to the real function
across the entire population-(b) corpus (0 mismatches over ~700+ leaves in
107 records) — so the analysis below is against the real logic, not an
approximation.

Across the whole corpus, only **three** distinct marker-key fragments ever
actually gate a leaf to `historical=True` (of the eleven in
`HISTORICAL_MARKER_KEY_FRAGMENTS`): `governing` (585 leaves, all inside one
record — `docs/evidence/polaris-generator-approval-offer-2026-09-12.json`,
which pins `"baseline": "<commit sha>"` and a `"governing": [...]` list of
`.syzygy/governance/contracts/candidates/*.md` digests as the exact bound
artifact set at that offer's commit — a genuine pinned-baseline packet, not
a live-tracked file needing re-verification); `reviewed_files_at_that_commit`
(63 leaves, the review-funnel snapshot pattern the prior review already
sampled and adjudicated as legitimate); and `sourceSha256AtCommit` (2 leaves,
a rule-6 mutation record's source digest pinned to the commit it ran at, the
exact pattern AGENTS.md's own guardrail describes). Confirmed the two
append-only-ledger leaves (`DECISION-HISTORY.md`, `ACCEPTANCE-ACT-RECORD.md`)
are both marked historical, and (via the diff's own
`_check_historical_classification` selftest fixture, read in full) that
ledger-basename detection is independently exercised outside a marker-key
context too.

Checked for the failure mode that would matter most — a common English word
in the fragment list (`baseline`, `governing`) silently suppressing real
drift on a live-tracked file — by tracing every occurrence of `baseline` in
the corpus: it appears widely as plain prose/commit-hash values (e.g.
`"baseline": "f4589e26..."`) but **never** as a key whose value is itself a
digest-map or digest-bearing list, so it never actually reaches the
leaf-classification code path; the fragment matches text but never gates a
real leaf. No instance found, across the full 107-record population, of an
actionable subject wrongly folded into "historical," and no
`driftClass: "historical-by-design"` record where a manual read of its
content disagreed with that label.

## 4. `pipeline.ts` failure-code carry-through and digest-failed unreachability

Failure-code carry-through (`pipeline.ts:264–296`): `invalidOutputReason` is
a single mutable local, assigned immediately before each fallible call
(`'parse-failed'` initial, then `'schema-rejected'` before `ports.validate`,
`'encode-failed'` before the first `encodeCanonicalJson`, `'digest-failed'`
before `digestCanonicalJson`) and read once in the `catch` block into the
durable `AttemptOutcome`. This is a correct last-assignment-wins state
machine — confirmed by re-reading the whole try/catch, not just the type
signature.

`digest-failed` unreachability: read `canonical-json.ts` in full (not just
the pipeline-side comment). `encodeCanonicalJson`'s only failure paths are
`invalid-limits` (constant, satisfied identically both calls),
`unsupported-value` (non-finite numbers — `JSON.parse` output is always
finite), `unsupported-object`/`unsupported-property`/`cycle` (Proxy, foreign
prototype, `__proto__`-as-own-property, non-enumerable descriptors, or a
cyclic reference — none of these can appear in a value freshly produced by
`JSON.parse`, and any of them present in the *original* `validated` would
already have thrown at the **first** `encodeCanonicalJson` call, producing
`encode-failed`, not reaching the digest step at all), and `byte-limit`/
`node-limit`/`depth-limit` (encoding is deterministic — sorted keys, fixed
JSON primitive spelling — so re-encoding the JSON.parse-reconstructed tree
under the identical limits reproduces byte-identical output and cannot newly
exceed a limit already satisfied). The comment's reasoning matches the code
exactly; the proof holds. This closes the prior review's non-blocking item 2
(documented rather than tested, one of the two options the prior review
explicitly offered).

The no-secrets contract (prior item 3) is now documented on both
`PipelinePorts.validate` and the `invalid-output` `AttemptOutcome` variant,
matching the prior review's suggested repair verbatim; re-confirmed
`parse-json.ts`/`canonical-json.ts` still throw only generic, content-free
messages and `provider-draft.ts`'s `check()` still never embeds values
(unchanged since the prior review, not re-read line-by-line this pass since
this diff didn't touch them).

## 5. Battery

- `python3 scripts/check_evidence_currency.py --selftest`: "all fixture
  predicates behaved as asserted across 10 independent checks" — clean, and
  additionally exercised under two reintroduced-bug mutations above (both
  caught, both reverted cleanly).
- `npx tsc -b packages/polaris-generation-core --force`: exit 0, clean
  (checked directly since `build:poc` doesn't include this package).
- `npm run build:poc`: exit 0, clean, matches claim.
- `npm test`: **125 files / 1719 passed, 3 skipped (1722)** — exact match
  to the claimed count, zero failures this run. `pipeline.test.ts` isolated:
  14/14 pass. The prior review's `polaris-copy.test.ts` timeout (outside
  this diff's 3 files, `syzygy-1z3.28`) did not reproduce this run —
  consistent with a pre-existing flake, not a regression; the bead's own
  second comment already discloses this correctly ("1 pre-existing
  unrelated ... timeout, file untouched by this diff") rather than repeating
  the unqualified original claim.
- `python3 scripts/check_governance.py`: **32 OK, 20 WARN, 0 FAIL (52
  checks)** — exact match to claim. All 20 WARNs are pre-existing,
  unrelated to `docs/evidence/*` or `polaris-generation-core` (CG-19b
  substrate pins, CG-22b/CG-23 allowlists, CG-24 selftest coverage, CG-27
  default-path claims in `.syzygy/governance/decisions/README.md` — none of
  which this diff touches).

## Verdict rationale

All four items from the prior REVISE are resolved: the one blocking finding
(item 1, `--rev` not honored) is fixed with a mechanically verifiable
correct implementation, independently re-derived and rule-6 confirmed
(including re-triggering the *exact* original bug on a live copy and
watching the new fixture catch it, then reverting to a clean diff); the
three non-blocking items (digest-failed coverage, no-secrets contract
documentation, selftest crash-mode robustness) are each addressed by one of
the repair options the prior review itself offered, and item 4's fix was
independently exercised against the prior review's own reproducing mutation.
The bonus historical/actionable drift-class split was checked for the
specific risk that matters (a common word silently promoting real drift to
"expected") and found sound over the full corpus, not just the three
unit-fixture cases. The evidence-currency first-run JSON is a reproducible,
non-hand-edited regeneration at the stated commit. Full battery reproduces
exactly as claimed, with no new WARN/FAIL and no regression.

## Method

Fresh detached worktree at `73b7f374d6cc4dd4f7138c8cbeb991e0aeb42c00`
(`/home/tze/GitHub/syzygy/.worktrees/pr68-confirm`), `npm ci` first, removed
at the end of this review. All git-tree reads used `git show`/`git ls-tree`
at pinned revs, never a live daemon or Butlers repository. Every mutation
applied to `scripts/check_evidence_currency.py` was syntax-checked
(`ast.parse`), exercised, and reverted with `git checkout --` before the
next step, confirmed via `git status --porcelain`. Independent
re-derivations (denominator via `git ls-tree`+`awk`; `find_digest_leaves`
trigger-key attribution) were written from scratch against the module's
public helpers (`DIGEST_KEY_RE`, `_looks_path_like`, `HEX64_RE`,
`_is_historical_marker_key`, `_classify_historical`), not by importing and
trusting `find_digest_leaves`/`classify_record` wholesale, and cross-checked
against the real function's output (0 mismatches) before being relied on.

**Files referenced**: `scripts/check_evidence_currency.py` (full, esp.
lines 8–21, 76–92, 219–281, 384–450, 493–525, 704–835),
`packages/polaris-generation-core/src/pipeline.ts` (lines 50–100, 264–300),
`packages/polaris-generation-core/src/canonical-json.ts` (full),
`packages/polaris-generation-core/src/pipeline.test.ts`,
`docs/evidence/n11-evidence-currency-first-run-2026-09-23.json`,
`docs/evidence/polaris-generator-approval-offer-2026-09-12.json`,
`docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json`. No files were
modified, committed, or pushed in the review worktree; every mutation was
reverted and confirmed clean before the next step.
