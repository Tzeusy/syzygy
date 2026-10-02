> # Record beside the reconciliation — not authority, binds nothing
>
> Dispositions the findings of the exact-head review of the spec-readability
> reconciliation (`syzygy-73e.5.6`, acceptance criterion 7). The checker does
> not read this file and `census.json` does not hash it.

# Round 1 dispositions — spec-readability reconciliation

- **Reviewed commit:** `4b289382601b168cfe8c1ce878a37e96d1ac6af4`.
- **Verdict (raw line 4):** `CONFIRM WITH EXCEPTIONS`; three findings, all
  notes, counted from the raw's finding headings. The raw confirms semantic,
  act and denominator parity at that head.
- **Effect:** a notes-only round clears the bytes it read. The record
  directory (other than this file), `scripts/check_spec_reconciliation.py`
  and `openspec/README.md` are unchanged since the reviewed commit.

Reviewed record: docs/reviews/R-SPEC-READABILITY-RECONCILIATION-1-RAW.md

## Dispositions

### 1 — the `openspec/README.md` edit exceeds the cited direction

Owner acknowledged, 2026-10-02. Asked whether to acknowledge the edit as a
route-page currency repair or revert the page, the owner selected
"Acknowledge (Recommended)". The edit stands as a currency repair of an
unbound navigation page; it is not a use of the 2026-09-28 restyle arm, and
this record, not the README's §4 wording, is the account of its authority.

### 2 — a green summary line sits beside unresolved Unknowns

Accepted as a note. The two report-only WARN rows (`syzygy-jloi`,
`syzygy-c51h`) are labelled Unknown in the same output and in §7 of the
record. A later edit to the checker may print the WARN count in the summary.

### 3 — wording drift in two places

Accepted as a note. The approval-check failure message is "owner argument
does not match exact offer bytes"; the record's paraphrase names the same
cause. The understanding row's "seven … and adds two" is a checkable count on
a navigation page. Neither is edited, so the reviewed bytes stay cleared.
