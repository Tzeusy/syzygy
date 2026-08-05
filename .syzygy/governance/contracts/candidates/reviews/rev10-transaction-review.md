# REV10 acceptance-transaction review (directive §13.5)

**Reviewer scope:** is the acceptance model truthful and executable — bootstrap owner adoption versus independently verified effective status honestly distinguished; digests, homes, acts, and correlation state coherent?

**Verdict: EXCEPTIONS** (5 located; 2 substantive, 3 mechanical). The core repair is sound — the rev9 defect is genuinely gone and all four digests verify — but the supersession is not clean, and RFC3-16(b) and RFC3-16(c) disagree on the consequence of state (1).

---

## Check 1 — Digest verification, by script

[Observed] From the final-prespec root:

```
sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt   → 32/32 OK, no failures
sha256sum ACTIVE-CONTRACT-MANIFEST.txt      → b77374b8080a7082f486248c05b54e38cdd460f30a6d7da627f026b57fb0d6fb
```

That is byte-exact to the §1 act-1 phrase argument (`FINAL-…-RECORD.md:15`). `find rfcs -name '*.md' | sort | wc -l` → **32**, matching the manifest line count exactly — no unlisted module, no listed-but-absent file.

The other three acts, verified against their **real** homes:

| Act | Bound digest | Recomputed against | Result |
|---|---|---|---|
| 2 CC-TEST-2 | `aa2d6353…52821` | `.syzygy/governance/policies/craft-and-care/testing-and-verification.md` | match |
| 3 topology | `0d34d1b5…61560` | `_bootstrap/rfc-phase/topology/BUNDLE-MANIFEST.md` | match |
| 4 overview | `42de2eb1…24240` | `.syzygy/intent/OVERVIEW.md` | match |

[Observed] `scripts/verify_final_prespec.py` → **PASS — all checks clean**, 322 numbered clauses, with the RFC-0001 oversize and the corpus-band miss printed as explicit notes rather than suppressed. §6's mechanical claim is true as written.

**No digest exception.** The manifest's own regeneration command (`find rfcs -name '*.md' | sort | xargs sha256sum`) is scoped to `rfcs/` only, which means §1's exclusion of `history/`, `fixtures/`, and the reports from act 1 is **mechanically enforced by the generator**, not merely asserted in prose. That is the right construction.

## Check 2 — Truthfulness under RFC3-16(c)

[Observed] The rev9 defect is real and locatable. `FOUNDATIONAL-RFC-ACCEPTANCE-RECORD.md` §2 states flatly:

> That committed act record *is* the effective status

[Observed] The rev10 record does **not** reproduce it, in any wording. `FINAL-…-RECORD.md:58-75` instead says the record "establishes an **owner-adopted bootstrap act**… from which effective status *for human governance* is read" — qualified — and then names the defect explicitly: *"every tree-resident record — including this committed act record — lies within the untrusted actor class's write reach, so Syzygy never claims the act is independently verified."*

I grepped the whole record and the whole 32-module corpus for unqualified "is the effective status" constructions and for `Status:.*Accepted` self-declarations. Clean in both. RFC3-16(c)(1) closes the same hole at the clause level, naming the specific artifact — *"including a committed acceptance-act record under `.syzygy/governance/decisions/`"* — and violation case 14 encodes all three failure modes (render-as-verified; committed-record-as-verification; correlation-by-stamp-edit). The commits/tags-never-sufficient rule is preserved in three independent places (record §2; RFC3-16(b); RFC3-16(c) bullet 4), satisfying OD-R10-5's "preserved owner decision."

**Check 2 passes.** The gap is rendered honestly and the A9 render vocabulary is fixed verbatim ("owner-adopted (bootstrap, uncorrelated)"; never "verified").

## Check 3 — Executability of the five steps

[Observed] Walked act 1 as if performed tomorrow. Steps 1, 2, 4, 5 are executable: the phrase is exact, step 2's script is the one I just ran, `.syzygy/governance/decisions/` **already exists** (contains `SURFACE-DECISION-RECORD.md`), so `ACCEPTANCE-ACT-RECORD.md` is a create-in-place, and step 5's SHA-mirror-afterwards ordering respects CT-027. Acts 2 and 4 bind content already committed at existing canonical homes — verified present and digest-matching. Act 5's D3 mechanics (`DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md:45-51`) are executable: two verbatim insertions, both anchor sentences quoted, amendment-log entry per the D1 precedent, one commit + tag, and it correctly self-classifies as a state-(1) bootstrap act.

