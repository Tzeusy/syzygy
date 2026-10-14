> # Record beside the package — not authority, binds nothing
>
> Dispositions of the second fresh-context review of the PWB class-granular
> extraction amendment package (M15). This record is not a package artifact:
> the manifest does not hash it and no builder reads it. It offers nothing
> and performs no act (VIS-4).

# Round 2 dispositions — PWB class-granular extraction amendment

- **Reviewed commit:** `1701c88f31dcf74130f6f2b5c84b990ebc49de08`.
- **Verdict (raw line 4):** `REVISE`. The review has one revise finding (1)
  and seven notes (2–8), with no blocking finding.
- **Stopping rule, set in `REVIEW-BRIEF.md` §"Round 2" before the round
  ran.** A notes-only round clears the bytes it read. Any other verdict
  leaves them uncleared: the package is not edited, no round 3 is
  dispatched, and the findings go to the owner.
- **Applied here:**
  - Nothing in the package was edited after the review. Every finding below
    is **open**, with a proposed repair for a later version.
    *(Superseded 2026-10-14: under the owner's direction of that day, all
    eight were repaired once in a new version; see "Repairs (2026-10-14)"
    below. The sentence stands as what was true when this record was
    written.)*
  - No round 3 is dispatched. *(Still true 2026-10-14: the brief now
    prepares round 3, and nothing has dispatched it.)*
- **Status: not cleared.** Scope A item 3 offers a package only after a
  round that returns CONFIRM, or CONFIRM WITH EXCEPTIONS with notes only.
  This version is not offered for sign-off. It goes to the owner as P-86.
  The drafter recommends packet Q1 *Revise*: one new version repairing all
  eight findings, then one fresh round.
- **Figures** [Observed]. These were re-derived at the reviewed commit by
  `scripts/build_pwb_class_granular_extraction_amendment.py --check`: 11
  proposed subjects, 5 patched; 17 requirements and 54 scenarios. The
  manifest file's sha256 is the one on raw line 3, recomputed by
  `git show 1701c88f:<manifest> | sha256sum`.

Reviewed record: docs/reviews/R-PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-2-RAW.md

## Dispositions

### 1 — rule provenance is normative over rule names the spec never binds (revise)

**Accepted, open.**

- [Observed at `1701c88f`] The signed spec says only that the source-path
  population "is closed by four rules" (spec line 68); it names none of
  them.
- [Observed] The code's `SOURCE_RULES`
  (`packages/three-surface-poc-core/src/project-shape-manifest.ts` line 71)
  lists five rules: `root-index`, `pillar-index`, `pillar-named-file`,
  `baseline-spec-tree` and `roster-tree`.
- The provenance oracle therefore cannot be decided for the root index
  source without judgment.

Proposed repair: bind each rule name to its numbered rule in the reader
definitions, and state which rule admits the root index and each pillar's
index file. Alternatively, scope the provenance obligation to the four
rules' sources.

### 2 — the failing-class scenario omits the source's own denominator (note)

**Open.** Proposed repair: add an AND line asserting that the source's own
item denominator is Unknown and that the source is shown as partially
extracted.

### 3 — signed unreadable-class text changes meaning unannounced (note)

**Open.** Proposed repair: in the delta, name the reinterpretation of the
unchanged sentence "each source any of its rows names fails as a source in
which a class fails" and of the signed scenario "Loaded profile names a
shape outside the vocabulary". Under the new exactness rule, the source's
other classes keep their items.

### 4 — "below" excludes the shared heading rule above it (note)

**Open.** Proposed repair: write "Wherever these heading rules, a shape or
a key form fails the source", or move the sentence above the shared rule.

### 5 — packet question 4 understates the recommended arm's reach (note)

**Open.** Proposed repair: say that a loaded profile's list or table row
naming two or more level-2 headings would flag every undeclared level-2
heading in its section, and that Butlers' written grammar has no such row.

### 6 — selftest expectations partly unpinned; no manifest or coverage mutant (note)

**Open.** Proposed repair: give the four named mutants their own phrase in
the expected finding, and add selftest mutants for the manifest-row and
contract-coverage predicates.

