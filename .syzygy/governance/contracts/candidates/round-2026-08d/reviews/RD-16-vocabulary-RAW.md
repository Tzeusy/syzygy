(part 1/2)

# Reviewer: vocabulary (RD-16) / Date: 2026-08-09 / Commit: 771965c

**Files read (complete list).** `README.md`; `.syzygy/intent/OVERVIEW.md`; `PROJECT-STATUS.md`; `.syzygy/governance/doctrine/README.md`, `architecture.md`, `trust-and-evidence.md`, `v1.md` (partial: gap boundary, actuator sites), `vision.md` (partial: thesis, actuator sites), `security.md` (sweep only); `C/policy-candidates/TERM-REGISTRY.md` (in full); `C/rfcs/RFC-0007/README.md`, `narrative-contract.md` (sweep), `rendering-and-surface.md` (sweep); `C/rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md` (RFC10-1), `portfolio-and-cross-project-consent.md` (RFC10-15); `C/rfcs/RFC-0001-project-graph-identity-state-planes.md` (sweep); `C/rfcs/RFC-000{2,3,4,5,6,8,9,11}` package indexes (sweep); `C/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` (act 4 row); `C/COMPACTION-CHARTER.md` (headings); `C/round-2026-08c/PUBLIC-VOCABULARY-COMPREHENSION-REPORT.md`; `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md` (§2 charter, SDR-1/2); `scripts/check_governance.py` (CG-23). Excluded per instruction and not opened: `C/round-2026-08d/`, `C/reviews/`, `C/history/`, `_bootstrap/`.

**Verification performed.** `python3 scripts/check_governance.py` → `25 OK, 15 WARN, 0 FAIL (40 checks)` [Observed]. `sha256sum .syzygy/intent/OVERVIEW.md` → `01d629515993188338f6a0e2d84d67543d8569003759a7c8f571a90b129c7cd1`, matching act 4's quoted argument in the acceptance record exactly [Observed]. `TERM-REGISTRY.md` appears in **no** wave manifest and in **no** act row of the acceptance record (`grep -rn "TERM-REGISTRY" ACTIVE-CONTRACT-MANIFEST.txt wave-manifests/ FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` → 0 hits) [Observed] — so registry-internal repairs cost no digest re-quote, while `OVERVIEW.md` repairs do.

---

## 1. `Gap` and `Unknown` classify the same case in opposite ways — undisclosed inside the artifact

**Severity: blocking.**

T-31's boundary statement:

> *Gap* (T-20 — a gap is something intended and **known** to be absent; an Unknown is not knowing whether it is absent. Rendering an Unknown as a gap manufactures knowledge).

T-20's own example, forty lines earlier:

> **Example.** An adopted requirement with no verifying evidence at evaluation E is a gap at E. V0 surfaces the absence; V1 computes the gap (SDR-12, adopted).

An adopted requirement with no verifying evidence is precisely "not knowing whether it is absent." T-31 says that is an Unknown; T-20 says it "is a gap at E." [Observed]

Adopted doctrine sides with T-31. `doctrine/v1.md`:

> **The V0/V1 gap boundary:** V0 surfaces *absence* — a declared capability with no mapped evidence, code mapping to no declared capability — rendered as Unknown. V1 computes *gaps*: intent-vs-observed deltas as navigable, work-generating objects.

[Inferred] "a declared capability with no mapped evidence" and "an adopted requirement with no verifying evidence" are the same class — declared intent, no evidence — so T-20's example asserts as a present-tense gap the case doctrine renders Unknown.

Both terms are in the registry's core eleven, both are listed in §5 as adopted-anchored, and this is the pair on which VIS-2 rests. The registry does **not** disclose the conflict: §6 "What this registry does not establish" lists five limitations, none of them this one [Observed — §6 read in full]. The disclosure exists only in `round-2026-08c/PUBLIC-VOCABULARY-COMPREHENSION-REPORT.md` ("**could not separate**… It is **owner decision packet 5**"), which is not on any reading path a registry reader is routed to.

