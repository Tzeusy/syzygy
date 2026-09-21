# Independent fresh-context review 2 — M2 evidence-currency funnel packet

Reviewed commit: `ec30494425d2fa1d10c01b05af3bd704768be2cb` (worktree
`agent/syzygy-dov.2`; `git status --porcelain` empty — all three reviewed
files are tracked at this commit). Its parent is
`a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d`, the packet's stated baseline.

Files under review, byte counts and sha256 computed this session by script
(`wc -c`, `sha256sum`; rule 3 — nothing transcribed):

- `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` — 63901 bytes,
  sha256 ec10194619758c66c1c15d7a040ea34fac420fed58cb43d9dee7790ec1b73ead
- `docs/evidence/polaris-m2-evidence-currency-funnel-2026-09-14.json` — 6926
  bytes, sha256
  f79a1e15a49446c487da88b8489871030eed1ce5374f232e0bec722416c3d4b9
- `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` — 28305 bytes,
  sha256 c7a2ffc512efc5f6f7fe7f8b6a4d1f598ec499b38415f287cdd802d15832fff1

Context files read (not under review), digests computed the same way:

- `docs/reviews/R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-RAW.md` — 39904 bytes,
  sha256 ff8c8f836e4488de939ae26d5e0a61c12d110c35a5438dd8aab3d5ff4be882bc
  (review 1; matches the packet's and the evidence record's citation of it)
- `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` — 20579 bytes, sha256
  89e0e7af90c979ef497422acd75527bb33131f0736ad9669ada11cb54d78eb01

Retained capture, re-derived this session: 1484487 bytes, sha256
e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111, 1481819
decoded characters — identical to the packet's head matter and the evidence
JSON `capture` block.

Date: 2026-09-14. Reviewer: fresh context, read-only. No repository body was
read; the Butlers-side figures (which blob changed between two revisions) are
taken from the packet's evidence record and were not re-derived here — the
Syzygy-side halves of every one of those rows were.

---

## What re-derived cleanly

Re-computed independently before reading the packet's number, by the methods
named.

**Capture counts.** `data-epistemic-freshness` is `fresh` 713 times and takes
no other value (three methods: attribute regex; literal split on
`data-epistemic-freshness=`; a parse of every `<span class="claim-tuple"`
opening tag — all three return 713/`fresh`). 713 claim-tuple span openings,
equal to the count of the literal `class="claim-tuple"`. Tuple shapes:
`Observed`/`report-fact`/`fresh` ×702 and `Unknown`/`unstated`/`fresh` ×11.
Exactly one distinct `data-evaluation-id`
(`evaluation:pwb-body-read:2026-09-13T13:33:24.295Z`), 713 occurrences. All
four freshness glossary sentences occur exactly once; three of the four
(`stale`, `broken`, `superseded`) are rendered by no tuple. 719 ISO-8601
instants, 713 inside `data-evaluation-id`, 6 in text nodes at offsets
859145, 859189, 860858, 1477549, 1477638, 1481753 — and the grouping the
packet states after F14 is correct: 859145 and 859189 sit inside the one
`<small>` Revision/committed/captured line, 860858 is after a `</small></p>`
in the authority-disclosure `<p><small>`. First visible instant at 58.0%.
`data-polaris-item="` 409, substring `data-polaris-item` 417, of which 8 are
`data-polaris-items` — the F18 predicate holds exactly.

**The L4-F1 re-measurement, Syzygy side.** From the retained machine captures
beside the page: `projectShape.sources` is 278 and `projectShape.items` is
415 [Observed]. Taking the evidence record's 15 changed source paths, all 15
are present in the 278-source population, and exactly **9** items carry an
anchor on one of them — the nine `claim:item:baseline-spec:*` for
`butler-relationship`, `butler-switchboard`, `core-daemon`, `core-notify`,
`dashboard-approvals`, `module-approvals`, `runtime-config-api`,
`runtime-config-dashboard-ui`, `runtime-config-table`. All nine have exactly
one rendered `data-polaris-item` row on the page and all nine of those rows
render `fresh`. The packet's 9 / 415, 9 / 409 and 9 / 9 rows are confirmed by
a method the packet does not name. The claim-id → rendered-row match is exact
in one direction: every rendered row matches a machine item (0 unmatched).

