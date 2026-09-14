# R-POLARIS-M6-GENERATOR-HONESTY-FUNNEL-1 — raw review

Review 1 of the M6 generator-honesty funnel packet. Fresh context,
read-only, no prior review. Independent reviewer (Claude), 2026-09-15.

## Bound bytes

Worktree: the M6 review worktree on branch agent/syzygy-dov.6.
HEAD `91b1343`; `git rev-parse HEAD^` = `a9f671e`, and the stat of that
head commit changes exactly the two reviewed files, so every measurement
below taken at HEAD is a measurement at the packet's stated baseline
`a9f671e` for all files other than those two. The short git status is
clean before and after this review.

| Artifact | Bytes (`wc -c`) | sha256 (`sha256sum`) |
|---|---:|---|
| `docs/design/POLARIS-M6-GENERATOR-HONESTY-FUNNEL.md` | 86188 | 5ff5520f5d4c3e709512c65bf81ca65ce4ac289c223d06a31f341999a418883d |
| `docs/evidence/polaris-m6-generator-honesty-funnel-2026-09-15.json` | 42882 | 29f5331b95056d6d7c2b841d5e5a19634131c67985befacbaa0b2e1050c38df6 |

Both digests computed this session, never transcribed. No act argument
and no signed digest is reproduced anywhere in this review; the two
digest records the packet consults are cited by path only.

Rule 10: this review is bound to those exact bytes. Any later edit to
either file retires it.

## What was re-run, and reproduced exactly

[Observed, all this session in the worktree.]

- **Schema field census.** Imported `stageSchema` from the package's own
  built `provider-draft.js`, walked all six stage schemas, collected
  every `properties` key and every `enum`. Per stage: `inventory` 5,
  `plan` 5, `author` 15, `edit` 15, `repair` 15, `fidelity` 6. Distinct
  across all six: **25**, the same 25 names the packet lists. Enums: **2**
  (`entries[].kind`, 9 values; `findings[].severity`, 2 values), **11**
  enum values in total. Under the packet's stated predicate — a name or
  enum admitting a per-asset or per-claim disposition, an unresolved or
  omitted state, or an epistemic class — **0** of the 25 and 0 of the 11
  qualify. Independent second method (rule 2): Python `re` sweeps of
  `provider-draft.ts` and `pipeline.ts` for `disposition`, `unresolved`
  and `unnecessary`, case-insensitive, return 0 in both files. The two
  methods agree.
- **`author`, `edit` and `repair` are one object.** `JSON.stringify` of
  the three returned schemas is byte-equal; only `version` differs.
  Declaration at `packages/polaris-generation-core/src/provider-draft.ts`
  line 33, as cited.
- **Fidelity shape and verdict polarity.** `fidelity` at lines 30–32;
  `findings` `minItems` 0 at line 31; `reviewVerdict` at lines 148–152
  returns blocking only when some finding carries the blocking severity
  value; `same()` at 86–89 throws `incomplete-coverage`; the two
  `same()` calls at 127–128 force both whole populations. All as stated.
- **`references()` is existence-only.** Lines 90–98 test only
  `sources.has(id)` over every `sourceIds` array. Nothing compares a
  claim's text to a source's text.
- **No validator compares output to input.** `context.draft` occurs at
  exactly lines 124 and 126, both inside the `fidelity` branch;
  `priorDraft` 0 occurrences; the `else` branch at 131–144 reads
  `context.plan` at 133, 134 and 137 only. Denominator: the whole file,
  152 lines by `wc -l`.
- **Prompt directive count.** 5 directives naming a schema for missing
  or unsupported material, at `prompts.ts` lines 6, 13, 18, 21 and 22,
  each quoted verbatim in the packet and verbatim at source. Corroborating
  sweeps reproduce: `unresolved` 6 (lines 6×2, 10, 13, 21, 22),
  `disposition` 5 (10, 13, 16, 21, 22), `omission` 2 (10, 20),
  `unsupported` 5, `omitted` 0, `unknown` 1 (line 27, the error string).
