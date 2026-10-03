# Owner sitting packet — "a Polaris dossier for redis/redis"

> **Candidate — binds nothing.** Drafted 2026-10-03 for the owner's target
> sentence in `docs/polaris-generation/TRACKER.md`. It lists what one sitting
> would need and infers no act: every row names its own record, its own act and
> its own review gate. A row is offered only after its package's confirming
> review (CONFIRM, or CONFIRM WITH EXCEPTIONS with notes only). State lives in
> the register rows P-87 to P-91 of `decisions/PENDING-OWNER-DECISIONS.md` and
> in each package. The status column below is a dated copy (2026-10-03) for
> reading order only; the PR, its raw reviews and its register row own the
> state, and a stale cell here loses to them.

## Terms used here

- **Observation** is reading a repository's files; **egress** is sending some
  of what was read to the model provider. They are separate consents (REQ-polaris-generation-025).
- **Manifest row**: the line of a package's manifest that holds one record's
  digest. An **option at the manifest row** is a structured question whose
  option names the record; selecting it is the act, and no phrase is typed
  (admission packet, Q5). This page quotes no phrase: where a typed phrase is
  an alternative (rows 7 and 9), its exact text is issued with the act package
  when the act is given, because a phrase carries a digest that would go stale
  here.
- **Content class** (RFC5-14): the closed list of kinds of content an egress
  consent may name, such as code or evidence. **RFC5-14 class** in row 7 is a
  seventh class, `project-documentation`, for README and LICENSE files.
- **RFC4-1 / RFC4-3 / RFC7-14**: contract clauses; RFC4-1 admits one
  implementation per registry role, RFC4-3 says a registry entry enables
  nothing without an implementation version, RFC7-14 is the clause the
  narrative profile may amend.
- **P-87 to P-91**: rows of `decisions/PENDING-OWNER-DECISIONS.md`, the
  register of open owner decisions. **gap n**: item n of the numbered gap list
  in `docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md`. **O1 to O4**: the
  options inside a row's own packet. **Q2, Q5, Q6**: questions of the
  screening-scope packet (Q2) and the admission packet (Q5, Q6).
- A spec change travels as a reviewed semantic delta and binds only when the
  owner signs it (CC-REV-2); that is what row 9's sign-off is.

## The sitting, in dependency order

Each act is separate and separately revocable (REQ-polaris-generation-025);
none implies another. "Option" means a structured question whose option names
the records at their manifest rows (admission packet Q5). "Ruling" means a plain
owner direction. Status is as of 2026-10-03 and none of it is an act. Rows 2, 3, 9 and 10 each
hold several separate decisions, listed as a, b, c and d; each is answerable
on its own.

