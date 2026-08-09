# Owner decision packets — round 2026-08d

> **This file decides nothing, adopts nothing, accepts nothing.** Twelve
> concise packets in the charter's required form. The queue itself is owned
> by `../../../decisions/PENDING-OWNER-DECISIONS.md`; where a packet here
> and that register disagree, the register wins. Packets whose ground this
> round changed say so explicitly: several questions now have one arm
> **already executed in candidate bytes** — that is a drafting posture, not
> a decision; declining the arm reverts the bytes before any wave act.
>
> **Partially superseded 2026-08-10 (launch-closure pass):** packets
> **2, 7, 8, 10, 11** have current packets in
> `.syzygy/governance/decisions/` (`UNKNOWNS-AND-GAPS-`,
> `PROJECT-SHAPE-FACETS-`, `HUMAN-ENTRY-`, `KNOWLEDGE-HYGIENE-`,
> `OPENSPEC-FORM-AND-VERSION-DECISION.md`) — do not act from the versions
> below. Packets 1, 3, 4, 5, 6, 9, 12 remain current here.

## Packet 1 — The acceptance-wave split itself

- **Question:** accept the foundational contracts as six independent wave
  acts (A core observatory · B views · C1 packet identity · C2 selection
  policy · D1 mission prevention · D2 mission effects) instead of one
  all-in-one act?
- **Current authority:** none — acceptance structure is the owner's.
  Candidate design: `ACCEPTANCE-WAVE-DESIGN.md`; live phrases:
  `../FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`.
- **Options:** (a) six waves as offered; (b) fewer, coarser waves (e.g.
  A+B, C, D); (c) revert to all-in-one.
- **Costs:** (a) six ceremonies, six digests to verify; (b) re-partition
  and re-review; (c) restores the RD-8 "surprised act" — every defect in
  any contract blocks all of them.
- **Recommendation [Inferred]:** (a). Every depends_on edge points backward
  in ceremony order A→B→D1→D2→C1→C2; each wave leaves a coherent corpus if
  nothing later is ever accepted.
- **Earliest gate:** before the first wave act.
- **Independent work:** review and repair proceed regardless; only the act
  ceremonies wait.

## Packet 2 — `Unknown` versus `Gap`

- **Question:** adopt the two-term rule: **no evidence → Unknown; evidence
  of non-satisfaction → Gap**?
- **Current authority:** VIS-2 defines Unknown (doctrine, in force). "Gap"
  is defined nowhere in force — only in the candidate
  `policy-candidates/TERM-REGISTRY.md`, which awaits its own act.
- **Options:** (a) the two-term rule; (b) fold both into Unknown; (c) other
  vocabulary.
- **Costs:** (a) one new core term to teach; (b) conflates "we don't know"
  with "we know it's not met" — the difference that decides whether work is
  reconciliation or investigation; (c) re-review of the registry.
- **Recommendation [Inferred]:** (a) — it is the distinction the
  three-state thesis already implies.
- **Earliest gate:** before OpenSpec Capability 1 (specs will use both
  words in acceptance criteria).
- **Independent work:** yes, everything except OpenSpec authoring.

## Packet 3 — Mission V0/V1 staging

- **Question:** stage Missions as **propose-only V0** (Wave D1) with the
  **effect-bearing correction plane as V1** (Wave D2)?
- **Current authority:** none adopted; P-23 in the register; reviews RC-7,
  RD-1/RD-1b. The wave split makes the staging *performable*: D1 and D2 are
  separate acts.
- **Options:** (a) accept D1, hold D2 for V1; (b) accept D1+D2 together;
  (c) decline both.
- **Costs:** (a) V0 missions cannot apply effects — correction machinery
  unexercised until V1; (b) larger first slice, correction plane must be
  implemented before any mission runs; (c) no missions at all in V0.
- **Recommendation [Inferred]:** (a) — RC-7's argument stands: a V0 that
  can only propose does not need reversal machinery, and the ceiling and
  the plane move together by construction when D2 is a separate act.
