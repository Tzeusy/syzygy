# R-DOV24-6 — dispositions (classification only)

Raw: `R-DOV24-LOADED-PROFILE-AMENDMENT-6-RAW.md`, verdict `REVISE` (line 2
of the raw), over `fa9bc47e` (main), manifest row as in the raw's head.

On the lead session's process decision of 2026-10-15, made under the
owner's autonomy direction, a round-6 REVISE is classified and **nothing
is repaired**. The package, the builder and the patch are unedited. Under
the stopping rule the bytes stay **unconfirmed**, and the act is not
offered. Register row P-112 is marked with this outcome.

The reviewer found every round-5 repair resolved against the bytes (the
raw's criteria 1–3 and 5).

| Finding | Severity | Classification |
|---|---|---|
| 1 — P-112 says "nine open questions: the eight original ones … and" the ordering question; the packet has nine numbered questions plus the ordering question in its rebase note (ten), and question 9 (root independence vs M15) is left out | revise | Register-row wording, not package bytes. Marked where it stands in P-112 and not rewritten. |
| 2 — `apply`'s `if refusal:` → `if False:` survives both modes: the selftest exercises `apply_refusal`, never `apply` | note | Builder test gap. Not repaired; carried to `syzygy-dov.32` with the round-4 notes. |
| 3 — "no round 6 is dispatched" is now false (packet :15 and :412, delta :293, brief :13, P-112) | note | Marked in P-112 only. The package sentences are left as they are, because this round edits no package bytes. A future repair marks them in place. |
| 4 — the entry's `governingBehaviorContract` pin is four PWB-spec sign-offs behind the current `spec.md`; the ordering question does not say that performing this act first re-adopts that stale pin | note | Bears on the ordering. The lead session's process decision of 2026-10-15 (P-112) is that this act goes first and the P-95 redraft rebases over it. The re-pin of `governingBehaviorContract` is P-95's job either way. Recorded in P-112. |

## Lead disposition, 2026-10-15 (later the same day)

This section supersedes the "nothing is repaired … stay unconfirmed …
not offered" reading above. That text is kept as written.

The raw's verdict stays `REVISE` (raw line 2), copied exactly. The
disposition below is the **lead session's**, recorded as the lead's under
the owner's autonomy direction; the reviewer did not give it, and neither
did the owner.

- Finding 1, the only revise-level finding, is in register row P-112,
  outside the package bytes the round reviewed. It is **repaired outside
  the package**, by a dated mark in P-112 that corrects the count to ten
  questions and names question 9.
- Findings 2, 3 and 4 are notes on the package.
- With the revise finding repaired outside the package, the lead
  dispositions the package bytes at `fa9bc47e` as **cleared, notes only,
  under the owner's 2026-09-26 stopping rule**. The package bytes are not
  edited.

The cleared subject is the package at `fa9bc47e`, identified by git blob
ids:

| File | Blob |
|---|---|
| `OWNER-DECISION-PACKET.md` | `ca063494a846dc2452c7acb03fb29bf9ee39a249` |
| `SEMANTIC-DELTA.md` | `00930256140e7d0c5fafff75b9c87a0cf467964a` |
| `IMPACT-LEDGER.md` | `a817b388181d8cfc0167f46e8350a4266f6ab8d9` |
| `REVIEW-BRIEF.md` | `45e99df5c90eaeb0b96cda7deb9bad4c11d7074a` |
| `PWB-LOADED-PROFILE-AMENDMENT-MANIFEST.txt` | `c38b720a3d6652c051d9482fc72676c038357a03` |
| `proposed/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json.patch` | `71cc703e9dd343b76417be510dfe3e207b1277ba` |
| `scripts/build_pwb_registry_loaded_profile_amendment.py` | `4770f885f47db6598602e56cb61f2dbcfdf282cd` |

The manifest row is as in the raw's head. [Observed:
`git diff --stat fa9bc47e origin/main` over these paths and the subject
is empty at this disposition's commit.]

Each note's handling:
- **Finding 2** (the `apply` call-site mutant) is added to
  `syzygy-dov.32`.
- **Finding 3** (the package's "no round 6" sentences): those sentences
  stay unmarked, because the cleared bytes are not edited. P-112 is the
  current record.
- **Finding 4** (the `governingBehaviorContract` pin lags the current
  `spec.md`) **must be resolved or disclosed before the owner performs the
  act**. It is disclosed in P-112. Resolution is the P-95 redraft, which
  rebases over this package.

P-112 is now ready for the owner's decision. Nothing is performed,
recorded or labelled accepted.
