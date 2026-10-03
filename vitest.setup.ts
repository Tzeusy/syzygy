import { beforeEach } from 'vitest';

// Vitest runs a file's tests back to back without yielding to the event
// loop, so a file of synchronous tests is one long macrotask. The worker
// answers its parent over an RPC whose calls time out after a fixed 60 s, and
// a reply can only be read when the loop turns: a file whose synchronous
// tests summed past 60 s under load failed the run with "Timeout calling
// onTaskUpdate" though every test passed (syzygy-w90k). One loop turn before
// each test lets pending replies land, so only a single test that blocks for
// 60 s can still starve the RPC; sync-child-process-guard.test.ts keeps long
// child processes out of that position.
beforeEach(() => new Promise<void>((resolve) => setImmediate(resolve)));
