# R-POLARIS-DOSSIER-GATE-SOURCES-2
Verdict: REVISE
Reviewed commit: 014545fc5f2d39577eacf56d63edaeb42ce79bd8
Subject: PR #377 (syzygy-qkea.21)

Reviewer: fresh-context independent reviewer, 2026-10-07, round 2. Scope: `git diff origin/main...014545fc` (16 files, +853/-101). Any later evidence-only commit is out of scope. No external or target repository content was fetched.

## Governing clauses (quoted)

- RFC3-16(a) (`.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md`:168, located via `DIRECTIVE-REGISTER.md`:277): "An **authorization-bearing governance artifact** is any artifact whose presence **authorizes a dangerous act, unblocks or widens a claim class** ...". Round 1 quoted its effect rule: "An effective owner act is an actual human owner act whose record is current, attributable, scope-matched and bound to the artifact's exact digest under RFC3-16(b)."
- RFC3-16 (same file, :134-137): "The **effective** lifecycle status ... is determined by an **owner-act record** (RFC3-16(a)/(b)) binding the act to the artifact's **exact immutable content digest**".
- polaris-dossier-local-agent-mode v1.1 (`openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md`:11, quoted in round 1): "its withdrawal SHALL refuse further steps of any run that relies on it"; and (:13) "withdrawal of the observation consent, the registry entry or a policy act refuses every later step of the run."
- The recorders' own revocation line, written into every record:
  - `scripts/record_dossier_local_agent_acts.py` `render_act`: "Supersession / revocation: supersedes nothing; revoked only by a later exact owner act naming it."
  - `scripts/record_versioned_signoff.py` `installed_lines`: "Supersession / revocation: supersedes nothing; revoked only by a later exact owner act naming it".
  - The latter's docstring calls the supersession RFC3-16(b) item 8.

## Verification performed

- [Observed] Scratch worktree at 014545fc, `npm ci`, then `vitest run packages/polaris-dossier packages/polaris-generation-consent`: 23 files, 879/879 passed.
- [Observed] `.syzygy/governance/decisions/` is byte-identical between 014545fc and origin/main (5c78d3ec): `git diff --stat` printed nothing. No sitting act or sign-off record exists on either.
- [Observed] Two probe test files ran in the scratch worktree only; the worktree was removed afterwards. Each probe builds a records root with every sitting act and the v1.0 sign-off rendered by the real recorders, the same way `gate-acts.test.ts` `world()` does. Each run was done twice:
  - "MIN": one unrelated decisions file;
  - "REAL": every file of the checkout's real `decisions/` copied in.
  
  Each probe then adds one decisions file and reads every gate source. The results are quoted in the findings below.
- [Observed] REAL baseline: with every act and the sign-off recorded over today's real `decisions/` tree, every source is `ok`: D9, RFC7-20, drawer stated, both statements, and the registry. The PENDING-OWNER-DECISIONS.md P-104 row is the only real file that carries a swept needle (fixed-string `git grep` over `decisions/` for every stem, record basename and subject tuple returned only that line). That answers criterion 2 for today's tree.
- [Unknown] I did not run `scripts/check_docs_review_campaign_partition.py`. It reads the git tree from the current directory, and the simple-Bash rule forbids `cd`. CI covers it.

## Round-1 dispositions

