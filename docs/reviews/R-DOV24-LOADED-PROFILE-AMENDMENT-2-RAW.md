# R-DOV24-2 — confirmation review of PR #123
Verdict: REVISE
Reviewed commit: 1395d44a0d02a788d543ab7ae5ebc5b330d6611c
Manifest sha256: 1ff8665adcb9236cb07d1bdcafda5b1766ca3073bd8ee0f9ebc1f64b1c6c3fd7

Reviewer: independent confirmation review (round 2), read-only, fresh
detached worktree at 1395d44; nothing edited in the subject tree, nothing
pushed. Candidate package; binds nothing; nothing here claims adoption
(VIS-4).

**Correction to the brief's head digest.** The brief gave
`65dc74817721dc663077f0bba89303b36f5222b32c75d2f03d76eae36d51675c`. That is
the sha256 of the manifest *file*
`PWB-LOADED-PROFILE-AMENDMENT-MANIFEST.txt` [Observed, `sha256sum`]. The
manifest's single *row* — the proposed-bytes digest of the subject, which is
the act argument per the manifest's own header ("the row hashes the PROPOSED
bytes") — is `1ff8665a…c6c3fd7`, and I re-derived it independently (below).
The head above carries the row digest. A recorder that expects the file
digest would refuse this head; the brief should name which one it wants.

## Commands run and outputs read

Merge-base with origin/main: `08d4d02` (= origin/main at review time) [Observed].

1. Manifest re-derivation, independent of the builder [Observed]:
   `git archive 1395d44` into a scratch dir; `git apply` the `.18` patch,
   then this package's `proposed/…json.patch`; `sha256sum` the subject →
   `1ff8665adcb9236cb07d1bdcafda5b1766ca3073bd8ee0f9ebc1f64b1c6c3fd7`, equal
   to the manifest row; the result parses as JSON.
2. `python3 scripts/build_pwb_registry_loaded_profile_amendment.py --check`
   → exit 0, ".18 pending: current bytes + .18 patch …" [Observed].
3. `… --selftest` → exit 0, "190 predicates … all fail closed" (Node
   v24.6.0) [Observed].
