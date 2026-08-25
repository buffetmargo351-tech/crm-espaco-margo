from pathlib import Path


def rep(text, old, new, label):
    if old not in text:
        raise SystemExit(f'PADRAO NAO ENCONTRADO: {label}')
    return text.replace(old, new, 1)

# HOME
p = Path('home.html')
s = p.read_text(encoding='utf-8')
old = '''    function contarEmpresasDaCHO(retornoOportunidades) {
      return unificarTodasOportunidadesHome(retornoOportunidades).filter(casal => {
        const status = normalizarStatus(casal.status_casal);
        if (temVisitaAgendada(casal)) return false;
        if (status === "PERDIDO" || status === "GANHO") return false;
        return ehCorporativo(casal);
      }).length;
    }
'''
new = '''    function contarEmpresasDaCHO(retornoOportunidades, casaisNovosApi = []) {
      const mapa = new Map();
      [
        ...unificarTodasOportunidadesHome(retornoOportunidades || {}),
        ...(Array.isArray(casaisNovosApi) ? casaisNovosApi.filter(ehCorporativo) : [])
      ].forEach(casal => {
        if (casal && casal.casal_id) mapa.set(casal.casal_id, casal);
      });

      return Array.from(mapa.values()).filter(casal => {
        const status = normalizarStatus(casal.status_casal);
        if (temVisitaAgendada(casal)) return false;
        if (status === "PERDIDO" || status === "GANHO") return false;
        return ehCorporativo(casal);
      }).length;
    }
'''
s = rep(s, old, new, 'home contarEmpresasDaCHO')
s = rep(s,
'''          if (totalEmpresasHome) totalEmpresasHome.textContent = String(contarEmpresasDaCHO(dadosOportunidades));''',
'''          if (totalEmpresasHome) totalEmpresasHome.textContent = String(contarEmpresasDaCHO(dadosOportunidades, casais));''',
'home chamada contador empresas')
s = rep(s,
'''        } catch (erroOportunidades) {
          console.warn("Não foi possível carregar oportunidades. Novos casais serão exibidos mesmo assim.", erroOportunidades);
        }
''',
'''        } catch (erroOportunidades) {
          console.warn("Não foi possível carregar oportunidades. Novos casais serão exibidos mesmo assim.", erroOportunidades);
          const totalEmpresasHome = document.getElementById("totalEmpresasHome");
          if (totalEmpresasHome) totalEmpresasHome.textContent = String(contarEmpresasDaCHO({}, casais));
        }
''',
'home fallback empresas via crm/casais')
p.write_text(s, encoding='utf-8')

# OPORTUNIDADES
p = Path('oportunidades.html')
s = p.read_text(encoding='utf-8')
s = rep(s,
'''    const API_OPORTUNIDADES = "https://n8n.espacomargo.com.br/webhook/crm/oportunidades";''',
'''    const API_OPORTUNIDADES = "https://n8n.espacomargo.com.br/webhook/crm/oportunidades";
    const API_CASAIS = "https://n8n.espacomargo.com.br/webhook/crm/casais";''',
'oportunidades API_CASAIS')
s = rep(s,
'''    function organizarDadosPorStatus(retorno) {
      const todos = [
        ...(retorno.agendar || []),
        ...(retorno.resgatar || []),
        ...(retorno.agendados || []),
        ...(retorno.encerrados || [])
      ];''',
'''    function extrairListaCasais(dadosCasais) {
      if (Array.isArray(dadosCasais)) return dadosCasais;
      if (dadosCasais && Array.isArray(dadosCasais.casais)) return dadosCasais.casais;
      if (dadosCasais && Array.isArray(dadosCasais.data)) return dadosCasais.data;
      if (dadosCasais && Array.isArray(dadosCasais.items)) return dadosCasais.items;
      if (dadosCasais && dadosCasais.casal_id) return [dadosCasais];
      return [];
    }

    function organizarDadosPorStatus(retorno, casaisNovosApi = []) {
      const todos = [
        ...(retorno.agendar || []),
        ...(retorno.resgatar || []),
        ...(retorno.agendados || []),
        ...(retorno.encerrados || []),
        ...(Array.isArray(casaisNovosApi) ? casaisNovosApi.filter(ehCorporativo) : [])
      ];''',
'oportunidades incluir corporativos NOVO')
s = rep(s,
'''        const resposta = await fetch(API_OPORTUNIDADES + "?t=" + Date.now());
        const retorno = await resposta.json();
        try {''',
'''        const resposta = await fetch(API_OPORTUNIDADES + "?t=" + Date.now());
        const retorno = await resposta.json();

        let casaisNovosApi = [];
        try {
          const rc = await fetch(API_CASAIS + "?t=" + Date.now(), { cache: "no-store" });
          const jc = await rc.json();
          casaisNovosApi = extrairListaCasais(jc);
        } catch (e) {
          console.warn("Não foi possível carregar NOVOS para compor EMPRESAS:", e);
        }

        try {''',
'oportunidades fetch crm/casais')
s = rep(s,
'''        dados = organizarDadosPorStatus(retorno);''',
'''        dados = organizarDadosPorStatus(retorno, casaisNovosApi);''',
'oportunidades chamada organizar')
p.write_text(s, encoding='utf-8')

# PWA CACHE
p = Path('service-worker.js')
s = p.read_text(encoding='utf-8')
s = rep(s,
'''const CACHE_NAME = "crm-margo-pwa-v15-empresas-20260825";''',
'''const CACHE_NAME = "crm-margo-pwa-v16-empresas-novos-20260825";''',
'cache V1.16')
p.write_text(s, encoding='utf-8')

# README
Path('README_V1_16_EMPRESAS_NOVOS.txt').write_text('''V1.16 — EMPRESAS CAPTURA LEADS CORPORATIVOS AINDA EM NOVO\n\nCorreção técnica sobre V1.15:\n- /crm/casais é a fonte dos registros NOVO ainda sem resposta;\n- EMPRESAS agora combina corporativos vindos de /crm/casais com /crm/oportunidades;\n- corporativos NOVO continuam excluídos de NOVOS CASAIS;\n- somente registros corporativos do endpoint /crm/casais são adicionados à tela Oportunidades, evitando alterar filas de casamento;\n- precedência permanece AGENDADOS > EMPRESAS > ATENÇÃO > OPORTUNIDADES;\n- fila EMPRESAS continua compartilhada entre usuários autenticados;\n- cache PWA atualizado para V1.16.\n\nMotivo:\no fluxo corporativo correto nasce como status_casal=NOVO e modo_atendimento_ia=HUMANO. Como a V1.15 montava EMPRESAS apenas com /crm/oportunidades, um lead corporativo recém-chegado poderia ficar invisível até mudar de status.\n''', encoding='utf-8')

# Sanidade
home = Path('home.html').read_text(encoding='utf-8')
opp = Path('oportunidades.html').read_text(encoding='utf-8')
assert 'contarEmpresasDaCHO(dadosOportunidades, casais)' in home
assert 'contarEmpresasDaCHO({}, casais)' in home
assert 'const API_CASAIS = "https://n8n.espacomargo.com.br/webhook/crm/casais";' in opp
assert 'casaisNovosApi.filter(ehCorporativo)' in opp
assert 'organizarDadosPorStatus(retorno, casaisNovosApi)' in opp
print('V1.16 patch OK')
