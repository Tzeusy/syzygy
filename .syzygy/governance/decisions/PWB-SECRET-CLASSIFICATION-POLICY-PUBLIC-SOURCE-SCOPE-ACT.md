# Owner act — Polaris Butlers secret-classification policy approval (public-source screening scope)

Date: 2026-10-07

Recorded at (UTC): 2026-10-07T17:47:25Z

Owner: Tzeusy

Act identity: `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL-2026-10-07`

Act type: `approve-policy`

Project identity: `project:syzygy`

Artifact identity: `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`

Exact digest (SHA-256): `d42defcaf4dbb9b4e815f988ef8ba62be1dad081aa851d430b427b35c42f346b`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by the owner's option selection recorded below

Supersession / revocation: this act supersedes, for the `approve-policy` role only,
the 2026-10-02 act recorded at `.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md`. Its argument
`66cd41ee626efb11d666d19c0cd42c6d001ec4482837b71475c42f661f1d936c` was the policy's exact digest until this act's patch was
applied. That record, its digest, its tag and the bytes it bound remain
immutable history. This act is revoked only by a later exact owner act naming
it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the confirmed packet at `.syzygy/governance/contracts/candidates/public-source-screening-scope/OWNER-DECISION-PACKET.md`, which
by design carries no digest. The act takes this phrase, whose argument is the
row of the package manifest:

```text
APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY: d42defcaf4dbb9b4e815f988ef8ba62be1dad081aa851d430b427b35c42f346b
```

The owner did not type the phrase. On 2026-10-07 the owner answered a structured
question in the Claude Code CLI that opened "Do you sign the public-source screening scope version 1, POLICY-CANDIDATE.json at its row of the screening scope manifest?" by selecting the
option below; the selection is the instruction, and it names the policy "at the
manifest row". The label and description, verbatim:

| Label | Description |
|---|---|
| "Sign it, with Q2 to Q8 as recommended" | "Q2 widen the read gate to the simulated list, Q3 accept, Q4 this one alone, Q5 and Q6 accept, Q7 confirm, Q8 defer." |

The argument was read from the row of `.syzygy/governance/contracts/candidates/public-source-screening-scope/PUBLIC-SOURCE-SCREENING-SCOPE-MANIFEST.txt`, re-derived
from the builder's proposed bytes at recording, and, after the package's patch
was applied in the same change, matched the policy on disk. A swapped argument
would have been refused: the recorder rejects an argument that is not the row.

Frozen provenance:

- frozen subject (package bytes): `02c37988264d77d7a3114895a49c34795aba45b7`;
- manifest SHA-256: `1cbf45a0da07a4cf769a17b6ac98960c6ae214c2d88a4f974e7b9d5026bc4f83`;
- confirmation review: `.syzygy/governance/contracts/candidates/public-source-screening-scope/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-4-RAW.md`, verdict
  `CONFIRM WITH EXCEPTIONS`, its head bound to the manifest file's SHA-256 above; notes, if
  any, are dispositioned in `.syzygy/governance/contracts/candidates/public-source-screening-scope/ROUND-4-DISPOSITIONS.md`; the raw names
  reviewed commit `895f1622ebf55fa397f7552ad3b5a85c6ad9dc7b` [Observed — the raw's own line; binding is by
  digest]; and
- recording tag: `pwb-approve-policy-public-source-scope-signed-2026-10-07`, on the commit carrying this act record.

## Effect

The policy `polaris-butlers-project-shape-secrets`, policy-owning project
`project:syzygy`, is approved at version `1.2.0-public-source-candidate.1` as the observing project's
secret-classification policy: the base scope for the pair
(`project:syzygy`, `repository:butlers-configured-poc`) and the one content class
`declared-project-shape-text` is byte-identical to the bytes the superseded act
approved, and the policy gains one additive top-level object,
`publicSourceScope`, for admitted public repositories. That scope classifies
only into `code-structure`, `code-content` and `derived-composites`, never
`work-history`; every other admitted blob is indeterminate and excluded from
reading and egress; every detector and the active-content rule apply unchanged;
and the closed exclusion-reason set is the values of the exported constant
`GENERATION_EXCLUSION_REASONS`, which the recorder required to be readable
before recording. `policyVersion` is the only existing value that changes.

## What this act does not authorize

This act is the policy authority PWB-REQ-005 and the public-source scope need
and satisfies only its own. It names no repository and grants no observation
consent, no read, no egress and no provider call: each takes its own act
(REQ-polaris-generation-025). The Butlers read gate refuses a policy on its
digest first, so it keeps refusing this one until the change that records this
act re-points the gate as the packet's Q2 describes; the recorder does not do
that. It grants no write, execution, deployment, release, recovery, mission,
autonomous or multi-user authority, widens no consent, edits no performed
record, accepts no candidate contract and amends no doctrine. It proves no
read, screening, parse, render or answer result.
