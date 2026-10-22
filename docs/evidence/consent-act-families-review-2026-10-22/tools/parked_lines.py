"""Changed (+/-) lines of package-reader.ts in the subject diff that name a parked-egress identifier or carry a 64-hex digest.
argv[1] = the diff."""
import re
import sys

NAMES = ['EGRESS_V2_INSTANCE', 'V2_REVOCATION', 'readInForceEgress', "'egress-consent'", 'OWNER_ANSWERS_SHA256', 'HISTORICAL_POLICY_ACTS']
cur, changed, hits = None, 0, []
for line in open(sys.argv[1], encoding='utf-8'):
    if line.startswith('diff --git '):
        cur = line.split(' b/')[-1].strip()
        continue
    if cur != 'packages/polaris-generation-consent/src/package-reader.ts' or line.startswith(('+++', '---')):
        continue
    if line[:1] in '+-':
        changed += 1
        if any(n in line for n in NAMES) or re.search(r'[0-9a-f]{64}', line):
            hits.append(line.rstrip('\n')[:160])
print('changed package-reader.ts lines', changed, 'hits', len(hits))
for h in hits:
    print(' ', h)
