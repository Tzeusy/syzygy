import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vitest/config';

export default defineConfig({
  resolve: {
    alias: {
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
    projects: [
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
