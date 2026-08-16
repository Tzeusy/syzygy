# Owner decision packet — the merged-but-unreconciled Unknown reason (P-31)

> **This file decides nothing.** Bounded packet, in the fixed seven-part
> shape: question, current authority, options, recommendation, costs, which
> digest would change, exact next transaction. **No history chain** — the
> review that raised this is named once, as provenance, and not narrated.

## Question

The corpus's flagship V0 rendering — a project whose evidence has been
merged, but whose reconciliation has **not been computed** — must render
`Unknown`. Which reason does that `Unknown` carry?

Today: **none.** `RFC2-24` closes the reason vocabulary at twelve, none of the
twelve names this condition, and the same clause forbids minting a reason
downstream. A thirteenth reason would reopen a list **decision `A5` closed at
twelve**, which only the owner may do.

## Current authority

| | |
|---|---|
| The closed list | `RFC2-24` — twelve reasons, primary and secondary drawn from the same twelve; a condition outside the list is disclosed as a named fact of the render, never dressed as a reason |
| Why it is closed | prior owner decision **`A5`** |
| The rendering obligation | `RFC6-19` class 8 — *"an uncomputed reconciliation renders Unknown, never green"* |
| Verbatim carriage | `RFC6-14` — label, tier, reason and freshness travel verbatim from the RFC 0002 vocabulary |
| The drafted arm | sub-clause **`RFC2-19(a)`** in `../contracts/candidates/rfcs/RFC-0002/reconciliation-chain.md`, disclosed in place as awaiting this ruling |
| Provenance | `round-2026-08d/reviews/RD-15-facets-RAW.md` finding 3 |

Every contract clause above is **candidate**. Nothing here binds today.

## Options

- **(a) Ratify the drafted exemption.** `RFC2-19(a)` stands as written: the
  `reconciliation-pending` state and its rendering are *"**never stamped with,
  counted among, or absorbed by an aggregate of RFC2-24 Unknown reasons**,"*
  applying the exemption `RFC8-12` states for its four absence values. The
  condition is disclosed as a **fact of the render** — named, counted in its
  own right, expandable, routed to its resolving action — and the twelve stay
  twelve. The clause's own argument for why no existing reason fits is that
  `#2 missing-evidence` *"names a claim whose evidence was sought and not
  found, which misdescribes a verdict never sought."*
- **(b) Revert the drafted arm and open the list.** Amend `RFC2-24` to
  **thirteen** reasons, minting one for this condition. Reopens what `A5`
  closed, and every aggregate's per-reason disclosure gains a bucket.
- **(c) Revert the drafted arm and rule the condition out of scope for V0** —
  V0 never renders a merged-but-unreconciled project, so the case does not
  arise. Requires saying what V0 renders instead.
- **(d) Decline to rule now.** The drafted arm rides Wave A unratified,
  meaning the owner accepts Wave A while one of its sub-clauses is
  self-described as awaiting a ruling.

## Recommended option

`[Inferred]` **(a)**, and the reasoning matters more than the conclusion.

The condition is not an *unknown of the world* — it is a **not-yet-computed**
state of Syzygy's own pipeline. The twelve reasons answer "why can this not be
known?"; this one answers "why has this not been done?" Minting a thirteenth
reason would put a work-state answer inside an evidence-state vocabulary,
which is the category error `RFC6-14`'s *"an aggregate carries no epistemic
state of its own"* is elsewhere protecting against.

(b) is the honest alternative if the owner disagrees with that framing, and
the disagreement is a real one about what a "reason" is for. (c) is available
but would need V0's rendering restated. (d) is the option this packet exists
to avoid: it converts Wave A from a knowing act into a surprised one.

## Costs

| | |
|---|---|
| **(a)** | one clause ratified as drafted. **No byte moves** — `RFC2-19(a)` already exists in the candidate bytes; ratification is the act, not an edit |
| **(b)** | `RFC2-24` amended (a Wave A module), every aggregate's per-reason disclosure widened, `A5` reopened by owner act, and a semantic delta plus fresh-context review before the wave is re-offered |
| **(c)** | `RFC2-19(a)` removed, and V0's rendering of the case restated somewhere — the cheapest-looking option with the least-known blast radius |
| **(d)** | zero now; the cost lands at the Wave A act, where it is worst |

Options (b) and (c) both **regenerate the Wave A manifest digest**, which
**retires the existing Wave A confirmation** (`VERDICT: CONFIRM`, RD-31b) and
requires a fresh exact-package review before the wave can be offered. Option
(a) does not.

## Which digest would change

| Option | Wave A manifest digest | Wave A confirmation |
|---|---|---|
| (a) ratify as drafted | **unchanged** | **survives** |
| (b) thirteenth reason | **regenerates** | **retired** |
| (c) revert and rescope | **regenerates** | **retired** |
| (d) defer | unchanged | survives, and the act binds an unratified sub-clause |

Verify before acting, from the repository root:

```sh
python3 scripts/check_governance.py
sha256sum .syzygy/governance/contracts/candidates/wave-manifests/WAVE-A-MANIFEST.txt
```

## Exact next transaction

**Ruling wanted before Wave A is re-offered**, so the wave is accepted
knowingly.

For **(a)**, the transaction is a recorded decision, not an act — one row in
`SURFACE-DECISION-RECORD.md` reading, in substance: *"P-31: `RFC2-19(a)` is
ratified as drafted; the RFC2-24 list stays closed at twelve."* The Wave A
act then binds it as an ordinary accepted clause.

For **(b)** or **(c)**, the transaction is a **semantic delta** against the
affected Wave A module, a fresh-context review of the changed bytes, manifest
regeneration, and a new exact-package review — in that order. Do not perform
the Wave A act until that sequence completes.

## Earliest required gate

Before the Wave A act. `P-33` is what withholds the Wave A offer today; this
ruling is wanted at or before the same sitting.

## Ruled 2026-08-16

Owner, via an adversarially-reviewed questionnaire packet, direct
conversational response — chose **(a)**: ratify the drafted `RFC2-19(a)`
exemption as written. Recorded as **SDR-34** in `SURFACE-DECISION-RECORD.md`.
Full record: `PENDING-OWNER-DECISIONS.md` (row `P-31`, 2026-08-16 resolved
section) and the owner's local decision packet.
