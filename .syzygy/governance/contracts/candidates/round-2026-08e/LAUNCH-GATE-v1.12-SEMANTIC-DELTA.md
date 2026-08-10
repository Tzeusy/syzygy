# Launch-gate v1.11 → v1.12 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority. This delta records every change of meaning so
> "no question was weakened" stays a reviewable claim. Owner approval of
> v1.12 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34) —
> and the offer waits on a fresh-context re-review of this delta
> (**RD-40**), because the session that authored these bytes may not
> confirm them.

Baseline: v1.11 as re-reviewed by RD-39 (subject sha256
`506463ffa7caff9988f4a4dc0b66df6f652bf582d5f3c0d0f3ca5001e20533b9` at
commit `c70e756`; raw review `reviews/RD-39-instrument-v111-RAW.md`,
`VERDICT: REVISE`, 2 BLOCKING / 2 MAJOR / 3 MINOR — and the strongest
verification pass of the chain: all seven RD-38 repairs present, five
closed outright, ten of the reviewer's twelve mutation-reverts failing
exactly the fixtures their repair added, the uniformity count up from
10-of-16 to 13-of-17, §1–§8 byte-identical per-section for the fifth
amendment running). Every delta below closes an RD-39 finding;
dispositions in `reviews/DISPOSITION-REGISTER.md`. **This is a
validator-and-records batch a fifth time: no question block, no verdict
word, and no section §1–§8 of the instrument changed** (verified
per-section against `git show c70e756:launch-gate-pre-specifications.md`;
§8 parameter block `6610` bytes, digest unchanged across all eight
instrument versions that have carried it — recompute with the validator's
own `param_block_bytes`). The instrument bytes that move: the
`effective_version:` header, the appended §9 v1.12 entry, and three dated
correction markers in the §9 v1.11 entry (D-1 names them). Validator
changes carry fixtures (`scripts/launch_gate_results.py --selftest`,
**132 fixtures** — the count read from the selftest's own printed
output); **seven** mutation-reverts, each failing exactly the fixtures
its repair added.

RD-39's diagnosis, adopted as this batch's discipline — moved one word
past RD-38's uniformity: **direction**. *"A repair must be specified over
the property the instrument requires — 'the record's own structure, not a
quotation of it'; 'the record's own last verdict line' — and then
verified against every carrier and every downstream rule that property
touches, including the rules the repair itself newly stands upstream of.
A strip is not a distinction, and inserting one changes the meaning of
every rule defined over the text it edits."* Like its five predecessors,
this record predicts nothing about whether the batch is the last.

## D-1 — corrections of the frozen v1.11 delta and the §9 v1.11 entry (the frozen record is not edited)

Four claims of the v1.11 delta are false; per the D-10 convention the
frozen record is not edited, and this entry is the correction of record.
The three that also appear inside §9 — the bytes an approval digest
binds — carry dated correction markers in place (the RD36-01/RD38-02
precedent; §9 is changelog, not §1–§8).

1. **D-2's "reaches every check" claim** (and §9's parenthetical "no
   longer validates by quoting the template"): **false** — true of the
   fenced carrier only. RD-39 measured the composite validating at 0
   errors when the template is carried in an HTML comment (both
   surfaces, LG-4 included), a blockquote, a four-space-indented block,
   or one line of prose. The repair had closed one carrier of four; the
   distinction itself is D-3 below.
2. **D-7's premise** ("the raw last value was returned") and the
   "eight mutation-reverts, each failing exactly the fixtures its
   repair added" sentence (also in §9 and P-34): **false** — v1.10's
   `_decl` returned `vals[-1].strip()`, a stripped value, so the
   trailing-space witness fixture passed at v1.10 too, and reverting
   v1.11's return to the exact v1.10 bytes failed **0 of 116**
   fixtures. The mutation the delta cited reverted to code that never
   existed. The real behavioral change — internal whitespace — was
   unfixtured; it is fixtured at D-6 below.
3. **The directionality statement**: **false three ways** (RD39-04) —
   D-2 newly *accepted* records v1.10 rejected (the fenced-appendix
   over-rejection, measured at 9 errors → 0) while being listed
   reject-only, contradicting the delta's own D-2 bullet; the
   trailing-space "new acceptance" was not new (0 errors at both
   versions); and the accept/reject vocabulary could not express the
   batch's most consequential change — **same acceptance, changed
   verdict** — which is exactly where RD39-01's harm lived. This
   delta's "What did not change" section states directionality over
   three axes.
4. **D-6's impossibility sentence** ("not closable by version
   cross-checks") and §9's "no version cross-check can refuse it":
   **false** — the validator verifies a record against the commit the
   record itself names, so a lawful v1.10-era record scores 0 errors
   under the v1.11 validator at its own named commit (RD-39's own
   construction). The residual was a scope decision stated as an
   impossibility; the scope is closed at D-5 below.

