# RC-2 — Vision / Polaris north-star review (RAW)

**Reviewer:** fresh-context agent, no authoring history, no `_bootstrap/` access.
**Date:** 2026-08-05.
**Scope read (exactly):** `README.md`, `.syzygy/intent/OVERVIEW.md`,
`.syzygy/governance/doctrine/vision.md`, `.syzygy/governance/doctrine/README.md`,
`PROJECT-STATUS.md`. Two narrow filesystem lookups were run to answer question 6
(which README owns the glossary) and to test one Layer-2 pointer's
navigability (`term registry`); no other file was opened.
**Question:** Is the north star human-comprehensible, memorable, and delivered
with genuine progressive disclosure?
**Posture:** adversarial; no desired outcome. `vision.md`'s *rules* are treated
as settled; only its presentation is critiqued.

---

## 1. MEMORABILITY

### 1a. The thesis I wrote from memory, before re-opening anything

> "Humans declare what should be true, evidence shows what is true, the
> difference becomes work that agent fleets do — and the difference is always
> shown honestly; no evidence means Unknown."

### 1b. What the documents actually say

There are **three canonical one-sentence theses in the five files, and no two
are the same sentence**:

- `README.md:3-5` — "humans define what should be true, evidence shows what is
  true, and agent fleets do bounded work to close the difference — with the
  difference always rendered honestly."
- `.syzygy/intent/OVERVIEW.md:20-22` — "Humans define what should be true.
  Evidence shows what is true. Agents do work to close the difference. Syzygy
  explains all three — and lets humans govern bounded missions instead of
  micromanaging tasks."
- `.syzygy/governance/doctrine/vision.md:16-26` — "a specification-driven
  software control plane: an observatory (V0) and harness … that makes a
  software portfolio's vision→spec→code hierarchy legible, truthful, and
  navigable."

My recall reproduced the README/OVERVIEW pair almost verbatim and **dropped
exactly the two clauses those two documents added beyond it**: "Syzygy explains
all three" and "lets humans govern bounded missions instead of micromanaging
tasks." I also recalled nothing of `vision.md`'s own framing — no
*observatory*, no *witness*, no *harness*, no *vision→spec→code*.

**Verdict on compressibility: yes, the thesis compresses — but the compressed
form the reader retains is not the one the OVERVIEW leads with.** What survives
one reading is a three-beat structure (declare / observe / close the difference)
plus one hard rule (no evidence means Unknown). Everything else is attrition.
That is a good result and the corpus should be built around it.

### 1c. Three problems the compression test exposes

**(i) The most memorable sentence in the corpus is used nowhere downstream.**
`vision.md:26` — "**Showing the truth is the soul of the product.**" Nine
words, no caveats, entirely true, and it appears in neither `README.md` nor
`OVERVIEW.md`. The two public front doors instead lead with a 40-word
four-sentence construction (`OVERVIEW.md:20-22`) that I demonstrably could not
hold intact.

**(ii) Three different triads compete for the name.** The codename means "the
astronomical alignment of three bodies — here: vision, specification, code"
(`.syzygy/governance/doctrine/README.md:17-19`). `vision.md:19-23` uses that
triad *and*, in the same paragraph, a different one: desired / observed /
execution state. `OVERVIEW.md:20-22` introduces a third: humans-define /
evidence-shows / agents-close, then says "Syzygy explains all three" without
saying which three. A reader who is asked "what are the three things?" cannot
answer reliably. The metaphor that names the project (vision, spec, code) is
*not* the triad the OVERVIEW's central model uses (desired, observed,
execution), and nothing anywhere reconciles them.

**(iii) The thesis needs one caveat to stay true, and the OVERVIEW's Layer 1
does not carry it.** `OVERVIEW.md:22` ends the 30-second thesis with "lets
humans govern bounded missions instead of micromanaging tasks." Mission
governance rests on candidate contract RFC-0010 and *proposed* doctrine
amendment D3 — the OVERVIEW itself says so at `:74-75` and again, at length, at
`:160-163` ("an open owner question, not a settled one"). `vision.md`'s thesis
(`:14-26`) contains no mission concept at all, and `vision.md:72-74` states
"Not autonomous… autonomy beyond VIS-4's stated bounds is licensed only through
the mechanism VIS-4 names, never by reinterpretation." So the single most
quotable sentence in the project's presentation artifact is **half doctrine and
half unaccepted candidate, with no label**, in a file whose own header
(`:10-11`) promises "Anchors marked *candidate* cite contract clauses that bind
nothing until owner acceptance." Layer 1 (`:18-25`) is the only claim block in
Layers 1-2 with no anchor line at all.

**(iv) The word "Syzygy" is never defined in either public front door.**
`README.md:1` and `OVERVIEW.md:13` both use it as a bare title.
`OVERVIEW.md:15-16` says only that it is a working codename. The etymology that
makes the name memorable — three bodies in alignment: vision, specification,
code — exists at `.syzygy/governance/doctrine/README.md:17-19`, four levels
down a directory tree, in a file the root README's "Start here" list never
names (`README.md:90-104` links `doctrine/` as a directory at `:79` and
`vision.md` directly at `:94`, never `doctrine/README.md`). A reader can finish
both front doors without learning why the project is called what it is called.

---

## 2. PROGRESSIVE DISCLOSURE

### 2a. Can a 5-10 minute reader stop at Layer 2?

**Structurally yes; practically no.**

