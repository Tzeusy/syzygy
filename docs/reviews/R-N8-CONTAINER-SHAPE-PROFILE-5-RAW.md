# R-N8-5 — confirmation review of PR #124
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 51b82b63a5c43449f3df5828efe2aaa51cc3cdea
Manifest sha256: 2bf8addcb4168ad4b20a56e3097ca59a94e02fb9e820156ad796e31a50f2ae0e

Reviewer: independent round-5 confirmation reviewer. I worked in a fresh
detached worktree at the reviewed commit and removed it after the review. I
made no commit, push or branch edit.

- Package: `.syzygy/governance/contracts/candidates/pwb-container-shape-profile-amendment/` (called `P/` below).
- Builder: `scripts/build_pwb_container_shape_profile_amendment.py` (called "builder").
- "spec:N" is a line of
  `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`
  after I applied all three `proposed/` patches with `git apply` to a scratch
  copy of the subject.
- Every other file:line reference is at 51b82b6.
- Commits since round 4: `74c1b3c` (the repairs) and `51b82b6` (the partition
  recount).

## Commands run and output (at 51b82b6)

| Command | Result |
|---|---|
| builder `--check` | exit 0. "matches 11 proposed subjects (3 patched, 8 unchanged); the whole spec equals the current spec with 8 pinned edits; … 22 PWB-REQ-002 rules, 5 scenarios word for word … 12 declared sibling-composition outcomes verify". Then: "shape and key-form sentences hash to syzygy-dov.24's at 1d5966c; scripts/build_pwb_registry_loaded_profile_amendment.py is not in this tree …" |
| builder `--selftest` | exit 0. "selftest: 196 mutants killed — …" |
| builder `--diff` | exit 0. Prints the three patches (303 lines). |
| `python3 scripts/check_governance.py` | exit 0. "32 OK, 20 WARN, 0 FAIL (52 checks)". CG-7d: "SIGN OFF PWB CONTAINER-SHAPE PROFILE AMENDMENT — 1 quotation(s), 0 finding(s), 0 performed digest(s)". No WARN line names this package or `u05`. |
| `python3 scripts/check_governance.py --selftest` | exit 0. "285 fixtures, 0 failing". |
| `python3 scripts/check_docs_review_campaign_partition.py` | exit 0. "total=252 assigned=252 raw=227 other=25 unmatched=0 overlaps=0". Row "N8 container-shape profile gate 4". `ls docs/reviews \| wc -l` = 252, and `docs/README.md:99` says 252. |
| Manifest file digest, by `sha256sum` and by Python `hashlib` | Both give `2bf8addcb4168ad4b20a56e3097ca59a94e02fb9e820156ad796e31a50f2ae0e`. This equals `P/OWNER-DECISION-PACKET.md:25` and `:241`, the only two places it occurs in the tree. |
| Manifest rows, re-derived by my own script over the patched scratch copy | 11 rows, 0 mismatches, paths in codepoint order. The subject tracks 15 files. The 4 not in the manifest are `contract-coverage-parts/RFC-0001-0003.md`, `RFC-0004-0006.md`, `RFC-0007-0009.md` and `tasks.md`, as disclosed. |
| `openspec validate polaris-project-wide-butlers-model --strict` on the patched copy | "Change 'polaris-project-wide-butlers-model' is valid" |
| `syzygy-dov.24`'s `--check` at `0d1ccc5`, with this round's `spec.md.patch` applied (verifies `P/IMPACT-LEDGER.md:146`) | Passes: "… manifest matches the 1 proposed subject …" |

`git status --short` in the worktree was empty after every mutation run.

## Shared text with dov.24 at 1d5966c (my own script)

I read `SHAPES` and `ITEM_KEY_SENTENCES` by `ast.literal_eval` from
`git show 1d5966c:scripts/build_pwb_registry_loaded_profile_amendment.py`.

- They hold 9 and 7 entries.
- The SHA-256 of `repr((SHAPES, ITEM_KEY_SENTENCES))` is
  `64b15eaeed24b510c7d744bdd09f1de4f5989d2c05c9165b3826b8ac226d753d`. This
  equals the builder's `SHARED_TEXT_SHA256`.
- `SHAPES` equals this builder's `SHAPES`.
- `{name: sentence}` over this builder's `KEY_FORMS`, with the one `None` name
  (`prefixed-ordinal`) left out, equals `ITEM_KEY_SENTENCES`.
