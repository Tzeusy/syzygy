#!/usr/bin/env python3
"""Build and verify the inert public-source screening-scope version-3 package.

Package `contracts/candidates/public-source-screening-scope-v3/` (`syzygy-wsev`:
the Markdown active-content scanner withholds C source). This script performs
no owner act and writes no act record.

Version 2 (`contracts/candidates/public-source-screening-scope-v2/`, variant
none, approved 2026-10-07) applies the base active-content classification "to
every admitted body, Markdown or not", and says a loosening "would be a later
policy version and an explicit owner question". Version 3 is that version. It
changes two values inside `publicSourceScope` and nothing else:

- `activeContent` gains `codeContentExemption`: a code-content body whose
  extension the chosen variant lists is admitted without the active-content
  scan, only while every sink renders it as entity-encoded text under a
  script-forbidding Content-Security-Policy; every detector still runs;
- `inheritedRules` says the base active-content classification applies except
  where that exemption exempts a body.

`policyVersion` moves to the next minor, with the version-2 variant name kept
and the version-3 variant appended (`.none.code-all`, `.none.code-non-web`).

The subject is the policy AFTER version 2: the bytes of the version-2 manifest
row `none`. The builder takes the policy on disk when it hashes to that row, or
recovers that row's bytes by reversing this package's own patch when the disk
already is one of this package's rows (the state after a version-3 act). The
proposed bytes live only as unified diffs under `proposed/`; the two-row
manifest hashes the bytes each diff produces; the row the owner picks is the
argument of one superseding `approve-policy` act.

  --write             regenerate the patches and the manifest
  --check             verify the package against the policy on disk
  --digests           print the manifest rows (refuses while stale)
  --manifest-digest   print the SHA-256 of the manifest FILE (refuses while stale)
  --selftest          mutate each predicate; each must fail

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
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_public_source_screening_scope_v2 as v2  # noqa: E402

POLICY = v2.POLICY
SCOPE_KEY = v2.SCOPE_KEY
PKG = pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v3")
MANIFEST = PKG / "PUBLIC-SOURCE-SCREENING-SCOPE-V3-MANIFEST.txt"
V2_BASE_VARIANT = "none"

#: Languages that commonly carry HTML in their source: the non-web variant keeps scanning these.
WEB_EXTENSIONS = [".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx", ".php"]
VARIANTS = ("all", "non-web")

EXEMPTION_RULE = (
    "such a body is admitted without the active-content scan: neither step 4 of classificationOrder, nor the "
    "active-content condition of classificationSuccess, nor the malformed-code-context exclusion applies to it, "
    "because the Markdown code-context profile does not describe source code (it reads a comparison such as "
    "a<b && c>d as an HTML tag, and an unpaired backtick in source as a code context that never closes). Every "
    "detector still runs over the whole body; the denied-path, strict-UTF-8, NUL and resource-limit rules are "
    "unchanged; a project-documentation body, or a code-content body this exemption does not name, is scanned as "
    "before")
RENDER_CONDITION = (
    "the exemption holds for a sink only while that sink renders such a body, or any span of it, as text: every one "
    "of the characters & < > \" ' is written as a character reference, the bytes are never parsed as Markdown or "
    "HTML and never mint a link, element, attribute, script or handler, and the page carries a "
    "Content-Security-Policy whose default-src is 'none' and which carries no script-src, script-src-elem, "
    "script-src-attr or object-src directive. A consumer that cannot confirm this for a sink scans the body as "
    "before for that sink, and excludes it whole on a finding")
#: A later directive overrides default-src for its own fetch type, so the condition names each one it forbids.
FORBIDDEN_CSP_DIRECTIVES = ("script-src", "script-src-elem", "script-src-attr", "object-src")
EGRESS_RULE = (
    "the exemption changes no egress or consent rule: a span of such a body reaches an agent session or a provider "
    "only under the rules that already govern code-content")
ACTIVE_RULE = (
    "the base activeContentClassification, inertContextRule and the active-content condition of "
    "classificationSuccess apply unchanged to every admitted body that codeContentExemption does not exempt, "
    "Markdown or not: such a body with an active-content form outside a valid inert code context is excluded whole "
    "as active content")
CONSEQUENCE = (
    "[Inferred] a source file whose only active-content finding was markup-like bytes outside a Markdown code "
    "context (a comparison, a generic type, a template literal, a string holding HTML) is admitted when its "
    "extension is exempt; the first public-target run (2026-10-08) withheld seven C files of its target for active "
    "content. A body a secret detector matches stays excluded whole")
INHERITED_OLD = "activeContentClassification and the strict-UTF-8 and NUL rules"
INHERITED_NEW = ("activeContentClassification (except where activeContent.codeContentExemption exempts a body) "
                 "and the strict-UTF-8 and NUL rules")


def patch_path(variant: str) -> pathlib.Path:
    return PKG / "proposed" / f"{POLICY.name}.{variant}.patch"


def source_extensions(scope: dict) -> list[str]:
    return next(r for r in scope["contentClassification"]["rules"] if r["class"] == "code-content")["sourceExtensions"]


def exempt_extensions(scope: dict, variant: str) -> list[str]:
    src = source_extensions(scope)
    return list(src) if variant == "all" else [e for e in src if e not in WEB_EXTENSIONS]


def exemption(scope: dict, variant: str) -> dict:
    applies = ("a body this scope classifies code-content whose final path segment ends with one of "
               "exemptExtensions, compared case-sensitively as ASCII as sourceExtensions are")
    if variant == "non-web":
        applies += ("; " + ", ".join(WEB_EXTENSIONS) + " are code-content but not exempt, because those languages "
                    "commonly carry HTML in their source, and such a body is scanned as before")
    return {"appliesTo": applies, "exemptExtensions": exempt_extensions(scope, variant), "rule": EXEMPTION_RULE,
            "renderCondition": RENDER_CONDITION, "egress": EGRESS_RULE}


def v3_scope(scope2: dict, variant: str) -> dict:
    s = copy.deepcopy(scope2)
    if s["inheritedRules"].count(INHERITED_OLD) != 1:
        raise ValueError("inheritedRules does not name the base active-content classification exactly once")
    s["inheritedRules"] = s["inheritedRules"].replace(INHERITED_OLD, INHERITED_NEW, 1)
    s["activeContent"] = {"rule": ACTIVE_RULE, "codeContentExemption": exemption(s, variant), "consequence": CONSEQUENCE}
    return s


def next_version(version: str, variant: str) -> str:
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)(-.+)", version)
    if not m:
        raise ValueError(f"unparseable policyVersion {version}")
    return f"{m.group(1)}.{int(m.group(2)) + 1}.0{m.group(4)}.code-{variant}"


def propose(base_text: str, variant: str) -> str:
    """Text replacement of the one scope block and the version line, so every other byte is preserved."""
    base = json.loads(base_text)
    old = v2.block(base[SCOPE_KEY])
    if base_text.count(old) != 1:
        raise ValueError("the version-2 scope block is not found exactly once in its own bytes")
    version = f'  "policyVersion": "{base["policyVersion"]}",\n'
    if base_text.count(version) != 1:
        raise ValueError("policyVersion line not found exactly once")
    out = base_text.replace(old, v2.block(v3_scope(base[SCOPE_KEY], variant)), 1)
    out = out.replace(version, f'  "policyVersion": "{next_version(base["policyVersion"], variant)}",\n', 1)
    got = json.loads(out)
    expected = dict(base)
    expected["policyVersion"] = next_version(base["policyVersion"], variant)
    expected[SCOPE_KEY] = v3_scope(base[SCOPE_KEY], variant)
    if got != expected or list(got) != list(base):
        raise ValueError("text replacement changed something other than the scope block and policyVersion")
    return out


def unified(base_text: str, new_text: str) -> str:
    return "".join(difflib.unified_diff(
        base_text.splitlines(True), new_text.splitlines(True),
        f"a/{POLICY.as_posix()}", f"b/{POLICY.as_posix()}", n=1))


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
    return ("# PUBLIC-SOURCE SCREENING SCOPE VERSION 3 MANIFEST\n"
            "# Candidate; this file and its rows bind nothing by themselves.\n"
            "# 2 rows, one per variant (all, non-web). Each row hashes the PROPOSED bytes\n"
            "# (the version-2 policy, variant none, with that variant's\n"
            "# proposed/<name>.<variant>.patch applied). The owner picks at most one row;\n"
            "# that row is the argument of one superseding approve-policy act.\n"
            + rows)


def base_bytes(root: pathlib.Path = ROOT) -> tuple[str, str]:
    """(version-2 none bytes, mode): 'prospective' when the disk is those bytes, 'performed-v3' when the
    disk is one of this package's rows and reversing its patch gives them back."""
    want = v2.manifest_rows(root).get(V2_BASE_VARIANT)
    if want is None:
        raise ValueError("the version-2 manifest has no row for variant none")
    disk_text = (root / POLICY).read_text()
    if sha(disk_text) == want:
        return disk_text, "prospective"
    own = [v for v, dg in manifest_rows(root).items() if dg == sha(disk_text)]
    if own and (root / patch_path(own[0])).is_file():
        back = v2.reverse_patch((root / patch_path(own[0])).read_text(), disk_text)
        if sha(back) != want:
            raise ValueError("reversing this package's patch over the policy on disk does not give the version-2 bytes")
        return back, "performed-v3"
    raise ValueError("the policy on disk is neither the version-2 variant-none bytes nor one of this package's "
                     "rows; the base is unknown")