Also corrected in passing: the delta template's *"byte-identical to
their pre-batch state"* phrasing was loose for the just-added
predecessor raw review (RD-39 §3, carried from RD-38's same note); this
delta's "What did not change" names the frozen population explicitly.

## D-2 — the terminal verdict line is measured over the raw record bytes (RD39-01, BLOCKING — a hole the v1.11 batch created, closed)

v1.11 inserted `_active_text` upstream of RD35-02's terminal-line rule
("the last line CONTAINING the literal token") and thereby silently
redefined "last": a record whose stored terminal `GATE VERDICT:` line
read `NOT READY`, hidden behind an unterminated fence, validated with 0
errors and printed `READY FOR <the verbatim launch target>` into the
trend row — same acceptance as v1.10, opposite verdict, on the one line
§5 makes decisive. The sharper carrier was four-space-indented
backticks, which are not a fence in CommonMark at all, so the discarded
`NOT READY` was ordinary visible prose to every reader. At v1.12:

- The terminal line is the last line carrying the token **in the raw
  bytes**. If that line is not also the active terminal line — fenced,
  comment-carried, swallowed by an unterminated fence, or shadowed by
  a quoted verdict line placed after the record's own — the record
  **errors loudly**, and no earlier line is ever parsed in its place.
- Consequence accepted and stated: a record that quotes a verdict line
  *after* its terminal verdict (e.g. in a template appendix) now
  errors as ambiguous rather than validating. §5's "terminal" means
  last; a record wanting a quoted appendix puts it before the terminal
  verdict or omits the verdict line from the quotation. The selftest's
  lawful-appendix fixture is reshaped accordingly and a new fixture
  asserts the ambiguity error.
- Fixtures: the laundered unterminated-fence record errors; the
  quoted-verdict-after-terminal record errors; the indented-carrier
  record parses its visible `NOT READY` correctly (via D-4's grammar);
  the no-fence qualified-terminal control still errors (RD35-02's
  fixtured shape, unchanged).
- Re-executed against RD-39's attack records, git on, real digests:
  the laundered record scores 1 loud error and the trend verdict
  column carries `—`, never `READY`; the indented-carrier record's
  trend verdict is `NOT READY`.
- Mutation-proven: reverting to the active-text-only rule fails
  exactly the two new RD39-01 fixtures.

## D-3 — presence becomes the record-versus-quotation distinction, not another carrier strip (RD39-02 BLOCKING, RD39-07 MINOR)

v1.11 implemented "a quotation is not the record" as a fence strip;
RD-39 measured the composite — G1 and six declared fields deleted —
validating clean when the template rode an HTML comment (invisible in
rendered markdown), a blockquote, an indented block, or one line of
prose. At v1.12 the presence checks own the distinction the value
checks already had:

- The six `Label:` presence tokens are **line-anchored field reads**:
  the label at ≤3 spaces of indentation (CommonMark's own bound),
  optionally list-marked or bold-wrapped, internal whitespace
  normalized (`[^\S\n]+` between label words, `[^\S\n]*` before the
  colon — closing RD39-07: `Reviewer  model family:` and
  `Materials given :` are present, never "missing"). A blockquoted
  `> Label:`, a ≥4-space-indented line, and a mid-line prose mention
  all fail the anchor — they are quotations of the label, not the
  field.
- The non-authority banner gets a **structural test**: a blockquote
  line carrying the phrase — §5's banner IS a blockquote, which is
  precisely why blockquote-stripping could never be the fix. A prose
  restatement fails it. **Disclosed limit, stated rather than
  silent:** a nested-blockquote quotation (`> > …`) of the banner
  still satisfies the structural test, being byte-for-byte the
  banner's own form one level deeper; in RD-39's blockquote composite
  the other six fields and LG-4 still reject the record (6 errors).
- **HTML comments join fences in `_active_text`** — a comment is the
  one carrier no reader ever sees, so its bytes are not the record;
  this also ends the comment-carried G1 heading satisfying LG-4. An
  unterminated comment blanks the rest, loud on the roster and on
  D-2's raw-terminal rule.
- Fixture matrix: comment/blockquote/indented/prose carriers each
  rejected on their surface; inline-comment lawful record accepted;
  bold-wrapped, double-spaced, and list-marked labels accepted.
- Re-executed against RD-39's composite in all four carriers, git on:
  comment 7 errors, blockquote 6, indented 7, prose 7 — zero clean
  passes.
- Mutation-proven: reverting presence to substring scans fails exactly
  five fixtures (four carrier rejections and the RD39-07 double-space
  acceptance); removing comment stripping fails exactly the two
  comment fixtures.

## D-4 — the fence grammar aligns with CommonMark where RD-39 measured divergence (RD39-06, MINOR)

Two divergences closed: a fence marker now counts only at ≤3 spaces of
indentation (four-space-indented backticks are literal content of an
indented code block, so the prose between them — RD39-01's sharper
carrier — stays active), and a closing run must be the same character
and at least as long as the opening run, alone on its line (a
four-backtick fence is no longer closed by three, so its quoted
content stays stripped). Correct behaviors RD-39 verified — tilde
fences, info strings, mid-line backticks inert, blockquoted fences
inert — are preserved. Fixtures both directions; each divergence
mutation-proven separately.

## D-5 — the prior is validated as a record at its own named commit (RD39-05, MINOR)

RD-39 refuted the v1.11 impossibility claim by construction: LG-1/
LG-2/LG-11 verify a record against the commit **it** names, so a
lawful v1.10-era record scores 0 errors under this validator at its
own commit. That construction is adopted as the repair: the `--prior`
record is validated whole (recursion depth 1 — the prior's own
`--prior` is never followed), so a bare roster-complete row block —
lawful verdicts or not — is refused, and the all-`Not met` fabrication
that drove New-findings to zero is refused with it. The refusal names
itself and the trend column reads `n/a — prior record failed
validation`, as before. The two lawful-prior fixtures still pass (the
scoped-prior fixture now names its scoped defect, as a lawful record
must under LG-9). **Honest cap, stated rather than silent:** a forged
but fully lawful-shaped record naming a real commit remains
representable — this guard demands the full lawful shape at the
prior's own anchors, a raised bar, not an impossibility claim.
Mutation-proven: reverting to the roster-only guard fails exactly the
three bespoke prior fixtures.

## D-6 — the internal-whitespace fixture: rule 6 satisfied against the code the repair replaced (RD39-03, MAJOR)

The v1.11 normalization repair's real behavioral change — collapsing
*internal* whitespace, which v1.10's `.strip()` did not — gains its
fixture: `E3 reopen-list: none  identified` accepts. Reverting
`_decl`'s return to the **exact v1.10 bytes** now fails exactly that
fixture, which is the rule-6 proof the v1.11 batch claimed and did not
have. The trailing-space fixture is kept as a regression guard,
stripped of its witness status. D-7's false premise and the false
mutation sentence are corrected at D-1 (and dated in §9); P-34's
recommendation is corrected directly, being a living record.

## What did not change

- **No section §1–§8 of the instrument changed** — verify per-section
  against `git show c70e756:launch-gate-pre-specifications.md`. The §8
  parameter block hashes identically across all eight instrument
  versions that have carried it (recompute with the validator's own
  `param_block_bytes`, never from this record). The instrument bytes
  that move: the `effective_version:` header, the appended §9 v1.12
  entry, and the three dated RD39-02/RD39-03/RD39-05 correction
  markers in the §9 v1.11 entry (D-1).
- **No frozen record is edited.** The frozen population, named
  explicitly: the nine deltas v1.4–v1.11 and the raw reviews RD-33
  through RD-39 are byte-identical to their state at `c70e756` (RD-39's
  raw review was added after `c70e756` and is frozen as stored; its
  storage digest is in the delivery register). The v1.11 delta's four
  false claims are corrected by this delta's D-1, in the D-10
  convention.
- **No question weakened, no ID renumbered, no verdict word changed.**
- **Directionality, on three axes** (the RD39-04 restatement):
  *Newly rejected:* the laundered-terminal and quoted-after-terminal
  records (D-2), the comment/blockquote/indented/prose carrier
  composites and the comment-carried G1 (D-3), the four-backtick
  short-close exploit (D-4), the bare and fabricated priors (D-5) —
  each fixtured or re-executed above. *Newly accepted:* the
  indented-backtick record whose visible `NOT READY` v1.11 deleted
  (D-2/D-4, fixtured); the double-spaced and space-before-colon label
  forms v1.11 reported missing (D-3, fixtured); the internal-whitespace
  marker form (D-6, fixtured — an acceptance v1.11 made and never
  fixtured, now owned). *Same acceptance, changed verdict:* the
  indented-carrier record — accepted by both versions — reports
  `NOT READY` at v1.12 where v1.11 reported no verdict at all after
  deleting the line; no case moves in the dishonest direction
  (READY where the record says otherwise), and the laundering case
  that did is now an error, not a verdict.

## Fixture arithmetic

116 → **132**: +1 RD39-05 (bare lawful roster refused, added to the
bespoke prior loop), +3 RD39-01 (laundered terminal rejected;
quoted-after-terminal rejected; indented-carrier parses correctly), +1
RD39-06 (four-backtick short-close), +3 RD39-02 comment carriers
(field-in-comment rejected; G1-in-comment rejected; inline comment
lawful), +4 RD39-02 anchor carriers (blockquote, indented, prose,
prose-banner rejected), +3 RD39-07 acceptances (bold, double-space,
list-marked), +1 RD39-03 (internal whitespace). Count read from the
selftest's own printed output (`132 fixtures, 0 failing`). All
LG-1…LG-13 checks still fire; the seven mutation-reverts each fail
exactly the fixtures their repair added (denominators: 2, 2, 1, 1, 5,
3, 1).
