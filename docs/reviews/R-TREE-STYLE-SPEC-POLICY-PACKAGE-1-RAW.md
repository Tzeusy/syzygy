# R-TREE-STYLE-SPEC-POLICY-PACKAGE-1 — specification-policy restyle package review
Verdict: CONFIRM WITH EXCEPTIONS
Manifest SHA-256: 0abd08981ae693720c33c339b9d53ac2a4c42c141d0ad23be2e83e90c5cd000e
Reviewed commit: f527c01ca93c6f3555187d48666b774c6560d8b0

Reviewer: independent fresh-context agent, 2026-09-28. Base: main at a9a0830.

## Scope

- **Package:** `.syzygy/governance/contracts/candidates/spec-policy-readability-restyle/`. This covers `OWNER-DECISION-PACKET.md`, `SPEC-POLICY-AMENDMENT-MANIFEST.txt` and `proposed/*.patch`.
- **Tooling:**
  - `scripts/build_spec_policy_readability_restyle.py`;
  - `scripts/record_spec_policy_readability_restyle.py`;
  - the spec-policy parts of the `scripts/check_governance.py` diff a9a0830..f527c01: the constants, `_act_subjects`, the `_performed_act_digests` single pass, `_activate_spec_policy_restyle_copy_registries`, the CG-7h successor block and its selftests.
