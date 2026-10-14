# Review brief — Three-Surface POC identity amendment

> **Candidate — binds nothing.** This brief tells a fresh-context reviewer
> what to read and what to decide. It is not itself under review.

## What you are reviewing

One CC-REV-2 amendment package against the signed
`openspec/changes/three-surface-poc-experience/` specification:

- the four patches under `proposed/`;
- the manifest `THREE-SURFACE-POC-IDENTITY-AMENDMENT-MANIFEST.txt`;
- `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md` and `OWNER-DECISION-PACKET.md` in
  this directory;
- the builder `scripts/build_three_surface_poc_identity_amendment.py`.

Read the proposed bytes with `python3
scripts/build_three_surface_poc_identity_amendment.py --diff`. Or apply the
patches in a scratch copy; never apply them in the tree.

## Governing references (read only these)

- **The ruling:**
  `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`,
  row P-75.
- **The design the ruling adopted:**
  `docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md`, §"Slice 3 — One amendment
  package" and Gate 5.
- **The signed subject:** the six artifacts of
  `openspec/changes/three-surface-poc-experience/` and their act,
  `.syzygy/governance/decisions/THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md`.
- **The specification bar:** CC-SPEC-1…11 in
  `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`.
  It is in force despite the path; craft acts 6 and 7 bound it.
- **The clauses the package maps:** RFC1-25 and RFC1-26 in
  `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`;
  RFC6-1, RFC6-3, RFC6-12 and RFC6-14 in
  `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`;
  RFC2-24 and RFC2-25 in
  `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`.
- **The sign-off scope:**
  `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`.
- **Doctrine:** VIS-1, VIS-2, VIS-3 and VIS-7 in
  `.syzygy/governance/doctrine/vision.md`, and
  `.syzygy/governance/doctrine/trust-and-evidence.md`.

## Acceptance criteria

1. **Ruling content.** The package carries exactly what P-75 ruled, and
   nothing more:
   - POC-REQ-054;
   - the POC-REQ-060 amendment;
   - POC-REQ-055;
   - a ribbon scenario;
   - Q3's seven outside kinds, repaired by a new requirement plus disclosure,
     with the signed coverage row unedited;
   - Q4's Inferred as a typed landing zone with no production constructor.
2. **The specification bar.** Each new or amended requirement meets
   CC-SPEC's bar: one obligation form, a scope, and a sweep oracle with a
   denominator. It also needs an observable, oracle independence, a
   falsifier, and scenarios that the requirement text actually carries.
3. **Contract claims.** Every contract claim is anchored to a defined clause
   (verification rule 8). The matrix's new covered rows are honest: no row
   claims a consequence its requirement's oracle does not observe, and every
   uncovered limb of a newly mapped clause is listed as Unknown.
4. **Signed bytes.** No signed byte outside the proposed patches changes. In
   the coverage matrix, the only signed rows that move are the four Part B2
   beliefs named in the delta; the RFC1-26 closure row survives byte for byte.
5. **Mechanics.** `--check` passes, `--selftest` passes, and each selftest
   mutant fails on its own predicate (rule 6). The generated dependency file
   equals regeneration, and the printed totals equal computation.
6. **Honest claims.** The package claims no adoption, schedules no
   implementation, and names every residual the sign-off change must carry.
   The residuals named today are the sign-off route, the reconciliation
   checker and census, and the version-tag recorder registration.
7. **Plain language.** A fresh reader can restate what changes and what does
   not (VIS-3).

Run the checks in a clone, not this worktree (verification rule 7). Use
`python3 scripts/build_three_surface_poc_identity_amendment.py --check` and
`--selftest`, and `python3 scripts/check_governance.py`.

## Output contract

Write your raw output verbatim to the path the dispatcher names; it ends in
`-RAW.md`. The first four non-blank lines must be exactly these, in any
order after the title:

```text
# <title>
Reviewed commit: <40-hex commit you read>
Manifest SHA-256: <sha256 of THREE-SURFACE-POC-IDENTITY-AMENDMENT-MANIFEST.txt, the file>
Verdict: CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE
```

The `Manifest SHA-256` is the digest of the manifest **file** at the reviewed
commit, computed by script. It is not any row inside it.

