# Final exact-manifest semantic confirmation — report

> **Non-authoritative round record.** The raw review is
> `reviews/RD-8-exact-manifest-RAW.md` and is never edited. Where this file and
> the raw review disagree about what the reviewer found, **the raw review
> wins**. Verdict words are copied, not summarised.

## The commission and the verdict

An independent reviewer read the exact bytes of all five act subjects and
answered one question: **would an owner performing these acts, having read only
the offering and the subjects it names, be surprised by anything they had just
bound?**

**`VERDICT: REVISE`.**

> **Yes. Twelve surprises, and one of them means the act would not be a knowing
> act at all.**

## The subjects are sound. The document standing between the owner and them was not.

The reviewer's own division, and it is the finding:

> The digest arithmetic is sound. All 32 module digests recompute exactly, the
> manifest's population is exactly the module set in both directions, all five
> act arguments match their named subjects, every mechanical check passes, and
> the four contract sections I was asked to read in full are unusually
> well-written — a cold reader can restate what nearly all of them bind.
>
> What is not sound is **the owner-facing offering.**

And its closing sentence:

> The failure is that the document standing between the owner and these
> subjects no longer describes them.

## S1 · The offering did not state the two open blocking defects, and the status page said it did — **closed**

**The sharpest finding, and it was mine.**

`PROJECT-STATUS.md` named the two open blocking contract defects and then said
*"the acceptance packet states them before the act phrases."* The reviewer
checked the document `AGENTS.md` routes the owner to —
`round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md` — and swept it:

| Token | Hits in the routed-to offering |
|---|---|
| `RFC10-10` | **0** |
| `RFC11-4` | **0** |
| `consumption` | **0** |
| `round-2026-08c` | **0** |
| `RD-1`, `RD-4` | **0** |

> A checker who verified the claim at `PROJECT-STATUS.md:79` by reading the
> offering would find ten imperfections and conclude the two blocking ones must
> be among them.
>
> This is the finding that converts act 1 from a knowing act into a surprised
> one, and it is the reason for the verdict.

**The reviewer was right and the diagnosis is exact — it was a routing
failure.** `FINAL-OWNER-ACCEPTANCE-PACKET.md`, which *does* state both defects
before the phrases, was written in this same session and **nothing pointed at
it.** A packet nobody is routed to is a packet nobody reads.

**Closed three ways:**

1. **`AGENTS.md`** now names `round-2026-08c/FINAL-OWNER-ACCEPTANCE-PACKET.md`
   as the owner-facing offering, and says why the previous one is stale.
2. **`PROJECT-STATUS.md`** routes there too, and separates the *offering* from
   the *ceremony* — the phrases and the five steps live in
   `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`, which wins over any
   offering.
3. **The superseded offering carries a `SUPERSEDED — 2026-08-07` banner that
   states both blocking defects in full**, so a reader arriving on an old link
   is not the reader RD-8 describes.

## S2 · The acceptance record understated act 1 by six clauses — **closed**

Under the heading *Package identity* — *"the section a reader consults to learn
what the package **is**"* — the record claimed **322 numbered clauses** and
**RFC10-1..16**, labelled *script-verified*.

The script reports **328**, and RFC10 runs to **22**. The gap is exactly the six
correction-plane clauses. §1's act-1 row narrated their addition; §3 was never
swept.

**Two derived figures in the same section were stale the same way** — RFC-0001
at 8,353 words against an actual 8,342, and the corpus at 99,067 against the
verifier's 102,623. **And the re-quote count disagreed three ways** across two
files, one of them the acceptance authority.

**Closed, and not by refreshing the numbers.** §3 now **points at the verifier
and the budget report** rather than restating them, and says why: *a figure
quoted outside its owning artifact goes stale silently* — this repository's
third verification rule, broken in the record that governs its own acceptance.
The re-quote count now has one home, §1's act-1 row.

## S3 · A binding clause selects on a key deleted from all 32 modules — **open, frozen**

**RFC11-4** instructs the compiler to select on `depends_on` / `provides_to`.
`grep -rn -F "provides_to"` over `rfcs/` returns **exactly one line: this one.**
No module carries the key — its removal was a deliberate normative change made
in this round, and the clause naming it was not swept.

> a **live dangling reference inside act 1's digest set**, of the same class
> the round spent six re-quotes eliminating. It is disclosed nowhere.

**Now disclosed** — in the acceptance packet, item 3 of act 1's imperfections.
**Not repaired:** it is a normative edit to frozen bytes. It is the one finding
RD-8 says requires a manifest churn, and it should be batched.

## S4 · An owner-attention item outlived its defect — **closed**

