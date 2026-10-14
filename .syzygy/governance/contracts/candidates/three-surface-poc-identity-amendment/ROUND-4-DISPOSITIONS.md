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
    *(Superseded 2026-10-14: on the owner's direction of that day the
    package was edited once, to repair findings 26–32. See "Repairs,
    2026-10-14" below.)*
  - **No round 5 is dispatched.**
    *(Superseded 2026-10-14: the same direction orders one fresh
    confirmation round over the repaired bytes before the owner is asked
    the content questions.)*
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
*(Superseded 2026-10-14: every finding below is repaired; see "Repairs,
2026-10-14" at the end. The "open" words below are kept as written.)*

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

## Repairs, 2026-10-14

**Warrant.** The owner's direction of 2026-10-14, as relayed to this repair
by the coordinating session: repair where needed, then one fresh
confirmation review per packet before the owner is asked the content
questions. No decision record in `.syzygy/governance/decisions/` names that
direction yet [Observed: three files there carry the date, and each concerns
the P-107 v1.2 sign-off]. The direction
answers this record's recommendation ("answer Question 1 with **Revise**")
in substance. It is not an answer to the packet's Question 1 or Question 2,
both of which stay open.

**Effect.**

- Every finding, 26–32, is repaired once, notes included. No finding needed
  an owner choice.
- The repair retires the round-4 review (rule 10). The repaired bytes are
  **unconfirmed, pending round 5**.
- The manifest was regenerated with the builder's `--write`. The patches
  were regenerated from an applied scratch copy, and
  `GOVERNING-DEPENDENCIES.md` from the dependency generator over the
  repaired spec. No generated byte was hand-edited.
- The round-5 raw's `Manifest SHA-256` line carries the digest of the
  manifest **file** at the reviewed commit, computed by script. The review
  brief's output contract is unchanged.

**Figures, re-derived over the repaired bytes.** These come from the
builder's `--check` and from an independent script that imports nothing
from the builder: 26 requirements and 28 scenarios; Part A 139 rows over 78
clauses, 103 covered and 36 Unknown; 32 rows marked "Amendment row".
Round 4 read 134 rows, 102 covered and 32 Unknown. The selftest now runs 32
structure mutants, up from 24.

| Finding | Repair |
|---|---|
| 26 (revise) | POC-REQ-054's sweep population is now every element on the served surfaces **and** every record in the machine answer that carries a subject identity. "Owned" is decided by a stated procedure: the attributed source record carries a non-empty identifier of its source's own record format. Two value-free limbs hold for every subject, owned or not: one identity value per subject, and one subject per identity value. Both are in the oracle's decision rule and the falsifier. The RFC6-1 covered row now says "for a subject a source authority owns". The RFC6-3 covered row reads "names the same subject … and in the machine answer". Its justification is now the oracle's attribution and counts, not "all surfaces read one model instance". |
| 27 (revise) | POC-REQ-060's Scope, sweep and decision rule now quantify over every entity, relationship and claim in the machine answer. The sweep checks that each carries exactly one epistemic record. The falsifier adds "an entity, relationship or claim with no epistemic record or with more than one". The RFC6-14 covered row now says "carries exactly one epistemic record" and names that denominator. |
| 28 (revise) | RFC2-25's `asserted-by-worker` Authority words each have a row. **"never green"** is covered: the claim is Inferred and renders with the declared Inferred encoding, distinct from Observed. **"never a status input"** is covered for the two computations the POC performs (no Observed total, no Unknown cleared), with an Unknown row for any positive status. **"Visible"** is a new Unknown row. **"challengeable"** has its own Unknown row. "Never clears an Unknown" moved from the never-green row to the status-input row. |
| 29 (note) | The delta now says "every other signed consequence or belief row is unchanged". It names the computed lines that do move: the RFC2, RFC6 and Total family-table rows and the five `COMPUTED_LINES`. |
| 30 (note) | `spec_findings` now fails when any signed reader-notes line is lost, except the six lines `READER_NOTE_EDITS` names (the rewrapped group and decision-key lists). It checks their replacements through `READER_NOTE_PHRASES`, including the group range "(054–055, 060–061)". New required phrases guard POC-REQ-054's two independence clauses and POC-REQ-055's "none is imported from the model". `companion_findings` guards the proposal's Q4 sentence (`PROPOSAL_Q4`). The `--check` line prints the requirement count computed over the proposed spec. Eight new mutants cover these guards, including each probe the reviewer reported as surviving. |
| 31 (note) | A new Unknown row under RFC2-25 covers the source limb: the claim arises from "An LLM worker's assertion of an outcome with no retained artifact". The oracle checks only that the record names an assertion. "A comparison of each Unknown it addresses" is replaced by a recount of every Unknown in the machine answer with and without the record, whose two sets by identity must be equal. The Inferred scenario's THEN follows: "leaves every Unknown in the machine answer Unknown". |
| 32 (note) | The delta and the owner packet each carry a second labelled departure: role pairs, not only kinds. Each quotes the design's slice-3 sentence and says what "Revise" would remove. The semantic-class and rule row is split. "A closed-name relationship honours its row's semantic class and rule" now sits under RFC1-25, and "No relation is re-typed" under RFC1-26. |

**Sibling packages.** [Observed 2026-10-14] The block-provenance builder
(`scripts/build_three_surface_poc_block_provenance_amendment.py --check`,
P-97) still passes over the repaired patches. It applies both spec patches
in every order and warns, as before, that this package and the
governing-intent amendment (P-100) are a declared mutually exclusive pair.
The impact ledger's "Sibling packages: none" sentence is marked stale at the
sentence, not removed.
