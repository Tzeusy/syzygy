> **Candidate — binds nothing.** Drafted 2026-10-15 under the owner direction
> `DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15` and CC-REV-2. It performs no act,
> amends no signed byte and edits no byte of any other candidate. It takes
> effect only if the owner signs it off, after a fresh independent review of
> these exact bytes (VIS-4).

# Semantic delta DOSSIER-CLI-RUNNER-1 — the local agent CLI subprocess runner

The owner directed on 2026-10-15 that where Syzygy drives a dossier's model
step it runs "*our local codex or claude cli binary* like a subprocess with
explicit workspace/instructions/artifacts path and skill/mcp guidance, no
custom SDK or API tooling". This delta writes that down as one added
requirement, REQ-polaris-generation-045, for runs launched under the
candidate change `openspec/changes/polaris-dossier-one-command-run/`.

**Artifact(s):** one requirement proposed for addition to
`openspec/changes/polaris-dossier-one-command-run/proposed/polaris-generation/spec.md`,
after REQ-polaris-generation-044. That change is itself an unsigned
candidate. This package does **not** edit it: an OpenSpec change is one
coherent category overlapping no other change, and the runner is part of the
launched-session category that change already owns. The text below is folded
into that change at its next revision, by whoever holds it (`syzygy-zwja`),
and is reviewed again with it there. Until then it is a proposal over that
change, not a second change.

**Stable IDs affected:** REQ-polaris-generation-045 is proposed (free at
`origin/main` `2d6a3632`: no occurrence in `openspec/`, `.syzygy/`,
`packages/` or `docs/`, by a fixed-string sweep this session; the round-1
reviewer's sweep at `113fe505` found it only in this package and the P-111
row). It refines
REQ-polaris-generation-041 ("with the agent tool, version and model the
operator declared for the run") and REQ-polaris-generation-042 ("the agent
tool's own installation and configuration as the tool requires") without
editing either. No identifier is retired, renamed or renumbered.

**Change class:** **Normative.** Under the candidate REQ-041 the agent tool
is whatever the operator declared and is started however the supervisor
chooses; nothing says what reaches the tool from outside the run, which
agent tools may be launched, what happens when the binary is missing, or
that no provider client may be built. Under this delta a build that launches
an undeclared binary or provider, lets the operator's settings or
environment or the clone's own settings and instruction files widen or
redirect a launched session, uses a bypass-permissions mode, passes
instructions or guidance implicitly, links a provider SDK or API client into
the model step, runs a session with no time bound, reports a run as ready
when its binary is absent, or omits the unlimited-reading disclosure fails.

**Author:** agent drafting for the owner direction (lane
`dossier-local-cli-subprocess`).

**Date:** 2026-10-15, drafted over `origin/main` `2d6a3632`.

## Sources

- The owner direction
  `.syzygy/governance/decisions/OWNER-DIRECTION-DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15.md`.
- The owner direction
  `.syzygy/governance/decisions/POLARIS-DOSSIER-ONE-COMMAND-RUN-DIRECTION.md`
  (`POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14`), whose packet answers Q2
  (the launched agents' transmissions stay the operator's own act) and Q7
  ("Claude Code first … Codex once its statement is in force") this delta
  keeps.
- The signed v1.2 sign-off record
  `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-v1.2.md`,
  which names as a remaining limit "allow rules in your own ~/.claude or
  project settings still apply inside these sessions; a flag that could
  switch them off exists, and I'll evaluate it as a follow-up" — the
  follow-up is bead `syzygy-zzt5` item (a).

## Authority chain today

[Observed, from the files named, at `2d6a3632`]

1. The adopted generator specification
   (`openspec/changes/polaris-manifesto-generation/`) is written for
   Syzygy-made provider calls (stage budgets, provider receipts, a
   registered route).
2. The signed `polaris-dossier-local-agent-mode` (v1.0, v1.1, v1.2) adds the
   operator-agent mode, REQ-polaris-generation-033 to 036: the operator's own
   agent session does the model work, "Syzygy makes no model-provider call",
   and every inventory and review session is one "the operator starts"
   (REQ-035), in launch form `terminal` or `bang`.
3. The candidate `polaris-dossier-one-command-run` (REQ-040 to 044, unsigned)
   adds launched runs, in which Syzygy starts each session itself.
   Implementation of its slices 1 to 5 is authorized as a prototype by item 5
   of `POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14`; the prototype is
   `packages/polaris-dossier/src/polaris.ts`, which starts the `claude`
   binary under `bwrap` in a `tmux` window with a private per-role home.
4. The provider-route packages (route A, route B) are parked by item 4 of
   `POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05` and, since 2026-10-15, not
   pursued.

**Finding.** No signed requirement permits Syzygy to start an agent CLI: the
signed text says the operator starts every session. A Claude Code subprocess
runner is inside an implementation authorization only as the one-command-run
**prototype** (item 5 above), and it is specified only by unsigned candidate
text. Codex is inside neither: the prototype resolves only `claude`
(`claudeExecutable()`), and packet Q7 defers Codex until a Codex provider
statement is in force. None of the candidate text says how instructions,
skills or MCP guidance reach the tool, how the operator's own settings are
kept out, or that no SDK or API client may be used. So a delta is needed,
and it binds only with the one-command-run change's sign-off.

The Redis agent-provider statement in force scopes itself to "operator-agent
runs over this one repository with this one tool and provider"
(`DOSSIER-AGENT-PROVIDER-V2-REDIS-ANTHROPIC-ACT.md`). That it also covers a
session Syzygy launches rests on the one-command run's packet Q2 answer,
which reads a launch of the operator's own tool as keeping the transmissions
the operator's act [Inferred: a direction's adopted recommendation, not a
reading of the statement act itself].

