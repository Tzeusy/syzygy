#!/usr/bin/env python3
"""Verify and manifest the public-admission registry-entry candidates.

Package `contracts/candidates/public-admission-registry-entries/`: two
proposed adapter-registry entries (the Anthropic Agent SDK provider route and
one shared public Git-hosting source-acquisition adapter), each a whole
`proposed/*.json` file. They bind nothing; each takes effect only through its
own owner act over its exact bytes, whose argument is that file's row of
`PUBLIC-ADMISSION-REGISTRY-MANIFEST.txt`.

  --check            fail if a proposed entry breaks a predicate, a package
                     Markdown file carries a 64-hex token, or the manifest is
                     stale
  --write            regenerate the manifest (after a --check of the entries)
  --digests          print each proposed file's SHA-256
  --manifest-digest  print the SHA-256 of the manifest FILE
  --selftest         one mutant per predicate; each must be caught
"""
import copy
import hashlib
import json
import pathlib
import re
import sys

PKG = pathlib.Path(".syzygy/governance/contracts/candidates/public-admission-registry-entries")
MANIFEST = "PUBLIC-ADMISSION-REGISTRY-MANIFEST.txt"
BUTLERS = pathlib.Path(".syzygy/governance/declarations/adapter-registry/"
                       "POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json")
INSTALLED = pathlib.Path(".syzygy/governance/declarations/adapter-registry")
HEX64 = re.compile(r"[0-9a-f]{64}")
#: RFC4-2 items 1-7 as the keys an entry must carry.
REQUIRED = ("observerId", "implementationId", "observerVersion", "implementationVersion",
            "contractId", "contractVersion", "inputClasses", "outputFactClasses",
            "determinismClass", "failureStates", "typedAuthority")
#: The egress record's route conditions, as keys the provider entry must carry.
ROUTE_KEYS = ("tools", "ambientContext", "telemetry", "stateLocation",
              "acceptanceCheck", "fallback")
