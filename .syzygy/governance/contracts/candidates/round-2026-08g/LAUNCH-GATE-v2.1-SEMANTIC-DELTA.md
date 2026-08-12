# Launch-gate instrument — v2.0 → v2.1 semantic delta

> **A delta, not an approval.** The instrument remains a **candidate**; its
> approval as process policy is **P-34**, ungranted. This file records every
> change of meaning between v2.0 and v2.1 so that "no readiness question was
> weakened" stays a claim a reviewer can check rather than one this session
> makes about itself.
>
> **Nothing here is confirmed.** v2.1 is the repair of two `REVISE` verdicts,
> made by the session that received them. A repair session cannot confirm its
> own repairs.

## Why there is a v2.1

v2.0's two commissioned reviews both returned `REVISE`:

| Review | Subject | Verdict |
|---|---|---|
| RD-48 | policy semantics | `REVISE` — 11 findings |
| RD-47 | schema, validator, renderer | `REVISE` — 12 findings |

RD-48's central answer was reassuring and is worth stating first, because the
rest of this file is a list of defects: **no readiness question, row-level
verdict word, or trend column was dropped, renamed, or made unreachable at
v2.0.** The weakening question the charter asked was answered *no*. What the
two reviews found instead was that the instrument had drifted away from the
tool that implements it, in both directions.

## What did not change

**§1, §2, §3, §6 and §8 are byte-identical to v2.0.** Measured, not asserted —
and **reproducible**, which the v2.0 delta's equivalent table was not (RD-48
f7). The two subjects:

```text
v2.0   05ecaa954e81ef95f6e2e2b409fbcb5bd5391037c10d9624ab4af3217a00f6d2
       launch-gate-pre-specifications.md at commit efa6d63
v2.1   3afdffdab0d71d32a4e901f43db1c11ba096f699e240050e8cc6cbb95ada12c8
       the working-tree file — and the digest the formal packet seals
```

The method, which is the whole of it — split each text on its `^## <n>\.`
headings, keeping the heading line with the span it opens, and sha256 each
span:

```python
import re, hashlib, subprocess
old = subprocess.run(["git","show","efa6d63:launch-gate-pre-specifications.md"],
                     capture_output=True, text=True).stdout
new = open("launch-gate-pre-specifications.md").read()
def spans(t):
    p = re.split(r"(?m)^(## \d+\..*)$", t)
    return {re.match(r"## (\d+)\.", p[i]).group(1):
            hashlib.sha256((p[i] + p[i+1]).encode()).hexdigest()
            for i in range(1, len(p), 2)}
```

```text
§1  1f2d1d60a28ada2a   identical
§2  0d7340f2ee9a8b8c   identical
§3  fe0b051e136d2fee   identical
§4  f4a2a6423a89703f -> 84d5d3d456e7c05a
§5  c6847ffa7812853b -> 0b63585544520df4
§6  9906fcac454062cd   identical
§7  d24deb9c8eb39995 -> 9e17cb8de0458976
§8  01209c0f052971f7   identical
§9  e49dde205d069a96 -> 9301d992b12b889a
```

**One caveat, stated because this file is itself a measurement.** The §9 span
digest above is the last one computed, and §9 is the changelog — it is the one
span a further edit to this amendment would move. If you recompute and §9
differs while §1–§8 match, the amendment's *substance* is unchanged and this
table is stale in its least load-bearing row. Any §1–§8 mismatch is a real
finding.

So: **no question's text moved** (§3), **no protocol obligation changed**
(§2), **no parameter changed** (§8), and the trend-log rules are untouched
(§6). Four sections moved and each is accounted for below.

The §8 digest above is also the parameter-block digest the sealed formal
packet binds — unchanged, so every fixed input of a formal administration is
the same as it was at v2.0.

## D-1 — §4 states the gate verdict vocabulary *(RD-48 f3)*

**Was:** `NOT READY` appeared in the instrument only inside §9's changelog —
9 occurrences, all at line ≥ 889. The tool emitted it as a Python literal, the
renderer printed it as the report's last line, and the trend log carried it in
a column.

**Is:** §4 defines all three words in a table, states that the set is closed,
that a record may not contain any of them, and that `NOT READY` is the
default branch.

**Direction:** neither a strengthening nor a weakening of any verdict — it
gives an already-used word a home. What it removes is the position where the
instrument that "owns readiness semantics" did not name the word its own
failing branch produces.