- **The example-file validator run.** Rebuilt the context from the file's
  own single source and called `validateStage` for each of the six landed
  stages against `illustrativeOutput`, `illustrativeLaterDraft` and the
  whole file: 18 calls, **18** `invalid-fields`, 0 passes; plus
  `stageSchema('understand')` throwing `invalid-stage`. 19 of 19, with
  the packet's stated denominator. `illustrativeOutput`'s five keys are
  exactly `editorialState`, `claims`, `unresolved`, `assetDispositions`,
  `coverage`, none in the 25-name census, and `check()` at lines 61–63
  rejects on key-set inequality before examining contents, as stated.
- **The demo command chain.** Run as-is: exit **0**, stdout exactly the
  success line the packet quotes, 7 output files (3 `.html`, 3 `.json`,
  `report.json`). Counterexample re-run (symlink moved aside, both
  `dist` trees removed): exit **2**, **42** `error TS` lines, **5**
  `TS2307` naming the workspace package, across **6** files, all under
  the generation directory of the POC app — the packet's figures exactly,
  and the first error line matches its evidence record verbatim. Symlink
  restored, rebuilt, rerun: exit **0**, same success line. The short git
  status is clean afterwards; the symlink is back in place.
- **`build:poc`.** `package.json` line 15 is `tsc -b --force` over four
  projects and does not name the generation package. Confirmed. (Note
  that `build` at line 14 and `typecheck` at line 21 do name it; the
  defect is real for the demo chain, which runs `build:poc`.)
- **`tasks.md` census.** Predicate `^- \[[ xX]\] `: **24** boxes, **0**
  checked. Tasks 1.4, 2.2, 2.4 and 3.5 are at lines 11, 22, 24 and 50
  and their quoted texts are verbatim.
- **No-egress sweep.** Literal `egress`, case-sensitive, over the four
  kit files (102 + 144 + 108 + 119 = 473 lines): **1**, at the kit
  README line 4. `grants no`: **2**, the same line and the
  `ARTIFACTS-AND-TOOLS.md` line 15 sentence, correctly characterised as
  about grant validity rather than a grant. `AUTHORING.md`: **0** of
  either. `npm ci`: **0** over the core README plus the four kit files.
  `poc:generator-demo` occurs once in either README, at core README
  line 55.
- **Every contract and spec quotation.** All checked at source, at the
  cited lines, against the defined clause (rule 8):
  - REQ-polaris-generation-002 at overlay line 9 (`ID:` at 11);
    REQ-004 at overlay 78 (`ID:` 80); REQ-006 at overlay 180 (`ID:` 182);
    REQ-019 at overlay 453 (`ID:` 455). Predecessor: REQ-002 at base 52,
    REQ-003 at base 98, REQ-006 at base 302, REQ-019 at base 1015. Every
    sentence the packet quotes is verbatim and contiguous at those lines.
  - REQ-019's first two sentences are identical between overlay and
    predecessor; first divergence is at character 2158 of the paragraph,
    well past them, as claimed.
  - The composition rule: the overlay's `ID:` lines are exactly 002, 004,
    006, 009, 012, 014, 019, 030, 031 — the seven modified plus the two
    added the understanding act's Scope paragraph names, which the packet
    quotes verbatim (that act, lines 29–32).
  - Gate 5 scenarios: "Two requested diagrams have different obligations"
    at overlay 465–469; "Required visual unavailable" at 103–107; "Source
    trade-off omitted entirely" at 199–203; "Omitted material
    qualification" at 205–212; "New evidence outside the current budget
    or authority" at 214–220; "No supported optional asset" at 91–95;
    "Research projection cannot mint authority" at 501–505; "Computed
    output has no enabled production renderer" at base 159–163;
    "Editorial relationship diagram" at base 117–121. All exist at the
    cited lines with the quoted WHEN/THEN text verbatim.
  - REQ-006's scenario headings are exactly five, at overlay 187, 193,
    199, 205 and 214, and **none** states the edit-stage silent-deletion
    case. The packet's [Observed] claim reproduces.
  - Every requirement the packet maps a slice to (003, 004, 006, 019)
    lies inside Phase A's named set, `EXECUTION-PHASES.md` line 18,
    "Requirements 001-012, 014-019 and 025". Phase A's scope sentence at
    lines 10–11 is quoted verbatim.
  - `SCHEMA-CONTRACT.md` lines 33–39: the heading at line 26, the
    requested/output distinction at 28–31 including "Requiredness cannot
    be downgraded by provider output", and the three-row table at 35–39
    with every payload and invariant the packet quotes field-for-field.
  - The implementation-authorization act's line 42 is quoted verbatim,
    all 402 characters.
  - RFC2-26: the whole clause at lines 196–221 under the heading at 194,
    quoted with **no elision** — 1,781 characters, byte-identical after
    whitespace normalisation.
  - Doctrine: VIS-2 at 96–106 (including "a stale view silently green"),
    VIS-3 at 108–110, VIS-4's "One class is always human-gated, gate open
    or not: … normative data contracts" at 131–133, VIS-5's
    "materialization is exclusively a worker action against scheduled
    work" at 158–159, SEC-1 at line 10, SEC-2 at 25–37 including "Model
    providers are such services." All verbatim. The S9-F4 tag correction
    from SEC-1 to SEC-2 is right.
