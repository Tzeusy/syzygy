# Review R-POLARIS-DOSSIER-ONE-COMMAND-RUN-1
Reviewed commit: 8afadc5544efc6c88c44e0d0fa6f261551a60b96
Subject SHA-256: c1a84c61c637cc767d5808c7d054b2be90c4da924d2a3af1af58cf4b51eb99c2
Verdict: REVISE

Reviewer: fresh-context reviewer, round 1 of the whole change. Not the author.

## What was checked

- [Observed] `git rev-parse HEAD` returned the expected 40-hex commit above.
- [Observed] `sha256sum` of the five change files matched every expected value:
  spec.md c1a84c61c637cc767d5808c7d054b2be90c4da924d2a3af1af58cf4b51eb99c2;
  proposal.md 886b1251d6fa36ae06b82d06bda0ff5d61f6d7a8b204356e6ba6b8c8e8c1114d;
  design.md efaf3ffa9078706a6d29f0dd8c69bc7877b2a2415ee45410c762183bf16d905f;
  OWNER-PACKET.md c3718554163598ddec42aa02b6e328082897eaf31542d47d243ec25050b74a7a;
  tasks.md c5ca57189c1df65df07e75e06a97ea38e5a884fd042de43e828bee086954acd0.
- Read in full: the five files of `openspec/changes/polaris-dossier-one-command-run/`.
- Governing references read: decisions `POLARIS-DOSSIER-ONE-COMMAND-RUN-DIRECTION.md`,
  `OWNER-DIRECTION-DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15.md`,
  `OWNER-DIRECTION-DOSSIER-CLI-RUNNER-REPAIR-AND-DISCLOSE-2026-10-15.md`,
  `POLARIS-DOSSIER-LOCAL-AGENT-MODE-DIRECTION.md`, targeted lines of
  `POLARIS-DOSSIER-WAITING-SESSIONS-DIRECTION.md` and
  `DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md`; the signed REQ-033 to 036
  text in `openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md`
  (lines 1-30 and 320-326 read in full, the rest by search); `doctrine/security.md`
  lines 40-119 (SEC-2, SEC-3); targeted lines of `doctrine/vision.md`; the
  source-acquisition sign-off row of `ACCEPTANCE-ACT-RECORD.md` (lines 1318-1337)
  and `contracts/candidates/dossier-local-agent-acts/OWNER-SITTING-PACKET.md`
  lines 48-72; `packages/polaris-dossier/src/polaris.ts` lines 280-450 and
  targeted search; `packages/polaris-dossier/src/inventory.ts` by search.
- REQ-045 fold: a Python `difflib` comparison of SEMANTIC-DELTA.md lines 136-241
  against spec.md lines 244-347. [Observed] The only differences are: round-5
  note 2 (login check inside the view, recorded, no login-status command
  refuses), note 1 (managed-settings WHEN clause), note 3 (pinned-tree-only
  wording, Falsifier "omits or mislabels", Oracle present-class set), and one
  added sentence reading REQ-042's configuration clause. The warrant YAML is
  unchanged. Notes 4 and 5 are carried in the test change and are not spec text.
- Test change: `git show 8afadc5544efc6c88c44e0d0fa6f261551a60b96 -- apps` and lines 20-179 of
  `apps/three-surface-poc/src/polaris-authority-sweep.test.ts`.
- Help quotations: `claude --help` and `codex exec --help` run locally.
  [Observed] `--restricted`, `--setting-sources`, `--strict-mcp-config` and
  `--bare` exist for Claude Code, and `--permission-mode` admits "acceptEdits",
  "auto", "bypassPermissions", "manual", "dontAsk", "plan"; `--ignore-user-config`
  ("auth still uses `CODEX_HOME`"), `--ignore-rules` and `--approve-for-me`
  exist for Codex. The design's flag names are accurate.
- Not checked: any target repository, dossier state root or run directory
  (forbidden); no project script or `syzygy` command was run; the test was
  not executed.

## Findings

