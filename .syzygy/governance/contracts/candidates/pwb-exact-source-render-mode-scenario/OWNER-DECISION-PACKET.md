# Owner decision packet — PWB exact-source render mode

> **Inert offering.** This packet performs nothing. It presents one
> decision, records nothing, and authorizes no implementation. A commit, a
> merged pull request, a review, a manifest, silence or a general "approved"
> performs no act.

> **Candidate — binds nothing.** The package this packet describes is a
> drafted CC-REV-2 semantic delta. It would take effect only through an
> owner act over the behavior manifest below, recorded in
> `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`. Until that act,
> the 2026-09-05 specification stands unchanged.

Date: 2026-09-21 (drafted); repaired 2026-09-22 after round 1.

Round 1 returned `CONFIRM WITH EXCEPTIONS` on commit `08f980f`
(`docs/reviews/R-PWB-EXACT-SOURCE-RENDER-MODE-DELTA-RAW.md`); its three
findings are dispositioned in `SEMANTIC-DELTA.md` §Review. The repairs
touched no manifest subject, so the digest and the phrase below are the ones
that review named — but the repaired bytes need a second fresh reviewer
before the phrase is offered (verification rule 10).

Ruling this serves: row **P-81** of
`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`,
recorded in `.syzygy/governance/decisions/DECISION-HISTORY.md`. That row
already chose arm A; this package is the scenario it ordered, not a
re-litigation of it.

Behavior manifest: `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` (this directory),
eleven rows, hashing the eleven PWB behavior artifacts **as they will be
after** the four patches under `proposed/` are applied. Four rows differ
from the tree today; seven equal it.

Behavior manifest SHA-256:
`5796c1541a90a109c0259a079d2262883942d1f97ac36c733ecf2c0c28763433`

This packet wrapper is not an act subject. Once a review is retained
against this package, changing this packet retires that review.

## Why this is here

The exact-source route serves one population today: requirements belonging
to a baseline specification Git object. Every other source in the
consented content class is refused with the reason
`unconsented-source-or-provider`, although the evaluation already admitted
it, already classified it, and already holds its revision-bound identity
and content digest.

The M14 funnel measured the gap: of 278 source rows, 192 are served exactly
today and 86 are non-baseline. Of those 86, 77 were admitted as classified
blobs and 9 are withheld — seven manifests, one page, and one artifact the
record excludes [Observed,
`docs/design/POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md` and
`docs/evidence/polaris-m14-provenance-depth-funnel-2026-09-17.json`]. You
ruled arm A: reach the 77, never the 9, behind a scenario to PWB-REQ-011
and the act that follows sign-off.

The obstacle is that PWB-REQ-011's one body-reading scenario admits exactly
one population by name, and `design.md` §8 argues the route "therefore needs
no wider content class" from that population alone. Reaching the other 77
without amending both would be implementation ahead of its requirement.

## What the package changes

In the specification (PWB-REQ-011) and its supporting argument:

- the route serves **every source the evaluation admitted as a classified
  blob**, in exactly one render mode drawn from a **closed** two-mode set:
  the existing requirement-section mode for sources with requirement
  headings, and a whole-body mode for the rest;
- a source whose record outcome is **excluded** is served in **no** mode.
  That is stated as its own invariant and its own scenario, so the
  withholding does not depend on a class gate that a later change could
  widen;
- **every** mode applies the same authority, exact-object,
  secret-detection and inert-content gates to the **complete transient
  body before encoding any part of it**. No detector is relaxed, skipped or
  narrowed to a section; a failed gate leaves the body Unknown with its
  reason;
- each served mode exposes a **scroll anchor** for each reading unit a
  citation can name. The anchor is presentation only: it removes, narrows
  and reorders nothing the route serves without it, and it never enters,
  replaces or qualifies any source, claim or narrative anchor identity;
- each served route's mode, each source identity and each refusal's reason
  are recoverable, **per rendered tuple**, from the same evaluation in the
  machine answer — which is how the parity sweep extends over the anchor
  parameter, as your ruling requires;
- `design.md` §8 gains the argument for the wider *source* population inside
  the same content class, and `CAPABILITY-COVERAGE.md` row 10 restates the
  obligation it covers. `GOVERNING-DEPENDENCIES.md` is regenerated.

## What the package does not change