| Round-1 finding | Status at 014545fc | Evidence |
|---|---|---|
| 1 REVISE: statement not withdrawable by Record ID or Subject | **Repaired** | `gate-sources.ts` `statementForm` adds `recordId.toLowerCase()` and the subject tuple to the stems. `namesDigestBoundAct` field-line regex now includes `record\s+id\|subject` (package-reader.ts diff). Tests at `gate-acts.test.ts`:221-245 cover Record ID, case/underscore folding, Subject on a field line and in prose, and the aggregate field-line arm, each against only its own statement. Probe [Observed]: the act identity (`AGENT-PROVIDER-REDIS-ANTHROPIC-2026-10-07`), the recording tag (`dossier-local-agent-redis-agent-anthropic-signed-2026-10-07`), the full artifact path and a space-separated Record ID each withdraw only the Anthropic statement. Residual forms: new findings 3 and 4. |
| 2 REVISE: sign-off not withdrawable by tag; test asserted the fail-open | **Repaired, but the exemption is too wide (new finding 1)** | `LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM.stems` adds `...-sign-off` and the tag (package-reader.ts). The old `gate-acts.test.ts`:195 `ok` assertion now expects `refused` (:207-214). New tests at :247-256 cover the tag, case and both sign-off spellings. Probe [Observed]: "public-git-source-acquisition-local-agent v1.0" (with a space) refuses, and so does the sign-off record's own basename. |
| 3 NOTE: reader bytes unbound (owner question) | **Open, not stated in the PR body** | The PR body (gh pr view, 2026-10-07) has no sentence on the reader-bytes gap. See new finding 7. |
| 4 NOTE: laxer parse (Owner/Provenance/Scope/A1) | **Partly repaired** | `recorderLines` (package-reader.ts) now requires `Owner: Tzeusy`, the first Provenance line, the A1 line and the exact Scope line. Tests at `gate-acts.test.ts`:273-293. Other recorder lines are still optional or unchecked: see new finding 2. |
| 5 NOTE: mutant gaps | **Repaired in tests**; mutant record still pending (out of scope) | - Fenced second table, separator row and third row: `gate-acts.test.ts`:295-305.<br>- Duplicated Record ID/Subject for drawer and statement: :311-312 and :327-328.<br>- `withdrawn` is no longer hard-coded: `providerStatement` sets `withdrawn: true` when the refusal carries `namedBy`, and the tests at :213 and :231-233 assert the "is withdrawn" disclosure. |
| 6 NOTE: fail-closed spots hold | Still holds | Re-run in the 879-test pass. |
| 7 NOTE: real-tree pins will break at the sitting; stems in a sitting log | **Repaired (pins tree-conditional)**; the log caution still applies | `gate-acts.test.ts`:84-111 `expectFollowsTree`; `real-tree.test.ts` signoff arm; `start-gates.test.ts` preflight `recorded(stem)`. Criterion-3 analysis is below. New finding 5 is a concrete case of the log caution. |
| 8 NOTE: exact (tool, provider) scope | Still holds | `init.ts`:124 and `reverify.ts`:152 pass `agentTool` and `agentProvider`. Tests at `gate-parts.test.ts`:134-166, plus the `start-gates.test.ts` Codex/Anthropic case at init and the Codex/OpenAI-vs-Claude Code case at reverify. |

### Criterion 3: the tree-conditional pins

[Observed] The pins are not tautologies:

- `expectFollowsTree` (`gate-acts.test.ts`:97-111) decides the expectation from `fs.existsSync` of each act's dedicated record path. It does not derive it from any reader.
- When the record is present it expects `ok`, with a literal identity shape (or the literal tag for the registry).
- When it is absent it expects the literal not-established, unstated or absent text.

A gate that refuses a present record, or that admits with no record, fails either branch. Both branches run on synthetic worlds at :87-92:

- no records;
- every record;
- each act alone;
- the sign-off alone.

The real checkout runs the absent branch (:84-86).

The `start-gates.test.ts` preflight pin and the `real-tree.test.ts` sign-off pin also decide from file existence. Limits are in new finding 8.

## New findings

1. **REVISE — the P-104 exemption hides any line that starts with `| P-104 |`, so a withdrawal written as such a row leaves the registry sign-off `ok` (criterion 1).**

   Evidence: `package-reader.ts` `findActRecord` removes every line of `PENDING-OWNER-DECISIONS.md` for which `line.startsWith(prefix)` holds before it sweeps. `LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM.citedRows` sets `prefix: '| P-104 |'`. The rule has no pin on the row's bytes and no limit on the number of matching lines.

   Probes [Observed], both on MIN and REAL:
   - The real register plus a second line `| P-104 | Withdrawn by the owner: public-git-source-acquisition-local-agent-v1.0 |`: registry `ok`.
   - A register holding only that line: `ok`.
   - `| P-104 | Withdrawn: .syzygy/governance/declarations/adapter-registry/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-CANDIDATE.json |`: `ok`. Even the full installed path is hidden.

   What does hold [Observed]:
   - The exemption applies only to the registry form. A P-104-prefixed line naming `AGENT-PROVIDER-redis-redis-anthropic` withdraws that statement.
   - It applies only at `decisions/PENDING-OWNER-DECISIONS.md`: a nested `sub/PENDING-OWNER-DECISIONS.md` refuses.
   - `| P-1040 |` is not exempt (test at :266).

   The PR's own test (:257-271) checks P-105 and P-1040 but never a second or edited P-104 line.

   [Inferred] Recording a ruling against a register row is the register's normal use. "P-104: sign-off withdrawn" is a likely form for an owner withdrawal.

   Proposed repair: exempt exactly one line, and only while its bytes are the pinned row:
   - pin it the way `CITATION_ALLOWLIST` pins a file (a sha256 of the row line, or the exact row text in the form);
   - sweep every other line, a second identical copy included.

   When the sitting resolves or edits the row, the same commit re-pins it. The tree-conditional real-tree pin then catches a forgotten re-pin as a refusal, which is fail-closed. Add tests for:
   - a second P-104 line naming the tag;
   - the P-104 row with "withdrawn" appended;
   - the installed path inside a P-104 line.

