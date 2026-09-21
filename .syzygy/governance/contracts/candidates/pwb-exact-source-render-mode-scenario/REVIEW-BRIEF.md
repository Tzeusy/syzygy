> **Candidate — binds nothing.** The review instruction for a drafted
> CC-REV-2 semantic delta. It performs no act, adopts nothing and authorizes
> no implementation. The change it reviews would take effect only through an
> owner act over this package's behavior manifest, named in
> `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`.

# Review brief — PWB exact-source render mode

Review the exact candidate commit and the manifest without authoring
context. The candidate is inert and must not be treated as an act. The
proposed bytes are the patches under `proposed/` over the current tree,
printed by `python3
scripts/build_pwb_exact_source_render_mode_amendment.py --diff`; nothing in
`openspec/` is changed on the reviewed commit.

This is the **first round**. There is no prior raw review of this delta and
no disposition list to check. Judge the bytes on their own.

One thing the reviewer must know that the bytes do not say: a second
candidate amends the same specification in parallel
(`.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/`).
The two are independent in meaning and collide on exactly one generated
line. `IMPACT-LEDGER.md` §"Merge and effect boundary" states the rule and
the builder asserts it; criterion 8 below asks you to test that claim rather
than accept it.

Required baseline:

- `VIS-1`, `VIS-2`, `VIS-3`, `VIS-4`, `VIS-7`; `SEC-1`, `SEC-2`, `SEC-3`;
- `CC-REV-2`, `CC-REV-4`, `CC-REV-6`; `CC-SPEC-1`…`CC-SPEC-11` and
  `CC-IMPACT-1`…`CC-IMPACT-7` (in `contracts/candidates/policy-candidates/`,
  in force by craft acts 6 and 7); `CC-BAR-3`, `CC-TEST-5`, `CC-TEST-6`;
- `RFC2-26`, quoted in `SEMANTIC-DELTA.md` §"Change class" — the
  change-class argument stands or falls on it;
- the warrants PWB-REQ-011 itself declares: `RFC7-13` (primary), `RFC1-26`,
  `RFC3-27`, `RFC3-28`, `RFC6-20`, `RFC6-21`, `CC-BAR-3`, and the parent
  requirement `three-surface-poc-experience/POC-REQ-031`;
- `PWB-REQ-003`, `PWB-REQ-005`, `PWB-REQ-006`, `PWB-REQ-014`, `PWB-REQ-015`,
  `PWB-REQ-020` — reached, not amended;
- the current signed PWB eleven-artifact package and its performed
  2026-09-05 amendment act (`PWB-TRUTH-READINESS-AMENDMENT-ACT.md`);
- the per-repository consent record and the one consented content class, as
  the specification and `design.md` §8 describe them;
- the owner ruling this delta serves, row P-81 of
  `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`;
- the evidence: `docs/design/POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md` and
  `docs/evidence/polaris-m14-provenance-depth-funnel-2026-09-17.json`.

Review criteria:

1. **Withholding holds.** No reading of the amended text serves a body for a
   source whose record outcome is excluded, in either mode, by any route,
   parameter or anchor. Nine sources are withheld today — seven manifests,
   one page, one excluded artifact. Try to construct a reading in which any
   of them is served, and say what you tried.
2. **The gates are not weakened.** Every mode applies the authority,
   exact-object, secret-detection and inert-content gates to the *complete*
   transient body before any part of it is encoded, and a failed gate leaves
   the body Unknown with its reason rather than serving a partial body. Check
   that "before encoding any part of it" cannot be read as per-section.
3. **No wider content class.** The amendment reaches more *sources inside the
   consented class* and no byte outside it. Test the claim against the
   amended `design.md` §8 and against the specification text; a reading that
   admits a new class is a blocking finding.
4. **Change class.** `SEMANTIC-DELTA.md` argues Normative and quotes RFC2-26
   in full. Judge the argument, not the label: is there a reading in which
   the adopted PWB-REQ-011 already obliges what the proposed text obliges? If
   so, the class is wrong in the safe direction and should still be said.
5. **Anchors are not identity.** PWB-REQ-014 says labels, file paths and
   coordinates never serve as anchor identity. A scroll anchor is a
   coordinate. Check that the proposed text keeps it presentation-only,
   that it cannot enter, replace or qualify a source, claim or narrative
   anchor identity, and that PWB-REQ-014 therefore needs no amendment — and
   that the anchor removes, narrows and reorders nothing.
6. **Parity.** P-81 requires the parity sweep to extend over the anchor
   parameter. The delta discharges that inside PWB-REQ-011 rather than by
   editing PWB-REQ-020. Check that the per-rendered-tuple obligation is
   real, falsifiable, and consistent with PWB-REQ-020's own words; and that
   parity is per tuple, never per id.
7. **Closed vocabulary.** The render-mode set is stated as closed. Check
   that it is closed in the text and not merely called closed, that a
   third mode would need an amendment, and that the mode of each served
   route and the reason of each refusal are recoverable from the machine
   answer.
8. **Package mechanics.** The manifest hashes exactly the post-apply bytes
   of the eleven subjects; `--check` and `--selftest` fail closed for
   manifest drift, patch corruption, a transcribed generated digest, and
   the parallel-lane collision; the candidate cannot bind anything by merge.
   Run them; read the output, not the exit code.
9. **Coverage and totals.** `CAPABILITY-COVERAGE.md` row 10 still describes
   what PWB-REQ-011 obliges, the population stays 31 and the totals stay
   25 / 6 / 0, and no other row silently changes meaning.
10. **Scope discipline.** The package draws no PWB-REQ-015 delta and no
    PWB-REQ-002 delta, both of which the owner sequenced separately. Check
    that it also does not *achieve* either one by side effect.
11. **Comprehension.** A fresh reader can restate what changes, what stays
    refused, the one owner choice and the two-step path without author
    context.
12. **Owner packet.** The phrase is present but stated as not offered;
    silence and partial answers perform nothing; nothing in the packet
    authorizes an implementation.

The raw review must state the exact reviewed commit, the manifest SHA-256,
one exact verdict from the set `CONFIRM`, `CONFIRM WITH EXCEPTIONS`,
`REVISE`, and every finding with the file and line it anchors to. A reviewer
who authors a semantic fix retires their review; repaired bytes need a new
fresh reviewer.
