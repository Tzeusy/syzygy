import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';

import * as daemon from '@syzygy/cap1-daemon';

interface PackageManifest {
  readonly exports?: {
    readonly '.': string | {
      readonly types?: string;
      readonly import?: string;
      readonly default?: string;
    };
  };
}

const manifest = JSON.parse(
  readFileSync(new URL('../package.json', import.meta.url), 'utf8'),
) as PackageManifest;

describe('cap1-daemon package', () => {
  it('is importable with built runtime and declaration entries', () => {
    expect(daemon).toBeDefined();
    expect(manifest.exports?.['.']).toEqual({
      types: './dist/index.d.ts',
      import: './dist/index.js',
      default: './dist/index.js',
    });
  });

  // The generic host moved to @syzygy/http-host (syzygy-bpyt.7.3). The barrel re-exports it, so a consumer finds every value it
  // found before, and no other: the list is the barrel's runtime names at 9b539e5f.
  it('exports the values it exported before the host moved out', () => {
    expect(Object.keys(daemon).sort()).toEqual([
      'CONSENT_DECISIONS_RELATIVE_PATH', 'CONSENT_RECORD_EXTENSION', 'CONSENT_RECORD_FIELDS', 'CREDENTIAL_FILE_MODE',
      'CREDENTIAL_FILE_NAME', 'CREDENTIAL_TOKEN_BYTES', 'DAEMON_HOST', 'DAEMON_SCENARIO_CONTEXT', 'DECLARATION_RELATIVE_PATH',
      'HANDLER_FAILURE_REASON', 'HANDLER_FAILURE_STATUS', 'HUMAN_ENTRY_ROUTE_PATH', 'HUMAN_PAGE_PATH', 'MACHINE_CONTENT_TYPE',
      'MACHINE_PROJECT_PATH', 'README_RELATIVE_PATH', 'REFUSAL_BODY', 'REFUSAL_STATUS', 'REPOSITORY_ROOT_SCOPE',
      'STATE_DIR_MODE', 'STATE_WRITE_REFUSALS', 'UNKNOWN_ROUTE_REASON', 'UNKNOWN_ROUTE_STATUS', 'authorizeStateWrite',
      'createDaemon', 'credentialFromAuthorizationHeader', 'ensureCredential', 'escapeHtml', 'evaluateProject',
      'factsFromAnswers', 'humanRoutes', 'loadConsentReference', 'loadConsentReferences', 'machineProjectBody', 'machineRoutes',
      'minimalRootRoute', 'observeDeclaration', 'observeReadmeEvidence', 'observeRepositorySnapshot', 'observeRootCandidate',
      'resolveConsentReferencePath', 'verifyCredential',
    ]);
  });
});
