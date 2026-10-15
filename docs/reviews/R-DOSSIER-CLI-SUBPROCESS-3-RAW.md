# Review R-DOSSIER-CLI-SUBPROCESS-3
Reviewed commit: d0f776d8e584fa188674fa7f47053253027c776b
Subject SHA-256: 7228e9aa96cd68c7132559393068d3709659b52924140708e22ff6d17b5ae39b
Verdict: REVISE

Reviewer: fresh-context reviewer; not the author. Round 3, confirming round over repaired bytes.
Brief: `.syzygy/governance/contracts/candidates/dossier-local-cli-subprocess-runner/REVIEW-BRIEF.md`, Round 1 section
(stopping-rule sentence excepted, per dispatch). Focus: egress and trust boundary.
Companion read: `.syzygy/governance/decisions/OWNER-DIRECTION-DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15.md`,
sha256 da3a6726e1c668ef8a57a19e8093bf9f8fe9a792d446e83df83757d1577751c7 (computed by sha256sum; matches dispatch).

## What was checked

- [Observed] `git rev-parse HEAD` = d0f776d8e584fa188674fa7f47053253027c776b. `sha256sum` of the subject and the
  companion both equal the dispatch's values.
- [Observed] Read in full: the subject, the companion direction record, the brief, the round-2 raw,
  `ROUND-2-DISPOSITIONS.md` and `ROUND-2-REPAIRS.md`. The round-1 closure is taken from the round-2 raw (line 41
  onward), which was read in full.
