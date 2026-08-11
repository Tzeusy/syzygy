# RD-50 — Default-path human clarity, the cold reader (round-2026-08f, frozen commit `e2efda6`)

> **Provenance banner, added by the recording session — everything below the
> rule is the reviewer's raw output, copied verbatim and unedited.** The
> verdict word is copied exactly.
>
> | | |
> |---|---|
> | **Charter role** | §14 review 4 — can a technically capable newcomer meet the charter's human standard on the routed path? |
> | **Dispatched** | 2026-08-11 |
> | **Subject commit** | `e2efda6` — the whole default reading path, not a named file set |
> | **Context** | fresh — the reviewer was given the standard, a reading order, and no project history |
> | **Model family** | same family as the corpus authors. Supports repair; **is not the formal launch administration** (charter §2.15) |
> | **Verdict** | `CONFIRM WITH EXCEPTIONS` |
>
> **Disposition is not recorded here.** This file is the reviewer's bytes.

---

I have enough to answer all five questions. Writing the review record.

---

# VERDICT: CONFIRM WITH EXCEPTIONS

The routed path works. I reached all five answers in 13 files and ~1,864 lines out of a 365-file, 109,600-line corpus (1.7%), without opening `_bootstrap/`, `history/`, `HISTORY.md`, `PROCESS-LESSONS.md`, or any review round. That is the standard's hardest clause and the repo passes it decisively.

It fails one clause, three times: **"without ... resolving contradictory process records."** Three documents on the path I was routed to told me a different thing than `PROJECT-STATUS.md` about whether Waves A and B are confirmed, and about which version of the launch-gate policy the owner is being asked to approve. Two of the three carry no precedence banner, so I could not resolve them mechanically — I had to go check the artifact myself.

---

## Reading path (in the order I actually took it)

| # | File | Lines | Verdict |
|---|---|---|---|
| 1 | `/home/tze/GitHub/syzygy/README.md` | 142 | unavoidable |
| 2 | `/home/tze/GitHub/syzygy/.syzygy/intent/OVERVIEW.md` | 263 | unavoidable |
| 3 | `/home/tze/GitHub/syzygy/.syzygy/governance/doctrine/README.md` | 81 | unavoidable |
| 4 | `/home/tze/GitHub/syzygy/.syzygy/governance/doctrine/vision.md` | 245 | unavoidable |
| 5 | `/home/tze/GitHub/syzygy/PROJECT-STATUS.md` | 154 | unavoidable |
| 6 | `/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/README.md` | 74 | unavoidable |
| 7 | `…/candidates/HOW-TO-AUTHOR-A-SYZYGY-SPEC.md` | 88 | unavoidable |
| 8 | `…/candidates/FIRST-OPENSPEC-SEQUENCE.md` | 102 | unavoidable |
| 9 | `/home/tze/GitHub/syzygy/.syzygy/governance/doctrine/v1.md` | 130 | unavoidable — **and I found it late, by accident** |
| 10 | `…/decisions/PENDING-OWNER-DECISIONS.md` | 208 | necessary; ~55% is history I did not need |
| 11 | `…/decisions/WAVE-A-INSTALL-SHAPE-DECISION.md` | 152 | unavoidable for Q2 |
| 12 | `/home/tze/GitHub/syzygy/CONTRIBUTING.md` | 93 | unavoidable |
| 13 | `…/candidates/TASK-ROUTER.md` | 132 | unavoidable — the best routing artifact here |

**13 files read in full, 1,864 lines.** Partial: `FORMAL-CAPABILITY-1-LAUNCH-PACKET/README.md` (~40 of 186), `launch-gate-pre-specifications.md` (header only, ~20 of 2,059). Total ~1,924 lines.

Nothing on this path was history I did not need except the changelog stack inside `PENDING-OWNER-DECISIONS.md`. That is a genuinely good result and I want it recorded as clearly as the findings.

---

## Q1 — What is this project FOR?

