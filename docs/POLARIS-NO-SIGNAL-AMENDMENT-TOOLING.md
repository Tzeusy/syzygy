# Checking a future Polaris no-signal amendment

This tooling supports preparation and verification of a possible contract
amendment. It does not adopt that amendment, create owner records, install new
contract text, authorize the manifesto generator, or permit provider effects.

## What the check recognizes

The prospective dedicated record is
.syzygy/governance/decisions/POLARIS-NO-SIGNAL-AMENDMENT-ACT.md.
The aggregate record remains
`.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`.
The prospective subject is
.syzygy/governance/contracts/candidates/polaris-no-signal-amendment/CONTRACT-AMENDMENT-MANIFEST.txt.
Its exact digest is the argument to the proposed label
`SIGN OFF POLARIS NO-SIGNAL CONTRACT AMENDMENT`.
Naming these locations creates no performed act or valid subject.

Each record must contain one complete bare ceremony line: the label, a colon
followed by one ASCII space, and its lowercase SHA-256 argument. Indentation,
trailing whitespace or prose, alternate spacing and backtick wrapping are not
accepted. Extra or malformed occurrences of this label are rejected,
including an attempted aggregate entry without a dedicated record.

The manifest has two digest rows, in this order, relative to the contracts home:

1. `rfcs/RFC-0008/state-vocabulary-and-cost.md`
2. `rfcs/RFC-0009/interaction-parity-and-release.md`

The same current bytes must appear at both installed and candidate locations.
The active manifest and generated views can then be regenerated normally.
Historical Wave A/B and general-bootstrap transaction manifests stay unchanged.
The amendment package and dedicated recorder must be reviewed separately before
an owner is asked to perform an act; this checker is not that recorder.

## Existing and successor behavior

Without a recorded successor, CG-7h continues to compare current contracts against
the original performed bootstrap transaction. A candidate manifest cannot change
that expectation. Unsigned contract edits still fail.

A successor must agree between dedicated and aggregate records, bind the exact
closed manifest, and preserve the valid predecessor. Only its two module paths
can take new expected digests. Every other module remains checked against the
predecessor, and all installed/candidate mirror pairs remain checked. Neither a
regenerated current manifest nor a matching label alone grants an exception.

The original predecessor records and immutable manifest identities remain part
of validation. A malformed attempted successor is a finding, not a reason to
silently accept current bytes. Existing PWB amendment-chain handling is separate
and retains its own validation.

## Verification

The existing CG-7h selftest family exercises unsigned candidates, valid
supersession and invalid record/manifest/history cases at the checker seam.
It must reject stale subjects, missing or duplicated records, broken predecessor
history, malformed or non-closed path populations, unrelated module drift, and
missing or differing mirror bytes. These checks concern record consistency;
they do not establish owner intent or product comprehension from fabricated
records.

Run `python3 scripts/check_governance.py --selftest` for the fixture suite.
Before reporting the final tooling commit as passing, run the current canonical
battery from PROJECT-STATUS.md in a fresh clone. Generated-output drift and
invalid records must be investigated, not suppressed to make that battery pass.
