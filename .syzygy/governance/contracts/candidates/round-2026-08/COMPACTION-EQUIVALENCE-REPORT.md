# Compaction equivalence — current-state summary (derived, never authority)

**Derived summary (2026-08-05, human-clarity refactor round).** It answers
one question in one place — *what does the rev9 → rev10 compaction claim
about semantic equivalence, and what is true of the corpus as it stands
today?* Every figure and every claim below is a restatement of a source
named on the line that carries it. **The sources win over this file,
always.** Nothing here is a clause, a review verdict, or an acceptance
record.

**The stored reviews are never edited.** `reviews/rev10-equivalence-review.md`
and the §20 raw reports stay exactly as stored, including the one sentence
now known to be stale (§4 below). A stored review is a record of what a
reviewer said at a moment; correcting it would destroy the record. What
travels with the record instead is this file and the change log at the end
of `04-CLAUSE-MIGRATION-MATRIX.md`.

## 1. What was compacted, in numbers

From `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` §"The numbers, stated
honestly" and `04-CLAUSE-MIGRATION-MATRIX.md`:

| Measure | rev9 | rev10 |
|---|---|---|
| Normative contract text (rev9-derived) | 90,410 w | 73,685 w (−18.5%) as compacted single files |
| Package-split scaffolding (25 module files) | — | +7,333 w |
| Package README indexes (7) | — | +12,696 w |
| New contracts RFC-0010 / RFC-0011 | — | +5,353 w |
| **Total on disk (32 modules)** | 90,410 w | **99,067 w** as reported; **99,080 w** today (see §5) |
| Tier 2 history (linked, non-normative, outside every default load) | interleaved | 27,521 w in `history/` |
| Mandatory reading path for one governed task | ~90,410 w (whole corpus — the only safe instruction) | 10,893–18,315 w measured across the five accepted fixtures |

The 35,000–50,000-word target band was **not** reached and the report says
so, with per-RFC arithmetic: nine independent workers converged on −12% to
−22%, and closing to 40k would have meant deleting obligations, which
OD-R10-3 forbids.

## 2. Clause accounting

**322 numbered clauses**, verified in this session by
`python3 scripts/verify_final_prespec.py` — output line
`numbered clauses defined: 322`, run ending `PASS — all checks clean`.
That is 294 rev9 numbered clauses + RFC10-1…16 + RFC11-1…12.

Identity preservation, re-verified 2026-08-05 by an independent Python `re`
census of `history/rev9-rfcs/` against `rfcs/` (the ugrep hazard makes a
`grep` sweep insufficient for a universal claim):

- rev9: 294 numbered + 21 lettered clause identities;
- rev10: 322 numbered + 22 lettered;
- **zero lost, zero renumbered**;
- gained set, exhaustively: `RFC10-1…16`, `RFC11-1…12`, and **`RFC3-16(c)`**.

So the new-clause count beyond the two new contracts is **1**, not 2. The
matrix's header said 2; it now says 1, logged in that file's change log.
`03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` already said "one new sub-clause
(RFC3-16(c))" and needed no correction.

## 3. The one deliberate semantic resolution

**RFC8-25's superseded fallback.** Rev9's sentence *"Until the bound is
declared, the coverage test above is the operative limit"* is dropped, and
owner decision **B13**'s strictly stricter fail-closed rule stands in its
place: *"Where no threshold is declared, no mutation inherits."* The
retirement is disclosed on the RFC8-25 matrix row, in
`WORKER-REPORT-DIGEST.md` §"Substantive rulings" ruling 3, and in the 03
report; the dropped text survives verbatim in `history/RFC-0008-history.md`.
The stored equivalence review checked it as fixture F-EQ-7 and passed it.
Direction: strictly stricter. **This is the only clause-text semantic
resolution of the pass.**

(The matrix row's pointer to this ruling read "see report judgment call 1",
a heading that exists nowhere in the packet. It now points at the ruling —
logged in the matrix change log.)

## 4. The RFC3-16(b) insertion, now disclosed

