# R-DOV24-4 dispositions — loaded-profile registry amendment, confirmation round 4

> **Candidate record — binds nothing.** This page dispositions the notes of
> one review. It performs no act, issues no direction and edits no reviewed
> byte.

**Review:** `R-DOV24-LOADED-PROFILE-AMENDMENT-4-RAW.md`, retained verbatim
beside this page. Its verdict line (line 2) reads `Verdict: CONFIRM WITH
EXCEPTIONS`. It has no revise-severity finding and six notes, N-A–N-F.

**Subject:** the candidate package
`.syzygy/governance/contracts/candidates/pwb-registry-loaded-profile-amendment/`
and `scripts/build_pwb_registry_loaded_profile_amendment.py`, as reviewed at
commit `1d5966c`. The review binds the package by the manifest row digest in
the raw's head (line 4), the act argument the package's REVIEW-BRIEF
predicate names.

**Why nothing here edits the package or the builder.** Under the 2026-09-26
sitting rule (`POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1), a notes-only
CONFIRM WITH EXCEPTIONS clears the exact bytes the review read. Any edit to
them retires that review (rule 10). This commit adds only this page, the raw
and the `docs/README.md` row and count; the package and builder have no diff
against `1d5966c` [Observed: `git diff --stat 1d5966c HEAD`].

| Note | Summary | Disposition |
|---|---|---|
| N-A | The inserted block is checked only after parsing, so a shadowed duplicate key passes (builder:424–457). The current bytes carry no duplicate key. | **Routed to `syzygy-dov.32`.** Not fixed on #123. The reviewed bytes are free of the defect; the gap is in what `--check` would catch in a later revision. |
| N-B | Three item-key sentences omit the trim the code applies in `declarationKey` and the topology label. | **Routed to `syzygy-dov.32`.** Shared verbatim with N8 (PR #124); the repair lands in both packages together so the text stays identical. |
| N-C | `sharedReadingRules` does not state that CRLF line endings are stripped. | **Routed to `syzygy-dov.32`**, with N-B. |
| N-D | LINK accepts one or more spaces or tabs before a title; the sentence says "a space or tab". | **Routed to `syzygy-dov.32`**, with N-B. |
| N-E | `--selftest` still passes with the new `[[other]]` probe or the link-before-table probe removed; only the unpinned probe count of 123 shows it. | **Routed to `syzygy-dov.32`.** |
| N-F | `--selftest` has no mutant for a changed base line next to the insertion (builder mutant B2 survives); the live check does kill such a line. | **Routed to `syzygy-dov.32`.** |

`syzygy-dov.24` stays open: the owner has not performed or declined the
registry-entry amendment act.
