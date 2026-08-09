(part 1/2)

Reviewer: facets (RD-15)
Date: 2026-08-09
Commit: 771965c
Files read (in full): `C/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`; `C/rfcs/RFC-0002/README.md`, `snapshot-and-evaluation-core.md`, `challenge-lifecycle.md`, `reconciliation-chain.md`, `rendering-vocabularies.md`; `C/rfcs/RFC-0008/README.md`, `identity-authority-materialization.md`, `state-vocabulary-and-cost.md`, `accounting-reconciliation-and-release.md`; `.syzygy/governance/doctrine/vision.md`, `trust-and-evidence.md`. Partial (for identity/exclusivity anchors only): `C/rfcs/RFC-0001-project-graph-identity-state-planes.md` (RFC1-5/7/9/10/11/24/25/27/28/31). Sweeps ran over 39 RFC files under `C/rfcs/` (Python `re`, whitespace-normalised); `C/round-2026-08d/`, `C/reviews/`, `C/history/`, `_bootstrap/` were not opened.

Clause denominator for absence claims below: RFC6-1…RFC6-28 (28), RFC2-1…RFC2-26 (26), RFC8-1…RFC8-32 (32) — all 86 read in full.

---

## 1. The outcome facet is single-valued but never made disjoint, and RFC6-7 promises a determinism the clause cannot deliver — major

[Observed] RFC6-5: *"Every selectable reference resolves to exactly one outcome from the **closed outcome set** below, in every surface and every endpoint."* Two of the nine rows overlap on their face:

> | `resolved` | The reference resolves at the evaluation | Full drawer fact set available |
> | `unknown` | The reference resolves but the governing claim renders Unknown | Carry exactly one RFC2-24 reason and its resolution route |

A reference that resolves and whose claims are partly Unknown satisfies both. So do `retired` + `unconsented` (a retired identity whose retirement record sits behind an unconsented source), `resolved-absent` + `excluded`, and `unresolvable` + `incompatible-scenario`.

[Observed] No precedence or disjointness rule exists. Sweep over RFC-0006, whitespace-normalised: `precedence` 0 hits, `mutually exclusive` 0 hits, `disjoint` 0 hits; denominator RFC6-1…RFC6-28, read in full.

[Inferred] This collides with RFC6-7: *"For one (reference, evaluation identity, scenario context), the outcome and fact set are part of the deterministic layer: identical across runs and across surfaces (VIS-7)."* Determinism over a non-disjoint value domain is asserted, not constructible — and RFC6-23 makes the resulting disagreement *"release-blocking under the trust floor."*

**Repair:** add a clause (or a limb of RFC6-5) stating the outcome domain's precedence order over the nine values, or restate the rows as mutually exclusive predicates. Fail-closed ordering (policy states `excluded`/`unconsented` above identity states above `resolved`) is the shape the rest of the corpus uses.

## 2. RFC6-5's `unknown` row forces multi-cause collapse and drops RFC2-24's "primary" — major

[Observed] RFC6-5 `unknown` obligation: *"Carry **exactly one** RFC2-24 reason and its resolution route."* RFC2-24: *"Every Unknown claim instance carries exactly one **primary** reason from this list (**secondary reasons may annotate**)."*

Two distinct defects in one sentence. (a) RFC6-5 says "exactly one reason," not "exactly one primary reason," so read literally it forbids the secondary annotations RFC2-24 opens — and RFC2-24 spends a paragraph closing that secondary vocabulary precisely so it can be carried. (b) The obligation is stated at *reference* level while RFC2-24's is at *claim-instance* level, and RFC6-19 class 2 confirms an entity has several: *"label + tier + Unknown reason … for the entity's **governing claims** at this evaluation."* An entity whose claims are Unknown for `missing-evidence` and `no-currency-bound-declared` has no lawful rendering: one cause must be discarded.

[Inferred] This is VIS-1's failure shape — *"Comprehension is achieved by simplifying presentation, never content"* — arriving through a contract clause rather than an implementation.

**Repair:** amend RFC6-5's `unknown` row to "carry the governing claims' primary reasons with their resolution routes, per RFC2-24 (one primary per claim instance, secondaries as annotation)," and drop the reference-level singular.

## 3. The corpus's flagship V0 output — merged-but-unreconciled — renders "Unknown" with no reason from the closed twelve — major

[Observed] RFC2-19: *"**V0 renders the absence honestly** — merged-but-unreconciled work renders "reconciliation evidence absent / Unknown", and a wall of such Unknowns on a fleet-built project is correct output, not a defect."* RFC8-29 repeats it verbatim.

