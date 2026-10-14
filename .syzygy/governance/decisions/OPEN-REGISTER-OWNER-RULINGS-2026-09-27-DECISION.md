# The open register — the owner's rulings on six items (answered 2026-09-27, applied 2026-10-14)

> **Status: ruled; applied 2026-10-14 where still open.** Six items drawn
> from the open table of [`PENDING-OWNER-DECISIONS.md`](PENDING-OWNER-DECISIONS.md)
> were answered by the owner in a local questionnaire packet (in the
> git-ignored `.syzygy/local/` directory, file
> owner-questionnaire-open-register-2026-09-26.md). Each item passed
> independent scope and recommendation review before it was put to the
> owner, and the owner took the recommended option on every one with no
> edits. This record owns the rulings. Nothing here is an act: no digest is
> bound, no doctrine, contract, policy, specification or matrix byte changes,
> and no acceptance-record row is added. It is a plain owner direction in the
> shape of [`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`](POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md).

## How the answers were given and applied

- **Answered:** by Tzeusy (owner), in the Claude Code CLI, one structured
  question per item, session syzygy-17, recorded 2026-09-27. Each item's
  decision block reads `Agreed`, owner edits none, and quotes the option
  label the owner selected (quoted per item below).
- **Applied:** the owner then instructed, on 2026-10-14 in the lead Claude
  Code session, by structured question: "Apply your six 2026-09-26 answers
  (P-50/51, PR5, P-49, P-25, P-18-C3, P-10) now, each through the workflow
  that owns it." That instruction covers exactly these six items. It is not
  approval of any merge, external or live action beyond what each item's
  own boundary names.
- **Evidence snapshot:** the items were reviewed at Syzygy `23b486c`. Before
  applying, each item's load-bearing facts were re-checked at `origin/main`
  `8f1fbec7` on 2026-10-14 (results per item below). Two items had been
  overtaken in the meantime by later owner rulings; they are recorded as
  such and nothing was re-applied.

Each section below is its own decision; agreement to one is not approval of
another.

## 1. P-50 and P-51 — closed: the adopted Capability 1 specification owns both obligations

- **Choice:** A — "A. Close both (Recommended)".
- **Ruling:** both obligations in Capability 1 charter row 1.1 — "never
  partial registration" (P-50) and "a named failure" (P-51) — are the
  adopted specification's own stricter rules, in CAP1-REQ-002 ("An invalid
  declaration is a named failure, never a partial registration"). RFC3-9
  backs only the Unknown rendering and the no-auto-repair rule. No contract
  amendment is needed and the charter is not edited.
- **Boundary:** closes register rows P-50 and P-51 only. No edit to
  RFC-0003, the charter, or any bound specification file; no contract
  amendment; no new requirement.
- **Re-check 2026-10-14:** [Observed] CAP1-REQ-002's heading is unchanged
  (`openspec/changes/project-registration-and-honest-shape-visibility/specs/project-registration-and-honest-shape-visibility/spec.md`
  line 98), and the coverage file's RFC3-9 row still says failing by name
  "is this specification's own authored strictness"
  (`openspec/changes/project-registration-and-honest-shape-visibility/CONTRACT-COVERAGE.md`
  line 105).
- **Applied:** rows P-50 and P-51 moved to
  [`DECISION-HISTORY.md`](DECISION-HISTORY.md). Their beads `syzygy-l3o`
  and `syzygy-oaa` were already closed (each closed when it queued its row)
  and carry a note pointing here.

## 2. PR5-POLICY-REWRITE — PR #5 closed, five findings routed to one follow-up

- **Choice:** A — "A. Close + route findings (Recommended)".
- **Ruling:** close draft PR #5 and beads `syzygy-2dn` and `syzygy-blu`;
  route the five still-open findings against the specification policies
  (RD69-N1, RD69-N3, RD69-N5, RD70-N1, RD70-N2) to one tracked follow-up, to
  be fixed as a findings-only correction when the policies are next
  amended; mark RD70-N3 fixed.
- **Boundary:** no edit to either binding policy, no merge, no new policy
  draft or amendment.
- **Already done before this application:** [Observed] PR #5 was closed
  without merge on 2026-09-28 and both beads were closed, under the
  separate owner ruling "Close #5, use restyle"
  ([`OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md`](OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md)).
  That part is not re-applied. The meaning-preserving restyle that ruling
  chose did not address the five findings: [Observed] RD70-N1's stray "as
  CC-SPEC-8" still stands in CC-SPEC-11 on 2026-10-14.
- **Applied:** follow-up bead `syzygy-4x77` (owner-gated; related to
  `syzygy-hfp7`, the other note waiting on the next policy amendment)
  carries the five findings. **RD70-N3 is fixed**: the 2026-09-01 amendment
  made CC-SPEC-8 name all nine modules. The round-2026-08i disposition
  register still labels it open; that file is historical and is not edited,
  so this record and the bead are where the fixed state is recorded.

## 3. P-49 — RFC-0007 needs no amendment: the count is 324

