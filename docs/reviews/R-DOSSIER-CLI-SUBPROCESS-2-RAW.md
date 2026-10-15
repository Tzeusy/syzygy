# Review R-DOSSIER-CLI-SUBPROCESS-2
Reviewed commit: b386b433eceaf0cffdbbb8c125c93328083e0f74
Subject SHA-256: c5b3a43228276d5910e16c592278f7428775e378f412c0f27986fdf8767bdd20
Verdict: REVISE

Reviewer: fresh-context reviewer; not the author. Round 2, confirming round over repaired bytes.
Brief: `.syzygy/governance/contracts/candidates/dossier-local-cli-subprocess-runner/REVIEW-BRIEF.md`, Round 1 section
(stopping-rule sentence excepted, per dispatch). Focus: egress and trust boundary.
Companion read: `.syzygy/governance/decisions/OWNER-DIRECTION-DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15.md`,
sha256 da3a6726e1c668ef8a57a19e8093bf9f8fe9a792d446e83df83757d1577751c7 (computed by sha256sum; matches dispatch).

## What was checked

- [Observed] `git rev-parse HEAD` = b386b433eceaf0cffdbbb8c125c93328083e0f74; both digests computed by `sha256sum`
  and equal to the dispatch's.
- [Observed] Read in full: the delta, the direction record, the round-1 raw, `ROUND-1-DISPOSITIONS.md`, the brief.
- [Observed] `claude --help` and `codex exec --help` read in full on this host. Every help quotation in the delta's
  table (SEMANTIC-DELTA.md:235-246) matches the help text, including the `--restricted` text "managed settings and
  --settings still apply; add --strict-mcp-config to skip MCP servers too", "refuses bypassPermissions", and Codex
  `--ignore-user-config` "auth still uses `CODEX_HOME`".
- [Observed] `git grep -F REQ-polaris-generation-045 HEAD` over `openspec .syzygy packages docs apps scripts`: hits
  only in this package (REVIEW-BRIEF.md:13, SEMANTIC-DELTA.md:13,26,148), PENDING-OWNER-DECISIONS.md:1298 (P-111) and
  docs/README.md:144 (campaign row). The ID is free in `openspec/`.
- [Observed] Candidate REQ-041 (spec.md:63) and REQ-042 (spec.md:112) quotations in the delta (lines 31-33, 114-116)
  match; REQ-042 still reads "Network access SHALL be left to the agent tool".
- [Observed] `POLARIS-DOSSIER-LOCAL-AGENT-MODE-DIRECTION.md` item 2 (lines 68-74): "The operator's agent session
  sending target content to its own provider is the operator's own act ... must disclose that the agent read the
  clone without restriction". Supports the delta's paragraph 5 citation (SEMANTIC-DELTA.md:146).
- [Observed] `packages/polaris-dossier/src/polaris.ts`: :330-332 `claudeExecutable()` with `SYZYGY_POLARIS_AGENT`;
  :343-344 copy of `~/.claude/.credentials.json`; :395 `--dangerously-skip-permissions` when
  `state.authorSkipPermissions`; :400 `--add-dir` with the clone for author and inventory. Evidence bullet
  (SEMANTIC-DELTA.md:278-286) is accurate.
- [Observed] P-111 (PENDING-OWNER-DECISIONS.md:1298) carries Q1 and Q2 as the delta's lines 321-329 say.
- Not read, per the brief: any target repository, any state root or run directory. No `syzygy` command, no network
  call.

## Round-1 finding closure

| # | Class | Status | Reason |
|---|---|---|---|
| 1 | revise | not closed (in part) | Closed for the process environment and tool options: SEMANTIC-DELTA.md:138 "The operator SHALL declare for the run ... the model provider", "a process environment it writes and records in full, from an allow-list", provider-selecting options "absent or set by Syzygy"; scenario :170-174; Case/Falsifier :207, :211. Not closed for the third vector the round-1 text named, "a Claude Code managed-settings `env` block" (raw line 49): the repair leaves managed settings in effect and only disclosed (:140). See new finding 1. |
| 2 | revise | closed | Oracle scoped to "built non-test runtime output and the lockfile" with endpoint hosts and credential file paths (:209); per-process connection record in a network namespace (:207-208) gives the connection clause (:192) an observable. Residual wording in new finding 3. |
| 3 | revise | closed | Project-level instruction files and "the settings, instruction and MCP files of every directory the session can read, the clone included" excluded (:140); unobserved exclusion refuses (:140 "A source counts as excluded only once its exclusion has been observed ... until then it counts as not excluded"); clone scenario :164-168 and Case :207. Residual coverage gap in new finding 4. |
| 4 | revise | closed | Paragraph 5 (:146) states the tool can send any class in the clone, rests it on item 2 and Q2 "not on the statement", restricts Syzygy's own packets to listed classes, and mandates the run-page disclosure; scenario :199-203. The refuse arm is put to the owner (:321-329; P-111 Q2). Direction record :118-125 names the limit. Arm choice is the owner's (note 6). |
| 5 | note | closed | "Could grant" gone; refusal unit is the run throughout (:140, :162, :168); managed settings recorded and disclosed, not read (:140). |
| 6 | note | closed | :104-110 quotes the statement's "operator-agent runs" scope and labels reach to launched sessions Inferred on Q2. |
| 7 | note | closed | :138 "SHALL read no provider credential except to copy the tool's own credential file, unparsed ... and SHALL record that it did"; file in oracle scope (:191, :209). |
| 8 | note | closed | Codex rows for `-p`, `-c`, `--oss`, `--local-provider` and both bypass flags (:244-245); hooks and user-level `AGENTS.md` under `CODEX_HOME` Unknown and refused until observed (:245). |
| 9 | note | closed | :138 "SHALL NOT start the tool in any mode that bypasses the tool's permission checks"; Falsifier :211; evidence :282-284 names `--dangerously-skip-permissions`. |
| 10 | note | closed | :192 "no process that is not the declared tool or a process it started opens a connection to a model-provider endpoint". |
| 11 | note | closed | No repair needed; :26-30 now cites the round-1 sweep. The ID is still free in `openspec/` at HEAD (sweep above); docs/README.md:144 is a new, expected hit. |

