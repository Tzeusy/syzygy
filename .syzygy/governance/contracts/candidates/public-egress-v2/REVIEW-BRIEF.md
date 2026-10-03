# Review brief — second Anthropic egress version (sitting row 8)

> **Candidate — binds nothing.** This brief says what an independent reviewer
> is given and what they decide. It carries no verdict. Dispatch it only when
> `python3 scripts/build_public_egress_v2.py --check` and `--ready` both pass on
> a tree that carries current main; a review over bytes that the next edit
> changes is void (rule 10). Round 1 returned REVISE
> (`reviews/R-EGRESS-V2-1-RAW.md`, `ROUND-1-DISPOSITIONS.md`).

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
row inside it): the title, `Reviewed commit:`, `Manifest SHA-256:`, `Verdict:`.
A blank line after the title breaks the head.

**Which digest.** `--manifest-digest` prints the manifest FILE's digest, the one
the head carries; `--digests` prints the record's digest (the manifest's row, the
act argument), which is a different value and is not the head's. The dispatch
message must name them by those commands, not by prefix.

## Acceptance criteria

Each is yes or no with the evidence that settles it.

1. **The differences are exactly the listed ones.** Diff the record against the
   first version's. Are the version, the added class, the table, and the
   route-neutral wording (provider line, retention, the "beyond these fields"
   paragraph, the model-sees-only condition, route context and telemetry) the
   only differences, other than the instance header, the title and the
   revocation line? Quote each differing line. The added class
   `project-documentation` is a declared, intended widening of what may leave;
   say whether it is declared as such and not hidden. Does the template differ from
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
7. **Nothing else moved.** The admitted repositories are the first version's,
   byte for byte. Retention, route context, telemetry and the provider line
   differ deliberately (route-neutral wording): is each change a restatement or
   a loosening? Is any claim here a promise the record cannot keep?

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
11. **Per-route bytes.** For each route, does the record's summary agree with
    that entry's `requestBytes` (Agent SDK entry in
    `public-admission-registry-entries/proposed/`, Messages API entry in
    `provider-route-messages-api-entry/proposed/`)? Quote the entry field and
    the record line side by side. Does the record permit a route's bytes only
    while its entry is in force, and does it leave stripping to the owner?
12. **What the owner is told.** Does the packet say in plain words what signing
    lets leave the machine (excerpts of files of the two named repositories for
    discovery ranking, and README and guide files under the new class), with the
    caps, and that nothing about the route changes? Check the caps against
    `packages/polaris-generation-core/src/discovery.ts`.
13. **Per-route parameters.** For each route, are the pinned parameters (model,
    effort, tools, thinking, output ceiling) and the endpoint stated as that
    entry lists them, with the differences between the routes spelled out and no
    sentence saying they are "the same"?
14. **Order of signing.** Is signing the first version after this one refused
    (the first version's recorder), and is the packet's statement of it true?
15. **The pinned template delta.** Does `--check` fail when the template moves
    without `templateDelta` in `v2.json` being updated?
