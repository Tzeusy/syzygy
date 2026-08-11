# RD-52 — Owner-packet one-sitting comprehension (round-2026-08f, frozen commit `e2efda6`)

> **Provenance banner, added by the recording session — everything below the
> rule is the reviewer's raw output, copied verbatim and unedited.** The
> verdict word is copied exactly.
>
> | | |
> |---|---|
> | **Charter role** | §14 review 8 — can a real owner settle the bounded decision packet in one sitting? |
> | **Dispatched** | 2026-08-11 |
> | **Subject commit** | `e2efda6` — bytes frozen; nothing in the subject was edited between dispatch and this record |
> | **Entry point given** | `round-2026-08f/CAPABILITY-1-OWNER-DECISION-PACKET.md`, and only what it links |
> | **Context** | fresh — the reviewer stood in for an owner with one sitting and no project history |
> | **Model family** | same family as the corpus authors. Supports repair; **is not the formal launch administration** (charter §2.15) |
> | **Verdict** | `REVISE` — with three findings the reviewer marks **blocking** |
>
> **Disposition is not recorded here.** This file is the reviewer's bytes.
> The reviewer's opening sentence refers to a cross-check agent it attempted
> and did not receive; it is preserved as written.

---

The cross-check agent hasn't returned; everything below I verified myself, first-hand.

---

# VERDICT: REVISE