**Two step-3 defects — E2 and E3 below.**

## Check 4 — Independence and supersession

Act independence in the abstract is well drawn: §1's preamble and each row's "Unchanged from rev9" wording make clear no act implies another, and act 5 is explicitly marked **Optional** with RFC-0010/0011 stated not to depend on it. Scope exclusion for act 1 is explicit and generator-enforced (Check 1).

**But the rev9→rev10 supersession is not clean — E4 below.**

## Check 5 — Status headers, all 32 modules

[Observed] Extracted the `**Status:**` block from every one of the 32 files. All 32 carry the two-state self-declaration; **none** self-declares acceptance. Two variants exist, and the split is correct rather than sloppy: the 8 package README index files say "binding **each module file's** exact content digest," the 24 module files say "**this file's**." Line-wrap differs across files; the sentence does not. No exception.

## Check 6 — RFC3-16(c) internal coherence

This is where the substantive finding is. See E1.

---

# Exceptions

### E1 — RFC3-16(b) and RFC3-16(c) assign different consequences to the same state, and the record states only the favorable half
**Location:** `rfcs/RFC-0003/governance-homes-and-owner-acts.md:271-277` (RFC3-16(b) *Bootstrap correlation*) against `:351-353` (RFC3-16(c) final bullet) and `:281-290` (*Effect when the predicate fails*); mirrored at `FINAL-…-RECORD.md:58-75`.

[Observed] RFC3-16(b) says bootstrap artifacts "render with their gap stated honestly (the A9 posture), not as verified" — a **rendering** obligation, no blocking.

[Observed] RFC3-16(c)'s final bullet routes the same artifacts somewhere much stronger: *"an authorization-bearing artifact resting on a state-(1) record has not satisfied the predicate, and RFC3-16(a)'s Effect when the predicate fails governs its dependent effects."* That effect rule is: dependent effect **blocked**, "the adoption does not bind," authorization **renders Unknown**, and the condition **mints a contradiction routed to owner adjudication**.

[Observed] RFC3-16's own *Scope* paragraph (`:152-157`) places "the adoptable class" — which the §1.2 table defines as `doctrine/`, `contracts/`, `policies/`, `declarations/` — squarely under the RFC3-16(a) predicate.

[Inferred] Composing those three passages literally: at V0, before A1 exists, **every one of the 32 accepted contract modules, plus the adopted VIS/SEC doctrine, plus the craft policies, is in state (1)** — so a conforming implementation must render each Unknown and mint a contradiction against each, and "the adoption does not bind."

[Inferred] I read this as a deliberate two-audience split (state (1) governs humans; machine gates wait for correlation) rather than an outright contradiction — RFC3-16(c)(1)'s license is carefully worded "*for human governance*," and RFC3-16's "is effectively accepted" carries the qualifier "to the extent RFC3-16(c) licenses for that record's state." But **nothing in the package says this out loud**, and the two clauses read as if they disagree:

- (b) tells the implementer to render a caveat.
- (c) tells the implementer to block and mint a contradiction.

An implementer reading (b) alone builds the wrong thing. And record §2 tells the owner only the favorable half — *"The owner and the humans working with them lawfully govern development by it"* — never that under RFC3-16(c)'s own last bullet, the corpus they are accepting does not satisfy the predicate for Syzygy's machine gates until a later correlation act. That is not a false statement; it is an incomplete one **at exactly the seam the rev10 repair was made to make honest**, which is why I raise it rather than note it.

**Why it blocks:** the review question is whether the model is coherent, and two clauses of the same sub-section prescribe different implementer behavior for the identical artifact class. **Cost to fix:** one sentence in RFC3-16(b)'s bootstrap paragraph reconciling it to (c), and one sentence in record §2 stating the machine-gate half. Both are additive; the RFC-side sentence invalidates the act-1 digest, so it must land before the confirming review binds the final manifest.

