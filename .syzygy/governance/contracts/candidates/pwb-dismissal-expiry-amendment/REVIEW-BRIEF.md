# Review brief — dismissal with a live expiry (PWB-REQ-007)

> **Candidate — binds nothing.** This commissions an independent review; it
> carries no verdict and performs no act. The reviewer must not receive the
> drafting conversation or a desired verdict.

## Exact review inputs

Give the fresh reviewer only:

- this package in full: `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`,
  `OWNER-DECISION-PACKET.md`, this brief, the eleven-row manifest and all six
  `proposed/*.patch` files;
- `scripts/build_pwb_dismissal_expiry_amendment.py` and the matching
  registration diff in `scripts/check_governance.py`;
- the signed PWB eleven-artifact subject;
- PWB-REQ-007, PWB-REQ-001, RFC1-20, RFC1-25, RFC2-1, RFC2-13, RFC2-14,
  RFC2-15, RFC2-24, RFC2-25, RFC6-14, RFC6-17, VIS-2 and VIS-6 at their
  definition sites;
- CC-REV-1, CC-REV-2, CC-REV-4 and CC-REV-6;
- the semantic-delta template and normative-change workflow;
- the P-79 ruling row, the 2026-09-23 retention direction, and the M12
  funnel's Q5 row and slice 4 section;
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
   RFC2-1 item 9 and RFC6-14 sibling-state parity. Report any clause it
   contradicts or leaves out.
5. **No wall clock.** No sentence lets a page or answer change by reading
   time. The first scenario's "reading the first evaluation again" case must
   hold.
6. **Tuple preservation.** No tuple value changes; the challenge vocabulary
   is untouched; RFC2-13's `resolved-dismissed` is not conflated.
7. **Aggregate polarity.** No aggregate counts a dismissed claim as resolved
   or favourable, and dismissed members are counted separately.
8. **Refusals.** The refused-record cases close every way a record could
   dismiss without authority.
9. **Same-change propagation.** All eleven subjects; the six patched files
   change together and the other five stay exact.
10. **Coverage rows.** Test the nine repair-row changes independently,
    especially RFC2-1.r2 (Unknown), RFC1-25.r2 and RFC6-14.r5 (believed not
    applicable). Confirm totals regenerate to 625 / 143 / 236 / 246.
11. **Impact sweep.** Re-run the 1,537-file sweep and continuation forms if
    practical; check the 19 digest pins and implementation consumers.
12. **Sibling composition.** Exercise the 15 declared outcomes in both
    orders.
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
    open questions answerable by a non-specialist; silence keeps current
    behaviour.

## Required report

Start with one exact verdict word: **CONFIRM**, **CONFIRM WITH EXCEPTIONS**
or **REVISE**. Then give numbered findings mapped to criteria and
verification rules, the commands and mutations run with their denominators,
exact files and lines for each finding, and any owner-only decision still
blocking final bytes.

Raw output is kept verbatim under `docs/reviews/` with a filename ending
`-RAW.md`. Findings are dispositioned in `SEMANTIC-DELTA.md`; verdict words
are copied exactly.
