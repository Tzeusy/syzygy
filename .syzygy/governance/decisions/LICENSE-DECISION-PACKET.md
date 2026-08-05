<!-- Tracked copy created 2026-08-05 (human-clarity refactor round, P-14 packet promotion).
     Source: _bootstrap/knowledge-refactor/LICENSE-DECISION-PACKET.md (founder-local history).
     The license choice is the owner's and remains PENDING. -->

# LICENSE-DECISION-PACKET — knowledge-architecture refactor pass, §10.3

**Directive:** `KNOWLEDGE-ARCH-REFACTOR-DIRECTIVE.md` @ `01d25994…`, §10.3 —
*"If no licence exists, produce a concise owner decision packet… Do not choose
the licence without owner approval."*

**Status: no licence is declared, and this packet does not choose one.** It
lays out the four candidates the directive names, against what this project
has already decided about itself.

> **[Unknown] — this is not legal advice.** The framing below is engineering
> and governance reasoning, not a legal opinion. A licence choice with real
> consequences deserves review by someone qualified, which no participant in
> this pass is.

---

## 1. Why the choice is not obvious here

Most projects pick a licence by habit. Three properties of *this* project make
the default answer less automatic:

1. **It reads other people's repositories.** Syzygy observes governed
   projects, ingests their structure and evidence, and writes into their
   `openspec/**` and `.syzygy/**`. Whether a copyleft obligation could reach a
   *governed* project — rather than only Syzygy itself — is the question the
   owner most needs answered, and it is the one this packet cannot answer.
2. **Its output includes governance artifacts it authors.** Doctrine drafts,
   spec deltas, and records written *by* Syzygy into another repository are
   output, not derivative works of the tool — under all four candidates, on
   the ordinary reading. But "on the ordinary reading" is doing real work in
   that sentence.
3. **It is designed for agent consumption.** Machine-queryable endpoints are
   first-class product surface. A licence that constrains network use
   (AGPL-3.0) interacts with that differently than one that does not.

## 2. The candidates

| | **Apache-2.0** | **MIT** | **MPL-2.0** | **AGPL-3.0** |
|---|---|---|---|---|
| Permissiveness | Permissive | Permissive, minimal | Weak copyleft, **per-file** | Strong copyleft, **incl. network use** |
| Patent grant | **Explicit** | None | Explicit | Explicit |
| Copyleft reach | None | None | Modified MPL files only | The whole work, and users served over a network |
| Adoption friction | Low | Lowest | Low–moderate | **Highest** — many organisations forbid it |
| Contribution terms | Well-understood | Well-understood | Well-understood | Well-understood |
| Fits "read others' repos" | No obligation on the observed project | Same | Same | **The question to resolve** — the observed project is not a derivative work on the ordinary reading, but this is exactly where advice is worth buying |

## 3. What the project has already decided that bears on this

Not new arguments — existing commitments that constrain the choice:

- **Comprehensible truth over convenience.** A licence chosen to maximise
  adoption at the cost of the project's stated purpose would contradict the
  ranking doctrine already fixes.
- **The public repository must tell the same story as the founder's machine.**
  That is a transparency commitment; it is not itself a copyleft argument, but
  it sits closer to AGPL's spirit than to MIT's.
- **Agents are first-class consumers with the same truth guarantees as the
  owner.** If Syzygy is ever offered as a hosted service by someone else,
  AGPL-3.0 is the only candidate that would compel that operator to publish
  modifications.
- **No stack is chosen.** So no ecosystem licence convention applies yet —
  the choice is not being forced by a dependency.

## 4. The trade in one line each

- **Apache-2.0** — maximum adoption with patent protection. Choose if you want
  Syzygy used everywhere, including inside companies that would fork it
  privately. *The conventional default for infrastructure.*
- **MIT** — maximum adoption, minimum text, **no patent grant**. Choose only
  if the patent gap is genuinely acceptable; for a tool this structural, it
  probably is not.
- **MPL-2.0** — improvements to Syzygy's own files come back; anything built
  around it does not have to. Choose if the goal is protecting the core
  without constraining users.
- **AGPL-3.0** — a hosted competitor must publish its modifications. Choose if
  Syzygy-as-a-service by others is a real concern and adoption friction is an
  acceptable price. **Note the friction is real**: many organisations forbid
  AGPL dependencies outright, which would exclude exactly the engineering orgs
  this tool is aimed at.

## 5. What this packet cannot tell you

Stated so the gaps are not mistaken for coverage:

- **[Unknown]** Whether any copyleft obligation could reach a *governed
  project's* repository through Syzygy's writes. The ordinary reading is no —
  Syzygy's output is not a derivative work of Syzygy — but this is the single
  question where being wrong is expensive, and it wants a lawyer, not a
  reviewer.
- **[Unknown]** Whether the owner intends a hosted offering. AGPL's case rests
  almost entirely on that, and it is not recorded anywhere in the decision log.
- **[Unknown]** Contributor-agreement posture (DCO, CLA, or neither), which
  interacts with the licence and is a separate decision.
- **[Observed]** No licence file exists in the repository today; `CONTRIBUTING`
  correctly states that external contributions cannot currently be accepted.

## 6. What happens on a decision

Adding a licence is an owner act with ordinary mechanics: the `LICENSE` file,
a `README` line, and a `CONTRIBUTING` update land in **one change** (the
same-logical-change rule), and the decision is recorded in the owner-decision
log with its rationale — including, if AGPL is chosen, the adoption-friction
trade being accepted knowingly.

**This pass proposes nothing and chooses nothing.**
