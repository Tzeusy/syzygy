# Review - D8 doctrine amendment packet (Inferred first-class, P-102)
Reviewed commit: 59fbf78700d72b14d1551926c2b55b464c61aa5e
Package digest: 330e61136be78086f7ecf17418f417d54bbacbb11f7bac7d37782d57108a8746
Verdict: REVISE

Reviewer: fresh-context agent that did not draft the package (CC-REV-1),
round 1 under `REVIEW-BRIEF.md`. Date 2026-10-03.

## Method

- Cloned `/home/tze/GitHub/syzygy` and checked out the reviewed commit. The
  package digest above was computed at the clone's root with the brief's
  command: `sha256sum $(git ls-files <package dir> | LC_ALL=C sort) | sha256sum`
  (4 files: IMPACT-LEDGER.md, OWNER-DECISION-PACKET.md, REVIEW-BRIEF.md,
  SEMANTIC-DELTA.md).
- Added a second worktree at `6bb6ef26`, the commit the ledger's figures
  are pinned to, and re-ran the term sweep and the reader sweep there and at
  the reviewed commit.
- Read the governing references the brief names. To check composition
  (packet section 8) I fetched D7's packet from branch
  `agent/syzygy-u05.14`.
- Ran one rule-6-style probe in my scratch worktree: I applied insertion
  (d2) to `vision.md`, ran three derived-artifact checks, then restored the
  file. No other file was edited.

## What holds [Observed unless marked]

- All three doctrine sha256 values in packet section 1 and SEMANTIC-DELTA
  match the bytes at both `6bb6ef26` and the reviewed commit. The doctrine
  files are byte-identical between those two commits.
- Every anchor's quoted text and line range is exact:
  - trust-and-evidence.md 44–49, 95–96, 134–137 and 175–180;
  - vision.md 232–234;
  - architecture.md 23–25.
- These quotations are also exact at the line ranges given:
  - RFC1-14 (361–368), RFC1-16 (378–390) and the RFC1 deferral (1003–1004);
  - RFC4-26 (154–162), RFC7-2(c) (96–97) and RFC2-25 (168–189);
  - the POC CONTRACT-COVERAGE RFC4-26 row (line 119);
  - REQ-polaris-generation-031's "Attributed answers, presentation
    preferences and adopted intent SHALL remain distinct existing classes"
    and "Missing input/persistence consent SHALL preserve the limitation
    without silently retaining or using the answer" (amendment spec.md
    line 640);
  - P-71 Q3 ("Q3 arm (b), a pure drafter that writes no file", rulings
    file line 58);
  - P-74 Q3 (line 64) and P-76 Q2 (line 62);
  - A6 line 25 ("**The syzygy repository itself**; second: **butlers**",
    which the packet quotes without the bold markup);
  - the M4 funnel Q3 sentence;
  - N15's `why` and L2-F5's title.
- The term sweep reproduces exactly at `6bb6ef26`:
  - 1,540 files, 145 hit files and 405 occurrences;
  - every lane row matches the ledger table;
  - a `git grep -l -i -E` second method returns a set-equal 145
    (`comm -3` empty);
  - authority-lane line numbers (doctrine 14/38/54/75, decision and
    specification rows) match.
- The reader sweep reproduces: 421 files and 11 readers over the stated
  population.
- The digest sweep reproduces:
  - trust-and-evidence.md's and architecture.md's digests occur in no
    tracked file;
  - vision.md's occurs only in the three evidence files named.
- Applying (d2) moves VIS-7 from line 250 to line 256, which is the six
  lines the ledger states. DIRECTIVE-REGISTER.md has 0 rows naming
  trust-and-evidence.md or architecture.md.
- `05-CONTRACT-INDEX.yaml` lines 570, 572 and 574 are the three doctrine
  rows. trust-and-evidence.md's current `rule_ids` lack VIS-4, so clause
  (b)'s citation would add it.
