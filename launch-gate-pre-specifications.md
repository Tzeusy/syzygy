# Launch Gate — Pre-Specification Readiness

```yaml
status: candidate process policy — owner approval pending, see
  .syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md
owner: the project owner (VIS-4 — no verdict here performs an owner act)
effective_version: v1.7 (candidate; v1.3 was the pilot-administered version)
governs: how pre-specification readiness is evaluated — the question set,
  administration protocol, verdict vocabulary, verdict formula, the
  launch-scope parameters (§8), results record format, and trend log
does_not_govern: whether specifications are authored (the owner's launch
  decision); the content of any artifact under judgment; any acceptance,
  adoption, or approval
amendment_process: semantic delta per NORMATIVE-CHANGE-WORKFLOW.md shape,
  changelog entry in §9, question IDs never renumbered or reused; owner
  approval required once this instrument is in force
canonical_result_home: .syzygy/governance/decisions/launch-gate/
  (administration records verbatim + TREND-LOG.md; the 2026-08-09 pilot
  record remains immutable at
  .syzygy/governance/contracts/candidates/round-2026-08d/reviews/)
```

**What this is.** A benchmark-style question series for judging whether a
vision-guided, spec-driven project is ready to begin authoring specifications.
It is administered to a fresh-context LLM reviewer (or a human) at each
synthesis↔review cycle, and its verdicts are the acceptance criteria for the
"begin specifications" decision.

**What this is not.** Not authority. Not doctrine. Not a contract. A process
instrument only — no verdict here adopts, accepts, or approves anything on the
owner's behalf. The owner reads the verdicts and decides.

**Three artifact classes, never conflated:**

```text
Launch-gate definition (this file)
    owner-approved process policy once in force
    governs how pre-specification readiness is evaluated

Administration record
    evidence produced by applying the policy at one named commit
    never adopts anything; stored verbatim; superseded, never edited

Owner launch decision
    authorizes or refuses specification authoring
    the only one of the three that is an act
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
  record quotes the instrument's sha256 and the parameter block's sha256.
- The record names the commit, and every citation is verified against it.
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
- Copy these verdict words exactly into the results record. Never translate
  a verdict into softer language. Questions are quoted verbatim at the
  version administered — a verdict rendered against a paraphrased question
  is void, and every operationalization judgment call is recorded.

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
`LAUNCH_TARGET`, `REQUIRED_WAVES`, `DEFERRED_WAVES`). The launch-gate rule:

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
>
> Every term of this formula is a predicate over the closed verdict
> vocabulary — nothing in it requires a word the rows may not contain.

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
error (LG-9), never a lawful record. The gate never requires internally
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
  `Owner deferral decision:` field names the owner decision (path or
  identifier) that granted it — a reviewer's own evidence-cell wording
  ("treated as owner-deferred") is not a deferral and satisfies nothing.
- **Any deferral-carrying pass is `READY-WITH-DEFERRALS`.** The F2 deferral
  limb of the formula — and any other owner deferral a pass rests on —
  changes the verdict word: plain `READY FOR <LAUNCH_TARGET>` over any
  deferral, or over a nonzero `Deferred count:`, is a contradiction and a
  validation error.
- **The `READY-WITH-DEFERRALS` predicate, stated as a formula** (RD34-01 —
  a verdict word with no predicate of its own is a branch a pass can ride
  through unchecked, and every term of this section's formulas is a
  predicate over the closed vocabulary):

  > **READY-WITH-DEFERRALS** =
  >     every conjunct of **READY FOR `<LAUNCH_TARGET>`** above —
  >     every E question `Met`; no plain `Not met` in launch-scope A–D;
  >     F1 `Met` or `Unknown`; F3 `Met`; F4 `Met` —
  >     with exactly one substitution: the F2 limb is satisfied by an
  >     **owner-cited deferral** (the `Owner deferral decision:` field)
  >     instead of `Met`,
  >     AND `Deferred count:` is nonzero AND the citation is present.

  The E, A–D, F1, F3 and F4 conjuncts are **never deferrable** — each
  carries this section's own rationale for blocking — so the two pass
  verdicts differ in exactly one limb, and the validator runs the full
  conjunct battery on both branches (LG-6/LG-7): plain `READY FOR`
  requires F2 `Met` and zero declared deferrals; `READY-WITH-DEFERRALS`
  requires the citation and the nonzero count, and fails on any non-F2
  conjunct exactly as a plain pass would.
- F5 and F6 are recorded and disclosed (§5's family line; the trend row)
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

## 5. Results record format

One record per administration:

```markdown
# Launch-gate administration — <date>, commit <sha>
> This administration record is evidence, never an owner act; its verdict
> authorizes nothing (instrument preamble; VIS-4).
Instrument version: <vX.Y>  sha256: <instrument digest at the named commit>
Parameter block sha256: <digest of §8 as bound for this administration>
Launch target: <LAUNCH_TARGET, verbatim from the parameter block>
Reviewer: <model/version or human, fresh context: yes/no>
Reviewer model family: <alternate families across administrations where possible;
  same-family administrations must say so here and in the trend row>
