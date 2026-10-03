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
#: RFC2-23's six states; "Missing quantity" is the one for absent tokens or cost.
DEGRADATION = {"Observer failed", "Source unreachable", "Partial snapshot",
               "Excluded content", "Consent withdrawn", "Missing quantity"}
#: RFC2-24's closed twelve reasons.
REASONS = {"missing-declaration", "missing-evidence", "no-currency-bound-declared",
           "stale-beyond-currency-bound", "mapping-coverage-absent",
           "unconsented-source-or-provider", "excluded-content",
           "contradicted-pending-adjudication", "challenge-suspended",
           "source-uncaptured-or-unreachable", "reference-unresolvable",
           "execution-blocked"}
CLASSES = {"capture", "derivation-deterministic"}
FETCH = "git fetch --depth=1 --no-tags --no-recurse-submodules <upstream> <commit>"
FETCH_FULL = (FETCH + ": one shallow fetch of exactly one admitted commit object id per fetch from the "
              "upstream locator named in the observation consent; a fetch of any other object, ref, tag "
              "or history is refused")
EGRESS_SOURCE = re.compile(r"record PUBLIC-EGRESS-anthropic .*version \d+\.\d+\.\d+-candidate\.\d+")
ACCEPTANCE = ("byte for byte", "requestBytes", "in neither fails")
#: Request fields the entry must pin itself, so the acceptance admits no profile-set byte.
PINNED = ("model", "tools", "effort", "thinking", "maxTokensCeiling")
RUNTIME_PIN = ("0.3.288", "2.1.288")


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
    if e.get("typedAuthority", {}).get("workingTreeRead") is not False:
        out.append(f"{name}: workingTreeRead must be false")
    if e.get("typedAuthority", {}).get("executeObservedCode") is not False:
        out.append(f"{name}: executeObservedCode must be false")
    if e.get("determinismClass") not in CLASSES:
        out.append(f"{name}: determinismClass outside RFC4-2")
    by_class = e.get("determinismByOutputClass", {})
    outputs = {c.get("class") for c in e.get("outputFactClasses", [])}
    if set(by_class) != outputs or not set(by_class.values()) <= CLASSES:
        out.append(f"{name}: determinismByOutputClass does not cover each output class once")
    if e.get("contractVersion") != butlers_contract:
        out.append(f"{name}: contractVersion differs from the adopted Butlers entry's")
    if e.get("adoptionStatus") != "candidate-entry-unadopted":
        out.append(f"{name}: adoptionStatus is not candidate-entry-unadopted")
    for key, state in e.get("failureStates", {}).items():
        if not isinstance(state, dict):
            continue
        if "degradationState" in state and state["degradationState"] not in DEGRADATION:
            out.append(f"{name}: failure state {key} names a degradation state outside the set")
        if "degradationState" not in state and "executionFact" not in state:
            out.append(f"{name}: failure state {key} names neither a degradation state nor an execution fact")
        if state.get("unknownReason") not in REASONS:
            out.append(f"{name}: failure state {key} names a reason outside RFC2-24")
    if "determinismClassNote" not in e:
        out.append(f"{name}: scalar determinismClass is unexplained")
    if not isinstance(e.get("snapshotInputMapping"), dict):
        out.append(f"{name}: snapshotInputMapping is not a per-class mapping")
    else:
        unmapped = {c.get("class") for c in e.get("inputClasses", [])} - set(e["snapshotInputMapping"])
        if unmapped:
            out.append(f"{name}: snapshotInputMapping omits input classes {sorted(unmapped)}")
    if e.get("supersession") is None:
        out.append(f"{name}: supersession statement missing")
    if e.get("snapshotInputMapping") is None:
        out.append(f"{name}: snapshotInputMapping missing")
    if e.get("typedAuthority", {}).get("authorityType") == "model-provider":
        for k in ROUTE_KEYS:
            if k not in e.get("routeConditions", {}):
                out.append(f"{name}: routeConditions lacks {k}")
        ta = e.get("typedAuthority", {})
        if ta.get("toolInvocation") != []:
            out.append(f"{name}: toolInvocation must be empty")
        pin = e.get("runtimePin", {})
        if (pin.get("version"), pin.get("bundledCli")) != RUNTIME_PIN:
            out.append(f"{name}: runtimePin is not the measured SDK and CLI versions")
        rc = e.get("routeConditions", {})
        if not EGRESS_SOURCE.search(rc.get("source", "")):
            out.append(f"{name}: routeConditions.source names no egress record ID and version")
        if not all(w in rc.get("acceptanceCheck", "") for w in ACCEPTANCE):
            out.append(f"{name}: acceptanceCheck does not require generator parts byte for byte and the listed bytes")
        rb = e.get("requestBytes", {})
        for k in ("pinnedVersions", "generatorBuilt", "runtimeFixed", "routeFixedByThisEntry", "headers", "probe", "absentByConstruction", "unlistedBytes"):
            if k not in rb:
                out.append(f"{name}: requestBytes lacks {k}")
        for k in PINNED:
            if k not in rb.get("routeFixedByThisEntry", {}):
                out.append(f"{name}: routeFixedByThisEntry does not pin {k}")
        if (rb.get("pinnedVersions", {}).get("version"), rb.get("pinnedVersions", {}).get("bundledCli")) != RUNTIME_PIN:
            out.append(f"{name}: requestBytes pins other versions than runtimePin")
        if "requestBytes" not in ta.get("readAuthority", ""):
            out.append(f"{name}: readAuthority does not point at requestBytes")
        if not rc.get("fallback", "").startswith("none"):
            out.append(f"{name}: fallback must be none")
        if len(ta.get("networkAccess", [])) != 1:
            out.append(f"{name}: provider networkAccess must be exactly one destination")
        for cls in ("model-identity",):
            if cls not in outputs:
                out.append(f"{name}: outputFactClasses lacks {cls}")
        if "runtime-version-and-configuration" not in {c.get("class") for c in e.get("inputClasses", [])}:
            out.append(f"{name}: inputClasses lacks runtime-version-and-configuration")
        if "writeSurfaceArgument" not in ta:
            out.append(f"{name}: writeSurface is not argued")
        if "[Unknown]" not in " ".join(e.get("unknowns", [])):
            out.append(f"{name}: unknowns lists no Unknown")
    else:
        fetch = e.get("typedAuthority", {}).get("fetch", "")
        if fetch != FETCH_FULL:
            out.append(f"{name}: fetch is not the declared shallow single-commit form")
        ta = e.get("typedAuthority", {})
        if len(ta.get("networkAccess", [])) != 1:
            out.append(f"{name}: networkAccess must be exactly one destination")
        limits = e.get("resourceLimits", {})
        sem = e.get("resourceLimitSemantics", {})
        for k in limits:
            if k != "status" and k not in sem:
                out.append(f"{name}: resource limit {k} has no semantics")
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

    for doc, tag in ((prov, "provider"), (src, "git")):
        mut(f"{tag}: status upgraded", doc, lambda e, d: d.update(status="adopted"), "status")
        mut(f"{tag}: adoptionStatus adopted", doc, lambda e, d: e.update(adoptionStatus="adopted"), "adoptionStatus")
        mut(f"{tag}: invented version", doc, lambda e, d: e.update(implementationVersion="1.0.0"), "implementationVersion")
        mut(f"{tag}: write surface granted", doc, lambda e, d: e["typedAuthority"].update(writeSurface=["x"]), "writeSurface")
        mut(f"{tag}: observed code executed", doc, lambda e, d: e["typedAuthority"].update(executeObservedCode=True), "executeObservedCode")
        mut(f"{tag}: working tree read", doc, lambda e, d: e["typedAuthority"].update(workingTreeRead=True), "workingTreeRead")
        mut(f"{tag}: wrong determinism class", doc, lambda e, d: e.update(determinismClass="live"), "determinismClass")
        mut(f"{tag}: per-class determinism dropped", doc, lambda e, d: e.pop("determinismByOutputClass"), "determinismByOutputClass")
        mut(f"{tag}: per-class value invented", doc,
            lambda e, d: e["determinismByOutputClass"].update({next(iter(e["determinismByOutputClass"])): "live"}), "determinismByOutputClass")
        mut(f"{tag}: contract version drift", doc, lambda e, d: e.update(contractVersion="sha256:0"), "contractVersion")
        mut(f"{tag}: two entries", doc, lambda e, d: d["entries"].append(e), "not exactly one")
        mut(f"{tag}: network widened", doc, lambda e, d: e["typedAuthority"]["networkAccess"].append("elsewhere"), "networkAccess")
        mut(f"{tag}: supersession dropped", doc, lambda e, d: e.pop("supersession"), "supersession")
        mut(f"{tag}: snapshot mapping dropped", doc, lambda e, d: e.pop("snapshotInputMapping"), "snapshotInputMapping")
        mut(f"{tag}: degradation state invented", doc,
            lambda e, d: next(v for v in e["failureStates"].values() if isinstance(v, dict) and "degradationState" in v).update(degradationState="Fine"),
            "degradation state")
        mut(f"{tag}: reason outside RFC2-24", doc,
            lambda e, d: next(v for v in e["failureStates"].values() if isinstance(v, dict)).update(unknownReason="made-up"), "RFC2-24")
        mut(f"{tag}: state names neither state nor fact", doc,
            lambda e, d: e["failureStates"].update(x={"unknownReason": "excluded-content"}), "neither a degradation state")
        for k in REQUIRED:
            mut(f"{tag}: declaration {k} dropped", doc, lambda e, d, k=k: e.pop(k), "missing RFC4-2")
    for k in ROUTE_KEYS:
        mut(f"route condition {k} dropped", prov, lambda e, d, k=k: e["routeConditions"].pop(k), "routeConditions")
    mut("tool invocation allowed", prov, lambda e, d: e["typedAuthority"].update(toolInvocation=["bash"]), "toolInvocation")
    mut("runtime pin drift", prov, lambda e, d: e["runtimePin"].update(version="0.3.289"), "runtimePin")
    mut("egress record unnamed", prov, lambda e, d: e["routeConditions"].update(source="instances/egress-anthropic"), "egress record ID")
    mut("fallback allowed", prov, lambda e, d: e["routeConditions"].update(fallback="the direct API"), "fallback")
    mut("model identity dropped", prov, lambda e, d: e["outputFactClasses"].pop(3) and e["determinismByOutputClass"].pop("model-identity"), "model-identity")
    mut("runtime version input dropped", prov, lambda e, d: e["inputClasses"].pop(-2), "runtime-version")
    mut("write surface unargued", prov, lambda e, d: e["typedAuthority"].pop("writeSurfaceArgument"), "not argued")
    mut("unknowns emptied", prov, lambda e, d: e.update(unknowns=[]), "lists no Unknown")
    mut("acceptance admits any byte", prov, lambda e, d: e["routeConditions"].update(acceptanceCheck="any byte passes"), "acceptanceCheck")
    mut("egress version dropped", prov, lambda e, d: e["routeConditions"].update(source="record PUBLIC-EGRESS-anthropic, any version"), "egress record")
    mut("profile-set model unpinned", prov, lambda e, d: e["requestBytes"]["routeFixedByThisEntry"].pop("model"), "does not pin")
    mut("max_tokens ceiling unpinned", prov, lambda e, d: e["requestBytes"]["routeFixedByThisEntry"].pop("maxTokensCeiling"), "does not pin")
    mut("runtime-fixed list dropped", prov, lambda e, d: e["requestBytes"].pop("runtimeFixed"), "requestBytes lacks")
    mut("headers list dropped", prov, lambda e, d: e["requestBytes"].pop("headers"), "requestBytes lacks")
    mut("request bytes pin other versions", prov, lambda e, d: e["requestBytes"]["pinnedVersions"].update(version="0.3.289"), "other versions")
    mut("readAuthority stops pointing at requestBytes", prov,
        lambda e, d: e["typedAuthority"].update(readAuthority="none"), "readAuthority")
    mut("scalar determinism unexplained", src, lambda e, d: e.pop("determinismClassNote"), "unexplained")
    mut("input class unmapped", prov, lambda e, d: e["snapshotInputMapping"].pop("run-budget"), "omits input classes")
    mut("full-history fetch", src, lambda e, d: e["typedAuthority"].update(fetch="git clone <upstream>"), "fetch")
    mut("fetch loses --no-tags", src,
        lambda e, d: e["typedAuthority"].update(fetch=e["typedAuthority"]["fetch"].replace("--no-tags ", "")), "fetch")
    mut("fetch adds all tags", src,
        lambda e, d: e["typedAuthority"].update(fetch=e["typedAuthority"]["fetch"].replace(": one", " --tags: one")), "fetch")
    mut("fetch widened after the colon", src,
        lambda e, d: e["typedAuthority"].update(fetch=e["typedAuthority"]["fetch"] + " and all tags and full history"), "fetch")
    mut("limit without semantics", src, lambda e, d: e["resourceLimits"].update(maxIndexDepth=16), "no semantics")
    with tempfile.TemporaryDirectory() as t:
        root = pathlib.Path(t) / "pkg"
        (root / "proposed").mkdir(parents=True)
        inst = pathlib.Path(t) / "installed"
        inst.mkdir()
        for p in proposed():
            (root / "proposed" / p.name).write_bytes(p.read_bytes())
        (root / MANIFEST).write_text(manifest_text(root))
        muts.append(("clean temp package passes", check(root, BUTLERS, inst) == []))
        victim = next(iter(proposed(root)))
        keep = victim.read_text()
        victim.write_text("{not json")
        muts.append(("proposed file not JSON", any("not JSON" in f for f in check(root, BUTLERS, inst))))
        victim.write_text(keep)
        victim.rename(victim.with_suffix(".moved"))
        muts.append(("one proposed entry missing", any("expected 2" in f for f in check(root, BUTLERS, inst))))
        victim.with_suffix(".moved").rename(victim)
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
