# Owner decision packet — missing effective currency bound outside freshness

> **Inert draft.** This packet performs nothing. It records no act,
> authorizes no implementation and changes no signed byte. A commit, review,
> merged pull request, passing check, silence or general approval performs no
> act. The phrase and digest below are retained only so governance checks can
> detect drift; they are not offered until repaired exact bytes pass a fresh
> independent review.

Date: 2026-09-22. Gate bead: `syzygy-dov.20`.

Warrant: your 2026-09-21 P-69 arm B/Q7a direction — disclose a missing
RFC2-9 bound outside the freshness slot, keep the claim Unknown, and prepare a
CC-REV-2 scenario to PWB-REQ-007 behind its own sign-off and act. That ruling
is direction to draft, not an act. No act is offered here.

Manifest: `PWB-MISSING-CURRENCY-DISCLOSURE-MANIFEST.txt`, eleven rows over the
closed PWB behavior subject. Six rows hash proposed bytes and five current
bytes.

Manifest SHA-256:
`cb73f2294ee2773391371d09f1ce916afe2c56ba270e4557af8e69284bdbea83`

The builder writes this digest. Any patch, manifest or subject change retires
the argument and requires regeneration plus exact-byte review.

## What a reviewed successor would offer

One Normative PWB amendment, despite the ruling's "clarification scenario"
name:

- a class with no effective owner-act-provenance currency bound remains
  `Unknown` with primary reason `no-currency-bound-declared` and exact route
  `Declare the bound in quality policy`;
- the missing-bound condition is a named expandable fact of the render outside
  the freshness slot;
- none of `fresh`, `stale`, `broken`, `superseded` or a fifth value is
  fabricated for that condition;
- every other tuple field remains, and no aggregate absorbs the claim into a
  current/favourable value, drops its primary reason count or hides its route;
- proposal and coverage artifacts move in the same logical change, including
  five newly honest `unknown-uncovered` contract consequences.

The independent reviewer is asked explicitly to confirm or contradict the
Normative classification. A classification of Clarifying would require a
finding explaining how the compliance population does not change.

## Not yet offered: the sign-off phrase

The behavior act phrase for this manifest would be:

`SIGN OFF PWB MISSING-CURRENCY DISCLOSURE SCENARIO: cb73f2294ee2773391371d09f1ce916afe2c56ba270e4557af8e69284bdbea83`

It is registered so governance checks see it go stale, but it is **not
offered**: Review 1 returned `REVISE`, and the repaired exact bytes have not
received fresh-context confirmation. If you reply with this phrase now,
nothing is performed. A future recorder must reject a digest that differs from
the manifest then present and must prove each manifest row against the
post-apply tree.

## What this act would not do

- It would not amend RFC2-9, RFC2-10, RFC6-14, RFC6-17, RFC7-16, RFC7-33,
  CAP1-REQ-062, doctrine, policy, topology, consent or registry values.
- It would not accept the `.18` registry checkpoint or any of its thirteen
  proposed bounds.
- It would not continue implementation across the registry escalation trigger.
- It would not authorize M2 slice 5, wire `assessCurrency`, render the route,
  alter a tuple, or change an aggregate.
- It would not decide the order of another PWB successor; the adoption change
  records the chain position.

## Owner-visible consequences

1. Five accepted-contract consequences become honestly `unknown-uncovered` in
   the PWB matrix. This act changes the PWB specification; it does not weaken
   those contracts or authorize implementation across the gaps.
2. The observer-registry and secret-policy candidates both pin the predecessor
   `spec.md` digest. An adopted PWB successor stales both pins. This package
   does not repair them without authority.
3. The performed opening aggregate discloses its own freshness. A member in
   this scenario has no freshness value of its own; how the aggregate's
   freshness reads then is not decided here, and implementation must not claim
   the two compose semantically until it is.
4. The generated dependency declaration carries the digest of the proposed
   `spec.md`; a later PWB amendment regenerates it against the actual
   predecessor, and no stale patch is selected.

## Required sequence if signed

1. Independent fresh-context review over the exact package head, with raw
   output retained and every finding dispositioned.
2. Reconfirmation if any reviewed byte changes.
3. Regenerate this package over the actual predecessor if needed; run
   `--check`, `--selftest` and `--diff` on final bytes.
4. Sign off by version under `OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`:
   the owner selects an option naming the package and version, and
   `scripts/record_versioned_signoff.py` applies the six patches, writes the
   sign-off record and appends one aggregate block. No typed phrase or digest
   argument is required.
5. Create the printed `<package>-v<major>.<minor>` tag on the commit carrying
   the applied result and verify all eleven post-apply rows.
6. Run the canonical governance battery in a clone and retain the transcript.

## Remaining separate gates for M2 slice 5

Even after this specification act, slice 5 remains blocked on the following; the first is already done:

- the registry-entry amendment act at `.18`, performed 2026-09-30;
- the plain implementation-continuation direction at `.19`;
- a fresh implementation authorization that resolves the five disclosed
  contract-coverage gaps and names the exact built behavior.

No default performs any of these. If unanswered, current signed behavior and
the current no-route implementation stay in force.

## Verification before any answer

```sh
uv run scripts/build_pwb_missing_currency_disclosure_scenario.py --check
uv run scripts/build_pwb_missing_currency_disclosure_scenario.py --selftest
uv run scripts/build_pwb_missing_currency_disclosure_scenario.py --diff
python3 scripts/check_governance.py
python3 scripts/check_governance.py --selftest
```

The first two builder commands are integrated into the canonical/hosted lists
once all parallel candidate branches are combined; this branch leaves CG-26's
coupled lists untouched.
