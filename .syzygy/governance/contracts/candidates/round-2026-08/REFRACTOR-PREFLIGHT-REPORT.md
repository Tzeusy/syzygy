# Refactor preflight report — human-clarity refactor round

**Round:** human-clarity refactor, public-clone normalization, final
pre-specification gate (owner round prompt, processed 2026-08-05).
**Lead:** this session (fresh Claude Fable session, per the round prompt).
**Status of this file:** process record for this round. Not authority; it
describes state, decides nothing.

## 1. Repository state at round start

| Fact | Value |
|---|---|
| Branch | `main`, in sync with `origin/main` (git@github.com:Tzeusy/syzygy.git) |
| HEAD | `9e6f2f7db55c4ce672daf9636f1cf2ab664879c8` |
| Working tree | clean except one untracked file: the round prompt itself (`syzygy_fable_human_clarity_refactor_round_prompt.md`) |
| Tracked files | 36 |
| Git tags | `doctrine-adopted-2026-07-30` (only) |
| Ignored (relevant) | `.dolt/`, `*.db`, `.beads-credential-key`, `.syzygy/cache/`, `.syzygy/local/`, `_bootstrap/` (versioned `.gitignore`; `_bootstrap/` exclusion made durable at `9e6f2f7`, FD-021/FD-037) |
| Beads | database empty (0 issues) before this round; one process-housekeeping issue created for this round. No product work exists or is created |
| Parallel-lead check | checkpoint tail + `_bootstrap/knowledge-refactor/reviews/` mtimes all 2026-08-04 ≤ 23:33; session B recorded its own stand-down. No live parallel lead. This session is the consolidating lead the checkpoint hands off to |

## 2. Current governance state

- **Doctrine — ADOPTED.** `.syzygy/governance/doctrine/` (6 files),
  owner act `ADOPT DOCTRINE` 2026-07-30, commit `9bdfe98`, tag
  `doctrine-adopted-2026-07-30`. One amendment in force: **D1** (map
  historical scope, commit `84d4a88`), logged in the doctrine README.
  Amendment **D3** (bounded missions) exists only as a draft; act 5 pending.
- **Owner decisions.** Tracked: `decisions/PENDING-OWNER-DECISIONS.md`
  (P-1..P-16, as-of `adddc34`, now stale in known ways),
  `decisions/SURFACE-DECISION-RECORD.md` (SDR-1..33). Founder decision log
  (FD-*) and most owning records are founder-local under `_bootstrap/`.
- **Craft-and-care — installed and owner-approved (D2)** at
  `.syzygy/governance/policies/craft-and-care/` with three known defects
  (P-7 false bootstrap banners on all 10 files; P-8 unsatisfiable
  retired-phrase binding at `INSTALL-RECORD.md:20`; pending CC-TEST-2
  confirmation act 2).
- **Contract corpus — candidate, founder-local.** Rev10 compacted package:
  32 modules (RFC 0001–0011), 322 clauses, manifest digest
  `08793ddf70f3…`, CONFIRM-bound by the rev10 confirming review, offered
  but not accepted (P-1). Lives only under
  `_bootstrap/rfc-phase/final-prespec/` — invisible to clones before this
  round.
- **Topology — candidate, founder-local.** 10-file bundle, digest
  `0d34d1b5…` (P-3), also `_bootstrap/`-only before this round.
- **Overview.** `.syzygy/intent/OVERVIEW.md` (1,290 words) committed at
  `fcb05c0`; act-4 digest `42de2eb1…` offered, not adopted; carries a
  hand-maintained stale "where this stands" gate section (four-review
  corroborated defect; P-4/P-13).
- **OpenSpec.** No `openspec/` directory exists. Correct for the phase.
- **Implementation.** None (correct; pre-implementation boundary holds).
- **Public GitHub-visible state.** A cloner sees: one-line README, stale
  `AGENTS.md`, doctrine, decisions (2 files), craft policies with false
  banners, two heart-and-soul skills, beads hooks. **A clone cannot see:**
  any RFC module, the manifest, the acceptance record, topology, the
  verification scripts, the decision log, the front-door drafts, term
  registry, hygiene policy, fixtures — all founder-local (P-9). Prior
  measurement: clone answers 2 of 9 self-containment questions
  (`PUBLIC-CLONE-VERIFICATION-REPORT.md`, 2026-08-04).

