> **Candidate — binds nothing.** Review brief for the semantic delta beside
> it. A review performs no act.

# Review brief — DOSSIER-CLI-RUNNER-1 (local agent CLI subprocess runner)

## Round 1

**Subject:** `SEMANTIC-DELTA.md` in this directory, at the commit named in
the dispatch, read together with the direction record
`.syzygy/governance/decisions/OWNER-DIRECTION-DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15.md`.

**Focus:** the egress and trust boundary. Does the proposed
REQ-polaris-generation-045, with the direction record:

1. keep every transmission of target content inside an act already in
   force (repository, content class, agent tool and provider), and refuse
   otherwise — including Codex, for which no provider statement exists;
2. keep the operator's own tool settings (allow rules, hooks, plugins, MCP
   servers, instruction files) from widening a launched session, and say
   honestly what happens where a tool cannot exclude a layer;
3. exclude provider SDK and API client code and credential reads, with a
   falsifier that can actually catch one;
4. fail closed when the binary is absent, mismatched or overruns its bound,
   showing Unknown and never ready or green (VIS-2);
5. avoid overlapping the candidate change `polaris-dossier-one-command-run`
   or editing signed bytes;
6. state its authority finding (what is and is not already authorized)
   accurately against the files it cites.

**Governing references you may read:** the two files above; the decision
records they cite under `.syzygy/governance/decisions/`;
`openspec/changes/polaris-dossier-one-command-run/` and
`openspec/changes/polaris-dossier-local-agent-mode/`;
`.syzygy/governance/doctrine/` (VIS-2, VIS-4, SEC-2, SEC-3);
`packages/polaris-dossier/src/polaris.ts`; the `claude --help` and
`codex exec --help` output on the host.

**Forbidden:** reading any target repository (no Redis clone, no Butlers
checkout or path, nothing under any dossier state root or run directory),
running any `syzygy` dossier or polaris command, and any network call.

**Verdict words:** exactly one of `CONFIRM`, `CONFIRM WITH EXCEPTIONS`
(notes only) or `REVISE`, on line 4 of the raw. Findings numbered, each
marked revise or note, each anchored to a file and line and quoting it.

**Stopping rule (set before round 1):** a notes-only round clears these
bytes; a `REVISE` is repaired once and the package goes to the owner with
the repair unconfirmed; no round 2 is dispatched by this lane.
