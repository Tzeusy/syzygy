# Polaris understanding dependency-union successor — owner decision packet

> **Status:** Proposal, drafted 2026-10-02 for bead `syzygy-c51h`. It binds
> nothing until the owner performs the act below (VIS-4). It is not offered
> yet: no review has been run, and the recording prerequisites below have
> not landed. Until the act, the understanding amendment stays exactly as
> `POLARIS-UNDERSTANDING-READABILITY-SUCCESSOR-ACT.md` bound it.

The understanding amendment's generated `GOVERNING-DEPENDENCIES.md` is
meant to be the union of its specification's warrants blocks. It is
missing one identifier. The 2026-09-28 tree-form amendment added `CC-REV-8`
to the policies warrants of REQ-polaris-generation-004, but the union still
lists `CC-SPEC-2, CC-SPEC-4`. The file is a signed subject, so it cannot
simply be regenerated. This package proposes the regenerated union as a
successor to that one file.

## What you are asked to decide

Whether to sign off the regenerated union, in one act. To sign off, write
exactly:

```text
SIGN OFF POLARIS UNDERSTANDING DEPENDENCY UNION SUCCESSOR: 9c01c82d482aa79a5342ec650e7c284e4c90a900e38ea8166c8f7708599b34c8
```

The argument is the sha256 of [`SUCCESSOR-MANIFEST.txt`](SUCCESSOR-MANIFEST.txt).
Its one row names the union's digest after sign-off. If you say nothing,
the current bytes stay in force.

## What changes

- **`GOVERNING-DEPENDENCIES.md`.** In the policies section,
  `CC-SPEC-2, CC-SPEC-4` becomes `CC-REV-8, CC-SPEC-2, CC-SPEC-4`. No other
  byte changes. To read the change:
  `python3 scripts/readability_successor.py --package .syzygy/governance/contracts/candidates/polaris-understanding-dependency-union-successor --diff`.
- **Unchanged:** the specification, `proposal.md`, `design.md`,
  `COVERAGE.md`, `SYNTHESIS-MAP.json`, `tasks.md`, `.openspec.yaml`, and the
  base generator change and its union. Every requirement, scenario and
  warrant block keeps its bytes.

**Change class: Editorial.** This is a claim the review should test, not an
exemption. The file says it is "review routing, not authority, new
permission or proof of semantic coverage". The regeneration brings a
derived artifact back in line with sources that have not changed. No
obligation is added, removed or moved. `CC-REV-8` already binds
REQ-polaris-generation-004 through its own warrants block. The union only
stops under-reporting it.

## Signing path

This is a phrase-and-digest act, recorded by `scripts/readability_successor.py`,
the tool that recorded the readability successor it supersedes for this
file. Version-tag sign-off does not apply here.
`decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md` covers
"the PWB specification deltas, the observer registry entry and the contract
successors queued behind them". A Polaris generation amendment file is none
of these.

## Read gate

None. [Observed] No code under `packages/` or `apps/` reads this file. The
body-read gate (PWB-REQ-005) evaluates only consent, the secret policy and
the observer registry entry. No Butlers read and no Polaris generation
behaviour changes.

## Evidence that the regeneration is exact

`scripts/build_polaris_dependency_unions.py`, new with this package,
regenerates both Polaris unions from their specifications' warrants
blocks:

- [Observed] Its renderer reproduces the signed base union byte for byte.
- [Observed] It reproduces the signed understanding union byte for byte
  once `CC-REV-8` is removed from the specification's text.
- `--check` requires the base union to equal its regeneration, and the
  understanding union either to equal its regeneration or, while this
  package is unperformed, to be its signed predecessor with this package
  proposing the regeneration.
- `--selftest` covers 15 fixtures.

`scripts/check_spec_reconciliation.py` R7 cross-checks the same union with
an independent parser. Its selftest case `union-after-successor-act`
requires R7 to report zero findings over the proposed bytes.

## Before this can be recorded

The act cannot be recorded cleanly until these land, each with its own
review. Rehearsal on 2026-10-02: a scratch copy, a placeholder raw,
`--record`, then the battery's affected checks.

1. **Chained successors in the successor tool.** [Observed]
   `readability_successor.py --all --check` then fails for
   `polaris-understanding-readability-successor`, because its row for this
   file no longer matches the tree. The tool must accept a performed
   package whose row was replaced by a later performed package, where the
   later package's predecessor for that subject is exactly the earlier row.
2. **The understanding adoption recorder follows the chain.** [Observed]
   `record_polaris_understanding_adoption.py --check` then fails ("current
   subject drift" on `design.md`), because a package that fails its check
   contributes no successor rows. It must compose adopted → readability →
   this successor instead of treating two claims as contested. It runs the
   successor tool only at a pinned digest (`SUCCESSOR_TOOL_SHA`), and its
   own comment says a tool change "needs a new pin here, and so a new
   history review". Item 1 therefore carries that review. [Unknown] Whether
   further failures sit behind the first one it reports.
3. **The reconciliation is re-derived.** [Observed]
   `check_spec_reconciliation.py` R2 then fails for the understanding
   child, by its own design ("a later act over any subject fails R2 by
   design"). The re-derivation names this act as the understanding union's
   terminal record.
4. **Battery.** `build_polaris_dependency_unions.py --check` and
   `--selftest` join the battery, the hosted workflow and the CG-26 count
   sentence in one integration edit. This draft leaves all three alone.

When those are in, `SUCCESSOR.json`'s pins name the confirming raw and the
reviewed manifest digest, and the phrase above is offered.

## What signing does

`scripts/readability_successor.py --record` writes the act record and its
section in the acceptance record, then installs the regenerated union. Its
`--check` then verifies the file against its row. After that, R7 reports 0
findings. The act widens no implementation authority and grants no project,
source, provider, write, deployment or release permission.
