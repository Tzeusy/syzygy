# MISSION-CONTROL-REVIEW — charter §14 assessment of the Mission/Autonomy material

**What this is.** A review artifact produced in the human-clarity refactor
round (charter §14, required output listed at §20). It is **not authority**,
accepts nothing, and adopts nothing. It proposes no edit to any artifact
inside the act-1 frozen digest set. Where it recommends a change, the change
is either (a) carried in a separate, unadopted packet at the owner's act-5
gate, or (b) recorded as a candidate for a *future* amendment after the
relevant act, precisely because editing a digest-bound artifact now would
churn the manifest and invalidate the confirming cycle.

**Reviewed material and exact digests as read (2026-08-05):**

| Artifact | sha256 |
|---|---|
| `rfcs/RFC-0010-mission-control-autonomy.md` | `8481335836115c5ec0316f62fd229177f17292e35cc1d71e9d48d0445c3574c6` |
| `DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md` (D3 as drafted) | `30efb7c5fc933e18fc5f5e5c3daaab7689881d9e51cb282e997f0a4c450ba173` |
| `doctrine/vision.md` | `816ad50c59abb08ab85dcb1be18e39c4123695521914249d9ded1a980beafa86` |
| `doctrine/architecture.md` | `e19d255f9a2f2ddaf4da83eb0fe74f17b17d96d31b31bb03f76accb1a2ac11de` |

[Observed] RFC-0010's live digest equals its `ACTIVE-CONTRACT-MANIFEST.txt`
entry — the contract is unedited since manifest generation, and nothing in
this review changed it.

**Method and its limits.** RFC-0010 was read in full, clause by clause.
RFC-0011 was read at RFC11-1..3 and its RFC 0005 integration; RFC 0005's
egress (RFC5-14) and execution-profile (RFC5-18/20) modules were read at the
clauses cited here. Every "term does not appear" claim below was produced with
Python `re` over the file, **not** with `grep` (this machine's `grep` is
ugrep; see `PROCESS-LESSONS.md`). Counts are counted from the charter's own
fenced lists, not recalled. The prior assessment was read — it lives at
`_bootstrap/knowledge-refactor/MISSION-AUTONOMY-ASSESSMENT.md`, which is
**git-excluded founder-local history, unavailable in a clone and never
authority**; every claim of its that matters here is restated inline, so this
review is readable without it. Its §1 method warning — seven field names that
*look* absent because RFC-0010 states them in different words — was treated as
a live trap and re-tested rather than inherited.

---

## 1. Does the contract match the owner's operating model?

Charter §14's model:

```text
Human defines goal, constraints, risk, budget, and evidence bar
→ human approves one bounded Mission
→ agents plan, execute, verify, retry, and recover within the envelope
→ human is interrupted only for declared exceptions
```

