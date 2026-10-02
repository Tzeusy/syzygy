# R-N8-4 — confirmation review of PR #124
Verdict: REVISE
Reviewed commit: e381e4e0e9c58200ada76c8e8a368e56d670a4ac
Manifest sha256: 2c59453345276366d1a5b7f95dcacc40b199a4edc350072dd564d52aeb11ae82

Reviewer: independent round-4 confirmation reviewer, fresh detached worktree
at the reviewed commit (removed after review). No commit, push or branch edit.
Package: `.syzygy/governance/contracts/candidates/pwb-container-shape-profile-amendment/`.
Builder: `scripts/build_pwb_container_shape_profile_amendment.py`.
"spec:N" is a line of
`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`
after all three `proposed/` patches were applied (`git apply`) to a scratch
copy of the subject. Other file:line references are at e381e4e.

## Commands run and output (at e381e4e)

| Command | Result |
|---|---|
| builder `--check` | exit 0; "matches 11 proposed subjects (3 patched, 8 unchanged); the whole spec equals the current spec with 8 pinned edits; 9 shapes, 8 key forms, 8 vocabulary, 3 key-form, 8 profile, 13 loaded-profile and 4 declared-item rules … 21 PWB-REQ-002 rules, 5 scenarios word for word … 12 declared sibling-composition outcomes verify"; then "shape and key-form sentences hash to syzygy-dov.24's at 1d5966c; scripts/build_pwb_registry_loaded_profile_amendment.py is not in this tree …" |
| builder `--selftest` | exit 0; "selftest: 185 mutants killed — …" |
| builder `--diff` | exit 0; prints the three patches |
| `python3 scripts/check_governance.py` | exit 0; "32 OK, 20 WARN, 0 FAIL (52 checks)"; CG-7d "SIGN OFF PWB CONTAINER-SHAPE PROFILE AMENDMENT — 1 quotation(s), 0 finding(s), 0 performed digest(s)" |
| `python3 scripts/check_governance.py --selftest` | exit 0; "285 fixtures, 0 failing" |
| `python3 scripts/check_docs_review_campaign_partition.py` | exit 0; "total=251 assigned=251 raw=226 other=25 unmatched=0 overlaps=0"; row "N8 container-shape profile gate 3"; `ls docs/reviews \| wc -l` = 251 |
| manifest file digest, `sha256sum` and Python `hashlib` | both `2c59453345276366d1a5b7f95dcacc40b199a4edc350072dd564d52aeb11ae82`; equals OWNER-DECISION-PACKET.md:25 and :202 |
| manifest rows re-derived by my script over the patched scratch copy | 11 rows, 0 mismatches; paths in codepoint order; the subject tracks 15 files, the 4 left out (three `contract-coverage-parts/*`, `tasks.md`) are the ones SEMANTIC-DELTA.md:21-24 and packet :18-21 disclose |
| `openspec validate polaris-project-wide-butlers-model --strict` on the patched copy | "Change 'polaris-project-wide-butlers-model' is valid" |

Worktree `git status --short` was empty after every mutation run.

## Round-3 resolution

