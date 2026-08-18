# Project status

> **As-of: 2026-08-18** (the commit introducing this revision —
> `git log -1 --format=%h PROJECT-STATUS.md`). A hand-authored pointer page:
> it **must not be the sole source** for any fact it states. Each row cites
> the record that owns it, and where they disagree the record wins and this
> page is stale.
>
> This page holds **current state only**. The launch-gate review chronology
> is at `.syzygy/governance/decisions/launch-gate/HISTORY.md`; process
> lessons are at `.syzygy/governance/decisions/PROCESS-LESSONS.md`; each
> pass's reports live in the `round-*` trees. None is default reading.

## Lifecycle stage

**Final pre-specification.** No application code exists, and none may be
added until behavioral specifications are authored and approved — which
cannot begin until the owner accepts the foundational contracts and
separately authorizes launch.

## The launch path, in one table

The launch target is **Capability 1 — Project registration and honest shape
visibility**. Its contract prerequisite is **Waves A + B only**.

| Step | State | Owning record |
|---|---|---|
| Wave A (RFC 0001–0006, 19 modules) | **ACCEPTED — act performed 2026-08-17.** The owner wrote the exact phrase over the RD-31b-confirmed argument `8972d963…`; the 19 modules are installed at `contracts/rfcs/` (shape (M), 19/19 digest-verified from the governed home). Owner-adopted bootstrap, uncorrelated — never "verified". | `decisions/ACCEPTANCE-ACT-RECORD.md`; tag `wave-a-accepted-2026-08-17` |
| Wave B (RFC 0007–0009 + the three surfaces, 11 modules) | **ACCEPTED — act performed 2026-08-17, after Wave A.** The owner wrote the exact phrase over the RD-32c-confirmed argument `193e3c1e…`; the 11 modules are installed at `contracts/rfcs/` (shape (M), 11/11 digest-verified). Owner-adopted bootstrap, uncorrelated — never "verified". | `decisions/ACCEPTANCE-ACT-RECORD.md`; tag `wave-b-accepted-2026-08-17` |
| Waves C1/C2/D1/D2 | **Deferred** — candidate, not accepted, not used by the launch target, not offered. Not retired. | `contracts/candidates/DEFERRED-WAVE-POSTURE.md` |
| Owner rulings, 2026-08-16 | **P-31, P-33, P-35, P-36, P-37, P-38, P-39, P-40 ruled** in one adversarially-reviewed sitting, plus P-34 below. Zero contract bytes moved; both wave confirmations survive. | `decisions/PENDING-OWNER-DECISIONS.md` §"Resolved on 2026-08-16"; each row names its owning record |
| Launch-gate policy | **Owner-approved process policy at v2.4** — P-34 ruled arm (a), 2026-08-16, **with two disclosed BLOCKING residuals** (RD-67 f1, RD-68 f1 — false-`READY` paths reachable only by an adversarial record author), **F5 not promoted**. Ten `REVISE` verdicts across v2.0–v2.4 stand as recorded; this is approval-with-residuals, not a clean review verdict. A bounded v2.5 is an owner option, not a gate. | `decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (the recorded approval); instrument `launch-gate-pre-specifications.md`; `round-2026-08h/reviews/DISPOSITION-REGISTER.md` |
| P-41 + P-42, offered jointly | **PERFORMED — acts 6 and 7, 2026-08-17, one sitting** (the joint-sitting requirement satisfied). CC-SPEC-1…11 and CC-IMPACT-1…7 are **in force as owner-confirmed craft** at their reviewed digests; the files bind at their committed homes, uncopied and unedited. Review chain: RD-51 (`REVISE`) → repair → RD-69 (`REVISE`, one launch blocker) → the one blocker-only repair → RD-70 (`CONFIRM WITH EXCEPTIONS`). Nine non-blocking findings traveled into force disclosed. | `decisions/ACCEPTANCE-ACT-RECORD.md`; `.syzygy/governance/policies/craft-and-care/INSTALL-RECORD.md`; tag `craft-acts-6-7-confirmed-2026-08-17` |
| Formal launch administration | **Administration 1 performed 2026-08-18 — verdict `NOT READY`** (10 plain Not-met, 2 scoped, 5 Unknown, 0 reopened). Out-of-family (OpenAI GPT-5.6 Pro), fresh context with disclosed limitations, against commit `71e5986` at approved v2.4; the record validated and its verdict computed by the committed scripts. The strongest findings are stale current-state claims on the default path (since repaired), the contract-index drift (since regenerated), Wave A rejection collapsing the launch path (B4), clone-unreachable D1 rationale (C7), and unbounded governance effort (F6). The 2026-08-09 v1.3 **pilot** (`NOT READY`) remains steering evidence only. | `decisions/launch-gate/ADMINISTRATION-2026-08-18-CAPABILITY-1.json` (the record); `decisions/launch-gate/TREND-LOG.md` |
| OpenSpec (`openspec/`) | **No specification content.** A tool-created scaffold (config plus empty trees) exists and is not specification work; authoring is forbidden until the owner's launch decision. | `contracts/candidates/HOW-TO-AUTHOR-A-SYZYGY-SPEC.md` |
| Implementation | **Does not exist.** Blocked on accepted specifications. | — |

**Four owner acts have been performed, all 2026-08-17:** Wave A, Wave B,
and craft acts 6 + 7.
`.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` exists since the
first act and owns every performed act; nine offered acts remain
unperformed.

## Gates already closed

| Gate | State | Owning record |
|---|---|---|
| Doctrine adoption | ✅ Adopted 2026-07-30, amendment D1 in force | tag `doctrine-adopted-2026-07-30`; `.syzygy/governance/doctrine/README.md` |
| Craft-and-care approval | ✅ Approved (owner decision D2) | `.syzygy/governance/policies/craft-and-care/INSTALL-RECORD.md` |
| Surface decisions | ✅ Recorded SDR-1…37 | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md` |
| The 2026-08-16 rulings | ✅ See the launch-path table above | `decisions/PENDING-OWNER-DECISIONS.md` §"Resolved on 2026-08-16" |

