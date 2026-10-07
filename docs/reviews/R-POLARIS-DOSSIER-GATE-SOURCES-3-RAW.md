# R-POLARIS-DOSSIER-GATE-SOURCES-3
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: a6157cb06accd49b1fd841c92678b27bcac3550b
Subject: PR #377 (syzygy-qkea.21)

Reviewer: fresh-context independent reviewer, 2026-10-07, round 3 (final).
Scope: `git diff origin/main...a6157cb0`, 20 files, +1469/-101. Any later
evidence-only commit (the mutant record) is out of scope. I fetched no
content from any external or target repository.

Stopping rule applied: REVISE is reserved for a criterion break that would
let a gate admit what it should refuse, or refuse a correctly recorded
sitting. I found none, so every finding below is a NOTE.

## Governing clauses (quoted)

- **RFC3-16.** `DIRECTIVE-REGISTER.md`:277 places it at
  `.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md`:112.
  From :218: "An effective owner act is an actual human owner act whose record
  is current, attributable, scope-matched and bound to the artifact's exact
  digest under RFC3-16(b)."
- **polaris-dossier-local-agent-mode v1.1**
  (`openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md`):
  - :11: "its withdrawal SHALL refuse further steps of any run that relies on
    it".
  - :13: "withdrawal of the observation consent, the registry entry or a
    policy act refuses every later step of the run".
  - :13: "Syzygy SHALL establish that ... any per-project statement, D9 and
    the owner's reading of RFC7-20 are in force from the record of the
    owner's act that makes each effective ... never from a status word or a
    file's presence."
- **The recorders' own revocation line**, in
  `scripts/record_dossier_local_agent_acts.py` `render_act` and in
  `scripts/record_versioned_signoff.py` `installed_lines`:501-502:
  "Supersession / revocation: supersedes nothing; revoked only by a later
  exact owner act naming it".

## Verification performed

- [Observed] **Test suite at a6157cb0.** Scratch worktree, `npm ci`, then
  `vitest run packages/polaris-dossier packages/polaris-generation-consent`:
  27 files, 976 passed, 1 skipped.
- [Observed] **Criterion-2 probe.** A probe test file, run in the scratch
  worktree only and never committed, built a records root as follows:
  - every file of the real `.syzygy/governance/decisions/` copied in;
  - the five sitting act records rendered by the real
    `record_dossier_local_agent_acts.render_act`;
  - the five aggregate blocks rendered by `render_aggregate_block` and
    appended to `ACCEPTANCE-ACT-RECORD.md`, as `do_record` does;
  - the entry installed;
  - the v1.0 sign-off rendered by `record_versioned_signoff.render_record`,
    with its `render_aggregate` block appended.

  Results [Observed]:
  - **Base:** D9, RFC7-20, drawer, Anthropic, OpenAI and registry are all
    `ok`.
  - **P-104 row rewritten stem-free:** the row became `| P-104 | Resolved
    2026-10-07: the local-agent Redis sitting. The owner performed acts A, E,
    F, G and H, each a separate act; see the dedicated records | resolved |
    — | the sitting packet |`. All six sources stay `ok`.
  - **That row then moved to `DECISION-HISTORY.md`:** all six stay `ok`.
- [Observed] **Withdrawal probes on the same REAL root.** Each line below was
  added as a new decisions file unless stated otherwise.
  - Each of these refuses or withdraws exactly its own source and nothing
    else:
    - a second `| P-104 |` register line naming the tag;
    - the real P-104 row with a trailing CR;
    - the real P-104 row with a trailing space;
    - the statement act's recording tag
      `dossier-local-agent-redis-agent-anthropic-signed-2026-10-07`;
    - the drawer act identity `NO-EVIDENCE-DRAWER-REDIS-2026-10-07`;
    - the drawer Record ID `NO-EVIDENCE-DRAWER-redis-redis`;
    - the D9 Record ID;
    - the RFC7-20 Record ID;
    - the OpenAI act identity;
    - the sign-off record's full decisions path;
    - an `Act identity:` field line appended to the aggregate.
  - An unrelated note changed nothing.
  - Two forms were not seen. See note 2.