- [Observed] `claude --help` on this host: the `--bare` quotation at SEMANTIC-DELTA.md:249 ("Anthropic auth is
  strictly ANTHROPIC_API_KEY or apiKeyHelper via --settings (OAuth and keychain are never read)") matches the help
  text, and so do the `--restricted` text ("managed settings and --settings still apply; add --strict-mcp-config to
  skip MCP servers too") and the `--safe-mode` text ("Auth, model selection, built-in tools and plugins, and
  permissions work normally"). I did not re-run `codex exec --help`, because the round-2 repairs touched no Codex row.
- Consistency checked across paragraphs 1 to 5 (:138-146), every scenario (:152-214), the Case, Observable, Oracle
  and Falsifier (:218-222), the `--bare` row (:249), Downstream impact (:311-326) and the Review section (:346-359).
- Not read, per the dispatch: any target repository, any state root or run directory. I ran no `syzygy` command, no
  npm or node script, and made no network call.

## Round-2 finding closure

| # | Class | Status | Reason |
|---|---|---|---|
| 1 | revise | closed | :140 "Before any session starts, Syzygy SHALL read, from the tool's administrator-managed settings at the locations the declared tool and version documents, only the keys that can select, redirect or authenticate a model provider, its environment block included"; "Where any such key names or could select a provider, endpoint or credential route other than the declared provider, Syzygy SHALL refuse the launched run, naming the key and file"; unreadable or unparsable location, and unknown keys for the version, also refuse with Unknown. Scenario :176-180, Case :218 ("administrator-managed settings seeded, in an attended run, with a provider-redirecting environment block, and made unreadable"), Falsifier :222 ("a run starts while managed settings redirect the provider or cannot be read"). This is arm (a), and it fails closed. Residuals: new findings 2 and 3. |
| 2 | note | closed, with the lead's departure | The contrapositive loophole is gone: :138 "an allow-list that admits no variable selecting, redirecting or authenticating a model provider, with one exception". The exception replaces the disposition's "admit no credential variable" wording. Judged under task 2 in new finding 1, which finds it not fully fail-closed. |
| 3 | note | closed | Oracle :220 "excepting exactly two uses: the copy of the tool's own credential file and the pass-through of the one declared credential variable"; scenario :202 and Falsifier :222 ("a credential read other than the two excepted uses") now agree. A third use, introduced by the finding-1 repair, is new finding 2. |
| 4 | note | closed | :140 "skills, custom agents, custom commands and output styles, whether in the operator's home or in any directory the session can read, the clone included, other than the skills Syzygy names"; scenario :166, Case :218 and Falsifier :222 name them. |
| 5 | note | closed | :138 "SHALL take the executable from that declaration alone, never from an environment variable or other ambient setting; a test stand-in is declared by absolute path like any tool"; scenario :182-185; Case :218 seeds `SYZYGY_POLARIS_AGENT`; Downstream :313-315 says to "stop resolving `SYZYGY_POLARIS_AGENT` from the environment". |
| 6 | note | carried to the owner (no repair due) | :336-344 leaves the arm to P-111 Q2, unchanged, as both the disposition and the repair map say. Restated as new finding 4. |

## New findings

1. [revise] The declared-credential-variable exception admits whatever variable the operator names, and nothing
   checks it. SEMANTIC-DELTA.md:138 reads: "where the declared provider authenticates the tool through a variable,
   the operator SHALL name that one variable in the run declaration, and Syzygy SHALL pass it from its own
   environment to the tool unparsed", and then "The allow-list SHALL admit nothing else that selects, redirects or
   authenticates a provider". [Observed] Nothing requires Syzygy to check that the named variable only
   authenticates, rather than also selecting or redirecting a provider or endpoint. No refusal is stated where it
   does. Because the value is passed unparsed, the value cannot show the difference either: only the name can. The
   words "nothing else" exempt the declared variable from the select and redirect bars as well as the authenticate
   bar.
   [Inferred] Suppose an operator names a base-URL or provider-switch variable as "the credential variable". It
   reaches the tool, and the tool sends clone content to an endpoint that no statement covers. Meanwhile the run page
   names the Anthropic statement and says "the tool authenticated through it" (:138, :174).
   Scenario :173 ("the session's effective provider is the declared one") and Falsifier :222 ("a
   provider-redirecting variable or option ... reaches the tool") both say this must not happen. The SHALL text,
   however, gives the build neither a duty nor a means to prevent it. Every other declared input fails closed when
   its check fails: the binary by path, executable bit and version (:142), managed settings by their keys (:140), and
   exclusions only once observed (:140). This one input does not, and brief item 1 asks the requirement to "refuse
   otherwise".
   Repair: admit the declared name only from a closed list, per tool and provider, of variables that the declared
   tool and version documents as authenticating only. Record that list as Observed for the version, as the
   exclusions are. Refuse the launched run, naming the variable, when the declared name is not on the list. Add a Case
   that declares a redirecting variable as the credential variable.

2. [note] The managed-settings read is a third credential-adjacent read, which the two-exception oracle forbids.
   Paragraph 2 (:140) requires reading the managed keys "that can ... authenticate a model provider, its environment
   block included". Paragraph 1 (:138) says "Syzygy SHALL read no provider credential except" the file copy and the
   declared pass-through. The Oracle (:220) inspects runtime output for "credential variable names" and excepts
   "exactly two uses".
   [Inferred] A conforming managed-settings reader has to hard-code those variable names in order to recognise them.
   It also parses a file whose environment block may hold a credential value. On that reading, scenario :202 and the
   Falsifier clause "a credential read other than the two excepted uses is present in runtime output" (:222) fire on
   every conforming build. This is the same mechanism as round-2 note 3, and it does not open egress, so it is a
   note. Repair: name the managed-key inspection as a third exception in :138, :202, :220 and :222. Make it by key
   name only, with values never recorded, logged or compared beyond what deciding a mismatch needs.

3. [note] The Falsifier omits one of the managed-settings refusal arms. :140 refuses in three cases: on a
   mismatching key, on an unreadable or unparsable location, and where "the managed layer's provider-relevant keys
   for the declared tool and version are not known". Falsifier :222 covers only "a run starts while managed settings
   redirect the provider or cannot be read", and the Case (:218) seeds no unknown-version arm. Add "or where the
   managed layer's provider-relevant keys for the declared version are not known" to both.
   [Unknown] Whether either tool delivers managed settings at a location that is not a file (for example a policy
   store or settings served remotely). The unknown-keys arm appears to cover that case only if the implementer reads
   "locations the declared tool and version documents" to include it.

4. [note] The arm choice is the owner's alone, P-111 Q2, unchanged since round 2. The direction record (:99-101) says
   content goes through a launched CLI "only where an act already in force covers that repository, that content
   class and that agent tool with its provider". The delta's drafted arm (:146) lets unlisted classes go with a
   disclosure. Direction :118-125 names the tension honestly. This is not a defect of the delta.

Counts: 1 revise, 3 notes; round-2 closure 5 closed, 1 carried to the owner (finding 6), 0 not closed.
