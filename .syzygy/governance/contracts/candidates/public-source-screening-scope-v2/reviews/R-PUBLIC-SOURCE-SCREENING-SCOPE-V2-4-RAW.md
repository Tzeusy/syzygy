# R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-4 — screening scope v2 review, round 4 (narrow delta)
Reviewed commit: 72ddd76272f538801de8a100240f17ef202ff540
Manifest SHA-256: 770a020afd02ee33fefb29b4879aa81e604d8aac45576286f5dc64084a4f5570
Verdict: REVISE

Reviewer: fresh-context governance reviewer (Claude Opus 5.5). I worked in a detached worktree at the reviewed commit, with a second detached worktree at ded37fca for the comparison. I called no model provider and read no external repository body. Probe scripts ran in a scratch directory outside both worktrees. I restored every mutant with `git checkout -- .`, and `git status --porcelain` was empty afterwards.

## Scope note

[Observed] ded37fca is not an ancestor of 72ddd762 (`git merge-base --is-ancestor` exits 1), because the branch was rebased onto main. The literal `git diff ded37fca..72ddd762` therefore also carries 11 files from main: the workflow, PROJECT-STATUS.md, two PWB builders and two evidence records. `gh pr diff 326 --name-only` lists only the package directory and `scripts/build_public_source_screening_scope_v2.py`. I reviewed the diff of those paths between the two commits.

## Checks run (this session, at the reviewed commit)