## Gates still open, beyond the launch path

| Gate | State | Owning record |
|---|---|---|
| Craft amendment CC-TEST-2 | Awaiting confirmation at the current digest | `INSTALL-RECORD.md` **2026-08-06** correction block |
| Topology bundle | Candidate — no act performed | `.syzygy/map/topology-candidates/BUNDLE-MANIFEST.md` |
| Project overview | Draft — awaiting adoption | `.syzygy/intent/OVERVIEW.md` |
| Doctrine amendment D3 (bounded missions) | Proposed — adopt, amend, or decline | `contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (rev1) |
| Knowledge-hygiene craft policy | Candidate — own craft act (P-12) | `policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` |
| Decision-record convention (P-43) | Open — not launch-gating; earliest gate is a deferral-bearing administration | `decisions/PENDING-OWNER-DECISIONS.md` row P-43 |
| CC-REV-2 lagging-spec exception (P-44) | Offered, two arms, declining is one of them — not launch-gating | `policy-candidates/CC-REV-2-LAGGING-SPECIFICATION-AMENDMENT-OFFER.md` |
| License | Undecided — owner/legal | `.syzygy/governance/decisions/LICENSE-DECISION-PACKET.md` |

## Next lawful step

The remaining launch path, in order — each step's owning record governs:

1. ~~Owner performs the **Wave A act**, then the **Wave B act**~~ —
   **both done 2026-08-17**, A then B
   (`decisions/ACCEPTANCE-ACT-RECORD.md`).
2. ~~**P-41 + P-42**: perform craft acts 6 and 7 in one sitting~~ —
   **done 2026-08-17**, same day as the wave acts, one sitting
   (`decisions/ACCEPTANCE-ACT-RECORD.md`).
3. ~~**Formal Capability 1 administration** under approved v2.4~~ —
   **Administration 1 run 2026-08-18, verdict `NOT READY`**
   (`decisions/launch-gate/ADMINISTRATION-2026-08-18-CAPABILITY-1.json`).
   Repair of its repairable findings, then a second administration at a
   descendant commit declaring this record as prior, is the gate's own
   path to `READY`; several findings (A6, C7, F6, B5) want owner input,
   not session work.
4. The owner's separate **launch decision** — lawfully the owner's to make
   with the `NOT READY` verdict in hand; the gate is the evidence bar this
   pass's charter chose, not a lock on the owner. Specification authoring
   only after the decision; implementation only after specifications are
   accepted.

## How to verify this page

```sh
python3 scripts/check_governance.py
python3 scripts/check_governance.py --selftest
python3 scripts/launch_gate_results.py --selftest            # historical Markdown records
python3 scripts/validate_launch_administration.py --selftest # the structured record path
python3 scripts/render_launch_administration.py --selftest
CS=.syzygy/governance/contracts/candidates/scripts
python3 $CS/verify_final_prespec.py
python3 $CS/build_contract_index.py --check
python3 $CS/build_dependency_index.py --check
python3 $CS/build_budget_report.py --check
python3 $CS/build_active_manifest.py --check
python3 $CS/build_task_router.py --check
python3 $CS/build_task_router.py --selftest
python3 $CS/build_capability_1_views.py --check      # capability 1: charter -> views
python3 $CS/build_capability_1_views.py --selftest
DR=.syzygy/governance/contracts/candidates/round-2026-08f/fixtures/DRY-RUN-ADMINISTRATION.json
python3 scripts/validate_launch_administration.py $DR
python3 scripts/render_launch_administration.py $DR --check
git tag --list 'doctrine-*'
```

The sixteen checks above are the same sixteen the hosted workflow runs
(`.github/workflows/governance-docs.yml`), so "hosted CI is green" and "the
battery is clean" are one claim rather than two a reader conflates. The
`git tag` line is orientation, not a check — it prints and cannot fail.
**CG-26** parses both lists and fails on any divergence, including a
miscounted number in the sentence above.

**Read the output, not the exit code** — a PASS over zero examined items
verified nothing. Every check prints its own denominator; the WARNs are
declared-by-design. `--selftest` covers **the checks that have a fixture**,
not every check — CG-24 prints which, and that figure is the one to quote.

**Run it in a clone, not only here** — one working tree and its clone have
disagreed before, invisibly from the machine holding the git-excluded
directory. A clone report is valid only for the commit it names; the most
recent is
[`round-2026-08g/FINAL-PUBLIC-CLONE-REPORT.md`](.syzygy/governance/contracts/candidates/round-2026-08g/FINAL-PUBLIC-CLONE-REPORT.md).

**No result figures are quoted on this page.** Run the commands.
