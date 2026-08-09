# Doctrine amendment draft — D3 (proposed): human-triggered propagation may authorize a bounded mission

**SUPERSEDED by rev1 (`DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md`), 2026-08-10.**
The acceptance record's act-5 row names rev1 as the subject: this draft's
`vision.md` insertion cannot be applied as written (SD-8), and rev1 exists
to remove that defect. Kept in place, unedited below this banner, as the
original the owner may compare.

**Status: DRAFT — not applied.** Doctrine amendment is an owner act
(VIS-4; AGENTS.md adoption authority). This draft exists because owner
direction OD-R10-2 asked for the minimal clarification *if doctrine needs
it*; the owner may also rule that RFC 0010 alone suffices and no amendment
is needed. Nothing in RFC 0010 or 0011 depends on this amendment being
adopted — until adoption, human-triggered propagation reads exactly as
doctrine already states.

**Operative consequence of declining, stated plainly (safety-review D5):**
RFC 0010 can be *accepted* without this amendment — it binds nothing
doctrine forbids — but Mission Control cannot lawfully *operate*:
unamended, architecture.md's human trigger is one deliberate
propagate/sync pass, and a mission authorizing repeated
plan/materialize/execute/verify/re-plan cycles is not that. Declining D3
is a lawful choice; it keeps missions out of operation until doctrine
says otherwise.

**Why this amendment is not self-licensing under VIS-4 (safety-review
D4; the owner may overrule this position):** VIS-4's two-part mechanism
(accepted adjudication RFC + explicit owner doctrine amendment) governs
opening *autonomy beyond VIS-4's stated bounds* — delegation of the
always-human decision classes. A bounded mission delegates **execution
inside every gate** and never adoption, approval, widening, or any
always-human class, so this draft's position is that it clarifies the
*trigger grain* of an already-human-triggered loop rather than opening
autonomy beyond VIS-4's bounds — which is why a doctrine amendment alone
(this document, an owner act) is offered. If the owner instead rules
that a bounded mission *is* autonomy beyond VIS-4's stated bounds, then
VIS-4's own terms apply: an accepted adjudication RFC is also required,
and this amendment alone is insufficient — RFC-0010 would serve as that
adjudication RFC only after the owner designates it as such.

## What it amends

Two sentences, clarified in place; no rule renumbered, no rule retired.

**architecture.md**, "The loop" paragraph — after "The loop is
**human-triggered**: someone specs a desired shape, then deliberately
triggers a propagate/sync pass.", append:

> A human trigger may take either grain: one deliberate propagate/sync
> pass, or one deliberately approved **bounded mission** — a single owner
> act authorizing repeated plan/materialize/execute/verify/re-plan cycles
> strictly inside an explicit autonomy envelope (objective, budgets, risk
> limits, protected surfaces, stop conditions — at minimum; the envelope
> also bounds permitted write scope, tools, required gates and reviews,
> evidence obligations, and the completion predicate) that agents can
> never widen, ending at the envelope's own terminal conditions. The
> mission grain does not alter what remains human: VIS-4's always-human
> classes, envelope approval and widening, and **every gate that would
> otherwise apply** — a mission is authority to proceed inside the gates,
> never authority to skip one.

**vision.md**, "Not autonomous." bullet — after "The loop is
human-triggered;", the clarifying insertion:

> (a trigger may authorize one pass or one bounded, envelope-limited
> mission — see architecture.md; either way the trigger is a deliberate
> human act, and expiry or exhaustion of a mission's envelope halts, never
> extends, its authority)

## What it deliberately does not change

- VIS-4's always-human classes and the spec-adoption gate mechanism —
  untouched; a mission cannot open, widen, or substitute for that gate.
- "Not autonomous" as posture — a mission is a *human-triggered* act with a
  bounded envelope, not default autonomy; unattended reconciliation remains
  outside doctrine.
- The idempotence invariant and one-upward-arrow loop shape — untouched.

## Adoption mechanics (if the owner adopts)

Amend both files in place with the verbatim text above; record the
amendment in the doctrine README's amendment log as **D3** with the owner's
adopting phrase and date, per the D1 precedent; one commit + annotated tag.
Under RFC3-16(c) this is an owner-adopted bootstrap act until correlation.
