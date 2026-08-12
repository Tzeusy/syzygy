# Launch Gate — Pre-Specification Readiness

```yaml
status: candidate process policy — owner approval pending, see
  .syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md
owner: the project owner (VIS-4 — no verdict here performs an owner act)
effective_version: v2.2 (candidate; v1.3 was the pilot-administered version)
governs: how pre-specification readiness is evaluated — the question set,
  administration protocol, verdict vocabulary, verdict formula, the
  launch-scope parameters (§8), the structured administration source record
  and its generated report (§5), and the trend log
does_not_govern: whether specifications are authored (the owner's launch
  decision); the content of any artifact under judgment; any acceptance,
  adoption, or approval
amendment_process: semantic delta per NORMATIVE-CHANGE-WORKFLOW.md shape,
  changelog entry in §9, question IDs never renumbered or reused; owner
  approval required once this instrument is in force
record_schema: launch-gate-administration.schema.json (the machine annex of
  §5; an administration source record conforms to it or it is not a record)
canonical_result_home: .syzygy/governance/decisions/launch-gate/
  (administration source records as JSON + their generated reports +
  TREND-LOG.md; the 2026-08-09 pilot record remains immutable at
  .syzygy/governance/contracts/candidates/round-2026-08d/reviews/, in the
  Markdown form v1.3 defined)
```

**What this is.** A benchmark-style question series for judging whether a
vision-guided, spec-driven project is ready to begin authoring specifications.
It is administered to a fresh-context LLM reviewer (or a human) at each
synthesis↔review cycle, and its verdicts are the acceptance criteria for the
"begin specifications" decision.

**What this is not.** Not authority. Not doctrine. Not a contract. A process
instrument only — no verdict here adopts, accepts, or approves anything on the
owner's behalf. The owner reads the verdicts and decides.

