# Report — rev10 mission/autonomy safety review (directive §13.3)

**Reviewer role:** adversarial mission/autonomy safety. **Verdict: EXCEPTIONS** (14, ranked; 6 blocking for a Mission Control acceptance act, 8 non-blocking but should be recorded).

**What I read** [Observed]: `rfcs/RFC-0010-mission-control-autonomy.md`, `rfcs/RFC-0011-context-compiler.md`, `DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md` in full; `rfcs/RFC-0003/governance-homes-and-owner-acts.md` in full; `rfcs/RFC-0003/manifests-and-namespace.md` §2.4–2.6; RFC5-3/4/5/6/12/13/14/15/16/18/25/26 (clause bodies); RFC6-13..17; RFC8-12/16/28/30; doctrine `vision.md`, `security.md`, and `architecture.md`'s "The loop" paragraph; and the supporting records `02-OWNER-DIRECTION-RECORD.md`, `06-CONTEXT-LOAD-MAP.md`, `07-AUTONOMY-EXTENSION-REGISTER.md`, `08-OPEN-QUESTION-TRIAGE.md`, `09-OPEN-SPEC-READINESS-REPORT.md`. I did **not** read RFC-0001, 0002, 0004, 0007, 0009 in full, nor `04-CLAUSE-MIGRATION-MATRIX.md`; findings that would depend on those are labelled [Unknown] where relevant.

**One structural observation up front** [Observed]: `grep` over `rfcs/` shows **no clause in RFC 0001–0009 cites any `RFC10-n` or `RFC11-n`**. Every autonomy safety obligation in this package is single-sourced in RFC-0010/0011. That is not itself a defect (they are new and downstream), but it means the no-self-widening rule has no redundancy: if RFC10-8 is later amended, nothing else in the corpus independently forbids envelope widening. Worth the owner knowing before the act.

---

## Part A — Attacks run, path by path

### A1. Uncorrelated bootstrap approval as a sufficient mission authorization
**Path:** A fleet worker (SEC-3 untrusted actor class, extended to committed artifacts at RFC3-16(a)) commits a mission record, an envelope, and a bootstrap-shaped act record — owner phrase + digest + commit + tag, all of which are tree-resident and therefore forgeable from inside the tree (RFC3-16(c) says exactly this). The mission leaves `awaiting-approval` and runs.
**Clauses:** RFC10-9 (rfcs/RFC-0010, L173–178); RFC3-16(a) *Effect when the predicate fails*; RFC3-16(c) final bullet.
**Analysis:** RFC3-16(c) is unambiguous — "an authorization-bearing artifact resting on a state-(1) record **has not satisfied the predicate**, and RFC3-16(a)'s *Effect when the predicate fails* governs its dependent effects", i.e. the run does not launch. RFC10-9 sentence 1 says the envelope "is honored only with verifiable owner-act provenance, **and** under the two-state model an uncorrelated bootstrap approval renders honestly as owner-adopted, never as verified." Conjoining those two clauses invites the reading *"a bootstrap approval is honored; it just renders differently."* Sentence 3 then blocks only an envelope "without act provenance" — not "without **verifiable** act provenance" — so an attacker with a forged bootstrap record argues sentence 3 is inapplicable and sentence 2 tells them how to render it.
**Verdict: GAP — blocking.** The operative consequence is never stated either way. Under the strict (correct) reading, **no mission may be approved or run until the A1 correlation mechanism exists** — i.e. Mission Control cannot lawfully operate at V0, which is the entire point of OD-R10-1. Under the loose reading, missions run on a forgeable record. One of those is the owner's decision and neither is written down. (Note: RFC5-15 and RFC5-18(c) impose the same pre-A1 block on egress and code execution, so the constraint pre-exists RFC-0010; RFC10-9 is the only place in the corpus that pairs the predicate with a "renders as owner-adopted" clause in a way that reads as a carve-out.) [Observed for the clause texts; Inferred for the two readings.]

### A2. Sibling child missions over-subscribing one parent budget
**Path:** A planner creates child missions C1…Cn. Each is minted with an envelope no wider than "the parent's **remaining** envelope" *evaluated at mint time*, before any child has spent. Each child then exhausts its own grant. Total spend is n × parent-remaining.
**Clauses:** RFC10-8 (L159–170) forbids "creating a child mission whose envelope exceeds the parent's remaining envelope" and "consuming another mission's budget"; RFC10-11 (L201–208) forbids borrowing.
**Analysis:** Neither clause is violated on its face. No child exceeds the remaining envelope at its own mint instant, and no child consumes *another mission's* budget — each consumes its own lawful grant. The missing concept is **reservation**: nothing defines a child grant as debited from the parent at grant time, nor states the invariant Σ(outstanding child grants) + parent spend ≤ parent budget.
**Verdict: GAP — blocking.** This is a clean arithmetic widening that survives a literal reading of the load-bearing clause. [Inferred.]

