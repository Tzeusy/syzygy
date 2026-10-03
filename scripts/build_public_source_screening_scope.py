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

The diff is GENERATED from the policy bytes on disk, never hand-written. PR #120
(self-observation scope) also adds a top-level object and bumps the version,
and the ordering is asymmetric: if PR #120 is performed first, this package
reruns `--write` against its performed bytes and the next minor follows; if
this package is performed first, PR #120's builder needs code edits and a changed
digest-bound consent. This package therefore uses its own label
(`public-source-candidate.1`). `--check` fails while the package is stale
against the policy, and also while the target-metadata field list it embeds
differs from the pipeline's `sourcePopulation` in `pipeline.ts`.

  --write            regenerate the patch and the manifest
  --check            verify the package against the policy on disk
  --manifest-digest  print the SHA-256 of the manifest FILE
  --selftest         mutate each predicate; each must fail

`--check` also reports act-readiness: the closed exclusion-reason set must be
readable from the exported constant `GENERATION_EXCLUSION_REASONS` in
generation-source.ts. It is read through the TypeScript compiler API by
`scripts/read_ts_exported_string_array.mjs` (node and the repo's `typescript`
dependency; if either is missing the reader refuses). A package that is not
act-ready exits 1 unless `--pending-symbol` is passed; the proposed bytes and
the manifest do not depend on the constant's values.

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
#: indeterminate: excluded from reading and from egress, never guessed.
SOURCE_EXTENSIONS = [".c", ".h", ".cc", ".cpp", ".hpp", ".cs", ".go", ".java", ".js",
                     ".mjs", ".cjs", ".jsx", ".kt", ".lua", ".php", ".py", ".pyi",
                     ".rb", ".rs", ".sh", ".sql", ".swift", ".tcl", ".ts", ".tsx"]

RUN_PROFILE_SYMBOLS = [
    {"path": "packages/polaris-generation-core/src/dossier-profile.ts", "symbol": "DOSSIER_READER_QUESTIONS"},
    {"path": "packages/polaris-generation-core/src/dossier-profile.ts", "symbol": "DOSSIER_REQUESTED_ASSETS"},
]

INSTRUCTION_SYMBOLS = [
    {"path": "packages/polaris-generation-core/src/prompts.ts", "symbol": "promptForStage"},
    {"path": "packages/polaris-generation-core/src/provider-draft.ts", "symbol": "stageSchema"},
]


PIPELINE = pathlib.Path("packages/polaris-generation-core/src/pipeline.ts")
GENERATION_SOURCE = pathlib.Path("packages/polaris-generation-core/src/generation-source.ts")
#: [Inferred] the closed set of exclusion reasons is the value of this exported
#: constant, which is not yet in code (requested of the generator's lane). The
#: rule names the symbol and lists no reason, so the set cannot go stale in the
#: policy; the builder reads it and fails closed while it is absent.
EXCLUSION_REASON_SYMBOL = {"path": GENERATION_SOURCE.as_posix(), "symbol": "GENERATION_EXCLUSION_REASONS"}


READER = pathlib.Path("scripts/read_ts_exported_string_array.mjs")


def exclusion_reasons(root: pathlib.Path = ROOT, script: pathlib.Path | None = None) -> list[str]:
    """The closed exclusion-reason set, read from the exported constant in
    generation-source.ts through the TypeScript compiler API (a node script,
    never a text scan). Fails closed: no node, no `typescript`, a file with
    syntax errors, a symbol not bound exactly once at the top level, not
    exported, not `const`, not a literal array of string literals `as const`, or
    an empty, repeating or non-kebab-case set is an error. (`script` is for the
    selftest's mutants.)"""
    path = root / GENERATION_SOURCE
    if not path.is_file():
        raise ValueError(f"{GENERATION_SOURCE.as_posix()} is absent")
    if shutil.which("node") is None:
        raise ValueError("node is unavailable, so the reason set cannot be read")
    done = subprocess.run(["node", str(script or ROOT / READER), str(path), EXCLUSION_REASON_SYMBOL["symbol"]],
                          capture_output=True, text=True, timeout=60)
    if done.returncode != 0:
        why = done.stderr.strip().splitlines()
        raise ValueError(why[-1] if why else "the reader failed")
    try:
        reasons = json.loads(done.stdout)
    except ValueError:
        raise ValueError("the reader printed something other than a JSON array")
    sym = EXCLUSION_REASON_SYMBOL["symbol"]
    if not isinstance(reasons, list) or not reasons or any(not isinstance(r, str) or not re.fullmatch(r"[a-z][a-z0-9-]*", r) for r in reasons) \
            or len(set(reasons)) != len(reasons):
        raise ValueError(f"{sym} is empty, repeats a reason or holds more than kebab-case string literals")
    return reasons