### 7 — "the root index was not read" is undefined when it reads but fails its grammar (note)

**Open.** Proposed repair: define "read" as the root index's body read and
its PWB-REQ-004 grammar admitted, or state the other choice, and say
whether baseline-spec and roster counts carry the qualification in that
case.

### 8 — residual 5 is filed under an [Observed] list of signing-change tasks (note)

**Open.** Proposed repair: move residual 5 out of "Residuals the signing
change must carry" into its own "Open owner question" line that cites
packet question 6.

## Repairs (2026-10-14)

Under the owner's direction of 2026-10-14 (relayed to the drafting session
by the lead session; no decision record holds it yet): one new version
repairing all eight findings, then one fresh round. The repairs were made
once, over `main` at `8f1fbec7`, on branch `candidate/p86-round2-repairs`.
Proposed bytes changed only in `spec.md.patch` and `design.md.patch`;
`GOVERNING-DEPENDENCIES.md.patch` and the manifest were regenerated by
`build_pwb_class_granular_extraction_amendment.py --write`. **The repaired
bytes are unconfirmed, pending round 3.**

| Finding | Repair |
|---|---|
| 1 (revise) | Hunk 1 now binds five rule names to the four signed rules: rule 1 admits the root index itself as `root-index` and each named pillar root's index file as `pillar-index`; rule 2 `pillar-named-file`; rule 3 `baseline-spec-tree`; rule 4 `roster-tree` (with its `MANIFESTO.md`). A loaded profile's tree population names its source by its `pathPattern`. The flag values are restated by rule number; "the pillar rules … admit none" becomes "the first rule then admits only the root index itself, and the second admits no source"; the third scenario names the root index's own rule. The design gains a rule-names bullet. The delta names the root-index-under-rule-1 reading and the alternative not taken (scoping provenance to the rules' named sources). [Observed] The five names equal `SOURCE_RULES` at `8f1fbec7`, `project-shape-manifest.ts` line 71. |
| 2 (note) | "A failing class keeps its siblings" gains: AND the source's own item denominator renders Unknown, and the source is shown as partially extracted with each class's outcome. |
| 3 (note) | The delta's part 1 gains "Signed text whose meaning changes without a byte changing", naming the unreadable-class sentence and the scenario "Loaded profile names a shape outside the vocabulary"; "What explicitly does NOT change" points to it. |
| 4 (note) | Hunk 2 now reads "Wherever the shared rules above, or a shape or key form below, fail the source, the failure fails the class whose row it reads, in that source". |
| 5 (note) | Packet question 4's recommended arm now says that a loaded profile's list or table row naming two or more level-2 headings would flag every undeclared level-2 heading in its level-1 section or file, and that Butlers' written grammar has no such row. |
| 6 (note) | The four named mutants each expect their own phrase. New selftest mutants: one character of the spec manifest row (the manifest predicate, now its own `manifest_findings`), a contract-coverage clause count changed from 324 to 325 (the generator's own `--check`), and five for the repaired text. Rule 6 was run on the new ones: with their phrases removed from the required lists, or the manifest or coverage predicate stubbed to pass, each fails. |
| 7 (note) | Hunk 1 defines read: the root index is read when its body is read (present at the revision, admitted, within its resource limits). A body that reads but whose grammar fails is still read, and neither a pillar-root naming failure nor a PWB-REQ-004 root-grammar failure qualifies a rule 3 or rule 4 count. The reading is put to the owner as new packet **question 7**, with the other arm. |
| 8 (note) | Residual 5 left "Residuals the signing change must carry"; it is now an "Open owner question, not a signing-change task" line citing packet question 6. |

- **Left for the owner:** packet question 7 (the read definition). The
  rule-1 reading in finding 1 is named in the delta, not asked.
- **Figures** [Observed], by `--check` after the repairs: 11 proposed
  subjects, 5 patched; 17 requirements and 54 scenarios (unchanged: the
  repairs add no scenario). `--selftest`: 39 structure mutants, the
  manifest row and the contract-coverage count, patch drift, an
  unclassified sibling, the pending patch population and the two order
  fixtures all fail closed.
