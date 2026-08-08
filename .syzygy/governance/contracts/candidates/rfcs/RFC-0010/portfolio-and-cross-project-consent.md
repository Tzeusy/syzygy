---
id: RFC-0010
title: Mission Control and Autonomy Envelopes — portfolio authority and cross-project consent
status_source: owner-act-record
module: portfolio-and-cross-project-consent
clauses: "RFC10-15, RFC10-21 (non-contiguous — see the package clause map)"
governs: [workspace-governance, portfolio-missions, cross-project-consent]
applies_to: [mission-control, workspace, machine-clients]
depends_on: [RFC-0003, RFC-0005]
tags: [portfolio, consent, egress, fail-closed, prevention-plane]
---

# RFC 0010 — Mission Control: portfolio authority and cross-project consent

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — as an owner-adopted bootstrap act until
the independent A1 correlation mechanism exists, and as a Syzygy-verified
effective act only after correlation (RFC3-16). Absent such a record, this
contract binds nothing.

**Package:** module 5 of 5 of the RFC 0010 contract package. Index, clause
map, lookup rule, package-level integration and deferrals: `README.md`.
Rationale, amendment history, and violation cases:
`../../history/RFC-0010-history.md` (non-normative).

**Serves:** VIS-4, VIS-5; SEC-1, SEC-2.

## 1. Scope of this module

The portfolio authority plane and its hard boundary against project-internal
truth (RFC10-15), and the consent composition rule for anything a mission
assembles across project boundaries (RFC10-21). Both are prevention-plane
boundary rules: they draw lines that no mission, whatever its autonomy
level, may cross.

## 2. The contract

**RFC10-15.** **Portfolio authority is a distinct plane.** A cross-project
mission never makes one project authoritative over another. Portfolio-level
governance — workspace missions, portfolio priorities, global and
per-project budgets, fleet capacity and concurrency, project
pause/maintenance-only modes, cross-project attention and scheduling
policy — lives in a typed, platform-level **workspace governance store**,
distinct from the presentation-only workspace manifest (which remains
personal presentation state, RFC 0003). The store's entries that authorize
anything are RFC3-16(a) artifacts. The store **must never become
authoritative for project-internal doctrine, contracts, specifications, or
behavior** — its writ ends at scheduling, budget, and attention policy.
Where the writ's own enumeration (per-project budgets, pause and
maintenance-only modes) meets that prohibition, **the prohibition wins**:
pausing a project means Syzygy refuses to schedule against it, and never
mutates project-internal state or status. Its concrete home and schema are
deferred (§8 q3) — and minting the store is an authority-plane widening
that requires an RFC3-15-style recorded owner widening, not merely a
schema decision.

**RFC10-21. Cross-project composites carry every embedded project's consent
requirement.** A context packet, prompt, summary, embedding, or any other
composite assembled **under any mission** is
subject, at the RFC5-15 choke point, to the egress-consent record of **every
project whose content it embeds** — not one of them, never the project
the composing step names for itself, and **regardless of how many projects the
mission's declared target names**. The predicate is a property of the
*content*, not of the mission's scope declaration: a mission declared against
project A alone, whose envelope grants a path containing project B's checkout
and whose composite embeds B's content, is squarely inside this clause. Keying
the rule on declared scope would let the composing party choose whether the
rule applies by choosing how to declare its own target — the party the rule
exists to bind. A composite embedding content from a
project for which the naming (project, provider) consent is absent, not in
force, or of unverifiable provenance **fails closed and the refusal renders**,
exactly as an undeterminable content class does (RFC5-14); so does a composite
whose embedded content cannot be attributed to a project of origin at all.
Evidence gathered
within one project never satisfies a completion predicate scoped to another.
Where the workspace governance store's per-project budget and an envelope's
budget both bind (RFC10-15, RFC10-7), **the lesser binds**, and a portfolio
mission's spend against a project is debited from that project's budget as
well as the mission's.

## 8. Owner questions

*Package numbering; question numbers never shift. Full package index:
`README.md` §8.*

3. **Workspace governance store — OPEN.** Home and minimal schema —
   platform-level typed store, location to be proposed at surface
   specification.

---

*End of RFC 0010 module 5. Clauses RFC10-15 and RFC10-21 — non-contiguous by
design; the package README's clause map is the lookup authority. Nothing
merged, nothing retired.*
