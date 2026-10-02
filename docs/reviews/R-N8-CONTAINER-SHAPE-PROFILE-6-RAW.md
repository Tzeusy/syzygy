# Review round 6 — N8 container-shape profile amendment (syzygy-u05.8)
Reviewed commit: 2b7f084c0ef9215605e06d83b795a42ee7f9b45f
Manifest SHA-256: 84d261b23fac519a6ee909f9b0570c2d1cdc03ba07c5dcefda55dd55b00fecd4
Verdict: REVISE

Fresh-context review (CC-REV-1) of
`.syzygy/governance/contracts/candidates/pwb-container-shape-profile-amendment/`
at the commit above. Earlier raws and dispositions were not read. The sign-off
would be version-tagged; the manifest digest in the head is informational.

## What was run

- [Observed] `--check` passes (11 rows, 3 patched, 8 unchanged). `--selftest`
  prints "181 mutants killed" and `EXPECTED_KILLED = 181`
  (`scripts/build_pwb_container_shape_profile_amendment.py:520`).
- [Observed] In a `git archive` copy under the scratchpad, the three patches
  apply cleanly over the current tree (which already carries the opening-band,
  render-mode, machine-view, missing-currency and dismissal-expiry edits).
  `sha256sum` of the patched spec.md, CAPABILITY-COVERAGE.md and
  GOVERNING-DEPENDENCIES.md equals the three proposed manifest rows
  (a12d9696..., b26c4dfd..., 90ed762b...). In the patched copy
  `build_polaris_project_wide_spec_dependencies.py --check` passes,
  `build_polaris_project_wide_contract_coverage.py --check` reports 324 clauses
  represented, and `openspec validate polaris-project-wide-butlers-model
  --strict` reports valid.
- [Observed] Six patch mutants in the archive copy (refused-profile "never
  returns" made "may return"; "never zero" dropped; "at most two headings" made
  three; "never a heading" made "may be"; "does not restart" made "restarts";
  the unscoped Unknown clause), each fails `--check` on the pinned-text
  comparison and on its own named predicate (for example "loaded-profile bullet
  lacks refused profile does not fall back").
- [Observed] `python3 scripts/check_governance.py`: 31 OK, 21 WARN, 0 FAIL.
- [Observed] The shape and key-form sentences were read against
  `project-shape-extraction.ts` for the shapes the Butlers grammar uses
  (topLevelListItems, tablesOf, headedTable, ORDINAL_H2, TOML_TABLE/TOML_NAME,
  LINK, LEADING_BOLD/CODE, DASH_AFTER_LABEL). No sentence is looser or stricter
  than the code for those paths. The `CLASS_ROWS` category mapping
  (project-shape-coverage.ts:85-95) with `LAYER_ROWS` ordinals 1-6 matches the
  declared-item bullet. The P-74 Q2 and P-82 quotations match the Ruled cells.
  No `containerShapes`/`classGrammar` or profile exists in the adopted registry
  entry today, so "until a profile is declared" is currently true.
- [Observed] Reachability, hidden/collapsed content and PWB-REQ-020 parity are
  not touched by the text and not claimed by it.

## Findings

**Finding 1 — the PWB-REQ-002 oracle requires equality with the written grammar for a Butlers profile the same text requires to be Unknown** (revise)
`proposed/spec.md.patch:205-211` (patched spec.md lines 267-274) says that "for
Butlers read through its loaded profile, both also apply the grammar written in
these reader definitions and must produce the same identities and D". The case
list at the requirement (patch lines 190-196) and scenarios 2 and 3
(patched spec.md from line 302) are about "Butlers' loaded profile" that gives
a class no row or names an out-of-vocabulary shape; there the profile reading
must render the class and its category Unknown, while the written grammar
yields a known D. The two extractors then disagree, which the first falsifier
clause ("the independent extractors disagree") calls a failure, so a conforming
observer fails its own oracle on a case the sweep is told to include. The
text also says Butlers' profile "declares exactly the following extraction
grammar" (patched line 164), which is true only of a conforming profile, so the
oracle clause needs the same restriction. Repair: scope the written-grammar
comparison to a Butlers profile that reproduces the written grammar (the
scenario 1 case), and state that for a profile that leaves a class unreadable
the expected D is Unknown. This is normative text that can condemn lawful
behaviour, so it is not a note.

**Finding 2 — mutant counts in the prose are stale** (note)
`OWNER-DECISION-PACKET.md:365` says the selftest "now kills 196 mutants" and
`REVIEW-BRIEF.md:88` says "(196 mutants)"; `--selftest` kills 181 and the
builder fixes `EXPECTED_KILLED = 181` (line 520). The 181 reflects the
2026-10-02 regeneration (retired sibling-composition table). Re-derive both
sentences from the selftest output. `OWNER-DECISION-PACKET.md:350` ("185") is
a dated historical line and may stay if marked.

**Finding 3 — "cannot tell is or is not declared" pulls against the claim that today's code conforms** (note)
Patched spec.md lines 139-141 treat a profile "the observer cannot tell is or is
not declared for Butlers" as refused (Unknown). Today's observer has no loader
and consults no profile, so read literally it cannot tell, and
`SEMANTIC-DELTA.md` (Downstream impact 1; Warrant) and `IMPACT-LEDGER.md`
Table 2 say it conforms while none is declared. The registry admission could be
what lets it tell, but no sentence says so. Say who determines "declared"
(for example the adopted registry entry the observer is admitted under), or
list this with the limb-5 window in packet question 7.

**Finding 4 — the brief's raw-head predicate is not the one the versioned recorder parses** (note)
`REVIEW-BRIEF.md:101-117` still requires `Verdict:` second and a lowercase
`Manifest sha256:`, as the retired act recorder did.
`scripts/record_versioned_signoff.py:193-208` parses the first four non-blank
lines for one `Reviewed commit:`, one `Manifest SHA-256:` and one `Verdict:`
of `CONFIRM` or `CONFIRM WITH EXCEPTIONS`. This raw follows the recorder.
Refresh the brief's recording section so the next reviewer is not given two
conflicting heads.

## Remaining after Finding 1

Findings 2 to 4 are notes only. Nothing else found would make the normative
text wrong or unsafe: the Unknown propagation (class, category, every source
counted), the no-fallback rules, the exactness bullet and the unchanged Butlers
class bullets verified as described above.
