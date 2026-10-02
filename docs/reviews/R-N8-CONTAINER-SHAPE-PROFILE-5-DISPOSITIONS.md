# R-N8-5 dispositions — container-shape profile amendment, confirmation round 5

> **Candidate record — binds nothing.** This page dispositions the notes of
> one review. It performs no act, issues no direction and edits no reviewed
> byte.

**Review:** `R-N8-CONTAINER-SHAPE-PROFILE-5-RAW.md`, retained verbatim beside
this page. Its verdict line (line 2) reads `Verdict: CONFIRM WITH
EXCEPTIONS`, and its severity line (line 283) records no revise-severity
finding and five notes, N-m to N-q (raw lines 99, 118, 144, 161 and 177).

**Subject:** the candidate package
`.syzygy/governance/contracts/candidates/pwb-container-shape-profile-amendment/`
and `scripts/build_pwb_container_shape_profile_amendment.py`, as reviewed at
commit `51b82b6`. The review binds the package by the manifest file digest in
the raw's head (line 4), the act argument the package's REVIEW-BRIEF
predicate names.

**Why nothing here edits the package or the builder.** Under the 2026-09-26
sitting rule (`POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1), a notes-only
CONFIRM WITH EXCEPTIONS clears the exact bytes the review read. Any edit to
them retires that review (rule 10). This commit adds only this page, the raw
and the `docs/README.md` row and count; the package and builder have no diff
against `51b82b6` [Observed: `git diff --stat 51b82b6 HEAD`].

**Read the packet with N-o and N-p in hand.** Both touch what the owner
reads, not what the amendment says.

| Note | Summary | Disposition |
|---|---|---|
| N-m | Three calls in `check()` (`population_findings`, `structure_findings`, `composition_findings`) are unpinned by the selftest; removing any one survives it. The live code calls all three. | **Routed to `syzygy-u05.18`.** Selftest rigor only; `--check` behaves correctly at these bytes. |
| N-n | "A change to any file no patch is declared to change fails `--check`" (SEMANTIC-DELTA:26-28, IMPACT-LEDGER:112) is broader than the check: a patch hunk creating a new file passes. True for the manifest subjects. | **Routed to `syzygy-u05.18`.** A recorder applying the patches must apply only the declared ones. |
| N-o | Packet :100-101 ("Already ruled") still says there is one such act and `syzygy-dov.24` drafts it, contradicting question 7, which leaves that identification unsettled. | **Routed to `syzygy-u05.18`.** Question 7 governs: whether dov.24's act is the registry act P-74 Q2 ruled is an open owner question. |
| N-p | Question 7's second part gives option (a) only its benefit and option (b) only its cost, and omits a third arm: the registry act lands without Butlers' rows. The packet recommends neither. | **Routed to `syzygy-u05.18`.** Framing only; the third arm is an answer the owner may give. |
| N-q | The window disclosure names one falsifier clause, but the round-4 N-h clause (a known denominator for a refused or unread Butlers profile) fires in the window too. | **Routed to `syzygy-u05.18`.** |

`syzygy-u05.8` stays open: the owner has not performed or declined the
container-shape profile amendment act.
