# R-ARBITRARY-PUBLIC-REPO-1
Verdict: REVISE
Reviewed commit: 8a661db7fb27ac5234889c454f8e8a940507c525
Subject: openspec/changes/polaris-dossier-arbitrary-public-repo/

Reviewer: fresh-context reviewer (Claude Opus 5.5), 2026-10-08. Read-only.
Bytes read with `git show 8a661db7…:<path>`; governing texts read at
`origin/main` `3409ef5ae9f7dcbadbb248d4df1c295dc43a5b0b` (still the tip of
`origin/main` when fetched for this review). No external or target
repository content was fetched.

Files reviewed (8): `proposal.md`, `design.md`, `proposed/polaris-generation/spec.md`,
`OWNER-PACKET.md`, `IMPACT-LEDGER.md`, `GOVERNING-DEPENDENCIES.md`,
`tasks.md`, and the one-row hunk of `openspec/README.md`.

## Confirmations (no finding)

- [Observed] Every quotation in the `design.md` table "Which clauses require
  per-repository consent" (design.md:7-26) matches the bytes at the cited
  lines at `3409ef5a`: SEC-2 `security.md:42-45`; SEC-4 `security.md:116-117`;
  `architecture.md:26-27` and `:62-64`; `doctrine/README.md:25-26`; RFC1-3
  `RFC-0001…md:178-181`; RFC5-12 `consent-egress-secrets.md:99-100` and `:111`;
  RFC3-30 `manifests-and-namespace.md:519-521`; REQ-025 base spec `:1400`;
  REQ-033 local-agent spec `:11` and `:13`. The REQ-002 quotation (base spec
  `:52`) and the REQ-034 phrases (local-agent spec `:230`, `:234`) also match.
  Ruling 10b is quoted accurately (`REDIS-LOCAL-AGENT-SITTING-DIRECTION.md:37-39`).
- [Observed] The finding the lead asked about holds as far as it goes:
  per-repository *read* consent is required by `architecture.md:26-27`,
  RFC1-3, RFC5-12 and RFC3-30, not by SEC-2 (egress) or SEC-4 (writes); so a
  spec sign-off alone cannot supply it. Finding 1 says what the table misses.
- [Observed] Impact-ledger sweeps re-run by script over
  `git ls-tree -r -z --name-only 3409ef5a`: 2,569 paths, 4 non-UTF-8 skipped;
  file counts A 37, B 181, C 77, D 19, E 34, F 0 — every figure equals the
  ledger. [Observed] `git grep -l -E "REQ-polaris-generation-03[789]" origin/main`
  returns no file, so 037..039 do not collide on main at `3409ef5a`.
- [Observed] Every scenario is WHEN/THEN(/AND); each requirement carries
  Case/Observable/Oracle/Oracle independence/Falsifier; scenario count 9+8+3=20
  matches the ledger's PROJECT-STATUS row.
- [Observed] No artifact in the package presents any act as performed; every
  file carries a candidate banner, and the packet says no act is offered
  before review (OWNER-PACKET.md:3-5).

## Findings

### 1. The Q0 "reading" contradicts the text of RFC3-7, RFC5-12 and RFC1-2/RFC3-6; it is an amendment in substance, and the clause table omits the clauses that show it (blocking)