Rev10's Bootstrap-correlation paragraph in
`rfcs/RFC-0003/governance-homes-and-owner-acts.md` carries a **role split**
that rev9 did not: what a state-(1) record — owner-adopted, not yet
correlated — *suffices for* now depends on how the artifact is consumed.
An artifact consumed as a **constraint** binds at full strength; an
artifact consumed as an **authorization for an effect** (a consent, an
autonomy envelope, a write-expanding policy) has **not** satisfied the
RFC3-16(a) predicate on a state-(1) record alone, and *Effect when the
predicate fails* governs that effect until the correlation act — RFC10-9 is
the worked example.

- **Found by:** the §20.2 semantic-preservation review, finding 3.
- **Corroborated by:** `10-EXIT-REPORT.md` answer 6, which describes "the
  constraint/authorization split in RFC3-16(b)" as part of the delivered
  acceptance-semantics repair.
- **Authorizing direction:** **OD-R10-5**, "acceptance semantics repaired
  without weakening" (`02-OWNER-DIRECTION-RECORD.md`), the same direction
  that authorized the RFC3-16 relaxation and RFC3-16(c).
- **Direction of the change:** fail-closed. Constraints binding more broadly
  narrows agent behaviour; authorizations stay blocked until correlation.
  The §20.2 reviewer found no security weakening.
- **Status now:** the matrix row for RFC3-16(b) discloses the insertion, its
  effect, and its authorizing direction, and its outcome word is
  `retained with wording sharpened` rather than `retained unchanged`.
- **It mints no clause identity**, so it is not a tally item (§2).

**The stored equivalence review is stale on exactly this point, and only
this point.** Its fixture F-EQ-2 evidence line reads: *"The
Bootstrap-correlation and Effect-when-the-predicate-fails paragraphs are
preserved verbatim."* That sentence is not true of the Bootstrap-correlation
paragraph as the file now stands — the insertion either post-dates the
review or was missed by it. **The review file is not edited.** Its F-EQ-2
verdict (PASS on the nine binding items, on item 9's A1 mechanism-class
wording, and on the RFC5-25 location constraint) is unaffected; what is
stale is the "verbatim" characterisation of one of the two named
paragraphs.

## 5. What is true of the corpus today

- `verify_final_prespec.py` → **PASS — all checks clean** (322 clauses,
  32 modules, two justified oversize/total notes).
- `build_contract_index.py --check` → **no drift**, after a generator fix
  that admits lettered limbs whose bold headline opens with running prose;
  `RFC9-16(d)` was missing from the RFC-0009 clause list and is now present
  (§20.2 finding 8).
- Corpus total is **99,080 w**, 13 words above the 99,067 the 03 report
  states, because `rfcs/RFC-0003/governance-homes-and-owner-acts.md` grew
  from 4,401 to 4,414 w when the retired rev9 acceptance phrase was
  corrected. That edit is a **this-round** change, disclosed in
  `SEMANTIC-DELTAS-THIS-ROUND.md`; the 03 report is a
  point-in-time record and is not amended.
- Three fixture totals and one `06-CONTEXT-LOAD-MAP.md` module figure are
  stale by exactly that edit (and, for fixture 4, by this round's craft
  edits). Enumerated as findings T-2 and T-4 in
  `../TASK-TO-CONTRACT-INDEX.md`; no selection changed, only measured size.

## 6. What this file does not claim

Obligation-level preservation is **not** established corpus-wide by anyone.
The §20.2 reviewer's exhaustive sweeps establish *identity*-level
preservation corpus-wide and full-RFC accounting for RFC-0002; its
obligation findings cover **15 sampled clause identities**, and the reviewer
says so explicitly. The stored equivalence review's fixtures cover eight
more. Any statement stronger than that — "every obligation preserved",
"zero semantic drift" — is **[Unknown]** and must not be written into an
acceptance record. Two further accounting imprecisions the §20.2 reviewer
raised are recorded and **not** repaired: `retained unchanged` is used on
rows carrying word-level copy-edits (RFC3-16(a), RFC7-21), and
`copied verbatim` is used on the RFC2-24 row where five Resolution-route
cells shed non-amendment rationale sentences. Both are vocabulary
imprecision on rows whose obligations the reviewer verified as preserved.
