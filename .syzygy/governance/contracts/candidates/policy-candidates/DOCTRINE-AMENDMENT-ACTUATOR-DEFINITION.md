# Proposed doctrine amendment — define *actuator* and *actuator toolchain*

> **Candidate. Proposed, not performed.** This file changes nothing. Doctrine
> is adopted, and **only the owner amends it (VIS-4)**. It is drafted here so
> the owner can approve or decline a fully specified edit rather than a
> description of one. Owner item **P-25(c)**.
>
> **Composes with** `DOCTRINE-EDITORIAL-AMENDMENT-GLOSSARY-CITATION.md`
> (P-25(a)), which qualifies doctrine's three "README glossary" citations and
> explicitly declines to define the terms those citations imply. This packet
> takes up **exactly one** of the three it names — *actuator* / *actuator
> toolchain*. It supersedes nothing: the two can be adopted in either order or
> independently, and the third undefined term, *ai-bootstrap toolchain*
> (`v1.md:98`), is still proposed by neither.

## The defect, stated precisely

`vision.md` uses **actuator** as a load-bearing noun in its Thesis — the
sentence that says what Syzygy does — and cites a glossary that does not
define it.

| Site | Text |
|---|---|
| `doctrine/vision.md:25` | "Syzygy computes and shows the difference, and harnesses the existing **actuator toolchain** to close it." |
| `doctrine/vision.md:38` | "it assumes the public **actuator toolchain** (README glossary), never one private machine." |
| `doctrine/vision.md:58` | "observed truth is machine-consumable and actually consumed by the **actuator toolchain**" |
| `doctrine/v1.md:53` | "endpoints in real **actuator** use *and* the three-axis propagation slice" |

The glossary the second site cites — `doctrine/README.md:15`, `## Glossary
(read first)` — has seven bullets and defines neither word. Its nearest
bullet names a different phrase:

> **the `/th-*` skills and claude/codex CLIs** — the designated initial
> **agent toolchain** for workers and actuators.

[Observed] That bullet is the only place in the adopted tree where the word
*actuators* appears outside `vision.md` and `v1.md`, and it uses the word
without defining it, in the course of defining something else. So a reader who
follows `vision.md:38`'s pointer finds the toolchain's designated tools, and
still cannot answer *what is an actuator* or *is the "agent toolchain" the
same thing as the "actuator toolchain"*.

[Observed] Sweep denominator: all six files of `.syzygy/governance/doctrine/`,
case-insensitive `grep -rn actuator` — five hits, the four tabulated above
plus the glossary bullet. No definition among them.

This is the defect the launch-gate administration of 2026-08-09 recorded as
finding **D3**, and it is one of the three terms P-25 already names as
"genuinely undefined anywhere reachable".

## The proposed insertion, verbatim

**Insertion site.** `.syzygy/governance/doctrine/README.md`, inside
`## Glossary (read first)`, as a new bullet placed **immediately after** the
substrate bullet that begins "**OpenSpec** — the designated initial
behavioral-specification substrate" and **before** the "**Rule identifiers**"
bullet. The site is chosen because the new bullet names the same tools by
role as the bullet above it, and reads as its continuation.

**Text to insert, exactly:**

```markdown
- **Actuator / actuator toolchain** — an **actuator** is whatever performs the
  work that Syzygy's answers generate: an agent worker, a fleet of them, or a
  human doing it by hand. The **actuator toolchain** is the existing, external
  agent-execution toolchain Syzygy harnesses rather than replaces — designated
  initially as the `/th-*` skills and claude/codex CLIs named above, working
  over the designated work-scheduling substrate. "Agent toolchain" above and
  "actuator toolchain" in vision.md name the same role. Syzygy computes and
  shows the difference between desired and observed state; the actuator
  toolchain closes it (vision.md, Thesis). Syzygy is not itself an actuator:
  it writes implementation code nowhere (VIS-5, VIS-6) and its effects reach
  code only through dispatched work (architecture.md).
```

## Why this is editorial-plus-one-definition, and the claim is reviewable

Under the normative-change workflow, "editorial" is a claim someone can check,
not a label that exempts an edit from review. The claim here is deliberately
weaker than the P-25(a) packet's, and is made in two parts.

