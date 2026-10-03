#!/usr/bin/env python3
"""Build and verify the inert public-source screening-scope version-2 package.

Package `contracts/candidates/public-source-screening-scope-v2/`
(`syzygy-mea`, dossier gap on prose sources). This script performs no owner act
and writes no act record.

Version 1 (`contracts/candidates/public-source-screening-scope/`) adds the
`publicSourceScope` object and leaves prose indeterminate "until a later policy
version maps it". Version 2 is that later version for one class: it maps the
RFC5-14 class `project-documentation` (defined by the RFC-0005 amendment of PR
#257) to a closed, literal set of repository paths. Nothing else in the scope
moves: the detectors, the active-content rule, the access boundary and the raw
body handling are byte-equal to version 1, and `work-history`,
`governance-text` and `evidence-content` stay unclassified.

The subject is the secret-classification policy of `project:syzygy` AFTER
version 1: this builder derives that base bytes from the version-1 package
(`propose` over the policy on disk, checked against the version-1 manifest
row), or takes the policy on disk when it already is those bytes. Both give the
same base, so the patch and the manifest row do not depend on whether the
version-1 act has been performed. The proposed bytes live only as a unified
diff under `proposed/`; the one-row manifest hashes the bytes the diff produces
and that row is the argument a superseding `approve-policy` act would take.

  --write                regenerate the patch and the manifest
  --check                verify the package against the policy on disk
  --ready                --check plus the prerequisites an act needs: the
                         RFC5-14 class is defined in the installed RFC-0005
                         text and the version-1 act is performed
  --manifest-digest      print the SHA-256 of the manifest FILE
  --selftest             mutate each predicate; each must fail

`--pending-prerequisite` lets `--ready` and `--manifest-digest` pass while a
prerequisite is unmet (drafting and review); the prerequisite is then a NOTE.

Review-head contract for a recorder written after the review: the raw's first
four non-blank lines carry `Reviewed commit: <40 hex>`, `Manifest SHA-256:
<SHA-256 of the manifest FILE>` and a `Verdict:` line (`CONFIRM` or `CONFIRM WITH
EXCEPTIONS`); findings are numbered `**Finding N — title** (blocking|revise|note)`.
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
sys.path.insert(0, str(ROOT / "scripts"))
import build_public_source_screening_scope as v1  # noqa: E402

POLICY = v1.POLICY
SCOPE_KEY = v1.SCOPE_KEY
PKG = pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v2")
PATCH = PKG / "proposed" / (POLICY.name + ".patch")
MANIFEST = PKG / "PUBLIC-SOURCE-SCREENING-SCOPE-V2-MANIFEST.txt"
V1_MANIFEST = v1.PKG / v1.MANIFEST.name
RFC5_INSTALLED = pathlib.Path(".syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md")
RFC5_CLASS_ROW = "| `project-documentation` |"
V1_ACT = pathlib.Path(".syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md")
V2_CLASSES = ("code-structure", "code-content", "project-documentation", "derived-composites")

#: The closed, literal rule. [Inferred] proposals for the owner, derived from the
#: kinds of file the RFC5-14 amendment names ("README, user and developer guides,
#: tutorials, how-to and overview documents, changelogs and release notes,
#: contribution guides, and licence and notice files, ordinarily"); a path outside
#: them is indeterminate, never guessed. Matching folds ASCII letters to lower
#: case in a copy of the path and nothing else; the path is carried as admitted.
#: Root names that are policy or governance text by their ordinary content
#: (design, governance, security, code of conduct) are deliberately absent.
ROOT_STEMS = ["readme", "changelog", "changes", "release-notes", "release_notes", "releasenotes",
              "contributing", "license", "licence", "copying", "notice", "notices",
              "news", "history", "authors", "faq"]
#: Owner opt-ins, off by default. Turning one on is an edit of ENABLED_OPT_INS,
#: a --write and a fresh review; it is never a flag the act chooses.
OPT_IN_STEMS = {"architecture": "architecture", "manifesto": "manifesto"}
ENABLED_OPT_INS: tuple[str, ...] = ()
PREFIX_DIGITS = "0123456789"
PREFIX_DIGIT_COUNT = 2
PREFIX_SEPARATOR = "-"
DOCUMENT_SUFFIXES = ["", ".md", ".rst", ".txt"]
DOC_TREE_ROOTS = ["docs", "doc"]
DOC_TREE_EXTENSIONS = [".md", ".rst", ".txt"]
#: Directory segments (not the file name) that take a docs-tree path out of the class.
DOC_EXCLUDED_SEGMENTS = ["adr", "adrs", "decisions", "rfc", "rfcs", "spec", "specs", "specification",
                         "design", "governance", "policy", "policies", "security"]
#: A .txt file under the docs tree is not prose when its name is on this closed list.
DOC_TXT_EXCLUDED_NAMES = ["cmakelists.txt", "robots.txt"]
DOC_TXT_EXCLUDED_PREFIXES = ["requirements"]
LICENSE_TREE_ROOTS = ["licenses"]
LICENSE_TREE_SUFFIXES = [".md", ".txt"]


def enabled_stems() -> list[str]:
    return ROOT_STEMS + [OPT_IN_STEMS[k] for k in ENABLED_OPT_INS]


def ascii_fold(path: str) -> str:
    return "".join(c.lower() if "A" <= c <= "Z" else c for c in path)


def has_numeric_prefix(name: str, r: dict) -> bool:
    p = r["rootStemNumericPrefix"]
    n = p["digitCount"]
    return len(name) > n and all(c in p["digits"] for c in name[:n]) and name[n] == p["separator"]


def classify_documentation(path: str, rule: dict | None = None) -> bool:
    """Reference reading of the rule, used by the fixtures and the mutants. The
    policy carries the rule as data; this is the oracle a consumer's code is
    checked against, not code the policy ships. Characters are compared as code
    points against the listed ASCII sets; no Unicode-aware class is used."""
    r = rule or documentation_rule()
    p = ascii_fold(path)
    if not p or p.startswith("/") or p.endswith("/") or "//" in p or "\\" in p:
        return False
    parts = p.split("/")
    if any(s in ("", ".", "..") for s in parts):
        return False
    name = parts[-1]
    if len(parts) == 1:
        stems = set(r["rootStems"])
        candidates = [name]
        if has_numeric_prefix(name, r):
            candidates.append(name[r["rootStemNumericPrefix"]["digitCount"] + 1:])
        for cand in candidates:
            for suffix in r["documentSuffixes"]:
                if cand.endswith(suffix) and cand[:len(cand) - len(suffix)] in stems:
                    return True
        return False
    if parts[0] in r["docTreeRoots"] and any(name.endswith(e) and len(name) > len(e) for e in r["docTreeExtensions"]):
        if any(s in r["docExcludedSegments"] for s in parts[1:-1]):
            return False
        if name.endswith(".txt") and (name in r["docTxtExcludedNames"]
                                      or any(name.startswith(x) for x in r["docTxtExcludedPrefixes"])):
            return False
        return True
    if len(parts) == 2 and parts[0] in r["licenseTreeRoots"] and \
            any(name.endswith(e) and len(name) > len(e) for e in r["licenseTreeSuffixes"]):
        return True
    return False


#: (path, expected) pairs. Each is a claim the packet makes about what becomes
#: sendable and what stays withheld; the selftest checks them and mutates the
#: rule to be sure they can fail. Non-ASCII characters are written as escapes.
FIXTURES = [
    ("README.md", True), ("readme", True), ("ReadMe.Md", True), ("README.MD", True), ("README", True),
    ("CHANGELOG.md", True), ("CHANGES.txt", True), ("00-RELEASENOTES", True), ("RELEASE-NOTES.rst", True),
    ("CONTRIBUTING.md", True), ("LICENSE", True), ("LICENSE.txt", True), ("Licence.md", True),
    ("COPYING", True), ("NOTICE", True), ("NOTICES.txt", True), ("NEWS", True), ("HISTORY.md", True),
    ("AUTHORS", True), ("FAQ.md", True), ("12-README.md", True),
    ("docs/guide.md", True), ("docs/a/b/intro.rst", True), ("Docs/Guide.MD", True), ("doc/usage.txt", True),
    ("docs/notes.txt", True),
    ("licenses/agpl-3.0.txt", True), ("LICENSES/rsal.TXT", True),
    # policy and governance text by ordinary content: withheld at the root (and as directories under docs)
    ("SECURITY.md", False), ("SECURITY", False), ("DESIGN.md", False), ("GOVERNANCE.txt", False),
    ("CODE_OF_CONDUCT.md", False), ("Code-Of-Conduct.md", False), ("ARCHITECTURE.md", False),
    ("MANIFESTO", False), ("MANIFESTO.rst", False),
    ("docs/adr/0001-decision.md", False), ("docs/specs/protocol.md", False), ("docs/governance/policy.md", False),
    ("docs/security/policy.md", False), ("doc/rfc/rfc-1.txt", False), ("docs/a/Design/x.md", False),
    ("docs/policies/p.md", False), ("docs/specification/x.rst", False), ("docs/decisions/d.md", False),
    ("docs/design.md", True), ("docs/spec.md", True),
    # build and tooling .txt files under docs
    ("docs/CMakeLists.txt", False), ("docs/requirements.txt", False), ("docs/requirements-dev.txt", False),
    ("docs/robots.txt", False), ("doc/a/CMakeLists.txt", False), ("docs/CMakeLists.md", True),
    # not mapped: nested and vendored, wrong names or shapes
    ("src/README.md", False), ("deps/lua/README", False), (".github/README.md", False),
    ("TLS.md", False), ("TODO.md", False), ("CODEOWNERS", False),
    ("README.md.bak", False), ("readme.html", False), ("README.md ", False), ("123-README.md", False),
    ("0-README.md", False), ("README.md/x", False), ("docs", False), ("docs/", False), ("docs/conf.py", False),
    ("docs/diagram.png", False), ("docs/.md", False), ("design/overview.md", False), ("api-docs/x.md", False),
    ("licenses/sub/x.txt", False), ("licenses/x.py", False), ("license/x.txt", False),
    ("../README.md", False), ("docs/../README.md", False), ("/README.md", False), ("a//b.md", False),
    # non-ASCII: nothing beyond A-Z is folded, and only ASCII digits make a prefix
    ("٠١-README.md", False), ("١٢-LICENSE", False),
    ("LICENſE", False), ("docs/ſpecs/x.md", True), ("docs/CMAKELISTS.txt", True),
    ("READMEİ.md", False),
]


def documentation_rule() -> dict:
    return {
        "class": "project-documentation",
        "rule": ("the body of an admitted blob whose repository-relative path is matched by exactly one "
                 "of the three path rules below, after every screening step. Matching compares a copy "
                 "of the path with its ASCII letters A-Z folded to a-z and nothing else folded, "
                 "normalized or decoded; the path is carried as admitted. A path with an empty, '.' "
                 "or '..' segment, a backslash or a leading or trailing '/' matches nothing. No "
                 "extractor runs: the class is by path and the body is admitted as whole-blob spans. "
                 "The class is decided by these paths alone: a file's own claim about itself, or a "
                 "directory name outside the three rules, places nothing in it (RFC5-14)"),
        "pathRules": [
            {"id": "root-document",
             "rule": "a path with one segment whose name, after removing rootStemNumericPrefix when it "
                     "is present and then one suffix from documentSuffixes (any that fits), is one of "
                     "rootStems"},
            {"id": "docs-tree",
             "rule": "a path of two or more segments whose first segment is one of docTreeRoots, whose "
                     "name ends with one of docTreeExtensions and is longer than it, none of whose "
                     "directory segments after the first is in docExcludedSegments, and which is not a "
                     "name ending in .txt that equals one of docTxtExcludedNames or starts with one of "
                     "docTxtExcludedPrefixes"},
            {"id": "licenses-tree",
             "rule": "a path of exactly two segments whose first segment is one of licenseTreeRoots and "
                     "whose name ends with one of licenseTreeSuffixes and is longer than it"},
        ],
        "rootStemNumericPrefix": {"digitCount": PREFIX_DIGIT_COUNT, "digits": PREFIX_DIGITS,
                                  "separator": PREFIX_SEPARATOR, "optional": True,
                                  "note": "exactly the ASCII characters listed in digits; no other character, "
                                          "including any Unicode digit, is a digit here"},
        "rootStems": enabled_stems(),
        "documentSuffixes": DOCUMENT_SUFFIXES,
        "docTreeRoots": DOC_TREE_ROOTS,
        "docTreeExtensions": DOC_TREE_EXTENSIONS,
        "docExcludedSegments": DOC_EXCLUDED_SEGMENTS,
        "docTxtExcludedNames": DOC_TXT_EXCLUDED_NAMES,
        "docTxtExcludedPrefixes": DOC_TXT_EXCLUDED_PREFIXES,
        "licenseTreeRoots": LICENSE_TREE_ROOTS,
        "licenseTreeSuffixes": LICENSE_TREE_SUFFIXES,
        "disjointFromSourceExtensions": "none of documentSuffixes, docTreeExtensions or licenseTreeSuffixes is in sourceExtensions, so no blob has two classes by extension; a blob matched here is never code-content",
        "notMapped": ("nested and vendored documentation (a README below the root outside docs-tree), "
                      "specification, design, decision and policy text, which this policy leaves unmapped "
                      "by its own choice (root files named design, governance, security or code of conduct, "
                      "and docs-tree paths under a directory in docExcludedSegments), build and tooling "
                      ".txt files named in docTxtExcludedNames or docTxtExcludedPrefixes, committed "
                      "reports, and any other prose: they stay indeterminate"),
    }


INDETERMINATE = (
    "every other admitted blob, including documentation outside the project-documentation rule's paths "
    "(for example a README below the root), specification, design, decision and policy documents (this "
    "policy leaves them unmapped), committed reports, "
    "and configuration or data in an extension outside sourceExtensions, is indeterminate and is treated "
    "as unclassifiable under unclassifiableExclusion: excluded from reading and from egress (fail "
    "closed), recorded hash-not-body, and never stored or rendered. Its path, object id and size remain "
    "code-structure"
)

PREREQUISITE = {
    "requires": "the RFC-0005 amendment that defines the class project-documentation in the closed vocabulary of RFC5-14",
    "rule": ("the project-documentation rule classifies a blob only while the in-force RFC-0005 "
             "vocabulary lists project-documentation; a consumer that cannot confirm that treats every "
             "blob the rule names as indeterminate, and the rest of this scope is unchanged"),
    "consentRule": ("a consent record that does not list project-documentation does not permit its "
                    "egress, and no consent granted before the class existed is read as covering it "
                    "(RFC5-14 as amended); this policy confers no consent"),
}


def v2_scope(scope1: dict) -> dict:
    """Version 2 of the scope object, derived from version 1's: four keys change or are added."""
    s = copy.deepcopy(scope1)
    cc = s["contentClassification"]
    cc["classesClassified"] = list(V2_CLASSES)
    rules = cc["rules"]
    at = next(i for i, r in enumerate(rules) if r["class"] == "code-content") + 1
    rules.insert(at, documentation_rule())
    cc["indeterminate"] = INDETERMINATE
    s["prerequisite"] = copy.deepcopy(PREREQUISITE)
    return s


