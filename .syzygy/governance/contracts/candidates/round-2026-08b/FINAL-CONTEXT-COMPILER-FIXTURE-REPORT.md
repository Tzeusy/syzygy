# Context fixtures — what they prove, and the thing they do not

> **Non-authoritative round record.** RFC-0011's clauses are the authority
> for what a context packet must be; the fixtures are evidence about the
> corpus, not obligations on it. Supersedes
> `../round-2026-08/CONTEXT-COMPILER-FIXTURE-REPORT.md`, which is
> banner-marked as a round record.

## The finding that reframes everything else

**`scripts/context_load.py` is not a compiler, and there is no mechanical
route from a task to a packet.**

Review RC-6 established this from the script's own interface, and it
reproduces in one command: `context_load.py` takes *paths you have already
chosen*, counts their words, multiplies by 1.35, and prints a total. It has
no notion of a task, a warrant, a risk class, an `applies_to` value, a clause
identifier, or a dependency edge. Nothing in `scripts/` maps a task to a
selection.

So each fixture's **selection is human judgment**, narrated afterwards in its
"Selection rule trace (RFC11-4)" prose. What is mechanical is the
*measurement* of that selection. Every fixture nonetheless carried the line
`Compiler: context_load.py, selection rules rev10-fixtures`, which reads as
though a compiler produced the set.

The prior report said the fixtures "are selection fixtures, not packets." It
did not say the further thing, which is the one that matters: **they are also
not compiled selections.** They are worked examples of what a compiler, if
one existed, ought to produce.

**This cannot be fixed in this phase.** A selector is application code, and
this phase forbids application code. The honest position is therefore: the
per-task load is *governed* (RFC-0011 says what a packet owes), *budgeted*
(each fixture is measured), and *demonstrated by hand* — and it is **not
compiled**. Any claim that Syzygy has automatic context compilation today is
false, and the readiness answer must say so rather than route around it.

## What the fixtures do prove

Eight tasks, each with a mandatory load, an omitted-candidate list with
reasons, and a re-runnable digest. Every one lands between roughly 10.8k and
22.2k words against a rev9 whole-corpus path of ~121k. That is a real result:
it establishes that a *correct* selection for one task exists and is small,
which is the premise the Context Compiler contract is built on. It does not
establish that a machine can find it.

## Freshness — now mechanical, and it was needed

All eight fixtures were stale when checked on 2026-08-05b. Every packet
digest and every word count had drifted from what the fixture recorded.

| Fixture | Recorded | Actual | Drift |
|---|---|---|---|
| 1 — Polaris narrative | 13,864 | 13,842 | −22 |
| 2 — Trajectory adapter | 18,315 | 18,282 | −33 |
| 3 — Orrery lens | 14,134 | 14,110 | −24 |
| 4 — execution profile | 10,893 | 10,866 | −27 |
| 5 — cross-project mission | 12,843 | **14,581** | **+1,738** |
| 6 — doctrine amendment | 11,537 | 11,523 | −14 |
| 7 — kernel identity | 15,767 | 15,738 | −29 |
| 8 — OpenSpec authoring | 22,258 | 22,242 | −16 |

The small negatives are the `provides_to` front-matter key being removed from
every module. Fixture 5's +1,738 is RFC-0010's correction plane — the fixture
that loads the Mission contract, growing by exactly the six clauses that
review demanded. All eight are corrected and each carries a dated
re-measurement note stating its previous value.

**The check that found them is new.** `check_governance.py` CG-18 parses each
fixture's declared mandatory set, concatenates it in listed order, and
recomputes both the digest and the word count. Before this round nothing did
that, which is why the drift accumulated silently. RC-6 caught two of the
eight by hand; CG-18 catches all eight, every run, with a denominator.

A note on the check's own history: its first version anchored on a `(recompute`
suffix and silently examined 4 of 8 fixtures while printing a count — the
precise failure mode this repository exists to prevent. It now anchors on the
`## Packet digest` heading and covers all eight.

## Coverage against the eight required classes — seven, not eight

