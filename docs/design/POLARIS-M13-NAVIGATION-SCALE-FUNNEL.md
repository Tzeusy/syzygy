# Feature request M13 — Navigation at population scale: labels that name their subject, an outline that indexes the page, and a source record you do not have to open 278 times

> **Candidate — binds nothing.** Bead `syzygy-dov.13`, move M13 of the
> 2026-09-13 vision pursuit (`docs/pursuits/2026-09-13-vision-pursuit.md`,
> section "### M13" at line 420), written in the shape of
> `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` and its twelve siblings.
> Planning only: nothing here authorizes implementation. This packet names
> lawful arms for the owner to take; it rules no slice authorized or
> unauthorized, and the owner disposes.

Date: 2026-09-15. Author: a funnel session (Claude), for the owner.

Size: **small** (slices 1 and 2) / **medium** (slice 4) / **large** (slices 3
and 5).

Baseline: Syzygy `a9f671e` (main). The subject is the rendered Polaris human
page and the renderer that emits it.

**Line-count convention, stated once.** A "line N" below is the one-based
index into the split-on-newline segments of the file at `a9f671e` — the
number `sed -n 'Np'` prints. A byte count is the UTF-8 length.

**Capture convention, stated once.** Two captures are read. The **post-trim**
capture is the retained lane A "after" capture, `polaris-direct.html`
(1,478,637 bytes) and `polaris-tailnet.html` (1,484,487 bytes), served at
Syzygy `2ef68f5` against Butlers revision `2e3bac97790b4bd8906dcac63eadb5642a0bb1ac`
and recorded in `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`.
The **pre-trim** capture is the earlier `polaris-7478.html` the dossier
audited (2,090,025 bytes as it sits on disk). Every figure below names which
capture it is measured on and gives that capture's byte count as its
denominator. No daemon was started this session and the loopback daemon on
port 7478 was never contacted.

## The five questions for the owner

Batched, recommended answer first. Everything below is the evidence behind
them. Q1 is the packet's central question: three of the five slices change
what a script would have to do, and the page carries exactly one script
today.

| # | Question | Recommended |
|---|---|---|
| Q1 | **May client-side filtering or pagination be added to Polaris as progressive enhancement, given the page's current one-script posture?** Measured this session: the post-trim capture carries exactly **1** `<script` element, `SECTION_NAV_SCRIPT` (`apps/three-surface-poc/src/polaris.ts` lines 1232–1289); the pre-trim capture carried **2**, the second being the narrative JSON that lane A removed. The page carries **0** `<noscript>` elements; the only `<noscript>` in the app is Orrery's (`apps/three-surface-poc/src/orrery.ts` lines 144–146). Nothing in either specification, in doctrine, or in any decision constrains client-side scripting on Polaris by name: over the 7 files of `openspec/changes/three-surface-poc-experience`, the 15 of `openspec/changes/polaris-project-wide-butlers-model`, the 6 of `.syzygy/governance/doctrine` and the 67 of `.syzygy/governance/decisions`, a case-insensitive sweep for script, javascript, "progressive" and "without JavaScript" returns **0** sentences constraining the page's own scripting in doctrine and **0** in decisions; the specification hits are POC-REQ-021 and POC-REQ-022, quoted in Gate 5. | **Progressive enhancement over the native disclosure, never a script the reader needs** — with the server-rendered complete population always present, which is POC-REQ-022's own bar. **Every lawful arm:** (a) *no script* — a server-rendered "first 20 / all" pair of disclosures, zero new script, zero new state, more bytes; (b) *progressive enhancement over native `<details>`* — the recommended arm, the population always served, a script that only hides; (c) *server-side paging by route* — a `?page=` or `?prefix=` parameter on the Polaris route, no script at all, but it makes the page's identity depend on a query parameter and multiplies the routes PWB-REQ-011's depth sweep must enumerate. **Counter-argument to the recommendation, and it is the strong one:** arm (b) is the only arm that creates *hidden* content, and RFC9-13 — quoted in Gate 2 — says in terms that "A filter that hides entities shows a persistent count of what it hid", so arm (b) buys its convenience with a new invariant the checker must hold. **Default if unanswered: no filter and no pagination ships**; slices 1, 2 and 4 are unaffected, and slice 3 proceeds in its no-script form. |
| Q2 | **May the source-record disclosure be re-formed into columns of the table it already sits in — and if a PWB scenario requires the disclosure form, is that re-forming an amendment through CC-REV-2?** The dossier reads the 278 source records as free-standing disclosures to be "collapsed into one filterable, grouped source table". Measured at source: they are **already** rows of a table. `apps/three-surface-poc/src/polaris.ts` line 836 returns one `<tr>` per source, and line 835 builds a `<details class="source-record">` that sits *inside* that row's second cell. So the slice is not "build a table"; it is "hoist four fields out of a disclosure into columns of the table around it". Swept this session: the literal string "details" occurs **0** times across all 7 files of the POC-experience change and all 15 of the PWB change, and no scenario in either specification prescribes a disclosure element for the source record. What the specifications do require is the *content* — PWB-REQ-001's revision-bound source identity, PWB-REQ-003's reason and Unknown denominator, PWB-REQ-007's complete epistemic state — all of which survive the hoist. | **Yes, hoist it; no CC-REV-2 delta is needed, because no scenario names the form.** The disclosure costs a reader one interaction per source to see four fields that fit in three columns, and it costs the page 53,376 bytes of pure scaffolding (Gate 4). **Counter-argument:** PWB-REQ-011's invariant is that "A reader who stops at any level SHALL retain a true, coarser account", and the disclosure *is* a level; flattening it removes a stopping point and puts 278 rows × 4 fields in front of a reader who wanted the path column. That is a comprehension trade-off VIS-1 ranks second, and it is the owner's to weigh, not this packet's. **Second lawful arm:** keep the disclosure, and put only the identity and the outcome in new columns — half the saving, no level removed. **Default if unanswered: the second arm.** |
| Q3 | **Is interpolating the item identity into the two shared labels a change to rendering vocabulary under RFC2-26, or an engineering decision inside the existing act?** `apps/three-surface-poc/src/polaris-copy.ts` line 129 defines `label.source-record` as the literal 'Source record' and line 134 defines `label.exact-text` as 'Exact text'. On the post-trim capture, **278** `<summary>` elements read literally 'Source record' and **386** links read literally 'Exact text'. Those two strings are rows of the closed copy table PWB-REQ-012 governs, and PWB-REQ-012's oracle is a hand-typed one (`apps/three-surface-poc/src/polaris-copy.test.ts`). Interpolating a subject into them turns two fixed strings into two templates. | **It is an engineering decision inside the existing act, not an RFC2-26 consequence of RFC-0002.** RFC2-26 bars scheduling implementation work for user-observable consequences **of RFC-0002** from that RFC alone; this work is scheduled from PWB-REQ-012 and PWB-REQ-016, both approved OpenSpec requirements with scenarios, and Gate 5 runs the test per slice. **Counter-argument:** PWB-REQ-012 declares a *closed* set of roles and a word-and-term rule over owner-visible strings, and a label that varies per instance is no longer a row of a closed table in the sense the requirement's oracle assumes — an owner who reads "closed" strictly may want the templating ruled rather than inherited. **Second lawful arm:** rule it a vocabulary change and put a CC-REV-2 scenario to PWB-REQ-012 first. **Default if unanswered: slice 1 ships the suffix form** (label first, subject appended), which the existing oracle's own `startsWith` predicate already admits (Gate 6 item 5). |
| Q4 | **Adding any filter introduces personal presentation state the bound contract-coverage matrix records PWB as not having. Does the owner want the filter kept stateless, or the coverage judgment re-opened?** `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0007-0009.md` line 175 carries the row `RFC9-13.c1`, whose applicability cell reads, verbatim: "No camera/filter/bookmark state", and whose verdict is `believed-not-applicable`. That file is one of the eleven rows of the manifest the 2026-09-05 truth-and-readiness act signed (`.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`), so it is a bound byte and **may not be edited**. | **Keep the filter stateless — nothing stored, nothing restored, the count of what is hidden rendered beside the control — so the row stays true and RFC9-13's own sentence is satisfied by construction.** A stateless filter has no camera, no bookmark and no saved selection; only a live hidden count. **Counter-argument:** a filter a reader must re-apply on every load is the filter they stop using, and the owner may prefer a remembered prefix, which is exactly the state that row denies. **Second lawful arm:** accept the stateful filter and route the coverage row through CC-REV-2 with a new owner act, since the bound bytes cannot be corrected in place. **Default if unanswered: no filter ships** (the same default as Q1), and the row stays true because nothing changed. |
| Q5 | **Are slices 3, 4 and 5 presentation-only inside the bounded non-release POC, or do they trip an escalation trigger of the implementation authorization?** `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` lines 150–156 read, verbatim: "Stop and return to the owner before proceeding if implementation would need any of: a change to doctrine or an accepted contract; a further amendment to the signed PWB specification beyond the 2026-09-05 package; a change to security, privacy, or retention posture beyond the 2026-09-05 approved secret-classification policy; a change to the constraints or envelope the 2026-09-05 registry entry declares; any observation outside the consented content class or repository; or any scope beyond the signed change." Gate 3 tests each slice against that sentence. | **Slices 1, 2 and 4 trip no trigger on any reading; slices 3 and 5 should be ruled explicitly.** Slices 1, 2 and 4 change only how already-modeled facts are named and indexed: no new read, no new content class, no spec clause needed. Slice 3 removes a disclosure level PWB-REQ-011's depth invariant arguably counts, and slice 5 adds a rendering mode the specification does not describe — both are readings of "any scope beyond the signed change", and this packet does not choose between them. **The two readings, neither chosen here.** (i) The act authorizes implementing the signed change, and a signed change's presentation requirements are satisfied by whatever rendering meets them, so a rendering choice is inside scope [Inferred]. (ii) "Scope beyond the signed change" reaches a rendering mode the specification never contemplated, in which case slices 3 and 5 need a fresh owner direction naming them [Inferred]. **Default if unanswered: slices 1, 2 and 4 proceed; slices 3 and 5 hold.** |

### Decided in this packet, not put to the owner

**The dossier's "prerequisite: none" survives for four of the five slices and
is corrected for the fifth.** The dossier's machine record gives M13 a
`prerequisite` value of `none` over all five merged moves. Re-derived this
session: slices 1, 2, 3 and 4 need no doctrine amendment, no owner act and no
spec amendment *to file*, and slices 1, 2 and 4 need none to land either.
Slice 5 (S4-M6) is the correction: it is the one slice whose recommended
shape touches a **bound** artifact's standing judgment — the `RFC9-13.c1`
row quoted in Q4 — and the dossier's own slice plan opens with "Confirm the
page's no-required-JS posture before adding client-side filtering", which is
the confirmation this packet performs and which turns into Q1 and Q4. So
"prerequisite: none" is true as the dossier meant it (nothing blocks filing)
and incomplete as a reader would take it (Q1, Q4 and Q5 are genuine gates
before landing).

