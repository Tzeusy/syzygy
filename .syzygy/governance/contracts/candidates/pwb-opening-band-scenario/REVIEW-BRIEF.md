# Review brief — the Polaris opening-band aggregate scenario

> **Candidate — binds nothing.** An agent drafted these bytes under the
> owner's 2026-09-21 direction recorded in
> `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
> (row P-71, arm A, question 7). This brief commissions a review; it is not
> a review and carries no verdict. Only a dedicated owner act naming this
> package's manifest digest could give the proposed bytes effect.

**No review has been run against this package.** The drafting agent did not
review its own work: the normative-change workflow stops the author at step
2, and a self-review would satisfy neither CC-REV-1's independence nor the
fresh-context rule.

---

## What the reviewer receives

Fresh context, with only these inputs — nothing from the drafting session:

- this package in full: `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`,
  `PWB-OPENING-BAND-SCENARIO-MANIFEST.txt`, `OWNER-DECISION-PACKET.md`,
  `proposed/spec.md.patch`, `proposed/GOVERNING-DEPENDENCIES.md.patch`, and
  `scripts/build_pwb_opening_band_scenario.py`;
- the governing references the delta cites: the signed PWB specification,
  the three-surface specification's POC-REQ-032, RFC2-26 at its defined
  clause, PWB-REQ-007, PWB-REQ-010, PWB-REQ-011, PWB-REQ-012 and
  PWB-REQ-020;
- the owner ruling record named in the banner, rows P-68, P-69, P-71,
  P-71-Q5, P-74, P-75 and P-78;
- the three design packets the reconciliation quotes: the M2, M3 and M4
  funnels;
- the semantic-delta template and the normative-change workflow;
- these criteria.

**Freeze.** The bytes reviewed are the bytes at the commit the review names
(rule 10). Any later edit to this package retires the review; a revision
that follows an owner answer to an open question needs a fresh one.

---

## Criteria

Numbered so findings can cite them. Each is answerable against the bytes.

1. **Quotation fidelity.** Every passage the delta quotes from a signed
   specification, an RFC, a design packet or the ruling record matches its
   source exactly, at the line range given. Nearby prose is not the clause
   (rule 8). Report any paraphrase presented as a quotation.

2. **Change class.** The delta claims **Normative** and argues it from
   added obligation, not diff size. Is that the correct class under the
   template's table? A finding that it is Clarifying, or that it is
   Structural, is in scope.

3. **The scenario's form.** The proposed scenario is WHEN/THEN/AND in the
   specification's existing scenario form, sits under PWB-REQ-010 after the
   existing scenario and before the `warrants` block, and is falsifiable:
   each clause can fail on an inspectable rendering. Report any clause that
   cannot be falsified, or that states a value rather than a behaviour.

4. **One coherent category, no overlap.** The change is one category and
   overlaps no other change. In particular it must not enter the region of
   the P-69 Q7a PWB-REQ-007 clarification (gate bead `syzygy-dov.20`), the
   P-75 Q1 three-surface package (gate bead `syzygy-dov.26`), or the lane B
   scoped-attributes amendment (gate bead `syzygy-dov.17`).

5. **The reconciliation is performed, not asserted.** P-71 conditions slice
   3 on "the three-way opening-band reconciliation". The delta must name the
   three parties from the packet, quote each party's own design text, and
   show which clause of the proposed scenario each agreement produces.
   Report any party quoted only through another party's summary of it, and
   any agreement claimed without a quoted basis.

6. **Contradictions surfaced, never reconciled inside the delta.** The
   template's rule 6 is the bar. Five open questions are raised (OQ-1 to
   OQ-5). For each: is it a genuine tension between two texts, is the
   reading that would make this change land easier explicitly named and
   **not** taken, and is the decision left to the owner? Report any place
   where the delta in fact settles a question it says it leaves open — and
   any further contradiction the delta missed.

7. **RFC2-26.** The delta claims this scenario supplies limb 1 for slice 3
   only, and that slices 4 and 5 remain unmapped on the funnel's own sweeps
   despite P-71 placing them "behind the same scenario". Check both halves
   against RFC2-26's defined clause. A finding that the scenario does not
   even clear slice 3 — because the consequence spans two requirements'
   subjects, which is OQ-2 — is squarely in scope.

8. **What does not change.** The eight-item list is complete and true: no
   requirement minted or retired, no `warrants` block moved, no authority
   added to the CC-IMPACT-1 union, no implementation file touched, and
   **no write into any observed repository described** (P-71-Q5). Report any
   omission.

9. **The impact ledger.** The method is stated well enough to re-derive
   every figure; the denominator is the whole tracked population; the
   continuation-form sweep is present; the class-3 finding about the two
   digest-pinned declarations is correctly labelled Observed, with its
   Inferred part marked. Re-run the sweeps if practical and report any
   figure that does not reproduce (rules 2, 4 and 9).

10. **The manifest and the builder.** The manifest covers all eleven
    artifacts of the bound subject, its two patched rows hash the
    post-apply bytes and its nine unchanged rows hash current bytes. The
    builder's selftest fixtures each fail closed per predicate (rule 6):
    population closure, byte drift, path order, subject drift, patch
    corruption, lane B composition in both orders and a corrupted case,
    generated-declaration tampering, and the declaration-patch collision.
    Mutate an input and confirm the failure rather than trusting the exit
    line (rule 4).

11. **Governance hygiene.** No performed act's digest argument or truncated
    signed digest is quoted (CG-7e, CG-15); act records are cited by path.
    No observed-repository path is set in a code span (CG-1b). Every file
    head carries a candidate banner naming the owner act that would give it
    effect. Substantive claims are labelled Observed, Inferred or Unknown.
    Nothing is labelled accepted, signed or adopted. No byte of the signed
    change directory is edited in place; the proposed bytes exist only as
    diffs under `proposed/`.

12. **Scope of authority.** Nothing in this package performs an act,
    schedules implementation work, or reads as permission to render the
    band. The scenario is conditional by construction; confirm that a
    conforming implementation may still render no opening aggregate at all.

---

## Verdict

One of exactly these three words, copied exactly into the review's raw
output:

- **CONFIRM** — the package may go to the owner as it stands.
- **CONFIRM WITH EXCEPTIONS** — it may go to the owner, with the listed
  non-blocking findings recorded beside it.
- **REVISE** — one or more findings must be repaired and the review re-run
  against the repaired bytes.

Raw output is retained verbatim under `docs/reviews/`, in a file whose name
ends `-RAW.md`, and the verdict word is copied, never restated. A finding
cites a criterion number above and, where it bears on a verification rule,
that rule's number.