**Code sweeps.** `assessCurrency`/`CurrencyBoundDeclaration` appear in exactly
three source files (`packages/cap1-core/src/staleness.ts`,
`packages/cap1-conformance/src/req-042.conformance.test.ts`,
`req-062.conformance.test.ts`) plus documentation; **0** occurrences anywhere
under `packages/three-surface-poc-core` or `apps/three-surface-poc`. `horizon`
across non-test `packages/*/src` and `apps/*/src` returns one hit,
`polaris.ts`:156, about horizontally scrollable tables. Two reading plans are
defined (`polaris-reading-plan.ts`:4 and :293); `excerpt-label` occurs twice
in the capture, once as the CSS rule and once as a rendered marker, so
exactly one condensed rendering — the packet's row.

**Code citations.** `staleness.ts` `assessCurrency` spans 87–155 with five
return paths over three `state` values, and the `no-bound-declared` return
(94–104) carries `state`, `label`, `reason`, `claimClass` and **no**
`freshness`, while the three `stale` returns each set `freshness: 'stale'`
and `current` sets `freshness: 'fresh'` — the F7/Q7 gap is real.
`project-shape-model.ts`:162–166 is the standing-argument comment, :167 the
`FRESH` constant, :185 and :193 its two uses, and the `@syzygy/cap1-core`
import (19–27) already brings in `FRESHNESS_STATES` and `FreshnessState`.
`polaris-copy.ts`:45–49, `polaris.ts`:357, `model.ts`:100–110,
`main.ts`:80–81/113/134/187/201, `git-observation.ts`:61 and
`walkthrough-preflight.ts`:212–220 are all exactly what the packet says, and
the preflight does require only `` `${term} —` `` for *presented* terms, so
an appended unreachability marker keeps the check passing.