| Model step | Clause | Verdict |
|---|---|---|
| Human defines goal, constraints, risk, budget, evidence bar | RFC10-4 (objective, rationale, target, pinned inputs), RFC10-7 (the envelope's full field set) | **COVERED** |
| Human approves **one bounded** Mission | RFC10-4 (initiating owner act; "a mission without verifiable owner-act provenance authorizes nothing"), RFC10-9 (approval is an RFC3-16(a) act, and specifically a *runtime* A1-mechanism act) | **COVERED** |
| Agents plan / execute / verify / retry / recover inside the envelope | RFC10-6 (missions authorize materialization of work; work semantics stay RFC 0008/0002), RFC10-7 (retry and concurrency budgets, checkpoint and recovery obligations), RFC10-8 (no self-widening), RFC10-10 (preventive guardrail enforcement) | **COVERED** |
| Human interrupted only for declared exceptions | RFC10-13 ("the attention queue **compresses event volume into decision-ready packets**; streaming every run event to the human is a violation of this clause, not a conservative default") plus its enumerated escalation triggers | **COVERED** |

[Observed] The contract states the model the owner asked for, in the direction
the owner asked for it: RFC10-13 makes routine streaming a *violation*, which
is stronger than merely permitting compression.

**One qualification, which is the whole of the D3 question.** RFC-0010 §2
concedes it itself: *"missions can be specified under this contract but cannot
lawfully operate under unamended doctrine's one-pass trigger."* The operating
model is contractually shaped and doctrinally un-launched. See §5.

**Consequences the owner is already holding** (acceptance record §7 items 6–8,
restated here only as review context, not re-decided): mission approval is a
runtime act, so **Mission Control V0 must ship the approval ceremony and
external audit trail as a hard precondition** (RFC10-9); **decomposition is off
by default** (RFC10-8); and **D4** — whether a bounded-autonomy doctrine
amendment adopted through Syzygy's own ceremony is doctrine amending doctrine —
remains the owner's to rule.

---

## 2. Is Mission Control workspace-level, and never a fourth truth surface?

**Verdict: COVERED, with one placement note.**

- **RFC10-1** states it directly: a *workspace-level operator domain*, minting
  no project truth; a Mission Control view of project state is "a projection
  of kernel answers (RFC 0006), rebuildable and non-authoritative."
- **RFC10-15** keeps portfolio authority in a distinct plane and states the
  tie-break in the safe direction: where the workspace store's own enumeration
  (per-project budgets, pause modes) meets the prohibition on governing
  project-internal state, **the prohibition wins** — pausing a project means
  Syzygy refuses to schedule against it and never mutates project status.
- **RFC10-2** forbids the failure mode that would create a shadow surface in
  practice: scraping human-rendered output instead of consuming the semantic
  API is "never a conforming integration."
- Violation cases 3 and 6 name both drift paths concretely.

[Inferred] **Placement note (minor).** RFC10-14 homes project-bound mission
artifacts at `.syzygy/work/missions/<mission-id>/` — inside Trajectory's
namespace. That is consistent with RFC 0003's closed six-name validator
(acceptance record §7 item 1) and RFC10-6 already separates missions from work
semantically. The residual risk is presentational, not structural: surface
specification must ensure a mission record is never enumerated *as* a work item
in Trajectory. Recorded for the Mission Control changeset, not a contract gap.

---

## 3. Mission envelope — charter §14 field coverage

Sixteen fields, counted from the charter's fenced list.

| # | Charter field | Clause | Mark |
|---|---|---|---|
| 1 | objective | RFC10-4 — "its **objective and rationale**" | **COVERED** |
| 2 | target projects/capabilities | RFC10-4 — "its **target** (workspace, projects, capabilities, and/or requirements)" | **COVERED** |
| 3 | exact intent revisions | RFC10-4 — "its **exact pinned inputs** — the doctrine, contract, specification, policy, and evaluation revisions it runs under, by digest or revision identity"; immutable for the mission's life, with a pinned-input change raising an escalation rather than silently retargeting | **COVERED** |
| 4 | autonomy level | RFC10-7 — "the **maximum autonomy level**"; enumeration deferred (§8 q2) but the clause **fails closed**: "the maximum autonomy level of every envelope is capped at **propose-only**" until an owner act enumerates the vocabulary | **COVERED** |
| 5 | allowed/prohibited change classes | RFC10-7 — "permitted **change classes**; **prohibited and human-only surfaces** (the VIS-4 always-human classes … appear here as a floor, not a choice)" | **COVERED** |
| 6 | write/tool/network/model permissions | RFC10-7 — write: "allowed **projects, repositories, and paths**"; tool and model: "allowed **tools, model/provider classes, and execution profiles** (by RFC5-18 profile identity)". **Network** is bound *compositionally*, not as a named field: the profile identity carries RFC5-20's network policy, and RFC10-6 holds the RFC5-14 egress-consent gate unbypassable. See note below. | **COVERED** |
| 7 | budget | RFC10-7 — "**budgets** — token, monetary, wall-clock, retry, and concurrency" | **COVERED** |
| 8 | time limit | RFC10-7 — wall-clock budget, plus "**stop, pause, cancellation, and expiry conditions**"; RFC10-5 makes `expired` always reachable | **COVERED** |
| 9 | parallelism | RFC10-7 — "concurrency" (portfolio-level fleet capacity separately at RFC10-15) | **COVERED** |
| 10 | required evidence | RFC10-7 — "**evidence and reconciliation requirements**"; RFC10-6 binds the completion predicate to a declared minimum RFC2-25 evidence tier, defaulting to the strongest applicable tier when unstated | **COVERED** |
| 11 | review floors | RFC10-7 — "**required gates and independent reviews**" | **COVERED** |
| 12 | stop conditions | RFC10-7 (field) + RFC10-11 (bound exhaustion halts and never self-extends) | **COVERED** |
| 13 | escalation conditions | RFC10-7 ("**escalation triggers**") + RFC10-13 (minimum trigger set) | **COVERED** |
| 14 | completion predicate | RFC10-7 (field) + RFC10-6 ("**A mission is not work, and work is never proof**"; predicate evaluated against evidence, never against work having been performed) | **COVERED** |
| 15 | checkpoint and rollback | RFC10-7 — "**checkpoint and recovery obligations**"; RFC10-11 — in-flight work "completes or checkpoints per the envelope's recovery obligations". **Gap:** the words *rollback*, *compensation*, and *revert* appear **zero times** in RFC-0010 (verified with Python `re`, not `grep`). No clause states what a mission owes for effects already applied when it fails, is cancelled, or expires. | **PARTIAL** |
| 16 | context packet identity | Carried by **RFC11-1** (the packet identifies its objective, the governing envelope, and its own final digest) and **RFC11-2/RFC11-3** (packet digest is part of every execution record; a governed run without a packet is a violation). Within RFC-0010 the obligation appears only in §5's *unnumbered* integration prose — "every mission-spawned agent run receives a governed context packet; the envelope is a mandatory packet input" — and no `RFC10-n` clause binds a mission to the packets its runs consumed. | **PARTIAL** |

**Totals: 14 COVERED · 2 PARTIAL · 0 ABSENT.**

**Note on field 6 (network).** Marking this ABSENT would be a fabricated gap —
exactly the failure the prior assessment logged. Network reach *is* bounded:
the envelope grants an execution profile by identity, and RFC5-20's network
policy is part of that profile (including the "no route to Syzygy" rule); and
content leaving owner-controlled infrastructure needs an RFC5-14 egress-consent
record naming provider and content classes, which RFC10-6 forbids any mission
from bypassing. Under RFC10-7's unstated-is-narrowest rule, an envelope with no
profile grant permits no execution at all, hence no network. The residual is
**ergonomic, not authorizational**: narrowing network reach for one mission
requires selecting or minting a different execution profile, because the
envelope has no field with which to narrow a profile in place. That belongs to
surface specification.

**Note on field 15 (rollback).** The gap does not bite today: while RFC10-7's
propose-only cap stands, no mission can produce the external effect that would
need rolling back. The autonomy extension register already schedules the work —
"Compensation/rollback of *external* effects: **required before
auto-merge/deploy**". The honest statement is that *checkpoint* is a stated
obligation and *rollback* is a scheduled future obligation with no current
clause, and that the gate blocking it is real.

**Note on field 16 (context packet identity).** Arguably by design: packet
identity is per-run, missions bind pinned *inputs*, and the join runs through
execution records. The reviewable consequence is citation-mechanical. RFC11-1
has context compiled by selecting "the exact RFC clauses, **by clause ID**";
an obligation living in §5's integration prose has no clause ID to be selected
by. The obligation is not lost — RFC11-1 and RFC11-3 carry it independently —
but a reader compiling only RFC-0010 clauses would not see it. Remedy, if any,
is an OpenSpec requirement at surface specification, not a contract edit.

---

## 4. Attention Item — charter §14 field coverage

Eight fields, counted from the charter's fenced list. All are in **RFC10-12**,
whose binding list is quoted per row.

| # | Charter field | RFC10-12 text | Mark |
|---|---|---|---|
| 1 | what happened | "**what happened**" | **COVERED** |
| 2 | why human judgment is required | "**why human attention is required**" | **COVERED** |
| 3 | evidence | "the **evidence and its uncertainty** (Unknowns rendered as Unknowns, RFC 0002)" | **COVERED** |
| 4 | available choices | "the **available choices**" — plus "the **consequence of each choice**", which the charter did not ask for | **COVERED** |
| 5 | default if ignored | "the **default and expiry if ignored** — an expiry default must be safe: expiry may narrow, pause, or block, and may **never widen** an envelope or approve anything" | **COVERED** |
| 6 | blocked work | "what work is **blocked**" | **COVERED** |
| 7 | reversibility | "whether the situation is **reversible**" | **COVERED** |
| 8 | deadline/expiry | "the default and **expiry** if ignored"; RFC10-13 adds that items never silently disappear — each terminates in a recorded resolution, expiry-to-safe-default, or explicit human dismissal, all attributable and queryable | **COVERED** |

**Totals: 8 COVERED · 0 PARTIAL · 0 ABSENT.**

RFC10-12 exceeds the charter in three respects worth naming because they are
what an implementation would be tempted to drop: the **safe-expiry rule**
(expiry may never widen or approve — violation case 4 is exactly the deploy
approved by an expiring item); the **resolution act and its provenance** as a
bound field, with a resolution that authorizes anything being an RFC3-16(a)
act; and the **anti-bulk rule** — "a bulk act over unenumerated items resolves
nothing."

[Inferred] One deferral is disclosed rather than hidden: §7 defers
"attention-queue SLA and batching policy," so *how promptly* an item reaches a
human is unspecified. That is a surface-specification question; the charter
did not ask for it.

---

## 5. Doctrine interplay — does "not autonomous" accidentally require
task-level approval?

### 5.1 The exact text today

`vision.md` lines 72–74, verbatim:

> - **Not autonomous.** The loop is human-triggered; autonomy beyond VIS-4's
>   stated bounds is licensed only through the mechanism VIS-4 names, never by
>   reinterpretation.

`architecture.md` lines 246–248, verbatim:

> The loop is **human-triggered**: someone specs a desired shape, then
> deliberately triggers a propagate/sync pass.

### 5.2 What the unamended wording actually requires

[Observed] `vision.md`'s bullet does **not**, by itself, fix the *grain* of a
trigger — it says only that the loop is human-triggered. Read alone, it does
not require task-level approval.

[Observed] `architecture.md` does fix the grain: a trigger is "a propagate/sync
pass" — singular. A mission authorizing repeated plan/materialize/execute/
verify/re-plan cycles is more than one pass, so under unamended doctrine each
cycle needs its own trigger.

[Inferred] The precise defect is therefore **not** that doctrine requires
approval of every *task* — it is that doctrine ties one human act to one
*pass*, which under a mission collapses into approving each cycle, which is
functionally the micromanagement the charter's §3 item 14 forbids. RFC-0010 §2
and the D3 draft both state this consequence without softening it, and the D3
draft is explicit that declining is a lawful choice that keeps missions out of
operation.

[Observed] The second half of the `vision.md` bullet — "autonomy beyond VIS-4's
stated bounds is licensed only through the mechanism VIS-4 names" — is
untouched by D3 and does the load-bearing work of keeping VIS-4 intact. It also
forecloses the dangerous misreading: a mission cannot be *its own* licensing
mechanism for autonomy beyond VIS-4's bounds, because that bullet says only
VIS-4's named mechanism can license it.

### 5.3 D3 as drafted — sufficient in substance

**Verdict: substantively sufficient, and not overbroad in effect.** It fixes
the grain and nothing else. VIS-4's always-human classes, envelope approval and
widening, and every otherwise-applicable gate are preserved by the
architecture.md insertion's own last sentence ("a mission is authority to
proceed inside the gates, never authority to skip one"); RFC10-7 independently
seats the VIS-4 classes in every envelope as "a floor, not a choice."

**But three defects justify a minimally revised packet:**

**(a) The `vision.md` insertion point is broken as specified.** The draft says
the insertion goes *"after 'The loop is human-triggered;'"* — the quoted anchor
includes the semicolon. Applied literally, the amended sentence reads:

> The loop is human-triggered; (a trigger may authorize one pass or one
> bounded, envelope-limited mission — see architecture.md; …) autonomy beyond
> VIS-4's stated bounds is licensed only through the mechanism VIS-4 names…

— a parenthetical stranded between a semicolon and the clause it precedes, with
no punctuation joining them. This is not a style quibble: the draft's own
adoption mechanics say *"Amend both files in place with the verbatim text
above,"* and VIS-3 requires a fresh-reader review at material amendment. An
insertion instruction that cannot be applied without an unrecorded editorial
judgment is a defect in an owner-act artifact. The fix is one word of
placement: insert **before** the semicolon.

**(b) The `architecture.md` insertion mirrors RFC10-7's field enumeration into
doctrine.** The parenthetical reads: *"(objective, budgets, risk limits,
protected surfaces, stop conditions — at minimum; the envelope also bounds
permitted write scope, tools, required gates and reviews, evidence obligations,
and the completion predicate)"*. The first half is a **floor** ("at minimum") —
a floor cannot conflict with a wider contract list. The second half is a
**mirror** of RFC10-7's enumeration, and it creates a second normative home for
one norm: amend RFC10-7's field set later and doctrine silently diverges. This
is charter §3 item 5 (typed authority — doctrine answers *why*, accepted RFCs
answer load-bearing *how*) and the §16 knowledge-health detector "duplicate
normative claims" / "conflicting definitions", applied to doctrine itself.
Minimal fix: keep the floor, drop the mirror, and say in one clause that the
exact field set is contract material.

