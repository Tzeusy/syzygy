# Semantic delta 3 — compact specification acceptance and impact rules

**Artifacts:**

- `../policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`
- `../policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`

**Stable IDs affected:** `CC-SPEC-1` through `CC-SPEC-11` and `CC-IMPACT-1`
through `CC-IMPACT-7`; none is added, retired, reused, or renumbered.

**Overall change class:** **Normative.** The proposal adds acceptance units,
source-complete populations, deterministic failure paths, and merge blockers
that a predecessor-compliant artifact could lack. Structural rewriting and
clarifications take the highest class present.

**Author:** Codex drafting worker for `syzygy-2dn`

**Date:** 2026-08-28

## Human summary

The confirmed mainline policies accumulated chronology, review codes, and
patch-specific explanations until the active rules were difficult to apply.
This proposal replaces that presentation with one repeated format for every
rule: purpose, inputs/population, decision, possible results, missing-evidence
behavior, retained evidence, and sources.

The acceptance policy now says exactly what is accepted, how every obligation
and accepted-contract consequence enters a population, how it is classified,
where Unknown lives, and why Unknown defers acceptance. The impact policy now
freezes the accepted specification corpus, reconciles generated declarations
against their expected requirement unions, partitions all relationships into
four results, and blocks partial merge. Stable rule IDs and the sibling-policy
model remain. Amendment chronology and review dispositions live here, not in
the rules.

> **Authority boundary.** This record and both policy files are proposals until
> a performed owner Decision names their exact final digests. An act naming
> those digests can confirm the same frozen bytes without a banner edit. This
> draft authorizes no merge, adoption, approval-record edit, implementation, or
> owner act.

## Exact mainline-to-proposal mapping

The mainline baseline is commit
`4ee5847bd68344d671e72677b828dd5520cecb21`. Its two policy subjects are
byte-identical to tag `craft-acts-6-7-confirmed-2026-08-17` and reproduce the
performed-act digests:

```text
CC-SPEC   9889b7e311ad941eec84d01dc2c035c7e2502a57cf18e68a1028a76d5b814871
CC-IMPACT cd6ec838e701f0258889d0c3c2776fc91fe1686829379b789ae5b151b04c27c0
```

The proposal is the complete content of the same paths at the exact review
head. This command emits every old and new line, so no excerpt selection can
hide a changed obligation:

```sh
BASE=4ee5847bd68344d671e72677b828dd5520cecb21
REVIEW_HEAD=$(git rev-parse HEAD)
git diff --no-ext-diff --unified=100000 "$BASE" "$REVIEW_HEAD" -- \
  .syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md \
  .syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md
```

Completeness is checked independently by requiring the path census below to
emit exactly the two subjects and `git diff --check` to emit nothing:

```sh
git diff --name-only "$BASE" "$REVIEW_HEAD" -- \
  .syzygy/governance/contracts/candidates/policy-candidates/
git diff --check "$BASE" "$REVIEW_HEAD" -- \
  .syzygy/governance/contracts/candidates/policy-candidates/
```

The repository-level proposal diff must contain exactly these two subjects and
this record—three tracked files, no fourth file.

`[Observed]` `git show | sha256sum` and an independent Python byte read both
reproduced the two baseline digests above and byte equality between mainline
and the act-bound tag. `sha256sum` and Python also independently reproduced the
CC-IMPACT-7 fixture and answer-key digests printed in that rule.

## Complete obligation map and canonical classes

Each row accounts for the full stable-ID obligation against mainline. The
full-file mapping above owns exact text.