**Repair.** Either amend T-20's example so the no-evidence case reads Unknown and reserve *gap* for a known-absent declaration, or amend T-31's cross-reference — and, whichever way it goes, state the open question **inside both entries**, since a defect visible only from a round report is not disclosed to the artifact's readers.

---

## 2. `Reconciliation` is used on the default path in the sense its own entry reserves against — twice in one file, in two senses

**Severity: blocking (for the overview offering).**

T-26, formal definition:

> **Unqualified "reconciliation" means exactly one thing in Syzygy: the post-merge evaluation of whether a merged change satisfies the intent revision that warranted it.**

`OVERVIEW.md:45–47`:

> Execution state never substitutes for either of the others. The computed
> difference between desired and observed becomes **reconciliation work**, and
> agent fleets are the actuators that perform it.

and `OVERVIEW.md:54`: `    Diff["Reconciliation work"]`.

That names the *desired-vs-observed difference* — a pre-merge object. The same file then uses the reserved sense correctly at `:176–178`:

> Every merged change enters a reconciliation chain and stays visibly
> **reconciliation-pending** until checked against the exact intent revision
> that warranted it.

So one artifact carries both senses, and its Drawer 2 attributes only the second to RFC-0002 [Observed]. `README.md` contains **zero** occurrences of `reconcil*` (full-file sweep) and names the same diagram node honestly: `O --> G[Difference<br/>gaps · contradictions · Unknowns]`.

CG-23 cannot see this: `Reconciliation` is a **core** term, and CG-23 examines only the advanced set (see finding 5). The registry itself says "a core term used loosely is worse than an advanced term used precisely" — and the only mechanical test of the bound is blind to exactly that class.

**Repair.** Replace the pre-drawer noun. `README.md`'s "Difference" already works, and doctrine uses the same bare phrase — `vision.md`: "Syzygy computes and shows the difference, and harnesses the existing actuator toolchain to close it." Cost: a digest re-quote of act 4 (the record has re-quoted twice already, 2026-08-05 and 2026-08-05b, and documents how).

---

## 3. There is no term for "the difference between desired and observed" — and the registry does not record that

**Severity: major.**

Sweep denominator: the registry's 31 entries (T-01…T-31, headings enumerated by script), doctrine's 13 frozen nouns (`architecture.md`, "Vocabulary": *project, capability, gap, contradiction, evidence, warrant, aligned, converged, genome-complete, genome, snapshot, evaluation, observation record*), and the doctrine glossary's 7 bullets. **No entry in any of the three names the aggregate.** [Observed]

The nearest is `Gap` (T-20), which names a strict subset:

> **Formal definition.** Compatible desired state not yet realized in observed state — the intent-vs-observed, work-generating delta.

*Compatible* excludes contradictions, and T-31 excludes Unknowns — the other two members of README's own "gaps · contradictions · Unknowns". The concept the narrative reaches for has no term, which is why `OVERVIEW.md` borrowed a reserved one (finding 2). §6's list of what the registry does not establish does not record this.

**Repair.** Either admit a term under §3's five conditions, or record in §6 that the aggregate is deliberately unnamed and that plain "the difference" is the sanctioned phrasing (doctrine already uses it).

---

## 4. The default path's vocabulary routing resolves 1 of the 11 core terms

**Severity: major.**

`README.md:92–95` makes a single, exclusive routing promise:

> **Unfamiliar word?**
> [`.syzygy/governance/doctrine/README.md`](…)
> holds the glossary — the only one in this repository, and the one doctrine
> means when it says "README glossary". This file has none.

The doctrine glossary has **7 bullets**: *Syzygy · Owner · Governed project · `.syzygy/` and `openspec/` · Polaris / Trajectory / Orrery · OpenSpec · Rule identifiers* [Observed, counted by script]. Against the registry's core eleven (*Project, Capability, Desired state, Observed state, Execution state, Evidence, Unknown, Gap, Contradiction, Reconciliation, Mission*), it resolves **one** — `Project`, and only under a different head word (`Governed project`). Ten of eleven return nothing. `README.md` contains **zero** links to `TERM-REGISTRY.md` [Observed, `grep -c`], so the artifact that does hold those ten is unreachable from the page that promises the answer.