**(c) The packet is silent on act ordering.** The draft correctly states that
"nothing in RFC 0010 or 0011 depends on this amendment being adopted." It does
not state the converse. Act 5 (adopt D3) and act 1 (accept the foundational
contracts) are independent gates that may be performed in either order. If D3
is adopted first, doctrine — binding, adopted — uses the terms *bounded
mission* and *autonomy envelope* while **no accepted contract defines either**;
RFC10-7's unstated-is-narrowest rule and the propose-only cap would not be in
force to constrain them. The operational risk today is nil (there is no code),
but it is precisely the "hidden active authority" / "orphaned clause" condition
the charter's own health list names. And the ordering has a harder edge:
**if the owner rules D4 the other way** — that a bounded mission *is* autonomy
beyond VIS-4's stated bounds — then VIS-4's own terms require an accepted
adjudication RFC as well, and D3 alone is insufficient; RFC-0010 could serve
only after acceptance *and* explicit designation. Under that ruling, act 1
must precede act 5 as a matter of VIS-4, not of convenience.

### 5.4 Minimal change, stated

Written to a separate, unadopted packet:
`.syzygy/governance/contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md`.
The original draft is untouched. The three changes are: move the `vision.md`
insertion before the semicolon (and give it a precise anchor); replace the
`architecture.md` field-mirror with a doctrine-level floor plus an explicit
"exact fields are contract material" pointer; add a sequencing note (packet
prose, **not** doctrine text) recording the act-1/act-5 dependency and its
D4-conditional hard form. One judgment call is flagged in the packet rather
than made silently: the revised `vision.md` insertion also carries the
gate-preservation clause, which the original carried only in `architecture.md`.