- [Observed] **Byte-equality probes.** Each was applied to all five act
  records:
  - All five sitting acts refuse for each of: a trailing space, an extra
    blank line, a missing final newline, an extra final newline, CRLF, a BOM,
    an NBSP for a space, and a date changed in `Act identity` only.
  - The sign-off refuses for a trailing tab, CRLF and an extra final newline.
  - These were accepted, and each is recorder-writable or recorder-adjacent:
    - a CR inside the `label` slot: Python's `Selection.validate` rejects only
      `\n`;
    - an act verdict `CONFIRM WITH EXCEPTIONS`: the recorder writes it;
    - a sign-off with `Review verdict: CONFIRM` and a non-`none` disposition:
      the recorder never writes this. See note 3.
- [Observed] **Stem-free rewrite applied to the real tree.** I rewrote the
  P-104 row in the scratch worktree's real `PENDING-OWNER-DECISIONS.md` the
  same way and re-ran both packages: 1 failed, 975 passed. The failure is at
  `gate-acts.test.ts`:263. See note 1.
- [Observed] **The scratch worktree was removed afterwards.**
- [Unknown] **The docs partition script was not run.** I did not run
  `check_docs_review_campaign_partition.py`, because it needs `cd` and this
  review allows only simple Bash. CI covers it.

## Round-2 dispositions

| Round-2 finding | Status at a6157cb0 | Evidence |
|---|---|---|
| 1 REVISE: the P-104 exemption hid any `\| P-104 \|` line | **Repaired** | `package-reader.ts`:76 sets `P104_ROW_SHA256`. `withoutCitedRows` (:104-108) blanks only the first line whose sha256 equals the pin, and only in `citedRows[].file === rel`, which is `PENDING-OWNER-DECISIONS.md`. Every other line is swept, a second identical copy included. Tests at `gate-acts.test.ts`:260-284 cover a duplicate row, a P-104 withdrawal line, the installed path in a P-104 line, an appended "Withdrawn.", an edited row, `P-1040`, and the row moved to history. My probes add CR and trailing-space variants, and both refuse [Observed]. The exemption cannot hide a withdrawal: the line it skips has fixed bytes, and blanking it cannot join two halves of a stem into a miss, because `carries` collapses whitespace runs into one dash. |
| 2 REVISE: readers accepted records that differ from the recorders' output | **Repaired** | `recorder-template.ts` builds an anchored regex: `^…$`, no `m` flag, every metacharacter escaped, and a repeated slot as a backreference. `templateFields` also requires `render(fields) === text`. `fromTemplate` adds the recorder's 64-hex ban on owner-selection slots. Each round-2 mutation is now a test: supersession removed or changed, phrase removed, phrase argument changed, second Provenance line changed, a second Provenance state, Effect changed, "Withdrawn by this record." appended, a recording tag for another date. They are at `gate-acts.test.ts`:286-309 for the acts and :310-329 for the sign-off, including the Owner selection, Review, Reviewed commit, Disposition, Scope A and "What this does not do" lines. My whitespace and encoding probes all refuse. **The cross-check is real.** `gate-acts.test.ts`:477-488 compares the TypeScript `template.render` with the stdout of `python3 -c … m.render_act(...)` and `vs.render_record(...)` (`recorder-fixtures.testkit.ts`:404-425). It is not TypeScript compared with TypeScript. Residual: note 3. |
| 3 NOTE: partial-path, basename, label and title forms unswept | **Repaired for the listed forms** | `sittingForm` stems now hold the artifact basename, label and title. `carriesLoosely` handles spaced and backticked tuples. Tests are at :337-361. Two record-title forms remain unswept: note 2. |
| 4 NOTE: drawer Subject unswept | **Repaired** | `fieldStems: ['(project:syzygy, repository:redis-redis)']` is read on field lines only (`gate-sources.ts` DRAWER_FORMS). Tests at :348 and :362-366. [Observed] `record_public_repo_admission_acts.py` writes no `Subject:` field line, so the row-1 act will not trip it. |
| 5 NOTE: P-104 moved to history refuses | **Dispositioned (fail-closed; superseded by lead plan)** | The test at :281-283 asserts the refusal. The lead's plan rewrites the row stem-free, and then the move refuses nothing (probe above). |
| 6 NOTE: v1.0 hard-wired | **Dispositioned** | The doc comment at `package-reader.ts`:295-297 names the v1.1 consequence. The PR body says the same. |
| 7 NOTE: stale PR body | **Repaired** | `gh pr view 377`, head `a6157cb0`: the body describes the template, the pinned exemption and the tree-following pins. It has a "Reader bytes: disclosure" paragraph: "It does not bind the bytes of `git-object-reader.ts` ... the owner's question E in `REDIS-LOCAL-AGENT-SITTING-BRIEF.md`. This PR does not decide it." |
| 8 NOTE: pin limits | **(a) unchanged, accepted; (b) repaired; (c) repaired** | (a) `real-tree.test.ts` still runs only its absent branch until the sitting. The synthetic worlds cover the present branch. (b) `gate-acts.test.ts`:471-476 compares every form's file with `Act.record` and `record_rel(pkg,'1.0')`, both obtained from the Python recorders through `recorderRecordPaths`. (c) `const KINDS = [` is fixed. |
| 9 NOTE: criterion 5 holds | Still holds | See criterion 4 below. |

