# Vocabulary and overview repairs — semantic delta record

> **Process record. Never authority, and it adopts nothing.** It records every
> change of meaning made while discharging the round-2026-08d dispositions
> `repair-record(R-REC)` for review **RD-16** (vocabulary, `VERDICT: REVISE`)
> and `repair-record(R-OVW)` for RD-16 plus **RD-10 finding F14**. Every edit
> below lands in **candidate** bytes and is ratified or reverted by the owner
> at the act that binds each artifact. "Editorial" and "no semantic change"
> are reviewable claims here, not labels.

**Baseline.** The reviews are bound to commit `771965c`; this pass ran at
`e69c923` plus the working tree. Two artifacts were edited:

| Artifact | Bound by an act? | Consequence |
|---|---|---|
| `policy-candidates/TERM-REGISTRY.md` | **No.** It appears in no wave manifest and in no act row of the acceptance record (RD-16 verified this by sweep) | Repairs cost no digest re-quote |
| `.syzygy/intent/OVERVIEW.md` | **Yes — act 4, not performed** | **Every edit below moves act 4's digest.** The acceptance record's act-4 argument must be re-quoted from the file by its own generator before the act is offered; verify with `check_governance.py` CG-7 |

Two files were **created**: `policy-candidates/DOCTRINE-AMENDMENT-ACTUATOR-DEFINITION.md`
and this record. One file received a **two-paragraph cross-reference only**:
`policy-candidates/DOCTRINE-EDITORIAL-AMENDMENT-GLOSSARY-CITATION.md`.

