# Convergence preflight — round 2026-08i

> **A dated verification snapshot, valid only for the commit it names.**
> Verified this session (2026-08-17) at `HEAD = 9c43fc5` unless a line says
> otherwise. Where this page and an owning record disagree, the record wins.
> Truncated hashes are orientation only — the owning record holds the value.

## Repository state

- **HEAD:** `9c43fc5` (2026-08-16). Working tree clean apart from the
  convergence pass prompt (untracked) and this round's own artifacts.
  `[Observed]`
- **Check battery at HEAD, run this session:** 32 OK, 18 WARN, 0 FAIL
  (50 checks); CG-7 act-argument digest checks among the OK set. `[Observed]`

## Wave A / Wave B

- **Wave A (RFC 0001–0006, 19 modules):** `VERDICT: CONFIRM` (RD-31b) bound
  to the current manifest argument (`8972d963`, per
  `wave-manifests/WAVE-A-MANIFEST.txt` and acceptance record §1). The P-33
  obstacle is ruled — install shape **(M)**, zero bytes moved, confirmation
  preserved (`WAVE-A-INSTALL-SHAPE-DECISION.md`). **Offer unblocked; act not
  performed.** `[Observed]`
- **Wave B (RFC 0007–0009 + three surfaces, 11 modules):** `VERDICT: CONFIRM`
  (RD-32c) on the current argument (`193e3c1e`). Nothing withholds it; it
  follows Wave A. **Act not performed.** `[Observed]`
- `decisions/ACCEPTANCE-ACT-RECORD.md` does not exist — correct, the first
  act creates it. `[Observed]`

## Resolved launch decisions (owner rulings, recorded)

Per `PENDING-OWNER-DECISIONS.md` "Resolved on 2026-08-16" and the named
owning records:

- **P-31** — RFC2-19(a) ratified as drafted (SDR-34).
- **P-33** — install shape **(M)**; confirmation-preserving; zero bytes.
- **P-34** — launch-gate **v2.4 approved as process policy, arm (a)**, with
  two disclosed BLOCKING residuals (RD-67 f1: abbreviated
  `repository_commit` lets the schema load from `HEAD`; RD-68 f1:
  `U+2800`/category-`So` defeats the invisible-character strip); **F5 not
  promoted**. Ten `REVISE` verdicts across v2.0–v2.4 stand as recorded;
  the approval is approval-with-residuals, not a clean verdict.
  Owning record: `LAUNCH-GATE-AUTHORITY-DECISION.md`.
- **P-35** — operating constraints, option (a) (table recorded, Unknowns
  kept).
- **P-36** — Unknown vs Gap two-term rule (SDR-35).
- **P-37** — seven facets, no rollup, drafting site a2 = the Capability 1
  specification (SDR-36).
- **P-38** — human entry as drafted, option (a) (`HUMAN-ENTRY-DECISION.md`).
- **P-39** — OpenSpec pinned at **1.9.0** (`GOVERNANCE-SUBSTRATE-LOCK.yaml`).
- **P-40** — one change ⇄ one coherent capability (SDR-37).

## Remaining launch decisions and acts

1. Owner performs the **Wave A act**, then the **Wave B act**.
2. **P-41 + P-42** — the joint specification-acceptance and shape-to-spec
   impact craft acts. The only subject still eligible for one repair/review
   cycle.
3. **Formal launch administration** under approved v2.4 — out-of-family
   model or human reviewer.
4. Owner's separate **launch decision**.

Open but **not** launch-gating: P-43, P-44 (declining is an arm), P-12,
P-14, and the C/D-deferred rows — each states its own earliest gate.

## P-41 / P-42 exact state

- Candidates: `policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`
  (CC-SPEC-1…10) and `…/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`
  (CC-IMPACT-1…7). Reviewed as **RD-51, `VERDICT: REVISE`** (20 findings);
  **amended 2026-08-13** against it; the repaired bytes are **unreviewed**.
  The P-40 prerequisite on CC-SPEC-1 is now satisfied. The CC-IMPACT blind
  fixture has been run and passed (RD-59). `[Observed]`
- Owner packets (`SPECIFICATION-ACCEPTANCE-DECISION.md`,
  `SHAPE-TO-SPEC-IMPACT-DECISION.md`): reviewed **RD-63 / RD-64, both
  `VERDICT: REVISE`** (2026-08-16, frozen at `918574c`), repaired per
  `round-2026-08h/reviews/DISPOSITION-REGISTER.md`; those repairs are
  **unconfirmed**. Several packet prerequisite statements ("rule P-40
  first") were written before the 2026-08-16 rulings landed and are now
  satisfied, not wrong. `[Observed]`

## Launch gate and formal administration

- Instrument `launch-gate-pre-specifications.md` at **v2.4**, owner-approved
  process policy (P-34). Instrument/schema digests: quoted only in
  `LAUNCH-GATE-AUTHORITY-DECISION.md`, verified there by the battery.
- **No formal administration has been run.** The only administration on
  record is the 2026-08-09 **pilot** at v1.3, `GATE VERDICT: NOT READY`.
  `[Observed]`

## OpenSpec and implementation

- `openspec/` holds a tool-created scaffold only — one tracked
  `config.yaml` plus empty trees; **zero specification content**.
  `[Observed]` (`find openspec -type f` → 1 file, this session.)
- **No implementation** — no `src/`, `apps/`, `packages/`, no product
  toolchain manifest. `[Observed]`

## Stale default-path statements (this pass's Workstream A subjects)

- `PROJECT-STATUS.md` (as-of 2026-08-11): "Eleven rulings … prepared, never
  made"; "Next lawful step: Rule P-33"; P-34 listed open. All superseded by
  the 2026-08-16 rulings. `[Observed]`
- `AGENTS.md` carries a `# Notes to self` section on the default path.
- `PENDING-OWNER-DECISIONS.md` header notes its own launch-scope index rows
  are struck through rather than removed; its P-34 index bullet still reads
  "remains open" below the ruled banner. `[Observed]`
