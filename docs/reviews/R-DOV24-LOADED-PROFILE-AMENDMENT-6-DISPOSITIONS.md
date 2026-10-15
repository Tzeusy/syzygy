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
