#!/usr/bin/env python3
"""Build and verify the inert Syzygy self-observation act packets (P-74 Q3).

This script performs no owner act and writes no act record. The package
prepares three separate owner acts for one test-only self-observation of
this repository (`project:syzygy`, `repository:syzygy`):

1. a consent record — a new file, drafted in full under `proposed/`;
2. a second adapter-registry entry — a new file, drafted in full under
   `proposed/`; and
3. a self-observation scope added to the secret-classification policy — the
   policy's current bytes are the argument of a performed `approve-policy`
   act, so the proposed bytes live only as one unified diff under
   `proposed/`, never in place.

Each act has its own manifest. Rows 1 and 2 hash the drafted files, which
are installed byte-for-byte at adoption, so the row is the act argument.
Row 3 hashes the policy's current bytes with the diff applied.

`--check` compares, by exact value, everything each draft says about what
may be read, how, and where the result may go: the consent's head and its
whole `## Scope` section, the registry file's head, its entry's key set and
eleven of its values, and the policy's whole self-observation scope. It
also checks the values it does not pin (the pair, the observer version, the
PWB specification digest, the source population and the limit semantics),
that each new install target is free (act pending) or holds exactly the
proposed bytes (act installed), that the policy either takes the patch
(pending) or already holds its result (installed), that no sibling
candidate package patches or drafts any of the three targets, that every
manifest is an exact regeneration, and that the owner packet quotes the two
new-file arguments at their current digests and offers no policy argument.
The pins live here, not in the drafts, so `--write` can never regenerate a
manifest over a widened draft. It holds before, between and after the
three adoptions, in any order, and `--apply` refuses an act that is already
installed. Bare invocation refuses to overwrite the
manifests; pass `--write` to regenerate them.
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import itertools
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
CANDIDATES = pathlib.Path(".syzygy/governance/contracts/candidates")
PACKAGE = CANDIDATES / "pwb-self-observation-acts"
PROPOSED = PACKAGE / "proposed"
PACKET = PACKAGE / "OWNER-DECISION-PACKET.md"

CONSENT_NAME = "SYZYGY-SELF-PROJECT-SHAPE-OBSERVATION-CONSENT.md"
REGISTRY_NAME = "POLARIS-SYZYGY-SELF-PROJECT-SHAPE-OBSERVER-CANDIDATE.json"
POLICY = pathlib.Path(
    ".syzygy/governance/policies/"
    "POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json")
POLICY_PATCH_NAME = f"{POLICY.name}.patch"
BUTLERS_REGISTRY = pathlib.Path(
    ".syzygy/governance/declarations/adapter-registry/"
    "POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json")
SPEC = pathlib.Path(
    "openspec/changes/polaris-project-wide-butlers-model/specs/"
    "polaris-project-wide-butlers-model/spec.md")

#: act key -> (label, install target, manifest, manifest title)
ACTS = {
    "consent": (
        "CONSENT TO SYZYGY SELF PROJECT-SHAPE OBSERVATION",
        pathlib.Path(".syzygy/governance/decisions") / CONSENT_NAME,
        PACKAGE / "SELF-OBSERVATION-CONSENT-MANIFEST.txt",
        "SYZYGY SELF-OBSERVATION CONSENT MANIFEST"),
    "registry": (
        "ADOPT POLARIS SYZYGY SELF PROJECT-SHAPE OBSERVER REGISTRY ENTRY",
        pathlib.Path(".syzygy/governance/declarations/adapter-registry")
        / REGISTRY_NAME,
        PACKAGE / "SELF-OBSERVATION-REGISTRY-ENTRY-MANIFEST.txt",
        "SYZYGY SELF-OBSERVATION REGISTRY ENTRY MANIFEST"),
    "policy": (
        "APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY",
        POLICY,
        PACKAGE / "SELF-OBSERVATION-POLICY-EXTENSION-MANIFEST.txt",
        "SYZYGY SELF-OBSERVATION POLICY EXTENSION MANIFEST"),
}
PROPOSED_POPULATION = sorted((CONSENT_NAME, REGISTRY_NAME, POLICY_PATCH_NAME))

OBSERVING = "project:syzygy"
OBSERVED = "repository:syzygy"
CONTENT_CLASS = "declared-project-shape-text"
BUTLERS_OBSERVED = "repository:butlers-configured-poc"
POLICY_CURRENT_VERSION = "1.1.0-candidate.1"
POLICY_PROPOSED_VERSION = "1.2.0-candidate.1"
#: The only ingest boundaries the self scope may name. Every one of the base
#: scope's served or stored boundaries (cache, log, walkthrough-record) is
#: outside it.
SELF_BOUNDARIES = ("observation", "model", "human-html", "machine-json")
SELF_OBSERVER_ID = "polaris-syzygy-self-project-shape"
SELF_OBSERVER_VERSION = "1.0.0-candidate.1"
#: The closed source population the consent, the policy scope and the
#: registry entry all name: one index, and the five files it links to.
DOCTRINE = ".syzygy/governance/doctrine/"
SELF_PHASE_A = (f"{DOCTRINE}README.md",)
SELF_PHASE_B = tuple(f"{DOCTRINE}{name}" for name in (
    "architecture.md", "security.md", "trust-and-evidence.md", "v1.md",
    "vision.md"))
#: Everything each draft says about what may be read, how, and where the
#: result may go, pinned by exact value, so `--write` can never regenerate a
#: manifest over a widened draft. The consent's head (title to revocation
#: state) and its whole `## Scope` section are compared whitespace-normalized;
#: the registry and policy values are compared as parsed JSON.
CONSENT_HEAD = (
    ('# Syzygy self project-shape observation consent (test-only) Date: '
     '2026-09-26 (drafted); the act, if performed, records its own instant '
     'Owner: Tzeusy Record ID: `PWB-SELF-CONSENT-2026-09-26` Record version: '
     '`1.0.0-candidate.1` Consent class: observation Observation content '
     'class: `declared-project-shape-text` Subject: `(project:syzygy, '
     'repository:syzygy)` Current locator: the root of the Syzygy checkout '
     "that runs the conformance test, resolved from that checkout's own Git "
     'metadata at test time (configuration, not repository identity) Purpose: '
     'test-only. This consent exists for one conformance fixture that '
     "measures the project-shape pipeline against this repository's own "
     'tracked tree (M8 slice 6). Nothing observed under it is served to any '
     'reader. Status: **candidate; no effect until the owner acts on this '
     'exact digest** (self-declared stamp; effective status comes only from '
     'an owner-act record, RFC3-16) Proposed revocation state: active; '
     'supersedes no earlier consent'))
CONSENT_SCOPE = (
    ('The consent covers read-only reads of exact Git objects in this '
     'repository, at the one fixed Git revision a conformance fixture names, '
     'and only of this closed population of at most six tracked files, all '
     'under `.syzygy/governance/doctrine/`: - phase A: `README.md`; and - '
     'phase B: those of `architecture.md`, `security.md`, '
     '`trust-and-evidence.md`, `v1.md` and `vision.md` that `README.md` links '
     'to at that revision. No other file is read, even if the index links to '
     'it, and no further index is followed. The reads are selected by '
     'observer `polaris-syzygy-self-project-shape` version '
     '`1.0.0-candidate.1` in the second adapter-registry entry for this pair, '
     'and screened by the self-observation scope of the secret-classification '
     'policy at version `1.2.0-candidate.1`. This consent covers those two '
     'versions only. A later version of either, or any wider population, '
     'needs a new consent act; a superseding registry entry or policy never '
     'widens this one. Everything read is used only inside the conformance '
     'test process. The rendered page and machine answer the test builds are '
     'in-memory values the test inspects; they are never served, cached, '
     'logged, written to disk or written to a walkthrough record. Test '
     'assertions compare only digests, counts, identities and closed reasons. '
     'No assertion message, snapshot, reporter output or test log carries an '
     'observed body or rendered text. The scope excludes: - any repository '
     'other than this one, including the Butlers repository, whose consent is '
     'a separate record this one neither widens nor narrows; - the working '
     'tree, untracked or ignored files, and any revision other than the one '
     'the fixture names; - data stores, credential stores, secret APIs and '
     'the process environment; - credential files and arbitrary '
     'implementation-file bodies; - executing any code in this repository as '
     'part of the observation, and network egress; - any write to this '
     'repository; and - any route, cache, log line, stored evaluation or '
     'walkthrough record, including test-runner output, snapshots and CI '
     'logs. The grant has no silent expiry. The owner may narrow or revoke it '
     'through a later recorded act; revocation does not erase prior '
     'observation records.'))
REGISTRY_HEAD = {
    'schemaVersion':
        1,
    'registryVersion':
        '1.0.0-candidate.1',
    'status':
        'candidate-no-effect-until-owner-act',
    'governanceHome':
        '.syzygy/governance/declarations/adapter-registry',
    'project':
        'project:syzygy',
}
REGISTRY_ENTRY_KEYS = (
    ('observerId',
     'observerVersion',
     'discoveryVersion',
     'purpose',
     'role',
     'contractId',
     'contractVersion',
     'contractVersionSource',
     'governingBehaviorContract',
     'subject',
     'authorizationModes',
     'authorizationModeDerivation',
     'provenanceDisclosure',
     'implementation',
     'implementationStatus',
     'surfaceExposure',
     'inputClasses',
     'outputFactClasses',
     'determinismClass',
     'determinism',
     'typedAuthority',
     'observationGrammar',
     'resourceLimits',
     'resourceLimitSemantics',
     'parsePassIdentities',
     'admissionFailureMapping',
     'failureStates',
     'claimStateMapping',
     'selfReferenceRule',
     'adoptionStatus'))
INPUT_CLASSES = (
    ('git-revision', 'git-object-id'),
    ('repository-locator-mapping',
     'opaque-repository-id-plus-normalized-approved-locator'),
    ('git-object-database', 'repository-id-plus-resolved-git-common-dir'),
    ('governing-behavior-contract', 'contract-id-plus-sha256-content-digest'),
    ('git-tree-entry',
     'repository-id-plus-revision-plus-repository-relative-path-plus-'
     'object-id'),
    ('git-blob', 'repository-id-plus-blob-object-id'),
    ('project-shape-source-manifest', 'sha256-content-digest'),
    ('observation-consent', 'record-id-plus-provenance-state'),
    ('secret-classification-policy',
     'policy-id-plus-version-plus-content-digest-plus-provenance-state'),
    ('observer-registry-entry',
     'observer-id-plus-version-plus-content-digest-plus-provenance-state'),
    ('resource-limits', 'canonical-json-sha256'),
)
REGISTRY_PINNED = {
    'purpose':
        ('test-only conformance fixture (M8 slice 6): measures the '
         "project-shape pipeline against this repository's own tracked tree "
         'at one fixed Git revision; serves no surface'),
    'authorizationModes':
        ['independently-verified', 'owner-trusted-bootstrap'],
    'provenanceDisclosure':
        ('Observation uses owner-trusted records; independent audit is not '
         'configured.'),
    'implementation':
        ('none yet; a conformance module under '
         'packages/three-surface-poc-core/src/ would be added by M8 slice 6 '
         'only after all three self-observation acts exist; this entry names '
         'no implementation identity or version until that slice does, and '
         'the self discovery has its own discoveryVersion because it differs '
         'from the Butlers discovery in seed, population and roster'),
    'implementationStatus':
        ('no implementation reads this entry; adopting it authorizes no code '
         'change by itself'),
    'typedAuthority':
        {'authorityType': 'version-control',
         'questions': ['What currently exists?'],
         'readAuthority': "within this repository's own Git object database "
                          'at the one fixed revision the conformance fixture '
                          'names, phase A reads only the root index this '
                          "profile's sourcePopulation names and Git tree "
                          'metadata needed to derive the manifest; phase B '
                          'reads only those sourcePopulation phase-B paths '
                          'the root index links to, addressed as exact Git '
                          'objects in that revision-bound manifest; no '
                          'further index is followed',
         'writeSurface': [],
         'databaseAccess': [],
         'networkAccess': [],
         'executeObservedCode': False,
         'workingTreeRead': False},
    'surfaceExposure':
        {'servedRoutes': [],
         'cache': False,
         'log': False,
         'storedEvaluation': False,
         'walkthroughRecord': False,
         'rule': 'the page and machine answer are built only as in-memory '
                 'values inside the conformance test process and are never '
                 'served, cached, logged or written anywhere; test assertions '
                 'compare only digests, counts, identities and closed '
                 'reasons, and no assertion message, snapshot, reporter '
                 'output or test log carries an observed body or rendered '
                 'text'},
    'inputClasses': [{"class": name, "identityScheme": scheme}
                     for name, scheme in INPUT_CLASSES],
    'resourceLimits':
        {'maxSources': 512,
         'maxBytesPerSource': 1048576,
         'maxTotalBytes': 16777216,
         'maxIndexDepth': 4,
         'maxParsePassesPerSource': 16,
         'maxHumanResponseBytes': 2097152,
         'maxMachineResponseBytes': 8388608},
    'selfReferenceRule':
        ('no object read as an observed Git blob under this entry, including '
         'any policy, registry entry, consent record, act record, manifest, '
         'owner packet or the acceptance-act record, is an authority input to '
         'any evaluation; authority for this pair is evaluated only for the '
         'pair (project:syzygy, repository:syzygy) and is never inherited '
         'from another pair, including through expectations keyed only by the '
         'observing project'),
    'adoptionStatus':
        'candidate-unadopted',
}
SELF_SCOPE = {
    'purpose':
        ('test-only conformance fixture (M8 slice 6): the project-shape '
         "pipeline measured against this repository's own tracked tree at one "
         'fixed Git revision; nothing observed under this scope is served'),
    'observingProject': OBSERVING,
    'observedRepository': OBSERVED,
    'contentClass': CONTENT_CLASS,
    'authorizationModes':
        ['independently-verified', 'owner-trusted-bootstrap'],
    'ingestBoundaries': list(SELF_BOUNDARIES),
    'ingestBoundaryRule':
        ('human-html and machine-json exist only as in-memory values inside '
         'the conformance test process; nothing under this scope is served, '
         'cached, logged, stored as an evaluation, written to a walkthrough '
         'record or written to disk; test assertions compare only digests, '
         'counts, identities and closed reasons, and no assertion message, '
         'snapshot, reporter output or test log carries an observed body or '
         'rendered text'),
    'phaseASeedPaths': list(SELF_PHASE_A),
    'phaseBPaths': list(SELF_PHASE_B),
    'derivedSeedRule':
        ('after the seed is admitted, phase B reads only those phaseBPaths '
         'entries the seed links to at the fixed revision; no further index '
         'is followed, no path outside phaseBPaths is read even if the seed '
         'links to it, nothing is derived from directory basenames, and a '
         'basename shared with the Butlers grammar confers no extraction '
         'class'),
    'inheritedRules':
        ('every other rule in this policy applies to this scope unchanged: '
         'the access boundary, phase-B manifest rule, Git-objects-only '
         'admission, encodings, denied paths, every detector, active-content '
         'classification, match action, unclassifiable exclusion, redaction '
         'classes, classification order, classification success and raw-body '
         'handling. Where one of those rules names the signed PWB grammar, '
         'the signed PWB source grammar or the signed PWB closed set, it '
         "reads under this scope as follows: the PWB grammar's extraction "
         'classes and fixed literals apply unchanged; a phase-B manifest '
         'validates only when every entry is a phaseBPaths member the seed '
         'links to; and a source that matches no signed literal is excluded '
         'as an unknown extraction class, never admitted under a looser or '
         'unsigned grammar. No approved requirement names this pair, so this '
         "reading is this policy's own and binds only through the act that "
         'approves it'),
    'selfReferenceRule':
        ('no object read as an observed Git blob under this scope, including '
         'any policy, registry entry, consent record, act record, manifest, '
         'owner packet or the acceptance-act record, is an authority input to '
         'any evaluation; authority inputs are read only through the '
         'governance-inputs path, exactly as for the base scope; authority '
         'for this pair is evaluated only for the pair (project:syzygy, '
         'repository:syzygy) and is never inherited from another pair, '
         'including through expectations keyed only by the observing project'),
}

#: Every finder check() calls; the selftest proves each call site survives.
CHECK_FINDERS = ("population_findings", "consent_findings",
                 "registry_findings", "policy_findings", "target_findings",
                 "composition_findings", "manifest_findings",
                 "packet_findings")
ROW = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)
HEX64 = re.compile(r"[0-9a-f]{64}")
PATCH_TARGET = re.compile(r"^\+\+\+ b/(\S+)", re.MULTILINE)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_bytes(rel: pathlib.Path, root: pathlib.Path = ROOT) -> bytes:
    target = root / rel
    if not target.is_file():
        raise ValueError(f"missing: {rel.as_posix()}")
    return target.read_bytes()


def spec_digest(root: pathlib.Path = ROOT) -> str:
    return sha256(read_bytes(SPEC, root))


def one_line(text: str) -> str:
    """Whitespace-normalized text, so a hard wrap never hides a sentence."""
    return " ".join(text.split())


# ------------------------------------------------------------- policy


def policy_proposed(current: bytes | None = None,
                    patch: pathlib.Path | None = None,
                    reverse: bool = False) -> bytes:
    """The policy's bytes with the one proposed diff applied (or reversed)."""
    body = read_bytes(POLICY) if current is None else current
    patch = ROOT / PROPOSED / POLICY_PATCH_NAME if patch is None else patch
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
        (base / POLICY).parent.mkdir(parents=True, exist_ok=True)
        (base / POLICY).write_bytes(body)
        done = subprocess.run(
            ["git", "apply", "--whitespace=nowarn"]
            + (["-R"] if reverse else []) + [str(patch)],
            cwd=base, capture_output=True, text=True)
        if done.returncode != 0:
            raise ValueError(
                f"{patch.name} does not {'reverse' if reverse else 'apply'} "
                f"on the current bytes of {POLICY.as_posix()}: "
                f"{done.stderr.strip()}")
        return (base / POLICY).read_bytes()


