Title: Contract successor chain tooling — review 1
Verdict: REVISE
Reviewed: 26719cc
Reviewer: independent fresh-context agent

**Commands run at 26719cc (worktree clean before and after)**

| Command | Result |
|---|---|
| `python3 scripts/check_governance.py` | exit 0: "32 OK, 20 WARN, 0 FAIL (52 checks)". The CG-7h line is "102 predicates examined, 0 findings". The parent bb9ecea gives the same CG-7h line. I ran the parent from a `git archive` with no `.git`, so its overall total (31 OK / 21 WARN) cannot be compared. |
| `python3 scripts/check_governance.py --selftest` | exit 0: "295 fixtures, 0 failing". 0 lines start with FAIL. All 13 new restyle fixtures pass. |
| `build_contract_readability_restyle.py --selftest` | exit 0: "20 fixtures, 0 failing". |
| `build_contract_readability_restyle.py --check` | exit 0: "package absent … nothing to verify". |
| `record_contract_readability_restyle.py --selftest` | exit 0: "17 fixtures, 0 failing". |
| `record_contract_readability_restyle.py --check` | exit 0: "not performed: no dedicated or aggregate record". |

What I confirmed `[Observed]`:
- **An unrecorded package stays inert.** `restyle-candidate-no-records` fails and `restyle-candidate-inert` passes at 76.
- **Record validation is kept.** An aggregate-only or dedicated-only record fails (probe: 31 findings). So do a mismatched digest, malformed or duplicated label lines, an unsorted link, an empty link, a path outside the bootstrap, and mirror drift.
- **The fold enforces the latest link on both mirrors.** It is checked on the installed tree, and the installed/candidate equality loop covers the mirror.

I tested the attack paths below with a scratch copy of `check_governance.py`. Its only change was extra `probe-*` kinds in `_selftest_cg7h`, using the commit's own `link()` helper.

**Material findings**

M1. `scripts/check_governance.py:3325-3339` (link population), `:2552` (chain tuple). CG-7h no longer limits which modules a link may bind, and it never excludes RFC-0007/rendering-and-surface.md.
- The old no-signal branch called `manifest_rows(..., 2)` and `require_exact_paths(..., POLARIS_NO_SIGNAL_PATHS)`. Both were removed. Each link may now bind any non-empty, sorted subset of the 30 bootstrap paths, and the chain tuple has no per-link population.
- Probe results with valid records, all OK and 0 findings:
  - `probe-ns-rfc7`: a no-signal manifest with 3 rows, adding RFC-0007/rendering-and-surface.md. OK at 81.
  - `probe-restyle-30`: a restyle manifest with all 30 rows. OK at 108.
  - `probe-restyle-rfc7-only`: a restyle manifest binding only RFC-0007/rendering-and-surface.md. OK at 79.
- Failure scenario: an agent writes a restyle manifest that includes rendering-and-surface.md, plus two records in the recorder's format. CG-7h passes, and the battery accepts changed bytes for the module that must stay excluded.
- The exclusion is enforced only by the builder's `population()`, at record time. The recorder's `--check` calls `validate(..., verify_package=False)` (`record_contract_readability_restyle.py:164`, `:283`). The builder's `--check` is in no battery or CI (a sweep found no citers outside the two new scripts). Nothing standing re-checks the exclusion after recording.
- The selftest was loosened to fit. `contract-extra` used to expect "expected 2". Now it passes only because `zz-extra.md` is not a bootstrap path (`:6832`), so an extra bootstrap path is accepted.
- Required fix: give each chain entry its own closed, exact path tuple. No-signal is `POLARIS_NO_SIGNAL_PATHS`; restyle is the bootstrap paths minus rendering-and-surface.md. Add fixtures for both extra-bootstrap-path cases.

M2. `scripts/record_contract_readability_restyle.py:83-91`, `:68-80`, `:179-191`. This recorder's phrase and subject validation is weaker than its siblings'.
- `validate_instruction` accepts any non-empty, single-line text.
- The recorder does not bind:
  - an owner-supplied digest argument, as `record_pwb_state1_amendment.py` requires with `argument != manifest_sha`;
  - a frozen subject commit or packet head (compare `FROZEN_SUBJECT`/`PACKET_HEAD`);
  - a CONFIRM review raw by digest (compare `REVIEW_SHA` in `record_polaris_understanding_adoption.py`);
  - an exact instruction. The polaris sibling refuses anything but "Adopt it", and its selftest refuses "continue".
- Probe: on a builder fixture with a verifying package, `record(root, "continue", …, verify_package=True)` succeeded, and `check(..., verify_package=True)` then returned True.
- Failure scenario: any agent turn whose words are passed to `--record` adopts whatever verifying package is on disk at that moment. That package may be unreviewed or regenerated after review, because nothing ties the recorded digest to the bytes the owner was shown. AGENTS.md says recorders "hard-code the frozen subject and packet head" and "validate the owner's phrase against current bytes". This recorder does neither.
- Required fix: take the owner's digest argument and compare it with the manifest. Pin the reviewed raw by path and sha plus a frozen commit, or refuse `--record` until those constants exist.

M3. `scripts/check_governance.py:3282-3352` (fold). The fold follows chain order, not the order the acts were performed, so a later owner act can be silently cancelled.
- Probe `probe-shadow`: the restyle is performed, then no-signal is performed with valid records, and the no-signal bytes are never installed. Result: OK at 111, 0 findings.
- The details say the no-signal rows were "superseded by" the restyle manifest, even though the restyle act came first.
- If the no-signal bytes are installed (`probe-shadow-nsbytes`), CG-7h fails with 2 findings. So once the restyle is performed, no-signal can never take effect, and its recorded act reports as valid history.
- This is fail-closed for bytes. It is not honest about acts, and it is a fold/ordering bug of the kind the brief asked about.
- Required fix: either reject a recorded link whose successor in the chain was performed earlier, or order the fold by aggregate record position.

**Notes**

N1. `record_contract_readability_restyle.py:227-228` passes vacuously. The fixture "unverified package refused by the builder" runs against a temp root with no bootstrap manifest. `population()` raises FileNotFoundError, which becomes "package inputs unreadable". The builder's verification findings are never reached, and the recorder is never exercised against a real verifying package with `verify_package=True`.

N2. `build_contract_readability_restyle.py:514-517` checks the wrong branch. The "empty (no-op) patch" fixture is rejected with "No valid patches in input" (does not apply). The "changes nothing" branch at `:218` is never exercised, and the expected substring (the module path in backticks) would match almost any finding.

N3. `build_contract_readability_restyle.py:393-409`. `--apply --at-adoption` does not check that the act record exists. CG-7h then fails closed, but an apply-first change carries no evidence that the owner performed anything. The recorder explicitly allows the "applied first" path (`:75`).

N4. `scripts/check_governance.py:3301-3304`. The chain-predecessor finding looks only at the immediately previous attempted link. That is harmless at two links, because the invalid link fails CG-7h by itself, but it does not match the docstring's "blocks every later link".

N5. The commit message says "13 rule-6 mutations each fail a selftest". No evidence record with old/new fragments and the commit is included, as AGENTS.md requires for rule-6 claims.

N6. Neither new script is wired into the PROJECT-STATUS battery or CI. That is consistent with the CG-26 "register at merge" note, but combined with M1 it means no standing check enforces the 29-module scope.
