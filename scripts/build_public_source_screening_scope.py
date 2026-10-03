#!/usr/bin/env python3
"""Build and verify the inert public-source screening-scope package.

Package `contracts/candidates/public-source-screening-scope/` (`syzygy-mea`,
gap 12). This script performs no owner act and writes no act record.

The subject is `project:syzygy`'s secret-classification policy. The package
adds one additive top-level object, `publicSourceScope`, and bumps
`policyVersion` by one minor; every other key stays byte-equal. The proposed
bytes live only as a unified diff under `proposed/`; the one-row manifest
hashes the bytes the diff produces, and that row is the argument a superseding
`approve-policy` act would take.

The diff is GENERATED from the policy bytes on disk, never hand-written. That
is the reconciliation with PR #120 (self-observation scope, which also adds a
top-level object and bumps the version): whichever act lands second reruns
`--write` against the other's performed bytes, and the next minor follows
automatically. `--check` fails while the package is stale against the policy.

  --write            regenerate the patch and the manifest
  --check            verify the package against the policy on disk
  --manifest-digest  print the SHA-256 of the manifest FILE
  --selftest         mutate each predicate; each must fail

Review-head contract for the recorder written after the review: the raw's
first four non-blank lines carry `Reviewed commit: <40 hex>`,
`Manifest SHA-256: <SHA-256 of the manifest FILE>` and a `Verdict:` line
(`CONFIRM` or `CONFIRM WITH EXCEPTIONS`); findings are numbered
`**Finding N — title** (blocking|revise|note)`.
"""

from __future__ import annotations

import copy
import difflib
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
POLICY = pathlib.Path(".syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json")
PKG = pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope")
PATCH = PKG / "proposed" / (POLICY.name + ".patch")
MANIFEST = PKG / "PUBLIC-SOURCE-SCREENING-SCOPE-MANIFEST.txt"
SCOPE_KEY = "publicSourceScope"
RFC5_14_CLASSES = ("governance-text", "code-structure", "code-content",
                   "work-history", "evidence-content", "derived-composites")
#: Ranges over RFC5-14's closed vocabulary that the public scope may classify
#: into. `work-history` is never classified for a public target (owner answer
#: Q2) and `project-documentation` is not yet in the vocabulary (Q7).
SCOPE_CLASSES = ("code-structure", "code-content", "derived-composites")
ROW = re.compile(r"^([0-9a-f]{64})  (\S+)$", re.MULTILINE)

#: [Inferred] proposals for the owner; a file with another extension is
#: indeterminate and refused egress, never guessed.
SOURCE_EXTENSIONS = [".c", ".h", ".cc", ".cpp", ".hpp", ".cs", ".go", ".java", ".js",
                     ".mjs", ".cjs", ".jsx", ".kt", ".lua", ".php", ".py", ".pyi",
                     ".rb", ".rs", ".sh", ".sql", ".swift", ".tcl", ".ts", ".tsx"]

INSTRUCTION_SYMBOLS = [
    {"path": "packages/polaris-generation-core/src/prompts.ts", "symbol": "promptForStage"},
    {"path": "packages/polaris-generation-core/src/provider-draft.ts", "symbol": "stageSchema"},
]