[Observed] No clause binds that Unknown to a reason. Sweep: each of the twelve RFC2-24 reason tokens, over 39 RFC files, with a ±160-char context filter for `reconcil|merged|pending` — the only hits are reason #8 attached to `contradiction-raised` (RFC2-18, RFC2-15) and to orphaned work (RFC8-8). Nothing attaches a reason to `reconciliation-pending`. RFC8-24, which exists to enumerate *"the RFC2-24 reasons Trajectory most renders on its claims,"* lists five and none of them covers "the evaluation that would decide this is deliberately not computed at this stage": #2 `missing-evidence` is defined as *"Declaration exists; no current evidence artifact for the claim,"* which misdescribes a verdict that was never sought.

[Inferred] The hole cannot be filled downstream: RFC2-24 forbids it — *"no implementation may mint, spell, or force-fit a value the list does not carry … the honest move is to amend this list, never to annotate outside it."* And RFC2-24 does not carry an exemption for this state, though the corpus knows how to write one: RFC8-12 exempts the four normalized-state absence values explicitly (*"never stamped with, counted among, or absorbed by an aggregate of RFC2-24 Unknown reasons (RFC6-6)"*). The single most-rendered condition at V0 gets neither a reason nor an exemption.

**Repair:** either amend RFC2-24 with a thirteenth reason for the uncomputed reconciliation evaluation (owner decision A5 closed the list at twelve, so this is an owner act, not an editorial one), or add a clause exempting `reconciliation-pending` from RFC2-24 the way RFC8-12 exempts its absence values — and say which, because "Unknown" with neither is unimplementable.

## 4. Three facets are declared parity-checkable by their owning clauses and are absent from RFC6-22/23 and RFC6-17 — major

[Observed] Sweep over RFC-0006, whitespace-normalised, denominator RFC6-1…RFC6-28: `challenge-pending` 3 hits — RFC6-14 and RFC6-19 item 6 (×2); `chain state` 1 hit — RFC6-19 item 8; `normalized work state` 1 hit — RFC6-19 item 8. Zero hits in RFC6-17, RFC6-22, RFC6-23.

RFC6-22 fixes the tuple: *"the same epistemic states (label + tier + reason + freshness), the same sibling surface states (dismissed-by-decision, unadopted-draft, editorial-draft — RFC6-14), and the same scenario context."* RFC6-23 lists what no pair may disagree on: *"an entity's existence, an edge, a label, a tier, a reason, a freshness state, a sibling surface state, a scenario context, or a count over the same declared scope."* RFC6-17 defines aggregate disclosure as *"the full RFC6-22 equivalence tuple."*

[Observed] Three owning clauses assert coverage that these enumerations do not provide:
- RFC2-13 §5: *"**Provides to RFC 0006 and the surface RFCs:** `challenge-pending` as a named rendered state — queryable under RFC6-13, carried verbatim in machine answers under RFC6-14, and **parity-checkable under RFC6-22/23**."* RFC6-14 does carry it; RFC6-22/23 do not check it. And RFC2-13 itself rules it out of every category RFC6-22 does name: *"**not** the `suspended` tier … **not** an RFC2-24 Unknown reason … **not a sibling surface state**."*
- RFC8-12: closure of the normalized state is justified because *"a value the contract never names can be neither carried verbatim on a machine answer (RFC6-14) nor checked for parity, and **RFC6-22/23 make the resulting disagreement release-blocking**."* The normalized state is not in RFC6-22's tuple.
- RFC-0008 README §6 makes the identical argument for naming `closed-unmerged`.

[Inferred] Consequence: a table and a scene may disagree on an item's chain state, or on whether a claim carries a pending challenge, without triggering the release-blocking rule the corpus relies on three times. RFC6-18 catches it per-selection (*"two surfaces showing different evidence for one selection at one evaluation is a **kernel defect**"*), but RFC6-22/23 govern multi-element renderings, which is where boards and scenes live.

**Repair:** extend RFC6-22's tuple and RFC6-23's disagreement list with `challenge-pending`, the normalized work state, and the chain state; and extend RFC6-17's disclosed composition correspondingly — RFC2-24's rendering rule says *"the disclosure any aggregate owes is **RFC6-17's in full**,"* so an aggregate today can satisfy the stated obligation in full while disclosing nothing about reconciliation.

## 5. The chain-state vocabulary is cited as closed and is never closed — major

