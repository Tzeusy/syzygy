> # Record beside the package — not authority, binds nothing
>
> Dispositions the findings of the second fresh-context review of the PWB
> tree-framing amendment. It is not a package artifact: the manifest does
> not hash it and no builder reads it. It offers nothing and performs no act
> (VIS-4).

# Round 2 dispositions — PWB tree-framing amendment

- **Reviewed commit:** `8e45097e2af3be8bbff929c717eb3eefae59d608`.
- **Verdict (raw line 5, the fourth non-blank line):** `CONFIRM WITH
  EXCEPTIONS`; five findings, all notes, counted from the raw's finding
  headings.
- **Effect:** a notes-only round clears the bytes it read. The package and
  its builder are unchanged since the reviewed commit.

Reviewed record: docs/reviews/R-PWB-TREE-FRAMING-AMENDMENT-2-RAW.md

## Dispositions

Findings 1, 2 and 5 are totality gaps the amended text leaves to the
implementer. They are carried to the implementation bead `syzygy-73e.20`
with the fail-closed reading VIS-2 gives each, and to the next amendment of
PWB-REQ-014:

### 1 — an opening over a group with no rendered child has no weakest label

Carried. Implementation reading: an empty group's opening is Unknown.

### 2 — the followed review record has no stated failure path

Carried. Implementation reading: a missing, unreadable or mis-hashing
record is disclosed as Unknown on the page, never read as "nothing owed".

### 3 — openings carry only a label; the `project-fact` role name is shared

Accepted as a note. The copy role (PWB-REQ-012) and the claim role
(PWB-REQ-014) are distinct vocabularies; the implementation names them
apart in code.

### 4 — added verification bullets are pinned only by the manifest digest

Accepted as a note. The manifest binds the bytes to this review (rule 10).
Pinned fragments per added bullet are left for a later builder change.

### 5 — a supported edge whose endpoint has no claim has no stated reason

Carried. Implementation reading: such an edge is not drawn and is disclosed
with `missing-declaration`. Today's model holds no such edge.