2. **REVISE — the readers still accept records that differ from the recorders' fixed output in RFC3-16(b) item 8 (supersession), in the owner's phrase argument, and in several sign-off lines (criterion 4).**

   Probe [Observed]: each mutation was applied to all five dossier act records and the sign-off record. Every one left every source `ok`, D9, RFC7-20, drawer, both statements and the registry alike:
   - **Supersession removed:** the `Supersession / revocation:` line (both physical lines) deleted.
   - **Supersession replaced:** "supersedes nothing" changed to "supersedes the earlier act". `supersessionText` (package-reader.ts:132-145 region) returns `''` when the line is absent and accepts any text. Neither `readDigestBoundActState` nor `readVersionedSignoffState` compares it to the recorder's sentence.
   - **Phrase removed:** the `text` fence carrying the phrase `<LABEL>: <argument>` deleted from the act records.
   - **Phrase argument replaced:** the phrase's argument changed to `0`×64 while `Exact digest (SHA-256):` keeps the real digest. The phrase is what the owner's act takes ("The act takes this phrase, whose argument is this record's row"). The reader binds only the `Exact digest` line and never checks that the two agree.
   - **Provenance second line changed:** the line after `Provenance state: ...` replaced ("explicitly selected by the owner's option selection recorded below" in the act records, "the owner's option selection quoted above" in the sign-off). `recorderLines` matches only the first physical line.
   - **Sign-off lines removed:** `Owner selection:`, `Review:`, `Reviewed commit:`, `Disposition:`, `Scope A extension:` and the `## What this does not do` section each deleted. `readVersionedSignoffState` requires none of them, although `parse_record` in `record_versioned_signoff.py` treats the first five as mandatory ("record carries no `{key}:` line").
   - **Text appended:** "Withdrawn by this record." added to the act's own record. The sweep skips `form.file`, and no check holds the record to the recorder's template.

   [Inferred] Impact: a writer who can forge the record can forge these lines too, which is why round 1 rated this class a NOTE. Criterion 4 for this round is "Readers require every line the recorders write; no laxer parse". Supersession is an RFC3-16(b) item the recorder documents as such, and the phrase is the act's own argument.

   Proposed repair, either of:
   - (a) re-render: rebuild the expected record from the parsed fields with the recorder's fixed template, the free-text slots excepted (the selection quote, question opening, label and description, frozen and review provenance). Require byte equality for every fixed line and section, including both Supersession lines, both Provenance lines and the fenced `<LABEL>: <digest>` phrase, whose digest must equal `Exact digest`.
   - (b) at minimum: `one()` each of those lines with its exact recorder text. Require the phrase's argument to equal the Exact digest line. Require the sign-off's `Owner selection`, `Review`, `Reviewed commit` and `Disposition` lines, with `Disposition: none` exactly when the verdict is `CONFIRM`.

   Add one test per mutation above.

3. **NOTE — partial-path, basename, label and title forms do not withdraw. The repository's own citation style is one of them, and adding these needles costs nothing on today's tree (criterion 1).**

   Probes [Observed]: each of the following left its source `ok` on MIN and REAL:
   - `contracts/candidates/dossier-local-agent-acts/instances/redis/AGENT-PROVIDER-STATEMENT-ANTHROPIC.md`. The P-104 row itself cites the package in this governance-relative form.
   - The bare basename `AGENT-PROVIDER-STATEMENT-ANTHROPIC.md`.
   - `NO-EVIDENCE-DRAWER-STATEMENT.md`, `in-force/D9-IN-FORCE-RECORD.md` and `RFC7-20-READING-IN-FORCE-RECORD.md`.
   - `POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-CANDIDATE.json` and `declarations/adapter-registry/POLARIS-...CANDIDATE.json`.
   - The phrase labels "CONSENT TO AGENT PROVIDER ANTHROPIC FOR REDIS-REDIS" and "BIND D9 TO EXACT BYTES FOR OPERATOR-AGENT RUNS".
   - The record titles "agent-provider statement for redis/redis: Claude Code with Anthropic" and "Public Git source acquisition, local-agent version — version-tagged sign-off v1.0".
   - The Subject written with spaces after the colons, or with each part in its own backticks: `(project: syzygy, ...)`, ``(`project:syzygy`, `repository:redis-redis`, `agent-provider:anthropic`)``.
   - "the public-git-source-acquisition-local-agent entry, signed off at 1.0" and the bare package key.

   The recorders say revocation is by "a later exact owner act naming it". The full act identity, the tag, the full path and the Record ID all work, so this is a NOTE, not a REVISE.

   [Observed] A fixed-string `git grep` of `decisions/` for `AGENT-PROVIDER-STATEMENT`, `NO-EVIDENCE-DRAWER`, `D9-IN-FORCE`, `RFC7-20-READING-IN-FORCE` and `LOCAL-AGENT-CANDIDATE.json` returns nothing. Adding each artifact's basename, and the phrase label, as stems therefore adds no false refusal today.

   Proposed repair: add the artifact basename and the act label to each form's stems. For the Subject, match the tuple after stripping backticks and the whitespace after `:`. Or state these forms as unswept in the reader's doc comment, beside the existing "a withdrawal worded without a stem ... is not seen".

