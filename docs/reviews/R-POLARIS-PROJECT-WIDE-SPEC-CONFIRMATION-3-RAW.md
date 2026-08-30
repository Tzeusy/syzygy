# Independent confirmation report

## Exact subject and checks

[Observed] Review subject: exact commit `a89956847ecbc26b1529f205d115146e7b21723c`.

[Observed] No repository mutation was performed. The sole working-tree change remains the pre-existing unrelated `.gitignore`.

[Observed] All requested standard checks passed:

- Dependency generator selftest and `--check`.
- Contract-coverage generator selftest and `--check`.
- Strict OpenSpec validation.
- Governance: 759 files, 32 OK, 19 WARN, 0 FAIL.
- Governance selftest: 156 fixtures, 0 failing.

[Observed] Review-record integrity matches the disposition register:

- Original: `b47fbb0…9587dc`
- Pass 1: `b58286e…9d1d29`
- Pass 2: `79c15dc…24d5f`

[Observed] All six signed parent artifacts still match the exact digests in `THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md:42-49`; none differs from the signed parent commit.

## Independent arithmetic

[Observed] Two independent index/body methods agree on 324 accepted, unique RFC 0001–0009 clauses. Every indexed identity has exactly one definition in its indexed authoritative module.

[Observed] Matrix arithmetic:

- Base rows: `210 + 220 + 183 = 613`
- Repair rows: 68, superseding 62 distinct base rows
- Effective rows: `613 - 62 + 68 = 619`
- Effective dispositions: 136 covered, 235 Unknown uncovered, 248 believed not applicable
- All 324 accepted clauses represented; no extra clause identities

[Observed] Base family totals independently reproduce:

| RFC | Clauses | Rows | Covered | Unknown | Believed N/A |
|---|---:|---:|---:|---:|---:|
| 1 | 39 | 100 | 7 | 55 | 38 |
| 2 | 27 | 51 | 10 | 24 | 17 |
| 3 | 38 | 59 | 11 | 25 | 23 |
| 4 | 32 | 88 | 7 | 59 | 22 |
| 5 | 27 | 75 | 11 | 50 | 14 |
| 6 | 28 | 57 | 15 | 21 | 21 |
| 7 | 41 | 91 | 19 | 54 | 18 |
| 8 | 32 | 32 | 0 | 0 | 32 |
| 9 | 60 | 60 | 0 | 0 | 60 |

[Observed] Capability arithmetic is correct: 27 rows = 21 covered + 6 lawfully out of scope.

[Observed] The disposition register accounts for all 17 earlier findings: original 1–9, pass-1 N1–N3, and pass-2 N4–N8.

## Mutation testing

[Observed] The checker correctly rejected:

- IDs wholly outside its regex;
- malformed base and repair column counts;
- wholly invalid base and repair dispositions;
- incorrect embedded per-family counts;
- deletion of a base row while its embedded family count remained unchanged.

[Observed] It incorrectly accepted:

- a regex-valid base ID with the wrong clause prefix;
- a regex-valid repair ID with the wrong clause prefix;
- `covered:PWB-REQ-001junk`;
- a covered disposition using an undeclared `;` separator;
- a corrupted bold `Total` count row;
- deletion of the bold `Total` row;
- deletion of a repair row, restoring the superseded base row.

[Observed] An unregenerated repair deletion would still make `--check` report manifest drift. The parser itself nevertheless accepts the changed semantic overlay and can be made green by ordinary regeneration.

[Inferred] Pass-2 N4 and pass-1 N1 are not closed. The checker enumerates table rows better than before, but does not enforce exact identity relationships, exact covered-disposition syntax, or all embedded count rows.

## Exhaustive repair-overlay review

[Observed] The overlay contains 56 covered rows, 9 Unknown rows, and 3 believed-not-applicable rows.

### Covered rows with a deciding oracle

[Observed] These 52 rows have a bounded oracle matching the effective consequence:

