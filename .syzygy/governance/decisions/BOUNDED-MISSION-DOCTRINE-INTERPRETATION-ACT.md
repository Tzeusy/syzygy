# Owner act — bounded missions under existing doctrine

Date: 2026-08-31

Owner: Tzeusy

Decision ID: `BOUNDED-MISSION-DOCTRINE-INTERPRETATION-2026-08-31`

The owner was asked:

> “should I record that existing doctrine permits bounded missions to leave
> `awaiting-approval` when an exact owner-approved mission and envelope exist?
> I recommend yes. Machines still cannot mint, self-approve, or widen owner
> acts.”

The owner answered:

> “yes”

## Ruling

Existing doctrine permits bounded multi-pass mission operation when a human
owner approves the exact mission and exact envelope. The approval is the
human-trigger required by the doctrine; bounded execution inside that approved
envelope is not autonomous vision steering.

This ruling satisfies the owner-interpretation alternative stated in candidate
RFC10-24. If RFC 0010 is later accepted and its behavioral specifications are
signed, a mission may leave `awaiting-approval` after every independent gate in
that contract passes.

## Boundary

This ruling does not:

- accept RFC 0010 or any Mission Control specification;
- approve, start or resume a mission today;
- permit a machine or agent to mint, impersonate, self-approve, widen, revoke
  or reinterpret an owner act, mission or envelope;
- allow a child mission or runtime decision to exceed its parent envelope;
- replace consent, authentication, budgets, execution profiles, recovery,
  effect verification, stop or escalation gates; or
- permit autonomous doctrine/spec adoption or owner-role delegation.

Mission approval and every envelope amendment remain exact human owner acts.
The generalized trusted-bootstrap direction changes whether those real acts
need external correlation; it changes none of their effect-specific limits.
