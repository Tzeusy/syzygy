# RD-29 — Human-language review (round-2026-08e, frozen commit eb7e486)

## 1. Subject identification

**Subject.** The frozen clone at
`/tmp/claude-1000/-home-tze-GitHub-syzygy/3fa62952-e192-440e-8b1f-5b48212d8da1/scratchpad/clone-08e-r5`,
verified at HEAD `eb7e486` ("round-2026-08e: the RD-28 spec-authoring repair batch — the
authoring path stops improvising"), working tree clean. Every claim below binds those bytes
and no others. I read nothing outside this clone and did not consult the live repository.

**Charter role.** Human-language reviewer — the cold reader. The launch target under review is
Capability 1 (Waves A+B; C1/C2/D1/D2 deferred). My experience of reading the entry path is the
evidence; where I stumbled, I recorded the stumble before resolving it.

**Register position.** `round-2026-08e/reviews/DELIVERY-AND-VERDICT-REGISTER.md:31` lists RD-29
as "Human-language reviewer · README, overview, doctrine entry path, task routing · not yet
dispatched". This document is that review.

## 2. Method

**Reading order** (a newcomer's, per charter, first pass with no lookahead):

1. `README.md` (134 lines) — read start to finish, noting each unresolved term at the line it
   appeared.
2. `.syzygy/intent/OVERVIEW.md` (261 lines) — including both drawers.
3. `AGENTS.md` (219 lines).
4. `.syzygy/governance/doctrine/README.md` (81 lines), then `doctrine/vision.md` (245) and
   `doctrine/security.md` (60) as the entry's reading order directs.
5. `PROJECT-STATUS.md` (180 lines).
6. `contracts/candidates/TASK-ROUTER.md` (119 lines) and the `AGENTS.md` routing table — six
   routes followed to their named destination.
7. `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` (160 lines), read as the owner
   would: once, in order, asking "what am I being asked to do, in what order, at what cost?"

**Second pass — verification.** Everything load-bearing was checked against the bytes with
Python `re` or `git grep -F`, never a bare pattern (rule 1). Specifically:

- **Existence sweep of path references.** Extracted every backticked token ending in
  `.md/.txt/.yaml/.py/.json` from the five entry-path files (README 10, AGENTS 28,
  PROJECT-STATUS 27, OVERVIEW 10, PENDING 79 tokens) and resolved each against four candidate
  bases. Every unresolved token was then inspected by hand; all but the ones reported in
  RD29-09 are ellipsis shorthand (`…/round-2026-08d/…`) or same-directory relative names that a
  human resolves correctly.
- **Counts recomputed, never transcribed** (rule 3): wave manifest rows (A 19, B 11, C1 2, C2 1,
  D1 5, D2 1 = 39) against `ACTIVE-CONTRACT-MANIFEST.txt` (39 rows) — the six waves partition
  the active set exactly; `SDR-` identifiers in `SURFACE-DECISION-RECORD.md` (33 distinct, max
  33); doctrine glossary bullets (7); context-selection fixtures (10, numbered 1–10); 08d review
  raw files (15, RD-9…RD-23); 08e review raw files (5, RD-24…RD-28).
- **Claims spot-verified in their owning records**: the launch-gate pilot's
  `GATE VERDICT: NOT READY` and its "31 questions asked (A×6, B×5, C×6, D×4, E×6, F×4) = **17
  Not met** + 12 Me[t]…" line, and that E1–E6 are each rendered **Not met**; the craft act-2
  argument in `INSTALL-RECORD.md` and in acceptance record §1 row 2; the `doctrine-adopted-2026-07-30`
  tag present in the clone; VIS-1/VIS-2 text at `vision.md:82`/`vision.md:96`.
- **Register measurements with denominators** (rule 9): of the 30 open rows in
  `PENDING-OWNER-DECISIONS.md`, 5 state an "Earliest gate", 4 carry a recommendation, 2 mention
  "Capability 1", 0 are marked deferred, and the string `DEFERRED-WAVE-POSTURE` occurs 0 times
  in the file. Open section = 3,751 words; longest single row = 346 words (P-21).
- **Term sweeps**: `\bact 1\b` — AGENTS.md 3, PENDING 6 (plus one capitalized "Act 1" at
  PENDING:118 that the case-sensitive sweep does not count), PROJECT-STATUS 0, README 0,
  OVERVIEW 0.
- **One bounded absolute-claim sweep** over all 315 tracked `.md` files (denominator stated) for
  `convergen*|regenerat*`: 133 files match. That figure measures *usage*, not capability claims —
  I found no counterexample to README:124 and I do not assert there is none. See RD29-10.

**Labels.** [Observed] = I read the bytes or ran the sweep this session. [Inferred] = my reading
of what a cold reader would conclude. [Unknown] = not measured.

I edited and created nothing. Read-only throughout.

---

## 3. Findings

### RD29-01 — BLOCKING — The owner's decision register routes act 2 to the retired digest block

`decisions/PENDING-OWNER-DECISIONS.md:74`:

> `| P-2 | **Act 2** — confirm craft amendment CC-TEST-2 | acceptance record §1 row 2; digest block in `../policies/craft-and-care/INSTALL-RECORD.md` (2026-08-05 correction) |`

The 2026-08-05 correction block is the **superseded** one. `INSTALL-RECORD.md:69` carries
`3858820f64768ef20e6514fe8adb28076263f071ac77e66a5520a612f3bcb26d  testing-and-verification.md`,
and `INSTALL-RECORD.md:72-74` says of it:

> "The pending craft-confirmation act (act 2) therefore then bound the now-superseded
> `CC-TEST-2@3858820f…` (the amended `testing-and-verification.md` above; **superseded
> 2026-08-06**, below)"

`INSTALL-RECORD.md:109-111` names the live argument
`CC-TEST-2@7a716090bc827121b3f70c4f7e252fc5680cd8a56d7b4121b70f3673489690a0` and states that
"the previously offered, now-stale `CC-TEST-2@3858820f…` argument satisfies" nothing. The
acceptance record agrees — §1 row 2 (line 28) carries `7a716090…`. `PROJECT-STATUS.md:42` gets
it right and says so explicitly:

> "`INSTALL-RECORD.md` **2026-08-06** correction block — the 2026-08-05 block holds the retired
> `3858820f…` argument (review RD-8, finding S11)"

So two documents on the owner's default path give opposite pointers for the same act, and the
one that is *named for the owner's decisions* points at the block the status page flags as
retired. [Observed] This is the RD-8 shape verbatim — "the finding that converts act 1 from a
knowing act into a surprised one" (`AGENTS.md:62-63`). Mitigations exist and are real: the row's
first pointer (acceptance record §1 row 2) is correct, and the section head at
`PENDING-OWNER-DECISIONS.md:67-69` mandates CG-7 verification before acting. They reduce the
probability, not the defect. A one-word fix ("2026-08-06 correction") closes it.

### RD29-02 — BLOCKING — The status page's gate table and launch path omit the specification-acceptance craft act (P-41), which the register calls a blocking Capability 1 prerequisite

Sweep of `PROJECT-STATUS.md` (whole file, 180 lines, denominator = the file): `CC-SPEC` 0
occurrences, `P-41` 0, `SPECIFICATION-ACCEPTANCE` 0, `spec-acceptance` 0. [Observed]

Yet `PENDING-OWNER-DECISIONS.md:150` says:

> "| P-41 | **The specification-acceptance craft act** … `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`
> (CC-SPEC-1…10) is the sole named owner of launch-gate E5 and **a blocking Capability 1
> prerequisite**, yet until this row existed it had no queue entry, no act row, and no presence
> in the craft cluster it mints into — the owner had no route to satisfy the prerequisite"

and `AGENTS.md:50` carries it as one of the eleven open acts ("Craft 2 (P-41) | The
specification-acceptance standard CC-SPEC-1…10"). The craft cluster now carries a pointer too
(`INSTALL-RECORD.md:127-135`, "Pending candidate — recorded 2026-08-10").

The page that does *not* carry it is the one the corpus designates as the single answer to
"what is the current gate state" — `OVERVIEW.md:5` ("Current gate state is read from
`PROJECT-STATUS.md`, never from here"), `AGENTS.md:80`, `TASK-ROUTER.md:107`. Its twelve-row gate
table (lines 33–49) has no row for it, and its "Next lifecycle step" (lines 130–142) enumerates
the Capability 1 path —

> "then the per-wave owner offers (acts on Waves A and B only), the launch-gate formal
> administration under the owner-approved instrument (P-34 first), and the owner's launch
> decision"

— naming P-34 but not P-41. [Inferred] An owner planning the launch from this page plans a route
with a stated prerequisite missing from it. The same omission repeats one step off README route
4: `contracts/candidates/README.md`'s layout table describes `policy-candidates/` as "(term
registry, knowledge-hygiene policy, semantic-delta workflow)" — three of the eight files in that
directory, omitting the launch-blocking one.

[Unknown] I did not verify P-41's own claim that the candidate is "the sole named owner of
launch-gate E5" — `launch-gate-pre-specifications.md` contains no occurrence of `CC-SPEC` or
`SPECIFICATION-ACCEPTANCE`; the ownership is asserted from the policy candidate's side
(`SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md:5,8`) and by RD-28. The gate-table omission stands
regardless of how that resolves.

### RD29-03 — MAJOR — Three entry-path pages enumerate three different sets of open owner acts, and no page carries the union

[Observed], all at this commit:

| Page | Enumeration | Set |
|---|---|---|
| `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1 (lines 22–31) | 10 act rows | A, B, C1, C2, D1, D2, 2 (craft CC-TEST-2), 3 (topology), 4 (overview), 5 (D3) |
| `AGENTS.md:36-53` | "**Eleven acts are open**" | the above 10 **plus** Craft 2 / P-41 — **minus** nothing |
| `PROJECT-STATUS.md:33-49` | 12 gates | includes gate 9 "Knowledge-hygiene craft policy — ⏳ **Candidate — own craft act**" and gate 10 License; **excludes** P-41 |

The knowledge-hygiene craft act is a real open act — `PENDING-OWNER-DECISIONS.md:114`: "**Knowledge-hygiene
craft policy** — needs its own `CONFIRM CRAFT AMENDMENT` act" — and it is absent from AGENTS.md's
act table, which is the table that carries the count. Taking the union, twelve acts are open (six
waves + CC-TEST-2 + knowledge-hygiene + spec-acceptance + topology + overview + D3), so
`AGENTS.md:36`'s "Eleven acts are open" is a computed-sounding figure that no page's enumeration
supports. [Inferred] A newcomer who trusts the act table — the stated purpose of that section —
will not learn that two of the open craft acts exist.

### RD29-04 — MAJOR — `AGENTS.md` still keys three statements to "act 1", which the wave restructure retired

`AGENTS.md:22` — "**Owner-approved (D2)**; clause force begins at act 1"
`AGENTS.md:24` — "**No — candidate.** `contracts/rfcs/` exists only after act 1"
`AGENTS.md:25` — "**No — candidate.** `map/topology/` exists only after act 3"

There is no act 1. The acceptance record's act column reads A, B, C1, C2, D1, D2, 2, 3, 4, 5
(lines 22–31), and `AGENTS.md:36-37` itself says the single act "was restructured into **six wave
acts**". The correct referents exist and are stated elsewhere: the accepted contract home is
created "only by the first wave act's install step" (`contracts/candidates/README.md:5-6`), and
craft clause force was deliberately re-bound on 2026-08-10 — `INSTALL-RECORD.md:117-121`:

> "The paragraph now binds craft force phrase-free to 'the digest-bound acceptance acts defined
> in the active acceptance record', which the round-2026-08d wave restructuring makes the six
> wave acts."

So the operating-procedure page is one revision behind the record whose repair it should be
reflecting. (Act 3 in line 25 is fine — act 3 still exists.) The same residue is live in the
owner's queue: `PENDING-OWNER-DECISIONS.md` carries six lowercase `act 1` occurrences plus one
"Act 1" at line 118, four of them inside *open* rows — P-17 ("Act 1 (and act 5 for the mission
terms) closes this"), P-24 ("act 1 becomes a **requirement** before act 5"), P-27 ("inside act
1's digest set"), P-28 ("all normative edits to act 1's digest subject"). Line 89 shows the
repair pattern already applied once, to the ordering note only.

### RD29-05 — MAJOR — The register's recommended ceremony order contradicts the deferred-wave posture

`PENDING-OWNER-DECISIONS.md:73` (P-1):

> "**The six foundational wave acts** (restructured from the single act at round 2026-08d;
> **recommended ceremony order A → B → D1 → D2 → C1 → C2**)"

and lines 84–88:

> "**Act ordering (recommendation, not a rule):** perform Waves A, B, D1 and D2 before act 5."

Against `DEFERRED-WAVE-POSTURE.md:69-70`: "**No C/D wave act is offered while this posture
stands**", and `PROJECT-STATUS.md:24-31`, which states the launch prerequisite is "**Waves A + B
only**". [Observed] The string `DEFERRED-WAVE-POSTURE` occurs **0 times** in
`PENDING-OWNER-DECISIONS.md`; "Capability 1" occurs twice in 30 open rows.

[Inferred] The owner opening the register — the file README route 6 and `AGENTS.md:82` both send
them to — reads a six-act ceremony order beginning A, B, D1, D2 and a recommendation to perform
D1 and D2 before act 5. Nothing on the page says four of those six acts will not be offered. That
is a launch-relevant misreading available on the first pass, and the ordering note is precisely
the sentence that was already repaired once for naming a retired gate (line 89-90, "RD-20 M5").

### RD29-06 — MAJOR — As a reading experience, the register cannot answer the owner's three questions: which gate the launch, in what order, at what cost

Measured over the 30 open rows [Observed]:

- **5 of 30** state an earliest gate (P-29, P-30, P-32, P-33, P-41).
- **4 of 30** carry a recommendation (P-28, P-29, P-30, P-31).
- **0 of 30** are marked deferred — although `PROJECT-STATUS.md:27-29` declares "the P-29/P-30/P-32
  rulings that gate their repairs" **visibly deferred**, and `DEFERRED-WAVE-POSTURE.md:22-26` adds
  the D3/D4 questions to that set. P-29's row instead reads "Earliest gate: before Wave C2 is
  re-offered" — true, and silent on the fact that Wave C2 is not being offered.
- The open section is **3,751 words** in a single table; the longest row (P-21) is **346 words**
  and contains four dated amendments to itself, including a disclosed measurement correction.

The header helps only partially: lines 9–12 list the round's additions but stop at P-40 —
`P-41` does not appear in the as-of note that claims to enumerate what changed, though the row
exists at line 150. There is no status column, no launch/deferred column, no ordering, and no
per-row cost. [Inferred] Reading this file once, in order, I could not have told you which five
decisions the owner must make before Wave A is offered. I could reconstruct it only by reading
`DEFERRED-WAVE-POSTURE.md` and `PROJECT-STATUS.md` first and re-reading the register against
them — which inverts the routing (`AGENTS.md:82` sends "Open owner questions" here first).

### RD29-07 — MAJOR — P-20's row is false against the bytes it is read beside

`PENDING-OWNER-DECISIONS.md:121`:

> "The fixture-coverage gap is now named precisely — the ***evidence-adapter* class has no
> fixture**; the set is seven-for-eight with one double-count"

At this commit `fixtures/` holds ten context-selection fixtures, and fixture 9 is
`context-selection-9-evidence-adapter.md`, whose own head reads "**# Context-selection fixture 9
— evidence-adapter change (gate provenance and fidelity)** … Written 2026-08-05b to close the
coverage gap recorded at `round-2026-08b/FINAL-CONTEXT-COMPILER-FIXTURE-REPORT.md:81-114` (*"the
evidence-adapter class has no fixture"*)". [Observed] `PROJECT-STATUS.md:98-99` states the other
half: "The ten fixtures carry a task/answer boundary … and fixture 10 covers the
Trajectory-lifecycle class whose double-count RD-5 found."

So the register quotes, as a live gap, the exact sentence a tracked fixture was written to close,
and the row carries no "ground changed" note although eight other rows in the same table do. The
owner reading P-20 is told a coverage hole exists that the bytes closed. [Inferred] This is the
same class as RD29-01: a decision row that has fallen behind its own subject.

### RD29-08 — MAJOR — The designated human entry page never states that it is unadopted, and its header sentence reads as though it were adopted

`.syzygy/intent/OVERVIEW.md:6-7`:

> "Adopted by its own owner act (`ADOPT PROJECT OVERVIEW: <digest>`), which binds this file's
> exact bytes and nothing else."

Read cold, in the present perfect, that sentence says the page has been adopted; the mechanism
reading requires the reader to already know the act has not been performed. Nothing else in the
file's 261 lines says it is a draft. The truth is at `PROJECT-STATUS.md:44` — "⏳ **Draft —
refactored, awaiting adoption**" — and at `README.md:102-103`, which labels the link "(draft;
adoption pending)". [Observed]

This matters more than a general drafting nit because P-38 makes this file the **fixed human
entry**: "fixed entry `.syzygy/intent/OVERVIEW.md`; per-repository discoverability finding …
propose-only root-README link" (`PENDING-OWNER-DECISIONS.md:147`). A reader arriving at the entry
page directly — the arrival path the project intends to build — gets no candidate marking on a
page whose sibling artifacts are all scrupulously marked ("Candidate — accepted by no act yet",
"NOT ACCEPTED", "binds nothing"). The header's own next clause ("Current gate state is read from
`PROJECT-STATUS.md`") is a route, not a status, and the reader has no reason to think the page's
*own* status is the gate state in question. "Adopted **only** by its own owner act — not yet
performed" would close it, and (rule 10 permitting) it is a change to act 4's digest subject, so
it belongs in a batch, not a hotfix.

### RD29-09 — MINOR — Two script paths in `AGENTS.md`'s routing table resolve nowhere

`AGENTS.md:77`:

> "**`contracts/candidates/TASK-ROUTER.md`** — the one generated router (validated by
> `scripts/build_task_router.py`); context-budget measurement stays with `06-CONTEXT-LOAD-MAP.md`
> / `scripts/context_load.py`"

The other paths in that cell are relative to `.syzygy/governance/`. Under that reading the
scripts would be at `.syzygy/governance/scripts/`, which does not exist; under a repo-root
reading, `scripts/` holds exactly `check_governance.py` and `launch_gate_results.py`. Both
scripts actually live at `.syzygy/governance/contracts/candidates/scripts/`. [Observed] A
newcomer following the row gets "No such file or directory" and has to search. The router's own
header ("Written by `scripts/build_task_router.py`", `TASK-ROUTER.md:4`) is correct because it is
relative to the router's directory.

### RD29-10 — MINOR — The front door makes an unswept repository-wide absolute about itself

`README.md:123-125`:

> "**No claim of alignment, convergence, or regeneration capability is made anywhere in this
> repository**, and any document appearing to make one is wrong by doctrine (VIS-2)."

This is a "zero/anywhere" claim of the exact shape rules 2 and 9 govern, on the page a reader
trusts first, and no artifact owns the sweep behind it. My own bounded sweep (denominator: 315
tracked `.md` files) found 133 files using `convergen*`/`regenerat*` language; I inspected the
top of that distribution and found north-star and candidate-mechanism usage, **not** capability
claims — so I am not asserting a counterexample, and I am also not able to confirm the absolute.
The second clause ("any document appearing to make one is wrong by doctrine") converts the
sentence into something unfalsifiable, which is a different move from measuring it. [Inferred]
The honest form is the one the repo uses everywhere else: state the sweep, its denominator, and
its date, or state the rule without the "anywhere" quantifier.

### RD29-11 — MINOR — The glossary pointer arrives after the vocabulary does

Reading `README.md` straight through, the first terms of art land at line 27 ("desired state",
"observed state", "execution state"), line 36 ("doctrine VIS-1"), line 38 ("**Unknown**" as a
noun), lines 42–54 (four codenames, "projections", "the kernel", "candidate contract RFC-0010",
"a pending doctrine amendment (D3)"), and line 71 ("typed, explicitly authorized adapters
(VIS-5)"). The glossary route appears at **line 93**, under "Start here":

> "**Unfamiliar word?** [`.syzygy/governance/doctrine/README.md`](…#glossary-read-first) holds
> the adopted glossary … (seven entries; this file has none)."

Both facts in the parenthesis check out: the doctrine glossary has exactly seven bullets
(`doctrine/README.md:17-49`) and `README.md` has none [Observed], and the `#glossary-read-first`
anchor resolves to `## Glossary (read first)` at line 15. The placement is the issue, not the
content. Two terms are worse off: **"wave"** and **"act"** are defined nowhere on the entry path
in any form. A reader meets "restructured into **six wave acts**" for the first time at
`PROJECT-STATUS.md:18` with no gloss and no link to one — the design document is named, but what
an *act* is (an exact phrase the owner types, binding one digest, performed once) has to be
inferred from the acceptance record. [Inferred] Given that the entire repository is organized
around acts, one sentence defining the word on the status page would repay itself.

### RD29-12 — MINOR — The doctrine entry opens with three identifiers a clone cannot resolve

`doctrine/README.md:9`, the first table a reader meets on the doctrine page:

> "Owner decision D1, ratifying the packet at `../decisions/DOCTRINE-AMENDMENT-D1-MAP-HISTORICAL.md`
> (extracted under **FD-037**; original authored in the bootstrap record); scope made
> unconditional by **rev7 rework directive item A2** (not owner decision A2)"

`FD-037` is cited in 19 tracked files including this one [Observed, `git grep -c -F`], but the FD
log itself is founder-local — the register says so at P-15: "FD-n identifiers are still cited
from tracked files while the log itself is founder-local". So the doctrine front page's first
provenance note is unresolvable from a clone, as is "rev7 rework directive item A2". The
parenthetical "(not owner decision A2)" tells the reader that two A2s exist without letting them
reach either.

Continuing the doctrine reading order as directed, `vision.md:16` ("Syzygy (see README glossary)")
and `vision.md:38` ("the public **actuator toolchain** (README glossary)") reproduce the P-25 /
P-25(c) defects: the README the reader holds has no glossary (the root README now routes to the
right one — repair (b), done), and *actuator* is defined nowhere. Both are disclosed with drafted
packets and unrepaired, which is a legitimate posture; I record them because they are what the
cold reader actually hits, in the thesis paragraph, two clicks from the front door.

### RD29-13 — MINOR — The README describes a non-existent system in the present tense for 47 lines before saying so

`README.md:69-72`:

> "The loop is human-triggered. Syzygy writes project content directly only under `openspec/**`
> and `.syzygy/**`; it never writes implementation code, and it reaches every other system
> through typed, explicitly authorized adapters (VIS-5)."

The banner at lines 7–12 does say "no application code … deliberately", so a careful reader is
warned; but the flow between line 14 ("Concretely, the intended shape is…", correctly hedged) and
line 119 ("## What is not implemented — Everything.") drops the hedge, and the mermaid loop at
lines 58–67 is drawn as a working system. `OVERVIEW.md:125-126` solves the same problem in one
sentence — "This page describes intended shape, not current capability" — and the README would
benefit from borrowing it. [Inferred] I would not have acted wrongly on this, which is why it is
MINOR; but the flinch is real, and this project's own bar (VIS-1) is about exactly that flinch.

### RD29-14 — MINOR — The candidate package README under-lists two directories on a routed path

`contracts/candidates/README.md` layout table: `policy-candidates/` is described as "(term
registry, knowledge-hygiene policy, semantic-delta workflow)" against eight files actually
present — the omitted ones include `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` (see RD29-02),
`DOCTRINE-AMENDMENT-ACTUATOR-DEFINITION.md` (P-25(c)'s packet) and
`DOCTRINE-EDITORIAL-AMENDMENT-GLOSSARY-CITATION.md` (P-25(a)'s). The `scripts/` row names four of
the seven scripts present. [Observed] This is README route 4's destination, so it is on a default
path.

---

## 4. What reads well

This is the strongest state I would expect a corpus of this shape to be in, and several things
are done better here than in most repositories I could be reading:

- **The three-state thesis lands in one pass.** `OVERVIEW.md:35-49` — table, then diagram, then
  the sentence "Execution state never substitutes for either of the others" — is genuinely
  30-second comprehensible, and the README's compressed version at lines 27–32 says the same thing
  without contradicting it. I could restate the project's argument after one read, unprompted.
- **The progressive disclosure works.** `OVERVIEW.md:147-149` ("You have the argument. Everything
  past this point is optional drill-down … nothing below changes anything asserted above") is a
  promise the drawers keep. Drawer 2's per-claim authority table, with an explicit **Adopted /
  Recorded / Candidate** column, is the single best artifact on the entry path: it tells a cold
  reader which sentences they may rely on and which they may not, claim by claim.
- **Non-duplication is enforced where it costs something.** `OVERVIEW.md:126-133` refuses to
  restate the gate table and says why — "this file's bytes are frozen by an owner act, and a gate
  table frozen inside it would go quietly false the first time a gate fired." That is the rule
  being applied against the author's own convenience, and it is correct.
- **The status page is honest in the places it would be easiest not to be.** "Open state,
  honestly" (lines 79–128) leads with the unrepaired, states "fifteen `REVISE` verdicts, zero
  `CONFIRM`", labels its own coverage claim `[Inferred]`, and volunteers "**One thing this project
  does not have, stated plainly:** there is no mechanical task-to-context-packet compiler". The
  withdrawn-figures paragraph (lines 166–173) — removing numbers *because* they went stale twice —
  is the epistemic rule applied to the page itself.
- **`DEFERRED-WAVE-POSTURE.md` is a model disclosure.** Per-wave reason, per-wave *"what remains
  defective (disclosed, not hidden)"*, the gating owner decision, and a standing rule that no C/D
  act is offered. Line 45 — "Escapes are findings against *this file's* claims — report them,
  never absorb them" — is an invitation to be checked, which is rare and worth keeping.
- **Route integrity is largely repaired.** I followed six routes (contract question → TASK-ROUTER;
  "May I implement X?" → SURFACE-CLAUSE-ROUTING-MATRIX; spec authoring → HOW-TO-AUTHOR; Mission
  work → DEFERRED-WAVE-POSTURE; term → doctrine glossary → TERM-REGISTRY; status →
  PROJECT-STATUS). Every destination exists, is what the route says it is, and carries an accurate
  self-description. The two superseded neighbours a reader could stumble into —
  `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md` and `DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md` — both
  now open with explicit SUPERSEDED banners naming their replacements, which closes RD25-04 as far
  as I can see from these bytes. `TASK-ROUTER.md`'s deferred-wave rows are labelled in the heading
  itself, not in a footnote.
- **Counts I could recompute, recomputed.** 39 modules partitioned exactly by six wave manifests;
  19 + 11 for Waves A and B; SDR-1…33; ten fixtures; seven glossary entries; fifteen 08d reviews;
  "17 of 31 … including all six of section E" confirmed against the raw administration. Nothing in
  the numeric surface of the entry path failed a check.

## 5. Overall assessment — the cold reader's honest experience

Reading this corpus cold, the *argument* arrives intact and the *state* does not. Within ten
minutes I could say what Syzygy is, what three things it refuses to conflate, why "Unknown" is a
feature, and — unusually — what deliberately does not exist yet. That is the hard half of the
job, and it is done. The trouble starts at the question the project most needs a reader to answer
correctly: **what happens next, and who decides.** Three pages answer it three ways. AGENTS.md
counts eleven open acts and lists a set that omits one of them; PROJECT-STATUS lists twelve gates
and omits a different one, including from the launch path it explicitly enumerates; the
acceptance record lists ten. The owner's own decision register — the file every route points to
for "what am I being asked" — opens with a six-act ceremony order whose last four acts are not
being offered, never once names the deferral posture that says so, marks none of its thirty rows
as launch-gating or deferred, states an earliest gate on five of them, and sends the owner to the
retired digest block for the one act whose argument was superseded four days ago. Two of its
rows describe a repository that no longer exists at this commit.

None of these is a defect of *intent*. They are the residue of a corpus that repairs itself in
waves and whose navigation layer lags the record layer by one pass — the exact failure mode the
project has named, priced, and written rules against, showing up in the one layer the rules do
not mechanically check. The pattern is legible in the fixes already landed: the craft record was
re-bound "phrase-free" on 2026-08-10 precisely so a future retirement could not re-create this,
while AGENTS.md three lines from its own act table still says clause force begins at "act 1". The
same day's register gained P-41 and its own as-of header did not.

The honest posture is otherwise real, and I want to be precise about that: this corpus tells the
truth about itself more consistently than it navigates itself. Where it oversells, it oversells
by omission — a gate table missing a prerequisite, an entry page not marking its own candidacy —
not by claiming capability. Where it undersells, it buries: the launch scope, the deferral, and
the five decisions actually standing between today and the first offer are distributed across
four files and reconstructable only by reading them in the right order, which is not the order
the routes give. A reader who follows the routes as written arrives at a coherent picture of the
*project* and an incoherent picture of the *queue*.

Fixing this is small work, and none of it is normative: correct one pointer (RD29-01), add one
gate row and one path step (RD29-02), reconcile three act enumerations to one (RD29-03/04), and
give the register a status column, a deferral marking, and an ordering (RD29-05/06). Every
finding above is repairable without touching a contract clause — except RD29-08, which touches
act 4's digest subject and therefore belongs in a batch. What is not small is the judgment the
findings imply: the entry path is not yet at the standard the corpus behind it holds, and this is
the layer the owner will be standing in when the acts are offered.

VERDICT: REVISE
