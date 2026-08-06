# Context-selection fixture 5 — cross-project Mission

**Objective.** A governed task: draft a two-project Mission (objective,
envelope, budgets, stop conditions) for owner approval. Risk class:
portfolio authority — the mission and its envelope are RFC3-16(a)
artifacts (RFC10-9); no execution occurs inside this task.

**Selection rule trace (RFC11-4).** Warrant names a Mission → RFC-0010
(whole contract: identity, lifecycle, envelope, attention, portfolio
plane). Every mission-spawned run needs packets → RFC-0011 (whole).
Mission approval is an owner act under the two-state model → RFC-0003
`governance-homes-and-owner-acts` + README. Doctrine floor → `vision.md`
(VIS-4 always-human classes, the not-autonomous posture).

## Required context (mandatory, deterministic)

```
scripts/context_load.py rfcs/RFC-0010-mission-control-autonomy.md \
  rfcs/RFC-0011-context-compiler.md rfcs/RFC-0003/README.md \
  rfcs/RFC-0003/governance-homes-and-owner-acts.md doctrine:vision.md
```

Measured: **16,489 words ≈ 22,260 estimated tokens** — inside the 15–20k
working target.

## Omitted applicable candidates, with reasons

- RFC-0008 — deliberately **suggested, not mandatory**: at approval time
  the mission authorizes future materialization; the work-state contract
  binds when work items exist. The two-field consumption rule the
  drafter must not violate is restated at binding strength in RFC-0010 §5
  (RFC8-12/28/30). When the mission starts running, RFC-0008 becomes
  mandatory for its packets.
- RFC-0005 — the approving client's admission is the session's concern,
  not the draft's; envelope references to execution profiles are by
  RFC5-18 identity, carried in RFC-0010's text.
- RFC-0001/0002/0004/0006/0007/0009 — no kernel-entity, evidence, or
  surface change in the drafting task; per-project doctrine/contract
  pins enter the mission's own pinned-input list (RFC10-4), which the
  approval ceremony verifies, not this packet.
- Craft policies — no code, no tests.

## Why no applicable constraint was lost

The no-self-widening rule (RFC10-8), narrow-reading default (RFC10-7),
the two-plane authority split (RFC10-15 — neither project becomes
authoritative over the other), the act machinery the approval will use
(RFC3-16(a)/(b)/(c)), and the always-human floor (VIS-4) are all
mandatory-loaded. The mission's pinned inputs are identities resolved at
approval, not documents this packet must contain (RFC11-1 binds them by
identity).

## Suggested inferred additions (provenance: index adjacency)

RFC-0008 README + `identity-authority-materialization` (+4,607 words) if
the drafter wants materialization semantics in view; RFC-0005
`admission-and-boundary` if machine-client scopes for mission-affecting
acts (RFC10-3) are being set in the same draft.

## Packet digest

sha256 over the mandatory files concatenated in listed order:
`f276e732e5bd58a7…`.

**Selection: hand-authored golden selection. Measurement: mechanical.
Compiler implementation: absent.** `scripts/context_load.py` resolves a
path list it is handed and counts words; it has no notion of a task, a
warrant, a risk class, an `applies_to` value, or a dependency edge. The
selection above was made by a human and the trace is the reasoning that
produced it, written down — not a machine's output narrated afterwards.
The `Compiler: context_load.py, selection rules rev10-fixtures` line this
fixture used to carry was removed 2026-08-06: there is no compiler, and
`rev10-fixtures` resolved to nothing anywhere in the repository.

*Re-measured 2026-08-05 (refactor round): figures and packet digest refreshed after this round's recorded corrections to RFC-0003 governance-homes (P-6, +13 w) and the craft banners (P-7, security policy +26 w); selection unchanged. Prior figures/digest are in git history.*

*Re-measured 2026-08-05b by `scripts/check_governance.py` CG-18, which recomputes the digest and the word count from the declared mandatory set rather than trusting the recorded figures. Previous: 12,843 words, digest `c92c6f8a936b12b0…`. Selection unchanged; the movement is contract edits landing under a fixture that had no mechanical freshness check until now.*
