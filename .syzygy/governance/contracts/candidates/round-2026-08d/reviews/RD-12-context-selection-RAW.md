(part 1/2)

# Reviewer: context-selection (RD-12) / Date: 2026-08-09 / Commit: 771965c

**Files read.** `C/rfcs/RFC-0011/deterministic-selection-and-budget.md`; `C/rfcs/RFC-0011/README.md`; front matter of all 39 files under `C/rfcs/`; `C/05-CONTRACT-INDEX.yaml`; the ten `C/fixtures/context-selection-*.md` (fixtures 2, 5, 10 under the blind protocol); `C/TASK-TO-CONTRACT-INDEX.md`; defining clause text for RFC8-12, RFC8-10, RFC7-3, RFC5-3, RFC3-16(a), RFC10-4, RFC10-9, RFC10-17; `.syzygy/governance/doctrine/` heads; `C/scripts/build_budget_report.py` (run), `scripts/check_governance.py` (run). Not read, per instruction: `C/round-2026-08d/`, `C/reviews/`, `C/history/`, `_bootstrap/`.

**Method note.** Mutation tests were run against a *copy* of the clone in my own scratchpad; the clone at `clone-771965c` was not written to. All sweeps used Python `re`, never system grep.

---

## Blind derivation 1 — fixture 2 (Trajectory work-provider adapter)

I read lines 1–17 (the `## Task` block and the `---` rule), stopped, and derived the following before reading line 18 onward.

**My derived selection.** Seed (RFC11-14 rule 1) from the warrant's named clause RFC8-12 → `RFC-0008/state-vocabulary-and-cost.md` + README; the adapter → `RFC-0004/general-contract.md` + `named-adapters.md` + README; the declared risk class (RFC3-16(a)) → `RFC-0003/governance-homes-and-owner-acts.md` + README. Rule 2 then leaves open edges to RFC-0001, RFC-0002, RFC-0005, RFC-0006 and (via the RFC-0008 README) RFC-0007; I resolved RFC-0002 by loading `snapshot-and-evaluation-core.md` (currency/derivation) and left RFC-0001, RFC-0005, RFC-0006, RFC-0007 open with their cited clause identities enumerated. Rule 4/RFC11-16: `RFC-0007/narrative-contract.md` declares `constrains: [RFC-0001, RFC-0002, RFC-0004, RFC-0008]`, `constrains_source: RFC7-3`; RFC-0004 and RFC-0008 are selected, so I entered **RFC7-3 as a constraining clause**. Doctrine: `vision.md` (VIS-4 owner acts, VIS-2), with an explicit RFC11-15 statement that the doctrine limb is not claimed deterministic. Boundary rule: declarations only (off-seam).

**Recorded selection.** `RFC-0004/{README, general-contract, named-adapters}`, `RFC-0008/{README, state-vocabulary-and-cost}`, `RFC-0003/{README, governance-homes-and-owner-acts}`, `doctrine:security.md`.

**Divergences.**

| # | Divergence | Fault |
|---|---|---|
| 2a | I entered **RFC7-3** under rule 4/RFC11-16; the recorded answer neither loads it nor mentions the `constrains` edge anywhere | **Shared** — the recorded answer never dispositions a declared relation (F1); the policy never says whether a contract-level `constrains` list is a "declared seam" (F9) |
| 2b | I enumerated cited clause identities for the open RFC-0001/0002/0006/0007 edges; the recorded answer disposes of all four in one line, by a different test — *"not cited by the warrant's clause set"* | **Recorded answer** (F2). Measured: the loaded modules cite 13 distinct RFC1-n, 20 RFC2-n, 6 RFC6-n, 4 RFC7-n identities — 43 in total, 0 enumerated |
| 2c | I loaded `RFC-0002/snapshot-and-evaluation-core.md`; the recorded answer leaves the RFC-0002 edge open | **Policy** (F7) — rule 2 makes both conforming |
| 2d | I derived `vision.md`; the recorded answer derives `security.md` (SEC-3) | **Policy** (F5) — no RFC11-15 ownership metadata exists, so neither derivation is deterministic; the fault becomes the recorded answer's only because it prints its doctrine file under a heading reading *"mandatory, deterministic"* with no RFC11-15 basis statement |