def policy_state(root: pathlib.Path = ROOT) -> tuple[str, bytes, bytes]:
    """(state, base bytes, proposed bytes) for act 3 in the tree at `root`.

    Before act 3 the patch applies forward to the policy: the act is pending
    and the current bytes are the base. After act 3 the policy already holds
    the proposed bytes, so the patch reverses cleanly and the reversal is
    the base. Anything else is drift, and neither state is claimed.
    """
    current = read_bytes(POLICY, root)
    patch = root / PROPOSED / POLICY_PATCH_NAME
    try:
        return "pending", current, policy_proposed(current, patch)
    except ValueError as forward:
        try:
            base = policy_proposed(current, patch, reverse=True)
        except ValueError:
            raise forward from None
        return "installed", base, current


def policy_findings(proposed: bytes, current: bytes,
                    root: pathlib.Path = ROOT) -> list[str]:
    """The extension adds one scope and changes nothing the base scope uses."""
    if proposed == current:
        return [f"the policy patch changes nothing: {POLICY.as_posix()}"]
    try:
        new, old = json.loads(proposed), json.loads(current)
    except ValueError as error:
        return [f"policy bytes are not valid JSON: {error}"]
    findings: list[str] = []
    if new.get("policyVersion") != POLICY_PROPOSED_VERSION:
        findings.append(f"policyVersion is not {POLICY_PROPOSED_VERSION}: "
                        f"{new.get('policyVersion')!r}")
    # Everything except the version and the one new key must be unchanged.
    for key in sorted(set(old) | set(new)):
        if key in ("policyVersion", "selfObservationScope"):
            continue
        if old.get(key) != new.get(key):
            findings.append(f"the extension changes the base policy's {key!r}")
    scope = new.get("selfObservationScope")
    if scope != SELF_SCOPE:
        findings.append("selfObservationScope is not exactly the pinned "
                        "scope: pair, content class, modes, boundaries, "
                        "population and every rule sentence")
    # The pinned seed must also exist in the tree being checked.
    seeds = scope.get("phaseASeedPaths") if isinstance(scope, dict) else None
    for seed in seeds if isinstance(seeds, list) else []:
        if not isinstance(seed, str) or not (root / seed).is_file():
            findings.append(f"phase-A seed is not a file in this "
                            f"repository: {seed!r}")
    return findings


