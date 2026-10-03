# R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-5 — screening scope v2 review, round 5 (narrow delta)
Reviewed commit: fd4e2509dacaa4e0839ab50be9273244a9d7ce93
Manifest SHA-256: 26690d2bfc7eee2f9ee3ae1615824b46a562c33bb0335569936cff1ea451816e
Verdict: REVISE

Reviewer: fresh-context governance reviewer (Claude Opus 5.5). After `git fetch origin`, I worked in a detached worktree at the reviewed commit. I reviewed `git diff 72ddd762 fd4e2509`, which covers 10 files: the round-4 repair 33b15a65 and the commit that retains the raw. I re-derived each round-4 finding from the bytes. I extracted the `project-documentation` rule from each variant's `propose()` output and ran adversarial licenses-tree paths through the builder's reference reader (`classify_documentation`) under that rule. I applied three source mutants to the builder and restored each with `git checkout -- .`; `git status --porcelain` was empty afterwards. I called no model provider, read no external repository body, and sent nothing to any network service other than the git fetch. The probe script ran from the scratch directory, outside the worktree.

## Checks run (this session, at the reviewed commit)

- [Observed] `--check`: "public-source screening scope v2: current", exit 0.
- [Observed] `--selftest`: "selftest: 112 of 112 predicates held", exit 0.
- [Observed] `--ready --pending-prerequisite`: "current" plus two NOTE lines: the class is not in the installed RFC-0005 text, and the version-1 act is not recorded. Exit 0.
- [Observed] `--manifest-digest --pending-prerequisite`: 26690d2bfc7eee2f9ee3ae1615824b46a562c33bb0335569936cff1ea451816e. `sha256sum` of the manifest file gives the same digest.
- [Observed] For every variant, the rule object inside `propose(v1_bytes, variant)` equals `documentation_rule(variant)` (4 of 4 True). The SHA-256 of each variant's proposed bytes begins with the prefix of its manifest row: none e6a2ef4f…, manifesto 16a1b3f1…, architecture 84505c0a…, both a39823ed….
- [Observed] `python3 scripts/check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
- [Observed] Criterion 8: a 64-hex sweep over the 8 package Markdown files outside `reviews/` found 0 digests.
- [Observed] `git diff --shortstat 72ddd762 33b15a65`: "8 files changed, 70 insertions(+), 28 deletions(-)". This matches the unreviewed-repair statement at OWNER-DECISION-PACKET.md:7-12 and ROUND-4-DISPOSITIONS.md.

## Round-4 findings against the bytes

**B-1 (licenses-tree denylist): holds.** [Observed] The repair adds one branch to `classify_documentation` (builder:184-187), and that branch only returns False. Across the four patches, the only change is the `licenses-tree` rule text, so `docExcludedTokens` and every other constant are byte-unchanged. No path can become newly mapped. Results from the reference reader, using each variant's rule taken from its proposed bytes:

| Path | none | manifesto | architecture | both |
|---|---|---|---|---|
| licenses/SECURITY.md, licenses/Security.MD, licenses/sEcUrItY.txt, LICENSES/GOVERNANCE.TXT, Licenses/Policy.md | withheld | withheld | withheld | withheld |
| licenses/security.md.txt, licenses/security.MD.txt, licenses/x.security.md, licenses/x security.md, licenses/security_x.txt, licenses/-security-.md, licenses/spec.v2.md, licenses/Code of Conduct.md | withheld | withheld | withheld | withheld |
| licenses/design-doc.md, licenses/ADR-0001.md, licenses/rfc.txt, licenses/doctrine.txt, licenses/principles.md, licenses/conduct.md, licenses/specs.md, licenses/policies.txt | withheld | withheld | withheld | withheld |
| licenses/MANIFESTO.md, licenses/manifesto.MD, licenses/manifestos.txt | withheld | mapped | withheld | mapped |
| LICENSES/Architecture.txt, licenses/architectures-x.md | withheld | withheld | mapped | mapped |
| licenses/sub/security.md, licenses/governance/x.md, license/security.md, licenses/security.rst, licenses/security, licenses/security.md.bak, "licenses/security.md " | withheld (no rule) | withheld | withheld | withheld |
| licenses/ѕecurity.md (Cyrillic s), licenses/SECURİTY.md, licenses/ſecurity.md, licenses/ｓecurity.md (fullwidth), licenses/security​.md, licenses/security+policy.md, licenses/security(policy).md, licenses/security–policy.md (en dash), licenses/securitypolicy.md | mapped | mapped | mapped | mapped |

The last row is the documented by-name limit, and the docs tree behaves the same way: [Observed] docs/ѕecurity.md, docs/ſecurity.md and docs/security+policy.md are mapped. The scope sentence discloses it ("written without a separator … or split by a character outside the separator list"). It is not new and it is not a regression. Mutant M2 (the `license_denylist` default set to False) fails `--selftest` on "every path fixture holds" and the opt-in fixtures of all four variants. Q1 (packet:68-71) now names the licenses folder.

**N-1 (scope sentence from constants): holds, with one weak predicate.** [Observed] `scope_sentence()` (builder:537-546) is built from DOC_TREE_ROOTS, LICENSE_TREE_ROOTS, DOC_EXCLUDED_TOKENS, OPT_IN_DOC_WORDS and WITHHELD_ROOT_NAMES. Mutant M1 replaces the opt-in words with "xyz". It is caught: "FAIL the scope sentence names every denylist word, opt-in word and withheld root name", 111 of 112. That predicate covers the opt-in words only through the default variant's `docExcludedTokens`, which is enough. The example predicate is weaker; see R5-3.

**N-2 (Q4 default): the Q4 text holds. The repair leaves the generated list contradicting it.** [Observed] Q4 (packet:113-117) now says the root README, a README under docs or doc, and a README directly under licenses are mapped, and src/README.md is withheld. The reader agrees: docs/README.md True, licenses/README.md True, src/README.md False. See R5-1.

**N-3 (Q3 words): holds.** [Observed] Packet:97-102 lists doctrine and principle, and says the same words withhold a file name directly under licenses. The reader agrees (rows above).

**N-4 (diff range): no repair needed.** The repair diff is stated by commit range, and the shortstat matches.

## Findings

**Finding R5-1 — the generated "Stays withheld" list, and the policy's `notMapped` text, say READMEs and the other root names below the root outside docs or doc are withheld. The licenses-tree rule maps them, and the repaired Q4 now says so.** (revise)

Evidence:
- [Observed] OWNER-DECISION-PACKET.md:42 and SEMANTIC-DELTA.md:75, both generated by builder:585, say: "READMEs and the other root names when they sit below the root outside docs or doc (vendored libraries carry their own)" are withheld.
- [Observed] The reference reader maps licenses/README.md, licenses/LICENSE.txt, licenses/CHANGELOG.md and licenses/NEWS.md, in all four variants. licenses/README.md is a selftest fixture with expected value True (builder:205).
- [Observed] The packet now contradicts itself on the question N-2 raised. Q4 (packet:113-114) says "a README … directly under the licenses folder" is mapped, while the generated list at packet:42 says it is withheld.
- [Observed] SEMANTIC-DELTA.md:56-57 says these lists "are the only statement of what is sendable and what is withheld".
- [Observed] The policy bytes repeat the claim in all four patches. `notMapped` (none.patch:113) begins "nested and vendored documentation (a README below the root outside docs-tree)". `indeterminate` (none.patch:120) gives "(for example a README below the root)" as documentation outside the rule's paths.
- [Observed] The line is not new. Builder:565 at 72ddd762 carries the same text, and round 4 called it accurate.
- [Inferred] The claim errs toward withholding more than the rule does. This is the same class as round-3 and round-4 B-1: a withholding claim wider than the rule, in the list the owner signs against. Under this review's bar ("makes a packet claim false"), that makes it revise-severity. No governance-shaped text becomes sendable through it.

Proposed repair:
- Change builder:585 to "… below the root outside docs, doc and licenses (vendored libraries carry their own); a file directly under licenses is mapped whatever its stem unless a denylist word withholds it".
- In `notMapped`, write "a README below the root outside docs-tree and licenses-tree". In `indeterminate`, write "(for example src/README.md)".
- Add a selftest predicate tying each generated withheld line to at least one fixture. Regenerate the patches and the manifest. This changes all four manifest rows, so it needs a further narrow review.

**Finding R5-2 — the variant line, and `notMapped`, describe the denylist and the opt-in lift as docs-only.** (note)

Evidence:
- [Observed] Packet:35 and SEMANTIC-DELTA.md:68 say each variant "lifts the same word from the docs withholding". Since 33b15a65 the variant also lifts it from the licenses-tree withholding: licenses/MANIFESTO.md is mapped only under manifesto and both.
- [Observed] `notMapped` (none.patch:113) lists the denylist withholding only as "docs-tree paths whose directory or file name has a word in docExcludedTokens". The licenses-tree rule text (none.patch:27) does state the denylist, and `notMapped` ends "and any other prose", so neither sentence is false.

Proposed repair: in the same regeneration as R5-1, write "from the docs and licenses withholding" and "docs-tree and licenses-tree paths".

**Finding R5-3 — the "every example the sentence gives is mapped" predicate tests hard-coded literals, not the sentence's examples. The sentence also says such text "under any other name is sendable".** (note)

Evidence:
- [Observed] Builder:785-786 checks `docs/SecurityPolicy.md` and `docs/ADR0001.md` as literals.
- [Observed] Mutant M3 rewrites the sentence's example to "(Security, ADR0001)". docs/Security.md is withheld, so the example becomes false, yet `--selftest` holds 112 of 112. Only `--check` would see the file drift.
- [Inferred] "such text under any other name is sendable" overstates sendability. For example, src/policy-notes.md and a root notes.md are indeterminate and withheld. This errs toward safety.

Proposed repair:
- Make the example list a constant used by both the sentence and the predicate.
- Write "such text under any other name inside the mapped paths is sendable".

**Finding R5-4 — REVIEW-BRIEF.md is still the round-4 brief.** (note)

Evidence:
- [Observed] REVIEW-BRIEF.md:1 says "(round 4, narrow delta)". It has no criterion for the round-4 repairs. Its recording section names `R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-4-RAW.md`.
- [Observed] ROUND-4-DISPOSITIONS.md says "there is no round 5". The packet itself (packet:11-12) offers "ask for one more review", so this round is lawful. The record will still read inconsistently once this raw lands.
- [Observed] Criterion 1 says the variants "differ only in `rootStems`". By design they also differ in `docExcludedTokens` and the `policyVersion` suffix.

Proposed repair: when this raw is retained, add a round-5 criterion and recording name to the brief, correct criterion 1, and note in the round-5 dispositions that the owner or lead asked for this round.

## No new weakening

[Observed] The repair's effect on the rule is monotone toward withholding: one added `return False` branch in the reader, plus rule text. The `docExcludedTokens`, `docTokenSeparators`, `licenseTreeRoots` and `licenseTreeSuffixes` bytes are unchanged in all four patches. [Inferred] No path is newly mapped by 33b15a65. The tightening is consistent with the RFC5-14 class text (`rfc5-project-documentation-class/SEMANTIC-DELTA.md`:47: prose that "does not govern its development").
