# Owner act — PWB exact-source render-mode amendment sign-off

Date: 2026-10-02

Owner: Tzeusy

Act identity: `PWB-EXACT-SOURCE-RENDER-MODE-AMENDMENT-SIGNOFF-2026-10-02`

Project identity: `project:syzygy`

Provenance state: `owner-adopted (bootstrap, uncorrelated)`

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the independently confirmed packet at
`.syzygy/governance/contracts/candidates/pwb-exact-source-render-mode-scenario/OWNER-DECISION-PACKET.md`
and performed the offered indivisible behavior amendment by writing exactly:

```text
SIGN OFF PWB EXACT-SOURCE RENDER-MODE AMENDMENT: 527be5ac3732619608355ae9658c92cee45341e831521bc526398481dd915785
```

The argument is the SHA-256 of
`.syzygy/governance/contracts/candidates/pwb-exact-source-render-mode-scenario/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`.
It was recomputed at recording and matched the phrase. The manifest bytes
were verified against frozen subject `4b2f0df92676dfb89ca600c15f349070251d74bb`; the package's
patches were applied through its builder in the same change, and all eleven
rows were then verified to hash the tree. The presented packet bytes were
verified against the packet head. The act instant is the moment the owner
wrote the phrase, in-interaction, on 2026-10-02.

Frozen provenance:

- frozen subject (manifest and packet bytes): `4b2f0df92676dfb89ca600c15f349070251d74bb`;
- owner-packet head: `4b2f0df92676dfb89ca600c15f349070251d74bb`;
- confirmation review: `docs/reviews/R-PWB-EXACT-SOURCE-RENDER-MODE-DELTA-CONFIRMATION-3-RAW.md`, verdict
  `CONFIRM WITH EXCEPTIONS`, bound to this manifest digest; the raw names reviewed commit
  `99cecd84639798feb34275dd652aeb747fb55fcf` [Observed — the raw's own line; binding is by digest];
- disposition record: `.syzygy/governance/contracts/candidates/pwb-exact-source-render-mode-scenario/ROUND-3-DISPOSITIONS.md`, dispositioning
  the review's notes under the `CONFIRM WITH EXCEPTIONS` verdict, never by editing
  the reviewed bytes; and
- recording tag: `pwb-exact-source-render-mode-amendment-signed-2026-10-02`, on the commit carrying this act record.

## Effect

PWB-REQ-011 is amended so that the exact-source route serves every source
the evaluation admitted as a classified blob, in exactly one render mode
drawn from a closed two-mode set: the existing requirement-section mode for
sources with requirement headings, and a whole-body mode for the rest. A
source whose record outcome is excluded is served in no mode, as its own
invariant and scenario. Every mode applies the same authority, exact-object,
secret-detection and inert-content gates to the complete transient body
before encoding any part of it; a failed gate leaves the body Unknown with
its reason. Each served mode exposes a presentation-only scroll anchor per
reading unit a citation can name, which never enters, replaces or qualifies
any source, claim or narrative anchor identity. Each served route's mode,
each source identity and each refusal's reason are recoverable per rendered
tuple from the same evaluation in the machine answer, so the parity sweep
extends over the anchor parameter. `design.md` §8 carries the argument for
the wider source population inside the one consented content class,
`CAPABILITY-COVERAGE.md` row 10 restates the obligation, and
`GOVERNING-DEPENDENCIES.md` is regenerated.

This act is the latest link over the eleven-artifact PWB behavior
population. Every earlier act's rows remain immutable act-time history;
none is edited, retired or re-hashed by this record.

## Signed artifacts

| Repository-relative artifact | sha256 |
|---|---|
| `openspec/changes/polaris-project-wide-butlers-model/.openspec.yaml` | `bd2504cb580ca73eeb2510481ca4665ee11e2127360fc0be12c104f347fb515f` |
| `openspec/changes/polaris-project-wide-butlers-model/CAPABILITY-COVERAGE.md` | `c5b178d14dfe212913c8a1bc3836620586e3e880f3a84210fb5b2f6cc687ad92` |
| `openspec/changes/polaris-project-wide-butlers-model/CONTRACT-COVERAGE-REPAIR-DELTA.md` | `77f6b685f7a92eff39d874b92ed36b99e832ded16d1970f1242b6750641b5349` |
| `openspec/changes/polaris-project-wide-butlers-model/CONTRACT-COVERAGE.md` | `ada47e4b993951873855a3055e0958bd5e0947ab51060404b0ef11eaff84c578` |
| `openspec/changes/polaris-project-wide-butlers-model/GOVERNING-DEPENDENCIES.md` | `de3f7b8f4bdc1c792f7ca9a75c21d4447cc239e58879edc758f1783798352373` |
| `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0001-0003.md` | `f28404be66a4241503f2214757d640361751934b2ab308dafeada5c6d2152e50` |
| `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0004-0006.md` | `ec091e743cb95070b30980021f2b5bdf054128161a86f6f8a8bbdf7678ffbc29` |
| `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0007-0009.md` | `6e480d6b94734abd41b15fbdcab1e6d7df9d60f68f0f3f5b0d66f98462728cd0` |
| `openspec/changes/polaris-project-wide-butlers-model/design.md` | `de697647646873937c79f457ff1d39c41e041ede8ab3a3b8a05cb1bb5f96c270` |
| `openspec/changes/polaris-project-wide-butlers-model/proposal.md` | `2054c425e02f4eaffb1a2eeec07238fe4975a8f6eb41d1bc429a4a891fb93a38` |
| `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` | `14e01af3cdca463f2b9b30eee9a315b7f170f38516804222f89704a99f1aa740` |

All eleven rows take effect together or none do. An edit to any listed
artifact breaks this act's digest binding and must use the amendment path.

## What this act does not authorize

No content class widens: the route reads only what the performed consent
covers, and the nine withheld sources (seven TOML butler manifests, one
frontend page, one excluded artifact) stay digest-only with the source
denominator unchanged. No detector changes. PWB-REQ-014, PWB-REQ-020,
PWB-REQ-003, -005, -006 and -015 are not amended; the P-81 Q5 PWB-REQ-015
delta and the P-82 PWB-REQ-002 delta are separate changes. This act
authorizes no implementation of the amended semantics: the pursuit bead
under M14 opens only under a fresh, separate owner authorization, and the
269-of-278 figure and the page-size effect are measured there, never
assumed here.

It approves no policy, adopts no registry entry, widens no consent, and
grants no write, egress, observed-code execution, deployment, release,
recovery, mission, second repository, wider content class, autonomous
behavior or multi-user support. It proves no read, screening, parse, render,
answer or comprehension result. It does not edit the signed parent
`three-surface-poc-experience` artifacts, accept RFC 0010 or RFC 0011, amend
doctrine, or start automatic follow-on work.