def bump_minor(version: str) -> str:
    return v1.bump_minor(version)


def reverse_patch(patch_text: str, new_text: str) -> str:
    with tempfile.TemporaryDirectory() as d:
        target = pathlib.Path(d) / POLICY
        target.parent.mkdir(parents=True)
        target.write_text(new_text)
        done = subprocess.run(["patch", "-R", "-p1", "--no-backup-if-mismatch", "-s"],
                              cwd=d, input=patch_text, text=True, capture_output=True)
        if done.returncode != 0:
            raise ValueError("patch does not reverse: " + (done.stdout + done.stderr).strip()[:200])
        return target.read_text()


def v1_bytes(base_text: str, root: pathlib.Path = ROOT) -> tuple[str, str]:
    """(version-1 proposed bytes, mode). mode is 'prospective' when the policy on disk is the
    pre-version-1 policy, 'performed' when it already is the version-1 bytes, and 'performed-v2'
    when it already is THIS package's proposed bytes (the version-1 bytes are then recovered by
    reversing the patch and must hash to the version-1 manifest row)."""
    row = re.search(r"^([0-9a-f]{64})  ", (root / V1_MANIFEST).read_text(), re.M)
    if not row:
        raise ValueError("the version-1 manifest has no row")
    disk = hashlib.sha256(base_text.encode()).hexdigest()
    if SCOPE_KEY in json.loads(base_text):
        if disk == row.group(1):
            return base_text, "performed"
        own = re.search(r"^([0-9a-f]{64})  ", (root / MANIFEST).read_text(), re.M) if (root / MANIFEST).is_file() else None
        if own and disk == own.group(1) and (root / PATCH).is_file():
            back = reverse_patch((root / PATCH).read_text(), base_text)
            if hashlib.sha256(back.encode()).hexdigest() != row.group(1):
                raise ValueError("reversing the patch over the policy on disk does not give the version-1 bytes")
            return back, "performed-v2"
        raise ValueError("the policy on disk carries publicSourceScope but is neither the version-1 bytes nor "
                         "this package's proposed bytes (its hash is in neither manifest); the base is unknown")
    proposed = v1.propose(base_text)
    if hashlib.sha256(proposed.encode()).hexdigest() != row.group(1):
        raise ValueError("the version-1 proposal over the policy on disk does not hash to the version-1 "
                         "manifest row: the version-1 package is stale against this policy")
    return proposed, "prospective"