---

## 6. Semantics under scenario

Each scenario names the clauses that decide it and then the residual, if any.

### S1 — Budget exhausts mid-mission

**Decided by:** RFC10-11 — reaching any bound "halts further materialization
and execution under that mission — transition to `paused` or `blocked` with an
Attention Item — and never silently raises the bound, borrows against another
mission, or downgrades the required gate set." RFC10-8 makes an agent-side
raise a violation. Violation case 2 names the "helpfully extends it 10%"
failure directly. The Attention Item's expiry cannot widen (RFC10-12), so
walking away cannot resume the mission.

**Residual — the sharpest seam found in this review.** RFC10-11's last
sentence: *"Partial work already lawfully dispatched completes or checkpoints
per the envelope's recovery obligations."* Completing in-flight work after the
bound is exhausted **spends past the exhausted bound**. No clause requires that
overrun to be bounded, reserved for in advance, or recorded as an overrun. A
conforming implementation could therefore exhaust a token budget and then spend
materially more finishing what was dispatched, with the record showing a
respected bound. [Inferred] The fix is small and belongs in a future RFC-0010
amendment, not now: either require the envelope to reserve completion headroom
inside the bound, or require the overrun to be recorded as attributable
evidence with its own Attention Item. Recorded here as a post-act-1 amendment
candidate — proposing it as an edit today would churn the frozen digest and
force another confirming cycle for a defect that cannot bite while the
propose-only cap holds.

