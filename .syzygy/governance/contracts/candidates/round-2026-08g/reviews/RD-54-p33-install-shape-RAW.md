# RD-54 — P-33 decision packet and install-shape analysis (round-2026-08g, frozen commit `a47635b`)

> **Provenance banner, added by the recording session — everything below the
> rule is the reviewer's raw output, copied verbatim and unedited.** The
> verdict word is copied exactly.
>
> | | |
> |---|---|
> | **Charter role** | §5 review 1 — the P-33 decision reviewer: option completeness, costs, contract typing, navigability, and whether the owner can rule from the packet |
> | **Dispatched** | 2026-08-13 |
> | **Subject commit** | `a47635b` — bytes frozen; nothing in the subject was edited between dispatch and this record |
> | **Subject files** | `decisions/WAVE-A-INSTALL-SHAPE-DECISION.md`; `round-2026-08g/P33-SEMANTIC-INSTALL-ANALYSIS.md` |
> | **Context** | fresh — subject, governing references and acceptance criteria only. The reviewer's own disclosures of what else it opened, and why, are the first section of its output and are part of the raw bytes |
> | **Model family** | same family as the corpus authors. Supports repair; **is not the formal launch administration** |
> | **Verdict** | `REVISE` — two findings the reviewer marks **BLOCKING** |
>
> **Disposition is not recorded here.** This file is the reviewer's bytes.

---

I have completed my independent verification. Writing the review.

---

VERDICT: REVISE

# Preliminary disclosures

Files I read that are not in my subject or governing-reference list, and why:

- `/home/tze/GitHub/syzygy/syzygy_fable_opus_owner_spec_launch_closure_prompt.md`, **lines 300–384 only**. Criterion F asks me to test the packet's characterisation of a "standing owner instruction". A repo-wide sweep (774 files, all `.md/.txt/.yaml/.json/.py`) found the phrase `clean typed layout` in exactly 5 places: twice in the packet, once in the analysis, twice in this file. It is the only artifact carrying the instruction, so testing F was impossible without it. I read only §6.3–§6.6 and did not read the file's findings, dispositions, or history sections.
- `.syzygy/governance/contracts/candidates/02-OWNER-DIRECTION-RECORD.md` (full), to check whether the standing instruction lived in a governance artifact. It does not.
- `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` — grep only, two lines, to locate the P-33 register row.
- `.syzygy/governance/contracts/candidates/scripts/build_active_manifest.py` (lines 1–280), `scripts/check_governance.py` (grep only), `.gitignore`, `.syzygy/governance/doctrine/trust-and-evidence.md` and `vision.md`.

I did not open any `reviews/` directory, any `DISPOSITION-REGISTER.md`, any `HISTORY.md`, `PROCESS-LESSONS.md`, or any round report other than the two subject files. I did not open `round-2026-08d/POST-INSTALL-LINK-REPORT.md`, `round-2026-08f/P33-SEMANTIC-INSTALL-ANALYSIS.md`, or any RD-nn file. Every RD-nn number appearing below is quoted from the subject files or the acceptance record, never read at source.

---

# A. Option completeness

**METHOD.** I did not take the packet's axis table as the space. I derived the lawful settings myself from three sources: (1) the `contracts/` cell and closure sentence of RFC3-15 as they actually read in `rfcs/RFC-0003/governance-homes-and-owner-acts.md:73–89`; (2) the current filesystem state of `.syzygy/governance/` and `.syzygy/governance/contracts/`, enumerated with `ls`; (3) the generator `scripts/build_active_manifest.py`, read to determine exactly which inputs the wave-manifest byte-stream depends on, so I could compute for myself which relocations are byte-free. I then asked, for each companion class and for the candidates tree itself, whether a home exists that is lawful under RFC3-15 *and* costs no accepted byte.

**OBSERVATION.**

The current tree, `[Observed]` by `ls`:

```
.syzygy/governance/       -> contracts  decisions  doctrine  policies      (4 of 5 categories exist)
.syzygy/governance/contracts/ -> candidates                                 (exactly one entry)
```

`.syzygy/governance/contracts/` today contains exactly one directory, `candidates/`, and that directory contains `history/`, `matrix-rows/`, `CONTEXT-BUDGET-REPORT.md`, `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md`, `ACTIVE-CONTRACT-MANIFEST.txt`, `wave-manifests/`, `reviews/`, `scripts/`, `fixtures/`, `policy-candidates/`, seven `round-*/` trees and the 39 draft modules. The acceptance record confirms this is the tracked home, "present in every clone, at `.syzygy/governance/contracts/candidates/`" (`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:239`), and its step 3 establishes that a wave act does **not** delete the candidate home — the parallel act 3 rule reads "does **not** delete `topology-candidates/` — retirement of the candidate home is a separate, later cleanup" (`:157–159`).

Therefore, under option (M) as written, after the Wave A act:

```
.syzygy/governance/contracts/ -> candidates/   rfcs/
```

The packet states at line 55 that both options put "nothing else in `contracts/`", and the analysis states at line 288 that contract-category purity is "**Full.** `contracts/` holds `rfcs/` and nothing else". Both are false against the tree. This is developed under criterion F; here it matters because it opens an option the packet does not carry.

**The missing option.** Call it **(M+)**: option (M) *plus* relocating the candidates tree to a home outside `.syzygy/governance/`. The analysis's own axis row `D''` already establishes the rule that makes this free — "outside `.syzygy/governance/` | Yes — RFC3-15's scope stops at `governance/` | no" (`P33-SEMANTIC-INSTALL-ANALYSIS.md:241`). Applying that row to the candidates tree as a whole rather than to `history/` alone yields:

| | (M) as offered | (M+) |
|---|---|---|
| Accepted bytes moved | 0 | **0** |
| Wave A / Wave B confirmations | survive | **survive** |
| RFC3-15 amendment | none | **none** (destination is outside `governance/`) |
| `contracts/` after act 1 | `candidates/` **and** `rfcs/` | **`rfcs/` only** |
| Dangling in-module strings | 88 | 88 |

