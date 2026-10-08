# Review — PR 409 P-105/P-106 record and install
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: c4a5921d3d3fec1ff25c86083321de5a0f7db123
Reviewer: fresh-context

Base `c88bbf9eae1282ba0aa19349594f9e6a8f822fbd`. Commits reviewed: 4cd1ded7, 557e7074, 53b10a82 and c4a5921d (c4a5921d adds only the two mutant-evidence JSON files over 53b10a82). Everything ran in a detached scratch worktree at the head commit, which was removed afterwards. No target-repository content was read. Every probe body was synthetic.

Findings are notes only (N1–N6). No finding blocks the merge. The criteria table comes first, then the findings.

## Criteria

### 1. Act records: selection, instant, binding

Met. [Observed]

- **Selection text.** A script compared each act record with `owner-selections-2026-10-08.md`. Both records quote the question opening, the label and the description verbatim, all three matching. The source's "— SELECTED" suffix is the lead's marker and is correctly left off the label.
- **Selected, not typed.** Both records say "The owner did not type the phrase".
- **Instant.** Both records carry `Recorded at (UTC): 2026-10-08T16:24:27Z`. That is 0.162 s after the answer instant of 16:24:26.838Z, so neither act takes effect before the answer.
- **Rows and digests.** Every digest was computed by script:
  - The v3 argument `c13bd56c…` is the `[variant: all]` row of the v3 manifest. The manifest file hashes to `e5328701…`, which is the `Manifest SHA-256:` in the head of `R-PUBLIC-SOURCE-SCREENING-SCOPE-V3-2-RAW.md`.
  - The provider argument `b7a8d099…` is the one row of its manifest. That manifest file hashes to `62cd699a…`, which is the head of `R-DOSSIER-AGENT-PROVIDER-V2-2-RAW.md`.
- **Frozen files.** `--freeze-table 5db1dd72…` re-derives both recorders' `FROZEN_FILE_DIGESTS` exactly, 7 of 7 and 6 of 6.
- **Recorder checks.** Both `--check` lines pass in the battery.

### 2. Installed bytes

Met. [Observed]

- **Policy.** The base policy hashes to `98a87f81…`, which is v2's argument. `git apply` of `proposed/…json.all.patch` to the base gives `c13bd56c…`, byte-equal to the head policy. The `git diff` between base and head shows exactly the patch's hunks: `policyVersion`, the `activeContent` object and `inheritedRules`.
- **Statement.** The v2 statement is unchanged between `5db1dd72`, base and head, at `b7a8d099…`. A word-diff of v1 against v2 shows these differences:
  - the template and builder paths in the banner;
  - the draft date;
  - the record version;
  - the added `project-documentation` class;
  - the supersession line.
- **v1's term.** v1 is superseded only from v2's instant. Gate probe:
  - at 16:24:26Z the only statement is v1 (`0.1.0-candidate.1`, five classes);
  - at 16:24:27Z and at the current time the only statement is v2 (`0.2.0-candidate.1`, six classes).

### 3. Install lists

Met, 17 of 17 done and none deferred. [Observed]

Population: 8 items in the v3 IMPACT-LEDGER, 8 install-time bullets in the provider v2 SEMANTIC-DELTA, and 1 install requirement in v3's ROUND-2-DISPOSITIONS (note 1). The other four disposition notes need no install: v3 notes 2 and 3 are a residual and a wording note, and provider notes 1 and 2 are taken or read as stated.

**v3 ledger:**