def is_exempt(path: str, policy_text: str) -> bool:
    """Reference oracle: would the scope in these bytes admit a body at this path without the active-content scan?"""
    scope = json.loads(policy_text)[SCOPE_KEY]
    ex = scope.get("activeContent", {}).get("codeContentExemption")
    if ex is None:
        return False
    name = path.rsplit("/", 1)[-1]
    is_code = any(name.endswith(e) for e in source_extensions(scope))
    return is_code and any(name.endswith(e) for e in ex["exemptExtensions"])


#: (path, exempt under all, exempt under non-web)
FIXTURES = [
    ("src/server.c", True, True),
    ("src/server.h", True, True),
    ("deps/lua/src/lapi.c", True, True),
    ("utils/install_server.sh", True, True),
    ("tests/helpers.tcl", True, True),
    ("web/app.js", True, False),
    ("web/App.tsx", True, False),
    ("index.php", True, False),
    ("README.md", False, False),
    ("docs/guide.md", False, False),
    ("src/server.C", False, False),
    ("redis.conf", False, False),
]


def semantic_findings(base_text: str, proposed_text: str, variant: str) -> list[str]:
    """Structural claims the packet makes; each is mutated in --selftest."""
    base, new = json.loads(base_text), json.loads(proposed_text)
    bad: list[str] = []
    if new.get("policyVersion") != next_version(base["policyVersion"], variant):
        bad.append("policyVersion is not the next minor with the variant appended")
    if {k: v for k, v in new.items() if k not in (SCOPE_KEY, "policyVersion")} != {
            k: v for k, v in base.items() if k not in (SCOPE_KEY, "policyVersion")}:
        bad.append("a key other than policyVersion and the scope differs from version 2")
    s2, s3 = base[SCOPE_KEY], new.get(SCOPE_KEY)
    if not isinstance(s3, dict):
        return bad + ["publicSourceScope missing"]
    moved = {k for k in set(s2) | set(s3) if s2.get(k) != s3.get(k)}
    if moved != {"activeContent", "inheritedRules"}:
        bad.append(f"scope keys changed beyond activeContent and inheritedRules: {sorted(moved)}")
    if s3.get("inheritedRules") != s2["inheritedRules"].replace(INHERITED_OLD, INHERITED_NEW, 1):
        bad.append("inheritedRules is not version 2's with the exemption named once")
    ac = s3.get("activeContent", {})
    ex = ac.get("codeContentExemption", {})
    src = source_extensions(s3)
    if ac.get("rule") != ACTIVE_RULE:
        bad.append("the active-content rule is not the declared one")
    if not ex:
        return bad + ["codeContentExemption missing"]
    exts = ex.get("exemptExtensions", [])
    if not set(exts) <= set(src) or len(exts) != len(set(exts)):
        bad.append("an exempt extension is not a code-content source extension, or one repeats")
    if variant == "all" and exts != list(src):
        bad.append("variant all does not exempt exactly the source extensions")
    if variant == "non-web" and (set(exts) & set(WEB_EXTENSIONS) or set(src) - set(exts) != set(WEB_EXTENSIONS) & set(src)):
        bad.append("variant non-web does not exempt exactly the source extensions outside the web list")
    if ex.get("rule") != EXEMPTION_RULE or "Every detector still runs over the whole body" not in ex.get("rule", ""):
        bad.append("the exemption rule is not the declared one, or no longer keeps every detector")
    if ex.get("renderCondition") != RENDER_CONDITION:
        bad.append("the render condition is not the declared one")
    cond = ex.get("renderCondition", "")
    if "default-src is 'none'" not in cond or any(not re.search(rf"(?<![\w-]){re.escape(d)}(?![\w-])", cond)
                                                  for d in FORBIDDEN_CSP_DIRECTIVES):
        bad.append("the render condition does not require default-src 'none' and forbid every script-bearing directive")
    if ex.get("egress") != EGRESS_RULE:
        bad.append("the egress statement is not the declared one")
    if ex != exemption(s3, variant):
        bad.append("the exemption object is not exactly the declared one")
    for key in ("detectors", "contentClassification", "accessBoundary", "rawBodyHandling", "sourceAdmission"):
        if s3.get(key) != s2.get(key):
            bad.append(f"{key} differs from version 2")
    for path, want_all, want_non_web in FIXTURES:
        want = want_all if variant == "all" else want_non_web
        if is_exempt(path, proposed_text) != want:
            bad.append(f"fixture {path!r}: expected exempt={want}")
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
        if not path.is_file() or path.read_text() != unified(base, proposed):
            findings.append(f"{v}: patch differs from its regeneration over the version-2 bytes")
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
        (root / patch_path(v)).write_text(unified(base, proposed))
    (root / MANIFEST).write_text(manifest_text(proposeds))


