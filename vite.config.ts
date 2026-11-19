import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// GitHub Pages serves the site from /<repo-name>/. Override with BASE_PATH if needed.
export default defineConfig({
  base: process.env.BASE_PATH ?? '/csca-trainer/',
  plugins: [react()],
  build: { chunkSizeWarningLimit: 2500 },
  test: {
    include: ['tests/**/*.test.ts'],
    environment: 'node',
  },
} as any);
