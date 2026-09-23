CONFIRM

Tested clean detached head `77b655df8ed229dae346048468d89a0b296a2349` against base `31b5e94cd8bd41236c62fbdc13708d4f7fb4bbbf`. That base is the local merge-base; PR #107’s live head matched the tested commit.

1. [Observed] Both proposed patches pass `git apply --check`. The spec patch adds one sentence to REQ-polaris-generation-006 and one scenario before `Form: lifecycle transition.` No other requirement marker is added or changed.

2. [Inferred] The new scenario is falsifiable: each omitted input-block ID requires a `removed` action and reason. Its unchanged, unrepairable repair arm remains distinguishable from a content-changing repair.

3. [Observed] The status patch changes only `177` to `178`. The current status file still says `177`; neither proposed patch was applied.

4. [Observed] The builder’s `--check` reported 6 behavior subjects, 2 patched, 0 manifest mismatches, a +1 scenario delta confirmed by two methods, and 0 sibling collisions. Its `--selftest` reported all 6 fixtures failing closed. I inspected the manifest-tamper fixture: it copies the real manifest into scratch, flips the first data-row digest character, and runs `check()` on that mutated fixture.

5. [Observed] Relative to the base, the adopted amendment spec, performed decisions, two earlier raw reviews, and both proposed patches are unchanged. The current status difference is the separate P-76 sentence. No owner act for this scenario exists.

6. [Observed] Criterion 8 is repaired for normal module initialization. A fresh module initialized with `ROOT` set to an absent scratch root produced 0 candidate subject entries and no packet-copy registry row. Initialization against the present worktree produced exactly 1 subject and the named packet-copy row. Both gates test this package’s own manifest. No `PWB_SUCCESSOR_CHAIN` link was added.

7. [Observed] The mutation record matches the tested source SHA-256 and retained registration-review raw SHA-256. I replayed both recorded false mutants in memory without editing files: disabling either gate changed the governance selftest from 265 fixtures, 0 failing to 265 fixtures, 1 failing at the absent-manifest case.

8. [Observed] The unmutated governance selftest reported 265 fixtures, 0 failing. The full governance check reported `32 OK, 20 WARN, 0 FAIL (52 checks)`. No hosted workflow or status-page verification-battery line changed.

9. [Observed] The semantic delta’s three owner questions remain questions. The packet’s act phrase matches the manifest digest, but it is marked not yet offered. No adoption, proposed-patch application, or implementation authorization occurred.

10. [Observed] A fresh `proposed/` directory sweep found this package and 6 siblings. A patch-target sweep found only this package targeting either affected file, consistent with the ledger and builder.

Limit: changing `ROOT` *after* importing the module leaves the already-initialized global packet-copy row in memory, although `_act_subjects()` then drops its entry. Production derives `ROOT` from the script path at startup; the fresh-initialization absence probe above tests that lifecycle. This confirmation does not establish PR merge readiness, adoption, or the full independently recomputed 178-scenario total.
