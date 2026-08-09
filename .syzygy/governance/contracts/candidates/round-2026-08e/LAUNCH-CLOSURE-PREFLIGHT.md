# Launch-closure preflight — round 2026-08e

> **Historical snapshot — non-authoritative round record.** Written before
> any repair of this pass; every figure below was measured this session at
> the stated HEAD, by the stated method. Where a later artifact and this file
> disagree, the later artifact wins and this file is a snapshot. The act
> arguments it quotes are the *pre-repair* ones and are quoted as history,
> never as an offer.

- **Session date:** 2026-08-10
- **Charter:** `syzygy_fable_launch_gate_capability1_closure_prompt.md`
  (repo root, untracked — the owner's working copy; it is the cause of the
  one CG-2a FAIL below and is never committed)
- **Parallel-lead check:** clean — checkpoint tail is the 2026-08-05 round
  close; newest `reviews/` mtime (2026-08-09 21:56) matches this track's own
  predecessor commits at HEAD; nothing modified today by another session.
  [Observed]

## 1. Repository state

| Item | Value |
|---|---|
| Branch | `main`, up to date with `origin/main` |
| HEAD | `e69c9239a95534411a2da6659dbb7cadbfa5f70a` — "governance: the launch-gate instrument itself, committed beside its first answers" |
| Working tree | clean apart from the untracked charter file |
| Tracked files | 308 (`git ls-files | wc -l`); 297 texty (extensions `.md`, `.txt`, `.yaml`, `.yml`, `.py`) |
| Application code | none — `openspec/`, `src/`, `apps/`, `packages/` absent; 0 tracked files with code extensions (`ts/js/go/rs/java/c/cpp/rb`) [Observed] |
| CI | `.github/workflows/governance-docs.yml` — documentation-only battery |
| Clone verification | `round-2026-08d/CLONE-VERIFICATION.md`, valid **only for `771965c`** — 4 commits behind HEAD; a fresh clone run is owed before any new "clean" claim |

## 2. Launch gate

| Item | Value |
|---|---|
| Instrument | `launch-gate-pre-specifications.md` **v1.3** (§9 changelog), tracked at HEAD |
| Instrument sha256 | `5b5e76535ebab73ec06351eb16094882f79d01b8eb786883b1411f4f0ebc49ad` |
| Administrations | exactly one — 2026-08-09, at commit `067d8a0`, reviewer Anthropic Claude (same family as the corpus authors; the record itself flags this) |
| Raw record | `round-2026-08d/reviews/LAUNCH-GATE-ADMINISTRATION-2026-08-09-RAW.md` (immutable) |
| Result | **GATE VERDICT: NOT READY** — 12 Met, 17 Not met (all six E questions among them), 2 Unknown (A5, F1); G1 completed with four proposed questions (F5 assurance independence, G2 instrument capture, F6 governance-per-increment, C7 successor recoverability) |
| Pilot defects (why it is not the formal baseline) | the instrument was untracked at the administered commit; no instrument digest recorded in the record; no parameter-block digest recorded; same-family reviewer. All four are §7.2 grounds in this pass's charter. [Observed] |

## 3. Wave structure and act arguments

Six wave acts (round-2026-08d design), none performed;
`decisions/ACCEPTANCE-ACT-RECORD.md` correctly absent. Manifest digests
(= act arguments) at HEAD, from `sha256sum` this session — the acceptance
record owns the quoted arguments; CG-7a verifies them every run (78 entries,
0 findings):

| Wave | Manifest sha256 |
|---|---|
| A (RFC 0001–0006, 19 modules) | `8d4f3e723f0ec6a7645cd70abc0d5fe5ebdc6fe1b27e9faa5ad29761613e7816` |
| B (RFC 0007–0009, 11 modules) | `daa6a5dd37b7f92ac4ba4fc8a7bb491ecbffc02ba43227448f64f88dc3c3bebb` |
| C1 (RFC-0011 packet module + index) | `a5d3ba1f22ad0ff5ff66485b1829e5b2f652a8c7678dcc96699eaca4ac5b2b4d` |
| C2 (RFC-0011 selection module) | `acd27bb8f9b7be76725057b4280e2dc9fe23f3e9fac17c448542b9cb250d8b1a` |
| D1 (RFC-0010 prevention plane, 5 files) | `570e617091bb41d8b34ca17b09e12f41d22e4d592a23249c8a737a698f8c0dff` |
| D2 (RFC-0010 correction plane, 1 file) | `ab590e3e553a2f1f2db92d1c676a0fd5c05d2283548163e5c3663df5a31382d8` |

## 4. Reviews and dispositions

- **Fifteen round-2026-08d reviews delivered, all fifteen `VERDICT: REVISE`,
  zero `CONFIRM`** — nine dimension (RD-9…RD-17), six wave exact-package
  (RD-18…RD-23); verdicts register:
  `round-2026-08d/reviews/DELIVERY-AND-VERDICT-REGISTER.md`. All reviews
  bound to baseline commit `771965c`. [Observed]
- **173 findings, all disposed** in
  `round-2026-08d/reviews/DISPOSITION-REGISTER.md`: batches R-A, R-B, R-D1,
  R-D2, R-C1, R-C2, R-FIX, R-REC, R-SCR, R-OVW (+R-TOP added by §8), seven
  cross-cutting designs X1–X7, five owner questions P-29…P-33, two recorded
  non-findings. **No repair has landed**: nothing in `rfcs/`, fixtures,
  the acceptance record, or wave manifests edited since `771965c` in
  response to these reviews. [Observed — the manifests regenerate clean]
- Launch-gate administration findings routed into the same batches by the
  register's §8 (added 2026-08-09).

## 5. Owner decisions open