**Repair.** Either narrow the promise ("the glossary covers governance vocabulary; the term registry covers kernel vocabulary — candidate") or route the reader to both. As written, the sentence's exclusivity ("the only one") converts a partial index into an apparent complete one.

---

## 5. The registry's leak census understates both classes, and CG-23 cannot support the claim made for it

**Severity: major.**

The registry states:

> **The bound is testable, it is tested every run, and it currently fails.**

and enumerates:

> Two classes of leak are known and neither is exempted:
> - **Advanced terms used on the default path**, which CG-23 names. Both current hits sit inside act 4's digest subject…
> - **Terms used on the default path with no entry here at all** — *kernel*, *surface*, *workspace*, *actuator*.

Three problems, each measured:

**(a) CG-23 misses inflected and line-wrapped forms.** Its matcher is `re.compile(r"\b" + re.escape(name) + r"\b", re.I)` over the pre-drawer body. Running it myself against `OVERVIEW.md`'s default-path body: `\bProject Genome\b` → **False**, `\bProject\s+Genome\b` → **True** — the source reads `its **Project\nGenome**`, so advanced term T-03 is present and unreported [Observed]. Two more advanced terms are present and unreported for the same class of reason: `Diff -->|warranted work| Fleet` (`OVERVIEW.md:58`, T-17 — `\bWarrant\b` does not match *warranted*) and "an explicitly approved **Mission** envelope" (`OVERVIEW.md:93`, T-28 — whose entry permits the bare alias only "after first use", and the full form never occurs). So "**Both** current hits" is a census of what one regex sees, presented as a census of what exists. CG-23's own header prints `40 term-in-files examined, 2 findings` — 20 advanced terms × 2 files, the whole denominator.

**(b) CG-23 exempts core terms by construction**, so finding 2 — the worse defect by the registry's own ranking — is structurally invisible.

**(c) The four-item enumeration understates the round's own count.** `round-2026-08c/PUBLIC-VOCABULARY-COMPREHENSION-REPORT.md` records **fifteen**: "`surface` · `kernel` · `plane` · `workspace` · `actuator` · `experience` · `owner act` · `gate` · `evidence bar` — and six more it enumerates." My independent sweep of the default path (denominator: `README.md`, 129 lines / 834 words, plus `OVERVIEW.md` lines 1–142, 884 words — the registry's own definition of the path) confirms all of `surface` (13×), `kernel` (3×), `workspace` (3×), `actuator` (2×), `experience` (1×, `README.md:40` `## The four experiences`), `projection` (2×), `control plane` (1×), `gate` (7×), `owner act` (2×), `evidence bar` (2×) — none with an entry in the registry or the glossary [Observed].

**Repair.** Widen the matcher to `\s+` for multi-word terms and to stems for inflected ones; state CG-23's blind spots (core terms, no-entry terms) in the same paragraph that calls the bound "tested every run"; and replace the four-item list with the recorded fifteen or a pointer to the enumeration, since a shorter list in a later artifact reads as a repair that did not happen.

---

## 6. The registry contradicts itself about its own size, in two directions

**Severity: major.**

Counted by script: **31** entries, `#### T-01 … T-31` [Observed]. The banner and §5 agree — "none of its **31 entries** acquires force"; "Counted by script over the **31 entries** above, not by hand". §6 does not:

> It records what the **30 listed terms** mean and who owns each meaning.
> **No newcomer comprehension test has been run** on any of the **30 entries**.

And §5's own arithmetic fails:

> **Eighteen** of this registry's **thirty-one** terms sit outside the frozen list (**twelve** correspond to a frozen noun: ten by exact name plus *Project Genome*→genome and *Source snapshot*→snapshot; the frozen *genome-complete* has no registry entry of its own).