def check_exit(findings: list[str], ready: list[str], pending: bool) -> int:
    """Exit status of `--check`: stale bytes always fail; a package that is not
    act-ready fails unless `--pending-symbol` was passed."""
    return 1 if findings or (ready and not pending) else 0


def source_population_fields(root: pathlib.Path = ROOT) -> list[str]:
    """Field names of the `sourcePopulation` entry the pipeline sends, read from
    pipeline.ts. Fails closed: a shape this cannot read is an error, never an
    empty list (the egress record's generated table classes the field
    `sourcePopulation` as target-metadata; this names its members)."""
    text = (root / PIPELINE).read_text()
    m = re.search(r"const sourcePopulation = frozen\.sources\.map\(source => \(\{(.*?)\}\)\);", text, re.S)
    if not m:
        raise ValueError("cannot read the sourcePopulation entry shape in pipeline.ts")
    body = re.sub(r"\.\.\.\(source\.exclusion\.excluded \? \{ reason: [^}]*\} : \{\}\)", "reason: <excluded only>", m.group(1))
    names = re.findall(r"(?:^|,)\s*(\w+)\s*:", body)
    if not names or "sourceId" not in names:
        raise ValueError("sourcePopulation entry has no readable fields")
    return names


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
                {"class": "code-content", "rule": "the body of an admitted blob whose final path segment ends with one of sourceExtensions, compared case-sensitively as ASCII, after every screening step. Configuration written in a listed extension (for example a .config.js file, setup.py or a .sh file) is therefore code-content. No extractor runs: the class is by extension and the body is admitted as whole-blob spans", "sourceExtensions": SOURCE_EXTENSIONS},
                {"class": "derived-composites", "rule": "computed from the classes of what a composite embeds (RFC5-14); a composite embedding any unclassified or excluded content is refused"},
            ],
            "governanceTextPaths": [],
            "evidenceContentPaths": [],
            "indeterminate": "every other admitted blob, including README files, guides, tutorials, specification and design documents, committed reports, LICENSE files, and configuration or data in an extension outside sourceExtensions, is indeterminate and is treated as unclassifiable under unclassifiableExclusion: excluded from reading and from egress (fail closed), recorded hash-not-body, and never stored or rendered. Its path, object id and size remain code-structure. A later policy version maps prose once RFC5-14 defines a class for it",
        },
        "instructionTextRule": {
            "class": "code-content",
            "classOwner": "project:syzygy",
            "closedList": INSTRUCTION_SYMBOLS,
            "rule": "the generator's instruction text is the text produced by exactly these two symbols at the prompt and schema versions a request names; it is not target content and is not read from a target. No other file or symbol of project:syzygy's repository is classified by this rule. Every detector in this policy applies to it before the first request of a run",
        },
        "classificationBasis": "a class is decided at the runtime check from the origin of the content, tracked from where it entered the choke point (RFC5-14); a field name never assigns it. The field-level table in a public-target egress record is a gate on which fields may be carried and cannot confer a class, so content under a classed field name keeps the class of its origin (REQ-polaris-generation-025: composition preserves embedded classifications and origins)",
        "targetMetadataRule": {
            "class": "code-structure",
            "fields": source_population_fields(),
            "fieldsDerivedFrom": "the sourcePopulation entry in packages/polaris-generation-core/src/pipeline.ts, read by this builder; the confirmed admission egress record's generated table classes the field sourcePopulation as target-metadata",
            "rule": "the metadata the generator carries for each admitted-snapshot source, admitted or excluded alike, is exactly the fields listed and nothing else; reason is carried only for an excluded source and only as a member of the closed set that exclusionReasonSymbol names. No body, no content digest and no policy detail is carried under this rule. A path of an excluded source is not in the list and is not carried: the sourceId of an excluded source is an opaque identifier not derived from its path or body. [Inferred] this bytes-level rule is enforced only by the reader implementation, which the generator's lane is asked to write that way; nothing else in these bytes checks it",
            "exclusionReasonSymbol": EXCLUSION_REASON_SYMBOL,
            "reasonRule": "the closed set of exclusion reasons is exactly the values of the exported constant named by exclusionReasonSymbol, read from code at the commit a run names; this policy lists no reason, so the set cannot differ from the values the constant declares. A reason outside that constant is not carried, and the generator's validator refuses it before a request. [Inferred] the constant and the validator are requested of the generator's lane and are not in code at this package's base; the package is not ready for an act until the constant exists (the builder fails closed while it is absent)",
        },
        "runProfileRule": {
            "class": "code-content",
            "classOwner": "project:syzygy",
            "closedList": RUN_PROFILE_SYMBOLS,
            "rule": "the run's reader questions and requested assets are classified only when they are the values of exactly these code-declared symbols, selected by a profile id a request carries (which id and which carrier is an open owner question: the base has no request field for one). A value from any other origin, including a run-directory file or an operator-supplied string, is unclassified under this scope and is not carried until a later policy version defines its origin and a validation. [Observed on the branch of PR #259] these symbols are readonly constants in dossier-profile.ts; [Observed on the base] the pipeline types readerQuestions as unknown, validates only requestedAssets and forwards readerQuestions unchanged, and no code reads a run-profile file. The typed reader-question validation the owner asked for is not yet in code and is not assumed here",
        },
        "detectors": "every detector in this policy applies unchanged to every body under this scope, including inert code contexts; public visibility exempts nothing, and a match excludes the whole artifact with hash-not-body provenance (matchAction, RFC5-17)",
        "activeContent": {
            "rule": "the base activeContentClassification, inertContextRule and the active-content condition of classificationSuccess apply unchanged to every admitted body, Markdown or not: a body with an active-content form outside a valid inert code context is excluded whole as active content. This scope adds no loosening",
            "consequence": "[Inferred] a source file that embeds markup-like bytes outside a valid inert code context, for example an HTML string in a script, is withheld. The first run measures how many; a loosening would be a later policy version and an explicit owner question",
        },
        "accessBoundary": {
            "postgresql": False, "credentialApi": False, "processEnvironment": False,
            "workingTree": False, "untrackedFiles": False, "observedCodeExecution": False,
            "networkEgress": False,
            "networkEgressRoutes": ["the shallow by-commit fetch from the target's upstream that the observation consent describes", "the registered provider route through the single egress check"],
            "routeRule": "the networkEgress boolean stays false as the base reads it; the only permitted network use is these two routes, carried beside it, and a consumer that reads the boolean alone fails closed. The base accessBoundary is otherwise unchanged",
        },
        "rawBodyHandling": {
            "storage": "run-directory-only",
            "logging": "never",
            "rendering": "quoted-context-encoded-spans-in-editorial-draft",
            "machineResponse": "never",
            "externalEgress": "classified-content-under-an-effective-egress-consent",
            "rule": "storage is permitted only inside a run directory under project:syzygy's state directory, outside git; rendering only in a generated editorial draft; external egress only for content this scope classifies and only under a separate egress consent for the pair",
        },
        "inheritedRules": "every other rule in this policy applies to this scope unchanged: detectors, matchAction, unclassifiableExclusion, redactionClasses, activeContentClassification and the strict-UTF-8 and NUL rules. 'Every other rule' means the policy's rules outside any named scope object; the rules inside the base scope object, and inside any sibling scope object another act adds, do not govern this scope, and the other way round: the routes, boundaries, rawBodyHandling and rules written inside this object govern only the repositories in observedRepositories and never the base scope or a sibling scope. The base classificationOrder and classificationSuccess name the signed PWB grammar; under this scope they read: membership in the admitted snapshot replaces membership in a PWB phase, and the content-classification rules above replace the PWB closed extraction class, so a blob with no class under those rules has an unknown extraction class and is excluded whole (step 6), while a code-content body needs no extractor and is admitted as whole-blob spans. No approved requirement names this reading, so it is this policy's own and binds only through the act that approves it",
        "selfReferenceRule": "a target repository's policy, configuration or documentation text is never an input to this policy's evaluation (RFC3-30); authority for a pair is evaluated only for that pair and is never inherited from another pair, including through expectations keyed only by the observing project",
    }


