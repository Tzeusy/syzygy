# R-DOV24-3 — confirmation review of PR #123
Verdict: REVISE
Reviewed commit: 929100ff7b273a6c6ce93ed8068943ec15de809f
Manifest sha256: 5280846f70b31811e38faffb36c5217c0090fd92ba04f19b763a127b0d105682

Reviewer: independent agent, fresh context, 2026-09-27. Given the package
at `.syzygy/governance/contracts/candidates/pwb-registry-loaded-profile-amendment/`
(REVIEW-BRIEF.md, OWNER-DECISION-PACKET.md, SEMANTIC-DELTA.md,
IMPACT-LEDGER.md, the manifest, `proposed/…json.patch`), the builder
`scripts/build_pwb_registry_loaded_profile_amendment.py`, AGENTS.md
"Verification rules", the observer code in
`packages/three-surface-poc-core/src/project-shape-extraction.ts` and
`project-shape-manifest.ts`, and the two decision records the brief names
(`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`,
`POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`). Worked in a
detached worktree at the reviewed commit; the base is `96ee305` (merge-base,
equal to origin/main at review time).

## Round-2 findings — resolution

| Finding | Resolution | Evidence |
|---|---|---|
| D1 — per-row shape, key form and extra fields unbound | **Resolved for shape, key form and class-row extra fields; one residual gap (F2 below).** | Builder `structure_findings` (lines 414–586) has a per-row field allowlist (`ROW_FIELDS`, `SHAPE_FIELDS`, `FORM_FIELDS`, lines 194–210), requires every needed field, and pins shape, item-key and semantics sentences. `probes()` (1117–1314) runs the shape and key-form probes per row. `--selftest` reports 223 predicates. My own run: 71 effective mutants against the proposed JSON and builder, 59 killed. Every per-row shape, key-form and class-row extra-field mutant on a non-first row of its shape was killed (A1, A6–A17, A19–A21, A27–A31, A57, B1). Survivors are listed under F2, N1 and N2. |
| D2 — digests called proof | **Resolved.** | OWNER-DECISION-PACKET.md:78–88 says the manifest and observation digests are not evidence for `classGrammar`, `containerShapes` or `sourceGrammarSemantics` [Inferred], and marks whether items are compared as [Unknown]. The scope sentence (SEMANTIC-DELTA.md:88, pinned `SEMANTICS["scope"]`) requires every source's extracted items to be reproduced. |
| D3 — gloss column treated as the owner's words | **Resolved.** | Q3 (packet:180–200) and the warrant (SEMANTIC-DELTA.md:131–147) quote only the "Ruled" cell as the owner's and name the gloss as the recorder's. Residual column-attribution nuances for P-82 are in N4 and are notes. |
| D4 — landing order and Q8 attribution | **Resolved.** | The landing order (packet:123–135) quotes "Readiness order, lane B last (Recommended)", matching POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md:114, and cites the option arrows (:116–118) as what it selected. Q8 (packet:218–227) cites the P-72 Ruled cell (P68-P83 record :60) verbatim. |
| D5 — four code behaviours unstated | **Resolved; each one checked against the code.** | Column-0 ATX: `ATX = /^(#{1,6})[ \t]+…/` is anchored at column 0. Design key: `nfc(link[1].trim())`. TOML value: `nfc((n[1] ?? n[2] ?? '').trim())`, with no escape decoding (project-shape-extraction.ts:545–575). Catalog context is the heading text; topology context is the ordinal (`ORDINAL_H2`). The sentences state all four. |

## New findings

**F1 — revise. Criterion 4 is not met at byte level, and the packet's
"Nothing else in the entry changes" is false as written.**
`proposed/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json.patch`
carries three hunks against `.18`'s bytes that are neither a version nor
one of the six added keys:
- patch:25–26 reflows `"questions": ["What currently exists?"],` onto
  several lines;
- patch:36–37 rewrites the literal em dash in
  `"Topology snapshot — where components live…"` as `—`;
- patch:45–46 does the same for `"Runtime behaviour — executed source…"`.

The cause is the builder's serializer. `json.dumps(doc, indent=2)` at
builder:1583, with `ensure_ascii` left at its default of True, re-emits the
whole document. The patch contains no other em dash change, which is
consistent with `.18`'s bytes never passing through that serializer.

REVIEW-BRIEF.md:68–69 states the criterion in bytes: "Only the two versions
and the six added keys may differ from `.18`'s bytes." OWNER-DECISION-PACKET.md:48
says "Nothing else in the entry changes; the builder checks that." The
builder's `unchanged_findings` (builder:371) compares parsed JSON only, so
it cannot see these hunks. Semantically the entry is unchanged: I parsed
`.18`-applied and proposed bytes and found only the six additions and two
version changes.

The owner would be signing a row digest over bytes that rewrite two
precedence-row strings the owner never asked to touch. Neither prior raw
flagged this; the hunks were already present in the round-2 patch.