| ID | Mainline obligation | Proposal disposition | Class |
|---|---|---|---|
| CC-SPEC-1 | One coherent capability and clear scope. | Preserved; adds explicit whole-capability/focused-change units, baseline, difference, and omission failure. | Normative |
| CC-SPEC-2 | Six closed governing-warrant fields, all material accepted authority, generated spec union, no user-need escape. | Preserved; defines materiality and Unknown, names requirement provenance, and separates RFC1-25 work warrants. | Normative |
| CC-SPEC-3 | Stable IDs; amend and retire in place. | Preserved in the repeated operational form. | Structural |
| CC-SPEC-4 | Five requirement forms; five falsifiability elements; four rejected oracle forms. | Preserved compactly, including invariant/prohibition denominators. | Structural |
| CC-SPEC-5 | Explicit non-goals and Unknown. | Preserved; adds durable rule-owned homes and human/machine link parity. | Normative |
| CC-SPEC-6 | Never select an unresolved shape decision; author cannot finally classify their own work. | Preserved with a revision-bound question population and explicit results. | Clarifying |
| CC-SPEC-7 | Implementation detail only when behavior requires it. | Preserved with a reproducible removal test. | Clarifying |
| CC-SPEC-8 | Applicable observable consequences map to requirements or contract-owned reviewed N/A. | Preserved and completed with exact manifest/path selection, index-bound clause offsets, byte-total module/line spans including preamble, deterministic rows, local N/A verification, Unknown homes, and denominators. | Normative |
| CC-SPEC-9 | Fresh-reader review under VIS-3/CC-REV-4. | Preserved; states exact evidence, results, and missing-review behavior. | Clarifying |
| CC-SPEC-10 | Exact-digest lawful adoption under VIS-4. | Preserved; adds one purpose-bound owner-Decision selection algorithm, consumer-specific durable selection homes, durable banner semantics, and current-state reporting. | Normative |
| CC-SPEC-11 | Coverage table over capability obligations, three result sets, non-author confirmation. | Preserved and completed for both units with deterministic extraction, occurrence-preserving deduplication, retirement, non-circular mappings, unaffected-baseline evidence outside the focused population, and determinate acceptance. | Normative |
| CC-IMPACT-1 | Generated six-field specification union; one capability; empty differs from absent. | Preserved with explicit expected/actual comparison evidence. | Clarifying |
| CC-IMPACT-2 | Shape changes sweep the same six classes; vocabulary consumption also triggers. | Preserved; separates provenance from work permission and makes the undefined vocabulary relationship revision-bound and fail-closed. | Normative |
| CC-IMPACT-3 | Sweep reports population, affected, unaffected, undecidable, reason, and method. | Preserved and completed with exact accepted corpus, retired entries, expected/actual rows, projection-defect validation separate from authoritative contradiction, exhaustive partitions, and deterministic parent propagation. | Normative |
| CC-IMPACT-4 | Undecidable renders Unknown or contradiction, never unaffected. | Preserved; gives every early/late result a home, routes projection defects through regeneration, blocks merge, and reserves contradiction exit for a purpose-eligible owner adjudication Decision plus a new sweep. | Normative |
| CC-IMPACT-5 | Named amendment/sweep actors and a confirmer other than the author. | Preserved with explicit evidence and result handling. | Clarifying |
| CC-IMPACT-6 | Shape and required spec amendments land together; no side-policy exception. | Preserved; defines one merge transaction, blocks invalid generated declarations, and records that the declined exception supplies no authority. | Clarifying |
| CC-IMPACT-7 | Blind run against the named immutable fixture, known answer, fresh administrator, dispositions, and no reliance before pass. | Preserved; adds exact answer-key digest and a distinct grader after result freeze. | Normative |

Additional carriers:

| Carrier | Disposition | Class |
|---|---|---|
| Both authority banners | Replace time-bound candidate prose with exact-digest, Decision-selected language true before and after approval. | Normative |
| Inline amendment chronology and finding codes | Remove from active rules; preserve in this record, predecessor bytes, prior deltas, and raw reviews. | Structural |
| Historical blind-exercise claim | Keep the immutable fixture and proof requirement in CC-IMPACT-7; keep historical verdict provenance here without turning it into a current claim. | Clarifying |

## Terms introduced, retained, and retired from active use

