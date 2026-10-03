# R-M9-POC-IDENTITY-AMENDMENT-3 — fresh-context review, round 3, Three-Surface POC identity amendment
Reviewed commit: 38c1c5c9be35419425a7177535c163894f51f1d4
Manifest SHA-256: 0a259835594eb846037bf643c7db648905a97fa68c1fc44d3ab03cb1209abf5e
Verdict: REVISE

Reviewer: fresh-context Claude agent, 2026-10-03. Clone of `.worktrees/parallel-agents/syzygy-dov.26` checked out at the commit above. The manifest digest is `sha256sum` of `THREE-SURFACE-POC-IDENTITY-AMENDMENT-MANIFEST.txt` (the file) at that commit.

Line citations of the form `proposed spec.md:N` and `proposed CONTRACT-COVERAGE.md:N` are into the six subjects after applying the four patches in a scratch copy outside the clone (`patch -p1`). Package files are cited by their own line numbers at the reviewed commit.

## What I ran and read

- [Observed] `python3 scripts/build_three_surface_poc_identity_amendment.py --check` exits 0: "manifest matches 6 proposed subjects (4 patched, 2 unchanged); 26 requirements, Part A 78 clauses over 132 rows; structure, regeneration and the preserved RFC1-26 row verify".
- [Observed] `--selftest` exits 0: "22 structure mutants, patch drift, manifest order and subject drift all fail closed on their own predicates". I read the selftest loop (builder lines 609–615). Each mutant must change the bytes and produce a finding that starts with its own expected predicate string. That is a per-predicate test, not an exit-code test.
- [Observed] `python3 scripts/check_governance.py`: "31 OK, 21 WARN, 0 FAIL (52 checks)". None of the 21 WARN lines names this package or its builder.
- [Observed] I applied the patches in a scratch copy and hashed all seven files in the change directory. The six subject digests equal the six manifest rows exactly. `tasks.md` is not a subject.
- [Observed] My own recount over the proposed matrix (Python, rows matching `^\| RFC`, split by section heading):
  - Part A: 132 rows over 78 clauses, 102 covered, 30 Unknown. Signed: 107 / 74 / 92 / 15.
  - Part B1: 28 rows over 27 clauses, before and after.
  - Part B2: 223 clauses signed, 219 proposed. 78 + 27 + 219 = 324.
  - The proposed `contracts[]` union over the 26 requirement blocks equals the Part A clause set (78 identifiers).
  - `GOVERNING-DEPENDENCIES.md` totals: 9 doctrine + 78 contracts + 3 decisions = 90 distinct authorities, as printed.
  - The proposed spec has 28 `#### Scenario:` headings, matching `IMPACT-LEDGER.md:162`.
- [Observed] Signed-row diff, signed versus proposed matrix, as multisets of `| RFC…` lines:
  - Six lines are removed: the RFC2 and RFC6 family-table rows, plus the four Part B2 rows RFC2-25, RFC6-1, RFC6-3 and RFC6-12.
  - Every other signed row survives, in its original relative order (subsequence check).
  - Of the 27 added lines, 2 are the recomputed family-table rows. The other 25 all carry "Amendment row".
- [Observed] The signed row `| RFC1-26 | Relations outside the closed table don't exist; no prose-widening | covered | POC-REQ-052 |` occurs exactly once in both the signed and proposed matrices, byte-identical (proposed CONTRACT-COVERAGE.md:90).
- [Observed] I recomputed every `IMPACT-LEDGER.md` figure at `ab22492` with `git ls-tree -r -z` and Python `re`, and all match:
  - 1,924 files, of which 4 fail UTF-8 decoding;
  - 46/242, 2/2, 3/8, 15/43, 37/68 and 21/55 for the six patterns;
  - 83 tracked `*.patch` files under `contracts/candidates/`.
- [Observed] `SEMANTIC-DELTA.md` §2's relation count also checks out:
  - RFC1-25's table has 26 data rows at RFC-0001 lines 596–621 and 30 backticked first-column tokens.
  - At `ab22492`, `poc-seeds.ts` emits 9 relationships over 8 kinds, and `contains` runs `project:butlers` → `capability:…` (lines 194–199).
  - Only `contains` is a table token.
