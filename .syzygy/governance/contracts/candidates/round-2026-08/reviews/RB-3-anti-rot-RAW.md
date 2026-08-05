# RB-3 — Knowledge architecture and anti-rot — RAW reviewer report

**Review vertical 3.** Fresh-context session. Raw output, stored verbatim.

---

## Provenance

**Repository state at review.**

```text
HEAD            9e6f2f7db55c4ce672daf9636f1cf2ab664879c8
branch          main
working tree    dirty (concurrent round edits by sibling workstreams)
review date     2026-08-05
corpus sha256   ac817d5b4838df526d1cef800d27deae1fda001c68263c22f08c6c83f558006d
                (the 71-file pinned corpus of TERM-MIGRATION-REPORT §1.1,
                recomputed by its own stated command — see §Sweeps below)
```

**Constraint honoured:** nothing under `_bootstrap/` was read. No authoring
conversation was sought or received. Everything below rests on clone-visible
tracked or untracked-but-present files, read at source in this session.

### What I read in full

- `policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` (441 lines)
- `policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md` (183 lines)
- `policy-candidates/SEMANTIC-DELTA-TEMPLATE.md` (159 lines)
- `policy-candidates/TERM-REGISTRY.md` (1,334 lines — §§1–3, §5, §6 in full;
  all 30 entries parsed programmatically; T-01…T-06, T-26…T-30 read in full)
- `round-2026-08/TERM-MIGRATION-REPORT.md` (542 lines)
- `round-2026-08/ACTIVE-AUTHORITY-MAP.md`, `ARTIFACT-INVENTORY.md`,
  `HISTORICAL-ARCHIVE-INDEX.md`, `PROCESS-LESSONS.md`,
  `SEMANTIC-DELTAS-THIS-ROUND.md`
- `AGENTS.md`, `README.md`
- `.syzygy/governance/policies/craft-and-care/README.md`, `INSTALL-RECORD.md`
- `06-CONTEXT-LOAD-MAP.md`, `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`
  (§1, §6, §7), `ACTIVE-CONTRACT-MANIFEST.txt`,
  `04-CLAUSE-MIGRATION-MATRIX.md` (change log §), `README.md` and
  `00-README.md` of `candidates/`
- `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`
- `.syzygy/map/topology-candidates/BUNDLE-MANIFEST.md`
- `scripts/check_governance.py` (CG-4, CG-7, CG-8 bodies)

### What I read at source for citation resolution

`doctrine/vision.md` (Thesis, north star), `doctrine/architecture.md`
(Governed projects; Typed authority; Project Genome; Definitions; Snapshots
and the loop; Vocabulary), `doctrine/trust-and-evidence.md` (Evidence and the
two other warrants; Status claims vs narrative claims; Staleness),
`doctrine/security.md`, `decisions/SURFACE-DECISION-RECORD.md` (ID range),
and inside the candidate contract corpus: RFC1-8, RFC1-14, RFC1-15, RFC1-18,
RFC1-22, RFC1-24, RFC1-25, RFC1-32, RFC2-17, RFC2-25, RFC3-4, RFC3-16,
RFC8-12, RFC8-28, RFC10-4, RFC10-6, RFC10-15, RFC11-1, RFC11-8, RFC11-11.

### Commands run

```sh
# 1. Repository state and sizes
git rev-parse HEAD; git log --oneline -3; git tag -l
wc -l -w <all subject files>
git ls-files --cached --others --exclude-standard          # 177 paths

# 2. Term-registry structural conformance (Python re; 30 entries parsed)
#    field-label presence per entry; owning-authority block extraction;
#    authority-coverage classification cross-check

# 3. Citation resolution — all 58 distinct RFCn-m citations in the registry
#    resolved against a clause index built over the 32 modules

# 4. Craft clause-family enumeration
python3 -c "re.findall(r'CC-[A-Z]+-\d+') over craft-and-care/*.md"

# 5. Sweep A of TERM-MIGRATION-REPORT §1.2, verbatim, plus its corpus digest
#    command from §1.1 (both reproduced below)

# 6. Repository checks
python3 scripts/check_governance.py

# 7. Digest verification of all four gate arguments
sha256sum ACTIVE-CONTRACT-MANIFEST.txt \
          craft-and-care/testing-and-verification.md \
          topology-candidates/BUNDLE-MANIFEST.md \
          .syzygy/intent/OVERVIEW.md

# 8. Artifact-inventory cluster counts recomputed from git ls-files
```

`grep` was used only with `-F`/`-n` on literals and never to support a
universal claim; every load-bearing count below is Python `re`.

---

## Sweep reproduction — TERM-MIGRATION-REPORT

I re-ran the report's own Sweep A (§1.2, verbatim) and its corpus digest
command (§1.1, verbatim) at this session's tree state.

**Corpus pin.** 71 files, in the six declared groups at the declared counts
(doctrine 6, craft 10, rfc-candidates 32, decisions 5, front-door 7,
topology-candidates 11). **Reproduced exactly.**

Corpus digest recomputed: `ac817d5b4838df526d1cef800d27deae1fda001c68263c22f08c6c83f558006d`.

This is **not** the report's pin (`21ff53b0…`) — and the report predicted
exactly this, naming `ac817d5b4838df52…` at §1.1 as the value it already saw
four minutes after pinning. The tree has not changed since that second
computation. The report's honesty about its own corpus drift is verified, not
merely asserted.

**Counts checked — 5 claims requested, 22 phrases re-run.** Every figure
reproduces exactly:

| Claim (report §, line) | Claimed | Reproduced | |
|---|---:|---:|---|
| `source snapshot` (§1.3, :185) | 27 occ / 16 files | 27 / 16 | ✓ |
| `snapshot` bare (§1.3, :186) | 235 occ / 40 files | 235 / 40 | ✓ |
| `state plane` Sweep A (§1.4, :219; §4, :351) | 16 / 6 | 16 / 6 | ✓ |
| `state plane` literal-space, no plural (§1.4, :217) | 1 | 1 | ✓ |
| `state plane` literal-space, plural (§1.4, :218) | 12 | 12 | ✓ |
| `execution plane` literal-space (§1.4, :225) | 0 | 0 | ✓ |
| `execution plane` Sweep A (§1.4, :225) | 1 | 1 | ✓ |
| `feature` (§3, :312) | 28 / 12 | 28 / 12 | ✓ |
| `status` bare (§3, :313) | 316 / 62 | 316 / 62 | ✓ |
| `state` bare (§3, :314) | 693 / 63 | 693 / 63 | ✓ |
| `done`/`complete`/`finished` (§3, :315) | 34/48/5 · 12/23/3 | identical | ✓ |
| `proof` (§3, :316) | 36 / 20 | 36 / 20 | ✓ |
| `conflict` (§3, :317) | 22 / 16 | 22 / 16 | ✓ |
| `source of truth` (§3, :318) | 8 / 6 | 8 / 6 | ✓ |
| `passing`/`compliant` (§3, :319) | 12/2 · 10/2 | identical | ✓ |
| `notification`/`alert`/`inbox` (§3, :320) | 0 | 0 / 0 / 0 | ✓ |
| `context window`/`system prompt` (§3, :321) | 0 | 0 / 0 | ✓ |
| `main repo`/`primary repo` (§3, :322) | 0 | 0 / 0 | ✓ |
| `tech debt`, `audit log`, `not applicable` (§3, :323–324) | 0 | 0 | ✓ |
| `four states` (§2, :274) | 0 (A and B) | 0 | ✓ |
| six-plane table (§2, :241–249) — all 14 cells | as tabled | all 14 identical | ✓ |
| five-dimension table (§4, :349–356) — all 6 rows | as tabled | all 6 identical | ✓ |

**One count does not reproduce:** `feature id` (§3, :312, `→ **0** (Sweep A
and B)`) scores **1** under Sweep A's own pattern. See **F8**.

This is, on the evidence, the most reproducible quantitative artifact in the
repository. §1.3 and §1.4 are genuinely good work: the pattern-vs-concept
distinction and the line-wrap/emphasis hazard are both real, both demonstrated
with a falsifiable measurement, and both correctly generalised.

---

## Findings

### F1 — BLOCKING · All four digest-bound act phrases in the acceptance record are stale, and `AGENTS.md` names two owners for that one fact

`AGENTS.md:37-40` states:

> "The single owning record for exact phrases, digests, and ceremony is the
> acceptance record in `.syzygy/governance/contracts/candidates/` (this file
> deliberately does not restate digests — **the record and the manifests own
> them**)."

Two sentences, two different owners for one fact. Under CC-KNOW-1 / CC-REV-3
that is a duplicate-authority declaration in the routing file itself. It is
not theoretical: **the record and the manifests now disagree on every single
gate argument.**

Verified this session by `sha256sum` against each act's own subject artifact:

| Act | Record states (`FINAL-…-RECORD.md`) | Artifact actually hashes to | |
|---|---|---|---|
| 1 | `08793ddf70f3…` (:15, :118, :213, :215) | `5c4d6798354135bd860b3a2637c282f535c519bdd1a3cbab67d7555367af6caa` | **MISMATCH** |
| 2 | `aa2d6353de88…` (:16) | `3858820f64768ef20e6514fe8adb28076263f071ac77e66a5520a612f3bcb26d` | **MISMATCH** |
| 3 | `0d34d1b518fe…` (:17) | `89279260e4b2a74c0c32503e082802bee5811b54b42d329d265cd7df3e671ef9` | **MISMATCH** |
| 4 | `42de2eb1434d…` (:18) | `49a1a09c2f45ac6df9be19f48f1c136e37f52e4f627cbdcd097e91a3452e61fa` | **MISMATCH** |

Each mismatch has a recorded cause and a correct current value living
somewhere else in the tree:

- act 1 — `SEMANTIC-DELTAS-THIS-ROUND.md:20-21` (SD-1) records the manifest as
  regenerated; correct value in `ACTIVE-CONTRACT-MANIFEST.txt` itself and
  restated at `ARTIFACT-INVENTORY.md:14`;
- act 2 — `INSTALL-RECORD.md:71-74` states in terms that "the previously
  offered `CC-TEST-2@aa2d6353…` argument is **stale and satisfies nothing**";
- act 3 — `SEMANTIC-DELTAS-THIS-ROUND.md:29-32` (SD-2) records the bundle
  digest invalidated and `BUNDLE-MANIFEST.md` regenerated;
- act 4 — `OVERVIEW.md` is modified in the working tree (`git status`), and
  `ARTIFACT-INVENTORY.md:24` records a "four-layer refactor this round".

**Why this is blocking and not merely stale bookkeeping.** `AGENTS.md:47`
routes act 4's digest *specifically* to "digest stated in the acceptance
record" — i.e. an agent or owner following the repository's own routing lands
on `42de2eb1…` and would write a phrase that binds an artifact state that no
longer exists. The record carries no staleness banner of any kind; its header
(:1-9) reads as current. By the repository's own rule — "an artifact edited
after its act is, for the record, an artifact with no act" (`AGENTS.md:52-54`)
— its mirror is equally true here: **an act argument that no longer names any
artifact is a phrase that accepts nothing.**

