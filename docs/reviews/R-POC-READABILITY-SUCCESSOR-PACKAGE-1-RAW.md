# R-POC-READABILITY-SUCCESSOR-PACKAGE-1 — POC readability successor package review
Verdict: CONFIRM WITH EXCEPTIONS
Manifest-file SHA-256: 221f1ececa321bf0cc6cd5e01f401e9eada38466c3c00dde43095f8cb8a0cd4d
Reviewed commit: e3878c5493c27edc7d89f87e5f5814624c02587b

Reviewer: fresh-context Claude agent (Opus 5.5), 2026-09-29.
Base: origin/main 41ec6760bfb93e51ad3828112051a53cff5f0bc5 (merge-base of the
reviewed commit). Focus range: a40bf82..e3878c5 (commits f4ff181, e3878c5).

## Scope

The owner-decision package
`.syzygy/governance/contracts/candidates/three-surface-poc-readability-successor/`
at the reviewed commit, with attention on what changed after review 4
(`docs/reviews/R-POC-READABILITY-SUCCESSOR-REVIEW-4-RAW.md`, committed at
a40bf82): the new recorder
`scripts/record_three_surface_poc_readability_successor.py`, the builder
changes in `scripts/build_three_surface_poc_readability_successor.py`, the
CG-7d/CG-7e registration and activation selftest in
`scripts/check_governance.py`, the rewritten `OWNER-DECISION-PACKET.md`, and
the battery wiring in `PROJECT-STATUS.md` and
`.github/workflows/governance-docs.yml`. Per-requirement semantic review was
not redone; three requirements were spot-checked. Governing references:
AGENTS.md (hard prohibitions, verification rules, governance recorders),
`THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md`, `ACCEPTANCE-ACT-RECORD.md`, and the
sibling `scripts/record_spec_policy_readability_restyle.py`.

All experiments ran in scratch clones (`pre`, `adopt`, `mut`) under the
review scratchpad; the reviewed clone was not edited.

## Facts established

1. [Observed] `sha256sum` of
   `THREE-SURFACE-POC-READABILITY-SUCCESSOR-MANIFEST.txt` at the reviewed
   commit reproduces the digest in the head above; the packet's one phrase
   (packet line 18) carries the same argument. A repository-wide grep for the
   label outside `docs/reviews/` finds exactly that one line.
2. [Observed] `git diff --stat a40bf82 e3878c5` over the package directory
   and `openspec/` touches only `OWNER-DECISION-PACKET.md`: the manifest and
   the four `proposed/*.patch` files are byte-identical to the bytes review 4
   bound. Review 4's raw carries one `Verdict` line (`CONFIRM`, line 7) and
   one manifest-binding line naming this digest (line 4).
3. [Observed] `git diff --name-only a40bf82 e3878c5` lists 8 files:
   the workflow, the packet, `PROJECT-STATUS.md`, `docs/README.md` (partition
   count 280 to 284), one evidence JSON, the builder, `check_governance.py`
   and the new recorder. None is under `apps/`, `packages/`, `openspec/` or
   `.syzygy/governance/decisions/` (grep over the list: no match). Criterion 6
   holds.
4. [Observed] PREDECESSOR table. Five rows equal the rows of
   `THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md` lines 44-49 (proposal, design,
   spec, GOVERNING-DEPENDENCIES, .openspec.yaml). The CONTRACT-COVERAGE.md row
   is not the sign-off act's row but equals row 10 of
   `general-trusted-bootstrap-authorization/TRANSACTION-MANIFEST.txt`, which
   is the file's current digest. All six equal the live bytes at the reviewed
   commit. `tasks.md` is correctly outside the six signed subjects.
5. [Observed] Recorder refusals (criterion 1), read in code and exercised by
   the selftest: unpinned; phrase not `fullmatch` of `LABEL: <64 hex>`;
   argument not equal to the recomputed manifest digest; manifest digest not
   equal to the pin; raw sha not equal to its pin; `Verdict` lines not
   exactly one or not `CONFIRM` / `CONFIRM WITH EXCEPTIONS`; manifest-binding
   lines not exactly `[pinned digest]`; any subject off its predecessor
   (via `check()` returning candidate only when all six equal PREDECESSOR);
   builder `check()` findings; proposed bytes not hashing to the manifest
   rows. All preflights run before the first write.
6. [Observed] Selftest: `--selftest` reports 21 fixtures, 0 failing, at the
   reviewed commit. Rule-6 spot mutations of the recorder, each run against
   the unmodified selftest, all killed (selftest exit 1 with the named
   fixture failing): removing the verdict count; weakening the binding test
   to membership; disabling the argument/digest comparison; disabling the
   candidate predecessor-drift raise ("installed without an act" accepted);
   dropping the BEGIN/END marker counts ("aggregate marker duplicated"
   accepted); disabling the successor-row drift test; dropping the act body
   comparison; disabling the raw sha pin; disabling the stale-pin test;
   disabling the missing-dedicated-record raise (selftest crashes, nonzero).
7. [Observed] `check_governance.py`: mutating the packet's digest by one hex
   character yields CG-7d and CG-7e FAIL (2 FAIL, exit 1). Removing the
   packet registration, or the aggregate-record registration, from
   `_activate_poc_readability_copy_registry` fails the corresponding new
   selftest case (exit 1).