- **Bound-byte constraint (b).** The current sha256 of
  `SCHEMA-CONTRACT.md` does equal the value recorded for that path in
  the v2 coverage record's `subjectBindings` map. Verified by comparison,
  neither value reproduced here.
- **Bound-byte constraint (c).** The scope record's `status` is
  "unadopted; awaiting final independent review and owner acts" and
  `implementedGenerator` is false, over 21 file rows — a pre-act snapshot,
  as the packet says. The five package-contract files the packet names
  are all rows.
- **No act-bound byte is proposed for edit.** Swept all nine
  slice-touched paths against every file under the governance decisions
  tree, the governance contracts tree and `docs/evidence`: no act
  manifest carries any of them. (See F10 for what does.)
- **The dossier.** The M6 ranked-move entry, its `merges` list, its
  `prerequisite` string, the prose What/Slices/Prerequisite bullets, and
  S9-F1's "main @ `1932f74`" evidence line all read as the packet reports.
  The packet records the `syzygy_audited_at` discrepancy in its own two
  files and proposes no edit to the dossier — correct handling.
- **Packet self-checks, Gate 6 item 11.** All reproduce exactly: 1,073
  non-fence lines; **0** with an odd backtick count; **2** lines over 78
  columns outside fences, tables and headings, both a single code-span
  path; **261** distinct code spans; **10** containing a `/` that do not
  resolve, and they are exactly the ten enumerated.
- **Governance check.** Running `scripts/check_governance.py` in this
  worktree ends `32 OK, 20 WARN, 0 FAIL (52 checks)`. No finding names
  either reviewed file.
- **Collision.** M6's candidate surface is **23** files, as stated, and
  the file-set intersection with every sibling packet is **0** — M2, M3,
  M4, M5 and lane B, recomputed against those worktrees at their current
  heads. The two near-misses are quoted accurately; both sibling mentions
  are baseline-provenance prose and M5's says in terms that none of the
  files it cites is touched. M6's worktree carries no pending-register
  row; the five siblings carry P-68, P-69, P-70, P-71, P-72.

That is a high reproduction rate. The findings below are what did not
reproduce, or what the packet did not say.

## Findings

### F1 — blocking

Packet lines 31 (Q6), 509 (Gate 3 authorizing-act table, slice 4) and
881 (Gate 5 RFC2-26 table, slice 4), in
`docs/design/POLARIS-M6-GENERATOR-HONESTY-FUNNEL.md`.

**Defect.** The packet's authorization analysis never names the
understanding-adoption act's own limiting sentence. In the governance
decisions tree, POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md
lines 39–41 read: "Existing implementation and applicability acts retain
their own exact scopes. This act grants no implementation extension,
source/provider/content permission, write consent, deployment or
release." Gate 0 lists that act, and Gate 0's composition paragraph
quotes its Scope paragraph from lines 29–32 — nine lines above — so the
file was read and the sentence was passed over.

This is load-bearing for slice 4 and only for slice 4. Slice 4's single
named requirement clause, in both Gate 3 and Gate 5, is "The original
finding, repair, dispositions and input/output identities SHALL remain
traceable" (overlay REQ-polaris-generation-006, line 180). I swept both
specification files for that exact sentence this session: **1**
occurrence in the overlay, **0** in the predecessor. It is
amendment-added text. By contrast every clause the other slices rest on
is predecessor text carried through unchanged — REQ-004's "Every
requested asset SHALL have an explicit produced, reasoned-omission or
unresolved disposition" is present verbatim at base line 186, REQ-006's
coverage-and-readiness sentence at base line 302, REQ-019's disposition
sentence at base line 1015 — all inside the requirement set the
implementation-authorization act names, so slices 2, 3 and 5 are covered
on either reading.

