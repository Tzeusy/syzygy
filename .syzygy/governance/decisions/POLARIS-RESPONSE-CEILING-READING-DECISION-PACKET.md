# Owner decision packet — what the Polaris response ceilings measure once responses are compressed

> **Candidate — binds nothing.** This packet is an inert offering. It
> performs no act, records no ruling, adopts nothing, authorizes no
> implementation and changes no accepted artifact. It puts **one** reading
> to you, with four smaller questions that follow from it, and gives the
> exact text of the dated owner direction that would give your answers
> effect. Until you issue that direction in your own words, in your own
> session, nothing here has any effect. A commit, a merged pull request, a
> review, a passing check, a bead closing, silence, or a general
> "approved" performs nothing.

Date drafted: 2026-09-26. Drafted by an agent session under the owner's
2026-09-21 rulings, which authorize drafting only.

Gate bead: `syzygy-dov.27`. It blocks `syzygy-dov.10.4` (M10 slice 4b,
response compression).

Warrant for drafting: `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
(this directory), row **P-77**, arm **A**, which reads in part:

> Q2 compression needs a dated owner act on the ceiling reading before it
> ships

and, in the same row's consequences column:

> The registry entry is edited on no arm.

The question itself was put in `docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md`,
row Q2 of its question table and §"The ceiling, and what compression
would do to it". That funnel remains the question P-77 was ruled on; this
packet is the gate the ruling named, and it repeats only what you need to
answer.

## In one paragraph

Polaris refuses to serve a page or a machine answer that is bigger than a
declared number of bytes: 2 MiB for the human page, 8 MiB for the machine
JSON. Today nothing is compressed, so "how big is the response" has one
answer. Once responses are gzip-compressed, it has two: the size of the
page before compression, and the (much smaller) size actually sent. The
observer registry entry says the ceiling applies to "the final encoded
HTTP body", and those words fit both. You are asked which one the ceiling
means. On one answer the ceiling keeps its strength and compression is a
pure transfer saving; on the other, the 2 MiB page ceiling stops binding
at any page size this project can currently produce.

## Why an owner act is needed at all

`[Observed]` The act in force that authorizes PWB implementation stops at
this kind of change. `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`
(this directory), §"Escalation triggers", names among its triggers:

> a change to the constraints or envelope the 2026-09-05 registry entry
> declares

`[Inferred]` Whether compression is such a change depends on the reading,
and you ruled (P-77 Q2) that the reading is yours to make before any
compression ships. So the gate exists whichever reading you choose.

## Why this is a plain dated direction, not a digest-bound act

`[Inferred]` The instrument is a **plain owner direction**: it binds no
artifact digest, adds no row to `ACCEPTANCE-ACT-RECORD.md`, needs no
manifest, no recorder script and no act phrase, and registers nothing in
`scripts/check_governance.py`. Four reasons:

1. **There are no new governed bytes to bind.** You ruled that "The
   registry entry is edited on no arm." The direction reads existing
   words; it changes none. A digest-bound act binds the bytes it adopts,
   and here there are none to adopt.
2. **It closes a trigger crossed by meaning, not by bytes.** That is the
   same shape as the retention-posture gate (`syzygy-dov.28`), which P-79
   called "a retention-posture change needing an owner act before slice
   1" and which was closed by a plain direction.
   `POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DIRECTION.md` (this
   directory) says of itself that it binds no artifact digest, needs no
   manifest or recorder script, adds no row to the acceptance-act record
   and registers nothing.
3. **A digest-bound act would go stale for the wrong reason.** The
   registry entry has a pending candidate amendment (`.18`, the currency
   and briefing package) and another in drafting (`syzygy-dov.24`, the
   loaded profile). Binding this reading to today's registry digest would
   retire it the moment either lands, although neither changes the words
   this reading is about. The direction instead names the words, and the
   check below fails if the words change.
4. **Registering a phrase would be false.** CG-7d and CG-7e police a
   phrase's digest against its subject's current bytes. This direction
   has no phrase and no subject digest, so there is nothing for them to
   check.

If you would rather this were a digest-bound act, say so; that is not an
arm this packet drafts, because the only subject such an act could bind
is a new declaration file that restates a sentence the registry already
holds, which is a second home for the same fact.

## What is true today

All `[Observed]` in this session at the commit this packet was drafted
on, unless marked.

- **What is measured.** `boundedResponse` in
  `apps/three-surface-poc/src/routes.ts` measures the response with
  `const observed = Buffer.byteLength(body, 'utf8');` — the UTF-8 bytes of
  the response string. With no compression in play, that is exactly the
  body sent.
- **Nothing is compressed anywhere.** No non-test TypeScript source under
  `apps/*/src` or `packages/*/src` mentions `zlib`, `gzip` or a
  `Content-Encoding` header. The check script below re-runs this sweep and
  prints its file count.
- **What a breach does.** A response over its ceiling is not served. The
  daemon answers HTTP 503 with a small JSON failure body that names the
  limit, the declared and observed sizes and the population counts, and
  records the breach so the status strip can show it. The registry states
  the rule in `breachResult`: "final-output breaches emit only a bounded
  typed failure carrying evaluation identity, limit identity, declared
  value, observed value and population counts; no truncated or
  success-shaped model is emitted".
- **The breach that has happened.** On 2026-09-13 the human page was
  refused: an 838-byte 503 body recorded 2,132,656 observed bytes against
  the declared 2,097,152 (recorded in
  `docs/evidence/polaris-m9-one-identity-funnel-2026-09-15.json`).
- **What compression would save.** From the M10 funnel, gzip level 6, not
  re-measured here: the machine answer goes from 5,520,314 to 851,986
  bytes (15.4%) and the human page from 1,478,637 to 105,850 bytes (7.2%).
  At that ratio the refused 2026-09-13 page would have been about 153,551
  bytes on the wire, roughly 14 times inside its ceiling.
- **The specification uses the same word.** PWB-REQ-006 in
  `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`
  says "Final encoded human HTML and machine JSON SHALL each have an
  explicit byte ceiling." and its scenario "Resource breach is bounded and
  explicit" ends "human and machine responses stay within their own
  declared encoded-byte ceilings". Its oracle is "exact final encoded-byte
  counts". The word "encoded" carries the same two readings there.
- **No test can tell the readings apart today.** With nothing compressed,
  both readings give the same number for every response.

## The ceilings this reading covers

| Ceiling | Declared value | The registry's sentence for it | Status |
|---|---:|---|---|
| `maxHumanResponseBytes` | 2,097,152 | "the final encoded HTTP body for each Polaris HTML response" | in force |
| `maxMachineResponseBytes` | 8,388,608 | "the final encoded HTTP body for each authenticated Polaris machine JSON response" | in force |
| `maxBriefingResponseBytes` | 20,480 | "the final encoded HTTP body for each authenticated derived read-only machine view response …" (the sentence continues) | **proposed only**, by the candidate `pwb-registry-currency-briefing-amendment` package (`.18`); not in force |

`[Observed]` All three sentences open with the same six words, "the final
encoded HTTP body". The check script derives this table's key set from
the registry and from `.18`'s proposed patch, and fails if a response
ceiling exists that this table does not name.

## The two readings

**Reading 1 — the ceiling measures the body before compression.** "The
final encoded HTTP body" means the response in its final character
encoding (UTF-8), which is what the code measures today. Compression is
applied afterwards, to a body that has already passed.

- The ceiling keeps exactly the strength it has today. The 2026-09-13 page
  would still be refused.
- Every client gets the same answer for the same evaluation: the pass or
  refusal does not depend on whether the client asked for gzip.
- The size a client sees in `Content-Length` and the size the ceiling
  checked are different numbers, on purpose. If compression is used only
  when it makes the body smaller, the size sent is never larger than the
  size checked, so the ceiling still bounds what goes on the wire.
- Cost: the words "final encoded HTTP body" arguably lean the other way.
  In HTTP's own vocabulary a content coding such as gzip is an
  "encoding", so a reader of the registry alone could take it to mean
  bytes on the wire. Under this reading the registry sentence stays
  as written, and this direction is where its meaning is recorded.

**Reading 2 — the ceiling measures the bytes actually sent.** "The final
encoded HTTP body" means the body after content coding, exactly as it
leaves the daemon.

- Compression changes what is measured. The human ceiling would stop
  binding at any page size the project currently produces (the funnel's
  largest human page is about 14 times inside it once compressed), and
  the refused 2026-09-13 page would have been served.
- The answer depends on the client. The same evaluation could be refused
  to a client that does not ask for gzip and served to one that does,
  because the identity-coded body is larger.
- The words fit this reading at least as well as Reading 1.
- `[Inferred]` It turns a refusal that is recorded and shown into a
  success, for the same bytes of content. That is the direction the funnel
  flagged as the one VIS-2 ("No evidence means Unknown, not success")
  cares about. It is not a VIS-2 violation by itself — a served page is not
  a claim of convergence — but it loosens a safety limit that PWB-REQ-006
  names SEC-3 as its warrant for.

## Open questions

Each question below is yours. The drafter's recommendation is marked;
nothing here decides it.

### Q1 — Which reading does each response ceiling bear?

- **(a) Reading 1: before compression** *(recommended)*. Compression may
  ship; the ceiling keeps measuring the UTF-8 body; the difference between
  the size sent and the size checked is recorded, not hidden.
- **(b) Reading 2: bytes actually sent.** Compression may ship; the
  ceiling is measured after compression, per response, and the slice-4b
  bead must record that the human ceiling no longer binds at current
  sizes and that the pass or refusal now depends on the client.
- **(c) Decline, or say nothing.**

**Default if unanswered:** compression does not ship. Slice 4b stays
blocked. Conditional GET (slice 4a) is unaffected; it is already on
`main` and changes no size.

Why (a) is recommended `[Inferred]`: it is the reading the code already
implements, so it changes no enforced limit; it gives every client the
same answer; and it keeps the one refusal the project has ever recorded a
refusal. The price is a sentence whose words a reader could take the other
way, recorded here instead of in the registry because you ruled the
registry is edited on no arm.

### Q2 — Does the reading also cover a response ceiling adopted later?

The briefing ceiling proposed by `.18` uses the same six words. If you
adopt `.18`, should the reading you chose in Q1 apply to it too?

- **(a) Yes: every response ceiling in the entry whose sentence reads
  "the final encoded HTTP body" bears the Q1 reading**, including one
  adopted after this direction *(recommended)*.
- **(b) No: only the two ceilings in force today.** A later ceiling needs
  its own reading before any compressed response is measured against it.

**Default if unanswered:** (b). A later ceiling's responses are served
uncompressed until you rule.

### Q3 — Where is the difference between the size sent and the size checked written down?

Under either reading the two numbers can differ.

- **(a) In this direction and on the slice-4b bead only** *(recommended)*.
  No new header and no new machine field.
- **(b) Also in every response**, as a header carrying the checked size.
  This is a new machine-visible field, so under P-77 Q6 it would join the
  parity sweep as its own family.

**Default if unanswered:** (a).

### Q4 — Does either reading need a specification amendment to PWB-REQ-006?

`[Inferred]` The drafter's view: **no, on either reading.** PWB-REQ-006's
words ("final encoded", "encoded-byte") carry the same two readings as
the registry's, and a direction that says which one binds changes no
requirement text. If you hold that the specification's words fix one
reading and you choose the other, that is a CC-REV-2 amendment with its
own delta, review and act, and compression waits for it.

- **(a) No amendment needed** *(recommended)*.
- **(b) An amendment is needed first.** Slice 4b waits for a CC-REV-2
  delta to PWB-REQ-006.

**Default if unanswered:** (b). A reviewer who finds the specification
fixes one reading raises it before this direction is issued.

### Q5 — Which compression may ship?

- **(a) gzip only**, from Node's own `node:zlib`, applied only when the
  client asks for it and only when it makes the body smaller, with
  `Vary: Accept-Encoding` set *(recommended; the funnel's slice-4b
  sketch)*.
- **(b) gzip and Brotli.**
- **(c) Any coding Node supports.**

**Default if unanswered:** (a). No new dependency is added on any arm.

## What is the drafter's and not yours

These are design choices inside the recommended arms. Say if you want any
changed.

1. "Compress only when it makes the body smaller" (Q5 (a)). It is what
   keeps the size sent at or below the size checked under Reading 1.
2. The 503 failure body is small (hundreds of bytes) and is served
   uncompressed on every arm.
3. The compression threshold (the smallest body worth compressing) is an
   implementation detail of slice 4b and is not a governed value.

## The proposed direction text

For Q1 (a), Q2 (a), Q3 (a), Q4 (a), Q5 (a). Other answers change the
marked paragraphs; the drafter will redraft on request.

```
OWNER DIRECTION — WHAT THE POLARIS RESPONSE CEILINGS MEASURE UNDER
COMPRESSION