### A3. Child missions minted without an owner act
**Path:** As above, but the question is whether an agent may mint a child mission at all.
**Clauses:** RFC10-4 (L104–112) — every mission binds "its **initiating owner act** (mission approval is an authorization-bearing act under RFC3-16(a) — a mission without verifiable owner-act provenance authorizes nothing)"; RFC10-8's child-mission limb.
**Analysis:** These two are in direct tension. If every mission needs its own owner act, RFC10-8's child limb guards a case that cannot arise and children are useless for delegation; if children inherit the parent's act, RFC10-4's "a mission without verifiable owner-act provenance authorizes nothing" is contradicted. RFC10-8's phrasing ("not by creating a child mission whose envelope **exceeds**…") strongly implies agents *may* create children within bounds.
**Verdict: GAP — blocking (paired with A2).** The ambiguity sits in the exact place a self-widening agent would probe, and RFC10-7's narrow-reading rule does not reach it (it governs envelope *fields*, not contract interpretation). [Observed texts; Inferred tension.]

### A4. Launching on silently thinned mandatory context
**Path:** An envelope does not state a context-completeness requirement. The compiler produces a packet marked incomplete/Unknown with the gap named. The run launches anyway, and the disclosure is read by nobody.
**Clauses:** RFC11-6 (rfcs/RFC-0011, L114–122): "**where the governing policy or envelope requires complete context**, the run does not launch"; RFC10-7's narrow-reading rule (L155–157).
**Analysis:** Blocking on incomplete context is **opt-in**. Context completeness is not among RFC10-7's enumerated envelope fields, so "an envelope field left unstated is the narrowest reading" does not supply a fail-closed default for it. This inverts the corpus's own posture everywhere else — RFC5-14 ("undeterminable fails closed"), RFC5-16 (unclassifiable content excluded, not indexed), VIS-2 (no evidence means Unknown, not success), SEC-5 ("unclassifiable fails closed"). RFC11-6's own sentence ends "rather than proceeding on silently thinned context", which is precisely what the default permits.
**Verdict: GAP — blocking.** An agent running under a doctrine rule it was never given is indistinguishable from one ignoring it (RFC-0011 §2's own argument), and the failure is invisible to the human. [Observed clause; Inferred consequence.]

### A5. Guardrail enforcement asserted over a plane Syzygy does not control
**Path:** Not an attack by an agent — an attack on the owner's belief. RFC10-10 (L182–199) states "Mission Control **MUST prevent** execution outside the approved authority and resource envelope" and that enforcement is "**preventive**, not merely observational: an out-of-envelope act is refused at the choke point… not performed-then-flagged."
**Clauses:** RFC10-10; doctrine `vision.md` "**Not an enforcement engine — outward**… It shows untruth in governed projects; it does not make it impossible"; VIS-5 (effects on other authorities occur only through typed authorized adapters); `architecture.md` ("Work-to-code and code-to-deployment belong to the orchestration toolchain, **outside Syzygy's body**").
**Analysis:** Syzygy can refuse to dispatch, authorize, or mediate an act that traverses *its* choke point. It cannot prevent a fleet worker holding its own toolchain credentials from writing a file, opening a PR, or invoking a provider. RFC10-10 does not scope its MUST to the choke point, so it reads as a guarantee the architecture cannot deliver. [Inferred] This is the most dangerous failure mode in the package because it makes human control *nominal while believed to be real*: the owner grants a wider envelope than they otherwise would, trusting a preventive guarantee whose actual reach is "whatever the adapter grant is".
**Verdict: GAP — blocking.** Fix is textual, not architectural: scope the MUST to acts mediated by Syzygy, and state honestly (VIS-1 rank 1) that effects reached through the actuator toolchain are bounded by the adapter authorization, not by the guardrail runtime.

### A6. Agent-model profiles as self-asserted gate satisfaction
**Path:** An envelope requires an independent review (RFC10-7 lists "required gates and independent reviews"). Routing consults an agent/model profile whose `independence` property is a **profile fact** (RFC11-10, L153–162). A worker writes or amends a profile asserting the independence property, and the required gate is satisfied without a second actor.
**Clauses:** RFC11-10; RFC3-16(a) (predicate limb 2 "unblocks or widens a claim class"; limb 4 "binds project truth in a way no downstream status check can falsify").
**Analysis:** RFC11-10 requires profiles to be versioned and requires *quality* history to be "identified evidence, not reputation prose" — but the independence property, the permission set, and the task/risk classes served are plain assertions. The profile registry home is deferred (RFC 0011 §8 q2), so no write-authority class is assigned. Nothing in RFC-0011 cites RFC3-16(a). RFC3-16(a) is self-extending by predicate ("in scope whether or not the RFC introducing it cites this clause"), so it formally reaches profiles — but the corpus's own instruction applies: where limb 4 is the only catch, "the honest reading is that the artifact's class has not yet been thought about properly — **treat that as a finding, not as settled coverage**."
**Verdict: GAP — blocking.** RFC-0011 violation case 7 (L206–208) describes this exact failure but attributes it to fallback-order logic, i.e. as a bug rather than as a forgeable-assertion class. [Observed clauses; Inferred that the predicate reaches profiles.]

### A7. Suppressing mandatory context by editing selection metadata
**Path:** RFC11-4 (L100–107) selects mandatory context from `depends_on`/`provides_to`, "explicit `applies_to` and clause-level metadata". An untrusted writer edits `applies_to` front matter in a governed artifact so the selector never generates it as a candidate. The packet reports no omission, because omission accounting (RFC11-1, "the **explicitly omitted candidate context, each with its reason**") only covers candidates the selector produced.
**Clauses:** RFC11-4, RFC11-7 (L124–128), RFC11-1, RFC3-16(a)/(b) item 3.
**Analysis — partially blocked:** For an artifact under an owner act, front matter is inside the digest, so the edit destroys the act (RFC3-16(b) item 3) and the artifact renders unadopted with a contradiction minted. **But** that check only fires if something digest-verifies the artifact — and an artifact excluded by tampered metadata is never selected, hence never verified. The failure is self-concealing. The exposure is largest for artifacts *not* under an act (policies pre-approval, declarations, OpenSpec requirements once they exist) and for the generated index: RFC11-7 forbids a *hand-maintained* sidecar and declares indexes rebuildable projections, but **no clause requires the compiler to verify the projection is current and faithful before selecting from it**. A poisoned projection looks complete, so RFC11-6 never triggers.
**Also [Observed]:** RFC11-4's citation "(RFC3-15's contract-index projection)" is **dangling** — RFC3-15 defines the five governance categories and their install gates and says nothing about a contract index or any projection (verified by reading RFC3-15 in full and grepping `rfcs/RFC-0003/` for "index": the only hits are in the package README, which is self-declared "navigational and non-normative"). The authority for the metadata layer is cited to a clause that does not establish it.
**Verdict: GAP — non-blocking but should be closed.** On the prompt's specific question — does RFC3-16(a) close it? Formally the predicate reaches the class, but nothing operationalizes it, and the corpus's own limb-4 instruction says to record that as a finding rather than as settled coverage.