So Q6's answer, "The existing implementation-authorization act covers
all five; no new act is needed", is stated without disclosing that one
of the five is scheduled from bytes the predecessor does not carry and
that the act adopting those bytes disclaims any implementation
extension. Two readings are genuinely available — (i) the impl act
authorizes requirements by identity, so an amended REQ-006 is still
REQ-006; (ii) "grants no implementation extension" means newly added
clauses are not thereby authorized work — and the packet silently takes
(i). [Inferred: which reading the owner holds. Observed: the sentence
exists, the clause is overlay-only, and the packet names neither.]

The consequence is not cosmetic. Q6's second arm advises that if the
owner rules the other way, "hold those two and land 1, 4 and 5", calling
slice 4 "the least gated of the three schema slices" because "its
requirement is named in the effective REQ-polaris-generation-006". On
reading (ii) slice 4 is the *most* gated of the three, because its
requirement is named **only** in the effective text and not in the
authorized predecessor. A lawful arm is therefore missing and a
recommendation points the wrong way.

**Repair.** (a) Quote the sentence at Gate 0 and in Q6. (b) Add one
column or line to the Gate 3 act table recording, per slice, whether its
named clause is predecessor text (give the base line) or overlay-only.
(c) Add the arm to Q6: slice 4 (and deferred slice 6, whose glossary
clause "Glossaries SHALL explain concepts where needed for
comprehension" is likewise overlay-only — 0 occurrences in the
predecessor) may need a fresh owner direction or a CC-REV-2 scenario
because their clauses arrived with an act that grants no implementation
extension. (d) Correct Q6's second-arm handoff sentence accordingly.

### F2 — non-blocking

Packet line 184, and the run-1 output-byte total in the evidence
record's demo-command-chain measurement.

**Defect.** "Run 1 produced 7 files — three `.html`, three `.json` and a
`report.json`, 41,940 bytes in total." Re-run twice this session into
two separate output directories: 7 files both times, **87,940** bytes
both times (11,308 + 15,713 + 11,395 + 15,981 + 11,313 + 15,655 +
6,575). The generator's output is deterministic across the two runs, so
this is not run variance. The file list and count are right; the total
is not, in both the packet and its machine record. [Observed.]

**Repair.** Correct both figures to the measured total, or state the
method that produced 41,940 so a reader can reconcile it.

### F3 — non-blocking

packet line 306.

**Defect.** "The package exports exactly two validators over provider
payloads: `validateStage` … and `reviewVerdict` …; the other four
exports are `encodeCanonicalJson`, `digestCanonicalJson`,
`parseBoundedJson` and `stageSchema` [Observed, enumerated by a literal
sweep for lines beginning `export` …, over the four non-test sources]."
Two parts do not hold. `packages/polaris-generation-core/src/index.ts`
lines 1–14 re-export **eleven** runtime values: those four, the two
validators, and `CANONICAL_JSON_ENCODING`, `CanonicalJsonError`,
`BoundedJsonError`, `promptForStage` and `runGenerationPipeline`. And
`packages/polaris-generation-core/src/` holds **six** non-test sources,
not four. The stated predicate would not yield four either: it includes
`export function` and `export const`, which `promptForStage`,
`runGenerationPipeline` and `CANONICAL_JSON_ENCODING` all match.
[Observed.]

The claim this enumeration supports — that no validator in the package
compares a stage's output to its input — is independently established by
the `context.draft`/`priorDraft` sweep and reproduces exactly, so
nothing downstream moves.

**Repair.** Drop the "other four exports" enumeration or correct it, and
correct the denominator to six non-test sources here and at packet line 329.

### F4 — non-blocking

packet line 384.

