# R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-3 — screening scope v2 review, round 3
Reviewed commit: ded37fcaf2f63e0ebc34b618a834d10475d24baf
Manifest SHA-256: aaeab36e7913ba77ff1f0478f9f470276a1d636f41ed6b17c66d91df78a7392e
Verdict: REVISE

Reviewer: fresh-context governance reviewer (Claude Opus 5.5). I worked in a detached worktree at the reviewed commit. I called no model provider and read no external repository body. Probe scripts ran in a scratch directory outside the worktree. Every mutant was restored with `git checkout -- .`, and `git status --porcelain` was empty afterwards.

## Checks run (this session, at the reviewed commit)

- [Observed] `gh pr view 326`: headRefOid = ded37fcaf2f63e0ebc34b618a834d10475d24baf, draft. The PR diff against main (`gh pr diff --name-only` and `git diff` from merge-base 328119ff) touches only the package directory and `scripts/build_public_source_screening_scope_v2.py`. No file under `apps/` or `packages/` is changed.
- [Observed] `--check`: "current", exit 0.
- [Observed] `--selftest`: "101 of 101 predicates held", exit 0, no FAIL line.
- [Observed] `--ready`: exit 1, with two FINDINGs: the class is not in the installed RFC-0005 text, and the v1 act is not recorded.
- [Observed] `--ready --pending-prerequisite`: exit 0, with the same two lines as NOTE.
- [Observed] Manifest file digest: `sha256sum` and `openssl dgst -sha256` both give aaeab36e…392e. `--manifest-digest --pending-prerequisite` prints the same value, which equals the expected one.
- [Observed] `python3 scripts/check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
- [Observed] `gh pr checks 326`: `checks` pass and `node` pass. Both runs have headSha ded37fca…, conclusion success.
- [Observed] Variants: each patch, applied to the derived v1 bytes (mode `prospective`), hashes to its manifest row. The `policyVersion` values are `1.3.0-public-source-candidate.1.none`, `.manifesto`, `.architecture` and `.both`, so they are distinct (round-2 N-3 repaired).

## Criterion 1 — round-2 findings

**B-1 (round 2).** I took each variant's rule from the patched policy JSON and ran 86 paths through two readers: the builder's reference reader, and an independent reader I wrote from the policy's own rule text. The independent reader asserts that at most one path rule matches. The two readers agree on all 86 paths in all 4 variants (0 mismatches).
- Every path listed in the round-2 raw is withheld in every variant, with two exceptions:
  - The opt-ins are sendable exactly in their own variant and in `both`: `docs/MANIFESTO.md`, `docs/ARCHITECTURE.md`, `docs/architecture/overview.md`, `MANIFESTO`, `00-ARCHITECTURE.md`.
  - `docs/ſpecs/x.md` (long s) is sendable in all variants. This follows the literal rule by design.
- The extra probes behave like this:
  - `docs/securityguide.md` is sendable in all variants (whole-word rule).
  - Withheld in all variants: `docs/Design Patterns/intro.md`, `docs/v1.0-spec.md`, `docs/my_ADR.md`, `doc/x/conduct.rst`, `DOCS/SECURITY.md`.
  - `docs/manifesto/README.md` is sendable only in manifesto and both. `docs/architecture.md` is sendable only in architecture and both.
- First directory versus deeper: the first segment must be `docs` or `doc` and is never tokenised. `security/docs/x.md`, `adr/x.md` and `design/docs/x.md` are withheld because they are outside every path rule. `docs/docs/security/x.md` and `docs/a.security/x.md` are withheld by token.
- The generated block equals the behaviour. Rule-6 results against `--check`, each restored afterwards, all STALE:
  - Removing `conduct` from `DOC_TOKEN_GROUPS` in the builder makes all four patches, the fixtures, the manifest, and both generated blocks (packet and delta) fail.
  - Dropping the space separator gives the same failures.
  - Hand edits inside the block (dropping `adrs` in the packet, dropping `adrs` in the delta, deleting "NOT") each fail "generated lists differ".
- `indeterminate` and `notMapped` (builder 252-270) agree with the block.

**N-2 (round 2) repaired:** delta:105 says "See packet Q3", the builder docstring at line 23 says "four-row manifest", and `--write` names the four patches.
**N-3 (round 2) repaired:** see above; the delta covers it at 143-149.
**N-4 (round 2) repaired:** delta 78-83.

## Criterion 2 — no new weakening

[Observed] I compared the round-2 builder (from a1564e1f) with this one over a generated population of 44,992 paths. Newly mapped by round 3: 0 in each of the four variants. Newly withheld: 9,330 (none), 9,006 (manifesto), 8,961 (architecture), 8,583 (both). `public-source-screening.ts:96` still runs `detectSecrets` and then `scanActiveContent` on every body, and the PR does not touch it. `semantic_findings` still fails on any change to the detectors, activeContent, accessBoundary or rawBodyHandling.

## Criterion 4 — rule 6, one rule literal per variant

In each of the four patches I changed the denylist literal `"security"` to `"securit"`, one variant at a time. Each run returns exactly "<variant>: patch differs from its regeneration", STALE.

## Findings

**Finding 1 — the packet's plain-words summary still says the rule maps no governance text** (blocking)
OWNER-DECISION-PACKET.md:12-13 says: "It maps no policy, governance or decision text." The rule maps such text whenever its path carries no denylisted whole word. Each of these is sendable in all four variants under both readers:
- `docs/doctrine/x.md`
- `docs/SecurityPolicy.md`
- `docs/CodeOfConduct.md`
- `docs/ADR0001.md`
- `docs/RFC0001.md`
- `docs/spec(v2).md`
- `docs/spec+v2.md`
- `docs/principles.md`
- `docs/standards/x.md`

The packet's own generated block at line 31 says the opposite ("a governance document whose path carries none of these words is NOT withheld"), and so does the delta at 99-104. The sentence is the first statement of scope the owner reads, and it sits outside the generated block. Changing it to "It maps no policy at all" leaves `--check` "current" (mutant run). This is the same overclaim as round-1 Finding 1 and round-2 Finding 1, surviving in hand prose.
Repair: restate the sentence to match line 31, for example "it withholds policy and governance text by name only".

**Finding 2 — `doctrine`, the first word in the RFC5-14 governance-text row, is not in the denylist** (note)
The installed RFC5-14 row reads "`governance-text` | Doctrine, spec, decision, policy text". The #257 bullet names "doctrine, spec, decision or policy text". Packet Q3 (lines 92-93) and the delta (line 100) both quote that list. Yet `DOC_TOKEN_GROUPS` (builder lines 104-108) has no `doctrine`, and `docs/doctrine/**` is sendable in every variant. The generated list is exact about this, so this is a decision rather than a misstatement. Either add the word, or have Q3 say plainly that doctrine is not denied by name.

**Finding 3 — the opt-in words have no plural forms** (note)
Every base group carries plurals ("adrs", "policies", "designs"). The opt-in words do not. `docs/manifestos/x.md` and `docs/architectures.md` are sendable in the none variant, while Q1 (line 64) says "neither word is mapped anywhere". That is literally true for whole words, but it is narrower than a reader will assume.

**Finding 4 — not every question has one decision with a stated default** (note)
- Q1 and Q3 carry "Default:".
- Q2 and Q4 carry only "Recommended:".
- Q5 (lines 103-105) is a statement, not a decision, and has no default.
- Q1:79 says "only one variant act may ever be recorded". The delta at 145-147 is more exact: nothing in the bytes enforces it, and the recorder must refuse unless the act is a declared superseding version.

**Finding 5 — the Q3 cost example understates the mapped side** (note)
Q3 (lines 90-92) illustrates the cost with "a protocol write-up called wire-format". Two kinds of name are mapped that the example does not show:
- CamelCase or concatenated governance names (`SecurityPolicy`, `ADR0001`).
- Names that use a separator outside `-_. `, such as `(`, `+`, `,`, `~`, tab or NBSP.

They are disclosed only implicitly, by "whole word" plus the separator list.

Criteria summary:
1. Round-2 findings: B-1 holds in the bytes, and its block is generated and checked. N-2, N-3 and N-4 hold.
2. No new weakening: holds (0 newly mapped over 44,992 paths).
3. Owner packet: costs are stated in both directions in Q1 and Q3. Finding 1 (blocking) and Finding 4 apply.
4. Mechanical checks: all green as listed. Manifest file digest aaeab36e…392e.