*(A real owner cannot settle this packet in one sitting — not because of reading volume alone, but because four of the eleven decisions are, by the packet's own text, not settleable at all right now.)*

---

## File-and-effort log

| # | File | How much I read | Why |
|---|---|---|---|
| 1 | `.syzygy/governance/contracts/candidates/round-2026-08f/CAPABILITY-1-OWNER-DECISION-PACKET.md` | all 182 lines | the start point |
| 2 | `.syzygy/governance/decisions/WAVE-A-INSTALL-SHAPE-DECISION.md` | all 152 | Q2/Q3 — the first decision |
| 3 | `.syzygy/governance/contracts/candidates/round-2026-08f/P33-SEMANTIC-INSTALL-ANALYSIS.md` | all 179 | packet routes to it for method/denominators |
| 4 | `.syzygy/governance/decisions/PROJECT-SHAPE-FACETS-DECISION.md` | all 88 | row 3 didn't stand alone |
| 5 | `.syzygy/governance/decisions/UNKNOWNS-AND-GAPS-DECISION.md` | all 79 | boundedness check |
| 6 | `.syzygy/governance/decisions/HUMAN-ENTRY-DECISION.md` | all 85 | row 5 says "the alternative" — needed the options |
| 7 | `.syzygy/governance/decisions/SPECIFICATION-GRANULARITY-DECISION.md` | all 57 | boundedness check |
| 8 | `.syzygy/governance/decisions/OPENSPEC-FORM-AND-VERSION-DECISION.md` | all 62 | Q4 |
| 9 | `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` | all 153 | Q1/Q4 — the largest linked packet |
| 10 | `.syzygy/governance/decisions/PROJECT-OPERATING-CONSTRAINTS-DECISION.md` | all 67 | Q4 |
| 11 | `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 2 rows read in full (P-31 L184, P-42 L196) + all 42 row headers enumerated | P-31 has no packet; needed the denominator |
| 12 | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/reconciliation-chain.md` | L210–259 of 346 (found by grep) | to see the P-31 arm I'd be ratifying |
| 13 | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/governance-homes-and-owner-acts.md` | L73–117 of 530 (found by grep) | to see the RFC3-15 cell (1e) amends — **quoted nowhere in the packet** |
| 14 | `PROJECT-STATUS.md` | L62–116 | contradiction check |
| 15 | `.syzygy/governance/contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` | §1 rows 2–5 (L28–31) | to check what the packet omits |
| 16 | shell | `sha256sum` on the two P-34 artifacts; `wc -l` on the launch-gate instrument (**2,059 lines**) and the two unlinked craft policies (107 + 119) | to test the packet's own verification step |

**Read to answer the questions: ~1,150 lines of dense normative prose (~14k words).** Not read, though the decisions require them: the 2,059-line launch-gate instrument (P-34), the 17 KB v2.0 semantic delta, the two craft-policy candidates (P-41/P-42).

---

## Q1 — What am I being asked to decide, in total?

Eleven rulings across ten sections:

1. **P-33** — where the four non-contract companions live when Wave A installs, and whether a 39-row manifest may install at a 19-module act.
2. **P-31** — ratify or revert the drafted RFC2-19(a) exemption for merged-but-unreconciled work.
3. **P-37** — does the project-shape facet vocabulary belong to the Capability 1 spec or to contract semantics (and, in the linked packet only, *which drafting site*).
4. **P-36** — fix the definitions of `Unknown` and `Gap`.
5. **P-38** — fix the human entry point and the discoverability posture.
6. **P-40** — define what "one OpenSpec change" is.
7. **P-39** — pin an OpenSpec version and record the migration posture.
8. **P-41** — bring the specification-acceptance standard CC-SPEC-1…10 into force.
9. **P-42** — bring the shape-to-spec impact rule CC-IMPACT-1…7 into force.
10. **P-35** — state the project's real operating constraints, or honest Unknowns.
11. **P-34** — approve launch-gate v2.0 as process policy.

**But the packet cannot actually answer this question**, which is finding 3: its exclusion list (L164–174) accounts for P-1, the C/D waves, P-29/30/32, P-12 and P-14…P-28 — and silently omits five open queue entries, three of which are owner *acts* still on the acceptance record: **P-2** (`CONFIRM CRAFT AMENDMENT: CC-TEST-2`), **P-3** (`ACCEPT TOPOLOGY`), **P-4** (`ADOPT PROJECT OVERVIEW`), **P-5** (D3), and **P-10**. Since P-41/P-42 — also craft amendments — *are* on the page as Capability 1 prerequisites, I cannot tell whether CC-TEST-2 is one too.

## Q2 — Which first, and why must it be first?

**P-33.** Not because it is cheapest — it is the most expensive thing on the page — but because the Wave A act's install step *is the thing under question*. L30–32: the act "would freeze the install ceremony it questions." An act is digest-binding and unrepairable afterwards; every other decision on the page is a recorded ruling that can be revised. P-33 is the only one whose lateness is irreversible.

Second-order reason, and the packet earns credit for stating it (L37–41): **no arm of P-33 preserves Wave A's existing `CONFIRM`.** Since the regeneration happens regardless, P-31 and P-37 should be ruled in the same sitting so they ride the same regeneration rather than forcing a second one.

## Q3 — For P-33, my options, their cost, and can I rule today?

Six arms, priced in a measured table (`WAVE-A-INSTALL-SHAPE-DECISION.md` L71–77) with a stated method and denominator (39 modules; 68 `history/` references across the 30 launch-path modules). This is the best-constructed part of the whole packet:

- **(1a)** companions outside `governance/` — 30 modules move, both waves' confirmations retire.
- **(1b)** widen the `contracts/` cell — 1 module moves, Wave A retires, Wave B survives.
- **(1c)** drop the copies — 30 modules move, both retire.
- **(1d)** mint `contracts-companion/` — 1 + 30 modules move, both retire. *The most expensive arm, and the previously recommended one.*
- **(1e)** typed closed enumeration — 1 module moves, Wave A retires, Wave B survives. **Recommended.**
- **(1f)** install-time link rewriting — rejected, because it breaks `sha256sum -c` on the install.

The real trade is honest and legible: (1e) buys cheapness by keeping historical rationale inside the accepted-contract home under a name; (1a)/(1c) buy a clean type boundary at the cost of a second full re-review. The packet says so itself (L100–106): *"the honest reason is the 68 references, not a principle."*

**Could I rule today? Directionally yes; finally no.** Two things are missing. First, arm (1e) amends RFC3-15's `contracts/` cell, and **the packet never quotes that cell** — I had to find it at `rfcs/RFC-0003/governance-homes-and-owner-acts.md:86`, inside a 530-line module. Its stem (L73–81) also says the category set is *"closed except by the two lawful widenings this RFC records"* and that *"A plane validator therefore accepts exactly these six names and rejects a seventh"* — load-bearing for (1d) and absent from every cost column. Second, the replacement wording does not exist: L56 says the ceremony text "is then drafted" *after* I rule. I would be approving a direction and never seeing the bytes.

Question 2 of P-33 (the 39-row manifest) I *could* rule today: **(2b)**, generator-written banner — but only after opening the linked packet, because the top page states the question and never gives its options.

## Q4 — Which cannot be taken without information outside this repository?

- **P-39** — needs the installed and current-upstream npm versions of `@fission-ai/openspec` and a diff of their changeset formats. The packet flags this itself (L122–123) as a **pre-sitting task with cost `[Unknown]`**.
- **P-34** — needs two independent reviews that `LAUNCH-GATE-AUTHORITY-DECISION.md` L84–85 says were **"not dispatched"**, and the subsequent administration needs a reviewer outside this corpus's model family (L147).
- **P-41 / P-42** — need a commissioned fresh review on bytes that must first be frozen (packet L135).
- **P-35** — needs facts that exist only in my head (operators, hours/week, reviewer capacity, budget, horizon). Not in any repository, mine included.

## Q5 — What if I take none of them?

Nothing moves, and the packet never says so in one place — I had to assemble it. Wave A cannot be re-offered (`WAVE-A-INSTALL-SHAPE-DECISION.md` L138–141: RD-18 B2 is blocking against the act's own ceremony); Wave B follows Wave A, so it doesn't move either; no formal launch administration can be run under approved policy (P-34); no launch decision; no OpenSpec, so no Capability 1. The two standing `CONFIRM` verdicts keep aging — though per L37–39 they retire under every P-33 arm anyway, so delay costs nothing *there* and freezes everything else. The one thing that does decay: each further repair round makes the confirmed arguments staler, and RD-8's recorded lesson is that routing an owner to a stale offering *"converts act 1 from a knowing act into a surprised one."*

## Q6 — Where does the packet recommend as though already decided?

Yes, repeatedly. The recommendations are written in normative present tense, not as options:

- L78: *"**(a)** — the **Capability 1 specification owns the observable facet vocabulary**"* and L79 *"**No rollup.** Each facet exposes its constituent facts and reasons; no facet composes into a maturity or compliance score."* That is a rule, stated as a fact, before I have ruled.
- L111: *"in these words: *One OpenSpec change governs one coherent capability, or one coherent change to a capability…*"*
- L100: *"Syzygy may **propose** a root README link and never directly writes one."*
- L134–135: *"bring both into force **before** Capability 1 is authored… The specification-acceptance policy's bytes **should be** frozen after P-40 is ruled, then reviewed fresh, then repaired, then offered."* — a work order addressed to me.
- L40–41: *"That is not a reason to delay the ruling — it is the reason to batch P-31 and P-37 into the same regeneration."* — arguing me out of an option before I have considered it.
- L45: *"★ the only obstacle to offering Wave A."*

The `[Inferred]` labels and the L10–11 disclaimer do real work, and I credit them. But a disclaimer at the top does not undo eight rules written in the indicative below it.

---

## Judgment

**One sitting? No. My estimate: 3.5–5 hours of owner time for the seven that are settleable, and full settlement is impossible in any single sitting.**

What drove it: ~1,150 lines of dense normative prose to read the packet plus its eight linked packets (60–80 min at careful pace with re-reads); +15 min to find and read the RFC3-15 cell P-33 amends; +10 min to find the P-31 arm inside a 346-line contract module; +20–30 min for P-35, which is introspective drafting, not choosing; and unbounded time for P-34 (a 2,059-line instrument, whose two prerequisite reviews do not exist) and P-41/P-42 (226 lines of unlinked policy, gated behind P-40 → freeze → review → repair → offer).

**Genuinely bounded** (rulable in the sitting from what is written): **P-36**, **P-40**, **P-38**, **P-31**, **P-37** (once the six-vs-seven contradiction is resolved), **P-33** (directionally — see finding 6), and P-33's question 2.

**Open-ended research or third-party work dressed as decisions:** **P-34** (two undispatched reviews + a 2,059-line instrument), **P-41** and **P-42** (a five-step chain each, three steps of which are other people's labor), **P-39** (out-of-clone version archaeology the packet itself reclassifies as pre-work), and **P-35**, which is a blank eight-row form, not a choice among options.

**Rows that forced me to open another file to understand them:** row 3 (P-37 — the drafting-site sub-choice is invisible on the top page); row 5 (P-38 — "the alternative arm" is one of three); row 2 (P-31 — no packet at all; the queue row, then a grep into a 346-line module); row 8 (P-41/P-42 — zero file references in the entire section); row 1 (P-33 — the second question's options exist only in the linked packet); row 10 (P-34 — the review status that makes it undecidable).

**Where I had to hold more than three things at once:** the P-33 chain — arm → RFC3-15 amendment → one module's bytes move → wave-manifest digest changes → RD-31b's `CONFIRM` retires → ceremony text drafted → argument regenerates → one fresh exact-package review → offer → Wave A act, *which also ratifies P-31 and, under sub-arm (a1), P-37's vocabulary* → Wave B act. Eleven links, with two other decisions riding on link ten. And the P-41 chain at L135–138: rule P-40 → freeze bytes → commission review → repair → generate offering → perform the act → all before authoring.

**Credit where due, stated plainly:** the P-33 cost table with its denominator is decision-grade work, and I would not have understood the trade without it. The honest counter-argument at `WAVE-A-INSTALL-SHAPE-DECISION.md` L100–106 tells me when to reject the recommendation — that is unusually good practice. And the two P-34 digests **verify exactly** against the files (`05ecaa95…`, `e0167fb8…`).

---

## Findings

**1. [blocking] The one-sitting claim is false by the packet's own contents.**
`CAPABILITY-1-OWNER-DECISION-PACKET.md:3-8, 176-182`. The page says it collects rulings "so they can be settled in one sitting." But P-34's own packet (`LAUNCH-GATE-AUTHORITY-DECISION.md:84-85`) says *"This packet is therefore **prepared, not offered**"* with both required reviews *"`[Unknown]` — not dispatched"*; P-41/P-42 (L128-138) require a freeze-review-repair-offer chain; P-39 (L122-123) is *"a **pre-sitting task** with cost `[Unknown]`"*. Four of eleven cannot be settled. **Fix:** split the page into "settleable now" and "blocked — with the unblocking action and who performs it," and delete the one-sitting framing.

**2. [blocking] The top page's P-37 recommendation contradicts its own linked packet and the queue.**
`CAPABILITY-1-OWNER-DECISION-PACKET.md:78` — *"Core facets: Registered · Shape present · Human-understandable · Observable · Traceable · Reconciled. *Mission-ready* is a future extension facet, after the deferred Context/Mission contracts are accepted."* Against `PROJECT-SHAPE-FACETS-DECISION.md:9` — *"Adopt **seven independent project-shape facets**"* — and its rule 3 at L29-33: *"**Mission-ready may render `not evaluated / deferred / Unknown`** … a deferred facet renders its deferral honestly rather than waiting invisible."* `PENDING-OWNER-DECISIONS.md:191` also says *"seven independent."* These differ operationally: does Capability 1 render a Mission-ready row now, or none at all? And by the packet's own L6-7 (*"where a linked packet and this page disagree, the packet wins"*), the top-page recommendation is void as written. **Fix:** restate as seven facets with rule 3, or rule the demotion in the linked packet first and regenerate.

**3. [blocking] The exclusion list omits five open queue entries, three of them owner acts.**
`CAPABILITY-1-OWNER-DECISION-PACKET.md:164-174` accounts for P-1, C/D waves, P-29/30/32, P-12, P-14…P-28. Not mentioned anywhere on the page: **P-2** (`CONFIRM CRAFT AMENDMENT: CC-TEST-2`), **P-3** (`ACCEPT TOPOLOGY`), **P-4** (`ADOPT PROJECT OVERVIEW`), **P-5** (D3) — all live at `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:28-31` — plus **P-10**. Queue denominator: 42 entries, 35 open. **Fix:** account for every open entry with a one-line reason; explicitly say whether CC-TEST-2 is a Capability 1 prerequisite, since its two siblings are.

**4. [material] The dependency diagram attaches most rows to the wrong gate.**
`CAPABILITY-1-OWNER-DECISION-PACKET.md:21-27` draws P-36, P-38, P-39, P-40, P-41, P-42, P-35, P-34 joining one edge into "formal launch administration". Per the rows' own *Earliest gate* cells, only P-35 (L148) and P-34 (L159) gate there: P-38 gates at the Wave B act (L103), P-36 (L92), P-40 (L114) and P-41/P-42 (L137) gate spec authoring, P-39 gates the first changeset (L125). Six of eight are misplaced in the one picture an owner uses to order the work. **Fix:** draw four gates (Wave A act, Wave B act, administration, authoring) and attach each row to the gate its own cell names.

**5. [material] "Only three rows are ordered by necessity" is wrong, and names four.**
`CAPABILITY-1-OWNER-DECISION-PACKET.md:30-35` — *"Only three rows are ordered by *necessity*"* then names P-33, P-31, P-37 and P-34; and *"Everything else is ordered by cost, not by logic."* But every remaining row states a hard gate (L92, L103, L114, L125, L137, L148). Nothing on the page is purely cost-ordered. **Fix:** say "three necessity *orderings*", or drop the claim and let the per-row gates speak.

**6. [material] P-33 asks me to amend a clause cell it never quotes.**
`WAVE-A-INSTALL-SHAPE-DECISION.md:14-16` paraphrases RFC3-15's `contracts/` row; arm (1e) amends that exact cell. The text lives at `rfcs/RFC-0003/governance-homes-and-owner-acts.md:86`, and the stem at L73-81 carries *"A plane validator therefore accepts exactly these six names and rejects a seventh"* — directly load-bearing for arm (1d) and absent from the cost table's columns. The repo's own verification rule 8 requires quoting the clause. **Fix:** print the current cell verbatim next to the proposed replacement wording, and add a column for "changes a conformance requirement".

**7. [material] P-34's verification command does not run as written.**
`LAUNCH-GATE-AUTHORITY-DECISION.md:51-56` — *"Verify before acting"* followed by `sha256sum launch-gate-pre-specifications.md launch-gate-administration.schema.json`. Both files are at the repo root; the packet sits in `.syzygy/governance/decisions/`. I ran it as written and got `No such file or directory`. From the repo root both digests match the table exactly. The single step the packet insists on before an owner acts fails silently-looking for anyone who copy-pastes it. **Fix:** use repo-root-relative paths and name the required cwd.

**8. [material] P-38 collapses four options into "the alternative", and buries a substantive drafted answer.**
`CAPABILITY-1-OWNER-DECISION-PACKET.md:102` — *"The alternative arm costs one Wave B regeneration plus a two-document seam"* — but `HUMAN-ENTRY-DECISION.md:44-58` carries (a), (b), (c) and (d), and that cost is (d)'s alone. The top page also omits `HUMAN-ENTRY-DECISION.md:29-34`, where the drafting pass wrote into RFC7-39 that the fixed entry *is* the primary narrative — *"a substantive answer the pass made, not a derivation."* **Fix:** name the options; surface any answer a pass drafted on the owner's behalf on the top page, not three files down.

**9. [material] P-37's "Digest invalidated: none" is true only of a sub-arm the top page never mentions.**
`CAPABILITY-1-OWNER-DECISION-PACKET.md:80` says *"(a): none"*. `PROJECT-SHAPE-FACETS-DECISION.md:59-65` splits (a) into (a1) — *"cost: the Wave A argument regenerates and the fresh exact-package review binds the new bytes"* — and (a2). The digest column, the one column an owner scans for irreversibility, is wrong for half of option (a). **Fix:** put the (a1)/(a2) split in the row.

**10. [material] Three decisions have no linked packet at all.**
`CAPABILITY-1-OWNER-DECISION-PACKET.md:70` routes P-31 to "the queue row P-31" — a single ~250-word table cell at `PENDING-OWNER-DECISIONS.md:184`; the arm's actual bytes are at `rfcs/RFC-0002/reconciliation-chain.md:224-254`, which I found by grep. §8 (L128-138) contains **zero** file references, though both candidates exist (`contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`, 107 lines; `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`, 119 lines). I am asked to bring CC-SPEC-1…10 into force with no route to CC-SPEC-1…10. **Fix:** link all three, with line anchors.

**11. [material] The supporting analysis contradicts the packet it supports.**
`P33-SEMANTIC-INSTALL-ANALYSIS.md:100` labels (1d) *"(current recommendation)"* and L104-105 states *"The current recommendation **(1d) is the most expensive arm in the space**, and the packet does not say so."* But `WAVE-A-INSTALL-SHAPE-DECISION.md:84` recommends **(1e)**, L90 says *"The 2026-08-10 recommendation of (1d) is withdrawn"*, and L92-93 does say it is the most expensive. The same analysis then recommends (1e) at its own L149. The top page points me at this file (L58). An owner who follows that pointer reads a withdrawn recommendation presented as current. **Fix:** regenerate the analysis against the current packet; never leave a superseded arm labelled "current".

**12. [material] The status page and the packet give different marching orders.**
`PROJECT-STATUS.md:104-106` — *"Rule **P-33**… nothing downstream — Wave B's offer, the launch-gate administration, the first specification — moves until it is ruled."* Against `CAPABILITY-1-OWNER-DECISION-PACKET.md:34-35` — *"Everything else is ordered by cost, not by logic."* One tells me to do a single thing; the other tells me to batch ten. Also `PROJECT-STATUS.md:65` calls all eleven *"prepared"*, while `LAUNCH-GATE-AUTHORITY-DECISION.md:84-85` says P-34 is *"**prepared, not offered**"*. **Fix:** have the status page point at the packet's ordering rather than restate it.

**13. [minor] "Nine packets" matches nothing countable.**
`CAPABILITY-1-OWNER-DECISION-PACKET.md:179`. The page has 10 numbered sections, 11 P-numbers, and 8 linked decision packets (I enumerated its own file references). `PROJECT-STATUS.md:64` says *"Eleven rulings"*. **Fix:** compute it or drop it — this is exactly the transcribed-figure failure the repo's own rule 3 forbids.

**14. [minor] Two file references don't resolve from where the packet sits.**
`CAPABILITY-1-OWNER-DECISION-PACKET.md:65` (`RFC-0002/reconciliation-chain.md`) and `:126` (`GOVERNANCE-SUBSTRATE-LOCK.yaml`) — both use the same code-span convention as the working relative paths at L56 and L82, so I cannot tell which are paths and which are names. I confirmed both fail to resolve from the packet's directory. **Fix:** one convention, all resolvable.

**15. [minor] P-33's second question is asked on the top page and never optioned there.**
`CAPABILITY-1-OWNER-DECISION-PACKET.md:49` asks it; L51 and L52 (Options, Recommendation) cover only arms 1a–1f. (2a)/(2b) and the sharp consequence — *"(2a) does not mean 'install later' — it means 'install never, while the posture stands'"* — live only at `WAVE-A-INSTALL-SHAPE-DECISION.md:131-136`. **Fix:** one row per question.

**16. [minor] Throat-clearing, hedging, and self-grading.**
The five-line *"This file decides nothing"* disclaimer at L3-11 is repeated near-verbatim at the head of all eight linked packets — nine copies of the same paragraph in one reading path. L176-182, *"The one-sitting claim, stated as a claim"*, asserts the design goal, concedes the pass *"cannot answer [it] about its own work"*, and labels it `[Inferred]` — a section that grades its own homework while reserving credit; it should simply not be there. L45's *"★ the only obstacle"* and L40-41's *"That is not a reason to delay the ruling"* both push rather than inform. **Fix:** one disclaimer in the corpus, at the queue; delete the self-assessment; state consequences and let me choose.

---

## Missing — things I would refuse to decide without

1. **The proposed replacement text for RFC3-15's `contracts/` cell.** `WAVE-A-INSTALL-SHAPE-DECISION.md:56` says the ceremony text is drafted *after* I rule. Arm (1e) is a constitutional amendment; I would be approving a direction and never seeing the bytes that bind. Give me the current cell and the proposed cell, side by side.
2. **The two craft-policy texts** for P-41/P-42 (finding 10). I will not put CC-SPEC-1…10 into force sight-unseen, and the packet gives me no path to them.
3. **A complete act-and-decision inventory.** Eleven rulings plus — how many acts? The page says the wave acts are "not on this page", omits four more open acts entirely, and never totals what the launch path costs me. I need one table: every open entry, launch-critical or not, with a reason.
4. **For P-35, the consequence of my honest answers.** The form (`PROJECT-OPERATING-CONSTRAINTS-DECISION.md:23-32`) asks eight questions and tells me A6 becomes answerable. It does not tell me what fails if my answers are "one operator, a few hours a week, no independent reviewers" — which, per `LAUNCH-GATE-AUTHORITY-DECISION.md:107-110` (F5, *"Every administration so far has been by the corpus authors' model family"*), is very likely the true answer and the one that reshapes the project. Pre-compute that branch before asking me to fill the form.
