# 07 — Client Trust Boundaries

> **Reviewed draft — grounded in proposed foundational contracts (currency note, not an ordering precondition: this bundle's own gate is §2 act 3 of the acceptance record and does not wait on the RFC act).** Reviewed fresh-context (reviews 5–7, dispositions recorded); updated at the rev7 rework for the corrected contracts (D1 historical scope, five governance categories, walkthrough three-way split, captured external confirmation, `Base` scenario context). Becomes canonical only by its **own owner act** — `ACCEPT TOPOLOGY: <bundle-manifest-digest>`, binding the exact digest of every file in the bundle — never implicitly on the RFC gate (RFC3-16: this stamp is a self-declaration; effective status lives in the owner-act record).
>
> Rendering: Mermaid is the durable, renderable fallback chosen for this phase; an Excalidraw + SVG upgrade is a tracked follow-up.

## What this shows

Who may talk to Syzygy and through what: the two client classes, the three
closed exposure modes, classification by credential (never location), and
where the consent gates sit between an admitted client and any effect.

```mermaid
flowchart TB
    subgraph Clients["Clients"]
        B["Browser (owner's devices)"]
        M["Machine clients —<br/>agents / CLIs, own credentials,<br/>never the owner's (RFC5-1)"]
        Anon["Unauthenticated visitor —<br/>including hostile local processes<br/>and DNS-rebinding pages (SEC-1)"]
    end

    subgraph Modes["Closed exposure-mode set (RFC5-8) — fresh install serves loopback ONLY (RFC5-10)"]
        Loop["Loopback —<br/>cleartext permitted; identity NEVER<br/>inferred from location"]
        Tail["Tailnet (Tailscale Serve / TLS) —<br/>device identity satisfies device restriction,<br/>never client classification (RFC5-9)"]
        LAN["Owner-configured TLS LAN —<br/>Syzygy-layer auth is the only identity"]
    end

    subgraph Syz["Syzygy boundary [target] — SEC-1"]
        Class{{"Classification by credential presented,<br/>never network location or header heuristics (RFC5-3)"}}
        Sess["Browser discipline, even on loopback:<br/>owner-attended session + anti-CSRF proof<br/>+ Host validation vs DNS rebinding (RFC5-4)"]
        Cred["Machine credential:<br/>owner-issued ceremony, scoped deny-by-default,<br/>rotatable, revocable at next act (RFC5-6/11)"]
        Open["Closed unauthenticated set:<br/>liveness/health + auth bootstrap only —<br/>no portfolio data (RFC5-5)"]
        Gates["Consent gates per act (RFC5-12):<br/>observation / write / egress / execution —<br/>each class its own revocable record"]
        Data["Portfolio data, endpoints, adapter effects —<br/>every act audited (RFC5-25)"]
    end

    B -->|"HTTPS or loopback"| Modes
    M -->|"HTTPS or loopback / OS-mediated channel"| Modes
    Anon -->|"reaches only"| Open
    Modes -->|"every request"| Class
    Class -->|"no machine credential ⇒ browser class"| Sess
    Class -->|"valid machine credential ⇒ machine class"| Cred
    Sess -->|"authenticated ≠ authorized: scopes checked per act (RFC5-1c)"| Gates
    Cred -->|"scope check per act"| Gates
    Gates -->|"admitted acts only; same fact set + labels for both classes (RFC6-13)"| Data
```

## Trust boundaries

- **Location is never identity** [Observed: SEC-1; RFC5-3]: loopback gets
  the full discipline; a browser page's fetch of `localhost` must fail
  origin validation and the anti-forgery proof structurally. An absent
  Origin header neither admits nor condemns.
- **Two credential populations plus one more** [Observed: RFC5-2/24]:
  browser sessions, machine credentials, and Syzygy's own adapter
  credentials are disjoint; none is transferable, and an execution profile
  can never name an adapter credential as injectable.
- **Fail closed** [Observed: RFC5-8]: an unauthenticated network-exposed
  configuration is invalid — Syzygy refuses to serve rather than serve it.
- **Acts vs claims** [Observed: RFC5-11]: revocation of a credential,
  consent, or profile takes effect at the next act, immediately; only the
  rendering of its consequences flows through identified evaluations.
- **Execution consent is the fourth gate** [Observed: RFC5-18]: observed
  code runs only under an owner-approved execution-profile version —
  default-deny credentials, declared network, resource limits, destructive
  operation gates (SEC-3); blocked entirely until RFC 0005 is accepted.

## [target] vs already true

- **[target]:** everything — no daemon, endpoint, session, credential, or
  profile machinery exists. The machine-client mechanism itself is an open
  enumerated choice for acceptance (RFC5-7; RFC 0005 §8 q1).
- **[Observed] today:** SEC-1..5 are adopted doctrine; the platform posture
  (local-first daemon + browser app, owner devices only) is recorded scope
  (v1.md) and remains RFC-open.
- **[Inferred]:** the tailnet mode reflects the owner's current device
  topology (FD-029/OQ-007); the class is "owner-controlled overlay with
  device identity and TLS," so Tailscale itself is substitutable.
