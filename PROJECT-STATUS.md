# Project status

> **As-of: 2026-08-10** (the commit introducing this revision of this file —
> `git log -1 --format=%h PROJECT-STATUS.md`). This file is a hand-authored
> pointer page with an as-of revision: it **must not be the sole source** for
> any fact it states — each row cites the owning record, and where they
> disagree, the record wins and this file is stale. It is regenerated or
> corrected in the same change whenever a gate fires.

## Lifecycle stage

**Final pre-specification.** No application code exists; none may be added
until the foundational contracts are accepted and behavioral specifications
are authored and approved.

## Gates

The single foundational-contract act was **restructured into six wave acts
at round-2026-08d** (owner work order; design:
`.syzygy/governance/contracts/candidates/round-2026-08d/ACCEPTANCE-WAVE-DESIGN.md`).
An **act** is an exact phrase the owner types once, binding one
script-computed digest of one artifact set; a **wave** is one of the six
contract subsets those acts accept independently. The acceptance record
owns the phrases and the ceremony — and its **§7** ("items requiring
explicit owner attention at the gate") is read **before any act** (§2
step 0): it lists the drafted arms and open questions each act ratifies
beyond its digest.
The rev9 and rev10 all-in-one acceptance phrases are retired and satisfy
nothing (the acceptance record's retirement paragraph names them).

**Launch scope (owner-directed, 2026-08-10).** The launch target is
**Capability 1 — Project registration and honest shape visibility**, whose
contract prerequisite is **Waves A + B only**. Waves C1/C2/D1/D2 — and the
P-29/P-30/P-32 rulings that gate their repairs — are **visibly deferred**,
not retired: candidate, not accepted, not used by the launch target, and no
C/D wave act is offered while that posture stands. The posture and its
per-wave reasons are
`.syzygy/governance/contracts/candidates/DEFERRED-WAVE-POSTURE.md`.

| # | Gate | Gate state | Owning record |
|---|---|---|---|
| 1 | Doctrine adoption | ✅ **Adopted** 2026-07-30, amendment D1 in force | tag `doctrine-adopted-2026-07-30`; `.syzygy/governance/doctrine/README.md` |
| 2 | Craft-and-care approval | ✅ **Approved** (owner decision D2) | `.syzygy/governance/policies/craft-and-care/INSTALL-RECORD.md` |
| 3 | Surface decisions | ✅ **Recorded** SDR-1…33 | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md` |
| 4a | Wave A — kernel/evidence/storage/admission/selection (RFC 0001–0006) | ⏳ **Candidate — no act performed** | acceptance record §1 + `wave-manifests/WAVE-A-MANIFEST.txt` |
| 4b | Wave B — the three surfaces (RFC 0007–0009) | ⏳ **Candidate — no act performed** | acceptance record §1 + `wave-manifests/WAVE-B-MANIFEST.txt` |
| 4c | Waves C1/C2 — context packets; selection policy (RFC-0011) | ⏸️ **Deferred — candidate, no act performed, not offered** while the deferred-wave posture stands | `DEFERRED-WAVE-POSTURE.md`; acceptance record §1 + `wave-manifests/WAVE-C1…C2-MANIFEST.txt` |
| 4d | Waves D1/D2 — mission prevention; correction plane (RFC-0010) | ⏸️ **Deferred — candidate, no act performed, not offered** while the deferred-wave posture stands | `DEFERRED-WAVE-POSTURE.md`; acceptance record §1 + `wave-manifests/WAVE-D1…D2-MANIFEST.txt` |
| 5 | Craft amendment CC-TEST-2 (act 2) | ⏳ **Awaiting confirmation** at the current digest | `INSTALL-RECORD.md` **2026-08-06** correction block — the 2026-08-05 block holds the retired `3858820f…` argument (review RD-8, finding S11) |
| 6 | Topology (act 3) | ⏳ **Candidate — no act performed** | `.syzygy/map/topology-candidates/BUNDLE-MANIFEST.md` |
| 7 | Project overview (act 4) | ⏳ **Draft — refactored, awaiting adoption** | `.syzygy/intent/OVERVIEW.md` header |
| 8 | Doctrine amendment D3 — bounded missions (act 5, optional) | ⏳ **Proposed** — adopt, amend, or decline | `.syzygy/governance/contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (rev1; supersedes the original `…-DRAFT.md`) |
| 9 | Knowledge-hygiene craft policy | ⏳ **Candidate — own craft act** (P-12) | `.syzygy/governance/contracts/candidates/policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` |
| 9b | Specification-acceptance craft standard (CC-SPEC-1…10) | ⏳ **Candidate — own craft act; blocking Capability 1 prerequisite** (P-41, added 2026-08-10) | `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`; queue row P-41 |
| 10 | License | ⏳ **Undecided — owner/legal** | `.syzygy/governance/decisions/LICENSE-DECISION-PACKET.md` |
| 11 | Behavioral specifications (OpenSpec) | ⛔ **Not started** — blocked on the wave acts | — |
| 12 | Implementation | ⛔ **Not started** — blocked on gate 11 | — |

**No owner acceptance act has been performed.**
`.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` does not exist,
which is the correct state — it is created by the first act.

The full open-decision queue is
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`. The exact
phrases, digest arguments, and the ceremony live in
`.syzygy/governance/contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`,
which wins over any offering. The `round-2026-08c/`, `round-2026-08b/` and
`round-2026-08/` offerings are superseded and banner-marked. No Wave A or
Wave B offer stands yet: each wave's offer waits on its fresh exact-package
review of the regenerated argument, at the end of the round-2026-08e review
fleet (the register:
`.syzygy/governance/contracts/candidates/round-2026-08e/reviews/DELIVERY-AND-VERDICT-REGISTER.md`).

## What exists in this repository

Adopted doctrine; owner-approved engineering policy; recorded owner
decisions with tracked warrant extracts; the candidate contract corpus
(RFC 0001–0011, 39 modules — RFC-0010 split into a five-module package and
RFC-0011 into two at round-2026-08d) with its generated manifests (active +
six wave), acceptance record, ten context-selection fixtures, reviews, and
verification scripts; the candidate topology bundle; candidate policy
additions; the overview draft; navigation skills; documentation-only CI.
**No** `openspec/`, no accepted-contract home, no source tree, no product
CI, no implementation backlog.

## Open state, honestly

**The two blocking defects the 2026-08-07 readiness report named are
repaired in the candidate bytes, and the repairs are unreviewed.**

1. **Mission safety.** The RFC10-17-vs-RFC10-10 contradiction (budget
   invariant over the ledger, prevention demanded over consumption) is
   repaired by the round-2026-08d rewrite of RFC-0010's budget module
   (six-quantity accounting; enforced-limit admission at the RFC5-21
   launch gate and the RFC5-15 per-transmission predicate), and the
   correction plane was rebuilt against reviews RD-1/RD-1b's blocking
   findings. The pre-split disposition report and the frozen-bytes rule it
   described are historical:
   `…/round-2026-08c/MISSION-SAFETY-CLOSURE-REPORT-vNEXT.md` (banner-marked).
2. **Deterministic context selection.** RFC11-4's unsatisfiable universal
   is replaced by declared `implementation_boundary` metadata (RFC11-13),
   stated traversal/termination rules (RFC11-14), declared doctrine/craft
   ownership or stated judgment (RFC11-15), and clause-first `constrains`
   consumption (RFC11-16); RFC-0001…0005 now carry real phase-rule clauses
   (RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27). The ten fixtures carry a
   task/answer boundary for blind derivation, and fixture 10 covers the
   Trajectory-lifecycle class whose double-count RD-5 found. [Inferred]
   Class coverage is claimed by construction only — no independent blind
   derivation has run over the restructured fixtures yet.

**The Wave A and Wave B repairs have landed; no confirming review is bound
to the regenerated arguments yet.** The round-2026-08d fresh-context review
pass delivered fifteen reviews — **fifteen `REVISE` verdicts, zero
`CONFIRM`** — with all 173 findings disposed in
`…/round-2026-08d/reviews/DISPOSITION-REGISTER.md`. The round-2026-08e
launch-closure pass then repaired Waves A and B under the owner's
Capability 1 direction (semantic deltas:
`…/round-2026-08e/WAVE-A-SEMANTIC-DELTA.md`, `WAVE-B-SEMANTIC-DELTA.md`)
and regenerated their manifests; the C/D-wave findings remain disposed but
unrepaired, deliberately, under the deferred-wave posture. The 08e
fresh-context review fleet is mid-flight (its register is the record of
which reviews are in); **the wave offers wait on the final exact-package
reviews**, and until those bind the current arguments, no wave argument
carries a confirming review. Separately, a pilot administration of the
owner's launch-gate instrument (v1.3, at commit `067d8a0`) returned
**GATE VERDICT: NOT READY** — 17 of 31 questions Not met, including all six
of section E, the OpenSpec-readiness section itself; the raw record is
`…/round-2026-08d/reviews/LAUNCH-GATE-ADMINISTRATION-2026-08-09-RAW.md`.
The instrument is now **v1.8** (candidate; owner approval prepared as
P-34). The repair-and-re-review chain: RD-24 (v1.4, REVISE) → v1.5 →
RD-33 (REVISE, five MAJOR) → v1.6 → RD-34 (REVISE — all twelve RD-33
repairs verified, one BLOCKING: the deferral-carrying pass branch ran no
formula conjunct) → v1.7 → RD-35 (REVISE — all eleven RD-34 repairs
verified, one BLOCKING: the new citation-existence check shipped
inverted, rejecting every real `.syzygy/` decision path, invisible
because no fixture tested the passing direction) → v1.8. The v1.8 batch
is validator-and-records only — RD-35: "the instrument has converged
while the validator has not"; instrument §1–§8 are byte-unchanged from
v1.7. Each re-review verified the prior batch whole before finding the
next class; the P-34 offer waits on the RD-36 re-review of the v1.8
delta, and the formal administration that a launch decision could rely
on has not yet been run.

**One thing this project does not have, stated plainly:** there is no
mechanical task-to-context-packet compiler — `context_load.py` measures a
selection you have already made, and every fixture's selection is
hand-authored. The fixtures' verification checklists say so per fixture.

## Next lifecycle step

The Capability 1 path, per `DEFERRED-WAVE-POSTURE.md`: finish the
round-2026-08e fresh-context review fleet, ending with the exact-package
reviews of the regenerated **Wave A** and **Wave B** arguments; repair
anything those reviews find and re-bind; then the per-wave owner offers
(acts on Waves A and B only), the launch-gate formal administration under
the owner-approved instrument (P-34 first), and the owner's launch
decision — with the authoring-side prerequisites (P-39 form, P-40
granularity, **P-41 the specification-acceptance craft act**) ruled before
the first spec is authored. Waves C1/C2/D1/D2 and the P-29/P-30/P-32 rulings stay deferred
until the owner lifts that posture. After the waves an owner accepts, the
first concrete proposal runs through `/th-projects
project-feature-request` toward an owner-approved OpenSpec delta —
specification authoring, still no implementation.

## How to verify this page

```sh
python3 .syzygy/governance/contracts/candidates/scripts/verify_final_prespec.py
python3 .syzygy/governance/contracts/candidates/scripts/build_contract_index.py --check
python3 .syzygy/governance/contracts/candidates/scripts/build_dependency_index.py --check
python3 .syzygy/governance/contracts/candidates/scripts/build_budget_report.py --check
python3 .syzygy/governance/contracts/candidates/scripts/build_active_manifest.py --check
python3 scripts/check_governance.py
git tag --list 'doctrine-*'
```

Also run `python3 scripts/check_governance.py --selftest`, which puts a
synthetic failing input against **the checks that have a fixture** — not every
check. **CG-24 computes which families are covered and prints the figure every
run**; quote that, never "each check shown able to fail", which two independent
reviews found false while it sat beside a fixture count. The selftest exists
because this repository has shipped a validator that could not fail: the dependency index reported 20
asymmetric edges at every generation while its own drift check reported clean,
because regenerating a knowingly-broken graph reproduces the same
knowingly-broken file.

**The result figures that used to sit here are withdrawn.** They were correct
when written and stale within two commits, twice, in the two documents an owner
is sent to for evidence — the exact failure the battery was built to catch,
recurring in the description of the battery. Run the commands; every check
prints its own denominator and its own rationale, and the WARNs are
declared-by-design (forward references, frozen-packet pointers, report-only
budget and default-load figures, allowlists). **Read the output, not the exit
code** — a PASS over zero examined items verified nothing.

Run it in a **clone**, not only here. At one commit this round the two
disagreed — 0 FAIL in the working tree, 1 FAIL in a clone — because CG-14
asked the local filesystem whether a git-excluded directory existed, and the
founder machine has one. That divergence is the whole failure mode this
repository keeps re-acquiring, and it is invisible from the machine that has
the directory.
