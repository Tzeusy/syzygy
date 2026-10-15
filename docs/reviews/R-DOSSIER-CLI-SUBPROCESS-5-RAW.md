# Review R-DOSSIER-CLI-SUBPROCESS-5
Reviewed commit: 3fd1837783ea52cbc4305dd0e0f128fbdb9d15fb
Subject SHA-256: 478c86d5bc474d806019c943de751968fe0765683f65640e843436dc1f0cd73d
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context reviewer, not the author. Round 5 is a confirming round over repaired bytes.
Brief: `.syzygy/governance/contracts/candidates/dossier-local-cli-subprocess-runner/REVIEW-BRIEF.md`, Round 1 section
(its stopping-rule sentence is excepted, per dispatch). Focus: the egress and trust boundary.

## What was checked

- [Observed] `git rev-parse HEAD` = 3fd1837783ea52cbc4305dd0e0f128fbdb9d15fb, as the dispatch expects.
- [Observed] `sha256sum` of the three files, all matching the dispatch:
  - subject `SEMANTIC-DELTA.md`: 478c86d5bc474d806019c943de751968fe0765683f65640e843436dc1f0cd73d;
  - `OWNER-DIRECTION-DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15.md`: da3a6726e1c668ef8a57a19e8093bf9f8fe9a792d446e83df83757d1577751c7;
  - `OWNER-DIRECTION-DOSSIER-CLI-RUNNER-REPAIR-AND-DISCLOSE-2026-10-15.md`: 9f5103b469d37923092e1771b7f4b294c14487046392fa5ad33811846c880d4f.
- [Observed] Read in full: the subject, both companions, the brief, the round-4 raw, `ROUND-4-DISPOSITIONS.md`,
  `ROUND-4-REPAIRS.md`, `POLARIS-DOSSIER-LOCAL-AGENT-MODE-DIRECTION.md` (item 2 of the 2026-10-05 rulings) and
  `DOSSIER-AGENT-PROVIDER-V2-REDIS-ANTHROPIC-ACT.md`.
- [Observed] Searched for the "path listing" wording behind REQ-polaris-generation-030. The signed
  `openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:11` uses the same construction:
  "the source classes of the tree at the pinned revision, as Syzygy's own path listing of that tree exposes them
  (REQ-polaris-generation-030)".
- [Observed] Read `WARRANT_FAMILIES` and `DOSSIER_DECISION` in `apps/three-surface-poc/src/polaris-authority-sweep.test.ts`
  (lines 28 and 31-41).
- [Observed] Ran `claude --help` on this host. The `--bare`, `--restricted`, `--safe-mode`, `--setting-sources`,
  `--strict-mcp-config` and `--disable-slash-commands` quotations in the flag table (:253-258) match the help text.
  I did not run `codex exec --help`, because no Codex row changed this round.
- Not done, per the dispatch: I read no target repository, state root or run directory, ran no `syzygy` command or
  npm/node script, and made no network call.

## Round-4 finding closure

