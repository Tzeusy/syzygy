# Source-of-truth seams — closure report

> **Non-authoritative round record.** The raw review is
> `reviews/RD-6-source-of-truth-RAW.md` and is never edited. Where this file
> and the raw review disagree about what the reviewer found, **the raw review
> wins**. Verdict words are copied, not summarised.

## The commission and the verdict

A reviewer with no authoring context was asked whether the project's central
claim survives its own corpus: **one owning artifact per assertion;
presentation, projections and personal state never become truth.**

**`VERDICT: REVISE`.** Nineteen findings.

**What holds, recorded first, in the reviewer's own assessment:**

> The project's central claim … holds in most of the corpus, and in two places
> it holds better than I expected.

And the diagnosis, which is the most useful sentence in the review:

> None of this is dishonesty and none is fabrication; every artifact I checked
> said true things about itself. **The failures are all of one shape: a rule
> migrated into the thing that enforces it, and then the enforcement became the
> only copy.**

**Method note the reviewer disclosed and this file repeats:** the working tree
was **dirty and changing during the review** — a parallel session was editing
the term registry, the nine fixtures and the checker. Every mutation test was
run in a pristine `git archive HEAD` extraction, never in the repository.

## H-1 · Seven act digests were examined by no check — **closed**

The finding that carried the verdict, and it was **mutation-proven**:

> I falsified all four act arguments in the artifact `AGENTS.md` names as *the
> owner-facing offering*, plus three in the round-2026-08c closure preflight,
> and the full battery reported `0 findings` and exited `0`.

CG-7a…7d checked the acceptance record's own copies. **Seven further copies of
current act arguments lived in three other tracked files and nothing looked at
them** — including the file the repository's own operating procedure sends the
owner to.

**Closed by CG-7e**, `cg7e_act_digest_copies()`, with a decidable per-file act
registry and two predicates:

1. a **registered** file declaring an act must carry that act's **current**
   argument;
2. an **unregistered** file carrying a current act digest **fails** — so a new
   copy cannot appear silently.

Files bannered `SUPERSEDED` or `Historical` are skipped; CG-15b owns those.
**Mutation-tested per verification rule 6**, and it reports `5 files examined,
0 findings` today.

**What this finding also bought, and it is worth more than the check:** it
surfaced that **act 2's argument in the owner-facing offering was the retired
one**. Corrected in the offering, in the public-clone verification report, and
in the closure preflight. **A defect an owner could have acted on** — found
only because a reviewer mutated the inputs instead of reading the outputs.

**RD-6's own proposed repair was tried and reverted.** Widening CG-15's
`TRUNC_DIGEST` pattern produced **47 findings, none of them defects**. The
pattern stays at `{8,63}` with its required marker, and a comment in the
checker records that the widening was attempted and why it was not kept.

## A-1 / E-1 · `constrains` is authorized by no clause — **partly closed, and the open part is the finding**

> Three of the 32 modules the owner would sign carry `constrains: [...]`. The
> one contract clause that enumerates the selection relations (RFC11-4) does
> not include it, and still names a key (`provides_to`) that was deleted from
> every module.

**Both halves verified independently.**

**Closed:** the count is now **two** modules, not three — review RD-4 found both
originally-declared edges wrong in direction and both real ones undeclared, and
the corrected declarations sit on the two modules whose clauses state the
restriction. The relation is projected into `05-CONTRACT-INDEX.yaml`, the
anchor is checked, and `CONTRACT-DEPENDENCY-INDEX.md` now says on its own face:

> Until that clause changes, a conformant compiler would not read this relation
> at all.

**Open, and RD-6 is right that the repair does not reach it:** *"neither touches
the clause text, so this one stands."* **RFC11-4 still does not name
`constrains`, and still names `provides_to`, which no module declares.** Both
are normative edits to act 1's digest subject. **Owner item P-21(c).**

**E-1 is closed:** the relation model's decision record now exists at
`RELATION-MODEL-DECISION.md`, and the dependency index no longer states
selector obligations no clause carries (RD-4 F-15).

## F-1 · Five thresholds printed as charter figures cite charter sections that do not exist — **open**

The checker enforces five thresholds and prints them every run, attributed to
charter sections with no referent. **This is the review's own diagnosis in its
purest form**: the rule migrated into the enforcement, and the enforcement
became the only copy — while still crediting an authority that cannot be
consulted.