1. [revise] The one-commit clone that REQ-040 has Syzygy make has no act in
   force, and the spec says REQ-033 to 036 already name it. Spec line 9: "carries
   the run through every step REQ-polaris-generation-033 to 036 name, in this
   order: preflight; the one-commit clone of a consented revision into a
   directory under the state root". [Observed] REQ-033 to 036 contain no
   Syzygy clone step. The source-acquisition entry in force for the local-agent
   mode was signed on the basis that "This one fetches nothing: it reads your
   clone's `.git` directory" and "In this mode you make the clone"
   (`dossier-local-agent-acts/OWNER-SITTING-PACKET.md` lines 66 and 52), and
   that packet says the earlier fetching version was "parked with the provider
   mode" (line 65). [Observed] The prototype makes the fetch itself
   (`polaris.ts` line 282: `'fetch', '-q', '--depth=1', url, chosen.commit`).
   The proposal (line 142) says "No new egress, consent or read." A network
   acquisition of a repository body by Syzygy is a read that REQ-033 routes only
   "through the registered observer". The change has to name the act that
   covers a Syzygy-made fetch, or make the clone the operator's act stated as
   such, or keep only the `--clone` path until an entry covers it. Either way
   the claim that REQ-033 to 036 name this step must go.

2. [revise] Launch records, view digests and REQ-045's launch-record fields are
   labelled Observed although they are records Syzygy stored, and the REQ-033
   rule against that is not displaced. Spec line 65: "the run record SHALL
   record the launch form `syzygy-launched` and, labelled Observed because
   Syzygy itself did each"; line 67 says the top-level-session fact "becomes
   Observed from the launch record"; line 114 has the view digest "labelled
   Observed". The signed REQ-033 (local-agent spec line 25) says "Syzygy SHALL
   NOT rest an Observed label on a record it stored" and lists, among the values
   that must be labelled Inferred when they are not re-derived, "the declared
   session identifiers and launch forms". Neither REQ-041, 042 nor 045 names that
   text as displaced, so for a launched run the signed text and the added text
   conflict whenever a page shows a launch record after the step that wrote it.
   Criterion 3: the displacement is incomplete.

3. [revise] REQ-041's displacement of REQ-035 leaves the sentence that refuses a
   `syzygy-launched` inventory. REQ-035 (local-agent spec line 324) goes on,
   right after the clause REQ-041 displaces: "each is labelled Inferred and
   attributed to whoever declared it. Syzygy SHALL refuse an inventory or verdict
   whose declared launch form is neither, and neither SHALL count until its
   launch form is declared." "Neither" means neither a new terminal nor the
   shell-escape prefix. Spec line 67 replaces only "its launch form, which is a
   new terminal or the shell-escape prefix, as the operator declares it". Read
   as written, the unchanged sentence refuses every launched inventory and
   verdict, and "labelled Inferred" contradicts line 65. Each of these needs an
   exact quoted displacement.

4. [revise] For launched runs the tool narrowing of REQ-035's waiting sessions
   lapses, and nothing replaces it. REQ-035 (line 326) ties it to a printed
   command: "The command Syzygy prints for a waiting session SHALL pre-approve
   ... only read tools over the session's own directory (and, for the inventory
   session, the clone) and that one Syzygy command for that directory, and never
   a write or a general shell" and "the printed command SHALL also limit a
   waiting session to its read tools". In a launched run Syzygy prints no
   command (spec line 67), and REQ-045 line 248 governs only settings,
   instructions, skills and MCP, not which of the tool's own tools a session
   has. So under the spec a launched helper may get a general shell and network
   tools, which bears on findings 5 and 6. [Observed] The prototype is stricter
   than the spec (`polaris.ts` line 396 passes `--tools` and
   `--disallowedTools` to helpers). [Inferred] Fail-open by omission.

