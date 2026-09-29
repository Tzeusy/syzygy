# Polaris generator base readability successor — owner decision packet

> **Status:** Proposal. It binds nothing until the owner performs the act
> below (VIS-4). Until then the generator specification stays exactly as
> `POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md` bound it.

The package restyles the Polaris generator proposal and design for reading,
and replaces the proposal's pre-adoption banner with a present-tense status
naming the adoption act. The specification, tasks, every contract document
and the other bound sources are unchanged, so every REQ-polaris-generation
requirement, scenario and warrant stays byte-identical. The understanding
amendment's overlay is untouched; it has its own successor package.

## What you are asked to decide

Whether to sign off the restyled proposal and design, in one act. To sign
off, write exactly:

```text
SIGN OFF POLARIS GENERATOR BASE READABILITY SUCCESSOR: 13d45770e2a8202892ec319b9e2ba3ec4ab127d587bf86d697e4e60efdc952d3
```

The argument is the sha256 of [`SUCCESSOR-MANIFEST.txt`](SUCCESSOR-MANIFEST.txt),
whose 23 rows name each bound file's digest after sign-off. If you say
nothing, the current bytes stay in force.

## What changes

- **`proposal.md`.** A status banner naming the adoption act and the
  understanding amendment; the capability stated first; why, what changes,
  scope and applicability as shallow lists. Every claim and exclusion is
  kept.
- **`design.md`.** The design opens with its thesis and says what it is not;
  each decision becomes a short tree. The coexistence table with the PWB
  requirements is kept whole.
- **Unchanged:** the specification, `tasks.md`, `.openspec.yaml`, every
  contract document in the change, and the two `docs/design/` sources.
- **One side effect.** `scripts/polaris_generator_approval.py --check`
  compares the 2026-09-12 approval offer with today's bytes. After sign-off
  it reports the two restyled files as drifted, which is correct: the offer
  records what was approved then. It is not in the battery.

To read the change: `python3 scripts/readability_successor.py --package
.syzygy/governance/contracts/candidates/polaris-generator-base-readability-successor --diff`.

## What adopting does

`scripts/readability_successor.py --record` writes the act record and its
section in the acceptance record, then installs the two restyled files. Its
`--check` then verifies all 23 files against their rows.

It widens no implementation authority and grants no project, source,
provider, write, deployment or release permission.

## Evidence

- **Review:** pending. The tool refuses to record until a fresh review
  confirms the manifest digest.
