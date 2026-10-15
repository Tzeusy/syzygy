#!/usr/bin/env python3
"""Build and verify the inert public-source screening-scope version-4 package.

Package `contracts/candidates/public-source-screening-scope-v4/` (`syzygy-olmr`:
whole-blob secret screening and a narrow root-document list withhold most of a
target's maintainer documentation from the fidelity packet). This script
performs no owner act and writes no act record.

Version 3 (`contracts/candidates/public-source-screening-scope-v3/`, variant
all, approved 2026-10-08) keeps the version-1 sentence that "a match excludes
the whole artifact with hash-not-body provenance". Version 4 retains a body a
single-line detector matches as RFC5-17's `redacted-span` instead: the lines a
match touches, and one guard line on each side, are withheld; a cited span
that includes a withheld line is withheld whole; every detector runs again over
what is retained, and any match there excludes the body whole. A
`private-key-material` match still excludes the body whole, because that
detector matches only a key's header line and the key itself follows it.

Two variants, one manifest row each:

- `span`: the redaction rule only;
- `span-guides`: the redaction rule, and the root-document path rule also
  admits a closed list of root guide names (`rootGuideStems`), only with a
  non-empty suffix from `rootGuideSuffixes`.

Values that change inside `publicSourceScope`: `detectors` (one clause
appended), `inheritedRules` (one phrase replaced), the new object
`secretRedaction`, and, in `span-guides` only, the project-documentation rule's
root-document text, `notMapped` text, and two new lists. `policyVersion` moves
to the next minor with the variant appended. Nothing else may change.

The subject is the policy AFTER version 3: the bytes of the version-3 manifest
row `all`. The builder takes the policy on disk when it hashes to that row, or
recovers it by reversing this package's own patch when the disk is one of this
package's rows (the state after a version-4 act).

  --write             regenerate the patches and the manifest
  --check             verify the package against the policy on disk
  --digests           print the manifest rows (refuses while stale)
  --manifest-digest   print the SHA-256 of the manifest FILE (refuses while stale)
  --selftest          mutate each predicate; each must fail

Review-head contract for a recorder written after a confirming review: the
raw's first four non-blank lines carry `Reviewed commit: <40 hex>`,
`Manifest SHA-256: <SHA-256 of the manifest FILE>` and a `Verdict:` line
(`CONFIRM` or `CONFIRM WITH EXCEPTIONS`).
"""

from __future__ import annotations

import copy
import hashlib
import json
import pathlib
import re
import shutil
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_public_source_screening_scope_v2 as v2  # noqa: E402
import build_public_source_screening_scope_v3 as v3  # noqa: E402

POLICY = v2.POLICY
SCOPE_KEY = v2.SCOPE_KEY
PKG = pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v4")
MANIFEST = PKG / "PUBLIC-SOURCE-SCREENING-SCOPE-V4-MANIFEST.txt"
V3_BASE_VARIANT = "all"
VARIANTS = ("span", "span-guides")

#: Detectors whose match does not hold the secret it signals: a key's material follows its header line,
#: and an AWS access-key id (AKIA...) is paired with a secret key no detector matches (round 1, finding 1).
WHOLE_ARTIFACT_DETECTORS = ["private-key-material", "known-token-formats"]
#: A body holding any of these anywhere is never retained as redacted-span: a PEM block whose header the
#: private-key literals do not list (an EC key, for example) is key material no detector matches (finding 3).
WHOLE_ARTIFACT_FRAGMENTS = ["-----BEGIN "]
GUARD_LINES = 1

#: Root prose names RFC5-14's own list covers (guides, tutorials, how-to and overview documents,
#: contribution and credit files). Deliberately absent: security, manifesto, architecture, design,
#: governance, conduct, roadmap, maintainers, agents, claude (governance-text or owner-declined in
#: version 2), build (a Bazel build file), and any single project's topic name.
ROOT_GUIDE_STEMS = [
    "install", "installing", "installation", "building", "hacking", "development", "developing",
    "usage", "tutorial", "overview", "getting-started", "getting_started", "gettingstarted",
    "upgrading", "migrating", "migration", "troubleshooting", "support",
    "contributors", "credits", "thanks", "acknowledgments", "acknowledgements",
]
ROOT_GUIDE_SUFFIXES = [".md", ".rst", ".txt"]
FORBIDDEN_GUIDE_STEMS = {"security", "manifesto", "manifestos", "architecture", "design", "governance",
                         "code_of_conduct", "code-of-conduct", "conduct", "policy", "build", "roadmap",
                         "maintainers", "codeowners", "agents", "claude", "tls"}

DETECTORS_OLD = "a match excludes the whole artifact with hash-not-body provenance (matchAction, RFC5-17)"
DETECTORS_NEW = (DETECTORS_OLD + ", except where secretRedaction retains a body as redacted-span; every detector "
                 "still runs over the complete body first")
