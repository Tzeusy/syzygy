# Polaris understanding readability successor — owner decision packet

> **Status:** Proposal. It binds nothing until the owner performs the act
> below (VIS-4). Until then the understanding amendment stays exactly as
> `POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md` and the tree-form
> amendment bound it.

The package restyles the understanding amendment's proposal and design for
reading, and replaces the proposal's pre-adoption banner with a present-tense
status naming the adoption act and the tree-form amendment. The amendment's
specification, coverage, synthesis map and tasks are unchanged, so every
modified and added requirement stays byte-identical.

## What you are asked to decide

Whether to sign off the restyled proposal and design, in one act. To sign
off, write exactly:

```text
SIGN OFF POLARIS UNDERSTANDING READABILITY SUCCESSOR: 2bd0892a2d6b7ca09cfc06dd4325a1bc3cd3706852a08963836b17bd2c5d3b98
```

The argument is the sha256 of [`SUCCESSOR-MANIFEST.txt`](SUCCESSOR-MANIFEST.txt),
whose eight rows name each amendment file's digest after sign-off. If you say
nothing, the current bytes stay in force.

## What changes

- **`proposal.md`.** A status banner naming both acts; the amendment's thesis
  stated first — investigate, ask the owner, then argue the purpose; scope and
  exclusions as shallow lists. Every claim is kept.
- **`design.md`.** A new opening sentence states the design's thesis —
  supported understanding before writing, with review sending defects back
  to the step that caused them — and the placement section becomes a short
  tree. The other five sections are unchanged.
- **Unchanged:** `specs/…/spec.md`, `COVERAGE.md`, `GOVERNING-DEPENDENCIES.md`,
  `SYNTHESIS-MAP.json`, `tasks.md`, `.openspec.yaml`, and the base generator
  change.
- **Recorder support, needed before recording.**
  `scripts/record_polaris_understanding_adoption.py` checks the adopted bytes
  of all eight files, so installing the restyle would fail its `--check`. A
  follow-up recorder change lets a file equal a performed readability
  successor's row, but only when that successor's recorded predecessor is
  exactly the adopted digest. It carries its own history review, and the act
  is not recorded until it lands.

To read the change: `python3 scripts/readability_successor.py --package
.syzygy/governance/contracts/candidates/polaris-understanding-readability-successor --diff`.

## What adopting does

`scripts/readability_successor.py --record` writes the act record and its
section in the acceptance record, then installs the two restyled files. Its
`--check` then verifies all eight files against their rows.

It widens no implementation authority and grants no project, source,
provider, write, deployment or release permission.

## Evidence

- **Review 1**
  ([`R-POLARIS-UNDERSTANDING-READABILITY-SUCCESSOR-1-RAW.md`](../../../../../docs/reviews/R-POLARIS-UNDERSTANDING-READABILITY-SUCCESSOR-1-RAW.md)):
  `REVISE` — one false packet sentence and one dropped "must", both
  repaired.
- **Review 2**
  ([`R-POLARIS-UNDERSTANDING-READABILITY-SUCCESSOR-2-RAW.md`](../../../../../docs/reviews/R-POLARIS-UNDERSTANDING-READABILITY-SUCCESSOR-2-RAW.md)):
  `CONFIRM WITH EXCEPTIONS` over the manifest digest above, notes only; the
  notes and their dispositions are in [`REVIEW-NOTES.md`](REVIEW-NOTES.md).
  The package is pinned to that review.