**S2-M3, heading normalization, is ordinary engineering and is stated here as
a decision, not asked as a question.** Swept this session with a
case-insensitive Python `re` pattern for a bare `h1`…`h6` token, the phrase
"heading level" and the word "outline": **0** matching lines over the 7 files
of the POC-experience change, **0** over the 6 doctrine files, and **16**
over the 15 PWB files — every one of the sixteen about the *Butlers source*
grammar, not about a rendered heading level. The nearest sentence is the PWB
specification's line 57, "Heading levels/text, top-level list depth, table
column counts, one-based ordinals and literal keys are exact", which sits
inside the closed extraction grammar (the bullet list at lines 36–62 that
defines how an item is minted from a Butlers file) and governs what the
extractor may read, not what the renderer may emit. No spec sentence fixes a
rendered heading level. The slice's oracle and mutants are in Gate 4.

**The dossier's "372 distinct targets" is wrong, and it was wrong on the
capture the dossier itself audited.** S2-F2 says the 372 'Exact text' links
point "to 372 distinct `/polaris/source?identity=...` targets". Measured on
the pre-trim capture this session: **372** links, **185** distinct hrefs.
Measured on the post-trim capture: **386** links, **192** distinct hrefs. The
correction makes the finding *stronger*, not weaker — the labels are not only
identical to each other, they are identical across pairs of links that go to
the same place, so a reader choosing from the accessibility tree's link list
sees 386 identical names over 192 destinations.

**The dossier's "~150 near-duplicate per-item citation links" in the
architecture group is 89.** Measured on both captures, between
`<h2 id="polaris-group-architecture">` and `<h2 id="polaris-group-catalog">`:
**89** anchors, **2** distinct hrefs, of which one accounts for **88**. The
shape the finding describes is real and more extreme than stated.

**The tab-stop figure needs two numbers, and the dossier published one.** The
dossier's 228 is reproduced exactly on the pre-trim capture under its own
predicate (172 anchors + 53 open-disclosure summaries + 3 `tabindex="0"`
regions before the catalog heading). But the predicate counts anchors that
sit inside a closed `<details>`, and those are not tab stops: the page emits
**0** `<details open>`, so with scripting off every one of the 359
disclosures is closed at load. Counted again with closed-disclosure contents
excluded, the same cut yields **62** tab stops pre-trim and **61** post-trim.
Both numbers are true of different questions and both are published in the
Measurements section. The 226/228 figure is the size of the population a
reader must *pass through* once they start opening things; the 61/62 figure
is what the first Tab key actually walks.

## Gate 0 — Baseline

| Pillar | Present | Constrains this request |
|---|---|---|
| Doctrine | `.syzygy/governance/doctrine/vision.md`, `security.md` | VIS-1, VIS-2, VIS-3, VIS-5, VIS-7; no SEC rule is engaged (no read, no egress, no store) |
| Decisions | `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` (2026-09-02), `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` (2026-09-05), `PWB-TRUTH-READINESS-AMENDMENT-ACT.md` (2026-09-05), `THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md` | the first two are the implementation grant and its continuation, quoted in Q5 and Gate 3; the third binds the eleven PWB artifacts |
| Specification | `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md` (24 requirements, 24 scenarios, 1,008 lines) and `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` (17 requirements, 31 scenarios, 1,152 lines) | PWB-REQ-011, 012, 016, 020; POC-REQ-021, 022, 030, 061 |
| Amendment overlay | **None as a separate directory.** AGENTS.md's overlay rule names an explicit overlay change only for the Polaris *generator* (`openspec/changes/polaris-manifesto-understanding-amendment/`). The PWB 2026-09-05 amendment was performed **in place**: the eleven rows of `.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` include the PWB spec, proposal, design and three coverage-matrix parts, and those are the bytes in the tree today | every PWB citation below is to the current, amended bytes, and every one of those files is a bound byte no slice may edit |
| Contracts | `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md` (RFC2-26, line 196 per `DIRECTIVE-REGISTER.md`), `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md` (RFC7-34, line 241), `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md` (RFC9-13, line 442) | RFC2-26's phase rule, run in Gate 5; RFC7-34's operability limb; RFC9-13's hidden-count rule, which is Q4 |
| Policies | `.syzygy/governance/contracts/candidates/policy-candidates/` (CC-SPEC, CC-IMPACT, in force despite the directory name) | CC-REV-2 is the amendment path Q2's and Q3's second arms would need |

**Three bound-byte constraints this packet obeys.** (a) Every file named in
the Specification and Amendment-overlay rows above is a row of the 2026-09-05
manifest or of the six signed POC-experience artifacts, so **no slice
proposes editing one**; Q2's and Q3's second arms route through CC-REV-2 and
a new act rather than through an edit. (b) Swept this session over the 913
tracked files under `.syzygy/`, `openspec/`, `docs/` and `scripts/`: of the
15 implementation files in this packet's candidate surface, **0** appear as a
row of any of the 66 manifest-named files in that population under a digest,
and **2** appear as a path in one evidence record
(`docs/evidence/polaris-manifesto-example-mutation-2026-09-09.json`, which
names `apps/three-surface-poc/src/polaris.ts` and
`apps/three-surface-poc/src/polaris-first-reading.test.ts` as mutation
targets, not as bound bytes). **No act-bound byte is proposed for edit.**
(c) **Two files in the surface are still at bytes a retained review
confirmed.** `apps/three-surface-poc/src/polaris-reading.ts` and
`apps/three-surface-poc/src/polaris-reading-plan.ts` hash today to the two
values `docs/reviews/R-POLARIS-VISIBLE-DIAGRAMS-FIDELITY-CONFIRMATION-2026-09-10-RAW.md`
lists under "Reviewed file hashes" (verdict, copied exactly: **PASS**); the
same raw lists `apps/three-surface-poc/src/polaris.ts`, whose current bytes
no longer match. Slice 2 edits `polaris-reading.ts`, which retires that
review's binding to it — verification rule 10 applied to a raw review rather
than to a packet. The implementing bead must re-run that bounded fidelity
review. Neither digest is reproduced here; the review is cited by path.

## Gate 1 — Motif

**At Butlers scale the page's names stopped naming anything.** On the
post-trim capture (1,478,637 bytes), **278** disclosure summaries read
literally 'Source record' and **386** links read literally 'Exact text', and
those 386 links resolve to **192** distinct destinations. In the
accessibility tree — the exact non-visual browsing mode this codebase's own
harness inspects, `apps/three-surface-poc/src/polaris-accessibility.ts` —
the links list and the summaries list are therefore two columns of identical
strings. Every one of those 664 controls is individually correct and
individually useless for choosing. That is VIS-3's failure mode arriving not
through a wiring bug but through population: the strings were written and
verified at fixture scale, where four of them is four.

**The outline indexes 11 of the 39 section headings it is the only index
for.** `depthNav` (`apps/three-surface-poc/src/polaris.ts` lines 1529–1556)
emits **33** links: all **7** h2 groups, 4 diagrams, 5 catalog classes, 10
component-guide chapters, 1 deep dive, 5 evidence anchors and 1 exact-source
route. The page carries **39** `<h3>` elements, every one of them with an
id; **11** of those 39 ids are drawer targets and **28** are not. And the
drawer is a `<details>` the page emits with no `open` attribute — **0** of
the page's 359 disclosures are open in the served markup — so with scripting
off the whole outline is behind one summary.

**The heading outline a screen reader builds has a hole in the middle.** The
post-trim capture carries 1 h1, 7 h2, 39 h3, 19 h4, **0** h5 and 14 h6 —
80 headings, and h5 never occurs. Of those 80, **18** are markdown-derived
(emitted by `apps/three-surface-poc/src/polaris-markdown.ts` as a bare
`<hN>` with no attributes): 4 at h4 and **14** at h6. The cause is one
expression, `apps/three-surface-poc/src/polaris-markdown.ts` line 157:
`const level = Math.min(6, heading[1]!.length + 3);`
— a source `#` becomes h4, `##` becomes h5, `###` or deeper becomes h6. No
fragment on this page uses `##`, so h5 never appears, and 14 of 18 land at
h6. The clearest instance sits directly under a page heading:
`<h3 id="polaris-account-v1-scope">` "V1 scope" is followed inside
`.reading-prose` by a bare `<h6>` reading
"Core Infrastructure" with no h4 and no h5 between them — a three-level skip.

**And half the h6s are Syzygy's own choice, not Butlers'.** The nine h6s
under the V1-scope statement come from Butlers prose whose own headings are
`###` (measured from the retained machine capture: the one account statement
carrying markdown headings is `projectAccount[4]`, key `v1-scope`, 9 heading
lines, every one at hash depth 3). The five under the selected-passages block
do not: `apps/three-surface-poc/src/polaris-reading.ts` line 112 *synthesizes*
a heading by prefixing `### ` to a passage title, and that synthesized depth
3 is then mapped to 6 by the same expression. Syzygy picks the depth, and
picks the one that clamps.

**Success criteria, per slice.** Slice 1: no two controls on the page share
an accessible name unless they share a destination. Slice 2: no rendered
heading is more than one level below the heading that precedes it. Slice 3: a
reader sees a source's identity, rule, outcome and digest without opening
anything. Slice 4: every h2 and every h3 on the page is reachable from the
first few tab stops. Slice 5: a class with 192 members is scannable, and
whatever is hidden says how much.

**What M13 is not.** It is not a Butlers change, not a new read, not a new
content class, not a machine-contract change, and not a claim that anything
on the page becomes more true. Every fact, claim id, anchor, parity field and
href the page carries today is carried by every slice below; the only slice
that removes an element is slice 3, and what it removes is a disclosure
wrapper, not a fact.

## Measurements at `a9f671e` and on the retained post-trim capture

Every figure below was taken this session. Method, predicate, denominator and
raw output for each are in the evidence record beside this packet.

### 1. The two labels and their consumers

At `a9f671e`, `apps/three-surface-poc/src/polaris-copy.ts` line 129 is, in
full:

```
  { id: 'label.source-record', role: 'scope-instruction', kind: 'label', text: 'Source record' },
```

and line 134 is:

```
  { id: 'label.exact-text', role: 'action-label', kind: 'label', text: 'Exact text' },
```

**Consumer sweep.** `grep -n -F` for each id over `apps/three-surface-poc/src/`
— denominator **86** files, all of them `.ts`. `label.source-record` occurs on
**2** lines in **2** files: its definition, and `apps/three-surface-poc/src/polaris.ts`
line 835 (the dossier said 818). `label.exact-text` occurs on **3** lines in
**2** files: its definition, `polaris.ts` line 378 and `polaris.ts` line 1549
(the dossier said 1530). Line 378 is the body of the shared helper
`exactTextLink`, whose head at line 377 is `function exactTextLink(identity: string): string {`;
line 1549 is the per-dive link inside `depthNav`. The helper has **5** call
sites in `polaris.ts` — its own definition at 377 plus lines 533, 552, 836
and 1081 — so the dossier's "two sites" is three sites over six references.

The source-record disclosure is built at `polaris.ts` line 835 and consumed
at line 836. Line 836's opening is:

```
  return `<tr id="polaris-source-${escapeHtml(sourceSlug(source.path))}" data-polaris-source="${escapeHtml(source.claim.claimId)}"${block?.attrs ?? FACT}><td>${index + 1}</td><td>
```

— that is, **the source record is already inside a table row.** The
disclosure's four fields (identity, rule and pillar, outcome and anchor,
digest) are the whole of its body.

### 2. Populations, both captures

Predicates, stated once: `<details` counts opening tags; `source-record`
counts the literal `<details class="source-record">`; a "literal 'Source
record' summary" is `<summary…>Source record</summary>`; an "'Exact text'
link" is `<a …>Exact text</a>`; a "distinct target" is a distinct `href`
attribute value (identical after percent-decoding, checked both ways).

| Population | Dossier (S2-F1/F2/F3, S4-M6) | Pre-trim capture, 2,090,025 B | Post-trim capture, 1,478,637 B |
|---|---:|---:|---:|
| `<details>` total | 353 | 353 | **359** |
| `<details class="source-record">` | 271 | 271 | **278** |
| `<summary>` reading literally 'Source record' | 271 | 271 | **278** |
| `<summary>` total | — | 353 | **359** |
| Links reading literally 'Exact text' | 372 | 372 | **386** |
| Distinct source-route targets those links point at | 372 | **185** | **192** |
| All hrefs | — | 1,061 (dossier) | **1,089** |
| `<h1>/<h2>/<h3>` | —/7/39 | 1/7/39 | **1/7/39** |
| `<h4>/<h5>/<h6>` | 19/0/15 | 19/0/15 | **19/0/14** |
| Markdown-derived headings (bare `<hN>`) | — | 4 h4, 15 h6 | **4 h4, 14 h6** |
| `<table>` / `<tbody>` | 10 (dossier LEDGER) | 10 / 10 | **5 / 5** |
| `<script` elements | — | 2 | **1** |
| `<noscript>` elements | — | 0 | **0** |
| `<details open>` in served markup | — | 0 | **0** |
| `tabindex="0"` regions | — | 10 (dossier) | **5** |

The two host forms of the post-trim capture agree on every row above; the
tailnet form differs only in the mount prefix on internal links, which is why
it is 5,850 bytes larger.

### 3. The heading expression and what it produces

At `a9f671e`, `apps/three-surface-poc/src/polaris-markdown.ts` lines 156–160
read, in full:

```
    if (heading) {
      const level = Math.min(6, heading[1]!.length + 3);
      output.push(`<h${level}>${inline(heading[2]!)}</h${level}>`);
      i++;
      continue;
```

Adjacent-pair skips on the post-trim capture, over all 80 headings in
document order: **3** — one h2→h4, one **h3→h6**, one h4→h6. The h3→h6 skip
is `<h3 id="polaris-account-v1-scope">` "V1 scope" (byte 88,024) followed by
`<h6>` "Core Infrastructure" (byte 88,501). The h4→h6 skip is a bare `<h4>`
"From an insight to a digest" followed by `<h6>` "The Butler-as-Daemon
Model". Of the 14 h6s, **1** follows an h3, **1** follows an h4 and **12**
follow another h6.

**Per-fragment minimum hash depth.** Derivable for exactly one fragment from
the retained machine capture (`api-poc.json`, 5,520,314 bytes): of every
string value in the model, **6** contain a markdown heading line, and all six
are the same v1-scope statement reached by different paths
(`projectShape.projectAccount[4].statement` and its duplicates). Its 9
heading lines are all at hash depth **3**, so its rendered minimum is h6,
placed directly under the h3 that anchors it. For the other rendered
fragments — the four diagram captions and the selected-passages block — the
source markdown is not exposed in either capture, so their minimum hash depth
is **[Unknown]** from the capture. A test would need the `body` string each
`renderPolarisMarkdown` call receives: the chapter bodies from
`projectReading` and the passage text from
`apps/three-surface-poc/src/polaris-reading-plan.ts`. One of the two is
already known at source rather than from the capture: `polaris-reading.ts`
line 112 ends `: \`${heading === true ? '### ' : ''}${passage}\`;`, so every
passage it marks as a heading is synthesized at depth 3 and renders at h6
regardless of the Butlers source.

### 4. The outline

At `a9f671e`, `apps/three-surface-poc/src/polaris.ts` line 1529 is the
function head:

```
function depthNav(shape: ProjectShape, dives: readonly CapabilityDeepDive[]): string {
```

and line 1629 is the call site:

```
    sidebar: depthNav(shape, dives) + SECTION_NAV_SCRIPT,
```

The dossier cited lines 1510–1538; the function at `a9f671e` runs 1529–1556.

**What it lists.** Four depth levels, named by the copy ids `depth.summary`,
`depth.catalog`, `depth.detail` and `depth.source`. On the post-trim capture
the rendered `<nav class="depth-nav">` is 8,746 bytes (direct form; 8,761
tailnet) and carries **35** anchors: **2** in a `<p class="quick-links">`
*outside* the collapsible (Capabilities → `#polaris-group-v1`, Key roles →
`#polaris-account-purpose`) and **33** inside `<details class="contents-list">`.
The 33 break down as **7** h2 group links, **4** curated diagram anchors,
**5** catalog-class anchors, **10** component-guide chapter anchors, **1**
capability deep dive, **5** evidence-section anchors and **1** exact-source
route link. Of the **39** h3 ids on the page, **11** are among those targets
and **28** are not; all **7** h2 ids are.

**Tab stops before `<h2 id="polaris-group-catalog">`.** Two predicates, both
published.

| Predicate | Pre-trim | Post-trim |
|---|---:|---:|
| Dossier's: every `<a href>` + every `<details><summary>` + every `tabindex="0"`, document order, before the cut | 172 + 53 + 3 = **228** | 172 + 52 + 2 = **226** |
| Focusable in the served markup: the same three classes, excluding anything nested inside a `<details>` with no `open` attribute (a `<summary>` is itself focusable and is counted) | 9 + 53 + 0 = **62** | 9 + 52 + 0 = **61** |

The cut is at byte 912,381 (line 1,039) pre-trim and byte 281,945 (line
1,031) post-trim. The dossier's 228 is reproduced exactly, addend by addend.
The second row is the number a keyboard reader actually walks with scripting
off, and it is smaller because 163 of the 172 preceding anchors are inside
closed disclosures — which is its own finding: those links are unreachable
until something opens their container.

**The architecture group's repeated citations.** Between the architecture h2
and the catalog h2 there are **89** anchors with **2** distinct hrefs; one
href, `#polaris-source-about-lay-and-land-components-md`, accounts for **88**
of them. Identical on both captures. The dossier said "~150"; the shape it
describes is real and the concentration is higher than reported.

### 5. Catalog populations and what lane A did to them

Per-class, measured by bounding each `id="polaris-class-<cls>"` at the next
class id or the next `<h2>`, whichever comes first:

| Class | Pre-trim form | Pre-trim items | Post-trim form | Post-trim items |
|---|---|---:|---|---:|
| `principle` | table, `<tbody>` | 7 | table, `<tbody>` | 7 |
| `success-criterion` | table, `<tbody>` | 13 | table, `<tbody>` | 13 |
| `catalog-entry` | table, `<tbody>` | 65 | table, `<tbody>` | 65 |
| `topology-component` | table, `<tbody>` | 87 | **compact list, no `<tbody>`** | 87 |
| `roster-identity` | table, `<tbody>` | 6 | **compact list** | 6 |
| `design-contract` | table, `<tbody>` | 32 | **compact list** | 32 |
| `baseline-spec` | table, `<tbody>` | 185 | **compact list** | **192** |
| `craft-policy` | table, `<tbody>` | 7 | **compact list** | 7 |
| total `data-polaris-item` on the page | | 402 | | **409** |

So the dossier's S4-M6 target — "baseline-spec 185, topology-component 87" as
*table rows* — no longer exists in that form. Lane A converted the five
statement-less classes to `<ul class="item-list">`, and baseline-spec grew
from 185 to 192 between the two Butlers revisions. **Three** class tables
remain, and the page's 5 tables are: principle (8 `<tr>`), success-criterion
(14), catalog-entry (66), the sources table at `#polaris-shape-sources`
(279, i.e. 1 header + 278) and the root-index table at `#polaris-shape-root-index`
(8). `<tbody>` still marks each of the three surviving class tables.

### 6. The one script, and what breaks without it

`SECTION_NAV_SCRIPT` is `apps/three-surface-poc/src/polaris.ts` lines
1232–1289. It does five things: it sets the outline drawer's `open` from a
`min-width: 1000px` media query and closes it on link click when narrow; it
opens a component guide's `<details>` when the location hash names that
guide, on click, on `hashchange` and at `DOMContentLoaded`; it wires the
"Read the complete declaration" button (`class="expand-declaration"`, **1**
instance on the page) to expand or collapse all ten guides; it keeps that
button's `aria-expanded` in sync on `toggle`; and it sets `aria-current="location"`
on the drawer link whose hash matches the topmost group heading, on scroll.

Without it, **[Observed] from the served markup**: every fact, link and
disclosure is still present and operable — the drawer opens by its own
`<summary>`, each guide opens by its own `<summary>` — and exactly two
affordances stop working: the drawer no longer opens itself on a wide screen,
and the expand-all button becomes an inert control. The page is therefore
already at POC-REQ-022's bar and already one inert button past it; no region
renders empty. That is the posture S4-M6 asks this packet to confirm, and it
is confirmed: **Polaris requires no script to be read, and carries one
control that does nothing without one.**

### 7. Bytes

Measured on the post-trim direct-form capture, 1,478,637 bytes; ceiling
2,097,152; headroom recorded by the lane A measurement record as **612,665**
bytes on the tailnet form, with the owner's restated Q3 target of 1,400,000
bytes still **84,487** bytes away on that form.

| Slice | Mechanism | Marginal bytes (direct form) |
|---|---|---:|
| 1 Labels | append " — " + the source path (mean 43.8 B over 278) to each source-record summary | **+13,010** |
| 1 Labels | append " — " + the identity's path part (mean 43.3 B over 386) to each 'Exact text' link | **+17,874** |
| 2 Headings | level change only, no new element | **0** |
| 3 Source record as columns | remove 278 × (`<details class="source-record"><summary …>Source record</summary>` at mean 182 B, plus `</details>` at 10 B) = 53,376 B; add three `<td></td>` pairs per row (9 B each) and three header cells | **−45,800** [Inferred: the added-cell figure is arithmetic, not a render] |
| 4 Jump list | add the 28 unlisted h3 ids as drawer links, at the current mean of 196 B per fragment link | **+5,479** |
| 5 Filter or paging | [Unknown] until Q1 picks an arm: arm (a) duplicates a bounded head of each list, arm (b) adds a script and a count, arm (c) adds no bytes to any one response and multiplies responses | **[Unknown]** |
| **Net, slices 1–4** | | **−9,437** |

Fragment-only links cost the same on both host forms, so slice 4's figure is
identical on the tailnet capture; slice 1's is too, since neither payload is
a URL. Slices 1–4 together leave the page smaller than they found it, and
none of them moves it toward the ceiling. [Observed for every measured
addend; Inferred for the net, which is a sum of four estimates and not a
render.]

## Gate 2 — Doctrine

**VIS-3 — Human interpretability is a core tenet.** Quoted at the clause,
`.syzygy/governance/doctrine/vision.md` lines 108–121: "Every normative
artifact — spec, doctrine, contract — must remain digestible by a human
unfamiliar with the project. The test: fresh-reader review, run at adoption
and on material amendment, by a reader (human or agent) with no access to the
authoring context, who must be able to restate the artifact's intent and
constraints correctly". The rendered Polaris page is not a normative artifact,
so VIS-3 does not bind it directly; the doctrine that reaches this page is
**VIS-1's second rank**, and this packet says so rather than inheriting the
dossier's tag [Inferred — a reading of VIS-3's scope, stated not resolved.
The dossier's M13 entry cites VIS-3 for all four S2 moves without this
qualification, and the strongest defence of that tag is that the page's whole
purpose is to make governed artifacts digestible, so a page that defeats
digestion defeats what VIS-3 exists for].