- [Observed] Every quotation I checked matches its source:
  - RFC6-1 at RFC-0006 lines 108 and 112–118, RFC6-3 at line 135, RFC6-12 at line 263, and RFC6-14 at lines 279–291;
  - RFC1-26 at RFC-0001 lines 736–742;
  - RFC2-25's `asserted-by-worker` row (rendering-vocabularies.md:180);
  - `trust-and-evidence.md` lines 25, 84–85 and 115–116;
  - the design's lines 797–798 and 920;
  - Scope A's list at the 2026-10-02 direction lines 30–32;
  - the P-75 row (ruling record line 63);
  - `check_governance.py:1780`.
- [Observed] Residuals: `check_spec_reconciliation.py:214` pins `"POC": (24, 24)`, and `record_versioned_signoff.py:117–` `real_packages()` lists only `pwb-*` packages.

## Earlier repairs

- [Observed] Round 2's Findings 12, 14, 15, 16, 17, 18 and 19 landed as dispositioned.
  - The handle limb is now an Unknown row (proposed CONTRACT-COVERAGE.md:135).
  - "Exactly one link target" now has a duplicate-target count.
  - The Unknown slot's reason, route and encoding are now counted.
  - RFC6-12 is narrowed, with an Unknown row for openability.
  - The RFC6-14 disclosure has a mutant.
- [Observed] Round 2's Finding 13 landed only in part. The decision rule now counts all four falsifier limbs, and the account of `contains` is corrected. The correspondence repair took neither of the two forms the finding offered ("as literals, or make the role-pair limb Unknown"). Finding 20 below follows from that.

## Findings

**Finding 20 — The RFC1-26 disclosure row claims every role-pair violation is disclosed, but the role-pair decision rests on an unconstrained correspondence that no oracle checks** (revise)

- [Observed] POC-REQ-055 decides role-pair membership "read through a checked-in declaration that maps each shared-model entity kind to the RFC 0001 class it corresponds to, or to none" (proposed spec.md:1033–1036). Its oracle independence treats that declaration as an expected value: "the kind-to-class correspondence is a checked-in declaration; none is imported from the model" (proposed spec.md:1062–1064).
- [Observed] Two places put the declaration outside the signed text. The delta makes it "an implementation artifact of slice 8, in the same way that POC-REQ-060's token table is an implementation artifact" (`SEMANTIC-DELTA.md:188–190`). The requirement does not fix its content.
- [Inferred] The analogy with the token table does not hold:
  - A token table has no truth value; it *defines* the expected encoding.
  - The correspondence carries a truth claim ("the class it corresponds to"), and no stated procedure decides it. CC-SPEC's "without judgment" bar is therefore not met for this limb.
  - The correspondence also decides compliance. The same slice that emits the relationships writes it, so it is not independent of the implementation under test.
- [Observed] The RFC1-25 amendment row is honestly scoped: "read through a declared kind-to-class correspondence" (proposed CONTRACT-COVERAGE.md:88). The RFC1-26 amendment row is not. It claims: "Every emitted relationship outside the closed table, by kind or by role pair, is disclosed as outside it, with a reason, never presented as a closed-table relation" (proposed CONTRACT-COVERAGE.md:91). No Unknown row covers the truthfulness of the correspondence.
- **Failure scenario.**
  - [Inferred] Slice 8 checks in a correspondence mapping the POC kind `project` to RFC 0001's Capability class.
  - The `contains` relationship `project:butlers` → `capability:…` then reads as Capability→Capability, a pair the `contains`/`part_of` row assigns (RFC-0001:596). It is emitted unflagged.
  - Every count in POC-REQ-055's decision rule is zero, and the falsifier forbids flagging it ("a flag on a relationship the table fully admits", proposed spec.md:1067–1068).
  - Yet the delta itself classifies that edge as outside the table by role pair (`SEMANTIC-DELTA.md:168–175`).
  - So the RFC1-26 row's "never presented as a closed-table relation" is not observed by the oracle. This fails criterion 3, because a covered row claims a consequence its oracle does not observe, and criterion 2, because the correspondence limb has no deciding procedure.
