# Independent review (round 1) — PWB readability successor
Reviewed commit: 934e9c9fcac9714e9de5e40db5c3697e2d58ff55
Manifest SHA-256: 9292caad6b81f7cced085395f8ac2b547880eb891e14c224ae3e9d220274e794
Verdict: CONFIRM WITH EXCEPTIONS

## Method

Read at the full commit via `git archive` into scratch trees (repo not edited). Patches applied with `git apply -p1` to a scratch copy; comparisons by my own script, independent of the builder.

## Checks run

- Predecessor: all 11 current subject bytes hash to the item-depth manifest rows (11 rows, 0 mismatches). [Observed]
- Patches: all four apply cleanly; exactly four of eleven subject files differ; all 11 package-manifest rows re-derived against the applied tree, 0 mismatches; manifest-file sha256 equals the value in the head. [Observed]
- Builder `--check` and `--selftest` pass (52 predicates); `--diff` prints; `--apply` without `--at-adoption` refuses. [Observed]
- Over the applied copy: `build_polaris_project_wide_contract_coverage.py --check` (324 clauses), `build_polaris_project_wide_spec_dependencies.py --check` (17 reqs), `check_polaris_response_ceiling_reading.py --check` (OK), `openspec validate polaris-project-wide-butlers-model --strict` (valid). `check_governance.py` on the unapplied archive: 0 FAIL. [Observed]
- Independent spec comparison (own script): 17 requirement headings and 44 scenario headings equal, same order, each once. Per requirement: the group line plus normative region compared after removing only whitespace, list markers, the label bullets and the `**Verification.**` line: words equal in 17/17; modal multiset/sequence (SHALL NOT, SHALL, MUST NOT, MUST, MAY, SHOULD) equal in 17/17; tail from `- **Case` byte-equal in 17/17. Purpose outside the guide: words equal. Every deleted line that matched scenario/warrants/verification patterns is a reflowed normative sentence, not a tail line. [Observed]
- Group column of the guide table matches each requirement's `Group:` line for all 17; titles match; numbering gaps (008, 009, 017–019) and file order (004 after 007) are true; every requirement has a `warrants` block. [Observed]
- GOVERNING-DEPENDENCIES.md differs by exactly the source-digest line (new digest equals sha256 of the applied spec.md). [Observed]
- Mutations I ran: weakening one added `SHALL NOT` to `SHALL` in spec.md.patch fails with "normative words changed" and "modal sequence changed" for PWB-REQ-005; corrupting a manifest row fails "manifest differs from deterministic proposed-byte regeneration". [Observed]
- Ledger counts at 1ecb998: 1,838 paths; 207 files containing the subject name by `git grep -F`; class partition 7/68/13/56/42/15/2/4 equals the ledger. [Observed]
- Reading of the labels: the nested "It / Otherwise / That / Neither" bullets (e.g. PWB-REQ-004, 006, 007, 015, 020, 021) keep their original sentence order, so each pronoun has the same antecedent as in the signed prose; I found no label that adds a term or condition. [Inferred, from reading each listed instance]

## Findings

**Finding 1 — proposal inert-code sentence is stronger than the requirement and the map calls it preserved** (note)
`proposal.md` (proposed), What Changes, "Reads are bounded and inert": "markup-like examples inside them do not make a source active content." The signed proposal said "not active content merely because they contain markup-like examples", and PWB-REQ-006 "Inert code contexts" says such examples "SHALL NOT alone cause active-content exclusion". The new sentence drops the qualifier "merely"/"alone" and reads as an unconditional rule, although the same requirement still excludes malformed (unclosed) spans and fences. SEMANTIC-MAP.json classes the unit "What Changes — bounded, contained, inert reads; inert code contexts; secret screening" as preserved ("split into children"); it is at best clarified, and the note does not disclose the dropped qualifier. Non-normative prose, the specification governs, so no behavioural consequence; restoring "alone" and re-noting the unit would close it.

**Finding 2 — "repository-contained" dropped from the same proposal bullet** (note)
Same unit: the signed bullet said shape reads "are bounded, repository-contained and inert"; the new bullet says reads "take exact Git objects only, with no symlink or submodule escape". The containment idea survives by implication and PWB-REQ-006 "Containment" states it fully, so nothing is lost normatively, but the map's "same claim" for this unit is slightly generous. Fold into Finding 1's repair if the owner wants it.

**Finding 3 — a patch tail edit that leaves the proposed bytes unchanged is not detected** (note)
Appending a stray line after the last hunk of `proposed/design.md.patch` still passes `--check`, because the manifest hashes the proposed bytes, not the patch files. Harmless to the signed bytes (the recorder applies the patch and re-proves every row), and reviews bind to commit digests anyway. Mentioned only because the brief asked for predicate kills: the changed-modal and stale-manifest predicates both fail closed as required.

## Criteria summary

1 predecessor and siblings: met. 2 identities and order: met. 3 normative words: met by script and by reading; no lost modal, condition, Unknown or refusal found. 4 byte-equal parts and dependencies regeneration: met. 5 reading guide: marked non-normative, adds no requirement, every statement, the flow diagram and the table check against the requirements; cannot be read as a rule. 6 proposal and design: all 15 changed units are faithful summaries of signed text or correct removals; the other classified units hold except the notes in Findings 1–2; CAPABILITY-COVERAGE quotations are found. 7 semantic map: 120 units, 17 and 44 preserved, changed_count 15, no blanket equivalence claim seen. 8 mechanics: met. 9 owner boundary: no phrase offered; packet names the VERSIONED_PWB_PACKAGES, VERSIONED_LATER and battery wiring. 10 comprehension: the proposed spec.md alone states scope, indexes all 17 requirements and separates reading aids from normative words.