- **Choice:** A — "A. Rule 324, no amendment (Recommended)".
- **Ruling:** the accepted RFC 0001–0009 clause population is the **324**
  headed clauses. RFC-0007's six lettered parts — RFC7-2(a)–(c),
  RFC7-9(a)–(c) and RFC7-11(a) — are named parts of their parent clauses,
  citable by their letters; lists that go clause by clause (the routing
  matrix, CG-17) may show them as rows. This matches how RFC-0005 and
  RFC-0009 treat lettered parts. No text changes.
- **Boundary:** a counting ruling only. No edit to RFC-0007, the matrix,
  any coverage file or any script. It does not endorse the matrix's
  per-part routes (RFC7-2(b) routed "not applicable" while its parent is
  not) or its "45"; both belong to P-10.
- **Re-check 2026-10-14:** [Observed] after the 2026-09-28 contract
  readability restyle, RFC-0007's front matter, closing line and README
  still list the six as sub-clauses; RFC7-2's parts are list items and
  RFC7-9's bold-led paragraphs in `narrative-contract.md`; the three
  coverage files under `openspec/changes/` still state 324.
- **Applied:** row P-49 moved to [`DECISION-HISTORY.md`](DECISION-HISTORY.md).

## 4. P-25 — overtaken by doctrine amendment D5; nothing applied

- **Choice:** A — "A. Yes to both (Recommended)": "actuator toolchain" and
  "agent toolchain" name the same thing, and agent workers and humans
  working by hand are actuators. The boundary recorded meanings only, so
  that agents could review the two drafted amendments (P-25(a), P-25(c))
  before a later adoption.
- **Overtaken:** [Observed] the same day, 2026-09-27, the owner adopted
  doctrine amendment D5 with the words "Adopt D5"
  ([`DOCTRINE-AMENDMENT-D5-READABILITY.md`](DOCTRINE-AMENDMENT-D5-READABILITY.md)).
  D5 absorbed both amendments, and rows P-25 and P-25(c) were moved to
  `DECISION-HISTORY.md` then. The review this answer was to unblock is
  moot. Nothing is re-applied.
- **What the answer still says:** D5 left its judgment call 2 — the
  actuator identity sentence ("Agent toolchain" and "actuator toolchain"
  name the same role) and reviewer note N2 (whether a human working by hand
  counts) — "as drafted" for the owner. [Inferred] This answer agrees with
  both as drafted. It is recorded as the owner's stated meaning, not as an
  amendment, and changes no doctrine byte.

## 5. P-18 (part C-3) — "Claim" is compatible with doctrine's frozen nouns

- **Choice:** A — "A. Record reading, close (Recommended)".
- **Reading:** `architecture.md`'s Vocabulary section freezes thirteen
  technical nouns for citation (project, capability, gap, contradiction,
  evidence, warrant, aligned, converged, genome-complete, genome, snapshot,
  evaluation, observation record). The list fixes those words and forbids no
  others, so *Claim* — the noun accepted RFC1-24 uses for every positive
  status — is compatible with it. Doctrine is not amended. RFC3-15 names
  this directory as the home for such adjudications; the 2026-08-31
  bounded-mission reading is the precedent for a reading that amends
  nothing.
- **Register notes for the row's other parts:**
  - **P-18(a)**, the governance-category count, was ratified at the Wave A
    act of 2026-08-17: the foundational acceptance record's §7 says "The
    same act ratifies the P-18(a) seam", and Act A carried §7.
  - **P-18(c)**, "evidence tier" versus "rendering tier", is not a doctrine
    seam (doctrine uses neither phrase); it is one of P-17's eight
    undefined terms and is in effect deferred with P-17.
- **Boundary:** one reading and the two register notes. No doctrine or
  contract edit, no change to P-17. C-1, C-2 and C-4, which the row names
  but does not ask, are excluded.
- **Re-check 2026-10-14:** [Observed] after every doctrine amendment adopted
  since the item was reviewed, the Vocabulary section still lists the same thirteen nouns and omits
  *Claim*; RFC1-24 still reads "All positive status flows through Claims".
- **Applied:** row P-18 moved to [`DECISION-HISTORY.md`](DECISION-HISTORY.md)
  with the (a) and (c) notes.

## 6. P-10 — the routing-matrix review is knowingly deferred, with three triggers

- **Choice:** A — "A. Defer with 3 triggers (Recommended)".
- **Ruling:** no confirming review of `SURFACE-CLAUSE-ROUTING-MATRIX.md`
  now. Its route definitions and Capability 1 authoring supplement are
  reviewed before (1) the next launch-gate administration or (2) a new or
  amended specification relies on them; its remaining rows, including the
  six newest RFC-0010 clauses, before (3) Wave C or D is taken up.
- **Boundary:** records the three triggers only. No review is dispatched
  now and the matrix is not edited. Whether RFC 0010–0011 are accepted is
  untouched (they stay deferred candidates), as is P-49's question.
- **Re-check 2026-10-14:** [Observed] CG-17 examines 210 routed clauses
  (the P-10 row says 199); no launch-gate administration has run since
  Administration 1.
- **Applied:** row P-10 stays open, annotated as knowingly deferred with
  the three triggers. Bead `syzygy-ynpa` (deferred) holds the review and
  is dispatched only when a trigger fires.

## What remains for the owner

Nothing from these six. No item needed an act phrase or a bound-byte edit.
The findings in `syzygy-4x77` are fixed only by a future reviewed
amendment of the specification policies, which needs its own owner act.
