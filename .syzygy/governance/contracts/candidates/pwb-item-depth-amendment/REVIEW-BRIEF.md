# Review brief — PWB item depth

> **Candidate — binds nothing.** This brief says what an independent reviewer
> is given and what they decide. It is not a review and carries no verdict.
> Do not read the candidate, manifest, commit or pull request as an owner act
> or as implementation authority.

## What the reviewer is given, and nothing else

**The artifact** — the files of
`.syzygy/governance/contracts/candidates/pwb-item-depth-amendment/`
(`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`, this
brief, `PWB-ITEM-DEPTH-AMENDMENT-MANIFEST.txt`), the six patches under
`proposed/`, and `scripts/build_pwb_item_depth_amendment.py`.

**The subject** — `openspec/changes/polaris-project-wide-butlers-model/` at its
current bytes; they must remain unchanged by the review.

**Governing references**

- P-81 question 5 in
  `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
  and `docs/design/POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md`, Q5.
- VIS-1, VIS-2, VIS-3, VIS-4, VIS-7.
- CC-REV-1/2/4/6/7/8, CC-SPEC-1…11, CC-IMPACT-1…7.
- RFC2-24, RFC6-14, RFC6-22, RFC7-12…19, RFC7-26/27, RFC7-29, RFC7-33/34.
- PWB-REQ-002, PWB-REQ-003, PWB-REQ-004, PWB-REQ-007, PWB-REQ-010,
  PWB-REQ-011, PWB-REQ-013, PWB-REQ-014, current and proposed
  PWB-REQ-015, PWB-REQ-016 and PWB-REQ-020 in the subject's `spec.md`.
- `OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`, for how a
  confirmation is used.

## Acceptance criteria

1. **Scope.** The delta changes PWB-REQ-015's subject from capability-only
   detail to the complete declared `catalog-entry` population and nothing
   broader. Try to construct a reading that invents a capability or an item.
2. **Bands.** Exactly argument, contract and reality remain, in that order and
   with one existing authority class per block. No fourth class or relaxed
   band obligation is introduced.
3. **Declared relation only.** Test an Observed item with no relation, two
   mutually exclusive relations, two compatible relations (a requirement and a
   non-goal), a same-label requirement and generated prose. The fixed-role
   relation claim keeps its own stable identity, complete tuple, RFC2-24 reason
   and route without changing or borrowing the item tuple. Is every population
   of captured relations, including a mixed one in which some members exclude
   one another, given exactly one result, is "excludes" defined without
   inferring from prose, and is that result deterministic in both channels?
   Does the relation claim have an admitted source and a named currency class,
   or is its absence stated?
4. **Exact intent.** Requirement, scenario, doctrine and non-goal material is
   reachable verbatim from its owner only through PWB-REQ-011's exact-source
   route, never stored, embedded in the band or paraphrased in normative
   position; every excluded, missing, unreadable or gate-failed related source
   has a stated result.
5. **Identity and parity.** Every declared item has exactly one detail; item
   and relation identities and their separate complete tuples survive catalog,
   detail and exact source in both channels. URL, label, path and coordinate
   are not identity.
6. **Proposals and reality.** Current intent remains operative; proposal
   material appears only for matching declared capability detail under
   PWB-REQ-013, where it is adjacent, separate, non-anchorable and
   non-status-bearing. Non-capability detail carries none. A capability that
   matches no item or several has a stated result and a stated matching
   declaration. Reality uses only the one shared model and evaluation.
7. **Neighboring authority.** Attempt to show that PWB-REQ-002, 003, 004, 007, 010,
   011, 013, 014, 016 or 020, or a cited RFC, becomes false under the applied text (render
   modes and their gates, the missing-currency and dismissal rules, the
   machine-view categories, the exact-source route). A counterexample that the
   drafted text does not already disclose as an open point is a finding. The
   four open points in `SEMANTIC-DELTA.md` are disclosed and routed to the
   owner; judge only whether the disclosure is accurate and complete.
8. **Package mechanics.** Run the builder with `--check`, `--selftest` and
   `--diff`. Re-derive all eleven manifest rows and the manifest-file SHA-256;
   verify six patch targets and no edit of a current signed byte. Apply all six
   patches in a scratch copy and run the repository's
   `scripts/build_polaris_project_wide_contract_coverage.py --check` and
   `scripts/build_polaris_project_wide_spec_dependencies.py --check` over it. Check the
   sibling classification: every tracked PWB spec patch is applied, pending or
   in the closed declined list, and the counts in `IMPACT-LEDGER.md` match.
   Confirm `--apply` without `--at-adoption` is refused and that a failed check
   leaves every signed-subject byte unchanged, in a scratch mirror. Re-derive
   the ledger's file counts with the predicates it publishes.
9. **Owner boundary.** The retained phrase is visibly not offered, no
   successor-chain position is asserted, no landing order is attributed to the
   owner, and sign-off would still authorize no implementation.
10. **Comprehension and form.** Under CC-REV-8 a reader with no authoring
    context can restate the population, the three bands, the unmapped-item
    behavior, the compatible-set behavior and the two later owner gates
    (sign-off, then a fresh implementation authorization). The relation diagram
    repeats the text faithfully and introduces no extra state or route.

## Out of scope

Whether to sign off; the order of other PWB successors; any implementation
file; the registry entry and secret policy pins.

## Recording

Raw output goes under `docs/reviews/`, in a file whose name ends `-RAW.md`,
verdict words copied exactly.

**The raw's head.** The version-tagged recorder
(`scripts/record_versioned_signoff.py`) reads the raw by this predicate, so
the head must satisfy it exactly:

> The first four non-blank lines of the raw are, in order: a title line
> beginning `# `; `Reviewed commit: ` followed by the full 40-hex commit;
> `Manifest SHA-256: ` followed by the 64-hex SHA-256 of the file
> `PWB-ITEM-DEPTH-AMENDMENT-MANIFEST.txt` (informational); and `Verdict: `
> followed by `CONFIRM`, `CONFIRM WITH EXCEPTIONS` or `REVISE`, copied exactly.

**Findings.** A `## Findings` section follows. Each finding is a bold heading
of the form `**Finding N — title** (blocking)`, `(revise)` or `(note)`, with N
numbered from 1 without gaps. A CONFIRM WITH EXCEPTIONS clears the bytes only
when every finding is a note. Cite file and line for each.