- **Repair (either suffices).**
  - Write the correspondence for the POC's nine entity kinds as literals in POC-REQ-055 (or its reader notes), so the owner signs it and the oracle transcribes it.
  - Or qualify the RFC1-26 disclosure row the same way the RFC1-25 row is qualified ("… by kind, or by role pair as read through the declared correspondence …"). Then add an Unknown amendment row: "the declared kind-to-class correspondence matches RFC 0001's class definitions". The builder's totals and the 132/102/30 figures would move with it.

**Finding 21 — RFC1-25's semantic-class and Rule-column limbs, and RFC1-26's no-re-typing limb, have no Unknown row, and POC-REQ-055's falsifier forbids disclosing them** (note)

- [Observed] RFC1-25's table assigns each relation more than a role pair. Each row also has a Semantic class column and a Rule column, for example:
  - `contains`/`part_of`: "Only within one authority's own hierarchy; cross-authority nesting must use a typed relation" (RFC-0001:596);
  - `refines`: "Both endpoints adopted" (598);
  - `implements`: "Declared … or inferred (profile; challenge-only)" (601).
- [Observed] RFC1-26 adds that profiles "may not re-type these" (RFC-0001:739).
- [Observed] POC-REQ-055 decides only name and mapped role pair. Its decision rule counts "flagged relationships whose kind and mapped role pair the table assigns" as failures (proposed spec.md:1055–1060). The falsifier calls such a flag "a flag on a relationship the table fully admits" (proposed spec.md:1067–1068).
- [Inferred] Consider a closed-name relationship in an assigned pair that breaks its row's Rule or Semantic class, such as a cross-authority `contains` or an `implements` edge that is not challenge-only. POC-REQ-055 must leave it unflagged, and none of the 25 added rows lists that limb as Unknown.
- The amendment rows themselves are honestly scoped ("by kind or by role pair"), and the signed matrix's RFC1-25 limb inventory never listed these limbs. That is why this is a note.
- **Suggested change.** Add one Unknown amendment row under RFC1-25/26: "a closed-name relationship honours its row's semantic class and rule; no relation is re-typed". Also align "fully admits" in the falsifier with the decision rule's narrower "kind and mapped role pair".

**Finding 22 — The builder does not guard signed prose outside the matrix rows and the spec preamble, and its docstring still describes POC-REQ-055 per kind** (note)

- [Observed] I ran two mutations through `structure_findings` over the proposed bytes, and both returned `[]`:
  - replacing the matrix banner's "**No N/A is minted on the author's authority.**" with "**N/A may be minted.**";
  - renaming `proposal.md`'s "## Acceptance inputs" heading.
- In other words, the builder guards matrix *rows* (`coverage_findings`), spec blocks and the preamble before `## ADDED Requirements`, and one proposal line. It does not guard the matrix's non-row prose or the rest of `proposal.md`.
- [Observed] Spec edits outside the guarded regions are caught only incidentally: the regenerated `GOVERNING-DEPENDENCIES.md` embeds the spec's sha256, so any spec edit trips "differs from regeneration".
- [Observed] By diff, no such signed prose is edited in the current patches, so criterion 4 is met today. The guard is narrower than the docstring's "The signed bytes are never edited" framing suggests.
- [Observed] The builder docstring line 10 still reads "POC-REQ-055 (every relation kind is a closed-vocabulary name or flagged outside it)". The requirement is now per relationship and per role pair.

**Finding 23 — Lane B's disposal is evidenced by a code comment rather than the owner direction that disposed of it** (note)

