V1.17 — NAVEGAÇÃO EM FILA + CORREÇÃO EMPRESAS

1. Correção EMPRESAS
- Home passa a incorporar retorno.empresas de /crm/oportunidades.
- oportunidades.html passa a incorporar retorno.empresas.
- Lead corporativo já presente na API de oportunidades deixa de ficar invisível no App.

2. Navegação vertical de atendimento
- Atendimento ganha botão ↓ no topo direito.
- O botão abre diretamente o próximo registro da mesma fila.
- Funciona para NOVOS, OPORTUNIDADES/AGENDAR, EMPRESAS, RESGATAR, AGENDADOS, ATENÇÃO e ENCERRADOS.
- A fila é reconstruída pelas APIs reais e preservada em sessionStorage por segurança.
- Ao chegar ao último registro, o botão fica desabilitado.
- A seta ‹ do topo volta para a fila de origem, em vez de obrigar retorno ao menu.
- O botão Início continua levando à Home.

3. Segurança
- Nenhuma mudança em Milene, WhatsApp, n8n, regras de funil ou dados.
- EMPRESAS continua compartilhada; demais filas respeitam usuario_id.
- Cache PWA atualizado para V1.17.