- Composition (packet section 8):
  - D7 anchors vision.md 105–107 and architecture.md 329–334, and D3 edits
    the loop paragraph and the "Not autonomous" passage. D8's anchors are
    VIS-6 (vision.md 232–234) and architecture.md 23–25, so no bytes
    overlap.
  - Neither D3 nor D7 names trust-and-evidence.md as an insertion site.
  - The re-anchoring rule (packet section 8) is sound.
- The premise-check placement of (a) and (c) is right: no doctrine
  sentence forbids either. The blockers are PWB-REQ-012's closed roles, the
  undefined inference profile (RFC1 deferral, RFC1-16, RFC4-26) and the POC
  exclusion, as the packet says.
- Clause (b) against trust-and-evidence.md line 14: no contradiction.
  - Line 14 reads "Status rests on evidence; a recorded human decision and
    a work warrant authorize other acts, but neither is evidence".
  - Line 36 reads "Two acts are authorized by warrants that are *not*
    evidence".
  - Both enumerate warrants. (b)'s class is drafted as "neither evidence
    nor a warrant", so the warrant count stays two [Inferred]. See note 8
    for a structural wrinkle.
- Clause (d) and VIS-5: the destination `.syzygy/**` is an existing write
  root, and nothing is written into the observed project, so the write
  roots are not widened [Inferred]. P-71 Q3's ruling is stated correctly,
  and the packet says a first write still needs its own act.