[Observed] RFC8-12: *"The **RFC2-18 chain state** (`merged`, `reconciliation-pending`, `reconciled@E`, `unsatisfied`, `contradiction-raised`, `Unknown(reason)`) is a **separate field with its own closed vocabulary (RFC8-28)**."*

[Observed] RFC8-28 does not close it: *"The RFC2-18 chain states — `merged`, `reconciliation-pending`, `reconciled@E`, `unsatisfied`, `contradiction-raised`, `Unknown(reason)` — are **first-class Trajectory states**, queryable and filterable on the durable identity."* Sweep of `closed` in `accounting-reconciliation-and-release.md`: 11 occurrences — `fail-closed` (×4), `warrant classes are closed` (×2), `closed navigation-outcome set` (×2), `closed` work item (×2), `closure fallacy`. None closes the chain list. RFC2-18 states the vocabulary as a transition expression, not a closed enum, and never uses the word.

[Inferred] This is verification rule 8's exact failure: a property attributed to a clause that the clause does not carry. It matters because the chain state is the one facet carrying the reconciliation truth, and it is simultaneously outside RFC6-22/23 (finding 4) — the least protected of the load-bearing facets.

**Repair:** state the closure in RFC8-28 in RFC8-12's own form ("six values, closed; no implementation may mint, spell, or force-fit one"), or correct RFC8-12's citation.

## 6. Two parity-carried vocabularies are closed only in non-normative prose — major

[Observed] **Freshness (RFC2-10):** *"Logical freshness state — `fresh`, `stale`, `broken`, `superseded` — changes status and therefore participates in the VIS-7 identity test."* No closure declaration. Sweep of `closed` in `snapshot-and-evaluation-core.md`: 3 occurrences, all "the closed snapshot rule" / "The closed rule" (RFC2-1). Yet freshness is carried verbatim on every machine answer (RFC6-14), counted per-value in every aggregate (RFC6-17: *"per-freshness-state counts"*), and made release-blocking on disagreement (RFC6-23).

[Observed] **Degradation states (RFC2-23):** the clause is headed *"RFC2-23 — Each with its rendering obligation"* and closes nothing. The only closure claim is in the module's §0 reader map — *"This module owns **the three closed vocabularies every surface renders**: the degradation states…"* — which is explicitly subordinate: *"If this section and a clause disagree, the clause wins."* RFC-0002 README §5 hands these states to a consumer that will map onto them: *"**Provides to RFC 0004:** … the degradation states RFC4-2 item 6 maps its internal errors onto."*

[Inferred] RFC2-24 gives the argument for its own closure — *"RFC6-14 requires every machine answer to carry its Unknown reason **verbatim** … and leaving it unstated is how the value gets chosen by whoever implements the render first"* — and that argument transfers verbatim to freshness. Among the facets RFC6-14/17/22 carry, label (RFC2-25, *"exclusive and exhaustive"*), tier (*"Six tiers, closed"*), Unknown reason (*"Twelve reasons, closed"*), sibling surface states (*"three sibling surface states, closed"*) and navigation outcome (*"closed outcome set"*) are closed by clause; freshness and degradation state are not. Scenario context (RFC6-24) enumerates three contexts without the word "closed" — the weakest case of the three, since the clause is definitional, but it is the same omission.

**Repair:** add "closed at four values" to RFC2-10 and a closure sentence to RFC2-23, in the form RFC2-24/25 already use.

## 7. `reconciled` sits inside a facet that disclaims claim status, tier, and observation-record membership — major

[Observed] RFC8-12: the normalized state *"is not a Claim (RFC1-24; RFC2-5) … a derived rendering of scheduler and repository facts, not a status claim about a capability, so it carries **no RFC2-5 two-level claim identity, no RFC2-25 tier, and no membership in the observation record** (RFC2-6)."*

[Observed] RFC8-13's row for one of its eight live values contradicts the premise:

> | `reconciled` | `reconciled@E` per RFC2-18 | **A reconciliation verdict claim, gate-backed Observed (RFC2-25)**, rendered with its evaluation identity | V0: never renders … |

So seven live values derive from scheduler and repository facts and one derives from a status claim — the one value in the enum that is green-capable. RFC2-18 confirms its class: *"`reconciled@E`: … a **positive status claim requiring gate-backed Observed evidence** (RFC2-25)."* Carried in the normalized-state field it arrives stripped of the tier RFC2-25 makes the sole licence for a positive claim, and outside the observation record RFC2-6 makes immutable.

