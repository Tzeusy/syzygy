# Launch-gate v1.6 → v1.7 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority. This delta records every change of meaning so
> "no question was weakened" stays a reviewable claim. Owner approval of
> v1.7 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34) —
> and the offer waits on a fresh-context re-review of this delta
> (**RD-35**), because the session that authored these bytes may not
> confirm them.

Baseline: v1.6 as re-reviewed by RD-34 (subject sha256
`9d68fa3b8f588072b746a51243f66fa0c9de75c97c6ea945b08ea0cf44238544` at
commit `0bdd37d`; raw review `reviews/RD-34-instrument-v16-RAW.md`,
`VERDICT: REVISE`, 1 BLOCKING / 4 MAJOR / 6 MINOR — and all twelve RD-33
repairs verified present, six by execution). Every delta below closes an
RD-34 finding; dispositions in `reviews/DISPOSITION-REGISTER.md`. **No
question's fail condition was narrowed, no verdict word was removed, no ID
renumbered.** Validator changes each carry a mutation fixture
(`scripts/launch_gate_results.py --selftest`, **43 fixtures**).

RD-34's sharpened diagnosis, accepted whole: v1.6's central repair moved
the entire deferral-carrying-pass population onto the one verdict branch
the validator checked against no §4 conjunct. RD-34's closing judgment —
*"after RD34-01 there is no unchecked verdict branch left to route a pass
through"* — is this batch's convergence claim; RD-35 tests it.

## D-1 — The `READY-WITH-DEFERRALS` predicate stated and checked (RD34-01, BLOCKING)

§4 now states the predicate **as a formula**: identical to
`READY FOR <LAUNCH_TARGET>` in every conjunct — every E `Met`, no plain
`Not met` in launch-scope A–D, F1 `Met`-or-`Unknown`, F3 `Met`, F4 `Met`
— with exactly one substitution (the F2 limb satisfied by an owner-cited
deferral), plus a nonzero `Deferred count:` and the citation. The E, A–D,
F1, F3 and F4 conjuncts are declared **never deferrable**, each already
carrying §4's own rationale. The validator runs the full conjunct battery
on **both** pass branches; RD-34's H9d — all 39 rows `Not met` under
`READY-WITH-DEFERRALS` with a citation, which validated clean at v1.6 —
is now a fixture that fails without the repair. *Semantic change:* a pass
route that existed only by omission is closed; §4's own "every term is a
predicate over the closed vocabulary" claim becomes true of both pass
verdicts. Nothing weakened.

## D-2 — Deferral citations gain a shape-and-existence test (RD34-02, MAJOR; RD34-07, MINOR)

The `Owner deferral decision:` value must be a repository path — verified
to **exist at the record's named commit** when git checks run — or a
decision identifier (`SDR-n` / `P-n` / `D-n` / `B-n` shape, lettered
sub-forms included). Label wording — `(owner only)`, `the owner`, `TBD` —
is rejected, so RD33-03's string can no longer satisfy the check one
field over. And §5's first disjunct is now enforced: a nonzero
`Deferred count:` requires the citation under **any** verdict, not only
`READY-WITH-DEFERRALS` — an uncited deferral cannot enter the trend log
through a `NOT READY` record. Fixtures: label rejected, nonexistent path
rejected (git on), identifier accepted, uncited-count-under-NOT-READY
rejected. The RD33-03 disposition row's overclaim is corrected in place
with a dated marker — the row described this check before it existed.

## D-3 — The terminal `GATE VERDICT:` line is the one parsed (RD34-03, MAJOR)

The validator takes the **last** match, matching §5's "terminal line"
word. RD-34's H6 — a summary `GATE VERDICT: NOT READY` shadowing a
terminal `READY FOR` over a failing row set — is a fixture proving the
terminal line is now the one checked. The pilot record's two-line shape
can no longer pick which line the tool sees.

## D-4 — A new scoped finding is a new finding (RD34-04, MAJOR)

§6 states the rule precisely: New-findings counts rows newly `Not met`
(not `Not met` in the prior administration — a scoped row turning plain
counts, it newly blocks; the r5 behavior RD-34 verified is preserved)
plus rows newly scoped that were not previously a finding under either
rendering — so scoping never zeroes the delta column, and reclassifying
an old finding never double-counts. The validator implements exactly the
two limbs; both directions are bespoke selftest checks (prior-clean →
current-scoped counts 1; prior-scoped → current-plain still counts 1).

## D-5 — The two stale version references, made version-neutral (RD34-05, MAJOR)

`DEFERRED-WAVE-POSTURE.md` (a `DEFAULT_ROUTE_SET`-reachable file and §8's
`LAUNCH_TARGET` source) and `FIRST-OPENSPEC-SEQUENCE.md` (§8's
`FIRST_SPEC_CANDIDATE`) no longer quote an instrument version at all —
each cites the instrument's own `effective_version:` header, so a version
bump cannot strand them a third time. RD-34 noted this was a
**Reopened**-class recurrence (the same two files RD25-03's row recorded
fixed); the repair removes the class rather than patching the instance.
The mechanical-guard alternative RD-34 raised was considered and declined
in favor of this — recorded in the disposition table so the choice is
visible.

## D-6 — Smaller validator strengthenings (RD34-06, RD34-08, RD34-11, MINOR)

LG-9's placeholder set widens past the literal "none" (`n/a`, `TBD`,
`todo`, `pending`, `not applicable`, bare digits, bare punctuation — the
H1 strings are a fixture). LG-11's launch-target check upgrades from
substring containment to whitespace-normalized **equality** with the
`LAUNCH_TARGET` scalar or its first sentence, per §5's "verbatim" — the
H7 fragments (`Capability 1`, `The`) now fail, and the GOOD fixture
carries the full first sentence. LG-10 binds **membership** as well as
presence: a row ID outside the 39-entry roster errors, so an invented
question cannot enter the trend row's computed columns (H5 is a fixture).

## D-7 — Record honesty (RD34-09, RD34-10, MINOR)

The v1.6 delta's D-7 claimed §6 project-invariance in a form RD-34 showed
was not literally true: §6 still names the Syzygy trend-log path, because
RD24-17 **requires** §6 to name it. The honest statement, made here in
the form RD-34 supplied: **§6 carries no project-specific record or
narrative; the trend-log path remains, as RD24-17 required.** The two
requirements were in tension and the v1.6 delta resolved it by asserting
the stronger claim — the same over-assertion class its own D-10 was
correcting. The frozen v1.6 delta is not edited. P-34's option (a) now
routes the owner to D-10 before the v1.5 delta's two corrected claims
(RD34-10).

## What did not change

Question IDs and texts A1–A6, B1–B5, C1–C7, D1–D4, E1–E6, F1–F6, G1 —
**zero question blocks changed** in this amendment (v1.6's one E4 edit
stands; v1.7 touches §4, §6, §9 and the header only, so §1, §2, §3, §5,
§7 and §8 are byte-unchanged from v1.6). The closed verdict vocabulary is
unchanged. The `READY FOR` formula's conjuncts are
unchanged; `READY-WITH-DEFERRALS` gained its explicit predicate and lost
nothing — a record lawful under a correct v1.6 reading remains lawful
under v1.7.
