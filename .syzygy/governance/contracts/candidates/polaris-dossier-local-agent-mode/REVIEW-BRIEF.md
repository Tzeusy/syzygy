# Review brief — Polaris dossier local-agent mode

> **Candidate — binds nothing.** This brief says what an independent
> reviewer is given and what they decide. It is not a review and carries no
> verdict. No round has run.

## What the reviewer is given, and nothing else

CC-REV-1 calls for a fresh context holding only the artifact, its governing
references and the acceptance criteria.

**The artifact under review.**

- `openspec/changes/polaris-dossier-local-agent-mode/proposed/polaris-generation/spec.md`
  (the subject), and in the same change `proposal.md`, `design.md`,
  `tasks.md` and `GOVERNING-DEPENDENCIES.md`.
- In `.syzygy/governance/contracts/candidates/polaris-dossier-local-agent-mode/`:
  `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md` and this
  brief.

**Governing references.**

- The warrant: `POLARIS-DOSSIER-LOCAL-AGENT-MODE-DIRECTION.md` (in the decisions home; it lands by PR #351 and is not on `main` at this change's base).
- `.syzygy/governance/contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`
  and `SEMANTIC-DELTA-TEMPLATE.md`; CC-SPEC-1 to CC-SPEC-11 in
  `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` and CC-IMPACT-1 to
  CC-IMPACT-7 in `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` (craft acts 6 and
  7 put these in force; the path still says candidate); CC-REV-1 and CC-REV-2.
- RFC2-24 (`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`),
  RFC3-16, RFC4-2, RFC4-19, and RFC7-2, RFC7-9, RFC7-10, RFC7-13, RFC7-19,
  RFC7-20 and RFC7-25 in `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`,
  each read at its defining clause and quoted (verification rule 8);
  `DIRECTIVE-REGISTER.md` gives file and line.
- The effective requirements 001, 004, 005, 006, 012, 017, 018, 019, 020,
  025, 030 and 031: the base spec
  `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`,
  the overlay `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`,
  `decisions/POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md`, and the base change's
  `INTERFACES.md`.
- Doctrine VIS-1 to VIS-4 and SEC-2, SEC-3, SEC-5 (`.syzygy/governance/doctrine/`).
- The sibling candidate `openspec/changes/polaris-non-governed-narrative-profile/`,
  for overlap only.
- `AGENTS.md`, "Hard prohibitions" and "Verification rules".

The reviewer does not receive the drafting conversation, the drafter's
messages to the lead, or any signal of a desired verdict.

## Acceptance criteria

Each is a yes/no question with the evidence that settles it.

1. **Does the change do what the direction authorizes, and no more?** Compare
   with direction items 1 to 5 and "What this direction does not do". Any
   grant of read, egress, write or execution, any withdrawal of the provider
   mode, or any adoption language is a blocking finding.
2. **Is every quotation of current text exact?** Re-extract each block under
   "Current meaning" from its file by script and compare. Is each displaced
   fragment named in the spec present verbatim in the effective file?
3. **Is the displacement complete and bounded?** Is there an adopted
   sentence that an operator-agent run would still violate and that the
   change neither displaces nor reads (check 001, 004, 012, 019, 020, 025 and
   the base change's design files)? Is anything displaced for the provider
   mode?
4. **Is any contract or doctrine changed in effect?** In particular RFC7-20
   and REQ-polaris-generation-001 (owner question O1), RFC2-24's closed
   Unknown reasons, RFC7-10's anchor form, SEC-2 and SEC-3. A spec that
   contradicts an accepted clause is blocking.
5. **Is every Observed claim something Syzygy can observe?** Check each
   requirement's Observed / Inferred / operator-declared split against what a
   local process can actually see. An unobservable fact labelled Observed is
   blocking.
6. **Can each scenario be falsified as written?** CC-SPEC: one WHEN/THEN pair,
   an independent oracle, a falsifier that a wrong implementation would
   trip.
7. **Is the change class right?** The delta says Normative.
8. **Is the impact ledger reproducible?** Re-run its published regexes at its
   commit and compare the counts and the 135-file classification.
9. **Are the owner questions genuinely the owner's, each with a
   recommendation and an honest alternative?** Is any question the drafter
   should have settled, or any decision taken that belongs to the owner?
10. **Does `design.md` stay design?** No implementation code in `openspec/**`;
    the skill and Codex texts are prose, and no command it names claims
    behavior the requirements do not require.

## Output

A raw review stored verbatim as `reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-<n>-RAW.md`
in this package. Its first four non-blank lines:

```text
# Review R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-<n>
Reviewed commit: <40-hex commit the reviewer read>
Subject SHA-256: <sha256 of proposed/polaris-generation/spec.md at that commit, computed by script>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

Then `## Findings`, each numbered continuously as
`**Finding N — title** (blocking|revise|note)`, with the evidence. The
recorder for the sign-off form is not yet chosen (owner question O5); if the
owner chooses `scripts/record_versioned_signoff.py`, its head contract asks
for a `Manifest SHA-256:` line instead, and this brief is revised before the
confirming round.