I verified the zero-byte property myself rather than assuming it. `build_active_manifest.py:187–189` writes rows as `f"{sha}  {rel}"` where `rel` is computed by `os.path.relpath(..., root)` against the **candidates root**, not against the repository root (`enumerate_modules`, lines 137–140). Moving the candidates tree wholesale therefore changes neither the row paths nor the per-module digests nor the four header lines. `[Observed]` from the generator source; `[Inferred]` that the resulting manifest bytes are identical, since I did not perform the move.

(M+) is strictly better than (M) on the one dimension the packet's recommendation rests on — typed containment — at identical cost on every dimension the packet prices. Its existence is the counterexample to the packet's claim at line 55 that both options already achieve purity, and it is materially better than both offered options.

Two further lawful settings are absent from the enumeration:

- **`records/` as the manifest home.** The standing instruction names it explicitly ("governance/decisions/ **or governance/records/**", prompt line 341). The analysis's axis B prices only "inside the owner-act record" and "`contracts/wave-manifests/`". `records/` is in fact excluded — its cell admits only "Kernel-authored durable facts minted on a non-owner actor's submission, or by the pre-declared deterministic challenge-sweep policy" (`governance-homes-and-owner-acts.md:89`), and an owner-side membership manifest is neither — but a rejected setting is supposed to be rejected *with its rule* (the analysis's own §7 discipline), and this one is not rejected at all.
- **Whether installation into `contracts/` is required at all.** The cell says what the category *may contain*; no clause I found says every accepted contract must be copied there. The packet never tests this premise, and it is the premise that generates the whole problem. I do not think the resulting option (accepted modules living in a directory called `candidates/`) is better, but the enumeration claims closure and does not close over it.

**JUDGEMENT: FAIL.**

---

# B. Cost correctness

**METHOD.** Deliberately not the packet's method. Rather than searching for six named companion targets, I extracted *every* backtick code span from all 39 modules with Python `re` (`` `([^`]+)` ``), stripped anchors and trailing punctuation, and **resolved each candidate string against the filesystem relative to its own module's directory**. A string is counted only if it names a file that exists. Each resolving string was then classified by whether its resolved path falls inside `rfcs/` (survives install) or outside it (dangles under M). This measures the quantity that actually matters — pointers that resolve today and stop resolving after the copy — without needing to know the companion taxonomy in advance. I separately swept for Markdown links (`\[([^\]]*)\]\(([^)]+)\)`), reference-style link definitions, and raw HTML anchors, and separately swept raw text (outside code spans) for the same targets, to catch references the code-span method structurally cannot see.

Denominator, established first and cross-checked two ways: the six wave manifests carry **39 rows**, all distinct, no path in two manifests; `os.walk` over `rfcs/` finds **39** `.md` files; both set differences are empty. All 39 files' sha256 match their manifest rows. Wave manifest digests recomputed: `WAVE-A 8972d963…f884a`, `WAVE-B 193e3c1e…7e3ed` — both match the arguments in the acceptance record §1 (`:22–23`).

**OBSERVATION.**

*Companion reference count.* My independent method reproduces the packet's figure, cell for cell:

```
path-ish code spans resolving to a real file:      269   (denominator: all 39 modules)
  resolving inside rfcs/  (survive install):       182
  resolving outside rfcs/ (dangle under M):         87
```

Broken out: `history/*` 76 (RFC-0008 14, RFC-0002 12, RFC-0004 12, RFC-0005 10, RFC-0010 8, RFC-0009 7, RFC-0007 6, RFC-0003 3, RFC-0001 2, RFC-0006 2), `CONTEXT-BUDGET-REPORT.md` 9, `matrix-rows/RFC-0003-rows.md` 1, `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` 1. By wave: A 44, B 33, C1 1, D1 8, D2 1 — i.e. 44 / 33 / 10, exactly as the packet states. **This part of the measurement is confirmed.**

*Markdown links.* **0**, across all 39 modules. Not "0 to companion targets" — zero Markdown links of any kind, plus 0 HTML anchors and 0 genuine reference-style link definitions (my regex produced one hit, `[Observed: SDR-22]: (a)` at `RFC-0009/semantic-geography.md:648`, which is prose, not a link). The packet's claim is true and, if anything, understated. **Confirmed.**

*But the 87 is an undercount.* Sweeping raw text rather than code spans, `history/` occurs **77** times, of which 76 are inside code spans. The 88th reference is bare prose:

> `rfcs/RFC-0001-project-graph-identity-state-planes.md:83`
> `answered by whatever the first implementation does [Observed:`
> `../history/RFC-0001-history.md, the K-F1/K-F2 narrative].`

This is a Wave A module. Wave A's count is **45**, not 44; the total is **88**, not 87. The packet describes the population as "87 backtick path strings" (line 74) — the 88th carries no backticks, so it is invisible to the packet's stated method and would remain unfixed by a rewrite pass scoped to code spans.

I also found one candidate-tree pointer that resolves *nowhere*, today or after install: `rfcs/RFC-0003/manifests-and-namespace.md:604` cites `` `round-2026-08e/WAVE-A-SEMANTIC-DELTA.md` ``, which does not resolve relative to `rfcs/RFC-0003/`. It is a pre-existing defect, not a cost of P-33, but it belongs in the disclosed population of a document whose selling point is that the strings "resolve in any clone of this repository" (packet line 76).

*Which modules move under each option.* Under (M): none. Under (T): every module carrying at least one outside reference is edited. Measured: **19 of 19** Wave A modules and **11 of 11** Wave B modules carry at least one. So under (T) **all 30** launch-path rows change — not "up to 30" (packet line 86, line 165; analysis line 304). The hedge is unnecessary and, on a document deciding whether to spend two confirmations, it understates the certainty of the cost.

*The confirmation-retirement rule.* This is where the measurement fails. The packet's rule, at lines 43–44:

> **A confirmation retires if and only if the arm edits a file that is a row in a wave manifest.** The ceremony text is in no manifest.