Date: <date issued>
Owner: Tzeusy
Continues: decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md and
decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md, whose
registry-envelope escalation trigger this direction answers and does
not widen. Answers P-77 Q2
(decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md).

1. THE READING. [Q1] Each response ceiling in the observer registry
   entry's resource envelope whose sentence reads "the final encoded
   HTTP body" measures the response body in its final character
   encoding, before any HTTP content coding is applied. Today that is
   maxHumanResponseBytes and maxMachineResponseBytes. [Q2] It is also
   any such ceiling adopted after this direction. The number checked is
   the one routes.ts checks today.

2. WHAT MAY SHIP. [Q5] gzip response compression, applied only when the
   client accepts gzip and only when the compressed body is smaller than
   the body that passed its ceiling, with Vary: Accept-Encoding set.
   Because of that rule the bytes sent never exceed the bytes checked.

3. WHAT DOES NOT CHANGE. The declared values, the refusal on breach (a
   bounded typed failure, nothing truncated, nothing success-shaped),
   the breach record and readiness false on breach. A response that is
   refused today is refused after compression ships.

4. DISCLOSURE. [Q3] The size sent and the size checked are deliberately
   different numbers. This direction and the slice-4b bead say so. No
   new header or machine field carries the checked size.

5. WHAT THIS DOES NOT DO. It edits no registry, specification or policy
   byte [Q4: no PWB-REQ-006 amendment is needed]. It sets no new or
   relaxed ceiling, adds no route, reads no new source and widens no
   act. Every exclusion of the 2026-09-02 authorization and its
   2026-09-05 continuation stands.

