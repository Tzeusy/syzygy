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

`--check` verifies each artifact's structural claims, their agreement on
the pair, content class, pinned versions and closed source population, that
each new install target is free (act pending) or holds exactly the proposed
bytes (act installed), that the policy either takes the patch (pending) or
already holds its result (installed), that no sibling candidate package
patches or drafts any of the three targets, that every manifest is an exact
regeneration, and that the owner packet quotes the two new-file arguments
at their current digests and offers no policy argument. It holds before,
between and after the three adoptions, in any order, and `--apply` refuses
an act that is already installed. Bare invocation refuses to overwrite the
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
#: Sentences each artifact must carry, compared whitespace-normalized.
ASSERTION_BOUND = ("assertion message, snapshot, reporter output or test log "
                   "carries an observed body or rendered text")
GRAMMAR_READING = ("a source that matches no signed literal is excluded as an "
                   "unknown extraction class")
NO_INHERITANCE = "is never inherited from another pair"
#: The consent's grant paragraph, from "## Scope" to the version pins,
#: compared whitespace-normalized and whole. It is the SEC-4 grant, so an
#: added path, a dropped closure sentence or a widened read fails.
CONSENT_GRANT = (
    "The consent covers read-only reads of exact Git objects in this "
    "repository, at the one fixed Git revision a conformance fixture names, "
    "and only of this closed population of at most six tracked files, all "
    f"under `{DOCTRINE}`: - phase A: `README.md`; and - phase B: those of "
    "`architecture.md`, `security.md`, `trust-and-evidence.md`, `v1.md` and "
    "`vision.md` that `README.md` links to at that revision. No other file is "
    "read, even if the index links to it, and no further index is followed.")
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
    if not isinstance(scope, dict):
        return findings + ["selfObservationScope is missing or not an object"]
    if (scope.get("observingProject"), scope.get("observedRepository"),
            scope.get("contentClass")) != (OBSERVING, OBSERVED, CONTENT_CLASS):
        findings.append("selfObservationScope names a different pair or "
                        "content class")
    boundaries = scope.get("ingestBoundaries")
    if not isinstance(boundaries, list) or not set(boundaries) <= set(
            SELF_BOUNDARIES):
        findings.append(f"selfObservationScope names an ingest boundary outside "
                        f"{', '.join(SELF_BOUNDARIES)}: {boundaries!r}")
    # An empty or non-list seed list fails the population equality below;
    # this loop adds only that each seed exists in the tree being checked.
    seeds = scope.get("phaseASeedPaths")
    for seed in seeds if isinstance(seeds, list) else []:
        if not isinstance(seed, str) or not (root / seed).is_file():
            findings.append(f"phase-A seed is not a file in this "
                            f"repository: {seed!r}")
    if (seeds, scope.get("phaseBPaths")) != (list(SELF_PHASE_A),
                                             list(SELF_PHASE_B)):
        findings.append("selfObservationScope's phase-A and phase-B paths are "
                        "not the closed population the consent names")
    for key in ("purpose", "ingestBoundaryRule", "derivedSeedRule",
                "inheritedRules", "selfReferenceRule"):
        if not isinstance(scope.get(key), str) or not scope[key].strip():
            findings.append(f"selfObservationScope sentence is empty: {key}")
    for key, phrase in (("ingestBoundaryRule", ASSERTION_BOUND),
                        ("inheritedRules", GRAMMAR_READING),
                        ("selfReferenceRule", NO_INHERITANCE)):
        if phrase not in one_line(str(scope.get(key, ""))):
            findings.append(f"selfObservationScope {key} does not say: "
                            f"{phrase}")
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
    if doc.get("project") != OBSERVING:
        findings.append(f"registry project is not {OBSERVING}")
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
    for key in ("implementationId", "implementationVersion"):
        if key in entry:
            findings.append(f"{key} is named before any slice names an "
                            "implementation")
    subject = entry.get("subject") or {}
    if (subject.get("observingProject"), subject.get("observedRepository")) != (
            OBSERVING, OBSERVED):
        findings.append("registry subject names a different pair")
    contract = entry.get("governingBehaviorContract") or {}
    if contract.get("version") != f"sha256:{spec}":
        findings.append("governingBehaviorContract.version is not the current "
                        "PWB specification digest; regenerate after the PWB "
                        "specification act that moved it")
    authority = entry.get("typedAuthority") or {}
    for key in ("writeSurface", "databaseAccess", "networkAccess"):
        if authority.get(key) != []:
            findings.append(f"typedAuthority.{key} is not empty")
    for key in ("executeObservedCode", "workingTreeRead"):
        if authority.get(key) is not False:
            findings.append(f"typedAuthority.{key} is not false")
    exposure = entry.get("surfaceExposure") or {}
    if exposure.get("servedRoutes") != []:
        findings.append("surfaceExposure.servedRoutes is not empty")
    for key in ("cache", "log", "storedEvaluation", "walkthroughRecord"):
        if exposure.get(key) is not False:
            findings.append(f"surfaceExposure.{key} is not false")
    if ASSERTION_BOUND not in one_line(str(exposure.get("rule", ""))):
        findings.append(f"surfaceExposure.rule does not say: {ASSERTION_BOUND}")
    population = (entry.get("observationGrammar") or {}).get(
        "sourcePopulation") or {}
    if (population.get("phaseA"), population.get("phaseB")) != (
            list(SELF_PHASE_A), list(SELF_PHASE_B)):
        findings.append("observationGrammar.sourcePopulation is not the closed "
                        "population the consent names")
    if NO_INHERITANCE not in one_line(str(entry.get("selfReferenceRule", ""))):
        findings.append(f"selfReferenceRule does not say: {NO_INHERITANCE}")
    limits = entry.get("resourceLimits")
    semantics = entry.get("resourceLimitSemantics")
    if not isinstance(limits, dict) or not isinstance(semantics, dict):
        findings.append("resourceLimits or resourceLimitSemantics is not an "
                        "object")
    else:
        for key in limits:
            if key not in semantics:
                findings.append(f"resource limit without a semantics "
                                f"sentence: {key}")
    return findings