### A8. Sharding as lawful mandatory-context removal
**Path:** A profile declares a small context capacity (RFC11-10). RFC11-11 (L166–176) names sharding as a lawful response to budget pressure. Mandatory context — including the envelope and the VIS-4 always-human class list — is split across shards, so no single run ever holds the full prohibition set.
**Clauses:** RFC11-11, RFC11-5 (L109–112), RFC10-7 ("the VIS-4 always-human classes… appear here as a floor"), RFC-0010 §5 ("the envelope is a mandatory packet input").
**Analysis:** RFC11-11 blesses sharding but sets no integrity condition on it. There is no non-shardable core. [Inferred.]
**Verdict: GAP — non-blocking, easily closed.** Name a non-shardable core (envelope in full, prohibited/human-only surfaces, applicable doctrine rules) that every shard carries.

### A9. Packet as the permission grant rather than a report of it
**Path:** RFC11-1 (L67–82) requires the packet to identify "the **allowed tools and permissions** (deny-by-default, within the envelope)". If any enforcement point reads permissions *from the packet*, then whoever mints packets grants permissions — and the compiler is not an owner act.
**Clauses:** RFC11-1; RFC10-8; RFC3-16(a).
**Analysis:** "within the envelope" is a constraint on the compiler's honesty, not an enforcement rule; nothing states that the packet is never an authorization source. A packet is immutable and digest-bound, which is integrity, not provenance. [Inferred.]
**Verdict: GAP — non-blocking.** State explicitly: the envelope authorizes; the packet *reports* what it was compiled under; enforcement re-derives from the envelope at the choke point.

