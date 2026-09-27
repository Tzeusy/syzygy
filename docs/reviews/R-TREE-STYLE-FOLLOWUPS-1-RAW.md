Title: Review-note repairs (syzygy-73e.17/18) — review 1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed: origin/main..b590f52
Reviewer: independent fresh-context agent

## Material findings

None. The exceptions below are notes only.

## Notes

**N1. The docstring claim that a `diagram-clearer` relationship "keeps its `missing-diagram` finding" is only partly true.** The sentence is at `packages/polaris-generation-core/src/rendered-design.ts:20-22`. [Observed, code read at `relationshipRule`]
- For `diagram-clearer` with `supported` or `partly-supported` support, a dangling name does give `missing-diagram`.
- For `diagram-clearer` with `unsupported` support, the name resolves to no figure. `figure?.disposition.kind !== 'omitted'` is then true, so the finding is `undrawable-without-recorded-omission`, not `missing-diagram`.
- Either way the relationship blocks and does not throw, so behaviour is sound. Only the prose overstates.
- The other new doc statements match the code: `sourceIds` is `refs` (`provider-draft.ts:31`, min 1, unique, never resolved), `support` is not re-derived, and the partly-supported-nodes condition is not checked.

**N2. The ceremony-line heuristic can falsely fail a future recorder's section.** This answers question (b). [Observed by probe]
- `ACT_CEREMONY_LINE` treats any all-caps `LABEL: …<64 hex>` line as another act's phrase.
- I modelled a no-signal section on the restyle recorder's body, with the label swapped and markers added. It passes, both alone and followed by the restyle section. Each link returns its own instant with no problem.
- These three variants fail closed inside the link's own section:
  - a `SHA-256: <hex>` or `RFC-0008 SHA256: <hex>` line
  - a fenced verbatim quote of a predecessor phrase, such as `SIGN OFF GENERAL TRUSTED-BOOTSTRAP AUTHORIZATION TRANSACTION: <hex>`
  - one section carrying two acts, as the general-bootstrap section does with CC-SPEC at aggregate lines 88/95
- An unmarked no-signal section followed by a later unmarked act also fails. The forward scan stops only at a marker or an `Act instant:` line, never at a heading.
- A census of 1,010 tracked `.md`/`.txt` files found 21 distinct labels matching the heuristic. 19 are real act labels. The other two, `SHA256` and a truncated `MACHINE-VIEW AMENDMENT`, occur only in `docs/reviews/*-RAW.md`. So today's exposure is only in the future.
- `docs/POLARIS-NO-SIGNAL-AMENDMENT-TOOLING.md:25-29` still describes only the "nearest `Act instant:` above" rule. It does not tell a future recorder author about the new section constraints: markers or distinct sections, one act label per section, no upper-case digest headings.

**N3. The fix closes borrowing an existing instant; writing a new instant line is the residual the N-a raw already accepted.** [Observed]
- Splicing the phrase under the understanding act's instant plus a copied `Act instant: 2026-09-13T01:58:26Z` line straight after it passes `_contract_link_instant`. The forward scan breaks at that copied line.
- It edits the understanding block, so `record_polaris_understanding_adoption.py --check` fails with "aggregate act changed". That check is in both batteries (PROJECT-STATUS:314, workflow:180).
- A fresh mid-file section with its own backdated instant, placed between two marked sections, also passes CG-7h. This is the N-a raw's "earlier" variant, which it accepted as a residual. Only judging order from git history would close it.

**N4. Minor points in the evidence file.**
- `commits."N-e and R2-N2"` names 135bab4, but the N-e wiring landed in c3ce9da. 135bab4 contains it, so the runs are valid.
- Three `check` fields carry a host-specific interpreter path, `/home/tze/.pyenv/versions/3.10.12/bin/python3`.
- The equivalence argument for `M-own-label-counted-as-other` holds. `position` is the first line containing the label, and a second own-label line after it is caught by the exactly-one-record rule.

## Answers to (a)–(f)

**(a) The splice is closed on the real aggregate.** [Observed]
- I inserted a bare `SIGN OFF POLARIS NO-SIGNAL CONTRACT AMENDMENT: <hex>` line at every position in the real `ACCEPTANCE-ACT-RECORD.md` (521 positions). The dedicated record repeated the nearest instant above.
  - 335 positions have no instant above and already fail.
  - **0 of 186** instant-bearing positions were accepted.
- The same sweep over the real aggregate plus the real restyle recorder's `block(body(...))`: **0 of 234** accepted (569 positions in all).
- The real restyle section still resolves to its own instant, `('2026-09-28T00:00:00Z', None)`.
- Every `@<sha>`-form and comma-bearing label in the real record matches the heuristic, as the structure map of aggregate lines 17–498 showed.
- Prose lines with colons that are not all-caps, such as `Confirming review: … (sha256 …)`, `Predecessor: ADOPT …: <hex>` and `- CONFIRM …`, do not match.

**(b)** No false failure for a restyle-shaped recorder. There is a latent risk for other shapes and the tooling doc is out of date (N2).

**(c)** The CG-26 triple is exact.
- PROJECT-STATUS diff: 3 insertions, 1 deletion — two `--selftest` lines and the count sentence `forty` → `forty-two`. Nothing else changed.
- Workflow: 6 insertions, two steps.
- CG-26 reports 42 published, 42 hosted, 42 shared.
- My own count of the block: 42 commands and 42 `run:` steps. The only text differences are `$CS`/`$DR` variable expansions.
- The other "40 checks" strings are historical `check_governance` outputs in `round-2026-08c/d`.

**(d)** Correct. The guard applies only to `prose-sufficient` with a `named` diagram, it runs before findings are derived, and every draft diagram id counts regardless of disposition. The docs are accurate except for N1.

**(e)** Re-runnable. In a scratch clone at b590f52 I applied each `old`→`new` pair, asserting each `old` fragment occurs once. **14 of 14** mutants reproduce their recorded exit code and outcome: 13 killed, 1 equivalent survivor. The selftest mutants' failure counts match (4/1/1/2/1/4/0). Afterwards the tree was restored clean.

**(f) Runs in the worktree at b590f52.**

| Command | Result |
|---|---|
| `python3 scripts/check_governance.py` | 32 OK, 20 WARN, 0 FAIL (52 checks); CG-7h OK, 102 predicates, 0 findings |
| `python3 scripts/check_governance.py --selftest` | 327 fixtures, 0 failing, including the 3 splice fixtures, 2 real-recorder fixtures and the N-a probe |
| `build_contract_readability_restyle.py --check` | OK (29 modules) |
| `build_contract_readability_restyle.py --selftest` | 22 fixtures, 0 failing |
| `record_contract_readability_restyle.py --check` | "not performed" |
| `record_contract_readability_restyle.py --selftest` | 33 fixtures, 0 failing |
| `npx tsc -b packages/polaris-generation-core` | exit 0 |
| `npx vitest run packages/polaris-generation-core` | 8 files, 143 tests passed |

I did not run the full canonical battery in a fresh clone (rule 7). The worktree was not modified, and my scratch clone was removed.
