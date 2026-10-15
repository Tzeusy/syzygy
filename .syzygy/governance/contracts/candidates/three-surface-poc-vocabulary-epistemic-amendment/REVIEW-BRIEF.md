# Review brief — Three-Surface POC vocabulary and epistemic-record amendment

> **Candidate — binds nothing.** This brief tells a fresh-context reviewer
> what to read and what to decide. It is not itself under review.

## What you are reviewing

One CC-REV-2 amendment package against the signed
`openspec/changes/three-surface-poc-experience/` specification:

- the four patches under `proposed/`;
- the manifest `THREE-SURFACE-POC-VOCABULARY-EPISTEMIC-AMENDMENT-MANIFEST.txt`;
- `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md` and `OWNER-DECISION-PACKET.md` in
  this directory;
- the builder `scripts/build_three_surface_poc_vocabulary_epistemic_amendment.py`.

Read the proposed bytes with `python3
scripts/build_three_surface_poc_vocabulary_epistemic_amendment.py --diff`,
or apply the patches in a scratch copy. Never apply them in the tree.

This package is a narrower redraft of the parked
`../three-surface-poc-identity-amendment/` (register row P-84). It is not a
seventh round of that package. Read the parked package only for the
findings census's input: its six raws
(`docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-1-RAW.md` to `-6-RAW.md`) and
their `ROUND-<n>-DISPOSITIONS.md` records.

## Governing references (read only these)

- **The ruling:**
  `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`,
  row P-75.
- **The narrowing:** the owner's 2026-10-14 direction, quoted as relayed in
  `SEMANTIC-DELTA.md` §"Why this package exists".
- **The design the ruling adopted:**
  `docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md`, §"Slice 3 — One amendment
  package", and slices 4a, 4b and 8.
- **The signed subject:** the six artifacts of
  `openspec/changes/three-surface-poc-experience/`, their act
  `.syzygy/governance/decisions/THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md`,
  and the two v1.0 sign-off records
  `THREE-SURFACE-POC-BLOCK-PROVENANCE-AMENDMENT-SIGNOFF-v1.0.md` and
  `THREE-SURFACE-POC-GOVERNING-INTENT-AMENDMENT-SIGNOFF-v1.0.md` beside it.
- **The specification bar:** CC-SPEC-1…11 in
  `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`.
  It is in force despite the path; craft acts 6 and 7 bound it.
- **The clauses the package maps:** RFC1-25 and RFC1-26 in
  `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`;
  RFC2-24 and RFC2-25 in
  `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`;
  RFC6-14 in
  `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`.
- **The sign-off route:**
  `.syzygy/governance/decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md`.
- **Doctrine:** VIS-1, VIS-2, VIS-3 and VIS-7 in
  `.syzygy/governance/doctrine/vision.md`, and
  `.syzygy/governance/doctrine/trust-and-evidence.md`.

## Acceptance criteria

1. **Ruling content, as narrowed.** The package carries POC-REQ-055 and the
   POC-REQ-060 amendment, and with them P-75's Q2 (the POC's own record
   shape, not PWB-REQ-007's), Q3 (the outside kinds repaired by a new
   requirement plus disclosure, the signed coverage row unedited) and Q4
   (Inferred as a typed landing zone with no production constructor). It
   carries nothing of POC-REQ-054, the ribbon, the cross-surface link row
   or the join key.
2. **The narrowing is justified and complete.** The findings census in
   `SEMANTIC-DELTA.md` places every one of the 43 findings in exactly one
   theme, and its counts follow from the raws. Its conclusion follows from
   the census. Every item left out is listed as deferred scope, with an
   owner question in the packet.
3. **The specification bar.** Each new or amended requirement meets
   CC-SPEC's bar: one obligation form, a scope, and a sweep oracle with a
   denominator. It also needs an observable, oracle independence, a
   falsifier, and scenarios the requirement text actually carries. Check
   especially that nothing in POC-REQ-055 or POC-REQ-060 still leans on the
   deferred subject identity.
