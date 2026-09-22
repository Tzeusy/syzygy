# `docs/` — the implementation plane's working documents

> **Not authority.** Nothing here adopts, accepts, or approves anything, and
> nothing here may be cited as a rule. Authority lives in `.syzygy/**`
> (doctrine, decisions, policies, contracts) and `openspec/**`
> (specifications); current state lives in `PROJECT-STATUS.md`. Where a page
> here disagrees with one of those, **the owning record wins and this page is
> stale** — report the disagreement rather than resolving it here.

`.syzygy/**` says what must be true and `openspec/**` says what the software
must do. This directory holds the third thing: the **implementation plane's**
own working record — how the work was planned, what was reviewed, and what
evidence a run actually produced. It is written by and for the people and
agents doing the building.

## What is here

| Path | What it is | Reader, and the question it answers |
|---|---|---|
| `CAPABILITY-1-IMPLEMENTATION-PLAN.md` | The Capability 1 build plan | An implementer: "what is the next lawful implementation step, and under which act?" |
| `PWB-IMPLEMENTATION-PLAN.md` | The Polaris project-wide Butlers-model build plan | Same, for the PWB pipeline |
| `THREE-SURFACE-POC.md` | How to run the bounded POC | Anyone: "how do I start this thing and see it?" |
| `reviews/` | The review corpus — raw reviewer output and its dispositions | A reviewer or repairer: "what did an independent reader find, and what happened to each finding?" |
| `evidence/` | Machine-produced run records (mutation sweeps, browser and fresh-checkout runs), as JSON | Anyone checking a claim: "what did that run actually output?" |
| `plans/` | Dated design notes for a single bead, written before the work | An implementer picking up that bead: "what shape was already decided, and by whom?" |
| `superpowers/plans/`, `superpowers/specs/` | Spent plans and designs from an external-harness convention, kept as evidence | Someone auditing a past change: "what was the plan the work was actually done against?" |