Agreement on the RFC-0004/RFC-0008/RFC-0003 module set and on the off-seam boundary disposition was exact.

## Blind derivation 2 — fixture 5 (cross-project Mission)

Read lines 1–16, stopped, derived, then read on.

**My derived selection.** All five RFC-0010 modules + README (identity/lifecycle for RFC10-4, envelope for RFC10-9, budgets for RFC10-17, stop/effects, portfolio/cross-project consent) — the warrant names a part of the artifact defined by each. `RFC-0003/governance-homes-and-owner-acts.md` + README for RFC3-16(a). `RFC-0005/consent-egress-secrets.md` for the two-project consent/egress plane, **plus RFC5-3** under rule 4/RFC11-16 (`RFC-0005/admission-and-boundary.md` declares `constrains: [RFC-0006, RFC-0009, RFC-0010, RFC-0011]`, source RFC5-3, and RFC-0010 is selected). Doctrine: `vision.md` (VIS-4) **and** `security.md` (SEC-2, SEC-4 — per-repository consent is the doctrine a two-project mission can violate), with the RFC11-15 basis stated. Open edges to RFC-0001, RFC-0002, RFC-0004, RFC-0006, RFC-0008 enumerated clause-by-clause. I did **not** derive RFC-0011.

**Recorded selection.** All five RFC-0010 modules + README; `RFC-0011/{README, packet-identity-provenance-and-memory}`; `RFC-0003/{README, governance-homes-and-owner-acts}`; `doctrine:vision.md`.

**Divergences.**

| # | Divergence | Fault |
|---|---|---|
| 5a | Recorded loads **RFC-0011 (two files)**; no RFC11-14 rule produces it. Sweep: **0 of 39** RFC files list RFC-0011 in `depends_on` — it is a sink. The fixture's own omission bullet claims *"the RFC-0011 dependency edge is satisfied by the loaded packet module (RFC11-14 rule 2)"* | **Recorded answer**, with a policy gap behind it: rule 2 covers outbound edges only, and RFC11-14 has no inbound-edge rule (F3) |
| 5b | I entered **RFC5-3**; recorded omits RFC-0005 entirely and never mentions the `constrains` edge that names RFC-0010 and RFC-0011 — both selected here | **Shared** (F1, F9) |
| 5c | I loaded `RFC-0005/consent-egress-secrets.md`; recorded omits it | **Policy** (F7) — conforming either way |
| 5d | I loaded `security.md`; recorded neither loads nor names it. Sweep: fixture 5 mentions 1 of the 5 substantive doctrine files | **Recorded answer** (F6) — rule 7 requires every excluded applicable candidate in the register |
| 5e | I enumerated cited clauses on six open edges (RFC-0001: 3, RFC-0002: 9, RFC-0004: 9, RFC-0005: 12, RFC-0006: 3, RFC-0008: 8 — 44 identities); recorded enumerates 0 | **Recorded answer** (F2) |

## Blind derivation 3 — fixture 10 (Trajectory work lifecycle)

Read lines 1–30, stopped, derived, then read on.

**My derived selection.** RFC-0008 all three modules + README (RFC8-9/10/11 identity and the one-way door; RFC8-12..20 for dispatch and terminal states; RFC8-21..32 for accounting and release). RFC-0010: `budget-reservation.md` **and `effects-recovery-and-stop.md`** — the warrant's word *"recovered"* points at `recovery_reserve`, which RFC10-17 defines only by reference: *"held undispatchable so that **RFC10-19's** compensating actions are fundable after an RFC10-11 exhaustion"*, and RFC10-19 lives in `effects-recovery-and-stop.md`. `RFC-0001` in full (work identity, single file). `RFC-0004/execution-record.md` (run envelope). `RFC-0002/rendering-vocabularies.md` + README. **RFC7-3 and RFC5-3** under rule 4/RFC11-16 (RFC-0004/RFC-0008 are RFC7-3 targets; RFC-0010 is an RFC5-3 target). Doctrine `vision.md`. I expected the closure to blow the budget and require sharding.