grounded on line 41: "that manifest is **19 per-module digest rows and nothing else**". The analysis repeats both at lines 134–148.

`WAVE-A-MANIFEST.txt` is **not** 19 rows and nothing else. It is four comment lines and then 19 rows:

```
# WAVE-A-MANIFEST — kernel, evidence, storage, admission, cross-surface selection (RFC 0001-0006)
# 19 module(s); subset of ACTIVE-CONTRACT-MANIFEST.txt; rows sorted by codepoint order of the path.
# Generated by scripts/build_active_manifest.py — regenerate with it; never hand-edit.
# This file's own sha256 is the argument of the phrase `ACCEPT FOUNDATIONAL WAVE A: <sha256>`.
```

I confirmed against the generator (`build_active_manifest.py:224–232`) that all four lines are emitted into the file whose sha256 is the act's argument. The correct rule, derived rather than asserted, is:

> The argument regenerates **iff the wave manifest's own byte-stream changes**, which occurs if (a) any listed module's digest changes, **(b) any row's path string changes**, or **(c) any of the four header lines changes** — including the line that names the ceremony phrase, the line that names the generator's path, the line that names `ACTIVE-CONTRACT-MANIFEST.txt`, and the line that states the module count.

The packet's rule is right in the "if" direction and **wrong in the "only if" direction**, which is the direction the whole document leans on. Concretely: the packet's closing instruction is that after the ruling "the ceremony is drafted to match" (line 179). If that drafting renames the acceptance phrase — a thing this record has done twice before, since §1a records the retirement of `ACCEPT FOUNDATIONAL RFCS` and of the all-in-one phrase (`:74–82`) — header line 4 changes, the manifest regenerates, and Wave A's confirmation retires **under option (M)**, with no manifest-row file touched. The packet tells the owner the opposite in bold at line 50: "Choosing where a companion goes, or declining to install it, costs nothing."

A second live instance: the packet's own separate recommendation is to install neither package-wide manifest. Header line 2 of every wave manifest names `ACTIVE-CONTRACT-MANIFEST.txt` and asserts the wave is a subset of it. Declining to *install* that file does not change the header, so this particular ruling is byte-free — but the owner cannot determine that from the rule the packet gave them, because under that rule the header does not exist.

*One further unpriced consequence of (M).* Ceremony step 3 verifies the install by running `sha256sum -c wave-manifests/WAVE-<X>-MANIFEST.txt` **from `.syzygy/governance/contracts/`** (`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:149–151`). Option (M) does not install the wave manifest, so that command has no file to read from that directory and the install-verification step becomes unexecutable as written. The fix is ceremony-only and therefore cheap, but (M)'s cost block lists "re-review required: none" and says nothing about the installed tree losing its in-tree integrity artifact — the thing a future reader would use to re-verify the 19 accepted modules without leaving the accepted tree. That is a real property of (M) and it appears in neither cost block.

**JUDGEMENT: FAIL.** The reference count is confirmed but low by one and mis-scoped to backticks; the "up to 30" is actually exactly 30; and the mechanical retirement rule — the packet's own "one thing worth knowing before you read the options" — rests on a false statement about the manifest's contents and is unsound in the direction that matters.

---

# C. Contract typing

**METHOD.** I read both clauses in full at source rather than accepting either subject file's quotation, and compared the quoted fragments byte-for-byte against the module text. For each of the six companion classes I asked only one question: does the *defined clause's* "May contain" cell name this artifact class? I treated the cell as the boundary and the surrounding section prose as non-binding.

**OBSERVATION.**

*Does RFC3-15's `contracts/` cell admit a wave manifest?* The cell, quoted exactly from `governance-homes-and-owner-acts.md:86`:

> | `contracts/` | Accepted load-bearing contracts (RFCs), including normative data contracts and external service contracts | Owner acceptance: for the foundational set, **the digest-bound acts defined by the active acceptance record** — that record owns the acts, their exact phrases, and their arguments, and this clause quotes none of them, so a phrase this clause named could never outlive its retirement; owner sign-off per VIS-4 thereafter |

**No.** A wave manifest is a list of digests; it is not a contract, not a normative data contract, and not an external service contract. The "May contain" column is closed by the framing sentence's "exclusively", which the clause glosses in place as "'exclusively' bounding what each category may contain" (`:73–74`). The packet's typing is correct, and its five-of-six / one-of-six split (analysis §2) is correct on the clause's own words. I reach the same conclusion independently.

One caveat on the quotation. Both subject files elide the install-gate column with "…" — the packet at line 26, the analysis at lines 26–29 (which quotes it, but breaks off at "…"). The elided text is the one sentence in the cell that most nearly supports the opposite reading: the record "owns the acts, their exact phrases, and **their arguments**", and the argument *is* the wave manifest. That is a gate-column statement about authority, not a "may contain" statement about residence, so it does not in fact admit the manifest — but an owner ruling on typing should be shown the strongest text against the ruling, and neither file shows it.

The packet's quotation of the framing sentence (lines 30–32) also elides the gloss:

> The **five** constitutional categories of `.syzygy/governance/` hold, **exclusively** … A plane validator therefore accepts exactly these six names and **rejects a seventh**.

The elipsis swallows "— 'exclusively' bounding what each category may contain, and the five-category set itself being closed except by the two lawful widenings this RFC records". The elision happens to remove text that *supports* the packet's reading, so it does not mislead; the analysis quotes it correctly at lines 33–38. Noted as a fidelity slip, not a distortion.

*Does RFC3-20 permit the generated reports in `.syzygy/cache/`?* The clause, quoted exactly from `manifests-and-namespace.md:356–364`:

> **RFC3-20.** **`.syzygy/cache/` is rebuildable projection, nothing else** (VIS-6). The deletion-safety invariant: deleting `cache/` in its entirety, at any instant, changes no truth, status, work, consent, or authoritative artifact — everything in it is re-derivable from the artifacts that own its facts. Nothing in `cache/` may be cited as evidence, serve as a snapshot input, hold Genome membership, or be the only home of any fact.

