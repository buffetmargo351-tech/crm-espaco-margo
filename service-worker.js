const CACHE_NAME = "crm-margo-pwa-v4-midia-manual-20260807";
const ARQUIVOS_CACHE = [
  "./",
  "home.html",
  "atendimento.html",
  "manifest.json",
  "icons/icon-192.png",
  "icons/icon-512.png"
];

self.addEventListener("install", function (event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function (cache) {
      return cache.addAll(ARQUIVOS_CACHE);
    }).catch(function () {
      return Promise.resolve();
    })
  );
  self.skipWaiting();
});

self.addEventListener("activate", function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(
        keys
          .filter(function (key) { return key !== CACHE_NAME; })
          .map(function (key) { return caches.delete(key); })
      );
    })
  );
  self.clients.claim();
});

self.addEventListener("fetch", function (event) {
  const request = event.request;
  const url = new URL(request.url);

  if (request.method !== "GET") return;

  // Não cacheia chamadas externas/API.
  if (url.origin !== self.location.origin) return;

  event.respondWith(
    fetch(request)
      .then(function (response) {
        const copia = response.clone();
        caches.open(CACHE_NAME).then(function (cache) {
          cache.put(request, copia);
        });
        return response;
      })
      .catch(function () {
        return caches.match(request);
      })
  );
});