# ------------------------------------------------------------ registry


def registry_findings(body: bytes, spec: str,
                      root: pathlib.Path = ROOT) -> list[str]:
    try:
        doc = json.loads(body)
    except ValueError as error:
        return [f"registry entry is not valid JSON: {error}"]
    entries = doc.get("entries")
    if not isinstance(entries, list) or len(entries) != 1:
        return ["registry file does not carry exactly one entry"]
    entry = entries[0]
    findings: list[str] = []
    if {k: v for k, v in doc.items() if k != "entries"} != REGISTRY_HEAD:
        findings.append("registry file head is not exactly the pinned head")
    if not isinstance(entry, dict) or tuple(entry) != REGISTRY_ENTRY_KEYS:
        return findings + ["registry entry keys are not exactly the pinned "
                           "key set, in order"]
    try:
        butlers = json.loads(read_bytes(BUTLERS_REGISTRY, root))["entries"][0]
        for key in ("observerId", "discoveryVersion"):
            if entry.get(key) == butlers.get(key):
                findings.append(f"{key} collides with the Butlers entry")
    except (ValueError, KeyError, IndexError) as error:
        findings.append(f"cannot read the Butlers entry to compare: {error}")
    if entry.get("observerVersion") != SELF_OBSERVER_VERSION:
        findings.append(f"observerVersion is not {SELF_OBSERVER_VERSION}, the "
                        "version the consent pins")
    subject = entry.get("subject") or {}
    if (subject.get("observingProject"), subject.get("observedRepository")) != (
            OBSERVING, OBSERVED):
        findings.append("registry subject names a different pair")
    contract = entry.get("governingBehaviorContract") or {}
    if contract.get("version") != f"sha256:{spec}":
        findings.append("governingBehaviorContract.version is not the current "
                        "PWB specification digest; regenerate after the PWB "
                        "specification act that moved it")
    for key, value in REGISTRY_PINNED.items():
        if entry.get(key) != value:
            findings.append(f"registry {key} is not exactly the pinned value")
    population = (entry.get("observationGrammar") or {}).get(
        "sourcePopulation") or {}
    if (population.get("phaseA"), population.get("phaseB")) != (
            list(SELF_PHASE_A), list(SELF_PHASE_B)):
        findings.append("observationGrammar.sourcePopulation is not the closed "
                        "population the consent names")
    semantics = entry.get("resourceLimitSemantics")
    for key in REGISTRY_PINNED["resourceLimits"]:
        if not isinstance(semantics, dict) or key not in semantics:
            findings.append(f"resource limit without a semantics "
                            f"sentence: {key}")
    return findings