def dump(doc: dict) -> str:
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


def block(scope: dict) -> str:
    return '  "' + SCOPE_KEY + '": ' + json.dumps(scope, indent=2, ensure_ascii=False).replace("\n", "\n  ") + ",\n"


def propose(base1_text: str) -> str:
    """Text replacement of the one scope block and the version line, so every other
    byte of the version-1 policy is preserved."""
    base = json.loads(base1_text)
    old = block(base[SCOPE_KEY])
    if base1_text.count(old) != 1:
        raise ValueError("the version-1 scope block is not found exactly once in its own bytes")
    version = f'  "policyVersion": "{base["policyVersion"]}",\n'
    if base1_text.count(version) != 1:
        raise ValueError("policyVersion line not found exactly once")
    out = base1_text.replace(old, block(v2_scope(base[SCOPE_KEY])), 1)
    out = out.replace(version, f'  "policyVersion": "{bump_minor(base["policyVersion"])}",\n', 1)
    got = json.loads(out)
    expected = dict(base)
    expected["policyVersion"] = bump_minor(base["policyVersion"])
    expected[SCOPE_KEY] = v2_scope(base[SCOPE_KEY])
    if got != expected or list(got) != list(base):
        raise ValueError("text replacement changed something other than the scope block and policyVersion")
    return out


