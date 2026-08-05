# Context-load map — reader map and measured load tests (directive §5/§7)

> **Derived measurement record — never authority.** This map reports what a
> task must load and what that costs; it states no obligation. The contracts
> it routes to own their own meaning, and where this map and a contract
> disagree, the contract wins and this map is stale. Its packet-size figures
> are a measured working target under RFC11-11, not a policy limit — the
> policy-side trigger table is candidate `CC-BUDGET-1`
> (`policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md`); the two
> instruments measure the same thing on different scales and neither
> overrides the other absent an owner act.

## The corpus, as loadable modules

11 contracts → **32 modules** (7 packages + 2 single-file RFCs + RFC-0010 +
RFC-0011 + 7 package READMEs), mean normative module ~3,500 words. Machine
lookup: `05-CONTRACT-INDEX.yaml` (regenerable:
`scripts/build_contract_index.py --check`). Word measurement for any
selection: `scripts/context_load.py <paths>` — all figures below are its
output, re-runnable from this packet.

| Contract | Modules (words) |
|---|---|
| RFC-0001 | single, 8,342 (justified oversize — dictionary; see 03 report) |
| RFC-0002 | core 1,955 · challenge 2,225 · reconciliation 2,470 · rendering 2,388 · README 1,809 |
| RFC-0003 | manifests 4,819 · governance-homes 4,407 · README 913 |
| RFC-0004 | general 1,677 · adapters 3,682 · execution-record 1,770 · fidelity 1,737 · README 1,670 |
| RFC-0005 | admission 3,635 · consent-egress 2,343 · profiles 2,192 · README 1,997 |
| RFC-0006 | single, 4,167 |
| RFC-0007 | narrative 5,165 · rendering 3,142 · README 2,324 |
| RFC-0008 | identity/materialization 2,684 · state/cost 3,504 · accounting 3,051 · README 1,918 |
| RFC-0009 | geography 6,996 · grammar/lenses 5,538 · parity/release 3,023 · README 2,025 |
| RFC-0010 | single, 4,841 |
| RFC-0011 | single, 2,264 |

## Reader map — who loads what

- **Kernel implementer:** RFC-0001 + RFC-0002 (core, challenge,
  reconciliation) + RFC-0003 governance-homes.
- **Surface implementer (any):** owning surface package + RFC-0002
  rendering + RFC-0006.
- **Adapter author:** RFC-0004 (general + adapters) + RFC-0008 state/cost
  + RFC-0003 governance-homes.
- **Security/profile work:** RFC-0005 (relevant module) + RFC-0003
  governance-homes + doctrine `security.md` + craft security policy.
- **Mission Control / CLI / MCP spec author:** RFC-0010 + RFC-0011 +
  RFC-0005 admission + RFC-0006 + RFC-0003 governance-homes.
- **Narrative author:** RFC-0007 (README + narrative) + RFC-0002
  rendering + doctrine `vision.md`.
- Every package README carries the deterministic clause-lookup rule, so a
  cited `RFCn-m` resolves to one module without search.

## Measured context-selection exercises (fixtures/, directive §7)

| # | Task | Mandatory load | Tokens (est) | Within 15–20k target |
|---|---|---|---|---|
| 1 | Polaris narrative change | 13,864 w | 18,716 | ✓ |
| 2 | Work-provider adapter mapping change | 18,315 w | 24,725 | **disclosed exception** — authorization-bearing risk class; sharding path stated in fixture |
| 3 | Orrery lens change | 14,134 w | 19,080 | ✓ |
| 4 | Execution-profile amendment | 10,893 w | 14,705 | ✓ |
| 5 | Cross-project Mission draft | 12,843 w | 17,338 | ✓ |

Baseline displaced: rev9's only safe instruction was whole-corpus loading —
~123,200 words ≈ 166,300 estimated tokens per task (re-measured 2026-08-05). Median fixture load is
**~11% of that**. The token heuristic (words × 1.35) is stated in
`context_load.py`; the acceptance target is a working policy figure, **not
doctrine** (RFC11-11; RFC 0011 §8 q1 leaves its custody to the owner).


> *Figures re-measured 2026-08-05 after this round's recorded P-6/P-7 corrections (see the fixtures' own re-measure notes). This map covers the five accepted-set fixtures; draft fixtures 6–8 are measured in `round-2026-08/CONTEXT-COMPILER-FIXTURE-REPORT.md` and are deliberately not routed from here until reviewed.*

## Rules the map rides on

Mandatory selection is deterministic from the index metadata + warrant
(RFC11-4); suggestion never suppresses (RFC11-5); incomplete is Unknown and by
default blocks launch — proceeding on disclosed-incomplete context needs
an explicit, owner-visible relaxation (RFC11-6); the index is a
rebuildable projection, never a second truth store (RFC11-7). Each fixture
records its omitted-candidate reasons and packet digest.
