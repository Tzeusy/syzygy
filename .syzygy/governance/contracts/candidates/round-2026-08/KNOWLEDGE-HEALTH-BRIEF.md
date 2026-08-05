# Knowledge Health — capability brief

**Status: candidate brief. Binds nothing.** It creates no OpenSpec changeset,
proposes no runtime, chooses no stack, and is not a specification. Charter
§16 asks for a reviewed brief for a *future* shared observer; this is that,
and no more.

**Two things ran, and the difference matters.** `scripts/check_governance.py`
in this repository implements part of the detection list over this corpus.
An earlier prototype from the knowledge-refactor pass implemented a different
part; its working notes are founder-local under the git-excluded
`_bootstrap/knowledge-refactor/` and are **unavailable in a clone** — cited
here as history, never as evidence a reader can check. Where this brief says
*prototyped*, something ran and its output can be reproduced by running the
tracked script. Where it says *unbuilt*, nothing has been demonstrated.

---

## 1. What the capability is

A **Knowledge Health observer**: a deterministic checker over a project's
governed knowledge — doctrine, contracts, specifications, policies, decisions,
and the derived navigation over them — reporting defects in the same epistemic
vocabulary the product uses about everything else.

It holds **challenge authority only**. It may suspend confidence in a claim;
it may never establish one. It is the Inferred plane's rule turned on the
project's own documents.

## 2. Detections

Sixteen classes, from charter §16. **3 prototyped, 5 partial, 8 unbuilt** —
counted from the table, not estimated.

| # | Detection | State | What exists / what it needs |
|---|---|---|---|
| 1 | Dangling internal links | **Prototyped** | `CG-1a/1b`: markdown links *and* code-span path references, with declared forward-reference and frozen-packet classes |
| 2 | Orphaned requirements or clauses | **Prototyped** | Clause-ID continuity over a defining file; already enforced by `.syzygy/governance/contracts/candidates/scripts/verify_final_prespec.py` |
| 3 | Context-budget violations | **Prototyped** | `CG-8` reports §11.4 triggers; the package verifier enforces its own module ceiling with declared justifications |
| 4 | Duplicate normative claims | **Partial** | `CG-9` finds duplicate authority *homes*; byte-comparison of known duplicate surfaces was prototyped. Claim-level duplication across differently-worded clauses is unbuilt |
| 5 | References to superseded decisions | **Partial** | `CG-2a` catches one hand-named instance (the retired acceptance phrase). The general form needs a machine-readable supersession register; none exists |
| 6 | Historical material in active context | **Partial** | `CG-3`, `CG-12`, `CG-1d` catch routing to and citation of the excluded bootstrap tree. Lane assignment for every artifact does not exist, so coverage is by pattern, not by manifest |
| 7 | Hidden active authority | **Partial** | `CG-6` (accepted homes must not exist before an act), `CG-9`, `CG-12`. Does not detect authority hidden *inside* a permitted home |
| 8 | Current-state prose past its revision | **Partial** | Declared-count-versus-table checking was prototyped; `CG-10` surfaces the pending register's as-of line for human judgement. **Prose self-counts are not caught** |
| 9 | Undefined terms | **Unbuilt** | Needs a sweep for normatively-used terms absent from the term registry. Newly feasible once this round's registry candidate settles |
| 10 | Duplicate definitions | **Unbuilt** | Requires semantic comparison, not string matching |
| 11 | Conflicting definitions | **Unbuilt** | Same; the hard case is a word used as both a state plane and an epistemic label |
| 12 | Deprecated synonyms | **Unbuilt** | Needs the registry's deprecated-synonym column populated and stable |
| 13 | Summary/source divergence | **Unbuilt** | Needs a declared source-link per derived artifact |
| 14 | Stale evidence | **Unbuilt** | Needs evidence currency bounds; no evidence store exists |
| 15 | Missing fresh-reader review | **Unbuilt** | Needs review records as data, not prose |
| 16 | Agent-authored claims without source or warrant | **Unbuilt** | The hardest: provenance on *claims*, not files |

**The unbuilt eight are not future work of equal weight.** 9–13 need a data
structure that does not exist yet. 14–16 need the product itself.

## 3. Output vocabulary

Four classes, matching the project's own epistemics.

| Output | Meaning |
|---|---|
| **Observed issue** | A defect demonstrated against current content, with artifact, location, and the check that found it |
| **Inferred concern** | A pattern suggesting a defect, not demonstrated. **Never blocks** |
| **Unknown coverage** | The check could not run — inputs unreachable, corpus absent, declared exclusion. **Reported, never silently omitted** |
| **Suggested remediation** | A proposal a human or a governed change process may act on. **Never self-applying** |

**Unknown is the load-bearing class.** The prototype's most instructive bug
turned unreachable inputs into dozens of reported defects — missing evidence
rendered as findings, the mirror image of green-by-default. Any
implementation inherits that failure mode. If the class is absent from the
vocabulary, missing evidence will be reported as something it is not.

## 4. Non-negotiable properties

1. **It never rewrites a normative artifact.** Not a banner, not a link, not a
   digest, not "obviously safe" whitespace. It reports; a human changes the
   artifact under the normative-change workflow. An observer that edits its
   own subject destroys the evidence that it was ever wrong.
2. **Every PASS states its denominator.** A check that examined zero items
   reports Unknown, never success. *(A green "all relative links resolve" over
   a corpus with zero parsed links produced a false published claim once.)*
3. **Every PASS states the class it covered.** "All 13 links resolve" was
   true, reassuring, and about the wrong population while the defect sat in an
   unparsed syntax.
4. **A new check's first non-empty result is a hypothesis about the checker**
   until one hit is confirmed at source. Three prototype checks produced 9, 56
   and 91 phantom findings on first run; all three were checker bugs.
5. **Declared exclusions and allowlists are counted and printed**, never
   silent. A silent exemption is indistinguishable from a missing check.
6. **Deterministic.** Same corpus, same result.
7. **It must be able to fail on demand.** A check never shown failing has not
   been shown to work.

## 5. What this brief does not establish

- **It is not a specification.** No requirements, no acceptance criteria, no
  interface, no schedule.
- **Nothing here has been validated against a corpus that is not this
  project's own.** Every threshold and heuristic is calibrated to a
  documentation-only repository with no code.
- **The hardest detection is the one nothing addresses.** #16 —
  agent-authored claims without a warrant — is the failure this project keeps
  hitting, and neither the tracked checker nor this brief proposes a mechanism
  for it. Every instance so far was caught by a human reading or by a
  derivation run after the claim was written. Stated plainly rather than
  listed as future work of equal weight: **the defect class that most
  motivates this capability is the one it currently cannot detect.**

## 6. Routing

| Material | Home | Why |
|---|---|---|
| What the observer *displays* — reports, drill-down, dashboards, any user-visible behaviour | **Future OpenSpec** (`spec/knowledge-health`, a provisional routing name only) | User-observable behaviour is OpenSpec's, and OpenSpec does not exist yet |
| The obligation to run checks before claiming a corpus clean | craft-and-care | An engineering-and-evidence obligation, not a feature |
| Detections needing new data structures (9–13) | Blocked on those structures | Not schedulable as behaviour yet |
| Detections needing runtime evidence (14–16) | Blocked on the product | — |

**No changeset is created and no domain is scaffolded here.** When OpenSpec
exists, every user-visible consequence of this capability — what a report
shows, what a drill-down opens, what an operator can suppress — becomes an
OpenSpec requirement first and code second. Nothing in this brief may be
scheduled as implementation on its own authority.