| Finding | Status | Evidence |
|---|---|---|
| R-C — unscoped falsifier fired on the conforming interim state | Resolved | Scoped at all four sites: spec:282-283 "or a project other than Butlers with no loaded profile reports a known item denominator"; builder:417-419 (`REQUIREMENT_RULES`); SEMANTIC-DELTA.md:164-168; REVIEW-BRIEF.md:74-75. My revert of the spec clause to the round-3 wording is killed (whole-spec pin, spec:282). Butlers today (no profile declared) trips no falsifier clause [Inferred, clause by clause over spec:276-283]. |
| N-a — "reads" left declared-but-unread falling back | Resolved in the text; see new R-D | spec:137-141 now triggers on "declared" and treats a declared-unread or undeterminable Butlers profile as refused; scenario spec:317-324 renamed "Refused or unread Butlers profile does not fall back"; IMPACT-LEDGER.md:119 updated. The repair opens the conflict with P-74 Q2's sequence recorded as R-D. |
| N-b — no case/scenario for a non-Butlers project with no profile | Resolved | Case spec:259-264 adds it; scenario spec:326-332 "Project with no profile has Unknown item denominators" ("… render Unknown, never zero"). Whole-profile refusal (spec:154-157) now also makes every class and category Unknown. |
| N-c — shared sentences out of step with the code | Resolved as a copy | By my own script, independent of the builder's constant: `SHAPES` and `ITEM_KEY_SENTENCES` read by `ast.literal_eval` from `git show 1d5966c:scripts/build_pwb_registry_loaded_profile_amendment.py` equal this builder's `SHAPES` and the non-`None` `KEY_FORMS` sentences (9 and 7 entries); SHA-256 of `repr((SHAPES, ITEM_KEY_SENTENCES))` there is `64b15eaeed24b510c7d744bdd09f1de4f5989d2c05c9165b3826b8ac226d753d` = `SHARED_TEXT_SHA256` (builder:127). The 16 spec bullets (spec:50-93, 96-119), with line wraps joined, backticks removed and the final full stop dropped, equal dov.24's sentences exactly: 16 compared, 0 differ; dov.24's sentences contain no backtick. The dov.24 builder is unchanged between 1d5966c and 0d1ccc5 (`git log 1d5966c..0d1ccc5 -- <builder>` empty). The link-title (spec:108-110, "in double quotes") and `[[other]]` (spec:89-91) text now matches round 3's code reading. dov.24's N-B/N-C/N-D not re-raised, per brief. |
| N-d — class-to-category mapping miscited | Resolved | `CLASS_ROWS` at `packages/three-surface-poc-core/src/project-shape-coverage.ts:85-95` gives layers 1,1,1,1,2,3,4,5,6 exactly as SEMANTIC-DELTA.md:182-185 says, and agrees with spec:27-32. `classesForPillar` survives only in the round-2/3 disposition text (packet :297). |
| N-e — B6/B7 survived the selftest | Resolved | Re-ran both: B6 (`if text != expected` → `if False`) fails the selftest "corrupted manifest row digest passed"; B7 fails "undeclared subject change passed the population predicate". See N-i for the wiring gap next to them. |
| N-f — unchanged text guarded only by digest | Resolved | builder:524ff `SPEC_EDITS` + `pin_findings` (builder:1030) hold the whole proposed spec to current bytes with 8 edits. My 17 spec mutants through `requirement_findings` (below) were all killed by the pin, including PWB-REQ-003 SHALL NOT→MAY and a PWB-REQ-001 SHALL→SHOULD. "a changed byte anywhere else fails `--check`" (SEMANTIC-DELTA.md:29-31) is true [Observed]. Weakening a `REQUIREMENT_RULES` entry fails the selftest "rule tables changed without their pinned digest" [Observed]. |
| N-g — unstated details | Resolved (two stated, two disclosed) | spec:47 "at most two headings"; spec:149 more headings than allowed → unreadable; spec:124-126 prefixed-ordinal does not restart. Label trim and first-failure precedence disclosed at SEMANTIC-DELTA.md:261-269 and routed to `syzygy-dov.32` with the shared text. |

## New findings

### R-D (revise) — "until declared" does not agree with P-74 Q2's sequence; the packet says it does

P-74 Q2, Ruled cell (`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:64`):
"one registry-entry amendment act before slice 5's fifth limb only, the first
four limbs thread a profile parameter with current constants as default".
The ruled order is: the registry act, then later limb 5 (the loader). Between
them the code runs on current constants.

The repaired text (spec:137-141): "Until a profile is declared for Butlers,
the observer reads Butlers by the grammar written below … A Butlers profile
that is declared but that the observer does not read, for any reason, is
treated as one the loader refuses". The profile "is carried in the
project-shape observer's owner-adopted registry entry" (spec:127-129), and the
package names `syzygy-dov.24`'s registry act as that home (SEMANTIC-DELTA.md:309-311,
packet :100-101).

The consequence follows [Inferred]. Suppose the registry act puts Butlers'
grammar rows into its entry, and it lands before limb 5, as P-74 Q2 orders and
packet Q7 recommends ("yes, and after"). Then from that act until limb 5,
Butlers has a declared profile that the observer does not read. The text
requires every Butlers class and category to be Unknown (scenario spec:317-324).
Today's code reports known counts by its constants, so it is non-conforming,
and the falsifier's "a refused Butlers profile returns Butlers to the built-in
grammar" (spec:281-282) fires on it.

The package states the opposite in three places:

- OWNER-DECISION-PACKET.md:102-104: "until that act and limb 5, the code runs
  on today's constants. The drafted text writes that in as Butlers' built-in
  default, so the code conforms by the text, not by chance." The text writes
  the default in only until the act, not until limb 5.
- SEMANTIC-DELTA.md:298-303: the default "until a profile is declared for it,
  which is the design P-74 Q2 ruled, so today's code conforms by the text".
  The same claim appears at SEMANTIC-DELTA.md:215-216, "Item 4's interim
  default writes that ruling into the specification".
- IMPACT-LEDGER.md:119: the extraction code "keeps working". That is true
  only while no profile is declared.

This breaks criterion 5 ("agree with P-74 Q2") and makes a stated claim false.
The window is not disclosed anywhere: a grep of `limb` over the five package
files finds no mention of the act-to-limb-5 interval. Questions 6 and 7 put
the ordering to the owner without saying that the recommended order leaves
Butlers all-Unknown, or the code in breach, until limb 5 ships.

Two repairs would work; the choice between them is the owner's:

- (a) Keep "declared", which is the fail-closed choice. State the window and
  its consequence in the packet and the semantic delta. Correct the three
  conformance claims to "until a profile is declared". Put to the owner in
  Q6/Q7 whether the registry act must land together with limb 5.
- (b) Tie the default to P-74's sequence in the text, for example "until
  limb 5's loader reads a profile". That reopens round-3 N-a's
  declared-but-unread gap, which would then need its own treatment.

### Notes

N-h (note) — VIS-2: no falsifier names a known zero for an unreadable class
or a refused Butlers profile. spec:276-283 names a known count for a
non-Butlers project with no profile. It also names a built-in rule
substituted for a missing one, and a refused Butlers profile returning to
the written grammar. It does not name a class that a loaded profile leaves
unreadable, or a refused or unread Butlers profile, rendering a *known*
denominator by some other route, such as an empty set counted as 0. The
oracle (spec:267-275) covers only "every class a loaded profile leaves
unreadable", not a refused profile. So the refused-profile Unknown is
required only by scenario spec:317-324. SEMANTIC-DELTA.md:223-224 says this
is exactly the empty-set hazard the class/category rule exists for. Consider
one falsifier clause: "a class a loaded profile leaves unreadable, or any
class of a refused Butlers profile, reports a known item denominator".

N-i (note) — the selftest tests two `--check` predicates as functions but
not as wired into `check()`. Mutant "check skips manifest" (builder:1360,
the `verify_manifest` call replaced by `pass`) and mutant "check skips
shared" (builder:1354, the `shared_text_findings()` call removed) both
survive `--selftest` ("185 mutants killed", rc 0). The live `--check` does
call both today, so its output is true at this commit [Observed]. But
builder:1963-1970 prints "shape and key-form sentences hash to
syzygy-dov.24's at 1d5966c" unconditionally on success. With the second
mutant it would print that claim without having checked it. The packet
(:296) says the digest is "checked on every `--check`". That is literally
true now, but no mutant pins it.

N-j (note) — the "exactly once" anchor claim is not selftest-covered.
builder:521 says each anchor "must occur exactly once in the current
spec.md". Mutant `base.count(anchor) != 1` → `< 1` (builder:1018) survives
the selftest. The "8 drifted anchors" fixtures test absence, not
duplication. The live check is correct. A separate equivalent mutant: the
path-order branch of `verify_manifest` (builder:1314) disabled also survives,
because the exact-text comparison below it subsumes it. That one is harmless.

N-k (note, minor) — SEMANTIC-DELTA.md:24-25 and IMPACT-LEDGER.md:112 say the
three matrix parts "regenerate" unchanged. They are inputs the
contract-coverage generator reads (`build_polaris_project_wide_contract_coverage.py:25-27`),
not outputs. Their unchanged bytes are enforced by the population predicate
(builder:1333, "undeclared subject change") and the manifest rows, not by
regeneration. Say "are unchanged (checked)".