### A10. Attention flooding and batch resolution
**Path:** RFC10-13 (L222–231) forbids streaming every run event, but bounds nothing about **decision** volume. A fleet generates many individually legitimate attention items; the human bulk-dismisses. "Explicit human dismissal" is one of the three lawful terminations, so the flood is laundered into consent.
**Clauses:** RFC10-12 (L211–220), RFC10-13, RFC-0010 §7 (L319–324) which **defers "attention-queue SLA and batching policy"**.
**Analysis:** RFC10-12 requires each item to carry its choices and each choice's consequence, and makes an authorizing resolution an RFC3-16(a) act (which via RFC3-16(b) items 2–3 would force per-item binding). That is a real partial block. But nothing forbids one act resolving N items, nothing caps item rate per mission, and the anti-rubber-stamp control is precisely what §7 defers. There is a floor for envelopes (RFC10-7) and no analogous floor for attention.
**Verdict: PARTIAL — non-blocking, but this is the "rubber-stamp by construction" surface the prompt names, and it is deferred without a floor.**

### A11. Approval without seeing the effective envelope
**Path:** The owner approves a mission whose authored envelope omits several fields. RFC10-7's narrow reading makes the omissions safe *semantically*, but nothing requires the approval surface to render the **effective** envelope (authored text + narrow-resolved defaults). The owner approves text, not consequences.
**Clauses:** RFC10-7 (L155–157); RFC10-2's extension of RFC6-13/RFC6-14 parity to mission data; RFC3-16(b) item 3 (the act binds the exact digest, so content substitution is blocked).
**Verdict: PARTIAL — non-blocking.** Content integrity is protected; comprehension is not. Recommend an approval-disclosure obligation: the act renders the effective envelope, including "unstated ⇒ no write access / zero delegated spend / lowest autonomy level". [Inferred.]

### A12. Autonomy level unstated, with no vocabulary to be narrow about
**Path:** A mission is approved with no maximum autonomy level. The narrow reading requires "the narrowest", but the level enumeration is explicitly deferred (RFC10-7 L148–151; §8 q2 L331–333), so there is no narrowest value to resolve to. The field is vacuous and the agent self-selects.
**Clauses:** RFC10-7; §8 q2.
**Analysis [Observed]:** `08-OPEN-QUESTION-TRIAGE.md` L45 asserts "Until enumerated, RFC10-7's narrow reading **caps every envelope at propose-only** — safe default". That is the right rule — but it lives in a **non-normative process record**, not in the contract. RFC10-7's text says nothing of the kind.
**Verdict: GAP — non-blocking, one-sentence fix.** Move the propose-only interim floor into RFC10-7.

### A13. Self-unblocking after a violation
**Path:** An agent attempts a self-widening. RFC10-8 transitions the mission to `blocked`, records the attempt as evidence, mints an Attention Item. The agent then "resolves the condition" and the mission takes RFC10-5's `blocked (→ running on unblock)` transition without any human act.
**Clauses:** RFC10-5 (L116–121), RFC10-8 (L167–170), RFC10-13.
**Analysis:** RFC10-5 names the unblock transition with **no actor constraint**. RFC10-11's exhaustion case is self-blocking (resuming would require raising a bound = a human act), but the RFC10-8 violation case has no stated exit gate. Attention-item expiry cannot do it (RFC10-12 forbids expiry from widening or approving), so the flooding path (A10) does not reach it — but a plain "condition cleared" transition is not an attention resolution at all. [Observed clause texts; Inferred gap.]
**Verdict: GAP — non-blocking, sharp.** Require that exit from `blocked` where the block arose under RFC10-8 (or RFC10-11) is a human resolution act.