def public_scope() -> dict:
    return {
        "purpose": "admit arbitrary public repositories to the Polaris generator: read their Git snapshot objects, screen them under this policy and classify them into RFC5-14 classes; a target repository's own text is data to screen, never policy (RFC3-30)",
        "observingProject": "project:syzygy",
        "observedRepositories": "exactly the repository ids named by an effective public-repository observation consent record whose subject is (project:syzygy, repository:<id>); the policy names no repository, so admitting or withdrawing a target never edits it",
        "authorizationModes": ["owner-trusted-bootstrap"],
        "ingestBoundaries": ["observation", "model", "run-directory", "human-html"],
        "ingestBoundaryRule": "run-directory is a per-run directory under project:syzygy's state directory, outside git; human-html is a generated editorial draft shown only on the local daemon's draft view or as a static file in the run directory, never published; there is no cache, log, machine-json or walkthrough-record boundary for this scope",
        "sourceAdmission": {
            "discoveryMode": "all-tracked-blobs-at-admitted-commit",
            "gitObjectsOnly": True,
            "admittedSnapshot": "the commit object ids listed by the observation consent; a tag name is a label only",
            "notAdmitted": ["symbolic links (mode 120000)", "submodule entries (mode 160000)", "any object outside the listed commits' root trees"],
            "resourceLimits": "the limits declared by the registered source-acquisition entry for the fetch; a limit failure excludes the whole artifact as unclassifiable-excluded",
            "deniedPaths": "the base policy's sourceAdmission.deniedPathBasenames, deniedPathPrefixes, deniedPathSuffixes and pathRuleScope apply unchanged",
            "allowedTextEncodings": ["utf-8"],
        },
        "contentClassification": {
            "vocabulary": "RFC5-14's closed vocabulary; this scope classifies into the classes in classesClassified only",
            "classesClassified": list(SCOPE_CLASSES),
            "neverClassified": ["work-history"],
            "rules": [
                {"class": "code-structure", "rule": "normalized repository-relative paths, object ids and sizes of admitted snapshot entries, taken from Git tree metadata, with no body"},
                {"class": "code-content", "rule": "the body of an admitted blob whose final path segment ends with one of sourceExtensions, after every screening step", "sourceExtensions": SOURCE_EXTENSIONS},
                {"class": "derived-composites", "rule": "computed from the classes of what a composite embeds (RFC5-14); a composite embedding any unclassified or excluded content is refused"},
            ],
            "governanceTextPaths": [],
            "evidenceContentPaths": [],
            "indeterminate": "every other admitted blob, including README, guides, tutorials, LICENSE files, configuration and data, is indeterminate: refused egress and shown as such. A later policy version maps prose once RFC5-14 defines a class for it",
        },
        "instructionTextRule": {
            "class": "code-content",
            "classOwner": "project:syzygy",
            "closedList": INSTRUCTION_SYMBOLS,
            "rule": "the generator's instruction text is the text produced by exactly these two symbols at the prompt and schema versions a request names; it is not target content and is not read from a target. No other file or symbol of project:syzygy's repository is classified by this rule. Every detector in this policy applies to it before the first request of a run",
        },
        "detectors": "every detector in this policy applies unchanged to every body under this scope, including inert code contexts; public visibility exempts nothing, and a match excludes the whole artifact with hash-not-body provenance (matchAction, RFC5-17)",
        "activeContent": {
            "markdownAndProse": "the base activeContentClassification applies unchanged to Markdown and any other prose that would be rendered as markup",
            "otherAdmittedFiles": "every other admitted file is untrusted text that is never interpreted as markup: it is scanned by every detector and context-encoded at every sink, as the base inertContextRule already requires of inert bytes; markup-like bytes in it are not an active-content match",
        },
        "accessBoundary": {
            "postgresql": False, "credentialApi": False, "processEnvironment": False,
            "workingTree": False, "untrackedFiles": False, "observedCodeExecution": False,
            "networkEgress": False,
            "networkEgressRoutes": ["the shallow by-commit fetch from the target's upstream that the observation consent describes", "the registered provider route through the single egress check"],
            "routeRule": "networkEgress is false except for these two routes; the base accessBoundary is otherwise unchanged",
        },
        "rawBodyHandling": {
            "storage": "run-directory-only",
            "logging": "never",
            "rendering": "quoted-context-encoded-spans-in-editorial-draft",
            "machineResponse": "never",
            "externalEgress": "classified-content-under-an-effective-egress-consent",
            "rule": "storage is permitted only inside a run directory under project:syzygy's state directory, outside git; rendering only in a generated editorial draft; external egress only for content this scope classifies and only under a separate egress consent for the pair",
        },
        "inheritedRules": "every other rule in this policy applies to this scope unchanged: detectors, matchAction, unclassifiableExclusion, redactionClasses and the strict-UTF-8 and NUL rules. The base classificationOrder and classificationSuccess name the signed PWB grammar; under this scope they read: membership in the admitted snapshot replaces membership in a PWB phase, and the content-classification rules above replace the PWB closed extraction class. No approved requirement names this reading, so it is this policy's own and binds only through the act that approves it",
        "selfReferenceRule": "a target repository's policy, configuration or documentation text is never an input to this policy's evaluation (RFC3-30); authority for a pair is evaluated only for that pair and is never inherited from another pair, including through expectations keyed only by the observing project",
    }


