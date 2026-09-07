# Decision history — resolved rows and register chronology

> **Historical record, deliberately off the default path.** This file holds
> what the pending register used to carry inline: the resolved-row
> narratives and the register's own as-of chronology. Nothing here is open,
> and nothing here is authority — every ruling below names the record that
> owns it, and that record wins. The live queue is
> [`PENDING-OWNER-DECISIONS.md`](PENDING-OWNER-DECISIONS.md).
>
> Moved here 2026-08-17 (convergence pass, round 2026-08i). The register's
> pre-refactor row narratives — including the long accumulated open-row
> cells — are preserved verbatim in git history at commit `9c43fc5`
> (`git show 9c43fc5:.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`).

## Resolved on 2026-09-07 (the written-estate questions, P-54…P-59 and P-66)

The seven questions gathered by the documentation-estate packet
(`DOCUMENTATION-ESTATE-DECISION-PACKET.md`, written 2026-09-05, extended
2026-09-06) were ruled by the owner in one reply on 2026-09-07 agreeing with
every recommendation in it, and applied the same day so far as each arm
allows — two of the seven defer by their own terms and one is disclosure
only. The rulings record is `DOCUMENTATION-ESTATE-OWNER-RULINGS-DECISION.md`,
which owns the full detail and quotes the reply verbatim.

| # | What happened |
|---|---|
| P-54 | **Ruled — arm (b)**: `openspec/config.yaml` trimmed to its one live setting, `schema: spec-driven`; the shipped `context:` and `rules:` examples deleted, and this project's agent-facing context ruled to travel through `AGENTS.md` and the governed plane rather than tool config. A comment in the file states the ruling so the block is not reintroduced. The file's only evidence citation, in the Administration-1 launch-gate record, is anchored to commit `71e5986` and describes the scaffold rather than quoting its bytes, so the trim retires nothing. |
| P-55 | **Ruled — arm (b)**: this project does not use the OpenSpec archive and spec-materialization steps. `openspec/specs/` and `openspec/changes/archive/` each took a one-line README saying so. Neither directory had ever been tracked (git stores no empty directory), so the READMEs also make them exist in a clone for the first time — before this, the "two empty directories" a reader saw were present only in the authoring checkout. |
| P-56 | **Ruled — arm (b)**: `syzygy_begin_specification_stage_capability1_prompt.md` stays at the repository root and took a head note — what it opened, that the stage closed on 2026-08-20, that it is not an instruction to any agent reading the repository today, and why it is kept there. Not (a): (a) edits a decision record to buy a tidier root listing. The citation pinning it here, in `CAPABILITY-1-SPECIFICATION-AUTHORING-DECISION.md`, wraps across a line break ("(repository" / "root)"), which is why a basename sweep does not find it. |
| P-57 | **Ruled — arm (a)**: an agent was authorized to write `openspec/README.md` as navigation only — which change is adopted and under which act, which are candidate, what the empty directories mean — banner-marked never authority. **The arm reserved the owner's review of its text, and that review has not happened**; the page is committed so it is reviewable in place and says so on its face. It is the governed plane's only agent-authored page. |
| P-58 | **Ruled — arm (a), folded into act 4 whenever the owner next takes it up**: the overview is to name VIS-1 and VIS-2 by identifier and keep the activity-is-not-proof sentence as prose rather than as one of two rules. The arm defers by its own terms — an agent may prepare the delta, only the owner performs the act — so `.syzygy/intent/OVERVIEW.md` is byte-unchanged and was not opened for editing. Prepared as delta **OVW-1** with P-59, unreviewed. |
| P-59 | **Ruled — arm (a), alongside P-58**: the overview's bolded "Nothing is implemented" is to be replaced by the route to `PROJECT-STATUS.md` that the next paragraph already takes. Same deferral; deliberately the same one delta, because a second edit to act 4's argument later would retire whatever confirmation the first earned. |
| P-66 | **Ruled — arm (b), with (a) riding along if a CC-SPEC amendment ever comes**: the amendment-history banner naming five of the nine phase rules CC-SPEC-8 defers to is a permanent, disclosed blemish. Nothing was edited — the file's bytes are a performed act's argument — and arm (c), a standalone amendment act for prose that binds nothing, was not taken. **This row and the rulings record are the disclosure; the next audit should not re-raise it.** |