- All 16 sentences occur in the proposed spec. I compared them with
  whitespace collapsed, backticks removed and the final full stop dropped: 0
  are missing.
- `git log 1d5966c..0d1ccc5 -- <that builder>` is empty.

## Round-4 resolution

| Finding | Status | Evidence |
|---|---|---|
| R-D — the default lasts until a profile is "declared", which conflicts with P-74 Q2's order | **Resolved, by option (a)** | See the R-D detail below the table. |
| N-h — no falsifier clause for a known denominator from an unreadable class or a refused or unread Butlers profile | Resolved | spec:282-285 now reads "a class a loaded profile leaves unreadable, or any class of a Butlers profile that is refused or declared but unread, reports a known item denominator". The same text is in `REQUIREMENT_RULES` (builder:417-421) and SEMANTIC-DELTA.md:167-170. The digest is re-pinned (builder:520). Dropping the rule without re-pinning fails the selftest "rule tables changed without their pinned digest". Changing "known" to "zero" in the patch fails `--check` (pin, rule, dependency and composition findings). |
| N-i — `check()` was not tested with `verify_manifest` or `shared_text_findings` removed | Resolved | builder:1868-1893. I re-ran both round-4 survivors. Without `shared_text_findings()` the selftest fails with "check() passed without the shared-text digest". Without `verify_manifest` it fails with "check() passed a corrupted manifest". Three sibling calls are still unpinned: see N-m. |
| N-j — duplicate anchors were not tested | Resolved | builder:1856-1866. My round-4 mutant (`!= 1` changed to `< 1`) now fails the selftest with "duplicated anchor passed". |
| N-k — the matrix parts were said to "regenerate" | Resolved | SEMANTIC-DELTA.md:24-28 and IMPACT-LEDGER.md:112 now call them files the generator reads. `build_polaris_project_wide_contract_coverage.py:24-28` confirms that `PARTS` is the three `contract-coverage-matrix/` files, which are inputs. All three have manifest rows. The claim "a change to any file no patch is declared to change fails `--check`" is broader than the check: see N-n. |
| N-l — the semantic delta identified dov.24's act as the one P-74 Q2 ruled | Resolved in the delta | SEMANTIC-DELTA.md:326-329 now says the fields are the "drafted" home and that the identification "is not settled (packet question 7)". The packet still makes the identification at :100-101: see N-o. |
| Selftest 185 → 196 | Confirmed | 185 + 1 new requirement rule + 8 duplicated anchors + 2 `check()` fixtures = 196. This equals `EXPECTED_KILLED` (builder:523) and the run's output. |

R-D detail, checked site by site:

- **The window is disclosed and labelled [Inferred].**
  - It has its own packet subsection, `P/OWNER-DECISION-PACKET.md:108-125`, with the label at :117-118.
  - SEMANTIC-DELTA.md:219-229 discloses it in the warrant.
  - SEMANTIC-DELTA.md:312-320 discloses it in downstream item 1.
  - IMPACT-LEDGER.md:119 discloses it.
- **The three contrary claims are corrected**, at packet :102-106, SEMANTIC-DELTA.md:219-229 and :312-320, and IMPACT-LEDGER.md:119.
- **Criterion 5 is corrected** at REVIEW-BRIEF.md:73-77.
- **Q6 is scoped** at packet :153-156: "but only while no Butlers profile is declared".
- **Q7's second part** is at packet :168-182. Options (a) and (b) are left undecided: "none decided here", and the recommendation "does not choose between (a) and (b)".
- **Option (b) is named as not taken** at packet :122-124, with its reason, round 3's N-a.
- **No remaining conformance claim is unscoped.** I swept `conform|keeps working|no gap|by the text|today's code|interim` over the five `.md` files, the patches and the builder. Every conformance claim is now limited to "while no Butlers profile is declared".
- **The window agrees with P-74 Q2's order.** The Ruled cell at decision line 64 is "one registry-entry amendment act before slice 5's fifth limb only". The record's own "What it means" cell says "Slice 5's fifth limb waits for the registry act". The disclosed window is exactly the interval from that act to limb 5.

## Consistency (criterion 7), from the patched text

Each state leads to exactly one outcome [Observed, spec:137-157, 282-285, 319-334]:

| State | Butlers | Project other than Butlers |
|---|---|---|
| loaded | Profile rows only. A class with no row or an invalid row is Unknown, and so is its category. Every source stays counted. | Same |
| refused | Every class and category is Unknown. Never the default. | Not loaded, so Unknown, never zero |
| declared but unread | Treated as refused | Not loaded, so Unknown |
| undeterminable | Treated as refused | Not loaded, so Unknown |
| none | The built-in default. The disclosed window does not apply, because nothing is declared. | Unknown, never zero |

