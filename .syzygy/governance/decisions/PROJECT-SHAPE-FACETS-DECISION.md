# Owner decision packet — project-shape facets (P-37; supersedes round-08d packet 7)

> **This file decides nothing.** Current form of the shape-facet question
> (previously round-2026-08d packet 7), restated for the Capability 1
> launch scope. Queued as **P-37**.

## Question

Adopt **seven independent project-shape facets, with no cross-facet
rollup**, as the shape vocabulary the views render:

```text
Registered
Shape present
Human-understandable
Observable
Traceable
Mission-ready
Reconciled
```

## Rules the adoption carries

1. **No rollup.** Facets never fold into one compliance score — the
   rollup VIS-2 exists to prevent. Each facet exposes its constituent
   facts and reasons ("Why this answer?").
2. **Registration is not certification.** `Registered: true` reads as a
   relationship, never an endorsement; no facet value implies another.
3. **Capability 1 scope.** Only facets whose governing Wave A/B semantics
   are accepted may be *specified*; **Mission-ready may render
   `not evaluated / deferred / Unknown`** until the C/D-wave semantics
   exist — a deferred facet renders its deferral honestly rather than
   waiting invisible.
4. Per-facet value domains come from the governing clauses (RFC6-18/19 as
   amended); a facet with no evidence renders Unknown with its reason.

## Current authority — corrected 2026-08-10 (RD30-01)

**The seven-facet vocabulary itself is drafted nowhere.** A fresh sweep
over all 30 Waves A+B modules (RD-30, denominator stated in its raw
review) finds the facet names — `Shape present`, `Human-understandable`,
`Mission-ready` — in **zero** contract bytes; they exist only in this
packet and the round-08d owner work order. An earlier form of this
section said "Wave A ratifies the drafted form"; that was false of the
vocabulary and is retired.

What **is** drafted, and what Wave A does ratify: RFC6-18/19 as amended
at round-2026-08d — the anti-rollup rules this packet's rules 1–4 ride on
(work state and chain state never folded; uncomputed reconciliation
renders Unknown; no composite badge). The facet *vocabulary* would live
either in an RFC-0006 amendment (drafted after this ruling, before the
Wave A act, so the act ratifies it knowingly) or in the Capability 1
specification itself (the routing matrix stages RFC 0001–0005/0006
enumerations at surface specification). Ruling (a) therefore also
chooses a drafting site, and the ruling record must name it.

## Options

- **(a)** Seven facets as stated in this packet, rules 1–4 above —
  **plus a named drafting site**: (a1) an RFC-0006 amendment before the
  Wave A act (cost: the Wave A argument regenerates and the fresh
  exact-package review binds the new bytes), or (a2) the Capability 1
  specification (cost: the vocabulary is spec-governed, not
  contract-governed, and a later surface could restate it differently
  unless the spec is the single home).
- **(b)** Permit an explicit, labelled composite facet — lawful only if
  its derivation is fully rendered; re-opens the RFC-0006 review.
- **(c)** Fewer facets — reprices only this packet and its consumers;
  RFC-0006/0008 carry no facet vocabulary to re-review (corrected
  2026-08-10 — the earlier cost claim was false).

## Recommendation

`[Inferred]` **(a) with site (a2)** — the Capability 1 spec as the
single home keeps the contract set stable and the exact-package reviews
already in flight valid; (a1) is the stronger anchoring if the owner
wants the vocabulary contract-governed, at the cost of another Wave A
regeneration. Rule 3 exists so the deferred Mission waves cannot hold
Capability 1 hostage while also never being silently presumed.

## Digest consequences and the exact next transaction

*(Added 2026-08-13, owner charter §16 — the costs were stated inside the
options; this gathers them where they can be compared.)*

| Arm | Wave A manifest | Wave B manifest | Confirmations |
|---|---|---|---|
| **(a1)** seven facets, drafted into an RFC-0006 amendment before the Wave A act | **regenerates** | unchanged | **Wave A's is retired** — a fresh exact-package review binds the new bytes before the wave can be offered |
| **(a2)** seven facets, owned by the Capability 1 specification | **unchanged** | unchanged | **both survive** |
| **(b)** an explicit labelled composite facet | **regenerates** | unchanged | Wave A's is retired; RFC-0006's review re-opens |
| **(c)** fewer facets | **unchanged** | unchanged | both survive — corrected 2026-08-10; RFC-0006/0008 carry no facet vocabulary to re-review |

**This is the decision whose arms differ most in cost**, and the difference is
one confirmed wave. `(a2)` is recommended partly for that reason, and the
owner should know that is what the recommendation is trading: contract-level
anchoring of the vocabulary, for keeping a confirmation that already exists.

**Pre-work required:** none for `(a2)` or `(c)`. For `(a1)` and `(b)`: draft
the amendment, travel it as a semantic delta, and regenerate the manifest —
in that order, before the ruling is recorded.

**Review required:** `(a1)` and `(b)` need a fresh-context review of the
changed RFC-0006 bytes **and** a new exact-package review of the regenerated
Wave A argument. `(a2)` and `(c)` need neither.

**Exact next transaction.** One row in `SURFACE-DECISION-RECORD.md` naming
**both** the facet set and its drafting site — the site is half the ruling,
and a row naming only the facets leaves the question open in the form that
caused this packet's 2026-08-10 correction.

## Earliest required gate

Wave A act (RFC-0006 is in Wave A); the ruling is cheapest before the
Wave A re-offer.

## Independent work

Yes — everything except OpenSpec authoring of the facet rows.