INHERITED_OLD = "detectors, matchAction, unclassifiableExclusion, redactionClasses,"
INHERITED_NEW = ("detectors, matchAction and redactionClasses (except that secretRedaction retains a body of an "
                 "admitted snapshot as redacted-span where its rule says so, and for such a body reads the detector "
                 "condition of classificationSuccess as no detector matching its retained text), "
                 "unclassifiableExclusion,")

REDACTION = {
    "appliesTo": (
        "a body of an admitted snapshot whose path this scope admits (code-content or project-documentation), "
        "after the denied-path, strict-UTF-8, NUL and resource-limit rules pass. Text an agent session writes (a "
        "draft, an inventory, a verdict, a finding) is not such a body and is screened as before"),
    "redactionClass": "redacted-span",
    "wholeArtifactDetectors": WHOLE_ARTIFACT_DETECTORS,
    "wholeArtifactFragments": WHOLE_ARTIFACT_FRAGMENTS,
    "guardLines": GUARD_LINES,
    "rule": (
        "every detector runs over the complete transient body exactly as before, including inert code contexts. "
        "Here a detector's matches are every match it makes starting at any offset of the text, overlapping "
        "matches included, not only those a left-to-right non-overlapping scan reports. When at least one "
        "detector matches, none of the matches is from a detector in wholeArtifactDetectors, and the body holds "
        "none of wholeArtifactFragments (compared exactly, case-sensitively), the body is retained as "
        "redacted-span (RFC5-17) instead of excluded whole. Lines are split at LF, CRLF "
        "or CR, as the generator counts lines; a match touches every line that holds any of its characters. A "
        "line a match touches, and guardLines lines before and after it, is a withheld line. Every detector then "
        "runs again over the retained text, which is the body with each withheld line replaced by an empty line "
        "of the same terminator; a match there excludes the whole artifact as excluded-artifact. A body with a "
        "match from a detector in wholeArtifactDetectors, a body holding one of wholeArtifactFragments, and a body "
        "with a match the consumer cannot place on lines, is excluded whole as before"),
    "withheldLines": (
        "a withheld line is never stored, logged, rendered, sent, quoted, used to verify a quotation, or given to "
        "an agent session, and no digest of a withheld line, or of any part of one, is recorded. Wherever the "
        "retained body is shown or carried, each run of consecutive withheld lines is replaced by one marker that "
        "names the redaction and the total count of withheld lines in the body. The whole body's content digest "
        "and its Git object id remain recorded (RFC5-17 requires the digest), so a guess at short withheld lines "
        "can be checked against them; the target being public does not lift this residual"),
    "citedSpanRule": (
        "a cited span (a start line and an end line of the body) that includes a withheld line is withheld whole, "
        "never shown in part, and every claim that depends on it renders Unknown with reason excluded-content "
        "(RFC5-17). A cited span that includes no withheld line is screening-admitted content of the body's class "
        "and is carried with the body's redaction count disclosed beside it; its own text is screened by every "
        "detector before it is carried, and a match withholds it"),
    "provenance": (
        "the retained body's exclusion record is hash-not-body: the content digest of the complete body, its "
        "repository-relative path, policyId, policyVersion, the redaction class redacted-span, the id of each "
        "detector that matched, and the numbers of the withheld lines"),
    "unchanged": (
        "the active-content scan, its malformed-code-context exclusion and activeContent.codeContentExemption run "
        "over the complete body exactly as before, and an active-content finding excludes the body whole; the "
        "content classes, the consent and egress rules and rawBodyHandling are unchanged; a withheld line changes "
        "no class"),
    "consequence": (
        "[Inferred] a body whose only detector matches are credential-assignment or credential-bearing-url forms "
        "(a token in a badge URL, a placeholder password in an example) keeps every line outside the matched "
        "lines and their guards; the trial of 2026-10-14 withheld all 41 cited spans of one README for one match "
        "on its first line. The cost: a body with a match is evidence that the file carries credentials, and "
        "whole-blob screening withheld everything in it; under this rule a secret in such a body that no "
        "detector matches (one beyond the guard line, or one continuing past it) is admitted"),
}

ROOT_RULE_OLD = ("a path with one segment whose name, after removing rootStemNumericPrefix when it is present and then "
                 "one suffix from documentSuffixes (any that fits), is one of rootStems")
ROOT_RULE_NEW = (ROOT_RULE_OLD + ", or, when the suffix removed is one of rootGuideSuffixes, one of rootGuideStems")
NOT_MAPPED_OLD = "root files named design, governance, security or code of conduct;"
NOT_MAPPED_NEW = ("root files named design, governance, security, code of conduct, manifesto or architecture; a "
                  "rootGuideStems name with no suffix;")