**VIS-1 — Comprehensible truth first; never comprehensible fiction.** Lines
82–95, quoted at the load-bearing sentence: "Comprehension is achieved by
simplifying *presentation*, never *content*: an honest view may aggregate,
defer, or progressively disclose Unknowns, but may never substitute a
confident state for an Unknown one." Every slice here is a
presentation-simplification and **no slice removes, aggregates away or
re-states a fact**: the label slices add subject text beside an unchanged
href; the heading slice changes an integer in a tag name; the columns slice
moves four fields out of a wrapper; the outline slice adds links to ids that
already exist; and the filter slice — on every arm — keeps the complete
population served. VIS-1's own worked example is the licence for slice 5:
"collapsing forty Unknown-status modules into one region labeled 'Unknown
×40'" is honest simplification, and a hidden count is exactly that shape.

**VIS-1's ordering is what ranks the slices.** Rank 1 is truth and
observation determinism; rank 2 is comprehension of the truth's presentation.
None of these five slices touches rank 1 — that is why none of them is
urgent, and why slice 3, which is the largest, is not the first. Slices 1 and
2 buy the most comprehension per byte and per line changed.

**VIS-2 — No evidence means Unknown, not success.** Lines 96–106. Engaged in
one place only: if slice 5 hides rows, the count of what is hidden is not a
convenience but the difference between a filtered list and a list that lies
about its denominator. RFC9-13 says the same thing at the contract level (see
below), and PWB-REQ-003's prohibition — "The POC SHALL NOT shrink the
source-path denominator" — says it for the source population specifically.

**VIS-5 — Syzygy never writes code; direct writes are confined to two
namespaces.** Lines 141–160. Every file in Gate 3's table is under `apps/**`;
nothing is written into `openspec/**` or `.syzygy/**`, and the work is a
worker action against scheduled work.

**VIS-7 — The observatory itself must be trustworthy.** Lines 183–193,
quoted at the limb this packet must not break: "every rendered internal
project-entity link resolves to its identified target (the normative link
rule, exactly as stated in trust-and-evidence.md floor bullet 2)". Slice 4
adds 28 new fragment links; every target is an id the same render already
emits, and the existing guard (Gate 6 item 3) fails on a dangling one. Slice
1 changes link *text* and never a link *href* — which is also what keeps
PWB-REQ-020's parity intact, because `sourceRouteIdentities`
(`apps/three-surface-poc/src/polaris-source.ts` lines 49–58) reads the exact-
source identity back off the href and nothing else carries it.

**RFC9-13 — personal presentation state.** Quoted verbatim at its defined
identifier, `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`
line 442 per `DIRECTIVE-REGISTER.md`:

> **RFC9-13.** Personal presentation state — camera, filters, bookmarks,
> saved lens/analytical-plane selections — lives in `.syzygy/local/` and never
> affects truth-bearing encodings (VIS-6, exception (a); RFC3-21). A filter
> that hides entities shows a persistent count of what it hid.

Both sentences bind slice 5, and the second is an invariant its checker must
hold. The first is what makes Q4 a question rather than a detail: the bound
PWB coverage matrix records that PWB has no such state.

**RFC7-34 — Non-visual recoverability.** Quoted at its defined identifier,
`.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md` line
241: "Every such distinction is recoverable **without colour, position, or
layout** — by label, text, or structure". A control whose only distinction
from 277 others is its position in the document is not recoverable by label,
text or structure. That is the contract sentence slice 1 exists to satisfy,
and it is why slice 1 is argued from RFC7-34 and PWB-REQ-016 rather than from
a preference.

**No SEC rule is engaged.** No slice reads a repository body, sends anything
anywhere, stores anything, or changes what is classified. The one new string
each label slice renders is a path or identity the page already renders
elsewhere in the same row.

## Gate 3 — Topology

