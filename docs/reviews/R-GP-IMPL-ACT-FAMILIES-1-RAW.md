# R-GP-IMPL-ACT-FAMILIES-1 — CC-REV-1 implementation review of syzygy-bpyt.8.4, round 1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 9f49b6cb
Subject: r1-review.diff sha256 c0fc8b9ed4e570d4040f32563ade0ac29109540c231a9fbbd2530693eb1a3415

Reviewer: independent fresh-context CC-REV-1 trust-boundary (consent gate) reviewer, default model. I did not author the change
and did not change it. No target-repository content was fetched or read: every world below is Syzygy's own checkout plus
in-memory overlays.

## 1. Subject identity checks

- [Observed] `sha256sum` of the subject file `lead/b84/r1-review.diff`:
  `c0fc8b9ed4e570d4040f32563ade0ac29109540c231a9fbbd2530693eb1a3415`. **Matches** the brief.
- [Observed] In a fresh scratch clone, `git diff b7697f6ac82c7fdb47c6858f70b23febdd3f505c 9f49b6cbec290c2cc0d3a94f3af820d83f5fb780`
  written to a file hashes to the same `c0fc8b9e…3a1415`. **Matches**; 7 files, 63255 insertions, 141 deletions.
- [Observed] `gh pr view 505` head is `9f49b6cbec290c2cc0d3a94f3af820d83f5fb780`, base `main`, state OPEN. The merge base of
  `9f49b6cb` with GitHub `main` (fetched into the clone as `gh/main`, tip `b7697f6a`) is
  `b7697f6ac82c7fdb47c6858f70b23febdd3f505c`, as the brief says.
- [Observed] The branch is three commits: `d7f7ea87` (refactor), `bc5f0f16` (differential script and runner), `9f49b6cb`
  (evidence). `git diff --stat bc5f0f16 9f49b6cb` touches only the three `docs/evidence/consent-act-family-*` files, so the
  code the lane's evidence ran at `bc5f0f16` is the reviewed code.
- [Observed] `packages/polaris-generation-consent/src/package-reader.ts` at `9f49b6cb` (via `git show`) hashes to
  `6efd4c4edc29f00c021f8723cc4b0716171c1ae05099892cef3fb21d6f13063c`, the digest both evidence records name for the new
  tree; at `b7697f6a` it hashes to `ebf5cbf468fd442289e11e390c9a7e3b20c39bdcd02e1a6214d096a52d0e3dc3`, the old-tree digest
  the differential names. `act-families.test.ts` hashes to `1c449f31…b284708`, the digest the parent-run record names.
- [Observed] `git diff --quiet b7697f6a 9f49b6cb -- AGENTS.md .syzygy openspec` exits 0: nothing governed is edited.

## 2. Clauses relied on (quoted)

- AGENTS.md (unchanged by the subject), verification rule 4: "Read a check's output, not its exit code, and check its
  denominator against the whole population." Rule 6: "Mutate the input and confirm the check fails, per predicate, before
  trusting it". Rule 9: "A claim of absence needs a sweep with a denominator." Rule 11: "An evidence record names its subject
  and the subject's digest; a record that names neither cannot be re-checked against the bytes it describes." Guardrail:
  "Fail-closed polarity: withdrawal defeats grant; future-dated evidence is stale; no evidence → Unknown." Guardrail: "Fresh
  `git worktree`: run `npm ci` inside it first, or `NodeNext` silently resolves `@syzygy/*` to the main checkout's
  `node_modules`." Hard prohibition: "An act's escalation triggers (doctrine or contract change, spec amendment,
  security/privacy/retention posture, scope) need a new owner act."
- `.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`, GP-Q0 part 1, lines 52–55:
  "\"Behavior-preserving\" means none of the following changes: — a rendered byte, a wire format, a refusal string or an exit
  code; … — a consent, security or retention decision." Line 62: "**Which ones:** pull requests touching class 1 (authority
  boundaries), class 3 (deterministic observation) or class 4 (security), and class-6 pull requests that remove an endpoint."
  Lines 64–66: "an old-versus-new differential over a mutated-record corpus that includes records with altered prose; — a
  rule-6 mutant for each predicate; — a non-blocking owner notice in the cycle report." Line 67: "Beads known to touch a
  class: … and `8.4`." Part 2, line 80 (row "How the consent gate recognizes an act"): "**Kept as is.** … Bead `8.4` never
  moves a byte-exact act onto field parsing". Part 3, lines 95–96: "Any change not listed here to what a gate accepts or
  refuses stops and returns to the owner."
- `.syzygy/governance/policies/craft-and-care/review-and-documentation.md`, CC-REV-1, line 31: "1. **authority boundaries** —
  write-universe, typed-authority table, adapter authorization (VIS-5, VIS-6);" line 37: "4. **security** — anything under
  SEC-1…SEC-5, auth surfaces, egress paths;" line 40: "6. **public interface** — machine-queryable endpoints, adapter
  contracts, anything an external consumer can depend on;" line 45: "**Class membership is contested by default and is never
  finally determined by the agent performing the change**"; line 49: "**The change record states** which classes the change
  touches, or \"none,\"".
