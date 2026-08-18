# C2 population report — normative modals and their owners

> **Retained sweep output, never authority.** Written 2026-08-18 (round
> 2026-08j) to settle Administration 1's **C2 Unknown**, whose recorded
> settlement is: *"Run and retain a full, current C2 population report
> over README.md, AGENTS.md, and every governance Markdown/YAML artifact,
> enumerating each normative 'should,' its sole owner, and every
> conflict-resolution rule."* The sweep is
> [`sweep_c2_normative_population.py`](sweep_c2_normative_population.py)
> (this directory) — re-run it rather than trusting this page's copy; the
> run below is valid for the working tree it names.

## The run (2026-08-18, working tree at the repair-pass commit)

```text
C2 normative-modal population sweep
population: 425 file(s), 132389 line(s); 8276 line(s) carry a normative modal

| owner class | files | modal lines |
|---|---|---|
| historical/frozen (round trees, history, launch-gate raw) | 245 | 4459 |
| adopted doctrine | 6 | 98 |
| owner-approved craft | 10 | 100 |
| substrate lock (record) | 1 | 6 |
| owner decisions and acts | 24 | 199 |
| accepted contracts (Waves A/B) | 30 | 1121 |
| generated views (presentation, never authority) | 4 | 30 |
| candidate contracts and policies | 103 | 2230 |
| root operating docs (README/AGENTS) | 2 | 33 |
```

Over-counting is deliberate: a modal inside a quotation, code fence, or
negation still counts, because a *denominator* must bound the population
from above (verification rule 9). The number to quote is therefore
"8,276 modal-carrying lines examined," never "8,276 rules."

## How sole ownership is decided — the conflict-resolution rules

Each rule is quoted from, and owned by, the artifact cited beside it.

1. **The authority table** (`AGENTS.md` §"Where authority lives",
   `README.md` §"What is authoritative here") assigns each *question* one
   owning home; both tables carry the qualifier that they are operating
   procedure/presentation, never themselves authority.
2. **Identifier ownership**: "Cite by identifier … Identifiers are
   amended in place or retired, never renumbered" (`AGENTS.md`). A clause
   ID (`VIS-2`, `CC-SPEC-8`, `RFC3-16`) has exactly one defining artifact;
   `05-CONTRACT-INDEX.yaml` resolves contract clauses mechanically and
   `check_governance.py` CG-25 requires every check to name its owning
   rule.
3. **Record-beats-pointer banners**: every routing/status page carries its
   own subordination clause — e.g. `PROJECT-STATUS.md`: "where they
   disagree the record wins and this page is stale";
   `decisions/README.md`: "where this page disagrees with one of them,
   that file wins."
4. **Generated views decide nothing**: "treat a draft, candidate, index,
   summary, or generated view as authority" is a hard prohibition
   (`AGENTS.md`); each generated file's own banner repeats it.
5. **Historical/frozen material is off the authority path**: round trees,
   `history/`, and raw review bytes "never authority" (`AGENTS.md` §Task
   routing) — 245 of the 425 files, disqualified as owners by class.

Under these rules, class membership plus identifier ownership gives each
active normative line exactly one owner *by construction* for classes
1–6 of the table; the classes that could not own a rule (generated,
historical) are exactly the classes the rules above disqualify.

## The known residual, stated rather than hidden

Three advisory check rules live today only in `check_governance.py`
prose plus the **candidate** knowledge-hygiene policy: CG-20, CG-21,
CG-27 (each prints its own downgrade note naming this). C2's fails-when
clause — "a rule lives only inside a validator" — matches them, and the
open queue row **P-12** is the decision that would give them an
authoritative home. This was disclosed before Administration 1 and
remains the honest answer: the C2 residual is one owner decision wide,
not unbounded.

## What this report does not claim

It does not claim that no two artifacts *state* overlapping rules — the
duplication question is a reading judgment this enumeration makes
tractable (start with the two smallest active classes: doctrine's 98 and
craft's 100 modal lines). It claims only what the sweep measured: the
population is 425 files / 8,276 modal lines, every file classifies into
exactly one owner class, and the conflict rules between classes are the
five quoted above.