31 − 12 = **19**, not eighteen. I verified the twelve by hand: ten exact-name matches (Project, Capability, Gap, Contradiction, Evidence, Warrant, Aligned, Converged, Evaluation, Observation record) plus the two named mappings [Observed].

`round-2026-08c` claims this class was closed — "thirty entries where a script counts thirty-one… **All are corrected**". Two instances of "30" and one arithmetic contradiction survive at this commit. This is the volatile-derived-value class the corpus's own verification rule 3 exists to catch, inside the artifact written to fix that class elsewhere.

**Repair.** Compute all four self-counts (entries, core, outside-frozen, corresponding-to-frozen) or delete them; a count of one's own contents is a derived value.

(part 2/2)

## 7. The registry's own naming resolution for T-16 is not applied inside the registry

**Severity: major.**

T-16 records the conflict and rules on it:

> The registry does not get to choose: the majority name leads here, the minority name is recorded as a synonym, and **which one the corpus adopts is an open question for the owner**

Occurrence counts inside `TERM-REGISTRY.md`: *rendering tier* **5**, *evidence tier* **9** [Observed]. The minority name leads in the most-cited place in the file — §1's five-dimension table:

> | **Evidence tier** | *How strongly does the evidence support the claim?* |

and in the §1 rule's own list of dimension names ("*state plane*, *epistemic label*, *evidence tier*, *work lifecycle state*, *governance lifecycle state*"), and in three "Related but distinct" cross-references (T-06, T-14, T-15). A reader who meets the dimension in §1 and the entry in §4 meets two names, with the entry declaring the one §1 uses to be the demoted synonym.

**Repair.** Apply the ruling: *rendering tier* in §1's table, the rule, and all three cross-references; keep *evidence tier* only in T-16's parenthetical, alias line, and conflict note.

---

## 8. `Mission Control` — three strengths of the same negation, and a core term borrowed for it

**Severity: major.**

Owning clause, RFC10-1:

> Mission Control is a **workspace-level operator domain**, not a fourth project-specific truth surface.

`README.md:47` (table cell, unqualified):

> | **Mission Control** | workspace-level operator capability — **not a fourth surface** | …

`README.md:50–52` (prose, qualified — and disagreeing with its own cell):

> Mission Control is a workspace-level operator capability, not a fourth project truth surface

`OVERVIEW.md:85–86` (unqualified, and stronger than the clause its Drawer 2 cites for it):

> And one thing that is *not* a surface: **Mission Control**, a **workspace-level operator capability** spanning projects

Three readings: *not a surface* / *not a fourth surface* / *not a fourth project-specific truth surface*. Only the third is the clause. `README.md` holds two of them, seven lines apart. [Observed]

Compounding it: both default-path artifacts substitute **capability** for the clause's **domain**, and `Capability` is core term T-04 — "A named unit of declared behavior that the project's own spec or shape documents assert exists" — a project-scoped identity. Applying it to a workspace-level object is the core-term-used-loosely case §1 ranks as the worse defect. And the section heading `## The four experiences` groups Mission Control with the three surfaces under a collective noun with no entry anywhere, against doctrine's `## One kernel, three surfaces`.

**Repair.** Copy RFC10-1's noun and its exact negation into both files; retire "experiences" or define it in place.

---

## 9. `workspace` carries at least three referents and has no entry — while being listed as a deprecated synonym

**Severity: major.**

T-01 deprecates it: "*repo*, *codebase*, *workspace* — a workspace is a set of projects and is a distinct, portfolio-level concept (RFC10-15, candidate)." That distinct concept gets no entry of its own. Referents found, each quoted:

- a scope — "workspace-level operator capability" (`README.md:47`, `OVERVIEW.md:86`);
- an authority store — "lives in a typed, platform-level **workspace governance store**" (RFC10-15);
- personal presentation state — "distinct from the presentation-only workspace manifest (which remains personal presentation state, RFC 0003)" (RFC10-15).

