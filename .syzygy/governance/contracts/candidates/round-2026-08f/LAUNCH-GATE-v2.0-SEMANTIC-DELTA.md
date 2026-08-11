# Launch-gate v1.18 → v2.0 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority. This delta records every change of meaning so
> "no question was weakened" stays a reviewable claim. Owner approval of
> v2.0 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34).
> The offer waits on two fresh-context reviews (§14 of the owner charter:
> policy-semantics and structured-record), because the session that
> authored these bytes may not confirm them.

**Baseline.** v1.18 at commit `4aa221b` — instrument sha256
`616364a579115d7ab948e5c3799a95eae21262ccfe1eebedf29b9cc136ae6561`,
Markdown validator `scripts/launch_gate_results.py` sha256
`278ee1ea14fb3c87f69668ac77410f24a890a725f9285a35b53e432030aafe7a`
(329 fixtures, 0 failing). The last review bound to the instrument is
**RD-45**, on v1.17, `VERDICT: REVISE`. **No review is bound to v1.18**: its
re-review (RD-46) was composed and never dispatched.

**Subject.** v2.0 — instrument sha256
`05ecaa954e81ef95f6e2e2b409fbcb5bd5391037c10d9624ab4af3217a00f6d2`;
schema `launch-gate-administration.schema.json` sha256
`e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb`;
`scripts/validate_launch_administration.py` sha256
`dd41d134dbff20e06d7830f669f1cc62a04134082f6c653c1618d649068d2409`;
`scripts/render_launch_administration.py` sha256
`d1d4928cf729a07338788962c8266ff241e8ec87387eaab1482a59bb47c27041`.
Digests are of the working-tree bytes at authoring time and are recomputed
at the commit that carries them; the packet, not this line, is what a
reviewer binds.

---

## Why this is v2.0 and not v1.19

The owner's charter closed the loop this instrument had been running:

> Do not write v1.19 as another Markdown-carrier repair. … Do not dispatch
> another review whose main purpose is finding one more Markdown quotation,
> HTML, list, fence, table, or rendering carrier.

The record it closed is worth stating plainly, because it is the argument
for the change. Thirteen consecutive administrations of the instrument —
**RD-33 through RD-45 — every one `REVISE`**. The last five converged on a
single question:

> *Is this line the record's own claim, or a quotation of one?*

RD-41 answered it with state. RD-42 with state for Markdown's containers and
enumeration for HTML's. RD-43: the region does not begin or end where a
reader sees it. RD-44: a region begins at a line, not at a `<`. RD-45: the
rule was fixed and **the set it ranges over was never measured** — four
element names still carried a `READY FOR` beneath a visible `NOT READY` at
zero errors.

Each repair was correct. The class did not close, because the question is
not answerable by rule: it is a property of a document format asked to be
two things at once. §5 of v1.18 defined one Markdown file that was
simultaneously a human report and the machine-validated source of a launch
decision. v2.0 does not answer the question a fourteenth time. **It deletes
the question.**

---

## D-1 — the administration record stops being Markdown *(§5, replaced)*

**Was:** one Markdown file per administration, in a template §5 defined,
parsed by `launch_gate_results.py` for its verdict, its counts, its declared
fields and its roster.

**Is:** two files, and only one of them is a fact.

```text
<record>.json    canonical source — validated, the only authority
<record>.md      generated presentation — never parsed, never cited
```

The source conforms to `launch-gate-administration.schema.json`, committed
beside the instrument. The report is produced by
`render_launch_administration.py` and opens with the literal words
`Generated presentation. / Canonical source: <record>.json / Do not edit
this file.`

**Change of meaning:** an administration fact now has exactly one home, and
it is typed. Nothing in the correctness path reads Markdown, HTML, CSS
visibility, or a rendering. The v1.13–v1.18 carrier machinery — the DOM
model, the hiding-element population, the container stack — has no successor
in this path; it is not ported, and it is not needed.

## D-2 — three artifact classes become four *(preamble)*

