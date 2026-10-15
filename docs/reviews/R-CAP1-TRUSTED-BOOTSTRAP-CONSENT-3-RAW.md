# R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-3 — confirmation review of cap1-trusted-bootstrap-consent
Reviewed commit: 70af85e86dc17e8f6d1378f36575781c55084ec0
Manifest SHA-256: 1a9f76df2a6e29f9f8e724138c7687900357f8248ca2d3f8093eadefe99ea8a8
Verdict: REVISE

Fresh-context CC-REV-1 (security/authority-boundary) and CC-REV-4 (fresh-reader)
confirmation review of the rebased candidate package cap1-trusted-bootstrap-consent.

## Summary

[Observed] Subject freeze: `sha256sum` of
docs/evidence/cap1-trusted-bootstrap-consent-2026-10-15/review-3-subject.json is
1a9f76df2a6e29f9f8e724138c7687900357f8248ca2d3f8093eadefe99ea8a8, equal to the
expected value. The manifest names 14 paths; `find` over
openspec/changes/cap1-trusted-bootstrap-consent/ returns exactly those 14 files,
and all 14 per-file `sha256sum` values equal the manifest.

[Observed] Review-2 comparison: the candidate bytes reviewed in round 2 are
recoverable from git. Commit c596fda4ab35edd0a99c85cb3fec26895bd33f3d contains
the directory, and a scripted hash of each of its 14 blobs equals
docs/evidence/cap1-trusted-bootstrap-consent-2026-09-14/review-2-subject.json
(14/14; that manifest's own sha256 is
90f46579420aa43ea6e5e341fdf9b92d84da1283742d8f4e7964e77a4ca71790, the value
R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-2-RAW.md:19 records). Of the 14 files, 8 changed
between that commit and the reviewed commit: BASELINE.json, CAPABILITY-COVERAGE.md,
GOVERNING-DEPENDENCIES.json, PREDECESSOR-REQUIREMENTS.md, README.md,
REVIEW-DISPOSITION.md, VALIDATION.md, proposal.md. This matches the brief's list.
spec.md, design.md, CONTRACT-COVERAGE.md, APPLYING.md, tasks.md and .openspec.yaml
are byte-identical to review 2.

Criterion 1 (rebase correctness) [Observed]: all 15 BASELINE.json
protected-predecessor digests equal the worktree file's sha256, the blob at
baseline 2d6a36328f638d3ce52605e88328c1ac7b4c9895, and the blob at HEAD (15/15
on all three). The baseline is an ancestor of the reviewed commit
(`git merge-base --is-ancestor` exit 0). Of the 13 original rows, 11 hash
the same at the old baseline a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d and now;
the CAP1 design.md and proposal.md moved. Their new digests equal the successor
column of CAPABILITY-1-READABILITY-SUCCESSOR-ACT.md:36-37, which states "The
specification, both coverage tables and the generated dependencies are
unchanged" (line 40). Both GOVERNING-DEPENDENCIES.json source_files hashes match.
The adopted CAP1 spec.md is byte-identical at a9f671e9 and now. I recomposed the
42-requirement spec by replacing the two adopted bodies with the candidate bodies,
and it hashes to the recorded composed_spec_sha256,
33a3e8d3a5e4ad427aa93cb350a557dd746ce527a946306e7e89b4c65e390ddb. Both
PREDECESSOR-REQUIREMENTS.md excerpts equal the adopted CAP1-REQ-011 (adopted
spec.md:359) and CAP1-REQ-046 (spec.md:1501) bodies exactly (scripted
comparison). `openspec validate cap1-trusted-bootstrap-consent --strict
--no-interactive` reports valid.

Criterion 2 (non-normative rebase) [Observed]: the full diff shows no change to
any requirement, scenario, warrant, coverage row or design sentence. The edits are
the baseline commit, digests, two added protected rows, banners, dated marks and
disposition/validation text. Every new factual sentence I tested holds except
one: the "never committed" claim (Finding 1).