- [Observed] `SEMANTIC-DELTA.md:60–61` cites `scripts/check_governance.py` line 1780, a source-code comment, for "Lane B was declined 2026-10-02 and never performed".
- [Observed] The owner record is `.syzygy/governance/decisions/POLARIS-LANE-B-DECLINED-AND-TARGET-REVISED-DIRECTION.md`, whose line 36 reads "1. **Lane B is declined.**".
- [Inferred] A comment is not authority (verification rule 8). Cite the direction instead. The P-75 sequencing condition is met either way.

**Finding 24 — POC-REQ-054's oracle leaves element-to-subject attribution and authority-less subjects unstated, and "a score, a verdict" is not separately decided** (note)

- [Inferred] Per-element identity equality (proposed spec.md:978–985) needs the checker to know which subject an element depicts *without* reading the identity it carries. Otherwise the comparison is circular. The requirement does not say how that attribution is made. It is probably feasible from labels or source routes, but it is unstated.
- [Observed] Oracle independence derives the expected identity "from … each subject's owning source record" (proposed spec.md:986–990).
  - The POC holds subjects with no owning source authority, such as `unknown-region` and `runtime` (`poc-seeds.ts` kinds at `ab22492`, lines 180–187).
  - For those subjects the derivation is unstated. The requirement's "mints none of its own" applies only "where a source authority owns" the identity.
- [Observed] The ribbon paragraph forbids an unfilled slot rendering as "a score, a verdict" (proposed spec.md:961). The decision rule counts slots lacking the Unknown label, reason, route or encoding, and slots styled as positive.
  - [Inferred] A slot that carries all four *and* a score passes.
  - The covered rows do not claim this limb, which is why this is a note.

**Finding 25 — POC-REQ-060's decision rule names the route and "exactly one" limbs only through "off-vocabulary"** (note)

- [Observed] The falsifier lists "an Unknown with no route" and a record breaching "exactly one primary reason". The decision rule reads "zero off-vocabulary records and zero breached Inferred limbs decide" (proposed spec.md:1130–1131).
- [Inferred] A missing route, or two primary reasons, is a shape defect, not a vocabulary defect. "Off-vocabulary" decides those limbs only if read as "off the closed-vocabulary shape", the Observable's wording.
- The RFC2-24 covered amendment row claims "exactly one primary reason … with its resolution route". Saying "zero records off the closed-vocabulary shape (label, tier nesting, exactly one primary reason with its route)" would close the reading.

## Criteria summary

1. **Ruling content:** met.
   - The package carries POC-REQ-054, the ribbon scenario, POC-REQ-055, the POC-REQ-060 amendment, Q3's disclosure repair with the signed row unedited, and Q4's landing zone.
   - The proposal and packet both say no production constructor exists without its own act (proposed proposal.md amendment section; `OWNER-DECISION-PACKET.md:53–55`).
   - The join-key departure from the adopted design is disclosed and put to the owner.
2. **Specification bar:** not met for POC-REQ-055's correspondence limb (Finding 20). Otherwise met, with notes 24 and 25.
3. **Contract claims:** not met. The RFC1-26 disclosure row over-claims (Finding 20). Every other added covered row I checked is observed by its requirement's oracle. The Unknown rows for RFC6-1, RFC6-3, RFC6-12, RFC6-14, RFC2-24 and RFC2-25 enumerate the uncovered limbs I found in those clauses' text, except as noted in Finding 21.
4. **Signed bytes:** met. Only the four named Part B2 rows and the two recomputed family rows leave. The RFC1-26 row is byte-identical. All six subject digests equal the manifest.
5. **Mechanics:** met.
   - `--check` and `--selftest` pass, and each mutant is matched to its own predicate.
   - The dependency file equals regeneration, and every printed total equals my computation.
   - The guard is narrower than the docstring (Finding 22).
6. **Honest claims:** met.
   - The package claims no adoption and schedules no implementation.
   - All three named residuals are present and verified (`SEMANTIC-DELTA.md:322–343`).
   - Finding 20's correction will need to reach the packet's POC-REQ-055 paragraph if the disclosure row is narrowed.
7. **Plain language:** met. The packet's three bullets and its "What signing does not do" section let a fresh reader restate what changes and what does not.
