# Launch-gate v1.7 → v1.8 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority. This delta records every change of meaning so
> "no question was weakened" stays a reviewable claim. Owner approval of
> v1.8 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34) —
> and the offer waits on a fresh-context re-review of this delta
> (**RD-36**), because the session that authored these bytes may not
> confirm them.

Baseline: v1.7 as re-reviewed by RD-35 (subject sha256
`c0b0dca4813123d9c660193bd3bd21d66437586cff1829839ad7dc03a6c877b2` at
commit `eb53c3e`; raw review `reviews/RD-35-instrument-v17-RAW.md`,
`VERDICT: REVISE`, 1 BLOCKING / 3 MAJOR / 3 MINOR — and all eleven RD-34
repairs verified present, eight by rebuilding RD-34's own records and
executing the validator). Every delta below closes an RD-35 finding;
dispositions in `reviews/DISPOSITION-REGISTER.md`. **This is a
validator-and-records batch: no question block, no verdict word, and no
section §1–§8 of the instrument changed** — RD-35's own words: *"none of
my seven findings requires an instrument amendment. §5 already says
'terminal', §4 and §5 already say `<LAUNCH_TARGET>`, §3 already states
E3's fail condition."* The instrument's only moved bytes are the
`effective_version:` header and the §9 changelog entry. Validator changes
each carry a mutation fixture
(`scripts/launch_gate_results.py --selftest`, **64 fixtures**).

RD-35's convergence verdict, accepted whole: *"the instrument has
converged while the validator has not"* — and this batch deliberately
declines to predict it is the last. RD-36 tests it.

## D-1 — The citation-existence check un-inverted, and its passing direction fixtured (RD35-01, BLOCKING)

`str.lstrip("./")` is a character-class strip: every citation beginning
`.syzygy/` lost its leading dot, resolved as `syzygy/…`, and was rejected
as *"a citation to nowhere"* — **the path form was unusable for every
decision in the repository's own decision home** (§8's `C7_POPULATION`).
The repair is a prefix strip (`v[2:] if v.startswith("./") else v`), and
— for the first time — the **passing direction is fixtured**: an existing
repository path (`.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md`)
is ACCEPTED at the named commit with git checks on and the real committed
digests, beside the existing rejection fixture for a nonexistent path.
RD-35 named the blind spot exactly: every prior path fixture asserted a
rejection, so a check that rejected its entire lawful input set read as
green (verification rule 6's untested direction). The mutation was
re-applied to a copy this session and the new fixture fails without the
repair — the fixture sees the bug it exists to prevent.

**Correction of the v1.7 delta's D-2, in the D-10 convention (the frozen
record is not edited):** D-2 stated *"verified to exist at the record's
named commit when git checks run"* — not true of the v1.7 bytes for any
`.syzygy/` path. The claim is true of the v1.8 bytes. The disposition
register's RD34-02 row additionally claimed a *"real-path … accepted"*
fixture that did not exist among the 43; that row carries a dated
correction, the same convention as RD33-03's row — which was corrected
once already for describing this same check before it existed. Two
corrections on one check's record trail is itself evidence for RD-35's
convergence reading, and is recorded here so the owner meets it.

## D-2 — The terminal line is the anchor, and it must parse (RD35-02, MAJOR)

