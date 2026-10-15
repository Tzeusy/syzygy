# Round 2 repair — public-source screening scope, version 4

> **Candidate — binds nothing.** Repairs for the findings of
> `docs/reviews/R-OLMR-SCREENING-SCOPE-V4-2-RAW.md` (verdict line 5:
> `Verdict: REVISE`), classified first in `ROUND-2-DISPOSITIONS.md`. Made
> 2026-10-15 under the lead's final-cycle direction: one repair, one round 3;
> a round-3 REVISE goes to the owner with no round 4.

| Finding | Severity | Repair |
|---|---|---|
| 1 — common credential shapes keep the secret line | revise | **Both arms.** (b) `secretRedaction.redactedClasses: ["project-documentation"]`: a code-content body and every other class stay excluded whole on any match (whole-file fixtures "code body with a token", "unclassified root file with a token", "nested README with a token"; predicate "redaction widened to code-content caught" and fixture-flip mutant). (a) The delta's "What it gives up" and the packet's "What it costs" name the six shapes as reaching the packet when they occur in a documentation file, with `AKIA…` and `ASIA…` written out |
| 2 — the disclosed residuals reproduce as stated | note | No change |
| 3 — "any PEM header" wider than the literal check | note | Check widened, fail-closed: `wholeArtifactLinePattern` `^[ \t]*-{4,}[ \t]*BEGIN` keeps the body whole on any dashed BEGIN header line (PEM and RFC 4716, indented or not), and `wholeArtifactFragments` holds the base64 starts of `-----BEGI` and `---- BEGI`. Fixtures "RFC 4716 key beside a badge", "indented PEM header beside a badge", "base64 PEM in a Secret example"; predicates "a dropped dashed-header pattern caught", "a dropped PEM fragment caught". The delta names what is still not caught (a base64 key encoded from another offset) |
| 4 — builder docstring describes the pre-round-1 rule | note | Rewritten to the current rule |
| 5 — ledger residue; every-offset scan cost | note | The ledger names the nine remaining policy-path files (breakage Unknown, assessed at install) and the per-offset scan's cost: no early stop, a sticky loop, and possible quadratic backtracking in `credential-bearing-url`, bounded by the resource limits with a breach excluding the file whole |

Recovery for the trial's README (41 spans) is unchanged by the narrowing:
README.md is project-documentation, so its spans that cite neither line 1 nor
line 2 become admissible; how many is still Unknown.

Verification: builder `--write`, then `--check` passes and `--selftest` holds
40 of 40 predicates.