Anchors: design.md:33-42 ("The literal text is met: each observed repository
has a record naming it"); OWNER-PACKET.md:35-46 ("One act; no doctrine or
contract text changes"); spec.md:11 ("The instance record is not an owner
act, adds no act and widens no consent").

Clauses it rests on, all [Observed] at `3409ef5a`:

- RFC3-7 (`RFC-0003/manifests-and-namespace.md:256-264`): "**Consent
  records** are governance acts stored in `.syzygy/governance/decisions/`,
  referenced — never embedded — from the declaration. … Observation/write
  consent (SEC-4): subject is the pair *(observing Project, repository)* …
  Every observed repository requires one, governed root or not." And
  `:274-276`: "Every consent record carries attribution, grant timestamp, and
  scope, and is individually revertable. Attribution is a stored field and
  therefore a *claim* about who granted it; it is honored only under
  RFC3-16(a)."
- RFC5-12 (`consent-egress-secrets.md:95-97`): "one record instance grants
  exactly one class, so each is individually revocable and individually
  renderable".
- RFC1-2 (`RFC-0001…md:175-176`): "Repository identity is a declared identity
  in the project declaration, never a remote URL or path". RFC3-6
  (`manifests-and-namespace.md:249-254`): "An entry whose consent reference
  does not resolve to an in-force consent record is **not observed**".

[Inferred] Under REQ-037 the record that names the repository (the instance
record) is, by the spec's own words, not an act, grants nothing, is written by
Syzygy into the run state directory (not `decisions/`), is referenced from no
declaration, and is revocable only by the standing act or a new standing
version. The record that grants (the standing act) names no repository. So no
single record is both "a governance act stored in `decisions/`" and one whose
subject is the (Project, repository) pair, and no record "grants" for that
repository in the sense RFC5-12 uses. A machine-written record that carries
an owner attribution is exactly the "claim about who granted it" RFC3-7
says is honored only under RFC3-16(a). The repository identity is declared
by the operator per run, not in the project declaration (RFC1-2, RFC3-6). A
reading that makes all of this "a recorded per-repository consent record"
does not choose between two meanings of ambiguous words, as the
bounded-mission act did with the human-trigger ("Existing doctrine permits
bounded multi-pass mission operation…",
`BOUNDED-MISSION-DOCTRINE-INTERPRETATION-ACT.md:21-24`); it sets aside the
clauses' stated location, act-character and grant subject. The design's
claim "The literal text is met" (design.md:36) is not accurate, and the
packet's "no doctrine or contract text changes" (OWNER-PACKET.md:37-38) tells
the owner the cheap route is not an amendment when it is one in substance.
VIS-4 makes this the owner's call; it is the packet's job to say plainly what
is being called.

The clause table (design.md:9-25) cites RFC3-30 but omits RFC3-7, RFC3-6
and RFC1-2/RFC1-4, and the amendment route (design.md:43-48,
OWNER-PACKET.md:40-42, IMPACT-LEDGER.md:69-75) names RFC-0005 and RFC-0001
but not RFC-0003, whose RFC3-7 is the clause most directly displaced.

Repair: (a) add RFC3-7, RFC3-6 and RFC1-2/RFC1-4 to the table with quotes;
(b) strike "The literal text is met" and "no doctrine or contract text
changes"; state in Q0 that option A departs from RFC3-7's storage and
act-character text and RFC5-12's "one record instance grants", and that a
reviewer reading it as an amendment would be right on the text; (c) either
recommend B, or keep A as recommended but present it as an owner ruling that
these clauses do not bind standing-admission runs — which is an amendment by
another name and should carry the amendment path's review (CC-REV-2 /
normative-change workflow); (d) add RFC-0003 to every amendment-route
listing, and to REQ-037's opening paragraph and warrants (`contracts:` gains
RFC3-6, RFC3-7).

### 2. Precedence and exclusion are keyed on an operator-declared identity, so a withdrawn per-repository consent can be laundered (blocking)

