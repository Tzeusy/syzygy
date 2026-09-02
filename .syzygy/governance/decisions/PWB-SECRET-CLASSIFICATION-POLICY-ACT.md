# Owner act — Polaris Butlers secret-classification policy approval

Date: 2026-09-02

Owner: Tzeusy

Act identity: `PWB-SECRET-CLASSIFICATION-POLICY-APPROVAL-2026-09-02`

Act type: `approve-policy`

Project identity: `project:syzygy`

Artifact identity: `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`

Exact digest (SHA-256): `513a3be75bbd417a06d475c46bb423393ac59013e307157357083f29781a2a61`

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
APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY: 513a3be75bbd417a06d475c46bb423393ac59013e307157357083f29781a2a61
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
- recording tag: `pwb-approve-policy-signed-2026-09-02`, on the commit carrying this act record.

## Effect

The policy below (`polaris-butlers-project-shape-secrets`, policy-owning
project `project:syzygy`) is approved as the observing project's
secret-classification policy for that pair and content class, across every
ingest boundary the PWB spec names. Denied credential filenames and suffixes,
four detectors, strict UTF-8 without NUL and a closed extraction class per
source are mandatory; any detector match excludes the whole artifact with
class `excluded-artifact`, anything unclassifiable excludes it with class
`unclassifiable-excluded`, and only the digest, path, policy id/version and
detector id or exclusion reason are retained. Raw bodies are never stored,
logged, rendered, returned or sent anywhere.

The act is a warrant, never evidence that any effect succeeded. State (1) is
owner-trusted, uncorrelated and same-tree forgeable from Syzygy's
perspective; its digest detects later drift, not authorship or attendance.
An edit to the artifact breaks this act's digest binding; changes travel as a
new act.

## What this act does not authorize

This act is one of the three separate authorities PWB-REQ-005 requires and
satisfies only its own. It grants no observation consent and adopts no
adapter-registry entry; a body read still needs both of those acts in a
valid state, plus separate PWB implementation authorization (task 1.8).

It grants no write, egress, execution, deployment, release, recovery, mission,
second-repository, autonomous or multi-user authority, edits no signed
artifact, accepts no candidate contract and amends no doctrine.
