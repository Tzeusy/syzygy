# Owner act — Polaris Butlers project-shape observer registry-entry adoption (behaviour-contract re-pin)

Date: 2026-10-02

Owner: Tzeusy

Act identity: `PWB-OBSERVER-REGISTRY-ENTRY-BEHAVIOR-CONTRACT-REPIN-2026-10-02`

Act type: `adopt-registry-entry`

Project identity: `project:syzygy`

Artifact identity: `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`

Exact digest (SHA-256): `ad9cd6769bffbb1a3ef94625c73226dec133fb7c9f1e0bc40186b09b15e165fa`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by the owner's option selection recorded below

Supersession / revocation: this act supersedes, for the `adopt-registry-entry` role only, the 2026-09-30 act recorded at `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md`.
Its argument `2356b9ed3235b3dff79caeb352803a30c446b7365a2a7ea74df302b9fa51386a` was the subject's exact digest until
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
ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY: ad9cd6769bffbb1a3ef94625c73226dec133fb7c9f1e0bc40186b09b15e165fa
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
act to its own manifest row. The argument above was read from the registry row of
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
- recording tag: `pwb-adopt-registry-entry-signed-2026-10-02`, on the commit carrying this act record.

## Effect

The re-pinned adapter-registry entry (`polaris-butlers-project-shape`,
version `1.2.0-candidate.1`, discovery version
`pwb-discovery-v2-candidate.1`) is adopted in Syzygy's governance home
`.syzygy/governance/declarations/adapter-registry` for `project:syzygy` and
the configured Butlers repository, in place of the 2026-09-30 entry, with
read-only authority and an empty write surface. Exactly two values change:
`governingBehaviorContract.version` now names the PWB `spec.md` that the
`pwb-readability-successor-v1.0` sign-off binds (the `spec.md` row of that
package's manifest), and `signedBy` names that version-tagged sign-off and
its record. The source population, observation grammar, resource envelope,
currency bounds, briefing ceiling and the absence of write, execution,
egress and second-repository capability are byte-identical to the bytes the
2026-09-30 act adopted.

## What this act does not authorize

This act is one of the three separate authorities PWB-REQ-005 requires and
satisfies only its own. It grants no observation consent, and it neither
approves nor adopts the secret-classification policy, which took its own separate act the same
day. The read gate evaluates this act only under the owner's plain
continuation direction C of the same selection, recorded at
`.syzygy/governance/decisions/OWNER-INSTRUCTIONS-2026-10-02-PWB-BEHAVIOR-CONTRACT-REPIN.md`; no implementation consumes
`governingBehaviorContract` or any other field it did not read before.

It grants no write, egress, execution, deployment, release, recovery,
mission, second-repository, autonomous or multi-user authority, widens no
consent, changes no version label, edits no performed record, accepts no
candidate contract and amends no doctrine. It proves no read, screening,
parse, render or answer result.