- No scenario, body paragraph, falsifier clause, packet question or ledger row contradicts another, apart from N-o.
- The disclosed window follows from the "declared but unread" row. Every text that describes it agrees with P-74 Q2's order.
- Q7's second part offers (a) and (b) without recommending either, and nothing in it is presented as the owner's. N-p is about framing only.

## New findings

N-m (note) — the builder's `check()` still has three unpinned calls, the same
class as round 4's N-i. I ran each mutant below against `--selftest`, and
each survives ("196 mutants killed", rc 0):

- builder:1355: `population_findings(patch_files())` replaced by `[]`.
- builder:1360: `findings.extend(structure_findings(proposed))` removed.
- builder:1362: `findings.extend(composition_findings())` removed.

With the second or third mutant, `--check` would still print that "22
PWB-REQ-002 rules, 5 scenarios word for word … and 12 declared
sibling-composition outcomes verify" (builder:1995-2008) without checking
them. The live `--check` does call all three, so its output is true at this
commit [Observed].

The packet's N-i disposition (:352) claims only the two calls it names, so it
is true as written. Criterion 8 asks for claims that no mutant covers, and
these are those claims. The two `check()` fixtures at builder:1868-1893 show
the pattern that would pin them.

N-n (note) — the claim "a change to any file no patch is declared to change
fails `--check`" is broader than the check. It appears at
SEMANTIC-DELTA.md:26-28 and IMPACT-LEDGER.md:112.

To test it, I appended a `new file mode` hunk creating
`openspec/changes/polaris-project-wide-butlers-model/EXTRA.md` to
`proposed/CAPABILITY-COVERAGE.md.patch`. `--check` still passed with its full
success message.

This happens because `proposed_bytes` (builder:915-927) applies the patches
to a scratch tree that holds only the 11 subjects. `population_findings` then
compares only those 11 subjects.

The consequences are limited:

- A hunk that edits one of the four files left out of the manifest fails
  anyway, because that file is absent from the scratch tree.
- `--apply` writes only `PATCHED` (builder:1960-1962), so the created file
  would not land through the builder.
- A recorder that "applies the three patches" with `git apply` (packet :276)
  would create it, and `--diff` prints it.

For the three matrix parts, which are manifest subjects, the claim is true.
Either scope the sentence to the manifest's subjects, or refuse any patch
path outside `PATCHED`.

N-o (note) — the packet still identifies dov.24's act as the one P-74 Q2
ruled, under "Already ruled". This is round 4's N-l, left standing in the
packet.

- `P/OWNER-DECISION-PACKET.md:100-101`, under the heading "Already ruled, and
  what it settles here", reads: "there is one such act. `syzygy-dov.24`
  drafts it".
- Question 7 (:160-163) says the opposite is open: "What it does not settle
  is whether `syzygy-dov.24`'s drafted act is that act for this profile too".
- The Ruled cell names no bead. Only the record's routing column names gate
  `.24`.

The repaired SEMANTIC-DELTA.md:326-329 now agrees with Q7, so the packet
bullet is the one place left that disagrees. It is unchanged since round 4,
where it was missed. Suggested wording: "`syzygy-dov.24` drafts a registry
act; whether it is that act is question 7".

N-p (note, framing) — Q7's second part (packet :175-179) is neutral in its
verdict but not in how it describes the two options.

- Option (a) is given only its benefit, that "no declared Butlers profile
  ever goes unread". It is not given its cost: the registry act, and anything
  else dov.24's act carries, waits until limb 5 is built. That is in some
  tension with Q6's recommendation that the registry and specification
  "agree the first time".
- Option (b) is given only its cost: non-conformance, and a falsifier that
  fires.
- A third arm is not listed. The registry act could land first without
  Butlers' grammar rows, so that no profile is "declared" until limb 5.

The packet does not claim the two options are exhaustive, and it recommends
neither. Consider giving each option one line of cost.

N-q (note, minor) — the window disclosure names one falsifier clause, but
two fire.

- The disclosure at packet :116-117 and SEMANTIC-DELTA.md:226-227 names "a
  refused Butlers profile returns Butlers to the built-in grammar".
- During the window, this round's new clause also fires [Inferred]: "any
  class of a Butlers profile that is refused or declared but unread, reports
  a known item denominator" (spec:283-285).