Syzygy is meant to be a local-first daemon plus browser app that sits beside your other repositories and keeps three things that most tools blur into one deliberately separate: **what you said should be true** (doctrine and specs you approved), **what is actually true** (code, tests, CI, runtime, captured as durable evidence), and **what was merely done** (work items, runs, merges). It computes the difference between the first two and refuses to let the third stand in for either — a merged PR is a fact about activity, not proof the intent was met. The user is one person running fleets of AI agents across a portfolio, whose actual complaint is that an orchestration day ends with big diffs and no account of what changed or whether it matched intent. Syzygy's answer is to make that account computable and to render "I don't know" as a first-class, colored, reasoned answer rather than a green check. Agents are a co-equal consumer — the same truth is served over machine-queryable endpoints, and scraping a rendered table is explicitly not a conforming integration.

## Q2 — Lifecycle stage and the single next lawful step

**Final pre-specification.** No application code, no `openspec/`, no backlog, no chosen language/framework/database. Adopted doctrine + owner-approved engineering policy exist; a 39-module candidate contract corpus exists but **no owner acceptance act has ever been performed** (`.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` does not exist, and its absence is the correct state).

**Single next lawful step:** rule **P-33** — the Wave A installation shape. Packet at `/home/tze/GitHub/syzygy/.syzygy/governance/decisions/WAVE-A-INSTALL-SHAPE-DECISION.md`. Nothing downstream moves until the owner picks one of six arms (1a–1f). `PROJECT-STATUS.md:102-109` states this unambiguously, and the packet's own cost table (lines 71-82) is the clearest piece of decision writing in the repository.

## Q3 — One file to learn whether a decision has been made

**`/home/tze/GitHub/syzygy/.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`** — every P-n row states whether it is open and names the record that owns the detail.

**How I learned that:** not from `README.md`. README line 118 lists it as item 6 under "what the owner has not yet decided," which reads as a to-do list, not as the decision register. I only learned it was *the* register from `PROJECT-STATUS.md:66` — *"the queue that owns them is …/PENDING-OWNER-DECISIONS.md"* — and from the file's own line 47, *"That file decides nothing and this one still owns the queue."*

**Caveat I have to state honestly:** it is not *one* file. Decided things live in at least four places — `SURFACE-DECISION-RECORD.md` (SDR-1…33), `OWNER-ANSWERS-2026-08-01.md`, the doctrine amendment log in `doctrine/README.md:7-9`, and the not-yet-existing `ACCEPTANCE-ACT-RECORD.md`. The `decisions/` directory has **no index file**, so a reader who clicks README's link lands on a bare listing of 16 filenames with no guide.

## Q4 — What may I NOT do, and where is that stated

Stated in three places, consistently:

- `README.md:126-133` — nothing is implemented; stack choices require an accepted contract.
- `CONTRIBUTING.md:11-17` — *"Nothing in this repository may add application or library code, choose a stack, create behavioral-specification changesets, or build an implementation backlog until the foundational contracts are accepted and specification authoring formally opens."*
- `HOW-TO-AUTHOR-A-SYZYGY-SPEC.md:82-88` — `openspec/` is created by the owner-authorized first changeset and by nothing else, *"including this file's."*

Also: no license exists, so no external code contribution can be accepted (`CONTRIBUTING.md:3-9`). And no one may accept contracts or adopt doctrine on the owner's behalf (VIS-4).

This was the easiest question in the set. The prohibition is repeated at every door without contradicting itself once.

## Q5 — If I had to author the first specification tomorrow