## 3. Stale-phrase sweep (tracked files, Python `re`, 2026-08-05)

| Phrase | Hits | Where |
|---|---|---|
| `seed, not adopted doctrine` | 1 | `AGENTS.md:3` |
| `about/` | 10 | `AGENTS.md` ×5, heart-and-soul SKILL.md ×2 (both copies, as "no about/ tree" guidance — acceptable), craft README ×2 (historical note) |
| `prompts/00` (bootstrap routing) | 1 | `AGENTS.md:23` |
| `ACCEPT FOUNDATIONAL RFCS` (retired) | 3 | `INSTALL-RECORD.md:20` (P-8), `AGENTS.md:31`, `AGENTS.md:159` |
| `bootstrap-phase record` (false banner) | 11 | all 10 canonical craft files (P-7) + INSTALL-RECORD provenance line (historically true there) + a truthful mention in PENDING-OWNER-DECISIONS |
| `founder-local` | 3 | `.gitignore`, PENDING-OWNER-DECISIONS (truthful disclosures) |

Also inside the candidate digest sets (from the §20 batteries, re-confirmed
this round): retired phrase at `rfcs/RFC-0003/governance-homes-and-owner-acts.md:87`
(act-1 set, P-6) **and** `topology/README.md:45` (act-3 bundle — the second
leg, from the respawn battery delta index #6).

## 4. Inherited defect queue this round must dispose

Sources: `20-DISPOSITIONS.md` (six primary reviews, all EXCEPTIONS),
`20-RESPAWN-DELTA-INDEX.md` (18 additional findings), rev10 confirming
review residuals (R1 stale RFC-0007 self-count), pass findings F-4/F-6/F-10/
F-11, P-1..P-16 register. The owner's round prompt §7 supplies directed
dispositions for all sixteen P-items; §4/§19 defines the review battery that
must re-validate the result.

## 5. Homes decided for this round (structural, disclosed)

RFC3-15 (candidate) closes `.syzygy/governance/` to six category names —
`doctrine/ contracts/ policies/ decisions/ records/` + reserved
`declarations/`. The round prompt's suggested `governance/reviews/` home
would violate that validator, so this round uses:

| Content | Home |
|---|---|
| Candidate contract package (32 modules, manifest, acceptance record, fixtures, portable scripts, non-normative history/ + matrix-rows/ companions, package reviews) | `.syzygy/governance/contracts/candidates/` |
| This round's process records and review raws | `.syzygy/governance/contracts/candidates/round-2026-08/` |
| Candidate topology bundle | `.syzygy/map/topology-candidates/` |
| Candidate policies (knowledge hygiene, term registry) | `.syzygy/governance/contracts/candidates/policy-candidates/` |
| Owner-decision artifacts (regenerated pending queue, license packet, FD-037 warrant extractions, decision register) | `.syzygy/governance/decisions/` |
| Public front door | repository root |
| Documentation-only CI | `.github/workflows/` |

Candidate homes carry explicit non-authority banners; nothing is installed
into an accepted home (`contracts/rfcs/`, `map/topology/`) and nothing is
labeled accepted. Placing *candidates* beneath `contracts/` is a disclosed
structural interpretation (the closed validator names categories; lifecycle
labeling distinguishes accepted from candidate content); it is surfaced for
owner ratification in the final acceptance record rather than silently
assumed.

## 6. Round sequencing (from the owner's §7 dispositions)

1. FD-037 warrant extraction + repoints (plan already owner-ruled).
2. P-9: candidate package + topology → tracked candidate homes.
3. P-6 both legs, P-7 banners, P-8 binding → regenerate digests/manifest.
4. Front door (§8), overview refactor (§9), term registry (§10), corpus
   metadata/indexes (§11), craft hygiene policy (§12), semantic-delta
   workflow (§13), Mission review (§14), Context Compiler fixtures (§15),
   knowledge-health brief (§16), portable validation + CI (§17).
5. Review battery (§4: nine verticals) + P-10 missing reviews; raw verdicts
   stored unchanged; dispositions.
6. Final exact-manifest review; owner acceptance package; regenerated
   pending-decision register; stop at owner gates (§22).