Materials given: <list, with deviations from the fixed list called out>
Operationalization notes: <every judgment call made interpreting a question>

| Q | Verdict | Evidence / counterexample (paths + quotes) |
|---|---------|--------------------------------------------|
| A1 | Met | ... |
| E1-form | Met | ... |
| E1-home | Met | ... |
| E1-granularity | Met | ... |
| E1-acceptance-authority | Met | ... |
| E1-change-process | Met | ... |
| E1 | Met | rollup — Met only when all five sub-rows are Met |
| ... | | |

## G1 — completeness critic
<G1 is recorded here as a section, never as a verdict row — it yields no
Met/Not-met verdict>

E3 reopen-list: <empty | enumerated items>
Deferred-wave findings recorded outside launch scope: <list | none>
Deferred count (owner-deferred findings this administration): <n>
Reopened count (previously recorded resolved, recurred): <n>
Owner deferral decision: <path or identifier of the owner decision granting
  every deferral this record carries — required whenever Deferred count is
  nonzero or the verdict is READY-WITH-DEFERRALS; omitted otherwise>
Unknowns and what would settle them: <list>
Reviewer's falsification notes: <what they tried to break and couldn't>
GATE VERDICT: READY FOR <LAUNCH_TARGET> | NOT READY |
  READY-WITH-DEFERRALS (owner only)
```

The terminal line's `GATE VERDICT:` token is literal — it is the line the
validator parses and the trend row carries; the `Deferred count:` and
`Reopened count:` fields are required, and their absence is a validation
error, never an implicit zero (VIS-2 applies to the gate's own record).
The template's `(owner only)` parenthetical is a description of who may
grant deferrals, never a satisfier: a `READY-WITH-DEFERRALS` verdict is
lawful only with the `Owner deferral decision:` field naming the granting
decision, and copying the template's own words meets no requirement
(LG-7). Of the trend row's figures, the Not-met, Scoped, and Unknown
counts are **computed from the rows**; Deferred and Reopened are
**declared required fields** the validator parses — declared, not
computed, which is exactly why their absence errors instead of reading
zero.

Store the record verbatim in the canonical result home. Never edit a past
administration; supersede it. `scripts/launch_gate_results.py` validates a
record — verdict vocabulary, counts, G1 presence, named commit, digests —
and generates the trend row; the instrument, not the tool, owns readiness
semantics. The validator also binds the **question roster**: a full
administration answers every question (A1–A6, B1–B5, C1–C7, D1–D4, E1 with
its five sub-rows, E2–E6, F1–F6, plus the G1 section), and a record
missing any row is a validation error (LG-10) — absence of a question is
never a pass, and a delta administration's record cannot support a gate
decision (§2's full-vs-delta rule, now checked rather than trusted).

---

## 6. Trend log

Append one line per administration to
`.syzygy/governance/decisions/launch-gate/TREND-LOG.md`; this is F1's
evidence.

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

Generalization rule: the [U] questions and the §2/§4 protocol are the
invariant; everything project-specific lives in the parameter block. If a
generalized version needs to edit a [U] question to fit a project, that is a
finding about the question — record it upstream, don't fork silently.

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
