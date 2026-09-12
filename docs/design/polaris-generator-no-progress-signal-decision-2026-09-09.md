# Claimed work without a captured progress signal — candidate decision

[Observed] RFC8-13 defines active from a qualifying recent signal,
activity-undetermined from an undeclared bound, and stale-or-dead from a real
last-signal instant older than the bound. RFC4-23 limits progress signals to
branch-tip movement, new commits or PR-state changes. These source clauses remain
unchanged; this note is not an adopted interpretation or semantic amendment.

[Inferred] A generator can have recorded provider responses and saved draft
artifacts while its claimed work has no captured signal of those qualifying
kinds. With an effective bound present, none of the three activity predicates
above describes it. Claim time, a model receipt or a heartbeat cannot be relabelled
as the missing signal. Other states remain available only when their own
predicates independently hold.

## Proposed remedy to review

Extend the activity-undetermined derivation to the activity-assessment case where
no admissible last-progress-signal observation is available, while preserving its
existing missing-bound case. Disclose which prerequisite is absent: bound, signal
or both. This is a proposed semantic change, not a permission to reinterpret the
current accepted row. It would preserve the thirteen-value vocabulary and keep
the value state-local, separate from claim Unknown reasons.

| Input in the activity-assessment branch | Proposed outcome |
|---|---|
| Bound absent/ineffective | Existing activity-undetermined behavior; declare an effective bound |
| Bound effective, no admissible last-signal observation | Proposed activity-undetermined branch; show the missing observation without inventing time or asserting no event ever happened |
| Bound effective, qualifying signal within it | Existing active predicate, with the real signal and bound |
| Bound effective, admissible signal older than it | Existing stale-or-dead with the real last-signal instant |

Independent blocked, ready, review and terminal predicates are not overridden by
this proposal. Provider/stage evidence remains useful as generation progress but
does not become a qualifying worker signal. A lost history source stays explicitly
unavailable; it is not proof the worker never progressed.

An alternative is a new normalized absence value for missing signals. That would
change the closed enum and every consumer's compatibility obligation, so the
existing-value extension is the smaller semantic change to investigate. Neither
alternative is adopted here. If an existing effective mapping can lawfully answer
the concrete case through another predicate, demonstrate that evidence before
commissioning an amendment.

## Required decision work

Review the exact affected clauses and consumer meanings, the mapping's effective
act/version, retrospective evaluation stability, and the missing/expired/invalid
signal counterexamples. Any actual contract amendment must follow the governed
semantic-delta process and preserve prior versions and evaluations. Until that
work is complete, the generator must expose the unresolved conformance case and
cannot claim full normalized-state support. It must not avoid the case by hiding
claimed work or manufacturing scheduler transitions.
