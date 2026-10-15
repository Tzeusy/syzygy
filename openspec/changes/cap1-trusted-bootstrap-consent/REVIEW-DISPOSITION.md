# Candidate correction record — 2026-09-14

[Observed] First independent semantic verdict: **REVISE**. First fresh-reader
verdict: **PASS**. Verbatim output retained at
docs/reviews/R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-1-RAW.md (a byte-identical copy,
made 2026-10-15, of the raw first kept at an ignored local path). It binds its
listed predecessor candidate hashes; subsequent edits retire that review for
the changed bytes.

1. Coverage/dependency omission: candidate CAPABILITY-COVERAGE.md partitions the
   declared amendment obligations and preserves the predecessor's residuals;
   CONTRACT-COVERAGE.md expands the affected consent consequences and explicitly
   retains general non-consent Unknown; GOVERNING-DEPENDENCIES.json is generated
   from the full 42-requirement composition and independently checked. Submitted
   for confirmation by the independent reviewer, not self-confirmed.
2. Human-attendance oracle: the negative case now supplies observable missing
   owner-act evidence or a declared non-human actor. A fixture manifest owns the
   expected refusal/read count independently of the implementation. A separate
   limitation states that byte-identical forgery is not mechanically detectable
   under bootstrap and remains unauthorized. Submitted for independent confirmation.

No owner decision has been replaced by a review verdict. Adoption, implementation,
record encoding and authority-source acquisition remain separately gated.

## Confirmation review 2 — 2026-09-14

[Observed] Review 2 is **PASS** / **PASS**, CC-SPEC-11 **CONFIRMED**
(docs/reviews/R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-2-RAW.md lines 1–3), over the
14-file subject manifest retained byte-identical at
docs/evidence/cap1-trusted-bootstrap-consent-2026-09-14/review-2-subject.json.
Both review-1 findings are recorded there as resolved.

## Rebase onto current main — 2026-10-15

[Observed] Until 2026-10-15 the candidate was never committed to main or to
any pushed ref; it sat untracked in the main checkout. (One local, unpushed
commit, c596fda4ab35edd0a99c85cb3fec26895bd33f3d of 2026-10-04 on the local
branch governance/redis-sitting-simulation, carries all 14 files with blobs
equal to review 2's subject, per review 3, finding 1.) Re-hashing BASELINE.json's 13 protected predecessors against main at
2d6a36328f638d3ce52605e88328c1ac7b4c9895 found 11 unchanged and 2 moved: the
Capability 1 proposal.md and design.md, both replaced by the owner-signed
readability successor of 2026-09-29
(decisions/CAPABILITY-1-READABILITY-SUCCESSOR-ACT.md, which states the
specification, both coverage tables and the generated dependencies are
unchanged). The adopted CAP1 spec.md and the candidate spec.md are
byte-identical to the hashes GOVERNING-DEPENDENCIES.json records, so the
42-requirement composition and its dependency union are unchanged. RFC3-16's
home file was also restyled by the 2026-09-28 contract readability act; it
was not in the original protected set.

Changes made, all mechanical and scripted: BASELINE.json and
GOVERNING-DEPENDENCIES.json carry the new baseline commit; BASELINE.json
carries the two moved digests and adds the readability successor act and the
RFC3-16 home file as protected predecessors (15 rows). README.md and
proposal.md carry a "Candidate — binds nothing" banner; this record and
VALIDATION.md cite the retained review copies; PREDECESSOR-REQUIREMENTS.md
names the rebased baseline; CAPABILITY-COVERAGE.md's "confirmation is pending"
sentence is marked and dated in place. No requirement, scenario, warrant,
coverage row or design sentence changed. These edits retire review 2
for the changed bytes; confirmation review 3 is bound to the rebased bytes.
