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
the pair and content class, that the new install targets are still free,
that no sibling candidate package patches any of the three targets, that
every manifest is an exact regeneration, and that the owner packet quotes
the two new-file arguments at their current digests and offers no policy
argument. Bare invocation refuses to overwrite the manifests; pass
`--write` to regenerate them.
"""

from __future__ import annotations

import argparse
import hashlib
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


def spec_digest() -> str:
    return sha256(read_bytes(SPEC))


# ------------------------------------------------------------- policy


def policy_proposed(current: bytes | None = None,
                    patch: pathlib.Path | None = None) -> bytes:
    """The policy's current bytes with the one proposed diff applied."""
    body = read_bytes(POLICY) if current is None else current
    patch = ROOT / PROPOSED / POLICY_PATCH_NAME if patch is None else patch
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
        (base / POLICY).parent.mkdir(parents=True, exist_ok=True)
        (base / POLICY).write_bytes(body)
        done = subprocess.run(
            ["git", "apply", "--whitespace=nowarn", str(patch)],
            cwd=base, capture_output=True, text=True)
        if done.returncode != 0:
            raise ValueError(
                f"{patch.name} does not apply to the current bytes of "
                f"{POLICY.as_posix()}: {done.stderr.strip()}")
        return (base / POLICY).read_bytes()


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
    seeds = scope.get("phaseASeedPaths")
    if not isinstance(seeds, list) or not seeds:
        findings.append("selfObservationScope names no phase-A seed")
    else:
        for seed in seeds:
            if not isinstance(seed, str) or not (root / seed).is_file():
                findings.append(f"phase-A seed is not a file in this "
                                f"repository: {seed!r}")
    for key in ("purpose", "ingestBoundaryRule", "derivedSeedRule",
                "inheritedRules", "selfReferenceRule"):
        if not isinstance(scope.get(key), str) or not scope[key].strip():
            findings.append(f"selfObservationScope sentence is empty: {key}")
    return findings


# ------------------------------------------------------------ registry


def registry_findings(body: bytes, spec: str) -> list[str]:
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
        butlers = json.loads(read_bytes(BUTLERS_REGISTRY))["entries"][0]
        if entry.get("observerId") == butlers.get("observerId"):
            findings.append("observerId collides with the Butlers entry")
    except (ValueError, KeyError, IndexError) as error:
        findings.append(f"cannot read the Butlers entry to compare: {error}")
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
    return findings


# ------------------------------------------------------ package-level


def population_findings(names: list[str]) -> list[str]:
    if sorted(names) != PROPOSED_POPULATION:
        return ["proposed/ population is not the three declared files: "
                + ", ".join(sorted(names))]
    return []


def new_target_findings(root: pathlib.Path = ROOT) -> list[str]:
    """A new file's install target must still be free, or adoption overwrites."""
    return [f"install target already exists: {ACTS[k][1].as_posix()}"
            for k in ("consent", "registry") if (root / ACTS[k][1]).exists()]


def composition_findings(root: pathlib.Path = ROOT) -> list[str]:
    """No sibling candidate package may patch any of the three targets."""
    targets = {ACTS[k][1].as_posix() for k in ACTS}
    findings = []
    for patch in sorted((root / CANDIDATES).glob("*/proposed/*.patch")):
        if patch.parent.parent.name == PACKAGE.name:
            continue
        for hit in PATCH_TARGET.findall(patch.read_text()):
            if hit in targets:
                findings.append(
                    f"{patch.relative_to(root).as_posix()} also patches {hit}")
    return findings


def artifacts() -> dict[str, bytes]:
    return {
        "consent": read_bytes(PROPOSED / CONSENT_NAME),
        "registry": read_bytes(PROPOSED / REGISTRY_NAME),
        "policy": policy_proposed(),
    }


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


def check() -> list[str]:
    findings: list[str] = []
    findings.extend(population_findings(
        [p.name for p in (ROOT / PROPOSED).iterdir()]
        if (ROOT / PROPOSED).is_dir() else []))
    try:
        bodies = artifacts()
    except ValueError as error:
        return findings + [str(error)]
    findings.extend(consent_findings(bodies["consent"].decode("utf-8")))
    findings.extend(registry_findings(bodies["registry"], spec_digest()))
    findings.extend(policy_findings(bodies["policy"], read_bytes(POLICY)))
    findings.extend(new_target_findings())
    findings.extend(composition_findings())
    for key, body in bodies.items():
        target = ROOT / ACTS[key][2]
        findings.extend(manifest_findings(
            key, target.read_text() if target.is_file() else None,
            render(key, body)))
    packet = ROOT / PACKET
    findings.extend(packet_findings(
        packet.read_text() if packet.is_file() else None,
        {k: sha256(v) for k, v in bodies.items()}))
    return findings


