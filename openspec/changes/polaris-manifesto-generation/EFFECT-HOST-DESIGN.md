# Generator effect host — implementation decision candidate

Proposed implementation choice for requirements 021/022 and host-overlap rows
H04/H14. This is not permission to provision accounts, start services, read a
project, send content or publish an artifact. The existing PWB host remains intact.

## Separate the protected generator from the legacy host

Use a separate local generator process and browser origin. Its first supported
host is Linux. The loopback default is a distinct loopback address, such as
127.0.0.2, on its configured port; the current PWB host remains on 127.0.0.1.
Binding/ownership and browser behavior must be verified, not inferred from the
example address. A different port on the same host is insufficient cookie
isolation. Host-only generator cookies must not be sent to the legacy host.

The generator owns its route family, principal/session admission and protected
stores. It shares versioned code primitives with the POC through library APIs,
not through a credential-bearing HTTP proxy. Existing PWB machine tokens and
human-open routes confer no generator rights. A registered, read-only navigation
handoff can carry project/selection identifiers, never credentials or a grant.
No legacy route may serve the generator's draft/artifact store.

External machine clients use RFC5-7(a): independent per-client high-entropy
bearer tokens over loopback (or a separately admitted TLS exposure), with only
verifiers stored at rest. Each credential retains its own identity, scopes,
issuance/expiry, owner-declared rotation overlap and next-request revocation.
The recorder Unix socket is a separate service-to-recorder mechanism, not the
external CLI authentication choice.

Browser requests use host-only, HttpOnly, SameSite-Strict sessions with explicit
origin/anti-forgery checks and project/operation scopes. Non-browser calls use a
separate scoped machine credential; mixed credential modes are rejected. Initial
unauthenticated navigation serves only the pairing/login interface, not project
metadata. Missing Origin is not identity or automatic permission: navigation must
satisfy its declared session/navigation-proof rules, and mutations require their
anti-forgery proof. Do not classify trust from User-Agent or loopback location.

Browser pairing requires a fresh owner-attended confirmation on the trusted
supervisor interface, as distinct from machine-client authentication. An
authenticated CLI may prepare a pending request, but cannot by itself mint a
browser grant or attendance proof. The browser's one-use request includes a
fresh nonce and proof-of-possession challenge, bound to the intended origin,
requested scope and expiry. The trusted interface shows that exact request to
the owner and records the explicit attended confirmation before grant issuance.

The recorder's supervisor-only control interface records owner-attendance and
privileged recovery facts. The generator append interface cannot mint those
record classes. Ordinary machine credentials, caller-supplied attendance flags,
TTY presence or a mutable approval file are not attendance proof. A configured
host without a trustworthy attended interface keeps browser pairing unavailable;
it must not fall back to unattended CLI approval.

Redemption consumes the protected attendance/grant record once and verifies the
browser's challenge. The machine credential never enters the browser. This binds
the pairing exchange, not the resulting session to a device or network: afterward
the presented session credential is the identity, with declared lifetime and
next-request revocation. Server stores contain verifiers, not presentable machine
or session credentials. No credential appears in a URL, audit payload, provider
input or ordinary log. Pairing is attended setup, not repeated per editorial pass.

Exposure beyond loopback is a separate configuration/effect decision and requires
authenticated TLS for owner devices. It is not enabled by this implementation
choice. Distinct origin and cookie isolation must hold for any later reverse
proxy configuration as well; path separation alone is not origin isolation.

## A narrow protected recorder

Use a dedicated local recorder process under a different OS principal from the
generator. Its code and service configuration are installed from reviewed bytes
into supervisor-owned, non-writable locations. Its journal and integrity key live
outside governed repositories in a recorder-owned directory. The generator and
untrusted execution profiles have no direct write access to that directory.
The trusted host administrator is outside the excluded-actor threat model.

Three roles are explicit:

| Role | Permitted access |
|---|---|
| Trusted supervisor/administrator | Install reviewed code/configuration, provision principals, perform recorded recovery |
| Generator service principal | Call the recorder's constrained append/query operations; write only its admitted artifact/control homes |
| Untrusted project execution profile | No recorder socket, journal, key, generator credentials or supervisor capability |

The recorder exposes a bounded Unix-domain protocol; socket permissions and peer
credentials admit only the configured service principal. There is no arbitrary
file-path, overwrite, delete or shell operation. An append request identifies an
operation, expected predecessor, event type and bounded metadata. The recorder
supplies authenticated sender identity, sequence and integrity binding; it does
not trust caller-provided actor or acceptance flags. Repeated operation identity
with the same payload resolves to the same receipt; conflicting payloads fail.

The receipt is returned only after durable append. Records form an ordered,
integrity-verifiable chain whose key is not available to the generating actor.
Read/query returns protected records by identity and verifies the stored chain.
Hash chaining alone is insufficient when an excluded actor can replace the file,
key or recorder executable; such a deployment is refused for real effects.

Record only the required control/provenance metadata: actor references, operation
and attempt identities, input/output/effect digests, actual outcome, evaluation
references and necessary usage/uncertainty. Source bodies, prompts, generated prose
and credentials do not belong in this trail. Admitted content uses its separately
permitted retention home. Authored narrative still belongs in its declared intent
home; an application cache does not silently become that home.

Recorder integrity demonstrates receipt integrity, not factual correctness,
human adoption or independently verified owner authority. Those predicates keep
their own evaluators and evidence. The recorder is not a new authority tier.

## Effects, restart and outage

Provider dispatch and authoring/adoption operations require the protected durable
recording stages defined by their operation protocol. A mutable local file, stale
acknowledgement or failed append cannot substitute for a receipt. Where an effect
may already have occurred, retain that uncertainty and resolve by the existing
attempt identity; do not resend because the process restarted.

On startup or reconnect, obtain the authoritative receipt/control position from
the protected recorder. Reject forged, replaced, truncated or mismatched records
and local pointers. An incomplete journal tail is quarantined and diagnosed by
the trusted recovery path; the generator cannot rewrite it into a success record.
Recovery preserves the last verified history and produces its own attributed
record before affected operations resume.

If protected audit is unavailable, refuse new generative, budget-increasing,
adoption and export effects. Preserve the authorized protective-stop exception:
local cancellation, dispatch disabling and response suppression may still occur
under their admitted stop path. Pending stop metadata is explicitly provisional,
not ceremony evidence or proof of provider cancellation. Reconnect reconciles it
against the protected history; unavailable trusted recovery keeps new effects
stopped. Already incurred or unknown usage remains visible.

## Verification before real effects

Use a controlled Linux fixture with genuinely different principals and private
filesystem/socket permissions. Run the attempted journal/key/executable replacement
and socket append as the excluded principal; assert actual denial and unchanged
protected history using an independent read. Run a valid append/query/restart as
the admitted service. A same-user mock is only a unit fixture, not this evidence.

Exercise a lost acknowledgement, duplicate/conflicting operation, tampered local
pointer, forged receipt, damaged journal tail, unavailable recorder and unavailable
trusted recovery across restart. Verify actual effect counts and uncertainty, not
only an error code. During outage prove that an authorized stop prevents new
provider calls without claiming that an in-flight provider stopped.

Verify in real browsers that legacy-host requests receive no generator cookie,
legacy credentials cannot read or mutate generator state, foreign-origin and
missing-proof mutations fail, an authenticated unattended CLI cannot mint or replay an owner-attendance proof,
and repeated valid pairing/rotation/revocation has
the specified scope and next-request behavior. A protected implementation test
fixture does not provision or certify the eventual owner host.
