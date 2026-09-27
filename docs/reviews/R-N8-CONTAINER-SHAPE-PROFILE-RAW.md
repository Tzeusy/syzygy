# R-N8 — independent review of PR #124
Verdict: REVISE
Reviewed commit: a7eda10d3bb71e86679793cc17d5afafc5509012
Manifest sha256: 3eb181c44ca29d57f31f2804caaebcc8b3deb9f81d79391395a04e4bc299fca6

Reviewer: fresh-context, read-only reviewer dispatched by the team lead,
2026-09-27. Subject: `.syzygy/governance/contracts/candidates/pwb-container-shape-profile-amendment/`
(bead `syzygy-u05.8`, N8), its builder
`scripts/build_pwb_container_shape_profile_amendment.py`, and the
`scripts/check_governance.py` registration diff; base `origin/main` 23b486c.
Worktree at the reviewed commit; nothing in the main checkout or any branch
was edited, nothing pushed.

Recording note: `REVIEW-BRIEF.md` says to record the raw under
`docs/reviews/`. The lead's dispatch directed this file to the session
scratchpad instead; the lead's instruction was followed. Retention under
`docs/reviews/` with a `-RAW.md` basename and a campaign-partition row is the
lead's step.

## Commands run and output read

1. Manifest digest, two methods: `sha256sum` and Python `hashlib` over
   `PWB-CONTAINER-SHAPE-PROFILE-MANIFEST.txt` both give
   `3eb181c44ca29d57f31f2804caaebcc8b3deb9f81d79391395a04e4bc299fca6`,
   equal to the two copies in `OWNER-DECISION-PACKET.md` (lines 22 and 121)
   [Observed].
2. Manifest rows, two methods: (a) the builder's own `proposed_bytes`;
   (b) independently, `git archive` of the base subject, `git apply` of the
   three patches, `sha256sum` of every file. All 11 rows match on both
   [Observed]. The subject directory tracks 15 files; the manifest omits
   `contract-coverage-parts/*.md` (3) and `tasks.md` — the same 11-row
   population every sibling PWB manifest uses [Observed].
3. `python3 scripts/build_pwb_container_shape_profile_amendment.py --check`
   → "matches 11 proposed subjects (3 patched, 8 unchanged); 9 shapes,
   14 profile rules, 6 PWB-REQ-002 rules, 2 scenarios, … 12 declared
   sibling-composition outcomes verify", exit 0 [Observed].
4. Same builder `--selftest` → "74 mutants killed", exit 0; fixture list
   hand-counted at 74 (rule 4 denominator) [Observed].
5. `python3 scripts/check_governance.py` → "32 OK, 20 WARN, 0 FAIL
   (52 checks)", exit 0. CG-7d subject line: "SIGN OFF PWB CONTAINER-SHAPE
   PROFILE AMENDMENT — 1 quotation(s), 0 finding(s)"; CG-7e OK over 39
   files [Observed].
6. `python3 scripts/check_governance.py --selftest` → "268 fixtures,
   0 failing" [Observed].
7. `python3 scripts/check_docs_review_campaign_partition.py` →
   total=241 assigned=241 unmatched=0, exit 0 [Observed].
8. `npx -y openspec validate polaris-project-wide-butlers-model --strict`
   (openspec 1.9.0; not pinned in `package.json`) on a scratch copy with the
   three patches applied → "Change … is valid"; `--json` 1 passed, 0 failed
   [Observed].
9. `syzygy-dov.24` (origin/agent/tier4-dov24, 31305bc) builder `--check`
   with N8's `spec.md.patch` applied on top → passes, confirming the
   ledger's Table 4 composition claim for that sibling [Observed].
10. Diff of base vs patched `spec.md`: hunks only at base lines 30, 120,
    128, 131, 139, 147 — reader definitions and PWB-REQ-002; the nine
    Butlers class bullets are byte-identical [Observed].