def bump_minor(version: str) -> str:
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)(-.+)", version)
    if not m:
        raise ValueError(f"unparseable policyVersion {version}")
    return f"{m.group(1)}.{int(m.group(2)) + 1}.0{m.group(4)}"


def dump(doc: dict) -> str:
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


def propose(base_text: str) -> str:
    """Text insertion, so every base byte outside the two edits is preserved
    (the policy file is hand-formatted and does not round-trip through a
    serializer)."""
    base = json.loads(base_text)
    if SCOPE_KEY in base:
        raise ValueError(f"policy already carries {SCOPE_KEY}")
    lines = base_text.splitlines(True)
    version = f'  "policyVersion": "{base["policyVersion"]}",\n'
    if lines.count(version) != 1:
        raise ValueError("policyVersion line not found exactly once")
    lines[lines.index(version)] = f'  "policyVersion": "{bump_minor(base["policyVersion"])}",\n'
    start = lines.index('  "scope": {\n')
    end = lines.index("  },\n", start)
    block = json.dumps(public_scope(), indent=2, ensure_ascii=False).replace("\n", "\n  ")
    lines.insert(end + 1, f'  "{SCOPE_KEY}": {block},\n')
    out = "".join(lines)
    expected = dict(base)
    expected["policyVersion"] = bump_minor(base["policyVersion"])
    got = json.loads(out)
    reordered = {k: got[k] for k in got if k != SCOPE_KEY}
    if reordered != expected or got[SCOPE_KEY] != public_scope():
        raise ValueError("text insertion changed something other than policyVersion and the new scope")
    return out


def unified(base_text: str, new_text: str) -> str:
    return "".join(difflib.unified_diff(
        base_text.splitlines(True), new_text.splitlines(True),
        f"a/{POLICY.as_posix()}", f"b/{POLICY.as_posix()}", n=1))


def apply_patch(root: pathlib.Path, base_text: str, patch_text: str) -> str:
    with tempfile.TemporaryDirectory() as d:
        target = pathlib.Path(d) / POLICY
        target.parent.mkdir(parents=True)
        target.write_text(base_text)
        done = subprocess.run(["patch", "-p1", "--no-backup-if-mismatch", "-s"],
                              cwd=d, input=patch_text, text=True, capture_output=True)
        if done.returncode != 0:
            raise ValueError("patch does not apply: " + (done.stdout + done.stderr).strip()[:200])
        return target.read_text()


def manifest_text(proposed: str) -> str:
    return ("# PUBLIC-SOURCE SCREENING SCOPE MANIFEST\n"
            "# Candidate; this file and its row bind nothing by themselves.\n"
            "# 1 artifact; the row hashes the PROPOSED bytes (the policy with\n"
            "# proposed/<name>.patch applied) and is the argument of one superseding\n"
            "# approve-policy act over that subject.\n"
            f"{hashlib.sha256(proposed.encode()).hexdigest()}  {POLICY.as_posix()}\n")