### A14. Mission-affecting **scopes** as a substitute for the owner act
**Path:** RFC10-3 (L92–97) says "mission-affecting scopes (approve, pause, cancel, envelope change) are distinct scope entries, never implied by read scopes." It does **not** say they may never be issued to a machine credential. RFC5-6 permits scoping a machine credential to "reach adapter-mediated effects", and issuance is owner-attended — so an owner could issue a fleet credential holding `mission.approve` / `mission.envelope-change` once, and the fleet then self-approves thereafter.
**Clauses:** RFC10-3; RFC10-4; RFC10-8 ("Widening is exclusively a human act carrying RFC3-16(a) owner-act provenance"); RFC5-5/5-6 ("never the owner's" identity).
**Analysis — blocked, but only by a second clause.** RFC10-8 and RFC10-4 hold: a machine credential cannot produce an owner act, because the A1 mechanism class is an **owner-attended, Syzygy-mediated ceremony correlated to an external audit trail**. So the scope alone cannot authorize. But RFC10-3's phrasing makes "approve" and "envelope change" look like grantable capabilities, and an implementer reading RFC10-3 in isolation would ship exactly the bypass.
**Verdict: BLOCKED (by RFC10-8/10-4 + RFC3-16(a)), with a legibility defect worth fixing** — say plainly that holding the scope permits *submitting* an act for owner attendance and nothing more.

### A15. Workspace-store entry overriding project-internal truth
**Path:** A workspace-store entry sets a project's requirement priority, or pauses a project into maintenance-only mode, or zeroes its budget.
**Clauses:** RFC10-15 (L241–252); RFC10-1 (L69–76); RFC3-21 (workspace manifest as personal presentation state).
**Analysis — mostly blocked, with an edge contradiction.** The priority-override case is explicitly a violation case (RFC-0010 §4 case 6) and RFC10-15 states the store "must never become authoritative for project-internal doctrine, contracts, specifications, or **behavior**". Store entries that authorize are RFC3-16(a) artifacts — a real control. **But** the same clause's own enumeration of the store's writ includes "per-project budgets" and "project pause/maintenance-only modes", and pausing a project *is* project-internal behavior. The prohibition and the enumeration overlap and no tie-break is stated. [Observed both texts; Inferred the overlap.]
**Verdict: PARTIAL — non-blocking.** Add: the prohibition wins; pause/maintenance-mode means Syzygy **refuses to schedule**, and never mutates project state or project-internal status.

### A16. The store as an authority plane with no home, class, or gate
**Path:** RFC10-15 mints a "typed, platform-level **workspace governance store**" whose home and schema are deferred (§8 q3).
**Clauses:** RFC10-15; RFC3-15 ("the five-category set itself being **closed except by the two lawful widenings this RFC records**"; B19 precedent — "widen explicitly rather than stretch a category's 'exclusively'"); RFC3-2's four write-authority classes.
**Analysis:** A new authorization-bearing store is exactly the widening RFC3-15(a) sets a precedent for, and RFC-0010 defers it rather than following the precedent. No governance category, no write-authority class, no lifecycle, no install gate is assigned. [Inferred.]
**Verdict: GAP — non-blocking (the store cannot ship without §8 q3 closing), but the deferral should be stated as "requires an RFC3-15-style recorded owner widening", not as a schema detail.**

### A17. Mission artifacts homed outside the governance categories
**Path:** RFC10-14 (L235–239) homes the mission record, **envelope**, checkpoints and attention items under `.syzygy/work/missions/<mission-id>/`, "subject to RFC 0003's governance-home discipline".
**Clauses:** RFC10-14; RFC10-9 (envelope is authorization-bearing); RFC3-18 (`intent/`, `work/`, `map/` are **surface namespaces** whose internal contracts belong to RFCs 0007–0009); RFC3-15 (the governance categories, with their install-gate column); RFC3-19.
**Analysis:** `work/` is not a governance home — RFC3-18 classes it as a surface namespace and assigns its internal contracts to RFCs 0007–0009, not 0010. So (i) RFC10-14 defines internal structure of a namespace another clause assigns elsewhere, without amending RFC3-18; and (ii) an authorization-bearing artifact is homed outside the five categories and therefore outside their install gates. RFC3-19's "`.syzygy/work/**` owns approved execution intent" softens (ii) — but RFC3-16 reads effective status from the **act record**, and RFC10-14 never says where the mission-approval act record lives (it should be `governance/decisions/`, binding the envelope digest per RFC3-16(b) item 3).
**Verdict: GAP — non-blocking.** As written, an implementer can treat the in-tree envelope file plus its stamp as the approval — the exact failure RFC3-16's "a tree-resident stamp is never self-authenticating" exists to prevent.

