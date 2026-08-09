# Owner decision packet — specification granularity (P-40)

> **This file decides nothing.** New packet: the launch-gate pilot failed
> E1's *granularity* sub-verdict because no artifact states what one
> specification comprises, and the two then-live sequencing documents
> used different units (six changesets vs four capabilities). Queued as
> **P-40**.

## Question

Adopt the granularity rule:

> **One OpenSpec change governs one coherent capability, or one coherent
> change to a capability. Its requirements may span several views, but
> the change has one owner-readable product argument and one acceptance
> decision.**

## What the rule buys

- The unit of specification = the unit of owner acceptance = the unit of
  provability ("each capability must be provable on its own" — the
  first-spec sequence's ordering rule).
- A change is never split by view (no separate "Polaris spec" and
  "endpoint spec" for one capability — machine/human parity is a
  requirement inside the one change, not a sibling document).
- A change is never merged by convenience (two capabilities with separate
  product arguments never share one acceptance decision).

## Current authority

None — this is the gap. The four-capability decomposition in the current
`FIRST-OPENSPEC-SEQUENCE.md` already follows this rule de facto; the
superseded 09-report's six-changeset decomposition did not (it split by
API surface). Adopting the rule ratifies the capability decomposition as
the granularity, not just an ordering.

## Options

- **(a)** The rule as stated.
- **(b)** Finer: one change per view/API surface — more, smaller
  acceptance decisions; parity between views becomes a cross-change
  invariant nobody owns.
- **(c)** Coarser: one change for all of V0 — restores the all-or-nothing
  acceptance the wave restructuring just dismantled, at the spec layer.

## Recommendation

`[Inferred]` **(a)**.

## Earliest required gate

Before OpenSpec Capability 1 is authored (it defines what "Capability 1
is one spec" even means).

## Independent work

Everything up to OpenSpec authoring.