The preamble's `Launch-gate definition / Administration record / Owner
launch decision` becomes `Launch-gate policy / Administration source record
/ Administration report / Owner launch decision`. The third was doing two
jobs under one name, which is the whole defect in one line.

## D-3 — the record can no longer claim a verdict

**Was:** the record's terminal `GATE VERDICT:` line carried the verdict; the
validator recomputed and compared. Every false-READY finding of the last
five rounds was a way of getting a *claimed* verdict past that comparison.

**Is:** there is no `final_verdict` field to author. The schema's
`additionalProperties: false` **rejects** one rather than comparing it, and
`validate_launch_administration.py` computes the verdict from the rows by
§4's formula. The charter offered comparison or omission; omission is taken,
because a record that cannot state a conclusion cannot be believed about
one.

## D-4 — absence is an error, and counts are lengths *(VIS-2, structurally)*

**Was:** §5's declared fields were required by prose and checked by LG-5 and
LG-12, each check paid for by an incident in which a deleted template line
read as answered, or an empty field borrowed the next line's text.
`Deferred count:` and `Reopened count:` were **declared** figures the
validator parsed, required precisely so their absence could error instead of
reading zero.

**Is:** every field is required by the schema; a missing one fails
validation with no charitable reading available. `Deferred` and `Reopened`
are the **lengths of required arrays** — an absent array is an error, an
empty array is an explicit assertion of zero, and there is no third state.

**This is a strengthening, and it is named as one:** the old rule needed a
declared count *because* a Markdown record could omit a line silently. The
new shape gets the same guarantee from the type system and additionally
makes the count uncountable-by-mistake, since it is derived from the very
entries it counts.

## D-5 — scope cannot be laundered by wording *(new)*

Each row carries `verdict` **and** `launch_scope` as independent typed
fields that the validator requires to agree: `deferred-wave-only` is lawful
with `Not met (out of launch scope)` and with no other verdict. Rendering a
defect out of launch scope now takes two deliberate acts rather than one
soft phrase. LG-9's disclosure rule is carried and tightened: a scoped row
requires a `deferred_wave_findings` entry **naming that question**, and a
finding that meets any of §4's five blocking conditions cannot support a
scoped verdict at all.

## D-6 — §2 says which artifact is the record

Added to the administration-integrity list: the record *is* the JSON; a
reviewer who submits only prose has submitted no record; an edited report is
detectable by `render_launch_administration.py --check` rather than assumed
absent. §2's verdict-vocabulary rule now notes that the vocabulary is a
closed enumeration in the schema, so a softened verdict is a schema error
rather than a reading the next reader must catch.

## D-7 — the trend row is generated, and its comparability limit is stated

**Was:** §6's row was typed into `TREND-LOG.md` from the record.

**Is:** `validate_launch_administration.py --trend-row` prints it from the
source record; the New-findings column is computed against the record
`prior_record` names. Column semantics are unchanged (a scoped finding is a
finding; a deferral is a finding until resolved; a new scoped row is a new
finding).

Added, and it is a limitation rather than a feature: **trend comparability
across the v2.0 boundary is limited.** The questions and the formula are
unchanged, so verdicts remain comparable question by question; the *counts*
are comparable only insofar as the earlier records' parsed figures were
correct — which is exactly what thirteen `REVISE` verdicts put in doubt. A
trend line crossing the boundary must say so, by §6's own rule that a trend
across different questions is not a trend.

## D-8 — the schema joins the portable core *(§7)*

§7's generalization rule named the [U] questions and the §2/§4 protocol as
the invariant. The schema is added: it names no Syzygy artifact, and the
launch target, waves, and fixed cases it carries are values a parameter
block supplies.

## D-9 — obligations the old validator could not check, now checked

Each is a requirement §2/§3/§4 already stated in prose and no v1.x check
enforced:

| New | Requirement it enforces |
|---|---|
| `LA-6` per-row `falsification_attempt` | §2's "attempt to fail every question first" — a verdict that survived no attempt is not credible |
| `LA-9` concept→trace coverage | §3's E3 credibility protocol: an empty reopen list *without the trace table* is Unknown, not Met |
| `LA-10` case-text equality against §8 | §2's "a verdict rendered against a paraphrased question is void", applied to E4's fixed cases |
| `LA-10` silence recording | §3's "silence over a case the launch target needs routed is a finding in its own right" |
| `LA-11` vacuous-deferral guard | a deferral defers a *finding*; one claimed against a `Met` row would still convert a plain pass into `READY-WITH-DEFERRALS` |
| `LA-13` full-vs-delta and fresh context | §2's "the gate decision itself requires a full administration"; previously trusted |
| `LA-15` prior-record anchoring | §6's trend delta is meaningless against a record from a divergent history |
| `LA-16` pilot-recurrence check | §8's `PILOT_RECURRENCE_CHECK`, previously an instruction nothing could tell had been skipped |

Carried forward unchanged in substance from LG-1…LG-13: identity and digest
binding, launch-target verbatim binding, roster completeness *and closure*,
the closed vocabulary, evidence-for-`Met`, counterexample-for-`Not met`,
settlement-for-`Unknown`, E1's five sub-rows and its rollup, scoped-row
disclosure, the E3 reopen gate, deferral citation (a made decision — `P-n`
names the queue of decisions *not* made, `D-n` a delta item, `B-n` review
numbering, and none grants anything), and §4's formula over both pass
branches.

## D-10 — what happens to the Markdown chain

`scripts/launch_gate_results.py` **stays**, at 329 fixtures, and its scope
narrows to what it is now for: validating the historical Markdown records
written under v1.3–v1.18. The 2026-08-09 pilot and every subsequent Markdown
administration remain immutable evidence in the format their version
defined. **Nothing is migrated.** Migrating them would rewrite evidence, and
the one thing a superseded record must keep is its own bytes.

---

## What did **not** change — measured, not asserted

Sections of the instrument, digested before and after:

| Section | State | Bytes |
|---|---|---|
| Preamble | changed (D-2) | 2896 → 3678 |
| §1 Derivation tiers | **byte-identical** | 788 |
| §2 Administration protocol | changed (D-6) | 4350 → 4751 |
| §3 The question series | **byte-identical** | 15250 |
| §4 Verdict computation | **byte-identical** | 5642 |
| §5 Record format | replaced (D-1) | 3567 → 5984 |
| §6 Trend log | changed (D-7) | 2175 → 3199 |
| §7 Generalization path | changed (D-8) | 1024 → 1213 |
| §8 Parameter block | **byte-identical** | 6577 |
| §9 Changelog | appended | 75572 → 79579 |

Method: split both texts on `^## <n>\.` headings and sha256 each span; the
figures above are that run's output. **§3 byte-identical is the claim that
matters**: not one question's text moved, so "no question was weakened" is
not a judgment call about this amendment — there is no amended question to
judge. **§4 byte-identical** means the formula, both pass branches, the five
blocking conditions, the never-deferrable conjuncts and the closed
vocabulary are the v1.18 ones. **§8 byte-identical** means the
parameter-block digest is unchanged, so every binding a record makes to §8
is the binding v1.18 made.

