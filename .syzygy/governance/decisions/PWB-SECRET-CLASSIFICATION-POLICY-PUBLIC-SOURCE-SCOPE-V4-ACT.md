# Owner act — Polaris Butlers secret-classification policy approval (public-source screening scope, version 4)

Date: 2026-10-20

Recorded at (UTC): 2026-10-20T13:41:25Z

Owner: Tzeusy

Act identity: `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V4-APPROVAL-2026-10-20`

Act type: `approve-policy`

Project identity: `project:syzygy`

Artifact identity: `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`

Exact digest (SHA-256): `1f2836fa8379ff83a0651338448c39b66b318d36976525277425ece6ca3a83bb`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by the owner's option selection recorded below

Supersession / revocation: this act supersedes, for the `approve-policy` role only, the 2026-10-08 act recorded at `.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V3-ACT.md`. That is the version-3 screening-scope act. Its argument
`c13bd56c70698ccdf55fa2b0a81ed51f4b3f385848d5eccd97b8be3cfad48fce` was the policy's exact digest until this act's patch was
applied. That record, its digest, its tag and the bytes it bound remain
immutable history. This act is revoked only by a later exact owner act naming
it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the one question of the packet at `.syzygy/governance/contracts/candidates/public-source-screening-scope-v4/OWNER-DECISION-PACKET.md`,
which by design carries no digest. The package manifest has two rows, one per
variant; the owner picked exactly one. The act takes this phrase, whose
argument is the chosen row:

```text
APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY: 1f2836fa8379ff83a0651338448c39b66b318d36976525277425ece6ca3a83bb
```

The owner did not type the phrase. On 2026-10-20 the owner answered a structured
question in the Claude Code CLI that opened "Screening scope v4 (P-110) cleared round 4 (CONFIRM WITH EXCEPTIONS, 5 notes, none revise). In project-documentation files it withholds only the lines a credential matches, plus one line either side, instead of the whole file; code and config stay whole-file. Any key header anywhere withholds the whole file. Known cost, stated in the packet: credential formats no detector matches (e.g. Django SECRET_KEY, JSON "password", sk_live_/AIza/github_pat_ keys, Bearer headers, postgres:// passwords) reach the review packet when they appear in a documentation file. Sign it?" by selecting the
option below. The label and description, verbatim:

| Label | Description |
|---|---|
| "Sign, variant span-guides (Rec.)" | "Line redaction plus a fixed list of root guide names (INSTALL, BUILDING, HACKING, USAGE… with .md/.rst/.txt) read as documentation." |

The packet maps that option to its words "Sign screening scope version 4, variant span-guides"; the selection is the
instruction, and the words name the variant and the manifest row.

Chosen variant: `span-guides`.

The argument was read from the chosen row of `.syzygy/governance/contracts/candidates/public-source-screening-scope-v4/PUBLIC-SOURCE-SCREENING-SCOPE-V4-MANIFEST.txt`,
re-derived from the builder's proposed bytes for that variant at recording,
and, after the variant's patch was applied in the same change, matched the
policy on disk. A swapped argument would have been refused: the recorder
rejects an argument that is not a row.

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
`project:syzygy`, is approved at version `1.5.0-public-source-candidate.1.none.code-all.redact-span-guides` as the observing project's
secret-classification policy. It is the version-3 policy plus one change inside
`publicSourceScope`, the new object `secretRedaction` (with the `detectors`
and `inheritedRules` sentences amended to name it). A body the scope classifies
project-documentation (`redactedClasses`; code-content and every other class
stay excluded whole on any match) is retained as RFC5-17 `redacted-span` when
every detector match in it is from `credential-assignment` or
`credential-bearing-url`. Matches are counted from every start offset,
overlapping ones included, and a match may span lines. The lines a match
touches, and one guard line on each side, are withheld. A cited span that
includes a withheld line is withheld whole, and its claim stays Unknown. Every
detector runs again over what is retained, and any match there excludes the
body whole. The body is still excluded whole on a `private-key-material` or
`known-token-formats` match, on any line that begins with four or more `-` and
then BEGIN (`wholeArtifactLinePattern`), and on `-----BEGIN `, `---- BEGIN ` or
a base64 form of such a header anywhere in the body (`wholeArtifactFragments`).

Variant `span-guides` also widens the project-documentation root-document
rule: a root file whose name is one of 23 guide stems
(`rootGuideStems`, among them INSTALL, BUILDING, HACKING, USAGE, TUTORIAL,
OVERVIEW, GETTING-STARTED, UPGRADING, MIGRATION, TROUBLESHOOTING, SUPPORT,
CONTRIBUTORS and CREDITS) with a `.md`, `.rst` or `.txt`
suffix (`rootGuideSuffixes`) is classed project documentation. A guide name
without one of those suffixes is not.

`policyVersion` is the only other value that changes. The cost the packet
states stands with the act: a secret no detector matches, in a documentation
file where another line matched, reaches the review packet unless it sits on a
withheld line (the packet and `ROUND-4-DISPOSITIONS.md` name the common shapes).

## What this act does not authorize

This act is the policy authority the public-source scope needs and satisfies
only its own. It names no repository and grants no observation consent, no
read, no egress and no provider call: each takes its own act
(REQ-polaris-generation-025), and the redaction changes no detector, egress or
consent rule. The read gates refuse a policy on its digest first, so they keep
refusing this one until the install change re-points them once, against these
bytes; the recorder does not do that, and the screens retain nothing new until
the install change teaches them the redaction (`IMPACT-LEDGER.md`). It grants no write, execution,
deployment, release, recovery, mission, autonomous or multi-user authority,
widens no consent, edits no performed record, accepts no candidate contract
and amends no doctrine or specification. It proves no read, screening, parse,
render or answer result. It is the only variant act over this manifest.