**Quoted clauses, re-read at their defined locations.** VIS-2
(`vision.md`:96), VIS-7 (:183), RFC2-9
(`RFC-0002/snapshot-and-evaluation-core.md`:187), RFC2-10 (:209),
`architecture.md`:221–229 and :236, `trust-and-evidence.md`:97–104,
CAP1-REQ-062 (Capability 1 spec, heading at 1837) and PWB-REQ-007's currency
scenario — every quoted fragment is verbatim at its named location.
PWB-REQ-007's heading is at 439, the scenario at 470–474, the `contracts:`
row of its `warrants` block at 480 naming `RFC2-9, RFC2-10`. PWB-REQ-020's
heading is at 902; its Observable ("both populations contain equivalent
multisets") at 915, its Scenario THEN ("the complete human fact multiset
equals the machine fact multiset") at 931, its Falsifier tail ("or associated
with a different evaluation in either channel") at 924–926, and the enumerated
population sentence at 906–909 — the packet's F2 repair quotes all four
correctly. The escalation-trigger fragments "a change to the constraints or
envelope the registry entry declares", "any observation outside the consented
content class or repository" and "any scope beyond the signed change" are
verbatim at `decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`:88–94, hard
wrapped. F16's premise re-derives: `grep -c` of `CAP1-REQ` and of `PWB-REQ`
over `DIRECTIVE-REGISTER.md` both return 0.

**Register arithmetic.** The P-69 note's "**22** open rows below
(sub-lettered rows counted) and **5** acceptance-act rows, **27** in all"
re-derives exactly: 22 data rows under "Open, and only the owner can dispose"
(P-10 … P-69, with P-25(c) counted) and 5 under the acceptance-acts section.

**Digest and path hygiene.** Every hex token of 7+ characters in the packet
and the evidence record is a git revision (`a9f671e`, `2e3bac97790b`,
`7c8743f63`, two 40-hex revisions) or a full sha256 of an unbound file (the
capture, the packet's own prior bytes, the evidence record, review 1). No act
argument, manifest digest or truncated signed digest appears — nothing
CG-7e/CG-15 reaches. No backticked Butlers path in the packet or in the
register row; the Butlers paths in the evidence JSON are bare JSON strings,
not code spans. `python3 scripts/check_governance.py` run read-only in the
worktree: **32 OK, 20 WARN, 0 FAIL (52 checks)**, unchanged from review 1;
the one new WARN line naming the packet's family is a dangling-link note
against the retained review's citation of a lane-B evidence file that lives
only on `agent/syzygy-dov.17`, and a retained raw may not be edited.

**Hard prohibitions.** Checked each of the seven recommendations, answered as
recommended, against AGENTS.md's list. None puts implementation code in
`openspec/**` or `.syzygy/**` (slice 5 edits a JSON declaration); none opens
a deferred wave, Mission Control, release, remote access or multi-user
support; none adds a repository body read; none adds unattended agent
coordination; none adopts doctrine, accepts a contract or labels anything
accepted for the owner; none opens a second PWB spec package. The act table
says "**None found**" where no act exists (row 4b).

---

## Findings

### G1 — blocking — the P-69 row still carries the warrant the packet withdrew

`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`:199, Q4 clause:

> **Q4** how re-observation is triggered — recommended **an explicit operator
> route, no timer** (unattended coordination is prohibited; no act found that
> authorizes a timer, none needed for the route)

The packet withdrew that warrant after review 1's F5 and says so in terms at
`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:47 — "An earlier draft
leaned on AGENTS.md's 'no unattended agent coordination'; a single daemon's
timer is not agent coordination, and that sentence is withdrawn (review 1
finding F5)" — and its repair table at :793 reports F5 as "Accepted and
repaired: the unattended-coordination sentence withdrawn". The register row is
the artifact the owner rules from, and it still asserts, as the *first* of two
warrants, a prohibition that the packet's own post-review text says does not
reach a single daemon's timer. An owner ruling Q4 from the register would rule
on a ground the packet has disclaimed.

*Resolves by:* deleting the clause "unattended coordination is prohibited;"
from the row so it reads "(no act found that authorizes a background poller;
none needed for the operator route)", matching the packet.

### G2 — blocking — the P-69 row misdescribes which slices may run now

Same line, Q6 clause:

> slices 1–4 (horizon probe, `asOf` guard, lapsed-selection announcement,
> legend marking) touch no governed artifact and may run under the 2026-09-05
> continuation

The packet's four no-act slices are 1 Legend truth, 2 Evidence horizon,
3 an `evidence` block on the machine payload, 4 `asOf` immutability
(:344–350, :383–500). The row invents a slice that the packet does not have —
"lapsed-selection announcement" appears in the packet only as scenario S9
(:648–652) and as one mutation target (:756) — and **drops slice 3**, the one
slice whose lawfulness rests on a conditional `[Inferred]` reading of
PWB-REQ-020 that the packet itself says could pull slice 3 into Q6's collision
(:480–484). So the register both authorizes-by-description work the packet
never scoped and hides from the owner the slice with the stated contingency.

*Resolves by:* "slices 1–4 (legend marking, horizon probe, an `evidence` block
on the machine payload, `asOf` guard)", and either scoping S9 as a slice in
the packet (see G3) or dropping it from the row.

### G3 — blocking — S9 is an acceptance obligation with no slice, no topology row and no act row

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:648–652 states scenario
S9 ("A lapsed reviewed selection announces itself"), and Gate 6 item 4 at :756
requires rule-6 mutation evidence for "the reading-plan announcement". Neither
has a slice in Gate 3's table (:344–350), a design sketch in Gate 4
(:383–554), a row in the authorizing-act table (:368–375), a success criterion
(:114–130), a line in the funnel summary (:814–828) or a mention in the
recommended handoff (:830–867); nor is it in "Out of scope, explicitly"
(:654–659). The dossier lists this move for M2 by name
(`docs/pursuits/2026-09-13-vision-pursuit.md`:152–153, L4-M5, "announce a
lapsed reviewed reading selection instead of falling back silently"), so the
omission is a scope gap against the dossier the packet says it implements —
the same class of defect as review 1's F9, one move later. As written Gate 6's
acceptance contract cannot be satisfied: it demands mutation evidence for work
no slice builds.

*Resolves by:* either adding S9 as slice 6 with its topology row, its act row
(it edits `polaris-reading.ts`/`polaris.ts` only, so no act) and a success
criterion, or moving it to "Out of scope, explicitly" with the reason and
striking it from Gate 6 item 4 — and in either case making the P-69 row match.

### G4 — non-blocking — "nothing above 58% of the page carries a date" is false under its own words

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:184–185 ("Nothing above
58% of the page carries a date [Observed]") and :111–112 ("the next reader …
meets no date at all until 58.0% of the way down").

Sweeping the same capture for human-visible dates in *any* form — ISO instants
plus bare `YYYY-MM-DD` plus month names, outside tag markup — returns 8 hits,
and two of them sit **above** the stated threshold: `2026-08-24` at offset
840110 (56.69%) and at 841381 (56.78%), both inside rendered `<cite>` text,
the filename `docs/superpowers/specs/2026-08-24-whatsapp-identity-
reconciliation-design.md`. The claim is true only for the narrower predicate
the evidence record actually used (`iso_instant_occurrences_total`,
`human_visible_text_node_instants_*`), which the sentence does not state.
A reader does meet a date before 58%; what they do not meet is an *instant of
the evaluation*. This is the project's own recorded lesson that a figure
published without its predicate cannot be re-derived, and it is the one
`[Observed]` label in the packet I could falsify.

*Resolves by:* "No instant of this evaluation appears in rendered text above
58% of the page [Observed: ISO-8601 instants in text nodes, two methods; two
`YYYY-MM-DD` strings occur earlier, both inside a cited source filename]".

### G5 — non-blocking — the packet's new PWB-REQ-020 reading is contradicted by the capture it measures

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:464–470:

> PWB-REQ-020 does not permit the machine channel to carry more *facts* than
> the page: its Observable reads "both populations contain equivalent
> multisets", its Scenario "the complete human fact multiset equals the machine
> fact multiset" …

The quotes are verbatim (verified at spec :915 and :931). But the retained
machine capture beside the page already carries six project-shape item facts
the page renders nowhere: `claim:item:project-account-section:` `architecture`,
`v1-scope`, `v1-success`, `purpose`, `promises`, `refusals` — 415 machine
items against 409 rendered `data-polaris-item` rows, and the string
`project-account-section:architecture` occurs **0** times in the served bytes
[Observed, this session, both channels of the same retained capture]. The
existing parity sweep passes on this capture. So one of two things is true and
the packet says neither: either the strict reading it now adopts is wrong (the
Case at :912–914 scopes the comparison to "every project-shape parity marker
on Polaris and every corresponding machine-answer fact", and the normative
SHALL at :906–909 is one-directional — page facts recoverable *from* the
machine answer), in which case slice 3's argument is much stronger than the
packet makes it and needs no `[Inferred]` contingency; or the strict reading is
right, in which case the implementation is in breach today over six items and
the packet has walked past a live PWB-REQ-020 finding.

This also makes the packet's own denominators (415 machine items vs 409
rendered rows, :96–97) read as an unexplained discrepancy in a table the owner
is asked to rely on.

*Resolves by:* stating the six `project-account-section` items as the existing
precedent, saying which reading they establish, and either dropping the
`[Inferred]` contingency at :480–484 or converting it into a disclosed
possible PWB-REQ-020 finding for the owner. Give the 415/409 rows a one-line
note that the six unrendered items are the difference.

### G6 — non-blocking — the F6 repair attributes the escalation trigger to the wrong act

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:371: "**The consent
act's escalation trigger** is scoped to the content class and the repository
('any observation outside the consented content class or repository')".

`decisions/PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md` has four sections
(Ceremony, Effect, What this act does not authorize) and **no** escalation
section; `grep -ci trigger` over it returns 0. The quoted phrase occurs in
exactly one tracked file under `.syzygy/`,
`decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`:92–93, in its "Escalation
triggers" section. The consent act contributes only the scope sentence the
same cell quotes next ("at the Butlers revision the POC observes"). Review 1's
F6 asked for the trigger's actual words; the repair supplied them but bound
them to an act that does not contain them, which is rule 8 in the other
direction. The conclusion (no act needed) is unaffected — the trigger exists,
in the act the slices ride.

*Resolves by:* "the implementation-authorization act's escalation trigger
('any observation outside the consented content class or repository'); the
consent act's scope sentence names 'the Butlers revision the POC observes',
and the probe reads a ref of the already-consented repository …".

### G7 — non-blocking — slice 2 still runs the F4 argument that Q3 abandoned

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:446–450, under the
heading "**Why the probe cannot be folded into freshness**":

> If a changed source set a claim's freshness to `broken`, then the page served
> at 10:00 and the page served at 14:00 for one identified evaluation would
> disagree on a status-bearing field. RFC2-10 makes that disagreement
> release-blocking and VIS-7 names it as a violation. Hence Q3.

The three lines immediately above it (:441–444) say the opposite: "the probe's
result is computed once, at build, and carried on the model — never read at
render", so two reads at 10:00 and 14:00 cannot disagree whichever field
carries the value. Q3 itself (:46) now concedes this — "the probe is computed
once at build, so folding would not make two reads disagree" — and grounds the
answer on RFC2-10's evaluation scoping instead. The repair table at :792
reports F4 as repaired with "the render-time-drift argument kept only as a
non-ground", but here it is not a non-ground: it is the section's whole
argument, under a heading that promises the reason, and it contradicts the
paragraph above it and the question it cites.

*Resolves by:* replacing :446–450 with Q3's actual ground (a changed source is
a fact of a different evaluation; RFC2-10 binds a claim's freshness to the
evaluation that produced it, so a value sourced from a second evaluation is a
freshness state no run of the first could reproduce), keeping the render-time
sentence only as the argument that does *not* decide it.

### G8 — non-blocking — slice 1's `stale` marker states the wrong reason and is self-falsifying under Q7

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:388–390:

> - `stale` — older than the declared currency bound. *Not reachable at this
>   evaluation: no claim class has declared a currency bound. Route: the
>   registry currency-bound declaration and its owner act.*

Two problems, both reader-visible copy. First, the stated reason is not the
operative one: `stale` is unreachable today because nothing routes freshness
through `assessCurrency` at all — `project-shape-model.ts`:167 hands every
claim `FRESHNESS_STATES[0]` — not because no bound is declared. Second, under
Q7's own recommended answer (:50, :539–546) a class with **no** declared bound
renders `stale`; the absence of a bound is then precisely the condition that
*makes* `stale` reachable, so the marker's stated reason becomes the refutation
of its own claim the day slice 5 lands. The packet's handoff (:838–843) shows
it knows this — "the copy oracle then requires the `stale` legend sentence to
have lost its marker … which, on the day slice 5 lands, is every class" — but
the marker text is not written to survive it.

*Resolves by:* "*Not reachable at this evaluation: no claim's freshness is
judged against a currency bound — the model assigns a constant. Route: declare
the bound in the registry, act on it, and route freshness through
`assessCurrency` (slice 5).*" — a reason that stays true until the slice lands
and false exactly when it does.

### G9 — non-blocking — the batch framing calls Q5's losing arm unlawful, which no clause makes it

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:36–40: "Q3, Q4 and Q5 are
contract-determined … each has **one lawful arm and one arm that is unlawful or
unauthorized**"; and Q5 at :48: deleting the three entries "would hide the
closed vocabulary and make the page's own glossary incomplete **against the
contract**".

For Q3 and Q4 the sentence holds on the packet's reasoning (a second
evaluation's value dressed as this evaluation's freshness; an unauthorized
background poller). For Q5 it does not. RFC2-10 closes the *vocabulary* and
says the list changes only by amendment to the RFC; nothing in it, in
PWB-REQ-007/016/021, or in the preflight requires a rendered glossary to carry
vocabulary members no claim uses — the packet's own preflight finding (:409–413,
verified at `walkthrough-preflight.ts`:212–220) is that only *presented* terms
must be explained, which is exactly why extra entries are permitted and why
fewer would be too. Deleting three entries would be worse; it would not be
unlawful. Telling the owner that their alternative is unlawful removes a
genuine choice rather than smoothing it, which the questionnaire invariant
forbids in the same way.

*Resolves by:* moving Q5 out of the "one lawful arm" sentence and stating its
real shape — both arms are lawful, marking is recommended because it keeps the
closed vocabulary visible to the reader and lets one copy oracle carry the
legend through slice 5 without a second edit, while deleting would make the
page silent about three states the contract still defines.

### G10 — editorial — CAP1-REQ-062 is read as treating the two arms "exactly" alike

:50 and :540: "CAP1-REQ-062's invariant treats an unbounded class exactly as
out-of-bound evidence ('SHALL NOT support a current or favourable answer')".

The clause (verbatim at Capability 1 spec :1841–1848) makes out-of-bound
evidence its grammatical subject and then names two *different* consequences,
distinguished by reason: `stale-beyond-currency-bound` for the first,
`no-currency-bound-declared` for the second. It assigns no freshness value to
either — which is exactly the silence `assessCurrency` mirrors and Q7 exists to
break. "Exactly" overstates a clause that distinguishes them; the recommendation
survives on its other three legs and is correctly labeled `[Inferred]`.

*Resolves by:* "CAP1-REQ-062 puts an unbounded class under the same invariant
as out-of-bound evidence — both render Unknown, with distinct reasons — and
assigns neither a freshness value".

### G11 — editorial — the target's unit convention is unstated and inconsistent within the packet

:142–147 reads the M1 ruling's "under 1.4 MB" as **1,400,000** bytes and pairs
it, in the same sentence, with "the 2,097,152-byte response ceiling" (2 MiB).
The byte figure is defensible — the cited lane A record carries
`result.q3Target.bytes = 1400000` — but the ruling's own words
(`POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`:34) say only "1.4 MB", the
project writes 2,097,152 as "2 MB" in AGENTS.md, and :186 of this same packet
calls 639,806 bytes "625 KB" (binary). Under the binary reading the overage
would be 16,481 / 10,631 rather than 84,487 / 78,637. The same slip is in
"418,000 to 443,000 bytes are reserved" at :146–147, where the source figure is
"418–443 KB". The direction of the conclusion is unaffected either way.

*Resolves by:* naming the source of the byte figure ("the lane A record's
`q3Target.bytes`, 1,400,000") and using one convention for the KB/MB figures
in the same paragraph.

### G12 — editorial — two unlabeled forward estimates

:148, "The horizon band and the marked legend add bytes measured in hundreds",
sits inside a paragraph whose bracket reads `[Observed: … computed
2026-09-14]`; it is a projection about unbuilt code and should be `[Inferred]`.
:719, "Lane B's headline saving (currently recorded as 188,902 bytes tailnet)",
carries no label and no path — reasonably, since the record lives only on
`agent/syzygy-dov.17`, which the packet says elsewhere; say so here too.

### G13 — editorial — three citation offsets are one or several lines short

:579–581 puts PWB-REQ-007's currency scenario "at line 472"; 472 is its WHEN
bullet and the scenario heading is at 470 (the packet quotes 470–473). :353–354
says "`project-shape-model.ts` line 20 imports `FRESHNESS_STATES` and
`FreshnessState`"; the import statement spans 19–27 and `FreshnessState` is on
24. :50 and :532 cite `staleness.ts` "lines 97–103" for the `no-bound-declared`
return, which begins at 98 (97 is the last line of its comment). None changes a
conclusion; all three are the class review 1 raised as F13.

### G14 — editorial — the P-69 row says "two constants" where there is one

`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`:199: "from two
constants in `packages/three-surface-poc-core/src/project-shape-model.ts`".
There is one constant, `FRESH` at :167, assigned at :185 and :193 — as the
packet itself has it ("deletes its `FRESH` constant", :517). The error is
inherited from the dossier (:160–161) and should not travel further.

---

## Repair verification, F1–F20

Each row checked against the current bytes at `ec30494`.

| F | Claimed | Verified | Evidence |
|---|---|---|---|
| F1 headroom | repaired | **REPAIRED** | :139–152 states 84,487 / 78,637 over the 1,400,000-byte target and 612,665 / 618,515 under the 2,097,152 ceiling with the 418–443 KB reservation, labeled; arithmetic re-derived, all four differences exact; the "~479 KB" sentence is gone and its retirement disclosed. Unit-convention nit at G11 |
| F2 PWB-REQ-020 | repaired | **REPAIRED** | :464–486 quotes Observable, Scenario and Falsifier verbatim (spec :915, :931, :924–926) and makes the narrower enumerated-population argument, labeled `[Inferred]` with its condition at :480–484. New objection to the reading at G5 |
| F3 `broken` route | repaired | **REPAIRED** | :392–399 states unreachable-by-design, names only a model that carries evidence across revisions, and explicitly disclaims the horizon as a route |
| F4 Q3's ground | repaired | **PARTIAL** | Q3 at :46 restated on RFC2-10 evaluation scoping ✓, but slice 2's "Why the probe cannot be folded into freshness" (:446–450) still argues render-time drift as the reason — G7 |
| F5 Q4's first warrant | repaired | **PARTIAL** | Withdrawn in the packet at :47 ✓; still asserted in the P-69 register row, `PENDING-OWNER-DECISIONS.md`:199 — G1 |
| F6 consent scope | repaired | **PARTIAL** | :371 now quotes the trigger's actual words ✓ but attributes it to the consent act, which contains no such section — G6 |
| F7 undeclared-bound freshness | repaired | **REPAIRED** | Named at :529–546 and batched as Q7 (:50) with a recommendation and a stated alternative; the engine gap re-verified at `staleness.ts`:94–104 |
| F8 "one new boundary" | repaired | **REPAIRED** | :352–359 "Boundaries crossed: none new"; the import at `project-shape-model.ts`:19–27 confirms the existing edge |
| F9 L4-F1 absent | repaired | **REPAIRED** | :77–105 carries the re-measurement with denominators; 9/415, 9/409 and 9/9-fresh re-derived here independently from the retained machine and human captures |
| F10 digest-bound bytes | repaired | **REPAIRED** | :509–515 names the prohibition verbatim and states the superseding-act mechanism and that the superseded record is never edited |
| F11 one-package rule | repaired | **REPAIRED** | :701–710 labeled `[Inferred]`, argued from manifest mechanics, and explicitly says no clause states it |
| F12 staleness clause | repaired | **REPAIRED** | :325–333 states the clause's superseded-record subject, calls the 58% depth a legibility defect and labels the extension `[Inferred]`; clause re-read at `trust-and-evidence.md`:99–104 |
| F13 hunk header | repaired | **REPAIRED as stated; not re-derivable here** | :677–683 gives both ranges and shows 472 between them. The lane B package is absent from this branch (`git ls-files`, `find` → 0 paths, as the packet says at :664–670), so the hunk headers are `[Unknown]` to this review |
| F14 instant grouping | repaired | **REPAIRED** | :179–184 two on the `<small>` line, one in the authority disclosure; offsets and the intervening `</small></p>` re-derived |
| F15 four or five arms | repaired | **REPAIRED** | :521–523 "five return paths over three `state` values"; Gate 6 item 4 (:752) says "five arms" — consistent, and five is correct |
| F16 register route | repaired | **REPAIRED** | :231–236; `grep -c` over `DIRECTIVE-REGISTER.md` returns 0 for `CAP1-REQ` and 0 for `PWB-REQ` |
| F17 file count | repaired | **REPAIRED** | :201–207 says three source files with the `dist/` caveat; the evidence JSON's `assessCurrency_files` now lists three with a note. Re-derived: three |
| F18 predicate | repaired | **REPAIRED** | :175 names `data-polaris-item="` with 417/8 beside it; all three counts re-derived |
| F19 P-68 not on baseline | repaired | **REPAIRED** | :664–670 says P-68 is on that branch's register copy only and main's last note is P-67; confirmed — main at `a9f671e` has no P-69 either, and this branch adds it |
| F20 Q1 omits the warrants | repaired | **REPAIRED** | Q1 at :44 cites the `warrants` block at spec line 480; verified, `contracts:` there lists `RFC2-9, RFC2-10` |

Net: 16 REPAIRED, 3 PARTIAL (F4, F5, F6), 1 REPAIRED-as-stated but not
re-derivable in this worktree (F13). No finding is NOT REPAIRED.

## Per-question assessment of the new and reframed material

| Q | Scope stated truthfully? | Genuine owner gate? | Recommendation follows? |
|---|---|---|---|
| **Q1** (unchanged, plus F20's warrants line) | **Yes.** Every element re-derived: the comment at :162–166, RFC2-9 verbatim, 713/713 three ways, the warrants row at spec :480 | **Yes** | **Yes**, and now near-mechanical with the warrants citation |
| **Q3** (reframed) | **Yes** in the question cell; **no** in slice 2, which still argues the ground Q3 abandons (G7) | **Disclosed, not a gate** — the packet says so plainly, which is the right handling | **Yes** |
| **Q4** (reframed) | **Yes** in the packet; **no** in the register row, which keeps the withdrawn warrant (G1) | **Disclosed, not a gate** — correctly labeled | **Yes**, on the act-absence warrant alone |
| **Q5** (reframed) | **Partly.** The three-of-four measurement and the preflight reading are exact; the "one lawful arm" framing is not (G9), and the `stale` marker's reason is wrong (G8) | **A real choice**, contrary to the packet's framing | **Yes** as a recommendation; **no** as a legality claim |
| **Q7** (new) | **Yes.** The engine gap is exactly as described — I read the five returns; PWB-REQ-007's tuple requirement and RFC2-10's closure are verbatim | **Yes.** RFC2-10 puts the choice outside the implementer's reach, every class reaches this arm first, and the alternative is a Capability 1 conformance amendment — only the owner can pick | **Yes**, `[Inferred]` and honestly alternatived; the CAP1-REQ-062 leg is over-read (G10) |
| **Q6** (unchanged; register row new) | **Yes** in the packet; the register row misdescribes the slice set (G2) | **Yes** | **Yes** |
| **P-69 row overall** | Q1, Q2, Q3, Q5, Q7 and the default-if-unanswered match the packet; Q4 and Q6 do not (G1, G2); "two constants" is wrong (G14). The review-1 disclosure in the sources cell — that every repair post-dates the REVISE verdict and is uncovered until a second review confirms the current bytes — is exactly right and is the best sentence in the row |

## Cross-cutting

**Labeling.** 27 `[Observed]`, 7 `[Inferred]`, 0 `[Unknown]` over 867 lines —
up from 17/1 at review 1, and the five unlabeled inferences review 1 named are
now labeled. Every `[Observed]` I could test holds except G4's. Two forward
estimates remain unlabeled (G12). No label overstates in the
`[Inferred]`→`[Observed]` direction.

**Sweeps and denominators.** Every "zero/all" claim in the packet carries a
denominator and a second method, and the ones I re-ran (0 `assessCurrency`
references in the POC trees, 1 `horizon` hit, 3 of 4 legend states unreachable,
1 of 2 reading plans condensed, 0/0 spec families in the register) all hold.
The one absence claim with an unstated predicate is G4's.

**Digest and act hygiene.** Clean — see above. Slice 5's handling of the
digest-bound registry entry is the correct superseding-act shape, and the
packet says so.

---

## Summary

The packet is materially better than the bytes review 1 read: sixteen of
twenty findings are fully repaired, the L4-F1 re-measurement is real and I
re-derived its Syzygy half independently, the PWB-REQ-020 quotes are now
verbatim, and Q7 is a genuine addition that names a hole nobody had to find.
I withhold CONFIRM for three reasons, none of which touches a recommended
answer. Two are in the P-69 register row — the artifact the owner actually
rules from — which still states as a warrant a prohibition the packet withdrew
under review (G1) and misnames the four slices that may run now, inventing one
and dropping the one with a stated contingency (G2). The third is in the packet
itself: scenario S9 and a rule-6 mutation obligation exist for a move the
dossier assigns to M2 and the packet never scopes as a slice, so Gate 6's
acceptance contract cannot be met as written (G3). All three are cheap. Beyond
them, fix the false absence claim at G4 (a reader does meet a date before 58%,
inside a cited filename), decide what the six unrendered
`project-account-section` items mean for the PWB-REQ-020 reading slice 3 rests
on (G5), re-attribute the escalation trigger (G6), delete the render-time-drift
argument from slice 2 (G7), rewrite the `stale` marker's reason so it survives
slice 5 (G8), and stop calling Q5's losing arm unlawful (G9) — and this becomes
a CONFIRM with no change to any of the seven recommendations.

Findings by severity: 3 blocking (G1, G2, G3), 6 non-blocking (G4–G9),
5 editorial (G10–G14).

Verdict: REVISE