# ------------------------------------------------------------- consent


def consent_findings(text: str) -> list[str]:
    findings: list[str] = []
    # No agent may draft words into the owner's mouth: the Butlers record
    # quotes a statement the owner actually made, and no such statement
    # exists for this pair.
    if re.search(r"^>\s*[“\"]", text, re.MULTILINE):
        findings.append("consent carries a quoted owner statement; none has "
                        "been given for this pair")
    if BUTLERS_OBSERVED in text.split("## Scope", 1)[0]:
        findings.append("consent head names the Butlers repository")
    # The head and the scope are the grant: pair, class, purpose, locator,
    # status, revocation, closed population, pinned versions, where results
    # may go and every exclusion. A later version of the other two artifacts
    # can never widen them.
    if one_line(text.split("## Where the grant comes from", 1)[0]) != (
            CONSENT_HEAD):
        findings.append("consent head is not exactly the pinned head")
    if one_line(text.split("## Scope", 1)[-1].split(
            "## Provenance state and effect", 1)[0]) != CONSENT_SCOPE:
        findings.append("consent ## Scope section is not exactly the pinned "
                        "scope")
    return findings


# ------------------------------------------------------ package-level


def population_findings(names: list[str]) -> list[str]:
    if sorted(names) != PROPOSED_POPULATION:
        return ["proposed/ population is not the three declared files: "
                + ", ".join(sorted(names))]
    return []


def target_state(key: str, root: pathlib.Path = ROOT) -> str:
    """'pending' or 'installed' for a new-file act; ValueError when occupied."""
    target = root / ACTS[key][1]
    if not target.exists():
        return "pending"
    source = root / PROPOSED / (CONSENT_NAME if key == "consent"
                                else REGISTRY_NAME)
    if target.is_file() and source.is_file() and (
            target.read_bytes() == source.read_bytes()):
        return "installed"
    raise ValueError(f"install target occupied by different bytes: "
                     f"{ACTS[key][1].as_posix()}")


def target_findings(root: pathlib.Path = ROOT) -> list[str]:
    """A new file's install target is free (pending) or holds exactly the
    proposed bytes (installed); anything else would be overwritten."""
    findings = []
    for key in ("consent", "registry"):
        try:
            target_state(key, root)
        except ValueError as error:
            findings.append(str(error))
    return findings


def composition_findings(root: pathlib.Path = ROOT) -> list[str]:
    """No sibling candidate package may patch or draft any of the targets."""
    targets = {ACTS[k][1].as_posix() for k in ACTS}
    names = {ACTS[k][1].name for k in ACTS}
    findings = []
    for drafted in sorted((root / CANDIDATES).glob("*/proposed/**/*")):
        if not drafted.is_file() or (
                drafted.relative_to(root / CANDIDATES).parts[0]
                == PACKAGE.name):
            continue
        rel = drafted.relative_to(root).as_posix()
        if drafted.name in names:
            findings.append(f"{rel} also drafts a file named {drafted.name}")
        if drafted.suffix == ".patch":
            for hit in PATCH_TARGET.findall(
                    drafted.read_text(errors="replace")):
                if hit in targets:
                    findings.append(f"{rel} also patches {hit}")
    return findings


def artifacts(root: pathlib.Path = ROOT) -> dict[str, bytes]:
    return {
        "consent": read_bytes(PROPOSED / CONSENT_NAME, root),
        "registry": read_bytes(PROPOSED / REGISTRY_NAME, root),
        "policy": policy_state(root)[2],
    }


def adoption_states(root: pathlib.Path = ROOT) -> dict[str, str]:
    return {"consent": target_state("consent", root),
            "registry": target_state("registry", root),
            "policy": policy_state(root)[0]}


