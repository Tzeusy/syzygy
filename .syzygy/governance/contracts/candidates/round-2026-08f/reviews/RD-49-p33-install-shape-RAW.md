# RD-49 — P-33 semantic installation options (round-2026-08f, frozen commit `e2efda6`)

> **Provenance banner, added by the recording session — everything below the
> rule is the reviewer's raw output, copied verbatim and unedited.** The
> verdict word is copied exactly.
>
> | | |
> |---|---|
> | **Charter role** | §14 review 3 — the P-33 arm space, its costs, and whether an owner can rule from the packet |
> | **Dispatched** | 2026-08-11 |
> | **Subject commit** | `e2efda6` — bytes frozen; nothing in the subject was edited between dispatch and this record |
> | **Subject files** | `decisions/WAVE-A-INSTALL-SHAPE-DECISION.md`; `round-2026-08f/P33-SEMANTIC-INSTALL-ANALYSIS.md` |
> | **Context** | fresh — subject, governing references and acceptance criteria only |
> | **Model family** | same family as the corpus authors. Supports repair; **is not the formal launch administration** (charter §2.15) |
> | **Verdict** | `REVISE` — with three findings the reviewer marks **BLOCKING** |
>
> **Disposition is not recorded here.** This file is the reviewer's bytes.

---

VERDICT: REVISE

---

## A. Is the arm space complete?

**Method.** I decomposed the decision into its three independent axes — (i) where the four companion classes go, (ii) whether the two manifest classes stay in `contracts/`, (iii) whether the 87 in-module path references are rewritten — and enumerated the cross-product, then tested each cell against the *defined clause*, RFC3-15, quoted below. I anchored lawfulness to the clause's `contracts/` cell only, not to prose near it.

**The clause, quoted exactly** (`rfcs/RFC-0003/governance-homes-and-owner-acts.md:73-86`):

> **RFC3-15.** The **five** constitutional categories of `.syzygy/governance/` hold, exclusively — "exclusively" bounding what each category may contain, and the five-category set itself being closed except by the two lawful widenings this RFC records… A plane validator therefore accepts exactly these six names and rejects a seventh…
>
> | `contracts/` | Accepted load-bearing contracts (RFCs), including normative data contracts and external service contracts | …

**Observation.** The space is **not** complete, and the missing arm is cheaper than the recommendation on both of the packet's own measures.

Arms the packet does not list:

| Unlisted arm | Lawful? | Cost on the packet's measures |
|---|---|---|
| **(1g)** Drop the companion copies from the ceremony **and do not repair the references**; carry both manifests inside the owner-act record rather than in `contracts/` | **Yes.** `contracts/` then holds `rfcs/` only — the cell is satisfied literally. The act record is a `decisions/` member ("Recorded owner decisions: adoptions…"). No clause requires a module's prose path references to resolve inside the installed tree (sweep below). | **0 modules move. 0 confirmations retire.** Both RD-31b and RD-32c survive |
| **(1h)** Companions to a home outside `.syzygy/governance/` (RFC3-15's scope is `.syzygy/governance/` only), references unrepaired | Yes — RFC3-15 does not reach outside `governance/` | 0 modules, 0 confirmations |
| **(1i)** **Split by type** — `rfcs/`→`contracts/rfcs/`; manifests→the act record; the two *generated* reports→`.syzygy/cache/` (RFC3-20: "`.syzygy/cache/` is rebuildable projection, nothing else" — they are rebuildable, so lawful there); `history/`+`matrix-rows/` stay in the candidates tree | Yes | 0 modules if references are left alone |
| **(1j)** Install the companions as symlinks into the candidates tree | **Undecided** — no clause addresses symlinks; whether a symlink is "held" by the category is a new open question. Worse than (1g): buys nothing and opens a question | 0 modules |
| **(1k)** Copy the companions in a separate non-act operation after the act | **Unlawful as a fix.** RFC3-15's "exclusively" bounds *what the category may contain*, not when it came to contain it. Timing does not cure containment | — |

The decisive omission is **(1g)**. The packet's (1c) is "*Drop the companion copies from the ceremony **and repair the modules' backlinks*** …" (`WAVE-A-INSTALL-SHAPE-DECISION.md:36-39`). The repair is what makes (1c) cost thirty modules; the packet never argues the coupling. Its own supporting analysis supplies the argument *against* the coupling, twice:

- §3 q1 (`P33-SEMANTIC-INSTALL-ANALYSIS.md:56-59`): "The dependency is **navigational**, not semantic: a reader who cannot open `RFC-0002-history.md` still reads RFC-0002 correctly, and finds a broken link where a rationale pointer was."
- §3 q5 (lines 77-83): "the copy does not preserve access to the rationale — the candidates tree already does — the copy preserves **the resolution of a relative link**."

**Absence sweep, with denominator.** Denominator: all 39 modules under `contracts/candidates/rfcs/`. I extracted every line containing `link`/`backlink` co-occurring with `must|shall|required|resolve` (Python `re`, not a bracket class): **9 hits in 6 modules**, all read individually. All 9 are runtime/product clauses about project-entity or surface links — RFC1-11's trust-floor rule for retired identities, RFC6-20 ("Every internal link in the fact set… if a surface renders such a citation *as a link*, that link must resolve"), RFC7-3, RFC8/RFC9 rendering clauses. **None governs a governance-tree file path inside a contract module's prose.** I also confirmed `check_governance.py` contains zero post-install link checks (0 hits for `post.install` over the file), consistent with the acceptance record's own statement that "`CG-14` still checks install *routes* only."

**Judgement — FAIL.** A lawful arm strictly cheaper than the recommendation, on the packet's own two axes, is absent from the packet. This is the material finding the criterion contemplates, and it is blocking because it also falsifies the packet's headline claim (see D).

---

## B. Is the cost measurement correct?

**Method.** Independent re-measurement, not a re-run of the packet's script. I built the denominator from the six wave manifests and cross-checked it against the filesystem; then extracted every backtick code span in every module with Python `re` (`` `([^`]+)` `` — no bracket class over `]`), and counted per-target occurrences per wave. I then separately masked all code spans and swept the remainder, and separately counted markdown-link syntax.

**Denominator, verified two ways.** 39 `.md` files under `rfcs/`; the six wave manifests hold 19 + 11 + 9 = 39 paths; set difference in both directions is empty (0 files unmanifested, 0 manifest rows missing from disk). Wave A = 19, Wave B = 11, C/D = 9. **Agrees.**

**My counts (modules, references):**

| Target | Wave A | Wave B | C/D | Packet's figure |
|---|---|---|---|---|
| `history/` | **19 modules, 40 refs** | **11 modules, 28 refs** | 6 modules, 8 refs | identical |
| `matrix-rows/` | 1, 1 | — | — | identical |
| `CONTEXT-BUDGET-REPORT.md` | 3, 3 | 3, 4 | 2, 2 | identical |
| `03-…-COMPACTION-REPORT.md` | — | 1, 1 | — | identical |

40 + 28 = **68**. **Full agreement, cell for cell**, including the C/D row the packet's decision file omits. Corroborated independently: `round-2026-08d/POST-INSTALL-LINK-REPORT.md` reports "87 relative references examined" and my total companion-reference count is also 87 (76 + 1 + 9 + 1) — i.e. the *entire* relative-reference population of the 39 modules is companion-directed.

**One correction to the characterisation, not the count.** All 87 are **code spans, not hyperlinks**. Markdown link syntax (`](…)`) matching any companion target: **0 hits over 39 modules**. Outside code spans there is exactly **1** further occurrence (`RFC-0001-project-graph-identity-state-planes.md`, an `[Observed: ../history/RFC-0001-history.md, …]` attribution). The packet calls these "code-span links" that "resolve"; nothing renders or resolves — a reader must manually follow a path string. This matters because it is the entire cost of arm (1g).

**Judgement — PASS on the numbers; the word "link" overstates what breaks.**

---

## C. Is (1e) the cheapest lawful arm on the packet's own measure?

**Method.** Re-derived the packet's table from the measurement in B, then compared (1e) against each arm it must beat.

**Observation — no, on two independent counts.**

1. **(1e) is not cheaper than (1b); it is tied.** The packet's own table gives (1b) and (1e) identical cells: 1 module moved, Wave A retired, Wave B survives. The packet concedes it — "(1b) remains offerable and is (1e) without the closed enumeration" (line 96-98). Yet the recommendation's four stated reasons (lines 84-88) — "moves one module instead of thirty, retires one confirmation instead of two, keeps every reference resolving without touching an accepted reference, and states what the tree contains" — are **shared with (1b) on the first three**. Only the fourth distinguishes, and it rests entirely on one unlabelled sentence: "A closed enumeration is not a stretched category" (lines 55-56).

2. **That sentence is where the reasoning does not survive re-derivation.** The packet applies RFC3-15(a)'s precedent objection to (1b) and then silently exempts (1e), though the objection is identical. The clause, quoted (`governance-homes-and-owner-acts.md:96-99`):

   > The fifth category is an explicit widening of a structure this RFC calls constitutional, made by owner amendment rather than by stretching a category's "exclusively" — **the precedent any future widening follows.**

   The packet's own restatement of (1b) says "widening an existing cell's contents is exactly the stretching move the clause warns against" (lines 30-34). (1e) also widens an existing cell's contents — from one occupant class to three. Re-typing is widening with a fence around it. Whether a fence converts a stretch into a non-stretch is precisely the question, and the packet answers it by assertion in a single unlabelled clause. That is the load-bearing move of the whole recommendation and it is not argued.

3. **(1g) beats (1e) outright** on the packet's own two axes: 0 modules vs 1, 0 confirmations retired vs 1, and no RFC3-15 amendment at all.

4. **(1d)'s "most expensive arm" cell is *understated*, not overstated.** The packet prices (1d) as an RFC3-15 amendment plus a 68-reference rewrite. It also requires amending the closure sentence "A plane validator therefore accepts exactly these six names and **rejects a seventh**" — minting `contracts-companion/` inside `governance/` makes a seventh name, so (1d) rewrites RFC3-15's *closure* rule, not merely adds a row. The packet does not say this.

**Judgement — FAIL.** The recommendation is joint-cheapest among the listed arms, not cheapest; the principle that breaks the tie is an unlabelled assertion that the clause's own precedent sentence cuts against; and a cheaper arm exists outside the list.

---

## D. Does any arm preserve the current Wave A confirmation?

**Method.** Established what the argument is a function of, then evaluated each arm against that function. Acceptance record §1 row A defines the Wave A phrase argument as the digest of `wave-manifests/WAVE-A-MANIFEST.txt`, "whose own digest is the act's argument". I recomputed it: `sha256sum wave-manifests/WAVE-A-MANIFEST.txt` → `8972d9630b95f5d4266432dbb1b3602114576bbd6c0f29d6f9bd6f905b1f884a`, matching §1 row A and RD-31b. Wave B → `193e3c1e15e4…`, matching. The manifest body is nineteen per-module digest rows and nothing else. **Therefore the argument regenerates if and only if at least one of the nineteen module byte-streams changes.** The ceremony text lives in `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`, which is in no wave manifest and feeds no argument.

**Per-arm result:**

| Arm | A module bytes move? | Argument regenerates? | RD-31b CONFIRM |
|---|---|---|---|
| (1a) **as written** (with rewrite) | yes, 19 | yes | retires — packet correct |
| (1a) without rewrite | no | **no** | **survives** |
| (1b) | yes — `RFC-0003/governance-homes-and-owner-acts.md`, a Wave A manifest row | yes | retires — packet correct |
| (1c) **as written** | yes, 19 | yes | retires — packet correct |
| (1c) without repair | no | **no** | **survives** |
| (1d) | yes (RFC3-15 amendment) | yes | retires — packet correct |
| (1e) | yes (same module as 1b) | yes | retires — packet correct |
| (1f) | rejected | — | — |
| **(1g)** *(unlisted)* | **no** | **no** | **survives — and so does RD-32c** |

**Observation.** Every per-arm cell in the packet's table is correct *for the arm as the packet specifies it*. The universal claim above the table is not:

> **There is no arm that preserves the current confirmations.** Whichever is ruled, at least the Wave A exact-package gate re-runs on a regenerated argument. (`WAVE-A-INSTALL-SHAPE-DECISION.md:79-82`)

That is a claim about the *arm space*, it is unlabelled, and it is false — because the space is incomplete (A). It has also propagated outward as settled fact: `round-2026-08f/CAPABILITY-1-OWNER-DECISION-PACKET.md` opens its P-33 section with "**One fact governs the whole page: there is no arm of P-33 that preserves the current Wave A confirmation**", and `AGENTS.md` restates it in the repository's operating procedure.

**And it contradicts the confirming review the packet depends on**, without disclosing the contradiction. RD-31b (`round-2026-08e/reviews/RD-31b-wave-a-RAW.md:99, 107`), quoted exactly:

> **Yes — these bytes are offer-ready. The Wave A act may be offered on argument `8972d963…` once, and only once, P-33 is ruled.**
>
> The one thing that must happen first is not in the bytes at all. **Rule P-33, and the offer opens on this argument.**

RD-31b's expectation is defensible only for an arm that moves no module byte. The honest statement is not "no arm preserves the confirmation" but "**every arm currently drafted** moves bytes — and an arm that moves none exists."

**Judgement — FAIL.** The claim under test is false, unlabelled, load-bearing, and already propagated into two downstream artifacts and the repository's operating procedure.

---

## E. Is the second question answered soundly?

**Method.** Read Q2 in both files, re-derived its arm space on the same three axes (what is installed, where, and when), and checked whether each stated arm's consequence is complete and whether the machinery each arm presumes exists.

**What is sound.** The defect statement is precise and correctly typed: "a membership record whose scope is wider than the act that installs it is **not** membership, it is an inventory" (`P33-SEMANTIC-INSTALL-ANALYSIS.md:133-135`). The 2026-08-11 addition — that under the deferred posture (2a) means "install never, while the posture stands" — is a genuine consequence, correctly named, and I verified its premise: `DEFERRED-WAVE-POSTURE.md` places C1/C2/D1/D2 off the offer path, and acceptance record §1 offers no final wave act.

**What is not sound.**

1. **The arm space is incomplete, in the same way as Q1.** Unlisted: **(2c)** install only the *wave* manifests and no active manifest at all — the installed wave manifests then *are* the identity record, exactly scoped to what each act bound; **(2d)** install a regenerated accepted-rows-only manifest at each act; **(2e)** carry the 39-row manifest with the owner-act record rather than in `contracts/` — which is what the analysis's **own §1 typing table** prescribes for it ("with or attached to the owner-act record, digest exact", line 21-22). The analysis types the artifact and then §4 re-offers only the two pre-existing arms, both of which put it in `contracts/`. The typing the charter commissioned never becomes an arm.

2. **(2b) presumes machinery that does not exist.** (2b) turns on "a **generator-written** banner… regenerated at each act". `scripts/build_active_manifest.py` is 412 lines and contains **0 occurrences** of `banner` (Python `re`, case-insensitive). The packet does not tell the owner that ruling (2b) creates a generator obligation.

3. **The consequence is stated for (2a) and not for (2b).** Under the deferred posture, (2b) permanently installs a 39-row inventory in the accepted tree of which 9 rows name modules that will never be accepted while the posture stands. That is (2a)'s mirror consequence and it is absent.

4. **The two questions are answered independently and their cross-product is never checked — and one combination is self-contradictory.** (1e) amends the cell to "a **closed enumeration of three occupant classes** — accepted contract modules (`rfcs/`), integrity-bearing manifests (`wave-manifests/`), and one explicitly named non-normative resolution lane" (lines 48-56). `ACTIVE-CONTRACT-MANIFEST.txt` installs at `contracts/ACTIVE-CONTRACT-MANIFEST.txt`, not inside `wave-manifests/`. Under a **closed** enumeration it is not admitted. An owner ruling **(1e) + (2b)** would therefore adopt a cell that forbids the file the same ruling installs.

**Judgement — FAIL.** The typing is sound; the arm space is not, one arm presumes absent machinery, one consequence is stated asymmetrically, and the two questions interact in a way the packet does not surface.

---

## F. Does the packet decide, bind, or present inference as observation?

**Method.** Read every declarative sentence in both files for (a) owner-reserved acts, (b) imperative/binding mood, (c) substantive claims without an epistemic label, checking each unlabelled claim against whether it is a measurement I could reproduce or an LLM assertion.

**What is right.** Both files disclaim decision in their first lines — "**This file decides nothing**", "**Analysis, not a decision.** P-33 is the owner's, and this file rules nothing", "**Nothing here is applied.** No module is edited, no ceremony text is changed, and no arm is drafted into the acceptance record." Both recommendations carry `[Inferred]`. The honest counter-argument section (lines 100-106) is real and names (1a)/(1c) as "a legitimate ruling, not a mistake". Withdrawing the analyst's own prior (1d) recommendation is within remit. **No owner-reserved act is performed; no binding language appears. VIS-4 is respected.**

**What is wrong — unlabelled claims doing load-bearing work.**

| Claim | Location | Problem |
|---|---|---|
| "**There is no arm that preserves the current confirmations.**" | packet 79-80 | Unlabelled, bold, universal over a space; false; contradicts RD-31b. This is an LLM assertion presented as observation |
| "**(1d) is the most expensive arm in the space**" | packet 92-93 / analysis 104 | Unlabelled comparative that presupposes the space is complete — the very thing unproven |
| "A closed enumeration is not a stretched category." | packet 55-56 | Unlabelled definitional assertion carrying the entire recommendation |
| "19 of 19 Wave A and 11 of 11 Wave B… 68 references" | packet 66-69 | Correct, but transcribed into the packet with **no label**, while the owning artifact labels it `[Observed]`. Verification rule 3: a derived value quoted outside its owning artifact goes stale silently |
| every "retired"/"survives" cell | packet 71-78 | Inferences about a future act's digest behaviour, rendered as plain table facts |
| "exactly **two** of the six belong in an accepted-contract home… right to refuse the other four" | analysis 27-29 | Unlabelled — **and contradicted by its own table five lines above**, which sends *five* of six elsewhere (both manifests go "with or attached to the owner-act record") |

**Judgement — PASS on VIS-4, FAIL on epistemic labelling.** The most consequential sentence in the packet is an unlabelled false universal.

---

## G. Could an owner rule from this packet alone?

**No.** Ruling (1e) as written requires opening at least seven things the packet does not carry:

1. **RFC3-15's `contracts/` cell itself.** The packet never quotes it. Its paraphrase — "the home holds accepted contract content **exclusively**" — is *wider* than the cell's actual words, "Accepted load-bearing contracts (RFCs), including normative data contracts and external service contracts". "Contract content" can be read to cover manifests; "contracts (RFCs)" plainly cannot. An owner amending a cell must see the cell.
2. **The sentence (1d) would also have to amend**: "A plane validator therefore accepts exactly these six names and rejects a seventh."
3. **The replacement text.** (1e) asks for a closed enumeration but drafts none. There is nothing to rule on beyond a description of a shape.
4. **The name of the third occupant class.** (1e) says "one **explicitly named** non-normative resolution lane" — and never names it. A closed enumeration with an unnamed member cannot be ruled.
5. **Which module moves.** The table says "**1**". Only the analysis names it (`RFC-0003/governance-homes-and-owner-acts.md`).
6. **Why "retired"/"survives" follow.** The argument is `sha256(WAVE-A-MANIFEST.txt)` and the manifest is nineteen module digests — stated in neither file. Without it the column is unauditable.
7. **What the re-review costs.** "One fresh exact-package review of the regenerated Wave A argument" appears only in the analysis §3 q8.

**And two routing defects would mislead an owner who follows the documented ceremony.** Acceptance record §2 step 0 is "**Read §7 first**… no phrase before it." §7 item 11 (line 507) still says P-33's "own recommendation is the RFC3-15(a) recorded-widening route" — that is **(1d), withdrawn on 2026-08-11**. The register row the packet itself says "still owns the queue entry" (`decisions/PENDING-OWNER-DECISIONS.md:186`) lists only three arms and marks as "reviewer-preferred" the option "amend RFC3-15's `contracts/` cell by its own RFC3-15(a) recorded-widening route" — a justification **the packet itself states is false** (lines 30-35). An owner reading the ceremony's mandated first document, or the register that owns the queue entry, meets the withdrawn recommendation and the disproved justification. RD-8's characterisation applies exactly: routing an owner to a stale offering converts a knowing act into a surprised one.

---

# Findings

**1. BLOCKING — the arm space omits the cheapest lawful arm.**
`decisions/WAVE-A-INSTALL-SHAPE-DECISION.md:21-78`
Evidence: (1c) is specified as "Drop the companion copies **and repair the modules' backlinks**"; the repair is never argued for and is what produces its 30-module cost. The uncoupled arm — drop the copies, leave the 87 code-span path strings alone, carry both manifests inside the owner-act record — satisfies RFC3-15's `contracts/` cell literally, moves **0** module bytes, requires **no** RFC3-15 amendment, and retires **no** confirmation. Its only cost is 87 dangling textual path references in the installed tree, a cost the analysis's own §3 q1 and q5 characterise as navigational and non-semantic, with the candidates tree preserving all access regardless.
Fix: add the arm as (1g) with its true cost stated (87 unresolvable in-tree path strings, all clone-resolvable in the candidates tree), and either recommend it or state on the record why the 87 dangling strings are worth one retired confirmation plus an amendment to a constitutional clause.

**2. BLOCKING — the packet's headline claim is false, unlabelled, and contradicts the review it relies on.**
`decisions/WAVE-A-INSTALL-SHAPE-DECISION.md:79-82`
Evidence: "There is no arm that preserves the current confirmations." The argument is `sha256(wave-manifests/WAVE-A-MANIFEST.txt)` = `8972d963…` (recomputed), a function of the nineteen module byte-streams only; the ceremony text is in no manifest. Any arm touching no module byte preserves it. RD-31b, the confirming review, says at line 107: "**Rule P-33, and the offer opens on this argument.**" The claim has propagated to `round-2026-08f/CAPABILITY-1-OWNER-DECISION-PACKET.md:41-43` ("One fact governs the whole page") and to `AGENTS.md`.
Fix: replace with the true and narrower statement — "every arm *currently drafted* moves at least one accepted byte; an arm that moves none is arm (1g)" — label it, and correct the two downstream restatements.

**3. BLOCKING — (1e) and (2b), the two recommendations, are mutually inconsistent.**
`decisions/WAVE-A-INSTALL-SHAPE-DECISION.md:48-56` and `:120-125`
Evidence: (1e)'s closed enumeration admits "integrity-bearing manifests (`wave-manifests/`)". (2b) installs `ACTIVE-CONTRACT-MANIFEST.txt` at `contracts/`, outside `wave-manifests/`. A *closed* enumeration excludes it. Ruling both adopts a cell that forbids a file the same ruling installs.
Fix: either name `ACTIVE-CONTRACT-MANIFEST.txt` in the enumeration, or route it to the act record per the analysis's own typing, and state the Q1×Q2 cross-product explicitly.

**4. MATERIAL — RFC3-15's `contracts/` cell is never quoted, and the paraphrase softens the breach.**
`decisions/WAVE-A-INSTALL-SHAPE-DECISION.md:12-17`; `P33-SEMANTIC-INSTALL-ANALYSIS.md:27-29`
Evidence: the packet says the row "says the home holds accepted contract content **exclusively**". The cell says "Accepted load-bearing contracts (RFCs), including normative data contracts and external service contracts". Under the real words the manifests are as plainly excluded as `history/`; under the paraphrase they read as arguably admitted — which is why the analysis can assert "exactly two of the six belong" while its own table sends five of six elsewhere.
Fix: quote the cell verbatim in the packet, and reconcile the "two of six" sentence with the table above it.

**5. MATERIAL — the RFC3-15(a) precedent objection is applied to (1b) and silently withheld from (1e).**
`decisions/WAVE-A-INSTALL-SHAPE-DECISION.md:26-35` vs `:48-56`
Evidence: RFC3-15(a) reads "made by owner amendment rather than by stretching a category's 'exclusively' — **the precedent any future widening follows**". The packet applies this to (1b) in a restated correction, then exempts (1e) with the unlabelled sentence "A closed enumeration is not a stretched category." (1e) widens the same cell from one occupant class to three.
Fix: state the objection against (1e) too, label the counter as `[Inferred]`, and argue it rather than assert it — or concede that under the clause's own precedent (1d) is the endorsed route and (1e) is a departure the owner is being asked to make knowingly.

**6. MATERIAL — the "relocate ⇒ rewrite 68 references" coupling is unargued and contradicted internally.**
`decisions/WAVE-A-INSTALL-SHAPE-DECISION.md:64-78`; `P33-SEMANTIC-INSTALL-ANALYSIS.md:56-59, 77-83`
Evidence: the coupling is the sole source of the 30-module cost assigned to (1a), (1c) and (1d), and thus the sole basis on which (1e) "moves one module instead of thirty". The analysis argues the opposite twice.
Fix: price each relocating arm twice — with and without the reference repair — and let the owner see that the repair is a discretionary quality choice, not a consequence of the ruling.

**7. MATERIAL — two artifacts an owner is directed to read still carry the withdrawn recommendation.**
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:507`; `decisions/PENDING-OWNER-DECISIONS.md:186`
Evidence: §7 item 11 — the document the ceremony's step 0 makes mandatory reading before any phrase — says P-33's "own recommendation is the RFC3-15(a) recorded-widening route", i.e. (1d), withdrawn 2026-08-11. The register row, which the packet says "still owns the queue entry", lists three arms (no 1d/1e/1f) and marks as reviewer-preferred an option justified by the RFC3-15(a) route the packet itself proves does not exist.
Fix: update both to the current arm space and recommendation, or have the packet state in its own voice that §7 and the register row are stale and which text governs.

**8. MATERIAL — Q2's arm space is incomplete and (2b) presumes absent machinery.**
`decisions/WAVE-A-INSTALL-SHAPE-DECISION.md:113-136`; `P33-SEMANTIC-INSTALL-ANALYSIS.md:129-145`
Evidence: three arms are unlisted — install only wave manifests; install a regenerated accepted-rows-only manifest; carry the 39-row manifest with the act record (the analysis's own typing, never converted into an arm). `scripts/build_active_manifest.py` (412 lines) contains 0 occurrences of `banner`. The (2a)-under-deferral consequence is stated; the symmetric (2b) consequence — a permanent 9-row over-listing in the accepted tree — is not.
Fix: add the three arms, state the generator obligation (2b) creates, and state (2b)'s standing consequence beside (2a)'s.

**9. MINOR — the cost figures are transcribed into the packet unlabelled.**
`decisions/WAVE-A-INSTALL-SHAPE-DECISION.md:64-69`
Evidence: the analysis labels the measurement `[Observed]`; the packet re-states 19/19, 11/11 and 68 with no label and no method. The figures are correct today (I reproduced all four rows exactly) but nothing binds them to the bytes. Verification rule 3.
Fix: label the figures and name the owning artifact and its method inline, or generate the row.

**10. MINOR — "links" overstates what the 87 references are.**
`decisions/WAVE-A-INSTALL-SHAPE-DECISION.md:66-69`; `P33-SEMANTIC-INSTALL-ANALYSIS.md:37-48, 86-89`
Evidence: 0 of the 87 companion references use markdown link syntax; all 87 are inert backtick code spans (plus one bare prose reference). "Every reference resolving" and "none of the 68 resolve" describe manual path-following, not navigation.
Fix: say "code-span path references a reader follows by hand", so the cost of every relocating arm is not read as broken navigation.

**11. MINOR — the packet's arm table omits (1f); the analysis's includes it.**
`decisions/WAVE-A-INSTALL-SHAPE-DECISION.md:71-78` vs `P33-SEMANTIC-INSTALL-ANALYSIS.md:95-102`
Fix: carry the (1f) row with its rejection into the packet's table so the table's population matches the option list above it.

**12. MINOR — (1d)'s cost is understated in the one respect that favours the recommendation.**
`decisions/WAVE-A-INSTALL-SHAPE-DECISION.md:40-46, 92-98`
Evidence: minting a category inside `governance/` also contradicts RFC3-15's closure sentence, "A plane validator therefore accepts exactly these six names and rejects a seventh" — so (1d) amends the closure rule, not just adds a row. The packet prices only the row plus the rewrite.
Fix: state it. It strengthens the packet's own case against (1d) and shows the sweep was done.

**13. MINOR — the packet cannot be ruled without the analysis.**
`decisions/WAVE-A-INSTALL-SHAPE-DECISION.md` throughout
Evidence: the moving module is unnamed, the re-review scope is absent, the argument's derivation is absent, and (1e)'s enumeration has no draft text and no name for its third class. See G items 3-7.
Fix: fold those five facts into the packet, and draft the replacement cell text (1e) would install.

---

## What I could not test and why

- **Whether an owner would accept 87 dangling path strings in the accepted tree.** That is the actual trade in arm (1g) and it is a values question reserved to the owner (VIS-4). I established that no *clause* forbids it (sweep in A, denominator 39 modules) and that RD-7's original finding was a review preference, not a clause obligation. I did not judge whether the owner should mind.
- **Whether `decisions/` may hold a manifest `.txt` beside an act record, as opposed to the act record quoting the manifest inline.** RFC3-15's `decisions/` cell reads "Recorded owner decisions: adoptions, dismissals (reason + expiry), adjudications, consent records (RFC3-7), overrules" — it neither admits nor excludes an attached membership file. This is a genuinely open reading and I flag it rather than resolve it; arm (1g) is safe under the inline-quotation form regardless.
- **The `history/`, `matrix-rows/` and generated-report bytes themselves.** I did not read them; my measurement is of references *into* them from the 39 modules, which is what the cost claim is about.
- **Whether RD-31b's CONFIRM would survive a *ceremony*-only change in the reviewer's own judgement.** I established the argument is byte-derived and does not move, and I quoted RD-31b's own expectation that the offer opens on this argument after P-33 is ruled. Whether that reviewer would re-affirm given a rewritten step 3 is a question only a re-administration answers; I did not simulate one.
- **Any prior review of this packet.** I read RD-31b, RD-32b/c excerpts and the disposition register only to establish the argument-digest chain and the confirmation state. I did not read RD-18, RD-26 or RD-30, so I cannot say whether findings 1-3 were raised before and dispositioned.
- **Execution of the checkers.** I ran no repository check script; all measurements above are my own Python `re` sweeps over the working tree at `e2efda6` (both subject files verified byte-identical to that commit via `git diff --stat`, empty).
