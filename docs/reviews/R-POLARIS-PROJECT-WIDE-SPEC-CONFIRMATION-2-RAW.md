# Independent confirmation report

## Exact subject and checks

[Observed] Subject: exact commit `b4470708b7752b48acb5df81fe9a707b296fead6` (`spec: close Polaris confirmation findings [syzygy-1z3]`).

[Observed] The reviewed files have no worktree differences from that commit. The sole pre-existing modification is unrelated `.gitignore`.

[Observed] Review-record integrity matches the disposition register:

- Original raw review: `b47fbb0eb73507d0f6a4d4cc50f72908c6330c8a82be689477ce1f59209587dc`
- Confirmation pass 1: `b58286e3328028d64c273cae0450c5be397e0d1160537333d44eb727b59d1d29`

[Observed] Requested checks passed:

- dependency generator `--selftest` and `--check`;
- contract-coverage generator `--selftest` and `--check`;
- `openspec validate polaris-project-wide-butlers-model --strict`;
- tracked-scope governance: 758 files, 32 OK, 19 WARN, 0 FAIL;
- governance selftest: 155 fixtures, 0 failing.

[Observed] Independent counts:

- Accepted index: 324 rows / 324 unique clause IDs.
- Accepted contract bodies: 327 heading occurrences / 324 unique IDs; the three duplicate occurrences are cross-contract quotations, and the unique body set equals the index set exactly.
- Matrix parts: 210 + 220 + 183 = 613 base consequences.
- Repair overlay: 67 rows superseding 62 base rows.
- Effective total: `613 - 62 + 67 = 618`.
- Effective dispositions: 142 covered, 230 Unknown uncovered, 246 believed not applicable.
- Capability table: 27 rows = 21 covered + 6 lawfully out of scope.
- Repair rows: 62 covered + 4 Unknown uncovered + 1 believed not applicable.

[Observed] The RFC 0001–0003 matrix’s embedded count table is stale despite the correct generated manifest. Its real counts are:

- RFC1: 100 = 7 covered + 55 Unknown + 38 believed not applicable.
- RFC2: 51 = 10 + 24 + 17.
- RFC3: 59 = 11 + 25 + 23.
- Total: 210 = 28 + 104 + 78.

[Observed] All six signed parent artifacts match the act exactly:

- `proposal.md`: `6459f56c…72eddb`
- `design.md`: `0847bf5f…8695c`
- parent `spec.md`: `f0eda5b9…d960e`
- `CONTRACT-COVERAGE.md`: `0c8472a9…d9ce`
- `GOVERNING-DEPENDENCIES.md`: `4bdcf6c6…c1da4`
- `.openspec.yaml`: `9187547d…6976`

[Observed] No signed-parent artifact differs from `db5eaee`; only the deliberately unsigned parent `tasks.md` changed later.

## Per-finding verdicts

### 1. Consequence-granular contract review — NOT CONFIRMED

[Observed] RFC3-7.c2 is now correctly split into observation and egress rows, and the current arithmetic is 618 effective consequences.

[Observed] The malformed-row guard is not generally fail-closed. It rejects the selftest’s `yes/no` mutation, but independent in-memory mutations showed:

- malformed base consequence ID: accepted, regenerated 617 rows;
- broken base column structure: accepted, regenerated 617 rows;
- malformed repair ID, disposition, or columns: accepted, silently restored the superseded base row and retained 618 rows with changed dispositions.

[Observed] Several repair rows also narrow or change accepted consequences rather than exhaust them, including RFC1-18.r2, RFC6-14.r1, RFC7-2.r1, RFC7-26.r1, RFC7-30.r1, and RFC7-32.r3.

[Inferred] The matrix is not yet a fail-closed exhaustive consequence review.

### 2. Warrant overclaims — NOT CONFIRMED

[Observed] All 62 repair-overlay `covered:` rows were checked against exact accepted text and the named requirement’s case, observable, oracle, independence statement, and falsifier.

[Observed] Thirty-nine rows have an oracle that decides the stated consequence:

`RFC4-3.r3`, `RFC4-7.r2`, `RFC4-7.r3`, `RFC1-19.r1`, `RFC1-19.r2`, `RFC1-24.r1`, `RFC1-24.r2`, `RFC2-9.r1`, `RFC2-24.r1`, `RFC6-14.r2`, `RFC6-14.r3`, `RFC6-17.r1`, `RFC6-17.r3`, `RFC7-16.r1`, `RFC7-16.r2`, `RFC7-16.r4`, `RFC7-33.r1`, `RFC7-1.r1`, `RFC7-2.r2`, `RFC7-2.r3`, `RFC7-3.r1`, `RFC7-9.r1`, `RFC7-9.r2`, `RFC7-9.r3`, `RFC7-10.r2`, `RFC7-12.r1`, `RFC7-12.r2`, `RFC7-13.r1`, `RFC7-14.r2`, `RFC7-15.r1`, `RFC7-17.r2`, `RFC7-26.r2`, `RFC7-27.r1`, `RFC7-33.r2`, `RFC7-33.r3`, `RFC7-31.r1`, `RFC7-32.r1`, `RFC7-34.r1`, `RFC7-34.r2`.

[Observed] Twenty-three remain partial or semantically inaccurate:

- `RFC4-3.r1`: no oracle compares capture time with source-claimed time.
- `RFC4-3.r2`: no oracle exhausts identity/version on every emission.
- `RFC4-7.r1`: no per-project registry-location/scoping oracle.
- `RFC1-18.r1`: no exact durable derivation or cross-evaluation case.
- `RFC1-18.r2`: repair consequence drops binding challenge state; the case does not enumerate it.
- `RFC2-10.r1`: no repeated-run determinism case.
- `RFC2-25.r1`: no tier-meaning or sibling-state distinction oracle.
- `RFC6-14.r1`: accepted text covers every entity and claim; repair covers claims only.
- `RFC7-2.r1`: accepted text permits anchored, non-normative, or epistemically labeled claims; the row incorrectly says every claim is anchored.
- `RFC7-2.r4`: runtime output enumeration does not exhaust narrative-producing authoring acts.
- `RFC7-3.r2`: no deletion-invariance mutation.
- `RFC7-5.r1`: presentation attributes do not decide entity class and ownership.
- `RFC7-10.r1`: no closed target-class/durable-ID/no-label-path-coordinate oracle.
- `RFC7-14.r1`: byte comparison does not test absence of a stored normative copy.
- `RFC7-17.r1`: no exactly-one-authority-class check per block.
- `RFC7-26.r1`: omits the named default `Base` mode and observed-reality limb.
- `RFC7-29.r1`: no exhaustive typed-authority-table oracle.
- `RFC7-29.r2`: personal-state separation has no counterexample or oracle.
- `RFC7-33.r4`: distinct narrative/kernel Claim machine types appear only in the SHALL text.
- `RFC7-30.r1`: a current non-release material-change run does not decide the accepted release-milestone consequence.
- `RFC7-31.r2`: oracle does not inspect all verdict/rationale/judging-party fields.
- `RFC7-31.r3`: Unknown-never-met is checked, but exact `verdict-unlawful` recording is not.
- `RFC7-32.r3`: “one applicable walkthrough” weakens the accepted release-run condition.

[Inferred] Identifier agreement is complete, but semantic warrant agreement is not.

### 3. Capability denominator includes refusals — CONFIRMED

[Observed] Independent counting confirms 27 rows partitioned into 21 covered and 6 lawfully out of scope. The explicit refusal population from proposal/design is represented.

### 4. Observation consent and concrete secret policy — CONFIRMED

[Observed] PWB-REQ-005 consistently requires the consent/policy/registry triple in its case, observable, oracle, and falsifier.

[Observed] It uses RFC3-7’s exact consent subject pair: `(observing Syzygy Project, configured Butlers repository)`. Another project or repository cannot match.

[Observed] Invalid authority yields zero body reads and project-model Unknown. Separate owner gates remain prerequisites; sign-off mints none.

### 5. Closed item identity and discovery — PARTIAL

[Observed] The source population, nine item classes, path-independent identity, duplicate handling, non-recursion, and Unknown denominator behavior are substantially clearer.

[Observed] The extraction procedure is still not syntactically closed. Terms such as “numbered non-negotiable,” “the two success sections,” “top-level named entry,” “RFC index-table identity,” and “component tables” do not bind exact source files, heading levels/text, list grammar, key normalization, or malformed-input behavior.