The analysis's answer — lawful-but-contestable, because CG-20 routes every volatile measurement to `CONTEXT-BUDGET-REPORT.md` *as its home*, and cache may not be "the only home of any fact" (`P33-SEMANTIC-INSTALL-ANALYSIS.md:237`, `:358–360`) — is correct and honestly hedged. I confirmed CG-20 exists and is a real routing rule in `scripts/check_governance.py` (rule text at line 180: "the routing artifacts state no measurement"; the pointer-to-the-budget-report exemption at line 4326).

But the analysis misses the decisive fact about that home. `.gitignore` line 8 excludes `.syzygy/cache/` from version control:

```
# Rebuildable projections — never a source of truth (VIS-6)
.syzygy/cache/
```

`git check-ignore -v .syzygy/cache/x` returns `.gitignore:8` — `[Observed]`. So under Strategy T's axis C, the two generated reports become **absent from every clone**. The analysis's Strategy T table nevertheless states at line 313:

> | Clone visibility | Same content, typed homes |

That row is false for the reports. It is the one row in the T column that reads as a non-cost, and it is the row where T's cost is largest: the budget report is the cited home of every volatile measurement in the package, and axis C as specified would put it where no clone can read it. This is a typing failure with a concrete consequence, not a hedge.

The other four classes type correctly: `history/` and `matrix-rows/` are not contracts (their own README is quoted in the acceptance record as stating "Nothing in this directory binds", `:171–172`); `ACTIVE-CONTRACT-MANIFEST.txt` is not a contract; the accepted modules are.

**JUDGEMENT: FAIL** — on the `cache/` limb. The RFC3-15 typing passes; the RFC3-20 typing reaches the right verdict on the wrong evidence and asserts a clone-visibility property that the repository's own ignore file contradicts.

---

# D. Navigability

**METHOD.** I read the packet once as an outsider would, listing every proper noun, figure, path, identifier and rule it uses without carrying, and then checked each against the repository to see whether it is resolvable at all. I treated "could rule from the packet alone" as: can the reader (i) understand the question, (ii) verify or at least locate every load-bearing figure, (iii) understand what each option costs, without opening the analysis or any history.

**OBSERVATION.**

The packet is genuinely well shaped for this. It is short, it states the question in one sentence, it quotes the clause it turns on, it gives two options with parallel cost blocks, it names the trade in a single interrogative sentence, and it carries an honest counter-argument. A capable engineer would understand what is being asked. That is a real improvement and I want it on the record before the list of gaps.

Things the reader must open that the packet does not carry:

1. **The owner charter itself.** The packet's departure rationale (lines 118–125) rests entirely on "the charter's steer" and "the owner charter directs…". It gives no path, no identifier, no date, no quotation of the instruction. My repo-wide sweep found the instruction in exactly one artifact: an **untracked file at the repository root**, `syzygy_fable_opus_owner_spec_launch_closure_prompt.md`. It is not under `.syzygy/`, not under `decisions/`, not in `02-OWNER-DIRECTION-RECORD.md`, and not in `PENDING-OWNER-DECISIONS.md`. A reader who wants to check whether the packet is departing from the instruction faithfully cannot find the instruction. Worse, a reader in a fresh clone cannot find it at all — `git status` shows this file class as untracked.
2. **What "RD-31b", "RD-32c", "RD-49" are.** The packet cites three review identifiers as the reason two confirmations exist and one rewrite happened (lines 7, 97, 184-adjacent). None is expanded, dated, or located. Under (T) the reader is told two `CONFIRM` verdicts "stop covering anything" without ever being told what they covered.
3. **The argument digest `8972d963…`** (line 180) is truncated and its source file is named only in the front-matter note, not beside the figure.
4. **The 87 figure's method.** The packet says "87 backtick path strings" and "swept over all 39 modules" but never states that the sweep was restricted to backtick spans, which is exactly the restriction that made it miss the 88th reference. A reader cannot tell what was and was not swept.
5. **What "the ceremony" currently says.** The packet's whole question is whether the install ceremony breaches RFC3-15, and it never quotes the ceremony. The reader must open `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:142–193` to see the six install copies at issue.
6. **`.syzygy/cache/` and the history home.** These appear in the analysis's Strategy T (axes C and D) but not in the packet's (T). The packet's (T) says only "Same homes, plus every internal reference repointed" (line 83), which is *not* Strategy T as the analysis defines it — the analysis's T also relocates reports to `cache/` and rationale to a named history home, and it is that relocation which generates the "unless a history home is minted under `governance/`" amendment caveat the packet then reproduces at lines 89–91 without ever explaining what history home. The packet's (T) is internally incomplete: it carries a caveat about a thing it never mentions.
7. **Whether doctrine forbids dangling references.** The packet asserts no clause requires resolution, sweeping the 39 candidate contract modules — which bind nothing today. It never checks doctrine, which is the only binding authority in this repository. I checked: VIS-7 and the trust floor's bullet 2 scope the link rule to "every **rendered internal project-entity link** — code, requirement, work item, capability, evidence, decision, and map entity" (`doctrine/trust-and-evidence.md:119–123`, `vision.md:183–193`), so it does **not** reach a path string in a contract module's prose. The packet's conclusion survives — but VIS-7's violation clause reads "*Violation:* a dangling internal link", and an owner asked to accept 88 dangling strings in the governance tree will think of VIS-7 immediately. The packet does not raise it, so the reader must go and check it themselves.

**JUDGEMENT: FAIL.** The packet is close, and items 3–5 alone would be MINOR. Items 1, 6 and 7 are not: the reader cannot locate the owner instruction the recommendation departs from, cannot see what option (T) actually is, and is not shown the one binding rule that appears to bear on the question.

---

# E. Epistemic honesty

**METHOD.** I enumerated every substantive claim in the packet and asked three things of each: does it carry a label; if it carries `[Observed]`, is it a measurement rather than a reading; and does the sentence decide anything. I then checked whether the counter-argument states the opposing case at its strongest or at a strawman's strength.

**OBSERVATION.**