def unified(base_text: str, new_text: str) -> str:
    return "".join(difflib.unified_diff(
        base_text.splitlines(True), new_text.splitlines(True),
        f"a/{POLICY.as_posix()}", f"b/{POLICY.as_posix()}", n=1))


def manifest_text(proposed: str) -> str:
    return ("# PUBLIC-SOURCE SCREENING SCOPE VERSION 2 MANIFEST\n"
            "# Candidate; this file and its row bind nothing by themselves.\n"
            "# 1 artifact; the row hashes the PROPOSED bytes (the version-1 policy with\n"
            "# proposed/<name>.patch applied) and is the argument of one superseding\n"
            "# approve-policy act over that subject.\n"
            f"{hashlib.sha256(proposed.encode()).hexdigest()}  {POLICY.as_posix()}\n")


def semantic_findings(base1_text: str, proposed_text: str) -> list[str]:
    """Structural claims the packet makes; each is mutated in --selftest."""
    base, new = json.loads(base1_text), json.loads(proposed_text)
    bad: list[str] = []
    if new.get("policyVersion") != bump_minor(base["policyVersion"]):
        bad.append("policyVersion is not the next minor")
    if {k: v for k, v in new.items() if k not in (SCOPE_KEY, "policyVersion")} != {
            k: v for k, v in base.items() if k not in (SCOPE_KEY, "policyVersion")}:
        bad.append("a key other than policyVersion and the scope differs from version 1")
    s1, s2 = base[SCOPE_KEY], new.get(SCOPE_KEY)
    if not isinstance(s2, dict):
        return bad + ["publicSourceScope missing"]
    # only four things move in the scope: the class list, the rules, the indeterminate reading, the prerequisite
    moved = {k for k in set(s1) | set(s2) if s1.get(k) != s2.get(k)}
    if moved != {"contentClassification", "prerequisite"}:
        bad.append(f"scope keys changed beyond contentClassification and prerequisite: {sorted(moved)}")
    c1, c2 = s1["contentClassification"], s2.get("contentClassification", {})
    if {k for k in set(c1) | set(c2) if c1.get(k) != c2.get(k)} != {"classesClassified", "rules", "indeterminate"}:
        bad.append("contentClassification changed beyond classesClassified, rules and indeterminate")
    if c2.get("classesClassified") != list(V2_CLASSES):
        bad.append("classesClassified is not exactly version 1's plus project-documentation")
    if "work-history" in c2.get("classesClassified", []) or c2.get("neverClassified") != ["work-history"]:
        bad.append("work-history is classified or no longer never-classified")
    if c2.get("governanceTextPaths") or c2.get("evidenceContentPaths"):
        bad.append("governance-text or evidence-content path rules are non-empty in this version")
    others1 = [r for r in c1["rules"]]
    others2 = [r for r in c2.get("rules", []) if r.get("class") != "project-documentation"]
    if others1 != others2:
        bad.append("a rule other than project-documentation differs from version 1")
    docs = [r for r in c2.get("rules", []) if r.get("class") == "project-documentation"]
    if len(docs) != 1 or docs[0] != documentation_rule():
        bad.append("the project-documentation rule is not exactly the declared one")
    else:
        d = docs[0]
        src = next(r for r in c2["rules"] if r["class"] == "code-content")["sourceExtensions"]
        if set(d["documentSuffixes"]) & set(src) or set(d["docTreeExtensions"]) & set(src) \
                or set(d["licenseTreeSuffixes"]) & set(src):
            bad.append("a documentation extension is also a source extension")
        for path, want in FIXTURES:
            if classify_documentation(path, d) != want:
                bad.append(f"fixture {path!r}: expected {want}")
    if "excluded from reading and from egress" not in c2.get("indeterminate", ""):
        bad.append("indeterminate does not state the one fail-closed reading")
    if s2.get("prerequisite") != PREREQUISITE:
        bad.append("prerequisite is not exactly the declared one")
    for key in ("detectors", "activeContent", "accessBoundary", "rawBodyHandling", "inheritedRules", "selfReferenceRule"):
        if s2.get(key) != s1.get(key):
            bad.append(f"{key} differs from version 1")
    return bad