**Recorded selection.** RFC-0001; RFC-0008 README + all three modules; RFC-0010 README + `budget-reservation`; RFC-0002 README + `rendering-vocabularies`; `RFC-0004/execution-record` (no index); RFC-0006 (single file); `doctrine:vision.md`.

**Divergences.**

| # | Divergence | Fault |
|---|---|---|
| 10a | I loaded `RFC-0010/effects-recovery-and-stop.md`; recorded omits it | **Policy** (F7) — rule 2 closes the RFC-0010 edge on any one module, and nothing selects *which* |
| 10b | Recorded loads **RFC-0006 in full**; I left that edge open with enumeration | **Policy** (F7) — both conforming |
| 10c | I entered **RFC7-3 and RFC5-3**; recorded's open-edge table names RFC7-24, RFC7-20, RFC7-38, RFC5-21/15/18 — never RFC7-3 or RFC5-3, and never the `constrains` relation | **Shared** (F1) |
| 10d | Recorded selects RFC-0004 without its index and records the declaration *"read at the index bytes the packet digest below was stamped against"* — but the packet digest is *"sha256 over the mandatory files"*, and `RFC-0004/README.md` is not among them | **Recorded answer** (F4) |

Fixture 10 is otherwise the best specimen in the set: its rule-2 table enumerates eight cited clause identities with promotion triggers, its doctrine register names all six doctrine files, and its verification checklist leaves *"Selection produced deterministically"* **unchecked** with the reason *"false by construction. No selector exists."* That honesty is the correct posture and should not be edited away.

(part 2/2)

---

## Findings

**1. [blocking] RFC11-16 is exercised by 0 of 10 fixtures, and every live `constrains` declaration in the corpus is silently ignored by fixtures that select its targets.**
Anchor — RFC11-14 rule 4: *"**Constraints.** Load a `constrains` source clause when the task touches the declared seam (RFC11-16)."* RFC11-16: *"Where a selected clause, module, or the task's declared seam is the target of a clause-anchored `constrains` relation, the mandatory set includes the **constraining clause** — not automatically the entire constraining contract… The packet records why each constraint entered."*
Sweep (denominator 39 RFC files): exactly 2 declare `constrains` — `RFC-0005/admission-and-boundary.md` → `[RFC-0006, RFC-0009, RFC-0010, RFC-0011]`, `constrains_source: RFC5-3`; `RFC-0007/narrative-contract.md` → `[RFC-0001, RFC-0002, RFC-0004, RFC-0008]`, `constrains_source: RFC7-3`. Sweep (denominator 10 fixtures): **0** contain the string `constrains`, **0** contain `RFC11-16`, **0** contain `RFC5-3`. Fixture 2 selects two RFC7-3 targets, fixture 5 selects two RFC5-3 targets, fixture 10 selects three targets across both — and none loads the constraining clause or records why it did not enter. RFC-0011 module 2 §1 makes reproduction of these fixtures the acceptance test; a clause with zero coverage and three live counterexamples cannot ride through on it.
Repair — either add the constraint disposition to fixtures 1, 2, 5, 9 and 10 (whichever select a declared target), or, if the intended reading is that a contract-level target list is not a "declared seam", say so in RFC11-16's text and have one fixture demonstrate the negative disposition. Do not leave the clause untested either way.

