Title: Contract chain tooling follow-ups (syzygy-73e.12/13, CG-26) — review 1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed: origin/main..bd5e4b0
Reviewer: independent fresh-context agent

## Material findings

None. I found no defect that would justify REVISE.

## Answers to (a)–(f)

**(a) N2 is closed for accidental and out-of-order insertion, and fails closed as claimed. [Observed]**

Method: in scratch clone `rv2`, I ran the real recorder with the owner phrase `ADOPT CONTRACT READABILITY RESTYLE: 6e83675f…`. Then I ran `build_contract_readability_restyle.py --apply --at-adoption`. The recorder wrote `Act instant: 2026-09-27T22:20:22Z` (aggregate line 527).

- **No false failure on real output:** CG-7h **OK**, 133 predicates, 0 findings. The only FAILs were CG-7a (29) and CG-18 (20), which are the known N3 regenerations from review 2.
- **Probes:** 11 variants. Each one spliced a synthetic no-signal record, with its manifest and dedicated record, into the performed tree.

| Variant | CG-7h result |
|---|---|
| Inserted above the restyle, instant later | FAIL: "is after later chain link(s)" |
| Instant equal to the restyle's | FAIL: "adoption order is ambiguous" |
| No instant | FAIL: "0 `Act instant:` lines" |
| Two instants | FAIL: "2 … lines" |
| Impossible date (`2026-02-30`) | FAIL: "not a real UTC second" |
| Trailing space on the line | FAIL: "malformed" |
| Dedicated and aggregate instants disagree | FAIL: "differs" |
| Phrase spliced between the restyle's own instant and its phrase | FAIL: equal instant |
| Appended below the restyle, with an earlier instant | FAIL: the positional check still fires |
| Inserted above, with a genuinely earlier instant | OK: superseded history, the intended shape |
| `between-early` (see N-a) | OK |

**(b) Nothing breaks for earlier acts. [Observed]**
- Neither chain label appears in the real aggregate (grep). No chain act was performed before this change.
- The recorder is untouched by this diff and already writes the required form.
- The no-signal link has no recorder, so the only exposure is documentation (N-c).

**(c) The N5 fixtures are real. [Observed]** I ran my own five mutants against `--selftest`, and each was killed:
- the import call replaced with `pass`;
- `root` ignored;
- `registry` ignored;
- the early return removed;
- the label emptied.

**(d) The CG-26 triple is exact. [Observed]**
- The PROJECT-STATUS diff is two hunks and nothing else: two battery lines added at 346–347, and the count word "thirty-eight" changed to "forty" at 357.
- The workflow adds exactly the two matching steps.
- The live CG-26 row reads: `40 published, 40 hosted, 40 shared`, 0 findings.
- No other "thirty-eight" survives outside historical round files.

**(e) The evidence is re-runnable. [Observed]**
- All 15 mutants carry `old`/`new`/`commit`.
- At `53375ef`, each `old` fragment occurs exactly once. All 15 reproduce the recorded exit code and failing rows.
- The tree was clean after restore.

**(f) Battery results at bd5e4b0, clean clone. [Observed]**

| Command | Result |
|---|---|
| `check_governance.py` | 32 OK, 20 WARN, 0 FAIL (52 checks). CG-7h OK, 102 predicates. CG-7e OK, 42 files |
| `check_governance.py --selftest` | 321 fixtures, 0 failing |
| `build_contract_readability_restyle.py --check` | OK |
| `build_contract_readability_restyle.py --selftest` | 22 fixtures, 0 failing |
| `record_contract_readability_restyle.py --check` | "not performed", exit 0 |
| `record_contract_readability_restyle.py --selftest` | 33 fixtures, 0 failing |

## Notes

**N-a. An instant is self-declared, and the aggregate lookup is not scoped to the link's own section.**
- The recorder accepts any `--instant` (`record_contract_readability_restyle.py:470`).
- Probe `between-early`: I inserted a no-signal phrase only, with no instant line of its own, directly under an unrelated act's `Act instant: 2026-09-13T01:58:26Z` (aggregate line 479). The dedicated record carried the same instant. CG-7h returned **OK**, 137 predicates, 0 findings, and read the no-signal act as superseded history.
- `_contract_link_instant` (`check_governance.py:3120-3124`) takes the nearest instant line above the phrase, even when an END marker or another act's phrase lies between them.
- The same OK comes from backdating a whole inserted section ("earlier" variant).
- This requires writing a false instant, which is the residual the N2 raw itself accepted by proposing instants. A structural fix would require no intervening `<!-- …:END -->` or phrase line between the instant and the phrase, or would judge append-only order from git history. [Inferred]

**N-b. One surviving mutant is equivalent.** Changing `if t < instant` to `if t <= instant` survives, but it only double-reports a case the equality check already fails. The docstring says the aggregate instant sits "above its phrase". The code measures from the first line naming the label; the two differ only when prose names the label, which the mention check already fails.

**N-c. The no-signal tooling doc is now incomplete.** `docs/POLARIS-NO-SIGNAL-AMENDMENT-TOOLING.md:19-23` still lists the record requirements as the bare ceremony line only. A future no-signal recorder built from that doc would fail CG-7h on its first recording. I did not check whether the doc is digest-bound.

**N-d. The evidence commit will become unreachable.** The evidence names `53375ef`. A rebase-merge will leave that commit reachable from no ref (the AGENTS.md rule-6 note). Consider citing a stable anchor as well, or merging so that it survives.

**N-e. The battery wires in `--check` only.** Neither restyle script's `--selftest` joins the battery. Sibling amendment builders, such as `build_pwb_registry_currency_briefing_amendment`, carry both. This is within the stated scope; it is only an asymmetry.

## Checks and denominators

- Instant-logic probes over the real recorder's output: 11. Of these, 9 FAIL as intended; 2 OK (one intended, one is N-a).
- Evidence mutants re-run at `53375ef`: 15 of 15 reproduce.
- My own mutants: 8. Of these, 7 were killed and 1 survived (the equivalent one in N-b).
- CG-26 lines: 40 published, 40 hosted, 40 shared.
- PROJECT-STATUS diff hunks: 2 (3 insertions, 1 deletion).
- Branch currency: `HEAD..origin/main` is empty after fetch.

Scratch clones only: `/tmp/claude-1000/-home-tze-GitHub-syzygy/42f1d844-9fb6-4091-8261-544ed369daaf/scratchpad/rv{1..4}`. The worktree was not modified.
