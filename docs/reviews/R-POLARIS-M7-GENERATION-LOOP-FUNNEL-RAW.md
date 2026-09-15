# R-POLARIS-M7-GENERATION-LOOP-FUNNEL — review 1 (raw, retained verbatim)

Reviewer: independent fresh-context session, 2026-09-15. No prior review.
Worktree: scratchpad `m7wt`, branch agent/syzygy-dov.7, HEAD `0c4b4a9`
("docs: Polaris M7 generation-loop funnel packet, first draft
[syzygy-dov.7]"). Baseline the packet measures at: `a9f671e`.

## Bytes reviewed (computed with wc -c and sha256sum, never transcribed)

| File | Bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M7-GENERATION-LOOP-FUNNEL.md` | 109383 | 9465bf5934b91f5d12bd067fc55bbc26511610fb780b97b67dbe81dfb5f12d0f |
| `docs/evidence/polaris-m7-generation-loop-funnel-2026-09-15.json` | 28824 | f44d2f3024784ac4a511ca0576bdd97dbafe2f42c4a5baa385fb79c22632ef57 |

`git diff --name-status a9f671e HEAD` in this worktree returns exactly two
rows, both `A`, both the files above: the packet writes no register row, as
it says [Observed, run this session].

Sibling heads read this session, all read-only in their own worktrees:
lane B `4090f98`, M2 `f2f37dd`, M3 `6574600`, M4 `63b8e33`, M5 `ba9ca61`,
M6 `83c9f60`, M8 `8035c8f`, M9 `206d775`. M1's packet was read on this
worktree's own tree at `a9f671e`.

`npm run build:poc` exit 0 in this worktree;
`python3 scripts/check_governance.py` last line read in full:
"32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted".
`git status --short` is empty at the end of this session — nothing new under
tracked paths. `npm test` was
not run: no claim in the packet turns on it, and the pipeline figures were
taken by driving the built modules directly.

Rule 1 observed throughout: every load-bearing sweep below was run with
Python `re` or exact substring counting, never a bracket class.

---

## Findings

### F1 — non-blocking — the "20 files" denominator names the wrong set

`docs/design/POLARIS-M7-GENERATION-LOOP-FUNNEL.md` Gate 1 item 1, Q3, the
SEC-2 paragraph in Gate 2, Gate 6 items 1 and 2, and the funnel summary;
`docs/evidence/polaris-m7-generation-loop-funnel-2026-09-15.json`
`measurements.plane_disjointness.denominator` and
`measurements.egress_surface.denominator`.

**Defect.** The stated denominator is "the 20 files of
`packages/polaris-generation-core/src` and
`apps/three-surface-poc/src/polaris-generation`". That set is **17** tracked
files (11 + 6), not 20. 20 is the count for the whole core *package* (14
tracked files, including its README, package.json and tsconfig.json) plus
the app directory (6) [Observed, `git ls-files` over both spellings this
session]. A reader who re-runs the sweep as written gets a different
denominator from the one the figure was taken over — rule 2's whole point.

**Not a defect in the result.** I ran both sweeps over both sets. The three
plane literals (`three-surface-poc-core`, `PocModel`, `projectShape`) occur
0 times over the 17-file set and 0 times over the 20-file set; the six
network primitives occur 0 times over the 20-file set and the three
`https://` hits are the two escaping fixtures in
`apps/three-surface-poc/src/polaris-generation/draft-preview.test.ts` lines
48 and 59 and the one in
`packages/polaris-generation-core/src/provider-draft.test.ts` line 61 — all
three inside tests, exactly as claimed.

**Repair.** Write the denominator as "the 20 tracked files of
`packages/polaris-generation-core` and
`apps/three-surface-poc/src/polaris-generation`", in the packet at every
site and in the two evidence fields.

### F2 — non-blocking — the evidence record's self-corpus predicate yields 107 files, not the 105 it reports

`docs/evidence/polaris-m7-generation-loop-funnel-2026-09-15.json`
`measurements.self_corpus.predicate`; packet "What a real corpus costs" and
Q2.

**Defect.** The record's predicate reads "every tracked .md under
.syzygy/governance/doctrine, every top-level tracked .md under
.syzygy/governance/decisions, and every tracked .md under
.syzygy/governance/contracts/rfcs". Run exactly as written that is 6 + 71 +
**30** = **107 files / 1,369,266 bytes / 1,360,678 characters**, largest
63,903 characters [Observed, computed this session]. Every published figure
re-derives **exactly** under a different predicate — RFC *modules* only,
i.e. the .md files one directory below `rfcs/` — which is 6 + 71 + 28 = 105
files, 1,266,454 bytes, 1,258,724 characters, 0 over the 100,000-character
cap, largest 55,836 characters. The excluded pair is
`.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`
and
`.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`,
both accepted RFCs that happen to be single files rather than directories.
The packet's own prose ("the 28 accepted RFC modules") carries the right
count and silently drops two accepted RFCs without saying so.

**Repair.** State the predicate as the module form and add one clause naming
the two single-file RFCs as out of scope and why — or include them and
restate the six figures.

### F3 — non-blocking — the self-corpus envelope figure does not re-derive from the stated method

Packet "What a real corpus costs" table, row "One `inventory` envelope,
encoded"; evidence `measurements.self_corpus.inventory_envelope_encoded_bytes`
= 1294284.

**Defect.** The method given is "encode one real `inventory`-stage envelope
with the package's own `encodeCanonicalJson` under the limits `pipeline.ts`
line 122 constructs" over the 105 files. It omits the two free inputs the
figure depends on: what each source's `sourceId` is, and what
`readerQuestions` holds. Reproducing it four ways this session over the same
105 files, the same `promptForStage('inventory')`, the same
`stageSchema('inventory')` and the same envelope shape `pipeline.ts` line
176 constructs, I get: **1,300,688** bytes with `sourceId` = the
repository-relative path; **1,297,209** with the basename; **1,294,914**
with `source-N` ids and the demo's three reader questions; **1,294,827**
with `source-N` ids and an empty reader-question array. None equals
1,294,284. The nearest is 543 bytes away.

What does re-derive exactly: the limit probe (1,000,000 rejected with
`byte-limit`, 2,000,000 accepted) under every one of the four variants, and
the arithmetic of the ×5 floor (5 × 1,294,284 = 6,471,420). Slice 3's own
oracle already states this figure loosely ("an `inventory` envelope of about
1.29 MB"), which every variant satisfies.

**Repair.** Publish the `sourceId` scheme and the reader-question array
beside the figure in the evidence record, or restate the table row as
approximate and let slice 3's oracle carry it. Rule 3's shape: a computed
figure a later reader cannot recompute is not yet evidence.

### F4 — non-blocking — Gate 5's opening sentence is wrong about REQ-009

Packet, Gate 5, first paragraph: "003, 008, 010, 020 and 009 are not among
the seven amended, so the predecessor is cited."

**Defect.** REQ-polaris-generation-**009 is** one of the seven. The
understanding act's Scope paragraph, quoted correctly by this same packet in
Gate 0 and read at source this session at
`.syzygy/governance/decisions/POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md`
lines 29-32, reads "REQ-polaris-generation-002, 004, 006, 009, 012, 014 and
019 take their full amended clauses and preserved scenarios". The packet's
*practice* is correct — its only REQ-009 citations are at the overlay
(Gate 3 "overlay line 241 onward", Gate 5 "overlay line 243", both of which
resolve: the heading is at overlay 241 and the requirement text at 243). So
this is a false sentence about the composition rule sitting directly above a
correct application of it, which is the worse failure mode for a reader
checking the rule.

**Repair.** Strike `and 009` from that list; REQ-009 belongs with 006 and
014 in the "cited at the overlay" half of the sentence.

### F5 — non-blocking — "four envelopes, not six" reconciles with nothing else in the packet

Packet, "Figures that differ from the dossier" item 6.

**Defect.** The item reads "the `inventory` stage is *already* structurally
independent … so slice 2 is a narrowing of four envelopes, not six". Slice
2's own design sketch in Gate 4 says the opposite arithmetic in two
different ways: it lists all six envelopes and marks four of them
"unchanged", then states "**Exactly two envelopes change**: `fidelity` and
`repair` lose `plan`." And six stages minus the already-independent
`inventory` is five, not four. Three numbers — 2, 4, 5 — for one quantity,
with no statement of which population "four" is over.

**Repair.** One sentence: either name the four (if the intended population
is the stages that carry the plan today — author, edit, fidelity, repair —
say so, and reconcile it with "exactly two change"), or restate the
difference as "one of the six envelopes already has the bounded shape, and
the pattern is already in the package".

### F6 — non-blocking — Q1's load-bearing [Observed] label carries the inference the owner is being asked to make

Packet, Q1 row of the five-question table.

**Defect.** "A file inside an observed project is **none of those five**
[Observed, the clause read at source this session and its five classes
enumerated]." What was observed is RFC7-10's text and its five classes — I
confirmed both at
`.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md` lines
204-213, and the packet's Gate 5 block quote of both paragraphs (204-213 and
215-223) is verbatim with no unmarked elision. Whether a git tree entry
falls outside all five is not observed; it is precisely the reading Q1 asks
the owner to make, and the packet's own recommended arm is that it falls
**inside** the fifth. An `[Observed]` label on the negative and a
recommendation for the positive cannot both stand. Per AGENTS.md
§Epistemic discipline, an LLM assertion is Inferred.

**Repair.** Relabel `[Inferred]`, or restate the observed part exactly — the
clause names five classes and names no class for a file inside an observed
repository — and carry the conclusion as the reading it is.

### F7 — non-blocking — the collision surface is narrower than the packet's own touch-set, and it hides one live file collision

Packet, "Collision and sequencing", method paragraph and the seven-row
table; lane B's row.

**Defect.** The intersection is taken over "M7's own 24-file candidate
surface". Gate 3's topology table names **15** paths M7 would touch, and
three of them are outside that 24: `PROJECT-STATUS.md` (slice 5),
`packages/three-surface-poc-core/src/project-shape-observation.ts` (slice 4)
and `apps/three-surface-poc/src/polaris-source.ts` (slice 1). Recomputing
this session over the packet's own span predicate against a 27-file set:

- **lane B at `4090f98` modifies `PROJECT-STATUS.md` on its branch.** So the
  sentence "The intersection with M7's surface is 0 under both predicates"
  holds only under the narrower surface. (The practical risk is nil — lane
  B's hunks are at `PROJECT-STATUS.md` lines ~249-263, M7 slice 5's target
  paragraph is at lines 38-44, both read at source this session — but the
  published claim is a file-set claim.)
- **M5 at `ba9ca61` intersects at 3, not 1**, adding `polaris-source.ts` and
  `project-shape-observation.ts`. The second is the very file M7 slice 4
  says it would touch for the fourth registry ceiling, and the packet's
  prose already says M5 slice 3 and M7 slice 4 reach "the same two places" —
  so the narrative is right and only the number understates.

Everything the packet *did* publish re-derives exactly under its own stated
predicate. I recomputed all seven rows: M1 3 spans / 1 file / 1;
lane B 0; M2 19 / 11 / 1; M3 15 / 13 / 0; M4 31 / 22 / 1; M5 11 / 9 / 1;
M6 26 / 13 / **11**, with the eleven files identical to the packet's list.
The floor disclosure also re-derives: M6 cites `pipeline.ts` as a bare span
**10** times and at its full path **0** times. Lane B's stronger predicate
re-derives too: `git diff --name-only a9f671e HEAD` in its worktree names
three implementation-plane files, all under `scripts/`, intersection 0.
M1's quoted sentence begins on line 143 and ends on line 144 of
`docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`, as stated. M2 slice 3, M4
slice 5 and M5 slices 1 and 3 each carry
`apps/three-surface-poc/src/routes.ts` in their Gate 3 "Lives in" column,
as stated.

**Repair.** Take the intersection over the Gate 3 touch-set, or state the
surface's three exclusions at the site — the way the M6 floor is already
stated at its site, which is the right model.

### F8 — non-blocking — "disjoint from M7 by design" is unlabeled and is now false

Packet, "Collision and sequencing", the M8/M9 paragraph.

**Defect.** "**Two other P2 packets are being drafted in parallel and their
content is [Unknown] to this session** … Both worktrees are at `a9f671e`
with no commits, so no intersection can be computed against them. **They are
disjoint from M7 by design** …". The first clause is honestly labeled; the
bolded conclusion is an unlabeled substantive claim, and it is now
measurable. M8 has committed `8035c8f` and M9 `206d775`. Recomputed this
session at those heads under the packet's own predicate:

- **M8 intersects M7's 24 at 4**: `apps/three-surface-poc/src/routes.ts`,
  `docs/polaris-generation/README.md`,
  `docs/polaris-generation/ARTIFACTS-AND-TOOLS.md` and `package.json`. Two
  of those four are M7 slice 5's own files. Under the 27-file set it is 6,
  adding `polaris-source.ts` and `project-shape-observation.ts`.
- **M9 intersects at 2**: `apps/three-surface-poc/src/routes.ts` and
  `package.json` — so the count of packets proposing to edit that one
  240-line file is six, not four.

The packet's `could_not_verify` entry ("[Unknown] which arm … whether M8 or
M9 will claim any file in M7's 24") covers this honestly; the prose sentence
does not, and a later reader will read the sentence, not the record.

**Repair.** Strike "They are disjoint from M7 by design" or relabel it
`[Inferred]` with the subject-level reasoning only, and — since the heads now
exist — add the two recomputed rows.

### F9 — non-blocking — slice 5's five fields are not "taken field for field from SEC-2's own sentence" (rule 8)

Packet, "Slice 5 — Name the act…", first paragraph.

**Defect.** SEC-2, read at source at
`.syzygy/governance/doctrine/security.md` lines 25-37 this session, names
**two** of the five: the **providers** permitted for a governed project and
the **content classes** that may be sent ("Onboarding consent must name the
providers permitted for a governed project and the content classes that may
be sent"). The **route**, the **retention** and the **refusal behaviour on
withdrawal** are not in SEC-2. The third is REQ-001's, which the packet does
cite separately and correctly (base line 12, quoted exactly). The first two
have no cited anchor anywhere. "Field for field from SEC-2's own sentence"
is therefore a contract claim wider than the clause it is anchored to, which
is the failure rule 8 names. The SEC-2 block quote itself is exact,
including the source's own emphasis, with no added emphasis.

**Repair.** Attribute each field to the clause that carries it — two to
SEC-2, one to REQ-001, and the route and retention as this packet's own
proposal, labeled as such.

### F10 — editorial — five anchor and quotation imprecisions

Each is harmless to the argument; each is a citation a reader cannot land
on, and this corpus's standard is that a citation lands.

1. `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
   line **53** carries `"class": "git-tree-entry"`; the `identityScheme` the
   packet quotes is on line **54**. Cited as 53 in Q1 and in Gate 3 slice 1.
   (The literal sweep behind it is exact: `git-tree-entry` occurs **1** time
   across the **619** tracked files under `.syzygy/` and `openspec/`
   [Observed, recomputed this session], and both named acts carry that path
   as "Artifact identity" at line 13 of each.)
2. `openspec/changes/polaris-manifesto-generation/EXECUTION-PHASES.md`'s
   sentence "It does not create or mutate live scheduler items, call a real
   provider, serve owner effect controls, or read another project" **begins
   on line 13**; only its second half is on line 14. Cited twice as line 14.
3. `apps/three-surface-poc/src/routes.ts`: `boundedResponse` is declared at
   line **138** under its comment at 137 and closes at **143**; the packet's
   "lines 137–142" ends one line short.
4. `apps/three-surface-poc/src/polaris-generation/draft-preview.ts` line 23
   is quoted as ``<a href="#source-${index}" aria-label="Read source ${index
   + 1}">`` — the trailing ``[${index + 1}]</a>`` is dropped with no
   ellipsis. The claim it supports is exact.
5. REQ-008's sentence begins "**An** uncertain attempt SHALL continue to
   reserve its maximum charge…" at base line 400; the packet lowercases the
   `A` to embed it mid-sentence without marking the alteration. (A
   full-sentence sweep for the packet's spelling returns 0 hits in both
   specification files, which is how I found it — worth noting because it is
   exactly the false-absence shape AGENTS.md warns about.)

### F11 — editorial — one code span reads as a file path and does not resolve

Packet, "Slice 5 … This packet names the act and does not draft it":
`decisions/README.md`. It resolves only as
`.syzygy/governance/decisions/README.md`. The evidence record lists it among
the 35 non-resolving slash-bearing spans, but the record's own note on that
list — "none is a file path this packet cites" — is false for this one
entry. (I re-ran the span sweep: 264 distinct spans, and the two over-width
non-fence lines the record names, **205** and **889**, are the two I get
under the record's own predicate. Backtick parity: **0** odd-count non-fence
lines, confirmed independently.)

**Repair.** Write the full path, and drop that entry from the note's scope.

### F12 — editorial — slice 5's tasks.md §3 partition omits 3.4a

Packet, "Slice 5 … **What it buys** … **What it does not buy:** 3.1, 3.2 and
3.5". Stated as exhaustive ("Exactly the obligations in `tasks.md` §3 …"
plus a complement). `openspec/changes/polaris-manifesto-generation/tasks.md`
§3 has **seven** boxes: 3.1, 3.2, 3.3, 3.4, **3.4a** (line 49), 3.5, 3.6
[Observed, enumerated this session]. 3.4a — "Apply DESIGN-ACCEPTANCE.md to
the full rendered reading, including the owner's reported failures" — is an
actual-generated-artifact obligation and belongs on the buys side.

**Repair.** Name 3.4a in the buys list, or say the partition is over the six
numbered boxes and 3.4a rides 3.4.

---

## The five questions

| # | Scope truthful? | Genuine hard human gate? | Recommendation follows from the evidence? | Every lawful arm named? |
|---|---|---|---|---|
| Q1 `git-tree-entry` vs RFC7-10's five classes | Yes. The clause, the registry entry and both binding acts are exactly where and as the packet says; neither artifact may be edited | **Yes.** Reading a sixth target kind into a list RFC7-10 closes with "No target class exists for narrative content, renderings, or editorial drafts" is an accepted-contract reading, and VIS-4's first sentence names RFC acceptance shape-defining (vision.md 122-124, read at source). Not ordinary engineering | Yes, and the counter-argument is stated at full strength rather than smoothed — the packet says in terms that the fifth class "reads naturally as *Syzygy's own* evidence artifacts". No consensus language | **Three named, one missing.** A fourth lawful arm is unnamed: rule the clause **not engaged** — that REQ-003's "source anchors" are the bundle's anchors into governed artifacts and a provider-side source record is not an anchor in RFC7's sense. The packet gestures at it ("leaves the specification's own anchor obligation open") without offering it as an arm. Also: Q1's default is the only one of the five that **ships** rather than holds; that is a defensible trade-off but it is the least conservative default in the packet and is not flagged as such |
| Q2 self-corpus read | Yes. The reservation sentence is verbatim at the act's line 42; the corpus figures re-derive (F2's predicate caveat aside) | **Yes, but the weakest of the five.** The packet's own argument for arm 1 is strong and it concedes "the sentence above can be read the other way". A recorded ruling is cheap and the ambiguity is real, so it clears the bar — but a reader could fairly call this engineering that wants cover | Yes. The counter-argument ("building the pipe before the egress act exists") is the real one and is given its weight | Yes — rule it a self-read, or a narrow direction in the named shape; declining is folded into the default, which is "slice 3 does not ship" |
| Q3 draft route category | Yes. P-72's Q1 is quoted exactly from M5's packet at `ba9ca61`, including "retroactively"/"prospectively"; the membership test genuinely fails (0 references to the observation plane) | **Yes**, though it is a question *about* a question already before the owner rather than a new gate. The packet says so and recommends folding rather than opening a third framing, which is the right instinct | Yes | Yes for the two it numbers, plus the honest disclosure that P-72's arm (c) has **no** corresponding arm here. A separate later delta is named in prose but not numbered as an arm |
| Q4 drafted act | Yes. P-71's Q3 arms are reported as they stand on `63b8e33`, and the subject distinction (Syzygy's own narrative vs a finding about the observed project) is real | **Weakest as a gate.** The recommended arm is P-71's arm (b), which the packet itself says "needs no act on anyone's reading" — so the recommended path dissolves the question. The gate is real only on the file-writing limb, which the packet routes back to P-71 | Yes, and the counter-argument (a packet the owner must copy out of a JSON body is worse for the owner; "satisfies the letter and strains the intent") is not smoothed | Yes: arm (b) now, wait for P-71, or the file-writing limb under P-71's arm (a) |
| Q5 admit port reserve/complete | Yes. The comment at `packages/polaris-generation-core/src/pipeline.ts` lines 60-64, the declaration at 65, the test pin at `pipeline.test.ts` 73-76 and REQ-008's scenario at base 407-411 are all exactly as described, and the mismatch is genuine — a port that refuses a completed identity cannot satisfy "resume reuses those stages" | **Yes.** A reviewed safety property at the one boundary where a mistake spends real provider effects, and VIS-4's always-human-gated class reaches normative data contracts | Yes, with the retained-prohibition condition carried into the recommendation rather than left to the implementation | Yes: rule it an implementation with the condition, or a caller-side cache outside the port with the mismatch recorded. Default is the second — conservative |

**No lawful arm is called unlawful anywhere.** **No owner trade-off is
smoothed into consensus language** — every question carries its
counter-argument at strength, and Q1's, Q2's and Q5's counter-arguments are
the strongest sentences in their rows. **Every question states a
default-if-unanswered**, and four of the five default to not shipping; Q1's
is the exception noted above. **No P-73 question is re-asked**: P-73's six
questions, read at source on `83c9f60`, are the disposition field, the
support discriminant, the fail-closed fidelity verdict, the kit example
file, the onramp and the act/RFC2-26 question — none of them is any of
Q1-Q5. **P-71's Q3 and P-72's Q1-Q2 are reported, not re-asked**, and the
long definition the packet quotes from M5's Q1 occurs exactly once in M5's
packet, verbatim.

---

## Measurements re-derived

Every row was recomputed this session in the worktree, against the stated
predicate, by driving the built modules or by exact substring counting.

| Claim | Re-derives? | My figure |
|---|---|---|
| Per-stage `inputBytes`: inventory 3,422 / plan 4,297 / author 7,971 / edit 8,807 / fidelity 6,283, total 30,780 | Yes, exactly | identical, via a capturing `admit` port over the shipped garden fixture |
| Corpus 439 bytes as `JSON.stringify` encodes it; 70.1× | Yes, exactly | 439; 70.11 |
| Marginal slope 439→30,780, 3,439→65,780, 6,439→100,780; 11.67 bytes billed per source byte | Yes, exactly | identical; slope 70,000/6,000 = 11.667 |
| Envelope `inputs` keys per stage (inventory 2, plan 3, author 4, edit 5, fidelity 5) | Yes, exactly | identical |
| Sentinel occurrences 1 / 2 / 2 / 4 / 4, total 13 | Yes, exactly — but only with the sentinel in the **mechanism** source | with the sentinel in `purpose` I get 1/2/2/3/3, total 11. The method statement does not say which source carries it; worth one clause in the evidence record |
| System prompts 1,971 / 2,371 / 2,459 / 1,968 / 2,515 (+repair 1,847); five-stage total 11,284 | Yes, exactly | identical |
| Six schemas 14,155 bytes; author/edit/repair share one 3,961-byte object | Yes, exactly | identical |
| Prompt transmitted twice, billed once | **Yes** — `pipeline.ts` 176 puts `system: prompt.system` in the envelope, 219 passes `system: prompt.system` to `ports.generate` alongside `input: encoded`, and 177-179 charge `Buffer.byteLength(encoded)` only | confirmed at source; L3-F7's "billed twice per call" is the error the packet names |
| Self-corpus 105 files / 1,266,454 bytes / 1,258,724 chars / 0 over cap / largest 55,836 | Yes, exactly — under the module predicate, not the record's stated one | identical; see F2 |
| Inventory envelope 1,294,284 bytes | **No** | 1,300,688 / 1,297,209 / 1,294,914 / 1,294,827 across four readings of the stated method; see F3 |
| 1,000,000 rejected `byte-limit`, 2,000,000 accepted | Yes | identical under all four variants |
| `list()` default `maxItems` 200 at `provider-draft.ts` 15; source schema at 109 takes it | Yes, exactly, and the schema line is quoted verbatim | identical |
| Butlers 278 sources, 86 bodies, 1,120,065 bytes; 78 over the 200-item cap | Yes, exactly, from the retained machine capture in the lane A session scratchpad (never from the observed checkout) | `projectShape.counts.sources` 278, `resourceUse.bodiesCounted` 86, `resourceUse.totalBytes` 1,120,065; 278 − 200 = 78 |
| `routes.ts`: 240 lines, 15 entries, 15 distinct paths, 11 human-open, 4 machine-credentialed = 2 logical routes twice | Yes, exactly | counted from the return array at lines 206-239 |
| `generation` and `draft` occur 0 times, case-insensitive, whole file | Yes | 0 and 0 over the 240-line file |
| `routes.ts` 21-22 are the presentation-path constants, not the route table | Yes | `POLARIS_PRESENTATION_PATH` on 21, `POLARIS_PRESENTATION_KIND` on 22 |
| `tasks.md` 24 boxes under `^- \[[ xX]\] `, 0 checked, 51-line file | Yes, exactly | identical; the five quoted task lines (22, 23, 24, 31, 47) are verbatim |
| Ten-sentence clause-origin sweep (REQ-003 1×/0×, REQ-006 1×/1×, REQ-014 1×/1×, REQ-010 1×/0×, REQ-020 1×/0×, REQ-008 1×/0×) | Yes, exactly, all ten | identical, at the stated lines |
| `f4589e2..a9f671e` over the M7 paths: 22 rows, 20 A, 2 M, `routes.ts` in no row | Yes, exactly | identical; the two M rows are `docs/polaris-generation/README.md` and `package.json` |
| `1932f74..a9f671e` over the same paths: 0 rows | Yes | 0 |
| 15 Gate 3 paths vs every `*-MANIFEST.txt`, every `docs/evidence/*manifest*.json` and the acceptance record: 0 hits each, 21-file manifest population | Yes, exactly | 14 + 7 = 21 manifests plus the acceptance record; 0 hits for all 15. I also swept the 214 retained raws and the foundational acceptance record for act arguments naming those paths — the only hit is a stale-marking sentence, not an argument, so the conclusion holds under the wider sweep too |
| Generator scope record: 21 rows, all under the package directory, 0 implementation paths; banner "unadopted…" and `implementedGenerator` false | Yes, exactly | identical |
| Synthetic verification record: 17 rows, all 17 equal current bytes | Yes, exactly | 17 matching, 0 mismatching, recomputed; the 17 are exactly the 11 + 6 files of the two source directories |
| `git-tree-entry` occurs 1× across the two governed trees | Yes | 1 hit over 619 tracked files |
| Collision: M1 1, lane B 0, M2 1, M3 0, M4 1, M5 1, M6 11; M6 cites `pipeline.ts` 10× bare / 0× full path | Yes, exactly, all seven rows and both span counts | identical — see F7 for the surface-definition caveat and F8 for M8/M9 |
| Registers: six siblings one row each at P-68…P-73; this worktree, M8's and M9's end at P-53 | Yes, exactly | 27 `^| P-` rows in each sibling, 26 in each of the three; `a9f671e`'s register has 26 |
| Packet: 109,383 bytes, 1,312 lines, 0 odd-backtick non-fence lines, over-width lines 205 and 889 | Yes, exactly | identical |
| `check_governance.py` ends `0 FAIL` | Yes | "32 OK, 20 WARN, 0 FAIL (52 checks)" — tail line read in full |

### Contract and specification citations opened at source

All exact unless F4/F9/F10 says otherwise. RFC7-10 at
`.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md` 204-213
plus its target-state paragraph at 215-223, both quoted whole with no
unmarked elision, and `DIRECTIVE-REGISTER.md` line 388 does name it at
`:204`. RFC7-21 at the same file 398-406, with a marked ellipsis. RFC2-26 at
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`
196-221 under the `###` heading at 194, both paragraphs verbatim, and its
package-scope sentence does sit at 219-220. VIS-1 at
`.syzygy/governance/doctrine/vision.md` 82 onward; VIS-2 at 96-106 with a
marked ellipsis; VIS-4 at 122-139; VIS-5 at 141-162 with "materialization is
exclusively a worker action against scheduled work" at 158-159. SEC-2 at
`.syzygy/governance/doctrine/security.md` 25-37. The implementation act's
reservation at line 42 and the understanding act's lines 39-41 are verbatim.
Base spec: REQ-003 at 96/98/100 with scenarios at 105-109 and 111-115;
REQ-006 at 300/302; REQ-008 at 398/400 with scenarios at 407-411 and
413-417; REQ-010 at 526/528 with scenarios at 535-539 and 541-545; REQ-014
at 753/755; REQ-020 at 1081/1083 with its scenario at 1089-1093; REQ-001's
withdrawal sentence at 12. Overlay: REQ-006 at 180 with **exactly five**
scenarios at 187, 193, 199, 205 and 214 — I read all five, and the packet's
absence claim is right: none states the envelope-contents case; REQ-009 at
241/243 with "Changed source" at 250-254; REQ-014 at 367 with "Narrow
evidence offered as completion" at 380-384, "Unfamiliarity without
project-specific patching" at 392-399 and "Shared model blind spot" at
409-414. The composition rule in AGENTS.md is honoured in practice
throughout; only F4's sentence misstates it.

### Gate 5 (RFC2-26), independently

Denominator 7 confirmed against Gate 3's seven slice rows. Slices 1, 3, 4
and 6 do map to named requirement-and-scenario pairs at the cited lines,
each of which I opened. Slice 2's absence claim survives its own sweep with
its denominator stated (five REQ-006 scenarios, all five enumerated). One
note rather than a finding: scenario 199's AND — "an author-generated
outline or claim list cannot replace the independent source inventory" — is
closer to slice 2's subject than "nearest scenario" suggests, since the plan
*is* an author-generated outline; the packet does cite 199 and 205 as the
nearest, so the reader is routed correctly either way.

### The dossier

Not edited — the branch adds two files and touches nothing else. All six
"figures that differ" are real, checked against line 307 of
`docs/pursuits/2026-09-13-vision-pursuit.md`, its M7 Evidence bullet, L3-F5,
L3-F7, L3-M6 and L3-M8 in the harvest: L3-F7 does say "the prompt is billed
twice per call" and does frame the 200 cap as "more than 200 admitted
bodies"; L3-F5's evidence does list both `routes.ts:21-22` and
`routes.ts:220`; the dossier's slice 2 does say "fidelity envelope built
from the draft alone"; L3-M6 does say "publish the resulting draft preview
as the second project"; and the inventory-already-independent point is
absent from all of them. The dossier's `prerequisite` value is exactly
"none; owner act for egress" and `syzygy_audited_at` is exactly `f4589e2`,
and the packet's two corrections to that line are both earned. The
prerequisite line is fairly tested.

---

## Summary

- blocking: **0**
- non-blocking: **9** (F1-F9)
- editorial: **3** (F10-F12)

The packet's measurement work is unusually strong: of the thirty-odd figures
I recomputed, one does not re-derive (F3), two re-derive only under a
predicate other than the one published (F1, F2), and the rest are exact
including every line anchor, every file-set intersection and both
load-bearing zeros. Its contract citations land at the clause, its
counter-arguments are not smoothed, and its defaults are conservative. The
exceptions above are predicate and labeling repairs, one false sentence
about the amendment list (F4), one internal arithmetic inconsistency (F5),
and two collision figures that are correct under a surface narrower than the
packet's own touch-set (F7, F8).

Verdict: CONFIRM WITH EXCEPTIONS
