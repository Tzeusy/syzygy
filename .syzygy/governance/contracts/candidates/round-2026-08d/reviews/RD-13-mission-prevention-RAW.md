(part 1/2)

Reviewer: mission-prevention (RD-13)
Date: 2026-08-09
Commit: 771965c
Files read: `C/rfcs/RFC-0010/README.md`; `mission-identity-approval-and-lifecycle.md`; `prevention-envelope-and-attention.md`; `budget-reservation.md`; `portfolio-and-cross-project-consent.md`; `effects-recovery-and-stop.md` (read to resolve RFC10-18(a)/RFC10-19/RFC10-20/RFC10-23 cross-references cited from the prevention plane); `.syzygy/governance/doctrine/vision.md`; `.syzygy/governance/doctrine/security.md`; `C/rfcs/RFC-0003/governance-homes-and-owner-acts.md` (RFC3-16 only); `C/rfcs/RFC-0005/consent-egress-secrets.md`, `execution-profiles.md` (RFC5-12/14/15/21/22 only).

Sweep denominator for every absence claim below: all **6** files under `C/rfcs/RFC-0010/` (README + 5 modules), swept with Python `re` (not system ugrep) over the literal terms `pinned`, `child`, `decomposition`, `dispatch`, `running`, `park duration`, `establisher`, `evaluator`, `item rate`, `exempt`, `embed`, `wall-clock`, `no effects`, `render`, `target project`, plus a full `RFC\d-\d+(\([a-z]\))?` citation extraction.

---

## Answers to the eight review questions

**1. Approval.** [Observed] No path from minted to `running` skips an owner act, but no clause says so directly. The guarantee is assembled from three: RFC10-9 (*"An envelope present in a governed tree without verifiable act provenance authorizes nothing (RFC3-16(a)'s effect rule); its mission cannot leave `awaiting-approval`"*), RFC10-17 (*"**authorized** (the owner act's figure)"* — with no owner act there is no `authorized`, so the admission inequality admits no dispatch), and RFC10-24's blanket hold. See finding 9.

**2. Pinned inputs.** [Observed] Pinned at mint, asserted immutable — but the approval act binds the **envelope's** digest, not the mission record carrying the pinned inputs. See finding 4.

