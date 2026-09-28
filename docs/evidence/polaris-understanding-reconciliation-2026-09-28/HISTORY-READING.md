# Reading the reconciliation's frozen inputs as history

The reconciliation review froze thirteen inputs at C1. Two of them move on
lawfully after C3: CC-SPEC takes owner-adopted successors, and the recorder
itself changed to read CC-SPEC that way. The recorder therefore reads both, as
it already read the status pages and the governance checker, at C1.

- **Owner ruling.** "R1: read as history", recorded in
  [`OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md`](../../../.syzygy/governance/decisions/OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md).
- **What stays checked.**
  - Every C1 input still hashes, at C1, to the digest the confirming review
    bound (`REVIEW-RAW.md`).
  - The C1 CC-SPEC digest must appear in the acceptance record as a
    `CONFIRM CRAFT AMENDMENT: CC-SPEC@<digest>` line, so the review stays
    bound to CC-SPEC bytes a performed act confirmed.
  - The other inputs, and every subject, are still compared against today's
    bytes.
- **What binds the recorder now.** Its current bytes must equal the digest
  that the latest retained `HISTORY-REVIEW-<n>-RAW.md` in this directory binds.
  - That raw carries exactly one `Verdict:` header, `CONFIRM` or
    `CONFIRM WITH EXCEPTIONS`.
  - It carries exactly one line
    `` - `scripts/record_polaris_understanding_adoption.py`: `<sha256>` ``.
  - Every history review is retained: its introducing commit holds the same
    bytes. A later change to the recorder needs a new, higher-numbered raw;
    earlier raws stay unchanged.
- **Rule-6 evidence.** [`history-reading-rule6.json`](history-reading-rule6.json)
  records each guard's mutant, its fragments and the commit it ran at; each
  one fails the selftest.