5. [revise] REQ-044 controls what Syzygy tells a launched session but not what
   the session does, and SEC-3 binds the process. `doctrine/security.md` lines
   65-69: "**What this binds:** Syzygy itself, every process Syzygy launches or
   schedules, and every instruction a Syzygy feature gives an agent ... None of
   them runs observed code outside a profile". REQ-033 line 15: "Syzygy SHALL
   execute no observed code, SHALL launch or schedule no process that does".
   In a launched run Syzygy launches the agent process (REQ-041, 045). Spec line
   208 only puts the rule in every brief and refuses `allow-execution`, and line
   114 rules out calling the view an execution profile. Nothing stops a launched
   session's shell from running code in the clone, for example after a prompt
   injection from clone text, and REQ-044's Falsifier (line 231) never tests
   whether a launched process ran observed code. The change must do one of
   three things: constrain the launched process so it cannot run observed code
   (code-running tools removed or narrowed to the named Syzygy commands, and
   observed by a stand-in probe in the Falsifier); show why SEC-3's process
   clause is met; or name this as a doctrine question for the owner. The
   proposal's "Launched runs are reading-only" (line 140) is currently a claim
   about instructions, not processes.

6. [revise] Sending target content to destinations other than the provider
   rests on no act and is not refused. Spec line 112: "Network access SHALL be
   left to the agent tool; Syzygy SHALL disclose that it does not restrict where
   a session sends data." The rulings the spec cites cover only the provider.
   `POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05` item 2 says "The operator's
   agent session sending target content to its own provider is the operator's
   own act". Packet Q2 (OWNER-PACKET line 55) is headed "Whose act are the
   agents' provider transmissions in a launched run?". REQ-045 line 254 rests the
   unlisted-class sends on those rulings "to its provider". A session that
   Syzygy launched, possibly with a general shell (finding 4) and an automatic
   approval mode (finding 7), can send clone content to any host, and the spec
   only discloses it. Criterion 1 needs one of two things: the requirements name
   what covers those sends and disclose that as REQ-045 does for unlisted
   classes, or they keep launched sessions from making them. A disclosure alone
   is not an act.

