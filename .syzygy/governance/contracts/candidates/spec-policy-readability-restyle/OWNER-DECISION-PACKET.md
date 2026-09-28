# Specification-policy readability restyle — owner decision packet

> **Status:** Proposal. It binds nothing until the owner performs the act
> below (VIS-4). Until then CC-SPEC and CC-IMPACT stay exactly as acts 6 and
> 7 and the general trusted-bootstrap transaction bound them.

The package restyles the two in-force specification policies to CC-REV-8, the
tree style the rest of the governed estate now uses. No rule changes. Three
disclosed banner sentences change, because they are false today.

## What you are asked to decide

Whether to adopt the restyled bytes of both policies, in one act:

- `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` — CC-SPEC-1…11;
- `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` — CC-IMPACT-1…7.

To adopt, write exactly:

```text
CONFIRM SPECIFICATION POLICY READABILITY RESTYLE: 0abd08981ae693720c33c339b9d53ac2a4c42c141d0ad23be2e83e90c5cd000e
```

The argument is the sha256 of
[`SPEC-POLICY-AMENDMENT-MANIFEST.txt`](SPEC-POLICY-AMENDMENT-MANIFEST.txt),
whose two rows name each policy's restyled digest. If you say nothing, both
policies stay in force at their current bytes.

## What changes

- **Form.** Each file and section opens with its answer; rule bodies become
  shallow trees; three non-normative diagrams show the acceptance model and
  the propagation path. Every clause lead, heading and identifier is
  unchanged; the package builder checks all three.
- **Banners, disclosed as a status change.** Your 2026-09-28 answer "Fix
  banners too" folds these in:
  - Both head banners said "Candidate. Binds nothing until its own
    `CONFIRM CRAFT AMENDMENT` act." Both policies have been in force since
    2026-08-17. The banners now say so and name the acceptance record as the
    authority on which bytes are in force.
  - CC-SPEC's amendment history said CC-SPEC-8 cites five contract phase
    rules. The clause cites nine. The history now names all nine: this is
    P-66 arm (a), which you ruled rides along with the next CC-SPEC
    amendment.
  - CC-SPEC's history said the RD-69 repair "awaits its one confirming
    review". RD-70 confirmed it on 2026-08-17; the history now says so.

## What stays the same

- CC-IMPACT-7 still pins its blind-run fixture by path and digest. The pin is
  normative and is not restyled away.
- The nine open non-blocking findings from RD-69 and RD-70 stay open.
- The path, file names and titles still say "candidate". The banners say
  that too.

## What adopting does

1. The recorder writes the act record, appends it to the acceptance record,
   and appends an entry to the craft install record. It also writes one
   `CONFIRM CRAFT AMENDMENT: CC-…@<digest>` line per policy, derived from the
   manifest rows, so every existing check reads the new digests.
2. The package's patches are applied to both policies.
3. The act-6, act-7 and transaction-row digests become act-time history.
   The governance checker already knows the successor, so nothing else is
   rewritten.

It grants no implementation, source, provider, write, deployment or release
permission.

## Evidence

- **Prose reviews** of the restyle, over the drafts before the banner changes:
  - [`R-TREE-STYLE-SPEC-POLICY-1-RAW.md`](../../../../../docs/reviews/R-TREE-STYLE-SPEC-POLICY-1-RAW.md)
    — REVISE; every material finding repaired;
  - [`R-TREE-STYLE-SPEC-POLICY-2-RAW.md`](../../../../../docs/reviews/R-TREE-STYLE-SPEC-POLICY-2-RAW.md)
    — CONFIRM WITH EXCEPTIONS, notes only.
- **Package review**, over these exact bytes, the banner changes and the
  tooling: pending. The recorder refuses to record until that review
  confirms the manifest digest above.
- **Prerequisite, your ruling "R1: read as history":** the
  understanding-reconciliation recorder reads the CC-SPEC bytes it froze as
  history, so adopting this package does not retire that reconciliation
  ([`HISTORY-READING.md`](../../../../../docs/evidence/polaris-understanding-reconciliation-2026-09-28/HISTORY-READING.md)).
