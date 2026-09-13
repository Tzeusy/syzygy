# Polaris page size at the response ceiling — the owner's ruling on P-67 (2026-09-13)

> **Status: ruled and being applied.** The three batched questions the M1
> feature-request funnel gathered
> (`docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`, register row P-67) were
> answered by the owner in one reply on 2026-09-13. This record owns the
> ruling; the packet remains the question it was ruled on. Where this file
> and the owner's own words differ, the words win, and they are quoted in
> full below. Nothing here is an act: no digest is bound, no specification,
> policy or registry changes, and no acceptance-record row is added. It is a
> plain owner direction in the shape of the P-63 ruling
> (`PWB-CYCLE-OWNER-RULINGS-DECISION.md`).

## The owner's reply, verbatim

Claude Code chat, 2026-09-13, about 21:15 +08:00, in answer to the packet
summary that presented Q1, Q2 and Q3 with their recommended answers:

> Agreed

Evidence snapshot the questions were answered at: Syzygy `8887cff` (main,
clean apart from the co-lead's in-flight `AGENTS.md`); Butlers head
7c8743f63 for the breach, 66ed58f for the rendered capture.

## The three rulings

Each is its own decision; agreement to one is not approval of another. The
recommended answer was taken in every case, as presented.

| Question | Ruled | What it means | Applied by |
|---|---|---|---|
| **Q1** (lane A) | **Yes** — an implementation-only trim of the Polaris human page in the P-63 shape: the narrative JSON is no longer embedded in the human page (the identical payload stays at the authenticated presentation route), and item classes whose items carry no statement render as a compact list instead of a three-column table. No specification text changes. | Bead `syzygy-dov.1`; measured before and after on a committed clean tree, direct and tailnet host forms, evidence retained under `docs/evidence/`; every P-63 invariant re-checked; independent review before close. |
| **Q2** (lane B) | **Yes, after lane A is measured** — the semantic-delta package for scoped epistemic attributes (PWB-REQ-007, 014, 020; draft text in the funnel packet) is to be drafted once the lane A measurement is retained. Drafting is authorized; adoption is a separate owner act in the 2026-09-05 amendment shape. | A follow-up bead under `syzygy-dov.1`, filed when the lane A evidence lands. |
| **Q3** (scope) | **Accept** — M1 delivers a smaller per-item slope and a removed constant, not a sublinear page; the restated target is the page at Butlers head under 1.4 MB on both host forms and under 1,000 bytes per new item after lane B. Catalogs on their own routes are a separate spec question, not opened. | The bead's title keeps the pursuit wording; its notes carry the restated target and this record. |

## Sequencing, in one sentence

Lane A is built, measured and reviewed first under the existing bead; the
lane B package is drafted against the retained lane A numbers; nothing
touches the signed PWB specification until its own act.