def patch_path(variant: str) -> pathlib.Path:
    return PKG / "proposed" / f"{POLICY.name}.{variant}.patch"


def doc_rule(scope: dict) -> dict:
    return next(r for r in scope["contentClassification"]["rules"] if r["class"] == "project-documentation")


def v4_scope(scope3: dict, variant: str) -> dict:
    s = copy.deepcopy(scope3)
    for key, old, new in (("detectors", DETECTORS_OLD, DETECTORS_NEW), ("inheritedRules", INHERITED_OLD, INHERITED_NEW)):
        if s[key].count(old) != 1:
            raise ValueError(f"{key} does not carry the version-3 phrase exactly once")
        s[key] = s[key].replace(old, new, 1)
    items = list(s.items())
    at = [k for k, _ in items].index("activeContent") + 1
    s = dict(items[:at] + [("secretRedaction", copy.deepcopy(REDACTION))] + items[at:])
    if variant == "span-guides":
        r = doc_rule(s)
        root = next(p for p in r["pathRules"] if p["id"] == "root-document")
        if root["rule"] != ROOT_RULE_OLD or r["notMapped"].count(NOT_MAPPED_OLD) != 1:
            raise ValueError("the version-3 root-document rule or notMapped text is not the expected one")
        root["rule"] = ROOT_RULE_NEW
        r["notMapped"] = r["notMapped"].replace(NOT_MAPPED_OLD, NOT_MAPPED_NEW, 1)
        ritems = list(r.items())
        rat = [k for k, _ in ritems].index("rootStems") + 1
        r2 = dict(ritems[:rat] + [("rootGuideStems", list(ROOT_GUIDE_STEMS)),
                                  ("rootGuideSuffixes", list(ROOT_GUIDE_SUFFIXES))] + ritems[rat:])
        rules = s["contentClassification"]["rules"]
        rules[rules.index(r)] = r2
    return s


def next_version(version: str, variant: str) -> str:
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)(-.+)", version)
    if not m:
        raise ValueError(f"unparseable policyVersion {version}")
    return f"{m.group(1)}.{int(m.group(2)) + 1}.0{m.group(4)}.redact-{variant}"


def propose(base_text: str, variant: str) -> str:
    base = json.loads(base_text)
    old = v2.block(base[SCOPE_KEY])
    if base_text.count(old) != 1:
        raise ValueError("the version-3 scope block is not found exactly once in its own bytes")
    version = f'  "policyVersion": "{base["policyVersion"]}",\n'
    if base_text.count(version) != 1:
        raise ValueError("policyVersion line not found exactly once")
    out = base_text.replace(old, v2.block(v4_scope(base[SCOPE_KEY], variant)), 1)
    out = out.replace(version, f'  "policyVersion": "{next_version(base["policyVersion"], variant)}",\n', 1)
    got = json.loads(out)
    expected = dict(base)
    expected["policyVersion"] = next_version(base["policyVersion"], variant)
    expected[SCOPE_KEY] = v4_scope(base[SCOPE_KEY], variant)
    if got != expected or list(got) != list(base):
        raise ValueError("text replacement changed something other than the scope block and policyVersion")
    return out


def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def manifest_rows(root: pathlib.Path) -> dict[str, str]:
    path = root / MANIFEST
    if not path.is_file():
        return {}
    return {m.group(2): m.group(1) for m in
            re.finditer(r"^([0-9a-f]{64})  \S+  \[variant: ([\w-]+)\]$", path.read_text(), re.M)}


def manifest_text(proposeds: dict[str, str]) -> str:
    rows = "".join(f"{sha(proposeds[v])}  {POLICY.as_posix()}  [variant: {v}]\n" for v in VARIANTS)
    return ("# PUBLIC-SOURCE SCREENING SCOPE VERSION 4 MANIFEST\n"
            "# Candidate; this file and its rows bind nothing by themselves.\n"
            "# 2 rows, one per variant (span, span-guides). Each row hashes the PROPOSED bytes\n"
            "# (the version-3 policy, variant all, with that variant's\n"
            "# proposed/<name>.<variant>.patch applied). The owner picks at most one row;\n"
            "# that row is the argument of one superseding approve-policy act.\n"
            + rows)


def base_bytes(root: pathlib.Path = ROOT) -> tuple[str, str]:
    want = v3.manifest_rows(root).get(V3_BASE_VARIANT)
    if want is None:
        raise ValueError("the version-3 manifest has no row for variant all")
    disk_text = (root / POLICY).read_text()
    if sha(disk_text) == want:
        return disk_text, "prospective"
    own = [v for v, dg in manifest_rows(root).items() if dg == sha(disk_text)]
    if own and (root / patch_path(own[0])).is_file():
        back = v2.reverse_patch((root / patch_path(own[0])).read_text(), disk_text)
        if sha(back) != want:
            raise ValueError("reversing this package's patch over the policy on disk does not give the version-3 bytes")
        return back, "performed-v4"
    raise ValueError("the policy on disk is neither the version-3 variant-all bytes nor one of this package's "
                     "rows; the base is unknown")


