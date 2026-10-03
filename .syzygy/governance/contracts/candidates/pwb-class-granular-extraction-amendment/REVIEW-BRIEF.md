# Review brief — PWB class-granular extraction amendment (M15)

> **Candidate — binds nothing.** This brief tells a fresh-context reviewer
> what to read and what to decide. It is not itself under review.

## What you are reviewing

One amendment package against the signed PWB specification,
`openspec/changes/polaris-project-wide-butlers-model/`. It consists of:

- the five patches under `proposed/` (four authored, one regenerated);
- the manifest `PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-MANIFEST.txt`;
- `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md` and `OWNER-DECISION-PACKET.md` in
  this directory;
- the builder `scripts/build_pwb_class_granular_extraction_amendment.py`,
  and the one-entry change to `scripts/build_pwb_release_label_amendment.py`
  that lists this package as a pending sibling.

To read the proposed bytes, run `python3
scripts/build_pwb_class_granular_extraction_amendment.py --diff`, or apply
the patches in a scratch copy. Never apply them in the tree.

## Governing references (read only these)

- **The ruling.** P-82 at line 70 of
  `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`.
  The "Ruled" column is the owner's answer; "What it means" is the
  recorder's gloss.
- **The question it answered.**
  `docs/design/POLARIS-M15-PIPELINE-TRUTHFULNESS-FUNNEL.md`, questions Q1 to
  Q4 and their arms.
- **The signed subject.** The eleven artifacts the manifest names, as they
  stand after the container-shape sign-off
  (`.syzygy/governance/decisions/PWB-CONTAINER-SHAPE-PROFILE-AMENDMENT-SIGNOFF-v1.0.md`).
  That package's `OWNER-DECISION-PACKET.md` question 8 asked to keep it and
  this one separate, and said the second to land must have its review check
  "the category rule and how far the exactness sentence reaches".
- **The sign-off scope.**
  `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`.
- **The specification bar.** CC-SPEC-1…11 in
  `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`.
  It is in force despite the path, because craft acts 6 and 7 bound it.
- **The delta form.**
  `.syzygy/governance/contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`
  and `SEMANTIC-DELTA-TEMPLATE.md` beside it.
- **The code the funnel measured**, for checking the delta's claims about
  today's behaviour: `packages/three-surface-poc-core/src/project-shape-extraction.ts`
  and `project-shape-manifest.ts`.
- **Doctrine.** VIS-1, VIS-2 and VIS-3 in `.syzygy/governance/doctrine/vision.md`.

## Acceptance criteria

1. **Ruling content.** The package carries each of P-82's four answers:
   - Q1: a delta only, drafted under the normative-change workflow;
   - Q2: a partially extracted outcome designed in it, not built;
   - Q3: unenumerated headings as a surface flag, a counted and routed
     Unknown;
   - Q4: root-independence flags in the same delta.

   Every reading the drafter chose where the ruling is silent is named and
   put to the owner.
2. **The specification bar.** The amended PWB-REQ-002 still meets CC-SPEC:
   one obligation form, scope, a sweep oracle with a denominator, an
   observable, oracle independence, a falsifier, and scenarios its text
   carries. Each new obligation has an oracle limb, a falsifier limb and a
   scenario.
3. **The two questions the container-shape packet left for this review.**
   - **The category rule.** Is a class's and a category's item denominator
     Unknown in every case where it counts a failed class or a class with an
     unenumerated heading, and is a class that read never allowed to mask a
     failed sibling?
   - **How far the exactness sentence reaches.** Does the narrowed "no
     partial item set" rule still bind every grammar, loaded or built-in?
     Is anything that failed a whole source before now silently partial?
4. **Signed bytes.** No signed byte outside the patches changes. Every
   requirement but PWB-REQ-002 is byte-identical, the text before the reader
   definitions is unchanged, and every signed line of the reader definitions
   and PWB-REQ-002 survives except those the delta quotes as replaced.
5. **Honest claims.** Each [Observed] claim is checkable at the named
   commit; [Unknown] is used where nothing was read, in particular about
   Butlers' V1 index. The package claims no adoption, authorizes no build or
   read, and names the residuals the sign-off change must carry and the
   packages it collides with.
6. **Mechanics.**
   - `--check` and `--selftest` pass, and each selftest mutant fails on its
     own predicate (rule 6).
   - The dependency file equals regeneration, and
     `scripts/build_polaris_project_wide_contract_coverage.py --check` passes
     over the proposed bytes.
   - The capability totals equal computation.
   - `scripts/build_pwb_release_label_amendment.py --check` still passes.
7. **Plain language.** A fresh reader can restate what changes and what does
   not (VIS-3).

Run the checks in a clone, not this worktree (verification rule 7):

- `python3 scripts/build_pwb_class_granular_extraction_amendment.py --check`
- `python3 scripts/build_pwb_class_granular_extraction_amendment.py --selftest`
- `python3 scripts/build_pwb_release_label_amendment.py --check`
- `python3 scripts/check_governance.py`
- `python3 scripts/check_spec_reconciliation.py --check`

## Output contract

Write your raw output verbatim to the path the dispatcher names; the
filename ends in `-RAW.md`. Over the first four non-blank lines:

- line 1 is `# ` followed by a title;
- line 2 is `Reviewed commit: ` followed by the 40-hex commit you read;
- line 3 is `Manifest SHA-256: ` followed by the lowercase 64-hex sha256 of
  the bytes of `PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-MANIFEST.txt` at that
  commit, computed by script (`git show <commit>:<path> | sha256sum`). It is
  never a row inside the manifest;
- line 4 is `Verdict: ` followed by exactly one of `CONFIRM`,
  `CONFIRM WITH EXCEPTIONS` or `REVISE`.

Then add a `## Findings` section, numbering findings as
`**Finding N — title** (blocking|revise|note)`. CONFIRM WITH EXCEPTIONS means
every finding is a `note`.

**Stopping rule, set before this round.** One round only. A notes-only
round, meaning `CONFIRM` or `CONFIRM WITH EXCEPTIONS` with every finding a
note, clears the bytes it read. Any other verdict is repaired, no second
round is dispatched, and the package goes to the owner with the repaired
bytes unreviewed.