Criterion 3 (consent/trust boundary) [Observed/Inferred]: the replacements are
faithful to RFC3-16 as currently written. RFC3-16(b) items 1–9 and "Omitting the
field is invalid; explicit absence is not independent verification"
(governance-homes-and-owner-acts.md:294-297) map to candidate spec.md:7 ("An
omitted audit-identity field is invalid; explicit absence is permitted only for
state (1)"). "A failed, unavailable or indeterminate A1 attempt never creates state
(1)" (:306-307) maps to spec.md:7 and the scenario at :35-38. The RFC3-16(a)
failure list "Missing, digest-mismatched, wrong-scope, stale, expired, superseded,
revoked, unattributed or non-human act state blocks the dependent effect, renders
the authorization Unknown and mints a contradiction routed to owner adjudication"
(:319-322) is carried, refused before dependent reads, at spec.md:7 and :30-33.
"A machine may prepare an act for owner attendance; it may not mint, impersonate,
approve, widen, revoke or reinterpret one" (:248-250) is respected by spec.md:40-43
and design.md:38-43. The trust premise "does not prove the tree could not forge
the record" (:245-247) is restated, not smoothed, at spec.md:75. The
render-vocabulary rule "never 'verified'" (:391-392) is carried at spec.md:92.
No place widens authority, implies consent from absence, or lets a machine-only
act admit observation.

Criterion 4 [Observed]: each of the 10 added scenarios has a producible
controlled case, literal expected tuples specified independently of the
implementation, intercepted-read observables and a stated falsifier (spec.md:75,
:77, :135). CC-SPEC-4's "oracle is not defined by, and does not consult, the
implementation under test" is met. CONTRACT-COVERAGE.md maps RFC3-16(a)/(b) items
1–9/(c), RFC3-7/RFC3-30 and RFC6-13/14/RFC7-33 per consequence, and keeps general
non-consent admission Unknown (:43). Its quoted predecessor row (:10) is verbatim
predecessor CONTRACT-COVERAGE.md:109. Re-derived CC-SPEC-11 counts: the candidate
table has 15 rows (A-01..A-10, X-01..X-05: 10 covered, 5 excluded, 0 unresolved).
The 10 A rows correspond one-to-one with the 10 added scenario titles. The
predecessor CAPABILITY-COVERAGE.md has 26 unique O/X/U rows (O-01..O-21, U-01,
X-01..X-04), and O-05/O-10/O-19/U-01 are present as cited.

Criterion 5 [Inferred]: a fresh reader can say what adoption would do. It lets an
explicitly human-selected, uncorrelated state-(1) act admit exact
repository-observation scope without an A1 provider. Correlated state (2) stays
distinct and never falls back. Invalid acts are refused before reads, and the
exact provenance is disclosed in both channels. A reader can also say what
adoption would not do: no provider, no implementation authority, no consent for
any repository, and no detection of byte-identical forgery. The trade-off is
stated plainly at proposal.md:17-20 ("hashes detect changed bytes, not
forgeries") and spec.md:75.

Criterion 6 [Observed]: nothing claims adoption, implementation authority,
consent for any repository, or a fresh-clone battery pass. See README.md:3-6,
proposal.md:3-5 and :65-70, VALIDATION.md:4 and :21-22, and APPLYING.md:44-49.
The decision packet README.md:6 names exists at that path.

## Findings

**Finding 1 — The rebase record states as Observed that the candidate was never committed, but git holds a commit containing it** (revise)
[Observed] REVIEW-DISPOSITION.md (rebase section, first sentence) reads: "[Observed]
The candidate was never committed; it sat untracked in the main checkout." Commit
c596fda4ab35edd0a99c85cb3fec26895bd33f3d is a single-parent commit dated
2026-10-04 with the message "Merge origin/main into agent/dossier-wiring". It
adds all 14 files under openspec/changes/cap1-trusted-bootstrap-consent/, and its
blobs hash to the review-2 subject manifest 14/14. `git branch -a --contains`
reports it reachable only from the local branch
governance/redis-sitting-simulation, not from main or any remote ref. Writing
"never committed (to main or any pushed ref)" would be true. The unqualified
sentence is not, and it is labelled Observed, which criterion 2 forbids. The
error helps more than it hurts: that commit independently corroborates the
review-2 bytes. A one-sentence correction (qualify the claim, or mark and date it
in place, and optionally cite the commit as provenance) is enough. No normative
byte is affected. Under rule 10 the correction would retire this review for
REVIEW-DISPOSITION.md only.

**Finding 2 — Adoption must say how the bound predecessor coverage text that would go stale is superseded** (note, for the owner)
[Inferred] If adopted, predecessor CONTRACT-COVERAGE.md:109 would still say "no
adopted requirement covers valid-state admission or the other invalid-act cases".
Its Part A totals at :140-142 ("65 consequence rows over 38 clauses — 63 covered,
2 Unknown") would also go stale. Those bytes are bound and the candidate rightly
leaves them unedited. It uses a candidate overlay instead
(CONTRACT-COVERAGE.md:14-19). APPLYING.md:23 and :34-40 already acknowledge that
CC-REV-2 ("No merge may leave mainline with an invalidated authoritative artifact
still asserting the old truth", review-and-documentation.md:93-94) needs the
consequences settled in one adoption transaction. The owner should make sure the
adoption act says explicitly that the overlay supersedes row 109 and those totals
(or that a coverage successor replaces them), so default-route readers are not
left with the old truth. This does not block the candidate specification.

Read-only review; no fixes authored. Preserve this raw output unchanged under CC-REV-6.