### S2 — A stop condition fires during a write

**Decided by:** RFC10-10 — guardrail enforcement is *preventive*: an
out-of-envelope act "is refused at the choke point … not performed-then-flagged"
(the same single-choke posture as RFC5-15). RFC10-11 halts further
materialization. Every guardrail decision — allow, refuse, halt — is recorded
as identified evidence attributable to mission, work item, and principal
(RFC5-25). RFC10-10 also scopes its MUST honestly: an actor holding
externally-granted toolchain credentials can act outside Syzygy's mediation,
and those effects are bounded by adapter and credential authorization (VIS-5),
not by this runtime.

**Residual.** RFC-0010 states no atomicity or interruption semantics for an act
already at the choke point — a half-applied multi-file write, a pushed commit.
The envelope's recovery obligations are the slot where that belongs, and the
format is deferred (§7). This is the same hole as field 15 (rollback), seen
from the other side. It cannot bite while the propose-only cap holds, since a
propose-only mission produces no external effect to interrupt.

### S3 — Child-mission decomposition requested without a grant

**Decided by, cleanly:** RFC10-8 — "**Child missions are reservations, not
copies:** an agent may mint a child mission only where the parent envelope
**explicitly grants decomposition** … absent the grant, the narrow reading is
no children." An attempt is self-widening, so: mission → `blocked`, attempt
recorded as evidence, Attention Item minted. RFC10-5 makes the exit from that
`blocked` state a **human resolution act** — "an agent's 'condition cleared'
assertion never takes that transition." Where a grant *does* exist, every child
grant is debited from the parent's remaining envelope at grant time, so
siblings can never jointly exceed the one owner act. Violation case 1 names
both halves. **No gap.**

