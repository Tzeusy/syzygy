# Owner act — Polaris Butlers secret-classification policy approval (public-source screening scope, version 2)

Date: 2026-10-07

Recorded at (UTC): 2026-10-07T17:49:25Z

Owner: Tzeusy

Act identity: `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-APPROVAL-2026-10-07`

Act type: `approve-policy`

Project identity: `project:syzygy`

Artifact identity: `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`

Exact digest (SHA-256): `98a87f818e0c60ca11f808f9122bbd4b1df1ad72a29f85eb81b879fd644d3f49`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by the owner's option selection recorded below

Supersession / revocation: this act supersedes, for the `approve-policy` role only, the 2026-10-07 act recorded at `.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md`. That is the version-1 screening-scope act. Its argument
`d42defcaf4dbb9b4e815f988ef8ba62be1dad081aa851d430b427b35c42f346b` was the policy's exact digest until this act's patch was
applied. That record, its digest, its tag and the bytes it bound remain
immutable history. This act is revoked only by a later exact owner act naming
it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the confirmed packet at `.syzygy/governance/contracts/candidates/public-source-screening-scope-v2/OWNER-DECISION-PACKET.md`, which
by design carries no digest. The package manifest has four rows, one per
variant; the owner picked exactly one. The act takes this phrase, whose
argument is the chosen row:

```text
APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY: 98a87f818e0c60ca11f808f9122bbd4b1df1ad72a29f85eb81b879fd644d3f49
```

The owner did not type the phrase. On 2026-10-07 the owner answered a structured
question in the Claude Code CLI that opened "Do you sign screening scope version 2 at the row of its variant none in the version 2 manifest?" by selecting the
option below; the selection is the instruction, and it names the policy "at the
manifest row". The label and description, verbatim:

| Label | Description |
|---|---|
| "Sign it, variant none" | "README, changelog, contribution, licence files and top-level docs guides become readable, with Q3 to Q5 at the packet defaults." |

Chosen variant: `none`.

The argument was read from the chosen row of `.syzygy/governance/contracts/candidates/public-source-screening-scope-v2/PUBLIC-SOURCE-SCREENING-SCOPE-V2-MANIFEST.txt`,
re-derived from the builder's proposed bytes for that variant at recording,
and, after the variant's patch was applied in the same change, matched the
policy on disk. A swapped argument would have been refused: the recorder
rejects an argument that is not a row.

Frozen provenance:

- frozen subject (package bytes): `7327259c293263e64599988b9785e6c3ecd058a3`;
- manifest SHA-256: `7757e70c4d0e8e65c19c77f4970853967456cdd7f225077feac1f91e16200e1e`;
- confirmation review: `.syzygy/governance/contracts/candidates/public-source-screening-scope-v2/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-7-RAW.md`, verdict
  `CONFIRM WITH EXCEPTIONS`, its head bound to the manifest file's SHA-256 above; notes are dispositioned in `.syzygy/governance/contracts/candidates/public-source-screening-scope-v2/ROUND-7-DISPOSITIONS.md`; the raw names
  reviewed commit `be724397b9a1a72837eb2c7811efd356f5c010de` [Observed — the raw's own line; binding is by
  digest]; and
- recording tag: `pwb-approve-policy-public-source-scope-v2-signed-2026-10-07`, on the commit carrying this act record.

## Effect

The policy `polaris-butlers-project-shape-secrets`, policy-owning project
`project:syzygy`, is approved at version `1.3.0-public-source-candidate.1.none` as the observing project's
secret-classification policy. It is the version-1 policy (the Butlers scope and
the public-source scope, byte-identical) plus one change inside
`publicSourceScope`: the RFC5-14 class `project-documentation` is classified by
the closed path rule of the variant chosen (root documents, the docs and doc
trees minus the withheld words, and the licenses tree), with the opt-in root
names neither MANIFESTO nor ARCHITECTURE withheld. The class
is classified only while the in-force RFC-0005 vocabulary lists it; every
detector and the active-content rule apply unchanged to every admitted body;
`work-history` is never classified; and policy and governance text is withheld
by name only, as the package's generated lists state. `policyVersion` is the
only existing value that changes besides that scope.

## What this act does not authorize

This act is the policy authority the public-source scope needs and satisfies
only its own. It names no repository and grants no observation consent, no
read, no egress and no provider call: each takes its own act
(REQ-polaris-generation-025), and a consent that does not list
`project-documentation` still permits no egress of it (RFC5-14). The Butlers
read gate refuses a policy on its digest first, so it keeps refusing this one
until the install change re-points the gate once, against these bytes; the
recorder does not do that. It grants no write, execution, deployment, release,
recovery, mission, autonomous or multi-user authority, widens no consent, edits
no performed record, accepts no candidate contract and amends no doctrine. It
proves no read, screening, parse, render or answer result. It is the only
variant act over this manifest: another variant needs a declared successor
package.
