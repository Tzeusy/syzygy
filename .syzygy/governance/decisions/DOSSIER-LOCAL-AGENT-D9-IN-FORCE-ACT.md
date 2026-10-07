# Owner act — D9 in force for operator-agent runs

Date: 2026-10-07

Recorded at (UTC): 2026-10-07T17:53:25Z

Owner: Tzeusy

Act identity: `D9-IN-FORCE-OPERATOR-AGENT-2026-10-07`

Act type: `bind-exact-bytes`

Project identity: `project:syzygy`

Artifact identity: `.syzygy/governance/contracts/candidates/dossier-local-agent-acts/instances/in-force/D9-IN-FORCE-RECORD.md`

Exact digest (SHA-256): `41fdfaea8cbde4cd8220910113fb5b376c7834a470d8c2d9badd9ab0fec9ac66`

Scope: REQ-polaris-generation-033's execution rule only

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by the owner's option selection recorded below

Supersession / revocation: supersedes nothing; revoked only by a later exact
owner act naming it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the confirmed packet at
`.syzygy/governance/contracts/candidates/dossier-local-agent-acts/OWNER-SITTING-PACKET.md`, which by design carries no digest. The act takes
this phrase, whose argument is this record's row of the sitting manifest:

```text
BIND D9 TO EXACT BYTES FOR OPERATOR-AGENT RUNS: 41fdfaea8cbde4cd8220910113fb5b376c7834a470d8c2d9badd9ab0fec9ac66
```

The owner did not type the phrase. On 2026-10-07 the owner answered a structured
question in the Claude Code CLI that opened "Do you sign the D9 in-force record at its row of the dossier local-agent acts manifest?" by selecting the
option below; the selection is the instruction, and it names the record "at
the manifest row". The label and description, verbatim:

| Label | Description |
|---|---|
| "Sign it" | "Binds D9 to the current security.md and v1.md bytes; it runs nothing until a choice for one run is recorded." |

The argument was read from this record's row of
`.syzygy/governance/contracts/candidates/dossier-local-agent-acts/DOSSIER-LOCAL-AGENT-SITTING-MANIFEST.txt` at the frozen commit and matched the record on
disk at recording. A swapped argument would have been refused: the recorder
rejects an argument that is not this record's row.

Frozen provenance:

- frozen subject (package bytes): `d19ec98bb3bfb9c83f48919715cb5b8c7710ede8`;
- the sitting manifest file hashes to `ecf916c4f67c2ba8c8a33739653eef75a36874b925bd28e08852219243f1fb56` (a container digest,
  no act's argument; worded so CG-7e's bare-heading pass does not read it as
  a stale copy of this act's argument);
- confirmation review: `.syzygy/governance/contracts/candidates/dossier-local-agent-acts/reviews/R-DOSSIER-LOCAL-AGENT-SITTING-3-RAW.md`, verdict
  `CONFIRM WITH EXCEPTIONS`, its head bound to the manifest file's SHA-256 above; notes, if
  any, are dispositioned in `.syzygy/governance/contracts/candidates/dossier-local-agent-acts/ROUND-3-DISPOSITIONS.md`; the raw names
  reviewed commit `d19ec98bb3bfb9c83f48919715cb5b8c7710ede8` [Observed — the raw's own line; binding is by
  digest]; and
- recording tag: `dossier-local-agent-d9-in-force-signed-2026-10-07`, on the commit carrying this act record.

## Effect

The record binds D9, adopted 2026-10-06, to the exact whole-file bytes of `security.md` and `v1.md` it lists, so the act cross-check of RFC3-16(a) may treat D9 as in force for REQ-polaris-generation-033's execution rule while both files hash to those digests, and not otherwise.

## What this act does not authorize

This act satisfies only its own authority; the sitting's other acts each take
their own act and none implies another (REQ-polaris-generation-025). It gives
no observation consent, adopts no registry entry or screening policy, amends
no doctrine, contract or specification, and grants no read, egress, write,
execution, deployment, release, autonomous or multi-user authority beyond
what its Effect states. It proves no read, screening, generation or answer
result.