4. **NOTE — the drawer record's Subject is not swept (criterion 1).**

   Probe [Observed]: "Subject: `(project:syzygy, repository:redis-redis)` drawer statement withdrawn" leaves the drawer stated. [Observed] No file in `decisions/` carries `repository:redis-redis` today.

   [Inferred] The Redis observation consent's own act record may carry the same tuple once row 1 is recorded. A bare tuple stem could then false-refuse, so this needs care.

   Proposed repair: sweep the exact parenthesized tuple on `Subject:` field lines only, and check that against the row-1 recorder's output. Or disclose the gap.

5. **NOTE — moving the P-104 row to `DECISION-HISTORY.md` after the sitting refuses the registry gate (criteria 2, 3).**

   Probe [Observed]: the real P-104 row written into `DECISION-HISTORY.md` makes the registry `refused` on MIN and REAL, because the exemption is file-bound. [Observed] The register's convention moves resolved rows there: `DECISION-HISTORY.md`:30 holds the resolved P-103 row.

   This is fail-closed, and the tree-conditional pin would catch it in CI. It is still a false refusal that the sitting's own housekeeping would cause.

   Proposed repair: put this in the sitting's install checklist. With finding 1's byte-pinned row, pin the row wherever it lives; or have the history row cite the sign-off without the tag.

6. **NOTE — the registry form is hard-wired to v1.0, so any later sign-off of the package refuses the gate until code changes.**

   [Inferred, from the stems] A `PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-SIGNOFF-v1.1.md` file carries the `...-signoff` stem, and `findActRecord` treats it as a withdrawal of v1.0. The recorder says "a later edit is a new version, never a retirement of the earlier one", but the gate reads it as one.

   Fail-closed, so acceptable. Name it in the form's doc comment so that a v1.1 sign-off is known to need a reader change in the same commit.

7. **NOTE — the PR body is stale and omits the disclosure round 1 asked for.**

   [Observed] The body still says "A real-tree test pins every source as absent on this checkout"; the pins are now tree-conditional. Its verification block is at `ff832300`, and it does not describe the round-1 repairs. It has no sentence on round-1 note 3: the registry gate admits any `git-object-reader.ts` bytes under a v1.0 sign-off.

   Proposed repair: update the body, and state the reader-bytes gap with a pointer to the owner's open question in `REDIS-LOCAL-AGENT-SITTING-BRIEF.md`.

8. **NOTE — limits of the tree-conditional pins (criterion 3).**
   - (a) [Observed] `real-tree.test.ts`'s sign-off arm runs only its absent branch until the sitting. Its present branch is not exercised in that file; `gate-acts.test.ts` covers the same predicate on synthetic worlds.
   - (b) [Inferred] Every pin keys on the reader's own filename, a literal in the test. If the recorder ever wrote a different path, the pin would read "absent", the gate would agree, and CI would stay green while a recorded act went unread. [Observed] Today the recorder's `Act.record` is `DECISIONS / f"DOSSIER-LOCAL-AGENT-{self.stem}-ACT.md"` and `record_rel` for the sign-off. Both agree with the forms, but no test pins that agreement. Add one test asserting `m.ACT_BY_KEY[k].record` and `record_rel(pkg, '1.0')` (via the Python recorders) equal each form's `file`.
   - (c) Cosmetic: `real-tree.test.ts` `const KINDS =[` is missing a space.

9. **NOTE — criterion 5 holds.** [Observed]
   - The gate filters `r.agentTool === agentTool && r.provider === provider` (`gate-sources.ts` `providerStatementGate`).
   - `init.ts`:124 and `reverify.ts`:152 pass the declared pair.
   - The record must carry exactly one `Agent tool:` line that opens with the form's tool name.
   - The cross pairs are tested at the gate, at `init` and at `reverify`.
   - No PR byte labels a sitting act accepted or in force. `gate-sources.ts` describes D9 as "adopted by the owner's words, logged in the doctrine amendment log with no digest, which RFC3-16(a) does not read as an act", which matches the record.

## Counts

2 REVISE (findings 1, 2); 7 NOTE (findings 3–9). Round-1 findings 1 and 2 are repaired; note 4 is partly repaired; note 3's disclosure is still missing.