### A18. Completion by weak evidence
**Path:** A mission's completion predicate is a field of the envelope. Nothing bounds its strength. "Evidence: the run log exists" satisfies RFC10-6 literally.
**Clauses:** RFC10-6 (L130–138); RFC2-25 tiers; RFC8-30.
**Analysis:** RFC10-6 correctly forbids work-as-proof, and RFC-0010 §5 imports RFC8-30 — but only for *work-item rendering inside mission views*, not for the mission's own completion. So "mission completed" can rest on `asserted-by-worker` evidence. [Inferred; the RFC2-25 tier vocabulary is [Unknown] to me in full detail — I read it only via RFC6-17's and RFC8-30's citations.]
**Verdict: GAP — non-blocking.** Require the predicate to declare a minimum RFC2-25 tier, and require the completion render to disclose the tier actually achieved (VIS-2).

### A19. Ambiguity resolution has a citation its source does not support
**Path:** RFC10-8 says "not by re-interpreting an ambiguous bound in its own favor (**ambiguity resolves narrow, per RFC10-7**)". RFC10-7 states a rule for fields left **unstated**, not for fields stated ambiguously. [Observed.]
**Verdict: GAP — non-blocking, textual.** Fold the ambiguity rule into RFC10-7 so the citation is true, and add "an ambiguous envelope bound" to RFC10-13's escalation-trigger list — currently ambiguity is self-adjudicated by the agent under a rule that only forbids deciding "in its own favor", which is a self-judged standard.

### A20. Governed-memory promotion as pre-resolved ambiguity
**Path:** A worker promotes a "lesson derived from an incident" — e.g. "the envelope's path grant is understood to include generated files" — into governed memory. It is then **mandatory** context (RFC11-8, L132–140). The agent has not re-interpreted anything in its own favor; the memory did it in advance.
**Clauses:** RFC11-8 ("Promotion from transcript to memory is an explicit, **attributable** act"); RFC-0011 §8 q3 ("default until ruled: propose-only"); RFC10-8.
**Analysis:** "Attributable" is not "owner-act verifiable" — RFC3-16(a)'s whole premise is that a stored attribution field is a claim by whoever wrote the file. A memory artifact that interprets an envelope or a gate satisfies the RFC3-16(a) predicate. The propose-only default is a real mitigation, but it lives in an **open question**, not in clause text, so RFC10-7's narrow-reading discipline does not reach it and it evaporates the moment q3 is answered any other way. [Observed texts; Inferred the interpretation vector.]
**Verdict: PARTIAL — non-blocking.** Move the propose-only default into RFC11-8's clause body, and state that a memory artifact interpreting an envelope, gate, or prohibited surface is authorization-bearing under RFC3-16(a).

### A21. Blocked attacks (recorded so the ACCEPT side is not silent) [Observed]
- **Mission bypassing consent/egress/execution gates:** BLOCKED — RFC10-6's "a mission is authority to *proceed inside* the gates, never authority to skip one", naming RFC5-12/5-14/5-18 explicitly. Clean, and it closes the cross-project-mission write-consent path too.
- **Packet as an egress-consent loophole:** BLOCKED — RFC11-9 states it in terms ("a packet is not a consent loophole").
- **Expiry maturing into authorization:** BLOCKED — RFC10-12's "expiry may narrow, pause, or block, and may never widen an envelope or approve anything", plus §4 case 4.
- **Attention items silently disappearing:** BLOCKED — RFC10-13's three-way termination requirement with attributability. Residual noted at A10 (volume, not disappearance).
- **Attention item resolved by a non-human actor:** BLOCKED for authorizing resolutions — RFC10-12 makes an authorizing resolution an RFC3-16(a) act, which a machine principal cannot produce. Expiry-to-safe-default is a non-human termination but is bounded to narrow/pause/block.
- **Mission Control becoming a second project truth store:** BLOCKED — RFC10-1 plus §4 case 3; projections are rebuildable and non-authoritative.
- **Cross-project mission making one project authoritative over another:** BLOCKED — RFC10-15 first sentence plus §4 case 6.
- **Scraping the UI as an integration:** BLOCKED — RFC10-2 plus §4 case 7.
- **Approving a path and getting different content:** BLOCKED — RFC3-16(b) item 3 ("approving a path never approves future content at that path"), inherited by RFC10-9.
- **Agent acting under the owner's identity:** BLOCKED — RFC5-5/5-6 ("never the owner's").
- **Pinned-input change silently retargeting a running mission:** BLOCKED — RFC10-4's immutability rule plus the escalation-with-re-approval choice.

---

## Part B — The D3 doctrine draft (attack surface 5)