| Slice | Lives in | Governed artifact touched |
|---|---|---|
| 1 Labels name their subject | `apps/three-surface-poc/src/polaris-copy.ts` (lines 129 and 134); `apps/three-surface-poc/src/polaris.ts` (lines 377–379, 835, 1549); `apps/three-surface-poc/src/polaris-copy.test.ts`; `apps/three-surface-poc/src/polaris-accessibility.ts` | none |
| 2 Heading normalization | `apps/three-surface-poc/src/polaris-markdown.ts` (lines 156–160); `apps/three-surface-poc/src/polaris-reading.ts` (line 112); `apps/three-surface-poc/src/polaris-markdown.test.ts` | none |
| 3 Source record as columns | `apps/three-surface-poc/src/polaris.ts` (lines 823–837, `sourceRow`, and line 1014's header cell list); `apps/three-surface-poc/src/polaris-first-reading.test.ts`; `apps/three-surface-poc/src/polaris-parity-sweep.test.ts` | none |
| 4 The outline indexes the page | `apps/three-surface-poc/src/polaris.ts` (lines 1529–1556, `depthNav`; line 1319's list styles); `apps/three-surface-poc/src/polaris-accessibility.browser.test.ts`; `apps/three-surface-poc/src/polaris-reachability.test.ts` | none |
| 5 Large populations | `apps/three-surface-poc/src/polaris.ts` (lines 605–606, the class item population); `apps/three-surface-poc/src/polaris-copy.ts` (a new control label and a hidden-count sentence); `apps/three-surface-poc/src/polaris-parity-sweep.test.ts` | none edited — but the bound `RFC9-13.c1` row's standing judgment is at stake, which is Q4 |

Boundaries crossed: none. Every file above is in the implementation plane,
which is what point 3 of the 2026-09-02 authorization reserves the work to:
"Code in the ordinary implementation plane only — `apps/**`, `packages/**`,
tooling, root manifests — never inside `openspec/**` or `.syzygy/**`".

Not touched by any slice: the observation pipeline, the extraction grammar,
the body-read authority gate, the machine answer's shape, the exact-source
route's resolution (`apps/three-surface-poc/src/verbatim-route.ts`), and every
href on the page.

### The authorizing act, per slice

The act in force is `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`
(2026-09-02) as continued by `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`
(2026-09-05). Its authorization sentence, quoted verbatim from the 2026-09-02
record's point 1 (lines 50–52): "**Implementation planning and
implementation** of the signed `polaris-project-wide-butlers-model` change —
tasks §2 through §5 of its `tasks.md` — as one bounded improvement cycle of
the Three-Surface POC." The continuation's point 3 (lines 110–114) restates
the bound: "**Scope is otherwise unchanged from 2026-09-02.** The same one
configured Butlers repository, the same content class `declared-project-shape-text`,
the same ordinary implementation plane". Its limiting sentences are the
"What this does not authorize" list at lines 125–146 and the escalation
triggers at lines 150–156, quoted in full in Q5.

**Neither act names a rendering.** There is no overlay for PWB, so there is
no predecessor-versus-overlay reading to do per slice: the 2026-09-05
amendment replaced the bytes in place and the clauses every slice below rests
on are the current, amended text. The per-slice question is therefore only
whether a trigger is crossed.

| Slice | Owner act needed | The trigger tested, and the sentence it is tested against |
|---|---|---|
| 1 Labels | **No** on any reading | Tested against "a further amendment to the signed PWB specification beyond the 2026-09-05 package". PWB-REQ-012 constrains a heading's word count and a notice's vocabulary; it does not fix a label's text, and the copy table is implementation. Q3 is the owner's opportunity to read "closed set" more strictly than this packet does |
| 2 Headings | **No** on any reading | Same sentence. The only spec sentence naming heading levels is the PWB specification's line 57, inside the extraction grammar; it governs the Butlers source, not the rendered document. Quoted in "Decided in this packet" above |
| 3 Source record as columns | **Should be ruled — Q5** | Tested against "any scope beyond the signed change". PWB-REQ-011's invariant names four reading levels — summary, catalog, detail, exact source — and the source-record disclosure is not one of the four; on that reading the hoist is inside scope. On the wider reading, removing any stopping point the reader had is a change to the depth structure the requirement quantifies over |
| 4 The outline | **No** on any reading | Same sentence. The outline is not named in either specification: a sweep for "outline" returns 0 lines over both spec trees and over doctrine. It is an implementation of PWB-REQ-016's "focus order reaches every target" and POC-REQ-061's "in an order that follows the surface's reading structure" |
| 5 Large populations | **Should be ruled — Q1, Q4, Q5** | Tested against **three** sentences: "any scope beyond the signed change" (a rendering mode neither specification describes); "a change to doctrine or an accepted contract" (the bound `RFC9-13.c1` row's "No camera/filter/bookmark state" stops being true if the filter remembers anything); and, on arm (c), the route-shape change PWB-REQ-011's depth sweep enumerates |

This packet tests each slice against those sentences and **rules none of
them**. Q1, Q4 and Q5 put the readings to the owner.

All five slices run under `syzygy-dov.13`, the pursuit bead; no new bead is
filed by this packet.

## Gate 4 — Design sketch, per slice

### Slice 1 — Every label names its subject (small; no act; Q3 rules the classification)

**The change.** `label.source-record` and `label.exact-text` stay in the copy
table as their current literals and gain a documented suffix form: the
renderer appends a separator and one subject string that is already present
in the same row. For the source-record summary at `polaris.ts` line 835 the
subject is `source.path` — the value line 836 already renders in the row's
first cell — so the summary reads "Source record — about/lay-and-land/components.md".
For `exactTextLink` at line 378 the subject is the identity's path component,
which is what a reader is choosing between; the full identity is 159 bytes on
average and unreadable, the path component is 43.

**Why the suffix form and not a prefix.** The existing hand-typed copy oracle
(`apps/three-surface-poc/src/polaris-copy.test.ts` line 308) decides that a
copy row is "reached" by `entry.text === row.text || entry.text.startsWith(row.text) || entry.text.includes(row.text)`.
A suffix is reached by `startsWith`, so the oracle keeps working without
being relaxed. That is deliberate and it is also the AGENTS.md copy-oracle
guardrail read in the other direction: the guardrail warns that a very short
label is "reached" by coincidence and proves nothing. Interpolation makes the
labels *longer* and more distinctive, so it does not create a coincidence;
what it does create is a row whose rendered text is no longer a fixed string,
and that is exactly Q3.

**The three things this slice must not do.** (a) It must not touch the href.
`sourceRouteIdentities` (`polaris-source.ts` lines 49–58) reads the exact-
source identity back off the `href` attribute and the comment at lines 44–47
says in terms that the href is "the one carrier of the identity; no attribute
restates it"; PWB-REQ-020 parity is per rendered tuple, not per id, and the
catalog group and the evidence group each render the same 192 identities, so
a change that made the two renderings differ would be invisible to an
id-level check. (b) It must not push a prohibited word into a heading or
lede. `polaris-copy.test.ts` line 132 applies the prohibited-term regex only
where `frame.kind` is defined, and a summary or anchor has no kind, so a
Butlers path containing "document" or "section" would pass today — the
implementing bead should assert the interpolated text against the same regex
anyway, because relying on a frame classification is relying on an accident.
(c) It must not interpolate anything not already on the page: the subject is
copied from a value the same row renders, never fetched.

**Oracle.** An independent uniqueness sweep over the served page, hand-typed
in the test and importing nothing from the renderer: extract every `<summary>`
text and every `<a>` text with its `href`; assert that no two controls share
an accessible name unless they share an href; report both denominators (359
summaries, 1,089 anchors on the current capture). The fixture must be the
project-shape fixture that renders more than one source, so the invariant has
a population to be true over.

**Rule-6 mutants.** (a) Revert `polaris.ts` line 835 to the bare
`copy('label.source-record')` and confirm the uniqueness sweep fails naming
the duplicate count, not merely "a duplicate". (b) Interpolate a *constant*
instead of `source.path` and confirm the sweep still fails — this is the
mutant that proves the check tests distinctiveness and not merely length.
(c) Change the interpolated value from the path to the claim id and confirm
the sweep **passes**, recording honestly that the check constrains
distinctiveness and not which subject is chosen. (d) Change the href while
leaving the text alone and confirm the PWB-REQ-020 parity sweep fails.

### Slice 2 — A heading one level below the heading above it (small; no act; ordinary engineering)

**The change.** `polaris-markdown.ts` line 157 stops adding a fixed 3 and
starts mapping relative to the fragment's own shallowest heading and to the
level of the element that anchors it. Concretely: `renderPolarisMarkdown`
gains an anchoring level (the level of the heading the fragment is rendered
under — h3 in every current call site), scans the fragment's heading lines
once for their minimum hash depth `m`, and maps a source heading of depth `d`
to `min(6, anchor + 1 + (d - m))`. A fragment whose shallowest heading is
`###` then starts at h4 instead of h6, and a fragment mixing `###` and `####`
keeps its internal relief. Separately, `polaris-reading.ts` line 112 stops
synthesizing `### ` and synthesizes `# `, so Syzygy's own generated heading
is the shallowest thing in its fragment and the mapping does the rest.

**Why this is ordinary engineering and not an owner question.** No sentence
in either specification or in doctrine fixes a rendered heading level (the
sweep and its denominators are in "Decided in this packet" above). The one
requirement in the neighbourhood, PWB-REQ-012, governs a heading's word count
and its vocabulary, both unchanged. The change is invisible to every parity
marker: heading elements carry no `data-parity-field`, no `data-claim-id` and
no id.

**Oracle.** A hand-typed sequence check over the rendered page: extract every
heading in document order with its level, and assert that no heading's level
exceeds its predecessor's by more than one. Expected values are literals in
the test, never imported from `polaris-markdown.ts`. Report the denominator
(80 headings on the current capture) and the level histogram, so a run that
silently stops rendering headings fails on the denominator rather than
passing on an empty population.

**Rule-6 mutants.** (a) Restore `Math.min(6, heading[1]!.length + 3)` and
confirm the sequence check fails naming the h3→h6 pair. (b) Change the
mapping to `anchor + (d - m)` (one level too shallow, so a fragment heading
collides with its anchor) and confirm a second assertion — that no fragment
heading is at or above its anchor's level — fails. (c) Restore `'### '` at
`polaris-reading.ts` line 112 and confirm the check fails on the
selected-passages block specifically, which is the mutant that proves the two
halves of the slice are independently guarded. (d) Feed a fragment whose
headings are `#`, `##` and `####` and assert the rendered levels are h4, h5
and h6 — the relief-preservation case, which the fixed offset also gets right
and the naive "always start at h4" rewrite would not.

### Slice 3 — The source record is columns, not a disclosure (large; Q2 and Q5)

**The change.** `sourceRow` (`polaris.ts` lines 823–837) stops building the
`<details class="source-record">` at line 835 and puts its four fields into
three new cells of the row it already returns: identity (the existing
`<cite data-parity-field="shape-source-identity">`), rule and pillar, and
outcome, anchor and digest. The header cell list at line 1014 gains the three
matching `<th scope="col">` entries from the copy table. Nothing else moves:
the row keeps its id, its `data-polaris-source`, its claim-block attributes,
its path cell, its exact-text link, its denominator cell and its claim tuple.

**Two guardrails this slice must hold, both from AGENTS.md.** First, the
literal `<tbody>`: `apps/three-surface-poc/src/polaris-parity-sweep.test.ts`
line 494 finds class tables by `section.inner.includes('<tbody>')` and
`apps/three-surface-poc/src/polaris-reachability.test.ts` line 368 asserts
`region.inner.startsWith('<table>')`. Both are bare-literal predicates that
silently match nothing if an attribute is hoisted onto the tag, dropping a
family to a human count of 0 rather than failing. If this slice needs a role
or a data attribute on the sources table, it goes on the region div:
`tableRegion` (`polaris.ts` lines 158–160) already takes an `attrs` parameter
and line 1014 already passes ` data-source-index` through it. Second, the
fragment-target rule:
`apps/three-surface-poc/src/polaris-first-reading.test.ts` lines 242–246
assert that no id inside any `<details>` is the target of any
`href="#…"`, and lines 233–235 assert specifically that
`id="polaris-shape-sources"` is inside no disclosure. This slice moves in the
safe direction — it takes content *out* of a disclosure — but the assertions
must keep passing with the new cells, and the `it(...)` that carries them is
named "keeps each item population and the exclusions complete behind a native
disclosure whose control names the count, leaves the sources table open for
fragment navigation, and hides nothing by style".

**Oracle.** The existing PWB-REQ-020 parity sweep is the oracle and it does
not need changing: it compares the page's marker multisets against the
machine answer, and this slice changes neither channel's markers. The added
check is a per-row completeness assertion — for every source in the model,
the rendered row exposes identity, rule, outcome and digest as text, with the
denominators of both populations reported.

**Rule-6 mutants.** (a) Drop the digest cell for sources whose support has no
`contentDigest` and confirm the completeness assertion fails rather than
silently rendering an empty cell (the case the current disclosure handles
with `sentence.no-body-read`). (b) Hoist `role="region"` onto the `<table>`
tag and confirm the reachability test at line 368 fails — if it does not, the
predicate is the defect and must be repaired before the slice lands. (c) Put
one of the new cells inside a `<details>` and confirm the fragment-target
assertion fails. (d) Swap two rows' identity cells and confirm the parity
sweep fails on the multiset, not merely on a count.

### Slice 4 — The outline indexes the page it is the index for (medium; no act)

**The change.** `depthNav` (`polaris.ts` lines 1529–1556) keeps its four
depth levels and its collapsible, and gains two things. First, every h2 and
every h3 the render emits appears in it: the function already receives the
shape and the dives, and the 28 missing ids are all ids the same render
computes (account sections, class sections, capability bands, evidence
sub-sections). Second, the `<p class="quick-links">` that already sits
*outside* the collapsible — today two links — becomes the always-reachable
skip list: the 7 group headings, in document order, as the first links in the
page's tab order. The collapsible keeps the full 60-odd-entry outline.

**Why not the command palette the dossier's S2-M4 proposes.** A palette
"opened by a dedicated keystroke" is a control that does not exist without
script, and the page's posture is that nothing a reader needs requires
script (Measurement 6). Building the palette makes Q1's arm (b) a
prerequisite for navigation rather than for convenience, which is a much
larger ask than filtering a catalog. The always-reachable skip list gets the
same first-Tab reachability with zero script, and a palette can be added on
top later as pure enhancement. **This is a design decision taken in this
packet, not an owner question** — it costs the reader nothing and it removes
a dependency; if the owner wants the palette, Q1's arm (b) is where to say
so.

**Why the collapsible stays.** Removing it would put 60 links in the linear
tab order ahead of the article on every page load, which trades one wall for
another, and `SECTION_NAV_SCRIPT` already opens it on wide screens. The
fragment-target guardrail is the reason the *targets* must stay out of
disclosures, not the reason the *index* must.

**Oracle.** Extend the existing gated browser harness
(`apps/three-surface-poc/src/polaris-accessibility.browser.test.ts`) with an
expected-target list built from the rendered headings rather than from
`depthNav`: extract every `<h2 id>` and `<h3 id>` from the served page,
assert each is a drawer target, and assert each resolves — the denominator is
the heading population, so a render that stops emitting a section fails. A
second, non-browser assertion in `polaris-reachability.test.ts`: the first
seven focusable anchors in document order are the seven group headings.

**Rule-6 mutants.** (a) Remove one h3 from the drawer and confirm the
coverage assertion fails naming that id. (b) Point one drawer link at an id
the render does not emit and confirm the resolution assertion fails (the
VIS-7 dangling-link case). (c) Move the quick-links paragraph inside the
`<details>` and confirm the first-seven-focusable assertion fails. (d) Emit
the drawer with `open` and confirm the tab-stop assertion changes as
predicted — the mutant that proves the count is measured and not assumed.

### Slice 5 — A population you can get through (large; Q1, Q4 and Q5)

**The change, in whichever arm Q1 picks.** The five compact lists
(`polaris.ts` line 605) and the three class tables (line 606) gain a bounded
first view. Arm (a), no script: each population renders its first 20 entries
plus a nested disclosure holding the remainder, whose summary names the
remaining count — pure markup, the complete population always in the
document. Arm (b), progressive enhancement: the complete population renders
as today, and a script adds a path-prefix input that sets `hidden` on
non-matching entries and renders a live count of what is hidden beside the
control; with script off the control is absent and nothing is hidden. Arm
(c), server-side paging: a query parameter on the Polaris route selects a
window, and the page states the window and the total.

**What is invariant across all three arms.** The complete population is
always recoverable — arm (a) behind one summary, arm (b) by not running the
script or by clearing the input, arm (c) by the "all" window. Whatever is
not visible carries a count, which is RFC9-13's second sentence and VIS-1's
"Unknown ×40" shape. No entry is removed from the served bytes in arms (a)
and (b), so the PWB-REQ-020 parity multiset is unchanged; arm (c) changes it,
which is why arm (c) is the arm that needs the depth-sweep re-run.

**Where the bytes go.** Arm (a) adds a disclosure per class and duplicates
nothing, so it is nearly free in bytes and costs one more interaction. Arm
(b) adds a control, a count element and script. Arm (c) removes bytes from
any one response and multiplies responses. The packet does not estimate arm
(c) because the response population is [Unknown] until the window size is
chosen.

**Oracle.** A served-page assertion that for every class the number of
rendered `data-polaris-item` entries equals the machine answer's count for
that class — the assertion the parity sweep already makes, which arms (a) and
(b) must not weaken — plus a hidden-count assertion: whatever the page
declares hidden equals the rendered population minus the visible population,
computed independently of the renderer. For arm (b) the browser harness
asserts that with script disabled the visible population is the complete one.

**Rule-6 mutants.** (a) Truncate the served population instead of hiding it
and confirm the parity sweep fails with both denominators reported. (b) Make
the hidden count a constant and confirm the hidden-count assertion fails. (c)
Remove the count element entirely and confirm the assertion fails on its
absence rather than passing on a missing element — the RFC9-13 case. (d) For
arm (b), make the script set `display: none` through a style attribute and
confirm the existing "hides nothing by style" assertion
(`apps/three-surface-poc/src/polaris-first-reading.test.ts` line 248)
still governs the served markup.

### Design bar for the human surface

Four things the implementing beads should hold that are not tested by any
oracle above and are stated here so they are not lost: the interpolated
subject must be the *shortest* string that distinguishes (a path, not an
identity); the skip list must not grow a visual weight that competes with the
first heading; a hidden count must read as a fact, not as an apology; and a
new column must not push the sources table's horizontal scroll past what the
`tabindex="0"` region can show at 400px, because that region is a keyboard
stop precisely so a wide table stays operable.

## Gate 5 — Specification

Two adopted specifications are in force for this surface and neither has an
overlay change directory: `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`
(**24** requirements, **24** scenarios, 1,008 lines) and
`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`
(**17** requirements, **31** scenarios, 1,152 lines), the latter as amended in
place on 2026-09-05. Every requirement and scenario cited below was read at
source this session, in the current bytes.

### The keyword sweep and its denominators

Case-insensitive, run with Python `re` over every file in each tree (per
verification rule 1, not with `grep` classes). Denominators: **7** files in
the POC-experience change, **15** in the PWB change, **6** in
`.syzygy/governance/doctrine`.

| Term | POC-experience (7 files) | PWB (15 files) | Doctrine (6 files) |
|---|---:|---:|---:|
| outline | 0 | 0 | 0 |
| heading | 0 | 31 | 0 |
| keyboard | 7 | 29 | 1 |
| accessible | 2 | 0 | 1 |
| landmark | 0 | 0 | 0 |
| "skip link" | 0 | 0 | 0 |
| disclosure | 9 | 42 | 0 |
| details | **0** | **0** | 0 |
| navigation | 3 | 6 | 2 |
| paginat | 2 | 0 | 0 |
| filter | 4 | 12 | 1 |
| label | 16 | 80 | 7 |
| "source record" | 0 | 2 | 0 |
| "exact text" | 0 | 4 | 0 |

Three of these matter and are read here rather than counted. **"details" is
0 everywhere**, so no requirement or scenario names the disclosure element
and Q2's form question has no spec sentence against it. **"outline" is 0
everywhere**, so slice 4 implements a requirement about focus order, not a
requirement about an outline. **The 2 "source record" hits and all 12 PWB
"filter" hits are in the contract-coverage files, not in the specification
proper**: the "source record" hits are the `RFC4-5` row's "Walkthrough/source
records are retained", and the "filter" hits are RFC6-15, RFC6-16, RFC6-22,
RFC6-23 and the `RFC9-13.c1` row quoted in Q4.

### The RFC2-26 test, run over all five slice rows

RFC-0002 is an accepted design contract in force. Its phase rule is quoted
verbatim at the defined clause,
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md` line
196 per `DIRECTIVE-REGISTER.md`, under the `###` heading "Authority boundary
at the OpenSpec seam (binding phase rule)" at line 194 — **both paragraphs,
no elision**:

> **RFC2-26.** This contract schedules nothing: **it is not a specification of
> record from which implementation work may be scheduled**. No implementation
> work for user-observable consequences of this contract — evaluation and
> snapshot displays, claim and challenge rendering, Unknown-reason and
> rendering-tier presentation, reconciliation-chain and gap surfaces, API
> answers over epistemic state — may be scheduled solely from this RFC. Before
> implementation, every observable consequence either maps to an approved
> OpenSpec requirement and scenario in the governance root's `openspec/**`
> plane, or carries a reviewed N/A judgment proving it purely structural with
> no independently testable behavior. **The reviewed N/A judgment's home and
> gate.** A reviewed N/A judgment is a recorded owner judgment homed in
> `decisions/` (RFC3-15), and the judgment is honored only through an effective
> owner act under RFC3-16(a), in state (1) or state (2), with that state rendered;
> absent or invalid acts map nothing and leave the consequence unmapped and
> Unknown, never covered (RFC3-16(a)'s effect rule; VIS-2).
>
> **Rows are per observable consequence, not per clause.** A clause with five
> observable consequences and one mapped requirement is not covered; the matrix
> discloses the consequences it enumerates for each clause, so a
> complete-looking matrix over under-enumerated consequences is a defect of the
> matrix. At surface specification a
> clause-to-requirement coverage matrix over RFC2-1..RFC2-26 is produced —
> **that matrix is review material, never authority**. This clause creates no
> OpenSpec content now (none may exist during bootstrap). This clause binds the
> whole RFC 0002 package, not this module alone. (Shape-parallel with RFC6-28,
> RFC7-38, RFC8-32, RFC9-52, RFC10-16, RFC11-12.)

**The denominator is five**: the five slice rows of Gate 3's act table
[Observed, counted this session over that table]. The test is run over all
five.

| Slice | RFC2-26 consequence class | Approved requirement **and** scenario | Limb 1 |
|---|---|---|---|
| 1 Labels | **None enumerated.** A control's accessible name is not an evaluation display, a claim or challenge rendering, an Unknown-reason or rendering-tier presentation, a reconciliation surface, or an API answer over epistemic state. The clause's list does not reach it | **PWB-REQ-016**, line 864, scenario **"Keyboard-only owner reaches exact intent"** at lines 885–889, quoted verbatim: "**WHEN** the owner performs the material-change walkthrough without a pointing device / **THEN** every prompt and exact-source path remains operable and understandable / **AND** the retained run record identifies keyboard-only mode". The requirement text is the closer match: "Every project distinction and summary-to-source path SHALL be recoverable by text and operable by keyboard without relying on color, position or layout" (lines 868–870). Also **PWB-REQ-012**, line 679, scenario **"Section headings name project concepts"** at lines 705–710 | **Available**, on two requirement-and-scenario pairs. Q3 exists because PWB-REQ-012 declares a *closed* role set over owner-visible strings and this slice makes two of them variable — a reading, not a measurement |
| 2 Headings | **None enumerated.** A heading's level number is structural; it renders no state and answers no query | **POC-REQ-061**, line 966, scenario **"Keyboard-only reading"** at lines 993–997, quoted verbatim: "**WHEN** a keyboard-only reader traverses each surface / **THEN** every interactive element is reachable with visible focus, in an order that follows the surface's reading structure". **The fit is partial and this packet says so**: the scenario is about focus order, and a heading is not an interactive element. **PWB-REQ-016**'s requirement text — "recoverable by text… without relying on color, position or layout" — is the closer sentence, and a heading level *is* structure rather than layout | **Requirement available, scenario partial.** This packet does not call slice 2 lawful or unlawful on that. It records that the consequence class is not one RFC2-26 enumerates, so limb 1 is not the operative test; the operative test is Gate 3's trigger table, and slice 2 crosses no trigger |
| 3 Source record as columns | **"claim and challenge rendering"** — the row carries a claim tuple and a provenance marker, and the fields being hoisted are a claim's support | **PWB-REQ-001**, line 69 (the source identity and revision binding), **PWB-REQ-003**, line 160, scenario **"Excluded source fails closed"** at lines 184–189, quoted verbatim: "**WHEN** an admitted shape source cannot be classified as safe to index / **THEN** its source identity remains counted as Unknown / **AND** its within-source item denominator is Unknown / **AND** only hash-not-body exclusion provenance is exposed", and **PWB-REQ-007**, line 439. All three require the *content* the disclosure holds; **none names its form** [Observed: the PWB specification's **31** scenario headings were enumerated this session; the **5** under PWB-REQ-001, 003, 007 and 011 are at lines 98, 184, 470, 651 and 657, and none names a disclosure element — the literal "details" occurs 0 times in the tree] | **Available on content, silent on form.** The clause's bar is "an approved OpenSpec requirement **and** scenario", and slice 3's observable consequence — the same four fields, one interaction earlier — maps to all three. The residual risk is PWB-REQ-011's depth invariant, which is Q2's counter-argument and Q5's trigger test, not an RFC2-26 gap |
| 4 The outline | **None enumerated.** A navigation index of ids the page already emits renders no state | **PWB-REQ-016**, line 864, same scenario as slice 1, whose **Observable** limb reads "every distinction has text, focus order reaches every target, no pointer-only action exists"; and **POC-REQ-061**, scenario **"Keyboard-only reading"** at lines 993–997, whose THEN names "an order that follows the surface's reading structure" — the closest sentence in either specification to what slice 4 does | **Available**, on two requirement-and-scenario pairs |
| 5 Large populations | **"Unknown-reason and rendering-tier presentation"** on arms (a) and (b) — a hidden count is a rendering tier with an explicit remainder; **"API answers over epistemic state"** on arm (c), because a windowed route changes what an answer's scope declaration must say | **POC-REQ-022**, line 456, scenario **"No-script request"** at lines 478–483, quoted verbatim: "**WHEN** a surface page is fetched and rendered without JavaScript / **THEN** its facts are served in exact server-rendered form, or the region explicitly discloses that the spatial/board rendering is unavailable without script". Also **POC-REQ-021**, line 417, whose prohibition is "The POC SHALL NOT load executable client code from outside its own built, version-controlled outputs" — satisfied by any inline script, which is how `SECTION_NAV_SCRIPT` ships today. And **PWB-REQ-011**, line 632, for arm (c)'s route shape | **Available for arms (a) and (b); partial for arm (c).** No scenario in either specification describes a windowed or paged catalog route, so arm (c)'s observable consequence maps to PWB-REQ-011's requirement text and to no scenario. If the owner takes arm (c) and reads RFC2-26's bar strictly, the repair routes the clause itself names are a scenario added through CC-REV-2, or a reviewed N/A judgment homed in `decisions/` and honored through an effective owner act under RFC3-16(a). This packet's view of the second: probably not reachable, because the clause admits an N/A judgment only for a consequence "purely structural with no independently testable behavior", and a route that changes which items an answer contains is independently testable [Inferred — the clause names the route, Observed; whether arm (c) fits it is a reading] |

**What the test establishes and what it does not.** It establishes
[Observed] that slices 1 and 4 map to named requirement-and-scenario pairs in
both adopted specifications; that slice 3's content maps to three
requirements and one scenario while its *form* is named by neither
specification anywhere; that slice 2's requirement is available and its
nearest scenario is about interactive elements rather than headings; and that
slice 5 maps for two of its three arms. It does **not** establish that any
slice is lawful: that is Q5's, and RFC2-26's own scope sentence — "This
clause binds the whole RFC 0002 package, not this module alone" (lines
219–220) — is a reading the owner may take more or less broadly than this
packet has.

### New WHEN/THEN scenarios, for the beads' acceptance contract, not the spec

These are acceptance criteria for the implementing beads. They are **not**
proposed spec text and nothing here amends a requirement.

**S1 (slice 1).** WHEN the page renders a shape with more than one source,
THEN no two controls share an accessible name unless they share an `href`,
AND the assertion reports both denominators (the summary population and the
anchor population), so a render that emits fewer controls fails rather than
passes on a smaller set.

**S2 (slice 1).** WHEN an 'Exact text' label is interpolated, THEN the link's
`href` is byte-identical to what it was before the interpolation, AND
`sourceRouteIdentities` over the served page returns the same list in the same
order with the same multiplicity.

**S3 (slice 2).** WHEN any markdown fragment is rendered under an anchoring
heading, THEN no rendered heading's level exceeds its predecessor's by more
than one, AND no fragment heading is at or above its anchoring heading's
level.

**S4 (slice 2).** WHEN a fragment's shallowest heading is `###`, THEN its
rendered headings start one level below the anchor, AND a fragment mixing
`###` and `####` keeps two distinct rendered levels.

**S5 (slice 3).** WHEN a source has no body digest, THEN its digest cell
renders the no-body-read sentence rather than empty, AND a rendered empty
cell is a failure, not a pass.

**S6 (slice 3).** WHEN the sources table is rendered, THEN `id="polaris-shape-sources"`
is inside no `<details>` and no id that any `href="#…"` names is inside one,
AND the table region's own tag opens with the bare literal `<table>`.

**S7 (slice 4).** WHEN the page is rendered, THEN every `<h2 id>` and every
`<h3 id>` it emits is a target of the depth navigation, AND every depth-
navigation fragment target resolves to an id the same render emits.

**S8 (slice 4).** WHEN a keyboard reader presses Tab from the top of the
page, THEN the seven group headings are reachable within the first ten stops,
AND that count is measured from the served markup rather than asserted.

**S9 (slice 5).** WHEN a population is bounded by any arm, THEN the number of
entries the page declares hidden equals the served population minus the
visible population, computed without importing the renderer, AND a missing
count element is a failure rather than a zero.

**S10 (slice 5).** WHEN the page is served and no script runs, THEN every
class's rendered `data-polaris-item` count equals the machine answer's count
for that class, AND both denominators are reported.

## Collision and sequencing

**M13's candidate surface is 15 files**, every one of them under
`apps/three-surface-poc/src/` and every one resolving in this worktree: the
five renderer modules the slices edit (`polaris.ts`, `polaris-copy.ts`,
`polaris-markdown.ts`, `polaris-reading.ts`, `polaris-reading-plan.ts`), three
shared modules a slice reads or restyles (`polaris-source.ts`,
`design-tokens.ts`, `page-shell.ts`), and seven tests
(`polaris-first-reading.test.ts`, `polaris-copy.test.ts`,
`polaris-markdown.test.ts`, `polaris-accessibility.ts`,
`polaris-accessibility.browser.test.ts`, `polaris-reachability.test.ts`,
`polaris-project-shape.test.ts`).

**Two predicates, both published, because they disagree on 7 of the 13
rows.** M11's second review found that a single-column full-path predicate
drops continuation-form and bare-basename citations, so both columns are here
from the start.

- **Predicate A (full path):** every backticked code span in the sibling
  packet that contains a `/` and resolves to a *file* in this worktree,
  intersected with the 15-file surface.
- **Predicate B (basename):** the file's basename occurring anywhere in the
  sibling packet's bytes, in a code span or not, inside a path or standing
  alone. B is a superset of A by construction, and B is the predicate that
  catches a packet that names `polaris.ts` in prose without a path.

Every head below was read this session with `git -C <worktree> rev-parse --short HEAD`.

| Sibling | Title | Head | A | B | B-only additions |
|---|---|---|---:|---:|---|
| M1 lane A (on main, in this worktree) | Polaris page size: state page-invariant facts once | `a9f671e` | 0 | **1** | `polaris.ts` |
| lane B, PR #35, P-68 | Polaris page size: state page-invariant facts once (lane B copy) | `4090f98` | 0 | **1** | `polaris.ts` |
| M2, PR #36, P-69 | Evidence currency: compute the horizon, wire `assessCurrency`, make the legend true | `f2f37dd` | 2 | **4** | `polaris-reading-plan.ts`, `polaris.ts` |
| M3, PR #37, P-70 | Honest encoding at the gate: POC-REQ-060 on Polaris and a real sweep | `6574600` | 6 | **7** | `page-shell.ts` |
| M4, PR #38, P-71 | Close the owner loop: a route from every Unknown, home as the day-opening, and run the return path once | `63b8e33` | 4 | **5** | `polaris-reading.ts` |
| M5, PR #39, P-72 | The agent's briefing: a task-scoped route, the dispatch packet and the prohibitions on the machine channel | `ba9ca61` | 2 | **4** | `design-tokens.ts`, `polaris-copy.ts` |
| M6, PR #40, P-73 | The generator's honesty contract | `83c9f60` | **0** | **0** | — |
| M7, PR #42, P-76 | Close the generation loop | `f97baf4` | 1 | 1 | — |
| M8, PR #43, P-74 | Portability: the profile as a loaded, digest-bound registry input | `bce9039` | **10** | **10** | — |
| M9, PR #41, P-75 | One identity, one epistemic shape, one vocabulary across the surfaces | `65de02b` | 4 | 4 | — |
| M10, PR #44, P-77 | The machine consumer gets a contract | `95f31cb` | 1 | 1 | — |
| M11, PR #45, P-78 | Operability: the daemon can say what it is serving | `bbd6837` | 4 | 4 | — |
| M12, PR #46, P-79 | Retained evaluations, a rendered claim-state delta, and the owner's note | `49b70bc` | 3 | **4** | `polaris-first-reading.test.ts` |

**The collision is real and it is concentrated in three files.** Under
predicate B, `apps/three-surface-poc/src/polaris.ts` is named by **11** of the
13 siblings, `apps/three-surface-poc/src/polaris-copy.ts` by **7**,
`apps/three-surface-poc/src/polaris-source.ts` by **5** and
`apps/three-surface-poc/src/design-tokens.ts` by **4**. M13's five slices all
edit `polaris.ts`, two edit `polaris-copy.ts`. The zero-intersection story
some of the sibling packets tell is not available to this one and this packet
does not tell it.

**The three siblings that own the same pixels.**

- **M1 (lane A, already on main at `2ef68f5`; lane B, PR #35, P-68)** owns
  page bytes and owns the compact-list rendering of exactly the catalog
  populations S4-M6 would bound. Lane A's `<ul class="item-list">` is the
  container slice 5 modifies, and the lane A record's own follow-up says the
  page is still 84,487 bytes over the owner's restated target on the tailnet
  form. **Slice 5 must land after lane B, not before**: lane B is a semantic
  delta on scoped epistemic attributes over the same item entries, and two
  passes rewriting the same `<li>` is one rebase nobody needs.
- **M5 (PR #39, P-72)** owns the agent briefing and names `polaris-copy.ts`
  and `design-tokens.ts` under predicate B. Slice 1 adds copy-table behaviour
  and slice 4 adds list styling; the overlap is the file, not the rows.
- **M9 (PR #41, P-75)** owns "one identity per item" across the surfaces, and
  slice 1's whole question is *which* identity string a label should show.
  **M9 decides the vocabulary slice 1 renders.** If M9 lands first, slice 1
  interpolates M9's identity; if slice 1 lands first, M9 will rewrite the
  interpolation. The cheaper order is M9 first, and if the owner wants slice 1
  sooner, the bead should say that it is interpolating a pre-M9 string.
- **M10 (PR #44, P-77)** owns the machine contract the identities in those
  labels are drawn from. The labels render a human-facing shortening of a
  machine identity; if M10 changes the identity's shape, slice 1's subject
  changes with it.

**M14 is a sequencing note, not a collision.** Bead `syzygy-dov.14`,
"Provenance depth", is not yet drafted and shares this packet's exact-text and
source-record surface: its S5-M2 drops the exact-source route's class gate and
its S5-M3 scopes the route to one requirement. Both change what an 'Exact
text' link *points at*; slice 1 changes what it is *called*. They do not
conflict, but M14 will add links to the 386 and change the 192, so slice 1's
uniqueness sweep should be written to a denominator it reads from the page
rather than to a constant.

**The shared governance file.** All twelve sibling branches add exactly one
row to `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` — P-68 (lane
B) through P-79 (M12), each present only in its own worktree's register
[Observed, counted this session with the predicate `^| P-` over the thirteen
worktrees' registers: 27 rows in each of the twelve, 26 in this one, and
exactly one row at or above P-68 in each of the twelve]. **This packet adds
no row**, by instruction: M13's five questions would be registered as
**P-80** after review 1, batched.

**Sequencing inside M13.** Slices 1 and 2 are independent of everything,
including each other, and are the two that should land first: together they
are a few dozen lines, they need no owner ruling on the recommended arms, and
they buy the most comprehension per byte. Slice 4 is independent of 1 and 2
and can land in parallel. Slice 3 should follow slice 1, because hoisting the
disclosure changes what the source row's controls are and the uniqueness
sweep is easier to write once against the final shape. Slice 5 comes last: it
waits on Q1, on Q4 and on lane B.

**Not verifiable this session.** [Unknown] Whether the sibling branches'
actual diffs stay inside the paths their packets cite, until they land — the
table above is computed over packet *text*, not over branch diffs. [Unknown]
Which arm the owner takes on Q1, and therefore what slice 5 is. [Unknown]
Whether Butlers' baseline-spec population is still 192 at the next
evaluation; it moved 185 → 192 between the two captures, so every count in
the catalog rows is an as-of figure and not a constant. [Unknown] The per-
fragment minimum hash depth of the four diagram captions and the
selected-passages block, which neither capture exposes.

## Gate 6 — Engineering bar

1. **Every count carries its predicate and its denominator**, and every one
   was taken this session — the source figures in the worktree at `a9f671e`,
   the page figures on the two named captures with their byte counts as
   denominators. Every literal sweep was run with Python `re` rather than
   with `grep` classes, per verification rule 1.
2. **Two methods for the load-bearing figures.** The 278 source records are
   established both by the `<details class="source-record">` count and by the
   count of `<summary>` elements reading literally 'Source record'; the two
   agree. The 386/192 link-to-target ratio is established both by matching the
   anchor text and by extracting the `href` values and deduplicating them
   percent-encoded and percent-decoded; the two agree. The 228 tab-stop figure
   is reproduced addend by addend against the dossier's own three addends
   before the second predicate is applied (rule 2).
3. **The claims of absence carry sweeps with denominators** (rule 9). "No
   specification sentence prescribes a disclosure element" is 0 occurrences of
   the literal "details" over 7 + 15 files. "No specification or doctrine
   sentence fixes a rendered heading level" is 0 matching lines over 7 + 6
   files and 16 over 15 PWB files, every one of the sixteen read and every one
   about the Butlers source grammar. "No decision constrains client-side
   scripting" is 0 over 67 decision files. Each sweep is case-insensitive and
   the pattern is published in the evidence record.
4. **Rule-6 mutants are specified per slice and per guard branch**, above;
   each names the predicate to mutate and the assertion that must then fail.
   Slice 3's mutant (b) is a *self-test of the guard*: if hoisting an
   attribute onto the `<table>` tag does not fail the reachability assertion,
   the assertion is the defect and must be repaired before the slice lands.
5. **The copy-oracle guardrail is applied in both directions.** The suffix
   form is chosen because `polaris-copy.test.ts` line 308's reach predicate
   admits it by `startsWith`; and the uniqueness sweep slice 1 adds is
   deliberately *not* a substring test, because a substring test over labels
   that all begin with the same seven characters would be satisfied by
   coincidence — which is the guardrail's original case read forward.
6. **Conformance expected values are literals in the tests**, never imported
   from the module under test (AGENTS.md), and each new assertion reports its
   denominator so a shrunken population fails rather than passes.
7. **No act-bound byte is proposed for edit.** Swept this session over the
   913 tracked files under `.syzygy/`, `openspec/`, `docs/` and `scripts/`:
   none of the 15 surface files appears as a digest row of any of the 66
   manifest-named files in that population, and no act manifest carries one.
   Two appear as *paths* in one evidence record, as mutation targets. That is
   a claim about acts only — see item 8.
8. **Two surface files are still at bytes a retained review confirmed, and
   editing one retires that confirmation.**
   `apps/three-surface-poc/src/polaris-reading.ts` and
   `apps/three-surface-poc/src/polaris-reading-plan.ts` hash to the two values
   `docs/reviews/R-POLARIS-VISIBLE-DIAGRAMS-FIDELITY-CONFIRMATION-2026-09-10-RAW.md`
   records; slice 2 edits the first. Verification rule 10 applied to a raw
   review: the implementing bead must re-run that bounded fidelity review and
   retain a new raw. Neither digest is reproduced here (CG-15); the review is
   cited by path.
9. **No governance prose is edited and no register row is added.** This
   packet writes exactly two files, both under `docs/`.
10. **Independent review.** This packet has had **none**. It is a first
    draft, and every figure in it is uncovered until a fresh-context review
    confirms it. Verification rule 10 applies to this file: any later edit
    retires a review bound to these bytes, and superseded wording will be
    marked and dated in place, never deleted.
11. **The battery was run in this worktree at the end of this session.**
    `scripts/check_governance.py` ends with 32 OK, 20 WARN and **0 FAIL**
    over 52 checks, counts derived rather than asserted, and neither of this
    packet's two files appears in any finding. No test suite was run: this packet proposes
    no code change, and the baseline suite's state at `a9f671e` is the lane A
    record's, cited by path rather than re-asserted here.
12. **Conventions this packet was checked against, this session.** Every
    non-fence line has an even backtick count, so no code span is broken
    across a line break. No observed-repository path is backticked anywhere in
    this file. No act argument, manifest digest or truncated signed digest is
    reproduced; the three digest-bearing records consulted are cited by path.
    Computed over the bytes this packet ends in: **0** of **1,209** non-fence
    lines has an odd backtick count; **20** lines exceed 78 columns outside
    fences, tables, block quotes and headings, each of them a single
    unbreakable code span or quoted literal; and of **232** distinct code
    spans, **15** contain a `/` and do not resolve as a path here. Each of
    the fifteen is enumerated in the evidence record and none is a path:
    four write-root globs, one governance-root directory reference inside
    the RFC9-13 quotation, one bare `decisions/` inside the RFC2-26
    quotation, one route-and-query shape, and eight HTML or template
    fragments quoted as markup.

## Funnel summary

```
## Feature Request: M13 - Navigation at population scale
Size: small (slices 1, 2) / medium (slice 4) / large (slices 3, 5)
Baseline: Syzygy a9f671e; the dossier audited a capture at f4589e2, BEFORE the lane A trim landed on main at 2ef68f5, so every dossier line number and population count below is re-derived at a9f671e and on the retained post-trim capture
- G1 Motif: 278 disclosure summaries read literally 'Source record' and 386 links read literally 'Exact text' over 192 distinct destinations, so the accessibility tree's own links list is two columns of identical strings; the one outline indexes 11 of the page's 39 h3 ids and sits behind a summary the page never opens (0 of 359 details are open in the served markup); 14 of the 18 markdown-derived headings land at h6 and h5 never occurs, from one expression, polaris-markdown.ts:157; 5 of those 14 are Syzygy's own synthesized '### ' at polaris-reading.ts:112 [Observed, all measured this session with predicates and denominators stated]
- G2 Doctrine: VIS-1 rank 2 (comprehension by simplifying presentation, never content) is the operative rule and VIS-3 is tagged with a stated qualification rather than inherited; VIS-2 and RFC9-13's "a filter that hides entities shows a persistent count of what it hid" bind slice 5; VIS-7's link rule and RFC7-34's "recoverable without colour, position, or layout" bind slices 4 and 1; no SEC rule is engaged
- G3 Topology: apps/three-surface-poc/src only; no governed artifact touched; slices 1, 2 and 4 cross no escalation trigger on any reading, slices 3 and 5 are tested against the continuation act's "any scope beyond the signed change" and put to the owner
- G4 Design: labels gain a suffix subject the same row already renders, chosen so the existing copy oracle's startsWith predicate still reaches them; heading levels map relative to the fragment's own minimum hash depth and the anchoring heading; the source record's four fields become three columns of the table its row is already in; the outline lists every h2 and h3 and the always-reachable quick-links becomes a 7-entry skip list, with no command palette because the page needs no script; the catalog populations get a bounded first view in whichever of three arms Q1 picks
- G5 Spec: 0 occurrences of the literal "details" and 0 of "outline" across both spec trees, so no scenario names the disclosure form or the outline; RFC2-26 run over all five slices (denominator 5): slices 1 and 4 map to named requirement-and-scenario pairs, slice 3's content maps to three requirements and one scenario while its form is named nowhere, slice 2's scenario fit is partial and its consequence class is not one the clause enumerates, slice 5 maps for arms (a) and (b) and is partial for arm (c)
- G6 Bar: two methods for every load-bearing figure; three absence claims each with a stated pattern and denominator; rule-6 mutants per slice including one self-test of an existing guard; no act-bound byte proposed for edit, with the retained fidelity review's re-run obligation recorded for slice 2; NO independent review yet - this is a first draft
Figures corrected against the dossier: 'Exact text' targets 372 -> 185 pre-trim and 192 post-trim (the dossier's figure was wrong on its own capture); source records 271 -> 278; 'Exact text' links 372 -> 386; details 353 -> 359; h6 15 -> 14; tables 10 -> 5; baseline-spec 185 table rows -> 192 compact-list entries; topology-component 87 table rows -> 87 compact-list entries; architecture-group citation links ~150 -> 89 over 2 distinct hrefs; in-group h3s outside the outline ~30 -> 28; polaris.ts source-record line 818 -> 835; exact-text line 1530 -> 378 and 1549; depthNav 1510-1538 -> 1529-1556
Acts: PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md (2026-09-02) as continued by PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md (2026-09-05); there is no PWB overlay change directory - the 2026-09-05 amendment replaced the spec bytes in place and they are bound by the eleven-row manifest, so no slice may edit them; slices 3 and 5 should be ruled against the continuation act's escalation triggers at lines 150-156
Open questions: Q1-Q5 above, NOT registered - this packet writes two files and no register row, by instruction; the row would be P-80 after review 1, batched. The twelve siblings' rows are P-68 lane B, P-69 M2, P-70 M3, P-71 M4, P-72 M5, P-73 M6, P-74 M8, P-75 M9, P-76 M7, P-77 M10, P-78 M11, P-79 M12, each only on its own branch
Governance check in this worktree at the end of this session: 32 OK, 20 WARN, 0 FAIL (52 checks) - counts derived, not asserted; neither of this packet's two files appears in any finding
Sign-off: pending - the owner's
Recommended handoff: land slices 1 and 2 now (no gate, few lines, the most comprehension per byte); then slice 4; rule Q2 and Q5 before slice 3; rule Q1, Q4 and Q5 and land lane B before slice 5
```

## Recommended handoff

**Land slices 1 and 2 first, under `syzygy-dov.13`.** Neither needs an owner
ruling on the recommended arms, neither crosses a trigger on any reading of
the act, and between them they fix the two defects that make the page
unusable non-visually at Butlers scale: 664 controls that do not name their
subject, and a heading outline with a hole where h5 should be. Slice 2 is a
few lines in two files. Slice 1 is a suffix and a uniqueness sweep. Together
they make the page's accessibility tree navigable for the first time since the
population passed a few dozen.

**Then slice 4, which is where the reader's time actually goes.** An outline
that indexes 11 of 39 sections and opens only for a reader who finds its
summary is not an index. The slice as designed keeps the collapsible, adds
the 28 missing ids and promotes seven links — the seven group headings — into
the always-reachable paragraph that already exists outside it. That is a
small change to one function with a browser-harness assertion behind it, and
it is the one slice whose benefit a reader notices on the first Tab press.

**Rule Q2 and Q5 before slice 3.** The hoist is the largest byte saving in
this packet (about 45,800 bytes, against a page with 612,665 bytes of
headroom and an owner target still 84,487 bytes away) and the largest single
improvement to the sources table, and it is also the one slice that removes
a stopping point a reader has today. The question is not whether it is safe —
no scenario names the form, and the content survives — but whether the owner
wants that level to exist. If the answer is "keep the level", the second arm
(identity and outcome as columns, the rest in the disclosure) gets half the
saving and changes nothing else.

**Slice 5 waits on three things and that is the right order.** It waits on
Q1, because a filter that needs script is a different product from a
disclosure that does not. It waits on Q4, because the bound coverage matrix
records that Polaris has no filter state and that row cannot be edited. And
it waits on lane B, because lane B rewrites the same list entries and two
passes over 324 items is one rebase too many. If the owner answers Q1 with
arm (a) — no script at all — slice 5 becomes small and can be taken with
slice 4.

**If M9 lands before slice 1**, slice 1 interpolates M9's identity and the
work is done once. If the owner wants slice 1 sooner, the bead should record
that it is rendering a pre-M9 string and that M9 will change it — which is a
cost worth paying, because 664 identical labels is a defect a reader meets on
the first page load and an identity vocabulary is not.