Repair: either serialize so that `.18`'s bytes are preserved outside the
additions (use `ensure_ascii=False` and insert the keys rather than
re-dumping, then add a byte-level check), or restate criterion 4 and
packet:48 as "parsed values" and name the three reformatting hunks. The
first option changes the row digest and needs `--write`.

**F2 — revise. A rule-6 survivor: the second heading of a two-heading row
is unprobed.** Mutant A4 deletes `level` from `classGrammar[4].headings[1]`
(`v1-scope`, "What v1 Defers"). It passes `--check`'s structure, spec, code
and behaviour stages.

The code fixes that heading at level 2 (`oneHeading(doc, 2,
V1_HEADINGS.defers, cls)`, project-shape-extraction.ts:389). A level-less
heading object means "matches at any level" (pinned `headingMatch`
sentence, builder:222–223). So the mutated entry would declare a looser
reading than the code performs, and nothing catches it.

Why it survives:
- The headingMatch probes use only `headings[0]` (builder:1266–1268:
  `level, text = headings[0]`).
- The witness renders a level-less heading at `level or 2` (builder:968–972).

Controls: the same deletion on `headings[0]` (B4), on row 5 (B5) and on
row 1 (B6) is killed, and changing `headings[1]` to level 3 (B3) or to
another text (B2) is killed.

OWNER-DECISION-PACKET.md:281 (N5) says every row writes `level` "wherever
the code fixes one". That is true of the proposed bytes, but the builder
does not enforce it for this heading, and the packet does not list it among
the pin-only claims (packet:72–76).

Repair: run the headingMatch probes for each entry of `headings`, and add
A4 to `--selftest`.

**N1 — note. Extra keys outside class rows, pillar rows, tree populations
and `rootIndex` pass.** These survived:
- A44: `rootIndex.pillarRootTable` gains a key.
- A46 and B7: an `extractionBindings` row, first or non-first, gains a key.
- A47: `sourcePopulation` gains a key.

The builder comment at builder:190–192 argues that "a field nothing reads
would be a claim nothing tests", but that allowlist covers only class
rows, pillar rows, tree populations and the top level of `rootIndex`. The
proposed bytes carry no such key, and the packet makes the no-extra-field
claim only for rows (packet:63–64), so this is a note. Extending the key-set
checks to those three objects would close it.

**N2 — note. Unread or order-only mutants that survive.**
- A18: a true but redundant `pillar` on `principle` passes. The comment at
  builder:190 says "`pillar` only where two bindings share a source name",
  but that rule is not enforced.
- A60: `roster-identity.field` set to `"name "` (trailing space) passes,
  because the witness writes `name  = …` and `TOML_NAME` allows whitespace
  before `=`.
- Order-only permutations pass, and none changes what the code reads:
  `extractionBindings` (A41), `classGrammar` rows 7 and 8 (A42),
  `treePopulations` (A51) and the `containerShapes` key order (A55).

**N3 — note. Sentence clauses looser or stricter than the code, and not
probed.**
- (a) `first-cell-link-text` (builder:177) says "optionally with a quoted
  title". `LINK` (project-shape-extraction.ts:324) accepts only a
  double-quoted title.
- (b) `toml-table-field` (builder:152–153) says "the field inside any other
  table, is not read". But `TOML_TABLE` (:545) does not match an
  array-of-tables header such as `[[other]]`, so a `name` line after
  `[[other]]` that follows `[butler]` is still read as butler's, or trips
  "name repeated".
- (c) `pillarRootLinks` ("after the table, every root-index link…") can be
  read as positional. `declaredPillarRoots` (project-shape-manifest.ts:365)
  takes links from the whole root-index text, and "after" holds only as
  processing order. No probe distinguishes the two readings.