**Four artifact classes, never conflated** (v2.0 splits the third — the
record — into its source and its presentation, because asking one Markdown
file to be both a human report and a machine-validated source record is what
produced this instrument's longest defect chain):

```text
Launch-gate policy (this file)
    owner-approved process policy once in force
    human-readable Markdown
    governs how pre-specification readiness is evaluated

Administration source record
    strict structured data (JSON), conforming to the schema named above
    the answers and evidence for ONE administration at a named commit
    never adopts anything; superseded, never edited

Administration report
    generated Markdown, produced from the source record
    a presentation for human reading
    NEVER parsed back as authority, and never the source of any fact

Owner launch decision
    authorizes or refuses specification authoring
    the only one of the four that is an act
```

An administration verdict is never itself an owner act, and a READY verdict
authorizes nothing.

**Design intent.** The questions are formulated *independently of the
project's specification corpus*, so they can detect faults in that corpus
rather than inherit them. Each question is falsifiable (carries a "fails
when"), each verdict must cite evidence, and the whole series is parameterized
so it can later be generalized and concretized into reusable skills (see
§7).

**Versioning.** Question IDs are stable forever — never renumbered, never
reused. Amendments happen in place or by appending, and every amendment gets
a changelog entry (§9); the trend log (§6) is only meaningful across
comparable questions.

---

## 1. Derivation tiers — how independence is kept

Every question is tagged with where it comes from:

- **[U] Universal** — any pre-specification project should pass it, regardless
  of what the project claims about itself. These are the bias hedge: they hold
  even if the project's own goal statement has blind spots.
- **[G] Goal-derived** — follows from the project's *adopted goal statement*
  (its vision/doctrine), which is the thing specifications must serve. Using
  the goal statement is legitimate; using the candidate specification corpus
  is not.

**No question may be derived from the artifacts under judgment.** If a
question can only be stated using the spec corpus's internal structure
(its module names, clause IDs, package boundaries), it does not belong here.

---

## 2. Administration protocol

Give the reviewer:

1. This file.
2. The project's goal statement (vision/doctrine) and public entry document.
3. Read access to the repository at a **named commit**.
4. The parameter block for the project (§8 for Syzygy).

Withhold from the reviewer:

- Authoring history, prior review results, and prior administrations of this
  gate (except when answering F1, which needs the trend log).
- Any summary of "how it's going." The reviewer reads primary artifacts.

The withhold list and the repository read grant reconcile as follows: trees
holding prior reviews and administrations are in scope as **objects** of the
F2/F4/C3 sweeps (they are files, and a stale claim in one is a finding) but
are never **read for content** — their findings, verdicts, and narratives
must not inform any other question's answer. A reviewer who has read them
for content records that fact as a materials deviation.

The materials list is fixed by this file plus the parameter block — never
curated per administration. Any deviation (something added, missing, or
unreadable) is recorded in the results record.

Administration integrity requirements (a record missing any of these cannot
support a gate decision):

- The instrument must be **committed at the administered commit**, and the
  record carries the instrument's sha256 and the parameter block's sha256.
- The record names the commit, and every citation is verified against it.
- **The record is the JSON source, not the report.** A reviewer who submits
  only prose has submitted no record; a report edited after generation is
  not evidence of anything, and `render_launch_administration.py --check`
  is how that is detected rather than assumed.
- A **formal** administration (one a launch decision may rely on) is run
  full, not delta, by a fresh-context reviewer — preferably from a
  different model family than the corpus's authors; if it cannot be, the
  record and the trend row must say so, since a family-constant trend
  measures agreement as much as convergence.
- A repair session may not administer the gate over its own repaired bytes.

Rules for the reviewer:

- **Verdict vocabulary is closed:** `Met`, `Not met`,
  `Not met (out of launch scope)`, `Unknown(reason)`. Nothing else. No
  "partially met," no "met with caveats" — a caveat that matters makes it
  `Not met`; one that doesn't is omitted. The scoped form is lawful only in
  A–D, only for a defect confined to a deferred wave that meets none of
  §4's five blocking conditions; it records the counterexample honestly
  without converting the launch-scope verdict, and both the formula and the
  record validator read it.
- **Met requires cited evidence** — file paths and quoted text. An
  unsupported Met is recorded as Unknown.
- **Not met requires a concrete counterexample** — the artifact and passage
  that fails, or the sweep (with denominator) that shows absence.
- **Unknown is a respectable answer.** No evidence means Unknown, never a
  guessed pass. State what evidence would settle it.
- **Attempt to fail every question first.** The reviewer's job is
  falsification; a question survives a genuine attempt to break it or its
  verdict is not credible.
- **No aggregate score is the deliverable.** A summary table is fine; a
  single percentage or grade substituting for per-question verdicts is not.
  Rollups hide exactly the defects this gate exists to catch.
- **Evidence is commit-anchored.** Every citation must exist at the named
  commit; evidence quoted from any other version is void.

Administration shape:

- **Order:** A → B → C → D → E → F → G. D must precede E3 — the reopen-list
  is only credible from a reviewer who has already demonstrated
  comprehension. Within a section, questions are independent.
- **Effort:** most of A–C are document-level judgments (minutes each); D1,
  D2, E3, and E4 are exercises (tens of minutes); F needs the trend log and
  a corpus sweep. A full administration should fit one focused session — if
  it cannot, that is itself evidence against D1.
- **Full vs delta:** between cycles, a delta administration (re-asking only
  questions whose evidence changed) is acceptable for steering. The gate
  decision itself requires a full administration at the named commit —
  regressions do not announce themselves.
- Record these verdict words exactly. In the structured record the
  vocabulary is a closed enumeration, so a softened verdict is a schema
  error rather than a reading the next reader has to catch. Questions are
  bound at the version administered — a verdict rendered against a
  paraphrased question is void — and every operationalization judgment call
  is recorded in the record's own field, never left in prose.

---

## 3. The question series

### A. Problem and vision

- **A1 [U]** Does the project name a specific, *lived* human problem — one
  whose resolution would be observable in a specific person's behavior?
  *Fails when:* the problem is a category ("agent observability") rather than
  an experience.
  *Evidence:* the vision's problem statement, quoted; whether it names a
  person, a day, a felt failure.

- **A2 [U]** Is the thesis falsifiable — does the project state what evidence
  would prove it wrong, and when that judgment gets made?
  *Fails when:* every conceivable outcome can be narrated as success, or the
  falsifier has no trigger point.

- **A3 [U]** Are the exclusion boundaries sharp enough to *reject a plausible
  near-miss* — could a reviewer, citing only the vision, refuse a product
  that superficially resembles the goal (e.g., "an issue tracker with a nice
  dashboard")?
  *Fails when:* the is/is-not list only excludes strawmen nobody would build.
  *Administer concretely:* judge the pre-written near-miss descriptions in
  the parameter block (`NEAR_MISSES`), accepting or rejecting each with a
  vision citation — never invent softer near-misses on the spot.

- **A4 [U]** Is the problem tractable as scoped: does a smallest end-to-end
  slice exist that exercises the core loop and could be built and honestly
  evaluated with bounded effort?
  *Fails when:* the first demonstrable value requires most of the system to
  exist.

- **A5 [U]** Are the project's consumers enumerated, and does every major
  shape commitment trace to a named consumer's need — and every named
  consumer to at least one commitment that serves it?
  *Fails when:* a consumer exists only in rhetoric, or a shape element serves
  no one who was named.
  *Population:* the closed `MAJOR_SHAPE_COMMITMENTS` list in the parameter
  block — never an all-clause table, and never a population the reviewer
  invents mid-run. *Evidence:* a two-way table (commitment → named consumer
  need; consumer → at least one commitment), either pre-existing in the
  repository or built by the reviewer during the administration. The table
  is evidence for this verdict, never new authority.

- **A6 [U]** Is the scope achievable with the resources the project actually
  has — people, attention, money, calendar — stated rather than implied?
  *Fails when:* the shape silently assumes a team, budget, or cadence the
  project does not have.

### B. Decomposability and sequencing

*The unit of decomposition — "chunk" throughout this section and in D2's
seam task — is bound by `CHUNK_UNIT` in the parameter block, never chosen by
the reviewer or the administering session.*

- **B1 [U]** Does the shape decompose into chunks that are each independently
  understandable, independently acceptable-or-rejectable, and valuable before
  later chunks exist?
  *Fails when:* acceptance is practically all-or-nothing, whatever the
  packaging says.

- **B2 [U]** Is chunk ordering explicit and acyclic — does no chunk's
  acceptance silently presume an unaccepted one?
  *Fails when:* a chunk's text relies on a sibling that could still be
  rejected, with no stated fallback.

- **B3 [U]** Does the first buildable slice generate *evidence about the
  thesis itself*, not just infrastructure?
  *Fails when:* the slice proves the team can build plumbing but nothing
  about whether the product idea is right.

- **B4 [U]** Can any single chunk be rejected without collapsing the whole —
  is partial acceptance a designed state rather than an accident?
  *Fails when:* rejecting one chunk invalidates digests, references, or
  premises across the others.

- **B5 [U]** Does the sequencing retire risk early — are the assumptions most
  likely to invalidate the thesis scheduled to be tested in the earliest
  chunks that can test them?
  *Fails when:* early chunks are the comfortable ones and every
  thesis-threatening unknown lives late — or nobody can name the riskiest
  assumption at all.

### C. Vision-guided, spec-driven discipline

- **C1 [U]** Does authority flow one way — vision → shape → specs →
  implementation — with each layer citing upward and no lower layer quietly
  redefining a higher one?
  *Fails when:* a lower artifact restates a higher rule with drifted meaning,
  or a summary is treated as the rule.

- **C2 [U]** Is every normative "should" owned by exactly one artifact, with
  conflicts between artifacts resolved by rule rather than by reading order?
  *Fails when:* two artifacts answer the same question and a reader must
  guess which wins; or a rule lives only inside a validator, index, or
  generated report.
  *Scope note:* C2 asks whether exactly one owner **exists** (ownership);
  D2 asks whether a reader can **find** it (routing). Evidence for one is
  not evidence for the other.
  *Population:* the artifact set named by `C2_POPULATION` in the parameter
  block — a `Met` needs the sweep over that set, with its denominator
  stated; a partial read cannot support `Met`.

- **C3 [G]** Does the project apply its own epistemics *to itself* — are
  claims about its own state evidence-backed and labeled, with absence of
  evidence rendered as unknown, never as done?
  *Fails when:* a status document claims green/zero/complete without a sweep
  run against the current bytes.

- **C4 [G]** Are the human decision points enumerated and non-delegable — can
  a reader determine *from artifacts alone* whether any given decision was
  actually made by a human?
  *Fails when:* an agent-authored artifact could pass as an owner act, or a
  pending decision is indistinguishable from a made one.

- **C5 [U]** Does the shape separate what the project controls from what it
  assumes of its substrate — external tools, formats, platforms — with each
  load-bearing assumption recorded alongside a stated posture if it breaks?
  *Fails when:* an external dependency is treated as guaranteed, or its
  failure would reshape the project and no artifact admits that.
  *Population:* the assumption registry named by `C5_POPULATION` in the
  parameter block; an assumption found outside it is itself a finding.

- **C6 [U]** Does required authority scale with irreversibility — are
  hard-to-undo or externally visible actions gated more strongly than
  routine, revertable ones?
  *Fails when:* one approval level covers everything, or an irreversible
  effect is reachable through a routine path.

- **C7 [U]** Could a competent stranger, given only what a clone contains,
  continue the project — including re-deriving why each irreversible
  decision was made?
  *Fails when:* any load-bearing rationale exists only outside the
  distributable artifact set.
  *Population:* the decision record set named by `C7_POPULATION` in the
  parameter block — "each irreversible decision" quantifies over it.
  *(Added v1.4 from the pilot administration's G1; successor recoverability
  is distinct from F4's abandon-safety — F4 asks whether the corpus lies to
  a reader, C7 asks whether a successor could act on it.)*

### D. Comprehensibility

- **D1 [U]** Fresh-engineer test: can a capable engineer with no prior
  contact state the problem, thesis, current lifecycle stage, and next
  pending decision after bounded reading (≤ 60 min)?
  *Fails when:* correctness requires archaeology — reading history, resolving
  contradictory metadata, or knowing which documents are stale.

- **D2 [U]** Task-routing test: from the front door (the `DEFAULT_ROUTE_SET`
  entry points), can they reach the *single* rule governing one concrete
  task without exhaustive reading?
  *Administer concretely:* use the tasks fixed in the parameter block —
  chosen before the administration, never by the reviewer or the
  administering session mid-run. At least one task must cross a seam
  between two chunks.
  *Fails when:* the route requires reading the corpus, or two routes give two
  answers.

- **D3 [U]** Is invented vocabulary minimal and defined-before-use — does
  each coined term buy clarity ordinary language couldn't?
  *Fails when:* the default reading path (`DEFAULT_ROUTE_SET`) uses a term
  before defining it, or a coined term shadows an ordinary word's meaning.
  *Population:* the coined-term enumeration named by `D3_POPULATION` in the
  parameter block; a coined term absent from it is itself a finding.

- **D4 [U]** Do the entry/summary documents make no claim their sources
  don't — is simplification confined to presentation, never meaning?
  *Fails when:* an overview asserts something stronger, softer, or fresher
  than its owning source.
  *Population:* the entry/summary set is `D4_POPULATION` in the parameter
  block — the whole set, not only `ENTRY_DOCUMENT`.

### E. Readiness to author specifications — the gate itself

- **E1 [U]** Is it defined what a specification *is* here — form, home,
  granularity, acceptance authority, and change process — before the first
  one is written?
  *Fails when:* the first spec author would have to invent the medium while
  writing the message.
  *Record sub-verdicts:* form, home, granularity, acceptance authority,
  change process — five answers, not one. E1 is Met only when all five are.

- **E2 [U]** Is the first specification identified, with every prerequisite
  either satisfied or explicitly waived on the record?
  *Fails when:* "what comes first" is answered differently by different
  documents, or prerequisites are discovered rather than listed.

- **E3 [U]** Would authoring the first spec force reopening any vision- or
  shape-level question? Enumerate them.
  *This is the sharpest single gate: hand the reviewer the shape corpus and
  the first spec's charter, and ask what they would have to reopen. An empty
  list — genuinely arrived at, not asserted — is the readiness signal.*
  *Fails when:* the list is non-empty; "ready" is then false regardless of
  every other verdict.
  *Credibility protocol:* the reviewer first enumerates the first spec's
  central concepts and obligations, then traces each to the shape artifact
  that would govern it. An empty reopen-list **without this trace table** is
  recorded as Unknown, not Met — a shallow reading also produces an empty
  list.

- **E4 [U]** Is the shape/spec boundary crisp enough that an author knows
  which side any given sentence falls on — without asking?
  *Administer concretely:* the candidate statements are fixed in the
  parameter block (`E4_CASES`) — the same cases on every administration, so
  E4 verdicts are comparable across the trend log; the reviewer classifies
  each from its text alone (shape side or spec side — the classification is
  two-valued), then compares against the project's own routing as recorded
  in the artifact named by `E4_ROUTING_AUTHORITY` in the parameter block.
  Disagreement with the project's routing is a fail; the project's routing
  disagreeing with itself over parallel cases is a fail. Where the routing
  authority is **silent** on a case — no rule of it covers the statement —
  the reviewer records `routing authority silent` in that case's evidence,
  and the silent case counts as neither agreement nor disagreement: E4 is
  judged over the cases the authority actually answers, with the silent
  ones enumerated in the row. Silence over a case the launch target *needs
  routed* is a finding in its own right, recorded in the results.

- **E5 [U]** Do acceptance criteria exist for a spec itself — how one will be
  judged complete, testable, and faithful to the shape above it?
  *Fails when:* spec acceptance would be a vibe check by whoever reviews it.

- **E6 [U]** Is there a defined propagation path for a shape change *after*
  specs exist — how affected specs are detected, who amends them, and how
  the interim disagreement is surfaced rather than hidden?
  *Fails when:* the first post-spec shape amendment would create silent
  contradictions between layers.

### F. Process health and convergence

- **F1 [U]** Is the improvement cycle *converging* — are successive review
  rounds finding fewer and less severe defects, with a declared stop
  condition other than exhaustion?
  *Requires the trend log (§6).*
  *Fails when:* each round's fixes mint the next round's findings, or no one
  can state what would end the cycle.

- **F2 [U]** Is the governance corpus proportionate to what it protects —
  does each artifact have an owner and a retirement path, and does repairing
  a defect not routinely create new artifacts?
  *Fails when:* the corpus grows monotonically; defect → new report → new
  validator → new defect.
  *Operational proxies:* the artifact-count trend across cycles; the ratio
  of normative artifacts to meta-artifacts (reports, validators, indexes) —
  meta should not outgrow normative; a sweep for artifacts no reading route
  reaches.

- **F3 [U]** Can the owner make each acceptance decision from a bounded
  packet in one sitting, without archaeology?
  *Fails when:* the honest answer to "what am I binding?" requires reading
  history or trusting a summary the packet itself calls non-authoritative.

- **F4 [U]** If all improvement stopped today, would the corpus be safe to
  abandon — no artifact left misstating the current state to a future reader?
  *Fails when:* any stale claim, superseded offering, or dead route is
  reachable from a default reading path without a banner.

- **F5 [U]** Is the project's assurance mechanism independent of the thing
  it assures — would an error shared by every available reviewer be
  detectable, and by what?
  *Fails when:* independence is procedural (a different session) rather than
  substantive (different failure modes — a different model family, a human,
  or a mechanical check), and no artifact says so. A gate administered only
  by the corpus's own authors' model family is this question's own example;
  the administration record must disclose it.
  *(Added v1.4 from the pilot's G1. This question also covers instrument
  capture: an administering party whose interests are the corpus authors'
  is not substantively independent, and a question amended in the same
  change that repairs the corpus's failure against it must be flagged in
  the trend log — §6's "a trend across amended questions is not a trend".)*

- **F6 [U]** Is governance effort per delivered increment bounded and
  declining — and is there a declared ceiling past which process is cut
  rather than added?
  *Fails when:* nobody can state the ratio of governance artifacts to
  delivered product increments, or the ratio grows without a declared stop.
  Pre-specification, "delivered increment" reads as: accepted artifacts and
  closed owner decisions, not authored candidates.
  *(Added v1.4 from the pilot's G1; F2 measures corpus proportionality at a
  point, F6 measures the trend of effort against progress.)*

### G. Gate self-scrutiny

- **G1 [U]** Completeness critic — the reviewer must answer: *what readiness
  dimension could this project fail that no question above would catch?*
  Proposed missing questions are recorded in the results and considered for
  upstream amendment of this instrument (§9 changelog).
  *G1 yields no Met/Not-met verdict; an administration that skips it is
  incomplete and cannot support a gate decision.*

---

## 4. Verdict computation

The gate is administered **against a named launch target** (parameter block:
`LAUNCH_TARGET`, `REQUIRED_WAVES`, `DEFERRED_WAVES`).

**The three gate verdict words, defined here** *(added at v2.1, review RD-48
finding 3 — `NOT READY` was emitted by the tool, printed as the report's last
line and carried in the trend log, while appearing in this instrument only
inside §9's history. The word the failing branch produces had no home in the
instrument that owns readiness semantics):*

| Word | Means |
|---|---|
| **`READY FOR <LAUNCH_TARGET>`** | Every conjunct below holds and the pass rests on no deferral |
| **`READY-WITH-DEFERRALS`** | Every conjunct holds except that the F2 limb is satisfied by an owner-cited deferral rather than by `Met` |
| **`NOT READY`** | Any conjunct fails. The default: this is the verdict whenever the formula does not produce one of the two pass words |

The set is closed. **A record carries no verdict field** — the verdict is
computed, never claimed, and the schema's closure refuses one — and no
administration may translate a verdict into softer language. *(Narrowed at
v2.2, RD-55 f6: this clause read "a record may not contain any of them",
which nothing enforces and nothing could sensibly enforce — a reviewer's
free text may legitimately quote a verdict word. What is enforced is that no
FIELD carries one, and the report renders every free-text field as data, so a
quoted verdict cannot present itself as the report's own.)*

**A verdict is not a gate result.** *(Added at v2.1; charter §7.1.)* Three
outcomes are distinct and must be presented separately:

| Outcome | Produced when |
|---|---|
| **Row/formula outcome** | Always. It is a function of the rows and nothing else |
| **Administration eligibility** | Separately determined, and **conjunctive over five limbs**: the record is `formal`; `administration_kind` is `full`; the reviewer declares fresh context; the record validates with **zero** errors; and the checks that bind it to the repository actually ran — with git unavailable, identity, binding, case-text, deferral and evidence existence are not verified, and an unverified record is not eligible *(the fourth limb was stated at v2.1 and implemented at only one of its four consumers; the fifth was a disclosed limit that eligibility did not consider — RD-55 f1, RD-56 f1 and f7)* |
| **Formal gate result** | Only for an eligible record. For any other, the formal gate result is **none**, and the row outcome is diagnostic |

An administration failing any limb may therefore produce a diagnostic row
outcome. **It may never produce a `READY FOR` gate result.** *(v2.1 wrote
"a delta, non-formal, stale or invalid administration"; `stale` named no
limb, defined nothing, and was computed nowhere — RD-55 f7. The limbs above
are the list.)*

**The fourth outcome has a name: `NONE`.** When an administration is
ineligible the gate result is the literal `NONE`, followed by the limbs it
failed. Every surface uses that word — the trend log's Gate-verdict column,
the generated report's terminal line, and the validator's own output —
so §6's column vocabulary is four-valued and all four values are defined
here. *(Added at v2.2, RD-55 f8: v2.1 introduced the outcome in prose as
"none" and three tool surfaces spelled it three ways.)*

This reaches every place a gate result is stated, and §6's trend log is one of
them: the Gate-verdict column carries the **gate result**, so an ineligible
administration deposits `NONE — not eligible` there and its row outcome
travels beside it as the diagnostic it is. §6's counting columns are unaffected
— a diagnostic administration's findings are findings. *(The column's rule is
stated here rather than in §6 so that the three-outcome separation has one
home; §6 is byte-unchanged at v2.1.)*

The launch-gate rule:

> **READY FOR `<LAUNCH_TARGET>`** =
>     every E question `Met` for the named launch target
>     AND no `Not met` in launch-scope A–D — a
>         `Not met (out of launch scope)` row does not block
>     AND F1 is `Met` or `Unknown` — a `Not met` F1 blocks,
>         whichever of its two limbs failed
>     AND F3 is `Met`
>     AND F4 is `Met`
>     AND (F2 is `Met` OR explicitly owner-deferred with a bounded
>          reduction plan)
>     AND E3's reopen list is empty
>
> Every term of this formula is a predicate over the closed verdict
> vocabulary — nothing in it requires a word the rows may not contain.

*The E3 conjunct is stated here from v2.1 (review RD-48 finding 2). The tool
has computed it since v2.0 and the generated report printed it under the
heading "Conjuncts of the §4 formula", while §4 listed five. It is a
strengthening and it is grounded in §3's own E3 rule — "**an empty list is
the readiness signal**", and E3's fails-when is "the list is non-empty;
'ready' is then false regardless of every other verdict". But a formula term
the instrument does not carry is a term the instrument does not own, and §5
says the instrument, not the tool, owns readiness semantics. It is now a
stated conjunct rather than an unstated one.*

**Launch scope.** A–D questions are answered over the whole repository —
global source-of-truth and current-path hygiene are never scoped away — but
a defect that lives *only* in a deferred wave's candidate semantics blocks
the verdict **only if** it:

- is on the default reading or task route;
- changes a required wave's meaning;
- is a dependency of the launch target;
- makes the repository misstate current truth;
- prevents the owner from understanding the launch decision.

A deferred wave's internal defect meeting none of these is recorded in the
results (it stays a finding) without converting the launch-scope verdict:
its question's row takes the verdict `Not met (out of launch scope)`, and
the defect is listed on the record's deferred-wave findings line. Rendering
such a defect as a bare `Met` is a false row; rendering it as a bare
`Not met` blocks a verdict §4 says it must not block — the scoped form is
the only honest rendering, and the validator counts it separately. The
disclosure is the scoped form's honesty, so it is checked, not trusted: a
record with any scoped row whose deferred-wave findings line names no
defect asserts a scoped defect exists and that none exists — a validation
error (`LA-9`), never a lawful record. *(Identifier corrected at v2.1,
RD-48 f1 — `LG-9` belongs to the historical Markdown validator.)* The gate never requires internally
unrelated deferred semantics to be accepted.

Qualifications:

- `Unknown` in launch-scope A–D does not block by itself, but every Unknown
  must carry what evidence would settle it, and unsettled Unknowns
  accumulate as owner risk, stated in the results.
- F1/F3/F4 are explicit conjuncts because a project must not launch while
  its owner packet requires archaeology (F3), its default path contains
  stale claims (F4), or the process loop has visibly failed to converge
  (F1). The F1 conjunct is a verdict predicate: `Met` or `Unknown` passes
  (no trend yet is not a veto), `Not met` blocks — whether it failed by
  divergence or by the missing stop condition, both of which live in F1's
  own fails-when.
- Only the owner may defer F2, and only against a bounded reduction plan
  (maximum new meta-artifacts, artifacts to retire, stop condition). An
  `Unknown` F2 is deferrable on exactly the same owner-deferral terms as a
  `Not met` F2 — trend-shaped proxies can be legitimately unknowable at
  Administration 1, and the deferral discloses that rather than blocking on
  it. A deferral is claimed only by **citation**: the record's
  `owner_deferrals[].decision_citation` names the owner decision — an
  `SDR-n` identifier, or a file in `.syzygy/governance/decisions/` that is
  not the pending queue — that granted it, together with a
  `bounded_reduction_plan`. A reviewer's own evidence-cell wording ("treated
  as owner-deferred") is not a deferral and satisfies nothing; neither is a
  queue entry, a Beads issue, or a candidate decision packet, each of which
  records that the owner has **not** ruled. *(Field name corrected at v2.1,
  RD-48 finding 1: this clause named `Owner deferral decision:`, a field of
  the Markdown record format v2.0 deleted.)*
- **Any deferral-carrying pass is `READY-WITH-DEFERRALS`.** The F2 deferral
  limb of the formula — and any other owner deferral a pass rests on —
  changes the verdict word: plain `READY FOR <LAUNCH_TARGET>` over any
  deferral, or over a nonzero `len(owner_deferrals)`, is a contradiction and
  a validation error. *(Field name corrected at v2.1, RD-48 f1.)*
- **The `READY-WITH-DEFERRALS` predicate, stated as a formula** (RD34-01 —
  a verdict word with no predicate of its own is a branch a pass can ride
  through unchecked, and every term of this section's formulas is a
  predicate over the closed vocabulary):

  > **READY-WITH-DEFERRALS** =
  >     every conjunct of **READY FOR `<LAUNCH_TARGET>`** above —
  >     every E question `Met`; no plain `Not met` in launch-scope A–D;
  >     F1 `Met` or `Unknown`; F3 `Met`; F4 `Met` —
  >     with exactly one substitution: the F2 limb is satisfied by an
  >     **owner-cited deferral** (`owner_deferrals[].decision_citation`)
  >     instead of `Met`,
  >     AND `len(owner_deferrals)` is nonzero AND the citation resolves.

  The E, A–D, F1, F3 and F4 conjuncts are **never deferrable** — each
  carries this section's own rationale for blocking — so the two pass
  verdicts differ in exactly one limb, and the validator runs the full
  conjunct battery on both branches (`LA-12`): plain `READY FOR`
  requires F2 `Met` and zero declared deferrals; `READY-WITH-DEFERRALS`
  requires the nonzero count **and a citation that resolves**, and fails on
  any non-F2 conjunct exactly as a plain pass would. *(Corrected at v2.2,
  RD-55 f4. v2.1 annotated this sentence but left the literal `LG-6/LG-7`
  standing — checks in `launch_gate_results.py`, which validates historical
  Markdown records only and never runs on a structured record — while three
  documents said the citation had been replaced. The structured path's check
  is `LA-12`. The resolving-citation limb was likewise stated here and
  selected from the deferral count alone until v2.2, RD-56 f8.)*
- F5 and F6 are recorded and disclosed (`reviewer.model_family`; the trend
  row) *(field name corrected at v2.1, RD-48 f1 — §5 has no "family line")*
  but are deliberately not conjuncts at Administration 1: both were added
  from the pilot's G1 and have no baseline yet, and F5's substantive limb
  is partially satisfied by mechanical checks even under a same-family
  administration. Promoting F5 to a conjunct is an owner option flagged in
  the P-34 packet; until taken, a `Not met` F5 or F6 travels as stated
  owner risk, never silently.
- The gate can be *passed with enumerated deferrals* only by explicit owner
  decision, never by the reviewer or the administering session.
- G1 yields no verdict and never blocks, but an administration missing G1
  is incomplete and cannot support a gate decision.

---

## 5. The administration record — structured source, generated report

**One administration produces two files, and only one of them is a fact.**

```text
<record>.json    the source record — canonical, validated, the only authority
<record>.md      the generated report — presentation, never read back
```

The source record conforms to `launch-gate-administration.schema.json`,
committed beside this instrument and digest-bound in the administration
packet. The schema is the machine annex of this section: where this section
and the schema describe the same requirement, the schema is the one a tool
enforces, and a disagreement between them is a defect in this instrument to
be repaired by amendment, never resolved by a reader's judgment at
administration time.

**Why the format changed at v2.0.** Between v1.3 and v1.18 this section
defined a Markdown record that was simultaneously a human report and the
machine-validated source of a launch decision. Thirteen consecutive
administrations of the instrument returned `REVISE`, and their findings
converged on a single question no Markdown rule answered stably: *is this
line the record's own claim, or a quotation of one?* Quotations, fences,
comments, list items, continuations, raw HTML, hidden DOM regions, CSS
visibility, tag populations, and disagreements between renderers each
produced a path on which a false `READY FOR` could be carried past a
validator. v2.0 does not answer the question again. It removes it: the
verdict is computed from typed fields, and the Markdown carries no fact
that anything reads.

**What the record represents** (the schema is normative on shape; this is
the reading of it):

```text
schema_version, date, administration_kind (full | delta), formal
instrument: path, version, sha256
parameter_block_sha256
repository_commit
launch_target, required_waves, deferred_waves
reviewer: identity, model, model_family, fresh_context,
          same_family_as_corpus_authors
materials: included, withheld, deviations
operationalization_notes
question_results[]: question_id, question_digest, verdict, launch_scope,
                    evidence[], counterexample, unknown_reason,
                    unknown_settlement, falsification_attempt
e3: concepts, trace_rows, reopen_items
e4: routing_authority, fixed_case_results[]
owner_deferrals[], deferred_wave_findings[], reopened_findings[]
pilot_recurrence_check
g1: critic_answer, proposed_missing_questions[]
falsification_summary
prior_record
```

Every evidence entry names a **repository path, the commit, a line/range or
stable identifier, and a short quote or measurement**. Evidence is
commit-anchored: an entry whose commit is not the record's own is void, and
the validator rejects it rather than reading it charitably.

**The record carries no verdict.** There is no `final_verdict` field to
author, and the schema rejects one: the verdict is computed by
`scripts/validate_launch_administration.py` from the rows, by §4's formula.
The previous format let a record state its own conclusion and asked a tool
to agree; a record that cannot state one cannot be believed about one.

**Three properties this shape buys, each of which the Markdown format could
not hold:**

1. **Absence is an error, never an implicit answer.** A missing required
   field fails validation. There is no deleted-template-line that reads as
   answered, and no field that borrows the next line's text.
2. **Scope cannot be laundered by wording.** `verdict` and `launch_scope`
   are separate typed fields that must agree, so rendering a defect out of
   launch scope takes two deliberate acts, not one soft phrase.
3. **Counts are computed, not declared.** `Deferred` and `Reopened` are the
   lengths of required arrays: an absent array is an error, an empty array
   is an explicit assertion of zero, and neither can be a silent zero
   (VIS-2 applied to the gate's own record).

**The generated report** is produced by
`scripts/render_launch_administration.py` and opens with, literally:

```text
Generated presentation.
Canonical source: <record>.json
Do not edit this file.
```

It is never parsed, never cited as the source of an administration fact, and
`--check` regenerates it to detect an edited one. A record that does not
validate is not rendered at all.

**What the validator checks** (`LA-1` … `LA-16`, and `LA-3b`, each with at
least one mutation fixture). *(Amended at v2.1, review RD-48 finding 5. This clause
read "the tool's own docstring is the enumeration, and it is the tool's, not
this instrument's, to keep current" — an instrument making a document
normative and simultaneously disclaiming responsibility for its currency,
and that docstring was already false about `LA-13`. **The enumeration below
is this instrument's**; the tool implements it, and a check the tool runs
that this list does not name is a finding against the tool.)* The checks
cover: schema conformance;
instrument, parameter-block and commit identity; the launch-target and wave
binding; roster completeness and closure; verdict/scope agreement; evidence
discipline per verdict; E1's five sub-rows and its rollup; scoped-row
disclosure against the deferred-wave findings; E3's credibility protocol and
its reopen-list gate; E4's fixed-case completeness and case-text fidelity;
the E4 routing authority's binding to §8 (`LA-3b` — named here at v2.2,
RD-55 f2 and RD-56 f8: v2.1 took back this enumeration in the same pass that
added a check the enumeration did not name, which by this clause's own
construction is a finding); the schema's own identity, since a record
validated against anything but the committed schema is not validated
(RD-56 f3); deferral citation — **a made owner decision**, never a queue
entry, a log, an index, a decision packet, or a document that declares its
own status unresolved (RD-56 f5); §4's formula on both pass branches; full-vs-delta and fresh-context integrity; G1's
presence and answer; prior-record anchoring; and the pilot-recurrence check.

The instrument, not the tool, owns readiness semantics. A record the tool
passes can still support nothing if this file's non-mechanical requirements
— fresh context, family disclosure, a genuine falsification attempt, a full
administration — were not honored. Those live in the record's fields and the
reader's judgment, and no validator promotes them to facts.

**Historical records.** Administrations performed under v1.3–v1.18 are
Markdown records in the format those versions defined. They remain immutable
historical evidence, they are never migrated, and
`scripts/launch_gate_results.py` remains in the repository to validate
**those** records only. It is not the correctness path for any v2.0
administration, and no v2.0 record is a Markdown file.

Store the source record and its generated report in the canonical result
home. Never edit a past administration; supersede it.

## 6. Trend log

Append one line per administration to
`.syzygy/governance/decisions/launch-gate/TREND-LOG.md`; this is F1's
evidence. **The row is generated**, not transcribed:
`validate_launch_administration.py --trend-row` prints it from the source
record, and the New-findings column is computed against the record the
`prior_record` field names. A hand-typed trend row is a figure quoted
outside its owning artifact, which is how the columns went stale before.

```markdown
| Date | Commit | Not-met | Scoped | Unknown | Deferred | Reopened | New findings vs prior | Gate verdict |
|------|--------|---------|--------|---------|----------|----------|----------------------|--------------|
```

Convergence means the Not-met and new-findings columns trend to zero across
administrations *without the questions being weakened*. If a question is ever
amended, note it here — a trend across different questions is not a trend.

**A scoped finding is a finding.** The Scoped column counts
`Not met (out of launch scope)` rows; rendering a defect scoped must never
improve the read of any other column, and a finding class invisible to
every column would be invisible to F1 — which is answered from this log
and only from it. The Scoped column trends to zero the same way Not-met
does: deferred waves are eventually accepted or their defects repaired,
never laundered. A **new** scoped finding is a **new finding**: the
New-findings column counts rows newly `Not met` (not `Not met` in the
prior administration — a scoped row turning plain counts, it newly
blocks) plus rows newly scoped that were not previously a finding under
either rendering — so rendering a defect scoped never zeroes the delta
column, and reclassifying an old finding never double-counts it.

A deferral is a finding until resolved: moving a finding from Not-met to
Deferred must never improve the read of any other column. Reopened counts
findings previously recorded resolved that recurred — a nonzero Reopened
column indicts the resolution process, not just the finding.

**Trend comparability across the v2.0 boundary is limited, and the limit is
stated rather than smoothed.** The pilot (v1.3) and every subsequent
Markdown administration were recorded in a format whose counts were parsed
from prose; v2.0's are computed from typed fields. The questions and the
formula are unchanged, so the *verdicts* are comparable question by
question; the *counts* are comparable only insofar as the earlier records'
parsed figures were correct, which is precisely what thirteen `REVISE`
verdicts put in doubt. A trend line drawn across the boundary must say so,
by the same rule that governs amended questions: a trend across different
measurement methods is not a trend.

The formal trend log begins with the first administration meeting §2's
integrity requirements ("Administration 1"). Whether any earlier,
non-conforming administration exists — and why it does not open the log —
is project-specific and recorded in the trend log's own header, never
here (§7's rule: everything project-specific lives in the parameter block
or the project's own records; the pilot-recurrence instruction is §8's
`PILOT_RECURRENCE_CHECK`).

---

## 7. Generalization path (future work, not this file's job)

This instrument is deliberately structured to be generalized, then
concretized as skills under `/th-projects`:

1. **`launch-gate-author`** — given a project's goal statement, generate the
   [G] questions and bind the [U] questions to the project's parameter block
   (§8 shape). The [U] tier is the portable core; it should ship verbatim.
2. **`launch-gate-administer`** — run one administration: spawn a
   fresh-context reviewer with the §2 materials, enforce the verdict
   vocabulary, produce the §5 record, append to the §6 trend log.
3. **`launch-gate-trend`** — read the trend log and answer F1 honestly,
   including the "questions were weakened" check.

Generalization rule: the [U] questions, the §2/§4 protocol, **and the
record schema's field shapes** are the invariant; everything project-specific
lives in the parameter block.

*(Corrected at v2.1, review RD-48 finding 4. This rule said the schema
"names no Syzygy artifact". **It does**: its `$id` is a `github.com/Tzeusy/
syzygy` URL, it names `launch-gate-pre-specifications.md` and
`scripts/validate_launch_administration.py`, it cites VIS-2 and VIS-4, and
it carries this project's `SDR-n`/`P-n` decision-identifier conventions.
`validate_launch_administration.py` additionally hardcodes the decisions
home that `LA-11` depends on. What actually generalizes is the schema's
**field shapes**; its identifiers, doctrine citations and decision
conventions are project bindings that a generalized version must rebind.)*

**The portable core includes the two tools.** Without a validator and a
renderer a v2.0-or-later record cannot be validated, verdicted, or read: the
verdict is computed and the record may not claim one, so an instrument
shipped without them ships a record format nobody can turn into an answer.
A generalized version must carry the tools or state a tool-independent
procedure for computing §4's formula. If a generalized version needs to edit a
[U] question to fit a project, that is a finding about the question —
record it upstream, don't fork silently.

---

## 8. Parameter block — Syzygy binding

| Parameter | Value |
|---|---|
| `PROJECT` | Syzygy (provisional codename) |
| `GOAL_STATEMENT` | `.syzygy/governance/doctrine/` (adopted 2026-07-30; vision.md is the core) |
| `ENTRY_DOCUMENT` | `.syzygy/intent/OVERVIEW.md` (governed presentation, never authority) |
| `CURRENT_STATE` | `PROJECT-STATUS.md` |
| `SHAPE_CORPUS` | `.syzygy/governance/contracts/candidates/` — **withheld from question derivation; readable for answering** |
| `SPEC_MEDIUM` | OpenSpec (`openspec/` — does not exist yet; its absence is correct pre-gate) |
| `FIRST_SPEC_CANDIDATE` | `.syzygy/governance/contracts/candidates/FIRST-OPENSPEC-SEQUENCE.md` (revision 3, which declares itself "the single current first-spec document"). If that file is absent at the administered commit, E2 is `Not met` (nothing identified), never `Unknown` |
| `HUMAN_DECIDER` | the owner; owner acts per the acceptance record; VIS-4 governs delegation |
| `EPISTEMIC_LABELS` | Observed / Inferred / Unknown (doctrine trust-and-evidence) |
| `CHUNK_UNIT` | the six wave acts — A, B, C1, C2, D1, D2. B-section "chunk" = wave; the wave manifests are the chunk boundaries |
| `E4_ROUTING_AUTHORITY` | `.syzygy/governance/contracts/candidates/SURFACE-CLAUSE-ROUTING-MATRIX.md` — the clause-to-route matrix (candidate, readable for answering); its OS routes are the spec side, all others the shape side |
| `DEFAULT_ROUTE_SET` | `README.md`, `AGENTS.md`, `.syzygy/intent/OVERVIEW.md`, `PROJECT-STATUS.md`, `.syzygy/governance/doctrine/README.md`, `.syzygy/governance/contracts/candidates/TASK-ROUTER.md` — the default reading and task routes for D2/D3/F4 and §4's blocking condition 1 |
| `C2_POPULATION` | `README.md`, `AGENTS.md`, and every `.md`/`.yaml` file under `.syzygy/governance/` — the normative and candidate-normative artifact set |
| `C5_POPULATION` | `.syzygy/governance/policies/GOVERNANCE-SUBSTRATE-LOCK.yaml` — the external-baseline registry; assumptions found outside it are findings |
| `C7_POPULATION` | `.syzygy/governance/decisions/` — the owner decision records (SDR-*, warrants, pending queue) |
| `D3_POPULATION` | the term registry `.syzygy/governance/contracts/candidates/policy-candidates/TERM-REGISTRY.md` plus the doctrine glossary in `.syzygy/governance/doctrine/README.md` |
| `D4_POPULATION` | `README.md`, `.syzygy/intent/OVERVIEW.md`, `PROJECT-STATUS.md`, `AGENTS.md` |
| `PILOT_RECURRENCE_CHECK` | the pilot (2026-08-09, v1.3) documented under E6/F1/F3 a retired ceremony phrase still standing as the live acceptance gate in two digest-carrying owner documents. At Administration 1: sweep the current bytes for any retired acceptance phrase presented as current (the project's own CG-2a check names the population); if present, it belongs in the Reopened column, not the Not-met column alone |
| `D2_ROUTINE_TASK` (fixed) | "add an evidence adapter for a new CI system" |
| `D2_AUTHORITY_TASK` (fixed) | "change what counts as a completed Mission" |
| `D2_SEAM_TASK` (fixed) | "trace a merged change from its work record to its reconciled status" — crosses the work-surface/evidence seam |
| `NEAR_MISSES` (for A3) | (1) an issue tracker with a code browser and dashboards; (2) a documentation portal that renders governance artifacts beautifully; (3) a CI-status aggregator with an AI chat over it |

Launch-scope parameters for the next formal administration:

```yaml
LAUNCH_TARGET: >
    Capability 1 — Project registration and honest shape visibility.
    Defined in .syzygy/governance/contracts/candidates/DEFERRED-WAVE-POSTURE.md,
    whose owner-directed statement reads: "The launch target is Capability 1
    — Project registration and honest shape visibility, whose contract
    prerequisite is Waves A + B only." That artifact also states, per
    deferred wave, why the target does not use it.

REQUIRED_WAVES: [A, B]

DEFERRED_WAVES: [C1, C2, D1, D2]

DEFERRED_WAVE_POSTURE: >
    candidate; not accepted; not used by the launch target; excluded from
    default task routing except where a route explicitly inspects those
    candidates; unresolved defects disclosed in
    .syzygy/governance/contracts/candidates/DEFERRED-WAVE-POSTURE.md
```

`MAJOR_SHAPE_COMMITMENTS` — A5's closed population (never an all-clause
table). A5 is answered repository-wide and **wave-blind**: whether a
commitment's governing semantics sit in a required or a deferred wave does
not change its row in the two-way table, and A5's fail condition is
unchanged by launch scope:

```text
typed authority
Polaris
Trajectory
Orrery
machine-queryable endpoints
evidence/Unknown truthfulness
write boundary
context packets
Mission Control
3D + non-3D comprehension
propagation proof
```

`E4_CASES` — the fixed candidate statements, classified from their text
alone on every administration, then compared against the project's own
routing rule. Written in ordinary language deliberately, so they derive
from no corpus-internal structure:

1. "Every registered project has exactly one graph identity, and a rename
   does not mint a new one." *(structural graph identity rule)*
2. "When a repository is registered, a human can see in the product that
   registration succeeded, what was registered, and what was not."
   *(human-visible registration behavior)*
3. "A region with no evidence renders visibly as Unknown — never green,
   never zero." *(visual Unknown behavior)*
4. "Every specification change receives an independent fresh-context review
   before adoption." *(spec-quality/review obligation)*
5. "A machine client can query any project answer a human can see, and
   receives the same facts with the same epistemic labels." *(machine
   endpoint behavior)*
6. "When a shape artifact changes, every affected specification is
   enumerated and amended in the same logical change, or the disagreement
   is rendered rather than hidden." *(shape-change propagation rule)*

Notes for administering against Syzygy specifically:

- The reviewer may *answer* questions using the candidate corpus; the
  questions themselves were derived only from adopted doctrine, the overview,
  and universal principles (this file, first authored 2026-08-09, session
  with candidate RFCs deliberately unread).
- Verdict words here are compatible with, but not identical to, the repo's
  review vocabulary (`REVISE`/`EXCEPTIONS`/`REJECT`); never translate between
  the two vocabularies — record both where both apply.
- This file is a process instrument under the repo's own rules: it is never
  citable as authority, and no gate verdict performs an owner act.

---

## 9. Changelog

- **v2.2** (2026-08-13, repair pass — the two v2.1 reviews) — v2.1's two
  commissioned reviews (RD-55 policy semantics, RD-56 machinery) both
  returned `REVISE`, and **both found the same blocking defect
  independently**: §4's eligibility clause stated four limbs and the tool
  implemented three, so a record whose only defect was a forged instrument
  digest still deposited `READY FOR …` into the trend log §6 calls F1's only
  evidence, and into the generated report's last line. Eligibility now owns
  all five limbs (the fifth — that the binding checks actually ran — was a
  disclosed limit nothing acted on), is computed last so it can count the
  errors, and every consumer reads the one answer. §4 also gains the name
  `NONE` for the fourth outcome, drops `stale` (an ineligibility ground that
  defined nothing), narrows the closed-set clause to what is enforced, and
  finally replaces the `LG-6/LG-7` citation v2.1 annotated but did not
  change. §5's enumeration names `LA-3b`, the schema's own identity, and
  what a deferral warrant is not. **The tool repairs, each with a fixture
  verified to fail without it:** free text is neutralized at every one of
  its sites rather than the two a reviewer named (the forgery reproduced
  verbatim through `operationalization_notes`); `--schema` is bound, and a
  schema that constrains nothing is refused; the prior-record path is
  resolved inside the repository before its contents zero a trend column; a
  deferral warrant is judged by shape, not by a three-name list that
  accepted 16 of the decisions home's 20 files; `--allow-invalid` renders a
  refusal instead of a traceback; the git-unavailable note reaches the
  stored artifact instead of only stdout; invisible characters no longer
  defeat the placeholder lexicon; and the fixture that claimed to cover the
  wave-binding repair — and passed against the unrepaired validator, because
  it mutated the record rather than the instrument — is replaced by one that
  mutates the instrument in a scratch repository.

- **v2.1** (2026-08-13, repair pass — the two v2.0 reviews) — the amendment
  RD-47 and RD-48 earned, both of which returned `REVISE` on v2.0.
  **§4 gains three things it should always have carried:** the closed set of
  **gate verdict words**, including `NOT READY`, which the tool emitted and
  the instrument defined only inside this changelog (RD-48 f3); the **E3
  reopen-list conjunct**, which the tool has computed since v2.0 and the
  report printed as a "§4 conjunct" while §4 stated five (RD-48 f2); and the
  separation of **row/formula outcome, administration eligibility and formal
  gate result** into three distinct outcomes, so that a delta or non-formal
  administration produces a diagnostic outcome and never a `READY FOR` gate
  result (charter §7.1; RD-47 f11, RD-48 f5). §4's clauses now name the
  **schema fields** (`owner_deferrals[].decision_citation`,
  `len(owner_deferrals)`, `reviewer.model_family`) and the `LA-*` checks,
  in place of Markdown-record fields v2.0 deleted and `LG-*` checks that
  never run on a v2.0 record (RD-48 f1). **§5 takes back the check
  enumeration** it had delegated to a script docstring while disclaiming
  that docstring's currency — and which was already false about `LA-13`
  (RD-48 f5). **§7's claim that the schema "names no Syzygy artifact" is
  withdrawn**: it is false, and the portable core now includes the two
  tools, without which no record can be turned into an answer (RD-48 f4).
  The changelog's own stale fixture count is deleted rather than corrected —
  the count is printed by `--selftest` and stated nowhere else (RD-48 f6).
  **§1, §2, §3, §6 and §8 are byte-identical to v2.0** — measured by
  splitting both texts on their `## <n>.` headings and digesting each span,
  not asserted: no question's text moved, no protocol obligation changed, no
  parameter changed, and the roster and trend-log rules are untouched. §4,
  §5, §7 and §9 are the four that moved, and each is accounted for above.
  The three-outcome separation is stated in §4 as reaching **every** place a
  gate result appears, which caught one the CLI repair had missed: §6's
  Gate-verdict column was still generated from the row outcome, so an
  ineligible administration with all-`Met` rows would have deposited
  `READY FOR …` into the log F1 is answered from and only from (RD-48
  f10(b)). Four further RD-48 findings concern the **v2.0 delta document**
  rather than this instrument; they are dispositioned in the v2.1 delta,
  including the two normative sentences v2.0 deleted from §2 without record
  (f8) and the preamble's "stored verbatim" (f11) — both are recorded there,
  and **neither is restored**, because §2's successor obligations are
  equivalent-or-stronger and re-opening §2 would cost its byte-identity for
  no gain in force.

- **v1.0** (2026-08-09) — initial instrument: A1–A4, B1–B4, C1–C4, D1–D4,
  E1–E5, F1–F4; protocol, verdict rule, records, trend log, generalization
  path, Syzygy binding.
- **v1.1** (2026-08-09, improvement pass 1 — coverage) — added A5
  (consumers), A6 (resource realism), B5 (risk-ordered sequencing), C5
  (substrate assumptions), C6 (reversibility-graded authority), E6
  (post-spec shape propagation), G1 (completeness critic).
- **v1.2** (2026-08-09, improvement pass 2 — anti-gaming) — fixed materials
  list; commit-anchored evidence; pre-written `NEAR_MISSES` for A3;
  parameter-fixed routing tasks including a seam-crossing task for D2; E3
  credibility protocol (trace table or the verdict is Unknown);
  deferred/reopened columns in the trend log with the no-laundering rule;
  verbatim-question, operationalization-notes, and model-family rules in
  the results record.
- **v1.3** (2026-08-09, improvement pass 3 — administrability) — question-ID
  stability rule and this changelog; administration order, effort sizing,
  and the full-vs-delta rule; E1 sub-verdicts; F2 operational proxies;
  C2/D2 scope note; G1 completeness requirement in the verdict rules.
- **v1.4** (2026-08-10, post-pilot amendment — typed authority and launch
  scope; candidate, owner approval pending) — status/authority header and
  the three-artifact-class lifecycle model; §2 administration integrity
  requirements (committed instrument, instrument + parameter-block digests,
  family disclosure, no self-review of repaired bytes); launch-scope
  parameters (`LAUNCH_TARGET`, `REQUIRED_WAVES`, `DEFERRED_WAVES`,
  `DEFERRED_WAVE_POSTURE`) and the five-condition deferred-wave blocking
  rule in §4; strengthened verdict formula (F3/F4 conjuncts; F2 met or
  owner-deferred with a bounded plan); A5 population fixed to the closed
  `MAJOR_SHAPE_COMMITMENTS` list with the two-way-table evidence rule; E4
  cases fixed in the parameter block (`E4_CASES`, six statements); D2 tasks
  promoted from suggested to fixed; results record gains digests, launch
  target, and the deferred-wave findings line; §6 pilot note (the
  2026-08-09 v1.3 administration is steering evidence, not the formal
  trend baseline, four reasons recorded); new questions **C7** (successor
  recoverability), **F5** (assurance independence, folding the pilot's
  instrument-capture proposal into its second limb), **F6** (governance
  effort per delivered increment) — all three from the pilot's G1; the
  pilot's fourth proposal (a standalone G2) is declined as overlapping F5,
  recorded in `round-2026-08e/LAUNCH-GATE-v1.4-SEMANTIC-DELTA.md`;
  `scripts/launch_gate_results.py` named as the record validator. No
  existing question weakened; no ID renumbered.
- **v1.5** (2026-08-10, post-RD-24 amendment — the fresh instrument
  review's 21 findings; candidate, owner approval pending) — verdict
  formula restated as predicates over the closed vocabulary: the F1
  conjunct is now `Met`-or-`Unknown` (RD24-09), and the launch-scope rule
  gained the `Not met (out of launch scope)` row form that the formula and
  validator both read (RD24-05); §5 template gains a required non-authority
  banner (RD24-02), the literal `GATE VERDICT:` token, a G1 section slot
  (RD24-10), explicit `Deferred count:` / `Reopened count:` fields whose
  absence errors rather than reading zero (RD24-19), and the five E1
  sub-verdict rows (RD24-21); §2 gains the withhold-versus-read-access
  reconciliation (RD24-15); B-section "chunk" bound to `CHUNK_UNIT`
  (RD24-18); C2/C5/C7/D3/D4 populations bound to parameter-block
  denominators (RD24-20); `LAUNCH_TARGET` cites Capability 1's defining
  artifact (RD24-06); `DEFAULT_ROUTE_SET` enumerated (RD24-07);
  `FIRST_SPEC_CANDIDATE` fixed to one path with the absent-case rule
  (RD24-13); `E4_ROUTING_AUTHORITY` named (RD24-16); the pilot recurrence
  instruction moved to §8 as `PILOT_RECURRENCE_CHECK` with the defect
  described in place (RD24-14); §6 names the trend-log path (RD24-17);
  `governs:` gains the launch-scope parameters (RD24-03); Unknown-F2
  deferral terms and the deliberate F5/F6 non-conjunct status stated
  (RD24-11, RD24-12). Semantic delta:
  `round-2026-08e/LAUNCH-GATE-v1.5-SEMANTIC-DELTA.md`. No existing
  question weakened; no ID renumbered.
- **v1.6** (2026-08-10, post-RD-33 amendment — the v1.5 re-review's five
  MAJOR and seven MINOR findings; candidate, owner approval pending) —
  the absence-reads-as-success class closed one level up from v1.5's
  repairs: §4's scoped-row disclosure is now checked, not trusted (a
  scoped row beside an empty deferred-wave findings line is a validation
  error, LG-9 — RD33-01); the §6 trend table gains the **Scoped** column
  so scoped findings are visible to F1's convergence read, with the
  a-scoped-finding-is-a-finding rule (RD33-02); deferrals are claimed
  only by citation — the §5 template gains the required
  `Owner deferral decision:` field, the `(owner only)` parenthetical is
  declared a description never a satisfier (RD33-03), and **any
  deferral-carrying pass is `READY-WITH-DEFERRALS`** — plain `READY FOR`
  over any deferral is a stated contradiction (RD33-04); the validator
  binds the full question roster so a missing row errors instead of
  passing silently (LG-10 — RD33-05, which also closes RD33-10's
  E1-rollup omission), and cross-checks the record's declared instrument
  version and launch target against the committed instrument and §8
  (LG-11 — RD33-06); §5 states honestly which trend figures are computed
  and which are declared required fields (RD33-09); §6's project-specific
  pilot paragraph moves to the trend log's own header, restoring §7's
  project-invariance rule in bytes (RD33-07b, RD24-14's secondary limb);
  E4 gains the routing-authority-silence rule — a silent case counts as
  neither agreement nor disagreement and is enumerated (RD33-12).
  Validator: LG-7 rewritten, LG-9/LG-10/LG-11 added, the
  prior-vs-current `startswith`/`==` asymmetry fixed, the reduced GOOD
  fixture replaced by a full §5-template-shaped record, and fixtures
  added for LG-7 and LG-2's digest-mismatch limb so the
  every-check-has-a-fixture claim is true (RD33-03/08). Semantic delta:
  `round-2026-08e/LAUNCH-GATE-v1.6-SEMANTIC-DELTA.md`. No existing
  question weakened; no ID renumbered.
- **v1.7** (2026-08-10, post-RD-34 amendment — the v1.6 re-review's one
  BLOCKING, four MAJOR and six MINOR findings; candidate, owner approval
  pending) — the unchecked-branch class closed: §4 states the
  **`READY-WITH-DEFERRALS` predicate as a formula** — identical to
  `READY FOR` in every conjunct, with exactly the F2 limb satisfied by an
  owner-cited deferral, the non-F2 conjuncts never deferrable — and the
  validator runs the full conjunct battery on both pass branches, so an
  all-Not-met record can no longer validate under any verdict word
  (RD34-01); the deferral citation gains a shape-and-existence test — a
  repository path verified at the named commit, or a decision identifier;
  label wording rejected (RD34-02); the validator parses the **last**
  `GATE VERDICT:` line, matching §5's "terminal" (RD34-03); §6 states
  that a new scoped finding is a new finding, and New-findings is
  computed over newly-Not-met ∪ newly-scoped (RD34-04); the two
  stale-version references on routed paths are corrected and made
  version-neutral so a bump cannot strand them again (RD34-05); LG-9's
  placeholder set widened past the literal "none" (RD34-06); a nonzero
  `Deferred count:` requires the citation under any verdict (RD34-07);
  the launch-target check upgraded from containment to normalized
  equality with `LAUNCH_TARGET` or its first sentence (RD34-08); the
  roster binds membership as well as presence — invented question IDs
  are rejected (RD34-11); P-34 points the owner to D-10's corrections of
  the frozen v1.5 delta (RD34-10); the v1.7 delta restates D-7's claim
  in its honest form (RD34-09). Each change carries a fixture. Semantic
  delta: `round-2026-08e/LAUNCH-GATE-v1.7-SEMANTIC-DELTA.md`. No
  existing question weakened; no ID renumbered.
- **v1.8** (2026-08-10, post-RD-35 amendment — the v1.7 re-review's one
  BLOCKING, three MAJOR and three MINOR findings; candidate, owner
  approval pending) — a **validator-and-records batch: no question
  block, no verdict word, and no section §1–§8 changed** (RD-35: "none
  of my seven findings requires an instrument amendment"); this
  changelog entry and the version header are the only instrument bytes
  that move. The citation-existence check is un-inverted — a prefix
  strip replaces the character-class `lstrip` that rejected every real
  `.syzygy/` decision path, and the passing direction is fixtured for
  the first time: an existing repository path is ACCEPTED at the named
  commit (RD35-01); the terminal `GATE VERDICT:` anchor becomes the
  last line containing the literal token, which must itself parse to
  the closed set — a qualified or quoted terminal verdict errors
  instead of being skipped for an earlier match, and `|` in a captured
  verdict is rejected before it can corrupt §6's nine-column trend row
  (RD35-02); the verdict line's `READY FOR <target>` tail gets the same
  normalized-equality test the header `Launch target:` line already
  had — one placeholder, one enforcement standard (RD35-03); the E3
  reopen-list cross-check lands beside LG-8/LG-9: a non-empty list
  beside `E3 | Met` or any READY verdict errors, enforcing §3's own
  "'ready' is then false regardless of every other verdict" (RD35-04);
  "names nothing" becomes a shared lexicon rule rather than an
  enumeration, so decorated placeholders fail without a fourth
  extension (RD35-05); the deferral-identifier families narrow to made
  decisions — SDR-n/B-n [corrected 2026-08-10, RD36-01: `B-n` named no
  decision family in this repository — see the v1.9 entry below]; P-n
  (the pending queue) and D-n (delta items)
  grant nothing (RD35-06); §5's declared record fields gain presence
  checks, including the RD24-02 non-authority banner, and an Unknown
  row requires named settling evidence (RD35-07). Each change carries a
  fixture. Semantic delta:
  `round-2026-08e/LAUNCH-GATE-v1.8-SEMANTIC-DELTA.md` (which also
  carries the correction of the v1.7 delta's D-2 overclaim, in the
  D-10 convention — the frozen record is not edited). No existing
  question weakened; no ID renumbered.
- **v1.9** (2026-08-10, post-RD-36 amendment — the v1.8 re-review's two
  MAJOR and five MINOR findings; candidate, owner approval pending) —
  a **validator-and-records batch** again: no question block, no
  verdict word, and no section §1–§8 changed; the instrument bytes that
  move are this entry, the version header, and one dated correction
  marker in the v1.8 entry above, whose family claim was false — `B-n`
  is round-2026-08c's review-finding numbering, names no decision
  anywhere in the decisions home, and granted nothing (RD36-01). The
  identifier family narrows to **SDR-n alone**, existence-checked
  against the decisions home at the record's named commit; `B-n` is
  rejected with a reason naming what it is, and a path resolving to a
  directory is rejected — a tree is not a decision record (RD36-06).
  Every §5 field value is line-anchored, so a field written with an
  empty value is absent rather than silently borrowing the next line's
  text as its answer (RD36-02); field occurrences disagreeing in value
  are an error, so a narrative line cannot shadow a declared count into
  the trend row (RD36-03); "names nothing" gains the negation-prefix
  rule — a value led by a negation word asserts emptiness — closing the
  "no defects found" class on LG-9 and the mirror false-rejection on
  LG-13 (RD36-04); §5's eighth declared field, the `Reviewer:`
  fresh-context disclosure, joins LG-12's presence set (RD36-05). The
  fixture discipline RD-36 prescribed is adopted: changed predicates
  are fixtured in both directions, and the empty and shadowed field
  cases are fixtured, not only the absent case — 74 fixtures, the two
  decisive repairs re-proven by mutation. Semantic delta:
  `round-2026-08e/LAUNCH-GATE-v1.9-SEMANTIC-DELTA.md` (which also
  carries the correction of the v1.8 delta's D-6, in the D-10
  convention — the frozen record is not edited). No existing question
  weakened; no ID renumbered.
- **v1.10** (2026-08-10, post-RD-37 amendment — the v1.9 re-review's two
  MAJOR and four MINOR findings; candidate, owner approval pending) — a
  **validator-and-records batch** a third time: no question block, no
  verdict word, and no section §1–§8 changed; the instrument bytes that
  move are this entry and the version header. The batch adopts RD-37's
  uniformity rule — a predicate serves consumers of one polarity only,
  and a parsing repair reaches every field, with the selftest asserting
  the uniformity itself. LG-13's emptiness became a positive test over
  the closed marker vocabulary §5's own slot names (`empty` / `none` /
  `none identified`) [corrected 2026-08-10, RD38-02: §5's slot is
  `<empty | enumerated items>` and names no vocabulary — the marker
  list is validator policy, published in LG-13's error message; see the
  v1.11 entry below], never the negation of the placeholder test — the
  v1.9 negation-prefix rule, shared across checks of opposite polarity,
  had silently loosened LG-13 into accepting negation-led lines that
  still enumerate reopen items, a measured regression against v1.8
  (RD37-01). Every declared field — the three §5 content fields and the
  label-shaped §2 integrity anchors included — now parses by collecting
  all occurrences, disagreements erroring in both orders, and a
  source-scan meta-fixture fails any future field that reverts to a
  first-match read (RD37-02, RD37-06). LG-4's G1 test anchors to the
  heading's own shape rather than a substring mention (RD37-03); the
  `--prior` record is validated against the question roster before the
  New-findings column trusts it (RD37-04); the SDR existence guard
  matches at identifier boundaries and excludes the pending-decision
  queue from its corpus (RD37-05 — the anchoring's substring direction
  is unfixturable against the live gapless population, stated rather
  than silent). 86 fixtures; all four decisive repairs re-proven by
  mutation, each failing exactly the fixtures it added. Semantic delta:
  `round-2026-08e/LAUNCH-GATE-v1.10-SEMANTIC-DELTA.md` (which also
  carries the correction of the v1.9 delta's D-4 — the sentence
  claiming the negation edge fails "never as a silent pass" was false
  of LG-13 — in the D-10 convention: the frozen record is not edited).
  No existing question weakened; no ID renumbered.
- **v1.11** (2026-08-10, post-RD-38 amendment — the v1.10 re-review's
  one BLOCKING, two MAJOR and four MINOR findings; candidate, owner
  approval pending) — a **validator-and-records batch** a fourth time:
  no question block, no verdict word, and no section §1–§8 changed; the
  instrument bytes that move are this entry, the version header, and
  one dated correction marker in the v1.10 entry above, whose grounding
  for the LG-13 marker vocabulary was false — §5's slot is
  `<empty | enumerated items>` and names no vocabulary; the vocabulary
  is validator policy, and it is now **published in LG-13's own error
  message** so a reviewer can learn the lawful markers from the
  rejection itself (RD38-02). The record-versus-quotation distinction
  reaches every check: fenced blocks are stripped from the text all
  checks read, on the record and the `--prior` side alike, so a fenced
  quotation of §5's template satisfies nothing (a record that deletes
  its G1 section and six declared fields no longer validates by quoting
  the template — RD-38's composite now scores the same seven errors
  with the appendix as without it [corrected 2026-08-10, RD39-02: true
  of the fenced carrier only — an HTML comment, a blockquote, an
  indented block, or one line of prose still satisfied the presence
  checks at v1.11; see the v1.12 entry below]) and shadows nothing (a quoted
  example row fires no duplicate or disagreement check) (RD38-01,
  BLOCKING). The three §2 integrity anchors are brought under RD36-02's
  line-anchoring rule that the other declared fields already carry —
  `^`-anchored, never crossing a newline — so an empty digest field is
  absent rather than borrowing the next line, and a mid-line narrative
  mention ("I checked whether Instrument version: v1.9 would be
  accepted") is inert instead of becoming the value LG-2/LG-11 report
  on (RD38-03). The marker vocabulary widens to ten honest emptiness
  forms (`empty`, `none`, `none identified`, `none known`, `n/a`, `na`,
  `nil`, `nothing`, `zero`, `0`), decoration-stripped, and the LG-13
  message says what the field *carries*, never that it "enumerates"
  (RD38-02/RD38-07); `_decl` returns the same normalization the
  disagreement rule compares on (RD38-07). The evadable source-scan
  meta-fixture is replaced by what RD-37 actually prescribed,
  behaviorally: a generated loop drives a disagreeing decoy through
  every declared label in both orders — twenty fixtures from one loop —
  so a field reverted to a first-match read fails by the behavior it
  changes, not by a syntactic pattern a refactor can evade (RD38-04).
  The `--prior` record now obeys the same closed verdict vocabulary and
  duplicate-row rules a current record obeys (RD38-06; disclosed
  residual: a bare roster-complete row block with lawful verdicts is
  still a lawful prior, because a prior administration lawfully names
  an older instrument version and digests, so no version cross-check
  can refuse it [corrected 2026-08-10, RD39-05: the impossibility
  claim is false — the validator verifies a record against the commit
  the record itself names, so a prior can be held to its own anchors;
  see the v1.12 entry below]). 116 fixtures; **eight** mutation-reverts, each
  failing exactly the fixtures its repair added [corrected 2026-08-10,
  RD39-03: false for one of the eight — reverting `_decl`'s return to
  the exact v1.10 bytes failed nothing, because v1.10 returned a
  stripped value, not a raw one; see the v1.12 entry below], including a
  first-match reversion carrying RD-38's own comment-evasion shape,
  caught behaviorally in both orders; RD-38's attack records
  re-executed — the composite scores 7 errors, the borrowed digest is
  refused as absent, the narrative mention is inert, the eleven honest
  emptiness wordings accept while `unknown`/`TBD` still reject (an
  unknown reopen-list is not an empty one). Semantic delta:
  `round-2026-08e/LAUNCH-GATE-v1.11-SEMANTIC-DELTA.md` (which also
  carries the corrections of the frozen v1.10 delta's D-2 first-bullet
  vocabulary claim, its both-directions sentence, and its D-3
  meta-fixture sentence, in the D-10 convention — the frozen record is
  not edited). No existing question weakened; no ID renumbered.
- **v1.12** (2026-08-10, post-RD-39 amendment — the v1.11 re-review's
  two BLOCKING, two MAJOR and three MINOR findings; candidate, owner
  approval pending) — a **validator-and-records batch** a fifth time:
  no question block, no verdict word, and no section §1–§8 changed; the
  instrument bytes that move are this entry, the version header, and
  three dated correction markers in the v1.11 entry above, whose
  quotation claim (RD39-02), mutation claim (RD39-03) and prior-side
  impossibility claim (RD39-05) were each false of the bytes. The batch
  adopts RD-39's diagnosis — a repair must be specified over the
  **property** the instrument requires, then verified against every
  carrier and every downstream rule that property touches, including
  the rules the repair itself newly stands upstream of: *"a strip is
  not a distinction, and inserting one changes the meaning of every
  rule defined over the text it edits."* The terminal `GATE VERDICT:`
  line is measured over the **raw record bytes** — v1.11's fence strip,
  inserted upstream of RD35-02's terminal-line rule, had silently
  redefined "last", so a stored terminal `NOT READY` behind an
  unterminated fence was reported `READY FOR <the verbatim target>`;
  now, if the raw terminal line is not the active terminal line, the
  record errors loudly and no earlier line is parsed in its place — a
  verdict quoted after the record's own terminal verdict is ambiguous,
  never silently resolved [corrected 2026-08-11, RD40-01: false of the
  v1.12 bytes — the rule compared raw text to stripped text, so a
  verdict quoted in a blockquote, an indented code block, a list item
  or a line of prose was present in both, agreed, and was parsed as
  the terminal verdict; four such records validated at 0 errors with
  a stored `NOT READY` reported as `READY FOR <the verbatim target>`.
  Made true at v1.13 by the own-line predicate; see the v1.13 entry
  below] (RD39-01, a hole the v1.11 batch itself
  created and this batch closes). The presence checks become the
  record-versus-quotation **distinction** rather than another carrier
  strip: the six `Label:` presence tokens are line-anchored field
  reads (≤3-space indent per CommonMark, list markers and bold
  decoration lawful, internal whitespace normalized — closing RD39-07
  in the same stroke), so blockquoted, deep-indented, and mid-line
  prose carriers of a label satisfy nothing; the non-authority banner
  gets a structural test — a blockquote line carrying the phrase,
  §5's own form; and HTML comments join fences in the strip, since a
  comment is the one carrier no reader ever sees (RD39-02). The fence
  grammar aligns with CommonMark where RD-39 measured divergence: a
  fence marker counts only at ≤3 spaces of indentation, and a closing
  run must be at least as long as the opening run (RD39-06). The
  `--prior` record is validated **as a record at its own named
  commit** — LG-1/LG-2/LG-11 already verify against the commit a
  record itself names, which is RD-39's refutation of the v1.11
  impossibility claim, adopted as the repair — so a bare
  roster-complete row block, lawful verdicts or not, is refused, and
  the all-`Not met` fabrication that drove New-findings to zero is
  refused with it (RD39-05; honest cap: a forged but fully
  lawful-shaped record naming a real commit remains representable —
  the guard raises the bar to the full lawful shape at the prior's
  own anchors, and claims no impossibility). The internal-whitespace
  acceptance — the behavioral change the v1.11 normalization repair
  actually made — gains its fixture, so reverting `_decl`'s return to
  the exact v1.10 bytes now fails a fixture, satisfying verification
  rule 6 against the code the repair replaced (RD39-03). 132
  fixtures; seven mutation-reverts, each failing exactly the fixtures
  its repair added; RD-39's attack records re-executed — the
  laundered record errors loudly with no verdict parsed, the
  indented-carrier record parses its visible `NOT READY`, and the
  composite rejects in all four carriers (disclosed limit: a
  nested-blockquote quotation of the banner still satisfies the
  banner's structural test, because §5's banner is itself a
  blockquote — the other six fields and LG-4 still reject such a
  record [corrected 2026-08-11, RD40-02: false of the v1.12 bytes —
  the presence anchor admitted a leading list marker, so a bullet-list
  quotation of §5's field template satisfied all six `Label:` tokens;
  with the banner nested-blockquoted and a column-0 `## G1` heading in
  the same appendix, a record carrying none of the eight fields
  validated at 0 errors under `READY FOR <the verbatim target>`. The
  six fields and the banner were made to reject at v1.13 (measured: 6
  errors); LG-4 is *not* among them — see the v1.13 entry's disclosed
  limits below]). Semantic delta:
  `round-2026-08e/LAUNCH-GATE-v1.12-SEMANTIC-DELTA.md` (which also
  carries the corrections of the frozen v1.11 delta's D-7 premise,
  its "reaches every check" claim, its directionality statement, and
  its D-6 impossibility sentence, in the D-10 convention — the frozen
  record is not edited). No existing question weakened; no ID
  renumbered.
- **v1.13** (2026-08-11, post-RD-40 amendment — the v1.12 re-review's
  two BLOCKING, three MAJOR and three MINOR findings; candidate, owner
  approval pending) — a **validator-and-records batch** a sixth time:
  no question block, no verdict word, and no section §1–§8 changed;
  the instrument bytes that move are this entry, the version header,
  and two dated correction markers in the v1.12 entry above, whose
  ambiguity claim (RD40-01) and disclosed-limit claim (RD40-02) were
  each false of the bytes the approval digest would have bound. The
  batch adopts RD-40's prescription in place of its own habit:
  *"stop enumerating carriers and enumerate the question."* Five rules
  asked "is this line the record's own, not a quotation of it?" and
  answered it five different ways; four consecutive blocking findings
  (RD38-01, RD39-01, RD40-01, RD40-02) were that one question answered
  inconsistently. There is now **one own-line predicate**, written
  once and applied by every consumer: after the fence and
  HTML-comment strip, a line is the record's own when it carries no
  blockquote marker (the banner alone excepted, which requires
  *single-level* `> `, §5's own form, so a nested `> > ` quotation
  now fails), sits at **≤3 columns** of indentation with tabs
  expanded to 4-column stops, carries no list marker of any kind
  (`-`, `*`, `+`, ordered) [corrected 2026-08-11, RD41-01: false of the
  v1.13 bytes — the predicate was line-local, and a container is a
  REGION, not a line: `- `, `> `, `1. ` and four spaces each mark a
  block's FIRST line and every one of them continues without its
  marker, so a list item's continuation lines were classified as the
  record's own and RD-38's composite validated at 0 errors under
  `READY FOR <the verbatim target>` a fifth time. Made true at v1.14 by
  a predicate that carries the block stack across lines; see the v1.14
  entry below], is not the text line of a setext heading [corrected
  2026-08-11, RD41-06: a setext heading is the record's own visible
  text, not a quotation of it, and putting it in the containment
  predicate made a `---` under the terminal verdict hide the decisive
  line behind a message untrue of the record. At v1.14 it is a separate
  declaration-form requirement, consumed by the field reads and not by
  the terminal-verdict rule], and is not inside a raw-HTML block (`<details>`/`<summary>`). Its
  consumers are the terminal-verdict rule, the six `Label:` presence
  tokens, the non-authority banner test, and the G1 anchor. `_decl`
  is deliberately **not** a consumer: it is `^`-anchored with no
  decoration allowance at all, so every quotation carrier either
  fails the anchor outright or produces a loud disagreement error —
  a stated scope decision, not an omission. [corrected 2026-08-11,
  RD41-02: false of the v1.13 bytes. A `<details>` block and setext
  heading text both reach column 0, so `_decl` read them; and where a
  record declared the field nowhere else there was no disagreement to
  be loud about — the quotation silently BECAME the declared value. A
  record whose reopen items were visible prose and whose
  `E3 reopen-list: empty` sat inside collapsed content validated at 0
  errors under `READY FOR <the verbatim target>`, as did a hidden
  `Owner deferral decision:`. The scope decision was also internally
  inconsistent: `Unknowns and what would settle them:` inside
  `<details>` errored while `E3 reopen-list:` did not. At v1.14 `_decl`
  IS a consumer for presence — a value carried only on non-own lines
  is an absent field — with the loud-disagreement behaviour on own
  lines unchanged; see the v1.14 entry below] The terminal-verdict rule
  is computed over the **raw** bytes in the predicate's shape:
  a `GATE VERDICT:` line quoted *after* the record's own terminal
  line — in a blockquote, an indented code block, a list item, or a
  sentence of prose — is now an ambiguity error rather than the
  parsed verdict (RD40-01; four such records had validated at 0
  errors, each converting a stored `NOT READY` into `READY FOR <the
  verbatim target>`), and a record whose *every* `GATE VERDICT:` line
  is a quotation is refused by name rather than resolved. The v1.12
  presence anchor's list-marker allowance is **reversed** (RD40-02):
  `- Operationalization notes:` was accepted at v1.12 as lawful
  decoration and is rejected at v1.13 as a quotation — the deliberate
  loss of an RD39-07 acceptance, taken because the decoration
  allowance *is* the canonical carrier of a quoted field list, and
  because presence and lawful-decoration were two requirements merged
  into one regex. Tabs are expanded before every indentation
  measurement, opening and closing fence alike, since CommonMark's
  bound is three *columns* and one tab had been deleting a line every
  reader sees (RD40-03). The LG-11 version-disagreement fixture is
  rebuilt on the RD34-05 shape: the template's `Instrument version:`
  literal is rewritten to the committed instrument's own
  `effective_version` before mutation, so the fixture can no longer
  be satisfied by its unmutated baseline (RD40-04); a dead
  row-verdict helper is deleted and the single row normalization
  documented at the loop that owns it (RD40-07). **145 fixtures**;
  eight [corrected 2026-08-11, RD41-03: **ten** — the figure the v1.13
  delta, P-34, PROJECT-STATUS and the disposition register all state,
  and the one the bytes do; "eight" was carried over from the v1.11
  entry. Verification rule 3's own case, inside the artifact an
  approval digest binds] mutation-reverts, each failing exactly the fixtures its
  repair added, with one honesty qualification measured rather than
  asserted (RD40-08's own standard): the list refusal is carried
  **twice** — by the predicate and by the presence anchor — so each
  single-layer revert fails 0 presence fixtures and only the combined
  revert to v1.12's exact configuration fails 2; the combined revert
  is the behavioral witness, and the redundancy is defense in depth,
  not two proofs. RD-40's attack records re-executed at the named
  commit with git checks on and real digests: each of the four
  quoted-after-terminal carriers errors (1 each) with the trend
  verdict column blank; the all-quoted record errors by name; RD-38's
  composite carried on a bullet list, with the banner nested-
  blockquoted, rejects at **6 errors** (five `Label:` fields and the
  banner); and the tab-fence record now scores exactly what its
  four-space control scores (3 errors, `Deferred count` read as 3)
  where at v1.12 it scored 0. **Disclosed limits, each measured:**
  LG-4 is satisfied by a column-0 `## G1` heading wherever it sits
  and however empty the section beneath it — that heading *is*
  structurally the record's own, so this is an emptiness question and
  not a quotation question, and it is left to a later batch; it opens
  no pass (the composite scores 6 errors with the heading and 7
  without) [corrected 2026-08-11, RD41-04: the parenthetical
  measurement is exact and reproduces; the generalization is false —
  the residual was a load-bearing limb of a **0-error** pass (RD41-01's
  composite), not a cost of one error inside an already-failing record.
  It was also wider than disclosed: LG-4's `\s*` crossed the newline,
  so a bare `###` followed by any own line beginning `G1 ` satisfied
  the anchor with no G1 heading at all — RD37-03's class returning
  through a door nobody checked. Both are closed at v1.14: LG-4 now
  requires the heading to open a non-empty section, and its anchor is
  matched per line. **This is the third batch running whose disclosed
  limit was true narrowly and false as stated; the v1.14 entry states
  its limits as measurements and nothing wider**]. An asymmetric `**Label:*` still satisfies presence, and
  the trend row is still printed above the error list carrying the
  record's *claimed* verdict when the record is invalid — both
  carried forward from RD-40's minor findings. Semantic delta:
  `round-2026-08e/LAUNCH-GATE-v1.13-SEMANTIC-DELTA.md` (which also
  carries the corrections of the frozen v1.12 delta's D-2 fourth
  limb, its disclosed-limit generalization, its D-4 "CommonMark's own
  bound" phrasing, its directionality assignment, and its D-5
  mutation denominator, in the D-10 convention — the frozen record is
  not edited). No existing question weakened; no ID renumbered.
- **v1.14** (2026-08-11, post-RD-41 amendment — the v1.13 re-review's
  four BLOCKING, four MAJOR and four MINOR findings; candidate, owner
  approval pending) — a **validator-and-records batch** a seventh time:
  no question block, no verdict word, and no section §1–§8 changed;
  the instrument bytes that move are this entry, the version header,
  and four [corrected 2026-08-11, RD42-05: **five**. The v1.13 entry
  carries markers for RD41-01, RD41-06, RD41-02, RD41-03 and RD41-04;
  the count was written from the four findings the sentence then names
  and never recounted against the bytes. Counted at v1.15 with Python
  `re` over the entry's span, not by eye — with a pattern that tolerates
  the line wrap (`\[corrected\s+2026-\d\d-\d\d,\s+(RD\d\d-\d\d)`), since
  a marker whose date and finding id fall on different lines is invisible
  to the obvious one-line pattern and both entries carry such markers] dated correction markers in
  the v1.13 entry above, whose
  predicate definition (RD41-01), `_decl` scope sentence (RD41-02),
  mutation count (RD41-03) and disclosed-limit generalization
  (RD41-04) were each false of the bytes an approval digest would have
  bound. RD-41 verified every one of RD-40's eight findings present
  and six closed outright, reproduced all ten mutation denominators,
  the fixture arithmetic, the §1–§8 identity and the frozen
  population — and then broke the batch's central claim one level up.
  **The predicate now carries state.** v1.13 enumerated markdown's
  containers; RD-41's finding is that a container is a **region, not a
  line** — `- `, `> `, `1. ` and four spaces each mark a block's
  *first* line, and every one of them continues without its marker, so
  a list item's continuation lines were classified as the record's own
  and RD-38's composite validated whole a fifth time. The predicate is
  now CommonMark's block-structure phase in the subset this instrument
  needs: for each line, the stack of containers open at it —
  blockquote at any depth, list item at its content column, raw-HTML
  block [corrected 2026-08-11, RD42-01: false of the v1.14 bytes — the
  HTML limb was not a block at all but a counter over two tag names,
  `<details>` and `<summary>`, decrementable by an inline code span.
  `<div style="display:none">`, `<p style="display:none">`,
  `<span hidden>` and `<table><tr><td>` each carried a declared field
  past it, and a `` `</details>` `` written as prose reopened the one
  element it named while every renderer left it closed. The batch had
  adopted "the predicate carries state" for markdown's containers and
  written an enumeration for HTML's — the enumeration returning inside
  the repair that replaced enumeration. At v1.15 it is an ELEMENT-
  nesting decision: a region opens at a line whose content begins with
  a tag of any name, every tag inside the region is read, a close tag
  pops back to the element it names and pops nothing if it names none,
  code spans are removed before any tag is read, and self-closing and
  void forms open nothing; see the v1.15 entry below] — maintained
  across lines, with lazy continuation; a line is
  the record's own iff that stack is empty, and `bq1` iff it is
  exactly one blockquote. Three things this repair had to decide, each
  stated rather than assumed. **Blockquote laziness is deliberately
  not implemented**, and §5 is the reason: §5's own template places the
  declared fields on unmarked lines directly beneath the blockquote
  banner, so strict CommonMark laziness would refuse every lawful
  record, that template first (measured: 43 fixtures fail). A
  blockquote therefore ends at the first line not carrying its marker,
  and the limit that leaves is fixtured in its accepting direction
  rather than described. **Setext headings leave the predicate** — a
  heading is the record's own visible text, not a quotation of it — and
  become a separate declaration-form requirement consumed by the field
  reads and not by the terminal-verdict rule, where v1.13's version
  made a `---` under the verdict hide the decisive line behind a
  message untrue of the record (RD41-06, with four further lawful
  records restored: a fenced `<details>` example, a self-closing
  `<details/>` in prose, and a comment mentioning `<details>`, each of
  which the v1.13 raw-side call refused because it ran on *un*-stripped
  text where §9 said "after the strip" [corrected 2026-08-11, RD42-06:
  as written, true of one of the four. Measured on the fixtures' own
  bytes, three — the fenced `<details>` example, the self-closing
  `<details/>` in prose, and the comment mentioning `<details>` —
  validate at 0 errors at v1.13 as well (only the `---` case moved 1 →
  0), because each was written BELOW the record's
  terminal verdict, where v1.14's own new rule already refuses to read
  anything; the fixtures witnessed that rule, not this repair. At v1.15
  those three are rebuilt above the verdict (the fourth tests a `---`
  after the verdict and belongs where it is) and both repairs are
  witnessed directly: reverting the raw-side call to un-stripped text fails the
  fenced-`<details>` fixture (1 of 187, mut15 m9), and applying the
  setext requirement to the terminal rule fails the `---` fixture (1 of
  187, m10)]). **`_decl` becomes a
  consumer** (RD41-02): a declared value carried only on non-own lines
  is an absent field, never a supplied one [corrected 2026-08-11,
  RD42-03: true of nine of the ten call sites, not of `Parameter block
  sha256:`, which still read the full active text — so §2's integrity
  anchor, the value that binds a record to the instrument bytes it was
  administered under, could be supplied from collapsed content BELOW
  the terminal verdict, and the record was then refused for a digest
  *mismatch* it did not have rather than for the absence it did. Fixed
  at v1.15, with the call sites enumerated mechanically rather than
  counted by eye: 10 of 10 read the record's own lines]. And because a quotation
  whose fields land at column 0 unmarked is byte-for-byte §5's own
  declaration form — §5 defines no marker that would tell the two
  apart — two further rules close what containment cannot: a
  declaration is read only from lines at or above the record's own
  terminal verdict (§5 places every field there, and the verdict is
  terminal), and a field whose value is §5's own angle-bracket
  placeholder has not been answered. LG-4 requires its heading to open
  a **non-empty** section and matches its anchor per line (RD41-04);
  unicode whitespace is folded before the `GATE VERDICT:` token is
  searched for, closing a record whose visible terminal `NOT READY`
  was invisible to a literal substring search while an earlier `READY
  FOR` was reported in its place (RD41-08); the LG-1 commit-existence
  fixture is rebuilt from a real commit so its mutation is what makes
  its assertion true (RD41-11). **168 fixtures**; **sixteen**
  mutation-reverts, fourteen [corrected 2026-08-11, RD42-04:
  **thirteen**. D-7's revert — the raw-side predicate call — fails **0
  of 168**, a third unwitnessed repair alongside the two this entry
  already discloses, and the fourteen was carried over from the
  batch's plan rather than recounted from the runs. The denominator
  list that follows has fourteen entries for thirteen witnesses]
  of which fail exactly the fixtures their
  repair added (denominators 1, 1, 1, 43, 5, 1, 1, 1, 1, 1, 5, 1, 3,
  3). **Disclosed limits, each measured, none generalized:** two
  predicate clauses — the tab expansion and the ≤3-column bound — fail
  **0 of 168** when reverted alone, because every consumer either
  requires `bq1` or carries its own `^ {0,3}` anchor; they are
  defence-in-depth, they have no single-layer witness, and this entry
  says so rather than counting them as proven (RD41-10). Unmarked
  lines beneath any blockquote are the record's own, per the §5
  decision above. An asymmetric `**Label:*` still satisfies presence,
  and the trend row is still printed above the error list carrying the
  record's *claimed* verdict when the record is invalid — both carried
  forward. Semantic delta:
  `round-2026-08e/LAUNCH-GATE-v1.14-SEMANTIC-DELTA.md` (which also
  carries the corrections of the frozen v1.13 delta's directionality
  assignment, its "only direction lost" sentence, its
  `effective_version` count, and its disclosed-limit generalization,
  in the D-10 convention — the frozen record is not edited). No
  existing question weakened; no ID renumbered.
- **v1.15** (2026-08-11, post-RD-42 amendment — the v1.14 review's six
  BLOCKING, three MAJOR and four MINOR findings; candidate, owner
  approval pending) — a **validator-and-records batch** an eighth time:
  no question block, no verdict word, and no section §1–§8 changed;
  the instrument bytes that move are this entry, the version header,
  and five dated correction markers in the v1.14 entry above, whose
  predicate description (RD42-01), `_decl` scope claim (RD42-03),
  mutation count (RD42-04), marker count (RD42-05) and restoration
  claim (RD42-06) were each false of the bytes an approval digest
  would have bound. RD-42 verified all twelve RD-41 findings present,
  reproduced the fixture arithmetic, the §1–§8 identity and the frozen
  population, ran every captured fixture through both validators on
  identical bytes — and found the same question answered inconsistently
  a sixth time. **The HTML limb was the enumeration the batch said it
  had abandoned.** v1.14 carried state for markdown's containers and a
  two-tag-name counter for HTML's, so `<div style="display:none">`,
  `<p style="display:none">`, `<span hidden>` and `<table><tr><td>`
  each hid a declared field from the reader [corrected 2026-08-11,
  RD43-01's method applied to this batch's own claim: four of the five
  hide it; `<table><tr><td>` does not — measured with `pandoc` and
  `html5lib`, the field sits in a `td` a reader sees. The predicate
  refuses it all the same, because deciding *hiding* means evaluating
  CSS the instrument cannot evaluate; that over-refusal is named at
  v1.16 rather than described as harm prevented] while the validator
  read it as the record's own, and an inline `` `</details>` `` code span
  reopened the one element the counter did know. At v1.15 a raw-HTML
  region is an **element-nesting** decision, like every other container
  in the predicate: it opens at a line whose content begins with a tag
  of any name; inside it every tag on every line is read; a close tag
  pops back to the element it names and pops nothing if it names none,
  so `<table><tr><td>` … `</td></tr></table>` closes where a reader
  sees it close [corrected 2026-08-11, RD43-01: false of the v1.15
  bytes in both directions, measured against `pandoc` + `html5lib`
  rather than argued. The region CLOSED where a reader does not — a
  `</details>` written as an indented code block, and a
  backslash-escaped `\</details>`, each render as literal text and
  leave the element open, and v1.15 popped on both. And it FAILED to
  open where a reader sees it open — a `<div style="display:none">`
  mid-sentence (CommonMark start condition 6 interrupts a paragraph,
  and HTML5 closes the open `<p>`), and an opening tag split across two
  lines (`<div` with no `>` on the line). Each of the four carried
  `E3 reopen-list: empty` past the validator at **0 errors** under
  `READY FOR <the verbatim target>`, with the field's DOM ancestor
  measured as `details` or a display:none `div`. Repaired at v1.16, and
  the repair is stated as what it is: the block phase is decided first
  and tags are read only out of what survives it] and a lawful record
  carrying a closed appendix keeps
  its own verdict readable; code spans are removed before any tag is
  read; self-closing and void forms open nothing [corrected 2026-08-11,
  RD43-01: true of void forms, false of self-closing ones. HTML5 ignores
  the slash on a non-void HTML element, so `<div/>` opens a `div` and
  `<details/>` opens a `details` — measured. v1.16 opens on both, and the
  two fixtures that asserted otherwise are flipped]. Outside a region a
  line must **begin** with a tag to open one, so a reviewer writing
  *about* a carrier — a `<details>` named mid-sentence, a
  `` `<summary>` `` in a code span, a `<details>` in a table cell —
  no longer breaks their own record: three lawful records that v1.14
  refused with 8, 8 and 1 errors now validate clean (RD42-09)
  [corrected 2026-08-11, RD43-01: two of the three are lawful; the
  `<details>` named mid-sentence is not. RD-42 measured it with
  `lxml.html` — libxml2's legacy parser — and under the HTML5 algorithm
  browsers and GitHub implement, an unescaped `<details>` mid-sentence
  closes the open paragraph and collapses everything below it. v1.16
  withdraws that acceptance and refuses the record with a message true
  of it; the code-span and table-cell forms stay lawful, and they are
  how a reviewer writes about a carrier safely]. The
  same door had laundered a verdict: a `READY FOR` hidden in collapsed
  content below a record's visible terminal `NOT READY` was reported
  as the record's verdict, in pure ASCII, which is the harm the unicode
  fold was taken for (RD42-02). `Parameter block sha256:` — the tenth
  `_decl` site, and §2's integrity anchor — now reads the record's own
  lines like the other nine, with the sites enumerated mechanically
  rather than counted (RD42-03). LG-4's emptiness requirement excludes
  §5's declared trailer fields from G1 section content, so a bare
  `## G1` in the shape §5 mandates opens an EMPTY section instead of
  validating at 0 errors (RD42-07) [corrected 2026-08-11, RD43-04: true
  of the refusing direction, and the accepting direction was withdrawn
  in silence. What remained after the trailer filter had also to be a
  line of the record's OWN — a containment test, and the wrong one for a
  *section* — so G1 content written as a bulleted list, a numbered list,
  a blockquote, a fenced block or indented code was refused with
  "opens an EMPTY section", a message untrue of a record whose G1
  section a reader plainly sees has content. A bulleted list is the
  natural form for a completeness critic's output. v1.16 asks presence
  over the raw lines instead, with an accepting fixture for each of the
  five forms], and one heading regex requires the
  space CommonMark requires, so `###G1` is not a heading (RD42-11).
  The angle-bracket placeholder rule keeps its shape and loses its
  false sentence: the message now states what it matched — a value
  written entirely inside angle brackets, which is §5's template form
  and not an answer — rather than claiming the value is §5's own
  placeholder text, which it need not be (RD42-08); matching §5's
  literal strings instead was considered and rejected by measurement,
  because the exploit abbreviates the template it quotes. **187
  fixtures**; **thirteen** mutation-reverts, twelve of which fail
  exactly the fixtures their repair added (denominators 10, 3, 2, 3, 1,
  1, 1, 1, 1, 2, 1, 1). **Disclosed limits, each measured, none
  generalized:** the raw-HTML-line classification — a line whose own
  content begins with a tag is raw HTML, not the record's own text —
  fails **0 of 187** when reverted alone (m4), because every declared
  value is read `^`-anchored and the verdict-token scan counts raw
  lines; it is defence in depth and this entry says so rather than
  counting it as proven. The two v1.14 clauses with no single-layer
  witness (tab expansion, the ≤3-column bound) remain so. A record
  line whose own text *begins* with an inline tag is read as raw HTML
  and cannot carry a declaration; §5's fields begin with their labels,
  and no fixture in the corpus is affected [corrected 2026-08-11,
  RD43-03: understated on two counts. The consequence is not that the
  line cannot carry a declaration — it is that **every line after it,
  including the terminal verdict, stops being the record's own**: a
  lawful record scored 8 errors, among them LG-6 telling the
  administrator their column-0 terminal verdict sat "inside a container
  opened on an earlier line". And the shapes that triggered it are not
  tags: a CommonMark **autolink** (`<https://…>`, `<owner@example.com>`)
  and the `<word …>` shorthand §5's own template writes for an unfilled
  value. "No fixture in the corpus is affected" was true and is VIS-2's
  own case — the corpus is the measurement, not the population. v1.16
  excludes autolinks before any tag is read and confines inline elements
  to their own paragraph]. §5's non-authority banner
  can still be satisfied by a quotation of the banner in an appendix
  (RD42-12, carried forward: the banner is the one line whose
  quotation is indistinguishable from its assertion). The depth scan
  is quadratic in nesting depth on adversarial input (RD42-13, carried
  forward; records are short and the scan is read-only). An asymmetric
  `**Label:*` still satisfies presence, and the trend row is still
  printed above the error list carrying the record's *claimed* verdict
  when the record is invalid — both carried forward. Semantic delta:
  `round-2026-08e/LAUNCH-GATE-v1.15-SEMANTIC-DELTA.md` (which also
  carries the corrections of the frozen v1.14 delta's false claims, in
  the D-10 convention — the frozen record is not edited). No existing
  question weakened; no ID renumbered.
- **v1.16** (2026-08-11, post-RD-43 amendment — the v1.15 review's two
  BLOCKING, two MAJOR and three MINOR findings; candidate, owner
  approval pending) — a **validator-and-records batch** a ninth time:
  no question block, no verdict word, and no section §1–§8 changed;
  the instrument bytes that move are this entry, the version header,
  and **six** dated correction markers in the v1.15 entry above
  (counted over that entry's span with a wrap-tolerant pattern, the
  method RD42-05 made necessary), whose element-nesting sentence,
  self-closing clause, RD42-09 acceptance claim, carrier claim, LG-4
  claim and inline-tag residual were each false or materially
  incomplete of the bytes an approval digest would have bound. RD-43
  verified all thirteen RD-42 findings present — **eight closed
  outright**, two closed for everything the finding constructed, one
  closed in its refusing direction only, one partially, **one not
  closed** — reproduced the fixture arithmetic by set difference of
  printed fixture names, reproduced twelve of thirteen mutation
  denominators with the thirteenth at 0 exactly as disclosed, and
  measured the git-skip hazard the dispatch named (**175 fixtures**
  from a non-git directory, twelve `_git=True` fixtures silently
  absent) before running any mutant. **The method changed, and it is
  the durable part of this batch.** RD-43 settled every claim about
  what a reader sees by rendering the record with `pandoc` and parsing
  it with an HTML5 parser, and this batch adopts that as its rule: a
  claim about a reader is a measurement of the rendered document, never
  a reading of the CommonMark specification. Applied, it falsified
  v1.15 in both directions at once. The region **closed where a reader
  does not**: a `</details>` written as an indented code block, and a
  backslash-escaped `\</details>`, each render as literal text and left
  the element open while v1.15 popped on them. It **failed to open
  where a reader sees it open**: a condition-6 element mid-sentence
  closes the open paragraph, and an opening tag needs no `>` on its own
  line. Four carriers followed, each supplying `E3 reopen-list: empty`
  from content whose DOM ancestor is `details` or a display:none `div`,
  at **0 errors** under `READY FOR <the verbatim target>` — and one of
  them laundered a verdict below a record whose last visible line read
  `GATE VERDICT: NOT READY` (RD43-01, RD43-02). At v1.16 the block
  phase is decided **first** — fences, HTML comments, indented code
  blocks, backslash escapes and code spans are literal text — and tags
  are read only out of what survives. **CommonMark's own start
  condition 6 names the elements that open a region from any position**,
  including mid-paragraph [corrected 2026-08-11, RD44-01, and the
  correction is of this batch's reading, not of any reviewer's:
  **false** — condition 6, like all seven start conditions, requires the
  line to BEGIN with the tag; what distinguishes it from condition 7 is
  that it may *interrupt a paragraph*, and closing a paragraph is not
  opening a region. What v1.16 implemented is HTML5's list of start tags
  that close an open `<p>` — a different fact about a different thing.
  Measured cost, swept with its denominator: of the 62 names, 53 named
  once mid-sentence in a reviewer's own G1 section blanked the rest of a
  lawful record — declared fields, G1 section and terminal verdict — and
  scored 0 errors before this batch. v1.17 returns the trigger to
  line-initial and confines mid-line openings to elements that take
  content out of sight]; every other name is condition 7, which
  cannot interrupt a paragraph, so it renders inline and reaches only to
  the end of its own paragraph — and only when it carries a hiding
  attribute (`hidden`, `display:none`, `aria-hidden`) does it carry a
  declaration out of sight [corrected 2026-08-11, RD44-03 and RD44-06:
  **false in both limbs**. By element type — CommonMark's start
  condition 1, `script`, `style`, `textarea` and `title` — content is
  raw text a browser never paints, from ANY position and past any blank
  line, and `<details>` collapses its content with no attribute at all;
  a mid-line `<script>` and a mid-line `<style>` each carried a whole
  record out of sight at 0 errors. And the three named attributes are an
  ENUMERATION, not a sufficiency condition: `visibility:hidden` and
  `opacity:0` hid a declared field at 0 errors. v1.17 gives condition 1
  its own rule, adds both properties, and states both lists as the
  enumerations they are]. That distinction is what keeps
  `Materials given: the fixed §2 list <plus the parameter block>`
  lawful. **An autolink is not a tag** (RD43-03): `<https://…>`,
  `<owner@example.com>` and §5's own `<word …>` shorthand are excluded
  before any tag is read, closing a defect that blanked every line
  after such a line — the terminal verdict included — and refused a
  lawful record with 8 errors. **A section's content is what a reader
  sees in it** (RD43-04): LG-4's emptiness test is asked over the raw
  lines, so G1 written as a bulleted list, a numbered list, a
  blockquote, a fenced block or indented code satisfies it, while a
  heading with nothing but §5's declared trailer beneath it still does
  not. **205 fixtures**; **twelve** mutation-reverts, **all twelve**
  failing exactly the fixtures their repair added (denominators 2, 1,
  15, 1, 1, 1, 2, 1, 5, 1, 2, 16) [corrected 2026-08-11, RD44-07(b) and
  RD44-08: the denominators reproduce exactly — RD-44 rebuilt all
  twelve — and the two characterisations around them do not. Two
  reverts (autolinks-read-as-tags, and the emptied condition-6 set) also
  break fixtures that PRE-DATE the batch, because they revert layers
  those fixtures already rested on, so "exactly the fixtures their
  repair added" is untrue of them. And seven of the 26 new-or-renamed
  fixtures are broken by no revert at all: they are accepting-direction
  fixtures documenting a lawful shape, which is a different job from
  witnessing a repair. The claim below of "no unwitnessed repair" is
  withdrawn — the measurement it stood in for is the twelve
  denominators, which hold] — the first batch of this chain with
  no unwitnessed repair, and two of the twelve earned their witness
  only after fixtures were added for constructions the corpus could not
  otherwise separate. **One acceptance is withdrawn on purpose:** a
  `<details>` named mid-sentence without escaping. RD-42 called that
  record lawful on an `lxml.html` parse; under the HTML5 algorithm it
  collapses everything below it, so v1.16 refuses it, and the code-span
  and table-cell forms — measured lawful — are how a reviewer writes
  about a carrier safely. Across the **54** stored attack records of
  the RD-39, RD-40, RD-41 and RD-42 rounds, run through both
  validators, that record is the **only** one whose output moves
  [corrected 2026-08-11, RD44-05: **withdrawn entirely**. The population
  is unidentifiable from four remembered harness sizes — RD-44 could
  reproduce neither the 54 nor the attribution — and the reviewer
  measured five movers, not one, two of which this batch's own delta
  table listed. It is the second consecutive round in which an attack-
  record regression claim proved unreproducible. v1.17 replaces the
  claim with a scripted corpus sweep whose population is defined by
  construction (every record the selftest hands to the validator,
  captured from each version's own run) and whose counts are printed by
  the script; the rule this chain adopts is that a regression claim
  quotes a script's output or does not appear].
  **Disclosed limits, each measured, none generalized:** the predicate
  refuses a declaration carried inside **any** raw-HTML element the
  record opens, whether or not that element hides it — `<table><tr><td>`
  and a bare `<div/>` are both refused and neither hides its content —
  because deciding *hiding* means evaluating CSS this instrument cannot
  evaluate; the over-refusal is in the safe direction and §5 never
  places a declared field inside raw HTML. The two v1.14 clauses with
  no single-layer witness (tab expansion, the ≤3-column bound) remain
  so. Blockquote laziness is still deliberately not implemented, for
  the §5-template reason stated at v1.14. §5's non-authority banner can
  still be satisfied by a quotation of itself in an appendix (RD42-12);
  the depth scan is still quadratic in nesting depth (RD42-13); an
  asymmetric `**Label:*` still satisfies presence; and the trend row is
  still printed above the error list carrying the record's *claimed*
  verdict when the record is invalid — all carried forward. Semantic
  delta: `round-2026-08e/LAUNCH-GATE-v1.16-SEMANTIC-DELTA.md` (which
  also carries the corrections of the frozen v1.15 delta's false
  claims, in the D-10 convention — the frozen record is not edited). No
  existing question weakened; no ID renumbered.
- **v1.17** (2026-08-11, post-RD-44 amendment — the v1.16 review's three
  BLOCKING, three MAJOR and two MINOR findings; candidate, owner
  approval pending) — a **validator-and-records batch** a tenth time: no
  question block, no verdict word, and no section §1–§8 changed; the
  instrument bytes that move are this entry, the version header, and
  **four** dated correction markers in the v1.16 entry above (counted
  over that entry's span with a wrap-tolerant pattern, the method
  RD42-05 made necessary), whose condition-6 sentence, condition-7
  sufficiency clause, mutation characterisation and attack-record
  regression claim were each false of the bytes an approval digest would
  have bound. RD-44 reproduced **every one of the twelve** mutation
  denominators, verified §1–§8 byte-identical at all eight byte counts
  across ten versions, confirmed the frozen v1.15 entry stripped of its
  six markers is byte-for-byte the frozen prose, reconciled 187 + 18 =
  205 by fixture-name set difference — and then found the same question
  answered inconsistently a seventh time, in the batch that adopted the
  method which answers it. **The method was adopted and not applied to
  the rule it was used to justify.** v1.16 decided the block phase first
  and then decided where a block *begins* from a list it had read out of
  the wrong specification: `pandoc` falsifies "condition 6 opens a
  region from any position" in three lines. **A region begins at a
  LINE, not at a `<`** — that sentence is RD-44's, and it is the durable
  part of this batch. Applied, it costs and it pays. The cost, swept
  with its denominator: **53 of the 62 names** in the condition-6
  enumeration, named once mid-sentence in a reviewer's own G1 section,
  blanked the rest of a lawful record at **0 errors** [corrected
  2026-08-11, RD45-09(b): the blanking scores **6** errors, not 0. The
  "0 errors" belongs to RD-44's sentence about v1.15, from which this
  one was compressed, and a compression that changes a measurement is
  not a compression] — RD43-03's harm
  widened from three shapes to fifty-three, inside the batch that closed
  RD43-03. The payment: **four independent constructions** each produced
  `record valid`, exit 0 and a trend row reading
  `READY FOR <the verbatim target>` beneath a record whose last visible
  line read `GATE VERDICT: NOT READY` — a mid-line `<script>`, a
  mid-line `<style>`, an indented-code `</details>` placed after an ATX
  heading rather than a paragraph, and a lone pipe-delimited line
  carrying a `display:none` div. All four are refused at v1.17, each
  with a fixture, and each was re-executed against this batch's bytes.
  At v1.17 the region trigger is **line-initial** for every name, and a
  **mid-line** tag opens a region only when it takes its content out of
  a reader's sight [corrected 2026-08-11, RD45-01 and RD45-03, and both
  limbs are this batch's own failure. **The rule is right and the set it
  ranges over was never measured**: the set shipped as condition 1 plus
  `details`, and `<iframe>`, `<noframes>`, `<noembed>` and `<select>`
  each carried a whole record out of sight at 0 errors — two of them
  refused at v1.16, and `iframe` a name RD-44 had recorded as correctly
  refused. Worse, 65 of the 83 new fixtures took their expected
  direction from that same set, so the corpus relabelled itself instead
  of failing. And a second change of meaning shipped **unrecorded**: the
  split-tag rule was narrowed to line-initial position and its
  condition-6 test dropped, which reopened the mid-line carrier in one
  direction and refused §5's own wrapped shorthand in the other. A delta
  that says it records every change of meaning recorded neither. v1.18
  generates the set against the render over an 84-name population and
  moves the fixtures' expectation to a literal measured table]: by element type — CommonMark's **condition 1**
  raw-text elements (`script`, `style`, `title`, whose content a browser
  never paints and inside which *nothing is a tag* until their own close
  arrives) and `details` (collapsed) — or by a hiding attribute
  (RD44-01, RD44-03, RD44-06). `textarea` is raw text that IS painted
  and is deliberately absent from the hiding set. `para_open` now means
  *a paragraph is open*: an ATX heading, a thematic break, a raw-HTML
  block line, a table row and a setext underline each end one, so an
  indented line after any of them is an indented code block (RD44-02).
  **A table row is a row of a table** — the carve-out is computed from a
  delimiter row beneath a header, not from the presence of two pipes
  (RD44-04). The hiding set gains `visibility:hidden` and `opacity:0`
  [corrected 2026-08-11, RD45-08: one spelling of one value. `opacity:.0`
  and `opacity:0%` are the same CSS value and each hid a declared field
  at 0 errors. v1.18 reads the property's value rather than matching a
  literal] and is stated as an **enumeration** beside the condition-6
  one, not as a sufficiency condition (RD44-06). LG-6 now names the line
  that opened
  the region an administrator's column-0 verdict sits inside, which the
  RD43-03 disposition promised and did not ship (RD44-01, second limb)
  [corrected 2026-08-11, RD45-05: **false of the shipped bytes**. The
  message named the last line *before* the region — a declared field
  that opened nothing — because the walk looked for the last line
  flagged as the record's own, and the line that opens a region is never
  one. The fixture asserted only that the substring "opened at line"
  appeared, so it passed. At v1.18 the opening line is carried on the
  region's own stack entry and the fixture asserts the line NUMBER].
  **288 fixtures** (205 + 83 new names, 0 dropped, 0 renamed, by set
  difference of printed names); **nine** mutation-reverts, one per
  repair, each run **inside a repository** so no git fixture is silently
  skipped, killing 54, 17, 1, 3, 1, 2, 1, 11 and 1 fixtures. **One
  finding is declined, with its measurement:** RD44-06 asked that the
  word "hidden" inside §5's angle-bracket shorthand stop counting, on
  the reading that `<see the hidden appendix>` is prose. Rendered, it is
  not — `hidden` is a **global boolean attribute** and HTML5 applies it
  to unknown elements, so the next declared field's DOM ancestry
  measures `see[HIDDEN]` and a reader does not see it. The record is
  refused, the code-span form is fixtured as the safe way to write it,
  and the widening limb of the same finding is adopted in full.
  **Regression, by script rather than by memory** (RD44-05): every
  record each version's own selftest hands to the validator was captured
  from both runs and replayed through **both** validators with that
  record's own git setting — 199 records at v1.16, 282 at v1.17, 200
  carried forward, 0 dropped — and **0 carried-forward records moved**.
  Of the 82 records added at v1.17, **65 are answered differently by
  v1.16**, which is the corpus RD-44 asked for: the accepting direction
  can now tell. Both counts are printed by the sweep script; neither is
  typed. **Disclosed limits, each measured, none generalized:** both
  enumerations are enumerations — the block-level names and the hiding
  attributes — and a construction outside either is read as prose; a
  close tag written inside a mid-line `<textarea>` is still parsed as a
  tag, which can end a region early and can never hide a field
  [corrected 2026-08-11, RD45-04: **false, and backwards**. Ending a
  region early is precisely how a field is hidden — the validator
  believes the `</div>` closed the hiding element, the browser knows it
  did not. Measured: `<div style="display:none">` above
  `Appendix prose <textarea>` above `</div>` above `</textarea>` renders
  the following field inside `div[style=display:none]`, and the record
  validated at **0 errors**. At v1.18 a raw-text element suppresses tag
  reading whether or not it opened a region]; the
  predicate still refuses a declaration carried inside any raw-HTML
  region the record opens at a line, whether or not it hides, because
  deciding *hiding* means evaluating CSS this instrument cannot
  evaluate; the two v1.14 clauses with no single-layer witness (tab
  expansion, the ≤3-column bound) remain so; blockquote laziness is
  still deliberately not implemented; §5's non-authority banner can
  still be satisfied by a quotation of itself in an appendix (RD42-12);
  the depth scan is still quadratic in nesting depth (RD42-13); an
  asymmetric `**Label:*` still satisfies presence; and the trend row is
  still printed above the error list carrying the record's *claimed*
  verdict when the record is invalid — all carried forward. Seven
  accepting-direction fixtures are broken by no revert and are named as
  what they are: documentation of a lawful shape, not a witness
  (RD44-08) [corrected 2026-08-11, RD45-09(a): **eleven**, measured over
  the whole population. Seven was RD-44's figure for v1.16's 26-fixture
  population, carried into this entry as a fact about v1.17 — a derived
  value quoted outside the measurement that owns it, which is
  verification rule 3's failure mode exactly]. Semantic delta:
  `round-2026-08e/LAUNCH-GATE-v1.17-SEMANTIC-DELTA.md` (which also
  carries the corrections of the frozen v1.16 delta's false claims, in
  the D-10 convention — the frozen record is not edited). No existing
  question weakened; no ID renumbered.
- **v1.18** (2026-08-11, post-RD-45 amendment — the v1.17 review's four
  BLOCKING, four MAJOR and one MINOR findings; candidate, owner approval
  pending) — a **validator-and-records batch** an eleventh time: no
  question block, no verdict word, and no section §1–§8 changed; the
  instrument bytes that move are this entry, the version header, and
  **six** dated correction markers in the v1.17 entry above (counted
  over that entry's span with a wrap-tolerant pattern, the method
  RD42-05 made necessary), whose region-and-set sentence, `textarea`
  residual, LG-6 claim, hiding-set clause, unwitnessed-fixture count and
  compressed error count were each false of the bytes an approval digest
  would have bound. RD-45 reproduced **all nine** v1.17 mutation
  denominators on its **first** reconstruction, verified §1–§8
  byte-identical at all eight counts across eleven versions, confirmed
  every changelog entry from v1.0 to v1.15 byte-identical and the v1.16
  entry byte-for-byte the frozen prose beneath its four markers,
  reconciled 205 + 83 = 288 by set difference with 0 dropped and 0
  renamed, and **rebuilt the uncommitted corpus sweep from the delta's
  prose alone**, reproducing every figure — the strongest records result
  this chain has produced, and the reviewer says so before anything
  else. **And the same question was answered inconsistently a ninth
  time, this round by the batch's own method.** v1.17 fixed the RULE — a
  mid-line tag opens a region only when it takes its content out of
  sight — and never measured the SET it ranges over. `<iframe>`,
  `<noframes>`, `<noembed>` and `<select>` are each unpainted mid-line;
  each laundered a `READY FOR <the verbatim target>` beneath a record
  whose last visible line read `GATE VERDICT: NOT READY`, at **0
  errors**; two of the four were refused at v1.16; and `iframe` is a
  name RD-44 had written down as correctly refused. The corpus could not
  tell, because **65 of the 83 new fixtures computed their expected
  direction — and their own titles — from the set under test**, so a
  wrong membership relabelled them instead of failing them. Beside that,
  three parser defects: a `>` inside a quoted attribute value ended the
  tag match, so `<div style="content:'>';display:none">` reached no
  hiding test at all (RD45-02, which defeated the whole of the widened
  hiding set rather than an edge of it); a `</div>` written inside a
  mid-line `<textarea>` closed the hiding `<div>` around it in the
  validator and not in the browser (RD45-04); and the split-tag rule,
  narrowed **without record**, reopened the mid-line carrier while
  refusing §5's own shorthand wrapped across two lines (RD45-01). **At
  v1.18 every enumeration in the predicate is generated against the
  render over a named population with a denominator, and no fixture
  takes its expected direction from the thing it is testing.** The
  mid-line hiding set is measured over **84 names** — CommonMark's
  condition-6 list ∪ the HTML5 raw-text and escapable-raw-text elements
  ∪ the HTML Standard's UA-stylesheet `display:none` set ∪ every element
  whose content model is fallback or non-painted content — rendered
  under both `-f gfm` and `-f commonmark` and parsed with `html5lib`,
  which agreed on all 84: **eight hide** (`details`, `iframe`,
  `noembed`, `noframes`, `script`, `select`, `style`, `title`), **69
  paint**, and **seven the measurement could not settle** (`basefont`,
  `datalist`, `dialog`, `head`, `noscript`, `rp`, `template`) are
  refused in the safe direction and **disclosed as unsettled rather than
  counted as measured** — this parser closes them at the following
  `</p>` while the UA stylesheet does not paint their content, and one
  of them (`dialog`) had its paragraph-closing behaviour changed in HTML
  after this parser was written. The tag scanner consumes quoted
  attribute values as the tokenizer does; a raw-text element suppresses
  tag reading **whether or not it opened a region**; an opening tag
  whose `>` arrives on a later line is continued from **either**
  position and cancelled by a blank line, then classified by the one
  rule; a region opened inside a markdown container **ends where that
  container ends** — a `<details>` named inside a blockquote or a list
  item no longer swallows the rest of the record, which was three
  over-refusals of twelve on the most likely lawful sentence in this
  corpus; the hiding test reads the **value** of `opacity` rather than
  one spelling of it; and LG-6 names the line that opened the region by
  carrying it on the region itself. **329 fixtures** (288 + 106 new
  names − 65 renamed, by set difference of printed names); **twelve**
  mutation-reverts, one per repair, each run **inside a repository**,
  breaking 1, 1, 5, 8, 1, 5, 2, 3, 1, 1, 2 and 1 fixtures — and one of
  the twelve was rebuilt after its first construction proved to be
  mutating only part of the set it named, which is the apparatus
  mutated before the finding, as RD-44 taught this chain to do.
  **Regression, by script** (the rule RD44-05 established): 282 records
  carried forward, 0 dropped, and **exactly five move**, every one of
  them named and deliberate — `iframe` and `noframes`, whose refusal is
  RD45-03's repair, and `basefont`, `dialog` and `head`, whose refusal
  is the disclosed safe direction. Of the 106 fixtures added, **24 are
  broken by at least one revert and 82 by none**: 73 of those 82 are the
  measured table's accepting entries, whose job is to document a lawful
  shape rather than to witness a repair, and the remaining 9 are second
  constructions of a repair another fixture already witnesses. Both
  counts are generated by the run. **Disclosed limits, each measured,
  none generalized:** the seven unsettled names above are an
  over-refusal in the safe direction, and a reviewer who writes one of
  them mid-sentence about this instrument is refused; the hiding
  attributes remain an enumeration, and a construction outside it is
  read as prose; the predicate still refuses a declaration carried
  inside any raw-HTML region the record opens at a line, whether or not
  it hides, because deciding *hiding* means evaluating CSS this
  instrument cannot evaluate; the two v1.14 clauses with no
  single-layer witness (tab expansion, the ≤3-column bound) remain so;
  blockquote laziness is still deliberately not implemented; §5's
  non-authority banner can still be satisfied by a quotation of itself
  in an appendix (RD42-12); the depth scan is still quadratic in nesting
  depth (RD42-13); an asymmetric `**Label:*` still satisfies presence;
  and the trend row is still printed above the error list carrying the
  record's *claimed* verdict when the record is invalid — all carried
  forward. Semantic delta:
  `round-2026-08e/LAUNCH-GATE-v1.18-SEMANTIC-DELTA.md` (which also
  carries the corrections of the frozen v1.17 delta's false claims —
  including the change of meaning it did not record at all — in the
  D-10 convention; the frozen record is not edited). No existing
  question weakened; no ID renumbered.

- **v2.0** (2026-08-11, structured-record migration — owner charter
  *"Syzygy — Structured Launch Gate, Owner-Decision Closure, and
  Capability 1 Readiness"*, §5) — **the administration record stops being
  Markdown.** The owner's direction was to stop the carrier-by-carrier
  repair loop rather than to run it once more: between v1.3 and v1.18 this
  file asked one Markdown document to be both a human report and a
  machine-validated source record, and thirteen consecutive administrations
  (RD-33 … RD-45) returned `REVISE`, the last five of them on one question
  — *is this line the record's own claim, or a quotation of one?* — that
  quotations, fences, comments, list items, continuations, raw HTML, hidden
  DOM regions, CSS visibility, tag populations and renderer disagreements
  each reopened. v2.0 removes the question instead of answering it again.
  **What changed:** §5 is replaced — the canonical record is JSON
  conforming to the new committed schema
  `launch-gate-administration.schema.json`, the Markdown report is
  generated from it by `scripts/render_launch_administration.py` and is
  never parsed back, and `scripts/validate_launch_administration.py`
  (checks `LA-1` … `LA-16`, each with at least one mutation fixture;
  the count is printed by `--selftest` and stated nowhere else) validates the
  record and
  **computes** the verdict; the preamble's three artifact classes become
  four, splitting record from report; §2 adds the integrity requirement
  that the record *is* the JSON and that an edited report is detectable by
  `--check`; §6's trend row is generated from the record rather than typed,
  and states the comparability limit across the format boundary; §7 adds
  the schema to the portable core. **What did not change:** every question
  ID and every question's text; the §4 formula, both pass branches, the
  five blocking conditions, the never-deferrable conjuncts, and the closed
  verdict vocabulary; §8's parameter block, byte for byte. **Three
  properties the new shape holds that the old could not:** a missing field
  is an error rather than a template line that reads as answered; `verdict`
  and `launch_scope` are separate typed fields that must agree, so
  laundering a defect out of scope takes two deliberate acts rather than
  one soft phrase; and `Deferred`/`Reopened` are array lengths, so an
  absent array errors and an empty one asserts zero, with no silent zero
  available (VIS-2 applied to the gate's own record). The record can no
  longer claim a verdict at all: the schema rejects a `final_verdict` key.
  **Historical records are not migrated** — the 2026-08-09 pilot and every
  Markdown administration remain immutable evidence in the format their
  version defined, and `scripts/launch_gate_results.py` (329 fixtures)
  stays in the repository to validate those and only those. **Disclosed
  limits, measured rather than asserted:** the validator reads the
  instrument's own §8 prose in exactly one place — binding E4's fixed cases
  — and that read is bounded (it stops at the first non-consecutive case
  number) and fail-closed (no cases parsed is an error, a count or text
  mismatch is an error), which is why it is disclosed here rather than
  claimed absent; the schema interpreter is a documented subset of JSON
  Schema and **rejects any keyword it does not implement**, so the schema
  cannot quietly rely on one that is ignored, but it is a subset and not
  the reference implementation (where `jsonschema` is installed the
  selftest cross-checks against it as a second method; hosted CI installs
  no packages, so that cross-check never gates anything); presence tests on
  free-text fields remain content-blind by design, guarded only against a
  placeholder lexicon, so the truthfulness of an evidence quote stays with
  the reader; and no administration has yet been performed under this
  version — v2.0 is a candidate whose approval is P-34. Semantic delta:
  `round-2026-08f/LAUNCH-GATE-v2.0-SEMANTIC-DELTA.md`. No existing question
  weakened; no ID renumbered; the formula is unchanged.
