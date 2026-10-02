# Owner act — Polaris Butlers secret-classification policy approval (behaviour-contract re-pin)

Date: 2026-10-02

Owner: Tzeusy

Act identity: `PWB-SECRET-CLASSIFICATION-POLICY-APPROVAL-BEHAVIOR-CONTRACT-REPIN-2026-10-02`

Act type: `approve-policy`

Project identity: `project:syzygy`

Artifact identity: `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`

Exact digest (SHA-256): `66cd41ee626efb11d666d19c0cd42c6d001ec4482837b71475c42f661f1d936c`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by the owner's option selection recorded below

Supersession / revocation: this act supersedes, for the `approve-policy` role only, the 2026-09-05 act recorded at `.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md`.
Its argument `d148f0360841cfc30cdc9ecedbffe722e31044e4bb048cd33f83cc193ee88e75` was the subject's exact digest until
this act's patch was applied. That record, its digest, its tag and the bytes
it bound remain immutable history. This act is revoked only by a later exact
owner act naming it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the independently confirmed packet at
`.syzygy/governance/contracts/candidates/pwb-behavior-contract-repin/OWNER-DECISION-PACKET.md`,
which by design carries no digest. The act takes this phrase, whose argument
is this subject's row of the effect manifest:

```text
APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY: 66cd41ee626efb11d666d19c0cd42c6d001ec4482837b71475c42f661f1d936c
```

The owner did not type the phrase. On 2026-10-02 the owner answered a structured
question in the Claude Code CLI that opened "Perform the PWB behaviour-contract re-pin?" by
selecting the option below; the selection is the instruction, and it names
both acts "at the manifest rows". The label and description, verbatim:

| Label | Description |
|---|---|
| "A + B + C now (Recommended)" | "Perform both acts at the manifest rows and give direction C; I write the recorder, record both acts and re-point the gate in one change, so reads keep working." |

[Observed] The question text also carried a garbled parenthetical,
verbatim: "(policy ad9cd6… is the registry row; 66cd41… is the policy row)". Its first word can be read as
pairing the policy with the registry row's prefix; the rest of it states the
pairing the manifest carries. It is not the binding: the option binds each
act to its own manifest row. The argument above was read from the policy row of
`.syzygy/governance/contracts/candidates/pwb-behavior-contract-repin/PWB-EFFECT-REPIN-MANIFEST.txt` at the reviewed
commit, re-derived from the builder's proposed bytes at recording, and,
after the package's patch was applied through its builder in the same
change, matched the artifact on disk. A swapped argument would have been
refused: the recorder rejects an argument that is not this subject's row.
The full account is `.syzygy/governance/decisions/OWNER-INSTRUCTIONS-2026-10-02-PWB-BEHAVIOR-CONTRACT-REPIN.md`.

Frozen provenance:

- frozen subject (package bytes) and owner-packet head: `140874b7364266475dd8980be480e2783e0d8e72`;
- effect manifest SHA-256: `036e49ee804126fbf56f77d593bc0d62c155e283f3535f6ef3952f60aec04fb8`;
- confirmation review: `docs/reviews/R-PWB-BEHAVIOR-CONTRACT-REPIN-RAW.md`, verdict
  `CONFIRM WITH EXCEPTIONS`, its head bound to the effect manifest file's SHA-256 above;
  its two findings are notes, dispositioned in
  `.syzygy/governance/contracts/candidates/pwb-behavior-contract-repin/ROUND-1-DISPOSITIONS.md`; the raw names reviewed commit
  `140874b7364266475dd8980be480e2783e0d8e72` [Observed — the raw's own line; binding is by digest]; and
- recording tag: `pwb-approve-policy-signed-2026-10-02`, on the commit carrying this act record.

## Effect

The re-pinned policy (`polaris-butlers-project-shape-secrets`, version
`1.1.0-candidate.1`, policy-owning project `project:syzygy`) is approved as
the observing project's secret-classification policy for the pair
(`project:syzygy`, `repository:butlers-configured-poc`) and the one content
class `declared-project-shape-text`, in place of the 2026-09-05 approval.
Exactly two values change: `governingBehaviorContract.version` now names the
PWB `spec.md` that the `pwb-readability-successor-v1.0` sign-off binds (the
`spec.md` row of that package's manifest), and `signedBy` names that
version-tagged sign-off and its record. Every denied credential filename and
suffix, every detector, the strict-UTF-8 rule, the closed extraction class
per source, the Markdown code-context profile and every retention rule are
byte-identical to the bytes the 2026-09-05 act approved.

## What this act does not authorize

This act is one of the three separate authorities PWB-REQ-005 requires and
satisfies only its own. It grants no observation consent, and it neither
approves nor adopts the registry entry, which took its own separate act the same
day. The read gate evaluates this act only under the owner's plain
continuation direction C of the same selection, recorded at
`.syzygy/governance/decisions/OWNER-INSTRUCTIONS-2026-10-02-PWB-BEHAVIOR-CONTRACT-REPIN.md`; no implementation consumes
`governingBehaviorContract` or any other field it did not read before.

It grants no write, egress, execution, deployment, release, recovery,
mission, second-repository, autonomous or multi-user authority, widens no
consent, changes no version label, edits no performed record, accepts no
candidate contract and amends no doctrine. It proves no read, screening,
parse, render or answer result.