| # | Class | Status | Reason |
|---|---|---|---|
| 1 | revise | closed | :138 "Every provider-selecting option of the tool (such as a configuration profile, a configuration override, or a local or third-party provider switch) SHALL be either absent or set by Syzygy to the declared provider." The modal verb is back. The flag-table citation at :262 ("REQ-045 first paragraph") again points at SHALL text. |
| 2 | note | closed | :138 "Syzygy SHALL read no provider credential except to copy the tool's own credential file ...; the read-only inspection of the administrator-managed settings' provider-relevant keys in the next paragraph is the one other permitted read, and its values reach no record, log, page or child process." This matches :140 ("never recorded, logged, stored, transmitted or passed to the tool"), the scenario at :202, the Oracle at :227 ("excepting exactly two uses") and the Falsifier at :229 ("a credential read other than the two excepted uses"). |
| 3 | note | closed (scenario lags; new note 1) | :140 "or authenticates the tool by any means other than its own credential file (such as an API key, a key helper or a token, even for the declared provider), Syzygy SHALL refuse the launched run, naming the key and file." The Case at :225 ("with an API key or key helper for the declared provider") and the Falsifier at :229 ("authenticate it by any means other than the tool's own credential file") carry the same rule. The scenario at :178 was not widened to match. |
| 4 | note | closed | :138 "Before any session starts, Syzygy SHALL check that the tool's own credential file is present ... and that the tool reports itself logged in from it alone ...; where the file is absent, the tool's login is held elsewhere (such as a system keychain), or the check cannot be made, Syzygy SHALL refuse the launched run, naming the failure, start no session, and report the run's readiness and every claim that depends on the model step as Unknown." There is a new scenario at :217-221, the Case at :225 seeds "an operator home whose credential file is absent, and one whose login is keychain-only", and the Falsifier at :229 covers both. The status-command step leaves two small gaps (new note 2). |
| 5 | note | answered by the owner; written faithfully | :146 "a launched run SHALL NOT be refused for it", with the basis "`POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05` item 2, and for launched runs the one-command run's packet Q2 and `DOSSIER-CLI-RUNNER-REPAIR-AND-DISCLOSE-2026-10-15` item 2". The page "SHALL give the list of content classes present in the clone at the pinned revision ... each marked as listed or not listed ... and it SHALL state that the tool could read the whole clone and may have sent its provider content of the classes the statement does not list". This matches direction item 2: "The run page states that the tool may send its provider content of classes the statement does not list, and gives the list of classes present." It also keeps that item's "Packets Syzygy itself writes still carry only the classes the statement lists" (:146 "Packets Syzygy itself writes ... SHALL carry only the content classes that statement lists"). |

## Task 2 — consistency and the egress boundary after the repairs

- [Observed] Paragraph 1 (:138), paragraph 2 (:140), the "No provider client" scenario (:199-203), the Oracle (:227)
  and the Falsifier (:229) now agree on exactly two permitted credential-adjacent reads. The Downstream impact section
  (:319-328) names every new duty: the managed-key read and its authentication refusal, the login check, "pass no
  credential variable", and the present-class list built from the path listing. The "Owner question" section
  (:347-356) states the answer and its scope correctly: "Syzygy's own packets carry only the classes the statement
  lists", "The refuse arm was not chosen", and "Only Q1 ... remains open". The warrant block (:237) and the Warrant
  section (:289-292) both add `DOSSIER-CLI-RUNNER-REPAIR-AND-DISCLOSE-2026-10-15`.
- [Observed] The disclosure scenario (:210-215) gives the same three duties as :146: name the statement and its
  classes; list the present classes, each marked, with any undeterminable one shown as Unknown; and give the
  may-have-sent statement with no refusal. The Case at :225 seeds "a clone holding content classes the statement does
  not list". The Falsifier at :229 covers "a run is refused for unlisted content classes in the clone, or the run
  page omits the present-class list or the may-have-sent statement".
- [Inferred] The present-class list can be derived without any read that no act covers. It is built from "Syzygy's
  own path listing of that tree" (:146). That is the same metadata-only construction the signed local-agent text
  already uses for its governed-subject test (signed spec :11). Such a listing is one of Syzygy's own reads at the
  pinned commit, under the observation consent, which item 3 of the 2026-10-05 rulings leaves binding. A class that a
  path cannot decide is shown as Unknown, not settled by reading a body, so the list adds no body read.
- [Inferred] The requirement still fails closed on every arm it states. An undeclared tool, path, version or provider
  refuses, and so do a missing statement, an unobserved exclusion, managed redirection or managed authentication, an
  unreadable managed layer, a failed login check and a missing binary. Each refusal leaves readiness and the
  dependent claims Unknown. The only arm that does not refuse is the one the owner chose: unlisted classes in the
  clone. Its basis is the operator's-own-act ruling, now recorded for launched runs. Every transmission Syzygy makes
  stays inside the statement in force (:146). The tool's own sends go to a declared tool and provider that has a
  statement in force. Their content classes go beyond that statement, and they rest on item 2 of the 2026-10-05
  rulings, on packet Q2 and on item 2 of the new direction, as :146 says.
