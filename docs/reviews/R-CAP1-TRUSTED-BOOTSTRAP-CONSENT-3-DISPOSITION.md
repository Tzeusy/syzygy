# R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-3 — disposition

Reviewed record: docs/reviews/R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-3-RAW.md

[Observed] Verdict `REVISE` (raw line 4), over commit
70af85e86dc17e8f6d1378f36575781c55084ec0 and the subject manifest
docs/evidence/cap1-trusted-bootstrap-consent-2026-10-15/review-3-subject.json.
The round has two findings, one revise and one note. Each was repaired once.
Under the owner's 2026-09-26 stopping rule no round 4 was dispatched, so the
repaired bytes are unreviewed.

1. **Finding 1 (revise): the "never committed" sentence is false.** Repaired
   in the candidate's `REVIEW-DISPOSITION.md`. The sentence now reads "never
   committed to main or to any pushed ref" and names the local, unpushed
   commit c596fda4ab35edd0a99c85cb3fec26895bd33f3d (2026-10-04). That commit
   was re-checked with `git branch -a --contains`, which reports only the
   local branch governance/redis-sitting-simulation. The packet's matching
   status sentence was repaired the same way. No normative byte changed.
2. **Finding 2 (note, for the owner): adoption must supersede the stale
   predecessor coverage row and totals.** Carried into the owner packet
   `.syzygy/governance/decisions/CAP1-TRUSTED-BOOTSTRAP-CONSENT-OWNER-DECISION-PACKET.md`
   under Question 1. The adoption change must state that the overlay
   supersedes the bound RFC3-16(a) row and the Part A totals, or carry a
   coverage successor. No candidate byte changed for it.

The edit to `REVIEW-DISPOSITION.md` moves that file's hash away from
review-3-subject.json. Any later round must freeze a new subject.