**Not repaired**, and the reason is that repairing it requires deciding *where
each threshold's real home is*, which is a policy question. Four of the five
are budget or ceiling figures whose home is the uninstalled `CC-BUDGET-*`
family — **owner packet 7**. Recorded rather than silently re-attributed;
re-attributing a threshold to a plausible home would be the same defect wearing
a correction.

## The remaining findings

| # | Finding | Disposition |
|---|---|---|
| **F-2** | A justification hard-coded in the verifier, attributed to a report that does not contain it | **Open.** Same class as F-1 |
| **F-3** | Rules with a second copy inside the enforcement, enumerated | **Open.** The enumeration is the value; the repair is per-rule and each needs a home |
| **F-4** | CG-9's name overclaims what it can test | **Open.** A check whose name promises more than its predicate delivers is how a reader over-trusts a green line. Cheap to fix, and it changes a check identifier, which CC-REV-7 makes non-trivial |
| **A-2** | The budget figures exist in four places | **Closed.** `CONTEXT-BUDGET-REPORT.md` is the single home; CG-20 and CG-21 are inverted to *prohibit* measurement in the load map and contract prose, with the module count as denominator. Review RD-5 then found the report still transcribing figures out of fixture prose — closed at the generator, which now redacts and prints what it redacted |
| **A-3** | Approximate in the source, exact in the derivation | **Open.** A `≈` that loses its qualifier downstream is a precision claim nobody made |
| **E-2** | Facts existing only in `CONTEXT-BUDGET-REPORT.md` | **Accepted by design, and stated.** That file is *supposed* to be the only home for a measurement. What E-2 correctly identifies is that a generated file being the sole home makes its generator load-bearing — hence the selftest, and hence `--check` in the battery |
| **E-3** | `05-CONTRACT-INDEX.yaml` carries no candidate marker and asserts a `status_source` field it does not project | **Open.** A generated projection with no candidate banner is one careless citation away from being read as accepted |
| **E-4** | `ACTIVE-CONTRACT-MANIFEST.txt` has no generator | **Open, and it is the sharpest of the remaining.** The manifest is **act 1's digest argument**, and it is maintained by hand. Every other digest in this repository is scripted (verification rule 3). Writing a generator for it now would move the digest the owner is being offered, so it is routed to the pass after the acts — and named here so the exception is visible rather than assumed |
| **C-2** | Eleven candidate-lane artifacts carry no candidate or non-authority marker | **Open.** Enumerated by the reviewer; each is a one-line banner and eleven files' worth of digest movement |
| **C-3** | The term registry claims mechanical enforcement from a check that does not do it | **Closed.** CG-23 now derives the core set from the registry's own table rather than a hard-coded tuple, matches at word boundaries with an enumerated printed allowlist, and the registry describes it accurately — including that it is **report-only** because the core set is candidate |
| **D-2** | The default check scope depends on the founder's working tree | **Open.** The failure mode this repository keeps re-acquiring, and the reason the battery is run in a clone |
| **D-3** | Machine-local state in a tracked generated artifact | **Open** |
| **D-4** | A verifier's clause-count baseline is sourced to a git-excluded artifact | **Open.** A baseline a clone cannot read is a baseline a clone cannot check |
| **G-1** | P-22 is real, correctly recorded, and one leg of it is a plain citation error nobody has named | **Recorded** in owner packet 2 |
| **G-2** | Sweep for other authority-bearing registries in presentation or personal state | **Closed as a sweep** — one instance, no others. The instance is P-22 |

## What closed, what did not, and the honest shape of it

**Closed: 5 of 19.** H-1 (with a check and a real defect found), A-2 (twice —
once at the report, once at the generator), C-3, E-1, G-2.

**Open: 14.** Of those, **F-1 through F-4 and A-3 are one family** — a rule
that lives only inside its own enforcement, or an authority citation that does
not resolve. RD-6's diagnosis names it precisely, and the family is not closable
by editing checks: each member needs a decision about where its rule belongs,
and four of them wait on the uninstalled `CC-BUDGET-*` family (**packet 7**).

**E-4 is the one an owner should see before act 1.** The manifest that *is* act
1's digest argument has no generator, in a repository whose third verification
rule reads *digests are scripted, never transcribed*. Nothing suggests it is
wrong today — CG-7a recomputes all 32 entries and reports 0 findings. But it is
the one place where the rule the repository enforces everywhere is not enforced
on the artifact that matters most, and the reason it is not repaired here is
that repairing it would move the digest being offered.

**None of the fourteen is hidden behind a waiver, and none blocks an act.**
Each is a candidate-lane defect an act would bind knowingly, and the acceptance
packet states them before the act phrases.
