# R-DOV27-2 dispositions — response-ceiling reading packet, confirmation round 2

> **Candidate record — binds nothing.** This page dispositions the notes of
> one review. It performs no act, issues no direction and edits no reviewed
> byte.

**Review:** `R-DOV27-RESPONSE-CEILING-PACKET-2-RAW.md`, retained verbatim
beside this page. Its verdict line (line 200) reads `Verdict: CONFIRM WITH
EXCEPTIONS`. It has no revise-severity finding and five notes, N1–N5.

**Subject:** `.syzygy/governance/decisions/POLARIS-RESPONSE-CEILING-READING-DECISION-PACKET.md`
and `scripts/check_polaris_response_ceiling_reading.py`, as reviewed at
commit `36f0aa8`. The review binds the packet by the full SHA-256 in the
raw's head (line 4).

**Why nothing here edits the packet or the checker.** Under the 2026-09-26
sitting rule, a notes-only CONFIRM WITH EXCEPTIONS clears the exact bytes the
review read. Any edit to them retires that review (rule 10). The branch was
rebased onto `66114ac` after the review; the packet's SHA-256 is unchanged by
the rebase and the checker has no diff against `36f0aa8` [Observed:
`sha256sum` and `git diff 36f0aa8 HEAD` on the rebased branch].

| Note | Summary | Disposition |
|---|---|---|
| N1 | The packet labels "applied alone or composed in sequence (the check does both)" `[Observed]`, but C5 composes in path order, where lane B does not apply on top of `.20`, so the check never composed lane B. The reviewer's own run in the ruled order keeps every quote. | **Left in place.** A known packet-text note on cleared bytes. The substantive claim holds by the reviewer's ruled-order run; the wording overstates what the check shows. Recorded here so a reader of the packet does not take the C5 `OK` as covering lane B. |
| N2 | The C3 gate (`direction_permits`) is a substring test: it opens on a decline that quotes the reading or mentions gzip as not permitted, does not scan subdirectories, has no narrowing form and does not scope the coding. One case closes it spuriously, which fails closed. | **Routed to `syzygy-dov.31`.** Not fixed on #117. The owner direction and the slice-4b review remain the real gate. |
| N3 | Widened sweep terms are not individually pinned by selftest lines, paragraph-2 scoping is unpinned, and a `compression` import, a `'br'` literal and `.js`/`.mjs` sources lie outside the sweep, so "in any form" overstates it. | **Routed to `syzygy-dov.31`.** Not fixed on #117. |
| N4 | The credential bullet does not say whether compressing Butlers-derived text crosses the continuation act's "security, privacy, or retention posture" trigger; only the registry-envelope trigger is argued. | **Routed to `syzygy-dov.31`** as a question to settle before any later revision is offered: state the drafter's view with its reason, or add an owner question with a fail-closed default. Until then the packet is silent on that trigger, and silence does not answer it. |
| N5 | "The shared weak ETag is the drafter's choice, listed below" points the wrong way; the list is above. | **Left in place.** An editorial slip on cleared bytes. The list is item 4 of "What is the drafter's and not yours". |

`syzygy-dov.27` stays open: the owner has not issued the direction.
