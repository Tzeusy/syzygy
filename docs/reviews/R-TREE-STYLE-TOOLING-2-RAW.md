Title: Contract successor chain tooling — review 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed: 69a9e74
Reviewer: independent fresh-context agent

**Where I ran things.** I ran every command and probe in a fresh `git clone` of the worktree, pinned at 69a9e74. `git status --porcelain` was empty before and after every run. I edited nothing in the worktree.

While I was reviewing, the shared worktree changed under me. `scripts/record_contract_readability_restyle.py` became modified, and two untracked files appeared: `candidates/contract-readability-restyle/REVIEW-NOTES.md` and `docs/reviews/R-TREE-STYLE-CONTRACT-PACKAGE-1-RAW.md`. That was another session, not me. None of it is reviewed here, and I re-ran the battery in the clean clone.

## Task 4: battery at 69a9e74 [Observed]

| Command | Output |
|---|---|
| `python3 scripts/check_governance.py` | exit 0. "32 OK, 20 WARN, 0 FAIL (52 checks)". CG-7h: "102 predicates examined, 0 findings". CG-7e: "40 files examined, 0 findings". CG-7d: WARN, "62 quotations examined, 0 findings". |
| `check_governance.py --selftest` | exit 0. "305 fixtures, 0 failing". |
| `build_contract_readability_restyle.py --selftest` | exit 0. "22 fixtures, 0 failing". |
| `build_contract_readability_restyle.py --check` | exit 0. "manifest matches 29 patched modules on both identical mirrors; clause leads, front matter and headings unchanged; verify_final_prespec, CG-13 and CG-17 pass". |
| `record_contract_readability_restyle.py --selftest` | exit 0. "33 fixtures, 0 failing". |
| `record_contract_readability_restyle.py --check` | exit 0. "not performed: no dedicated or aggregate record". |
| `check_docs_review_campaign_partition.py` (extra) | exit 0. "total=261 assigned=261 raw=236 … unmatched=0 overlaps=0". |

## Task 1: review-1 findings

**M1: RESOLVED.**
- Each chain entry now carries a closed tuple. The tuple is at `scripts/check_governance.py:2616`, the bootstrap literal at `:2010`, and the restyle population (the 30 bootstrap paths minus RFC-0007/rendering-and-surface.md) at `:2047`.
- The count and exact-population checks are at `:3413-3414`. Fixtures are at `:6919-6920` and `:6976-6978`, and the static tuple check against the manifest on disk is at `:6942`.
- The builder also compares its population with `CONTRACT_RESTYLE_PATHS`, at `build_contract_readability_restyle.py:372`.
- Live-tree probes: I built each manifest, wrote both records by hand with the manifest's real digest, and installed the bytes.
  - 30 rows including the rendering module: CG-7h **FAIL**, "parsed 30 digest row(s), expected 29" plus "population/order differs from the closed 29-path contract".
  - 28 rows (RFC-0006 dropped): **FAIL**, "parsed 28 … expected 29".
  - Rendering-only manifest with new rendering bytes installed: **FAIL**, "parsed 1 … expected 29", and the rendering module is still held to its bootstrap digest.

**M2: RESOLVED in the recorder.** Standing enforcement is still missing; see N1 below.
- The exact phrase is enforced by `PHRASE.fullmatch` at `record_contract_readability_restyle.py:136-142`.
- The owner's argument must equal the manifest digest (`:253-254`).
- All three pins are `None` (`:75-77`), and `validate_pins` refuses while any is unset (`:113-116`). It also checks the manifest sha against its pin, the raw's sha, the verdict in the raw's four-line head, and the manifest digest in that head (`:117-133`).
- The selftest refuses "continue", trailing words, a wrong digest, and unpinned or partly pinned recorders, in both the synthetic group and the real-package group (`:324-356`, `:420-427`).
- The mutants M2-phrase-search, M2-argument-unchecked and M2-unpinned-allowed are each killed on re-run (task 3).

**M3: RESOLVED for append-order.** It can be bypassed by inserting a record mid-file; see N2.
- `position` is set at `check_governance.py:3363` and the out-of-order finding at `:3387`.
- Live probe: restyle performed and applied, then no-signal appended. CG-7h **FAIL** with "`SIGN OFF POLARIS NO-SIGNAL CONTRACT AMENDMENT` is recorded after later chain link(s) `ADOPT CONTRACT READABILITY RESTYLE`", and the restyle link is then named against the broken predecessor.

**N1–N6.**
- **N1: RESOLVED.** A real verifying package is recorded with `verify=True`, and a tampered patch is refused with the builder's own finding (`recorder:408-448`).
- **N2: RESOLVED.** The fixture is now an identity hunk that applies and hits "changes nothing". Mutant N2-changes-nothing-off is killed.
- **N3: RESOLVED.** `apply` refuses unless the recorder's `check` passes (`builder:405-423`). Live probe: installing the bytes with no records gives CG-7h FAIL with 29 findings.
- **N4: RESOLVED.** `broken` accumulates every invalid link (`:3381`), with a three-link cascade fixture.
- **N5: RESOLVED, with an exception.** An evidence record now exists, but the commit it names is dangling; see N4 below.
- **N6: NOT RESOLVED, and deferred on purpose.** Neither script is in the battery or CI, which the commit message says is left for the CG-26 merge-time commit.

## Task 2: new holes

