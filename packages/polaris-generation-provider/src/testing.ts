/** Test support, imported by tests and testkits only. `LOOPBACK_FOR_TESTS` is what lets a gate forward to a loopback
 * upstream; production code must not import this module, and a scan in egress-gate.test.ts fails the build if it does. */
export { LOOPBACK_FOR_TESTS } from './egress-gate.js';
export { startCaptureEndpoint, type CaptureEndpoint, type Script } from './capture-endpoint.testkit.js';