- `.syzygy/governance/doctrine/security.md`, SEC-2, lines 42–45: "**SEC-2 — Portfolio data leaves owner-controlled
  infrastructure only through explicit, scoped consent.** No governed-project content, or anything derived from it, is sent to
  a store or service the owner does not control — model providers included — without explicit, recorded, per-project
  consent."
- `.syzygy/governance/doctrine/vision.md`, VIS-4, lines 168–170: "**VIS-4 — Humans steer the vision; agents shape within it.**
  Shape-defining changes always need the owner's sign-off; Syzygy and its agents may draft them, never adopt them."
- The bead `syzygy-bpyt.8.4` (read with `bd show --json`, no mutation): acceptance criteria "1. Three bespoke families
  expressed as form rows; one sweep implementation. 2. package-reader and gate-acts suites pass unchanged; refusal strings
  identical (golden). 3. Fresh rule-6 run, every row and sweep mutant killed, evidence retained. 4. Fresh-context
  trust-boundary review raw retained." Gate: "the existing suite unchanged plus a fresh rule-6 run with one mutant per form
  row and per sweep (retain evidence)."

## 3. What I ran and the results

Two scratch clones under `scratchpad/rev-505/`: `base` at `b7697f6a`, `head` at `9f49b6cb`, each with its own `npm ci` and
`npx tsc -b packages/polaris-generation-consent packages/polaris-dossier` (the clones sit under `/tmp`, outside the main
checkout, so no `@syzygy/*` import can fall through to the main checkout's `node_modules`).

1. **Code trace, base versus head, family by family** [Inferred from reading both files whole; confirmed by items 6–9]:
   - *Admission.* Base `parseAct` and head `parseActRecord` + `ADMISSION_FAMILY.dialect` perform the same set of checks:
     title prefix; `Act type` one-of `consent-observation|consent-egress`; `Date` one and a real calendar day; identity equal
     to the form's; type equal to the form's; `Artifact identity` equal to the form's; `Exact digest (SHA-256)` one;
     `Project identity` one; `actInstant` on `Recorded at (UTC)`. No recorder lines, no supersession field in either. Base
     `namesAdmission` and head `namesAct` over `{stems: ADMISSION_STEMS, needles: ADMISSION_PATHS, fields:
     everyField(stems+paths), quoted: true, loose: false, citations: true}` are the same predicate (same stems in the name,
     same needles in the text outside `ACCEPTANCE-ACT-RECORD.md`, same four labels with `>` allowed, same `sweepText`). The
     owner-answers pin moves into `findActRecords` with the same `sha256` comparison and the same thrown refusal.
   - *Policy.* Base `parsePolicyAct` and head `parseActRecord` + `POLICY_FAMILY.dialect` perform the same set: title, `Artifact
     identity` = `POLICY_PATH` (now via `form.artifact`, which every row spreads from `APPROVE_POLICY`), `Act type` `[a-z-]+`
     and = `approve-policy`, identity, digest, date (real day), project, the provenance opening regex (byte-identical,
     unanchored), `actInstant`, `supersessionText`. Base `namesPolicy` and head `namesAct` agree: scope stem in name; scope
     stem in text outside the aggregate; `Artifact identity` lines carrying the policy path and `Act identity` lines carrying
     the path or the policy stem, with `>` not allowed (`UNQUOTED_FIELD_LINE` is base's regex with two more alternatives
     appended; for a line base matched, head's alternation tries the same first two alternatives first, so the same capture
     wins, and the two new labels map to no needles); policy stem plus `withdraw|revok` in the name (moved from last to second
     in a pure `||`); no citation allowlist. Pins (`HISTORICAL_POLICY_ACTS`, same three digests) are checked before the sweep
     in both.
   - *Class.* Base `readClassAct` and head `parseActRecord` + `CLASS_FAMILY.dialect` agree on title, `Act type` `[^`\n]+` =
     `contract-amendment`, identity `RFC5-PROJECT-DOCUMENTATION-AMEND-<date>`, artifact = `CLASS_MODULE`, digest = sha256 of
     the module, `Act instant` label, supersession. Head adds an explicit real-calendar-day check that base did not have; it
     refuses nothing new, because base's `actInstant` already refused every such record (the instant must carry the same date
     and round-trip through `toISOString`); world `class-date-invalid` (item 8) and named alteration `date-invalid` (item 6)
     both answer `refused: invalid-records` in both trees. Base `namesClassAct` and head agree (class stem in name; stem or
     module in text outside the aggregate; module or stem on `Artifact identity` / `Act identity`, `>` allowed; allowlist on).
   - *Digest-bound and versioned sign-off.* `findActRecord`→`findActRecords`, `namesDigestBoundAct`→`namesAct` over
     `digestBoundSweep`, inline parse→`parseActRecord` + `RECORDER_DIALECT`: same order (template first, else recorder lines),
     same field reads, same `why` template literals (only `digest`→`act.digest` and `identity`→`act.identity`, the same
     values). `VersionedSignoffForm` has no `exemptRecords` field (base `package-reader.ts:682-692`), so head passing no
     `exempt` for it is equivalent.
   - *Ordering.* Head finishes the whole walk and sweep before parsing any admission or policy record; base interleaved them.
     Every check on those two paths throws the same `AdmissionRecordError('invalid-records')` and is a pure function of the
     same file bytes, so the result (records, or that one error) is the conjunction of the same checks in either order. On the
     strict digest-bound path, where the `why` text depends on order, the order is unchanged. The `strict` wrapper maps any
     `AdmissionRecordError` to `{state: 'refused', why: error.message}` in both trees.
   - *Parked half and pins.* `tools/parked_lines.py` over the 308 changed lines of `package-reader.ts` in the subject diff
     (181 + 127): 0 name `EGRESS_V2_INSTANCE`, `V2_REVOCATION`, `readInForceEgress` or `'egress-consent'`; 0 carry a 64-hex
     digest; 4 name a pin, and all four move a use rather than a value (`pins: new Map([[OWNER_ANSWERS_FILE,
     OWNER_ANSWERS_SHA256]])` and `pins: HISTORICAL_POLICY_ACTS` added, the two inline checks they replace removed).
     `consent-ports.ts`, `recorder-template.ts` (the `SLOT.line` read) and `index.ts` are not in the diff.
2. `npx vitest run --project @syzygy/polaris-generation-consent act-families.test.ts package-reader.test.ts` at head
   [Observed]: "Test Files  2 passed (2)", "Tests  358 passed (358)" (65 + 293).
3. The same command at base with head's `act-families.test.ts` copied in unchanged (then deleted) [Observed]: "Tests  358
   passed (358)", act-families "(65 tests)". The characterization file passes on the parent.
4. `npx vitest run --project @syzygy/polaris-generation-consent --project @syzygy/polaris-dossier` at head [Observed]: "Test
   Files  35 passed (35)", "Tests  1660 passed | 1 skipped (1661)" (consent 468 + dossier 1192, as the PR says).
5. `npm run typecheck` at head: exit 0, no diagnostics [Observed]. `python3 scripts/check_governance.py` at head [Observed]:
   "32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted". `python3 scripts/check_quotations.py` [Observed]: "OK
   QC-1 … 0 findings". `npx vitest run apps/three-surface-poc/src/polaris-authority-sweep.test.ts
   apps/three-surface-poc/src/polaris-generation/public-source-screening.test.ts` [Observed]: "Tests  41 passed (41)" (5
   PWB-REQ-014 authority-sweep tests, 36 public-source-screening tests). I did not run the full canonical battery; the PR's
   "commands=110 nonzero=0" is lane-reported [Unknown to me beyond the checks above].
6. **The differential, re-run** (`node head/scripts/differential_consent_act_families.mjs --old base --new head --workers 6`)
   [Observed]: "3890 worlds, 18366 answers compared, 0 mismatches, 1510 distinct answer vectors"; trees `old b7697f6a`
   (package-reader `ebf5cbf4…`), `new 9f49b6cb` (`6efd4c4e…`), both `clean: true`. Compared with the committed record
   (which ran `--new bc5f0f16`): `totals` equal, and every one of the 3890 world rows has the identical (kind, subject,
   operator, answer-vector sha256). The committed differential reproduces exactly from fresh clones.
7. **Differential sensitivity** (both sides really run their own tree): I edited head's compiled
   `dist/package-reader.js` only, flipping the policy family's `quoted: false` to `quoted: true` (the `pol-quoted` mutant),
   and re-ran `--kinds probe` [Observed]: "986 worlds, 11832 answers compared, 6 mismatches", exit 1; the six are the policy
   reader and policy chain on the `quoted-field-Act_identity` probe of `pwb-secret-classification-policy` and the
   `quoted-field-Artifact_identity` / `quoted-field-Act_identity` probes of the policy path: the old policy reader returns
   the version-4 identity and the old chain answers `ok … over 4`, while the new reader "throws AdmissionRecordError:
   invalid-records" and the new chain answers `refused: invalid-records`. The record of that run still named the new tree's
   src digest `6efd4c4e…` (see N5). Dist
   rebuilt with `tsc -b --force` afterwards and the edit confirmed gone (`grep -c` of the original line: 1).
8. **My own counterexample hunt** (`tools/probe.mjs`, 50 constructed worlds the corpus lacks, overlaid in memory on the old
   tree's own Syzygy checkout, read by both trees' compiled packages, 7 readers each: admission reader, policy reader, policy
   chain, class act, in-force egress, registry act, local-agent sign-off) [Observed]: "50 worlds, 350 answers compared, 0
   mismatches". I re-ran it at the end of the review over freshly verified builds (see the note at the end of this item):
   "50 worlds, 350 answers compared, 0 mismatches, 6 distinct short-label vectors" (`out/probe-rerun.txt`). The worlds:
   the base world; field labels spelled with tab, U+00A0, U+3000, U+FEFF, U+2028 and fullwidth
   letters, each naming the policy act, the class module, and the policy path inside the aggregate record; `>` Artifact
   identity / `Record ID` / `Subject` lines in the aggregate naming the policy path, class module and class stem; a `>`
   admission `Record ID` in the aggregate; `* **Act identity:**` and `>>` lines; `sub/PWB_SECRET_CLASSIFICATION_POLICY_REVOKE.md`;
   a withdrawal word without the stem; copies of the policy v1, historical policy, Redis admission and class records under
   `archive/`; a historical pin edited, alone and with a naming file, and with a malformed policy v1 record (order probes);
   a malformed policy v4 record beside a naming file; a malformed class record with the module deleted; class `Act type` in
   capitals; class date 2026-02-30 with a matching instant; policy v1 dated 2026-02-29; a non-JSON policy file, alone and
   beside a naming file; a file system whose `readdir` returns every decisions entry twice, alone and with a naming file; a
   repeated supersession field in the Redis admission act; the class act without Owner and A1 lines; a `>` policy `Act
   identity` in the aggregate and in another file; the policy stem alone on `Artifact identity` and on `Record ID`.
   *Build check.* The `tsc -b --force` in item 7 that restored head's `dist` ran at 04:09. My item-9 replay was editing
   head's `src/package-reader.ts` in the same clone at that time, so I checked that no mutant had been compiled in. At the
   end, with both trees' tracked files clean (`git status --porcelain --untracked-files=no` empty) and the sources at
   `ebf5cbf4…` and `6efd4c4e…`, a fresh `npx tsc -b --force packages/polaris-generation-consent` in each tree left
   `dist/package-reader.js` byte-identical: base `8472f4cb132a8f7a572df4929c2704871aa0e95f9d1bff8de59ece48a6fb1c4d`,
   head `d7679a04196c8b8cc4d8979aff77e6126e6247d160b4ebf8feba153a019b7b28`, the same before and after. The re-run above
   used those builds. The item-6 differential finished at 03:58, before item 7, and none of my vitest runs tests `dist`
   (`vitest.config.ts` aliases the package to `src`).
9. **Rule 6, re-run in full** (`env -C head python3 scripts/rule6_mutation_runner.py
   docs/evidence/consent-act-family-mutants-2026-10-22.json <out>`, all 101 mutants, at `9f49b6cb`) [Observed]:
   95 killed, 1 survived (`adm-needles`, "survived 0"), 5 errored. The 5 errored are the dossier mutants, run under the
   wrong project by the replay (N11). Re-run with `--project @syzygy/polaris-dossier` (`tools/dossier_spec.py`), they print
   "db-fieldstems killed 1", "g-exempt killed 10", "g-exempt-bytes killed 4", "g-why killed 6", "g-template killed 20".
   `tools/compare_mutants.py` over the record and both re-runs: "identical outcome, counts, failed-test names and
   fragments: 101 of 101 ; differing 0", with "re-run outcomes {'killed': 100, 'survived': 1}". Afterwards `git status
   --porcelain` in the head clone printed nothing, and `package-reader.ts` hashed to `6efd4c4e…` again. The record's
   killed counts are therefore reproduced at the reviewed commit, not only at `bc5f0f16`. An abrupt end would print no
   `Tests` line. The only rows without one are those five, all explained, so the `pkill -f vitest` that another session ran
   at about 03:55 (+08), which the coordinator reported, did not end any counted run.
10. **Supplementary row mutants** (`tools/build_row_spec.py`, 16 mutants, each `old` fragment checked to occur exactly once in
    package-reader.ts at `9f49b6cb`, same runner and same three test files) [Observed]: all 16 killed. Every run printed a
    `Tests` line over 398 tests in the three files, and none errored. Failed counts: `rv-pol-v1-spread` 267,
    `rv-pol-v2-spread` 10, `rv-pol-v4-spread` 2, `rv-pol-v1-identity` 267, `rv-pol-v2-identity` 10, `rv-pol-v3-identity` 4,
    `rv-pol-v4-title` 2, `rv-adm-requests-type` 1, `rv-adm-egress-v1-identity` 80, `rv-adm-egress-v2-version` 14,
    `rv-adm-egress-v2-title` 13, `rv-family-policy-forms` 2, `rv-family-admission-forms` 1, `rv-family-class-forms` 194,
    `rv-family-class-dialect` 194, `rv-family-policy-dialect` 5. The record (`out/row-mutants.json`) names commit
    `9f49b6cbec290c2cc0d3a94f3af820d83f5fb780` and `package-reader.ts` `6efd4c4e…`. Afterwards the tree was clean and the
    file hashed to `6efd4c4e…` again.
11. **`adm-needles` equivalence, mechanically** (`tools/adm_needles.mjs`, `fold`/`stemFolds` copied from the reviewed file)
    [Observed]: each of the four `ADMISSION_PATHS` needles' folded spelling contains an `ADMISSION_STEMS` needle's folded
    spelling ("…/public-repo-admission/instances -> public-repo-admission", "…/public-egress-v2/…/EGRESS-CONSENT-ANTHROPIC.md
    -> public-egress-v2, public-egress-", "…/public-repo-admission/ -> public-repo-admission", "…/public-egress-v2/ ->
    public-egress-v2, public-egress-"). Since `carries(text, path)` means some folded spelling of the text contains the
    path's folded spelling, it then contains the stem's, so the text test is already true from the stems; the field test
    still uses stems and paths, and the aggregate exemption covers both alike. The mutant is equivalent, in head and in base.
12. **Importer sweep** (`tools/importers.py`, rule 9) [Observed]: of 3034 tracked files, 681 code and config files scanned
    (479 `.ts`, 115 `.py`, 60 `.json`, 12 `.mjs`, 12 `.yaml`, 3 `.yml`; `docs/evidence/` excluded); 24 hits for an import of
    `@syzygy/polaris-generation-consent` (any subpath), a relative import of `package-reader` inside the package, or a
    `polaris-generation-consent/(src|dist)/` path string. Production readers of the changed code: `packages/polaris-dossier/src/gate-sources.ts`
    (`readPolicyActChain`, `readDigestBoundActState`, `readVersionedSignoffState`, `createPackageAdmissionRecordsPort`),
    `packages/polaris-dossier/src/screen.ts` (`readPolicyActChain`, `readClassActState`) and
    `apps/three-surface-poc/src/polaris-generation/public-source-screening.ts` (`readPolicyActChain`, `readClassActState`,
    `POLICY_ACT_FORMS` for `.file`/`.title` only); scripts `scripts/redis_screening_remeasure.mjs`, `scripts/simulate_redis_sitting.py`,
    `scripts/install_redis_local_agent_sitting.py` (line 673 names `real-tree.test.ts` among its gate tests). `index.ts` is unchanged and does not
    re-export `PolicyActForm` (the one exported type whose shape changed), so no consumer outside the package sees it.
    **The PWB P1 body-read gate does not go through any changed code**: `apps/three-surface-poc/src/governance-inputs.ts`,
    `apps/three-surface-poc/src/production-reobserve.ts` and `packages/three-surface-poc-core/src/body-read-authority.ts`
    are not hits, and no file under `packages/three-surface-poc-core/` is (0 hits). `governance-inputs.ts:62` names the v4
    record path as data (`PWB_ACT_RECORDS.policy`, block opening at line 60); `body-read-authority.ts` parses it with its own
    `parseOwnerActRecord` from `./owner-act-record.js` (import at line 60).
13. **Copied corpus versus PR #500** (`tools/compare_corpus.py`) [Observed]: `refs/pull/500/head` is `c08a015d`; the
    `PROSE_ALTERATIONS` and `HEAD_FIELD_ALTERATION` block of `recorder-fixtures.testkit.ts` there and the copy in the
    differential script are "EQUAL after stripping TS annotations" (`(text: string) =>`, `as const`, the `Object.freeze` /
    type annotation and the doc comments), and all 16 regex and string literals of the original occur in the copy. Not
    byte-equal; behaviour-equal, as the script's own comment ("copied verbatim in behaviour") says.
14. **Runner callers** (rule 9) [Observed]: `git grep -l -F rule6_mutation_runner` over all 3034 tracked files outside
    `docs/evidence/` returns `docs/plans/2026-10-21-greenfield-parity-audit.md`, two `docs/reviews/*-RAW.md` and the script
    itself; under `docs/evidence/` 25 records cite it. No CI workflow, no `PROJECT-STATUS.md` battery line and no script
    calls it; `runnerSha256` is read by nothing but the runner. No vitest config sets `reporters`.

## 4. Findings

No blocking finding. I found no record that base and head answer differently, by trace, by the re-run differential, by
the sensitivity run and by 50 constructed worlds; GP-Q0 part 3 is not engaged.

### N1 — Classes are 1 and 4, not 4 alone (note)
- Evidence: the PR body states "**CC-REV-1 classes:** 4, the consent boundary." The change also rewrites the sweep and parse
  path of `readDigestBoundActState` (registry entry act `REGISTRY_GIT_SOURCE_ACT_FORM`, act type `adopt-registry-entry`) and
  of `readVersionedSignoffState` (`LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM`, whose installed entry is under
  `.syzygy/governance/declarations/adapter-registry/`), which the dossier start gates (`gate-sources.ts`) read to decide
  whether the source-acquisition adapter is authorized: CC-REV-1 class 1, "adapter authorization (VIS-5, VIS-6)". Class 4
  holds for SEC-2 consent and egress. Not class 6: `index.ts` is unchanged and the one reshaped exported type,
  `PolicyActForm`, is not re-exported.
- Failure scenario: the cycle report's owner notice and the landing record name class 4 only, so a later audit of class-1
  changes misses this PR.
- Fix: state "classes 1 and 4" in the PR body and in the owner notice. GP-Q0 line 62 sets the same three extra checks for
  class 1 as for class 4, so no further evidence is owed.

### N2 — GP-Q0's third extra check, the owner notice, does not exist yet (note)
- Evidence: GP-Q0 lines 64–66 require "a non-blocking owner notice in the cycle report"; the brief says the coordinator
  posts it at landing. Nothing in the subject is or could be that notice.
- Failure scenario: the PR lands with two of the three GP-Q0 checks evidenced.
- Fix: at landing, the coordinator posts the notice in `syzygy-bpyt.10`, naming classes 1 and 4 (N1), the differential and
  mutant records, and the knob decision (N9).

### N3 — The rule-6 record has no mutant for most form rows (note)
- Evidence: the bead's gate asks for "one mutant per form row and per sweep". The record's row mutants cover the one class
  row (all five fields), one of four admission rows (`row-admission-redis-type`), the shared `APPROVE_POLICY` object, the
  version-3 spread and the version-4 identity, and the registry form's type. Not mutated: the version-1, 2 and 4 spreads
  (each a changed line), the version-1 to 3 identities, the version-4 title, the requests, egress-1 and egress-2 admission
  rows, and each family's `forms` list and each strict reader's choice of dialect. The PR body's coverage line ("one each
  for: every form-row field the change touches") therefore overstates the record. My 16 supplementary mutants over exactly
  those rows are all killed (section 3 item 10). The gap is in the evidence, not in the tests. Two of the 16 are killed by
  a single test (`rv-adm-requests-type` and `rv-family-admission-forms`, both by the records-port `repositoryIdsFor`
  test).
- Failure scenario: a later edit that drops one row's `...APPROVE_POLICY` or retargets one row is caught only by whichever
  suite happens to cover that version, and the evidence record does not show it.
- Fix: add the 16 mutants of `tools/build_row_spec.py` (listed in section 7) to the retained record at landing, or cite this
  raw beside it; neither changes a reviewed byte of code.

### N4 — `adm-needles` survives and is equivalent; acceptance criterion 3 is met only with that argument (note)
- Evidence: section 3 items 9 and 11. The redundancy is base's: `namesAdmission` already tested `[...ADMISSION_STEMS,
  ...ADMISSION_PATHS]` in the text.
- Failure scenario: none for the gate. The criterion "every row and sweep mutant killed" reads as unmet to anyone who does
  not follow the equivalence note.
- Fix: accept the equivalence (it is proven above, not just argued). The listed follow-up that drops `ADMISSION_PATHS` from
  the text needles is a change to a consent sweep, so it needs its own differential and review even though it is
  behaviour-neutral by the same proof.

### N5 — The differential record binds the source digest, not the compiled code it runs (note)
- Evidence: the script imports each tree's `dist/index.js` and `dist/gate-sources.js` but records
  `packageReaderSha256` of `src/package-reader.ts`. In item 7 I changed only the new tree's `dist`, the run reported 6
  mismatches, and its record still named `6efd4c4e…`. A stale or hand-edited `dist` (for example a tree built at another
  commit, or a `tsc -b` that skipped because of a stale `.tsbuildinfo`) would produce a record whose stated subject is not
  what ran (rule 11).
- Failure scenario: a future run over an unbuilt or stale new tree reports 0 mismatches against code that is not the
  change, and the record looks valid.
- Fix: record the sha256 of each tree's `dist/package-reader.js` and `dist/gate-sources.js` beside the source digests, or
  build both trees inside the script. The committed 2026-10-22 record is unaffected: item 6 reproduced every world from
  fresh, freshly built clones.

### N6 — "1510 distinct answer vectors" measures answer content, not verdict variety; three corners are thin (note)
- Evidence: the compared answer is the full JSON, including each parsed act's `text`, so an accepted line edit is a new
  answer. Distinct answers summed over the 24 reader-and-instant slots are 1746; distinct labels (verdict and reason, digests
  and texts dropped) are 167. `policy-chain@2026-10-22` has 1015 distinct answers and 3 labels; `class-act` 189 and 3.
  `policy-chain@2026-10-08` never answers `ok` in any of the 3890 worlds (2 labels, both `refused`): no world puts an earlier
  policy version in force over matching bytes. The records port is compared on the 8 base worlds only (probes and subject
  worlds leave it out); its answers are built from the admission and policy readers, which are compared everywhere.
- Failure scenario: a reader reports a large distinct-vector count as evidence of verdict coverage that is not there.
- Fix: in later records report labels beside answers; add one world that overlays the policy file with bytes an earlier
  version's act binds (for example version 3's, from git history) so the mid instant reaches `ok`. Not needed for this PR:
  the chain-term code (`policyTerms`, `policyActAt`, `policyMismatch`) is not in the diff, and the unchanged suite's
  `describe('the policy port and the strict policy chain agree')` / `it('on every world in the fixture set, at every
  instant')` (`package-reader.test.ts:995-997`, eight instants including 2026-10-01 and 2026-10-03, with its own
  `satisfied > 10` non-vacuity check) passes.

### N7 — The altered-prose corpus is a behaviour-equal copy of an unmerged PR (note)
- Evidence: section 3 item 13. PR #500 (`c08a015d`) has not merged.
- Failure scenario: #500 revises its corpus and lands; this script's copy silently diverges from the corpus the bead notes
  say it reuses.
- Fix: the lane's listed follow-up (repoint the differential at the 8.10 corpus once #500 lands). Keep this record as it is;
  it is valid for its own bytes.

### N8 — `rule6_mutation_runner.py`: verdicts unchanged for existing callers, but the recorded `command` is not the command run (note)
- Evidence: with no `--tree` the runner's tree is `'.'`, `run` passes `cwd='.'`, and the kill rule (`killed = (failed or 0)
  > 0 or tot is None`) and its `Tests` regexes are unchanged; the summary line still prints because `--reporter=default`
  is kept. But every run now passes `--reporter=default --reporter=json --outputFile.json=<tmp>`, while the record's new
  `command` field holds the argv without those three flags, and each mutant record gains `command` and `failures`. No CI,
  battery or script calls the runner (item 14), so nothing breaks.
- Failure scenario: a reader re-runs a record's `command` and gets the same verdict but a different invocation than the one
  the record claims.
- Fix: store the exact argv in `command`, or name the reporter flags in the `runner` text.

### N9 — The unaligned knobs carry pre-existing fail-open asymmetries; aligning them is an owner decision (note)
- Evidence: preserved, as GP-Q0 part 3 requires, and pinned by `act-families.test.ts`: the policy sweep ignores `>` field
  lines (my world `policy-quoted-agg-act-id`, `> Act identity: <policy v1 identity>` in the aggregate record: policy `ok` in
  both trees, while the same line names the admission, class and registry acts for their families); the admission family
  checks neither recorder lines nor a repeated supersession field (`admission-supersession-dup`: `ok` in both); the class
  family checks no recorder lines (`class-recorder-lines-gone`: `ok` in both).
- Failure scenario: a withdrawal written as a blockquoted field line in the aggregate record does not defeat the policy
  grant, against "withdrawal defeats grant".
- Fix: file the lane's "knob-alignment owner decision" as a decision bead under `syzygy-bpyt.1`, each knob a separate
  option, since every alignment makes a gate stricter (a change to what it refuses). Nothing in this PR should change.

### N10 — The bead's own text is stale for a cold reader (note)
- Evidence: the bead description says "screening-policy (v1-v3)" and names `packages/polaris-dossier/src/package-reader.ts`;
  the code has four policy forms (version 4 added 2026-10-20, `syzygy-3sjj`) and the file is
  `packages/polaris-generation-consent/src/package-reader.ts` (the coordinator's 2026-10-22 note corrects the path, not the
  version range). Its outcome also says "rows of the existing data-driven DigestBoundActForm table"; the change adds an
  `ActForm` shape that `DigestBoundActForm` satisfies, which meets criterion 1 in substance.
- Fix: amend the bead description (v1–v4, the real path) when it closes.

### N11 — Replaying the record as a spec skips its five dossier mutants, and the runner counts them killed (note)
- Evidence: the runner's docstring says "a previous OUT.json is a valid SPEC". The record's top-level `project` is
  `@syzygy/polaris-generation-consent`. Five mutants (`db-fieldstems`, `g-exempt`, `g-exempt-bytes`, `g-why`,
  `g-template`) ran with the `command` "npx vitest run --project @syzygy/polaris-dossier
  packages/polaris-dossier/src/gate-acts.test.ts", but their records carry no `project` key: the runner writes none, at
  base and at head. Replaying the record as the spec (item 9) runs those five under the consent project, which holds no
  such test file. Vitest prints no `Tests` line, and the runner reports "errored". Its rule `killed = (failed or 0) > 0 or
  tot is None` counts that as killed. My replay reported "db-fieldstems errored None", "g-exempt errored None",
  "g-exempt-bytes errored None", "g-why errored None" and "g-template errored None". Run by hand under the consent project
  (`npx vitest run --project @syzygy/polaris-generation-consent packages/polaris-dossier/src/gate-acts.test.ts`), vitest
  prints "No test files found, exiting with code 1". Re-run with the project taken from each recorded command
  (`tools/dossier_spec.py`), all five are killed with the record's counts (1, 10, 4, 6, 20 of 130), as item 9 shows.
- Failure scenario: a later confirmation run replays the record and reports every mutant non-surviving, but no test ran
  for five of them. That is an exit-code reading of a check (rule 4) built into the runner.
- Known: `syzygy-bpyt.11` (open, P3, read with `bd show`) records the dropped `project` and says "The 8.10 lane worked
  around it with one record per project". This record is the mixed-project shape that bead says breaks, and the PR does not
  use that workaround. The bead does not mention that the runner then counts the empty run as killed.
- Fix: no change to reviewed code is needed. Either split the record into one record per project, as 8.10 did, or give
  each of the five mutant records a `note` citing `syzygy-bpyt.11`, saying that a replay needs the project taken from its
  `command`. The record has no top-level `note` today. Add to `syzygy-bpyt.11`:
  keep counting a mutant that breaks loading as killed, but stop the run when vitest selected no test file, rather than
  calling that a kill.

## 5. Changed outputs

None found. Evidence: the re-run differential (0 of 18366 answers differ, full answer JSON compared, including every `why`
text, parsed act fields and record lists, item 6); the 50-world probe (0 of 350, item 8); the characterization file passing
65/65 on both trees (items 2–3); the unchanged consent and dossier suites (item 4); typecheck clean (item 5). No rendered
byte, wire format, exit code or refusal string changes; no digest-bound artifact is edited (nothing under `.syzygy/**`). The
only new outputs are the three evidence records, the differential script, and two new keys in future runner records (N8).
`package-reader.ts` grows from 912 to 966 lines (+181 −127): four parsers and four sweeps become one each, and the
difference is the per-family knob data and its comments.

## 6. Verdict per acceptance criterion

1. "Three bespoke families expressed as form rows; one sweep implementation." **Met.** Admission, policy and class are
   `ActForm` rows read by one `parseActRecord`; `namesAdmission`, `namesPolicy`, `namesClassAct` and
   `namesDigestBoundAct` are one `namesAct`, walked by one `findActRecords`. No byte-exact act moved onto field parsing:
   template forms still go through `fromTemplate` before any field read (GP-Q0 part 2).
2. "package-reader and gate-acts suites pass unchanged; refusal strings identical (golden)." **Met.** No existing test file
   is in the diff; `package-reader.test.ts` 293/293 and the dossier project (which includes `gate-acts.test.ts`) pass. There
   is no golden file as such: identity of refusal strings rests on the differential comparing every answer's full text, the
   `g-why` mutant (killed) and the dossier suite's assertions.
3. "Fresh rule-6 run, every row and sweep mutant killed, evidence retained." **Met with N3 and N4.** The record's 101
   mutants reproduce at `9f49b6cb`: 100 killed and 1 survived, and all 101 are identical to the record (outcome, counts,
   failed-test names and fragments) once the five dossier mutants run under their own project (item 9, N11). The one
   survivor, `adm-needles`, is shown equivalent (item 11, N4). The form rows the record leaves unmutated are covered by my
   16 supplementary mutants, all killed (item 10, N3). The PR's record is retained in the PR. My re-run records and the row
   record are in `scratchpad/rev-505/out/` for the coordinator to retain beside this raw.
4. "Fresh-context trust-boundary review raw retained." **Met by this file once the coordinator retains it.**

GP-Q0 extra checks (class 1 and 4): differential over a mutated-record corpus with altered prose — **present and reproduced**
(N5–N7 are notes); a rule-6 mutant per predicate — **present** for every `namesAct`, `findActRecords` and `parseActRecord`
predicate and every knob, with the row gaps of N3 now run; owner notice — **missing until landing** (N2).

## 7. Test quality

- `act-families.test.ts` expectations are literals (verdict vectors, paths, identities, `Date.UTC` instants); nothing is
  imported from the module under test except the readers and one form. Fixtures that touch the file system or spawn the
  recorders are built in `beforeAll`; the module-scope tables are plain data and cannot throw at describe time. Each dialect
  row asserts its alteration took (`not.toBe(BASE[file])`), and the allowlist mock is cleared after each test.
- Passing on the parent is shown by the retained record (`…-characterization-on-parent-2026-10-22.json`, test file digest
  and parent commit named) and by my own run (item 3).
- Thin spots: the admission verdict collapses every resolved read to `ok`, so a row cannot tell "record read" from "record
  read but unbound"; several knobs are killed by a single test (`adm-quoted`, `pol-citations`, `cls-needles`,
  `cls-quoted`, …). Acceptable for a characterization file whose content-level check is the differential.
- Two of my 16 row mutants are killed by one test each (N3). Every other row mutant is killed by 2 to 267 tests.
- Supplementary mutants run (id: change in `package-reader.ts` at `9f49b6cb`). The exact `old`/`new` fragments are in
  `out/row-spec.json` and `out/row-mutants.json`, and each `old` occurs exactly once:
  - `rv-pol-v1-spread`, `rv-pol-v2-spread`, `rv-pol-v4-spread`: delete the `...APPROVE_POLICY,` line from that version's
    row.
  - `rv-pol-v1-identity`, `rv-pol-v2-identity`, `rv-pol-v3-identity`: `…-APPROVAL-${date}` → `…-APPROVED-${date}` in that
    version's identity.
  - `rv-pol-v4-title`: `(public-source screening scope, version 4)'` → `(… version 4 )'`.
  - `rv-adm-requests-type`: the psf/requests row's `type: 'consent-observation'` → `'consent-egress'`.
  - `rv-adm-egress-v1-identity`: `` `PUBLIC-EGRESS-ANTHROPIC-${d}` `` → `` `PUBLIC-EGRESS-ANTHROPIC-X-${d}` ``.
  - `rv-adm-egress-v2-version`: `artifact: EGRESS_V2_INSTANCE, version: 2 }` → `version: 1 }`.
  - `rv-adm-egress-v2-title`: `…consent to Anthropic, version 2'` → `…consent to Anthropic, v2'`.
  - `rv-family-policy-forms`: `forms: POLICY_ACT_FORMS,` → `forms: POLICY_ACT_FORMS.slice(0, 3),`.
  - `rv-family-admission-forms`: `forms: ADMISSION_ACT_FORMS,` → `forms: ADMISSION_ACT_FORMS.slice(1),`.
  - `rv-family-class-forms`: `forms: [CLASS_ACT_FORM],` → `forms: [],`.
  - `rv-family-class-dialect`: the class reader's `parseActRecord(…, CLASS_FAMILY.dialect)` → `RECORDER_DIALECT`.
  - `rv-family-policy-dialect`: the policy reader's `parseActRecord(text, form, POLICY_FAMILY.dialect)` →
    `RECORDER_DIALECT`.

## 8. Cleanup

- Deleted [Observed: `ls` afterwards lists neither]: the scratch clones `scratchpad/rev-505/base` (207M) and
  `scratchpad/rev-505/head` (146M). Before deletion both trees' tracked files were clean, and head's `package-reader.ts`
  hashed to `6efd4c4e…` after every mutant run.
- Kept in `scratchpad/rev-505/`, all small, for the coordinator to retain or delete:
  - this raw;
  - `tools/`, the scripts named above;
  - `out/`: the differential re-run and sensitivity records, the mutant replay, the dossier re-run, the row spec and row
    record, the probe re-run output and a copy of head's `package-reader.ts`;
  - `my.diff`, the re-derived subject diff, sha256 `c0fc8b9e…3a1415`;
  - `pr500-testkit.ts`, PR #500's testkit at `c08a015d`, for item 13.
- No process of mine is running, and every monitor I started has ended.
- I made no `bd` mutation, push, PR comment or merge, and edited nothing in the main checkout or under `.worktrees/`.
- I fetched no target-repository content. Every world was built from Syzygy's own tracked files.