- Clause (e) and the battery or launch-gate: the launch-gate record
  (`ADMINISTRATION-2026-08-18-CAPABILITY-1.json`, keys `question_results`,
  `reviewer`, `repository_commit`, …) is a reviewer administration, not an
  observation record. "Observation record" is a defined doctrine term
  (trust-and-evidence.md line 144: "the immutable result of one identified
  status evaluation"). So neither the battery nor a launch-gate
  administration falls under (e)'s literal text [Inferred]. Finding 4
  covers the scope risk that does exist.
- N15 departure for (b): the departure is honest and necessary. An LLM
  assertion is already Inferred (trust-and-evidence.md line 25), so
  "agent-produced answers" needs no doctrine. Note 6 covers a second,
  undisclosed departure.
- Acceptance criterion 4 holds: no doctrine byte, contract, specification
  or code is edited by the commit (4 files added, all inside the package
  directory, per `git show --stat`).

## Findings

### 1. Revise-level [Observed]: clause (f) collapses `unadopted-draft` into `editorial-draft`

The packet's section 2 maps (f) to "`unadopted-draft`, then presentation
(RFC7-4)". The clause text reads "an unadopted draft until a human adopts
it, and once adopted is presentation only, never a claim source". RFC2-25
(rendering-vocabularies.md lines 191–199) defines the two states by what
each becomes:

> an unadopted draft awaits an **adoption gate into authority**, and once
> through it, it binds and is citable. An editorial draft awaits a **human
> authorship act into a non-authoritative artifact**, and **stays
> non-citable even after that act completes** … Collapsing the two would
> misstate both directions at once

A draft that stays non-citable after adoption is RFC2-25's
`editorial-draft`, not `unadopted-draft`.

- Both the clause wording ("an unadopted draft") and the section 2 mapping
  are wrong.
- The "Clarifying" class claim ("RFC2-25's `unadopted-draft` and
  `editorial-draft` states … already say this") also does not hold as
  drafted.
- Even though (f) is recommended for decline, an owner who adopts it would
  adopt text that contradicts an accepted contract's distinction.
- Repair: use `editorial-draft` (or the state RFC7 assigns to presentation),
  and correct the section 2 row.

### 2. Revise-level [Observed quotes; Inferred reading]: clause (d)'s premise and no-change arm misplace the blocker

Packet section 0 says doctrine forbids (d) "**Yes, by omission**", on the
reading that "`architecture.md` defines a governed project by its writable
governance root". architecture.md does not say "writable":

- line 14: "A governed project has one governance root, where Syzygy
  writes only `openspec/**` and `.syzygy/**`". This is a confinement, not
  a requirement that the root be writable.
- lines 18–21: the definition requires a designated root and explicit
  observation.

The pursuit finding the packet cites as evidence locates the block
elsewhere (L2-F5 `detail`): "VIS-5 names `openspec/**` as a lawful
direct-write root, so doctrine does not forbid it in the abstract - but the
one registered adapter declares `"writeSurface": []` … and the 2026-09-02
act bounds it". The rulings file's P-71-Q5 row (line 59) already names the
non-doctrine path: "(1) a dated owner act naming the write, (2) a
registry-entry amendment act taking `writeSurface` from empty to the named
path". So:

- The no-change arm, "promotion, dismissal and persisted answers about
  Butlers stay dead-ended", is overstated. Without (d), an act route into
  the observed project's own plane exists in principle (whether the owner
  wants it is a separate question).
- The premise row should say that the binding blocker today is the
  registry entry and the 2026-09-02 act. Clause (d) is an alternative
  destination that avoids writing into the observed project; it is not the
  only lawful route.
- The packet also neither cites nor reconciles the architecture.md
  Definitions entry. "**Project** — one or more repositories with one
  owner and exactly one designated governance root … These meanings change
  only by doctrine amendment" (lines 210–216). An "observed-only project"
  is named a project without saying whether it has a designated governance
  root. The brief lists the Definitions as a governing reference.

### 3. Revise-level [Observed; Inferred]: clause (e) is not fully shown representable

Acceptance criterion 2 is not met for (e), for two reasons.

- **(i) "Render as self-observed" is unmapped.** The clause requires the
  records to "render as self-observed". Section 2 maps (e) to "Observed, at
  its ordinary tier" with "ordinary" freshness, and maps no label, tier,
  reason, freshness value or sibling state to "self-observed". The packet
  should say where it lives (for example, as provenance disclosed as a fact
  of the render). Otherwise it reads as an unstated tier-like qualifier
  next to RFC2-25's closed set ("No new tier without an amendment to this
  RFC").
- **(ii) The cited rule is not the one that licenses the restriction.** The
  restriction "a claim *about Syzygy itself* is restricted below
  `gate-backed`" cites RFC2-25's "A tier … may only *restrict* its parent
  label's authority". That sentence governs a tier relative to its label,
  not a subject-based ban on assigning a tier. RFC2-25 also defines no
  ordering among tiers, so "below" has no referent.
- The intended effect is representable: such claims are never assigned
  `gate-backed`, which RFC2-25 makes "The **only** tier that may support a
  positive status claim". It should be stated that way and grounded in the
  clause itself (a doctrine rule), not in the RFC2-25 sentence quoted.

### 4. Revise-level [Inferred]: clause (e)'s "never satisfy this floor" is broader than the packet's stated intent

The stated intent is that the observatory never self-certifies (aligned,
converged, genome-complete). The text also says the records "never satisfy
this floor". The floor's first two bullets are properties of the pipeline:

- observation-record determinism across runs of one evaluation;
- internal-link resolution.

Evidence that these hold may lawfully come from running the pipeline over
some repository. A6 names "The syzygy repository itself" as the first
proving project. Under the clause as drafted, a determinism or
link-resolution run whose subject is Syzygy's own repository could not
count toward the release-blocking floor. "Satisfy" is also ambiguous: it
could mean "cannot be evidence the floor holds", or that such records are
outside the floor.

- The trigger phrase "observes its own repository as an observed project"
  uses a term doctrine does not define. It is neither (d)'s "observed-only
  project" nor architecture.md's "observed-source repository", and
  Syzygy's own repository is a governance root.
- The scope statement that keeps the battery and launch-gate out sits in
  the packet, not in the inserted bytes. Only the defined term
  "observation records" does that work (see "What holds").
- Repair: confine the denial to claims about Syzygy's own conformance or
  status (alignment, convergence, genome-completeness, the release
  verdict), name the trigger with a defined term, and say whether
  pipeline-property evidence over the Syzygy tree may count.

### 5. Revise-level [Observed]: the ledger's derived-artifact sweep misses doctrine readers, and applying D8 breaks a battery check the ledger does not name

The section 4 reader sweep covers only `apps/`, `packages/` and `scripts/`.
Tracked readers under `.syzygy/governance/contracts/candidates/scripts/`
fall outside it:

- `build_budget_report.py`, `context_load.py`, `build_task_router.py` and
  `build_capability_1_views.py`;
- `build_contract_index.py`, whose output the ledger does list.

A sweep of all tracked `.ts/.py/.js/.mjs/.yaml/.yml/.sh` files outside the
original three roots (25 files) finds 8 doctrine-path readers. In my scratch
worktree at `6bb6ef26`, applying insertion (d2) alone to vision.md gave:

- `build_budget_report.py --check` reported "DRIFT:
  context-selection-6-doctrine-amendment.md — anchored measurement is
  stale", the same for `context-selection-8-openspec-authoring.md`, and
  "DRIFT: CONTEXT-BUDGET-REPORT.md — differs from regeneration". The
  fixtures load `doctrine:vision.md` (5 fixtures),
  `doctrine:architecture.md` (3) and `doctrine:trust-and-evidence.md` (1).
- `build_directive_register.py --check` and `build_contract_index.py
  --check` also drifted, as the ledger predicts. I then restored the file.

Packet section 9 step 3 regenerates only "the derived indexes
`IMPACT-LEDGER.md` §4 names", so the context-budget report and the
fixture anchor files are missing from the application recipe and the blast
radius (acceptance criterion 1). Repair: widen the reader population, add
the context-budget report and the fixture anchors, and re-derive the
count.

### 6. Note [Observed]: (b) departs from L3-M7's rendering without saying so

L3-M7, the move the packet says (b) drafts, reads: "Rendered, it is never
Observed and never Inferred: it is attributed …".

- Clause (b) renders it "Observed as a fact about the record" (`report-fact`).
- The departure is necessary under the three-label rule (L3-M7's form would
  be a fourth label), but packet section 0 discloses only the N15 wording
  departure and the VIS-6-exception alternative.
- L3-M7 also proposes the answer as "the honest filler for a first-reading
  Unknown". The packet should say whether (b) permits that or forbids it,
  since (a) forbids a synthesis to fill an Unknown.

### 7. Note [Observed]: (b)'s no-change arm overstates what the specification permits

The no-change arm says "the generator may ask and use an answer within one
run and must not retain it". REQ-polaris-generation-031 (amendment spec.md
line 508, its record-shape requirement) says "Clarification persistence and draft use SHALL require
applicable input classification, content consent and retention". Its
consent sentence (line 640) bars silently "retaining or using" the answer.
Use within a run is therefore also consent-gated; the arm should say so.