**2. [major] Rule 2's individual-enumeration duty is discharged by 2 of 10 fixtures; fixtures 2 and 5 substitute a bulk dismissal under a different test.**
Anchor — RFC11-14 rule 2: *"An edge is **satisfied by loading at least one module of the depended-on contract; where an edge is left unsatisfied, the clause identities the loaded modules cite from the depended-on contract are enumerated and disposed of individually in the omission register.**"*
Fixture 2's register reads *"RFC-0001/0002/0006/0007/0009/0010/0011, craft — not cited by the warrant's clause set"* — one line for four open edges, and the test it applies (cited by the **warrant**) is not the test rule 2 states (cited by the **loaded modules**). Measured over the seven loaded files: 13 distinct RFC1-n, 20 RFC2-n, 6 RFC6-n, 4 RFC7-n identities are cited; 0 are enumerated. Fixture 5 is the same shape over six open edges, 44 cited identities, 0 enumerated. Fixtures 9 and 10 do it correctly, as tables. Fault: the recorded answers — the rule is clear and two siblings obey it.
Repair — give fixtures 2 and 5 the clause table fixtures 9 and 10 carry, or close the edges.

**3. [major] Fixture 5 mandatory-loads RFC-0011 under a dependency edge that does not exist, and cites rule 2 for it.**
Anchor — RFC11-14 rule 2 (quoted above) and rule 3: *"**No silent transitivity.** Traverse beyond direct edges only where an edge is explicitly marked transitive."*
Sweep (denominator 39): **0** files list `RFC-0011` in `depends_on`. RFC-0011 depends on RFC-0010, not the reverse. Fixture 5's omission register nonetheless states *"the RFC-0011 dependency edge is satisfied by the loaded packet module (RFC11-14 rule 2)"*. The inclusion may be right on the merits — a mission envelope does pin the packet duties its runs inherit — but no rule in RFC11-14 produces it, so it is not deterministic, and it adds two files to a fixture already disclosing a budget exception. Behind the mis-citation is a policy gap: RFC11-14 defines outbound traversal only and says nothing about a contract that depends *on* the seam being edited.
Repair — either state an inbound-edge rule in RFC11-14 and re-derive, or drop RFC-0011 to the suggested set. Delete the false rule-2 citation either way.

**4. [major] RFC11-4's index-digest duty is unmet by 2 of 2 fixtures that exercise it.**
Anchor — RFC11-4: *"A packet that selects a contract without loading its index **records the declaration verbatim together with the digest of the index it was read from**."*
Sweep (denominator 10): two fixtures select a contract index-lessly — fixture 9 (RFC-0005, RFC-0003) and fixture 10 (RFC-0004). Both record the declaration verbatim and both bind it with the identical phrase *"read at the index bytes the packet digest below was stamped against."* Each fixture defines that digest as *"sha256 over the mandatory files concatenated in listed order"*, and `RFC-0005/README.md`, `RFC-0003/README.md`, `RFC-0004/README.md` are not mandatory files. The packet digest therefore cannot bind those bytes, and no index digest is recorded. The clause's whole point — that a later index edit invalidates the recorded declaration — is unserved.
Repair — record each index file's own sha256 in the applied-rule paragraph, machine-written by `build_budget_report.py` and covered by CG-18. It must not be transcribed.

