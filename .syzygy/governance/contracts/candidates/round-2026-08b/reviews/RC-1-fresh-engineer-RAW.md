# RC-1 — Fresh-engineer comprehension review (RAW)

**Reviewer posture.** Independent fresh-context senior engineer. No prior
exposure to this project. Read only inside a clean `git clone` at
`…/scratchpad/clean-clone`. Did not read the working tree, did not read any
`_bootstrap/` tree (none exists in the clone), and deliberately did not read
`round-2026-08/reviews/` as a source — two lines from stored reviews surfaced
incidentally in a `grep` sweep and are marked where used.

**Date of review:** 2026-08-05. **Clone:** 191 tracked files, 1 git tag
(`doctrine-adopted-2026-07-30`).

**Method note.** Every quantitative claim below was produced by running the
command in the same session. Where a claim is universal ("all 32 modules"), the
sweep covering it is shown. Where a figure is compared against a document's
own figure, both were computed here, not copied.

---

## PASS A — README only, 30 seconds

Read: `README.md` (802 words). Nothing else.

| # | Question | Score | Basis |
|---|---|---|---|
| 1 | What is Syzygy? | **2** | `README.md:3-5` — "A specification-driven control plane for software projects: humans define what should be true, evidence shows what is true, and agent fleets do bounded work to close the difference — with the difference always rendered honestly." Reinforced concretely at `README.md:14-16`: "a **local-first daemon with a browser app**". |
| 2 | Why does it exist? | **2** | `README.md:22-25` — "A day of agent-fleet work too often ends with oversized diffs, scattered completions, and no coherent account of what changed or whether it matched intent." Plus the three-state answer at `README.md:27-32`. |
| 3 | What stage is it at? | **2** | `README.md:7-12` — "**Current stage: pre-specification project-shape normalization.** This repository contains **no application code, no behavioral specifications, and no implementation backlog — deliberately.**" And `README.md:111` — "Everything." under *What is not implemented*. |
| 4 | Where do I read next? | **2** | `README.md:90-104` — the eight-item numbered "Start here" list, ordered, each with a one-line purpose. |

**Pass A total: 8/8.** This is an unusually good 30-second front door. Three
specific things it does that most repositories do not: it states the negative
inventory before the positive one; it distinguishes *intended shape* from
*current capability* in the same paragraph (`README.md:14-18`); and it tells
me the license is undeclared and why that blocks contribution
(`README.md:117-124`) rather than leaving me to discover it.

