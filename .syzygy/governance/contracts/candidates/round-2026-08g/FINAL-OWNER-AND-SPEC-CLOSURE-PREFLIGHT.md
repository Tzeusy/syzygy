# Preflight — owner-decision, launch-policy and specification-discipline closure

> **Measurement, not decision.** This file records the verified starting
> state of round-2026-08g at the commit named below. It accepts nothing,
> approves nothing, and rules nothing. Every figure here was produced by
> running the named command in this session; nothing is transcribed from a
> prior report.
>
> Written to satisfy the owner charter's §1. Where the charter's own snapshot
> and this measurement disagree, **this measurement governs** — the charter
> says so itself.

## 1. Branch, HEAD, working tree

```text
branch        main
HEAD          f7ba735ee9acaadeb1c56107712a77d7c8c1072f
subject       "The reviews arrived, and three documents did not hear about it"
working tree  clean, except one untracked file (below)
```

`[Observed]` — `git rev-parse HEAD`, `git status --porcelain`.

**The charter's snapshot is current, not stale.** It names `f7ba735` and the
repository is at `f7ba735`. None of the charter's §1 escape clauses ("if the
repository has advanced") fires. Every posture bullet in charter §1 was
re-verified independently below and **all fourteen hold**.

The one untracked file is the owner charter itself,
`syzygy_fable_opus_owner_spec_launch_closure_prompt.md`. It is an owner
instruction, not a repository artifact, and is not committed.

### 1a. The charter file turns the battery red, and that is a real finding

`check_governance.py` CG-1b sweeps **every** `.md` in the working tree,
including untracked ones. The charter contains the code span
`decisions/README.md`, a file the charter itself asks this pass to create. So:

```text
with the charter present    30 OK, 18 WARN, 1 FAIL (48 checks)
with it moved aside          30 OK, 18 WARN, 0 FAIL (48 checks)
```

`[Observed]` — both runs performed this session; the file was moved to a
scratch directory and moved back, and `git status` confirms it is restored.

The corpus is clean. But "the battery is green" is currently a claim about
**the working tree**, not about the committed corpus — a reader with any
untracked scratch note containing an unresolvable path string gets a red
battery and no way to tell it apart from a corpus defect. Recorded as finding
**G-1** below. It self-resolves for this particular path once §11.3's
`decisions/README.md` exists, which is not the same as being fixed.

## 2. The battery, run in full this session

```text
check_governance                          30 OK, 18 WARN, 0 FAIL (48 checks)
verify_final_prespec                      PASS — all checks clean
build_contract_index --check              no drift — 11 contracts, 39/39 modules with a front-matter id, 367 clauses
build_dependency_index --check            no drift — 176 authored depends_on edges, 8 constrains edges
build_budget_report --check               fixture anchors and the generated report match regeneration
build_active_manifest --check             all 7 manifests match regeneration — 39 modules in 6 waves
build_task_router --check                 no drift — 13 task classes validated
build_task_router --selftest               11 fixtures, 0 failing
check_governance --selftest               125 fixtures, 0 failing
launch_gate_results --selftest            329 fixtures, 0 failing
validate_launch_administration --selftest  75 fixtures, 0 failing
render_launch_administration --selftest    12 fixtures, 0 failing
```

**552 fixtures, 0 failing** — 125 + 329 + 75 + 12 + 11, summed here and
belonging to no other document.

`[Observed]`, local working tree, CPython 3.10.12. This is **not** clean-clone
evidence and must not be quoted as such; see §11.

`--selftest` covers the families that have a fixture. CG-24 computes the
coverage figure itself and it is the only one to quote:

```text
18 of 25 check families have at least one fixture
no --selftest fixture: CG-3, CG-5, CG-6, CG-9, CG-10, CG-11, CG-12
```

## 3. Wave A and Wave B — digests and verdicts

| | Argument (`sha256` of the wave manifest) | Review | Verdict, copied exactly |
|---|---|---|---|
| Wave A | `8972d9630b95f5d4266432dbb1b3602114576bbd6c0f29d6f9bd6f905b1f884a` | RD-31b | `VERDICT: CONFIRM` |
| Wave B | `193e3c1e15e4b1375f938d62c9e8c1a442984313e0794ada5965d2cdf9d7e3ed` | RD-32c | `VERDICT: CONFIRM` |

