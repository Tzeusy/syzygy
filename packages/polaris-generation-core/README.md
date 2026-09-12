# Polaris generation core

Pure deterministic generation primitives. No source acquisition, permission
service, provider dispatch, filesystem writes or owner acts live here.

`encodeCanonicalJson(value, limits)` defines `polaris-json-v1`: compact JSON,
UTF-16-sorted object keys, original array order and ECMAScript JSON primitive
spelling. The output uses UTF-8 for size and digest accounting, without Unicode
normalization. Negative zero encodes as zero. Lone surrogates are JSON escapes.
This is a local versioned encoding, not a claim of RFC 8785 conformance.

Every call supplies positive safe-integer byte and node limits and a depth limit
from 0 through 256. Root depth is zero; every value occurrence counts as a node.
Shared objects count at each occurrence. Cycles, sparse arrays, non-finite numbers,
non-JSON primitives, proxies, custom prototypes, accessors, symbol/hidden fields,
extra array fields and `__proto__`/`constructor`/`prototype` object keys are refused.
Plain and null-prototype data objects are supported. Diagnostics contain only
bounded error codes, never input values or keys.

`digestCanonicalJson` hashes those exact bytes using SHA-256 and returns the
encoding and algorithm alongside the digest. It performs no I/O. Canonical shape
validation does not validate a generator schema, resolve an identity, establish
source fidelity or authorize any effect. Callers must first use a bounded parser
that rejects duplicate keys; duplicate keys cannot be recovered from an already
parsed JavaScript object. Schema validation remains a separate obligation.