### S4 — A run needs network egress the envelope never named

**Decided by:** the composition in §3's field-6 note. No profile grant → no
execution → no network (RFC10-7's narrowest reading). A profile grant carries
RFC5-20's network policy. Content leaving owner infrastructure additionally
needs an RFC5-14 egress-consent record naming provider and content class, which
RFC10-6 forbids any mission from bypassing, and RFC11-1's packet is explicitly
"not a consent" instrument. **Fails closed at three independent points.**

### S5 — A pinned input changes while the mission runs

**Decided by:** RFC10-4 — pinned inputs are immutable for the mission's life;
"a change to any pinned input does not silently retarget a running mission — it
raises an escalation (RFC10-13) whose choices include re-approval against the
new inputs." RFC10-13 lists the trigger set; RFC10-12 requires the choices and
each choice's consequence to be stated. Re-approval is a resolution that
authorizes something, hence an RFC3-16(a) act. **No gap.**

### S6 — A mission blocks on a protected surface, then the agent re-plans

**Decided by:** RFC10-13 (a protected or human-only surface in the proposed
path is an escalation trigger) and RFC10-10 (the act is refused at the choke
point, and the refusal is recorded evidence).

**Residual, and I want to be precise about how weak it is.** RFC10-5's
human-exit rule is scoped to blocks "where the block arose under RFC10-8 or
RFC10-11" — self-widening and bound exhaustion. A block arising from an
RFC10-13 escalation is not covered by that sentence, so on its face an agent's
"condition cleared" assertion could take the transition. [Inferred] In practice
the hole closes: re-planning *around* a protected surface is exactly what a
bounded mission is for and needs no human; and a wrong self-certification gets
refused again at RFC10-10's preventive choke point rather than executed. What
remains genuinely unstated is whether an escalation-sourced block is
human-exit-only by rule. That is a surface-specification question for the
Mission Control changeset, and it is listed as such rather than as a contract
defect.

---

## 7. Findings, ranked

| # | Finding | Severity | Disposition |
|---|---|---|---|
| F1 | D3's `vision.md` insertion anchor produces an ungrammatical doctrine sentence, and its `architecture.md` insertion mirrors RFC10-7's envelope field enumeration into doctrine, creating a second home for one norm | **Material** — both live in an artifact the owner is asked to adopt verbatim | Minimally revised packet written (§5.4); original draft untouched; owner adopts, amends, or declines |
| F2 | Act ordering is unstated: adopting D3 (act 5) before act 1 leaves *bounded mission* and *autonomy envelope* as adopted doctrine terms with no binding definition; and if the owner rules D4 the other way, VIS-4's own terms force act 1 first | **Material, governance-shaped** — zero operational risk today | Sequencing note added to the revised packet as packet prose, not doctrine text |
| F3 | RFC10-11 permits in-flight work to complete past an exhausted bound with no clause requiring the overrun to be reserved, bounded, or recorded (S1) | **Material after the propose-only cap lifts; inert before it** | Post-act-1 amendment candidate — not proposed as an edit now, because RFC-0010 is digest-frozen and the defect cannot bite under the cap |
| F4 | Rollback / compensation of already-applied effects has no clause in RFC-0010 (zero occurrences of *rollback*, *compensation*, *revert*) | Moderate; scheduled | Already gated by the autonomy extension register ("required before auto-merge/deploy"); recorded, not re-proposed |
| F5 | Context-packet identity reaches missions only through RFC-0011 clauses and RFC-0010's unnumbered §5 prose; a clause-ID-based context compilation of RFC-0010 alone would not surface it | Moderate; citation-mechanical | OpenSpec requirement at surface specification |
| F6 | Escalation-sourced `blocked` states have no stated human-exit rule (RFC10-5 covers only RFC10-8/RFC10-11 blocks) | Low — closed in practice by RFC10-10's preventive re-check | Surface-specification question for the Mission Control changeset |
| F7 | Portfolio fleet concurrency (RFC10-15) and per-mission concurrency (RFC10-7) have no stated composition rule | Low — derivable: RFC10-8 forbids widening, RFC10-15's writ ends at scheduling | Note for surface specification |
| F8 | Mission artifacts home inside `.syzygy/work/` — structurally correct, presentationally adjacent to work items | Low | Surface specification must never enumerate missions as work items |
| F9 | Narrowing network reach for one mission requires selecting or minting a different execution profile; the envelope has no field to narrow a profile in place | Low, ergonomic | Surface specification |

**Carried forward unchanged from the prior assessment** (re-checked, still
true): `Recovery Action` is the one arguable un-reified entity — RFC-0010
states recovery as an *obligation* without naming the record it produces, and
entities without names get invented locally by implementers. No term is
proposed for the registry on that basis.

---

## 8. What this review did not do

- **It did not re-open the term-registry question.** The prior assessment's
  recommendation (admit none of Agent Profile, Budget, Checkpoint, Recovery
  Action; `Human Attention Item` already at T-30) was re-read and is not
  disturbed.
- **It did not read all 28 RFC-0010/0011 clauses in full.** RFC-0010: all 16,
  in full. RFC-0011: RFC11-1..3 and the RFC 0005 integration only. A defect in
  RFC11-4..12 would not have been found here.
- **It did not enumerate the autonomy-level vocabulary** (§8 q2 is open by
  owner design; the propose-only cap is the contract's own safe default), nor
  rule on §8 q1 or q3.
- **It did not edit, and did not propose editing, any artifact inside the act-1
  frozen digest set.** F3–F6 are recorded as post-act or
  surface-specification work for exactly that reason.
- **It rules on nothing.** D3, D4, and every act remain the owner's.
