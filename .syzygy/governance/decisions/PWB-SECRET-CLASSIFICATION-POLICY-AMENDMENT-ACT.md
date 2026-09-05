# Owner act — Polaris Butlers secret-classification policy approval (amendment)

Date: 2026-09-05

Owner: Tzeusy

Act identity: `PWB-SECRET-CLASSIFICATION-POLICY-APPROVAL-AMENDMENT-2026-09-05`

Act type: `approve-policy`

Project identity: `project:syzygy`

Artifact identity: `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`

Exact digest (SHA-256): `d148f0360841cfc30cdc9ecedbffe722e31044e4bb048cd33f83cc193ee88e75`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by performing the offered state-(1) phrase

Supersession / revocation: this act supersedes, for the `approve-policy` role
only, the 2026-09-02 act recorded at `.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-ACT.md`. That
record, its digest, its tag and the bytes it bound remain immutable history.
This act is revoked only by a later exact owner act naming it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the independently confirmed packet at
`.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/OWNER-DECISION-PACKET.md`,
after Decision 1 of that packet was recorded at
`.syzygy/governance/decisions/PWB-TRUTH-READINESS-AMENDMENT-ACT.md`,
and performed this one act by writing exactly:

```text
APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY: d148f0360841cfc30cdc9ecedbffe722e31044e4bb048cd33f83cc193ee88e75
```

The argument is the SHA-256 of the artifact itself. It was recomputed at
recording and matched the phrase, the effect-manifest row and the bytes
committed at frozen subject `4daea0868a0e15ea2f9407efc18f143dbabbd64b`. The act instant is the moment
the owner wrote the phrase, in-interaction, on 2026-09-05.

Frozen provenance:

- reviewed subject: `4daea0868a0e15ea2f9407efc18f143dbabbd64b` (this pins the effect manifest and
  both amended artifacts with the eleven behavior artifacts as one tree);
- owner-packet head: `875ef026f00b3b2a87b72f2977ab12380af5cc2a`;
- final evidence head: `62d3bb74b21e43b07a7b708f5c743e6ee27ac946`;
- final contract/oracle, security/public-interface and fresh-reader
  comprehension verdicts: `CONFIRM`;
- final owner-packet verdict: `CONFIRM`, zero findings; and
- recording tag: `pwb-approve-policy-signed-2026-09-05`, on the commit carrying this act record.

## Effect

The amended policy below (`polaris-butlers-project-shape-secrets`, version
`1.1.0-candidate.1`, policy-owning project `project:syzygy`) is approved as the
observing project's secret-classification policy for the pair
(`project:syzygy`, `repository:butlers-configured-poc`) and the one content
class `declared-project-shape-text`, across every ingest boundary the PWB spec
names, in place of the 2026-09-02 approval. Every denied credential filename
and suffix, all four secret detectors, strict UTF-8 without NUL and the closed
extraction class per source are unchanged and mandatory; every detector still
runs over the complete body, inert code contexts included. The amendment adds
one closed Markdown code-context profile: markup-like bytes wholly inside a
syntactically closed inline code span or fenced code block are inert for
active-content detection only, while a genuine active form outside such a
context, or a malformed code context, excludes the whole artifact. Any
detector match excludes the whole artifact with class `excluded-artifact`,
anything unclassifiable excludes it with class `unclassifiable-excluded`, and
only the digest, path, policy id/version and detector id or exclusion reason
are retained. Raw bodies are never stored, logged, rendered, returned or sent
anywhere, and admitted Markdown is never rendered as HTML.

The act is a warrant, never evidence that any effect succeeded. State (1) is
owner-trusted, uncorrelated and same-tree forgeable from Syzygy's
perspective; its digest detects later drift, not authorship or attendance.
An edit to the artifact breaks this act's digest binding; changes travel as a
new act.

## What this act does not authorize

This act is one of the three separate authorities PWB-REQ-005 requires and
satisfies only its own. It grants no observation consent and adopts no
amended adapter-registry entry (Decision 3 of the same packet remains a
separate owner act); a body read under the amended semantics still needs
the consent act and the applicable registry act in a valid state, plus the
owner's separate continuation of PWB implementation authorization across
the signed-spec, policy and registry escalation triggers.

It grants no write, egress, execution, deployment, release, recovery, mission,
second-repository, autonomous or multi-user authority, widens no consent,
edits no signed artifact, accepts no candidate contract and amends no
doctrine. It proves no read, screening, parse, render or answer result.
