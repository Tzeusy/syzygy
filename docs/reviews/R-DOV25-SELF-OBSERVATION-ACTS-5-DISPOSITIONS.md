# R-DOV25-5 dispositions — self-observation act packets, confirmation round 5

> **Candidate record — binds nothing.** This page dispositions the notes of
> one review. It performs no act, issues no direction and edits no reviewed
> byte.

**Review:** `R-DOV25-SELF-OBSERVATION-ACTS-5-RAW.md`, retained verbatim
beside this page. Its verdict line (line 2) reads `Verdict: CONFIRM WITH
EXCEPTIONS`. It has no revise-severity finding and four notes, n10–n13
(raw lines 95, 103, 111 and 121).

**Subject:** the three candidate packets of
`.syzygy/governance/contracts/candidates/pwb-self-observation-acts/` and
`scripts/build_pwb_self_observation_acts.py`, as reviewed at commit
`1a5c03a`. The review binds the packets by the three manifest row digests in
the raw's head (line 4), the act arguments the package's REVIEW-BRIEF
predicate names.

**Why nothing here edits the packets or the builder.** Under the 2026-09-26
sitting rule (`POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1), a notes-only
CONFIRM WITH EXCEPTIONS clears the exact bytes the review read. Any edit to
them retires that review (rule 10). This commit adds only this page, the raw
and the `docs/README.md` row and count; the packets and builder have no diff
against `1a5c03a` [Observed: `git diff --stat 1a5c03a HEAD`].

| Note | Summary | Disposition |
|---|---|---|
| n10 | The end-to-end selftest case accepts a single draft finding where its disposition says "the two"; builder mutants B11 and B17 survive `--selftest`. The live end-to-end run produces both findings. | **Routed to `syzygy-dov.33`.** Selftest rigor only; no stated `--check` guarantee is false. |
| n11 | `pol()` drops the final newline, so about 26 policy value mutants fail for that reason alone; builder mutant B12 survives. | **Routed to `syzygy-dov.33`.** |
| n12 | The patch file's own bytes are unpinned: extra hunks or prose pass `--check` and are shown by `--diff`; an extra file-creation hunk makes `--check` fail after `--apply policy`. | **Routed to `syzygy-dov.33`.** No act argument changes; the policy act binds the patch output, not the patch file. |
| n13 | "Any byte change to what the patch produces" holds only relative to the base policy; a changed base (pre-adoption) or installed policy (post-adoption) passes the builder's `--check` after `--write`. Pre-adoption, `check_governance.py` CG-7e fails it. | **Routed to `syzygy-dov.33`**, to add the scoping clause the reviewer suggests. |

`syzygy-dov.25` stays open: the owner has not performed or declined any of
the three self-observation acts.
