# Review brief — PWB tree framing

> **Candidate — binds nothing.** This brief says what an independent reviewer
> is given and what they decide. It is not a review and carries no verdict.
> Do not read the candidate, manifest, commit or pull request as an owner act
> or as implementation authority.

The reviewer decides whether the package's proposed PWB-REQ-014 text makes
Polaris's own framing an abstraction tree with supported, inert diagrams,
without touching Butlers text or any neighbouring requirement.

## What the reviewer is given, and nothing else

**The artifact** — the files of
`.syzygy/governance/contracts/candidates/pwb-tree-framing-amendment/`
(`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`, this
brief, `PWB-TREE-FRAMING-AMENDMENT-MANIFEST.txt`), the five patches under
`proposed/`, and `scripts/build_pwb_tree_framing_amendment.py`.

**The subject** — `openspec/changes/polaris-project-wide-butlers-model/` at its
current bytes; they must remain unchanged by the review.

**Governing references**

- CC-REV-8 in `.syzygy/governance/policies/craft-and-care/review-and-documentation.md`.
- `.syzygy/governance/decisions/OWNER-DIRECTION-2026-09-28-TREE-STYLE-ROLLOUT.md`.
- `.syzygy/governance/decisions/POLARIS-TREE-FORM-AMENDMENT.md` ("Interactions")
  and `POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md` (the SVG ruling).
- `.syzygy/governance/decisions/POLARIS-LANE-B-DECLINED-AND-TARGET-REVISED-DIRECTION.md`
  (the 1,650,000-byte working target).
- VIS-1, VIS-2, VIS-3, VIS-4, VIS-7, SEC-3.
- CC-REV-1/2/3/4/6/7/8, CC-SPEC-1…11, CC-IMPACT-1…7.
- RFC7-2, RFC7-13, RFC7-17.
- PWB-REQ-006, PWB-REQ-007, PWB-REQ-010, PWB-REQ-011, PWB-REQ-012,
  current and proposed PWB-REQ-014, PWB-REQ-015, PWB-REQ-016, PWB-REQ-020 and
  PWB-REQ-021 in the subject's `spec.md`.
- `OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`, for how a
  confirmation is used.

## Acceptance criteria

1. **Scope.** Only PWB-REQ-014's block, the design decision, the two proposal
   sub-bullets, coverage row 33 and the regenerated dependencies move. Try to
   find a byte of another requirement, a scenario of another requirement or
   the reading guide that the patches move.
2. **Butlers text stays verbatim.** Try to construct a reading under which an
   opening may paraphrase, condense, reorder or replace Butlers-declared text,
   or under which tree form applies to anything but Syzygy-authored openings
   and ledes.
3. **Openings are true summaries.** Is "states only what that group's own
   rendered children state" testable, and does it rule out an opening that
   introduces a conclusion found nowhere beneath it? Is the set of groups that
   must open (project category, catalog, item detail, evidence group) clear
   enough to enumerate on a rendered page?
4. **One opening aggregate.** Show whether any opening can become a second
   Unknown aggregate before the first capability catalog, contrary to
   PWB-REQ-010's scenario, or a counting statement without PWB-REQ-007's
   aggregate disclosure.
5. **Diagram support.** Test an edgeless relationship, a relationship whose
   only edges are Unknown, a node drawn from a label, an element drawn Unknown
   without a claim establishing it, and a prose-sufficient relationship. Is
   each result stated, and is no element ever drawn without a model claim?
6. **Inert render.** Do the excluded classes match the owner's 2026-09-28 SVG
   ruling, does validation precede every sink, and does a failed render emit
   nothing active while keeping the text equivalent? Does anything in the
   delta amend PWB-REQ-006, or need to?
7. **Neighbouring authority.** Attempt to show that PWB-REQ-006, 007, 010,
   011, 012, 015, 016, 020 or 021, or RFC7-2/13/17, becomes false under the
   applied text. A counterexample the delta does not already disclose as an
   open point is a finding. Judge the four open points only for accuracy and
   completeness.
8. **Package mechanics.** Run the builder with `--check`, `--selftest` and
   `--diff`. Re-derive all eleven manifest rows and the manifest-file SHA-256;
   verify five patch targets and no edit of a current signed byte. Apply all
   five patches in a scratch copy and run
   `scripts/build_polaris_project_wide_contract_coverage.py --check` and
   `scripts/build_polaris_project_wide_spec_dependencies.py --check` over it.
   Check the sibling classification: every tracked PWB spec patch is pending,
   applied, performed by an existing record or in the closed declined list, and
   the counts in `IMPACT-LEDGER.md` match. Confirm `--apply` without
   `--at-adoption` is refused and a failed check leaves every signed-subject
   byte unchanged, in a scratch mirror. Re-derive the ledger's citer counts
   with the predicates it publishes.
9. **Budget claim.** The page-size table is labelled Observed and the
   projection Inferred. Judge only whether the labels and the method are
   honest; re-measuring needs a private daemon and is not required.
10. **Owner boundary.** No phrase is offered, no successor-chain position is
    asserted, no landing order is attributed to the owner, and sign-off would
    authorize no implementation.
11. **Comprehension and form.** Under CC-REV-8 a reader with no authoring
    context can restate what an opening may say, when a diagram is owed, what
    happens to an undrawable or failed diagram, and the two later owner gates
    (sign-off, then a fresh implementation authorization). The resolution
    diagram repeats the text and adds no state or route.

## Out of scope

Whether to sign off; the order of other PWB successors; any implementation
file; which relationships a later rendered-design review lists.

## Recording

Raw output goes under `docs/reviews/`, in a file whose name ends `-RAW.md`,
verdict words copied exactly.

**The raw's head.** The version-tagged recorder
(`scripts/record_versioned_signoff.py`) reads the raw by this predicate, so
the head must satisfy it exactly:

> The first four non-blank lines of the raw are, in order: a title line
> beginning `# `; `Reviewed commit: ` followed by the full 40-hex commit;
> `Manifest SHA-256: ` followed by the 64-hex SHA-256 of the file
> `PWB-TREE-FRAMING-AMENDMENT-MANIFEST.txt` (informational); and `Verdict: `
> followed by `CONFIRM`, `CONFIRM WITH EXCEPTIONS` or `REVISE`, copied exactly.

**Findings.** A `## Findings` section follows. Each finding is a bold heading
of the form `**Finding N — title** (blocking)`, `(revise)` or `(note)`, with N
numbered from 1 without gaps. A CONFIRM WITH EXCEPTIONS clears the bytes only
when every finding is a note. Cite file and line for each.