## D-2 — §4 states the E3 conjunct the tool computes *(RD-48 f2)*

**Was:** §4 listed five core conjuncts. `_compute` added a sixth — *E3's
reopen list is empty* — and the generated report printed all six under the
heading "Conjuncts of the §4 formula".

**Is:** §4 lists six, with a labelled note explaining that the tool computed
it from v2.0 and that its ground is §3's own E3 rule (*"an empty list is the
readiness signal"*; fails-when: *"the list is non-empty; 'ready' is then false
regardless of every other verdict"*).

**Direction: a strengthening, and it was already in force.** No administration
becomes easier to pass. What changes is that the strengthening is now a term
the instrument carries rather than one only the tool knows.

## D-3 — row outcome, eligibility and gate result are three things *(charter §7.1; RD-47 f11, RD-48 f5)*

**Was:** one verdict, computed from the rows and presented as the gate's
answer. RD-48 built a record with `formal: false`, `administration_kind:
delta` and every row `Met`; the tool printed `Computed gate verdict: READY FOR
Capability 1 …`, then a §6 trend row carrying that verdict, then `record
valid`, exit 0 — with no error and no note — although §2 rejects a delta
record as gate evidence.

**Is:** §4 defines three outcomes and requires them presented separately.
Eligibility is computed from `formal`, `administration_kind`, `fresh_context`
and the presence of validation errors. The CLI prints `Row/formula outcome:`
and `Formal gate result:` as two lines. The report prints
`ROW/FORMULA OUTCOME:` and then either the gate verdict or
`GATE VERDICT: NONE — this administration is not eligible …` with the reasons
enumerated.

**Direction: a strengthening.** No lawful record loses a pass it previously
had: the formula is unchanged, and an eligible record's gate result *is* its
formula outcome. What is removed is the route by which a diagnostic run's
output read like a gate answer.

**And it reaches §6.** Stating the rule as covering *every* place a gate
result appears caught one the CLI repair had missed: the trend row was still
generated from the row outcome, so an ineligible administration with all-`Met`
rows would have written `READY FOR …` into the log F1 is answered from and
only from. The column now carries `NONE — not eligible; row outcome was …`.
§6's own bytes did not move — the rule is stated in §4, where the separation
lives — and the counting columns are untouched, because a diagnostic
administration's findings are still findings.

**Visible immediately:** the committed dry-run report's last line changed from
`GATE VERDICT: NOT READY` to `GATE VERDICT: NONE — … (formal: false;
administration_kind: delta; the reviewer declares no fresh context)`.

## D-4 — §4's clauses name fields that exist *(RD-48 f1)*

§4 was byte-identical at v2.0, which is exactly what left it pointing at the
deleted Markdown record format. Four clauses named fields no v2.0 record has,
and two cited checks that never run on a v2.0 record:

| §4 said | §4 now says |
|---|---|
| `Owner deferral decision:` field | `owner_deferrals[].decision_citation` |
| `Deferred count:` | `len(owner_deferrals)` |
| §5's "family line" | `reviewer.model_family` |
| `LG-9` | `LA-9` |
| `LG-6/LG-7` | the `LA-*` checks, with a note that `LG-*` belongs to the historical Markdown validator |

**Direction: no change of meaning.** Each is the same predicate over the same
fact, named in the vocabulary the record actually uses. The deferral clause
additionally now states what RD-47 f4 found the *validator* was not enforcing
— that a queue entry, a Beads issue and a candidate packet grant nothing —
which is a statement of the rule LA-11 already claimed, not a new rule.

## D-5 — §5 takes back the check enumeration *(RD-48 f5)*

**Was:** *"the tool's own docstring is the enumeration, and it is the tool's,
not this instrument's, to keep current."* An instrument making a document
normative while disclaiming responsibility for its currency — and that
docstring was already false about `LA-13`, claiming it rejected a delta record
when the check gates entirely on `formal`.

**Is:** the enumeration is the instrument's. The tool implements it, and a
check the tool runs that §5 does not name is a finding against the tool. The
`LA-13` docstring is corrected, and the half that was actually missing —
eligibility — is D-3.

**Direction: a strengthening of ownership**, and no check's behaviour changed.

## D-6 — §7's false generalization claim is withdrawn *(RD-48 f4)*

