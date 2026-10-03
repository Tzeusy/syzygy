# R-M9-POC-IDENTITY-AMENDMENT-2 — fresh-context review of the Three-Surface POC identity amendment package (round 2)
Reviewed commit: 25f4e891f8a9e0f19c2f8d0f4a3444e39c3e603a
Manifest SHA-256: a61970f5a6e10efb50dab65c2c9e89147a180a1b38cfb0d028f073e35fcc9d4e
Verdict: REVISE

Reviewer: a fresh-context agent. It read only the package, the governing references `REVIEW-BRIEF.md` lists, the acceptance criteria, and the round-1 raw and dispositions, which it read to check the repairs. The review ran in a clone of `.worktrees/parallel-agents/syzygy-dov.26` checked out at the commit above. No repository file was edited. The proposed bytes were read through `--diff`. The patches were also applied with `git apply` in a scratch copy outside the clone, built by `git archive HEAD openspec/changes/three-surface-poc-experience`. The manifest digest above was computed with `sha256sum` over the manifest file.

## Mechanics run

- [Observed] `python3 scripts/build_three_surface_poc_identity_amendment.py --check` printed: "manifest matches 6 proposed subjects (4 patched, 2 unchanged); 26 requirements, Part A 78 clauses over 130 rows; structure, regeneration and the preserved RFC1-26 row verify".
- [Observed] `--selftest` printed: "selftest: 19 structure mutants, patch drift, manifest order and subject drift all fail closed on their own predicates". I counted 19 entries in the `mutants` dict (`scripts/build_three_surface_poc_identity_amendment.py:485-585`). Each entry is checked by `f.startswith(expected)` (line 590), so every mutant fails on its own named predicate.
- [Observed] `python3 scripts/check_governance.py` printed "31 OK, 21 WARN, 0 FAIL (52 checks)".
- [Observed] In the scratch copy, the sha256 of each of the six applied subjects equals its manifest row (manifest lines 7–12).
- [Observed] I counted the proposed matrix with my own Python, independently of the builder:
  - signed matrix: Part A 107 rows over 74 clauses, 92 covered and 15 Unknown; Part B1 28 rows over 27 clauses; Part B2 223 clauses;
  - proposed matrix: Part A 130 rows over 78 clauses, 102 covered and 28 Unknown; Part B1 28 rows over 27 clauses; Part B2 219 clauses.

  These agree with `SEMANTIC-DELTA.md:247-252` and the printed totals. The proposed spec has 26 `### Requirement:` headings and 28 `#### Scenario:` headings, which agrees with `IMPACT-LEDGER.md` ("26 requirements and 28 scenarios").
- [Observed] Criterion 4. A line diff of the signed coverage matrix against the proposed one removes only these lines:
  - the RFC2 and RFC6 family-table rows;
  - the Total row;
  - the Part A totals sentence;
  - the four Part B2 rows RFC2-25, RFC6-1, RFC6-3 and RFC6-12;
  - the Part B2 total;
  - the two count sentences in "Verifying this table".

  Every added `| RFC` row contains "Amendment row", except the two family-table rows.
- [Observed] Signed row. The row `| RFC1-26 | Relations outside the closed table don't exist; no prose-widening | covered | POC-REQ-052 |` appears exactly once in the signed matrix and exactly once in the proposed matrix, byte-identical.
- [Observed] The impact ledger's figures re-derive exactly at `ab22492`:
  - 1,924 paths from `git ls-tree -r -z`, with 4 skipped on UTF-8 decode failure;
  - `POC-REQ-060`: 46 files and 242 occurrences;
  - the continuation regex: 2 files and 2 occurrences;
  - `POC-REQ-05[45]`: 3 files and 8 occurrences;
  - `POC-REQ-052`: 15 files and 43 occurrences;
  - the spec path: 37 files and 68 occurrences;
  - the coverage path: 21 files and 55 occurrences.

  No continuation form of 054 or 055 exists at that commit. I checked with `git grep -P 'POC-REQ-[^\n]*(?:, |/|\.\.| and |–|-)05[45]\b'` after filtering out the literal forms: 0 hits.
