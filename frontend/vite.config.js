import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  base: '/', // ✅ مهم جداً للمسارات المطلقة
  server: {
    https: false,
    proxy: {
      '/auth': {
        target: 'https://localhost:443',
        changeOrigin: true,
        secure: false,
      },
    },
  },
});