7. [revise] REQ-045 bans only modes that bypass permission checks, which lets in
   the automatic-approval modes. Spec line 246: "Syzygy SHALL NOT start the tool
   in any mode that bypasses the tool's permission checks." [Observed] Claude
   Code offers `--permission-mode` "auto", "acceptEdits" and "dontAsk", and Codex
   offers `--approve-for-me` ("Route approval requests through automatic
   review"). Read literally, none of these bypasses a check. The signed REQ-033
   (line 15) already treats "an automatic-approval or permission-bypass
   setting" as one class. REQ-043 (line 163) requires that "no session SHALL gain
   any permission" while the operator is detached, but an automatic approver
   grants permissions with nobody attending. [Observed] The prototype starts
   every session with `'--permission-mode', 'auto'` (`polaris.ts` lines
   395-396). REQ-045 should forbid automatic-approval modes too, or name the
   permitted modes per tool and role, and its Falsifier should test them.

8. [revise] REQ-041, 042 and 045 disagree about each session's directory and
   writable paths (criterion 4). Spec line 248 (REQ-045): "the session's
   workspace directory (its working directory and its only writable path, as
   REQ-polaris-generation-042 states)". REQ-042 does not state that. Line 112
   gives the author "the clone read-only, the run's state directory read-only,
   and the run's `drafts/` path read-write", with no own directory, and for every
   session "all read-only except the agent tool's own state". REQ-041 (line 63)
   starts every session "in that session's own directory", and REQ-042's
   scenario (line 124) names "the authoring session's directory" separately from
   `drafts/`. REQ-045's added reading (line 248) places the configuration as "the
   tool's installation, read-only, and that private configuration home". It says
   neither whether that home is writable nor where "the agent tool's own state"
   now lives. The author's workspace, the author's writable set and the tool's
   writable state have to be the same in all three requirements. [Observed] The
   prototype uses the run directory, read-only apart from `drafts/`, as the
   author's working directory (`polaris.ts` line 311), so "its only writable
   path" is false for the author there.

9. [revise] REQ-040's closing sentence is contradicted by the change's own other
   requirements. Spec line 13: "Every check, freeze, packet, validation,
   refusal, label and disclosure SHALL be that of REQ-polaris-generation-033 to
   036; the one command adds no step that decides readiness and removes none."
   REQ-041 adds a counting rule ("An inventory or verdict from a launched run
   SHALL count only when its session's launch record exists", line 65) and a
   refusal of `terminal` and `bang`. REQ-042 adds the host-view refusal. REQ-044
   refuses `allow-execution`. REQ-045 adds a dozen refusals before `init` or
   before any session, and new disclosures. All of these are refusals and
   disclosures that REQ-033 to 036 do not have, and several decide readiness.
   The sentence should be limited to what REQ-040 itself adds, or say "and those
   of REQ-041 to 045".

10. [revise] Several prose statements disagree with the spec or with the tree
    (criterion 6).
    - proposal.md lines 88-89: "starts each session ... as a sibling process of
      its own supervisor". The spec says "a child of the run's supervisor
      process" (line 63).
    - proposal.md lines 96-99: "the clone read-only, its own directory writable
      ... and every other session's directory and the run's state directory
      absent". The spec gives the author the state directory read-only and
      `drafts/` writable (line 112).
    - proposal.md lines 44-45, under "[Observed unless marked]":
      "`packages/polaris-dossier/src/inventory.ts` hard-codes `LAUNCH_FORMS =
      ['terminal', 'bang']`". [Observed] At the reviewed commit, inventory.ts line
      379 reads `LAUNCH_FORMS = Object.freeze(['terminal', 'bang',
      'syzygy-launched'] as const)`.
    - design.md lines 56-58: "the agent tool's own config and state directory
      read-write (it needs its login and transcripts)". REQ-045 (line 248) says
      "never the operator's own configuration directory".
    - proposal.md lines 137-139: "whether that launch keeps the agents'
      transmissions the operator's own act is packet Q2". This reads as open,
      but Q2 was answered on 2026-10-14 (OWNER-PACKET line 55).

11. [revise] The prototype status section of design.md (lines 160-195) leaves
    out departures that bear on the egress and trust boundary. [Observed] from
    `polaris.ts`:
    - every session is started with `--permission-mode auto` (lines 395-396);
    - when `SYZYGY_POLARIS_AGENT` is unset the executable comes from `PATH` by
      `command -v claude` (line 334). The design discloses only the environment
      variable, and its REQ-045 section says Syzygy "never resolves a binary from
      `PATH`";
    - the role prompt goes as a positional argument, not as an instructions file
      named on the command line (lines 395-396);
    - Syzygy types messages into the authoring pane with `tmux send-keys`
      (lines 445-447). That is an instruction route REQ-045's "in no other way"
      (line 248) does not list;
    - Syzygy fetches the clone itself (line 282; see finding 1);
    - `agentProvider: 'anthropic'` and `operatorIsOwner: true` are hard-coded
      into the run configuration (lines 290-292), not declared by the operator.
    Criterion 6 asks for prototype departures to be disclosed.

12. [note] REQ-045 does not say how long the copied credential files live.
    Line 246 lets Syzygy "copy the tool's own credential file, unparsed, to where
    the tool expects it inside the session's view". Nothing says when the copies
    are removed, at close, stop, deadline or refusal. [Observed] The prototype
    leaves one copy per role under `<state root>/<run>.agents/<role>/.claude/`
    (`polaris.ts` lines 340-344). [Inferred] With refresh-token rotation, a
    copy's refresh may also invalidate the operator's original. Worth one
    sentence on lifetime and removal.

13. [note] REQ-043's "permission" is not defined, which weakens its oracle.
    Line 163: "no session SHALL gain any permission". The Oracle independence
    (line 192) takes "permissions" from "the operating system", but the
    permissions that matter here are the agent tool's approvals, which the
    operating system does not show. Name what counts as a permission and where
    the independent observation comes from (for example, the stand-in's own
    record of the approvals it received).

14. [note] REQ-041 line 63, "Each helper session ... SHALL obtain its input only
    through the waiting command", sits awkwardly with REQ-043 line 161: panes
    are "interactive exactly as the agent tool presents it", so the operator can
    type into a helper. State that operator input in a helper pane is outside
    "input", or disclose it on the review page.

15. [note] REQ-040's stop list (line 11) does not say what happens to the run
    when a session reaches its REQ-045 time bound (line 250: "leave the
    session's result absent"). [Inferred] It is probably covered as "a refusal
    by any step" at the next check. Saying so would make REQ-040's Falsifier
    decidable for that case.

16. [note] Packet Q2 (OWNER-PACKET lines 57-59) says the 2026-10-08 packet
    warned that the disclosure "turns false and RFC7-20 and the public egress
    record would apply". [Observed] `DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md`
    line 132 says only that "the 'no provider call' disclosure turns false". A
    search of that file for "RFC7-20" and "egress record" returned no lines. The
    second half is the drafter's addition and should not be attributed to that
    packet. The answer itself is not reopened.

17. [note] tasks.md lines 10-14 read as left-over drafting: "Nothing to strike;
    strike or narrow requirements per the answers (Q2 changes REQ-041's
    disclosure; Q4 no changes REQ-042's refusal; Q5 no adds a pause rule to
    REQ-043; Q6 renames the command throughout)." The checked box says nothing
    was struck, while the parenthesis lists conditional edits for answers the
    owner did not give.

18. [note] REQ-042 line 112: "Syzygy SHALL NOT run such a command in a form that
    copies content from outside the view into a path the session can read". On
    a literal reading this could catch REQ-035's own delivery, which writes the
    packet into the helper's directory before `dossier await` lets the helper
    read it. One clause saying that Syzygy's deliveries under REQ-035 are not
    such a copy would remove the doubt.

19. [note] REQ-042 has no rule for the case where a forbidden path lies inside
    a path every view mounts read-only, such as a state root inside the Syzygy
    checkout or inside the tool's installation directory. The reachability
    matrix in the Falsifier catches it only for the fixture layout. [Observed]
    The prototype refuses tool directories that contain the state root or home
    (`polaris.ts` lines 363-369), but not a state root under the checkout. A
    host-check clause would close this.

20. [note] REQ-045 (line 248) re-reads a clause of REQ-042, another requirement
    of this same unsigned change ("For a launched run, REQ-polaris-generation-042's
    ... reads as"). Since both are candidates in one change, writing the reading
    into REQ-042's own text would remove one level of indirection and would have
    exposed finding 8. This is an editorial choice for the drafter.

21. [note] Two [Observed] claims in the prose rest on material outside this
    repository and were not verified, because the brief forbids reading it: the
    Redis run's `run.json` figures (proposal lines 13-17) and "bubblewrap 0.11.1
    builds an unprivileged view" (OWNER-PACKET lines 76-77). [Unknown] to this
    review.

Test change (criterion 7), no finding: [Observed] `DOSSIER_DECISION` gains the
exact alternative `ONE-COMMAND-RUN`. The new `DOSSIER_RUNNER_DECISION` admits
`LOCAL-CLI-SUBPROCESS` exactly and `CLI-RUNNER-` followed by an uppercase
suffix. Every value matching it must sit under `decisions` and have a declared
`Decision ID:` (test lines 138-141), so the open suffix is bounded by the
declaration check. Positive and negative syntax cases were added for both. No
existing family, assertion or population check was removed or loosened. Both
runner ids and `POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14` have `Decision ID:`
lines (direction files, line 7 each). The test was not executed in this review.

Displacement quotations checked, no finding beyond 2 and 3: [Observed] all
four quoted REQ-035 strings in spec line 67 occur verbatim at local-agent spec
lines 320, 326 and 324, and the REQ-033 string in spec line 116 occurs verbatim
at line 25. No signed byte is edited: the commit touches only the change
directory and the test file.

Counts: 11 revise, 10 notes (21 findings).