## New findings

1. [revise] An unexcludable settings layer can redirect the provider while the run proceeds as statement-covered.
   SEMANTIC-DELTA.md:140: "Administrator-managed settings, which neither tool offers a flag to exclude, SHALL be
   recorded as not excluded, labelled Observed as Syzygy's own finding about the tool, and disclosed on the run page;
   Syzygy does not read them." The same requirement's provider guarantee (:138, "every provider-selecting option of
   the tool ... either absent or set by Syzygy to the declared provider") and scenario :173 ("the session's effective
   provider is the declared one") cover only what Syzygy passes. [Observed] the help confirms managed settings still
   apply under `--restricted` ("managed settings and --settings still apply"). [Inferred, from Claude Code's settings
   model, not from the help text] a managed settings file can carry an `env` block or provider-selecting keys
   (third-party provider switch, base URL, `apiKeyHelper`) that the tool applies after Syzygy writes the environment.
   Under the current text such a run is not refused: it starts, sends target content to a provider no statement
   covers, and its page names the Anthropic statement with a generic "managed settings not excluded" line. Brief
   item 1 asks the delta to "keep every transmission ... inside an act already in force ... and refuse otherwise";
   this is the case round-1 finding 1 named (raw line 49) and the repair did not address. The falsifier (:211, "a
   provider-redirecting variable or option reaches the tool") cannot fire, since the redirect does not reach the tool
   from Syzygy, and a stand-in tool will not apply managed settings at all.
   Repair (either): (a) have Syzygy inspect only the provider-selecting and `env` keys of the tool's managed settings
   (tool configuration on the operator's host, not target content) and refuse the run, naming the key, where any
   names or could select a provider other than the declared one, with a Case seeding a managed `env` redirect in an
   attended run; or (b) weaken :173 and :138 to say the effective provider is guaranteed only where no managed layer
   is present, record the effective provider as Unknown otherwise, and make the run-page disclosure say specifically
   that a managed layer can change the provider the statement was checked against.

2. [note] The environment allow-list wording admits the declared provider's credential variables, which the
   credential and inspection clauses forbid reading. SEMANTIC-DELTA.md:138: "an allow-list that admits no variable
   selecting, redirecting or authenticating a model provider other than the declared one" — read contrapositively, an
   authenticating variable for the declared provider (e.g. `ANTHROPIC_API_KEY`) may be admitted, but writing it means
   reading it, against the same paragraph's "SHALL read no provider credential except to copy the tool's own
   credential file" and the oracle's "no read of a provider credential variable" (:191). It also re-opens the API-key
   route the delta rejects for `--bare` (:238). Say the allow-list admits no provider-authenticating variable at all.

3. [note] The Falsifier drops the scenario's credential-file exception. SEMANTIC-DELTA.md:191 excepts "the recorded
   copy of the tool's own file"; :211 reads "a provider SDK, API client, endpoint host or credential read is present
   in runtime output" with no exception, and the oracle (:209) lists "credential file paths". A conforming build
   necessarily names the tool's credential path to copy it (polaris.ts:343), so the Falsifier as written fires on
   every conforming build. Carry the exception into :211.

4. [note] The excluded-source list and the Cases omit skills, custom agents, commands and output styles in the
   operator home and the clone. :140 enumerates settings layers, instruction files, "settings, instruction and MCP
   files", plugins, hooks and ambient MCP; :160 and :166 seed allow rules, hooks, plugins, MCP servers and instruction
   files. [Observed] `claude --help` `--safe-mode` lists "CLAUDE.md, skills, installed plugins, hooks, MCP servers,
   custom commands and agents, output styles" as distinct customization classes, and `--restricted` speaks only of
   "settings files" and MCP. A clone-side `.claude/skills/` or `.claude/agents/` is target-controlled instruction text.
   Paragraph 2's "in no other way" arguably covers them, but no Case would catch one. Name them and seed them.

5. [note] The prototype's stand-in override is a substitution route the requirement forbids, and the downstream list
   does not name it. :138 "Syzygy SHALL NOT search for, substitute or fall back to another tool, path"; [Observed]
   polaris.ts:330-332 resolves `SYZYGY_POLARIS_AGENT` from the environment in place of `claude`. Downstream impact
   (:300-302) should say the stand-in is declared by absolute path like any tool, not taken from the environment.

6. [note] Arm choice, for the owner only. The direction record still says content may go through a launched CLI
   "only where an act already in force covers that repository, that content class and that agent tool with its
   provider" (direction :99-101), while the delta's drafted arm lets unlisted classes go with disclosure (:146). The
   record's dated paragraph (:118-125) names the tension and defers it to P-111 Q2; this is honest and not a defect of
   the delta. Recorded so the owner sees both sentences together.

Counts: 1 revise, 5 notes; round-1 closure 10 closed, 1 not closed in part (finding 1).