### E2 — Act 3's bound artifact is not in the packet; its step-2 verification is not scriptable from the packet
**Location:** `FINAL-…-RECORD.md:17` — "the nine topology files at `topology/BUNDLE-MANIFEST.md`'s digests."

[Observed] Paths in this package are relative to `final-prespec/` (per the review charter and every other path in the record). `final-prespec/topology/` **does not exist**; the bundle lives at `_bootstrap/rfc-phase/topology/`. §6 asserts *"All scripts derive their root from their own location and run from the delivered packet on any machine (directive §11)"* — [Observed] that assertion does not hold for act 3, whose entire bound content is outside the packet.

[Observed] The digest itself is fine (`0d34d1b5…` confirmed, and the bundle manifest's internal `sha256sum -c` block is well-formed with its own run-from-here instruction). **Why it blocks weakly:** the owner or lead can find it, so this is a dangling reference rather than an unexecutable act — but it falsifies §6's portability claim and leaves act 3 the only gate whose step 2 cannot be run from the delivered packet. Fix: make the path repo-relative, or ship the bundle inside the packet.

### E3 — Act 1's installation breaks the manifest's own relative paths, defeating the mandated post-copy verification
**Location:** `FINAL-…-RECORD.md:42-48`, step 3.

Step 3 installs "the 32 modules (with their package directory structure) plus `ACTIVE-CONTRACT-MANIFEST.txt` to `.syzygy/governance/contracts/rfcs/`" and requires that "copies are digest-verified after the copy."

[Observed] Every manifest entry is prefixed `rfcs/` (e.g. `rfcs/RFC-0002/README.md`). [Inferred] Landing the manifest at `.syzygy/governance/contracts/rfcs/ACTIVE-CONTRACT-MANIFEST.txt` makes those entries resolve to `.syzygy/governance/contracts/rfcs/rfcs/RFC-0002/README.md` — nonexistent. `sha256sum -c` would fail 32/32 on a **correct** install. The verification the step mandates cannot be performed as the step describes.

Fix is one word of precision: the manifest must land at `.syzygy/governance/contracts/` (one level above `rfcs/`), or the step must name the directory to run `-c` from. **Why it matters more than it looks:** this record's whole discipline is "never hand-transcribe a digest, always verify by script," and the one install step it defines silently produces a script that fails.

### E4 — The rev9 RFC gate is still live and independently executable; supersession is advisory only
**Location:** `FINAL-…-RECORD.md:28-31`; corroborated by `00-README.md:18-21` and the rev9 record's own header.

The rev10 record makes supersession **conditional on the act** ("on the owner's act, supersedes…"; "A rev10 act supersedes the rev9 gate") and then merely advises against the old phrase: the rev9 phrase *"should not be used."* 00-README says the same: the compacted corpus "supersedes it **on owner acceptance only**."

[Observed] In the window before any rev10 act — i.e. right now — the rev9 gate is fully executable:

- the nine rev9 RFCs still sit at `_bootstrap/rfc-phase/rfcs/` at **exactly** the rev9 record's §3 digests (verified all nine: `34f930c5…`, `3f57935c…`, `90c1279d…`, `bb0fce86…`, `ebfe7401…`, `20bd414e…`, `2b94c3b7…`, `74f59fde…`, `ceabc3e3…`);
- the rev9 record carries **no** supersession marker pointing to rev10 — I grepped it; its only "superseded" references point *backwards* at pre-rev8 packets — and it still self-describes as *"the only current owner-facing acceptance index"*;
- so the rev9 act-1 phrase would pass its own record's step 2 verification today.

[Observed] Aggravating: the rev9 phrase is **`ACCEPT FOUNDATIONAL RFCS` with no digest argument at all**. Unlike every other act in either record, it cannot self-identify which corpus it binds. [Inferred] An owner who writes it — reasonably, having been shown that phrase for weeks — produces a formally valid rev9 act over the nine-RFC corpus, and nothing in either document catches it.

**Why it blocks:** the independence criterion was "no path where both the rev9 and rev10 RFC phrases could be validly offered." That path exists, is currently open, and is the one an owner is most likely to walk by muscle memory. **Fix:** a retirement header written into the rev9 record itself (not only into rev10), retiring `ACCEPT FOUNDATIONAL RFCS` unconditionally at delivery of rev10 rather than at rev10's act. Supersession of an *authority* should not be conditional on exercising the authority that supersedes it.

### E5 — Act 3's home is undefined-by-omission (minor)
**Location:** `FINAL-…-RECORD.md:47` — "act 3 installs topology to `.syzygy/map/topology/`."

[Observed] `.syzygy/map/` does not exist. Act 1's clause says its home is "created at this step"; act 3's carries no equivalent. [Inferred] `.syzygy/map/` is a **surface namespace** under RFC3-18, so creating it is a plane-namespace change, not just a mkdir. Non-blocking — the copy implies creation — but the record is precise everywhere else about which step mints a home, and this is the one gap.

---

## Risks worth naming even where I did not raise an exception

- **§6 is incomplete by design and says so** [Observed: `reviews/` is empty; the act-1 digest is offered pre-convergence]. Honest, but it means the §1 phrase currently on offer is provisional. [Observed] Of the five exceptions, only E1's RFC-side sentence touches `rfcs/`; E2, E3, E5 and E4 are edits to `FINAL-…-RECORD.md`, `00-README.md` and the rev9 record — none of which is in the manifest, so none invalidates `b77374b8…`. Worth stating explicitly in §3, because the current text ("Regenerated after the rev10 confirming review if any fix lands") does not distinguish fixes that touch `rfcs/` from fixes that don't, and a reader could conclude the digest must churn when it need not.
- **§7 item 1 is a genuine semantic commitment, correctly disclosed.** [Observed] Accepting act 1 with q4 unruled rides RFC3-15's drafted default into the digest — and that default is not passive: RFC3-15 states *"A plane validator therefore accepts exactly these six names and rejects a seventh; neither rejecting `declarations/` nor admitting an unreserved directory is conforming."* The owner is accepting a **six-name closed validator**, not merely deferring a question. The record's phrasing ("or knowingly ride the drafted default") is accurate but understates how load-bearing the default is.
- **RFC-0010's RFC10-9 applies the two-state model correctly** [Observed: `rfcs/RFC-0010-mission-control-autonomy.md:172-179`]: the mission envelope is declared authorization-bearing, an uncorrelated bootstrap approval "renders honestly as owner-adopted, never as verified," and an envelope without act provenance leaves its mission in `awaiting-approval`. This is the one place the corpus works the effect rule through concretely, and it does so consistently — [Inferred] which is also what makes E1's silence about the corpus's own state (1) conspicuous by comparison.
- [Unknown] Whether the owner intends state-(1) artifacts' dependent effects to actually block at V0, or intends the effect rule to reach only artifacts *other than* the foundational corpus. E1 cannot be resolved from the package text alone; it needs an owner ruling or an authoring-intent statement.

---

## Summary

| Check | Result |
|---|---|
| 1. Digests by script | PASS — 32/32 OK; manifest digest byte-exact to act-1 phrase; acts 2/3/4 all verify |
| 2. Truthfulness vs rev9 defect | PASS — defect absent in all wordings; RFC3-16(c) + case 14 close it at clause level |
| 3. Executability, acts 1–5 | **E2, E3, E5** — step 3 of acts 1 and 3 |
| 4. Independence & supersession | **E4** — both RFC gates live; rev9 phrase argument-free |
| 5. Status headers (32/32) | PASS — consistent two-state; none self-declares acceptance |
| 6. RFC3-16(a)/(b)/(c) coherence | **E1** — (b) and (c) prescribe different implementer behavior for state (1) |

**Verdict: EXCEPTIONS.** E1 and E4 are substantive and should be fixed before the confirming review binds the final manifest; E2, E3 and E5 are mechanical and cheap. None of the five requires reopening a decision — all are text repairs to the record and to RFC3-16(b). Notably, only an E1 fix touching `rfcs/RFC-0003/governance-homes-and-owner-acts.md` would invalidate `b77374b8…`; the rest live outside the manifest.