**5. [major] RFC11-15's basis statement is absent from 6 of 10 fixtures, and fixtures 6 and 9 make contradictory claims about the same metadata.**
Anchor — RFC11-15: *"Where a task class or risk class has no declared ownership metadata, doctrine/craft selection for it is **not claimed deterministic**, and the packet states that basis rather than implying a derivation that did not happen."*
Sweeps: 10/10 fixtures load at least one doctrine file inside a section headed **"Required context (mandatory, deterministic)"**; 4/10 mention RFC11-15; 1/10 (fixture 9) says *"not claimed deterministic"*. Fixtures 2, 5 and 10 — my three blind subjects — say nothing. The metadata itself does not exist: **0 of 39** RFC files carry `task_classes` or `risk_classes` front matter, and `05-CONTRACT-INDEX.yaml`'s `governance_sources` rows carry only `file`, `role`, `words`, `rule_ids`. Fixture 6 asserts *"Doctrine ownership metadata is declared in the contract index's `governance_sources`"*; fixture 9 states accurately that those rows *"carry no clause rows, no `governs`, no `applies_to`, and their `rule_ids` are a mention scan."* Fixture 9 is right and fixture 6's sentence is false against the artifact it names.
Repair — correct fixture 6's sentence to fixture 9's; add the RFC11-15 basis line to every fixture that loads doctrine or craft; and answer, at owner level, whether RFC11-15's metadata is to be authored at V0 or the clause's escape hatch is the permanent posture.

**6. [major] Rule 7 is applied to doctrine by 5 of 10 fixtures; fixture 5 omits the doctrine file its own task class most implicates.**
Anchor — RFC11-14 rule 7: *"**Omissions are enumerated.** Every excluded applicable candidate is recorded in the packet's omission register with its reason."*
Sweep, denominator 5 substantive doctrine files (`architecture.md`, `security.md`, `trust-and-evidence.md`, `v1.md`, `vision.md`): fixtures 6, 7, 8, 9, 10 name or load 5/5. Fixtures 1 (2/5), 3 (2/5), 2 (1/5), 4 (1/5), 5 (1/5) leave three or four entirely unmentioned. Fixture 5 is the sharpest case: its task is a **cross-project** mission whose module 5 is tagged `[portfolio, consent, egress, fail-closed]`, and `security.md` — which holds SEC-2 and SEC-4, the per-repository consent rule — appears nowhere in the fixture, neither loaded nor omitted.
Repair — extend the doctrine register of fixtures 1–5 to the full denominator, as fixtures 6–10 already do.

**7. [major] Rule 2 is defined at contract granularity, so two conforming selectors produce different packets — and did, on two of my three derivations.**
Anchor — RFC11-14 rule 2: *"An edge is **satisfied by loading at least one module of the depended-on contract**"*; against RFC11-4: *"**Mandatory context is selected deterministically** — same inputs, same selection."*
Nothing selects *which* module satisfies an edge. Divergences 2c, 5c, 10a and 10b are all this one gap: I chose `RFC-0002/snapshot-and-evaluation-core`, `RFC-0005/consent-egress-secrets` and `RFC-0010/effects-recovery-and-stop` where the recorded answers chose otherwise, and every one of those choices conforms. Packets are measured, digested and budget-tested at module granularity, so "same inputs, same selection" is false exactly where it is checked.
Repair — add a module-selection predicate to rule 2: the satisfying module is the one whose clause map contains the cited clause identities; where citations span modules, all such modules enter, or the edge is recorded open under the enumeration limb.

**8. [major] Rule 2 and rule 3 contradict each other on iteration, and rule 3's escape has no expression in the corpus.**
Anchor — rule 2: *"Add the direct `depends_on` obligations of **every selected module**"*; rule 3: *"Traverse beyond direct edges only where an edge is **explicitly marked transitive**"*; rule 6: *"**Termination.** Stop at identities already included."*
A module added by rule 2 is thereafter a selected module, so rule 2 read literally iterates to a fixpoint — which is the transitive traversal rule 3 forbids. Nothing states whether rule 2 applies once to the rule-1 seed set or to closure. Two selectors terminate differently on any corpus where a second-order module introduces a new contract, and this one qualifies. Cycle behavior is undefined for the same reason: RFC-0002/0003/0004/0005 form a mutual-dependency clique, which rule 6 disposes of under a fixpoint reading and which never arises under a once reading. Separately, *"explicitly marked transitive"* has no expression anywhere: a sweep of `rfcs/` for `transitive` returns 4 hits — 3 are RFC-0010 prose about stop propagation, 1 is rule 3's own text — and no front-matter field for the marker is defined in any artifact.
Repair — state the quantifier explicitly ("rule 2 applies once, to the modules selected under rule 1"), and either name the transitivity marker's field or retire rule 3's escape clause as unexpressible.