def check(root: pathlib.Path = ROOT) -> list[str]:
    findings: list[str] = []
    try:
        base1, mode = v1_bytes((root / POLICY).read_text(), root)
        proposed = propose(base1)
    except ValueError as exc:
        return [str(exc)]
    expected_patch = unified(base1, proposed)
    patch_path, manifest_path = root / PATCH, root / MANIFEST
    if not patch_path.is_file() or patch_path.read_text() != expected_patch:
        findings.append("patch differs from its regeneration over the version-1 bytes")
    else:
        try:
            if v1.apply_patch(root, base1, patch_path.read_text()) != proposed:
                findings.append("applying the patch does not yield the proposed bytes")
        except ValueError as exc:
            findings.append(str(exc))
    if not manifest_path.is_file() or manifest_path.read_text() != manifest_text(proposed):
        findings.append("manifest differs from its regeneration")
    present = sorted(p.name for p in (root / PKG / "proposed").glob("*")) if (root / PKG / "proposed").is_dir() else []
    if present != [PATCH.name]:
        findings.append(f"proposed/ holds {present}, not exactly the declared patch")
    findings += semantic_findings(base1, proposed)
    if (root / PACKET).is_file():
        spliced = splice_packet((root / PACKET).read_text())
        if spliced is None:
            findings.append("packet lacks its single generated-lists block")
        elif spliced != (root / PACKET).read_text():
            findings.append("packet's generated lists differ from the rule's constants")
    for md in sorted((root / PKG).glob("*.md")):
        if re.search(r"(?<![0-9a-fA-F])[0-9a-f]{64}(?![0-9a-fA-F])", md.read_text()):
            findings.append(f"{md.name}: carries a 64-hex token; the argument comes only from the manifest row")
    return findings


PACKET = PKG / "OWNER-DECISION-PACKET.md"
BEGIN, END = "<!-- BEGIN GENERATED: lists -->", "<!-- END GENERATED: lists -->"


def packet_block() -> str:
    """The sendable and withheld lists, generated from the rule's constants so the packet cannot
    drift from the policy bytes."""
    r = documentation_rule()
    up = lambda xs: ", ".join(x.upper() for x in xs)
    names = ", ".join(x.upper() for x in r["rootStems"])
    off = [k for k in OPT_IN_STEMS if k not in ENABLED_OPT_INS]
    on = list(ENABLED_OPT_INS)
    return "\n".join([
        "**Becomes readable** (and, under a consent that lists the class and a separate egress consent, sendable):",
        "",
        f"- Root-level files named {names} (any letter case; an optional prefix of two ASCII digits and a "
        f"hyphen, so 00-RELEASENOTES counts; no extension or one of {', '.join(r['documentSuffixes'][1:])}).",
        f"- Files ending {', '.join(r['docTreeExtensions'])} under a top-level {' or '.join(r['docTreeRoots'])} folder, at any "
        f"depth, except under a directory named {', '.join(r['docExcludedSegments'])}, and except .txt files named "
        f"{', '.join(r['docTxtExcludedNames'])} or starting {', '.join(r['docTxtExcludedPrefixes'])}.",
        f"- Files ending {', '.join(r['licenseTreeSuffixes'])} directly inside a top-level {' or '.join(r['licenseTreeRoots'])} folder.",
        f"- Owner opt-ins, currently ON: {up(on) or 'none'}; currently OFF: {up(off) or 'none'}.",
        "",
        "**Stays withheld** (excluded from reading and from egress, hash-not-body):",
        "",
        "- Root files named DESIGN, GOVERNANCE, SECURITY, CODE_OF_CONDUCT or CODE-OF-CONDUCT, "
        "and the opt-in names above while they are off.",
        f"- Anything under a docs or doc directory named {', '.join(r['docExcludedSegments'])}.",
        f"- {', '.join(r['docTxtExcludedNames'])} and requirements*.txt files under docs or doc.",
        "- READMEs and the other root names when they sit below the root outside docs or doc "
        "(vendored libraries carry their own), and a design directory.",
        "- Specification, decision, policy and report text, and any other prose.",
        "- Any file that fails a secret detector or the active-content rule: those screens are unchanged "
        "and apply to this prose in full.",
        "- Everything, while the RFC-0005 amendment of PR #257 is not in force.",
    ])