def semantic_findings(base_text: str, proposed_text: str) -> list[str]:
    """Structural claims the packet makes; each is mutated in --selftest."""
    base, new = json.loads(base_text), json.loads(proposed_text)
    bad: list[str] = []
    if new.get("policyVersion") != bump_minor(base["policyVersion"]):
        bad.append("policyVersion is not the next minor")
    if {k: v for k, v in new.items() if k not in (SCOPE_KEY, "policyVersion")} != {
            k: v for k, v in base.items() if k != "policyVersion"}:
        bad.append("a key other than policyVersion and the new scope differs from the base")
    scope = new.get(SCOPE_KEY)
    if not isinstance(scope, dict):
        return bad + ["publicSourceScope missing"]
    classes = scope["contentClassification"]["classesClassified"]
    if not set(classes) <= set(SCOPE_CLASSES) or "work-history" in classes:
        bad.append("classesClassified leaves the allowed RFC5-14 subset or includes work-history")
    if "project-documentation" in json.dumps(scope):
        bad.append("scope names project-documentation, which RFC5-14 does not yet define")
    if [(s["path"], s["symbol"]) for s in scope["instructionTextRule"]["closedList"]] != [
            (s["path"], s["symbol"]) for s in INSTRUCTION_SYMBOLS]:
        bad.append("instruction-text list is not exactly the two declared symbols")
    raw = scope["rawBodyHandling"]
    if raw["logging"] != "never" or raw["machineResponse"] != "never":
        bad.append("logging and machine response must stay never")
    ab = scope["accessBoundary"]
    if any(ab[k] for k in ("postgresql", "credentialApi", "processEnvironment", "workingTree",
                           "untrackedFiles", "observedCodeExecution", "networkEgress")):
        bad.append("an accessBoundary field other than the two named routes is true")
    if len(ab["networkEgressRoutes"]) != 2:
        bad.append("networkEgress routes are not exactly two")
    if scope["authorizationModes"] != ["owner-trusted-bootstrap"]:
        bad.append("authorizationModes is not exactly owner-trusted-bootstrap")
    if "machine-json" in scope["ingestBoundaries"] or "log" in scope["ingestBoundaries"]:
        bad.append("an ingest boundary the scope forbids is present")
    if scope["contentClassification"]["governanceTextPaths"] or scope["contentClassification"]["evidenceContentPaths"]:
        bad.append("governance-text or evidence-content path rules are non-empty in this version")
    return bad


def check(root: pathlib.Path = ROOT) -> list[str]:
    findings: list[str] = []
    base_text = (root / POLICY).read_text()
    try:
        proposed = propose(base_text)
    except ValueError as exc:
        return [str(exc)]
    expected_patch = unified(base_text, proposed)
    patch_path, manifest_path = root / PATCH, root / MANIFEST
    if not patch_path.is_file() or patch_path.read_text() != expected_patch:
        findings.append("patch differs from its regeneration over the policy on disk")
    else:
        try:
            if apply_patch(root, base_text, patch_path.read_text()) != proposed:
                findings.append("applying the patch does not yield the proposed bytes")
        except ValueError as exc:
            findings.append(str(exc))
    if not manifest_path.is_file() or manifest_path.read_text() != manifest_text(proposed):
        findings.append("manifest differs from its regeneration")
    present = sorted(p.name for p in (root / PKG / "proposed").glob("*")) if (root / PKG / "proposed").is_dir() else []
    if present != [PATCH.name]:
        findings.append(f"proposed/ holds {present}, not exactly the declared patch")
    findings += semantic_findings(base_text, proposed)
    return findings


def write(root: pathlib.Path = ROOT) -> None:
    base_text = (root / POLICY).read_text()
    proposed = propose(base_text)
    (root / PATCH).parent.mkdir(parents=True, exist_ok=True)
    (root / PATCH).write_text(unified(base_text, proposed))
    (root / MANIFEST).write_text(manifest_text(proposed))