N-l (note, minor) — SEMANTIC-DELTA.md:309-311 calls `syzygy-dov.24`'s fields
"the one registry act P-74 Q2 ruled". Packet Q7 (:137-143) says the same
identification is not settled ("whether `syzygy-dov.24`'s drafted act is
that act for this profile too"). The Ruled cell names no bead; `.24`
appears only in the record's routing column. Align SEMANTIC-DELTA with Q7.

## Rule-6 mutants (my own)

Spec text, run through `requirement_findings(mutated, current)` directly,
which isolates the text predicates from the manifest and dependency digests.
17 were run and 17 killed, all by the whole-spec pin:

- the R-C revert
- scenario 5 without "never zero"
- PWB-REQ-003 SHALL NOT→MAY
- "never returns" → "may return"
- the undeterminable clause dropped
- "declared" → "loaded"
- category map swap
- "no other project has a built-in default" dropped
- scenario 4 WHEN without "or the observer does not read it"
- the oracle's Butlers leg dropped
- a Butlers heading case change
- a shape sentence changed
- PWB-REQ-001 SHALL→SHOULD
- whole-profile refusal weakened
- `heading-section` two→three
- a trailing newline

One anchor, the case-list edit, missed on wrap and was not run.

Builder mutants against `--selftest`: 24 were run, 19 killed and 5 survived.

Killed:

- B6
- B7
- pin disabled
- shared digest disabled
- module SHAPES compare disabled
- module key compare disabled
- composition disabled
- dependency disabled
- contract-coverage compare disabled
- capability row disabled
- warrants check disabled
- first-scenario check disabled
- scenario text compare disabled
- retired text disabled
- patched-unchanged disabled
- patch-name population disabled
- `REQUIREMENT_RULES` loop disabled
- scenario position disabled
- a weakened `REQUIREMENT_RULES` value (by the rule-tables digest)

Survived:

- `check()` without `verify_manifest` (N-i)
- `check()` without `shared_text_findings` (N-i)
- anchor count `!= 1` → `< 1` (N-j)
- manifest path-order branch disabled (N-j, equivalent)
- the rule-tables digest comparison disabled. It survives trivially: it
  guards a constant, and the weakened-rule mutant above shows it works.

## Other criteria

- State map (criterion 7). Each of the ten states maps to one outcome [Observed, spec:137-157, 317-332]:

  | State | Butlers | Project other than Butlers |
  |---|---|---|
  | loaded | profile rows only; an invalid or missing class is Unknown with its category | same |
  | refused | all classes and categories Unknown; never the default | no loaded profile, so Unknown |
  | declared but unread | treated as refused | no loaded profile, so Unknown |
  | undeterminable | treated as refused | no loaded profile, so Unknown |
  | none | built-in default | Unknown, never zero |

  No scenario, paragraph or falsifier contradicts another. The one conflict
  is with the ruled sequence (R-D), not inside the text.
- Butlers grammar (criterion 4). A diff of the old and new grammar blocks
  differs only in the opening line and the moved exactness paragraph.
  spec:158-163 is word for word apart from its "For every grammar, loaded or
  built-in," opening.
- VIS-2 (criterion 5). Every no-evidence path in the body and the scenarios
  yields Unknown, never zero, subject to N-h on the falsifier list.
- Owner attribution (criterion 9). The sweep
  `\b(ruling|rulings|ruled|chose|decided|answer\w*|you|your)\b`
  (case-insensitive, Python `re`) over the five package `.md` files gives 51
  line hits. Each owner-voiced quote matches the source:
  - P-74 Q2 and P-82 match the Ruled cells at decision lines 64 and 70.
  - §6 "Draft it now (Recommended)" matches the sitting record at line 139.
  - "Readiness order, lane B last (Recommended)" matches the owner-values
    record at line 114. The `.21 → .30 → .22 → lane B` order is attributed
    as the presented option, not the answer.
  - The "What it means" and "Reading" text is labelled as the recorder's, at
    packet :110-111, :150-151 and :185, SEMANTIC-DELTA.md:316-317 and
    IMPACT-LEDGER.md:148.
  - The remaining mis-attribution is N-l (identification, not a quote).
- VIS-4 (criterion 10). Nothing is labelled accepted or in force. The phrase
  is marked "not offered" (packet :198-209). No landing order beyond the
  ruled four is attributed to the owner.
- Open questions 4, 6, 7 and 8 are genuine owner questions. Q6 and Q7 need
  R-D's window added.

Severity: 1 revise (R-D); 5 notes (N-h, N-i, N-j, N-k, N-l). Round-3 R-C and
N-a–N-g resolved.