*Does the packet decide, bind, or perform an act?* **No.** It opens "**This file decides nothing**" (line 3), states there is no ceremony phrase and that this is "a recorded owner decision, not a digest-binding act" (line 169), and ends with a blank template for the owner to fill in their own words (lines 172–176). The analysis opens with the same disclaimer and adds that no confirmation is retired. Nothing in either file installs, edits an accepted module, or claims an act occurred. This is correct and I found no exception. VIS-4 is respected.

*Does it preserve the trade-off?* **Yes, and unusually well.** The "Honest counter-argument" (lines 128–133) states the case for (T) at full strength — "a governance home containing pointers to nowhere is a defect regardless of what any clause requires… the confirmations were obtained once and can be obtained again; the installed tree is read for years" — and explicitly says taking (T) "is a legitimate ruling and not a mistake". It then locates the `[Inferred]` precisely: "sits on the weighting, not on the measurement". That is the correct placement and it is the best paragraph in the packet. No consensus-smoothing.

*Labelling.* Here it fails. The packet carries exactly two labels, both `[Inferred]`, both on recommendations (lines 100, 151). **Every figure in the two cost blocks is unlabelled** — "0", "87", "up to 30 modules", "survives", "RETIRES", "none". Criterion D says the packet must stand alone; standing alone, it presents a dozen quantities with no epistemic status at all. The analysis labels them `[Observed]`; the packet does not inherit labels by reference.

*An inference presented as measurement.* Lines 76–79:

> The same string resolves in any clone of this repository, and no clause requires it to resolve — swept over all 39 modules, 9 hits for link-obligation language, **all of them runtime rendering clauses about product surfaces**.

The count (9 across 39 modules) is a measurement; I reproduced it exactly — 9 lines across 6 of 39 modules. The classification "all of them runtime rendering clauses about product surfaces" is a **reading of nine sentences by a language model**, and it is presented inside the same clause as the count, in the same unlabelled sentence, with the measurement's authority. That is the failure mode the repository's own discipline names. It also is not quite right: `rfcs/RFC-0006-cross-surface-selection-query-drawer.md:378` reads "Citations of doctrine rules **and accepted contracts** … if a surface renders such a citation *as a link*, that link must resolve to the identified artifact" — a clause about citations of accepted contracts, which is closer to the subject matter than "product surfaces" suggests, even though the rendering condition is what saves it. And the analysis's own enumeration of the nine (`:170–174`) names RFC1-11, RFC6-20, RFC7-3, RFC8 and RFC9 — five sources for hits that my sweep locates in **six** modules, the missing one being `rfcs/RFC-0004/named-adapters.md:82`. An enumeration offered as the content of a nine-item denominator should name all six.

*One unlabelled false statement of fact.* Line 41, "that manifest is 19 per-module digest rows and nothing else", is not hedged, not labelled, and not true (criterion B). It is the premise of the bolded rule immediately beneath it.

**JUDGEMENT: FAIL.** The packet does not decide, does not bind, and preserves the trade-off honestly — those are the hard parts and it gets them right. But the measurements are unlabelled in the document that must stand alone, and a model's classification of nine clauses is folded into a sentence that reads as a sweep result.

---

# F. The recommendation

**METHOD.** I isolated the load-bearing claim as a testable proposition — *the layout the charter calls "clean typed" is reachable under (M) without moving an accepted byte, therefore cleanliness and economy are not in tension* — and tested it in two steps. First I obtained the charter's actual definition of the typed layout rather than the packet's paraphrase of it. Then I enumerated, home by home, what the tree would contain after a Wave A act under (M), from `ls` output plus the acceptance record's install steps, and compared the two.

**OBSERVATION.**

The charter's Strategy T layout, quoted exactly (prompt lines 337–349):

```text
governance/contracts/rfcs/
    accepted normative modules only

governance/decisions/ or governance/records/
    owner act and integrity-bearing membership manifest

.syzygy/cache/
    rebuildable generated indexes and measurements

governance/history/ or immutable Git identities
    non-authoritative rationale and review evidence
```

and the steer, quoted exactly (prompt lines 367–369):

> Given Syzygy's stated priority of human interpretability and typed authority, prefer the clean typed layout **unless** the owner explicitly chooses confirmation preservation over installed-tree self-containment.

The packet's characterisation of the steer (lines 118–120) is **faithful**. Its claim that the steer "assumed typing and preservation were in tension" is also a fair reading of the charter, which pairs Strategy T with "confirmed bytes may need amendment; confirmation may retire". So the *form* of the departure argument is legitimate: if typing turned out to be free, the charter's condition would indeed not be engaged.

Now the substance. Under option (M), after the Wave A act, the four typed homes stand as follows:

| Charter's typed home | What (M) actually produces | Typed? |
|---|---|---|
| `governance/contracts/rfcs/` — accepted modules only | `governance/contracts/rfcs/` — accepted modules only | **yes** |
| `governance/decisions/` — act + membership manifest | manifest quoted inline in `decisions/ACCEPTANCE-ACT-RECORD.md` | **yes** |
| `.syzygy/cache/` — rebuildable generated measurements | reports remain at `governance/contracts/candidates/CONTEXT-BUDGET-REPORT.md` and `…/03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` | **no** |
| `governance/history/` — non-authoritative rationale | rationale remains at `governance/contracts/candidates/history/` | **no** |

Two of the four typed homes are not achieved by (M). And the failure is not cosmetic, because both unachieved homes leave their content **inside `.syzygy/governance/contracts/`** — the very category whose "exclusively" is the entire subject of P-33.

The packet's own argument forecloses the only escape. Its typing rule is that the cell names contracts (RFCs) and nothing else, so "a wave manifest is not an RFC; neither is a history file, a matrix-row file, or a generated report" (line 35). That rule does not become weaker one directory deeper. If `contracts/history/` is excluded by the cell, `contracts/candidates/history/` is excluded by the same words — "may contain" is about contents, and the analysis has already ruled out timing as a cure ("'exclusively' bounds *what the category may contain*, not when it came to contain it", `:256–257`). The same reasoning disposes of depth.