## Current meaning

At the candidate REQ-polaris-generation-041 and 042, a launched session runs
"with the agent tool, version and model the operator declared for the run",
inside a view that admits "the agent tool's own installation and
configuration as the tool requires". Nothing is said of:

- which binaries may be declared, or how Syzygy finds them;
- which of the tool's settings layers load (Claude Code reads user, project
  and local settings by default; Codex reads `$CODEX_HOME/config.toml` and
  execpolicy rules);
- how the role's instructions, the workspace, the artifact path, skills and
  MCP servers are given to the tool;
- a time bound per session beyond the run deadline;
- what happens when the declared binary is missing or is not the version
  declared;
- whether the model step may instead be served by a provider client Syzygy
  links itself.

## Proposed meaning

The requirement text to fold in, in the spec's own form:

~~~~markdown
### Requirement: Local agent CLI subprocess runner

In a launched run Syzygy SHALL perform every model step only by starting the operator's locally installed agent command-line tool as a child process of the run's supervisor, and by no other means. The tool SHALL be one of a closed set, `claude` (Claude Code) and `codex` (Codex CLI). The operator SHALL declare for the run the tool by name, absolute executable path and version, and the model provider the tool is to use; Syzygy SHALL NOT search for, substitute or fall back to another tool, path, version or provider, and SHALL take the executable from that declaration alone, never from an environment variable or other ambient setting; a test stand-in is declared by absolute path like any tool. Syzygy SHALL start the tool with a process environment it writes and records in full (the declared credential variable below by name only), from an allow-list that admits no variable selecting, redirecting or authenticating a model provider, with one exception: where the declared provider authenticates the tool through a variable, the operator SHALL name that one variable in the run declaration, and Syzygy SHALL pass it from its own environment to the tool unparsed, never logging, storing or transmitting its value, SHALL record its name (never its value) in the launch record, and the run page SHALL disclose that the tool authenticated through it. The allow-list SHALL admit nothing else that selects, redirects or authenticates a provider, and every provider-selecting option of the tool (such as a configuration profile, a configuration override, or a local or third-party provider switch) either absent or set by Syzygy to the declared provider. Syzygy SHALL NOT start the tool in any mode that bypasses the tool's permission checks. Syzygy SHALL NOT contain, load or call a model-provider SDK or API client, open a connection to a model provider, or resolve a provider route for this step. Syzygy SHALL read no provider credential except to copy the tool's own credential file, unparsed, to where the tool expects it inside the session's view, and to pass the one declared variable above, unparsed; it SHALL record that it did each; authentication is the tool's own, under the operator's account.