**(1) The edit is additive and touches no existing sentence.** No adopted
sentence is amended, deleted, or reworded. No rule identifier is created,
renumbered, or retired. Nothing in `vision.md`, `v1.md`, `architecture.md`,
`trust-and-evidence.md`, or `security.md` changes. Every existing use of the
word keeps its current reading — which is the test: **if any of the four sites
tabulated above reads differently after the insertion, the claim is wrong.**

**(2) One definition is genuinely added, and that is not editorial — so it is
named rather than folded in.** A term used in doctrine's Thesis and defined
nowhere is a gap; filling it is a substantive act, however small. What the
insertion is *not* is a new obligation: every sentence in it is either a
restatement of adopted text with its citation, or a naming of the identity a
reader must otherwise guess.

- "harnesses rather than replaces" restates `vision.md`, "Not a replacement
  for its substrate": *"The spec, work-scheduling, and orchestration tools
  remain the mechanisms; Syzygy integrates and harnesses [the] toolchain."*
- "designated initially as the `/th-*` skills and claude/codex CLIs" restates
  the glossary bullet directly above the insertion point, adding no tool and
  removing none. **Beads** is designated for work scheduling by its own
  bullet, which is why this one says "working over the designated
  work-scheduling substrate" rather than naming it a second time — a
  designation restated in two places drifts.
- "Syzygy computes and shows the difference … the actuator toolchain closes
  it" is `vision.md:25`, quoted.
- "Syzygy is not itself an actuator" restates VIS-5/VIS-6's two-namespace
  write boundary and `architecture.md`'s orthogonal-plane sentence, *"whose
  effects reach code only through scheduled work."*

**The one sentence a reviewer should press on** is that identity claim:
*"Agent toolchain" above and "actuator toolchain" in vision.md name the same
role.* [Inferred] It is inferred from use, not stated anywhere in the adopted
tree — the glossary bullet says the agent toolchain is "for workers and
actuators", and `vision.md` never uses "agent toolchain". No adopted sentence
contradicts it and nothing in the corpus requires two distinct roles. But it
is an inference, and if the owner reads the two phrases as naming different
things, **this sentence must be struck and the amendment redrafted** — do not
adopt it silently on this packet's say-so.

## What this amendment deliberately does not do

- **It admits no term registry entry.** The candidate `TERM-REGISTRY.md` has
  no `actuator` entry and gains none from this packet. Its §3 admission rule
  has five conditions, one of which is a fresh-reader distinction test that
  cannot be run by the party proposing the term. The registry's own disposition
  for this word is the other arm of its rule: **the default path stops using
  it.** That arm is done — `intent/OVERVIEW.md` no longer uses *actuator*
  (2026-08-10). Doctrine keeps the word because doctrine uses it; this packet
  is what makes doctrine's use readable.
- **It does not define *ai-bootstrap toolchain*** (`v1.md:98`), the third of
  P-25's undefined terms. That one needs a separate decision about what the
  designation actually names, and guessing it here would be the same defect in
  a new place.
- **It changes no rendering, no check, and no candidate contract text.**
  [Observed] Sweep denominator: all **39** `.md` files under
  `contracts/candidates/rfcs/`, `grep -rn -i -F actuator` — **four**
  occurrences, all in rationale or roadmap prose and **none defining the
  term**: `RFC-0004/fidelity-joins-and-mappings.md:172` and
  `RFC-0004/README.md:121,202` (the co-evolution roadmap behind RFC4-29) and
  `RFC-0008/accounting-reconciliation-and-release.md:86` (the chain's honesty
  assessment). Each reads the same before and after the insertion; a defined
  term is what they have been assuming.

## If the owner adopts

1. Insert the bullet verbatim at the site named.
2. Record it in the doctrine README's amendment log with the owner's adopting
   words and the date, following the D1 precedent — as **D-next**, whichever
   identifier is free; identifiers are never reused.
3. Record the act in `.syzygy/governance/decisions/`, citing this file.
4. **Run VIS-3's fresh-reader review**, or record a reasoned decision not to.
   Unlike P-25(a), this packet does **not** claim exemption: it adds a
   definition, and VIS-3 binds at adoption and material amendment. The
   cheapest form is the one condition §3(5) of the term registry describes — a
   reader given only this bullet and the glossary bullet above it places five
   real examples correctly.
5. Close **P-25(c)**. P-25(a) — the citation qualifiers — is independent and
   stays open unless separately adopted; P-25(b), reachability, is already
   done.