So the two claims that carry the recommendation are false:

- Packet line 55: "Both options put accepted modules at `contracts/rfcs/` and **nothing else in `contracts/`**". Under (M), `contracts/` holds `candidates/` **and** `rfcs/`. `[Observed]` — `ls .syzygy/governance/contracts/` returns exactly `candidates`, and the acceptance record's step-3 rule (`:157–159`) establishes that a wave act does not delete the candidate home.
- Analysis line 288: "Contract-category purity | **Full.** `contracts/` holds `rfcs/` and nothing else". Same defect, stated as a measured property in a cost table.

And therefore the load-bearing claim itself — analysis lines 319–330, "**Strategy T's typing is available without paying for it**… the clean type boundary the charter argues for is achieved by *declining to install the companions*" — does not hold. Declining to install the companions leaves them where they already are, and where they already are is inside the category. The charter's condition ("unless the owner explicitly chooses confirmation preservation over installed-tree self-containment") **is** engaged after all, because under (M) as offered the owner is choosing preservation over *both* self-containment and typed containment.

The recommendation may still be the right one. I want to be clear that I am not ruling for (T). What I am finding is that the stated reason for departing from the owner's steer is unsound, and it is unsound in the direction that makes the departure look free.

The repair is available and cheap, which is why I regard this as fixable rather than fatal. Option **(M+)** from criterion A — (M) plus relocating the candidates tree to a home outside `.syzygy/governance/`, licensed by the analysis's own axis row `D''` — makes the packet's central claim *true*: it delivers `contracts/` holding `rfcs/` and nothing else, at zero accepted bytes, with both confirmations surviving, and with no RFC3-15 amendment. With (M+) offered, the departure from the charter's steer is properly grounded, because the typed boundary genuinely would be reachable without moving a byte, and the residual choice genuinely would be axis E alone.

**JUDGEMENT: FAIL.** Tested hard, as instructed, and the load-bearing claim does not survive contact with `ls`.

---

# Findings

