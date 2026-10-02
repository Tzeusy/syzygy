# R-PUBLIC-ADMISSION-1 — public-repository admission package
Reviewed commit: a1dc043bb3b6f7b7446cc899aa615d18df159f6d
Verdict: REVISE
Reviewer: fresh-context subagent, 2026-10-03

Scope read: every file under
`.syzygy/governance/contracts/candidates/public-repo-admission/` at the
reviewed commit (6 files: `OWNER-DECISION-PACKET.md`, three templates, two
`instances/requests/` records), against SEC-2, SEC-3, SEC-5; RFC5-12…RFC5-17;
RFC5-25; RFC3-16, RFC3-30; RFC4-1; REQ-polaris-generation-001, 010, 011, 017,
025; `ADAPTER-DECLARATIONS.md`; the Scope A direction; the Butlers observation
consent precedent; `docs/polaris-generation/TARGETS.md`; the policy JSON.
`git rev-parse HEAD` equalled the reviewed commit before reading.

Verified true [Observed]: the T1 revision id matches TARGETS.md line 37, and
`git ls-remote https://github.com/psf/requests 'refs/tags/v2.34.2*'` (refs
only) returns `6e83187b8feb273ed4c6cdab5efd8d54901dfab3` with no `^{}` peeled
line, so the tag is lightweight and the id is the commit. The policy file
exists and carries performed acts (`decisions/PWB-SECRET-CLASSIFICATION-POLICY-ACT.md`,
`-AMENDMENT-ACT.md`, `-BEHAVIOR-CONTRACT-REPIN-ACT.md`). The generator
specification is adopted (PROJECT-STATUS.md line 28; proposal status banner),
and none of REQ-001/010/017/025 is replaced by the understanding amendment
(which modifies 002, 004, 006, 009, 012, 014, 019). Scope A item 1 covers
exactly "the PWB specification deltas, the observer registry entry and the
contract successors queued behind them", as Q5 says. The kit's "Start here"
step 4 does propose route and retention as kit controls, as Q3 says. PR #120
exists, open, "draft three test-only self-observation acts". Each instance
differs from its template only in filled fields and the header note (`diff`
run on both pairs).

## Findings

1. **blocking — observation scope contradicts itself on which revisions are read.**
   `templates/OBSERVATION-CONSENT-TEMPLATE.md` lines 28 and 36–37 (and
   `instances/requests/OBSERVATION-CONSENT.md` lines 32 and 40–41):
   "Read-only reads of exact Git objects reachable from the admitted
   revisions" versus "The scope excludes: - any revision not listed above".
   Every ancestor commit of `6e83187…` is a Git object reachable from the
   admitted revision and is also a revision not listed, so the record both
   grants and excludes the entire history. The packet states a third scope,
   line 38–39: "read-only reads of exact Git objects at the pinned revisions".
   Separately, template line 36–37 excludes "any working tree other than the
   scratch clone", which implies the clone's working tree is in scope although
   the grant is Git objects only (the existing policy sets
   `accessBoundary.workingTree: false` and `sourceAdmission.gitObjectsOnly:
   true`). Governing clause, RFC5-12: "Every consent record names its class,
   subject, scope, granting principal, grant instant, and revocation state."
   A scope that admits and excludes the same objects does not name a scope.
   Repair: state one population, e.g. "the commit object at each admitted
   revision, its root tree, and the trees and blobs reachable from that tree;
   no ancestor commit, other ref, or commit metadata beyond the admitted
   commit", make the packet line 38 say the same, and replace the working-tree
   exclusion with "any working tree, including the scratch clone's (reads are
   Git objects only)".

2. **blocking — under the Q4 recommendation the screening policy is not the observing project's.**
   `instances/requests/OBSERVATION-CONSENT.md` line 18: "Subject:
   `(project:oss-requests, repository:psf-requests)`"; packet lines 85–86:
   "`project:oss-requests` observing `repository:psf-requests`"; packet lines
   28–30: the screening scope is "An extension of the observing project's
   secret-classification policy (currently
   `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json` …)".
   That policy declares `"policyOwningProject": "project:syzygy"` and
   `"observingProject": "project:syzygy"`. With `project:oss-requests` as the
   observing project, extending project:syzygy's policy screens oss-requests'
   ingest under another project's policy. Governing clauses, RFC3-30: "Project
   A observing repository R requires A's own consent record for R" and
   "**Governing policy is a property of the *observing* project's governance
   root.** Project A screens, bounds, and classifies everything it ingests
   under **A's** policies in A's own plane"; RFC5-16: "The governing policy is
   the observing project's own (RFC3-30)". The Butlers precedent puts the
   observing project in the subject: `(project:syzygy,
   repository:butlers-configured-poc)`. Acceptance criterion 3 cannot be
   verified because the package never says which project observes and where
   its governance root is. Repair: either (a) keep `project:syzygy` as the
   observing project in every observation subject and say the per-target
   project identity applies to egress and rendering only — then re-argue Q4,
   since RFC5-12 makes egress per (Project, provider) and the subject of each
   egress record must be a Project that owns the content; or (b) keep one
   project per target and state that each target project's governance root is
   declared in Syzygy's plane and that the public-source scope is adopted as
   *that* project's policy (one policy act per project, or a declared shared
   policy whose owning-project field names each), and put this trade-off into
   Q4 as part of the question.

