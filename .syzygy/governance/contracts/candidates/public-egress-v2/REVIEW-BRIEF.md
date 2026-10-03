# Review brief — second Anthropic egress version (sitting row 8)

> **Candidate — binds nothing.** This brief says what an independent reviewer
> is given and what they decide. It carries no verdict. Dispatch it only after
> PR #281 is on main and `python3 scripts/build_public_egress_v2.py --ready`
> exits 0); a review over a not-ready record is wasted by the next edit
> (rule 10).

## What the reviewer is given, and nothing else

CC-REV-1: a fresh context holding the artifact, its governing references and
the acceptance criteria.

**The artifact.** Every file of
`.syzygy/governance/contracts/candidates/public-egress-v2/` except `reviews/`,
plus `scripts/build_public_egress_v2.py` and the first version's record and
template it is built from (`../public-repo-admission/`).

**Governing references.** SEC-2, SEC-3, VIS-4; RFC5-12 to RFC5-16 and RFC3-30,
each read at its defining clause; REQ-polaris-generation-001, 017, 025; the
`rfc5-project-documentation-class` package's proposed RFC5-14, read as if in
force; `public-source-screening-scope`'s instruction-text rule.

**The head of your raw review** must be four lines, in this order, with the
manifest FILE digest (the output of `--manifest-digest`, not the digest of the
row inside it): the title, `Verdict:`, `Reviewed commit:`, `Manifest SHA-256:`.
A blank line after the title breaks the head.

## Acceptance criteria

Each is yes or no with the evidence that settles it.

1. **The differences are exactly the listed ones.** Diff the record against the
   first version's. Are the version, the added class, the table, and the
   route-neutral wording (provider line, retention, the "beyond these fields"
   paragraph, the model-sees-only condition, route context and telemetry) the
   only differences, other than the instance header, the title and the
   revocation line? Quote each differing line. Does the template differ from
   the first version's template only in the lines that make this so?
2. **Is the supersession sentence right?** Quote RFC5-13. Does "prospective"
   hold, and is signing this version alone coherent with REQ-polaris-generation-025
   (consents separately revocable)?
3. **Order.** Is it true that, without row 7, the permitted class is
   undeterminable under RFC5-14's closed vocabulary? If it is not, say what
   the single egress check does instead.
4. **The table.** Does every discovery stage in `requiredStages` occur in the
   record's table, each field with exactly one class? Re-run the derivation;
   do not trust the record.
5. **Instruction text.** Does any discovery instruction text come from a
   symbol the screening scope's rule does not name? If so, the record would
   refuse its own request: say so as blocking.
6. **Readiness gate.** Mutate `requiredStages` (empty; a stage the table lacks;
   a substring of a stage); do `--digests` and `--manifest-digest` refuse each?
   Run `--selftest` and read its output.
7. **Nothing else moved.** Are retention, route context and the admitted
   repositories byte-identical to the first version's? Is any claim here a
   promise the record cannot keep?

## Verdict form

One of CONFIRM, CONFIRM WITH EXCEPTIONS (notes only), REVISE (blocking
findings). Findings as `**Finding N — title** (blocking|revise|note)`.

## Added criteria for the route-neutral wording

8. **Neutral and sufficient.** Read the record against both registry entries
   (PR #255 and PR #273): does it permit exactly the bytes each entry lists
   and no other, with neither route hard-coded? Quote the clause for the
   entry-pinned fields (model, effort, tools, thinking, output ceiling). Does
   it still refuse a field outside the table?
9. **Independence.** Does anything in the record make signing it choose a
   route, or make a route entry depend on signing it? The packet says they are
   independent; is that true of the bytes?
10. **No weakening.** Is any first-version condition (tools off, no context of
    its own beyond the listed bytes, telemetry off, run-directory retention)
    weaker here than there? Name each change and say whether it is a
    restatement or a loosening.