`[Observed]` — `sha256sum` over `wave-manifests/WAVE-A-MANIFEST.txt` and
`WAVE-B-MANIFEST.txt` this session. Both match the arguments the acceptance
record's §1 names and the two reviews confirm.

**Neither act has been performed.** `decisions/ACCEPTANCE-ACT-RECORD.md` does
not exist, and that absence is correct. Wave A's offer is withheld **solely by
P-33**; Wave B is withheld by nothing except its own ordering behind Wave A.

The four deferred manifests also digest cleanly (C1 `a5d3ba1f…`, C2
`acd27bb8…`, D1 `570e6170…`, D2 `ab590e3e…`); they are recorded here only so
the population is 6 of 6, not 2 of 6.

## 4. The eight round-08f reviews — all obtained, verdicts copied exactly

| Review | Subject | Verdict |
|---|---|---|
| RD-47 | launch-gate schema, validator, renderer | `REVISE` |
| RD-48 | launch-gate policy semantics, v2.0 | `REVISE` |
| RD-49 | P-33 install shape | `REVISE` |
| RD-50 | default human path | `CONFIRM WITH EXCEPTIONS` |
| RD-51 | specification acceptance + shape-to-spec impact | `REVISE` |
| RD-52 | owner packet, one-sitting model | `REVISE` |
| RD-53 | Capability 1 task route | `REVISE` |

`[Observed]` — each verdict read from its own raw file in
`round-2026-08f/reviews/`. Seven `REVISE`, one `CONFIRM WITH EXCEPTIONS`.
This reproduces the charter's §1 list exactly.

All eight are **same-model-family as the corpus authors**. Under the charter
each supports repair and **none is the formal launch administration**.

## 5. P-33 — current packet and recommendation

```text
packet     decisions/WAVE-A-INSTALL-SHAPE-DECISION.md          1,575 words
analysis   round-2026-08f/P33-SEMANTIC-INSTALL-ANALYSIS.md
```

Current recommendations: **(1e)** typed closed enumeration for Q1, **(2b)**
generator-written banner for Q2 — both `[Inferred]`.

RD-49 returned `REVISE` with **thirteen findings**, three marked BLOCKING.
Their state entering this round:

| Finding | State |
|---|---|
| 1 — arm space omits the cheapest lawful arm | **repaired** — (1g) added with its 87-string cost |
| 2 — headline claim false and propagated | **repaired** — corrected at four sites |
| 3 — (1e) and (2b) are mutually inconsistent | **open** — BLOCKING |
| 4 — RFC3-15's cell never quoted; paraphrase softens the breach | **open** |
| 5 — the RFC3-15(a) objection is applied to (1b), withheld from (1e) | **open** |
| 6 — the relocate⇒rewrite coupling is unargued | **open** |
| 7 — two artifacts an owner must read carry the withdrawn recommendation | **open** |
| 8 — Q2's arm space incomplete; (2b) presumes absent machinery | **open** |
| 9–13 — labelling, "links" overstatement, missing (1f) row, understated (1d), packet unruleable alone | **open** |

`[Observed]` for the repair state of 1 and 2 (both visible in the current
bytes); `[Observed]` for the rest being absent from those bytes.

**A blocking finding is open, so P-33 is not decision-ready today.** RD-49's
section G answers the charter's own question directly: *could an owner rule
from this packet alone?* — **"No."**

## 6. Launch gate — current version and bound bytes

```text
version    v2.0, candidate. P-34 ungranted; no administration has been run under it
record     structured JSON; the Markdown report is generated and never parsed back
```

| Artifact | sha256 |
|---|---|
| `launch-gate-pre-specifications.md` | `05ecaa954e81ef95f6e2e2b409fbcb5bd5391037c10d9624ab4af3217a00f6d2` |
| `launch-gate-administration.schema.json` | `e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb` |
| `scripts/validate_launch_administration.py` | `d6b203f7c276aa4e58e0b1d0bb4d4cf947158dea34255370a2683bc981e0c745` |
| `scripts/render_launch_administration.py` | `9f90fa6ad6f6feaed175b78fe9e0901a2e3279586ffbf73b7854ead6140f9ed3` |

