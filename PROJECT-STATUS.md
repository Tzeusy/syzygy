# Project status

> **As-of: 2026-08-11** (the commit introducing this revision —
> `git log -1 --format=%h PROJECT-STATUS.md`). A hand-authored pointer page:
> it **must not be the sole source** for any fact it states. Each row cites
> the record that owns it, and where they disagree the record wins and this
> page is stale.
>
> This page holds **current state only**. The launch-gate review chronology
> that used to live here is at
> `.syzygy/governance/decisions/launch-gate/HISTORY.md`; process lessons are
> at `.syzygy/governance/decisions/PROCESS-LESSONS.md`. Neither is default
> reading.

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
| Wave A (RFC 0001–0006, 19 modules) | **Confirmed** — `VERDICT: CONFIRM` on the current argument `8972d963…` (RD-31b). **Offer withheld solely by P-33.** | acceptance record §1 + §7 item 11; `wave-manifests/WAVE-A-MANIFEST.txt` |
| Wave B (RFC 0007–0009 + the three surfaces, 11 modules) | **Confirmed** — `VERDICT: CONFIRM` on the current argument `193e3c1e…` (RD-32c). Nothing withholds it; it **follows Wave A**. | acceptance record §1; `wave-manifests/WAVE-B-MANIFEST.txt` |
| Waves C1/C2/D1/D2 | **Deferred** — candidate, not accepted, not used by the launch target, not offered. Not retired. | `contracts/candidates/DEFERRED-WAVE-POSTURE.md` |
| Launch-gate policy | **Candidate v2.0** — structured-record migration. Owner approval is **P-34**, not granted. Two fresh-context reviews are required before the offer and **have not been obtained**. | `launch-gate-pre-specifications.md`; `round-2026-08f/LAUNCH-GATE-v2.0-SEMANTIC-DELTA.md` |
| Formal launch administration | **Not performed.** The only administration on record is the 2026-08-09 **pilot** (v1.3), which returned `GATE VERDICT: NOT READY`. | `round-2026-08d/reviews/LAUNCH-GATE-ADMINISTRATION-2026-08-09-RAW.md` |
| OpenSpec (`openspec/`) | **Does not exist.** Authoring is forbidden until the owner's launch decision. | — |
| Implementation | **Does not exist.** Blocked on accepted specifications. | — |

**No owner acceptance act has been performed.**
`.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` does not exist,
which is the correct state — the first act creates it.

## Gates already closed

| Gate | State | Owning record |
|---|---|---|
| Doctrine adoption | ✅ Adopted 2026-07-30, amendment D1 in force | tag `doctrine-adopted-2026-07-30`; `.syzygy/governance/doctrine/README.md` |
| Craft-and-care approval | ✅ Approved (owner decision D2) | `.syzygy/governance/policies/craft-and-care/INSTALL-RECORD.md` |
| Surface decisions | ✅ Recorded SDR-1…33 | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md` |

## Gates still open, beyond the launch path

| Gate | State | Owning record |
|---|---|---|
| Craft amendment CC-TEST-2 | Awaiting confirmation at the current digest | `INSTALL-RECORD.md` **2026-08-06** correction block |
| Topology bundle | Candidate — no act performed | `.syzygy/map/topology-candidates/BUNDLE-MANIFEST.md` |
| Project overview | Draft — awaiting adoption | `.syzygy/intent/OVERVIEW.md` |
| Doctrine amendment D3 (bounded missions) | Proposed — adopt, amend, or decline | `contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (rev1) |
| Knowledge-hygiene craft policy | Candidate — own craft act (P-12) | `policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` |
| Specification-acceptance standard (CC-SPEC-1…10) | Candidate — own craft act (P-41); a Capability 1 prerequisite | `policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` |
| Shape-to-spec impact rule (CC-IMPACT-1…7) | Candidate — own craft act (P-42); a Capability 1 prerequisite | `policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` |
| License | Undecided — owner/legal | `.syzygy/governance/decisions/LICENSE-DECISION-PACKET.md` |