def selftest() -> int:
    results: list[tuple[str, bool]] = []
    with tempfile.TemporaryDirectory() as d:
        scratch = pathlib.Path(d)
        (scratch / POLICY).parent.mkdir(parents=True)
        shutil.copy(ROOT / POLICY, scratch / POLICY)
        write(scratch)
        results.append(("pristine package checks clean", check(scratch) == []))

        def mutate(name: str, fn, needle: str) -> None:
            snap = {p: p.read_bytes() for p in (scratch / PKG).rglob("*") if p.is_file()}
            policy = (scratch / POLICY).read_bytes()
            try:
                fn()
                got = check(scratch)
                results.append((name, any(needle in f for f in got)))
            finally:
                (scratch / POLICY).write_bytes(policy)
                for p in (scratch / PKG).rglob("*"):
                    if p.is_file() and p not in snap:
                        p.unlink()
                for p, b in snap.items():
                    p.write_bytes(b)

        def edit_patch(old, new):
            return lambda: (scratch / PATCH).write_text((scratch / PATCH).read_text().replace(old, new, 1))

        mutate("a one-byte patch edit is caught", edit_patch('"observingProject"', '"observingProjecT"'), "patch differs")
        def flip_manifest():
            row = (scratch / MANIFEST).read_text().splitlines(True)
            row[-1] = ("0" if row[-1][0] != "0" else "1") + row[-1][1:]
            (scratch / MANIFEST).write_text("".join(row))

        mutate("a one-character manifest digest edit is caught", flip_manifest, "manifest differs")
        mutate("a policy that moved under the package is caught",
               lambda: (scratch / POLICY).write_text((scratch / POLICY).read_text().replace(
                   '"schemaVersion": 1', '"schemaVersion": 1,\n  "note": "x"', 1)),
               "differs from its regeneration")
        mutate("an extra file under proposed/ is caught",
               lambda: (scratch / PKG / "proposed" / "extra.patch").write_text("x"), "proposed/ holds")
        mutate("a policy that already carries the scope is refused",
               lambda: (scratch / POLICY).write_text(propose((scratch / POLICY).read_text())), "already carries")

        # semantic predicates, mutated on the proposed bytes
        base_text = (ROOT / POLICY).read_text()
        proposed = propose(base_text)

        def sem(name, fn, needle):
            doc = json.loads(proposed)
            fn(doc)
            results.append((name, any(needle in f for f in semantic_findings(base_text, dump(doc)))))

        sem("work-history classified is caught", lambda x: x[SCOPE_KEY]["contentClassification"]["classesClassified"].append("work-history"), "work-history")
        sem("project-documentation named is caught", lambda x: x[SCOPE_KEY].update(note="project-documentation"), "project-documentation")
        sem("a third instruction symbol is caught", lambda x: x[SCOPE_KEY]["instructionTextRule"]["closedList"].append({"path": "x.ts", "symbol": "y"}), "instruction-text list")
        sem("logging opened is caught", lambda x: x[SCOPE_KEY]["rawBodyHandling"].update(logging="run-directory-only"), "logging")
        sem("workingTree opened is caught", lambda x: x[SCOPE_KEY]["accessBoundary"].update(workingTree=True), "accessBoundary")
        sem("a third egress route is caught", lambda x: x[SCOPE_KEY]["accessBoundary"]["networkEgressRoutes"].append("z"), "exactly two")
        sem("independently-verified mode added is caught", lambda x: x[SCOPE_KEY].update(authorizationModes=["independently-verified", "owner-trusted-bootstrap"]), "authorizationModes")
        sem("machine-json boundary added is caught", lambda x: x[SCOPE_KEY]["ingestBoundaries"].append("machine-json"), "ingest boundary")
        sem("a base key altered is caught", lambda x: x["rawBodyHandling"].update(logging="run"), "differs from the base")
        sem("version not bumped is caught", lambda x: x.update(policyVersion=json.loads(base_text)["policyVersion"]), "next minor")
        sem("governance-text path rule added is caught", lambda x: x[SCOPE_KEY]["contentClassification"].update(governanceTextPaths=["docs/**"]), "non-empty")
    failed = [n for n, ok in results if not ok]
    for n, ok in results:
        print(("ok   " if ok else "FAIL ") + n)
    print(f"selftest: {len(results) - len(failed)} of {len(results)} predicates held")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode == "--selftest":
        return selftest()
    if mode == "--write":
        write()
        print("wrote", PATCH.as_posix(), "and", MANIFEST.as_posix())
        return 0
    if mode == "--manifest-digest":
        if check():
            print("refusing: package is stale; run --check", file=sys.stderr)
            return 1
        print(hashlib.sha256((ROOT / MANIFEST).read_bytes()).hexdigest())
        return 0
    if mode == "--check":
        findings = check()
        for f in findings:
            print("FINDING", f)
        print("public-source screening scope:", "STALE" if findings else "current")
        return 1 if findings else 0
    print(f"unknown mode {mode}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
