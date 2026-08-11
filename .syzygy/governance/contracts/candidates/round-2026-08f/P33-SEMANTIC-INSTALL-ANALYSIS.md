# P-33 — the Wave A install shape, analysed by semantic class

> **Analysis, not a decision.** P-33 is the owner's, and this file rules
> nothing. It exists because the owner charter of 2026-08-11 (§7) directed
> that the packet be rebuilt on **what the material is**, not on where it
> currently sits: *"Do not recommend a vague `contracts-companion/` bucket
> merely because the materials currently sit near the contracts."* The
> packet the owner reads is
> `../../../decisions/WAVE-A-INSTALL-SHAPE-DECISION.md`; this is its
> supporting measurement.

## 1. The material, typed

The first wave act's install step (acceptance record §2 step 3) copies six
kinds of thing into `.syzygy/governance/contracts/`. They are three
different types wearing one label:

| Material | What it actually is | Where the charter's typing sends it |
|---|---|---|
| `rfcs/**` (the manifest's modules) | **accepted normative contract content** | `contracts/rfcs/` — already correct |
| `wave-manifests/WAVE-*.txt` | **integrity-bearing membership** — which modules an act bound, at which digests | with or attached to the owner-act record, digest exact |
| `ACTIVE-CONTRACT-MANIFEST.txt` (39 rows) | integrity-bearing membership, **for a package no single act accepts** | same — but see §4 below, it is P-33's second question |
| `history/**` | **historical rationale** — why a clause reads as it does, rejected alternatives, answered questions | git history, or one explicitly named historical lane; **never accepted contract content** |
| `matrix-rows/**` | **review evidence** — the RFC-0003 clause census | same as `history/` |
| `CONTEXT-BUDGET-REPORT.md`, `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` | **generated current measurements** | a derived home (`.syzygy/cache/` or equivalent); rebuildable by definition |

Typed this way, exactly **two** of the six belong in an accepted-contract
home, and RFC3-15's `contracts/` row — which says the home holds accepted
contract content *exclusively* — is right to refuse the other four.

## 2. The measurement that decides the cost of every arm

The reason the companions were copied at all is that the modules **link
into them**. Swept over the whole 39-module candidate corpus, counting
code-span path references:

| Target | Wave A | Wave B | C/D |
|---|---|---|---|
| `history/…` | **19 of 19 modules**, 40 references | **11 of 11 modules**, 28 references | 6 modules, 8 references |
| `matrix-rows/…` | 1 module, 1 reference | — | — |
| `CONTEXT-BUDGET-REPORT.md` | 3 modules, 3 references | 3 modules, 4 references | 2 modules, 2 references |
| `03-…-COMPACTION-REPORT.md` | — | 1 module, 1 reference | — |

Method: regex over code-span path references in every `.md` under
`contracts/candidates/rfcs/`, denominator 39 modules (19 Wave A, 11 Wave B,
9 deferred). The figure that matters: **every module of both launch-path
waves links into the historical lane** — 68 references across the 30
modules an owner is about to accept. `[Observed]`

This is why the question is not "where should companions live" but "what
happens to 68 references in 30 confirmed modules."

## 3. The eight questions, answered

**1. Which artifacts are required to interpret the accepted contract?**
None of the four. Every clause is normative on its own text; `history/`
carries *why*, not *what*. The dependency is **navigational**, not
semantic: a reader who cannot open `RFC-0002-history.md` still reads
RFC-0002 correctly, and finds a broken link where a rationale pointer was.

**2. Which artifacts are required only to prove how it was reviewed?**
`matrix-rows/` entirely; `history/` substantially (rejected alternatives,
answered §8 questions); the reviews under `round-2026-08*/reviews/`, which
the ceremony does **not** copy and should not.

**3. Which artifacts are rebuildable?** `CONTEXT-BUDGET-REPORT.md` and
`03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` — both generated, both with
`--check` regeneration guards today. The manifests are generated too. Only
`history/` and `matrix-rows/` are authored prose that no generator can
reproduce.

**4. Which artifact owns the acceptance membership and digest?** The wave
manifest for each act, and the owner-act record that quotes it. This is
already the ceremony's shape and it is the correct one; nothing in P-33
should move it.

**5. What remains clone-visible after installation?** Everything: the
candidates tree is not deleted by any act (the ceremony says so explicitly
for topology and installs by copy, never move). So the historical material
is clone-visible **whether or not it is also copied** into the governed
tree. This is the load-bearing fact behind the whole question: the copy
does not preserve access to the rationale — the candidates tree already
does — the copy preserves **the resolution of a relative link**.

**6. Which links resolve after installation?** Under the ceremony as
written, all of them, because the companions are copied to exactly the
paths the `../../` references land on. Under any arm that moves the
companions elsewhere, **none of the 68** resolve without rewriting the
references.

**7. Does the chosen shape require a Wave A contract amendment?**
**Every arm does.** This is the analysis's main finding, and it is not
stated in the current packet:

| Arm | Modules whose bytes move | Wave A confirmation | Wave B confirmation |
|---|---|---|---|
| (1a) companions outside `governance/` | 19 A + 11 B (rewrite 68 refs) | retired | retired |
| (1b) widen RFC3-15's `contracts/` cell | **1** (RFC-0003's homes module) | retired | **survives** |
| (1c) drop the copies, repoint at candidates | 19 A + 11 B | retired | retired |
| (1d) mint `contracts-companion/` **inside** `governance/` *(current recommendation)* | **1 + 19 A + 11 B** — the new category is an RFC3-15 amendment **and** every `../../history/` reference must be rewritten to reach it | retired | retired |
| (1e) type the cell: a closed enumeration of three occupants | **1** (RFC-0003's homes module) | retired | **survives** |
| (1f) install-time link rewriting | 0 accepted bytes — **rejected**, see below | — | — |

The current recommendation **(1d) is the most expensive arm in the space**,
and the packet does not say so. It is an RFC3-15 amendment *and* a 68-
reference rewrite, because a category minted at
`governance/contracts-companion/` is not where the `../../history/`
reference inside an installed RFC-0002 README lands. That cost belongs in front of
the owner before the ruling, not after it.

**(1f), named so the space is visibly searched, and rejected:** let the
ceremony rewrite the references while copying, so accepted bytes stay put
and installed bytes resolve. Rejected because the ceremony's own invariant
is *"Installation, bytes unchanged"* verified by `sha256sum -c`: an
installed byte that differs from the accepted byte makes the digest
verification meaningless, which is the one thing the act must not trade.

**8. If so, which confirmation is retired and what re-review is needed?**
Under (1b) or (1e): the RD-31b `VERDICT: CONFIRM` on Wave A argument
`8972d963…` is retired, because one Wave A module's bytes move and the
wave manifest's digest with them. The required re-run is **one fresh
exact-package review of the regenerated Wave A argument** — the same gate
RD-31b itself was, run once more on the new bytes. Wave B's `193e3c1e…`
and RD-32c's confirmation are untouched, because no Wave B module moves.

Under (1a), (1c) or (1d): **both** confirmations retire and **both**
exact-package gates re-run.

## 4. The second question — the 39-row manifest at the first act

`ACTIVE-CONTRACT-MANIFEST.txt` is integrity-bearing membership for a
39-module package, installed by an act that accepts 19 modules. Typed, the
defect is precise: a membership record whose scope is wider than the act
that installs it is **not** membership, it is an inventory, and an
inventory in the accepted tree reads as a claim of acceptance.

The two drafted arms — (2a) defer the install to the final act, (2b)
install with a generator-written banner naming which waves are bound —
remain the arms. Typing adds one observation: under the launch posture,
**there is no final wave act on the offer path**. Waves C1/C2/D1/D2 are
deferred, so (2a) does not mean "install later", it means "install never,
while the posture stands". If the owner takes (2a), the package-identity
record simply does not exist in the governed tree for the foreseeable
future, and that should be stated as the consequence rather than discovered
later. `[Observed — DEFERRED-WAVE-POSTURE.md]`

## 5. What this analysis recommends, and does not

`[Inferred]` — **(1e)**, the typed closed enumeration: amend RFC3-15's
`contracts/` cell to name exactly three occupant classes — accepted
contract modules, integrity-bearing manifests, and one explicitly named
**non-normative resolution lane** holding `history/`, `matrix-rows/` and
the two generated reports, each outside every digest set and each carrying
its own "nothing here binds" statement.

It is recommended for three reasons and against one:

- it moves **one** module instead of thirty, and retires **one**
  confirmation instead of two;
- it keeps every reference resolving without touching a single accepted
  reference;
- it says out loud what the tree contains, which is the thing RFC3-15's
  "exclusively" exists to protect — a closed enumeration is not a stretched
  category;
- **against it:** the charter's typing would send historical rationale and
  generated measurements *out* of the contract home entirely, and (1e)
  keeps them in, under a name. That is a real compromise with the typing
  principle, and the honest reason is the 68 references, not a principle.
  An owner who values the clean type boundary above the reference cost
  should take (1a) or (1c) with the two-wave re-review priced in.

Prefer the literal names the charter names — `history`, `reviews`, `cache`,
`decisions`, `records`. `contracts-companion` is invented packaging
vocabulary for a thing that already has two ordinary names, and it is the
one arm whose cost the packet understated.

**Nothing here is applied.** No module is edited, no ceremony text is
changed, and no arm is drafted into the acceptance record. The ruling is
P-33's, and the Wave A offer waits on it.