4. Three states, in a scratch copy of the tree [Observed]:
   - `.18` pending: `--check` and `--selftest` pass (1–3 above).
     `--apply --at-adoption` refuses: "the .18 act has not been applied",
     exit 1; `--apply` without `--at-adoption` exits 2.
   - `.18` applied (its own builder's `--apply --at-adoption`): `--check`
     exit 0 (".18 adopted: current bytes"); `--selftest` exit 0.
   - This package applied (`--apply --at-adoption`): subject sha256 =
     `1ff8665a…c6c3fd7`; `--check` exit 0 ("this package adopted: current
     bytes with this patch reversed"); `--selftest` exit 0; a second apply
     refuses ("already carries this package's bytes", exit 1).
5. `python3 scripts/check_governance.py` → "32 OK, 20 WARN, 0 FAIL (52
   checks)". The WARN set equals base `08d4d02`'s, except that my base
   archive lacked `.git` and so added one CG-11 git-unavailable WARN there
   [Observed].
6. `python3 scripts/check_governance.py --selftest` → "265 fixtures, 0
   failing" [Observed].
7. `python3 scripts/check_docs_review_campaign_partition.py` →
   "total=246 assigned=246 raw=221 other=25 unmatched=0 overlaps=0"; row
   "P-74 loaded-profile registry gate 1 2026-09-27" [Observed].
8. IMPACT-LEDGER counts re-derived at `08d4d02` with
   `git grep -l -w -F -e <name> 08d4d02 -- | wc -l` (second method to the
   ledger's own sweep): `companions` 16, `relativePath` 14, `rootIndex` 12,
   `pillars` 29, `sourcePopulation` 6, `CATALOG_HEADINGS` 8,
   `observationGrammar` 17, `registryVersion` 8, `observerVersion` 39,
   `rootIndexRequired` 5, `rootIndependent` 0; every new key and shape name
   (`classGrammar`, `containerShapes`, `sourceGrammarSemantics`,
   `sharedReadingRules`, `pillarRootLinks`, `extractionBindings`,
   `top-level-decimal-list`, …) 0. All equal the ledger's figures
   (IMPACT-LEDGER.md:62-66, 87-93) [Observed].
9. Rule-6 mutation run: my harness
   (`scratchpad/mut/mut.py`, 164 lines; runs `structure_findings` →
   `spec_findings` → `code_findings` → `behaviour_findings` on a mutated
   copy of the proposed entry; output `scratchpad/mut/run2.log`) over 55
   mutants: the 17 still-applicable round-1 mutants plus variants (M1–M18),
   23 new single-field mutants (N1–N23) and 10 cross/extraneous-field
   mutants (X1–X10). 47 killed, 8 survived [Observed]. Survivors and their
   exact mutations (subject: proposed entry at `1ff8665a…`, commit
   `1395d44`):
   - N2 `row(g,'success-criterion',source='vision.md')['container']='top-level-decimal-list'` (old `top-level-list`)
   - N3 same on `source='v1.md'`
   - N17 `row(g,'catalog-entry')['itemKey']=ITEM_KEY_SENTENCES['principle']`
   - N22 `row(g,'roster-identity')['itemKey']='the fixed key'`
   - X3 `row(g,'baseline-spec')['itemKey']='the fixed key'`
   - X4 `row(g,'design-contract')['column']='Path'` (field added)
   - X5 `row(g,'project-account-section','architecture')['heading']={'level':2,'text':'Non-Negotiable Rules'}` (field added)
   - X6 `row(g,'principle')` gains `table='x'`, `field='y'`
   Round-1 M4 (principle container → `top-level-list`) is still killed only
   incidentally — by "container shape declared and never used" — but my
   swap X1 (principle ↔ vision-success containers) is killed behaviourally.
10. N8 comparison (PR #124 at `c103523`): all 9 container-shape sentences
    and 7 item-key sentences appear in N8's `spec.md.patch` added lines; 7
    shapes and 4 keys verbatim, the rest verbatim after stripping Markdown
    backticks only [Observed].
11. Import check: `project-shape-observation.ts:25-43` imports only
    `node:child_process`, `node:crypto`, `body-read-authority` (type),
    `content-classification` (type), `resource-ledger`, `git-tree` and
    `project-shape-manifest`; `project-shape-manifest.ts:27-36` imports
    only `node:crypto` and `git-tree`. Neither imports
    `project-shape-extraction.ts` [Observed].

## Round-1 resolution

| Round-1 | Disposition (packet line) | Round-2 result |
|---|---|---|
| R1 revise | Fixed (OWNER-DECISION-PACKET.md:231) | **Partially resolved.** All 17 applicable round-1 mutants killed (M4 incidentally). But the disposition's claim "each row's heading, level, source and key are now bound behaviourally or structurally" is false: 8 new wrong versions survive (new finding D1). |
| R2 revise | Fixed (:232) | Resolved in substance; sentences match the code except for note D5's omissions. |
| R3 revise | Fixed (:233) | Resolved: `sharedReadingRules` lists the shared rules. |
| R4 revise | Fixed (:234) | Resolved: the pillarRootLinks sentence states links read after the table, and two roots make the pillar Unknown; the probe on ambiguous roots passes; X10 (sentence edit) killed. |
| R5 revise | Fixed (:235) | Resolved as to `.20`/`.18`. Residual attribution form: note D4. |
| R6 revise | Fixed (:236) | Resolved: `rootIndependent` 0 hits in package and builder; Q9 and IMPACT-LEDGER.md:145 disclose P-82 Q4 / M15's `rootIndexRequired`. |
| R7 revise | Fixed (:237) | Resolved: all three states pass (command 4). |
| N1 note | Fixed (:238) | Resolved: counts re-derived by a second method, all equal (command 8). |
| N2 note | Fixed (:239) | Resolved: wording gone. |
| N3 note | Fixed (:240) | Two readings are given, but the question itself attributes a recorder's sentence to the owner: new finding D3. |
| N4 note | No change (:241) | Agreed. |
| N5 note | Fixed (:242) | Resolved: every row uses a `heading` object; the level is range-checked. |

## New findings

### D1 — revise — per-row shape and item-key forms are not bound; 8 wrong versions survive

[Observed] `behaviour_findings` probes each container shape once
(`done_shapes`, scripts/build_pwb_registry_loaded_profile_amendment.py:1067,
1074-1075) and each item-key form once (`done_forms`, :1068, :1142-1143),
and `_form()` (:754) keys the form by the itemKey *sentence*. So:

- N2/N3: a success-criterion row relabelled `top-level-decimal-list`
  survives. The witness is built from the profile as a decimal list, which
  the code (`topLevelListItems`, numbered or bulleted) also accepts, and the
  shape's probes ran on the principle row. The mutated entry would declare
  that bulleted success criteria fail; nothing notices.
- N17: the catalog row given the principle's itemKey sentence (bold only,
  no dash rule, no code-span alternative) survives: the form is already
  "done" by the principle row, so no catalog-form probe runs, and the
  witness's bold-plus-dash items satisfy both.
- N22/X3: the roster and baseline rows given "the fixed key" survive: for
  `tree-path` and `toml-table-field` the prediction ignores the itemKey.
- X4/X5/X6: fields a shape does not read (`column` on a
  `first-table-rows` link row, `heading` on `every-level-2-section`,
  `table`/`field` on a list row) are accepted. X5 is a substantive false
  claim — "architecture reads under 'Non-Negotiable Rules'" — that
  structure, spec, code and behaviour all pass.

`structure_findings` (:389) checks only that every declared shape is used
somewhere (:515-517), not which fields each row may carry or which shape and
key form each row's source and class admit.

This contradicts the R1 disposition (packet :231, "each row's heading,
level, source and key are now bound behaviourally or structurally") and the
brief's criterion 1 ("… and shape"). Repair options [Inferred]: run the
shape and form probes per row, not per shape/form; pin each row's
(class, source) → (container, itemKey form) as the headings are pinned; and
reject fields not read by the row's shape. Put N2, N3, N17, N22, X3–X6 in
`--selftest`.

### D2 — revise — the named proof cannot witness most of the new fields

The entry's scope sentence (builder :189-193; proposed patch :341) says
loading the fields "must reproduce the current source manifest and
observation digests byte for byte". SEMANTIC-DELTA.md:168-170 calls "Limb
1's regression oracle (reproduce today's manifest and observation digests
from the profile)" "the proof"; OWNER-DECISION-PACKET.md:69-71 calls it
"the full proof".

[Observed] Neither the observation module nor the manifest module imports
`project-shape-extraction.ts` (command 11); extraction is consumed by
`project-shape-model.ts` and `synthetic-corpus-coverage.ts`. [Inferred] So
the manifest and observation digests are functions of `rootIndex`,
`pillars`, `sourcePopulation` and bindings only; they cannot change when
`classGrammar`'s headings, item keys or `containerShapes`/
`sourceGrammarSemantics` are wrong. An oracle that reproduces them proves
nothing about those three keys, which are most of the patch. The claim must
either name an extraction-level witness (the extracted item set per source,
or the model/claim output that consumes it) or be narrowed to the keys the
two digests actually cover — and Q2's recommendation ("perform this act
only once limb 1 has proven the profile reproduces today's digests", packet
:150-153) inherits the same gap.

### D3 — revise — Q3 and the Warrant attribute the recorder's reading to the owner

POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:53 heads its columns
"Row | Ruled | What it means | Applied by". In row P-74 (:64) the *Ruled*
cell is:

> **A** — Q1 ride the existing act for slices 1, 3, 4, 6, 7, hold 2 and 5;
> Q2 one registry-entry amendment act before slice 5's fifth limb only, the
> first four limbs thread a profile parameter with current constants as
> default; …

Both "Slice 5's fifth limb waits for the registry act" and "The consent
record, the registry entry and PWB-REQ-005 are edited on no arm" are in the
*What it means* cell — the recorder's reading, not the owner's answer
[Observed].

- SEMANTIC-DELTA.md:129-132 quotes the Ruled text correctly, then continues
  "and in the same row: 'Slice 5's fifth limb waits for the registry act'"
  as part of the Warrant, and :134-139 "The same row also says 'The consent
  record … edited on no arm.' Read literally that forbids this package's
  subject … The owner decides the reading". "[Observed, quoted from row
  P-74]" is literally true but places recorder prose in the owner's
  warrant.
- OWNER-DECISION-PACKET.md:155-169 (Q3) asks the owner "How should P-74's
  sentence … be read? … Please say which you meant." The owner did not
  write that sentence; the verbatim answer is arm A as presented. The
  question should say the sentence is the recorder's reading of arm A, and
  ask whether that reading is right — or drop the conflict, since the Ruled
  cell has no "edited on no arm" clause at all.

### D4 — note — owner attributions quote option text, not the verbatim answer

- Landing order: OWNER-DECISION-PACKET.md:107-109 ("**What you ruled.** …
  `.21` → `.30` → `.22` → lane B") and SEMANTIC-DELTA.md:28-30 ("the owner
  has ruled only `.21` → `.30` → `.22` → lane B"). The record's verbatim
  answer cell (POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md:114)
  is "Readiness order, lane B last (Recommended)"; the arrows are the
  option as presented (:116-118). Substance correct; quote the answer and
  cite the option text as what it selected. The packet's "four
  specification-touching packages" (:108) also differs from the record's
  question, "lane B and the three spec-touching packages".
- Q8 (OWNER-DECISION-PACKET.md:186-188) says "You ruled 'one registry act,
  not two'". That phrase is at P68-P83 record :75, under "## Cross-cutting
  readings this record fixes" (:73) — the recorder's section. The substance
  is supported by P-72's Ruled cell (:60, "Q2 mint
  `maxBriefingResponseBytes` under a superseding registry act, the fold-in
  ruled now"); cite that instead.

### D5 — note — shape and key sentences omit four behaviours of the code

Checked against `project-shape-extraction.ts` [Observed]:

- `headingMatch` (builder :194-200) says "an ATX heading (one to six #
  marks, then a space or tab)"; the regex (:156) is anchored at column 0,
  so an indented `   ## x` is not a heading. Not stated.
- The design-contract key is trimmed and NFC-normalized (:484-486); the
  itemKey sentence says only "the link text of the first cell".
- The TOML `name` value is trimmed and NFC-normalized but double-quoted
  escapes are not decoded (:569); the roster sentences don't say so.
- Catalog items carry `context` = heading text and the result carries
  `catalogHeadings` (:442-459); topology items carry `context` = ordinal
  (:519). No field or shared rule states the context output.

Since these sentences are shared verbatim with N8 (command 10), any repair
must land in both packages in the same form.

## Criteria summary

1. Round-1 findings: R2–R7, N1–N5 resolved; R1 partially (D1).
2. Sentences vs code: largely exact; D5 notes.
3. Tooling: `--check`/`--selftest` pass in all three states; manifest
   re-derived; governance 0 FAIL; selftest 265/0; partition clean.
4. Rule-6: 47/55 killed; 8 survivors (D1).
5. rootIndependent / P-82 Q4 overlap: disclosed (Q9, ledger :145).
6. Owner attribution: D3 (revise), D4 (note).
7. VIS-4: no adoption claim found [Observed]. Python `re` sweep over the
   package's 4 `.md` files: `\b[0-9a-f]{64}\b` → 0 hits in each;
   `(?i)\b(is|was|now) (accepted|adopted)\b` → 1 hit, IMPACT-LEDGER.md:145,
   the conditional "if M15's recommended arm is adopted", which claims
   nothing.