**D1. "every gate the envelope names" is a weakening in one plain reading.** `DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md` L25–26: "The mission grain does not alter what remains human: VIS-4's always-human classes, envelope approval and widening, and **every gate the envelope names**." Read literally, gates the envelope does *not* name are not preserved — the opposite of RFC10-6's "a mission is authority to proceed inside the gates, never authority to skip one." Since doctrine outranks the RFC, this sentence is the one an agent would cite. **Fix: "and every gate that would otherwise apply."** [Observed text; Inferred consequence.] **Exception.**

**D2. Doctrine's inline definition of "autonomy envelope" is narrower than RFC10-7's.** L21–24 enumerates "objective, budgets, risk limits, protected surfaces, stop conditions". RFC10-7's envelope additionally bounds allowed **paths/repositories/projects**, allowed **tools and execution profiles**, **required gates and independent reviews**, **evidence and reconciliation requirements**, **checkpoint/recovery obligations**, and the **completion predicate**. If doctrine must stand alone (VIS-3), doctrine's five-element list becomes the constitutional floor, and the two most load-bearing bounds — permitted write scope and required gates — are absent from it. **Fix: mark the parenthetical explicitly non-exhaustive** ("at minimum objective, permitted change classes and write scope, budgets, risk limits, protected surfaces, required gates, and stop conditions"). [Observed both texts.] **Exception.**

**D3. Is "bounded mission" definable without RFC-0010? Yes — ACCEPT on that question,** subject to D2. The architecture.md insertion is self-contained: it defines the mission grain, the envelope, the no-widening property, and the terminal condition without requiring the reader to hold RFC-0010, and the vision.md insertion cross-references only architecture.md, which is inside doctrine. [Observed.]

**D4. The amendment may be self-licensing under VIS-4 — unaddressed.** The vision.md bullet reads in full: "The loop is human-triggered; autonomy beyond VIS-4's stated bounds is licensed only through the mechanism VIS-4 names, never by reinterpretation." VIS-4's mechanism is **two-part**: an accepted adjudication RFC *and* an explicit owner doctrine amendment — "RFC acceptance alone never opens it." D3 inserts an authorization for repeated agent-driven cycles into that exact bullet, via a doctrine amendment **alone**, with no adjudication RFC. The draft's "What it deliberately does not change" section asserts VIS-4's classes are untouched, but never addresses the prior question: **is a bounded mission "autonomy beyond VIS-4's stated bounds" at all?** If yes, D3 alone is insufficient by VIS-4's own terms. If no (the defensible position — a mission delegates *execution inside gates*, never adoption authority), the draft should say so explicitly and say why, because otherwise the amendment is the "reinterpretation" the sentence forbids, performed inside the sentence that forbids it. **Exception — and this one is squarely the owner's to rule on.** [Observed clause texts; Inferred the licensing question.]

**D5. "Nothing in RFC 0010 or 0011 depends on this amendment being adopted" (L7–9) is true of acceptance and false of operation.** RFC-0010 §2 concedes the point itself: "until the owner rules on it, this contract's reading of human-triggered propagation stands only as far as doctrine already permits." Unamended, `architecture.md` defines the human trigger as "someone specs a desired shape, then deliberately triggers **a propagate/sync pass**" — one pass. A mission authorizing repeated plan/materialize/execute/verify/re-plan cycles is not that. So RFC-0010 can be *accepted* without D3 (it binds nothing doctrine forbids), but **Mission Control cannot lawfully operate**. The draft's framing invites the owner to decline the amendment while believing missions are covered. **Exception — state the operative consequence of non-adoption in both documents.** [Observed both texts; Inferred the consequence.]

**D6. What D3 gets right, and it matters:** "expiry or exhaustion of a mission's envelope halts, never extends, its authority" is the correct doctrine-level statement of RFC10-11, placed where an RFC cannot amend it. The amendment renumbers nothing, retires nothing, and follows the D1 precedent for the amendment log. No objection to the mechanics (L45–50). [Observed.]

---

## Part C — Exceptions, ranked and located

**Blocking (should be resolved before an acceptance act over RFC-0010/0011):**