**The check battery does not catch three of the four.** `check_governance.py`
CG-7b examines **1 argument** (act 1) and FAILs on it:

```text
FAIL  CG-7b  act-1 argument matches the manifest — 1 argument examined, 1 finding
        …offers 08793ddf70f3… but the manifest now hashes to 5c4d67983541…
        — the act would bind a package that no longer exists
```

Acts 2, 3 and 4 are outside every check's class, and no check output says so.
That is CC-KNOW-18's denominator rule failing in the one place it matters
most: a truthful "1 examined" over a population of 4.

**Additional restatement sites** that carry the stale values and would also
need the same logical change: `00-README.md:39-40` (topology `0d34d1b5…`,
overview `42de2eb1…`, craft `aa2d6353…`) and `10-EXIT-REPORT.md:113`.

---

### F2 — MATERIAL · The round's first real use of its own change workflow under-states a blast radius, and the delta register's universal claim is not met

`SEMANTIC-DELTAS-THIS-ROUND.md:3` claims: *"Every normative or
authority-adjacent edit this round travels as a recorded delta."* That is a
completeness claim in the sense of CC-KNOW-16.

It is not met, and the gap is inside the act-1 digest set.

- SD-1 (`:20-21`) attributes the act-1 manifest churn to one file:
  *"invalidates the prior act-1 manifest digest `08793ddf…` → manifest
  regenerated."* The only module SD-1 names is
  `rfcs/RFC-0003/governance-homes-and-owner-acts.md`.
- But `rfcs/RFC-0007/README.md` — **line 21 of
  `ACTIVE-CONTRACT-MANIFEST.txt`, squarely inside the act-1 digest set** —
  was also edited this round. `04-CLAUSE-MIGRATION-MATRIX.md:1065` (row 4)
  records it explicitly: *"The same stale figures were corrected in
  `rfcs/RFC-0007/README.md` in the same batch."* I verified the file: line 46
  now reads `this index is 2,326`, and `wc -w` returns 2,326.
- SD-7 (`:115-116`) acknowledges this obliquely — *"content then modified only
  per SD-1..SD-2 and the R1/D2 accounting fixes **recorded separately**"* —
  but "separately" resolves to no delta. The record is the 04 matrix's own
  change log, which is not the round's delta register and is not linked from
  it.

