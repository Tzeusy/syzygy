# D3 coined-term report — enumeration, first use, definition site

> **Retained sweep output, never authority.** Written 2026-08-18 (round
> 2026-08j) to settle Administration 1's **D3 Unknown**, whose recorded
> settlement is: *"A generated D3 report enumerating every coined term
> from the two prescribed populations, its first default-path use,
> definition site, and ordinary-language justification."* The sweep is
> [`sweep_d3_coined_terms.py`](sweep_d3_coined_terms.py) (this
> directory) — re-run it rather than trusting this page's copy; the run
> below is valid for the working tree it names. The standing per-term
> mechanical companion is `check_governance.py` **CG-23** (report-only).

## The run (2026-08-18, working tree at the repair-pass commit)

```text
D3 coined-term sweep
population: 41 term(s) (registry 31, glossary remainder), route set 6 file(s), 961 line(s)

| term | definition site | first default-path use |
|---|---|---|
| Project | TERM-REGISTRY.md T-01 (candidate) | `README.md:27` |
| Governance root | TERM-REGISTRY.md T-02 (candidate) | — not used on the default path |
| Project Genome | TERM-REGISTRY.md T-03 (candidate) | `.syzygy/intent/OVERVIEW.md:247` |
| Capability | TERM-REGISTRY.md T-04 (candidate) | `PROJECT-STATUS.md:23` |
| Requirement | TERM-REGISTRY.md T-05 (candidate) | — not used on the default path |
| State plane | TERM-REGISTRY.md T-06 (candidate) | — not used on the default path |
| Desired state | TERM-REGISTRY.md T-07 (candidate) | `.syzygy/intent/OVERVIEW.md:43` |
| Proposed state | TERM-REGISTRY.md T-08 (candidate) | — not used on the default path |
| Observed state | TERM-REGISTRY.md T-09 (candidate) | `.syzygy/intent/OVERVIEW.md:44` |
| Inferred state | TERM-REGISTRY.md T-10 (candidate) | — not used on the default path |
| Execution state | TERM-REGISTRY.md T-11 (candidate) | `.syzygy/intent/OVERVIEW.md:45` |
| Historical state | TERM-REGISTRY.md T-12 (candidate) | — not used on the default path |
| Claim | TERM-REGISTRY.md T-13 (candidate) | `AGENTS.md:161` |
| Evidence | TERM-REGISTRY.md T-14 (candidate) | `.syzygy/intent/OVERVIEW.md:18` |
| Claim epistemic label | TERM-REGISTRY.md T-15 (candidate) | — not used on the default path |
| Unknown | TERM-REGISTRY.md T-31 (candidate) | `README.md:44` |
| Rendering tier (also called "evidence tier") | TERM-REGISTRY.md T-16 (candidate) | — not used on the default path |
| Warrant | TERM-REGISTRY.md T-17 (candidate) | — not used on the default path |
| Challenge | TERM-REGISTRY.md T-18 (candidate) | — not used on the default path |
| Contradiction | TERM-REGISTRY.md T-19 (candidate) | — not used on the default path |
| Gap | TERM-REGISTRY.md T-20 (candidate) | — not used on the default path |
| Source snapshot | TERM-REGISTRY.md T-21 (candidate) | — not used on the default path |
| Evaluation | TERM-REGISTRY.md T-22 (candidate) | — not used on the default path |
| Observation record | TERM-REGISTRY.md T-23 (candidate) | — not used on the default path |
| Aligned | TERM-REGISTRY.md T-24 (candidate) | — not used on the default path |
| Converged | TERM-REGISTRY.md T-25 (candidate) | — not used on the default path |
| Reconciliation | TERM-REGISTRY.md T-26 (candidate) | `.syzygy/intent/OVERVIEW.md:184` |
| Mission | TERM-REGISTRY.md T-27 (candidate) | `README.md:53` |
| Autonomy envelope | TERM-REGISTRY.md T-28 (candidate) | — not used on the default path |
| Attention item | TERM-REGISTRY.md T-29 (candidate) | — not used on the default path |
| Context packet | TERM-REGISTRY.md T-30 (candidate) | — not used on the default path |
| Syzygy | doctrine/README.md §Glossary (adopted) | `README.md:1` |
| Owner | doctrine/README.md §Glossary (adopted) | `README.md:91` |
| Governed project | doctrine/README.md §Glossary (adopted) | `.syzygy/governance/doctrine/README.md:25` |
| .syzygy | doctrine/README.md §Glossary (adopted) | `README.md:30` |
| openspec | doctrine/README.md §Glossary (adopted) | `README.md:79` |
| Polaris | doctrine/README.md §Glossary (adopted) | `README.md:50` |
| Trajectory | doctrine/README.md §Glossary (adopted) | `README.md:51` |
| Orrery | doctrine/README.md §Glossary (adopted) | `README.md:52` |
| OpenSpec | doctrine/README.md §Glossary (adopted) | `AGENTS.md:43` |
| Rule identifiers | doctrine/README.md §Glossary (adopted) | `.syzygy/governance/doctrine/README.md:45` |

20 term(s) never appear on the default path; counts computed by this script, never transcribed.
```

## Reading the table

- **Ordinary-language justification** is carried by the populations
  themselves, per entry: the term registry's core table pairs each term
  with "the plain question it answers", and each `T-nn` entry body
  states why ordinary language would not do; the doctrine glossary
  defines each codename inline. This report points there rather than
  restating 41 justifications (the registry owns them; restating would
  re-open the door the pointer closes).
- **Defined-before-use, as the route set implements it:** every route-set
  entry file carries a glossary pointer in its opening sections —
  `README.md` §"Start here" routes unfamiliar words by kind,
  `AGENTS.md` has the "What a term means" routing row, and
  `doctrine/README.md` *is* the adopted glossary, placed first in its
  own file ("read first"). A term's first default-path use is therefore
  at most one routed hop from its definition. Whether that satisfies
  D3's bar is the next administrator's judgment; this report supplies
  the enumeration that judgment needs.
- **Over-reporting is deliberate**: matching is a plain phrase match, so
  ordinary-word shadowing (Project, Evidence, Claim, Unknown, Gap …)
  counts ordinary uses as uses. The safe direction for "used before
  defined" — and the shadowing question itself is D3's second limb,
  already tracked per-term by CG-23's exemption notes.
- **20 of 41 terms never appear on the default path.** `[Observed]`
  That is half the vocabulary living only in contract/policy depth —
  consistent with a registry built for drafting contracts rather than
  for the front door, and worth re-checking after Capability 1 is
  authored (its specification will pull facet and state-plane vocabulary
  onto more-travelled paths).

## Standing

This report settles D3's *enumeration* question. The registry itself
remains a candidate (its approval as working drafting vocabulary is
P-16's, ruled or not as the queue records); nothing here adopts a term.