**1. BLOCKING — the typed layout is not achieved under the recommended option, which is the packet's entire reason for departing from the owner's steer.**
*Against:* `.syzygy/governance/decisions/WAVE-A-INSTALL-SHAPE-DECISION.md:55` and `:105–108`; `round-2026-08g/P33-SEMANTIC-INSTALL-ANALYSIS.md:288` and `:319–330`.
*Evidence:* `ls .syzygy/governance/contracts/` returns exactly one entry, `candidates`. That directory holds `history/`, `matrix-rows/`, `CONTEXT-BUDGET-REPORT.md`, `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md`, `ACTIVE-CONTRACT-MANIFEST.txt`, `wave-manifests/`, `reviews/`, `scripts/`, seven `round-*/` trees and the 39 draft modules. The acceptance record establishes that a wave act does not delete the candidate home (`:157–159`, act 3's rule) and names `.syzygy/governance/contracts/candidates/` as the tracked source home present in every clone (`:239`). After a Wave A act under (M), `contracts/` therefore holds `candidates/` **and** `rfcs/`. The packet's own typing rule ("a history file is not an RFC", packet `:35`) excludes that content from the category regardless of nesting depth, and the analysis has already rejected the only alternative cure — "'exclusively' bounds *what the category may contain*, not when it came to contain it" (`:256–257`).
*Fix:* Either (a) add option **(M+)** — (M) plus relocating `contracts/candidates/` to a home outside `.syzygy/governance/`, which the analysis's own axis row `D''` (`:241`) establishes needs no amendment and moves no accepted byte; verify with `build_active_manifest.py --check` that the wave manifests are byte-identical after the move (they will be: rows are candidates-root-relative, `build_active_manifest.py:137–140, 187–189`) — and recommend from the corrected space; or (b) state plainly that neither offered option achieves contract-category purity, delete the "Full" purity rows and the "nothing else in `contracts/`" claim, and re-derive the recommendation against the charter's condition, which is then genuinely engaged.

**2. BLOCKING — the mechanical confirmation-retirement rule is unsound in the direction the packet relies on, because its premise about the manifest's contents is false.**
*Against:* `WAVE-A-INSTALL-SHAPE-DECISION.md:41` and `:43–44` and `:50`; `P33-SEMANTIC-INSTALL-ANALYSIS.md:134–148`.
*Evidence:* `WAVE-A-MANIFEST.txt` is not "19 per-module digest rows and nothing else". Its first four lines are generated comments (`build_active_manifest.py:224–232`), the fourth of which reads `# This file's own sha256 is the argument of the phrase \`ACCEPT FOUNDATIONAL WAVE A: <sha256>\`.` The argument is `sha256` of the whole file, header included — recomputed this session as `8972d9630b95f5d4266432dbb1b3602114576bbd6c0f29d6f9bd6f905b1f884a`, matching the acceptance record `:22`. So a ceremony change that renames the acceptance phrase regenerates the header, regenerates the argument, and retires the confirmation **without editing any manifest row** — contradicting both the "if and only if" rule and the bolded "costs nothing" at line 50. Phrase retirement is not hypothetical here: the acceptance record §1a records two prior retirements (`:74–82`).
*Fix:* Replace the rule with the correct one — *the argument regenerates iff the wave manifest's byte-stream changes, i.e. if any listed module's digest changes, any row's path string changes, or any of the four generated header lines changes (including the line naming the acceptance phrase)* — quote the four header lines in the packet so the owner can see what is in the argument, and re-check the "costs nothing" claim against it. Add an explicit caveat to the "Exact next transaction" section that drafting the ceremony to match must not alter the phrase, or the ruling's own zero-cost property is destroyed.

**3. MATERIAL — Strategy T's clone-visibility row is false: `.syzygy/cache/` is gitignored.**
*Against:* `P33-SEMANTIC-INSTALL-ANALYSIS.md:313` ("Clone visibility | Same content, typed homes"), and axis row `C'` at `:237`.
*Evidence:* `.gitignore:8` excludes `.syzygy/cache/` under the comment "Rebuildable projections — never a source of truth (VIS-6)"; `git check-ignore -v .syzygy/cache/x` confirms. Under axis C, `CONTEXT-BUDGET-REPORT.md` and `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` become absent from every clone. This compounds the RFC3-20 objection the analysis already raises correctly — the budget report is the cited home of every volatile measurement (CG-20, `check_governance.py:180`, `:4326`) and cache may not be "the only home of any fact" (`manifests-and-namespace.md:360–361`).
*Fix:* Correct the row to "Clone visibility | **Generated reports become absent from every clone** — `.syzygy/cache/` is gitignored (`.gitignore:8`); rationale and manifests unchanged", and promote axis `C'` from "lawful but contestable" to "lawful only if the reports' role as the cited home of every volatile measurement is first re-routed **and** their disappearance from clones is accepted".

**4. MATERIAL — the companion-reference count is low by one, and its method is scoped to backticks in a way the packet does not disclose.**
*Against:* `WAVE-A-INSTALL-SHAPE-DECISION.md:69` and `:74`; `P33-SEMANTIC-INSTALL-ANALYSIS.md:101`, `:115`, `:126`.
*Evidence:* Raw-text sweep of all 39 modules finds `history/` **77** times against 76 inside code spans. The 88th reference is bare prose at `rfcs/RFC-0001-project-graph-identity-state-planes.md:83`: `[Observed: ../history/RFC-0001-history.md, the K-F1/K-F2 narrative]`. This is a Wave A module, so the correct split is **45 / 33 / 10 = 88**, not 44 / 33 / 10 = 87. Because the string carries no backticks it is invisible to a code-span sweep and would survive a rewrite pass scoped to code spans. Separately, `rfcs/RFC-0003/manifests-and-namespace.md:604` cites `` `round-2026-08e/WAVE-A-SEMANTIC-DELTA.md` ``, which resolves neither today nor after install, contradicting the packet's "resolves in any clone of this repository" (`:76`) for at least one member of the candidate-tree pointer population.
*Fix:* Re-run the sweep over raw text, not code spans; restate the total as 88 with the per-wave split 45 / 33 / 10; state the method's scope in the packet itself ("path references in module prose, whether or not in backticks"); and disclose the one pointer that resolves nowhere today.

**5. MATERIAL — the reader cannot locate the owner instruction the recommendation departs from.**
*Against:* `WAVE-A-INSTALL-SHAPE-DECISION.md:118–125`.
*Evidence:* A repo-wide sweep of 774 `.md/.txt/.yaml/.json/.py` files finds the phrase "clean typed layout" in exactly 5 places: packet `:119`, `:122`; analysis `:292`; and lines 333 and 368 of `syzygy_fable_opus_owner_spec_launch_closure_prompt.md`, an **untracked file at the repository root**. It is not in `02-OWNER-DIRECTION-RECORD.md`, not in `decisions/PENDING-OWNER-DECISIONS.md`, and not under `.syzygy/`. The packet cites the instruction four times and gives no path, date or quotation. A reader in a fresh clone cannot find it at all.
*Fix:* Quote the instruction verbatim in the packet (the two sentences at prompt lines 367–369 and the four-home block at 337–349 are enough), and cite where it is recorded. If it is not recorded in a tracked governance artifact, record it — a recommendation cannot depart from an instruction the tree does not carry.

**6. MATERIAL — option (T) as the packet describes it is not the strategy whose costs the packet quotes.**
*Against:* `WAVE-A-INSTALL-SHAPE-DECISION.md:81–98`.
*Evidence:* The packet's (T) is "Same homes, plus every internal reference repointed at its new location" — axis E alone. But the analysis's Strategy T (`:296–300`) also sets axis C to `.syzygy/cache/` and axis D to "a named history home". The packet then reproduces a cost caveat that only the analysis's T generates — "none, unless a history home is minted under `governance/` — that amends the closure sentence" (`:89–91`) — referring to a history home its own description of (T) never mentions. The reader is shown a caveat about a component that has been removed from the option.
*Fix:* Either restore axes C and D to the packet's (T) description (and carry finding 3's clone-visibility cost with them), or delete the history-home amendment caveat, which does not arise under (T)-as-described. The two must agree.

**7. MATERIAL — measurements in the packet carry no epistemic labels, and one model reading is presented inside a sweep result.**
*Against:* `WAVE-A-INSTALL-SHAPE-DECISION.md:64–72`, `:85–94`, `:76–79`.
*Evidence:* The two cost blocks present roughly a dozen quantities with no `[Observed]` / `[Inferred]` / `[Unknown]` label; only the two recommendations are labelled. The analysis labels its figures; the packet does not inherit labels by reference, and criterion D requires the packet to stand alone. Separately, line 79's "9 hits for link-obligation language, all of them runtime rendering clauses about product surfaces" fuses a reproducible count (I reproduced 9 hits across 6 of 39 modules) with a model's classification of nine sentences, in one unlabelled clause. The classification is also imprecise: `RFC-0006:378` governs citations of "doctrine rules **and accepted contracts**", not only product surfaces, and the analysis's enumeration of the nine (`:170–174`) names five sources for hits my sweep locates in six modules, omitting `rfcs/RFC-0004/named-adapters.md:82`.
*Fix:* Label every figure in both cost blocks `[Observed]`. Split line 79 into a labelled measurement ("`[Observed]` 9 hits across 6 of 39 modules") and a labelled reading ("`[Inferred]` each governs rendered runtime references, not governance-tree file paths — the nearest case is RFC6-20, which binds only where a surface renders a citation as a link"). Correct the analysis's enumeration to name all six modules.

