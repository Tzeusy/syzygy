# Fresh-context review brief — general trusted-bootstrap authorization

> **Review input, not authority.** Review the exact transaction manifest and
> its bound subjects at the supplied frozen commit. Do not infer a desired
> verdict from the authoring history or from earlier reviews.

## Subject

- Baseline: `20e5b6e7c512436b67dec9eb05e0ee926096a7b5`.
- Primary change:
  `GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-SEMANTIC-DELTA.md` and the exact
  subjects bound by `TRANSACTION-MANIFEST.txt`.
- Downstream consistency: candidate RFC 0010, the current routing/policy
  summaries, and the performed-wave manifest/checking repair in
  `build_active_manifest.py` and `check_governance.py`.
- Historical Wave A/B manifests, performed act records, raw reviews and
  superseded candidates are evidence only and must not be rewritten to current
  semantics.

## Governing references

- Doctrine: VIS-1, VIS-2, VIS-4, VIS-5, VIS-7; SEC-2 through SEC-5;
  `trust-and-evidence.md` warrant/evidence and trust-floor rules.
- Contract: RFC3-16(a), RFC3-16(b), RFC3-16(c), plus every direct consumer
  named in the semantic delta.
- Craft: CC-REV-1, CC-REV-2, CC-REV-4, CC-REV-6 and CC-REV-7.
- Owner warrants:
  `GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-DIR-2026-08-31` and
  `BOUNDED-MISSION-DOCTRINE-INTERPRETATION-2026-08-31`.

## Acceptance criteria

1. State (1) and state (2) remain the only provenance states. Both may carry
   an effective real human owner act; only state (2) supports the claim
   independently verified.
2. State (1) is explicit, exact-digest and scope bound, and visibly
   uncorrelated. A file, stored name, machine submission or agent assertion is
   never by itself a human act.
3. Failed, unavailable or indeterminate A1 correlation never creates state
   (1) or silently downgrades a record claiming state (2).
4. Missing, invalid, stale, revoked, superseded, wrong-scope, unattributed,
   non-human or digest-mismatched acts fail closed. Every effect-specific gate
   remains conjunctive.
5. Owner acts are warrants, never evidence that an effect succeeded, a claim
   is true, a release occurred or recovery worked.
6. The amendment creates no deployment/recovery authority, consent, policy
   approval, registry adoption, execution approval, release, mission, or
   implementation authorization.
7. RFC 0010 remains candidate and non-operative. The doctrine ruling satisfies
   RFC10-24's owner-ruling alternative but no independent mission gate.
8. All nine accepted OpenSpec phase rules use one consequence: a valid state
   (1) or state (2) act can carry the reviewed N/A judgment with state shown;
   absent or invalid acts map nothing and leave the consequence Unknown.
9. Installed RFC 0001-0009 bytes equal their candidate mirrors. Historical
   performed Wave A/B manifests retain their exact act-time bytes and digests;
   current active and unperformed-wave manifests track current candidate bytes.
10. Every invalidated signed coverage artifact and the in-force CC-SPEC policy
    is in the same exact-digest owner transaction. PWB-REQ-005 and PWB-REQ-022
    are honestly labeled as deliberately stricter state-(2)-only behavior.
11. The 204-file impact population is complete by two independent baseline
    readings, and every member has one disposition.
12. The five transaction act rows have precise subjects, scopes and
    supersession behavior. A partial ceremony performs none of them.

## Reviewer output

Lead with exactly one verdict: `CONFIRM`, `CONFIRM WITH EXCEPTIONS`, `REVISE`,
or `REJECT`. Then list findings with artifact and line evidence, identifying
which acceptance criterion or governing rule is affected. Distinguish blockers
from non-blocking observations. Restate the resulting authority and
non-authority boundaries in plain language as the VIS-3 fresh-reader check.
