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
RFC-0011 + 7 package READMEs). Machine lookup: `05-CONTRACT-INDEX.yaml`
(regenerable: `scripts/build_contract_index.py --check`).

**Module sizes are not listed here.** They were, per contract, and eleven of
eleven rows went stale — one of them badly — while the paragraph above them
said the figures were "re-runnable from this packet". A fresh engineer caught
two by hand and then correctly stopped trusting the file, which is the real
cost of a stale derived view: it does not merely mislead, it spends the
reader's trust in everything around it. Current per-module measurement lives
in the generated `CONTEXT-BUDGET-REPORT.md` §3, and the measurement of any
selection you make is `scripts/context_load.py <paths>`.

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

## Measured context-selection exercises (fixtures/)

Nine fixtures live in `fixtures/`. Each states its own mandatory selection,
its omitted candidates with reasons, and its packet digest; each one's
measurement is **written by a generator and verified by a second, independent
one** — `scripts/build_budget_report.py` writes the anchored figure and
`scripts/check_governance.py` CG-18 recomputes it from the fixture's own
declared load command.

**The per-fixture figures that used to sit in this table are gone**, for the
reason above: they were a third copy of a measurement whose first copy is the
fixture and whose second is now generated. Read
`CONTEXT-BUDGET-REPORT.md` §1 for all nine, with each one's disposition
against the proposed decomposition trigger, and §2 for the candidate budget
exceptions with their reviewer, scope and expiry.

What the fixture set is *for* survives the deletion and is worth stating
plainly: **rev9's only safe instruction was to load the whole corpus.** The
selections below it are a small fraction of that. The exact fraction is a
measurement and lives with the other measurements.

## Rules the map rides on

Mandatory selection is deterministic from the index metadata + warrant
(RFC11-4); suggestion never suppresses (RFC11-5); incomplete is Unknown and by
default blocks launch — proceeding on disclosed-incomplete context needs
an explicit, owner-visible relaxation (RFC11-6); the index is a
rebuildable projection, never a second truth store (RFC11-7). Each fixture
records its omitted-candidate reasons and packet digest.