**8. MATERIAL — (M) removes the installed tree's integrity artifact and breaks the ceremony's own verification step, and neither cost block says so.**
*Against:* `WAVE-A-INSTALL-SHAPE-DECISION.md:59–72`.
*Evidence:* Ceremony step 3 verifies the copy by running `sha256sum -c wave-manifests/WAVE-<X>-MANIFEST.txt` **from `.syzygy/governance/contracts/`** (`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:149–151`). Option (M) does not install the wave manifest, so that command has nothing to read from that directory. The repair is ceremony-only and therefore free under the corrected rule of finding 2 — but the consequence for a *future* reader is not free: under (M) the accepted tree contains no digest list against which its 19 modules can be re-verified without leaving it. (M)'s block lists "re-review required: none" and is silent on both points.
*Fix:* Add a row to (M)'s cost block — "in-tree integrity artifact: none; re-verification requires the digests quoted in the act record" — and note in "Exact next transaction" that ceremony step 3's verification command must be re-pointed at the candidates tree.

**9. MINOR — "up to 30 modules" understates a certainty.**
*Against:* `WAVE-A-INSTALL-SHAPE-DECISION.md:86` and `:165`; `P33-SEMANTIC-INSTALL-ANALYSIS.md:304`.
*Evidence:* Every Wave A module (19 of 19) and every Wave B module (11 of 11) carries at least one out-of-tree reference. Under axis E' all 30 launch-path rows change; there is no "up to" about it.
*Fix:* State "all 30 modules (19 Wave A + 11 Wave B); measured — every module in both waves carries at least one such reference".

**10. MINOR — the `records/` home is not rejected with a rule, though the owner instruction names it.**
*Against:* `P33-SEMANTIC-INSTALL-ANALYSIS.md:231–243` (axis B rows).
*Evidence:* The charter's Strategy T names "governance/decisions/ **or governance/records/**" as the manifest's home (prompt line 341). Axis B enumerates only "inside the owner-act record" and "`contracts/wave-manifests/`". The §7 discipline is to reject a setting only with its stated rule; this setting is not rejected at all. (It *is* excluded — the `records/` cell admits only kernel-authored facts minted on a non-owner actor's submission or by the challenge-sweep policy, `governance-homes-and-owner-acts.md:89` — but the packet must say so.)
*Fix:* Add the row with that quotation as its rule.

**11. MINOR — no binding authority is checked; only candidate contracts are swept.**
*Against:* `WAVE-A-INSTALL-SHAPE-DECISION.md:76–79`; `P33-SEMANTIC-INSTALL-ANALYSIS.md:163–181`.
*Evidence:* The "does any clause require an installed path string to resolve" sweep covers the 39 candidate modules, which bind nothing today. Doctrine binds. VIS-7 states the trust floor and its violation case is "a dangling internal link" (`doctrine/vision.md:191`); the normative rule at `doctrine/trust-and-evidence.md:119–123` scopes it to "every rendered **internal project-entity link** — code, requirement, work item, capability, evidence, decision, and map entity". I checked and the rule does not reach a governance-tree path string in module prose, so the packet's conclusion survives — but an owner asked to accept 88 dangling strings will think of VIS-7, and the packet does not raise it.
*Fix:* Add one sentence: "`[Observed]` Doctrine's link rule (VIS-7, trust-and-evidence.md floor bullet 2) is scoped to rendered internal *project-entity* links across seven named entity classes and does not reach a file path in a contract module's prose; the 88 strings do not engage it."

**12. MINOR — both files elide the sentence that most nearly argues against their typing.**
*Against:* `WAVE-A-INSTALL-SHAPE-DECISION.md:24–25`; `P33-SEMANTIC-INSTALL-ANALYSIS.md:26–29`.
*Evidence:* Both quote the `contracts/` cell and cut its install-gate column at "…". The elided text is "that record owns the acts, their exact phrases, and **their arguments**" — and the argument *is* the wave manifest. It is a statement about authority, not residence, so it does not admit the manifest into the category; but it is the strongest text against the ruling and neither file shows it.
*Fix:* Quote the cell's third column in full in both files, and add one sentence distinguishing gate authority from residence.

---

# What I could not test and why

- **Whether a re-review of the regenerated arguments would return `CONFIRM` again.** Only a re-administration answers it. The analysis says so at `:361–363` and I agree; nothing in my sweep bears on it.
- **The prior reviews RD-7, RD-18, RD-26, RD-30, RD-31b, RD-32c, RD-47, RD-48, RD-49.** I was instructed not to read `reviews/` directories and did not. Every claim I make about them is either quoted from the acceptance record or from the two subject files, and I take none of them as established. In particular I did not verify that RD-31b and RD-32c returned `CONFIRM`, nor that RD-49 returned `REVISE` with three BLOCKING findings — I read those as claims by the subject files, and the exceptional weight the packet's economy argument places on the two confirmations rests entirely on facts I could not check.
- **`round-2026-08d/POST-INSTALL-LINK-REPORT.md`.** The acceptance record (`:188–192`) says this file re-runs RD-7's sweep with the companion copy in place and records the remaining unresolved population with its denominator — which is the closest thing in the repository to a competing measurement of the quantity at issue. It is a round report and I did not open it. My 88 and its figures may or may not agree; I could not reconcile them.
- **Whether the candidates tree can in practice be relocated (option M+) without breaking the check battery.** I verified that the wave-manifest bytes are location-independent by reading the generator's path handling, but I did not execute the move, did not run `check_governance.py`, and did not audit how many other artifacts cite `contracts/candidates/…` by path. The relocation's zero-accepted-byte property is `[Observed]` from the generator source; its total cost is `[Unknown]`.
- **The full owner charter.** I read only prompt lines 300–384. Sections §6.1, §6.2 and everything outside that window are unread, so I cannot say whether the charter elsewhere anticipates the containment problem in finding 1 or already forecloses option (M+).
- **Whether `decisions/` may hold an attached manifest `.txt`.** The analysis flags this as a genuinely open reading (`:355`). I read the `decisions/` cell (`governance-homes-and-owner-acts.md:88`) and agree it neither admits nor excludes one. It is an owner question, not a measurement, and I did not attempt to resolve it.
- **How many of the 182 in-`rfcs/` code-span references survive the install unchanged.** I confirmed they resolve inside `rfcs/` today and that the install preserves the package directory structure (`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:142–144`), but I did not simulate the copy, so "all 182 survive" is `[Inferred]` from the structure-preserving copy rule, not measured against an installed tree.