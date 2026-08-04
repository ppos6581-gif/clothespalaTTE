const CACHE_NAME = 'palette-vr-cache-v1';
const ASSETS = [
  '/',
  '/index.html',
  '/manifest.json',
  'https://tailwindcss.com',
  'https://jsdelivr.net',
  'https://jsdelivr.net'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log('App Core Cache opened successfully.');
      return cache.addAll(ASSETS);
    })
  );
});

self.addEventListener('fetch', (e) => {
  // Let external Netlify serverless execution requests bypass local cache
  if (e.request.url.includes('/.netlify/functions/')) return;
  e.respondWith(
    caches.match(e.request).then(cached => cached || fetch(e.request))
  );
});