P-1…P-5 (the acts), P-10, P-12, P-14…P-25, P-27…P-33 in
`decisions/PENDING-OWNER-DECISIONS.md`; twelve packets in
`round-2026-08d/OWNER-DECISION-PACKETS.md`. **None ruled.** The charter's
owner-direction block (this pass) additionally fixes: launch target =
Capability 1; required waves = A+B; C1/C2/D1/D2 visibly deferred.

## 6. Governance battery at HEAD (read output, not exit code)

- `check_governance.py`: **24 OK, 15 WARN, 1 FAIL (40 checks)**. The FAIL is
  CG-2a on the untracked charter file (`…closure_prompt.md:297` quotes the
  retired phrase in its search list) — 298 files examined, 1 finding, none
  in tracked state. The 15 WARNs are the declared-by-design classes.
- `--selftest`: **78 fixtures, 0 failing**; CG-24: **16 of 24 check families
  have at least one fixture** (uncovered: CG-1…6, CG-9, CG-10).
- `verify_final_prespec.py`: PASS; **341 numbered clauses**; total 110,081
  words over the 35–50k band (declared, justification carried).
- All four generators `--check` clean: contract index, dependency index,
  budget report ("fixture anchors match regeneration"), all 7 manifests.

## 7. Sweeps (Python `re` over `git ls-files`, denominator 297 texty files)

| Token | Hits | Live-presented (outside allowlisted history/reviews) |
|---|---|---|
| `ACCEPT FOUNDATIONAL RFCS` (rev9, retired) | 31 | 0 — CG-2a green on tracked state |
| `ACCEPT COMPACTED FOUNDATIONAL RFCS` (rev10, retired) | 38 | **5 files present it as current**: `rfcs/RFC-0003/governance-homes-and-owner-acts.md:86` (Wave A digest set), `map/topology-candidates/README.md:44-47` (act-3 digest set), `policies/craft-and-care/INSTALL-RECORD.md:22-24` (in force), `02-OWNER-DIRECTION-RECORD.md:89`, `09-OPEN-SPEC-READINESS-REPORT.md:17`. **CG-2a is blind to this phrase** — `RETIRED_PHRASE` constant (`check_governance.py:427`) names only the rev9 phrase. |
| `ready, conditional` | 3 | 1 — `09-OPEN-SPEC-READINESS-REPORT.md:20`, unbannered "Verdict: ready" |
| `199 clause` | 5 | 1 — `SURFACE-CLAUSE-ROUTING-MATRIX.md:19` (matrix holds 210 rows; CG-17 confirms 210) |
| `322 clause` | 19 | 3 active-lane: `09-…REPORT.md:11,13`, `10-EXIT-REPORT.md:80`, `FINAL-…-ACCEPTANCE-RECORD.md:370` (verifier prints 341) |
| `Nine fixtures` | 3 | 1 — `06-CONTEXT-LOAD-MAP.md:47` (ten exist) |
| `rfcs/RFC-0010-mission-control-autonomy.md` (dead path) | 51 | active-route: `TASK-TO-CONTRACT-INDEX.md:49`, `SURFACE-CLAUSE-ROUTING-MATRIX.md:798`, `04-CLAUSE-MIGRATION-MATRIX.md:1044`, `10-EXIT-REPORT.md:112` |
| `rfcs/RFC-0011-context-compiler.md` (dead path) | 45 | active-route: `TASK-TO-CONTRACT-INDEX.md:49`, `SURFACE-CLAUSE-ROUTING-MATRIX.md:926`, `04-CLAUSE-MIGRATION-MATRIX.md:1045`, `10-EXIT-REPORT.md:113` |

(`06-CONTEXT-LOAD-MAP.md`'s dead RFC-0010/0011 routes at `:38-39` are
whole-word path references caught by the pilot; they sit among the 51/45.)

## 8. Default reading path and task routing at HEAD

- Default path: `README.md` → `PROJECT-STATUS.md` → `intent/OVERVIEW.md` →
  `doctrine/vision.md`; agents additionally `AGENTS.md`.
- Task-routing artifacts (competing, per pilot D2): `AGENTS.md` routing
  table → `06-CONTEXT-LOAD-MAP.md`; `TASK-TO-CONTRACT-INDEX.md` (declares
  the load map wins, and its T-5 records the load map's designated answer
  wrong); `SURFACE-CLAUSE-ROUTING-MATRIX.md` ("May I implement X?").
- Stale/superseded reachable without banner: the five-file retired-phrase
  set above; `09-OPEN-SPEC-READINESS-REPORT.md`; the matrix totals block;
  the load map's fixture count and adapter row. `CONTEXT-BUDGET-REPORT.md`
  as-of matches its regeneration check this session (drift check clean).

## 9. Charter §1 posture statements — verification result

All eleven statements verified true at HEAD, with two precisions:
the administration's Not-met count is **17** (its own part-5 header
briefly said 16 and the record's addendum corrects itself — the
enumeration was always 17); and the disposition register carries
**173 findings** of which 2 are recorded non-findings. No correction to
current records required before proceeding. [Observed]

## 10. Sequencing constraints this pass honors

1. Disposition register §8: the **R-SCR CG-2 extension lands before the
   phrase-sweep repairs** it checks.
2. Register §2: R-SCR/R-REC draft immediately; wave batches after the
   P-29/P-30 rulings **for C/D waves only** — this pass defers C/D waves
   entirely (charter owner-direction 3/6), so R-A and R-B proceed now.
3. Verification rule 10: reviews bind digests; the round-08d reviews remain
   the verdicts for `771965c`; each repaired wave gets a scripted manifest
   regeneration and a **fresh exact-package review of the new bytes** before
   it may be offered.
4. No owner act is performed by this pass; every gate is prepared, none
   fired.