**9. [major] The clause-only inclusion RFC11-16 mandates has no defined interaction with RFC11-4, rule 2, or measurement.**
Anchor — RFC11-16: *"the mandatory set includes the **constraining clause** — not automatically the entire constraining contract. The constraining clause's direct dependencies enter only where required to interpret that clause."* Against RFC11-4: *"The mandatory set always includes, **for every selected contract**, what that contract's implementation-boundary declaration names (RFC11-13)."*
Three questions are unanswered: (i) does a clause-only inclusion make its contract a "selected contract", triggering RFC11-4's per-contract boundary duty; (ii) does the clause's module enter rule 2's *"every selected module"* quantifier, since a clause is not a module; (iii) how is a clause-only inclusion measured and digested, when `context_load.py` resolves file paths and nothing else. No fixture answers any of them — 0/10 exercise RFC11-16 at all (F1). This is the concrete reason my derivations diverged on RFC7-3/RFC5-3 rather than merely disagreeing about them.
Repair — state the three dispositions in RFC11-16, and make the fixture that exercises it (per F1) demonstrate all three.

**10. [major] Module 2 §1 defers its acceptance criterion to a place where no criterion is stated.**
Anchor — RFC-0011 module 2 §1: *"This module is acceptable only when its selection rules can reproduce the blind golden selection fixtures — **the acceptance criterion is stated with the fixtures, not here**, because a criterion inside its own subject cannot gate it."*
Sweep: `fixtures/` holds 11 files; **0** contain "acceptance criterion" or any pass/fail standard for a blind derivation. A sweep of the whole candidates tree excluding `round-*`, `reviews/` and `history/` returns 6 hits for the phrase, none in `fixtures/`. The consequence is not theoretical: this review produced divergences on 3 of 3 fixtures and there is no stated standard for how many, or of what kind, defeat acceptance. The deferral is well-reasoned; the destination is empty.
Repair — state the criterion in `fixtures/` (a README is the obvious home), including what "reproduce" means: set equality, or set equality modulo the module-choice latitude rule 2 currently grants (F7), and what an unenumerated omission costs.

**11. [minor] The generated projection RFC11-4 names as a selection input does not carry the field RFC11-4 most depends on.**
Anchor — RFC11-4: *"explicit `applies_to` and clause-level metadata (**the contract-index projection** — a rebuildable RFC11-7 projection…)"*, and *"the mandatory set always includes… what that contract's implementation-boundary declaration names (RFC11-13), **consumed from the contract's own index**."*
`05-CONTRACT-INDEX.yaml` (540 lines) contains **0** occurrences of `implementation_boundary`; it projects `status_source, title, governs, applies_to, depends_on, tags, modules, module_ranges, clauses, constrains, constrains_source`. No violation — RFC11-13 locates the declaration in the governed artifact and RFC11-4's "own index" means the package README — but a selector working from the projection must open eleven READMEs for a field the projection could carry, which is friction pointed straight at the clause with the least tolerance for it.
Repair — project `implementation_boundary` into `05-CONTRACT-INDEX.yaml` from the same front matter, under the existing `--check` drift guard.

---

## Secondary questions, answered

**Q4 — Is RFC11-4 satisfiable over all eleven contracts?** Partly. [Observed] Its RFC11-13 limb is satisfiable: **11 of 11** contracts declare `implementation_boundary` in their index front matter, all `kind: requires-openspec`, and every named clause (RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27, RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16, RFC11-12) resolves to a defining module. [Observed] Its RFC11-15 limb is **not** satisfiable: 0 of 39 modules carry `task_classes`/`risk_classes`, and `governance_sources` is a mention scan, not ownership metadata (F5). [Observed] Its "declared risk and change class" input is supplied only by the task statement's prose, which no metadata schema constrains. So RFC11-4 is satisfiable for contract selection and not for doctrine/craft selection — which is what RFC11-15's escape clause concedes, and what 6 of 10 fixtures fail to state.

