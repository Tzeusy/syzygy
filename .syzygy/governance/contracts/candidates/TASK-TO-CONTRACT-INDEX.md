# Task-to-contract index — derived, never authority

**Derived index (2026-08-05, human-clarity refactor round).** It answers one
question — *given a task, which contract modules must be loaded?* — by
restating what `06-CONTEXT-LOAD-MAP.md` and the modules' own front matter
already say. **`06-CONTEXT-LOAD-MAP.md` is the cited source and wins over this
file wherever they differ**; the modules win over both. Nothing here is a
clause, nothing here may be cited as authority, and this index selects nothing
on its own: mandatory selection is deterministic from the index metadata plus
the work warrant (RFC11-4), suggestion never suppresses (RFC11-5), and
incomplete context renders Unknown and by default blocks launch (RFC11-6).

**Machine lookup:** `05-CONTRACT-INDEX.yaml` (clause → module).
**Edge lookup:** `CONTRACT-DEPENDENCY-INDEX.md` (contract → contract).
**Measurement:** every figure below is `scripts/context_load.py` output,
re-run 2026-08-05 and re-runnable from this packet.

## How this index was derived, and what it could not be derived from

Charter §11.5 asks each module to declare `task_classes` and `risk_classes`,
and this index to be generated from them. **Those fields do not exist on any
of the 32 modules** (verified 2026-08-05 by a front-matter sweep of every
module: present are `id`, `title`, `status_source`, `governs`, `applies_to`,
`depends_on`, `provides_to`, `tags`, plus per-file `package` / `module` /
`modules` / `clauses`). So the task classes below are **not generated** —
they are the reader-map roles that `06-CONTEXT-LOAD-MAP.md` already states,
plus the five accepted fixtures in `fixtures/`, cross-checked against
`applies_to` and `governs`. This index is therefore a **transcription with
measurement**, not a projection, and it goes stale when 06 or a module
changes. See finding T-1.

## Task classes → modules to load

Straight from the reader map in `06-CONTEXT-LOAD-MAP.md` §"Reader map — who
loads what". The module paths and word figures are resolved and measured here;
the *membership* of each row is 06's, not this file's. Every package README
carries the deterministic clause-lookup rule, so a cited `RFCn-m` resolves to
one module without search (06, final bullet) — READMEs are named in a row only
where 06 names them.

| Task class | `applies_to` | Modules to load (per 06) | Measured |
|---|---|---|---|
| Kernel implementer | `kernel` | `rfcs/RFC-0001-project-graph-identity-state-planes.md` · `rfcs/RFC-0002/snapshot-and-evaluation-core.md` · `rfcs/RFC-0002/challenge-lifecycle.md` · `rfcs/RFC-0002/reconciliation-chain.md` · `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | 19,399 w ≈ 26,189 tok |
| Surface implementer — Polaris | `polaris` | `rfcs/RFC-0007/` (README + narrative-contract + rendering-and-surface) · `rfcs/RFC-0002/rendering-vocabularies.md` · `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | 17,186 w ≈ 23,201 tok |
| Surface implementer — Trajectory | `trajectory` | `rfcs/RFC-0008/` (README + identity-authority-materialization + state-vocabulary-and-cost + accounting-reconciliation-and-release) · `rfcs/RFC-0002/rendering-vocabularies.md` · `rfcs/RFC-0006-…` | 17,712 w ≈ 23,911 tok |
| Surface implementer — Orrery | `orrery` | `rfcs/RFC-0009/` (README + semantic-geography + visual-grammar-and-lenses + interaction-parity-and-release) · `rfcs/RFC-0002/rendering-vocabularies.md` · `rfcs/RFC-0006-…` | 24,137 w ≈ 32,585 tok |
| Adapter author | `kernel`, `trajectory`, `orrery` | `rfcs/RFC-0004/general-contract.md` · `rfcs/RFC-0004/named-adapters.md` · **`rfcs/RFC-0002/rendering-vocabularies.md`** · **`rfcs/RFC-0005/execution-profiles.md`** · `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | 14,346 w ≈ 19,367 tok |
| Security / execution-profile work | `kernel`, `machine-clients` | the relevant `rfcs/RFC-0005/` module · `rfcs/RFC-0003/governance-homes-and-owner-acts.md` · `doctrine:security.md` · `craft:security-and-secrets.md` | 7,956 w ≈ 10,741 tok (with `execution-profiles.md` as the relevant module) |
| Mission Control / CLI / MCP spec author | `mission-control`, `machine-clients` | `rfcs/RFC-0010-mission-control-autonomy.md` · `rfcs/RFC-0011-context-compiler.md` · `rfcs/RFC-0005/admission-and-boundary.md` · `rfcs/RFC-0006-…` · `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | 19,314 w ≈ 26,074 tok |
| Narrative author | `polaris` | `rfcs/RFC-0007/README.md` · `rfcs/RFC-0007/narrative-contract.md` · `rfcs/RFC-0002/rendering-vocabularies.md` · `doctrine:vision.md` | 12,033 w ≈ 16,245 tok |

