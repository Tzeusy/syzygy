# Owner instructions — the PWB behaviour-contract re-pin, 2026-10-02

Date: 2026-10-02

Owner: Tzeusy

Decision ID: `OWNER-INSTRUCTIONS-PWB-BEHAVIOR-CONTRACT-REPIN-2026-10-02`

This record states how the owner gave the two digest-bound re-pin acts and
the plain continuation direction C that went with them. It performs no act,
binds no digest and edits no act record. Each act record keeps its own
bytes, and `scripts/record_pwb_behavior_contract_repin_acts.py` regenerates
them exactly.

## What the owner was asked, and what the owner selected

On 2026-10-02 the owner answered one structured question in the Claude Code
CLI. The question opened with "Perform the PWB behaviour-contract re-pin?".
The rest of its text was not relayed to the recording session, so it is not
reproduced here [Unknown beyond these words and the parenthetical below].

The option the owner selected, with its description as shown:

| Label | Description |
|---|---|
| "A + B + C now (Recommended)" | "Perform both acts at the manifest rows and give direction C; I write the recorder, record both acts and re-point the gate in one change, so reads keep working." |

A, B and C are the three items of the package's owner packet
(`contracts/candidates/pwb-behavior-contract-repin/OWNER-DECISION-PACKET.md`,
"The three things the owner would be asked for"): A, the `approve-policy`
act over the re-pinned secret-classification policy; B, the
`adopt-registry-entry` act over the re-pinned observer registry entry; and
C, the read-gate direction below. The owner did not type either act phrase.
The selection is the instruction.

## The garbled parenthetical, disclosed

[Observed] The question text carried this parenthetical, verbatim:

> (policy ad9cd6… is the registry row; 66cd41… is the policy row)

Its first word can be read as pairing the policy with the registry row's
prefix. The rest of it states the pairing the manifest carries: the row
beginning `ad9cd6` is the registry entry's, and the row beginning `66cd41`
is the policy's. The parenthetical is not what binds. The selected option
says "Perform both acts at the manifest rows", so each act's argument is
that subject's row of
`contracts/candidates/pwb-behavior-contract-repin/PWB-EFFECT-REPIN-MANIFEST.txt`
at the reviewed commit `140874b7364266475dd8980be480e2783e0d8e72`. The
recorder re-derived both rows from the builder's proposed bytes before
applying anything, and it refuses an argument that is not the named
subject's own row, so a swapped argument could not have been recorded.

Acts recorded from that selection, each with its own record, aggregate
section and recording tag:

- A — `PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md`,
  superseding `PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md` for the
  `approve-policy` role only; tag `pwb-approve-policy-signed-2026-10-02`.
- B — `PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md`, superseding
  `PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md` for the
  `adopt-registry-entry` role only; tag
  `pwb-adopt-registry-entry-signed-2026-10-02`.

The confirming review is `docs/reviews/R-PWB-BEHAVIOR-CONTRACT-REPIN-RAW.md`
(`CONFIRM WITH EXCEPTIONS`, two findings, both notes), dispositioned in
`contracts/candidates/pwb-behavior-contract-repin/ROUND-1-DISPOSITIONS.md`.
Under the 2026-09-26 sitting ruling a notes-only round clears the bytes it
read.

## Direction C — the read-gate re-point

The packet put direction C in the shape of the 2026-09-30 re-point
(`OWNER-INSTRUCTIONS-2026-09-29-30-READABILITY-AND-REGISTRY.md`), as
follows:

> Adopting the re-pinned registry entry and policy makes the Butlers read
> gate fail closed, because it still expects the 2026-09-30 registry act
> and the 2026-09-05 policy act. Do you direct the implementation to
> evaluate the two new acts instead? This covers only the act pointers,
> act identities, recording tags, supersession targets and tests. No new
> field is consumed.

The owner gave it by the same selection ("give direction C").

### The direction, as issued

A plain owner direction. It binds no digest, needs no manifest or
recorder, and adds no row to `ACCEPTANCE-ACT-RECORD.md`.

- **Permitted:** for the policy and registry roles, the body-read
  expectations name the new act records, act identities and recording
  tags. The records they supersede become the expected supersession
  targets: `PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md` and
  `PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md`. Tests change
  to match.
- **Unchanged:** the version anchors (`1.2.0-candidate.1`,
  `1.1.0-candidate.1`), consent, content class, configured repository,
  every exclusion of the acts in force, and the 2026-09-30 direction's bar
  on reading the currency and briefing fields.
- **Not permitted:** consuming `governingBehaviorContract` or any other
  field the implementation does not read today.

The re-point lands in the same change as the two act records
(`apps/three-surface-poc/src/governance-inputs.ts` and its tests), so
there is no interval in which the gate expects acts the tree no longer
binds.

## What this record does not do

It does not edit, re-date or supersede any act record, and it does not
change what any act bound. It grants no observation consent and no write,
egress, execution, deployment, release, recovery, mission,
second-repository, autonomous or multi-user authority.