Implementation *plans* live here. The **authorizing act** for any of that work
does not — it lives in `.syzygy/governance/decisions/`. A plan in this
directory is never permission; find the act first (`AGENTS.md`, "Where
authority lives").

## `reviews/` — the corpus, by campaign

Raw reviewer output is stored **verbatim and never edited** (CC-REV-6). Files
ending `-RAW.md` are that verbatim output; `-DISPOSITION.md` and `*-PACKET.md`
files are the synthesis over them. Correcting a RAW file is never the repair —
the repair is a new disposition that cites it.

| Campaign | Files | Recorded | What was under review | Last verdict of record, and where the findings landed |
|---|---|---|---|---|
| `R-S2` … `R-S7` | 4 | 2026-08-21 → 2026-08-22 | Capability 1 domain-slice risk floors | S7 ends `CONFIRM WITH EXCEPTIONS` (`R-S7-RISK-FLOOR-REVIEW.md:8`); its retained exceptions route through the named follow-up beads and the local guardrail note. |
| `R-RT-*` | 2 | 2026-08-23 | Capability 1 runtime vertical slice | The confirmation is `CONFIRMED` (`R-RT-CONFIRMATION-REVIEW.md:4`); the repaired bypass and residual note are dispositioned in the same pair. |
| `R-POC-*` | 8 | 2026-08-30 → 2026-08-31 | Three-Surface POC product cycles and owner walkthrough | The cycle closed, but the later owner walkthrough records `FAIL — BLOCKER` (`R-POC-OWNER-WALKTHROUGH-POLARIS.md:18`); that finding launched the project-wide Polaris work. |
| Project-wide Polaris specification and observation gate | 15 | 2026-08-31 | Read-boundary incident, observation exception, and project-wide candidate | The post-ceiling disposition is `CONFIRMED` (`R-POLARIS-PROJECT-WIDE-SPEC-REVIEW-DISPOSITION.md:181`); the owner act, not this review, owns sign-off. |
| `R-GENERAL-TRUSTED-*` | 24 | 2026-08-31 → 2026-09-01 | General trusted-bootstrap transaction | The final reader pass is `CONFIRM` (`R-GENERAL-TRUSTED-BOOTSTRAP-POST-ACT-READER-FINAL-CONFIRMATION-RAW.md:1`); findings landed in the two disposition files and performed transaction. |
| `R-PWB-STATE1-*` | 14 | 2026-09-02 | PWB state-(1) amendment | The post-act current-state pass is `EXACT VERDICT: CONFIRM` (`R-PWB-STATE1-ACT-CURRENT-STATE-RAW.md:123`); dispositions landed in the amendment package and act. |
| `R-PWB-EFFECT-*` | 3 | 2026-09-02 | PWB consent, secret-policy, and registry effect acts | The owner-packet review is `EXACT VERDICT: CONFIRM` (`R-PWB-EFFECT-ACTS-OWNER-PACKET-RAW.md:353`); its security finding was repaired before the three acts. |
| `R-PWB-TRUTH-*` | 11 | 2026-09-05 | PWB truth-and-readiness amendment and dependent effects | The final owner-packet review is `EXACT VERDICT: CONFIRM` (`R-PWB-TRUTH-POLICY-OWNER-PACKET-FINAL-RAW.md:19`); findings landed in the amendment and effect-act packages. |
| PWB live exact-head | 5 | 2026-09-05 → 2026-09-06 | Live implementation truth, parity, copy, and comprehension | The last raw lane remains `VERDICT: REVISE` (`R-PWB-LIVE-EXACT-HEAD-UX-RAW.md:445`); all fifteen findings route into the recovery campaign below. |
| PWB recovery reconciliation | 5 | 2026-09-06 | Two reconciliation generations and retained reviews | Gen 2 ends `CONFIRM WITH EXCEPTIONS` (`2026-09-06-pwb-recovery-reconciliation-gen2-packet.md:164`); its four Low/Info residues route to ordinary beads. |
| `R-PWB-P63-*` | 1 | 2026-09-07 | P-63 Polaris response trim | The verdict is `CONFIRMED WITH FINDINGS` (`R-PWB-P63-POLARIS-TRIM-RAW.md:16`); both should-fix items landed in the same branch and evidence record. |
| Orrery height finding | 1 | 2026-09-09 | Orrery bar-height encoding | The retained review says `CONFIRM FINDING` (`R-POLARIS-ORRERY-HEIGHT-FINDING-RAW.md:3`); the repair landed with the Orrery height fix. |
| Polaris editorial repair | 6 | 2026-09-10 | Selection fidelity and editorial passages | The code confirmation is `CONFIRMED` (`R-POLARIS-EDITORIAL-CODE-CONFIRMATION-RAW.md:1`); dispositions are summarized in `2026-09-09-polaris-editorial-repair.md`. |
| Polaris manifesto design and code | 8 | 2026-09-10 | Manifesto structure, navigation, design, and implementation | The final code pass is `CONFIRMED` (`R-POLARIS-MANIFESTO-CODE-FINAL-RAW.md:1`); earlier design and code findings are retained in the same campaign. |
| Polaris reading assets and navigation | 6 | 2026-09-10 | Reading-plan assets, guide navigation, and race repair | The repair confirmation is `PASS` (`R-POLARIS-READING-ASSETS-REPAIR-CONFIRMATION-2026-09-10-RAW.md:9`); RRA-1 is dispositioned there. |
| PWB declared-home repair | 3 | 2026-09-10 | Declared-home mutation and readiness repair | The final review is `CONFIRMED` (`R-PWB-DECLARED-HOME-FINAL-RAW.md:1`); the mutation-fragment finding landed in the repair. |
| PWB owner-walkthrough capture | 3 | 2026-09-10 | Live, semantic-readiness, and final owner-review captures | The final capture says `READY FOR OWNER REVIEW` (`R-PWB-WALKTHROUGH-FINAL-CAPTURE-RAW.md:1`); owner judgment remains a separate state. |
| Polaris visible diagrams | 5 | 2026-09-10 | Diagram visibility, fidelity, and final diff | The final diff confirmation is `PASS` (`R-POLARIS-VISIBLE-DIAGRAMS-FINAL-DIFF-2026-09-10-RAW.md:3`); prior visibility and fidelity findings landed in the same change. |
| Polaris generation kit | 2 | 2026-09-12 | Candidate reusable authoring guidance | The confirmation is `PASS` (`R-POLARIS-GENERATION-KIT-CONFIRMATION-2026-09-12-RAW.md:3`); it explicitly limits the verdict to the documentation handoff. |
| Polaris generator product and scope | 3 | 2026-09-12 | Generator product readiness, fresh product review, and scope | The final scope confirmation is `PASS` (`R-POLARIS-GENERATOR-SCOPE-CONFIRMATION-2026-09-12-RAW.md:3`); remaining authority work is in the adjacent campaign. |
| Polaris generator authority and recorder | 7 | 2026-09-12 | Authority staging, offer, recorder, and final readiness | The last pairing confirmation is `CONFIRMED` for AR-3 (`R-POLARIS-GENERATOR-AUTHORITY-PAIRING-CONFIRMATION-2026-09-12-RAW.md:3`); AR-1 remains the recorded phase/refusal disposition. |
| Polaris understanding amendment | 3 | 2026-09-13 | Product clarification and formal amendment synthesis | The formal synthesis is `ready for formal owner review` (`R-POLARIS-UNDERSTANDING-FORMAL-SPEC-2026-09-13-RAW.md:3`); adoption remains owned by its act. |
| PWB M1 lane A | 1 | 2026-09-13 | Polaris page-size lane-A evidence | The review ends `CONFIRMED WITH FINDINGS` (`R-PWB-M1-POLARIS-LANE-A-RAW.md:477`); its should-fix items landed in the lane-A branch. |
| P-68 scoped-attributes package | 4 | 2026-09-14 | Scoped epistemic-attributes semantic delta | Review 4 ends `CONFIRM WITH EXCEPTIONS` (`R-PWB-SCOPED-ATTRIBUTES-DELTA-4-RAW.md:489`); findings landed in the candidate package, which binds nothing without its act. |
| Polaris M2 funnel | 6 | 2026-09-14 | P-69 evidence-currency funnel | Review 6 ends `CONFIRM WITH EXCEPTIONS` (`R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-6-RAW.md:327`); findings landed in the M2 packet before owner ruling. |
| Polaris M3 funnel | 7 | 2026-09-14 → 2026-09-15 | P-70 honest-encoding funnel | Review 7 ends `CONFIRM WITH EXCEPTIONS` (`R-POLARIS-M3-HONEST-ENCODING-FUNNEL-7-RAW.md:336`); findings landed in the M3 packet before owner ruling. |
| Polaris M4 funnel | 7 | 2026-09-14 → 2026-09-15 | P-71 owner-loop funnel | Review 7 ends `CONFIRM WITH EXCEPTIONS` (`R-POLARIS-M4-OWNER-LOOP-FUNNEL-7-RAW.md:310`); findings landed in the M4 packet before owner ruling. |
| Polaris M5 funnel | 4 | 2026-09-14 → 2026-09-15 | P-72 agent-briefing funnel | Review 4 ends `CONFIRM WITH EXCEPTIONS` (`R-POLARIS-M5-AGENT-BRIEFING-FUNNEL-4-RAW.md:363`); findings landed in the M5 packet before owner ruling. |
| Polaris M6 funnel | 2 | 2026-09-15 | P-73 generator-honesty funnel | Review 2 ends `CONFIRM WITH EXCEPTIONS` (`R-POLARIS-M6-GENERATOR-HONESTY-FUNNEL-2-RAW.md:491`); findings landed in the M6 packet before owner ruling. |
| Polaris M7 funnel | 2 | 2026-09-15 | P-76 generation-loop funnel | Review 2 ends `CONFIRM WITH EXCEPTIONS` (`R-POLARIS-M7-GENERATION-LOOP-FUNNEL-2-RAW.md:550`); findings landed in the M7 packet before owner ruling. |
| Polaris M8 funnel | 2 | 2026-09-15 | P-74 portability funnel | Review 2 ends `CONFIRM WITH EXCEPTIONS` (`R-POLARIS-M8-PORTABILITY-FUNNEL-2-RAW.md:526`); findings landed in the M8 packet before owner ruling. |
| Polaris M9 funnel | 2 | 2026-09-15 | P-75 one-identity funnel | Review 2 ends `CONFIRM WITH EXCEPTIONS` (`R-POLARIS-M9-ONE-IDENTITY-FUNNEL-2-RAW.md:492`); findings landed in the M9 packet before owner ruling. |
| Polaris M10 funnel | 2 | 2026-09-15 | P-77 machine-contract funnel | Review 2 ends `CONFIRM WITH EXCEPTIONS` (`R-POLARIS-M10-MACHINE-CONTRACT-FUNNEL-2-RAW.md:359`); findings landed in the M10 packet before owner ruling. |
| Polaris M11 funnel | 2 | 2026-09-15 | P-78 operability funnel | Review 2 ends `CONFIRM WITH EXCEPTIONS` (`R-POLARIS-M11-OPERABILITY-FUNNEL-2-RAW.md:520`); findings landed in the M11 packet before owner ruling. |
| Polaris M12 funnel | 2 | 2026-09-15 | P-79 retained-evaluations funnel | Review 2 ends `CONFIRM WITH EXCEPTIONS` (`R-POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL-2-RAW.md:380`); findings landed in the M12 packet before owner ruling. |
| Polaris M13 funnel | 2 | 2026-09-15 → 2026-09-16 | P-80 navigation-scale funnel | Review 2 ends `CONFIRMED` (`R-POLARIS-M13-NAVIGATION-SCALE-FUNNEL-2-RAW.md:220`); all review-1 exceptions are dispositioned there. |
| Polaris M14 funnel | 1 | 2026-09-17 | P-81 provenance-depth funnel | Review 1 ends `CONFIRM WITH EXCEPTIONS` (`R-POLARIS-M14-PROVENANCE-DEPTH-FUNNEL-1-RAW.md:189`); findings landed in the M14 packet before owner ruling. |
| Polaris M15 funnel | 1 | 2026-09-17 | P-82 pipeline-truthfulness funnel | Review 1 records `CONFIRM WITH EXCEPTIONS` (`R-POLARIS-M15-PIPELINE-TRUTHFULNESS-FUNNEL-1-RAW.md:3`); findings landed in the M15 packet before owner ruling. |
| Polaris M16 funnel | 1 | 2026-09-17 | P-83 renderer and visual-system funnel | Review 1 records `CONFIRM WITH EXCEPTIONS` (`R-POLARIS-M16-RENDERER-VISUAL-SYSTEM-FUNNEL-1-RAW.md:1`); findings landed in the M16 packet before owner ruling. |
| P-79 retention-posture gate | 2 | 2026-09-22 | Retained-evaluations retention decision packet | The confirmation remains `CONFIRM WITH EXCEPTIONS` (`R-POLARIS-RETENTION-POSTURE-PACKET-CONFIRMATION-RAW.md:4`); the candidate packet records its repaired and residual findings. |
| P-81 exact-source gate | 2 | 2026-09-22 | Exact-source render-mode semantic delta | The confirmation is `CONFIRM` (`R-PWB-EXACT-SOURCE-RENDER-MODE-DELTA-CONFIRMATION-RAW.md:4`); repairs landed in the candidate package, which awaits its act. |
| P-72 machine-view gate | 6 | 2026-09-22 → 2026-09-23 | Derived read-only machine-view semantic delta | The sixth review, over the round-5 repairs, is `CONFIRM WITH EXCEPTIONS` (`R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-5-RAW.md:4`) with all twelve brief criteria satisfied and no new finding; its one exception is the `RFC6-21` reading the owner already chose, carried forward from rounds 1–5. Whether that exception still blocks offering the act phrase is an owner question.
| P-71 opening-band gate | 6 | 2026-09-22 → 2026-09-23 | Opening-band scenario delta | The fifth sequential review, over the round-4 repairs, is `REVISE` (`R-PWB-OPENING-BAND-SCENARIO-DELTA-CONFIRMATION-4-RAW.md:4`); a parallel independent round over the round-2 bytes is retained beside it; findings remain dispositioned in the candidate package, which awaits a round 6. |
| P-69/P-72 registry gate | 4 | 2026-09-22 → 2026-09-23 | Currency-bound and briefing-ceiling registry amendment | The third confirmation is `CONFIRM` (`R-PWB-REGISTRY-CURRENCY-BRIEFING-DELTA-CONFIRMATION-3-RAW.md:5`), over the bytes that repair the second confirmation's F1 and F2; the candidate package awaits its act, with question 6 held for the owner. |
| P-69 Q7a missing-currency gate | 2 | 2026-09-23 | Missing-currency-bound disclosure scenario delta | The confirmation is `CONFIRM` (`R-PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-DELTA-CONFIRMATION-RAW.md:1`); repairs landed in the candidate package, which awaits its act and applies after lane B. |
| N8 generality measurement | 4 | 2026-09-23 | Slice 1: synthetic second-project corpora and per-class coverage matrix (PR #63); slice 2: `repairFor` narrowed to genuine shape mismatches (PR #73); slice 3: `SourcePopulation` admitted-input port at the generator front door (PR #86) | Slice 1 `CONFIRM` (`R-PWB-N8-SLICE1-REVIEW-RAW.md:19`); slice 2 `REVISE` (`R-PWB-N8-SLICE2-REVIEW-RAW.md:3`), repaired, then `CONFIRM` (`R-PWB-N8-SLICE2-CONFIRMATION-RAW.md:3`). Slice 3 `CONFIRM` (`R-PWB-N8-SLICE3-REVIEW-RAW.md:3`). |
| N4 page honesty | 2 | 2026-09-23 | Slices 3-4: evaluation-identity footers on Trajectory and Orrery, `--focus`/`--measure-reading` tokens (PR #67) | `REVISE` (`R-PWB-N4-SLICES3-4-REVIEW-RAW.md:1`), repaired; confirmation `CONFIRM` (`R-PWB-N4-SLICES3-4-CONFIRMATION-RAW.md:6`). |
| N11 drift sweep | 3 | 2026-09-23 | Slices 1 and 3: `scripts/check_evidence_currency.py` sha256 drift sweep and the typed pipeline failure code (PR #68); slice 2: scheduled generation-core mutation gate and rule-6 evidence run (PR #82) | Slices 1 and 3 `REVISE` (`R-PWB-N11-SLICES1-3-REVIEW-RAW.md:1`), repaired; confirmation `CONFIRM` (`R-PWB-N11-SLICES1-3-CONFIRMATION-RAW.md:3`). Slice 2 `CONFIRM` (`R-PWB-N11-SLICE2-REVIEW-RAW.md:3`). |

The 48 rows partition the tracked directory at HEAD: 218 files, 218 assigned,
no remainder [Observed — re-derived for HEAD dated 2026-09-23 by
`scripts/check_docs_review_campaign_partition.py`; the helper evaluates every
anchored predicate independently, reports overlaps and unmatched paths, and
derives dates from `git log --diff-filter=A`]. These are navigation figures,
not measurement, and they go stale the moment a review lands — re-run the
helper rather than trusting the row.

Three things the table cannot show. The PWB rows are a dependency chain, not
four independent campaigns: the state-(1) amendment made a behavioral change,
the effect acts then granted the authority that change could satisfy, and the
truth-and-readiness amendment later replaced the state-(1) artifacts outright
while amending the two instruments the effect acts had put in force — the act
records say so, and only they say it. A `CONFIRM` verdict is a reviewer's
finding about frozen bytes, never an adoption: what binds is always the act in
`.syzygy/governance/decisions/`. And a campaign with nothing open in its own
files may still have left something open elsewhere — the S-slice row's
`syzygy-e3e`, the POC row's walkthrough blocker, the recovery row's §5.3.

## `plans/` and `superpowers/` — two homes, one role

Both hold plan-and-design notes; they are split by which harness wrote them,
not by what they are. Prefer `plans/` for anything new.

`superpowers/` is **path-pinned and must not be moved or renamed.** The
general trusted-bootstrap authorization's impact ledger classifies every path
under that prefix as spent historical evidence, and
`scripts/build_general_trusted_bootstrap_impact_ledger.py` hard-codes the
prefix string to do it. Relocating a file out of that directory would silently
re-classify it on the next regeneration.

**One of the four is not spent.** The ledger's classification is about where a
file sits, not about whether the work it plans is finished, and those two
answers have come apart. Read the table before treating any of these as
history — and read the `bd` issue, never the "REQUIRED SUB-SKILL" line at a
file's head, which addressed the worker of the day.

| File | Issue | State |
|---|---|---|
| `superpowers/plans/2026-08-24-cap1-runtime-hardening-followups.md` | epic `syzygy-u2a` | **Live.** The epic names it as its *approved implementation guidance* at commit `d11c07e`, and shapes its six implementation children on that file's Tasks 1–6. The epic is open (P1) and its human gate `syzygy-u2a.1` is blocked |
| `superpowers/specs/2026-08-23-cap1-runtime-hardening-followups-design.md` | `syzygy-ydr`, `syzygy-e84`, `syzygy-h84` | Spent. The design the plan above was written from |
| `superpowers/plans/2026-08-27-syzygy-vky-validator-hardening.md` | `syzygy-vky` (closed) | Spent |
| `plans/2026-08-26-syzygy-vky-validator-hardening-design.md` | `syzygy-vky` (closed) | Spent. The design for the same work as the row above — two files, one bead, split only by which harness wrote them. Neither is cited by anything |

[Observed — swept 2026-09-06: four files across the three directories; each
searched for `syzygy-*` identifiers in its own text, and each filename searched
across every tracked `.md` and `.py`. Two are cited, both by the general
trusted-bootstrap impact ledger; two are cited by nothing.]

## `evidence/` — run records

Each file is one run's machine output at a named commit, kept because a claim
elsewhere cites it. A mutation-run record is valid **only for the commit it
names** (`AGENTS.md` verification rule 7). Reading the file's own contents is
the check; the filename is not the evidence.

**This directory has no index of its own, and does not need one:
`PWB-IMPLEMENTATION-PLAN.md` is the index.** Every file here is cited, and 25
of the 28 are cited by that plan, at the task whose evidence they are — so the
route in is the plan's task, never a listing of this directory. The three the
plan does not name are the three a *reviewer* produced rather than a task
(`…-gen2-reviewer.json`, `pwb-recon-gen1-reviewer-…`,
`pwb-recon-gen2-reviewer-…`); the reconciliation packets in `reviews/` cite
those, which is the correct home for a reviewer's own run. [Observed — swept
2026-09-06: 28 files, each basename and stem searched across every tracked
`.md`, `.py`, `.ts`, `.json`, `.yml`, `.txt` and `.sh` outside this directory;
28 cited, 0 uncited, 25 cited by the plan, remainder enumerated above.]

A JSON here does not say whether the work it evidences is finished — a run
that passed at a commit says nothing about the finding a later review raised
against the same seam. `bd show` and `PROJECT-STATUS.md` own that.

## The maintenance contract

This directory is governed by the adopted craft policy
`.syzygy/governance/policies/craft-and-care/review-and-documentation.md`. The
clauses that bind what you write here — cited, not restated:

- **CC-REV-2** — a change that moves a responsibility updates its
  documentation *in the same change*; it does not merge with the
  contradiction open.
- **CC-REV-3** — documentation **cites** authoritative artifacts, it never
  restates them normatively. A restated rule drifts and becomes a shadow
  authority. If you find the same question answered in two homes, surface the
  contradiction; do not silently pick a winner.
- **CC-REV-5** — substantive claims carry `[Observed]` (with a resolvable
  source), `[Inferred]`, or `[Unknown]`. Missing evidence renders Unknown,
  never Inferred.
- **CC-REV-6** — raw reviewer output is stored unchanged before synthesis, and
  every revise-severity finding is fixed or explicitly overruled with recorded
  rationale. Nothing is dropped.
- **CC-REV-7** — identifiers are stable: amend in place, retire rather than
  renumber.

In practice, for this directory: a page that no longer has a nameable reader
and a question it answers should be merged or removed, not left to rot; a page
that has gone stale is marked stale **with evidence at the stale sentence**,
never left silently standing behind a general "this page may be stale" banner.

## What does not belong here

- Implementation code (it belongs in `apps/**`, `packages/**`, `scripts/`).
- Anything normative — rules, acceptance, adoption, approval. Those are owner
  acts under `.syzygy/governance/` (VIS-4).
- A second copy of state `PROJECT-STATUS.md` already owns.
- Per-tool scratch conventions from an external harness. If a tool wants a
  directory of its own, it gets one outside `docs/`.