# --- reference oracles (fixtures; the policy carries the rules as data) ------

def is_documentation(path: str, policy_text: str) -> bool:
    """Reference reading of the root-document rule as amended, delegating every other path to version 2's oracle."""
    r = doc_rule(json.loads(policy_text)[SCOPE_KEY])
    if v2.classify_documentation(path, r):
        return True
    p = v2.ascii_fold(path)
    if "/" in p or not p or "\\" in p or p in (".", ".."):
        return False
    stems = set(r.get("rootGuideStems", []))
    cands = [p] + ([p[r["rootStemNumericPrefix"]["digitCount"] + 1:]] if v2.has_numeric_prefix(p, r) else [])
    return any(c.endswith(sfx) and c[:len(c) - len(sfx)] in stems
               for c in cands for sfx in r.get("rootGuideSuffixes", []) if sfx)


_NO_RESCREEN = False  # selftest mutant switch
_NON_OVERLAPPING = False  # selftest mutant switch: a plain left-to-right scan


def withheld_lines(body: str, policy_text: str) -> set[int] | None:
    """Reference reading of secretRedaction: the withheld 1-based line numbers, or None when the body is excluded
    whole. An empty set means no detector matched (the body is admitted unredacted)."""
    doc = json.loads(policy_text)
    red = doc[SCOPE_KEY].get("secretRedaction")
    lines = re.findall(r"[^\r\n]*(?:\r\n|\r|\n)|[^\r\n]+$", body)
    starts, pos = [], 0
    for ln in lines:
        starts.append(pos)
        pos += len(ln)

    def line_of(offset: int) -> int:
        lo = 0
        for i, s in enumerate(starts):
            if s <= offset:
                lo = i
        return lo + 1

    def matches(text: str) -> list[tuple[str, int, int]]:
        if not _NON_OVERLAPPING:
            return all_offsets(text)
        out = []
        for d in doc["detectors"]:
            if d["kind"] == "literal-fragment":
                for v in d["values"]:
                    for m in re.finditer(re.escape(v), text):
                        out.append((d["id"], m.start(), m.end()))
            else:
                flags = re.I if "i" in d.get("flags", "") else 0
                for m in re.finditer(d["pattern"], text, flags):
                    out.append((d["id"], m.start(), m.end()))
        return out

    def all_offsets(text: str) -> list[tuple[str, int, int]]:
        out = []
        for d in doc["detectors"]:
            if d["kind"] == "literal-fragment":
                for v in d["values"]:
                    out += [(d["id"], i, i + len(v)) for i in range(len(text)) if text.startswith(v, i)]
            else:
                rx = re.compile(d["pattern"], re.I if "i" in d.get("flags", "") else 0)
                for i in range(len(text)):
                    m = rx.match(text, i)
                    if m:
                        out.append((d["id"], m.start(), m.end()))
        return out

    found = matches(body)
    if not found:
        return set()
    if red is None or any(i in red["wholeArtifactDetectors"] for i, _, _ in found) or any(
            f in body for f in red.get("wholeArtifactFragments", [])):
        return None
    g = red["guardLines"]
    held: set[int] = set()
    for _i, a, b in found:
        for n in range(line_of(a), line_of(max(a, b - 1)) + 1):
            held.update(k for k in range(n - g, n + g + 1) if 1 <= k <= len(lines))
    retained = "".join(re.sub(r"[^\r\n]", "", ln) if k + 1 in held else ln for k, ln in enumerate(lines))
    if matches(retained) and not _NO_RESCREEN:
        return None
    return held


#: (path, documentation under span, documentation under span-guides)
DOC_FIXTURES = [
    ("README.md", True, True),
    ("INSTALL.md", False, True),
    ("Building.rst", False, True),
    ("00-UPGRADING.txt", False, True),
    ("HACKING.md", False, True),
    ("INSTALL", False, False),
    ("BUILD", False, False),
    ("SECURITY.md", False, False),
    ("MANIFESTO", False, False),
    ("MANIFESTO.md", False, False),
    ("ARCHITECTURE.md", False, False),
    ("TLS.md", False, False),
    ("modules/MODULES.md", False, False),
    ("src/INSTALL.md", False, False),
    ("AGENTS.md", False, False),
]