**Reading order** (this is the repo's own route, and it holds up):

1. `…/candidates/HOW-TO-AUTHOR-A-SYZYGY-SPEC.md` — the five authorities: form (P-39), home (RFC-0003/0004), granularity (P-40), acceptance authority (VIS-4), change process (CC-REV-2).
2. `…/candidates/FIRST-OPENSPEC-SEQUENCE.md` — Capability 1's six behaviour rows and its prerequisite state table.
3. `…/candidates/TASK-ROUTER.md:111-122` — the "Author Capability 1" route, which names the exact five modules to load and the eleven blocking decisions.
4. The five named RFC modules (RFC-0001, RFC-0003 manifests, RFC-0002 rendering vocabularies, RFC-0007 rendering-and-surface, RFC-0008 state-vocabulary).
5. `…/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` — CC-SPEC-1…10, the acceptance bar.
6. `…/round-2026-08e/FIRST-SPEC-TRACE-TABLE.md` — concept-to-clause trace.

**What blocks me:** everything. Eleven owner rulings, none made — P-33, P-31, P-36, P-37, P-38, P-39, P-40, P-41, P-42, P-34, P-35 — plus the Wave A and Wave B acceptance acts themselves. `FIRST-OPENSPEC-SEQUENCE.md:75` states it plainly: *"Nothing is `satisfied` and nothing is `owner-waived` today."*

The count **11** appears identically in `PROJECT-STATUS.md:70-82` and in `TASK-ROUTER.md:119` (where it is generator-verified against the queue). That agreement is the strongest consistency signal I found anywhere in the repository.

The single most interesting blocker: **P-37**. `FIRST-OPENSPEC-SEQUENCE.md:66` says the facet vocabulary Capability 1 must render *"is drafted **nowhere**"*, and `TASK-ROUTER.md:122` confirms by measurement: *"it appears in zero of the 30 Waves A+B modules."* The first spec is blocked on vocabulary that does not exist yet, and the repo says so out loud rather than hiding it. That is the doctrine working.

---

## Findings

**1. [blocking] The decisions register renders as broken markdown for 20 of its 22 open rows.**
`…/decisions/PENDING-OWNER-DECISIONS.md`, blank lines at 167, 170, 172, 174, 176, 179, 181, 187.
The last table delimiter row in the file is line 157. Eight blank lines after it split the "Open, and only the owner can dispose" table into nine fragments. Under GFM a table requires a header plus a delimiter row, so fragments 2–9 — rows **P-21 through P-42**, which is every launch-critical decision including P-33, P-34, and P-36 through P-42 — render as literal pipe-delimited paragraphs, not a table. `[Inferred]` — I verified the delimiter positions mechanically but could not render GitHub here.
This lands on Q3 directly: the one file that owns "has this been decided" is visually unreadable for exactly the rows that matter.
**Fix:** delete the eight blank lines. One-line change; no content moves.

**2. [material] Three documents on the routed path say Waves A and B are not confirmed; `PROJECT-STATUS.md` says they are.**

> `PROJECT-STATUS.md:29` — *"Wave A (RFC 0001–0006, 19 modules) | **Confirmed** — `VERDICT: CONFIRM` on the current argument `8972d963…` (RD-31b)."*

> `…/candidates/README.md:21-23` — *"the Wave A/B repair batches landed at round-2026-08e and **await fresh exact-package reviews before the acts may be offered**."*

> `…/candidates/FIRST-OPENSPEC-SEQUENCE.md:59` — *"Wave A act performed at a confirmed argument | Owner act | **blocking** — repairs landed this pass; fresh exact-package review then the offer"*

> `…/candidates/README.md:18-20` — *"the round-2026-08d review pass delivered fifteen fresh-context reviews, **all fifteen `REVISE`, zero `CONFIRM`**"* — presented under the heading **"Current state (2026-08-10, launch-closure pass)"**.

`candidates/README.md` is where README.md item 4 lands a reader. Neither it nor `FIRST-OPENSPEC-SEQUENCE.md` carries the *"where this file and the owning record disagree, the record wins"* banner that `PROJECT-STATUS.md:6-7` and `PENDING-OWNER-DECISIONS.md:6-7` both carry — so I had no mechanical way to resolve the conflict and had to go verify against the queue myself. That is precisely what the standard forbids.
**Fix:** the precedence banner on both files, plus a dated state line. Both are one day stale, not wrong in kind.

**3. [material] `P-34` asks the owner to approve a version of the launch gate that no longer exists.**

> `…/decisions/PENDING-OWNER-DECISIONS.md:188` — *"approve `launch-gate-pre-specifications.md` **v1.18** as the owner-approved process policy"*

> `PROJECT-STATUS.md:32` — *"Launch-gate policy | **Candidate v2.0** — structured-record migration. Owner approval is **P-34**"*

> `launch-gate-pre-specifications.md:7` — `effective_version: v2.0 (candidate; v1.3 was the pilot-administered version)`

The register that "owns the queue" names a superseded subject for the decision. `FIRST-OPENSPEC-SEQUENCE.md:70` sidesteps it with *"current version per the instrument's own header; RD34-05"* — a workaround that proves the register was known to go stale and was left to.
**Fix:** stop writing the version number into the row; cite the instrument's header, as the sequence file already does.

**4. [material] The repo's own 48-check battery reports 0 FAIL and catches none of findings 1–3.**
I ran `python3 scripts/check_governance.py` read-only: `30 OK, 18 WARN, 0 FAIL`. A newcomer told that "the battery is clean" (`PROJECT-STATUS.md:136-138`) would reasonably infer the corpus is internally consistent. It is not, on the front-door path.
**Fix:** a currency check — any file asserting a wave/gate state must either match `PROJECT-STATUS.md` or carry the precedence banner.

**5. [material] The one document that says what the software would actually do is not linked from the front door.**
`README.md` "Start here" (lines 98-124) lists eight destinations. `.syzygy/governance/doctrine/v1.md` is not among them, and the string `v1.md` appears zero times in `README.md`. Yet v1.md is the only file that says V0 ships portfolio truth, 3D spatial code visualization at project→capability→component granularity, work-dependency graphs, machine-queryable endpoints, and a three-axis propagation proof-of-concept. I reached it on hop nine, via `OVERVIEW.md:144`.
**Fix:** add v1.md to "Start here" as item 3, between vision.md and PROJECT-STATUS.md.

**6. [material] `PENDING-OWNER-DECISIONS.md` makes the reader read the governance history it is supposed to spare them.**
Lines 9-63 are 55 lines of nested `as-of` / *"Previously as-of"* / *"Later on"* blocks before the first content. The **P-34 cell alone (line 188) is 1,283 words / 8,593 characters in a single table cell** — a chained narrative of v1.4→v1.18 with every reviewer finding inline, including sentences like *"a `>` inside a quoted attribute value defeated the whole hiding enumeration."* P-21 is 464 words; P-28 is 310.
`PROJECT-STATUS.md` already solved this — it moved its chronology to `decisions/launch-gate/HISTORY.md` and says so at lines 9-13. This register did not follow.
**Estimate:** 208 → ~90 lines. Each row becomes question / owning record / earliest gate. The litigation history moves to `launch-gate/HISTORY.md` (P-34) or to each decision's own packet file, which already exist for P-33, P-36, P-37, P-38, P-39, P-40, P-41.

**7. [minor] `decisions/` has no index.**
`README.md:88` links `.syzygy/governance/decisions/` as *"Prior owner rulings — Recorded."* The directory has 16 `.md` files and one subdirectory and **no `README.md`**. A reader who follows that link gets a filename listing and must guess. Every other governed directory I visited has one.
**Fix:** a ~25-line `decisions/README.md` — pending queue here, surface rulings there, doctrine amendments in the doctrine log, acts in the (not-yet-existing) act record.

**8. [minor] Terms used before they are defined, at the line where it happened.**

| Term | First use | Defined? |
|---|---|---|
| "agent fleets" | `README.md:4` | never formally; inferable |
| "final pre-specification" | `README.md:7` | never defined as a stage anywhere; the name has to be taken on faith |
| **"act"** / "owner act" | `README.md:11` | **never defined on the routed path.** I inferred from `OVERVIEW.md:6` (`ADOPT PROJECT OVERVIEW: <digest>`) that it is a literal phrase the owner types binding a digest. This is the single most load-bearing concept in the repository and I had to reverse-engineer it |
| `openspec/` | `README.md:92` | `doctrine/README.md:40` — one hop later |
| `VIS-1`, `SEC-4`, `D2`, `D3`, `RFC-0010` | `README.md:40,58,87,89` | scheme explained at `doctrine/README.md:45` |
| "kernel" | `README.md:54` | `OVERVIEW.md:68` |
| **`P-33`, `RD-31b`, `RD-32c`, "argument", "the offer", "install shape"** | `PROJECT-STATUS.md:29` | **none defined anywhere I was routed to.** "Argument" (= the sha256 an act binds) I inferred from `candidates/README.md:33`. `RD-nn` I inferred to be review IDs |
| `E1`…`E6` | `HOW-TO-AUTHOR-A-SYZYGY-SPEC.md:11,21,41,50,75` | never; inferred as launch-gate question IDs |
| "wave" | `PROJECT-STATUS.md:29` | never defined; inferable as a bundle of RFCs accepted by one act |
| *actuator*, *actuator toolchain* | `vision.md:38` | **the repo already knows** — logged as P-25(c), `PENDING-OWNER-DECISIONS.md:177` |

The `README.md:100-107` "Unfamiliar word?" pointer only covers the seven-entry doctrine glossary and the candidate term registry. Neither carries `act`, `argument`, `wave`, `offer`, or `P-n`. Those are process vocabulary, and process vocabulary has no glossary.

**9. [minor] A riddle where a definition belongs.**
`OVERVIEW.md:116` — *"(Doctrine has a name for that corpus; Drawer 2 says where to find it.)"* The name is **Project Genome**, and it is 131 lines away at line 247. This is the one place in the front-door corpus where the writing chose cleverness over telling me the thing. **Fix:** name it inline.

**10. [minor] A 2,059-line internal process instrument sits in the repository root.**
`/home/tze/GitHub/syzygy/launch-gate-pre-specifications.md` — 127 KB, the second-largest thing a newcomer's `ls` shows, never mentioned in `README.md` (zero hits for "launch-gate"). Same for the root directory `FORMAL-CAPABILITY-1-LAUNCH-PACKET/`. Both are legitimate artifacts; neither belongs in the first thing a stranger sees.
**Fix:** move under `.syzygy/governance/policies/` and `.syzygy/governance/decisions/launch-gate/`, or name them in README's authority table.

**11. [minor] The sealed launch packet is bound to a commit five behind HEAD.**
`FORMAL-CAPABILITY-1-LAUNCH-PACKET/README.md` binds `5c3013f0…`; HEAD is `e2efda65…`. I verified the bound artifact is unaffected — `launch-gate-pre-specifications.md` hashes to `05ecaa95…` at both commits — so nothing is broken. But a reviewer following the packet's *"verify every digest before you begin"* at HEAD will find a commit mismatch and must work out for themselves that it does not matter.

**12. [not a defect — recorded as a positive] Zero marketing language on the front door.**
I swept `README.md`, `PROJECT-STATUS.md`, `OVERVIEW.md`, `CONTRIBUTING.md`, and `vision.md` for *rigorous / world-class / unprecedented / elegant / meticulous / robust / seamless / powerful* and the like. **Zero hits.** `README.md:128` opens the "What is not implemented" section with the single word *"Everything."* `PROJECT-STATUS.md:97` volunteers *"One thing this project does not have, stated plainly."* `WAVE-A-INSTALL-SHAPE-DECISION.md:84-106` withdraws its own prior recommendation, says why it was wrong, and then argues against its replacement under the heading "Honest counter-argument to the recommendation." I went looking for self-congratulation and did not find any. The nearest thing to hedging is finding 9's riddle.

---

## Where I had to guess

1. That an "act" is a literal phrase the owner types, binding a named digest. Never stated; inferred from `OVERVIEW.md:6`.
2. That an act's "argument" is the sha256 of a manifest file. Inferred from `candidates/README.md:33`.
3. That `RD-nn` are review identifiers and `P-nn` are pending-decision identifiers. The `P-` scheme is inferable from the register's shape; `RD-` is never explained.
4. Whether Waves A and B are confirmed. I resolved it in `PROJECT-STATUS.md`'s favor because it is dated one day later and carries the precedence banner — not because any document told me to.
5. Whether P-34 asks about v1.18 or v2.0. I checked the instrument's own header to settle it.
6. That "final pre-specification" means "doctrine adopted, contracts drafted, nothing accepted." No file defines the stage name.

---

## What the software would actually DO for a user

**Confidence: moderate-high on shape and behaviour; low on interaction detail; zero on stack.**

You point it at a repository you own and register it as a governed project. It writes a `.syzygy/` directory beside your code and reads — never writes — everything else. From then on it answers three questions from one shared model:

- **Polaris:** what is this project supposed to be? Rendered from doctrine and specs you approved, so it is your stated intent read back to you, not a summary of your code.
- **Trajectory:** what remains, what is running, what changed, what did it cost — and *has the result been verified against the intent that authorized it?* That fifth question is the whole product. Every merged change sits visibly `reconciliation-pending` until it has been checked against the exact revision of the intent that authorized it, and the four possible answers — reconciled with evidence / merged but not evaluated / evaluated and unsatisfied / evaluated with a contradiction raised — must never share a rendering. At V0 the honest answer for all merged work is the second one, and the doc says a wall of pending states is *correct output, not failure*.
- **Orrery:** a 3D spatial map of the codebase at project → capability → component → source/test granularity, where capability names come from your own declared artifacts and code mapping to no declared capability renders **Unknown** rather than being quietly inferred into something. Unknown is a first-class color.

Point it at a project with no declared artifacts and it renders almost entirely Unknown — and that is stated as the correct output. Its first move on such a project is to *draft* doctrine and shape documents into `.syzygy/governance/` for you to sign off; drafted is rendered as unadopted until you do.

Everything the owner sees is equally available to agents over machine-queryable endpoints — that is mandatory at V0, not an export. Agents do detailed work only inside a **Mission**: one bounded job carrying an objective, permissions, budget, time limit, an evidence bar, and stop conditions it cannot widen itself. The loop is human-triggered throughout. It never writes implementation code; it writes only inside `openspec/**` and `.syzygy/**`, and touches git, CI, and your issue tracker only through typed, explicitly authorized adapters.

The one-sentence version: **it is the thing you open at the end of an agent-fleet day to find out what actually changed, under whose authority, and whether it matched what you asked for — and it tells you "I don't know, and here is why" rather than showing you green.**

**Why my confidence is not higher:** I know what it displays and what it refuses to display, but nothing about *how*. There is no UI specification, no schema, no API shape, no chosen language, framework, database, or graph store — deliberately, all of it gated behind contracts that have not been accepted. The three surfaces are described by charter and doctrine, never designed. I can tell you what Orrery must never do (roll facets up into a composite badge, render Unknown as green) far more precisely than what it looks like.

I want to record, though, that being able to write the paragraph above at all is the answer to the question this review was actually asking. The concern behind "this project claims to be about a product, not only about governance" is that the governance has eaten the product. **It has not.** The product is legible from `vision.md`, `v1.md`, `OVERVIEW.md`, and Capability 1's six behaviour rows in `FIRST-OPENSPEC-SEQUENCE.md:30-37`. What has gone wrong is narrower and more fixable: the *process* record around the product — the wave states, the P-34 subject, the register's rendering — has accumulated faster than its maintenance, and three files on the front-door path are a day behind the two that are current.

---

## What I still do not know after reading everything I was routed to

1. **What an owner act physically is.** Does the owner type a phrase into a terminal? Commit a file? Sign something? `ACCEPTANCE-PHRASE-REGISTRY.yaml` and `OVERVIEW.md:6` imply a literal phrase plus a digest, but I never read the ceremony. `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` (581 lines) owns it and nothing routed me there — I found it only in a directory listing.
2. **What a Syzygy specification looks like.** I know who owns each authoring question and what would make one acceptable in the abstract, but I have never seen one, and P-39 (which OpenSpec, what form) is unruled. There is no example, not even a sketch.
3. **What the seven project-shape facets are.** Capability 1's central behaviour, and `TASK-ROUTER.md:122` measured that they appear in zero of the 30 launch-path modules. They exist nowhere. P-37 decides who drafts them.
4. **Why the launch gate needed 18 revisions.** The P-34 cell narrates it in exhausting detail — HTML-hiding carriers, CommonMark start conditions, quoted attribute values — but never says at the top what the instrument *is* or why validating a readiness record turned into an adversarial parser problem. I read 1,283 words about the fight and learned nothing about the thing being fought over.
5. **Whether the repo's own doctrine has ever been tested against a real codebase.** `v1.md:60-62` names "the owner's other live projects" as the proving ground and explicitly says self-observation of the Syzygy repo is not the credibility test. Nothing tells me whether any of the design survived contact with one.
6. **When any of this happens.** P-35 is the row for operating constraints and it is unruled — the pilot found *"zero resource statements in 281 files."* One operator, no dates, no capacity, no horizon. Honest, and completely opaque.