Syzygy SHALL give the tool, explicitly on its command line or in files it names there, and in no other way: the session's workspace directory (its working directory and its only writable path, as REQ-polaris-generation-042 states); the role's instructions file, written by Syzygy and recorded by digest; the artifacts output path the session's result is handed in through; and the skill and MCP guidance for the role, each skill as a named file or directory and each MCP server as an explicit configuration, or the explicit statement that the role has none. Every other settings, instruction and MCP source SHALL be excluded: the tool's user, project and local settings layers; user-level and project-level instruction files (such as `CLAUDE.md` and `AGENTS.md`); the settings, instruction and MCP files of every directory the session can read, the clone included; skills, custom agents, custom commands and output styles, whether in the operator's home or in any directory the session can read, the clone included, other than the skills Syzygy names; plugins; hooks; and ambient MCP configuration. Syzygy SHALL exclude each by the tool's own flags where they exist, and otherwise by a private configuration home inside the session's view holding only what Syzygy wrote there. A source counts as excluded only once its exclusion has been observed for the declared tool and version, in a stand-in or attended run whose record is retained as evidence; until then it counts as not excluded. Where any source other than the tool's administrator-managed settings is not excluded, Syzygy SHALL refuse the launched run before any session starts, naming the source. Administrator-managed settings, which neither tool offers a flag to exclude, SHALL be recorded as not excluded, labelled Observed as Syzygy's own finding about the tool, and disclosed on the run page. Before any session starts, Syzygy SHALL read, from the tool's administrator-managed settings at the locations the declared tool and version documents, only the keys that can select, redirect or authenticate a model provider, its environment block included; this is tool configuration on the operator's host, not target content. Where any such key names or could select a provider, endpoint or credential route other than the declared provider, Syzygy SHALL refuse the launched run, naming the key and file. Where a managed-settings location exists but cannot be read or parsed, or the managed layer's provider-relevant keys for the declared tool and version are not known, Syzygy SHALL refuse the launched run and report the session's effective provider and every claim that depends on the model step as Unknown. The launch record SHALL hold, labelled Observed, each managed-settings location checked, whether it was present, and the provider-relevant keys found by name.

Before `init`, Syzygy SHALL check that the declared executable exists at its path, is executable, and reports the declared version; where any check fails it SHALL refuse the launched run, naming the failure, start no session, and report the run's readiness and every claim that depends on the model step as Unknown, never as ready, passed or empty. Each session SHALL carry a time bound, declared for the run and no later than the run deadline; Syzygy SHALL stop a session that exceeds it, record the stop, and leave the session's result absent and its dependent claims Unknown. A session that exits non-zero, writes no result at its artifacts path, or writes one that fails validation SHALL count as no result.

For each launched session the launch record of REQ-polaris-generation-041 SHALL also hold, labelled Observed: the tool's name, executable path and reported version; the declared provider; the process environment the tool was started with, by variable name, and by digest over its names and every value other than the declared credential variable's; the digest of the instructions file; the artifacts output path; the exact skill and MCP guidance given, by path and digest, or that none was given; each settings layer and whether it was excluded, and by what means; and the session's time bound and whether it was reached.

This requirement grants no consent. A run whose declared tool and provider have no agent-provider statement in force for the target SHALL be refused before any session starts, naming the missing statement. Packets Syzygy itself writes for a launched session SHALL carry only the content classes that statement lists. A launched session can read the whole clone, so the tool can transmit to its provider content of any class in the clone, listed or not; that rests on the owner's rulings that the agent session's own reading and sending are the operator's own act (`POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05` item 2, and for launched runs the one-command run's packet Q2), not on the statement. The run page SHALL disclose this: it SHALL name the statement and the classes it lists, and state that the tool's reading of the clone was not limited to them.