Then add a `## Findings` section. Number findings continuously as
`**Finding N — title** (blocking|revise|note)`. CONFIRM WITH EXCEPTIONS
means every finding is a `note`.

## Round 6

*(Added 2026-10-14, before the round, by the cycle-2 repair lane. Everything
above this heading still governs round 6 except where this section says
so.)*

**Warrant.** The owner's direction of 2026-10-14, given in the lead session
and relayed to the repair lane: repair every round-5 finding, notes
included, then one fresh review under the same stopping rule [Observed: as
relayed; not yet recorded under `decisions/`].

**Stopping rule, set before the round.** One round.

- A verdict with **no revise-level finding** (`CONFIRM`, or `CONFIRM WITH
  EXCEPTIONS` whose findings are all notes) clears the exact bytes it read,
  under the owner's 2026-09-26 ruling
  (`../../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1).
  Its notes go in a sibling `ROUND-6-DISPOSITIONS.md`, and the package is
  not edited.
- A verdict of **`REVISE`** (any revise-level finding) goes back to the
  owner with its findings open: no further repair and no round 7 without a
  new owner direction.
- A clearance is not a sign-off. Question 1 stays the owner's (VIS-4). A
  verdict is never re-labelled.

**What changed since round 5.**

- Findings 33–38 are repaired as `ROUND-5-DISPOSITIONS.md` §"Repairs,
  2026-10-14 (cycle 2)" maps them.
- The patches were regenerated over `main` after the P-97 block-provenance
  sign-off moved the signed spec and its dependency file. The P-97 bytes
  are now part of the signed subject the patches apply to; they are not
  this package's content.
- Question 2 is answered by
  `../../../decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md`.
  Criterion 6's "sign-off route" residual is therefore answered, and the
  delta now names five residuals; judge criterion 6 against that list.

**Governing references.** Those listed above, plus the Scope A extension
named just above, the round-5 raw
`docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-5-RAW.md`, and
`ROUND-5-DISPOSITIONS.md`.

**What to test, at least.**

- Finding 33: do POC-REQ-054's attribution rule, ownership test and
  equality limb now reach machine-answer records, and does the new
  unattributed-carrier limb close the phantom-subject path the round-5 raw
  describes? Do the RFC6-1 and RFC6-3 covered rows claim no more than the
  oracle now states?
- Finding 34: is one denominator phrase used in the sweep and the first
  scenario?
- Finding 35: does the RFC2-25 "never green" row, and the delta, state the
  reading the covered limb rests on, and say where the other reading lands?
- Finding 36: is "that source's own identifier" now fixed per source by a
  stated route, and is Unknown ownership honest (never passing)? Did that
  repair change what any covered row claims?
- Finding 37: run your own probes against the round-4 and round-5 repair
  text; the builder's selftest now carries 48 structure mutants.
- Finding 38: is the sibling regeneration step in the delta's residual
  list?
- Signed bytes: the patches apply to the current signed tree, including the
  P-97 bytes, and change nothing outside the declared edits.
- Are the dated status marks at the stale sentences, with the old text
  kept, and is any stale sentence left unmarked?

**Output.** Write the raw review to
docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-6-RAW.md (a file this round
creates; left out of code span so the path check does not ask it to exist
first). **Head contract:** its first four non-blank lines must be
exactly these, with nothing appended to the title line:

```text
# R-M9-POC-IDENTITY-AMENDMENT-6 — fresh-context review, round 6, Three-Surface POC identity amendment
Reviewed commit: <the full 40-hex commit you reviewed>
Manifest SHA-256: <sha256 of THREE-SURFACE-POC-IDENTITY-AMENDMENT-MANIFEST.txt, the file>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

`Manifest SHA-256` is the sha256 of the manifest **file**
`THREE-SURFACE-POC-IDENTITY-AMENDMENT-MANIFEST.txt` at the reviewed
commit, computed by script (`sha256sum` at a clean checkout whose
`git rev-parse HEAD` is the reviewed commit). It is not any row inside the
manifest, and not the digest of any proposed subject. Number findings
continuously from 39, label each `[Observed]`, `[Inferred]` or `[Unknown]`,
mark each `blocking`, `revise` or `note`, and close with the count of
each.
