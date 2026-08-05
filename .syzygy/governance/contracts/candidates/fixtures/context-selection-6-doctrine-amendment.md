# Context-selection fixture 6 — doctrine / shape amendment

**Status:** DRAFT — a candidate fixture, not part of the rev10 accepted
fixture set (fixtures 1–5). Binds nothing. Repaired 2026-08-05 against the
two stored §20.4 reviews; the repairs are recorded in
`round-2026-08/CONTEXT-COMPILER-FIXTURE-REPORT.md`.

**Objective.** A governed task: draft a minimal doctrine amendment packet
(the D3 bounded-mission shape) and prepare its owner-adoption ceremony.
Risk class: **shape-defining** — VIS-4 always-human; no code, no runtime.

**Selection rule trace (RFC11-4).** The task class is *doctrine amendment*,
so **the amended text itself is mandatory**. The D3 draft names its own two
amendment sites: `architecture.md`, "The loop" paragraph — which carries the
substantive bounded-mission insertion — and `vision.md`, "Not autonomous."
bullet — the cross-referencing insertion
(`DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md`, "What it amends"). `v1.md`
carries the V0/V1 scope boundary the amendment must not cross. The
**ceremony** half of the objective pulls two further files: doctrine's
`README.md`, which is the amendment log's home and carries both the D1
recording precedent the draft's adoption mechanics cite and the
identifier-stability rule the draft relies on ("no rule renumbered"); and
the owner-act contract → RFC-0003's `governance-homes-and-owner-acts` module
plus its package README (spanning invariants + the deterministic
clause-lookup rule).

## Required context (mandatory, deterministic)

```
scripts/context_load.py doctrine:vision.md doctrine:v1.md \
  doctrine:architecture.md doctrine:README.md \
  rfcs/RFC-0003/README.md rfcs/RFC-0003/governance-homes-and-owner-acts.md
```

Measured: **11,537 words ≈ 15,574 estimated tokens** — just above the
5,000–15,000-token default packet band, well below the 20,000-token
justification trigger (charter §11.4 context-budget table; the table's home
is the candidate knowledge-hygiene craft policy, which is not yet installed
— until it is, the charter table is cited directly and no `CC-BUDGET-*`
identifier is used, because none resolves to a governed artifact). The
limits are decomposition triggers, not validity laws (§11.4): the band
position is **disclosed**, and no waiver is required.

## Omitted applicable candidates, with reasons

- RFC-0010 Mission Control — the amendment's *subject*, not its
  *authority*: drafting doctrine text does not require the mission
  contract. But D3's inserted sentence copies RFC-0010's envelope
  vocabulary, and the draft's own adoption analysis turns on RFC-0010's
  status, so this is not a bare exclusion — it is moved to the **suggested**
  set below with provenance (RFC11-5), which is where inference may add and
  never suppress.
- RFC-0001 kernel — no entity, identity, relation, or plane semantics
  change; the amendment adds no term the kernel dictionary defines.
- RFC-0002/0004/0005/0006/0007/0008/0009 — no evaluation, evidence,
  execution, selection, or surface behaviour changes; D3 changes the
  *trigger grain* of the loop, not what any surface renders.
- RFC-0011 — no packet is compiled by this task; the packet *for* this task
  is what the fixture demonstrates.
- doctrine `security.md`, `trust-and-evidence.md` — the insertion changes no
  security posture (it explicitly preserves every gate) and no
  evidence/temporal rule; neither file is an amendment site, and neither is
  cited by the draft.
- Craft policies (all) — no engineering obligation is at issue in drafting
  doctrine text; the fresh-reader review duty the amendment must satisfy is
  doctrine's own (VIS-3), carried in the mandatory `vision.md`.
- Topology bundle (`.syzygy/map/topology-candidates/**`) — candidate
  material that binds nothing, and D3 changes no placement. Named here so
  the absence is a decision, not a gap; the loop-flow file is suggested
  below for the drafter who wants the diagram in view.
- `history/**`, `_bootstrap/**` — historical lane, never on a default
  reading path and never authority (AGENTS.md).

## Why no applicable constraint was lost