One friction point, recorded now and relevant to Pass B: the section heading
`README.md:40` is "**The four experiences**", and the table lists four named
surfaces. Adopted doctrine knows **three**
(`.syzygy/governance/doctrine/README.md:38-39`: "Polaris / Trajectory /
Orrery — provisional codenames for Syzygy's three surfaces"). The README's
body text does correct this immediately (`README.md:49-53`: Mission Control
"is a workspace-level operator capability, not a fourth project truth
surface… defined by candidate contract RFC-0010 and a pending doctrine
amendment (D3), neither yet accepted"). A skimmer reads the heading; a reader
reads the correction. Non-blocking, but the heading is the only line in the
front door that overstates.

---

## PASS B — the README's "Start here" default path, ~10 minutes

Read, in order: `.syzygy/intent/OVERVIEW.md` (1,430 w),
`.syzygy/governance/doctrine/vision.md` (2,156 w), `PROJECT-STATUS.md`
(709 w). Then `CONTRIBUTING.md` (550 w) and `SECURITY.md` (582 w) to close the
front door. Total ≈ 5,400 words. I did **not** open any RFC in this pass.

### The five comprehension questions

**1. Desired vs observed vs execution state — GOT IT, cleanly.**

Desired state is what humans have declared should be true: doctrine and
specifications. Observed state is what evidence shows is actually true: code,
tests, CI, runtime captures. Execution state is the record of fleet activity —
runs, merges, work lifecycle — and it is a *third* thing that is never
evidence for either of the other two. The gap between desired and observed is
the reconciliation work; agent fleets are the actuators that close it.

Source: `OVERVIEW.md:37-44` states it and the mermaid diagram at
`OVERVIEW.md:47-59` makes the non-substitution visually explicit — the arrow
from Exec to Observed is labelled `"merged changes — evidence, never proof"`.
Confirmed in adopted doctrine at `vision.md:19-24`. This is the single
clearest idea in the corpus and it survives every restatement I checked.

**2. Polaris / Trajectory / Orrery / Mission Control — GOT IT, with one
caveat.**

`OVERVIEW.md:66-75`. Polaris = intent surface ("what is this project supposed
to be?"). Trajectory = work surface ("what remains, what runs, what merged
*without yet being reconciled*?"). Orrery = map surface, a spatial view over
capability identities where Unknown is a first-class colour. Mission Control =
workspace-level operator surface for bounded delegated missions across
projects — explicitly *not* a fourth project truth surface, and explicitly
gated on candidate RFC-0010 plus unadopted amendment D3.

The load-bearing structural claim — that the first three are projections over
one kernel and none is independently authoritative — is at `OVERVIEW.md:61-64`
and `README.md:49-51`.

Caveat: the four names are working codenames only
(`OVERVIEW.md:15-17`), which the corpus repeats often enough that I stopped
noticing it. That is the right trade.

**3. Why merged work is not proof intent was satisfied — GOT IT, and this is
the argument's best passage.**

Merging is an execution-state event. It says a change landed; it says nothing
about whether the change satisfies the intent revision that warranted it.
`OVERVIEW.md:121-128` makes it operational: every merged change enters a
reconciliation chain and stays visibly `reconciliation-pending` until checked
against *the exact intent revision that warranted it*, and the four terminal
answers — reconciled-with-evidence, Unknown(reason), unsatisfied,
contradiction-raised — "are four different answers that never share a
rendering." The sentence that sold me: "A wall of pending states on a
fleet-built project is *correct output*, not failure" (`OVERVIEW.md:126-127`).

**4. What Syzygy is permitted to write — GOT IT.**

Direct project-content writes are confined to exactly two namespaces:
`openspec/**` and `.syzygy/**`. Everything else is read-only or reached
through typed, explicitly authorized adapters. It never writes implementation
code; it may generate code-shaped *proposals* as governance artifacts but may
never apply or merge their generated contents. Source: `OVERVIEW.md:142-150`
for the summary, `vision.md:141-165` (VIS-5) for the binding text. VIS-5 is
also where I learned the rule is about attribution and separation, not human
control of code — an unusually honest carve-out (`vision.md:160-162`).

`CONTRIBUTING.md:32-37` adds the distinction that actually mattered to me as a
would-be contributor: VIS-5 binds *Syzygy the system*, not people working on
this repository. Without that paragraph I would have concluded I could not
edit `README.md`.

**5. What remains unimplemented — GOT IT, unmistakably.**

Everything. `README.md:111-115`: "There is no daemon, no UI, no graph store,
no adapter, no 3D view, no endpoint, and no chosen language, framework, or
database." `OVERVIEW.md:87-91` repeats it. `PROJECT-STATUS.md:30-31` marks
gates 11 (OpenSpec) and 12 (implementation) `⛔ Not started`. `SECURITY.md:5-6`
says it a third way: "no running software, no deployed service, and no
released artifact."

### Terms I had to learn to get through the DEFAULT path

Marked **[load-bearing]** (the argument does not work without it),
**[jargon]** (a name for something I could have been told in plain words), or
**[provenance]** (bookkeeping detail that interrupted the argument).

| Term | First seen | Verdict |
|---|---|---|
| desired / observed / execution state | `OVERVIEW.md:37` | **[load-bearing]** — the whole thesis |
| reconciliation work / reconciliation-pending | `OVERVIEW.md:43,122` | **[load-bearing]** |
| Unknown (as a status, capitalized) | `README.md:38` | **[load-bearing]** |
| evidence / Observed / Inferred | `OVERVIEW.md:111-117` | **[load-bearing]** |
| identified evaluation; (source snapshot, as-of instant) | `OVERVIEW.md:115-117` | **[load-bearing]**, but dense on first contact |
| kernel / surface / projection | `OVERVIEW.md:61-64` | **[load-bearing]** |
| typed authority | `OVERVIEW.md:99` | **[load-bearing]** |
| adapter | `README.md:70` | **[load-bearing]** |
| contradiction (vs gap) | `OVERVIEW.md:106` | **[load-bearing]** |
| Polaris / Trajectory / Orrery / Mission Control | `README.md:44-47` | **[jargon]** — mitigated by mandatory literal subtitles, which is the right mitigation |
| Syzygy itself | `README.md:1` | **[jargon]**, unavoidable |
| Mission envelope / attention items | `OVERVIEW.md:155-157` | **[load-bearing]** for Layer 3 |
| Project Genome | `OVERVIEW.md:81-82` | **[jargon]** — one capitalized coinage for "the complete normative corpus", used twice, defined nowhere on the default path except by apposition |
| warrant | `OVERVIEW.md:132` (diagram) | **[load-bearing]** but *undefined on the default path* — it appears first inside a mermaid node, `Intent["Approved intent (warrant)"]`, and is never given a sentence |
| gate-backed evidence | `OVERVIEW.md:127` | **[load-bearing]** but undefined until RFC-0004 |
| actuator toolchain | `vision.md:25,38,58` | **[jargon]** — see finding 4; genuinely undefined anywhere in the clone |
| escape property | `vision.md:56,62,229` | **[jargon]** — used three times as though standard; means "the property that stops this being merely X" |
| proving ground | `vision.md:241` | **[jargon]**, undefined |
| V0 / V1 | `vision.md:17` | **[load-bearing]** |
| VIS-n / SEC-n / SDR-n / CC-* / RFCn-m | throughout | **[load-bearing]** — the citation system is the corpus's best feature |
| D1 / D2 / D3 | `AGENTS.md`, `PROJECT-STATUS.md:20-27` | **[provenance]** — three unrelated amendment/decision IDs sharing a `D` prefix; D1 is an adopted doctrine amendment, D2 an owner approval decision, D3 a proposed doctrine amendment. I had to build a table |
| act 1…act 5 | `PROJECT-STATUS.md:23-27` | **[provenance]**, but necessary |
| RFC3-16 / RFC3-16(a) | `OVERVIEW.md:3,151` | **[provenance]** on the default path — cited three times before Layer 4, always as a reason something is *not* binding. It is the single most intrusive citation in the overview |
| "owner-adopted (bootstrap, uncorrelated)" | `OVERVIEW.md:150` | **[provenance]** — a rendering string quoted verbatim into a 5-minute explainer |
| candidate vs accepted vs adopted vs approved vs recorded | `README.md:79-85` | **[load-bearing]** and correct, but five statuses is four more than most readers expect |
| CG-7 / CG-7d | `PROJECT-STATUS.md:59-61` | **[provenance]** — a check ID in the status page's blocking-defect paragraph |
| semantic delta | `CONTRIBUTING.md:43` | **[load-bearing]** for contributors |
| fresh-reader review | `vision.md:110` | **[load-bearing]** |
| term registry | `OVERVIEW.md:95,187` | **[provenance]** — named twice, never linked (finding 8) |

**Count: 12 load-bearing, 8 jargon, 6 provenance.** That ratio is defensible.
The jargon that actually costs the reader is the *undefined* jargon —
`warrant`, `actuator toolchain`, `escape property`, `Project Genome`,
`proving ground` — not the codenames, which are disciplined by their
mandatory literal subtitles.

### Was Layer 3 / Layer 4 forced on me?

**Layer 4: genuinely optional and genuinely useful.** It is a bare
concept → owning-authority → status table (`OVERVIEW.md:169-188`). It reads as
a drawer, not as prose. I could have closed the file at line 166 and lost
nothing.

**Layer 3: nominally optional, structurally forced, and it is where the
overview stops being an argument.** Three observations:

1. There is no navigational affordance to skip it. The layers are `##`
   headings in one 194-line file with no table of contents and no "stop here
   if…" instruction. `OVERVIEW.md:9-11` tells me where *anchors* live, not
   where *I* should stop. Layer 2 ends at line 95 with "Foundational terms
   used so far… the full vocabulary lives in the term registry" — which reads
   as a handoff to a glossary, not as a permission to stop.

2. Layer 3's density is a step change. Layer 2 carries 3 source-anchor
   citations. Layer 3 carries, by my count, 21 clause citations in 68 lines —
   `RFC1-21, RFC2-15, RFC2-3, RFC2-4, RFC2-17…21, RFC4-13, RFC8-28, RFC3-3,
   RFC3-16(a)/(b), RFC5-25, RFC10-1…16` plus VIS/SEC. Every one of them binds
   nothing. The header warns me of this (`OVERVIEW.md:10-11`, "Anchors marked
   *candidate* cite contract clauses that bind nothing until owner
   acceptance"), which makes the reading experience honest and exhausting at
   the same time.

3. Two Layer-3 passages are *not* drill-down, they are the argument's
   conclusion, and burying them costs the document. The write-boundary
   paragraph (`OVERVIEW.md:142-150`) contains the single most consequential
   sentence in the overview — "Fleet workers are untrusted even inside the
   writable plane… anything that *authorizes* an effect is honored only with
   owner-act provenance the repository itself cannot forge; until that
   mechanism ships, every authorization gate renders its gap honestly." That
   belongs in Layer 2. Similarly `OVERVIEW.md:158-163` — that whether D3 plus
   RFC-0010 satisfy VIS-4's licensing mechanism "is an open owner question,
   not a settled one" — is the most important open question in the project and
   it is in the fourth paragraph of the technical layer.

**Verdict on the layering:** Layer 4 earns its label. Layer 3 does not — it is
presented as optional depth but carries two Layer-2-grade conclusions, and the
file provides no mechanism (TOC, per-layer time estimate, explicit exit) to
act on the optionality it claims. This is a *structure* finding, not a content
one; the content of Layer 3 is good.

---

## PASS C — one concrete task, one hour

**Task:** "I want to change how evidence adapters report CI results."

### The path I actually took

| Step | File | Why | Words |
|---|---|---|---|
| 1 | `README.md:73-88` (already read) | Authority table → "Load-bearing technical contracts" → `contracts/candidates/` | — |
| 2 | `.syzygy/governance/contracts/candidates/README.md` | Directory orientation. Layout table (`:18-31`) named `TASK-TO-CONTRACT-INDEX.md` as "task-routing" | 418 |
| 3 | `TASK-TO-CONTRACT-INDEX.md` | Task-class table `:41-50`. My task ≈ row "Adapter author" → RFC-0004 general + adapters, RFC-0008 state/cost, RFC-0003 governance-homes | 1,196 |
| 4 | `06-CONTEXT-LOAD-MAP.md` | The cited source that "wins over" the index (`TASK-TO-CONTRACT-INDEX.md:6-7`). Confirmed the row verbatim at `:42-43` | 680 |
| 5 | `rfcs/RFC-0004/README.md` | Package index + deterministic clause lookup rule (`:53-58`) | 1,676 |
| 6 | `rfcs/RFC-0004/named-adapters.md` | **RFC4-13 — the governing clause.** Found without search via the lookup rule | 3,685 |
| 7 | `rfcs/RFC-0004/general-contract.md` | RFC4-2/4-7: no output is admissible unless the adapter is registered | 1,680 |
| 8 | `policies/craft-and-care/testing-and-verification.md` (CC-TEST-2) | RFC4-13 cites it by name at `named-adapters.md:197-200` | 1,113 |

**Words read to reach the governing clause: ≈ 10,450.** Against a contract
corpus of **99,094 words** (`verify_final_prespec.py`, run in session) that is
**10.6%**. Against the whole clone it is smaller still.

### The answer I arrived at

RFC4-13 (`named-adapters.md:135-210`) governs test/CI/gate observers.
Concretely, changing how an evidence adapter reports CI results is bounded by:

- Syzygy **reads** CI reports; it does not run them (SEC-3).
- A gate outcome is emitted `gate-backed` only when *both* the
  retention/format predicate and the provenance predicate hold; otherwise
  `report-fact`; a bare LLM assertion is `asserted-by-worker`. **The observer
  never upgrades a tier** (`named-adapters.md:142-149`).
- `gate-backed` requires **exactly one of four routes**: Syzygy-launched
  profiled run; externally confirmed-and-captured CI/hosting run (RFC4-13(a));
  owner-declared trusted-external-oracle policy, scoped to a (project, gate
  class) pair *with an expiry*; or a governed-checker execution (RFC4-13(b)).
- Anything I add must satisfy RFC4-2's declaration set and be in the RFC4-7
  registry, whose entries are honored only under RFC3-16(a).

That is an actionable, testable brief. **Yes — I could have acted correctly
without reading the whole corpus**, with two qualifications recorded as
findings 1 and 2 below.

### Wrong turns and dead ends

- **No dead links.** Every path I followed resolved. `CG-1a` (51 markdown
  links) and `CG-1b` (714 code-span references) both report 0 findings, and my
  own traversal agrees — with one exception I found by hand, finding 3.
- **One near-miss on entry.** The candidates directory has both `README.md`
  and `00-README.md`. I opened `README.md`, which was correct; `00-README.md`
  is the rev10 packet's own delivery report, described as "packet history"
  (`candidates/README.md:30`). A reader who opens the numbered one first lands
  in superseded process material. Cheap to recover from; worth one line of
  disambiguation.
- **One genuinely wrong route, from the routing index itself.** See finding 1.
- **One stale pointer in the directory README.** See finding 6.

---

## Factual records requested

### A. Contradictory, circular, or self-undermining material

**A1 — The routing index the reader is sent to carries three findings that are
themselves false.** `TASK-TO-CONTRACT-INDEX.md` §Findings:

- **T-4** (`:110-113`) asserts "`06-CONTEXT-LOAD-MAP.md` line 16 carries a
  stale module figure: RFC-0003 governance-homes **4,401 w**, actual
  **4,414 w**." `06-CONTEXT-LOAD-MAP.md:26` reads **4,414**. The claim is
  false and the line number is wrong (the RFC-0003 row is line 26).
- **T-2** (`:97-102`) asserts fixtures 2, 4 and 5 state stale totals of
  18,302 / 10,854 / 12,830. The fixtures now read **18,315**
  (`fixtures/context-selection-2-trajectory-adapter.md:25`), **10,893**
  (`…-4-execution-profile.md:26`) and **12,843**
  (`…-5-cross-project-mission.md:23`) — i.e. exactly the re-measured values.
  The "As stated in the fixture … **stale**" column at `:72-75` is wrong in
  three of five rows.
- T-4 additionally claims "The rest of 06's per-module table reproduces
  exactly (`wc -w`, all 32 modules, same date)". **I ran that sweep.** 30 of
  32 rows reproduce; **2 do not**: `06-CONTEXT-LOAD-MAP.md:33` states RFC-0010
  = 3,096 (actual **3,103**) and `:34` states RFC-0011 = 2,257 (actual
  **2,264**). Verified by three independent measurements agreeing —
  `wc -w`, `verify_final_prespec.py`, and `scripts/context_load.py`.

The pattern is exactly the hazard the corpus itself names: a derived value
quoted outside its owning artifact goes stale silently. Here the *staleness
report* went stale.

**A2 — The defining acceptance record's supersession is circular in a public
clone.** `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:3-8`: "This record
defines the owner gates over the rev10 final pre-specification package and, on
the owner's act, supersedes `_bootstrap/rfc-phase/FOUNDATIONAL-RFC-ACCEPTANCE-RECORD.md`
(rev9) **as the acceptance authority**." So until an act, the acceptance
authority is a file that does not exist in the clone, while the ceremony that
would produce the act is defined by the record that has not yet superseded it.
The document is aware of the shape of this problem — `:36-39` argues that
supersession of an authority "must not be conditional on exercising the
authority that supersedes it" — and resolves it by asserting a retirement
notice was written into the rev9 record. **That notice is unverifiable in a
clone.** Self-consistent, unfalsifiable from here.

**A3 — "Public" toolchain that is machine-local.** `vision.md:38` (adopted
doctrine): "it assumes the public actuator toolchain (README glossary), never
one private machine." `round-2026-08/PUBLIC-CLONE-AUTHORITY-MATRIX.md:35`
classifies the same toolchain's engineering baseline as
"machine-local … external … out of scope for this repo". The craft cluster
adopts it by reference from `~/.claude/skills/th-engineering/subskills/`
(`policies/craft-and-care/README.md:18`). Doctrine's word for it is *public*;
the corpus's own record of it is *machine-local*.

**A4 — Two similarly-named acceptance records, with the wrong one winning on a
point where it is wrong.** `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`
(defining) and `round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md` (presenting).
The presenting record correctly states "Where the two disagree, that record
wins and this one is stale" (`:12-13`). They disagree on act 3's install
source path, and the defining record is the one that is wrong — see finding 3.
The precedence rule therefore propagates the defect rather than containing it.

**A5 — The overview's self-declaration cites a clause that binds nothing to
establish that its own stamp binds nothing.** `OVERVIEW.md:1-4`: "adopted only
by its own owner act… (RFC3-16: this stamp is a self-declaration; effective
status lives in the owner-act record)." RFC3-16 is a candidate clause. Honest,
labelled, and unavoidable at this lifecycle stage — recorded as observed
circularity, not as a defect.

**A6 — `PROJECT-STATUS.md` disclaims being a sole source while being one.**
`:3-8`: "it **must not be the sole source** for any fact it states — each row
cites the owning record." Gate rows 11 and 12 (`:30-31`, OpenSpec and
implementation, both `⛔ Not started`) cite owning record "—" (none). The
verification-results paragraph (`:89-93`) is also sole-source. Both facts are
independently checkable — I reproduced 15 OK / 7 WARN / 0 FAIL over 22 checks
exactly — so this is a wording overreach, not a truth problem.

### B. Documents that disclaim authority while being the only home of a fact

**B1 — Task→module routing exists only in files that disclaim authority.**
`06-CONTEXT-LOAD-MAP.md:3` — "**Derived measurement record — never
authority.**" `TASK-TO-CONTRACT-INDEX.md:1` — "derived, never authority",
`:6-7` — "`06-CONTEXT-LOAD-MAP.md` is the cited source and wins over this
file". `06` in turn says the contracts win over it. Follow the chain to the
end and the question "which modules must I load for task X?" has **no
authoritative answer anywhere** — the modules carry `applies_to`,
`depends_on`, `governs` front matter, but no module states a task class.
`TASK-TO-CONTRACT-INDEX.md:24-30` says so explicitly: charter §11.5's
`task_classes` / `risk_classes` fields "**do not exist on any of the 32
modules**". Meanwhile RFC11-4 makes mandatory selection "deterministic from
the index metadata plus the work warrant" and RFC11-6 makes incomplete context
Unknown that blocks launch. The mechanism the contract presumes is not
present, and its stand-in disclaims authority. This is the most consequential
instance of the pattern.

**B2 — Finding T-1 itself.** The fact that no module carries the §11.5 task
metadata appears, so far as my sweep found, only in
`TASK-TO-CONTRACT-INDEX.md:24-30, 90-96` — a file that states nothing in it
may be cited as authority.

**B3 — `PROJECT-STATUS.md`.** See A6.

**B4 — `SECURITY.md`'s executable-surface inventory** (`:10-20`) is the only
enumeration of what in this repository executes. It does not disclaim
authority, and I verified it: `git ls-files` outside `.syzygy/` returns
exactly the five hooks, the workflow, `.claude/settings.json`,
`scripts/check_governance.py`, plus data and markdown. `.claude/settings.json`
does run `bd prime` on `SessionStart` (and on `PreCompact`, which the file
does not mention — a one-word omission, not a misstatement). Accurate.

### C. Files I was pointed to that do not exist in this clone

| Pointer | Cited at | Status |
|---|---|---|
| `topology/` (act 3 install source) | `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:92` | **Does not exist.** Bundle is at `.syzygy/map/topology-candidates/`. See finding 3 |
| "README glossary" | `vision.md:16`, `vision.md:38` | **Ambiguous, effectively dead.** `README.md` has no glossary (`grep -in glossary README.md` → no match). A glossary exists at `.syzygy/governance/doctrine/README.md:15-49`, and it does **not** define "actuator toolchain" |
| `~/.claude/skills/th-engineering/subskills/` | `policies/craft-and-care/README.md:18`, `engineering-bar.md:4-5` | **Not in clone, by design.** See finding 4 |
| `_bootstrap/rfc-phase/FOUNDATIONAL-RFC-ACCEPTANCE-RECORD.md` | `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:5` | Not in clone. Declared git-excluded history; but see A2 |
| `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` | many | **Correctly absent** — created by the first act. Declared at `PROJECT-STATUS.md:33-35`, allowlisted as CG-1c forward reference |
| `.syzygy/project.yaml`, `contracts/rfcs/**` | RFC-0003, topology | **Correctly absent** — forward references, CG-1c |
| 26 frozen-packet paths (`final-prespec/…`, `rev9` RFC filenames, `reviews/0N-…`) | matrix-rows, history, stored reviews | **Correctly absent** — CG-1d, "unresolvable in a clone by construction" |

Everything in the "correctly absent" rows is declared. Only the first two rows
are defects.

### D. Is the front door honest about what does and does not exist?

**Yes — substantially, and better than any comparable repository I have
read.** Specifics I checked rather than assumed:

- `README.md:111` "Everything." is not softened anywhere.
- `PROJECT-STATUS.md:89-93` claims "packet verifier PASS; both index builders
  report no drift; `check_governance.py` 15 OK, 7 WARN, 0 FAIL over 22
  checks." **I reproduced all four, exactly.**
- All **five** act arguments verify from clone bytes, computed independently:
  act 1 `f2914fc5…` = `sha256sum ACTIVE-CONTRACT-MANIFEST.txt`; act 2
  `3858820f…` = `testing-and-verification.md`; act 3 `7a3b2249…` =
  `BUNDLE-MANIFEST.md`; act 4 `ce7794fd…` = `OVERVIEW.md`; act 5 `0328cb37…` =
  `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md`. `sha256sum -c
  ACTIVE-CONTRACT-MANIFEST.txt` → 32/32 OK; all 9 topology member digests
  verify.
- `PROJECT-STATUS.md:66-70` volunteers that **no fresh-context review has been
  run over the current bytes** and that the planned ninth review "was never
  run". `round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md:186-211` states it at
  length, including "'small and recorded' is the author's claim about the
  author's own edits, which is precisely the claim review exists to test."
  That is the strongest honesty signal in the corpus.
- `CONTRIBUTING.md:3-9` and `README.md:117-124` are consistent on the license
  gap. `SECURITY.md:52-58` explicitly declines to claim its own governance
  records are independently verified.

**Three honesty gaps**, all narrow:

1. `CONTRIBUTING.md` requires that a change "confirm no active artifact depends
   on the git-excluded `_bootstrap/**` tree for essential meaning" (`:64-66`)
   and says nothing about the *other* unreadable dependency — the machine-local
   `th-engineering` bar that the approved engineering policy adopts wholesale.
   `round-2026-08/PUBLIC-CLONE-AUTHORITY-MATRIX.md:35` directs exactly this:
   "disclose in CONTRIBUTING (do not import)". `grep -rn th-engineering
   CONTRIBUTING.md` → no match. **The directed disclosure was not made.**
2. `README.md:40` "The four experiences" (see Pass A).
3. `round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md:218` says the clone
   simulation covered "190 files"; this clone tracks **191**. Trivially
   explicable, but it is a count quoted as evidence.

---

## VERDICT: EXCEPTIONS

1. **[Blocking] The defining acceptance record's act-3 install step names a
   directory that does not exist.**
   `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:92` — "act 3 installs the
   bundle (shipped in this packet at `topology/`) to `.syzygy/map/topology/`".
   There is no `topology/` directory anywhere in the repository
   (`find . -type d -name topology` → empty); the bundle is at
   `.syzygy/map/topology-candidates/`, as `candidates/README.md:36-37` itself
   states. The presenting record has it right (`round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md:86`),
   but the precedence rule (`:12-13`) makes the *defining* record win. Act 3's
   ceremony step 3 therefore cannot be executed as written. Compounding: the
   repository's own link checker cannot see this, because
   `scripts/check_governance.py:198` classifies any reference matching
   `^(\.\./)*(topology|history|matrix-rows)/` as frozen-packet history and
   demotes it to a CG-1d WARN — an allowlist written for stale *history*
   references is silently absorbing a live *instruction*. CG-1b's "714
   references examined, 0 findings" is therefore not the guarantee it reads
   as.

2. **[Blocking] The only task→module routing in the repository is
   under-inclusive for the exact task I was given, in a way that RFC11-6 says
   should block launch.** `06-CONTEXT-LOAD-MAP.md:42-43` and
   `TASK-TO-CONTRACT-INDEX.md:47` route "Adapter author" to RFC-0004 (general
   + adapters) + **RFC-0008 state/cost** + RFC-0003 governance-homes. For
   *evidence* adapters reporting CI results this is wrong in both directions:
   - **Missing:** `rfcs/RFC-0002/rendering-vocabularies.md`, which owns
     RFC2-25, the tier registry that defines `gate-backed` / `report-fact` /
     `asserted-by-worker` — the vocabulary RFC4-13 emits and cites five times
     (`named-adapters.md:143,148,192,404`). Confirmed via
     `05-CONTRACT-INDEX.yaml:80`. Also missing RFC-0005, which owns RFC5-21,
     the profiled run that *is* `gate-backed` route 1.
     `rfcs/RFC-0004/README.md:10` declares `depends_on: [RFC-0001, RFC-0002,
     RFC-0003, RFC-0005]` — the reader-map row contradicts the package's own
     declared dependencies.
   - **Surplus:** RFC-0008 state/cost is the work-state vocabulary and cost
     accounting; it is in RFC-0004's `provides_to`, not its `depends_on`.
   A packet compiled from this row is incomplete against its own dependency
   declaration, and RFC11-6 makes incomplete context Unknown that "by default
   blocks launch". I recovered only because RFC-0004's clause-lookup rule and
   `05-CONTRACT-INDEX.yaml` let me chase citations by hand.

3. **[Blocking] The task-routing index publishes three findings that are
   false, one of which is a universal claim contradicted by a two-row
   counterexample.** `TASK-TO-CONTRACT-INDEX.md` T-4 (`:110-113`) and T-2
   (`:97-102`, and the "stale" column at `:72-75`) are all false against
   current bytes — see record A1 for each. T-4's "The rest of 06's per-module
   table reproduces exactly (`wc -w`, all 32 modules, same date)" fails on
   `06-CONTEXT-LOAD-MAP.md:33` (RFC-0010: claims 3,096, actual 3,103) and
   `:34` (RFC-0011: claims 2,257, actual 2,264). Full 32-row sweep run in
   session; 30 reproduce, 2 do not. A reader who trusts these findings will
   mistrust four correct files and trust one incorrect claim. Note that
   `06-CONTEXT-LOAD-MAP.md` is *also* independently stale in those two rows.

4. **[Blocking] Owner-approved engineering policy adopts, by reference, a
   baseline no clone can read, pinned by a date rather than a digest.**
   `policies/craft-and-care/README.md:14-20` and `engineering-bar.md:4-5`
   adopt the `th-engineering` `engineering-bar` (biases 1–9 + Definition of
   Done), `test-rigor` (rules 1–8) and `dependency-hygiene` (rules 1–7) from
   `~/.claude/skills/th-engineering/subskills/`. The cluster explicitly "does
   not restate" them (`README.md:22`), so `CC-BAR-1`'s three registered
   overrides (`engineering-bar.md:14-24`) reference "canonical bias 1",
   "canonical test-rigor rule 2", "canonical rule 6" — none readable here. The
   pin is "the installed `th-engineering` bar **as read on 2026-07-30**"
   (`README.md:37-38`) — a date, not a content digest, so the drift check the
   pin exists to enable ("mechanical rather than hopeful", `:43-44`) cannot
   actually be performed by anyone but the machine owner. Consequence: a fresh
   engineer cannot determine this project's definition of done. This *is*
   disclosed (`round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md:76-78`), which
   is why I rate it blocking-for-comprehension rather than concealed — but
   disclosure does not make the bar readable, and act 2 binds a policy whose
   tier-3 baseline is unauditable.

5. **[Non-blocking] Adopted doctrine's first substantive sentence cites a
   glossary that the reader cannot find, for a term the glossary does not
   define.** `vision.md:16` — "Syzygy (see README glossary)"; `vision.md:38` —
   "the public actuator toolchain (README glossary)". `README.md` has no
   glossary. `.syzygy/governance/doctrine/README.md:15-49` has one; it defines
   *Syzygy* but never the phrase "actuator toolchain" — its nearest entry
   (`:60-63`) names "the `/th-*` skills and claude/codex CLIs" as "the
   designated initial agent toolchain". A repo-wide sweep for "actuator
   toolchain" returns 13 uses and **zero definitions**. Non-blocking only
   because repairing it is a doctrine amendment, which is the owner's act, not
   an editorial fix.

6. **[Non-blocking] The candidate directory's own layout table points at the
   superseded D3 draft and omits the live one.**
   `candidates/README.md:31` lists `DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md`
   as "The D3 proposal (act 5, optional)". Act 5's subject is
   `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` **rev1**
   (`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:19`;
   `PROJECT-STATUS.md:27`), which "supersedes `…-DRAFT.md`, whose `vision.md`
   insertion cannot be applied as written (SD-8)". The rev1 file is a
   top-level member of that very directory and appears nowhere in its layout
   table. A reader orienting from the directory README is routed to the
   version that is known not to apply.

7. **[Non-blocking] `OVERVIEW.md` Layer 3 is labelled optional drill-down but
   carries two Layer-2-grade conclusions, and the file offers no mechanism to
   act on the optionality.** No TOC, no per-layer exit instruction, no time
   estimate. The write-boundary/unforgeable-provenance paragraph
   (`:142-150`) and the open VIS-4 licensing question (`:158-163`) are the
   overview's two most important claims and are both below the "five-minute
   argument" fold. Layer 4, by contrast, is a genuine drawer and works.

8. **[Non-blocking] Five terms load-bearing on the default path are used
   without definition anywhere a default-path reader will reach.** `warrant`
   (introduced inside a mermaid node, `OVERVIEW.md:132`), `actuator toolchain`
   (see 5), `escape property` (`vision.md:56,62,229`), `Project Genome`
   (`OVERVIEW.md:81`, defined only by apposition), `proving ground`
   (`vision.md:241`). The "term registry" is named twice as the answer
   (`OVERVIEW.md:95`, `:187`) and **never linked** — `:95` gives no path and
   `:187` gives only a directory; the file is
   `contracts/candidates/policy-candidates/TERM-REGISTRY.md`, and it is itself
   an unaccepted candidate (`round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md:178`,
   register items P-16/P-17/P-18 — "eight undefined public terms").

9. **[Non-blocking] `CONTRIBUTING.md` omits a disclosure its own round record
   directed it to make.** `PUBLIC-CLONE-AUTHORITY-MATRIX.md:35` prescribes
   "out of scope for this repo; **disclose in CONTRIBUTING** (do not import)"
   for the th-engineering tier-3 baseline. `CONTRIBUTING.md` does not mention
   it, while `:59-66` does require clone-reconstructability against
   `_bootstrap/**` only. The public-clone rule is enforced against one
   unreadable dependency and silent about the other.

10. **[Non-blocking] `README.md:40` "The four experiences"** overstates against
    adopted doctrine's three surfaces (`doctrine/README.md:38-39`). Corrected
    in the body four lines later (`:49-53`); the heading is what a skimmer
    keeps.

11. **[Non-blocking] Minor front-door inaccuracies.**
    (a) `round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md:218` says the clone
    simulation covered 190 files; this clone tracks 191.
    (b) `PROJECT-STATUS.md:3-8` says it "must not be the sole source for any
    fact it states — each row cites the owning record", but gate rows 11 and
    12 (`:30-31`) cite "—".
    (c) `SECURITY.md:14-15` describes `.claude/settings.json` as running
    `bd prime` "on session start"; it also registers a `PreCompact` hook.
    (d) The candidates directory has both `README.md` and `00-README.md` with
    no disambiguating first line on the latter.

**What I am explicitly not raising.** The five act digests all verify; the 32
module digests verify; both index builders report no drift; the packet
verifier passes; `check_governance.py` reproduces its stated 15/7/0. The
clause-numbering discipline, the per-package deterministic lookup rule, and
the "candidate binds nothing" banners are the reason a stranger could reach
RFC4-13 in ~10,000 words. The corpus's honesty about its own residual — that
no review has seen the current bytes — is the reason this review found what it
found rather than being told it.
