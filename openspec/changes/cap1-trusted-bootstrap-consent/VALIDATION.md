# Candidate validation record

[Observed] Candidate checked on 2026-09-14 against the baseline in BASELINE.json.
This is authoring validation, not an implementation/clone-battery pass or adoption.

- `openspec validate cap1-trusted-bootstrap-consent --strict --no-interactive`:
  valid.
- Stock th-projects `spec-trace-check.py --authoring` on the whole working repo:
  178 errors; a temporary HEAD archive of the same OpenSpec population reports
  176 pre-existing errors. The two candidate findings require invented
  REQ-project-registration-and-honest-shape-visibility-NNN identifiers. This
  repository's adopted CAP1 IDs are stable under CC-SPEC-3/CC-REV-7 and must not
  be renamed to satisfy that incompatible generic convention. No checker or
  baseline was modified or suppressed. All other candidate structure predicates
  passed that checker; this is an explicit ID-convention exception, not a claim
  that the stock whole-repository authoring gate passed.
- Independent heading/ID comparison found the same two exact predecessor titles
  and stable IDs; both original scenario names remain. Baseline protected-file
  hashes match. These comparisons are scripted, not hand-transcribed.
- `python3 scripts/check_governance.py`: 32 OK, 20 WARN, 0 FAIL across 52 checks.
  This working-tree checker uses its own tracked-file population; new candidate
  files are not proven by that result. Do not claim a fresh-clone battery pass.

[Unknown] Implementation behavior, hostile real-act detection, full live CAP1
coverage and owner comprehension have not been tested. Independent candidate
review is recorded separately and cannot authorize implementation or adoption.

## Corrected candidate, 2026-09-14

[Observed] OpenSpec strict validation passed again after correction. Candidate-only
trace validation in an isolated temporary OpenSpec root reports exactly the two
documented legacy-ID format findings and no other candidate findings. The existing
CAP1 dependency parser successfully parsed the 42-requirement composition; the
generated six-class union matched a second literal-list extraction. The capability
amendment table contains 10 covered and 5 non-goal-excluded rows, with no unresolved
amendment behavior row; the unchanged predecessor has 26 unique obligation rows.
Independent semantic review must still confirm the declared obligation partition.
Protected predecessor hashes still match. No runtime tests were run.

## Rebased candidate, 2026-10-15

[Observed] Protected-predecessor digests were recomputed by script against main
at 2d6a36328f638d3ce52605e88328c1ac7b4c9895: 11 of the original 13 matched;
the Capability 1 proposal.md and design.md had moved under the 2026-09-29
readability successor act. BASELINE.json now records all 15 rows (the 13 plus
that act and RFC3-16's home file) at that commit, and a re-run of the
comparison script reports 15/15 match. Both spec files named in
GOVERNING-DEPENDENCIES.json hash as recorded, so the composition was not
regenerated. `openspec validate cap1-trusted-bootstrap-consent --strict
--no-interactive`: valid. The governance check result is recorded in the
commit that lands this candidate, not here. No runtime tests were run; the
"protected predecessor hashes still match" sentence above refers to the
2026-09-14 baseline.