def render(key: str, body: bytes) -> str:
    label, target, _manifest, title = ACTS[key]
    how = ("the drafted file under proposed/, installed byte-for-byte at "
           "adoption" if key != "policy" else
           "the subject's current bytes with proposed/*.patch applied; the "
           "current bytes stay the argument of the act in force")
    lines = [
        f"# {title}",
        f"# This row binds only by the owner act `{label}` that takes its",
        "# digest as argument; until that act is performed it binds nothing.",
        f"# 1 artifact; the row hashes {how}.",
        "# It matches the tree only after --apply at adoption.",
        f"{sha256(body)}  {target.as_posix()}",
    ]
    return "\n".join(lines) + "\n"


def manifest_findings(key: str, text: str | None, expected: str) -> list[str]:
    rel = ACTS[key][2].as_posix()
    if text is None:
        return [f"manifest missing: {rel}"]
    rows = ROW.findall(text)
    if [path for _d, path in rows] != [ACTS[key][1].as_posix()]:
        return [f"{rel}: row population or path differs"]
    if text != expected:
        return [f"{rel}: differs from exact regeneration"]
    return []


def packet_findings(text: str | None, digests: dict[str, str]) -> list[str]:
    """The packet quotes both new-file arguments and offers no policy one."""
    if text is None:
        return [f"owner packet missing: {PACKET.as_posix()}"]
    findings = []
    for key in ("consent", "registry"):
        label = ACTS[key][0]
        quoted = re.findall(re.escape(label) + r":\s*`?([0-9a-f]{64})", text)
        if not quoted:
            findings.append(f"packet does not quote the {key} argument")
        elif set(quoted) != {digests[key]}:
            findings.append(f"packet quotes a stale {key} argument")
    if re.search(re.escape(ACTS["policy"][0]) + r":\s*`?[0-9a-f]{64}", text):
        findings.append("packet offers a policy argument before the "
                        "superseding act is prepared")
    return findings


def check(root: pathlib.Path = ROOT) -> list[str]:
    """Every predicate over the tree at `root`, before, between or after the
    three adoptions, in any order."""
    findings: list[str] = []
    findings.extend(population_findings(
        [p.name for p in (root / PROPOSED).iterdir()]
        if (root / PROPOSED).is_dir() else []))
    try:
        _state, base, proposed = policy_state(root)
        bodies = artifacts(root)
    except ValueError as error:
        return findings + [str(error)]
    findings.extend(consent_findings(bodies["consent"].decode("utf-8")))
    findings.extend(registry_findings(bodies["registry"], spec_digest(root),
                                      root))
    findings.extend(policy_findings(proposed, base, root))
    findings.extend(target_findings(root))
    findings.extend(composition_findings(root))
    for key, body in bodies.items():
        target = root / ACTS[key][2]
        findings.extend(manifest_findings(
            key, target.read_text() if target.is_file() else None,
            render(key, body)))
    packet = root / PACKET
    findings.extend(packet_findings(
        packet.read_text() if packet.is_file() else None,
        {k: sha256(v) for k, v in bodies.items()}))
    return findings


# ------------------------------------------------------------ selftest


#: What `check()` needs to run in a scratch root: the package, the three
#: install targets' neighbours, the specification and the seed population.
SCRATCH_COPIES = (PACKAGE, POLICY, BUTLERS_REGISTRY, SPEC,
                  pathlib.Path(".syzygy/governance/doctrine"))


def scratch_root(into: pathlib.Path) -> pathlib.Path:
    for rel in SCRATCH_COPIES:
        source, target = ROOT / rel, into / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.is_dir():
            shutil.copytree(source, target)
        else:
            shutil.copyfile(source, target)
    return into


def quietly(fn, *args):
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*args)