[Inferred] Two independent parsers can still derive different item populations.

### 6. Path, active-content, and resource controls — CONFIRMED

[Observed] PWB-REQ-006 retains exact-object containment, traversal/NUL/symlink/submodule rejection, no execution, inert output, unsafe-URL blocking, declared budgets, sink scans, and visible Unknown on limit breach.

### 7. Plain-copy oracle — CONFIRMED

[Observed] The closed roles, word bounds, prohibited terms, cardinalities, exhaustive string population, and independent DOM/text oracle remain effective.

### 8. Complete RFC7-30 prompt — CONFIRMED

[Observed] PWB-REQ-021 retains the complete prompt set, including claim strength and strengthening route. PWB-REQ-016 separately requires nonvisual/keyboard traversal.

### 9. Proposal authority language — CONFIRMED

[Observed] Sign-off is explicitly necessary but insufficient; finding-derived improvement-cycle authority and security prerequisites remain separate.

### Pass-1 N1 — NOT CONFIRMED

[Observed] The original `yes/no` malformed row is fixed, but malformed IDs, column shapes, repair dispositions, and repair rows can still be silently dropped.

### Pass-1 N2 — CONFIRMED

[Observed] PWB-REQ-005 consistently uses triples, three owner-act provenances, and all-three-valid terminology.

### Pass-1 N3 — CONFIRMED

[Observed] PWB-REQ-021 now keeps answers/paths/identities/mode in the execution record and places verdict/rationale/judging party in a separate owner decision. PWB-REQ-022 preserves the two homes and fail-closed pairing.

## New findings

### N4. BLOCKER — Malformed-row detection recognizes only already-valid-looking IDs

[Observed] `CONSEQUENCE_LIKE_RE` uses nearly the same ID grammar as the parser, so a malformed ID or broken first columns cease to look like a consequence row. Repair rows have no independent table-row denominator check.

Minimum fix: validate every data row inside both matrix tables independently of ID validity, reject wrong column counts/IDs/dispositions, and add base and repair mutations for bad IDs, missing separators, and invalid dispositions.

### N5. BLOCKER — Twenty-three covered repairs lack an exact deciding oracle

[Observed] The exhaustive list is recorded under finding 2. Several are accepted-clause under-enumerations, not merely weak wording.

Minimum fix: either add a bounded independent oracle for each full consequence or disposition the uncovered limb separately as Unknown/believed not applicable.

### N6. BLOCKER — Item extraction remains parser-ambiguous

[Observed] Nine classes are named, but the Markdown grammar is not executable by two independent implementations without interpretation.

Minimum fix: bind each class to exact files, headings/levels, row or list syntax, normalization, duplicate behavior, and malformed-input outcomes; prove each with independent extraction fixtures.

### N7. DEFECT — Embedded RFC1–3 matrix totals are stale

[Observed] The file says 209 consequences while containing 210, and its RFC3/disposition counts are also stale.

Minimum fix: correct the embedded table and make generation/checking validate embedded per-family totals against parsed rows.

### N8. DEFECT — RFC6-17 sibling-state applicability is collapsed into an overbroad N/A row

[Observed] `RFC6-17.r2` groups sibling, challenge, reconciliation-chain, and work states as believed not applicable. The candidate explicitly renders drafted capabilities/proposals, so the `unadopted-draft` sibling-state limb is used even if challenge/chain/work states are not.

Minimum fix: split sibling-state composition from the genuinely unused state families and disposition each independently.

## Security verdict

**SECURITY VERDICT: REVISE**

[Observed] The operational trust boundary is substantially sound: exact repository consent pair, concrete policy and observer-registration triple, zero-read failure, contained Git-object reads, no observed-content execution, inert rendering, sink scanning, resource limits, and separate evidence/decision authority.

[Observed] The fail-closed coverage checker can still silently discard malformed security/authority consequences, and several claimed authority controls lack exact deciding oracles.

[Inferred] This is not an unsafe foundation, but it is not yet an acceptable implementation contract.

## Overall verdict

**REVISE**

[Inferred] Findings 3, 4, 6, 7, 8, 9 and pass-1 N2/N3 are confirmed. Finding 5 remains partial. Findings 1, 2 and pass-1 N1 remain materially unresolved; the malformed-row escape and semantic covered-row overclaims are blocking.
