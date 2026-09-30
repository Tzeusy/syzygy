# Owner act — Polaris Butlers project-shape observer registry-entry adoption (currency bounds and briefing ceiling amendment)

Date: 2026-09-30

Owner: Tzeusy

Act identity: `PWB-OBSERVER-REGISTRY-ENTRY-CURRENCY-BRIEFING-AMENDMENT-2026-09-30`

Act type: `adopt-registry-entry`

Project identity: `project:syzygy`

Artifact identity: `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`

Exact digest (SHA-256): `2356b9ed3235b3dff79caeb352803a30c446b7365a2a7ea74df302b9fa51386a`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by performing the offered state-(1) phrase

Supersession / revocation: this act supersedes, for the `adopt-registry-entry` role
only, the 2026-09-05 act recorded at `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`.
Its argument `0765f4d534afad9003463790113fd433d250550091df783c1ff372d227643e4f` was the subject's exact digest until
this act's patch was applied. That record, its digest, its tag and the bytes
it bound remain immutable history. This act is revoked only by a later exact
owner act naming it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the independently confirmed packet at
`.syzygy/governance/contracts/candidates/pwb-registry-currency-briefing-amendment/OWNER-DECISION-PACKET.md`,
which by design carries no digest, and performed this one act by writing
exactly:

```text
ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY: 2356b9ed3235b3dff79caeb352803a30c446b7365a2a7ea74df302b9fa51386a
```

The argument is the SHA-256 of the artifact itself. It was recomputed at
recording from the package's proposed bytes, matched the single row of
`.syzygy/governance/contracts/candidates/pwb-registry-currency-briefing-amendment/PWB-EFFECT-AMENDMENT-MANIFEST.txt`,
and, after the package's patch was applied through its builder in the same
change, matched the artifact on disk. The act instant is the moment the
owner wrote the phrase, in-interaction, on 2026-09-30.

Frozen provenance:

- frozen subject (package bytes): `4b59e39f501bae2a7ffbbe9dad5c76df2a8f85e5`;
- owner-packet head: `4b59e39f501bae2a7ffbbe9dad5c76df2a8f85e5`;
- effect manifest SHA-256: `df174263c462db92001ea629116df9d51e2f7679db7676c3c5b29601081b4b13`;
- confirmation review: `docs/reviews/R-PWB-REGISTRY-CURRENCY-BRIEFING-DELTA-CONFIRMATION-3-RAW.md`, verdict
  `CONFIRM`, its head bound to the argument above (the manifest row, which
  the raw re-derived by script); the raw names reviewed commit
  `79c2101fa8944d368d7bf588c0106dab98ce4b41` [Observed — the raw's own line; binding is by digest]; and
- recording tag: `pwb-adopt-registry-entry-signed-2026-09-30`, on the commit carrying this act record.

## Effect

The amended adapter-registry entry (`polaris-butlers-project-shape`,
version `1.2.0-candidate.1`, discovery version
`pwb-discovery-v2-candidate.1`) is adopted in Syzygy's governance home
`.syzygy/governance/declarations/adapter-registry` for `project:syzygy` and
the configured Butlers repository, in place of the 2026-09-05 entry
(version `1.1.0-candidate.1`), with read-only authority and an empty
write surface. It keeps the signed PWB source population, the policy that
screens it, the closed observation grammar, the deterministic resource
envelope and the absence of write, execution, egress and second-repository
capability, and adds two declarations the owner chose value by value:
13 explicit per-class currency bounds under one
closed semantics block (P-69 question 2, arm (a)), under which an
undeclared class remains Unknown and an out-of-bound assessment is a typed
result, never a guess; and one further response ceiling,
`maxBriefingResponseBytes` (P-72 question 2), which bounds a
single-subject view built from an already-served evaluation and serves
bounded typed failure, never truncated success. The entry is a declared
mapping: adopting it changes no code and authorizes none to be written.

## What this act does not authorize

This act is one of the three separate authorities PWB-REQ-005 requires and
satisfies only its own. It grants no observation consent and approves no
secret-classification policy. No implementation consumes the new fields
until the owner issues the separate plain continuation direction the
ruling record names, and no briefing route is served before the derived
read-only machine-view specification is signed off and its ceiling is
declared. It leaves the entry's `status` and `adoptionStatus` keys, which
carry its governance lifecycle, byte-identical.

It grants no write, egress, execution, deployment, release, recovery,
mission, second-repository, autonomous or multi-user authority, widens no
consent, edits no signed artifact, accepts no candidate contract and amends
no doctrine. It proves no read, screening, parse, render or answer result.