Anchors: spec.md:9 ("a repository identity in the form the standing record
fixes … no per-repository observation consent record exists for the pair
(`project:syzygy`, that repository) … the repository is not a declared
repository of any Syzygy project declaration; and the repository is not on
the standing record's exclusion list"); spec.md:11 ("the upstream URL and the
fork or clone location, as configuration and never as repository identity");
spec.md:35-39 (scenario "Per-repository consent takes precedence": "a
withdrawn per-repository consent is never replaced by the standing
admission"); design.md:72-79.

Clause: RFC5-13 (`consent-egress-secrets.md:115`): "Consent revocation is
prospective: it stops future acts (RFC5-11) and renders dependent claims
Unknown". RFC3-7 (`manifests-and-namespace.md:277-279`): "consenting to
observation by one project must not silently admit another" (the same
principle for subjects).

[Inferred] All three exclusion predicates compare the identity the operator
types at run start. Nothing binds that identity to the bytes: the URL is a
label, Syzygy makes no network request, and identity is free text in "the
form the standing record fixes". If Redis's consent is withdrawn, the
operator (or an agent session that runs `init`) can clone the same
repository, declare `github-redis-redis-fork` or any other identity, and the
standing admission admits it — the outcome the precedence scenario says
never happens. The same holds for a repository declared in a Syzygy project
and for an excluded one. The scenario and falsifier test only the case where
the operator declares the matching identity.

Repair: make the precedence and exclusion predicates content-based as well
as name-based, checkable from the local object store with no network: e.g.
refuse the standing route when the pinned commit, or (where history is
admitted) any commit reachable from it, or the root commit(s), equals a
revision named by any per-repository observation consent record in any state,
or equals a root commit Syzygy has recorded for a declared or excluded
repository; also compare the normalised declared URL against the locator
hints of every consent record and declaration. State the residual honestly
(a repository with no recorded revision overlap remains distinguishable only
by declaration, labelled Inferred). Add a scenario "Withdrawn consent under a
different identity" and a falsifier arm for it. Have the standing record's
exclusion list carry URLs and commits, not only identities.

### 3. REQ-038 changes Redis runs, contradicting "Redis is untouched" and REQ-037's own falsifier (blocking)

Anchors: spec.md:3 ("a run under a per-repository observation consent, Redis
included, keeps every predecessor requirement and scenario … except where
REQ-polaris-generation-038 says it applies to every operator-agent run");
spec.md:98 ("In an operator-agent run, every claim block that states why …
SHALL declare exactly one basis"); spec.md:83 (REQ-037 falsifier: "or
Redis's run changes in any respect"); spec.md:71-75 (scenario "Redis keeps
its own consent": "the run proceeds under those records exactly as before
this change"); proposal.md:67 ("**Redis is untouched.**");
OWNER-PACKET.md:25 ("Redis is not affected.").

Clause: CC-SPEC falsifier discipline as applied here — a falsifier that a
conforming implementation of a sibling requirement must trigger is not
testable as written. [Inferred] Under REQ-038 every Redis draft gains a
mandatory basis field, new repair findings and new fidelity verdict fields,
and REQ-034's reader topic is re-read for it; so "Redis's run changes in any
respect" is falsified by REQ-038 itself, and the proposal and packet tell
the owner Redis is unaffected when its dossier rules change.

Repair: choose one. (a) Scope REQ-038 to standing-admission runs and say
so in its first sentence and in spec.md:3; or (b) keep it for every
operator-agent run, narrow REQ-037's falsifier and scenario to "Redis's
admission basis, consent, statements and pinned revisions change", and
correct proposal.md:67 and OWNER-PACKET.md:25 to say Redis dossiers also
take REQ-038's basis rule (add a Q3 sub-question: apply to Redis too?).

### 4. Admitting history conflicts with REQ-033 sentences that neither 037 nor 038 names as read (blocking)

Anchors: spec.md:3 ("For a run under the standing admission it reads the
predecessor text that each requirement below names, and only that text");
spec.md:11 (scope includes "the ancestor commit objects reachable from it
where, and only where, the standing record admits history"); spec.md:100,
102 (commit-message citations); OWNER-PACKET.md:56 (Q1d recommends
including history).

Clause, [Observed] at `polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:13`:
"Every read Syzygy makes for the run SHALL be a Git object read by object
identifier at the pinned revision through the registered observer" and
"Syzygy SHALL recompute the object identifier of every commit, tree and blob
it reads on the path from the pinned commit to each blob it uses"; and its
falsifier (`:215`): "an object is read from the working tree or at another
commit".

[Inferred] An ancestor commit object is a read "at another commit", and its
message is not on "the path from the pinned commit to each blob". Because
spec.md:3 says the change reads only the text it names, and neither 037 nor
038 names these 033 sentences, 033 still forbids the reads that Q1d's
recommended option and REQ-038's commit-message premises depend on. Either
history can never be admitted, or 037 contradicts 033 unstated.

Repair: in REQ-037 (or 038), name these two 033 sentences and the falsifier
arm and give their reading for a standing run whose record admits history
(e.g. ancestor commit objects reached by parent links from the pinned commit,
each re-hashed, are reads "at the pinned revision's history"); state whether
ancestor trees and blobs are in scope (spec.md:11 admits commit objects only;
say so in the packet). Also say whether commit author and committer names
and e-mail addresses are rendered, and under which screening class — a
third-party author's address is personal data, and VIS-4 keeps privacy
posture human-gated.

### 5. REQ-038's guarantees rest on the agent's own marking; an unmarked motive claim escapes the basis, the marker and the fidelity check (blocking)

Anchors: spec.md:98 ("The agent marks the kind and the basis; Syzygy sees
only the marking, and the page SHALL say that whether an unmarked block
states one of the four kinds is the agent's report"); spec.md:106 ("The
fidelity verdict … SHALL record, for every block of the four kinds, whether
its quotation states what the block claims or its trail supports it").

Clause: VIS-2 (`vision.md`): "No evidence means Unknown, not success"; base
REQ-002 (`polaris-manifesto-generation/…/spec.md:52`): "an Inferred label
alone SHALL NOT make speculation eligible. Generated prose SHALL NOT
impersonate an author".

[Inferred] A block the agent leaves unmarked that says "the authors chose X
to avoid Y" is not "a block of the four kinds" for any rule in REQ-038: it
needs no basis, gets no "not the authors' stated intent" marker, is not
subject to the bar on attributing intention (that bar is on "A reconstructed
block", spec.md:102), and the fidelity verdict need not assess it. Disclosing
that classification is the agent's report is honest about the gap but does
not close it, and acceptance criterion 4 asks that every reconstruction be
"never presented as authors' intent". The fidelity reviewer is the only
independent party that can see the gap.

Repair: require the fidelity verdict to classify every Inferred block, not
only marked ones, as stating or not stating a motivation, trade-off,
advantage or position, and make a block it classifies as one of the four
kinds without a basis a blocking finding (deficient subject: the marking).
Extend the bar on attributing intention to the authors to every block, not
only reconstructed ones. Add a scenario "Unmarked motivation" and a
falsifier arm.

### 6. "Maintainer-stated" is assigned to any non-generated file or any commit message, including vendored third-party text (note)

Anchor: spec.md:100 ("from text the subject's maintainers wrote: a source at
the pinned revision that carries no generated-file marker … or … a commit
message of a commit reachable from the pinned commit").

[Inferred] A vendored dependency's README, a copied licence text, or a
drive-by contributor's commit message satisfies this test, so a dependency's
claims could render as the subject's maintainer-stated advantage — the
attribution error 10b exists to avoid ("A dossier's advantages rest on what
the maintainers wrote down", `REDIS-LOCAL-AGENT-SITTING-DIRECTION.md:37-38`).
Repair: say that authorship by the maintainers is Inferred from location;
exclude paths the run's profile classes as vendored or third-party; let the
fidelity review record "not maintainer text" as a finding; or rename the
basis `repository-stated`.

### 7. Packet Q1c says local commits are "Excluded"; nothing in the spec excludes, declares or checks it (note)

Anchor: OWNER-PACKET.md:55 ("**Excluded.** Only commits published in the
public repository." Why: "Your own commits on the fork … may carry your own
notes or credentials."); spec.md:13 ("that the pinned commit is published at
the upstream URL … are the operator's declarations"); spec.md:9 (the
operator's required declarations are only URL, location and identity).

[Inferred] The pinned commit is HEAD, whatever it is; the operator is not
even asked to declare publication. The credential worry is met by SEC-5
screening, not by this exclusion. Repair: add the publication declaration to
spec.md:9's list and the disclosures; reword Q1c to "excluded by the
permission's words, not checked: you declare it, and SEC-5 screening still
applies".

### 8. The governed predicate's review attribution is wrong, and a reviewed residual is not carried (note)

Anchors: design.md:96-98 ("That reading was reviewed (R3-F9) as 'never less
strict than a root-only, exact-case match'"); OWNER-PACKET.md:75 ("it was
reviewed as the safe reading").

[Observed] R3-F9's words in `packages/polaris-dossier/src/governed.ts:6`
are "the scenario wording 'an adopted capability declaration' is not the
test"; the "never less strict" sentence is the code comment's own
(`governed.ts:7-8`). The review that assessed it is
`docs/reviews/R-POLARIS-DOSSIER-S3-GATES-2-RAW.md:54`, which lists residual
non-governed forms (default-ignorable code points, a trailing tab, NTFS
stream and 8.3 short names) and calls them a disclosure item because "The
project the statement protects has no motive to hide its own governance
tree". [Inferred] That premise was about the owner's own projects; for
arbitrary third-party trees it should be re-stated. Repair: cite the S3
review by path and line, carry its residual list into design decision 4, and
say whether the premise holds for third-party trees (rule 8).

### 9. The packet does not tell the owner that D9's execution case now reaches code from unknown authors (note)

Anchors: OWNER-PACKET.md:61 ("running code only as D9 already allows");
proposal.md:70 ("no execution beyond D9 as REQ-033 states it").

Clause, SEC-3 (`security.md`), "What the permitted case costs": "the session
runs with the owner's own credentials and network … Observed code it runs can
reach them, and can change any file the owner can … Nothing contains it".
[Inferred] SEC-3 is formally unchanged (the per-run choice is still
required), so this is not a weakening; but the owner accepted that cost with
Redis in view, and the standing admission extends it to any repository the
operator clones, of unknown provenance. Repair: add a line to Q1 (or a Q7)
naming the cost verbatim and asking whether standing-admission runs should
refuse the execution choice by default.

### 10. The installed registry entry is not in the impact ledger (note)

Anchor: design.md:156-160 cites only
`contracts/candidates/public-git-source-acquisition-local-agent/proposed/…CANDIDATE.json:58`.
[Observed] An identically named file exists at
`.syzygy/governance/declarations/adapter-registry/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-CANDIDATE.json`.
Repair: name the installed copy, say which one the gate reads, and list it in
IMPACT-LEDGER.md's "Edits required" table against slice 3.

### 11. REQ-039 smaller issues (note)

Anchors: spec.md:183, 189. "Scope: v1-mandatory" on a requirement that has
effect only under a ruling not yet made; and "a draft block that rests on a
source outside the clone SHALL fail the check" — Syzygy can know this only
from the agent's marking, which the text does not say (contrast spec.md:98).
Repair: state the conditional scope, and that detection rests on the
agent's marking, with the fidelity review as backstop.

### 12. The standing record's drawer statement is unlabelled in the spec (note)

Anchors: spec.md:15 ("no kernel evidence drawer exists for a repository
admitted only under it"); design.md:60 ("[Inferred true by construction …]").
Repair: give the spec the same footing the design has: the statement is the
owner's, made in advance, and its truth for a given repository is Inferred
from the precedence and declaration exclusions of Finding 2.

## Acceptance criteria

1. Quotations accurate and anchored: met for every quotation checked; the
   clause set is incomplete (Finding 1), and one review attribution is wrong
   (Finding 8).
2. Q0's reading lawful as a reading: **not met** — an amendment in substance
   (Finding 1).
3. Safeguards kept; no laundering: screening, SEC-5, the in-process reader
   and SEC-3 are kept as text; laundering of a withdrawn consent is **not
   prevented** (Finding 2); history reads conflict with REQ-033 (Finding 4).
4. REQ-038 honesty: marked reconstructions are well handled; unmarked ones
   escape (Finding 5); maintainer attribution overclaims (Finding 6).
5. Scenarios: WHEN/THEN and testable; missing the identity-laundering,
   unmarked-motivation and history-read refusal paths; one falsifier
   contradicts REQ-038 (Finding 3).
6. Ledger denominators: stated and re-derived exactly; IDs free on main.
   Met, with Finding 10.
7. Packet: readable, every question recommended, nothing presented as
   decided; Q0 misdescribes option A (Finding 1), Q1c overstates (Finding 7),
   Redis claim inaccurate (Finding 3).