### 8. Note [Inferred]: (b)'s example and its placement

- **The example blurs a line the specification keeps.** "which of two
  sources governs" looks like adjudicating a contradiction. RFC2-24 reason
  #8 `contradicted-pending-adjudication` routes to "Owner adjudication", and
  REQ-031 lists "contradiction or interpretation dispositions" separately
  from "attributed answer revisions". The packet should say whether such an
  answer is, or can become, an adjudication.
- **The section's opening sentence no longer covers the section.** The
  answer-first opening (line 14) and the heading "Evidence, and the two
  other warrants" will not mention the third class (b) adds beneath them.
  This is not a contradiction.

### 9. Note [Inferred]: (c)'s change class

(c) is classed "Clarifying", yet the packet says it "extends the word from
capability↔code to any cross-surface subject". RFC1-16 and RFC4-26 bound
class (ii) to capability↔code only, so applying challenge-only authority to
new subjects is a normative narrowing over a wider domain. It is not a
restatement.

### 10. Note [Observed]: the PWB coverage-part row is narrower than described

`contract-coverage-parts/RFC-0007-0009.md` line 35 is the RFC7-2 row
"Non-factual framing is machine-marked non-normative". It records **Unknown
uncovered** because "its closed roles contain no `non-normative` standing".
That is RFC7-2(b) alone, not "RFC7-2's three-way classification" as packet
section 0 and ledger section 3.3 say. Whether `project-fact` may carry
Inferred is the drafter's inference, and should be labelled that way.