def bump_minor(version: str) -> str:
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)(-.+)", version)
    if not m:
        raise ValueError(f"unparseable policyVersion {version}")
    # A label distinct from PR #120's 1.2.0-candidate.1, which names different bytes.
    return f"{m.group(1)}.{int(m.group(2)) + 1}.0-public-source-candidate.1"


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
    if [(x["path"], x["symbol"]) for x in scope["runProfileRule"]["closedList"]] != [
            (x["path"], x["symbol"]) for x in RUN_PROFILE_SYMBOLS]:
        bad.append("run-profile list is not exactly the two declared symbols")
    if "never assigns it" not in scope.get("classificationBasis", ""):
        bad.append("classificationBasis does not say a field name never assigns a class")
    tm = scope.get("targetMetadataRule", {})
    if tm.get("fields") != source_population_fields():
        bad.append("targetMetadataRule fields differ from the pipeline's sourcePopulation")
    if tm.get("exclusionReasonSymbol") != EXCLUSION_REASON_SYMBOL or tm.get("class") != "code-structure":
        bad.append("targetMetadataRule reason symbol or class differ from the declared ones")
    if "exclusionReasons" in tm:
        bad.append("targetMetadataRule hand-lists exclusion reasons instead of naming the code symbol")
    if "exclusionMetadata" in scope:
        bad.append("exclusionMetadata (digest and policy fields the pipeline does not send) is back")
    if "the other way round" not in scope["inheritedRules"]:
        bad.append("sibling separation holds in one direction only")
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
    if "otherAdmittedFiles" in scope["activeContent"] or "no loosening" not in scope["activeContent"].get("rule", ""):
        bad.append("active content is loosened or no longer states that it adds no loosening")
    if "excluded from reading and from egress" not in scope["contentClassification"]["indeterminate"]:
        bad.append("indeterminate does not state the one fail-closed reading")
    if "sibling scope object" not in scope["inheritedRules"]:
        bad.append("inheritedRules does not separate sibling scopes")
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