3. **blocking — Q4's recommendation is filled into both instances unmarked, presented as decided.**
   `instances/requests/OBSERVATION-CONSENT.md` line 18 and
   `instances/requests/EGRESS-CONSENT-ANTHROPIC.md` line 18 fill `project:oss-requests`
   with no "pending Q4" marker, while both headers (lines 5–6) say "Fields
   marked "pending Q…" follow the packet's open questions and change if the
   owner answers differently", which tells a reader that unmarked fields do
   not depend on an open question. Packet line 61: "None is decided by this
   packet." Governing: acceptance criterion 6 ("no recommendation is
   presented as decided"); VIS-4 (only the owner decides). Repair: mark the
   Subject line in both instances "— pending Q4" (and the Record ID if Q4
   changes the identity), and check every other filled field for a
   dependency on Q1–Q6.

4. **blocking — Q5 rests on a false premise and omits the clause the recommendation would bend.**
   Packet lines 97–98: "Without it, each record needs the digest-and-phrase
   act form." Not true of the repository's records: PROJECT-STATUS.md line
   227 records the 2026-10-02 superseding policy and registry acts as "two
   separate superseding state-(1) acts, each bound to its artifact's own
   SHA-256 … Given by one option selection ("A + B + C now"), not typed
   phrases". So a third form exists — option selection, digest-bound, no
   typed phrase — and it is the form already used for this very policy. Q5
   also does not disclose that the records it would move to a no-digest tag
   are ones accepted contracts say are honoured only through a digest-bound
   act. RFC5-16: "the policy is honored **only under RFC3-16(a)**, through an
   effective owner act bound to its exact digest"; RFC3-16: effective status
   "is determined by an **owner-act record** (RFC3-16(a)/(b)) binding the act
   to the artifact's **exact immutable content digest**"; REQ-025: "screened
   under the observing project's secret policy with effective exact-digest
   act". Scope A item 1 says "No typed phrase and no digest argument is
   required." Whether a git tag on a commit satisfies RFC3-16(b)'s exact-digest
   binding for a policy and consent records that RFC5-15 gates egress on is an
   open question the owner should see before choosing; extending Scope A to
   them may be a contract question (an escalation trigger), not a plain
   direction. Also, `scripts/record_versioned_signoff.py` requires a package
   builder check and a `Manifest SHA-256` line in the raw head (docstring
   steps 3 and 6); this package has neither, so "each target's admission is
   one structured question" needs tooling the packet does not mention.
   Repair: rewrite Q5 with three options (status quo phrase-and-digest;
   option selection bound to each record's SHA-256, as on 2026-10-02; Scope A
   tag extension), quote RFC5-16 / RFC3-16(a) beside the third, state that
   whether a tag satisfies them is unresolved, and recommend the second (or
   argue the third against the clause).

5. **note — RFC4-1 paraphrased as a permission.** Packet lines 46–47: "RFC4-1
   permits one registered adapter per project per external authority". RFC4-1:
   "Every external authority is reached through exactly one registered adapter
   per project; nothing else in Syzygy touches that authority directly." It is
   a requirement and an exclusivity rule, not a permission. Repair: "RFC4-1
   requires exactly one registered adapter per project per external authority".

6. **note — REQ-001's scenario is cited as requiring distinct projects.** Packet
   lines 87–89: "REQ-polaris-generation-001's first scenario ("Two project
   identities") asks for distinct identities". The scenario: "**WHEN** two
   independently admitted snapshots from distinct project domains are
   supplied … **THEN** the unchanged generator accepts each with its own
   project identity". It tests that the generator supports distinct project
   identities when given them; it does not require that each public target be
   its own project. Repair: "REQ-001's first scenario shows the generator
   supports one identity per project; it does not decide this question" and
   let the egress-revocability argument carry the recommendation.

7. **note — the review requirement is attributed to Scope A, which does not cover this package.**
   Packet lines 114–115: "Per Scope A item 3, a fresh-context round returning
   CONFIRM, or CONFIRM WITH EXCEPTIONS with notes only, precedes offering it."
   Scope A item 1 limits the direction to "the PWB specification deltas, the
   observer registry entry and the contract successors queued behind them",
   and packet line 95 itself says it covers "not consent or policy records".
   Repair: cite the review requirement's own source (CC-REV / the act ceremony
   for digest-bound records) or say "by analogy with Scope A item 3, pending
   Q5".