ID: REQ-polaris-generation-045
Source: VIS-2; governing warrants below.
Scope: v1-mandatory

#### Scenario: Declared tool started with explicit inputs only

- **WHEN** a launched run starts a session with the declared tool
- **THEN** the process tree shows that tool, at the declared path, as a child of the supervisor, with a command line naming the workspace, the instructions file, the artifacts path and the role's skill and MCP guidance
- **AND** the launch record holds each of those by path and digest, and the settings layers with how each was excluded

#### Scenario: Operator settings do not widen a session

- **WHEN** the operator's user, project and local settings for the tool carry an allow rule, a hook, a plugin and an MCP server that the role is not given
- **THEN** none of them is in effect in the launched session: the allow rule grants nothing, the hook does not fire, and the plugin and MCP server are absent
- **AND** where an exclusion has not been observed for the declared tool and version, the launched run is refused before any session starts, naming the source

#### Scenario: Clone carries tool settings and instructions

- **WHEN** the clone, or the operator's home, holds tool settings, an MCP configuration, instruction files, skills, custom agents, custom commands and output styles (such as `.claude/settings.json`, `.mcp.json`, `CLAUDE.md`, `AGENTS.md`, `.claude/skills/`, `.claude/agents/`, `.claude/commands/`, `.claude/output-styles/`, `.codex/`) granting an allow rule, starting an MCP server and telling the agent to write outside its directory
- **THEN** none of them is in effect in any launched session that can read the clone
- **AND** where their exclusion has not been observed for the declared tool and version, the launched run is refused before any session starts

#### Scenario: Provider redirected by the environment

- **WHEN** the operator's environment carries a variable or tool option that selects, redirects or authenticates a model provider other than the declared one
- **THEN** the launched session's environment and command line carry none of it, and the session's effective provider is the declared one
- **AND** the launch record lists the environment Syzygy wrote by variable name; where the operator declared the provider's credential variable, it is the only authenticating variable passed, recorded by name only, and the run page says the tool authenticated through it

#### Scenario: Managed settings redirect or cannot be read

- **WHEN** the tool's administrator-managed settings carry an environment block or key that selects, redirects or authenticates a provider other than the declared one, or a managed-settings location exists but cannot be read or parsed
- **THEN** Syzygy refuses the launched run before any session starts, naming the key and file, or the unreadable location
- **AND** the session's effective provider and every claim depending on the model step read Unknown, and the launch record lists each location checked

#### Scenario: Stand-in taken from the environment

- **WHEN** an environment variable such as `SYZYGY_POLARIS_AGENT` names an executable other than the declared one
- **THEN** Syzygy starts the declared executable or refuses the run, and never starts the one the variable names

#### Scenario: Binary absent

- **WHEN** the declared executable is missing, not executable, or reports a different version
- **THEN** Syzygy refuses the launched run before `init`, naming the failure, and starts no session
- **AND** the run's readiness and every claim depending on the model step read Unknown, and no page or status reads ready or green

#### Scenario: Session exceeds its time bound

- **WHEN** a launched session is still running at its time bound
- **THEN** Syzygy stops it and records the stop
- **AND** the session's result is absent and its dependent claims are Unknown

#### Scenario: No provider client