def splice_packet(text: str) -> str | None:
    if text.count(BEGIN) != 1 or text.count(END) != 1 or text.index(BEGIN) > text.index(END):
        return None
    a, b = text.index(BEGIN) + len(BEGIN), text.index(END)
    return text[:a] + "\n" + packet_block() + "\n" + text[b:]


def readiness(root: pathlib.Path = ROOT) -> list[str]:
    """What an act needs beyond byte currency."""
    out: list[str] = []
    rfc = root / RFC5_INSTALLED
    if not rfc.is_file() or RFC5_CLASS_ROW not in rfc.read_text():
        out.append("the class project-documentation is not defined in the installed RFC-0005 text "
                   "(the PR 257 amendment is not applied)")
    if not (root / V1_ACT).is_file():
        out.append("the version-1 screening-scope act is not recorded, so the base is still prospective")
    return out


def write(root: pathlib.Path = ROOT) -> None:
    base1, _mode = v1_bytes((root / POLICY).read_text(), root)
    proposed = propose(base1)
    (root / PATCH).parent.mkdir(parents=True, exist_ok=True)
    (root / PATCH).write_text(unified(base1, proposed))
    (root / MANIFEST).write_text(manifest_text(proposed))
    if (root / PACKET).is_file():
        spliced = splice_packet((root / PACKET).read_text())
        if spliced is None:
            raise ValueError("packet lacks its single generated-lists block")
        (root / PACKET).write_text(spliced)