**The package is inert. [Observed]**
- CG-7h stays at 102 predicates, the bootstrap-only count review 1 recorded.
- Records without installed bytes fail CG-7h with 29 findings.
- Installed bytes without records also fail CG-7h with 29 findings.

**The packet registration works live.**
- Flipping one hex digit of the packet's digest: CG-7d and CG-7e both FAIL.
- Changing the manifest while the packet keeps the old digest: CG-7d and CG-7e both FAIL.
- Appending a bare `Manifest SHA-256: <stale>` heading to the packet: CG-7e FAIL.
- A stale digest cited inline mid-sentence passes. This is the known unlabeled-copy limit (`syzygy-wh1`).

## Task 3: rule-6 evidence

`docs/evidence/contract-successor-chain-mutations-2026-09-28.json` stores `file`, `old`, `new`, `selftest`, `exit`, a summary, the failing fixtures and `commit` for each of its 26 mutants.

I re-ran **all 26** at 69a9e74. Each `old` fragment occurs exactly once, and every mutant was killed with the same fixture count as recorded, for example M1-exact-count "305 fixtures, 8 failing", N3-unrecorded-apply "22 fixtures, 3 failing" and M2-unpinned-allowed "33 fixtures, 4 failing". The tree was clean afterwards.

## Findings

No material findings.

**N1. No standing check enforces the recorder's review pin.**
- Where: `record_contract_readability_restyle.py:111-133` versus `check_governance.py:3348-3420`.
- Failure scenario: an agent writes both records by hand with the manifest's real digest and installs the bytes. CG-7h then passes (OK, 133 predicates in my probe), while `record_… --check` fails with "recorder unpinned".
- No `record_*` script is in PROJECT-STATUS or CI, so the M2 pins bind only when someone uses the recorder.
- This matches the sibling recorders and is not a regression, but it means review 1's M2 remedy has no standing enforcement. Consider wiring the recorder's `--check` in the CG-26 integration commit.

**N2. The out-of-order check can be bypassed by inserting a record above the aggregate's end.**
- Where: `check_governance.py:3363`. `position` is the first aggregate line naming the label, and nothing verifies that the aggregate is append-only.
- Probe: restyle performed and applied. Then a no-signal record binding bytes that are never installed is inserted at aggregate line 11, with its dedicated record and manifest.
- Result: CG-7h **OK**, 137 predicates, 0 findings. CG-7c, CG-7d and CG-7e also pass.
- The details report the no-signal rows as "superseded by" the restyle. That is review 1's M3 shadow again: a recorded act that never takes effect reads as valid history.
- Bytes still fail closed: installing the no-signal bytes fails CG-7h. The dedicated record's `Act instant`, or an aggregate prefix digest, could order acts instead.

**N3. The adoption flow the packet describes ends with a red battery, and nothing documents the regeneration.**
- Where: `OWNER-DECISION-PACKET.md:25-35` and `build_contract_readability_restyle.py:405`.
- After a valid record and apply, CG-7a fails with 29 findings (ACTIVE-CONTRACT-MANIFEST rows) and CG-18 fails with 20 findings (all 10 context-selection fixtures' digest and word counts).
- I checked the 10 context-selection fixtures: none is digest-cited or named in a manifest, so they can be regenerated. The generated-index CI steps are likely to go stale as well [Inferred].
- The builder's `--check` claims CG-13 and CG-17 pass, but not CG-7a or CG-18.

**N4. The evidence record and a commit message cite a commit no ref reaches.**
- The evidence's `commit` is `2fd8082…`, and 69a9e74's message says "repaired in 2fd8082". `git for-each-ref --contains 2fd8082` returns nothing: it is the pre-rebase twin of 80ec3c0.
- The three scripts are byte-identical between 2fd8082 and 80ec3c0 (empty `git diff --stat`), so the record can still be re-run, but it should name 80ec3c0 or the script blob shas before 2fd8082 is garbage-collected.

**N5. The packet registration has no selftest.**
- Where: `check_governance.py:2587-2600`.
- Mutant: I replaced the `_activate_contract_restyle_packet_copy_registry()` call with `pass`. The selftest still reports "305 fixtures, 0 failing", so the mutant **survives**.
- Live, the same mutant drops CG-7e to 39 files and misses a flipped packet digest. CG-7d still catches it.
- The function's `registry`/`root` parameters are never exercised.

**N6. The packet overstates the binding review and does not quote the recorder's head predicate.**
- Where: `OWNER-DECISION-PACKET.md:67-69`.
- It says in the present tense that the binding review "carries this manifest digest in its head; the recorder is pinned to it". No such review exists at 69a9e74, and every pin is `None`.
- The recorder requires `Manifest SHA-256: <digest>` within the first four non-blank lines (`recorder:107-108`, `:131`). A reviewer who uses the standard Title/Verdict/Reviewed/Reviewer head, like this one, pushes that line to line 5, and the recorder refuses the raw.
- Per AGENTS.md, the brief must quote this predicate.

**N7. The packet does not say that adopting the restyle forecloses the no-signal link as the chain now stands.**
- Where: `check_governance.py:2616` and `:3387`.
- Chain order is adoption order, so once the restyle is performed, any no-signal act recorded afterwards fails CG-7h permanently until the chain tuple is reordered. My probe confirmed this.
- The two no-signal modules are among the 29 restyled ones. The packet (`:22-24`) names the scoped-attributes conflict but not this one.
- No no-signal package exists in any ref today, so the effect is prospective.