- (d) Builder-side: rewriting a pinned sentence consistently in the builder
  and the JSON, for example appending "Items may nest." to `top-level-list`
  (B11), survives. The packet admits this at packet:72–74 ("checked only by
  its exact wording being pinned"), so this is not a gap in disclosure.

**N4 — note. P-82 column attribution.** The P-82 "Ruled" cell (P68-P83
record :70) says only "Q4 design the root-independence flags in the same
delta". `PWB-REQ-002`, `.15.1` and "after `.17`" come from the recorder's
"What it means" and "Applied by" columns.
- SEMANTIC-DELTA.md:187–188 labels as [Observed] that "the ruling for P-82
  Q4 puts 'the root-independence flags' in M15's delta to `PWB-REQ-002`
  (`.15.1`)". That attributes recorder placement to the ruling.
- OWNER-DECISION-PACKET.md:231–232 says the "What it means" column places
  the delta "(`.15.1`, after `.17`)". The `.15.1, after .17` part is in the
  "Applied by" column. It is recorder text either way.
- IMPACT-LEDGER.md:145 has the same column nuance.

None of these presents recorder text as the owner's answer, but the
delta's "ruling" wording at :187 comes closest.

**N5 — note. SEMANTIC-DELTA.md:234–239 is stale.** Its "## Review" section
names round 1 only and says "This revision has not been reviewed;
`REVIEW-BRIEF.md` states what round 2 is given." This contradicts the same
file's line 156 ("two independent review rounds each returned REVISE") and
the round-2 raw retained at `docs/reviews/`. Mark it at the sentence, per
the CG-27 lesson.

## Owner-attribution sweep (criterion 7)

- Regex, Python `re`, case-insensitive:
  `\b(rul(ing|ings|ed)|chose|decided|answer\w*|you|your)\b`.
- Population: the four package `.md` files plus the builder.
- Result: 56 hits (ledger 2, packet 36, brief 6, delta 11, builder 1). I
  read every hit.
- Every quotation presented as the owner's matches a "Ruled" cell or the
  verbatim answer at OWNER-VALUES:114.
- No "What it means" gloss or recorder heading is presented as the owner's
  words, apart from the column nuances in N4.

## VIS-4 sweep (criterion 6)

- 64-hex digests over all 6 files in the package directory: one hit, the
  manifest row (`PWB-LOADED-PROFILE-AMENDMENT-MANIFEST.txt:9`). No `.md`
  file carries a digest. I confirmed this with `grep -E` and a second
  method, Python `re` with hex-boundary lookarounds.
- Acceptance wording over the 4 `.md` files and the builder, using
  `(?i)\b(is|was|now|been|are|were|hereby)\s+(accepted|adopted|approved|signed off|in force|binding)\b|\badopted\b|\baccepted\b`:
  25 hits.
  - Every builder hit names a state of the subject, such as "`.18`
    adopted", "this package adopted" or the `ADOPTED` state label.
  - Packet:6 and brief:75 are disclaimers.
  - Packet:270 is review-record prose.
  - Ledger:145 quotes the P-82 cell.
- The heads of the packet and the delta both say "Candidate — binds
  nothing". The patch keeps `"status": "candidate-amendment-no-effect-until-owner-act"`.
- Nothing labels this package accepted or adopted.

## Checks run

1. `python3 scripts/check_governance.py` gave "32 OK, 20 WARN, 0 FAIL (52
   checks)". The WARN set is identical to base `96ee305`, apart from CG-1f
   examining 203 references against base 202, with 0 findings.
   `--selftest` gave "282 fixtures, 0 failing".
2. I ran the builder `--check` and `--selftest` in all three states, from
   the worktree and from a `git archive` copy.
   - (a) `.18` pending: check OK, row `5280846f…`; "selftest: 223
     predicates", exit 0.
   - (b) `.18` applied: same results.
   - (c) This package applied: same results, and the subject sha256 equals
     the row.
   - `--apply --at-adoption` before `.18` refuses with exit 1 ("the .18 act
     has not been applied"). `--apply` without `--at-adoption` exits 2. A
     second apply refuses with exit 1 ("already carries this package's
     bytes").
3. `python3 scripts/check_docs_review_campaign_partition.py` gave
   "total=250 assigned=250 raw=225 other=25 unmatched=0 overlaps=0". The
   P-74 row count is 2 (docs/README.md:97).
4. Independent row digest. From `git archive` of the reviewed commit, I
   applied `.18`'s patch and then this patch with `git apply`, then took
   `sha256sum` of the subject:
   - current `0765f4d5…`;
   - after `.18`, `2356b9ed…`;
   - after this patch, `5280846f70b31811e38faffb36c5217c0090fd92ba04f19b763a127b0d105682`.

   The last equals the manifest row, and the result parses as JSON.
5. Mutants. Harnesses: `mut3.py` (60 mutants, A1–A60) and `mut3b.py` (12,
   B1–B12). Each takes `json.loads(proposed_bytes())`, mutates it and runs
   `unchanged_findings`, `structure_findings`, `spec_findings`,
   `code_findings` and `behaviour_findings` in that order. The unmutated
   base passes all five.
   - A-series: 60 run, 50 killed, 10 survived:
     - A4 (F2);
     - A18 and A60 (N2);
     - A41, A42, A51 and A55 (N2, order only);
     - A44, A46 and A47 (N1).
   - B-series: 12 run, 9 killed, 3 survived:
     - B7 (N1);
     - B11 (N3d, admitted as pin-only);
     - B12, which was void: the sentence contains no "Unknown", so the
       mutation was a no-op. Excluded.
   - Killed, by stage:
     - structure: the class-row extra-field, binding-match, pinned-key and
       unused-shape mutants;
     - spec: B2;
     - code: A37–A40, A43 and B9;
     - behaviour: the rest, including every per-row shape and key-form
       swap on non-first rows (A6–A15, A30, A32, A57) and heading
       level/text changes (A2, A3, A5, A22–A25, A34, A50, A53, B3–B6).
6. Owner-attribution and VIS-4 sweeps: see above.

Totals: 72 mutants run, 71 effective (B12 void), 59 killed, 12 survived.
F2 is the one survivor that loosens a reading the code fixes.
