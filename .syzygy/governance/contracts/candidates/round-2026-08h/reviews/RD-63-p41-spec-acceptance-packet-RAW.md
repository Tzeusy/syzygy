# RD-63 — fresh-context owner-decision-packet review: P-41 specification-acceptance craft act

| Field | Value |
|---|---|
| Review ID | RD-63 |
| Date | 2026-08-16 |
| Frozen commit | `918574c` (`918574c97c29a33ed76e44b27250b557160ddcd7`) |
| Subject | `.syzygy/governance/decisions/SPECIFICATION-ACCEPTANCE-DECISION.md` |
| Subject digest (sha256, verified this session) | `effd5545bc94571d7da1112168030115baae7c135acb91db832033584119301d` — matches the commissioned digest |
| Reader posture | **Fresh context** — no prior knowledge of this corpus loaded before Phase 1 |
| Reviewer | LLM, **same model family as the corpus authors** (correlated-blindspot risk applies to this review's own findings) |
| Frozen worktree | `/tmp/claude-1000/-home-tze-GitHub-syzygy/8a4c1d91-a90d-4b95-a6ee-8a433a87fc1b/scratchpad/frozen-918574c/` — read-only; nothing edited |

Protocol: Phase 1 answers below were written after reading **only** the packet
and **before** any other file was opened. They are reproduced verbatim; where
Phase 2 later contradicted them, the correction appears in Phase 2, not by
editing Phase 1.

---

## Phase 1 — the fresh-reader test (written before opening any other file)

### 1. What is the question the owner is being asked to decide?

`[Observed]` The packet's `## Question` section opens with an imperative, not
an interrogative: *"Put a specification-acceptance standard in force before the
first spec is authored."* The thing to be put in force is named — the candidate
policy `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`, clauses
**CC-SPEC-1…CC-SPEC-10** — and its content is summarised as *"what a spec must
name, how testability is judged, and the coverage bar (CC-SPEC-8) a spec is
reviewed against."* The packet then says it *"binds nothing until its own
`CONFIRM CRAFT AMENDMENT` act."*

`[Inferred]` The decidable question in *this sitting* is narrower than the
heading, and the packet says so explicitly one section later: *"**This act is
not performable today.** … What the owner *can* do in the sitting is choose the
route below; the act itself follows the review."* So the real question is:
**by which of three routes should the first specification's acceptability be
judged — a confirmed standard (a), an unconfirmed candidate (b), or no written
standard (c)?** I had to compose that from two sections; the `## Question`
heading alone does not state it.

`[Inferred]` MINOR: a fresh reader reading only `## Question` would believe they
are being asked to perform the act today. The correction is present and
prominent (the very next heading, bolded), so the packet self-repairs — but the
question section itself is mis-stated as an instruction rather than a choice.

### 2. What are the options, and what does each cost?

`[Observed]` Three options, all with stated costs — within the required 2–4:

- **(a) Review-then-act.** *"a fresh-context review of the candidate
  (CC-SPEC-1…10), repairs disposed, then the `CONFIRM CRAFT AMENDMENT` act
  binding the reviewed digest, recorded in the craft `INSTALL-RECORD.md` per the
  CC-TEST-2 precedent."* Cost: *"one review cycle before the first spec can be
  judged acceptable; the standard is then in force and citable."*
- **(b) Author against the unconfirmed candidate,** *"recording that choice at
  the launch decision."* Cost: *"the first spec's acceptance is judged against
  text with no act behind it — the judgment binds by the owner's acceptance of
  the spec itself, not by a standard in force; a later act may then invalidate
  criteria the spec was already judged by."*
- **(c) Decline a written standard entirely;** *"judge Capability 1's
  acceptability ad hoc at its own acceptance decision."* Cost: *"launch-gate E5
  stays `Not met` on its own terms, and the second spec inherits no bar."*

`[Inferred]` The costs are asymmetrically specified. (b) and (c) get their
downside named in concrete terms (invalidated criteria; a gate criterion staying
`Not met`; no inherited bar). (a)'s cost is one clause — *"one review cycle"* —
with **no elapsed-time, sequencing, or launch-delay figure**, and it is
immediately followed by an upside clause in the same sentence. A reader choosing
between "one review cycle" and "a later act may invalidate criteria the spec was
already judged by" is not being given a like-for-like comparison. This is the
one place where I suspect the packet leans.

`[Unknown]` What "one review cycle" costs in practice — days? a sitting? two
agents? The packet gives no unit, so I cannot price (a) against (b)'s speed
advantage, which is the only reason (b) exists.

### 3. Which digests/confirmations would change under each option?

`[Observed]` A three-row table answers this per arm:

| Arm | Wave A / Wave B manifests | Confirmations | What binds |
|---|---|---|---|
| (a) | **unchanged** | **both survive** | *"the **policy file's own digest**, computed at the act (`CC-TEST-2` precedent), never transcribed in advance"* |
| (b) | unchanged | both survive | *"nothing — the spec's acceptance rests on the owner accepting the spec, not on a standard in force"* |
| (c) | unchanged | both survive | *"nothing"* |

And the summary: *"**No arm touches a contract wave.** This is craft policy:
neither manifest regenerates and neither confirmation is retired under any arm.
What differs is whether anything is in force when the first specification is
judged."*

`[Observed]` The packet also states, in `## What cannot happen in this sitting`,
that *"no ceremony phrase or digest subject is minted for it in
`ACCEPTANCE-PHRASE-REGISTRY.yaml` — the phrase is minted at the offering, after
the review, with the digest computed at the act (never transcribed in advance)."*

`[Unknown]` **Which two confirmations "both survive" refers to is never stated.**
The packet says "both survive" three times and "neither confirmation is retired"
once, but never names them. A fresh reader cannot tell what they would be
checking if they wanted to verify this row. Same for "Wave A / Wave B manifests"
— named, never located.

`[Inferred]` The digest-consequence answer is otherwise clean and genuinely
informative: the interesting content is the *negative* claim (nothing
regenerates, nothing retires), which is exactly what an owner needs to know to
rule cheaply, plus the one positive (under (a) the policy file's own digest
becomes bound, and is computed at the act — so ruling now does not freeze bytes
now).

### 4. What pre-work or review is still required — and does the packet ask the owner to approve anything currently `REVISE` or unreviewed?

`[Observed]` **Pre-work:** *"**rule `P-40` first.** `CC-SPEC-1` consumes the
granularity rule by identifier, so ruling P-40's arm (b) or (c) changes
`CC-SPEC-1`'s content without changing its text — the standard must be confirmed
against a ruled P-40, not a pending one."* This is stated twice — once as an
`## Ordering constraint (RD30-13)` section, once in the digest-consequences
block — in near-identical words.

`[Observed]` **Review:** *"one fresh-context review of `CC-SPEC-1…10`, and it
must cover the **repaired** bytes: the candidate was rewritten on 2026-08-13 and
no independent reader has seen the result. Commission it **jointly with `P-42`**
— `CC-IMPACT-1`'s spec-level declaration is generated as the union of
`CC-SPEC-2`'s six fields, so reviewing either alone leaves a dangling
generation."*

`[Observed]` **Does it ask the owner to approve something unreviewed?** No — and
it says so unusually loudly. *"**This act is not performable today.** The
candidate was authored 2026-08-10 and has had no fresh-context review; the
craft-amendment precedent (CC-TEST-2) is review-then-act."* The packet
volunteers the disqualifier in its own second section, in bold, rather than
burying it. On this criterion the packet is, on first read, exemplary: it
withholds an act the owner might otherwise have performed.

`[Inferred]` **But two statements about the review status do not sit together
comfortably.** §"What cannot happen" says the candidate *"has had no fresh-context
review."* §"Review required" says the review *"must cover the **repaired**
bytes: the candidate was rewritten on 2026-08-13."* Repairs normally follow
findings, and findings normally follow a review. Either (i) some review did occur
and produced the repairs — in which case "no fresh-context review" is at best
incomplete and the packet is silent on that review's verdict word, or (ii) the
rewrite was self-initiated with no review behind it, in which case "repaired" is
the wrong word. **A fresh owner cannot tell which, and the difference matters:**
under reading (i) there may be an outstanding `REVISE` verdict the owner is not
being shown. Flagged for Phase 2 as the single most load-bearing thing I could
not settle from the packet.

`[Unknown]` No review verdict word (`CONFIRM` / `REVISE` / `EXCEPTIONS`) appears
anywhere in the packet, for any subject.

### 5. What is the exact next transaction after a ruling?

`[Observed]` Stated, and it is a sequence rather than a single step:
*"Under (a): rule P-40; commission the joint review; disposition every finding;
freeze the bytes; then `CONFIRM CRAFT AMENDMENT` over the frozen digest,
recorded in the craft `INSTALL-RECORD.md`. The ceremony phrase is minted at the
offering, after the review — not now."*

`[Inferred]` MINOR: the next transaction is given **only for arm (a)** — the
recommended arm. If the owner rules (b) or (c), the packet says only, inside the
option text, that (b) is *"recording that choice at the launch decision"* and
gives (c) no transaction at all. A packet that tells you what to do next only if
you take the recommendation is doing a small amount of steering. Under (c) I
would not know which file records the declination, or whether launch-gate E5's
`Not met` needs a corresponding edit somewhere.

### 6. Could I rule from this packet alone, without reading any review history? Where did I get stuck?

`[Inferred]` **Qualified yes.** I could rule (a) from this packet alone with
reasonable confidence: the recommendation is marked `[Inferred]`, the reasoning
is short and checkable in principle, the act is disclosed as not-performable, and
the digest table shows the ruling is cheap under every arm (nothing regenerates,
nothing retires). The decision is genuinely low-stakes *as a ruling* — it orders
work rather than binding bytes.

`[Inferred]` **Where I got stuck — seven places, in rough descending order:**

1. **The unreviewed / "repaired" tension** (finding above). If a review exists
   with a `REVISE` verdict, the packet's central "no fresh-context review" claim
   is misleading and the honest disclosure I credited it for is weaker than it
   looks. I cannot resolve this without outside knowledge.
2. **"Both confirmations survive" — which two?** Never named, so unverifiable
   from the packet.
3. **P-40's arms are not summarised.** The pre-work says ruling P-40 (b) or (c)
   *"changes CC-SPEC-1's content without changing its text."* To feel the weight
   of the ordering constraint I need to know what (b) and (c) *are*. I cannot
   judge whether this constraint is real or decorative from the packet.
4. **CC-SPEC-8's "coverage bar" is named but not stated.** It is the clause the
   `## Question` section singles out as the bar a spec is reviewed against, and
   its content is absent.
5. **Launch-gate E5** is cited as staying `Not met` under (c). Its text is not
   given, so I cannot check that (c) really leaves it unmet "on its own terms",
   nor that (a) would satisfy it.
6. **The CC-TEST-2 precedent** is invoked three times as the reason the route is
   review-then-act and the reason the digest is computed at the act. Its content
   is nowhere in the packet; I am asked to trust an unshown precedent.
7. **Where the craft `INSTALL-RECORD.md` is** — the terminal transaction writes
   to it, and the packet gives no path (unlike the candidate policy, which gets a
   full relative path).

`[Observed]` What the packet does **not** do, to its credit: it reproduces no
review history. There is no chain of prior offerings, no superseded-rev
narrative, no list of findings. The one historical fact stated (rewritten
2026-08-13) is a single clause serving the live instruction *"the review must
cover the repaired bytes."*

---

## Phase 2 — verification against the cited corpus

*(Written after the Phase 1 answers above were fixed. Every file opened is
enumerated in the confirmation section.)*

### 2.1 Headline correction to Phase 1

`[Observed]` My Phase 1 answer 4 flagged the *"repaired"* / *"no fresh-context
review"* tension as the thing I could not settle. It resolves against the
packet, decisively, and in the direction I feared:

- The candidate's own banner (L13–15) reads: *"The delta is
  `../round-2026-08g/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA.md` … the
  findings it answers are **RD-51's**, raw at
  `../round-2026-08f/reviews/RD-51-spec-acceptance-and-impact-RAW.md`."*
- `RD-51-spec-acceptance-and-impact-RAW.md` L21 reads exactly:
  **`VERDICT: REVISE`**. It carries 20 findings, 4 of them blocking or material
  against `CC-SPEC-*`.
- The register row for P-41 (`PENDING-OWNER-DECISIONS.md` L187) states it
  correctly: *"**Amended 2026-08-13** — the candidate was repaired against
  **RD-51's 20 findings** … The repaired bytes are **unreviewed**."*

So the packet's sentence *"The candidate was authored 2026-08-10 and has had no
fresh-context review"* is **false at the frozen commit**, and it is false in the
one direction that matters: it presents the subject as *never reviewed* when it
was reviewed and returned **`REVISE`**. The word `REVISE`, the review ID
`RD-51`, and the finding count appear **nowhere** in the packet.

### 2.2 Verification table

Every row was checked against the frozen worktree at `918574c`.

| # | Packet claim (quoted) | Verified against | Result |
|---|---|---|---|
| 1 | *"The candidate was authored 2026-08-10 and has had no fresh-context review"* | `RD-51-…-RAW.md` L21 `VERDICT: REVISE`; candidate banner L13–15; `PENDING-OWNER-DECISIONS.md` L187 | **FALSE** — reviewed; verdict `REVISE`; 20 findings. See F1 |
| 2 | *"the candidate was rewritten on 2026-08-13 and no independent reader has seen the result"* | candidate banner *"**Amended 2026-08-13**"*; `DISPOSITION-REGISTER.md` *"the review has not been dispatched and **the bytes are not frozen**"* | **TRUE** |
| 3 | `CC-SPEC-1…CC-SPEC-10` exist and are *"what a spec must name, how testability is judged, and the coverage bar (CC-SPEC-8)"* | candidate L26–271; CC-SPEC-4 (testability), CC-SPEC-8 (*"Applicable contract clauses are covered or lawfully N/A"*) | **TRUE** |
| 4 | `CC-SPEC-1` reads *"one coherent capability, per the granularity rule, P-40"* | candidate L44–48: *"the clause **previously** said 'per the granularity rule, P-40'"* — removed 2026-08-13 per RD-51 f3 | **FALSE — quotes deleted bytes.** See F3 |
| 5 | *"ruling P-40 option (b) or (c) changes CC-SPEC-1's content without changing its text"* | same — this is verbatim the *repaired* defect. Current clause states the rule inline and says *"This clause may not be frozen before P-40 is ruled"* | **STALE RATIONALE, TRUE CONCLUSION.** See F3 |
| 6 | P-40 has arms (a)/(b)/(c) | `SPECIFICATION-GRANULARITY-DECISION.md` L39–44 | **TRUE** |
| 7 | *"`CC-IMPACT-1`'s spec-level declaration is generated as the union of `CC-SPEC-2`'s six fields"* | `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` L28–41: *"the **same six classes** CC-SPEC-2 defines"*, *"the union of its requirements' CC-SPEC-2 declarations, generated — never hand-authored"*; CC-SPEC-2's closed set of six (candidate L57–68) | **TRUE — exact** |
| 8 | Joint offering with P-42 is required | `PENDING-OWNER-DECISIONS.md` L187 gives **two** reasons; packet gives one | **TRUE BUT PARTIAL.** See F11 |
| 9 | *"no ceremony phrase or digest subject is minted for it in `ACCEPTANCE-PHRASE-REGISTRY.yaml`"* | sweep of the 210-line registry, `grep -E "CC-SPEC\|CC-IMPACT"` → **0 hits**; 12 entries present, none for this policy | **TRUE — swept, denominator 210 lines / 12 entries** |
| 10 | *"the phrase is minted at the offering, after the review, with the digest computed at the act (never transcribed in advance)"* | `PROCESS-GLOSSARY.md` **offer** (*"Preparing an offer is not performing it"*) and **argument** (*"the exact bytes an act binds, identified by a `sha256` digest"*); `INSTALL-RECORD.md` shows superseded arguments that *"satisfied nothing"* | **TRUE** |
| 11 | *"recorded in the craft `INSTALL-RECORD.md` per the CC-TEST-2 precedent"* | `.syzygy/governance/policies/craft-and-care/INSTALL-RECORD.md` L42–53 — CC-TEST-2's 2026-08-02 amendment recorded there, prompted by *"rev7 review 9 finding S1"* (review → amendment → act) | **TRUE for the form.** But the CC-TEST-2 *act* is itself unperformed. See F12 |
| 12 | *"Wave A / Wave B manifests … unchanged"*, *"both survive"*, *"No arm touches a contract wave"* | `WAVE-A-MANIFEST.txt` (23 lines) and `WAVE-B-MANIFEST.txt` (15 lines): `grep -F "policy-candidates"` → **0**, `grep -F "SPEC"` → **0** in both | **TRUE — swept with denominators** |
| 13 | *"both survive"* referents | `PROCESS-GLOSSARY.md` L39 (*"Waves A and B are both *confirmed* today"*) and the **retire / survive** row | **TRUE but unnamed in the packet.** See F7 |
| 14 | (c): *"launch-gate E5 stays `Not met` on its own terms"* | `launch-gate-pre-specifications.md` L404–406: *"**E5 [U]** Do acceptance criteria exist for a spec itself — how one will be judged complete, testable, and faithful…"*; `Not met` is a lawful verdict word (L143) | **TRUE**, but incomplete — a `Not met` E question blocks `READY` outright (L537–538). See F6 |
| 15 | Implied: (a) closes E5 | `DISPOSITION-REGISTER.md` f14: *"**open, and deliberately** … launch-gate E5's 'complete' limb is unclosed — 0 of 10 clauses ask whether the requirement set covers the capability it claims"*; restated on the candidate's own surface | **OVERSTATED — undisclosed residual.** See F2 |
| 16 | *"Before the first specification is authored (`FIRST-OPENSPEC-SEQUENCE.md` prerequisite row)"* | that file L84: *"P-41 specification acceptance standard in force \| Craft act \| **blocking** — candidate exists … wants review + its craft act, or the owner knowingly authors against the candidate"* | **TRUE — row exists and matches** |
| 17 | *"The fresh-context review … can be ordered now, before any other ruling"* | packet's own next transaction (*"Under (a): rule P-40; commission the joint review"*); candidate L46–47 (*"may not be frozen before P-40 is ruled"*); `DISPOSITION-REGISTER.md` (*"Charter §9.8 sequences one combined fresh-context review **after P-40 is ruled**; P-40 is not ruled, so the review has not been dispatched"*) | **CONTRADICTED — by the packet itself and by two other records.** See F4 |
| 18 | *"(Added 2026-08-13, owner charter §16.)"* | no such charter is tracked at `918574c` (`git ls-files \| grep -i charter` returns four unrelated files); RD-51 f18 named this same defect class and the policies repaired it by citing the tracked delta instead | **UNVERIFIABLE — warrant absent from the frozen bytes.** See F9 |
| 19 | No review history reproduced | packet is 101 lines; no finding list, no chain of offerings, no superseded-rev narrative | **TRUE — criterion met, and well** |
| 20 | Recommendation marked `[Inferred]` | packet L56: *"`[Inferred]` **(a)**"* | **TRUE — criterion met** |

### 2.3 Acceptance criteria, one row each

| Required element | Present? | Evidence |
|---|---|---|
| Question | **Partly** | `## Question` states an imperative, not a question; the decidable question is in the next section. F10 |
| Current authority | **Partly** | Stated as *"It binds nothing until its own `CONFIRM CRAFT AMENDMENT` act"* — the force status is given, but there is no `## Current authority` section as P-40's packet carries, and the *review* status given is false. F1 |
| 2–4 options | **Yes** | Three, at L37–52 |
| Recommendation marked `[Inferred]` | **Yes** | L56 |
| Costs | **Partly** | Every arm has a cost clause; (a)'s is unquantified and asymmetric with (b)/(c)'s. F5 |
| Digest consequences | **Yes** | Three-row table, verified accurate (rows 12–13 above) |
| Pre-work required | **Yes** | *"rule `P-40` first"* — stated twice; conclusion correct, rationale stale. F3 |
| Review still required | **Partly** | The *forward* requirement is stated well; the *backward* status is false and the open findings are hidden. F1, F2 |
| Exact next transaction | **Partly** | Given for arm (a) only. F8 |
| Does **not** reproduce review history | **Yes** | Verified — this is the packet's clearest strength |
| Does not ask approval of unrepaired `REVISE` subjects without saying so | **No** | It asks for no approval today — genuinely mitigating — but it says the subject was never reviewed, when its verdict was `REVISE` with one material finding still open **and routed to this decision**. F1, F2 |
| Comprehensible from the packet alone | **Partly** | Yes as a route-choice; no as a status assessment — the status it conveys is wrong |

### 2.4 Findings

| # | Finding | Severity |
|---|---|---|
| **F1** | **The packet states the subject has never been reviewed; it was reviewed and returned `REVISE`.** Packet: *"The candidate was authored 2026-08-10 and has had no fresh-context review."* Frozen fact: `RD-51-spec-acceptance-and-impact-RAW.md` L21, **`VERDICT: REVISE`**, 20 findings, of which f1 and f9 were blocking. The candidate's own banner names RD-51; the P-41 register row names *"RD-51's 20 findings"*. The words `RD-51` and `REVISE` appear nowhere in the packet. The 2026-08-13 update repaired half the fact — the `## Review required` block correctly says the *repaired* bytes are unseen — and left the false sentence standing two sections above it. An owner reading top-to-bottom is told the disqualifier is *"not reviewed yet"*; the true disqualifier is *"reviewed `REVISE`, repaired by the session that read the verdict, one material finding deliberately open"*. Those are different decisions. | **BLOCKING** |
| **F2** | **The one deliberately-open material finding is routed to P-41 by name, and P-41's packet does not mention it.** `DISPOSITION-REGISTER.md` f14: *"**open, and deliberately.** No clause tests a specification for **completeness against its capability**, so launch-gate E5's 'complete' limb is unclosed — 0 of 10 clauses ask whether the requirement set covers the capability it claims. The fix is a new clause, and charter §9 does not direct one; **minting an unrequested clause enlarges what the owner must approve at P-41**."* The candidate repeats it on its own surface, *"because a candidate that hides its own open findings is the failure VIS-2 names."* The packet — the owner's bounded view of P-41 — hides it. Consequence, and this is the material part: the packet's arm (c) is costed as *"launch-gate E5 stays `Not met`"*, which reads as *(a) makes E5 `Met`*. By the corpus's own record, E5's *"complete"* limb stays unclosed **under (a) too**, and the instrument forbids the halfway verdict (*"No 'partially met'… a caveat that matters makes it `Not met`"*). f15's two open limbs — *"applicable" undefined* and the circular reviewed-N/A home — are likewise undisclosed. The register asked this question at P-41; the packet does not put it to the owner. | **BLOCKING** |
| **F3** | **The packet quotes `CC-SPEC-1` text that was deleted, and gives a repaired defect as its live rationale.** Packet, twice: *"CC-SPEC-1 consumes the granularity rule by identifier ('one coherent capability, per the granularity rule, P-40') — ruling P-40 option (b) or (c) changes CC-SPEC-1's content without changing its text."* Candidate L44–48: *"(Restated 2026-08-13, RD-51 f3 — the clause **previously said** 'per the granularity rule, P-40', so its meaning would have changed with no amendment the moment P-40 was ruled differently…)"*. The clause now states the proposed rule inline and says *"if the owner rules otherwise or declines, the clause is **amended** before the craft act, not silently re-pointed."* The **conclusion** (rule P-40 first) survives on independent grounds — the clause's own *"This clause may not be frozen before P-40 is ruled"* — but the packet's stated reason is a defect that no longer exists, and the parenthetical quotes bytes that are not in the file. Verification rule 8: an anchored quotation must be of a clause that says it. | **MATERIAL** |
| **F4** | **The packet contradicts itself on when the review may be commissioned, and the loose end is the expensive one.** `## Independent work`: *"The fresh-context review of the candidate can be ordered now, before any other ruling."* `## Exact next transaction`: *"Under (a): **rule P-40**; commission the joint review."* Two other records side with the latter: the candidate (*"This clause may not be frozen before P-40 is ruled"*) and `DISPOSITION-REGISTER.md` (*"Charter §9.8 sequences one combined fresh-context review **after P-40 is ruled**; P-40 is not ruled, so the review has not been dispatched and the bytes are not frozen"*). An owner acting on the last line of the packet spends the review cycle on bytes that a P-40 (b)/(c) ruling then amends — the retired-confirmation failure the corpus's rule 10 exists to prevent, and the exact cost arm (a) was chosen to pay only once. | **MATERIAL** |
| **F5** | **The arms are not costed on comparable terms, and the asymmetry favours the recommendation.** (a): *"one review cycle before the first spec can be judged acceptable; the standard is then in force and citable"* — no elapsed time, no sequencing position, and the sentence ends on the benefit. (b): *"a later act may then invalidate criteria the spec was already judged by."* (c): *"E5 stays `Not met` … the second spec inherits no bar."* (b) is the arm whose only rationale is speed, and the packet never states what (a)'s speed cost *is*, so the one trade-off the owner is being asked to weigh is unpriced on one side. Combined with F2 — where (a)'s benefit is overstated — the presentation leans toward (a) in both directions at once. | **MATERIAL** |
| **F6** | **(c)'s cost is understated in the other direction.** *"launch-gate E5 stays `Not met` on its own terms"* omits that the readiness formula reads *"**every** E question `Met` for the named launch target"* (L537–538) — so a `Not met` E5 blocks a `READY` verdict entirely, not merely leaving one row unmet. The packet leaves a fresh reader to discover the launch-blocking consequence in the instrument. | **MINOR** |
| **F7** | **"Both confirmations survive" never names its referents.** Stated three times, plus *"neither confirmation is retired under any arm"*, with no route to `PROCESS-GLOSSARY.md`, whose **retire / survive** row and L39 (*"Waves A and B are both *confirmed* today"*) supply the meaning. The practical import is stated in plain words, so the row is usable; the term is not self-contained. | **MINOR** |
| **F8** | **The exact next transaction is given only for the recommended arm.** Under (b) the packet offers only *"recording that choice at the launch decision"* — no file named. Under (c), nothing: no record site, and no statement of whether E5's row needs a corresponding entry anywhere. A packet that tells the owner what to do next only if they take the recommendation is doing quiet steering. | **MINOR** |
| **F9** | **The packet's own warrant is absent from the frozen bytes.** *"(Added 2026-08-13, owner charter §16.)"* — no such charter is tracked at `918574c`. This is RD-51 f18's defect class verbatim (*"three amendment warrants cite a document absent from the frozen bytes"*), which the two policy candidates repaired by citing the tracked semantic delta instead. The packet carries the unrepaired instance. | **MINOR** |
| **F10** | **`## Question` is an instruction, not a question.** *"Put a specification-acceptance standard in force before the first spec is authored"* pre-supposes the answer to the choice the packet then offers. The genuine question — which of three routes — is recoverable only from `## What cannot happen in this sitting` and `## Options`. Sibling packets phrase theirs as questions (`decisions/README.md` §3: *"Where do accepted contract modules and their companions install?"*, *"`Unknown` versus `Gap` — one word or two?"*); P-41's row there is likewise a topic, *"The specification-acceptance craft amendment"*. | **MINOR** |
| **F11** | **The joint-review rationale is half the register's, and the third sequenced item is missing.** Packet: *"`CC-IMPACT-1`'s spec-level declaration is generated as the union of `CC-SPEC-2`'s six fields."* Register L187 adds the second, independent reason: *"CC-IMPACT-2's trigger set **is** CC-SPEC-2's warrant set, so accepting one alone reintroduces two blocking defects."* Neither does the packet mention **P-44** (the CC-REV-2 lagging-specification amendment), which the register says *"sequences after P-40"* as *"part of the combined CC-SPEC/CC-IMPACT review"* — so the review the owner is being asked to commission is a three-subject review, and the packet describes a two-subject one. | **MINOR** |
| **F12** | **"The precedent exists" overstates what CC-TEST-2 is.** The recommendation rests partly on *"the precedent exists"*, and CC-TEST-2 is invoked three times. The 2026-08-02 *amendment* did happen and is recorded in `INSTALL-RECORD.md`, so the precedent for the **form** is real. But CC-TEST-2's confirming act is itself act 2 of the thirteen open acts — *"the one craft amendment still needing confirmation"* (registry note), and *"no owner act has been performed in this repository at all"* (`PROCESS-GLOSSARY.md`). No craft amendment has ever completed this route end to end. | **MINOR** |

**Counts: 2 BLOCKING, 3 MATERIAL, 7 MINOR.**

### 2.5 What the packet does well — recorded so the repair does not lose it

`[Observed]` Three things are genuinely good and should survive any rewrite:

1. **It withholds an act it could have offered.** *"**This act is not performable
   today.**"* — bolded, in the packet's second section, before the options. That
   is the disclosure discipline the acceptance criteria are protecting, and it is
   why F1/F2 are disclosure failures rather than an unlawful offer: the owner is
   not being asked to bind anything today.
2. **It reproduces no review history.** No chain, no superseded offerings, no
   finding list. The single historical clause it carries (*"rewritten on
   2026-08-13"*) is load-bearing for a live instruction.
3. **Its digest table is accurate and is the useful kind of answer** — the
   negative claim, verified here with denominators: neither manifest names a
   policy-candidate file, so nothing regenerates and nothing retires under any
   arm.

### 2.6 The repair that would make this `CONFIRM`

`[Inferred]` Small and local — no new analysis is required, because every fact
needed already exists in tracked records:

1. Replace *"has had no fresh-context review"* with the register's own words:
   reviewed as **RD-51**, `VERDICT: REVISE`, 20 findings, repaired 2026-08-13 by
   the session that read the verdict, **repaired bytes unreviewed**.
2. Add the open findings the register routes here: **f14** (E5's *"complete"*
   limb unclosed, 0 of 10 clauses, open **deliberately** — and the register says
   the fix was withheld precisely so as not to enlarge what the owner approves at
   P-41, which makes it an owner question, not an editorial one), and **f15**'s
   two open limbs. Correct (c)'s cost line so it no longer implies (a) closes E5.
3. Re-quote `CC-SPEC-1` from the current bytes and re-ground the ordering
   constraint on the clause's own *"This clause may not be frozen before P-40 is
   ruled"*.
4. Delete or correct `## Independent work` so it does not contradict the next
   transaction; state the review's true sequence (after P-40, jointly with P-42
   and P-44).
5. Give (a) a cost in the same units as (b) and (c); give (b) and (c) a next
   transaction; name the two confirmations; cite the tracked delta rather than
   the untracked charter.

None of this changes the recommendation. **(a) still looks right** — and would
look right for a better-stated reason: it is the only arm under which the
standard's remaining hole (f14) is visible to a reviewer rather than absorbed
silently into the first specification's acceptance.

### 2.7 Reviewer's own limits `[Unknown]`

1. **Same model family as the corpus authors.** Anything the authoring sessions
   and I would both miss, I missed too. F1–F4 were found by cross-reading
   records, not by insight.
2. **The owner charter (§9, §9.8, §16) is untracked** and I did not read it. I
   judged the packet on its own words and on tracked records only. If §16
   prescribes the digest-consequences format, the packet conforms to a
   specification I could not open.
3. **I ran no repository check script** — no `check_governance.py`, no
   `--selftest`. Nothing in this review depends on a scripted digest beyond the
   `sha256sum` of the subject, which I ran and which matched.
4. **f14's substance is not re-litigated here.** I take the register's and the
   candidate's own statement that 0 of 10 clauses test capability completeness as
   given; I did not independently sweep the 10 clauses to confirm the count.
5. **`RD-51` was read only at its verdict line, headings and tail.** I confirmed
   the verdict word and the finding structure; I did not read all 20 findings.

---

## Confirmation — every file opened, in order

Phase 1 (packet only):

1. `.syzygy/governance/decisions/SPECIFICATION-ACCEPTANCE-DECISION.md` — the
   subject, read whole; `sha256sum` run and matched before reading.

Phase 2:

2. `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` — whole
3. `.syzygy/governance/contracts/candidates/round-2026-08f/reviews/RD-51-spec-acceptance-and-impact-RAW.md` — headings, verdict line, tail
4. `.syzygy/governance/decisions/README.md` — L1–67
5. `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` — P-41/P-42/P-43/P-44 rows and the launch-scope index
6. `.syzygy/governance/decisions/SPECIFICATION-GRANULARITY-DECISION.md` (P-40) — L29–80
7. `.syzygy/governance/decisions/SHAPE-TO-SPEC-IMPACT-DECISION.md` — listed only, not read (P-42's packet is not this review's subject)
8. `.syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` — CC-IMPACT-1/2 region
9. `.syzygy/governance/contracts/candidates/round-2026-08g/reviews/DISPOSITION-REGISTER.md` — the CC-SPEC/CC-IMPACT disposition block and its summary
10. `.syzygy/governance/contracts/candidates/ACCEPTANCE-PHRASE-REGISTRY.yaml` — swept whole (210 lines), L75–130 read
11. `.syzygy/governance/policies/craft-and-care/INSTALL-RECORD.md` — CC-TEST-2 regions
12. `.syzygy/governance/contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` — act-2 row via grep only
13. `launch-gate-pre-specifications.md` (repo root) — E5/E6 region, verdict-vocabulary rules, readiness formula
14. `.syzygy/governance/contracts/candidates/FIRST-OPENSPEC-SEQUENCE.md` — prerequisite table
15. `PROCESS-GLOSSARY.md` (repo root) — the status table and the acts/arguments/offers section
16. `.syzygy/governance/contracts/candidates/wave-manifests/WAVE-A-MANIFEST.txt` — swept, 23 lines
17. `.syzygy/governance/contracts/candidates/wave-manifests/WAVE-B-MANIFEST.txt` — swept, 23→15 lines
18. `git ls-files | grep -i charter` and `find -iname "*charter*"` — to test claim 18

Nothing in the frozen worktree was edited. No check script was run. The only
computed value I quote is the subject's `sha256`, run this session.

---

VERDICT: REVISE