- **WHEN** the built, non-test runtime output of the Syzygy packages and the lockfile are inspected, and a launched run is made with stand-in tools under a network observation
- **THEN** no model-provider SDK or API client, no provider endpoint host and no read of a provider credential variable or credential file (other than the recorded copy of the tool's own credential file and the unparsed pass-through of the one declared credential variable) is present in or reachable from the launched-run code
- **AND** no process that is not the declared tool or a process it started opens a connection to a model-provider endpoint during the run

#### Scenario: Tool without a provider statement

- **WHEN** the operator declares `codex` for a target that has an agent-provider statement in force only for Claude Code with Anthropic
- **THEN** Syzygy refuses the launched run before any session starts, naming the missing statement

#### Scenario: Run page discloses unlimited reading

- **WHEN** a launched run renders its pages
- **THEN** the run page names the agent-provider statement and the content classes it lists
- **AND** states that the tool could read the whole clone and its reading was not limited to those classes

Form: event-response.

- **Case:** Launched runs with stand-in `claude` and `codex` executables that record their own argv, environment, parent process and the files they can read; an operator home seeded with a permissive allow rule, a hook that writes a marker file, a plugin and an MCP server; a clone and an operator home seeded with tool settings, an MCP configuration, instruction files, skills, custom agents, custom commands and output styles; an operator environment seeded with a provider-redirecting variable, a provider-selecting tool option, an undeclared credential variable and a `SYZYGY_POLARIS_AGENT` naming another executable; a declared credential variable; administrator-managed settings seeded, in an attended run, with a provider-redirecting environment block, and made unreadable; a declared bypass-permissions mode; runs with the binary removed, made non-executable and reporting a wrong version; a stand-in that never exits; a declared tool with no provider statement for the target; an inspection of the built non-test runtime output and the lockfile; a run in a network namespace whose connection attempts are recorded per process, with the provider endpoints resolved to a local recorder.
- **Observable:** Each stand-in's recorded argv, environment and readable files, the hook's and the clone's marker files, the process tree, the per-process connection record, the launch records, the refusals and their wording, each page's readiness and disclosure wording, the stop records, and the inspection's output.
- **Oracle:** The expected argv, environment allow-list, guidance and settings-exclusion list per role and tool, and the refusal, disclosure and Unknown wording, written before the run; for the inspection, the known provider SDK package names, provider endpoint hosts, credential variable names and credential file paths, scoped to built non-test runtime output and the lockfile so that test fixtures holding those strings as sentinels are out of scope, and excepting exactly two uses: the copy of the tool's own credential file and the pass-through of the one declared credential variable.
- **Oracle independence:** Argv, environment, readable files, markers and connections come from the stand-ins, the file system and the network namespace, not from Syzygy's launch record; the inspection reads the lockfile and built output, not Syzygy's own claims.
- **Falsifier:** A session starts with an undeclared tool, path, version or provider, with an executable taken from the environment, or in a bypass-permissions mode; an operator or clone allow rule, hook, plugin, MCP server, instruction file, skill, custom agent, custom command or output style takes effect; a provider-redirecting variable or option, or any authenticating variable other than the one declared, reaches the tool; the declared credential variable's value appears in any record, log or page; a run starts while managed settings redirect the provider or cannot be read; a credential read other than the two excepted uses is present in runtime output; instructions or guidance reach the tool by any route not on its command line or in a file it names; a run starts with an unobserved exclusion; a missing or mismatched binary leaves any readiness or claim other than Unknown, or a session starts; a session runs past its bound; a provider SDK, API client or endpoint host is present in runtime output; a process other than the declared tool or its descendants opens a connection to a model-provider endpoint; a run without a provider statement for its tool starts a session; or the run page omits the unlimited-reading disclosure.

```yaml
warrants:
  primary: VIS-2
  doctrine: [VIS-2, VIS-4, SEC-2, SEC-3]
  contracts: [RFC7-20]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: [DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15, POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14, POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05]
  topology: []
  parent_requirements: [REQ-polaris-generation-041, REQ-polaris-generation-042]
```
~~~~

## Settings isolation: the flags evaluated

[Observed: `claude --help` at Claude Code 2.1.300 and `codex exec --help` at
codex-cli 0.162.1 on this host, 2026-10-15. Behaviour beyond the help text is
Unknown until the stand-in and attended runs observe it — the cross-link to
`syzygy-zzt5` item (a), which asks for the same observation for operator-started
waiting sessions.]

| Tool | Flag | What its help says | Fit for the runner |
|---|---|---|---|
| Claude Code | `--setting-sources <sources>` | "Comma-separated list of setting sources to load (user, project, local)." | The direct means to exclude all three layers. [Unknown] whether an empty list is accepted; to be observed. |
| Claude Code | `--restricted` | Removes the code-running tools and WebFetch "unless --tools names them", "ignores user, project and local settings files (managed settings and --settings still apply; add --strict-mcp-config to skip MCP servers too)", confines file tools to the working directories and refuses bypassPermissions. | Strongest fit: one flag covers the settings layers and file confinement; `--tools` must then name `Bash` for the role's one Syzygy command. Managed settings still apply and must be disclosed. |
| Claude Code | `--strict-mcp-config` with `--mcp-config` | Only the MCP servers given are used. | Required for explicit MCP guidance; already passed by the prototype for helper sessions. |
| Claude Code | `--bare` | Skips hooks, plugin sync, auto-memory and CLAUDE.md discovery, but "Anthropic auth is strictly ANTHROPIC_API_KEY or apiKeyHelper via --settings (OAuth and keychain are never read)". | **Not fit:** it forces key-only authentication and drops the operator's subscription login. The declared-credential-variable exception of paragraph 1 lets the operator choose a variable the tool itself reads; it never makes one mandatory, and Syzygy still calls no API (round-2 note 2). |
| Claude Code | `--safe-mode` | Disables CLAUDE.md, skills, plugins, hooks, MCP servers, custom agents; "Auth, model selection, built-in tools and plugins, and permissions work normally." | Partial: does not by itself exclude settings-file allow rules [Inferred from "permissions work normally"]; would also disable the explicit skills the role needs. |
| Claude Code | `--disable-slash-commands` | "Disable all skills". | Use only for roles with no skill guidance. |
| Codex | `--ignore-user-config` | "Do not load `$CODEX_HOME/config.toml`; auth still uses `CODEX_HOME`". | Direct fit for the user layer, keeping the operator's login. |
| Codex | `--ignore-rules` | "Do not load user or project execpolicy `.rules` files". | Direct fit for the rules layers. |
| Codex | `-s read-only`, `-C <dir>`, `--add-dir`, `--ephemeral`, `-o <file>`, `--output-schema <file>` | Sandbox policy, working root, extra writable dirs, no session files, last-message file, response schema. | Workspace (`-C`), artifacts path (`-o`), schema, and no persisted transcript. `--add-dir` makes a directory *writable*, so the clone must not be passed that way. |
| Codex | `-p, --profile`, `-c, --config <key=value>`, `--oss`, `--local-provider` | A profile layered on the user config, a config override, an open-source provider, a local provider. | Provider-selecting: absent, or set by Syzygy to the declared provider (REQ-045 first paragraph). |
| Codex | `--dangerously-bypass-hook-trust`, `--dangerously-bypass-approvals-and-sandbox` | Run hooks without persisted trust; skip all approvals and sandboxing. | Forbidden: bypass modes. Whether `--ignore-user-config` also suppresses hooks and a user-level `AGENTS.md` under `CODEX_HOME` is [Unknown]; until observed, those sources count as not excluded and a Codex run is refused. |
| Claude Code | `--dangerously-skip-permissions`, `--permission-mode bypassPermissions` | Bypass all permission checks. | Forbidden: bypass modes; `--restricted` itself "refuses bypassPermissions". |

The prototype today does not pass `--setting-sources` or `--restricted`; it
relies on a private home (`prepareAgentHome`) holding only a copied
credential file and a seeded onboarding record, which keeps the operator's
user settings out of the view [Inferred: from the code; not observed in a
run]. Project and local settings of the session's own directory are Syzygy's
to write, and are empty. Whether Claude Code reads project settings from an
`--add-dir` directory such as the clone is Unknown; REQ-045 counts those
files as not excluded, and so refuses the run, until their exclusion is
observed.

## What explicitly does NOT change

- REQ-polaris-generation-033 to 036 and every signed byte of
  `polaris-dossier-local-agent-mode`; the operator-started flow.
- REQ-polaris-generation-040 to 044 as drafted; this delta adds to them and
  edits none.
- The consent, screening, agent-provider statement and content-class gates.
  The runner adds a refusal; it relaxes none.
- SEC-3: no launched session executes observed code.
- The provider-route packages stay parked and not pursued.

## Warrant

The owner direction `DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15`, items 2 and 4,
under VIS-2 (an absent binary or an unexcluded layer is shown as such, never
as green) and SEC-2 (no consent is widened).

## Evidence or decision basis

- The owner's words, quoted in the direction record.
- [Observed] `packages/polaris-dossier/src/polaris.ts` at `2d6a3632`:
  `claudeExecutable()` resolves only `claude`, or the stand-in named by
  `SYZYGY_POLARIS_AGENT`; `launchSession` passes `--permission-mode`,
  `--tools`, `--allowedTools`, `--disallowedTools` and `--strict-mcp-config`
  and no settings-source flag; for the authoring session it can instead pass
  `--dangerously-skip-permissions` (`state.authorSkipPermissions`), which
  REQ-045 forbids in a launched run; and it passes the clone to the author
  and inventory roles with `--add-dir`, which is why the clone's own settings
  and instruction files are named among the excluded sources.
- [Observed] no `@anthropic-ai` dependency in the root, `polaris-dossier`,
  `polaris-generation-core` or `three-surface-poc` `package.json` at
  `2d6a3632`; the Agent SDK and Messages API adapters exist only on the
  unmerged PRs #258 and #264.
- The CLI help text quoted above.

## Terms introduced / retired

- **Local agent CLI subprocess runner:** the part of a launched run that
  starts the declared tool. No term is retired.

## Downstream impact

- `packages/polaris-dossier/src/polaris.ts`: add `codex`, the declared path
  and version check, the settings-exclusion flags, explicit guidance and the
  per-session bound; take any stand-in executable from the run declaration by
  absolute path and stop resolving `SYZYGY_POLARIS_AGENT` from the
  environment; read the provider-relevant keys of the tool's
  administrator-managed settings before any session starts; pass only the
  one declared credential variable; implementation waits for the sign-off.
- Bead `syzygy-bc0g` (re-scoped to this route), `syzygy-zzt5` item (a), and
  `syzygy-zwja` (the one-command-run change, which takes this text in).
- A Codex run over any target also needs an agent-provider statement for
  Codex with its provider for that target; none exists.
- On folding into `openspec/`, the warrant block's
  `DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15` must belong to an id family
  `apps/three-surface-poc/src/polaris-authority-sweep.test.ts` knows
  (`WARRANT_FAMILIES`); check that test at fold-in time [Unknown whether the
  current families admit it].

## Migration / supersession plan

- Folded into `openspec/changes/polaris-dossier-one-command-run/` at its next
  revision, reviewed with it, and signed with it by version tag. No byte of
  another change moves now.
- Nothing is superseded by this delta; the direction record states what the
  direction supersedes.

## Owner question carried with the delta

The content-class trade-off is the owner's, not the drafter's. This draft
takes the disclosure arm: the tool may read and send any class in the
clone, Syzygy's own packets carry only listed classes, and the page says so.
The other arm refuses a launched run unless the statement lists every
content class present in the readable clone; it holds the line the direction
record states, at the cost that a Redis run may not start until the
statement is widened. Register row P-111 asks this as Q2.

## Review

**Required class:** Full review per CC-REV-1 (Normative), fresh context, on
the egress and trust boundary; brief in `REVIEW-BRIEF.md` beside this file.
Round 1 (`docs/reviews/R-DOSSIER-CLI-SUBPROCESS-1-RAW.md`) was `REVISE`; its
eleven findings were repaired once, mapped in `ROUND-1-DISPOSITIONS.md`.
Round 2 (`docs/reviews/R-DOSSIER-CLI-SUBPROCESS-2-RAW.md`) was `REVISE` with
one revise finding (administrator-managed settings could redirect the
provider) and five notes, classified in `ROUND-2-DISPOSITIONS.md`. Under the
lead's cycle-3 decision the revise finding was repaired with its fail-closed
arm (a), and notes 2 to 5 were repaired; note 6 is the owner's (P-111 Q2) and
is left unchanged. The mapping is in `ROUND-2-REPAIRS.md`. One round 3
follows; a notes-only round clears these bytes, a `REVISE` is classified and
the lane stops.
