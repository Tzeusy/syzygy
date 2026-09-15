# R-POLARIS-M8-PORTABILITY-FUNNEL — review 1 (raw, retained verbatim)

Independent fresh-context review. Read-only. No tracked file was edited in
any worktree; `git status --short` in the review worktree is empty at the
end of this session, and `git diff a9f671e...HEAD --name-only` names only
the two reviewed files.

## Subject and bytes

Worktree: branch `agent/syzygy-dov.8`, HEAD
`8035c8fa6cb18b59369719c3f16d853e05e1e812`
("docs: Polaris M8 portability funnel packet, first draft [syzygy-dov.8]").
Packet baseline `a9f671e`. Digests computed with `sha256sum`, sizes with
`wc -c`; neither value is transcribed.

| File | Bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md` | 110515 | `62ee454380619164b23e9e5bb896da5c1eb9f1cc6717c7c70b4d02c12ca15782` |
| `docs/evidence/polaris-m8-portability-funnel-2026-09-15.json` | 42655 | `49b6f4dcbc4382645c4ca198bbc26af1fa530c45dbe042dd51228f4fe15e19d8` |

Sibling worktree HEADs read this session, read-only:
lane B `4090f98`, M2 `f2f37dd`, M3 `6574600`, M4 `63b8e33`, M5 `ba9ca61`,
M6 `83c9f60`, M7 `0c4b4a9`, M9 `206d775`. All eight match the packet's
recorded heads where the packet records one.

`python3 scripts/check_governance.py` in the worktree ends
`32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted`
(tail line read, not grepped). [Observed]

## Summary

This is an unusually well-measured packet. Every load-bearing count in
"Measurements at `a9f671e`" re-derived exactly under the stated predicate:
74 of 133, 37/37 against 64/69, 139/74 recursive with the six named extras,
the NUL byte at offset 13,811 on line 305, 4 of 191 copy rows at lines 26,
60, 62 and 235 with the 83/77/19/12 role partition, 18 modules / 51 lines,
2 non-test registry readers against 3 test files, 4/6 builder users, the
14,604-byte registry entry with its six `observationGrammar` keys, the
0-occurrence specification sweep with 37/29/2, 17 and 24 requirements,
31 and 24 scenarios, and all six computed sibling intersections
(1/7/6/9/5/2). The digest comparisons hold. No act-bound byte is proposed
for edit outside the mechanism its binding act names, no observed-repository
path is backticked, and no manifest or truncated signed digest is
reproduced.

The findings below are citation-anchor defects, one measurement whose cause
is misattributed, two self-descriptions whose stated predicate does not
re-derive, and one collision denominator that omits the two largest
unmeasured intersections. None falsifies a conclusion or a recommendation.
No blocking finding.

## Findings

### F1 — non-blocking — RFC1-2 is cited at the wrong lines, twice
`docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md:37` (Q4) and `:520` (Gate 2).

**Defect.** Both cite RFC1-2's sentence "Repository identity is a declared
identity in the project declaration, never a remote URL or path — URLs and
default branches change; identity must not" at
`.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`
**lines 27–28**. At `a9f671e` lines 27–28 are
the line reading "SDR §5 questions 1–3." and the "Rationale, amendment
history, and rejected alternatives" line — unrelated front matter, in the
RFC's own header block. RFC1-2 opens at
line 121 and the quoted sentence spans lines **126–128**, beginning at
"Repository" on 126 [Observed, opened at source]. The identifier and the
quoted words are exact; only the anchor is wrong, by ninety-nine lines.
This is the clause Q4's recommended arm rests on and the clause Gate 2
substitutes for the dossier's SEC-1 tag, so a reader checking either follows
the citation to boilerplate.

**Repair.** Cite lines 126–128 in both places.

### F2 — non-blocking — three further anchors miss the packet's own convention
The packet fixes its convention at lines 18–23: "the cited line is the one
the quoted words **begin** on".

- `:641` (Gate 3, slice 5): the escalation trigger "a change to the
  constraints or envelope the registry entry declares" is cited at
  `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` lines 92–93. The words begin on
  line **91** ("…policy; a change to the") and end on 92.
- `:636` (Gate 3, slice 2): "any scope beyond the signed change" is cited at
  line 94. The words begin on line **93** ("or any scope beyond the signed")
  and end on 94.
- `:544` (Gate 2): RFC1-10 is cited at lines 263–266; the quoted sentence
  spans **263–265**, and 266 belongs to the next sentence.

All three quotations are otherwise verbatim [Observed, opened at source].

**Repair.** 91–92, 93–94, 263–265.

### F3 — non-blocking — a systematic +1 in three stated line denominators
`:98` (Gate 0), `:963` and `:970` (Gate 5), `:1261` (Gate 6 item 10).

**Defect.** The packet reports the PWB specification at **1,153** lines and
the Three-Surface POC specification at **1,009**, and its own non-fence
population at **1,344**. Measured at `a9f671e`: the two files carry 1,152
and 1,008 physical lines (both newline-terminated; `wc -l` 1152/1008, and
`len(bytes.split(b"\n"))` 1153/1009), and the packet has 1,358 physical
lines of which **1,343** are outside fences [Observed, both methods run
this session]. The cause is uniform — `len(text.split('\n'))` counts a
phantom trailing element on a newline-terminated file. The packet's own
stated convention at line 23 is "counts of physical lines", which these
three are not. No sweep result changes: the 0-occurrence specification
sweep, the 37/29/2 counts and the "0 odd-backtick lines" result all
re-derive exactly under either denominator.

**Repair.** 1,152 / 1,008 / 1,343, or state the counting rule.

### F4 — non-blocking — "deterministic input" does not occur at line 76
`:1041` (Gate 5, slice 5 row).

**Defect.** The packet writes: the phrase "deterministic input" occurs "at
lines 76, 85 and 95, all inside the requirement's own prose and its
falsifier, never inside a scenario". `grep -F "deterministic input"` over
the PWB specification returns **two** lines, 85 and 95. Line 76 reads
"observer/parser version as deterministic **evaluation** inputs" — a
different phrase [Observed, run this session]. The conclusion the sentence
draws (the phrase never appears inside a scenario) survives under either
reading, and PWB-REQ-001's single scenario is confirmed at lines 98–102.

**Repair.** "occurs twice, at lines 85 and 95; line 76 carries the variant
'deterministic evaluation inputs'".

### F5 — non-blocking — the 73-vs-74 divergence is attributed to the wrong cause
`:214`–`:222` ("Second method, and it disagrees by one").

**Defect.** The packet says "ugrep classifies the file as binary, and `-l`
silently omits it". Run directly, ugrep does **not** omit it: over
`packages/three-surface-poc-core/src/project-shape-coverage.test.ts` alone,
`ugrep -il butler` exits 0 and prints the path, and `ugrep -ic` prints 44
[Observed, ugrep 7.8.4, invoked directly this session]. The omission comes
from the `-I` (ignore-binary-files) flag this environment's `grep` wrapper
injects ahead of every invocation; with an explicit 133-path argument list
passed to system `grep`, the count is **74**, not 73. Both figures are real
and the packet's headline (74 of 133) is the correct one; but a later reader
who reproduces "the second method" with bare ugrep gets 74 and cannot see
where 73 came from, which is exactly the reproducibility this section
exists to buy. The practical instruction — pass `-a` or use Python — is
unaffected, since `-a` overrides `-I`.

**Repair.** Attribute the omission to the wrapper's `-I`, and record the
exact invocation that produced 73.

### F6 — non-blocking — "asserts the two section headings" overstates line 267
`:383` ("The tests that assert the current identity").

**Defect.** "**1** asserts the two section headings
(`apps/three-surface-poc/src/polaris-copy.test.ts` line 267)". Line 267
asserts one heading string, `What Butlers is`, inside a clean-fragment
expectation. The proving case's name occurs exactly **once** in that file,
on line 267; `How Butlers is built` occurs nowhere in it [Observed, whole
file swept this session]. The slice-2 cost this paragraph measures is
therefore one assertion over one heading, not two.

**Repair.** "1 asserts one of the two section headings (line 267)".

### F7 — non-blocking — the 31-file surface's stated predicate does not re-derive
`:1129` (collision method) and Gate 3's topology table at `:565`–`:573`.

**Defect.** The packet defines its surface as "every existing file named in
Gate 3's topology table", size **31**. Gate 3's table names **23** distinct
existing files; it gives the rest only as counts — "and four test files"
(slice 2), "and two test files" (slice 3), "and their tests" (slice 7). The
evidence record's `m8_surface` supplies the eight missing names
(`polaris-first-reading.test.ts`, `polaris-project-shape.test.ts`,
`walkthrough-preflight.test.ts`, `git-observation.test.ts`,
`body-read-authority.test.ts`, `model.test.ts`,
`project-shape-manifest.test.ts`, `project-shape-observation.test.ts`),
which no reader of the packet alone can derive [Observed, both enumerated
this session; all 31 resolve as files, confirming the packet's
"every one of the 31 resolves"]. Separately, the evidence record's
`m8_by_slice` assigns `packages/three-surface-poc-core/src/project-shape-model.ts`
to **S6**, while Gate 3's slice 6 row says "**none edited**" and Gate 4's
slice 6 says "No existing source module changes."

**Repair.** Either name the eight test files in Gate 3 or state the
predicate as "Gate 3's table plus the tests the evidence record enumerates";
and reconcile S6's claim on `project-shape-model.ts` with Gate 3 and Gate 4.

### F8 — non-blocking — the collision denominator omits the two largest intersections
`:1153` ("M8 is the collision-heavy packet in this set") and `:1196`
("The two other P2 packets drafted in parallel — M7 and M9").

**Defect.** The packet computes its intersection against six siblings and
declares "M8 intersects five of the six" and "M8 is the collision-heavy
packet in this set". M7 and M9 are recorded as **[Unknown]** — "neither was
read, and neither worktree was opened" — which is an honest statement of
what the packet did, not a false claim. But both worktrees exist and are
readable, so the headline rests on six of eight siblings. Recomputed here
with the packet's own predicate and its own 31-file surface:

- M7 (`0c4b4a9`): 31 implementation-plane spans, 29 resolve to a path, 21 to
  a file, intersection **7** — `git-observation.ts`, `polaris-source.ts`,
  `routes.ts`, `docs/polaris-generation/ARTIFACTS-AND-TOOLS.md`,
  `docs/polaris-generation/README.md`, `project-shape-model.ts`,
  `project-shape-observation.ts`.
- M9 (`206d775`): 21 spans, 19 / 12, intersection **6** — `polaris-copy.ts`,
  `polaris.ts`, `routes.ts`, `trajectory.ts`, `model.ts`,
  `project-shape-model.ts`.

M7's 7 exceeds every measured sibling but M4's 9 [Observed, computed this
session at those heads]. The packet's dossier-derived inference about M7 —
"the first is disjoint from every M8 slice but 4, and `routes.ts` is in
slice 2's surface" — is falsified by the actual packet, which also spans
slice 3's and slice 5's files. Its inference about M9 is confirmed in
direction (M9 does collide with slice 2 and slice 7) but not in file set:
M9's packet does not code-span `orrery.ts`, which the dossier entry cites.
The packet's recommendation that M8 land last and that "M8 and M9 need
explicit sequencing" is strengthened, not weakened, by the recomputation.

**Repair.** Compute the two rows, or restate the headline with its
six-of-eight denominator.

### F9 — non-blocking — the retained capture is unreachable and escapes the packet's own resolution predicate
`:333` ("The rendered page, from the retained capture").

**Defect.** Two measurements — the 96 occurrences of the exact proper noun,
and the verbatim `h1` element quoted at `:338` — have a single source,
`polaris-7478.html`. That file exists nowhere in the worktree and is not
tracked; the evidence record places it at `scratchpad/capture/…`, outside
the repository [Observed, `git ls-files` and a whole-tree walk this session:
0 matches]. Neither measurement is checkable by this or any later reviewer,
and both are labeled `[Observed]`. Compounding it, Gate 6 item 10's
resolution accounting is scoped to code spans that "contain a `/`" — so of
the 29 filename-shaped spans carrying no slash, `polaris-7478.html` is the
only one that matches nothing in the tree, and the packet's own predicate
structurally cannot see it. The packet does disclose the capture's
provenance, its earlier revision, and that every source row cited against it
was re-read at `a9f671e` (which I confirmed for the copy rows and the
`DEFAULT_CLAIM_ROLE` map).

**Repair.** Either retain the capture under `docs/evidence/`, or relabel the
two capture-only figures `[Unknown]` to a reader without it; and widen item
10's predicate to all filename-shaped spans.

### F10 — non-blocking — the default-if-unanswered set contradicts itself on slice 3
`:33` (Q1), `:37` (Q4), `:1298` (Recommended handoff).

**Defect.** Q1's default is "slices 1, 4 and 6's design work proceed to
review; nothing lands" — slice 3 is not named. Q4's default is "**the
recommended arm**", whose recommended arm has slice 3 read the locator from
the consent record, i.e. proceed. The handoff line says "land slice 3 first
(smallest, no act, no rendered claim)". An owner who answers nothing is
given three different statuses for slice 3: unmentioned, proceeding, and
first to land. Q1's recommended arm does include slice 3 in the ride-the-act
set, so the intent is legible; the defaults are not consistent.

**Repair.** State slice 3's status explicitly in Q1's default.

### F11 — non-blocking — Gate 0 names two doctrine constraints the packet never applies
`:95` (Gate 0 doctrine row).

**Defect.** The doctrine row lists "VIS-1, VIS-2, VIS-4, VIS-5, VIS-7;
SEC-1 …, SEC-5" as constraining this request. Gate 2 quotes VIS-1, VIS-2,
VIS-5, VIS-7 and SEC-1 at their clauses and engages each per slice. **VIS-4**
and **SEC-5** are never quoted, never applied and never discharged anywhere
in the packet [Observed, whole-file sweep this session: `VIS-4` occurs twice,
both in Gate 0's table and the hard-prohibition restatement; `SEC-5` occurs
three times, all in enumerations, none at a clause]. VIS-4 is live here —
Q2 and Q3 ask the owner to perform four acts — and SEC-5 is live for slice 6,
which proposes running the secret detectors over this repository's own tree.

**Repair.** Quote and apply both in Gate 2, or drop them from Gate 0's row.

### F12 — editorial — six rows called five
`:1296`. "the five siblings' existing rows are P-68 lane B, P-69 M2,
P-70 M3, P-71 M4, P-72 M5 and P-73 M6" enumerates six. The six assignments
are exact: each sibling branch adds exactly that one `^| P-` row against
`a9f671e` and no other [Observed, diffed in all six worktrees this session].
The register at `a9f671e` carries 26 `^| P-` rows (21 open, 5 acted) and
tops at P-53, so none of P-68…P-73 exists on main — as the packet says.

### F13 — editorial — "one or two each" is wrong for one of the thirteen
`:288`. Of the 13 modules holding the remaining 19 of the 51 non-comment
lines, `apps/three-surface-poc/src/test-project-shape-fixture.ts` carries
**3** (lines 19, 28, 54) [Observed].

### F14 — editorial — the mutation record has seven keys, not five
`:398`. `docs/evidence/polaris-manifesto-example-mutation-2026-09-09.json`
carries `commit`, `file`, `old`, `new`, `exitCode`, `output`, `restored`.
The packet reads five of them and then quotes `restored` in the same
sentence. Every substantive claim about the record verifies: `exitCode` 1,
`restored` true, **no** `sha256` field, and the guarded fragment
`renderPolarisMarkdown(example.statement as string)` present exactly once in
`apps/three-surface-poc/src/polaris.ts` [Observed].

### F15 — editorial — three quotation-fidelity slips
- `:37` (Q4) renders PWB-REQ-005's total row as "no 'other invalid' bucket"
  with straight quotes; line 248 uses curly quotes.
- `:37` (Q5) ends the REQ-014 anchor-set quotation at "contains no unused
  anchors"; the sentence continues "and is small enough for a reader to
  identify which anchor supports which claim" (lines 767–768), with no
  ellipsis marking the stop.
- `:1049` ends POC-REQ-050's normative sentence at "declared
  capability-to-path mappings"; the source continues ", with a deterministic
  layout per observation" (lines 779–780), likewise unmarked.
None changes the sense. By contrast the VIS-1, VIS-2, VIS-7, SEC-1 and
RFC2-26 quotations mark every elision with `…` and are verbatim, and
RFC2-26 is reproduced whole, both paragraphs, with no elision, as claimed.

### F16 — editorial — one of the fourteen `polaris.ts` lines is never accounted for
`:280` calls all 14 "renderer-built sentences"; the difference table at
`:451` enumerates 6 remediation sentences (419, 423, 425, 427, 432, 441) and
7 pillar routes (671–683 odd) — thirteen. Line **583** is the fourteenth and
is named nowhere. Slice 2's design says "the fourteen renderer-built
sentences", so the count is used; the reader cannot tell what the
fourteenth is.

## Owner-question table

| # | Scope truthful? | Genuine hard gate? | Recommendation follows? | All lawful arms named? |
|---|---|---|---|---|
| Q1 | Yes. The 0-occurrence sweep, the 37/29/2 counts, PWB-REQ-001 line 73 and the reader note at lines 23–24 all re-derive exactly | **Yes.** Whether portability rides the existing act or needs a CC-REV-2 amendment is an authority question no clause settles | Yes, and the packet marks the split as a reading `[Inferred]` rather than a rule | Three arms, plus a default. The counter-argument is stated as "strong" and argues against the recommendation — not smoothed |
| Q2 | Yes. 14,604 bytes, one entry, six grammar keys, the digest match and the act's lines 76–77 and 88–90 all verify verbatim | **Yes.** The act's own closing sentence makes any edit a new act; enlarging what a digest binds is an owner cost | Yes. The limb split (only limb 5 needs the act) is supported by the five-limb design | Two arms, plus a default. The counter-argument (a recurring forever-cost, on a grammar still moving) is real and preserved |
| Q3 | Yes. Confirmed independently: over 84 governance files (`declarations/**`, `decisions/*.md`, `policies/**`) the only `repository:` identifier anywhere is `repository:butlers-configured-poc`, and **0** files name `repository:syzygy`; exactly one adapter-registry entry exists | **Yes.** Three ceremonies and an unqualified RFC1-3 sentence | Yes, and the packet does not run the slice | Two arms. The packet explicitly declines to call the second lawful **or** unlawful and says why — the correct posture, not a hedge |
| Q4 | Mostly. Consent line 15/17–18, and PWB-REQ-005 lines 231/245/248 all verify. The RFC1-2 anchor is wrong (F1) | **Borderline.** By the packet's own reasoning the recommended arm needs no act and changes no refusal semantics, and its default is "the recommended arm" — i.e. it proceeds unanswered. What makes it owner material is the second arm, which contradicts an act-bound "exactly 195", and the security-surface trade-off the counter-argument states | Yes | Two arms, plus a default. The counter-argument is the stronger security reading and is not softened |
| Q5 | Yes. `DEFAULT_CLAIM_ROLE` at lines 260–265 and the comment at 257–259 verify verbatim; REQ-014 lines 764–767 and 774 verify | **Yes.** Claim-role promotion is a REQ-014 question with its own oracle | Yes — defer the promotion, file it separately | Two arms, plus a default. The counter-argument ("a new kind of dishonesty rather than the old one") is the sharpest sentence in the packet and is kept |
| Q6 | Yes. `shell.lede` at line 27, no proper noun, `scope-instruction`, and **not** one of the 4 census rows — all re-derived | **Yes.** VIS-1 rank 2 against rank 1 is doctrine, not engineering | Yes | Two arms, plus a default that preserves the status quo and records it. PWB-REQ-012 line 688 is quoted **against** the recommendation |
| Q7 | Yes. `model.ts` lines 113 and 118 are literal types; 4 non-test and 6 test files name the builder | **Yes**, and correctly framed: the owner set the ceremony rule, so the packet puts rather than decides | Yes | Two arms, plus a default. Labeled `[Inferred]` as a judgment about who owns the rule |

No lawful arm is called unlawful anywhere. No owner trade-off is smoothed:
every question carries a counter-argument that argues against its own
recommendation, and Q1's is labeled "strong". Every question states a
default if unanswered; all seven defaults are lawful (each is either "no
change" or "design only, nothing lands"), with the slice-3 inconsistency at
F10 the one flaw in the set.

## Measurement table

| Claim | Re-derived? | My figure / note |
|---|---|---|
| 133-file top-level denominator (80 app + 53 core) | Yes | 133 (80 + 53) |
| 74 match / 59 do not | Yes | 74 / 59 |
| 37 test + 37 non-test, against 64 / 69 | Yes | 37 / 37, 64 / 69 |
| Remainder 27 test / 32 non-test; 34 app / 25 core | Yes | identical |
| Recursive 139 files, same 74; six extras under `polaris-generation/`, none matching | Yes | 139 / 74; the six are `draft-preview.ts`, `draft-preview.test.ts`, `draft-preview.browser.test.ts`, `pipeline-demo.ts`, `pipeline-demo-main.ts`, `pipeline-demo.test.ts` — "three tests" is exact |
| `grep -il` gives 73 | Yes, under this environment's wrapper | 73 via the wrapper; **74** with bare ugrep or system grep — cause misattributed, F5 |
| NUL byte at offset 13,811, line 305, in `project-shape-coverage.test.ts` | Yes | offset 13,811, line 305, exactly one NUL, in the template separator |
| `grep -ail` lists it; `grep -aic` gives 44 | Yes | both |
| 18 non-comment modules, 51 lines; 14/6/5/4/3 concentration | Yes | identical, file-by-file |
| Copy table 191 rows; second count 191 | Yes | 191 parsed, 191 raw `{ id: '` |
| 4 proper-noun rows at lines 26, 60, 62, 235 | Yes | identical (note: the proper-noun set itself is not enumerated in the packet) |
| Role partition 83 + 77 + 19 + 12 = 191 | Yes | identical |
| `shell.lede` line 27, no proper noun, `scope-instruction` | Yes | identical |
| Capture: 96 occurrences; verbatim `h1` | **No — unverifiable** | capture absent from the tree; F9 |
| Registry entry 14,604 bytes, one entry | Yes | identical |
| Six `observationGrammar` keys | Yes | `factFamilies`, `fixedCatalogKeys`, `fixedClassKeys`, `fixedProjectAccountKeys`, `precedence`, `rootSummary` |
| Grammar carries no root index path / extraction bindings / heading literals / tree rules | Yes | confirmed by key enumeration |
| `inputClasses` names `repository-locator-mapping` with that identity scheme, no value | Yes | identical |
| `subject.observedRepository` = `repository:butlers-configured-poc` | Yes | identical |
| Registry digest matches the amendment act record | Yes | full-digest `grep -F` hit; value not reproduced |
| Act lines 76–77 and 88–90 quoted verbatim | Yes | exact |
| Registry entry is a row of 2 manifests + the acceptance record | Yes | `PWB-EFFECT-ACTS-MANIFEST.txt`, `PWB-EFFECT-AMENDMENT-MANIFEST.txt`, `ACCEPTANCE-ACT-RECORD.md` |
| 22-file digest-binding corpus (14 `*MANIFEST.txt` + 7 evidence + 1) | Yes | 14 + 7 + 1 = 22 |
| 4 of 33 named paths appear in it | Yes, **and robust** | 4 under the 22-file corpus; still 4 when the corpus is widened to all 92 (`+ decisions/*.md`) |
| 2 non-test registry readers, 3 test | Yes | `governance-inputs.ts`, `walkthrough-inputs.ts`; 3 core tests |
| `load` closure at `governance-inputs.ts:314–331` | Yes | exact |
| `governance-inputs.ts:113` is the options interface (dossier row 3) | Yes | exact |
| `project-shape-coverage.ts`: 85 blank, `CLASS_ROWS` 86, `FACT_FAMILIES` 78 | Yes | exact |
| `polaris.ts` 420 brace, 424 `active-content`, 428 `denied-path` | Yes | exact |
| Remediation at 419, 423, 425, 427, 432, 441; routes at 671–683 odd | Yes | exact (line 583 unaccounted, F16) |
| `model.ts` 113 literal type, 118 literal `capabilityId`, 369 builder, 694 value | Yes | exact |
| 4 non-test + 6 test builder users | Yes | exact, enumerated |
| 1 h1-regex asserter at `polaris-first-reading.test.ts:62` | Yes | exact |
| 3 remediation-sentence asserters | Yes | the three named |
| 1 locator-constant namer (`git-observation.test.ts`) | Yes | exact |
| "1 asserts the two section headings" at `polaris-copy.test.ts:267` | **Partly** | line 267 asserts **one** heading; F6 |
| Consent record: subject line 15, locator line 17, parenthetical to 18 | Yes | exact |
| PWB-REQ-005: 195 at lines 231 and 248; consent row 9 at 245 | Yes | exact |
| PWB-REQ-005 prohibition at line 206 | Yes | exact |
| Scenario "Missing observation consent…" 296–300 | Yes | exact |
| PWB-REQ-012 line 683; "at most one `scope-instruction`" line 688 | Yes | exact |
| Scenario "Section headings name project concepts" 705–710 | Yes | exact |
| PWB-REQ-014 lines 764–765, 766–767, 774 | Yes | exact (F15 on the unmarked stop) |
| POC-REQ-050 line 777, falsifier 791–793, scenario 795–799 | Yes | exact |
| POC-REQ-051 line 812 | Yes | exact |
| Reader note "binding" line 18; subject at 23–24 | Yes | exact |
| PWB-REQ-001: line 73 WHEN; 74–76; 76–77; 78 | Yes | exact |
| PWB-REQ-001 has exactly one scenario (98–102) | Yes | exact |
| "deterministic input" at 76, 85, 95 | **No** | 85 and 95 only; F4 |
| 17 + 24 requirements; 31 + 24 = 55 scenarios | Yes | exact |
| 0 occurrences of the five literals in each specification | Yes | 0 / 0, both files in full |
| 37 / 29 / 2 proving-case occurrences | Yes | exact |
| "profile" once in the PWB specification, line 357 | Yes | exact |
| Both specification digests match their act records | Yes | PWB at `PWB-TRUTH-READINESS-AMENDMENT-ACT.md:89`; POC at `THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md` |
| Five `spec.md` under `openspec/changes/`, one per change | Yes | exact |
| RFC2-26 heading 194, clause 196–221, whole, no elision | Yes | byte-compared |
| RFC1-3 lines 130–133 | Yes | exact |
| RFC1-10 lines 263–266 | **Anchor over-reaches** | quoted sentence is 263–265; F2 |
| RFC1-2 lines 27–28 | **No** | clause at 121, sentence at 126–128; F1 |
| VIS-1 82–95, VIS-2 96–106, VIS-5 141–166, VIS-7 183–193 | Yes | quotations verbatim, elisions marked |
| SEC-1 `security.md` 10–23 | Yes | verbatim, elision marked |
| "No SEC clause names a repository locator" | Yes, with denominator | 0 hits for `locator` (case-insensitive) over all 6 doctrine files |
| No consent, registry entry or policy names the Syzygy repository | Yes, with denominator | 84 governance files swept; only `repository:butlers-configured-poc` occurs; 0 name `repository:syzygy`; exactly 1 registry entry |
| Implementation act: 59–61, 73, 88–94 | Yes | exact (two anchors inside the trigger list slip, F2) |
| Continuation act 69–71 | Yes | exact |
| Generator act line 42 | Yes | exact |
| `ARTIFACTS-AND-TOOLS.md` sentence wraps 94–95 | Yes | exact, and the wrap is real |
| `EXECUTION-PHASES.md` 5–6 and 13–14 | Yes | exact |
| Mutation record: commit, old, new, exitCode 1, restored true, no sha256 | Yes | exact; seven keys not five (F14) |
| Guarded fragment present exactly once in `polaris.ts` | Yes | 1 |
| Sibling intersections 1 / 7 / 6 / 9 / 5 / 2 | Yes | identical, and the span columns (3/17/15/26/11/24 any; 1/11/13/22/9/13 file) all match |
| Sibling heads `a9f671e` / `f2f37dd` / `6574600` / `63b8e33` / `ba9ca61` / `83c9f60` / `4090f98` | Yes | identical |
| No sibling branch touches an implementation-plane file | Yes for the six | M2–M6 diffs are `docs/**` + `PENDING-OWNER-DECISIONS.md`; M1 is on main. Lane B does touch `scripts/**`, which the packet says separately |
| Lane B intersection 0 by construction | Yes | 0 `scripts/` paths in the 31-file surface |
| M7 / M9 intersections | **Not computed by the packet** | 7 and 6; F8 |
| 31-file surface, all resolve | Yes for resolution | all 31 are files; the stated predicate does not re-derive, F7 |
| 0 odd-backtick non-fence lines of 1,344 | Yes for 0 | 0 of **1,343**; F3 |
| 6 lines over 78 columns outside fences/tables/quotes/headings | Yes | exactly 6, at 141, 329, 337, 412, 505, 523 |
| 250 distinct code spans; 11 with `/` not resolving | Yes | 250 and 11, and the 5+1+1+1+1+1+1 breakdown is exact |
| No observed-repository path backticked | Yes | 0 occurrences of the locator value; the one `BUTLERS`-bearing span is a Syzygy `decisions/` filename |
| No manifest or truncated signed digest reproduced | Yes | four comparisons reported as match/no-match only |
| Dossier differences 1–5 real | Yes | each opened at source |
| Dossier difference 7 (SEC-1 tag) real | Yes | dossier line 322 reads "VIS-1 and SEC-1 (locator)." |
| Dossier difference 8 (L1-M7 in `What`, in no slice) real | Yes | dossier line 320 names L1-M7; the slice list at 332–335 has six |
| Dossier's other citations "verified exactly" | Spot-confirmed | `project-shape-extraction.ts:689`, `git-observation.ts:40`, `project-shape-manifest.ts:47` all land on the intended anchors |
| Dossier not edited | Yes | only the two packet files differ from `a9f671e` |

## Gate 5 — the requirement-and-scenario test, checked per slice

Denominator seven, as the packet states; the seven rows are the seven slice
rows of Gate 3's authorizing-act table [Observed, counted].

- Slice 1, 4: "no consequence enumerated" — agreed. A test module and two
  unbound kit pages reach no surface and answer no query.
- Slice 2: the requirement-partial / scenario-absent finding re-derives. The
  55-scenario sweep for *project name*, *display name*, *project identity*,
  *names the project*, *which project*, *heading names* returns 0. The two
  repair routes quoted from RFC2-26 are in the clause; the packet's reading
  that the N/A route is "not reachable here" is labeled `[Inferred]`, which
  is the right label.
- Slice 3: PWB-REQ-005 line 206 and the scenario at 296–300 are exact and do
  cover the observable consequence (a new refusal reason: zero reads,
  Unknown, reason rendered).
- Slice 5: PWB-REQ-001 at 73 with its determinism sentence at 74–76 is exact;
  the single scenario at 98–102 is about the source set, not the input
  identity set — the packet's "requirement available, scenario not" holds.
  Its own sharpest counter-reading (that a closed four-item list may be
  *contradicted* rather than implemented by a fifth input) is stated, not
  buried.
- Slice 6: the absence is confirmed by my own sweep with its denominator
  (above). RFC1-3 and PWB-REQ-005 are correctly described as gates on
  whether the slice may run, not as coverage.
- Slice 7: POC-REQ-050 at 777, falsifier at 791–793, scenario at 795–799 and
  POC-REQ-051 at 812 are all exact, and the scenario's THEN is indeed what a
  seeded region from another project fails.

## Composition and bound-byte checks

No amendment overlay applies to either adopted specification, as the packet
says: the one overlay composition AGENTS.md names is the Polaris *generation*
pair, which governs slice 4's plane only. Both specification files are
digest-cited by owner-act records and neither is proposed for edit. The two
governed artifacts a slice touches are the registry entry (edited, only
through a new act — the mechanism its binding act's own closing sentence
names) and the consent record (read only). **No digest-bound byte is
proposed for edit outside that mechanism** [Observed, sweep over the 22-file
corpus and, independently, over all 92 manifest/evidence/decision files].
The packet's Gate 0 correctly declines to touch either specification's false
candidate banner, per the AGENTS.md rule that a bound file's banner may be
permanently wrong.

## Verdict

CONFIRM WITH EXCEPTIONS. Sixteen findings: 0 blocking, 11 non-blocking,
5 editorial. The packet's substance — its measurements, its seven questions,
its RFC2-26 test and its collision ordering — stands; F1 and F8 are the two
worth repairing before the register row lands, and F3's counting rule should
be fixed everywhere at once.

Verdict: CONFIRM WITH EXCEPTIONS