_TOKEN = "tok" + "en=" + "abcdefgh12345678"
#: (name, body, expected withheld lines under both variants; None = excluded whole)
BODY_FIXTURES = [
    ("clean body", "# T\nplain\n", set()),
    ("badge on line 1", f"[![c](https://x/y?{_TOKEN})]\nline2\nline3\nline4\n", {1, 2}),
    ("match mid-body", f"a\nb\nc {_TOKEN}\nd\ne\n", {2, 3, 4}),
    ("assignment across lines", "a\nb\npass" + "word\n\n= abcdefgh12345678\nf\ng\n", {2, 3, 4, 5, 6}),
    ("private key header", "a\n-----BEGIN " + "PRIVATE KEY-----\nMIIB\n-----END PRIVATE KEY-----\n", None),
    ("CRLF lines", f"a\r\n{_TOKEN}\r\nc\r\nd\r\n", {1, 2, 3}),
    ("emptied lines join a new match", "pass" + f"word\nx\na {_TOKEN}\ny\n= abcdefgh12345678\n", None),
    ("AWS access-key id with its secret key", 'provider "aws" {\n  access_key = "AKIA' + "ABCDEFGHIJKLMNOP" + '"\n'
     '  region = "us-east-1"\n  secret_key = "wJalrXUtnFEMIK7MDENGbPxRfiCYEXAMPLEKEY12"\n}\n', None),
    ("hidden overlapping match", "intro\nsecret: pass" + "word\n\n\n: Hunter2Hunter2Real\nend\n", {1, 2, 3, 4, 5, 6}),
    ("EC key beside a badge", f"[b](https://x/y?{_TOKEN})\n\n-----BEGIN EC " + "PRIVATE KEY-----\nMHcC\n-----END EC PRIVATE KEY-----\n", None),
]


def semantic_findings(base_text: str, proposed_text: str, variant: str) -> list[str]:
    base, new = json.loads(base_text), json.loads(proposed_text)
    bad: list[str] = []
    if new.get("policyVersion") != next_version(base["policyVersion"], variant):
        bad.append("policyVersion is not the next minor with the variant appended")
    if {k: v for k, v in new.items() if k not in (SCOPE_KEY, "policyVersion")} != {
            k: v for k, v in base.items() if k not in (SCOPE_KEY, "policyVersion")}:
        bad.append("a key other than policyVersion and the scope differs from version 3")
    s3, s4 = base[SCOPE_KEY], new.get(SCOPE_KEY)
    if not isinstance(s4, dict):
        return bad + ["publicSourceScope missing"]
    moved = {k for k in set(s3) | set(s4) if s3.get(k) != s4.get(k)}
    allowed = {"detectors", "inheritedRules", "secretRedaction"} | ({"contentClassification"} if variant == "span-guides" else set())
    if moved != allowed:
        bad.append(f"scope keys changed are {sorted(moved)}, not {sorted(allowed)}")
    if s4.get("detectors") != s3["detectors"].replace(DETECTORS_OLD, DETECTORS_NEW, 1):
        bad.append("the scope detectors sentence is not version 3's with the redaction clause appended")
    if s4.get("inheritedRules") != s3["inheritedRules"].replace(INHERITED_OLD, INHERITED_NEW, 1):
        bad.append("inheritedRules is not version 3's with the redaction exception named once")
    red = s4.get("secretRedaction")
    if red != REDACTION:
        bad.append("secretRedaction is not exactly the declared object")
    if not isinstance(red, dict):
        return bad + ["secretRedaction missing"]
    for det in WHOLE_ARTIFACT_DETECTORS:
        if det not in red.get("wholeArtifactDetectors", []):
            bad.append(f"{det} no longer excludes the whole artifact")
    if "-----BEGIN " not in red.get("wholeArtifactFragments", []):
        bad.append("a PEM header no longer excludes the whole artifact")
    if "overlapping matches included" not in red.get("rule", ""):
        bad.append("the match set is no longer every match from every offset")
    det_ids = {d["id"] for d in new["detectors"]}
    if not set(red.get("wholeArtifactDetectors", [])) <= det_ids:
        bad.append("a wholeArtifactDetectors id names no detector")
    if not isinstance(red.get("guardLines"), int) or red.get("guardLines", 0) < 1:
        bad.append("guardLines is not a positive integer")
    for needle in ("Every detector then runs again over the retained text", "excluded-artifact"):
        if needle not in red.get("rule", ""):
            bad.append("the rule no longer re-screens the retained text and excludes it whole on a match")
    if "withheld whole, never shown in part" not in red.get("citedSpanRule", ""):
        bad.append("a cited span that includes a withheld line is no longer withheld whole")
    if "no digest of a withheld line" not in red.get("withheldLines", ""):
        bad.append("a withheld line's digest is no longer forbidden")
    if "excludes the body whole" not in red.get("unchanged", ""):
        bad.append("the active-content exclusion is no longer whole-body")
    for key in ("activeContent", "accessBoundary", "rawBodyHandling", "sourceAdmission", "prerequisite"):
        if s4.get(key) != s3.get(key):
            bad.append(f"{key} differs from version 3")
    if s4 != v4_scope(s3, variant):
        bad.append("the scope is not exactly the declared version-4 scope")
    cc3, cc4 = s3["contentClassification"], s4.get("contentClassification", {})
    if variant == "span-guides":
        r3, r4 = doc_rule(s3), doc_rule(s4)
        others3 = [r for r in cc3["rules"] if r["class"] != "project-documentation"]
        others4 = [r for r in cc4["rules"] if r["class"] != "project-documentation"]
        if others3 != others4 or {k: v for k, v in cc3.items() if k != "rules"} != {k: v for k, v in cc4.items() if k != "rules"}:
            bad.append("a classification rule other than project-documentation differs from version 3")
        if set(r4) - set(r3) != {"rootGuideStems", "rootGuideSuffixes"}:
            bad.append("the documentation rule gained keys other than rootGuideStems and rootGuideSuffixes")
        if r4.get("rootStems") != r3["rootStems"]:
            bad.append("rootStems differs from version 3")
        guides = r4.get("rootGuideStems", [])
        if guides != ROOT_GUIDE_STEMS or set(guides) & (FORBIDDEN_GUIDE_STEMS | set(r3["rootStems"])):
            bad.append("rootGuideStems is not the declared list, or names a withheld or existing stem")
        if any(set(v2.tokens(st, r3["docTokenSeparators"])) & set(r3["docExcludedTokens"]) for st in guides):
            bad.append("a rootGuideStems name carries a docExcludedTokens word")
        if r4.get("rootGuideSuffixes") != ROOT_GUIDE_SUFFIXES or "" in r4.get("rootGuideSuffixes", [""]):
            bad.append("rootGuideSuffixes is not the declared non-empty list")
        src = next(r for r in cc4["rules"] if r["class"] == "code-content")["sourceExtensions"]
        if set(r4.get("rootGuideSuffixes", [])) & set(src):
            bad.append("a rootGuideSuffixes entry is a code-content source extension")
    elif cc4 != cc3:
        bad.append("contentClassification differs from version 3")
    for path, want_span, want_guides in DOC_FIXTURES:
        want = want_span if variant == "span" else want_guides
        if is_documentation(path, proposed_text) != want:
            bad.append(f"documentation fixture {path!r}: expected {want}")
    for name, body, want in BODY_FIXTURES:
        if withheld_lines(body, proposed_text) != want:
            bad.append(f"body fixture {name!r}: expected withheld {want}")
    return bad


