# R-POLARIS-M8-PORTABILITY-FUNNEL — review 2 (raw, retained verbatim)

Independent fresh-context review of the review-1 exception repairs and of
the register row. Read-only: no tracked file was edited in any worktree, no
state-changing git command was run, the Butlers checkout and every
`.worktrees/` directory were left unopened, and no file named
`machine-credential.token` was read or printed. `git status --short` in the
review worktree was empty before this session's first read and is empty at
the end of it.

## Subject and bytes

Worktree: `agent/syzygy-dov.8`, HEAD
`4b2e8cbba4ec97fb434f17d88f7f8677982e849a`. Packet baseline `a9f671e`.
Sizes by `wc -c`, digests by `sha256sum`; neither transcribed.

| File | Bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md` | 146362 | `6a94a115a48f0ff8d8f9c834ae104dad0b55dc36f4568f4e7b66a6fa3d46ae2b` |
| `docs/evidence/polaris-m8-portability-funnel-2026-09-15.json` | 64220 | `c983836e25479262a7dd3c1702dd9d3b574982aa8b32ac23807b2febad0b81bc` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 35499 | `7964d61c00a27af84fad2002cde98ec3598f01b38e5f6f970d63a4f5e9b3f282` |
| `docs/reviews/R-POLARIS-M8-PORTABILITY-FUNNEL-RAW.md` (review 1, unedited) | 32375 | `85fcffa1db2f48e1b73df0689d37c154a445fe1c956f948936609b30e3c9b38d` |

The retained raw's bytes are byte-identical to what the packet's review-1
section and the record's `review1` block cite for it [Observed]. The two
files review 1 was bound to, recomputed here with `git show 8035c8f:<path>`:
the packet 110515 / `62ee454380619164b23e9e5bb896da5c1eb9f1cc6717c7c70b4d02c12ca15782`
and the record 42655 / `49b6f4dcbc4382645c4ca198bbc26af1fa530c45dbe042dd51228f4fe15e19d8`
— both match the packet's table and the record's `review1` block exactly
[Observed].

`python3 scripts/check_governance.py` in the worktree ends
`32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted`
(tail line read, not grepped) — unchanged from review 1 [Observed].

Sibling worktree heads read this session, read-only, by
`git -C <wt> rev-parse --short HEAD`: lane B `4090f98`, M2 `f2f37dd`,
M3 `6574600`, M4 `63b8e33`, M5 `ba9ca61`, M6 `83c9f60`, **M7 `1803608`**
and **M9 `65de02b`**. Six match the heads the packet's collision table
names; M7 and M9 have moved since it was written (from `0c4b4a9` and
`206d775`), and both figures are reported below [Observed].

Note on method, per verification rule 1: `grep` here is a shell function in
the session snapshot that execs the CLI binary with `argv[0]` set to
`ugrep` and injects `-G --ignore-files --hidden -I` plus six
`--exclude-dir` entries ahead of every caller argument (the snapshot line
was read directly). Every load-bearing count below was taken with Python
`re` over bytes decoded explicitly, and the two places a `grep`
corroboration is reported name the invocation.

## Summary

The sixteen review-1 exceptions are applied, and fourteen of them are
repaired completely and verify at source. Two are **partial**: F7's
restated derivation and F16's corrected phrase are applied at the site the
finding named and not at the sites that carry the figure. Nothing found
here falsifies a measurement's conclusion, a recommended answer, a lawful
arm or a default. No blocking finding.

The eight new findings are: one stale pair of keys in the evidence record
that presents the first draft's size and digest as current (G1); two
undated present-tense claims about siblings that have since moved or were
never true of lane B (G2, G3); two self-referential figures that no longer
re-derive over the bytes that carry them or whose predicate is short by an
unstated bound (G4, G5); the two partial repairs (G6 carries F16); and two
editorial slips introduced by the repairs themselves (G7, G8).

## Review-1 repair verification, F1–F16

Every row re-derived at source over the current bytes this session.

| # | Severity as filed | Verdict | Evidence |
|---|---|---|---|
| F1 | non-blocking | **REPAIRED** | `RFC-0001-project-graph-identity-state-planes.md` line 121 opens `**RFC1-2.**`; the quoted sentence begins at the trailing word *Repository* on line **126** and ends on **128**; lines 27–28 are front matter. Both sites (Q4's cell and Gate 2) now cite 126–128 with the clause opening at 121, and both quote the superseded "lines 27–28" in place, dated [Observed, opened at source] |
| F2 | non-blocking | **REPAIRED** | `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`: "a change to the constraints or envelope the registry entry declares" begins on **91**, ends 92; "any scope beyond the signed change" begins on **93**, ends 94. RFC1-10's quoted sentence spans **263–265**; 266 opens the next sentence. All three corrected with superseded citations kept [Observed] |
| F3 | non-blocking | **REPAIRED** | `wc -l` gives **1152** and **1008**; `len(bytes.split(b"\n"))-1` gives the same and the naive split gives 1153 / 1009. All four sites carry the corrected figures, and the counting rule is stated once at the packet's lines 20–33. The packet's own non-fence denominator, now **1697**, re-derives exactly over these bytes [Observed, both methods run] |
| F4 | non-blocking | **REPAIRED** | Python `re` over the PWB specification in full returns the literal "deterministic input" on lines **85** and **95** only; line 76 carries "deterministic **evaluation** inputs". The packet's sentence now says so and its conclusion is unchanged [Observed] |
| F5 | non-blocking | **REPAIRED**, reproduced both ways | Over the 133-path argument list: wrapper `grep -il` → **73**; wrapper `grep -ail` → **74**; `/bin/grep -il` → **74**; `/bin/grep -aic` on `packages/three-surface-poc-core/src/project-shape-coverage.test.ts` → **44**. That file carries exactly one NUL at byte offset **13,811**, on line **305**. `command -v ugrep` is empty and `type grep` names the shell function; the snapshot's line injects `-G --ignore-files --hidden -I` plus six `--exclude-dir` entries. The packet now attributes the 73 to the wrapper's `-I` and records the invocation that produced it — correct [Observed, all invocations run this session] |
| F6 | non-blocking | **REPAIRED** | The proving case's name occurs exactly **once** in `apps/three-surface-poc/src/polaris-copy.test.ts`, on line **267**, inside one clean-fragment expectation asserting one heading string; the second group heading occurs nowhere in the file. The packet reads "one of the two section headings" [Observed, whole file swept] |
| F7 | non-blocking | **PARTIAL** | The surface itself re-derives: the record's `m8_surface` holds **31** paths, all 31 resolve as files, the eight test files are named in the packet, and 23 + 8 = 31. Slice 6's reconciliation is applied in Gate 3's row, Gate 4's slice and the collision list, all three marked *exercised, never edited*. **But** the restated intermediate figures do not re-derive over the bytes that carry them — see **G4** |
| F8 | non-blocking | **REPAIRED** | Recomputed independently under the packet's stated predicate against the record's 31-path surface, in each sibling worktree at the head the table names. Span columns and intersections reproduce **exactly**, all nine rows — see the collision section below. M9's basename-tolerant **8**, with `apps/three-surface-poc/src/orrery.ts` and `packages/three-surface-poc-core/src/body-read-authority.ts` as the two uncounted bare spans, reproduces. Lane B's 0-by-construction holds: the 31-path surface carries no `scripts/` path [Observed] |
| F9 | non-blocking | **REPAIRED** | The capture is **2,090,025** bytes, sha256 `0bff1adfc43b1d5f8595e3a5c13bc56f54a27fb5ca0175fa838be04eb3a36305`, and `git ls-files` in the worktree returns 0 matches for it. Holding the file, both figures reproduce: **96** occurrences of the exact proper noun, and the `h1` element is verbatim as quoted. Both now carry the dual "[Observed at the retained capture] / [Unknown] to a reader without that file" label, and the decision not to copy it into the tree is stated with its reason. Item 10's predicate is widened — but see **G5** on how it is stated |
| F10 | non-blocking | **REPAIRED** | All four sites now agree on slice 3. Q1's default reads "slices 1, 3, 4 and 6's design work proceeds to review; nothing lands" and says why; Q4's default is the recommended arm; the funnel-summary handoff line leads with "rule Q1 first" and quotes the superseded line; the prose handoff carries the condition. No recommendation moves [Observed, all four read] |
| F11 | non-blocking | **REPAIRED** | VIS-4 is quoted at `vision.md` lines **122–139** (the clause opens on 122 and its *Violation* list ends on 139) and applied to Q2's and Q3's four acts and to Q1's spec-level-versus-shape-level contest. SEC-5 is quoted at `security.md` lines **54–60** and applied to slice 6's detector run and Q3's policy extension. The packet's correction of the finding's own counts is itself correct: the first draft carried `VIS-4` **1** time and `SEC-5` **2**, not 2 and 3 [Observed, counted over `8035c8f`]. One new quotation slip inside this repair — **G7** |
| F12 | editorial | **REPAIRED** | The funnel summary now reads "the six siblings' existing rows" and enumerates P-68…P-73, quoting the superseded "five". Each of those six branches adds exactly that one `^| P-` row against `a9f671e` and no other [Observed, diffed in all six worktrees] |
| F13 | editorial | **REPAIRED** | Under the same comment-blanking predicate, `apps/three-surface-poc/src/test-project-shape-fixture.ts` carries **3** of the 51 lines, at **19, 28, 54**. The packet reads "one to three each" and names the file and its lines. The remaining twelve carry 16 lines between them, so "one to two for twelve of them" holds [Observed] |
| F14 | editorial | **REPAIRED** | The record carries seven keys — `commit`, `file`, `old`, `new`, `exitCode`, `output`, `restored` — with `exitCode` 1, `restored` true and no `sha256`. The packet says seven and keeps the raw's observation that it reads five and quotes the sixth [Observed] |
| F15 | editorial | **REPAIRED** | All three opened at source. PWB line 248 uses curly quotes around *other invalid* and the packet now reproduces them. PWB-REQ-014's anchor-set sentence continues "and is small enough for a reader to identify which anchor supports which claim" and the quotation is extended to 766–768. POC-REQ-050's sentence continues ", with a deterministic layout per observation" and the quotation is extended to 777–780 [Observed] |
| F16 | editorial | **PARTIAL** | Line **583** is `const practicalOrder = ['Butlers', 'Staffers', 'Dashboard', 'Connectors'];`, and the fourteen non-comment lines re-derive as 419, 423, 425, 427, 432, 441, 583, 671, 673, 675, 677, 679, 681, 683. The differences table and the disposition row both name it and state the consequence for slice 2. **But** the phrase it corrects is unchanged at its three use sites — see **G6** |

## New findings

### G1 — non-blocking — the record's own `file_bytes` and digest keys still present the first draft's figures as current
`docs/evidence/polaris-m8-portability-funnel-2026-09-15.json`, the
top-level `file_bytes` and `file_digests_sha256` keys.

**Defect.** Both carry a single entry for
`docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md`: **110515** bytes and the
digest `62ee454380619164b23e9e5bb896da5c1eb9f1cc6717c7c70b4d02c12ca15782`.
Those are the bytes at `8035c8f`. The packet at this commit is **146362**
bytes and hashes to
`6a94a115a48f0ff8d8f9c834ae104dad0b55dc36f4568f4e7b66a6fa3d46ae2b`
[Observed, `wc -c` and `sha256sum` this session, and `git show 8035c8f:`
for the comparison]. Neither key is dated, qualified or marked superseded,
and neither names a commit — unlike `review1.reviewed_files_at_that_commit`
twelve keys below, which carries the same two values correctly labelled as
the reviewed bytes at `8035c8f`. The record also records neither its own
size nor its own digest, in either place. A reader who takes the top-level
keys as the record's statement of what it describes is given the size and
digest of bytes that no longer exist, in the one file whose whole job is to
be the checkable side of the packet. This is the packet's own
"superseded wording is marked in place and dated, never deleted" rule
unapplied to the record.

**Repair.** Rename the two keys to say `_at_8035c8f`, or add the current
figures with their commit beside the superseded pair.

### G2 — non-blocking — "no sibling branch touches an implementation-plane file today" is false for lane B, and its denominator is stale
`docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md:57–58` and `:1363–1370`.

**Defect.** Both sentences read "every one of the six sibling branches is a
documentation branch" and the second closes "**no sibling branch touches an
implementation-plane file today** [Observed, run in all six worktrees this
session]". A name-only diff of lane B against `a9f671e` at `4090f98` names
`scripts/build_pwb_scoped_attributes_amendment.py`,
`scripts/check_governance.py`,
`scripts/estimate_pwb_scoped_attributes_saving.py` and
`.github/workflows/governance-docs.yml` among its governance files
[Observed, run this session]. The packet contradicts the sentence itself
seventeen lines later: "Lane B also edits `scripts/check_governance.py`".
Separately, F8 widened the sibling denominator from six to nine, and both
sentences and the bracketed denominator still say six, although M7's and
M9's worktrees were opened this session for the F8 repair. At their
current heads M2–M7 and M9 do each name only `docs/**` and the register
[Observed, eight diffs run], so the true statement is available.

**Repair.** "Every one of the seven documentation sibling branches — M2
through M7 and M9 — names only `docs/**` and the register; lane B is the
exception and edits `scripts/`", with the denominator eight branches.

### G3 — non-blocking — "M7 and M9 carry no register row yet" is false at the siblings' current heads
`docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md:1273`, `:1274`, `:1617–1619`
and the funnel summary at `:1650`; also
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:136–137`.

**Defect.** Four sites in the packet and the register's own blockquote
state, in the present tense and without a date or a head, that M7 and M9
carry no register row. At `1803608` M7's branch adds exactly one row,
**P-76**; at `65de02b` M9's adds exactly one, **P-75** [Observed, `^+| P-`
over `git diff a9f671e` in each worktree this session]. The claim was true
of the heads the collision table names (`0c4b4a9`, `206d775`) and is not
true of the branches as they now stand. There is no numbering collision:
main tops at P-53 and the nine sibling registers carry P-68, P-69, P-70,
P-71, P-72, P-73, **P-74** (this branch), P-75 (M9) and P-76 (M7), each
only on its own branch [Observed, nine registers recounted this session].

**Repair.** Bind the claim to the heads the table names, or restate it at
the current heads and name P-75 and P-76.

### G4 — non-blocking — F7's restated derivation figures no longer re-derive over the bytes that carry them
`docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md:1244–1249` (the collision
method's bracketed restatement) and the F7 disposition row at `:1606`.

**Defect.** Both say "Gate 3's topology table carries **30** code spans,
**25** of them file-shaped and distinct; **20** resolve as written". Over
the bytes at `8035c8f` that is exact: 30 spans, 26 file-shaped distinct of
which one is the directory span `packages/three-surface-poc-core/src/`,
leaving 25, and 20 resolving as written [Observed, `git show 8035c8f:`].
Over the current bytes it is not: the F7 repair itself added two spans to
Gate 3's slice-6 row —
`packages/three-surface-poc-core/src/project-shape-model.ts` and
`m8_by_slice` — so the table now carries **32** code spans, **26**
file-shaped and distinct less the directory span, and **21** resolving as
written [Observed, both computed this session]. The derived figures are
unaffected and re-derive exactly: 25 existing files, less the two governed
artifacts the third column names, is **23**; plus the record's **8** tests
is **31**, and all 31 resolve as files. This is the self-referential class
the packet identifies and resolves for item 10 and the over-width count by
a final pass ("written as placeholder tokens and resolved by a final
pass"); the discipline was not carried to the F7 restatement.

**Repair.** Re-derive the three intermediate figures last, or date them to
`8035c8f` the way the review-1 table dates its digests.

### G5 — non-blocking — item 10's widened predicate is short by an unstated bound, and the figures resting on it cannot be re-derived as written
`docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md:1513–1532` (Gate 6 item 10,
"The resolution predicate, widened").

**Defect.** The predicate is stated as: "A span is filename-shaped if it
contains a `/` or if it is a bare name of the form *stem*-dot-*extension*."
Applied literally over the same span population, the figures are **149**
filename-shaped, **52** not resolving, **40** slash-free non-resolving and
**13** resolving nowhere, of which **11** are dotted identifiers. The
packet publishes 145 / 48 / 36 / 9 / 7. The four spans that decide it are
`shell.heading`, `group.overview`, `group.architecture` and
`evidence.relationships` — the same dotted-identifier form as `shell.lede`
and `capability.scope`, which the packet does count. The published figures
re-derive **exactly** only if the extension is bounded to six characters or
fewer, which the stated predicate does not say: at bounds of 3, 4, 5, 6 and
7 the filename-shaped count is 137, 141, 142, **145** and 146 [Observed,
all six runs this session]. This is the AGENTS.md lesson that a word set
published as "or similar" is not a predicate and the figure resting on it
cannot be re-derived. Everything else in item 10 reproduces exactly: **297**
distinct non-fence code spans, **12** slash-bearing non-resolving spans
(the enumerated twelve), **27** bare basenames resolving as a tracked
basename, **0** odd-backtick non-fence lines of **1697**, and — under
either reading of the bound — the load-bearing **1**, `polaris-7478.html`.

**Repair.** State the extension bound, or publish 149 / 52 / 40 / 13 / 11.

### G6 — non-blocking — F16's correction is applied at one site and not at the three that use the figure
`docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md:789`, `:816` and `:1193`.

**Defect.** The differences table and the F16 disposition now both state
that "the fourteen renderer-built sentences" is thirteen sentences and one
ordering constant, and that slice 2 must carry the constant. The three
places that *use* the figure are byte-identical to the first draft
[Observed, compared against `git show 8035c8f:`]:

- `:789` slice 2's "What": "Do the same for the fourteen renderer-built
  sentences in `apps/three-surface-poc/src/polaris.ts`".
- `:816` slice 2's rule-6 mutant (c): "Leave one of the fourteen
  remediation sentences untemplated".
- `:1193` scenario S3: "the four page eyebrows and all fifteen remediation
  sentences carry that name".

The last two are wrong in kind as well as in count: only **6** of the
fourteen lines are remediation sentences (419, 423, 425, 427, 432, 441);
seven are pillar routes (671–683 odd) and one is the ordering constant at
583 [Observed, re-derived under the comment-blanking predicate]. S3 is the
acceptance contract an implementing bead would be held to, so the
mis-description is the one that would propagate.

**Repair.** Carry the correction to all three sites; S3 should name the
classes rather than one count.

### G7 — editorial — a new unmarked quotation stop, introduced by the F11 repair
`docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md:615–621` (Gate 2, SEC-5) and
`:585–600` (Gate 2, VIS-4).

**Defect.** The SEC-5 quotation ends "A secret reproduced in any Syzygy
surface, store, or endpoint is a trust-floor violation." with a closing
period. At `.syzygy/governance/doctrine/security.md` the sentence continues
"(trust-and-evidence.md, floor bullet 4)." on line 59 [Observed, opened at
source]. The stop is unmarked — the same defect F15 repaired at
PWB-REQ-014 and POC-REQ-050 in this same pass. The VIS-4 quotation
likewise ends at "an agent editing a spec to match code it just wrote."
where the *Violation* list continues "; treating RFC acceptance alone as
opening the gate."; that one is milder, because the quotation already
carries a leading `…` inside the *Violation* clause and reads as excerpted.
Everything else in both quotations is verbatim and every internal elision
is marked, and both clause anchors are exact.

**Repair.** Mark both stops with `…`.

### G8 — editorial — item 10's over-width figure changed predicate and the superseded figure was deleted rather than marked
`docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md:1508–1512` and `:1670–1673`.

**Defect.** The first draft read "**6** lines exceed 78 columns outside
fences, tables, block quotes and headings, and every one is a single
unbreakable code span: four repository paths, one quoted HTML element and
one path inside a sentence." The current bytes read "**16** lines exceed 78
columns under the predicate 'outside fenced code blocks, first non-space
character not a pipe, length over 78'". Both figures are true of their own
predicate — I re-derive **16** under the stated one and **7** under review
1's over the current bytes [Observed, both run] — but the predicate change
and the superseded "6" are unmarked, in a packet that marks every other
supersession in place and dated. A reader comparing review 1's confirmed 6
to the packet's 16 reads a regression that did not happen. The dropped
clause matters too: of the seven lines over 78 under review 1's predicate,
six are single unbreakable code spans and the seventh, `:1517` at 79
columns — "contain a `/` — write-root and glob patterns, a regular
expression, an HTML" — is ordinary breakable prose introduced by these
repairs, so the deleted claim is now false as well as unmarked.

**Repair.** Quote the superseded figure and its predicate in place, and
either rewrap `:1517` or drop the unbreakable-span claim explicitly.

## Load-bearing measurements, re-run this session

Every figure below was taken in the review worktree at `4b2e8cb` with
Python `re` over bytes decoded explicitly, unless a `grep` invocation is
named. Denominators and predicates are the packet's own.

| Claim | Re-derived? | My figure |
|---|---|---|
| Top-level `.ts` population, 80 app + 53 core | Yes | **133** |
| 74 match *butler* case-insensitively / 59 do not | Yes | 74 / 59 |
| 37 test + 37 non-test matching, against 64 / 69 | Yes | identical |
| Remainder 27 test / 32 non-test; 34 app / 25 core | Yes | identical |
| Recursive 139 files, same 74, six extras under `polaris-generation/` | Yes | 139 / 74; the six named are exact |
| Wrapper `grep -il` 73, `-ail` 74, `/bin/grep -il` 74, `-aic` 44 | Yes | identical, four invocations run |
| One NUL at offset 13,811, line 305 | Yes | exactly one |
| 18 non-comment modules, 51 lines; 14 / 6 / 5 / 4 / 3 concentration | Yes | identical, file by file |
| `polaris.ts` fourteen non-comment lines | Yes | 419, 423, 425, 427, 432, 441, **583**, 671–683 odd |
| Copy table 191 rows, second count 191 raw `{ id: '` | Yes | 191 / 191 |
| 4 proper-noun rows at 26, 60, 62, 235 | Yes | identical |
| Role partition 83 + 77 + 19 + 12 = 191 | Yes | identical |
| `shell.lede` line 27, no proper noun, `scope-instruction` | Yes | identical |
| Capture 2,090,025 bytes; 96 occurrences; verbatim `h1`; 0 `git ls-files` matches | Yes | identical |
| Registry entry 14,604 bytes, one entry, six `observationGrammar` keys | Yes | identical, keys enumerated |
| Four digest comparisons (registry entry, both specifications, consent record) | Yes | all four match their cited records; no value reproduced here |
| Registry entry is a row of 2 manifests plus the acceptance record | Yes | identical |
| 22-file digest-binding corpus (14 `*MANIFEST.txt` + 7 evidence + 1) | Yes | 14 + 7 + 1 = 22 |
| 4 of 33 named paths in that corpus | Yes | the same four |
| 2 non-test registry readers, 3 test | Yes | `governance-inputs.ts`, `walkthrough-inputs.ts` |
| `model.ts` 113 / 118 literal types, 369 builder, 694 value | Yes | exact |
| 4 non-test + 6 test builder users | Yes | exact |
| `git-observation.ts:6` locator constant; `git-observation.test.ts` names it | Yes | exact |
| `polaris-first-reading.test.ts:62` h1 regex | Yes | exact |
| `polaris-copy.test.ts:267`, one heading, name occurs once in the file | Yes | exact |
| Mutation record: seven keys, `exitCode` 1, `restored` true, no `sha256` | Yes | exact |
| Both specifications 1,152 / 1,008 physical lines | Yes | `wc -l` and split both agree |
| 0 occurrences of the five literals in each specification | Yes | 0 / 0, both files in full |
| 37 / 29 / 2 proving-case occurrences | Yes | exact |
| "profile" once in the PWB specification, line 357 | Yes | exact |
| 17 + 24 requirements; 31 + 24 = 55 scenarios | Yes | exact |
| The 55-scenario sweep for the six identity phrases returns 0 | Yes | 55 swept, 0 match |
| PWB-REQ-001 has exactly one scenario, 98–102 | Yes | exact |
| "deterministic input" at 85 and 95 only | Yes | exact |
| Five `spec.md` under `openspec/changes/`, one per change | Yes | 5 |
| `project-shape-extraction.ts:369` dispatches on `base === 'vision.md'`, and `.syzygy/governance/doctrine/` holds `vision.md`, `architecture.md`, `v1.md` | Yes | exact |
| `main.ts:102` keys the snapshot by a literal name prefix | Yes | exact |
| 297 distinct code spans; 12 slash-bearing non-resolving; 27 basenames; 0 odd-backtick of 1697; 16 over 78 | Yes | exact |
| 145 filename-shaped / 48 non-resolving / 9 nowhere | **Only under an unstated bound** | 149 / 52 / 13 as stated; G5 |
| Gate 3 table: 30 spans, 25 file-shaped, 20 resolving | **No, at these bytes** | 32 / 26 / 21; the derived 25 / 23 / 31 hold; G4 |

## Contract and doctrine quotations, spot-checked at the cited line

Every quotation below was opened at source this session and compared
against the packet's rendering (rule 8).

- **RFC1-2** — clause opens at line 121; quoted sentence spans **126–128**.
  Verbatim. [Observed]
- **RFC1-3** — lines **130–133**, including "governance root or not".
  Verbatim. [Observed]
- **RFC1-10** — lines **263–265**. Verbatim; 266 opens the next sentence.
  [Observed]
- **RFC2-26** — heading at 194, clause at **196–221**. Reproduced **whole,
  both paragraphs, with no elision**: normalised byte comparison against
  the source lines returns an exact match. [Observed]
- **PWB-REQ-001** — line 73 WHEN; determinism sentence beginning on 74 and
  ending on 76; "Human and machine readers SHALL receive those identities"
  on 76–77; "Every emitted project-shape fact…" on 78; scenario 98–102.
  All verbatim. [Observed]
- **PWB-REQ-005** — prohibition 206; disclosure 220–222; "exactly 195
  independently decided cases" beginning on 231; consent row 245 with its
  three fields and its 9; total row 248 with **curly** quotes around *other
  invalid*; scenario 296–300. All verbatim. [Observed]
- **PWB-REQ-012** — line 683; "At most one entry `scope-instruction` may
  state the POC bound" on 688; scenario 705–710. Verbatim. [Observed]
- **PWB-REQ-014** — claim roles 764–765; anchor-set sentence complete at
  766–768; anchor target classes at 774. Verbatim. [Observed]
- **POC-REQ-050** — normative sentence complete at **777–780**; falsifier
  791–793; scenario 795–799. **POC-REQ-051** at 812. Verbatim. [Observed]
- **Three-Surface POC reader notes** — "binding on how this file is read"
  on 18; the configured-project sentence on 23–24. Verbatim. [Observed]
- **`PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`** — grant point 3 at 59–61;
  the second-repository exclusion beginning on 73; the escalation triggers
  at 88–94. Verbatim. [Observed]
- **Continuation act** — the owner's question at 69–71, with the retained
  exclusions. Verbatim. [Observed]
- **`PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`** — Effect close at
  76–77; "What this act does not authorize" at 88–90. Verbatim. [Observed]
- **Generator act** — line 42, including the reservation. Verbatim.
  [Observed]
- **`EXECUTION-PHASES.md`** — 5–6 and 13–14. Verbatim. [Observed]
- **`ARTIFACTS-AND-TOOLS.md`** — the bar genuinely wraps 94–95. Verbatim.
  [Observed]
- **Consent record** — subject on 15; "Current locator:" on 17 with the
  path in a code span and the parenthetical running onto 18. [Observed]
- **VIS-4** — `vision.md` **122–139**, verbatim with internal elisions
  marked; the terminal stop is unmarked but reads as excerpted (G7).
- **SEC-5** — `security.md` **54–60**, verbatim to the stop, which is
  unmarked (G7).
- **VIS-1, VIS-2, VIS-5, VIS-7, SEC-1** — unchanged from the first draft
  and confirmed by review 1; spot-re-read, still exact. [Observed]

## The collision table, recomputed at both sets of heads

Predicate as the packet states it: every code span of the sibling packet
beginning `apps/`, `packages/`, `scripts/` or `docs/polaris-generation/`
(or equal to `package.json`), resolved against this worktree under
`os.path.exists` and `os.path.isfile`, the file-resolving set intersected
with the record's 31-path `m8_surface`.

| Sibling | Head the packet names | any / file / ∩ | Current head | any / file / ∩ |
|---|---|---|---|---|
| M1 (on main) | `a9f671e` | 3 / 1 / **1** | same | — |
| M2 | `f2f37dd` | 17 / 11 / **7** | `f2f37dd` | unchanged |
| M3 | `6574600` | 15 / 13 / **6** | `6574600` | unchanged |
| M4 | `63b8e33` | 26 / 22 / **9** | `63b8e33` | unchanged |
| M5 | `ba9ca61` | 11 / 9 / **5** | `ba9ca61` | unchanged |
| M6 | `83c9f60` | 24 / 13 / **2** | `83c9f60` | unchanged |
| M7 | `0c4b4a9` | 29 / 21 / **7** | **`1803608`** | 30 / 22 / **7** |
| M9 | `206d775` | 19 / 12 / **6** | **`65de02b`** | 20 / 13 / **7** |
| lane B | `4090f98` | not computed; **0** by construction | `4090f98` | 0 by construction |

Every published figure reproduces exactly at the head its row names
[Observed, all nine computed this session]. At M9's current head the
full-path intersection rises to **7**, because `orrery.ts` — one of the two
bare basenames the packet discloses — is now written as a full path there;
the basename-tolerant figure is **9**, the two uncounted bare spans being
`packages/three-surface-poc-core/src/body-read-authority.ts` and
`docs/polaris-generation/README.md`. M7's intersection is unchanged at 7,
and it carries no bare spans that add to it under either predicate
[Observed]. **"M8 intersects eight of the nine sibling packets — every one
but lane B" survives at both sets of heads**, and the ordering
recommendation (M8 lands last) is unaffected.

The 31-path surface carries no `scripts/` path, so lane B's 0 is genuinely
by construction [Observed].

## The seven questions, re-put after the repairs

| # | Scope truthful? | Genuine hard gate? | Recommendation follows? | All lawful arms named? |
|---|---|---|---|---|
| Q1 | **Yes.** The 0-occurrence sweep, 37 / 29 / 2, the corrected 1,152 / 1,008 denominators, PWB-REQ-001 line 73 and the binding reader note at 23–24 all re-derive exactly | **Yes.** No clause settles whether portability rides the existing act or needs a CC-REV-2 amendment, and VIS-4's "contested by default and is never made by the agent performing the change" is now quoted against the packet's own position | Yes, and the split is still labelled `[Inferred]` rather than asserted as a rule | Three arms plus a default. The counter-argument is called "strong" and argues against the recommendation |
| Q2 | **Yes.** 14,604 bytes, one entry, six grammar keys, the digest match and the act's 76–77 and 88–90 all verify verbatim | **Yes.** The binding act's own closing sentence makes any edit a new act; VIS-4 reserves it to the owner | Yes; the limb split is supported by the five-limb design | Two arms plus a default; the forever-cost counter-argument is preserved |
| Q3 | **Yes.** Independently confirmed: the consent record's subject line 15 names `repository:butlers-configured-poc`, exactly one adapter-registry entry exists, the implementation act's line 73 exclusion and the continuation's 69–71 are verbatim, and RFC1-3's 130–133 is unqualified | **Yes.** Three ceremonies against an unqualified clause | Yes, and the slice is designed and not run | Two arms. The packet still declines to call the second lawful **or** unlawful and says why — the correct posture. SEC-5 is now quoted at its clause and applied to the third act |
| Q4 | **Yes** — review 1's "mostly" is discharged: F1's anchor is corrected at both sites and re-verified here at 126–128 | **Borderline**, for the reasons review 1 gave and the packet keeps: the recommended arm needs no act and its default proceeds; what makes it owner material is the second arm, which contradicts an act-bound "exactly 195", and the security-surface trade-off | Yes | Two arms plus a default; the counter-argument is the stronger security reading and is not softened |
| Q5 | **Yes.** `DEFAULT_CLAIM_ROLE` at 260–265 with its comment at 257–259, REQ-014 at 764–765, the now-complete 766–768 and 774 all verify | **Yes.** Claim-role promotion is a REQ-014 question with its own covering-and-minimal oracle | Yes — defer the promotion and file it separately | Two arms plus a default; "a new kind of dishonesty rather than the old one" is kept intact |
| Q6 | **Yes.** `shell.lede` at line 27, no proper noun, `scope-instruction`, and not one of the four census rows — all re-derived | **Yes.** VIS-1 rank 2 against rank 1 is doctrine, not engineering | Yes | Two arms plus a status-quo default that the packet records as an outcome. PWB-REQ-012 line 688 is still quoted **against** the recommendation |
| Q7 | **Yes.** `model.ts` 113 and 118 are literal types; 4 non-test and 6 test files name the builder | **Yes**, and correctly framed: the owner set the ceremony rule, so it is put rather than decided | Yes | Two arms plus a default; labelled `[Inferred]` as a judgment about who owns the rule |

**RFC2-26's reviewed-N/A arm.** It is named for every slice that could
reach it. Slices 2 and 5 are the two whose consequences are enumerated and
unmapped by a scenario, and both cells quote the arm from the clause
("a recorded owner judgment homed in `decisions/` (RFC3-15)", honoured only
through an effective owner act under RFC3-16(a)) and mark the packet's own
view that slice 2 does not fit it as `[Inferred]`. Slice 7's consequence
maps to POC-REQ-050 with its scenario, so the arm is not needed; slices 1,
4 and 6 enumerate no consequence, so the clause is not engaged. No lawful
arm is called unlawful anywhere in the packet [Observed, all seven rows
read].

**No trade-off is smoothed.** Every question still carries a
counter-argument that argues against its own recommendation, and Q1's is
still called strong. No recommended answer, second arm or default moved
between `8035c8f` and these bytes: I compared all seven Q-cells across the
two versions and the only substantive change is F10's addition of slice 3
to Q1's default, which the packet marks and dates in place [Observed].

## The register

**Faithfulness.** The P-74 row renders all seven questions in the order and
substance the packet's Q1–Q7 table carries **after** the repairs. Each
question's recommended arm, second arm (and Q1's third), counter-argument
and default-if-unanswered is present and matches the packet's cell. Q1's
default reads "slices 1, 3, 4 and 6's design work proceeds to review;
nothing lands" — the post-F10 wording, not the first draft's. Q1's third
arm's "slice 2 proceeds with the five" is a faithful contraction of the
packet's "slices 1, 3, 4, 6 and 7". Q4's default is "the recommended arm"
with its reason. [Observed, both read side by side]

**Verdict word and counts.** The blockquote copies the verdict word exactly
— **CONFIRM WITH EXCEPTIONS** — and states "no blocking, eleven
non-blocking, five editorial, F1–F16", which matches the raw's "0 blocking,
11 non-blocking, 5 editorial" and its sixteen findings. The row's cell
repeats the same counts and correctly partitions F1–F11 non-blocking and
F12–F16 editorial. [Observed]

**Recount.** Reproducible under the predicate the blockquote states — split
the file on `## ` headings and match, at line start in each section, a
table row whose first cell is `P-` followed by anything but a cell break.
At `a9f671e`: 5 in the acceptance-act section, 21 in the open section,
**21 / 5 / 26**. On this branch: 5 and 22, **22 / 5 / 27**. Both figures
re-derive exactly [Observed, run against both trees this session].

**Which rows live only on their branches.** The register's claim is correct
for the six it names — main tops at **P-53**, and each of lane B, M2, M3,
M4, M5 and M6 adds exactly one row (P-68, P-69, P-70, P-71, P-72, P-73) and
no other against `a9f671e` [Observed, nine registers recounted at their
current heads]. It is **wrong** about M7 and M9, which now carry **P-76**
and **P-75** on their own branches — G3. There is no collision with P-74.

**Digest and path hygiene.** The P-74 row and the blockquote reproduce no
digest of any length and backtick no observed-repository path: a sweep for
runs of 8 or more hex characters over both returns **0**, and no code span
in either contains an observed-repository path — the only Butlers-bearing
spans anywhere in the packet are Syzygy `decisions/` and `declarations/`
filenames, an opaque repository identifier, source fragments and the
capture's `h1` [Observed, both swept]. CG-1b and CG-7e/CG-15 hold, and
`check_governance.py` ends `0 FAIL`.

## Invariants

- No manifest row or truncated signed digest is reproduced in the packet,
  the record or the register row. The five full hex strings in the packet
  are the retained raw's own digest, the capture's, the two `8035c8f` file
  digests the review names, and one git commit id from the mutation record
  — none is an act argument or a signed-digest prefix [Observed].
- No observed-repository path is backticked anywhere in the three
  artifacts [Observed, sweep above].
- Every code-span path resolves, or is accounted for: 12 slash-bearing
  non-resolving spans enumerated, 27 bare basenames resolving as tracked
  basenames, and one span naming a real file outside this repository — the
  capture — disclosed with its size and digest. G5 concerns how the
  accounting's predicate is stated, not the accounting's conclusion.
- Substantive claims are labelled. I found no unlabelled substantive claim
  introduced by the repairs; the two capture-only figures now carry the
  dual label F9 asked for.
- Zero/all claims carry a predicate and a denominator, and every one I
  re-ran this session reproduces, with the two exceptions at G4 and G5.
- Digests are computed, never transcribed, in both the packet and the
  record; the record's two stale keys at G1 are a labelling defect, not a
  transcription.
- Prose is within 78 columns except the 16 the packet itself reports, of
  which one (`:1517`) is breakable prose — G8. No code span is broken
  across a line break: 0 odd-backtick non-fence lines of 1697.
- `python3 scripts/check_governance.py` ends `0 FAIL`.

## Closing

The repairs hold. Fourteen of sixteen are complete and verify at source;
two are partial in the same way — the finding's own site is repaired and
the sites that carry the figure are not (F7 → G4, F16 → G6). The eight new
findings are all repairable in place, none of them touches a recommended
answer, a lawful arm, a default or a gate, and the packet's substance — its
measurements, its seven questions, its RFC2-26 test and its collision
ordering — stands at these bytes.

By verification rule 10 this review binds `4b2e8cb` and the four digests in
the header table, and any later edit retires it.

Verdict: CONFIRM WITH EXCEPTIONS