What works: the layer headings are honestly named and advertise their own
altitude (`OVERVIEW.md:18`, `:27`, `:97`, `:167`), and Layer 2 ends with a
deliberate hand-off line at `:94-95` ("Foundational terms used so far … the
full vocabulary lives in the term registry"). That is a real stopping cue and
it deserves credit.

What defeats it:

1. **The Layer-4 drawer is pre-empted inline.** The header promises a two-tier
   system — "Source anchors sit at the end of each claim block; the drill-down
   table in Layer 4 is the full source drawer" (`OVERVIEW.md:9-10`). In
   practice Layer 2 carries *both*: four inline `*Sources:*` lines (`:35`,
   `:45`, `:77-78`, `:91`) citing `RFC1-22`, `RFC6-13`, `RFC-0010`, `SDR §1-2`
   — identifiers that are unresolvable without Layer 4. The mechanism designed
   to let a reader defer provenance instead injects unresolvable provenance
   into the five-minute read, and the unresolved identifiers *pull* the reader
   forward. That is the opposite of progressive disclosure.
2. **Layer 2 raises questions only Layer 3 answers, and flags them as
   unresolved.** `:70` introduces "Unknown is a first-class color" with no
   account of what Unknown is until `:111-119`. `:74-75` names "candidate
   contract RFC-0010 and pending doctrine amendment D3" and leaves the reader
   holding an unexplained dependency until `:160-163`. `:80-86` announces a
   "north star" and a "standing mandate" and defines the operative force of
   neither.
3. **There is no explicit permission to stop.** One sentence would fix this
   ("If you stop here you have the argument; Layers 3-4 are the mechanism and
   the sources"). Its absence, combined with (1), makes Layers 3-4 read as
   continuation.

### 2b. Distinct concepts a reader must hold to finish Layer 2

Enumerated from `OVERVIEW.md:1-95`, counting each term the reader must retain
to parse a later sentence in Layers 1-2:

| # | Concept | First use |
|---|---|---|
| 1 | governed presentation artifact (never authority) | `:5-6` |
| 2 | owner act binding a content digest | `:2-3` |
| 3 | RFC clause-ID citation form (RFC3-16, RFC7-3) | `:3`, `:7` |
| 4 | candidate vs adopted status distinction | `:10-11` |
| 5 | working codename convention (poetic name + literal subtitle) | `:15-16` |
| 6 | Unknown — never green, never zero | `:24` |
| 7 | doing work ≠ proof of intent satisfied | `:25-26` |
| 8 | owner (single accountable human) | `:29` |
| 9 | agent fleet | `:29` |
| 10 | portfolio of projects | `:29-30` |
| 11 | underspecification surfacing after deployment | `:33-34` |
| 12 | desired state | `:38` |
| 13 | observed state | `:39-40` |
| 14 | execution state | `:40-41` |
| 15 | evidence | `:39-40` |
| 16 | reconciliation work | `:43-44` |
| 17 | actuator | `:43-44` |
| 18 | warrant / "warranted work" | `:56` (diagram) |
| 19 | semantic kernel | `:61-62` |
| 20 | temporal project graph | `:62` |
| 21 | evaluation engine | `:62-63` |
| 22 | surface / projection, non-authoritative | `:63-64` |
| 23 | machine query plane | `:63` |
| 24 | Polaris | `:66` |
| 25 | Trajectory | `:67` |
| 26 | Orrery | `:69` |
| 27 | capability identity | `:70` |
| 28 | Unknown as a first-class color | `:70` |
| 29 | adopted amendment D1 | `:71` |
| 30 | Mission Control | `:71` |
| 31 | workspace vs project level | `:72-73` |
| 32 | pending doctrine amendment D3 | `:75` |
| 33 | Project Genome | `:81` |
| 34 | north star ≠ present doctrine | `:83-85` |
| 35 | standing mandate (live fleet observability) | `:84-86` |
| 36 | term registry | `:95` |

**Count: 36 distinct concepts.** Target range in the question: 8-12. Actual is
**3x the ceiling**. Even discounting the header (items 1-4) and the diagram
label (18) as arguably out-of-body, the running total is 31.

The load is not evenly distributed: items 1-17 are load-bearing and mostly
earn their place. Items 19-23 and 27-36 arrive in a 35-line stretch
(`:61-95`) that introduces **eighteen** new concepts, including three
governance identifiers (D1, D3, RFC-0010) and two normative categories with
opposite force (north star vs standing mandate) in a single paragraph. That
stretch, not the whole layer, is where the five-minute read breaks.

### 2c. Provenance interrupting the argument in Layers 1-2

Every instance, quoted, with judgment:

| # | `path:line` | Text | Judgment |
|---|---|---|---|
| P1 | `OVERVIEW.md:1-4` | "Reviewed presentation draft — adopted only by its own owner act, `ADOPT PROJECT OVERVIEW: <digest>`, binding this file's exact content digest — never implicitly on any other gate (RFC3-16: this stamp is a self-declaration; effective status lives in the owner-act record)." | **Not needed here.** The act phrase and digest mechanics matter to exactly one reader (the owner performing act 4) at exactly one moment. One action away. Layer 4's closing paragraph (`:190-193`) already discusses digests and act phrases — this belongs there. |
| P2 | `OVERVIEW.md:5-7` | "This overview is a governed presentation artifact and may never be cited in place of doctrine, contracts, specifications, policy, or topology (RFC7-3's rule, applied to itself)." | **Needed, but not at this length.** "Presentation, never authority" is a four-word version of the same honesty. The RFC7-3 citation is one action away. |
| P3 | `OVERVIEW.md:7-8` | "Current project status is read from `PROJECT-STATUS.md` and the owner-act records, never from this page." | **Needed** — and see §3: the file then violates it nine times. |
| P4 | `OVERVIEW.md:9-11` | "Source anchors sit at the end of each claim block; the drill-down table in Layer 4 is the full source drawer. Anchors marked *candidate* cite contract clauses that bind nothing until owner acceptance." | **Needed only because inline anchors exist.** Remove the inline anchors from Layers 1-2 and this instruction disappears with them. |
| P5 | `OVERVIEW.md:35` | "*Sources: vision.md (owner transformation; the human problem).*" | **Deferrable.** Cheapest of the four (a filename, no clause IDs), but it interrupts the single most human paragraph in the document — the one that establishes the reader's sympathy. |
| P6 | `OVERVIEW.md:45` | "*Sources: vision.md (three-state thesis); candidate: RFC1-22.*" | **`RFC1-22` is not needed here** and cannot be resolved by a reader at this point. Move to Layer 4. |
| P7 | `OVERVIEW.md:71` | "historical state included by adopted amendment D1" | **Not needed.** An amendment letter mid-bullet, inside the one-line description of a surface. The reader learns nothing about Orrery from "D1". |
| P8 | `OVERVIEW.md:74-75` | "defined by candidate contract RFC-0010 and pending doctrine amendment D3" | **The *caveat* is needed** (this surface is not settled); **the identifiers are not.** "not yet accepted — see Layer 4" carries the same honesty. |
| P9 | `OVERVIEW.md:77-78` | "*Sources: architecture.md (one kernel, three surfaces); SDR §1–2; candidate: RFC6-13, RFC-0010.*" | **Deferrable in full.** Also note the anchor says "one kernel, **three** surfaces" directly beneath a heading that says "four experiences" (`:61`) — the anchor silently contradicts the claim it supports. |
| P10 | `OVERVIEW.md:91` | "*Sources: PROJECT-STATUS.md (gate table); VIS-2 forbids implying more.*" | **Half needed.** The `PROJECT-STATUS.md` pointer is the *only* thing that should remain of the whole "What exists today" block (see §3). "VIS-2 forbids implying more" is the author defending themselves to a governance reader, mid-argument, to a reader who has not met VIS-2. |
| P11 | `OVERVIEW.md:80-86` | *(absence)* the north-star block carries **no** `*Sources:*` line, unlike all four other Layer-2 blocks | **Needed and missing.** This is the one claim in the document that VIS-2 (`vision.md:96-98`) most tightly constrains — a regeneration ideal — and it is the only unanchored block. The pattern's one exception is its most consequential case. |

**Summary:** of eleven provenance interruptions in Layers 1-2, **two carry
information the reader needs at that point** (P3, and the caveat half of P8),
one is needed-but-missing (P11), and the rest are drawer material presented as
body text.

---

## 3. FROZEN CURRENT STATE

`OVERVIEW.md:7-8` states the rule: *"Current project status is read from
`PROJECT-STATUS.md` and the owner-act records, never from this page."* The file
then hard-codes current status in at least nine places, one of which is a
column literally headed **Status**.

| # | `path:line` | Frozen fact | Goes stale when | Where it belongs |
|---|---|---|---|---|
| F1 | `OVERVIEW.md:74-75` | "defined by candidate contract RFC-0010 and **pending** doctrine amendment D3" | act 1 (RFC-0010 accepted) or act 5 (D3 adopted/declined) | Status-free phrasing: "defined by RFC-0010 and doctrine amendment D3"; status via the Layer-4 pointer row |
| F2 | `OVERVIEW.md:87-90` | "**What exists today.** Adopted doctrine, owner-approved engineering policy, and a candidate contract corpus awaiting owner acceptance. **Nothing is implemented** — no daemon, no UI, no store, no endpoints, no chosen stack." | act 1; act 2; first line of implementation | `PROJECT-STATUS.md:43-51` already holds a strictly better version of this paragraph. Replace the block with one sentence + link. |
| F3 | `OVERVIEW.md:160-163` | "Whether the proposed bounded-Mission amendment (D3) plus the candidate Mission contract satisfy that mechanism is **an open owner question, not a settled one**" | act 5 | `PROJECT-STATUS.md:27` (gate 8) and the D3 packet |
| F4 | `OVERVIEW.md:171-175` | Status column: five doctrine rows "Adopted"; "(amendment D1 in force)" | future doctrine amendment | Stable today, but it is still status in a file that disclaims status |
| F5 | `OVERVIEW.md:177-185` | Status column: **eleven rows** reading "Candidate" (RFC-0001 … RFC-0011) | **act 1** — all eleven flip at once | Single pointer row: "Status of every contract: `PROJECT-STATUS.md` gate table" |
| F6 | `OVERVIEW.md:186` | "Owner-approved (D2)" for craft-and-care | act 2 (CC-TEST-2) changes the approved digest | same |
| F7 | `OVERVIEW.md:187` | "Vocabulary … Candidate" | gate 9 (knowledge-hygiene craft act, `PROJECT-STATUS.md:28`) | same |
| F8 | `OVERVIEW.md:190-191` | "**Candidate modules live under** `.syzygy/governance/contracts/candidates/`" | act 1 — accepted modules move to `contracts/rfcs/`, so this path becomes wrong | Layer-4 pointer row |
| F9 | `OVERVIEW.md:71` | "historical state included by **adopted** amendment D1" | future amendment | minor, but same class |

**The structural trap.** This file is bound by act 4 to its exact content
digest (`OVERVIEW.md:2-3`), and repository operating procedure holds that an
artifact edited after its act is an artifact with no act. Nine of the facts
above are the status of *other* acts — 1, 2, 3, 5 and gate 9. Therefore:

- If act 4 is performed **before** acts 1/2/5, the adopted overview becomes
  false the moment any of them fires, and cannot be corrected without
  re-performing act 4.
- If act 4 is performed **after** them, the file must be edited first — which
  changes the digest the acceptance record currently quotes, invalidating the
  act-4 argument.

Either way **the current text forces an act-ordering constraint that no
document in scope states**. `PROJECT-STATUS.md:16-31` presents gates 4-8 as an
unordered menu; `README.md:96` calls `PROJECT-STATUS.md` the "exact current
gate state" and says nothing about ordering. This is a live gate-arithmetic
hazard of the same family as the one `PROJECT-STATUS.md:56-64` already
discloses.

**Additionally — circular status authority.** `PROJECT-STATUS.md:26` names the
owning record for gate 7 as "`.syzygy/intent/OVERVIEW.md` header", while
`OVERVIEW.md:7-8` says status is never read from that page. The header does not
in fact contain the string "Draft — refactored, awaiting adoption" that
`PROJECT-STATUS.md:26` attributes to it. Each file points at the other; neither
owns the fact.

**Minimal fix for the whole class:** delete the Status column from the Layer-4
table and replace it with a single line beneath the table — "Status of every
row: `PROJECT-STATUS.md` gate table + the owner-act record" — and reduce
`:87-90` to one sentence with a link. That removes F1-F9 in one edit, makes
`:7-8` true, and dissolves the act-ordering trap.

---

## 4. THE HEADER

`OVERVIEW.md:1-11` — eleven blockquoted lines, ~140 words, **before the H1**.
Content: an act phrase with a digest placeholder, two RFC clause citations
(RFC3-16, RFC7-3), a self-declaration disclaimer, a status disclaimer, and a
description of the file's own anchor conventions.

**Effect on a first-time reader.** The reader arrives from `README.md:92-93`,
which promises "the project argument, 30 seconds to full depth." The first
thing they meet is not the argument. It is the document talking about its own
adoption status in a vocabulary (act, digest, RFC3-16, "self-declaration",
"governed presentation artifact") that the document has not yet taught. The
30-second promise is consumed entirely by the preamble, and the reader's first
inference is "this is a compliance artifact," which is precisely the impression
`vision.md:61-64` warns against ("Not a documentation portal").

There is a second, subtler cost: the header's most important line (`:7-8`,
status is never read from this page) is the fourth of five claims in a wall of
text, so it reads as boilerplate — which may be why the body then violates it
nine times (§3).

**A form that keeps the same honesty with less friction.** Two lines above the
title, everything else moved to the Layer-4 closing paragraph (`:190-193`),
which already discusses digests and act phrases:

> **Presentation, not authority — never cite this page in place of doctrine,
> contracts, specs, policy, or topology.**
> Current status: [`PROJECT-STATUS.md`](../../PROJECT-STATUS.md). Adoption
> terms, source conventions, and act phrase: [Layer 4](#layer-4--exact-authority-drill-down).

Nothing true is lost — RFC3-16's self-declaration point, RFC7-3's rule, the act
phrase, and the candidate-anchor convention all restate cleanly one scroll away,
next to the material they govern. The reader reaches "Humans define what should
be true" in under ten seconds instead of sixty.

---

## 5. JARGON AUDIT (Layers 1-2 only)

Key: **(a)** essential to the argument at this altitude · **(b)** deferrable to
drill-down · **(c)** undefined at point of use.

| Term | `path:line` | Mark | Note |
|---|---|---|---|
| Syzygy | `:13` | **(a)(c)** | Never defined in this file or `README.md`. Definition exists only at `doctrine/README.md:17-19`. The project's own name is the worst-defined term in the corpus. |
| working codename / literal subtitle | `:15-16` | (b) | Self-explaining, but spends the reader's first line of body text on naming policy. |
| desired state / observed state / execution state | `:38-41` | (a) | Defined inline, well. The document's strongest passage. |
| evidence | `:39-40` | (a)(c) | Used as if ordinary; carries a hard technical definition (durable, identified, integrity-verifiable — `vision.md:98-99`) that only arrives at Layer 3 `:112-113`. A reader who takes the ordinary meaning misreads "no evidence means Unknown." |
| Unknown (capitalized state) | `:24`, `:70` | (a) | Contextually clear; capitalization does real work. |
| reconciliation work | `:43-44` | (a) | Defined just enough ("the computed difference becomes"). |
| actuator | `:43-44` | (b)(c) | Inferable from "perform it". `vision.md:38-39` treats "the public actuator toolchain" as a glossary term; it is not one (see §6). |
| warrant / "warranted work" | `:56` | (b)(c) | Appears only inside the diagram, defined nowhere in Layers 1-2. Diagram labels are read first and explained last. |
| semantic kernel | `:61-62` | (a)(c) | Load-bearing — "none is independently authoritative" depends on it — and given no definition beyond a restatement. |
| temporal project graph | `:62` | (b)(c) | Two unexplained modifiers on an unexplained noun. |
| evaluation engine | `:62-63` | (b)(c) | Meaningless until `:115-117`. |
| surface / projection | `:63-64` | (a) | Adequately defined by "project it; none is independently authoritative". |
| machine query plane | `:63` | (a)(c) | Named once, never explained, and then **dropped from the list it introduces** — see finding 3. |
| Polaris / Trajectory / Orrery / Mission Control | `:66-75` | (a) | Correctly handled: every codename carries a literal subtitle. Best-executed convention in the file. |
| capability identity | `:70` | (b)(c) | Used once, undefined; the reader cannot picture what Orrery is a map *of*. |
| "Unknown is a first-class color" | `:70` | (b) | Evocative and fine, though it presumes a rendering model not yet introduced. |
| amendment D1 | `:71` | (b)(c) | A bare letter identifier. |
| doctrine amendment D3 | `:75` | (b)(c) | Same. |
| candidate contract RFC-0010 | `:75` | (b)(c) | Same. |
| RFC1-22 / RFC6-13 / SDR §1-2 | `:45`, `:77-78` | (b)(c) | Clause-ID grammar (`RFC<n>-<clause>`) is never explained; the reader cannot tell whether `RFC1-22` is a document or a line. |
| Project Genome | `:81` | (b) | Adequately defined in place ("complete normative corpus"). |
| north star (as a normative category) | `:83-85` | (a) | Explicitly labeled "not present doctrine and never a current capability claim". Correctly done. |
| standing mandate | `:84` | (a)(c) | The phrase is doing heavy normative work — and understates its source (§6). A reader cannot tell it outranks the north star it shares a paragraph with. |
| owner | `:29`, `:94` | (b)(c) | Carries a precise doctrinal meaning (the single human accountable — `doctrine/README.md:22-24`) that is never stated here. |
| term registry | `:95` | (b)(c) | No path, no link. Layer 4 `:187` gives a *directory*, not the file. The file is `.syzygy/governance/contracts/candidates/policy-candidates/TERM-REGISTRY.md` [Observed] — reachable, but only by guessing. The closing sentence of Layer 2 is a dead-end pointer. |
| governed presentation artifact | `:5` | (c) | Header. |
| owner act / content digest | `:2-3` | (c) | Header. |

**Tally for Layers 1-2:** 27 flagged terms, of which **13 are (c) undefined at
point of use**. Of those 13, six are governance identifiers (D1, D3, RFC-0010,
RFC1-22, RFC6-13, SDR) that belong in the drawer, and four (`machine query
plane`, `semantic kernel`, `capability identity`, `evidence`) are load-bearing
words the argument actually leans on.

---

## 6. VISION.MD — support, drift, and the "README glossary"

### 6a. Where the overview and doctrine agree (credit where due)

- `OVERVIEW.md:29-34` is a faithful, well-compressed rendering of
  `vision.md:28-36`. It keeps the owner's specific failures (oversized diffs,
  scattered completions, underspecification after deployment) instead of
  smoothing them into "better visibility."
- `OVERVIEW.md:37-44` tracks `vision.md:19-24` accurately, including the hard
  part — "scheduled, completed, or merged work is never proof."
- `OVERVIEW.md:83-85` preserves VIS-2's exact posture on the regeneration
  ideal: "north star, not present doctrine and never a current capability
  claim" (`vision.md:204-212`). No overclaim.
- `OVERVIEW.md:156-160` correctly reproduces `vision.md:72-74`'s "never by
  reinterpretation," and `:160-163` volunteers that D3's sufficiency is an open
  question — an honest disclosure the document was not obliged to make.

### 6b. Drift — overstatement

**D1 [overstatement, Layer 1].** `OVERVIEW.md:22` puts "lets humans govern
bounded missions instead of micromanaging tasks" *inside the 30-second thesis*.
`vision.md`'s thesis (`:14-26`) has no mission concept; `vision.md:72-74` says
the loop is human-triggered and autonomy expansions require VIS-4's named
mechanism. The overview's own Layer 3 (`:160-163`) says whether D3 plus RFC-0010
satisfy that mechanism is unsettled. So the thesis line asserts as settled
something the same file later calls open. Layer 1 carries no anchor and no
candidate mark to signal it.

**D2 [overstatement / fidelity, Layer 2].** `OVERVIEW.md:61` heads the block
"One kernel, **four experiences**"; `:63-64` says "**Three project surfaces and
a machine query plane** of equal standing project it"; the bullets that follow
(`:66-75`) are Polaris, Trajectory, Orrery, **Mission Control** — and Mission
Control is described in the same bullet as "Workspace-level, **not a fourth
project truth surface**". The enumeration therefore delivers a different four
than the sentence promises, and **the machine query plane is silently dropped
from the list it was just named in.** That plane is not incidental:
`vision.md:39-41` makes agents one of *two first-class consumers from day one*.
`README.md:40-47` repeats the same defect — a table headed "The four
experiences" listing the same four, with no machine plane anywhere in the
document, immediately followed by `README.md:49-53` explaining that Mission
Control is not a fourth surface. A fresh reader cannot restate the surface
model correctly from either front door, which is the VIS-3 test
(`vision.md:108-114`).

### 6c. Drift — understatement

**D3 [understatement, and a category collision].** `OVERVIEW.md:80-86` puts two
things with **opposite normative force** in one paragraph:

- the regeneration north star — explicitly *not* doctrine (`vision.md:204-212`);
- live fleet observability — explicitly binding: "Syzygy is **not complete**
  until its owner can watch agent fleets work live… Every roadmap **must** carry
  it as a named, sequenced item with stated entry criteria; removing it, or
  leaving it unsequenced, **violates doctrine**" (`vision.md:220-225`).

The overview renders the second as "a separate standing mandate is live fleet
observability — watching agent fleets work, deferred until there is observed
truth to annotate" (`:84-86`). Every word is true; the *force* is gone. A
binding, roadmap-blocking doctrinal obligation reads as a nice-to-have,
sentence-adjacent to an aspiration the same paragraph disclaims. Merging the
two makes it likely a reader assigns both the weaker status.

**D4 [understatement — the north star's only operative rule is dropped].**
`vision.md:210-212`: "It exerts direction: decisions should nudge projects
toward it, and a decision that materially forecloses it **must record that
foreclosure — the unrecorded foreclosure is the violation.**" That is the sole
present-tense, enforceable consequence of the north star, and `OVERVIEW.md:80-86`
omits it entirely. The overview keeps the disclaimer and drops the duty. Also
dropped: the converse flow — deriving candidate vision from an existing codebase
(`vision.md:213-215`), which is *legitimate today* and is arguably the only
part of the genome story that describes something the project could do now —
and the `[Unknown]` on achievability with spec completeness as the biggest named
risk (`:216-218`).

**D5 [understatement — the corpus's own best framings unused].**
`vision.md:44-52` defines Syzygy as a **witness / observatory** (V0) and a
**harness** (V0 PoC, V1 full), and `vision.md:54-74` gives five sharp "what it
is not" statements — including "Not a documentation portal… A Syzygy from which
no work is ever dispatched has failed, regardless of how good its documents
look" (`:61-64`). None of this reaches `OVERVIEW.md`. The observatory/harness
pair is `vision.md`'s most compressible image, and the documentation-portal
line is the single most useful sentence a reader of a 100%-documents repository
could be handed.

**D6 [front-door inconsistency].** `README.md:14-18` states the intended shape
concretely — "a **local-first daemon with a browser app**… the platform
commitment itself is doctrine-level, while language, framework, and database
are deliberately unchosen." `OVERVIEW.md` never says what the thing physically
is, at any layer. The document `README.md:92-93` bills as "30 seconds to full
depth" is *less* concrete about the artifact than the one-paragraph README
summary above it.

**D7 [minor, status-label drift].** `README.md:7` — "Current stage:
**pre-specification project-shape normalization**." `PROJECT-STATUS.md:12` —
"**Final pre-specification.**" Two labels for one lifecycle stage, in the two
files a newcomer reads first, with the README linking to the other for "the
exact gate state" (`README.md:12`).

### 6d. The "README glossary" reference — what it actually resolves to

`vision.md` cites a "README glossary" twice, both unlinked:

- `vision.md:16` — "Syzygy (see README glossary) is a specification-driven
  software control plane"
- `vision.md:38-39` — "it assumes the public actuator toolchain (README
  glossary), never one private machine"

**What I found [Observed], by enumerating every `README.md` in the repository
(excluding `.git`, `_bootstrap/`, `node_modules`) and searching each for
"glossar":**

- **Exactly one** README in the repository contains a glossary:
  `.syzygy/governance/doctrine/README.md:15` — `## Glossary (read first)`.
  Fifteen READMEs were scanned; the other fourteen contain no match.
- The intended target for `vision.md:16` is
  `.syzygy/governance/doctrine/README.md:17-21` ("**Syzygy** — provisional
  codename for this project; literally, the astronomical alignment of three
  bodies — here: vision, specification, code…"). It exists and is good.
- **The root `README.md` has no glossary** [Observed — full read, plus the
  scan above], and does not define "Syzygy" anywhere.

**Can a reader find it? Substantially no, and the failure mode is specific.**
The root README's "Start here" (`README.md:90-104`) routes a reader to
`vision.md` at step 2 (`README.md:94`) directly — it never names
`doctrine/README.md`. A reader who reaches `vision.md:16` therefore has just
come *from* a file called README, and the unqualified phrase "README glossary"
most naturally denotes that one. They will scroll the root README, find no
glossary, find no definition of "Syzygy", and conclude the reference is broken.
The correct target is a sibling file in `vision.md`'s own directory, so the fix
is trivially available: `[doctrine README glossary](README.md#glossary-read-first)`.

**Second, partial-resolution problem.** `vision.md:38-39` cites the same
glossary for "the public **actuator toolchain**." That term is **not a glossary
entry** [Observed]. The nearest entry is
`.syzygy/governance/doctrine/README.md:39-44`, which defines "the `/th-*`
skills and claude/codex CLIs — the designated initial **agent** toolchain for
workers and actuators." So the reader who successfully finds the right README
still does not find the term they were sent for; they find a near-synonym and
must infer the equivalence. "Actuator" itself is defined nowhere in the two
doctrine files in scope, yet it is load-bearing in `vision.md:25`, `:38`, `:58`
and in `OVERVIEW.md:43-44`, `:53`.

**Presentation note on `vision.md` itself** (rules treated as settled): VIS-1's
five-rank priority ordering (`vision.md:82-94`) is the most-cited object in the
corpus and is buried as inline prose inside a thirteen-line paragraph, where
`(1)…(5)` must be parsed out of a running sentence. Rendering it as a numbered
list would change no content and materially improve the fresh-reader test that
VIS-3 (`:108-114`) imposes on this very file. Similarly, VIS-5 (`:141-165`) is
25 lines, roughly double any other rule; its normative core lands in the first
sentence and is then qualified for 22 lines, which invites readers to stop early
and miss the adapter clause.

---

## VERDICT

VERDICT: REVISE

### Findings

**1. [Blocking] Layer 1's thesis asserts unaccepted candidate material as
settled, unanchored and unlabeled.** `OVERVIEW.md:22` — "lets humans govern
bounded missions instead of micromanaging tasks" — depends on RFC-0010
(candidate) and D3 (proposed), which the same file concedes at `:74-75` and
`:160-163`. `vision.md:14-26` has no mission concept; `vision.md:72-74` is "Not
autonomous." Layer 1 (`:18-25`) is the only claim block in Layers 1-2 with no
`*Sources:*` anchor, so the header's candidate-marking convention (`:10-11`)
never fires on the sentence that most needs it.
**Minimal fix:** cut the clause from Layer 1 — the thesis is stronger at three
beats — and keep bounded missions where it is already honestly handled, at
`:71-75` and `:156-163`. If it must stay in Layer 1, append the anchor
`*Source: candidate RFC-0010; proposed doctrine amendment D3 — neither
accepted.*`

**2. [Blocking] The surface enumeration is internally inconsistent and drops
the machine query plane.** `OVERVIEW.md:61` says "four experiences"; `:63-64`
promises "Three project surfaces and a machine query plane"; `:66-75` delivers
three surfaces plus Mission Control, which `:72-73` says is not a project
surface. The machine query plane — one of `vision.md:39-41`'s two first-class
consumers — never appears again in the document, and appears nowhere in
`README.md`. `README.md:40-53` repeats the identical defect. A fresh reader
cannot restate the surface model correctly, which is the VIS-3 test.
**Minimal fix:** in `OVERVIEW.md:63-64` write "Three project surfaces and a
machine query plane of equal standing project it; a fourth, workspace-level
operator surface sits beside them:" and add a fifth bullet for the machine query
plane. Retitle `README.md:40` from "The four experiences" to "The surfaces" and
add the machine plane row.

**3. [Blocking] Nine current-state facts are frozen into a digest-bound file, in
violation of the file's own line 8, creating an unstated act-ordering trap.**
See §3, F1-F9 — chiefly the eleven "Candidate" rows at `OVERVIEW.md:177-185`,
"Owner-approved (D2)" at `:186`, "What exists today" at `:87-90`, and the
candidates-path sentence at `:190-191`. Because act 4 binds this file's exact
digest, performing act 4 before acts 1/2/5 adopts a document that becomes false
on the next act and cannot be repaired without re-performing act 4; performing
it after requires an edit that invalidates the act-4 argument. No document in
scope states this ordering constraint (`PROJECT-STATUS.md:16-31` presents the
gates as an unordered menu).
**Minimal fix:** delete the Status column from the Layer-4 table and put one
line beneath it — "Status of every row: `PROJECT-STATUS.md` gate table plus the
owner-act record"; reduce `:87-90` to "**What exists today.** No implementation
— see [`PROJECT-STATUS.md`](../../PROJECT-STATUS.md)."; drop "candidate",
"pending", and the candidates path from `:74-75` and `:190-191`.

**4. [Blocking] Circular status authority between `PROJECT-STATUS.md` and the
overview header.** `PROJECT-STATUS.md:26` names "`.syzygy/intent/OVERVIEW.md`
header" as the owning record for gate 7 and quotes a status ("Draft —
refactored, awaiting adoption") that does not appear in that header;
`OVERVIEW.md:7-8` says status is never read from that page. Neither file owns
the fact.
**Minimal fix:** change the gate-7 owning record in `PROJECT-STATUS.md:26` to
the acceptance record (which owns act 4), matching gates 4 and 6.

**5. [Blocking] The north star and the fleet-observability mandate are merged
into one paragraph despite opposite normative force, and the north star's only
operative rule is dropped.** `OVERVIEW.md:80-86` renders `vision.md:220-225`'s
roadmap-blocking obligation ("not complete until…", "every roadmap must carry
it…, violates doctrine") as "a separate standing mandate", adjacent to an ideal
the same paragraph disclaims as non-doctrine; and it omits
`vision.md:210-212`'s "a decision that materially forecloses it must record
that foreclosure — the unrecorded foreclosure is the violation." The block is
also the only Layer-2 block with no source anchor, despite being the claim VIS-2
most constrains.
**Minimal fix:** split into two short blocks. North star keeps the disclaimer
and gains one sentence: "A decision that materially forecloses it must record
that foreclosure." Fleet observability gets its own line stating the binding
form. Add `*Sources: vision.md (the north star, honestly labeled; eventual
mandate); VIS-2.*`

**6. [Blocking] The project's name is undefined in both public front doors, and
`vision.md`'s "README glossary" pointer misroutes.** `README.md` and
`OVERVIEW.md:13` both use "Syzygy" without definition. The only glossary in the
repository is `.syzygy/governance/doctrine/README.md:15` [Observed — all 15
READMEs scanned], which `README.md:90-104` never links; `vision.md:16` and
`:38-39` cite it unlinked, and a reader arriving from the root README will
search the wrong file. `vision.md:38-39`'s referent, "actuator toolchain", is
not a glossary entry at all — the nearest is "agent toolchain"
(`doctrine/README.md:39-44`).
**Minimal fix (presentation only, no rule change):** in `vision.md:16` and
`:38-39` link the sibling explicitly — `[doctrine README
glossary](README.md#glossary-read-first)`; add "vision, specification, code —
the three bodies the name aligns" to `README.md:1-5` and `OVERVIEW.md:15-16`;
add `README.md:90-104` step 0 pointing at `doctrine/README.md`.

**7. [Blocking] Layer 2 carries 36 distinct concepts against a 8-12 target, with
18 of them in the 35-line stretch `:61-95`.** See §2b. The five-minute read is
not deliverable at this density.
**Minimal fix:** the F-class deletions in finding 3 and the anchor moves in
finding 8 remove roughly ten (D1, D3, RFC-0010, RFC1-22, RFC6-13, SDR, act,
digest, candidate/adopted status, governed presentation artifact) without
touching the argument. Then cut "temporal project graph" and "evaluation engine"
from `:62-63` to "a single semantic kernel computes every truth exactly once"
and let Layer 3 name the parts, and drop "capability identities" from `:70`.
That lands near 20 — still high, but within reach of a five-minute read.

**8. [Non-blocking] Inline `*Sources:*` lines pre-empt the Layer-4 drawer they
advertise.** `OVERVIEW.md:35`, `:45`, `:77-78`, `:91` inject clause IDs that
cannot be resolved without Layer 4, pulling the reader forward; `:77-78` even
cites "one kernel, three surfaces" beneath a heading claiming four (§2c P9).
**Minimal fix:** keep bare filenames in Layers 1-2 (`vision.md`,
`architecture.md`); move every clause ID and SDR reference into the Layer-4
table.

**9. [Non-blocking] The 11-line pre-title header is disproportionate.**
`OVERVIEW.md:1-11`, ~140 words, four governance citations, before the H1 — and
its one load-bearing line (`:7-8`) is buried fourth of five.
**Minimal fix:** the two-line replacement in §4; move RFC3-16, RFC7-3, the act
phrase, and the anchor convention into the existing Layer-4 closing paragraph
at `:190-193`.

**10. [Non-blocking] Layer 4, billed as "the full source drawer" (`:10`), omits
two authorities the body cites.** Layer 3 `:99-105` names topology ("intended
placement") and `openspec/**` ("required observable behavior") as typed
authorities; neither has a row in the table at `:169-188`, though
`README.md:83-84` lists both.
**Minimal fix:** add a topology row (`.syzygy/map/topology-candidates/`) and an
`openspec/` row.

**11. [Non-blocking] Layer 2's closing pointer is a dead end.**
`OVERVIEW.md:95` — "the full vocabulary lives in the term registry" — gives no
path; Layer 4 `:187` gives a directory, not the file. The file is
`.syzygy/governance/contracts/candidates/policy-candidates/TERM-REGISTRY.md`
[Observed].
**Minimal fix:** link the file at `:95`; correct the `:187` cell to the file
path.

**12. [Non-blocking] Three competing triads make the name unmemorable.**
vision→spec→code (`doctrine/README.md:17-19`, `vision.md:19`); desired /
observed / execution (`vision.md:20-23`, `OVERVIEW.md:37-44`); define / show /
close (`OVERVIEW.md:20-22`, which then says "Syzygy explains all three" without
saying which three).
**Minimal fix:** one clause in `OVERVIEW.md:15-16` — "the name is the alignment
of vision, specification, and code; the model that follows tracks them as
desired, observed, and execution state" — and change `:22` from "all three" to
"all three states".

**13. [Non-blocking] The corpus's most memorable and most self-disciplining
lines never reach a reader.** `vision.md:26` ("Showing the truth is the soul of
the product"), `vision.md:44-52` (witness / observatory / harness), and
`vision.md:61-64` ("A Syzygy from which no work is ever dispatched has failed,
regardless of how good its documents look") appear in neither front door.
**Minimal fix:** put `vision.md:26` verbatim at the end of `OVERVIEW.md`'s
Layer 1, attributed to `vision.md`; add the observatory/harness pair as one
sentence in Layer 2.

**14. [Non-blocking] `OVERVIEW.md` never states the intended physical shape.**
`README.md:14-18` calls the local-first daemon plus browser app a doctrine-level
platform commitment; the document billed as "30 seconds to full depth"
(`README.md:92-93`) omits it at every layer.
**Minimal fix:** one sentence in Layer 2 near `:87-90`, phrased as intent.

**15. [Non-blocking] Lifecycle-stage label drift between the two entry files.**
`README.md:7` "pre-specification project-shape normalization" vs
`PROJECT-STATUS.md:12` "Final pre-specification".
**Minimal fix:** use `PROJECT-STATUS.md`'s wording in `README.md:7`.

**16. [Non-blocking] `vision.md` presentation (rules settled, rendering only).**
VIS-1's five-rank ordering (`vision.md:82-94`) is the most-cited object in the
corpus and is inline prose inside a 13-line paragraph; VIS-5 (`:141-165`) is 25
lines, roughly double any other rule, with its core in sentence one and 22 lines
of qualification after.
**Minimal fix (editorial, semantic-delta review as usual):** render VIS-1's
`(1)…(5)` as a numbered list; split VIS-5's adapter and proposal-artifact
qualifications into a sub-paragraph beneath the rule sentence.

---

*Reviewer note on epistemic status: all `path:line` claims above are [Observed]
from the files in scope. The README-glossary enumeration in §6d is [Observed]
via a scripted walk of every `README.md` in the working tree excluding `.git`,
`_bootstrap/`, and `node_modules` (15 files, one match). Judgments of reader
effect, memorability, and normative force are [Inferred].*
