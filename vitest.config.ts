import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vitest/config';

export default defineConfig({
  resolve: {
    alias: {
      '@syzygy/polaris-generation-core': fileURLToPath(new URL('./packages/polaris-generation-core/src/index.ts', import.meta.url)),
      '@syzygy/polaris-generation-consent/testing': fileURLToPath(new URL('./packages/polaris-generation-consent/src/testing.ts', import.meta.url)),
      '@syzygy/polaris-generation-consent': fileURLToPath(new URL('./packages/polaris-generation-consent/src/index.ts', import.meta.url)),
      '@syzygy/polaris-dossier': fileURLToPath(new URL('./packages/polaris-dossier/src/index.ts', import.meta.url)),
      '@syzygy/cap1-core': fileURLToPath(
        new URL('./packages/cap1-core/src/index.ts', import.meta.url),
      ),
      '@syzygy/cap1-daemon': fileURLToPath(
        new URL('./packages/cap1-daemon/src/index.ts', import.meta.url),
      ),
      '@syzygy/three-surface-poc-core': fileURLToPath(
        new URL('./packages/three-surface-poc-core/src/index.ts', import.meta.url),
      ),
    },
  },
  test: {
    // Half the cores (syzygy-w90k): several lanes run their suites on one
    // host, and a worker per core oversubscribed it. Vitest takes the bound
    // only here, for every project; a project may set no worker count.
    maxWorkers: '50%',
    setupFiles: [fileURLToPath(new URL('./vitest.setup.ts', import.meta.url))],
    projects: [
      {
        extends: true,
        test: {
          name: '@syzygy/polaris-generation-core',
          include: ['packages/polaris-generation-core/src/**/*.test.ts'],
        },
      },
      {
        extends: true,
        test: {
          name: '@syzygy/polaris-generation-consent',
          include: ['packages/polaris-generation-consent/src/**/*.test.ts'],
        },
      },
      {
        extends: true,
        test: {
          name: '@syzygy/polaris-dossier',
          include: ['packages/polaris-dossier/src/**/*.test.ts'],
        },
      },
      {
        extends: true,
        test: {
          name: '@syzygy/cap1-conformance',
          include: ['packages/cap1-conformance/src/**/*.test.ts'],
        },
      },
      {
        extends: true,
        test: {
          name: '@syzygy/cap1-daemon',
          include: ['packages/cap1-daemon/src/**/*.test.ts'],
        },
      },
      {
        extends: true,
        test: {
          name: '@syzygy/three-surface-poc-core',
          include: ['packages/three-surface-poc-core/src/**/*.test.ts'],
        },
      },
      {
        extends: true,
        test: {
          name: '@syzygy/three-surface-poc-app',
          include: ['apps/three-surface-poc/src/**/*.test.ts'],
        },
      },
    ],
  },
});
