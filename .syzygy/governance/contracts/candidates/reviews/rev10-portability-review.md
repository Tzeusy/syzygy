# REV10 portability review (directive §13.6) — final report

**Reviewer charter:** can a fresh reviewer reproduce every mechanical claim from the delivered packet on a different machine — no absolute paths, no hidden local-only dependencies?

**Method executed:** the entire `final-prespec/` tree was copied to a scratch location outside the repository (`/tmp/claude-1000/.../scratchpad/portability/final-prespec`, no `.syzygy` ancestor anywhere up-tree — verified by ancestor scan), `scripts/__pycache__/` removed from the copy, and every quoted command run from that copy. Digest comparisons against the repo's canonical homes were run separately.

**Timing note.** [Observed] The live packet changed *during* this review: `topology/` (10 files) and `reviews/rev10-transaction-review.md` appeared at 01:27, after my 01:23 scratch copy. A full `diff -rq` between live packet and scratch copy shows those are the **only** differences, so every result below holds for the current packet except where noted; the topology additions were verified directly against the live tree.

## 1. Per-command outcomes (all from the scratch copy unless stated)

| Command | Outcome |
|---|---|
| `python3 scripts/verify_final_prespec.py` | [Observed] **PASS, exit 0** — "97861 words across 32 modules", "numbered clauses defined: 322", RFC-0001 oversize justification and corpus-band note printed as described |
| `python3 scripts/build_contract_index.py --check` | [Observed] **"index matches regeneration — no drift", exit 0** |
| `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` (from packet root — correct directory per the manifest's `rfcs/...` path format) | [Observed] **all 32 modules OK, exit 0** |
| Fixture 1 `context_load.py` command | [Observed] **13,806 w / 18,638 tok** — matches claim exactly |
| Fixture 2 command | [Observed] **18,175 w / 24,536 tok** — matches (the disclosed over-target exception) |
| Fixture 3 command | [Observed] **14,134 w / 19,080 tok** — matches |
| Fixture 4 command | [Observed] **10,728 w / 14,482 tok** — matches (includes `craft:security-and-secrets.md` = 820 w from the packet copy) |
| Fixture 5 command | [Observed] **11,684 w / 15,773 tok** — matches |
| Fixture packet digests (cat mandatory files in listed order \| sha256sum) | [Observed] all five match the quoted prefixes: `8e4d78a4c0804d01…`, `5117434a89aaba10…`, `2b61de863d391233…`, `2e1989733faefd3c…`, `1fb5a5eeb05306eb…` |
| F-EQ-1 | [Observed] **Substantive pass, annotation imprecise** — items 1–11 byte-identical, in order, unrenumbered in both captures; but the diff also shows 5-vs-2 trailing unrelated numbered lines (`grep -A40 'RFC2-1'` also matches RFC2-10/13/18/…), so the stated "differences only in stripped History parenthetical, item 11" does not describe the actual output (the item-11 History delta is not even visible, since the capture takes only each item's first line) |
| F-EQ-2 | [Observed] **Command output 14, stated pass value 9.** The sed range `/RFC3-16(b)/,/Bootstrap correlation/` starts at the *first* `RFC3-16(b)` occurrence (line 6, front-matter clause list) and restarts on later mentions, sweeping in `9.)*` and unrelated numbered lines (7., 9., 13., 14.). The nine binding items themselves are present, in order, and item 9 retains "always, under the A1 mechanism class" byte-identical to rev9 line 556 — verified with an anchored range (`/^\*\*RFC3-16(b)\. What an owner act binds/`, which yields exactly 9). Also: process substitution `<(…)` fails under POSIX `sh` (Syntax error observed); works under bash and zsh |
| F-EQ-3 | [Observed] **Pass** — "Same-class pairs only" row present in both files, byte-identical (programmatic diff empty) |
| F-EQ-4 | [Observed] **Pass** — no MISSING lines for any of the thirteen states |
| F-EQ-5 | [Observed] **Pass** — 11 table rows both sides, row text identical (programmatic diff empty) |
| F-EQ-6 | [Observed] **Pass** — constraint present in both homes (admission-and-boundary.md:303, governance-homes-and-owner-acts.md:227) |
| F-EQ-7 | [Observed] **Pass** — "operative limit" absent from the active module (grep exit 1), present in rev9 (line 626) and in `history/RFC-0008-history.md` with the B13-supersession reasoning (lines 248, 253) |
| F-EQ-8 | [Observed] **FAILS its stated pass condition for `D2`.** Verifier PASS; the ID grep over `rfcs/` returns A1 A5 A8 A9 B13 B19 B9 CC-TEST-2 D1 — **no D2**. `grep -rn 'D2' rfcs/` confirms zero occurrences anywhere in the active corpus. D2 appears only in `craft-and-care/` headers ("owner decision D2 (2026-08-01)"), which the command's `-r rfcs/` scope never touches. `matrix-rows/RFC-0003-rows.md:105` even states "(D1/D2 and CT-* never appear in RFC 0003.)" |
| Script from unrelated cwd (`cd /`) | [Observed] all three scripts (verify, index `--check`, context_load with `doctrine:`/`craft:` prefixes) produce correct output from `/` — root is derived from `__file__`, no cwd assumption |

## 2. Prefix fallback and copy fidelity

- [Observed] In the scratch location (no `.syzygy` ancestor), `doctrine:`/`craft:` specs resolved to the packet's own `doctrine/` and `craft-and-care/` copies; fixture word counts came out identical to the claims, so the fallback genuinely works off-repo.
- [Observed] `diff -r` of packet `doctrine/` vs `.syzygy/governance/doctrine/` and packet `craft-and-care/` vs `.syzygy/governance/policies/craft-and-care/`: **byte-identical, both trees.** No drift.
- [Inferred — design note, non-blocking] `context_load.py`'s resolution order *prefers* any `.syzygy` ancestor over the packet copy. On a machine where the packet sits inside a repo whose doctrine has drifted, fixture numbers would silently change with no indication of which source was used. A `--source`-printed resolution path or a packet-copy-first order would eliminate the ambiguity.

## 3. Absolute-path sweep

- [Observed] Exactly **one** hit for `/home/|/Users/|/tze/` across all .md/.py/.txt/.yaml: `01-REV9-ADVERSARIAL-FINDINGS.md:64` — a finding *about* the old rev9 scripts carrying `/home/tze/…`. **Documentary; no mechanical claim depends on running those scripts** (the packet ships portable replacements). Classified: documentary mention, acceptable.
- [Observed] `~/.claude/skills/…` appears once in `craft-and-care/README.md:18` inside an `[Observed]` provenance note — documentary.
- [Observed] `_bootstrap/…` references occur only in explicitly historical/provenance positions: matrix-rows `Source:` lines, `COMPACTION-CHARTER.md`, `craft-and-care/INSTALL-RECORD.md`, `history/README.md` (which explicitly labels the full rev9 review corpus "machine-local, git-excluded by owner design"), `00-README.md`, the acceptance record's supersession/mirror clauses. All `../../history/…` citations inside `rfcs/` resolve within the packet. No mechanical claim requires the `_bootstrap/` tree outside `final-prespec/`.

## 4. Mechanical claims in the three reports — recomputation

All recomputed from the scratch copy:

| Claim | Stated | Recomputed | Match |
|---|---|---|---|
| Total on disk, 32 modules (03 report, acceptance §3) | 97,861 w | 97,861 (verifier) | ✓ |
| Clause count (03, acceptance §3) | 322 | 322 (verifier) | ✓ |
| Component arithmetic 73,558+7,333+12,637+4,333 | 97,861 | 97,861 | ✓ |
| Tier 2 history extracted | 27,521 w | `wc -w history/RFC-000*-history.md` = 27,521 | ✓ |
| 7 package READMEs | 12,637 w | 12,637 | ✓ |
| RFC-0010+0011 | 4,333 w | 4,333 | ✓ |
| Fixture range / median (03, acceptance §3) | 10,728–18,175, median ≈13,800 | 10,728–18,175, median 13,806 | ✓ |
| RFC-0001 size | 8,352 w | 8,352 | ✓ |
| Manifest digest (acceptance §1 act 1 / §3) | `b77374b8080a7082f486248c05b54e38cdd460f30a6d7da627f026b57fb0d6fb` | identical | ✓ |
| rev9 corpus digests (fixture header, history/README) | nine 8-hex prefixes | all nine match in order (34f930c5…ceabc3e3) | ✓ |
| Act 2 digest (repo `testing-and-verification.md`) | `aa2d6353…b52821` | identical | ✓ |
| Act 3 digest (topology `BUNDLE-MANIFEST.md`) | `0d34d1b5…ad61560` | identical for both the `_bootstrap/rfc-phase/topology/` original and the packet's 01:27-added copy; all nine member digests inside the bundle manifest verify OK | ✓ |
| Act 4 digest (repo `.syzygy/intent/OVERVIEW.md`) | `42de2eb1…24f240` | identical | ✓ |
| **06-CONTEXT-LOAD-MAP module table** | RFC-0009 README **2,266**; parity/release **3,029** | actual **2,029** and **3,027** (verifier and `context_load.py` agree) | **✗ two stale cells** |

All other 30 cells of the 06 module table match the verifier exactly. The map's framing sentence — "all figures below are its output, re-runnable from this packet" — is false for those two cells.

## 5. Hidden dependencies

- [Observed] All three scripts import only the standard library (`argparse`, `re`, `sys`, `pathlib`). `build_contract_index.py` emits/checks the YAML with its own code — **no PyYAML**. No network, no subprocess, no env-var dependence found.
- [Observed] Acts 2–4 of the acceptance record bind digests of artifacts outside the packet (repo craft home, topology, committed overview). This is by design and stated in the record ("bind content already committed at canonical homes"); with the 01:27 addition of `topology/`, the topology bundle is now also reproducible from the packet. Craft policy bytes are in the packet (`craft-and-care/`, digest-identical to canonical); the overview is not in the packet — its digest claim is verifiable only against the repo/commit `fcb05c0`. Acceptable: gates 2–4 are explicitly repo-anchored acts, not packet-internal claims.
- [Observed — hygiene] The delivered packet contains `scripts/__pycache__/*.cpython-310.pyc` — machine-generated Python bytecode. Harmless, but it would travel in a zip and is not source; should be deleted before delivery.
- [Observed] Shell requirements: F-EQ-2 and F-EQ-8 as quoted require bash/zsh (process substitution; POSIX `sh` fails with a syntax error). [Inferred] F-EQ-8's `\b` in `grep -o` is GNU-grep behavior; on BSD/macOS grep the ID census may behave differently. Neither is stated in the fixture file.

## 6. Findings register

1. **F-EQ-8 D2 census fails as written** — `fixtures/semantic-equivalence-fixtures.md`, F-EQ-8 pass condition vs command scope. [Observed] `D2` appears nowhere under `rfcs/`; the stated pass condition "every listed decision ID appears somewhere in the active corpus" is not reproducible. Fix: drop D2 from the list (it is a craft-cluster decision, honored in `craft-and-care/` headers and the acceptance record) or widen the command's scope and say so. **Exception — does not block act 1** (fixtures are outside the act-1 manifest scope; no normative module is wrong), but the packet's own semantic-equivalence check must not fail its own pass condition.
2. **Two stale figures in `06-CONTEXT-LOAD-MAP.md`** (RFC-0009 README 2,266→2,029; parity/release 3,029→3,027) under a sentence claiming all figures are script output. [Observed] Likely a pre-final-edit snapshot of RFC-0009. **Exception — does not block act 1** (Tier 3 projection, outside the manifest), but it is exactly the drift class the packet's own Risk 1 (03 report) warns about; correct the two cells.
3. **F-EQ-2 command yields 14, stated 9** — sed range restarts on later `RFC3-16(b)` mentions. [Observed] Underlying claim true (nine items, byte-preserved, item 9 wording intact). **Non-blocking**; anchor the range (e.g. start at `^\*\*RFC3-16(b)\.`) so the printed number equals the stated number.
4. **F-EQ-1 expected-output annotation imprecise** — actual diff contains trailing slop beyond the described delta, and the described History-parenthetical delta is not visible in the capture. [Observed] Items 1–11 verified identical. **Non-blocking**; reword the expectation or tighten the grep.
5. **Prefix resolution order prefers ancestor `.syzygy` over packet copies** — silent-source ambiguity on drifted hosts. [Inferred risk] **Non-blocking** (copies currently byte-identical; scratch run provably used packet copies).
6. **`scripts/__pycache__/` shipped** — [Observed], hygiene, **non-blocking**.
7. **bash/zsh + GNU-grep assumptions in two fixture commands, unstated** — [Observed]/[Inferred], **non-blocking**; one line in the fixture header ("run under bash or zsh with GNU grep") closes it.
8. **Packet mutated mid-review** (`topology/`, one review file, 01:27) — [Observed]. Not a portability defect; the additions verify clean. Noted so the confirming review knows the tree it binds includes them.

## 7. Verdict

**EXCEPTIONS** — findings 1 and 2 are reproduction failures of the packet's own stated mechanical claims and must be fixed (or the claims corrected); findings 3–8 are non-blocking. **None of the exceptions touches any of the 32 active modules, the manifest, or its digest** — `b77374b8…fb0d6fb` remains valid and act 1 is not invalidated by fixing them, since `fixtures/` and `06-CONTEXT-LOAD-MAP.md` are explicitly outside act 1's scope. The core portability question is answered **yes**: from a copy outside the repository, on stdlib Python alone, from any cwd, every verifier, index check, manifest check, all five context-selection fixtures (totals and digests exact), and seven of eight semantic-equivalence fixtures reproduce precisely; the doctrine/craft fallback resolves to packet copies that are byte-identical to the canonical homes; the single absolute-path occurrence is documentary.