def selftest() -> int:
    findings = check()
    if findings:
        print("SELFTEST FAILED: the package does not verify on current bytes")
        for finding in findings:
            print(f"  {finding}")
        return 1
    bodies = artifacts()
    consent = bodies["consent"].decode("utf-8")
    registry = bodies["registry"]
    _state, current, proposed = policy_state()
    spec = spec_digest()
    count = 0

    def expect(label: str, got: list[str]) -> bool:
        nonlocal count
        count += 1
        if not got:
            print(f"SELFTEST FAILED: {label} passed")
            return False
        return True

    def csub(phrase: str, replacement: str) -> str:
        """Replace one phrase of the consent across any hard wrap."""
        pattern = r"\s+".join(re.escape(word) for word in phrase.split())
        return re.sub(pattern, replacement, consent, count=1)

    # Consent predicates.
    consent_mutants = (
        ("a consent naming another repository",
         consent.replace(f"({OBSERVING}, {OBSERVED})",
                         f"({OBSERVING}, {BUTLERS_OBSERVED})", 1)),
        ("a consent naming another content class",
         consent.replace(f"`{CONTENT_CLASS}`", "`declared-project-text`", 1)),
        ("a drafted owner quotation",
         consent.replace("## Scope", "> “you have consent”\n\n## Scope", 1)),
        ("a consent with no candidate Status line",
         consent.replace("Status: **candidate;", "Status: **in force;", 1)),
        ("a consent with two Status lines",
         consent.replace("Consent class:", "Status: candidate\n\nConsent "
                         "class:", 1)),
        ("a consent head naming the Butlers repository",
         csub("has been given for this pair.",
              f"has been given for this pair or {BUTLERS_OBSERVED}.")),
        ("a consent with an unpinned observer",
         csub(f"version `{SELF_OBSERVER_VERSION}`", "")),
        ("a consent with an unpinned policy version",
         csub(f"at version `{POLICY_PROPOSED_VERSION}`", "at any version")),
        ("a consent a later version may widen",
         csub("needs a new consent act", "is covered")),
        ("a consent with no assertion bound",
         csub("reporter output or test log", "reporter output")),
        ("a consent missing one population member",
         consent.replace("`trust-and-evidence.md`", "`trust.md`", 1)),
        ("a consent granting another path",
         consent.replace("no further index is followed.",
                         "no further index is followed. Phase A also: "
                         "`AGENTS.md` and every file under `apps/`.", 1)),
        ("a consent population that is not closed",
         csub("closed population of at most six tracked files",
              "population of tracked files")),
        ("a consent that follows links",
         csub("No other file is read, even if the index links to it, and no "
              "further index is followed.",
              "Any file the index links to is read.")),
        ("a consent that also reads the working tree",
         csub("reads of exact Git objects in this repository",
              "reads of exact Git objects in this repository and the "
              "working tree")),
        # Round-3 widening mutants: each lies outside the grant paragraph.
        ("a consent that drops the working-tree exclusion",
         csub("- the working tree, untracked or ignored files, and any "
              "revision other than the one the fixture names;", "")),
        ("a consent granting apps/ after the version pins",
         csub("never widens this one.", "never widens this one. The consent "
              "also covers every tracked file under `apps/`.")),
        ("a consent whose results may be served",
         csub("they are never served, cached, logged, written to disk or "
              "written to a walkthrough record.", "they may be served and "
              "cached.")),
        ("a production consent", csub("Purpose: test-only.",
                                      "Purpose: production.")),
        ("a consent that drops the execution and egress exclusion",
         csub("- executing any code in this repository as part of the "
              "observation, and network egress;", "")),
        ("a consent locator widened to remote clones",
         csub("the root of the Syzygy checkout that runs the conformance test",
              "any remote clone of it fetched at test time")),
        ("a consent that no longer excludes Butlers",
         csub("any repository other than this one, including the Butlers "
              "repository,", "any repository other than this one or the "
              "Butlers repository,")),
        ("a consent that permits writes",
         csub("- any write to this repository; and", "- and")),
        ("an irrevocable consent",
         csub("active; supersedes no earlier consent",
              "irrevocable; supersedes the Butlers consent")),
    )
    for label, mutant in consent_mutants:
        assert mutant != consent, label
        if not expect(label, consent_findings(mutant)):
            return 1

    # Registry predicates, mutated through the parsed document.
    def reg(fn) -> bytes:
        doc = json.loads(registry)
        fn(doc["entries"][0])
        return json.dumps(doc, indent=2).encode()

    def reg_doc(fn) -> bytes:
        doc = json.loads(registry)
        fn(doc)
        return json.dumps(doc, indent=2).encode()

    def butlers(key: str) -> str:
        return json.loads(read_bytes(BUTLERS_REGISTRY))["entries"][0][key]

    registry_mutants = (
        ("invalid registry JSON", registry + b"}"),
        ("a second registry entry",
         reg_doc(lambda d: d["entries"].append(dict(d["entries"][0])))),
        ("a registry for another project",
         reg_doc(lambda d: d.__setitem__("project", "project:butlers"))),
        ("the Butlers observerId",
         reg(lambda e: e.__setitem__("observerId", butlers("observerId")))),
        ("the Butlers discoveryVersion",
         reg(lambda e: e.__setitem__("discoveryVersion",
                                     butlers("discoveryVersion")))),
        ("an observerVersion the consent does not pin",
         reg(lambda e: e.__setitem__("observerVersion", "1.1.0-candidate.1"))),
        ("a named implementationId",
         reg(lambda e: e.__setitem__("implementationId", "x/y"))),
        ("a named implementationVersion",
         reg(lambda e: e.__setitem__("implementationVersion", "1.0.0"))),
        ("a registry subject naming the Butlers repository",
         reg(lambda e: e["subject"].__setitem__("observedRepository",
                                                BUTLERS_OBSERVED))),
        ("a stale PWB specification digest",
         reg(lambda e: e["governingBehaviorContract"].__setitem__(
             "version", "sha256:" + "0" * 64))),
        ("a non-empty write surface",
         reg(lambda e: e["typedAuthority"].__setitem__("writeSurface",
                                                       ["docs/"]))),
        ("database access",
         reg(lambda e: e["typedAuthority"].__setitem__("databaseAccess",
                                                       ["sqlite"]))),
        ("network access",
         reg(lambda e: e["typedAuthority"].__setitem__("networkAccess",
                                                       ["https"]))),
        ("observed-code execution",
         reg(lambda e: e["typedAuthority"].__setitem__("executeObservedCode",
                                                       True))),
        ("a working-tree read",
         reg(lambda e: e["typedAuthority"].__setitem__("workingTreeRead",
                                                       True))),
        ("a served route",
         reg(lambda e: e["surfaceExposure"].__setitem__("servedRoutes",
                                                        ["/polaris"]))),
        ("a cached self-observation",
         reg(lambda e: e["surfaceExposure"].__setitem__("cache", True))),
        ("a logged self-observation",
         reg(lambda e: e["surfaceExposure"].__setitem__("log", True))),
        ("a stored evaluation",
         reg(lambda e: e["surfaceExposure"].__setitem__("storedEvaluation",
                                                        True))),
        ("a walkthrough record",
         reg(lambda e: e["surfaceExposure"].__setitem__("walkthroughRecord",
                                                        True))),
        ("an exposure rule with no assertion bound",
         reg(lambda e: e["surfaceExposure"].__setitem__("rule", "never served"))),
        ("a widened source population",
         reg(lambda e: e["observationGrammar"]["sourcePopulation"]["phaseB"]
             .append("AGENTS.md"))),
        ("a missing source population",
         reg(lambda e: e["observationGrammar"].pop("sourcePopulation"))),
        ("an inheritable self-reference rule",
         reg(lambda e: e.__setitem__("selfReferenceRule", "observed text"))),
        ("resource limits that are not an object",
         reg(lambda e: e.__setitem__("resourceLimits", []))),
        ("a resource limit without semantics",
         reg(lambda e: e["resourceLimits"].__setitem__("maxExtra", 1))),
        ("a resource limit whose semantics sentence is gone",
         reg(lambda e: e["resourceLimitSemantics"].pop("maxSources"))),
        ("an adopted-looking registry head",
         reg_doc(lambda d: d.__setitem__("status", "adopted"))),
        ("an extra registry entry key",
         reg(lambda e: e.__setitem__("httpFetch", True))),
        # Round-3 widening mutants.
        ("a read authority over any repository and the working tree",
         reg(lambda e: e["typedAuthority"].__setitem__(
             "readAuthority", "any repository and the working tree"))),
        ("a production registry purpose",
         reg(lambda e: e.__setitem__("purpose",
                                     "production; serves /polaris"))),
        ("an agent-asserted registry authorization mode",
         reg(lambda e: e["authorizationModes"].append("agent-asserted"))),
        ("a gutted registry self-reference rule",
         reg(lambda e: e.__setitem__(
             "selfReferenceRule",
             "authority is never inherited from another pair"))),
        ("a thousandfold maxSources",
         reg(lambda e: e["resourceLimits"].__setitem__("maxSources", 512000))),
        ("an adopted registry entry",
         reg(lambda e: e.__setitem__("adoptionStatus", "adopted"))),
        ("an implementation naming a file",
         reg(lambda e: e.__setitem__(
             "implementation",
             "packages/three-surface-poc-core/src/self.ts"))),
        ("an http-fetch input class",
         reg(lambda e: e["inputClasses"].append(
             {"class": "http-fetch", "identityScheme": "url"}))),
        ("a disk-writing exposure",
         reg(lambda e: e["surfaceExposure"].__setitem__("diskWrite", True))),
        ("a process-environment read",
         reg(lambda e: e["typedAuthority"].__setitem__(
             "processEnvironmentRead", True))),
        ("no provenance disclosure",
         reg(lambda e: e.__setitem__("provenanceDisclosure", ""))),
    )
    for label, mutant in registry_mutants:
        assert mutant != registry, label
        if not expect(label, registry_findings(mutant, spec)):
            return 1

    # Policy predicates.
    drifted = current.replace(b'"policyVersion": "1.1.0-candidate.1"',
                              b'"policyVersion": "1.1.0-candidate.2"', 1)
    assert drifted != current
    count += 1
    try:
        policy_proposed(drifted)
    except ValueError:
        pass
    else:
        print("SELFTEST FAILED: the policy patch applied over drifted bytes")
        return 1
    with tempfile.TemporaryDirectory() as scratch:
        broken = pathlib.Path(scratch) / POLICY_PATCH_NAME
        original = (ROOT / PROPOSED / POLICY_PATCH_NAME).read_text()
        # Corrupt one context line, so the patch no longer matches the bytes.
        corrupted = original.replace(
            '"policyId": "polaris-butlers-project-shape-secrets"',
            '"policyId": "polaris-other-secrets"', 1)
        assert corrupted != original
        broken.write_text(corrupted)
        count += 1
        try:
            policy_proposed(patch=broken)
        except ValueError:
            pass
        else:
            print("SELFTEST FAILED: a corrupted policy patch applied")
            return 1
    # Base and proposal both carry the extension, so only the no-op
    # predicate can see it.
    if not expect("a no-op policy patch", policy_findings(proposed, proposed)):
        return 1
    if not expect("invalid policy JSON",
                  policy_findings(proposed + b"}", current)):
        return 1
    with tempfile.TemporaryDirectory() as scratch:
        # The seed list is right; only the file is missing from this tree.
        if not expect("a phase-A seed absent from the tree", policy_findings(
                proposed, current, pathlib.Path(scratch))):
            return 1

    def pol(fn) -> bytes:
        doc = json.loads(proposed)
        fn(doc)
        return json.dumps(doc, indent=2).encode()

    def self_scope(key: str, value) -> bytes:
        return pol(lambda d: d["selfObservationScope"].__setitem__(key, value))

    policy_mutants = (
        ("an unbumped policyVersion",
         pol(lambda d: d.__setitem__("policyVersion", POLICY_CURRENT_VERSION))),
        ("a changed base scope",
         pol(lambda d: d["scope"].__setitem__("observedRepository", OBSERVED))),
        ("a dropped detector",
         pol(lambda d: d["detectors"].pop())),
        ("a missing selfObservationScope",
         pol(lambda d: d.pop("selfObservationScope"))),
        ("a self scope naming the Butlers repository",
         self_scope("observedRepository", BUTLERS_OBSERVED)),
        ("a self scope that caches",
         pol(lambda d: d["selfObservationScope"]["ingestBoundaries"].append(
             "cache"))),
        ("a phase-A seed that is not a file here",
         self_scope("phaseASeedPaths", ["about/README.md"])),
        ("an empty phase-A seed list", self_scope("phaseASeedPaths", [])),
        ("a widened phase-B population",
         self_scope("phaseBPaths", list(SELF_PHASE_B) + ["AGENTS.md"])),
        ("an empty purpose", self_scope("purpose", "")),
        ("an empty ingest boundary rule", self_scope("ingestBoundaryRule", " ")),
        ("an ingest boundary rule with no assertion bound",
         self_scope("ingestBoundaryRule", "nothing is served")),
        ("an empty derived-seed rule", self_scope("derivedSeedRule", "")),
        ("an empty inherited-rules sentence", self_scope("inheritedRules", "")),
        ("inherited rules with no signed-grammar reading",
         self_scope("inheritedRules", "every other rule applies unchanged")),
        ("an empty self-reference rule", self_scope("selfReferenceRule", " ")),
        ("an inheritable self-reference rule",
         self_scope("selfReferenceRule", "this policy is observed text")),
        # Round-3 widening mutants.
        ("a self scope with no detectors", self_scope("detectors", [])),
        ("an agent-asserted self scope mode",
         pol(lambda d: d["selfObservationScope"]["authorizationModes"].append(
             "agent-asserted"))),
        ("a self scope with no ingest boundaries",
         self_scope("ingestBoundaries", [])),
        ("a production self scope",
         self_scope("purpose", "production: rendered and served on /polaris")),
        ("inherited rules without every detector",
         pol(lambda d: d["selfObservationScope"].__setitem__(
             "inheritedRules", d["selfObservationScope"]["inheritedRules"]
             .replace("every detector, ", "")))),
        ("a gutted self-scope self-reference rule",
         self_scope("selfReferenceRule",
                    "authority is never inherited from another pair")),
        ("a derived-seed rule reading every linked file",
         self_scope("derivedSeedRule",
                    "phase B reads every file the seed links to")),
        ("an ingest boundary rule that serves and caches",
         pol(lambda d: d["selfObservationScope"].__setitem__(
             "ingestBoundaryRule", "may be served and cached; no assertion "
             "message, snapshot, reporter output or test log carries an "
             "observed body or rendered text"))),
        ("a self scope with no authorization modes",
         pol(lambda d: d["selfObservationScope"].pop("authorizationModes"))),
    )
    for label, mutant in policy_mutants:
        assert mutant != proposed, label
        if not expect(label, policy_findings(mutant, current)):
            return 1

    # Package-level predicates.
    if not expect("an extra proposed file", population_findings(
            PROPOSED_POPULATION + ["EXTRA.md"])):
        return 1
    with tempfile.TemporaryDirectory() as scratch:
        # A full scratch copy, so the drafted source exists and the finding
        # can only come from the byte comparison.
        root = scratch_root(pathlib.Path(scratch))
        target = root / ACTS["consent"][1]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("already here\n")
        if not expect("an install target occupied by different bytes",
                      target_findings(root)):
            return 1
        target.unlink()
        sibling = root / CANDIDATES / "other-package" / "proposed"
        sibling.mkdir(parents=True)
        (sibling / "x.patch").write_text(
            f"--- a/{POLICY.as_posix()}\n+++ b/{POLICY.as_posix()}\n")
        if not expect("a sibling patching the policy",
                      composition_findings(root)):
            return 1
        (sibling / "x.patch").unlink()
        (sibling / REGISTRY_NAME).write_text("{}\n")
        if not expect("a sibling drafting a whole install target",
                      composition_findings(root)):
            return 1
        (sibling / REGISTRY_NAME).unlink()
        # A real sibling nests a patch one level down; the sweep recurses.
        (sibling / "contract").mkdir()
        (sibling / "contract" / "x.patch").write_text(
            f"--- a/{POLICY.as_posix()}\n+++ b/{POLICY.as_posix()}\n")
        if not expect("a nested sibling patch", composition_findings(root)):
            return 1
    for key, body in bodies.items():
        baseline = render(key, body)
        digest = ROW.findall(baseline)[0][0]
        flipped = "0" * 64 if digest != "0" * 64 else "1" * 64
        if not expect(f"a {key} manifest digest mutation", manifest_findings(
                key, baseline.replace(digest, flipped, 1), baseline)):
            return 1
        if not expect(f"a {key} manifest path mutation", manifest_findings(
                key, baseline.replace(ACTS[key][1].as_posix(), "OTHER", 1),
                baseline)):
            return 1
        if not expect(f"an absent {key} manifest",
                      manifest_findings(key, None, baseline)):
            return 1
    digests = {k: sha256(v) for k, v in bodies.items()}
    packet = (ROOT / PACKET).read_text()
    if not expect("a stale consent argument in the packet", packet_findings(
            packet.replace(digests["consent"], "0" * 64), digests)):
        return 1
    if not expect("a stale registry argument in the packet", packet_findings(
            packet.replace(digests["registry"], "0" * 64), digests)):
        return 1
    if not expect("an offered policy argument", packet_findings(
            packet + f"\n{ACTS['policy'][0]}: {digests['policy']}\n",
            digests)):
        return 1

    # Every finder must still be called by check(): replace each in turn
    # with one that returns a sentinel, and require check() to surface it.
    module = sys.modules[__name__]
    for name in CHECK_FINDERS:
        original = getattr(module, name)
        setattr(module, name, lambda *_a, **_k: ["SENTINEL"])
        try:
            got = [f for f in check() if f == "SENTINEL"]
        finally:
            setattr(module, name, original)
        if not expect(f"check() without its {name} call", got):
            return 1

    # --apply installs nothing over a package that does not verify.
    with tempfile.TemporaryDirectory() as scratch:
        root = scratch_root(pathlib.Path(scratch))
        manifest = root / ACTS["consent"][2]
        manifest.write_text(manifest.read_text().replace(
            digests["consent"], "0" * 64))
        count += 1
        if quietly(apply, "consent", True, root) == 0 or (
                root / ACTS["consent"][1]).exists():
            print("SELFTEST FAILED: --apply installed over a package that "
                  "does not verify")
            return 1

    # --apply without --at-adoption installs nothing, even over a package
    # that verifies.
    with tempfile.TemporaryDirectory() as scratch:
        root = scratch_root(pathlib.Path(scratch))
        count += 1
        if quietly(apply, "consent", False, root) == 0 or (
                root / ACTS["consent"][1]).exists():
            print("SELFTEST FAILED: --apply installed without --at-adoption")
            return 1

    # Three separate acts, in every order: after each adoption the package
    # still verifies, the installed act refuses a second --apply, and the
    # manifests keep matching.
    for order in itertools.permutations(ACTS):
        with tempfile.TemporaryDirectory() as scratch:
            root = scratch_root(pathlib.Path(scratch))
            done: list[str] = []
            for key in order:
                count += 1
                if quietly(apply, key, True, root) != 0:
                    print(f"SELFTEST FAILED: --apply {key} refused after "
                          f"{done or 'no act'}")
                    return 1
                done.append(key)
                findings = check(root)
                states = {} if findings else adoption_states(root)
                if findings or any(states.get(k) != ("installed" if k in done
                                                 else "pending")
                                   for k in ACTS):
                    print(f"SELFTEST FAILED: after {done}, states {states}, "
                          f"findings {findings}")
                    return 1
                count += 1
                if quietly(apply, key, True, root) == 0:
                    print(f"SELFTEST FAILED: a second --apply {key} after "
                          f"{done} succeeded")
                    return 1
    print(f"selftest: {count} predicates — consent drafted owner "
          "quotation, Butlers named before the scope, pinned head and pinned "
          "scope, with every round-1 to round-3 widening mutant; registry "
          "JSON, entry count, pinned head, closed key set, observerId and "
          "discoveryVersion collision, observer version, pair, "
          "specification digest, eleven pinned values, source population and "
          "limit semantics; policy drift, corruption, no-op, version, base "
          "scope, pinned self scope and a seed absent from the tree; "
          "proposed population, occupied install target, sibling patch, "
          "nested sibling patch and sibling draft, --apply without "
          "--at-adoption and over a package that does not verify, three "
          "manifests' digest, path and absence, the packet's two quoted "
          "arguments and absent policy offer, and every check() call site "
          "all fail closed; and all six adoption orders verify after each "
          "act and refuse a repeated act")
    return 0


