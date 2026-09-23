# Review brief — Polaris edit/repair deletion-account scenario

> Candidate — binds nothing. Bead `syzygy-dov.23`. Review this package with
> only itself, `SEMANTIC-DELTA.md`'s cited baseline files, and the
> acceptance criteria below — per CC-REV-6, without the authoring
> conversation.

## Baseline citations (read these, not this brief's paraphrase)

- `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`,
  the P-73 row — the owner warrant this package answers.
- `.syzygy/governance/policies/craft-and-care/review-and-documentation.md:52`
  — CC-REV-2, "The same-logical-change rule."
- `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`
  lines 178-222 — the current text of REQ-polaris-generation-006 this
  package patches.
- `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`
  lines 300-344 — the predecessor's own copy of REQ-006, superseded in
  force for this ID; confirm it is genuinely not the one being patched.
- `PROJECT-STATUS.md` line 34 — the scenario-count sentence this package
  also patches.
- `packages/polaris-generation-core/src/provider-draft.ts` (schema
  definitions, `validateStage`) and `pipeline.ts` (stage sequencing) — the
  code-level evidence this package cites; not modified by this package.
- `proposed/spec.md.patch` and `proposed/PROJECT-STATUS.md.patch` — the
  actual proposed bytes; every other document in this package quotes them,
  none of them defines them.
- `POLARIS-EDIT-REPAIR-DELETION-SCENARIO-MANIFEST.txt` — the generated,
  scripted post-apply digests.

## Numbered, falsifiable review criteria

1. **Patch scope.** Does `proposed/spec.md.patch` touch anything other than
   (a) appending one sentence to REQ-006's requirement paragraph and (b)
   inserting exactly one new `#### Scenario:` block before `Form: lifecycle
   transition.`? Run `git apply --check` against current HEAD to confirm it
   still applies cleanly, then diff its hunks against this brief's claim.
2. **No other requirement touched.** Grep the patch for `### Requirement:`
   or `ID: REQ-polaris-generation-` — it must appear only in the unmodified
   context lines around REQ-006, never inside a `+` line targeting a
   different requirement.
3. **Scenario is falsifiable and distinguishable.** Read the new scenario's
   three clauses: does "the output is invalid unless its change account
   names each omitted block's id with a removed action and a reason" state
   an actual, checkable failure condition (not just aspirational prose)?
   Does the third clause's "valid and is distinguishable in the record from
   a repair that changed content" avoid conflating "nothing needed fixing"
   with "something was silently dropped"?
4. **PROJECT-STATUS.md patch is the only change to that file.** Confirm the
   patch's single hunk changes only the digit "177" to "178" on the cited
   line and nothing else in the file.
5. **Manifest is honest.** Run
   `python3 scripts/build_polaris_edit_repair_deletion_scenario.py --check`
   and read its stdout (not just its exit code, per verification rule 4):
   it must report 0 manifest mismatches, the scenario delta confirmed by
   two methods, and 0 sibling patch collisions.
6. **Selftest actually fails closed.** Run
   `python3 scripts/build_polaris_edit_repair_deletion_scenario.py --selftest`
   and read its per-fixture output. Independently pick one fixture (e.g.
   the manifest-digest-tamper one) and hand-verify, by reading the
   builder's `_fixture_root`/mutation code, that the mutation it applies
   really is the one it claims and not a no-op that happens to still
   raise for an unrelated reason.
7. **No governed byte was edited in place.** `git status` and `git diff
   --stat` against `origin/main` for this branch must show the spec file
   and `PROJECT-STATUS.md` themselves as **unchanged**; only new files
   (this package's directory, the builder script, and
   `check_governance.py`'s registration additions) may appear.
8. **CG-7d/CG-7h registration.** Confirm
   `scripts/check_governance.py`'s `_act_subjects()` and
   `ACT_DIGEST_COPY_FILES` carry an entry for this package's act phrase,
   gated on the package's own existence (not unconditionally active), and
   that no `PWB_SUCCESSOR_CHAIN`-equivalent chain-link entry was added (per
   AGENTS.md: "register a phrase and a copy, never a chain link").
9. **CG-26 untouched.** Confirm no line was added to the PROJECT-STATUS
   verification battery, the hosted CI workflow, or the battery's own
   check-count sentence — AGENTS.md reserves that for one later
   integration commit.
10. **`python3 scripts/check_governance.py` is 0 FAIL** on the branch head,
    read from its printed summary line, not inferred from exit code alone.
11. **Owner questions are genuinely open, not decided here.** Confirm
    `SEMANTIC-DELTA.md`'s three open questions are phrased as questions,
    with no default answer smuggled into the proposed patch text itself.
12. **Landing-order note is present and computed live.** Confirm
    `IMPACT-LEDGER.md`'s sibling-collision sweep names its method and
    denominator, and that a fresh run of that same sweep (`for d in
    .syzygy/governance/contracts/candidates/*/; do [ -d "${d}proposed" ] &&
    echo "$d"; done`) at review time still returns the same result the
    ledger claims — or, if a new sibling package with a `proposed/`
    directory has since been added, that the reviewer re-runs `--check`
    and confirms `composition_findings()` correctly flags it.

## What a CONFIRM verdict means here

That the two patches are scoped exactly as SEMANTIC-DELTA.md describes, the
manifest's digests are the actual scripted output of the builder (not
hand-edited), the six rule-6 fixtures are genuine (not vacuous), no
governed byte was touched in place, and the three open questions are
correctly left to the owner rather than pre-decided. A CONFIRM here does
**not** mean the specification amendment is adopted, that slice 4's
implementation is authorized, or that the `PROJECT-STATUS.md` digit is
live — those require the owner's act.
