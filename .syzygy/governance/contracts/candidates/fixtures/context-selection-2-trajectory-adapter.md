# Context-selection fixture 2 — Trajectory work-provider adapter change

**Objective.** A governed work item: amend the substrate-to-normalized
work-state derivation mapping for a work-provider adapter (the RFC8-12
artifact). Risk class: **authorization-bearing** — the mapping widens what
the surface reports as live/dispatchable, so it is an RFC3-16(a) artifact.

**Selection rule trace (RFC11-4).** Warrant names the adapter and mapping →
RFC-0004 (`general-contract` + `named-adapters` + README) and RFC-0008
`state-vocabulary-and-cost` + README (RFC8-12/13 live there). The
risk/change class (authorization-bearing) pulls the owner-act machinery →
RFC-0003 `governance-homes-and-owner-acts` + README (RFC3-16(a)/(b)/(c)).
The untrusted-actor premise is doctrine → `security.md` (SEC-3).

## Required context (mandatory, deterministic)

```
scripts/context_load.py rfcs/RFC-0004/README.md \
  rfcs/RFC-0004/general-contract.md rfcs/RFC-0004/named-adapters.md \
  rfcs/RFC-0008/README.md rfcs/RFC-0008/state-vocabulary-and-cost.md \
  rfcs/RFC-0003/README.md rfcs/RFC-0003/governance-homes-and-owner-acts.md \
  doctrine:security.md
```

Measured: **18,282 words ≈ 24,681 estimated tokens** — **above the
15–20k working target, disclosed as a risk-class exception** (RFC11-11):
an authorization-bearing change may not shed its authorization contract
(RFC3-16(a) module) or the mapping's consuming vocabulary (RFC8-12/13
tables), and RFC11-5 forbids trimming mandatory context to fit a budget.
The lawful alternatives — sharding the task (mapping edit vs approval
ceremony as two packets) — are noted in the warrant; this fixture shows
the undivided form with the exception stated rather than hidden.

## Omitted applicable candidates, with reasons

- RFC-0004 `execution-record` and `fidelity-joins-and-mappings` — the
  mapping change touches ingestion classification, not execution-record
  capture or join semantics; their clauses are not cited by RFC8-12/13.
- RFC-0008 `identity-authority-materialization` and
  `accounting-reconciliation-and-release` — state derivation, not
  dispatch or accounting.
- RFC-0003 `manifests-and-namespace` — no manifest field changes.
- RFC-0005 — no client, consent, or profile surface touched (the
  owner-act ceremony's audit anchor RFC5-25 is cited inside RFC3-16(b)
  item 9 at binding strength).
- RFC-0001/0002/0006/0007/0009/0010/0011, craft — not cited by the
  warrant's clause set.

## Why no applicable constraint was lost

The three contracts that make this change dangerous are all fully
loaded: what a mapping may claim (RFC8-12/13, tables verbatim), what an
adapter may write (RFC-0004), and why the artifact is honored only under
owner-act provenance (RFC3-16(a), with the SEC-3 premise from
`security.md`). The exception path is a disclosure, not an omission.

## Suggested inferred additions (provenance: index adjacency)

RFC-0002 `rendering-vocabularies` (how derived states render downstream);
RFC5-25's clause (audit-trail location) if the ceremony itself is in
scope.

## Packet digest

sha256 over the mandatory files concatenated in listed order:
`614823e0930f2c88…`. Compiler: `context_load.py`, selection rules
rev10-fixtures.

*Re-measured 2026-08-05 (refactor round): figures and packet digest refreshed after this round's recorded corrections to RFC-0003 governance-homes (P-6, +13 w) and the craft banners (P-7, security policy +26 w); selection unchanged. Prior figures/digest are in git history.*

*Re-measured 2026-08-05b by `scripts/check_governance.py` CG-18, which recomputes the digest and the word count from the declared mandatory set rather than trusting the recorded figures. Previous: 18,315 words, digest `a398a06362074451…`. Selection unchanged; the movement is contract edits landing under a fixture that had no mechanical freshness check until now.*