| # | Item | Done |
|---|---|---|
| 1 | The third `POLICY_ACT_FORMS` form, and the chain generalised | yes |
| 2 | The v2 battery lines replaced by v3's | yes |
| 3 | The CG-7e chain row, the `variant-row` offering and the v2 manifest gate | yes; CG-7e is OK over 91 files |
| 4 | Both screens, through the shared `codeContentExempt`, and all three body call sites (`repo-corpus.ts`, `check.ts`, `review.ts`) pass the path | yes |
| 5 | The app act port moved to `readPolicyActChain` (`syzygy-p83h`) | yes |
| 6 | The Butlers gate re-pinned: `governance-inputs.ts`, and `PWB_POLICY_IDENTITY`, which `content-classification.ts` reads | yes |
| 7 | Version pins | yes: `git grep -F` over packages, apps, scripts and .github finds the v2 version literal only in test fixtures and the v2/v3 recorders |
| 8 | The simulator and the repin builder | yes; `check_spec_reconciliation.py` is unchanged, with a note on it under criterion 6 |

**Provider delta:**

| # | Item | Done |
|---|---|---|
| 1 | Version-aware `STATEMENT_FORMS` | yes |
| 2 | Sweep collision, v2 reading v1 | yes |
| 3 | Sweep collision, v1 reading v2 (`exemptRecords`, both ways) | yes |
| 4 | The `--tool` prerequisite | met earlier, by #406 |
| 5 | Preflight agrees with the gate, because the term ends in `statementsFor` | yes |
| 6 | A single in-force statement | yes |
| 7 | The class gate, which needs no change | yes |
| 8 | `gate-acts.test.ts`, the recorder and the CG registrations | yes |

**v3 disposition note 1:** done. The installer `--selftest` holds 101 of 101, and `--check --only policy,reconcile` reports "not installed: none".

### 4. renderCondition

Met. [Observed] The probes used the head policy bytes through `buildDossierScreen(policy, true)`:

- **`.c` comparison.** A `src/server.c` body holding `a<b && c>d` is admitted. Without a path it is `active-content`.
- **`.c` secret.** A `.c` body holding `AKIA…` plus the comparison is `secret-detector-match`.
- **Markdown.** `README.md` with `<script>` is `active-content`. `docs/guide.md` with the comparison is `active-content`.
- **Other paths.**
  - `src/SERVER.C` is not exempt: the class is undefined and the body is `active-content`.
  - `.env` is denied.
  - `web/app.js` holding an HTML string is admitted, as variant `all` intends.
- **Rendered pages.** `renderDossier` was given synthetic sources whose text is a C comparison:
  - the span lands only on the three `sources/*.html` pages, as `a&lt;b &amp;&amp; c&gt;d`;
  - no `.html` file carries the raw form;
  - every HTML page passes `pageSinkCspFinding`.
- **CSP checker probes.** The checker refuses `script-src-elem`, upper-case `SCRIPT-SRC`, `default-src 'self'`, `'none' 'self'`, a duplicate `default-src`, Report-Only, two metas, a `<base>` before the meta and an unquoted `http-equiv` (fail-closed). It accepts `worker-src`, `frame-src` and `child-src`, as the clause's exact list of four allows.
- **Tests.** `page-sink.test.ts` and `render.test.ts` ("renders an exempt body only through a renderer that declares the page-sink contract…") pass.

**README in packets.** `unconsentedClass('project-documentation', statementContentClasses(...))` over the real tree:

- at 16:24:26Z it withholds `project-documentation`;
- at 16:24:27Z and at the current time it admits it.

The README path is classed `project-documentation` with the class act in force. This composition is the one `review.ts:202` uses.

### 5. Gate and preflight

Met. [Observed]

- **At and after 16:24:27Z.**
  - `preflight('https://github.com/redis/redis')` is `ready`.
  - The screening policy is `ok` under `…SCOPE-V3-APPROVAL-2026-10-08`.
  - The only statement is `…@0.2.0-candidate.1`, which `providerStatementGate` also returns.
  - Observation consent, the registry sign-off, D9 and the RFC7-20 reading are each `ok`.
- **Absent before and after.** The codex statement and the drawer statement are absent. [Inferred] That is unchanged from base, since neither act record exists.
- **One second before the instant.** The policy gate is refused: the bytes differ from v2's argument. That is expected for an act instant, and not a regression.
- **Tests.** The `gate-acts.test.ts` "closes no other gate" case passes, as does `real-tree.test.ts` "refuse nothing".