DEGRADATION = {"Observer failed", "Source unreachable", "Partial snapshot",
               "Excluded content", "Consent withdrawn"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def proposed(root=PKG):
    return sorted((root / "proposed").glob("*.json"))


def findings_for(name, doc, butlers_contract):
    out = []
    if doc.get("status") != "candidate-entry-no-effect-until-owner-act":
        out.append(f"{name}: status is not the candidate label")
    if len(doc.get("entries", [])) != 1:
        return out + [f"{name}: not exactly one entry"]
    e = doc["entries"][0]
    for k in REQUIRED:
        if k not in e:
            out.append(f"{name}: missing RFC4-2 declaration {k}")
    if e.get("implementationVersion") is not None:
        out.append(f"{name}: implementationVersion must stay null until implemented")
    if e.get("typedAuthority", {}).get("writeSurface") != []:
        out.append(f"{name}: writeSurface must be empty")
    if e.get("typedAuthority", {}).get("executeObservedCode") is not False:
        out.append(f"{name}: executeObservedCode must be false")
    if e.get("determinismClass") not in ("capture", "derivation-deterministic"):
        out.append(f"{name}: determinismClass outside RFC4-2")
    if e.get("contractVersion") != butlers_contract:
        out.append(f"{name}: contractVersion differs from the adopted Butlers entry's")
    if e.get("adoptionStatus") != "candidate-entry-unadopted":
        out.append(f"{name}: adoptionStatus is not candidate-entry-unadopted")
    for key, state in e.get("failureStates", {}).items():
        if isinstance(state, dict) and state.get("degradationState") not in DEGRADATION:
            out.append(f"{name}: failure state {key} names a degradation state outside the set")
    if e.get("typedAuthority", {}).get("authorityType") == "model-provider":
        for k in ROUTE_KEYS:
            if k not in e.get("routeConditions", {}):
                out.append(f"{name}: routeConditions lacks {k}")
        if e.get("typedAuthority", {}).get("toolInvocation") != []:
            out.append(f"{name}: toolInvocation must be empty")
    else:
        fetch = e.get("typedAuthority", {}).get("fetch", "")
        if "--depth=1" not in fetch or "exactly one admitted commit" not in fetch:
            out.append(f"{name}: fetch is not declared shallow by exactly one commit")
        if e.get("typedAuthority", {}).get("workingTreeRead") is not False:
            out.append(f"{name}: workingTreeRead must be false")
    return out


def manifest_text(root=PKG):
    rows = sorted((f"{root.as_posix()}/proposed/{p.name}", sha(p.read_bytes())) for p in proposed(root))
    return ("# PUBLIC ADMISSION REGISTRY ENTRIES MANIFEST\n"
            "# Candidate; this file and its rows bind nothing by themselves.\n"
            f"# {len(rows)} artifacts; rows sorted by codepoint path; each row hashes the\n"
            "# proposed file's exact bytes and is the argument of one separate owner act.\n"
            "# Each row requires its own act; neither row binds the other.\n"
            + "".join(f"{s}  {p}\n" for p, s in rows))


def check(root=PKG, butlers=BUTLERS, installed=INSTALLED):
    out = []
    contract = json.loads(butlers.read_text())["entries"][0]["contractVersion"]
    files = proposed(root)
    if len(files) != 2:
        out.append(f"expected 2 proposed entries, found {len(files)}")
    for p in files:
        try:
            doc = json.loads(p.read_text())
        except ValueError as exc:
            out.append(f"{p.name}: not JSON ({exc})")
            continue
        out += findings_for(p.name, doc, contract)
        if (installed / p.name).exists():
            out.append(f"{p.name}: candidate bytes already sit in the installed home")
    for md in sorted(root.glob("*.md")):
        if HEX64.search(md.read_text()):
            out.append(f"{md.name}: carries a 64-hex token")
    m = root / MANIFEST
    if not m.is_file() or m.read_text() != manifest_text(root):
        out.append(f"{MANIFEST}: stale or missing")
    return out


def selftest():
    import tempfile
    base = json.loads(next(iter(proposed())).read_text()) if proposed() else None
    assert base is not None, "no proposed entries to mutate"
    contract = json.loads(BUTLERS.read_text())["entries"][0]["contractVersion"]
    prov = json.loads((PKG / "proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json").read_text())
    src = json.loads((PKG / "proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-CANDIDATE.json").read_text())
    assert not findings_for("p", prov, contract) and not findings_for("s", src, contract)
    muts = []

    def mut(name, doc, fn, needle):
        d = copy.deepcopy(doc)
        fn(d["entries"][0], d)
        muts.append((name, any(needle in f for f in findings_for("m", d, contract))))

    mut("status upgraded", prov, lambda e, d: d.update(status="adopted"), "status")
    mut("declaration dropped", prov, lambda e, d: e.pop("failureStates"), "missing RFC4-2")
    mut("invented version", prov, lambda e, d: e.update(implementationVersion="1.0.0"), "implementationVersion")
    mut("write surface granted", src, lambda e, d: e["typedAuthority"].update(writeSurface=["x"]), "writeSurface")
    mut("observed code executed", src, lambda e, d: e["typedAuthority"].update(executeObservedCode=True), "executeObservedCode")
    mut("wrong determinism class", prov, lambda e, d: e.update(determinismClass="live"), "determinismClass")
    mut("contract version drift", prov, lambda e, d: e.update(contractVersion="sha256:0"), "contractVersion")
    mut("adopted label", src, lambda e, d: e.update(adoptionStatus="adopted"), "adoptionStatus")
    mut("degradation state invented", src,
        lambda e, d: e["failureStates"]["fetchFailed"].update(degradationState="Fine"), "degradation state")
    mut("route condition dropped", prov, lambda e, d: e["routeConditions"].pop("telemetry"), "routeConditions")
    mut("tool invocation allowed", prov, lambda e, d: e["typedAuthority"].update(toolInvocation=["bash"]), "toolInvocation")
    mut("full-history fetch", src, lambda e, d: e["typedAuthority"].update(fetch="git clone <upstream>"), "fetch")
    mut("working tree read", src, lambda e, d: e["typedAuthority"].update(workingTreeRead=True), "workingTreeRead")
    with tempfile.TemporaryDirectory() as t:
        root = pathlib.Path(t) / "pkg"
        (root / "proposed").mkdir(parents=True)
        inst = pathlib.Path(t) / "installed"
        inst.mkdir()
        for p in proposed():
            (root / "proposed" / p.name).write_bytes(p.read_bytes())
        (root / MANIFEST).write_text(manifest_text(root))
        muts.append(("clean temp package passes", check(root, BUTLERS, inst) == []))
        (root / "X.md").write_text("a" * 64)
        muts.append(("hex token in package prose", any("64-hex" in f for f in check(root, BUTLERS, inst))))
        (root / "X.md").unlink()
        (root / MANIFEST).write_text(manifest_text(root).replace("1", "2", 1))
        muts.append(("stale manifest", any("stale" in f for f in check(root, BUTLERS, inst))))
        (root / MANIFEST).write_text(manifest_text(root))
        name = next(iter(proposed())).name
        (inst / name).write_text("{}")
        muts.append(("candidate installed early", any("installed home" in f for f in check(root, BUTLERS, inst))))
    bad = [n for n, ok in muts if not ok]
    for n, ok in muts:
        print(("ok   " if ok else "FAIL ") + n)
    print(f"selftest: {len(muts) - len(bad)} of {len(muts)} predicates held")
    return 1 if bad else 0


def main(argv):
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode == "--selftest":
        return selftest()
    if mode == "--write":
        bad = check_entries_only()
        if bad:
            print("\n".join(bad), file=sys.stderr)
            return 1
        (PKG / MANIFEST).write_text(manifest_text())
        print(f"wrote {PKG / MANIFEST}")
        return 0
    if mode in ("--check", "--digests", "--manifest-digest"):
        bad = check()
        if bad:
            for f in bad:
                print("FINDING", f)
            return 1
        if mode == "--digests":
            for p in proposed():
                print(f"{sha(p.read_bytes())}  {p}")
        elif mode == "--manifest-digest":
            print(sha((PKG / MANIFEST).read_bytes()))
        else:
            print("public-admission registry entries: current")
        return 0
    print(f"unknown mode {mode}", file=sys.stderr)
    return 2


def check_entries_only():
    return [f for f in check() if MANIFEST not in f]


if __name__ == "__main__":
    sys.exit(main(sys.argv))