Under `NORMATIVE-CHANGE-WORKFLOW.md` step 2 ("every dependent found, by a
stated method"), SD-1's impact field is the exact field the workflow's own
worked micro-example (`:126-150`) says "does the real work here." Its first
live exercise names one of at least two files that moved the digest.

**Compounding defect, same batch.** `04-CLAUSE-MIGRATION-MATRIX.md:1052-1053`
opens its change log with:

> "Corrections to this file's **accounting**, not to any clause text. **No
> contract module changed in this batch**; the act-1 digest set is unaffected
> by rows below that touch only this file."

The second clause is correctly qualified ("rows below that touch only this
file"). The first is not, and row 4 twelve lines later contradicts it
outright. A fresh reader of that paragraph concludes the act-1 digest set is
intact — which is precisely the wrong conclusion, and precisely what CG-7b
FAILs on.

Note also that a literal-space `grep` for `"No contract module changed in this
batch"` returns zero: the sentence is line-wrapped at `contract` / `module`.
This is TM-8 §1.4's own hazard, encountered live while verifying TM-8 §1.4.

---

### F3 — MATERIAL · `PROCESS-LESSONS.md` asserts that a candidate model supersedes adopted doctrine's phrasing, contradicting TM-8 and the registry

`PROCESS-LESSONS.md:85-87`:

> "…contracts RFCn-m; craft CC-*; **the six-plane state vocabulary supersedes
> older three/four-state phrasings in presentation prose** (canonicalized this
> round in the term registry)."

Three separate problems, all verifiable against this round's own outputs:

1. **It reverses the round's finding.** `TERM-MIGRATION-REPORT.md:279-295`
   (TM-8) concludes: *"There is **no term drift to repair here**"*, and its
   recommended disposition item 2 is *"Record the three-state thesis as a
   **compression, permitted in presentation prose**, **not as a deprecated
   synonym**."* "Supersedes" is the deprecated-synonym reading TM-8
   explicitly rejected.
2. **It elevates candidate over adopted.** `TERM-REGISTRY.md:91-95` is
   unambiguous: *"doctrine's three-state thesis is **adopted**; the six-plane
   model is **candidate**… It does not and cannot make RFC1-22 binding. Until
   an owner act accepts RFC-0001, 'six planes' is how we agree to speak, and
   `vision.md` is still what governs."* `vision.md:19` (adopted) is the text
   PROCESS-LESSONS says is superseded.
3. **It revives text TM-8 proved does not exist.** `four states` scores **0**
   by Sweep A *and* Sweep B (`TERM-MIGRATION-REPORT.md:274`; I reproduced the
   zero). TM-8's open item O-6 exists solely to correct P-16's phrase *"the
   older four-state phrasing"* because it names nothing. PROCESS-LESSONS
   re-introduces the same phantom in a tracked, clone-visible file.

`PROCESS-LESSONS.md` self-labels as never authority and non-default context
(`:5-9`) — which mitigates but does not cure it, because `AGENTS.md:123-124`
cites it by path as "Incident history behind these rules," and item 3 is a
statement of fact about the corpus that is simply false.

---

### F4 — MATERIAL · Two context-budget instruments, different bands, relationship stated nowhere

Requested test. The result is: **not a contradiction, but not a stated
two-instruments relationship either — the relationship does not exist in any
tracked file.**

| Instrument | Where | Packet band |
|---|---|---|
| Charter §11.4, carried verbatim as **CC-BUDGET-1** | `CRAFT-KNOWLEDGE-HYGIENE-POLICY.md:288-297` | default packet **5,000–15,000 tokens**; above **20,000** → justification or decomposition |
| Measured working target | `06-CONTEXT-LOAD-MAP.md:45-51` | "Within **15–20k** target" |

I verified CC-BUDGET-1's six rows against the charter's §11.4 table
(`syzygy_fable_human_clarity_refactor_round_prompt.md:804-816`): **identical,
all six rows, no drift.** CC-BUDGET-1 is a faithful carry. The problem is what
sits beside it:

- **Neither file cites the other.** `06` cites RFC11-11 and calls its number
  "a working policy figure, **not** doctrine" (`:55-57`). CC-BUDGET-1 cites
  nothing beyond the charter. RFC11-11 (verified at source,
  `RFC-0011-context-compiler.md:193-205`) delegates the concrete number to
  "the rev10 context-load map and context-selection fixtures" and rules it
  "must not be frozen into contract text without an owner act." So RFC11-11
  points at `06`; nothing points at CC-BUDGET-1; and CC-BUDGET-1 points at
  neither.
- **The bands genuinely disagree in the middle.** Fixtures 1 (18,716), 3
  (19,080) and 5 (17,338) are marked ✓ by `06` and sit **above** CC-BUDGET-1's
  default packet band. Under CC-BUDGET-2 each should have triggered a
  decomposition review whose outcome is *recorded*; none is recorded anywhere.
  Fixture 4 (14,705) is marked ✓ against a target it is *below*.
- **The implementing check silently covers 2 of §11.4's 6 rows.**
  `check_governance.py:553-556` implements only `README.md` (1,200) and
  `AGENTS.md` (1,500) as file budgets, plus the two module thresholds. **The
  two context-*packet* rows — the rows that govern context packets — are not
  checked at all**, and CG-8's output ("34 artifacts examined") does not
  disclose the omitted class. The code carries a comment explaining a
  *different* two-instruments relationship (the 7,000-word ceiling in
  `verify_final_prespec.py`) but says nothing about the packet rows or `06`.
- **The owner is asked the wrong version of the question.** Hygiene-policy
  ruling item 4 (`:437-438`) asks whether CC-BUDGET-1's figures "should bind as
  stated or be re-derived from this repository's actual corpus." It does not
  tell the owner that a re-derived, *measured* figure already exists in the
  repository and disagrees. That omission is the material part of this
  finding.

**README/AGENTS against their budgets** (requested): `README.md` 751 words
against 1,200 ✓; `AGENTS.md` 1,376 words against 1,500 ✓. Both under. CG-8
reports both clean. `AGENTS.md` at 92% of trigger is worth a note but is not a
finding.

---

### F5 — MATERIAL · `TERM-REGISTRY.md:1311-1317` — "sixteen of thirty" is arithmetically unreachable; the true figure is 18

The registry's closing gap statement:

> "Doctrine freezes thirteen technical nouns… **Sixteen of this registry's
> thirty terms sit outside the frozen list.**"

Verified at source. `architecture.md:287-289` freezes exactly thirteen nouns,
and the registry quotes all thirteen correctly — that half is right.

Enumerating the thirty entries against those thirteen:

- **On the list (12):** T-01 Project, T-03 Project Genome (*genome*),
  T-04 Capability, T-14 Evidence, T-17 Warrant, T-19 Contradiction, T-20 Gap,
  T-21 Source snapshot (*snapshot*), T-22 Evaluation, T-23 Observation record,
  T-24 Aligned, T-25 Converged.
- **Outside (18):** T-02, T-05, T-06, T-07, T-08, T-09, T-10, T-11, T-12,
  T-13, T-15, T-16, T-18, T-26, T-27, T-28, T-29, T-30.

Sixteen is not reachable under any matching rule. The thirteenth frozen noun
(*genome-complete*) has no registry entry at all, so **at most 12 entries can
match** — the outside count cannot fall below 18. Under strict headword
matching (rejecting *Project Genome*→genome and *Source snapshot*→snapshot)
the figure is 20.

The claim **understates the very authority gap the paragraph exists to
report**, in the artifact whose entire methodological premise is counting
rigor, two lines after a paragraph headed "Counted by script." It is the exact
class CC-KNOW-17 governs.

---

### F6 — MATERIAL · The pending-decision register routes ten items to `_bootstrap/**` paths whose tracked homes now exist

`PENDING-OWNER-DECISIONS.md` is on the default agent reading path
(`AGENTS.md:64-65`: *"open decisions → `decisions/PENDING-OWNER-DECISIONS.md`"*).
Its owning-record column still points into founder-local storage for records
that SD-7 relocated into the tracked tree this round:

| Item | Register points to | Tracked home that now exists |
|---|---|---|
| P-1 (:21) | `_bootstrap/rfc-phase/final-prespec/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` | `candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` |
| P-2…P-5 (:22-25) | "same record" (as above) | as above |
| P-5 (:25) | `_bootstrap/rfc-phase/final-prespec/DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md` | `candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md` |
| P-12 (:46) | `_bootstrap/knowledge-refactor/CRAFT-KNOWLEDGE-HYGIENE-POLICY-DRAFT.md` | `candidates/policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` |
| P-14 (:48) | `_bootstrap/knowledge-refactor/LICENSE-DECISION-PACKET.md` | `decisions/LICENSE-DECISION-PACKET.md` |

This is a partial propagation of one logical change (CC-REV-2; CC-KNOW-14):
the relocation landed, the reading paths did not. The register's own
disclosure (`:12-15`) says a clone "cannot resolve those pointers; whether
those records move to a tracked home is itself item P-9" — but for the rows
above **they have already moved**, so the disclosure now understates the
repository and overstates the clone gap.

CG-12b allowlists the file wholesale ("file-level disclosure that these
pointers are git-excluded"), so no check surfaces it.

Related, same file: P-16 (:50) still reads *"the older four-state phrasing"* —
the wording TM-8's O-6 exists to correct. Not this workstream's file to edit,
correctly so; recorded here as confirmation that O-6 is still open.

---

### F7 — MATERIAL · `06-CONTEXT-LOAD-MAP.md` carries no derived label, and it is the routed entry point for every contract question

`AGENTS.md:62-63`: *"Contract question → start at
`contracts/candidates/06-CONTEXT-LOAD-MAP.md`."* It is the first artifact an
agent with a contract question opens.

`ACTIVE-AUTHORITY-MAP.md:42-44` lists it among "Generated indexes (this file,
`05-CONTRACT-INDEX.yaml`, `CONTRACT-DEPENDENCY-INDEX.md`,
`TASK-TO-CONTRACT-INDEX.md`, `06-CONTEXT-LOAD-MAP.md`) are derived and never
authority."

But the file itself (`:1`) is titled only *"Context-load map — reader map and
measured load tests (directive §5/§7)"* and carries **no derived marker, no
"never authority" line, and no named source** in its first ten lines. Its
siblings all do:

- `TASK-TO-CONTRACT-INDEX.md:1` — "derived, never authority"
- `CONTRACT-DEPENDENCY-INDEX.md:1` — "derived, never authority"
- `05-CONTRACT-INDEX.yaml:1-2` — "generated projection… Authoritative metadata
  lives in the active contract files' front matter"
- `ACTIVE-AUTHORITY-MAP.md:1` — "derived, never authority"

CC-KNOW-11 requires each derived artifact to be "labeled derived, names its
source." `06` is the one member of that set that is neither, and it is the one
on the routed path. It is also the file CC-KNOW-11's own violation example
cites (*"a generated context-load map carrying two stale cells"*, `:191-193`).

Mitigating: `candidates/README.md:1-3` carries a strong directory-level
"NOT ACCEPTED / nothing here binds" banner covering the whole tree. That
addresses *candidate* status; it does not address *derived* status.

---

### F8 — MINOR · `TERM-MIGRATION-REPORT.md:312` — `feature id → 0 (Sweep A and B)` is 1 under Sweep A's own pattern

The report's `ws()` helper (`:120-123`) joins words with
`(?:\s|\*|_|` + backtick + `)+`, which includes the underscore. Under that
pattern `feature_id` matches. Re-running Sweep A verbatim:

```text
feature id                          1     1
```

Located: `rfcs/RFC-0001-project-graph-identity-state-planes.md:750` —
`11. *(RFC1-32)* A surface stores `feature_id` alongside capability
identities.`

**The substantive assessment is unaffected** — the single hit is RFC1-32's own
violation example, i.e. the clause deprecating the term, exactly the class the
row's prose already accounts for ("11 of 28 are RFC1-32's own no-Feature
clause"). The defect is that a **zero claim is asserted for an instrument that
does not produce it**, in the report whose §1.3 thesis is that "an occurrence
count is a measurement of a pattern, not of a concept." Sweep B (literal
`grep -ioF 'feature id'`) does return 0; the parenthetical should say Sweep B
only, and the Sweep A result should be stated with its site.

---

### F9 — MINOR · `ACTIVE-AUTHORITY-MAP.md:22` cites a fact the craft README does not carry

The row routes clause accounting to "clause counts per file in the cluster
README." The craft cluster README contains no clause counts: its "Reading
order" (`:57-79`) lists eight files with topic descriptions only, and a sweep
for `[0-9]+ (clause|rule)` over that file returns nothing. The map sends a
reader to a home that does not hold the fact.

(The row is otherwise correct: all nine CC-* families it names verify against
the installed cluster — `BAR, DEP, OBS, PERF, PROV, REV, SEC, TEST, VIZ`,
reproducing TM-11(b)'s enumeration exactly.)

---

### F10 — MINOR · `ARTIFACT-INVENTORY.md:5` — "175 files"; actual is 176

Recomputed by the inventory's own stated command
(`git ls-files --cached --others --exclude-standard`, excluding the round
prompt): **176**.

**All eighteen cluster rows reproduce exactly** — 7 / 6 / 5 / 10 / 32 / 22 /
9 / 19 / 9 / 9 / 4 / 12 / 4 / 11 / 1 / 2 / 3 / 11, summing to 176 with zero
uncovered paths. The single discrepancy is the header total, and its cause is
visible in the table: the `round-2026-08/` row is honestly labelled `11+`
("grows until round close") and now holds 12. The row disclosed its own
volatility; the header did not inherit the disclosure. Writing this review
file makes it 177.

---

### F11 — MINOR · Three artifacts disagree about whether residual R1 is fixed; the source says fixed

- `CRAFT-KNOWLEDGE-HYGIENE-POLICY.md:266-268` (CC-KNOW-17) — present tense:
  *"[Observed — a residual of this kind **rides in the current candidate
  package**]"*
- `FINAL-…-RECORD.md:271-281` (§7 item 10) — *"`rfcs/RFC-0007/README.md` line
  46 states its own size as **2,268** words"*, and offers the owner a choice
  between accepting it and directing a fix
- `PROCESS-LESSONS.md:30-31` — *"(R1 itself was corrected in this round's
  package revision.)"*

