# Review brief — PWB readability successor

> **Candidate — binds nothing.** This brief says what an independent reviewer
> is given and what they decide. It is not a review and carries no verdict.
> Do not read the candidate, manifest, commit or pull request as an owner act
> or as implementation authority.

## What the reviewer is given, and nothing else

**The artifact** — the files of
`.syzygy/governance/contracts/candidates/pwb-readability-successor/`
(`SEMANTIC-DELTA.md`, `SEMANTIC-MAP.json`, `IMPACT-LEDGER.md`,
`OWNER-DECISION-PACKET.md`, this brief,
`PWB-READABILITY-SUCCESSOR-MANIFEST.txt`), the four patches under
`proposed/`, and `scripts/build_pwb_readability_successor.py`.

**The subject** — `openspec/changes/polaris-project-wide-butlers-model/` at its
current bytes; they must remain unchanged by the review.

**Governing references**

- The owner's 2026-09-27 readability direction (`syzygy-73e`), D5, D6 and
  CC-REV-8.
- VIS-1, VIS-2, VIS-3, VIS-4, VIS-7.
- CC-REV-1/2/4/6/7/8, CC-SPEC-1…11, CC-IMPACT-1…7.
- Every `PWB-REQ-*` requirement in the subject's `spec.md`, current and
  proposed.
- `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`, for which PWB
  acts and sign-offs are in force.
- `OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`, for how a
  confirmation is used.

## Acceptance criteria

1. **Predecessor.** Confirm the current eleven subject bytes equal the
   item-depth v1.0 manifest rows, and that every sibling PWB spec patch is
   applied or declined, as `IMPACT-LEDGER.md` says.
2. **Identities and order.** All 17 requirement headings and all 44 scenario
   headings survive unchanged, in the same order, each exactly once.
3. **Normative words.** Compare each requirement's current and proposed
   normative region independently of the builder. Try to find a lost or
   weakened modal, a dropped condition, qualification, Unknown, refusal or
   fail-closed branch, a moved sentence that changes what a pronoun or
   "otherwise" refers to, or a bold label that reads as an added term or
   condition. A label that changes how a sentence is read is a finding even
   when the words are equal.
4. **Byte-equal parts.** Every group line, verification block, scenario and
   warrants block is byte-equal; regenerate `GOVERNING-DEPENDENCIES.md`
   independently and confirm only its source digest moves.
5. **Reading guide.** The guide is marked non-normative and says it adds no
   requirement. Check that every statement in it, the flow diagram and the
   table is true of the requirements, and that none can be read as a rule.
6. **Proposal and design.** Read both as a fresh reader. Check every unit the
   semantic map classifies: a `preserved` unit says what it said, a
   `clarified` unit adds no claim, and each of the 15 `changed` units is a
   faithful summary of signed text or a correct removal of a false sentence.
   A changed unit the map calls preserved or clarified, or a summary that
   says more or less than the requirement it names, is a finding. The
   quotations `CAPABILITY-COVERAGE.md` relies on must still be found.
7. **Semantic map.** Every requirement and scenario maps once, old to new,
   with its observable, coverage, contract and implementation consequence.
   No blanket equivalence claim is made anywhere in the package.
8. **Package mechanics.** Run the builder with `--check`, `--selftest` and
   `--diff`. Re-derive all eleven manifest rows and the manifest-file SHA-256;
   verify four patch targets and no edit of a current signed byte. Apply the
   four patches in a scratch copy and run
   `scripts/build_polaris_project_wide_contract_coverage.py --check`,
   `scripts/build_polaris_project_wide_spec_dependencies.py --check`,
   `scripts/check_polaris_response_ceiling_reading.py --check` and
   `openspec validate polaris-project-wide-butlers-model --strict` over it.
   Kill at least the changed-modal and stale-manifest predicates yourself.
   Confirm `--apply` without `--at-adoption` is refused and that a failed
   check leaves every signed-subject byte unchanged, in a scratch mirror.
   Re-derive the ledger's file counts with the predicates it publishes.
9. **Owner boundary.** No phrase is offered, no implementation authority is
   implied, and the packet says what the sign-off change must also wire.
10. **Comprehension.** Under CC-REV-8, a reader with no authoring context can
    use the proposed `spec.md` alone to say what the specification covers,
    find any requirement from the table, and tell normative words from
    reading aids.

## Out of scope

Whether to sign off; whether the normative words should be reworded (the
packet routes that to the owner); any implementation file; the registry entry
and secret policy pins.

## Recording

Raw output goes under `docs/reviews/`, in a file whose name ends `-RAW.md`,
verdict words copied exactly.

**The raw's head.** The version-tagged recorder
(`scripts/record_versioned_signoff.py`) reads the raw by this predicate, so
the head must satisfy it exactly:

> The first four non-blank lines of the raw are, in order: a title line
> beginning `# `; `Reviewed commit: ` followed by the full 40-hex commit;
> `Manifest SHA-256: ` followed by the 64-hex SHA-256 of the file
> `PWB-READABILITY-SUCCESSOR-MANIFEST.txt` (informational); and `Verdict: `
> followed by `CONFIRM`, `CONFIRM WITH EXCEPTIONS` or `REVISE`, copied exactly.

**Findings.** A `## Findings` section follows. Each finding is a bold heading
of the form `**Finding N — title** (blocking)`, `(revise)` or `(note)`, with N
numbered from 1 without gaps. A CONFIRM WITH EXCEPTIONS clears the bytes only
when every finding is a note. Cite file and line for each.
