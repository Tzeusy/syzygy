# Owner act — Butlers project-shape observation consent

Date: 2026-09-02

Owner: Tzeusy

Act identity: `PWB-BUTLERS-OBSERVATION-CONSENT-2026-09-02`

Act type: `consent-observation`

Project identity: `project:syzygy`

Artifact identity: `.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md`

Exact digest (SHA-256): `5d705d75f993059d5ae5561b1a6f99d143462d9d2e5bcea8ecc9b0c258777841`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by performing the offered state-(1) phrase

Supersession / revocation: none — this act supersedes no earlier act and is
revoked only by a later exact owner act naming it

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the independently confirmed packet at
`.syzygy/governance/contracts/candidates/pwb-effect-acts/OWNER-SIGNOFF-PACKET.md`
and performed this one act by writing exactly:

```text
CONSENT TO BUTLERS PROJECT-SHAPE OBSERVATION: 5d705d75f993059d5ae5561b1a6f99d143462d9d2e5bcea8ecc9b0c258777841
```

The argument is the SHA-256 of the artifact itself. It was recomputed at
recording and matched the phrase, the manifest row and the bytes committed at
frozen subject `48e0f5db645d1fb08e5e3a65c5e50dbcece40412`. The act instant is the moment the owner
wrote the phrase, in-interaction, on 2026-09-02.

Frozen provenance:

- reviewed subject: `48e0f5db645d1fb08e5e3a65c5e50dbcece40412` (this pins `ACT-SEMANTICS.md`, the
  manifest and all three artifacts as one tree);
- owner-packet head: `a322a60e9f2b166273a80e3fc145bc3a8193c962`;
- security review of the original subject and confirmation review of this
  subject: `CONFIRM`;
- owner-packet readability review: `CONFIRM`; and
- recording tag: `pwb-consent-observation-signed-2026-09-02`, on the commit carrying this act record.

## Effect

The consent record below is the owner's effective observation consent for
the pair (`project:syzygy`, `repository:butlers-configured-poc`) and the one
content class `declared-project-shape-text`. Scope: read-only Git objects
selected by the signed PWB source population at the Butlers revision the POC
observes. Excluded: PostgreSQL and every other data store, credential stores
and secret APIs, `.env` and credential files, arbitrary implementation-file
bodies, working-tree traversal, code execution, network egress, writes to
Butlers, and any second repository. The consent has no silent expiry; the
owner may narrow or revoke it only by a later exact act. It does not
retroactively authorize the reads recorded in the precondition-read incident.

The act is a warrant, never evidence that any effect succeeded. State (1) is
owner-trusted, uncorrelated and same-tree forgeable from Syzygy's
perspective; its digest detects later drift, not authorship or attendance.
An edit to the artifact breaks this act's digest binding; changes travel as a
new act.

## What this act does not authorize

This act is one of the three separate authorities PWB-REQ-005 requires and
satisfies only its own. It approves no secret-classification policy and
adopts no adapter-registry entry; a body read still needs both of those acts
in a valid state, plus separate PWB implementation authorization (task 1.8).

It grants no write, egress, execution, deployment, release, recovery, mission,
second-repository, autonomous or multi-user authority, edits no signed
artifact, accepts no candidate contract and amends no doctrine.
