"""Sweep every tracked code file of the repo at argv[1] for imports of package-reader.ts (relative) or of the
@syzygy/polaris-generation-consent package (bare, any subpath), or for a path string naming the package's src/dist.
Prints the denominator (files scanned by extension), every hit, and the readers each hit names."""
import collections
import re
import subprocess
import sys

repo = sys.argv[1]
files = subprocess.run(['git', '-C', repo, 'ls-files', '-z'], check=True, capture_output=True).stdout.decode().split('\0')
exts = ('.ts', '.tsx', '.mts', '.cts', '.js', '.mjs', '.cjs', '.py', '.sh', '.json', '.yml', '.yaml')
scan = [f for f in files if f.endswith(exts) and not f.startswith('docs/evidence/')]
by_ext = collections.Counter(f.rsplit('.', 1)[-1] for f in scan)
print('tracked files', len([f for f in files if f]), 'scanned', len(scan), dict(by_ext))
pat_bare = re.compile(r"""['"]@syzygy/polaris-generation-consent(?:/[^'"]*)?['"]""")
pat_rel = re.compile(r"""['"](?:\.{1,2}/)+(?:[^'"]*/)?package-reader(?:\.js|\.ts)?['"]""")
pat_path = re.compile(r"polaris-generation-consent/(?:src|dist)/")
symbols = ['createPackageAdmissionReader', 'createPackagePolicyReader', 'readPolicyActChain', 'readClassActState', 'readInForceEgress',
           'readDigestBoundActState', 'readVersionedSignoffState', 'createPackageAdmissionRecordsPort', 'createAdmissionRecordsPort',
           'POLICY_ACT_FORMS', 'ADMISSION_ACT_FORMS', 'REGISTRY_GIT_SOURCE_ACT_FORM', 'LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM']
hits = []
for f in scan:
    try:
        text = open(f'{repo}/{f}', encoding='utf-8').read()
    except (UnicodeDecodeError, FileNotFoundError, IsADirectoryError):
        continue
    kinds = []
    if pat_bare.search(text):
        kinds.append('bare')
    if pat_rel.search(text) and f.startswith('packages/polaris-generation-consent/'):
        kinds.append('relative')
    if pat_path.search(text):
        kinds.append('path')
    if kinds:
        used = [s for s in symbols if re.search(r'\b' + s + r'\b', text)]
        hits.append((f, kinds, used))
print('hits', len(hits))
for f, kinds, used in hits:
    print(f'  {f}  [{",".join(kinds)}]  {" ".join(used)}')
for target in ('apps/three-surface-poc/src/governance-inputs.ts', 'apps/three-surface-poc/src/production-reobserve.ts',
               'packages/three-surface-poc-core/src/body-read-authority.ts'):
    print('PWB path file', target, 'is a hit:', any(h[0] == target for h in hits))
core = [h for h in hits if h[0].startswith('packages/three-surface-poc-core/')]
print('three-surface-poc-core hits:', len(core))