- PWB-REQ-001/005: `RFC4-3.r2`, `RFC4-3.r3`, `RFC4-7.r1`–`r3`
- PWB-REQ-007: `RFC1-19.r1`–`r2`, `RFC1-24.r1`–`r2`, `RFC2-9.r1`, `RFC2-24.r1`, `RFC2-25.r1`, `RFC6-14.r1`–`r3`, `RFC6-17.r1`, `RFC6-17.r3`, `RFC7-16.r1`, `RFC7-16.r2`, `RFC7-16.r4`, `RFC7-33.r1`
- PWB-REQ-014: `RFC7-1.r1`, `RFC7-2.r1`–`r3`, `RFC7-3.r1`–`r2`, `RFC7-9.r1`–`r3`, `RFC7-10.r2`, `RFC7-12.r1`, `RFC7-29.r2`, `RFC7-33.r2`–`r4`
- PWB-REQ-015: `RFC7-12.r2`, `RFC7-13.r1`, `RFC7-14.r1`–`r2`, `RFC7-15.r1`, `RFC7-17.r1`–`r2`, `RFC7-26.r1`–`r2`, `RFC7-27.r1`
- PWB-REQ-016/022: `RFC7-31.r1`–`r3`, `RFC7-32.r1`, `RFC7-34.r1`–`r2`

### Covered rows not confirmed

1. [Observed] `RFC1-18.r1`: RFC1-18 defines durable identity from `(subject identity, cited normative-reference identity, declared scope)`. PWB-REQ-007 checks stability across two evaluations but defines no exact derivation or independent derivation oracle.

2. [Observed] `RFC1-18.r2`: the accepted clause requires deterministic same-evaluation identity and includes status as well as label/tier/reason/evidence/freshness/challenge. The repair consequence narrows that text, and PWB-REQ-007 has no same-evaluation rerun.

3. [Observed] `RFC2-10.r1`: the row explicitly claims evaluation-deterministic freshness, but the case compares two different evaluations rather than repeated runs of one evaluation.

4. [Observed] `RFC7-10.r1`: PWB-REQ-014’s closed anchor classes are `doctrine, contract, requirement, decision, evidence, work`. RFC7-10’s actual classes include kernel references, doctrine/contract citations, OpenSpec anchors, decisions or policies, and evidence. The candidate omits policy and does not independently compare its class vocabulary with RFC7-10.

[Inferred] Original finding 2 and pass-2 N5 remain blocking.

### Unknown/not-applicable rows

[Observed] The nine Unknown rows are conservatively and correctly disclosed: `RFC4-3.r1`, `RFC6-17.r2`, `RFC7-16.r3`, `RFC7-2.r4`, `RFC7-5.r1`, `RFC7-5.r2`, `RFC7-26.r3`, `RFC7-29.r1`, `RFC7-32.r2`.

[Observed] Release-only `RFC7-30.r1` and `RFC7-32.r3` are lawfully believed not applicable to this explicitly non-release change.

[Observed] `RFC6-17.r5` is not correctly classified. PWB-REQ-007 explicitly places challenge state on every project claim and exercises challenge fixtures. RFC6-17 requires challenge composition whenever aggregate members carry it. Challenge aggregation is therefore applicable and uncovered; only reconciliation-chain and work-state aggregation are genuinely unused.

## Targeted requirement conclusions

- [Observed] PWB-REQ-005 is internally consistent. It uses the consent/policy/registry triple throughout, verifies all three provenances, uses the exact `(observing Syzygy Project, configured Butlers repository)` subject, checks registry home/scope/empty write surface, and requires zero reads plus Unknown for every invalid case.
- [Observed] PWB-REQ-007 now covers challenge fields, aggregate label/tier/freshness/reason counts, tier meanings, and sibling separation. Durable-identity derivation and same-evaluation determinism remain insufficient.
- [Observed] PWB-REQ-014 now exercises deletion invariance, captured target-state immutability, personal-state exclusion, and a narrative machine type distinct from kernel Claim. Its target-class vocabulary does not match RFC7-10.
- [Observed] PWB-REQ-015 has exact `Base` mode, observed reality, three band classes/order, byte-verbatim requirement/scenario/doctrine/non-goal checks, proposal separation, and a static no-copy sweep.
- [Observed] PWB-REQ-021 and PWB-REQ-022 correctly separate execution evidence from owner decision authority. Run and judgment fields, homes, identities, modes, verdict, rationale, judging party, provenance, and exact `verdict-unlawful` handling are all independently checked.

## Item-extraction identity

[Observed] At Butlers commit `6a3c907c…a82992`, two independent implementations—a direct line/state parser and a Pandoc AST parser with punctuation rewriting disabled—produce the same row-based population:

- 395 identities total
- 182 baseline specs
- 61 catalog entries
- 80 topology components
- 27 design contracts
- 12 roster identities
- 13 success criteria
- 7 principles
- 7 craft policies
- 6 project-account sections

[Observed] The specification still admits a second result. Its reader definition says topology components use first-column table identities, while the literal grammar says topology-component “is each H2 … and each first-column bold label.” Treating each matching H2 as an item adds ten identities, yielding 405.

[Inferred] Two implementations agree only after choosing the row-only interpretation. The specification text itself does not uniquely compel that choice, so original finding 5/pass-2 N6 is not confirmed.

## Per-finding verdicts

| Finding | Verdict |
|---|---|
| Original 1 — consequence-granular matrix | **NOT CONFIRMED** |
| Original 2 — warrant overclaims | **NOT CONFIRMED** |
| Original 3 — capability denominator | **CONFIRMED** |
| Original 4 — consent and secret policy | **CONFIRMED** |
| Original 5 — closed item identity/discovery | **PARTIAL / NOT CONFIRMED** |
| Original 6 — containment, active content, resources | **CONFIRMED** |
| Original 7 — plain-copy oracle | **CONFIRMED** |
| Original 8 — complete cold-open prompt | **CONFIRMED** |
| Original 9 — authority language | **CONFIRMED** |
| Pass-1 N1 — silently dropped rows | **NOT CONFIRMED** |
| Pass-1 N2 — triple/pair consistency | **CONFIRMED** |
| Pass-1 N3 — evidence/decision separation | **CONFIRMED** |
| Pass-2 N4 — malformed-row escape | **NOT CONFIRMED** |
| Pass-2 N5 — semantic overclaims | **NOT CONFIRMED** |
| Pass-2 N6 — item grammar ambiguity | **NOT CONFIRMED** |
| Pass-2 N7 — embedded totals | **PARTIAL / NOT CONFIRMED** |
| Pass-2 N8 — sibling-state applicability | **NOT CONFIRMED** |

## New findings

### N9. BLOCKER — Exact row identities and covered dispositions remain under-validated

[Observed] Regex-valid wrong-prefix base/repair IDs and junk-bearing covered dispositions pass. Bold total rows are not checked, and a repair row can disappear while the superseded base silently returns.

Minimum fix: define and enforce canonical clause-to-consequence ID derivation; require exact comma-separated covered requirement syntax; validate family and bold-total rows; add declared repair row/supersession/disposition counts and mutations for wrong-prefix IDs, junk suffixes, missing totals, and deleted repair rows.

### N10. BLOCKER — Four repair rows still claim unsupported coverage

[Observed] `RFC1-18.r1`, `RFC1-18.r2`, `RFC2-10.r1`, and `RFC7-10.r1` lack an exact accepted-clause oracle.

Minimum fix: add exact independent derivation/repeated-run/vocabulary oracles, or split and disposition the unexercised limbs as Unknown.

### N11. BLOCKER — Topology extraction has two lawful readings

[Observed] Row-only extraction gives 395 identities; reading “each H2” literally gives 405.

Minimum fix: say explicitly that qualifying H2s establish the ordinal context but mint no item; only qualifying first-column table labels mint topology-component identities.

### N12. BLOCKER — Challenge aggregation is falsely believed not applicable

[Observed] PWB-REQ-007 makes challenge state part of project claims, while `RFC6-17.r5` declares challenge aggregation unused.

Minimum fix: split challenge composition into an applicable `unknown-uncovered` row; retain reconciliation-chain and work-state composition as separate believed-not-applicable rows if still unused.

## Security verdict

**SECURITY VERDICT: REVISE**

[Observed] The operational trust boundary in PWB-REQ-005/006 is substantially sound: exact consent subject, concrete policy and registry provenance, zero-read failure, exact-object containment, inert rendering, sink scans, resource limits, and separated evidence/decision authority.

[Observed] The contract checker still accepts malformed identity/disposition forms, and the matrix still overclaims identity and authority semantics.

[Inferred] This is not an unsafe foundation, but it is not yet an acceptable implementation contract.

## Overall verdict

**REVISE**

[Inferred] Mechanical totals and standard checks are green, but exact fail-closed matrix validation, four covered semantic rows, the item grammar, and RFC6-17 challenge applicability remain unresolved. No owner decision is needed to repair these specification correctness defects.