- **Earliest gate:** the D1/D2 acts.
- **Independent work:** yes — Waves A/B/C do not depend on this.

## Packet 4 — D3/D4 ordering

- **Question:** rule open question D4 (may a doctrine amendment place a
  bounded mission inside VIS-4's bounds by stipulation?) **before**
  considering doctrine amendment D3.
- **Current authority:** VIS-4 (adopted); D3 packet rev1 §6 (candidate);
  P-24.
- **Options:** (a) rule D4 first, then adopt whichever D3 text the ruling
  implies; (b) adopt D3 as written (settles D4 silently); (c) decline D3.
- **Costs:** (a) one extra ruling; (b) forecloses D4 inside the sentence
  built to prevent that; (c) bounded missions stay outside doctrine —
  which the D1 wave tolerates (RFC10-24 holds every mission at
  `awaiting-approval` until the doctrine question is ruled).
- **Recommendation [Inferred]:** (a). Unchanged from P-24.
- **Earliest gate:** before act D3 (optional act 5).
- **Independent work:** yes — all wave acts precede this safely.

## Packet 5 — Mission extension profile

- **Question:** admit Mission and Attention Item identity via an
  **extension profile in RFC1-7** (with named minting authority) rather
  than widening the unconditional V0 core (RFC1-5)?
- **Current authority:** P-28. **Ground changed this round:** option (b)
  of P-28 is executed **in candidate bytes** — RFC1-7 carries the mission
  extension profile and RFC10-4 grounds identity in it (semantic delta
  A-2/A-7).
- **Options:** (a) keep the profile as drafted (accepting Wave A ratifies
  it); (b) widen RFC1-5's core instead; (c) strike mission identity from
  the identity system.
- **Costs:** (a) profile machinery in the first wave; (b) mission becomes
  V0-core entity — collides with propose-only staging; (c) a
  budget-spending entity outside identity, the failure RFC1-9 exists to
  prevent.
- **Recommendation [Inferred]:** (a), unchanged from P-28's analysis.
- **Earliest gate:** Wave A act (the profile is in RFC-0001).
- **Independent work:** yes.

## Packet 6 — Registry authority

- **Question:** does the portfolio layout registry live in the
  **governance plane** (typed workspace governance store, RFC10-15) rather
  than personal workspace presentation state?
- **Current authority:** P-22; RFC3-10/11/21 (candidate). **Ground changed
  this round:** RFC9-8(a) is redrafted to the governance store with a
  staged reference (semantic delta A-9); the old contradiction is repaired
  in candidate bytes rather than ruled.
- **Options:** (a) ratify the governance-plane placement (Wave B act binds
  the redrafted RFC9-8(a)); (b) rule for the workspace manifest and revert.
- **Costs:** (a) portfolio re-lay waits for an accepted RFC 0010 store;
  (b) restores the RFC3 contradiction RC-4 found.
- **Recommendation [Inferred]:** (a).
- **Earliest gate:** Wave B act.
- **Independent work:** yes.

## Packet 7 — Project-shape facets

- **Question:** adopt the seven independent facets with per-facet value
  domains and **no cross-facet rollup** as the shape vocabulary the
  surfaces render?
- **Current authority:** candidate RFC-0006 (RFC6-18/19 as amended this
  round: work state and chain state never folded; uncomputed
  reconciliation renders Unknown).
- **Options:** (a) as drafted; (b) permit an explicit, labeled composite
  facet; (c) fewer facets.
- **Costs:** (a) no single "health score" anywhere — deliberate; (b) the
  rollup VIS-2 exists to prevent, unless its derivation is fully rendered;
  (c) re-review of RFC-0006/0008.
- **Recommendation [Inferred]:** (a).
- **Earliest gate:** Wave A act (RFC-0006 is in Wave A).
- **Independent work:** yes.

## Packet 8 — Human entry and discoverability

- **Question:** fix the human entry at `.syzygy/intent/OVERVIEW.md`
  (governed presentation, never authority) and make repository
  discoverability a **per-repository kernel finding** (yes/no/Unknown)
  with **no root write** by Syzygy?
- **Current authority:** candidate RFC7-39/40 (new this round); VIS-5.
- **Options:** (a) as drafted; (b) allow a proposed root-README pointer via
  adapter; (c) leave entry unspecified.
- **Costs:** (a) undiscoverable repositories surface as Unknown findings,
  not silently; (b) still propose-only under VIS-5, adds an adapter
  surface; (c) every clone renegotiates where to start.
- **Recommendation [Inferred]:** (a); (b) remains available later as an
  OpenSpec-level proposal without contract change.
- **Earliest gate:** Wave B act.
- **Independent work:** yes.

## Packet 9 — Core vocabulary

- **Question:** approve the small public core / advanced tier split of the
  term registry (T-01…T-31) as the working vocabulary?
- **Current authority:** candidate `policy-candidates/TERM-REGISTRY.md`;
  P-16/P-17/P-18/P-25 in the register carry the known defects (default-path
  leaks `Evaluation`, `Claim`; three genuinely undefined terms; three
  doctrine seams).
- **Options:** (a) approve with the leaks repaired first; (b) approve as-is
  knowingly; (c) amend the tiering.
- **Costs:** (a) the overview edit moves act-Overview's digest — cheapest
  before that act fires (the RD-8-quoted argument); (b) known leaks become
  approved; (c) re-review.
- **Recommendation [Inferred]:** (a), sequenced before the overview act.
- **Earliest gate:** before the overview act and before OpenSpec.
- **Independent work:** yes, except overview-digest-touching edits.

## Packet 10 — Knowledge hygiene

- **Question:** which knowledge-hygiene craft policy: the 22-rule original
  or the 10-rule compaction?
- **Current authority:** P-12; both candidates in `policy-candidates/`.
  Until one fires as its own craft act, **CC-BUDGET-1 is installed
  nowhere** and the context-budget threshold has no owning rule.
- **Options:** (a) compact 10-rule (carries the migration map, adds one
  listed obligation); (b) original 22-rule; (c) neither.
- **Costs:** (a) twelve rules retired into named survivors; (b) more
  surface to maintain; (c) the budget threshold stays orphaned.
- **Recommendation [Inferred]:** (a), after a fresh confirming review of
  the compaction.
- **Earliest gate:** its own `CONFIRM CRAFT AMENDMENT` act; before
  OpenSpec (specs will cite CC-BUDGET-1).
- **Independent work:** yes.

## Packet 11 — OpenSpec version

- **Question:** which OpenSpec format/version does Capability 1 use?
- **Current authority:** none — no `openspec/` exists (correct). The
  th-projects spec-format contract is the candidate consumer shape.
- **Options:** (a) pin the current th-projects `spec-format.md` revision;
  (b) pin an external OpenSpec release; (c) defer until the first
  changeset drafts.
- **Costs:** (a/b) a pin to verify at first use; (c) the first changeset
  author chooses implicitly — an owner decision made by default.
- **Recommendation [Inferred]:** (a), recorded as a pin in the substrate
  lock at decision time.
- **Earliest gate:** before the first OpenSpec changeset.
- **Independent work:** yes — everything up to OpenSpec authoring.

## Packet 12 — License

- **Question:** unchanged from `LICENSE-DECISION-PACKET.md` (P-14): four
  candidates, three `[Unknown]`s including copyleft reach into governed
  repositories.
- **Current authority:** none; owner + qualified legal review.
- **Options / costs:** in the owning packet, not restated here.
- **Recommendation:** none — not to be chosen autonomously.
- **Earliest gate:** before any public release; does not block wave acts
  or OpenSpec.
- **Independent work:** yes.