### 6. Checks and battery

Met, except one battery line that could not run here; see N5. [Observed]

- **check_governance.** 32 OK, 21 WARN, 0 FAIL.
  - CG-7e: OK.
  - CG-26: OK, with 92 published, 92 hosted and 92 shared.
  - `--selftest`: passes.
- **Battery.** I ran it as one shell script with an ERR trap and read the log. 95 of the 96 block lines ran clean. `check_spec_reconciliation.py --selftest` failed twice, with `[Errno 28] No space left on device` from `shutil.copytree`. `df -i /tmp` shows 99–100% of inodes used on the shared tmpfs, so the failure is environmental. That check's result is [Unknown] here.
- **Known v3.**
  - installer: 101 of 101;
  - simulator `--selftest`: ok;
  - repin builder `--check`: "3 later act patch(es) reversed = proposed bytes";
  - both package builders `--check`: current.
- **Vitest.** I could not run the full suite here: it died on ENOSPC, the same inode exhaustion, in an unrelated fixture. The 13 targeted files all pass, 767 tests in total: the PR's 10 changed or added test files, plus `real-tree.test.ts`, `draft-preview.test.ts` and `dossier-render.test.ts`.

### 7. Mutants

Met. [Observed]

- **Record contents.** Both records carry `old` and `new` for every mutant and the commit `53b10a82`. The ts record also carries file and test SHA-256s and the runner path and digest, and `scripts/rule6_mutation_runner.py` is tracked.
- **Counts.** 53 ts mutants with 3 survivors, and 8 py mutants with 1 survivor.
- **The four claimed equivalents, re-derived:**
  - `exemption-keys-names`: with exactly five keys, a key missing from the required set leaves that key's value undefined. The `typeof`, digest or `Array.isArray` check then refuses. Equivalent for JSON input, since there are no inherited values.
  - `exemption-ext-string`: `includes` on an all-string `sourceExtensions` is false for any non-string. Both callers enforce `stringList` (`screen.ts:73`, `public-source-screening.ts:142`). Equivalent.
  - `exempt-final-segment`: a full path ends with an extension while its final segment does not only if the extension contains `/`. Both callers refuse such an extension with `^\.[^/\s]+$` at the same lines. Equivalent under every current caller; see N4.
  - `repin-variant-hyphen` (py): equivalent on every reachable tree, since the recorded variant is `all` and the v3 recorder refuses a second variant act. The hyphen branch itself is unexercised.

### 8. No unlawful edits

Met. [Observed]

- **Population.** 35 files were modified between base and head; none was deleted. For each one, I hashed the base bytes and searched all 2,633 tracked files at head, as full digests and 16-character prefixes.
- **Citers found:**
  - the policy, whose old digest is cited by the v2 manifest and act, the aggregate record, the v3 act, check_governance and the py mutant record, as history or arguments, and changed by the recorder's designed step;
  - some code files, cited only by earlier mutation-evidence records as subjects.
- **Dispositions.** Neither `ROUND-2-DISPOSITIONS.md` is digest-cited. The edits renumber headings, keep their words, and append "Install notes".
- **Raws.** No `-RAW.md` file was modified.
- **Labels.** Nothing is labelled accepted beyond "effective owner authority … for its own role only".

## Findings

### N1 — note: "Recorded at" is the act instant, not the recording instant