The validator anchored on the last regex **match**, and the verdict regex
requires end-of-line — so any terminal verdict carrying a qualifier
failed to match and the tool silently read an earlier line. RD-35's
H6-reverse: a summary `READY FOR …` line above a terminal
`GATE VERDICT: NOT READY — pending the owner's F2 deferral decision`
validated clean and trended as a pass. Now the anchor is the last line
**containing the literal token** `GATE VERDICT:`; that line must itself
parse to the closed verdict set — a qualified or quoted terminal verdict
is an **error**, never an invitation to look upward — and a captured
verdict containing `|` is rejected before it can structurally corrupt
§6's nine-column trend row. Fixtures: the qualified-terminal case and the
quoted-§5-template appendix case; the anchoring mutation was re-applied
to a copy and the fixture fails without the repair. *Semantic change:*
§5's "terminal line" word is enforced as written; the v1.7 delta's D-3
sentence (*"the two-line shape can no longer pick which line the tool
sees"*) becomes true of the bytes — at v1.7 it held only when the
terminal line matched.

## D-3 — The verdict line's target is the header's target (RD35-03, MAJOR)

`READY FOR anything the reviewer likes` validated clean and entered the
trend row — the one string F1 is answered from. The `READY FOR <target>`
tail now gets the **same** whitespace-normalized equality test LG-11
applies to the header `Launch target:` line (the `LAUNCH_TARGET` scalar
or its first sentence): one placeholder, one enforcement standard.
Fixtures: the verbatim-target READY record validates clean (git on, real
digests — also the first clean-validating full-template READY fixture);
a target §8 never bound fails.

## D-4 — E3's reopen-list is checked against its own verdict (RD35-04, MAJOR)

§3 calls E3 *"the sharpest single gate"* and states *"the list is
non-empty; 'ready' is then false regardless of every other verdict"* —
and the validator never read the field. A record enumerating three
reopened shape questions beside `E3 | Met` and `READY FOR` validated
clean. New check (LG-13), the same shape as LG-8 and LG-9 — a declared
field contradicting a verdict row: a non-empty `E3 reopen-list:` beside
`E3 | Met` errors, and beside any READY verdict errors; the field itself
is required (absence reads as empty, and absence is never a pass).
"Empty" is judged by the same names-nothing rule LG-9 owns, so the two
share one definition. Fixtures: enumerated-list-beside-Met, enumerated
list under READY, deleted field.

## D-5 — "Names nothing" becomes a lexicon rule (RD35-05, MINOR)

LG-9's placeholder test was an enumeration `fullmatch`, and decorated
forms of its own target word passed — `(none known)`, `-- none --`,
`unknown`, `tba`. The rule is now shared `_names_nothing()`: after
stripping punctuation, a value names something only if at least one
token falls outside the placeholder lexicon (articles and bare digits
never count). No fourth enumeration extension; the residual class is
removed rather than chased. Fixtures: the RD-35 residual strings.

## D-6 — Deferral identifiers narrow to made decisions (RD35-06, MINOR)

`P-n` names this repository's **pending**-decision queue — `P-34` is
itself the unmade decision that offers this instrument — and `D-n` is a
semantic-delta item number. Both satisfied a *granted*-deferral citation
at v1.7. The identifier form now accepts `SDR-n`/`B-n` (made decisions);
`P-n`/`D-n` are rejected with an error naming the reason. Fixtures:
`P-34` and `D-10` rejected, `B-1` accepted, `SDR-33` accepted (existing).

## D-7 — §5's declared fields are enforced (RD35-07, MINOR)

Seven record fields §5 declares — including the non-authority banner
RD24-02 made required — could each be deleted with zero errors. New
check (LG-12): the banner, `Reviewer model family:`, `Materials given:`,
`Operationalization notes:`, `E3 reopen-list:`, `Unknowns and what would
settle them:`, and `Reviewer's falsification notes:` are presence-tested;
and a record with any `Unknown` row must name settling evidence in the
Unknowns field (§4's companion requirement, previously checkless — a
placeholder there errors). The non-mechanical §2 requirements (fresh
context, full administration) remain prose-and-judgment, as the tool's
scope note discloses. Fixtures: each deletion errors; Unknown rows
beside a placeholder Unknowns field error.

## What did not change

Question IDs and texts A1–A6, B1–B5, C1–C7, D1–D4, E1–E6, F1–F6, G1 —
**zero question blocks changed**; §1 through §8 of the instrument are
**byte-unchanged from v1.7** (the header's `effective_version:` line and
the §9 changelog entry are the only instrument bytes that move — a
narrower footprint than any amendment in this chain). The closed verdict
vocabulary, the `READY FOR` conjuncts, and the `READY-WITH-DEFERRALS`
predicate are unchanged. Every check that existed at v1.7 still fires on
its v1.7 fixtures — all 43 prior fixtures pass, unmodified except that
the shared GOOD template's version line and the one fixture that
rewrites it track the header, updated v1.7→v1.8; a record lawful under
a **correct** v1.7 reading remains
lawful under v1.8 — the newly rejected records are exactly those §3, §4
and §5 already condemned in prose the validator did not yet enforce.