def check(root: pathlib.Path = ROOT) -> list[str]:
    findings: list[str] = []
    try:
        base, _mode = base_bytes(root)
        proposeds = {v: propose(base, v) for v in VARIANTS}
    except (ValueError, OSError) as exc:
        return [str(exc)]
    if len(set(proposeds.values())) != len(VARIANTS):
        findings.append("two variants produce the same bytes")
    for v, proposed in proposeds.items():
        path = root / patch_path(v)
        if not path.is_file() or path.read_text() != v3.unified(base, proposed):
            findings.append(f"{v}: patch differs from its regeneration over the version-3 bytes")
        else:
            try:
                if v2.v1.apply_patch(root, base, path.read_text()) != proposed:
                    findings.append(f"{v}: applying the patch does not yield the proposed bytes")
            except ValueError as exc:
                findings.append(f"{v}: {exc}")
        findings += [f"{v}: {f}" for f in semantic_findings(base, proposed, v)]
    if not (root / MANIFEST).is_file() or (root / MANIFEST).read_text() != manifest_text(proposeds):
        findings.append("manifest differs from its regeneration")
    present = sorted(p.name for p in (root / PKG / "proposed").glob("*")) if (root / PKG / "proposed").is_dir() else []
    if present != sorted(patch_path(v).name for v in VARIANTS):
        findings.append(f"proposed/ holds {present}, not exactly the two declared patches")
    for md in sorted((root / PKG).glob("*.md")):
        if re.search(r"(?<![0-9a-fA-F])[0-9a-f]{64}(?![0-9a-fA-F])", md.read_text()):
            findings.append(f"{md.name}: carries a 64-hex token; the argument comes only from the manifest rows")
    return findings


def write(root: pathlib.Path = ROOT) -> None:
    base, _mode = base_bytes(root)
    proposeds = {v: propose(base, v) for v in VARIANTS}
    (root / PKG / "proposed").mkdir(parents=True, exist_ok=True)
    for v, proposed in proposeds.items():
        (root / patch_path(v)).write_text(v3.unified(base, proposed))
    (root / MANIFEST).write_text(manifest_text(proposeds))


# --- selftest ---------------------------------------------------------------

def _fixture(tmp: pathlib.Path) -> pathlib.Path:
    for rel in (POLICY, v3.MANIFEST):
        (tmp / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / rel, tmp / rel)
    if (ROOT / PKG).is_dir():
        shutil.copytree(ROOT / PKG, tmp / PKG, ignore=shutil.ignore_patterns("reviews"))
    else:
        (tmp / PKG).mkdir(parents=True)
    write(tmp)
    return tmp