### 11. Note [Observed]: the section 4 reader table enumerates 12 readers against a stated 11

The table lists `self-corpus.ts` "(and test)" and also "five tests". The
tracked test readers are `git-blob-batch.test.ts`, `self-corpus.test.ts`,
`req-023`, `req-061` and `req-integration`, so the self-corpus test is
counted twice. `build_contract_index.py` appears as a row's builder but is
not one of the 11 (see finding 5).

### 12. Note [Observed]: the ledger's figures predate the reviewed commit

The ledger pins its figures to `6bb6ef26`, which is two commits behind the
reviewed commit; the ledger states this. At `59fbf787`, with the package
excluded, the same predicate gives 1,554 files, 147 hit files and 407
occurrences. The two new hits are:

- `PENDING-OWNER-DECISIONS.md` line 1042 ("Q5: the copy roles of the new
  strings", the PWB opening-index amendment). This hit is undispositioned
  and touches the copy-role mechanism behind Q-S1.
- `pwb-opening-index-amendment/ROUND-1-DISPOSITIONS.md`.

Neither falsifies a clause.

### 13. Note [Observed]: register row and decision basis

- Register row P-102, which packet section 9 says "closes with the
  outcome", does not exist at the reviewed commit. The register's highest
  row is P-100, and P-101 exists only on D7's branch. Say who adds it and
  when.
- SEMANTIC-DELTA's evidence basis cites P-75 Q4 ("`Inferred` added as a
  typed landing zone with no production constructor"), but the packet never
  uses it. It bears directly on N15's "unconstructible by any module" and on
  section 2's representability claim.

### 14. Note [Inferred]: clause (a) wording

- "Names the exact claims it composes over" sits beside "anchors nothing".
  Under RFC7-9 and RFC7-10, naming claims may be implemented as anchors.
  Say "is not an anchored claim (RFC7-2(a))" if that is what is meant.
- In section 2, (a)'s freshness cell says "stale or withdrawn". "Withdrawn"
  is not one of RFC2-10's four values. A `broken` or `superseded` input also
  needs its mapping stated.
- The (a)/(f) overlap for a generated manifesto stays [Unknown], as the
  ledger honestly records. The "surface composes" scope does not settle it.

### 15. Note [Inferred]: clause (d)'s destination phrase

- "The governance root the owner runs Syzygy from" is not a doctrine term.
  Doctrine knows only each governed project's own root.
- Records one project holds about another touch RFC1's deferral
  "Cross-project relationship semantics → portfolio profile (SDR-30)". SDR-30
  says cross-project semantic relationships "render **unconfirmed/asymmetric**".
- Neither the packet nor the ledger considers this deferral. Whether (d)
  needs that profile is an owner question the packet should route.

## Summary

- Revise-level findings: 5 (findings 1–5).
- Notes: 10 (findings 6–15).
- All quotations, anchors, line numbers and digests I checked are exact.
- The term sweep reproduces and is set-equal.
- The premise check is right for (a) and (c).
- Clause (f) is mapped to the wrong sibling state (finding 1).
- Clause (d)'s doctrine-gap premise overstates the block (finding 2).
- Clause (e) is under-specified in rendering and scope (findings 3 and 4).
- The derived-artifact sweep misses a battery-checked report that
  application would break (finding 5).