| Term | Movement and owner |
|---|---|
| acceptance unit | Introduced as a policy-local term owned by CC-SPEC-1; exactly whole-capability or focused-change. |
| whole-capability acceptance | Introduced and owned by CC-SPEC-1; CC-SPEC-11 supplies its population. |
| focused-change acceptance | Introduced and owned by CC-SPEC-1; CC-SPEC-11 supplies its baseline/difference population. |
| requirement provenance | Introduced as the plain name for CC-SPEC-2's existing six fields; CC-IMPACT cites that owner. It does not mean work permission. |
| material governing authority | Introduced as CC-SPEC-2's local removal test, not a new authority class. |
| coverage population | Retained from CC-SPEC-11 and defined once in the acceptance policy's shared terms. |
| reviewed N/A | Retained; the contracts own the owner gate, while CC-SPEC-8 states only its local verification consequence. |
| work warrant and `motivates` | Retained from doctrine and RFC1-25; no new record class is minted. |
| governing warrant / warrant set for provenance | Retired from active policy prose because it conflated provenance with work authority; historical uses remain untouched. |
| `CC-TEST-4 pattern` shorthand | Retired from active policy prose; the two non-author confirmation obligations are stated directly. |
| `consumes its vocabulary` | Neither introduced nor defined. It remains an explicitly undefined external relationship and therefore routes dependent cases to undecidable/Unknown. |

These policy-local terms do not add a value to a closed enum and require no
term-registry row for this proposal. Reusing one as project-wide closed
vocabulary would require a separately authorized registry amendment; this
three-file change does not perform one.

## Findings answered by the compact rewrite

The final semantic review at
`0edc9a86aaea1aad658e03300a90acbe3e375ac4` left four inline threads:

| Finding | Compact-rewrite disposition |
|---|---|
| [Missing generated-union rows](https://github.com/Tzeusy/syzygy/pull/5#discussion_r3877044182) | CC-IMPACT-3 creates rows over the union of expected and actual identities plus an absent-field sentinel. Empty actual fields retain missing expected identities; mismatch makes CC-IMPACT-1 Not satisfied and blocks merge, while impact derives from authoritative expected identities rather than falsely minting a doctrine contradiction. |
| [Stale three-set owner summary](https://github.com/Tzeusy/syzygy/pull/5#discussion_r3877044409) | The impact policy and this obligation map state the same four results and precedence for requirements, reconciliation rows, and specifications. |
| [Unrecorded acceptance vocabulary](https://github.com/Tzeusy/syzygy/pull/5#discussion_r3877044676) | The term table identifies each introduced term, its owning rule, and why no closed-registry admission occurs in this proposal. |
| [False overall-class summary](https://github.com/Tzeusy/syzygy/pull/5#discussion_r3877045654) | The overall class is Normative; every row uses exactly one canonical class and the account makes no false lower-class remainder claim. |

The independent fresh-reader review at the same head left seven material
findings without inline-comment authority:

| Finding | Compact-rewrite disposition |
|---|---|
| Ambiguous policy-act selection | CC-SPEC-10 selects eligible Decisions by stated purpose, act type, subject, digest, scope, and explicit supersession/revocation only. |
| Incomplete Markdown unit accounting | CC-SPEC-8 uses checked clause-definition offsets, partitions every module byte into physical line spans first, records preamble/no-clause bytes, and makes any marker, grouping, overlap, or gap uncertainty Unknown. |
| Undefined installed-path correspondence | CC-SPEC-8 states the literal correspondence: prefix each manifest `rfcs/...` path with `.syzygy/governance/contracts/`. |
| Deduplication conflicts with relationship evidence | CC-SPEC-11 preserves every source occurrence and groups only an identical revision/locator/span/outcome tuple; stable IDs link but never erase evidence. |
| Missing direct rows | CC-IMPACT-3 reconciles the union of expected and actual identities and emits missing/extra discrepancies before parent derivation; mismatch fails CC-IMPACT-1 without pretending a generated projection is authority. |
| Adjudication used an incompatible acceptance-record selector | CC-SPEC-10 is purpose-bound and generic across eligible owner Decisions; CC-IMPACT-4 calls it with purpose `adjudicate`, not `adopt`. |
| Unbound external-policy claim | The impact rules no longer claim that an external candidate clause applies regardless of force. Their denominator and Unknown rules stand locally on VIS-2 and the named accepted sources. |

## First compact-review dispositions

At exact head `413ce020587ec8638ba16dc25ca099e55b3e30d3`, the independent semantic
review returned **`VERDICT: REVISE`** and the blind reader returned
**`FRESH-READER REVISE`**. Their overlapping findings are dispositioned once:

| Finding | Correction |
|---|---|
| CC-SPEC-8 lacked total module accounting and parsing precedence. | The line-first population now covers every byte before Markdown interpretation, uses checked index offsets, retains preamble/no-clause spans, and routes any marker/grouping uncertainty to Unknown. |
| Decision-selection contradictions all pointed to a specification-adoption home. | CC-SPEC-10 now requires a purpose-specific `decision-selection` section in each consumer: CC-SPEC-8, CC-SPEC-11, CC-IMPACT-3, CC-IMPACT-4, or the policy authority-state projection. |
| CC-IMPACT-7 omitted answer-key identity and the grading actor. | It now names and hashes the answer key, freezes the blind administrator's result, and assigns a different CC-IMPACT-5 confirmer to verify inputs and grade. |
| Focused acceptance did not dispose unaffected baseline requirements. | Unaffected rows remain in the complete sweep denominator but explicitly stay outside the focused acceptance population; affected and undecidable rows enter it. |
| Generated-union mismatch was falsely called a doctrine contradiction. | The row records match/missing/extra; mismatch makes CC-IMPACT-1 Not satisfied and blocks merge. Impact derives from the authoritative expected identity; only two authoritative claims can be contradicted. |
| RD-70's verdict lost its prefix. | The verbatim table below now records `VERDICT: CONFIRM WITH EXCEPTIONS`. |

This is the single bounded compact-rewrite correction cycle authorized after
the two reviews. It changes no authority source and requires entirely new
semantic and fresh-reader review of the corrected exact bytes.

## What explicitly does not change

- No owner decision is made for P-43.
- The declined lagging-specification exception is not revived or re-offered.
- No accepted contract, doctrine, topology, term registry, act record, install
  record, historical review, raw output, or prior semantic delta is edited.
- No RFC-0010/RFC-0011, Mission, context-selection, future capability,
  deployment, or external-project work is authored, planned, backlogged, or
  implemented.
- The six CC-SPEC-2 provenance fields remain closed and unchanged.
- RFC1-25's work-warrant classes, VIS-4's gates, the contract-owned reviewed-N/A
  gate, CC-REV-2's same-logical-change rule, and the blind fixture/answer bytes
  are not changed.
- No policy ID is added, retired, reused, or renumbered.
- This proposal is not merge, adoption, implementation, or approval-record
  authority.

## Warrant and evidence basis

The owner selected the compact-rewrite option on 2026-08-28 after repeated
new-context reviews found structural readability debt. That authorizes drafting
and independent review of these three files only.

The governing basis is VIS-2 (missing evidence is Unknown), VIS-3
(fresh-reader review), VIS-4 (owner adoption), SDR-37 (one coherent capability
or coherent change), RFC1-25 (work warrants and owner adjudication), RFC3-15 and
RFC3-16 (Decision homes, exact-digest acts, provenance and supersession), the
five accepted OpenSpec-seam clauses cited by CC-SPEC-8, and CC-REV-1/2/3/4/6/7.

## Downstream sweep and retained evidence

The final evidence pass uses two independent methods over the same population:

1. `git ls-files --cached --others --exclude-standard` supplies the path list;
   Python decodes every file, searches literals and regex predicates, and
   prints every matching path and remainder.
2. `rg -l -F` or `rg -l` runs over that exact path list; sorted path sets must
   equal the Python sets, not merely have the same count.

`[Observed]` The compact-rewrite working population was 659 files: 659 decoded
as text and zero were undecodable. Python and `rg` returned identical sorted
path sets for every downstream literal:

| Reference | Files / 659 | Reference | Files / 659 |
|---|---:|---|---:|
| CC-SPEC-1 | 54 | CC-IMPACT-1 | 38 |
| CC-SPEC-2 | 21 | CC-IMPACT-2 | 13 |
| CC-SPEC-5 | 8 | CC-IMPACT-3 | 11 |
| CC-SPEC-8 | 26 | CC-IMPACT-4 | 6 |
| CC-SPEC-10 | 22 | CC-IMPACT-5 | 5 |
| CC-SPEC-11 | 19 | CC-IMPACT-6 | 13 |
| CC-SPEC subject filename | 37 | CC-IMPACT-7 | 18 |
| CC-IMPACT subject filename | 25 | | |

`[Observed]` Python heading extraction and anchored `rg` independently found
exactly CC-SPEC-1…11 once and CC-IMPACT-1…7 once. Literal counting by Python
and `rg -o -F` independently found 18 occurrences of every rule-format label:
`Purpose`, `Inputs/population`, `Decision`, `Possible results`, `Missing
evidence`, `Retained evidence`, and `Sources`. A Python table parser and an
independent `awk` projection found all 18 stable-ID delta rows using one
canonical class: ten Normative, six Clarifying, two Structural, and zero
Editorial; all three carrier rows also use one canonical class.

`[Observed]` `wc -w` and Python whitespace splitting agreed on 2,200 words for
CC-SPEC and 1,482 for CC-IMPACT. Python literal counting and `rg -o -F` also
agreed that the two active policies contain zero occurrences of each retired or
time-bound phrase: `CC-TEST-4`, `warrant set`, `work-warrant record`, `Nothing
in it binds today`, `no script today`, `current doctrine state`, `neither
exists`, `Amended 2026`, `Reviewed 2026`, `CC-KNOW-16`, `RD-`, `P-43`, and
`P-44`. The deliberately unresolved phrase `consumes its vocabulary` occurs
once, in its fail-closed rule. The active policies contain the expected single
`line-first partition`, `generated-missing`, and `one merge transaction`
definitions, plus the exact answer-key path once.

`[Observed]` `git diff --check` emitted nothing. The working-tree status and an
independent `git diff --name-only` projection both enumerated exactly the two
policy subjects and this record as modified tracked files; no untracked or
fourth path existed. Final exact-head review must rerun these same commands
after commit because the commit SHA, not this authoring state, is the review
subject.

`[Observed]` The CC-SPEC-8 accepted-manifest procedure was exercised by two
methods. A Python byte/hash method found 39 candidate rows, 19 Wave A rows, 11
Wave B rows, a disjoint selected union of 30, nine excluded rows, and zero
installed-path or digest mismatches. An independent `awk`/`comm` count produced
39/19/11 and nine excluded rows, while `sha256sum -c` reported all 30 selected
installed files OK. These are evidence for this proposal, not timeless counts
inside the policy.

Stable IDs preserve citation targets. Digest identity is deliberately changed:
performed acts name predecessor bytes, not these proposals. No downstream
authority or historical file is edited in anticipation of an act.

## Prior verdicts, copied exactly

| Reviewed subject/head | Verbatim verdict fields retained |
|---|---|
| Original accepted-policy review chain | `VERDICT: REVISE`; `VERDICT: REVISE`; `VERDICT: CONFIRM WITH EXCEPTIONS` |
| PR head `31422229bbdf646f53a3f81fb33b331bce40b9b3` | `Verbatim-Verdict: VERDICT: REVISE`; `Status: corrections-required` |
| PR head `e44b5bc673121d74a44052199d39e37cc148e213` | `VERDICT: REVISE`; `FRESH-READER REVISE` |
| PR head `b0fefad232f07dab6bfce6998d90e3660250b42f` | `VERDICT: REVISE`; `FRESH-READER REVISE` |
| PR head `5f4e6a9cf7fbbe4c12db84dfe63bb36a569e120d` | `VERDICT: REVISE`; `FRESH-READER REVISE` |
| PR head `cddcd2dc9790e0afeba419b090c4333b0fe90113` | `VERDICT: REVISE`; `FRESH-READER REVISE` |
| PR head `0edc9a86aaea1aad658e03300a90acbe3e375ac4` | `VERDICT: REVISE`; `FRESH-READER REVISE` |
| PR head `413ce020587ec8638ba16dc25ca099e55b3e30d3` | `VERDICT: REVISE`; `FRESH-READER REVISE` |

The first row is RD-51, RD-69, then RD-70. Complete raw reports for the later
off-thread reviews are not stored in a clone-resolvable home; the canonical
review Bead retains summaries. This evidence-home limit is not relabelled as a
pass. Earlier thread-by-thread history remains in the superseded branch version
of this record and in PR #5.

## Expected pre-act verification ledger

Before an owner act names the proposal digests, only failures satisfying all of
these conditions are expected:

- the predicate compares one of the two edited policies with a predecessor act
  digest or registered act-bound copy;
- the observed subject digest is the exact proposal digest;
- the failure returns to pass only through a new owner act over reviewed bytes,
  never by weakening a check or editing history.

`[Observed]` The final working-tree governance run examined 659 tracked files,
reported 31 OK, 18 WARN, and exactly two FAIL families:

| Family | Denominator | Findings | Expected reason |
|---|---:|---:|---|
| CG-7d | 18 digest quotations | 7 | Four CC-SPEC and three CC-IMPACT predecessor quotations no longer match the edited subjects. |
| CG-7e | 7 registered copy files | 7 | The same registered records still contain predecessor arguments, not proposal digests. |

The seven CG-7e findings are both subjects in
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`, both in
`ACCEPTANCE-ACT-RECORD.md`, CC-SPEC in
`SPECIFICATION-ACCEPTANCE-DECISION.md`, and both in the craft
`INSTALL-RECORD.md`. Those are authority or historical records this proposal
must not edit. No other check family reported FAIL. The clean-clone run must
reproduce this ledger at the exact commit. Any other FAIL—including link,
vocabulary, format, self-test, population, or battery failure—is a proposal
defect.

## Rollback and supersession

Before approval, rollback is closing the draft PR and abandoning this branch;
mainline and authority records remain unchanged. If the owner later approves
the exact reviewed bytes, a separately authorized transaction recomputes both
digests, appends the owning act/install records under their ceremony, and
explicitly supersedes the predecessor digests. That transaction is outside
this Bead. Editing a reviewed or acted-on policy retires the corresponding
review or act for the edited bytes.

## Compact-rewrite review contract

1. Freeze exactly the two policies and this record at one commit; record their
   SHA-256 values and the commit SHA.
2. A new-context semantic reviewer receives the three files, the 15-item Bead
   acceptance contract, and only the doctrine/contracts/policies cited by the
   rules. They reproduce the full-file mapping, classes, terms, non-goals,
   populations, failure paths, and expected-red ledger.
3. A different new-context fresh reader receives the two policies and their
   governing sources, but no finding codes, repair chronology, authoring
   discussion, or desired verdict. They must accurately restate both acceptance
   units; six-field provenance/work separation; deterministic CC-SPEC-8 and
   CC-SPEC-11 populations; retirement and Unknown behavior; reviewed-N/A
   decision; exact act selection; fixed impact corpus; expected/actual direct
   rows; four-set precedence and propagation; adjudication; actors; atomic
   landing; unresolved vocabulary behavior; and proof-before-reliance.
4. Both reviewers record raw output, independence, exact head/digests, and
   verdict words verbatim. Every material finding is fixed or explicitly
   overruled by the owner with rationale. Any semantic edit invalidates both
   reviews and requires new-context review of the new bytes.
5. Verification uses two methods for every universal, absence, population,
   path, and digest claim; checks both word ceilings; runs governance self-test
   and the canonical battery in a clean clone; checks hosted exact-head state;
   confirms the PR remains open and draft; and resolves every material thread.
6. Passing review is readiness to ask the owner, not adoption or merge authority.
   The policies remain non-binding until a performed owner act names the exact
   final digests.