### Criterion 4

- [Observed] **Tool and provider must both match.** `providerStatementGate`
  filters `r.agentTool === agentTool && r.provider === provider`.
  `providerStatement` requires exactly one `Agent tool:` line, and it must
  open with the form's tool name. The cross pairs are tested at the gate, at
  `init` and at `reverify`.
- [Observed] **The pins are not tautological.** `expectFollowsTree`
  (`gate-acts.test.ts`:99-113), the `real-tree.test.ts` sign-off arm and the
  `start-gates.test.ts` preflight pin each decide their expectation from
  `existsSync` of the recorder's path. None derives it from a reader. Each
  branch asserts literal states or reasons.
- [Observed] **Nothing is labelled accepted on the owner's behalf.**
  `gate-sources.ts` calls D9 "adopted by the owner's words, logged ... with
  no digest, which RFC3-16(a) does not read as an act". No PR byte calls a
  sitting act performed or in force.

## New findings

1. **NOTE: one test asserts that the exempt P-104 row exists, unconditionally.
   It fails once the installer rewrites the row stem-free, which goes against
   the lead's stated constraint.**

   Evidence: `gate-acts.test.ts`:262-263:

   ```ts
   const row = real(register).split('\n').find(line => line.startsWith('| P-104 |'))!;
   expect(row).toContain('public-git-source-acquisition-local-agent-v1.0');
   ```

   [Observed] With the real register's P-104 row replaced by the resolved,
   stem-free row, the suite fails at exactly this line: "expected '| P-104 |
   Resolved 2026-10-07: the lo…' to contain
   'public-git-source-acquisition-local-a…'". The other 975 tests pass. If the
   row is moved, `find` returns undefined and the test fails the same way.

   This is CI breakage, not a gate misbehaviour. The gate itself reads `ok`
   under the rewrite (probe above). That is why it is a NOTE rather than a
   REVISE. It will block the installer commit unless that commit also edits
   this test.

   Proposed repair: make the test independent of the tree.
   - Hold the pre-sitting row as a literal fixture in the test.
   - Assert `sha256(literal) === '05385b96…'`, by importing nothing from the
     module and comparing with the literal pin.
   - Exercise the exemption on that literal.
   - Optionally, add a tree-conditional assertion: if the real register holds
     a P-104 row whose hash equals the pin, it reads past; otherwise the real
     tree carries no needle on that row.

