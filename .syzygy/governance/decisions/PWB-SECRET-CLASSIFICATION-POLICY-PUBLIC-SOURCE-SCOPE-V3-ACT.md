# Owner act — Polaris Butlers secret-classification policy approval (public-source screening scope, version 3)

Date: 2026-10-08

Recorded at (UTC): 2026-10-08T16:24:27Z

Owner: Tzeusy

Act identity: `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V3-APPROVAL-2026-10-08`

Act type: `approve-policy`

Project identity: `project:syzygy`

Artifact identity: `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`

Exact digest (SHA-256): `c13bd56c70698ccdf55fa2b0a81ed51f4b3f385848d5eccd97b8be3cfad48fce`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by the owner's option selection recorded below

Supersession / revocation: this act supersedes, for the `approve-policy` role only, the 2026-10-07 act recorded at `.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-ACT.md`. That is the version-2 screening-scope act. Its argument
`98a87f818e0c60ca11f808f9122bbd4b1df1ad72a29f85eb81b879fd644d3f49` was the policy's exact digest until this act's patch was
applied. That record, its digest, its tag and the bytes it bound remain
immutable history. This act is revoked only by a later exact owner act naming
it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented decision 1 of the packet at `.syzygy/governance/decisions/DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md`,
which by design carries no digest. The package manifest has two rows, one per
variant; the owner picked exactly one. The act takes this phrase, whose
argument is the chosen row:

```text
APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY: c13bd56c70698ccdf55fa2b0a81ed51f4b3f385848d5eccd97b8be3cfad48fce
```

The owner did not type the phrase. On 2026-10-08 the owner answered a structured
question in the Claude Code CLI that opened "Decision 1 (P-105): Redis's core C files (server.c, networking.c, …) are withheld because the HTML check reads `a<b && c>d` as a tag. Screening policy v3 lets source files skip that check, but only while every page shows them as escaped text under a no-script CSP. Every secret detector still runs. Which do you choose?" by selecting the
option below. The label and description, verbatim:

| Label | Description |
|---|---|
| "Variant all (Recommended)" | "All 25 source extensions skip the HTML check. Widest: JS/PHP full of HTML strings are admitted too, protected only by escaping. Phrase: "Sign screening scope version 3, variant all"." |

The packet maps that option to its words "Sign screening scope version 3, variant all"; the selection is the
instruction, and the words name the variant and the manifest row.

Chosen variant: `all`.

The argument was read from the chosen row of `.syzygy/governance/contracts/candidates/public-source-screening-scope-v3/PUBLIC-SOURCE-SCREENING-SCOPE-V3-MANIFEST.txt`,
re-derived from the builder's proposed bytes for that variant at recording,
and, after the variant's patch was applied in the same change, matched the
policy on disk. A swapped argument would have been refused: the recorder
rejects an argument that is not a row.

Frozen provenance:

- frozen subject (package bytes): `5db1dd720338edd7963653f7e19ff727e1e99f32`;
- the manifest file hashes to `e5328701c62fa567d9f8dcc4d11c80266638b28bc368212b264514052bcec9e3` (a container digest, no act's
  argument);
- confirmation review: `docs/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V3-2-RAW.md`, verdict
  `CONFIRM WITH EXCEPTIONS`, its head bound to the manifest file's SHA-256 above; notes are dispositioned in `.syzygy/governance/contracts/candidates/public-source-screening-scope-v3/ROUND-2-DISPOSITIONS.md`; the raw names
  reviewed commit `5db1dd720338edd7963653f7e19ff727e1e99f32` [Observed — the raw's own line; binding is by
  digest]; and
- recording tag: `pwb-approve-policy-public-source-scope-v3-signed-2026-10-08`, on the commit carrying this act record.

## Effect

The policy `polaris-butlers-project-shape-secrets`, policy-owning project
`project:syzygy`, is approved at version `1.4.0-public-source-candidate.1.none.code-all` as the observing project's
secret-classification policy. It is the version-2 policy plus one change inside
`publicSourceScope`: a body the scope classifies code-content whose final path
segment ends with one of 25 exempt extensions (every one of the code-content rule's source extensions) is admitted
without the active-content scan, its success condition or the
malformed-code-context exclusion (`activeContent.codeContentExemption`). Every
detector still runs over every body; project-documentation bodies and every
other body are scanned as before; `renderRule` binds every body. The exemption
holds at a page only while the page writes the body as entity-encoded text
under an enforced Content-Security-Policy whose `default-src` is exactly
`'none'` and which carries no script-bearing directive (`renderCondition`); a
consumer that cannot confirm that scans the body as before for that page.
`policyVersion` is the only other value that changes.

## What this act does not authorize

This act is the policy authority the public-source scope needs and satisfies
only its own. It names no repository and grants no observation consent, no
read, no egress and no provider call: each takes its own act
(REQ-polaris-generation-025), and the exemption changes no egress or consent
rule. The read gates refuse a policy on its digest first, so they keep refusing
this one until the install change re-points them once, against these bytes;
the recorder does not do that, and the screens admit nothing new until the
install change teaches them the exemption. It grants no write, execution,
deployment, release, recovery, mission, autonomous or multi-user authority,
widens no consent, edits no performed record, accepts no candidate contract
and amends no doctrine or specification. It proves no read, screening, parse,
render or answer result. It is the only variant act over this manifest.
