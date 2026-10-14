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
   The only signed rows that move are RFC8-22, RFC8-23 and RFC8-24, from
   Part B2 to Part A.
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

## Round 3

*(Added 2026-10-14, before the round, by the cycle-2 repair lane. Nothing
above this heading governs round 3 except where this section says so.)*

**Warrant.** The owner's direction of 2026-10-14, given in the lead session
and relayed to the repair lane: repair every round-2 finding, notes
included, then one fresh review under the same stopping rule [Observed: as
relayed; not recorded under `decisions/` at the commit this section was
written].

**Stopping rule, set before the round.** One round.

- A verdict with **no revise-level or blocking finding** (`CONFIRM`, or
  `CONFIRM WITH EXCEPTIONS` whose findings are all notes) clears the exact
  bytes it read, under the owner's 2026-09-26 ruling
  (`../../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1).
  Its notes go in a sibling `ROUND-3-DISPOSITIONS.md`, and the package's
  other files are not edited. A cleared version may then be offered to the
  owner for sign-off by version tag, under
  `../../../decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md`.
- A verdict of **`REVISE`** goes back to the owner with its findings open:
  no further repair and no round 4 without a new owner direction.
- A clearance is not adoption; Q1–Q3 stay the owner's (VIS-4). A verdict is
  never re-labelled.

**Subject.** Every tracked file of
`.syzygy/governance/contracts/candidates/three-surface-poc-governing-intent-amendment/`
at the reviewed commit: `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`,
`REVIEW-BRIEF.md`, `ROUND-1-DISPOSITIONS.md`, `ROUND-2-DISPOSITIONS.md`,
`SEMANTIC-DELTA.md` and the four patches under `proposed/` — ten files.
Apply the patches in a scratch worktree at the reviewed commit, never in the
tree.

**Governing references.** Those listed above for round 1, with these
changes and additions:

- **You SHOULD read the two earlier raws and their dispositions**:
  `docs/reviews/R-N10-POC-GOVERNING-INTENT-1-RAW.md`,
  `docs/reviews/R-N10-POC-GOVERNING-INTENT-2-RAW.md`,
  `ROUND-1-DISPOSITIONS.md` and `ROUND-2-DISPOSITIONS.md` (its §"Repairs,
  2026-10-14 (cycle 2)" maps each round-2 finding to its repair).
- **The signed subject now includes P-97's sign-off:**
  `.syzygy/governance/decisions/THREE-SURFACE-POC-BLOCK-PROVENANCE-AMENDMENT-SIGNOFF-v1.0.md`.
- **The sign-off route:**
  `.syzygy/governance/decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md`
  in addition to the 2026-10-02 Scope A direction.
- **Both sibling packages**, for the overlap claims only:
  `three-surface-poc-block-provenance-amendment/` (signed) and
  `three-surface-poc-identity-amendment/` (P-84, unsigned, under repair in
  a separate lane the same day).
- **Clauses newly relied on:** RFC8-21 and the RFC8-24 continuation (lines
  176–180) in `RFC-0008/accounting-reconciliation-and-release.md`; RFC2-24's
  rendering rule in `RFC-0002/rendering-vocabularies.md`; and, in the signed
  spec, POC-REQ-042, POC-REQ-043 and POC-REQ-060.

**Criteria changed for round 3.** Criterion 4 now reads: no signed byte
outside the proposed patches changes; the signed rows that move are RFC8-22,
RFC8-23 and RFC8-24 (Part B2 to Part A) and RFC8-21 (Part B2 to Part B1);
the signed RFC2-24 reason-#10 row is edited to add POC-REQ-014. Criterion 5's
generator equality is judged over the signed bytes at the reviewed commit,
not at `c371339d`; the ledger's discovery sweep still re-derives at
`c371339d`. The other criteria stand.

**What to test, at least.**

- Is each round-2 finding repaired as `ROUND-2-DISPOSITIONS.md` §"Repairs,
  2026-10-14 (cycle 2)" says, and did any repair introduce a new inaccuracy?
- Finding 1: can an implementation satisfy POC-REQ-014 and signed
  POC-REQ-042 at once over a database larger than Trajectory's selection?
  Do scenario 1 and the oracle agree?
- Finding 2: does each Trajectory arm (encoding, resolution statement,
  narrowing) now have a decision procedure a checker can run, and do the
  RFC8-23 and RFC8-24 covered rows claim only what those procedures
  observe?
- Finding 3 and note 7: are the new RFC8-24 rows and the RFC8-21 move to
  Part B1 judged honestly, and do the printed totals equal computation?
- Finding 4: do all four patches pass `git apply --check` against the
  signed bytes at the reviewed commit, and does
  `scripts/build_three_surface_poc_spec_dependencies.py` over the proposed
  `spec.md` reproduce the proposed `GOVERNING-DEPENDENCIES.md`?
- Are the dated status marks at the stale sentences, with the old text
  kept, and is any stale sentence left unmarked? Is the packet's Q2 marked
  at the sentence and still plain?

**Output.** Write the raw review to
docs/reviews/R-N10-POC-GOVERNING-INTENT-3-RAW.md (a file this round
creates; left out of a code span so the path check does not ask it to exist
first). **Head contract:** its first four non-blank lines must be exactly
these, with nothing appended to the title line:

```text
# Review - Three-Surface POC governing-intent amendment (POC-REQ-014, P-100) — round 3
Reviewed commit: <the full 40-hex commit you reviewed>
Package digest: <sha256 by the method below>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

`Package digest` is the brief's scripted method **at the reviewed commit**,
unchanged from rounds 1 and 2: at the repo root of a clean clone or
worktree whose `git rev-parse HEAD` is the reviewed commit,
`sha256sum $(git ls-files .syzygy/governance/contracts/candidates/three-surface-poc-governing-intent-amendment | LC_ALL=C sort) | sha256sum`,
over the ten files above. It is the digest of the package's own tracked
bytes, not of any single file, and it includes this brief. Number every
finding as above, label each `[Observed]`, `[Inferred]` or `[Unknown]`, and
close with the count of each class.