11. Reviewer rule-6 mutations of the builder (applied to the proposed
    `spec.md`, run through `requirement_findings`):
    - KILLED: key forms "eight" → "nine".
    - SURVIVED (9): trailing grammar paragraph NFC → NFD; "never produces
      a partial item set" → "may produce"; PWB-REQ-001 body SHALL → MAY;
      the source-population bullet; REQ-002 oracle "must produce the same
      identities and D" → "may produce different"; scenario-1 WHEN →
      "any project"; scenario-2 THEN negated with the checked phrase kept;
      falsifier "partial population" removed; "Each admitted item SHALL be
      in exactly one" → MAY; "A source whose item population cannot be read
      SHALL" → MAY [Observed]. See N2.
12. Reviewer rule-6 mutations of the CG registration (scratch worktree,
    reverted with `git checkout` after each):
    - M1 both digest copies changed → CG-7d and CG-7e FAIL (killed).
    - M2 phrase-form copy only → CG-7d FAIL (killed).
    - M3 bare-digest copy at packet line 22 only → exit 0, SURVIVED; the
      same holds for the sibling missing-currency packet's line 22, so this
      is checker-wide and pre-existing. See N3.
    - M4 manifest byte edited → CG-7d and CG-7e FAIL (killed).
    - M5 `ACT_DIGEST_COPY_FILES` row removed → CG-7e FAIL (killed).
    - M6 `_act_subjects` entry removed → full check exit 0 even with a
      stale digest, but `--selftest` FAILs ("CG-7e unperformed PWB
      container-shape act watches the packet copy…") (killed by selftest).
    - M7 activation call removed → selftest passes; the activation is inert
      until an act record exists, which is by design [Observed].
    No `PWB_SUCCESSOR_CHAIN` link is added — correct for an unperformed
    candidate [Observed].
13. Impact-ledger sweeps, base 23b486c, denominator 1,540 tracked files
    (4 undecodable), Python `re` plus `git grep -F` [Observed]:
    - `PWB-REQ-002` literal: 48 files by both methods. Run/continuation
      forms (`PWB-REQ-001/002/…`, `PWB-REQ-00[0-9]`-style lists, regex
      `PWB-REQ-\d{3}(?:[/, ]+(?:and )?\d{3})+` with membership of 002) add
      12 files; a range form (`PWB-REQ-001..005`/`001–022`) adds 1: 61 total.
    - Nine shape names: `heading-section` 2 files, the other eight 0;
      `containerShapes` 0 — match the ledger.
    - "project profile": 7 files single-line, 8 when a line wrap is joined
      (the extra is a historical rev9 RFC-0005 copy wrapping
      "per-project\nprofile").
    - "key form" 1, "container shape" 11 — match the ledger.
14. Shape sentences checked against
    `packages/three-surface-poc-core/src/project-shape-extraction.ts`
    (`sectionOf`, `oneHeading`, `extractProjectAccountSections` ~359,
    `extractPrinciples` ~405, `extractSuccessCriteria` ~423,
    `extractCatalogEntries` ~438, `headedTable` ~462, `ORDINAL_H2`,
    craft-policy `File` column, roster `[butler]` table) and against
    `syzygy-dov.24`'s proposed registry `containerShapes`/`classGrammar`.
15. Decisions read at source: `POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
    §6 (and lines 157-158); the 2026-09-23 owner-values record §6;
    `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md` line 64 (P-74 Q2)
    and the P-82 (M15) ruling; RFC 0005 `README.md` line 86 in both the
    accepted and candidate copies.
16. Authority-word sweep over the package: only candidate / "binds
    nothing" banners, "owner-adopted registry entry" wording, the baseline
    commit, and the two manifest-digest copies (marked not offered). Nothing
    is labelled accepted or adopted on the owner's behalf [Observed].

## Findings

### R1 — revise [Observed]: the profile slot cannot express Butlers' own grammar

`proposed/spec.md.patch` line 32 (profile bullet, patch lines 29-40): "For
each class above, the observed project's profile … declares the source, the
heading or tree rule, exactly one container shape and exactly one key
form." One source and one shape per class. Butlers' grammar, which the same
patch says Butlers' profile "declares exactly" (patch lines 41-42), needs
more than that per class:

- project-account-section: three sources and two shapes (`vision.md`
  heading-sections; `architecture.md` every H2 joined into one item;
  `v1.md` two headings joined into v1-scope plus v1-success) —
  `extractProjectAccountSections` ~359.
- success-criterion: two sources with different key prefixes (`vision:`,
  `v1:`) — `extractSuccessCriteria` ~423.
- craft-policy: needs a `File` column selector — `headedTable` path.
- roster: needs a TOML table (`[butler]`) and field (`name`).
- catalog: nine named H3 headings.

`syzygy-dov.24`'s registry models exactly this with 15 per-row
`classGrammar` entries (6 rows for project-account-section, 2 for
success-criterion, `column: File`, `table`/`field`, a `headings` array).
Under N8's own schema, scenario 1 ("identities and D equal", patch lines
89-95) is unsatisfiable. Repair: make the profile rule per source row
(class → one or more rows, each with source, locator, shape, key form, and
the shape's parameters), and align names with dov.24.

### R2 — revise [Observed/Inferred]: conflict with the ruled P-74 Q2 design; Q7 already ruled

Patch lines 38-39: a missing rule "makes its sources' item denominators
Unknown; the observer never substitutes a built-in rule", and the falsifier
(patch line 81) fires on a rule "replaced by a built-in one". P-74 Q2
(`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:64`) ruled "one
registry-entry amendment act before slice 5's fifth limb only, the first
four limbs thread a profile parameter with current constants as default".
Current constants as default is a built-in rule in the sense the falsifier
names. Until Butlers' registry entry carries a profile, the strict text
makes every Butlers class Unknown, and the code the owner ruled for
violates it. `SEMANTIC-DELTA.md:166-169` and packet Q6
(`OWNER-DECISION-PACKET.md:81-87`) call this "conforming … only by
coincidence of its constants" — under the new text it does not conform
[Inferred]. The package cites neither P-74 Q2 nor where Butlers' profile
lives before the dov.24 act. Packet Q7 (`OWNER-DECISION-PACKET.md:88-92`,
"Does the registry need ride `syzygy-dov.24`'s act?") is substantially
already answered by P-74 Q2's "one registry-entry amendment act"; the packet
should cite the ruling and ask only what remains open. Repair: state the
interim (constants as the declared Butlers default until the registry act,
disclosed), or scope the no-built-in sentence to projects whose profile is
loaded, and quote P-74 Q2.

### R3 — revise [Observed]: owner-attributed landing order quotes more than was ruled

`OWNER-DECISION-PACKET.md:100-101`: "Your order is `.21` → `.30` → `.22` →
lane B, then `.20` and `.18`." The owner ruled `.21` → `.30` → `.22` →
lane B (owner-values record 2026-09-23 §6; the sitting's §6 at lines 157-158
says N8 does not change that order). ".20 and .18" is not in either ruling.
`IMPACT-LEDGER.md:114` likewise lists `.20` among "Specification acts that
land first". Repair: quote only the ruled order, and label the `.20`/`.18`
placement as the drafter's proposal [Inferred].

### R4 — revise [Inferred]: VIS-2 hole when a class's rule is missing

Patch lines 38-39 make "its sources' item denominators" Unknown — but the
missing rule is what names the class's sources. With no rule, no source is
attributed to the class, so nothing is made Unknown and the class/category
can render an empty set, i.e. 0. VIS-2: "No evidence means Unknown, not
success." Repair: a class with no admissible rule makes the class's (and its
category's) denominator Unknown, not its sources'. Add a scenario for the
missing-rule case distinct from scenario 2's malformed-rule case (patch
lines 97-103).

### R5 — revise [Observed]: shape sentences looser than the code; exactness paragraph now Butlers-only

The nine shape sentences (patch lines 10-28) paraphrase dov.24's and omit
behaviour the code enforces, so another project's reading is under-specified
(VIS-7 determinism):

- decimal / top-level lists: an empty list is malformed
  (`extractPrinciples` ~405, `extractSuccessCriteria` ~423) — not stated.
- first-table-rows: no table under the heading is malformed; heading matched
  at any level (`headedTable` ~462) — not stated.
- ordinal-level-2: zero ordinal H2s → missing-heading (Unknown); `ORDINAL_H2`
  is `/^(\d+[a-z]?)(?![\w])/` (single letter, non-word lookahead) — not
  stated.
- every-level-2-section: code joins every H2 section, heading text included,
  into one item; zero H2 fails. dov.24 says "joined in file order"; N8 drops
  both.
- missing or duplicate heading → Unknown (`oneHeading`) — not stated
  generally.

The base trailing paragraph ("Heading levels/text … exact. Unicode is
NFC-normalized; no case folding … never produces a partial item set", base
spec lines ~57-61) now sits inside the Butlers-only bullet after the patch,
so a non-Butlers profile loses exactness, NFC and no-partial-set.
`SEMANTIC-DELTA.md:139-142` itself says the sentences "were not re-checked
here". Repair: hoist the exactness paragraph to cover every profile, and
state each shape's failure conditions.

### N1 — note [Observed]: Butlers' written-grammar oracle compares identities only

Patch lines 67-69: the profile path "must produce the same identities and
D; for Butlers, both also apply the grammar written in these reader
definitions and must produce the same identities;". The written-grammar leg
omits D, while scenario 1 (patch lines 89-95) requires identities and D
equal. Unknown-vs-0 is exactly a D difference (VIS-2); add "and D".

### N2 — note [Observed]: builder guards phrases, not unchanged text

Nine reviewer mutants survived `--check` (command 11), including the
trailing grammar paragraph and SHALL→MAY in PWB-REQ-001/-002 bodies. The
"retained Butlers grammar" check covers the nine class bullets but not the
trailing paragraph. Current bytes were verified directly by hunk diff
(command 10), so no defect today; the builder would not catch a later one.
Suggest: hash-pin every base region the patch does not intend to touch.

### N3 — note [Observed]: bare-digest copy at packet line 22 unguarded

Mutant M3 survived: changing only `OWNER-DECISION-PACKET.md:22` passes both
CG-7d and CG-7e. Same for the sibling missing-currency packet's line 22 —
checker-wide, pre-existing, not introduced by this PR.

### N4 — note [Observed]: ledger misses continuation/range citers of PWB-REQ-002

Literal sweep 48 matches the ledger; continuation and range forms add 13
files (command 13), including a code citer
`apps/three-surface-poc/src/pwb-mutation-sweep-main.ts:226`
("PWB-REQ-001/002/003/004/005/010/012/020/022"), which Table 2 omits (it
lists `pwb-mutation-sweep.ts` only), plus `AGENTS.md` and the opening-band
and machine-view ledgers. The wrapped historical "per-project profile" in a
rev9 RFC-0005 copy is also uncounted. Publish the regex and the forms.

### N5 — note [Observed]: P-82 (M15) overlapping delta not in Table 4

P-82 rules a separate CC-REV-2 delta to PWB-REQ-002, sequenced behind lane
B. `IMPACT-LEDGER.md` Table 4 does not list it as a composing sibling.

### N6 — note [Observed]: warrant paraphrases doctrine (rule 8)

`SEMANTIC-DELTA.md:116-120` states what VIS-2 and VIS-7 "require" without
quoting the clauses. Quote them at source.

### N7 — note [Observed]: key-form list wording

The key-form list gives "the link target basename" without saying it is the
first-cell link of the design-contract table; and the `File`-column key for
craft policies is not named as a key form. Minor precision.

### N8 — note [Observed]: "whole subject"

`SEMANTIC-DELTA.md:21`: "eleven rows over the whole subject". The subject
tracks 15 files; the manifest covers 11, consistent with siblings. Say
"eleven rows over the subject's manifest population".

### N9 — note [Observed]: recording location

See the recording note above; the brief's `docs/reviews/` instruction was
superseded by the lead's dispatch.

## Confirmations (not findings)

- The act phrase is marked not offered; nothing is labelled accepted
  [Observed].
- RFC 0005 `README.md:86` "per-project profile" citation correct in both
  copies [Observed].
- Nine Butlers class bullets byte-identical; openspec strict valid; 12
  declared sibling-composition outcomes verify; dov.24 composition holds
  [Observed].
- Packet questions Q1, Q2, Q4, Q5, Q8, Q9 are genuine and not ruled in the
  records read; Q4 appears in no ruling [Observed]. Q7 — see R2. Q10's
  premise — see R3.
- "Current meaning" quotations in `SEMANTIC-DELTA.md` match the base bytes
  [Observed].
- The §6 quotations at `SEMANTIC-DELTA.md:110-114` match the sitting record
  [Observed].
