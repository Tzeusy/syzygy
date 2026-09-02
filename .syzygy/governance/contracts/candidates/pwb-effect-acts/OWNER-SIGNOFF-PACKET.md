# Owner sign-off packet — the three Butlers observation authorities

Frozen candidate commit: `48e0f5db645d1fb08e5e3a65c5e50dbcece40412`

Manifest: `.syzygy/governance/contracts/candidates/pwb-effect-acts/PWB-EFFECT-ACTS-MANIFEST.txt` (SHA-256 `d259c3798b2961489d31c55af09e86c9711c0cfd4e5ec626211fdc2447a54150`)

Act semantics: `.syzygy/governance/contracts/candidates/pwb-effect-acts/ACT-SEMANTICS.md`

## What you are being asked

Before Syzygy may read any Butlers project-shape file, three separate things
need your act: consent to observe Butlers, approval of the secret-screening
policy that runs on everything read, and adoption of the registry entry that
says exactly what the observer may read. This packet offers all three. Each
phrase below is one act on one file, bound to that file's exact SHA-256. You
may perform one, two or all three; a body read needs all three.

Performing an act here is a **state-(1)** act: owner-trusted, uncorrelated, and
same-tree forgeable from Syzygy's perspective. Its digest detects later drift;
it does not prove authorship or attendance. No independent audit trail (A1)
exists, and the act records that absence explicitly. This is the trust model
you selected on 2026-08-31 and signed into PWB-REQ-005 on 2026-09-02.

## The three files

**1. Observation consent** — `.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md`
SHA-256 `5d705d75f993059d5ae5561b1a6f99d143462d9d2e5bcea8ecc9b0c258777841`

Records your 2026-08-31 statement ("you have consent for butlers observation;
obviously don't read secrets from butler") as a consent record for the pair
(project:syzygy, repository:butlers-configured-poc), content class
`declared-project-shape-text`. Scope: read-only Git objects selected by the
signed PWB source population, at the Butlers revision the POC observes. It
excludes PostgreSQL, credential stores, secret APIs, `.env` and credential
files, arbitrary implementation-file bodies, working-tree traversal, code
execution, network egress, writes to Butlers and any second repository. No
silent expiry; you may narrow or revoke by a later act. It does not
retroactively authorize the reads recorded in the precondition-read incident.

**2. Secret-classification policy** — `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`
SHA-256 `513a3be75bbd417a06d475c46bb423393ac59013e307157357083f29781a2a61`

Syzygy's own concrete policy for screening Butlers bytes before anything is
modeled. Denied filenames and suffixes (`.env*`, `credentials.json`,
`secrets.json`, `id_rsa`, `id_ed25519`, `.pem`, `.key`, `.p12`, `.pfx`), four
detectors (private-key blocks, known token formats, credential assignments,
credential-bearing URLs), strict UTF-8 without NUL, and a closed extraction
class per source. Any match or anything unclassifiable excludes the whole file;
only its hash, path, policy id/version and the detector id or exclusion
reason are retained. Raw bodies
are never stored, logged, rendered, returned or sent anywhere.

**3. Observer registry entry** — `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
SHA-256 `d71eadb612cf657983d96ad44415b832054dc37e51ea674e569d9b8f655d05d7`

The governance-plane entry for the observer `polaris-butlers-project-shape`.
Read-only authority: phase A reads only the Butlers top-level README, the pillar README
indexes it names and Git tree metadata; phase B reads only the exact Git
objects in the resulting revision-bound manifest. Empty write surface, no
database access, no network access, no observed-code execution, no
working-tree reads, fixed resource limits. The implementation path it names
does not exist yet; adopting the entry authorizes no implementation.

## What this does and does not do

- All three acts together satisfy PWB-REQ-005's authority precondition in
  state (1). They are warrants, not evidence that any read, screening or
  derived claim succeeded.
- They do **not** authorize PWB implementation (task 1.8 is a separate act),
  any write, egress, execution, deployment, release, recovery, mission, a
  second repository, autonomous behavior or multi-user support.
- Nothing reads Butlers as a result of these acts. A read can only happen once
  an authorized implementation evaluates all three acts and finds them valid.
- Each act is recorded in `.syzygy/governance/decisions/` and appended to
  `ACCEPTANCE-ACT-RECORD.md`, with a tag on the recording commit. Editing any
  of the three files afterwards breaks its act; changes go through a new act.

## Evidence

- Fresh-context security and authority-boundary review of the original
  frozen subject `2fda7c440d996a5c58e6cf8577361520a0f1dca0`: `docs/reviews/R-PWB-EFFECT-ACTS-SECURITY-RAW.md`,
  verdict `CONFIRM` with two non-blocking findings, sha256
  `ef3010fce6eb0c55004f8cde1f09d92fe9a1cd068db70bec57fd5bde2b293d94`. One finding was repaired (the policy now names
  every closed redaction class); the other is closed by the act record
  freezing the reviewed commit.
- Fresh-context confirmation review at this exact commit and manifest:
  `docs/reviews/R-PWB-EFFECT-ACTS-SECURITY-CONFIRMATION-RAW.md`, verdict `CONFIRM`, sha256 `98bd5131c3f15b70e9d5172ad0aa92d094f6a67dc144e21a2d9f913c6d1e9549`.
- The manifest generator reproduces this closed three-row population and
  mutation-proves byte and path drift (`--selftest`).

## Exact owner responses

Each line is one act. Write exactly the line(s) you intend, and nothing else
on that line. State (1) is selected by performing the phrase; the recorder
writes the A1 audit-record identity as absent.

```text
CONSENT TO BUTLERS PROJECT-SHAPE OBSERVATION: 5d705d75f993059d5ae5561b1a6f99d143462d9d2e5bcea8ecc9b0c258777841
```
```text
APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY: 513a3be75bbd417a06d475c46bb423393ac59013e307157357083f29781a2a61
```
```text
ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY: d71eadb612cf657983d96ad44415b832054dc37e51ea674e569d9b8f655d05d7
```
