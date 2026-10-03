# Review brief — non-governed narrative profile

> **Candidate — binds nothing.** This brief says what an independent
> reviewer is given and what they decide. It is not a review and carries no
> verdict. Round 1 (REVISE) is retained in `reviews/`; this brief is for
> round 2 over the repaired bytes.

## What the reviewer is given, and nothing else

CC-REV-1 calls for a fresh context holding only the artifact, its governing
references and the acceptance criteria.

**The artifact under review.**

- `openspec/changes/polaris-non-governed-narrative-profile/proposed/polaris-generation/spec.md`
  (the subject), and in the same directory tree `proposal.md`, `design.md`,
  `tasks.md` and `GOVERNING-DEPENDENCIES.md`.
- In `.syzygy/governance/contracts/candidates/non-governed-narrative-profile/`:
  `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md` and this
  brief.

**Governing references.**

- `.syzygy/governance/contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`
  and `SEMANTIC-DELTA-TEMPLATE.md`; CC-SPEC-1 to CC-SPEC-11 in
  `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` and CC-IMPACT-1 to
  CC-IMPACT-7 in `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` (craft acts 6 and 7 put these in
  force; the path still says candidate); CC-REV-1 and CC-REV-2.
- RFC1-14 (`.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`)
  and RFC7-2, RFC7-6, RFC7-13, RFC7-14, RFC7-15, RFC7-17, RFC7-18, RFC7-19,
  RFC7-20 and RFC7-33 in `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`,
  each read at its defining clause and quoted (verification rule 8).
- The effective requirements 001, 002, 004, 020, 025 and 030: the base spec
  `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`,
  the overlay `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`,
  and `decisions/POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md`.
- Doctrine VIS-1 to VIS-4 and SEC-2.
- `docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md`, section 2 and
  gap 17, as the stated motive only.
- `AGENTS.md`, "Hard prohibitions" and "Verification rules".

## Acceptance criteria

Each is a yes/no question with the evidence that settles it.

1. **Is the change class right?** The delta says Normative. Is Clarifying
   the better class (an unchanged obligation made harder to misread), and is
   the reason given wrong?
2. **Is the current meaning quoted exactly?** Re-extract each quoted
   sentence, scenario and RFC clause from its file by script and compare.
3. **Does the requirement touch any bound byte?** Confirm by hashing and
   grepping manifests (`ACCEPTANCE-ACT-RECORD.md`, the packages'
   `*-MANIFEST.txt`) that no file the change edits is act-bound, and that
   the two adopted change directories are byte-identical to the base commit.
4. **Does (a) stay inside the existing rule?** The adopted scenario "Catalog
   membership comes from declarations" forbids inventing a declared
   capability from code. Does the proposed definition of "declared" keep
   that, and is a declaration form frozen before discovery a real constraint
   rather than a formality? Can a producer still launder a code-derived
   capability into the catalog?
5. **Does (b) respect RFC7-17 and RFC7-19?** The profile renders no reality
   band. Does that violate "exactly one of three authority classes" or "no
   hidden section", and is "one line per deep dive" a lawful reading of "one
   honest line" or an exception that RFC7-19 does not allow? Say which, and
   label it.
6. **Does (c) satisfy RFC7-13 and RFC7-14?** (c) no longer calls the span the
   leaf: the leaf altitude is one honest `missing-declaration` line and the
   span is the RFC7-2 (a) anchor. Is that lawful without an amendment to
   RFC7-13 or RFC7-14, and is RFC7-14 quoted whole in the delta? State your
   answer and its warrant; the owner decides (packet O1).
7. **Does the requirement meet CC-SPEC?** Check each of CC-SPEC-1 to 11 that
   applies: warrants complete and real, stable ID unused (sweep
   `REQ-polaris-generation-032` and report the denominator), named
   falsifiable form, non-goals explicit, no hidden shape decision.
8. **Is the impact ledger honest?** Re-run the six sweeps with the
   published regexes at the stated commit by your own script; report your own
   counts for each sweep, for A together with B, and for each classification
   row (the ledger states the path rules), and say where yours differ. Confirm
   the second-method claim. Name any citer form the regexes miss. Confirm the claimed tooling failure by placing a copy of the
   spec at `specs/polaris-generation/spec.md` in a scratch tree and running
   `scripts/count_polaris_effective_scenarios.py`.
9. **Does the package claim any authority it lacks?** No file may label
   anything accepted or adopted; every banner must say it binds nothing; no
   Markdown file may carry a 64-hex digest as an act argument; no target
   repository body is read or described as read.
10. **Do the epistemic labels hold?** Each Inferred, Observed and Unknown
    label must match its evidence.

11. **Round-1 repairs.** `reviews/ROUND-1-DISPOSITIONS.md` dispositions each
    round-1 finding. For each, is the disposition true of the current bytes?
    Name any repair that introduced a new defect, any count a repair copied
    rather than re-derived, and whether the glossary decision (packet O5,
    deferred) is justified by the sources it cites.

## Out of scope

- Whether to adopt it, which sign-off form to use and the owner rulings in
  the packet. A reviewer may say an answer is inconsistent with the package,
  but does not choose one.
- The altitude order for a dossier, the "advantages" framing and the page
  budget, which this change deliberately does not decide.

## Recording

Store the raw output verbatim in `reviews/` of this package as
`R-NON-GOVERNED-NARRATIVE-PROFILE-2-RAW.md`; round 1 is the `-1-RAW.md` beside
it and is never overwritten. The first four lines of the file must be the
title and exactly the three lines below, with **no blank line anywhere in
those four lines**:

```text
# <title>
Reviewed commit: <the 40-hex commit the reviewer read>
Subject SHA-256: <SHA-256 of the FILE proposed/polaris-generation/spec.md at that commit>
Verdict: CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE
```

"Subject SHA-256" is the digest of that one file under
`openspec/changes/polaris-non-governed-narrative-profile/`, not of a package
or manifest (this package has no manifest); print it with `sha256sum`. Number
findings continuously as `**Finding N — title** (blocking|revise|note)` under
a `## Findings` heading. A CONFIRM WITH EXCEPTIONS clears the bytes only when
every finding is a `note`, dispositioned in a sibling `ROUND-<n>-DISPOSITIONS.md`
naming the raw on a `Reviewed record:` line. Any later edit to the package
retires the review (rule 10).