- [Observed] Quotations checked against their sources:
  - P-75's arm text and consequences column (`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:63`);
  - RFC6-1 at `RFC-0006…:108`, with its bullets at 112–115 and 116–118;
  - RFC6-3 at line 135;
  - RFC6-12 at line 263;
  - RFC1-26 at `RFC-0001…:736`, including "no drafter, reviewer, adapter, or profile may widen the core vocabulary by prose";
  - RFC1-25's table: 26 data rows at lines 596–621 and 30 backticked tokens in column 1, counted by Python;
  - doctrine `trust-and-evidence.md:25`;
  - the lane-B sentence at `scripts/check_governance.py:1780`;
  - POC-REQ-060's signed sentence.

  All match.

## Repairs from round 1

[Observed] I checked each round-1 finding against the current bytes:

- **Landed:** 1, 2, 3, 5, 6, 7, 8, 9, 10 and 11.
- **Partly landed:** Finding 4. The round-1 repair instruction was "extend each Oracle line to the limbs its Falsifier lists". POC-REQ-060's oracle now names a procedure per Inferred limb. POC-REQ-054's oracle still decides none of its falsifier's surface-local-handle limb, and POC-REQ-055's decision rule still omits a falsifier limb (Findings 12 and 13).

## Findings

**Finding 12 — POC-REQ-054's decision rule leaves several limbs undecided that its requirement, falsifier, scenarios and covered rows claim** (revise)

- [Observed] The oracle decides on three counts only: "zero mismatched identities, zero dangling or mis-resolving links and zero absent or unjoined slots decide" (`proposed/spec.md.patch:78-82`). The following limbs are claimed elsewhere, and none of the three counts decides them.
  - **Surface-local handle.** The required behavior says "No surface-local handle … SHALL stand in for the identity where it crosses a surface boundary, a link or the machine answer" (patch:52-54). The falsifier lists "a surface-local handle used as a crossing identity" (patch:90). The covered RFC6-1 amendment row claims "no surface-local handle crosses a surface boundary, a link or an endpoint as the identity" (`proposed/CONTRACT-COVERAGE.md.patch:55`).
    - No procedure decides whether an identity value is a surface-local handle.
    - Oracle independence derives the expected identity from "each subject's owning source record" (patch:83-87). If that derivation yields a path-keyed value, a path-keyed link resolves correctly and passes all three counts.
    - [Inferred] CC-SPEC-4 requires an oracle that decides "by a stated procedure … without judgment". This limb has none.
  - **"Exactly one element".** The requirement asks that an element resolve "to exactly one element for the same subject on that surface" (patch:50-51). Duplicate elements carrying one identity on a surface are not counted. The oracle checks only links that exist.
  - **The reasoned Unknown slot.** The ribbon paragraph requires an unfilled slot to "render Unknown with its reason and its resolution route — never absent, blank, a score, a verdict or styled as a positive state" (patch:58-61). The ribbon scenario's THEN asserts that neither slot is "absent, blank or styled as Observed" (patch:106-109). The decision rule counts absent or unjoined slots only. An Unknown slot with no reason or route, or one styled as Observed, passes it.
  - **The RFC6-12 covered row.** The row claims "The same subject identity opens the subject on every surface that renders it" (CONTRACT-COVERAGE.md.patch:61). The case "follows every link between surfaces" (patch:71), but nothing requires that a link or any by-identity opening exists. A subject rendered on two surfaces with no link between them is outside every count, so "opens … on every surface that renders it" is not observed. This fails criterion 3: the row claims a consequence its oracle does not observe.
- **Repair.** Do one of the following:
  - add a deciding count for each limb, for example a stated predicate that classifies a value as surface-local, a per-surface duplicate count, and reason, route and encoding checks per Unknown slot; and either require a by-identity opening for every multi-surface subject or narrow the RFC6-12 row to "every link between surfaces that exists resolves by the identity";
  - or move the undecided limbs to Unknown amendment rows.

