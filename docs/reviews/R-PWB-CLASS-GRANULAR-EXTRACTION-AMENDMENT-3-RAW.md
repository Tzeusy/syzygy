# Review round 3 — PWB class-granular extraction amendment (M15)
Reviewed commit: 00e24fd2dd10e8ffa8ba9cbecf88f58443fe72df
Manifest SHA-256: 4562e028fc56b8b87aead03080aa9c515ce0308806a693977b9fcb35d8750abb
Verdict: REVISE

Reviewer: a fresh-context agent that did not draft this package. Brief:
`.syzygy/governance/contracts/candidates/pwb-class-granular-extraction-amendment/REVIEW-BRIEF.md`,
including its Round 3 section. Following that section, I did not read
`ROUND-1-DISPOSITIONS.md`, `ROUND-2-DISPOSITIONS.md` or anything under
`docs/reviews/`. The dispatcher also asked me to check that each round-2
finding was repaired, which conflicts with that instruction. I followed the
brief. I checked the round-2 repairs the package itself names (the packet's
status paragraph and Q7, and the delta's parenthetical repair notes), and I
judged the rest of the current bytes on their own merits.

Manifest digest: [Observed] `git show 00e24fd2…:<manifest path> | sha256sum`
gives the value on line 3. `sha256sum` over the file in a fresh clone at that
commit gives the same value.

## Checks run

All of these ran in a fresh `git clone --no-hardlinks` of this worktree,
detached at `00e24fd2` (rule 7). [Observed] at that commit:

- `build_pwb_class_granular_extraction_amendment.py --check` reported "class-granular candidate matches 11 proposed subjects (5 patched); 17 requirements, 54 scenarios; structure, regeneration, contract coverage, sibling classification and pending-patch order verify".
- `--selftest` reported "39 structure mutants, a manifest row, a contract-coverage count, patch drift, an unclassified sibling, the pending patch population, and divergent and failing application orders all fail closed on their own predicates".
- `build_pwb_release_label_amendment.py --check` passes: 11 subjects, 7 patched, 17 requirements, 55 scenarios.
- `check_spec_reconciliation.py --check` gives "7 of 7 predicates without FAIL; PASS". R6 is WARN, report-only: two pins are stale, attributed to `syzygy-2g0d`.
- `check_governance.py` has no FAIL line. Every line is OK or WARN (grep of the full output over `^(FAIL|OK|WARN)`).
- Rule-6 probe, my own script, outside the clone:
  - It re-ran the selftest's 39 structure mutants and printed each mutant's whole finding list.
  - It added three mutants of my own over phrases that have no dedicated mutant: "neither qualifies a count of the third or fourth rule", "The first and second rules need the root index;", and the third-rule naming clause.
  - All 42 fail. Each fails on its own predicate, not just on the shared GOVERNING-digest finding that every spec mutant also trips (see Finding 2 for what the selftest's assertions prove).
  - The manifest-row mutant asserts exact equality with the one manifest finding. The contract-coverage mutant asserts the generator's own `DRIFT` line. Both are specific.
- Code claims, re-read at `00e24fd2`. [Observed]
  - In `project-shape-manifest.ts`:
    - `SOURCE_RULES` is at line 71 with exactly the five names.
    - The comment "Rule 1 — the root index and the pillar roots it names" is at line 403.
    - `RootIndexState` is at line 126 with `read`, `unavailable` and `missing-at-revision`.
  - In `project-shape-extraction.ts`:
    - The module comment's whole-source sentence is at lines 14–17.
    - `CATALOG_HEADINGS` is at line 56.
    - `extractCatalogEntries` is at line 438.
    - `extractSource` is at line 628, with `kind: 'unknown'` on the first failed class at line 646.
  - `git diff --stat ef5d5f03 8f1fbec7` over the signed change directory and both code files is empty, as the delta says.
  - `git diff --stat 8f1fbec7 00e24fd2` touches only this package, its builder and the pending register.

## Criterion summary

1. **Ruling content.**
   - The package carries all four answers:
     - Q1: a delta only.
     - Q2: partially extracted is designed, not built.
     - Q3: a surface flag with a counted, routed Unknown.
     - Q4: root-independence flags in the same delta.
   - The drafter's readings are put to the owner as Q2–Q4, Q6 and the new Q7.
   - Q6 puts the narrower Q3 scope fairly and names the open half. It is now an open owner question, not a signing-change residual.
   - Met.
2. **The specification bar.**
   - The SHALL, oracle, falsifier and scenario limbs are present:
     - for the class rule;
     - for the source-level rule;
     - for the unenumerated-heading count;
     - for rule provenance;
     - for the root-index qualification.
   - The round-3 addition is **not** fully met. The provenance oracle cannot be decided without judgment for a source that two population rules admit (Finding 1).
   - A read root index whose grammar fails is decided one way, as still read. Q7 puts that reading to the owner.
3. **The category rule and the exactness reach.**
   - A class's and a category's denominator is Unknown whenever the class is Unknown in any source, for a failed class or an unenumerated heading.
   - The source-level rule stops a read sibling from masking a failed or flagged class.
   - The per-class exactness rule binds every class a source is assigned, for loaded and built-in grammars alike.
   - Former whole-source grammar failures now surface as partially extracted, with the source's own denominator Unknown. Nothing becomes silently partial.
   - Met.
4. **Signed bytes.** The builder's predicates passed, and their mutants fail. Met.
5. **Honest claims.**
   - The [Observed] code claims hold.
   - The V1 index's tenth heading is honestly [Unknown].
   - The package claims no adoption.
   - One bead attribution is stale, and the collision census names one pending sibling where four exist (Findings 3 and 4).
6. **Mechanics.**
   - Everything passes, and the totals (28 + 6 + 0 = 34) are computed by the builder.
   - The selftest's per-mutant assertions are weaker than its summary line claims (Finding 2).
7. **Plain language.** The packet's "What you would be signing" restates the change and its non-effects clearly. Met.

Round-2 repairs that the package names, each checked against the bytes:

- The shared-rules sentence now reaches "the shared rules above". Present in hunk 2.
- The root index has a rule name: `root-index`, under the first rule. Present, and asserted by scenario 3's last AND.
- "Read" is defined, and a read root index with a failing grammar is still read. Present, and put to the owner as Q7.
- Q4's recommended arm now discloses its reach beyond Butlers. Present.
- The open Q3 half moved from the residuals to an open owner question. Present.

I did not check the other round-2 findings against their record, because the brief forbids reading it.

## Findings

**Finding 1 — Rule provenance is undecidable for a source that two population rules admit** (revise)

The repaired reader definitions bind one name to each of the four signed rules:

> the second rule admits each file a pillar's index names as
> `pillar-named-file`; the third admits each baseline spec as
> `baseline-spec-tree`; and the fourth admits each roster `butler.toml`, and
> its `MANIFESTO.md`, as `roster-tree`.

The oracle and falsifier then require a single answer:

- Oracle: "every source names the rule that an independent derivation of the source-path population admits it under".
- Falsifier: "a source names no rule or a rule other than the one that admitted it".
- Scenario 3: "every admitted source names the rule that admitted it".

Neither the signed source-path sentence nor any added line says which name a source carries when more than one rule admits it. [Observed] Swept with `grep -i -E "whoever|owned by|both rules|more than one rule|names it|overlap"` over the proposed-at-HEAD `spec.md` and `design.md`. It returned three hits, none of them on this point.

The overlap is not hypothetical. [Observed] `project-shape-manifest.ts`:

- Line 284 says Butlers' "real Spec and Spine mapping" is to `openspec/`. A file that `openspec/README.md` names inside `openspec/` falls under the second rule. If it is `openspec/specs/<d>/spec.md`, it also falls under the third.
- The code settles this by a precedence the text never states. Lines 471–478 give a baseline spec or a roster `butler.toml` to rules 3 and 4 "whoever names it", "review of syzygy-1z3.29".
- A roster `MANIFESTO.md` named by a pillar index stays `pillar-named-file`, because line 478 excludes only `butler.toml`. So the code contradicts the new text's "the fourth admits … its `MANIFESTO.md` … as `roster-tree`" for that case.
- `addSource` keeps the first registration (line 393). So the root index, if a pillar index named it, would stay `root-index` by order alone.
- A loaded profile's `pathPattern` population that matches a pillar-named file has the same gap.

[Inferred] Whether Butlers' Spec and Spine index actually links to a baseline spec at `32f38feb` is unknown here, since no Butlers body was read. The code's guard shows the case was met once.

Consequences:

- An independent derivation that applies the four rules as written admits such a file under two rules. The oracle then has no single "rule it admits it under" to compare with.
- An implementation could name either rule, or follow the code's precedence, and an assessor could not say which complies.
- The round-3 brief asks exactly whether the provenance oracle "can be decided for every admitted source … without judgment". For this population it cannot.

The same gap leaves the `rootIndexRequired` flag of a doubly admitted source tied to whichever name is chosen. With the root index unread the outcome is harmless, because the rule-3 or rule-4 admission still stands. With it read, the source's provenance is still ambiguous.

Repair direction, for the drafter: state the precedence in the reader definitions, for example "a source more than one rule admits carries the name of the last of them in rule order; a loaded profile's population …", and cover the `MANIFESTO.md` and root-index cases. Give it its own falsifier limb or scenario, and a selftest mutant. Because it is a reading, put it to the owner, or tie it to the code's existing precedence and say whether that changes the code's `MANIFESTO.md` behaviour.

**Finding 2 — Five selftest mutants assert only a generic prefix, so the selftest does not prove they "fail on their own predicates"** (note)

Most mutants assert the specific phrase they remove. Five assert a prefix that any required-phrase failure would satisfy:

- "falsifier limb dropped" and "per-class oracle dropped" each expect `"PWB-REQ-002 carries 0 copies of required phrase"`.
- "signed scenario dropped" and "new scenario dropped" each expect `"PWB-REQ-002 lacks exactly one"`.
- "design catalog-count sentence dropped" expects `"design lacks"`.

[Observed] My re-run shows each of the five does in fact fail on its own phrase:

- 'a failed class withholds the items of a sibling class that r…'
- 'The comparison is made per source and class'
- the two scenario headings
- 'No `catalog-count` declaration is minted…'

So the predicates hold, but `selftest()` would still pass if one of them failed only on some other phrase, and the summary line overstates what is asserted.

Two new round-3 phrases have no mutant at all: "neither qualifies a count of the third or fourth rule" and "The first and second rules need the root index; …". My probes show both fail closed on their own phrase. The docstring honestly says the mutants are "a sample of the required phrases". Suggested: assert each mutant's full phrase prefix, and add mutants for the two root-index phrases the round-3 brief singles out.

**Finding 3 — The registry and policy pin residual names a performed bead** (note)

The delta's residual 4 says both pins are "already stale and Unknown until their own act (`syzygy-jloi`)". The ledger's "Registry entry and policy" section (line 113) says the same and is labelled plain [Observed].

[Observed] `bd show syzygy-jloi` gives "CLOSED … Performed 2026-10-02; PR #207". At `00e24fd2`, `check_spec_reconciliation.py` R6 attributes the current staleness to `syzygy-2g0d`, the tree-framing re-pin routed as P-95. The residual block is labelled [Observed at `ef5d5f03`], when the checker did name `syzygy-jloi`. The repairs re-derived the ledger census at `8f1fbec7` but left this attribution unrefreshed. Mark it at the sentence, or re-attribute it to `syzygy-2g0d`/P-95.

**Finding 4 — The collision census names one pending sibling; the builder lists four** (note)

Places that name only the release-label amendment:

- `IMPACT-LEDGER.md` line 20 says "Every sibling but one is performed or declined. The pending one, the release-label amendment…".
- "Packages and fields this collides with" lists only the release-label amendment among spec packages.
- The delta's "Downstream impact" says "**The pending sibling:** the release-label amendment".

[Observed] `PENDING_SIBLINGS` in the builder at `00e24fd2` holds four packages:

- accessible-name
- anchor-resolution
- opening-index
- release-label

The builder docstring (lines 120–124) and the ledger's 2026-10-14 sub-bullet partly disclose the others. Their spec patches touch other requirements, and the all-orders check passes over all five, so this is not a semantic collision. The table row is still a current-tense claim that is false at the reviewed commit, and criterion 5 asks the package to name what it collides with. Date the row, or list the four pending siblings with "composes, all-orders checked".

**Finding 5 — Scenario 3 does not exercise the source-path population total's qualification** (note)

The reader definitions require that "every source-path population total" counting a root-independent source states that it was derived without a read root index. Scenario 3's THEN covers only "every class and category count". The oracle limb is per source ("every source a rule that does not need it admitted carries the qualification"). Only the general falsifier limb ("a count derived without a read root index is shown without that qualification") reaches the total. The obligation is falsifiable, but it has no scenario of its own. Consider adding "and the source-path population total" to scenario 3's THEN.

Counts: 1 revise-level finding (Finding 1), 4 notes (Findings 2–5), 0 blocking.