§7 item 10 asked the owner to rule on a stale word count in
`rfcs/RFC-0007/README.md`, offering *"accept as-is, or direct a fix + digest
regeneration + one more digest-binding review."* The figure has **zero hits in
`rfcs/`** — it was removed by the fourth re-quote and the item survived the fix.

> An owner who chose that branch would commission a review cycle for a string
> that is not in the corpus.

**Closed, struck through rather than deleted** — an owner-attention item that
was live and is not is part of the record's history.

## S5, S6 · Two disclosed imperfections were themselves stale; the offering cited a document that did not exist — **closed**

Row 6 warned about a citation fixed two re-quotes earlier. Row 10 said the
RFC10-18 repair *"has been read by no reviewer"* — three reviews have since
read those bytes. Both errors ran in the **conservative** direction, which is
the safe way to be wrong — *"but combined with S1 they establish that §3 is not
a current inventory of what is wrong, and the owner has no way to know which
rows are live."*

And the offering's act-1 row declared itself *"superseded by the 2026-08-06
closure round's owner acceptance packet"* — **a document that did not exist**.

**All three corrected**, and the superseding packet now exists and is named.

## The findings that stay open

| # | Finding | State |
|---|---|---|
| **S3** | RFC11-4 names `provides_to`, which no module carries | **Frozen**, disclosed in the packet. Requires a manifest churn |
| **S7** | Act 2's phrase names one amendment; its digest binds a file that **adopts two external bars by reference** inside CC-TEST-7. `INSTALL-RECORD.md` frames CC-TEST-7 as a *record*, not an adoption | **Open, and stated in the packet.** The substance is almost certainly benign — the pin move was an explicit owner override closing P-26. *"The surprise is structural: the act's name and its argument have different scopes, and the wider scope contains an adoption the act's name does not mention"* |
| **S8** | **Both `constrains` lists are under-inclusive against their own source clause.** RFC7-3 constrains *"anywhere in Syzygy"* and the list names four; RFC5-3 binds *"all present and future clients"* and the list names four of six later contracts. Nothing validates completeness | **Open, and it sharpens what the dependency index already declared.** The index says **[Unknown]** whether a third edge exists; RD-8 makes it **[Observed]** that the population is incomplete on the source clauses' own words. Frozen bytes; **P-21** |
| **S9** | Act 1 binds RFC-0005 text naming `FD-009` as *"binding provenance"*, and **`FD-009` resolves nowhere in a clone** — `grep -rn -F` over `decisions/` and `doctrine/` returns zero hits. CG-12 guards `_bootstrap/` **paths**; bare identifiers pass invisibly | **Open.** This is **P-15** (the founder decision log) with a concrete cost attached: a clone reader cannot discover what a clause says is binding provenance for RFC5-8's exposure-mode set |
| **S10** | README's experiences table typed Mission Control as a *"workspace operator surface"*, in the column carrying "the intent surface", "the work surface", "the map surface" | **Closed.** The cell now reads *"workspace-level operator capability — **not a fourth surface**"*, matching RFC10-1 and OVERVIEW. README cured it two paragraphs later; *"a reader who reads the table"* did not get that far |
| **S11** | `PROJECT-STATUS.md` routed act 2 to the **2026-08-05** correction block, which holds the retired argument | **Closed** — it now names the 2026-08-06 block. The cell never stated a wrong *value*, which is why CG-7e passed it: **CG-7e enumerates act-argument *copies*, and this was a *pointer*.** A gap worth remembering |
| **S12** | The offering carried **no act phrases at all**, and its imperfections sat **after** its arguments | **Both addressed by the new packet**, which states every imperfection before every phrase. The phrase-free design of the old offering was deliberate and disclosed, and RD-8 calls it *"the safer design"* — the new packet quotes the phrases and CG-7e checks every one |

## What RD-8 verified mechanically, and it is the reassuring half

- **All 32 module digests recompute exactly.**
- **The manifest's population is exactly the module set, in both directions** —
  no file unlisted, no entry without a file.
- **All five act arguments match their named subjects**, computed fresh.
- **No volatile artifact is inside act 1's digest set.**
- **Front-matter is internally consistent** across the 32.
- **The four contract sections read in full are restatable by a cold reader.**

## Disposition — criterion 12

**Criterion 12 is `EXCEPTIONS`-grade, not met and not failed.** The exact final
package received a fresh semantic review; the review found the subjects sound
and the offering stale, and every offering-side finding is now closed. **Four
subject-side findings remain open** — S3, S7, S8, S9 — and all four are stated
in the acceptance packet before the act phrases.

**A note on what this round can and cannot claim.** The corrections above were
made **after** RD-8 returned, by the session that wrote the defects. **No
independent reviewer has read the corrected routing, the corrected acceptance
record, or the new acceptance packet.** A repair pass may not be its own
confirming reviewer, so criterion 12 is not marked met on the strength of
repairs nobody has checked.