8. [Observed] Builder mutation: in the adopted clone, replacing the
   installed-state predecessor reconstruction in `current_bytes` with `{}`
   makes `--selftest` exit 1 ("GOVERNING-DEPENDENCIES.md.patch does not
   apply"), so the reverse-apply path is exercised post-adoption.
9. [Observed] Battery before adoption (fresh clone `pre` at e3878c5, every
   line of the §"How to verify this page" block, `CS=`/`DR=` treated as
   assignments): 51 commands, 51 exit 0. `check_governance.py`: 31 OK,
   21 WARN, 0 FAIL of 52 checks; `--selftest` 344 fixtures, 0 failing.
   CG-26 reports 50 published, 50 hosted, 50 shared; the workflow has 50
   `run:` steps; the sentence says "fifty". Criterion 4 holds.
10. [Observed] Simulated adoption (clone `adopt`): committed a synthetic raw
    `docs/reviews/R-POC-READABILITY-SUCCESSOR-PACKAGE-1-RAW.md` with the head
    contract, pinned FROZEN_MANIFEST_SHA / REVIEW / REVIEW_SHA, committed;
    `--check` reported candidate-unperformed; `--record --phrase` exited 0,
    wrote the dedicated record and one marked aggregate section and changed
    exactly the four restyled subjects; `--check` then reported
    performed-exact and the builder reported installed. After committing,
    the whole battery again gave 51 commands, 51 exit 0 (check_governance
    0 FAIL, CG-7e 48 files, CG-7h 0 findings, CG-26 50/50/50; recorder
    selftest 21/0 via its post-act unperform path; builder selftest passes;
    `build_three_surface_poc_spec_dependencies.py --check` matches with 24
    requirements; directive register matches). Criterion 3 holds.
11. [Observed] The generated act record states the verbatim phrase, the pinned
    raw by path and full sha, a predecessor/successor table for all six
    subjects, supersession with the earlier act preserved, and "widens no
    implementation direction and grants no source, provider, write,
    deployment or release permission".
12. [Observed] Spot-check of the installed spec against its predecessor:
    24 `### Requirement` headings, identical in order and text; scenario
    count equal. Word-diff of the first requirements (code-structure
    observation event-response, prohibition, Unknown, invariant; work-item
    Dolt read and prefix invariant) shows only the added
    "**Required behavior.**" lead and "Scope of quantification:" becoming a
    "**Scope.**" bullet; requirement words are unchanged.
13. [Observed] Packet (criterion 5): present tense, plain; one phrase; states
    it binds nothing until the act; states that silence keeps the current
    signed bytes; grants nothing beyond the restyle; does not claim adoption.
    Its claims check out: review rounds 1-3 carry `REVISE`, round 4
    `CONFIRM`; the relative link to review 4 resolves (five levels up);
    CONTRACT-COVERAGE.md and .openspec.yaml rows equal their predecessors.

## Findings

N1 (note). The recorder writes sequentially, not atomically, contrary to
the package's own stated expectation. `IMPACT-LEDGER.md` line 66-67: "a
later independently reviewed owner-act recorder must preflight and
implement the complete six-row transaction atomically"; `SEMANTIC-DELTA.md`
line 108: "a dedicated recorder atomically applies the four proposed
patches". `record()` writes the act (`open("x")`), appends the aggregate,
then writes subjects one by one. All preflights precede the first write, a
filesystem failure mid-sequence leaves a state `--check` rejects, and git
restores it; the performed sibling recorder uses the same pattern. Not
blocking; the two prose sentences overstate the mechanism.

N2 (note). The packet's evidence item reads "**Package review** ...:
pending." Once this review is retained that sentence is stale, and the
packet is a CG-7e-registered prose file whose repair would itself want a
review round (AGENTS.md: "Candidate-package prose files are not manifest
rows: a prose repair keeps the act digest unchanged but still needs a
review round"). Consider leaving it and recording the review outcome in the
recorder pin commit and the review README row instead, or scoping the
follow-up review to that one sentence.

N3 (note). `docs/evidence/three-surface-poc-readability-cli-mutation-2026-09-28.json`
was rebound by f4ff181 ("after main integration") to `testedCommit`
6bd15978409cb6515c3a40f762ebdb0196bd5c60, which is not an ancestor of the
reviewed commit (`git merge-base --is-ancestor` fails; it is reachable only
from `origin/agent/syzygy-73e.5.2*`). Its builder, fixture, package and
subject bytes equal a40bf82's (empty `git diff --stat` over those paths),
but e3878c5 then changed the builder's `prepare_cli_scratch` (subjects now
seeded from `current_bytes()`), so the retained CLI mutation evidence
predates the reviewed builder. The builder `--selftest` still passes before
and after adoption; the evidence is simply not for this commit (rule 7).

N4 (note). Pinning the recorder to its binding raw is a post-review edit of
the reviewed recorder bytes (three constants). This is the established
sibling pattern and the constants are fully constrained by the head
contract, but the pin commit should change only those three lines, and
`--check` plus `--selftest` should be re-run on it.

No material findings.

## Verdict rationale

Every acceptance criterion holds with a reproduction: the manifest digest
recomputes; manifest and patches are the bytes review 4 bound; the recorder
refuses each required precondition and its fixtures fail on ten real code
mutations; post-record state is performed-exact and partial states fail;
the full battery exits 0 on all 51 lines both at the reviewed commit and
after a simulated adoption; check_governance is 0 FAIL with a passing
selftest and CG-26 at fifty; the packet offers one correct phrase and
grants nothing beyond the restyle; no signed POC byte, performed act or
implementation file changes. The four notes concern prose accuracy,
evidence currency and the pin procedure, none of which blocks the act.
Verdict word, therefore: CONFIRM WITH EXCEPTIONS.
