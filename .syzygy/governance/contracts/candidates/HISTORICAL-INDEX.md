# Historical and superseded artifacts — index

> **Generated-style navigation, never authority.** One row per
> historical/superseded artifact class reachable from this tree, so the
> active lane stays walkable without archaeology. Everything listed is
> **append-only history**: banner-marked at its own head where a reader
> could otherwise mistake it for current. If an artifact below appears on
> any default route as current, that is an F4 finding — report it.
> Maintained by hand at each round close (candidate for generation).

## Superseded current-lane artifacts (banner-marked in place)

| Artifact | Superseded by | Since |
|---|---|---|
| `09-OPEN-SPEC-READINESS-REPORT.md` | the launch-gate instrument + `PROJECT-STATUS.md` + `FIRST-OPENSPEC-SEQUENCE.md` | 2026-08-10 |
| `round-2026-08d/FIRST-OPENSPEC-SEQUENCE.md` (rev 2) | `FIRST-OPENSPEC-SEQUENCE.md` (rev 3, candidates root) | 2026-08-10 |
| `round-2026-08d/OWNER-DECISION-PACKETS.md` packets 2/7/8/10/11 | the five `decisions/*-DECISION.md` packets | 2026-08-10 |
| `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md` | `SURFACE-CLAUSE-ROUTING-MATRIX.md` | round-2026-08b |
| `history/TASK-TO-CONTRACT-INDEX.md` (moved off the active lane 2026-08-18, Administration 1 F2) + the load map's reader table | `TASK-ROUTER.md` (generated) | 2026-08-10 |
| `round-2026-08c/OWNER-DECISION-PACKETS.md` | round-08d packets, then the `decisions/` packets | 2026-08-09 |

## Historical rounds (whole directories; each has its own banners)

Eleven closed rounds, in the order they were recorded. Dates are each
directory's first-commit date; none is on a default path, and none is
authority.

| Directory | Recorded | What it holds |
|---|---|---|
| `round-2026-08/` | 2026-08-05 | Human-clarity refactor: charter, dispositions, superseded acceptance record and readiness report, archive index, reviews RB-1..8 |
| `round-2026-08b/` | 2026-08-05 | Term closure, dependency closure, superseded acceptance record, reviews RC-1..12 |
| `round-2026-08c/` | 2026-08-07 | Structural closure: superseded offering, readiness and clone reports, reviews RD-1..8 |
| `round-2026-08d/` | 2026-08-09 | Wave split and review pass: work order, wave design, verdict and disposition registers, reviews RD-9..23, and the launch-gate pilot administration (immutable) |
| `round-2026-08e/` | 2026-08-10 | Launch closure: preflight, launch-gate v1.4–v1.18 semantic deltas, Wave A and Wave B closure reports and deltas, reviews |
| `round-2026-08f/` | 2026-08-11 | Capability 1 readiness: context-route report, owner decision packet, spec-outline exercise, launch-gate v2.0 delta, the P-33 semantic install analysis, final public clone report. **Holds a live CI input** — see the note below |
| `round-2026-08g/` | 2026-08-13 | Owner-decision, launch-policy and specification-discipline closure: Capability 1 owner-decision index, planning-charter and default-path-currency accounts, launch-gate v2.1 and v2.2 deltas, shape-to-spec fixture 2 and its answer key |
| `round-2026-08h/` | 2026-08-16 | Launch-gate v2.3 and v2.4 semantic deltas, and their reviews. Its closure record is `reviews/DISPOSITION-REGISTER.md`, one level down rather than at the round's top level as in every other round |
| `round-2026-08i/` | 2026-08-17 | Convergence preflight: Capability 1 outline exercise 2, governance reduction plan (later revision), spec-acceptance-and-impact delta 2, pass checkpoint |
| `round-2026-08j/` | 2026-08-18 | The repair pass after Administration 1: disposition register, the thesis risk ordering (B5 settlement), and the C2-normative-population and D3-coined-term sweeps with their scripts |
| `round-2026-08k/` | 2026-08-20 | Capability 1 specification review binding (Pass 2 reviews RS-1..3 bound to exact bytes), and the prepared adoption act and implementation authorization |

