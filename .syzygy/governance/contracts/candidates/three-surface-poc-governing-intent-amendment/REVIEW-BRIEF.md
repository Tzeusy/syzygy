# Review brief — Three-Surface POC governing-intent amendment

> **Candidate — binds nothing.** This brief tells a fresh-context reviewer
> what to read and what to decide. It is not itself under review.

## What you are reviewing

One CC-REV-2 amendment package against the signed
`openspec/changes/three-surface-poc-experience/` specification, and the
owner decision it raises:

- the four patches under `proposed/`;
- `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md` and `OWNER-DECISION-PACKET.md` in
  this directory;
- register row P-100 in
  `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`.

Apply the patches in a scratch copy (`git worktree add --detach`, then
`git apply`); never apply them in the tree. There is no manifest or builder
in this version; the impact ledger says why.

## Governing references (read only these)

- **The drafting direction:**
  `.syzygy/governance/decisions/OWNER-DIRECTION-2026-10-03-OVERNIGHT-BEADS-LOOP.md`.
  It permits drafting and performs no act.
- **The coordinator's narrowing:** the 2026-10-03 notes on bead
  `syzygy-u05.10` (`bd show syzygy-u05.10`), quoted in `SEMANTIC-DELTA.md`.
- **The signed subject:** the six artifacts of
  `openspec/changes/three-surface-poc-experience/` and their act,
  `.syzygy/governance/decisions/THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md`.
- **The specification bar:** CC-SPEC-1…11 in
  `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`.
  It is in force despite the path; craft acts 6 and 7 bound it.
- **The clauses the package maps or relies on:**
  - RFC4-15 and RFC4-17 in
    `.syzygy/governance/contracts/rfcs/RFC-0004/named-adapters.md`;
  - RFC8-21, RFC8-22, RFC8-23 and RFC8-24 in
    `.syzygy/governance/contracts/rfcs/RFC-0008/accounting-reconciliation-and-release.md`;
  - RFC2-24 in
    `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`.
- **The sign-off scope:**
  `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`.
- **The sibling package the ledger names:**
  `.syzygy/governance/contracts/candidates/three-surface-poc-identity-amendment/`
  (for the overlap claim only).
- **Doctrine:** VIS-1, VIS-2, VIS-3, VIS-4 and VIS-6 in
  `.syzygy/governance/doctrine/vision.md`; SEC-5 in
  `.syzygy/governance/doctrine/security.md`.

**Security constraint on the reviewer.** Do not query the Butlers Beads
database or read any Butlers file. Every figure here can be checked against
the Syzygy tree or is labelled with the revision it was measured at.

## Acceptance criteria

1. **Narrowed scope.** The delta reads no new work-item column and admits no
   Butlers content class. Column admission is stated as an open question
   pointing to P-100. Item (c), the source-to-claims index, is deferred and
   listed in the packet, not drafted.
2. **The specification bar.** POC-REQ-014 meets CC-SPEC's bar: one
   obligation form, a scope, a sweep oracle with a denominator, an
   observable, oracle independence, a falsifier, and scenarios the
   requirement text actually carries.
3. **Contract claims.** Every contract claim is anchored to a defined clause
   and quoted (verification rule 8). The new covered matrix rows claim only
   what POC-REQ-014's oracle observes, and every uncovered limb of a newly
   mapped clause is listed as Unknown. Judge whether the chosen reason,
   `source-uncaptured-or-unreachable`, fits RFC2-24's condition text better
   than the alternatives the delta weighs.
4. **Signed bytes.** No signed byte outside the proposed patches changes.
   The only signed rows that move are RFC8-22 and RFC8-23, from Part B2 to
   Part A.
5. **Mechanics.** The proposed `GOVERNING-DEPENDENCIES.md` equals what
   `scripts/build_three_surface_poc_spec_dependencies.py` generates from the
   proposed `spec.md`. The matrix totals equal computation. The ledger's
   sweep figures re-derive at `c371339d`.
6. **Honest claims.** The package claims no adoption, schedules no
   implementation, does not treat the contents of unread Butlers columns as
   known, and names every residual the sign-off change must carry.
7. **Plain language.** The owner packet is plain and free of jargon. A fresh
   reader can restate the three questions and their consequences (VIS-3).

Run `python3 scripts/check_governance.py` in a clone at the reviewed commit,
not this worktree (verification rule 7).

## Output contract

Write your raw output verbatim to the path the dispatcher names; it ends in
`-RAW.md`. The first four non-blank lines must be exactly these:

```text
# <title>
Reviewed commit: <40-hex commit you read>
Package digest: <sha256 over the package files, computed as below>
Verdict: CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE
```

The package digest is the sha256 of the output of
`sha256sum $(git ls-files .syzygy/governance/contracts/candidates/three-surface-poc-governing-intent-amendment | LC_ALL=C sort)`
at the reviewed commit, computed by script.

Then add a `## Findings` section. Number findings continuously as
`**Finding N — title** (blocking|revise|note)`. CONFIRM WITH EXCEPTIONS
means every finding is a `note`.
