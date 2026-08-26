const CACHE_NAME = "crm-margo-pwa-v17-1-hotfix-empresas-atencao-20260826";
const ARQUIVOS_CACHE = [
  "./",
  "home.html",
  "atendimento.html",
  "oportunidades.html",
  "manifest.json",
  "icons/icon-192.png",
  "icons/icon-512.png"
];

function aplicarHotfixEmpresas(html, pathname) {
  let saida = html;

  if (pathname.endsWith("/oportunidades.html") || pathname.endsWith("oportunidades.html")) {
    // Leads corporativos ficam em modo HUMANO e podem vir agrupados em `atencao`
    // pelo endpoint /crm/oportunidades. A V1.17 não incluía esse grupo ao montar EMPRESAS.
    saida = saida.replace(
      "        ...(retorno.agendados || []),\n        ...(retorno.empresas || []),\n        ...(retorno.encerrados || []),",
      "        ...(retorno.agendados || []),\n        ...(retorno.empresas || []),\n        ...(retorno.atencao || []),\n        ...(retorno.encerrados || []),"
    );

    // Preserva explicitamente a fila de origem para a navegação vertical dentro de EMPRESAS.
    saida = saida.replace(
      '        card.onclick = () => window.location.href = urlComUsuario("atendimento.html?casal_id=" + encodeURIComponent(casal.casal_id));',
      '        card.onclick = () => window.location.href = urlComUsuario("atendimento.html?casal_id=" + encodeURIComponent(casal.casal_id) + "&fila=" + encodeURIComponent(tipo));'
    );
  }

  if (pathname.endsWith("/home.html") || pathname.endsWith("home.html") || pathname === "/") {
    // Mantém a contagem EMPRESAS consistente com a tela: inclui corporativos HUMANO vindos em `atencao`.
    saida = saida.replace(
      "        ...(retornoOportunidades.agendados || []),\n        ...(retornoOportunidades.empresas || [])",
      "        ...(retornoOportunidades.agendados || []),\n        ...(retornoOportunidades.empresas || []),\n        ...(retornoOportunidades.atencao || [])"
    );
  }

  return saida;
}

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

  // Não intercepta chamadas externas/API.
  if (url.origin !== self.location.origin) return;

  const ehHtmlComHotfix =
    url.pathname.endsWith("/oportunidades.html") ||
    url.pathname.endsWith("/home.html") ||
    url.pathname === "/";

  if (ehHtmlComHotfix) {
    event.respondWith(
      fetch(request, { cache: "no-store" })
        .then(async function (response) {
          if (!response.ok) return response;
          const html = await response.text();
          const corrigido = aplicarHotfixEmpresas(html, url.pathname);
          const headers = new Headers(response.headers);
          headers.delete("content-length");
          headers.set("Cache-Control", "no-store");
          return new Response(corrigido, {
            status: response.status,
            statusText: response.statusText,
            headers
          });
        })
        .catch(function () {
          return caches.match(request);
        })
    );
    return;
  }

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