`[Observed]` this session. All four match the digests the sealed formal packet
binds, so **the sealed packet is not stale**.

The only administration on record remains the 2026-08-09 pilot, `GATE VERDICT:
NOT READY`. No administration has ever been performed under v2.0.

## 7. RD-47 and RD-48 dispositions

**Both are recorded, and both are unrepaired.** The disposition register
carries them; the P-34 owner packet and the sealed formal packet both now
disclose the two `REVISE` verdicts rather than claiming the reviews were never
obtained.

The material findings that must move before v2.1 can freeze:

1. The **computed formula carries a sixth core conjunct §4 does not state**
   (RD-48 finding 2) — a strengthening, grounded in §3's E3 rule, but not a
   term the instrument carries.
2. **`NOT READY` has no home in §1–§8** although the tool emits it (RD-48).
   All nine occurrences fall at line ≥ 889, inside §9, which is history.
3. **The schema audit never requires an object schema to close** (RD-47), so
   deleting one `additionalProperties` re-opens the claimed-verdict route the
   whole v2.0 design rests on.
4. §4 still names record fields no v2.0 record has, and §5 delegates the
   validator enumeration to a Python docstring.

`[Observed]` — read from the two raw review files this session.

## 8. Owner-decision queue

```text
decisions/PENDING-OWNER-DECISIONS.md      7,181 words
  open section                            5,525 words, 31 rows
distinct P-identifiers in the file        42
```