def selftest() -> int:
    results: list[tuple[str, bool]] = []
    with tempfile.TemporaryDirectory() as d:
        scratch = pathlib.Path(d)
        for rel in (POLICY, V1_MANIFEST):
            (scratch / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(ROOT / rel, scratch / rel)
        (scratch / PACKET).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(ROOT / PACKET, scratch / PACKET)
        write(scratch)
        results.append(("pristine package checks clean", check(scratch) == []))

        def mutate(name: str, fn, needle: str) -> None:
            snap = {p: p.read_bytes() for p in (scratch / PKG).rglob("*") if p.is_file()}
            policy = (scratch / POLICY).read_bytes()
            v1m = (scratch / V1_MANIFEST).read_bytes()
            try:
                fn()
                results.append((name, any(needle in f for f in check(scratch))))
            finally:
                (scratch / POLICY).write_bytes(policy)
                (scratch / V1_MANIFEST).write_bytes(v1m)
                for p in (scratch / PKG).rglob("*"):
                    if p.is_file() and p not in snap:
                        p.unlink()
                for p, b in snap.items():
                    p.write_bytes(b)

        mutate("a one-byte patch edit is caught",
               lambda: (scratch / PATCH).write_text((scratch / PATCH).read_text().replace('"rootStems"', '"rootStemS"', 1)),
               "patch differs")

        def flip_manifest():
            row = (scratch / MANIFEST).read_text().splitlines(True)
            row[-1] = ("0" if row[-1][0] != "0" else "1") + row[-1][1:]
            (scratch / MANIFEST).write_text("".join(row))
        mutate("a one-character manifest digest edit is caught", flip_manifest, "manifest differs")
        mutate("a policy that moved under the package is caught",
               lambda: (scratch / POLICY).write_text((scratch / POLICY).read_text().replace(
                   '"schemaVersion": 1', '"schemaVersion": 1,\n  "note": "x"', 1)),
               "version-1")
        mutate("a version-1 manifest that moved is caught",
               lambda: (scratch / V1_MANIFEST).write_text((scratch / V1_MANIFEST).read_text().replace("0", "1", 1)
                                                         if "0" in (scratch / V1_MANIFEST).read_text().split("\n")[-2][:64] else
                                                         (scratch / V1_MANIFEST).read_text().replace("1", "2", 1)),
               "version-1")
        mutate("an extra file under proposed/ is caught",
               lambda: (scratch / PKG / "proposed" / "extra.patch").write_text("x"), "proposed/ holds")
        mutate("a packet list edited by hand is caught",
               lambda: (scratch / PACKET).write_text((scratch / PACKET).read_text().replace("DESIGN, GOVERNANCE", "GOVERNANCE", 1)),
               "generated lists differ")
        mutate("a packet without the generated block is caught",
               lambda: (scratch / PACKET).write_text((scratch / PACKET).read_text().replace(BEGIN, "", 1)),
               "lacks its single generated-lists block")
        mutate("a 64-hex token in package prose is caught",
               lambda: (scratch / PKG / "X.md").write_text("a" * 64), "64-hex")

        # the performed base gives the same package as the prospective one
        base0 = (ROOT / POLICY).read_text()
        v1text = v1.propose(base0)
        with tempfile.TemporaryDirectory() as d2:
            r2 = pathlib.Path(d2)
            for rel in (V1_MANIFEST,):
                (r2 / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(ROOT / rel, r2 / rel)
            (r2 / POLICY).parent.mkdir(parents=True, exist_ok=True)
            (r2 / POLICY).write_text(v1text)
            write(r2)
            results.append(("a performed base yields the same patch and manifest as a prospective one",
                            (r2 / PATCH).read_text() == (scratch / PATCH).read_text()
                            and (r2 / MANIFEST).read_text() == (scratch / MANIFEST).read_text()))
            results.append(("a performed base checks clean", check(r2) == []))
            (r2 / POLICY).write_text(v1text.replace('"schemaVersion": 1', '"schemaVersion": 1,\n  "note": "x"', 1))
            results.append(("a policy with a scope that is not the version-1 bytes is refused",
                            any("neither" in f for f in check(r2))))

        proposed = propose(v1text)

        def sem(name, fn, needle):
            doc = json.loads(proposed)
            fn(doc)
            results.append((name, any(needle in f for f in semantic_findings(v1text, dump(doc)))))

        S = SCOPE_KEY
        sem("work-history classified is caught", lambda x: x[S]["contentClassification"]["classesClassified"].append("work-history"), "work-history")
        sem("a class beyond project-documentation is caught", lambda x: x[S]["contentClassification"]["classesClassified"].append("governance-text"), "classesClassified")
        sem("a governance-text path rule is caught", lambda x: x[S]["contentClassification"].update(governanceTextPaths=["docs/**"]), "non-empty")
        sem("an evidence-content path rule is caught", lambda x: x[S]["contentClassification"].update(evidenceContentPaths=["reports/**"]), "non-empty")
        sem("a changed code-content rule is caught",
            lambda x: next(r for r in x[S]["contentClassification"]["rules"] if r["class"] == "code-content")["sourceExtensions"].append(".md"), "other than project-documentation")
        sem("a doc extension that is also a source extension is caught",
            lambda x: next(r for r in x[S]["contentClassification"]["rules"] if r["class"] == "code-content")["sourceExtensions"].append(".txt"), "also a source extension")
        sem("a changed documentation rule is caught",
            lambda x: next(r for r in x[S]["contentClassification"]["rules"] if r["class"] == "project-documentation")["docTreeRoots"].append("design"), "declared one")
        sem("a widened numeric prefix is caught",
            lambda x: next(r for r in x[S]["contentClassification"]["rules"] if r["class"] == "project-documentation").update(rootStemNumericPrefix={"digitCount": 2, "digits": "0123456789\u0660", "separator": "-", "optional": True, "note": "x"}), "declared one")
        sem("a dropped prerequisite is caught", lambda x: x[S].pop("prerequisite"), "prerequisite")
        sem("a weakened prerequisite is caught", lambda x: x[S]["prerequisite"].update(rule="always"), "prerequisite")
        sem("the fail-closed indeterminate reading dropped is caught", lambda x: x[S]["contentClassification"].update(indeterminate="refused"), "indeterminate")
        sem("active content loosened is caught", lambda x: x[S]["activeContent"].update(rule="no check"), "activeContent")
        sem("detectors loosened is caught", lambda x: x[S].update(detectors="relaxed"), "detectors")
        sem("a boundary opened is caught", lambda x: x[S]["accessBoundary"].update(workingTree=True), "accessBoundary")
        sem("raw body handling opened is caught", lambda x: x[S]["rawBodyHandling"].update(logging="run"), "rawBodyHandling")
        sem("a scope key added is caught", lambda x: x[S].update(extra=1), "beyond contentClassification")
        sem("a base key altered is caught", lambda x: x.update(detectorsNote="x") or x["rawBodyHandling"].update(logging="run"), "differs from version 1")
        sem("version not bumped is caught", lambda x: x.update(policyVersion=json.loads(v1text)["policyVersion"]), "next minor")

        # the rule oracle: every fixture holds, and each rule component can be made to fail
        rule = documentation_rule()
        results.append(("every path fixture holds", all(classify_documentation(p, rule) == w for p, w in FIXTURES)))
        results.append(("fixtures cover both outcomes", {w for _p, w in FIXTURES} == {True, False}))

        def broken(**over):
            r = copy.deepcopy(rule)
            r.update(over)
            return r
        for label, bad_rule in (
                ("a rule without ASCII folding is caught by the mixed-case fixtures", None),
                ("a widened root stem list is caught", broken(rootStems=ROOT_STEMS + ["todo"])),
                ("a widened document suffix list is caught", broken(documentSuffixes=DOCUMENT_SUFFIXES + [".html"])),
                ("a widened docs tree is caught", broken(docTreeRoots=DOC_TREE_ROOTS + ["design"])),
                ("a widened docs extension list is caught", broken(docTreeExtensions=DOC_TREE_EXTENSIONS + [".png"])),
                ("a second licences tree root is caught", broken(licenseTreeRoots=LICENSE_TREE_ROOTS + ["license"])),
                ("a narrowed stem list is caught", broken(rootStems=ROOT_STEMS[1:])),
                ("a dropped numeric prefix is caught", broken(rootStemNumericPrefix=dict(rule["rootStemNumericPrefix"], digitCount=9))),
                ("a security root name added is caught", broken(rootStems=enabled_stems() + ["security"])),
                ("a manifesto opt-in turned on is caught", broken(rootStems=enabled_stems() + ["manifesto"])),
                ("an architecture opt-in turned on is caught", broken(rootStems=enabled_stems() + ["architecture"])),
                ("an emptied excluded-segment list is caught", broken(docExcludedSegments=[])),
                ("a dropped governance exclusion is caught", broken(docExcludedSegments=[x for x in DOC_EXCLUDED_SEGMENTS if x != "governance"])),
                ("an emptied txt name denylist is caught", broken(docTxtExcludedNames=[])),
                ("an emptied txt prefix denylist is caught", broken(docTxtExcludedPrefixes=[]))):
            if bad_rule is None and label.startswith("a rule without"):
                orig = ascii_fold
                try:
                    globals()["ascii_fold"] = lambda p: p
                    caught = any(classify_documentation(p, rule) != w for p, w in FIXTURES)
                finally:
                    globals()["ascii_fold"] = orig
            else:
                caught = any(classify_documentation(p, bad_rule) != w for p, w in FIXTURES)
            results.append((label, caught))

        def swapped(name, fn):
            orig = globals()[name]
            try:
                globals()[name] = fn
                return any(classify_documentation(p, rule) != w for p, w in FIXTURES)
            finally:
                globals()[name] = orig
        results.append(("str.lower in place of the ASCII fold is caught (Kelvin sign)", swapped("ascii_fold", str.lower)))
        results.append(("str.casefold in place of the ASCII fold is caught (long s)", swapped("ascii_fold", str.casefold)))
        results.append(("a Unicode-aware digit test in the prefix is caught", swapped(
            "has_numeric_prefix", lambda name, r: len(name) > 2 and name[:2].isdigit() and name[2] == "-")))

        # readiness: the prerequisite, met and unmet, at the real installed path
        with tempfile.TemporaryDirectory() as d3:
            r3 = pathlib.Path(d3)
            (r3 / RFC5_INSTALLED).parent.mkdir(parents=True)
            (r3 / V1_ACT).parent.mkdir(parents=True, exist_ok=True)
            (r3 / RFC5_INSTALLED).write_text("# RFC-0005\n" + RFC5_CLASS_ROW + " defined |\n")
            (r3 / V1_ACT).write_text("act\n")
            results.append(("readiness is empty with the class installed and the v1 act recorded", readiness(r3) == []))
            (r3 / RFC5_INSTALLED).write_text("# RFC-0005\n")
            results.append(("readiness names the missing class", any("not defined" in f for f in readiness(r3))))
            (r3 / RFC5_INSTALLED).write_text("# RFC-0005\n" + RFC5_CLASS_ROW + " defined |\n")
            (r3 / V1_ACT).unlink()
            results.append(("readiness names the missing v1 act", any("version-1" in f for f in readiness(r3))))
            (r3 / V1_ACT).write_text("act\n")
            (r3 / RFC5_INSTALLED).unlink()
            results.append(("readiness refuses when the installed RFC file is absent", any("not defined" in f for f in readiness(r3))))
        results.append(("the real installed RFC-0005 path exists", (ROOT / RFC5_INSTALLED).is_file()))

        # the policy after this package's own act: the base is recovered by reversing the patch
        with tempfile.TemporaryDirectory() as d4:
            r4 = pathlib.Path(d4)
            for rel in (V1_MANIFEST, MANIFEST, PATCH, PACKET):
                (r4 / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(scratch / rel if rel in (MANIFEST, PATCH, PACKET) else ROOT / rel, r4 / rel)
            (r4 / POLICY).parent.mkdir(parents=True, exist_ok=True)
            (r4 / POLICY).write_text(proposed)
            results.append(("after this package's act, --check is still current (performed-v2)", check(r4) == []))
            (r4 / POLICY).write_text(proposed.replace('"schemaVersion": 1', '"schemaVersion": 1,\n  "note": "x"', 1))
            results.append(("after the act, a policy that is neither manifest row is refused", any("neither" in f for f in check(r4))))
    failed = [n for n, ok in results if not ok]
    for n, ok in results:
        print(("ok   " if ok else "FAIL ") + n)
    print(f"selftest: {len(results) - len(failed)} of {len(results)} predicates held")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    mode = argv[1] if len(argv) > 1 else "--check"
    pending = "--pending-prerequisite" in argv[2:]
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
        if readiness() and not pending:
            print("refusing:", readiness()[0], "(--pending-prerequisite prints the digest of a package not yet ready)", file=sys.stderr)
            return 1
        print(hashlib.sha256((ROOT / MANIFEST).read_bytes()).hexdigest())
        return 0
    if mode in ("--check", "--ready"):
        findings = check()
        for f in findings:
            print("FINDING", f)
        print("public-source screening scope v2:", "STALE" if findings else "current")
        if mode == "--ready":
            need = readiness()
            for f in need:
                print("NOTE" if pending else "FINDING", f)
            return 1 if findings or (need and not pending) else 0
        return 1 if findings else 0
    print(f"unknown mode {mode}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