def readiness(root: pathlib.Path = ROOT) -> list[str]:
    """Act-readiness, separate from byte currency: the closed reason set must be
    readable from code. The proposed bytes do not depend on its values."""
    try:
        exclusion_reasons(root)
    except ValueError as exc:
        return [f"not ready for an act: {exc}"]
    return []


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
        sem("a third run-profile symbol is caught", lambda x: x[SCOPE_KEY]["runProfileRule"]["closedList"].append({"path": "x.ts", "symbol": "y"}), "run-profile list")
        sem("classification by field name is caught", lambda x: x[SCOPE_KEY].update(classificationBasis="by field name"), "classificationBasis")
        sem("target metadata fields changed is caught", lambda x: x[SCOPE_KEY]["targetMetadataRule"].update(fields=["sourceId"]), "targetMetadataRule")
        sem("content digest added to target metadata is caught", lambda x: x[SCOPE_KEY]["targetMetadataRule"]["fields"].append("contentDigest"), "targetMetadataRule")
        sem("old exclusionMetadata returns is caught", lambda x: x[SCOPE_KEY].update(exclusionMetadata="digest"), "exclusionMetadata")
        sem("one-way sibling separation is caught", lambda x: x[SCOPE_KEY].update(inheritedRules=x[SCOPE_KEY]["inheritedRules"].replace("the other way round", "")), "one direction")
        sem("a hand-listed reason set is caught", lambda x: x[SCOPE_KEY]["targetMetadataRule"].update(exclusionReasons=["excluded-artifact"]), "hand-lists")
        sem("a changed reason symbol is caught", lambda x: x[SCOPE_KEY]["targetMetadataRule"]["exclusionReasonSymbol"].update(symbol="OTHER"), "reason symbol")
        sem("logging opened is caught", lambda x: x[SCOPE_KEY]["rawBodyHandling"].update(logging="run-directory-only"), "logging")
        sem("workingTree opened is caught", lambda x: x[SCOPE_KEY]["accessBoundary"].update(workingTree=True), "accessBoundary")
        sem("a third egress route is caught", lambda x: x[SCOPE_KEY]["accessBoundary"]["networkEgressRoutes"].append("z"), "exactly two")
        sem("independently-verified mode added is caught", lambda x: x[SCOPE_KEY].update(authorizationModes=["independently-verified", "owner-trusted-bootstrap"]), "authorizationModes")
        sem("machine-json boundary added is caught", lambda x: x[SCOPE_KEY]["ingestBoundaries"].append("machine-json"), "ingest boundary")
        sem("a base key altered is caught", lambda x: x["rawBodyHandling"].update(logging="run"), "differs from the base")
        sem("version not bumped is caught", lambda x: x.update(policyVersion=json.loads(base_text)["policyVersion"]), "next minor")
        sem("active content loosened is caught", lambda x: x[SCOPE_KEY]["activeContent"].update(otherAdmittedFiles="never markup"), "loosened")
        sem("indeterminate reading dropped is caught", lambda x: x[SCOPE_KEY]["contentClassification"].update(indeterminate="refused egress"), "indeterminate")
        sem("sibling scope separation dropped is caught", lambda x: x[SCOPE_KEY].update(inheritedRules="every other rule"), "sibling")
        sem("governance-text path rule added is caught", lambda x: x[SCOPE_KEY]["contentClassification"].update(governanceTextPaths=["docs/**"]), "non-empty")
    # the field list is read from pipeline.ts: a changed shape moves it, an unreadable one is refused
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        (root / PIPELINE).parent.mkdir(parents=True)
        real = (ROOT / PIPELINE).read_text()
        (root / PIPELINE).write_text(real.replace("sourceId: source.sourceId,", "sourceId: source.sourceId, path: source.path,", 1))
        results.append(("a field added to sourcePopulation moves the list", "path" in source_population_fields(root)))
        (root / PIPELINE).write_text(real.replace("const sourcePopulation = frozen.sources.map", "const sourcePopulation = frozen.sources.filter", 1))
        try:
            source_population_fields(root)
            results.append(("an unreadable sourcePopulation shape is refused", False))
        except ValueError:
            results.append(("an unreadable sourcePopulation shape is refused", True))
    # the reason set is read from code through the compiler API
    SYM = EXCLUSION_REASON_SYMBOL["symbol"]
    results.append(("--check exits 1 when not act-ready", check_exit([], ["x"], False) == 1))
    results.append(("--pending-symbol lets a not-ready package exit 0", check_exit([], ["x"], True) == 0))
    results.append(("stale bytes exit 1 even with --pending-symbol", check_exit(["stale"], [], True) == 1))
    decl = f"export const {SYM} = ['a-b', 'c'] as const;"
    ok_ab = ["a-b", "c"]
    fixtures = {   # name -> (source, expected set, or None for refused)
        "a readable constant yields its set": (f"export const {SYM} = [\n  'a-b', // x\n  'c',\n] as const;\n", ok_ab),
        "an added reason moves the set": (f"export const {SYM} = ['a-b', 'c', 'd'] as const;", ok_ab + ["d"]),
        "an absent symbol is refused": ("export const OTHER = ['a'] as const;", None),
        "an unexported symbol is refused": (f"const {SYM} = ['a'] as const;", None),
        "export let is refused": (f"export let {SYM} = ['a-b'] as const;", None),
        "a type-annotated constant is refused": (f"export const {SYM}: readonly string[] = ['a-b'] as const;", None),
        "a re-export is a second binding": (f"{decl}\nconst X = 1;\nexport {{ X as {SYM} }};\n", None),
        "an export list alone is refused": (f"const {SYM} = ['a'] as const;\nexport {{ {SYM} }};\n", None),
        "a declaration inside a function is not a declaration": (f"export function f() {{ {decl} }}\n", None),
        "a computed set is refused": (f"export const {SYM} = Object.keys(x);", None),
        "a satisfies form is refused": (f"export const {SYM} = ['a'] as const satisfies readonly string[];", None),
        "an as-other-type form is refused": (f"export const {SYM} = ['a'] as Foo;", None),
        "a non-literal member is refused": (f"export const {SYM} = ['a', b] as const;", None),
        "a template member is refused": (f"export const {SYM} = [`a`] as const;", None),
        "an uppercase member is refused": (f"export const {SYM} = ['A'] as const;", None),
        "an empty set is refused": (f"export const {SYM} = [] as const;", None),
        "a repeated reason is refused": (f"export const {SYM} = ['a', 'a'] as const;", None),
        "a commented-out declaration is not a declaration": (f"// {decl}\n", None),
        "a block-commented declaration is not a declaration": (f"/* {decl} */\n", None),
        "a string-embedded declaration is not a declaration": (f"const s = \"{decl}\";\nconst t = '{decl.replace(chr(39), chr(92) + chr(39))}';\n", None),
        "a commented member is not a member": (f"export const {SYM} = [\n  'a',\n  // 'retired',\n  /* 'old', */\n] as const;", ["a"]),
        "a commented old declaration before the live one is ignored": (f"// export const {SYM} = ['old'] as const;\n{decl}\n", ok_ab),
        "a second live declaration is refused": (f"{decl}\nexport const {SYM} = ['z'] as const;\n", None),
        "an unterminated comment is refused": (f"{decl}\n/* open", None),
        "a nested template holding the declaration is not a declaration": (f"const x = `${{`; {decl} `}}`;\n", None),
        "a regex holding a quote before a commented declaration is not a declaration": (f"const r = /'/; // '; {decl}\n", None),
        "a regex with slashes before a live declaration still reads": (f"const r = /[//]/;\n{decl}\n", ok_ab),
        "a quoted comment opener before a live declaration still reads": (f"const s = '/*';\n{decl}\nconst t = '*/';\n", ok_ab),
        "a regex with an escaped slash and star still reads": (f"const w = /\\/*x*\\//;\n{decl}\n", ok_ab),
        "a template with nested quotes before a live declaration still reads": (f"const u = `${{a ? 'x' : \"y\"}}`;\n{decl}\n", ok_ab),
        "an escaped quote before a live declaration still reads": (f"const s = 'it\\'s';\n{decl}\n", ok_ab),
        "a string running over a newline is a syntax error and is refused": (f"const s = 'abc\n{decl}\n", None),
    }
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        gs = root / GENERATION_SOURCE
        gs.parent.mkdir(parents=True)

        def read(src, script=None):
            gs.write_text(src)
            try:
                return exclusion_reasons(root, script), ""
            except ValueError as exc:
                return None, str(exc)

        for name, (src, want) in fixtures.items():
            results.append((name, read(src)[0] == want))
        # distinct refusals
        results.append(("an unexported symbol says so", "not exported" in read(f"const {SYM} = ['a'] as const;")[1]))
        results.append(("an absent symbol says so", "not declared" in read("export const OTHER = [];")[1]))
        results.append(("a repeated declaration says so", "more than one" in read(f"{decl}\n{decl}\n")[1]))
        # rule 6: each guard of the reader, removed in a copy, is caught by a fixture that needs it
        ts_dir = subprocess.run(["node", "-e", "console.log(require('path').dirname(require.resolve('typescript/package.json')))"],
                                capture_output=True, text=True, cwd=ROOT).stdout.strip()
        source = (ROOT / READER).read_text()
        mutants = [
            ("syntax errors tolerated", "if (sf.parseDiagnostics.length > 0) refuse(", "if (false) refuse(",
             ["a string running over a newline is a syntax error and is refused"]),
            ("a second binding tolerated", "if (bindings.length > 1) refuse(", "if (false) refuse(",
             ["a second live declaration is refused", "a re-export is a second binding"]),
            ("an unexported symbol tolerated", "if (!exported(st)) refuse(", "if (false) refuse(",
             ["an unexported symbol is refused"]),
            ("let tolerated", "if (!(st.declarationList.flags & ts.NodeFlags.Const)) refuse(", "if (false) refuse(",
             ["export let is refused"]),
            ("any `as` type tolerated", "init.type.typeName.getText(sf) !== 'const')", "false)",
             ["an as-other-type form is refused"]),
            ("non-string members tolerated", "if (!ts.isStringLiteral(el)) refuse(", "if (false) refuse(",
             ["a non-literal member is refused"]),
            ("a type annotation tolerated", "if (d.type) refuse(", "if (false) refuse(",
             ["a type-annotated constant is refused"]),
        ]
        scratch = pathlib.Path(tempfile.mkdtemp(prefix="reader-mutant-", dir=d))
        (scratch / "node_modules").mkdir()
        (scratch / "node_modules" / "typescript").symlink_to(ts_dir)
        for label, old, new, needs in mutants:
            if source.count(old) != 1:
                results.append((f"mutant: {label} (fragment not found exactly once)", False))
                continue
            mjs = scratch / "mutant.mjs"
            mjs.write_text(source.replace(old, new))
            caught = any(read(fixtures[n][0], mjs)[0] != fixtures[n][1] for n in needs)
            results.append((f"mutant: {label} is caught", caught))
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
    pending = "--pending-symbol" in argv[2:]
    if mode == "--manifest-digest":
        if check():
            print("refusing: package is stale; run --check", file=sys.stderr)
            return 1
        if readiness() and not pending:
            print("refusing:", readiness()[0], "(--pending-symbol prints the digest of a package that is not act-ready)", file=sys.stderr)
            return 1
        print(hashlib.sha256((ROOT / MANIFEST).read_bytes()).hexdigest())
        return 0
    if mode == "--check":
        findings = check()
        for f in findings:
            print("FINDING", f)
        print("public-source screening scope:", "STALE" if findings else "current")
        ready = readiness()
        for f in ready:
            print("NOTE" if pending else "FINDING", f)
        if not ready:
            print("exclusion reasons read from code:", ", ".join(exclusion_reasons()))
        return check_exit(findings, ready, pending)
    print(f"unknown mode {mode}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
