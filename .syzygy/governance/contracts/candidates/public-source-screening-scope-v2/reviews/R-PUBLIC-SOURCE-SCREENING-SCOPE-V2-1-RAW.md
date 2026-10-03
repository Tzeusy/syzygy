# R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-1 — screening scope v2 review
Reviewed commit: 85d7509eaee419a1296ec6820b39be77955f8f1f
Manifest SHA-256: 44f3f5b4b3364654adf4b3355c2a60a3bd17c3ac943eed75e73547e4e08d3edc
Verdict: REVISE

Reviewer: fresh-context governance reviewer (Claude Opus 5.5), detached worktree at the reviewed commit. No model provider called; no external repository body read.

## Checks run (this session, at the reviewed commit)

- [Observed] `build_public_source_screening_scope_v2.py --check`: "current", exit 0.
- [Observed] `--selftest`: "38 of 38 predicates held", exit 0.
- [Observed] `--ready`: exit 1, two FINDINGs (class not in installed RFC-0005 text; version-1 act not recorded).
- [Observed] `--ready --pending-prerequisite`: exit 0, the same two as NOTE.
- [Observed] `--manifest-digest --pending-prerequisite` and `sha256sum` of the manifest file agree: the digest in the head above, equal to the expected value.
- [Observed] Rule 6: changing the patch literal `"licenses"` to `"licences"` makes `--check` report "patch differs from its regeneration", exit 1. Adding `"design"` to `DOC_TREE_ROOTS` in the builder makes `--check` report the patch, the manifest and fixture `design/overview.md`, exit 1. Both restored, and the worktree is clean.
- [Observed] `python3 scripts/check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
- [Observed] `gh pr checks 326`: `checks` pass, `node` pass.
- [Observed] Consumer `apps/three-surface-poc/src/polaris-generation/public-source-screening.ts:95`: `screenBody` runs `detectSecrets` and then `scanActiveContent` on every body and does not read the classification rules. Mapping a document cannot skip either screen. `semantic_findings` (builder lines 284-325) fails any change to the base keys or to the scope keys `detectors`, `activeContent`, `accessBoundary`, `rawBodyHandling`, `inheritedRules` or `selfReferenceRule`, and its selftest mutants fire. Criterion 3 holds.
- [Observed] Symlinks: version-1 `sourceAdmission.notAdmitted` lists "symbolic links (mode 120000)" and submodules, so a symlink under `docs/` is never admitted. The rule is unaffected.
- [Observed] VIS-4: no package file labels anything accepted or approved. The one hit, "approved requirement" in `inheritedRules`, is unchanged version-1 text.

Edge-case probes through the builder's reference reader `classify_documentation`:
`README` T, `readme.MD` T, `00-RELEASENOTES` T, `docs/../src/x.c` F, `docs.md` F, `Docs/x.md` T, `doc/x.markdown` F, `.github/README.md` F, `vendor/x/README.md` F, `LICENSE.txt.exe` F, `docs/a/../b.md` F, `README\n` F, `licenses/.md` F. Also `docs/adr/0001-decision.md` T, `docs/specs/protocol.md` T, `docs/governance/policy.md` T, `docs/security/policy.md` T, `doc/rfc/rfc-1.txt` T, `docs/CMakeLists.txt` T, `docs/requirements.txt` T, `SECURITY` T, `GOVERNANCE.txt` T, `DESIGN` T, `CODE_OF_CONDUCT` T, `MANIFESTO.rst` T, `٠١-README.md` T, `١٢-LICENSE` T, `LICENſE` F.

## Findings

**Finding 1 — the proposed policy bytes contradict themselves, and the packet's withheld list is false** (blocking)
Patch line 79 (`notMapped`) says that "specification, design, decision and policy documents, committed reports, code of conduct and security policies" stay indeterminate. Patch lines 46, 50, 52 and 53-54 map the root stems `security`, `design`, `governance` and `code_of_conduct`/`code-of-conduct`. Patch lines 22-23 (`docs-tree`, any depth) map `docs/adr/…`, `docs/specs/…` and `docs/governance/…` (probes above). The builder's own fixture `("docs/design/decision.md", True)` (builder line 136) asserts that a decision document is mapped. The indeterminate text (patch line 86) also says "specification and design documents" stay indeterminate. OWNER-DECISION-PACKET.md lines 197-201 tell the owner that "specification, design and decision documents" are excluded from reading and from egress. That is false for any such file under `docs/` or `doc/`, and for a root DESIGN/GOVERNANCE/SECURITY file. SEMANTIC-DELTA.md lines 133-137 qualify the conduct and security exclusion with "below the root", but the policy bytes do not. The policy text and the rule must agree, and every packet example must hold under the reference reader (REVIEW-BRIEF criterion 7).

**Finding 2 — class fidelity: governance-text is mapped by name and directory, and Q3 does not surface all of it** (blocking)
The RFC5-14 amendment row reads "does not govern its development". Its bullet (rfc5-project-documentation-class/SEMANTIC-DELTA.md lines 53-56) says "A document the project's declared classification policy places as doctrine, spec, decision or policy text is `governance-text`", and lines 69-72 add that "a document that sets binding rules for the project's own governance (a decision record, a policy, a specification) is `governance-text`". Measured against that text:
- GOVERNANCE (project governance rules) and SECURITY (a disclosure policy) are policy or governance text by their ordinary content. CODE_OF_CONDUCT is a conduct policy. It is mapped, and Q3 omits it.
- DESIGN is withheld as a directory but mapped as a root file. That is inconsistent, and the policy's own `notMapped` excludes design documents.
- ARCHITECTURE: the amendment says that for "an architecture overview … the policy decides" (lines 79-80). Mapping it is defensible, but the default should be off and the owner can opt in.
- MANIFESTO is plausibly doctrine (`governance-text` row: "Doctrine, spec, decision, policy text"). It is mapped and not surfaced. [Inferred]
- `docs-tree` maps every `.md/.rst/.txt` at any depth. That places decision records, RFCs, specs and governance documents by directory name alone. It also maps non-prose `.txt` files such as `docs/CMakeLists.txt` (CMake build code) and `docs/requirements.txt`. Neither the packet nor Q3 says so.
- Q3 (OWNER-DECISION-PACKET.md lines 229-237) bundles two decisions, the directory and the names. For the names it gives no default ("confirm or strike").
Recommended revision: make DESIGN, GOVERNANCE, SECURITY and CODE_OF_CONDUCT/code-of-conduct off by default, and offer ARCHITECTURE and MANIFESTO as separate opt-ins with a default of off. Either exclude governance-shaped subtrees of `docs/` (adr, rfc(s), spec(s), decisions, governance, policy, security) or surface that the docs tree maps them. Make Q3 one decision with a default.

**Finding 3 — `rootStemPrefix` admits non-ASCII digits; the rule is not literal or closed** (blocking)
Patch line 30 carries `"(?:\\d\\d-)?"`, a regex in a dialect the policy does not name. In the builder's oracle (Python `re`, str pattern) `\d` matches every Unicode decimal digit. The probe gives `classify_documentation("٠١-README.md") == True` and `("١٢-LICENSE") == True`. The policy's own rule text (patch line 15) says that nothing beyond ASCII A-Z is "folded, normalized or decoded", and the delta calls the rule literal. A JavaScript consumer's `\d` is ASCII-only, so the oracle and a TS implementation would disagree on these paths. Replace the prefix with a literal description: two ASCII digits 0-9 and a hyphen, optional. Add a non-ASCII-digit fixture that must be False.

**Finding 4 — `--ready` checks a path that does not exist, so the RFC5-14 prerequisite can never be met** (blocking)
Builder line 66: `RFC5_INSTALLED = pathlib.Path("rfcs/RFC-0005/consent-egress-secrets.md")`, which is resolved against the repository root (line 361). The installed module is `.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md`, and `rfcs/` at the root does not exist (probe: "builder-path-ABSENT"). In a scratch root I put the real module plus a `| \`project-documentation\` |` row at its real home, together with a version-1 act file. `readiness()` still returned "the class project-documentation is not defined in the installed RFC-0005 text". It returned `[]` only when I placed the file at the nonexistent builder path. The check fails closed, but it is not the prerequisite the delta claims (SEMANTIC-DELTA.md lines 156-159; REVIEW-BRIEF criterion 5), and no selftest predicate exercises `readiness()` (rule 6). Fix the path, consider checking the candidates mirror as well, and add install/uninstall mutants.