[Inferred] This is the mixed value domain the facet model otherwise avoids: staging (`future`, `planned`, `ready`) and evidence (`reconciled`) in one enum, with the enum's own clause disclaiming the guardrails the evidence value needs. It is also why the two "orthogonal" fields are not disjoint — `merged` and `reconciled` are members of both vocabularies. RFC8-13's "V0: never renders" defers the exposure to V1 rather than removing it.

**Repair:** drop `reconciled` from the normalized vocabulary (twelve values, chain state carries `reconciled@E`), or carve it out of RFC8-12's non-Claim rule with an explicit statement that this one value carries its verdict claim's tier and evaluation identity.

(continued in part 2/2)

(part 2/2)

## 8. Dismissal replaces a status rendering, and no clause gives it RFC2-14's basis-visibility guarantee — minor

[Observed] RFC2-25 classes the sibling states by what they do to the rendering: *"the three sibling surface states **replace** a status rendering, while `challenge-pending` **accompanies** one"* (RFC2-13, same distinction). For challenge suspension the corpus then protects the underlying facts explicitly — RFC2-14: *"**Suspension is not erasure.** A suspended claim's deterministic basis stays visible for the entire lifecycle."* There is no counterpart for dismissal. Sweep across RFC2-1…RFC2-26 and RFC6-1…RFC6-28: the dismissal obligations are reason + expiry + never-green (RFC2-15, RFC6-19 class 5), never basis-visibility.

[Inferred] The facts survive in the drawer (RFC6-19 classes 2 and 5, RFC6-18's one fact set) and dismissed items are counted separately in aggregates (RFC6-17's sibling-state counts), so this does not breach VIS-6 — doctrine does license suppression: *"It may **suppress** a gap, rendered as *dismissed by human decision* — never as resolved, aligned, or green."* The residual asymmetry is that a human ruling may displace an Unknown on the primary surface where an inferred challenge may not.

**Repair:** state, in RFC2-15 or RFC6-19 class 5, that the dismissed gap's status and reason remain visible alongside the dismissal on the primary surface, matching RFC2-14's shape.

## 9. `blocked` carries one cause where a work item can genuinely have several — minor

[Observed] RFC8-17: *"`blocked` carries **a cause** from the **closed taxonomy** {`dependency`, `pr-wait`, `external`, `decision`} … Where the substrate conflates causes and **no declared derivation resolves one**, the item renders **blocked with cause Unknown**."*

[Inferred] The absence path covers zero resolved causes; nothing covers two. An item with an unmet dependency edge *and* an open PR awaiting review satisfies two declared derivations, and the clause offers no multi-valued render — so an implementation picks, and the owner clears the wrong blocker. RFC8-18's *"blocked time (split by RFC8-17 cause where history supports it)"* inherits the same single-valued assumption.

**Repair:** make the cause a set drawn from the closed taxonomy ("all causes whose declared derivation resolves"), with cause-Unknown reserved for the empty set.

## 10. A selectable entity may have no URL form — minor

[Observed] RFC6-2 scopes selectability to *"every entity of an extension profile loaded for the project **or workspace** (RFC1-7 — the mission profile's Mission and Attention Item included)."* RFC1-7 puts *"cross-project relationship entities"* in the portfolio profile. RFC6-8 pins *"(**project identity**, selection reference …)"*, and §7 defers *"cross-project selection, and workspace-level URLs → portfolio profile (SDR-29/30)."*

[Inferred] A workspace-loaded entity is therefore selectable under RFC6-2 with no defined URL under RFC6-8, while RFC6-12 requires *"Every URL-pinned selection is openable in any surface"* and VIS-7's link rule requires every rendered internal project-entity link to resolve.

**Repair:** state in RFC6-2 that selectability of workspace-scoped entities is deferred with the portfolio profile, or give RFC6-8 a workspace-identity limb.

## 11. An aggregate's own "epistemic state" is undefined — minor

[Observed] RFC6-14: *"Every entity, claim instance, **and aggregate** in a machine answer carries its epistemic state verbatim from the RFC 0002 vocabulary: the label …, the rendering tier (RFC2-25), the Unknown reason where applicable (RFC2-24), and the freshness state (RFC2-10)."* RFC 0002 defines none of these for aggregates: RFC2-25 — *"A tier qualifies how **a claim** renders"*; RFC2-24 — *"Every Unknown **claim instance** carries exactly one primary reason."*

[Inferred] Read literally the clause licenses a headline label over mixed membership — VIS-1's named violation, *"rendering that region green because its neighbors are green."* RFC6-17's composition requirement makes the honest form mandatory *in addition*, and RFC6-14 bars only the *silent* fold, so a headline "Observed" atop a disclosed 12-Unknown composition is not excluded by text.