`[Observed]` — counted this session by parsing the file's own section
boundaries, not by a file-wide row grep (a file-wide grep accepts rows under
`Resolved…`, which is the trap the repository's own notes record).

The 31 open rows are P-10, P-12, P-14 … P-42, including both P-25 and
**P-25(c)**, which are two distinct questions rather than a duplicated row —
checked, because a duplicate identifier would be a defect.

> **These figures are as-of this preflight's run and are now stale.** The
> queue has grown twice since: **P-43** (2026-08-13, RD-56 f5) and **P-44**
> (2026-08-13, RD-51 f1). Recounted 2026-08-13 by the same method —
> **7,684 words in the file; open section 6,028 words, 32 rows; 44 distinct
> P-identifiers.** The measurement above is left unedited because it is what
> the charter's §8 finding was made against; `PENDING-OWNER-DECISIONS.md`
> owns the current count, and `decisions/README.md` restates it.

The charter's §8 finding stands on these numbers: a 7,181-word queue mixing
rulable questions, unperformed research, unpassed reviews and future acts is
not a thing an owner can work through in one sitting, and RD-52 said so.

## 9. Default reading path

```text
README.md                    966 words
PROJECT-STATUS.md          1,110 words
AGENTS.md                  2,451 words   — over its declared band; see below
```

Missing entirely, and required by charter §11:

```text
PROCESS-GLOSSARY.md                        does not exist
.syzygy/governance/decisions/README.md     does not exist
```

`.syzygy/governance/doctrine/v1.md` **does exist** and is not linked from
README's Start Here (charter §11.1).

`AGENTS.md` carries a `# Notes to self` section added on 2026-08-11. Charter
§11.5 directs it back to `PROCESS-LESSONS.md`; that is an explicit owner
direction and this round performs it.

## 10. Specification-acceptance and shape-to-spec impact — current bytes

| Candidate | sha256 | Words |
|---|---|---|
| `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` | `e66609bc37caccd48620b0d6c05416170a8280e1de0d9dc7ebc45fcca6162857` | 817 |
| `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` | `4d030dbc48632b972b1d6c7d00b1d984ca49a110925f9f8c592bae1c5aa16dd5` | 978 |

Both are candidates. Neither is in force. RD-51 reviewed them together and
returned `REVISE`. Queued as **P-41** and **P-42**.

**The blind propagation fixture has never been administered.** The charter's
§9.7 asks for one; §17 makes "the propagation fixture passes" a readiness
conjunct. `[Unknown]` — not failing, never run.

## 11. Hosted CI and clean-clone evidence

**Hosted CI is green at the exact current commit.** `[Observed]` — read from
the run, not inferred from the presence of a workflow file:

```text
workflow    governance-docs
run         31498509158
head        f7ba735
conclusion  success
```

**Clean-clone evidence is stale.** The current report
(`round-2026-08f/FINAL-PUBLIC-CLONE-REPORT.md`) names commit `5e8b286`, three
commits behind HEAD, and a clone report is valid only for the commit it was
run at. Its fixture total (546) is also superseded by today's 552. A fresh
clone at this round's final commit is owed under charter §13.

That report additionally states *"Zero were obtained"* of the eight
commissioned reviews. That was true when written and is **false now** — all
eight were obtained on 2026-08-11. Recorded as finding **G-3**.

### 11a. The published battery and the hosted battery are not the same list

`PROJECT-STATUS.md` states, of its own verification block:

> The fourteen checks above are the same fourteen the hosted workflow runs.

**That sentence is false in three separate ways**, measured this session by
parsing both files and taking the set difference:

```text
commands in PROJECT-STATUS's block   13      (not fourteen)
steps in the hosted workflow         14
shared by both                       12

in PROJECT-STATUS only   git tag --list 'doctrine-*'
in hosted only           validate_launch_administration …/DRY-RUN-ADMINISTRATION.json
                         render_launch_administration  …/DRY-RUN-ADMINISTRATION.json --check
```

`[Observed]`. The sentence exists precisely to stop a reader conflating "the
battery is clean" with "hosted CI is green", and it is itself the conflation:
a reader who runs the published block runs **twelve** of the hosted fourteen
and never exercises the dry-run administration record at all.

`AGENTS.md` inherits the defect. Its 2026-08-11 sentence — *"the hosted
workflow must run exactly that list"* — states a requirement that is currently
violated, which is worse than silence because it reads as an assurance.

Recorded as finding **G-2**, and repaired under charter §13 this round.

## 12. Capability 1 — route and source population

Launch target and wave scope are unchanged and re-verified:

```text
target          Capability 1 — Project registration and honest shape visibility
required waves  A, B
deferred        C1, C2, D1, D2 — candidate, not accepted, not used, excluded from routing
```

The Capability 1 route lives in the generated `TASK-ROUTER.md`, built by
`build_task_router.py` and drift-checked in the battery. Its facet sweep is
recorded honestly in the generated text: the facet vocabulary *"appears in 0
of"* the 30 modules the Waves A+B manifests name, and P-37 decides whether the
Capability 1 specification owns it or Wave A must be amended.

**The route and `FIRST-OPENSPEC-SEQUENCE.md` are independently maintained.**
The router is generated; the sequence is hand-authored; nothing checks that
their prerequisite lists agree. That is charter §10's finding and RD-53's, and
no single source exists for them to be generated from. `[Observed]` — the
sequence file carries no generation banner and no generator writes it.

## 13. Findings this preflight raises on its own

| | Finding | State |
|---|---|---|
| **G-1** | `check_governance` sweeps untracked files, so any working-tree scratch file can turn the battery red and be indistinguishable from a corpus defect | open — needs a rule decision, not just a code change |
| **G-2** | `PROJECT-STATUS.md` falsely claims its published battery is the hosted battery; `AGENTS.md` states the requirement as though it held | repaired this round, §13 |
| **G-3** | `FINAL-PUBLIC-CLONE-REPORT.md` says zero of the eight reviews were obtained; all eight now are | open — the report is pinned to `5e8b286` and its replacement is owed anyway |

## 14. What this preflight does not establish

- **Nothing about content.** Every figure above is mechanical. A generated
  index matching regeneration says the generator is deterministic; it says
  nothing about whether the contract it indexes is right.
- **No clean-clone claim.** §2's battery ran in the working tree on the
  founder machine. At one past commit the working tree and a clone disagreed,
  because a check asked the local filesystem about a git-excluded directory.
  Until §13's clone is run at this round's final commit, clone status for that
  commit is `[Unknown]`.
- **No readiness claim.** The readiness question is charter §17's and is
  answered in this round's readiness report, not here.
