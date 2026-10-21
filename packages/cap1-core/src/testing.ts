// Test-support entry point, `@syzygy/cap1-core/testing`. Nothing here is
// reachable from the package barrel (index.ts) or from any production
// module: the conformance suite and the daemon's route tests import it
// explicitly, so production code carries only what the daemon runs.
//
// - parity-oracle.ts: the independent cross-channel parity oracle
//   (CAP1-REQ-041, CAP1-REQ-043).
// - write-boundary.ts: the CAP1-REQ-061 write-boundary reference model.
export * from './parity-oracle.js';
export * from './write-boundary.js';