## Fixtures and mutation-reverts

Generated by this run, not typed:

```text
validate_launch_administration.py --selftest   75 fixtures, 0 failing
render_launch_administration.py   --selftest   12 fixtures, 0 failing
launch_gate_results.py            --selftest  329 fixtures, 0 failing
```

**31 mutation-reverts, one per decision branch, 0 unwitnessed.** Each
reverts a single branch to the form that would pass a naive reading and runs
that tool's own selftest; a mutant killing zero fixtures means the branch is
decorative. Kill counts: m1 2, m2–m11 1 each, m12 3, m13–m22 1 each, m23 2,
m24 crashes the suite, m25–m31 1 each.

**Two defects the harness found in these very bytes**, recorded because the
alternative is a delta that reads as though the work were clean:

1. `LA-11`'s deferral-path check used `cite.lstrip("./")` to strip a leading
   `./`. `lstrip` takes a **character set**, so it ate the leading dot of
   every `.syzygy/…` path and turned each governed citation into a
   non-existent one. Caught by the `a directory grants nothing` fixture,
   which reported the wrong error. Fixed to a prefix strip, with the reason
   in the code; mutant **m13** now witnesses it.
2. The renderer's do-not-edit assertion was `DO_NOT_EDIT in out1` — a
   tautology satisfied by an empty constant, so the banner could have been
   deleted with every fixture passing. Caught by mutant **m30**, which
   killed nothing. The assertion now names the literal string.

Neither was found by reading. Both were found by mutating the apparatus
before believing its number.

## Disclosed limits, each measured, none generalized

- **The validator reads the instrument's own prose in exactly one place** —
  binding E4's fixed cases from §8. It is bounded (it stops at the first
  non-consecutive case number) and fail-closed (no cases parsed is an error;
  a count or text mismatch is an error). It is disclosed here rather than
  claimed absent, because "nothing parses Markdown" would be false. It is
  categorically unlike the thing v2.0 removes: the bytes read are pinned by
  a digest the record binds *before* the read, and every disagreement is an
  error rather than a reading.
- **The schema interpreter is a documented subset**, not the reference
  implementation. Its safety property is that it **rejects any keyword it
  does not implement**, so the schema can never quietly rely on an ignored
  one (mutant m25 witnesses this). Where `jsonschema` is installed the
  selftest cross-checks the base record against it as a second method; that
  cross-check never gates anything, because hosted CI installs no packages
  and a check that cannot run everywhere cannot be a requirement.
- **Presence tests on free-text fields are content-blind by design.** They
  are guarded only against a placeholder lexicon ("none", "n/a", "tbd"); the
  truthfulness of an evidence quote stays with the reader. A reviewer who
  writes a plausible false quote defeats this tool, and no version of it has
  ever claimed otherwise.
- **`launch_scope` agreement is a consistency check, not a scope oracle.** A
  reviewer who sets both fields to the scoped form for an in-scope defect
  passes; what the check removes is the *single*-typo path.
- **No administration has been performed under v2.0.** The verdict path is
  fixture-proven, not field-proven. The first real exercise is the formal
  administration the packet prepares, and it is deliberately not run by this
  session.
- **`--check` detects an edited report; it does not detect a deleted one.**
  A missing report is reported as missing, which is the honest behavior, but
  nothing forces a record's report to exist.

## What this does not touch

No question ID, no question text, no verdict word, no formula term, no
parameter. No owner act is performed, offered, or implied. The instrument
remains a candidate; P-34 remains open; `openspec/` still does not exist.

## Where the records cited here live

- Instrument: `launch-gate-pre-specifications.md` (repo root), §9 carries
  the v2.0 changelog entry.
- Schema: `launch-gate-administration.schema.json` (repo root).
- Tools: `scripts/validate_launch_administration.py`,
  `scripts/render_launch_administration.py`.
- The Markdown chain it supersedes: `round-2026-08e/LAUNCH-GATE-v1.*-SEMANTIC-DELTA.md`
  and `round-2026-08e/reviews/RD-33…RD-45`.
- Preflight for this round: `round-2026-08f/FINAL-LAUNCH-CLOSURE-PREFLIGHT.md`.