**At source:** `rfcs/RFC-0007/README.md:46` reads `this index is 2,326.
Package union: 10,636 words`; `wc -w` returns 2,326. R1 is fixed, and
`04-CLAUSE-MIGRATION-MATRIX.md:1065` records the fix with its recount.

So CC-KNOW-17 carries a stale `[Observed]` bracket, and the acceptance record
asks the owner to decide a question another workstream already executed —
which is also part of why the act-1 digest moved (F1, F2).

`reviews/DISPOSITIONS.md:153` also says "NOT FIXED", but that file is stored
review evidence and is correctly never edited
(`HISTORICAL-ARCHIVE-INDEX.md:11`). No finding there.

---

### F12 — MINOR · The term registry declares no field schema, and one entry's field label deviates

**All 30 entries carry all ten required elements** — stable ID, canonical
term, and the eight labelled fields (Plain language, Formal definition, Owning
authority, Permitted aliases, Deprecated synonyms, Related but distinct,
Example, Misuse). **Zero gaps.** I checked this programmatically across all
30 and then read the one entry my parser flagged.

Two machine-checkability nits:

1. **T-26 Reconciliation (`:1084`)** writes the label as `**Deprecated
   synonyms — and this is a hard reservation.**` rather than `**Deprecated
   synonyms.**`. The field is present and is the strongest one in the registry
   (the work-scheduler word reservation, verified against RFC2-17 at source).
   But it is the sole label deviation in 240 fields, and it produced a false
   gap in my first automated pass. Open item **O-9** proposes exactly such a
   check; it will fire on this entry.