- **Where:** `.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V3-ACT.md:5` and `DOSSIER-AGENT-PROVIDER-V2-REDIS-ANTHROPIC-ACT.md:5`; `scripts/record_public_source_screening_scope_v3_act.py:49`.
- **Quote:** the record says `Recorded at (UTC): 2026-10-08T16:24:27Z`. The recorder's docstring says "It then writes the dedicated record (with the UTC instant of recording)".
- **Observed:** the records were written at commit 4cd1ded7, whose author date is 2026-10-09 01:26:22 +0800, that is 17:26:22Z, about an hour after the stated instant. The value came from `--instant`.
- **Inferred:** this follows the 2026-10-07 sitting's precedent, and the gate correctly treats the value as the act's effective instant. A reader who takes the field label literally is misled. Both acts also share one instant: no check requires them to differ, and none failed.
- **Failing input:** read the field as the time the record was written; it is wrong by about 62 minutes.
- **Suggested:** say "act instant" in future recorder templates. The bound records stay as they are.

### N2 — note: v2's act record understates its difference from v1

- **Where:** `.syzygy/governance/decisions/DOSSIER-AGENT-PROVIDER-V2-REDIS-ANTHROPIC-ACT.md:73-75`.
- **Quote:** "differs from version 1 in nothing else but its draft date, version and supersession line".
- **Observed:** a word-diff of v1 against v2 also shows the banner's template path (`…TEMPLATE.md` → `…TEMPLATE-V2.md`) and its builder path (`build_dossier_local_agent_acts.py` → `build_dossier_agent_provider_v2.py`).
- **Inferred:** these are presentation lines with no consent effect. The record is now act-bound, so this note is for the next version's template only.

### N3 — note: the aggregate block says the gates are re-pointed by a separate change

- **Where:** `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md:1451`.
- **Quote:** "the read gates are re-pointed by a separate change."
- **Observed:** the gates were re-pointed by the installer in the same commit (4cd1ded7), as decision 1 of the packet requires ("in the same commit"). The sentence is the recorder template inherited from v1 and v2 (lines 1235 and 1289), and it is defensible only if "change" means the installer step.
- **Suggested:** template wording for future recorders only.

### N4 — note: `codeContentExempt` relies on its callers to refuse `/` in extensions

- **Where:** `packages/polaris-generation-core/src/public-source-classification.ts:203` and `:231`.
- **Observed:** `readCodeContentExemption` is exported and checks only that `exemptExtensions` ⊆ `sourceExtensions`. `codeContentExempt` matches on the final segment. Both current callers validate `^\.[^/\s]+$`, which is what makes `exempt-final-segment` equivalent.
- **Failing input, under a future caller without that validation:** `sourceExtensions = ['x/y.c']`. The path `a/x/y.c` has the final segment `y.c`, so the extension is never matched. That fails closed, but the mutant would then be distinguishable.
- **Suggested:** move the shape check into `readCodeContentExemption`, or document the precondition. No current exposure.

### N5 — note: no retained fresh-clone battery record; one battery line Unknown here

- **Where:** the PR body says "Rule-6 mutants and fresh-clone battery: added in a follow-up commit or comment on this PR".
- **Observed:**
  - the mutants were added at c4a5921d;
  - no fresh-clone battery transcript is in the tree, and `gh pr view --json comments` returns none;
  - hosted `checks` and `node` report pass (status only; I did not read their logs).
- **My run:** 95 of 96 lines are clean. `check_spec_reconciliation.py --selftest` is [Unknown] locally, for ENOSPC on an inode-exhausted `/tmp` (99–100% IUse), not for anything this PR changed. Its first stderr line was an informational note, the same at both runs.
- **Suggested:** retain the battery transcript for the merged head, per rule 7.

### N6 — note: the register note does not record that P-107 was answered in the same question

- **Where:** `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:1040`.
- **Quote:** "P-107 is another lane's and stays open."
- **Observed:** the selection source records the owner's P-107 answer in the same structured question: "B, reviewer may continue (Recommended) — SELECTED". The P-107 row and this note do not say so. [Inferred] A reader could re-ask the owner. This is out of this PR's acts but in the same dated note.

## Not found

- No binding defect.
- No unlawful edit to act-bound bytes.
- No gate closed beyond the expected pre-instant policy refusal.
- No path where an exempt body reaches a page unescaped or without the CSP.

The README-in-packet behaviour flips exactly at v2's instant.