**Was:** *"The schema generalizes without change — it names no Syzygy
artifact."*

**Is:** false, and now stated as such. The schema's `$id` is a
`github.com/Tzeusy/syzygy` URL; it names `launch-gate-pre-specifications.md`
and `scripts/validate_launch_administration.py`; it cites VIS-2 and VIS-4; and
it carries this project's `SDR-n`/`P-n` decision conventions. The validator
additionally hardcodes the decisions home `LA-11` depends on. §7 now says what
generalizes — the schema's **field shapes** — and adds the two tools to the
portable core, since without them a v2.0-or-later record cannot be validated,
verdicted or read.

**Direction: a correction of a false claim**, with no effect on any
administration.

## D-7 — §9 stops quoting a fixture count *(RD-48 f6)*

**Was:** "74 mutation fixtures", while `--selftest` printed 75. A derived
value quoted outside its owning artifact went stale inside one commit.

**Is:** the sentence names no count. The count is printed by `--selftest` and
stated nowhere else.

## D-8 — the deletions v2.0 made without record *(RD-48 f8, f11)*

A deletion of a normative sentence is a change of meaning, and the v2.0 delta
recorded only what §2 *gained*. **§2 and the preamble are byte-identical at
v2.1, so nothing here is restored** — this is the record that was missing, not
a repair. Three obligations left the text at v2.0:

| Deleted at v2.0 | Where the force went |
|---|---|
| *"Never translate a verdict into softer language."* (§2) | The schema's `verdict` **enumeration**, which is strictly tighter: a softened verdict is now a schema error rather than a reading the next reader has to catch. §4 also restates the prohibition at v2.1, in the closed-set clause |
| *"Questions are **quoted verbatim** at the version administered"* → *"bound at"* (§2) | `LA-2` verifies the instrument's own sha256 against the committed bytes, and §3 — the questions — is inside those bytes. Substantively equivalent; the record's `question_digest` may read `instrument-bound` precisely because the instrument itself is bound |
| *"stored verbatim"*, of the record artifact class (preamble) | *"Never edit a past administration; supersede it"* survives in §5 |

**Why not restore them.** Each successor is equivalent-or-stronger, and §2's
byte-identity is itself load-bearing evidence in this delta — the claim that
no protocol obligation changed. Re-opening §2 to re-add a sentence whose force
is already carried elsewhere would spend that evidence to buy nothing. The
judgement is `[Inferred]`, it is this session's, and a reviewer who disagrees
should say so: restoring is cheap and the argument against it is one of
economy, not of principle.

## D-9 — corrections to the v2.0 delta's own tables *(RD-48 f9, f10)*

The v2.0 delta's new-check table and disclosed-limits list were themselves
defective. They are superseded by this file, and the specific corrections are
recorded rather than left to the reader to notice:

- **`LA-14` was missing** from the new-check table. Its refusal of a
  placeholder G1 answer is new over `LG-4`, which tested only that a G1
  section was present.
- **`LA-16`'s row did not disclose its scope** — the check runs only when
  `formal` **and** `prior_record` is null.
- **`LA-13`'s row said the rule was "previously trusted"**, where v1.18's own
  §5 said *"now checked rather than trusted"*. **Withdrawn**; the claim was
  false about its own baseline.
