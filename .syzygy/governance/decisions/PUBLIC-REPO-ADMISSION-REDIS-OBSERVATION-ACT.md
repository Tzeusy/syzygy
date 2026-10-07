# Owner act — redis/redis public-repository observation consent

Date: 2026-10-07

Recorded at (UTC): 2026-10-07T17:50:25Z

Owner: Tzeusy

Act identity: `PUBLIC-OBS-REDIS-2026-10-07`

Act type: `consent-observation`

Project identity: `project:syzygy`

Artifact identity: `.syzygy/governance/contracts/candidates/public-repo-admission/instances/redis/OBSERVATION-CONSENT.md`

Exact digest (SHA-256): `a733220dcbc4276d396e32f51c39dcc4665e07579ecca3f0074e7e6e5a1916a4`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by the owner's option selection recorded below

Supersession / revocation: none recorded by this act; an earlier version of
the same record, if one was performed, is superseded only by a later act that
names it. This act is revoked only by a later exact owner act naming it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the confirmed packet at
`.syzygy/governance/contracts/candidates/public-repo-admission/OWNER-DECISION-PACKET.md`, which by design carries no digest. The act takes
this phrase, whose argument is this record's row of the package manifest:

```text
CONSENT TO PUBLIC OBSERVATION OF REDIS-REDIS: a733220dcbc4276d396e32f51c39dcc4665e07579ecca3f0074e7e6e5a1916a4
```

The owner did not type the phrase. On 2026-10-07 the owner answered a structured
question in the Claude Code CLI that opened "Do you sign the Redis observation consent, redis/OBSERVATION-CONSENT.md at its row of the public-repo admission manifest?" by selecting the
option below; the selection is the instruction, and it names the records "at
the manifest rows". The label and description, verbatim:

| Label | Description |
|---|---|
| "Sign it" | "Syzygy may read the Git objects of the four consented Redis commits and nothing else of Redis." |

The argument was read from this record's row of
`.syzygy/governance/contracts/candidates/public-repo-admission/PUBLIC-REPO-ADMISSION-MANIFEST.txt` at the frozen commit and matched the record on
disk at recording. A swapped argument would have been refused: the recorder
rejects an argument that is not this record's row.

Frozen provenance:

- frozen subject (package bytes): `7704b4a575acf29de93e3872ff549a856e6395ec`;
- manifest SHA-256: `51f70c07ed1bb5ea081c08fc2c06dd61b865f0c6888ae3f0faf17e8bf50bc649`;
- confirmation review: `.syzygy/governance/contracts/candidates/public-repo-admission/reviews/R-PUBLIC-ADMISSION-7-RAW.md`, verdict
  `CONFIRM WITH EXCEPTIONS`, its head bound to the manifest file's SHA-256 above; notes, if
  any, are dispositioned in `.syzygy/governance/contracts/candidates/public-repo-admission/ROUND-7-DISPOSITIONS.md`; the raw names
  reviewed commit `7704b4a575acf29de93e3872ff549a856e6395ec` [Observed — the raw's own line; binding is by
  digest]; and
- recording tag: `public-admission-redis-observation-signed-2026-10-07`, on the commit carrying this act record.

## Effect

The record is the owner's effective observation consent for the pair (`project:syzygy`, `repository:redis-redis`) at the four admitted revisions it lists: read-only reads of those commits' Git objects, fetched one commit at a time, with no execution, no write and no egress.

## What this act does not authorize

This act satisfies only its own authority; the package's other records each
take their own act and none implies another (REQ-polaris-generation-025). It
adopts no registry entry or screening policy, amends no contract, and grants
no read, egress, write, execution, deployment, release, autonomous or
multi-user authority beyond what its Effect states. Observation consent
permits no egress, and egress consent permits no read. It proves no read,
screening, generation or answer result.