**3. Envelope establisher / self-widening.** [Observed] The envelope is established by an owner act under RFC10-9, always A1-mechanism, never a bootstrap tree record. RFC10-8 closes the direct routes I attacked: budget, level, surfaces, paths, tools, gates, child-envelope excess, cross-mission budget consumption, ambiguity re-reading, expiry-widening (RFC10-12: *"expiry may narrow, pause, or block, and may never widen an envelope or approve anything"*), and store-side widening (RFC10-15 store entries are RFC3-16(a) artifacts; RFC10-21's *"the lesser binds"*). Two residual routes survive: attention allowance (finding 2) and child obligation-shaped fields (finding 10).

**4. Propose-only honesty.** [Observed] A propose-only mission cannot be rendered "no effects" for disclosure or spend — RFC10-7 states that itself, so it survives without module 4. Dimension (i) is not covered by RFC10-7's sentence, and no prevention-plane clause requires the mission record to enumerate the dimensions at all. See finding 8.

**5. Attention.** [Observed] Debits and establisher inheritance are defined; the stated invariant is nonetheless false, and demand can be manufactured by fan-out. See finding 2.

**6. Lifecycle.** [Observed] Every state in RFC10-5's diagram has an exit. Park bounds are duration-typed, explicitly exclude counts and rates, and terminate in a non-empty referent (the wall-clock budget every runnable mission must declare). The pre-running states are the exception: their expiry arrow has no defined trigger for a root mission (finding 3), and `awaiting-approval` is absorbing by RFC10-24's design (correct, and human-cancellable).

**7. Cross-project consent.** [Observed] Direct touching is closed: RFC10-6 forbids bypassing RFC5-12 consent; RFC10-7 denies authorship in a non-target project's namespaces; RFC10-21 is content-keyed and fails closed. The indirect route — origin attribution not surviving a lawful copy — is open. See finding 6.

**8. Guardrail boundaries.** [Observed] RFC10-10's MUST is scoped honestly to Syzygy's choke points, and for resource consumption it names its mechanism. For every other bound it names none. See finding 5.

---

## Findings

### 1. A human cancellation of a parent mission has no binding clause that stops its running children under the prevention plane alone — and the README's justification for staging that reference is false for this case
**Severity: blocking**

RFC10-17(a), release table, row 8:

> | the **parent** of outstanding child grants reaches any terminal state | the stop propagates to every derived child (RFC10-20(b)); each child grant is released at that child's resulting terminal record, to the parent's terminal accounting. No child grant survives its parent's terminal record except a reservation retained for a run that did not terminate, named under the row below |

RFC10-20 is a module-4 (correction-plane) clause. The package index offers the two planes for separate acceptance:

> The two planes are independently acceptable: a propose-only mission posture (RFC10-7's cap) is safe under the prevention plane alone, because the only effects it can cause are drafts inside the two governed namespaces, consented provider disclosure, and reserved spend — each bounded by modules 1–3 and 5.

and justifies the staged cross-references thus:

> Cross-module references from the prevention plane into module 4 (the release table's recovery hooks, RFC10-18 naming in lifecycle text) are **staged references**: they bind when module 4 is accepted and, until then, mark duties that cannot yet arise because no effect class that would trigger them is authorized.

[Observed] That justification does not hold for this row. A parent reaching `cancelled` by human act — RFC10-5's *"any non-terminal state → cancelled | expired   (human act)"* — requires **no effect class whatsoever**; it is reachable on day one of a propose-only posture. The row is also not a "recovery hook", so it is not even inside the README's own enumeration of what is staged.

[Observed] Absence sweep, denominator 6 files / 33 occurrences of `child`: the only parent→child termination propagation in the package is `budget-reservation.md:152` (the row above, citing RFC10-20(b)) and RFC10-20(b) itself at `effects-recovery-and-stop.md:252`. RFC10-5's human-act limb reaches "any non-terminal state" **of the mission the act names**; RFC10-8 makes children reservations but never says a parent's termination reaches them.

[Inferred] Consequence under prevention-plane-only acceptance: an owner cancels a mission; its derived children — whose only authorizing provenance is *"the **parent's** owner act plus a recorded derivation"* (RFC10-8) — keep dispatching against grants debited from a mission whose terminal accounting has already released in full. The stop the owner performed does not reach the work their act authorized. This defeats the human-control posture VIS-4 exists to hold and contradicts RFC10-8's own premise that children are reservations against one act.

**Repair.** Add to RFC10-8 (prevention plane, self-contained) a limb: *a derived child's authorization terminates when its parent reaches any terminal state; the child transitions to `cancelled` with that reason, dispatches nothing further, and its grant releases to the parent's terminal accounting.* Then RFC10-20(b) becomes the stronger run-level guarantee layered on top rather than the sole carrier. Separately, correct the README's staged-reference paragraph: either enumerate this row and state its true (non-effect-class) justification, or move the justification into a clause.

---

### 2. RFC10-8's attention invariant is stated as absolute and is contradicted by RFC10-22's exemptions; child fan-out amplifies the gap into owner-attention exhaustion
**Severity: major**

RFC10-8:

> **The debit covers attention allowance as it covers budget**: a child's maximum outstanding attention count and maximum item rate (RFC10-22) are debited from the parent's declared maxima at grant time under the same sibling-sum invariant — one owner act never mints more outstanding attention demand than its envelope declares.

RFC10-22:

> **Exactly two classes of item are exempt from both bounds, and the enumeration is closed.** **(i)** The item reporting that a bound was reached, or the resulting state change — minted and delivered at the maximum, because a safe behaviour the owner cannot be told about is, at the queue, the unsafe one

[Observed] The two are inconsistent on their face. With an undeclared maximum — *"an undeclared maximum means one outstanding item — the narrowest reading (RFC10-7)"* — a single mission reaching its bound mints the exempt class-(i) item and stands at two outstanding items, i.e. more than its envelope declares. RFC10-8's invariant is false even before any child exists.

[Observed] Absence sweep, denominator 6 files: `decomposition` occurs exactly once, at `prevention-envelope-and-attention.md:121` —

> an agent may mint a child mission only where the parent envelope **explicitly grants decomposition** (an owner-approved envelope field; absent the grant, the narrow reading is no children)

— and it is grant-shaped, not count-shaped. No maximum-child-count is a required envelope field anywhere in the package (0 hits for any child-count bound).

[Inferred] Attack: with decomposition granted, a deriving agent mints *N* children, each declaring a maximum outstanding attention count of zero (the sibling sum is then trivially within the parent's declared maxima, satisfying RFC10-8's debit). Each child reaches its bound on its first mandated item, pauses, and mints the exempt class-(i) item — which is exempt from **both** bounds, and therefore from the parent's debited maxima too. Dedup does not merge them: RFC10-12 binds *"the affected mission, work, and project"* into each item, so *N* children present *N* distinct decisions. *N* is limited only by budget debit, and a child that pauses immediately is cheap. RFC10-22's own closing sentence states the property this defeats: *"denial of owner attention is reachable without widening anything."*

**Repair.** (a) Restate RFC10-8's invariant with its true scope — *"never mints more **non-exempt** outstanding attention demand than its envelope declares"* — or make class-(i) items debit against the declaring mission's own allowance with a floor of one. (b) Add a **maximum derived-child count** (and maximum derivation depth) to RFC10-7's required envelope minimum, debited under the same sibling-sum invariant; unstated is one, per RFC10-7's narrowest reading.

---

### 3. RFC10-5's pre-running expiry arrow cites a maximum that RFC10-17(a) defines only for child missions; a root mission's `draft`/`awaiting-approval`/`approved` states are unbounded
**Severity: major**

RFC10-5's diagram:

> ```text
> draft | awaiting-approval | approved → expired   (maximum time to first
>                                                   dispatch, RFC10-17(a))
> ```

RFC10-17(a)'s row defining that maximum:

> | `draft`, `awaiting-approval`, or `approved` — **a child mission holding a grant it has not yet run under** | **held from grant time (RFC10-8), and bounded**: every child grant carries a **maximum time to first dispatch**, declared by the parent's envelope, defaulting to the parent's maximum park duration; at that maximum the child transitions to `expired` and its grant is released to the parent's remaining envelope. A grant held by a child that never starts is a reservation, and this row is its stated release point |

[Observed] The row's subject is *a child mission*, and the declaring authority is *the parent's envelope*. A root mission has no parent and no grant. Sweep for `first dispatch`, denominator 6 files, 3 occurrences (`budget-reservation.md:84` — an unrelated provider-quota limb; `budget-reservation.md:151`; `prevention-envelope-and-attention.md:137`, RFC10-8's child-grant sentence): the maximum is defined for child grants only.

[Observed] RFC10-5's "no park is indefinite" limb does not reach these states either — it is scoped to *"**`blocked`** or **`paused`**, whatever gave rise to it."* Pre-running states are not parks.

[Inferred] So a root mission can sit in `approved` indefinitely: a standing, live authorization with pinned inputs, dispatchable at any later moment. This is the precise shape verification rule 8 names — a transition justified by a clause whose own scope excludes the case.

**Repair.** Either add a root-mission limb to RFC10-17(a) (a maximum time to first dispatch declared by the envelope, defaulting to a stated finite figure — the envelope's shortest declared duration-typed maximum, as RFC10-5's park cascade already does), or delete the arrow from the diagram and state plainly that pre-running states are bounded only by human act.

---

### 4. The approval act binds the envelope's digest; the pinned inputs live on the mission record, whose digest no clause binds
**Severity: major**

RFC10-4:

> binding at minimum: its **objective and rationale**; its **target** …; its **exact pinned inputs** — the doctrine, contract, specification, policy, and evaluation revisions it runs under, by digest or revision identity; its **initiating owner act** … Pinned inputs are immutable for the mission's life

RFC10-14:

> The mission-approval **act record** does not live here: it is appended to `.syzygy/governance/decisions/`, binding **the envelope's exact digest** (RFC3-16(b) item 3) — the in-tree envelope file plus any stamp is never itself the approval.

RFC3-16, the mechanism both cite:

> The **effective** lifecycle status of a normative or authorization-bearing artifact is determined by an **owner-act record** (RFC3-16(a)/(b)) binding the act to **the artifact's exact immutable content digest** (RFC3-16(b) item 3).

[Observed] Sweep for `pinned`, denominator 6 files, 4 occurrences (`mission-identity-approval-and-lifecycle.md:86, 91, 92`; `effects-recovery-and-stop.md:187`). None binds the pinned inputs to a digest the act covers. Sweep of RFC10-7's envelope minimum: pinned inputs are **not** an envelope field — the list runs change classes, prohibited/human-only surfaces, maximum autonomy level, projects/repositories/paths, tools/model-provider classes/execution profiles, budgets, required gates and independent reviews, evidence and reconciliation requirements, stop/pause/cancellation/expiry conditions, checkpoint and recovery obligations, escalation triggers, completion predicate.

[Inferred] Result: "what the owner approved is what runs" is digest-enforced for the envelope and rests on an unenforced immutability assertion for the pinned inputs — in a tree RFC5-15 already tells us is *"writable by fleet workers, SEC-3's untrusted actor class."* RFC10-4's own escalation limb (*"a change to any pinned input … raises an escalation"*) presupposes a detectable change, which requires a bound baseline that no clause supplies.

**Repair.** Amend RFC10-14 so the mission-approval act record binds **both** digests — the envelope's and the mission record's (or a single manifest digest covering both) — and state that a mission record whose digest does not match the one the act bound authorizes nothing, on RFC3-16(a)'s effect rule.

---

### 5. RFC10-10's "MUST prevent" names a mechanism clause for resource consumption only; paths, tools, surfaces and gates carry the MUST with no mechanism named in this package
**Severity: major**

RFC10-10:

> execution guardrail enforcement — budgets, permissions, write boundaries, risk floors, stop conditions, protected surfaces, required approvals; Mission Control MUST prevent every act it mediates from exceeding the approved authority and resource envelope

and, for one of those:

> **For resource consumption this prevention is discharged by RFC10-17's enforced-limit admission rule**: a mediated dispatch or provider transmission is admitted only against an enforced limit with remaining headroom, and refused otherwise.

[Observed] Citation sweep across all 6 files: `RFC5-21` — the clause carrying *"filesystem confinement to the declared scope"* and the violation *"a write outside the declared scope"* — appears 6 times, all in `budget-reservation.md` (lines 65, 77, 117, as RFC10-17's enforced-limit anchor) and `effects-recovery-and-stop.md` (249, 287, kill switch). It appears **zero** times in `prevention-envelope-and-attention.md`. RFC10-10 names only RFC5-15 as *"the same single-choke posture"* — a stated analogy, not a mechanism.

[Inferred] So the package discharges its own MUST honestly for one dimension and asserts it for the rest. This is exactly the asymmetry review question 8 asks about: for permissions, write boundaries and protected surfaces, prevention is asserted over something the package elsewhere only accounts for or observes. The mechanism plausibly exists in RFC5-21, but "plausibly exists elsewhere" is not a discharge, and RFC10-16 defers the runtime that would supply it.

**Repair.** In RFC10-10, add the parallel sentence RFC10-17 already earns: *for path, tool, surface and gate bounds this prevention is discharged by RFC5-21's declared-scope filesystem confinement and network policy at the launch gate and RFC5-15 at the egress gate; a bound with no such enforcement point is monitoring-only and supports no autonomous dispatch* — mirroring RFC10-17's own resource-kind classification, which is the right shape and should be generalized rather than left resource-specific.

(part 2/2)

### 6. RFC10-21's content-keyed predicate is evaluated only at the egress choke point; nothing requires origin attribution to survive a lawful propose-only copy into another project's namespace
**Severity: major**

RFC10-21:

> A context packet, prompt, summary, embedding, or any other composite assembled **under any mission** is subject, **at the RFC5-15 choke point**, to the egress-consent record of **every project whose content it embeds** … The predicate is a property of the *content*, not of the mission's scope declaration … so does a composite whose embedded content cannot be attributed to a project of origin at all.

RFC10-7, propose-only:

> author drafts, proposals, and submissions into `.syzygy/**` and `openspec/**` **of the mission's declared target projects** rendered unadopted (RFC3-16) — a path grant reaching another project's checkout confers no authorship in that project's governed namespaces (the content-keyed reasoning of RFC10-21, applied to the write side).

[Observed] Sweep for `embed`, denominator 6 files, 6 occurrences — all inside RFC10-21, all at the egress choke point. RFC10-7's write-side sentence governs **where** a mission may write, not **what origin** the written content may carry. The reverse direction — importing project B's content *into* project A's governed namespace — is addressed by neither.

[Inferred] Attack, every step lawful under the quoted clauses: a mission targets A; its owner-approved envelope grants a path reaching B's checkout; B carries an RFC5-12 observation consent, so RFC10-6's gate is satisfied; the agent mechanically copies B's content into a draft under A's `.syzygy/**` (no egress, so RFC10-21 never fires); a later composite embeds that file, which is now attributable to A, and egresses to a provider consented for A alone. Outcome: B's source at a provider B never named — SEC-2's stated violation, *"project source sent to an unnamed model provider"* — reached without widening anything.

[Observed] RFC10-21's own wording (*"a property of the content"*) supports the closing reading; the defect is that the package supplies no rule making that reading computable after a copy. RFC10-14's *"typed, provenance-labeled"* discipline is about mission-home artifacts, not content origin.

**Repair.** Extend RFC10-21 with a second limb symmetric to the first: *content copied or derived across a project boundary carries its project of origin as recorded provenance; a composite's embedded-project set is computed from that provenance, not from the namespace the content currently occupies, and content whose provenance was not recorded at copy time is unattributable and fails closed.* Then RFC10-7's parenthetical claim about "the content-keyed reasoning applied to the write side" becomes true rather than aspirational.

---

### 7. The claim that makes the prevention plane separately offerable is non-clause README prose, and its enumeration of staged references is incomplete
**Severity: major**

Package index, §"The two planes, and the acceptance seam":

> The two planes are independently acceptable: a propose-only mission posture (RFC10-7's cap) is safe under the prevention plane alone, because the only effects it can cause are drafts inside the two governed namespaces, consented provider disclosure, and reserved spend — each bounded by modules 1–3 and 5.

[Observed] This paragraph carries no clause identifier. Every module in the package states *"Effective status is established solely by an owner-act record binding this file's exact content digest"* — so the README is an index, and its seam paragraph is section prose, not a clause. The load-bearing safety claim of a separate prevention-plane acceptance therefore rests on text that cannot be cited as binding.

[Observed] The paragraph's enumeration of staged references — *"the release table's recovery hooks, RFC10-18 naming in lifecycle text"* — omits at least RFC10-17(a)'s RFC10-20(b) parent-stop row (finding 1) and RFC10-7's reliance on RFC10-23's dimension vocabulary and RFC10-18(a)'s predicate scoping (finding 8). An enumeration offered as the account of what is staged, that is not a sweep, is the shape verification rule 9 names.

**Repair.** Move the independent-acceptability determination into a clause — either a new clause in module 1 or a limb of RFC10-16 — stating what the prevention plane guarantees standing alone, what each staged reference is, and what does *not* hold until module 4 binds. Produce the staged-reference list by sweep over the package with a stated denominator, not by recollection.

---

### 8. Propose-only's "no effects" prohibition omits dimension (i), and under prevention-plane-only acceptance no clause requires the mission record to state the effect dimensions at all
**Severity: major**

RFC10-7:

> **Consented provider disclosure and metered spend are effects in their own recorded dimensions** — external disclosure and resource consumption (RFC10-23) — pre-authorized by the consent record and the reserved budget; a `propose-only` mission that disclosed content or spent budget is **never rendered as having had "no effects"**

RFC10-23 (module 4), the clause that does cover all four:

> `propose-only` (RFC10-7) bounds dimension (ii) to nothing and is **never rendered as "no effects"** where dimension (i), (iii), or (iv) is non-empty … A mission's terminal record states all four dimensions.

[Observed] RFC10-7's prohibition names disclosure and spend only. Dimension (i) — *"drafts, proposals, and submissions inside the `.syzygy/**` and `openspec/**` namespaces"* — is the dimension propose-only is *for*, and it is the one RFC10-7's own sentence does not protect. [Observed] Sweep for `no effects`, denominator 6 files, 5 occurrences: 4 in `effects-recovery-and-stop.md`, 1 in `prevention-envelope-and-attention.md` (the sentence above). The four-dimension enumeration and the terminal-record duty exist only in module 4.

[Inferred] Under prevention-plane-only acceptance the negative rule survives (it is self-contained in RFC10-7) but the positive one does not: no prevention-plane clause requires a mission's record to enumerate what it disclosed, spent, or authored. RFC10-17's six quantities cover (iv) on the budget ledger and RFC5-15's audit record covers (iii) on the egress trail — but neither is the mission's account of itself, which is what VIS-2's honesty bar is asked to judge.

**Repair.** Pull the dimension enumeration and the "terminal record states all four dimensions" duty into the prevention plane — RFC10-7 or a new prevention-plane clause — leaving RFC10-23 in module 4 to carry only the correction-plane consequence (that RFC10-18(a) engages on dimension (ii) alone). Extend RFC10-7's prohibition to name dimension (i) explicitly.

---

### 9. No clause conditions dispatch on approval having occurred or on the mission being in `running`
**Severity: minor**

[Observed] Sweep for `dispatch`, denominator 6 files, 33 occurrences. Every one ties dispatch to budget and reservation — RFC10-17's *"**No work is dispatched without reserving its declared maximum cost against the envelope at dispatch time**"* — and none to a lifecycle state or to approval. RFC10-5's diagram implies `approved → running` at first dispatch but states no such rule; `running` appears in `prevention-envelope-and-attention.md` exactly once (line 63), in an unrelated ambiguity limb.

[Inferred] The prohibition does hold, by composition: RFC10-9 denies an unapproved envelope any force, RFC10-17's `authorized` is *"the owner act's figure"* so the admission inequality admits nothing without one, and RFC10-24 holds every mission at `awaiting-approval` today. A reader asked "can a mission begin work without an owner approval act?" must assemble three clauses across three modules to answer, and the wave split may separate them.

**Repair.** One sentence in RFC10-5's fixed-now list: *no work is dispatched and no Syzygy-mediated act is admitted under a mission outside `running`; the transition into `running` requires the approval act RFC10-9 predicates.*

---

### 10. A deriving agent authors the child's obligation-shaped envelope fields; RFC10-8's debits and inheritances enumerate only the grant-shaped ones
**Severity: minor**

RFC10-8 enumerates what a child may not exceed (*"not budgets, not autonomy level, not surfaces, not paths, not tools, not gates"*), what is debited (budget; *"maximum outstanding attention count and maximum item rate"*), what is inherited (*"the parent's declared completion establisher and effects-determination evaluator"*), and what the parent declares for it (*"a **maximum time to first dispatch**"*).

[Observed] Absent from all four lists, by sweep over the same 6 files: **maximum park duration** (RFC10-5: *"Every non-terminal park carries a **maximum park duration**, declared by the envelope"* — the child's own envelope), **maximum item expiry** (RFC10-22), and the correction-plane declarations (recovery obligations, sibling disposition, named recovery owner — `recovery owner` occurs exactly once in the package, at `effects-recovery-and-stop.md:183`, with no child-inheritance rule).

[Inferred] A deriving agent can therefore give a child a longer park duration than its parent's, holding a slice of the parent's debited budget past what the owner act contemplated. RFC10-8's general phrase *"a child mission whose envelope exceeds the parent's remaining envelope"* arguably reaches this, but "exceeds" is undefined for obligation-shaped and duration-shaped fields, and RFC10-7's obligation limb governs *unstated* fields, not a child stating a weaker one.

**Repair.** Add to RFC10-8: *a derived child's duration-typed and obligation-shaped envelope fields are inherited from the parent and may only be narrowed; a child field stating a weaker obligation or a longer maximum than the parent's binds nothing and the parent's figure governs.*

---

### 11. Whether wall-clock accrues while a mission is parked is undefined, and two bounds rest on it
**Severity: minor**

RFC10-5's park cascade terminates in the wall-clock budget:

> the set is never empty: wall-clock is a budget, an undeclared budget is zero delegated wall-clock (RFC10-7), so every runnable mission declares a wall-clock budget and this limb always has a referent.

RFC10-22's item-expiry default rests on the same quantity, measured differently:

> **an undeclared maximum item expiry means the mission's remaining wall-clock budget at mint time**

[Observed] The first reads the **declared** figure, the second the **remaining** figure. Sweep for `wall-clock`, denominator 6 files, 8 occurrences: no clause states whether wall-clock is consumed while a mission sits in `paused` or `blocked`.

[Inferred] Both bounds stay finite under either reading, so this is not a soundness defect — but a runtime implementing "wall-clock accrues while parked" and one implementing "it does not" produce different expiry instants for the same envelope, and RFC10-17(a)'s held-reservation row inherits the difference.

**Repair.** One sentence in RFC10-17 or RFC10-5 fixing whether parked time debits the wall-clock budget, and from what instant a maximum park duration runs.

---

VERDICT: REVISE
