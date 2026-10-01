# Owner act — PWB opening-band scenario sign-off

Date: 2026-10-01

Owner: Tzeusy

Act identity: `PWB-OPENING-BAND-SCENARIO-SIGNOFF-2026-10-01`

Project identity: `project:syzygy`

Provenance state: `owner-adopted (bootstrap, uncorrelated)`

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the independently confirmed packet at
`.syzygy/governance/contracts/candidates/pwb-opening-band-scenario/OWNER-DECISION-PACKET.md`
and performed the offered indivisible behavior amendment by writing exactly:

```text
SIGN OFF PWB OPENING-BAND SCENARIO: 7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46
```

The argument is the SHA-256 of
`.syzygy/governance/contracts/candidates/pwb-opening-band-scenario/PWB-OPENING-BAND-SCENARIO-MANIFEST.txt`.
It was recomputed at recording and matched the phrase. The manifest bytes
were verified against frozen subject `3369410d1e08366b852422a457e473e5fec64f1c`; the package's
patches were applied through its builder in the same change, and all eleven
rows were then verified to hash the tree. The presented packet bytes were
verified against the packet head. The act instant is the moment the owner
wrote the phrase, in-interaction, on 2026-10-01.

Frozen provenance:

- frozen subject (manifest and packet bytes): `3369410d1e08366b852422a457e473e5fec64f1c`;
- owner-packet head: `3369410d1e08366b852422a457e473e5fec64f1c`;
- confirmation review: `docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-CONFIRMATION-10-RAW.md`, verdict
  `CONFIRM WITH EXCEPTIONS`, bound to this manifest digest; the raw names reviewed commit
  `9162d622d67e3cba17c9691a5f19c3a8e4d2eded` [Observed — the raw's own line; binding is by digest];
- disposition record: `.syzygy/governance/contracts/candidates/pwb-opening-band-scenario/ROUND-11-DISPOSITIONS.md`, dispositioning
  the review's notes under the `CONFIRM WITH EXCEPTIONS` verdict, never by editing
  the reviewed bytes; and
- recording tag: `pwb-opening-band-scenario-signed-2026-10-01`, on the commit carrying this act record.

## Effect

PWB-REQ-010 gains one conditional scenario: if Polaris's first reading
level renders an aggregate over the Unknown project-shape claims of one
evaluation before the first capability catalog, there is exactly one such
aggregate; it displaces no project-level category; it carries the
PWB-REQ-007 label, tier and freshness with separate primary and secondary
counts and no headline status; its population and counts equal the claims
it names; every counted member stays disclosed at its own claim and
reachable from the aggregate; and the machine answer carries the same
aggregate (PWB-REQ-020, under the owner's 2026-09-26 wider reading of
"disclosure"). The aggregate quantifies over project-shape Unknowns only;
the currency probe and other region blocks are outside its population.
Nothing requires the band to be built. `GOVERNING-DEPENDENCIES.md` is
regenerated.

This act is the latest link over the eleven-artifact PWB behavior
population. Every earlier act's rows remain immutable act-time history;
none is edited, retired or re-hashed by this record.

## Signed artifacts

| Repository-relative artifact | sha256 |
|---|---|
| `openspec/changes/polaris-project-wide-butlers-model/.openspec.yaml` | `bd2504cb580ca73eeb2510481ca4665ee11e2127360fc0be12c104f347fb515f` |
| `openspec/changes/polaris-project-wide-butlers-model/CAPABILITY-COVERAGE.md` | `517d698b55425701919132163d316c3c891097d7a7058281b404e89bd05adcac` |
| `openspec/changes/polaris-project-wide-butlers-model/CONTRACT-COVERAGE-REPAIR-DELTA.md` | `77f6b685f7a92eff39d874b92ed36b99e832ded16d1970f1242b6750641b5349` |
| `openspec/changes/polaris-project-wide-butlers-model/CONTRACT-COVERAGE.md` | `ada47e4b993951873855a3055e0958bd5e0947ab51060404b0ef11eaff84c578` |
| `openspec/changes/polaris-project-wide-butlers-model/GOVERNING-DEPENDENCIES.md` | `86b1b49f28d9eb90c3cf47582ea9b8c78c55a50badd00a9717b24a779a4eba85` |
| `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0001-0003.md` | `f28404be66a4241503f2214757d640361751934b2ab308dafeada5c6d2152e50` |
| `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0004-0006.md` | `ec091e743cb95070b30980021f2b5bdf054128161a86f6f8a8bbdf7678ffbc29` |
| `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0007-0009.md` | `6e480d6b94734abd41b15fbdcab1e6d7df9d60f68f0f3f5b0d66f98462728cd0` |
| `openspec/changes/polaris-project-wide-butlers-model/design.md` | `b89fae42697810692507b5a049aa66949a04afd95d1df1783e95d910e7bfb53e` |
| `openspec/changes/polaris-project-wide-butlers-model/proposal.md` | `2054c425e02f4eaffb1a2eeec07238fe4975a8f6eb41d1bc429a4a891fb93a38` |
| `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` | `9a44bdb6573ad3136ebd0d4fb8f8922fbd512c31896014068b29b851404615ae` |

All eleven rows take effect together or none do. An edit to any listed
artifact breaks this act's digest binding and must use the amendment path.

## What this act does not authorize

This act authorizes no implementation: M4 slice 3 needs a separate
owner implementation authorization, and slices 4 and 5 stay gated on the
`syzygy-dov.26` amendment the OQ-1 answer routes them to. It describes no
write into any observed repository, widens no content class, route or
consent, and amends PWB-REQ-007, PWB-REQ-020 and POC-REQ-032 in no byte.
The registry entry and secret-classification policy, whose declared
governing-contract digest this amendment stales, are edited by no part of
it.

It approves no policy, adopts no registry entry, widens no consent, and
grants no write, egress, observed-code execution, deployment, release,
recovery, mission, second repository, wider content class, autonomous
behavior or multi-user support. It proves no read, screening, parse, render,
answer or comprehension result. It does not edit the signed parent
`three-surface-poc-experience` artifacts, accept RFC 0010 or RFC 0011, amend
doctrine, or start automatic follow-on work.