4. **Contract claims.** Every contract claim is anchored to a defined clause
   and quoted (verification rule 8). No covered row claims a consequence its
   requirement's oracle does not observe. Every uncovered limb of a newly
   mapped clause is listed as Unknown.
5. **Signed bytes.** No signed byte outside the proposed patches changes. In
   the coverage matrix the only signed row that moves is the RFC2-25 Part B2
   belief. The RFC1-26 closure row survives byte for byte, and POC-REQ-014's
   block is unchanged.
6. **Mechanics.** `--check` passes, `--selftest` passes, and each selftest
   mutant fails on its own predicate (rule 6). The generated dependency file
   equals regeneration, and the printed totals equal computation.
7. **Honest claims.** The package claims no adoption and schedules no
   implementation. It names every residual the sign-off change must carry
   (`SEMANTIC-DELTA.md` lists five).
8. **Plain language.** A fresh reader can restate what changes and what
   does not (VIS-3).

**What to test, at least.**

- The three changes from the parked POC-REQ-060 (`SEMANTIC-DELTA.md` §2):
  is each one decidable, and does each covered row still claim only what
  the oracle observes?
- POC-REQ-014, carried from note 4 of the P-100 round-3 raw: re-judge its
  encoding arm, and its RFC2-24 and RFC8-24 rows, against the amended
  POC-REQ-060's table, not only the patched lines.
- The census: re-derive the theme counts and the revise-level counts from
  the six raws' finding headings.
- Run your own probes against the phrase guards. The selftest fails if any
  listed guard lacks a mutant. Sentences outside the guards are frozen only
  by the manifest digest.

Run the checks in a clone, not this worktree (verification rule 7). Use
`python3 scripts/build_three_surface_poc_vocabulary_epistemic_amendment.py --check`
and `--selftest`, `python3 scripts/build_three_surface_poc_spec_dependencies.py --check`,
and `python3 scripts/check_governance.py`.

## Stopping rule, set before round 1

One round.

- A verdict with **no revise-level finding** (`CONFIRM`, or `CONFIRM WITH
  EXCEPTIONS` whose findings are all notes) clears the exact bytes it read,
  under the owner's 2026-09-26 ruling
  (`../../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1).
  Its notes go in a sibling `ROUND-1-DISPOSITIONS.md`, and the package is
  not edited.
- A verdict of **`REVISE`** (any revise-level finding) goes back to the
  owner with its findings open. There is no repair and no round 2 without a
  new owner direction.
- A clearance is not a sign-off. Question 1 stays the owner's (VIS-4). A
  verdict is never re-labelled.

## Output contract

Write the raw review verbatim to
docs/reviews/R-M9-POC-VOCABULARY-EPISTEMIC-AMENDMENT-1-RAW.md (a file this
round creates; it is left out of code span so the path check does not ask
it to exist first). **Head contract:** its first four non-blank lines must
be exactly these, with nothing appended to the title line:

```text
# R-M9-POC-VOCABULARY-EPISTEMIC-AMENDMENT-1 — fresh-context review, round 1, Three-Surface POC vocabulary and epistemic-record amendment
Reviewed commit: <the full 40-hex commit you reviewed>
Manifest SHA-256: <sha256 of THREE-SURFACE-POC-VOCABULARY-EPISTEMIC-AMENDMENT-MANIFEST.txt, the file>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

`Manifest SHA-256` is the sha256 of the manifest **file**
`THREE-SURFACE-POC-VOCABULARY-EPISTEMIC-AMENDMENT-MANIFEST.txt` at the
reviewed commit, computed by script (`sha256sum` at a clean checkout whose
`git rev-parse HEAD` is the reviewed commit). It is not any row inside the
manifest, and not the digest of any proposed subject.

Then add a `## Findings` section. Number findings from 1 as
`**Finding N — title** (blocking|revise|note)`, label each `[Observed]`,
`[Inferred]` or `[Unknown]`, and close with the count of each level.
`CONFIRM WITH EXCEPTIONS` means every finding is a `note`.

The docs review-campaign partition (`docs/README.md`) needs a row and a
pattern for this raw's basename in the same commit that lands it.