| Required class | Fixture | Assessment |
|---|---|---|
| Doctrine amendment | 6 | clean fit |
| Kernel identity change | 7 | clean fit |
| OpenSpec capability authoring | 8 | clean fit |
| **Evidence adapter change** | — | **uncovered** |
| Polaris governed-presentation edit | 1 | clean fit |
| Trajectory work-lifecycle change | 2 | clean fit |
| Orrery visual/lens change | 3 | clean fit |
| Bounded Mission spanning capabilities | 5 | clean fit |
| *(no required class)* | 4 | good fixture, matches no class |

**The evidence-adapter class has no fixture.** Fixture 2 is a *work-provider*
adapter change: it loads RFC-0004's `general-contract` and `named-adapters`
and explicitly excludes `execution-record.md` and
`fidelity-joins-and-mappings.md` — the two modules that carry the evidence
plane. RFC-0004 is titled *"Observation Sources, Evidence, Execution Records
and Adapters"*, and fixture 2 deliberately takes the non-evidence half. So
capture cadence, fidelity labels, provenance joins, and gate-artifact tiering
— RFC4-13's four routes, which CC-TEST-2 leans on — are exercised by no
fixture in the set.

Counting fixture 2 twice made an eight-for-eight map look complete when it is
**seven-for-eight with one double-count**. The prior report's table listed the
eight fixtures without mapping them to the required classes at all, which is
how the gap survived.

**Closed on 2026-08-06 by fixture 9**, `context-selection-9-evidence-adapter.md`
— an evidence-adapter change amending the test/CI/gate observer (RFC4-13) and
its registry entry for a new external CI provider. The class map is now
eight-for-eight without a double-count.

Three things about it are worth carrying, because none of them is flattering:

- **It does not fit the budget.** 24,025 words ≈ 32,433 estimated tokens — the
  largest packet in the set, above the 20,000-token decomposition trigger by
  either heuristic. The fixture states this and names a lawful shard (the
  fidelity-labeling half, 10,350 w ≈ 13,972 tokens, inside the band) rather
  than trimming the selection to flatter the figure. The tiering half is not
  rescuable.
- **It inherits every limitation above.** The selection is hand-authored;
  there is still no compiler. The fixture therefore records **no** `Compiler:`
  line and no selection-rule version — the eight before it claimed
  `Compiler: context_load.py`, which was the misdescription RC-6 found, and
  `rev10-fixtures` resolves to nothing anywhere in the repository.
- **One declared dependency edge is left open, not hidden.** Eight of the nine
  loaded modules declare `depends_on: RFC-0001`, and the packet does not carry
  it. The fixture tabulates all twelve cited RFC1-n identities, marks which
  five are restated at binding strength inside loaded clauses and which seven
  are citation rather than reliance, names three triggers that would promote
  RFC-0001 to mandatory, and measures the cost of closing it mechanically:
  32,367 w ≈ 43,695 tokens.

The gap this section recorded is closed. The limitation it recorded is not.

## The two shapes the hand-authored selections get wrong

RC-6 attempted three of the tasks from their packets alone. Its misses
cluster, and both clusters are properties a real compiler would have to
avoid:

1. **README-citation-for-clause-text substitution.** A packet loads a module
   that *names* a rule (VIS-2, RFC2-24) and treats naming as carriage. Found
   in fixtures 2 and 8. The package had identified this exact failure mode,
   left it unchecked in all eight, and then committed it twice more in files
   it had just repaired.
2. **Whole-contract granularity.** `applies_to: polaris` pulls 10,636 words
   of RFC-0007 when two of its three modules carry the load-bearing clauses.
   No mechanism exists to pull `RFC7-38 + RFC7-26..37` without
   `RFC7-1..RFC7-25`.

## One instrument that is not quotable on this machine

`semantic-equivalence-fixtures.md` (F-EQ-1…8) is a separate rev9→rev10
equivalence instrument, correctly excluded from the coverage table above. Its
commands are written for GNU grep; `grep` here is ugrep, so **F-EQ-4 and
F-EQ-8 need re-running under a real GNU grep before their results are
quotable.** They have not been.

## Verification

```sh
python3 scripts/check_governance.py            # read CG-18's line and its denominator
```
