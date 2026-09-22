# Owner decision packet — missing effective currency bound outside freshness

> **Inert offering.** This packet performs nothing. It records no act,
> authorizes no implementation and changes no signed byte. A commit, review,
> merged pull request, passing check, silence or general approval performs no
> act. Only the exact phrase and digest below, after independent review, can
> perform this one PWB specification amendment.

Date: 2026-09-22. Gate bead: `syzygy-dov.20`.

Warrant: your 2026-09-21 P-69 arm B/Q7a direction — disclose a missing
RFC2-9 bound outside the freshness slot, keep the claim Unknown, and prepare a
CC-REV-2 scenario to PWB-REQ-007 behind its own sign-off and act. That ruling
is direction to draft, not the act offered here.

Manifest: `PWB-MISSING-CURRENCY-DISCLOSURE-MANIFEST.txt`, eleven rows over the
closed PWB behavior subject. Six rows hash proposed bytes and five current
bytes.

Manifest SHA-256:
`42dd4f91314f7aed074f21095743ba7ed175ba9518a0d8766cf38d18568209d7`

The builder writes this digest. Any patch, manifest or subject change retires
the argument and requires regeneration plus exact-byte review.

## What is offered

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

## The exact owner act

If, after reading the retained fresh review and dispositions, you choose to
perform this amendment, the exact phrase is:

`SIGN OFF PWB MISSING-CURRENCY DISCLOSURE SCENARIO: 42dd4f91314f7aed074f21095743ba7ed175ba9518a0d8766cf38d18568209d7`

Anything else is not this act. The recorder must reject a digest that differs
from the manifest then present and must prove each manifest row against the
post-apply tree.

## What this act would not do

- It would not amend RFC2-9, RFC2-10, RFC6-14, RFC6-17, RFC7-16, RFC7-33,
  CAP1-REQ-062, doctrine, policy, topology, consent or registry values.
- It would not accept the `.18` registry checkpoint or any of its thirteen
  proposed bounds.
- It would not continue implementation across the registry escalation trigger.
- It would not authorize M2 slice 5, wire `assessCurrency`, render the route,
  alter a tuple, or change an aggregate.
- It would not decide the performance order of lane B, `.21`, or another PWB
  successor; the adoption change records that order in the successor chain.

## Owner-visible consequences

1. Five accepted-contract consequences become honestly `unknown-uncovered` in
   the PWB matrix. This act changes the PWB specification; it does not weaken
   those contracts or authorize implementation across the gaps.
2. The observer-registry and secret-policy candidates both pin the predecessor
   `spec.md` digest. An adopted PWB successor stales both pins. This package
   does not repair them without authority.
3. `.21`'s opening aggregate expects freshness counts. A member in this
   scenario has no freshness value. `.21` must be regenerated/reviewed against
   actual predecessor bytes before any act or implementation claims the two
   compose semantically.
4. Every sibling dependency patch collides on the generated source-digest
   line. The later package regenerates; no stale patch is selected.

## Required sequence if signed

1. Independent fresh-context review over the exact package head, with raw
   output retained and every finding dispositioned.
2. Reconfirmation if any reviewed byte changes.
3. Choose the actual predecessor and regenerate this later package if needed;
   run `--check`, `--selftest` and `--diff` on final bytes.
4. Run a dedicated recorder that validates the exact phrase, applies the six
   patches in the same change, regenerates both derived files, writes the
   dedicated act record and appends one aggregate record section.
5. Add this link to `PWB_SUCCESSOR_CHAIN` in the performed order and verify all
   eleven post-apply rows plus packet-copy registration.
6. Run the canonical governance battery in a clone and retain the transcript.

## Remaining separate gates for M2 slice 5

Even after this specification act, slice 5 remains blocked on:

- lane B / P-68 disposition (`syzygy-dov.17`);
- the registry-entry amendment act prepared at `.18`;
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
