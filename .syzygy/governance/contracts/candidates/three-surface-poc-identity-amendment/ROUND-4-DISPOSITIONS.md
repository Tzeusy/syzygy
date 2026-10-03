> # Record beside the package — not authority, binds nothing
>
> Dispositions of the fourth fresh-context review of the Three-Surface POC
> identity amendment package. This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It offers nothing and
> performs no act (VIS-4).

# Round 4 dispositions — Three-Surface POC identity amendment

- **Reviewed commit:** `de81d25930429d926566162b19b16fe52807be1a`.
- **Verdict (raw line 4):** `REVISE`. There are three revise findings
  (26, 27 and 28) and four notes (29–32), with no blocking finding.
- **Stopping rule applied.** `ROUND-2-DISPOSITIONS.md` set the rule before
  round 3 ran, and `ROUND-3-DISPOSITIONS.md` repeated it: round 3's findings
  were repaired once more, and if round 4 was also not notes-only, no
  further round would be dispatched and the open findings would go to the
  owner with the package. Round 4 is not notes-only. So:
  - **The package is not edited.** The bytes the owner would read are the
    bytes round 4 reviewed. Their manifest file hashes to the digest on the
    raw's line 3.
  - **No round 5 is dispatched.**
  - **The review has not cleared.** This version is not "ready for owner
    sign-off" in the sense the packet's Question 1 recommends ("Sign v1.0
    (recommended once the review clears)"). It goes to the owner with the
    seven findings below open.
- **Recommendation to the owner:** answer Question 1 with **Revise**. Direct
  the repairs proposed below, then one fresh round. Signing these bytes as
  they stand would sign covered rows that the round-4 reviewer found
  over-claim (findings 26–28).

Reviewed record: docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-4-RAW.md

## Findings, open

Each finding is **open**. The proposed repair is the drafter's reading of
the raw, offered for the owner's Revise answer. None is applied.

### 26 — POC-REQ-054's oracle misses the machine answer's identities and leaves "unowned" undefined (revise)

**Agreed; open.** Proposed repair:

- Enumerate the machine answer's identity-bearing records in the sweep
  population.
- For subjects that no source authority owns, add the reviewer's value-free
  check: every element attributed to one subject carries one identity value.
- Narrow the RFC6-3 covered row, whose justification ("all surfaces read one
  model instance") is an implementation fact, to what the oracle observes.

### 27 — POC-REQ-060 sweeps records, not the objects that must carry them (revise)

**Agreed; open.** Proposed repair:

- Make the denominator every entity, relationship and claim in the machine
  answer.
- Require exactly one record on each.
- Add "an entity, relationship or claim with no epistemic record" to the
  falsifier.

### 28 — RFC2-25's "Visible" limb unlisted; the covered row paraphrases the clause (revise)

**Agreed; open.** Proposed repair:

- Add a "Visible" Unknown amendment row.
- Restate the covered row against RFC2-25's own words ("never green",
  rendered distinctly from Observed).
- Move "never clears an Unknown" to the row for the "never a status input"
  limb.

### 29 — "Every other signed row is unchanged" overstates (note)

**Agreed; open.** The delta should say "every other signed consequence or
belief row", and name the family-table rows and computed lines that the
builder recomputes.

### 30 — guard gaps in the reader notes and the proposal's Q4 sentence (note)

**Agreed; open.** Proposed repair:

- Extend the lost-line check to the spec's reader notes.
- Add a phrase guard for the proposal's "needs its own owner act" sentence.
- Print the requirement count computed rather than as a literal.

The reviewer judged criterion 5 met.

### 31 — the Inferred limbs rest on "names" and an undefined "addresses" (note)

**Agreed; open.** Proposed repair:

- Add an Unknown row for the provenance limb: arising from an assertion, not
  only naming one.
- Replace "each Unknown it addresses" with a recount of every Unknown before
  and after.

### 32 — the role-pair widening is unlabelled as a departure; one row filed under the wrong clause (note)

**Agreed; open.** Proposed repair:

- Add a departure note in the delta: the design's slice 3 says "every
  emitted kind", and the package checks role pairs as well.
- Split the semantic-class and rule row so that those limbs sit under
  RFC1-25 and "no relation is re-typed" under RFC1-26.