**Finding 5 — the Unicode fixtures are inert, and the brief misdescribes them** (note)
`RKADME.md` (builder line 139) is all ASCII and contains no Kelvin sign. `READMEİ.md` fails because it has an extra character, whatever the folding. With `ascii_fold` replaced by `str.lower` or `str.casefold`, no fixture changes, so the mutants survive. Under `casefold`, `LICENſE` (long s) becomes True. No stem contains `k`, so a Kelvin fixture cannot bite. Use `ſ` (casefold to `s`) and the Finding 3 digits instead. REVIEW-BRIEF.md lines 36-37 claim "dotted-capital-I and Kelvin-sign names".

**Finding 6 — the "design" attribution is not anchored to the clause** (note, rule 8)
SEMANTIC-DELTA.md line 150 ("RFC5-14 puts specification, design, decision and policy text in `governance-text`") and the packet's Q3 make this attribution. The amended text says "doctrine, spec, decision or policy text" and does not name design. Withholding `design/` is this policy's choice, which is lawful, and should be stated as one.

**Finding 7 — supersession and the post-act state are unspecified** (note)
The packet says only "It supersedes the version-1 bytes" (OWNER-DECISION-PACKET.md line 44). Once the v2 act is performed, the policy on disk carries the scope and does not hash to the v1 row. `v1_bytes` (builder lines 222-225) then raises, so this package's own `--check` turns STALE after its own act, and no selftest covers a performed-v2 base. The phrase, the record name and the v1 recorder's `--check` behaviour are deferred to a recorder "written after the review". State them in the packet or ledger before the offering.

**Finding 8 — Q2 is not a decision; a selftest label mismatches its mutant** (note)
Q2 (packet lines 221-227) offers an alternative it calls impossible, so it is an ordering statement, not a decision. Selftest label "a licences tree allowed at any depth" (builder line 492) actually adds `license` to `licenseTreeRoots`.

Criteria summary: 1 fails (Findings 1 and 2); 2 fails (Finding 3; extension, prefix-form and depth probes otherwise as described); 3 holds; 4 partly holds (data `prerequisite` present and VIS-4 holds; `--ready` path wrong per Finding 4; supersession thin per Finding 7); 5 fails (withheld list false; Q3 not one decision with a default); 6 checks run as listed.
