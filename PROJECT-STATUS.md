# Project status

> **As-of: 2026-09-02** (the commit introducing this revision —
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

**Bounded Three-Surface POC mode (non-release).** Capability 1 and its local
runtime are implemented trusted groundwork. On 2026-08-29 the owner directly
authorized a deliberately bounded proof of concept across Polaris,
Trajectory, and Orrery, using Butlers as the initial external proving project.
For this experiment only, the direction supersedes the Capability-1-only and
no-external-project-onboarding restrictions. It authorizes implementation
outside Capability 1 only where required by the experiment; it does not amend
doctrine, accepted contracts, or the adopted Capability 1 specification.

The POC remains local, single-project, file-backed, human-triggered, and
experimental. It does not authorize production release or deployment,
autonomous adoption of intent, Syzygy-authored implementation code, broad
remote access, or multi-user support. Desired, execution, and observed state
remain distinct; no evidence means Unknown; activity or merge state is never
intent satisfaction; human and machine views consume one shared fact model;
every positive claim has resolvable provenance. The owning record is
`decisions/THREE-SURFACE-POC-MODE-DIRECTION.md`.

The runnable POC now includes an explicit human-triggered action that creates
or reuses one bounded Bead, Git-based worker-change observation for that item,
and a separately invoked file-backed JUnit capture, ingestion and verification
path. These mechanisms being implemented is not evidence that a work item was
materialized, a worker changed code, or a matching test artifact is current in
any particular run; the shared model renders the records it actually
has and fails closed on absent or mismatched evidence. The daemon never runs
the observed test suite automatically and Syzygy never dispatches a worker or
writes implementation code.

On 2026-09-01 the owner separately performed the indivisible five-row general
trusted-bootstrap authorization transaction recorded in
`decisions/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md` and the append-only
`decisions/ACCEPTANCE-ACT-RECORD.md`. It amended the accepted RFC 0001–0009
bytes at the exact 30-module amendment manifest, seven signed contract-coverage
artifacts, and CC-SPEC-8. A valid exact-scope human act may now be effective in
state (1), `owner-adopted (bootstrap, uncorrelated)`, or state (2),
`Syzygy-verified`; only state (2) is independently verified. The transaction
granted no effect-specific consent, policy approval, registry adoption,
observation, write, egress, execution, deployment, release, recovery, mission,
or implementation authority.

On 2026-09-02 the owner separately performed the exact PWB state-(1)
amendment sign-off recorded in `decisions/PWB-STATE1-AMENDMENT-ACT.md` and the
append-only act record. The eleven-artifact package at manifest
`14a84aba…b1e` is now the signed behavioral authority: PWB-REQ-005 and
PWB-REQ-022 accept valid exact-scope human acts in state (1) or state (2),
preserve the exact state, fail invalid acts closed and never call state (1)
independently verified. This sign-off created no consent, policy approval,
registry adoption, body-read or implementation authority.

On 2026-09-05 the owner signed Decision 1 of the PWB truth-and-readiness
packet, recorded in `decisions/PWB-TRUTH-READINESS-AMENDMENT-ACT.md` and the
append-only act record: the eleven-artifact package at
`contracts/candidates/pwb-truth-policy-amendment/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`
supersedes the 2026-09-02 digests as the signed behavioral authority (closed
fact/precedence grammar, inert-code admission, deterministic resource
envelope, one transient verbatim baseline requirement, PWB-REQ-021
readiness). The same day the owner approved Decision 2, the amended
secret-classification policy, as a separate state-(1) act bound to the
policy's own SHA-256 and recorded in
`decisions/PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md`; it supersedes
the 2026-09-02 policy approval for that role only, and that earlier record
stays immutable history. The owner then adopted Decision 3, the amended
observer registry entry, the same way
(`decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`), superseding the
2026-09-02 adoption for the registry role only. All three acts of the packet
are performed; consent is unchanged. The owner then continued PWB
implementation authorization for the 2026-09-05 amendment by direct
direction the same day
(`decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`, closing
bead syzygy-8i7): the amended semantics, policy and registry entry are now
the implementation target, with every 2026-09-02 exclusion retained and no
new authority added.

Later on 2026-09-02 the owner performed the three separate effect-specific
acts PWB-REQ-005 requires, each a state-(1) act bound to its artifact's own
SHA-256 at frozen subject `48e0f5d`: observation consent for the configured
Butlers repository (`decisions/PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md`),
approval of the concrete secret-classification policy
(`decisions/PWB-SECRET-CLASSIFICATION-POLICY-ACT.md`), and adoption of the
project-shape observer registry entry
(`decisions/PWB-OBSERVER-REGISTRY-ENTRY-ACT.md`). Each is recorded in the
append-only act record with A1 explicitly absent; none is independently
verified. Together they close the effect gate for the one Butlers
project-shape content class. They grant no implementation authority by
themselves. The owner then granted **PWB implementation authorization** the
same day (`decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`, closing task
1.8): the owner's one-word reply is recorded verbatim with the recorder's
explicit scope reading. Implementation of tasks §2–§5 is now dispatchable
in the ordinary implementation plane; the first Butlers body read is lawful
only after the implementation itself evaluates the three acts under
PWB-REQ-005, and only for the consented content class.

## The launch path, in one table

The launch target is **Capability 1 — Project registration and honest shape
visibility**. Its contract prerequisite is **Waves A + B only**.

| Step | State | Owning record |
|---|---|---|
| Wave A (RFC 0001–0006, 19 modules) | **ACCEPTED — original act performed 2026-08-17.** The owner wrote the exact phrase over the RD-31b-confirmed argument `8972d963…`; the 19 modules were installed at `contracts/rfcs/` under shape (M). That act-time manifest remains immutable history. The installed modules remain accepted and their current bytes are now bound by the 2026-09-01 30-module contract-amendment manifest. | `decisions/ACCEPTANCE-ACT-RECORD.md`; historical tag `wave-a-accepted-2026-08-17`; `contracts/candidates/general-trusted-bootstrap-authorization/CONTRACT-AMENDMENT-MANIFEST.txt` |
| Wave B (RFC 0007–0009 + the three surfaces, 11 modules) | **ACCEPTED — original act performed 2026-08-17, after Wave A.** The owner wrote the exact phrase over the RD-32c-confirmed argument `193e3c1e…`; the 11 modules were installed under shape (M). That act-time manifest remains immutable history. The installed modules remain accepted and their current bytes are now bound by the same 2026-09-01 30-module contract-amendment manifest. | `decisions/ACCEPTANCE-ACT-RECORD.md`; historical tag `wave-b-accepted-2026-08-17`; `contracts/candidates/general-trusted-bootstrap-authorization/CONTRACT-AMENDMENT-MANIFEST.txt` |
| Waves C1/C2/D1/D2 | **Deferred** — candidate, not accepted, not used by the launch target, not offered. Not retired. | `contracts/candidates/DEFERRED-WAVE-POSTURE.md` |
| Owner rulings, 2026-08-16 | **P-31, P-33, P-35, P-36, P-37, P-38, P-39, P-40 ruled** in one adversarially-reviewed sitting, plus P-34 below. Zero contract bytes moved; both wave confirmations survive. | `decisions/DECISION-HISTORY.md` §"Resolved on 2026-08-16 (owner ruling via adversarially-reviewed questionnaire packet)"; each row names its owning record |
| Launch-gate policy | **Owner-approved process policy at v2.4** — P-34 ruled arm (a), 2026-08-16, **with two disclosed BLOCKING residuals** (RD-67 f1, RD-68 f1 — false-`READY` paths reachable only by an adversarial record author), **F5 not promoted**. Ten `REVISE` verdicts across v2.0–v2.4 stand as recorded; this is approval-with-residuals, not a clean review verdict. A bounded v2.5 is an owner option, not a gate. | `decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (the recorded approval); instrument `launch-gate-pre-specifications.md`; `round-2026-08h/reviews/DISPOSITION-REGISTER.md` |
| P-41 + P-42, offered jointly | **PERFORMED — original acts 6 and 7, 2026-08-17, one sitting** (the joint-sitting requirement satisfied). CC-SPEC-1…11 and CC-IMPACT-1…7 remain **in force as owner-confirmed craft**. The original act-time statements and digests remain immutable history. The 2026-09-01 transaction separately amended CC-SPEC-8 at the current policy digest; CC-IMPACT was not amended. | `decisions/ACCEPTANCE-ACT-RECORD.md`; `.syzygy/governance/policies/craft-and-care/INSTALL-RECORD.md`; historical tag `craft-acts-6-7-confirmed-2026-08-17` |
| General trusted-bootstrap authorization transaction | **PERFORMED 2026-09-01 — one indivisible five-row transaction.** RFC 0001–0009 remain accepted at the amended 30-module manifest; the Capability 1 and Three-Surface coverage files plus five PWB coverage artifacts are amended; CC-SPEC-8 is amended. State (1) and state (2) may each carry an effective valid human act, but only state (2) is independently verified. At this act PWB-REQ-005/022 remained state-(2)-only; the separate 2026-09-02 act below superseded that behavior. RFC 0010/0011 remain candidate. | `decisions/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md`; `decisions/ACCEPTANCE-ACT-RECORD.md`; `contracts/candidates/general-trusted-bootstrap-authorization/TRANSACTION-MANIFEST.txt` |
| PWB state-(1) behavioral amendment | **SIGNED 2026-09-02 — exact eleven-artifact package.** Valid state-(1) or state-(2) human acts may satisfy PWB-REQ-005 and PWB-REQ-022 with exact state visible; only state (2) is independently verified, invalid acts fail closed and acts remain warrants. This is behavioral authority only: no effect-specific act, body read or implementation authority was granted. | `decisions/PWB-STATE1-AMENDMENT-ACT.md`; `decisions/ACCEPTANCE-ACT-RECORD.md`; `contracts/candidates/pwb-state1-amendment/PWB-AMENDMENT-MANIFEST.txt` |
| PWB implementation authorization (task 1.8) | **GRANTED 2026-09-02 — owner direction, state (1), recorded verbatim with the recorder's scope reading.** Authorizes tasks §2–§5 of the signed change as one bounded POC improvement cycle and the first body read of the one Butlers repository for content class `declared-project-shape-text`, after the implementation evaluates the three effect acts under PWB-REQ-005. No write, egress, execution, deployment, release, recovery, mission, second repository, or act-bound-artifact edit. | `decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` |
| PWB effect-specific acts (consent, policy, registry) | **PERFORMED 2026-09-02 — three separate state-(1) acts, each bound to its artifact's SHA-256.** Observation consent for the configured Butlers repository and content class `declared-project-shape-text`; the concrete secret-classification policy approved; the read-only, empty-write-surface observer registry entry adopted. A1 explicitly absent; not independently verified; acts are warrants, not evidence of effect. No implementation authority and no body read until task 1.8's separate authorization. | `decisions/PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md`; `decisions/PWB-SECRET-CLASSIFICATION-POLICY-ACT.md`; `decisions/PWB-OBSERVER-REGISTRY-ENTRY-ACT.md`; `decisions/ACCEPTANCE-ACT-RECORD.md`; `contracts/candidates/pwb-effect-acts/PWB-EFFECT-ACTS-MANIFEST.txt` |
| Formal launch administration | **Administration 1 performed 2026-08-18 — verdict `NOT READY`** (10 plain Not-met, 2 scoped, 5 Unknown, 0 reopened). Out-of-family (OpenAI GPT-5.6 Pro), fresh context with disclosed limitations, against commit `71e5986` at approved v2.4; the record validated and its verdict computed by the committed scripts. The strongest findings are stale current-state claims on the default path (since repaired), the contract-index drift (since regenerated), Wave A rejection collapsing the launch path (B4), clone-unreachable D1 rationale (C7), and unbounded governance effort (F6). The 2026-08-09 v1.3 **pilot** (`NOT READY`) remains steering evidence only. | `decisions/launch-gate/ADMINISTRATION-2026-08-18-CAPABILITY-1.json` (the record); `decisions/launch-gate/TREND-LOG.md` |
| Owner rulings, 2026-08-19 (the Administration-1 inputs) | **P-45…P-48 all ruled** in one adversarially-reviewed sitting, applied same day: the **A6 resource envelope stated** (2h/week; Claude-family + occasional GPT 5.6-family review; $200/mo ceiling; 2–3 workstreams) with **syzygy itself named the first proving project** (butlers second); **no governance ceiling** — case-by-case recorded knowingly (F6 stays `Not met`, disclosed, non-conjunct); the **governance-reduction plan adopted as directed work** (§1/§2/§4 retirements executed; §3 awaits the first accepted spec; no deferral created); the **repair cycle bounded at two further administrations** (if Administration 3 is not `READY`, the owner decides directly on the record in hand). Zero contract bytes moved. | `decisions/DECISION-HISTORY.md` §"Resolved on 2026-08-19, second sitting"; records `A6-RESOURCE-ENVELOPE-`, `F6-GOVERNANCE-CEILING-`, `F2-GOVERNANCE-REDUCTION-`, `LAUNCH-REPAIR-STOP-CONDITION-DECISION.md` |
| Owner launch decision | **Made 2026-08-20** — Capability 1 specification authoring authorized, with the `NOT READY` verdict in hand and accepted as diagnostic evidence; the P-48 stop-condition cycle ends early by the owner deciding directly. Specification definition only — no implementation, no implementation planning. | `decisions/CAPABILITY-1-SPECIFICATION-AUTHORING-DECISION.md` |
| OpenSpec (`openspec/`) | **Capability 1 remains ADOPTED: `project-registration-and-honest-shape-visibility`** (schema `spec-driven`, OpenSpec pinned 1.9.0). The owner adopted seven artifacts on 2026-08-20; the 2026-09-01 transaction superseded only `CONTRACT-COVERAGE.md`'s digest, leaving the other six adopted digests and all required behavior unchanged. The accepted specification supersedes the Capability 1 charter for required behaviour. | `decisions/CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md` (original act); `decisions/ACCEPTANCE-ACT-RECORD.md` (coverage amendment); the change directory |
| Implementation | **AUTHORIZED for Capability 1 — act dated 2026-08-21.** Plan first (stack, layout, slices→CAP1-REQ mapping, testing/evidence, review classes), then a bounded Beads backlog and code in ordinary root paths (`apps/**`, `packages/**`, tooling) — never in the governed plane. Capability 1 only; production deployment, onboarding, and release stay separate future decisions. | `decisions/CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md` |
| Three-Surface POC | **AUTHORIZED 2026-08-29, non-release and bounded.** One live Butlers proving project; WIP one for shared-model changes. The runnable implementation exposes human-triggered Bead materialization, worker-change observation, and separate file-backed test-artifact capture/ingestion/verification; availability of those paths is not a positive evidence claim for the current run. The original eight items completed 2026-08-30: all three product assumptions NOT FALSIFIED (`docs/reviews/R-POC-PRODUCT-REVIEW.md`), PRF-1 repair CONFIRMED. The owner's 2026-08-30 direction extends the experiment with **improvement cycles** (review → finding-derived repairs → confirmation, owner-reported per cycle), lifting the eight-item cap and one-review budget; every other bound stands. | `decisions/THREE-SURFACE-POC-MODE-DIRECTION.md`; `decisions/THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md`; `docs/THREE-SURFACE-POC.md` |

**Four original foundational owner acts were performed on 2026-08-17:** Wave
A, Wave B, and craft acts 6 + 7. A separate indivisible five-row amendment
transaction was performed on 2026-09-01, followed by the separate PWB
behavioral amendment on 2026-09-02; neither is a foundational offering.
`.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` exists since the
first act and owns every performed act. The nine still-open foundational
offerings remain open: deferred Waves C1/C2/D1/D2, CC-TEST-2, topology,
overview, D3, and **P-12 knowledge hygiene** as the ninth.

## Gates already closed

| Gate | State | Owning record |
|---|---|---|
| Doctrine adoption | ✅ Adopted 2026-07-30, amendment D1 in force | tag `doctrine-adopted-2026-07-30`; `.syzygy/governance/doctrine/README.md` |
| Craft-and-care approval | ✅ Approved (owner decision D2) | `.syzygy/governance/policies/craft-and-care/INSTALL-RECORD.md` |
| Surface decisions | ✅ Recorded SDR-1…37 | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md` |
| The 2026-08-16 rulings | ✅ See the launch-path table above | `decisions/DECISION-HISTORY.md` §"Resolved on 2026-08-16" |
| The 2026-08-18 questionnaire rulings | ✅ P-14 (MIT), P-16 (term registry as drafting vocabulary), P-24 (D4: inside VIS-4's bounds), P-44 (CC-REV-2 exception declined) — applied 2026-08-19 | `decisions/DECISION-HISTORY.md` §"Resolved on 2026-08-19"; each row's own decision record |
| The Administration-1 owner inputs | ✅ P-45…P-48 ruled and applied 2026-08-19 — see the launch-path table above | `decisions/DECISION-HISTORY.md` §"Resolved on 2026-08-19, second sitting" |
| License | ✅ **MIT** — root `LICENSE`; contributor-agreement posture remains a separate open question | `decisions/LICENSE-CHOICE-DECISION.md` |
| General trusted-bootstrap transaction | ✅ Five rows performed indivisibly 2026-09-01; provenance semantics, seven coverage artifacts and CC-SPEC-8 reconciled; no effect-specific or implementation authority granted | `decisions/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md`; `decisions/ACCEPTANCE-ACT-RECORD.md` |
| PWB state-(1) amendment | ✅ Eleven artifacts signed 2026-09-02; PWB-REQ-005/022 now accept valid state (1) or state (2), with exact state visible and invalid acts fail closed; no effect-specific or implementation authority granted | `decisions/PWB-STATE1-AMENDMENT-ACT.md`; `decisions/ACCEPTANCE-ACT-RECORD.md` |
| PWB truth-and-readiness amendment (Decision 1) | ✅ Eleven artifacts signed 2026-09-05, superseding the 2026-09-02 digests; implementation-authorization continuation granted the same day | `decisions/PWB-TRUTH-READINESS-AMENDMENT-ACT.md`; `decisions/ACCEPTANCE-ACT-RECORD.md`; `contracts/candidates/pwb-truth-policy-amendment/OWNER-DECISION-PACKET.md` |
| PWB secret-policy amendment (Decision 2) | ✅ Amended policy approved 2026-09-05 in state (1) at its own SHA-256, superseding the 2026-09-02 approval for the policy role only; the earlier record stays immutable history | `decisions/PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md`; `decisions/ACCEPTANCE-ACT-RECORD.md` |
| PWB observer-registry amendment (Decision 3) | ✅ Amended registry entry adopted 2026-09-05 in state (1) at its own SHA-256, superseding the 2026-09-02 adoption for the registry role only; the earlier record stays immutable history | `decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`; `decisions/ACCEPTANCE-ACT-RECORD.md` |
| PWB implementation authorization | ✅ Granted 2026-09-02 by owner direction; PWB tasks §2–§5 dispatchable, body read gated on PWB-REQ-005 evaluation inside the implementation | `decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` |
| PWB implementation-authorization continuation | ✅ Continued 2026-09-05 by owner direction for the 2026-09-05 amendment only; amended spec, policy and registry entry are the implementation target, every original exclusion retained | `decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` |
| PWB effect-specific acts | ✅ Consent, secret policy and observer registry entry each signed separately 2026-09-02 in state (1); effect gate closed for the one Butlers project-shape content class; no implementation authority granted | `decisions/PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md`; `decisions/PWB-SECRET-CLASSIFICATION-POLICY-ACT.md`; `decisions/PWB-OBSERVER-REGISTRY-ENTRY-ACT.md` |

## Gates still open, beyond the launch path

| Gate | State | Owning record |
|---|---|---|
| Craft amendment CC-TEST-2 | Awaiting confirmation at the current digest | `INSTALL-RECORD.md` **2026-08-06** correction block |
| Topology bundle | Candidate — no act performed | `.syzygy/map/topology-candidates/BUNDLE-MANIFEST.md` |
| Project overview | Draft — awaiting adoption | `.syzygy/intent/OVERVIEW.md` |
| Doctrine amendment D3 (bounded missions) | Proposed — adopt, amend, or decline. **D4 was ruled 2026-08-18** (inside VIS-4's bounds; reviewer's §1.2 wording designated) — a D3 rev2 and its VIS-3 fresh-reader review precede act 5 | `contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (rev1); `decisions/D4-RULING-DECISION.md` |
| Knowledge-hygiene craft policy | Candidate — own craft act (P-12) | `policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` |
| Decision-record convention (P-43) | Open — not launch-gating; earliest gate is a deferral-bearing administration | `decisions/PENDING-OWNER-DECISIONS.md` row P-43 |

## Next lawful step

The PWB behavioral amendment, the three effect-specific acts and the
implementation authorization are all signed for the one Butlers project-shape
content class. Project-wide Polaris implementation is now the lawful next
work, in this order:

1. Implementation follows `docs/PWB-IMPLEMENTATION-PLAN.md` (plan bead
   closed 2026-09-03): slices P1–P8 mapped to the bounded Beads backlog under
   `syzygy-1z3`, shared-model WIP one; the body-read authority evaluator (P1)
   lands before any observer code.
2. Before the first body read, the implementation evaluates the three effect
   acts under PWB-REQ-005 and fails closed on any invalid act; the acts are
   warrants, not evidence. Reads stay inside `declared-project-shape-text`
   and the approved secret-classification policy.
3. Review → repair → confirmation on frozen heads, then an owner report
   before any next cycle (tasks §5).
4. Add write, egress, execution, deployment, release, recovery, or mission
   authorization only if that effect is actually requested; none is today.

RFC 0010/0011 and the nine still-open foundational
offerings — including P-12 knowledge hygiene — remain candidate/open.

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
python3 scripts/build_capability_1_spec_dependencies.py --check  # capability 1 spec: warrants -> generated union
python3 scripts/build_capability_1_spec_dependencies.py --selftest
DR=.syzygy/governance/contracts/candidates/round-2026-08f/fixtures/DRY-RUN-ADMINISTRATION.json
python3 scripts/validate_launch_administration.py $DR
python3 scripts/render_launch_administration.py $DR --check
git tag --list 'doctrine-*'
```

The eighteen checks above are the same eighteen the hosted workflow runs
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