**Q5 — Is rule 2 precise enough that two selectors terminate identically?** No. Three distinct gaps: module choice within a satisfied edge is ungoverned (F7); the rule-2/rule-3 iteration quantifier is contradictory, which also leaves cycle behavior undefined (F8); and clause-only inclusions under RFC11-16 sit outside the rule's vocabulary entirely (F9). README-only loads are the one edge case that *is* defined — RFC11-4's index-less limb covers it — but neither fixture exercising it complies (F4). Empirically: two of my three blind derivations diverged from the record on module choice alone, and both divergences conform to the rule.

**Q6 — Do fixtures 1 and 8 state the same phase-boundary rule?** [Observed] Yes. They now state one two-tier rule from opposite sides and each names the other: fixture 1 — *"The task edits adopted narrative content and does **not** sit on the OpenSpec seam… so the boundary rule does not force the module defining RFC7-38… Contrast fixture 8, which sits on the seam and therefore must load the defining module. This is the single rule both fixtures apply."* Fixture 8 — *"this task **sits on that boundary**… The amended rule therefore forces the module *defining* RFC7-38 — `rendering-and-surface.md`… This is the same single rule fixture 1 applies from the other side."* Both name the prior contradiction and the amendment that closed it. This divergence is repaired.

**Q7 — Are fixture measurements machine-anchored?** [Observed] Yes, and the check is falsifiable — I verified it rather than trusting its exit code. `build_budget_report.py --check` prints `fixture anchors match regeneration` (exit 0). Against a scratchpad copy I ran three mutations: editing fixture 2's anchored word figure → `DRIFT: context-selection-2… anchored measurement is stale` (exit 1); appending words to `RFC-0008/state-vocabulary-and-cost.md` → drift on fixtures 2 and 10 plus the report itself; and a **word-count-preserving** one-word capitalization in the same mandatory file → still caught, proving the digest is checked independently of the word count. `check_governance.py` CG-18 reports `20 measurements examined, 0 findings` at baseline and `2 findings` under that mutation — denominator 20 = 10 fixtures × (words, digest), i.e. full coverage. The only transcribed figures remaining are frozen historical ones inside re-measurement notes (*"Previous: 18,315 words, digest a398a…"*), which are records, not live claims.

**Q8 — Does any fixture's recorded selection violate the policy it instantiates?** Yes: fixtures 2, 5 and 10 on RFC11-16/rule 4 (F1); fixtures 2 and 5 on rule 2's enumeration duty (F2); fixture 5 on rule 2's edge premise (F3); fixtures 9 and 10 on RFC11-4's index-digest duty (F4); fixture 6 on RFC11-15's factual premise (F5); fixtures 1–5 on rule 7 for doctrine (F6).

---

## Judgment

The policy has been genuinely repaired since the defects its own text records: rules 1–9 exist and are mostly operable, the two-tier phase-boundary rule is now stated identically from both sides, the index-less declaration limb exists, and every fixture measurement is machine-written and mutation-falsifiable. Fixtures 9 and 10 are good work — fixture 10 in particular refuses to check the determinism box and says why.

But the module's acceptance turns on one claim: that its rules reproduce the blind fixtures. Against that claim: a clause (RFC11-16) with zero fixture coverage and three live counterexamples in the fixtures themselves; a traversal rule that does not determine a module and contradicts its neighbor on iteration; a fixture that cites a dependency edge the corpus does not contain; and an acceptance criterion the clause defers to a location where nothing is written. Those are not imperfections an owner could knowingly bind — several are statements that are false against the artifacts, and the standard for judging the rest does not exist yet. They are edits.

VERDICT: REVISE