2. **"How to read an entry" (`:16-33`) never enumerates the ten fields.** It
   explains the term ID, the typed owning-authority marker, and the
   formal-vs-plain distinction — but states no field schema and no rule that
   every entry carries every field. The registry therefore has no declared
   conformance criterion to check against, which is a CC-KNOW-2 scope gap in
   the artifact whose sibling policy authored CC-KNOW-2.

---

### F13 — MINOR · `TERM-REGISTRY.md:1295` — "Counted by script" over a classification no script can make

The authority-coverage summary opens: *"Counted by script over the 30 entries
above, not by hand."* The arithmetic (22 + 8 = 30) is right and the entry
lists are right — I cross-checked every entry's owning-authority block.

But the classification itself is not scriptable from the entry text. Seven
entries (T-06, T-08, T-12, T-16, T-27, T-28, T-30) contain the word "adopted"
inside their owning-authority block while belonging to the *candidate-only*
row — because the block says things like *"No adopted doctrine clause defines
'state plane'"* (T-06), *"Adopted grounding: VIS-4"* (T-27), or *"SDR-9 and
SDR-33 (**adopted owner rulings**) behind `report-fact`"* (T-16). Sorting
those correctly requires reading what the adopted citation *does* — mechanism
versus definition — which is judgment.

The judgments are, as far as I can check, all defensible. The claim about how
they were reached is not. Under CC-KNOW-17 ("any quantitative claim states how
it was computed") the honest form is: entries enumerated by script, coverage
class assigned by reading.

---

### F14 — MINOR · CG-4's class covers 6 files; 31 of 32 contract modules are outside it with no disclosure in the output

`check_governance.py:389-422`: CG-4's target set is `00-README.md`, the four
`policy-candidates/*.md`, and `topology-candidates/TRACKING-NOTE.md` — six
files. The output reads `OK CG-4 candidate homes carry candidate banners —
6 files examined, 0 findings`.

`contracts/candidates/rfcs/` — the largest candidate home, 32 modules, the
act-1 subject — is not in the class. I checked: **31 of 32 modules do not
contain the word "candidate" in their first 12 lines.**

The code carries an explicit, well-reasoned comment for the *topology*
exemption (`:395-398`: stuffing a banner into a digest-bound member would
churn the offered digest for labelling alone). The identical reasoning applies
to the RFC modules, but it is nowhere written, and the check's *output* — the
thing CC-KNOW-18 says a reader must read — states a denominator without
stating the class it excludes.

**Not a careless-reader risk in practice:** `candidates/README.md:1-4` carries
a directory-level *"Candidate contract package — NOT ACCEPTED… nothing here
may be cited as accepted authority"*, and each module's own header states
*"Absent such a record, this contract binds nothing."* Answering the charge's
question 4 directly: **no candidate is citable as accepted by a careless
reader.** The finding is about the check's undisclosed class, not about the
labelling.

---

### F15 — MINOR · `README.md:75` states the craft cluster's status without the binding-onset caveat its two sibling maps both carry

| Where | How craft status is stated |
|---|---|
| `AGENTS.md:24` | "**Owner-approved (D2)**; clause-level force begins at foundational-contract acceptance (see `INSTALL-RECORD.md`)" |
| `ACTIVE-AUTHORITY-MAP.md:22` | "Owner-approved (D2); act-2 confirmation pending for CC-TEST-2's amendment" |
| `README.md:75` | "**Owner-approved** (D2)" — no caveat |

A front-door reader concludes the engineering bar binds today; `INSTALL-RECORD.md:17-26`
says it binds implementation work only from foundational-contract acceptance.
Practical risk is currently nil (there is no implementation work), which is
why this is minor rather than material — but the README is the artifact most
likely to be read alone.

---

## What I checked and found sound

Recording these because a review with no findings is itself a finding, and so
is a review that reports only findings.

**Hygiene policy (CC-KNOW-1…18, CC-BUDGET-1…4) — P-10's missing review.**

- **All six `Extends:` citations resolve** to real installed clauses:
  CC-KNOW-1→CC-REV-3, CC-KNOW-4→CC-PROV-3, CC-KNOW-9→CC-REV-1/CC-REV-4,
  CC-KNOW-10→CC-BAR-7, CC-KNOW-14→CC-REV-2. Each installed clause was read at
  source and each extension is a genuine governance-lane narrowing, not a
  restatement. Every other CC-* citation in the file (CC-REV-5, CC-REV-6,
  CC-REV-7, CC-BAR-2, CC-TEST-3, CC-TEST-4) resolves to an installed clause.
- **The 16-item coverage table (`:333-351`) checks out row by row** against the
  charter's list at `syzygy_fable_human_clarity_refactor_round_prompt.md:891-906`.
  Charter items and rule text match in substance for all sixteen; the three
  extras (CC-KNOW-16/17/18) are correctly segregated on their own row so they
  can be struck in one act.
- **CC-BUDGET-1's table is the charter's §11.4 table verbatim**, six rows, no
  drift. The change-log entry explaining why the draft's nine-row table was
  cut (`:361-374`) — because at least one adopted doctrine file already sat
  outside the dropped lower bounds, and "a candidate policy that puts adopted
  material in permanent breach is a defect in the policy" — is exactly right.
- **Every violation example actually violates its rule.** I read all 22. None
  is decorative; several are the repository's own incidents, correctly
  labelled `[Observed]`. The one stale bracket is F11.
- **No rule contradicts an installed clause or doctrine** that I could find.
  CC-KNOW-6's "a derived artifact supplying a definition manufactures
  authority" and CC-KNOW-11's "never in anticipation of an approval that has
  not happened" are both sharper than anything installed and consistent with
  CC-REV-3 and VIS-4.
- **The "What this policy does not do" section (`:411-427`) is unusually
  honest** — it names its own unaudited overlap, its unapplied admission test,
  and the fact that it has never been executed. That is the section a weaker
  candidate would omit.

**Term registry — P-10's missing review.**

- **All 58 distinct `RFCn-m` citations resolve** to a defining occurrence in
  the 32-module corpus. Zero dangling.
- **Spot-checked 20+ at source for content, not just ID existence**, covering
  well beyond the requested 3 doctrine-owned and 3 candidate-owned:
  - *doctrine-owned:* T-01/T-04/T-24/T-25 → `architecture.md` "Definitions"
    (:157) — Project, Capability, Aligned, Converged all match the doctrine
    text closely; T-02 → "Governed projects and the two-namespace plane"
    (:7); T-03 → "Project Genome" (:122) — the three-tier inventory matches;
    T-13/T-15 → `trust-and-evidence.md` "Status claims vs narrative claims"
    (:37); T-14/T-17 → "Evidence, and the two other warrants" (:8); T-12 →
    "Staleness" (:97); T-19/T-20 → `architecture.md` "Typed authority" (:84);
    T-22/T-23 → "Snapshots and the loop" (:207).
  - *candidate-owned:* RFC1-8 (T-03's Genome-as-membership-predicate — the
    clause's final sentence says exactly that), RFC1-14 (T-04 — near
    verbatim), RFC1-15 (T-05), RFC1-22 (T-06), RFC1-32 (T-04's Feature
    deprecation), RFC2-17 (T-26's word reservation), RFC2-25 (T-16), RFC3-4
    (T-02's location-is-designation), RFC8-12/RFC8-28 (work lifecycle),
    RFC10-4/RFC10-6 (T-27), RFC11-1 (T-30).
  - **Not one misattribution found.**
- **The five-dimension separation table (§1, `:42-48`) is internally
  consistent and correct at source.** Verified: the six state planes against
  RFC1-22; the three exclusive epistemic labels against
  `trust-and-evidence.md:59-68`; **all six evidence tiers with their parent
  labels** against RFC2-25 (`rendering-vocabularies.md:145-163`) — names,
  parents and the "a tier is never a fourth label" rule all match; **the
  thirteen work-lifecycle values** against RFC8-12
  (`state-vocabulary-and-cost.md:77-90`) — 8 live + 1 terminal + 4 absence =
  13, closed, exactly as tabled; the governance lifecycle against RFC3-16.
- **The term-admission rule is present** (§3, `:99-120`) with all four
  conditions, plus a corollary that is genuinely useful ("a distinction that
  is real is worth a term; a distinction that is merely felt is worth a
  sentence").
- **The registry cites and does not re-own.** Every entry names an owning
  authority; the header (`:8-11`) states that authorities win over the
  registry's restatements; §2 (`:91-95`) refuses to canonicalize six planes as
  anything more than a drafting convention. The charge's specific worry — a
  registry manufacturing authority — is directly and repeatedly defended
  against, and CC-KNOW-6 in the sibling policy names it as a violation class.
- **§6 "What this registry does not establish" (`:1321-1334`)** names four
  real limits including the unrun half of the lexical audit.

**Authority-map labelling (charge question 1, authority maps).** All three
maps are correctly typed as non-authoritative: `ACTIVE-AUTHORITY-MAP.md:1`
("derived, never authority"), `README.md:81-82` ("this README are
presentation"), `AGENTS.md:7-8` ("not project truth and must never be cited as
authority"). Verified five map rows at source: VIS-1…7 (7 exactly), SEC-1…5 (5
exactly), SDR-1…33 (33, contiguous, none missing), 32 contract modules,
topology "9 members + `BUNDLE-MANIFEST.md`" (bundle manifest lists exactly 9;
directory holds 11 with the manifest and tracking note). The
`ACCEPTANCE-ACT-RECORD.md`-does-not-exist claim and the
accepted-homes-not-created claims are true (`ls` confirms; CG-6 agrees). The
`doctrine-adopted-2026-07-30` tag exists and resolves.

**Lifecycle lanes and archive boundaries (charge question 4).**
`HISTORICAL-ARCHIVE-INDEX.md` is a clean, correct instrument — seven archives,
each with clone-visibility stated and an explicit "may be cited as" column.
No historical material is on a default reading path: `AGENTS.md:66-69` names
history only to exclude it, and its single history pointer (`:123-124`,
PROCESS-LESSONS) is labelled "Incident history behind these rules," which is
the provenance citation CC-KNOW-3 permits. CG-12 (28 citations examined) finds
no `_bootstrap/` cited as a required source. F3 and F6 are defects *inside*
that lane's contents and pointers, not breaches of the lane boundary itself.

**`NORMATIVE-CHANGE-WORKFLOW.md` and `SEMANTIC-DELTA-TEMPLATE.md`.** Both are
sound. Every CC-* citation resolves. The failure-mode table (`:160-169`) does
something rare and correct: its last row explicitly marks itself
*"Policy-motivated, not an incident"* rather than borrowing the evidenced
rows' authority. The template's "quoting a defect must not reproduce it"
standing rule (`:132-148`) is a real hazard, correctly generalised from
syntax to claims. Both files' "what this does not do" sections are honest,
including "it has not been executed end to end" — which F2 now partially
confirms.

**Summary drift (charge question 6).** Beyond F9/F10: `ARTIFACT-INVENTORY`'s
18 cluster rows all reproduce at source, and `ACTIVE-AUTHORITY-MAP`'s rows are
accurate except F9. Neither is meaningfully drifted. The drift in this
repository is not in the summaries — it is in the **authority record they
summarise** (F1).

---

## Answers to the charge's six questions, directly

1. **Does any fact now have two authoritative homes?** **Yes — one, and it is
   the most consequential fact in the repository.** The four owner-act
   arguments live in both the acceptance record and their manifests, `AGENTS.md`
   names both as owners in one sentence, and all four now disagree (**F1**).
   *Craft binding rules:* no duplicate home — the nine banners restate the rule
   but INSTALL-RECORD owns it and the banners point at the act; the hygiene
   policy cites the cluster README's precedence rather than re-owning it.
   *Vocabulary:* no duplicate home — the registry cites throughout and
   explicitly disclaims authority; doctrine's frozen nouns and the RFC closed
   vocabularies remain the owners (one miscount, **F5**). *Budgets:* not two
   homes but **two instruments with no stated relationship** (**F4**).
   *Authority maps:* all three correctly labelled derived/presentation/procedure;
   one broken row (**F9**), one omitted caveat (**F15**).
2. **Term registry rigor:** all 30 entries carry all ten fields, zero gaps;
   all 58 clause citations resolve; 20+ verified at source for content with no
   misattribution; the five-dimension table is present, complete and
   internally consistent against all four source vocabularies; the admission
   rule is present with all four conditions. Defects: **F5** (miscount),
   **F12** (no declared field schema; one label deviation), **F13**
   ("counted by script" overclaims the method). **Five migration-report counts
   were requested; 22 were re-run and 21 reproduce exactly — see the sweep
   table. One does not (F8).**
3. **Hygiene policy rigor:** 16-item coverage table verified row by row
   against the charter; all `Extends:` citations resolve; no contradiction with
   an installed clause or doctrine found; all 22 violation examples genuinely
   violate their rules. One stale `[Observed]` bracket (**F11**).
4. **Lifecycle lanes and archive boundaries:** no candidate is citable as
   accepted by a careless reader; no historical material is on a default
   reading path; `AGENTS.md` does not route agents to history. Defects are in
   the lane *contents* (**F3**) and *pointers* (**F6**), and in one check's
   undisclosed class (**F14**).
5. **Context budgets:** `check_governance.py` run; CG-8 read; README (751 /
   1,200) and AGENTS (1,376 / 1,500) both under budget; seven module triggers
   reported, all report-only and all previously disclosed. No active artifact
   is absorbing history — the AGENTS "Notes to self" appendix was correctly
   moved out to PROCESS-LESSONS this round, which is the right direction.
   Finding **F4**.
6. **Summary drift:** verified 18 of 18 inventory rows and 5+ authority-map
   rows at source. Drift is minimal (**F9**, **F10**). The stale artifact is
   the acceptance record, not the summaries.

---

## Verdict

The two P-10 subjects — the term registry and the knowledge-hygiene policy —
are, on this examination, **good work that would individually clear an
EXCEPTIONS bar**: rigorously cited, honestly bounded, self-disclosing about
their own limits, and reproducible where they make measurable claims. Their
defects (F5, F8, F11, F12, F13) are all correctable without touching a rule or
an entry's meaning.

The vertical as charged also covers the repository structure, and there the
answer is different. The repository's single-home discipline has failed at its
highest-stakes point: every one of the four digest-bound owner-act arguments
in the record `AGENTS.md` designates as their single owner is stale, three of
the four are invisible to every check, and the routing file itself declares two
owners for that fact in one sentence. An owner following the repository's own
routing today would write four phrases that accept nothing. That is not an
exception to be carried past the gate — it is the repair the gate is waiting
on. F2, F3, F6 and F7 compound it: a blast radius under-stated in the first
live use of the change workflow, a tracked record asserting that candidate
material supersedes adopted doctrine, ten default-path pointers left behind by
a completed relocation, and the routed entry point for contract questions
carrying no derived label.

**REVISE**
