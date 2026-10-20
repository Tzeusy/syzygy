# Owner act — Polaris Butlers secret-classification policy approval (public-source screening scope, version 4)

Date: 2026-10-20

Recorded at (UTC): 2026-10-20T14:48:37Z

Owner: Tzeusy

Act identity: `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V4-APPROVAL-2026-10-20`

Act type: `approve-policy`

Project identity: `project:syzygy`

Artifact identity: `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`

Exact digest (SHA-256): `319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly given by the owner's words recorded below

Supersession / revocation: this act supersedes, for the `approve-policy` role only, the 2026-10-08 act recorded at `.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V3-ACT.md`. That is the version-3 screening-scope act. Its argument
`c13bd56c70698ccdf55fa2b0a81ed51f4b3f385848d5eccd97b8be3cfad48fce` was the policy's exact digest until this act's patch was
applied. That record, its digest, its tag and the bytes it bound remain
immutable history. This act is revoked only by a later exact owner act naming
it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the packet at `.syzygy/governance/contracts/candidates/public-source-screening-scope-v4/OWNER-DECISION-PACKET.md`, which by
design carries no digest. Its one question offers two variants and decline;
the package manifest has two rows, one per variant, and the owner named
exactly one. The act takes this phrase, whose argument is the chosen row:

```text
APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY: 319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd
```

The owner did not type the phrase. On 2026-10-20 the owner gave these words,
verbatim, in the Claude Code CLI session:

> Sign screening scope version 4, variant span

The words name the variant, and the variant names the manifest row.

Chosen variant: `span`.

The argument was read from the chosen row of `.syzygy/governance/contracts/candidates/public-source-screening-scope-v4/PUBLIC-SOURCE-SCREENING-SCOPE-V4-MANIFEST.txt`,
re-derived from the builder's proposed bytes for that variant at recording,
and, after the variant's patch was applied in the same change, matched the
policy on disk. A swapped argument would have been refused: the recorder
rejects an argument that is not a row, and words that name the other variant.

Frozen provenance:

- frozen subject (package bytes): `65edb1cbbec97384afd7b71e9c069736c89d767c`;
- the manifest file hashes to `0621d646f91ef3b5572d882f4bb17f5bd0785d316b30516693e48884365157ec` (a container digest, no act's
  argument);
- confirmation review: `docs/reviews/R-OLMR-SCREENING-SCOPE-V4-4-RAW.md`, verdict
  `CONFIRM WITH EXCEPTIONS`, its head bound to the manifest file's SHA-256 above; notes are dispositioned in `.syzygy/governance/contracts/candidates/public-source-screening-scope-v4/ROUND-4-DISPOSITIONS.md`; the raw names
  reviewed commit `65edb1cbbec97384afd7b71e9c069736c89d767c` [Observed — the raw's own line; binding is by
  digest]; and
- recording tag: `pwb-approve-policy-public-source-scope-v4-signed-2026-10-20`, on the commit carrying this act record.

## Effect

The policy `polaris-butlers-project-shape-secrets`, policy-owning project
`project:syzygy`, is approved at version `1.5.0-public-source-candidate.1.none.code-all.redact-span` as the observing project's
secret-classification policy. It is the version-3 policy plus one change inside `publicSourceScope`, the new object `secretRedaction`: a body of class `project-documentation` in which a detector matches is retained as `redacted-span` (RFC5-17) instead of excluded whole, when none of its matches is from `private-key-material`, `known-token-formats`, no line matches `wholeArtifactLinePattern` and the body holds none of the 4 `wholeArtifactFragments`. Every match from every offset counts; each line a match touches, and 1 guard line(s) on each side, is withheld; every detector runs again over the retained text and any match there excludes the body whole; a cited span that includes a withheld line is withheld whole. Every other class, code-content included, is excluded whole on any match as before, and the active-content scan is unchanged. The scope's `detectors` and `inheritedRules` sentences each name the exception once. Variant `span` leaves every content-classification rule as version 3 has it. `policyVersion` is the only other value that changes.

## What this act does not authorize

This act is the policy authority the public-source scope needs and satisfies
only its own. It names no repository and grants no observation consent, no
read, no egress and no provider call: each takes its own act
(REQ-polaris-generation-025), and the redaction changes no egress or consent
rule. The read gates refuse a policy on its digest first, so they keep refusing
this one until the install change re-points them once, against these bytes;
the recorder does not do that, and the screens redact nothing until the
install change teaches them the rule. It grants no write, execution,
deployment, release, recovery, mission, autonomous or multi-user authority,
widens no consent, edits no performed record, accepts no candidate contract
and amends no doctrine or specification. It proves no read, screening, parse,
render or answer result. It is the only variant act over this manifest.