6. WHAT THIS IS NOT. It binds no artifact digest, adds no row to the
   acceptance-act record and registers nothing. It is a warrant, not
   evidence: it proves no response was measured or served.

7. WITHDRAWAL. A later direction may narrow or withdraw this one.
   Withdrawal defeats grant: on withdrawal no response is compressed.
```

For Q1 (b), paragraph 1 would read "… measures the response body as
sent, after any HTTP content coding …", paragraph 2 would drop the
"never exceed" sentence, and paragraph 3 would instead say that a
response refused today may be served compressed after compression ships,
and that the pass or refusal may differ between clients that do and do
not accept gzip.

The record of issue would be written as
`POLARIS-RESPONSE-CEILING-READING-DIRECTION.md` in this directory, in the
shape of the retention-posture direction: your words verbatim, the
direction as issued, and nothing else. It would edit no earlier record,
including this packet.

## What the direction would not authorize

- Any change to a declared ceiling value, in either direction.
- A second repository, a wider content class, a new route, a new
  credential class or any egress.
- Slices of M10 other than 4b; they stay under their own gates.
- Any edit to the registry entry, to PWB-REQ-006, or to this packet.

## Where this sits among the other packages

`[Observed]` This packet changes no file that any other candidate package
patches, and it binds no digest, so it is **outside** the landing order
you set on 2026-09-23 (`.21` → `.30` → `.22` → lane B, then `.20` and
`.18`). No manifest has to be regenerated because of it, and it has to be
regenerated after none.

What it does depend on is the **words** it quotes. The check script
compares each quoted clause with the file it comes from:

- If `.18` is adopted, the registry gains the briefing ceiling. The
  script already covers it; Q2 decides whether the reading reaches it.
- If `.18`, `syzygy-dov.24`, or any later registry act changes one of the
  response-ceiling sentences, the check fails, and this packet must be
  revisited before it is issued.
- If `.21`, `.30`, `.22` or lane B changes the PWB-REQ-006 sentences quoted
  above, the check fails the same way. `[Observed]` None of their current
  proposed patches touches those sentences.

It can therefore be issued before, between or after any of those acts.

## Impact

- **Files a future slice 4b would change** `[Inferred]`, from the funnel:
  `apps/three-surface-poc/src/routes.ts` and the server that writes the
  response, plus `node:zlib`. Nothing under `openspec/**` or `.syzygy/**`.
- **Tests that must exist before slice 4b is called done** `[Inferred]`,
  on the recommended arms: a body one byte over its ceiling is refused
  whether or not the client accepts gzip; a body that compresses larger is
  sent uncompressed; the sent size never exceeds the checked size; every
  compressed response carries `Vary: Accept-Encoding`; the 503 failure body
  is uncompressed.
- **What changes for readers.** Nothing on the page. Machine clients that
  accept gzip receive about 15% of today's bytes.
- **What does not change.** The registry entry, the specification, the
  secret-classification policy, the consent record, every act and every
  candidate package.

## Review

For a fresh-context reviewer. Read only this packet, the files it quotes,
and the P-77 row.

Acceptance criteria:

1. Every quoted clause is byte-true to its file (the check script tests
   this; confirm it by reading).
2. The two readings are both stated fairly; neither is presented as the
   only lawful one.
3. The instrument argument ("plain dated direction") holds against the
   continuation act's triggers and against P-77's words.
4. Every question has a stated default if unanswered, and every default
   is the fail-closed one.
5. The proposed direction text changes no governed byte and widens no
   act.
6. Nothing in the packet decides a question that belongs to the owner.

## How to check this packet

```
python3 scripts/check_polaris_response_ceiling_reading.py --check
python3 scripts/check_polaris_response_ceiling_reading.py --selftest
```

`--check` confirms the quoted clauses still match their files, that this
packet names every response ceiling the registry declares or `.18`
proposes, that no compression code has landed while no direction exists,
and that this packet keeps its banner and a default for every question.
`--selftest` breaks each of those on purpose and confirms the check fails.