- The disclosure does not say that only one clause fires, so it is not
  false. It is only incomplete.

## Rule-6 mutants (my own)

**Spec text.** I ran each mutant through `requirement_findings(mutated,
current)`. The unmutated patched text gives `[]`. I ran 14 mutants and all 14
were killed, every one by the whole-spec pin and most by a second predicate as
well (n = 2 or 3 findings each):

- N-h clause dropped
- "declared but unread" changed to "declared"
- "known" changed to "zero" in the new clause
- interim default changed to "Until limb 5 reads a profile" (option (b))
- declared-but-unread treated as absent
- undeterminable clause dropped
- scenario 4 WHEN without "or the observer does not read it"
- scenario 5 without "never zero"
- "never substitutes" changed to "may substitute"
- category dropped from the unreadable-class sentence
- PWB-REQ-002 body "until declared" changed to "until loaded"
- the oracle's Butlers leg dropped
- whole-profile refusal without the category clause
- `heading-section` "two" changed to "three"

I also ran one end-to-end mutant: the patch file itself edited ("known"
changed to "zero") and `--check` run. It was killed.

**Builder, against `--selftest`.** I ran 21 mutants: 15 were killed and 6
survived.

Killed:

- `check()` without `shared_text_findings`
- `check()` without `verify_manifest`
- anchor count `!= 1` changed to `< 1`
- B6
- B7
- pin always clean
- `REQUIREMENT_RULES` loop off
- new rule dropped without re-pinning
- shared digest comparison off
- module SHAPES comparison off
- module key comparison off
- retired text off
- warrants comparison off
- first-scenario comparison off
- scenario text comparison off

Survived:

- `check()` without `population_findings` (N-m)
- `check()` without `structure_findings` (N-m)
- `check()` without `composition_findings` (N-m)
- "manifest missing" branch off. Equivalent: `read_text` then raises, so
  `--check` still exits non-zero.
- rule-tables digest comparison off. Trivial: it guards a constant, and the
  dropped-rule mutant shows it works.
- killed-count comparison off. Trivial, for the same reason.

**What `--check` claims to pin, checked literally:**

- Packet :64-65, "the builder proves it with a digest of that draft's two
  tables", is true.
- Packet :83-84, "holds every other byte of it to today's", is true: it is
  the pin.
- The N-i and N-j dispositions (:352-353) are true as scoped.
- The N-k sentence is true for the manifest subjects and too broad beyond
  them (N-n).

## Other criteria

- **VIS-2 (criterion 5, check 8).** Every no-evidence path in the body, the
  scenarios and now the falsifier gives Unknown, never zero: spec:143-157,
  282-285, 319-334. No path gives a known zero.
- **Owner attribution (check 9).** I swept
  `\b(ruling|rulings|ruled|chose|decided|answer\w*|you|your)\b` with Python
  `re`, case-insensitive, over the five `.md` files. It gives 53 line hits:
  packet 37, delta 10, ledger 3, brief 3. The owner-voiced quotes match their
  sources:
  - P-74 Q2 and P-82 match the Ruled cells at decision lines 64 and 70.
  - §6's "Draft it now (Recommended)" matches the sitting record at line 139.
  - "Readiness order, lane B last (Recommended)" matches the owner-values
    record at line 114. Its order is given as the option presented.
  - The "What it means" and "Reading" text is labelled as the recorder's.
  - The only new owner-attribution phrase is SEMANTIC-DELTA.md:223, "as that
    ruling orders". It is accurate: the Ruled cell says "before".
  - The one identification still attributed beyond the Ruled cell is N-o.
- **VIS-4 (check 10).** Nothing is labelled accepted or in force. The phrase
  is "not offered" (packet :237-248), and :244-245 correctly says all four
  rounds said REVISE. No landing order beyond the ruled four is attributed
  to the owner.
- **Butlers grammar (criterion 4).** This round did not change it. It is
  held by the whole-spec pin, and the spec:158-163 exactness bullet is
  unchanged.
- **Open questions.** Q4, Q6, Q7 and Q8 are genuine owner questions, and
  Q6/Q7 now carry the window.

Severity: 0 revise; 5 notes (N-m, N-n, N-o, N-p, N-q). Round-4 R-D and N-h to
N-l resolved, with N-l resolved in the semantic delta only (N-o). Under the
2026-09-26 sitting rule, this notes-only CONFIRM WITH EXCEPTIONS clears the
bytes at the manifest digest above.
