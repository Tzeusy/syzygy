# P-114 round 2 — exact bytes cleared, three notes retained

[Observed 2026-10-20] The fresh round-2 raw at
`docs/reviews/R-PWB-REGISTRY-MACHINE-CEILING-AMENDMENT-2-RAW.md` says
`CONFIRM WITH EXCEPTIONS` (line 4), with three notes and no revise finding,
over the source lane's `7d7c3a3e` commit. Its owner-packet problem scope and
recommendation each say `Pass` (the raw's Owner-decision packet checks).
Under the owner's notes-only stopping rule, this clears the exact reviewed
proposal; it performs no sign-off and authorizes no implementation. The
reviewed delta, packet, brief, ledger, patch, manifest, builder and incident
record are unchanged. This sibling records the notes; it does not repair
those frozen bytes.

1. **Present the incident accurately.** The packet's opening refusal is the
   measured pre-revert incident. PR #474 reverted P-100; the later private
   measurement in `syzygy-59s5` records HTTP 200. No current outage or live
   service is established by the round-2 review. Offer the decision with
   that distinction beside it, and describe 72 days as an incident-rate
   extrapolation. The local owner packet does so. No new runtime claim is
   inferred from this review.
2. **Keep verification gates distinct.** The builder's static scanner admits
   the three counterexamples retained in the raw and its independent probe
   record. A builder pass is neither proof of a valid evaluated TypeScript
   constant nor a performed act or an admitted read. The authorized install
   must separately exercise the registry-parity test, dedicated recorder
   checks and full authority evaluation against the signed entry. Its
   implementation report must identify which gate proves which predicate.
   No TypeScript parser or additional implementation scope is authorized by
   this note.
3. **Record unaffected readers.** Three further source-path consumers read
   only `contractVersion`: `scripts/build_public_git_source_acquisition_local_agent.py`,
   `scripts/build_public_admission_registry_entries.py` and
   `scripts/build_provider_route_messages_api_entry.py`. The one-leaf patch
   leaves their consumed field unchanged, so these require no successor or
   edit. Read A2 together with this supplement rather than calling its
   original reader list complete.

[Observed] The raw discloses an interrupted Vitest corroboration attempt;
it is not a completed verification result. It reports the completed
canonical governance block separately. The historical dry-run command's
non-browser denominator was not confirmed by this review; any install run
must state its actual command and population, including browser cases or
explicit exclusions.

[Unknown] Owner sign-off, narrow implementation authorization and post-change
runtime behavior remain pending. P-115 is not drafted or signed here.
