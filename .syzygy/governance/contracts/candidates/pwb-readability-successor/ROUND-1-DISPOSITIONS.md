> # Record beside the package — not authority, binds nothing
>
> Dispositions the findings of the first fresh-context review of the PWB
> readability successor package. It is not a package artifact: the manifest
> does not hash it and no builder reads it. It offers nothing and performs no
> act (VIS-4).

# Round 1 dispositions — PWB readability successor

- **Reviewed commit:** `934e9c9fcac9714e9de5e40db5c3697e2d58ff55`.
- **Verdict (raw line 4):** `CONFIRM WITH EXCEPTIONS`; three findings, all
  notes, none revise or blocking, counted from the raw's finding headings.
- **Effect:** a notes-only round clears the bytes it read. The package is not
  edited by this record; editing a reviewed byte would retire the clearance.
  The package bytes at the reviewed commit equal the bytes at the commit this
  record lands on (`git diff 934e9c9` over the package directory is empty
  before this file is added).

Reviewed record: docs/reviews/R-PWB-READABILITY-SUCCESSOR-1-RAW.md

## Dispositions

### 1 — the proposal's inert-code sentence drops "alone"

Accepted and disclosed. The proposed `proposal.md` says markup-like examples
"do not make a source active content", where PWB-REQ-006 "Inert code
contexts" says they "SHALL NOT alone cause active-content exclusion". The
proposal is non-normative and the specification governs, so behavior is
unchanged. Reader note for the sign-off: read the proposal sentence with
"alone"; the semantic map's "preserved" for that unit is better read as
"clarified". A later readability pass may restore the word.

### 2 — "repository-contained" dropped from the same bullet

Accepted and disclosed, with finding 1. Containment is stated in full by
PWB-REQ-006 "Containment"; the proposal bullet implies it through "no
symlink or submodule escape".

### 3 — a patch tail edit that leaves the proposed bytes unchanged passes `--check`

Accepted as a note. The manifest hashes proposed bytes, not patch files, and
the recorder re-applies every patch and re-proves every row at sign-off, so
no signed byte can drift through it. No builder change in this round.
