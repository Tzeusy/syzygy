# Proposed editorial doctrine amendment — the "README glossary" citation

> **Candidate. Proposed, not performed.** This file changes nothing. Doctrine
> is adopted, and only the owner amends it (VIS-4). It is drafted here so the
> owner can approve or decline a fully specified edit rather than a
> description of one. Owner item **P-25**.

## The defect, stated precisely

Adopted doctrine cites a glossary at three sites without saying which file
holds it:

| Site | Text |
|---|---|
| `doctrine/vision.md:16` | "Syzygy (see README glossary) is a specification-driven software control plane:" |
| `doctrine/vision.md:39` | "…(README glossary), never one private machine." |
| `doctrine/v1.md:98` | "substrate is the public ai-bootstrap toolchain (README glossary)." |

**The glossary exists.** `.syzygy/governance/doctrine/README.md:15` is
`## Glossary (read first)`, running to `:49`. It is the only glossary in the
repository.

**The citation still misroutes.** A reader meeting "README glossary" opens
the README they are holding — the repository root one — finds no glossary,
and concludes the reference is broken. Two independent reviews reached
exactly that conclusion, and a third then propagated "the glossary does not
exist" into five tracked artifacts as though it were established fact. The
citation did not merely fail to help; it manufactured a false finding.

The reachability half is already repaired outside doctrine: the root
`README.md` now links the doctrine glossary directly. That fixes the reader's
recovery path. It does not fix doctrine's own sentence, which still names the
wrong file by implication, and doctrine can only be fixed by the owner.

## Why this is editorial, and the claim is reviewable

Under the normative-change workflow, "editorial" is a claim someone can check,
not a label that exempts an edit from review. The claim here: **each proposed
edit adds a path qualifier to a citation and changes no obligation, no
definition, no scope, and no rule.** Read the before/after pairs below and
test it — if any pair changes what doctrine requires of anyone, the claim is
wrong and this becomes a substantive amendment.

## The three edits, verbatim

**Site 1 — `doctrine/vision.md:16`**

> Syzygy (see README glossary) is a specification-driven software control plane:

becomes

> Syzygy (see the glossary in `governance/doctrine/README.md`) is a
> specification-driven software control plane:

**Site 2 — `doctrine/vision.md:39`**

> (README glossary), never one private machine.

becomes

> (glossary, `governance/doctrine/README.md`), never one private machine.

**Site 3 — `doctrine/v1.md:98`**

> substrate is the public ai-bootstrap toolchain (README glossary).

becomes

> substrate is the public ai-bootstrap toolchain (glossary,
> `governance/doctrine/README.md`).

A path is used rather than a relative markdown link because these files are
read as often through an agent's file reader as through a browser, and a bare
path resolves in both.

## What this amendment deliberately does not fix

Three terms are cited as though glossary-defined and are **defined nowhere
reachable**:

- **"actuator toolchain"** — `vision.md:38`. The nearest glossary entry is
  "agent toolchain", which is not the same term.
- **"ai-bootstrap toolchain"** — `v1.md:98`.
- **"actuator"** — used in `OVERVIEW.md` and in this repository's own agent
  instructions.

Qualifying the citation makes these *findable as missing* instead of
mysterious, which is an improvement and not a fix. Adding definitions is a
substantive doctrine amendment with its own drafting and its own fresh-reader
review under VIS-3, and it is not proposed here.

## If the owner adopts

1. Apply the three edits verbatim at the sites named.
2. Record it in the doctrine README's amendment log with the owner's adopting
   words and the date, following the D1 precedent.
3. Record the act in `.syzygy/governance/decisions/`, citing this file.
4. VIS-3's fresh-reader review is **not** triggered if the editorial claim
   holds — it binds at adoption and material amendment. If a reviewer judges
   any edit material, run it.
5. Close P-25(a). P-25(b), reachability, is already done.