# ------------------------------------------------------------- consent


def consent_findings(text: str) -> list[str]:
    findings: list[str] = []
    if f"Subject: `({OBSERVING}, {OBSERVED})`" not in text:
        findings.append("consent Subject line does not name the pair")
    if f"Observation content class: `{CONTENT_CLASS}`" not in text:
        findings.append("consent does not name the content class")
    status = [line for line in text.splitlines() if line.startswith("Status:")]
    if len(status) != 1 or "candidate" not in status[0]:
        findings.append("consent has no single candidate Status line")
    # No agent may draft words into the owner's mouth: the Butlers record
    # quotes a statement the owner actually made, and no such statement
    # exists for this pair.
    if re.search(r"^>\s*[“\"]", text, re.MULTILINE):
        findings.append("consent carries a quoted owner statement; none has "
                        "been given for this pair")
    if BUTLERS_OBSERVED in text.split("## Scope", 1)[0]:
        findings.append("consent head names the Butlers repository")
    # The scope is closed and pinned, so a later version of the other two
    # artifacts can never widen it.
    flat = one_line(text)
    for phrase in (f"observer `{SELF_OBSERVER_ID}` version "
                   f"`{SELF_OBSERVER_VERSION}`",
                   f"at version `{POLICY_PROPOSED_VERSION}`",
                   "needs a new consent act", ASSERTION_BOUND):
        if phrase not in flat:
            findings.append(f"consent scope does not say: {phrase}")
    grant = one_line(text.split("## Scope", 1)[-1].split(
        "The reads are selected", 1)[0])
    if grant != CONSENT_GRANT:
        findings.append("consent grant is not exactly the closed six-file "
                        "population: " + grant)
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
         consent.replace("Purpose: test-only.",
                         f"Purpose: test-only, like {BUTLERS_OBSERVED}.", 1)),
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
    if not expect("a no-op policy patch", policy_findings(current, current)):
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
        root = pathlib.Path(scratch)
        target = root / ACTS["consent"][1]
        target.parent.mkdir(parents=True)
        target.write_text("already here\n")
        if not expect("an install target occupied by different bytes",
                      target_findings(root)):
            return 1
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
    print(f"selftest: {count} predicates — consent pair, class, drafted owner "
          "quotation, status, head, pinned observer and policy versions, "
          "no-widening sentence, assertion bound and exact closed grant; registry "
          "JSON, entry count, project, observerId and discoveryVersion "
          "collision, pinned observer version, unnamed implementation, pair, "
          "specification digest, write surface, database and network access, "
          "code execution, working-tree read, served route, cache, log, "
          "stored evaluation, walkthrough record, assertion bound, source "
          "population, self-reference rule and limit semantics; policy "
          "drift, corruption, no-op, version, base scope, detectors, self "
          "scope, boundaries, seeds, a seed absent from the tree, phase-B "
          "population and rule sentences; proposed population, occupied "
          "install target, sibling patch, nested sibling patch and sibling "
          "draft, --apply over a package that does not verify, three "
          "manifests' digest, path and absence, the "
          "packet's two quoted arguments and absent policy offer, and every "
          "check() call site all fail closed; and all six adoption orders "
          "verify after each act and refuse a repeated act")
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
