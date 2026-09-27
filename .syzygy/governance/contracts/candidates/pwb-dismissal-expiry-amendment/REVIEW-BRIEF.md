# Review brief — dismissal with a live expiry (PWB-REQ-007)

> **Candidate — binds nothing.** This commissions an independent review; it
> carries no verdict and performs no act. The reviewer must not receive the
> drafting conversation or a desired verdict.

**Round 2 is a confirmation round.** Round 1 returned REVISE over
`9b18409` (pre-rebase); its raw is
`docs/reviews/R-DOV29-DISMISSAL-EXPIRY-DELTA-RAW.md`, and every finding is
dispositioned in the review record at the end of `OWNER-DECISION-PACKET.md`.
The round-2 reviewer checks each disposition against the raw and the current
bytes, then applies the criteria below afresh.

## Exact review inputs

Give the fresh reviewer only:

- this package in full: `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`,
  `OWNER-DECISION-PACKET.md`, this brief, the eleven-row manifest and all six
  `proposed/*.patch` files;
- `scripts/build_pwb_dismissal_expiry_amendment.py` and the matching
  registration diff in `scripts/check_governance.py`;
- the round-1 raw named above;
- the signed PWB eleven-artifact subject;
- PWB-REQ-007, PWB-REQ-001, RFC1-5, RFC1-12, RFC1-18, RFC1-20, RFC1-25, RFC2-1, RFC2-13, RFC2-14,
  RFC2-15, RFC2-24, RFC2-25, RFC6-14, RFC6-17, VIS-2 and VIS-6 at their
  definition sites;
- CC-REV-1, CC-REV-2, CC-REV-4 and CC-REV-6;
- the semantic-delta template and normative-change workflow;
- the P-79 ruling row, the 2026-09-23 retention direction, and the M12
  funnel's Q5 row and slice 4 section, and VIS-6's violation line;
- the current sibling packages (lane B, opening band `.21`, machine view
  `.22`, exact-source `.30`, missing currency `.20`) and `.18` as an
  unperformed candidate only;
- the criteria below.

**Freeze:** review the exact commit named in the raw output. Any later
package, patch, builder, manifest, registration or packet edit retires the
review.

## Criteria

1. **Quotation fidelity.** Every quoted clause matches its definition site;
   nearby prose does not stand in for a clause.
2. **Classification.** Decide independently between Clarifying and
   Normative.
3. **Arm fidelity.** Does the sibling-state arm honestly answer P-79 Q5's
   "before any dismissal touches a tuple"? Is the packet's framing of the
   other two arms fair?
4. **Contract fit.** The text satisfies RFC2-15 (attributed, reasoned,
   expiring, governed plane, never green, facts kept beside), RFC1-20 and
   VIS-6(a) (lapse only through a new evaluation), RFC1-25 `dismisses`,
   RFC2-1 item 9, RFC1-12 (retired identities) and RFC6-14 sibling-state
   parity. Test whether the claim-for-gap reading is labelled and whether
   every row resting on it is held Unknown. Report any clause it contradicts
   or leaves out.
5. **No wall clock.** No sentence lets a page or answer change by reading
   time. The first scenario's "reading the first evaluation again" case must
   hold.
6. **Tuple preservation.** No tuple value changes; the challenge vocabulary
   is untouched; RFC2-13's `resolved-dismissed` is not conflated.
7. **Aggregate polarity.** No aggregate counts a dismissed claim as resolved
   or favourable; dismissed members stay in every label, tier and reason
   count and are also counted separately.
8. **Refused, lapsed, retired.** The refused-record cases close every way a
   record could dismiss without authority, and a valid record that no longer
   applies is shown as lapsed or bound to a retired identity, never refused.
   The expiry boundary is exact.
9. **Same-change propagation.** All eleven subjects; the six patched files
   change together and the other five stay exact.
10. **Coverage rows.** Test the twelve repair-row changes independently,
    especially the four held or new Unknown rows (RFC1-20.r1, RFC1-25.r1,
    RFC2-15.r1, RFC6-14.r6) and the believed-not-applicable rows (RFC1-12.r2,
    RFC1-25.r2, RFC6-14.r5). Confirm totals regenerate to
    627 / 141 / 240 / 246.
11. **Impact sweep.** Re-run the 1,537-file sweep, the continuation forms
    and the published range-form regex; check the 19 digest pins and implementation consumers.
12. **Sibling composition.** Exercise the 15 declared outcomes in both
    orders and the sequential run.
13. **Builder fail-closed behaviour.** Run `--check`, `--selftest` and
    `--diff`; independently mutate at least the paragraph, a scenario, a
    warrant, a coverage row, the manifest and a composition outcome.
14. **Governance hygiene.** No bound byte edited; no performed act's argument
    or truncated digest quoted; no observed-repository path backticked;
    phrase and copy registered with no successor-chain link; CG-26 lists
    untouched.
15. **Authority boundary.** Nothing signs, adopts, authors a recorder or act
    record, chooses performance order, creates a write path or authorizes
    implementation.
16. **Owner packet.** Digest exact; one copyable phrase marked not offered;
    open questions answerable by a non-specialist; no package proposal
    attributed to the owner; silence keeps current behaviour.

## Required report

Start with one exact verdict word: **CONFIRM**, **CONFIRM WITH EXCEPTIONS**
or **REVISE**. Then give numbered findings mapped to criteria and
verification rules, the commands and mutations run with their denominators,
exact files and lines for each finding, and any owner-only decision still
blocking final bytes.

Raw output is kept verbatim under `docs/reviews/` with a filename ending
`-RAW.md`. Findings are dispositioned in the packet's review record; verdict words
are copied exactly.