# --------------------------------------------------------------- apply


def apply(key: str, at_adoption: bool, root: pathlib.Path = ROOT) -> int:
    if not at_adoption:
        print("refusing: --apply installs act-bound bytes; it is the adoption "
              "step and belongs in the change that records that act. Pass "
              "--at-adoption.")
        return 2
    findings = check(root)
    if findings:
        print("refusing to apply: the package does not verify")
        for finding in findings:
            print(f"  {finding}")
        return 1
    if adoption_states(root)[key] == "installed":
        print(f"refusing to apply: {ACTS[key][1].as_posix()} already holds "
              "the proposed bytes")
        return 1
    target = root / ACTS[key][1]
    if key == "policy":
        target.write_bytes(policy_state(root)[2])
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / PROPOSED / (CONSENT_NAME if key == "consent"
                                           else REGISTRY_NAME), target)
    print(f"applied {ACTS[key][1].as_posix()}")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--apply", choices=sorted(ACTS))
    parser.add_argument("--at-adoption", action="store_true")
    parser.add_argument("--diff", action="store_true",
                        help="print the proposed policy diff and exit")
    parser.add_argument("--write", action="store_true",
                        help="regenerate the three manifests (retires any "
                             "packet quoting them)")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if args.diff:
        sys.stdout.write((ROOT / PROPOSED / POLICY_PATCH_NAME).read_text())
        return 0
    if args.apply:
        return apply(args.apply, args.at_adoption)
    if args.check:
        findings = check()
        if findings:
            print("Syzygy self-observation act packets do not verify:")
            for finding in findings:
                print(f"  {finding}")
            return 1
        bodies = artifacts()
        states = adoption_states()
        print("Syzygy self-observation act packets verify: 3 manifests match "
              "their 3 proposed artifacts (consent, registry entry, policy "
              "extension)")
        for key, body in bodies.items():
            print(f"  {key} ({states[key]}): {sha256(body)}  "
                  f"{ACTS[key][1].as_posix()}")
        return 0
    if not args.write:
        print("refusing: regenerating a manifest changes an act argument; pass "
              "--write, then update every registered copy of the digest")
        return 2
    for key, body in artifacts().items():
        target = ROOT / ACTS[key][2]
        target.write_text(render(key, body))
        print(f"wrote {ACTS[key][2].as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
