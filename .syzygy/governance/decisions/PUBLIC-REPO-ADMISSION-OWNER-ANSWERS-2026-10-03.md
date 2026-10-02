# Owner direction — answers to the public-repository admission questions

Date: 2026-10-03

Owner: Tzeusy

Decision ID: `PUBLIC-REPO-ADMISSION-ANSWERS-2026-10-03`

Offering: `.syzygy/governance/contracts/candidates/public-repo-admission/OWNER-DECISION-PACKET.md`,
questions Q1–Q7, plus one question on review sequencing. The packet remains
the question; its drafts are regenerated to follow these answers.

This is a plain owner direction in the shape of
`POLARIS-RESPONSE-CEILING-READING-DIRECTION.md`. It binds no artifact digest,
adds no row to `ACCEPTANCE-ACT-RECORD.md` and registers nothing. It performs
no act: no consent, policy or registry entry takes effect by it. Each record
still needs its own act over its exact bytes, as Q5 below describes.

## The owner's words

On 2026-10-03, in the Claude Code CLI, the owner asked to be walked through
the packet's questions and answered eight structured questions in two
batches. Each question as put and the option selected, with its description
as shown, verbatim:

| Question | Selected label | Selected description |
|---|---|---|
| "Q1 — Which model provider may receive content from the public targets? The egress consent must name one; the model is recorded per run, not fixed in the consent." | "Anthropic, via Claude Code / Agent SDK" | "Same provider, but run through a Claude Code session or the Agent SDK. Uses your existing subscription, but the request/response capture is less direct, so the egress check and audit record need extra work." |
| "Q2 — Which content classes may be sent? RFC5-14's closed list: governance-text, code-structure, code-content, work-history, evidence-content, derived-composites." | "All but work-history (Recommended)" | "Specs and design docs, paths and symbols, source and test bodies, committed reports, and prompts built from them. Issues, PRs and CI history stay out. Understanding a codebase needs its bodies, and these repos are public." |
| "Q3 — Where do provider requests and replies (which contain the source spans sent) get retained?" | "Run directory, outside git (Recommended)" | "Requests, replies and run records stay in a per-run directory under Syzygy's state directory, never in git, logs or machine responses. Lets us inspect and replay runs; delete the run to delete the spans." |
| "Q7 — READMEs, guides, tutorials and LICENSE files fit none of RFC5-14's content classes, so today their egress is refused. Yet they are the best evidence of what a project is for, and Redis's licence test depends on LICENSE. How do we handle that?" | "Amend RFC5-14; T1 starts without (Recommended)" | "Draft an RFC-0005 amendment adding a class such as project-documentation (needs its own act). Meanwhile T1 (requests) runs on code and specs only and records what it couldn't send, which is a useful baseline in its own right." |
| "Q4 — Who is the observing project? It decides whose screening policy applies (RFC3-30)." | "Syzygy observes each target (Recommended)" | "Like Butlers: project:syzygy observes repository:psf-requests and so on. One policy and one egress record cover all targets. The cost: that egress record is the only (syzygy, Anthropic) record, so any future Butlers or Syzygy egress to Anthropic would be a new version of it." |
| "Q5 — How do you sign each target's records? They must be bound to exact bytes under RFC3-16(a)." | "One question per target, at manifest rows (Recommended)" | "As with the 2026-10-02 policy re-pin: you pick one option naming the records at their manifest rows (no typed phrase, no digest to read), stated as state (1) owner-adopted bootstrap. A recorder writes the act records." |
| "Q6 — Where may generated pages for public targets be shown?" | "Local only, editorial draft (Recommended)" | "A static file in the run directory now, and the daemon's /polaris/draft/<runId> view once built. Always labelled non-release editorial draft; never published or presented as the project's own site." |
| "Review — the round-3 repair is unreviewed. When should the confirming review run?" | "After applying these answers (Recommended)" | "I regenerate the records with your answers, then run one fresh-context review over the final bytes. The answers change the wording anyway, so reviewing now would be retired immediately." |

## The direction

1. The admission drafts follow the eight answers above.
2. **Q1 consequences, as the drafter reads them [Inferred].** The provider
   route is the Claude Agent SDK runtime. Two conditions follow and are
   written into the egress record: the route runs with every tool the
   runtime offers disabled, so the model sees only what each request
   carries; and any session transcript the runtime persists locally is
   retained material, kept in the run directory under Q3. Whether the
   runtime can be configured not to persist a transcript is [Unknown] until
   the adapter is built.
3. **Q7.** An RFC-0005 amendment adding a content class for project
   documentation is drafted as its own candidate package with its own act.
   T1 runs without that class and records what it could not send.

## What this does not do

It performs no act, grants no read, egress, write or execution, and edits no
act-bound byte. Withdrawal defeats grant: a later direction may change any
answer.