**Historical does not mean unreferenced — one round holds a live CI input.**
`.github/workflows/governance-docs.yml` runs
`scripts/validate_launch_administration.py` and
`render_launch_administration.py` against
`round-2026-08f/fixtures/DRY-RUN-ADMINISTRATION.json` on every push. That
fixture is a *current* test input living inside a closed round, so moving or
deleting the directory would break CI, not merely orphan a citation. Rounds
`h`, `i`, `j` and `k` are likewise cited as evidence by decision and act
records that are in force today. Read every round as closed *process* record;
do not read "closed" as "safe to relocate" without sweeping for citers first.
[Observed — swept 2026-09-05: the workflow reference is two `run:` lines in
`.github/workflows/governance-docs.yml`.]

Companions, not rounds:

| Directory | What it holds |
|---|---|
| `history/` + `history/rev9-rfcs/` | The frozen rev9 corpus and per-RFC amendment history |
| `matrix-rows/` | Per-contract routing row sources |
| `reviews/` (candidates root) | rev10-era reviews and dispositions |

## Repeated filenames — which copy is last

Twelve filenames occur in more than one round, each a successive revision
and no two byte-identical. A basename alone therefore identifies nothing:
resolve it here, or by first-commit date, before citing one. Three of these
families are named `FINAL-…` and are not final.

| Filename | Copies, oldest → newest | The last one |
|---|---|---|
| `FINAL-PRE-SPECIFICATION-READINESS-REPORT.md` | `round-2026-08/`, `round-2026-08b/`, `round-2026-08c/` | `round-2026-08c/` |
| `FINAL-PUBLIC-CLONE-REPORT.md` | `round-2026-08c/`, `round-2026-08f/`, `round-2026-08g/` | `round-2026-08g/` |
| `FINAL-CAPABILITY-1-READINESS-REPORT.md` | `round-2026-08f/`, `round-2026-08g/`, `round-2026-08i/` | `round-2026-08i/` |
| `P33-SEMANTIC-INSTALL-ANALYSIS.md` | `round-2026-08f/`, `round-2026-08g/` | `round-2026-08g/` |
| `GOVERNANCE-REDUCTION-PLAN.md` | `round-2026-08e/`, `round-2026-08i/` | `round-2026-08i/` |
| `FIRST-OPENSPEC-SEQUENCE.md` | `round-2026-08c/`, `round-2026-08d/` | the candidates-root copy (rev 3) supersedes both |
| `OWNER-DECISION-PACKETS.md` | `round-2026-08c/`, `round-2026-08d/` | the five `decisions/*-DECISION.md` packets supersede both |
| `FINAL-HUMAN-CLARITY-REVIEW.md` | `round-2026-08/`, `round-2026-08b/` | `round-2026-08b/` |
| `FINAL-OWNER-ACCEPTANCE-RECORD.md` | `round-2026-08/`, `round-2026-08b/` | superseded by `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` |
| `PUBLIC-CLONE-VERIFICATION-REPORT.md` | `round-2026-08/`, `round-2026-08b/` | `round-2026-08b/` |
| `DELIVERY-AND-VERDICT-REGISTER.md` | `round-2026-08d/reviews/`, `round-2026-08e/reviews/` | `round-2026-08e/reviews/` |
| `DISPOSITION-REGISTER.md` | `reviews/` under rounds `d`, `e`, `f`, `g`, `h` | `round-2026-08h/reviews/` |

[Observed — swept 2026-09-05 over every `.md` under the eleven round
directories, grouped by exact basename and compared by sha256: 12 of 217 distinct
basenames have more than one copy, and no two copies inside a family are
byte-identical. Ordering is each copy's `git log --diff-filter=A` date.
Re-run the sweep rather than trusting this table after any new round.]

## Retired identities (never reused)

- Acceptance phrases: rev9 `ACCEPT FOUNDATIONAL RFCS`; rev10
  `ACCEPT COMPACTED FOUNDATIONAL RFCS` — both retired, satisfy nothing;
  the machine census is `ACCEPTANCE-PHRASE-REGISTRY.yaml`.
- Act arguments: every superseded digest is quoted only inside its
  historical record (CG-7d/CG-15b police this).