| # | You give | Record and where | Form | Depends on | Status |
|---|---|---|---|---|---|
| 1 | Public-source screening scope | `public-source-screening-scope` (PR #266); the closed exclusion-reason set is whatever the code constant `GENERATION_EXCLUSION_REASONS` holds, which must exist before the act | option at the manifest row, plus the packet's Q2 continuation direction (see "Row 1 and the Butlers pin") | nothing; blocks every read | merged to main as a candidate, confirmed (CONFIRM WITH EXCEPTIONS at round 4, 895f1622, manifest in its package directory, notes only); the exclusion-reason constant must exist before the act; recorder on main |
| 2a | Provider execution route: route A or route B, see "Row 2 is one choice" below | route A in `public-admission-registry-entries` (PR #255); route B in the Messages API entry (PR #273) | option at the manifest row | gap 21 check for route A | PR #255 merged to main as a candidate, confirmed at d08f4400 (CONFIRM WITH EXCEPTIONS, round 4, notes only); PR #273 cleared at round 3 (CONFIRM WITH EXCEPTIONS); merged; three entry notes carried as known limitations |
| 2b | Credential and billing: will you supply an API key and accept API-account billing and terms | both routes (see below) | plain direction | 2a | not an act; no phrase |
| 3a | Git-hosting source-acquisition adapter: one shared adapter or one per target (P-89 O1) | `public-admission-registry-entries` (PR #255) | option at the manifest row | row 1 | merged to main as a candidate, confirmed at d08f4400, as row 2a |
| 3b | The adapter's proposed acquisition limits (P-89 O2, labelled Inferred) | same entry | part of the same option at the manifest row; the limits are bytes of the entry | 3a | as row 3a |
| 4 | Observation consent, psf/requests `v2.34.2` | `public-repo-admission` (PR #215) | option at the manifest row | rows 1, 3 | merged to main as a candidate, confirmed at 7704b4a5 (round 7) |
| 5 | Observation consent, redis/redis `8.10.2` plus `7.2.4`, `7.4.0`, `8.0.0` | same package (PR #215) | option at the manifest row | rows 1, 3 | merged to main as a candidate, confirmed at 7704b4a5 |
| 6 | Egress consent, `(project:syzygy, provider:anthropic)` listing requests and Redis | same package (PR #215) | option at the manifest row | rows 2, 4, 5; gap 21 | merged to main as a candidate, confirmed at 7704b4a5 |
| 7 | RFC5-14 `project-documentation` class | `rfc5-project-documentation-class` (PR #257) | contract-amendment act, in one of three forms (its packet): an option at the manifest row (binds the row), a typed contract act phrase over the manifest file (binds the file), or the version-tagged sign-off of the 2026-10-02 Scope A direction, which applies only if you rule that it reaches this amendment; P-88 | its review | merged to main as a candidate, confirmed at dff2f0dc (the commit its review read); its phrase registration lands in the install change |
| 8 | Egress, a second version adding `project-documentation` and the discovery stages, written to name the provider and request and not a route (independent of row 2a) | `public-egress-v2` (draft PR #299), generated by one command from the first version's parameters | option at the manifest row | rows 6 (optional once this is signed), 7 | drafted as a candidate in PR #299, **not ready**: the discovery stages are delivered by PR #281 and the record is generated from its head, but the builder prints no digest until #281 is on main; not reviewed; recorder not drafted. Perform row 7 first: until RFC5-14 lists the class, the record would permit a class no accepted contract defines. It must be confirmed beforehand against the row-7 package's proposed text; then row 7 and row 8 fit one sitting in that order |
| 9a | Narrative profile, first choice: an overlay on the generation spec, or an RFC7-14 amendment first (P-90 O1) | `polaris-non-governed-narrative-profile` (PR #256) | spec sign-off per 9c | its review | merged to main as a candidate, cleared at round 3 (CONFIRM WITH EXCEPTIONS, notes only); its raw review is `.syzygy/governance/contracts/candidates/non-governed-narrative-profile/reviews/R-NON-GOVERNED-NARRATIVE-PROFILE-3-RAW.md`; two spec-text notes are disclosed in its packet as known limitations |
| 9b | The omitted reality band (P-90 O2) | same package | part of 9c | 9a | as 9a |
| 9c | The sign-off form: Scope A reading, or a typed phrase over the spec digest (P-90 O3) | same package | the form itself | 9a, 9b | as 9a |
| 9d | The adoption path: move the spec file and generalize the scenario-count tooling (P-90 O4) | same package | install step | 9c | as 9a |
| 10a | Ruling: altitude order of a dossier (gap 17d) | `docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md` | plain direction, P-91 | none | no review needed |
| 10b | Ruling: advantages as maintainer-stated claims only, or also external comparison sources (gap 18) | same | plain direction, P-91 | none | no review needed |
| 10c | Ruling: the page budget, after the first measurement (gap 19, deferrable) | same | plain direction, P-91 | the first run | no review needed |
| 11 | Optional standing direction: per-target consent and egress-version instances are the builder's deterministic fill of reviewed templates, and the per-target act is one option naming them | gap 9; P-91 | plain direction; a novel reading of Q5, so it needs its own review | row 6 | not drafted as a review item |

PR #120 is the sibling self-observation scope. Row 1 and PR #120 each add a
top-level object to the same secret-classification policy and bump its version:
whichever is performed second must regenerate its package with `--write` first,
and row 1 uses its own version label so neither is renamed by the other. Row 1
does not depend on PR #120.

## If you decline or defer

The default is what happens with no answer; the cost is what that leaves out.
[Inferred] throughout, from the dependencies above and the gap analysis.

| Row | If declined or not yet given | Cost |
|---|---|---|
| 1 | No act is recorded. If Q2 is declined, the act waits for another ruling on the re-pin (see "Row 1 and the Butlers pin") | No Redis or other public body is read, so every later row has nothing to act on |
| 2a, 2b | No provider route; nothing is sent to any model | The dossier cannot be generated; reads and screening can still happen |
| 3a, 3b | No adapter | No repository is fetched, so no body is read |
| 4, 5 | No observation consent for that repository | That repository is not read (requests for 4, Redis for 5) |
| 6 | No egress consent | Reads may happen; nothing leaves the machine |
| 7 | The `project-documentation` class stays outside the vocabulary | README and LICENSE stay unsent; the licence-history regeneration waits |
| 8 | Egress stays at the first version | The new class and the discovery stages are not permitted, so discovery and README text cannot be sent |
| 9a to 9d | No profile | A dossier-shaped page for a non-governed repository has no specification basis |
| 10a | The specification's existing altitude order applies (it is reserved to you unless you rule otherwise, gap 17) | A different order is not available |
| 10b | Advantages are maintainer-stated only, which is lawful now (gap 18) | No external comparison sources |
| 10c | No page budget until the first run is measured | The first page is judged without a size limit |
| 11 | Each later target takes its own option at its manifest row | One extra question per target |

## Row 1 and the Butlers pin

Row 1's act replaces the policy file, and the Butlers read gate pins that file
by digest and version (`governance-inputs.ts`), so it refuses the new policy
until a re-pin changes the pin, its tests, two CI steps and the status battery.
Who depends on it:

- **Redis and any public target.** [Observed] On main, and on the
  dossier-consent branch that carries the admission-record reader, no module of
  the generation path (the polaris-generation app files and packages) imports
  the pin modules, and nothing reads `publicSourceScope`. The run does not read
  that pin today. [Observed] It also has no screening of public-target bodies
  at all yet (tracked as syzygy-vjqd, in progress). [Inferred from the lead's
  direction] That loader will read the policy only through row 1's act record,
  not the Butlers pin, so the Redis path depends on row 1 but not on the
  pin.
- **Butlers and the Three-Surface POC.** [Observed in the package's
  simulation] The act alone makes the existing Butlers read path refuse the
  policy on its digest, so the POC's Butlers pages would stop reading until the
  re-pin lands.

The re-pin is therefore not a separate sitting row. It is an install step under
a plain direction the owner gives inside row 1: the packet's Q2 asks to widen
the continuation from the gate alone to the list the simulation produces, as
the 2026-10-02 re-pin did for its set. The recorder performs no re-pin and says
so; the change that records the act makes it by hand, in the same commit. If
the owner declines Q2, the act should not be recorded until a re-pin is
otherwise ruled, because recording it alone breaks the Butlers path.

## Install step after row 1: the Butlers re-pin

When row 1's act is given, `scripts/record_public_source_screening_scope_act.py`
(on main) writes the act record, appends its aggregate section and applies the
package's patch, and refuses while `GENERATION_EXCLUSION_REASONS` is unreadable.
It re-points nothing. The re-pin is a separate, explicit step in the same
commit, run under the Q2 continuation direction the owner gives inside row 1:
the gate's expected version, scope anchors, act identity, recording tag and the
act-record and superseded-record pointers in `governance-inputs.ts`; the
version copy in `git-object-reader.ts` and the value `content-classification.ts`
takes from it; the tests that assert them; the status-battery lines and the two
CI steps that carry the policy digest; and the act-subject chain and
digest-copy rows in `check_governance.py`. The list is the one produced by
`scripts/simulate_public_source_screening_scope_act.py --tests`; the sitting
installer is to parse the performed record for its values. Without this step
the Butlers path stays refused; the Redis path is unaffected [Observed, see the
section above].

Correction, 2026-10-03: the impact ledger of the row-1 package (PR #266) lists
`project-shape-model.test.ts` as passing after the policy change because its
version literals are fixtures. [Observed] That holds for the act alone, but not
after the re-pin: the test asserts the policy version at two lines (435 and
592), so it fails until the installer updates them, which it does. The ledger
stays the reviewed bytes; this note and the runbook (PR #286, finding F10) carry
the correction.

## After the sitting, in order

1. Perform the recorders for the acts given, each with the argument or option
   the owner supplied (the runbook, PR #286, lists the command per row).
2. Run the one-command installer, the Redis sitting installer (PR #286).
   It refuses, with the tree restored, unless every required record exists, and
   it makes one commit with every record, the re-pin above included.
3. Run `poc:dossier` (PR #268) on the Redis URL. It stops with exit 3 if an
   admission record is missing.

Preconditions: PR #278 merged (the closed exclusion-reason set; runbook finding
F13) and PR #273 merged if route B is chosen. A rehearsal against synthetic
arguments is in PR #286 and changes nothing real.

Nothing in this order is an act; each step only records or applies what the
owner has already given.

## Row 2 is one choice

Route A (PR #255) runs the Agent SDK 0.3.288 and CLI 2.1.288 pin behind a
runtime loopback egress gate and a closed header table. Route B (PR #273)
calls the Messages API directly through `@anthropic-ai/sdk` 0.131.0. They
address one authority, so RFC4-1 admits one; PR #255's Git-hosting entry is
unaffected either way. Neither carries an implementation version, so neither
enables output by being signed (RFC4-3).

| | Route A (Agent SDK) | Route B (Messages API) |
|---|---|---|
| Credential | API key only under the confirmed bytes (the closed header set carries no other credential); billing is the API account, not a signed-in plan | API key only, from one environment variable (name proposed, [Inferred]) |
| Bytes beyond the generator's text | the runtime's own: a fixed system prefix, an empty system message, a per-run device and session id, headers naming the OS, CPU architecture and Node version, and sometimes a body-less probe the gate answers locally | the entry's listed fixed request, which includes the same three machine-identifying headers (OS, CPU architecture, Node version); the entry lists them as sent, and whether the egress record should require stripping them is your choice (PR #273, O2) |
| Surface | a bundled CLI process in the path | no bundled CLI; the Anthropic SDK library (0.131.0) is in the path |
| Review | confirmed at d08f4400 | cleared at round 3 (CONFIRM WITH EXCEPTIONS); merged |

Ask: which route (2a), and, because both are API-key only, whether the owner will
supply a key and accept API-account billing and terms (2b); if not, neither route
runs. This page makes no recommendation between the routes.

Pins common to both (labelled [Inferred], not measured): model `claude-opus-5-5`,
effort `high`, no tools, and a `max_tokens` ceiling of 64000. Say whether the
ceiling is acceptable for the first run; its measurement informs a later entry
version. Also decide the egress-record wording both entries need read: the
record's "fixed by the runtime" and "nothing else" phrases against the pinned
fields. Both entries' packets say the first egress version's conditions (it "adds
no context of its own") may need a version describing the route's fixed bytes.
[Observed] Row 8's record is written route-neutrally: it names the provider and
the request and admits the bytes whichever registered route entry lists. Route
choice (2a) and egress version 2 (row 8) are independent: neither requires the
other, and signing row 8 does not choose a route.

## Proposed run budget (owner-adjustable, not an act)

[Inferred] These values come from code caps and are unmeasured. They need no
phrase and bind nothing: the owner may change any value or leave them, and
nothing is signed over them. They will live in code under syzygy-bc0g.

- Unit `dossier-units-v1`: 1 unit is 1,000 tokens (input, cache and output),
  rounded up per call; a call whose usage is unknown counts at its full
  ceiling.
- Run total 4,000 units, about 4M tokens: a worst-case ceiling; typical spend
  is not measured.
- Shares: 1,000 units for discovery (at most 40 units per call), 3,000 for
  narrative.
- Per-stage cap: 600 units on stages that read all sources, 300 on the others.
- Per attempt: at most 64k output tokens. Wall clock: 2 hours.
- When the budget runs out, the run renders what is complete and marks the
  rest as deferred-by-budget.
- Cost is stated in tokens only; no price has been measured.

## Later-gate options, not asked now

A fingerprint-stripping option (`stripFingerprint`) is absent from the cited
gate and appears only in a later commit (abc9d411). It is a possible option of
a later gate version and is neither in the confirmed bytes nor asked at this
sitting.

## Row 1 questions that remain with the owner

Excluded-source metadata (what a withheld source may still carry); the
run-profile id and its carrier; how often active content will withhold a source
(measured by the first run, not decided now); and confirmation that the
exclusion-reason set is the constant's values. The generator also excludes
oversize sources, so a run excluding a Redis file for size sends that file's
path-level metadata only as the scope's rule lets it.

## What the sitting does not do

It performs nothing by being listed. Rows 7 and 9 do not alter any
bound byte until their own packets' install steps run. Rows 2 to 8 grant no
read or egress until all of their dependencies hold: a Redis body may not be
fetched before rows 1, 3 and 5, and may not reach the provider before row 6.
Without row 7 and row 8, Redis runs on code, tree and specification text only
and README and LICENSE stay unsent; the licence-history regeneration waits.

## Not on this page

Engine work (reader, chunking, discovery, Agent SDK adapter, multi-page
output) needs no act and is not asked of you. The dossier is a local editorial
draft, never published (Q6).
