> # Record beside the package — not authority, binds nothing
>
> Dispositions of the first fresh-context review of the PWB opening-index
> amendment package. This record is not a package artifact: the manifest
> does not hash it and no builder reads it. It offers nothing and performs
> no act (VIS-4).

# Round 1 dispositions — PWB opening-index amendment

- **Reviewed commit:** `0241fb835471af3a2ea23119959bdfa34ef14464`.
- **Verdict (raw line 4):** `REVISE`. The review has two revise findings
  (1, 2) and six notes (3–8), with no blocking finding.
- **Stopping rule as applied.** The brief, written before the round, said
  that a non-clearing verdict leaves the package unedited. After the round
  the coordinator directed otherwise for a first-round `REVISE` on a new
  draft: repair once, record each finding and its repair here, and run no
  round 2. That direction was applied; the brief carries a dated note.
- **Status: round 1 `REVISE`, repaired once, unconfirmed; owner decides.**
  No round 2 is dispatched. The repaired bytes are not offered as cleared
  under Scope A; the owner decides between signing, a confirmation round
  and revision (register row P-98).
- **Figures** [Observed]. Re-derived after the repair by
  `scripts/build_pwb_opening_index_amendment.py --check`: 11 proposed
  subjects, 2 patched; 17 requirements and 53 scenarios; `--selftest` 23
  structure mutants, each failing on its own predicate. All 24 orders of
  the four pending PWB spec patches apply to one identical result.

Reviewed record: docs/reviews/R-PWB-OPENING-INDEX-AMENDMENT-1-RAW.md

## Dispositions

### 1 — the word-counting method is not judgment-free (revise)

**Repaired.** The method now counts over the document as the browser holds
it after load, with every `details` in its first-load state. It lists its
exclusions exhaustively: `script`, `style`, `template` and `noscript`;
anything under `hidden`, `aria-hidden="true"`, computed `display: none` or
`visibility: hidden`; a closed `details`' content except its `summary`,
which now counts; and the index and stopping line themselves. An offset is
defined as the number of counted words before the target's first counted
word. The Oracle counts "the document after load", not "the served HTML".
New mutants: closed-details exclusion dropped, offset base dropped.

### 2 — the stopping line has no presence, uniqueness or placement falsifier (revise)

**Repaired.** "Exactly one stopping line SHALL stand immediately after the
first element of the target whose offset is largest". The Oracle requires
exactly one line at that place carrying the largest recomputed offset, and
the Falsifier adds "the stopping line is missing, repeated or misplaced, or
its offset is not the largest". New mutants: uniqueness dropped, placement
falsifier dropped.

### 3 — index targets are prose and have no stated recognizer (note)

**Repaired in part.** A row now routes to its target's heading, or to its
first element when it has none. Oracle independence says targets are
located by a recognizer whose selectors are published with the oracle.
The two narrower targets (`gaps` and the non-goals row) are not widened;
packet question 2 puts them to the owner.

### 4 — copy role and narrative-unit fit not reconciled with PWB-REQ-012 and PWB-REQ-014 (note)

**Repaired.** The requirement now says an unrendered row's text is an
`epistemic-disclosure`, PWB-REQ-012's one entry `scope-instruction` limit
counts only the statement of the POC bound, and the index precedes the
PWB-REQ-014 narrative tree and is not one of its units. Packet question 5
puts both readings to the owner.

### 5 — register rows P-98 and P-99 absent at the reviewed commit (note)

**Resolved outside the package.** [Observed] Both rows were added in a later
commit on this branch, so "P-98 is added by this change" is true of the
change. No package text changed for this finding.

### 6 — pair-checking and "do not overlap" overstate what was checked (note)

**Repaired.** The ledger now says the builder checks this package against
each of the other three, and that all 24 orders were applied to one
identical result. The packet no longer says the changes do not overlap; it
names the design decision and capability row P-85 and P-86 share.

### 7 — replaced lines may lose signed text, and table targets are unpinned (note)

**Repaired, in the shared engine and this builder.** Each `replaced` signed
line must now survive, less its full stop, as the prefix of a proposed line
(`scripts/pwb_requirement_amendment.py`, with a "replaced line truncated"
mutant). The new check found one real case: the repair had rewrapped the
signed falsifier line, and it was rewrapped back. All nine table rows are
now required phrases, with a target-swap mutant.

### 8 — index rows may trip the distinct-name check if both packages are signed (note)

**Repaired.** "A row's accessible name names its question, so it shares no
name with a link to a different place (PWB-REQ-016)." The accessible-name
ledger says so too.