**Defect.** "`git diff --numstat f4589e2 a9f671e` over
`packages/polaris-generation-core`, `docs/polaris-generation`,
`package.json` and `apps/three-surface-poc/src/polaris-generation` shows
all 22 files added with 0 deletions, including every file L3 and S9
cite." Re-run: 22 rows, of which **20 are additions and 2 are
modifications** — the kit README (16 added, 4 deleted) and
`package.json` (4 added, 2 deleted); `git diff --name-status` gives 20
`A` and 2 `M`. And three files this packet leans on existed at
`f4589e2` unchanged, so they appear in no row at all:
`docs/polaris-generation/example.json` (the whole subject of Q4),
`docs/polaris-generation/AUTHORING.md` and
`docs/polaris-generation/ARTIFACTS-AND-TOOLS.md` (slice 5's two targets
and five of the six rows of the kit-promises table). "Including every
file L3 and S9 cite" is therefore false, and the header sentence "The
dossier's stated audit commit does not hold for these two surfaces" is
over-broad: for those three files the dossier's audit commit holds
exactly. [Observed.]

The conclusion the paragraph draws does survive, independently: the same
diff restricted to `1932f74..a9f671e` returns 0 rows, which I confirm.
One gap remains in its denominator — that diff covers only the four
implementation paths, while the citation table below it also cites
specification lines. I checked separately: `1932f74..a9f671e` over
`openspec/` and `.syzygy/` returns 3 rows, all decision-register files
and no specification file, so the spec citations are current too.

**Repair.** Restate as 20 added and 2 modified; name the three unchanged
files; extend the currency sweep to the openspec paths the table cites,
or say explicitly that the spec files were checked separately.

### F5 — non-blocking

Packet lines 171 and 407, and the same class at packet lines 117, 328,
333 and 334.

**Defect.** The kit files are hard-wrapped, and the packet's line
citations name the line carrying the distinctive half of a quotation
rather than its span. Two are wrong rather than merely narrow:

- Packet line 171 — "The README's command is at … line 55, under the
  sentence at line 53, 'Run the controlled end-to-end example from
  the repository root:'." That sentence is at line **52**; line 53 is
  blank. The command at line 55 is right.
- Packet line 407 — the re-verification table corrects S9-F3's
  `AUTHORING.md` 45-49 to "45–46 … the sentence ends at 46". The
  sentence is "For each
  visual supply its reader question, named nodes, typed edges, edge /
  meaning, source support, necessary qualifications, text equivalent and
  proposed / placement." — it ends on line **47**, so the span is 45–47
  and the finding's range was closer than the correction. The packet's
  own quotation includes the word that sits on line 47.