`workspace` has **0 occurrences in the entire adopted doctrine tree** (6 files, swept case-insensitively) [Observed — confirming the registry's own claim].

**Repair.** Admit an entry under §3, or apply the registry's own recommended substitution ("*portfolio workspace* defined inline") on the default path. As it stands the word is simultaneously deprecated, undefined, and load-bearing on the public path.

---

## 10. Ambiguous `status` — sample frame and result

**Severity: minor.**

**Sample frame (stated):** the default reading path (`README.md`, `.syzygy/intent/OVERVIEW.md`, `PROJECT-STATUS.md`) plus every contract package index — `C/00-README.md`, `C/README.md`, and all 11 RFC package indexes: **16 files, 83 occurrences of the word**, of which 25 are structural (field key, banner, or table column) [Observed].

Structural uses resolve cleanly in 23 of 25: `status_source: owner-act-record` (×11) and `**Status:** Proposed foundational contract` (×11) are governance-lifecycle and qualified by their value; RFC-0001's 26 prose uses are uniformly claim-status ("All positive status flows through Claims", RFC1-24). The two table columns do not:

- `README.md:77` — `| Question | Authority | Status |` — rows 1–5 carry governance-lifecycle values (**Adopted**, **Recorded**, **Owner-approved**, **Candidate — accepted by no act yet**, **Candidate**); rows 6–7 carry existence facts (`Does not exist yet`, `Nothing exists yet`). Two domains under one column headed only `Status`.
- `PROJECT-STATUS.md:24` — `| # | Gate | Status | Owning record |` — mixes governance lifecycle (✅ **Adopted**, ⏳ **Candidate**) with `⛔ **Not started** — blocked on the wave acts`. `blocked` is a value of the **work lifecycle** in §1's closed thirteen.

§1's rule is explicit: "A field, column, count, badge, filter, or API key named only `status` is a defect wherever more than one of these five could be meant." Sharper still: neither table's actual domain — *does this artifact exist / has this gate fired* — is any of the five. The five-dimension closure has no dimension for the one the corpus's own front page needs.

**Repair.** Rename both columns (`Gate state`, `Authority state`), or add a sixth dimension to §1 and name it.

---

## 11. Terms used normatively before any reachable definition, on both default paths

**Severity: minor.**

`README.md` is one page with no drawer; every term is either defined in place or not at all. Defined in place and adequate: *desired/observed/execution state* (`:27–30`), *Unknown* (`:38`). Used with no definition in place and none at the glossary the page routes to: `control plane` (`:3`, the first five words of the project's self-description), `surface` (`:44`), `kernel` and `projections` (`:49`), `workspace` (`:47`), `experiences` (`:40`), `adapters` (`:61`), `gaps` and `contradictions` (`:60`) [Observed].

`OVERVIEW.md` places its definitions of *evidence*, *Unknown*, *evaluation*, *contradiction vs gap*, and *reconciliation* inside Drawer 1 — after the sentence "**Everything past this point is optional drill-down**" (`:139–140`). Pre-drawer, and therefore in non-optional text: `actuators` (`:47`), `reconciliation work` (`:46`), `evaluation engine` (`:65`), `warranted work` (`:58`), `Mission` envelope (`:93`), `evidence bar` (`:94`), `Project Genome` (`:105`). A reader who takes the file at its word never reaches the definitions.

**Repair.** Either move the four or five load-bearing definitions above the drawer boundary, or drop the terms from the argument in favour of the ordinary-language forms the registry itself prescribes.

---

## 12. Dangling citation: "§10.2 of the closure charter"

**Severity: minor.**

> §10.2 of the closure charter proposes the plain-language replacement for each, and the proposal is routed to the owner rather than applied here.

Sweep denominator: every `.md` under `C/` excluding `round-2026-08d/`, `reviews/`, `history/` — **zero** files contain the string "closure charter" and **zero** self-describe as one [Observed]. The artifact that actually carries the substitutions is named correctly in the *next* paragraph (`../round-2026-08c/PUBLIC-VOCABULARY-COMPREHENSION-REPORT.md`), and its headings are unnumbered, so there is no §10.2 to reach. `COMPACTION-CHARTER.md` — the only "charter" at `C/` root — has no §10.2 and does not discuss vocabulary substitution.

**Repair.** Delete the first pointer or replace it with the file the second one names.

---

## 13. Registry hygiene: one duplicated definition, one silent cross-reference, three plain-language lines that need a second Syzygy term

**Severity: minor.**

- **Duplicated definition.** `Unknown` is formally defined twice — T-15 ("**Unknown** — a claim that is neither evidence-backed Observed nor valid Inferred, including one whose evidence is missing, inaccessible, or stale") and T-31 (near-verbatim). The 2026-08-06 correction note explains why both entries exist (dimension vs value) but does not say which carries the definition of record.
- **Asymmetric boundary.** T-19 spells out its boundary with Gap ("the distinction is load-bearing… No surface, count, endpoint, or UI string may merge the two"); T-20's line reads only "Contradiction (T-19); Work item (…); **Unknown**." A reader arriving at `Gap` — the more likely entry point — learns nothing of the boundary that finding 1 turns on.
- **Circularity against §3(4).** §3 requires "a one-sentence plain-language explanation a competent engineer unfamiliar with Syzygy understands **without needing a second Syzygy term**." T-06: "Which of six kinds of assertion a record is making — assigned fresh at every evaluation, and never asked of a relation." T-13: "The one and only carrier of **status** in Syzygy" — the exact bare word §1 forbids where the dimension matters. T-16: "How strong a **claim's** backing is — six closed values, each living inside one of the three **labels**." §6 discloses the cause ("The admission rule (§3) was applied to no incumbent term"), so this is recorded rather than hidden — but the entries are what a newcomer reads.
- **Restatement drops a condition.** Doctrine's glossary: "**Governed project** — … explicitly brought under Syzygy observation; additional repositories are declared observed-source repositories, read-only to Syzygy unless separately onboarded, and **every observed repository requires consent** (architecture.md; security.md SEC-4)." T-01's formal definition carries the read-only clause and drops the consent condition. The banner's "owning authorities always win" covers it, but a SEC-4-bearing condition is a poor thing to lose in a restatement.

---

## 14. `Trajectory`'s one-line charter differs between the two default-path artifacts, and neither matches the recorded charter

**Severity: minor.**

`README.md:45` — "| **Trajectory** | the work surface | What is being done, by whom, under what authority? |"
`OVERVIEW.md:82` — "| **Trajectory** | the work surface | What remains, what runs, what merged *without yet being reconciled*? |"
`SURFACE-DECISION-RECORD.md` §2 — "**Trajectory — Work.** The owner's account of what remains, what is planned, what is active, what is blocked, what changed, what it cost, and why the work exists".

`Polaris` and `Orrery` agree across all three. Trajectory does not: `OVERVIEW`'s is a compression of the charter; `README`'s substitutes an authority/actor framing the charter does not contain. Neither is authority, so nothing is violated — but two default-path artifacts give one surface two different one-line charters.

**Repair.** Compress the charter once and use the same compression in both files.

---

## Scope note on repair cost

Findings **6, 7, 12, 13** and the registry half of **1, 3, 5** touch `TERM-REGISTRY.md` only, which no act's digest binds [Observed] — they are free to fix now. Findings **2, 8, 11, 14** touch `OVERVIEW.md`, whose bytes act 4 binds at the digest I verified above; fixing them costs a re-quote, which is the owner's call and not an agent's. Finding **4** and the `README.md` half of **8** and **10** touch `README.md`, which no act binds.

If the owner declines to re-quote act 4, findings **2, 8** (`OVERVIEW` side), **11** (`OVERVIEW` side) and **14** are the ones that would have to be named and knowingly bound. Findings **1, 6, 7, 12** cannot be carried that way: they are internal contradictions and a broken pointer in an unbound artifact, and an offering that carries them asks the owner to accept a registry that disagrees with itself about its own size, its own chosen name for a dimension, and — on the pair VIS-2 rests on — its own boundary.

VERDICT: REVISE
