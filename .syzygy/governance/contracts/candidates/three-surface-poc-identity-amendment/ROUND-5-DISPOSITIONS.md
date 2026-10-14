> # Record beside the package — not authority, binds nothing
>
> Dispositions of the fifth fresh-context review of the Three-Surface POC
> identity amendment package. This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It offers nothing and
> performs no act (VIS-4).
>
> **Status, 2026-10-14 (cycle 2): round-5 findings repaired once on
> 2026-10-14, unconfirmed pending round 6.** Every finding below, notes
> included, was repaired once; see "Repairs, 2026-10-14 (cycle 2)" below.
> The sentences that said otherwise are marked where they stand.
> *(Marked 2026-10-14, round 6: "pending round 6" is no longer true.
> Round 6 returned `REVISE`; see `ROUND-6-DISPOSITIONS.md`.)*

# Round 5 dispositions — Three-Surface POC identity amendment

- **Reviewed commit (raw line 2):**
  `e7fd5301daf1c52a8e8ddab08cb1e50ddf4169d8`, the head of
  `candidate/p84-round4-repairs` (draft PR #413).
- **Manifest file digest (raw line 3):**
  `998215c3aad0483f9862432cddfec6e1b263cd69dc5803e6b9c3a1e1f69b391c`.
  [Observed 2026-10-14] The manifest file hashes to the same value after the
  branch was rebased onto `main` and landed with this record, and the
  builder's `--check` passes there.
- **Verdict (raw line 4):** `REVISE`. One revise finding (33) and five
  notes (34–38), with no blocking finding (raw line 352).
- **Stopping rule applied.** The owner's direction of 2026-10-14
  (`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`):
  one repair and one review per packet; anything still `REVISE` goes to the
  owner with its findings, not into another loop. Round 4's findings were
  repaired once and round 5 is the one review. Round 5 is not notes-only.
  So:
  - **The package is not repaired again.** The only edits after the round
    are dated status marks at the sentences that said round 5 was pending.
    *(Marked 2026-10-14, later the same day: superseded. On the owner's
    further direction that day, relayed by the lead session, the package
    was repaired once more; see "Repairs, 2026-10-14 (cycle 2)".)*
  - **No round 6 is dispatched.** *(Marked 2026-10-14, cycle 2: round 6 is
    briefed in `REVIEW-BRIEF.md` §"Round 6"; the repair lane dispatched
    nothing.)*
  - **The review has not cleared.** This version is not offered for
    sign-off. It goes to the owner as register row P-84, with the six
    findings below open. *(Marked 2026-10-14, cycle 2: still not cleared
    and not offered; the six findings are repaired, unconfirmed pending
    round 6.)* *(Marked 2026-10-14, round 6: round 6 returned `REVISE`,
    so the bytes stay uncleared; see `ROUND-6-DISPOSITIONS.md`.)*
  - This record recommends nothing on Questions 1 and 2. *(Marked
    2026-10-14, cycle 2: Question 2 has since been answered by
    `../../../decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md`;
    this record still recommends nothing on Question 1.)*

Reviewed record: docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-5-RAW.md

## Round-4 repairs, as the reviewer judged them

Raw lines 137–174: findings 27, 28, 29, 31 and 32 repaired; 26 partly
repaired (its remainder is finding 33); 30 repaired for every probe round 4
reported, with new repair text partly unguarded (finding 37).

## Findings, open

*(Marked 2026-10-14, cycle 2: the heading and each "Open." below are as
classified after round 5; every finding was repaired once later the same
day, and the repairs are unconfirmed pending round 6.)* *(Marked
2026-10-14, round 6: round 6 returned `REVISE`; see
`ROUND-6-DISPOSITIONS.md`.)*

### 33 — POC-REQ-054 attributes elements, not machine-answer records, to subjects (revise)

**Open.** Raw line 178. *Repaired 2026-10-14 (cycle 2), below.* The repair widened the sweep population to
machine-answer records, but the oracle-independence attribution rule, the
ownership test and the equality limb still speak of elements only, while
the RFC6-3 and RFC6-1 covered rows and `SEMANTIC-DELTA.md` §1 say records
are attributed too. Criteria 2 and 3 are not met. The raw's repair: extend
the three sentences to "each element and record … by the source record it
renders or answers for", with a required phrase, or narrow both covered
rows and add an Unknown row for the machine-answer limb.

### 34 — POC-REQ-054's first scenario states a narrower denominator than its sweep (note)

**Open.** Raw line 236. *Repaired 2026-10-14 (cycle 2), below.* Use one denominator phrase in the sweep and the
scenario.

### 35 — "never green" is read as visual distinctness; RFC2-25's table uses "green" as a positive status (note)

**Open.** Raw line 247. *Repaired 2026-10-14 (cycle 2), below.* The covered row rests on a reading; the raw
suggests an `[Inferred]` tag on the row or a sentence in the delta.

### 36 — the ownership procedure's key term is not defined per source (note)

**Open.** Raw line 264. *Repaired 2026-10-14 (cycle 2), below.* A sentence saying the per-source identifier field
is fixed by the slice that lands the form would close it.

### 37 — the round-4 repair text is partly outside the builder's phrase guards (note)

**Open.** Raw line 283. *Repaired 2026-10-14 (cycle 2), below.* Seven of the reviewer's ten probes survived the
structure gate; the manifest digest freezes the reviewed bytes, and
criterion 5 is met.

### 38 — the sibling-package regeneration step sits in the ledger, not in the delta's residual list (note)

**Open.** Raw line 299. *Repaired 2026-10-14 (cycle 2), below.* A fifth residual line in the delta would put it
where the signing change will look.

## Repairs, 2026-10-14 (cycle 2)

**Warrant.** The owner's direction of 2026-10-14, given in the lead session
and relayed to this repair lane: repair every round-5 finding, notes
included, then one fresh review under the same stopping rule (a notes-only
round clears; a `REVISE` goes back to the owner) [Observed: as relayed;
not yet recorded under `decisions/`]. The lane repaired, dispatched no
review, and signed and recorded nothing.

**Round-5 findings repaired once on 2026-10-14, unconfirmed pending round
6.** *(Marked 2026-10-14, round 6: round 6 has run and returned `REVISE`;
see `ROUND-6-DISPOSITIONS.md`.)* Proposed bytes changed only through the four patches under
`proposed/`; the dependency file was regenerated by
`scripts/build_three_surface_poc_spec_dependencies.py` over the proposed
spec, and the manifest by the builder's `--write`.

| Finding | Repair | Where |
|---|---|---|
| 33 (revise) | POC-REQ-054's oracle independence now reads "It attributes each element and record to its subject by the source record it renders or answers for, never by the identity it carries"; its ownership test reads "the source record that an element renders or a record answers for"; the equality limb is "per-element and per-record identity equality". An element or record carrying a subject identity that renders or answers for no source record is attributed to no subject, and a new limb counts it in the Observable, the decision rule ("Zero elements or records carrying a subject identity that are attributed to no subject") and the Falsifier: this closes the phantom-subject path raw lines 198–212 describe. The RFC6-1 and RFC6-3 covered rows now cite that attribution in the requirement's words; neither claims more. `SEMANTIC-DELTA.md` §1's sentence, true of the delta and not of the requirement before, is marked and now matches. The option taken is the raw's first (extend, with phrase guards), not narrowing the rows. | `proposed/spec.md.patch`; `proposed/CONTRACT-COVERAGE.md.patch`; `SEMANTIC-DELTA.md` §1; builder `REQUIRED_PHRASES` and `COVERAGE_ROW_PHRASES` |
| 34 (note) | The first scenario now reports "the number of identities that appear in more than one of the surfaces and the machine answer as its denominator", the sweep's phrase. | `proposed/spec.md.patch`; builder phrase "scenario denominator equals the sweep's" |
| 35 (note) | The RFC2-25 "never green" covered row now carries an `[Inferred]` tag naming its reading ("rendered unlike Observed") and saying that on the reading "never rendered as a positive status" the limb is the Unknown positive-status row. `SEMANTIC-DELTA.md` §3 says the same and adds that POC-REQ-060's oracle does not check the declared Inferred encoding against a positive treatment. No requirement text changed for this finding. | `proposed/CONTRACT-COVERAGE.md.patch`; `SEMANTIC-DELTA.md` §3; builder `COVERAGE_ROW_PHRASES` |
| 36 (note) | POC-REQ-054's oracle independence now says which field of a source's record format is the identifier "is declared, per source, by the implementation slice that lands the identity's form"; until it is declared for a source, that source's subjects are of Unknown ownership and are reported Unknown for the equality limb, never as owned, unowned or passing, while the consistency limb, links and slots are still checked. The Observable carries the Unknown report. `SEMANTIC-DELTA.md` §1 and the packet's Departure 1 tell the reader; the delta labels the code-region consequence `[Inferred]`. No covered row's claim widened: the RFC6-1 covered row's equality limb was already limited to owned subjects. | `proposed/spec.md.patch`; `SEMANTIC-DELTA.md` §1; `OWNER-DECISION-PACKET.md` Departure 1 |
| 37 (note) | Every probe the raw reported as surviving (raw lines 124–133, seven of ten) now has a phrase guard and a selftest mutant, and so does every sentence this cycle added: 13 POC-REQ-054 and POC-REQ-060 phrases in `REQUIRED_PHRASES`, three row guards in the new `COVERAGE_ROW_PHRASES`, and 16 new mutants (32 → 48), each failing on its own predicate. The one existing phrase that the repair rewrapped ("zero subjects whose elements or records …", now lower case) and its mutant were updated. | `scripts/build_three_surface_poc_identity_amendment.py` |
| 38 (note) | `SEMANTIC-DELTA.md` §"Residuals the sign-off change must carry" now has a fifth item: the mutually exclusive governing-intent sibling (P-100), and that whichever is signed second is regenerated with `--write` over the first's applied bytes and reviewed again. | `SEMANTIC-DELTA.md` residual 5 |

**Also carried in this cycle, not a round-5 finding.**

- **Regeneration over `main`.** [Observed 2026-10-14] After the P-97
  block-provenance sign-off (`7f43802f`) moved the signed spec and its
  dependency file, this builder's `--check` failed on `main`:
  "GOVERNING-DEPENDENCIES.md.patch does not apply". The other three
  patches still applied (the spec patch at a 54-line offset). All four
  patches were re-emitted over the current signed bytes; `proposal.md.patch`
  came out byte-identical.
- **Question 2.** `OWNER-DECISION-PACKET.md` Question 2 is marked answered
  by `../../../decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md`,
  with the old text kept; residual 1 in the delta and the ledger's sibling
  note are marked at the sentence. Question 1 stays open.
- **No owner question added.** No repair needed a choice from the owner.

**Mechanics** [Observed 2026-10-14, in the repair worktree before commit]:
the builder's `--check` passes ("26 requirements, Part A 78 clauses over
139 rows"); `--selftest` passes ("48 structure mutants, patch drift,
manifest order and subject drift all fail closed on their own
predicates"). The Part A totals (103 covered, 36 Unknown) and family table
are unchanged, since no row was added or removed. The reviewer recomputes
the manifest file's digest at the reviewed commit (`REVIEW-BRIEF.md`
§"Round 6").