Narrower instances, where the quotation starts or ends on an uncited
line: the product-promise sentence cited at kit README line 70 begins on
line 69 (the dossier's S9-F2 cites 69-70 and is more precise); the Plan
prompt quotation cited at `AUTHORING.md` line 102 begins on line 101;
the asset-disposition sentence cited at `ARTIFACTS-AND-TOOLS.md` line 43
begins on line 42; the deep-dive promise cited at `AUTHORING.md` line 62
ends on line 63; and the glossary clause at `AUTHORING.md` :26, marked
"exact" in the table, ends on line 27. [Observed, all read at source.]

This matters more than usual in this repository: AGENTS.md records that
a citation wrapped across a line break is invisible to a basename sweep,
and a table presented as a citation correction is exactly where a reader
will trust the span.

**Repair.** Give the full span for every wrapped quotation; correct
packet line 171 to line 52 and packet line 407 to 45–47.

### F6 — non-blocking

packet line 328.

**Defect.** "the literal `glossar` occurs 0 times in `provider-draft.ts`
and `pipeline.ts`, and once in `prompts.ts` (line 13, as prose)
[Observed, case-insensitive sweep over the four non-test sources]."
Re-run with Python `re`, case-insensitive: 0 and 0 as stated, but
**2** in `prompts.ts` — line 13 ("Use contents, glossary and comparison
tables only when they help") and line 20 ("every generated claim-bearing
block, table cell, glossary explanation, deep dive and factual diagram
element/edge must have actual support"). The line-20 occurrence is in
the fidelity prompt, which makes it slightly more pointed than the
packet's version: the review prompt asks the model to check glossary
explanations the schema cannot carry. The schema-absence claim is
unaffected. [Observed.]

**Repair.** Correct the count to 2, name line 20, and fix the "four
non-test sources" denominator (see F3).

### F7 — non-blocking

packet line 891 and packet line 881.

**Defect, two parts.** (a) RFC2-26's scope sentence is cited at line
221: "RFC2-26's own scope sentence — 'This clause binds the whole RFC
0002 package, not this module alone' (line 221)". The sentence is at
lines **219–220**; line 221 carries the shape-parallel list. Same
wrapped-citation class as F5, in the sentence a reviewer is asked to
test. The clause quotation itself is complete and verbatim.

(b) On the substantive question the packet's reading survives. RFC2-26
bars implementation work "for user-observable consequences **of this
contract** … scheduled **solely from this RFC**"; the scope sentence
widens the rule across the RFC-0002 package's modules, not across
non-RFC-0002 work, so it does not defeat the reading. The packet also
preserves the narrow-scope reading as an arm, twice — in Q6's
counter-argument and in the closing "a reading the owner may take more
or less broadly than this packet has". Good.

But the slice-4 row names only one repair route if the owner reads the
bar strictly: "a scenario added through CC-REV-2". The clause the packet
quotes in full names a second, two sentences later: a reviewed N/A
judgment homed in `decisions/`, honored only through an effective owner
act under RFC3-16(a). For a packet whose job is to enumerate the owner's
lawful arms, leaving that one out of the row that needs it is a gap.
[Observed: the clause names it. Inferred: whether it fits slice 4,
since the clause requires the consequence be "purely structural with no
independently testable behavior" — which a change account plainly is
not, and saying so is itself the useful disclosure.]

**Repair.** Fix the line citation; add the N/A-judgment arm to the
slice-4 row, with the packet's own view of whether it is reachable.

### F8 — non-blocking

packet line 30 (Q5).

**Defect.** Q5 is ordinary engineering presented in the owner-gate
table. The packet establishes itself, at packet lines 507 and 838, that
slice 1 needs no act, crosses no act trigger, touches no bound byte and
enumerates no RFC-0002 consequence. Its three limbs are a README
sentence, one entry in a `tsc -b` project list, and a battery assertion.
Only the assertion carries a real trade-off (an `npm ci` in the
battery), and that is a cost judgment a delegate can make. Giving it a
"Default if unanswered: the install line lands and the assertion does
not" puts a routine engineering choice behind owner silence, and makes
the packet read as six gates when it has, at most, three (Q1, Q3, Q6).
[Inferred — a judgment about question classification, not lawfulness.]

**Repair.** Say in the Q5 cell that it is a cost trade-off the owner may
delegate rather than a gate, and keep the `build:poc` limb as a stated
decision rather than a question.

### F9 — non-blocking

packet line 28 (Q3).

**Defect.** Q3's second arm is described as "honest to read, unchanged
in effect", and its default as "rows are added, polarity is not
changed". What the cell does not say is which arm conforms to the
requirement it quotes. The effective REQ-polaris-generation-006 sentence
— "unresolved material omissions SHALL prevent readiness" (overlay line
180; identical at base line 302, verified) — is the obligation the
second arm leaves unimplemented, because today an unresolved material
omission that the model declines to report as `blocking` does not
prevent readiness. That is lawful, since Phase A is unfinished (all 24
`tasks.md` boxes unchecked), but it is a trade-off the owner is entitled
to see named rather than read as neutral. The packet is otherwise
careful here — it grounds the polarity in VIS-2 rather than reading
fail-closed into REQ-006, which is the honest move and I confirm the
quotation does not require it. [Observed for the quotation; Inferred for
the conformance consequence.]

**Repair.** One sentence in the Q3 cell: the second arm defers
conformance with that sentence of REQ-006, lawfully, and the bead should
record it.

### F10 — non-blocking

packet line 1022 (Gate 6 item 8) and packet line 489 (Gate 3).

**Defect.** Slices 2, 3 and 4 rewrite
`packages/polaris-generation-core/src/provider-draft.ts`, and slice 2
also `apps/three-surface-poc/src/polaris-generation/draft-preview.ts`.
Both are digest rows of
`docs/evidence/polaris-pipeline-synthetic-verification-2026-09-13.json`,
which records 17 source digests over exactly this surface; I confirmed
that the digest it records for `provider-draft.ts` equals that file's
current bytes, without reproducing either value. Gate 6 item 8's claim
is correct as written — no *act*-bound byte is proposed for edit, which
I verified by sweeping all nine slice-touched paths against every file
under the decisions, contracts and evidence trees, finding no act
manifest row for any of them. But the packet nowhere records that
landing slices 2–4 retires that verification record's binding to those
bytes and obliges a re-run. That is rule 10's shape applied to an
evidence record rather than a review, and it is the kind of thing this
packet otherwise tracks well. [Observed.]

**Repair.** Name the record in Gate 3 or Gate 6 and record the re-run
obligation for slices 2, 3 and 4.

### F11 — non-blocking

packet line 970 and packet line 941–packet line 960 (the collision section).

**Defect, two parts.** (a) "All four sibling packets add a row to
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`." There are
**five**: lane B P-68, M2 P-69, M3 P-70, M4 P-71, M5 P-72 — each present
in its own worktree's register and absent from the other four, and none
present in M6's. The funnel summary itself lists all five, so the prose
undercounts what the packet's own summary says.

(b) The intersection table names PR numbers but no sibling commit, so
its counts cannot be re-derived (rule 7). Recomputed this session
against the sibling worktrees at their current heads — M2 `f2f37dd`,
M3 `6574600`, M4 `63b8e33`, M5 `ba9ca61`, lane B `4090f98` — the
intersection is **0 for every sibling**, which is the load-bearing
claim and it holds; M6's surface is 23 files, as stated. The per-sibling
"resolving implementation paths" counts do not reproduce: I get 11, 13,
22, 9 and 1 where the packet reports 17, 15, 26, 11 and 3. The most
likely cause is that those branches advanced after the packet measured
(each head is a later review-applied commit), which is exactly why the
commit belongs in the row. [Observed.]

**Repair.** Say five; name the sibling commit each count was taken at,
or drop the counts and keep the intersection, which is the only figure
that carries weight.

### F12 — editorial

Internal inconsistencies, collected.

(a) Packet line 411 — "**Four figures that differ from the dossier**,
collected"
against the companion record's `figures_that_differ_from_the_dossier`,
which enumerates **six**. The two extra — S9-F3's line ranges, and the
`build:poc` omission — do appear in the packet's prose elsewhere, but a
reader comparing the collected list with the machine record finds a
mismatch in a list whose whole purpose is to be complete. (Note also
that the record's fifth entry repeats the F5 error: "AUTHORING.md 45-49
(the sentence ends at 46)".)

(b) Packet line 7 — the banner says "no arm below is called lawful or
unlawful by this packet", while each of Q1–Q6 labels its alternative
a "**Second lawful arm**". One or the other should give.

(c) packet line 184 — "The remaining 37 errors in run 2 are downstream
`TS7006`/`TS2339` consequences". Re-run: the 42 break down as 32
`TS7006`, 5 `TS2307`, 4 `TS2339` and 1 `TS7053`. 36 of the 37, not 37.

(d) Denominator convention drifts between measurements: `prompts.ts` is
given as "30 lines" and `tasks.md` as "a 52-line file" (split-on-newline
counts), while `provider-draft.ts` is given as "152 lines" (`wc -l`).
Each is right under one convention and off by one under the other; the
packet should name the convention once.

**Repair.** Mechanical in each case.

### F13 — non-blocking

packet line 26 (Q1) and packet line 812 (Gate 5's residue paragraph).

**Defect.** Q1's residue is stated as a forced literal contradiction:
"four spellings of a three-value enum across four artifacts, three of
which are digest-bound and cannot be edited to agree. Whichever literal
the implementation picks, it will disagree with at least one bound
artifact". The divergence is real and I verified all of it at source:
`SCHEMA-CONTRACT.md` lines 35–39 give Produced / Omitted / Unresolved;
REQ-019 (overlay 453, base 1015) says "produced, omitted or unresolved";
REQ-004 (overlay 78, base 186) says "produced, reasoned-omission or
unresolved"; `AUTHORING.md` line 102 says "planned,
unnecessary-with-reason or unresolved"; `ARTIFACTS-AND-TOOLS.md` line 43
says "produced, unnecessary-with-reason or unresolved". The three bound
/ two unbound split is also right — the two kit files appear in no act
manifest.

What is a reading rather than an observation is the forcing step. Of the
three bound artifacts only `SCHEMA-CONTRACT.md` **declares** a closed
vocabulary — line 33, "Each request resolves to exactly one
disposition:", followed by the three-row table. REQ-004 and REQ-019
describe the three dispositions in prose inside long requirement
paragraphs. A schema field named `omitted` that requires a reviewable
reason is a plausible satisfaction of REQ-004's "reasoned-omission",
because REQ-004 is stating that an omission must be reasoned, not
declaring a token. The packet's `[Inferred]` label in that cell attaches
to "that choice is the owner's", not to the forcing step, so the step
reads as measured. [Inferred — a reading of what those two requirement
sentences declare.]

This matters because the residue is the packet's stated reason Q1's
amendment arm is coherent, and it is what the Recommended handoff leans
on: "the reason it is coherent is the enum-spelling residue, which means
*any* implementation of the field will contradict a bound artifact".

**Repair.** Label the forcing step `[Inferred]`; say which of the three
declares a vocabulary and which two describe one; and let Q1 stand on
the divergence itself, which is real and is enough.

## The six questions

| # | Scope truthful? | Genuine gate? | Recommendation follows? | Lawful arms all named? |
|---|---|---|---|---|
| Q1 | **Yes.** The field census, the three bound artifacts and the spelling divergence all verify at source. | **Yes.** Whether conforming code to a normative data contract is implementation or amendment is squarely VIS-4's human-gated class, and the packet quotes VIS-4 correctly. | **Yes**, with F13: the recommendation is sound; the counter-argument overstates its force by reading prose as enum tokens. | **Yes** — implementation arm, CC-REV-2 amendment arm, and a stated default. |
| Q2 | **Yes.** `references()` is existence-only (lines 90–98, verified) and the two requirement quotations are verbatim at the cited lines. | **Partly.** This is a scoping decision more than a gate, but it is a large one and the packet says so plainly; presenting it is reasonable. | **Yes.** Defer-with-a-strong-counter is an honest shape, and the counter-argument is genuinely put rather than smoothed. | **Yes** — defer, or take it now as slice 2b. |
| Q3 | **Yes.** `minItems` 0 at line 31, `reviewVerdict` at 148–152, the REQ-006 quotation at overlay 180 — all verified. | **Yes.** It changes when a run reaches an owner-visible readiness state; the packet identifies that as the reason the owner should rule it. | **Yes**, with F9: the recommendation follows from VIS-2, and the packet correctly does *not* read fail-closed into REQ-006. | **Yes** — polarity change, rows-only, with the default stated; but the rows-only arm's conformance cost is unstated (F9). |
| Q4 | **Yes.** 19 of 19 reproduces exactly, and the fairness qualification — the file never claimed validator conformance — is the right correction to make against the packet's own interest. | **No, and the packet does not claim otherwise.** It is an editorial choice about a kit file bound by nothing; both arms are cheap. | **Yes.** | **Yes** — regenerate, or one routing sentence, with the default named. |
| Q5 | **Yes.** Every measurement reproduces, including the counterexample in both directions and the `build:poc` omission. | **No.** Ordinary engineering in the owner-gate table (F8). | **Yes**, on the merits. | **Yes** — both arms and the third limb are named. |
| Q6 | **Partly.** The act quotation, the Phase A scope and requirement set, the RFC2-26 clause and every requirement-and-scenario mapping verify exactly; what is missing is the understanding act's own limiting sentence (F1). | **Yes.** It is the one question that could stop every slice, and it is correctly identified as such. | **No, for slice 4.** The conclusion "no new act is needed" is drawn without the evidence that bears on it, and the second-arm handoff calls slice 4 the least gated when on the competing reading it is the most (F1). | **No.** The overlay-only-clause arm (F1) and RFC2-26's own reviewed-N/A-judgment arm (F7b) are both unnamed. |

## Overall

This is a strong, unusually well-measured packet. Almost every figure in
it reproduced under an independently written predicate, the contract and
doctrine quotations are verbatim at the defined clause without exception,
the Gate 5 requirement-and-scenario test holds at every cited line, the
collision result holds, the packet's own convention self-checks reproduce
to the digit, and the governance battery is clean. Its habit of stating
a predicate and a denominator beside every count is what made this review
cheap, and its corrections against its own interest — the demo succeeds,
S9-F1 is overstated, the example file never claimed conformance — are the
best thing in it.

It revises on one thing: the act analysis at its centre omits the one
sentence, in an act it lists and a file it quotes, that bears directly on
whether slice 4 is authorized, and that omission reverses a
recommendation. Everything else is arithmetic and citation hygiene.

Findings by severity: 1 blocking, 11 non-blocking, 1 editorial.

Verdict: REVISE
