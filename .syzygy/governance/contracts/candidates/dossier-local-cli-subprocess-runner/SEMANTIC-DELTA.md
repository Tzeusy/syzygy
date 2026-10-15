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
`packages/` or `docs/`, by a fixed-string sweep this session). It refines
REQ-polaris-generation-041 ("with the agent tool, version and model the
operator declared for the run") and REQ-polaris-generation-042 ("the agent
tool's own installation and configuration as the tool requires") without
editing either. No identifier is retired, renamed or renumbered.

**Change class:** **Normative.** Under the candidate REQ-041 the agent tool
is whatever the operator declared and is started however the supervisor
chooses; nothing says what reaches the tool from outside the run, which
agent tools may be launched, what happens when the binary is missing, or
that no provider client may be built. Under this delta a build that launches
an undeclared binary, lets the operator's user, project or local settings
widen a launched session, passes instructions or guidance implicitly, links
a provider SDK or API client into the model step, runs a session with no
time bound, or reports a run as ready when its binary is absent fails.

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

In a launched run Syzygy SHALL perform every model step only by starting the operator's locally installed agent command-line tool as a child process of the run's supervisor, and by no other means. The tool SHALL be one of a closed set, `claude` (Claude Code) and `codex` (Codex CLI), and SHALL be the one the operator declared for the run by name and absolute executable path; Syzygy SHALL NOT search for, substitute or fall back to another tool, path or version. Syzygy SHALL NOT contain, load or call a model-provider SDK or API client, hold or read a provider credential, or resolve a provider route for this step; authentication is the tool's own, under the operator's account, and Syzygy neither parses nor transmits it; at most it copies the tool's own credential file, unparsed, to where the tool expects it inside the session's view, and records that it did.

Syzygy SHALL give the tool, explicitly on its command line or in files it names there, and in no other way: the session's workspace directory (its working directory and its only writable path, as REQ-polaris-generation-042 states); the role's instructions file, written by Syzygy and recorded by digest; the artifacts output path the session's result is handed in through; and the skill and MCP guidance for the role, each skill as a named file or directory and each MCP server as an explicit configuration, or the explicit statement that the role has none. Syzygy SHALL start the tool with its user, project and local settings layers, its user-level instruction files, its plugins, its hooks and its ambient MCP configuration excluded, using the tool's own flags for each where they exist, and otherwise a private configuration home inside the session's view holding only what Syzygy wrote there. Where the tool offers no means to exclude a layer, Syzygy SHALL record that layer as not excluded, labelled Observed as Syzygy's own finding about the tool, and the run page SHALL disclose it; Syzygy SHALL NOT start the session if that layer could grant a permission the role is not allowed.

Before `init`, Syzygy SHALL check that the declared executable exists at its path, is executable, and reports the declared version; where any check fails it SHALL refuse the launched run, naming the failure, start no session, and report the run's readiness and every claim that depends on the model step as Unknown, never as ready, passed or empty. Each session SHALL carry a time bound, declared for the run and no later than the run deadline; Syzygy SHALL stop a session that exceeds it, record the stop, and leave the session's result absent and its dependent claims Unknown. A session that exits non-zero, writes no result at its artifacts path, or writes one that fails validation SHALL count as no result.

For each launched session the launch record of REQ-polaris-generation-041 SHALL also hold, labelled Observed: the tool's name, executable path and reported version; the digest of the instructions file; the artifacts output path; the exact skill and MCP guidance given, by path and digest, or that none was given; each settings layer and whether it was excluded, and by what means; and the session's time bound and whether it was reached.

This requirement grants no consent. Every transmission the tool makes to its provider remains subject to the consents and agent-provider statements in force for the repository and content class; a run whose declared tool and provider have no agent-provider statement in force for the target SHALL be refused before any session starts.

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
- **AND** where the tool offers no exclusion for a layer, the run is refused if that layer could grant a permission the role is not allowed

#### Scenario: Binary absent

- **WHEN** the declared executable is missing, not executable, or reports a different version
- **THEN** Syzygy refuses the launched run before `init`, naming the failure, and starts no session
- **AND** the run's readiness and every claim depending on the model step read Unknown, and no page or status reads ready or green

#### Scenario: Session exceeds its time bound

- **WHEN** a launched session is still running at its time bound
- **THEN** Syzygy stops it and records the stop
- **AND** the session's result is absent and its dependent claims are Unknown

#### Scenario: No provider client

- **WHEN** the built Syzygy packages and their resolved dependencies are inspected
- **THEN** no model-provider SDK or API client is present in or reachable from the launched-run code, and no code path reads a provider credential variable
- **AND** the only process that contacts a model provider in a launched run is the declared tool

#### Scenario: Tool without a provider statement

- **WHEN** the operator declares `codex` for a target that has an agent-provider statement in force only for Claude Code with Anthropic
- **THEN** Syzygy refuses the launched run before any session starts, naming the missing statement

Form: event-response.

- **Case:** Launched runs with stand-in `claude` and `codex` executables that record their own argv, environment, parent process and the files they can read; an operator home seeded with a permissive allow rule, a hook that writes a marker file, a plugin and an MCP server; runs with the binary removed, made non-executable and reporting a wrong version; a stand-in that never exits; a declared tool with no provider statement for the target; a dependency inspection of the built packages.
- **Observable:** Each stand-in's recorded argv and readable files, the hook's marker file, the process tree, the launch records, the refusals and their wording, each page's readiness wording, the stop records, and the dependency inspection's output.
- **Oracle:** The expected argv, guidance and settings-exclusion list per role and tool, and the refusal and Unknown wording, written before the run; a list of known provider SDK package names and credential variable names for the inspection.
- **Oracle independence:** Argv, readable files and markers come from the stand-ins and the file system, not from Syzygy's launch record; the dependency inspection reads the lockfile and built output, not Syzygy's own claims.
- **Falsifier:** A session starts with an undeclared tool or path; an operator allow rule, hook, plugin or MCP server takes effect; instructions or guidance reach the tool by any route not on its command line or in a file it names; a missing or mismatched binary leaves any readiness or claim other than Unknown, or a session starts; a session runs past its bound; a provider SDK, API client or credential read is present; or a run without a provider statement for its tool starts a session.

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
| Claude Code | `--bare` | Skips hooks, plugin sync, auto-memory and CLAUDE.md discovery, but "Anthropic auth is strictly ANTHROPIC_API_KEY or apiKeyHelper via --settings (OAuth and keychain are never read)". | **Not fit:** it would require an API key, which is the API tooling the owner excluded, and it drops the operator's subscription login. |
| Claude Code | `--safe-mode` | Disables CLAUDE.md, skills, plugins, hooks, MCP servers, custom agents; "Auth, model selection, built-in tools and plugins, and permissions work normally." | Partial: does not by itself exclude settings-file allow rules [Inferred from "permissions work normally"]; would also disable the explicit skills the role needs. |
| Claude Code | `--disable-slash-commands` | "Disable all skills". | Use only for roles with no skill guidance. |
| Codex | `--ignore-user-config` | "Do not load `$CODEX_HOME/config.toml`; auth still uses `CODEX_HOME`". | Direct fit for the user layer, keeping the operator's login. |
| Codex | `--ignore-rules` | "Do not load user or project execpolicy `.rules` files". | Direct fit for the rules layers. |
| Codex | `-s read-only`, `-C <dir>`, `--add-dir`, `--ephemeral`, `-o <file>`, `--output-schema <file>` | Sandbox policy, working root, extra writable dirs, no session files, last-message file, response schema. | Workspace (`-C`), artifacts path (`-o`), schema, and no persisted transcript. `--add-dir` makes a directory *writable*, so the clone must not be passed that way. |

The prototype today does not pass `--setting-sources` or `--restricted`; it
relies on a private home (`prepareAgentHome`) holding only a copied
credential file and a seeded onboarding record, which keeps the operator's
user settings out of the view [Inferred: from the code; not observed in a
run]. Project and local settings of the session's own directory are Syzygy's
to write, and are empty. Whether Claude Code reads project settings from an
`--add-dir` directory such as the clone is Unknown.

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
  and no settings-source flag.
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
  per-session bound; implementation waits for the sign-off.
- Bead `syzygy-bc0g` (re-scoped to this route), `syzygy-zzt5` item (a), and
  `syzygy-zwja` (the one-command-run change, which takes this text in).
- A Codex run over any target also needs an agent-provider statement for
  Codex with its provider for that target; none exists.

## Migration / supersession plan

- Folded into `openspec/changes/polaris-dossier-one-command-run/` at its next
  revision, reviewed with it, and signed with it by version tag. No byte of
  another change moves now.
- Nothing is superseded by this delta; the direction record states what the
  direction supersedes.

## Review

**Required class:** Full review per CC-REV-1 (Normative), fresh context, on
the egress and trust boundary; brief in `REVIEW-BRIEF.md` beside this file.