- **Evidence:** `docs/evidence/spec-policy-restyle-rule6-2026-09-28.json`.
- **Governing references:**
  - AGENTS.md;
  - `ACCEPTANCE-ACT-RECORD.md` (acts 6 and 7, and the general trusted-bootstrap transaction's row 5);
  - the current policy files;
  - `OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md`;
  - `DOCUMENTATION-ESTATE-OWNER-RULINGS-DECISION.md` (P-66);
  - the RD-70 raw;
  - the two prose-review raws.
- **Not reviewed on its merits:** the HISTORY_REVIEW_RAW and polaris-recorder history-reading change. It is noted only where it affects this package (N3).

All experiments ran in scratch clones under `pkgrev1/`: `exp1`, `sim`, `simregen`, `mut` and `base`. The reviewed clone was not modified.

## Facts established

1. [Observed] `sha256sum SPEC-POLICY-AMENDMENT-MANIFEST.txt` gives `0abd08981ae693720c33c339b9d53ac2a4c42c141d0ad23be2e83e90c5cd000e`. This equals the packet's phrase argument.
2. [Observed] I applied each patch with `patch` to a copy of its current policy. The results hash as follows:
   - `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` gives `38c0e629efa6fb6acdb3c7d0f63b02518191d03221ae290a6bbc691fc697a90e`;
   - `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` gives `e08270a2d2589aafaad59d9958683f094fb6170b38cfaa30e49f48c41645989c`.

   Both equal the manifest rows. `build_spec_policy_readability_restyle.py --check` reports "manifest matches both patched policies; clause leads, headings and identifiers preserved" (rc 0).
3. [Observed] The current policies hash as follows. These are their latest performed digests in the acceptance record.
   - CC-SPEC hashes to `6093dbbe519dad6c35a5aaeeb31355d2e435d76ec4f0c2c9affb0d1e5b6b5621`, the general trusted-bootstrap transaction's row 5.
   - CC-IMPACT hashes to `cd6ec838e701f0258889d0c3c2776fc91fe1686829379b789ae5b151b04c27c0`, act 7.

   The OLD files the two prose reviews compared against are byte-identical to today's policies.
4. [Observed] I diffed the prose-reviewed drafts (`review-spec2/NEW-*`) against the patched after-images. The only differences are the three disclosed banner changes:
   - the spec head banner;
   - the spec RD-69 paragraph: five RFCs become nine, and "awaits its one confirming review" becomes the RD-70 sentence;
   - the impact head banner.

   Everything else the prose reviews confirmed is byte-for-byte what the manifest binds.
5. **Rules unchanged (criterion 1).**
   - [Observed] The clause lead sequence and the heading sequence are identical in both files. No identifier is lost.
   - [Observed] I compared a per-clause word multiset, OLD against NEW, with mermaid blocks and diagram captions removed and sections split on the clause leads and the `##` headings. Inside the clauses:
     - the spec file differs only in list dashes and connectives: CC-SPEC-3 (the "and" before the retirement limb), CC-SPEC-6, CC-SPEC-8 (one "and", sentence-final periods) and CC-SPEC-11 (dashes);
     - the impact file differs only in list dashes: CC-IMPACT-2, 3, 5 and 6.
   - [Observed] Every other difference is an added intro sentence in "The rule", "What this policy is not", "What this rule set does not do" or "Why each rule is here".
   - I read each clause OLD against NEW. No obligation is added, dropped, weakened or strengthened.
6. **CC-IMPACT-7 fixture pin.** [Observed] The fixture path, the sha256 `685a71f7a52652a314f144ba1599982812921ede88220e69a0d5d327272ed4e0`, the answer-key path and the "run is void" sentence are all unchanged. They sit in the byte-identical CC-IMPACT-7 region.
7. **Banner claims are true (criterion 2).** [Observed]
   - Acts 6 and 7 (`ACCEPTANCE-ACT-RECORD.md`, "Acts 6 and 7 … confirmed, 2026-08-17") confirm CC-SPEC-1…11 and CC-IMPACT-1…7 "in force at those digests".
   - The new CC-SPEC-8 names nine phase rules. OLD named five in the history paragraph.
   - The RD-70 raw at `round-2026-08i/reviews/RD-70-p41-p42-confirming-RAW.md`, line 95, reads `VERDICT: CONFIRM WITH EXCEPTIONS`, which is the verdict the new banner quotes.
   - The owner's "Fix banners too" and P-66 arm (a) are recorded in `OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md`, line 31, and `DOCUMENTATION-ESTATE-OWNER-RULINGS-DECISION.md`, line 38.
   - Both relative links in the new banners resolve.
   - No line outside a fence has an odd backtick count, so no code span is broken.
8. **Before adoption, at f527c01.** [Observed]
   - `check_governance.py` gives "31 OK, 21 WARN, 0 FAIL (52 checks)".
   - `--selftest` gives "341 fixtures, 0 failing".
   - The builder `--selftest` gives 14/0, and the recorder `--selftest` gives 34/0.
   - The recorder `--check` gives "not performed: no record".
9. **Simulated adoption (criterion 5).** [Observed] Clone `sim`, in this order:
   1. I pinned `FROZEN_MANIFEST_SHA` to the manifest digest and `REVIEW` to a committed scratch raw whose head carries a CONFIRM verdict line and a manifest-digest line, with `REVIEW_SHA` set to that raw's sha256, and committed.
   2. `--apply --at-adoption` before recording refused ("no owner act is recorded", rc 1).
   3. `--record --phrase "CONFIRM SPECIFICATION POLICY READABILITY RESTYLE: <digest>"` succeeded.
   4. `--apply --at-adoption` applied both policies.
   5. I committed.

   Results after the commit:
   - `check_governance.py` gives "31 OK, 21 WARN, 0 FAIL (52 checks)". CG-7h now examines 145 predicates, against 134 before, and CG-7e examines 46 files, against 44.
   - The recorder `--check` gives PASS.
   - The builder `--check` reports "applied".
   - The policy hashes equal the manifest rows.
10. **Recorder behaviour (criterion 4).** [Observed]
    - It refuses when any pin is `None`.
    - The act body, aggregate block and install entry match the packet's "What adopting does" list and grant nothing beyond the restyle: "This act grants no implementation, source, provider, write, deployment or release permission."
    - The nested `CONFIRM CRAFT AMENDMENT: CC-IMPACT@…` / `CC-SPEC@…` lines are built from the manifest rows (`nested_lines`).
    - I ran 11 mutations of my own on the recorder. Nine are killed by the selftest: the head digest check, the pinned-manifest compare, the raw sha compare, the nested-row derivation (every row pointed at one path), the `None`-pin check, the builder-findings check, `[:4]`→`[:5]`, `fullmatch`→`search`, and the dedicated-record regeneration compare. Two survive (N4).
11. **Rule-6 evidence (criterion 7).** [Observed]
    - `git diff --quiet 015bef0 f527c01 -- scripts/` exits 0.
    - I re-ran all 21 recorded mutants at 015bef0. Each `old` fragment occurs exactly once, and each mutant fails its selftest with exactly the recorded last line. Two fail by exception, as recorded: #11 raises `FileNotFoundError` and #18 raises `KeyError`.

## Findings

No material findings.

**N1 — Two stale status sentences outside the three disclosed banners remain, and after adoption each contradicts its own file's new banner.** [Observed]

- **Impact file, `## Acceptance` (NEW lines 320–323, byte-identical to OLD):** "This is a **candidate**. It comes into force only by its own `CONFIRM CRAFT AMENDMENT` act … Nothing in it binds today, and no verdict of the launch gate may cite it as in force until that act is performed." NEW line 3 of the same file says "**In force:** acts 6 and 7 confirmed this file".
- **Spec file, "Known open findings" f15 row (NEW line 431):** "… Awaits the confirming review". NEW lines 42–44 say "RD-70 confirmed the repair".

Neither sentence is new, and the packet's banner count ("three") is exact, so criterion 2 holds. But the owner is being asked to re-bind both false sentences at new digests beside banners that contradict them. AGENTS.md: "Mark staleness **at the stale sentence** … never rely on a page banner to cover a specific false claim."

To fix: either disclose both in the packet's "What stays the same", or fold them into the banner fix. Folding them in needs a new manifest and a re-review.

**N2 — The packet's "nothing else is rewritten" understates the adoption change: two generated views go stale and fail the canonical battery unless regenerated.** [Observed] After the simulated adoption, in `sim`:

- `build_contract_index.py --check` reports "DRIFT: 05-CONTRACT-INDEX.yaml differs from regeneration". The cause is the INSTALL-RECORD word count, 1455 → 1535.
- `build_directive_register.py --check` reports "FAIL: DIRECTIVE-REGISTER.md is stale". All 18 CC-SPEC and CC-IMPACT line numbers move, for example CC-SPEC-1 goes from :42 to :72.

Running both generators (clone `simregen`) makes both checks pass, and `check_governance.py` stays at 0 FAIL. The precedent adoption commit a9a0830 regenerated `DIRECTIVE-REGISTER.md` and edited `PROJECT-STATUS.md`. The PROJECT-STATUS battery comment for this recorder ("not performed" until recorded) will also need its adoption edit.

Neither the packet nor the recorder or builder docstring names these steps. The packet sentence is true of governance semantics, since the checker needs no change. It is not true of the adopting commit.

**N3 — At the reviewed commit the canonical battery is red on the prerequisite the packet cites.** [Observed]

- `python3 scripts/record_polaris_understanding_adoption.py --check` at f527c01 gives "FAIL exact digest reconciliation unresolved: latest history review not confirming: docs/evidence/polaris-understanding-reconciliation-2026-09-28/HISTORY-REVIEW-3-RAW.md". HISTORY-REVIEW-1…3 all carry the verdict REVISE.
- The same check passes at a9a0830.
- Every other battery line from PROJECT-STATUS passes at f527c01: 45 of 46 rc 0.

The owner's ruling ("R1: read as history", `OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md`) says the recorder is moved "through its own reviewed cycle … before the restyle's phrase is offered". That cycle is not yet confirmed.

[Observed] I committed a synthetic `HISTORY-REVIEW-4-RAW.md` carrying a CONFIRM verdict and the recorder's current sha256. The polaris `--check` then passes both before adoption (`exp1`) and after the simulated adoption (`sim`). So the packet's claim that adopting "does not retire that reconciliation" holds, conditional on a real confirming round 4.

The failure belongs to the separate change and does not break this package's bytes. The packet should not reach the owner until that review confirms.

**N4 — Two recorder guards have no killing fixture.** [Observed] Both are mutations of `scripts/record_spec_policy_readability_restyle.py` at f527c01, run with `--selftest`:

- **The partial-record guard in `record()`.** Mutating `if MARKER.encode() in text or LABEL.encode() in text:` to `if False:` leaves "34 fixtures, 0 failing". The "second record refused" fixture is still killed by the later `ACT.exists()` check, so a partial aggregate or install section with no dedicated record is untested at record time. `check()` would still fail afterwards on the duplicated marker.
- **The already-applied guard in `verify_package`.** Mutating `if allow_applied:` to `if True:` leaves "34 fixtures, 0 failing". Recording over policy bytes already installed out of order is therefore accepted, and no fixture exercises "package bytes are already installed". The builder's own `--apply` still refuses before a record, so this only matters for a hand-applied patch.

Both fail open only against out-of-order manual steps. The rule-6 record does not claim these guards.

**N5 — Minor wording.** [Observed]

- **The new CC-IMPACT banner.** "and later performed acts amend them" is not yet true of CC-IMPACT: its latest performed digest is still act 7's. It becomes true once this act is performed, and the banner ships only in the adopted bytes, so it reads correctly at adoption.
- **Transaction row numbering.** The builder docstring says CC-SPEC is bound by "row 7 of the general trusted-bootstrap transaction". The recorder body says "row 5". Both are correct under different numberings: row 7 is the manifest-row number and row 5 is the act-row number. `check_governance.py` spells it out as "row 5 of its act, line 11 of its manifest". A reader of the docstring alone may be confused.

## Verdict rationale

All seven acceptance criteria hold.

1. Criterion 1 holds: the clause-by-clause read plus the word-multiset check show no rule change, and the CC-IMPACT-7 pin is intact.
2. Criterion 2 holds: exactly three banner changes, all true against the acceptance record and RD-70.
3. Criterion 3 holds: the manifest digest and both rows re-derive by script.
4. Criterion 4 holds: the recorder is pinned, derives the nested lines from the rows, and its selftest kills 9 of my 11 mutations and all of the rule-6 set.
5. Criterion 5 holds: 0 FAIL before and after a simulated adoption, and the selftest is 341/0.
6. Criterion 6 holds: the packet is plain, present tense, claims no adoption and grants nothing beyond the restyle.
7. Criterion 7 holds: all 21 mutants reproduce at 015bef0, and the scripts are identical at f527c01.

The five findings are notes. N1 leaves two pre-existing false status sentences beside the corrected banners. N2 is an undocumented regeneration step for the adopting commit. N3 is an out-of-package prerequisite that must confirm before the packet is offered. N4 is two untested fail-open guards against manual misordering. N5 is wording. None fails a criterion. Hence CONFIRM WITH EXCEPTIONS.