1. **RFC-0010 L173–178 (RFC10-9)** — pre-A1 mission authorization is undecided between "no mission may run until correlation exists" and "a forgeable bootstrap record suffices". RFC3-16(c)'s final bullet requires the former; RFC10-9 sentence 2 invites the latter; sentence 3 blocks only envelopes with *no* act provenance rather than *no verifiable* provenance. State the operative rule; if a bootstrap carve-out is intended, it is an owner ruling, not a rendering detail (standing boundaries: "no silent autonomy expansion").
2. **RFC-0010 L159–170 (RFC10-8)** — sibling child missions can each be granted the parent's un-debited remaining budget. Define child grants as reservations debited at grant time, with Σ(outstanding child grants) + parent spend ≤ parent budget.
3. **RFC-0010 L104–112 vs L159–170 (RFC10-4 vs RFC10-8)** — whether a child mission requires its own owner act is contradictory. Rule it explicitly.
4. **RFC-0011 L114–122 (RFC11-6)** — blocking on incomplete mandatory context is opt-in, against the corpus's fail-closed posture everywhere else (RFC5-14/5-16, VIS-2, SEC-5). Make complete-context blocking the default, with any relaxation an explicit, owner-visible envelope field.
5. **RFC-0010 L195–199 (RFC10-10)** — "MUST prevent execution outside the approved envelope" is asserted without scoping to Syzygy's choke point, contradicting doctrine's outward non-enforcement and VIS-5's adapter-only reach. Scope it, and disclose the residual honestly.
6. **RFC-0011 L153–162 (RFC11-10)** — profile facts (independence, permissions, risk classes served) satisfy envelope-required gates while being unverified self-assertions in a registry with no home and no write-authority class. Bring gate-satisfying profile fields under RFC3-16(a), or make them evidence-backed.

**Non-blocking, should be recorded:**

7. **`DOCTRINE-AMENDMENT-…-DRAFT.md` L25–26** — "every gate the envelope names" → "every gate that would otherwise apply".
8. **Same, L21–24** — doctrine's envelope definition omits write scope and required gates; mark the enumeration non-exhaustive.
9. **Same, L6–9 + RFC-0010 L56–63** — state that without D3 missions cannot lawfully *operate* (only that RFC-0010 can be accepted), and state whether a bounded mission is "autonomy beyond VIS-4's stated bounds" (VIS-4's mechanism is two-part).
10. **RFC-0010 L155–157 + §8 q2 L331–333** — the propose-only interim floor exists only in the non-normative `08-OPEN-QUESTION-TRIAGE.md` L45. Move it into RFC10-7.
11. **RFC-0010 L116–121 (RFC10-5)** — `blocked → running` has no actor constraint; exit from a block arising under RFC10-8 must be a human resolution act.
12. **RFC-0010 L222–231 + §7 L319–324 (RFC10-13)** — no floor on attention-item volume and no rule against batch resolution; the anti-rubber-stamp control is exactly what §7 defers. Add: one act resolves one item, or enumerates each item identity and choice.
13. **RFC-0010 L235–239 (RFC10-14) and L241–252 (RFC10-15)** — the envelope (authorization-bearing) is homed in a surface namespace RFC3-18 assigns to RFCs 0007–0009, with no stated home for the approval **act record**; and the store's prohibition ("never authoritative for project-internal behavior") overlaps its own enumerated writ (per-project budgets, project pause modes) with no tie-break. Also: the store is a new authority plane owed an RFC3-15-style recorded widening, not just a deferred schema.
14. **RFC-0011 L100–107, L166–176, L67–82, L132–140** — (a) RFC11-4's "(RFC3-15's contract-index projection)" is a **dangling citation**; RFC3-15 establishes no index or projection. (b) No obligation to verify the projection is faithful before selecting from it, so metadata tampering is self-concealing (RFC11-6 never fires). (c) RFC11-11 permits sharding with no non-shardable core. (d) RFC11-1's packet permission list is not declared non-authorizing. (e) RFC11-8's "attributable" promotion is weaker than RFC3-16(a), and the propose-only default lives in §8 q3 rather than clause text.

**Also worth the owner's eye (not exceptions):** RFC10-3's "mission-affecting scopes" phrasing (A14) reads as though `approve` / `envelope change` are grantable machine capabilities; RFC10-8 and RFC3-16(a) do block the bypass, but the clause invites a non-conforming implementation. And RFC10-6's completion predicate (A18) has no minimum evidence tier, so "mission completed" can rest on worker assertion.

**What I could not determine** [Unknown]: whether RFC-0001's identity rules or RFC-0002's contradiction/tier machinery independently close A7 (selection-metadata integrity) or A18 (completion evidence tier). I did not read those contracts in full, and no RFC10/RFC11 clause cites them for those purposes.

---
*Lead note: the reviewer retransmitted this report in full after an idle nudge
("RESEND (identical to msg fce82b91...)"); the resend matched the stored text
verbatim (adds only the "FINAL VERDICT: EXCEPTIONS." closing line).*