# ------------------------------------------------------------ selftest


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
    current = read_bytes(POLICY)
    proposed = bodies["policy"]
    spec = spec_digest()
    count = 0

    def expect(label: str, got: list[str]) -> bool:
        nonlocal count
        count += 1
        if not got:
            print(f"SELFTEST FAILED: {label} passed")
            return False
        return True

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
        ("a consent head naming the Butlers repository",
         consent.replace("Purpose: test-only.",
                         f"Purpose: test-only, like {BUTLERS_OBSERVED}.", 1)),
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

    registry_mutants = (
        ("invalid registry JSON", registry + b"}"),
        ("a second registry entry",
         reg_doc(lambda d: d["entries"].append(dict(d["entries"][0])))),
        ("a registry for another project",
         reg_doc(lambda d: d.__setitem__("project", "project:butlers"))),
        ("the Butlers observerId",
         reg(lambda e: e.__setitem__("observerId",
                                     "polaris-butlers-project-shape"))),
        ("a registry subject naming the Butlers repository",
         reg(lambda e: e["subject"].__setitem__("observedRepository",
                                                BUTLERS_OBSERVED))),
        ("a stale PWB specification digest",
         reg(lambda e: e["governingBehaviorContract"].__setitem__(
             "version", "sha256:" + "0" * 64))),
        ("a non-empty write surface",
         reg(lambda e: e["typedAuthority"].__setitem__("writeSurface",
                                                       ["docs/"]))),
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

    def pol(fn) -> bytes:
        doc = json.loads(proposed)
        fn(doc)
        return json.dumps(doc, indent=2).encode()

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
         pol(lambda d: d["selfObservationScope"].__setitem__(
             "observedRepository", BUTLERS_OBSERVED))),
        ("a self scope that caches",
         pol(lambda d: d["selfObservationScope"]["ingestBoundaries"].append(
             "cache"))),
        ("a phase-A seed that is not a file here",
         pol(lambda d: d["selfObservationScope"].__setitem__(
             "phaseASeedPaths", ["about/README.md"]))),
        ("an empty self-reference rule",
         pol(lambda d: d["selfObservationScope"].__setitem__(
             "selfReferenceRule", " "))),
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
        if not expect("an occupied install target", new_target_findings(root)):
            return 1
        sibling = root / CANDIDATES / "other-package" / "proposed"
        sibling.mkdir(parents=True)
        (sibling / "x.patch").write_text(
            f"--- a/{POLICY.as_posix()}\n+++ b/{POLICY.as_posix()}\n")
        if not expect("a sibling patching the policy",
                      composition_findings(root)):
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
    print(f"selftest: {count} predicates — consent pair, class, drafted owner "
          "quotation, status and head; registry JSON, entry count, project, "
          "observerId collision, pair, specification digest, write surface, "
          "code execution, working-tree read, served route, cache and limit semantics; policy "
          "drift, corruption, no-op, version, base scope, detectors, self "
          "scope, boundaries, seed and rule sentences; proposed population, "
          "occupied install target, sibling composition, three manifests' "
          "digest, path and absence, and the packet's two quoted arguments "
          "and absent policy offer all fail closed")
    return 0


# --------------------------------------------------------------- apply


def apply(key: str, at_adoption: bool) -> int:
    if not at_adoption:
        print("refusing: --apply installs act-bound bytes; it is the adoption "
              "step and belongs in the change that records that act. Pass "
              "--at-adoption.")
        return 2
    findings = check()
    if findings:
        print("refusing to apply: the package does not verify")
        for finding in findings:
            print(f"  {finding}")
        return 1
    target = ROOT / ACTS[key][1]
    if key == "policy":
        target.write_bytes(policy_proposed())
    else:
        source = ROOT / PROPOSED / (CONSENT_NAME if key == "consent"
                                    else REGISTRY_NAME)
        shutil.copyfile(source, target)
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
        print("Syzygy self-observation act packets verify: 3 manifests match "
              "their 3 proposed artifacts (consent, registry entry, policy "
              "extension); the policy patch applies to the bound bytes")
        for key, body in bodies.items():
            print(f"  {key}: {sha256(body)}  {ACTS[key][1].as_posix()}")
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