2. **NOTE: two remaining unswept forms are the artifacts' own record
   titles.**

   [Observed] Each of these leaves its source `ok` on the REAL root:
   - "Withdrawn: D9 for operator-agent runs — exact-bytes record", the H1 of
     `D9-IN-FORCE-RECORD.md`;
   - "Withdrawn: Agent-provider statement — redis-redis to anthropic", the H1
     of `AGENT-PROVIDER-STATEMENT-ANTHROPIC.md`.

   The forms carry the act record's title (`# Owner act — …`) as a stem, but
   not the artifact's own heading. Every identifier form the records carry
   does withdraw: Record ID, act identity, tag, path, basename, label, Subject
   and act title. Prose naming by an H1 title is not an identifier, which is
   why this is a NOTE.

   Proposed repair, either of:
   - add each artifact's H1 text (without `# `) as a stem, after a
     `git grep -F` over `decisions/` shows no hit;
   - list record headings beside the existing "a withdrawal worded without a
     stem ... is not seen" disclosure.

3. **NOTE: the sign-off reader accepts `Review verdict: CONFIRM` with a
   non-`none` Disposition, which `render_record` never writes.**

   `render_record`:554 writes `Disposition: {disposition or "none"}`, and
   `record()`:677 passes a disposition only for `CONFIRM WITH EXCEPTIONS`.
   `readVersionedSignoffState` (`package-reader.ts`:335) refuses only the
   converse, CWE with `none`.

   [Observed] The probe "confirm with a disposition" returns `ok`. Round 2
   proposed "`Disposition: none` exactly when the verdict is `CONFIRM`".

   [Inferred] There is no fail-open effect. The record still binds the same
   entry SHA-256 under a CONFIRM verdict, so it grants nothing more.

   Two related cosmetic gaps: the `SLOT.line` patterns accept a
   whitespace-only quote, label or description, and a CR in the quote. The
   recorders reject the whitespace-only form. A whitespace-only quote cannot
   carry "Extend Scope A", so the sign-off is unaffected.

   Proposed repair: also refuse `verdict === 'CONFIRM' && disposition !==
   'none'`. Optionally tighten `SLOT.line` to `[^\n]*\S[^\n]*`.

4. **NOTE: the cross-check covers one field set per recorder.**
   `gate-acts.test.ts`:477-488 renders with verdict `CONFIRM` and no
   disposition only.

   [Observed] I compared the Python source directly, and the conditional
   parts are plain substitutions:
   - `render_record` `Disposition: {disposition or "none"}`;
   - `render_act`, which has no verdict-dependent text.

   The port is therefore faithful today. Nothing tests that, though.

   Proposed repair: add one cross-check case with `CONFIRM WITH EXCEPTIONS`
   and a disposition path, for the sign-off.

## Criteria summary

- **Criterion 1: met.** Both round-2 REVISEs are repaired. Every note is
  repaired or dispositioned.
- **Criterion 2: met** [Observed].
  - Every identity form the records carry defeats the grant.
  - The exemption is byte-pinned, first copy only, register only, and
    cannot hide a withdrawal.
  - The real tree has no false refusal.
  - With every act recorded by the real renderers, over today's
    `decisions/`, aggregate blocks included, every source is `ok`.
  - It stays `ok` with the P-104 row rewritten stem-free, and with that row
    moved to history.
- **Criterion 3: met** [Observed].
  - The template is anchored and render-equal.
  - Every slot type, extra or missing line, whitespace and trailing-content
    mutation refuses.
  - The TypeScript port is checked against the Python recorders' output.
  - Residual: note 3, which is not fail-open.
- **Criterion 4: met.**
  - The pins follow the tree and are not tautological.
  - Tool and provider must match exactly.
  - Nothing is labelled accepted on the owner's behalf.
  - The PR body is current and makes the reader-bytes disclosure.
  - One test breaks the "no unconditional exempt-row assertion" constraint
    (note 1). It is fail-closed in CI.

## Counts

0 REVISE; 4 NOTE (new findings 1–4). Round-2 findings 1 and 2 are repaired.
Of round-2's notes 3–9, six are repaired or dispositioned, and note 8(a) is
accepted as is.