def selftest() -> int:
    results: list[tuple[str, bool]] = []

    def caught(name, mutate, needle):
        with tempfile.TemporaryDirectory() as t:
            tmp = _fixture(pathlib.Path(t))
            mutate(tmp)
            results.append((name, any(needle in f for f in check(tmp))))

    with tempfile.TemporaryDirectory() as t:
        tmp = _fixture(pathlib.Path(t))
        results.append(("a regenerated package verifies", check(tmp) == []))
        base, mode = base_bytes(tmp)
        results.append(("the base is the version-3 variant-all row", mode == "prospective"))
        for v in VARIANTS:
            (tmp / POLICY).write_text(propose(base, v))
            results.append((f"after a variant-{v} act the package still verifies",
                            check(tmp) == [] and base_bytes(tmp)[1] == "performed-v4"))

    def unknown_disk(tmp):
        (tmp / POLICY).write_text((tmp / POLICY).read_text().replace('"schemaVersion": 1', '"schemaVersion": 2', 1))
    caught("a policy on disk that is neither base nor row refused", unknown_disk, "base is unknown")

    def edit_patch(tmp):
        p = tmp / patch_path("span")
        p.write_text(p.read_text().replace('"guardLines": 1', '"guardLines": 0', 1))
    caught("a hand-edited patch refused", edit_patch, "span: patch differs")

    def edit_manifest(tmp):
        p = tmp / MANIFEST
        p.write_text(p.read_text().replace("[variant: span-guides]", "[variant: guides]"))
    caught("an edited manifest refused", edit_manifest, "manifest differs")

    def extra_patch(tmp):
        (tmp / PKG / "proposed" / "extra.patch").write_text("x\n")
    caught("an undeclared patch refused", extra_patch, "not exactly the two declared patches")

    def digest_in_md(tmp):
        (tmp / PKG / "SEMANTIC-DELTA.md").write_text("argument " + "a" * 64 + "\n")
    caught("a digest in a package Markdown file refused", digest_in_md, "64-hex")

    with tempfile.TemporaryDirectory() as t:
        tmp = _fixture(pathlib.Path(t))
        base, _ = base_bytes(tmp)

        def sem(name, variant, mutate, needle):
            doc = json.loads(propose(base, variant))
            mutate(doc)
            got = semantic_findings(base, v2.dump(doc), variant)
            results.append((name, any(needle in f for f in got)))

        def red(d):
            return d[SCOPE_KEY]["secretRedaction"]

        def guides(d):
            return doc_rule(d[SCOPE_KEY])

        sem("a detector change caught", "span", lambda d: d["detectors"][0]["values"].pop(), "a key other than")
        sem("a base matchAction change caught", "span",
            lambda d: d["matchAction"].__setitem__("action", "redact"), "a key other than")
        sem("an activeContent change caught", "span",
            lambda d: d[SCOPE_KEY]["activeContent"].__setitem__("rule", "x"), "scope keys changed")
        sem("private-key-material moved to redaction caught", "span",
            lambda d: red(d)["wholeArtifactDetectors"].remove("private-key-material"), "private-key-material")
        sem("known-token-formats moved to redaction caught", "span",
            lambda d: red(d)["wholeArtifactDetectors"].remove("known-token-formats"), "known-token-formats")
        sem("a dropped PEM fragment caught", "span",
            lambda d: red(d).__setitem__("wholeArtifactFragments", []), "PEM header")
        sem("a non-overlapping match set caught", "span-guides",
            lambda d: red(d).__setitem__("rule", REDACTION["rule"].replace(", overlapping matches included", "")),
            "every match from every offset")
        sem("a zero guard caught", "span-guides", lambda d: red(d).__setitem__("guardLines", 0), "guardLines")
        sem("a dropped re-screen caught", "span",
            lambda d: red(d).__setitem__("rule", REDACTION["rule"].replace(
                "Every detector then runs again over the retained text", "The retained text is kept")),
            "re-screens the retained text")

    # the oracle's own re-screen: without it the joined match would come back redacted
    with tempfile.TemporaryDirectory() as t:
        tmp = _fixture(pathlib.Path(t))
        base, _ = base_bytes(tmp)
        global _NO_RESCREEN
        _NO_RESCREEN = True
        try:
            got = withheld_lines(BODY_FIXTURES[6][1], propose(base, "span"))
        finally:
            _NO_RESCREEN = False
        results.append(("the oracle's re-screen is what excludes a joined match (mutant observed)", got == {2, 3, 4}))
        global _NON_OVERLAPPING
        _NON_OVERLAPPING = True
        try:
            got = withheld_lines(BODY_FIXTURES[8][1], propose(base, "span"))
        finally:
            _NON_OVERLAPPING = False
        results.append(("a non-overlapping scan leaks the hidden match's value line (mutant observed)",
                        got is not None and 5 not in got))
        sem("a partly shown span caught", "span",
            lambda d: red(d).__setitem__("citedSpanRule", "a span shows its surviving lines"), "withheld whole")
        sem("an allowed withheld-line digest caught", "span",
            lambda d: red(d).__setitem__("withheldLines", "a withheld line is recorded by digest"), "digest")
        sem("a per-span active-content exclusion caught", "span",
            lambda d: red(d).__setitem__("unchanged", "active content is redacted per line"), "active-content exclusion")
        sem("an unqualified scope detectors sentence caught", "span",
            lambda d: d[SCOPE_KEY].__setitem__("detectors", json.loads(base)[SCOPE_KEY]["detectors"]),
            "scope detectors sentence")
        sem("an unqualified inheritedRules caught", "span-guides",
            lambda d: d[SCOPE_KEY].__setitem__("inheritedRules", json.loads(base)[SCOPE_KEY]["inheritedRules"]),
            "inheritedRules is not version 3's")
        sem("an unbumped version caught", "span",
            lambda d: d.__setitem__("policyVersion", json.loads(base)["policyVersion"]), "policyVersion")
        sem("guide stems in variant span caught", "span",
            lambda d: guides(d).__setitem__("rootGuideStems", ["install"]), "contentClassification differs")
        sem("security added as a guide stem caught", "span-guides",
            lambda d: guides(d)["rootGuideStems"].append("security"), "rootGuideStems is not the declared")
        sem("manifesto added as a root stem caught", "span-guides",
            lambda d: guides(d)["rootStems"].append("manifesto"), "rootStems differs")
        sem("an empty guide suffix caught", "span-guides",
            lambda d: guides(d)["rootGuideSuffixes"].append(""), "rootGuideSuffixes")
        sem("a code extension as guide suffix caught", "span-guides",
            lambda d: guides(d)["rootGuideSuffixes"].append(".sh"), "rootGuideSuffixes")
        sem("a widened docs tree caught", "span-guides",
            lambda d: guides(d)["docTreeRoots"].append("wiki"), "not exactly the declared version-4 scope")
        sem("a widened source extension caught", "span-guides",
            lambda d: next(r for r in d[SCOPE_KEY]["contentClassification"]["rules"]
                           if r["class"] == "code-content")["sourceExtensions"].append(".conf"),
            "other than project-documentation")
        sem("a fixture flip caught (INSTALL.md not mapped)", "span-guides",
            lambda d: guides(d)["rootGuideStems"].remove("install"), "documentation fixture 'INSTALL.md'")
        sem("a body fixture flip caught (guard widened)", "span",
            lambda d: red(d).__setitem__("guardLines", 2), "body fixture 'match mid-body'")

    # the oracle itself: a private-key body must never come back redacted
    with tempfile.TemporaryDirectory() as t:
        tmp = _fixture(pathlib.Path(t))
        base, _ = base_bytes(tmp)
        prop = json.loads(propose(base, "span"))
        prop[SCOPE_KEY]["secretRedaction"]["wholeArtifactDetectors"] = []
        prop[SCOPE_KEY]["secretRedaction"]["wholeArtifactFragments"] = []
        got = withheld_lines(BODY_FIXTURES[4][1], v2.dump(prop))
        results.append(("the oracle redacts a key header only when the rule allows it (mutant observed)", got == {1, 2, 3}))

    # the documentation oracle must refuse a path outside every rule, or its fixtures prove nothing
    results.append(("the documentation oracle refuses a path outside every rule",
                    not is_documentation("notes/INSTALL.md", propose(base_bytes(ROOT)[0], "span-guides"))))

    failed = [n for n, ok in results if not ok]
    for name, ok in results:
        print(("ok   " if ok else "FAIL ") + name)
    print(f"selftest: {len(results) - len(failed)} of {len(results)} predicates held")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    flags = {"--write", "--check", "--digests", "--manifest-digest", "--selftest"}
    if len(argv) != 1 or argv[0] not in flags:
        print(__doc__)
        return 2
    mode = argv[0]
    if mode == "--selftest":
        return selftest()
    if mode == "--write":
        write(ROOT)
        print(f"wrote the two patches and {MANIFEST.name}")
        return 0
    problems = check(ROOT)
    if problems:
        for p in problems:
            print(f"FAIL {p}")
        return 1
    if mode == "--digests":
        print("".join(line + "\n" for line in (ROOT / MANIFEST).read_text().splitlines() if not line.startswith("#")), end="")
    elif mode == "--manifest-digest":
        print(hashlib.sha256((ROOT / MANIFEST).read_bytes()).hexdigest())
    else:
        print("public-source-screening-scope-v4: patches and manifest current")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
