# Capability 1 readability successor — owner decision packet

> **PERFORMED 2026-09-29.** The owner signed off this package; the act record is
> [`CAPABILITY-1-READABILITY-SUCCESSOR-ACT.md`](../../../decisions/CAPABILITY-1-READABILITY-SUCCESSOR-ACT.md).
> The banner below is the one the packet was offered with.

> **Status:** Proposal. It binds nothing until the owner performs the act
> below (VIS-4). Until then the Capability 1 specification stays exactly as
> `CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md` and the general
> trusted-bootstrap transaction bound it.

The package restyles the Capability 1 proposal and design for reading, and
replaces the proposal's opening banner. That banner still says "Candidate
specification … until that act, this change binds nothing", which has been
false since the adoption act; a successor is the only lawful way to correct
bound bytes. The specification, both coverage tables and the generated
dependencies are unchanged, so every CAP1-REQ, scenario and warrant stays
byte-identical.

## What you are asked to decide

Whether to sign off the restyled proposal and design, in one act. To sign
off, write exactly:

```text
SIGN OFF CAPABILITY 1 READABILITY SUCCESSOR: 10db138947497200ad7c788ce4719ba515c61832e3138f1af42201ec84a8870d
```

The argument is the sha256 of [`SUCCESSOR-MANIFEST.txt`](SUCCESSOR-MANIFEST.txt),
whose seven rows name each signed file's digest after sign-off. If you say
nothing, the current bytes stay in force.

## What changes

- **`proposal.md`.** A present-tense status banner naming the adoption act;
  the capability stated first; scope, non-goals, outcomes and Unknowns as
  shallow lists. Every claim is kept. "Impact" also names the separate
  implementation authorization, beside the non-goal that the specification
  itself authorizes nothing to be built.
- **`design.md`.** The design opens by saying what it is and points to the
  implementation plan; each decision (D1–D5) becomes a short tree. Every
  decision and trade-off is kept.
- **Unchanged:** `specs/…/spec.md`, `CAPABILITY-COVERAGE.md`,
  `CONTRACT-COVERAGE.md`, `GOVERNING-DEPENDENCIES.md` and `.openspec.yaml`.
- **One side effect.** The consent candidate `cap1-trusted-bootstrap-consent`
  (untracked, in the root working tree since 2026-09-14) would replace
  CAP1-REQ-011 and part of 046. It touches none of the files this act
  changes, but its `BASELINE.json` pins the current `proposal.md` and
  `design.md` digests. After sign-off, that baseline must be regenerated
  before the candidate goes to review.

To read the change: `python3 scripts/readability_successor.py --package
.syzygy/governance/contracts/candidates/capability-1-readability-successor --diff`.

## What adopting does

`scripts/readability_successor.py --record` writes the act record and its
section in the acceptance record, then installs the two restyled files. Its
`--check` then verifies all seven files against their rows.

It widens no implementation authority and grants no source, provider, write,
deployment or release permission.

## Evidence

- **Review 1**
  ([`R-CAP1-READABILITY-SUCCESSOR-1-RAW.md`](../../../../../docs/reviews/R-CAP1-READABILITY-SUCCESSOR-1-RAW.md)):
  `REVISE` — two dropped claims and one false packet claim, all repaired.
- **Review 2**
  ([`R-CAP1-READABILITY-SUCCESSOR-2-RAW.md`](../../../../../docs/reviews/R-CAP1-READABILITY-SUCCESSOR-2-RAW.md)):
  `CONFIRM WITH EXCEPTIONS` over the manifest digest above, notes only; the
  notes and their dispositions are in [`REVIEW-NOTES.md`](REVIEW-NOTES.md).
  The package is pinned to that review.
- **Read-only check:** `python3 scripts/readability_successor.py --package
  .syzygy/governance/contracts/candidates/capability-1-readability-successor --check`.
