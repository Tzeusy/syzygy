# Owner act — Polaris Butlers project-shape observer registry-entry adoption

Date: 2026-09-02

Owner: Tzeusy

Act identity: `PWB-OBSERVER-REGISTRY-ENTRY-ADOPTION-2026-09-02`

Act type: `adopt-registry-entry`

Project identity: `project:syzygy`

Artifact identity: `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`

Exact digest (SHA-256): `d71eadb612cf657983d96ad44415b832054dc37e51ea674e569d9b8f655d05d7`

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
ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY: d71eadb612cf657983d96ad44415b832054dc37e51ea674e569d9b8f655d05d7
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
- recording tag: `pwb-adopt-registry-entry-signed-2026-09-02`, on the commit carrying this act record.

## Effect

The adapter-registry entry below (`polaris-butlers-project-shape`) is
adopted in Syzygy's governance home
`.syzygy/governance/declarations/adapter-registry` for `project:syzygy` and
the configured Butlers repository, with read-only authority and an empty
write surface. It declares exactly what the observer may read (the signed PWB
source population), which policy screens it, and that the observer has no
write, execution, egress or second-repository capability. The entry is a
declared mapping only: no such module exists yet, and adopting the entry
authorizes none to be written.

The act is a warrant, never evidence that any effect succeeded. State (1) is
owner-trusted, uncorrelated and same-tree forgeable from Syzygy's
perspective; its digest detects later drift, not authorship or attendance.
An edit to the artifact breaks this act's digest binding; changes travel as a
new act.

## What this act does not authorize

This act is one of the three separate authorities PWB-REQ-005 requires and
satisfies only its own. It grants no observation consent and approves no
secret-classification policy; a body read still needs both of those acts in
a valid state, plus separate PWB implementation authorization (task 1.8).

It grants no write, egress, execution, deployment, release, recovery, mission,
second-repository, autonomous or multi-user authority, edits no signed
artifact, accepts no candidate contract and amends no doctrine.