No content class widens: the route still reads only what the performed
consent covers. The nine withheld sources stay digest-only, keep their
identity and digest in both channels, and leave the source denominator
unchanged. No detector changes. PWB-REQ-014 is **not** amended — a scroll
anchor is a coordinate, and the proposed text keeps coordinates out of
anchor identity rather than carving an exception. PWB-REQ-020 is **not**
amended — the parity obligation lands inside PWB-REQ-011's own text.
PWB-REQ-003, -005, -006 and -015 are untouched. The machine answer's shape
is unchanged. The coverage population stays 31 and the totals stay 25
covered, 6 lawfully out of scope, 0 Unknown. The full quoted current and
proposed text is in `SEMANTIC-DELTA.md`; the exact bytes are the patches
under `proposed/`.

Two things your ruling sequenced elsewhere are deliberately **absent**: the
PWB-REQ-015 delta (P-81 Q5) and the PWB-REQ-002 delta (P-82). Drawing
either here would make this change two categories.

## What it buys and what it costs

Served sources move from 192 of 278 to **269 of 278** [Inferred — a sum of
the funnel's measured 192 and 77; the rendered figure is what the
implementation's measurement reports]. The nine that remain are the nine you
ruled must remain.

Cost, all of it after the act and none of it in this package: the route's
class gate, a second render mode, the anchor parameter, the reachability
and parity sweeps extended over it, and the mutation proof for the new
falsifier classes. The sites are enumerated in `IMPACT-LEDGER.md`.

Page size is the risk worth naming. The route serves a transient body per
request, so it does not enlarge the Polaris page itself; the anchor
parameter adds bytes per internal link on the tailnet form. The page sits
inside the response ceiling today after the P-63 trim, and a response-ceiling
breach serves nothing and logs nothing, so the implementation bead must
measure rather than assume [Inferred].

## The decision

**Question:** should this package be reviewed and then offered for
sign-off as drafted?

**(a) Yes, as drafted** (recommended). A fresh-context review runs against
`REVIEW-BRIEF.md`; findings are repaired; the phrase below is offered with
a regenerated manifest. Nothing renders differently until the act is
performed and an implementation bead lands.

**(b) Yes, but with a different mode vocabulary.** The two modes are closed
by design, and a third mode later needs its own amendment. If you want a
third mode now — a table mode, say — say so before the review, because
adding one afterwards retires it.

**(c) No.** The route keeps its one population, the 86 non-baseline sources
stay digest-only, and P-81's slices 1–2 do not land.

A second, smaller choice, if you answer (a) or (b): **which amendment lands
first**, this one or the scoped-attributes package. They are independent in
meaning and collide on one generated line only. Whichever is second
regenerates that line and its manifest before its phrase is offered; the
ordering is yours and neither depends on the other.

One caveat on that ordering, raised by the round-1 review as F3 and worth
your eye because no tool prevents it: if the *other* package's
specification patch is taken alone — cherry-picked before the rest of its
package is ready — no patch tool objects, and the generated dependency file
is left naming a digest for a specification that is not on disk. This
package's `--check` now detects that tree, so it cannot pass silently, but
detection is not prevention. The safeguard is that each amendment lands
whole, with its regeneration step, which is what the migration plan in
`SEMANTIC-DELTA.md` requires.

Silence, a partial answer, a commit or a merge performs nothing; the
2026-09-05 package stays the PWB authority in every case until an act says
otherwise.

## Not yet offered: the sign-off phrase

The behavior act phrase for this manifest would be:

```
SIGN OFF PWB EXACT-SOURCE RENDER-MODE AMENDMENT: 5796c1541a90a109c0259a079d2262883942d1f97ac36c733ecf2c0c28763433
```

It is registered so that the governance checks see it go stale, but it is
**not offered** in this packet: no fresh-context review has been run on
these bytes yet. If you reply with this phrase now, no recorder exists that
would accept it, and nothing is performed.

## What happens after a "yes"

1. **Review.** A fresh-context reviewer, with only the package, the
   governing references and `REVIEW-BRIEF.md`, returns one exact verdict.
   Raw output is retained verbatim; findings are dispositioned in
   `SEMANTIC-DELTA.md` §Review; repaired bytes need a new reviewer. Round 1
   is done and repaired; round 2 is the outstanding step.
2. **Offer.** The manifest is regenerated over the repaired bytes and the
   phrase above is re-derived from it — never transcribed — and offered.
3. **Act.** A dedicated recorder validates the phrase against the manifest
   bytes, applies the four patches into `openspec/` with the builder's
   `--apply --at-adoption`, confirms every manifest row now hashes the tree,
   writes the dedicated act record and the aggregate section of
   `ACCEPTANCE-ACT-RECORD.md`, and registers the successor chain link, in
   one change.
4. **Implementation.** Only then does a bead open under the pursuit epic.
   Its measurement is what confirms the 269-of-278 figure and the page-size
   effect.
