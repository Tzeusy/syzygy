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
| Kernel implementer | `kernel` | `rfcs/RFC-0001-project-graph-identity-state-planes.md` · `rfcs/RFC-0002/snapshot-and-evaluation-core.md` · `rfcs/RFC-0002/challenge-lifecycle.md` · `rfcs/RFC-0002/reconciliation-chain.md` · `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | 19,439 w ≈ 26,242 tok |
| Surface implementer — Polaris | `polaris` | `rfcs/RFC-0007/` (README + narrative-contract + rendering-and-surface) · `rfcs/RFC-0002/rendering-vocabularies.md` · `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | 17,207 w ≈ 23,229 tok |
| Surface implementer — Trajectory | `trajectory` | `rfcs/RFC-0008/` (README + identity-authority-materialization + state-vocabulary-and-cost + accounting-reconciliation-and-release) · `rfcs/RFC-0002/rendering-vocabularies.md` · `rfcs/RFC-0006-…` | 17,741 w ≈ 23,950 tok |
| Surface implementer — Orrery | `orrery` | `rfcs/RFC-0009/` (README + semantic-geography + visual-grammar-and-lenses + interaction-parity-and-release) · `rfcs/RFC-0002/rendering-vocabularies.md` · `rfcs/RFC-0006-…` | 24,166 w ≈ 32,624 tok |
| Adapter author | `kernel`, `trajectory`, `orrery` | `rfcs/RFC-0004/general-contract.md` · `rfcs/RFC-0004/named-adapters.md` · `rfcs/RFC-0008/state-vocabulary-and-cost.md` · `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | 13,286 w ≈ 17,936 tok |
| Security / execution-profile work | `kernel`, `machine-clients` | the relevant `rfcs/RFC-0005/` module · `rfcs/RFC-0003/governance-homes-and-owner-acts.md` · `doctrine:security.md` · `craft:security-and-secrets.md` | 7,968 w ≈ 10,756 tok (with `execution-profiles.md` as the relevant module) |
| Mission Control / CLI / MCP spec author | `mission-control`, `machine-clients` | `rfcs/RFC-0010-mission-control-autonomy.md` · `rfcs/RFC-0011-context-compiler.md` · `rfcs/RFC-0005/admission-and-boundary.md` · `rfcs/RFC-0006-…` · `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | 17,584 w ≈ 23,738 tok |
| Narrative author | `polaris` | `rfcs/RFC-0007/README.md` · `rfcs/RFC-0007/narrative-contract.md` · `rfcs/RFC-0002/rendering-vocabularies.md` · `doctrine:vision.md` | 12,046 w ≈ 16,262 tok |

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
- **T-2 — three fixture totals are stale by exactly the edits made since
  they were measured.** Fixtures 2 and 5 are +13 words (the RFC-0003
  `governance-homes-and-owner-acts.md` retired-phrase fix, 4,401 → 4,414 w);
  fixture 4 is +39 (that +13 plus +26 from this round's edits to
  `craft:security-and-secrets.md`, 820 → 846 w). No selection changed —
  only the measured size of an already-selected file.
- **T-3 — the reader-map rows are role-scoped and five of eight exceed the
  §11.4 20,000-token decomposition trigger.** Kernel implementer 26,242,
  Orrery surface 32,624, Trajectory surface 23,950, Mission Control 23,738,
  Polaris surface 23,229. 06 makes no token claim for the reader map, so
  this contradicts nothing — but a packet compiled from a role row rather
  than from a warrant will trip §11.4, and the routing should say so where
  the reader map is used as a selection input.
- **T-4 — `06-CONTEXT-LOAD-MAP.md` line 16 carries a stale module figure:**
  RFC-0003 governance-homes **4,401 w**, actual **4,414 w** as of
  2026-08-05. The rest of 06's per-module table reproduces exactly
  (`wc -w`, all 32 modules, same date).
