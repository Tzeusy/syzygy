# PREPARED owner implementation-authorization act — Capability 1

> **PERFORMED 2026-08-21 — this packet is superseded history.** The owner
> performed the act with their own complete instrument (fixing all five
> open terms), recorded verbatim at
> `../../../decisions/CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md`.
> That record owns the authorization; nothing below satisfies anything.
> Preserved unchanged beneath this banner as the record of what was
> prepared and why.

> **Prepared, not performed. This file authorizes nothing.** Drafted
> 2026-08-21 after the owner replied "Authorized" to the adoption-act
> summary. The session declined to treat that word as the act: every
> performed act in this repository is an explicit instrument (the Wave
> A/B acts, craft acts 6/7, the launch decision, the adoption act), the
> pending-decisions register's standing rule is "Nothing in this
> register is self-executing. Acts happen only by the exact ceremonies
> their owning records define, performed by the owner," and a one-word
> authorization leaves every material term below undefined — recording
> it would mean the session authored the act's content on the owner's
> behalf (VIS-4). If the owner intended something other than
> implementation authorization, this packet simply waits or is
> discarded; nothing has changed.

## What this act would rest on

- The **adopted** Capability 1 specification — owner act dated
  2026-08-20, recorded at
  `decisions/CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md`, at the seven
  exact digests that record quotes. The specification governs all
  required behavior; implementation conformance is judged against it.
- The **operating constraints** the owner ruled 2026-08-16 (P-35,
  `decisions/PROJECT-OPERATING-CONSTRAINTS-DECISION.md`) and the
  **resource envelope** ruled 2026-08-19 (P-45/A6,
  `decisions/A6-RESOURCE-ENVELOPE-DECISION.md` — 2h/week, $200/mo,
  syzygy the first proving project).

## The terms the act must fix (currently undefined — owner's to decide)

1. **Scope of "implementation."** Which of these become lawful, in what
   order: implementation *planning* (design of the build, no code); an
   implementation *backlog* (Beads issues — currently prohibited);
   application/library *code* with `src/`-style trees and toolchain
   manifests (currently prohibited)? All at once, or planning first?
2. **Stack selection.** The standing prohibition on choosing a
   language, framework, database, graph store, renderer, or deployment
   target — lifted for Capability 1's implementation (bounded by the
   P-35 constraints), or does stack choice remain a separate owner
   ruling the planning phase must bring back?
3. **Repository home for implementation artifacts.** The governed
   planes are `openspec/**` and `.syzygy/**` (VIS-5 is about the
   *product's* runtime writes — CAP1-REQ-061 governs that); the
   *repository's* implementation tree needs a named home and a named
   authority for it.
4. **Evidence bar for implementation acceptance.** Which craft policies
   govern "done" for implementation work (CC-REV review discipline is
   in force; test/evidence standards for code are not yet defined) — or
   is that explicitly deferred to the planning phase's first output?
5. **Boundaries that stay closed** (suggested restatement): Capability 1
   only; no other capability's authoring or implementation; deferred
   waves untouched; the seven adopted artifacts remain unedited, with
   spec changes routed through CC-REV-2's amendment path; VIS-4 —
   security-posture-touching changes always owner-gated.

## Suggested instrument (owner's to amend, complete, or replace)

```text
OWNER ACT — CAPABILITY 1 IMPLEMENTATION AUTHORIZATION
Date: <date>
Owner: Tzeusy

Resting on the adopted Capability 1 specification
(decisions/CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md, at its recorded
digests), I authorize <scope per term 1 — e.g. "implementation planning
and implementation" / "implementation planning only"> for

  Capability 1 — Project registration and honest shape visibility

subject to: <terms 2–4 as the owner fixes them>, within the P-35
operating constraints and the A6 resource envelope.

This authorization covers Capability 1 only. It does not authorize any
other capability's authoring or implementation, does not touch the
deferred waves, and does not permit editing the seven adopted
specification artifacts.

Record this act verbatim at:
.syzygy/governance/decisions/CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md
```

Until such a record exists, implementation, implementation planning,
and any implementation backlog remain forbidden, exactly as
`PROJECT-STATUS.md` step 6 states.