- [Observed] The first companion's line "only where an act already in force covers that repository, that content
  class and that agent tool with its provider" (direction :99-101) reads more narrowly than the chosen arm. That same
  direction left the class question open at :118-125 ("Whether to disclose it or to refuse such runs is the owner's
  question, carried as P-111 Q2; this direction does not settle it"), and the second direction settles it. This is
  not a defect of the delta.

## New findings

1. [note] The managed-settings scenario does not test the repair for round-4 note 3. SEMANTIC-DELTA.md:178 reads:
   "carry an environment block or key that selects, redirects or authenticates a provider other than the declared
   one". Paragraph 2 (:140) also refuses a managed key that authenticates "even for the declared provider", and the
   Case (:225) and Falsifier (:229) both exercise that case. The SHALL text, the Case and the Falsifier all carry it,
   so a conforming build is still pinned down. Repair: add "or authenticates the tool by any means other than its own
   credential file, even for the declared provider" to :178.

2. [note] The login check at :138 says nothing about how the tool's status command is run, and it does not say what
   happens when the tool has no status command. [Inferred] The paragraph's environment rule ("Syzygy SHALL start the
   tool with a process environment it writes and records in full") plausibly covers the status invocation. But no
   text says the check runs inside the session's private configuration home, with only the copied credential file in
   view. If it ran against the operator's own home, or with an ambient credential variable, "logged in from it alone"
   could not be decided. The record clause at :144 covers launched sessions only, so this invocation's environment is
   not recorded. "by the tool's own status command where it has one" can also be read to mean that a presence check
   is enough when the tool has no status command, instead of counting that as "the check cannot be made". Both tools
   in the closed set do have a login-status subcommand [Inferred: `claude --help` lists `auth`; Codex was not re-read
   this round], so this opens no route today. Repair: say the check runs in the session's view and environment, is
   recorded, and refuses where the tool has no status command.

3. [note] The disclosure has no falsifier for a wrong list, and its scope is narrower than "the whole clone". The
   Falsifier at :229 fires only when the list or the statement is *omitted*. It does not fire when a present class is
   left out of the list, or when an unlisted class is marked "listed". The Oracle (:227) fixes the disclosure *wording*
   in advance, not the expected class set for the seeded clone. [Inferred] The list is also taken "at the pinned
   revision" (:146). A session that can read the clone's `.git` directory, other refs or untracked files can reach
   content outside that tree, and the list never shows it. The general statement "the tool could read the whole
   clone" still covers that content, and the disclosure is honest about its own scope, so this is a note. Repair: add
   "or the list omits or mislabels a present class" to the Falsifier, with the expected set from the seeded clone in
   the Oracle. Optionally, say that the list covers the pinned tree only.

4. [note] The fold-in check in Downstream impact names only one of the two new warrant IDs. It also calls its result
   Unknown, but the result can now be observed. :333-337 reads: "the warrant block's
   `DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15` must belong to an id family ... [Unknown whether the current families
   admit it]". [Observed] `polaris-authority-sweep.test.ts:28` defines `DOSSIER_DECISION =
   /^POLARIS-DOSSIER-(?:LOCAL-AGENT-[A-Z0-9]+(?:-[A-Z0-9]+)*|WAITING-SESSIONS)-\d{4}-\d{2}-\d{2}$/`. Neither that nor any
   other entry of `WARRANT_FAMILIES` (:31-41) matches `DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15`, the newly added
   `DOSSIER-CLI-RUNNER-REPAIR-AND-DISCLOSE-2026-10-15`, or `POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14`. As things
   stand, all three would fail that test at fold-in. This concerns tooling, not egress. Repair: name all the
   warrant-block decision IDs in that bullet and record the observed non-match.

5. [note] The summary under "Change class" (:36-46) was not updated for rounds 3 and 4. It does not list the new
   failures: starting while managed settings authenticate the tool, starting when the tool cannot authenticate from
   its own credential file, passing any credential variable, and refusing a run over unlisted classes or omitting the
   present-class list. It is a summary and not SHALL text, so no duty is lost.

No revise finding. [Inferred] None of the five notes reopens an egress route or a fail-open arm. Each one is a gap
in a scenario, a test or a summary, or a gap in how one SHALL arm is specified, and its intent is already carried by
the SHALL text.

Counts: 0 revise, 5 notes; round-4 closure 4 closed (item 3 with a lagging scenario, new note 1), 1 owner-answered and written faithfully (item 5).