**A reader-map row is a role's orientation, not a task packet.** Five of the
eight rows exceed the charter's 20,000-token decomposition trigger (§11.4);
four of the five accepted fixtures below, each scoped to *one* governed task
rather than to a role, stay under it — the exception is fixture 2, which 06
already carries as a **disclosed exception** with a sharding path. 06 claims
the 15–20k working target only for the fixtures, so this contradicts nothing
— but a packet compiled from a role row rather than from a warrant will trip
§11.4, and should be narrowed the way the fixtures narrow it.

## Measured task instances (`fixtures/`)

Each fixture is a worked selection for one governed task, with its own
omitted-candidate reasons and packet digest. These are the authoritative
worked examples of the selection rule; the rows above are the coarse map.
The five rows below are the **rev10 accepted fixture set**, which is exactly
what 06's measured-exercise table carries.

| # | Task | Risk class (fixture's own words) | Mandatory load, re-measured 2026-08-05 | As stated in the fixture |
|---|---|---|---|---|
| 1 | Polaris narrative/requirement change | content change on the intent surface; no code, no security surface | 13,864 w ≈ 18,716 tok | 13,864 / 18,716 — **current** |
| 2 | Trajectory work-provider adapter change | **authorization-bearing** (RFC3-16(a) artifact) | 18,315 w ≈ 24,725 tok | 18,302 / 24,707 — **stale, see T-2** |
| 3 | Orrery architecture-lens change | encoding-meaning change (channel registry, RFC9-26) | 14,134 w ≈ 19,080 tok | 14,134 / 19,080 — **current** |
| 4 | Security / execution-profile change | security surface, authorization-bearing | 10,893 w ≈ 14,705 tok | 10,854 / 14,652 — **stale, see T-2** |
| 5 | Cross-project Mission | portfolio authority (RFC10-9) | 12,843 w ≈ 17,338 tok | 12,830 / 17,320 — **stale, see T-2** |

`fixtures/` also holds **candidate fixtures 6, 7 and 8** (doctrine/shape
amendment, kernel identity change, OpenSpec requirement authoring), each
carrying its own `**Status:** DRAFT — a candidate fixture, not part of the
rev10 accepted fixture set (fixtures 1–5). Binds nothing.` banner. They are
therefore **correctly absent** from 06's table, they are in flight in this
round, and this index deliberately does not measure or route from them — a
draft fixture is not a task class.

## Findings

Recorded, not repaired — every one of them lives in a file outside this
index's authorization.

- **T-1 — the §11.5 task metadata does not exist.** No module declares
  `task_classes`, `risk_classes`, `terms`, `open_spec_mapping_status`, or
  `lifecycle` (`status_source` carries the lifecycle role instead). This
  index therefore cannot be generated and cannot be drift-checked the way
  `05-CONTRACT-INDEX.yaml` and `CONTRACT-DEPENDENCY-INDEX.md` can. Adding
  those fields is a change to files inside act 1's digest set and is not
  made here.
- **T-2 — RETIRED 2026-08-05b, and it was wrong when written.** It named
  three fixture totals as stale. All **eight** were stale, and the fix is
  now mechanical: `check_governance.py` CG-18 recomputes every fixture's
  digest and word count from its declared mandatory set, and all eight were
  corrected. See `round-2026-08b/FINAL-CONTEXT-COMPILER-FIXTURE-REPORT.md`.
- **T-3 — still true, and worse.** The reader-map rows are role-scoped and
  **six of eight** now exceed the §11.4 20,000-token decomposition trigger:
  Orrery surface 32,585, Kernel implementer 26,189, Mission Control 26,074
  (was 23,738 — RFC-0010's correction plane), Trajectory surface 23,911,
  Polaris surface 23,201, and Adapter author is now 19,367, just under. 06
  makes no token claim for the reader map, so this contradicts nothing — but
  a packet compiled from a role row rather than from a warrant will trip
  §11.4, and the routing should say so where the reader map is a selection
  input.
- **T-4 — RETIRED 2026-08-05b, and it was wrong when written.** It named one
  stale figure in `06-CONTEXT-LOAD-MAP.md` and asserted "the rest of 06's
  per-module table reproduces exactly (all 32 modules)". **Eleven of eleven
  contract rows were stale**, one by 1,745 words. The universal claim was
  written without the sweep it describes. All rows are regenerated, and
  CG-20 now recomputes every figure in that table against its module.
- **T-5 — the Adapter-author row was wrong in both directions, corrected
  2026-08-05b.** It omitted `RFC-0002/rendering-vocabularies.md`, which owns
  RFC2-25 — the tier registry defining `gate-backed` / `report-fact` /
  `asserted-by-worker`, the vocabulary RFC4-13 emits and cites five times —
  and `RFC-0005/execution-profiles.md`, which owns RFC5-21, the profiled run
  that *is* `gate-backed` route 1. It carried `RFC-0008/state-vocabulary-and-cost.md`,
  which is in RFC-0004's derived `provides_to`, not its `depends_on`. A
  packet compiled from the old row was incomplete against the package's own
  declared dependencies, which RFC11-6 makes Unknown and blocks launch on.
  Found by a fresh-engineer review attempting the task, not by a check.
- **T-6 — this index is still hand-maintained, and that is the root cause of
  T-2 through T-5.** Every defect above is a derived figure that drifted
  because nothing recomputed it. Two of them now have checks (CG-18, CG-20);
  the reader-map totals in this file do not, because the row *membership* is
  editorial and cannot be derived until T-1's task metadata exists.
