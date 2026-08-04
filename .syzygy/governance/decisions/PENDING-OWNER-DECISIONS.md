# Pending owner decisions — register

> **Status: every item below is PENDING. This file decides nothing, adopts
> nothing, accepts nothing.** It exists, on owner instruction (2026-08-04),
> to make the open decision queue explicit and clone-visible. Each row points
> at the record that owns the full detail; where this file and an owning
> record disagree, the record wins and this file is stale.
>
> **As-of: 2026-08-04, HEAD `adddc34`.** Hand-authored; regenerated or
> corrected in the same change whenever a listed decision is made.
>
> **Disclosure:** several owning records live under `_bootstrap/`, which is
> **founder-local and git-excluded** — deliberately absent from clones, not
> deleted. A clone can read this queue but cannot resolve those pointers;
> whether those records move to a tracked home is itself item P-9.

## The acceptance acts (none performed)

| # | Decision | Owning record |
|---|---|---|
| P-1 | **Act 1** — accept the compacted foundational design contracts (32 modules, exact phrase + package digest in the record) | `_bootstrap/rfc-phase/final-prespec/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` |
| P-2 | **Act 2** — confirm the craft-and-care amendment CC-TEST-2 | same record; `.syzygy/governance/policies/craft-and-care/INSTALL-RECORD.md` (amendment section) |
| P-3 | **Act 3** — accept the topology bundle | same record |
| P-4 | **Act 4** — adopt the project overview (`.syzygy/intent/OVERVIEW.md`); note: its digest freezes an authoring-time status section that predates the current gate (known coupling, record §7) | same record |
| P-5 | **Optional act 5** — adopt, amend, or decline the D3 bounded-mission doctrine amendment; consequence of declining is stated in the mission-control contract | same record; `_bootstrap/rfc-phase/final-prespec/DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md` |

The ten §7 owner-attention items of the acceptance record (including the
stale RFC-0007 self-count R1 and the corpus-size trade with its measured
per-task cost) remain part of P-1's knowing acceptance.

## Defects that only an owner ruling can dispose (from the §20 independent reviews, 2026-08-04)

| # | Decision | Evidence |
|---|---|---|
| P-6 | The retired acceptance phrase survives **inside the act-1 digest set** (`rfcs/RFC-0003/governance-homes-and-owner-acts.md:87`); the replacement phrase appears nowhere in the corpus. Options: accept knowingly (correction rides the first RFC-0003 amendment) or fix + regenerate manifest + one further digest-binding review | two independent §20 discoveries; `_bootstrap/knowledge-refactor/reviews/20-DISPOSITIONS.md` |
| P-7 | Every canonical craft-policy file opens with "this copy is the bootstrap-phase record" — false at the canonical home, inverting authority. The fix touches act-2's digest-bound file, so: accept knowingly, fix + re-offer act 2, or fold into P-9 | two independent §20 discoveries; same dispositions file |
| P-8 | `INSTALL-RECORD.md:20` conditions craft binding on the retired phrase (unsatisfiable as written). Digest-stable supersession note drafted; tracked-file edit needs owner sign-off | three §20 reviews + pass preflight |
| P-9 | **Clone visibility (FD-021 vs the refactor directive §19):** candidate contracts, topology, acceptance record, validation scripts, and the owner-decision ledger are all founder-local; committed artifacts cite warrants a clone cannot resolve; the tier-3 engineering baseline is machine-local. Decide what enters the tracked tree, and when | `_bootstrap/knowledge-refactor/PUBLIC-CLONE-VERIFICATION-REPORT.md` (2-of-9 scorecard) + four §20 reviews |
| P-10 | The §20 battery did not cover the pass's own unreviewed drafts (28 RFC-0006 routing rows; KA-1…24; CC-KNOW-1…12; CC-BUDGET-1…4; the term-registry completeness checks). Commission further review, or accept them explicitly as unreviewed drafts | dispositions §3(c) |

## Standing decisions carried from earlier phases

| # | Decision | Owning record |
|---|---|---|
| P-11 | Install the proposed public front door (README, AGENTS.md replacement, PROJECT-STATUS, CONTRIBUTING, SECURITY) once the current revision round closes. The `.gitignore` additions piece is already installed at commit `829e753` (recorded there as owner-approved 2026-08-04); the five document drafts remain pending | drafts in `_bootstrap/knowledge-refactor/drafts/` |
| P-12 | The knowledge-hygiene craft policy addition (own `CONFIRM CRAFT AMENDMENT` act required) | `_bootstrap/knowledge-refactor/CRAFT-KNOWLEDGE-HYGIENE-POLICY-DRAFT.md` |
| P-13 | The overview refactor proposal (§17) — untouched because it couples to act 4's digest | parked with the team lead |
| P-14 | License choice (four candidates; three [Unknown]s including copyleft reach into governed repositories — wants qualified legal review) | `_bootstrap/knowledge-refactor/LICENSE-DECISION-PACKET.md` |
| P-15 | Founder-decision-log digest binding / promotion to a tracked home | pass finding F-11 |
| P-16 | Canonicalize the six-plane state vocabulary over the older four-state phrasing | pass finding TM-1 |

**Nothing in this register is self-executing.** Acts happen only by the
exact ceremonies their owning records define, performed by the owner.