- [Observed] `gh pr view 326`: headRefOid 72ddd76272f538801de8a100240f17ef202ff540, draft=true.
- [Observed] `--check`: "current", exit 0.
- [Observed] `--selftest`: "107 of 107 predicates held", exit 0.
- [Observed] `--ready --pending-prerequisite`: exit 0. It prints "current" and two NOTE lines: the class is not in the installed RFC-0005 text, and the v1 act is not recorded.
- [Observed] `sha256sum` of the manifest file: 770a020afd02ee33fefb29b4879aa81e604d8aac45576286f5dc64084a4f5570. I recomputed the four manifest rows from `propose()` over the v1 bytes, and they equal the file's rows: none c38275e0…, manifesto f48e0d9f…, architecture 442391a2…, both a12059f6….
- [Observed] `python3 scripts/check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
- [Observed] `gh pr checks 326`: checks pass, node pass.

## Round-3 findings against the bytes

- **B-1 (round 3), sentence replaced: holds mechanically.** OWNER-DECISION-PACKET.md:9-11 no longer makes the claim. The scope sentence now sits inside the generated block, at OWNER-DECISION-PACKET.md:21 and SEMANTIC-DELTA.md:60. Each line was mutated in turn ("ADR0001" changed to "ADR0002"), and `--check` gave "FINDING <file>'s generated lists differ from the rule's constants", STALE, exit 1, for both files. A mutation of the hand prose outside the block (packet:11) leaves `--check` current, as expected. The new sentence still overclaims; see B-1 below.
- **N-1 (round 3): holds.** `doctrine`, `doctrines`, `principle` and `principles` are in `docExcludedTokens` in all four patches. Mutants that drop `doctrine`, or drop `principle`, fail `--selftest` with "FAIL every path fixture holds".
- **N-2 (round 3): holds.** Probe results, as (manifestos/x, architectures/x): none (withheld, withheld), manifesto (mapped, withheld), architecture (withheld, mapped), both (mapped, mapped). Mutants that drop `manifestos` or `architectures` from OPT_IN_DOC_WORDS fail `--selftest`.
- **N-3 (round 3): holds in part.** Q2 (packet:85) and Q4 (packet:104) now carry defaults. The names paragraph is restated as a fact (packet:109). Q1 (packet:80-83) states the one-variant constraint as recorder intent and says the bytes do not enforce it, which is accurate. Q4's new default label is inaccurate; see N-2 below.
- **N-4 (round 3): holds.** docs/SecurityPolicy.md, docs/CodeOfConduct.md, docs/ADR0001.md and docs/spec(v2).md are mapped in all four variants, matching Q3 (packet:95-98) and the new fixtures.

## No new weakening

[Observed] I generated a population of 106,674 paths. It crosses every root stem and denylist word (both heads), plus probe words, with separators `- _ . space ( +`, upper/lower forms, a 00- prefix, seven top segments (docs, doc, Docs, licenses, src, governance, .github), three depth shapes, and six extensions. I classified each path with each head's own oracle, under that head's rule taken from its `propose()` bytes. The oracle function is byte-identical between the heads. Results:

| Variant | Newly mapped | Newly withheld | Newly withheld, by word |
|---|---|---|---|
| none | 0 | 2,160 | doctrine(s), principle(s), architectures, manifestos: 360 each |
| manifesto | 0 | 1,800 | the same, without manifestos |
| architecture | 0 | 1,800 | the same, without architectures |
| both | 0 | 1,440 | doctrine(s) and principle(s) only |

Nothing is newly mapped. The plural "lifts" did not newly map anything: at ded37fca the plurals were mapped in every variant, so the change only denies them where the opt-in is absent.

## Findings

**B-1 (blocking): hand-written Q1 says the opt-in words are mapped nowhere in variant none, and the bytes contradict it. The new generated sentence has the same gap.**
OWNER-DECISION-PACKET.md:62-64 says the two words "are mapped (or withheld) everywhere the rule looks: as a root file and inside the docs folder". Packet:66 says "none: neither word is mapped anywhere". The rule also looks in a third place: the licenses-tree, at generated packet:27 and SEMANTIC-DELTA.md:52-53. That path rule has no token denylist. [Observed] In all four variants, at both heads, these paths are mapped:
- licenses/MANIFESTO.md
- LICENSES/Architecture.txt
- licenses/SECURITY.md
- licenses/governance-policy.md
- licenses/CODE_OF_CONDUCT.md
- licenses/doctrine.txt

So in variant none, MANIFESTO is mapped. The new generated sentence (packet:21, SEMANTIC-DELTA.md:60) says "the rule withholds policy and governance text by name only, using the listed words". licenses/SECURITY.md carries a listed word and is mapped. This is the round-3 B-1 class: a withholding claim that is wider than the rule. It affects the Q1 variant decision. The fix is one of two:
- add the denylist (and the opt-in words) to the licenses-tree rule; or
- state in Q1 and in the sentence that the words withhold only under docs/doc and at the root, and that any .md/.txt directly under licenses/ is mapped whatever its name.

The defect predates this round, but this round's sweep is the first to test it.

**N-1: the scope sentence is generated, but nothing checks its content against the rule.**
The sentence is a string literal at build_public_source_screening_scope_v2.py:539-541. `--check` binds the packet and delta to the builder's text, but no predicate couples the sentence to the rule. A mutant of the literal leaves `--selftest` at 107 of 107, and only `--check` goes STALE. Its named examples do match fixtures (SecurityPolicy, ADR0001 and spec(v2) are mapped). "Generated" here means not drifting, not true.

**N-2: Q4's new default overstates.** Packet:104 says "Default: root README only. Only the root README is mapped". [Observed] docs/README.md, docs/vendor/lua/README.md and licenses/README.md are mapped in every variant; src/README.md is withheld. Generated packet:16 is accurate ("below the root outside docs or doc"). Q4 is not.

**N-3: Q3's word list understates what is withheld.** Packet:91-92 lists "decision, specification, design, governance, policy, security, conduct, adr or rfc" and omits doctrine and principle. The list errs toward withholding more, and it defers to "the lists above". The policy bytes' `indeterminate` example list in all four patches is likewise illustrative and omits them. Neither is an overclaim.

**N-4: the scope of the requested diff.** See the scope note: the literal commit range includes 11 main-side files that the PR does not change.