**On act 4's digest.** RD-16 verified the pre-repair bytes as the now-stale
`01d6295159…`, matching the argument the acceptance record then quoted. Those
bytes no longer exist. **This record deliberately states no replacement
digest** — a digest quoted outside its owning artifact goes stale silently
(verification rule 3), and the record's generator owns act 4's argument.
Editing before the act is lawful and is the cheapest moment the repair is
available; editing *after* would not be (rule 10; "never edit an artifact
after an act has bound its digest").

---

## Part 1 — findings discharged

| Finding | Repair, in one line | Where |
|---|---|---|
| **RD-16 f1** *(blocking)* | T-20's example corrected to doctrine's answer — no evidence → **Unknown**, evidence of non-satisfaction → **Gap** — and the conflict disclosed **inside both entries**, pointing at P-36 | registry: T-20, T-31, §6 |
| **RD-16 f2** *(blocking for act 4)* | The pre-drawer noun `reconciliation work` retired; the desired-vs-observed object is now "the **difference** … gaps, contradictions, and Unknowns", as doctrine and `README.md` already phrase it | OVERVIEW `:45`, mermaid `:54` |
| **RD-16 f3** | §6 records that the aggregate is **deliberately unnamed** and that plain "the difference" is the sanctioned phrasing | registry §6 |
| **RD-16 f4** | Registry half: the routing gap stated in the tiering section — the doctrine glossary resolves 1 of the 11 core terms, and `README.md` links here nowhere. **README half is a handoff** | registry §tiering |
| **RD-16 f5** | Census rewritten three ways: CG-23's blind spots named in the same paragraph that calls the bound tested; the four-item list replaced by a **pointer** to 08c's recorded fifteen (never a transcription); the "neither was edited" sentence superseded. **CG-23 matcher widening is a handoff** | registry §tiering |
| **RD-16 f6** | All four self-counts recomputed 2026-08-10; the failed arithmetic (*eighteen* against 31 − 12) restated **range-free** as "every other entry"; the "counted by script" claim replaced with what actually recomputes them — nothing yet | registry §5 |
| **RD-16 f7** | T-16's own ruling applied: **rendering tier** leads in §1's table, §1's rule, and all three cross-references (T-06, T-14, T-15) and T-27's example; *evidence tier* survives only in T-16's heading parenthetical, conflict note, and alias line | registry §1, T-06/14/15/27 |
| **RD-16 f8** | RFC10-1's noun and its **exact** negation copied into OVERVIEW: "not a fourth project-specific truth surface … a workspace-level operator **domain**". **README half is a handoff** | OVERVIEW `:85` |
| **RD-16 f9** | `workspace`'s three referents recorded under T-01 with the two-sided disposition; the inline definition applied on the default path; entry admission left to P-16/P-17 | registry T-01; OVERVIEW `:85` |
| **RD-16 f10** | §1 records the sixth question the five dimensions do not answer (*does this exist / has this gate fired*) and names the two column renames. **Both columns are handoffs** | registry §1 |
| **RD-16 f11** | Every pre-drawer term used before definition either removed or defined in place: *actuators*, *reconciliation work*, *evaluation engine*, *warranted work*, *Mission envelope*, *evidence bar*, *Project Genome* | OVERVIEW, seven sites |
| **RD-16 f12** | The dangling "§10.2 of the closure charter" pointer deleted; the enumeration now points at the file that actually holds it | registry §tiering |
| **RD-16 f13** | Four hygiene defects: definition-of-record named for `Unknown` (T-31, with T-15 pointing at it); T-20's Gap/Contradiction **and** Gap/Unknown boundaries spelled out from the Gap side; three plain-language lines rewritten term-free (T-06, T-13, T-16); T-01's dropped **SEC-4 consent condition** restored | registry, five sites |
| **RD-16 f14** | OVERVIEW's Trajectory one-liner replaced with the **same compression `README.md` now carries**, derived from SDR-2's charter — what remains, what is running, what changed, what it cost, whether the result has been verified against intent, never satisfied by an issue list | OVERVIEW `:82` |
| **RD-10 F14** (overview half) | The quadruple routed to RFC8-28's wording, restoring *merged but not yet evaluated* — the state RFC8-29 makes V0's honest answer — with its V0 rendering stated | OVERVIEW Drawer 1 |
| Owner charter §8.5 | Default-path language: *kernel* → **shared project model** (one-time "(the *kernel*, in the technical contracts)"), *evaluation engine* → plain rendering, *portfolio workspace* defined inline, `Claim` and `Evaluation` leaks removed, `Project Genome` moved to Drawer 2. *surface* was **kept**, with the denominator: `\bsurfaces?\b` finds **8** pre-drawer uses — one is the ordinary English verb ("underspecification *surfaces* at the most expensive moment"), and the other seven are the literal product distinction (the three surfaces' proper names, their table, the two-consumers sentence, and RFC10-1's negation), which the charter exempts | OVERVIEW, six sites |

---

## Part 2 — semantic deltas, stated as deltas

### V-1 — `Gap` and `Unknown` no longer classify one case two ways *(registry; meaning changed)*

**Old meaning.** T-20: an adopted requirement with no verifying evidence "is a
gap at E". T-31: a gap is something *known* to be absent; not knowing whether
it is absent is an Unknown. One case, two opposite classifications, in the
pair VIS-2 rests on, disclosed in neither entry.

**New meaning.** No evidence → **Unknown**. Evidence establishing
non-satisfaction → **Gap**. T-20's example now reads that way and both entries
carry the disclosure.

**Why.** Adopted doctrine decides it: VIS-2, and `v1.md`'s V0/V1 gap boundary
("V0 surfaces *absence* … rendered as Unknown. V1 computes *gaps*"). T-31 was
already on doctrine's side; T-20's example was not.

**What is *not* claimed.** This is not a ruling. `Gap` is defined **nowhere in
force**. The two-term rule is queued as **P-36**
(`decisions/UNKNOWNS-AND-GAPS-DECISION.md`), which ratifies or reverts this
drafting — and that packet already anticipates this repair by name.

### V-2 — `reconciliation` reserved sense restored on the default path *(OVERVIEW; meaning changed — moves act 4)*

**Old meaning.** "The computed difference between desired and observed becomes
**reconciliation work**" named a *pre-merge* object with the word T-26 reserves
for the *post-merge* evaluation. The same file used the reserved sense
correctly in Drawer 1, so one artifact carried two senses.

**New meaning.** The pre-merge object is "the **difference** … gaps,
contradictions, and Unknowns". Only the post-drawer use is *reconciliation*,
in T-26's sense.

**Why.** T-26's reservation is hard ("means exactly one thing in Syzygy"),
`README.md` already names the same node honestly, and doctrine uses the bare
phrase. **No new term was minted** — see V-4.

### V-3 — Mission Control's negation has one strength *(OVERVIEW; meaning changed — moves act 4)*

**Old meaning.** "one thing that is *not* a surface … a **workspace-level
operator capability**" — a negation stronger than RFC10-1's, using **Capability**,
which is core term T-04 and project-scoped, for a workspace-level object.

**New meaning.** RFC10-1's own noun and negation: "not a fourth
project-specific truth surface … a workspace-level operator **domain**".

**Why.** Copying the clause is the only way three artifacts stop reading three
strengths. `README.md` still carries two of the three and is not edited here.

### V-4 — the unnamed aggregate is recorded as unnamed *(registry; disclosure added, no term minted)*

The corpus has no term for "gaps · contradictions · Unknowns taken together".
§6 now says so and sanctions the plain phrase. **No term was admitted**: §3's
five conditions include a fresh-reader distinction test the proposing party
cannot run, so minting one here would violate the registry's own rule while
repairing it.

### V-5 — `Mission` envelope and `evidence bar` defined in place *(OVERVIEW; clarifying — moves act 4)*

**Old.** "an explicitly approved **Mission** envelope — objective,
permissions, budget, time, evidence bar, stop and escalation conditions —
which they can never widen." `Autonomy envelope` (T-28) and *evidence bar*
were both load-bearing and undefined pre-drawer.

**New.** The bounds are named as bounds and the evidence bar is glossed
inline; "Widening any of them is a human act" restates T-28's no-self-widening
rule rather than dropping it. *Claim:* **no obligation changed** — the
envelope's content list is the same list.

### V-6 — the reconciliation quadruple matches RFC8-28 *(OVERVIEW; meaning changed — moves act 4)*

**Old.** *reconciled-with-evidence · Unknown(reason) · unsatisfied ·
contradiction-raised* — a partition that drops **merged, not yet evaluated**,
the state RFC8-29 makes V0's honest answer for all merged work.

**New.** RFC8-28's four, with the V0 rendering of the second stated.

**Why.** RD-10 F14: two "the four"s over one six-value chain, and the one an
owner reads first dropped the V0 answer.

### V-7 — four registry self-counts recomputed, one restated range-free *(registry; corrects a false figure)*

31 entries, 11 core, 12 corresponding to a frozen doctrine noun; therefore
**every other entry** — nineteen at this recompute — sits outside the frozen
list. The old sentence said *eighteen*, which fails its own arithmetic.
Per **X7**, the surviving formulation avoids the figure where it can, and the
section now states plainly that **no check recomputes these** and that any
such figure quoted elsewhere is stale by default.

### V-8 — the leak census stops overstating its instrument *(registry; corrects a claim)*

**Old.** "The bound is testable, it is tested every run"; "**Both** current
hits"; four no-entry terms; a pointer to a "closure charter §10.2" that does
not exist.

**New.** The bound is *partly* testable; CG-23's three blind spots are named
beside it; the no-entry class points at 08c's recorded fifteen and copies
nothing; the dangling pointer is gone. *Claim:* nothing here weakens the
bound — it stops a regex census being read as a census of what exists.

### V-9 — T-01 regains its SEC-4 consent condition *(registry; restores a dropped condition)*

Doctrine's glossary requires consent for **every** observed repository; T-01's
restatement carried the read-only clause and dropped the consent one. Restored
with its citation. *Claim:* this restores adopted meaning; it adds nothing.

### V-10 — `actuator` gets a doctrine home proposed, not a registry entry *(new candidate packet)*

`DOCTRINE-AMENDMENT-ACTUATOR-DEFINITION.md` proposes the exact glossary bullet
defining *actuator* / *actuator toolchain*, derived from the four adopted
sites that use the word. **It adopts nothing — doctrine is owner-only,
VIS-4.** It composes with the P-25(a) citation packet (cross-referenced in
both headers) and takes up one of the three terms that packet lists as
deliberately unfixed. The registry admits **no** entry; the default path stops
using the word instead. The packet's one inferred sentence — that "agent
toolchain" and "actuator toolchain" name the same role — is flagged inside it
as the sentence to press on.

---

## Part 3 — handoffs (not edited here; outside this pass's file boundary)

| # | What | Why it is someone else's |
|---|---|---|
| H-1 | **Root `README.md`, the "only glossary" promise** (RD-16 f4). Either narrow it ("the doctrine glossary covers governance vocabulary; the candidate term registry covers kernel vocabulary") or route the reader to both. As written, an exclusivity claim converts a 7-bullet partial index into an apparent complete one, while ten of the eleven core terms live in an artifact `README.md` never links | `README.md` is R-REC's, not this pass's |
| H-2 | **Root `README.md`, Mission Control** (RD-16 f8). Its table cell says "not a fourth surface" and its prose seven lines later says "not a fourth project truth surface"; both substitute **capability** for RFC10-1's **domain**. `OVERVIEW.md` now carries the clause's wording; until README does, two of the three strengths remain | same |
| H-3 | **`check_governance.py` CG-23's matcher** (RD-16 f5a). Widen multi-word terms to `\s+` and inflected forms to stems, per the disposition register's `R-SCR` route. **Before doing so, read H-4** | `scripts/` is R-SCR's |
| H-4 | **What a widened CG-23 would find in `OVERVIEW.md`: nothing.** [Observed] A whitespace-flexible, stem-tolerant sweep of the repaired file over all **20** advanced terms returns **zero** hits — the three the current matcher misses at baseline (`Project Genome` line-wrapped, `Warrant` via *warranted*, the bare `envelope` alias) are all gone, the last of them moved rather than hidden (see Part 4). Under the same sweep `README.md` returns one hit, `Claim` — the pre-existing enumerated ordinary-English exemption, not a new leak. So the widening is safe to land against these two files as they now stand; a **defined-in-place** use will still read as a leak to it, which is the third blind spot to design for | same |
| H-5 | **Two `Status` columns** (RD-16 f10): `README.md`'s authority table and `PROJECT-STATUS.md`'s gate table each mix governance-lifecycle values with a domain that is none of the five dimensions. Suggested renames: `Authority state`, `Gate state` | both files are R-REC's |
| H-6 | **Act 4's argument must be re-quoted** by the acceptance record's generator before the overview act is offered — scripted, never transcribed | the acceptance record is the lead's |
| H-7 | **P-25(c)** should be added to `decisions/PENDING-OWNER-DECISIONS.md` beside P-25(a)/(b), pointing at the new packet. This pass created the packet but did not edit the pending register | the pending register is R-REC's |
| H-8 | **CG-16 flags a verbatim quotation of its own headline.** [Observed] Its negation exemption requires the negator adjacent to the claim word (`\b(not\|never\|un\|no\|candidate)\b\W{0,14}`), and its headline puts three words between them — so any record storing CG-16's output verbatim fails CG-16. Two shapes are available: widen the exemption to allow intervening words, or add the check-output pattern to `VERBATIM_SOURCES`-style handling. Neither is done here | `scripts/` is R-SCR's |

## Part 4 — verification run at the end of this pass

`python3 scripts/check_governance.py`, the two blocks this pass is
accountable for. Read as **output**, not exit code (verification rule 4).

**CG-16 — `OK`, 0 findings** over the mentions it examined. Its headline is
described here rather than pasted, and the reason is itself a finding: CG-16
scans every file naming the registry for a claim word within a 90-character
window, and **its own headline contains one**. Its negation exemption matches
only an adjacent negator (`\W{0,14}`), so the headline's own "never … as
accepted" does not exempt it — pasting the line verbatim into this record made
CG-16 **FAIL on this record**. Recorded as **H-8**. This pass did not edit a
check to accommodate its own paperwork.

```text
WARN  CG-23  default-path vocabulary reported — 40 term-in-files examined, 0 findings — report-only — the core set is candidate, so this is the registry's own bound reported, not enforced
        [ordinary-English use, exempt] README.md — `Claim` (T-13) 1× — "No claim of alignment, convergence, or regeneration capability" (README.md:118) — the ordinary verb-shaped noun, not the kernel's positive-status carrier. An earlier revision of this exemption misquoted the very line it exempts; review RD-3 caught it in passing, and nothing here verifies the quotation mechanically
```

CG-23 was **2 findings** before this pass (`Claim` ×2 and `Evaluation` ×1, all
in `intent/OVERVIEW.md`) and is **0** after; the remaining line is the
pre-existing enumerated `README.md` exemption, which is printed, not a
finding. **This is the bound CG-23 can see**; what it cannot see is H-3/H-4
and is now disclosed inside the registry itself.

**One repair inside this pass was made *because* of that seam, and is recorded
rather than quietly done.** An intermediate draft glossed **Project Genome**
in place pre-drawer, which the registry's bound permits ("defining it in
place") but CG-23 cannot detect — it reported the compliant use as a leak the
moment a line rewrap brought the two words onto one line. The two dishonest
answers were available and both were refused: re-wrapping the line to hide the
term from the regex, and adding a checker allowlist entry for a use its
allowlist is not for. The term was moved to Drawer 2 instead and the argument
now carries the plain phrase, which is the registry's own first rule.

Other checks in the battery moved during this pass for reasons **outside** it
— concurrent script and fixture work by other agents was landing in the same
tree — so no repository-wide claim is made here, and none should be read from
these two blocks.