**Both amendment sites are in the mandatory set**, so the drafter can quote
and anchor the verbatim insertions rather than reconstruct them:
`architecture.md`'s "The loop" paragraph carries the human-trigger sentence
the substantive insertion appends to, and `vision.md`'s "Not autonomous."
bullet carries the site of the cross-referencing insertion. The gate that
makes adoption an owner act (VIS-4, in `vision.md`), the scope boundary the
amendment must not cross (`v1.md`), the amendment log with the D1 precedent
and the identifier-stability rule (doctrine `README.md`), and the act
machinery the ceremony uses — RFC3-16(a)/(b)/(c), including the
owner-adopted-bootstrap-act framing the draft's adoption mechanics cite —
are all mandatory-loaded.

**Index cross-check, with its limit stated.** Every RFC clause this task's
warrant cites (RFC3-16(a)/(b)/(c), RFC10-9 by reference) resolves through
`05-CONTRACT-INDEX.yaml` into the mandatory or suggested set, and RFC-0003's
governing phase rule travels with its package (RFC11-4's mandatory-inclusion
rule) in the selected README and module. The index's `governance_sources`
list was empty when this fixture was first written (it enumerated packet
copies removed in the tracked-home move); the generator was repointed at the
canonical homes later in the same round, so the projection now carries the
doctrine and craft sources and this cross-check resolves against it. The
doctrine and craft selections above were additionally verified against the
files directly.

The D3 amendment sites are additionally cross-checked against the D3
packet's own "What it amends" section, which names them.

## Suggested inferred additions (provenance: index adjacency)

RFC-0010 (3,096 words) — the envelope vocabulary the insertion copies
verbatim (objective, budgets, risk limits, protected surfaces, stop
conditions, write scope, tools, gates, evidence obligations, completion
predicate); a drafter checking that doctrine and contract say the same thing
in the same words should load it. Suggested, never mandatory: the doctrine
text is authored against doctrine, and RFC-0010's own status is one of the
questions the amendment leaves to the owner. Also
`.syzygy/map/topology-candidates/06-intent-to-reconciliation-flow.md`
(909 words, **candidate** — binds nothing) — the loop-flow view whose
trigger grain the amendment clarifies.

## Packet digest

sha256 over the mandatory files concatenated in listed order:
`958090be70dd525b…` (recompute: `cat <mandatory files> | sha256sum`).
Compiler: `context_load.py`, selection rules rev10-fixtures.

**Digest-source pinning.** This digest and the measured totals above are
computed over the **canonical-home bytes** as of 2026-08-05:
`doctrine:` resolves to `.syzygy/governance/doctrine/`, `rfcs/` to this
package. No packet copies of doctrine exist under this root any more, so
there is exactly one resolution and no silent source swap. A packet pins the
exact source digests it compiled from precisely so that a later change —
D3's own adoption amending `architecture.md` and `vision.md` in place, or
any corpus edit — **invalidates this packet rather than silently changing
what it meant**. A stale digest is the correct, visible outcome; a packet
whose contents drift under a fixed digest is not. (Live proof that this is
not hypothetical: three accepted-set fixtures no longer reproduce their
stated digests after the P-6 and P-7 fixes — see the fixture report.)

## Verification checklist (§15)

- [x] **All mandatory context included** — both amendment sites, the scope
      boundary, the amendment-log home, and the ceremony contract
- [x] **Unrelated modules excluded** — **30 of 32** RFC modules absent
      (2 loaded; count computed from `05-CONTRACT-INDEX.yaml`'s module
      list, not estimated)
- [x] **Stable output for identical inputs** — same argument list, same
      totals; order-independent (`context_load.py` sums a set)
- [x] **Budget respected or waiver emitted** — 15,574 est. tokens: above the
      5–15k default band by 574 tokens, disclosed; below the 20k
      justification trigger, so no waiver
- [x] **Omissions recorded** — every applicable candidate above is
      enumerated with a reason, including doctrine files, topology, and the
      historical lane
- [ ] **No generated summary replaces exact authority** — *not verifiable by
      the script.* The fixture names files; nothing checks that a consumer
      read the clause rather than an index or its own summary. See the
      fixture report's §5.