**Repair:** say in RFC6-14 that an aggregate carries its members' composition per RFC6-17 and no aggregate-level label, tier, or reason.

---

## Against the seven review questions

1. **Value domains.** Closed and typed for label, tier, Unknown reason, sibling surface states, navigation outcome, normalized work state, blocked cause. Not closed: freshness, degradation states (finding 6), chain state (finding 5). Mixed domain: the normalized work state (finding 7). The navigation-outcome set mixes fact and policy values (`excluded`, `unconsented`) but does so deliberately and with fail-closed rendering obligations — that is sound; its defect is non-disjointness (finding 1).
2. **Evidence versus decisions.** [Observed] No path found by which a dismissal, waiver, or ruling turns an observed value green. RFC2-15 (*"never green, resolved, or aligned"*), RFC2-25 (`gate-backed` is *"the **only** tier that may support a positive status claim"*), RFC6-19 class 5 and RFC2-13's provider-revocation rule hold the line, and dismissals carry reason + expiry with RFC2-15's re-opening rule. One asymmetry, finding 8.
3. **Scope.** Well handled: RFC6-16 (filters are declared scope), RFC6-17 (membership count and expansion to members), RFC6-22 ("same declared scope"), RFC2-16/2-21 (declared target scope), RFC6-5's explicit statement that `not-applicable` is *"Legitimate **per surface only**, never for the kernel, a URL, or an endpoint."* One hole, finding 10. No facet found silently aggregating across projects.
4. **Multiple causes.** Preserved in the strong places — RFC6-19 item 6 (*"every open challenge … The lifecycle state travels, never flattened"*), RFC2-18's paired warranted/current-revision state, RFC2-17's word reservation. Collapsed in two: findings 2 and 9.
5. **Staging versus health.** Separated by construction — RFC8-1's plane discipline, RFC6-19 class 1 (lifecycle) versus class 2 (epistemic state), RFC8-30's closure-fallacy prohibition, and the non-deferring layout obligation in RFC-0008 README §7 that keeps the terminal and absence values *"off the ladder, not at the end of it."* "Planned" cannot read as healthy. The one leak is `reconciled` inside the staging enum (finding 7).
6. **Anti-rollup.** RFC6-19 item 8 is correct and explicit — *"carried as two fields, never folded, and never rendered as proof of satisfaction (work is never proof); … uncomputed reconciliation renders Unknown, never green"* — and RFC8-28/8-30 back it inside Trajectory. The guarantee is complete only where a rendering carries the normalized state; RFC6-17's disclosure tuple, which RFC2-24 calls the aggregate's obligation *"in full,"* names neither field (finding 4). And the Unknown that item 8 mandates has no reason to carry (finding 3).
7. **Same-facts rule.** [Observed] Yes, and by clause. RFC6-18 computes *"**one fact set**, consumed by every surface and by the endpoints … they may **not** differ in which facts, labels, or provenance exist,"* RFC6-13 states the obligation bidirectionally, RFC6-21 stops minimal display from subsetting it, and RFC6-19 enumerates eight content classes rather than examples. Two small softnesses: RFC6-19 says the set *"contains"* the eight classes (a floor, which is fine given one kernel computes it), and class 1's *"lifecycle state (**including** unadopted draft and retired with successors)"* enumerates by instance. Neither is a defect; the guarantee holds.

## Assessment

The facet model is the strongest part of what I read: the three-label rule, six tiers, twelve reasons, nine outcomes and thirteen work-state values are genuinely closed, genuinely typed, and defended by clause-level reasoning about why closure is required rather than by assertion. The anti-rollup construction in RFC6-19 item 8 and the two-field handoff in RFC-0008 §5 are the right shape.

The defects cluster in one place: the seams between vocabularies. RFC-0002 and RFC-0008 each cite RFC6-14/17/22/23 as the enforcement that justifies their design, and RFC-0006's enforcement clauses were not extended to match — `challenge-pending`, the normalized work state, and the chain state are all named upstream as parity-checkable and are absent from the tuple that checks parity. The uncomputed-reconciliation Unknown carries no reason from a list its own contract forbids extending downstream. These are clause-text repairs, not structural ones; none of them is defensible as a knowingly-bound imperfection, because RFC2-24's closed list can only be repaired by amending RFC-0002, and an act that binds these digests makes that repair a re-acceptance rather than an edit.

VERDICT: REVISE
