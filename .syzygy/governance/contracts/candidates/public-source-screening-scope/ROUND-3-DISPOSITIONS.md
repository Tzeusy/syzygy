# Round 3 dispositions — public-source screening scope

> **Candidate — binds nothing.** Dispositions of
> `reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-3-RAW.md` (verdict REVISE; findings
> 1 and 2 revise, 3 to 7 notes), written 2026-10-03. The raw is retained
> verbatim. Its head names the reviewed commit and the manifest digest of the
> bytes it reviewed; this repair changes the patch, so those bytes are retired
> (rule 10) and a round-4 review is needed. No digest is copied here.

| # | Finding | Disposition |
|---|---|---|
| 1 | The constant reader accepted commented-out and string-embedded declarations and members | Repaired. `mask_source` blanks comments and replaces string bodies before any match; the reader requires exactly one live declaration, exported, and refuses a second or an unterminated comment or string. Fixtures: a commented-out declaration, a block-commented one, a string-embedded one, a commented member, a commented old declaration before the live one, a second live declaration, an unterminated comment. Rule-6 mutants: the selftest runs the reader with comment masking off and with double-quote masking off and requires the dependent fixtures to fail. Selftest 54 of 54. |
| 2 | `reasonRule` said the set "cannot differ from what the generator emits" | Repaired in the patch: it now says the set cannot differ from the values the constant declares. The manifest digest changed with the patch. |
| 3 | Q7 understated what the base emits | Repaired in packet Q7: names `body-not-retained-for-generation` from the app's source adapter and the PWB classifier's pass-through of `unknownReason` as a free string, and says the constant must cover reasons that originate outside generation-source.ts and the code must map the pass-through onto listed values. Request to the generator's lane, not a change to the bytes' operative rule. |
| 4 | The reader's export pre-check was redundant, its mutation survived | Repaired: the declaration check now has three distinct refusals ("not declared", "declared more than once", "not exported") and each has its own fixture asserting the message. |
| 5 | Ledger record count and status-page row | Repaired. The ledger now states the figure (61 at the repaired commit, six of them this package's own files, 55 others), the predicate beside it, and that each retained raw adds one. The status-page row names the re-pin builder's `--check` line (no digest literal, fails with the tree) beside the recorder's. The earlier figure 59 had been measured before the round-2 raw was retained; the next figure moves again when a raw is retained. |
| 6 | "One per population" counted three rules for four populations | Repaired in the semantic delta: three rules for four populations; the envelope-control labels are produced by the two instruction-text symbols. |
| 7 | "A path of an excluded source is not carried" rested on an unconstrained `sourceId` | Repaired in the rule: an excluded source's `sourceId` is an opaque identifier not derived from its path or body, labelled [Inferred] as enforced only by the reader implementation the generator's lane is asked to write that way. Added to the delta row. |

## Self-found

None beyond the reviewer's findings. The record count was found independently
before the raw arrived (the 60th file was the round-2 raw, retained after the
sweep was last run); the reviewer reached 60 as well.