Two things this pass recorded against the records themselves: the packet's
"none depends on another" holds for the questions but not for the
applications (P-57's index has to say what P-55 settled), and the register's
own published row counts had been one low since 2026-08-06 because their
stated predicate did not match the sub-lettered row `P-25(c)`. Both are
marked in place in the records that carried them.

## Resolved on 2026-09-07 (the PWB improvement-cycle questions, P-60…P-65)

The six questions gathered by the PWB cycle report
(`PWB-CYCLE-REPORT-DECISION-PACKET.md`, 2026-09-06) were ruled by the owner
in one reply on 2026-09-07 and applied the same day on that reply's own
apply instruction ("Follow your recommendations for all of the above. For
the butler page change, dispatch a subagent to do that"). Every item passed
independent adversarial subagent review (scope and recommendation verdicts)
in a local questionnaire packet before presentation; the review corrected
the two rows quoted below and found that the packet's "None depends on
another" was wrong for one pair. The rulings record is
`PWB-CYCLE-OWNER-RULINGS-DECISION.md`, which owns the full detail.

| # | What happened |
|---|---|
| P-60 | **Ruled — arm (a)/A**: repair the Butlers V1 page (nine edits over eight lines) so its catalog parses; no Syzygy act. The row's "one line uses a colon" understated it: the extractor stops at the first failure, and the page has five colon forms and four duplicate labels. **Owner edit to the boundary:** the edit is made by a dispatched agent on a Butlers branch, not by the owner's hand; merge stays the owner's and follows the P-63 trim. |
| P-61 | **Ruled — A**: bold the seven code-span first cells in the two Lay and Land tables (87 topology items); roster untouched, no grammar act. The row as written was wrong and is quoted here so the correction is checkable: it said the withheld roster files and the failing table "together … empty the catalog and topology populations and leave the roster denominator Unknown; readiness reports two limbs". The roster withholding gates no limb; the empty populations come from the two failing pages, and readiness reports three limbs. Same owner edit to the boundary as P-60. |
| P-62 | **Ruled — A**: add an index page at openspec/README.md in Butlers, linking only to directories, so Spec and Spine is discovered like the other four pillars. Written by the same dispatched agent as its own commit (the owner's "butler page change" read as covering it; droppable alone). Because this delegates drafting rather than a pre-reviewed edit, the commit is a proposal: its text goes before the owner verbatim and is final only on the owner's approval or knowing merge. |
| P-63 | **Ruled — A**: an implementation-only trim of the Polaris human page, measured before the P-60/P-61 repairs merge, target about 420 KB; if short, a registry act packet (raise or narrow) is drafted at once. Bead `syzygy-1z3.27`. The row's default, "the page serves until it crosses the ceiling, then reports the breach", misled by omission — at the ceiling the page serves nothing (HTTP 503, readiness false) — and its arm (c), "let the limit ledger report the breach", was false: no ledger sees a response-ceiling breach and nothing logs it. P-52 not ruled; the bead was filed on the item's stated boundary. |
| P-64 | **Ruled — A**: one sentence in the owner's words that following an Exact source link is a permitted walkthrough step, inserted below line 79 of the candidate walkthrough packet. The owner supplied it in a second reply the same day ("Yes, following the exact-source link is permitted.") and it was inserted verbatim as the last paragraph of "What is already in place"; the packet stays a candidate and binds nothing. |
| P-65 | **Ruled — A**: repair epic `syzygy-1z3.24` closed 2026-09-07 with criterion 4 (a passing retained run) recorded unmet and carried by `syzygy-1z3.22`'s readiness gate and by `syzygy-1z3.27`. The walkthrough stays gated on P-60, P-61, P-63 and a green preflight. |

## Resolved on 2026-08-19, second sitting (the Administration-1 owner inputs, P-45…P-48)

The four owner inputs queued by the Administration-1 repair pass
(2026-08-18) were ruled in one questionnaire sitting on 2026-08-19 and
applied the same day on the owner's explicit apply instruction. Every
item passed two rounds of independent adversarial subagent review
(scope and recommendation verdicts each) before presentation; the
review found and forced correction of two coordinator drafting defects
(a candidate artifact's phrase presented as a doctrine citation, and an
inverted claim about which arm guarantees the F2 verdict limb) — both
corrected before the owner saw the items. Each row names its own
decision record, which owns the full detail.

| # | What happened |
|---|---|
| P-45 | **Ruled — arm (a), the envelope stated**: engineering attention 2 hours/week; review capacity Claude-family agents plus the owner with occasional GPT 5.6-family review, no fixed cadence; model budget ceiling $200/month (Codex subscription); 2–3 concurrent workstreams; **first proving project: the syzygy repository itself**, butlers second. Settles Administration 1's A6 `Unknown`; the proving-project name is the risk-ordering record's own R2 partial test and gives R1 a named place to accrue evidence. The scope-versus-capacity assessment remains follow-on work. Record: `A6-RESOURCE-ENVELOPE-DECISION.md`. |
| P-46 | **Ruled — arm (b)**: no numeric governance-effort ceiling is declared; **case-by-case owner judgment is the recorded posture**. F6 stays `Not met` at future administrations knowingly and disclosed — a non-conjunct, non-blocking grade under instrument v2.4. Record: `F6-GOVERNANCE-CEILING-DECISION.md`. |
| P-47 | **Ruled — arm (a)**: the **governance-reduction plan is adopted as directed work** — banner-and-route retirements execute at their named gates without per-artifact re-asking; no deletion, no act-bound bytes, ever. Gates §1/§2/§4 had already arrived, so the declined P-44 offer and the sealed launch packet were banner-marked at the apply; §3 awaits the first accepted specification. No deferral is created; F2's grade at Administration 2 stays the grader's call. The plan's own doctrine-misattribution defect (found by the adversarial review) is disclosed in the record and queued in beads. Record: `F2-GOVERNANCE-REDUCTION-DECISION.md`. |
| P-48 | **Ruled — arm (a), N=2**: the repair↔administration cycle is bounded at **at most two further administrations**; if Administration 3 is not `READY`, the owner makes the launch decision directly on the record then in hand — the cycle ends either way. Answers the stop-condition half of F1's settlement; constrains when the decision stops being deferred, never its content. Record: `LAUNCH-REPAIR-STOP-CONDITION-DECISION.md`. |

## Resolved on 2026-08-19 (the 2026-08-18 questionnaire rulings, applied on explicit owner request)

Four rulings the owner recorded in the 2026-08-18 local questionnaire
sitting (items 10–13; the packet's own process note discloses that their
adversarial reviews were coordinator-direct rather than clean
independent-subagent passes). Each was applied canonically 2026-08-19,
on the owner's explicit apply instruction; each names its own decision
record, which owns the full detail.

| # | What happened |
|---|---|
| P-14 | **Ruled — MIT** (option B, owner-selected directly over the recommended legal-review-first arm; the copyleft-reach `[Unknown]` knowingly accepted unresolved by counsel). Applied: root `LICENSE` created, `README.md` §License and `CONTRIBUTING.md` posture updated. Record: `LICENSE-CHOICE-DECISION.md`; context: `LICENSE-DECISION-PACKET.md`. |
| P-16 | **Ruled — option A**: the term registry's 31 entries designated **non-binding working drafting vocabulary**; the registry stays candidate, banner unchanged, no entry citable as binding; P-17/P-18 stay open. Record: `TERM-REGISTRY-DRAFTING-VOCABULARY-DECISION.md`. |
| P-24 | **Ruled — option A**: doctrine question **D4** ruled *inside VIS-4's bounds*, and the reviewer's reason-stating §1.2 wording designated as the text act 5 would carry — clearing RC-7 F10 by an owner ruling rather than a side-effect sentence. Act 5 (P-5) stays open; the §1.1 autonomy-ceiling question stays unruled; no doctrine byte moved. Record: `D4-RULING-DECISION.md`. |
| P-44 | **Ruled — arm (b), declined**: no lagging-specification exception is added to CC-REV-2. Arm (a) was not lawfully choosable (RD-69 N4, offer defects) and was not chosen; any future exception is a fresh offer with a fresh review. The offer file is unedited. Record: `CC-REV-2-LAGGING-SPEC-EXCEPTION-DECISION.md`. |

## Resolved on 2026-08-17 (the four owner acts, and their §7 ratifications)

The acts themselves are recorded in
[`ACCEPTANCE-ACT-RECORD.md`](ACCEPTANCE-ACT-RECORD.md), which owns them;
these rows record only each queue row's disposal.

| # | What happened |
|---|---|
| P-41 | **Executed — act 6 performed 2026-08-17** (`CONFIRM CRAFT AMENDMENT: CC-SPEC@9889b7e3…`, one sitting with act 7). The specification-acceptance policy (CC-SPEC-1…11) is in force as owner-confirmed craft at its reviewed digest; the RD-51 → RD-69 (`REVISE`) → blocker repair → RD-70 (`CONFIRM WITH EXCEPTIONS`) cycle and the nine disclosed non-blocking findings travel with it. Owning records: `SPECIFICATION-ACCEPTANCE-DECISION.md`; `ACCEPTANCE-ACT-RECORD.md`; `../policies/craft-and-care/INSTALL-RECORD.md`. |
| P-42 | **Executed — act 7 performed 2026-08-17** (`CONFIRM CRAFT AMENDMENT: CC-IMPACT@cd6ec838…`, same sitting as act 6, satisfying the joint-sitting requirement). The shape-to-spec impact policy (CC-IMPACT-1…7) is in force at its reviewed digest. Owning records: `SHAPE-TO-SPEC-IMPACT-DECISION.md`; `ACCEPTANCE-ACT-RECORD.md`; `../policies/craft-and-care/INSTALL-RECORD.md`. |
| P-28 | **Resolved by ratification at the Wave A act** (acceptance record §7 item 16): performing the act with the drafted mission-extension profile riding in ratified it. The owner read §7 before the phrase (§2 step 0). Owning record: `ACCEPTANCE-ACT-RECORD.md` (Wave A entry). |
| P-22 | **Resolved by ratification at the Wave B act** (acceptance record §7 item 17): the RFC9-8(a) registry placement rode in and was ratified when the act was performed. Owning record: `ACCEPTANCE-ACT-RECORD.md` (Wave B entry). |

P-21 did **not** resolve at the acts — §7 item 18 ratifies only the
declaration's *presence* while sub-question (a) rides in unruled; its row
stays open in the register.

## Resolved on 2026-08-16 (owner ruling via adversarially-reviewed questionnaire packet)

Every ruling below is a **recorded decision, not a digest-binding act** —
none performs the Wave A or Wave B act, none runs the formal launch-gate
administration, and none authors OpenSpec. Each ruling was independently
adversarially reviewed (separate scope and recommendation verdicts) before
being presented, per the `user-questionnaire` subskill's mandatory gate; the
full packet, including the review record and one caught-and-corrected error
(a stale-framing discrepancy in an external plan's stated preference on
`P-33`), is the owner's local decision packet, not tracked in this
repository.

| # | What happened |
|---|---|
| P-31 | **Ruled.** Ratify the drafted `RFC2-19(a)` exemption as written — the merged-but-unreconciled Unknown carries no thirteenth reason; the `RFC2-24` list stays closed at twelve. Recorded as **SDR-34**, `SURFACE-DECISION-RECORD.md`. Zero bytes move; the Wave A confirmation is unaffected. |
| P-33 | **Ruled.** Install shape **(M)** — leave the accepted modules' internal path strings alone; install no companion package apparatus; install neither package-wide manifest. Recorded in `WAVE-A-INSTALL-SHAPE-DECISION.md`'s own template. Zero bytes move; both Wave A and Wave B confirmations are unaffected. This was the sole obstacle withholding the Wave A offer — **the offer is now unblocked; the Wave A act itself has not been performed.** |
| P-35 | **Ruled.** Full operating-constraints table filled in (option a) — 1 operator; attention and budget Unknown; independent-review capacity is Claude-family agents plus the owner, with occasional ad hoc other-model-family review; other rows recorded or Unknown. No date or delivery commitment. Recorded in `PROJECT-OPERATING-CONSTRAINTS-DECISION.md`. |
| P-36 | **Ruled.** The two-term rule: no verifying evidence → `Unknown`; evidence of non-satisfaction → `Gap`. Recorded as **SDR-35**, `SURFACE-DECISION-RECORD.md`; the term registry's `T-20`/`T-31` disclosed conflict note collapses to a pointer at that row. Zero bytes move on any contract module. |
| P-37 | **Ruled.** Seven project-shape facets adopted, no cross-facet rollup; drafting site = the Capability 1 specification (site a2), not an RFC-0006 amendment. Recorded as **SDR-36**, `SURFACE-DECISION-RECORD.md`, naming both the facets and the site. Both Wave A and Wave B confirmations are unaffected (the cheaper of the two drafting-site arms was chosen). |
| P-38 | **Ruled.** As drafted (option a): fixed entry `.syzygy/intent/OVERVIEW.md` identified with the primary narrative (RFC7-6, "not two front doors"); four-valued per-repository discoverability finding; propose-only root-README link. Recorded in `HUMAN-ENTRY-DECISION.md`. Zero bytes move; the Wave B confirmation is unaffected. |
| P-39 | **Ruled.** Pin current upstream OpenSpec, at **1.9.0** (refreshed at answer time from the packet's measured `1.8.0`, since upstream had published again and the owner had already upgraded). The schema/template format contract is confirmed byte-identical `1.8.0`→`1.9.0`; other tooling changes exist and are recorded `[Inferred]` non-breaking, not independently verified line-by-line. Recorded in `GOVERNANCE-SUBSTRATE-LOCK.yaml`'s `openspec` block. |
| P-40 | **Ruled.** One OpenSpec change governs one coherent capability, or one coherent change to one. Recorded as **SDR-37**, `SURFACE-DECISION-RECORD.md`. `FIRST-OPENSPEC-SEQUENCE.md` now cites the SDR row instead of asserting the rule in its own voice. Zero bytes move on any contract module. |
| P-34 | **Ruled (approved), arm (a).** The owner first ruled arm (c) after the v2.3 reviews (RD-65/RD-66, both `REVISE`, the fourth consecutive pair) — the structural v2.4 repair was committed (`4dd6e20`) and its review pair RD-67/RD-68 returned `REVISE`/`REVISE`, the fifth consecutive pair. The one structural repair held (no live forgery in v2.4), but two instance-patched class defects recurred as fresh BLOCKING false-`READY` paths. The owner weighed that under arm (c)'s reasoning and on 2026-08-16 ruled arm (a): **approved v2.4 as process policy, residuals disclosed, F5 not promoted**. The readiness standard's "launch-gate is owner-approved" conjunct is satisfied at v2.4; the formal (out-of-family) administration becomes runnable with the two residuals in hand. No unilateral v2.5 was begun; a bounded v2.5 remains an owner option, not a gate. Owning record: `LAUNCH-GATE-AUTHORITY-DECISION.md`. |

## Resolved on 2026-08-06 (owner override, recorded)

| # | What happened |
|---|---|
| P-26 | **Executed.** Owner override: re-pin `th-engineering` to the installed commit `f4cf1c7` (closing the drift instead of holding the 2026-07-30 pin) **and** vendor a byte-identical local copy in-tree at `.claude/skills/th-engineering/` and `.codex/skills/th-engineering/`, superseding the `PUBLIC-CLONE-AUTHORITY-MATRIX.md` "out of scope, do not import" disposition. CC-BAR-1 and CC-TEST-1…6 were re-checked against test-rigor's two new bars and the new engineering-bar Definition-of-Done item; no conflicts found, so no override text changed — `testing-and-verification.md` gained CC-TEST-7 recording the re-check, `engineering-bar.md`'s CC-BAR-1 gained a matching note. Full detail: `../policies/GOVERNANCE-SUBSTRATE-LOCK.yaml` `th_engineering`; `../policies/craft-and-care/INSTALL-RECORD.md` (2026-08-06 correction); `../policies/craft-and-care/README.md` "Adoption by reference" |

## Resolved during the 2026-08-05 round (recorded, not decisions to make)

| # | What happened |
|---|---|
| P-6 | **Executed.** The retired phrase was removed from both digest sets — `rfcs/RFC-0003/governance-homes-and-owner-acts.md` (act 1) and topology `README.md` (act 3). Both manifests regenerated; semantic deltas SD-1/SD-2 |
| P-7 | **Executed.** All nine canonical craft files now describe themselves truthfully as canonical; rule text byte-unchanged; digests regenerated (SD-3) |
| P-8 | **Executed.** `INSTALL-RECORD.md` binds craft force to the digest-bound acceptance act, not the retired phrase (SD-4) |
| P-9 | **Executed.** Candidate contracts, topology, acceptance record, reviews, validation scripts, decision warrants, and the license packet are tracked and clone-visible; raw interviews and bootstrap history stay founder-local (FD-021/FD-037) |
| P-11 | **Executed.** README, AGENTS.md, PROJECT-STATUS.md, CONTRIBUTING.md, SECURITY.md installed; `.gitignore` verified |
| P-13 | **Executed.** The overview's progressive-disclosure refactor landed (SD-9); its adoption is P-4 |

## The register's as-of chronology (oldest last)

- **2026-09-07** — the PWB cycle questions P-60…P-65 ruled in one owner
  reply (A on every row) and applied on its own apply instruction: rows
  moved to resolved; `PWB-CYCLE-OWNER-RULINGS-DECISION.md` owns them.
  P-52 stays open.
- **2026-08-20** — the owner's **launch decision**: Capability 1
  specification authoring authorized by explicit owner instruction
  (`CAPABILITY-1-SPECIFICATION-AUTHORING-DECISION.md`, which owns the
  decision). The Administration 1 `NOT READY` verdict stands as filed;
  the lifecycle stage moves from final pre-specification to
  specification defining. No queue row is disposed by this decision.
- **2026-08-19** — the 2026-08-18 questionnaire rulings applied: P-14
  (MIT), P-16, P-24 (D4), P-44 moved to resolved on the owner's explicit
  apply request. P-45…P-48 had been added 2026-08-18 by the
  Administration-1 repair pass (round 2026-08j).
- **2026-08-17** — the four owner acts: Waves A and B accepted (A then B),
  then craft acts 6 and 7 performed in one sitting. P-41/P-42 executed;
  P-22/P-28 resolved by §7 ratification; P-21 narrowed to its open
  sub-question (a). The register refactored the same day (this file
  created); resolved rows moved here.
- **2026-08-16** — eight rows ruled by the owner in one adversarially-reviewed
  questionnaire-packet sitting: P-31, P-33, P-35, P-36, P-37, P-38, P-39,
  P-40; P-34 ruled arm (c) then arm (a) the same day (see above).
- **2026-08-13** — P-43 and P-44 added; P-41/P-42 candidates amended against
  RD-51 and the two bounded packets added to the decisions home; P-34's row
  compressed (owner charter §8) after growing to 1,280 words of chronology.
- **2026-08-10** (round 2026-08e, launch closure) — rows P-25(c), P-34…P-41
  added (P-41 the same day, RD28-05), P-22 re-grounded, P-38 corrected to
  RFC7-40's four-value domain; the RFC7-39 entry-identity ruling disclosed at
  the acceptance record's §7 item 15 travels on P-38's packet; launch-scope
  index added before the open table (RD29-06).
- **2026-08-09** (round 2026-08d, structural closure) — the single
  foundational-contract act P-1 was restructured into **six wave acts**.
  Four open rows had their ground changed by candidate-byte repairs
  (P-21(c′), P-22, P-23, P-28); a candidate-byte repair is a drafting
  posture, not a decision. Later the same day the round's fresh-context
  review pass completed — fifteen reviews, every verdict `REVISE` — adding
  P-29…P-33.
- **2026-08-07** — P-28 added; P-21 extended with review RD-4's finding F-17
  (one arm of a pending question installed into candidate front matter while
  open).
- **2026-08-06c** — P-26 closed by owner override (see above); P-27 added
  from reviews RC-11 (`REVISE`) and RC-12 (`EXCEPTIONS`); vocabulary rows
  re-checked against `round-2026-08b/TERM-CLOSURE-REPORT.md`.
- **2026-08-05** — regenerated at the close of the human-clarity refactor
  round. The previous revision (as-of `adddc34`) is superseded: it listed
  P-6/P-7/P-8/P-9/P-11 as open when the round executed them, and routed most
  owning records to the git-excluded `_bootstrap/` tree.

## Superseded packet notes (2026-08-10)

P-12's packet became `KNOWLEDGE-HYGIENE-DECISION.md` and P-33's
`WAVE-A-INSTALL-SHAPE-DECISION.md` (both this directory), superseding the
round-08d packets file for those rows; the round-08d
`OWNER-DECISION-PACKETS.md` remained current for packets 1, 3, 4, 5, 9 and
12, with packet 6 stale and banner-marked (P-22's row and the packets file's
own banner said so).