8. **note — the one-paragraph summary understates the per-target work.** Packet
   lines 20–21: "admitting a new target means filling the same two templates
   and signing them, plus a one-time policy act shared by every target." Lines
   35 and 45–51 add a per-target registry entry with its own act. Repair: "two
   templates and one registry entry per target, plus a one-time policy act".

9. **note — the screening-scope outline contradicts the policy it extends.**
   `templates/PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md` lines 9–10: "The same
   secret detectors and exclusion rules as the existing policy", and lines
   24–26: "Executable configuration (install scripts, CI workflows, build
   files) may be read as text, is never executed, and is classified
   `code-content`." The existing policy excludes active content outside inert
   Markdown contexts as a whole-artifact exclusion (`activeContentClassification`,
   `malformedContextAction: exclude-whole-artifact`; AGENTS.md records 7 of 13
   `butler.toml` withheld because "TOML has no inert context"), and sets
   `accessBoundary.networkEgress: false` and `rawBodyHandling.externalEgress:
   "never"`. Under "the same … exclusion rules" `pyproject.toml`, `setup.py`
   and CI YAML would be withheld, and no body could leave under any egress
   consent. Repair: say which existing rules carry over (detectors, denied
   paths, unclassifiable exclusion, hash-not-body) and which the public scope
   replaces (active-content handling for non-Markdown files; the egress
   fields), so the owner sees the widening; REQ-025 "Existing
   project-specific admission, grammar and policy gates SHALL NOT be widened
   by generic schema support or fallback" makes that explicit statement
   necessary even though the Butlers scope is untouched.

10. **note — general documentation is mapped to `governance-text`.**
    `templates/PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md` lines 15–16: "prose
    documentation, specifications, RFC-like design docs, licences →
    `governance-text`". RFC5-14: "`governance-text` | Doctrine, spec,
    decision, policy text", and "The content-class vocabulary is closed at
    this RFC (amend to extend)". READMEs, tutorials and API guides are none of
    those four. Under Q2's recommendation the consequence is nil (both classes
    are permitted), but a later consent omitting `code-content` would still
    admit a tutorial full of code. Repair: flag the mapping as an owner
    classification choice in the outline, or map non-normative prose to
    indeterminate until a run needs it.

11. **note — egress record names no explicit scope or provenance state.**
    `templates/EGRESS-CONSENT-TEMPLATE.md` has no "Scope" field; the
    observation template (line 26) and the Butlers precedent (line 33) do.
    RFC5-12: every record "names its class, subject, scope …". The content
    classes and Conditions arguably are the scope, but say so. Neither template
    states which RFC3-16(c) provenance state the act would carry; the
    precedent does (lines 64–71: "state (1) under RFC3-16(c) … never
    'independently verified'"), and RFC5-15 requires "the exact state of each
    act is disclosed". Repair: add "Scope: transmission of the permitted
    classes, from content admitted under `PUBLIC-OBS-…`, to this provider via
    the registered route" and a "Proposed provenance state" line to both
    templates.

12. **note — REQ-010 is cited for more than it says.**
    `templates/EGRESS-CONSENT-TEMPLATE.md` lines 38–40 (instance 46–48):
    "Provider output is editorial inference: it never becomes an Observed
    claim, adopted intent or the target project's own statement
    (REQ-polaris-generation-010)." REQ-010: "A generated bundle SHALL remain
    editorial-draft until the existing effective-owner-act predicate … admits
    an attributed per-block authorship act" and its scenario "neither
    underlying intent adoption nor release authority is implied". It does not
    speak to Observed tier or to the target project's own statement, and it
    does let attested blocks gain curated status. Repair: "remains editorial
    draft unless a per-block authorship act admits it, and never implies
    intent adoption (REQ-polaris-generation-010)"; cite VIS-2 / the
    Inferred-label rule for "never Observed".

13. **note — "pending" text would be inside the signed bytes.**
    `instances/requests/EGRESS-CONSENT-ANTHROPIC.md` lines 1, 20, 32, 34
    ("— pending Q1", "— pending Q2.", "— pending Q3."). If the owner answers as
    recommended, the act would bind a consent record whose provider and
    retention fields say "pending". Repair: state in the header that the
    markers are stripped and the record re-versioned (`0.1.0-candidate.2`)
    after the owner answers Q1–Q4, and that only the stripped bytes are
    offered for the act.

14. **note — revocation sentence omits the dependent-claim consequence.**
    `templates/OBSERVATION-CONSENT-TEMPLATE.md` lines 50–52: "Revocation is
    prospective (RFC5-13): it stops future reads; records made under the
    consent remain, shown as withdrawn." RFC5-13: revocation "stops future acts
    (RFC5-11) and renders dependent claims Unknown
    (`unconsented-source-or-provider`, RFC2-24 #6) at the next evaluation".
    Repair: add "and claims depending on this repository render Unknown
    (`unconsented-source-or-provider`) at the next evaluation".
