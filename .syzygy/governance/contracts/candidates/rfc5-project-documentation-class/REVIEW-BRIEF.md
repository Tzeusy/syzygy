> **Candidate — binds nothing.** This brief says what an independent reviewer
> is given and what they decide. It is not a review and carries no verdict.
> Round 1 (REVISE) is retained in `reviews/`; this brief is for round 2 over
> the repaired bytes.

# Review brief — RFC5-14 `project-documentation` class

## What the reviewer is given, and nothing else

CC-REV-1 calls for a fresh context holding only the artifact, its governing
references and the acceptance criteria.

**The artifact under review.** Every file of
`.syzygy/governance/contracts/candidates/rfc5-project-documentation-class/`
(`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, this brief, `OWNER-DECISION-PACKET.md`,
`CONTRACT-AMENDMENT-MANIFEST.txt`, `proposed/RFC-0005/consent-egress-secrets.md.patch`)
and `scripts/build_rfc5_project_documentation_class.py`.

**The subject, at its current bytes:**
`.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md` and its
mirror under `contracts/candidates/rfcs/`.

**Governing references.**

- RFC5-14, RFC5-15, RFC5-16 and RFC5-17 at their defining clauses in the
  subject (quote the clause).
- RFC3-16(a) in `rfcs/RFC-0003/governance-homes-and-owner-acts.md`.
- SEC-2 in `.syzygy/governance/doctrine/security.md`; VIS-4.
- `contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md` and
  `SEMANTIC-DELTA-TEMPLATE.md`.
- `openspec/changes/polaris-manifesto-generation/SOURCE-POLICY.md`, section
  "Carry content provenance through composition", and REQ-polaris-generation-025
  in that change's `specs/polaris-generation/spec.md`.
- `contracts/candidates/general-trusted-bootstrap-authorization/CONTRACT-AMENDMENT-MANIFEST.txt`
  (the CG-7h binding of the subject).
- Question Q7 in the admission packet on the `polaris/public-repo-admission`
  branch (PR 215), as the warrant.

## Acceptance criteria

Each is a yes/no question with the evidence that settles it.

1. **Is the change class right?** The delta says Normative. Is any part of it
   Clarifying, and is any part more than Normative (does it touch a doctrine
   obligation, SEC-2, so that a doctrine act is needed)?
2. **Does the patch change exactly what the delta says?** One table row and
   one bullet in RFC5-14, nothing else. Re-derive by script: the six
   existing rows, the composite bullet, clause leads, front matter and
   headings are byte-identical (`python3 scripts/build_rfc5_project_documentation_class.py --check`).
3. **Is the membership definition precise enough to classify?** Take ten
   sample files a project might hold (a README, a CONTRIBUTING file, a
   LICENSE, an architecture overview, a design decision record, a
   specification, a docstring-heavy source file, a changelog, a generated API
   reference, a notebook) and place each. Name any that the text leaves
   ambiguous without the fail-closed rule, and say whether "contribution
   guides" sits wrongly against `governance-text`.
4. **Does the amendment widen any existing consent?** Confirm from RFC5-14 and
   RFC5-15 that a consent record listing the six classes does not permit the
   new one, and that the bullet saying so does not conflict with another
   clause.
5. **Does it keep the composite rule and secret screening intact?** The delta
   says "highest" is unchanged and no order is added. Is that statement true
   of the proposed text? Does "rule above" resolve to the composite bullet, and
   does "fails closed (RFC5-15)" cite a clause that says so for a single file?
6. **Is the blast radius honest?** Re-run the three sweeps in
   `IMPACT-LEDGER.md` at the commit they name, from the regexes, run form and
   span rule as printed there, by your own script, and report your own figures
   for A, B, A and B together, the union and C, and for each group of the
   classification (the ledger states a path rule per group). Do not accept the
   ledger's figures; say where yours differ and why. Name any authority text
   that enumerates the vocabulary and is not listed (rule 9). Confirm that
   `SOURCE-POLICY.md` is digest-bound by a performed act and so correctly left
   unedited.
7. **Is the migration plan sound?** The module is bound by the bootstrap
   manifest and the restyle link. Is it right that the patch must not be applied
   while this is a candidate, and does the plan name the regeneration and
   re-review cycle (workflow rule 7)?
8. **Does the package verify, and does the verification mean anything?** Run
   `--check` and `--selftest`. Name any claim the builder makes that no mutant
   covers.
9. **Does the package claim any authority it lacks?** No file may label
   anything accepted, adopted, approved or signed off; every banner must say it
   binds nothing; no 64-hex digest may appear in any Markdown file of the
   package.
10. **Is the act-form discussion in the packet accurate?** Are the three
    options described correctly, including that Scope A's named scope does not
    obviously reach an RFC-0005 amendment, and is it labelled Inferred?

11. **Round-1 repairs.** `reviews/ROUND-1-DISPOSITIONS.md` dispositions each
    round-1 finding. For each, is the disposition true of the current bytes?
    In particular: Finding 1 (does the signals sub-bullet now constrain only
    how a signal places a file in this class, leaving the content of a
    declared policy to the policy, and does the delta say so?) and Finding 2
    (do the published predicate and your own run agree?).

## Out of scope

- Whether to perform the act. That is the owner's alone.
- Public-source screening rules that place project documentation; a separate
  candidate.
- Any change to the "highest class" wording of the composite bullet.

## Recording

Store the raw output verbatim in `reviews/` of this package as
`R-RFC5-PROJECT-DOCUMENTATION-CLASS-2-RAW.md`; round 1 is the `-1-RAW.md` beside
it and is never overwritten. The first four lines of the file must be the
title and exactly the three lines below, with **no blank line anywhere in
those four lines** (a blank line pushes `Verdict:` past a literal four-line
head):

```text
# <title>
Reviewed commit: <the 40-hex commit the reviewer read>
Manifest SHA-256: <SHA-256 of the FILE CONTRACT-AMENDMENT-MANIFEST.txt>
Verdict: CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE
```

`Manifest SHA-256` is the digest of the manifest **file** at the reviewed
commit, printed with `sha256sum` (it has one row; the file and the row are
different digests, and the row is not what the head carries). Number findings
as `**Finding N — title** (blocking|revise|note)` under a `## Findings`
heading. A CONFIRM WITH EXCEPTIONS clears the bytes only when every finding is
a `note`, dispositioned in a sibling `ROUND-<n>-DISPOSITIONS.md` that names the
raw on a `Reviewed record:` line. Any later edit to the package retires the
review (rule 10).