**Finding 13 — POC-REQ-055's role-pair check has no declared entity-kind correspondence, decides only "reversed" roles, and the one in-table kind emitted today fails it undisclosed** (revise)

- **No declared correspondence.** [Observed] RFC1-25's Domain → Range column is written in RFC 0001's entity classes, for example "Project→Repository (declared); Repository→Code element (observed); … Capability→Capability" for `contains`/`part_of` (`RFC-0001…:596`).
  - The package itself records that "the POC's entity kinds are not RFC1-5's kinds" (CONTRACT-COVERAGE.md.patch:56). The POC's kinds are `project`, `capability`, `intent`, `code-region`, `test-definition`, `work-item`, `test-evidence`, `runtime` and `unknown-region` (`packages/three-surface-poc-core/src/poc-seeds.ts:131-187`).
  - The oracle independence says only that "each relation's set of role pairs are literals transcribed from RFC1-25's table" (`proposed/spec.md.patch:150-152`). Nothing declares how a POC kind maps to a Domain or Range class. [Inferred] So the check "against the set of role pairs the table assigns that relation" cannot terminate without judgment, which CC-SPEC-4 forbids.
- **The decision rule is narrower than the requirement.** [Observed] The rule reads "zero unflagged out-of-vocabulary kinds, zero flagged in-vocabulary kinds and zero reversed roles decide" (patch:147-149). The required behavior demands "the roles that table assigns the relation" (patch:128-129). A closed name emitted in a pair that is unassigned but not reversed passes the rule. The rule also omits a limb that the case (patch:142-143) and the falsifier (patch:155) both name: "a flagged kind rendered without its reason".
- **The eighth kind does not comply.** [Observed] The POC's one closed-name relationship is `contains` from `project:butlers` to `capability:whatsapp-transport-identity` (`poc-seeds.ts:194-199`).
  - Project→Capability is not among `contains`'s six assigned pairs. That row's rule says "cross-authority nesting must use a typed relation" (`RFC-0001…:596`).
  - The falsifier forbids "a flag on a kind that is in the table" (patch:154), so this relationship has no disclosure path. It must be renamed or re-typed.
  - The owner packet says "Seven of today's eight are outside" (`OWNER-DECISION-PACKET.md:24`). The delta's §2 reports only the name check (`SEMANTIC-DELTA.md:154-159`). [Inferred] A reader concludes that the eighth complies, and under the proposed text it does not. The owner is not told that all eight current kinds fail POC-REQ-055.
- **Repair.**
  - Declare the POC-kind-to-RFC1-class correspondence the check uses, as literals, or make the role-pair limb Unknown.
  - Make the decision rule count "closed name outside its assigned pairs" and "flag not rendered with its reason".
  - Correct the packet's and delta's account of `contains`.

**Finding 14 — The Inferred scenario asserts a tier the requirement does not require** (note)

- [Observed] The scenario "An agent assertion stays Inferred" requires that the record "carries the label Inferred with the tier `asserted-by-worker`" (`proposed/spec.md.patch:243-250`).
- The requirement requires a tier only "where one applies" (patch:188-189). The oracle validates tier membership and nesting, but not which tier an agent-asserted record must carry.
- RFC2-25 defines `asserted-by-worker` as an assertion "with no retained artifact" (`rendering-vocabularies.md`, RFC2-25 table). [Inferred] An agent assertion that carries a retained artifact might take no tier, or a different one.
- **Repair.** State the tier obligation in the requirement text, or drop the tier from the THEN.

**Finding 15 — "a code region's [identity owned] by its observed revision" misnames the owning authority** (note)

- [Observed] POC-REQ-054 reads: "a work item's by its tracker, a code region's by its observed revision" (`proposed/spec.md.patch:47-49`).
- RFC 0001's identity table gives Code element as minted by "Source adapter — adapter-defined, **not path-only**" (`RFC-0001…:224`). A revision identifies a snapshot, not the element.
- [Inferred] The parenthetical names the wrong authority for the one identity form the package deliberately leaves open. Name the source adapter, or drop the example.