- **Three limits were undisclosed and one named the wrong field.** All four
  are in the disclosed-limits list below: the git-unavailable degradation
  (item 3), the trend row's independence from the `formal`-gated checks
  (repaired instead, see D-3's reach into §6), the placeholder lexicon's
  partial application (item 8), and — the retarget — that the field deciding
  scope lawfulness is `deferred_wave_findings[].blocking_conditions_met`,
  not `launch_scope` (item 7).

## Tool changes with no instrument counterpart

These repair RD-47 findings. Each is a defect the tool had; none changes what
§4 means. **Every one of them validated clean before the repair, and most
produced a `READY` verdict while doing so.**

| # | Defect | Repair |
|---|---|---|
| f1 | `REQUIRED_WAVES` / `DEFERRED_WAVES` / `effective_version` written in a form the parser could not read were **skipped**, so a record could declare any wave set and pass | Unreadable is an **error**, never a skipped check. `LA-3` and `LA-2` say so in their messages |
| f6 | `_audit_schema` refused keywords it could not implement, but not a keyword **deleted**. Removing one `additionalProperties` re-opened the claimed-verdict route the whole design rests on | Any node declaring `properties` without `additionalProperties: false` is an error |
| f4, f5 | `PENDING-OWNER-DECISIONS.md` and `.beads/issues.jsonl` granted owner deferrals through the path branch; path-ness was tested by `"/" in cite`, so a real root-level file was rejected and anything with a slash accepted | Path-ness is decided by **resolving** the citation at the commit; the file must live in the decisions home and must not be one of the named non-warrant files. One list serves both the `SDR-n` and path branches |
| f2 | Reviewer free text was emitted as raw Markdown, so a record computing `NOT READY` rendered a report carrying two forged `GATE VERDICT: READY FOR …` lines and a forged figures section above the real ones | Free text is **data**: every line blockquoted, so no line can open a heading, table or fence at document level. Structure is forbidden rather than a list of phrasings |
| f3 | The §6 new-findings column was bound to a CLI flag the renderer does not have, so every report read `n/a (no prior record)` even when the record named one | The **record's** `prior_record.path` controls. Three outcomes kept distinct: a number, "no prior declared", and `Unknown (prior record … could not be read)` |
| f8 | Deferral paths were existence-checked; **evidence** paths were not. A fabricated filename with an invented quote passed clean | Evidence paths must resolve at the named commit. Quote truthfulness stays the reader's job, as documented |
| f12 | Duplicate JSON keys were silently last-wins, so a record could mean one thing to the tool and another to a reader | A duplicate key is refused, in both tools |
| f7 | `e4.routing_authority` was recorded and rendered but bound to nothing — the only §8 parameter the record restated without binding | `LA-3b` binds it to §8, as `LA-3` does for the launch target |

## Disclosed limits — what v2.1 still does not do

Carried forward, and none of them repaired here:

1. **Presence tests on free-text fields are content-blind by design.** A
   reviewer who writes a plausible false evidence quote defeats this tool, and
   no version has claimed otherwise. Blockquoting stops free text forging
   *structure*; it does not make it true.
2. **The JSON Schema interpreter is a documented subset**, whose safety
   property is that it rejects any keyword it does not implement.
3. **With git unavailable**, identity, binding, E4 case text, deferral and
   evidence existence are not verified. The tool emits a note saying so; the
   note is easy to miss beside a computed verdict.
4. **The validator reads the instrument's own prose in five places.** Two
   failed open and are repaired; all five remain prose reads.
5. **No administration has been performed under v2.0 or v2.1.** The verdict
   path is fixture-proven, not field-proven.
6. **RD-47's asymmetry is unrepaired.** A scoped row must be disclosed in
   `deferred_wave_findings`, but an E4 case laundered from "disagree" to
   `"silent"` plus `needed_by_launch_target: false` requires no disclosure
   anywhere and no cross-read of the routing authority.
7. **The field that decides scope lawfulness is
   `deferred_wave_findings[].blocking_conditions_met`**, not `launch_scope`
   — a reviewer-authored boolean, checked for consistency but not for truth.
   The v2.0 delta's limit note named the wrong field, which made the limit
   read narrower than it is.
8. **The placeholder lexicon is applied to four fields, not seven.**
   `falsification_attempt`, `bounded_reduction_plan`, `g1.critic_answer` and
   `pilot_recurrence_check.method` are screened; `counterexample`,
   `falsification_summary` and `evidence.quote` are not. Extending it is a
   judgement about false positives on legitimately terse text, and is
   deliberately not made in a repair pass.

## Fixtures

```text
validate_launch_administration --selftest    88 fixtures   (75 at v2.0)
render_launch_administration  --selftest     16 fixtures   (12 at v2.0)
```

Thirteen new fixtures, one per repaired predicate, plus the forgery RD-47
built, the eligibility branches, and both directions of the trend-row rule —
the ineligible row that must carry no verdict and the eligible row that must
still carry one. The count is printed by `--selftest` and is
stated here only as a delta; it is not this file's to keep current.

## What must happen next

**Two reviews, and nothing else first** — one on policy semantics, one on the
schema, validator and renderer, both against the repaired bytes in fresh
context. Until they return, v2.1 is an unreviewed amendment made by the
session that received the verdicts it responds to, and **P-34 must not be
offered on it**.
