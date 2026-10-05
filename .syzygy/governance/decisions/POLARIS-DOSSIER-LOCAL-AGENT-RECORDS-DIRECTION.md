# Owner direction — local-agent dossiers: Syzygy's own records

Date: 2026-10-05

Owner: Tzeusy

Decision ID: `POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-2026-10-05`

This direction follows the four `POLARIS-DOSSIER-LOCAL-AGENT-*` directions
given the same day. It answers question R1, which the repair of the first
fresh-context review of draft PR #353 raised for the owner: the operator's
agent runs as the operator, so it can write anything Syzygy stores on that
machine.

It is a plain owner direction. It binds no artifact digest, adds no row to
`ACCEPTANCE-ACT-RECORD.md` and registers nothing. It does not sign off the
local-agent amendment; only the owner's sign-off binds that (VIS-4).

## The owner's words

On 2026-10-05, in the Claude Code CLI, the owner answered one structured
question. The selected option is reproduced with its description as shown.

**R1.** "On your machine the agent runs as you, so it can write anything
Syzygy stores (run records, check results). How should the dossier mode
handle Syzygy's own records?"

| Label | Description |
|---|---|
| "Re-derive, label Inferred (Recommended)" | "Nothing Observed rests on a stored record: `check` and `render` re-derive every quotation and check from re-hashed git objects each time; repair counts, timestamps and history are labelled Inferred because the agent could have edited them. No setup needed." |

Options not taken: "Separate OS user" and "Sandbox the agent".

## The direction

1. No Observed label in a dossier rests on a record Syzygy stored on the
   operator's machine. `check` and `render` re-derive every quotation and
   every check from re-hashed git objects on each run.
2. Repair counts, timestamps and run history are labelled Inferred, because
   the operator's agent could have edited them.
3. No separate OS user or sandbox is required for the dossier mode's records.
