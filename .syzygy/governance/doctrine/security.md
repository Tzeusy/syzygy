# Security and blast radius

Trust-model doctrine for a service that indexes a whole portfolio, listens on a
network, executes observed-project code, and writes into repositories it
governs. Constitutional constraints only; execution-profile and authentication
contracts are RFC material — these are the rules those RFCs must satisfy.

## Non-negotiable rules

**SEC-1 — Authenticated by default.** Syzygy's endpoints and UI are reachable
without authentication only on the loopback interface, and client classes are
distinguished even there: **browser requests must pass origin/CSRF
protections, including on loopback** (browser-originated `localhost` calls and
DNS rebinding are in scope as attackers); **non-browser agent and CLI clients
are admitted only through an explicit machine-client authentication
mechanism**; loopback location alone is never proof of client identity; and an
absent browser Origin header is neither automatically trusted nor treated as a
browser-origin violation. The mechanism is authentication-RFC material. Any
exposure beyond localhost requires authenticated, TLS-protected access limited
to the owner's own devices; an unauthenticated network-exposed configuration
is never the default. *Violation:* a fresh install serving portfolio data on a
LAN address with no credential; a loopback endpoint answering an arbitrary web
page's fetch; a machine client admitted on loopback location alone.

**SEC-2 — Portfolio data leaves owner-controlled infrastructure only through
explicit, scoped consent.**
Governed-project content — source structure, specs, work history, and anything
derived from them, including prompts — is never transmitted to a store or
service the owner does not control without explicit, recorded, per-project
consent. **Model providers are such services.** Onboarding consent must name
the providers permitted for a governed project and the content classes that may
be sent; Syzygy renders that consent on the project's surface; providers not
named require fresh consent; absent consent, the inferred layer renders
Unknown rather than being computed. Remote backing dependencies are permitted
under the same consent rule. *Violation:* an index synced to a third-party
service as a side effect of a feature; project source sent to an unnamed model
provider.

**SEC-3 — Observed code is untrusted, everywhere.** Observed-project code executes
only inside an explicit, opt-in execution profile — default-deny, isolated
credentials, declared network access, resource limits, destructive-operation
gates — and is treated as untrusted regardless of who owns the project. The
profile contract is RFC material and blocking: no observed-project code
executes until that RFC is accepted. *Violation:* an execution profile that
inherits the host user's ambient credentials "for convenience."

**SEC-4 — Writes are consented, attributed, and revertable.** Syzygy writes into a
governed repository only after recorded per-repository consent (onboarding),
and every write is attributed to Syzygy, atomic, and individually revertable.
Syzygy never overwrites existing governance artifacts it did not author without
surfacing the conflict. *Violation:* first-pass doctrine drafting silently
replacing an existing `.syzygy/governance/` tree.

**SEC-5 — Secrets are never indexed.** Observation applies a declared
secret-detection policy (`.syzygy/governance/`); content matching it is
excluded and the exclusion is rendered; content that cannot be classified is
excluded, not indexed — unclassifiable fails closed. A secret reproduced in
any Syzygy surface, store, or endpoint is a trust-floor violation
(trust-and-evidence.md, floor bullet 4). *Violation:* a connection string
appearing in a map tooltip or API response.