## Launch-critical owner decisions

Eleven rulings stand between the confirmed contracts and a first
specification. They are prepared, never made, and the queue that owns them
is `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`. One bounded
packet collects them in dependency order:
`round-2026-08f/CAPABILITY-1-OWNER-DECISION-PACKET.md`.

```text
P-33  Wave A install shape      — the ONLY obstacle to offering confirmed Wave A
P-31  merged-but-unreconciled → Unknown
P-36  Unknown versus Gap
P-37  project-shape facets and their authority home
P-38  human entry and repository discoverability
P-39  OpenSpec form and version
P-40  specification granularity
P-35  project operating constraints
P-34  launch-gate v2.0 as process policy
P-41  the specification-acceptance craft act
P-42  the shape-to-spec impact craft act
```

## What exists in this repository

Adopted doctrine; owner-approved engineering policy; recorded owner
decisions with tracked warrant extracts; the candidate contract corpus
(RFC 0001–0011, 39 modules) with its generated manifests, acceptance record,
context-selection fixtures, reviews and verification scripts; the candidate
topology bundle; candidate policy additions; the overview draft; navigation
skills; the launch-gate policy, its record schema, its validator and its
renderer; documentation-only CI.

**No** `openspec/`, no accepted-contract home, no source tree, no product
CI, no implementation backlog.

**One thing this project does not have, stated plainly:** there is no
mechanical task-to-context-packet compiler — `context_load.py` measures a
selection you have already made, and every fixture's selection is
hand-authored. The fixtures' verification checklists say so per fixture.

## Next lawful step

Rule **P-33**. It is the single obstacle to offering a Wave A that is
already confirmed, and nothing downstream — Wave B's offer, the launch-gate
administration, the first specification — moves until it is ruled. The
packet is `.syzygy/governance/decisions/WAVE-A-INSTALL-SHAPE-DECISION.md`,
with the typed-content analysis at
`round-2026-08f/P33-SEMANTIC-INSTALL-ANALYSIS.md`.

After it: the Wave A act, then the Wave B act; P-34 approving the launch-gate
policy; the formal launch administration under that policy, run by a
reviewer outside this corpus's model family; and the owner's separate launch
decision. Specification authoring begins only after that decision, and
implementation only after specifications are accepted.

## How to verify this page

```sh
python3 scripts/check_governance.py
python3 scripts/check_governance.py --selftest
python3 scripts/launch_gate_results.py --selftest            # historical Markdown records
python3 scripts/validate_launch_administration.py --selftest # the v2.0 record path
python3 scripts/render_launch_administration.py --selftest
CS=.syzygy/governance/contracts/candidates/scripts
python3 $CS/verify_final_prespec.py
python3 $CS/build_contract_index.py --check
python3 $CS/build_dependency_index.py --check
python3 $CS/build_budget_report.py --check
python3 $CS/build_active_manifest.py --check
python3 $CS/build_task_router.py --check
python3 $CS/build_task_router.py --selftest
git tag --list 'doctrine-*'
```

The fourteen checks above are the same fourteen the hosted workflow runs
(`.github/workflows/governance-docs.yml`), so "hosted CI is green" and "the
battery is clean" are one claim rather than two a reader conflates.

**Read the output, not the exit code** — a PASS over zero examined items
verified nothing. Every check prints its own denominator; the WARNs are
declared-by-design. `--selftest` covers **the checks that have a fixture**,
not every check: CG-24 computes and prints which families are covered, and
that figure is the one to quote.

**Run it in a clone, not only here.** At one commit these disagreed — 0 FAIL
in the working tree, 1 FAIL in a clone — because a check asked the local
filesystem whether a git-excluded directory existed, and the founder machine
has one. That divergence is invisible from the machine that has the
directory.

**No result figures are quoted on this page.** Twice, figures that were
correct when written went stale within two commits — in the two documents an
owner is sent to for evidence. Run the commands.