**Finding 16 — Q4's "no production constructor" limb is carried nowhere a signer reads it as still binding** (note)

- [Observed] P-75 Q4 reads "`Inferred` added as a typed landing zone with no production constructor".
- The proposed spec only says the limbs are exercised by a fixture "While no agent has asserted anything" (patch:204-206).
- The proposal says "no Inferred record exists until an agent does" (`proposed/proposal.md.patch`, the amendment section). That reads as permitting a production Inferred record once an agent asserts.
- The adopted design says a constructible arm is an escalation needing its own act (`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:690`). The packet's "What signing does not do" (`OWNER-DECISION-PACKET.md:47`) does not say that signing leaves the arm unconstructible.
- [Inferred] The retained non-goal "Inferred mappings, edges or missing intent" (`proposal.md:67`) also sits beside a record shape that now admits an Inferred relationship. That relationship is an inferred edge, and the package calls the non-goal "unchanged" without reconciling the two.
- **Repair.** Add one sentence to the packet and the proposal: signing does not make the Inferred arm constructible in production, and that needs its own act.

**Finding 17 — POC-REQ-060 narrows doctrine's Inferred definition and anchors only to the narrower sentence** (note)

- [Observed] Doctrine defines Inferred as "the output of a declared inference process, carrying its inference provenance" (`trust-and-evidence.md:84-85`). It requires the inferred layer to record "the model, version, and inputs that produced it" (lines 115–116).
- POC-REQ-060 restricts Inferred to "an agent's assertion" and requires only that the record "name the agent assertion it arises from".
- The delta cites line 25 alone (`SEMANTIC-DELTA.md:224-225`).
- [Inferred] The narrowing follows the adopted design's Q4 framing (`POLARIS-M9-ONE-IDENTITY-FUNNEL.md:48`), so it does not exceed the ruling. The delta should still say it is a narrowing, and why the provenance limb is lighter than doctrine's.

**Finding 18 — The builder overstates its rule-6 coverage, and the RFC6-14 disclosure is unguarded** (note)

- [Observed] The docstring says "`--selftest`   one rule-6 mutation per predicate" (`scripts/build_three_surface_poc_identity_amendment.py:18`).
  - `REQUIRED_PHRASES` holds 27 phrase predicates (lines 91–125, counted by Python), and the 19 mutants exercise a handful of them.
  - Some predicates have no mutant at all: "warrants do not cite ruling", "the specification's title, banner or Purpose changed", "undeclared subject change" and "declared patched subject is unchanged".
- [Observed] Replacing the heading "**Amendment disclosure — the RFC6-14 fold note.**" with "**Note.**" in the proposed matrix returned zero findings from `structure_findings`. Round 1's Finding 6 repair therefore has no guard.
- Criterion 5 as written is met, because each mutant fails on its own predicate. The docstring's claim is not.
- **Repair.** Reword the docstring, or add the missing mutants and a predicate for the RFC6-14 disclosure.

**Finding 19 — "adds two things" introduces three bullets** (note)

- [Observed] `SEMANTIC-DELTA.md:170` reads "The proposed matrix adds two things:", and three bullets follow (lines 172–179).
- This is a small plain-language defect (criterion 7).

## Criteria summary

1. **Ruling content:** met, with Finding 16 on Q4's constructor limb.
2. **Specification bar:** not met, because of Findings 12 and 13.
3. **Contract claims:** not met. The RFC6-1 and RFC6-12 covered rows (Finding 12) and the RFC1-25 role-pair row (Finding 13) claim consequences their oracles do not decide.
4. **Signed bytes:** met. I verified it by diff, and the RFC1-26 row is byte-identical.
5. **Mechanics:** met, with Finding 18.
6. **Honest claims:** met for adoption and scheduling. All three named residuals are present (`SEMANTIC-DELTA.md:278-294`). The packet's "seven of eight" understates the impact (Finding 13).
7. **Plain language:** largely met (Finding 19).