# --- selftest ---------------------------------------------------------------

def _fixture(tmp: pathlib.Path) -> pathlib.Path:
    for rel in (POLICY, v2.MANIFEST):
        (tmp / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / rel, tmp / rel)
    shutil.copytree(ROOT / PKG, tmp / PKG, ignore=shutil.ignore_patterns("reviews"))
    write(tmp)
    return tmp


def selftest() -> int:
    results: list[tuple[str, bool]] = []

    def caught(name, mutate, needle):
        with tempfile.TemporaryDirectory() as t:
            tmp = _fixture(pathlib.Path(t))
            mutate(tmp)
            found = check(tmp)
            results.append((name, any(needle in f for f in found)))

    with tempfile.TemporaryDirectory() as t:
        tmp = _fixture(pathlib.Path(t))
        results.append(("a regenerated package verifies", check(tmp) == []))
        base, mode = base_bytes(tmp)
        results.append(("the base is the version-2 variant-none row", mode == "prospective"))
        (tmp / POLICY).write_text(propose(base, "all"))
        results.append(("after a variant-all act the package still verifies", check(tmp) == []
                        and base_bytes(tmp)[1] == "performed-v3"))
        (tmp / POLICY).write_text(propose(base, "non-web"))
        results.append(("after a variant-non-web act the package still verifies", check(tmp) == []))

    def unknown_disk(tmp):
        (tmp / POLICY).write_text((tmp / POLICY).read_text().replace('"schemaVersion": 1', '"schemaVersion": 2', 1))
    caught("a policy on disk that is neither base nor row refused", unknown_disk, "base is unknown")

    def edit_patch(tmp):
        p = tmp / patch_path("all")
        p.write_text(p.read_text().replace("a<b && c>d", "a<b and c>d", 1))
    caught("a hand-edited patch refused", edit_patch, "all: patch differs")

    def edit_manifest(tmp):
        p = tmp / MANIFEST
        p.write_text(p.read_text().replace("[variant: non-web]", "[variant: nonweb]"))
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

        sem("a detector change caught", "all",
            lambda d: d["detectors"][0]["values"].pop(), "a key other than policyVersion")
        sem("a scope detector-rule change caught", "all",
            lambda d: d[SCOPE_KEY].__setitem__("detectors", "none"), "scope keys changed")
        sem("a classification change caught", "all",
            lambda d: d[SCOPE_KEY]["contentClassification"]["classesClassified"].append("work-history"),
            "contentClassification differs")
        sem("a non-source exempt extension caught", "all",
            lambda d: d[SCOPE_KEY]["activeContent"]["codeContentExemption"]["exemptExtensions"].append(".md"),
            "not a code-content source extension")
        sem("a web extension in non-web caught", "non-web",
            lambda d: d[SCOPE_KEY]["activeContent"]["codeContentExemption"]["exemptExtensions"].append(".js"),
            "variant non-web does not exempt")
        sem("a missing extension in all caught", "all",
            lambda d: d[SCOPE_KEY]["activeContent"]["codeContentExemption"]["exemptExtensions"].remove(".c"),
            "variant all does not exempt")
        sem("a dropped render condition caught", "all",
            lambda d: d[SCOPE_KEY]["activeContent"]["codeContentExemption"].pop("renderCondition"),
            "render condition")
        for directive in FORBIDDEN_CSP_DIRECTIVES:
            sem(f"a render condition that allows {directive} caught", "non-web",
                lambda d, directive=directive: d[SCOPE_KEY]["activeContent"]["codeContentExemption"].__setitem__(
                    "renderCondition", re.sub(rf"(?<![\w-]){re.escape(directive)}(?![\w-])", "frame-src",
                                              RENDER_CONDITION)),
                "forbid every script-bearing directive")
        sem("a render condition without default-src 'none' caught", "all",
            lambda d: d[SCOPE_KEY]["activeContent"]["codeContentExemption"].__setitem__(
                "renderCondition", RENDER_CONDITION.replace("default-src is 'none'", "default-src is 'self'")),
            "forbid every script-bearing directive")
        sem("a dropped detector sentence caught", "all",
            lambda d: d[SCOPE_KEY]["activeContent"]["codeContentExemption"].__setitem__(
                "rule", EXEMPTION_RULE.replace("Every detector still runs over the whole body; ", "")),
            "no longer keeps every detector")
        sem("an unqualified inheritedRules caught", "all",
            lambda d: d[SCOPE_KEY].__setitem__("inheritedRules", json.loads(base)[SCOPE_KEY]["inheritedRules"]),
            "inheritedRules is not version 2's")
        sem("an unbumped version caught", "non-web",
            lambda d: d.__setitem__("policyVersion", json.loads(base)["policyVersion"]), "policyVersion")
        sem("a widened active-content rule caught", "all",
            lambda d: d[SCOPE_KEY]["activeContent"].__setitem__("rule", "nothing is scanned"),
            "active-content rule is not the declared one")
        sem("a fixture flip caught (README exempt)", "all",
            lambda d: (d[SCOPE_KEY]["contentClassification"]["rules"][1]["sourceExtensions"].append(".md"),
                       d[SCOPE_KEY]["activeContent"]["codeContentExemption"]["exemptExtensions"].append(".md")),
            "fixture 'README.md'")

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
        print("public-source-screening-scope-v3: patches and manifest current")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
