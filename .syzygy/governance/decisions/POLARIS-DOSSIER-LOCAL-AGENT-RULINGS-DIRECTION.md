# Owner direction — local-agent dossiers: RFC7-20 reading and code execution

Date: 2026-10-05

Owner: Tzeusy

Decision ID: `POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05`

This direction follows `POLARIS-DOSSIER-LOCAL-AGENT-MODE-DIRECTION.md`, given
the same day. It is a plain owner direction: it binds no artifact digest, adds
no row to `ACCEPTANCE-ACT-RECORD.md` and registers nothing. It amends no
contract and no specification. The generator-spec amendment that relies on it
binds only on the owner's sign-off (VIS-4).

## The owner's words

On 2026-10-05, in the Claude Code CLI, the owner answered two structured
questions raised while the local-agent amendment was being drafted. The
options selected, with their descriptions as shown, are reproduced below.

**Q1.** "An accepted contract (RFC7-20) says a draft is 'not computed' without
SEC-2 named-provider consent, and renders Unknown. Your agent session's
provider has no such consent today. How should a dossier drafted by your own
Claude Code/Codex session satisfy it?"

| Label | Description |
|---|---|
| "Rule it by interpretation" | "Read RFC7-20 as governing drafts Syzygy computes; an operator-computed draft is admitted with disclosure and byte-verified quotes. No extra record, but it rests on an interpretation of an accepted contract and a reviewer may call it a contract change." |

The option not taken was "Name my provider per project (Recommended)", one
per-project consent record naming the operator's provider.

**Q2.** "Your agent can build or run code inside the clone (SEC-3 only binds
Syzygy's own execution). What should the brief say?"

| Label | Description |
|---|---|
| "Allow, disclose" | "The agent may run the project (e.g. start redis-server to observe behaviour); claims based on that are labelled Inferred and the run record lists the commands the agent reports running." |

The option not taken was "Forbid, disclose (Recommended)".

## The direction

1. **The owner's reading of RFC7-20.** RFC7-20's condition, "absent SEC-2
   named-provider consent it is not computed", governs drafts that Syzygy
   computes. A draft computed by the operator's own agent session is admitted
   in the local-agent mode under three conditions:
   - the run record and page disclose how the draft was computed;
   - the operator declares the tool and provider, and they are recorded;
   - every rendered quotation is byte-verified against the pinned blobs.

   The owner chose this reading over a per-project provider consent record,
   knowing that a reviewer may call the reading a contract change. That
   trade-off is preserved here. A reviewer who finds it to be one should
   report it, not resolve it.
2. **Code execution by the agent.** In the local-agent mode the operator's
   agent session may build and run the observed project, for example starting
   its server to observe behaviour. The rules:
   - any claim that rests on such execution is labelled Inferred;
   - the run record lists the commands the agent reports having run;
   - Syzygy itself still never executes observed project code (SEC-3), and
     this direction changes nothing about Syzygy's own behaviour.
