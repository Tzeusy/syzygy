> **Candidate — binds nothing.** Notes record for review round 5. A note
> record performs no act. `SEMANTIC-DELTA.md` stays exactly as reviewed.

# Round 5 notes — DOSSIER-CLI-RUNNER-1

Raw: `docs/reviews/R-DOSSIER-CLI-SUBPROCESS-5-RAW.md`, verdict
`CONFIRM WITH EXCEPTIONS` (line 4), over commit
`3fd1837783ea52cbc4305dd0e0f128fbdb9d15fb`. The subject digest is the one in
the raw's head (line 3); this record does not copy it. Counts: 0 revise and 5
notes. Round-4 items 1 to 4 are closed, and item 5 (Q2) was answered by the
owner and is written faithfully (raw line 125).

The owner's 2026-09-26 stopping rule for repair-review loops says a notes-only round clears its
bytes, and its notes go in a sibling record. This round raised notes only,
so the reviewed bytes of `SEMANTIC-DELTA.md` are **cleared** and are **not
edited**. P-111 Q1, the version-tag sign-off with the one-command-run change,
is now owner-ready.

Some of these notes are wording gaps, so they ride with the text. When the
delta is folded into `openspec/changes/polaris-dossier-one-command-run/`
(`syzygy-zwja`), the fold-in carries the repairs below. That revision is
reviewed with the change, as the delta's migration plan says.

| # | Class | Carried to the fold-in |
|---|---|---|
| 1 | note | Widen the managed-settings scenario's WHEN clause to add "or authenticates the tool by any means other than its own credential file, even for the declared provider". The SHALL text, the Case and the Falsifier already carry this. |
| 2 | note | The login check runs in the session's view and environment and is recorded. A tool with no login-status command counts as "the check cannot be made", and the run is refused. |
| 3 | note | Add "or the list omits or mislabels a present class" to the Falsifier, with the expected class set from the seeded clone written into the Oracle. Say that the present-class list covers the pinned tree only. |
| 4 | note | The Downstream fold-in bullet should name all three warrant decision IDs and record the observed non-match against `WARRANT_FAMILIES` in `polaris-authority-sweep.test.ts`. The test's families must admit these IDs before the fold-in lands. |
| 5 | note | Refresh the "Change class" summary for the failure modes added in rounds 3 and 4. |

The reviewer's judgement (raw lines 121–123) is that none of the five
reopens an egress route or a fail-open arm.
