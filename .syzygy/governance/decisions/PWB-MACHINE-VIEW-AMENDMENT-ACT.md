# Owner act — PWB machine-view amendment sign-off

Date: 2026-10-02

Owner: Tzeusy

Act identity: `PWB-MACHINE-VIEW-AMENDMENT-SIGNOFF-2026-10-02`

Project identity: `project:syzygy`

Provenance state: `owner-adopted (bootstrap, uncorrelated)`

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the independently confirmed packet at
`.syzygy/governance/contracts/candidates/pwb-machine-view-amendment/OWNER-DECISION-PACKET.md`
and performed the offered indivisible behavior amendment by writing exactly:

```text
SIGN OFF PWB MACHINE-VIEW AMENDMENT: acabc7915e4461186b5878ce40cc0c62ed7cf91eadd7eead1cb179c80f672e72
```

The argument is the SHA-256 of
`.syzygy/governance/contracts/candidates/pwb-machine-view-amendment/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`.
It was recomputed at recording and matched the phrase. The manifest bytes
were verified against frozen subject `e58fd1cd1021734a6a617e87424ad3b531c3a61c`; the package's
patches were applied through its builder in the same change, and all eleven
rows were then verified to hash the tree. The presented packet bytes were
verified against the packet head. The act instant is the moment the owner
wrote the phrase, in-interaction, on 2026-10-02.

Frozen provenance:

- frozen subject (manifest and packet bytes): `e58fd1cd1021734a6a617e87424ad3b531c3a61c`;
- owner-packet head: `e58fd1cd1021734a6a617e87424ad3b531c3a61c`;
- confirmation review: `docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-6-RAW.md`, verdict
  `CONFIRM WITH EXCEPTIONS`, bound to this manifest digest; the raw names reviewed commit
  `e58fd1cd1021734a6a617e87424ad3b531c3a61c` [Observed — the raw's own line; binding is by digest];
- disposition record: `.syzygy/governance/contracts/candidates/pwb-machine-view-amendment/ROUND-7-DISPOSITIONS.md`, dispositioning
  the review's notes under the `CONFIRM WITH EXCEPTIONS` verdict, never by editing
  the reviewed bytes; and
- recording tag: `pwb-machine-view-amendment-signed-2026-10-02`, on the commit carrying this act record.

## Effect

PWB-REQ-020 gains one block, inside the requirement and before its SHALL
sentence, that names two closed categories of machine response served beside
the machine answer: the derived read-only machine view, whose members are
`GET /api/poc/polaris` and the prospective `GET /api/poc/briefing`, and the
generated editorial draft view, whose member is `GET /polaris/draft/<runId>`.
Every value a derived view serves is independently verified as derivable from
the machine answer's own bytes. A member that needs a ceiling of its own is
not served before the adapter-registry entry's resource envelope declares it.
A route enters either category only by a later amendment to this specification
naming it, and a route in neither category is neither admitted nor forbidden
by this requirement. The narrow reading of RFC6-21 is taken.
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
| `openspec/changes/polaris-project-wide-butlers-model/GOVERNING-DEPENDENCIES.md` | `992a4aabf8df4054af7c7750e2b3e941b066b67c172cd7d2dca56d7aa5a484db` |
| `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0001-0003.md` | `f28404be66a4241503f2214757d640361751934b2ab308dafeada5c6d2152e50` |
| `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0004-0006.md` | `ec091e743cb95070b30980021f2b5bdf054128161a86f6f8a8bbdf7678ffbc29` |
| `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0007-0009.md` | `6e480d6b94734abd41b15fbdcab1e6d7df9d60f68f0f3f5b0d66f98462728cd0` |
| `openspec/changes/polaris-project-wide-butlers-model/design.md` | `de697647646873937c79f457ff1d39c41e041ede8ab3a3b8a05cb1bb5f96c270` |
| `openspec/changes/polaris-project-wide-butlers-model/proposal.md` | `2054c425e02f4eaffb1a2eeec07238fe4975a8f6eb41d1bc429a4a891fb93a38` |
| `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` | `fe9afdb52cd03ffb79b370f09e7304fcaae68e24813ab97e9e2c68c369ff21e1` |

All eleven rows take effect together or none do. An edit to any listed
artifact breaks this act's digest binding and must use the amendment path.

## What this act does not authorize

This act authorizes no implementation: no route is built or served, and the
briefing member stays unservable until its ceiling is declared and the route
is separately authorized. It amends no byte of PWB-REQ-004, -011, -014 or
-016, widens no content class, consent, read, write or egress, and edits no
registry or policy byte. The second category's record-level fields and its
relation to the exact-source anchors are left to the later route amendment
that names the member.

It approves no policy, adopts no registry entry, widens no consent, and
grants no write, egress, observed-code execution, deployment, release,
recovery, mission, second repository, wider content class, autonomous
behavior or multi-user support. It proves no read, screening, parse, render,
answer or comprehension result. It does not edit the signed parent
`three-surface-poc-experience` artifacts, accept RFC 0010 or RFC 0011, amend
doctrine, or start automatic follow-on work.
